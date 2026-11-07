---
name: techstet
description: |
  Draft, edit, or review technical prose so it reads as written by a careful person for a specific reader, while keeping every defined term, modal, number, heading, label, and code span exactly as the source had them. Use for IT documents (ADRs, runbooks, design docs, governance and policy, RAPID, incident reports, READMEs, briefs, exec memos) and for technical book chapters. Use it whenever the user asks to make a draft clearer, less AI-sounding, more engaging, more human, tighter, or asks whether something reads as AI; whenever they ask to deslop, humanize, polish, or review technical writing; and whenever you are about to write more than a few paragraphs of technical prose yourself. Prefer it over generic humanizer or stop-slop skills for anything with defined terms, procedures, or decisions in it.
license: MIT
compatibility: claude-code codex-cli copilot-m365 cursor
metadata:
  version: "1.1.0"
  built-from: "humanizer 3.1 (blader), no-ai-slop (petergyang), stop-slop (hardikpandya), tagore 1.0, Rephrasy reverse-engineering 2026-11-07, Winston How to Speak and Sinek giver-mindset translations 2026-11-07"
---

# techstet

Technical prose has two ways to fail. It can read like a model wrote it: staged contrasts, triads, closers, inflated significance, bold labels on everything. Or it can be scrubbed clean and still say nothing a reader can act on. Most deslop tools fix the first and cause the second, and the paraphrase tools that promise to "humanize" also quietly change what the text means. This skill does both halves and then proves nothing was lost.

Three commitments drive everything below.

1. **Work on the whole document.** Terms, headings, and rhythm are document-level properties. A pass that sees one paragraph at a time renders the same term three ways and doubles the anaphora it was meant to remove. Read everything before editing anything.
2. **Meaning is fixed; wording is not.** Defined terms, modals (may, must, should, can, shall), numbers, dates, cross-references, headings, list labels, code, quotations, and deliberate fragments are invariants. An edit that touches one is a meaning change until the author says otherwise.
3. **Engagement comes from concreteness, not personality.** In a runbook or an ADR, "engaging" means the reader can see the thing: a worked example, a named failure, a sourced number, a decision stated with its consequence. Opinions and first person belong only where the genre and the author's sample allow them.

## Modes

Pick the mode from the request. When the user supplies text and says nothing else, use **edit**.

Load references in proportion to the job. For anything under about 1,000 words: `references/tells.md` and the matching section of `references/genres.md` are enough, plus `references/engagement.md` if you add anything. `references/preservation-gate.md` is for when you have no shell to run the script. `references/long-form.md` is for books and documents over about 5,000 words. Reading all five for a one-page ADR is wasted effort.

| Mode | What you return |
|---|---|
| **draft** | New prose from notes, a spec, or an outline, in the chosen genre, followed by the gate report. |
| **edit** | The edited text, a short **What changed** list, and the gate report. Minimum effective edit: leave strong sentences alone. |
| **detect** | Each tell found, with the quoted line and a one-line fix. No rewrite, no score, no verdict on whether a model wrote it. Named patterns are evidence; detectors guess. |
| **review** | The detect findings plus the scorecard in `references/engagement.md`, for a reviewer who will not apply changes. |

## Workflow

### 1. Fix the frame

Decide, and state in one line, three things before touching the text:

- **Genre.** One of: `adr`, `runbook`, `design-doc`, `policy`, `incident`, `readme`, `brief`, `book-chapter`, `blog`. Read the matching section of `references/genres.md`. The genre sets the voice, the allowed engagement moves, and any extra invariants. If you cannot tell, ask one question: who reads this and what should they do after?
- **Reader and payoff.** Name one reader by role ("the on-call engineer at 3 a.m.," "the VP who signs the matrix"), not "stakeholders." Write one line saying what that reader leaves with: one fact they lacked and one thing they can now do. Every later choice is tested against that line. A document written to be judged reads differently from one written to give the reader something, and readers can tell.
- **Voice source.** An author sample if one is given; otherwise the genre default. IT documents stay neutral, with "you" only in instructions. Book chapters take the author's voice from the sample or from the surrounding chapters. The sample overrides every tier 3 rule and the dash rule outright. It can also excuse a tier 1 or tier 2 pattern, but only for an instance that is demonstrably the author's habit in the sample and that carries information (a contrast that corrects a belief the reader holds, a fragment that lands a beat). Keep those, list them under "Left alone on purpose," and if the pattern runs more than a few times per chapter, ask the author whether to thin it. A sample never excuses chat residue, borrowed authority, or invented facts.
- **Invariants.** Build the term list before editing: every defined term, role name, body name, status value, and recurring phrase the document relies on. For a book, load the term ledger per `references/long-form.md`. Keep this list; the gate uses it.

### 2. Mark the tells

Read the whole text once and mark every pattern from `references/tells.md`, strongest first. The catalog is tiered: tier 1 patterns justify an edit on one sighting; tier 2 patterns need company before you act; tier 3 are style preferences the genre or sample can switch off. Mark at paragraph and section scale too: a contrast split across two sentences, three parallel examples, the same closer under every heading, every section ending on a summary line.

If the input is cut off mid-sentence or mid-definition, say so in the first line of What changed and work with what is there. Never complete a truncated sentence, definition, or list; a completion is an invention.

Do not mark deliberate fragments. Checklists, table cells, status enums, bullet labels, and changelog rows are fragments on purpose. A paraphraser given a fragment completes it and invents content to fill the gap; that is the single most damaging thing a rewrite can do to a technical document.

### 3. Remove, then add

Rewrite with both halves in mind:

- **Remove** the marked tells by stating the point directly. Delete a kicker; do not improve it. Replace a staged contrast with the claim. Merge a forced triad or develop its strongest item. Turn a labeled list into prose only when the labels carry no information; a list of real items stays a list.
- **Add** what the reader needs to act, from `references/engagement.md`: the concrete example, the named failure mode, the number with its source, the decision and what it costs, the reader task ("if X, do Y"), the one sentence that says why this section exists. Only add facts the source or the user supplied. If a paragraph needs a detail you do not have, write the simpler sentence or ask.

Do not paraphrase for its own sake. Changing "sets" to "defines" or "before" to "prior to" moves nothing for the reader and is exactly what a detector-evasion tool does. If a sentence has no tell and no missing concreteness, leave it.

### 4. Run the gate

Before delivering, diff the result against the source for every invariant. Use `scripts/preservation_check.py` when you have a shell:

```
python3 <skill-dir>/scripts/preservation_check.py original.md edited.md --terms terms.txt --genre <genre>
```

`<skill-dir>` is the folder this SKILL.md lives in. Without a shell, run the checklist in `references/preservation-gate.md` by hand. For each flag: revert it, or state in **What changed** why it is intended. A gate you did not run is not a gate; "I checked and it looks fine" is the failure mode this step exists to catch.

### 5. Deliver

Return what the mode asks for. **What changed** follows this shape, kept short:

```
Genre: <genre>. Voice: <sample | genre default>. Invariants held: <the ones that mattered>.
Removed: <tell, where, one line each>
Added: <move, where> or "none: the source supplies no facts for one; the strongest candidate is <X>"
Left alone on purpose: <anything a reader might expect changed, with the reason>
Gate: <n> flags; <each: revert | justify (why) | ask (question)>
Ask the author: <open questions, if any>
```

When the source has nothing concrete to add, say so and name what would strengthen it; do not invent the example. For a book chapter, add the long-form notes from `references/long-form.md` (voice card, ledger updates, callbacks checked, rhythm).

## Rules that override the usual deslop advice

These exist because the common rules were written for essays and break technical prose.

- **Keep adverbs that carry logic.** "Only," "separately," "retroactively," "not" are load-bearing in a procedure. Cut adverbs that add emphasis without information (actually, truly, genuinely, simply, really).
- **Keep passive voice when the actor is unknown or irrelevant.** "The certificate is rotated every 90 days" is fine. Convert to active when the actor matters and is missing ("Mistakes were made").
- **Keep every hedge that reports real uncertainty and every modal as written.** "May" is permission; "might" is possibility; "should" is advice; "must" is obligation. These are the content of a policy. Remove only stacked qualifiers that repair an earlier overstatement.
- **Keep three items when the meaning has three.** The tell is forcing three; a checklist with three steps is not a tell.
- **Keep headings that start with How, What, When.** "How an ADR reaches its decider" is a good heading.
- **Do not add "you," contractions, "here," or "however" to a neutral document to make it sound human.** That is a register leak, not voice.
- **Do not raise or lower register by synonym.** Precise beats plain and plain beats fancy, but the right word stays the right word.
- **Never expand a fragment into a sentence.**
- **Never add a fact, name, number, date, quote, citation, or ranking** that the source or the user did not supply. Fiction is the only exemption, and it is not this skill's job.

## Long-form work

For a book chapter or any document over roughly 5,000 words, read `references/long-form.md` before step 1. It covers the term ledger, the author voice sample, section and chapter rhythm (every section opening with a scene, every chapter ending on a lesson), cross-chapter callbacks, and how to work chapter by chapter without losing document-level consistency.

## What to leave alone

Quotations, titles, proper names, and passages that discuss a phrase rather than use it. Text in code blocks, inline code, commands, paths, YAML, link targets, and tables. Anything written before November 2022. An unusual specific detail, a mixed feeling the author states, a first-person choice the author can explain, a parenthetical aside that sounds like the author. People who judge "AI-sounding" by feel do little better than chance; several tells together are the evidence, and one tell in a careful writer's text is often a choice.
