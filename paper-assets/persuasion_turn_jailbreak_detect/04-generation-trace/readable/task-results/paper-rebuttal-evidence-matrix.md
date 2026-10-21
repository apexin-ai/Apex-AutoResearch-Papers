# paper rebuttal evidence matrix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_rebuttal-evidence-matrix_20260518T232848_result.json`
- **Structured JSON:** [`7f63c273e3dbcc9661f3.json`](../../sessions/7f/7f63c273e3dbcc9661f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Rebuttal evidence matrix written and registered (`art_20260518_0a9c4d`).

**Coverage summary**:
- **11 Must-Fix issues** (R2 N1-N7 + R3 N1-N5): 9 resolved, 2 partial (novelty framing, baseline comparison)
- **16 Should-Fix issues**: 10 resolved, 6 partial
- **8 Minor issues**: all resolved

**Remaining gaps** (no new experiments needed, but paper text adjustments pending):
1. **Novelty (MF2)** — framing adjustment in progress; defense relies on negative findings being unpredictable from "Don't Stop Pretraining"
2. **Baseline comparison (MF5)** — no direct DeepContext reproduction; mitigated by analysis paper positioning + LLM judge baseline
3. **Capacity caveat (SF9)** — needs to propagate from Discussion into Contribution 2 and Abstract
4. **Analysis depth (SF14)** — CKA heatmap added but no t-SNE/UMAP

All metrics are sourced from registry with experiment IDs cross-referenced.

---
