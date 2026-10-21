# check cqa1 32758 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1-32758-status_20260526T082137_result.json`
- **Structured JSON:** [`510ca96188bd0dcb6663.json`](../../sessions/51/510ca96188bd0dcb6663.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== SERVER: cqa1-32758 (6×4090D) — All 6 RUNNING ===

[RUNNING] pi05-crm-k2-long-s44-cqa1
  GPU 0: 63% util, 14.0/24 GB | elapsed 1h29m | PID 216649
  progress: long task "cream_cheese_box_and_butter" rollout 15/20 (~3rd task of 10)

[RUNNING] pi05-adaptive-object-s42-cqa1
  GPU 1: 21% util, 12.6/24 GB | elapsed 1h26m | PID 219043
  progress: object task "salad_dressing" just done 90%, after cream_cheese 70%

[RUNNING] pi05-adaptive-goal-s42-cqa1
  GPU 2: 18% util, 12.6/24 GB | elapsed 1h25m | PID 219679
  progress: goal task "open_the_top_drawer" rollout 5/20; prior: bowl_on_stove 95%, wine_bottle_on_cabinet 85%

[RUNNING] pi05-adaptive-object-s44-cqa1
  GPU 3: 23% util, 11.7/24 GB | elapsed 2h28m | PID 197917
  progress: object task "tomato_sauce" rollout 5/20; prior: bbq_sauce 95%, ketchup 60%

[RUNNING] pi05-adaptive-long-s43-cqa1
  GPU 4: 22% util, 13.1/24 GB | elapsed 2h27m | PID 198442
  progress: long task "KITCHEN_SCENE4_black_bowl_bottom_drawer" rollout 5/20; prior: cream_cheese_box+butter 100%, stove+moka_pot 95%

[RUNNING] pi05-adaptive-long-s44-cqa1
  GPU 5: 23% util, 13.1/24 GB | elapsed 2h26m | PID 199049
  progress: long task "stove+moka_pot" finished 100%, about to advance; prior: cream_cheese_box+butter 100%

=== Summary ===
- 0 completed (no JSON outputs for these 6 IDs yet)
- 6 running, all healthy (GPU util 18–63%, memory 12–14 GB, well within 24 GB)
- ETA: object/goal ~2-3h more; long ~4-6h more (max_steps=300, ~3rd task of 10)
- No errors observed in any log tail
```

---
