# analyze eval vla only long seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-vla-only-long-seed43_20260519T183306_result.json`
- **Structured JSON:** [`15447db17dac01d30724.json`](../../sessions/15/15447db17dac01d30724.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

## eval-vla-only-long-seed43 Metrics Summary

**Overall success rate: 13% (13/100 rollouts)**

| Task | Success Rate |
|------|-------------|
| KITCHEN_SCENE3 — stove + moka pot | **70%** |
| LIVING_ROOM_SCENE5 — white mug left, yellow mug right | **30%** |
| KITCHEN_SCENE6 — yellow/white mug in microwave | **20%** |
| LIVING_ROOM_SCENE6 — white mug on plate + chocolate pudding | **10%** |
| LIVING_ROOM_SCENE2 — alphabet soup + tomato sauce | 0% |
| LIVING_ROOM_SCENE2 — cream cheese + butter | 0% |
| KITCHEN_SCENE4 — black bowl in drawer | 0% |
| STUDY_SCENE1 — book in caddy | 0% |
| LIVING_ROOM_SCENE1 — alphabet soup + cream cheese | 0% |
| KITCHEN_SCENE8 — both moka pots on stove | 0% |

VLA-only baseline 在 LIBERO-Long 上表现很弱，10 个 task 中 6 个完全失败，仅 KITCHEN_SCENE3 达到 70%。这为 CRM 校正留出了很大的提升空间。

---
