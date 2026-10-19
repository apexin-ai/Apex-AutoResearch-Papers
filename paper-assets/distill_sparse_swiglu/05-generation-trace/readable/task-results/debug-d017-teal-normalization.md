# debug d017 teal normalization

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_d017_teal_normalization_20260515T222817_result.json`
- **Structured JSON:** [`492133c12f991b4df916.json`](../../sessions/49/492133c12f991b4df916.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D017 Bug Fix — Summary

### Root Cause
`teal_global_masks()` in `evaluate.py` scored neurons by **raw sigmoid(predictor(x))** averaged across tokens. Sigmoid probabilities are poor proxies for static neuron importance — they lack magnitude information. A neuron with high activation probability but tiny magnitude ranked above one with lower probability but large magnitude, leading to catastrophic mask selection.

### Two bugs fixed
1. **Wrong scoring metric**: Replaced `mean(sigmoid(logits))` with `mean(|intermediate| * (logits > 0))` — activation magnitude weighted by predictor hard mask. This scores each neuron by how large its activation is when the predictor keeps it.
2. **Missing per-layer normalization**: The old inline topk didn't use `_global_topk_masks()`, which normalizes per-layer scores by their mean before global ranking. Now reuses the shared function.

### Results

| Checkpoint | Metric | Before Fix | After Fix |
|---|---|---|---|
| 70% (kl_sparsity70_s42_v2) | teal_sparse_ppl | 136,069 | **17.91** |
| 30% (kl_sparsity30_s42_v3) | teal_sparse_ppl | (never eval'd) | **8.76** |

Reference: dense PPL = 6.12, predictor per-token PPL = 13.84 (70%) / 7.30 (30%).

### Registry updated
- `kl_sparsity70_s42_v2.teal_sparse_ppl` = 17.91
- `kl_sparsity30_s42_v3.teal_sparse_ppl` = 8.76

---
