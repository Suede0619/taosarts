# Taos Arts: agent instructions

This is a **public document repository**, not a deployed website or an approved festival program. Start with [SESSION_STATE.md](SESSION_STATE.md), [README.md](README.md), and [CONTRIBUTING.md](CONTRIBUTING.md). Read the relevant research and plan modules before changing their conclusions.

## Purpose and publication standard

Help artists sell work so they can afford to remain in Taos. The current direction is a year-round curated art/destination platform as the core business, with festivals supporting visibility, relationships and visits. Art spans contemporary and other work; the region is not a required aesthetic. Read the [current strategy/brand brief](planning/10-Platform-First-Strategy-and-Brand-Brief.md). Festival authority and separate entity arrangements remain unresolved. Cultivate serious collectors while preserving free public discovery, learning, music where appropriate, and fair artist participation. Begin with Taos and locally supported Arroyo Seco experiences; expand only when evidence and capacity support it.

Public documents must be **generic, anonymous foundations, research, specifications and brainstorming material**. Do not attribute the project, ideas, decisions, task progression or proposed roles to individual participants. Remove participant biographies, dedications, personal circumstances and conversation narratives rather than substituting an unnamed personal story. Assign work to role titles. This applies to tracked agent instructions, handoffs, data tables and prototype source as well as prose. The sole permitted participant-name reference is the factual business association in the HOUSE of FIRE listing. Independently sourced artist names and historical people remain legitimate research subjects. Ignored private material may retain names; leave originals unchanged. This standard supersedes older identity/narrative instructions.

Preserve these project decisions:

- **November 1, 2026 is day one**; year one ends October 31, 2027. Preserve actual historical/source dates and fixed external deadlines. Read [PROJECT-BASELINE.md](PROJECT-BASELINE.md) for dates and controlling decisions.

- [HeyTaos](https://heytaos.com/) is a potential complementary partner with broader, less selective coverage. No partnership is agreed.
- HOUSE of FIRE is a gallery research candidate; [gallery research](website-spec/research/03-TAOS-GALLERIES.md) contains supplied business details. A gallery's involvement does not establish festival board approval or delegated authority.
- The 2026 festival archive is an outstanding input. Its absence is not a reason to invent figures or repeat the project.
- [PROJECT-FOUNDATIONS.md](PROJECT-FOUNDATIONS.md) is the canonical anonymous concept and brainstorming document. Keep proposals, supplied planning assumptions and independently verified evidence distinct.

## Repository and publication boundaries

The repository root is `ART/`, with origin `https://github.com/Suede0619/taosarts.git`, branch `main`. The surrounding TAOS workspace is a different repository. Check root, remote, status, and staged paths before any Git mutation. Stage specific intended files. User requests to add, commit, and push have applied to this work; do not infer permission to include unrelated parent-repository changes.

Keep real buyer data, donor lists, financial statements, bank details, signatures, private contracts, grant accounts, and raw meeting/archive material out of public Git. `private/` is ignored. The original notes are preserved locally there, but will not exist automatically in a fresh clone. Never publish confidential material merely because the user has authorized committing public documents.

For named team and meeting work, read [the operating method](operations/README.md), then the local `private/operations/README.md` if present. The people register and central activity log are authoritative for operational roles and status; person folders and meeting prose link to them. Existing confidential person folders are locally excluded through `.git/info/exclude`, which does not travel with a clone. Keep future named records under `private/` or verify their exclusion before intake. Do not publish NDA portfolios, contact registers, raw correspondence or private meeting links. A local AI editor does not guarantee local model inference.

For incoming festival records, use a private copy of [the archive intake template](templates/2026-Archive-Intake.md). Preserve originals and permissions, reconcile privately, then publish only cleared aggregates or redacted summaries. Do not reproduce third-party art, logos, photographs, reports, or partner directories without appropriate permission.

## Evidence and accounting rules

- Keep **primary published information**, **secondary reporting/extractions**, **supplied planning notes**, **proposals**, and **unknowns** distinct. Anonymity must not turn a planning note into independently verified evidence. A source link is not an audit.
- Preserve the applicable year, geography, currency, counting method, and source. Missing data is blank or explicitly unknown, never zero.
- Do not manufacture historical festival attendance or art-sales series. Nonprofit revenue, program-service revenue, art sales, artist proceeds, tickets, and economic impact measure different things.
- The $1m/$3m/$5m scenarios are targets based on unvalidated assumptions, not forecasts, commitments, or historical results.
- Distinguish completed art value from deposits, signed pipeline, unfulfilled commissions, refunds, tax, shipping, admissions, and donations. Deduplicate orders across referral channels.
- Artist/gallery balances, tax, refunds, and restricted funds are not operating working capital.
- Artist-free participation and proposed commissions require authorization and funding; do not describe them as existing festival rules.
- Keep editorial selection independent of paid placement. Respect representation agreements, cultural authority, artist copyright, and conflict recusals.
- No budgets, dates, venues, sponsorships, partners, applications, or institutional acquisitions are approved merely because a plan names them.

## Updating research and the model

Read [the source register](research/04-Source-Register-and-Open-Questions.md) before researching a previously covered issue. Recheck current information when needed; record meaningful corrections instead of silently replacing old figures. Do not label a historical deadline as upcoming without checking the session date and current guidance.

For financial changes:

1. Edit [data/model-inputs.json](data/model-inputs.json), keeping proposed assumptions explicit.
2. Run `python3 tools/financial_model.py` from this repository. It uses Python's standard library and public inputs only.
3. Review the generated CSVs and [model results](data/model-results.md).
4. Reconcile explanatory figures in the business plan, financial plan, README, and handoff. Automatic generation does not update that prose.

The model checks allocation identities, order-cohort totals, timing shares, annual cash reconciliation, and downside cases. It does not validate demand, vendor quotes, accounting treatment, or legal feasibility.

For documentation-only changes, check relative links, factual consistency, and `git diff --check`; avoid unrelated regeneration or new tests. Review the staged diff and ensure `private/` is excluded before committing. If code or assumptions change, run validation appropriate to that change.

## Continuing work

The newest website work is in [website-spec/](website-spec/README.md). Read its [AGENTS.md](website-spec/AGENTS.md) before continuing. The sequence is **specification → review → prototype → review → production**. A design prototype and live preview are authorized in a separate repository; production remains a separate review gate. Atomic Audo Copenhagen #11 is the provisional prototype direction; the brand/design choice is not finalized. Zero Southwest Art commission applies to direct-artist website sales; its fee subsidy/funding proposal does not automatically rewrite the separate festival model. Research candidates are not authorized stock or agreed partners. Keep demo assistance/checkout clearly simulated; no live seller or financial integrations are authorized by prototype publication.

Use the dated [session handoff](SESSION_STATE.md) for the baseline, outstanding inputs, and next decisions. New user instructions take precedence over old priorities. Progress on work that does not depend on missing inputs; ask only for information genuinely needed for the next dependent action. Preparing a proposal does not authorize sending outreach, submitting an application, signing a contract, or spending money.

Denver planning is separate: read [Denver instructions](Denver/AGENTS.md), then the latest [Common Altitude execution package](Denver/Common-Altitude-2027/README.md). The subsequent October 24 user request explicitly authorized full creative/brand, marketing, business/PRD, proposed program, partner/hiring/action plans and finished pitch-deck artifacts, superseding the earlier research-only stop for creating those deliverables. It did not authorize sending, applications, bookings, hires, spending, signatures or public launch. The new larger-scope model is separate from prior Denver sensitivities, the legacy festival model and website economics. Candidate names describe researched professionals, never committed partners. Public participant anonymity remains in force; the named owner-deck copy is ignored/private.

The selected source repository for prototype and final production is `Suede0619/sw-arts-website`. The design prototype uses GitHub Pages at `https://suede0619.github.io/sw-arts-website/`; do not publish to Sites. GitHub Pages' official usage rules prohibit running an ecommerce business, so the final selling site needs a compatible host deployed from this same repository. See the website technical specification and prototype DEPLOYMENT.md; production hosting is unresolved, not permission to quietly choose another provider.

After meaningful work, update the handoff with actual changes, evidence, decisions, validation, and remaining questions. State the baseline commit or resulting commit without creating a circular requirement to embed the handoff's own commit hash. Keep the handoff concise and link to the detailed documents.
