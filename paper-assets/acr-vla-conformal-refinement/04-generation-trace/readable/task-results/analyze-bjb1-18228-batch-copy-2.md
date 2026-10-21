# analyze bjb1 18228 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_bjb1-18228-batch_20260519T231924_result.json`
- **Structured JSON:** [`cdb48d4f994dd2bb58ff.json`](../../sessions/cd/cdb48d4f994dd2bb58ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验均无 W&B 记录。以下是完整结果：

---

### 实验 1
```
exp_id: eval-vla-only-long-seed48
status: success (EXIT_CODE=0)
overall_success_rate: 0.14
per_task:
  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: 0.0 (0/10)
  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: 0.0 (0/10)
  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: 0.8 (8/10)
  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: 0.0 (0/10)
  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: 0.3 (3/10)
  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy: 0.1 (1/10)
  LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate: 0.1 (1/10)
  LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket: 0.0 (0/10)
  KITCHEN_SCENE8_put_both_moka_pots_on_the_stove: 0.0 (0/10)
  KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it: 0.1 (1/10)
n_tasks: 10
n_rollouts: 100 (10 per task)
log_path: /root/runs/acr-vla-conformal-refinement/eval-vla-only-long-seed48.log
result_path: /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed48.json
checkpoint_path: N/A (eval only)
wandb_run_id: N/A
```

### 实验 2
```
exp_id: eval-vla-only-object-seed50
status: success (EXIT_CODE=0)
overall_success_rate: 0.09
per_task:
  pick_up_the_alphabet_soup_and_place_it_in_the_basket: 0.0 (0/10)
  pick_up_the_cream_cheese_and_place_it_in_the_basket: 0.1 (1/10)
  pick_up_the_salad_dressing_and_place_it_in_the_basket: 0.1 (1/10)
  pick_up_the_bbq_sauce_and_place_it_in_the_basket: 0.2 (2/10)
  pick_up_the_ketchup_and_place_it_in_the_basket: 0.0 (0/10)
  pick_up_the_tomato_sauce_and_place_it_in_the_basket: 0.1 (1/10)
  pick_up_the_butter_and_place_it_in_the_basket: 0.0 (0/10)
  pick_up_the_milk_and_place_it_in_the_basket: 0.1 (1/10)
  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: 0.1 (1/10)
  pick_up_the_orange_juice_and_place_it_in_the_basket: 0.2 (2/10)
n_tasks: 10
n_rollouts: 100 (10 per task)
log_path: /root/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed50.log
result_path: /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed50.json
checkpoint_path: N/A (eval only)
wandb_run_id: N/A
```

### 实验 3
```
exp_id: eval-crm-long-seed46
status: success (EXIT_CODE=0)
overall_success_rate: 0.18
per_task:
  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: 0.0 (0/10)
  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: 0.0 (0/10)
  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: 0.9 (9/10)
  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: 0.0 (0/10)
  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: 0.2 (2/10)
  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy: 0.2 (2/10)
  LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate: 0.0 (0/10)
  LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket: 0.0 (0/10)
  KITCHEN_SCENE8_put_both_moka_pots_on_the_stove: 0.0 (0/10)
  KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it: 0.5 (5/10)
n_tasks: 10
n_rollouts: 100 (10 per task)
log_path: /root/runs/acr-vla-conformal-refinement/eval-crm-long-seed46.log
result_path: /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed46.json
checkpoint_path: N/A (eval only)
wandb_run_id: N/A
```

---

**摘要**: CRM obs_only (ε=0.2, K=10) 在 LIBERO-Long 上 18% vs VLA-only baseline 14%，提升 +4pp。主要增益来自 KITCHEN_SCENE3 (80%→90%) 和 KITCHEN_SCENE6 (10%→50%)，但 LIVING_ROOM_SCENE5 和 SCENE6 有回退。LIBERO-Object 的 VLA-only baseline seed50 仅 9%，显著低于其他 seed。

---
