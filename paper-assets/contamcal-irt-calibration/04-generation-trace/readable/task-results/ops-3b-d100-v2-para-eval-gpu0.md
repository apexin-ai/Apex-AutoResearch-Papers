# ops 3B d100 v2 para eval gpu0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_3B-d100-v2-para-eval-gpu0_20260515T000028_result.json`
- **Structured JSON:** [`2426f350929dc97c6bf1.json`](../../sessions/24/2426f350929dc97c6bf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 上仍有进程运行：

- **PID 461879**: `evaluate.py` — 3B d100 v2 **aligned** eval（mmlu gsm8k arc_challenge），output-dir 为 `Qwen2.5-3B_d100_v2_s42_aligned`，启动于 07:32:36

这是之前的 aligned eval 的残留进程（只跑了 mmlu/gsm8k/arc_challenge，没有 humaneval）。GPU 0 未空出，不能提交新任务。

需要确认：这个进程是否还在正常运行还是已经完成但未退出？是否需要 kill 它后再提交 paraphrased eval？

---
