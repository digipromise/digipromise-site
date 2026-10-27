# /ai-chatbot-development/ — SEO service page routing to the 6 agents
from build_parts import hero, head2, section, cards, agent_cards, steps, split, checklist

FAQS = [
    ('How much does AI chatbot development cost in Dubai?', 'With DigiPromise, ready-built industry agents start from the monthly prices shown on our pricing page, with a one-time setup fee or no setup fee on annual plans. Fully custom chatbots with special integrations are quoted after a short call.'),
    ('How long does it take to build an AI chatbot?', 'Our industry agents are ready to build on, so setup starts within 24 hours of your kickoff call. Custom builds with deeper integrations usually take 2 to 4 weeks.'),
    ('Can the chatbot speak Arabic?', 'Yes. Every chatbot we build understands and replies in Arabic and English, plus 100+ other languages, and switches automatically to the customer\'s language.'),
    ('Which channels can the chatbot work on?', 'Your website, WhatsApp Business, Instagram, Facebook Messenger and Telegram. Our Stella agent also handles phone calls.'),
    ('Do I need technical knowledge?', 'No. We handle the build, training, integrations, testing and ongoing improvements. You just review and approve.'),
    ('Can the chatbot connect to my CRM?', 'Yes. We connect to Google Sheets, HubSpot, Zoho and most CRMs through webhooks, so every lead lands where your team works.'),
]

PAGE = {
    'url': '/ai-chatbot-development/', 'motion': True, 'noindex': True,
    'title': 'AI Chatbot Development Company in Dubai | DigiPromise',
    'description': 'DigiPromise builds AI chatbots for businesses in Dubai and worldwide: Arabic & English, website and WhatsApp, trained on your data and live in days. Ready-built industry agents or custom builds.',
    'crumbs': [('Home', '/'), ('AI Chatbot Development', None)],
    'faqs': FAQS,
    'schema': [{'@type': 'Service', 'name': 'AI chatbot development', 'serviceType': 'AI chatbot development',
                'provider': {'@id': 'https://digipromise.com/#org'}, 'areaServed': ['AE', 'SA', 'QA', 'KW', 'BH', 'OM']}],
    'sections': [
        ('html', {'html': hero([('Home', '/'), ('AI Chatbot Development', None)], 'AI chatbot development · Dubai',
                               'AI chatbots that<br><span class="accent">actually sell.</span>',
                               'We design, build, train and run AI chatbots for businesses in Dubai and worldwide. Arabic and English, on your website and WhatsApp, connected to your CRM and live in days, not months.',
                               [('Book a free consultation →', '/contact/', 'btn-p'), ('See ready-built agents', '#agents', 'btn-o')])}),
        ('html', {'html': section(head2('Why DigiPromise', 'Not another<br>button-menu bot.') + cards([
            ('🧠', 'Trained on your business', 'Your services, prices, FAQs, policies and tone of voice, not generic answers.'),
            ('🇦🇪', 'Arabic &amp; English, natively', 'Built for GCC customers who switch between Arabic, English and other languages.'),
            ('🎯', 'Built to convert', 'Every chatbot qualifies, books and hands over leads, not just answers questions.'),
            ('🔌', 'Connected to your tools', 'WhatsApp, Instagram, Telegram, website, Google Sheets, HubSpot, Zoho and more.'),
            ('📈', 'Measured', 'A client dashboard shows conversations, leads and results.'),
            ('🛠️', 'Managed for you', 'We monitor, improve and update your chatbot every month.')]))}),
        ('html', {'html': section(head2('Ready-built agents', 'Start faster with an agent<br>built for your industry.', 'Most businesses do not need a chatbot built from zero. Our industry agents are ready to train on your data, with setup starting within 24 hours.') + agent_cards('Explore'), 'sec-lav', 'agents')}),
        ('html', {'html': section(head2('Our process', 'From first call to live<br>chatbot in days.') + steps([
            ('Discovery call', 'We map your customer questions, channels and goals in 30 minutes.'),
            ('Build &amp; train', 'We build the chatbot, train it on your data and connect your channels.'),
            ('Launch &amp; improve', 'We test with you, go live and improve it every month.')]), 'sec-navy')}),
        ('html', {'html': section(split('<h2 class="rv">Need something custom?</h2><p class="lead rv d1">Special integrations, internal tools, multi-branch routing or premium AI models. We build custom AI chatbots and agents on the same proven platform.</p>' +
                                        checklist(['Custom integrations with your systems', 'Premium AI models for complex questions', 'Multi-language, multi-branch setups', 'Internal assistants for your team']) +
                                        '<div class="btn-row rv"><a class="btn btn-p" href="/contact/">Get a custom quote →</a></div>',
                                        '<div class="demo rv"><div class="hub"><svg viewBox="0 0 400 320" preserveAspectRatio="none" aria-hidden="true"><path d="M60 40 C150 60 170 130 200 160"/><path d="M340 60 C260 80 230 130 200 160"/><path d="M40 260 C120 230 170 190 200 160"/><path d="M350 290 C280 250 230 190 200 160"/><path d="M200 10 C200 60 200 110 200 160"/></svg><span class="ch">🧡 HubSpot</span><span class="ch">🟢 WhatsApp</span><span class="ch">📊 Sheets</span><span class="ch">🛒 Shopify</span><span class="ch">🔗 Your API</span><div class="core mascot m-iris" aria-hidden="true"></div></div></div>'))}),
        ('faq', {'h2': 'AI chatbot development, explained.'}),
        ('cta', {'h2': 'Let\'s build your AI chatbot.', 'lead': 'Book a free 30-minute consultation. We will show you what your chatbot could handle and what it would cost.'}),
    ],
}
