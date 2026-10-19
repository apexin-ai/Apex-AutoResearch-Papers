# analysis eval obs only spatial norm02 seed47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-obs-only-spatial-norm02-seed47_20260519T170159_result.json`
- **Structured JSON:** [`dd35e87f2045f15a657f.json`](../../sessions/dd/dd35e87f2045f15a657f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。下面是分析总结。

---

## eval-obs-only-spatial-norm02-seed47 结果分析

**seed47 success rate: 32.0% (32/100)**

### Per-task breakdown

| Task | SR |
|------|-----|
| between_plate_and_ramekin | 80% |
| next_to_ramekin | 90% |
| next_to_cookie_box | 90% |
| on_cookie_box | 30% |
| next_to_plate | 20% |
| in_top_drawer | 10% |
| from_table_center | 0% |
| on_ramekin | 0% |
| on_stove | 0% |
| on_wooden_cabinet | 0% |

### n=4 cross-seed statistics (obs_only CRM, Spatial)

| Seed | SR |
|------|-----|
| 42 | 35% |
| 44 | 36% |
| 45 | 34% |
| 47 | 32% |
| **Mean ± Std** | **34.25% ± 1.71%** |

### vs VLA-only baseline (29.3% ± 1.7%, n=4)

- **Absolute improvement**: +4.95 pp
- **Welch's t-test**: t = 4.11, df ≈ 6, **p ≈ 0.006** (two-tailed)
- 统计显著 (p < 0.01)

### Conclusion: **success**

seed47 (32%) > VLA baseline (29.3%)。加入后 n=4 均值 34.25% ± 1.71%，相对 VLA-only 提升 16.9%，Welch's t-test p≈0.006，差异显著。obs_only CRM 在 LIBERO-Spatial 上的改进效果跨 seed 稳健。

---
