import re, subprocess, os, sys, shutil
sys.path.insert(0, '.')
import build as B
pages = [pg for pg in B.load_pages() if pg['url'] != '/dp-test/']
m = {pg['url']: (pg['url'].strip('/').replace('/', '-') or 'home') + '.html' for pg in pages}
m['/'] = 'home.html'; m['/ar/'] = 'ar-home.html'
os.makedirs('preview', exist_ok=True)
for pg in pages:
    src = 'dist/dp-pages/' + (pg['url'].strip('/').replace('/', '-') or 'home') + '.html'
    out = 'preview/' + m[pg['url']]
    subprocess.run(['python3', 'make_preview.py', src, out], check=True, capture_output=True)
    h = open(out).read()
    def rep(mo):
        path, _, frag = mo.group(1).partition('#'); path = path.split('?')[0]
        return 'href="' + (m.get(path, 'home.html') if path else '') + ('#' + frag if frag else '') + '"'
    open(out, 'w').write(re.sub(r'href="(/[^"]*)"', rep, h))
for f in ['inter.woff2', 'noto-arabic.woff2', 'client-amore-atelier.webp', 'client-the-allure.webp', 'founder-avatar.svg', 'founder-robot.webp', 'logo-512.png', 'logo-mark.webp', 'logo-full.webp'] + ['mascot-' + k + '.webp' for k in ('iris','aura','nova','luna','lara','stella','lilia')]:
    shutil.copy('dist/dp-pages/assets/' + f, 'preview/' + f)
print('ok', len(pages))
