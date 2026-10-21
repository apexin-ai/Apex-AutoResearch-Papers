# eval plan 006 training free reeval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_006_training_free_reeval_20260515T211513_result.json`
- **Structured JSON:** [`d41e0ed7db104c0b015c.json`](../../sessions/d4/d41e0ed7db104c0b015c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both artifacts registered. Here's the summary:

## Plan 006 Re-Evaluation Complete

### Bug Fixed
`_global_topk_masks` in `evaluate.py` lacked per-layer mean normalization. Activation magnitudes vary 50-100x across layers, causing early layers to be fully pruned and late layers to keep everything. Also added `dense_mse` normalization to the greedy error curves in both `evaluate.py` and `baselines.py`.

### Corrected Results (50% sparsity, LLaMA 3.1 8B, WikiText-2)

| Method | Before | After | Status |
|--------|--------|-------|--------|
| Dense | 6.12 | 6.12 | Reference |
| Uniform 50% | — | 23.90 | Sanity check |
| **Vanilla TEAL (global)** | 58,032 | **23.31** | FIXED |
| **WINA (global)** | 82,567 | **27.93** | FIXED |
| **TEAL Greedy (baselines.py)** | — | **33.47** | FIXED |
| TEAL Greedy (evaluate.py) | 50,035 | 164.76 | Partial — Layer 1 over-pruned |
| R-Sparse (global) | 74,929 | 151.20 | Mean norm insufficient for SVD scores |
| WINA Greedy | — | 2,126 | Inverted allocation — separate bug |

### Three methods are now validated and usable:
- **Vanilla TEAL global** (23.31) — best, simplest
- **WINA global** (27.93) — decent
- **TEAL greedy baselines.py** (33.47) — non-uniform allocation

### Remaining issues (lower priority):
- R-Sparse needs percentile/max normalization instead of mean normalization for SVD-weighted scores
- WINA greedy has an inverted allocation bug in its own error computation
- evaluate.py's greedy still over-prunes Layer 1

---
