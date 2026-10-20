# analysis naive baseline comparison

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_naive_baseline_comparison_20260524T015506_result.json`
- **Structured JSON:** [`7ce00693644801af7440.json`](../../sessions/7c/7ce00693644801af7440.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Results:

**Summary Table**

| Method | FPR (α=0) | Onset α | Cross-seed |
|---|---|---|---|
| PPL-slope (≥2 consec) | **100%** (3/3) | 0.10 | trivially consistent (always fires) |
| PPL-slope (≥3 consec) | **100%** (3/3) | 0.10 | trivially consistent (always fires) |
| Variance-threshold | **67%** (2/3) | 0.10 | inconsistent at null |
| PermG (fwd sig≥1) | **0%** (0/3) | 0.50 | 3/3 at α=0.50 |

**Key finding**: PPL-slope is unusable — perplexity naturally drifts upward even at α=0.00 (gen2→gen6 shows 4 consecutive increases: 20.0→20.3→20.5→20.9→21.0), so it fires on every null seed (100% FPR). Variance-threshold also has 67% FPR. PermG is the only method with 0% FPR — its causal lead-lag test only fires when contamination actually causes downstream degradation, not from natural training drift.

The "earlier onset" of baselines at α=0.10 is meaningless since they also fire at α=0.00.

Artifacts saved to:
- `artifacts/A2_naive_baseline_comparison.json`
- `artifacts/_project/A2_naive_baseline_comparison.md`

---
