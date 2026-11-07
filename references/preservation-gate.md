# Preservation gate: prove nothing was lost

Run after every edit or draft-from-source, before delivery. The gate exists because a rewrite that reads well can still have changed a modal, dropped a heading, rendered a term two ways, or invented a status value, and a reader-side review of the finished text will not notice. Two paraphrase runs on 2026-11-07 (a 9,000-word book sample and a 4,400-word governance draft) produced exactly those defects while reporting zero loss; mechanical checks caught 107 of 185 bad paragraphs the reviewers would otherwise have read.

With a shell: `python3 scripts/preservation_check.py original.md edited.md --terms terms.txt [--genre policy]`. It prints a report and exits non-zero on any flag. Without a shell, work through the table by hand against the source and record the result in **What changed**.

## Checks

| Check | Flag when | Resolution |
|---|---|---|
| Terms | Any term from the list appears fewer times in the edit, or a near-variant appears (decider → decision-maker, review → group, function → team). | Restore the term. Variation for style is never intended in technical prose. |
| Modals | A sentence's modal set changed: may ↔ might ↔ can ↔ should ↔ must ↔ shall; "only," "unless," "before," "after," "never" added or removed. | Restore unless the user asked for the change. A modal inside a removed rhetorical phrase ("one might be tempted") is not normative; justify it in one line. |
| Figures | A number, date, percentage, duration, or version is missing from the edit or new in it. | Restore or remove. A new figure is an invention. |
| Headings | Any heading text, level, or order differs; any heading missing. | Restore. Headings are navigation, not prose. |
| Labels and status values | A bold list label, step label, or status enum value changed, dropped, or new. | Restore. |
| Paragraph count | A source paragraph has no counterpart in the edit (deleted), or one paragraph became three (split), or two merged. | Intended merges and splits are fine; say so. Deletions need a reason. |
| Length | Overall ratio outside 0.85 to 1.15, or any paragraph outside 0.7 to 1.4. | Look for invention (longer) or dropped claims (shorter). A slop-heavy draft legitimately loses 20 to 35 percent when openers, riders, and closers go; justify it by listing what was cut and confirming no claim, number, or rule went with it. |
| Fragments | A bullet, table cell, or label that was a fragment is now a sentence. | Restore the fragment. |
| Code and paths | Backtick count, code block count, URL and path strings differ. | Restore. |
| Formatting | Bold, italic, table row, and list item counts differ beyond intended removals of decorative bold. | Restore structural formatting. |
| Proper nouns | A capitalized name, product, or acronym appears in the edit but not the source. | Remove. Invented names are the worst class of error. |
| Register leaks | Contractions, "you/your," "however," "here," "actually," "just" increased in a neutral genre. | Remove. |
| Passives | Count increased. | Revert the added passives unless the actor is unknown. |
| Dashes | Em or en dashes increased, or present at all in an IT document. | Replace. |
| Hedges | "I think," "probably," "in most cases," "where relevant" removed. | Restore if the source meant real uncertainty. |

A zero-flag report on a one-sentence edit is weak evidence; the script checks invariants, not voice or judgment. Say so when it applies.

## Reading the report

A flag is not automatically wrong. The response to each flag is one of: **revert** (restore the source wording for that span), **justify** (one line in What changed saying why the change is intended, for example "merged two paragraphs that said the same thing"), or **ask** (when the change would be right only if the user agrees, such as changing a rule's modal). Delivering with an unresolved flag is the failure this gate prevents.

## Building the term list

Before step 2 of the workflow, extract: every term the document defines or capitalizes consistently, every role and body name, every status value, every phrase that recurs three or more times in the same form. For a book, load the ledger per `long-form.md`. Save as one term per line; the script accepts `#` comments and `term|variant1|variant2` lines to catch known drifts.
