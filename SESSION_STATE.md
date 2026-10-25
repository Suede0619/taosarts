# Arts workspace handoff: October 25, 2026

## Link and prototype verification

The subsequent user request asked for a full link/display check, then add, commit and push. [The verification record](WORKSPACE-VALIDATION-2026-10-25.md) records the results against document baseline `4001f53` and website source `6a70379`. All 627 initial local references resolve, including heading anchors and links needed by a fresh clone. The website's static checks and all nine browser tests pass from its new location. All 64 pages render locally and live at desktop and phone sizes, with no runtime errors, failed site responses, missing images or horizontal overflow. All 17 published files match local bytes. Live desktop/phone screenshots pass visual review.

GitHub file trees match the baseline local repositories. The existing Pages workflow's validation and deployment jobs report success. No software or link repairs were necessary. This update adds verification documentation and handoff/index links only. Detailed local evidence stays ignored under `private/validation-2026-10-25/`. Team records, research/model assumptions, website source and deployment settings retain their prior contents.

## Shared team correction

The user's subsequent October 25 instruction confirms one internal team across both projects. Shared member folders, the people register, central activity log, meetings and drafts now live in [TEAM](TEAM/README.md). [TEAM/AGENTS.md](TEAM/AGENTS.md) and [the operating method](TEAM/OPERATING-METHOD.md) govern that workspace. This supersedes the earlier placement of shared team material under SouthwestArts. Baseline before this correction: `4a65593`.

The existing local member folders moved intact into TEAM, and the existing project-initiator record now has its own local member folder. Named records remain ignored. Only anonymous TEAM guidance belongs in public Git. The single people/activity registers retain their IDs and statuses, with a dated record of the user's clarification. Outside Denver contact dossiers remain in Denver's project-specific evidence archive.

Validation covered 147 active Markdown files and 627 relative links, all resolving. All 1,934 baseline files remain present at their expected paths. All 1,477 original archive files and 1,127 non-document files retain their hashes. Git excludes all 68 private TEAM files. Only the three anonymous TEAM guidance files enter public Git. Project model data, website source and deployment settings remain unchanged. Private member files and operational records require their existing local handling and do not sync through GitHub.

## Two workflows

The user separated ART into two workflows on October 25. [Denver](Denver/README.md) holds the Energy Center art festival and all related research, Common Altitude plans, program, budgets and decks. [SouthwestArts](SouthwestArts/README.md) holds Southwest Arts shows, platform plans, Taos research and website work.

Start with the matching [Denver instructions](Denver/AGENTS.md) and [handoff](Denver/SESSION_STATE.md), or [Southwest Arts instructions](SouthwestArts/AGENTS.md) and [handoff](SouthwestArts/SESSION_STATE.md). ART remains the public `Suede0619/taosarts` repository. Baseline before this reorganization: `a3f74a3193524b647f089d6f3b12edeaca57e001`.

## Folder changes

| Previous ART location | Current ART location |
|---|---|
| Southwest Arts README, session handoff and PROJECT documents | `SouthwestArts/` |
| `planning/`, `research/`, `data/`, `tools/`, `templates/` | Same folder names under `SouthwestArts/` |
| Public `operations/README.md` | Shared `TEAM/OPERATING-METHOD.md` |
| `website-spec/` | `SouthwestArts/website-spec/` |
| Independent `sw-arts-website/` checkout | `SouthwestArts/sw-arts-website/` |
| Local `private/source/` | `SouthwestArts/private/source/` |
| Local shared operational records | `TEAM/operations/` |
| Local internal member folders | Directly under `TEAM/` |

The root README and AGENTS.md now route work to the two workflows. Shared writing/contribution guidance and the October 24 review stay at the root. The shared historical editorial evidence remains ignored at `private/editorial-review/`. Denver retains its existing internal structure and private archives. Cross-workflow references point to the new Southwest Arts paths.

The website checkout retains its own `.git`, origin, branch and history. ART ignores both its current and older local locations. On another computer, pull the public documents and relocate any existing ignored checkout and local private folders separately after checking source and destination. Git does not sync or move those ignored records. Do not overwrite an existing destination or add the website as a submodule.

## Validation and remaining work

Validation covered 143 Markdown files and all 574 relative links, including active private working navigation. All links resolve. All 1,931 baseline files remain present at their expected locations. Hash comparisons preserve 1,477 original archive files, all 53 public CSV/JSON files, all 19 public binary/vector artifacts and all 17 website runtime files. Fifty-three tracked Southwest Arts documents/data/tool files move into the new folder, with a new workflow AGENTS.md.

The Southwest Arts financial model runs from its new path and reproduces the prior CSV outputs and numerical results. Its code changes only the two command-description strings. Website `npm run check` passes from the relocated checkout. Website source, tests, assets and deployment configuration retain their prior contents. Git exclusions cover every relocated private folder and the independent website checkout. Whitespace checks pass.

The separate website documentation commit `6a70379` updates only `AGENTS.md`, `README.md` and `DEPLOYMENT.md` for the new local location and document links. Its Pages workflow excludes these documentation-only paths, so that commit does not publish a new preview. The prior recorded deployment remains the website baseline.

Research dates, model assumptions, project timeline, proposal status and production review requirements remain as documented. The parent TAOS repository's unrelated housing changes remain outside this task. No deployment forms part of the reorganization. Private working navigation stays local and ignored.
