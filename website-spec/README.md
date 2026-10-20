# Southwest Art — website specification

**Current authorization:** Dave Paul has requested the design prototype and live preview in a separate `sw-arts-website` repository. The provisional Audo #11 direction is for review; production and live transactions still require a later approval. Project day one is November 1, 2026. Earlier specification-stage descriptions below describe the review sequence, not a current prohibition on the authorized prototype.
**Prepared October 19, 2026 for Dave Paul and Felix Kay. Stage: design prototype and live preview authorized; production awaits prototype review.**

The website's purpose is to sell art so artists can keep living and working in Taos. The proposed service combines an exceptional art catalog, thoughtful human/AI assistance, dependable buying and delivery, and a curated reason to visit. **Taos is the only v1 region**, with Arroyo Seco visible in location choices and trip planning.

**Start with [the main website specification](01-WEBSITE-SPEC.md), then [the design direction for approval](03-DESIGN-DIRECTION-FOR-APPROVAL.md).** The design prototype is implemented in [sw-arts-website](https://github.com/Suede0619/sw-arts-website), with [GitHub Pages preview](https://suede0619.github.io/sw-arts-website/) deployment status recorded in [SESSION_STATE.md](../SESSION_STATE.md). Live AI, real payments and booking integrations are not connected. The sequence is specification → your review → authorized design prototype → your review → authorized production build.

Dave chose GitHub for source and prototype hosting, superseding the abandoned Sites attempt. The eventual commercial production site keeps its source in the same repository; GitHub Pages' ecommerce restriction means its host must be resolved before live selling. See [technical architecture](06-DATA-TECHNICAL-AND-CONTENT-SPEC.md).

## The recommendations to review

| Topic | Proposed decision |
|---|---|
| Design | Atomic **Audo Copenhagen #11**, adapted with warm ivory, clay/juniper, excellent whole-artwork imagery and accessible type. **Pending your choice.** Aesop #35 is the alternative. |
| Organizing principle | Region-first, Taos-only launch; thirteen future destination clusters proposed separately. |
| Artist offer | Free core listing and zero Southwest Art commission on direct-artist sales. Literal full-art-price payout requires platform/sponsor funding for processing costs. |
| AI | One contextual Southwest Art concierge across every section; recommend OpenAI Responses API with `gpt-6.1-sol`, subject to a grounded task evaluation. |
| Experiences | Free editorial inclusion; earn only on eligible completed bookings through an approved affiliate/direct-referral agreement. |
| Paid services | Founding proposals: gallery **$150/mo**, restaurant **$99/mo**, lodging **$199/mo**. Disclose paid profiles and preserve independent curation. |
| Content | Ten artist candidates/six work records each, ten experiences, twelve gallery targets, eight restaurants and eight lodging properties. These are researched candidates, not agreed partners or ready-to-sell stock. |

“Southwest Art” is the requested working name. An established [Southwest Art Magazine](https://www.southwestart.com/) already uses it in this market. Keep it for internal spec/prototype discussion; assess naming, domain availability and potential confusion before choosing the public identity. No name/domain/trademark clearance has been performed.

## Document guide

| Document | Review purpose |
|---|---|
| [01 — Website specification](01-WEBSITE-SPEC.md) | Purpose, audiences, navigation, each section's UX, buying paths, service, metrics and approval gates. |
| [02 — Regions and Taos scope](02-REGIONS-AND-TAOS-SCOPE.md) | Logical future Southwest destination clusters and the actual Taos launch boundary. |
| [03 — Design direction](03-DESIGN-DIRECTION-FOR-APPROVAL.md) | Actual Atomic choices, recommended adaptation, type/color/layout/image standards; approval pending. |
| [04 — AI concierge and platform](04-AI-CONCIERGE-AND-PLATFORM.md) | Section modes, provider comparison, grounded tools, costs, human handoff and evaluation. |
| [05 — Commerce, pricing and operations](05-COMMERCE-PRICING-AND-OPERATIONS.md) | Stripe placeholder/production boundary, artist payouts, delivery, booking attribution and funding gap. |
| [06 — Data, technology and content](06-DATA-TECHNICAL-AND-CONTENT-SPEC.md) | Proposed stack, canonical records, imagery, editorial workflow, freshness and reliable operations. |
| [07 — Prototype and review plan](07-PROTOTYPE-AND-REVIEW-PLAN.md) | What the later prototype should show and how we will judge it before a production decision. |
| [08 — Collector growth and launch](08-COLLECTOR-GROWTH-AND-LAUNCH.md) | Legitimacy, remote collecting, visit service, acquisition experiments and practical launch capacity. |
| [Artists and sixty work candidates](research/01-TAOS-ARTISTS-AND-WORKS.md) | Six sourced records per proposed artist, asking prices where available, sizes, media and explicit gaps. |
| [Ten experiences](research/02-TAOS-EXPERIENCES.md) | Practical costs, duration, access, review snapshots, travel assumptions and booking routes. |
| [Twelve galleries](research/03-TAOS-GALLERIES.md) | Curatorial/recruitment rationale, programs, object examples, dated shows and source corrections. |
| [Eight restaurants and eight lodging targets](research/04-TAOS-FOOD-AND-LODGING.md) | Menus, price examples, room categories, rate limitations and practical service details. |
| [Source register and remaining inputs](research/05-SOURCES-AND-VERIFICATION.md) | Evidence quality, exclusions, source access limits and what still needs seller/provider confirmation. |
| [Data and image-reference index](data/README.md) | Downloadable research tables and instructions for interpreting them. |

## What the research establishes

The sixty work records have **31 published asking prices** and **60 image-reference URLs**. Every row remains disabled for checkout; none has our seller authority or cleared image rights. Six Miguel Martinez pages have price/availability conflicts. Several other artists publish no prices or creation years, and some listed works are editions, reproductions or possible resale. The evidence does **not** establish sixty simultaneously available newest/highest-priced direct-artist works. The artist research explains the exact limits and the next verification step.

The place table contains **38 targets: 12 galleries, 10 experiences, 8 restaurants and 8 lodging properties**. The image manifest has 98 artwork/place rows, 92 with source-image references; place-image association still needs review. No third-party image files or copied full menus/biographies are included as production assets.

Published brochure room ranges are distinguished from live date-specific quotes. Ended exhibitions, sold art, seasonal restaurant operations and the Ojo cold plunge's construction status are handled explicitly. The user experience must remain elegant while being truthful about these facts.

## Decisions for the specification review

1. Choose the Atomic base and approve or edit the proposed visual adaptation.
2. Confirm navigation, Taos scope and the proposed artist/place shortlist.
3. Confirm the originals/original-prints/reproductions mix and direct versus gallery seller routes.
4. Decide how to fund literal full-art-price artist payout, processing and the continuing service.
5. Review partner pricing, experience referral model and actual staff capacity.
6. Approve the prototype scope and identify the imagery we may use.

The design choice has been submitted for review and remains pending. The prototype stage is now authorized. Production implementation waits for the user's later prototype review and authorization. Future sessions must read [AGENTS.md](AGENTS.md) before continuing.
