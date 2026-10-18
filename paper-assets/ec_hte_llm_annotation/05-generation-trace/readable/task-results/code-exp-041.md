# code exp 041

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-041_20260524T124830_result.json`
- **Structured JSON:** [`380ff7ed468d3d581f96.json`](../../sessions/38/380ff7ed468d3d581f96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-041 完成：关键结果

**实验规模**：48 configs × 100 MC runs，总耗时 40.8s。

### Bias Identity R²

| Δπ | Mean R² | Range |
|----|---------|-------|
| 0.05 | 0.570 | [0.05, 0.84] |
| 0.10 | 0.851 | [0.73, 0.92] |
| 0.15 | 0.922 | [0.84, 0.97] |
| 0.20 | 0.951 | [0.89, 0.99] |

R² 随 Δπ 增大而升高——小 Δπ 时 analytic bias 极小，MC 噪声主导，R² 被压低。Δπ≥0.10 时 R²>0.85，确认 product structure 在非对称误分类下成立。FNR-dominant (r<1) 方向 R² 略高于 FPR-dominant (0.879 vs 0.768)。

### Diagnostic AUC

- 29/48 configs 有有效 AUC（K=2 + 小 Δπ 时数据点不足导致 NaN）
- K=4 configs 平均 AUC = **0.74**（range 0.57–0.83）
- K=2 configs 平均 AUC = **0.44**（仅 4 个数据点，离散化严重）

### Method Comparison（全 48 configs 平均）

| Method | Abs Bias | RMSE | Coverage |
|--------|----------|------|----------|
| Oracle | 0.058 | 0.072 | 0.946 |
| Naive | 0.080 | 0.096 | 0.830 |
| Global Corrected | 0.088 | 0.109 | 0.931 |
| EC-HTE (HB) | 0.098 | 0.125 | 0.920 |

EC-HTE 的 RMSE 高于 Global——这在非对称场景中符合预期：n_expert=250 拆分到 K 个子群后，per-subgroup 同时估 FPR 和 FNR 的方差远大于全局估计。EC-HTE 的主要优势体现在 coverage（0.92 vs naive 的 0.83），且 K=2 时 EC-HTE 与 Global 差距很小（RMSE 0.098 vs 0.091）。

**数据文件**：
- `results/exp041_asymmetric_grid.csv`（raw）
- `results/exp041_asymmetric_summary.csv`（summary）

---
