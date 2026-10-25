# Updating this document repository

Keep research, supplied planning inputs and proposed decisions distinguishable. A target is not an outcome. An organizer report is not an audit. A missing figure is not zero. Use direct source links near factual claims, record the applicable year and units, and explain corrections.

Read [WRITING-GUIDE.md](WRITING-GUIDE.md) before editing prose, headings, labels or presentations. Keep numbers, evidence status and source quotations accurate.

The [Denver Energy Center workflow](Denver/README.md) lives in `Denver/`. [Southwest Arts shows, platform and website work](SouthwestArts/README.md) live in `SouthwestArts/`. Read the relevant folder's AGENTS.md and handoff. Shared repository guidance stays at the ART root.

## Before changing a plan

1. Record new evidence, its source, date, permissions, and limitations.
2. Keep private source records outside Git. Publish approved aggregates or redacted summaries only.
3. Update the affected research and open questions.
4. For the Southwest Arts legacy model, change `SouthwestArts/data/model-inputs.json` and run `python3 SouthwestArts/tools/financial_model.py` from ART. Denver models have their own inputs and commands. Reconcile the affected explanatory prose.
5. Record material decisions with date, owner, authority, and effect on budget or scope. Do not describe proposals as approved without evidence.
6. Check relative links and review the actual staged diff before committing.

## Privacy and rights

Keep current public documents anonymous and unattributed. Use role titles for project responsibilities. Omit participant biographies, personal circumstances, dedications and narratives of who proposed or approved an idea. Apply this to agent instructions, handoffs, filenames, research tables and prototype copy too. A factual business-name association may remain in the HOUSE of FIRE listing. Sourced artists and historical figures remain valid research subjects. Private ignored records may retain names and original provenance. Anonymization must preserve the distinction between supplied planning notes, verified evidence and proposals.

Git ignores `private/`, environment files and local caches. An ignore rule does not remove something already tracked. Never commit buyer identities, bank/payment details, tax IDs, donor lists, signatures, private contracts, credentials, or the unredacted future 2026 archive. Store sensitive working records in an appropriately controlled location. This public repo is not a CRM or settlement system.

Do not import third-party images, brochures, reports, or a partner's directory without permission. Preserve artist copyright and limited promotional licenses. Nothing in this repository grants rights to festival marks, House of Fire assets, HeyTaos content, or other organizations' material.

## Commit scope

Run Git commands from this `ART` repository. Check `git rev-parse --show-toplevel` and `git remote -v` before staging or pushing. Stage specific public files, review them, and use a descriptive commit. The surrounding workspace has a separate repository and may contain unrelated work.
