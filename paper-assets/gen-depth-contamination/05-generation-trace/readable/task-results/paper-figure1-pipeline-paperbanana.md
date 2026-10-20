# paper figure1 pipeline paperbanana

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure1_pipeline_paperbanana_20260522T030029_result.json`
- **Structured JSON:** [`49170932aced68ef049d.json`](../../sessions/49/49170932aced68ef049d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出文件：**
- PNG: `docs/paper/figures/pipeline.png` (90 KB, 300 DPI)
- PDF: `docs/paper/figures/pipeline.pdf` (37 KB, 矢量)
- 源码: `artifacts/figure1_pipeline/draw_pipeline.py`

**图内容：** 5 阶段水平 pipeline（蓝→橙→绿→紫→深灰），每阶段有内部细节（文档堆叠、深度链+自循环箭头、4 组特征行、K 个二分类器行、带阈值线的柱状图），底部有数学标注。

**PaperBanana 说明：** PaperBanana `generate` 用 Imagen 生成的图是通用插画风格，无法精确控制标注和布局，不适合这类需要精确数学符号的 pipeline 图。最终改用 matplotlib 手写，可控性更强。

**可能的改进方向：**
- 如果需要 Stage 2 的自循环箭头更醒目，可以加粗或换色
- 如果论文是单栏格式，可调整 `figsize` 宽度

---
