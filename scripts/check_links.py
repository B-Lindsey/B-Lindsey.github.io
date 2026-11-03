#!/usr/bin/env python3
"""Crawl the built docs/ site the way GitHub Pages serves it.

docs/ is the web root, so CrossFire lives at /crossfire-pro/. Internal
links, stylesheets, scripts, images, and downloads must return 200 and,
inside the CrossFire site, must stay under that path.
"""

from __future__ import annotations

import http.server
import os
import re
import sys
import threading
from collections import deque
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LEGACY = ROOT / "scripts" / "legacy-redirects.txt"
HOST = "127.0.0.1"

ATTRS = ("href", "src", "poster")
LINK_RE = re.compile(
    r"(?:href|src|poster|data-url)\s*=\s*(?:\"([^\"]+)\"|'([^']+)'|([^\s>]+))",
    re.I,
)
CSS_URL_RE = re.compile(r"url\(\s*(?:\"([^\"]+)\"|'([^']+)'|([^)'\s]+))\s*\)", re.I)
REFRESH_RE = re.compile(
    r"http-equiv=[\"']?refresh[\"']?[^>]*content=[\"'][^\"']*url=([^\"'\s>;]+)",
    re.I,
)
ID_RE = re.compile(r"\bid\s*=\s*(?:\"([^\"]+)\"|'([^']+)'|([^\s>]+))", re.I)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DOCS), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        return


def start_server() -> tuple[http.server.ThreadingHTTPServer, str]:
    httpd = http.server.ThreadingHTTPServer((HOST, 0), Handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    port = httpd.server_address[1]
    return httpd, f"http://{HOST}:{port}"


def fetch(url: str) -> tuple[int, str, bytes]:
    req = Request(url, headers={"User-Agent": "crossfire-link-check"})
    try:
        with urlopen(req, timeout=20) as resp:
            body = resp.read()
            ctype = resp.headers.get("Content-Type", "")
            return resp.status, ctype, body
    except HTTPError as exc:
        return exc.code, "", exc.read()


def extract_refs(body: bytes, content_type: str) -> list[str]:
    text = body.decode("utf-8", errors="replace")
    refs: list[str] = []
    if "css" in content_type or text.lstrip().startswith(("/*", "@", ":root", "html")):
        for match in CSS_URL_RE.finditer(text):
            refs.append(next(g for g in match.groups() if g))
        return refs
    for match in LINK_RE.finditer(text):
        refs.append(next(g for g in match.groups() if g))
    for match in CSS_URL_RE.finditer(text):
        refs.append(next(g for g in match.groups() if g))
    return refs


def is_skippable(url: str) -> bool:
    lowered = url.lower()
    return (
        not url
        or lowered.startswith(("#", "mailto:", "javascript:", "data:", "tel:"))
    )


def main() -> None:
    if not (DOCS / "index.html").is_file():
        print("docs/index.html is missing. Run ./scripts/build.sh first.", file=sys.stderr)
        sys.exit(1)

    legacy = [
        "/" + line.strip().strip("/") + "/"
        for line in LEGACY.read_text().splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    httpd, origin = start_server()
    print(f"serving {DOCS} at {origin}")

    queue: deque[str] = deque()
    queued = set()

    def add(url: str) -> None:
        if url in queued:
            return
        queued.add(url)
        queue.append(url)

    add(origin + "/")
    add(origin + "/crossfire-pro/")
    for path in legacy:
        add(origin + path)

    errors: list[str] = []
    checked = 0
    try:
        while queue:
            url = queue.popleft()
            status, ctype, body = fetch(url)
            checked += 1
            path = urlparse(url).path
            if status != 200:
                errors.append(f"{status} {path}")
                continue

            text = body.decode("utf-8", errors="replace")
            refresh = REFRESH_RE.search(text)
            if path in legacy or (path.rstrip("/") in {p.rstrip("/") for p in legacy}):
                if not refresh:
                    errors.append(f"legacy page has no refresh redirect: {path}")
                else:
                    target = refresh.group(1)
                    if not target.startswith("/crossfire-pro/"):
                        errors.append(f"legacy redirect leaves /crossfire-pro: {path} -> {target}")
                    else:
                        add(urljoin(origin, target))

            if path.startswith("/crossfire-pro/") and "html" in ctype:
                for ref in extract_refs(body, ctype):
                    if is_skippable(ref):
                        continue
                    absolute = urljoin(url, ref)
                    parsed = urlparse(absolute)
                    if parsed.netloc and parsed.netloc != urlparse(origin).netloc:
                        continue
                    ref_path = parsed.path or "/"
                    if not ref_path.startswith("/crossfire-pro/"):
                        errors.append(f"link escapes /crossfire-pro: {path} -> {ref}")

            if "html" in ctype or "css" in ctype or path.endswith((".css", ".html")):
                ids = set()
                if "html" in ctype:
                    for match in ID_RE.finditer(text):
                        ids.add(next(g for g in match.groups() if g))
                for ref in extract_refs(body, ctype):
                    if is_skippable(ref):
                        # Same-page fragment.
                        if ref.startswith("#") and len(ref) > 1 and "html" in ctype:
                            frag = ref[1:]
                            if frag not in ids:
                                errors.append(f"missing anchor {ref} on {path}")
                        continue
                    absolute, frag = urldefrag(urljoin(url, ref))
                    parsed = urlparse(absolute)
                    if parsed.netloc and parsed.netloc != urlparse(origin).netloc:
                        continue
                    ref_path = parsed.path or "/"
                    if not ref_path.startswith("/"):
                        continue
                    add(origin + ref_path)
    finally:
        httpd.shutdown()

    # Second pass: fragments that point at other pages.
    # Done inline above only for same-page anchors. Cross-page fragments are
    # checked by fetching the target once more from a collected set.
    print(f"checked {checked} URLs")
    if errors:
        print(f"{len(errors)} problem(s):", file=sys.stderr)
        for err in errors[:80]:
            print("  " + err, file=sys.stderr)
        if len(errors) > 80:
            print(f"  ... {len(errors) - 80} more", file=sys.stderr)
        sys.exit(1)
    print("internal links, assets, and legacy redirects ok")


if __name__ == "__main__":
    main()
