# ops mask vis 64samples 50pct

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mask-vis-64samples-50pct_20260518T195924_result.json`
- **Structured JSON:** [`ec0d9056789170ed7d74.json`](../../sessions/ec/ec0d9056789170ed7d74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。50% sparsity + 64 samples 的 3 张可视化已生成。

## 产出文件

| 图 | PDF | PNG |
|---|---|---|
| 1. Mask divergence heatmap | `figures/mask_divergence_heatmap_50pct_64samples.pdf` | `.png` |
| 2. Neuron scatter (Layer 16) | `figures/neuron_scatter_layer16_50pct_64samples.pdf` | `.png` |
| 3. Mask comparison grid | `figures/mask_comparison_50pct_64samples.pdf` | `.png` |
| Stats JSON | `figures/mask_stats_50pct_64samples.json` | |

## 关键数值

- **Mean Jaccard similarity: 0.3176 (31.8%)**
- **Mean Jaccard distance: 0.6824 (68.2%)**
- Neuron scatter disagree (Layer 16): 40.6%
- Total tokens analyzed: 131,072 (64 samples x 2048 seq_len)
- Jaccard range: 0.2483 (Layer 26) ~ 0.4766 (Layer 31)

**注意**: 64 samples 下 Jaccard 均值 31.8% 与论文中引用的 47% 有显著差异。论文中写的 47% 可能来自之前 16 samples 或不同的计算口径（WikiText-2 eval set vs WikiText-103 calibration）。需要检查论文中 47% 的原始来源，考虑是否需要更新论文数据。

---
