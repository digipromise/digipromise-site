# /whatsapp-automation/ — SEO service page
from build_parts import hero, head2, section, cards, agent_cards, steps, split, checklist
from build_product import chat_demo

FAQS = [
    ('What is WhatsApp automation?', 'WhatsApp automation means an AI agent replies to your customers on WhatsApp for you. It answers questions, qualifies leads, takes bookings and orders, sends reminders and alerts your team, 24/7.'),
    ('Do I need the WhatsApp Business API?', 'For a full AI agent, yes. We set up the official WhatsApp Business Platform (API) for you through Meta, verify your business and connect it to your agent. You keep your brand name and number.'),
    ('Can I keep my current WhatsApp number?', 'Usually yes. A number can move to the WhatsApp Business Platform, but it can then no longer be used in the normal WhatsApp app at the same time. We guide you through the options before switching.'),
    ('Does Meta charge for WhatsApp messages?', 'Meta charges per message for some template messages, such as marketing and utility messages you send first. Replies inside a customer-started conversation are typically free. Any Meta fees are passed through at cost.'),
    ('Is WhatsApp automation allowed in the UAE?', 'Yes. Using the official WhatsApp Business Platform is fully supported in the UAE. We follow Meta\'s policies, such as only messaging customers who opted in.'),
    ('Can my team still reply on WhatsApp?', 'Yes. Your team sees every conversation and can take over any chat. The AI steps back as soon as a human replies.'),
]

PAGE = {
    'url': '/whatsapp-automation/', 'motion': True, 'noindex': True,
    'title': 'WhatsApp Automation & WhatsApp AI Chatbot for Businesses in Dubai | DigiPromise',
    'description': 'Automate WhatsApp with an AI agent that replies in seconds, qualifies leads, books appointments and sends reminders. Official WhatsApp Business API setup included. Arabic & English.',
    'crumbs': [('Home', '/'), ('WhatsApp Automation', None)],
    'faqs': FAQS,
    'schema': [{'@type': 'Service', 'name': 'WhatsApp automation', 'serviceType': 'WhatsApp AI chatbot and automation',
                'provider': {'@id': 'https://digipromise.com/#org'}, 'areaServed': ['AE', 'SA', 'QA', 'KW', 'BH', 'OM']}],
    'sections': [
        ('html', {'html': hero([('Home', '/'), ('WhatsApp Automation', None)], '🟢 WhatsApp automation · Dubai &amp; worldwide',
                               'Your WhatsApp,<br>answered <span class="accent">24/7.</span>',
                               'In the UAE, customers want to WhatsApp you, not fill in forms. DigiPromise puts an AI agent on your WhatsApp that replies in seconds, qualifies leads, books appointments and alerts your team.',
                               [('Automate my WhatsApp →', '/contact/', 'btn-p'), ('See pricing', '/pricing/', 'btn-o')])}),
        ('html', {'html': section(split('<h2 class="rv">More than auto-replies.</h2><p class="lead rv d1">Old WhatsApp bots sent a menu of numbers. Our AI agents hold a real conversation in Arabic or English and actually move the customer to a booking or sale.</p>' +
                                        checklist(['Understands free-text questions in any language', 'Answers from your prices, services and policies', 'Books, takes orders and sends payment links', 'Hands over to your team instantly when needed']),
                                        '<div class="demo rv">' + chat_demo([('u', 'السلام عليكم، كم سعر الباقة الشهرية؟'), ('b', 'وعليكم السلام! الباقة الشهرية بـ 399 درهم وتشمل جميع الحصص. هل تحب تجرب حصة مجانية؟'),
                                                                               ('u', 'Yes please, tomorrow evening?'), ('b', 'Done ✅ Free trial booked for tomorrow at 7pm. See you then!')]) + '</div>'))}),
        ('html', {'html': section(head2('What you can automate', 'Everything customers<br>WhatsApp you about.') + cards([
            ('💬', 'Enquiries &amp; FAQs', 'Prices, availability, locations and policies, answered instantly.'),
            ('🎯', 'Lead qualification', 'Budget, need and timeline captured before your team calls.'),
            ('📅', 'Bookings', 'Appointments, viewings, tables and test drives, booked in chat.'),
            ('🛒', 'Orders &amp; payments', 'Product questions, checkout and payment links.'),
            ('🔔', 'Reminders &amp; follow-ups', 'Booking reminders, abandoned carts and renewals.'),
            ('📲', 'Team alerts', 'Hot leads and bookings sent to the right person instantly.')]), 'sec-lav')}),
        ('html', {'html': section(head2('Setup', 'Official WhatsApp API,<br>set up for you.') + steps([
            ('Meta verification', 'We set up your WhatsApp Business Platform account and verify your business with Meta.'),
            ('Agent training', 'Your AI agent learns your services, prices, FAQs and tone.'),
            ('Go live', 'Your WhatsApp number starts answering 24/7, with your team in control.')]), 'sec-navy')}),
        ('html', {'html': section(head2('Pick your agent', 'WhatsApp automation,<br>built for your industry.') + agent_cards('Explore'))}),
        ('faq', {'h2': 'WhatsApp automation, explained.'}),
        ('cta', {'h2': 'Stop missing WhatsApp messages.', 'lead': 'Book a free 30-minute call and we will show you how your WhatsApp could answer itself.'}),
    ],
}
