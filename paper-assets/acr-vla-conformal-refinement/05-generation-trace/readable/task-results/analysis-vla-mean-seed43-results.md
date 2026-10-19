# analysis vla mean seed43 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vla-mean-seed43-results_20260516T045302_result.json`
- **Structured JSON:** [`95bd2be9e76aca495412.json`](../../sessions/95/95bd2be9e76aca495412.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval-vla-mean-object-seed43 结果：**

| Task | Success Rate | Successes/Total |
|------|-------------|-----------------|
| pick_up_the_alphabet_soup | 0.0 | 0/10 |
| pick_up_the_cream_cheese | 0.0 | 0/10 |
| pick_up_the_salad_dressing | 0.2 | 2/10 |
| pick_up_the_bbq_sauce | 0.3 | 3/10 |
| pick_up_the_ketchup | 0.1 | 1/10 |
| pick_up_the_tomato_sauce | 0.1 | 1/10 |
| pick_up_the_butter | 0.1 | 1/10 |
| pick_up_the_milk | 0.3 | 3/10 |
| pick_up_the_chocolate_pudding | 0.3 | 3/10 |
| pick_up_the_orange_juice | 0.1 | 1/10 |

- **overall_success_rate: 15%** (15/100 rollouts)
- baseline_mode: mean, K=10, benchmark: object

seed43 的 15% 比 seed42 的 12% 略高，但整体水平一致，VLA-mean baseline 在 object benchmark 上大约 12-15%。

---
