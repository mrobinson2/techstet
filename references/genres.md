# Genres: voice, moves, and invariants by document type

Pick one genre in step 1 and apply its section. Common invariants apply to every genre: defined terms, role and body names, modals, numbers and dates, cross-references, headings, list labels, status values, code, quotations, deliberate fragments.

**Lead with the problem or lead with the steps.** Briefs, ADR context sections, design docs, and policy purpose sections open with the problem and the cost of not solving it, because the reader does not yet share the reason. Runbooks, READMEs, and reference sections open with the steps or the facts, because the reader already has the reason and came for the how. The "why" in technical prose is a concrete problem with a consequence, never a belief statement ("we believe every team deserves"), which reads as marketing.

## adr (architecture decision record)

- **Voice:** neutral, third person. "We" is allowed for the deciding team if the template uses it.
- **Structure:** context, decision, consequences, options considered. Do not reorder the template.
- **Extra invariants:** status value (proposed, accepted, superseded), option labels (A, B, C), the decision sentence itself. The decision sentence may be tightened but its modal and scope may not change.
- **Moves:** decision with its cost; worked example of the decision applied; boundary; the reader's objection answered in the options section.
- **Tells to expect:** T5 straw-man alternatives, T6 inflated consequences, T9 three options when there were two, T17 "it is important to note."

## runbook / procedure

- **Voice:** instructional second person, imperative. "You" and "run," "check," "page" are correct here.
- **Structure:** preconditions, steps, verification, rollback. Numbered steps stay numbered.
- **Extra invariants:** step order, commands, flags, paths, thresholds, timeouts, role names in escalation, every "only," "before," "after," "unless."
- **Moves:** sequence with a consequence; named failure at the step where it happens; reader task phrased as a condition; verification after every change.
- **Allowed:** fragments in steps, labeled lists, bold on warnings, passive where the actor is the system.
- **Tells to expect:** T10 every step starting with "Ensure," T2 a lesson after the steps, T19 bold on everything.

## design-doc

- **Voice:** neutral; "we" for the authoring team.
- **Structure:** problem, goals and non-goals, design, alternatives, risks, open questions.
- **Extra invariants:** component names, interface names, SLO numbers, capacity figures, the goals and non-goals lists.
- **Moves:** worked example through the design; number with its source; decision with its cost in alternatives; boundary in non-goals.
- **Tells to expect:** T6 significance, T13 "leverages," T15 vocabulary, T16 "tied to."

## policy / governance / standard (includes RAPID, decision rights, guiding principles)

- **Voice:** neutral, third person, role names as subjects. No "you," no contractions, no first person.
- **Structure:** purpose, scope, definitions, rules, roles, exceptions, review. Keep definitions verbatim.
- **Extra invariants:** every modal (may, must, should, shall, can, might) is normative content; every defined term; role and body names; escalation triggers; thresholds; "proposed" and "draft" markers; numbered rules.
- **Moves:** worked example per rule or level; the one-sentence why for a section; boundary; before-and-after for a changed rule.
- **Allowed:** passive voice for rules whose actor is any role ("Decisions are recorded in the register"); tables; fragments in matrices and changelogs.
- **Tells to expect:** T6, T8 method narration in a changelog, T16, T17. Watch for register leaks introduced by an earlier tool: contractions, "you," "however."

## incident report / postmortem

- **Voice:** neutral, past tense, blameless. Role names, not people's names, unless the template says otherwise.
- **Extra invariants:** timeline timestamps, durations, impact numbers, action items with owners and dates, severity label.
- **Moves:** named failure (this is the whole document); sequence with a consequence; number with its source; decision with its cost in action items.
- **Tells to expect:** T6 "a valuable learning opportunity," T24 recap endings, T12 "the outage emerged."

## readme / developer doc

- **Voice:** instructional second person for setup; neutral for reference.
- **Extra invariants:** commands, versions, flags, env var names, file paths, code blocks, link targets.
- **Moves:** worked example (the quickstart is one); boundary (what this does not do); named failure in troubleshooting.
- **Allowed:** fragments, labeled lists, bold on commands and warnings.
- **Tells to expect:** T4 "Let's get started," T8 "This README is organized," T19.

## brief / exec memo / one-pager

- **Voice:** neutral with a stance allowed once, if the author takes one. "We recommend" is fine.
- **Structure:** decision requested, recommendation, reasoning, cost, risk, ask. Lead with the ask.
- **Extra invariants:** the recommendation sentence, every figure, deadlines, named decision-makers.
- **Moves:** decision with its cost; number with its source; stance (once); boundary.
- **Tells to expect:** T1 contrasts, T3 sayings, T9 three-point summaries, T24.

## book-chapter

- **Voice:** the author's. Take it from the sample or the surrounding chapters: sentence length, contraction rate, second person, use of scenes, whether chapters end on a lesson. The sample overrides every tier 3 rule and the dash rule.
- **Structure:** whatever the book's chapter template is. Keep heading levels and the callback lines to other chapters.
- **Extra invariants:** the term ledger (see `long-form.md`), canon definitions, chapter cross-references, recurring examples and named systems, exercise and prompt labels, the author's deliberate repetitions.
- **Moves:** scene (if the sample uses them); worked example; named failure; stance where the author already took one; rhythm at section scale.
- **Tells to expect:** T1, T2, T9 at paragraph scale, uniform paragraph length, every section ending on a quotable line, "not X but Y" scaffolding across sections.
- **Do not:** add first person the author did not use; change a term the ledger locks; vary a term for style; smooth a deliberately short sentence; add "actually," "just," "still."

## blog / public post (fallback)

- **Voice:** the author's, or plain and direct. Opinions and first person allowed.
- **Moves:** all of them, including stance.
- **Tells to expect:** all of them. This is the genre the source catalogs were written for; use them freely.
