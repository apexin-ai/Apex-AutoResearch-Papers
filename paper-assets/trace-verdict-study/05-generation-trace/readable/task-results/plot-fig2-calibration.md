# plot fig2 calibration

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_plot_fig2_calibration_20260515T175927_result.json`
- **Structured JSON:** [`fb95e60eb734ebeaf57f.json`](../../sessions/fb/fb95e60eb734ebeaf57f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

fig2_calibration 已经存在且质量良好：

- **PDF**: 24KB, **PNG**: 208KB — 均 > 10KB
- 数据来源：服务器 calibration JSON 的实际 bin 数据（非模拟）
- 2×2 布局、GridSpec 上下分割、Okabe-Ito 配色、gap 柱、ECE 标注、直方图 — 全部符合要求

文件位置：
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/figures/paper/fig2_calibration.pdf`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/figures/paper/fig2_calibration.png`

生成脚本：`figures/paper/gen_fig2_calibration.py`

唯一差异：X 轴范围是 [0.5, 1.0]（非 [0, 1]），因为所有 confidence 值 > 0.5，当前范围更紧凑易读。需要改为 [0, 1] 吗？

---
