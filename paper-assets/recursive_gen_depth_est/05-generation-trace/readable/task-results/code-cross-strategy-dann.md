# code cross strategy dann

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_strategy_dann_20260519T104344_result.json`
- **Structured JSON:** [`ebb9c388e49b8b5238ac.json`](../../sessions/eb/ebb9c388e49b8b5238ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files are saved. Here's the summary of all results:

## All 3 Models Complete

**LOSO Average (cross-model):**

| Method | Accuracy | MAE | Weighted Kappa |
|--------|----------|-----|----------------|
| RF | 0.5918 | 0.4969 | 0.7164 |
| DNN | 0.5939 | 0.4985 | 0.7137 |
| **DANN** | **0.6040** | **0.4755** | **0.7315** |

DANN wins on all aggregate metrics across all 3 models. The largest gains are on the hardest fold (hold-out top-k), where domain shift is greatest. Naive DNN barely improves over RF, confirming that the gains come from the gradient reversal domain adaptation rather than from the neural architecture itself.

**Files saved:**
- `artifacts/cross_strategy_da/dann_results.json` (all 3 models, per-fold + averages)
- `artifacts/cross_strategy_da/dann_vs_baseline_comparison.md` (full comparison with tables and analysis)

---
