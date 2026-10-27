# Hidden test page to prove the template + router work on the live server. noindex, not in sitemap.
PAGE = {
    'url': '/dp-test/',
    'noindex': True,
    'title': 'Template test – DigiPromise',
    'description': 'Internal template test page.',
    'product': 'iris',
    'crumbs': [('Home', '/'), ('AI Agents', '/ai-agents/'), ('Template test', None)],
    'faqs': [
        ('Is there a setup fee?', 'Monthly plans have a one-time setup fee. On annual plans it is fully waived on Starter and 50% off on Growth, Scale and Enterprise. Enterprise is quoted.'),
        ('Can I cancel anytime?', 'Monthly plans cancel anytime. Annual plans run 12 months, paid upfront.'),
        ('Do you bill in AED?', 'Yes. GCC clients are billed in AED, everyone else in USD.'),
    ],
    'sections': [
        ('hero', {
            'eyebrow': '🇦🇪 Template test · not public',
            'h1': 'If you can read this, <span class="accent">the template works.</span>',
            'lead': 'This hidden page checks the shared header, footer, fonts, currency switch, pricing block and chat widget on the live server.',
            'buttons': [('See pricing →', '#pricing', 'btn-p'), ('Book a demo', '/contact/', 'btn-o')],
            'without_label': 'Without DigiPromise', 'without': [('🕐', 'Lead messages at 11pm. You reply at 9am.'), ('🌐', 'Arabic visitor. No Arabic support.')],
            'with_label': 'With DigiPromise', 'with': [('⚡', 'AI replies in seconds, 24/7.'), ('📲', 'You get a WhatsApp alert instantly.')],
        }),
        ('ticker', ['300% avg conversion increase', '24/7 coverage, nights &amp; weekends', 'Arabic, English &amp; 100+ languages', 'Setup starts in 24 hours']),
        ('steps', {'eyebrow': 'How it works', 'h2': 'Live in 3 steps', 'steps': [
            ('Book a call', '30 minutes to map your leads.'), ('We train the agent', 'On your data and tone.'), ('Go live', 'Setup starts within 24 hours.')]}),
        ('pricing', {'eyebrow': 'Pricing', 'h2': 'IRIS pricing'}),
        ('faq', {'h2': 'Questions'}),
        ('cta', {'h2': 'Template test complete', 'lead': 'Reply "dn" in chat once this page loads correctly.'}),
    ],
}
