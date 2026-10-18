# ops token position visualization

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_token-position-visualization_20260521T103129_result.json`
- **Structured JSON:** [`53df9504e8ed7994488b.json`](../../sessions/53/53df9504e8ed7994488b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 产出

### 1. 可视化文件
- 远程 PDF: `/root/autodl-tmp/importance_margin_vla_compress/artifacts/token_position_viz.pdf`
- 远程 PNG: `/root/autodl-tmp/importance_margin_vla_compress/artifacts/token_position_viz.png`
- 远程 Heatmap: `/root/autodl-tmp/importance_margin_vla_compress/artifacts/token_norm_heatmap.pdf`
- 服务器: `cqa1-33015`

### 2. 空间聚集度量对比

| k | Method | Clusters | Largest Cluster | Coverage |
|---|--------|----------|-----------------|----------|
| 0.3 | L2-Norm | **3** | **86%** | 78% |
| 0.3 | Random | 6.4 | 36% | 71% |
| 0.5 | L2-Norm | **1** | **100%** | 78% |
| 0.5 | Random | 4.6 | 55% | 89% |
| 0.7 | L2-Norm | 2 | 97% | 100% |
| 0.7 | Random | 1.8 | 95% | 100% |

### 3. 关键发现

**L2 norm 空间聚集效应已确认。** X-VLA 的 vision token L2 norms 的 **CV = 0.0011**（mean=31.91, std=0.04），几乎完全相同。在这种极低 CV 下：

- **k=0.5 时 L2 pruning 的 24 个保留 token 全部落在一个连通区域**（1 cluster, 100%），形成一个大面积空间空洞——模型完全丢失了被剪掉区域的视觉信息
- Random pruning 平均分散为 4.6 个 cluster，最大仅占 55%，空间覆盖率从 78% 提升到 89%
- 机制：DaViT 的局部卷积/注意力使相邻 patch 的 L2 norm 存在空间相关性 → topk 在近乎相同的 norm 值上做决策时，空间相关性决定了哪些 token 被选中 → 形成连续聚集区域

---
