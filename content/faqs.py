# /faqs/ — grouped FAQ hub
import build as B
from build_parts import hero, section

GROUPS = [
    ('About our AI agents', [
        ('What does a DigiPromise AI agent do?', 'It replies to your customers on your website, WhatsApp, Instagram and phone in seconds, answers from your own information, qualifies leads, books appointments and sends hot leads to your team on WhatsApp.'),
        ('Which agent should I choose?', 'IRIS for real estate, AURA for ecommerce, Nova for restaurants and hotels, Luna for clinics, gyms and studios, Lara for car rental and Stella for phone calls. Not sure? Book a call and we will recommend one.'),
        ('Do the agents speak Arabic?', 'Yes. Every agent replies in Arabic, English and 100+ other languages, automatically matching the customer.'),
        ('Will customers know they are talking to AI?', 'Yes. Our agents introduce themselves as AI assistants and hand over to your team whenever a human is needed.'),
    ]),
    ('Setup &amp; support', [
        ('Do you set everything up?', 'Yes. We train the agent on your business, connect your channels, test it with you and keep improving it after launch.'),
        ('How long does setup take?', 'Setup starts within 24 hours of your kickoff call, and we agree the go-live date with you on that call. WhatsApp goes live as soon as Meta approves your business account; we prepare and submit everything for you. Custom integrations can take 2 to 4 weeks.'),
        ('Do I need any technical knowledge?', 'No. We handle everything technical. You review and approve.'),
        ('Can my team take over conversations?', 'Yes. Your team sees every conversation and can step in at any time.'),
    ]),
    ('Pricing &amp; billing', [
        ('Is there a setup fee?', 'Monthly plans have a one-time setup fee. Annual plans save 15%, with the setup fee fully waived on Starter and 50% off on Growth, Scale and Enterprise.'),
        ('Can I cancel anytime?', 'Monthly plans cancel anytime. Annual plans run for 12 months, paid upfront.'),
        ('Do you bill in AED?', 'Yes. Businesses in Dubai and worldwide are billed in AED, everyone else in USD.'),
        ('Is there a guarantee?', 'Yes. If you are not satisfied or change your mind, cancel any time and we refund the remaining amount under our refund policy. The setup fee is not refundable, because we agree your full scope before charging it. Monthly plans: cancel any time, and come back within 6 months without paying setup again. Annual plans: we refund what is left after the months used and the waived setup fee.'),
    ]),
]

blocks = ''.join('<h2 class="rv" style="font-size:24px;margin:48px 0 8px">' + g + '</h2><div class="faq" style="margin-top:0">' +
                 ''.join('<details><summary>' + B.e(q) + '</summary><p>' + B.e(a) + '</p></details>' for q, a in items) + '</div>' for g, items in GROUPS)

PAGE = {
    'url': '/faqs/', 'motion': True, 'noindex': True,
    'title': 'FAQs: AI Agents, Setup & Pricing | DigiPromise',
    'description': 'Answers to common questions about DigiPromise AI agents: what they do, Arabic support, setup time, pricing, billing in AED and our refund policy.',
    'crumbs': [('Home', '/'), ('FAQs', None)],
    'faqs': [qa for _, items in GROUPS for qa in items],
    'sections': [
        ('html', {'html': hero([('Home', '/'), ('FAQs', None)], 'FAQs', 'Questions, <span class="accent">answered.</span>',
                               'Everything you need to know about our AI agents, setup and pricing. Can\'t find your answer? WhatsApp us.',
                               [('WhatsApp us', 'https://wa.me/971585456331', 'btn-wa')], trust=False)}),
        ('html', {'html': section('<div class="prose">' + blocks + '</div>', 'sec-pink')}),
        ('cta', {'h2': 'Still have a question?', 'lead': 'Book a free 30-minute call or WhatsApp us and a real person will answer.'}),
    ],
}
