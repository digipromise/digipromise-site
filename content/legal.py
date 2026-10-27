# /refund-policy/ and /privacy-policy/ — DRAFTS, need your review (and ideally a lawyer) before launch
from build_parts import hero, section

DRAFT = '<p class="note">⚠️ Draft for review. Not legal advice. Please check with your lawyer before publishing.</p>'

REFUND = '''
<p><b>Last updated:</b> 7 October 2026</p>
<h2>1. Our promise</h2>
<p>If you are not satisfied, or simply change your mind, you can cancel at any time and we refund the remaining amount under the rules below. No lock-in, no arguments.</p>
<h2>2. Setup fee</h2>
<ul><li>Before we charge any setup fee, we agree with you exactly what you need and how we will deliver it. Because the work is planned and reserved for you from that point, the setup fee is not refundable.</li>
<li>If you take more than one plan for the same agent (for example Stella inbound and outbound), you pay one setup fee only, the higher one.</li></ul>
<h2>3. Delivery timeline</h2>
<p>Each AI agent is custom-built for your business. Our team contacts you within 24 hours of purchase and starts the build. Your go-live date depends on your requirements and integrations, and we confirm it with you on the kick-off call.</p>
<h2>4. Monthly plans</h2>
<ul><li>Cancel any time. Your plan stays active until the end of the month you have paid for and is not renewed. Part months are not refunded.</li>
<li>Come back within 6 months of cancelling and we will not charge the setup fee again for the same agent. A different agent or a much larger scope needs a new setup.</li>
<li>After 6 months, setup is charged as for a new client.</li></ul>
<h2>5. Annual plans</h2>
<p>You can cancel an annual plan at any time. We refund what you paid, minus:</p>
<ul><li>the months already used, charged at the normal monthly price (so the 15% annual discount no longer applies to them);</li>
<li><b>Starter:</b> the full setup fee that was waived when you joined;</li>
<li><b>Growth, Scale and Enterprise:</b> the 50% of the setup fee that was waived when you joined.</li></ul>
<p><b>Example (Starter):</b> you paid AED 25,500 for the year and cancel after 4 months. We deduct 4 × AED 2,500 = AED 10,000 plus the AED 5,000 setup fee, and refund AED 10,500.</p>
<h2>6. Not refundable</h2>
<p>One-time services such as CRM integration, add-ons already used, extra messages or call minutes already used, and any WhatsApp fees charged by Meta.</p>
<h2>7. How refunds are paid</h2>
<p>Refunds go back to the same payment account you paid from, within 35 to 45 days of your cancellation request.</p>
<h2>8. How to cancel</h2>
<p>Contact DigiPromise from your registered contact on WhatsApp at +971 58 545 6331 or by email at sales@digipromise.com.</p>'''

PRIVACY = '''
<p><b>Last updated:</b> 1 October 2026</p>
<p>DigiPromise ("we", "us") respects your privacy. This policy explains what information we collect, how we use it and your rights. It covers our website and the AI agents we run for our clients.</p>
<h2>1. Who we are</h2>
<p>DigiPromise is based in Dubai, United Arab Emirates.</p>
<h2>2. What we collect</h2>
<ul><li><b>From website visitors:</b> details you share in forms or chat (name, phone, email, business and message), plus basic analytics such as pages visited and device type.</li>
<li><b>From our clients:</b> account, billing and business information needed to build and run your agent.</li>
<li><b>From our clients' customers:</b> messages and details shared in conversations with an agent we run on a client's behalf.</li></ul>
<h2>3. How we use it</h2>
<ul><li>To reply to you and provide our services.</li><li>To build, train and improve the AI agent for the client it belongs to.</li><li>To bill clients and keep records.</li><li>To measure and improve our website.</li></ul>
<p>We do not sell personal information.</p>
<h2>4. Conversations handled for our clients</h2>
<p>When our AI agent talks to a client's customers, we process those conversations on behalf of that client. The client decides how that information is used, and our use is limited to running and improving that client's agent.</p>
<h2>5. Who we share it with</h2>
<p>Trusted service providers that help us run our services, such as hosting, messaging (for example WhatsApp by Meta), AI model providers, analytics and payments (for example Stripe). They only use the data to provide their service to us.</p>
<h2>6. How long we keep it</h2>
<p>We keep conversation logs for up to 12 months, unless the client asks us to delete them sooner. Billing records are kept for as long as UAE law requires. Website enquiries are kept for up to 24 months.</p>
<h2>7. Your rights</h2>
<p>You can ask us to access, correct, export or delete your personal information, in line with UAE data protection law (Federal Decree-Law No. 45 of 2021). Contact us at sales@digipromise.com.</p>
<h2>8. Cookies</h2>
<p>We use cookies and similar tools for analytics and to remember preferences such as your currency. If you arrive through a partner's referral link, we store that partner's code for up to 90 days so we can credit them; the code is attached to any enquiry you send us. You can control cookies in your browser settings.</p>
<h2>9. Changes</h2>
<p>We may update this policy. The latest version is always on this page.</p>
<h2>10. Contact</h2>
<p>DigiPromise, Dubai, UAE · sales@digipromise.com · +971 554 548 756</p>'''

def legal(url, name, h1, lead, body):
    return {'url': url, 'motion': True, 'noindex': True, 'title': name + ' | DigiPromise', 'description': lead,
            'crumbs': [('Home', '/'), (name, None)],
            'sections': [('html', {'html': hero([('Home', '/'), (name, None)], name, h1, lead, trust=False)}),
                         ('html', {'html': section('<div class="prose">' + body + '</div>')})]}

PAGES = [
    legal('/refund-policy/', 'Refund policy', 'Refund <span class="accent">policy.</span>', 'How cancellations, refunds and setup fees work for DigiPromise plans: cancel any time and get the remaining amount back.', REFUND),
    legal('/privacy-policy/', 'Privacy policy', 'Privacy <span class="accent">policy.</span>', 'How DigiPromise collects, uses and protects personal information on our website and in the AI agents we run.', PRIVACY),
]
