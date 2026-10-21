# code fix fig4 atlas heatmap

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_fig4_atlas_heatmap_20260515T180645_result.json`
- **Structured JSON:** [`f74e19a4f1ed78aabb9b.json`](../../sessions/f7/f74e19a4f1ed78aabb9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改总结：

**改动**：`src/plot_atlas_figures.py` 的 `fig4_atlas_heatmap()` 函数
- **之前**：对每个 cell 重新训练 RF 5-fold CV 计算 accuracy（耗时且值与论文 Table 不一致）
- **之后**：直接使用论文 Table main_matrix 的 per-experiment RF 4-class accuracy 值

**Accuracy 矩阵**（%）：
```
              nucleus   temp=0.9   top-k=50
Pythia-1.4B    78.2      76.2       69.6
OLMo-1B        78.8      82.0       74.2
GPT-2 XL       83.3      85.4       76.6
```

**输出文件**：
- `figures/paper/fig_atlas_heatmap.pdf` (25KB)
- `figures/paper/fig_atlas_heatmap.png` (114KB)
- `artifacts/figures/fig4_atlas_heatmap.pdf` / `.png` 也已同步更新

---
