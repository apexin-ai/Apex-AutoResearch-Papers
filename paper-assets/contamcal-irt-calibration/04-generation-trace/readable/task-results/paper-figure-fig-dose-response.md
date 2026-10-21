# paper figure fig dose response

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_dose_response_20260515T190235_result.json`
- **Structured JSON:** [`2715609fd4bd38a899f2.json`](../../sessions/27/2715609fd4bd38a899f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完成。

**输出文件**：
- PDF: `figures/paper/fig_dose_response.pdf`
- PNG: `figures/paper/fig_dose_response.png`
- 脚本: `figures/paper/gen_fig_dose_response.py`
- Artifact: `art_20260515_5b4e88`

**数据来源**：exp-001 registry aligned accuracy (seed s123)，所有 4 个 dosage level (0%, 0.5%, 2.5%, 10%) × 2 scales (0.5B, 1.5B) × 3 benchmarks (ARC, GSM8K, MMLU)。数据与任务给出的参考值吻合。

**图表特征**：
- 1×3 subplot，Okabe-Ito 配色，evenly-spaced x 轴
- ARC panel 标注 "Forgetting (γ<0)"，GSM8K panel 标注 "Inflation (γ>0)"
- MMLU panel 0.5B 区域浅红底 + position bias 标注
- 3B 灰色虚线框 [PENDING-3B] 占位
- d000 baseline 水平虚线
- 300 DPI 矢量 PDF

---
