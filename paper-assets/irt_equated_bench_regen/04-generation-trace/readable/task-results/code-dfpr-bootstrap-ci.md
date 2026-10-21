# code dfpr bootstrap ci

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dfpr_bootstrap_ci_20260521T074450_result.json`
- **Structured JSON:** [`da0c75cbef8b4586948d.json`](../../sessions/da/da0c75cbef8b4586948d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All artifacts registered. Summary:

**Bootstrap ΔFPR analysis complete** (1000 resamples × 5 subjects, 325s total).

Results per subject:

| Subject | ΔFPR | 95% CI | SE | Baseline FPR 95% CI |
|---------|------|--------|-----|---------------------|
| business_ethics | 0.000 | [0.000, 0.000] | 0.000 | [0.467, 0.600] |
| human_aging | 0.000 | [0.000, 0.000] | 0.000 | [0.350, 0.479] |
| professional_medicine | 0.000 | [0.000, 0.000] | 0.000 | [0.342, 0.452] |
| formal_logic | 0.000 | [0.000, 0.000] | 0.000 | [0.318, 0.398] |
| high_school_statistics | 0.000 | [0.000, 0.000] | 0.000 | [0.303, 0.393] |

0 non-zero ΔFPR iterations out of 5000 total. The zero is not a coincidence — it's algebraically guaranteed: cross-subject stratification scores and clean item responses are both invariant to within-subject injection, so the MH-DIF inputs for clean items are numerically identical at p=0 and p=1 regardless of which models are sampled. The report includes this proof.

Output files in `artifacts/plan_016_supplement/`:
- `bootstrap_dfpr.py` — code
- `bootstrap_dfpr_report.md` — report with method, results, algebraic proof
- `bootstrap_dfpr_results.csv` — per-subject summary
- `bootstrap_dfpr_samples.csv` — 5000 raw bootstrap iterations

---
