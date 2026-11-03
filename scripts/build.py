#!/usr/bin/env python3
"""Rebuild docs/ from sites/ and home/.

GitHub Pages serves the master branch /docs folder. This script is what
keeps that folder in sync with the Hugo (and static) sources. It does not
change the repository's Pages settings.
"""

from __future__ import annotations

import html
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / ".docs-build"
DOCS = ROOT / "docs"
REGISTRY = ROOT / "sites" / "registry.toml"
LEGACY = ROOT / "scripts" / "legacy-redirects.txt"
HUGO_NEEDLE = "v0.165.0"
SITE_ORIGIN = "https://b-lindsey.github.io"


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    sys.exit(1)


def hugo_version() -> str:
    try:
        out = subprocess.check_output(["hugo", "version"], text=True)
    except FileNotFoundError:
        fail("hugo is not on PATH. Install Hugo extended v0.165.0.")
    if HUGO_NEEDLE not in out or "+extended" not in out:
        fail(
            "Need Hugo extended v0.165.0 so the Blowfish assets match the "
            f"committed site.\nFound: {out.strip()}"
        )
    return out.strip()


def load_sites() -> list[dict]:
    data = tomllib.loads(REGISTRY.read_text())
    sites = data.get("site") or []
    if not sites:
        fail(f"No [[site]] entries in {REGISTRY}")
    seen = set()
    for site in sites:
        site_id = site.get("id", "")
        builder = site.get("builder", "")
        if not site_id or "/" in site_id or site_id.startswith("."):
            fail(f"Invalid site id: {site_id!r}")
        if site_id in seen:
            fail(f"Duplicate site id: {site_id}")
        seen.add(site_id)
        if builder not in {"hugo", "static"}:
            fail(f"{site_id}: builder must be 'hugo' or 'static'")
        for key in ("title", "kicker", "summary"):
            if not str(site.get(key, "")).strip():
                fail(f"{site_id}: missing {key}")
        src = ROOT / "sites" / site_id
        if not src.is_dir():
            fail(f"{site_id}: missing source directory {src}")
    return sites


def build_hugo(site_id: str, dest: Path) -> None:
    src = ROOT / "sites" / site_id
    if dest.exists():
        shutil.rmtree(dest)
    cmd = [
        "hugo",
        "--minify",
        "--gc",
        "--destination",
        str(dest),
    ]
    print(f"hugo {site_id} -> {dest.relative_to(ROOT)}")
    subprocess.run(cmd, cwd=src, check=True)
    # Cache and preview output stay out of git.
    for leftover in (src / "resources", src / "public", src / ".hugo_build.lock"):
        if leftover.is_dir():
            shutil.rmtree(leftover)
        elif leftover.exists():
            leftover.unlink()


def build_static(site_id: str, dest: Path) -> None:
    src = ROOT / "sites" / site_id
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(
        src,
        dest,
        ignore=shutil.ignore_patterns(".git", ".DS_Store", "README.md"),
    )


def write_home(sites: list[dict]) -> None:
    template = (ROOT / "home" / "index.template.html").read_text()
    cards = []
    for site in sites:
        href = site.get("href") or f"/{site['id']}/"
        cards.append(
            "      <li>\n"
            f'        <a class="card" href="{html.escape(href, quote=True)}">\n'
            f'          <span class="kicker">{html.escape(site["kicker"])}</span>\n'
            f'          <span class="title">{html.escape(site["title"])}</span>\n'
            f'          <span class="summary">{html.escape(site["summary"])}</span>\n'
            '          <span class="more">Open site</span>\n'
            "        </a>\n"
            "      </li>"
        )
    block = "\n".join(cards)
    if "<!-- SITES -->" not in template:
        fail("home/index.template.html is missing <!-- SITES -->")
    home = template.replace("<!-- SITES -->", block)
    (STAGING / "index.html").write_text(home)
    shutil.copyfile(ROOT / "home" / "404.html", STAGING / "404.html")
    shutil.copyfile(ROOT / "home" / "robots.txt", STAGING / "robots.txt")
    shutil.copyfile(ROOT / "home" / "sitemap.xml", STAGING / "sitemap.xml")
    shutil.copyfile(ROOT / "home" / "favicon.svg", STAGING / "favicon.svg")
    assets = STAGING / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / "home" / "home.css", assets / "home.css")
    (STAGING / ".nojekyll").write_text("")


def write_redirects() -> None:
    paths = [
        line.strip().strip("/")
        for line in LEGACY.read_text().splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    for rel in paths:
        target_path = f"/crossfire-pro/{rel}/"
        target_url = f"{SITE_ORIGIN}{target_path}"
        page = (
            "<!DOCTYPE html>\n"
            '<html lang="en">\n'
            "<head>\n"
            '<meta charset="utf-8">\n'
            '<meta name="robots" content="noindex">\n'
            f'<link rel="canonical" href="{html.escape(target_url, quote=True)}">\n'
            f'<meta http-equiv="refresh" content="0; url={html.escape(target_path, quote=True)}">\n'
            "<title>Moved</title>\n"
            f'<script>location.replace("{target_path}" + location.search + location.hash);</script>\n'
            "</head>\n"
            "<body>\n"
            "<p>This page has moved to "
            f'<a href="{html.escape(target_path, quote=True)}">{html.escape(target_url)}</a>.</p>\n'
            "</body>\n"
            "</html>\n"
        )
        dest = STAGING / rel / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page)
    print(f"redirects {len(paths)}")


def swap_docs() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    STAGING.rename(DOCS)


def main() -> None:
    print(hugo_version())
    sites = load_sites()
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir()
    try:
        for site in sites:
            dest = STAGING / site["id"]
            if site["builder"] == "hugo":
                build_hugo(site["id"], dest)
            else:
                build_static(site["id"], dest)
        write_home(sites)
        write_redirects()
        swap_docs()
    except Exception:
        if STAGING.exists():
            shutil.rmtree(STAGING)
        raise
    print(f"wrote {DOCS}")


if __name__ == "__main__":
    main()
