# /ar/affiliate-program/ — Arabic affiliate page. Rates live in pricing-v2.json → "affiliate".
import build as B
from build_parts import hero, head2, section, cards, steps, checklist

A = B.P['affiliate']
SR, MR, MO = A['setup_rate'], A['monthly_rate'], A['months']
pct = lambda r: f'{round(r * 100):g}%'
fee = B.P['billing']['setup_fee']
five = next(p for p in B.P['products'] if p['id'] == 'iris')
TN = {'starter': 'المبتدئة', 'growth': 'النمو', 'scale': 'التوسّع'}

def earn(tid):
    t = next(x for x in five['tiers'] if x['id'] == tid)
    s, m = fee[tid]['AED'] * SR, t['price']['AED'] * MR * MO
    return TN[tid], t['price']['AED'], fee[tid]['AED'], s, m, s + m

ex = [earn(t) for t in ('starter', 'growth', 'scale')]
fmt = lambda n: f'{n:,.0f} درهم'
EX_CARDS = '<div class="g3" style="margin-top:44px">' + ''.join(
    f'<div class="card rv d{i}" style="text-align:center"><span class="eyebrow">باقة {n}</span>'
    f'<div style="font-size:clamp(28px,4vw,40px);font-weight:800;margin:10px 0 4px">{fmt(tot)}</div>'
    f'<p class="muted" style="margin:0">لكل عميل في السنة الأولى</p>'
    f'<p class="muted" style="font-size:14px;margin-top:14px">{pct(SR)} من رسوم الإعداد {fmt(sf)} = <b>{fmt(s)}</b><br>{pct(MR)} من {fmt(pr)} شهرياً × {MO} = <b>{fmt(m)}</b></p></div>'
    for i, (n, pr, sf, s, m, tot) in enumerate(ex)) + '</div>'

FORM = f'''<div class="g2" style="align-items:start;gap:40px">
<div class="rv"><h2>قدّم خلال دقيقتين.</h2><p class="lead">نراجع كل طلب خلال يومي عمل ونرسل لك رابطك الخاص ومواد الشراكة على واتساب.</p>
''' + checklist(['الانضمام مجاني وبدون أهداف بيع', 'رابط وكود خاص بك، مثل digipromise.com/?ref=ALI25',
                 f'تتبّع لمدة {A["cookie_days"]} يوماً: تُحتسب لك الإحالة إذا اشترك العميل خلال {A["cookie_days"]} يوماً',
                 'نحن نقدّم العرض ونغلق البيع وننفّذ الإعداد. أنت فقط تعرّفنا على العميل.']) + f'''</div>
<div class="card rv d1" style="padding:32px"><form class="form" id="aff-form" novalidate data-webhook="{A["apply_webhook"]}" data-wa="{A["whatsapp"]}">
<div class="row2"><label>الاسم<input name="name" autocomplete="name" required></label><label>الشركة (اختياري)<input name="company" autocomplete="organization"></label></div>
<div class="row2"><label>رقم واتساب<input name="phone" type="tel" autocomplete="tel" placeholder="+971" dir="ltr" required></label><label>البريد الإلكتروني<input name="email" type="email" autocomplete="email" dir="ltr" required></label></div>
<div class="row2"><label>الدولة<input name="country" autocomplete="country-name" placeholder="الإمارات"></label>
<label>كيف ستُحيل العملاء؟<select name="channel"><option value="">اختر</option><option>عملائي (وكالة، مستقل، مستشار)</option><option>موقع أو مدونة أو نشرة بريدية</option><option>وسائل التواصل / محتوى</option><option>شبكة أعمال / توصيات</option><option>أخرى</option></select></label></div>
<label>الموقع أو حساب التواصل (اختياري)<input name="link" type="url" placeholder="https://" dir="ltr"></label>
<label style="flex-direction:row;align-items:flex-start;gap:10px;font-weight:500"><input type="checkbox" name="terms" required style="width:auto;margin-top:5px"> أوافق على شروط برنامج الشركاء أدناه.</label>
<button class="btn btn-p" type="submit">قدّم الآن ←</button>
<p class="form-msg muted" role="status" style="margin:0;font-size:14px"></p>
</form></div></div>
<script>
(function(){{var f=document.getElementById('aff-form');if(!f)return;
f.addEventListener('submit',function(e){{e.preventDefault();var m=f.querySelector('.form-msg'),v=function(n){{return (f.elements[n].value||'').trim()}};
if(!v('name')||!v('phone')||!v('email')){{m.textContent='يرجى إضافة الاسم ورقم واتساب والبريد الإلكتروني.';m.style.color='#B91C1C';return}}
if(!f.elements['terms'].checked){{m.textContent='يرجى الموافقة على شروط البرنامج.';m.style.color='#B91C1C';return}}
var data={{name:v('name'),company:v('company'),phone:v('phone'),email:v('email'),country:v('country'),channel:v('channel'),link:v('link'),ref:window.DP_REF||'',page:location.href,lang:'ar'}};
var hook=f.getAttribute('data-webhook');
var txt='طلب انضمام لبرنامج الشركاء\\nالاسم: '+data.name+(data.company?'\\nالشركة: '+data.company:'')+'\\nواتساب: '+data.phone+'\\nالبريد: '+data.email+(data.country?'\\nالدولة: '+data.country:'')+(data.channel?'\\nالقناة: '+data.channel:'')+(data.link?'\\nالرابط: '+data.link:'');
function done(){{m.style.color='';m.textContent='شكراً! استلمنا طلبك وسنرد عليك على واتساب خلال يومي عمل.';f.reset()}}
if(hook){{fetch(hook,{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(data)}}).then(done).catch(function(){{location.href='https://wa.me/'+f.getAttribute('data-wa')+'?text='+encodeURIComponent(txt)}})}}
else{{window.open('https://wa.me/'+f.getAttribute('data-wa')+'?text='+encodeURIComponent(txt),'_blank','noopener');done()}}
}});}})();
</script>'''

TERMS = checklist([
    f'العمولة: {pct(SR)} من رسوم الإعداد و{pct(MR)} من كل دفعة شهرية لأول {MO} شهراً، على المبالغ التي دفعها العميل فعلياً.',
    f'تصبح العمولة مستحقة بعد {A["hold_days"]} يوماً من تحصيل دفعة العميل. الدفعات المستردة أو الملغاة لا تُحتسب.',
    f'الدفع: شهرياً عبر تحويل بنكي أو Wise عندما يصل رصيدك إلى {A["min_payout_aed"]:,} درهم.',
    f'تُحتسب الإحالة لآخر رابط شريك نقر عليه العميل خلال {A["cookie_days"]} يوماً. العملاء الحاليون والعملاء المحتملون الموجودون لدينا مسبقاً لا يُحتسبون.',
    'ممنوع الإعلانات المدفوعة باسم DigiPromise، وممنوع الرسائل المزعجة والادعاءات المضللة عن الأسعار أو النتائج.',
    'لا يمكنك إحالة نفسك أو شركتك. قد نحدّث النسب للإحالات الجديدة بإشعار قبل 30 يوماً.',
])

FAQS = [
    ('من يمكنه الانضمام إلى برنامج شركاء ديجي برومس؟', 'كل من يعمل مع الشركات: وكالات التسويق والمواقع، المستقلون، المستشارون، المحاسبون، مدربو الأعمال، مزودو خدمات تقنية المعلومات وصنّاع المحتوى. لا يشترط أن تكون في الإمارات.'),
    ('كم يمكنني أن أربح؟', f'تحصل على {pct(SR)} من رسوم الإعداد لمرة واحدة و{pct(MR)} من الاشتراك الشهري للعميل لأول {MO} شهراً. في باقة النمو يعادل ذلك حوالي {fmt(ex[1][5])} لكل عميل في السنة الأولى.'),
    ('هل أحتاج إلى البيع أو تنفيذ الإعداد؟', 'لا. أنت تعرّفنا على الشركة برابطك أو كودك، ونحن نقدّم العرض ونغلق البيع ونبني الوكيل وندعم العميل.'),
    ('كيف تُتتبّع الإحالة؟', f'يحفظ رابطك الخاص كودك في متصفح الزائر لمدة {A["cookie_days"]} يوماً، وكل نموذج أو محادثة يبدؤها يحمل كودك. ويمكن للعميل أيضاً ذكر كودك في مكالمة العرض.'),
    ('متى وكيف أحصل على المال؟', f'تصبح العمولة مستحقة بعد {A["hold_days"]} يوماً من دفع العميل. ندفع شهرياً عبر تحويل بنكي أو Wise عندما يصل رصيدك إلى {A["min_payout_aed"]:,} درهم.'),
    ('هل أستطيع متابعة إحالاتي وأرباحي؟', 'نعم. يحصل الشركاء المعتمدون على لوحة تحكم تعرض النقرات والعملاء المحتملين والعملاء الفعليين والعمولات. وحتى إطلاقها نرسل كشفاً شهرياً.'),
]

PAGE = {
    'url': '/ar/affiliate-program/', 'motion': True,
    'title': 'برنامج شركاء ديجي برومس: اربح من إحالة عملاء وكلاء الذكاء الاصطناعي',
    'description': f'انضم إلى برنامج شركاء ديجي برومس واربح {pct(SR)} من رسوم الإعداد و{pct(MR)} من الاشتراك الشهري لمدة {MO} شهراً عن كل شركة تُحيلها. الانضمام مجاني.',
    'crumbs': [('الرئيسية', '/ar/'), ('برنامج الشركاء', None)],
    'faqs': FAQS,
    'sections': [
        ('html', {'html': hero([('الرئيسية', '/ar/'), ('برنامج الشركاء', None)], '🤝 برنامج شركاء ديجي برومس',
                               'أحِل الشركات.<br><span class="accent">واربح كل شهر.</span>',
                               f'عرّف الشركات على وكلائنا الأذكياء واربح {pct(SR)} من رسوم الإعداد و{pct(MR)} من اشتراكهم الشهري لمدة {MO} شهراً. نحن نتولى البيع والبناء والدعم.',
                               [('قدّم الآن ←', '#apply', 'btn-p'), ('كيف يعمل البرنامج', '#how', 'btn-o')], trust=False)}),
        ('html', {'html': section(head2('كيف يعمل', 'ثلاث خطوات.<br>بدون بيع.') + steps([
            ('قدّم', 'املأ النموذج القصير. نعتمدك ونرسل لك رابطك وكودك الخاص.'),
            ('شارك', 'أرسل رابطك للشركات التي تصلها رسائل واتساب ومكالمات وعملاء محتملون كثيرون.'),
            ('اربح', 'عندما تصبح عميلاً لدينا، تربح من رسوم الإعداد ومن كل دفعة شهرية لمدة سنة.')]), 'sec-navy', 'how')}),
        ('html', {'html': section(head2('العمولة', 'عمولة واضحة ومتكررة.') + cards([
            ('💼', f'{pct(SR)} من رسوم الإعداد', 'تُدفع مرة واحدة لكل عميل، على رسوم الإعداد (من 5,000 إلى 15,000 درهم).'),
            ('🔁', f'{pct(MR)} شهرياً لمدة {MO} شهراً', 'على كل دفعة شهرية يدفعها العميل في سنته الأولى.'),
            ('🏦', 'دفع شهري', f'عبر تحويل بنكي أو Wise بعد {A["hold_days"]} يوماً من دفع العميل. الحد الأدنى {A["min_payout_aed"]:,} درهم.')]), 'sec-lav')}),
        ('html', {'html': section(head2('أمثلة على الأرباح', 'كم يساوي عميل واحد لك.', 'بناءً على الباقات الشهرية لوكلاء IRIS وAURA وNova وLuna وLara.') + EX_CARDS)}),
        ('html', {'html': section(head2('لمن البرنامج', 'مثالي إذا كنت تعمل<br>مع الشركات بالفعل.') + cards([
            ('🎨', 'الوكالات ومصممو المواقع', 'أضف وكلاء الذكاء الاصطناعي لخدماتك بدون بنائها.'),
            ('🧑‍💼', 'المستشارون والمدربون', 'رشّح أداة مجرّبة لأصحاب الأعمال الذين تنصحهم.'),
            ('🧾', 'المحاسبون ومخلّصو المعاملات', 'عملاؤك يسألون كيف يوفّرون الوقت. هذا هو الجواب.'),
            ('💻', 'مزودو تقنية المعلومات', 'أضف وكيل واتساب والموقع إلى خدماتك.'),
            ('📣', 'صنّاع المحتوى والمجتمعات', 'شارك مع جمهور الأعمال في الإمارات وخارجها.'),
            ('🤝', 'شبكات الأعمال', 'عرّفنا على أصحاب الأعمال المناسبين واحصل على عمولتك.')]), 'sec-lav')}),
        ('html', {'html': section(FORM, '', 'apply')}),
        ('html', {'html': section('<div class="center"><span class="eyebrow rv">الشروط</span><h2 class="rv d1">شروط البرنامج بلغة بسيطة.</h2></div><div style="max-width:760px;margin:32px auto 0" class="rv">' + TERMS + '</div>', 'sec-lav')}),
        ('faq', {'h2': 'أسئلة عن برنامج الشركاء.'}),
        ('cta', {'btn': 'قدّم الآن ←', 'btn_url': '#apply', 'h2': 'تعرف شركة تحتاج وكيلاً ذكياً؟', 'lead': 'قدّم الآن واحصل على رابطك اليوم. لديك أسئلة؟ راسلنا على واتساب في أي وقت.'}),
    ],
}
