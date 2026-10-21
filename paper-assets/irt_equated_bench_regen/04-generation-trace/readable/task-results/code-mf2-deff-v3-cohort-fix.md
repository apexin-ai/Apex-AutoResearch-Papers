# code mf2 deff v3 cohort fix

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mf2_deff_v3_cohort_fix_20260522T110522_result.json`
- **Structured JSON:** [`ef952e99ea704330664c.json`](../../sessions/ef/ef952e99ea704330664c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All validations pass:

- **Valid models = 1884** < 1887 (3 models had no family match in response matrix)
- **m̄_weighted (254.48) > m̄_simple (62.80)** — skewed family sizes confirmed
- **Adjusted C%**: weighted = 13.51%, simple = 29.17% — both ≤ 31.3%
- **Simple DEFF = 3.87** — falls in reviewer's expected 3–5 range

Key changes from v2 (2118 models → 1884 ref+foc):
| Variant | DEFF | Adjusted C% |
|---------|------|------------|
| v2 (all families) | — | 17.45% |
| v3 weighted | 12.79 | 13.51% |
| v3 simple | 3.87 | 29.17% |

Output files written to `artifacts/mf2_deff_estimation/`:
- `mf2_deff_estimation_v3.py`
- `deff_results.csv` (16 columns, both DEFF variants)
- `deff_summary.md`

---
