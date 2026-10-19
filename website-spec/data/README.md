# Website research data

**Snapshot: October 19, 2026. Research and recruitment material, not a live catalog.**

| File | Records | Meaning |
|---|---:|---|
| [artist-cohort.csv](artist-cohort.csv) | 10 | Proposed artists, original selection rationale, context source and sourcing limits. |
| [artwork-candidates.csv](artwork-candidates.csv) | 60 | Six work candidates per artist, factual metadata, published price where available, observed source status, seller and image references. |
| [place-candidates.csv](place-candidates.csv) | 38 | Twelve gallery, ten experience, eight restaurant and eight lodging targets, with practical source/price limitations. |
| [image-source-manifest.csv](image-source-manifest.csv) | 98 | One research-reference row per work/place; 92 contain an image URL and six have no retrieved usable reference. |

These are UTF-8 CSVs readable in a spreadsheet. Source strings preserve published title/dimension details; original editorial briefs are our short research summaries. External URLs may expire or change.

## Work fields and availability

`artwork_year` is blank when unknown; upload/exhibition dates are not substituted. `dimensions_as_published` retains source order, while `dimension_unit` is blank if not established. `dimension_basis` identifies image/overall/framed where known or the need to confirm. Future canonical records require normalized dimensions and exact order/basis before hard size filters or scale visualization.

`price_usd` is a public asking price, not an accepted sale or full delivered cost. **Blank is unknown, never zero.** The six Miguel product-page `$0` values are excluded as placeholders. Edition/reproduction variants are separate from sold original paintings. `source_availability` describes the publisher's page/API, not a confirmation from an authorized seller to Southwest Art.

| Source status | Interpretation |
|---|---|
| `publisher_available` | Own site says available; still needs current seller confirmation and our permission. |
| `publisher_in_stock_1` | Gallery product page showed one in stock. |
| `shop_variant_available_true` | Specific nonzero-priced public shop variant reports available; not a different sold original. |
| `publisher_priced_not_marked_sold` | A priced print record was not marked sold in retrieved data. |
| `current_works_catalog` | Appears in the artist's Current Works collection; stock/date/unit still need confirmation. |
| `inquiry_listing` | Published work/inquiry context, not proof of present sale availability. |
| `publisher_priced_inquiry` | Seller publishes an asking price and invites inquiry; stock/title/proceeds still need confirmation. |
| `by_request_source_conflict` | Index and product information conflict; no sale assertion or checkout. |

All sixty records have `rights_status=not_cleared`, `seller_authority=not_obtained` and `checkout_eligible=false`. `DEMO-…` product references are explicit placeholders, **not Stripe product/price IDs** and not permission to charge. No secrets, payment accounts, actual buyer data or seller banking information are stored here.

## Image references

No image files were downloaded into this public package. A source-image URL is a discovery reference, not a license, an approved master or an instruction to hotlink production images. Artwork associations should be checked against the exact title/version; a shared photo of two Thom Wheeler objects is explicitly identified in work notes. Larry Bell's installation reference may be thumbnail-sized and is not a sufficient master.

Place-image rows are **unverified page-image candidates**. The first relevant non-logo source image is only a lead; it may depict a collection object, another room or a generic scene. Verify its subject, room/work association, quality, creator and permission before use. Missing rows remain blank instead of using an invented image. All production use is disabled pending clearance.

The full future asset record includes rights holder, photographer, permitted channels/territory/term, evidence, credit, dimensions/color profile, approved derivatives and withdrawal/expiry. See [technical/content specification](../06-DATA-TECHNICAL-AND-CONTENT-SPEC.md).

## From research to publishable content

Use these tables to prepare a targeted permission/inventory request after authorization, then reconcile the responses. Do not import them as published live offers. Keep actual agreements, private contact material, buyer records and raw source snapshots in appropriately controlled storage, outside public Git. Refresh source facts before relying on them in a later session.
