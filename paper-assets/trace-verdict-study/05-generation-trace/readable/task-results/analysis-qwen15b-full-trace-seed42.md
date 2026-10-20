# analysis qwen15b full trace seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_full_trace_seed42_20260516T120137_result.json`
- **Structured JSON:** [`a14a0378b869d7a4847b.json`](../../sessions/a1/a14a0378b869d7a4847b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Qwen-1.5B full_trace_seed42**: 77.06% accuracy (CI: [74.8%, 79.6%])，lift +5.5pp over majority baseline。

关键对比：
- **vs 同模型精简格式**：exception_only (99.83%) 和 VOTA (99.58%) 远超 full_trace (77.06%)，差距 22-23pp
- **vs 7B full_trace**：比 DeepSeek-7B v5 (81.76%) 低 4.7pp，差距主要在 fail_recall (0.53 vs 0.70)
- **vs no_trace**：比 no_trace (67.31%) 高 9.75pp，full_trace 确实有帮助但效率极低

核心结论：trace 格式选择的影响远大于模型规模。1.5B 模型用 exception_only 可达 99.8%，用 full_trace 仅 77.1%——完整 trace 的信息冗余对小模型是负担。

---
