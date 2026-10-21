# analyze eval pi05 vla only long seed44 r4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-pi05-vla-only-long-seed44-r4_20260522T155102_result.json`
- **Structured JSON:** [`3f2a2eaac022cdee549e.json`](../../sessions/3f/3f2a2eaac022cdee549e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== RESULTS ===
exp_id: eval-pi05-vla-only-long-seed44-r4
overall_success_rate: 95.0%
per_task_results: {
  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: 100.0% (10/10),
  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: 100.0% (10/10),
  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: 100.0% (10/10),
  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: 100.0% (10/10),
  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: 100.0% (10/10),
  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy: 100.0% (10/10),
  LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate: 100.0% (10/10),
  LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket: 90.0% (9/10),
  KITCHEN_SCENE8_put_both_moka_pots_on_the_stove: 60.0% (6/10),
  KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it: 100.0% (10/10)
}
total_rollouts: 100
wandb_run_id: N/A (no W&B logging in log)
log_tail: (see above, full log captured — process exited with EXIT_CODE=0)
=== END ===
```

**对比 seed42-r4 (94.0%)**：seed44-r4 达到 95.0%，高 1 个百分点。8/10 task 满分，失败集中在 KITCHEN_SCENE8 (60%) 和 LIVING_ROOM_SCENE1 (90%)。

---
