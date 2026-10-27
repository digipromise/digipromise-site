# Homepage (new). URL stays /home-v2/ until launch; switch to '/' in Phase 3 go-live.
import build_home_v2 as H
PAGE = {'url': '/', 'motion': True, 'noindex': True,
        'title': 'AI Agents & AI Employees for Businesses | DigiPromise',
        'description': 'DigiPromise builds and runs AI agents that answer, qualify and book every lead on your website, WhatsApp and phone in seconds, in Arabic and English, 24/7.',
        'crumbs': [('Home', '/')], 'faqs': H.faqs, 'sections': [('html', {'html': H.main})]}
