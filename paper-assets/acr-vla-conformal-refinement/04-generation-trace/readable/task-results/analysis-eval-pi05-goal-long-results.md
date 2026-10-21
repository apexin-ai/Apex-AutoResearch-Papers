# analysis eval pi05 goal long results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-pi05-goal-long-results_20260522T155016_result.json`
- **Structured JSON:** [`5145d3303c6daa7a9bb8.json`](../../sessions/51/5145d3303c6daa7a9bb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验已完成，结果如下：

---

### Goal Suite (bjb1-32546)

```
exp_id: eval-pi05-vla-only-goal-seed43-r4
status: completed
success_rate: 97.0% (97/100)
per_task_rates:
  open_the_middle_drawer_of_the_cabinet:        100% (10/10)
  put_the_bowl_on_the_stove:                    100% (10/10)
  put_the_wine_bottle_on_top_of_the_cabinet:    100% (10/10)
  open_the_top_drawer_and_put_the_bowl_inside:   70% (7/10)  ← 最弱
  put_the_bowl_on_top_of_the_cabinet:           100% (10/10)
  push_the_plate_to_the_front_of_the_stove:     100% (10/10)
  put_the_cream_cheese_in_the_bowl:             100% (10/10)
  turn_on_the_stove:                            100% (10/10)
  put_the_bowl_on_the_plate:                    100% (10/10)
  put_the_wine_bottle_on_the_rack:              100% (10/10)
wandb_run_id: N/A
errors: none
```

```
exp_id: eval-pi05-vla-only-goal-seed44-r4
status: completed
success_rate: 97.0% (97/100)
per_task_rates:
  open_the_middle_drawer_of_the_cabinet:         80% (8/10)
  put_the_bowl_on_the_stove:                    100% (10/10)
  put_the_wine_bottle_on_top_of_the_cabinet:    100% (10/10)
  open_the_top_drawer_and_put_the_bowl_inside:   90% (9/10)
  put_the_bowl_on_top_of_the_cabinet:           100% (10/10)
  push_the_plate_to_the_front_of_the_stove:     100% (10/10)
  put_the_cream_cheese_in_the_bowl:             100% (10/10)
  turn_on_the_stove:                            100% (10/10)
  put_the_bowl_on_the_plate:                    100% (10/10)
  put_the_wine_bottle_on_the_rack:              100% (10/10)
wandb_run_id: N/A
errors: none
```

### Long Suite (bjb1-18228)

```
exp_id: eval-pi05-vla-only-long-seed43-r4
status: completed
success_rate: 96.0% (96/100)
per_task_rates:
  LIVING_ROOM_SCENE2_alphabet_soup_and_tomato_sauce_in_basket:  100% (10/10)
  LIVING_ROOM_SCENE2_cream_cheese_and_butter_in_basket:         100% (10/10)
  KITCHEN_SCENE3_turn_on_stove_and_moka_pot:                    100% (10/10)
  KITCHEN_SCENE4_black_bowl_in_bottom_drawer:                   100% (10/10)
  LIVING_ROOM_SCENE5_white_mug_left_plate_yellow_mug_right:      90% (9/10)
  STUDY_SCENE1_book_in_back_compartment:                        100% (10/10)
  LIVING_ROOM_SCENE6_white_mug_on_plate_chocolate_pudding:      100% (10/10)
  LIVING_ROOM_SCENE1_alphabet_soup_and_cream_cheese_in_basket:  100% (10/10)
  KITCHEN_SCENE8_both_moka_pots_on_stove:                        70% (7/10)  ← 最弱
  KITCHEN_SCENE6_yellow_mug_in_microwave:                       100% (10/10)
wandb_run_id: N/A
errors: none
```

```
exp_id: eval-pi05-vla-only-long-seed44-r4
status: completed
success_rate: 95.0% (95/100)
per_task_rates:
  LIVING_ROOM_SCENE2_alphabet_soup_and_tomato_sauce_in_basket:  100% (10/10)
  LIVING_ROOM_SCENE2_cream_cheese_and_butter_in_basket:         100% (10/10)
  KITCHEN_SCENE3_turn_on_stove_and_moka_pot:                    100% (10/10)
  KITCHEN_SCENE4_black_bowl_in_bottom_drawer:                   100% (10/10)
  LIVING_ROOM_SCENE5_white_mug_left_plate_yellow_mug_right:     100% (10/10)
  STUDY_SCENE1_book_in_back_compartment:                        100% (10/10)
  LIVING_ROOM_SCENE6_white_mug_on_plate_chocolate_pudding:      100% (10/10)
  LIVING_ROOM_SCENE1_alphabet_soup_and_cream_cheese_in_basket:   90% (9/10)
  KITCHEN_SCENE8_both_moka_pots_on_stove:                        60% (6/10)  ← 最弱
  KITCHEN_SCENE6_yellow_mug_in_microwave:                       100% (10/10)
wandb_run_id: N/A
errors: none
```

---

### 汇总（含已有 seed42）

| Benchmark | seed42 | seed43 | seed44 | Mean ± Std |
|-----------|--------|--------|--------|------------|
| **Goal**  | 98.0%  | 97.0%  | 97.0%  | **97.3% ± 0.6%** |
| **Long**  | 94.0%  | 96.0%  | 95.0%  | **95.0% ± 1.0%** |

难点 task 一致：Goal 的 `open_the_top_drawer_and_put_the_bowl_inside`（70-90%），Long 的 `KITCHEN_SCENE8_both_moka_pots_on_stove`（60-70%）。日志均无 W&B run ID。

---
