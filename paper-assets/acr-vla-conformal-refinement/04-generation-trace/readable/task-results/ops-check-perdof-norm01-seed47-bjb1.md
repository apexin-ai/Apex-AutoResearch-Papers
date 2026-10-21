# ops check perdof norm01 seed47 bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-perdof-norm01-seed47-bjb1_20260517T225932_result.json`
- **Structured JSON:** [`19215537cad81d8c3aa3.json`](../../sessions/19/19215537cad81d8c3aa3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，结果如下：

**Overall SR: 14.0% (14/100)** — 10 tasks x 10 rollouts，全部完成。

Per-task breakdown:

| Task | SR | Successes |
|---|---|---|
| chocolate_pudding | 40% | 4/10 |
| salad_dressing | 30% | 3/10 |
| bbq_sauce | 30% | 3/10 |
| orange_juice | 20% | 2/10 |
| butter | 10% | 1/10 |
| milk | 10% | 1/10 |
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 0% | 0/10 |
| ketchup | 0% | 0/10 |
| tomato_sauce | 0% | 0/10 |

**结论: success**（实验正常完成，结果为 negative — perdof norm=0.1 seed47 的 SR 仅 14%）

- 模式: `crm_perdof`, baseline_mode: `single`, benchmark: `object`
- 日志路径: `/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json`
- 进程已退出，无残留进程

---
