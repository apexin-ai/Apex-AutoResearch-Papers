# code exp 006 maxitems fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_006_maxitems_fix_20260514T182321_result.json`
- **Structured JSON:** [`a63ec6e1cd461497499c.json`](../../sessions/a6/a63ec6e1cd461497499c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tests pass. Here's the summary:

**Fix 1 — `--max-items` random subsampling** (`run_exp006.py`): Already used `rng.choice` (not truncation as task description assumed), but seed was hardcoded `42`. Changed to use `args.seed` for consistency.

**Fix 2 — ADVI removed** (`run_exp006.py` + `run_irt_calibration.py`):
- Deleted `--method` argparse argument
- Deleted `fit_stan_model_advi` function
- Removed all ADVI branches from `run_benchmark_fit`, NUTS is now the only path

**Fix 3 — `joint_fit.py` max_items fixed**:
- Removed `dry_run` gate — max_items now applies regardless of dry-run mode
- Changed truncation (`[:max_items]`) to per-benchmark random subsampling (`rng.choice`)
- Subsampling happens inside `concatenate_benchmarks` before concatenation, so each benchmark gets proportional representation

Verification confirms:
- 100 items are randomly selected (first index=55, not 0)
- joint_fit and run_exp006 produce identical subsamples for same seed
- No ADVI references remain

---
