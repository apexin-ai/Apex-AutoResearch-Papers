# analysis westd vla only harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_westd-vla-only-harvest_20260526T115544_result.json`
- **Structured JSON:** [`50db3739836556d79eab.json`](../../sessions/50/50db3739836556d79eab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Conclusion updates failed because I used a long string — but all 6 experiments already had `conclusion: "success"` and `status: DONE` set from prior state. Metrics, checkpoint_path, and log_path all updated successfully.

## 汇总表

| exp_id | Benchmark | Seed | SR | 结论 |
|--------|-----------|------|----|------|
| westd-pi05-vla-only-goal-s42-paired | goal | 42 | **97.5%** | success |
| westd-pi05-vla-only-goal-s43-paired | goal | 43 | **96.5%** | success |
| westd-pi05-vla-only-goal-s44-paired | goal | 44 | **95.5%** | success |
| westd-pi05-vla-only-object-s42-paired | object | 42 | **99.5%** | success |
| westd-pi05-vla-only-object-s43-paired | object | 43 | **100%** | success |
| westd-pi05-vla-only-object-s44-paired | object | 44 | **99.5%** | success |

**均值**: Goal = 96.5% (±1.0%), Object = 99.7% (±0.3%)

最难任务: `open_the_top_drawer_and_put_the_bowl_inside` (goal benchmark, 跨 seed 80%-90%)，`pick_up_the_bbq_sauce` (object benchmark, 两个 seed 95%)。

---
