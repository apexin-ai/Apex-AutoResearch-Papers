We thank Reviewer mdt1 for recognizing the contribution and providing concrete improvement suggestions. We address each concern below.

**W1: Writing clarity and terminology.**

We agree the paper introduces several domain-specific terms (BCS, SCS, count degradation, schema confusability) and that some could be defined earlier. In the revision:
- We add a brief inline definition of BCS and SCS at first use in the introduction (before the formal definition in §3.2)
- "Count degradation" is clarified as "performance decline caused by increasing the number of candidate types" at first use
- We separate metric reporting from interpretation more clearly in §4, ensuring each quantitative statement is followed by its plain-language meaning

**W2: BCS computation—does it ignore context?**

BCS is intentionally a *schema-level* property, not an instance-level one. It is computed from type *names* (the labels appearing in the prompt), not from mentions or contexts in which those types occur. This is by design: BCS is meant as a pre-deployment risk assessment tool that can be computed from a schema definition alone, without running extraction on any data.

Specifically: embed("place of birth") produces a single vector from the type name string; BCS(batch) = mean pairwise cosine over all type-name pairs in the batch. There is no averaging over instance contexts because the metric characterizes the *schema* (what the model is asked to distinguish), not the *data* (what mentions look like in context).

This design choice has a clear tradeoff: BCS cannot capture context-dependent confusion (as we note in §3.2: "SCS does not capture context-dependent disambiguation or mention-level ambiguity; these contribute to residual variance"). An instance-averaged embedding would measure something different—how types are used in practice—which would require running the extraction pipeline first, defeating the pre-hoc purpose.

We clarify in the revision by adding to §3.2: "SCS operates on type-name strings rather than instance contexts, enabling pre-hoc computation from schema definitions alone."

**W3: BCS computed at schema level vs. dataset level.**

To confirm: BCS is computed per *batch* (a subset of types presented in one prompt), not across the entire dataset schema. Each experimental condition presents a specific batch of k types; BCS(batch) characterizes that specific prompt's type set. Different batches of the same k types drawn from the same schema will have different BCS values, which is precisely what enables our BCS-controlled experiments (§3.4).

**Formatting:** We ensure consistent line spacing throughout the revision.
