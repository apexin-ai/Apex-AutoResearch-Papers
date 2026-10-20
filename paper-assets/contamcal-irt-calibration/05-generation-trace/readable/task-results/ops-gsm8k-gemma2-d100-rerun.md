# ops gsm8k gemma2 d100 rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-gemma2-d100-rerun_20260520T062203_result.json`
- **Structured JSON:** [`91c795702a6c2fec1807.json`](../../sessions/91/91c795702a6c2fec1807.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:3 不空闲。** PID 293330 正在 cuda:3 上运行 gemma2 d100 eval（batch-size 8），已运行 15 分钟，占用 28660 MiB。output 目录为空（尚未产出结果）。

这就是之前 OOM 的同一配置（batch-size 8）的新实例。按 C001/C003，需要先 kill 这个进程才能提交新任务。

是否 kill PID 293330 然后用 batch-size 4 重跑？

---
