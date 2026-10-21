# ops mask divergence 50pct 64samples

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mask-divergence-50pct-64samples_20260519T121559_result.json`
- **Structured JSON:** [`597113f40f0e02bbe61c.json`](../../sessions/59/597113f40f0e02bbe61c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已存在，无需重新运行。结果汇总：

**50% Sparsity Mask Divergence (64 samples, 131K tokens)**

| Metric | Value |
|--------|-------|
| Mean Jaccard Distance | **0.6824 (68.24%)** |
| Min (layer 31) | 0.5234 |
| Max (layer 26) | 0.7517 |

论文声称的 ~68% divergence 与实测数据一致。数据来源文件 `/root/distill_sparse_swiglu/figures/mask_stats_50pct_64samples.json`，已注册为 artifact `art_20260519_bb2328`。

---
