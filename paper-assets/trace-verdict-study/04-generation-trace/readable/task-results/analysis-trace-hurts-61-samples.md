# analysis trace hurts 61 samples

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_trace_hurts_61_samples_20260520T162228_result.json`
- **Structured JSON:** [`7ca5ff87ea597728be11.json`](../../sessions/7c/7ca5ff87ea597728be11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论比预期更强：**61 个 trace-hurts 样本 100% 由 truncation 驱动**，不是"主要"而是"完全"。

核心证据：
- 61/61 的 full_trace 输入都饱和在 2015–2016 tokens（数据格式化时 trace 尾部被截断）
- 70 个短样本（trace 完整保留）准确率 100%，zero trace-hurts
- 77% 是 FP（右截断丢失了 trace 尾部的 failure 信号，模型默认预测 pass）
- no_trace 版本仅 77–401 tokens，不受截断影响

报告已写入 `artifacts/trace_hurts_analysis.md`。

---
