# code scale stratified irt

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scale-stratified-irt_20260516T052844_result.json`
- **Structured JSON:** [`677a7261f75c14eeaa8a.json`](../../sessions/67/677a7261f75c14eeaa8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Implementation complete. Summary of changes to `run_pooled_4bench_irt.py`:

**New function: `filter_data_by_scale(data, target_scale)`** (line 108)
- Filters the pooled data dict to only models of a given scale
- Returns None if no models match

**New function: `run_scale_stratified(data, args_dict, exclude_set, min_item_variance)`** (line 380)
- Loops over 0.5B / 1.5B / 3B, filters data per scale
- Runs `run_single_benchmark_fit` for each scale × benchmark combination
- Warns when only 1 dosage level (gamma prior-dominated)
- Saves per-scale JSON results to `OUTPUT_DIR/scale_stratified/&lt;scale>/`
- Prints summary table with γ̂, CI, R̂, ESS, N_models, N_items
- Flags convergence issues (R̂ > 1.01, ESS < 400, small N)

**Refactored: `run_pooled(data, args_dict, exclude_set, args)`** (line 502)
- Extracted from `main()` — identical behavior to before

**Modified: `parse_args()`** (line 619)
- Added `--stratify-by-scale` flag
- Added CLI args for Stan config (`--chains`, `--warmup`, `--samples`, etc.) — previously hardcoded

**Modified: `main()`** (line 645)
- Branches on `args.stratify_by_scale`: calls `run_scale_stratified` or `run_pooled`

D045 exclusion remains active — 0.5B on mmlu/arc_challenge will show as SKIPPED in the table, which is the expected behavior (position bias confound).

---
