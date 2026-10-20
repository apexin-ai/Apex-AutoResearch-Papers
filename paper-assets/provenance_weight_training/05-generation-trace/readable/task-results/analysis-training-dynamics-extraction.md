# analysis training dynamics extraction

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_training-dynamics-extraction_20260518T194659_result.json`
- **Structured JSON:** [`2411e87191988b2900f8.json`](../../sessions/24/2411e87191988b2900f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data extracted and saved. Here are the results:

---

## adaptive_fix_seed42 (Qwen3-0.6B, seed42)

**Run was terminated at step 24 (SIGTERM).** Only 25 optimizer steps available (100 per-batch entries with grad_accum=4).

### Per-step averages (25 steps):
| Metric | Mean | Median | Std |
|--------|------|--------|-----|
| b* | 1.306 | 1.065 | 0.790 |
| α_eff | 0.618 | 0.628 | 0.098 |
| ESS | 2.285 | 2.259 | 0.202 |
| mean_q | 0.637 | 0.634 | 0.079 |

### Per-batch (raw) stats:
- **α_eff at cap (>=0.8):** 29/100 = 29.0%
- **ESS near n_min (<2.1):** 73/100 = 73.0%

---

## contamination_60_adaptive_seed456 (Qwen3-0.6B, full 6103 steps)

This is the closest completed adaptive run (same model, same method, contamination_ratio=0.6 vs 0.4).

### Overall (6103 per-step averages):
| Metric | Mean | Median | Std |
|--------|------|--------|-----|
| b* | 1.387 | 1.109 | 0.989 |
| α_eff | 0.629 | 0.641 | 0.106 |
| ESS | 2.295 | 2.243 | 0.258 |
| loss (unweighted) | 1.925 | 1.915 | 0.257 |

### Key findings:
1. **Metrics are remarkably stable across training.** No convergence or phase transitions. b*, α_eff, and ESS show nearly identical distributions from Phase 1 to Phase 10.
2. **Per-batch:** α_eff hits the 0.8 cap in **34.3%** of batches; ESS is near n_min (< 2.1) in **67.6%** of batches. The per-step averaging smooths this out.
3. **b* is right-skewed:** median 0.86, mean 1.39, p99=10.22. Most batches use moderate b*, but occasional high-b* outliers pull the mean up.
4. **Loss decreases modestly** from 1.97 (early) to 1.90 (late), confirming the model is learning.

### Files saved:
- `/root/autodl-tmp/provenance_weight_training/artifacts/training_dynamics_adaptive_fix_seed42.csv` (25 rows, per-step avg)
- `/root/autodl-tmp/provenance_weight_training/artifacts/training_dynamics_adaptive_fix_seed42_per_batch.csv` (100 rows, raw)
- `/root/autodl-tmp/provenance_weight_training/artifacts/training_dynamics_contamination60_adaptive_seed456.csv` (6103 rows, per-step avg)

**For the paper figure,** the contamination_60_adaptive_seed456 data is the recommended source since adaptive_fix_seed42 only has 24 steps.

---
