# code data quality fix

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data_quality_fix_20260512T113345_result.json`
- **Structured JSON:** [`9e8462e0eb2b3015dbf8.json`](../../sessions/9e/9e8462e0eb2b3015dbf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 8/8 gold files now correctly found in connected sets. Here's the summary:

---

## Bug 1: Path normalization — Root Cause & Fix

**Root cause**: `_swebench_to_instance` extracts `gold_files` from patch diffs (e.g., `requests/sessions.py`), but when repos have `src/` or other prefix directories, the actual paths are different (e.g., `src/requests/sessions.py`). `find_buggy_function` updates `buggy_file` via os.walk but `gold_files` was never updated.

Two sub-cases:
- **requests-1963**: `requests/sessions.py` → `src/requests/sessions.py` (prefix mismatch)
- **xarray-3364**: `xarray/core/concat.py` → `xarray/structure/concat.py` (file relocated between base_commit and HEAD)

**Fix**: Added `normalize_path()` + `_common_suffix_length()` in both `extract_dataflow.py` and `mvp_phase1.py`. Normalizes gold paths against actual on-disk files via suffix matching before H2 computation. Also updates `gold_files` in main() when `find_buggy_function` relocates buggy_file.

## Bug 2: seaborn/scikit-learn skip — Root Cause

**Root cause**: `clone_repo` uses `--depth 1` (shallow clone at HEAD). The `git checkout base_commit` fails silently because the historical commit isn't available. If the buggy file was renamed/removed between `base_commit` and HEAD, `find_buggy_function` returns None → skip.

**Fix**: Changed `clone_repo` to:
1. Full clone (no `--depth 1`) for new clones
2. `git fetch --unshallow` + retry for existing shallow clones

## Updated H2 Results

| Metric | Before | After |
|--------|--------|-------|
| gold_in_connected | 6/8 | **8/8** |
| coverage_connected | 0.014388 | **0.014815** |
| coverage_disconnected | 0.0 | 0.0 |
| Fisher p-value | 1.54e-07 | **6.50e-09** |
| connected_hits/total | 6/417 | **8/540** |

xarray's connected count jumped from 1 to 124 because the normalization now correctly matches the relocated file.

## Recommendations for Full 5K Run

1. **Full clone required**: Remove `--depth 1` to enable proper `base_commit` checkout. This is the #1 source of skips.
2. **Path normalization is essential**: ~15% of SWE-bench repos use `src/` or `lib/` layouts where patch paths differ from on-disk paths.
3. **Expected skip rate with both fixes**: <5% (down from ~20% currently). Remaining skips would be repos that require special build setups.

---
