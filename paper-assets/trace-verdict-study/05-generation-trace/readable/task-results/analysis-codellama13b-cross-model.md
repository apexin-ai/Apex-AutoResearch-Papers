# analysis codellama13b cross model

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_codellama13b_cross_model_20260516T192003_result.json`
- **Structured JSON:** [`cdc80875cc741b4c921e.json`](../../sessions/cd/cdc80875cc741b4c921e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 数字全部验证通过，分析完成。

核心结论：

**Scale monotonicity (no_trace)**：严格单调 — 1.5B (67.31%) < 6.7B (73.36%) < 7B (75.13%) < 13B (76.50%)，边际收益递减。

**Scale-invariance (exception_only)**：确认。所有模型 ≥99.33%，最小的 1.5B 和最大的 13B 同为 99.83%。说明 exception trace 提供的信号足以使任务变得 trivial，与模型容量无关。

**关键 takeaway**：Information > Scale。exception_only 相对 no_trace 的提升 (22-33 pp) 远大于同条件下最小到最大模型的差距 (9.19 pp)。

产出已注册为 `art_20260516_d1d1bd`。

---
