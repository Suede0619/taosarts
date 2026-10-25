# Workspace and prototype validation: October 25, 2026

The Denver, Southwest Arts and shared TEAM organization preserves document navigation and prototype display. The audit found no broken internal links or prototype rendering failures.

Baseline document commit: `4001f53`. Website source commit: `6a70379`. The latest published runtime remains `3d04b8636507646cddc4aa99bedc5a1a252c9186`.

## Document and repository checks

| Check | Result |
|---|---|
| Active Markdown documents before this verification record | 147 files. |
| Local links and images | All 627 resolve, including two heading fragments. The parser includes Markdown tables, reference links and HTML links. |
| Public links and images | All 503 resolve within tracked files, including a fresh clone. |
| GitHub document links to main | All six reference existing paths. GitHub's current ART and website file trees match the local tracked trees and baseline commits. |
| Private team records | All 68 remain ignored. Public TEAM files contain anonymous guidance only. |
| Git whitespace checks | Pass. |

The counts above describe the initial audit. After adding this record and its handoff/index links, the final check covers 148 active Markdown files and 630 local references with no missing targets. Original source archives and historical third-party research URLs remain dated references. This audit checks folder navigation and software display. It does not refresh research facts or third-party schedules and prices.

## Prototype checks

The [published preview](https://suede0619.github.io/sw-arts-website/) returns HTTP 200 and renders from its existing GitHub Pages address.

| Check | Result |
|---|---|
| `npm run check` | Pass from the relocated `SouthwestArts/sw-arts-website/` checkout. |
| `npm test` | All nine existing browser tests pass under `/sw-arts-website/`. |
| Full route review | All 64 pages pass locally and live, at 1440 × 1000 desktop and 390 × 844 phone sizes. Total 256 page checks. |
| Rendering and navigation | No JavaScript runtime errors, failed site responses, broken images, unknown internal destinations or horizontal overflow. |
| Visual review | Live desktop and phone home-page screenshots display the layout and imagery correctly. |
| Published files | All 17 tracked files under `dist/` return HTTP 200 and match local bytes, including HTML, JavaScript, CSS, catalog, images, icon and robots.txt. |
| Published workflow | [Run 40097912500](https://github.com/Suede0619/sw-arts-website/actions/runs/40097912500) reports successful validation and deployment. |

The browser tests cover filters and empty results, saved-plan persistence, comparison, concierge filter/undo, simulated checkout, venue sections, lodging dates, phone navigation/focus, unsafe-input handling and Arroyo Seco travel origin. The route review covers every demo work, artist and place page, plus main pages and the artist/lodging tabs.

## Result and retained evidence

The checks required no website source, model, asset or deployment changes. This commit adds the verification record and updates navigation and handoffs. The separate website repository retains its prior source commit. The parent TAOS repository's housing work remains outside this task.

Detailed link targets, browser results, published-file hashes and screenshots remain local under ignored `private/validation-2026-10-25/`. Named team records and private link details do not enter public Git.
