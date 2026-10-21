# analysis eval mag obsonly norm005

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-obsonly-norm005_20260515T160124_result.json`
- **Structured JSON:** [`6048cce540e96b2344a3.json`](../../sessions/60/6048cce540e96b2344a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

## 最终结果：eval-mag-obsonly-norm005

**CRM v3-norm obs_only | spatial | max_correction_norm=0.05 | 10 rollouts × 10 tasks**

| Task | SR |
|---|---|
| T0: between_plate_ramekin | 80% |
| T1: next_to_ramekin | 90% |
| T2: table_center | 0% |
| T3: on_cookie_box | 40% |
| T4: top_drawer | 10% |
| T5: on_ramekin | 0% |
| T6: next_to_cookie_box | 80% |
| T7: on_stove | **0%** ← 新 |
| T8: next_to_plate | **50%** ← 新 |
| T9: on_wooden_cabinet | **0%** ← 新 |
| **Overall** | **35.0%** |

## Obs_only magnitude sweep 对比（spatial, 10-task final）

| norm | SR | 备注 |
|---|---|---|
| 0.03 | 55.0% (4t 中间值) | 待完成 |
| **0.05** | **35.0%** | ✅ 完成 |
| 0.2 | 45.7% (7t 中间值) | 待完成 |
| 0.3 | 46.0% (5t 中间值) | 待完成 |

norm=0.05 的最终 10-task SR（35.0%）比 7-task 中间值（42.9%）下降明显，后 3 个 task 仅 T8 有 50%，T7/T9 均为 0%。在当前 sweep 中 norm=0.05 是最低点。

---
