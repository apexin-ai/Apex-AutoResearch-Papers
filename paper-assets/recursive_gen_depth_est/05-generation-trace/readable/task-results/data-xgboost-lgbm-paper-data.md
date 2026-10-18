# data xgboost lgbm paper data

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_xgboost_lgbm_paper_data_20260515T194627_result.json`
- **Structured JSON:** [`d451a21562f25de915e4.json`](../../sessions/d4/d451a21562f25de915e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册 (`art_20260515_e69dad`)。以下是完整提取结果：

---

## Table 2 新行

| Method | 4-class Acc (%) | std (%) |
|--------|:-:|:-:|
| **XGBoost (GPU)** | **79.0** | 0.5 |
| **LightGBM (CPU)** | **78.8** | 0.8 |

XGBoost 以 79.0% 成为当前所有 baseline 中最高（RF 78.2%、CORAL 78.1%），LightGBM 78.8% 位列第二。

## Per-class Recall

| | d0 | d1 | d2 | d3 |
|--|:-:|:-:|:-:|:-:|
| XGBoost | 0.994 | 0.816 | 0.596 | 0.754 |
| LightGBM | 0.994 | 0.815 | 0.596 | 0.747 |

两者 recall 分布几乎一致，d2 仍是最难区分的类别。

## Pairwise AUC

| | d0v1 | d1v2 | d2v3 |
|--|:-:|:-:|:-:|
| XGBoost | 1.000 | 0.931 | 0.816 |
| LightGBM | 1.000 | 0.931 | 0.814 |

## 5-fold Accuracies

- **XGBoost**: 78.3, 79.3, 78.9, 78.8, 79.7
- **LightGBM**: 77.6, 79.1, 78.5, 79.0, 79.9

## Feature Importance

脚本未计算 XGBoost/LightGBM 的 feature importance。如需对比，需要补跑一个带 `clf.feature_importances_` 提取的版本。RF Top-5 供参考：var_surprisal (0.169) > p90_ppl (0.158) > mean_ppl (0.120) > mean_surprisal (0.088) > p75_ppl (0.067)。

---
