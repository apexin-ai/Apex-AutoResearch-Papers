# code n500 analysis audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n500_analysis_audit_20260514T224811_result.json`
- **Structured JSON:** [`511275e6ad20726e83c3.json`](../../sessions/51/511275e6ad20726e83c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All fixes verified. Final summary:

---

## Audit Results

### Issues found and fixed:

| # | File | Issue | Fix |
|---|------|-------|-----|
| 1 | `analyze_n500.py:39` | `B_BOOTSTRAP = 1000` | Changed to `10000` |
| 2 | `analyze_n500.py` | No per-phase null rate (W5 missing) | Added `midphase_null_rate()` function + integrated into `analyze_condition()` |
| 3 | `analyze_n500.py:424` | d_z computed for both imp AND rand (D059 violation) | Loop now only runs for `"imp"` masking |
| 4 | `analyze_n500_unified.py:131` | `midphase_null_rate` only computed rate for mid phase | Added `null_high_rate`, `null_low_rate`, `effective_n_*` for all 3 phases |
| 5 | `analysis/cross_model_analysis.py` | Hardcoded n=50 paths, won't work for n=500 | Added `--n500` flag, compute d_z on the fly instead of loading pre-computed files |

### No issues found (PASS):

| Requirement | Status | Details |
|---|---|---|
| D054 (Median-only) | **PASS** | `analyze_n500_unified.py` and `analyze_n500.py` use median + bootstrap CI as primary. `analyze_c2_n500.py` includes mean as reference only. |
| B=10,000 (W4) | **PASS** (after fix #1) | All scripts now use B=10,000. n=500 × 8 conditions × B=10,000 ≈ 10s — acceptable. |
| Per-phase effective n (W5) | **PASS** (after fix #2,#4) | All phases report `effective_n_*` and `null_*_rate` |
| D059 (d_z within-imp only) | **PASS** (after fix #3) | `analyze_n500_unified.py` was already compliant. `analyze_n500.py` fixed. |
| Aggregation script | **PASS** | `analyze_n500_unified.py` is the main one-click script, outputs all required data. `cross_model_analysis.py --n500` handles cross-model. |

### Pipeline readiness: **PASS**

---
