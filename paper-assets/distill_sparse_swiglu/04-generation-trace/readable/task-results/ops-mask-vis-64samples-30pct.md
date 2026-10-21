# ops mask vis 64samples 30pct

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mask-vis-64samples-30pct_20260518T195918_result.json`
- **Structured JSON:** [`8a727ff30773c15aee71.json`](../../sessions/8a/8a727ff30773c15aee71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结如下：

---

### 生成文件（westd-41718: `/root/distill_sparse_swiglu/figures/`）

| 文件 | 大小 |
|------|------|
| `mask_divergence_heatmap_30pct_64samples.pdf` | 14.3 KB |
| `mask_divergence_heatmap_30pct_64samples.png` | 64.1 KB |
| `neuron_scatter_layer16_30pct_64samples.pdf` | 39.4 KB |
| `neuron_scatter_layer16_30pct_64samples.png` | 282.7 KB |
| `mask_comparison_30pct_64samples.pdf` | 15.9 KB |
| `mask_comparison_30pct_64samples.png` | 52.2 KB |
| `mask_stats_30pct_64samples.json` | 998 B |

### 关键数值（64 samples, 131,072 tokens, 30% sparsity）

- **Mean Jaccard similarity**: 0.5374（距离: 0.4626）
- **Neuron scatter disagree (L16)**: 8.71%
- **Per-layer Jaccard similarity 范围**: 0.3999 (L27, 最低) ~ 0.6386 (L31, 最高)
- **深层（L24-L28）divergence 最大**: Jaccard distance 0.55-0.60，说明 KL predictor 在深层与 magnitude mask 分歧最大
- **中间层（L15-L18）agreement 最高**: Jaccard similarity ~0.61-0.63

### 与论文现有数据的一致性

论文报告 50% sparsity 下 Jaccard similarity 平均 47%。30% sparsity 下得到 53.7%，符合预期：sparsity 越低（保留更多神经元），两种 mask 方法重叠越大。

### 注意事项

文件目前仅在 westd-41718 上。本地机器无法直接 scp 到该服务器（缺少 SSH key 配置）。如需将文件传到 westd-34887 或本地，需要额外配置 SSH 互信或通过其他方式传输。

---
