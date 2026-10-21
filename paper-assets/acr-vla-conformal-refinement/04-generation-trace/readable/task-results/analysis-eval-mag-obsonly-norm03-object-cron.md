# analysis eval mag obsonly norm03 object cron

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-obsonly-norm03-object-cron_20260516T074107_result.json`
- **Structured JSON:** [`37170ccb46efb72026bb.json`](../../sessions/37/37170ccb46efb72026bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被清理）。

```
STATUS: success
OVERALL_SR: 19% (19/100)
PER_TASK_SR:
  alphabet_soup: 0%
  cream_cheese: 0%
  salad_dressing: 30%
  bbq_sauce: 30%
  ketchup: 0%
  tomato_sauce: 10%
  butter: 20%
  milk: 20%
  chocolate_pudding: 50%
  orange_juice: 30%
REGISTRY: updated (DONE, conclusion=success)
CRON: already deleted
```

**对比**: norm=0.3 (19%) 与 norm=0.1 (19%) 持平，低于 norm=0.2 (22%)，高于 argmin baseline (12%) 和 default (17%)。norm=0.2 仍是 obs_only magnitude sweep 的最优点。

---
