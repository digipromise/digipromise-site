"""Shared generator for the 6 AI-agent product pages. Each content/<agent>.py passes a config dict."""
import json
import build as B

e = B.e

def _chips(items):
    return ''.join('<span>' + x + '</span>' for x in items)

def _script_attr(script):
    return json.dumps(script, ensure_ascii=False).replace("'", "&#39;")

def _yn(v):
    if v is True: return '<span class="y">✓</span>'
    if v is False: return '<span class="n">✕</span>'
    return v

PS = {
 'en': {'cost': 'Monthly cost', 'cost_a': 'Salary + visa', 'cost_b': 'Low, but no results', 'from': 'From ', 'try': 'Try {n} live →', 'see_pricing': 'See pricing',
        'example': 'Example conversation with {n}', 'your_biz': '{n} · Your business', 'online': '● Online now', 'trusted': 'Trusted by leading brands.',
        'problem': 'The problem', 'how': 'How {n} works', 'who': 'Who {n} is for', 'compare': 'Compare', 'vs': '{n} vs the usual options.',
        'works': 'Works with', 'plugs': 'Plugs into the tools<br>you already use.', 'from_label': 'Answers customers on', 'to_label': 'Sends results to',
        'rest': 'Meet the rest of the team', 'diff': "Different industry?<br>There's an agent for that.", 'pricing': '{n} pricing',
        'pick': 'Pick a plan. Setup starts in 24 hours.', 'placeholder': 'Monthly or annual. Annual saves 15% and up to 100% of the setup fee.', 'faqh': '{n} questions, answered.',
        'greet': 'Hi, I am Digi 👋 Thinking about {n} for your business? Ask me how it works, what it costs or how fast it goes live.'},
 'ar': {'cost': 'التكلفة الشهرية', 'cost_a': 'راتب + تأشيرة', 'cost_b': 'منخفضة لكن بلا نتائج', 'from': 'يبدأ من ', 'try': 'جرّب {n} الآن ←', 'see_pricing': 'شاهد الأسعار',
        'example': 'مثال على محادثة مع {n}', 'your_biz': '{n} · شركتك', 'online': '● متصل الآن', 'trusted': 'موثوق من علامات تجارية رائدة.',
        'problem': 'المشكلة', 'how': 'كيف يعمل {n}', 'who': 'لمن صُمّم {n}', 'compare': 'المقارنة', 'vs': '{n} مقارنة بالخيارات المعتادة.',
        'works': 'التكاملات', 'plugs': 'يتكامل مع الأدوات<br>التي تستخدمها بالفعل.', 'from_label': 'يرد على العملاء عبر', 'to_label': 'يرسل النتائج إلى',
        'rest': 'تعرّف على بقية الفريق', 'diff': 'قطاع مختلف؟<br>لدينا وكيل مناسب لك.', 'pricing': 'أسعار {n}',
        'pick': 'اختر باقتك. ويبدأ الإعداد خلال 24 ساعة.', 'placeholder': 'اشتراك شهري أو سنوي. الاشتراك السنوي يوفّر 15% وحتى 100% من رسوم الإعداد.', 'faqh': 'أسئلة عن {n}',
        'greet': 'أهلاً، أنا ديجي 👋 تفكر في {n} لشركتك؟ اسألني كيف يعمل، وكم يكلف، ومتى يكون جاهزاً.'},
}

def product_page(c):
    S = {k: (v.replace('{n}', B.PRODUCTS[c['id']]['name']) if isinstance(v, str) else v) for k, v in PS[B.LANG].items()}
    p = B.PRODUCTS[c['id']]
    pid = p['id']; name = p['name']
    rot = ''.join(('<span class="on">' if i == 0 else '<span>') + w + '</span>' for i, w in enumerate(c['rotate']))
    feed = ''.join('<li><span>' + a + '</span><b>' + b + '</b></li>' for a, b in c['feed'])
    trust = ''.join('<span>' + B.icon(i) + t + '</span>' for i, t in c.get('trust', B.trust()))
    logos = ''.join('<span>' + c['logo_word'] + ' logo ' + str(i) + '</span>' for i in list(range(1, 7)) * 2)
    probs = ''.join('<div class="card rv d' + str(i) + '"><div class="ico" aria-hidden="true">' + ic + '</div><h3>' + e(h) + '</h3><p class="muted">' + t + '</p></div>'
                    for i, (ic, h, t) in enumerate(c['problems']))
    tabs_btn, tabs_panels = '', ''
    for i, t in enumerate(c['tabs'], 1):
        tid = pid + '-t' + str(i); pnl = pid + '-p' + str(i)
        tabs_btn += '<button role="tab" id="' + tid + '" aria-controls="' + pnl + '">' + t['label'] + '</button>'
        lis = ''.join('<li>' + x + '</li>' for x in t['bullets'])
        tabs_panels += ('<div class="tpanel" id="' + pnl + '" role="tabpanel" aria-labelledby="' + tid + '"' + ('' if i == 1 else ' hidden') + '><div><h3>' + t['h3'] + '</h3>'
                        '<p class="lead">' + t['lead'] + '</p><ul>' + lis + '</ul></div><div class="demo' + (' in' if t.get('in') else '') + '"' +
                        (' style="min-height:320px"' if t.get('in') else '') + '>' + t['demo'] + '</div></div>')
    personas = ''.join('<div class="persona rv d' + str(i) + '"><div class="emo" aria-hidden="true">' + ic + '</div><h3>' + h + '</h3><p class="pain">“' + e(q) + '”</p><p class="muted">' + t + '</p></div>'
                       for i, (ic, h, q, t) in enumerate(c['personas']))
    stats = ''.join('<div class="rv d' + str(i) + '">' + v + '<span>' + e(l) + '</span></div>' for i, (v, l) in enumerate(c['stats']))
    q = c.get('quote')
    quote = ''
    if q:
        quote = ('<div class="quote rv" style="margin-top:48px">' + ('<p class="ar">' + q['ar'] + '</p>' if q.get('ar') else '') +
                 '<blockquote>“' + q['text'] + '”</blockquote><cite>' + q['cite'] + '</cite></div>')
    cols = c['compare']['cols']
    thead = '<tr><th scope="col"></th>' + ''.join('<th scope="col">' + x + '</th>' for x in cols) + '<th scope="col" class="us">' + name + '</th></tr>'
    rows = c['compare']['rows'] + [(S['cost'], c['compare'].get('cost_a', S['cost_a']), c['compare'].get('cost_b', S['cost_b']),
                                    S['from'] + B.dual(p['tiers'][0]['price']))]
    tbody = ''.join('<tr><th scope="row">' + r[0] + '</th>' + ''.join('<td>' + _yn(v) + '</td>' for v in r[1:-1]) + '<td class="us">' + _yn(r[-1]) + '</td></tr>' for r in rows)
    others = ''.join('<a href="' + B.L(o['url']) + '"><div class="mascot m-' + o['id'] + '" aria-hidden="true"></div><b>' + e(o['name']) + '</b><small>' + e(B.cat(o)) + '</small></a>'
                     for o in B.P['products'] if o['id'] != pid)

    stage = c.get("stage_html") or ('<div class="stage rv"><div class="stage-card"><div class="stage-side"><h3>' + c["stage_title"] + '</h3><ul class="feed">' + feed + '</ul></div>'
 '<div class="phone" aria-label="' + S["example"] + '"><div class="phone-top"><i class="mascot m-' + pid + '" style="animation:none"></i><div>' + c.get("phone_title", S["your_biz"]) + '<small>' + c.get("phone_status", S["online"]) + '</small></div></div>'
 '<div class="msgs" style="display:flex;flex-direction:column;gap:8px" data-script=\'' + _script_attr(c["chat"]) + '\'></div></div></div></div>')
    top = f'''
<section class="hero2">
<div class="orb" aria-hidden="true"></div><div class="sparkles" aria-hidden="true"></div>
<div class="wrap">
<nav class="crumb rv" aria-label="Breadcrumb"><ol><li><a href="{B.L("/")}">{B.t("home")}</a></li><li><a href="{B.L("/ai-agents/")}">{B.t("nav_agents")}</a></li><li aria-current="page">{e(B.cat(p))}</li></ol></nav>
<div class="mascot m-{pid} hero-mascot rv" aria-hidden="true"></div>
<span class="eyebrow rv">{name} · {c["eyebrow"]}</span>
<h1 class="rv d1">{c["h1_before"]} <span class="rot">{rot}</span>{c["h1_after"]}</h1>
<p class="lead rv d2">{c["lead"]}</p>
<div class="btn-row rv d3">{('<a class="btn btn-p" href="#live-demo">' + S["try"] + '</a>') if c.get("demo_html") else ('<a class="btn btn-p" href="#" data-open-chat="' + e(c["try_prompt"]) + '">' + S["try"] + '</a>')}<a class="btn btn-o" href="#pricing">{S["see_pricing"]}</a></div>
<div class="trust-row rv d3">{trust}</div>
</div>
{stage}
</section>

{c.get("demo_html", "")}
<section><div class="wrap logos"><h2 class="rv">{S["trusted"]}</h2>
{B.client_marquee()}</div></section>

<section class="sec"><div class="wrap center">
<span class="eyebrow rv">{S["problem"]}</span><h2 class="rv d1">{c["problem_h2"]}</h2>
<p class="lead rv d2">{c["problem_lead"]}</p>
<div class="g3" style="margin-top:44px;text-align:left">{probs}</div></div></section>

<section class="sec sec-lav" id="how-it-works"><div class="wrap center">
<span class="eyebrow rv">{S["how"]}</span><h2 class="rv d1">{c["tabs_h2"]}</h2>
<div class="ptabs rv d2" aria-label="{S["how"]}">{tabs_btn}</div>
{tabs_panels}
</div></section>

<section class="sec"><div class="wrap center">
<span class="eyebrow rv">{S["who"]}</span><h2 class="rv d1">{c["personas_h2"]}</h2>
<div class="g4" style="margin-top:44px">{personas}</div></div></section>
'''
    mid = f'''
<section class="sec sec-navy"><div class="wrap">
<div class="stats-dark">{stats}</div>{quote}
</div></section>

<section class="sec"><div class="wrap center">
<span class="eyebrow rv">{S["compare"]}</span><h2 class="rv d1">{S["vs"]}</h2>
<div class="tbl-wrap rv d2" style="margin-top:36px;border:0"><table class="cmp"><thead>{thead}</thead><tbody>{tbody}</tbody></table></div>
</div></section>

<section class="sec sec-soft"><div class="wrap center">
<span class="eyebrow rv">{S["works"]}</span><h2 class="rv d1">{S["plugs"]}</h2>
<p class="lead rv d2">{c["works_lead"]}</p>
<p class="rv" style="margin:36px 0 0;font-weight:700">{c.get("from_label", S["from_label"])}</p>
<div class="chips rv">{_chips(c["works_from"])}</div>
<p class="rv" style="margin:32px 0 0;font-weight:700">{c.get("to_label", S["to_label"])}</p>
<div class="chips rv">{_chips(c["works_to"])}</div>
</div></section>
'''
    bottom = f'''
<section class="sec"><div class="wrap center">
<span class="eyebrow rv">{S["rest"]}</span><h2 class="rv d1">{S["diff"]}</h2>
<div class="team-row rv d2">{others}</div></div></section>
'''
    return {
        'url': B.L(p['url']), 'motion': True, 'noindex': True,
        'title': c['title'], 'description': c['description'], 'product': pid,
        'crumbs': [(B.t('home'), B.L('/')), (B.t('nav_agents'), B.L('/ai-agents/')), (B.cat(p), None)],
        'faqs': c['faqs'],
        'greet': c.get('greet', S['greet']),
        'sections': [
            ('html', {'html': top}), ('html', {'html': mid}),
            ('pricing', {'eyebrow': S['pricing'], 'h2': c.get('pricing_h2', S['pick']), 'bg': 'sec-lav',
                         'lead': S['placeholder']}),
            ('html', {'html': bottom}),
            ('faq', {'h2': S['faqh']}),
            ('cta', {'h2': c['cta_h2'], 'lead': c['cta_lead']}),
        ],
    }

# ---------- reusable demo snippets ----------
def chat_demo(pairs):
    return '<div class="phone" style="min-height:0;padding:0;gap:8px">' + ''.join('<div class="msg ' + w + '">' + t + '</div>' for w, t in pairs) + '</div>'

def card_demo(title, rows, score=None, score_label=''):
    r = ''.join('<div class="row"><span>' + a + '</span><b>' + b + '</b></div>' for a, b in rows)
    s = '<div class="score"><i style="width:' + str(score) + '%"></i></div><small class="muted">' + score_label + '</small>' if score else ''
    return '<div class="lead-card"><h4>' + title + '</h4>' + r + s + '</div>'

def alert_demo(title, rows, alert):
    return card_demo(title, rows) + '<div class="alert"><i aria-hidden="true"></i><div><b>DigiPromise · WhatsApp</b><small>' + alert + '</small></div></div>'


def live_demo(pid, eyebrow, h2, lead, label, chips, ph, send, replies, fallback, title, status, webhook=''):
    """Interactive try-it panel. replies: list of (keywords list, reply html). chips: list of (label, query)."""
    import json as _j
    data = _j.dumps({'r': [[k, r] for k, r in replies], 'f': fallback}, ensure_ascii=False).replace("'", '&#39;')
    btns = ''.join('<button type="button" data-q="' + e(q) + '">' + l + '</button>' for l, q in chips)
    return (f'<section class="sec" id="live-demo"><div class="wrap center"><span class="eyebrow rv">{eyebrow}</span>'
            f'<h2 class="rv d1">{h2}</h2><p class="lead rv d2">{lead}</p>'
            f'<div class="ld rv" data-ld=\'{data}\' data-webhook="{webhook}"><div class="ld-side"><p class="ld-label">{label}</p>{btns}</div>'
            f'<div class="phone ld-phone"><div class="phone-top"><i class="mascot m-{pid}" style="animation:none"></i><div>{title}<small>● {status}</small></div></div>'
            f'<div class="msgs ld-msgs" aria-live="polite"></div>'
            f'<form class="ld-form"><input type="text" maxlength="300" placeholder="{e(ph)}" aria-label="{e(ph)}"><button type="submit">{send}</button></form></div></div>'
            f'</div></section>')


def voice_stage(pid, title, sub, tap, listening, speaking, chips, note, lang):
    """Hero voice demo (Jarvis-style orb): browser speech-to-text + text-to-speech, answers from the page's .ld script."""
    btns = ''.join('<button type="button" data-vq="' + e(q) + '">' + l + '</button>' for l, q in chips)
    return (f'<div class="stage rv"><div class="stage-card vstage" data-vlang="{lang}" data-l-tap="{e(tap)}" data-l-listen="{e(listening)}" data-l-speak="{e(speaking)}">'
            f'<div class="vs-orb-wrap"><button class="vs-orb" type="button" aria-label="{e(tap)}"><span class="vs-ring r1"></span><span class="vs-ring r2"></span><span class="vs-ring r3"></span>'
            f'<span class="vs-core"><i class="mascot m-{pid}"></i></span></button><p class="vs-state">🎙️ {tap}</p></div>'
            f'<div class="vs-side"><h3>{title}</h3><p class="muted">{sub}</p><div class="vs-log" aria-live="polite"></div>'
            f'<div class="vs-chips">{btns}</div><p class="vs-note">{note}</p></div></div></div>')
