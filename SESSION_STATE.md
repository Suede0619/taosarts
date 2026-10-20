# Session handoff — October 19, 2026

Read [AGENTS.md](AGENTS.md) and [PROJECT-BASELINE.md](PROJECT-BASELINE.md) first. Check the current date, Git history and newest user instruction before treating an old source snapshot as current.

## Latest instructions and stage

- The user is **Dave Paul**, also **David Paul**. Use Dave Paul in documents and Dave in conversation. Canonical ART references have been corrected. Immutable private originals and Git history are not rewritten.
- **November 1, 2026 is day one**; year one ends October 31, 2027. Dave already lives in Arroyo Seco. Historical/research dates remain October 19 where that was the actual observation.
- Finish alignment first, then **build and publish a design prototype**, in a new folder and separate repository: `https://github.com/Suede0619/sw-arts-website`. This supersedes the earlier wait-before-prototype instruction. Production remains a separate review; no real purchases, booking or seller enrollment are authorized by a prototype.
- Dave explicitly requires GitHub for prototype/final source and requested GitHub hosting; he rejected the proposed Sites address. The design prototype is now **public on GitHub Pages**, with no sign-in. GitHub Pages prohibits running an ecommerce business, so a compatible GitHub-connected commercial host must be resolved before production; do not silently select or publish to another provider.
- Atomic Audo Copenhagen #11 is the provisional prototype direction, with Aesop #35 an alternative. A concrete prototype does not finalize the brand/design decision.

## Completed baseline before this alignment

The initial 31-file festival/history/business package was pushed in **f74b047**; agent/handoff guidance in **f0a4f43**; the twenty-file website specification/research package in **e987f7f**. Read only the relevant modules instead of repeating all research.

| Topic | Current entry point |
|---|---|
| Common identity, timeline, fixed dates and controlling website decisions | [PROJECT-BASELINE.md](PROJECT-BASELINE.md) |
| Consolidated meeting | [FelixMeet](FelixMeet), extensionless canonical document |
| Website specification | [website-spec/README.md](website-spec/README.md) |
| Dated first ninety days and year one | [Roadmap](planning/03-Twelve-Month-Roadmap-and-First-90-Days.md) |
| Zero-commission website economics | [Website commerce](website-spec/05-COMMERCE-PRICING-AND-OPERATIONS.md) |
| Older commission-bearing financial illustration | [Financial plan](planning/02-Financial-Model-and-Targets.md), [model inputs](data/model-inputs.json) |
| Festival history / missing historical sales evidence | [History](research/01-Taos-Fall-Arts-History-and-Economics.md) |
| Global benchmarks / original source register | [Benchmarks](research/02-Global-Festival-Benchmarks.md), [sources](research/04-Source-Register-and-Open-Questions.md) |

## What alignment changes

The roadmap uses Nov 1–30, Dec 1–30, and Dec 31–Jan 29 for its first 30/60/90-day phases. Calendar cash flow runs November 2026–October 2027. The older model's monetary assumptions are retained and explicitly labeled **not the current website budget or an approved consolidated forecast**. Its 20% direct-festival illustration cannot be applied to direct-artist Southwest Art website sales.

The newer website rules control: Taos-only v1; ten artist candidates and sixty work records; twelve gallery businesses/groups; ten experiences; eight restaurant/eight lodging targets; free core artist/experience inclusion; zero direct-artist platform commission; funded processing if promising the full art subtotal; founding profile proposals $150/$99/$199 monthly. The old 100-work pilot target is superseded; start with a manageable 12–20 cleared works and grow only if ready. Full cohort profile income is $4,184/month or $25,104 for six paid months on average; none is agreed revenue.

Website research has 31 published asking prices, 23 unconfirmed dimension units and 42 unknown art years among sixty work records. All research work records remain disabled for checkout, without obtained seller authority or cleared image rights. Six Miguel Martinez records have source conflicts. The 98-row artwork/place image manifest contains 92 reference URLs, not licensed assets. Production/prototype imagery must be original or suitably licensed and must not misattribute demo art to living artists.

## Fixed dates before kickoff

- **October 23, 2026, 11:59pm Mountain:** New Mexico Arts FY28 advance review if required. Authorized existing applicant must verify account/history; this is not a website grant entitlement. Final deadline **December 18** is in days 31–60.
- **October 22:** Larry Bell/Michelle Cooke opening at Taos Center for the Arts; optional local research, not a project deadline. Ron Cooper/Arnoldi/Dill show in Santa Fe is scheduled to close that day.
- **October 31:** Michelle Cooke's Santa Fe solo exhibition scheduled to end; optional.
- Meeting reference to an **October 24** Art as a Teacher launch remains unverified, including year. Do not treat it as confirmed.

Official links and verification context are in the baseline. PASEO announces Sept 17–18, 2027 but is separate from Fall Arts, whose 2027 dates remain unconfirmed.

## Preserve these evidence and operating limits

Felix Kay is Gallery Director at HOUSE of FIRE; his precise festival role/year/authority remains unconfirmed. His 2026 archive has not arrived. HeyTaos is the corrected identity behind TellUs and a potential complementary partner, not an agreed audience/data supplier. No historic annual total-art-sales/unique-attendance series was established; organization finances are not art GMV.

Revolt's visible summer shows have ended; source newsletters can include now-sold Gonske work; 192 at The Blake may be seasonally closed; Ojo's new cold plunge source says under construction; static inn rates are not live quotes. Refresh all date-sensitive facts before a real visit or production listing.

The original private meeting archive remains unchanged at `private/source/FelixMeet.original-2026-10-19.txt`, SHA-256 `8a0598a5dfaca65b80e27b7a70b99b3da727831c2a1cf7ffc7aece50204b7d9b`. Private raw sources and buyer/financial records stay outside public Git.

## Completed prototype and verified publication

**Live design prototype:** https://suede0619.github.io/sw-arts-website/

**Source repository:** https://github.com/Suede0619/sw-arts-website

| Publication evidence | Result |
|---|---|
| Published source | `353de133292bd443adb946a8bd3e6a299acf1f7b` on `main` |
| Preserved review build | Annotated tag `prototype-v0.1.0`, points to the same source commit |
| GitHub Actions | [Run 39334506833](https://github.com/Suede0619/sw-arts-website/actions/runs/39334506833), validation and deployment succeeded |
| GitHub Pages deployment | `7186341042`, `github-pages` environment; HTTPS enabled |
| Public browser verification | HTTP 200; all home images decoded; catalog/section counts correct; shared links preserve the project path; mobile menu/concierge usable; no browser errors; served HTML/script/styles/catalog/hero hashes match the pushed source |
| Automated browser checks | Nine passed locally and in GitHub Actions, under `/sw-arts-website/` |

The buildless prototype in local `ART/sw-arts-website/` has original ivory/clay/juniper visual design; six fictional demo artworks with original generated images/SVG; ten real artist research profiles with sixty source-only work records; twelve gallery, ten experience, eight restaurant and eight lodging candidates. It implements artwork filtering/sorting/zoom/comparison, contextual simulated concierge with filter/undo, clearly simulated checkout/viewing, Arroyo Seco travel origin, experience list/schematic, source-linked practical details and saved/shared/downloaded plans. Image provenance and exact generation prompts are in the website repo's `ASSETS.md`; deployment/rollback and future-session guidance are in `DEPLOYMENT.md` and `AGENTS.md`.

No real artist/venue participation, cleared sale inventory, booking availability or real money/model integrations are implied. The prototype uses original illustrations rather than uncleared named artists' images; AI/checkout/request simulations are labeled throughout. Real viewing requests are not sent. Private source images and test artifacts are ignored. No secrets, buyer records or private meeting originals were published.

The rejected Sites registration `appgprj_6ad65ca64d54819198c8b45f3a72e475` has **zero saved versions and no live/preview URL**, verified before GitHub deployment. Its source operation failed before committing/pushing. No delete operation was available; it remains unused/unpublished. The prototype's Sites manifest was removed. Do not deploy there. The [technical spec](website-spec/06-DATA-TECHNICAL-AND-CONTENT-SPEC.md) records the official Pages ecommerce restriction, while preserving GitHub as the final source repository.

## Repository boundaries and continuation

ART is the public **taosarts** document repository. The prototype has its own **sw-arts-website** repository and is ignored by ART; do not add it as an embedded repository/submodule. The surrounding TAOS repository has unrelated staged housing work; preserve it. Commit and push only each repository's intended files.

Alignment was completed and pushed in **7f2c6db** before prototype implementation. Parent identity guidance was pushed separately in **40cd4d3**. Validation passed for canonical names, relative links, contiguous Nov–Oct cash-flow periods, exact first-ninety-day dates, unchanged model monetary results, and the preserved private-archive checksum. The model generator passed its allocation/timing/cash checks. Website source and its review tag are pushed; the live Pages result is recorded above. This handoff update reconciles the specification's older “not built” language with the actual prototype. Further production work waits for Dave/Felix's prototype review, design decision, permissions/funding, and compatible commercial hosting choice. Unrelated parent staging remains unchanged.
