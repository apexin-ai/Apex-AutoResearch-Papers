# analyze eval random selection spatial seed42 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-random-selection-spatial-seed42-r2_20260520T144617_result.json`
- **Structured JSON:** [`1d0c80309a94c8c4ac32.json`](../../sessions/1d/1d0c80309a94c8c4ac32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
overall_success_rate: 0.34 (34%)
n_tasks: 10
n_rollouts: 10
total_rollouts: 100
per_task_sr:
  between_plate_and_ramekin:  70% (7/10)
  next_to_ramekin:            90% (9/10)
  from_table_center:          10% (1/10)
  on_cookie_box:              30% (3/10)
  in_top_drawer_cabinet:       0% (0/10)
  on_ramekin:                  0% (0/10)
  next_to_cookie_box:        100% (10/10)
  on_stove:                    0% (0/10)
  next_to_plate:              40% (4/10)
  on_wooden_cabinet:           0% (0/10)
errors: none (EXIT_CODE=0, 仅有 robosuite 宏文件和 torch_dtype deprecation 警告，无实质错误)
```

34% SR，与 seed43 (26%) / seed44 (28%) 同范围，偏高但合理。任务间方差大：简单空间关系（next_to_cookie_box 100%、next_to_ramekin 90%）表现好，复杂空间关系（on_stove、on_ramekin、in_drawer、on_cabinet）全部 0%。

---
