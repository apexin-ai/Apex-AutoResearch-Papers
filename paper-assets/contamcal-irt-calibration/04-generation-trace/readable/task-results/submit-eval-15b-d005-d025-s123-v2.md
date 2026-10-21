# submit eval 15B d005 d025 s123 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval-15B-d005-d025-s123-v2_20260515T135019_result.json`
- **Structured JSON:** [`e147fbc1a6c7c318f1c3.json`](../../sessions/e1/e147fbc1a6c7c318f1c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这两个 eval 实验**已经在运行中**，已经跑了约 9 分钟：

- **PID 566224** (cuda:0): `evaluate.py` — 1.5B d005 s123 aligned eval，运行 8m52s
- **PID 566311** (cuda:1): `evaluate.py` — 1.5B d025 s123 aligned eval，运行 8m48s

命令参数与本次要提交的完全一致（相同 adapter-path、output-dir、benchmarks）。看起来已经有人（或 hook）重新提交了这两个任务。

**不需要重新提交。** 按 C001 约束，目标 GPU 上已有同类进程，不应重复提交。

需要确认的是这两个进程是否已在 registry 中注册。要我检查 registry 状态并补登记吗？

---
