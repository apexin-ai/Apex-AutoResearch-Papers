# ops plot figures pilot

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plot-figures-pilot_20260521T063637_result.json`
- **Structured JSON:** [`9b25d185bfd7e704b96a.json`](../../sessions/9b/9b25d185bfd7e704b96a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 PDF 全部生成完毕：

| Figure | 文件 | 大小 |
|--------|------|------|
| (a) Simpson's Paradox | `simpsons_paradox_pilot.pdf` | 32 KB |
| (b) Selectivity Heatmap | `selectivity_heatmap_pilot.pdf` | 31 KB |
| (c) Pareto Scatter | `pareto_scatter_pilot.pdf` | 23 KB |

**数据说明**：
- **Figure (a)**：使用 Qwen 数据（CKA from mvp001 + AUROC from pareto_detail.csv）。Llama 只有 CKA 无 AUROC 数据，未纳入。左面板拟合 pooled 线性回归（显示 slope），右面板按层分色各自拟合。
- **Figure (b)**：EN 列填充 selectivity 值（灰色标记 <0.05 的低信号层），小字标注 real AUROC。其余 5 语言列显示 "—" + 浅灰底色。
- **Figure (c)**：5 语言 Okabe-Ito 配色，Pareto 最优点（L24/L27）加标注，对角线参考线。

脚本位于 `/root/xling_calib_direction/scripts/plot_figures.py`，输出在 `artifacts/figures/`。

---
