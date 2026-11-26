# ArtSouthwest: website specification

The [artist invitation and intake scope](12-ARTIST-INVITATION-AND-INTAKE.md) defines the MVP1 campaign, two conversion steps, callback path, image checks and database-to-catalog workflow.

The [MVP release roadmap](11-MVP-RELEASE-ROADMAP.md) sets the current feature order from the two-city catalog and day planner through editorial, visit planning, service, commerce and regional expansion.

The [November 21 findings](../research/07-Calendar-Editorial-and-Artist-Intake-2026-11-21.md) add an exhibition calendar, a short weekly roundup and group-friendly studio visit details for review. The [MVP1 scope](10-MVP1-WEBSITE-SCOPE.md) sets the sequence.

**Current stage:** The [Taos and Santa Fe catalog](https://artsouthwest.com/) is live. The [artist form](https://artist.artsouthwest.com/?campaign=taos-artists) and staff review use Neon. Follow the [handoff](../SESSION_STATE.md) for launch status. Project day one is November 1, 2026.

The website's purpose is to sell art so artists can keep living and working in Taos. **October 23 strategic alignment:** the year-round platform is the proposed core business, with festivals supporting discovery, relationships and visits. Contemporary and a full range of art belong. Southwest describes geography. Start onboarding with the [current strategy and brand brief](../planning/10-Platform-First-Strategy-and-Brand-Brief.md). The proposed service combines an exceptional art catalog, thoughtful human/AI assistance, dependable buying and delivery, and a curated reason to visit. **MVP1 covers Taos and Santa Fe in the catalog.** The first itinerary review uses central Taos. The [MVP1 website scope](10-MVP1-WEBSITE-SCOPE.md) sets the current counts and work packages. The table below records the October recommendations.

**Main documents:** [website specification](01-WEBSITE-SPEC.md) and [design direction](03-DESIGN-DIRECTION-FOR-APPROVAL.md). The separate [sw-arts-website repository](https://github.com/Suede0619/sw-arts-website) contains the prototype. [SESSION_STATE.md](../SESSION_STATE.md) records [GitHub Pages preview](https://suede0619.github.io/sw-arts-website/) deployment checks. Live AI, real payments and booking integrations are not connected. The sequence is specification then your review then authorized design prototype then your review then authorized production build.

GitHub is the source and prototype-hosting choice. The user excludes Sites hosting. The eventual commercial production site keeps its source in the same repository. Choose compatible hosting before live selling. GitHub Pages prohibits ecommerce business hosting. See [technical architecture](06-DATA-TECHNICAL-AND-CONTENT-SPEC.md).

## The recommendations to review

| Topic | Proposed decision |
|---|---|
| Design | Atomic **Audo Copenhagen #11**, adapted with warm ivory, clay/juniper, excellent whole-artwork imagery and accessible type. **Pending your choice.** Aesop #35 is the alternative. |
| Organizing principle | Region-first, Taos-only launch. Thirteen future destination clusters proposed separately. |
| Artist offer | The October model assumed zero commission. The [current artist intake](12-ARTIST-INVITATION-AND-INTAKE.md) sets 20% on completed artwork sales through the platform. |
| AI | One contextual ArtSouthwest concierge across every section. Recommend OpenAI Responses API with `gpt-6.1-sol`, subject to a grounded task evaluation. |
| Experiences | Free editorial inclusion. Earn only on eligible completed bookings through an approved affiliate/direct-referral agreement. |
| Paid services | Founding proposals: gallery **$150/mo**, restaurant **$99/mo**, lodging **$199/mo**. Disclose paid profiles and preserve independent curation. |
| Content | Ten artist candidates/six work records each, ten experiences, twelve gallery targets, eight restaurants and eight lodging properties. The research identifies candidates. The project has no partner agreements or ready-to-sell stock. |

The project adopted **ArtSouthwest** on November 23, 2026. Use that spelling across the catalog, artist intake and campaign materials.

## Document guide

| Document | Review purpose |
|---|---|
| [01. Website specification](01-WEBSITE-SPEC.md) | Purpose, audiences, navigation, each section's UX, buying paths, service, metrics and approval gates. |
| [02. Regions and Taos scope](02-REGIONS-AND-TAOS-SCOPE.md) | Logical future Southwest destination clusters and the actual Taos launch boundary. |
| [03. Design direction](03-DESIGN-DIRECTION-FOR-APPROVAL.md) | Actual Atomic choices, recommended adaptation, type/color/layout/image standards. Approval pending. |
| [04. AI concierge and platform](04-AI-CONCIERGE-AND-PLATFORM.md) | Section modes, provider comparison, grounded tools, costs, human handoff and evaluation. |
| [05. Commerce, pricing and operations](05-COMMERCE-PRICING-AND-OPERATIONS.md) | Stripe demonstration and production requirements, artist payouts, delivery, booking attribution and funding gap. |
| [06. Data, technology and content](06-DATA-TECHNICAL-AND-CONTENT-SPEC.md) | Proposed stack, canonical records, imagery, editorial workflow, freshness and reliable operations. |
| [07. Prototype and review plan](07-PROTOTYPE-AND-REVIEW-PLAN.md) | What the later prototype should show and how we will judge it before a production decision. |
| [08. Collector growth and launch](08-COLLECTOR-GROWTH-AND-LAUNCH.md) | Legitimacy, remote collecting, visit service, acquisition experiments and practical launch capacity. |
| [09. Database-driven arts sitemap](09-DATABASE-DRIVEN-ARTS-SITEMAP.md) | Proposed connected catalog, browse filters, artist/gallery/work pages, tours, visit planning, and permission-aware publishing. |
| [Artists and sixty work candidates](research/01-TAOS-ARTISTS-AND-WORKS.md) | Six sourced records per proposed artist, asking prices where available, sizes, media and explicit gaps. |
| [Ten experiences](research/02-TAOS-EXPERIENCES.md) | Practical costs, duration, access, review snapshots, travel assumptions and booking routes. |
| [Twelve galleries](research/03-TAOS-GALLERIES.md) | Curatorial/recruitment rationale, programs, object examples, dated shows and source corrections. |
| [Eight restaurants and eight lodging targets](research/04-TAOS-FOOD-AND-LODGING.md) | Menus, price examples, room categories, rate limitations and practical service details. |
| [Source register and remaining inputs](research/05-SOURCES-AND-VERIFICATION.md) | Evidence quality, exclusions, source access limits and what still needs seller/provider confirmation. |
| [Data and image-reference index](data/README.md) | Downloadable research tables and instructions for interpreting them. |

## What the research establishes

The sixty work records have **31 published asking prices** and **60 image-reference URLs**. Every row remains disabled for checkout. None has our seller authority or cleared image rights. Six Miguel Martinez pages have price/availability conflicts. Several other artists publish no prices or creation years, and some listed works are editions, reproductions or possible resale. The evidence does **not** establish sixty simultaneously available newest/highest-priced direct-artist works. The artist research explains the exact limits and the next verification step.

The place table contains **38 targets: 12 galleries, 10 experiences, 8 restaurants and 8 lodging properties**. The image manifest has 98 artwork/place rows, 92 with source-image references. Place-image association still needs review. The production asset set contains no third-party image files, copied full menus or biographies.

Brochure ranges retain their publication status. Obtain date-specific quotes separately. The research flags ended exhibitions, sold art, seasonal restaurants and the Ojo cold plunge’s construction status. The user experience must remain elegant while being truthful about these facts.

## Decisions for the specification review

1. Choose the Atomic base and approve or edit the proposed visual adaptation.
2. Confirm navigation, Taos scope and the proposed artist/place shortlist.
3. Confirm the originals/original-prints/reproductions mix and direct versus gallery seller routes.
4. Decide how to fund literal full-art-price artist payout, processing and the continuing service.
5. Review partner pricing, experience referral model and actual staff capacity.
6. Approve the prototype scope and identify the imagery we may use.

The design recommendation awaits review. The prototype stage is now authorized. Production implementation waits for the user's later prototype review and authorization. Future sessions must read [AGENTS.md](AGENTS.md) before continuing.
