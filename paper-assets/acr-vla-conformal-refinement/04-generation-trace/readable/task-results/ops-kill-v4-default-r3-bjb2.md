# ops kill v4 default r3 bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-v4-default-r3-bjb2_20260515T044255_result.json`
- **Structured JSON:** [`95df7f848d6a3b96783f.json`](../../sessions/95/95df7f848d6a3b96783f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：bjb2-40593 上没有 v4-default-r3 相关进程。**

当前状态：
- **唯一 GPU 进程**：PID 211962 — `reconvla-object` 实验（`evaluate.py --benchmark object --mode reconvla --K 10 --n_rollouts 20`），占用 5573MiB，正在运行中 → **已保留**
- **tmux session**：`eval-reconvla-object`（PID 211951）— 就是上面这个实验的 session
- **v4-default-r3 进程**：不存在，已经没有了。无需 kill 任何东西。

GPU 使用 5592MiB / 24564MiB，利用率 12%，全部是 reconvla-object 实验在用。

---
