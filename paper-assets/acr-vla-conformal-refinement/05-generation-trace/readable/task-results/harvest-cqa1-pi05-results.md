# harvest cqa1 pi05 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_cqa1-pi05-results_20260526T154442_result.json`
- **Structured JSON:** [`b9dc308977392a6da1bd.json`](../../sessions/b9/b9dc308977392a6da1bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Task 1: pi05-crm-k2-long-s44-cqa1 ✅ DONE
- **SR: 76.0% (152/200)**
- 日志干净，EXIT_CODE=0，无 OOM/CUDA error
- 异常项：KITCHEN_SCENE8_both_moka_pots 20% (4/20)；其余 9 任务 65–95%
- registry 已更新为 DONE，metrics/log_path/checkpoint_path 已设置

### Task 2: adaptive-long r3（**两个都在正常运行**）
| 实验 | PID | 状态 | GPU | 进度 |
|---|---|---|---|---|
| s43-cqa1-r3 | 350877 (alive, 4h48m) | RUNNING | cuda:4 11432 MiB, 70% | 6/10 任务完成，进行中：LIVING_ROOM_SCENE6 |
| s44-cqa1-r3 | 351443 (alive, 4h47m) | RUNNING | cuda:5 11432 MiB, 64% | 6/10 任务完成，进行中：LIVING_ROOM_SCENE6 |

无 OOM/error，日志持续输出。adaptive 模式 K=2 校正比 baseline 慢，预估剩余 ~2-3h（vs 估计的 1.7h，偏慢但不卡）。**无需 Agent 介入**。

### Task 3: pi05-adaptive-object-s43-cqa1-r3（**接近完成**）
- PID 364798 alive，4h14m elapsed
- cuda:2 10320 MiB, 49% util
- **9/10 任务完成**，最后一个任务（pick_up_the_orange_juice）已进行到 rollout 5/20
- 预估 <30 分钟内收尾。**无需 Agent 介入**。

三个运行中实验都健康，建议继续等待自然完成。

---
