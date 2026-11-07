# Engagement: what to add once the tells are gone

Removing tells produces clean prose. Clean prose that says nothing the reader can act on is its own failure, and the usual fix (opinions, first person, "let some mess in") is wrong for a runbook, an ADR, or a standards document. Engagement in technical writing is concreteness: the reader can see the thing, can tell what it costs, and knows what to do next.

Every move below adds only what the source or the user supplied. If the detail is missing, write the simpler sentence and tell the user what would make it stronger.

## The moves

| Move | What it looks like | Use it when |
|---|---|---|
| **Promise opening** | The first sentence or two say what the reader will be able to do or decide after reading: "After this section you can route any ADR to its decider without asking the council." | The document or section opens with background, a definition, or a run-up. Never with a joke, a rhetorical question, or "this document describes." |
| **Fence** | Name the neighbor concept the reader already knows and the one difference: "An agent is not a workflow. In a workflow the steps are fixed; an agent picks the next step." | A new term or idea is defined only from the inside. This is the legitimate form of "not X but Y": the negative half corrects a belief the reader holds. |
| **Honest gap** | Say what is unknown or unsourced in plain words: "Median time to approval is about two weeks; confirm from the ticket history before quoting it." | The draft hides a gap behind a hedge, a vague authority, or a confident number with no source. A stated gap builds credibility; a faked certainty is visible. |
| **Anchor visual** | One diagram or table that carries the idea, referenced from the prose, not repeated by it. | A routing rule, a decision matrix, or a sequence is explained in three paragraphs that a picture would replace. |
| **Worked example** | One real case traced through the rule: "A Level 2 ADR for the virtualization upgrade: the platform VP decides, application teams give input, the central function sees it in the register and makes no call-in." | A rule, matrix, or process has been stated abstractly. |
| **Named failure** | The specific way this goes wrong: "The last two outages came from a config pushed without the canary step." | A warning is phrased as "be careful" or "it is important to." |
| **Number with its source** | "Median time from request to approval was 14 days last quarter (ticket history, Q3)." | The text says "slow," "significant," "most," "often." |
| **Decision with its cost** | "We chose Key Vault. The cost is a second secrets store for the two teams already on HashiCorp." | A decision is stated without what it gives up. |
| **Reader task** | "If the alert fires twice in an hour, page the on-call lead, then run step 4." | The reader needs to act and the prose only describes. |
| **The one-sentence why** | "This section exists because teams were escalating decisions they were authorized to make." | A section's purpose is only implied by its heading. |
| **Before and after** | Two short versions of the same thing, old and new. | A change is described in the abstract. |
| **Boundary** | What is in and what is out, in one sentence each: "Covers new decisions only. Existing decisions are not backfilled." | Scope is implicit. |
| **Sequence with a consequence** | Not just the steps, but what each step changes: "After step 3 the register shows the ADR as ready for review, which opens the five-day call-in window." | A procedure reads like a list of verbs. |
| **The reader's objection, answered in full** | Name the real question a reader will have and answer it with a fact. | The text argues with no one (tell T5) but a real objection exists. |
| **Scene (books only)** | A short, specific moment the reader recognizes: the 3 a.m. page, the demo that worked once. | The chapter opens or turns on an abstraction. Only if the author's sample uses scenes. |
| **Stance (books and briefs only)** | The author's judgment, stated once and owned: "I would not run this without the canary." | The genre allows a point of view and the source expresses one. Never invent one. |

## Devices capped at one

Three devices from speaking craft work in writing when used once per chapter or document and read as a tell when used more.

- **Slogan.** One short memorable line tied to a concrete claim, placed with the promise, never as a closer. A slogan under every paragraph is T3.
- **Restatement.** One deliberate restatement of the central idea at chapter end, only when the author's sample does it. Per-section restatement is T2.
- **Echo close.** Revisit the opening image or example with what the reader now knows. Once per chapter.

## Rhythm as engagement

Readers stay with prose that moves. Three mechanical levers, none of which change meaning:

- **Sentence length.** Put a short sentence next to a long one on purpose. A procedure can be all short; an explanation should not be.
- **Paragraph length.** One-sentence paragraphs are allowed for a decision or a warning. Not for every paragraph.
- **Where the point sits.** Lead with the decision or the instruction. Put the reasoning after, and only the reasoning that would change whether the reader agrees.

## What not to add

- Opinions, humor, first person, or "mixed feelings" in an IT document.
- "You" in a policy or standard. Instructions take "you"; rules take the role name.
- A story or scene the author did not write.
- Any fact, number, name, date, or citation not in the source or the conversation.
- A better metaphor in place of a deleted one.

## Scorecard (review mode only)

Five questions, each answered with a number 1 to 5 and one sentence of evidence. Use it to tell a reviewer where to look, not as a gate.

| Dimension | Question |
|---|---|
| Clarity | Can a reader state the point of each section in one line? |
| Specificity | Does each claim name the thing, the number, or the case, or gesture at a category? |
| Fidelity | Did every defined term, modal, number, and heading survive unchanged? (From the gate.) |
| Rhythm | Do sentence and paragraph lengths vary, or is the text metronomic? |
| Reader fit | Is the voice the one the genre and the sample call for, with nothing leaked from a different register? |

Below 18 of 25, say which two dimensions to fix first.

In review mode also return a figures table: every number, percentage, date, and version in the text, with its source as the text gives it, and one of *sourced*, *unsourced*, *suspicious* (precise number, vague institution). The skill never invents a figure; this table catches the ones the draft inherited.
