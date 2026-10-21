# analyze eval obs only object norm005 seed48

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-object-norm005-seed48_20260519T185436_result.json`
- **Structured JSON:** [`04ed39ddcf28044f5c64.json`](../../sessions/04/04ed39ddcf28044f5c64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验数据全部拿到，汇总如下：

---

```
exp_id: eval-obs-only-object-norm005-seed48
status: success (EXIT_CODE=0)
overall_success_rate: 17.0% (17/100)
per_task_rates:
  alphabet_soup:        0%  (0/10)
  cream_cheese:        10%  (1/10)
  salad_dressing:      30%  (3/10)
  bbq_sauce:           30%  (3/10)
  ketchup:              0%  (0/10)
  tomato_sauce:        10%  (1/10)
  butter:              10%  (1/10)
  milk:                20%  (2/10)
  chocolate_pudding:   30%  (3/10)
  orange_juice:        30%  (3/10)
total_time: ~12.9h
notes: 无异常
```

```
exp_id: eval-perdof-object-norm003-seed47
status: success (EXIT_CODE=0)
overall_success_rate: 15.0% (15/100)
per_task_rates:
  alphabet_soup:        0%  (0/10)
  cream_cheese:         0%  (0/10)
  salad_dressing:      20%  (2/10)
  bbq_sauce:           30%  (3/10)
  ketchup:              0%  (0/10)
  tomato_sauce:        10%  (1/10)
  butter:              20%  (2/10)
  milk:                10%  (1/10)
  chocolate_pudding:   30%  (3/10)
  orange_juice:        30%  (3/10)
total_time: ~12.8h
notes: 无异常
```

```
exp_id: eval-obs-only-spatial-norm02-seed46-r2
status: success (EXIT_CODE=0)
overall_success_rate: 33.0% (33/100)
per_task_rates:
  bowl_between_plate_and_ramekin:   90%  (9/10)
  bowl_next_to_ramekin:            100%  (10/10)
  bowl_from_table_center:            0%  (0/10)
  bowl_on_cookie_box:               30%  (3/10)
  bowl_in_top_drawer:               10%  (1/10)
  bowl_on_ramekin:                   0%  (0/10)
  bowl_next_to_cookie_box:          80%  (8/10)
  bowl_on_stove:                     0%  (0/10)
  bowl_next_to_plate:               20%  (2/10)
  bowl_on_wooden_cabinet:            0%  (0/10)
total_time: ~1.7h
notes: 无异常。r2 重跑，耗时短于 Object 实验（Spatial 环境轻量）
```

---

**要点对比：**
- obs_only (ε=0.05) on Object: **17.0%**
- perdof (ε=0.03) on Object: **15.0%** — 略低于 obs_only，两者差距不大
- obs_only (ε=0.2) on Spatial: **33.0%** — Spatial 整体更高，但任务间方差极大（0%~100%）

---
