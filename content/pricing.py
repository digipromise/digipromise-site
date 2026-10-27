# /pricing/ — all 6 agents, plan B
import build as B
from build_parts import hero, head2, section

e = B.e
tabs = ''.join('<button role="tab" id="pt-' + p['id'] + '" aria-controls="' + p['id'] + '">' + p['name'] + ' <small style="font-weight:500;opacity:.7">· ' + e(p['category']) + '</small></button>' for p in B.P['products'])
panels = ''.join('<div class="tpanel-price" id="' + p['id'] + '" role="tabpanel" aria-labelledby="pt-' + p['id'] + '"' + ('' if i == 0 else ' hidden') + '>'
                 '<p class="center muted" style="margin:0 0 8px">' + e(p['title']) + ' · <a href="' + p['url'] + '">See how ' + p['name'] + ' works →</a></p>'
                 + B.pricing_block(p['id'], show_switch=False) + '</div>' for i, p in enumerate(B.P['products']))

included = [
    ('Setup &amp; training by our team', True, True, True, True),
    ('Website chat', True, True, True, True),
    ('WhatsApp', False, True, True, True),
    ('Instagram, Facebook &amp; Telegram', False, True, True, True),
    ('Bookings &amp; lead alerts', 'Lead capture', True, True, True),
    ('Client dashboard', False, 'Full dashboard', '+ reports', 'Custom + reports'),
    ('Trained on your full catalogue / listings', False, False, True, True),
    ('CRM integration', False, False, True, True),
    ('Premium AI models', False, False, 'On request', True),
    ('Dedicated account manager', False, False, False, True),
]
def yn(v):
    return '<span class="y">✓</span>' if v is True else ('<span class="n">✕</span>' if v is False else v)
rows = ''.join('<tr><th scope="row">' + r[0] + '</th>' + ''.join('<td' + (' class="us"' if k == 2 else '') + '>' + yn(v) + '</td>' for k, v in enumerate(r[1:])) + '</tr>' for r in included)
table = ('<div class="tbl-wrap rv" style="margin-top:36px;border:0"><table class="cmp"><thead><tr><th scope="col"></th><th scope="col">Starter</th><th scope="col">Growth</th>'
         '<th scope="col" class="us">Scale</th><th scope="col">Enterprise</th></tr></thead><tbody>' + rows + '</tbody></table></div>')

FAQS = [
    ('Is there a setup fee?', 'Monthly plans have a one-time setup fee that covers building, training and testing your agent. On annual plans it is fully waived on Starter and 50% off on Growth, Scale and Enterprise. Taking more than one plan for the same agent? You pay one setup fee, the higher one.'),
    ('How much do I save on an annual plan?', 'Annual plans are 15% cheaper than paying monthly. The setup fee is fully waived on Starter and 50% off on Growth, Scale and Enterprise.'),
    ('Can I cancel anytime?', 'Monthly plans can be cancelled anytime. Annual plans run for 12 months and are paid upfront.'),
    ('Do you bill in AED?', 'Yes. Businesses in Dubai and worldwide are billed in AED. Everyone else is billed in USD.'),
    ('Why is Enterprise quoted?', 'Enterprise depends on your message or call volume, the AI model you want and the systems we connect. We quote them so you only pay for what you need.'),
    ('What counts as a message?', 'Only the replies your AI agent sends count as messages. Messages your customers send are free. For example, 20,000 messages is about 2,000 conversations of 10 replies each. Stella plans include call minutes instead.'),
    ('Are WhatsApp fees included?', 'Replies to customers who message you first are included. If you send marketing or template messages through WhatsApp, Meta charges a small fee per message, passed through at cost.'),
    ('Is there a guarantee?', 'Yes. If you are not satisfied or change your mind, cancel any time and we refund the remaining amount under our refund policy. The setup fee is not refundable, because we agree your full scope before charging it. Monthly plans: cancel any time, and come back within 6 months without paying setup again. Annual plans: we refund what is left after the months used and the waived setup fee.'),
]

PAGE = {
    'url': '/pricing/', 'motion': True, 'noindex': True, 'greet': 'Not sure which plan fits? Tell me roughly how many leads or messages you get a month and I will recommend one.',
    'title': 'Pricing: AI Chatbot & AI Agent Plans in AED & USD | DigiPromise',
    'description': 'Simple monthly and annual plans for DigiPromise AI agents. Starter, Growth and Scale with fixed prices, Enterprise quoted. Save 15% annually, with up to 100% off the setup fee.',
    'crumbs': [('Home', '/'), ('Pricing', None)],
    'faqs': FAQS,
    'schema': [B.product_schema(p['id'], '/pricing/#' + p['id']) for p in B.P['products']],
    'sections': [
        ('html', {'html': hero([('Home', '/'), ('Pricing', None)], 'Simple, honest pricing',
                               'Pick your agent.<br>Pick your <span class="accent">plan.</span>',
                               'Fixed monthly prices for Starter, Growth and Scale, and a tailored quote for Enterprise. Save 15% with an annual plan, plus up to 100% off the setup fee.',
                               [('Compare plans ↓', '#plans', 'btn-p'), ('Get a quote', '/contact/', 'btn-o')])}),
        ('html', {'html': '<section class="sec sec-lav" id="plans"><div class="wrap center">' + B.switches() +
                  '<div class="ptabs" data-noauto aria-label="Choose an agent">' + tabs + '</div>' + panels + '</div></section>'}),
        ('html', {'html': section(head2('Compare plans', 'What every plan includes.') + table)}),
        ('faq', {'h2': 'Billing questions, answered.'}),
        ('cta', {'h2': 'Need something bigger or custom?', 'lead': 'Premium AI models, custom integrations, more volume or several agents together. Tell us what you need and we will quote it.'}),
    ],
}
