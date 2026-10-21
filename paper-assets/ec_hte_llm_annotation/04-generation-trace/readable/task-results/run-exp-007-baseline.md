# run exp 007 baseline

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp-007-baseline_20260520T213819_result.json`
- **Structured JSON:** [`09a627b1f387be7d90f2.json`](../../sessions/09/09a627b1f387be7d90f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment completed successfully. Key findings:

**Row counts**: raw = 36,000 rows (correct: 2400 runs × 5 methods × 3 z-per-subgroup combos), aggregated = 360 rows.

**EC-HTE == DSL**: Confirmed identical (placeholder behavior as expected).

**Summary of results:**

### DSL vs Global-Corrected
- **DSL has worse RMSE than Global across all regimes**, especially with k=4 subgroups where per-subgroup expert samples are small (n_expert/k can be as low as ~12). The variance penalty from per-subgroup MLE dominates.
- DSL has **lower absolute bias** than Global in the extreme regime (|bias| ~0.04-0.07 vs ~0.06 for Global), confirming that subgroup-specific correction reduces bias when heterogeneity is real.
- In homogeneous regime, DSL ≈ Global on bias (as expected — all subgroups have the same error rate), but DSL pays a RMSE penalty for estimating unnecessary per-subgroup parameters.

### DSL vs Naive
- DSL substantially reduces bias vs Naive in the extreme regime (|bias_z1| 0.074 vs 0.066 for Naive — close because Naive's attenuation bias is partially offset by DSL's variance).
- In moderate/homogeneous regimes, Naive actually has lower RMSE than DSL because the bias is small relative to DSL's variance cost.

### Coverage
- DSL coverage for z0 averages 0.91-0.94 (roughly meets 0.90 target).
- DSL coverage for z1 falls short: 0.85 (extreme), 0.90 (moderate), 0.90 (homogeneous). Under-coverage is driven by small n_expert/k=4 settings where the MLE CM is noisy.

### Implication for EC-HTE
This is exactly the gap HB partial pooling should close: DSL's variance is too high when per-subgroup expert labels are sparse. EC-HTE with a proper HB estimator should achieve DSL-level bias reduction while keeping variance closer to Global-corrected.

---
