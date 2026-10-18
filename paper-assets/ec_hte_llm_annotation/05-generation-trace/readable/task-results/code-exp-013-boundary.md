# code exp 013 boundary

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-013-boundary_20260521T072541_result.json`
- **Structured JSON:** [`5c3788d329af68ccade7.json`](../../sessions/5c/5c3788d329af68ccade7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. All three outputs saved:

- **`results/exp013_boundary_condition.csv`** — 3200 rows (100 runs × 4 subgroups × 4 methods × 2 z-levels)
- **`results/exp013_boundary_summary.csv`** — 32 rows aggregated
- **`results/exp013_boundary_analysis.md`** — full analysis

Key findings from 100 MC runs:

1. **Worst degradation is subgroup A (pi=0.30), not D (pi=0.03)** — RMSE reaches 0.62 for EB. The highest-misclassification subgroup suffers most because the CM estimation noise amplifies through a nearly-singular mixing matrix inversion, not because it has fewer labels.

2. **Stratified RMSE is ~2x global** on average (2.07x for z0, 2.06x for z1). Subgroup A hits 3.7–4.4x amplification.

3. **n_expert/K = 12.5 < 25 threshold** — confirmed. Per-subgroup CM estimates are too noisy; global correction dominates all stratified methods.

4. **EB vs MLE**: EB is ~5% worse than MLE here — the shrinkage target (pooled mean) is itself noisy with only 50 total labels, so partial pooling doesn't help. Both are far worse than global.

5. **Naive beats all correction methods on average RMSE** for this boundary case — the correction signal is swamped by estimation noise in the mixing matrix.

---
