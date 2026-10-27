# Builds the DigiPromise header + footer for pages WordPress still renders itself
# (AI News blog, posts, ROI tool). Output: dp-pages/wp-chrome-head.html, wp-chrome-foot.html,
# assets/dp-chrome.css (dp.css + widget.css scoped under .dpc so the blog content is untouched).
# The router injects the two partials via wp_head / wp_footer. Run after build.py.
import os, re, tinycss2
import build as B

ASSETS = os.path.join(B.PAGES, 'assets')

def scope(css, pre='.dpc'):
    out = []
    for r in tinycss2.parse_stylesheet(css, skip_comments=True, skip_whitespace=True):
        if r.type == 'qualified-rule':
            sel = tinycss2.serialize(r.prelude).strip()
            parts = []
            for s in sel.split(','):
                s = s.strip()
                if not s: continue
                s2 = re.sub(r'^(:root|html|body)(?=[\s\[:.]|$)', pre, s)
                if s2 == s:
                    s2 = pre + ' ' + s
                parts.append(s2)
            out.append(','.join(parts) + '{' + tinycss2.serialize(r.content) + '}')
        elif r.type == 'at-rule' and r.lower_at_keyword in ('media', 'supports') and r.content:
            out.append('@' + r.at_keyword + tinycss2.serialize(r.prelude) + '{' + scope(tinycss2.serialize(r.content), pre) + '}')
        elif r.type == 'at-rule' and r.lower_at_keyword in ('keyframes', 'font-face'):
            out.append(tinycss2.serialize([r]))
    return '\n'.join(out)

def main():
    B.LANG = 'en'
    base = open(os.path.join(ASSETS, 'dp.css')).read() + '\n' + open(os.path.join(ASSETS, 'widget.css')).read()
    css = scope(base)
    # reset the theme's styles inside our bars and keep them above the theme's page title
    css += '''
.dpc{font-family:var(--font);font-size:17px;line-height:1.65;color:var(--ink);position:relative;z-index:9990}
.dpc a{text-decoration:none}.dpc ul{list-style:none;margin:0;padding:0}.dpc h2{margin:0}
.dpc .hdr{position:sticky;top:0}
'''
    open(os.path.join(ASSETS, 'dp-chrome.css'), 'w').write(css)
    head = (f'<meta name="color-scheme" content="only light"><link rel="icon" href="{B.ASSET}favicon.ico?v={B.VER}" sizes="any"><link rel="icon" href="{B.ASSET}favicon-32.png?v={B.VER}" type="image/png" sizes="32x32"><link rel="apple-touch-icon" href="{B.ASSET}apple-touch-icon.png?v={B.VER}">'
            f'<link rel="preload" href="{B.ASSET}inter.woff2" as="font" type="font/woff2" crossorigin>'
            f'<link rel="stylesheet" href="{B.ASSET}dp-chrome.css?v={B.VER}"><link rel="stylesheet" href="{B.ASSET}dp-blog.css?v={B.VER}f">'
            '<style>#pxl-header-elementor,#pxl-footer-elementor,body>#digiLauncher,body>#digiPanel,body>.digi-greet{display:none!important}'
            '#dpc-top{position:sticky;top:0;z-index:9990}</style>\n')
    hdr = B.header({'url': '/'})
    # language switch on blog pages goes to the Arabic homepage
    hdr = hdr.replace('href="/ar/"', 'href="/ar/"')
    foot = B.footer()
    foot = foot.replace('</body></html>', '')
    scripts = re.findall(r'<script[^>]*></script>', foot)
    foot_html = re.sub(r'<script[^>]*></script>', '', foot)
    out = (f'<div class="dpc" id="dpc-top">{hdr}</div>\n<div class="dpc" id="dpc-bottom">{foot_html}</div>\n'
           '<script>(function(){var t=document.getElementById("dpc-top");if(t)document.body.insertBefore(t,document.body.firstChild);'
           '[].forEach.call(document.querySelectorAll("body>#digiLauncher,body>#digiPanel,body>.digi-greet"),function(e){e.remove()})})();</script>\n'
           + '\n'.join(scripts) + '\n')
    open(os.path.join(B.PAGES, 'wp-chrome-head.html'), 'w').write(head)
    open(os.path.join(B.PAGES, 'wp-chrome-foot.html'), 'w').write(out)
    print('wp chrome built', len(css), 'bytes css')

if __name__ == '__main__':
    main()
