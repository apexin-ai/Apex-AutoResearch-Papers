# analyze eval obs only spatial norm02 seed46 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-spatial-norm02-seed46-r2_20260519T185433_result.json`
- **Structured JSON:** [`672ca499c39eb600db28.json`](../../sessions/67/672ca499c39eb600db28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**结论: SUCCESS** — SR=33.0%，高于 VLA-only baseline (29.3%±1.7%)。

**关键数据**:
- 100 rollouts (10 tasks × 10)，正常结束无异常
- 4-seed 均值 33.75% (seed44=36%, seed45=34%, seed46=33%, seed47=32%)
- seed46 与其他 seeds 一致，落在 32%-36% 范围内

**Per-task 特征**: 强二分性——3 个 task ≥80% (next_to_ramekin 100%, between_plate_and_ramekin 90%, next_to_cookie_box 80%)，4 个 task 稳定 0% (from_table_center, on_ramekin, on_stove, on_wooden_cabinet)。这是跨 seed 稳定的系统性模式，非随机波动。

---
