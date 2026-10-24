# Venue participation, art sales and organizer economics

**October 24, 2026. Scenarios using untested assumptions.** All monetary inputs lack supporting evidence. The project has made no offer. The model prices no specific footprint or duration. The current direct-artist website policy remains zero Southwest Art commission. The project has no approved physical-fair commission or participation fee.

## Meaning of “proceeds”

Artwork sales are not automatically the organizer's money. A collector purchasing a $20,000 painting creates seller receivables and fulfillment obligations. That purchase does not create $20,000 of organizer revenue. Revenue must arise from separately authorized sponsorship, admissions, services or commissions.

| Possible basis for 10–20% | What it means | Principal issue |
|---|---|---|
| Completed artwork gross merchandise value (GMV) | Percentage of qualifying completed art transactions, before the seller receives its balance | Would require an explicitly funded charge, subsidy or separately agreed event commission. Keep protected artist balances out of owner payments |
| Organizer gross revenue | Percentage of defined event revenue, excluding seller pass-through and other exclusions | Owner may earn money while the event loses money. Sponsor/fee refunds and restricted funds need careful treatment |
| Defined distributable event profit | Percentage after specified costs, liabilities, tax provision and agreed reserves | Better aligns downside, but requires a transparent budget, related-party controls, a settlement process and agreed definitions |
| Approved incremental venue costs plus capped participation | Reimburse additional owner services against documented costs. Remaining eligible profit shared on agreed terms | Prevent double counting of services already included in the event budget. Cap/control exposure before commitment |

**Research recommendation:** explore waived base rent, a tightly specified service package and a capped share of distributable event profit. Compare that with a fixed capped venue-services charge. The proposed 10–20% range needs negotiation. The research establishes no market standard or agreement. An owner may prefer a minimum guarantee. Model its cash and cancellation effects before accepting the term.

## Reproducible sensitivity cases

The [standalone inputs](data/model-inputs.json), [generator](tools/feasibility_model.py) and [full generated results](data/model-results.md) are separate from the existing Taos/platform model. These are examples that expose dependencies. They are **not a budget for occupying two towers**, evidence of demand or production quotes.

| Assumption / result | Limited demand | Demand case to validate | Stretch demand |
|---|---:|---:|---:|
| Unique visitors | 2,000 | 8,000 | 12,000 |
| Qualified collector households | 250 | 600 | 1,280 |
| Assumed household purchase conversion | 20% | 25% | 25% |
| Completed buyers, assuming one order each | 50 | 150 | 320 |
| Average completed order | $10,000 | $20,000 | $25,000 |
| **Completed art GMV** | **$500,000** | **$3,000,000** | **$8,000,000** |
| Sponsorship | $150,000 | $600,000 | $1,050,000 |
| Ticket revenue | $21,000 | $140,000 | $288,000 |
| Optional gallery-service revenue | $50,000 | $120,000 | $250,000 |
| Other earned event revenue | $20,000 | $50,000 | $120,000 |
| **Organizer revenue, excluding art GMV** | **$241,000** | **$910,000** | **$1,708,000** |
| Total cost including $70,000 paid feasibility | $400,000 | $750,000 | $1,250,000 |
| **Surplus before venue share, tax and further reserves** | **−$159,000** | **$160,000** | **$458,000** |

Paid-ticket assumptions are respectively 35% at $30, 50% at $35 and 60% at $40. Optional gallery-service assumptions are 20 × $2,500, 30 × $4,000 and 50 × $5,000. Validate the paid-service offer and agree participation terms before including the income. They are not approved charges or a change to free core artist listings. The model counts cash sponsorship. Record in-kind support separately. Other program and service income remains untested. The model assumes no alcohol profit or fundraising donations. Support each assumption with evidence or remove it.

The model cost categories include paid feasibility, later delivery labor, artist commissions/content, production/fit-out, art logistics/security, building operations, marketing/collector acquisition, professional/permit costs and contingency. Their sum is not a qualified estimate of building compliance work. The contingency placeholders are especially weak protection for an uninspected conversion site. The 20% overrun stress below illustrates exposure. The project has no quotes for tax, financing, unusual remediation or international imports.

## How much would the owner make?

Using only the $3m art-GMV / $910,000 organizer-revenue / $160,000 pre-owner-surplus illustration:

| Owner share basis | 10% owner amount | 15% owner amount | 20% owner amount |
|---|---:|---:|---:|
| $3m completed artwork GMV | $300,000 | $450,000 | $600,000 |
| $910,000 organizer revenue | $91,000 | $136,500 | $182,000 |
| $160,000 positive operating surplus **before tax/reserves** | $16,000 | $24,000 | $32,000 |

The last line is an upper-bound arithmetic comparison. Actual distributable profit would be lower after applicable liabilities, tax provision and retained cash. **Do not present $16,000–$32,000 as a promised owner payout.**

At 15% of art GMV, the $450,000 owner payment would turn the example's $160,000 surplus into a **$290,000 deficit** unless another party separately funds the difference. At 15% of organizer revenue, only **$23,500** remains before tax/reserves. Show organizer revenue and costs separately from artwork sales.

Even a hypothetical 20% physical-fair art commission would generate only $600,000 from $3m GMV: a 10–20% GMV owner share would absorb 50–100% of that commission before event costs. The main model excludes that commission. The project has no authority to charge it. Any direct-artist charge needs an explicit agreement before it can fund building costs.

## What makes a $3m art-sales claim defensible?

The model tests **150 completed purchasing households × $20,000**. Buyer research must establish whether those assumptions are achievable. That requires all of the following evidence:

1. A consented, deduplicated collector pipeline, with realistic budget bands, geography, interests and a reason to travel. A mailing-list name is not a qualified household. Private identities stay outside public Git.
2. Galleries/artists willing to commit appropriate work, asking prices, price bands, insurance values, provenance and seller authority. Asking prices are not achieved sale prices.
3. After outreach authority, confirm appointment and travel intentions through buyer conversations. Give little weight to VIP interest without dates or budget.
4. A reliable transaction/fulfillment path: seller of record, title, tax treatment, representation agreements, accepted payment, fraud checks, shipping/installation, cancellation and seller settlement. Avoid multiple channels counting the same order twice.
5. A defined sales-recognition window. Report event-period completed sales and later attributed completed sales separately. Exclude unpaid reserves, refundable deposits, canceled purchases, tax and shipping.

Inventory asking value, nonbinding “pipeline,” auction estimates and economic impact are separate measures. No public benchmark establishes that the current team can produce 600 qualified collector households or a 25% conversion rate at $20,000. Those are the largest demand assumptions to test.

## Profit does not solve preopening cash

The model pays 85% of costs before opening. By then it collects 60% of sponsorship, 70% of gallery-service income, 30% of tickets and 30% of other revenue. In the middle case:

| Preopening cash item | Illustration |
|---|---:|
| Costs paid before opening | $637,500 |
| Gross cash collected before opening | $501,000 |
| Timing gap | $136,500 |
| Hold all advance ticket cash against refunds | $42,000 |
| Additional operating cash reserve | $50,000 |
| **Model external cash need** | **$228,500** |

This timing test uses assumed receipts. Actual contracts must support a cash-flow forecast. Sponsor and gallery refund obligations could increase reserves. Actual draw schedules may differ. Prepayments may be unearned or restricted. Artist/gallery sale balances, tax collections and restricted grants are not a bridge loan to the organizer. A $70,000 feasibility underwriter would not by itself finance event delivery.

## Downside matters more than the largest headline

| Change to middle illustration | Surplus before venue share, tax/reserves |
|---|---:|
| No change | $160,000 |
| Sponsorship 25% below assumption | $10,000 |
| Costs 20% above assumption | $10,000 |
| Both changes | **−$140,000** |
| Paid ticket revenue 40% below assumption | $104,000 |

The event is primarily sponsor-dependent in this illustration. With zero organizer art commission, artwork sales cannot cover a production deficit. Seller proceeds stay separate. A later model must add dated cash movements, cancel/resize gates, refund exposure, building-specific quotes and committed financing.

## Terms the later negotiation must settle

- Legal owner/licensee and exact property/floors/concourse. Preparation, public access, teardown and restoration periods. Existing tenants and construction interfaces.
- Owner contribution: waived base rent versus actual operating services, deposits, staff, utilities, security, cleaning, fit-out and cash activation support. “Free space” alone does not define this package.
- Share basis and exclusions: seller pass-through, sales tax, refunds, chargebacks, shipping reimbursements, charitable/restricted funds, refundable deposits and in-kind sponsorship. Recognize net organizer service income consistently.
- Approved costs, including paid founder work at disclosed rates. Related-party approval. Budget change control. Caps. Independent finance review. Owner cost reimbursement must not appear twice.
- Settlement order: return third-party balances and satisfy obligations. Provide applicable tax/claims/refund reserves. Honor agreed financing recoupment. Then calculate the defined eligible pool. Any owner/bonus split needs a written order of priority.
- Cancellation triggers, construction displacement, insurance, damage/restoration, stop-work authority, permitted uses, sponsor conflicts, data/media rights and later renewal. A fair must not delay the developer's construction program by assumption.

The owner should receive an honest downside case and a credible explanation of noncash benefits. Negotiate these benefits directly if they matter more to the owner than the likely first-year profit share.
