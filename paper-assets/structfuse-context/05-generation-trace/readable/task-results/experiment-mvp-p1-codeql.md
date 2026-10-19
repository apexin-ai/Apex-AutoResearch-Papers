# experiment mvp p1 codeql

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_mvp_p1_codeql_20260512T103754_result.json`
- **Structured JSON:** [`ba23b5d4f93678fc3951.json`](../../sessions/ba/ba23b5d4f93678fc3951.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline complete. Both checks **PASS**.

---

## MVP Phase 1 Results

### Phase 1a: CodeQL Pilot — **PASS**

| Instance | DB(s) | CG(s) | DF(s) | Reachable Files | Status |
|---|---|---|---|---|---|
| flask-4045 | 0 | 7.0 | 11.6 | 15/83 | OK |
| requests-1963 | 0 | 7.4 | 12.5 | 9/37 | OK |
| pytest-11143 | 0 | 9.3 | 17.7 | 41/262 | OK |
| pylint-5859 | 0 | 22.9 | 35.5 | 36/2366 | OK |
| xarray-3364 | 0 | 2.2 | 2.3 | 1/236 | OK |
| astropy-12907 | 0 | 24.6 | 28.5 | 20/995 | OK |
| sphinx-10325 | 0 | 16.4 | 31.1 | 131/774 | OK |
| matplotlib-18869 | 43 | 119.8 | 167.1 | 164/912 | OK |

- **Timeout rate: 0%** (threshold <30%)
- CG mean: 29.6s, max: 119.8s (matplotlib's `__init__`)
- DF mean: 43.4s, max: 167.1s
- 2 repos skipped (seaborn: buggy file not found, scikit-learn: buggy file not found)

### H2 Sanity Check — **PASS**

Gold patch file coverage:
- **Connected files**: 1.44% contain gold patch file
- **Disconnected files**: 0.00%
- **Fisher exact test**: OR=inf, p=0.0000

Per-instance breakdown: 6/8 repos have the gold patch file in the connected set (75%). xarray and requests missed (xarray had only 1 connected file due to CG/DF query failure returning only the buggy file itself; requests' gold file was structurally disconnected).

Report saved to `/root/autodl-tmp/mvp_results/mvp_phase1_report.json`.

---
