# ssh diagnose vla only object seed48

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-vla-only-object-seed48_20260520T001841_result.json`
- **Structured JSON:** [`8001da65f862a4d82d1d.json`](../../sessions/80/8001da65f862a4d82d1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。结果如下：

**Overall**: SR = **10.0%**（10/100 episodes）

**Per-task breakdown**（每 task 10 rollouts）:

| Task (pick & place to basket) | SR | Successes |
|---|---|---|
| bbq_sauce | 0.3 | 3/10 |
| salad_dressing | 0.2 | 2/10 |
| cream_cheese | 0.1 | 1/10 |
| butter | 0.1 | 1/10 |
| milk | 0.1 | 1/10 |
| chocolate_pudding | 0.1 | 1/10 |
| orange_juice | 0.1 | 1/10 |
| alphabet_soup | 0.0 | 0/10 |
| ketchup | 0.0 | 0/10 |
| tomato_sauce | 0.0 | 0/10 |

10 个 object 任务 × 10 rollouts = 100 episodes，seed=48，mode=vla_only（无 conformal refinement），benchmark=object。

---
