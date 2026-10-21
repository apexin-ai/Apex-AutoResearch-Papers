# analysis seed44 harvest pertask

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed44-harvest-pertask_20260516T152421_result.json`
- **Structured JSON:** [`7ab8b1c2d7690b032651.json`](../../sessions/7a/7ab8b1c2d7690b032651.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

argmin 仍在 orange_juice rollout 5/10，还需几分钟。

## 结果汇总

### seed44 obs_only ε=0.2 per-task (已完成，overall=16%)

| Task | SR | Successes |
|------|-----|-----------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 10% | 1/10 |
| salad_dressing | 20% | 2/10 |
| bbq_sauce | 20% | 2/10 |
| ketchup | 10% | 1/10 |
| tomato_sauce | 10% | 1/10 |
| butter | 20% | 2/10 |
| milk | 10% | 1/10 |
| chocolate_pudding | 30% | 3/10 |
| orange_juice | 30% | 3/10 |

### seed44 argmin (仍在运行，9/10 tasks done)

已完成 task 的部分结果：

| Task | SR | Successes |
|------|-----|-----------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 0% | 0/10 |
| salad_dressing | 10% | 1/10 |
| bbq_sauce | 20% | 2/10 |
| ketchup | 10% | 1/10 |
| tomato_sauce | 10% | 1/10 |
| butter | 0% | 0/10 |
| milk | 10% | 1/10 |
| chocolate_pudding | **50%** | 5/10 |
| orange_juice | *running* (1/5 at rollout 5) | - |

前 9 个 task: 11/90 = 12.2%。预计 overall 在 11-15% 左右。

**已完成：** obs_only artifact 已注册 (art_20260516_513b56)，registry metrics 已更新含 per_task_sr。argmin 预计几分钟内结束，结束后需要再次读取结果并注册。

---
