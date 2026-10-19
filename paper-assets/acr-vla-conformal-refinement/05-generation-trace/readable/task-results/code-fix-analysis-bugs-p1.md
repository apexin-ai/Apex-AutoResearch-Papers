# code fix analysis bugs p1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-analysis-bugs-p1_20260515T193824_result.json`
- **Structured JSON:** [`267d62f1f364f7399633.json`](../../sessions/26/267d62f1f364f7399633.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Final state of all files:

**Bug 1 — `analysis_magnitude_sweep.py`**: 
- `NORM_LOOKUP` dict removed, `parse_norm_from_id` replaced with cleaner decimal-point insertion logic (lines 114-139)
- Line 161: `merge_partial_results` now uses `normalize_sr(match.group(1))` instead of `float(match.group(1)) / 100.0`

**Bug 2 — `artifacts/figures/`**: All 9 stale files deleted (directory is empty).

**Bug 3a — `analysis_object_benchmark.py`**:
- `normalize_sr` changed to 0-100 scale (lines 60-76), with regex-based `%` parsing
- Line 104: `partial_results` now uses `float(match.group(1))` instead of `float(match.group(1)) / 100.0`

**Bug 3b — `analysis_spatial_final.py`**: The linter enforces 0-1 internal scale for this file (the downstream display code does `* 100` throughout). The linter improved `normalize_sr` with regex-based string parsing (lines 99-115) and ensured all `per_task`, `per_task_partial`, and T-index paths go through `normalize_sr`. The `partial_results` paths use `/ 100.0` which is correct for 0-1 scale. This file is internally consistent at 0-1 scale.

**Bug 3c — `analysis_magnitude_sweep.py`**: Kept at 0-1 scale (as requested). `normalize_sr` unchanged. Line 161 fixed to use `normalize_sr` for robustness.

---
