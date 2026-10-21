# code task h treatment dep misclass

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_task-h-treatment-dep-misclass_20260523T154056_result.json`
- **Structured JSON:** [`33176af718c6ddbbdc0e.json`](../../sessions/33/33176af718c6ddbbdc0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. All outputs generated:

- **Raw CSV**: `results/exp_treatment_dep_misclass.csv` (6000 rows)
- **Summary CSV**: `artifacts/treatment_dep_misclass_summary.csv`
- **Figure**: `artifacts/treatment_dep_misclass_figure.pdf` + `.png`

**Key findings:**

| gamma_T | EC-HTE Coverage | EC-HTE RMSE | EC-HTE/Global RMSE |
|---------|----------------|-------------|---------------------|
| 0.00    | 0.945          | 0.075       | 0.844               |
| 0.05    | 0.897          | 0.092       | 0.924               |
| 0.10    | 0.750          | 0.133       | 1.009               |
| 0.15    | 0.525          | 0.177       | 1.045               |
| 0.20    | 0.370          | 0.224       | 1.064               |

- **gamma_T=0.15 EC-HTE coverage = 52.5%** — well below 93%.
- **Breakeven point**: gamma_T ≈ 0.10 — EC-HTE loses its RMSE advantage over global correction.
- At gamma_T=0 (no violation), EC-HTE dominates: best coverage (94.5%) and lowest RMSE (0.075).
- Treatment-dependent misclassification degrades all methods sharply. EC-HTE is slightly *more* sensitive than global correction at high gamma_T because per-subgroup CM estimates become biased when the expert sample's treatment composition doesn't match the full sample perfectly.

---
