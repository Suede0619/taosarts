# Arts workspace: agent instructions

This public document repository contains two workflows. Read the matching instructions and handoff before starting work.

| Workflow | Instructions | Entry point and handoff |
|---|---|---|
| Denver Energy Center art festival and related work | [Denver/AGENTS.md](Denver/AGENTS.md) | [Denver/README.md](Denver/README.md), [Denver/SESSION_STATE.md](Denver/SESSION_STATE.md), then [Common Altitude](Denver/Common-Altitude-2027/README.md) |
| Southwest Arts shows, platform and website | [SouthwestArts/AGENTS.md](SouthwestArts/AGENTS.md) | [SouthwestArts/README.md](SouthwestArts/README.md), [SouthwestArts/SESSION_STATE.md](SouthwestArts/SESSION_STATE.md) |

Read [SESSION_STATE.md](SESSION_STATE.md), [WRITING-GUIDE.md](WRITING-GUIDE.md) and [CONTRIBUTING.md](CONTRIBUTING.md). The user's latest scope and corrections control the task. Keep Denver work in `Denver/` and Southwest Arts work in `SouthwestArts/`. The internal team spans both projects and belongs in [TEAM/](TEAM/README.md). Read [TEAM/AGENTS.md](TEAM/AGENTS.md) for that work. Shared repository guidance and the review covering both workflows stay at the ART root. Do not merge the workflows' financial models, event approvals or website economics.

## Project history and current split

| Date | Development | Current meaning |
|---|---|---|
| October 19, 2026 | The repository began with Taos arts and festival research, planning ideas, historical financial illustrations and a website/business concept. | These are dated research and proposals. Unknown historical sales and attendance remain unknown. |
| October 21 | Public writing was revised to remove participant attribution and use anonymous project roles. | Apply the anonymity and evidence rules to all public documents and prototype copy. |
| October 23 | Strategy shifted to a year-round curated art and destination platform as the proposed core business, with shows and festivals supporting discovery and visits. | The regional platform remains a proposal. Taos is the only v1 region. Direct artist website sales carry zero Southwest Arts commission. |
| October 24 | Denver research advanced into the separate Common Altitude event proposal, brand, plans, program, models and decks. | Denver planning has its own scope, model and approval gates. Proposed dates, venue, costs, funding and partnerships are unconfirmed. |
| October 25 | Work was organized into separate Denver and SouthwestArts folders. Shared team records moved to TEAM. Southwest Arts added buyer-led service and audience/pitch exploration. | Continue each workflow from its own handoff. The website source remains an independent repository. The service pivot is for review, not an adopted business or production change. |

This chronology explains how current scope developed. The dated [workspace handoff](SESSION_STATE.md) and each workflow handoff hold detailed deliverables, validation, open questions and corrections. Newer decisions supersede older proposals only where the documents say so.

## Repository boundaries

The repository root is `ART/`, origin `https://github.com/Suede0619/taosarts.git`, branch `main`. The surrounding TAOS workspace is a separate repository with unrelated work. Check working directory, Git root, remotes, status and staged paths before Git mutations. Stage only intended public files. Existing public commit/push authorization persists. It does not include private records or unrelated parent-workspace changes.

`SouthwestArts/sw-arts-website/` is the ignored, independent `Suede0619/sw-arts-website` repository. Its own AGENTS.md governs website changes. Preserve its Git history and origin when moving it. Do not add it as a submodule or embedded repository. Pulling or committing ART does not pull or commit website source. Older local checkouts may still use `sw-arts-website/`, which also remains ignored.

## Publication, evidence and privacy

Public documents must remain anonymous with respect to project participants. Use role titles. Omit participant biographies, personal circumstances, dedications, private conversations and narratives attributing proposals or decisions. Apply this to instructions, handoffs, tables and prototype copy. The sole participant-name exception is the factual business association in the HOUSE of FIRE listing. Independently sourced artists, historical figures and researched outside professionals remain legitimate subjects. Preserve original private records and their evidence status.

Distinguish published facts, secondary reports, supplied planning inputs, proposals and unknowns. Keep dates, units, source links and limitations. Missing data is unknown, never zero. A budget, proposed role, date or venue grants no approval. Art sales, artist proceeds, organizer revenue, tax, restricted funds and operating cash measure different things. Recheck unstable facts before relying on them. This folder reorganization does not refresh research.

Git ignores `private/` at every depth. Southwest Arts source archives remain under `SouthwestArts/private/`. Shared internal member folders and named operational records live in TEAM. The tracked `.gitignore` excludes all TEAM contents except its anonymous `README.md`, `AGENTS.md` and `OPERATING-METHOD.md`. Denver keeps project-specific private records in its own folders. The shared historical editorial archive remains under `private/editorial-review/`. Do not publish buyer/donor records, portfolios, NDA files, personal contact registers, raw correspondence, signatures, bank details, private contracts or credentials. Preserve source archives and original files. Verify exclusions before private intake or staging.

For named team work across either project, read [the operating method](TEAM/OPERATING-METHOD.md), then local `TEAM/INDEX.local.md` and `TEAM/operations/README.md` if available. One private people register and activity log remain authoritative across both workflows. Member folders link to these registers. Moving folders creates no new commitments or permission to send messages.

## Authority and verification

Preparing proposals and decks does not authorize outreach, applications, bookings, hires, spending, signatures or public launch. The Southwest Arts prototype has its own existing publication authority. Production review, seller permissions, commerce and hosting decisions remain separate. Keep its selected GitHub source repository. Do not publish it through Sites.

For structural or documentation changes, validate relative links, commands, Git exclusions and `git diff --check`. Preserve model numbers and source hashes. Avoid unrelated regeneration or test expansion. Follow each workflow's instructions when changing model inputs or generated copy. Update the relevant handoffs with actual changes, checks and unresolved work. Report repository scope and any committed paths accurately.
