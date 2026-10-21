# analysis eval perdof object norm03 seed45 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-perdof-object-norm03-seed45-r2_20260517T105635_result.json`
- **Structured JSON:** [`bd7d75bee5b9b43d0f3d.json`](../../sessions/bd/bd7d75bee5b9b43d0f3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

## eval-perdof-object-norm03-seed45-r2 Results

| Metric | Value |
|---|---|
| **Overall SR** | **6%** (6/100) |
| Conclusion | **success** (hypothesis confirmed) |

**Per-task breakdown:**

| Task | SR |
|---|---|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| ketchup | 0% |
| tomato_sauce | 0% |
| milk | 0% |
| salad_dressing | 10% |
| butter | 10% |
| chocolate_pudding | 10% |
| orange_juice | 10% |
| bbq_sauce | 20% |

**perdof ε=0.3 三 seed 汇总:** seed42=4%, seed44=4%, seed45=6% → **mean ≈ 4.7% ± 1.2%**

对比 obs_only ε=0.3: seed42=19%, seed44=18%, seed45=14% → mean ≈ 17%

perdof 在高 norm 下的 collapse 完全确认，SR 远低于 obs_only，支持 magnitude curve 中 perdof 急剧下降的叙事。

---
