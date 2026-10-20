# analysis holdout split validation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_holdout-split-validation_20260519T005549_result.json`
- **Structured JSON:** [`60d950612e826bddb6a2.json`](../../sessions/60/60d950612e826bddb6a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary of outputs:

**DDR partition is 100% consistent across both holdout splits.** All 7 features land in the same zone (drifting / intermediate / near-stationary) regardless of which 4 generators are in the selection vs. validation set.

| Feature | Zone | Split A sel/val |ρ| | Split B sel/val |ρ| |
|---|---|---|---|
| entropy_mean | drifting | 0.60 / 0.58 | 0.60 / 0.58 |
| ttr | drifting | 0.61 / 0.59 | 0.60 / 0.59 |
| hapax_ratio | drifting | 0.62 / 0.60 | 0.62 / 0.61 |
| entropy_std | intermediate | 0.19 / 0.21 | 0.22 / 0.17 |
| entropy_min | intermediate | 0.39 / 0.36 | 0.38 / 0.37 |
| entropy_max | near-stationary | 0.05 / 0.05 | 0.04 / 0.06 |
| tail_decay | near-stationary | 0.10 / 0.08 | 0.11 / 0.07 |

Saved files:
- `artifacts/_project/rebuttal/spearman_per_generator.json` (8-generator ρ data)
- `artifacts/_project/rebuttal/holdout_split_results.json` (full split validation results)
- `artifacts/_project/chart/fig_ddr_holdout_split.pdf` + `.png` (scatter plots)

---
