# DigiPromise AI Agents: System Development Spec

Version 1.0 · 7 Oct 2026 · Source: the live plans on digipromise.com (pricing + 7 agent pages)

This is the build brief for the DigiPromise system and client management project. It describes what the website already promises, so everything listed per plan must exist before that plan is sold. Build the shared core once, then each agent on top of it.

---

## 0. Ground rules

1. **The website is the contract.** Every line on a plan card is a feature to build and test. If a feature isn't ready, remove it from the site; don't sell around it.
2. **One shared core, 7 agent configs.** Don't build 7 separate systems. Agents differ in prompt, knowledge, tools and plan gating, not in the plumbing.
3. **Per-client config, not per-client workflows.** One client = one row of config (plan, channels, numbers, team, CRM, languages). Workflows read config at run time, using tags and config data because the n8n instance has no folders.
4. **Plan gating everywhere.** Every feature checks the client's plan before running (see section 3).
5. **Never edit production workflows directly.** Duplicate, test, then swap.
6. **Document every build** so a team member can run it without Malik.
7. **Accuracy.** No "unlimited" and no uptime SLA. Reply speed is "in seconds / under 5 seconds", never 1–2 seconds.

## 1. Existing stack (keep)

| Layer | Tool | Notes |
|---|---|---|
| Orchestration | n8n self-hosted at n8n.digipromise.com (Contabo VPS, Nginx, Certbot, Cloudflare DNS) | All agent logic and integrations |
| Database + vectors | Supabase (Postgres + pgvector) | Client config, conversations, leads, usage, knowledge chunks |
| LLM | Claude (primary); gpt-4o-mini for low-cost or simple nodes | Pick a model per node by cost and quality |
| Website chat | DigiPromise widget → engine.digipromise.com (live since 8 Oct 2026; old n8n.digipromise.com chat webhook retired) | Payload `{chatInput, sessionId, ref, page}` → `{output}`; origins limited to digipromise.com + www; 30 msgs/10 min, 2,000 chars; Digi reads prices from the engine DB, so keep it in sync with pricing-v2.json |
| WhatsApp | WhatsApp Business Cloud API (Meta) | Approved templates needed for outbound messages after 24 hours |
| Instagram / Messenger | Meta Graph API | App review / Tester role still to finish |
| Telegram | Telegram Bot API | One bot per client, or a shared bot with client routing |
| Voice (Stella, Lilia voice) | Voice AI provider + phone numbers | Choose a provider (see section 7) |
| CRM | HubSpot (own CRM); client CRMs: HubSpot, Zoho, others via webhook | |
| Sheets | Google Sheets | Default lead store on Starter |
| Email | Transactional email (alerts, monthly reports) | Use @digipromise.com sending domain once Google Workspace is live |
| Billing | Stripe (Nomod later) | Setup fee + monthly or annual |
| Monitoring | Master Error Alert workflow → Malik's Telegram | Extend to all agent workflows |
| Usage metering | "Client Usage Gate" sub-workflow + Supabase table | Extend to the rules in section 2.6 |

## 2. Shared core (build once, used by all agents)

### 2.1 Channel gateway
- One inbound entry per channel: website widget, WhatsApp, Instagram DM, Messenger, Telegram, phone (Stella).
- It normalises every message into a single format, `{client_id, agent_id, channel, contact_id, text/voice, media, ts}`, then sends it to the agent brain.
- Outbound replies go back through the same channel adapter.
- Channel availability by plan: website on all plans; WhatsApp, Instagram, Messenger and Telegram from Growth.

### 2.2 Agent brain
- An n8n AI Agent node with:
  - a system prompt built from the agent template plus the client config (name, tone, languages, rules)
  - a RAG tool (Supabase pgvector)
  - action tools per agent (booking, order lookup, and so on)
  - memory per contact
- Language: it detects the customer's language and replies in it, limited to the plan's language count (2 / 5 / 20 / 100+). English and Arabic are always included.
- Guardrails: it never invents prices, stock, availability or policies. If it doesn't know, it says so and offers a human handover.
- "Powered by DigiPromise" shows on every client widget.

### 2.3 Knowledge and sync
- **Starter:** trained on the client's website pages, with a manual refresh on request.
- **Growth and up:** website plus the client's own data (listings, catalog, menus and rooms, classes and services, fleet and rates).
- **Sync jobs:** monthly (Growth), weekly (Scale), daily (Enterprise). They pull from the client's website or a feed or API they provide (CRM feed, Shopify/WooCommerce API, XML or CSV).
- Store the chunks in pgvector with `client_id` and `source`, and log every sync run.

### 2.4 Lead and booking outputs
- **Lead alerts by WhatsApp and email:** 1 team member (Starter), 3 (Growth), 5 (Scale), unlimited (Enterprise).
- **Lead store:** Google Sheets on Starter; Sheets or the client's CRM (HubSpot, Zoho, Klaviyo for AURA, or any webhook) from Growth up.
- **CRM add-on (AED 369 one-time):** Starter clients only.
- **Human handover (Growth and up):** the agent pauses, notifies the team with the full chat, and the team replies from the dashboard or WhatsApp. The agent resumes after a timeout or when released.

### 2.5 Client dashboard
- **Growth:** full dashboard with conversations, leads, bookings and advanced analytics.
- **Scale:** adds downloadable reports and AI conversation insights (topics, objections, missed questions).
- **Enterprise:** custom dashboard and reports.
- **Starter:** no dashboard; alerts and Sheets only.
- **Monthly email report (Growth and up):** volumes, leads, bookings, top questions, usage against plan.

### 2.6 Usage metering (decided 7 Oct 2026)
- **Only AI replies count as messages.** Customer messages are free.
- **Monthly allowance:** 5,000 (Starter), 12,000 (Growth), 20,000 (Scale), custom (Enterprise).
- **Stella:** call minutes instead: 500 / 1,500 / 4,000 / custom. Extra minutes cost AED 1.20/min.
- Alert the client at 80% and 100% of their allowance.
- **Add-on:** extra 5,000 messages for AED 369/mo. Agree what happens at 100% with no add-on (soft cap plus upsell recommended).
- Log usage per client per day in Supabase.

### 2.7 Security and reliability
- **Spam protection and rate limiting** on every plan. It's not listed on the cards, but it must exist.
  - Per-contact message rate limit
  - Bot and junk detection
  - Block list
  - A cap on AI calls per client per hour
- **Identity check** before sharing private data. For example: order number plus email or phone (AURA), booking reference plus phone (Nova, Luna, Lara).
- **Privacy:** store only what's needed, encrypt keys, and use a per-client data separation key (`client_id` on every row).
- **Enterprise:** signed data agreement (DPA) on request.
- **Monitoring:** every workflow error goes to the Master Error Alert, and you get a daily health summary.

### 2.8 WhatsApp templates (Meta approval needed, fees per message)
| Template | Used by |
|---|---|
| Lead / booking alert to team member | All |
| Booking confirmation + reminder | Nova, Luna, Lara, IRIS (viewings), Stella |
| No-show reminder (day before / 2 h before) | Nova, Luna, Lara |
| Membership renewal reminder | Luna |
| Abandoned cart reminder | AURA |
| COD order confirmation | AURA |
| Document request (licence / passport) | Lara |
| Follow-up for silent leads (later) | IRIS first |

Keep the templates in a table with columns for language, status and approval date.

### 2.9 Client onboarding (target: setup starts within 24 hours of the kickoff call; go-live date agreed on the call)
1. Kickoff call (30 min): plan, channels, team members, CRM, languages, rules, FAQs.
2. Create the client config row and Stripe subscription.
3. Connect the channels. WhatsApp number + Meta verification is the long pole, usually several days.
4. Ingest the website and client data, then run the first sync.
5. Configure the prompt and tools, and set up the templates.
6. Run the test script (section 6). Get the client's sign-off and go live.
7. Day 7 and day 30 check-ins.

### 2.10 Billing and referrals
- **Setup fee** on monthly plans. On annual plans, the setup fee is waived on Starter and 50% off on other plans. Annual plans also get 15% off the plan price.
- **Combined Stella:** a client taking Stella inbound and outbound pays one setup fee, the higher one.
- **Affiliates:** the site stores `ref` (cookie, 90 days). Save `ref` on the lead and on the Stripe customer.
- **Commission:** 10% of the setup fee and 15% of monthly payments for 12 months. Hold for 30 days; minimum payout AED 500.
- **Webhooks to wire:**
  - Contact form: today it opens WhatsApp.
  - Affiliate apply form: `affiliate.apply_webhook` in pricing-v2.json, currently empty.

## 3. Plan matrix (shared across message agents)

| Capability | Starter | Growth | Scale | Enterprise |
|---|---|---|---|---|
| Website chat | ✓ | ✓ | ✓ | ✓ |
| WhatsApp, Instagram, Messenger, Telegram | ✗ | ✓ | ✓ | ✓ |
| Team alerts (WhatsApp + email) | 1 | 3 | 5 | Unlimited |
| Lead store | Sheets | Sheets or CRM | Sheets or CRM | Sheets or CRM |
| Trained on | Website | Website + client data (monthly sync) | Weekly sync | Daily sync |
| Languages | 2 (EN + AR) | 5 | 20 | 100+ |
| Human handover | ✗ | ✓ | ✓ | ✓ |
| Dashboard | ✗ | Full | + downloads + AI insights | Custom |
| Monthly email report | ✗ | ✓ | ✓ | ✓ |
| Agents per client | 1 | 1 | 3 | Custom number |
| Webhooks and API access | ✗ | ✗ | ✓ | ✓ |
| Multi-branch / multi-location | ✗ | ✗ | Nova, Luna, Lara | ✓ all |
| Custom integrations, DPA, account manager | ✗ | ✗ | ✗ | ✓ |
| Support | Email | Priority WhatsApp | Priority WhatsApp | Dedicated account manager |
| AI replies / month | 5,000 | 12,000 | 20,000 | Custom |

Store this matrix as data, for example a `plans` table, so workflows check entitlements rather than hard-coding them.

## 4. Per-agent specs

### 4.1 IRIS: real estate lead agent
- **Job:** reply to every buyer, tenant and investor enquiry in seconds, qualify on budget, area, timeline and purpose, book viewings, and send hot leads to agents.
- **Channels:** website (Starter); WhatsApp, Instagram, Messenger and Telegram (Growth and up). Bayut, Property Finder and Dubizzle enquiries are handled when they arrive on WhatsApp or the website. There's no direct portal connection.
- **Workflows to build:**
  1. Lead qualification flow, with lead score (hot / warm / cold) and summary card.
  2. Agent WhatsApp alert with the full chat and summary.
  3. Viewing booking into the agent's Google or Outlook calendar, with confirmation to the buyer and a reminder.
  4. Listing sync from the client's website or CRM feed (monthly / weekly / daily). Answer only from synced listings.
  5. Lead routing:
     - Scale: 3 IRIS agents (sales, leasing, off-plan).
     - Enterprise: route to the right branch or team.
  6. CRM push (HubSpot, Zoho, webhook).
  7. Later: automatic follow-up for silent leads, using a template. Add it to the site only when it's built.
- **Tests:**
  - An off-plan enquiry in Arabic gets qualified and booked, and the agent gets an alert within 1 minute.
  - IRIS never invents a price for a unit that isn't in the listings.

### 4.2 AURA: ecommerce sales and support
- **Job:** answer product questions, recommend products, send checkout links, track orders, recover carts, confirm COD orders.
- **Platforms:**
  - Shopify: Admin API scopes `read_orders`, `read_products`, `read_checkouts`, plus webhooks.
  - WooCommerce: REST API keys, plus the free "Advanced Shipment Tracking" and "Cart Abandonment Recovery" plugins.
  - Salla, Zid and Magento are custom (Enterprise).
- **Workflows to build:**
  1. Product Q&A and recommendations from catalog sync (stock, sizes, prices, delivery).
  2. Checkout link builder:
     - Shopify: cart permalink `/cart/VARIANT:QTY,...` plus `?discount=`.
     - WooCommerce: add-to-cart link, or a draft order with a pay link.
  3. "Where is my order?" (Growth and up): verify the order number plus email or phone, read fulfilment status and tracking link, then reply.
  4. Upsell and cross-sell rules (Growth and up), plus discount codes within the rules the client sets.
  5. Abandoned cart recovery (Growth and up). Trigger: Shopify checkout webhook, or the WooCommerce plugin webhook. Then:
     - wait about 1 hour
     - check that no order was placed
     - send a WhatsApp template with the checkout link
     - only with consent
  6. COD confirmation (Growth and up): on a new COD order, send a WhatsApp template with Confirm / Cancel, and write the status back to the order as a tag or note.
  7. Returns and exchange answers from the client's policy (all plans).
  8. Revenue tracking (Scale and up): tag AURA-generated checkouts (cart attribute or discount code), match them to paid orders, and show revenue on the dashboard.
  9. Live courier tracking (Enterprise): Aramex, DHL and others via the courier's API.
- **Tests:**
  - A wrong order number plus email returns no data.
  - A recovered cart is attributed to AURA.
  - A COD cancel updates the order.

### 4.3 Nova: hospitality (restaurants, cafés, hotels, holiday homes)
- **Job:** take table and room bookings, answer menu, room and amenity questions, cut no-shows.
- **Workflows to build:**
  1. Booking capture (date, time, party size, room type, name, phone) into Sheets or CRM (Starter: Sheets plus alert).
  2. Calendar confirmation (Growth and up): Google Calendar, or the client's booking or PMS system via webhook (custom at Enterprise).
  3. WhatsApp reminders: day before and same day, with Confirm / Cancel; cancellations free the slot and alert staff.
  4. Menu and room sync (monthly / weekly / daily).
  5. Scale:
     - Multi-location: the location is picked in the chat.
     - Staff routing: restaurant, rooms or events requests go to the right team.
     - 3 Nova agents.
- **Tests:**
  - It never confirms a booking without a slot rule or calendar check, or else it marks the booking "request, pending confirmation".
  - The reminder is sent and the cancel reply frees the slot.

### 4.4 Luna: health and fitness (clinics, gyms, studios, salons)
- **Job:** book appointments and classes, answer prices, services and timings, send reminders, nudge renewals.
- **Workflows to build:**
  1. Booking chat (Starter) into Sheets plus alert.
  2. Calendar booking (Growth and up): Google Calendar. Booking systems like Mindbody or clinic software are custom at Enterprise.
  3. No-show reminders (Growth and up).
  4. Membership renewal reminders (Growth and up), from an expiry date in Sheets or CRM, sent X days before.
  5. Class and service sync, multi-branch (Scale), and 3 Luna agents.
- **Compliance:** no medical advice and no diagnosis. Health questions go to staff handover. Minimise stored health data; DPA on request.
- **Tests:**
  - "Is this treatment safe for me?" goes to a human handover.
  - A renewal reminder fires on schedule.

### 4.5 Lara: car rental
- **Job:** answer rates, car types, deposit and document questions, take booking requests, collect documents.
- **Workflows to build:**
  1. Rate and fleet Q&A from fleet sync (no invented availability; "request" until staff confirm, unless connected to rental software).
  2. Booking request plus WhatsApp reminders (Growth and up).
  3. Document collection (Growth and up):
     - Request licence and passport photos on WhatsApp.
     - Store them securely in client-only storage with expiry.
     - Attach them to the booking.
  4. Multi-branch fleets (Scale), and 3 Lara agents (daily, monthly, chauffeur). Rental software integration is custom (Enterprise).
- **Tests:**
  - Documents are stored only in the client's space and deleted after the retention period.
  - Price answers match the synced rates.

### 4.6 Stella: AI calling agent (inbound plans + outbound plans)

**Inbound:**
- Concurrency and lines by plan:
  - Starter: 1 phone line, 2 calls at once.
  - Growth: 5 calls at once.
  - Scale: multiple lines, 10 calls at once.
  - Enterprise: custom number of lines.
- **Workflows to build:**
  1. Answer and qualify in a natural voice (Arabic and English), then send a call summary to the team by WhatsApp and email.
  2. Appointment booking into the calendar (Growth and up).
  3. Call recordings and transcripts (Growth and up).
  4. Live call transfer to a human (Growth and up).
  5. Call routing to the right team (Scale).
  6. Minute metering: 500 / 1,500 / 4,000 per month, then AED 1.20/min. Enterprise gets a volume-negotiated rate.

**Outbound:**
- Outbound 1: 50 calling hours, 2,500 contacts.
- Outbound 2: 150 hours, 7,500 contacts, plus CRM and webhook integration and priority dialling.
- Enterprise: 15,000+ contacts.
- **Workflows to build:**
  1. Campaign upload (CSV or CRM list) with consent and do-not-call check.
  2. Dialler with **up to 3 redial attempts per contact**, calling hours limited to local legal hours.
  3. Outcome tagging (interested, callback, not interested, wrong number) with CRM write-back.
  4. Monthly results report.

**Setup fee:** inbound plus outbound together pay one setup fee, the higher one.

**Tests:**
- Transfer works.
- The minute counter matches the provider's bill.
- No calls go outside allowed hours.

### 4.7 Lilia: personal assistant for business owners
- **Job:** an owner's assistant on WhatsApp that gives a daily briefing, sets reminders, triages the inbox and schedules meetings.
- **Plans:**
  - **Starter:** WhatsApp assistant, daily briefing, reminders, 1 inbox + 1 calendar, Arabic and English replies, approve-before-send by default, reads only what is connected.
  - **Growth:** email drafting and inbox triage, meeting scheduling, Telegram and voice notes (transcribe voice notes, reply), weekly summary every Sunday, full dashboard.
  - **Scale:** owner plus up to 4 assistants, shared tasks, connects to task tools (Notion, Asana, Trello), custom workflows.
  - **Enterprise:** executive teams, **private deployment** (dedicated server or instance for that client), custom team size, custom integrations.
- **Rules:**
  - Nothing is sent without approval unless the owner turns that off for a specific action.
  - OAuth scopes are as narrow as possible.
  - The owner gets a full audit log.
- No message allowance is shown on the site (decided). Still meter AI replies internally for cost control.
- **Demo:** the website's live demo currently uses sample answers. Connect it to an n8n chat webhook (`live_demo(..., webhook=...)` in content/lilia.py).
- **Tests:**
  - A draft is never sent without approval.
  - The Sunday summary is sent on time in the owner's timezone.

## 5. Data model (Supabase, minimum)

- `clients`: id, name, plan, billing (monthly/annual), currency, status, ref_code, created_at
- `agents`: id, client_id, product (iris…lilia), name, languages[], prompt_overrides, active
- `channels`: id, agent_id, type (web/whatsapp/ig/messenger/telegram/phone), credentials_ref, number/handle
- `team_members`: id, client_id, name, whatsapp, email, role, alert_on[]
- `contacts`: id, client_id, channel_ids, name, phone, email, language, consent_marketing
- `conversations` / `messages`: client_id, agent_id, contact_id, channel, role (user/ai/human), text, tokens, ts
- `leads`: client_id, contact_id, score, summary, fields jsonb, crm_id, status
- `bookings`: client_id, contact_id, type, start, end, location, status, reminder_state
- `orders_cache` (AURA): order_id, status, tracking_url, cod_state, aura_attributed
- `knowledge_chunks`: client_id, source, embedding vector, text, synced_at
- `sync_jobs`: client_id, source, frequency, last_run, result
- `usage_daily`: client_id, date, ai_replies, call_minutes
- `templates`: name, language, status, approved_at
- `plans`: plan entitlements as data (section 3)
- `referrals`: ref_code, client_id, setup_paid, monthly_paid[], commission_due, payout_status

## 6. Go-live test script (every client)

1. Each connected channel: send a message and get a correct reply in seconds.
2. Ask in Arabic and English. Replies match the language.
3. Ask something not in the knowledge. The agent admits it and offers handover (Growth and up).
4. Trigger a lead or booking. The alert reaches the right team member and the record lands in Sheets or CRM.
5. Product-specific tests (section 4).
6. Usage counter increments only on AI replies.
7. The error path: break one credential, check the Master Error Alert fires, then restore it.

## 7. Open decisions

1. **Refund policy (decided 7 Oct 2026):** no go-live guarantee. Setup fee non-refundable; monthly cancel any time (return within 6 months = no new setup); annual refund = paid − used months at monthly price − waived setup; refunds to the same account in 35–45 days. Billing must support these calculations.
2. **Voice provider for Stella:** choose on Arabic voice quality, cost per minute (needs to stay well under AED 1.20 retail) and concurrency.
3. **100% usage behaviour:** soft cap plus upsell, or hard stop.
4. **Meta Graph app review** for Instagram and Messenger: blocked at the Tester role, needs finishing before Growth plans are sold.
5. **HubSpot pipeline limit** (own CRM): upgrade, or add a stage to the existing pipeline.
6. **Lawyer review:** refund policy and affiliate terms.

## 8. Suggested build order

1. Shared core: channel gateway (web + WhatsApp), agent brain, config and plans tables, usage metering, alerts, Sheets, error monitoring.
2. IRIS (first sales focus), including calendar booking and agent alerts.
3. AURA (an existing client already uses it), including order tracking, checkout links, cart recovery, COD and revenue tracking.
4. Telegram, Instagram and Messenger adapters (needed for every Growth plan).
5. Dashboard v1 (Growth), plus monthly email report.
6. Nova, Luna, Lara: mostly config plus booking and reminder flows reused from the core.
7. Stella inbound, then outbound.
8. Lilia.
9. Scale and Enterprise extras: multi-agent, API and webhooks, downloads, AI insights, multi-branch.
