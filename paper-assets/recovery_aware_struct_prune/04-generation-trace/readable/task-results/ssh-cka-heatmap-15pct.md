# ssh cka heatmap 15pct

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cka_heatmap_15pct_20260521T013817_result.json`
- **Structured JSON:** [`6eb5d565c60d1d79ca8c.json`](../../sessions/6e/6eb5d565c60d1d79ca8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Diagonal CKA 均值

| Method | 15% sparsity | 20% sparsity |
|--------|-------------|-------------|
| **CKA-only** | **0.6104** | 0.6202 |
| **Standard** | **0.8958** | 0.9039 |

### 15% vs 20% 对比
- CKA-only: 15% 略低于 20%（0.610 vs 0.620），差异很小，说明 CKA-only 剪枝在两个 sparsity 下都大幅重塑了中间层表征（layer 9-23 区间 diagonal CKA 低至 0.42-0.51）
- Standard: 15% 与 20% 非常接近（0.896 vs 0.904），整体保留了与 dense 模型的高相似度

### Heatmap 特征
- CKA-only 15%：浅层（0-3）和深层（26）保留高相似度（>0.9），中间层（9-23）CKA 大幅下降至 0.4-0.5，表征发生显著重组
- Standard 15%：整体对角线高相似度（>0.7），浅层 4-6 处有一个低谷区域，但仍远高于 CKA-only

### 文件路径
- Heatmap 图: `/root/autodl-tmp/recovery_aware_struct_prune/results/cka_15pct/cka_heatmap_15pct.png`
- CKA-only JSON: `/root/autodl-tmp/recovery_aware_struct_prune/results/cka_15pct/cka_heatmap_cka_only_15.json`
- Standard JSON: `/root/autodl-tmp/recovery_aware_struct_prune/results/cka_15pct/cka_heatmap_standard_15.json`
- Dense reprs cache: `/root/autodl-tmp/recovery_aware_struct_prune/results/cka_15pct/dense_reprs.pt`

---
