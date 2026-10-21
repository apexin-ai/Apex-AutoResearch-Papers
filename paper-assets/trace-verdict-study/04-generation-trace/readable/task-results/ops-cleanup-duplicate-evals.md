# ops cleanup duplicate evals

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_duplicate_evals_20260516T022017_result.json`
- **Structured JSON:** [`0f72490b4a6c045d63b4.json`](../../sessions/0f/0f72490b4a6c045d63b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**已 kill：**
- PID 229047 + 229042（较早的 full_trace_v3 eval 及其 bash 父进程）

**保留：**
- PID 229422（较新的 full_trace_v3 eval，cuda:0，正常运行中，GPU 利用率 83%）
- PID 228241（deepseek_vota eval）已不在进程列表中，应该是已经自行完成了

---
