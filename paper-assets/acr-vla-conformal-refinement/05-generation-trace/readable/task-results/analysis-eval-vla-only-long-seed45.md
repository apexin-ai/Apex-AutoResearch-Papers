# analysis eval vla only long seed45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-vla-only-long-seed45_20260519T192037_result.json`
- **Structured JSON:** [`27e5ca84b4df799f86a1.json`](../../sessions/27/27e5ca84b4df799f86a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

## 结果总结

**eval-vla-only-long-seed45**: overall_success_rate = **17% (17/100)**

Per-task breakdown:

| Task | Success Rate |
|------|-------------|
| KITCHEN_SCENE3 (stove + moka pot) | 100% (10/10) |
| LIVING_ROOM_SCENE5 (mugs on plates) | 20% (2/10) |
| STUDY_SCENE1 (book in caddy) | 20% (2/10) |
| KITCHEN_SCENE6 (mug in microwave) | 20% (2/10) |
| LIVING_ROOM_SCENE6 (mug + pudding) | 10% (1/10) |
| LIVING_ROOM_SCENE2 (soup + tomato) | 0% |
| LIVING_ROOM_SCENE2 (cheese + butter) | 0% |
| KITCHEN_SCENE4 (bowl in drawer) | 0% |
| LIVING_ROOM_SCENE1 (soup + cheese) | 0% |
| KITCHEN_SCENE8 (two moka pots) | 0% |

## 4-seed 汇总 (VLA-only, LIBERO-Long)

| Seed | Success Rate |
|------|-------------|
| 42 | 11% |
| 43 | 13% |
| 44 | 12% |
| 45 | **17%** |

**Mean ± Std = 13.25% ± 2.63%**

seed45 是 4 个 seed 中最高的（17%），比前 3 个 seed 均值 12.0% 高出 5pp。方差主要来自 seed45，但整体 VLA-only baseline 在 Long suite 上稳定偏低（~13%），符合预期——长 horizon 多步任务对纯 VLA 挑战很大。

---
