# /ai-agents/ — hub for the 6 agents
from build_parts import hero, head2, section, cards, agent_cards, steps

FAQS = [
    ('What is an AI agent for business?', 'An AI agent is software that talks to your customers for you. It replies to messages and calls, answers questions from your own information, books appointments and sends qualified leads to your team, 24 hours a day.'),
    ('How is a DigiPromise agent different from a normal chatbot?', 'A normal chatbot follows fixed buttons and scripts. Our agents understand free-text questions in Arabic, English and 100+ languages, are trained on your business, take actions like bookings and are set up and managed for you.'),
    ('Which agent is right for my business?', 'Pick the agent built for your industry: IRIS for real estate, AURA for ecommerce, Nova for restaurants and hotels, Luna for clinics, gyms and studios, Lara for car rental and Stella for phone calls. If you are not sure, book a call and we will recommend one.'),
    ('Can I use more than one agent?', 'Yes. Many businesses combine a chat agent with Stella for phone calls. All your agents report into one client dashboard.'),
    ('Do you set everything up?', 'Yes. We train the agent on your business, connect your channels, test it with you and keep improving it after launch. You do not need any technical skills.'),
    ('How much do the agents cost?', 'Plans start from the prices shown on each agent card. Monthly plans have a one-time setup fee. Annual plans save 15%, with the setup fee fully waived on Starter and 50% off on Growth, Scale and Enterprise.'),
]

PAGE = {
    'url': '/ai-agents/', 'motion': True, 'noindex': True, 'greet': 'Not sure which agent fits your business? Tell me what you sell and I will point you to the right one.',
    'title': 'AI Agents for Businesses in Dubai & Worldwide: Chat, WhatsApp & Calling Agents | DigiPromise',
    'description': 'Seven AI agents for businesses in Dubai and worldwide: real estate, ecommerce, hospitality, health & fitness, car rental and phone calls. Fully managed setup, Arabic & English, 24/7.',
    'crumbs': [('Home', '/'), ('AI Agents', None)],
    'faqs': FAQS,
    'schema': [],
    'sections': [
        ('html', {'html': hero([('Home', '/'), ('AI Agents', None)], 'AI agents for businesses in Dubai &amp; worldwide',
                               'One AI agent for<br>every <span class="accent">industry.</span>',
                               'Each DigiPromise agent is trained for one industry, speaks Arabic and English, works 24/7 and is set up and run for you. Pick yours below.',
                               [('Find my agent ↓', '#agents', 'btn-p'), ('Book a demo', '/contact/', 'btn-o')])}),
        ('html', {'html': section(head2('Meet the team', 'Seven AI employees.<br>Built for your business.') + agent_cards(), 'sec-lav', 'agents')}),
        ('html', {'html': section(head2('What every agent does', 'Same promise,<br>whatever you sell.') + cards([
            ('⚡', 'Replies in seconds', 'Every message and call answered in under 5 seconds, day and night.'),
            ('🌍', 'Arabic, English &amp; 100+', 'Replies in the language your customer uses, automatically.'),
            ('🎯', 'Qualifies &amp; books', 'Asks the right questions, books the next step and scores every lead.'),
            ('📲', 'Alerts your team', 'Hot leads and bookings sent to your team on WhatsApp instantly.'),
            ('📈', 'Client dashboard', 'Every conversation, lead and result in one place, from Growth up.'),
            ('🛠️', 'Fully managed by our team', 'We build, train, launch and keep improving it. No tech skills needed.')]))}),
        ('html', {'html': section(head2('How it works', 'Live in days,<br>not months.') + steps([
            ('Book a 30-minute call', 'We look at where your leads come from and where they get lost.'),
            ('We build your agent', 'Trained on your services, prices, FAQs and tone of voice.'),
            ('Go live and grow', 'Connected to your channels and improved every month.')]), 'sec-navy')}),
        ('faq', {'h2': 'AI agents, explained.'}),
        ('cta', {'h2': 'Not sure which agent fits?', 'lead': 'Book a free 30-minute call and we will recommend the right agent and plan for your business.'}),
    ],
}
