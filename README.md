# Taos Arts — revival, livelihoods, and a year of execution

A document repository for Dave Paul and Felix Kay's work to help Taos artists sell art, remain in the community, and reach a wider public. Taos Fall Arts Festival is the initial focus; a separate curated Southwest arts guide is a proposed year-round partner product.

**Prepared October 19, 2026. Day one: November 1, 2026. Year one: November 1, 2026–October 31, 2027.** The plan begins after the 2026 festival, not before a future move to Taos. Dave Paul is already based in Arroyo Seco. This is a working proposal, not an approved festival program or a promise of sales.

[Current project baseline](PROJECT-BASELINE.md) records Dave Paul (also David Paul), the common timeline, pre-kickoff dates, current website decisions and the distinction from older financial illustrations. November 1 is project kickoff, not an automatic website launch or billing date.

## Start here

| Document | What it provides |
|---|---|
| [Southwest Art website — specification and prototype review](website-spec/README.md) | Taos-first spec, provisional Atomic design, zero direct-artist commission and researched candidates. **[Prototype source](https://github.com/Suede0619/sw-arts-website) implemented; [GitHub Pages preview](https://suede0619.github.io/sw-arts-website/) status in [the handoff](SESSION_STATE.md). Review before production.** |
| [Felix meeting — consolidated](FelixMeet) | One detailed account replacing four overlapping note versions, with Dave Paul's HeyTaos correction and House of Fire contact details. Kept at the original extensionless path. |
| [PRD and business plan](planning/01-PRD-and-Business-Plan-2027.md) | Mission, audiences, offers, business model, outcomes, governance, and launch conditions. |
| [Financial model and targets](planning/02-Financial-Model-and-Targets.md) | $1m / $3m / $5m art-sales scenarios, artist shares, operating budget, break-even and cash risk. |
| [Roadmap and first 90 days](planning/03-Twelve-Month-Roadmap-and-First-90-Days.md) | Dated tasks, proposed owners, decision gates, and a manageable pilot. |
| [History and economics](research/01-Taos-Fall-Arts-History-and-Economics.md) | Taos art history, festival milestones, annual organizational finances, missing sales/attendance evidence, and decline hypotheses. |
| [World benchmarks](research/02-Global-Festival-Benchmarks.md) | Sixteen event models, comparable numbers and their limits, lessons for sales and public enjoyment. |
| [HeyTaos and regional partnerships](research/03-HeyTaos-and-Regional-Partnerships.md) | Corrected identity, published advertising offer, complementary roles, and a measurable pilot proposal. |
| [Sources and open questions](research/04-Source-Register-and-Open-Questions.md) | Source links, evidence quality, unresolved claims, and what Felix's archive needs to answer. |

## The important findings

Public sources establish the festival's history and an organizational financial record, but **not a reliable annual series of total artwork sales or unique attendance**. Unknowns are left unknown. Felix's forthcoming 2026 folder should help reconstruct the baseline.

The older commission-bearing financial illustration models **$3m completed art value**, with a proposed **$1.98m artist share before production costs/tax**, **$579,000 operating income**, and **$485,000 operating expenses**. These are assumptions to test. The low case has a deficit; even an annually profitable case can run short of cash before festival sales arrive. Artist balances cannot finance operations.

The newer website specification requires **zero Southwest Art commission on direct artist sales** and separately addresses funding payment fees. Its economics supersede the older website assumptions. The older illustration above is not the current website budget or an approved consolidated forecast. Dave has now authorized building and publishing a design prototype in the separate `sw-arts-website` repository; production selling still requires a further review. Audo #11 is a provisional prototype direction, not a finalized brand decision.

**Near-term action:** determine immediately whether the authorized festival applicant must submit New Mexico Arts advance review by **October 23, 2026, 11:59pm Mountain**. The FY28 request is $5,000, with eligibility, match, public-program, and reimbursement conditions. Final applications are due December 18. [Funding plan and official links](planning/07-Funding-and-Sponsorship-Plan.md).

## Execution modules

- [Collector acquisition and sales](planning/04-Collector-Acquisition-and-Sales-Playbook.md)
- [Festival operations, artist equity, governance](planning/05-Festival-Operations-Artist-Equity-and-Governance.md)
- [Product, data and AI specification](planning/06-Product-Data-and-AI-Specification.md)
- [Funding and sponsorship](planning/07-Funding-and-Sponsorship-Plan.md)
- [Experiments and new ideas](planning/08-Experiments-and-New-Ideas.md)

## Working tools

Use private copies for actual personal, financial, contractual, or donor information:

- [2026 archive intake](templates/2026-Archive-Intake.md)
- [Partnership memorandum outline](templates/Partnership-MOU-Outline.md)
- [Artist/seller agreement checklist](templates/Artist-and-Seller-Agreement-Checklist.md)
- [Buyer brief](templates/Buyer-Brief.md)
- [Weekly scorecard](templates/Weekly-Scorecard.md)
- [Data definitions and downloadable tables](data/README.md)
- [Generated model results](data/model-results.md)

Recalculate the model with Python 3, standard library only:

```sh
python3 tools/financial_model.py
```

## Repository practice

New sessions should begin with [AGENTS.md](AGENTS.md) and the dated [session handoff](SESSION_STATE.md), which record completed work, key assumptions, validation, and unresolved inputs.

This repository is **public**. The unedited original meeting notes are preserved locally under ignored `private/source/`; future confidential archives belong under `private/` or in an appropriately controlled document store. Public documents contain business contact details supplied for House of Fire, research, planning assumptions, and empty templates. They do not include buyer lists, bank records, or private sales ledgers.

`ART` is an independent Git repository linked to [Suede0619/taosarts](https://github.com/Suede0619/taosarts). The surrounding Taos workspace remains separate. See [contribution and update guidance](CONTRIBUTING.md) before adding sources or future documents. Third-party images, text, logos, and records require their own permission; linking a source does not grant reproduction rights.
