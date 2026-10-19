# deploy bjb1 32546 batch6

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-batch6_20260517T112232_result.json`
- **Structured JSON:** [`b23f10342790d1d60929.json`](../../sessions/b2/b23f10342790d1d60929.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**前置检查结果：目标 GPU 全部被占用，无法部署。**

| 检查项 | 状态 |
|--------|------|
| 工作目录 `src/evaluate.py` | 存在 |
| obs_only checkpoint | 存在 |
| perdof checkpoint | 存在 |
| cuda:0 | **被占用** — PID 421086 (python, 5645MiB) |
| cuda:3 | **被占用** — PID 422357 (python, 5645MiB) |
| cuda:5 | **被占用** — PID 423767 (python, 5645MiB) |

实际上 bjb1-32546 的全部 6 张 4090 都有 python 进程在跑，没有空闲 GPU。需要等现有实验完成或手动终止后才能部署。

---
