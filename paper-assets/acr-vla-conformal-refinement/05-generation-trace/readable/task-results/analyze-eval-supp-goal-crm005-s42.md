# analyze eval supp goal crm005 s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-goal-crm005-s42_20260523T062604_result.json`
- **Structured JSON:** [`085af7965cd2ef1c4560.json`](../../sessions/08/085af7965cd2ef1c4560.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志中无 wandb，无 error/warning（仅有一个无害的 `DeprecationWarning: builtin type swigvarlink`）。JSON 输出与日志一致。

## 实验结果：eval-supp-goal-crm005-s42

```
overall_sr: 85.5% (171/200)
n_tasks: 10
n_rollouts: 200 (20 per task)
wandb_run_id: 无（未集成 wandb）

per_task_sr:
  put_the_bowl_on_the_stove:                100.0% (20/20)
  put_the_wine_bottle_on_top_of_the_cabinet: 95.0% (19/20)
  put_the_bowl_on_top_of_the_cabinet:        95.0% (19/20)
  push_the_plate_to_the_front_of_the_stove:  95.0% (19/20)
  turn_on_the_stove:                         95.0% (19/20)
  put_the_bowl_on_the_plate:                 95.0% (19/20)
  open_the_middle_drawer_of_the_cabinet:     85.0% (17/20)
  put_the_wine_bottle_on_the_rack:           75.0% (15/20)
  open_the_top_drawer_and_put_the_bowl_inside: 70.0% (14/20)
  put_the_cream_cheese_in_the_bowl:          50.0% (10/20)
```

**注意**：第二个日志 `goal_crm005_s42.log` 是同配置的另一次运行，数值略有不同（如 `put_the_bowl_on_the_stove` 95% vs 100%），tail -200 未截取到完整结果。以 `eval-supp-goal-crm005-s42.log` 为准。

**对比参考**：
- Spatial CRM norm=0.05 seed42: 80.0% → Goal CRM norm=0.05 seed42: **85.5%**
- Goal suite 的 CRM 表现优于 Spatial，6/10 tasks 达 95%+，仅 `put_the_cream_cheese_in_the_bowl` 明显偏低（50%）。

---
