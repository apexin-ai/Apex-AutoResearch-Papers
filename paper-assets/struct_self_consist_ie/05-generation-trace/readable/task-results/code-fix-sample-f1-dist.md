# code fix sample f1 dist

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_sample_f1_dist_20260514T043208_result.json`
- **Structured JSON:** [`33e70e190f45cb5e8c1d.json`](../../sessions/33/33e70e190f45cb5e8c1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files work. Here's a summary of changes:

**evaluation.py**: Added `compute_sample_f1_distribution()` (lines ~170–220) that computes per-sample F1 against gold for every sample in every instance, returning aggregate stats (`mean`, `std`, `pct_f1_zero`) and per-instance breakdowns.

**run_mvp_pilot.py**:
- Imported `compute_sample_f1_distribution`
- Added step 3b: calls the new function after consistency scoring
- Added `sample_f1_mean`, `sample_f1_std`, `sample_f1_pct_zero` to the report dict
- Added warning field when `pct_f1_zero > 30` recommending T=0.7
- Updated `print_report` to display the three new metrics and the warning

---
