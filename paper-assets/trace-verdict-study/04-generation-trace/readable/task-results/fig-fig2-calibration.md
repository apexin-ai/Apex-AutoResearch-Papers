# fig fig2 calibration

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fig_fig2_calibration_20260515T175615_result.json`
- **Structured JSON:** [`04652aaa3cda792add0f.json`](../../sessions/04/04652aaa3cda792add0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

fig2_calibration 已生成并拉回本地，之前的 worker 已完成了全部工作。

文件验证：
- **PDF**: 24.5 KB (`fig2_calibration.pdf`)
- **PNG**: 208 KB (`fig2_calibration.png`)

图表包含 2×2 布局：
- **(a) No Trace** — ECE = 0.172，明显 overconfidence（红色 gap 大）
- **(b) Full Trace** — ECE = 0.095，校准改善但仍有偏差
- **(c) Exception Only** — ECE = 0.002，近乎完美校准，样本集中在高 confidence
- **(d) VOTA** — ECE = 0.005，类似 exception_only，高度集中

每个 panel 都有 reliability curve（上）和 confidence 分布直方图（下），符合规格。

---
