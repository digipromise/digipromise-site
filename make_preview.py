"""Inline assets so a built page renders standalone: python3 make_preview.py <page.html> <out.html>"""
import re, sys, os, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B
src, out = sys.argv[1], sys.argv[2]
A = B.ASSET; AD = os.path.join(B.PAGES, 'assets')
h = open(src).read()
for f in ['dp.css', 'widget.css', 'dp-motion.css', 'dp-rtl.css']:
    css = open(os.path.join(AD, f)).read().replace('url(inter.woff2)', 'url(https://cdn.jsdelivr.net/npm/@fontsource-variable/inter/files/inter-latin-wght-normal.woff2)')
    h = re.sub(r'<link rel="stylesheet" href="' + re.escape(A + f) + r'[^>]*>', lambda m: '<style>' + css + '</style>', h)
for f in ['dp.js', 'widget.js', 'dp-motion.js']:
    js = open(os.path.join(AD, f)).read()
    h = re.sub(r'<script src="' + re.escape(A + f) + r'[^"]*" defer></script>', lambda m: '<script>' + js + '</script>', h)
logo = 'data:image/webp;base64,' + base64.b64encode(open(os.path.join(AD, 'logo-96.webp'), 'rb').read()).decode()
h = h.replace(A + 'logo-96.webp', logo).replace(f'<link rel="preload" href="{A}inter.woff2" as="font" type="font/woff2" crossorigin>', '')
h = h.replace('/wp-content/themes/aimo/dp-pages/assets/', '').replace('url(https://cdn.jsdelivr.net/npm/@fontsource-variable/inter/files/inter-latin-wght-normal.woff2)', 'url(inter.woff2)')
open(out, 'w').write(h); print(out, len(h))
