# ops mass deploy bjb1 32546 6gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mass-deploy-bjb1-32546-6gpu_20260518T022749_result.json`
- **Structured JSON:** [`2747dfef4772734d7bfb.json`](../../sessions/27/2747dfef4772734d7bfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 6 块 GPU 都在使用中。** 每块 GPU 都有 python 进程运行：

| GPU | 显存占用 | GPU利用率 | 进程 |
|-----|---------|-----------|------|
| 0 | 5201MiB / 24564MiB | 22% | python (PID 565173) |
| 1 | 4737MiB / 24564MiB | 21% | python (PID 549432) |
| 2 | 4736MiB / 24564MiB | 23% | python (PID 553052) |
| 3 | 5201MiB / 24564MiB | 21% | python (PID 562396) |
| 4 | 9466MiB / 24564MiB | 99% | 2个python进程 (PID 535595, 557072) |
| 5 | 5665MiB / 24564MiB | 22% | python (PID 571010) |

**无法部署任何实验——cuda:0 到 cuda:5 全部被占用。**

需要确认这些进程是否是你之前的实验（可以查 tmux sessions），如果是已完成的可以清理后重新部署。要我检查这些进程的具体信息吗？

---
