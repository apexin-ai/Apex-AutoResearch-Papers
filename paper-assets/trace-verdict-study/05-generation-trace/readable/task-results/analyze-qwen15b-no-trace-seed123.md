# analyze qwen15b no trace seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen15b_no_trace_seed123_20260520T215406_result.json`
- **Structured JSON:** [`72e6ae0ba65e8b002181.json`](../../sessions/72/72e6ae0ba65e8b002181.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `qwen15b_no_trace_seed123` 分析完成，registry 已更新为 DONE/success。

**结果汇总：**

| 指标 | seed123 | seed42 |
|------|---------|--------|
| Accuracy | **75.88%** [73.3%, 78.2%] | 67.31% |
| pass F1 | 0.832 | — |
| fail F1 | 0.571 | — |
| Lift over majority | +4.4pp | — |

**注意：** seed123 (75.88%) 比 seed42 (67.31%) 高 8.6pp，两个 seed 之间方差较大。这可能值得关注——如果后续做 cross-seed 分析，两者 CI 可能不完全重叠。

---
