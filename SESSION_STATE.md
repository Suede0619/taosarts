# Session handoff — October 19, 2026

This is a dated snapshot for a new session. Check the current date, Git history, and user's latest direction before treating an action as current. Stable working rules are in [AGENTS.md](AGENTS.md).

## What the user asked for

Make ART a document repository connected to the user-created `Suede0619/taosarts` repository. Consolidate four versions of Felix meeting notes into one detailed account. Research Taos Fall Arts history and economics, international festival practices, and a complete executable year-ahead PRD/business plan aimed at millions in art sales, artist livelihood, and broad public access. Correct “TellUs” to HeyTaos and include the House of Fire business contact details.

## What is complete

The initial **31-file public package** was committed and pushed to `main` as **`f74b0471272081157f42128f748455e9732fcd24`**. A subsequent user request to add/commit/push found no further changes; a push confirmed it was up to date. The continuity update adds this handoff and `AGENTS.md` to ART, links them from README, and adds workspace guidance to the separate parent repository.

| Deliverable | Location |
|---|---|
| One comprehensive meeting summary | [FelixMeet](FelixMeet) |
| Historical scene, milestones, organizational financial table, missing attendance/sales evidence | [Taos history and economics](research/01-Taos-Fall-Arts-History-and-Economics.md) |
| Sixteen international/regional event models, financial/attendance distinctions and transferable practices | [Global comparisons](research/02-Global-Festival-Benchmarks.md) |
| HeyTaos offer, partner roles, proposed pilot and regional expansion | [Partnership research](research/03-HeyTaos-and-Regional-Partnerships.md) |
| Sources, excluded claims, evidence limits and open questions | [Source register](research/04-Source-Register-and-Open-Questions.md) |
| Detailed PRD/business plan and seven execution modules | [Business plan](planning/01-PRD-and-Business-Plan-2027.md), then README navigation |
| Historical CSVs, assumptions, cash flow and sensitivity | [Data index](data/README.md) |
| Reproducible standard-library model | [tools/financial_model.py](tools/financial_model.py) |
| Archive intake, partnership, buyer, seller and weekly reporting templates | [README working tools](README.md#working-tools) |

The plan covers **October 19, 2026–October 18, 2027**. Stuart already lives in **Arroyo Seco**. The 2026 festival has ended; a 2027 festival date is not confirmed. The separate regional brand and AI concierge remain proposals. No website, payment system, live inventory service, partnership, grant submission, booking, or outreach was created by this document work.

## Key findings and decisions to preserve

- The festival's own history uses **1974**. The official 2026 promotion gives **September 18–October 4**. Older/aggregator pages can conflict or mix editions; source each edition explicitly.
- Public research did **not** establish a dependable annual total-art-sales or unique-attendance series. Do not treat that absence as zero sales or proof of a continuous post-pandemic decline.
- Organizational figures were reconstructed for **2014–2023 from ProPublica's IRS extraction** and **2024 from Cause IQ**. Full underlying filings were not reviewed. Public 2025/2026 organizational figures were not found.
- HeyTaos is a possible complementary partner. Published advertising asking prices are not achieved revenue, audience size, or ROI.
- Felix's role and House of Fire contact are recorded in the meeting summary; the festival board retains its own authority. A separate commercial guide cannot assume ownership of nonprofit assets, contacts, or funding.
- Core artist participation should be free in the proposed model, with funded services and clear commissions where agreed. Paid commercial services must not purchase editorial selection.

## Financial baseline — assumptions, not achieved results

| Scenario | Completed art value | Operating income | Operating costs | Surplus / deficit before unresolved tax |
|---|---:|---:|---:|---:|
| Low | $1,000,000 | $207,000 | $265,000 | −$58,000 |
| Base | $3,000,000 | $579,000 | $485,000 | $94,000 |
| Stretch | $5,000,000 | $973,000 | $700,000 | $273,000 |

Base assumptions: 30% direct festival sales at a 20% fee, 50% gallery-referred sales at a 4% fee paid from gallery margin, and 20% commission/procurement projects at a 15% fee. Weighted artist share is 66%, or **$1.98m before artists' production costs and tax**; gallery retained is 23%; project transaction income is 11%. These are proposed terms requiring agreement.

The base funnel assumes 2,000 opt-in prospect households, 800 qualified households, 440 buying households, and 550 orders. Its **55% qualified-to-buyer conversion is aggressive and unvalidated**. Higher-value inventory and procurement capacity are also unproved.

The base model assumes $50,000 opening unrestricted financing, not committed cash or operating income. Its minimum modeled cash balance is $19,550. A 20% art-sales shortfall produces a temporary negative cash balance despite an annual surplus. The low scenario is underfunded as written. See [the financial plan](planning/02-Financial-Model-and-Targets.md) before repeating any figure.

## Date-sensitive items as of this handoff

These dates were researched for the October 19 session. Recheck current official sources before acting; a future session must not describe passed dates as pending.

- **New Mexico Arts FY28:** advance review, if required, October 23, 2026, 11:59pm Mountain; final application December 18, 2026. Published request $5,000, with match, eligibility and reimbursement conditions. Activity period July 2027–June 2028, generally with a May completion term. It cannot by itself fund the full revival. Check applicant history and authority; no submission has occurred. [Funding plan and official sources](planning/07-Funding-and-Sponsorship-Plan.md).
- **PASEO:** its own call lists September 17–18, 2027. It is a separate organization/event, not an agreed art-sales partner. It explicitly says its program does not feature booths or sales. Coordinate without assuming its dates are Fall Arts dates.
- The research notes a Larry Bell/Michelle Cooke exhibition announced October 22–November 29, 2026 and a Harwood March 2027 closure/partial reopening. Reconfirm with the venues before an itinerary or visit.

## Outstanding inputs and next useful work

1. **Felix's 2026 archive has not arrived.** Use the intake template; recover completed art sales, payouts, liabilities, attendance methods, contracts, sponsor restrictions, costs and permissions. Reconcile privately before publishing aggregates.
2. Confirm authorized festival decision makers, Felix's precise role/year, the exact recent pause/2025 edition status, and the festival/guide relationship.
3. Obtain actual available cash, weekly founder capacity, and an approved pilot ceiling. A question about cash and time was asked during the work but no answer was supplied. Scenarios were used instead; the proposed first-90-day ceiling is $15,000, not authorization to spend.
4. Test buyer demand, available works, fees and seller/settlement responsibilities through the small manual concierge pilot before custom software or major event spending.
5. Obtain venue, staffing, insurance, access and handling quotes; replace budget envelopes and reassess cash timing.
6. Prepare specific partner proposals if requested, with rights, consent, measurement and commercial terms. HeyTaos and other named organizations are uncommitted.
7. Qualify funding sources. The modeled $50,000 base grants are unawarded, and most of that amount is not tied to an identified eligible award.

Continue independent work when an input is delayed. Do not fabricate archive contents, represent the plan as approved, or repeat all completed research merely to regain context.

## Local archive and validation already performed

The unchanged original meeting notes are preserved **locally, ignored** at `private/source/FelixMeet.original-2026-10-19.txt`. SHA-256:

```text
8a0598a5dfaca65b80e27b7a70b99b3da727831c2a1cf7ffc7aece50204b7d9b
```

The private source folder also contains retrieved research material. None is required to run the public model; none should be assumed present in a fresh clone.

Initial validation checked relative document links, the original-note checksum, staged private paths and credential patterns, whitespace, model arithmetic and cash reconciliation, and identical model outputs from a clean repository export without private files. A 54-link HTTP check returned 52 successes; Frieze and Setouchi blocked automated requests with 403 responses. Further source links were added during the final research pass; do not describe every external link as automatically tested. The published initial commit matched remote `main`, with a clean ART worktree.

For the next session: inspect actual status/history, read only the relevant modules, and revalidate the changes you make. Update this handoff after meaningful work.
