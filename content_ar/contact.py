# /ar/contact/
import build as B
from build_parts import hero, section

opts = ''.join('<option value="' + p['id'] + '">' + p['name'] + ' · ' + B.e(B.cat(p)) + '</option>' for p in B.P['products'])

FORM = '''<div class="g2" style="align-items:start;gap:40px">
<div class="card rv" style="padding:32px"><h2 style="font-size:24px">احجز عرضاً تجريبياً مجانياً لمدة 30 دقيقة</h2><p class="muted">أخبرنا قليلاً عن شركتك. نرد عليك خلال ساعة عمل واحدة عبر واتساب أو البريد الإلكتروني.</p>
<form class="form" id="contact-form" novalidate><input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="row2"><label>اسمك<input name="name" autocomplete="name" required></label><label>اسم الشركة<input name="company" autocomplete="organization"></label></div>
<div class="row2"><label>رقم واتساب<input name="phone" type="tel" autocomplete="tel" placeholder="+971" dir="ltr" required></label><label>البريد الإلكتروني<input name="email" type="email" autocomplete="email" dir="ltr"></label></div>
<div class="row2"><label>أي وكيل؟<select name="agent"><option value="">لست متأكداً بعد</option>''' + opts + '''</select></label>
<label>الباقة<select name="plan"><option value="">لست متأكداً بعد</option><option>المبتدئة</option><option>النمو</option><option>التوسّع (عرض سعر)</option><option>المؤسسات (عرض سعر)</option></select></label></div>
<label>ماذا تريد أن يتولى الوكيل؟<textarea name="message" rows="4" placeholder="مثال: الرد على عملاء واتساب من إعلانات ميتا وحجز المعاينات"></textarea></label>
<button class="btn btn-p" type="submit">إرسال ←</button>
<p class="form-msg muted" role="status" style="margin:0;font-size:14px"></p>
</form></div>
<div class="rv d1">
<div class="card" style="margin-bottom:16px"><div class="ico" aria-hidden="true">🟢</div><h3>راسلنا على واتساب</h3><p class="muted">أسرع طريقة للتواصل معنا.</p><a class="btn btn-wa" href="https://wa.me/971585456331" rel="noopener">تحدث على واتساب</a></div>
<div class="card" style="margin-bottom:16px"><div class="ico" aria-hidden="true">📞</div><h3>اتصل بنا</h3><p class="muted">ساعات العمل: من 10 صباحاً إلى 6 مساءً بتوقيت دبي.</p><a class="btn btn-o" href="tel:+971554548756" dir="ltr">+971 554 548 756</a></div>
<div class="card" style="margin-bottom:16px"><div class="ico" aria-hidden="true">✉️</div><h3>البريد الإلكتروني</h3><p class="muted">للمبيعات والشراكات.</p><a class="btn btn-o" href="mailto:sales@digipromise.com">sales@digipromise.com</a></div>
<div class="card"><div class="ico" aria-hidden="true">📍</div><h3>الموقع</h3><p class="muted">دبي، الإمارات. نخدم الشركات حول العالم: الولايات المتحدة وأوروبا والمملكة المتحدة والخليج.</p></div>
</div></div>
<script>
(function(){var f=document.getElementById('contact-form');if(!f)return;
var q=new URLSearchParams(location.search).get('plan');
if(q){var a=q.split('-');var s=f.agent;for(var i=0;i<s.options.length;i++)if(s.options[i].value===a[0])s.selectedIndex=i;
var m={starter:1,growth:2,scale:3,enterprise:4};if(m[a[1]])f.plan.selectedIndex=m[a[1]];}
f.addEventListener('submit',function(e){e.preventDefault();var msg=f.querySelector('.form-msg'),btn=f.querySelector('button[type=submit]');
var E=f.elements,g=function(n){return E[n]&&E[n].value?E[n].value.trim():''};
var bad=function(t){msg.textContent=t;msg.style.color='#B91C1C'};
if(!g('name')||(!g('phone')&&!g('email'))){bad('يرجى إدخال اسمك ورقم واتساب أو البريد الإلكتروني.');return}
var extra=[];if(E.agent&&E.agent.selectedIndex>0)extra.push('الوكيل: '+E.agent.options[E.agent.selectedIndex].text);if(E.plan&&E.plan.selectedIndex>0)extra.push('الباقة: '+E.plan.options[E.plan.selectedIndex].text);
var m=(extra.length?extra.join(' · ')+'\\n':'')+g('message');
btn.disabled=true;msg.style.color='';msg.textContent='جارٍ الإرسال…';
(window.DP_SEND?window.DP_SEND({name:g('name'),email:g('email'),phone:g('phone'),company:g('company'),message:m,website:g('website')}):Promise.resolve({ok:false})).then(function(r){btn.disabled=false;
if(r&&r.ok){location.href='/ar/thanks/'}else bad('لم يتم الإرسال: '+((r&&r.error&&r.error!=='network')?r.error:'تحقق من الاتصال وحاول مرة أخرى، أو راسلنا على واتساب.'))});});})();
</script>'''

PAGE = {
    'url': '/ar/contact/', 'motion': True, 'noindex': True,
    'greet': 'تفضّل الدردشة؟ اسألني أي شيء هنا وسأرد خلال ثوانٍ.',
    'title': 'تواصل مع ديجي برومس: احجز عرضاً تجريبياً مجانياً | دبي، الإمارات',
    'description': 'احجز عرضاً تجريبياً مجانياً لمدة 30 دقيقة لوكيل ذكاء اصطناعي من ديجي برومس. راسلنا على واتساب أو اتصل أو أرسل بياناتك ونرد خلال ساعة عمل. دبي، الإمارات.',
    'crumbs': [('الرئيسية', '/ar/'), ('تواصل معنا', None)],
    'schema': [{'@type': 'ContactPage', 'name': 'تواصل مع ديجي برومس', 'about': {'@id': 'https://digipromise.com/#org'}}],
    'sections': [
        ('html', {'html': hero([('الرئيسية', '/ar/'), ('تواصل معنا', None)], 'تحدث معنا', 'لنجعل <span class="accent">وكيلك يعمل.</span>',
                               'احجز عرضاً تجريبياً مجانياً لمدة 30 دقيقة، أو اسأل سؤالاً، أو اطلب عرض سعر لإعداد مخصص. شخص حقيقي يرد خلال ساعة عمل واحدة.', trust=False)}),
        ('html', {'html': section(FORM, 'sec-lav')}),
    ],
}
