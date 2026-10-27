# /affiliate-program/ — public affiliate page. Rates live in pricing-v2.json → "affiliate" (edit there, rebuild).
import build as B
from build_parts import hero, head2, section, cards, steps, checklist

A = B.P['affiliate']
SR, MR, MO = A['setup_rate'], A['monthly_rate'], A['months']
pct = lambda r: f'{round(r * 100):g}%'
fee = B.P['billing']['setup_fee']
five = next(p for p in B.P['products'] if p['id'] == 'iris')

def earn(tid):
    t = next(x for x in five['tiers'] if x['id'] == tid)
    s, m = fee[tid]['AED'] * SR, t['price']['AED'] * MR * MO
    return t['name'], t['price']['AED'], fee[tid]['AED'], s, m, s + m

ex = [earn(t) for t in ('starter', 'growth', 'scale')]
fmt = lambda n: f'AED {n:,.0f}'
EX_CARDS = '<div class="g3" style="margin-top:44px">' + ''.join(
    f'<div class="card rv d{i}" style="text-align:center"><span class="eyebrow">{n} plan</span>'
    f'<div style="font-size:clamp(28px,4vw,40px);font-weight:800;margin:10px 0 4px">{fmt(tot)}</div>'
    f'<p class="muted" style="margin:0">per client, first year</p>'
    f'<p class="muted" style="font-size:14px;margin-top:14px">{pct(SR)} of {fmt(sf)} setup = <b>{fmt(s)}</b><br>{pct(MR)} of {fmt(pr)}/mo × {MO} = <b>{fmt(m)}</b></p></div>'
    for i, (n, pr, sf, s, m, tot) in enumerate(ex)) + '</div>'

FORM = f'''<div class="g2" style="align-items:start;gap:40px">
<div class="rv"><h2>Apply in 2 minutes.</h2><p class="lead">We review every application within 2 business days and send your personal link and partner kit on WhatsApp.</p>
''' + checklist(['Free to join, no targets', 'Your own link and code, e.g. digipromise.com/?ref=ALI25',
                 f'{A["cookie_days"]}-day tracking: you get credit if they sign up within {A["cookie_days"]} days',
                 'We run the demo, the sale and the setup. You just introduce.']) + f'''</div>
<div class="card rv d1" style="padding:32px"><form class="form" id="aff-form" novalidate data-webhook="{A["apply_webhook"]}" data-wa="{A["whatsapp"]}">
<div class="row2"><label>Your name<input name="name" autocomplete="name" required></label><label>Company (optional)<input name="company" autocomplete="organization"></label></div>
<div class="row2"><label>WhatsApp number<input name="phone" type="tel" autocomplete="tel" placeholder="+971" required></label><label>Email<input name="email" type="email" autocomplete="email" required></label></div>
<div class="row2"><label>Country<input name="country" autocomplete="country-name" placeholder="UAE"></label>
<label>How will you refer clients?<select name="channel"><option value="">Choose one</option><option>My own clients (agency, freelancer, consultant)</option><option>Website, blog or newsletter</option><option>Social media / content</option><option>Business network / word of mouth</option><option>Other</option></select></label></div>
<label>Website or social profile (optional)<input name="link" type="url" placeholder="https://"></label>
<label style="flex-direction:row;align-items:flex-start;gap:10px;font-weight:500"><input type="checkbox" name="terms" required style="width:auto;margin-top:5px"> I agree to the affiliate terms below.</label>
<button class="btn btn-p" type="submit">Apply now →</button>
<p class="form-msg muted" role="status" style="margin:0;font-size:14px"></p>
</form></div></div>
<script>
(function(){{var f=document.getElementById('aff-form');if(!f)return;
f.addEventListener('submit',function(e){{e.preventDefault();var m=f.querySelector('.form-msg'),v=function(n){{return (f.elements[n].value||'').trim()}};
if(!v('name')||!v('phone')||!v('email')){{m.textContent='Please add your name, WhatsApp number and email.';m.style.color='#B91C1C';return}}
if(!f.elements['terms'].checked){{m.textContent='Please agree to the affiliate terms.';m.style.color='#B91C1C';return}}
var data={{name:v('name'),company:v('company'),phone:v('phone'),email:v('email'),country:v('country'),channel:v('channel'),link:v('link'),ref:window.DP_REF||'',page:location.href}};
var hook=f.getAttribute('data-webhook');
var txt='Affiliate application\\nName: '+data.name+(data.company?'\\nCompany: '+data.company:'')+'\\nWhatsApp: '+data.phone+'\\nEmail: '+data.email+(data.country?'\\nCountry: '+data.country:'')+(data.channel?'\\nChannel: '+data.channel:'')+(data.link?'\\nLink: '+data.link:'');
function done(){{m.style.color='';m.textContent='Thanks! Application received. We reply on WhatsApp within 2 business days.';f.reset()}}
if(hook){{fetch(hook,{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(data)}}).then(done).catch(function(){{location.href='https://wa.me/'+f.getAttribute('data-wa')+'?text='+encodeURIComponent(txt)}})}}
else{{window.open('https://wa.me/'+f.getAttribute('data-wa')+'?text='+encodeURIComponent(txt),'_blank','noopener');done()}}
}});}})();
</script>'''

TERMS = checklist([
    f'Commission: {pct(SR)} of the setup fee and {pct(MR)} of each monthly payment for the first {MO} months, on payments the client has actually made.',
    f'Commission becomes payable {A["hold_days"]} days after the client\'s payment clears. Refunded or cancelled payments are not commissionable.',
    f'Payouts: {A["payout"][0].lower()+A["payout"][1:]}, once your balance reaches AED {A["min_payout_aed"]:,}.',
    f'Credit goes to the last affiliate link the client clicked, within {A["cookie_days"]} days. Existing clients and leads already in our pipeline do not count.',
    'No paid ads on the DigiPromise name, no spam, no misleading claims about prices or results.',
    'You cannot refer yourself or your own business. We may update the rates for new referrals with 30 days\' notice.',
])

FAQS = [
    ('Who can join the DigiPromise affiliate program?', 'Anyone who works with businesses: marketing and web agencies, freelancers, consultants, accountants, business coaches, IT providers and content creators. You do not need to be in the UAE.'),
    ('How much can I earn?', f'You earn {pct(SR)} of the one-time setup fee plus {pct(MR)} of the client\'s monthly fee for the first {MO} months. On a Growth plan that is about {fmt(ex[1][5])} per client in the first year.'),
    ('Do I need to sell or do the setup?', 'No. You introduce the business with your link or code. We run the demo, close the sale, build the agent and support the client.'),
    ('How is a referral tracked?', f'Your personal link saves your code in the visitor\'s browser for {A["cookie_days"]} days. Every form and chat they start carries your code. The client can also mention your code on the demo call.'),
    ('When and how do I get paid?', f'Commission is payable {A["hold_days"]} days after the client pays. We pay monthly by bank transfer or Wise once your balance reaches AED {A["min_payout_aed"]:,}.'),
    ('Can I see my referrals and earnings?', 'Yes. Approved affiliates get a partner dashboard with clicks, leads, won clients and commission. Until it launches, we send a monthly statement.'),
]

PAGE = {
    'url': '/affiliate-program/', 'motion': True,
    'title': 'DigiPromise Affiliate Program: Earn by Referring AI Agent Clients',
    'description': f'Join the DigiPromise affiliate program. Earn {pct(SR)} of the setup fee plus {pct(MR)} of monthly fees for {MO} months for every business you refer to our AI agents. Free to join.',
    'crumbs': [('Home', '/'), ('Affiliate program', None)],
    'faqs': FAQS,
    'sections': [
        ('html', {'html': hero([('Home', '/'), ('Affiliate program', None)], '🤝 DigiPromise affiliate program',
                               'Refer businesses.<br><span class="accent">Earn every month.</span>',
                               f'Introduce businesses to our AI agents and earn {pct(SR)} of the setup fee plus {pct(MR)} of their monthly plan for {MO} months. We do the selling, building and support.',
                               [('Apply now →', '#apply', 'btn-p'), ('See how it works', '#how', 'btn-o')], trust=False)}),
        ('html', {'html': section(head2('How it works', 'Three steps.<br>No selling required.') + steps([
            ('Apply', 'Fill in the short form. We approve you and send your personal link and code.'),
            ('Share', 'Send your link to businesses that get lots of WhatsApp messages, calls or leads.'),
            ('Earn', 'When they become a client, you earn on their setup fee and every monthly payment for a year.')]), 'sec-navy', 'how')}),
        ('html', {'html': section(head2('Commission', 'Clear, recurring commission.') + cards([
            ('💼', f'{pct(SR)} of the setup fee', 'Paid once per client, on the one-time setup fee (AED 5,000 to 15,000).'),
            ('🔁', f'{pct(MR)} monthly for {MO} months', 'On every monthly payment the client makes in their first year.'),
            ('🏦', 'Paid monthly', f'By bank transfer or Wise, {A["hold_days"]} days after the client pays. Minimum AED {A["min_payout_aed"]:,}.')]), 'sec-lav')}),
        ('html', {'html': section(head2('Example earnings', 'What one client is worth to you.', 'Based on our IRIS, AURA, Nova, Luna and Lara monthly plans.') + EX_CARDS)}),
        ('html', {'html': section(head2('Who it is for', 'Perfect if you already<br>work with businesses.') + cards([
            ('🎨', 'Agencies &amp; web designers', 'Add AI agents to your offer without building them.'),
            ('🧑‍💼', 'Consultants &amp; coaches', 'Recommend a proven tool to the owners you advise.'),
            ('🧾', 'Accountants &amp; PROs', 'Your clients ask how to save time. This is an answer.'),
            ('💻', 'IT &amp; software providers', 'Bundle a WhatsApp and website agent with your services.'),
            ('📣', 'Creators &amp; communities', 'Share with business audiences in the UAE and beyond.'),
            ('🤝', 'Business networks', 'Introduce the right owners and get paid for it.')]), 'sec-lav')}),
        ('html', {'html': section(FORM, '', 'apply')}),
        ('html', {'html': section('<div class="center"><span class="eyebrow rv">Terms</span><h2 class="rv d1">Affiliate terms, in plain English.</h2></div><div style="max-width:760px;margin:32px auto 0" class="rv">' + TERMS + '</div>', 'sec-lav')}),
        ('faq', {'h2': 'Affiliate program questions, answered.'}),
        ('cta', {'btn': 'Apply now →', 'btn_url': '#apply', 'h2': 'Know a business that needs an AI agent?', 'lead': 'Apply now and get your link today. Questions? WhatsApp us any time.'}),
    ],
}
