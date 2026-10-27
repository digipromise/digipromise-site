"""DigiPromise static site builder.
Run: python3 build.py   ->  writes dist/dp-pages/*.html, dist/dp-router.php, dist/dp-pages/dp-sitemap.xml
Every page = shared head + header + <main> sections + footer. Content lives in content/*.py.
"""
import json, html, importlib.util, glob, os, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, 'dist')
PAGES = os.path.join(DIST, 'dp-pages')
SITE = 'https://digipromise.com'
ASSET = '/wp-content/themes/aimo/dp-pages/assets/'
VER = '18'  # bump to bust browser + Cloudflare cache after CSS/JS changes
P = json.load(open(os.path.join(ROOT, 'pricing-v2.json')))
PRODUCTS = {p['id']: p for p in P['products']}
WIDGET = open(os.path.join(ROOT, 'partials_widget.html')).read()
e = html.escape
import i18n
LANG = 'en'   # set per page while building (Arabic content modules set it to 'ar')
def t(k): return i18n.UI[LANG][k]
def L(url):
    # language-aware internal link
    if LANG == 'ar' and url.startswith('/') and not url.startswith('/ar/') and not url.startswith('/wp-content'):
        return '/ar' + url
    return url
def cat(p): return i18n.CAT_AR[p['id']] if LANG == 'ar' else p['category']
def ptitle(p): return i18n.TITLE_AR[p['id']] if LANG == 'ar' else p['title'].split('— ')[1]
def tier_name(tr): return i18n.TIER_AR[tr['id']] if LANG == 'ar' else tr['name']

# ---------- helpers ----------
def money(v, cur):
    if cur == 'AED':
        return f"{v:,.0f} درهم" if LANG == 'ar' else f"AED {v:,.0f}"
    return f"${v:,.2f}" if v % 1 else f"${v:,.0f}"

def dual(v):
    return f'<span class="usd">{money(v["USD"],"USD")}</span><span class="aed">{money(v["AED"],"AED")}</span>'

ICONS = {
    'bolt': '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    'globe': '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
    'chat': '<path d="M21 11.5a8.4 8.4 0 0 1-12.6 7.3L3 21l2.2-5.4A8.5 8.5 0 1 1 21 11.5z"/>',
    'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
}
def icon(n, s=15):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'

TRUST = i18n.UI['en']['trust']   # English default; use trust() for language-aware
def trust(): return t('trust')

def switches():
    aed = 'درهم' if LANG == 'ar' else 'AED'
    return ('<div class="switches"><div class="bill-switch" role="group" aria-label="' + t('billing') + '">'
            '<button data-bill-set="monthly">' + t('monthly') + '</button><button data-bill-set="annual">' + t('annual') + ' <span class="save">' + t('save15') + '</span></button></div>'
            '<div class="cur-switch" role="group" aria-label="' + t('currency') + '"><button data-set="USD">USD</button><button data-set="AED">' + aed + '</button></div></div>')

CK = 'https://engine.digipromise.com/webhook/checkout'
CK_PLANS = ('iris', 'aura', 'nova', 'luna', 'lara')  # Stripe checkout via engine (9 Oct 2026)

def _tier_card(p, tr, cta_url, out=False):
    pid = p['id']; O = i18n.OUT[LANG]
    inc = i18n.INCLUDES_AR[pid][tr['id']] if LANG == 'ar' else tr['includes']
    sep = '، ' if LANG == 'ar' else ', '
    ex = list(O['extras']) if out else i18n.extras(pid, tr['id'], LANG, inc)
    lead = ex.pop(0) if ex and (ex[0].startswith('Everything in') or ex[0].startswith('كل ما في')) else ''
    feats = (f'<li><b>{e(lead)}</b></li>' if lead else '') + ''.join(f'<li>{e(x.strip()[0].upper()+x.strip()[1:])}</li>' for x in inc.split(sep))
    if not out:
        dl = i18n.DASH_AR[tr['id']] if LANG == 'ar' else P['dashboard_levels'][tr['id']]
        feats += f'<li class="no">{t("dash")}</li>' if tr['id'] == 'starter' else f'<li>{e(dl)}</li>'
    feats += ''.join(f'<li>{e(x)}</li>' for x in ex)
    best = ''
    M = i18n.PLANS.get(LANG, {}).get(pid) if not out else None
    if M and tr['id'] in M['lists']:
        items = M['lists'][tr['id']]
        feats = ''.join((f'<li><b>{e(x)}</b></li>' if k == 0 and x.endswith(':') else f'<li>{e(x)}</li>') for k, x in enumerate(items))
        best = f'<p class="best">{e(M["best"][tr["id"]])}</p>'
    fee = p.get('setup_fee', {}).get(tr['id']) or P['billing']['setup_fee'][tr['id']]
    custom = tr['id'] in ('enterprise', 'outx')
    # annual setup fee: Starter fully waived, every other plan 50% off (7 Oct 2026)
    if tr['id'] == 'starter':
        ann = f'<s>{dual(fee)}</s> <span class="free">{t("waived")}</span>'
    else:
        ann = f'<s>{dual(fee)}</s> {dual({k: int(round(v * 0.5)) for k, v in fee.items()})} <span class="free">{t("half")}</span>'
    mo_ = '<small>' + t('mo') + '</small>'
    if custom:
        mo = f'<div class="price">{t("custom")}</div><p class="setup">+ {dual(fee)} {t("one_time")}<br>{t("tailored")}</p>'
        yr = f'<div class="price">{t("custom")}</div><p class="setup">{t("billed_ann")} · {ann}<br>{t("tailored")}</p>'
        btn = t('quote')
    elif tr['id'] == 'scale' and tr.get('from'):
        mo = f'<div class="price"><span class="pre">{t("from")}</span>{dual(tr["price"])}{mo_}</div><p class="setup">+ {dual(fee)} {t("one_time")}<br>{t("depends")}</p>'
        yr = f'<div class="price"><span class="pre">{t("from")}</span>{dual(tr["annual_monthly"])}{mo_}</div><p class="setup">{t("billed_ann")} · {ann}</p>'
        btn = t('quote')
    else:
        mo = f'<div class="price">{dual(tr["price"])}{mo_}</div><p class="setup">+ {dual(fee)} {t("one_time")}</p>'
        yr = (f'<div class="price">{dual(tr["annual_monthly"])}{mo_}</div>'
              f'<p class="setup">{t("billed")} {dual(tr["annual_total"])}{t("yr")} · {ann}</p>')
        btn = t('start') + ' ' + (O['names'][tr['id']] if out else tier_name(tr))
    cust = 'حسب الطلب' if LANG == 'ar' else 'Custom'
    qty = ''
    if out:
        qty = (f'<b>{tr["hours"]:,}</b> {O["hours"]} · <b>{tr["contacts"]:,}</b> {O["contacts"]}' if tr.get('hours') else f'<b>{cust}</b> {O["hours"]}')
    elif 'messages' in tr or 'minutes' in tr:
        k = 'messages' if 'messages' in tr else 'minutes'
        unit = ('رسالة شهرياً' if LANG == 'ar' else 'messages / month') if k == 'messages' else O['min']
        qty = f'<b>{tr[k]:,}</b> {unit}' if tr.get(k) else f'<b>{cust}</b> {unit}'
    if qty: mo += f'<p class="qty">{qty}</p>'; yr += f'<p class="qty">{qty}</p>'
    name = O['names'][tr['id']] if out else tier_name(tr)
    badge = f'<span class="badge">{t("popular")}</span>' if tr['popular'] else ''
    note = ''
    if pid == 'stella':  # UAE line requirement (17 Oct 2026)
        note = ('<p class="tnote">' + ('لعملاء الإمارات: يلزم خط هاتف إماراتي باسم شركتكم (رسوم إعداد ورسوم شهرية إضافية يدفعها العميل لمزوّد الخدمة).' if LANG == 'ar'
                else 'UAE clients: a UAE phone line in your company’s name is required (extra setup + monthly line fees, billed by the provider).') + '</p>')
    return (f'<div class="tier{" pop" if tr["popular"] else ""}">{badge}<h3>{name}</h3>{note}{best}'
            f'<div class="mo">{mo}</div><div class="yr">{yr}</div><ul>{feats}</ul>'
            + (f'<a class="btn {"btn-p" if tr["popular"] else "btn-o"}" data-ck="{pid}-{tr["id"]}" href="{CK}?plan={pid}-{tr["id"]}&amp;billing=monthly&amp;currency=aed">{btn}</a></div>'
               if (pid in CK_PLANS and not out and not custom and not (tr['id'] == 'scale' and tr.get('from'))) else
               f'<a class="btn {"btn-p" if tr["popular"] else "btn-o"}" href="{L(cta_url)}?plan={pid}-{tr["id"]}">{btn}</a></div>'))

def pricing_block(pid, cta_url='/contact/', show_switch=True):
    p = PRODUCTS[pid]
    cards = ''.join(_tier_card(p, tr, cta_url) for tr in p['tiers'])
    if p.get('outbound'):
        O = i18n.OUT[LANG]; g = 'g-' + pid
        outc = ''.join(_tier_card(p, tr, cta_url, out=True) for tr in p['outbound'])
        tiers = (f'<div class="grp-sw" role="group"><button type="button" class="on" data-grp="{g}-in">{O["tabs"][0]}</button><button type="button" data-grp="{g}-out">{O["tabs"][1]}</button></div>'
                 f'<div class="tiers" id="{g}-in">{cards}</div><div class="tiers t3" id="{g}-out" hidden>{outc}</div>')
    else:
        tiers = f'<div class="tiers">{cards}</div>'
    ah, al, an = i18n.ADDONS[LANG]
    per = {'mo': t('mo'), 'once': (' مرة واحدة' if LANG == 'ar' else ' one-time')}
    ads = {a['id']: a for a in P['addons']}
    ids = p.get('addons', ['msgs', 'wa'])
    so = (i18n.PLANS.get(LANG, {}).get(p['id']) or {}).get('starter_only', [])
    sol = ' (للباقة المبتدئة)' if LANG == 'ar' else ' (Starter plan)'
    addons = (f'<div class="addons"><b>{ah}</b>' + ''.join(f'<span>{e(al[i])}{sol if i in so else ""} · <em>{dual(ads[i]["price"])}{per[ads[i]["per"]]}</em></span>' for i in ids) + f'<small>{an}</small></div>') if ids else ''
    return (f'{switches() if show_switch else ""}{tiers}{addons}'
            + (('<p class="price-note"><b>' + ('تشترك في المكالمات الواردة والصادرة معاً؟ تدفع رسوم إعداد واحدة فقط، وهي الأعلى.' if LANG == 'ar' else 'Taking inbound and outbound together? You pay one setup fee, the higher one.') + '</b></p>') if p.get('outbound') else '')
            + f'<p class="price-note"><b>{t("need_premium")}</b> <a href="{L("/contact/")}">{t("tailored_quote")}</a><br>{t("price_note")}</p>')

CLIENTS = [('client-amore-atelier.webp', 'Amore Atelier Dubai', 145, 120), ('client-the-allure.webp', 'The Allure Dubai', 292, 80)]
def client_marquee():
    one = ''.join(f'<img src="{ASSET}{f}" alt="{n}" width="{w}" height="{h}" loading="lazy">' for f, n, w, h in CLIENTS)
    return '<div class="marq"><div class="marq-track">' + one * 6 + '</div></div>'

# ---------- schema ----------
ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": "DigiPromise", "url": SITE + "/",
       "logo": SITE + ASSET + "logo-512.png?v=2", "telephone": "+971554548756", "email": "sales@digipromise.com",
       "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "opens": "10:00", "closes": "18:00"},
       "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"},
       "areaServed": ["AE", "SA", "QA", "KW", "BH", "OM"]}

def product_schema(pid, url):
    p = PRODUCTS[pid]; offers = []
    for t in p['tiers']:
        if t['id'] == 'enterprise': continue
        for c in ('USD', 'AED'):
            offers.append({"@type": "Offer", "name": f'{p["name"]} {t["name"]} (monthly)', "price": t['price'][c],
                           "priceCurrency": c, "url": SITE + url,
                           "priceSpecification": {"@type": "UnitPriceSpecification", "price": t['price'][c],
                                                  "priceCurrency": c, "unitCode": "MON",
                                                  **({"minPrice": t['price'][c]} if t['id'] == 'scale' else {})}})
    # Service (not Product): we sell a managed service, so Google should not treat plans as shop items (8 Oct 2026)
    return {"@type": "Service", "name": p['name'], "description": p['title'], "serviceType": p['title'],
            "provider": {"@id": SITE + "/#org"}, "areaServed": "Worldwide", "url": SITE + url, "offers": offers}

def crumbs_schema(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, **({"item": SITE + u} if u else {})}
        for i, (n, u) in enumerate(crumbs)]}

def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

# ---------- layout ----------
def head(pg):
    graph = [ORG, crumbs_schema(pg['crumbs'])]
    if pg.get('product'): graph.append(product_schema(pg['product'], pg['url']))
    if pg.get('faqs'): graph.append(faq_schema(pg['faqs']))
    graph += pg.get('schema', [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    robots = 'noindex,nofollow' if pg.get('noindex') else 'index,follow,max-image-preview:large'
    url = SITE + pg['url']
    ar = pg['url'].startswith('/ar/')
    en_url = SITE + (pg['url'][3:] if ar else pg['url'])
    ar_url = SITE + (pg['url'] if ar else '/ar' + pg['url'])
    font = (f'<link rel="preload" href="{ASSET}noto-arabic.woff2" as="font" type="font/woff2" crossorigin>' if ar else
            f'<link rel="preload" href="{ASSET}inter.woff2" as="font" type="font/woff2" crossorigin>')
    rtl = f'\n<link rel="stylesheet" href="{ASSET}dp-rtl.css?v={VER}">' if ar else ''
    return f'''<!doctype html>
<html lang="{"ar" if ar else "en"}" dir="{"rtl" if ar else "ltr"}" data-cur="USD" data-bill="monthly">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(pg["title"])}</title>
<meta name="description" content="{e(pg["description"])}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="ar" href="{ar_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="DigiPromise"><meta property="og:locale" content="{"ar_AE" if ar else "en_US"}">
<meta property="og:title" content="{e(pg["title"])}"><meta property="og:description" content="{e(pg["description"])}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}{pg.get("og_image", ASSET + "logo-512.png?v=2")}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#9B3DFF"><meta name="color-scheme" content="only light"><meta name="supported-color-schemes" content="light">
<link rel="icon" href="{ASSET}favicon.ico?v={VER}" sizes="any"><link rel="icon" href="{ASSET}favicon-32.png?v={VER}" type="image/png" sizes="32x32"><link rel="apple-touch-icon" href="{ASSET}apple-touch-icon.png?v={VER}">
<script>(function(){{var d=document.documentElement,c;try{{c=localStorage.getItem('dp_cur')}}catch(e){{}}
if(!c){{var z='';try{{z=Intl.DateTimeFormat().resolvedOptions().timeZone||''}}catch(e){{}}
c=/^Asia\\/(Dubai|Muscat|Riyadh|Qatar|Kuwait|Bahrain)$/.test(z)?'AED':'USD'}}d.setAttribute('data-cur',c);d.classList.add('js')}})();</script>
{font}
<link rel="stylesheet" href="{ASSET}dp.css?v={VER}">{rtl}
<link rel="stylesheet" href="{ASSET}widget.css?v={VER}" media="print" onload="this.media='all'">
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});
var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;
j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-NJZDKDSM');</script>
<script type="application/ld+json">{ld}</script>
</head>
<body data-greet="{e(pg.get("greet") or t("greet"))}">
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NJZDKDSM" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<a class="skip" href="#main">{t("skip")}</a>'''

def header(pg=None):
    items = ''.join(f'<a href="{L(p["url"])}">{e(p["name"])}<small>{e(cat(p))}</small></a>' for p in P['products'])
    url = pg['url'] if pg else '/'
    other = (url[3:] if url.startswith('/ar/') else '/ar' + url)
    return f'''<div class="topbar"><div class="wrap"><span>🪄 <span class="tb-label">{t("tb_label")}</span> <b dir="ltr">2020 – 2026</b></span><span style="display:flex;gap:18px;align-items:center"><a class="lang-sw" href="{other}" hreflang="{t("lang_other_code")}" lang="{t("lang_other_code")}">🌐 {t("lang_other")}</a><span dir="ltr">📞 <a href="tel:+971554548756">+971 554 548 756</a></span></span></div></div>
<header class="hdr"><div class="wrap">
<a class="logo" href="{L("/")}"><img src="{ASSET}logo-mark.webp?v={VER}" alt="DigiPromise" width="59" height="40">DigiPromise</a>
<button class="nav-toggle" aria-label="{t("open_menu")}" aria-expanded="false" aria-controls="nav"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
<nav class="nav" id="nav" aria-label="Main"><div class="dd"><a href="{L("/ai-agents/")}">{t("nav_agents")} ▾</a><div class="dd-menu">{items}</div></div>
<a href="{L("/pricing/")}">{t("nav_pricing")}</a><a href="{L("/client-dashboard/")}">{t("nav_dash")}</a><a href="/category/ai-news/">{t("nav_blog")}</a><a href="{L("/about/")}">{t("nav_about")}</a><a href="{L("/contact/")}">{t("nav_contact")}</a>
<a class="btn btn-p hdr-cta" href="{L("/contact/")}">{t("demo")}</a></nav></div></header>'''

def footer():
    prods = ''.join(f'<li><a href="{L(p["url"])}">{e(p["name"])} · {e(cat(p))}</a></li>' for p in P['products'])
    yr = datetime.date.today().year
    return f'''<footer class="ftr"><div class="wrap"><div class="ftr-grid">
<div><a class="logo ftr-logo" href="{L("/")}"><img src="{ASSET}logo-full.webp?v={VER}" alt="DigiPromise" width="137" height="80" loading="lazy"></a>
<p style="margin-top:12px">{t("ftr_tag")}<br>{t("ftr_loc")} · <a href="tel:+971554548756" dir="ltr">+971 554 548 756</a><br><a href="mailto:sales@digipromise.com">sales@digipromise.com</a></p></div>
<div><h2 class="ftr-h">{t("ftr_agents")}</h2><ul>{prods}</ul></div>
<div><h2 class="ftr-h">{t("ftr_services")}</h2><ul><li><a href="{L("/ai-employees/")}">{t("ai_emp")}</a></li><li><a href="{L("/ai-chatbot-development/")}">{t("chatbot_dev")}</a></li><li><a href="{L("/whatsapp-automation/")}">{t("wa_auto")}</a></li><li><a href="{L("/pricing/")}">{t("nav_pricing")}</a></li><li><a href="{L("/client-dashboard/")}">{t("nav_dash")}</a></li></ul></div>
<div><h2 class="ftr-h">{t("ftr_company")}</h2><ul><li><a href="{L("/about/")}">{t("nav_about")}</a></li><li><a href="{L("/contact/")}">{t("nav_contact")}</a></li><li><a href="/category/ai-news/">{t("nav_blog")}</a></li><li><a href="{L("/affiliate-program/")}">{t("nav_aff")}</a></li><li><a href="{L("/faqs/")}">{t("faqs")}</a></li><li><a href="{L("/refund-policy/")}">{t("refund")}</a></li><li><a href="{L("/privacy-policy/")}">{t("privacy")}</a></li><li><a href="/data-deletion-policy/">{t("deletion")}</a></li></ul></div></div>
<div class="ftr-bottom"><span>© {yr} {t("rights")}</span><span>English · العربية</span></div></div></footer>
{WIDGET}
<script src="{ASSET}dp.js?v={VER}" defer></script>
<script src="{ASSET}widget.js?v={VER}" defer></script>
</body></html>'''

def breadcrumb_html(crumbs):
    li = ''.join(f'<li><a href="{u}">{e(n)}</a></li>' if u and i < len(crumbs) - 1 else f'<li aria-current="page">{e(n)}</li>'
                 for i, (n, u) in enumerate(crumbs))
    return f'<nav class="crumb" aria-label="Breadcrumb"><ol>{li}</ol></nav>'

# ---------- section renderers (pages pick and order these) ----------
def s_hero(pg, h):
    pills = ''.join(f'<span>{icon(i)}{t}</span>' for i, t in h.get('trust', TRUST))
    def ps(kind, label, items):
        lis = ''.join(f'<li><span aria-hidden="true">{ic}</span>{e(t)}</li>' for ic, t in items)
        mark = '❌' if kind == 'problem' else '✅'
        return f'<div class="ps-card {kind}"><div class="ps-label">{mark} {e(label)}</div><ul>{lis}</ul></div>'
    right = (f'<div class="ps">{ps("problem", h["without_label"], h["without"])}{ps("solution", h["with_label"], h["with"])}</div>'
             if h.get('without') else '')
    btns = ''.join(f'<a class="btn {c}" href="{u}">{t}</a>' for t, u, c in h['buttons'])
    return f'''<section class="hero grid-bg"><div class="wrap hero-grid"><div>
{breadcrumb_html(pg["crumbs"]) if len(pg["crumbs"]) > 1 else ""}
<span class="eyebrow">{h["eyebrow"]}</span>
<h1>{h["h1"]}</h1>
<p class="lead">{h["lead"]}</p>
<div class="btn-row">{btns}</div>
<div class="trust-row">{pills}</div></div>
{right}
</div></section>'''

def s_ticker(items):
    row = ''.join(f"<span>{t}</span><span class='dot'>✦</span>" for t in items * 2)
    return f'<div class="ticker" aria-hidden="true"><div class="ticker-track">{row}</div></div>'

def s_cards(sec):
    cards = ''.join(f'<div class="card"><div class="ico" aria-hidden="true">{c.get("ico","✦")}</div><h3>{e(c["h"])}</h3><p class="muted">{c["p"]}</p></div>' for c in sec['cards'])
    return f'''<section class="sec {sec.get("bg","")}" id="{sec.get("id","")}"><div class="wrap">
<div class="center"><span class="eyebrow">{sec["eyebrow"]}</span><h2>{sec["h2"]}</h2>{f'<p class="lead">{sec["lead"]}</p>' if sec.get("lead") else ""}</div>
<div class="g{sec.get("cols",3)}" style="margin-top:40px">{cards}</div></div></section>'''

def s_steps(sec):
    li = ''.join(f'<li><h3>{e(h)}</h3><p class="muted">{p}</p></li>' for h, p in sec['steps'])
    return f'''<section class="sec {sec.get("bg","sec-navy")}" id="{sec.get("id","how-it-works")}"><div class="wrap">
<div class="center"><span class="eyebrow">{sec["eyebrow"]}</span><h2>{sec["h2"]}</h2></div>
<ol class="steps" style="margin-top:40px">{li}</ol></div></section>'''

def s_pricing(pg, sec):
    return f'''<section class="sec {sec.get("bg","sec-lav")}" id="pricing"><div class="wrap center">
<span class="eyebrow">{sec["eyebrow"]}</span><h2>{sec["h2"]}</h2>{f'<p class="lead">{sec["lead"]}</p>' if sec.get("lead") else ""}
<div style="text-align:left">{pricing_block(pg["product"])}</div></div></section>'''

def s_stats(sec):
    st = ''.join(f'<div class="stat"><b>{v}</b><span class="muted">{e(l)}</span></div>' for v, l in sec['stats'])
    src = '<p class="src center">' + sec['source'] + '</p>' if sec.get('source') else ''
    return f'<section class="sec {sec.get("bg","sec-soft")}"><div class="wrap"><div class="g4">{st}</div>{src}</div></section>'

def s_faq(pg, sec):
    d = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><p>{e(a)}</p></details>' for i, (q, a) in enumerate(pg['faqs']))
    return f'''<section class="sec {sec.get("bg","sec-pink")}" id="faq"><div class="wrap"><div class="center"><span class="eyebrow">{t("faq")}</span><h2>{sec["h2"]}</h2></div>
<div class="faq">{d}</div></div></section>'''

def s_cta(sec):
    return f'''<section class="sec {sec.get("bg","sec-pink")}" style="padding-top:0"><div class="wrap"><div class="cta">
<h2>{sec["h2"]}</h2><p class="lead" style="margin:0 auto">{sec["lead"]}</p>
<div class="btn-row"><a class="btn btn-p" href="{sec.get("btn_url") or L("/contact/")}">{sec.get("btn") or t("demo")}</a><a class="btn btn-wa" href="https://wa.me/971585456331" rel="noopener">{t("wa_us")}</a></div></div></div></section>'''

def s_html(sec):
    return sec['html']

def render(pg):
    global LANG
    LANG = 'ar' if pg['url'].startswith('/ar/') else 'en'
    body = ''
    for kind, sec in pg['sections']:
        body += {'hero': lambda s: s_hero(pg, s), 'ticker': s_ticker, 'cards': s_cards, 'steps': s_steps,
                 'pricing': lambda s: s_pricing(pg, s), 'stats': s_stats, 'faq': lambda s: s_faq(pg, s),
                 'cta': s_cta, 'html': s_html}[kind](sec) + '\n'
    h, f = head(pg), footer()
    if pg.get('motion'):
        h = h.replace('</head>', f'<link rel="stylesheet" href="{ASSET}dp-motion.css?v={VER}">\n</head>')
        f = f.replace('</body>', f'<script src="{ASSET}dp-motion.js?v={VER}" defer></script>\n</body>')
    return h + '\n' + header(pg) + f'\n<main id="main">\n{body}</main>\n' + f

# ---------- router + sitemap ----------
ROUTER = '''<?php
/* DigiPromise static page router — GENERATED by build.py, do not edit by hand.
   Loaded from functions.php with:  require_once get_template_directory() . '/dp-router.php';  */
if (!defined('ABSPATH')) exit;
// Runs on 'init' (priority 0) so old redirect rules from the one-page site cannot hijack these URLs
add_action('init', function () {
    if (is_admin() || (defined('DOING_AJAX') && DOING_AJAX) || (defined('REST_REQUEST') && REST_REQUEST)) return;
    if (!in_array($_SERVER['REQUEST_METHOD'] ?? 'GET', array('GET', 'HEAD'), true)) return;
    $routes = %s;
    $path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
    if (!$path) return;
    // /ai-agents/real-estate  ->  301 to  /ai-agents/real-estate/
    if (substr($path, -1) !== '/' && isset($routes[$path . '/'])) {
        $qs = isset($_SERVER['QUERY_STRING']) && $_SERVER['QUERY_STRING'] !== '' ? '?' . $_SERVER['QUERY_STRING'] : '';
        wp_redirect(home_url($path . '/') . $qs, 301);
        exit;
    }
    if (!isset($routes[$path])) return;
    // leave WordPress search, previews and admin-style query URLs alone
    foreach (array('s', 'p', 'page_id', 'preview', 'post_type', 'feed') as $q) { if (isset($_GET[$q])) return; }
    $file = __DIR__ . '/dp-pages/' . $routes[$path];
    if (!is_readable($file)) return;
    global $wp_query;
    if ($wp_query) { $wp_query->is_404 = false; }
    status_header(200);
    $xml = substr($file, -4) === '.xml';
    header('Content-Type: ' . ($xml ? 'application/xml' : 'text/html') . '; charset=UTF-8');
    readfile($file);
    exit;
}, 0);
// WordPress-rendered pages (AI News blog, posts, tools): swap the theme header/footer for the DigiPromise ones
add_action('wp_head', function () {
    if (is_admin()) return;
    $f = __DIR__ . '/dp-pages/wp-chrome-head.html';
    if (is_readable($f)) readfile($f);
}, 99);
add_action('wp_footer', function () {
    if (is_admin()) return;
    $f = __DIR__ . '/dp-pages/wp-chrome-foot.html';
    if (is_readable($f)) readfile($f);
}, 99);
'''

def load_pages():
    pages = []
    global LANG
    for f in sorted(glob.glob(os.path.join(ROOT, 'content', '*.py'))) + sorted(glob.glob(os.path.join(ROOT, 'content_ar', '*.py'))):
        LANG = 'ar' if os.sep + 'content_ar' + os.sep in f else 'en'
        spec = importlib.util.spec_from_file_location(('ar_' if LANG == 'ar' else '') + os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        pages.extend(getattr(m, 'PAGES', None) or [m.PAGE])
    LANG = 'en'
    return pages

def main():
    os.makedirs(PAGES, exist_ok=True)
    routes, urls = {}, []
    live = os.environ.get('LIVE') == '1'
    for pg in load_pages():
        if live:
            if pg['url'] == '/dp-test/': continue
            pg['noindex'] = bool(pg.get('always_noindex'))
        fname = (pg['url'].strip('/').replace('/', '-') or 'home') + '.html'
        open(os.path.join(PAGES, fname), 'w').write(render(pg))
        routes[pg['url']] = fname
        if not pg.get('noindex'): urls.append(pg['url'])
        print('built', pg['url'], '->', fname)
    today = datetime.date.today().isoformat()
    sm = ''.join(f'<url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod></url>' for u in urls)
    open(os.path.join(PAGES, 'dp-sitemap.xml'), 'w').write(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>')
    routes['/dp-sitemap.xml'] = 'dp-sitemap.xml'
    php_arr = '[\n' + ''.join(f"        '{k}' => '{v}',\n" for k, v in routes.items()) + '    ]'
    open(os.path.join(DIST, 'dp-router.php'), 'w').write(ROUTER % php_arr)
    print('router routes:', len(routes))

if __name__ == '__main__':
    import build  # run through the importable module so content files share the same LANG state
    build.main()
