# analysis eval mag obsonly norm02

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-obsonly-norm02_20260515T160511_result.json`
- **Structured JSON:** [`633587b89dcdd04be1d0.json`](../../sessions/63/633587b89dcdd04be1d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果摘要：

## eval-mag-obsonly-norm02 结果

**obs_only CRM v3-norm | norm=0.2 | LIBERO spatial | K=10**

| Task | SR |
|---|---|
| T0 between_plate_ramekin | 90% |
| T1 next_to_ramekin | 100% |
| T2 table_center | 0% |
| T3 on_cookie_box | 30% |
| T4 top_drawer | 10% |
| T5 on_ramekin | 0% |
| T6 next_to_cookie_box | 90% |
| T7 on_stove | 0% |
| T8 next_to_plate | 30% |
| T9 on_wooden_cabinet | 0% |
| **Overall** | **35.0%** (35/100) |

**结论: negative** — 完整 10-task 结果从中期 7t 的 45.7% 跌落到 35%。后 3 个 task（T7/T8/T9）拉低了均值，其中 T7 和 T9 为 0%，T8 为 30%。

**magnitude sweep obs_only 对比（完整 10t 待补）：**

| norm | 7t avg | 10t avg |
|---|---|---|
| 0.05 | 42.9% | TBD |
| 0.1 | — | 35% |
| 0.2 | 45.7% | **35%** |
| 0.3 | 46.0% (5t) | TBD |

norm=0.2 最终与 obs_only norm=0.1 baseline 持平（均为 35%），未带来提升。

---
