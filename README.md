# Bernie Lindsey

Personal project sites published at <https://b-lindsey.github.io/>.

The root of the site is a short home page. Each project is a subfolder. The first one is [CrossFire PRO Procedures & Reference](https://b-lindsey.github.io/crossfire-pro/).

## Layout

```
sites/registry.toml          home-page cards, in order
sites/crossfire-pro/         Hugo source for the CrossFire site
home/                        home page, 404 page, and stylesheet
scripts/build.sh             rebuilds docs/
scripts/legacy-redirects.txt old CrossFire URLs that redirect
docs/                        what GitHub Pages serves
  index.html                 home page
  404.html
  assets/home.css
  crossfire-pro/             built CrossFire site
  procedures/, firecontrol/, …   redirects into /crossfire-pro/
```

GitHub Pages serves this repository from the `master` branch, `/docs` folder. `docs/.nojekyll` keeps Jekyll from rewriting the built files. Nothing in the repository settings has to change for that to keep working.

The CrossFire site stays out of search indexes: every page has `noindex`, and the root `robots.txt` disallows `/crossfire-pro/`. The home page itself does not.

## Rebuild

Install [Hugo extended v0.165.0](https://github.com/gohugoio/hugo/releases/tag/v0.165.0) (`hugo version` should say `v0.165.0` and `+extended`). That is the version the CrossFire site was built with. Blowfish v3.9.0 is a Hugo module (`sites/crossfire-pro/go.mod`), so Go is needed the first time Hugo downloads it.

```bash
./scripts/build.sh
```

Commit both the source and the rebuilt `docs/` folder. A pull request that changes a site without rebuilding `docs/` will fail the Build workflow, which rebuilds and checks that `docs/` matches.

Preview the CrossFire source on its own:

```bash
cd sites/crossfire-pro
hugo server
```

## Add a site

1. Create `sites/<id>/`.
   - Hugo: copy the shape of `sites/crossfire-pro/`. Set `baseURL` to `https://b-lindsey.github.io/<id>/`. Pin the theme the same way (Hugo module or a submodule) so the build does not depend on a theme copy that lives only on one machine.
   - Already-built HTML: put the files in `sites/<id>/` and use `builder = "static"`. The folder is copied to `docs/<id>/` as-is (`README.md` in that folder is not published).
2. Add a `[[site]]` entry at the bottom of `sites/registry.toml` (`id`, `builder`, `kicker`, `title`, `summary`). The card links to `/<id>/`.
3. Run `./scripts/build.sh` and commit.

## Old CrossFire URLs

Pages that used to live at the site root (`/procedures/…`, `/firecontrol/…`, `/testing/…`, `/charts/`, `/sources/`, `/about/`, plus tags and series) are small HTML redirects to the same path under `/crossfire-pro/`. The list is `scripts/legacy-redirects.txt`. GitHub Pages cannot send a real 301 while serving a folder, so these are browser redirects (`meta` refresh and `location.replace`).

Opening an old asset URL directly (`/images/…`, `/css/…`, `/downloads/…`) hits the root 404 page, which sends the browser to `/crossfire-pro/…`. Links inside the rebuilt site already point at `/crossfire-pro/`.

## CrossFire content

Procedures, charts, and the test-cut log live in `sites/crossfire-pro/content/`. After a test session, update the log in both `assets/data/test-cut-log.csv` and `static/downloads/test-cut-log.csv`, set `lastmod` on any page you edit, then rebuild. Details are in `sites/crossfire-pro/DEPLOY.md`.

Image and download paths in the Markdown go through the `relurl` shortcode (or a normal Markdown link) so they pick up the `/crossfire-pro/` base URL.

## Actions deployment

The Build workflow only checks the site. Publishing stays on the `master` `/docs` folder, which needs no settings change.

To publish from Actions instead, switch Settings → Pages → Build and deployment → Source to **GitHub Actions**, and replace the workflow with one that uploads `docs/` (`actions/upload-pages-artifact` and `actions/deploy-pages`). Leave the source as it is unless you make that change.
