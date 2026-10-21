# compute deberta c4 analysis

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_deberta-c4-analysis_20260519T202724_result.json`
- **Structured JSON:** [`8ca51b896e8bfc66cf3c.json`](../../sessions/8c/8ca51b896e8bfc66cf3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已有完整结果。训练脚本已自动完成 pairwise AUC + bootstrap CI + F1@0.50 + K* 计算。

## exp_deberta_c4 (DeBERTa-v3-base on C4 14B) Results

| Depth Pair | N | AUC | 95% CI | F1@0.50 |
|------------|---|-----|--------|---------|
| 0v1 | 10,000 | 0.9941 | [0.9930, 0.9951] | 0.9352 |
| 1v2 | 10,000 | 0.6781 | [0.6696, 0.6866] | 0.6751 |
| 2v3 | 10,000 | 0.5895 | [0.5814, 0.5979] | 0.6607 |
| 3v4 | 10,000 | 0.5651 | [0.5573, 0.5732] | 0.6204 |
| 4v5 | 10,000 | 0.5485 | [0.5411, 0.5562] | 0.2869 |

**K\* (θ=0.60) = 1**

- 30,000 samples, 5,000 docs, 5-fold CV, 10,000 bootstrap resamples
- 训练耗时 48.3 min

### 关键发现

- **0v1 区分度极高**（AUC 0.994）：depth-0（原始）vs depth-1（一次改写）几乎完全可分，说明首次生成改写留下了明显的风格/分布偏移信号。
- **1v2 开始急剧下降**（AUC 0.678）：一次改写 vs 两次改写的区分度大幅衰减，但 CI lower (0.670) 仍 > 0.60 阈值。
- **2v3 及之后接近随机**（AUC 0.565–0.590）：CI lower 均 < 0.60，分类器无法有效区分更深层的改写。
- **K\* = 1**：只有 0v1 这一对的 CI lower > θ=0.60。这意味着 DeBERTa 在 C4 数据上只能可靠区分"原始文本 vs 被改写过的文本"，无法区分改写的具体深度（1次 vs 2次 vs 更多次）。

---
