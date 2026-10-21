# code importance visualization v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_importance_visualization_v2_20260524T160302_result.json`
- **Structured JSON:** [`3e3cefa08ed39aec80b3.json`](../../sessions/3e/3e3cefa08ed39aec80b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有三张图表已在 westd-38929 上成功生成（今天 23:36）：

| 图表 | PDF | PNG |
|------|-----|-----|
| `fig_importance_heatmap` | 1.6 MB | 1.4 MB |
| `fig_importance_comparison` | 291 KB | 293 KB |
| `fig_importance_histogram` | 24 KB | 84 KB |

代码 `visualize_importance.py` 已完整存在，实现了：

1. **Heatmap（Figure 1）**：两行（task 22: "pick up cream cheese → basket" + task 3: "turn on stove → put moka pot"），每行 4 列：原图 / inferno heatmap / k=0.95 pruned / k=0.85 pruned
2. **Comparison（Figure 2）**：L2-Norm vs Random 对比 (k=0.50)，三面板：原图 / L2 retained / Random retained
3. **Histogram（Figure 3）**：30 帧（10 tasks × 3）聚合的 L2 norm 分布，标注 k=0.85/0.90/0.95 阈值线和 Cliff Zone

技术要点：
- SigLIP 224×224，patch=14 → 16×16 = 256 vision tokens/image
- Importance = L2 norm of projected embeddings (vision_tower → multi_modal_projector)
- 使用 GPU 1（空闲），模型加载 ~11GB
- 学术 matplotlib 风格：serif 字体、无网格、(a)(b)(c) 标注、colorbar、300 dpi PDF+PNG

输出路径：`/root/autodl-tmp/importance_margin_vla_compress/artifacts/figures/`

---
