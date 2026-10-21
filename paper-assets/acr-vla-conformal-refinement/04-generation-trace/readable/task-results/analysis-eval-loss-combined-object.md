# analysis eval loss combined object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-loss-combined-object_20260522T104008_result.json`
- **Structured JSON:** [`d36e6fe06e3e676639d5.json`](../../sessions/d3/d36e6fe06e3e676639d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No errors/exceptions found. Results:

```
avg_success_rate: 9.0%
total_successes: 18/200
per_task:
  alphabet_soup:        0.0%  (0/20)
  cream_cheese:        10.0%  (2/20)
  salad_dressing:      10.0%  (2/20)
  bbq_sauce:           15.0%  (3/20)
  ketchup:              0.0%  (0/20)
  tomato_sauce:         5.0%  (1/20)
  butter:               5.0%  (1/20)
  milk:                10.0%  (2/20)
  chocolate_pudding:   25.0%  (5/20)
  orange_juice:        10.0%  (2/20)
errors: none
conclusion_recommendation: NEGATIVE
```

**结论**：Combined loss CRM 的 9.0% (18/200) 略好于 MSE re-trained 的 7% (14/200)，但差异微小（+2pp），远低于原 Plan A CRM (K=2) 的 18.3%±2.1%，也低于 VLA-only 的 10.8%±1.3%。Combined loss 方向确认失败——per-DOF + conformal 联合训练在 val_loss 阶段就已严重退化（2.5x worse），eval 结果与之一致。该 checkpoint 无进一步使用价值。

---
