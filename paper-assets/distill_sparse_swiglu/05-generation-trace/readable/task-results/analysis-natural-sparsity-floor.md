# analysis natural sparsity floor

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_natural_sparsity_floor_20260517T041924_result.json`
- **Structured JSON:** [`136d0f121afb0326b1f3.json`](../../sessions/13/136d0f121afb0326b1f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果总结：

## 自然稀疏下限分析结果

**核心发现：自然稀疏下限极低（0.06%），28.5% 的实际稀疏度几乎完全是动态的。**

### Per-Layer Always-Pruned 分布 (threshold=0.1)

| 区间 | 层 | Always-Pruned | 特征 |
|------|-----|---------------|------|
| Early (0-7) | L0-L7 | **0** | 没有任何 neuron 被永久 prune |
| Mid (8-14) | L8-L14 | **0** | 同上 |
| Mid-Late (15-27) | L15-L27 | **2-9/层** | 极少量，占比 <0.06% |
| Late (28-31) | L28-L31 | **39-73/层** | 唯一有明显信号的区域，最高 L31=0.51% |

### 关键数字
- **总计 always-pruned**: 278 / 458,752 neurons = **0.06%**
- **Threshold 灵敏度**: thresh=0.05 → 0.01%, thresh=0.1 → 0.06%, thresh=0.2 → 0.44%
- **Gate prob 分布**: 53% 的 neuron 平均 gate prob 在 0.5-0.7 之间（高度动态）

### 解读

1. **28.5% 实际稀疏度不是来自"永久 dead neurons"**。predictor 学到的几乎全是 contextual/token-dependent 的 pruning 决策。
2. **Late layers (28-31) 有略高的静态稀疏**，但也仅 0.27%-0.51%。这些层的 gate prob 方差更大（std 0.19-0.22 vs 早期层 0.06-0.10），说明 predictor 在这些层做了更极端的分化。
3. **层间 mean gate prob 呈倒 U 形**：早期层 ~0.55-0.58，中间层上升至 ~0.71（L17-21），后期回落至 ~0.51-0.72。中间层保留更多 neuron，早期和晚期 prune 更积极。

JSON 已保存到服务器 `/root/distill_sparse_swiglu/artifacts/natural_sparsity_floor_analysis.json` 并注册为 artifact。

---
