# paper draft intro related conclusion

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_draft-intro-related-conclusion_20260515T225954_result.json`
- **Structured JSON:** [`b19611e2b9b3ef2189d1.json`](../../sessions/b1/b19611e2b9b3ef2189d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All citation keys verified against `references.bib` — no missing or fabricated references.

**Results:**

| Section | Before | After | Target |
|---|---|---|---|
| introduction.tex | 551w | 907w | 1000w |
| related_work.tex | 381w | 591w | 600w |
| conclusion.tex | 341w | 404w | 400w |

**Introduction** changes: Added broader APR context and test-time scaling motivation in the hook; expanded trajectory-level paragraph with concrete re-repair example; added paragraph positioning against LEVER/CodeT and claiming novelty of the systematic formulation comparison; added complexity-dependence paragraph with oracle framework preview; added bridge sentence with dataset/model references before contributions; strengthened C1 with second CWM seed confirmation.

**Related work** changes: Expanded each of the 5 paragraphs with sharper positioning and richer context. Added sentences on why generation cost scales, why verification quality matters for test-time scaling, how our per-test diagnostic differs from LEVER/CodeT, and that code complexity is the key moderator for the NLP classification-vs-generation tradeoff.

**Conclusion** changes: Added P2P regression limitation (1.04% mean), synthetic-to-real transfer limitation, "or pre-training regimes" to model family caveat. Expanded future work with oracle ensemble number (90.63%) and complexity-routing ensemble idea, 8B-8B completion mention.

All numbers match registry. All `\cite{}` keys exist in `references.bib`.

---
