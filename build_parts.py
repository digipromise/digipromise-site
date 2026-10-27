"""Reusable section snippets for non-product pages."""
import build as B
e = B.e

def hero(crumbs, eyebrow, h1, lead, buttons=None, extra='', mascot=None, trust=True):
    li = ''.join(('<li><a href="' + u + '">' + n + '</a></li>') if u else ('<li aria-current="page">' + n + '</li>') for n, u in crumbs)
    btns = ''.join('<a class="btn ' + c + '" href="' + u + '">' + t + '</a>' for t, u, c in (buttons or []))
    pills = ''.join('<span>' + B.icon(i) + t + '</span>' for i, t in B.trust()) if trust else ''
    m = '<div class="mascot m-' + mascot + ' hero-mascot rv" aria-hidden="true"></div>' if mascot else ''
    return ('<section class="hero2" style="padding-bottom:72px"><div class="orb" aria-hidden="true"></div><div class="sparkles" aria-hidden="true"></div><div class="wrap">'
            + ('<nav class="crumb rv" aria-label="Breadcrumb"><ol>' + li + '</ol></nav>' if crumbs else '') + m +
            '<span class="eyebrow rv">' + eyebrow + '</span><h1 class="rv d1">' + h1 + '</h1><p class="lead rv d2">' + lead + '</p>'
            + ('<div class="btn-row rv d3">' + btns + '</div>' if btns else '')
            + ('<div class="trust-row rv d3">' + pills + '</div>' if pills else '') + extra + '</div></section>')

def head2(eyebrow, h2, lead=''):
    return ('<div class="center"><span class="eyebrow rv">' + eyebrow + '</span><h2 class="rv d1">' + h2 + '</h2>'
            + ('<p class="lead rv d2">' + lead + '</p>' if lead else '') + '</div>')

def section(inner, bg='', sid=''):
    return '<section class="sec ' + bg + '"' + (' id="' + sid + '"' if sid else '') + '><div class="wrap">' + inner + '</div></section>'

def cards(items, cols=3):
    return ('<div class="g' + str(cols) + '" style="margin-top:44px">' + ''.join(
        '<div class="card rv d' + str(i % 4) + '"><div class="ico" aria-hidden="true">' + ic + '</div><h3>' + h + '</h3><p class="muted">' + t + '</p></div>'
        for i, (ic, h, t) in enumerate(items)) + '</div>')

def agent_cards(cta=None):
    cta = cta or ('تعرّف على' if B.LANG == 'ar' else 'Meet')
    arrow = ' ←' if B.LANG == 'ar' else ' →'
    out = ''
    for p in B.P['products']:
        u = min(t['price']['USD'] for t in p['tiers'] if t['price']['USD']); a = min(t['price']['AED'] for t in p['tiers'] if t['price']['AED'])
        out += ('<a class="card pcard rv" href="' + B.L(p['url']) + '" style="text-align:center"><div class="mascot m-' + p['id'] + '" style="width:110px;height:110px;margin:0 auto 18px" aria-hidden="true"></div>'
                '<span class="tag">' + e(B.cat(p)) + '</span><h3>' + e(p['name']) + '</h3><p class="muted">' + e(B.ptitle(p)) + '</p>'
                '<span class="from">' + B.t('from') + ' ' + B.dual({'USD': u, 'AED': a}) + '<small class="muted">' + B.t('mo') + '</small></span>'
                '<span style="margin-top:12px;font-weight:700;color:var(--purple)">' + cta + ' ' + e(p['name']) + arrow + '</span></a>')
    return '<div class="g3" style="margin-top:44px">' + out + '</div>'

def steps(items, dark=True):
    li = ''.join('<li class="rv d' + str(i) + '"><h3>' + h + '</h3><p class="muted">' + t + '</p></li>' for i, (h, t) in enumerate(items))
    return '<ol class="steps" style="margin-top:44px">' + li + '</ol>'

def checklist(items):
    return '<ul class="tick">' + ''.join('<li>' + x + '</li>' for x in items) + '</ul>'

def split(left, right, flip=False):
    return '<div class="feat' + (' flip' if flip else '') + '"><div class="feat-copy">' + left + '</div><div>' + right + '</div></div>'

def faq_page(pg, faqs, h2):
    pg['faqs'] = faqs
    return ('faq', {'h2': h2})


def dash_demo(lang='en'):
    """Homepage 'see every conversation' section: an example client dashboard (sample data)."""
    ar = lang == 'ar'
    T = (lambda en, a: a if ar else en)
    kpis = [(T('Conversations', 'المحادثات'), '214', '+18%'), (T('Qualified leads', 'عملاء مؤهّلون'), '58', '+12%'),
            (T('Bookings', 'الحجوزات'), '17', '+9%'), (T('Avg first reply', 'متوسط أول رد'), T('4 sec', '4 ث'), '')]
    rows = [('🟢', T('Ahmed K.', 'أحمد ك.'), T('2-bed in JVC, viewing Saturday?', 'شقة غرفتين في JVC، معاينة السبت؟'), T('Booked', 'تم الحجز'), 'ok'),
            ('📸', T('Sara M.', 'سارة م.'), T('Do you deliver to Abu Dhabi?', 'هل توصلون إلى أبوظبي؟'), T('Answered', 'تم الرد'), ''),
            ('✈️', T('Dmitry V.', 'دميتري ف.'), T('Price for 3 nights in December', 'سعر 3 ليالٍ في ديسمبر'), T('Hot lead', 'عميل جاهز'), 'hot'),
            ('💬', T('Fatima A.', 'فاطمة أ.'), T('Can I book a trial class?', 'هل يمكنني حجز حصة تجريبية؟'), T('Booked', 'تم الحجز'), 'ok'),
            ('📞', T('John R.', 'جون ر.'), T('Missed call → called back in 8 sec', 'مكالمة فائتة ← معاودة الاتصال خلال 8 ث'), T('Qualified', 'مؤهّل'), 'hot')]
    k = ''.join(f'<div class="dk"><span>{a}</span><b>{b}</b>' + (f'<em>{c}</em>' if c else '') + '</div>' for a, b, c in kpis)
    r = ''.join(f'<li{" class=on" if i == 0 else ""}><i aria-hidden="true">{ic}</i><div><b>{n}</b><small>{m}</small></div><span class="tag {c}">{t}</span></li>'
                for i, (ic, n, m, t, c) in enumerate(rows))
    chat = (f'<div class="msg u">{T("Hi, is the 2-bed in JVC still available?", "مرحباً، هل شقة الغرفتين في JVC ما زالت متاحة؟")}</div>'
            f'<div class="msg b">{T("Yes! AED 85,000/year, 2 cheques. Would Saturday 11am suit you for a viewing?", "نعم! 85,000 درهم سنوياً على دفعتين. هل يناسبك السبت 11 صباحاً للمعاينة؟")}</div>'
            f'<div class="msg u">{T("Perfect, book it.", "ممتاز، احجزها.")}</div>'
            f'<div class="msg b">{T("Done ✅ Viewing booked. Our agent Omar will WhatsApp you the location.", "تم ✅ حُجزت المعاينة. سيرسل لك مستشارنا عمر الموقع على واتساب.")}</div>')
    lead = (f'<div class="dlead"><b>{T("Lead summary", "ملخص العميل")}</b><div><span>{T("Budget", "الميزانية")}</span><b>AED 85k</b></div>'
            f'<div><span>{T("Area", "المنطقة")}</span><b>JVC</b></div><div><span>{T("Timeline", "الموعد")}</span><b>{T("This month", "هذا الشهر")}</b></div>'
            f'<div><span>{T("Sent to", "أُرسل إلى")}</span><b>{T("Omar · WhatsApp", "عمر · واتساب")}</b></div></div>')
    head = (T('Your dashboard', 'لوحة التحكم'), T('See every conversation.', 'شاهد كل محادثة.'),
            T('Every chat and lead your agent handles, in one place. Read any conversation, see who became a lead and which chats need your team.',
              'كل محادثة وعميل يتعامل معه وكيلك، في مكان واحد. اقرأ أي محادثة، واعرف من أصبح عميلاً، وأي المحادثات تحتاج فريقك.'))
    link = ('/ar/client-dashboard/' if ar else '/client-dashboard/')
    return (f'<section class="sec sec-lav" id="dashboard"><div class="wrap"><div class="center"><span class="eyebrow rv">{head[0]}</span>'
            f'<h2 class="rv d1">{head[1]}</h2><p class="lead rv d2">{head[2]}</p></div>'
            + app_dash(lang) +
            f'<div class="center" style="margin-top:28px"><a class="btn btn-o rv" href="{link}">{T("Explore the dashboard →", "تعرّف على لوحة التحكم ←")}</a></div></div></section>')


def app_dash(lang='en'):
    """Example client dashboard drawn to match the real app (app.digipromise.com, Overview screen). Sample data only (13 Oct 2026)."""
    ar = lang == 'ar'
    T = (lambda en, a: a if ar else en)
    nav = ''.join(f'<span{" class=on" if i == 0 else ""}>{x}</span>' for i, x in enumerate(
        [T('Overview', 'نظرة عامة'), T('Conversations', 'المحادثات'), T('Leads', 'العملاء المحتملون'), T('Setup &amp; settings', 'الإعداد والإعدادات')]))
    kpi = ''.join(f'<div class="ac"><small>{a}</small><b>{b}</b></div>' for a, b in
                  [(T('Chats (last 30 days)', 'المحادثات (آخر 30 يوماً)'), '214'), (T('Leads captured', 'عملاء تم تسجيلهم'), '58'), (T('Handed to your team', 'حُوّلت لفريقك'), '9')])
    def donut(title, pct, big, sub):
        return (f'<div class="ac"><h4>{title}</h4><div class="ring" style="--p:{pct}"><div><b>{big}</b><small>{sub}</small></div></div></div>')
    donuts = (donut(T('Messages used', 'الرسائل المستخدمة'), 26, '3,120', T('of 12,000', 'من 12,000'))
              + donut(T('Chats that became leads', 'محادثات أصبحت عملاء'), 27, '27%', T('58 of 214', '58 من 214'))
              + donut(T('Answered without help', 'أُجيب دون مساعدة'), 96, '96%', T('205 of 214', '205 من 214')))
    vals = [9, 12, 8, 15, 18, 11, 14, 20, 17, 13, 22, 19, 16, 24]
    days = ['30', '02', '04', '06', '08', '10', '12']
    bars = ''.join(f'<i style="height:{round(v / 24 * 100)}%"></i>' for v in vals)
    lbl = ''.join(f'<span>{d}</span>' for d in days)
    att = [(T('Sara M.', 'سارة م.'), T('Asked for a discount above your limit', 'طلبت خصماً أعلى من الحد المسموح'), T('12 min ago', 'قبل 12 دقيقة')),
           (T('John R.', 'جون ر.'), T('Wants to speak to a person', 'يريد التحدث مع شخص'), T('1 h ago', 'قبل ساعة'))]
    attn = ''.join(f'<li><b>{n}</b><span>{m}</span><small>{w}</small></li>' for n, m, w in att)
    rec = [(T('Ahmed K.', 'أحمد ك.'), 'WhatsApp', T('2-bed in JVC, viewing Saturday?', 'شقة غرفتين في JVC، معاينة السبت؟'), T('Lead', 'عميل محتمل'), 'tgl'),
           (T('Mariam A.', 'مريم أ.'), 'Instagram', T('Is the satin dress in size M?', 'هل فستان الساتان متوفر بمقاس M؟'), T('Answered', 'تم الرد'), ''),
           (T('Omar H.', 'عمر ح.'), T('Website', 'الموقع'), T('Table for 4 tonight at 8?', 'طاولة لأربعة الليلة الساعة 8؟'), T('Lead', 'عميل محتمل'), 'tgl'),
           (T('John R.', 'جون ر.'), 'WhatsApp', T('Can I talk to someone?', 'هل يمكنني التحدث مع شخص؟'), T('Handed over', 'حُوّلت للفريق'), 'tgh')]
    recs = ''.join(f'<li><b>{n}</b><em>{c}</em><span>{m}</span><i class="t {k}">{s}</i></li>' for n, c, m, s, k in rec)
    return (f'<div class="adash rv d2" role="img" aria-label="{T("Example of the DigiPromise client dashboard with sample data", "مثال على لوحة تحكم العميل في ديجي برومس ببيانات توضيحية")}">'
            f'<aside><div class="alogo"><img src="{B.ASSET}logo-mark.webp" alt="" width="41" height="28" loading="lazy">{T("Client Dashboard", "لوحة تحكم العميل")}</div><nav>{nav}</nav></aside>'
            f'<div class="amain"><div class="ahead"><div><h3>{T("Marina Homes", "مارينا هومز")}</h3><small>{T("Your AI agent", "وكيلك الذكي")}</small></div>'
            f'<div class="seg"><span>{T("7 days", "7 أيام")}</span><span class="on">{T("30 days", "30 يوماً")}</span><span>{T("90 days", "90 يوماً")}</span></div></div>'
            f'<div class="ag3">{kpi}</div><div class="ag3">{donuts}</div>'
            f'<div class="ag2"><div class="ac"><h4>{T("Chats per day", "المحادثات يومياً")}</h4><small>{T("Last 14 days", "آخر 14 يوماً")}</small><div class="abars">{bars}</div><div class="alabels">{lbl}</div></div>'
            f'<div class="ac"><h4>{T("Needs your attention", "تحتاج انتباهك")}</h4><small>{T("Chats handed to your team", "محادثات حُوّلت لفريقك")}</small><ul class="aatt">{attn}</ul></div></div>'
            f'<div class="ac"><h4>{T("Recent conversations", "أحدث المحادثات")}</h4><small>{T("See all", "عرض الكل")}</small><ul class="arec">{recs}</ul></div>'
            f'<p class="anote">{T("Example data", "بيانات توضيحية")}</p></div></div>')
