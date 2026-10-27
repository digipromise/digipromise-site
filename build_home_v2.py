"""Homepage v2 concept (motion layout). Writes dist/dp-pages/home-v2.html and a standalone preview."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B

P = B.P
A = B.ASSET
e = B.e

ICO = {
 'plug': '<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0V8zM12 18v4"/>',
 'brain': '<path d="M12 5a3 3 0 1 0-5.9.8A3 3 0 0 0 4 11a3 3 0 0 0 2 5.6A3 3 0 0 0 12 18zM12 5a3 3 0 1 1 5.9.8A3 3 0 0 1 20 11a3 3 0 0 1-2 5.6A3 3 0 0 1 12 18z"/>',
 'rocket': '<path d="M5 15c-1.5 1.5-2 5-2 5s3.5-.5 5-2M14 4c3-1 6-1 6-1s0 3-1 6l-6 6-5-5 6-6zM9 15l-3-3 3-1M15 9v0M12 18l1 3 3-3"/>',
 'chart': '<path d="M3 20h18M6 16l4-5 3 3 5-7"/>',
}
def ico(k): return f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICO[k]}</svg>'

BLURB = {
 'iris': 'Answers property enquiries, qualifies budget and area, books viewings.',
 'aura': 'Recommends products, tracks orders and recovers abandoned carts.',
 'nova': 'Takes table and room bookings and cuts no-shows with reminders.',
 'luna': 'Books appointments and classes and nudges members to renew.',
 'lara': 'Quotes rentals, checks availability and confirms bookings.',
 'stella': 'Picks up every call, books, qualifies and logs the outcome.',
 'lilia': 'Your personal assistant: inbox, calendar, WhatsApp and a daily briefing.',
}

def frm(p):
    return min(t['price']['USD'] for t in p['tiers'] if t['price']['USD']), min(t['price']['AED'] for t in p['tiers'] if t['price']['AED'])

agents = ''
for p in P['products']:
    u, a = frm(p)
    agents += f'''<a class="cf-item" href="{p["url"]}"><div class="mascot m-{p["id"]}" aria-hidden="true"></div>
<span class="tag">{e(p["category"])}</span><h3>{e(p["name"])}</h3><p>{BLURB[p["id"]]}<br><b>From {B.dual({"USD":u,"AED":a})}/mo</b></p><span class="more">Meet {e(p["name"])} →</span></a>'''

script = [
 ['u', 'Hi, do you have 2-bed apartments in JVC?'],
 ['b', 'Yes! 6 available right now. Are you buying or renting?', 0],
 ['u', 'Buying, budget around 1.4M'],
 ['b', 'Great. Cash or mortgage, and when are you planning to move?', 1],
 ['u', 'Mortgage, in 3 months'],
 ['b', 'Perfect. I can book a viewing Thursday 6pm or Saturday 11am. Which works?', 2],
 ['u', 'Saturday'],
 ['b', 'Booked ✅ Your agent Sara will WhatsApp you the location.', 3],
]

faqs = [
 ('What does a DigiPromise AI agent actually do?', 'It replies to your customers on your website, WhatsApp, Instagram and Telegram in seconds, asks the questions your sales team would ask, books appointments or viewings, and sends the qualified lead to your team on WhatsApp, Telegram or email.'),
 ('Is this a self-serve tool or do you set it up?', 'We set it up for you. Our team designs and trains the agent on your services, prices, FAQs and tone, connects your channels and tests it before launch. Setup starts within 24 hours of your kickoff call, and we agree the go-live date with you on that call.'),
 ('Does it speak Arabic?', 'Yes. Every agent replies in Arabic, English and 100+ other languages, and switches automatically to the language your customer writes in.'),
 ('Can I see what the agent says to my customers?', 'Yes. From the Growth plan up you get a client dashboard with every conversation, lead and booking, like the example above, and you can change the agent\'s answers any time.'),
 ('How much does it cost?', 'Plans start from AED 2,500 a month. Every agent is custom-built for your business, so there is a one-time setup fee from AED 5,000. Pay annually and you save 15% on your plan, plus the setup fee is fully waived on Starter and 50% off on Growth, Scale and Enterprise.'),
 ('What if it does not work for my business?', 'Every agent is designed around your business, your services and your customers. Before we start, we agree the exact scope with you, then we build and test it until it works the way you need. If you are not satisfied or change your mind, you can cancel any time and we refund the remaining amount under our refund policy. The setup fee covers the custom planning and build agreed with you, so it is not refundable. Monthly plans stay flexible: no lock-in, cancel any time, and come back within 6 months without paying setup again. We would rather earn your business every month.'),
]

from build_parts import dash_demo
DASH = dash_demo('en')
main = f'''
<section class="hero2">
<div class="orb" aria-hidden="true"></div><div class="sparkles" aria-hidden="true"></div>
<div class="wrap">
<span class="eyebrow rv">🤖 AI employees &amp; AI agents for your business</span>
<h1 class="rv d1">Your AI employee,<br><span class="rot"><span class="on">answering</span><span>qualifying</span><span>booking</span><span>closing</span></span> while you sleep.</h1>
<p class="lead rv d2">DigiPromise builds, trains and runs AI employees that answer every lead on your website, WhatsApp, Instagram, Telegram and phone in seconds, in English, Arabic, Russian and 100+ languages, around the clock.</p>
<form class="capture rv d3" action="#" novalidate><input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"><label class="sr" for="cap-email">Work email or WhatsApp</label>
<input id="cap-email" name="contact" type="text" placeholder="Work email or WhatsApp number" autocomplete="email">
<button class="btn btn-p" type="submit">Get my AI employee →</button></form>
<p class="capture-note rv d3">Free 30-minute call · Setup starts within 24 hours · Cancel anytime</p>
</div>
<div class="stage rv"><div class="stage-card">
<div class="stage-side"><h3>What IRIS just did, live</h3>
<ul class="feed"><li><span>Replied</span><b>in 3 seconds</b></li><li><span>Qualified</span><b>budget · cash or mortgage</b></li><li><span>Booked</span><b>viewing Saturday 11am</b></li><li><span>Alerted</span><b>agent on WhatsApp</b></li></ul></div>
<div class="phone" aria-label="Example conversation with IRIS"><div class="phone-top"><i></i><div>IRIS · Real estate<small>● Online now</small></div></div>
<div class="msgs" style="display:flex;flex-direction:column;gap:8px" data-script='{json.dumps(script, ensure_ascii=False).replace("'", "&#39;")}'></div></div>
</div></div>
</section>

<!-- logos belt removed 12 Oct 2026; re-add the Trusted-by section with B.client_marquee() -->

<section class="sec"><div class="wrap">
<div class="center"><span class="eyebrow rv">Fully managed</span><h2 class="rv d1">We build it. You just<br>watch the leads arrive.</h2>
<p class="lead rv d2">No templates to set up and no prompts to write. Our team connects your channels, trains the agent on your business and keeps improving it after launch.</p></div>
<div class="tl">
<div class="tl-i rv"><div class="tl-ic">{ico("plug")}</div><div class="tl-dot"></div><small>01</small><h3>We map your leads</h3><p class="muted">A 30-minute call to see where your enquiries come from and where they get lost.</p></div>
<div class="tl-i rv d1"><div class="tl-ic">{ico("brain")}</div><div class="tl-dot"></div><small>02</small><h3>We train your agent</h3><p class="muted">On your services, prices, FAQs and the way your best salesperson talks.</p></div>
<div class="tl-i rv d2"><div class="tl-ic">{ico("rocket")}</div><div class="tl-dot"></div><small>03</small><h3>We go live</h3><p class="muted">Website, WhatsApp, Telegram and Instagram connected and tested, including WhatsApp approval by Meta.</p></div>
<div class="tl-i rv d3"><div class="tl-ic">{ico("chart")}</div><div class="tl-dot"></div><small>04</small><h3>You close more</h3><p class="muted">Every lead answered and qualified, without hiring another person.</p></div>
</div></div></section>

<section class="sec sec-lav" id="agents"><div class="wrap center">
<span class="eyebrow rv">Meet the team</span><h2 class="rv d1">Seven AI employees.<br>One for every job.</h2>
<div class="cf rv d2"><button class="cf-nav cf-prev" aria-label="Previous agent">‹</button>{agents}<button class="cf-nav cf-next" aria-label="Next agent">›</button></div>
<div class="cf-dots"></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="feat"><div class="feat-copy"><h2 class="rv">They listen.</h2>
<p class="lead rv d1">Website chat, WhatsApp, Instagram, Telegram and phone calls, all handled by your AI team that never misses a message, even at 2am on a Sunday.</p>
<div class="kv rv d2"><div><span>Channels</span><b>Website · WhatsApp · Instagram · Telegram · Calls</b></div><div><span>Languages</span><b>English · Arabic · Russian · 100+</b></div><div><span>Hours</span><b>24/7, including weekends</b></div></div></div>
<div class="demo rv d1"><div class="hub"><svg viewBox="0 0 400 320" preserveAspectRatio="none" aria-hidden="true"><path d="M60 40 C150 60 170 130 200 160"/><path d="M340 60 C260 80 230 130 200 160"/><path d="M40 260 C120 230 170 190 200 160"/><path d="M350 290 C280 250 230 190 200 160"/><path d="M200 10 C200 60 200 110 200 160"/></svg>
<span class="ch">💬 Website</span><span class="ch">🟢 WhatsApp</span><span class="ch">📸 Instagram</span><span class="ch">📞 Calls</span><span class="ch">✈️ Telegram</span>
<div class="core mascot m-iris" aria-hidden="true"></div></div></div></div>

<div class="feat flip"><div class="feat-copy"><h2 class="rv">They answer.</h2>
<p class="lead rv d1">Real answers from your own prices, listings and policies, in your tone. Each reply moves the customer one step closer to a booking.</p>
<div class="kv rv d2"><div><span>First reply</span><b>Under 5 seconds</b></div><div><span>Trained on</span><b>Your FAQs, prices, catalogue</b></div><div><span>Goal</span><b>A booking, not just a chat</b></div></div></div>
<div class="demo rv d1"><div class="phone" style="min-height:0;padding:0"><div class="msg u">Do you deliver to Abu Dhabi?</div><div class="msg b">Yes, free delivery to Abu Dhabi on orders over AED 200, usually next day.</div><div class="msg u">And do you have this dress in size M?</div><div class="msg b">Size M is in stock in black and emerald. Want me to add black to your cart?</div><div class="msg u">Yes please</div><div class="msg b">Done 🛍️ Here is your checkout link.</div></div></div></div>

<div class="feat"><div class="feat-copy"><h2 class="rv">They hand over.</h2>
<p class="lead rv d1">When a lead is ready, your team gets a WhatsApp alert with everything they need: name, number, budget, timeline and the full chat.</p>
<div class="kv rv d2"><div><span>Lead sent to</span><b>WhatsApp · Google Sheets · CRM</b></div><div><span>Includes</span><b>Score, budget, timeline, chat</b></div><div><span>You see it in</span><b>Your client dashboard</b></div></div></div>
<div class="demo"><div class="lead-card"><h4>New qualified lead · IRIS</h4><div class="row"><span>Name</span><b>Ahmed K.</b></div><div class="row"><span>Looking for</span><b>2BR, JVC</b></div><div class="row"><span>Budget</span><b>AED 1.4M · mortgage</b></div><div class="row"><span>Viewing</span><b>Sat 11:00</b></div><div class="score"><i></i></div><small class="muted">Lead score 86 / 100</small></div>
<div class="alert"><i aria-hidden="true"></i><div><b>DigiPromise · WhatsApp</b><small>🔥 Hot lead: Ahmed K., 2BR JVC, viewing Sat 11am</small></div></div></div></div>
</div></section>

{DASH}
<section class="sec sec-navy"><div class="wrap">
<div class="stats-dark"><div class="rv"><b data-to="300" data-suf="%">0%</b><span>Avg conversion increase</span></div><div class="rv d1"><b data-to="85" data-suf="%">0%</b><span>Client satisfaction</span></div><div class="rv d2"><b>24/7</b><span>Every lead answered</span></div><div class="rv d3"><b data-to="6" data-suf=" yrs">0</b><span>Building for UAE businesses</span></div></div>
<div class="founder"><img class="rv" src="{A}founder-robot.webp" alt="Malik, founder of DigiPromise" width="320" height="320" loading="lazy"><div class="rv d1">
<blockquote>“Businesses don't need more AI tools. They need the right AI, built around how they work. That's what we deliver.”</blockquote><cite>Malik · Founder &amp; AI Consultant, DigiPromise</cite>
<a class="btn btn-o" href="/about/" style="margin-top:22px">Read the story →</a></div></div>
</div></section>
<svg class="ribbon" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0h1440v30C1100 80 340 80 0 30z" fill="#120C2A"/></svg>

<section class="sec center" style="padding-top:40px"><div class="wrap">
<h2 class="rv">Every enquiry answered.<br><span class="accent">Around the clock.</span></h2>
<div class="btn-row rv d1" style="justify-content:center"><a class="btn btn-p" href="/contact/">Book a free demo →</a><a class="btn btn-o" href="/pricing/">See pricing</a></div></div></section>
'''

faq_html = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><p>{e(a)}</p></details>' for i, (q, a) in enumerate(faqs))
main += f'''<section class="sec sec-pink" id="faq"><div class="wrap"><div class="center"><span class="eyebrow">FAQ</span><h2>Questions, answered.</h2></div><div class="faq">{faq_html}</div></div></section>'''

if __name__ == '__main__':
    pg = {'url': '/home-v2/', 'noindex': True, 'title': 'AI Agents & AI Employees for Businesses | DigiPromise',
          'description': 'DigiPromise, Dubai, builds and runs AI agents that answer, qualify and book every lead on your website, WhatsApp, Instagram, Telegram and phone in seconds, in 100+ languages.',
          'crumbs': [('Home', '/')], 'faqs': faqs, 'sections': []}

    html = B.head(pg).replace('</head>', f'<link rel="stylesheet" href="{A}dp-motion.css?v={B.VER}">\n</head>') \
        + B.header() + f'\n<main id="main">{main}</main>\n' \
        + B.footer().replace('</body>', f'<script src="{A}dp-motion.js?v={B.VER}" defer></script>\n</body>')
    open(os.path.join(B.PAGES, 'home-v2.html'), 'w').write(html)

    # standalone preview: inline assets so it renders anywhere
    AD = os.path.join(B.PAGES, 'assets')
    prev = html
    for f in ['dp.css', 'widget.css', 'dp-motion.css']:
        css = open(os.path.join(AD, f)).read().replace('url(inter.woff2)', 'url(https://cdn.jsdelivr.net/npm/@fontsource-variable/inter/files/inter-latin-wght-normal.woff2)')
        prev = re.sub(r'<link rel="stylesheet" href="' + re.escape(A + f) + r'[^>]*>', lambda m: '<style>' + css + '</style>', prev)
    for f in ['dp.js', 'widget.js', 'dp-motion.js']:
        js = open(os.path.join(AD, f)).read()
        prev = re.sub(r'<script src="' + re.escape(A + f) + r'[^"]*" defer></script>', lambda m: '<script>' + js + '</script>', prev)
    import base64
    logo = 'data:image/webp;base64,' + base64.b64encode(open(os.path.join(AD, 'logo-mark.webp'), 'rb').read()).decode()
    prev = prev.replace(A + 'logo-mark.webp', logo).replace(f'<link rel="preload" href="{A}inter.woff2" as="font" type="font/woff2" crossorigin>', '')
    open(os.path.join(B.ROOT, 'home-v2-preview.html'), 'w').write(prev)
    print('ok', len(html), len(prev))

