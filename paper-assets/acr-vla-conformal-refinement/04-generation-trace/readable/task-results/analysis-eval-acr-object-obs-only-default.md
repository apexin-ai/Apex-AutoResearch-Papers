# analysis eval acr object obs only default

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-acr-object-obs-only-default_20260516T064252_result.json`
- **Structured JSON:** [`e13b3de50abbb4afc246.json`](../../sessions/e1/e13b3de50abbb4afc246.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
TASKS_DONE: 10
TASKS_TOTAL: 10
OVERALL_SR: 17%
PER_TASK_SR: {alphabet_soup: 0%, cream_cheese: 0%, salad_dressing: 20%, bbq_sauce: 40%, ketchup: 0%, tomato_sauce: 10%, butter: 10%, milk: 10%, chocolate_pudding: 50%, orange_juice: 30%}
CONCLUSION: negative
ANALYSIS: Default max_correction_norm (~1.42) 的 obs_only 得到 17% SR，与 norm=0.1 (19%) 和 norm=0.2 (22%) 相比略低但处于同一量级。这说明 obs_only 模式对 correction norm 的大小确实非常鲁棒——即使 norm 从 0.1 放大到 1.42（14倍），SR 仅从 19-22% 微降到 17%，差异在统计噪声范围内。但整体 SR 仍然很低（17%），远低于 baseline 或 full CRM 的表现，说明 obs_only 本身的 refinement 能力有限，而非 norm 控制的问题。Hypothesis 部分验证：obs_only 对 norm 确实鲁棒，但鲁棒地维持在低性能水平。
LOG_TAIL:
[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 50.0% (5/10)
  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/10, success so far: 2/5
  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 10/10, success so far: 3/10
[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 30.0% (3/10)

============================================================
Overall success rate (crm_obs_only): 17.0% (17/100)
============================================================
[eval] Results saved to logs/eval_object_obs_only_default_norm.json
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
EXIT_CODE=0
```

---
