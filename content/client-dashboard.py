# /client-dashboard/
from build_parts import app_dash, hero, head2, section, cards, split, checklist

MOCK = app_dash('en')

FAQS = [
    ('What is the DigiPromise client dashboard?', 'It is your private online dashboard where you see every conversation your AI agent has had, every lead it captured and the chats it handed to your team.'),
    ('Which plans include the dashboard?', 'Growth and above include the client dashboard. Enterprise can get a custom dashboard. Starter does not include the dashboard.'),
    ('Can I download my leads?', 'Yes. Export your leads as a CSV file for the last 30 days, 90 days or 12 months.'),
    ('Can I change what my agent says?', 'Yes. Review any conversation and send us the change. Our team updates your agent for you.'),
    ('Is my data secure?', 'Your data is only used to run your agent and your dashboard. We never sell it, and you can ask us to export or delete it at any time.'),
]

PAGE = {
    'url': '/client-dashboard/', 'motion': True, 'noindex': True,
    'title': 'Client Dashboard: See Every Lead & Chat | DigiPromise',
    'description': 'The DigiPromise client dashboard shows every conversation and lead your AI agent handles, plus your message usage, lead conversion and the chats handed to your team.',
    'crumbs': [('Home', '/'), ('Client Dashboard', None)],
    'faqs': FAQS,
    'sections': [
        ('html', {'html': hero([('Home', '/'), ('Client Dashboard', None)], 'Your AI agent, fully visible',
                               'See every lead your<br>agent <span class="accent">brings in.</span>',
                               'Every chat, lead and handover in one dashboard. Know exactly what your AI agent is doing and what it is worth to your business.',
                               [('Book a demo →', '/contact/', 'btn-p'), ('See plans', '/pricing/', 'btn-o')], extra='<div style="margin-top:56px">' + MOCK + '</div>', trust=False)}),
        ('html', {'html': section(head2("What's inside", 'Everything your agent does,<br>in one place.') + cards([
            ('📊', 'Overview', 'Chats, leads captured and chats handed to your team, for the last 7, 30 or 90 days.'),
            ('🔢', 'Plan usage', 'See how many AI replies you have used this month against your plan.'),
            ('🎯', 'Lead conversion', 'What share of chats became leads, and how many your agent answered without help.'),
            ('💬', 'Every conversation', 'Read the full chat for every customer, on every channel.'),
            ('🙋', 'Needs your attention', 'Chats your agent handed to your team, so nobody waits for a reply.'),
            ('⬇️', 'Leads &amp; export', 'Everyone who shared their contact details, ready to download as CSV.')]), 'sec-lav')}),
        ('html', {'html': section(split('<h2 class="rv">Proof, not promises.</h2><p class="lead rv d1">Most businesses never know how many leads they lose. The dashboard shows you exactly how many chats your agent handled and how many became leads.</p>' +
                                        checklist(['Chats per day for the last 14 days', 'Leads captured and lead conversion', 'Chats answered without help vs handed to your team']),
                                        '<div class="demo rv"><div class="lead-card"><h4>📈 Last 30 days</h4><div class="row"><span>Chats</span><b>214</b></div><div class="row"><span>Leads captured</span><b>58</b></div><div class="row"><span>Answered without help</span><b>96%</b></div><div class="row"><span>Handed to your team</span><b>9</b></div><div class="score"><i style="width:27%"></i></div><small class="muted">Example data</small></div></div>'))}),
        ('faq', {'h2': 'Dashboard questions, answered.'}),
        ('cta', {'h2': 'See it with your own data.', 'lead': 'Book a 30-minute demo and we will walk you through the dashboard.'}),
    ],
}
