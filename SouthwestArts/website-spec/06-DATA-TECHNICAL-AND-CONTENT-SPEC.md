# Data, technical architecture and editorial operations

**Proposed production implementation specification, October 19, 2026. The separate repository contains the design prototype. Production awaits prototype review.**

**Hosting decision and constraint:** The selected source repository is [Suede0619/sw-arts-website](https://github.com/Suede0619/sw-arts-website) for both prototype and final production. GitHub hosting is the requested direction. The design preview uses [GitHub Pages](https://suede0619.github.io/sw-arts-website/), with only simulated assistance/checkout. Do not publish to Sites. **GitHub Pages prohibits running an ecommerce business or a site primarily facilitating commercial transactions.** The final selling website therefore needs a compatible host deployed from this same GitHub repository. Its selection remains open until production review. Static Pages also cannot execute server operations. A separate payment API alone does not resolve its ecommerce restriction. [Official GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits), [static hosting definition](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

## Initial catalog size and quality

Use a custom responsive site with server-rendered public pages, a structured editorial system, and a transactional database. Evaluate directory templates against object records, art presentation, contextual help and seller operations. Use custom components where a template cannot meet those needs.

Proposed production foundation: **Next.js with TypeScript**, **Sanity** for edited profiles/stories/permissions workflow, and **PostgreSQL through Supabase** for canonical inventory, holds, orders, consent and operational records. Use a managed image service such as Cloudinary for licensed masters and responsive derivatives, Stripe Connect/Checkout for approved payments, the selected model API for concierge assistance, a transactional email provider, and a licensed map/routing provider. Final services, hosting region, account ownership and costs are implementation decisions after prototype approval. These proposed vendor roles need evaluation and dependency installation. [Next.js documentation](https://nextjs.org/docs), [Sanity documentation](https://www.sanity.io/docs), [Supabase documentation](https://supabase.com/docs), [Cloudinary image delivery](https://cloudinary.com/documentation/image_transformations).

Keep public editorial content separate from private orders and conversations. Define one owner for every field: the CMS owns approved biography and presentation. The inventory database owns sellable quantity, price and hold state. Editorial previews may reference an inventory ID but cannot overwrite a paid order's terms. Use current supported releases and review service costs before a build commitment.

For sixty works, indexed database queries and a modest semantic index are sufficient initially. Do not buy a complicated search stack before query quality or scale justifies it. Ordinary price, dimension, medium and availability filtering must keep working if the AI provider is unavailable.

## Canonical records

| Entity | Essential fields and relationships |
|---|---|
| Region / place | Stable ID. Editorial region. Actual locality/jurisdiction. Public coordinates. Timezone. Source. Public-access status. A region tag does not change sovereignty or jurisdiction. |
| Artist | Approved display name/pronunciation. Verified identity. Self-described affiliations where supplied. Biography and evidence links. Taos relationship. Website/social references. Portrait rights. Seller/representation relationships. Publication consent. |
| Seller | Legal/display identity, artist/gallery/estate/reseller role, authorized work IDs, private agreements, settlement account reference, support/fulfillment responsibilities. Never expose banking data. |
| Work | Artist ID. Exact title. Art year or unknown. Medium. Unique/original-print/edition/reproduction classification. Edition number/size/proofs if known. Dimensions and unit/order/basis. Framed/unframed dimensions. Condition and provenance where applicable. Image IDs. Source/check date. |
| Offer / inventory | Work and seller IDs. Currency and exact minor-unit price or explicit inquiry. Tax category. Source availability versus confirmed availability. Quantity. Shipping origin. Approved delivery routes. Hold policy. Seller confirmation. Publication/checkout eligibility. |
| Asset / rights | File/master reference. Source URL. Depicted object. Creator/photographer. Copyright holder. License scope/territory/channel/term. Credit. Approval evidence. Dimensions/profile. Alt text. Expiry/withdrawal status. |
| Gallery / exhibition | Approved business profile. Real venues. Representation versus available resale artists. Dated shows. Work IDs. Appointment policy. Practical access. Paid-service status kept separate from editorial ranking. |
| Experience | Operator. Cultural/land authority where relevant. Meeting point. Duration. Age/exertion/access facts. Season. Time windows. Price basis. Cancellation/weather rules. Approved booking/referral route. Review evidence/date. |
| Restaurant | Cuisine, actual location, service periods, reservation route, dated menu/source, payment methods, fees, practical dietary/access information and partner agreement status. |
| Lodging / room type | Property, room type/capacity, amenities/limitations, access details, dated rate source, booking route. Live quotes also include stay dates, guests, currency, taxes, fees, cancellation and expiry. |
| Plan / inquiry | User-selected work/place IDs, preferences, dates, unresolved items, sharing/retention choice, communication consent and human owner. |
| Order / settlement | Immutable agreed line items, seller, taxes/delivery, currency, hold, verified payment events, fulfillment, refund/dispute, artist payout and reconciliation records. |
| Commercial relationship | Editorial eligibility, signed service scope, billing term, approved affiliate link/contract, disclosure, attribution basis and reporting. Payment never changes historical facts. |

Dimensions need typed values as well as the original source string. Store height, width and depth only after confirming the dimension order. Convert inches/centimeters for display without replacing the supplied measurements. Do not infer an unknown unit or turn framed dimensions into artwork dimensions. A drawing edition, a handmade print edition and a reproduction are distinct product types.

Artwork year, exhibition date, website upload date, source retrieval date and seller confirmation date are separate. An uploaded 2026 image of a 1998 work is not a new 2026 painting. Unknown prices are null. `$0` placeholders never create a free listing.

## Search and content behavior

Define a documented filter schema shared by controls, URLs and concierge tools. Normalize artist/title spelling for search while preserving the correct displayed names. Size queries must state whether they apply to image, framed or overall dimensions. Budget queries exclude unknown-price works unless the visitor requests inquiry listings. Allow users to include/exclude reproductions explicitly.

Use a measured palette descriptor or editor-approved color tags with a confidence label. It is an approximate discovery aid. Semantic tags describe visible subject/process or approved text. They must not invent cultural identity, authenticity or artist intent. A custom color palette must not modify the documentary artwork image.

Empty results show the actual constraint conflict, let the visitor remove a chip, and offer useful nearby choices with permission. The site cannot silently raise a budget or change originals to reproductions. Group inquiry-only records separately in price sorts.

Public pages provide descriptive URLs, titles, canonical links, crawlable content, breadcrumbs and a sitemap. Structured data must match the visible record: accurate product/offer availability, business/location information and dated events. Do not emit fabricated aggregate ratings, prices or offers for inquiry-only work. Prevent private plans and account/order pages from search indexing.

## Media production specification

For each cleared work, request a straight-on full image, detail views, signature or edition evidence, frame and edge views, and an optional installation image. Request a color-managed master, ideally at least 4,000 pixels on the long side where the work and rights permit. Record profile and photographer credit. Keep originals private. Review the intended use before accepting an image below the preferred resolution.

Make sRGB web derivatives with suitable format negotiation and fallbacks, several responsive widths, explicit dimensions, and on-demand high-resolution zoom. Proposed delivery budgets: ordinary card image budget of 60–150 KB, primary detail/hero image budget of 200–450 KB at their intended display size. Tune by visible quality, screen density and measured performance. Do not sacrifice fine artwork detail to a rigid compression target.

Present the whole artwork on a neutral background. Crop portraits and place photography only with an approved focal point. Never crop a work to fit a fashionable card ratio. Distinguish an installation photograph from a scale simulation. No generative enhancement, recoloring, invented detail, removed signature or synthetic room marketed as a real room. A wall preview must use licensed art at known dimensions and identify itself as a visualization. It cannot promise calibrated screen color.

Each restaurant/property/experience requests a compact professional image set: accurate exterior/location, meaningful interior/activity, relevant room/product detail and an access/arrival view where useful. A permission to use a business's photograph must cover the actual photograph's rights. Owner approval alone may not cover an independent photographer's license.

## Editorial workflow and freshness

Discovered then identity/source checked then facts reconciled then rights and seller authority recorded then partner/artist review then editorial approval then published then reconfirmation then archive/withdrawal. Imports create drafts. No scraped page can directly create a payable offer.

| Record | Proposed check cadence | Automatic behavior when stale |
|---|---|---|
| Unique-work availability | At least weekly. Immediately before a hold/payment. Feed updates as available | Remove Buy when stock confirmation expires. Allow a truthful availability inquiry. |
| Price, shipping, condition, seller authority | On change and before payable quote. Signed authority reviewed on expiry | Disable checkout when required facts or authority are missing. |
| Exhibition | Dated import plus editor check. Automatic start/end logic | Move ended shows to archive. Never leave them in “now.” |
| Hours, menus, access and booking URLs | Monthly and before a concierge-confirmed visit. Closures checked promptly | Display last checked and use provider confirmation when uncertain. |
| Lodging rates | Only for a dated quote within its actual expiry | Remove the quote after expiry. Preserve general room facts. |
| Image/license | Before publication and on expiry/withdrawal | Unpublish affected image and regenerate pages/cache. Retain required private audit evidence. |
| Public review snapshots | Research evidence only. Production uses permitted current display/feed | Do not present this research's cached counts as a live rating widget. |

Editors need preview, required-field validation, field-level sources, review notes, publication scheduling, change history and quick withdrawal. Proposed roles: contributor, editor, curator, commerce operator and administrator. A partner can suggest updates only to their own records. Apply separate access restrictions to payout data. A second reviewer approves seller/bank changes and material refunds.

## Reliability and privacy that support the experience

Use server-side secrets, scoped permissions, private storage, authenticated admin access, input validation, rate limits, signed webhooks and audited order changes. Validate server-side prices. Never trust a browser or model price. Maintain atomic holds, idempotent payment actions, reconciliation, tested backups and a recovery procedure. A degraded AI state still leaves search, contact and buying guidance usable.

Guest browsing should work without an account. Saved anonymous plans can live locally. Cloud saving and marketing are separate opt-ins. Collect only information needed to answer or fulfill the request. Proposed defaults: unfinished anonymous room photos deleted after seven days. Anonymous chat records after thirty days unless the user saves a consultation. Financial records follow the operator's actual retention requirements. Confirm vendor settings and retention before launch. Do not put conversation text, room photos, buyer names or order details into public analytics.

Analytics events use canonical IDs and consented attribution: `work_view`, `filter_applied`, `shortlist_add`, `inquiry_submitted`, `viewing_confirmed`, `quote_issued`, `payment_verified`, `delivered`, `artist_paid`, and eligible booking/payout events. Deduplicate webhooks and orders. Record clicks, completed sales, payouts and delivery as separate events, each with its own evidence.

## Implementation verification after authorization

Test concurrent purchase attempts, mid-session price and stock changes, expired holds, duplicate or out-of-order payment events, failed email and refunds. Also test wrong seller routing, image withdrawal, empty searches, assistant failures, inaccessible dialogs and slow phone connections. Verify public/private access separation and restore a backup. The specification stage created no application or test suite.
