# ArtSouthwest MVP release roadmap

The [artist invitation and intake scope](12-ARTIST-INVITATION-AND-INTAKE.md) supplies the MVP1 catalog intake workflow. Live sales remain a later release gate.

## Executive summary

**MVP1 has two features.** The first is a curated catalog using the existing prototype as its design and navigation reference. Taos and Santa Fe each get 10 artists, 10 galleries, 10 experiences, 10 food picks and 10 lodging picks. The second is an interactive AI day planner. The interaction designer defines how it understands a request, explains a route and handles a change. Prototype the conversation first, then test a bounded model with approved data before calling the AI feature complete.

**MVP2 gives people a reason to return** with a curated calendar, stories and a weekly roundup. **MVP3 makes visits easier to act on** with maintained routes, Santa Fe planning, sharing and reliable provider links. **MVP4 tests a staffed collector and visitor service. MVP5 tests paid offers and controlled transactions. MVP6 expands geography and operations when the evidence supports it.** Each release has an outcome, a dependency and a decision to make before committing the next release.

This roadmap governs feature sequence. The [MVP1 implementation brief](10-MVP1-WEBSITE-SCOPE.md) controls catalog and build details. The [interactive design brief](09-V1-INTERACTIVE-MVP-SCOPE.md) covers the first planner checkpoint. The [project baseline](../PROJECT-BASELINE.md) governs operating authority and artist economics.

## Delivery sequence

| Release | Visitor outcome | Primary dependency | Review decision |
|---|---|---|---|
| MVP1. Catalog and AI day planner | Discover both cities and build and revise one grounded Taos day plan. | Curated records, rights checks, agreed interaction and a bounded model test. | Can visitors find the art they want and trust the plan enough to use it? |
| MVP2. Calendar and editorial | Find what is happening and come back for the next selection. | Named editorial coverage, verified event records and a correction process. | Can the team update this reliably, and do visitors return? |
| MVP3. Practical visit planning | Plan a usable day in either city and reach the right venue or provider. | Maintained hours, access and travel facts, including Santa Fe route coverage. | Can people act on the plan, and can the team sustain the checks? |
| MVP4. Collector and partner service | Get a useful human response, viewing or shortlist. | Accepted operator, permissioned sellers, response capacity and agreed handoffs. | Do buyers and sellers find the service useful enough to repeat? |
| MVP5. Revenue and transactions | Pay for an approved service or purchase through a supported seller workflow. | Evidence of demand, finance owner, agreements and end-to-end controls. | Does each offer cover its real costs while supporting artists? |
| MVP6. Expansion and operations | Get the same quality in another market and through more partners. | Repeatable local ownership, editorial standards, permissions and viable economics. | Can the next market operate without degrading the first two? |

Releases are gates, not calendar promises. Catalog intake and interaction design can run in parallel. Start a later release when its dependencies have owners and the team has reviewed the evidence from the earlier work. A paper design or private prototype can inform that review without expanding the live product.

## MVP1 catalog and day planner

### Catalog using the existing prototype

Retain the existing visual direction, catalog cards, browse controls and artist, artwork and place detail patterns. Add a clear city switch and show the active city on every listing and detail view. Keep links between artists, their works and authorized galleries or sellers. Give the visitor a useful next step, such as seeing the official venue page or finding the permitted inquiry route. The existing prototype is the design reference. Demo checkout and other simulated actions do not define the release scope.

| Category | Taos | Santa Fe | Combined |
|---|---:|---:|---:|
| Artists | 10 | 10 | 20 |
| Galleries | 10 | 10 | 20 |
| Experiences | 10 | 10 | 20 |
| Food | 10 | 10 | 20 |
| Lodging | 10 | 10 | 20 |
| **Total catalog entries** | **50** | **50** | **100** |

Keep **2–5 associated works per artist** from the existing brief. That yields 40–100 work records in addition to the 100 catalog entries. Treat restaurants and coffee shops as food subtypes. The earlier coffee preference can guide the selection within the 10 food picks. Count any venue once in its primary category and let linked records appear on more than one page. Maintain reserves by city and category.

Start from the available [artist cohort](data/artist-cohort.csv), [artwork leads](data/artwork-candidates.csv) and [place leads](data/place-candidates.csv). They are research inputs. Record what passes artist participation, asset, attribution, venue and seller checks separately. Keep supplied or restricted materials in approved private intake. Use clearance, current sources, selection quality and fit for the city to decide what counts toward release. If a category is short, surface the gap and its cause at review. A partial build can be reviewed internally.

### Interactive AI day planner

The first supported route is central Taos. A visitor supplies a starting point, time window and interest, sees a short ordered list and map, and can request a swap. The planner explains why each stop fits, distinguishes a published schedule from availability, and offers a shorter plan or explains the conflict if nothing fits. Entry from Santa Fe clearly identifies that the first planner covers Taos and offers the Santa Fe catalog.

- **Design checkpoint.** Use the scripted flow and fictional fixtures to review prompts, editable assumptions, result layout, swaps, and recovery from closed or uncertain stops. Try a mixed-interest group scenario and a keyboard-only walkthrough. The interaction designer proposes the conversation and result. The builder implements the agreed behavior.
- **Bounded AI checkpoint.** After agreeing a test budget and approved server-side setup, evaluate a model on real language input. Let it interpret the visitor’s request and explain a result from allowed records. Keep route selection, time and order limits, record IDs and availability rules under application control. Use confirmed sources or clearly labeled fixtures. Offer form controls on timeout, invalid output or failure. Keep secrets server-side. Request no precise location or account for this test.
- **Release gate.** A small review group can move between both catalogs, find a specific work and complete, explain and revise a Taos plan. Test missing inputs, invalid venue IDs, out-of-window routes, unknown hours and model failure. A scripted build is useful for design review while model approval is pending. Record the mode it actually uses and the remaining gate. Public model access, spending and production hosting require their own approval.

Track cleared catalog entries by category and city, usable planner completions, successful revisions, route and evidence errors, model latency and cost per usable plan. Verify mobile and keyboard use and catalog regression. Record the target review date after both city leads and the build and design roles confirm capacity.

## MVP2 calendar, stories and repeat visits

**Sprint A** adds one exhibition run and separately timed opening per city as the working example. Link each opening to its show, venue and relevant artist records. Include local start and end times, status, sources, checked dates, an editor and a correction path. Support shareable links, city views and clear handling of schedule changes, cancellations and expired records. Keep editing with staff.

**Sprint B** adds one curated roundup and one artist story tied to those records. Test an optional studio process clip with artist approval, captioning and a transcript. Compare what visitors learn from the story with the effort of producing it. Test venue sharing if the venue opts in. Introduce recurring editorial email only with a named owner, an opt-in list, unsubscribe handling and a reliable publishing cadence. Treat another publisher’s audience as their own.

**Review gate.** The editor can publish, correct and retire an entry, readers can distinguish a show’s run from its opening and the team can maintain the work over consecutive editions. Measure event and story clicks, return visits, approved partner shares and edit time. The [November meeting findings](../research/07-Calendar-Editorial-and-Artist-Intake-2026-11-21.md) give the evidence and limits behind this phase.

## MVP3 actionable visits and a planner for both cities

**Sprint A** adds reviewed public access, timed events, closures, travel legs, visit lengths and amenities to the content records. Test mixed-interest groups and supported access needs with specific facts, including what companions can do and where visitors can find a restroom or food. Add better search and filters only where the records can support them.

**Sprint B** extends the planner to Santa Fe after the local route set passes the same checks as Taos. Add shareable plans, local save and optional location preference when retention and privacy are clear. Offer a verified official venue or provider link. Use curated self-guided routes as reusable starting points. Treat reservations, ticketing and hosted tours as distinct services with their own operators and confirmations.

**Review gate.** The planner handles both cities without silently mixing their records. Test accessibility, seasonal changes and stale hours. Measure completed plans, revisions, provider handoffs, data errors, and staff time spent maintaining records. Widen public AI access only after the project establishes ownership, reliability, failure handling and a cost allowance. See the [data and content spec](06-DATA-TECHNICAL-AND-CONTENT-SPEC.md).

## MVP4 human service and partner workflows

**Sprint A** tests a staffed art inquiry and visitor brief with a small pool of willing artists and galleries. The service operator checks interest, budget and viewing needs, sends an approved brief with consent, and returns a verified shortlist or viewing option. Track who handles response, seller confirmation, pickup and shipping. A request stays pending until the provider or seller confirms it.

**Sprint B** tests a simple permissioned submission form for seller updates, exhibition dates or image files. Editors approve each change before publication. Test existing seller-system exports or feeds only where they reduce duplicate entry. Add opt-in partner referrals, private shortlists or advisor collaboration when a real workflow calls for them. Keep any account or shared history bounded by consent, retention and deletion controls.

**Review gate.** An accepted operator delivers useful responses within the agreed coverage. Sellers and buyers confirm value and the project can afford the labor. Measure inquiries, confirmed viewings, response time, editorial load, and seller effort before increasing volume. See the [buyer-led service plan](../planning/11-Website-Pivot-Collector-and-Visit-Service.md).

## MVP5 funded services, sponsorship and controlled commerce

**Sprint A** runs one paid test with a defined payer and deliverable. Try host underwriting or a scoped human sourcing service. Once demand and cost justify it, test labeled ads or newsletter sponsorship, approved paid listing tools, or paid planner use. Keep core editorial inclusion neutral. Earlier proposed rates are hypotheses.

**Sprint B** evaluates seller-led checkout, or a controlled platform purchase with a small authorized seller group if it solves an identified need. Define seller authority, price and availability, payment and processing cost, tax handling, deposit and refund terms, packing and insurance, delivery responsibility, reconciliation, and damage response. Separate the completed art value, proceeds and operating revenue. Use the current 20% commission on completed platform artwork sales. Agree the fee basis and payout terms before checkout. Partner booking integrations need separate provider terms and real confirmation.

**Review gate.** A finance owner can reconcile all funds and the team can complete an order through delivery and settlement, including failure cases, on suitable production hosting. Measure contribution after service and processing costs, refunds and fulfillment. Maintain seller-led referrals if platform checkout cannot clear the gate. See the [commerce specification](05-COMMERCE-PRICING-AND-OPERATIONS.md).

## MVP6 regional expansion and later experiments

Add the next city or corridor through a separate pilot with a local owner, reviewed records, independent editorial checks and the ability to maintain it. Expand self-service onboarding, data feeds and regional reporting once they remove measured work. Evaluate hosted tours, workshops, festival referrals and hospitality programs separately with an operator, permissions and a budget. Festival agreements, financial models and event authority remain distinct from the website.

Use the [experiments backlog](../planning/08-Experiments-and-New-Ideas.md) for artist credits, institutional buying, salons, art education, collecting programs and impact reporting. Test each against a specific artist or visitor outcome and funded support. A wider regional network, permanent staffing or full partner portal needs evidence from the first operating markets.

## Ownership and operating rhythm

The city leads own selection and local verification. The editorial lead owns copy and clearance review. The interaction designer owns the planner design. The builder owns integration and release checks. The project lead makes scope and release decisions. Design and technology choices, including any framework migration, follow the needs shown by the review. Editorial coverage, service operations and finance each need an accepted owner before the corresponding phase. Named working assignments are recorded locally.

At each review, record coverage, data gaps, user observations, operating effort and the next gate. Name who owns any issue that can delay release. Keep only the features that improve the intended outcome and can be supported with the capacity available.
