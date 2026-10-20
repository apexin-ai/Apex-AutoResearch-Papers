# plot fig2 reliability diagram

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_plot_fig2_reliability_diagram_20260515T175823_result.json`
- **Structured JSON:** [`13c42d10fc17ffc5801e.json`](../../sessions/13/13c42d10fc17ffc5801e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已就位，图表质量良好：

- **PDF**: 24KB | **PNG**: 208KB
- 2×2 布局，Okabe-Ito 配色，ECE 标注，gap 柱（红色半透明），下方直方图 — 全部符合规格
- 数据来自服务器实际 calibration bin 数据

唯一差异：X 轴范围是 [0.5, 1.0] 而非 [0, 1]。因为所有 condition 的 confidence 值都 > 0.5，当前范围信息密度更高。需要改为 [0, 1] 吗？

---
