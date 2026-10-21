# exp r3w5 xgboost lgbm baseline

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_r3w5_xgboost_lgbm_baseline_20260515T193827_result.json`
- **Structured JSON:** [`40a0dace01d8fff261ec.json`](../../sessions/40/40a0dace01d8fff261ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 和 artifact 已更新。

## 结果

| Method | 4-class Acc | d0v1 AUC | d1v2 AUC | d2v3 AUC |
|--------|------------|----------|----------|----------|
| RF (ref) | 78.2% | 0.861 | — | 0.800 |
| **XGBoost** | **79.0% ± 0.5%** | 1.000 | 0.931 | 0.816 |
| **LightGBM** | **78.8% ± 0.8%** | 1.000 | 0.931 | 0.814 |

**Per-class recall（三方法一致）：** d0=0.994, d1=0.816, d2=0.596, d3=0.754

**结论：** 三种分类器（RF/XGBoost/LightGBM）收敛到 78-79%，证实信号天花板在 19 维特征而非分类器。d2 recall 最低（~0.60）是跨分类器的特征级限制，d2v3 是最难区分的相邻对（AUC ~0.81）。LightGBM 因服务器无 OpenCL 回退到 CPU，不影响结论。

---
