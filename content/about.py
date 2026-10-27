# /about/
from build_parts import hero, head2, section, cards, split, checklist

PAGE = {
    'url': '/about/', 'motion': True, 'noindex': True,
    'title': 'About DigiPromise: AI Agents Built in Dubai for Businesses Worldwide',
    'description': 'DigiPromise is a Dubai-based AI company building fully managed AI agents for businesses in Dubai and worldwide, helping founders adopt AI the right way, from consultation to fully managed AI employees.',
    'crumbs': [('Home', '/'), ('About', None)],
    'schema': [{'@type': 'AboutPage', 'name': 'About DigiPromise', 'about': {'@id': 'https://digipromise.com/#org'}},
               {'@type': 'Person', 'name': 'Malik', 'jobTitle': 'Founder & AI Consultant', 'worksFor': {'@id': 'https://digipromise.com/#org'}}],
    'sections': [
        ('html', {'html': hero([('Home', '/'), ('About', None)], 'About DigiPromise', 'Built in Dubai,<br>for <span class="accent">businesses worldwide.</span>',
                               'We help businesses adopt AI the right way: we find where AI pays off for you, then build and run the AI employees that deliver it.',
                               [('Meet our AI employees →', '/ai-agents/', 'btn-p'), ('Contact us', '/contact/', 'btn-o')], trust=False)}),
        ('html', {'html': section(split(
            '<span class="eyebrow rv">Our story</span><h2 class="rv d1" style="font-size:clamp(28px,3.6vw,44px)">The story behind DigiPromise</h2>'
            '<p class="rv d2">Most business owners I meet don\'t need another AI tool. They need someone to tell them, honestly, what AI should do in their business, and what it shouldn\'t.</p>'
            '<p class="rv d2">Every week a new AI tool launches, each one promising to change everything. Founders and CEOs know AI matters, but they are stuck. Which tool is real? Where do I start? Do I need to hire an AI team? Will it cost millions of dirhams? So they wait, or they buy three tools that don\'t talk to each other, and nothing changes.</p>'
            '<p class="rv d2">That gap is where I work. I\'m Malik, an AI consultant and builder. I design and build AI employees, AI agents and business automations, written in Python and connected to the tools a business already uses. But the most valuable part of my work happens before anything is built: understanding the business.</p>'
            '<p class="rv d2"><b>Businesses don\'t need AI for its own sake. They need more customers answered, fewer hours lost, and growth without adding headcount.</b></p>'
            '<p class="rv d2">So every DigiPromise project starts with a consultation, not a sales pitch. We map where your business loses time, leads and money. We decide which work AI should take over first, which tools you can safely ignore, and what results to expect, in plain language. Then we build only the solution that fits your business and pays for itself.</p>'
            '<p class="rv d2">Some businesses need an AI employee that answers every WhatsApp enquiry in seconds. Some need their sales follow-up automated. Some need a step-by-step plan to move their whole team to AI. Our job is to find the right answer for you, build it and run it, so you get the benefits of AI without hiring a team or building an AI department.</p>'
            '<p class="rv d2">Started in Dubai. Guiding businesses anywhere.</p>'
            '<p class="rv d2" style="font-size:20px;font-weight:700;color:var(--ink)">The promise is simple: the right AI for your business, without the confusion.</p>'
            '<p class="rv d2 muted">Malik, Founder &amp; AI Consultant, DigiPromise</p>',
            '<figure class="rv" style="margin:0;text-align:center"><img src="/wp-content/themes/aimo/dp-pages/assets/founder-robot.webp" alt="Malik, founder of DigiPromise" width="320" height="320" style="margin:0 auto;width:100%;max-width:300px;height:auto;border-radius:24px;box-shadow:0 30px 60px rgba(18,12,42,.25)"><figcaption class="muted" style="margin-top:12px;font-size:14px">Malik · Founder &amp; AI Consultant</figcaption></figure>'))}),
        ('html', {'html': section('<div class="stats-dark"><div class="rv"><b data-to="6" data-suf=" yrs">0</b><span>Building for UAE businesses</span></div>'
                                  '<div class="rv d1"><b data-to="100" data-suf="+">0</b><span>Languages supported</span></div>'
                                  '<div class="rv d2"><b data-to="300" data-suf="%">0%</b><span>Avg conversion increase</span></div>'
                                  '<div class="rv d3"><b data-to="85" data-suf="%">0%</b><span>Client satisfaction</span></div></div>', 'sec-navy')}),
        ('html', {'html': section(head2('What we believe', 'How we work.') + cards([
            ('⚡', 'Speed wins', 'The business that replies first usually wins the customer. Our agents reply in seconds.'),
            ('🤝', 'Fully managed by our team', 'You run your business. We build, train, launch and improve your agent.'),
            ('🔍', 'Honest AI', 'Our agents say they are AI and hand over to your team whenever a human is needed.'),
            ('🇦🇪', 'Local first', 'Arabic and English, GCC customers, UAE business culture, built in from day one.'),
            ('📈', 'Results you can see', 'Every lead, booking and result visible in your dashboard.'),
            ('🔒', 'Your data stays yours', 'Used only to run your agent. Never sold.')]), 'sec-lav')}),
        ('cta', {'h2': 'Let\'s talk about your business.', 'lead': 'Book a free 30-minute call. We will show you where AI can save your business time and win you more customers.'}),
    ],
}
