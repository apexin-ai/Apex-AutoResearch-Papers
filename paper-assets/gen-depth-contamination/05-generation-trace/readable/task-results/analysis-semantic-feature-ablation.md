# analysis semantic feature ablation

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_semantic_feature_ablation_20260517T151744_result.json`
- **Structured JSON:** [`566bfdbb142c427bc09f.json`](../../sessions/56/566bfdbb142c427bc09f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果已保存到 `artifacts/semantic_ablation_report.json`。

## 结果摘要

| Depth Pair | 15D AUC | 17D AUC | Diff |
|---|---|---|---|
| 0v1 | 0.9225 | 0.9232 | +0.0007 |
| 1v2 | 0.6123 | 0.6099 | -0.0024 |
| 2v3 | 0.5274 | 0.5239 | -0.0035 |
| 3v4 | 0.5169 | 0.5201 | +0.0032 |
| 4v5 | 0.5162 | 0.5120 | -0.0042 |

**K\* = 2（15D 和 17D 相同，无变化）**

### 特征重要性（17D 模型）
- `semantic_cosine_sim`: rank 11/17（importance=277.8）
- `entity_diversity`: rank 17/17（importance=76.8，最末）

### 结论
K\* 不变（均为 2）。语义特征不改变 discrimination boundary。两个新增特征排名靠后（平均 rank 14/17），表层统计特征（surprisal stats、freq entropy）主导分类。AUC 差异均在 ±0.005 范围内，属于噪声级别波动。

---
