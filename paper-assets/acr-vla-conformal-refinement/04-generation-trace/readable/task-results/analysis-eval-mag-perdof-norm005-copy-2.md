# analysis eval mag perdof norm005

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-perdof-norm005_20260515T172333_result.json`
- **Structured JSON:** [`e473d4cc764e12548502.json`](../../sessions/e4/e473d4cc764e12548502.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

**eval-mag-perdof-norm005** — perdof CRM v3-norm, spatial, norm=0.05, **完成，NEGATIVE**

| Task | SR |
|---|---|
| T0 between_plate_ramekin | 50% |
| T1 next_to_ramekin | 100% |
| T2 table_center | 0% |
| T3 on_cookie_box | 30% |
| T4 top_drawer | 0% |
| T5 on_ramekin | 0% |
| T6 next_to_cookie_box | 100% |
| T7 on_stove | 0% |
| T8 next_to_plate | 30% |
| T9 on_wooden_cabinet | 0% |
| **10-task avg** | **31%** |

**对比参考值：**
- perdof norm=0.1 = 35% → norm=0.05 降至 31%，更差
- obs_only norm=0.05 = 35% → perdof 同 norm 下差 4pp
- argmin baseline = 34% → perdof norm=0.05 低于 baseline 3pp
- perdof norm=0.03 = 30% → norm=0.05 仅比 0.03 高 1pp

**结论：negative。** 31% < 33% 阈值，低于 argmin baseline (34%)。perdof 在所有测试 norm 值下均未能超过 argmin baseline，表明 per-DoF correction 方向在 spatial benchmark 上不如 obs_only 和 argmin。

---
