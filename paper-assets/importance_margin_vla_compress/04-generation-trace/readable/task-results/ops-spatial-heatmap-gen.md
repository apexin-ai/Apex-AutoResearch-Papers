# ops spatial heatmap gen

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_spatial_heatmap_gen_20260522T080244_result.json`
- **Structured JSON:** [`e76f80ba7edc8da3e105.json`](../../sessions/e7/e76f80ba7edc8da3e105.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两组数据都完成了。以下是完整对比：

## Object vs Spatial Token Importance 对比

| Metric | Object (seed42) | Spatial (seed42) | 差异 |
|--------|-----------------|------------------|------|
| **Overall mean** | 251.61 | 249.38 | -2.23 |
| **Overall std** | 16.71 | 14.82 | -1.89 |
| **CV** | 0.066 | 0.059 | **-10.6%** |
| **Center (8×8) mean** | 268.01 | 260.38 | -7.63 |
| **Edge (outer) mean** | 246.14 | 245.71 | -0.43 |
| **Center-Edge gap** | 21.87 | 14.67 | **-33%** |
| **Center/Edge ratio** | 1.089 | 1.060 | |
| **Corners mean** | 237.50 | 234.89 | |
| **Top-10% share** | 11.2% | 11.1% | |

## 关键发现

1. **Spatial 的 importance 分布更均匀**：CV 低 10.6%（0.059 vs 0.066），center-edge gap 小 33%（14.67 vs 21.87）。

2. **差异主要来自 center 降低**：Spatial center mean 比 Object 低 7.63（260 vs 268），而 edge 几乎不变（245.7 vs 246.1）。即 Spatial 场景中中心区域的"独占重要性"降低了。

3. **解释 random cliff 差异**：Object 有更强的 center-high pattern → random 删除大概率命中低重要 edge tokens 但偶尔命中关键 center tokens → 方差大、cliff 陡。Spatial 更均匀 → random 删除的影响更 uniform → cliff 更平缓。

## 输出路径
- Spatial heatmap: `artifacts/token_importance_heatmaps/spatial_seed42/`
- Object heatmap: `artifacts/token_importance_heatmaps/object_seed42/`
- Raw norms (.npy): 两个目录各有 `mean_norms.npy`

---
