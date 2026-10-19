# analysis eval vla only object seed44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-vla-only-object-seed44-r2_20260516T050106_result.json`
- **Structured JSON:** [`80c8d75543bbb91753cc.json`](../../sessions/80/80c8d75543bbb91753cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**总体 SR: 10.0% (10/100)**

日志正常结束，最终 `EXIT_CODE=0`，无 error/traceback。

各 task SR：

| Task | SR |
|---|---|
| pick_up_the_alphabet_soup | 0% (0/10) |
| pick_up_the_cream_cheese | 10% (1/10) |
| pick_up_the_salad_dressing | 20% (2/10) |
| pick_up_the_bbq_sauce | 20% (2/10) |
| pick_up_the_ketchup | 0% (0/10) |
| pick_up_the_tomato_sauce | 0% (0/10) |
| pick_up_the_butter | 0% (0/10) |
| pick_up_the_milk | 10% (1/10) |
| pick_up_the_chocolate_pudding | 20% (2/10) |
| pick_up_the_orange_juice | 20% (2/10) |

三个 seed 汇总：

| Seed | SR |
|---|---|
| 42 | 12% |
| 43 | 12% |
| 44 | 10% |
| **Mean ± Std** | **11.3% ± 0.9%** |

符合预期范围（10-15%）。日志中未见 W&B run ID。

---
