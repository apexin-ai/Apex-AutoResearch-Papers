# diagnose multiscale seed44 r2 exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_multiscale-seed44-r2-exit_20260517T205440_result.json`
- **Structured JSON:** [`e97bb5c13e3c93995ff8.json`](../../sessions/e9/e97bb5c13e3c93995ff8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron already removed (not in session store).

## 结果汇报

**eval-k1-crm-multiscale-object-seed44-r2** 已完成，conclusion = **negative**。

### Overall SR: **10.0%** (10/100)

### Per-task breakdown (seed44):

| Task | SR | Successes |
|---|---|---|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 0% | 0/10 |
| salad_dressing | 20% | 2/10 |
| bbq_sauce | 10% | 1/10 |
| ketchup | 0% | 0/10 |
| tomato_sauce | 10% | 1/10 |
| butter | 0% | 0/10 |
| milk | 0% | 0/10 |
| chocolate_pudding | **40%** | 4/10 |
| orange_juice | 20% | 2/10 |

### GPU 状态 (bjb1-18228):

| GPU | Memory Used | Utilization |
|---|---|---|
| cuda:0 | 4735/24564 MiB | 22% (occupied) |
| cuda:1 | 4/24564 MiB | **free** |
| cuda:2 | 5664/24564 MiB | 20% (occupied) |
| cuda:3 | 4/24564 MiB | **free** |

cuda:3 已释放。cuda:1 和 cuda:3 均可用。

Registry 已更新为 DONE/negative，metrics 已写入。

---
