# Southwest Arts v1 interactive MVP scope

## Executive summary

Build one reviewable flow that helps a visitor plan a same-day art outing in Taos. From the existing Southwest Arts homepage, the visitor selects **Plan an art visit**, gives a starting point, time window and interests, and receives an editable itinerary with up to three stops. Each stop explains the art connection, shows estimated travel and visit time, and says what the visitor still needs to confirm. The visitor can swap a stop and see the rest of the plan adjust.

Start with a scripted interaction on the existing prototype and fictional records. That lets the team test whether conversation improves the visit before it pays for a model, gathers live availability or asks venues to integrate. The catalog remains available from the homepage. A successful test produces evidence for a build decision and gives the team a sample of what ongoing venue and editorial review would take.

The **interaction designer** owns the proposed conversation and result design. The **website builder** owns implementation and the review build. The **local arts reviewer**, if available, checks whether the sample route makes sense and identifies facts a public itinerary would need. The **project lead** confirms scope, capacity and the next decision. The proposed work window is **November 23–27, 2026**, with a review target of **November 30**. The first discussion confirms each role’s contribution and available time.

## 1. Product decision and audience

| Item | MVP definition |
|---|---|
| Visitor | A person already in or near central Taos who wants an art outing today and has a limited window. A first-time visitor can complete the task with only a starting landmark and a general interest. |
| Visitor problem | Individual listings may tell the visitor what exists. The visitor needs a manageable sequence that suits their taste and fits the time they have. |
| Hypothesis | Turning a short request into an editable route helps visitors choose a relevant art stop and act on it with fewer decisions. |
| Entry point | Add **Plan an art visit** alongside existing catalog browsing on the homepage. The itinerary opens a dedicated view within the existing website. |
| Deliverable | One interactive browser demo using sample records with a start, a recommended plan, an edit, and recovery when the requested plan cannot be produced. |
| Decision after review | Refine the interaction, authorize a separately scoped live-data pilot, or stop the itinerary work and retain catalog discovery. |

Use Taos as the only region in this review. Limit the sample itinerary to a central Taos route so travel assumptions can be inspected. The [project baseline](../PROJECT-BASELINE.md) governs regional scope and artist economics. The [AI specification](04-AI-CONCIERGE-AND-PLATFORM.md) covers the broader concierge. A production build needs its own review.

## 2. Scope and priorities

| Priority | Included work |
|---|---|
| Required | Homepage entry and return to browse. A suggested starter prompt, an editable brief, one clarifying question when essential information is missing, and an itinerary with a list and map. One supported swap followed by recalculation. Clear simulated data and availability labels. Manual starting-point entry, mobile and keyboard use, and recovery from no fit. |
| If the required flow passes | Try an additional supported interest or time window. Compare an alternate result layout or a lightweight map enhancement using the same fixtures. |
| After a separate review | Model API and real-time geolocation, geocoding and routing, provider-confirmed inventory, saved plans and accounts, partner booking and ticketing, payments, pricing tests, editorial publishing and expansion into additional regions. Each requires its own scope, owner and evidence. |

Use sample data and deterministic responses for the MVP. A small set of recognized phrases can fill the brief. Offer visible controls as a reliable way to correct or complete it. Mark the interaction as a **prototype with sample data** at entry and on the result. Stay with the existing catalog and design system so the review isolates the new visitor task.

## 3. Visitor flow

1. **Enter.** The homepage offers **Browse art** and **Plan an art visit**. The planner opens with one example request and a plain invitation to describe the outing.
2. **Describe.** The visitor can type, “I’m near Taos Plaza, I have three hours, and I’d like to see ceramics.” The planner shows which inputs it used. If the outing lacks a start time or origin, ask for the missing input. A small form lets visitors fill in or correct the brief directly.
3. **Confirm the brief.** Show the starting landmark, start time, time limit, art interests, and optional budget or mobility preference. The visitor can edit a field without restarting. Use Taos local time. Keep the location field usable without requesting device permission.
4. **Read the plan.** Show the art-led sequence in a numbered map and ordered list. Each stop has a reason to go, proposed time and dwell, travel from the previous point, any access note, and its verification status. Show the calculated end time and remaining buffer.
5. **Revise.** The visitor can select **Swap this stop** or use the supported prompt “Swap the second stop.” Offer a feasible replacement if one exists. Recompute timing, update map and list together, and show what changed. Preserve the other stops where their time windows still fit. Offer undo.
6. **Recover.** If a stop is unavailable, a route overruns the limit, or no replacement fits, explain the specific conflict. Offer a shorter route or one constraint the visitor can relax. Keep a feasible prior plan visible while describing the failed edit. Give the visitor a route back to catalog browsing.
7. **Finish.** The visitor can follow the demo route summary and see what would need a venue check. Use sample action labels for fictional stops. Only a reviewed real record may carry a verified external venue link.

### Worked example

This fictional fixture demonstrates timing. All walking estimates and opening windows are inputs for the test.

| Segment | Prototype itinerary |
|---|---|
| Brief | Plaza starting point, 1:00–4:00 p.m., ceramics, walking |
| First stop | Walk 10 minutes. A ceramics exhibition from 1:10–1:55 p.m. |
| Second stop | Walk 15 minutes. A pottery process display from 2:10–2:55 p.m. |
| Third stop | Walk 10 minutes. An exhibition with related work from 3:05–3:35 p.m. |
| Finish | Walk 15 minutes to the Plaza. Return at 3:50 p.m. with a 10-minute buffer. |
| Revision | Swap the second stop for one with a later opening. Recompute travel, waiting time and the return. Offer a shorter valid route if the proposed replacement pushes the return past 4:00 p.m. |

## 4. Data, implementation and interaction rules

### Sample records

Start with **five to eight** fictional places or stops, including one closed case, one unknown availability case and one feasible alternate. Include an optional food or rest stop only if it supports the art outing. The demo needs enough candidate records to exercise selection and revisions.

| Record | Fields |
|---|---|
| Visitor brief | Starting landmark ID, start time, available minutes, interest tags, optional budget cap and optional mobility preference |
| Stop | Stable ID, title, category, short art connection, interest tags, sample coordinates, opening windows in America/Denver, dwell minutes, cost estimate or unknown, access note or unknown, availability status, source/check fields where applicable |
| Travel leg | Origin and destination IDs, mode, forecast or fixture minutes, and source/status. Include the final leg when a return is part of the brief. |
| Itinerary | Brief, ordered stop IDs, scheduled arrival and departure, travel legs, end time, buffer, and unresolved checks |
| Revision | Original plan, requested swap, proposed replacement or reason it failed, recomputed plan, and previous plan for undo |

Keep the sample source list with the fixtures. Mark each sample record as fictional. If a reviewer proposes a real record, obtain editorial clearance and a dated source for public-facing facts. Show published hours separately from appointment or inventory confirmation. An unknown price stays unknown. A stop with unknown hours can appear as an optional lead with a check required. Keep it outside the timed sequence. Use public locations and review cultural access before including a real stop.

### Build approach

- Work from the existing [website source repository](https://github.com/Suede0619/sw-arts-website) in a review branch or local preview. Preserve the prototype’s buildless structure, relative asset paths and existing navigation. Keep the design sketch shareable even if implementation slips.
- Keep interpretation, route validation and rendering separate enough to inspect. The interpreter maps the supported prompt or form to the brief. The planner uses approved fixture IDs, estimated legs and time windows. The renderer presents the same ordered data in the map and list.
- Check arrival and departure against each opening window. Include walking, dwell and wait time, plus the return when requested. Reject a timed result that exceeds the visitor’s window. Apply a stated budget cap to known costs and surface any unknown costs explicitly. Never count an unknown cost as free.
- Save only the current plan and undo state in the active browser session. Request no account, precise coordinates, contact information or payment. Use no external model, mapping or analytics calls for this review. Keep inputs and fixture data separate from any private source material.
- State what happened after an update. Keep labels and errors available to keyboard and screen-reader users. Move focus predictably, announce the revised itinerary without forcing focus, and make every map fact readable in the ordered list. Use text with status color and make primary controls usable on a phone.
- Keep the map schematic if that is enough to understand the sequence. A route line conveys stop order and demo geography. Turn-by-turn navigation and verified accessibility would require separate data.

## 5. Team and work packages

The roles below describe proposed work. Confirm the review owner and each person’s available time before estimating delivery. One person owns each output.

| ID | Owner | Work and handoff | Done when |
|---|---|---|---|
| M1 | Project lead | Run a short scope discussion. Confirm the visitor, one flow, each person’s time and expected handoff, and the review audience. | The team has a shared scope, owner for each output, and review date or asynchronous alternative. |
| M2 | Website builder | Supply the existing preview, starter prompt, fictional record set and one sample route. | The designer can start without collecting venue data or setting up the source repository. |
| M3 | Interaction designer | Sketch entry, conversation turns, editable brief, result and swap. Include one no-fit or unknown-availability state. Use annotated screens or an interactive sketch if time allows. | A reviewer can follow the happy path and explain what the user changes and what the assistant does. Copy and state changes are clear enough to implement. |
| M4 | Local arts reviewer, if available | Review stop types, art relevance, plausible timing, public access and any editorial permissions a real version would require. | The review identifies what to keep, change or check. If this review slips, use fictional records and record the real-world checks as open. |
| M5 | Website builder | Implement the agreed interaction and validate the planner, mobile layout, focus and existing catalog path. | The required scenarios below pass in the review build. |
| M6 | Website builder | Prepare a short demo, retain the test results and summarize friction, failures and effort. | The project lead has current evidence and the list of unresolved issues. |
| M7 | Project lead | Review the demo with the design and build roles and decide whether to refine it, scope a pilot or stop. | The decision, reason, owner and next review condition are recorded. |

The designer’s first deliverable is the interaction, especially the questions, what the result can claim and how visitors correct it. The builder takes that handoff into the website and owns implementation and technical choices. Editorial, newsletter and regional business contributors can review later when a defined question calls for them.

## 6. Timeline and dependencies

| Target, America/Denver | Work | Dependency and exit |
|---|---|---|
| Mon Nov 23 | Scope discussion, then share prototype link and sample brief. | M1 and M2. Agree which sketch or screens the designer wants to return and set a realistic time allowance. |
| Tue–Wed Nov 24–25 | Explore the conversation and result. Prepare fixtures and collect local feedback if available. | M3 and M4. Agree one flow and resolve which states the builder needs to support. |
| Thu–Fri Nov 26–27 | Use available time for wiring and self-review. A sketch-only walkthrough can serve as the first design review if capacity is limited. | M5. Implement once the flow has a clear handoff. Preserve the test cases if implementation moves to the following week. |
| Mon Nov 30 target | Walk through happy path, swap and no-fit case. Record decision and follow-up. | M6 and M7. Move the review if the team needs more time for a meaningful walkthrough. |

These dates reserve no time. Prepare the sample route in advance so exploratory design time goes to the conversation. Favor asynchronous feedback if participants cannot meet. Where design or build capacity is limited, preserve the core flow and defer optional variations.

## 7. Acceptance and review

### Required scenarios

| Scenario | Pass condition |
|---|---|
| Homepage | Both entry points are findable. A visitor can reach the planner and return to catalog browsing. |
| Suggested prompt | The ceramics example yields a three-hour brief and a coherent sample itinerary. The visitor can inspect and edit every field the plan used. |
| Manual brief | A visitor can enter a starting landmark and select time and interest with keyboard or touch. |
| Missing input | The interface asks for the missing essential detail or routes to the form. It retains the valid inputs already supplied. |
| Valid swap and undo | Swapping the second stop recalculates the ordered plan, leg timing and end time. Undo restores the previous plan. |
| Invalid swap and cutoff | The planner excludes closed stops and rejects an itinerary that overruns the return deadline. It offers a feasible shorter option or states why none fits. |
| Time and access labels | Every timed stop has an opening window in the fixture and a time estimate. The result distinguishes sample data from a venue confirmation. It surfaces unknown access or costs in text. |
| Map and list | Both show the same stops and sequence. The list supports the full task without using a map. |
| Mobile and keyboard | All controls, including swap, undo and return, are reachable. Focus stays visible, changes are announced and the page has no horizontal overflow at phone width. |
| System boundary | There are no external actions, paid calls, live bookings, secrets or personal records in the demo. Existing catalog navigation still works. |

In the website repository, run `npm run check` and `npm test` for implementation review. Cover the new planner’s happy path, revision and failure recovery. Walk through the demo manually on desktop and a phone viewport, including one keyboard-only run.

### What the review should learn

Ask **three to five** reviewers, if available, to start from the homepage, plan a three-hour outing and change one stop without coaching. Record completion, time to first usable plan, where help was needed, whether they understood what remained unconfirmed, and which stop they would act on. Log route or data errors separately from usability issues. Give reviewers the catalog path as a comparison when practical. Use a short local notes sheet and avoid collecting personal contact information.

The first iteration passes review when the required scenarios work and reviewers can explain how to use and verify the result. A small group can expose confusing interactions. Demand, willingness to pay and real venue feasibility need separate evidence. If the team later tests a live model, include response time, cost per usable itinerary, and human review minutes in that pilot.

## 8. Open decisions and next gate

| Decision | Evidence needed |
|---|---|
| Which interface pattern to keep | Compare how easily reviewers find the planner, complete a prompt, edit the brief and revise a stop. |
| Whether a model adds value | Identify requests that scripted input or ordinary controls cannot handle well. Compare grounding, constraint-following, latency, costs and review effort before choosing a provider. |
| Whether to use current venue data | Identify a responsible editor, permissioned sources, freshness rules, correction and withdrawal process, and an owner for public access checks. |
| Whether to publish a wider preview | Review content rights, simulated labels, deployment behavior and access with the project lead. Obtain separate approval for any funded or production service. |

The project lead should record the next decision with an owner. A live pilot needs approved sources, a way to manage stale data, an accepted operator, a defined budget and a separate review of any external integrations.
