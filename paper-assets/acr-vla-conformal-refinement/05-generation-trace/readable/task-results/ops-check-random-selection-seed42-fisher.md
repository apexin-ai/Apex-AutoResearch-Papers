# ops check random selection seed42 fisher

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-random-selection-seed42-fisher_20260518T054851_result.json`
- **Structured JSON:** [`e42b6ed4be5795c5b40e.json`](../../sessions/e4/e42b6ed4be5795c5b40e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Status Report

### Random Selection seed42 (bjb2-40593)
**Still running** — 7/10 tasks completed, PID 395256 active since May 17.

Completed tasks so far:
| Task | SR |
|------|-----|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 10% (1/10) |
| salad_dressing | 10% (1/10) |
| bbq_sauce | 40% (4/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 20% (2/10) |
| butter | 0% (0/10) |

Running total: **8/70 = 11.4%** (3 tasks remaining: milk, chocolate_pudding, orange_juice)

### Random Selection seed43/44 (bjb2-28827)
**Not found** — no random_selection logs or JSONs exist on bjb2-28827. These experiments were never started.

### Fisher Exact Test
**Cannot run yet** — only partial data from seed42 (70/100 rollouts). No seed43/44 data exists.

Preliminary estimate based on 7/10 tasks: ~11.4% random selection vs 17.5% CRM obs_only (ε=0.2). The remaining 3 tasks (milk, chocolate_pudding, orange_juice) tend to have higher SR in CRM experiments, so the final random selection SR could increase.

Estimated completion: ~3-5 hours for remaining 3 tasks (30 rollouts).

**Recommendation:** Wait for seed42 to finish, then start seed43/44 on bjb2-28827 to get enough pooled data for a meaningful Fisher test.

---
