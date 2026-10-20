# Taos Arts: agent instructions

This is a **public document repository**, not a deployed website or an approved festival program. Start with [SESSION_STATE.md](SESSION_STATE.md), [README.md](README.md), and [CONTRIBUTING.md](CONTRIBUTING.md). Read the relevant research and plan modules before changing their conclusions.

## Purpose and user direction

Help artists sell work so they can afford to remain in Taos. Revive Taos Fall Arts Festival and develop a proposed, separate curated Southwest arts guide. Cultivate serious collectors while preserving free public discovery, learning, music where appropriate, and fair artist participation. Begin with Taos and locally supported Arroyo Seco experiences; expand only when evidence and capacity support it.

Preserve these corrections:

- The user is **Dave Paul**, also **David Paul**. Use Dave Paul in documents and Dave in conversation.
- **November 1, 2026 is day one**; year one ends October 31, 2027. Preserve actual historical/source dates and fixed external deadlines. Read [PROJECT-BASELINE.md](PROJECT-BASELINE.md) for dates and controlling decisions.

- **“TellUs” means [HeyTaos](https://heytaos.com/)**. Dave Paul sees it as a potential complementary partner: broader and less curated than the proposed arts guide. No partnership is agreed.
- Felix Kay is **Gallery Director at HOUSE of FIRE**. User-supplied business contact details are in [FelixMeet](FelixMeet).
- Felix's precise festival leadership year, title, and delegated authority are not established. His involvement is not board approval of this plan.
- Felix intends to provide his 2026 document folder later. Its absence is an open input, not a reason to invent figures or repeat the entire project.
- The original four-version notes were rewritten as one comprehensive summary at the **extensionless `FelixMeet` path**. Keep one canonical meeting account; distinguish later user corrections from the original conversation.

## Repository and publication boundaries

The repository root is `ART/`, with origin `https://github.com/Suede0619/taosarts.git`, branch `main`. The surrounding TAOS workspace is a different repository. Check root, remote, status, and staged paths before any Git mutation. Stage specific intended files. User requests to add, commit, and push have applied to this work; do not infer permission to include unrelated parent-repository changes.

Keep real buyer data, donor lists, financial statements, bank details, signatures, private contracts, grant accounts, and raw meeting/archive material out of public Git. `private/` is ignored. The original notes are preserved locally there, but will not exist automatically in a fresh clone. Never publish confidential material merely because the user has authorized committing public documents.

For incoming Felix records, use a private copy of [the archive intake template](templates/2026-Archive-Intake.md). Preserve originals and permissions, reconcile privately, then publish only cleared aggregates or redacted summaries. Do not reproduce third-party art, logos, photographs, reports, or partner directories without appropriate permission.

## Evidence and accounting rules

- Keep **primary published information**, **secondary reporting/extractions**, **meeting/user accounts**, **proposals**, and **unknowns** distinct. A source link is not an audit.
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

The newest website work is in [website-spec/](website-spec/README.md). Read its [AGENTS.md](website-spec/AGENTS.md) before continuing: the user requires **specification → review → prototype → review → production**, and Dave has now authorized a design prototype and live preview in a separate repository. Production remains a separate review gate. Atomic Audo Copenhagen #11 is the provisional prototype direction; the brand/design choice is not finalized. Zero Southwest Art commission applies to direct-artist website sales; its fee subsidy/funding proposal does not automatically rewrite the separate festival model. Research candidates are not authorized stock or agreed partners. Keep demo assistance/checkout clearly simulated; no live seller or financial integrations are authorized by prototype publication.

Use the dated [session handoff](SESSION_STATE.md) for the baseline, outstanding inputs, and next decisions. New user instructions take precedence over old priorities. Progress on work that does not depend on missing inputs; ask only for information genuinely needed for the next dependent action. Preparing a proposal does not authorize sending outreach, submitting an application, signing a contract, or spending money.

Dave selected `Suede0619/sw-arts-website` for prototype and final production source and requested GitHub hosting. The design prototype uses GitHub Pages at `https://suede0619.github.io/sw-arts-website/`; do not publish to Sites. GitHub Pages' official usage rules prohibit running an ecommerce business, so the final selling site needs a compatible host deployed from this same repository. See the website technical specification and prototype DEPLOYMENT.md; production hosting is unresolved, not permission to quietly choose another provider.

After meaningful work, update the handoff with actual changes, evidence, decisions, validation, and remaining questions. State the baseline commit or resulting commit without creating a circular requirement to embed the handoff's own commit hash. Keep the handoff concise and link to the detailed documents.
