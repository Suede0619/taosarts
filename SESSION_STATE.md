# Arts workspace handoff: October 25, 2026

## Two workflows

The user separated ART into two workflows on October 25. [Denver](Denver/README.md) holds the Energy Center art festival and all related research, Common Altitude plans, program, budgets and decks. [SouthwestArts](SouthwestArts/README.md) holds Southwest Arts shows, platform plans, Taos research and website work.

Start with the matching [Denver instructions](Denver/AGENTS.md) and [handoff](Denver/SESSION_STATE.md), or [Southwest Arts instructions](SouthwestArts/AGENTS.md) and [handoff](SouthwestArts/SESSION_STATE.md). ART remains the public `Suede0619/taosarts` repository. Baseline before this reorganization: `a3f74a3193524b647f089d6f3b12edeaca57e001`.

## Folder changes

| Previous ART location | Current ART location |
|---|---|
| Southwest Arts README, session handoff and PROJECT documents | `SouthwestArts/` |
| `planning/`, `research/`, `data/`, `tools/`, `templates/`, `operations/` | Same folder names under `SouthwestArts/` |
| `website-spec/` | `SouthwestArts/website-spec/` |
| Independent `sw-arts-website/` checkout | `SouthwestArts/sw-arts-website/` |
| Local `private/source/` and `private/operations/` | Same folder names under `SouthwestArts/private/` |
| Local person-material folders | `SouthwestArts/private/people/` |

The root README and AGENTS.md now route work to the two workflows. Shared writing/contribution guidance and the October 24 review stay at the root. The shared historical editorial evidence remains ignored at `private/editorial-review/`. Denver retains its existing internal structure and private archives. Cross-workflow references point to the new Southwest Arts paths.

The website checkout retains its own `.git`, origin, branch and history. ART ignores both its current and older local locations. On another computer, pull the public documents and relocate any existing ignored checkout and local private folders separately after checking source and destination. Git does not sync or move those ignored records. Do not overwrite an existing destination or add the website as a submodule.

## Validation and remaining work

Validation covered 143 Markdown files and all 574 relative links, including active private working navigation. All links resolve. All 1,931 baseline files remain present at their expected locations. Hash comparisons preserve 1,477 original archive files, all 53 public CSV/JSON files, all 19 public binary/vector artifacts and all 17 website runtime files. Fifty-three tracked Southwest Arts documents/data/tool files move into the new folder, with a new workflow AGENTS.md.

The Southwest Arts financial model runs from its new path and reproduces the prior CSV outputs and numerical results. Its code changes only the two command-description strings. Website `npm run check` passes from the relocated checkout. Website source, tests, assets and deployment configuration retain their prior contents. Git exclusions cover every relocated private folder and the independent website checkout. Whitespace checks pass.

The separate website documentation commit `6a70379` updates only `AGENTS.md`, `README.md` and `DEPLOYMENT.md` for the new local location and document links. Its Pages workflow excludes these documentation-only paths, so that commit does not publish a new preview. The prior recorded deployment remains the website baseline.

Research dates, model assumptions, project timeline, proposal status and production review requirements remain as documented. The parent TAOS repository's unrelated housing changes remain outside this task. No deployment forms part of the reorganization. Private working navigation stays local and ignored.
