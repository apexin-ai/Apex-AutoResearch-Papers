# analysis eval vla only object seed44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-vla-only-object-seed44-r2_20260516T064908_result.json`
- **Structured JSON:** [`493381a03698a91b35cb.json`](../../sessions/49/493381a03698a91b35cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
TASKS_DONE: 100
TASKS_TOTAL: 100
OVERALL_SR: 10%
PER_TASK_SR:
  pick_up_the_alphabet_soup_and_place_it_in_the_basket: 0%
  pick_up_the_cream_cheese_and_place_it_in_the_basket: 10%
  pick_up_the_salad_dressing_and_place_it_in_the_basket: 20%
  pick_up_the_bbq_sauce_and_place_it_in_the_basket: 20%
  pick_up_the_ketchup_and_place_it_in_the_basket: 0%
  pick_up_the_tomato_sauce_and_place_it_in_the_basket: 0%
  pick_up_the_butter_and_place_it_in_the_basket: 0%
  pick_up_the_milk_and_place_it_in_the_basket: 10%
  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: 20%
  pick_up_the_orange_juice_and_place_it_in_the_basket: 20%
CONCLUSION: success
ANALYSIS: seed44 整体 SR=10%，与 seed42=12%、seed43=12% 基本一致（差异 2pp，在 10 rollouts/task 的方差范围内）。三个 seed 的 VLA-only baseline 稳定在 10-12%，确认 baseline 稳定可靠。各 task 表现模式也一致：alphabet_soup/ketchup/tomato_sauce/butter 始终是 0% 的难任务，salad_dressing/bbq_sauce/chocolate_pudding/orange_juice 在 10-20% 波动。
LOG_TAIL:
  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5
  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10
[pick_up_the_butter_and_place_it_in_the_basket] success rate: 0.0% (0/10)
  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5
  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/10, success so far: 1/10
[pick_up_the_milk_and_place_it_in_the_basket] success rate: 10.0% (1/10)
  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5
  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/10, success so far: 2/10
[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 20.0% (2/10)
  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5
  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/10, success so far: 2/10
[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 20.0% (2/10)

============================================================
Overall success rate (vla_only): 10.0% (10/100)
============================================================
[eval] Results saved to logs/eval_object_vla_only_seed44.json
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
EXIT_CODE=129
EXIT_CODE=0
```

---
