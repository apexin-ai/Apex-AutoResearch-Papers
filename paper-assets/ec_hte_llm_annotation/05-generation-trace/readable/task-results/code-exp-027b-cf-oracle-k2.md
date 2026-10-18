# code exp 027b cf oracle k2

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-027b-cf-oracle-k2_20260522T141342_result.json`
- **Structured JSON:** [`f7f8368bd142fc9fb042.json`](../../sessions/f7/f7f8368bd142fc9fb042.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Results saved to `results/exp_cf_oracle_coverage_k2.csv`.

Key findings from K=2 extreme:

| Method | Coverage | |Bias| | RMSE |
|---|---|---|---|
| **Oracle** | **94.0%** | 0.0023 | 0.056 |
| **EC-HTE true CM** | **94.0%** | 0.0027 | 0.073 |
| **EC-HTE estimated CM** | **92.5%** | 0.0044 | 0.079 |
| Global true CM | 88.5% | 0.045 | 0.083 |
| Global estimated CM | 88.3% | 0.045 | 0.085 |
| **Naive** | **82.8%** | 0.046 | 0.077 |

**Interpretation:**
- Oracle at 94% — CF SE is reasonably calibrated even with K=2.
- EC-HTE true CM = 94%, estimated CM = 92.5% — CM estimation adds only ~1.5pp gap; the per-subgroup correction works well.
- Global correction (~88%) substantially underperforms per-subgroup correction because averaging π=0.05 and π=0.25 into a single global CM introduces systematic bias (visible in the ~0.045 |Bias|).
- Naive at 82.8% — matches the paper's 83-85% range. The coverage gap is driven by misclassification bias (especially subgroup 1 with π=0.25: 68-77% coverage), **not** by CF SE under-calibration.

---
