# ops submit d100 s42 eval cuda5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit-d100-s42-eval-cuda5_20260516T024458_result.json`
- **Structured JSON:** [`a535a9e9c1fc4cf0ef8b.json`](../../sessions/a5/a535a9e9c1fc4cf0ef8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:5 上仍有活跃进程：

- **PID 663067**: `compute_signals.py --adapter-path .../Qwen2.5-3B_d025_v3_s42/lora_adapter --benchmark mmlu --signal s4`
- 已运行 2h27m，占用 7796MiB

这个 d025_v3_s42 信号任务未被成功 kill。需要先终止它才能提交 eval batch。

是否 kill PID 663067？

---
