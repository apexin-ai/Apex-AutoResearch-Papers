# ops collect spatial bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-spatial-bjb1-18228_20260515T043840_result.json`
- **Structured JSON:** [`adb2d630f9e01c2f9e5a.json`](../../sessions/ad/adb2d630f9e01c2f9e5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 experiments are **still running**. Registry updated. Current status:

```
exp_id: eval-argmin-only-spatial (reconvla, PID 231421, elapsed 10h51m)
Status: RUNNING
Tasks: 9/10
Per-task:
  T0 between_plate_ramekin:  60% (6/10)
  T1 next_to_ramekin:       100% (10/10)
  T2 from_table_center:       0% (0/10)
  T3 on_cookie_box:           30% (3/10)
  T4 in_top_drawer:           10% (1/10)
  T5 on_ramekin:              10% (1/10)
  T6 next_to_cookie_box:      90% (9/10)
  T7 on_stove:                 0% (0/10)
  T8 next_to_plate:           30% (3/10)
  T9 ???:                     running...
Running total: 33/90 = 36.7%

exp_id: eval-acr-spatial-v4-small (acr_vla perdof, norm=0.1, PID 253085, elapsed 8h09m)
Status: RUNNING
Tasks: 7/10
Per-task:
  T0 between_plate_ramekin:  60% (6/10)
  T1 next_to_ramekin:       100% (10/10)
  T2 from_table_center:      10% (1/10)
  T3 on_cookie_box:           40% (4/10)
  T4 in_top_drawer:            0% (0/10)
  T5 on_ramekin:               0% (0/10)
  T6 next_to_cookie_box:      90% (9/10)
  T7-T9:                     running...
Running total: 30/70 = 42.9%

exp_id: eval-acr-spatial-v4-obs-only-r2 (crm_obs_only, norm=0.1, PID 270097, elapsed 6h18m)
Status: RUNNING
Tasks: 6/10
Per-task:
  T0 between_plate_ramekin:  90% (9/10)
  T1 next_to_ramekin:       100% (10/10)
  T2 from_table_center:       0% (0/10)
  T3 on_cookie_box:           40% (4/10)
  T4 in_top_drawer:           10% (1/10)
  T5 on_ramekin:               0% (0/10)
  T6-T9:                     running...
Running total: 24/60 = 40.0%

exp_id: eval-acr-spatial-v4-scalar (crm_scalar, norm=0.1, PID 288939, elapsed 3h04m)
Status: RUNNING
Tasks: 3/10
Per-task:
  T0 between_plate_ramekin:  60% (6/10)
  T1 next_to_ramekin:       100% (10/10)
  T2 from_table_center:      10% (1/10)
  T3-T9:                     running...
Running total: 17/30 = 56.7%
```

**初步趋势**（基于已完成任务）：
- **argmin (reconvla)**: ~36.7%，比之前报告的 37.5% 略低，几乎持平
- **v4-small (perdof)**: ~42.9%，与之前 42.0% 一致
- **obs-only-r2**: ~40.0%，比之前 48.0% 下降（之前 5 task 数据偏高）
- **scalar**: ~56.7%，之前 80% 是只有 2 task 时的值，随着更多 task 加入在回落

预计 argmin 最快完成（仅剩 1 task，~1h），scalar 最晚（还要 ~7-8h）。

---
