# /ar/ — Arabic homepage
import json
import build as B
from build_home_v2 import ico

A = B.ASSET
e = B.e

BLURB = {
 'iris': 'يجيب عن استفسارات العقارات، ويؤهّل الميزانية والمنطقة، ويحجز المعاينات.',
 'aura': 'يقترح المنتجات، ويتتبع الطلبات، ويستعيد السلال المتروكة.',
 'nova': 'يحجز الطاولات والغرف ويقلل عدم الحضور بالتذكيرات.',
 'luna': 'تحجز المواعيد والحصص وتذكّر الأعضاء بالتجديد.',
 'lara': 'تعطي أسعار الإيجار، وتتحقق من التوفر، وتؤكد الحجوزات.',
 'stella': 'ترد على كل مكالمة، وتحجز وتؤهّل وتسجّل النتيجة.',
 'lilia': 'مساعدتك الشخصية: البريد والتقويم وواتساب وملخص يومي.',
}

agents = ''
for p in B.P['products']:
    u = min(t['price']['USD'] for t in p['tiers']); a = min(t['price']['AED'] for t in p['tiers'])
    agents += (f'<a class="cf-item" href="{B.L(p["url"])}"><div class="mascot m-{p["id"]}" aria-hidden="true"></div>'
               f'<span class="tag">{e(B.cat(p))}</span><h3>{e(p["name"])}</h3><p>{BLURB[p["id"]]}<br><b>يبدأ من {B.dual({"USD": u, "AED": a})}/شهرياً</b></p><span class="more">تعرّف على {e(p["name"])} ←</span></a>')

script = [
 ['u', 'مرحباً، عندكم شقق غرفتين في JVC؟'],
 ['b', 'أهلاً! نعم، 6 شقق متوفرة الآن. هل تبحث عن شراء أم إيجار؟', 0],
 ['u', 'شراء، الميزانية حوالي 1.4 مليون'],
 ['b', 'ممتاز. الدفع نقداً أم بتمويل؟ ومتى تخطط للانتقال؟', 1],
 ['u', 'تمويل، خلال 3 أشهر'],
 ['b', 'رائع. أقدر أحجز معاينة الخميس 6 مساءً أو السبت 11 صباحاً. أيهما يناسبك؟', 2],
 ['u', 'السبت'],
 ['b', 'تم الحجز ✅ ستراسلك الوكيلة سارة على واتساب بالموقع.', 3],
]

faqs = [
 ('ماذا يفعل وكيل الذكاء الاصطناعي من ديجي برومس بالضبط؟', 'يرد على عملائك في موقعك وواتساب وإنستغرام وتيليجرام خلال ثوانٍ، ويطرح الأسئلة التي يطرحها فريق مبيعاتك، ويحجز المواعيد أو المعاينات، ويرسل العميل المؤهّل لفريقك على واتساب أو تيليجرام أو البريد.'),
 ('هل هي أداة أستخدمها بنفسي أم تتولون الإعداد؟', 'نتولى الإعداد بالكامل. يصمّم فريقنا الوكيل ويدرّبه على خدماتك وأسعارك وأسئلتك الشائعة وأسلوبك، ويربط قنواتك ويختبره قبل الإطلاق. يبدأ الإعداد خلال 24 ساعة من مكالمة الانطلاق، ونتفق معك على موعد الإطلاق خلال المكالمة.'),
 ('هل يتحدث العربية؟', 'نعم. كل وكيل يرد بالعربية والإنجليزية و+100 لغة أخرى، ويتحول تلقائياً إلى اللغة التي يكتب بها عميلك.'),
 ('هل أستطيع رؤية ما يقوله الوكيل لعملائي؟', 'نعم. من باقة النمو فما فوق تحصل على لوحة تحكم بكل محادثة وعميل وحجز، مثل المثال أعلاه، ويمكنك تعديل إجابات الوكيل في أي وقت.'),
 ('كم التكلفة؟', 'تبدأ الباقات من 2,500 درهم شهرياً. كل وكيل يُبنى خصيصاً لشركتك، لذلك توجد رسوم إعداد لمرة واحدة تبدأ من 5,000 درهم. مع الاشتراك السنوي توفّر 15% على باقتك، مع إعفاء كامل من رسوم الإعداد في باقة المبتدئة وخصم 50% عليها في باقات النمو والتوسّع والمؤسسات.'),
 ('ماذا لو لم يناسب شركتي؟', 'كل وكيل يُصمَّم حول شركتك وخدماتك وعملائك. قبل البدء نتفق معك على نطاق العمل بدقة، ثم نبني ونختبر حتى يعمل كما تحتاج. إذا لم تكن راضياً أو غيّرت رأيك، يمكنك الإلغاء في أي وقت ونعيد لك المبلغ المتبقي وفق سياسة الاسترداد. رسوم الإعداد تغطي التخطيط والبناء المخصص المتفق عليه، لذلك لا تُسترد. ويبقى الاشتراك الشهري مرناً: بدون التزام، ألغِ في أي وقت، وعد خلال 6 أشهر دون دفع الإعداد مجدداً. نفضّل أن نكسب ثقتك كل شهر.'),
]

from build_parts import dash_demo
DASH = dash_demo('ar')
main = f'''
<section class="hero2">
<div class="orb" aria-hidden="true"></div><div class="sparkles" aria-hidden="true"></div>
<div class="wrap">
<span class="eyebrow rv">🤖 موظفون ووكلاء بالذكاء الاصطناعي لشركتك</span>
<h1 class="rv d1">موظفك الذكي<br><span class="rot"><span class="on">يرد</span><span>يؤهّل</span><span>يحجز</span><span>يبيع</span></span> وأنت نائم.</h1>
<p class="lead rv d2">تبني ديجي برومس موظفين بالذكاء الاصطناعي وتدرّبهم وتديرهم ليردوا على كل عميل في موقعك وواتساب وإنستغرام وتيليجرام والهاتف خلال ثوانٍ، بالعربية والإنجليزية والروسية و+100 لغة، على مدار الساعة.</p>
<form class="capture rv d3" action="#" novalidate><input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"><label class="sr" for="cap-email">البريد الإلكتروني أو رقم واتساب</label>
<input id="cap-email" name="contact" type="text" placeholder="بريدك الإلكتروني أو رقم واتساب" autocomplete="email">
<button class="btn btn-p" type="submit">احصل على موظفي الذكي ←</button></form>
<p class="capture-note rv d3">مكالمة مجانية 30 دقيقة · يبدأ الإعداد خلال 24 ساعة · إلغاء في أي وقت</p>
</div>
<div class="stage rv"><div class="stage-card">
<div class="stage-side"><h3>ما فعله IRIS للتو، مباشرة</h3>
<ul class="feed"><li><span>ردّ</span><b>خلال 3 ثوانٍ</b></li><li><span>أهّل</span><b>الميزانية · نقداً أم تمويل</b></li><li><span>حجز</span><b>معاينة السبت 11 صباحاً</b></li><li><span>نبّه</span><b>الوكيلة على واتساب</b></li></ul></div>
<div class="phone" aria-label="مثال على محادثة مع IRIS"><div class="phone-top"><i></i><div>IRIS · العقارات<small>● متصل الآن</small></div></div>
<div class="msgs" style="display:flex;flex-direction:column;gap:8px" data-script='{json.dumps(script, ensure_ascii=False).replace("'", "&#39;")}'></div></div>
</div></div>
</section>

<!-- logos belt removed 12 Oct 2026 -->

<section class="sec"><div class="wrap">
<div class="center"><span class="eyebrow rv">إدارة كاملة</span><h2 class="rv d1">نحن نبنيه. وأنت فقط<br>تشاهد العملاء يصلون.</h2>
<p class="lead rv d2">لا قوالب تعدّها ولا أوامر تكتبها. فريقنا يربط قنواتك، ويدرّب الوكيل على شركتك، ويواصل تحسينه بعد الإطلاق.</p></div>
<div class="tl">
<div class="tl-i rv"><div class="tl-ic">{ico("plug")}</div><div class="tl-dot"></div><small>01</small><h3>نتعرّف على عملائك</h3><p class="muted">مكالمة 30 دقيقة لنعرف من أين تأتي استفساراتك وأين تضيع.</p></div>
<div class="tl-i rv d1"><div class="tl-ic">{ico("brain")}</div><div class="tl-dot"></div><small>02</small><h3>ندرّب وكيلك</h3><p class="muted">على خدماتك وأسعارك وأسئلتك الشائعة وطريقة حديث أفضل موظف مبيعات لديك.</p></div>
<div class="tl-i rv d2"><div class="tl-ic">{ico("rocket")}</div><div class="tl-dot"></div><small>03</small><h3>نطلقه</h3><p class="muted">الموقع وواتساب وتيليجرام وإنستغرام مربوطة ومختبرة، بما يشمل موافقة ميتا على واتساب.</p></div>
<div class="tl-i rv d3"><div class="tl-ic">{ico("chart")}</div><div class="tl-dot"></div><small>04</small><h3>تبيع أكثر</h3><p class="muted">كل عميل يُرد عليه ويُؤهّل، دون توظيف شخص إضافي.</p></div>
</div></div></section>

<section class="sec sec-lav" id="agents"><div class="wrap center">
<span class="eyebrow rv">تعرّف على الفريق</span><h2 class="rv d1">سبعة موظفين أذكياء.<br>واحد لكل مهمة.</h2>
<div class="cf rv d2"><button class="cf-nav cf-prev" aria-label="الوكيل السابق">›</button>{agents}<button class="cf-nav cf-next" aria-label="الوكيل التالي">‹</button></div>
<div class="cf-dots"></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="feat"><div class="feat-copy"><h2 class="rv">يستمعون.</h2>
<p class="lead rv d1">دردشة الموقع وواتساب وإنستغرام وتيليجرام والمكالمات، يتولاها فريقك الذكي الذي لا يفوّت أي رسالة، حتى الساعة 2 فجراً يوم الأحد.</p>
<div class="kv rv d2"><div><span>القنوات</span><b>الموقع · واتساب · إنستغرام · تيليجرام · المكالمات</b></div><div><span>اللغات</span><b>العربية · الإنجليزية · الروسية · +100</b></div><div><span>الساعات</span><b>24/7 حتى في العطل</b></div></div></div>
<div class="demo rv d1"><div class="hub"><svg viewBox="0 0 400 320" preserveAspectRatio="none" aria-hidden="true"><path d="M60 40 C150 60 170 130 200 160"/><path d="M340 60 C260 80 230 130 200 160"/><path d="M40 260 C120 230 170 190 200 160"/><path d="M350 290 C280 250 230 190 200 160"/><path d="M200 10 C200 60 200 110 200 160"/></svg>
<span class="ch">💬 الموقع</span><span class="ch">🟢 واتساب</span><span class="ch">📸 إنستغرام</span><span class="ch">📞 المكالمات</span><span class="ch">✈️ تيليجرام</span>
<div class="core mascot m-iris" aria-hidden="true"></div></div></div></div>

<div class="feat flip"><div class="feat-copy"><h2 class="rv">يجيبون.</h2>
<p class="lead rv d1">إجابات حقيقية من أسعارك وقوائمك وسياساتك، بأسلوبك. كل رد يقرّب العميل خطوة من الحجز.</p>
<div class="kv rv d2"><div><span>أول رد</span><b>خلال أقل من 5 ثوانٍ</b></div><div><span>مدرّب على</span><b>أسئلتك الشائعة وأسعارك ومنتجاتك</b></div><div><span>الهدف</span><b>حجز، وليس مجرد دردشة</b></div></div></div>
<div class="demo rv d1"><div class="phone" style="min-height:0;padding:0"><div class="msg u">توصلون أبوظبي؟</div><div class="msg b">نعم، التوصيل لأبوظبي مجاني للطلبات فوق 200 درهم، وعادةً في اليوم التالي.</div><div class="msg u">وهذا الفستان متوفر مقاس M؟</div><div class="msg b">مقاس M متوفر بالأسود والزمردي. أضيف لك الأسود للسلة؟</div><div class="msg u">إي لو سمحت</div><div class="msg b">تم 🛍️ هذا رابط الدفع.</div></div></div></div>

<div class="feat"><div class="feat-copy"><h2 class="rv">يسلّمون العميل.</h2>
<p class="lead rv d1">عندما يكون العميل جاهزاً، يصل لفريقك تنبيه على واتساب بكل ما يحتاجه: الاسم والرقم والميزانية والموعد والمحادثة كاملة.</p>
<div class="kv rv d2"><div><span>يُرسل العميل إلى</span><b>واتساب · Google Sheets · CRM</b></div><div><span>يشمل</span><b>التقييم والميزانية والموعد والمحادثة</b></div><div><span>تراه في</span><b>لوحة تحكم العميل</b></div></div></div>
<div class="demo"><div class="lead-card"><h4>عميل مؤهّل جديد · IRIS</h4><div class="row"><span>الاسم</span><b>أحمد ك.</b></div><div class="row"><span>يبحث عن</span><b>غرفتان، JVC</b></div><div class="row"><span>الميزانية</span><b>1.4 مليون درهم · تمويل</b></div><div class="row"><span>المعاينة</span><b>السبت 11:00</b></div><div class="score"><i></i></div><small class="muted">تقييم العميل 86 / 100</small></div>
<div class="alert"><i aria-hidden="true"></i><div><b>ديجي برومس · واتساب</b><small>🔥 عميل جاهز: أحمد ك.، غرفتان JVC، معاينة السبت 11 صباحاً</small></div></div></div></div>
</div></section>

{DASH}
<section class="sec sec-navy"><div class="wrap">
<div class="stats-dark"><div class="rv"><b data-to="300" data-suf="%">0%</b><span>متوسط زيادة التحويل</span></div><div class="rv d1"><b data-to="85" data-suf="%">0%</b><span>رضا العملاء</span></div><div class="rv d2"><b>24/7</b><span>كل عميل يُرد عليه</span></div><div class="rv d3"><b data-to="6" data-suf=" سنوات">0</b><span>نعمل لشركات الإمارات</span></div></div>
<div class="founder"><img class="rv" src="{A}founder-robot.webp" alt="رسم توضيحي لمالك، مؤسس ديجي برومس" width="320" height="320" loading="lazy"><div class="rv d1">
<blockquote>«الشركات لا تحتاج مزيداً من أدوات الذكاء الاصطناعي. تحتاج الذكاء الاصطناعي المناسب، مبنياً حول طريقة عملها. وهذا ما نقدمه.»</blockquote><cite>مالك · المؤسس ومستشار الذكاء الاصطناعي، ديجي برومس</cite>
<a class="btn btn-o" href="/ar/about/" style="margin-top:22px">اقرأ القصة ←</a></div></div>
</div></section>
<svg class="ribbon" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0h1440v30C1100 80 340 80 0 30z" fill="#120C2A"/></svg>

<section class="sec center" style="padding-top:40px"><div class="wrap">
<h2 class="rv">كل استفسار يُرد عليه.<br><span class="accent">على مدار الساعة.</span></h2>
<div class="btn-row rv d1" style="justify-content:center"><a class="btn btn-p" href="/ar/contact/">احجز عرضاً تجريبياً مجانياً ←</a><a class="btn btn-o" href="/ar/pricing/">شاهد الأسعار</a></div></div></section>
'''

faq_html = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><p>{e(a)}</p></details>' for i, (q, a) in enumerate(faqs))
main += f'''<section class="sec sec-pink" id="faq"><div class="wrap"><div class="center"><span class="eyebrow">الأسئلة الشائعة</span><h2>أسئلتك، بإجابات واضحة.</h2></div><div class="faq">{faq_html}</div></div></section>'''

PAGE = {'url': '/ar/', 'motion': True, 'noindex': True,
        'title': 'وكلاء وموظفون بالذكاء الاصطناعي للشركات | ديجي برومس',
        'description': 'تبني ديجي برومس من دبي وتدير وكلاء ذكاء اصطناعي يردون على كل عميل في موقعك وواتساب وإنستغرام وتيليجرام والهاتف ويؤهّلونه ويحجزون له خلال ثوانٍ، بأكثر من 100 لغة، على مدار الساعة.',
        'crumbs': [('الرئيسية', '/ar/')], 'faqs': faqs, 'sections': [('html', {'html': main})]}
