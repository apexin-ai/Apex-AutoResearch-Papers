# analyze pi05 object baseline harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-object-baseline-harvest_20260521T121542_result.json`
- **Structured JSON:** [`fed2dfc3a43962da65f5.json`](../../sessions/fe/fed2dfc3a43962da65f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 experiments updated to DONE. Here's the summary:

```
=== π0.5 VLA-only Object Baseline Results ===
seed42: SR = 82.0% (164/200, 10 tasks × 20 rollouts)
seed43: SR = 81.5% (163/200, 10 tasks × 20 rollouts)
seed44: SR = 81.0% (162/200, 10 tasks × 20 rollouts)
Mean ± Std: 81.5% ± 0.5%

Per-task breakdown:
Task                    seed42  seed43  seed44  Mean
alphabet_soup            85%     80%     85%    83.3%
cream_cheese            100%     95%     95%    96.7%
salad_dressing           60%     70%     65%    65.0%
bbq_sauce                80%     85%     80%    81.7%
ketchup                  80%     80%     85%    81.7%
tomato_sauce             55%     60%     55%    56.7%
butter                  100%     95%     90%    95.0%
milk                     80%     80%     85%    81.7%
chocolate_pudding       100%    100%    100%   100.0%
orange_juice             80%     70%     70%    73.3%

Log paths (bjb1-32546):
  ~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed{42,43,44}-r3.log
JSON results:
  /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed{42,43,44}.json
Model: /root/autodl-tmp/models/pi05_libero_finetuned/
```

结果非常稳定（std=0.5%）。最难的 task 是 tomato_sauce（56.7%）和 salad_dressing（65.0%），最简单的是 chocolate_pudding（100%）。

---
