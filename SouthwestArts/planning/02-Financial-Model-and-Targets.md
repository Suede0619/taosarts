# Financial model, sales targets, and cash discipline

October 19, 2026. **All forward figures are assumptions.** The project has no approved prices, committed funding or promised artist payments. USD, nominal. The model covers November 1, 2026–October 31, 2027, in twelve calendar-month periods. The project has no supplied current budget or founder time commitment.

The model is executable: edit [model-inputs.json](../data/model-inputs.json), then run `python3 SouthwestArts/tools/financial_model.py` from the ART repository root. From `ART/SouthwestArts/`, use `python3 tools/financial_model.py`. Outputs are [scenario results](../data/model-results.md), [scenario CSV](../data/scenario-summary.csv), [cash flow](../data/base-cashflow.csv), and [sensitivity](../data/sensitivity.csv). The generator checks that the allocation of every sales dollar reconciles, timing shares total 100%, order cohorts reach the base target, and cash receipts/payments reconcile to annual figures. The script checks arithmetic. Demand and delivery costs still need validation.

**Scope correction:** this is the earlier commission-bearing festival/integrated illustration, retained for comparison. It is **not the current Southwest Art website budget, an approved festival fee schedule, or a consolidated forecast**. The [new website commerce proposal](../website-spec/05-COMMERCE-PRICING-AND-OPERATIONS.md) controls zero direct-artist commission and the current profile fees. Rebuild a reconciled operating budget before using either set of figures to commit funds.

## Three ledgers, three different questions

1. **Artwork value:** What art was actually bought, paid for, and fulfilled? Exclude tax, shipping, admissions, donations, refunds, and outstanding commission balances.
2. **Artist and gallery proceeds:** Which seller should receive the money, under which agreement, and when did payment occur?
3. **Operating income and costs:** What money belongs to the festival or guide to run its own services?

One invoice can affect all three ledgers. Count revenue once. For shared nonprofit and company services, keep entity accounts and eliminate inter-entity transfers from consolidated reporting. These scenarios model earlier combined operations. They provide no current consolidated forecast, nonprofit return or company statement.

## Sales ambition and the buyer arithmetic

| Scenario | Completed art value | Artist proceeds* | Gallery retained* | Project transaction income* | Total operating income | Operating costs | Surplus / deficit before unresolved tax |
|---|---:|---:|---:|---:|---:|---:|---:|
| Low | $1m | $660,000 | $230,000 | $110,000 | $207,000 | $265,000 | **−$58,000** |
| Base | $3m | $1,980,000 | $690,000 | $330,000 | $579,000 | $485,000 | **$94,000** |
| Stretch | $5m | $3,300,000 | $1,150,000 | $550,000 | $973,000 | $700,000 | **$273,000** |

*Proposed channel mix and terms. Artist proceeds are before artists' materials, studio, labor, and tax. They are not profit or evidence that anyone can afford a particular rent. The low case is deliberately shown as underfunded: either raise $58,000 additional support or reduce costs/commitments. Do not call it a sustainable fallback as written.

The base sales architecture is $2m festival-associated and $1m year-round. “Associated” needs a recorded referral or direct order and a defined attribution window. The same sale appears once. These allocations divide the $3m target. They add no separate sales value.

| Base order cohort | Orders | Average completed art value | Total |
|---|---:|---:|---:|
| First and modest purchases | 300 | $1,000 | $300,000 |
| Established individual purchases | 180 | $5,000 | $900,000 |
| Larger collector purchases | 60 | $20,000 | $1,200,000 |
| Delivered procurement / commission milestones | 10 | $60,000 | $600,000 |
| **Total** | **550** | **$5,455 weighted average** | **$3,000,000** |

A single order can contain several works. Do not confuse order count with artworks. A $60,000 signed commission is pipeline until the relevant paid, delivered milestone qualifies under the reporting definition. Report deposits and contract face value separately.

A provisional funnel is **2,000 opt-in prospect households then 800 qualified households then 440 purchasing households then 550 orders**. That requires 40% qualification, 55% purchase conversion, and 1.25 orders per purchasing household. These demanding assumptions are not yet supported by local data. Measure actual cohorts, repeat purchases, lead time, and price bands before hiring against this case.

An initial inventory planning heuristic is **$10m of distinct available work at list price** for $3m realized art value. A 30% value sell-through lacks supporting evidence. Do not fill the inventory target with unrealistic prices, duplicate gallery listings, unavailable historical work, or unbuilt commission concepts. Maintain a separate capacity-qualified commission pipeline.

## Earlier channel assumptions: not current website policy

| Channel | Share of art value | Artist share | Gallery retained | Festival/guide fee | Who settles with buyer? |
|---|---:|---:|---:|---:|---|
| Direct festival sale | 30% | 80% | 0% | 20% | Authorized direct seller |
| Referred gallery sale | 50% | 50% assumed underlying contract | 46% | 4% | Gallery |
| Commission / procurement project | 20% | 85% | 0% | 15% | Contracted project seller |

The gallery referral fee comes from the modeled gallery margin, **not an extra deduction from the artist**. Actual artist/gallery contracts differ. Replace the assumption with agreed terms. Disclose fees, identify the work they cover and check for stacking with another representative’s commission. The review draws no current commission rate from old artist calls.

Weighted allocations are 66% artist, 23% gallery, and 11% project fee. At $3m, they reconcile to $1.98m + $690,000 + $330,000. The model assumes the project processes the direct and commission half of sales at a 3% effective payment cost, or **1.5% of total art value**. Gallery payment costs are outside this operating budget. Change these assumptions for wires, chargebacks, refunds, international sales, or a different seller arrangement.

## Other operating income and the first-year ramp

| Source | Low | Base | Stretch | Basis and warning |
|---|---:|---:|---:|---|
| Transaction services | $110,000 | $330,000 | $550,000 | 11% weighted fee. Not guaranteed. |
| Commercial partner services | $12,000 | $24,000 | $48,000 | The model assumes six paid months on average. Billing does not start automatically at launch. |
| Sponsorship | $60,000 | $125,000 | $200,000 | All uncommitted. |
| Grants | $0 | $50,000 | $75,000 | All unawarded. Eligibility/restrictions required. |
| Patron support | $15,000 | $30,000 | $60,000 | No donor commitment assumed. |
| Optional paid programs | $10,000 | $20,000 | $40,000 | Main exhibition remains free in the proposed model. |
| **Operating income** | **$207,000** | **$579,000** | **$973,000** | Not total art sold. |

The earlier illustration’s partner income assumes 20 galleries at $150/month for six months ($18,000) and ten hospitality businesses at $100/month for six months ($6,000). The proposed fees buy service packages. Editorial selection remains independent of payment. Low assumes twenty $100/month partners for six months. Stretch assumes thirty gallery partners at $200/month and twenty hospitality partners at $100/month for six months. Retention, willingness to pay, and the service workload remain unproved. The website’s newer targets are 12 galleries, 8 restaurants and 8 lodging profiles at $150/$99/$199 monthly. They yield $4,184/month or $25,104 over six paid months under full uptake. Do not add that income to this illustration without removing overlap.

Base sponsorship could be one $40,000 lead supporter, three $15,000 partners, and eight $5,000 community supporters. These package prices remain proposals. The $50,000 grant assumption needs several eligible sources. **New Mexico Arts FY28 permits a $5,000 request.** Treat the remainder as a funding gap until identified and awarded. [Funding plan](07-Funding-and-Sponsorship-Plan.md).

## Cost envelope

| Cost, including proposed paid capacity | Low | Base | Stretch |
|---|---:|---:|---:|
| Director / business development | $40,000 | $70,000 | $90,000 |
| Festival producer | $30,000 | $60,000 | $85,000 |
| Collector concierge / sales | $30,000 | $55,000 | $85,000 |
| Product and content | $35,000 | $70,000 | $90,000 |
| Community and education | $15,000 | $30,000 | $50,000 |
| Marketing | $25,000 | $55,000 | $85,000 |
| Venues, security, insurance | $20,000 | $35,000 | $60,000 |
| Fulfillment coordination | $10,000 | $25,000 | $35,000 |
| Payment processing | $15,000 | $45,000 | $75,000 |
| Legal and accounting | $15,000 | $20,000 | $20,000 |
| Contingency | $30,000 | $20,000 | $25,000 |
| **Total** | **$265,000** | **$485,000** | **$700,000** |

These budgets need vendor quotes and defined work hours. Staff lines must cover agreed pay plus employment/contractor obligations. Quote and classify actual work. Product/content includes hosting and software. The venue, security and insurance allowance must cover permits and essential facilities. Increase it if quotes exceed the allowance. Community costs include paid artists, musicians where programmed, advisors, access, and materials. Large installations, major transport systems, and a remote mesa event are **not financed by these estimates**.

Quote and record buyer-paid shipping, framing and installation separately. They are not included in art GMV. If the project subsidizes them, add an expense. Taxes, employer costs beyond the envelopes, refund losses, borrowing costs, and exceptional insurance needs require review. Settle liabilities, restrictions and tax before distributing any surplus.

## Unit economics and break-even

In the base mix, $1 of art value yields 11¢ of fee income and costs 1.5¢ in processing, leaving **9.5¢ before staff, marketing, event costs, and other overhead**. At 550 orders, that is $600 fee income and $82 processing per order, rounding processing to whole dollars. Channels differ significantly.

With $440,000 non-processing costs and $249,000 other operating income, the simple annual break-even art value is **$2.01m**. Without the assumed $50,000 grants it is **$2.54m**. Both figures round to $10,000. This holds the mix, fees, other support, and cost envelope constant. The equation tests fixed financial assumptions. It supplies no demand forecast.

The $55,000 base marketing budget is $125 per modeled purchasing household, excluding sales staff and other acquisition costs. Begin with a provisional paid acquisition ceiling below $200 per purchasing household, but assess full channel contribution, repeat behavior, and labor. Do not spend against presumed lifetime value without repeat evidence.

## Cash can fail even when the year looks profitable

The [monthly cash flow](../data/base-cashflow.csv) assumes **$50,000 opening unrestricted financing**. It is not counted as operating income and has no identified committed source. Base cash bottoms at **$19,550** before the final sales-heavy period. **$30,450 opening financing** merely avoids a negative balance. It does not provide the required reserve.

| Base-cost sensitivity | Annual result | Lowest cash with $50,000 opening |
|---|---:|---:|
| Base | $94,000 | $19,550 |
| Art value 20% lower | $37,000 | **−$7,810** |
| No grants | $44,000 | $19,550 |
| Sponsors 50% lower | $31,500 | **−$39,825** |
| Combined downside | **−$75,500** | **−$67,185** |

The November 2026–October 2027 calendar retains the previous project-month weights in the model: 18% of art value in September and 52% in October, with six partner-revenue months May–October. This is not evidence of an actual festival schedule or billing launch. Rephase after confirming actual dates and receipt schedules. The timing model receives grant reimbursement by the final period and collects other income when it recognizes revenue. Delayed receipts, restrictions, invoices, returns, or festival dates outside the assumed period worsen cash. A positive annual result is not permission to spend early. Keep a rolling 13-week forecast, a minimum eight weeks of unavoidable operating costs before major event commitments, and a downside funding or scope-reduction plan.

**Keep artist money, gallery balances, tax collections, refunds and restricted funds out of working capital.** Finance must establish account and ledger controls. The first pilot has a proposed staged $15,000 ceiling. It does not authorize the full $485,000 base expenditure.

## Reporting and attribution rules

Every order needs a unique ID, work IDs, seller, channel, source, currency, gross art value, discounts, tax, shipping, commission, recipient shares, payment dates, delivery status, refund status, and artist payout date. Deduplicate referrals and galleries against the same work/order.

Report **direct**, **verified assisted**, and **influenced but unverified** sales separately. Only the first two belong in the stated attributable target, with their evidence and window disclosed. None is automatically incremental: ask the buyer and seller whether the purchase would have happened anyway, and label incremental impact as an estimate with its method. Do not count a scan, lead, deposit, pledge, proposal, or unsigned procurement brief as a completed sale.

Public reporting should show aggregate outcomes and suppression for identifying small groups. Private order-level evidence stays outside this public repository.
