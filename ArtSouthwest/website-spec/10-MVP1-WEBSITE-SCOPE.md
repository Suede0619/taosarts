# ArtSouthwest MVP1 website scope

## Executive summary

MVP1 is one ArtSouthwest website with **Taos and Santa Fe catalogs** and **one interactive AI itinerary experience to review**. Visitors can browse a small selection of artists, works, galleries and places in either city. They can also try planning and revising a same-day art outing. The first itinerary prototype uses a central Taos route and clearly labeled sample data, as defined in the [interactive MVP scope](09-V1-INTERACTIVE-MVP-SCOPE.md). Santa Fe is in scope for the catalog from day one of MVP1. A Santa Fe itinerary can follow once its route records and operating owner pass review.

The two city leads build their shortlists in parallel. The editorial lead turns cleared material into consistent, artist-centered entries. The interaction designer defines the planner conversation, and the website builder implements the city catalogs and planner. The first integrated review checks content, city navigation, and the itinerary before the bounded AI checkpoint and any decision on public release.

## Preview priorities

The two-city site is a working preview for prospective partners and funders. **First review:** complete both curated catalogs, prepare the first confirmed artist profile for clearance and demonstrate the scripted Taos itinerary. Track artist agreement, cleared profile, cleared work images and current seller details as separate milestones. The confirmed profile stays out of the release count until it clears the applicable checks.

**After the core review:** if an editor can maintain it, add a calendar demonstration with one exhibition and linked timed opening per city, plus one curated roundup that links back to the site. Track venue and artist approvals before sharing. Use gallery sharing as an acquisition test when a venue opts in. Keep recurring email, gallery self-service uploads, public AI access and monetization for later decisions.

**Studio visit test:** add a mixed-interest group to the review script. Test whether visitors can see what companions can do, what access is confirmed and whether restrooms or food are nearby. Use an opt-in studio clip as a later content experiment. The [November findings](../research/07-Calendar-Editorial-and-Artist-Intake-2026-11-21.md) document the source, commercial boundaries and evidence limits.

## Catalog size and geography

Each city targets **10 artists, 10 galleries, 10 experiences, 10 food picks and 10 lodging picks**. The two catalogs total **100 artist and place records**, plus **40–100 linked work records** at 2–5 works per artist. Coffee belongs within the food selection. Count each venue once in its primary category. A work can appear under its artist and relevant gallery without a duplicate record.

The Taos lead can include appropriate nearby communities such as El Prado and Arroyo Seco, using their actual location labels. Start Santa Fe with the city itself. A visit outside the city needs a clear reason and an accurate location label. The first interactive route stays in central Taos. The [region brief](02-REGIONS-AND-TAOS-SCOPE.md) provides background on future travel corridors.

## Selection, evidence and publication

- **What earns a place.** Choose entries for distinctive art or craft, relevance to the city, usefulness to visitors, and the strength of the sources. For artists and galleries, look for a range of media and practices and clear representation or inquiry paths. For experiences, prioritize a specific activity a visitor can understand and verify. For hospitality, weigh place, practical fit and the usefulness of the location on an art trip. Presentation order is editorial and can group entries by interest or place. Describe picks as curated selections.
- **What makes an entry usable.** Give each record an ID, city and actual locality, primary category, short reason for inclusion, source URL, source check date, editorial owner and publication status. Record image credit and permission separately. For works, record artist attribution, medium, dimensions where known and authorized seller or inquiry route. Confirm an image matches the work before including it.
- **Which facts need checking.** Verify operation, access, hours, admission and appointment requirements against an appropriate current source before release. Record what the source covers and use a clear check-with-provider action when availability is unknown. Keep seller terms, cultural review and image rights with the record. Leave unknown prices blank or label them unknown. Artist or gallery listings do not create a partnership. The [data and content specification](06-DATA-TECHNICAL-AND-CONTENT-SPEC.md) gives the broader record model.
- **How an entry moves.** City lead nominates and checks the basic facts. Editorial lead reviews relevance, copy, permissions and credit. The builder imports cleared records and checks the rendered pages. The city lead confirms unresolved venue facts before release. Use draft, ready for editorial review, cleared, hold and published as record states. Keep a reserve shortlist. If a selected entry fails a release check, use a cleared reserve or raise the category gap at review.
- **Editorial independence.** Evaluate an affiliated gallery or a PR client by the same selection criteria. Record the relationship and ask an independent reviewer to confirm inclusion. For sensitive material or visits, obtain review from the relevant cultural authority and hold the entry while that authority is unclear.

## Visitor experience and build

| Surface | MVP1 behavior | Review check |
|---|---|---|
| Homepage | Offer a clear city choice and two ways into the site, **Browse the catalog** and **Plan an art visit**. | Visitors can tell that both cities have catalogs and that the planner demo covers central Taos. |
| City pages | Show the selected city, the five listing categories, and an easy switch to the other city. Keep works discoverable from artist pages and artwork views. | Counts reconcile with records. Category links and city context work on mobile and desktop. |
| Detail pages | Show why the entry belongs, approved images and attribution where available, practical information and a reliable next step. | Every published record meets its evidence and rights checks. Missing information is clear. |
| Interactive planner | Implement the [interactive scope](09-V1-INTERACTIVE-MVP-SCOPE.md). The visitor supplies origin, time and interests, sees a short mapped route and list, then swaps a stop. Include recovery when no replacement fits or availability cannot be confirmed. | The route fits the time window, revisions update both views, and visitors understand the sample data and what they would need to confirm. |
| Santa Fe planner entry | Explain the demo’s Taos coverage and give Santa Fe visitors a direct route to the Santa Fe catalog. | No silent switch of city or fabricated Santa Fe plan. A future Santa Fe route uses a separately reviewed set of local records. |

Keep catalog and day-planner implementation in the [website repository](https://github.com/Suede0619/sw-arts-website). The [artist webform repository](https://github.com/Suede0619/asw_artist_webform) supplies intake and the approved catalog feed. Use one catalog structure with city and category fields. Start with a scripted interaction for design review. The complete MVP1 planner also needs a bounded AI checkpoint with an approved budget and server-side setup. See the [release roadmap](11-MVP-RELEASE-ROADMAP.md#mvp1-catalog-and-day-planner). Live inventory, booking and ticketing, accounts, payments and automated outreach need separate decisions. The [project baseline](../PROJECT-BASELINE.md) governs production review and the 20% platform artwork-sales commission. Use the [artist intake scope](12-ARTIST-INVITATION-AND-INTAKE.md) for the invitation, form and database workflow.

## Work packages and owners

These are proposed task assignments. Confirm each person’s scope and available time before scheduling work.

| ID | Owner | Task and handoff |
|---|---|---|
| W1 | Website builder | Set up the shared catalog sheet and category fields, build city navigation and page templates, migrate reusable Taos records after review, and integrate the planner. Hand the team a review build and a list of content gaps. |
| W2 | Taos catalog lead | Lead the Taos shortlist across all categories. Prioritize artists, works and galleries. With separate outreach authority, confirm permission and practical details. Hand editorial a ranked shortlist and reserves with evidence links and known gaps. |
| W3 | Santa Fe catalog lead | Lead the Santa Fe shortlist across all categories. Use local gallery, editorial and destination knowledge to identify strong candidates and reliable sources. Mark relevant PR or client ties. Hand editorial a ranked shortlist and reserves. |
| W4 | Editorial lead | Write the selection rubric and entry examples. Shape artist profiles, work captions and experience descriptions. Check voice, credits, culturally sensitive material and image status. Hand the builder cleared copy and a hold list. |
| W5 | Interaction designer | Explore the first planner conversation, what the assistant can infer, and how it offers choices and names uncertainty. Sketch the result, a stop swap and a case without a confirmed option. Hand the builder an annotated flow in whatever format fits the agreed time. |
| W6 | Website builder and city leads | Builder checks navigation, accessibility, catalog rendering and planner behavior. Each city lead checks their own city’s real-world facts. Editorial lead reviews final copy and credits. The project lead records the release decision and unresolved work. |

## Sequence and review gates

| Phase | Work in parallel | Exit |
|---|---|---|
| Week 1 after kickoff | Builder shares the prototype and intake sheet. City leads nominate entries. Editorial drafts the rubric and examples. Interaction designer explores the Taos conversation. | Team confirms scope and capacity, and a test route and starter records are ready. |
| Week 2 | City leads check records and identify reserves. Editorial prepares the first cleared batch. Builder turns the first batch into both city pages and wires the planner flow. | Both catalogs work in the review build with initial records. The planner completes the core sample flow. |
| Week 3 target | Complete category coverage, review rights and venue facts, test the build, and resolve or log gaps. | Project lead can approve a wider preview, request fixes or keep the build for internal review. |

The sequence is a planning estimate. Count the weeks from a confirmed kickoff and adjust for availability and rights checks. The [interactive MVP scope](09-V1-INTERACTIVE-MVP-SCOPE.md) provides its own proposed design and review window. The planner can progress while the city lists are in research.

The integrated review checks four things.

1. **Coverage.** Both cities meet the MVP1 counts, or the review records the specific gap and a decision on whether to hold or narrow release. Each included artist has at least two cleared works for the counted catalog.
2. **Content.** Every published record has local context, a reason for selection, a source date, and the appropriate rights and access checks.
3. **Navigation and interaction.** Reviewers can change cities, find an artist and work, complete a Taos itinerary, and revise a stop. A Santa Fe visitor can understand the planner boundary and return to the catalog.
4. **Operations.** The project identifies who will correct stale information and review addition requests. The project lead reviews the bounded AI checkpoint and separately decides whether to widen the preview.
