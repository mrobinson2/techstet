# Tells: patterns that mark technical prose as model-written

Tiered by evidence weight. **Tier 1** justifies an edit on one sighting. **Tier 2** needs company from other tells in the same passage. **Tier 3** is style; the genre or the author's sample can switch it off. Every example is technical because the essay examples in the source catalogs do not transfer.

Underlying cause, from Wikipedia's "Signs of AI writing": a model writes whatever fits the widest range of readers and subjects. A person writes for one reader and one subject, so their choices are uneven and specific. Each tell is one form of the default choice.

## Tier 1: act on one sighting

### T1. Staged contrast (not X but Y)
**Watch for:** not X but Y; not just / not only / not merely X, but Y; it's not X, it's Y; "This does not mean X. It means Y."; a clipped negative tail ("..., no guessing"); "The question isn't X. It's Y."
**Why it is a tell:** the negative half names something nobody claimed so the positive half sounds bigger. Keep a contrast only when the negative half corrects a belief the reader actually holds. The fence move in `engagement.md` is that legitimate form: name the neighbor concept and the one difference.
**Before:** The problem isn't the model. It's the eval.
**After:** The eval matters more than the model here, because the model passed and the release still failed.
**Before:** Significance determines whether a decision is recorded. It does not, by itself, determine who decides.
**After (keep):** This one stays. Readers of the governance draft did believe significance routes a decision to the council; the contrast corrects that belief and both halves carry information.

### T2. Closer that restates
**Watch for:** a one-sentence paragraph repeating the paragraph before it; "That distinction matters."; "This is the key point."; a sentence after an example that names what the example showed; the same closer under every heading; a row of fragments ("No gate. No queue. No waiting.").
**Why:** it asks the reader to pause on a claim instead of adding to it. Delete it. Do not write a better closer. End on the last concrete fact, or on the next action.
**Before:** Rotate the key every 90 days. Automate the rotation. Alert on failure. Security is a process, not a product.
**After:** Rotate the key every 90 days, automate the rotation, and alert on failure.

### T3. Deep-sounding sayings and colon reveals
**Watch for:** the real question is, at its core, fundamentally, the heart of the matter, X is the Y of Z, "The detail that makes it work: a separate agent grades it."
**Why:** an ordinary point dressed as hidden truth. Replace with the specific claim in a plain sentence.
**Before:** At its core, observability is a culture problem.
**After:** Teams stop reading dashboards when the alerts page more than twice a week.

### T4. Staged run-up and fake candor
**Watch for:** Let's dive in, here's what you need to know, let's break this down, Here's the thing, Honestly?, Look, To be clear, The uncomfortable truth is, What most people get wrong, Here's what nobody tells you.
**Why:** announces the point instead of making it, or flatters the writer as lone expert. Cut the run-up and the sentence usually stands. The positive form is the promise opening in `engagement.md`: say what the reader will be able to do.

### T5. Arguing with no one
**Watch for:** This isn't about, I'm not saying, Don't get me wrong, Some might say... but, A tempting approach would be, One might be tempted to, It would be easy to just.
**Why:** rejects an option or objection that appears nowhere else. Keep an alternative only if a reader of this document would actually weigh it; then present it as an alternative, not a straw man. In an ADR the rejected options section is the place for that, with real reasons.

### T6. Inflated significance and send-offs
**Watch for:** pivotal, crucial, key role, marks a shift, underscores the importance, stands as a testament, evolving landscape, the future looks bright, a step in the right direction, Despite these challenges... continues to, Future Outlook sections.
**Why:** an ordinary fact is said to prove a trend or promise a future. Keep the fact. End on the last concrete fact or a stated plan with an owner.

### T7. Borrowed authority
**Watch for:** experts agree, industry reports suggest, studies show, widely regarded, best practice dictates (with no source), "according to leading vendors"; a precise figure with a vague institutional source ("a Stanford study found 27%," "Harvard Memory Lab," "17% per bullet point"); any statistic the reader could not trace to a document they can open.
**Why:** an unnamed authority stands in for the claim. Name the source and what it said if the source text or the user has it. Otherwise decide what the claim is doing: if the argument depends on it, keep it as a plain assertion in the author's voice ("Centralized secrets management reduces the attack surface") and ask for a source in What changed; if it is decoration, cut it. Never invent a citation.

### T8. Chat residue and self-description
**Watch for:** I hope this helps, Certainly!, Great question, Let me know if, Would you like me to; "This document is organized by," "The table below compares," "generated from," "anything unconfirmed is flagged."
**Why:** wrapper text and method narration that was never for the reader. Remove. Keep a convention note only when the reader cannot infer it, stated once.

## Tier 2: needs company

### T9. Forced triad
**Watch for:** three adjectives, three examples, three parallel sentences, three bullets when the material has two or five. At paragraph scale: three short cases followed by a lesson.
**Why:** three sounds complete whether or not the meaning has three parts. Check each item adds a distinct idea. Keep three real items; a procedure with three steps is not a tell.

### T10. Repeated openings
**Watch for:** three or more consecutive sentences or bullets starting with the same word or shape ("The system... The system... The system..."; "Ensure... Ensure... Ensure...").
**Why:** repetition handled by rule instead of by ear. Merge, change the subject, or lead with the action. Deliberate anaphora for emphasis is allowed once.

### T11. Dashes as the universal connector
**Rule:** no em or en dashes in IT documents; in a book, match the author's sample rate. Replace with a period, comma, colon, or parentheses. Leave hyphens and dashes in code, paths, ranges, and identifiers alone.

### T12. -ing riders and false agency
**Watch for:** highlighting, underscoring, ensuring, reflecting, showcasing, fostering bolted to a fact; "the decision emerges," "the data tells us," "the complaint becomes a fix," "the culture shifts."
**Why:** fake depth, or a hidden actor. State the fact; name who acts. "The team fixed it Tuesday" beats "the complaint becomes a fix."

### T13. Copula avoidance and fake-strong verbs
**Watch for:** serves as, stands as, functions as, acts as, represents, boasts, features, offers, leverages, utilizes, facilitates.
**Why:** longer phrases replacing is, are, has, uses. Use the plain verb.

### T14. Stacked qualifiers
**Watch for:** could potentially possibly, might arguably, it's also possible that, in some cases it may.
**Why:** usually repairs an earlier overstatement rather than reporting doubt. Keep one qualifier the source supports. Keep every modal as written; keep "I think" and "probably" when they are real uncertainty. Keep scope statements and safety notices.

### T15. AI vocabulary
**Watch for:** delve, leverage, utilize, facilitate, streamline, robust (figurative), seamless, cutting-edge, holistic, synergy, paradigm, tapestry, landscape (abstract), realm, multifaceted, meticulous, pivotal, crucial, intricate, elevate, empower, harness, ever-evolving, game changer, navigate (challenges), unpack, deep dive, additionally, actually, truly, genuinely.
**Why:** post-2023 frequency. A formal word outside this list is not a tell. Technical uses of robust, gate, pipeline, landscape (actual terrain) stay.

### T16. Vague association and vague declaratives
**Watch for:** linked to, tied to, associated with, in connection with; "The implications are significant," "The reasons are structural," "This has far-reaching consequences."
**Why:** says two things connect without saying how, or that something matters without saying what. Name the relationship or the specific consequence. If the source does not say, keep the vague wording rather than invent the link.

### T17. Interpretive metadiscourse
**Watch for:** As you can see, It is important to note, It's worth noting, The key takeaway is, In other words (when nothing was rephrased), That last part matters more than it sounds.
**Why:** steps outside the subject to tell the reader what to notice. If the prose shows it, delete the aside.

### T18. Portability failure
**Two tests.** Portability: could this sentence move unchanged to another company, product, team, or incident? Then it is filler. So what: could the reader answer it with "so what?" Then it is missing its consequence. Replace it with a fact, mechanism, consequence, or decision specific to this subject, or cut it.

## Tier 3: style the genre or sample can switch off

### T19. Bold as decoration and labeled lists
Bold on every item and a colon after every label. Remove bold that carries no information. Keep bold on a defined term at first use, on a warning, on a status value the reader scans for. Keep labeled lists in runbooks and checklists where the label is the step name.

### T20. Decorative headings
Title Case On Every Word, emojis, arrows, horizontal rules between every section, a heading written for effect ("The decision, on one screen") instead of for the reader ("How the six options compare"). Use sentence case and say what the section holds.

### T21. Curly quotes and inconsistent apostrophes
Match the document. Most editors auto-curl; alone this means nothing.

### T22. Passive voice and missing subjects
Convert when the actor matters and is hidden ("Mistakes were made," "It was decided"). Leave it when the actor is unknown, obvious, or irrelevant ("The certificate is rotated every 90 days").

### T23. Hyphenated pairs after the noun
"The report is high-quality" loses the hyphen after the noun; "a high-quality report" keeps it. Dictionary compounds (third-party, cross-functional) keep it everywhere.

### T24. Summary-recap ending
"In conclusion," "Overall," a final paragraph that restates the piece, a "Thank you" or "Questions?" equivalent. The last line is the contribution or the reader's next action. In a book chapter the author's sample decides whether a chapter ends on a lesson; one echo of the opening image with new meaning is a device, not a tell, when used once.

## Paragraph and section scale

Run these after the sentence pass; they survive sentence-level cleanup.

- Every paragraph ends on a punchy line.
- Every section opens the same way (a scene, a question, a definition).
- Every section is the same length.
- Sentence length is uniform (15 to 20 words throughout). Real writing has a 6-word sentence next to a 35-word one.
- Each section ends with a restatement of its heading.
- A heading followed by one line that repeats the heading before the content starts.
- The same transition word opening every paragraph.

## When not to act

Leave a watched phrase alone inside a quotation, a title, a proper name, code, or a passage discussing the phrase. Leave fragments that are fragments on purpose. Several tells together are the evidence; one tell in careful prose is often a choice.
