# Writing Without AI Slop: A Guide for Agents

This guide is for any agent that writes copy a person will read, grade or act on: slide text, reports,
memos, policies, emails, pull request descriptions, dashboard labels and webpage copy. It stands on its
own. You need no other file to follow it.

AI slop is wording that a fluent human editor would change because the reader stumbles on it, learns less
than the words promise, or reads past words that do nothing. Graders look for eleven named faults. Five
are judgements about the wording. Six are mechanical marks that graders flag on sight. This guide gives
the test for each, the forms it takes, what passes, and the fix.

The one question behind all eleven: could a careful writer rewrite this significantly better?

## The method in brief

1. Find out who reads the text and what they need to do with it.
2. Write the plain version first. Lead with the answer, the decision or the finding.
3. Run the six mechanical checks on the raw text (section 2).
4. Run the five judgement tests on every sentence, title and label (section 3).
5. Run the final checklist (section 7) before you hand the text over.

---

## 1. Habits of clean writing

These habits prevent most slop before it appears.

- **Name the actor.** Every verb needs a subject who does the action. Write "The finance team approved
  the budget". "The budget was approved" hides who acted.
- **Name the thing.** Write the product, the figure, the team, the date. A reader should be able to
  check every claim against something specific.
- **Lead with the point.** The first sentence carries the answer or the decision. Setup, context and
  caveats come after it, if at all.
- **Use the plain word.** "Use", "help", "show", "start", "increase". A long word earns its place only
  when it is the precise technical term.
- **State figures exactly.** "42%", "RMB 25–30m", "more than 40 deals". Where a figure is uncertain, give
  the source and the reason.
- **One idea per sentence.** Ten to twenty words is a good length. Split a sentence that needs a
  semicolon or a dash to hold together.
- **Match the structure to the content.** A two-sentence answer needs no headings. A reference document
  with repeated sections needs them.
- **Write titles that state the finding or name the content.** "Revenue grew 12% on data-centre demand"
  or "Q3 revenue". A title never gives the reader an order.
- **Stop when the point is made.** No recap, no closing flourish, no outlook paragraph the content did not
  ask for.

---

## 2. The six mechanical faults

Graders treat these as rules. Every instance counts, however well the rest of the sentence reads. Read
the raw text for them, since a rendered page can hide a dash or an arrow.

### 2.1 Punctuation

**The marks:** em dash `—`, semicolon `;`, an in-line dot separator `•` `·`, a vertical bar `|` used as a
separator, and any arrow `→` `←` `↑` `↓` `↗` `↘` `⇒` `->` `=>`. A spaced en dash between words
(`word – word`), a spaced hyphen between clauses (`plan - it works`) and a double hyphen `--` all count as
em dashes. **Colon stacking** also counts: two colons in one sentence, or a run of "Label: clause"
sentences used for rhythm.

**What passes:** a hyphen inside a compound word ("two-year"). An en dash inside a numeric or date range
("2021–2024", "RMB 5–9m") or as a minus sign. A single colon introducing a list, a label or an
explanation. A bullet character that starts a list line. Any mark inside code, a file path or a command.

| Slop | Clean |
|---|---|
| "Sales fell within weeks; the recovery took a year." | "Sales fell within weeks. The recovery took a year." |
| "Isolate what changed – and what stayed in place – under the new rule." | "List what the new rule changed. Then list what it kept." |
| "Strategy \| Execution \| Impact" | "Strategy, execution and results" or three separate headings |
| "Crisis-led plan → one trusted plan" | "The team replaced the crisis plan with a single agreed plan." |
| "Universities: reinforce guidance. Students: reduce social activity." | "Universities should repeat the guidance. Students should cut back on social events." |

### 2.2 "It's not X, it's Y"

**The test:** one subject gets two competing answers, one rejected and one asserted, in either order and
even across a full stop. The rejected half is usually a foil that nobody proposed.

**Every form counts:** "X is not A. It is B." "isn't just A, it's B". "B, not A". "not A but B". "B rather
than A". "B instead of A". "less A, more B". "Do B, not A". "The question isn't A, it's B."

**What passes:** a plain negation with nothing asserted in its place ("The report does not cover Q4"). A
contrast between two different subjects ("Revenue rose and costs did not"). A scope limit, where the
negated half is a stronger version of the asserted half ("supports a feasibility case, but not a full
investment decision").

| Slop | Clean |
|---|---|
| "This isn't just a calendar. It's a gateway to a more intentional life." | "The calendar shows each week's deadlines on one screen." |
| "Data access is not a background detail. It's the heart of the user experience." | "Users spend most of their session finding and opening data." |
| "Growth depends on 12 new multi-site buyers, not on walk-in trade." | "Growth depends on 12 new multi-site buyers." |
| "The right target is controlled automation rather than fully hands-off processing." | "The target is automation with a person approving each batch." |

State Y alone. If the contrast with X genuinely matters, give X its own sentence with its own reason.

### 2.3 Passive voice

**The test:** the subject receives the action, and the actor comes after the verb or never appears. Add
"by someone" after the verb. If that reads naturally, the clause is passive.

**Forms that count:** "was delayed", "has been verified", "were provided", "should be treated as", "is
expected to", "it is estimated that". Elliptical passives with "be" dropped also count: "Decision
requested", "Approval required", "no overhead assumed", "if approved", "Data updated just now". So do
passive gerunds ("him being traded") and passives in technical prose ("The certificate was marked as
replaced").

**What passes:** a participle that only describes a noun inside a sentence with another main verb
("modelled EBITDA", "the 45 migrated buyers", "cash invested by Year 1"). An adjective describing a
state, where "by someone" sounds wrong ("The market is concentrated", "The office is based in Shenzhen").

| Slop | Clean |
|---|---|
| "Issuance was driven by repricings." | "Repricings drove issuance." |
| "None of those inputs has been verified." | "No one has verified those inputs." |
| "Decision requested." | "Management asks the board to decide." |
| "The identified certificate was already marked as replaced." | "The system has already marked the certificate as replaced." |
| "Stakeholders should be informed of the change." | "The project lead will email the change to the three regional heads." |

When the source never names the actor, name the one the context implies.

### 2.4 Imperative title

**The test:** a title, heading, subheading, section label, chart title, card heading, column head or bold
lead-in whose main clause opens with a verb addressed to the reader. The advice may be sound. The form
still fails.

**Forms that count:** "Define the scope before planning", "Meet the team", "Know your numbers", "Don't
over-hedge", "Let's review the plan", "Unlock more insights", and a command after a label colon
("Pricing: hold the line").

**What passes:** a noun title ("Plan overview"), a gerund title ("Building the plan"), a question, a "How
to" title, and any imperative in body text or a bullet ("Approve the pilot in March"). Buttons and links
on a webpage ("Continue", "Run code") are controls, so they pass.

| Slop | Clean |
|---|---|
| "Screen the energy credit before the tariff" | "The energy credit decides the comparison" |
| "Meet the team" | "Project team" |
| "Continue learning" (as a section heading) | "Your next lessons" |

### 2.5 Slogan-like phrasing

**The test:** two questions. Is the line built on cadence: a fragment, a triad, a set formula, a staged
reveal? Does it contain nothing a reader could check: no figure, named item, named action or named risk?
Two yeses make a slogan.

**Forms that count:**

- Tagline fragments: "One team. One vision. Limitless possibilities."
- Two-subject contrast fragments: "Pipeline is flat. Spend isn't."
- Staged colon reveals: "Different sectors, same logic: reduce optional contact."
- Triads of abstractions: "faster, smarter and more intuitive", "scale, speed and certainty".
- Stock formulas: "not only saves time, but also transforms how teams collaborate".
- Transition slogans: "From paper-bound practicals to a shared digital workspace".
- Buzzword claims: "unlocks value, fosters alignment and drives meaningful impact".
- A short closer that only relabels: "That's the unlock." "The math is simple."
- A title of two clipped noun phrases joined by a comma: "Two active pilots, complementary learning
  contexts".

**What passes:** a list whose items carry figures or named actions. A short sentence that points at
something specific already stated ("That is the main delivery risk", after the text names the risk).

| Slop | Clean |
|---|---|
| "Pipeline is flat. Spend isn't." | "Pipeline held at $4.2m while spend rose 12%." |
| "From paper-bound practicals to a shared digital workspace" | "Students now record lab results in one shared online notebook." |
| "Two active pilots, complementary learning contexts" | "Pilots in Austria and Japan test different customer groups" |

### 2.6 Illustrative hedging

**The test:** read every number, range, chart caption and figure label. Any word or symbol that places a
figure near a value, or tells the reader the chart is only approximate, fails.

**Forms that count:** about, around, roughly, approximately, approx., circa, c., ~, ≈, almost, nearly,
near, close to, some ("some 40 deals"), just over, just under, upwards of, in the region of, on the order
of, ballpark. Labels that disown a figure: "illustrative", "Illustration:", "indicative", "directional",
"for illustration only", "for discussion only", "for reference only", "sample", "placeholder", "dummy
data". Softeners on a trend: "roughly flat", "broadly stable". A hedge on exact arithmetic still fails:
"~RMB 1.3m" for 20% of 6.5m.

**What passes:** an exact figure or a plain range. A real bound ("more than 40", "at least 12", "under
1%"). A source label ("projected", "modelled", "forecast", "reported", "budgeted"). A statistic name ("on
average", "median"). A measured margin ("±2 pts at 95% confidence"). An uncertainty the text explains
("preliminary because two regions have not reported").

| Slop | Clean |
|---|---|
| "Roughly 40% of users churn in month one." | "41% of users churn in month one." |
| "Almost half of respondents agreed." | "47% of respondents agreed." |
| "Illustrative normalized series, for discussion only" | "Index, January 2024 = 100. Source: company filings." |
| "Revenue stayed broadly stable." | "Revenue moved between $8.1m and $8.4m each quarter." |

If you do not have the exact figure, say where the uncertainty comes from.

---

## 3. The five judgement faults

These need judgement. Flag your own wording when a rewrite would be clearly better, and leave a wording
preference alone when the rewrite is no clearer. Length alone never makes a sentence slop. Each test
applies at three levels: a single word, a phrase inside a sentence, and a label such as a heading,
column head, tag or caption.

The fix tells you which fault you have:

| The fix is | The fault is |
|---|---|
| Add, move or swap a few words | Awkward/Unnatural |
| Say it in plainer, fewer words | Excessive/Flowery |
| Replace it with something specific | Vague/Empty |
| Delete it | Unnecessary |
| Rewrite it so it has one meaning | Illogical |

### 3.1 Awkward/Unnatural

**The test:** read it aloud as a colleague would say it. The meaning comes through, but no fluent writer
would put the words together this way.

**Common forms:**

- A wrong word the reader corrects on sight: "Contributions waned" for "decreased".
- A noun stack with the linking words dropped: "five-question pulse", "verbatim follow-up", "default
  zero-case checks".
- A noun forced into an adjective slot: "POST-COVID CONSUMER", "value-led".
- A modifier that lands on the wrong noun.
- An inanimate subject doing what only a person does: "their contexts broaden what the pilot can learn".
- A maths symbol inside a running sentence: "contribution = 16% of RMB 5.0m".
- Syntax inversion: "Only by working with the business can treasurers understand their risks."
- A coined noun for a code identifier: "nestedness" for `is_nested`.

| Slop | Clean |
|---|---|
| "A five-question pulse uses 0-10 scores and one verbatim follow-up." | "The five-question survey uses a 0-10 scale and one open-ended question." |
| "Consumers are thinking harder before they buy." | "Consumers have become more deliberate about purchases." |
| "Proceed only when five readiness gates are green." | "Proceed only when the deal meets all five criteria." |
| "The event ceiling remains anchored to a headcount cap and a percentage cap." | "Events have two limits: a headcount and a percentage of capacity." |

### 3.2 Excessive/Flowery

**The test:** write the plainest version that keeps every fact. If it is shorter or plainer and loses
nothing, the original was excessive. A real point sits under the dressing.

**Common forms:**

- Inflated vocabulary for a plain idea: "holistically cultivate a multifaceted ecosystem of synergistic
  capabilities".
- Two or more AI-associated words in one passage: delve, pivotal, robust, tapestry, underscore,
  showcase, foster, intricate, landscape, testament, vibrant, seamless, leverage, holistic.
- Promotional adjectives on a plain fact: vibrant, rich, renowned, groundbreaking, nestled.
- A modifier the noun already implies: "next-generation flagship smartphones".
- Stacked jargon: "pressurized metered-dose inhaler simulation capabilities".
- Stacked hedges: "may potentially be worth considering whether the team could possibly".
- Bureaucratic padding: "at this point in time it would be advisable to begin the process of".
- A list that keeps going after the point is made.

| Slop | Clean |
|---|---|
| "Catalyzing Transformative Excellence" | "Performance improvement" |
| "A structurally lower commute base" | "A permanent drop in commuting" |
| "It may potentially be worth considering whether the team could possibly delay the launch." | "The team could delay the launch." |
| "At this point in time, it would be advisable to begin reviewing the draft." | "The team should review the draft now." |

### 3.3 Vague/Empty

**The test:** ask which, what, who and how much. If the text cannot answer, the wording is vague. A
second test: would the line sit unchanged in a document about something else?

**Common forms:**

- An abstraction that names no product, metric or outcome: "broad-based usage", "sustain the core",
  "Strategic Value Drivers".
- A term the text never defines: "the same agentic loop", "exit economics", "progressive promotion".
- A phrase that stops before its object: "Municipal contracts support visibility." Visibility of what?
- A pronoun with no clear referent: "It holds the economics flat" after a five-item list.
- A derived figure with its steps unnamed: "$1.8m cash flow after adjustments" when the reader cannot
  see what took $2.4m to $1.8m.
- A vague authority: "experts argue", "research consistently shows", "observers note".
- Synthetic balance: "offers flexibility, but also presents unique challenges".
- Process in place of a reason: "after several rounds of review, we aligned on the next phase".
- A figurative claim: "Data Center is doing the heavy lifting".
- A heading cut down until it loses its subject: "Where to draw the line".
- A vague quantity where a number belongs: "a handful", "dozens", "significant", "double-digit".

| Slop | Clean |
|---|---|
| "Revenue $2.68B (+26%), with broad-based usage across products." | "Revenue $2.68B (+26%), led by Search and Cloud." |
| "Data Center is doing the heavy lifting." | "Data centres supplied most of the revenue growth." |
| "This represents a profound shift." | "Online orders rose from 12% to 31% of sales in two years." |
| "After several rounds of review, we aligned on the next phase." | "We chose the cheaper vendor because it can deliver by March." |

### 3.4 Unnecessary

**The test:** delete it and reread. If the meaning survives intact, the words were unnecessary.

**Common forms:**

- Filler labels: "A NEW ERA", "MOMENTUM AHEAD", "UNLOCKING POTENTIAL".
- Staging lead-ins: "Why it matters:", "The key takeaway:", "Bottom line:". "Bottom line" always counts.
- A label that repeats the title: "BOTH ACTIVE PILOTS" under a title naming two active pilots.
- A tacked-on benefit: "ensuring a seamless user experience", "to reveal what matters most".
- A word that repeats its neighbour: "practical consumer needs", "defined non-GAAP adjustments".
- Generic scene-setting: "In today's fast-paced digital landscape..."
- Restating the request: "When it comes to improving onboarding, there are several strategies."
- Meta-announcements: "Below is a polished and comprehensive rewrite tailored to your needs."
- Canned empathy: "I completely understand how frustrating this must feel."
- Redundant conclusions and canned endings: "In conclusion, these strategies can help organizations
  achieve their goals."
- Bold-label bullets that add nothing: a run of "**Label:** explanation" lines.
- More headings and bullets than the content needs.

**What passes:** section headers that help navigation, framing that narrows scope ("This memo covers the
two launch decisions due Friday"), and a qualifier that changes the claim ("alone", "annualized").

### 3.5 Illogical

**The test:** restate the wording as one plain fact. If you must choose between two readings, or the words
cannot be true together, the wording is illogical.

**Common forms:**

- Two readings: "17 January transactions" can mean deals dated 17 January or deals made in January.
- A contradiction inside the words: "Revenue Growth Decline Expansion".
- A word that makes the claim impossible: "Test, learn and scale the most promising ideas" (an idea
  cannot be "learned" here).
- A pronoun pointing at the wrong item.
- One label meaning two things on the same page: "Total sales" for a unit count and for revenue.
- A claim cut down until it asserts more than the content supports: "When faster shipping drives growth"
  for "When faster shipping drives growth rather than only raising costs".
- Figures in the same text that contradict each other.

| Slop | Clean |
|---|---|
| "Test, learn, and scale the most promising ideas" | "Develop, test and scale the most promising ideas" |
| "Transit & ground passenger jobs" | "Transit and passenger transport jobs" |
| "79% Transit use back to pre-pandemic" | "Transit use has recovered to 79% of its 2019 level" |

---

## 4. Special cases

### Technical content

- File paths, commands, flags, API names, functions, variables, config keys and error codes are never
  slop, however unfamiliar. Marks inside them are syntax: the `|` in a pipe, the `->` in a type
  signature, the `;` ending a statement.
- The prose around an identifier gets the full set of tests. Replace the identifier with "X" in your head
  and reread the sentence. If it still stalls, inflates or says nothing, fix the prose.
- Pull request and commit text hides passives. Ask who acted for every verb. "The cache was invalidated"
  becomes "The handler now invalidates the cache".
- A term the reader's own request introduced counts as defined for that reader.

### Spoken dialogue and author voice

- Speech has its own rules. Filler words, false starts and a `--` for a speaker breaking off are natural.
- Fix only wording that is genuinely wrong: a tense clash, two sentences fused together, a missing object.
- When you write in someone's voice, keep their asides and humour. The six mechanical faults still apply.

### Charts, tables and dashboards

- Captions, axis titles and legends follow the hedging rule. State the unit and the source.
- Trend arrows such as "↗ 12.8%" count as punctuation. Write "+12.8%".
- Status lines such as "Payment completed" or "Data updated just now" are passive. Name the actor or the
  time: "Last sync 09:14".
- A table cell or a standalone formula line is not a sentence, so "=" and terse noun phrases pass there.

### Audience

Write at the reader's level. For a lay reader, an unexplained term of art is a fault even when it is
correct. For a specialist, the standard term of the field is the plain word.

---

## 5. Words and phrases to remove on sight

| Remove | Use instead |
|---|---|
| delve, delve into | look at, examine, or say the finding |
| leverage | use |
| robust | name the property: tested, redundant, accurate |
| seamless, seamlessly | say what the user no longer has to do |
| holistic, holistically | name the parts covered |
| pivotal, crucial, critical (as filler) | say what depends on it |
| landscape, ecosystem, tapestry | market, set of tools, or the actual list |
| foster, cultivate | build, encourage, or the actual action |
| unlock, unlocking value | name the result |
| drive, drives impact | name the cause and effect |
| underscore, showcase, highlight (as filler) | show, or state the point |
| testament to | shows |
| in today's fast-paced world | delete |
| it's worth noting that | delete |
| bottom line, key takeaway, why it matters | delete and state the point |
| in conclusion | delete |
| about, around, roughly, approximately, ~ | the exact figure or a real bound |

---

## 6. Self-check commands

Run this on the finished text file before handing it over. Every hit needs a look. A hit inside code, a
numeric range or a direct quotation can stay.

```bash
# Punctuation marks
grep -nE '—|;|•|·|\||→|←|↑|↓|↗|↘|⇒|->|=>| – | - |--' draft.md

# Hedges on figures
grep -niE '\b(about|around|roughly|approximately|approx\.|circa|almost|nearly|close to|just over|just under|in the region of|illustrative|indicative|directional|for discussion only|for reference only|placeholder)\b|~|≈' draft.md

# Contrast framing
grep -niE "\bnot (just|only|merely)\b|isn't|is not|rather than|instead of|, not " draft.md

# Passive markers
grep -niE '\b(is|are|was|were|be|been|being|has been|have been)\s+\w+ed\b|\b(requested|required|assumed|completed|updated|provided)\b\.?$' draft.md

# AI vocabulary and staging phrases
grep -niE '\b(delve|pivotal|robust|tapestry|underscore|showcase|foster|intricate|landscape|testament|vibrant|seamless|leverage|holistic|unlock|bottom line|key takeaway|why it matters|in conclusion|in today)\b' draft.md
```

Then read every title and heading on its own and check its first word. A verb aimed at the reader means
an imperative title.

---

## 7. Final checklist

Tick every line before delivery.

**Mechanical faults**

- [ ] No em dash, semicolon, in-line dot, vertical bar or arrow outside code and numeric ranges.
- [ ] No sentence with two colons and no run of "Label: clause" sentences.
- [ ] No sentence that rejects one answer to assert another for the same subject.
- [ ] Every verb has a named actor, including labels and status lines.
- [ ] No title, heading, chart title or card heading opens with a command.
- [ ] No tagline fragment, abstract triad, "From X to Y" or relabelling closer.
- [ ] Every figure is exact, bounded or sourced, with no approximating word.

**Judgement faults**

- [ ] Every sentence reads naturally aloud.
- [ ] No sentence has a plainer version that keeps every fact.
- [ ] Every claim answers which, what, who and how much.
- [ ] Deleting any phrase would lose meaning.
- [ ] Every sentence has one reading.

**Shape**

- [ ] The first sentence carries the answer or decision.
- [ ] No scene-setting, meta-announcement, canned empathy or recap.
- [ ] The structure is the lightest one the reader needs.
- [ ] Terms suit the reader, and the text defines any term the reader may not know.

## 8. A worked rewrite

**Before:**

> **Why it matters:** In today's rapidly evolving landscape, our new platform isn't just a tool — it's a
> pivotal enabler of seamless collaboration. Adoption was driven by roughly 40% of teams; results have
> been transformative. Unlock your team's potential.

**Faults:** a staging lead-in, generic scene-setting, "It's not X, it's Y", an em dash, an AI vocabulary
cluster, a passive, a hedge on a figure, a semicolon, a vague claim, and a slogan closing on a command.

**After:**

> 41% of teams adopted the platform in its first quarter. Teams that use it close support tickets in two
> days, down from five, because every reply now sits in one shared thread.

The rewrite names the figure, the period, the result and the reason. A reader can check every claim in
it.
