# paper figure fig metric trajectory

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_metric_trajectory_20260515T175029_result.json`
- **Structured JSON:** [`39c18819ca453d678152.json`](../../sessions/39/39c18819ca453d678152.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Fig 4 已生成并注册。

**输出文件**:
- PDF: `figures/paper/fig_metric_trajectory.pdf` (19 KB, 矢量)
- PNG: `figures/paper/fig_metric_trajectory.png` (105 KB)

**数据验证** (4-seed mean, 与参考值一致):
- token_entropy: gen0=3.234 → gen10≈1.27, drift **-61%**
- distinct_1: gen0≈0.098 → gen10≈0.071, drift **-28%**

**可视化要素**:
- 蓝色 token_entropy 在 gen 1 即骤降至 ~0.59，橙色 distinct_1 在 gen 1 仍 ~1.0，gen 2 才开始下降 → "1-gen lead" 标注清晰
- 4-seed mean ± std 半透明区间（方差极小，说明现象跨 seed 稳定）
- 右侧标注最终 drift 百分比
- 3.25in × 2.5in single-column，serif 字体，Okabe-Ito 配色，300 DPI

---
