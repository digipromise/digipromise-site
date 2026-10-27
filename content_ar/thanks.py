# /ar/thanks/ — بعد إرسال نموذج الموقع بنجاح. noindex.
from build_parts import hero

PAGE = {
    'url': '/ar/thanks/', 'motion': True, 'noindex': True, 'always_noindex': True,
    'title': 'شكراً، وصلنا طلبك | ديجي برومس',
    'description': 'وصل طلبك إلى فريق ديجي برومس.',
    'crumbs': [('الرئيسية', '/ar/'), ('شكراً', None)],
    'sections': [
        ('html', {'html': hero([], 'تم استلام الطلب', 'شكراً — <span class="accent">وصلنا طلبك.</span>',
                               'سيتواصل معك فريقنا خلال ساعة عمل واحدة (من الأحد إلى الجمعة، 9 صباحاً حتى 6 مساءً بتوقيت دبي) عبر واتساب أو البريد الإلكتروني. تريد التحدث الآن؟',
                               [('راسلنا على واتساب ←', 'https://wa.me/971585456331', 'btn-p'), ('العودة للرئيسية', '/ar/', 'btn-o')], trust=False)}),
    ],
}
