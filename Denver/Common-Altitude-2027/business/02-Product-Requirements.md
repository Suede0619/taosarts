# Product requirements: event, art market and service system

**Working PRD v0.1, October 24, 2026.** Product includes the physical fair and digital/service layer. This document grants no authority to deploy software, enroll participants, transact or book. Read the [business plan](01-Business-Plan.md), [brand book](../brand/02-Brand-Book.md) and [project inputs](../data/project.json).

## Outcomes and users

Primary outcome: useful completed art purchases and paid creative work. Supporting outcomes: public discovery, informed collecting, reliable appointments/fulfillment, controlled host benefit and viable unrestricted cash.

The product serves collectors, advisers, first buyers, residents, artists, galleries, educators, families, sponsors and property teams. Operating users include the producer, crew, registrar, finance and customer-support staff. Each needs accurate information and a human escalation path.

## Essential journeys

1. **Public visitor:** understand what/when/status then find free art and optional paid experiences then get travel/access/sensory information then arrive/check in where required then choose a manageable route then ask a person then leave feedback without forced data capture.
2. **Collector:** discover work/seller then see accurate image, scale, medium, price/availability then request appointment or quote then receive informed human response then buy from the verified seller then receive condition/title/receipt and delivery support then confirm fulfillment.
3. **Artist/gallery:** accept clear terms then supply authorized records/assets then confirm installation/availability then handle appointments/offers then record completed orders once then reconcile obligations and outcomes.
4. **Program attendee:** understand price/access/age/sensory needs then choose available session then pay/reserve under clear terms then receive confirmation/reminders then attend or obtain policy-compliant refund/support.
5. **Operator:** review actual site/rights/funding then accept work/program then publish approved facts then operate with capacity controls then handle incidents then reconcile and report.

## Must-have acceptance requirements

| ID | Requirement | Acceptance evidence | Accountable function |
|---|---|---|---|
| PR-01 | Single truthful status for dates/site/participants | Public pages, decks, confirmations and staff scripts match approved record. Proposed facts labeled | Program |
| PR-02 | Free core discovery clearly distinguished from paid programs | Representative visitors can identify a free route and optional price before registration | Brand / visitor |
| PR-03 | Search/browse works without chat | Conventional filters let users find work by artist, seller, medium, size, price band and availability. Display relevant access information alongside results | Product |
| PR-04 | Accurate artwork record | Unique ID, rights, artist/title/year, medium/dimensions, seller, price/currency/tax/shipping basis, availability check date, image credit and inquiry route | Registrar |
| PR-05 | Seller authority and terms | Validated seller/representation, agreed sale/hold/refund/fulfillment responsibility before publication as available | Art market / legal |
| PR-06 | Reliable appointment flow | Request/confirmed/waitlist/canceled states. Named human owner. Time zone and access needs handled privately | Collector |
| PR-07 | Clear full-cost purchase path | Seller invoice/payment route and shipping/installation quote. No simulated checkout on a real work | Finance / seller |
| PR-08 | Protected money and deduplicated orders | No seller balances in organizer runway. Stable order IDs. Deposits/refunds/tax/shipping separately recorded | Finance |
| PR-09 | Reservation/capacity control | Only approved capacity offered. Sold-out/waitlist/cancellation work. Staff can reconcile bookings | Producer / ticketing |
| PR-10 | Accessible digital experience | Target WCAG 2.2 AA. Keyboard, labels, contrast, text alternatives, zoom, errors and non-chat completion tested | Product / access |
| PR-11 | Accessible physical journey | Site-specific professional route review, toilets/rest/sensory/help information and emergency interfaces | Producer / access |
| PR-12 | Human customer care | Published service hours, escalation, response target and incident handoff. No unsupported 24/7 promise | Visitor / collector |
| PR-13 | Rights/credits remain attached | Assets cannot publish without owner/license/channel/term/credit record | Brand / registrar |
| PR-14 | Private controlled CRM | Consent, access controls, retention, correction and deletion process. No buyer/health/contact data in public Git | Product / privacy lead |
| PR-15 | Safe installation and operation | Required owner/code/engineering approvals, inspection and stop authority documented | Producer / specialists |
| PR-16 | Honest results | Entries vs unique estimates, completed sales vs pipeline and organizer vs seller money separately reported | Finance / program |
| PR-17 | Offline/recovery path | Printed/controlled work and appointment references, manual check-in and human assistance work during an outage | Product / visitor |
| PR-18 | Useful post-sale care | Delivery/condition/payment exceptions have responsible seller and escalation. Completion evidence retained | Registrar / seller |

The AA standard defines a design and testing target. The project makes no current conformance claim. Qualified specialists must assess physical access separately. [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [ADA framework](https://www.ada.gov/resources/title-iii-manual/)

## Recommended implementation approach

Use one structured catalogue, one private CRM, managed ticketing and seller-led invoices/payment links, with a trained human concierge. Start with portable CSV/schema and clear ownership. This limits custom engineering while protecting seller authority and allowing excellent service.

Select actual vendors through a short paid proof: access/privacy, data export, fees, support, refunds, accessibility, integrations, failure recovery and total cost. Do not create accounts, choose paid plans or claim integrations are live in this stage. The product/program fee includes only an agreed implementation scope. Complex software requires a separate quote.

**Seller payment baseline:** a verified seller issues its own invoice/payment link and receives its own funds. Organizer records a consented attribution/order reference and completion status. A future multi-seller checkout would require separate underwriting, legal/tax/refund design, seller onboarding and engineering. Stripe’s direct-charge documentation explains a possible implementation. The project has no approved or implemented marketplace. [Stripe reference](https://docs.stripe.com/connect/direct-charges)

**Hosting/source:** the existing Southwest Art prototype remains in its separate GitHub repository. This package includes no deployed event website. A future commercial site needs an approved commercial-compatible host and source/release process. Do not use GitHub Pages as the operating ecommerce business.

## Data model

Core objects: EventVersion, SiteZone, AccessCondition, PersonConsent, Organization, Engagement, Artwork, AssetLicense, AvailabilityCheck, Appointment, SellerOrderReference, Session, Reservation, SponsorBenefit, Incident, VendorCommitment, CashRestriction, Decision and OutcomeAggregate.

Artwork availability states: research only then rights/authority pending then accepted then seller-confirmed available then on hold then sold pending completion then completed / canceled / returned. Display the relevant state honestly. Recording a catalogue item does not create consignment or ownership.

Engagement states: research candidate then authorized approach then interested then scope/terms pending then contracted then funded/ready then delivered then reconciled. Publish partner status only after the organization gives explicit permission.

Incident and access-request information may be sensitive. Store the minimum necessary under restricted access, with professional retention rules. Do not put diagnostic/health details or buyer identities in source-controlled public files.

## Optional innovation backlog

| Feature | Potential value | Entry condition |
|---|---|---|
| Source-grounded art/event concierge | Answer questions and help filter approved catalogue/program facts | Human-reviewed corpus, evaluation, disclosure, citations, privacy and budget |
| Personalized itinerary | Manage time, interests, mobility/sensory preferences | Explicit consent, nonprofiling defaults and a useful manual alternative |
| Corporate acquisition briefs | Help appropriate buyers commission/acquire art | Seller authority, conflict disclosure, full costs and experienced human advice |
| Artist-approved interactive catalogue | Connect a spatial work to informed discovery | Clear rights, accessibility, measured benefit and maintenance owner |
| Remote viewing/appointment rooms | Extend the market beyond travel | Accurate images/scale, staffed appointments and fulfillment capability |

The AI layer is a later tested enhancement, never the only interface or an authority on authenticity, valuation, legal/tax matters or available inventory. It cannot invent answers, expose private collector data or autonomously buy/reserve/commit money. Choose provider/model only after a task-specific quality/privacy/cost evaluation. This document selects no new provider and makes no best-model claim.

## Quality and launch testing

Test actual user tasks with collectors, artists, first buyers, older users and disabled participants. Verify one complete enquiry-to-seller-payment-to-delivery example using authorized test fixtures before real launch. Rehearse cancellation/refund, sold work, duplicate order, missed appointment, unavailable room, denied permissions and outage.

Proposed service targets to validate: human response within one staffed business day before the fair. Live show support staffed during opening/program hours. Important inventory updates within the agreed seller/registrar cadence. These are targets until resourced. Avoid unsupported guaranteed uptime or instant authenticity promises.

Complete the must-have requirements before adding optional features. Each feature needs a scope, owner, acceptance evidence and a funded maintenance path. The venue, rights and cash gates still control the physical event.
