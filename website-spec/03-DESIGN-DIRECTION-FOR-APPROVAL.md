# Design direction — recommendation awaiting approval

**Decision status: pending Stuart's choice.** The user explicitly asked to review the selected system before it is finalized. This document proposes a direction; it does not finalize it or authorize a prototype.

## The actual Atomic options reviewed

The supplied [Design System Atlas](http://atomic.nrvana.com/) contains forty distilled reference systems. Its public `data.js` and application source were retrieved on October 19, 2026, including the actual names, numbered entries, tokens and hash-navigation behavior. These are the Atlas author's interpretations, not proof that the original brands publish reusable component libraries, award claims, or licenses.

| Option | Atlas link | Fit for Southwest Art | Decision |
|---|---|---|---|
| **Audo Copenhagen, #11** | [Preview #11](http://atomic.nrvana.com/#11) | Warm light surfaces, architectural/large photography, restrained serif headings and square, quiet commerce components | **Recommended base** |
| **Aesop, #35** | [Preview #35](http://atomic.nrvana.com/#35) | Excellent literary/editorial restraint and natural tones; potentially more text-led than the art-first commerce objective | Alternative to review |
| Rivian, #32 | [Preview #32](http://atomic.nrvana.com/#32) | Strong landscape and practical specification language, but its adventure/automotive emphasis is less suited to the primary art proposition | Contextual reference, not proposed base |

Technical access note: the HTTPS site could not be fetched by the web reader; a local read retrieved the public source after a certificate-verification problem. No account or access control was bypassed. Source snapshots are private research files. A future production site must use valid HTTPS; this access issue has no bearing on the visual recommendation.

## Recommendation: adapt Audo, with art and legibility taking priority

Borrow the warmth, image confidence, typography rhythm and restraint. Build original Southwest Art components and content; do not copy Audo's logos, photographs, brand assets, or assume a font license. Confirm the Atlas kit's actual reuse terms before importing code. A reference system is a starting point, not a complete accessible commerce implementation.

Proposed adaptations:

- Make whole artworks the visual center; use environmental photography to establish place without tinting the art.
- Keep calm ivory and near-black foundations; add a small clay/juniper accent vocabulary through our own tokens.
- Increase body type to 18px in long reading areas and use weight 400; do not adopt thin body text merely because the reference does.
- Keep functional borders and focus rings where interaction needs them. A “borderless luxury” rule cannot hide form fields or selection.
- Use clear, explicit button labels. A person should not need to discover the purchase interface through animation.
- Preserve quiet square/very slightly rounded geometry; avoid decorative shadows and oversized pills.
- Use short, useful editorial copy with a clear path to the artist, work, viewing or visit.

The Southwest character should come from the art, people, light, architecture and specificity of place. Generic motifs and unconsented Indigenous patterns would weaken that identity.

## Proposed token direction — illustrative, not frozen

| Token | Proposed value | Use |
|---|---|---|
| Canvas | `#F6F2EB` | Warm page background, quieter than a decorative texture. |
| Art stage | `#FAFAF8` | Neutral work display; compare with pure white in color QA. |
| Ink | `#242522` | Primary text and essential controls. |
| Muted text | `#625F58` | Secondary text with readable contrast. |
| Clay | `#8D432E` | Small editorial accents and selected highlights. |
| Juniper | `#274A40` | Secondary interaction/wayfinding color, used sparingly. |
| Rule | `#D4CFC5` | Separators; not the only indicator of an input or state. |
| Focus | `#145A82` | High-visibility focus outline, tested against each surface. |

All actual foreground/background combinations require contrast testing. Do not assume that an attractive muted color passes accessibility. Semantic states use text and shape, not color alone.

Typography proposal: a licensed editorial serif with readable forms, paired with a clear sans-serif for filters, facts and commerce. The Atlas references Freight Display Pro and Suisse Intl; licensing and availability need confirmation. A prototype may use appropriately licensed alternatives such as Source Serif 4 and Inter if needed, with an explicit review of the resulting character. This is a proposed substitution, not a claim that those fonts exactly reproduce the reference.

Desktop scale starting points: display 64–80px, page heading 44–56px, section heading 28–40px, body 18px, compact metadata 14–16px. Mobile uses fluid sizes, 32–44px page headings and at least 16px form text. Adjust by actual text length and tested hierarchy, not fixed oversized headlines.

## Page composition rules

A maximum reading/content width around 1,440px, generous but purposeful margins, a 12-column desktop grid, 8-column tablet and 4-column mobile. Base spacing uses a consistent 4px scale with larger editorial intervals; whitespace supports comprehension rather than pushing useful work far below the fold.

Cards should not all look identical. Art needs a neutral contain frame and exact metadata; experiences need a useful photographic scene and practical facts; lodging needs a true room/property representation. Shared type, spacing, actions and metadata rhythm create coherence.

Detailed art pages place a large image beside a concise object/purchase panel. A second row contains context, details and seller/fulfillment information. The assistant appears as a modest invitation and optional panel, never a mascot covering the work.

## Image quality specification

**Acquisition:** obtain artist/photographer-authorized masters, ideally at least 4,000 pixels on the long edge when the source and rights permit, with accurate orientation, a consistent sRGB delivery workflow and visible texture/detail appropriate to the medium. Capture front, relevant detail, frame/back and optional honest installation context. Calibrated photography is preferable to trying to correct poor images after the fact.

**Integrity:** preserve the whole work, correct proportions, true color intent and actual framing status. No generative fill, replacement brushwork, fabricated studio scenes, automatic recoloring, aggressive sharpening, or AI-made “detail.” A room visualization must be labeled and derived from the actual licensed work at accurate scale.

**Delivery:** retain a protected master and generate responsive derivatives with explicit dimensions. Grid images should be appropriately small; zoom is loaded on demand. Use AVIF/WebP where quality and compatibility permit, with a suitable fallback. Never hotlink a seller's full-resolution image in production or scrape away a watermark to make an unauthorized image look clean.

**Art QA:** check crop, aspect ratio, color cast, orientation, blur, frame accuracy, rights, credit, alternative text and whether the actual work matches the record. Reject a beautiful image attached to the wrong title or edition. Image dimensions and compression are tested on high-density screens and ordinary mobile service.

**Performance budgets to validate:** first-screen transfer around 1.5MB or less on an ordinary collection page, art card derivatives typically below 150KB where visual fidelity allows, and a hero typically below 350KB. These are starting budgets, not reasons to destroy image fidelity. Use real devices and representative art images to balance them.

## Motion and interaction

Brief 120–200ms interface transitions; subtle image fades are acceptable. Honor reduced motion. No forced loading film, custom cursor dependency, scroll hijacking, unstable masonry jumps, or text that only appears on hover. Focus, loading, errors, success, stale inventory and unavailable items are designed states, not implementation leftovers.

## Approval requested

Review [Audo #11](http://atomic.nrvana.com/#11) and [Aesop #35](http://atomic.nrvana.com/#35). Confirm the base direction or request a different named system, then review the proposed modifications. The prototype can test a small typography/palette comparison after authorization, but no choice is silently treated as final now.
