# analysis pipeline nondeterminism fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pipeline-nondeterminism-fix_20260518T185409_result.json`
- **Structured JSON:** [`5b1bec55208dd0e140e0.json`](../../sessions/5b/5b1bec55208dd0e140e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Summary

### Root Cause
The ~3pp accuracy difference (74.51% vs 77.94%) is **NOT** from pipeline non-determinism. It's from **different constraint data**: `extract_constraints.py` re-extracted constraints via separate LLM calls (temperature=0.1), producing different constraints than exp-001's in-memory extraction. 202/204 problems have different constraint counts between the two datasets.

### Fixes Applied (4 files)

| File | Change |
|---|---|
| `sica/pipeline.py` | `list(set(...))` → `sorted(set(...))` (2 locations); returns `per_trace_constraints` in output |
| `sica/scorer.py` | Deterministic tiebreaking: alphabetical sort after frequency tie |
| `sica/z3_maxsat.py` | Added `z3.set_param('smt.random_seed', 42)` and `z3.set_param('sat.random_seed', 42)` |
| `run_consistency_filtering.py` | `list(set(...))` → `sorted(set(...))` |
| `run_z3_feedback_folio.py` | `list(set(...))` → `sorted(set(...))` |
| `run_full_mvp.py` | Saves per_trace_constraints files alongside intermediates |

### Verification
Fixed pipeline produces identical results (fingerprint `77b240fb54dca62dfbf8e0497b53526f`, 159/204) across:
- PYTHONHASHSEED = 0, 42, random
- 3 independent Python processes

### Impact on Paper
The canonical SICA accuracy should be re-established by re-running the full pipeline once with the fixes, which will now save the exact constraints used for scoring. The 74.51% from exp-001 and 77.94% from exp4 are both valid but computed on different constraint sets.

---
