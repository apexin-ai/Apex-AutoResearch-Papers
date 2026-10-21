# analysis magnitude curve consolidation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_magnitude-curve-consolidation_20260517T224156_result.json`
- **Structured JSON:** [`32aa239c3bc5fa7287ef.json`](../../sessions/32/32aa239c3bc5fa7287ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。数据已写入 `artifacts/magnitude_curve_data.md`。

核心发现：
- **obs_only**: 全 ε 范围平坦（13–17.5%），即使 default uncapped 也不崩溃
- **perdof**: 从 ε=0.05 的 14% 逐步下降到 default 的 0%（progressive collapse）
- **统计充足度**: ε=0.10 和 ε=0.20 两模型均 ≥3 seeds；ε=0.30 和 default 也够 3 seeds
- **关键缺口**: ε=0.03 和 ε=0.05 两模型都只有 1 seed（当前仅 obs_only ε=0.05 seed43 在跑），perdof ε=0.05 完全无补充计划

---
