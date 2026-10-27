# /ai-employees/ — SEO page for "AI employee(s)" (US + global first; low competition, 12 Oct 2026)
from build_parts import hero, head2, section, cards, agent_cards, steps, split, checklist

FAQS = [
    ('What is an AI employee?', 'An AI employee is an AI agent trained to do one job in your business, such as answering enquiries, qualifying leads, booking appointments or making follow-up calls. It works on your real channels (website, WhatsApp, Instagram, Telegram, phone), follows your rules and hands over to your team when a person is needed.'),
    ('How much does an AI employee cost?', 'DigiPromise AI employees start from $685 (AED 2,500) a month, plus a one-time setup fee from $1,365 (AED 5,000). Pay annually and you save 15%, with the setup fee fully waived on Starter and 50% off on other plans. See the pricing page for every plan.'),
    ('Will an AI employee replace my staff?', 'It replaces the repetitive part of the job, not your team. Your AI employee answers the same questions, chases the same leads and books the same appointments around the clock, so your people spend their time on customers who are ready to buy.'),
    ('Do you work with businesses in the United States?', 'Yes. We work with businesses in the US, the UAE and worldwide. US clients are billed in USD, and your AI employee works in your time zone, 24/7.'),
    ('What languages can an AI employee speak?', 'English, Arabic, Spanish, Russian and 100+ other languages. It replies in the language your customer writes in.'),
    ('Do I need technical skills?', 'No. Our team builds, trains, connects and manages your AI employee. You approve the scope and see every conversation and lead in your dashboard.'),
    ('How is an AI employee different from a chatbot?', 'A basic chatbot follows fixed buttons and scripts. An AI employee understands free-text questions, is trained on your services, prices and policies, takes actions such as booking and lead capture, and connects to your CRM.'),
]

PAGE = {
    'url': '/ai-employees/', 'motion': True,
    'title': 'AI Employees for Business: Hire an AI Employee | DigiPromise',
    'description': 'Hire an AI employee that answers every lead, books appointments and follows up 24/7 on your website, WhatsApp and phone. Built and managed for you, from $685/month. US, UAE and worldwide.',
    'crumbs': [('Home', '/'), ('AI Employees', None)],
    'faqs': FAQS,
    'schema': [{'@type': 'Service', 'name': 'AI employees for business', 'serviceType': 'AI employee / AI agent',
                'provider': {'@id': 'https://digipromise.com/#org'}, 'areaServed': ['US', 'AE', 'SA', 'Worldwide']}],
    'sections': [
        ('html', {'html': hero([('Home', '/'), ('AI Employees', None)], 'AI employees for business · US, UAE &amp; worldwide',
                               'AI employees that<br><span class="accent">never clock out.</span>',
                               'Hire an AI employee for the work your team never catches up on: answering every call and message, qualifying leads, booking appointments and following up. Trained on your business and managed by our team, from $685 a month.',
                               [('Book a free consultation →', '/contact/', 'btn-p'), ('Meet the AI employees', '#agents', 'btn-o')])}),
        ('html', {'html': section(split(
            '<span class="eyebrow rv">The basics</span><h2 class="rv d1">What is an AI employee?</h2>'
            '<p class="rv d2">An AI employee is an AI agent trained to do one job in your business, the way a new hire would. It learns your services, prices and policies, works on the channels your customers already use, and follows the rules you set.</p>'
            '<p class="rv d2">Unlike a new hire, it starts in days, works 24/7, answers in seconds and never forgets to follow up. And when a customer needs a person, it hands over to your team with the full conversation.</p>',
            checklist(['Answers every enquiry in seconds, day and night', 'Qualifies leads and books appointments', 'Works on website, WhatsApp, Instagram, Telegram and phone', 'Speaks English, Arabic, Spanish and 100+ languages', 'Connects to your CRM and calendar', 'Built, trained and managed by our team'])))}),
        ('html', {'html': section(head2('Roles', 'One AI employee<br>for every repetitive job.') + cards([
            ('📞', 'AI receptionist', 'Answers calls and messages, books appointments and routes urgent requests to your team.'),
            ('💼', 'AI sales rep', 'Replies to every lead in seconds, asks the right questions and books the meeting.'),
            ('📅', 'AI booking coordinator', 'Checks availability, confirms bookings and sends reminders to cut no-shows.'),
            ('🛒', 'AI store assistant', 'Answers product and order questions and recovers abandoned carts.'),
            ('☎️', 'AI caller', 'Calls new leads and past customers, follows up and reports results.'),
            ('🧑‍💼', 'AI personal assistant', 'Sorts your inbox, calendar and reminders so you keep the CEO hours.')]), 'sec-lav')}),
        ('html', {'html': section('<div class="center"><span class="eyebrow rv">Compare</span><h2 class="rv d1">AI employee vs a new hire.</h2></div>'
            '<div class="tbl-wrap rv d2" style="margin-top:36px;border:0"><table class="cmp"><thead><tr><th scope="col"></th><th scope="col">New hire</th><th scope="col" class="us">AI employee</th></tr></thead><tbody>'
            '<tr><th scope="row">Time to start</th><td>Weeks of hiring and training</td><td class="us">Setup starts within 24 hours</td></tr>'
            '<tr><th scope="row">Working hours</th><td>Office hours</td><td class="us">24/7, weekends and holidays</td></tr>'
            '<tr><th scope="row">Reply speed</th><td>Minutes to hours</td><td class="us">Seconds</td></tr>'
            '<tr><th scope="row">Languages</th><td>One or two</td><td class="us">100+</td></tr>'
            '<tr><th scope="row">Conversations at once</th><td>One</td><td class="us">Unlimited</td></tr>'
            '<tr><th scope="row">Monthly cost</th><td>Salary, visa, benefits, office</td><td class="us">From $685 / AED 2,500</td></tr>'
            '</tbody></table></div>')}),
        ('html', {'html': section(head2('Meet the team', 'Seven AI employees.<br>Pick the one your business needs.') + agent_cards('Meet'), 'sec-lav', 'agents')}),
        ('html', {'html': section(head2('How it works', 'From first call to working<br>AI employee.') + steps([
            ('Free consultation', 'We look at where your business loses time and leads, and which job an AI employee should take first.'),
            ('Build &amp; train', 'We train your AI employee on your business and connect your channels and CRM.'),
            ('Launch &amp; manage', 'We test with you, go live and keep improving it every month.')]), 'sec-navy')}),
        ('faq', {'h2': 'AI employees, explained.'}),
        ('cta', {'h2': 'Hire your first AI employee.', 'lead': 'Book a free 30-minute consultation. We will show you which job AI can take over first and what it would cost.'}),
    ],
}
