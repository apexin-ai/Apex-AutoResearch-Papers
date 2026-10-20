# analysis calibration reliability diagram

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_calibration_reliability_diagram_20260517T004711_result.json`
- **Structured JSON:** [`e93dd9d1f88938f2b1e1.json`](../../sessions/e9/e93dd9d1f88938f2b1e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已完成，输出在 `/root/trace-verdict-study/docs/paper/figures/calibration_reliability.pdf`。

**关键发现：**
- Exception Only：99.3% 样本 confidence > 0.95 且 accuracy = 1.0，几乎完美校准（ECE = 0.0027）
- No Trace：confidence 分散，各 bin accuracy 系统性低于 predicted confidence，典型 overconfidence 模式（ECE = 0.1715）

图中两条件对比非常直观，适合直接放入论文。

---
