# code mask visualization

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mask_visualization_20260518T183453_result.json`
- **Structured JSON:** [`4be7aeb109669030f557.json`](../../sessions/4b/4be7aeb109669030f557.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 3 个图已成功生成并保存。

### 产出总结

**脚本**: `/root/distill_sparse_swiglu/src/visualize_mask_patterns.py`

**生成的图片**（PDF + PNG，300 dpi，均在 `/root/distill_sparse_swiglu/figures/` 和 `artifacts/`）：

| 图 | 文件名 | 尺寸 | 关键发现 |
|---|---|---|---|
| Fig 1: Layer-wise Divergence Heatmap | `mask_divergence_heatmap.{pdf,png}` | 双栏宽 6.75" | Jaccard distance 0.34-0.69; 50% sparsity 平均 0.515（超过一半 neuron 选择不同） |
| Fig 2: Neuron Importance Scatter | `neuron_scatter_layer16.{pdf,png}` | 单栏宽 3.3" | Layer 16 有 35.4% disagreement (2497 KL-only, 2585 mag-only) |
| Fig 3: Concrete Mask Comparison | `mask_comparison.{pdf,png}` | 双栏宽 6.75" | Layers 2/16/28 的 KL vs magnitude binary mask 并排对比 |

**关键 takeaway**: 50% sparsity 下 KL predictor 和 magnitude pruning 平均有超过 50% 的 Jaccard distance，说明 KL distillation 学到了显著不同于 magnitude-based pruning 的 sparsity pattern。这为论文中 "KL discovers fundamentally different mask patterns" 的 claim 提供了直接 visual evidence。

---
