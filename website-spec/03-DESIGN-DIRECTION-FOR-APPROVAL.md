# Design direction: recommendation awaiting approval

**Decision status: provisional Audo #11 prototype authorized. Final design choice remains open.** The user requires review before final selection. This document proposes a direction. It does not finalize it or authorize a prototype.

## The actual Atomic options reviewed

The supplied [Design System Atlas](http://atomic.nrvana.com/) contains forty distilled reference systems. The research archive contains the October 19, 2026 public `data.js` and application source, including names, numbered entries, tokens and hash navigation. The Atlas author interprets the brands. The page grants no original-brand component license and establishes no award claim.

| Option | Atlas link | Fit for Southwest Art | Decision |
|---|---|---|---|
| **Audo Copenhagen, #11** | [Preview #11](http://atomic.nrvana.com/#11) | Warm light surfaces, architectural/large photography, restrained serif headings and square, quiet commerce components | **Recommended base** |
| **Aesop, #35** | [Preview #35](http://atomic.nrvana.com/#35) | Excellent literary/editorial restraint and natural tones. Potentially more text-led than the art-first commerce objective | Alternative to review |
| Rivian, #32 | [Preview #32](http://atomic.nrvana.com/#32) | Strong landscape and practical specification language, but its adventure/automotive emphasis is less suited to the primary art proposition | Contextual reference. The recommendation uses another base |

The web reader could not fetch the HTTPS site. A local read retrieved the public source after a certificate-verification problem. The research bypassed no account or access control. Source snapshots are private research files. A future production site must use valid HTTPS. This access issue has no bearing on the visual recommendation.

## Recommended Audo design and readability changes

Borrow the warmth, image confidence, typography rhythm and restraint. Build original Southwest Art components and content. Do not copy Audo's logos, photographs, brand assets, or assume a font license. Confirm the Atlas kit's actual reuse terms before importing code. The reference supplies design ideas. Accessible commerce requires further implementation.

Proposed adaptations:

- Make whole artworks the visual center. Use environmental photography to establish place without tinting the art.
- Keep calm ivory and near-black foundations. Add a small clay/juniper accent vocabulary through our own tokens.
- Increase body type to 18px in long reading areas and use weight 400. Do not adopt thin body text merely because the reference does.
- Keep functional borders and focus rings where interaction needs them. A “borderless luxury” rule cannot hide form fields or selection.
- Use clear, explicit button labels. A person should not need to discover the purchase interface through animation.
- Preserve quiet square/very slightly rounded geometry. Avoid decorative shadows and oversized pills.
- Use short, useful editorial copy with a clear path to the artist, work, viewing or visit.

The Southwest character should come from the art, people, light, architecture and specificity of place. Generic motifs and unconsented Indigenous patterns would weaken that identity.

## Proposed design tokens

| Token | Proposed value | Use |
|---|---|---|
| Canvas | `#F6F2EB` | Warm page background, quieter than a decorative texture. |
| Art stage | `#FAFAF8` | Neutral work display. Compare with pure white in color QA. |
| Ink | `#242522` | Primary text and essential controls. |
| Muted text | `#625F58` | Secondary text with readable contrast. |
| Clay | `#8D432E` | Small editorial accents and selected highlights. |
| Juniper | `#274A40` | Secondary interaction/wayfinding color, used sparingly. |
| Rule | `#D4CFC5` | Separators. Not the only indicator of an input or state. |
| Focus | `#145A82` | High-visibility focus outline, tested against each surface. |

All actual foreground/background combinations require contrast testing. Do not assume that an attractive muted color passes accessibility. Use text and shape alongside color for semantic states.

Typography proposal: a licensed editorial serif with readable forms, paired with a clear sans-serif for filters, facts and commerce. The Atlas references Freight Display Pro and Suisse Intl. Licensing and availability need confirmation. A prototype may use appropriately licensed alternatives such as Source Serif 4 and Inter if needed, with an explicit review of the resulting character. The proposed fonts provide a substitute. They do not exactly reproduce the reference.

Desktop scale starting points: display 64–80px, page heading 44–56px, section heading 28–40px, body 18px, compact metadata 14–16px. Mobile uses fluid sizes, 32–44px page headings and at least 16px form text. Set headline sizes through actual text and hierarchy tests.

## Page composition rules

A maximum reading/content-width limit of 1,440px, generous but purposeful margins, a 12-column desktop grid, 8-column tablet and 4-column mobile. Base spacing uses a consistent 4px scale with larger editorial intervals. Use spacing to improve reading while keeping useful work visible.

Cards should not all look identical. Art needs a neutral contain frame and exact metadata. Experiences need a useful photographic scene and practical facts. Lodging needs a true room/property representation. Shared type, spacing, actions and metadata rhythm create coherence.

Detailed art pages place a large image beside a concise object/purchase panel. A second row contains context, details and seller/fulfillment information. The assistant appears as a modest invitation and optional panel, never a mascot covering the work.

## Image quality specification

**Acquisition:** obtain artist/photographer-authorized masters, ideally at least 4,000 pixels on the long edge when the source and rights permit, with accurate orientation, a consistent sRGB delivery workflow and visible texture/detail appropriate to the medium. Capture front, relevant detail, frame/back and optional honest installation context. Calibrated photography is preferable to trying to correct poor images after the fact.

**Integrity:** preserve the whole work, correct proportions, true color intent and actual framing status. Use no generative fill, replacement brushwork, fabricated studio scene, recoloring, aggressive sharpening or AI-made detail. Label room visualizations and use the licensed work at accurate scale.

**Delivery:** retain a protected master and generate responsive derivatives with explicit dimensions. Grid images should be appropriately small. Load zoom images on demand. Use AVIF/WebP where quality and compatibility permit, with a suitable fallback. Never hotlink a seller's full-resolution image in production or scrape away a watermark to make an unauthorized image look clean.

**Art QA:** check crop, aspect ratio, color cast, orientation, blur, frame accuracy, rights, credit, alternative text and whether the actual work matches the record. Reject a beautiful image attached to the wrong title or edition. Test dimensions and compression on high-density screens and ordinary mobile service.

**Performance budgets to validate:** first-screen transfer limit of 1.5MB on an ordinary collection page, art card derivatives typically below 150KB where visual fidelity allows, and a hero typically below 350KB. Adjust the starting budgets if compression damages visible art detail. Use real devices and representative art images to balance them.

## Motion and interaction

Brief 120–200ms interface transitions. Subtle image fades are acceptable. Honor reduced motion. No forced loading film, custom cursor dependency, scroll hijacking, unstable masonry jumps, or text that only appears on hover. Design focus, loading, error, success, stale-stock and unavailable-item states explicitly.

## Design decisions for review

Review [Audo #11](http://atomic.nrvana.com/#11) and [Aesop #35](http://atomic.nrvana.com/#35). Confirm the base direction or request a different named system, then review the proposed modifications. The authorized prototype can compare typography and palette options. Final selection still needs review.
