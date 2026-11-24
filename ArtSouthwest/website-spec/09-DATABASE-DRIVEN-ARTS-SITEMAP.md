# Database-driven arts discovery and visit sitemap

The [MVP1 scope](10-MVP1-WEBSITE-SCOPE.md) gives the prototype two city catalogs and a central Taos planner. For the future calendar, link day-range exhibitions to timed occurrences and link a weekly roundup to those records and profiles. Assign a reviewer and correction flow before enabling venue-submitted images or recurring email.

**Status:** Information-architecture proposal for review. It uses the public European Cellars website as a reference for structured catalog navigation. It does not approve a new brand, regional expansion, live catalog, seller relationship, booking flow, or production build.

**Reference reviewed November 18, 2026:** [European Cellars Our Wines](https://www.europeancellars.com/our-wines/), [Producers](https://www.europeancellars.com/producers/), [Comando G producer profile](https://www.europeancellars.com/producer/comando-g/), [Jumilla wine detail](https://www.europeancellars.com/wine/monastrell/), and the site's [public sitemap index](https://www.europeancellars.com/sitemap.xml).

## Recommendation

Use European Cellars as a strong **information-architecture and catalog-model reference**. Build ArtSouthwest around connected, carefully maintained records for artworks, artists, galleries, places, experiences, events, and editorial collections. Let people browse across those records using useful filters and links.

Do not copy its branding, page text, imagery, layout, or code. Its business is a wine importer with producer portfolios, distributors, vintage records, ratings, and technical sheets. ArtSouthwest needs permission-aware art records, artist relationships, visit planning, and practical buyer service. Its distributor model does not fit our v1.

The reference works well because a catalog card identifies a wine, producer, region, and varieties; category shortcuts and filters help visitors narrow the catalog; producer pages connect their story, location, farming, portfolio, products, and downloads; and product details organize specific facts, process notes, ratings, and documents around one record. The public sitemap also exposes separate wine, producer, distributor, portfolio, employee, resource, and news content types. This suggests a structured publishing model, though the public pages do not reveal its full database design.

For ArtSouthwest, adapt those patterns to the artwork and its relationships. Keep Taos as the only v1 destination. Make other regions unavailable until editorial capacity and local relationships support them. Include Native and Indigenous artists only through accurate self-identification, community guidance, consent, and artist-controlled representation. Do not create one generic Indigenous style or infer identity from location or artwork.

## Proposed public sitemap

```text
/
├── Search
│   ├── Search all records
│   ├── Search results by type
│   └── Saved shortlist
├── Explore Taos
│   ├── Curated collections
│   ├── Places and neighborhoods
│   ├── Current events
│   └── Region guide
├── Art
│   ├── Browse all available and inquiry-only works
│   ├── Collections
│   │   ├── By medium or form
│   │   ├── By subject or theme
│   │   ├── By place, when verified
│   │   └── Editorial selections
│   └── Artwork detail
├── Artists
│   ├── Artist directory
│   ├── Artist profile
│   │   ├── Selected work
│   │   ├── Practice and materials
│   │   ├── Artist-approved biography
│   │   ├── Exhibitions and public events
│   │   └── Visit, contact, or purchase route
│   └── Artist participation information
├── Galleries
│   ├── Gallery directory
│   ├── Gallery profile
│   │   ├── Represented artists and works, with authorization
│   │   ├── Current exhibitions and events
│   │   ├── Hours, access, and visit information
│   │   └── Gallery contact or inquiry route
│   └── Gallery participation information
├── Visit
│   ├── Experiences
│   │   ├── Browse experiences
│   │   ├── Experience detail
│   │   └── Provider or host profile
│   ├── Guided tours
│   │   ├── Curated and hosted tours
│   │   ├── Tour detail and logistics
│   │   └── Request a custom guided visit
│   ├── Itinerary planning
│   │   ├── Build a saved visit plan
│   │   └── Request human assistance
│   ├── Places
│   │   └── Place detail
│   └── Practical information
│       ├── Travel between places
│       ├── Accessibility details
│       └── Seasonal and date-sensitive notices
├── Stories
│   ├── Artist and gallery features
│   ├── Place and art histories
│   ├── Learning resources
│   └── Editorial collections
├── About
│   ├── Purpose and editorial standards
│   ├── How the catalog works
│   ├── Image rights, attribution, and corrections
│   ├── Contact
│   └── Privacy and terms
└── Future regions
    └── Interest information only until a region passes its launch review
```

This tree describes a proposed information architecture, not approved production routes. The existing prototype may keep its simpler navigation during review.

## Global discovery behavior

The global search should find artworks, artists, galleries, experiences, places, events, and stories. Results should identify each record type and show why it matches. The interface should preserve the visitor's selected region and filters when they open a result and return.

Start with a small set of clear entry points: browse art, find an artist, plan a visit, and explore Taos or Santa Fe. Put shared search and the current region selector in persistent navigation. Show the active region. Do not expose future-region pages as populated destinations when the project has no maintained local catalog there.

Use searchable, controlled terms alongside plain-language text. Do not force art into mutually exclusive categories. A painting can have several media, subjects, techniques, and place relationships. Every filter needs an "All" or reset path, useful empty-state guidance, and a visible count only when the underlying query supports it.

## Catalog browse and detail templates

### Artwork collection

Each card should show an accurate image, title, artist, medium, dimensions with units, location context where approved, and a truthful status. State whether the record is available, inquiry-only, sold, or unconfirmed. Do not imply stock from a historical listing.

Useful initial filters include artist, medium, artwork form, subject, dimensions, price range when current and seller-confirmed, availability state, and gallery or direct seller. Add region and place filters after the underlying geography is reviewed. Use cultural or identity-related descriptors only when the artist or authorized source supplies them and the artist approves their use.

A collection page may group work by theme, medium, place, or editorial selection. Each collection must explain its inclusion basis. Do not sell ranking or editorial inclusion.

### Artwork detail

A work page should connect the artwork to its artist and authorized seller, then present:

- Full-view image and permitted details, with accurate color, crop, orientation, and attribution.
- Title, artist, date if verified, medium, dimensions and units, edition or originality status, and current availability.
- Price, currency, shipping, taxes, and other cost information only when confirmed by the seller.
- Artist and seller context, provenance or condition where relevant and verified.
- Clear inquiry or purchase next step, routed to the responsible seller.
- Related works, artist profile, gallery profile, and relevant visit options.

The prototype's inquiry and checkout simulations remain simulations. A catalog record alone does not authorize an offer, transaction, or payment.

### Artist profile

The profile should give an artist control over their name, pronouns if they choose to provide them, bio, practice descriptions, approved images, links, and visit conditions. Link to their records and authorized gallery representation. Keep self-description separate from editorial description. Include public studio access only when the artist explicitly authorizes it. Do not infer cultural identity, community, or territory.

### Gallery profile

A gallery record should show its verified location, public hours, access notes, contact route, current exhibitions, participating artists, and works the gallery is authorized to represent. Label paid services or sponsorship clearly. Editorial selection stays independent from paid placement.

## Visit and experience records

Treat experiences as designed services, not just directory entries. A future offer may be created by ArtSouthwest or delivered by an approved host. The page must identify who leads it, what the visitor will do, group size, duration, price or price status, schedule, meeting point, accessibility, cancellation terms, weather limits, and what the price includes. Keep this information current and seller-confirmed.

An itinerary can connect a gallery visit, artwork viewing, public event, meal, or other consented activity. Explain travel time and distance from a selected origin, and distinguish estimates from confirmed transit. Never reveal a private studio or restricted cultural location. Use an inquiry or human handoff until a real booking flow and partner authority exist.

## Core content records and relationships

Create canonical records with stable IDs. A visible page may combine related records but should not duplicate their editable facts.

- **Artwork:** artist, authorized seller, media, physical specifications, status, price record, shipping record, image assets, credits, rights, and source.
- **Artist:** approved identity and profile, practices, works, representation links, public locations if authorized, contact route, and profile permissions.
- **Gallery:** verified organization and public place details, artist relationships, exhibitions, represented inventory, and commercial disclosure.
- **Experience or tour:** host, itinerary, schedule, price, capacity, meeting location, accessibility, policies, and booking or inquiry authority.
- **Place:** public name, category, verified coordinates or address, region relationships, hours, access, and location privacy level.
- **Event:** organizer, venue, dates, ticket or registration details, status, and source.
- **Collection:** editorial purpose, selection criteria, included records, editor, and review date.
- **Story or learning resource:** author or source, subjects, related artists and places, permissions, citations, and last review.
- **Organization:** gallery, host, or cultural organization with explicit relationship status and permission scope.
- **Price, availability, and permission:** dated and attributable records. Do not treat a page edit date as proof that commercial terms remain current.

Records should support many-to-many links. One artist can work across several media and regions. One artwork can relate to an artist, a gallery, a collection, and a place. A gallery can represent multiple artists. An experience can connect several public places. One place can appear in multiple itineraries. Use separate seller, artist home, artwork origin, visit location, and shipping origin fields.

## Operating safeguards and release gates

Before publication, verify the artist and seller identity, the record-to-image match, rights and credit, current availability, price and shipping terms, and the visitor-facing action. Record who supplied each fact and when. Keep source files and private correspondence in the ignored local archive. Publish only approved excerpts and images.

For Indigenous art and cultural programming, let artists and relevant communities define the language and participation conditions. Obtain authority and consent for cultural knowledge, stories, locations, images, and visits. Do not make sacred knowledge searchable, map restricted places, or use culturally specific motifs as decoration. Provide a correction and takedown route.

This proposal does not authorize the user-facing brand, production development, new seller agreements, public image use, paid placement, live booking, or commercial hosting. Review the information architecture with artists, galleries, collectors, visitors, and Indigenous cultural advisors before production decisions.
