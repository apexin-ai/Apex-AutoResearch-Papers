# paper figure fig2 magnitude

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig2_magnitude_20260518T085810_result.json`
- **Structured JSON:** [`81a03a8005bfa360d2a7.json`](../../sessions/81/81a03a8005bfa360d2a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册。

**输出文件**:
- PDF: `artifacts/figures/paper/fig2_magnitude.pdf` (44 KB, 矢量)
- PNG: `artifacts/figures/paper/fig2_magnitude.png` (167 KB, 300 DPI)

**实现的 Patterns**:
- **A**: 粉色 collapse zone band (y < 2%)
- **C**: VLA-only baseline 灰色虚线 (11.2%)
- **D**: n<3 的点用空心 marker + italic "n=X" 标注
- **E**: n≥2 时显示 std error bars
- **J**: 所有文字标签带白色描边防遮挡

**设计选择**: 用 categorical 均匀间距 x 轴（而非对数刻度），6 个 ε 值等距排列，最后一个标为 "uncapped (1.42)"。perdof uncapped 的 0% 点叠加 × marker 并加粗标注 "0.0% (n=3)"。曲线标签直接标在线旁，无 legend 框。

---
