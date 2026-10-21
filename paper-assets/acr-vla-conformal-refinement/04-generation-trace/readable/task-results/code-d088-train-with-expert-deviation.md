# code d088 train with expert deviation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d088-train-with-expert-deviation_20260520T162806_result.json`
- **Structured JSON:** [`132964d4a193de3e807b.json`](../../sessions/13/132964d4a193de3e807b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 训练结果报告

### 数据统计
| 指标 | 值 |
|---|---|
| 样本数 N | 65,223 (K=1 object cache) |
| Expert deviation 范围 | [0.0338, 3.1002] |
| Mean / Median | 0.5054 / 0.4276 |
| P10 / P25 / P75 / P90 / P95 | 0.2047 / 0.2922 / 0.6320 / 0.9038 / 1.1150 |
| Binary label 比例 (>median) | 50.0% (32611 / 65223) |
| Unique tasks | 10 |

### 训练结果
| 指标 | 值 |
|---|---|
| Best val loss (BCE) | **0.5217** |
| Val accuracy (τ=0.42) | **73.15%** |
| Val F1 | **0.7674** |
| Val Precision | 0.6816 |
| Val Recall | 0.8778 |
| Val AUC | **0.8131** |
| 训练 epoch | 100 (未 early stop) |

### 校准阈值
- **τ = 0.42** (最大化 F1 score)

### 模型保存路径
- Checkpoint: `/root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt`
- Threshold: `/root/autodl-tmp/checkpoints/uncertainty_head_v1/threshold.json`
- 模型参数量: 15,665 (960→16→16→1 MLP)

### 关键观察
- AUC=0.81 说明模型在区分"VLA 准确"vs"VLA 不准确"方面有较好的判别力
- Recall=0.88 高于 Precision=0.68，模型倾向于将更多样本标记为"需要校正"（保守策略，适合安全关键场景）
- Prediction 分布 mean=0.51, std=0.27, range=[0.0005, 0.9764]，分布合理

---
