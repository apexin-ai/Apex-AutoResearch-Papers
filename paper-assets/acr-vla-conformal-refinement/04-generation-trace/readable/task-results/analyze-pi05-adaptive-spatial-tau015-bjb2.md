# analyze pi05 adaptive spatial tau015 bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-adaptive-spatial-tau015-bjb2_20260526T174119_result.json`
- **Structured JSON:** [`beeac5fea346dab4c599.json`](../../sessions/be/beeac5fea346dab4c599.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE(success)。

## 结果汇总

| 指标 | 值 |
|---|---|
| **SR** | **97%** (194/200) |
| **trigger_rate** | **11.2%** (2471/22013 steps) |
| **mean_correction_norm** | 0.2 |
| **mean_uncertainty** | 0.099 |
| **tau** | 0.15 |

**Per-task**: 6 tasks 100%, 2 tasks 95%, 2 tasks 90% (top_drawer, on_ramekin)

**vs tau=0.25 baseline**: SR 基本持平 (97% vs 97.2%), trigger_rate 大幅上升 (11.2% vs ~4%)。更低阈值触发了近 3 倍的修正，但并未提升 SR — 说明额外修正是冗余的。

**GPU**: cuda:0 已释放 (1 MiB / 24564 MiB)。

---
