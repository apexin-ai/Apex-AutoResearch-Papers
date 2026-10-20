# submit exp 002 signals 3B v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_002_signals_3B_v2_20260515T160645_result.json`
- **Structured JSON:** [`b6d6d505fc5eb95dc10b.json`](../../sessions/b6/b6d6d505fc5eb95dc10b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 4 不空闲，无法提交。**

当前 GPU 4 状态：
- PID 584233：`exp001/evaluate.py`（Qwen2.5-3B_d005_s123 评估），已运行 33 分钟
- 显存占用 13047 / 24564 MiB，利用率 70%

按 C002 约束，目标 GPU 必须空闲才能提交。需要等 exp001 评估完成，或改用其他空闲 GPU（当前 6 张卡全部在跑任务）。

---
