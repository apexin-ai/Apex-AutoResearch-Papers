# analyze eval vla only spatial seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-vla-only-spatial-seed42_20260519T143753_result.json`
- **Structured JSON:** [`2019c70dbc5350951c71.json`](../../sessions/20/2019c70dbc5350951c71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_id: eval-vla-only-spatial-seed42
conclusion: success
success_rate: 30%
per_task:
  between_plate_and_ramekin: 60%
  next_to_ramekin: 100%
  from_table_center: 0%
  on_cookie_box: 20%
  in_top_drawer: 0%
  on_ramekin: 0%
  next_to_cookie_box: 90%
  on_stove: 0%
  next_to_plate: 30%
  on_wooden_cabinet: 0%
对标: obs_only spatial K=10 seed42 = 35%
改进幅度: -5pp（VLA-only 30% < obs_only 35%）
```

符合预期：VLA-only baseline（30%）低于 obs_only + CRM（35%），说明 CRM 在 Spatial benchmark 上提供了 +5pp 的改进。任务方差很大——`next_to_ramekin` 和 `next_to_cookie_box` 接近满分，而 5 个任务完全失败（0%），说明 VLA 在需要精确空间定位的任务上存在系统性缺陷。

---
