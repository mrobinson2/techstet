# Long-form: books and documents over about 5,000 words

A chapter is edited one passage at a time but judged as a whole. Everything a paragraph-level pass gets wrong at book scale comes from losing that whole: the same term rendered three ways across chapters, every chapter opening with a scene, a callback to Chapter 4 that no longer matches what Chapter 4 says.

## 1. The term ledger

Keep a file per book: `terms.txt` for the gate, and a ledger with one row per locked definition.

| Term | Locked wording | Where defined | Variants to reject |
|---|---|---|---|
| agentic workflow | "a workflow in which a model chooses the next action inside limits a runtime enforces" | Ch 2, D3 | agent workflow, AI workflow |
| run state | ... | Ch 2 | run-state, state, session state |

Rules:
- A locked definition is quoted, not paraphrased, wherever it reappears.
- A term is never varied for style. Synonym cycling is a tell in essays and a defect in a book with a glossary.
- When the author changes a term, change the ledger first, then every chapter.
- The gate's `--terms` file is generated from the ledger, including the variants column so drifts are caught.

## 2. The author sample

Before editing any chapter, read a sample the author wrote without a model (or the chapters they have signed off). Record, in a short voice card kept with the ledger:

- Sentence length range and the typical short-long pattern
- Contraction rate (per 1,000 words) and whether second person is used
- Whether chapters open with a scene, a claim, or a question, and whether they end on a lesson
- Dash, parenthesis, and semicolon habits
- Recurring phrases the author owns (keep them) and recurring phrases that are tells (the author may still want them)
- First person: never, sparingly, or freely

The sample overrides every tier 3 rule in `tells.md` and the dash rule. Matching the author beats matching the catalog.

## 3. Section and chapter rhythm

After the sentence pass on a chapter, check the shapes the sentence pass cannot see:

- Do all sections open the same way? Vary one or two.
- Does every section end on a summary line or an aphorism? Keep at most one per chapter, where the author's sample does it.
- Are section lengths uniform? A short section next to a long one reads as intended; six equal sections read as generated.
- Does the chapter end the same way as the last three chapters?
- Is there one paragraph in the chapter under 20 words and one over 120? If not, the rhythm is metronomic.
- Count "not X but Y" across the chapter, not per paragraph. One is a choice; five is scaffolding.
- Count slogans and echo closes. At most one of each per chapter (see `engagement.md`, devices capped at one). A restatement of the chapter's idea at the end is allowed once, only when the author's sample ends chapters that way.
- Landmarks for re-entry. Readers of a long document skip. Each section opens so that someone landing there from the contents page knows what it covers and what it assumes, in one line, without a heading restated as a sentence (T24 in `tells.md`).

## 4. Cross-chapter consistency

- Every "as Chapter N showed" or "we return to this in Chapter N" must still be true after the edit. Keep a list of callbacks and check them.
- Recurring examples (a named system, a named team, a running scenario) keep the same name, the same facts, and the same tense.
- Exercise labels, prompt labels, figure and table numbers, and sidebars keep their format.
- Canon definitions appear verbatim where the book repeats them on purpose.

## 5. Working chapter by chapter

1. Load the ledger, the voice card, and the callback list.
2. Edit the chapter with the full workflow in SKILL.md.
3. Run the gate with the book's `terms.txt`.
4. Record ledger changes, new callbacks, and rhythm notes in the chapter's What changed.
5. Every five chapters, re-read the voice card against the edited chapters. Drift accumulates in the editor as well as the author.

## 6. What a book pass must not do

- Add first person, opinions, or "mixed feelings" the author did not write.
- Add "actually," "just," "still," "here's the thing."
- Join two short sentences the author wrote short.
- Split a long paragraph the author built on purpose.
- Replace a term the ledger locks, even with a clearer word. Propose it to the author instead.
- Invent a scene, a quote, a number, or a named person.
