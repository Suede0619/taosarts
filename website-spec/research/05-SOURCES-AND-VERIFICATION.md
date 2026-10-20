# Sources, evidence and remaining verification

**Research performed for the October 19, 2026 specification.** This register explains the evidence behind the recommendations; the detailed research and CSV rows link directly to their sources. It does not certify all sources as current, licensed or independently audited.

## Evidence hierarchy

1. Artist, authorized seller, operator, museum, Pueblo or land-manager information for facts they control. Public inventory is still not our permission to sell.
2. Current official technical/platform documentation for documented capabilities and fees.
3. Named review/marketplace/destination sources for their own ratings/listings, explicitly identified and dated as retrieved snapshots.
4. Dave Paul/Felix meeting and user accounts, labeled as supplied rather than independently verified.
5. Our proposals, manual travel estimates, budgets, editorial selection and design judgments, explicitly separated from source facts.

Raw fetched pages and extraction scripts remain under ignored `ART/private/source/website-spec/`. They are not a public archive or a production content license. Public deliverables contain concise original summaries, factual metadata and source/image-reference URLs. No account access, social login or CAPTCHA restriction was bypassed. Some local HTTP fetches returned errors, incomplete JavaScript pages or access blocks; usable alternative primary sources were used where available.

## Foundational project sources

| Source | What it supports | Limit |
|---|---|---|
| [Consolidated Felix notes](../../FelixMeet) | Mission, selective guide, human referral network, collector/public balance, AI idea, House of Fire and HeyTaos correction | Meeting date and several conversational claims unresolved; no agreements or board authority implied. |
| [Existing business plan](../../planning/01-PRD-and-Business-Plan-2027.md) and [experiments](../../planning/08-Experiments-and-New-Ideas.md) | Earlier strategy, regional concept, collector service and artist outcome measures | Its festival commission assumptions do not override the newest zero website-commission instruction. |
| [HeyTaos](https://heytaos.com/) and [earlier partnership research](../../research/03-HeyTaos-and-Regional-Partnerships.md) | Potential complementary broad-discovery partner | No content/data/affiliate agreement or verified audience performance. |
| [Southwest Art Magazine](https://www.southwestart.com/) | Existing same-market use of the working name | Not a trademark search or conclusion about availability/rights. |

## Design, AI and transaction sources

| Primary source | Used for | Verification limit |
|---|---|---|
| [Atomic Atlas](http://atomic.nrvana.com/), public [data.js](http://atomic.nrvana.com/data.js) | Actual named/numbered reference systems, design tokens and navigation; Audo #11/Aesop #35 | Local retrieval encountered certificate verification problems. Atlas material is not an original-brand asset/font license or an accessibility certification. |
| [OpenAI model catalog](https://developers.openai.com/api/docs/models) | Current `gpt-6.1-sol`, Astra and Luna roles/pricing; initial model recommendation | Recheck model availability/prices at implementation; no comparative performance test conducted. |
| [Structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs), [data controls](https://developers.openai.com/api/docs/guides/your-data) | Schema/tool approach and provider storage/configuration questions | Schema compliance does not guarantee truthful answers; no zero-retention configuration assumed. |
| [Claude model overview](https://platform.claude.com/docs/en/models/overview) | Sonnet 5.5 as an evaluation candidate | Documentation, not a measured Southwest Art benchmark. |
| [Gemini model overview](https://ai.google.dev/gemini-api/docs/models), [function calling](https://ai.google.dev/gemini-api/docs/function-calling) | Gemini 3.8 Flash candidate and tool approach | Same task evaluation still required. |
| [Stripe charge types](https://docs.stripe.com/connect/charges), [direct-charge fee-payer behavior](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior) | Proposed Connect flow, configurable fee responsibility and different dispute/refund roles | Actual account configuration, entity model and signed seller duties must be checked before production. |
| [Stripe Connect pricing](https://stripe.com/connect/pricing) | Current pricing reference for later budgeting | The spec's 3% allowance is illustrative, not a fee quote. |
| [FareHarbor affiliate program](https://fareharbor.com/scale/distribution-network/affiliates/), [affiliate help](https://help.fareharbor.com/hc/en-us/articles/42957556694811-FareHarbor-Distribution-Network-FHDN-for-affiliates) | Published 15% eligible-experience affiliate offer and reporting/payout model | No selected Taos operator or Southwest Art account is assumed enrolled/approved. |
| [Viator partner resources](https://partnerresources.viator.com/) | Published 8% completed-booking commission and 30-day referral window | Acceptance, actual eligible products and attribution terms still apply. |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Core Web Vitals](https://web.dev/articles/vitals) | Accessibility/performance targets | No site exists or has been tested against them. |
| [Next.js](https://nextjs.org/docs), [Sanity](https://www.sanity.io/docs), [Supabase](https://supabase.com/docs), [Cloudinary](https://cloudinary.com/documentation/image_transformations) | Proposed framework/content/database/image service roles | No dependency, account, hosting plan or final price selected. |

## Artist source coverage

| Artist | Main work sources | Important correction or limitation |
|---|---|---|
| Larry Bell | [Artist](https://larrybell.com/), [Anthony Meier](https://www.anthonymeier.com/artists/larry-bell) | Artist site live local retrieval returned a database error; gallery object records are inquiry leads. Public commissions/installations are not automatically sale stock. |
| Ron Cooper | [Charlotte Jackson artist page](https://www.charlottejackson.com/artists/RonCooper.html), [dated 2026 show](https://www.charlottejackson.com/current-exhibition.html), [203 works](https://203fineart.com/artists/34-ron-cooper/works/) | Correct artist born 1943; similarly named photographer/painter websites were excluded. Museum holdings are context, not inventory. |
| Kevin Macpherson | [Own portfolio](https://www.kevinmacpherson.com/collections/20051) and six individual work URLs in CSV | Available versus sold/not-for-sale checked; only one selected public price; source units unclear in several records. |
| Walt Gonske | [Own site](https://waltgonske.com/index.html), [current price-sorted gallery category](https://chimayotrading.com/product-category/artists/walt-gonske/?orderby=price-desc) and individual product pages | Old newsletter availability conflicts resolved against current product state; selected six show one in stock. Highest at retrieved seller, not entire artist market. |
| Thom Wheeler | [Own site](https://www.thomwheeler.com/) and its public Current Works data response | Fetched the same public gallery data used by the page, without authentication. No seller approval, creation year or dimension unit established. |
| Miguel Martinez | [Correct own site](https://www.miguelmartinezfineart.com/) and six product URLs | By Request versus out-of-stock/$0 conflict; placeholder/template language excluded. Wrong same-name artist domain excluded. |
| Ed Sandoval | [Own available-original page](https://www.edsandovalgallery.com/original-artwork-available/) | Six larger works, not a provable high-price or newest ordering; prices/year/unit absent. |
| Angie Coleman | [Own gallery](https://www.angiecolemanfinearts.com/gallery.php) and retrieved pagination | Six nonzero records selected; sold-out/$0 items excluded, including Three Forks Conejos and Hay Bales and Clouds. |
| Jonathan Warm Day Coming | [Own shop](https://jwarmdaycomingart.com/) and public product/variant metadata | Specific available variants selected; generic theme text misleadingly includes Sold out; sold originals distinguished from offered prints. |
| Sherrie McGraw | [Hindes](https://hindes.com/artist/sherrie-mcgraw/), three ArtzLine work pages linked in CSV; [Taos context](https://davidleffel.com/bio/) | Six verifiable seller listings include older/possible resale work. Own teaching platform did not provide six current sale records; higher-priced marketplace lead could not be reliably retrieved and was excluded. |

No social account is treated as a source merely because a name matches. Limited public access means this is not a complete social-media scrape. Ask artists for current inventory and approved masters rather than claiming exhaustiveness.

## Local venue source limits

The [experience research](02-TAOS-EXPERIENCES.md) contains the authority/operator links and separate review snapshots. Tripadvisor scores/counts are cached evidence with varying ages, not live statistics or a licensed display feed. NM River Adventures has inconsistent rounded scores/counts across retrieved versions; the range is disclosed. Williams Lake's old Forest Service PDF establishes a route reference, not today's access. Travel bands are our manual estimates pending routing.

The [gallery research](03-TAOS-GALLERIES.md) links the twelve targets. Revolt's “current/upcoming” shows have past dates; Lake Object's visible exhibitions are historical; R.C. Gorman's Taos location is taken from its current own-site location list. Bryans and mismatched/recycled gallery domains were excluded. House of Fire details come from Dave Paul; the promised Felix archive is absent.

The [hospitality research](04-TAOS-FOOD-AND-LODGING.md) links menus and rooms. PDF facts were extracted for concise factual samples; no complete menus are reproduced. Some menu PDFs are undated; file dates are not a guarantee. Juliette is the Hotel Willa restaurant. Orlando's own linked domain was unhelpful, so no official current menu/price was asserted. 192's current operation is unresolved after an October 17 seasonal-close listing. Static inn rate ranges are not live booking quotes. Hacienda del Sol is the Taos property, not a same-name Tucson/Mexico hotel.

## Inputs needed for the next authorized stage

1. Dave Paul/Felix review of the implemented design prototype and an explicit final Atomic design choice. Prototype authorization is recorded; production review remains open.
2. Felix-approved artist/gallery cohort, actual seller relationships and current object sheets.
3. Artist/photographer permission and usable masters for the prototype; separate authority for live selling.
4. Confirmed partner willingness, actual current menus/rooms/prices/hours/access and allowed booking/referral paths.
5. A funded processing policy, a scoped prototype/build budget and named ongoing service capacity.
6. An operating entity/seller model and the separate relationship to Taos Fall Arts Festival.
7. Working-brand/public-name decision before public release.
8. Felix's future 2026 archive, handled privately; it may inform later strategy but its absence does not invalidate independent website specification work.

These are concrete next inputs, not a reason to repeat all research in a fresh session. Refresh date-sensitive facts and retain the original observation alongside meaningful corrections.
