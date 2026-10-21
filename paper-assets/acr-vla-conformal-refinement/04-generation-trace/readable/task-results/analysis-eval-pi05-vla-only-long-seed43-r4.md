# analysis eval pi05 vla only long seed43 r4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-pi05-vla-only-long-seed43-r4_20260522T155135_result.json`
- **Structured JSON:** [`2c6c4029f59782e8c660.json`](../../sessions/2c/2c6c4029f59782e8c660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B 查询工具报错，但日志数据已完整。以下是结果汇总：

---

## seed43: **96.0%** (96/100)

| Task | Success Rate |
|------|-------------|
| LIVING_ROOM_SCENE2 — alphabet soup & tomato sauce in basket | 100% (10/10) |
| LIVING_ROOM_SCENE2 — cream cheese box & butter in basket | 100% (10/10) |
| KITCHEN_SCENE3 — turn on stove & put moka pot | 100% (10/10) |
| KITCHEN_SCENE4 — black bowl in drawer & close | 100% (10/10) |
| LIVING_ROOM_SCENE5 — white mug left plate & yellow mug right plate | **90%** (9/10) |
| STUDY_SCENE1 — book in back compartment of caddy | 100% (10/10) |
| LIVING_ROOM_SCENE6 — white mug on plate & chocolate pudding right | 100% (10/10) |
| LIVING_ROOM_SCENE1 — alphabet soup & cream cheese in basket | 100% (10/10) |
| KITCHEN_SCENE8 — both moka pots on stove | **70%** (7/10) |
| KITCHEN_SCENE6 — yellow mug in microwave & close | 100% (10/10) |

## seed44: **95.0%** (95/100) — 也已完成

| Task | Success Rate |
|------|-------------|
| LIVING_ROOM_SCENE2 — alphabet soup & tomato sauce in basket | 100% (10/10) |
| LIVING_ROOM_SCENE2 — cream cheese box & butter in basket | 100% (10/10) |
| KITCHEN_SCENE3 — turn on stove & put moka pot | 100% (10/10) |
| KITCHEN_SCENE4 — black bowl in drawer & close | 100% (10/10) |
| LIVING_ROOM_SCENE5 — white mug left plate & yellow mug right plate | 100% (10/10) |
| STUDY_SCENE1 — book in back compartment of caddy | 100% (10/10) |
| LIVING_ROOM_SCENE6 — white mug on plate & chocolate pudding right | 100% (10/10) |
| LIVING_ROOM_SCENE1 — alphabet soup & cream cheese in basket | **90%** (9/10) |
| KITCHEN_SCENE8 — both moka pots on stove | **60%** (6/10) |
| KITCHEN_SCENE6 — yellow mug in microwave & close | 100% (10/10) |

## 3-seed 汇总（含 seed42 = 94.0%）

| Seed | Overall |
|------|---------|
| 42 | 94.0% |
| 43 | 96.0% |
| 44 | 95.0% |
| **Mean ± Std** | **95.0% ± 0.82%** |

## 注意事项

- **KITCHEN_SCENE8 (both moka pots on stove)** 是一致性最差的 task：seed43=70%, seed44=60%，明显是 π0.5 在 Long benchmark 上的 hard task
- 其余 9 个 task 几乎全部 100%，仅有零星 1 个 rollout 失败
- 两个 seed 都正常退出（EXIT_CODE=0），无异常

---
