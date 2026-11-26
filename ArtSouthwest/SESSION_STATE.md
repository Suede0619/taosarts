# ArtSouthwest handoff

## November 25 full-width catalog backgrounds

The Taos and Santa Fe catalog pages extend the green purpose band, light catalog sections and gray visit-planning band to both browser edges. The visit-planning image now aligns with the experience cards and artist heading in the shared 1600px grid. Render serves [catalog revision `40e5d65`](https://github.com/Suede0619/sw-arts-website/commit/40e5d65991731d8395f418c64e19646863f45a67) after a manual deploy of the GitHub-verified intake revision `d4d56d7`. Both city pages passed desktop and phone checks with JavaScript disabled. The artist form and curator desk returned HTTP 200 after the switch.

## November 25 Render hosting cutover

The catalog, artist form and curator desk now run on the same Render Node service in Ohio. The first deploy used intake revision `c04c807`, which pins catalog revision `267ed92`. Three DNS-only Cloudflare CNAMEs point to Render. Each domain has a verified certificate and returned HTTP 200 from Render. The Mac is available for rollback through the previous tunnel configuration. The [deployment runbook](https://github.com/Suede0619/asw_artist_webform/blob/main/DEPLOYMENT.md#always-on-hosting) records the production setup.

Live verification opened the existing submission and its four private images. It also created a fictional application, four uploads and a callback. The curator published the fictional profile and three artworks, then paused them. The public profile and images came down, and verification removed the test data. One-time browser recovery also passed. Automated receipts and emailed artist links still need sender configuration.

## November 25 approved layouts and hosting preparation

The [live catalog](https://artsouthwest.com/) uses the approved prototype’s split hero, collection grid, mission band, gallery rows, experience cards, hospitality cards and illustrated trip-planning section. Sections share a 1600px outer container. The server sends catalog content in the first HTML response and refreshes published artwork after an approval, sale or withdrawal. Browsing no longer depends on a browser catalog request. Public category and detail URLs support direct navigation. The GitHub Pages design reference remains available.

Desktop and mobile verification covered 1920px, 390px and 320px views, city switching, food and lodging tabs, filtering, saved selections and the Taos planner. All nine home sections were 1600px wide at the 1920px viewport. Desktop browsing worked with JavaScript disabled. A curator pause removed the published page in the test branch, and republishing restored it. Live HTTPS tests preserved the existing submission, checked uploads and recovery, and removed the fictional verification records. Public samples returned their first byte in 0.28 to 0.47 seconds after the switch.

The [hosting runbook](https://github.com/Suede0619/asw_artist_webform/blob/main/DEPLOYMENT.md#always-on-hosting) packages the three domains into one Render Node service and pins the catalog revision from GitHub. The packaged build ran locally with production settings and the private review API.

## November 25 live domains and Neon cutover

The catalog is live at [artsouthwest.com](https://artsouthwest.com/). Artists submit and update work at [artist.artsouthwest.com](https://artist.artsouthwest.com/?campaign=taos-artists). Staff approve submissions and handle callback requests at the [password-protected curator desk](https://curator.artsouthwest.com/). The old campaign link redirects to the artist form. An active session on the old form can transfer through a one-time link. At the Neon cutover, Cloudflare forwarded all three hosts to the Mac’s private Node origin. The later Render cutover moved hosting while keeping the Neon data. The [deployment guide](https://github.com/Suede0619/asw_artist_webform/blob/main/DEPLOYMENT.md) records configuration and verification procedures.

The cutover rotated the database password, took the final private SQLite snapshot and migrated one existing submission, four image records with their originals and previews, and one callback. The live form now writes to Neon Postgres and private Object Storage. The live test verified new intake, callbacks and uploads, role isolation, private previews, and one-time artist recovery. It removed the fictional records and files after checking them. Approval, publication and withdrawal also passed on a separate Neon branch.

Collectors browse the site without accounts. Artists begin in the form and can save a private one-use link to return from another device within 180 days. Keep the same intake for new artwork and updates. Configure a verified transactional sender to support emailed sign-in links and receipts. Add named staff access as the curator group expands. The first campaign uses the artist host with the Taos campaign parameter. The existing letter and campaign artwork live in the ignored artist invitation folder. Send an internal Mailchimp test before the recipient campaign.

## November 25 catalog and intake release work

The approved prototype design carries into a separate production build in the existing catalog repository. It serves at `/discover/` on a configured intake origin, reads approved artists, available works and previews from the catalog API, and includes 80 source-linked place records. The two cities each have ten galleries, ten experiences, ten food listings and ten stays. The place copy uses facts from the individual sites. Venue photo candidates and their source and rights records are in the private archive. The GitHub Pages preview continues to serve the original design prototype.

The Taos planner generates a timed proposal and can revise the route using a fixed list of stops. It flags hours, access and reservations for confirmation. The service can call an AI model for stop selection when the server has a model key. The integrated browser check used the suggested itinerary mode. The concierge’s design and live-model review remain open.

The staff desk shows its storage backend and searches by reference, name or email. Staff can inspect the original submission details and private image previews. Artists can submit an update after publication. The previous version remains public until staff approve the update. The [intake runbook](https://github.com/Suede0619/asw_artist_webform/blob/main/DEPLOYMENT.md) describes the operator’s verification and approval steps.

The live intake continues to accept submissions through the macOS origin and Cloudflare tunnel. The live SQLite database and its image files have a verified private snapshot. A one-day Neon branch verified the SQLite import twice using a fictional record, including byte comparisons of originals and display files. Tests verified the Neon form, staff sign-in, image privacy, approval, withdrawal and catalog display. The production transfer needs the database credential rotation and a short cutover window.

Release order: complete the live migration, verify staff access and transactional email, and onboard the first ten artists per city while editorial clears venue images. Test the model-backed concierge with the interaction designer and confirm managed hosting before inviting the broader audience. The later onboarding agent should submit revisions through the same form API and staff queue. Extend the workflow to galleries, experiences, food and stays after testing the artist version. Tucson follows the two-city release.

## November 25 Neon integration

The intake app can use Neon Postgres and private Object Storage. The CLI deployed the services to the linked production branch. A separate local webform process tested saving drafts, private media access, submission, staff approval, catalog publication and withdrawal with fictional records. The public form still uses the existing SQLite and media store. The database credential needs rotation before moving real submissions. See the [intake source repository](https://github.com/Suede0619/asw_artist_webform) for the runtime and versioned schema.

## November 25 catalog and onboarding direction

The project lead approved the prototype designs for the finished website. The catalog launches with Taos and Santa Fe, with Tucson planned third. The [intake specification](website-spec/12-ARTIST-INVITATION-AND-INTAKE.md#form-and-agent-publication-workflow) records the shared form and agent workflow and human approval gate. The existing intake service produces an approved artist feed. The catalog connection and Neon migration remain pending. The prototype at GitHub Pages and the artist form at the custom domain both responded over HTTPS.

## November 23 direct artist profile

The live artist invitation opens the profile directly. Artists enter email alongside their bio and can save and resume in the same browser. The former start URL redirects to the profile. The local review desk holds submissions and callback requests. Email receipts and cross-device recovery require a transactional sender. Five API tests, two browser tests and desktop and mobile checks at the live address passed. The database upgrade preserved the callback queue. The [intake specification](website-spec/12-ARTIST-INVITATION-AND-INTAKE.md) records the updated flow.

## November 23 live artist webform update

The live artist form uses the Adobe Door photograph, the transparent ArtSouthwest wordmark and the approved invitation, callback and submission copy. The visible privacy links were removed. Artists grant website publication permission before submitting, and the staff desk handles catalog publication.

The preview refreshed at its existing public HTTPS address. The served photo and wordmark match the approved files. Four API tests, two browser tests and desktop and mobile checks at the public address passed. The preview uses sample data and simulates email and callbacks.

The webform serves Lato for body text and controls and Cormorant Garamond for headings. The shorter “Show your work with ArtSouthwest” title uses 70% of the prior type size. Chrome verified the rendered fonts and heading size on both desktop and mobile at the public address.

## November 23 naming update

The project adopted **ArtSouthwest**. Its folder is `ART/ArtSouthwest/`. The independent catalog checkout is `ArtSouthwest-website/`, and the intake service is `artist_webform/`. The plans, both website codebases, campaign copy and ten temporary logo options use the new name. The invitation pack contains the revised logos and the original ten editorial photos.

The public artist form preview serves the new name and wordmark. The [webform README](https://github.com/Suede0619/asw_artist_webform/blob/main/README.md#live-preview) records its temporary address and sample workflow. The catalog uses the existing GitHub Pages deployment workflow. Shared ART links point to the renamed folder. Original source records and the Mailchimp campaign files are in the private archive.

The build, four intake tests, two intake browser tests and nine catalog browser tests passed. Project links, all 61 invitation gallery links and all 20 download entries resolved. The financial model reproduced all three current scenario CSVs.

## November 23 artist intake implementation

The [artist webform repository](https://github.com/Suede0619/asw_artist_webform) contains the React and Express intake service at commit `e97ad2c`. The independent checkout lives at `artist_webform/`. It supports callbacks, private drafts and email links, profile and artwork uploads, consent and commission acknowledgment, editorial corrections and publication, sale reports and withdrawal. The catalog can read approved data at `/api/catalog`. The service creates its SQLite database on startup. Private images and the database share a durable volume. The [intake scope](website-spec/12-ARTIST-INVITATION-AND-INTAKE.md) records the implementation choices.

The production build, four API tests, two desktop and iPhone-sized Chromium journeys, and dependency audit passed. Tests used fictional records and simulated or local-file email. GitHub `main` was verified after pushing the reviewed source. Launch still needs HTTPS hosting, a persistent volume, transactional email credentials and a delivery smoke test. The application was not deployed and no invitation was sent. The existing catalog prototype did not change. The project-level ignore file protects the independent checkout and invitation exports. The ArtSouthwest documentation edits are local.

## Taos artist campaign and intake

The [artist invitation and intake scope](website-spec/12-ARTIST-INVITATION-AND-INTAKE.md) defines the Mailchimp-to-form journey, callback option, upload checks, draft saving and approved catalog publication. The campaign direction sets 20% commission on completed artwork sales through ArtSouthwest. The October zero-commission model remains historical. The local campaign pack contains artist-facing copy and visual options. Launch depends on a confirmed form URL, permissioned audience, callback coverage, approved seller terms and implemented data controls. No invitation, form or checkout was launched. Verification covered the 20 visual assets, logo text, form diagram, local links, archive contents and Git exclusion for the private campaign pack.

## November 21 staged MVP roadmap

The [MVP release roadmap](website-spec/11-MVP-RELEASE-ROADMAP.md) sets six release gates. MVP1 targets 100 artist and place entries across Taos and Santa Fe and a Taos planner with scripted design and bounded AI checkpoints. Later releases cover editorial, visit planning, staffed service, commerce and expansion. The build review needs city shortlists, asset permissions, accepted owners and approval for model testing. The website implementation and cost approvals remain open. Verification covered 24 local links, six release sections, five catalog count rows and Git exclusion for named assignments. Document baseline: `21ea53e`.

## November 21 meetings and confirmed artist intake

The [meeting findings](research/07-Calendar-Editorial-and-Artist-Intake-2026-11-21.md) and [MVP1 scope](website-spec/10-MVP1-WEBSITE-SCOPE.md) prioritize a two-city preview, one scripted Taos itinerary, and a later editorial sample with separate exhibition runs and timed events. The review adds mixed-interest visit needs and shipping questions. The planning modules carry the applicable decisions and evidence limits. Historical budgets and website source retain their existing state.

The project has one artist with documented agreement to appear. The local artist intake holds her draft profile and two original card photos. Work-specific images, rights, availability and seller details remain open. No second consent appears in the accessible project evidence. Document baseline: `21ea53e`.

Verification covered 80 local link targets, all 11 planning modules, both summary snapshots, byte-for-byte comparison of the two supplied originals and Git exclusion of the private records.

## MVP1 two-city website scope

The [MVP1 website scope](website-spec/10-MVP1-WEBSITE-SCOPE.md) sets per-city catalog counts for Taos and Santa Fe and uses the central Taos interactive planner as the first design test. It defines roles, handoffs, content review and release criteria. The baseline and website navigation documents point to the new scope. Named assignments are held in the ignored project archive. Team capacity, real records, publication permissions and the release date remain open.

## November 19 platform scoping update

The [November 18–19 synthesis](research/06-Platform-Scoping-2026-11-19.md) integrates three supplied meeting summaries. It documents a proposed same-day Taos itinerary prototype, catalog and trip-planning entry points, a blog and newsletter, and a cultural review step before publication. The project baseline, foundations, buyer-led service plan, source register and AI specification link the findings where they apply. The project holds the source links and snapshots in its Git-ignored archive.

Next scoping decisions cover workstream owners, data reliability, editorial capacity, brand structure, audience development and launch economics. Taos is the current v1 scope. Zero ArtSouthwest commission on direct-artist website sales remains the policy. The meeting notes supply proposals and preferences. Production, spending, staffing, partner terms and launch timing still require decisions. Document baseline: `57e878e`.

Verification covered eight knowledge-base files, 16 local links and anchors, three source snapshots and four ignored archive files. The update covers planning documents and private source intake only.

## November 19 interactive MVP scope

The [interactive MVP scope](website-spec/09-V1-INTERACTIVE-MVP-SCOPE.md) defines one simulated same-day Taos itinerary, from homepage entry through an editable brief, map and list, stop swap and no-fit recovery. It assigns proposed design, implementation, local arts review and decision responsibilities. November 23–27 is the proposed work window, with review targeted for November 30. Confirm availability and handoffs at the scope discussion. The review covers usability and route logic before a separate decision on live data, AI or wider release.

The document checks cover relative links, example route arithmetic, dates, anonymous wording and staged scope. The independent prototype is the implementation target for a later review build. Document baseline: `2831abc`.

## November 18 European Cellars reference review

Reviewed the public [wine catalog](https://www.europeancellars.com/our-wines/), [producer directory](https://www.europeancellars.com/producers/), one producer profile, one item detail, and the site's public sitemap. Added a [database-driven arts sitemap proposal](website-spec/09-DATABASE-DRIVEN-ARTS-SITEMAP.md) with linked catalog records, search and facets, artist/gallery/work profiles, designed and guided tours, visit planning, and publication safeguards. The proposal adapts information architecture only; it copies no text, images, code, or brand assets. Taos remains the only v1 region. Brand, cultural scope, production, and live services remain open decisions. The prototype and its data did not change.

## November 7 private gallery-content intake

A local intake contains four artist-profile messages and four attached work images. A private working catalog records supplied work metadata and concise editorial notes. One image carries a visible signature that conflicts with the artist named in its email; that association remains on hold. The messages do not document image/profile publication permission, seller authority, current availability, or confirmed buyer-facing pricing and shipping. Originals remain unchanged, and the intake folder is Git-ignored. No material was added to the public prototype.

## October 25 service pivot, audiences and Taos institutions

Start with the [buyer-led collector/visit service proposal](planning/11-Website-Pivot-Collector-and-Visit-Service.md) and [outreach hub](outreach/README.md) for current pitch preparation. The recommendation changes the leading offer from a paid profile to a useful buyer request and funded service. Existing seller records remain authoritative. Hosts could fund service capacity; buyers could pay for separately scoped optional work. All prices, demand, staffing and commercial results remain unvalidated. Zero platform commission on direct-artist website sales and Taos-first scope remain controlling.

The package contains 23 personas, a complete persona/product/pitch/timing matrix, 11 audience-grouped thirty-second scripts with editorial evaluations, an AI trust/environment note and a 117-record [entity roster](outreach/04-Taos-Arts-Entity-Directory-2026-10-25.md) with [CSV evidence fields](data/taos-arts-entities-2026-10-25.csv). Forty-one records have first-party identity evidence, 69 rely on network listings, six are conflicting/historical leads, and one uses supplied business details. These are organizations, sites and programs, not 117 verified active businesses or a complete census. The [source-register addition](research/04-Source-Register-and-Open-Questions.md#october-25-audience-institutions-and-service-pivot-additions) records the focused research.

The [Art as Teacher brief](research/05-Art-as-Teacher-Foundation-2026-10-25.md) documents its website's 2025 founding and planned first events in 2027. Its mission suggests listening about a small artist-approved digital learning encounter. Do not treat it as an agreed funder, lead source or commercial partner. Existing local institutional and hospitality innovation informs the approach.

Social pitches begin with attention to the person and occasion, permission and one relevant topic. Booked discovery precedes a funded rehearsal; regional-show invitations follow local feasibility. Named intake and personal role-boundary drafts stay ignored under shared TEAM. No outreach occurred. The service needs an accepted, funded operator; digital production does not imply sales or concierge work.

Validation covers local document links, all 23 persona/pitch matches, 11 scripts of 56–61 words, 117 unique directory IDs with evidence/source fields, source hashes, publication anonymity and ignored private records. Website source, financial model inputs and generated outputs remain unchanged. The existing live prototype still has scripted assistance and demo commerce. No production AI, inventory integration, live sale or deployment was added. Document baseline: `98b8b18`.

## October 25 prototype and link verification

[The workspace verification record](../WORKSPACE-VALIDATION-2026-10-25.md) confirms that the folder moves preserve document navigation and the prototype. Static checks and all nine browser tests pass from `ArtSouthwest-website/`. All 64 pages render locally and live on desktop and phone, with no broken images, failed site responses, runtime errors or horizontal overflow. All 17 published files match local bytes. The existing successful Pages deployment remains current. This verification requires no source or deployment change. Website source baseline: `6a70379`.

Read the shared [ART instructions](../AGENTS.md), this workflow's [AGENTS.md](AGENTS.md), and [PROJECT-BASELINE.md](PROJECT-BASELINE.md) first. Research remains an **October 19, 2026 snapshot** unless a specific source has a newer check date. This handoff records technical state and decisions without personal project attribution.


## October 25 folder organization

ArtSouthwest shows, research, platform plans and website work now live together in `ART/ArtSouthwest/`. [The folder map](README.md#folder-map) describes planning, research, website specifications, data/model tools, templates and operations. The independent website checkout is now `ART/ArtSouthwest/ArtSouthwest-website/`, with its Git history and origin intact. Local ArtSouthwest sources remain under ignored `private/`. Following the subsequent shared-team clarification, member folders and central operations now live in [TEAM](../TEAM/README.md) across both projects. The central people/activity registers retain their IDs and cross-workflow references.

The Denver Energy Center festival has its own sibling [workflow](../Denver/README.md) and [handoff](../Denver/SESSION_STATE.md). The Denver summaries from this former ART-wide handoff now live there. Shared writing guidance and the October 24 review remain at the ART root. Baseline before organization: `a3f74a3193524b647f089d6f3b12edeaca57e001`. Moving folders does not refresh research or change project decisions. Validation results appear in [the workspace handoff](../SESSION_STATE.md).

## October 24 writing review

The user requested a repository-wide rewrite under [WRITING-GUIDE.md](../WRITING-GUIDE.md). [The review record](../EDITORIAL-REVIEW-2026-10-24.md) describes the scope and checks. Baseline document commit is `bbcf37709c31898f20f87a828ee68ffa8a2c9c2a`.

The revision covers all 111 existing Markdown files, human-readable data fields, generator copy and 101 presentation slides. The generators produce matching reports and slide scripts. PowerPoint and PDF copies contain the revised wording. Numeric model inputs and calculation logic match the baseline. Raw sources, original notes, NDA material and research dates remain intact.

The separate prototype repository also receives a wording review. Its documentation, page copy and research summaries follow the same guide. Keep the public HOUSE of FIRE business association as the only participant-name exception. Prototype commit `3d04b8636507646cddc4aa99bedc5a1a252c9186` is live. [GitHub Actions run 40097912500](https://github.com/Suede0619/sw-arts-website/actions/runs/40097912500) passed validation, all nine browser tests and deployment. Public index.html, app.js and data.json match local files byte for byte. Local review covered all 64 routes with no runtime errors or horizontal overflow, plus desktop and phone visual checks.

Document checks cover 117 Markdown files across both repositories, 437 relative links, ten JSON documents with identical numeric values, forty CSV files with stable schemas, rows, numeric cells, dates, IDs and URLs, and four calculation/validation scripts with identical logic. Regeneration reproduces the edited reports, partner lists and calendars. Package checks cover eight PPTX/PDF pairs, 101 pages, 1,139 text shapes and 97 retained source hashes. Private records remain excluded from both commits.

## October 23 platform and operating-system update

The [current strategy and starter brand brief](planning/10-Platform-First-Strategy-and-Brand-Brief.md) now leads onboarding. The year-round art/destination platform is the proposed core business. Festivals support discovery, relationships and visits. Include contemporary and a full range of art. Taos remains the only v1 region. Denver and regional representatives are hypotheses. Proposed 10% of unspecified “sales” is not agreed and cannot override zero direct-artist commission. The project has no approved brand appointment, budget, ownership or compensation terms.

The [operating method](../TEAM/OPERATING-METHOD.md) establishes one private people register and one central activity/commitment/decision log, linked to source IDs and meeting records. Actual names, contact details, supplied correspondence, the new meeting account, portfolio review and draft sharing packet are local-only in ignored operational/person-material folders. Start with `../TEAM/operations/README.md` if available. The later October 25 clarification placed shared internal member folders directly under ART/TEAM. Named TEAM records remain ignored. Verify exclusion before copying new private material. Public GitHub contains none of these private records. The setup includes no shared private store or backup.

The shared note’s October 21 creation date supports the supplied Wednesday account. The private archive holds the shared document’s summary. Full audio/verbatim transcript was not recovered. The supplied portfolio exists locally and retains its NDA/no-forward restriction. The private catalog records three reference links, accessible snapshots, metadata and evidence limits. A public HTTP source was available where HTTPS failed, and restricted high-resolution photographs were not accessed. Reference contacts are not recruited team members. The notes, repository and prototype sharing packet awaits sending. Group-chat completion, exploratory introductions and reading remain unconfirmed. No email, text, recruitment or sponsor outreach occurred.

The $4,184/month calculation assumes 12 gallery profiles at $150, 8 restaurant profiles at $99 and 8 lodging profiles at $199. Artist profiles are free. No revenue or profit has materialized. Official Naoshima history does not support an oil-company origin. The reviewed sources establish no most-visited-island claim. Local-editor use does not guarantee local AI inference/no transmission. A reported Santa Fe event with 43 international galleries remains unidentified. Source context is in the [focused source-register addition](research/04-Source-Register-and-Open-Questions.md).

The New Mexico Arts conditional advance-review deadline was **rechecked October 23: today at 11:59pm Mountain**. Authorized-applicant eligibility/history is unknown. The project submitted no application. Artist/gallery schedules remain older snapshots. November 1 remains project day one. No launch date has approval.

The public README, baseline, foundations, business plan, roadmap, website index and agent instructions now follow the current brief. Financial model inputs/outputs, financial assumptions and website source were not changed. Baseline before this work: document commit `c61e6ad4c7c5c19e6f87133ba0c1cda9af760111`. The work left parent-workspace files untouched.

Validation: all 242 relative references across 44 public and 14 relevant private Markdown files resolve. Public text anonymity audit passes with only the existing HOUSE of FIRE listing exception. All 39 central-log IDs are unique. Checks covered listing arithmetic, retained hashes, the original NDA PDF checksum and the earlier private source archive checksum. Git exclusions cover named folders and private records. That change staged no financial-model or website source files. `git diff --check` passes.

## Publication standard and current stage

- Public foundations, brainstorming, plans, specifications, research tables, agent instructions and prototype copy are **generic and anonymous**. Do not publish participant names, biographies, dedications, personal circumstances or narratives of who introduced an idea or completed a task. Use accountable role titles.
- Public documents may retain the factual HOUSE of FIRE business association. Independently sourced artists and historical figures remain valid research subjects. Ignored private records may retain original names and provenance. Preserve originals.
- **November 1, 2026 is day one**. Year one ends October 31, 2027. Historical/source dates are not moved to kickoff.
- The separate [sw-arts-website repository](https://github.com/Suede0619/sw-arts-website) publishes the design prototype. The next stage is prototype review before production. A design preview grants no authority for purchases, bookings, seller enrollment, outreach or spending.
- Source stays on GitHub. The prototype uses public GitHub Pages. The user excludes Sites hosting. Before production, choose a GitHub-connected commercial host that supports ecommerce. GitHub Pages prohibits ecommerce business hosting.
- Atomic Audo Copenhagen #11 is the provisional prototype direction, with Aesop #35 an alternative. Final design approval remains open.

## Current document map

| Topic | Entry point |
|---|---|
| Current strategy and brand onboarding | [Platform/brand brief](planning/10-Platform-First-Strategy-and-Brand-Brief.md) |
| People, meetings and commitment tracking | [Operating method](../TEAM/OPERATING-METHOD.md). Actual records are private/local-only |
| Mission, dates, scope and controlling decisions | [PROJECT-BASELINE.md](PROJECT-BASELINE.md) |
| Anonymous foundations and brainstorming | [PROJECT-FOUNDATIONS.md](PROJECT-FOUNDATIONS.md) |
| Website specification and prototype review | [website-spec/README.md](website-spec/README.md) |
| First ninety days and year one | [Roadmap](planning/03-Twelve-Month-Roadmap-and-First-90-Days.md) |
| Zero-commission website economics | [Website commerce](website-spec/05-COMMERCE-PRICING-AND-OPERATIONS.md) |
| Legacy festival financial illustration | [Financial plan](planning/02-Financial-Model-and-Targets.md), [model inputs](data/model-inputs.json) |
| Founder pay, profit sharing and hiring proposals | [Three compensation scenarios](planning/09-Founder-Compensation-and-Hiring-Scenarios.md), standalone commercial illustrations. No approved pay, ownership or hiring commitments |
| Festival history and missing sales evidence | [History](research/01-Taos-Fall-Arts-History-and-Economics.md) |
| International event comparisons and evidence | [Benchmarks](research/02-Global-Festival-Benchmarks.md), [source register](research/04-Source-Register-and-Open-Questions.md) |

## Scope and economics that must remain aligned

The first phases run Nov 1–30, Dec 1–30 and Dec 31–Jan 29. Cash-flow periods run November 2026–October 2027. The legacy model retains its monetary assumptions and is explicitly **not the current website budget or an approved consolidated forecast**. Keep the model’s 20% direct-festival fee separate from direct-artist website sales.

Website scope: Taos-only v1. Ten artist candidates and sixty work records. Twelve gallery businesses/groups. Ten experiences. Eight restaurant/eight lodging targets. Core artist/experience inclusion is free. Direct-artist platform commission is zero. Promising the full art subtotal requires funded processing. Founding profile proposals are $150/$99/$199 monthly. All 28 targets would yield $4,184/month or $25,104 for six paid months on average. No customer has agreed to that revenue. Begin with 12–20 cleared works if that matches actual capacity, then grow toward sixty.

Research has 31 published asking prices, 23 unconfirmed dimension units and 42 unknown art years among sixty work records. No seller has authorized checkout or image reuse. Six Miguel Martinez records have source conflicts. The image manifest contains 98 artwork and place records and 92 reference URLs. It grants no asset licenses. Use original or licensed prototype imagery without attributing fictional work to living artists.

## Fixed external dates from the October 19 research

- **October 23, 2026, 11:59pm Mountain:** New Mexico Arts FY28 advance review if required. The authorized applicant must verify account/history and eligibility. Final deadline **December 18** falls in days 31–60.
- **October 22:** Larry Bell/Michelle Cooke opening at Taos Center for the Arts, and the scheduled close of the Ron Cooper/Arnoldi/Dill exhibition in Santa Fe. Optional research opportunities.
- **October 31:** scheduled end of Michelle Cooke’s Santa Fe solo exhibition. Optional.
- An **October 24** Art as a Teacher launch remains an unverified lead, including its year.

Source links and verification context are in the baseline. Recheck before relying on any date. PASEO’s separately announced Sept 17–18, 2027 dates do not establish Fall Arts dates.

## Evidence and private records

The 2026 festival archive is outstanding. The reviewed sources provide no reliable annual series of aggregate art sales or unique attendance. Organization finances are not art GMV. HeyTaos remains a prospective partner. It has agreed to supply no audience or data. Institutional authority and the festival/website relationship still need confirmation.

Dated source caveats include ended Revolt shows, potentially sold newsletter works, seasonal operations at 192 at The Blake, an Ojo cold plunge described as under construction, and brochure rates that are not live quotes. Refresh sensitive details before production or an actual visit.

Original private planning records and raw sources remain ignored and unchanged. Use the private archive-intake workflow for new records. Publish only cleared aggregates or redacted material. No buyer data, private accounts, personal biographies or raw source archives belong in public Git.

## Prototype implementation and deployment

**Website:** https://suede0619.github.io/sw-arts-website/

**Source:** https://github.com/Suede0619/sw-arts-website

The buildless prototype contains six fictional demo artworks, ten artist research profiles with sixty source-only records, twelve galleries, ten experiences, eight restaurants and eight lodging candidates. Implemented flows include filtering/sorting, zoom/comparison, contextual simulated assistance with filter/undo, simulated viewing/checkout, Arroyo Seco travel origin, experience list/schematic, source-linked practical detail and local saved/shared/downloaded plans.

Original generated imagery and SVG are distinct from actual artist inventory and venues. The prototype connects no live model, payment, email or booking service. The source repository’s `ASSETS.md` records image provenance/prompts. `DEPLOYMENT.md` and `AGENTS.md` describe hosting, verification, rollback and continued work.

Initial publication checks matched source `353de133292bd443adb946a8bd3e6a299acf1f7b`, GitHub Actions run `39334506833` and deployment `7186341042` on October 19. The historical `prototype-v0.1.0` tag preserves that release. It is not the current anonymous publication. The checks below record publication of the October 21 anonymous revision. Existing Git history and tags are not rewritten.

## October 21 anonymous editorial revision

- Replaced the personally framed meeting account with the standalone [foundations and ideas](PROJECT-FOUNDATIONS.md) document. Removed participant biographies, conversation history and personal attribution.
- Replaced named role assignments, approvals and archive references with functional responsibilities. Generalized conflict rules across all affiliated businesses.
- Updated every affected cross-reference, source qualification and publication instruction, including tracked agent files, research CSV and prototype source.
- Removed names from the prototype footer, About page, preview dialog, concierge response and data narrative. Retained only the factual HOUSE of FIRE director association in the gallery listing.
- Project dates, historical numbers, budgets, fee proposals, catalog counts, source dates and production review gates are unchanged. Ignored private records remain intact.

### Verification and published anonymous version

| Check | Result |
|---|---|
| Website source pushed and deployed | `0971c4c9a612885d9e0e87ee40d024a81c922d76` on `main` |
| GitHub Actions | [Run 39634101165](https://github.com/Suede0619/sw-arts-website/actions/runs/39634101165), all nine browser tests and deployment succeeded |
| Pages deployment | `7231224646`, success at the website address above |
| Local editorial audit | 74 public text files and all tracked binary assets checked. Only the permitted HOUSE of FIRE business association remains in the gallery research and website listing |
| Rendered prototype audit | All 64 implemented routes checked, plus preview dialog, concierge response and phone About/footer. No other participant names or browser errors |
| Live verification | Served HTML, script and catalog match the pushed source. Public Home, About, footer, dialog, concierge and phone views are anonymous. Only the HOUSE of FIRE listing retains the permitted business association |
| Documents, data and boundaries | Relative links and whitespace checks pass. Financial model/outputs and catalog facts/counts unchanged. Original ignored planning archive checksum unchanged. No parent-workspace files edited |

The current public files are anonymous. Older commits and tags remain historical records. Continue using the publication standard for every future edit, including agent instructions and technical handoffs.

## Repository boundaries and next work

The October 21 [founder compensation brief](planning/09-Founder-Compensation-and-Hiring-Scenarios.md) adds three anonymous alternatives: a lean paid pilot ($1,500/month gross per founder), an underwritten operation ($4,000), and service-led growth ($6,000). It itemizes revenue/cost assumptions, operating cash buffers, downside cases, example residual-cash sharing and role-specific hiring gates. The scenarios propose monthly operating levels. They establish no demand forecast, salary commitment or ownership agreement. They preserve zero direct-artist platform commission and remain separate from the unchanged legacy model. The growth example fails its single-milestone loss test without extra resilience. A positive base-case budget is not hiring approval. Check arithmetic, relative links and anonymous public wording for this document. No website or private records need changing.

ART is the independent public `taosarts` document repository. The prototype is a second repository at `ART/ArtSouthwest/ArtSouthwest-website/`, ignored by ART. Do not add it as a submodule or embedded repository. Work only inside ART for this task. Do not stage parent-workspace files or private records.

Next: review the prototype, record design revisions, resolve content/seller permissions and processing funding, establish operating capacity, and choose compatible commercial hosting before production. Anonymous planning is not proof of agreements, appointments or board authority. Recheck current facts when their use requires it. Do not repeat the entire research package unnecessarily.
