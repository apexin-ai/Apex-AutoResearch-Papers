# paper figure fig scoring crossover heatmap

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_scoring_crossover_heatmap_20260525T181019_result.json`
- **Structured JSON:** [`819c0b99acd9169003d8.json`](../../sessions/81/819c0b99acd9169003d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。经过 5 轮迭代，生成了 3 个文件：

- **PDF** (28KB): `fig_scoring_crossover.pdf` — 矢量格式，LaTeX 嵌入用
- **PNG** (175KB): `fig_scoring_crossover.png` — 300 DPI 预览
- **脚本**: `gen_fig_scoring_crossover.py` — 可复现

图表特性：
- 2×2 crossover heatmap，对角线颜色反转清晰传达 "strategy reversal"
- 每个 cell 三层信息：Δpp（大号加粗）、代表模型+条件（中号）、range（小号斜体）
- 绿/红 diverging 色系，power-curve 映射确保 ±28~30 pp 的 cell 也有足够饱和度
- 圆角矩形、白底、无网格线、无默认样式

---
