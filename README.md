# Taos art research and project plans

A collection of anonymous foundational documents, research, ideas and proposed plans to help Taos artists sell art, remain in the community and reach a wider public. The current direction is a year-round curated art and destination platform as the core business, with festivals and events supporting discovery, relationships and visits. Taos is the first proof of concept. Public documents assign responsibilities by role and omit personal attribution.

**Research prepared October 19, 2026. Strategy/operating alignment October 23. Denver research and comprehensive proposal/brand/presentation package October 24, 2026. Day one: November 1, 2026. Year one: November 1, 2026–October 31, 2027.** These working proposals have no festival approval and promise no sales.

[Current project baseline](PROJECT-BASELINE.md) records the common timeline, pre-kickoff dates, current website decisions and the distinction from older financial illustrations. November 1 starts the project. Launch and billing need separate decisions.

## Main documents

| Document | What it provides |
|---|---|
| [COMMON ALTITUDE. Denver full proposal and decks](Denver/Common-Altitude-2027/README.md) | Creative/brand, business/PRD, marketing, 72 partner candidates, event week, staffing and 365-day/53-week execution plan. Seven designed pitch decks plus brand deck in PPTX/PDF. |
| [Denver summer 2027 fair research](Denver/Summer-2027-Fair-Research/README.md) | Developer rental/events evidence, owner-share/sales sensitivities, pitch requirements, team candidates, compensation/seed analysis and naming. Research only. No actual deck or event approval. |
| [Platform strategy and starter brand brief](planning/10-Platform-First-Strategy-and-Brand-Brief.md) | Short current onboarding brief: platform-first direction, inclusive full-spectrum art, Taos v1, correct listing illustration and a brand scope to agree before work. |
| [People, meetings and commitments. Operating method](operations/README.md) | One private people register and central activity log. Public foundations remain anonymous. Named records, correspondence and NDA portfolios are local-only, outside public Git. |
| [Southwest Art website. Specification and prototype review](website-spec/README.md) | Taos-first spec, provisional Atomic design, zero direct-artist commission and researched candidates. **[Prototype source](https://github.com/Suede0619/sw-arts-website) implemented. [GitHub Pages preview](https://suede0619.github.io/sw-arts-website/) status in [the handoff](SESSION_STATE.md). Review before production.** |
| [Foundations and ideas](PROJECT-FOUNDATIONS.md) | Anonymous concept brief covering artist livelihoods, a selective guide, referral networks, education, AI, funding and unresolved decisions. |
| [PRD and business plan](planning/01-PRD-and-Business-Plan-2027.md) | Mission, audiences, offers, business model, outcomes, governance, and launch conditions. |
| [Financial model and targets](planning/02-Financial-Model-and-Targets.md) | $1m / $3m / $5m art-sales scenarios, artist shares, operating budget, break-even and cash risk. |
| [Founder compensation and hiring. Three scenarios](planning/09-Founder-Compensation-and-Hiring-Scenarios.md) | Anonymous proposals for founder pay, ownership/profit sharing, additional revenue, cash buffers and evidence required before hiring. Separate from the legacy festival model. The parties have agreed no compensation or split. |
| [Roadmap and first 90 days](planning/03-Twelve-Month-Roadmap-and-First-90-Days.md) | Dated tasks, proposed owners, decision gates, and a manageable pilot. |
| [History and economics](research/01-Taos-Fall-Arts-History-and-Economics.md) | Taos art history, festival milestones, annual organizational finances, missing sales/attendance evidence, and decline hypotheses. |
| [World benchmarks](research/02-Global-Festival-Benchmarks.md) | Sixteen event models, comparable numbers and their limits, lessons for sales and public enjoyment. |
| [HeyTaos and regional partnerships](research/03-HeyTaos-and-Regional-Partnerships.md) | Corrected identity, published advertising offer, complementary roles, and a measurable pilot proposal. |
| [Sources and open questions](research/04-Source-Register-and-Open-Questions.md) | Source links, evidence quality, unresolved claims, and what the 2026 festival archive needs to answer. |

## Evidence and financial assumptions

Public sources establish the festival's history and an organizational financial record, but **not a reliable annual series of total artwork sales or unique attendance**. Unknowns are left unknown. The outstanding 2026 festival archive could help reconstruct the baseline.

The older commission-bearing financial illustration models **$3m completed art value**, with a proposed **$1.98m artist share before production costs/tax**, **$579,000 operating income**, and **$485,000 operating expenses**. These are assumptions to test. The low case has a deficit. Even an annually profitable case can run short of cash before festival sales arrive. Artist balances cannot finance operations.

The newer website specification requires **zero Southwest Art commission on direct artist sales** and separately addresses funding payment fees. Its economics supersede the older website assumptions. The older illustration above is not the current website budget or an approved consolidated forecast. The separate `sw-arts-website` repository publishes the design prototype. Production selling still requires a further review. Audo #11 remains a provisional prototype direction. The brand decision stays open.

**Deadline status as of October 24:** the New Mexico Arts conditional advance-review deadline of **October 23, 2026, 11:59pm Mountain has passed**. Authorized-applicant eligibility and submission status remain unknown. The previously researched FY28 request is $5,000, with eligibility, match, public-program and reimbursement conditions. The published final deadline is December 18. This is separate from Denver funding. [Funding plan and official links](planning/07-Funding-and-Sponsorship-Plan.md).

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

## Repository and writing rules

Follow [WRITING-GUIDE.md](WRITING-GUIDE.md) for prose, headings, labels and presentations.

New sessions should begin with [AGENTS.md](AGENTS.md) and the dated [session handoff](SESSION_STATE.md), which record completed work, key assumptions, validation, and unresolved inputs.

This repository is **public**. Ignored `private/source/` preserves the original meeting notes unchanged. Named team/meeting records and the central activity log are in ignored `private/operations/`. Existing person-material folders have local Git exclusions. These records and NDA files do not sync through public GitHub. Future confidential archives belong under `private/` or in an appropriately controlled document store. Public documents contain business contact details supplied for House of Fire, research, planning assumptions, and empty templates. They do not include buyer lists, bank records, or private sales ledgers.

`ART` is an independent Git repository linked to [Suede0619/taosarts](https://github.com/Suede0619/taosarts). The surrounding Taos workspace remains separate. See [contribution and update guidance](CONTRIBUTING.md) before adding sources or future documents. Third-party images, text, logos, and records require their own permission. Linking a source does not grant reproduction rights.
