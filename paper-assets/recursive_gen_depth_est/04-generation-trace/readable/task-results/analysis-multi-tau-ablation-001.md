# analysis multi tau ablation 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multi_tau_ablation_001_20260516T023357_result.json`
- **Structured JSON:** [`2da1673c9c37e56ccaae.json`](../../sessions/2d/2da1673c9c37e56ccaae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 和 artifact 已更新。以下是分析总结：

---

## multi_tau_ablation_001 结果分析

### Within-τ 分类（5-fold CV）

| τ | 4-class acc | d0v1 AUC | d1v2 AUC | d2v3 AUC |
|---|---|---|---|---|
| 0.5 | 77.3% [75.4, 79.2] | 0.996 | **0.842** | 0.764 |
| 0.7 | 75.4% [73.5, 77.1] | 0.997 | **0.851** | 0.720 |
| 0.9 | 75.9% [74.2, 77.7] | 0.991 | **0.808** | 0.781 |
| 1.1 | 57.2% [55.2, 59.4] | 0.988 | **0.528** | 0.599 |

### d1v2 AUC 趋势
- **非单调**：0.842 → 0.851 (peak at τ=0.7) → 0.808 → 0.528
- **τ ∈ [0.5, 0.9] 区间稳定**：d1v2 AUC 全部 > 0.80，depth signal 鲁棒
- **τ=1.1 悬崖式下降**：d1v2 降至 0.528（近随机），4-class acc 降至 57%
- d0v1 AUC 在所有 τ 都 > 0.98，说明 depth-0 vs depth-1 的区分力不受温度影响

### τ=1.1 崩溃机制
训练 loss 揭示了原因：
- τ=0.5: depth-0=2.27 → depth-1=0.42 → depth-2=0.16（loss 急剧下降，低温下模型快速记忆自身输出）
- τ=1.1: depth-0=2.27 → depth-1=1.91 → depth-2=1.85（loss 几乎不降，高温输出太随机，模型无法学到自身模式）

**结论**：τ>1.0 时，温度放大使得 token 分布随机性过大，深层递归的 memorization 效应消失，depth-dependent 的统计特征被噪声淹没。

### Cross-τ LOO

| Holdout | acc | d1v2 AUC |
|---|---|---|
| τ=0.5 | 52.2% | 0.176 (inverted!) |
| τ=0.7 | 41.0% | 0.299 |
| τ=0.9 | 46.4% | 0.277 |
| τ=1.1 | 47.1% | 0.525 |
| **Mean** | **46.7%** | **0.319** |

Mean acc = 46.7% < 55% 阈值。**跨温度泛化失败**。特征分布是 τ-specific 的——在一个温度上训练的分类器无法迁移到另一个温度。

### Feature Importance 稳定性（来自已有 per-τ 实验）
Top-5 特征跨 τ 一致：**var_surprisal, p90_ppl, mean_ppl, mean_surprisal, p75_ppl**，只有排名顺序有微小差异。

### 与已有参考数据对比
- nucleus p=0.95: 78.2% / 0.861 → 本实验 τ=0.7 最接近: 75.4% / 0.851
- 之前 temp09: 76.3% / 0.833 → 本实验 τ=0.9: 75.9% / 0.808（CV split 方差范围内）

### 判定：**success**

三个有价值的发现：
1. **τ ∈ [0.5, 0.9] 内 depth signal 鲁棒**，不是单一温度的伪影
2. **τ=1.1 是有意义的边界条件**，可归因于 training-loss saturation
3. **Cross-τ 不可迁移**是重要的方法论 caveat——depth features 是 τ-dependent 的，论文中需要明确说明

### 缺失数据
Pipeline 未计算：per-τ feature importance、3-class accuracy、contamination rates、W&B logging。

---
