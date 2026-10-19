# analysis eval mag perdof norm02 object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-perdof-norm02-object_20260516T064903_result.json`
- **Structured JSON:** [`1b7b9e84dbf75120f715.json`](../../sessions/1b/1b7b9e84dbf75120f715.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
TASKS_DONE: 10
TASKS_TOTAL: 10
OVERALL_SR: 11%
PER_TASK_SR:
  alphabet_soup: 0%
  cream_cheese: 10%
  salad_dressing: 10%
  bbq_sauce: 10%
  ketchup: 0%
  tomato_sauce: 0%
  butter: 10%
  milk: 10%
  chocolate_pudding: 40%
  orange_juice: 20%
CONCLUSION: negative
ANALYSIS: perdof norm=0.2 在 object benchmark 上仅 11%，与 argmin baseline 的 12% 基本持平（差距在噪声范围内），未带来任何提升。对比 spatial benchmark 上 perdof norm=0.2 的 28.3%（6task partial），object 上的表现显著更差，说明 perdof 的增益不具备跨 benchmark 泛化性——在 object 这种 pick-and-place 场景下，CRM correction 几乎无效。chocolate_pudding (40%) 是唯一明显高于 baseline 的 task，其余均在 0-10% 区间。
LOG_TAIL: (最后 20 行)
  [pick_up_the_chocolate_pudding...] success rate: 40.0% (4/10)
  pick_up_the_orange_juice... rollout 5/10, success so far: 1/5
  pick_up_the_orange_juice... rollout 10/10, success so far: 2/10
  [pick_up_the_orange_juice...] success rate: 20.0% (2/10)

  ============================================================
  Overall success rate (crm_perdof): 11.0% (11/100)
  ============================================================
  [eval] Results saved to logs/eval_object_perdof_norm02.json
  EXIT_CODE=0
```

---
