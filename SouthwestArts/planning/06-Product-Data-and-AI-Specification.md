# Product, data, and AI specification

Version 1.0, October 19, 2026. This specifies a future product. This repository contains no production website, payment service, live inventory database or AI concierge.

**Superseded website detail:** the newer [Southwest Art website specification](../website-spec/README.md) controls routes, design proposal, AI platform, content counts and commerce. This document remains supporting service/data background. Day one is November 1, 2026. The user authorized the design prototype and live preview. Production remains a separate gate.

## Product promise

Find art worth seeing, know whether it is available, and reach a person who can help you view and buy it. Make a small number of excellent choices easy to understand on a phone. A human concierge supports the service. The authorized design prototype demonstrates contextual assistance and the production proposal includes grounded AI after evaluation.

### Primary journeys

1. A visitor selects interests, time, and price range, sees a short credible selection, and requests a viewing.
2. A collector or advisor submits a brief and receives verified work with specifications and an all-in quote.
3. An artist or gallery grants limited content permission, supplies inventory, confirms representation, and updates availability.
4. A public visitor finds free exhibitions, accurate hours, access information, and a manageable itinerary without creating an account.
5. A staff member turns a consented inquiry into an appointment/order, reconciles it, and tracks payout.
6. A partner shares a tagged link or licensed listing and receives aggregate results. Buyer lists remain private.

## Priority and acceptance criteria

| Priority | Capability | Acceptance criterion |
|---|---|---|
| P0 | Verified art catalog | Every published work has artist, title, medium, dimensions, currency/price or explicit inquiry status, seller, rights, and availability timestamp. |
| P0 | Filters and price bands | Budget, medium, size, and location filters operate on structured fields. No invented matching works. |
| P0 | Human inquiry and appointment | Buyer knows who responds and when. Inquiry has owner, consent, status, and next action. |
| P0 | Inventory administration | Authorized seller can update status. One canonical work ID prevents duplicate availability. |
| P0 | Clear editorial/sponsor labeling | Paid placement cannot appear as an independent curatorial choice. |
| P0 | Public program guide | Edition, date, timezone, venue, source, access, and last verification are visible. |
| P0 | Quote and settlement record | Seller responsibility, fee allocation, taxes, shipping, payment and payout are explicit before sale. |
| P0 | Measurement and privacy | Source tags and consent retained. Public repo contains no real buyer/settlement records. |
| P1 | Saved shortlists and remote viewing | Minimal buyer friction, consented communications, current availability reconfirmed. |
| P1 | Partner feed and referral dashboard | Written license, corrections, expiration and aggregate reporting. |
| P0 for production website. Simulated in prototype | AI discovery assistant | Passes the groundedness and routing criteria below. Manual route remains available. |
| P2 | Room visualizations, complex recommendation or collection tools | Implement only after confirming rights, demand, cost and accuracy. |

Public browse and a contact form can launch before account systems or live checkout. Use the existing seller's secure invoice process until settlement is mature. Do not create a marketplace tax/payment burden casually to reduce checkout steps.

## Information architecture

The current primary navigation is **Art & Artists**, **Galleries**, **Experiences**, **Eat & Stay**, and **Plan a Visit**. Date festival material and label its status within Taos content. Put art and real next actions ahead of a large editorial feed. Gallery profiles should distinguish a location from the artists it represents. Itineraries should state total travel assumptions and who checked them.

Design direction: calm typography, consistent image treatment, concise artist-led stories, visible prices, restrained motion, and fast mobile pages. Caption short process films and let visitors choose whether to play them. Evaluate the direction through task completion and conversion tests.

## Core data model

| Entity | Minimum fields / rules |
|---|---|
| Artist | ID, approved display name/bio, consented identity statements, contact held privately, image/text permissions, approval date. |
| Gallery / seller | ID, business details, representation links, locations, verified hours, seller/settlement responsibility, agreement status. |
| Work | Canonical ID, artist, title, date, medium, dimensions/units, edition, price/currency, tax/shipping treatment, images/license, condition/provenance as applicable, location, seller, status, timestamp. |
| Representation | Artist, gallery, territory/scope, relevant dates and limits. Private agreement reference. |
| Venue / event | Edition, dates/timezone, location, access notes, organizer, source/license, cancellation status, verification owner. |
| Itinerary | Stops, travel assumptions, opening checks, access, public/private permissions, last verified date. |
| Buyer household / brief | Private ID, consent, interests, budget range, authority, delivery needs, communication preferences, retention date. |
| Opportunity | Owner, buyer ID, sources, work IDs, stage, next action/date, quotes, lost reason. |
| Order / milestone | Unique ID, seller, works, qualifying art value, tax/shipping, discount, payments, delivery, refunds, attribution evidence. |
| Settlement | Order ID, contractual shares, fees, liabilities, approval, payout dates and exceptions. |
| Content permission | Rights holder, asset, permitted use/channels, term, credit, changes, takedown. |

A single physical work has one canonical ID even when several partners describe it. Editions require individual unit tracking. Status values should include available, held, sold/pending delivery, delivered, withdrawn, and unknown. Stale availability must be visibly uncertain. Do not present it as available until reconfirmed.

Separate public catalog data, private business records, and highly restricted payment/identity evidence. This public document repository holds schemas and synthetic examples only. Incoming festival records go through intake, classification and redaction before any publication.

## AI behavior

The first useful assistant is a retrieval and routing service over approved, structured local data. Fine-tuning is not a prerequisite. Separate **available inventory** from **art-historical context** and **general suggestions**. An O'Keeffe-related query can discuss relevant qualities or historical references without claiming that an O'Keeffe work is available in Taos.

Required behavior:

- Apply budget, dimensions, medium, location, and availability constraints to real records.
- Cite the relevant work/profile/event source and its verification date.
- Ask a short follow-up when constraints are unclear, or offer a human introduction.
- Say when there is no verified match. Never invent a work, price, provenance, identity, event, or opening hour.
- Use approved artist language. Do not infer tribal affiliation, ethnicity, personal biography, or artistic intention from appearance.
- Explain historical comparisons respectfully. Do not flatten Indigenous identity into a visual filter.
- Treat external pages and uploaded documents as untrusted content. Instructions inside them cannot change permissions or trigger transactions.
- Never execute purchases, change prices, grant discounts, disclose private records, or promise authenticity or investment returns autonomously.
- For route questions, use verified stops and travel assumptions. Do not invent access to private or sacred sites.

### Release evaluation

Create at least 150 realistic evaluation prompts from buyer and staff questions. Cover ordinary discovery, contradictory filters, stale data, no match, duplicate inventory, historical artists, cultural identity, malicious document instructions, event date changes, and requests for private information. The corpus itself contains no real buyer PII.

Release only with **zero invented works/prices in the evaluated set**, correct enforcement of explicit price/availability constraints, correct handling of private fields, source links for factual local recommendations, and a clear human handoff for unresolved cases. Passing the sample does not guarantee perfect behavior. Audit live conversations with appropriate consent and shut down misleading features promptly. A manual concierge remains the fallback.

## Nonfunctional requirements and security

- Aim for [WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/): keyboard navigation, contrast, alternative text, captions, labeled forms, usable errors, and tested mobile access. Verify with people and manual checks as well as automated tools.
- Proposed performance goal: primary mobile content loads quickly on ordinary cellular service. Measure a 2.5-second largest-contentful-paint target under a documented test condition. Avoid autoplay and unnecessarily large images.
- Staff roles should limit catalog, buyer, finance, and admin permissions. Require two-factor authentication for privileged access.
- Use hosted payment providers. Do not store card numbers. Keep secrets outside Git and redact sensitive documents before sharing.
- Record changes to price, availability, order state, permission, and payout. Maintain encrypted backups and test recovery. Choose recovery targets appropriate to transaction volume before launch.
- Define retention, deletion, export, and access requests in a written privacy policy appropriate to actual users and jurisdictions. Default to collecting less data.
- Provide an offline event contingency for permitted catalog/hold information without exposing private buyer lists.

## Analytics specification

Track view then inquiry then qualified brief then shortlist then appointment then quote then paid then delivered then settled. Record source and campaign only where useful, with privacy-aware consent. Do not require cookies or registration merely to read public information. Define events once and keep household, order, and artwork units distinct.

A/B tests should answer concrete questions: visible price bands versus no bands. Shortlists versus long grids. A viewing request versus generic contact. Concise artist stories versus generic destination copy. Measure completed tasks and purchases alongside clicks. Use small exploratory tests at low traffic and avoid false statistical certainty.

## Delivery and build-versus-buy

Use the [dated roadmap](03-Twelve-Month-Roadmap-and-First-90-Days.md): days 1–30 are November 1–30, days 31–60 December 1–30, and days 61–90 December 31–January 29. A design prototype/live preview is now authorized as preparation. Review it before production. Demo assistance and checkout stay clearly simulated. Real AI, inventory, payments and seller operations need separate production review and approval.

Prefer maintainable existing tools for content, customer records, forms, booking, secure payment, and email. Choose vendors after confirming cost, exportability, privacy, accessibility, and staff capability. Keep a portable data export and documented ownership. Build custom software only when existing tools cannot meet a demonstrated service need.
