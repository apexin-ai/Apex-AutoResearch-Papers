# fix d041 paper framing dataflow

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d041-paper-framing-dataflow_20260515T021011_result.json`
- **Structured JSON:** [`6618584cb9e368cf2b5f.json`](../../sessions/66/6618584cb9e368cf2b5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

paper_framing.md is fixed. I also found the same incorrect descriptions in the paper_drafts files — the spawn_worker should handle those, but let me flag the specific problems:

**method_v1.md** has the most critical errors:
- Line 71: "combines embedding distance with structural reachability filtering" — should be BM25 + structural connectivity
- Line 77: Formula uses `sim(E_θ0(q), E_θ0(f))` with `f ∉ R_G(q)` — wrong in both ranking (should be BM25) and filter (should be `f ∈ R_G(q)`, connected not disconnected)
- Line 79: "structurally disconnected in the data-flow graph" — should be "structurally connected"
- Line 85: Same "structurally disconnected" error

**introduction_v2.md**:
- Line 13: "filtering such pairs could yield genuinely informative training signal" — implies filtering OUT connected files, but code does the opposite
- Line 17: "filters structurally connected files from the embedding-distance candidate set" — wrong direction

**figure_design_v1.md**:
- Line 49/75/77: Visual description shows "no data-flow edges" for dataflow-aware negatives — should show connected files ranked by BM25

Summary of changes to paper_framing.md:

1. **Formal definition fixed**: `argmax_{x: s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)` → `argmax_{x: reachable_G(x,q) ∧ x ≠ x*} BM25(q, x)`
2. **Added Three-Strategy Difficulty Gradient subsection** clarifying each strategy's mechanism (random = uniform, embedding-distance = cosine similarity, dataflow-aware = structural filtering + BM25 ranking)
3. **Drift-immune note updated** to cover both graph and BM25 ranking as encoder-independent
4. **D041 comment added** at end of file

---
