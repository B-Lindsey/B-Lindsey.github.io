# Updating the CrossFire PRO site

This folder is the Hugo source for <https://b-lindsey.github.io/crossfire-pro/>.
The repository README at the root explains the folder layout, the home page, and how to rebuild.

Blowfish v3.9.0 is pinned as a Hugo module (`go.mod`, `config/_default/module.toml`).
`baseURL` is `https://b-lindsey.github.io/crossfire-pro/`.

## Rebuild

From the repository root, with Hugo extended 0.165.0:

```bash
./scripts/build.sh
```

That writes the site to `docs/crossfire-pro/` and refreshes the home page and the old-URL redirects. Commit `docs/` with the source change. GitHub Pages serves `master` `/docs`; no repository setting has to change.

To preview just this site:

```bash
hugo server
```

## Keep the procedures site out of search

- Every page has `<meta name="robots" content="noindex, nofollow">` (`robots` in `config/_default/params.toml`).
- `layouts/robots.txt` is published at `/crossfire-pro/robots.txt`. Crawlers only read the host `robots.txt`, so the root file (`home/robots.txt`) is what disallows `/crossfire-pro/`.
- Anyone with the link can still read it.

## Update after test results

Content lives in `content/`:

| What | File |
|---|---|
| Home | `content/_index.md` |
| Procedures 01–10 | `content/procedures/01-…md` … `10-…md` |
| Test-cut program / worksheet / log | `content/testing/` |
| FireControl pages | `content/firecontrol/` |
| Charts | `content/charts.md` (images in `static/images/`) |
| Sources | `content/sources.md` |

After a test session:

1. **Log**: update the CSV and copy it to **both** places:
   - `assets/data/test-cut-log.csv` (makes the table on the Test-Cut Log page)
   - `static/downloads/test-cut-log.csv` (the download link)
   Keep the header row the same. The page reads the column names from it.
2. **Results tables**: fill in the "Bernie's test results" section of the matching procedure (for example `05-razorweld-45-cut-settings.md`), and the chart page if the settings change.
3. Change `lastmod:` in the front matter of each page you edit (format `2026-10-28`). This is the "Last updated" date at the top of the page. If you delete the line, Hugo uses the file's modified time, and a rebuild on another machine can change the date.
4. Run `./scripts/build.sh` from the repository root and commit.

Notes:

- Links between pages use `{{< relref "…" >}}`. A broken reference stops the build with a REF_NOT_FOUND error.
- Images and the CSV download use `{{< relurl "images/…" >}}` or a Markdown link such as `[chart](/images/rw_chart.jpeg)`. Both are prefixed with `/crossfire-pro/` at build time. A raw `src="/images/…"` is not, and the link checker will fail.
- Keep `draft: false` or the page won't be published.
- `content/sources-before-layout-change.md` is an old draft (`draft: true`). It is not published.
- The worksheet prints in landscape (`printLandscape: true`), one session per page. Print from the browser.

`content/` was originally generated from master procedure notes. Edit the Markdown here. Regenerating from those notes would overwrite these files, including the JRWPC45LH manual updates.
