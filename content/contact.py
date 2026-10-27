# /contact/
import build as B
from build_parts import hero, section

opts = ''.join('<option value="' + p['id'] + '">' + p['name'] + ' · ' + B.e(p['category']) + '</option>' for p in B.P['products'])

FORM = '''<div class="g2" style="align-items:start;gap:40px">
<div class="card rv" style="padding:32px"><h2 style="font-size:24px">Book a free 30-minute demo</h2><p class="muted">Tell us a little about your business. We reply within 1 business hour by WhatsApp or email.</p>
<form class="form" id="contact-form" novalidate><input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="row2"><label>Your name<input name="name" autocomplete="name" required></label><label>Business name<input name="company" autocomplete="organization"></label></div>
<div class="row2"><label>WhatsApp number<input name="phone" type="tel" autocomplete="tel" placeholder="+971" required></label><label>Email<input name="email" type="email" autocomplete="email"></label></div>
<div class="row2"><label>Which agent?<select name="agent"><option value="">Not sure yet</option>''' + opts + '''</select></label>
<label>Plan<select name="plan"><option value="">Not sure yet</option><option>Starter</option><option>Growth</option><option>Scale (quote)</option><option>Enterprise (quote)</option></select></label></div>
<label>What would you like the agent to handle?<textarea name="message" rows="4" placeholder="e.g. reply to WhatsApp leads from our Meta ads and book viewings"></textarea></label>
<button class="btn btn-p" type="submit">Send →</button>
<p class="form-msg muted" role="status" style="margin:0;font-size:14px"></p>
</form></div>
<div class="rv d1">
<div class="card" style="margin-bottom:16px"><div class="ico" aria-hidden="true">🟢</div><h3>WhatsApp us</h3><p class="muted">Fastest way to reach us.</p><a class="btn btn-wa" href="https://wa.me/971585456331" rel="noopener">Chat on WhatsApp</a></div>
<div class="card" style="margin-bottom:16px"><div class="ico" aria-hidden="true">📞</div><h3>Call us</h3><p class="muted">Office hours: 10am to 6pm, Dubai time.</p><a class="btn btn-o" href="tel:+971554548756">+971 554 548 756</a></div>
<div class="card" style="margin-bottom:16px"><div class="ico" aria-hidden="true">✉️</div><h3>Email</h3><p class="muted">For sales and partnerships.</p><a class="btn btn-o" href="mailto:sales@digipromise.com">sales@digipromise.com</a></div>
<div class="card"><div class="ico" aria-hidden="true">📍</div><h3>Location</h3><p class="muted">Dubai, UAE. Serving businesses across the world: USA, Europe, UK and GCC.</p></div>
</div></div>
<script>
(function(){var f=document.getElementById('contact-form');if(!f)return;
var q=new URLSearchParams(location.search).get('plan');
if(q){var a=q.split('-');var s=f.agent;for(var i=0;i<s.options.length;i++)if(s.options[i].value===a[0])s.selectedIndex=i;
var m={starter:1,growth:2,scale:3,enterprise:4};if(m[a[1]])f.plan.selectedIndex=m[a[1]];}
f.addEventListener('submit',function(e){e.preventDefault();var msg=f.querySelector('.form-msg'),btn=f.querySelector('button[type=submit]');
var E=f.elements,g=function(n){return E[n]&&E[n].value?E[n].value.trim():''};
var bad=function(t){msg.textContent=t;msg.style.color='#B91C1C'};
if(!g('name')||(!g('phone')&&!g('email'))){bad('Please add your name and a WhatsApp number or email.');return}
var extra=[];if(E.agent&&E.agent.selectedIndex>0)extra.push('Agent: '+E.agent.options[E.agent.selectedIndex].text);if(E.plan&&E.plan.selectedIndex>0)extra.push('Plan: '+E.plan.options[E.plan.selectedIndex].text);
var m=(extra.length?extra.join(' · ')+'\\n':'')+g('message');
btn.disabled=true;msg.style.color='';msg.textContent='Sending…';
(window.DP_SEND?window.DP_SEND({name:g('name'),email:g('email'),phone:g('phone'),company:g('company'),message:m,website:g('website')}):Promise.resolve({ok:false})).then(function(r){btn.disabled=false;
if(r&&r.ok){location.href='/thanks/'}else bad('Not sent: '+((r&&r.error&&r.error!=='network')?r.error:'check your connection and try again, or message us on WhatsApp.'))});});})();
</script>'''

PAGE = {
    'url': '/contact/', 'motion': True, 'noindex': True, 'greet': 'Prefer to chat? Ask me anything here and I will reply in seconds.',
    'title': 'Contact DigiPromise: Book a Free AI Agent Demo | Dubai, UAE',
    'description': 'Book a free 30-minute demo of a DigiPromise AI agent. WhatsApp, call or send us your details and we reply within 1 business hour. Dubai, UAE.',
    'crumbs': [('Home', '/'), ('Contact', None)],
    'schema': [{'@type': 'ContactPage', 'name': 'Contact DigiPromise', 'about': {'@id': 'https://digipromise.com/#org'}}],
    'sections': [
        ('html', {'html': hero([('Home', '/'), ('Contact', None)], 'Talk to us', 'Let\'s get your <span class="accent">agent live.</span>',
                               'Book a free 30-minute demo, ask a question or get a quote for a custom setup. A real person replies within 1 business hour.', trust=False)}),
        ('html', {'html': section(FORM, 'sec-lav')}),
    ],
}
