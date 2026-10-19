# Data, technical architecture and editorial operations

**Proposed implementation specification · October 19, 2026. No implementation is authorized yet.**

## Build for a small, excellent catalog

Use a custom responsive site with server-rendered public pages, a structured editorial system, and a transactional database. A generic directory template would make the most important work—accurate object records, beautiful art presentation, contextual assistance and dependable selling—harder to control.

Proposed production foundation: **Next.js with TypeScript**, **Sanity** for edited profiles/stories/permissions workflow, and **PostgreSQL through Supabase** for canonical inventory, holds, orders, consent and operational records. Use a managed image service such as Cloudinary for licensed masters and responsive derivatives, Stripe Connect/Checkout for approved payments, the selected model API for concierge assistance, a transactional email provider, and a licensed map/routing provider. Final services, hosting region, account ownership and costs are implementation decisions after prototype approval. These are proposed roles, not installed dependencies or a completed vendor evaluation. [Next.js documentation](https://nextjs.org/docs), [Sanity documentation](https://www.sanity.io/docs), [Supabase documentation](https://supabase.com/docs), [Cloudinary image delivery](https://cloudinary.com/documentation/image_transformations).

Keep public editorial content separate from private orders and conversations. Define one owner for every field: the CMS owns approved biography and presentation; the inventory database owns sellable quantity, price and hold state. Editorial previews may reference an inventory ID but cannot overwrite a paid order's terms. Use current supported releases and review service costs before a build commitment.

For sixty works, indexed database queries and a modest semantic index are sufficient initially. Do not buy a complicated search stack before query quality or scale justifies it. Ordinary price, dimension, medium and availability filtering must keep working if the AI provider is unavailable.

## Canonical records

| Entity | Essential fields and relationships |
|---|---|
| Region / place | Stable ID; editorial region; actual locality/jurisdiction; public coordinates; timezone; source; public-access status. A region tag does not change sovereignty or jurisdiction. |
| Artist | Approved display name/pronunciation; verified identity; self-described affiliations where supplied; biography and evidence links; Taos relationship; website/social references; portrait rights; seller/representation relationships; publication consent. |
| Seller | Legal/display identity, artist/gallery/estate/reseller role, authorized work IDs, private agreements, settlement account reference, support/fulfillment responsibilities. Never expose banking data. |
| Work | Artist ID; exact title; art year or unknown; medium; unique/original-print/edition/reproduction classification; edition number/size/proofs if known; dimensions and unit/order/basis; framed/unframed dimensions; condition and provenance where applicable; image IDs; source/check date. |
| Offer / inventory | Work and seller IDs; currency and exact minor-unit price or explicit inquiry; tax category; source availability versus confirmed availability; quantity; shipping origin; approved delivery routes; hold policy; seller confirmation; publication/checkout eligibility. |
| Asset / rights | File/master reference; source URL; depicted object; creator/photographer; copyright holder; license scope/territory/channel/term; credit; approval evidence; dimensions/profile; alt text; expiry/withdrawal status. |
| Gallery / exhibition | Approved business profile; real venues; representation versus available resale artists; dated shows; work IDs; appointment policy; practical access; paid-service status kept separate from editorial ranking. |
| Experience | Operator; cultural/land authority where relevant; meeting point; duration; age/exertion/access facts; season; time windows; price basis; cancellation/weather rules; approved booking/referral route; review evidence/date. |
| Restaurant | Cuisine, actual location, service periods, reservation route, dated menu/source, payment methods, fees, practical dietary/access information and partner agreement status. |
| Lodging / room type | Property, room type/capacity, amenities/limitations, access details, dated rate source, booking route. Live quotes also include stay dates, guests, currency, taxes, fees, cancellation and expiry. |
| Plan / inquiry | User-selected work/place IDs, preferences, dates, unresolved items, sharing/retention choice, communication consent and human owner. |
| Order / settlement | Immutable agreed line items, seller, taxes/delivery, currency, hold, verified payment events, fulfillment, refund/dispute, artist payout and reconciliation records. |
| Commercial relationship | Editorial eligibility, signed service scope, billing term, approved affiliate link/contract, disclosure, attribution basis and reporting. Payment never changes historical facts. |

Dimensions need typed values as well as the original source string. Store height/width/depth only when their order is known. Convert inches/centimeters for display without replacing the supplied measurements. Do not infer an unknown unit or turn framed dimensions into artwork dimensions. A drawing edition, a handmade print edition and a reproduction are distinct product types.

Artwork year, exhibition date, website upload date, source retrieval date and seller confirmation date are separate. An uploaded 2026 image of a 1998 work is not a new 2026 painting. Unknown prices are null; `$0` placeholders never create a free listing.

## Search and content behavior

Define a documented filter schema shared by controls, URLs and concierge tools. Normalize artist/title spelling for search while preserving the correct displayed names. Size queries must state whether they apply to image, framed or overall dimensions. Budget queries exclude unknown-price works unless the visitor requests inquiry listings. Allow users to include/exclude reproductions explicitly.

Use a measured palette descriptor or editor-approved color tags with a confidence label. It is an approximate discovery aid. Semantic tags describe visible subject/process or approved text; they must not invent cultural identity, authenticity or artist intent. A custom color palette must not modify the documentary artwork image.

Empty results show the actual constraint conflict, let the visitor remove a chip, and offer useful nearby choices with permission. The site cannot silently raise a budget or change originals to reproductions. Price sorts put inquiry-only records in a visibly separate group rather than pretending to know their order.

Public pages provide descriptive URLs, titles, canonical links, crawlable content, breadcrumbs and a sitemap. Structured data must match the visible record: accurate product/offer availability, business/location information and dated events. Do not emit fabricated aggregate ratings, prices or offers for inquiry-only work. Prevent private plans and account/order pages from search indexing.

## Media production specification

For each cleared work request: straight-on full image; detail views; signature/edition where appropriate; framing/edges; and an optional truthful installation view. Request a color-managed master, ideally at least 4,000 pixels on the long side where the work and rights permit. Record profile and photographer credit; keep originals private. A smaller image can be accepted only after reviewing its actual intended use.

Make sRGB web derivatives with suitable format negotiation and fallbacks, several responsive widths, explicit dimensions, and on-demand high-resolution zoom. Proposed delivery budgets: ordinary card images around 60–150 KB, primary detail/hero images around 200–450 KB at their intended display size; tune by visible quality, screen density and measured performance. Do not sacrifice fine artwork detail to a rigid compression target.

Present the whole artwork on a neutral background. Crop portraits and place photography only with an approved focal point; never crop a work to fit a fashionable card ratio. Distinguish an installation photograph from a scale simulation. No generative enhancement, recoloring, invented detail, removed signature or synthetic room marketed as a real room. If a wall preview is offered, use genuine licensed art, known dimensions, a clearly labeled visualization and no false claim of calibrated screen color.

Each restaurant/property/experience requests a compact professional image set: accurate exterior/location, meaningful interior/activity, relevant room/product detail and an access/arrival view where useful. A permission to use a business's photograph must cover the actual photograph's rights; owner approval alone may not cover an independent photographer's license.

## Editorial workflow and freshness

Discovered → identity/source checked → facts reconciled → rights and seller authority recorded → partner/artist review → editorial approval → published → reconfirmation → archive/withdrawal. Imports create drafts. No scraped page can directly create a payable offer.

| Record | Proposed check cadence | Automatic behavior when stale |
|---|---|---|
| Unique-work availability | At least weekly; immediately before a hold/payment; feed updates as available | Remove Buy when confirmation is expired; allow a truthful availability inquiry. |
| Price, shipping, condition, seller authority | On change and before payable quote; signed authority reviewed on expiry | Disable checkout when required facts or authority are missing. |
| Exhibition | Dated import plus editor check; automatic start/end logic | Move ended shows to archive; never leave them in “now.” |
| Hours, menus, access and booking URLs | Monthly and before a concierge-confirmed visit; closures checked promptly | Display last checked and use provider confirmation when uncertain. |
| Lodging rates | Only for a dated quote within its actual expiry | Remove the quote after expiry; preserve general room facts. |
| Image/license | Before publication and on expiry/withdrawal | Unpublish affected image and regenerate pages/cache; retain required private audit evidence. |
| Public review snapshots | Research evidence only; production uses permitted current display/feed | Do not present this research's cached counts as a live rating widget. |

Editors need preview, required-field validation, field-level sources, review notes, publication scheduling, change history and quick withdrawal. Proposed roles: contributor, editor, curator, commerce operator and administrator. A partner can suggest updates only to their own records; payout data is restricted separately. A second reviewer approves seller/bank changes and material refunds.

## Reliability and privacy that support the experience

Use server-side secrets, scoped permissions, private storage, authenticated admin access, input validation, rate limits, signed webhooks and audited order changes. Validate server-side prices; never trust a browser or model price. Maintain atomic holds, idempotent payment actions, reconciliation, tested backups and a recovery procedure. A degraded AI state still leaves search, contact and buying guidance usable.

Guest browsing should work without an account. Saved anonymous plans can live locally; cloud saving and marketing are separate opt-ins. Collect only information needed to answer or fulfill the request. Proposed defaults: unfinished anonymous room photos deleted after seven days; anonymous chat records after thirty days unless the user saves a consultation; financial records follow the operator's actual retention requirements. Confirm vendor settings and retention before launch. Do not put conversation text, room photos, buyer names or order details into public analytics.

Analytics events use canonical IDs and consented attribution: `work_view`, `filter_applied`, `shortlist_add`, `inquiry_submitted`, `viewing_confirmed`, `quote_issued`, `payment_verified`, `delivered`, `artist_paid`, and eligible booking/payout events. Deduplicate webhooks and orders. A button click is not a sale, and a bank payout is not automatically evidence that a work was delivered.

## Implementation verification after authorization

Test meaningful failure cases: concurrent attempts to buy one unique work; price/status changes during a visit; expired holds; duplicate and out-of-order payment events; failed email; refunds; incorrect routing/seller; image withdrawal; empty searches; assistant tool failures; inaccessible dialogs; and a slow phone connection. Verify public/private access separation and restore a backup. No test suite or application has been built during this specification stage.
