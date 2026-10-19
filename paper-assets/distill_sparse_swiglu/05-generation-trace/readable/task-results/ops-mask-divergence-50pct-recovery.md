# ops mask divergence 50pct recovery

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mask-divergence-50pct-recovery_20260519T131648_result.json`
- **Structured JSON:** [`9283b9eed2b470ce9b65.json`](../../sessions/92/9283b9eed2b470ce9b65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

50% sparsity mask divergence 分析**已完成**，无需重启。两张 GPU 均空闲（0 MiB 占用）。

### 结果摘要

| 指标 | 值 |
|------|-----|
| Mean Jaccard | 0.5176 |
| Std Jaccard | 0.0610 |
| Max Jaccard | 0.6852 (layer 0) |
| Min Jaccard | 0.3310 (layer 31) |
| First quarter mean (L0-7) | 0.5804 |
| Middle half mean (L8-23) | 0.5149 |
| Last quarter mean (L24-31) | 0.4602 |

**关键发现**：
- 50% sparsity 下 predictor mask 与 magnitude mask 的平均 Jaccard 仅 0.518，说明 predictor 学到的 mask pattern 与简单 magnitude pruning 有显著差异（~48% 的激活选择不同）
- Layer 0 最高（0.685），layer 31 最低（0.331）——深层 mask 分歧最大
- 呈现从浅层到深层单调递减的趋势：浅层 0.58 → 中层 0.51 → 深层 0.46
- `per_layer_kl_retention` 全部精确 0.5，确认 sparsity 控制正确
- `per_layer_mag_retention` 略高于 0.5（0.500–0.516），magnitude baseline 保留比例基本一致

结果文件：`results/mask_divergence_50pct_activation_34887/llama8b_50pct_mask_divergence_50pct.json`

---
