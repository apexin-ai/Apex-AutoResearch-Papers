# paper patch narrative

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_patch-narrative_20260516T024638_result.json`
- **Structured JSON:** [`2cc423c077e4a3c80c7c.json`](../../sessions/2c/2cc423c077e4a3c80c7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Summary of changes:

1. **introduction.tex**: Added `fig:overview` figure environment (lines 29-34) with the correlation-selection gap figure. Added `\S Discussion` and `\S Conclusion` to paper outline (line 60).

2. **abstract.tex**: Changed WNUT-17 from equal-status dataset to "boundary probe" — now reads "on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe, using two model families".

3. **discussion.tex**: AUROC=0.735 now cites `\S\ref{sec:selection_gap}` (line 7). The n=81 subset now includes its definition and a cross-reference to `\S\ref{sec:complexity_robustness}` (line 25).

4. **limitations.tex**: "logistic regression proxy as an upper bound" removed (line 8).

5. **conclusion.tex**: Added sentence about 4B scale and free-form decoding ablations confirming gap robustness (line 12).

6. **Terminology**: Consistent — abstract/intro/discussion/conclusion use "entity voting"; experiments/method use formal "Voting Confidence" / "Voting Conf." in tables.

---
