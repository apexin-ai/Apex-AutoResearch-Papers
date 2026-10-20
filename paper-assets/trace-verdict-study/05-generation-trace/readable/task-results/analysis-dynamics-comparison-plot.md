# analysis dynamics comparison plot

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dynamics_comparison_plot_20260519T064242_result.json`
- **Structured JSON:** [`2d1ebb5eb0e438a33b58.json`](../../sessions/2d/2d1ebb5eb0e438a33b58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册。

**输出文件（westd-11235）：**
- PDF: `/root/trace-verdict-study/docs/paper/figures/training_dynamics.pdf` (27KB)
- PNG: `/root/trace-verdict-study/docs/paper/figures/training_dynamics.png` (141KB)

**图表内容：**
- 蓝色实线 (Exception-Only): step 50 即达 99.33%，step 200 饱和至 99.83%，之后完全平稳
- 红色虚线 (Full Trace): 在 82%~88% 区间持续震荡，best 88.82% (step 350)
- 两个关键点已用箭头标注
- Y 轴 80~100%，网格线，学术风格

**Artifact ID:** `art_20260519_b542ac`

---
