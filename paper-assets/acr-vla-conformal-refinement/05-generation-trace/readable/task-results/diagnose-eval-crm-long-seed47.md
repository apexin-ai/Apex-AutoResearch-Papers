# diagnose eval crm long seed47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-crm-long-seed47_20260520T000825_result.json`
- **Structured JSON:** [`52f8461b6bd647ae2ef5.json`](../../sessions/52/52f8461b6bd647ae2ef5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。**Cron false positive**——实验正常完成，无任何错误。

```json
{
  "root_cause": "eval脚本不写W&B也不写sentinel file，进程正常退出后cron检测找不到完成标记，自动标记为failed",
  "error_type": "cron_false_positive",
  "actual_completed": true,
  "metrics": {
    "overall_success_rate": 0.17,
    "per_task": {
      "LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket": 0.0,
      "LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket": 0.0,
      "KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it": 0.8,
      "KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it": 0.0,
      "LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate": 0.2,
      "STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy": 0.2,
      "LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate": 0.0,
      "LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket": 0.0,
      "KITCHEN_SCENE8_put_both_moka_pots_on_the_stove": 0.0,
      "KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it": 0.5
    }
  },
  "fix_steps": ["将实验状态从failed改为completed", "记录SR=17%到实验追踪表"]
}
```

日志尾部打印了 `Overall success rate (crm_obs_only): 17.0% (17/100)`，JSON 结果文件也完整写出。无 Traceback、无 OOM、无任何异常。进程已正常退出。与 seed45 (SR=18%) 完全相同的 false positive 模式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "eval脚本不写W&B也不写sentinel file，进程正常退出后cron检测找不到完成标记，自动标记为failed",
    "error_type": "cron_false_positive",
    "actual_completed": true,
    "metrics": {
      "overall_success_rate": 0.17,
      "per_task": {
        "LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket": 0.0,
        "LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket": 0.0,
        "KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it": 0.8,
        "KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it": 0.0,
        "LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate": 0.2,
        "STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy": 0.2,
        "LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate": 0.0,
        "LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket": 0.0,
        "KITCHEN_SCENE8_put_both_moka_pots_on_the_stove": 0.0,
        "KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it": 0.5
      }
    },
    "fix_steps": [
      "将实验状态从failed改为completed",
      "记录SR=17%到实验追踪表"
    ]
  }
}
```

</details>

---
