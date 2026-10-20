# figure regime map v1

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_regime-map-v1_20260515T133952_result.json`
- **Structured JSON:** [`24ac6ac235abddf2e8a4.json`](../../sessions/24/24ac6ac235abddf2e8a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张 figure 已生成并注册：

- **`regime_map_fdr.pdf`** — 4 条 Granger 方向的 -log10(p_FDR) vs α 曲线，灰带标出 α=0.75 detectability boundary，entropy→d1 的 p=0.054 边界点有空心 marker 标注
- **`consensus_heatmap.pdf`** — 5×5 α×method 显著率热图，α=0.75 TY 缺失以灰色 NA 标注，清晰展示 naïve/differenced/threshold 全 sig vs perm_granger/TY 保守的对比模式

脚本：`scripts/plot_regime_map.py`，纯 matplotlib+seaborn，无 GPU 依赖。

---
