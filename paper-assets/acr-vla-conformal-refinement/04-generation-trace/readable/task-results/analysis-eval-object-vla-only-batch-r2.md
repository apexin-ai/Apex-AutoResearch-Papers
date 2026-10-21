# analysis eval object vla only batch r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-object-vla-only-batch-r2_20260523T070438_result.json`
- **Structured JSON:** [`6fa528b7e6a5b85acfca.json`](../../sessions/6f/6fa528b7e6a5b85acfca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
RESULTS:
eval-object-vla-only-wrapper-s42-r2: SR=79.0%, episodes=200
eval-object-vla-only-wrapper-s43-r2: SR=77.0%, episodes=200
eval-object-vla-only-wrapper-s44-r2: SR=77.5%, episodes=200
eval-supp-obj-adapt-s42-r2: SR=77.5%, trigger_rate=70.2%, episodes=200

VLA-only 3-seed: mean=77.8% ± 1.0%
```

Per-task breakdown (20 rollouts each):

| Task | s42 | s43 | s44 | Adaptive |
|------|-----|-----|-----|----------|
| alphabet_soup | 85% | 70% | 70% | 80% |
| cream_cheese | 75% | 70% | 70% | 90% |
| salad_dressing | 85% | 75% | 75% | 70% |
| bbq_sauce | 85% | 85% | 90% | 85% |
| ketchup | 90% | 80% | 90% | 70% |
| tomato_sauce | 75% | 85% | 80% | 75% |
| butter | 65% | 60% | 75% | 65% |
| milk | 65% | 75% | 65% | 65% |
| chocolate_pudding | 70% | 75% | 65% | 80% |
| orange_juice | 95% | 95% | 95% | 95% |

Adaptive CRM (tau=0.074855) 的 overall SR 与 VLA-only s42 同 seed 相比从 79.0% 降到 77.5%，mean_unc=0.1104，trigger_rate=70.2%（70% 的 step 触发了 CRM 修正）。修正过于频繁但未带来提升，cream_cheese 和 chocolate_pudding 有改善，但 ketchup 和 salad_dressing 明显下降。

---
