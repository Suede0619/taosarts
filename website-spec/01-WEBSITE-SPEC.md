# Southwest Art: website specification for review

**Current stage:** The user authorized a design prototype and live preview in the separate `sw-arts-website` repository. The provisional Audo #11 direction is for review. Production and live transactions still require a later approval. Project day one is November 1, 2026. The earlier sections document the specification review sequence. They do not revoke prototype authority.
**Version 0.1, October 19, 2026, Anonymous planning specification. Product and curatorial review pending**

**Stage: design prototype implemented. Review precedes production.** Source is in [sw-arts-website](https://github.com/Suede0619/sw-arts-website). The preview uses [GitHub Pages](https://suede0619.github.io/sw-arts-website/) with actual publication status in [SESSION_STATE.md](../SESSION_STATE.md). The working brand, Atomic design direction, pricing, partner targets, inventory, and production technical choices remain proposals. The prototype processes no live commerce. GitHub is the required source repository for both builds. The [technical specification](06-DATA-TECHNICAL-AND-CONTENT-SPEC.md) records the Pages ecommerce restriction and unresolved commercial hosting choice.

Use **Southwest Art** as requested for this stage. An established [Southwest Art Magazine](https://www.southwestart.com/) already uses the name in this market. Review the public identity/domain and possible confusion before launch. The project has no name clearance.

## 1. The purpose and the promise

Help artists sell enough art to keep living and working in Taos. Make the region credible and compelling to collectors, advisors, designers, institutions, and first buyers from elsewhere in the world. A beautiful website must lead to real confidence, meaningful visits, completed purchases, safe delivery, and paid artists.

**The visitor promise:** discover exceptional art, understand its history, materials and context, know what is available, and get thoughtful help buying it or planning a worthwhile visit. The experience should be as careful as a respected gallery and as welcoming as a good host.

**Artist terms:** core artist consideration is free. Southwest Art charges no commission on direct-artist sales. Artist permission, representation agreements, and a funded payment-cost policy must make that promise true in practice.

The site must be worth using even when a person never travels. Remote viewings, excellent object records, truthful scale and color presentation, a short useful selection, and a complete delivery service are core offers. Travel adds direct encounters with artists, meaningful places, and hospitality. It does not compensate for a weak online buying experience.

## 2. Product decisions proposed for v1

| Decision | Recommendation | Why it serves the mission |
|---|---|---|
| Organizing principle | Region first, with **Taos** as the only published v1 region | Makes discovery legible without a thin regional directory. |
| Primary navigation | Art & Artists, Galleries, Experiences, Eat & Stay, Plan a Visit | Keeps art buying first while offering a complete visit. |
| Art commerce | Artist-direct works with zero Southwest Art commission. Gallery-represented work follows its authorized seller's arrangement | Preserves artist income and avoids undermining galleries. |
| AI | One Southwest Art concierge with page-specific modes and a shared user-controlled plan | Gives every section help without several competing chatbots. |
| Editorial selection | Independently selected. Paid partners clearly identified | Credibility requires visible independence. |
| Design foundation | Recommend Atomic **Audo Copenhagen #11**, adapted. Approval pending | Strong photography, warmth, restrained typography, practical product presentation. |
| Experience income | Free editorial curation. Approved affiliate/referral bookings first | Revenue can follow useful bookings without charging public places for inclusion. |
| Gallery/hospitality income | Optional paid partner profiles with concrete services and reporting | Funds art discovery while keeping core artist participation free. |
| Launch content | Ten selected artist candidates, six cleared works each, ten experiences, twelve gallery targets, eight restaurant and eight lodging targets | A coherent editorial launch. Each target still needs consent and current verification. |
| Technology sequence | Simulated interactions in prototype. Real inventory, payments and booking only after design approval and readiness checks | Allows visual decisions before irreversible integrations. |

These choices replace relevant website assumptions in the earlier broad business plan. They do not automatically alter festival governance, contracts, or its separate financial model.

## 3. Who we serve and how we establish legitimacy

### Collector and advisor

Needs a credible artist context, relevant current work, exact specifications, condition/provenance where relevant, representation, an informed contact, clear costs, and dependable delivery. A reputation claim must have a supporting source. Museum references document an artist’s history. They establish no museum endorsement of Southwest Art.

### Curious visitor and first buyer

Needs a welcoming entry, prices that can be understood, a few good choices, basic explanations without condescension, and an easy next step. Do not make a person disclose wealth or artistic expertise before helping. Expensive work can coexist with accessible original prints and modest purchases, correctly labeled.

### Artist and gallery

Needs control of work and story, accurate availability, appropriate image rights, respectful representation, qualified inquiries, straightforward selling, and clear settlement. A gallery's collector list is not ours to ingest. Resolve representation conflicts before offering an item for sale.

### Traveler

Needs a reason to come, a realistic way to get here, confirmed viewing opportunities, a sensible itinerary, useful experiences, and places to eat and stay. If there is no verified availability for a date or offer, the site says so.

### Resident and public participant

Needs access, belonging, cultural specificity, free choices, and transparency about commercial arrangements. The region is a living community. A guide should not turn homes, sacred places, or quiet villages into unconsented attractions.

### Trust is a service standard

Publish editorial responsibility, selection criteria, paid-service terms, buyer support, purchase follow-through and correction procedures. Use approved biographies and real editorial bylines. Avoid invented rankings, unsupported “museum quality” claims, generic luxury language, badges without evidence, manufactured reviews, and unapproved institutional logos.

## 4. Region architecture and navigation

The regional proposal is in [02-REGIONS-AND-TAOS-SCOPE.md](02-REGIONS-AND-TAOS-SCOPE.md). The regions group destinations around practical art visits. Places have a primary region and optional cross-region tags, while sovereign communities retain their own names and authority.

V1 defaults to Taos. A region switcher can explain the larger vision but should not lead to empty city pages. Future regions remain unpublished, with an optional quiet interest-registration link. A user sees the region persist through art, experiences, lodging, and their saved plan.

Proposed routes:

```text
/                         Southwest Art introduction; Taos is the live destination
/regions/taos             Taos editorial and collecting gateway
/regions/taos/art          Available work and artists; linked tabs
/artists/{slug}           Artist profile and cleared works
/art/{slug}               Work detail, availability and buying path
/regions/taos/galleries    Edited gallery directory
/galleries/{slug}         Partner/approved editorial profile
/regions/taos/experiences  Ten edited experiences, list and optional map
/experiences/{slug}       Full practical detail and an honest booking route
/regions/taos/eat          Selected restaurant profiles
/regions/taos/stay         Selected lodging profiles
/plan                     Saved work, viewings and visit plan
/journal/{slug}           Edited context that leads somewhere useful
/how-to-buy               Purchase, delivery, representation, returns and support
/about                    People, mission, selection, partners, corrections
```

These route names define the specification. Check prototype documentation for implemented routes. Event/festival content is date-scoped within Taos. The site does not invent a confirmed 2027 festival date.

## 5. Shared page structure and behavior

Every major section has a clear title, a short editorial premise, useful visual content, relevant controls, a contextual AI question area, and a visible human-help route. The art or experience comes first. Assistance remains easy to find.

**Desktop:** a restrained header, twelve-column layout, readable content width, clear image rhythm, and optional contextual side panel. **Mobile:** one-handed controls, useful first-screen content, full-width art where appropriate, and an accessible assistant sheet that does not cover the purchase or booking action. No compulsory account to browse, ask a basic question, or request a viewing.

Shared controls: region/location, selected filters with counts, result count, sort, clear/undo, save, share, and list/map where relevant. Retain filters through back navigation and support shareable URLs without personal preferences. The system announces changes for assistive technology. Never use color alone to communicate status.

One person can collect works and experiences into **Your Taos plan**. Start locally/anonymous. Offer an account or email link when it helps preserve a shortlist. Ask consent separately for service communication and marketing.

## 6. Home and Taos gateway

**First screen:** brand, live region, a single excellent licensed artwork or paired artwork/place composition, a concise reason to explore, with **Explore art** and **Plan a Taos visit** as the two main actions. The main promise should be comprehensible within five seconds. Candidate copy for review: “Art worth knowing. A place worth discovering.”

The next sequence is an edited selection of available work, the people behind it, a short explanation of Taos's artistic breadth, a few strong experiences, and help planning a visit. Describe specific artists, practices and institutions that justify a visit.

A “Why collect here?” section links to individual artist evidence and the buying service. A “Start with your interests” prompt can create a brief or apply visible filters. First-time collectors can choose approachable price bands without affecting how respectfully the site treats them.

Journal material is selective and useful: one artist's process, an informed collecting introduction, a thoughtful contemporary/historical connection, or a verified itinerary. Do not fill the site with generic AI destination articles.

## 7. Art and artists: free core participation

### Collection page

Use a clean, image-led grid. Default to a selected set of current, rights-cleared work. Keep price and seller commercial terms out of editorial ranking. Users can switch between **Works** and **Artists** without losing region or relevant filters.

Filters: artist, title/keyword, medium, original/unique/edition/reproduction, price, width/height/depth with units, orientation, year where known, subject, primary color palette, availability, seller/location, framing, and ready-to-ship versus commission. Optional filters should not overwhelm the first view. Expose the most useful five first, with the rest in a clearly named filter panel.

Sort: curator's selection, recently added, artwork year newest first, price ascending/descending, artist, and title. “Recently added” is not the work's creation year. Color search is an approximate visual aid. It must never imply authorship, identity, or cultural classification.

Work cards show the whole work inside a consistent neutral stage, without cropping the object. Beneath: artist, title, medium/year, dimensions, price or “Price on request,” and a truthful status. Saved works have an obvious state. Hover is optional, never the only way to see essential information.

### Artist profile

A licensed portrait or studio image, approved biography, artistic practice, verified Taos connection, selected institutional/exhibition references, current authorized seller(s), six cleared work records, optional process film, and ways to ask a question or request a viewing. Show the person's actual voice through approved quotations or interview material. Do not invent an artist statement.

The ten candidates form a recruitment list. The review establishes no fame ranking. The research separates international institutional recognition, regional market history, current activity and online inventory availability. Historical artists can inform editorial context. Estate and resale purchases do not pay a living artist directly.

The proposed cohort is Larry Bell, Ron Cooper, Kevin Macpherson, Walt Gonske, Thom (Tex) Wheeler, Miguel Martinez, Ed Sandoval, Angie Coleman, Jonathan Warm Day Coming and Sherrie McGraw. [Artist/work research](research/01-TAOS-ARTISTS-AND-WORKS.md) supplies six sourced candidates each. Of sixty records, thirty-one have published asking prices. None has our seller authority or cleared image rights. Six Miguel records contain source conflicts. Public pages do not establish several artists’ newest or highest-priced available work. Obtain actual priority inventory from each seller before a live offer.

### Work detail: the most important commercial page

On desktop, image and purchase information sit together. Mobile begins with the work, then immediately its essential facts and next action. Full-screen zoom, detail photographs, frame/back/condition images where appropriate, and accurately scaled room context are available without cluttering the initial image.

Required fields: artist, title, year or “not supplied,” medium, actual and framed dimensions with units, unique/edition/reproduction status, edition details, price/currency, seller and representation, availability check, signature/authenticity information where applicable, condition, shipping origin, delivery options/quote, returns/cancellation terms, image credits and rights. Do not imply that a beautiful image provides provenance.

Three honest actions:

- **Buy this work:** only when seller onboarding, signed authority, current inventory, price, tax/delivery treatment and terms are ready.
- **Request a viewing / quote:** valuable work, custom delivery, or work with an inquiry price.
- **Ask about availability:** unresolved status. This cannot look like an available item that merely needs payment.

The AI can explain, compare, help measure a space, suggest verified alternatives, and arrange a human handoff. It cannot authenticate, appraise, promise appreciation, negotiate unauthorized discounts, or perform an unconfirmed purchase.

## 8. Experiences: ten edited reasons to explore

This section excludes dining and lodging. The recommended mix includes living heritage, art institutions, architecture, a gorge walk, mountain hiking, rafting, skiing, and mineral soaking. Specific recommendations and source evidence are in [the experience research](research/02-TAOS-EXPERIENCES.md).

Cards expose type, duration, price basis, distance/travel estimate from a selected origin, time of day, season, booking requirement, physical demands, access limitations, and provider. Use icons only when understandable with text. A map complements a readable list. It is not the only interface.

Filters: type, date/season, morning/afternoon/evening, time available, free/paid and budget, travel time, exertion, accessibility, private/group, family suitability where published, indoor/outdoor and booking availability. “Near me” requires location permission. Default to Taos Plaza with an obvious origin switch to Arroyo Seco.

Details explain the activity, inclusions, preparation, cancellation and weather terms, meeting point, cultural and photography rules, and booking route. Distances and durations are estimates unless measured by a routing source. Recheck routes and seasonal conditions.

Do not charge admission for a public trail or imply an affiliate agreement with a Pueblo or museum. Free and noncommissionable experiences belong in the guide. Commissionable commercial bookings use an approved affiliate route or explicit provider contract. Tell travelers who fulfills the service and whether the platform earns a referral fee.

The concierge can compose a half-day, compare two experiences, account for travel and opening hours, and suggest an indoor alternative. It does not invent today's trail conditions, weather, availability, or cultural access.

## 9. Galleries: paid profiles with independent selection

Select twelve candidate galleries for the strength of their program, artist relationships, object information, collector service, international/regional relevance, and presentation. Assess quality, seller practice and work context alongside price. [The gallery research](research/03-TAOS-GALLERIES.md) explains each proposed target and what was actually found.

A profile contains approved editorial introduction, curatorial focus, represented artists versus estate/resale inventory, real location, verified hours/appointment policy, current and upcoming shows with start/end dates, selected cleared available works, practical visiting information, contact, and a human appointment request. Images and catalog material require permission. A static heading saying “current show” does not override a past end date.

Label paid participation **Partner profile**. Editorial selection and placement cannot be bought secretly. Unpaid factual references may remain where needed for a trustworthy itinerary or artist representation. A paid plan buys defined services and an enhanced profile. It grants no control over competing businesses’ inclusion.

The assistant answers from this gallery's approved records, compares distinct programs without favoritism based on fees, and helps request a viewing. It distinguishes “represented artist” from “work available on resale.” It never assumes every historical work routes money to the artist.

## 10. Food and lodging: paid partners, a better complete visit

These are separate discovery tabs under Eat & Stay. [The hospitality research](research/04-TAOS-FOOD-AND-LODGING.md) identifies eight restaurant and eight lodging recruitment targets. None is already a paid partner.

### Dining

Cards show cuisine, neighborhood, price basis, service period, reservation route, practical dietary information where confirmed, and a meaningful image. Details include approved copy, current menu link/date, a few factual menu examples, payment methods, verified hours and contact, access, and whether walk-ins are appropriate. Menus change. Avoid treating an old PDF as a live promise. Restaurant bookings go through the actual provider's permitted reservation route initially.

### Lodging

Cards show location, lodging type, room styles, distinguishing amenities, access notes, and either a verified date-specific rate or **Check rates for your dates**. Do not publish invented nightly prices. A quote needs dates, nights, guests, room type, currency, taxes/fees, cancellation, and the retrieval time.

A property page includes a small approved room-type table, a few excellent images, practical location/travel context, amenities and limitations, direct booking contact, and art-related context that is actually true. The AI matches a brief to confirmed property attributes. It cannot promise a room or quote inventory that the provider has not supplied.

Proposed founding prices: **galleries $150/month, restaurants $99/month, lodging $199/month**, subject to review and real willingness-to-pay testing. Pricing and first-year economics are in [the commerce plan](05-COMMERCE-PRICING-AND-OPERATIONS.md). Do not bill recruitment targets or imply an established audience.

## 11. AI assistance in every section

One discreet **Ask Southwest Art** interface appears on every major section and detail page. Its contextual title changes: “Find art for your space,” “Ask about this work,” “Plan an experience,” “Find a gallery,” or “Choose where to stay.” A person can always use ordinary filters and navigation without chatting.

The assistant proposes changes in plain language and applies the same structured filters the visible UI uses. Example: “Show available abstract works under $8,000, at least 24 inches wide.” It returns matching real records, displays the filter chips and result count, explains uncertainty, and offers undo. With multiple plausible meanings, it asks a concise follow-up.

The conversation can build a useful saved brief or itinerary with permission, carry chosen works between sections, prepare questions for the seller, and request human help. It does not become several inconsistent agents with separate memories. Detailed modes, tools, provider comparison, costs and evaluation are in [04-AI-CONCIERGE-AND-PLATFORM.md](04-AI-CONCIERGE-AND-PLATFORM.md).

## 12. Commerce and fulfillment requirements

The prototype has explicit **demonstration payment states**, with no live checkout and no implication that scraped inventory is ours to sell. Production requires artist/seller authority, rights, onboarding, payment accounts, tax responsibility, inventory locks, order state, refunds, delivery, insurance, and settlement.

The direct-artist service takes **zero Southwest Art commission**. Literal full-art-price payout also requires someone to fund processor costs. The recommended mission policy is platform/sponsor-funded fees when the budget and Stripe flow support it. Promise full artist receipt only after funding and implementing the fee policy. Gallery sales follow their separate disclosed seller agreements. [Commerce specification](05-COMMERCE-PRICING-AND-OPERATIONS.md).

Start with single-seller checkout per order. Do not add a multi-artist cart that creates misleading one-payment promises or complicated settlement before the basic service works. Expensive or complex international orders can use an informed quote/assisted purchase path. Payment alone is not delivery. The public sales metric requires qualifying completed orders.

## 13. Image and interaction quality are release gates

License art images and preserve color, orientation, detail and the complete work. A high-resolution master is not an excuse to make mobile users download it. Use generated responsive derivatives, progressive enhancement, carefully sized first-screen media and on-demand zoom. Never use generated or altered images as if they document an actual work or room.

Accessibility target: WCAG 2.2 AA. Practical targets: visible focus, keyboard-complete filtering and purchasing, accessible dialogs, clear labels, no hover-only essential content, text alternatives, reduced-motion support, readable type, and proper contrast. Mobile performance targets after representative testing: LCP ≤2.5 seconds, INP ≤200ms, CLS ≤0.1 at the 75th percentile. Test these acceptance targets during design review. The specification reports no measured results.

No forced cinematic intro, scroll hijacking, hidden prices, auto-opening chat, autoplay music, deceptive urgency, unskippable animation, tiny pale text, or enormous map blocking art. The distinction should come from art, editing, imagery and reliability.

## 14. Content operations and freshness

Use an editorial workflow: discovered then source-checked then rights/authority requested then approved then published then needs reconfirmation then withdrawn/archived. Record source, last check, person responsible, permission and expiration. Review work availability at least weekly and again at purchase. Partner inventory feeds should update much more frequently. High-value work needs an explicit confirmation/hold before payment.

Events automatically stop appearing as current after the end date. Menus, hours, rates, booking links, source URLs and accessibility details have owners and recheck schedules. Imported content does not auto-publish. A correction request has an accountable person and a response target of one business day.

Image permission is separate from permission to sell a work. Use public posts as research leads. Confirm title, price, availability and reuse rights separately. The research bypasses no social login or access control.

## 15. Measurement and commercial goals

Measure **completed art value and artist payments**, including how the proceeds distribute across artists. The earlier $3m ambition needs experiments and buyer evidence. It supplies no website conversion forecast.

Measure discovery then saved relevant work then qualified inquiry then viewing then quote then purchase then delivery then artist settlement. Compare local/remote and channels. Also track response time, inventory accuracy, quote time, abandoned purchase causes, image defects, access issues, repeat buyers and partner retention. Recognize experience income only after verifying an eligible completed booking under the actual program terms.

Proposed initial website pilot measures: ten onboarded artist/seller relationships, sixty cleared records or a smaller honestly stated launch, 98% spot-audited availability accuracy, a one-business-day human response, and five successfully fulfilled pilot purchases. Learn from actual behavior before expanding a large catalog or advertising budget. Do not fabricate launch traffic or collector numbers to sell partner fees.

## 16. Research and prototype review

Conduct moderated sessions with collectors/advisors, first buyers, artists/galleries, and local travelers/residents. A small initial study could include five collector/advisor participants, five first buyers, four artists/gallery staff, and four travelers/residents. The project has not yet conducted this proposed recruitment research.

Ask participants to find work within real constraints, distinguish originals from reproductions, compare scale and price, use assistant filters and undo, and request a viewing. Check whether they understand the seller and total cost. Test experience limits, demo lodging rates and the simulated purchase on a phone.

Record task success, time, confusion, trust and observed failures alongside design preferences. Significant confusion about availability, rights, actual purchase, cost, artist payout, paid placement or AI confidence is a blocker regardless of visual polish.

## 17. Three gates, with separate approval

Use the [technical/content requirements](06-DATA-TECHNICAL-AND-CONTENT-SPEC.md), [prototype review brief](07-PROTOTYPE-AND-REVIEW-PLAN.md), and [collector growth plan](08-COLLECTOR-GROWTH-AND-LAUNCH.md) as the supporting delivery modules.

**Gate A. This specification:** Product and curatorial reviewers assess the proposition, Atomic direction, navigation, content shortlist, artist economics, partner pricing and prototype scope. Resolve the design choice explicitly. No implementation begins before authorization.

**Gate B. Design prototype:** after approval, build a small coherent UI with clearly marked demonstration data and licensed imagery or appropriate placeholders. Include the Taos gateway, art search, artist/work detail, experience, gallery, dining/lodging, contextual assistant, saved plan and simulated checkout. Review desktop/mobile behavior and design, then revise.

**Gate C. Production:** only after prototype review and explicit authorization. Complete rights, inventory, partner agreements, payments, fulfillment, content/admin workflows, security, accessibility, analytics and performance validation. Prototype approval grants no live financial-integration authority.

## 18. Decisions requested in review

1. Atomic Audo Copenhagen #11 adaptation versus Aesop #35 or another named system.
2. Taos-first scope and future region taxonomy.
3. The artist cohort and mix of originals, original prints, editions and reproductions.
4. The literal 100%-art-price payout policy and who funds processing costs.
5. Gallery, experience and hospitality target lists and proposed founding prices.
6. AI recommendation and the boundary between automated assistance and human service.
7. Which prototype pages are essential and what imagery we have permission to use.
8. Available operating capacity and an agreed prototype budget/time envelope.

The spec is deliberately reviewable before those decisions. It is not a request to approve unseen future code or a claim that public-source content is ready for live commerce.
