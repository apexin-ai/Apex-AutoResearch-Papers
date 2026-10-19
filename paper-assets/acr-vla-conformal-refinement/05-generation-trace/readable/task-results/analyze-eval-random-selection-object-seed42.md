# analyze eval random selection object seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-random-selection-object-seed42_20260520T084945_result.json`
- **Structured JSON:** [`b5dc1e6884d3df7fd873.json`](../../sessions/b5/b5dc1e6884d3df7fd873.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 结果文件已成功读取，无 stdout 日志，无 W&B。

## 结果汇总：`eval_object_random_selection_seed42`

| 指标 | 值 |
|------|-----|
| **Overall SR** | **0.11** |
| n_tasks | 10 |
| n_rollouts per task | 10 |
| mode | random_selection (single) |
| benchmark | object |

### Per-task SR

| Task | SR | Successes/Total |
|------|----|-----------------|
| alphabet_soup | 0.0 | 0/10 |
| cream_cheese | 0.1 | 1/10 |
| salad_dressing | 0.1 | 1/10 |
| bbq_sauce | 0.1 | 1/10 |
| ketchup | 0.0 | 0/10 |
| tomato_sauce | 0.1 | 1/10 |
| butter | 0.1 | 1/10 |
| milk | 0.1 | 1/10 |
| chocolate_pudding | 0.2 | 2/10 |
| orange_juice | 0.3 | 3/10 |

**Overall SR = 0.11**，符合预期范围 (0.09–0.13)。2 个 task 全部失败（alphabet_soup, ketchup），orange_juice 最高 0.3，其余在 0.1–0.2。无异常，进程正常完成。

另外注意 logs 目录下还有 seed43/44/45 的 random_selection 结果文件，以及 k5 版本 (seed43)，如需汇总多 seed 可以一起读。

---
