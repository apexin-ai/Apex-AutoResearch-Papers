# analyze pi05 crm k2 object s42 bjb1 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-crm-k2-object-s42-bjb1-r2_20260526T142112_result.json`
- **Structured JSON:** [`79c994a5eb0f2bd407c5.json`](../../sessions/79/79c994a5eb0f2bd407c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE. Results:

```
=== RESULT ===
exp_id: pi05-crm-k2-object-s42-bjb1-r2
success_rate: 89.0%
successes: 178
total_rollouts: 200
per_task: {
  alphabet_soup: 100.0% (20/20),
  cream_cheese: 75.0% (15/20),
  salad_dressing: 95.0% (19/20),
  bbq_sauce: 95.0% (19/20),
  ketchup: 65.0% (13/20),
  tomato_sauce: 85.0% (17/20),
  butter: 95.0% (19/20),
  milk: 95.0% (19/20),
  chocolate_pudding: 95.0% (19/20),
  orange_juice: 90.0% (18/20)
}
errors: none
OOM: none
trigger_rate: N/A (always-on mode)
mean_uncertainty: not logged
conclusion: success
=== END ===
```

与 s44 (88%, 176/200) 高度一致，s42 略高 1pp。ketchup (65%) 和 cream_cheese (75%) 是两个最弱 task。

---
