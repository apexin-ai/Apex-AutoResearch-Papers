# harvest eval adaptive k spatial p50 seed44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval-adaptive-k-spatial-p50-seed44-r2_20260520T095202_result.json`
- **Structured JSON:** [`f94c50eb12c9fa50aceb.json`](../../sessions/f9/f94c50eb12c9fa50aceb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。完整 metrics：

| 指标 | 值 |
|---|---|
| **overall_success_rate** | **33%** (33/100) |
| avg_k | 6.40 |
| fast_path_ratio | 45.0% |
| adaptive_trigger_rate | 55.0% |
| mean_l2_distance | 0.0923 |
| threshold | 0.074855 |
| total_steps | 23,661 |
| fast_steps | 10,649 |
| full_steps | 13,012 |
| total_rollouts | 100 |

**Per-task SR:**

| Task | SR |
|---|---|
| next_to_ramekin | 100% |
| next_to_cookie_box | 90% |
| between_plate_and_ramekin | 60% |
| next_to_plate | 40% |
| on_cookie_box | 30% |
| in_top_drawer | 10% |
| from_table_center | 0% |
| on_ramekin | 0% |
| on_stove | 0% |
| on_wooden_cabinet | 0% |

与 seed43-r2 高度一致：SR 33% vs 33%，avg_k 6.40 vs 6.33，fast_path 45.0% vs 45.8%。Adaptive K 在 Spatial benchmark 上稳定复现，结论 success。

---
