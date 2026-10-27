# digipromise.com — site source

Static EN + AR pages for digipromise.com, served inside the WordPress theme `aimo` via `dp-router.php`.

## Layout
- `build.py` — builds every page into `dist/dp-pages/` (`LIVE=1` for production)
- `build_home_v2.py` — homepage
- `build_wpchrome.py` — header/footer used on WordPress (blog) pages
- `build_parts.py`, `i18n.py`, `plans_extra.py`, `pricing-v2.json` — shared parts, translations, prices
- `content/` (EN) and `content_ar/` (AR) — one file per page
- `partials_widget.html` — Digi chat widget markup
- `dist/dp-pages/assets/` — CSS, JS (dp.js, widget.js are edited here directly), images, fonts
- `docs/site-deploy-runbook.md` — how to deploy (read this first)

## Build (needs Python 3)
```
LIVE=1 python3 build.py
python3 build_home_v2.py
python3 build_wpchrome.py
cd dist && zip -qr dp-live-vN.zip dp-router.php dp-pages
```
Then follow docs/site-deploy-runbook.md (backup → upload to themes/aimo → extract → purge Cloudflare → verify).
