# code exp 003 hb rerun

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-003-hb-rerun_20260521T023504_result.json`
- **Structured JSON:** [`a4c6848b6ddc03000e6a.json`](../../sessions/a4/a4c6848b6ddc03000e6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete. Results verified (301 rows summary, 30,001 rows raw). Here's the HB vs stratified_mle comparison:

**Legend:** positive = HB wins (lower RMSE), `***` = HB loses by >20%, `++` = HB wins by >10%

| Regime | n_exp | Pattern |
|--------|-------|---------|
| **extreme** | 50 | S0/S1: HB slightly better (+3–9%). S2: mixed (+15% z0, **-44% z1 \*\*\***). S3: **HB much worse (-57% z0 \*\*\*)** |
| **extreme** | 100 | S0–S2: HB modestly better (+1–8%). S3: **HB strongly wins (+26/+60% ++)** |
| **extreme** | 250 | S0–S2: HB slightly better (+1–4%). S3: HB wins (+6/+17% ++) |
| **extreme** | 500 | All subgroups converge, HB ≈ MLE (<2% difference) |
| **moderate** | 50 | S0/S1: HB slightly better. S2: mixed. S3: **HB much worse (-17/-54% \*\*\*)** |
| **moderate** | 100 | S0–S2: HB modestly better. S3: **HB wins (+11/+24% ++)** |
| **moderate** | 250–500 | All converge, small HB advantage |

**Key takeaway:** At n=50, HB over-shrinks the rare high-misclassification subgroup S3, producing worse RMSE (the `***` flags). At n>=100, HB's partial pooling pays off, especially for S3 where it wins substantially. By n=500, both methods converge.

---
