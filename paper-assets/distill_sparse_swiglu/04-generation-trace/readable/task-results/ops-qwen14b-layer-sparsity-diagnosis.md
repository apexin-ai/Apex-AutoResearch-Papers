# ops qwen14b layer sparsity diagnosis

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen14b-layer-sparsity-diagnosis_20260519T134302_result.json`
- **Structured JSON:** [`cd91f66227c270d066d2.json`](../../sessions/cd/cd91f66227c270d066d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here's the full report:

---

## 结果

### 1. 每个 seed 前 6 层 weight statistics

三个 seed 的权重分布高度一致，没有显著差异：

| Layer | down.weight std | up.bias mean | 趋势 |
|-------|----------------|-------------|------|
| L0 | 0.012-0.016 | +0.005~+0.006 | 正 bias |
| L1 | 0.011-0.012 | -0.015~-0.018 | 负 bias |
| L2 | 0.013-0.015 | -0.026~-0.028 | 最负 bias |
| L3 | 0.015-0.016 | -0.021~-0.023 | 负 bias |
| L4 | 0.014-0.015 | -0.016~-0.017 | 负 bias |
| L5 | 0.016-0.018 | -0.007~-0.009 | 接近零 |

### 2. Sigmoid 行为（随机输入）

| Layer | s42 active | s123 active | s456 active | 预测稀疏度 |
|-------|-----------|-------------|-------------|-----------|
| L0 | 0.538 | 0.565 | 0.576 | ~45% |
| L1 | 0.249 | 0.236 | 0.319 | ~73% |
| L2 | 0.205 | 0.189 | 0.192 | ~80% |
| L3 | 0.394 | 0.328 | 0.337 | ~65% |
| L4 | 0.461 | 0.436 | 0.459 | ~55% |
| L5 | 0.480 | 0.459 | 0.442 | ~53% |

对比深层：L20-25 active=0.57-0.63，L43-47 active=0.68-0.75。

### 3. 结论：所有 seed 都有，不是 s42 特有

三个 seed 的 predictor 权重统计几乎一致。**这是系统性问题。**

### 4. 根因分析：eval pipeline 的 `scores = mag * hard_mask` 公式在 uniform top-k 下退化

Bug 在 `lm_eval_sparse_uniform.py` 的 score 计算逻辑：

```python
hard_mask = (logits > 0).float()        # 预测"保留"的神经元
scores = (mag * hard_mask).mean(dim=(0,1))  # 只有 hard_mask=1 的神经元有非零 score
```

然后 `_uniform_topk_masks` 做 per-layer top-k：
```python
num_keep = int(13824 * 0.7)  # = 9676
thr = torch.topk(s, 9676).values[-1]  # 如果非零 score 不足 9676 个 → thr = 0
masks[li] = (s >= thr)  # 0 >= 0 = True → 所有神经元保留 → sparsity = 0
```

**退化条件**：predictor 预测的 active ratio < (1 - sparsity_target) = 0.7。

- L1-4：predictor 预测 active 20%-46% < 70% → 非零 score 不足 → threshold=0 → 全保留 → **sparsity=0.000**
- L0：虽然随机输入下 active=54%，但真实数据上可能更高（>70%）→ 正常
- L5+：active 48%-75%，真实数据上普遍 >70% → 正常

**模型级别**：4/48 层 sparsity=0 → 整体从 30% 降到 27.5%，完全解释了观测。

### 根因总结

**不是 predictor 训练问题，是 eval 的 score 公式 bug。** predictor 正确地学到了"前几层应该更稀疏"，但 `mag * hard_mask` 公式在 predicted sparsity > target sparsity 时退化为全零 score，uniform top-k 的 `>=` 比较让所有神经元通过。

**修复方向**：score 应直接用 `sigmoid(logits)` 或 `logits` 本身，而非 `mag * hard_mask` 乘积。

---
