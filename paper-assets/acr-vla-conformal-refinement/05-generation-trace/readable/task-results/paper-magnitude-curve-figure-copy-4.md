# paper magnitude curve figure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_magnitude-curve-figure_20260516T144930_result.json`
- **Structured JSON:** [`2458e9575570b2f82717.json`](../../sessions/24/2458e9575570b2f82717.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已生成：

- **PDF**: `/root/acr-vla-conformal-refinement/figures/magnitude_curve_obs_vs_perdof.pdf` (33K)
- **PNG**: `/root/acr-vla-conformal-refinement/figures/magnitude_curve_obs_vs_perdof.png` (189K)

图表包含：
- obs_only CRM 蓝色实心圆线（倒 U 型），peak 22% at ε=0.2 带箭头标注
- perdof CRM 橙色三角线（单调递减），ε≥0.3 区域标注 "catastrophic collapse" + 橙色阴影
- 灰色虚线 baseline 12%，obs_only 与 baseline 之间浅蓝填充标注 "always ≥ baseline"
- 对数 X 轴，Okabe-Ito 色盲友好配色，无 top/right spines
- 绘图脚本保存在 `/root/acr-vla-conformal-refinement/figures/plot_magnitude_curve.py`

---
