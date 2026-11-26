# ArtSouthwest website: specification and review boundary

The [artist intake service](https://github.com/Suede0619/asw_artist_webform) has an independent checkout at `../artist_webform/`. It supports Neon Postgres and private Object Storage and exposes an approved-only catalog feed. See the [ArtSouthwest handoff](../SESSION_STATE.md) for current deployment status. Keep intake data and configuration out of both public repositories.

Use the [MVP1 scope](10-MVP1-WEBSITE-SCOPE.md) for the Taos and Santa Fe catalog, first Taos itinerary and editorial preview priorities. Read the October history below in its original context.

**Current stage:** The project lead approved the prototype design and authorized building the production catalog. The website repository holds the existing preview and a separate build for the Taos and Santa Fe catalog. Use the release handoff for the current review, hosting and commerce gates. Project day one is November 1, 2026.

Use the approved prototype’s varied page layouts for the live catalog. Keep the header, footer and major sections in a shared 1600px maximum-width container. Render the first page of each catalog view on the server. Verify on a wide desktop and a narrow phone and confirm that the browser can display catalog content from the initial HTML.

## Website history and status

The early ArtSouthwest work proposed a Taos-first digital art and destination service, with research into artists, works, galleries, experiences, food and lodging. The October 24 website specification organized the work into review gates: specification, design review, prototype, prototype review, then production. The design prototype was built and published separately in `Suede0619/sw-arts-website`; GitHub Pages is a preview, not the final commercial host.

The earlier website proposal assumed zero commission on direct artist sales. That rule applies to the website, not Denver's separately costed event proposal. The October 25 buyer-led service pivot explores requests, curated briefs and seller-confirmed next steps. It is a proposal and has not changed the prototype, model, pricing or production authority.

No live checkout, seller account, booking flow, catalog partnership or commercial hosting decision is approved by this history. Follow the handoff for the latest runtime verification and open decisions.

Maintain the reviewed design while building the production website. Live payment and booking flows require seller terms and separate operational setup. Domain registration and spending require their own authority. Keep all public prose, role assignments, data and prototype copy anonymous under the publication standard in the parent AGENTS.md. The business association in the HOUSE of FIRE listing is the sole participant-name exception.

Use ArtSouthwest as the project name. The regional taxonomy remains a future expansion proposal. The Atomic design-system choice is a recommendation awaiting the user's decision.

Hosting requirement: keep prototype and final source in `https://github.com/Suede0619/sw-arts-website`, with the prototype on GitHub Pages at `https://suede0619.github.io/sw-arts-website/`. Do not deploy to Sites. Pages prohibits ecommerce business hosting. Resolve a compatible GitHub-connected commercial host before production. The prototype's documentation explains the constraint. Keep all secret keys and private operations out of static frontend files.

Read README.md and 01-WEBSITE-SPEC.md first. The content research supports sourcing and recruitment. The project has no approved catalog. Listing a candidate creates no artist, gallery, experience, restaurant or lodging partnership. Distinguish actual source facts from proposals, estimates, sold work, unknowns, and seller-confirmed available inventory.

Use the [database-driven arts sitemap](09-DATABASE-DRIVEN-ARTS-SITEMAP.md) as a proposal for connected catalog records and discovery. European Cellars is a useful information-architecture reference for faceted catalogs, producer profiles, and detail pages. Do not copy its words, images, design assets, or code. Keep the current brand and design decisions open, and preserve Taos-only v1 scope. Evaluate artist/community-guided Indigenous arts coverage with consent and self-identification. Tours created and guided by the project are a service direction to evaluate, not an approved offer or booking integration.

The [current artist intake brief](12-ARTIST-INVITATION-AND-INTAKE.md) sets **20% commission on completed artwork sales through the platform**. Record the disclosure in intake and agree seller terms, fees and payouts before checkout. The festival model is separate.

The public repository may contain concise original research, source/image-reference URLs, factual metadata, schemas, and clearly marked demonstration fields. Raw fetched pages stay in ignored `ART/ArtSouthwest/private/source/website-spec/`. Source visibility is not a commercial image/text license. Obtain permission before publishing third-party artwork, photography, or substantial copied text in a prototype or production catalog. Do not bypass social-media login, CAPTCHA, or other access controls.

Maintain an impeccable user experience: meaningful art images, clear information, deterministic filters, useful contextual AI assistance, accurate inventory, honest full-cost quotes, and a reliable human handoff. AI must not invent art, prices, hours, availability, cultural identity, or completed transactions. This file does not authorize real outreach, booking, applications, or spending.
