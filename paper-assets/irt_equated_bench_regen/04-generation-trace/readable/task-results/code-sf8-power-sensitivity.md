# code sf8 power sensitivity

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sf8_power_sensitivity_20260521T201752_result.json`
- **Structured JSON:** [`2be826ef1f768edd415a.json`](../../sessions/2b/2be826ef1f768edd415a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 deliverables generated in `artifacts/sf8_power_sensitivity/`:

| File | Content |
|------|---------|
| `param_descriptives.csv` | Descriptive stats for PSN-IRT (14,042 items) and MetaBench (12,508 items) |
| `sensitivity_results.csv` | TPR/FPR across 6 discrimination levels, 1000 reps each |
| `sf8_report.md` | Markdown report with tables and interpretation |
| `sf8_power_sensitivity.py` | Reproduction script |

**Key results**:

- **Descriptives**: PSN-IRT MMLU has mean a=1.197 (SD=0.542), mean b=-0.838 (SD=0.790). MetaBench uses a different scale (mean disc=0.076) — different IRT calibration, not directly comparable.

- **Sensitivity** (Δb=1.4 logit shift, N=80/group, 10% contamination):

| a | TPR (ETS C) | 95% CI | FPR |
|---|-------------|--------|-----|
| 0.5 | 0.398 | [0.20, 0.60] | 0.033 |
| 0.8 | 0.683 | [0.45, 0.90] | 0.036 |
| 1.0 | 0.808 | [0.60, 0.95] | 0.038 |
| 1.2 | 0.874 | [0.70, 1.00] | 0.038 |
| 1.5 | 0.930 | [0.80, 1.00] | 0.038 |
| 2.0 | 0.949 | [0.80, 1.00] | 0.037 |

All 3 validation checks pass: TPR monotonically increases with a, FPR <0.05 everywhere, and at a≈1.2 the TPR (0.874) is consistent with Phase 2's aggregate 0.68 (which mixes items across the full a distribution including low-discrimination items that drag the average down).

---
