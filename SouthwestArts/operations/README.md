# People, meetings and commitments: operating method

**October 23, 2026, Proposed lightweight working system, now set up locally.** Keep the public foundation documents anonymous. Maintain named operational records privately, with one people register and one central activity log. Use ordinary Markdown at this stage. Another project-management subscription is unnecessary until coordination needs justify it.

## Why this structure

A folder for each person is useful for their material, but it is a poor master task system: a meeting can involve several people, proposals change, and copying the same task into several folders produces conflicting status. Use person folders as evidence drawers. Keep people/capacity in one register, and every live statement, proposal, commitment and decision in one log linked to its source. Meeting notes preserve context. The activity log holds current tasks.

| Layer | Canonical record | What belongs there | Access |
|---|---|---|---|
| Foundation | Current baseline, strategy/brand brief and specifications | Mission, scope, anonymous proposals, verified research, economics and review gates | Public GitHub |
| People | `private/operations/PEOPLE.md` | Actual names, contact details, role interest versus appointment, capabilities/evidence, availability and engagement questions | Private/local |
| Activity | `private/operations/ACTIVITY-LOG.md` | Statements, proposals, actions, decisions, unresolved questions, owners, evidence and current status | Private/local |
| Sources | `private/operations/SOURCES.md` and retained originals | Source IDs, exact correspondence, supplied summaries, date confidence, files, links and confidentiality restrictions | Private/local |
| Meetings | `private/operations/meetings/` | Dated interpreted account, source limitations and links to log IDs | Private/local |
| Participant material | `private/people/` | Original portfolios, capability evidence, reference catalogs and source snapshots | Private/local |
| Sharing | `private/operations/sharing/` and `drafts/` | A reviewed participant copy and ready-to-send messages, excluding unrelated private material | Private. Share deliberately |

The ignored records are **not included in GitHub or recreated by a clone**. This table maps the local records. Public GitHub contains no private files. The ART `.gitignore` excludes `private/` at every depth, including person material now under `SouthwestArts/private/people/`. Do not list named folder paths in anonymous public documents. Keep future confidential intake under `private/` and verify its exclusion.

## Minimum useful people record

Use a stable `P-###` identifier. Capture these fields without inventing the unknowns:

| Field | Recording rule |
|---|---|
| Identity/contact | Preferred spelling and supplied contact. Separate websites from email addresses. Record provenance. |
| Relationship | Contributor, potential collaborator, appointed contractor, reference contact or supplier. These are different states. |
| Role | Separate current activity, stated interest and an accepted appointment. Record scope/authority only when agreed. |
| Capability | Evidence by case, role credit and source. Preserve collaborators’ credits. Distinguish self-report from inspected output. |
| Availability | Stated hours/week, earliest start, duration, review cadence and constraints. Unknown is not unlimited. |
| Engagement | Accepted scope, fee/payment terms, funding, IP/usage rights, confidentiality, employer/client constraints and approval authority. |
| Follow-through | Link central activity IDs. Do not copy a second editable task list. |
| Verification | Source IDs, last checked date and what still needs confirmation. |

Keep a separate reference-network category. A supplied link or reported acquaintance is not a recruit, introduction, endorsement or available supplier. List missing functions as capability gaps. Add people only after actual involvement.

## Central log schema and vocabulary

Use one stable ID per distinct item, source references, a recorded date and a dated change note. Preserve old statements when later evidence corrects them.

| Record | Essential fields / allowed meaning |
|---|---|
| Statement `S-###` | Speaker when known, quotation or labeled paraphrase, source, date and confidence. “Said” does not mean verified. |
| Proposal `P-###` | Idea, origin/evidence, assumptions, affected scope/budget, unresolved questions and status. No contract implied. |
| Action `A-###` | Action, owner, whether accepted or merely suggested, actual due date if supplied, status, dependencies and completion evidence. |
| Decision `D-###` | Exact choice, decision-maker/authority, effective date, scope, source and any superseded decision. Absent authority stays a proposal. |
| Correction/question `C-###` | Original claim, corrected position or missing evidence, supporting source and consequence. |

Action statuses: **proposed then acceptance unconfirmed then accepted/open then in progress then complete**, with **blocked, declined, cancelled or completion unknown** when appropriate. Record a finished draft as awaiting sending. Record an inspected attachment as received locally. A suggested action in generated minutes is not proof of acceptance. Missing deadlines remain “not supplied”. Label suggested review dates explicitly. Keep them separate from accepted deadlines. Record external deadlines separately from personal commitments.

“Complete” requires a receipt, delivered artifact, accepted result or other relevant evidence. A positive email does not establish a formal role. A file on disk does not establish permission to redistribute it. Record current limitations alongside useful evidence.

## Working cadence

1. **Intake:** retain the original note/email/file privately. Assign a source ID, date confidence, handling rule and optional checksum. Preserve the original wording separately from interpretation.
2. **Interpret:** prepare one readable meeting account, distinguishing statements, proposals, decisions and missing facts. Link the original. Do not call a summary a verbatim transcript.
3. **Register:** update only the people register and central log for live roles/actions/status. Use links from person folders and meeting files.
4. **Confirm:** prepare a short participant review copy. Ask for corrections, owner acceptance and realistic dates. Do not declare silence approval. Sending is a separate action requiring actual authorization.
5. **Review:** a proposed weekly 15-minute check covers available capacity, a few next actions, blockers and funding. A meeting record creates no booking.
6. **Publish:** put only appropriate anonymous implications into the baseline/specs. Retain private attribution in the private source chain. Update the handoff after meaningful changes.

## Confidentiality and sharing

The NDA portfolio, contact details, raw emails, private meeting links and unapproved commercial terms stay out of public Git and the prototype. Public web visibility is not permission to reuse artwork, photography, client logos or lengthy text. Catalog relevant links and retain private research snapshots. Do not bypass high-resolution galleries’ access controls.

Git ignore controls ordinary staging. It provides no encryption, access control, backup or AI privacy guarantee. A folder on a local computer may supply context to a hosted model. Review provider/account settings and source permission before processing confidential work. [Zed explains its different model request paths](https://zed.dev/docs/ai/privacy-and-security). [Claude Code documents its data policies](https://code.claude.com/docs/en/data-usage). Checked October 23, 2026.

Before team-wide access, choose an access-controlled shared store with appropriate participants and backup. This setup provisions none of those protections. Do not invite anyone or move NDA files into a new service automatically. The existing local arrangement is useful now but is not yet a shared CRM.

## When to change tools

Move operations to a private shared task tool when several people need concurrent editing or the team repeatedly misses reminders. Preserve the IDs, evidence links, permissions and source archive. Migrate the master records once and retire the old board. Track a small weekly scorecard: open accepted actions, overdue real deadlines, unconfirmed ownership, available hours, funded workload and unresolved decisions. Do not use activity volume as proof of art sales or revenue.
