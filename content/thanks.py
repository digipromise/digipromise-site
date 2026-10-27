# /thanks/ — shown after a site form is sent (engine replied ok:true). noindex. Not the Stripe /thank-you/ page.
from build_parts import hero

PAGE = {
    'url': '/thanks/', 'motion': True, 'noindex': True, 'always_noindex': True,
    'title': 'Thanks, we have your request | DigiPromise',
    'description': 'Your request has reached the DigiPromise team.',
    'crumbs': [('Home', '/'), ('Thanks', None)],
    'sections': [
        ('html', {'html': hero([], 'Request received', 'Thanks — we’ve got<br><span class="accent">your request.</span>',
                               'Our team will contact you within 1 business hour (Sun–Fri, 9am–6pm Dubai) by WhatsApp or email. Want to talk now?',
                               [('WhatsApp us →', 'https://wa.me/971585456331', 'btn-p'), ('Back to home', '/', 'btn-o')], trust=False)}),
    ],
}
