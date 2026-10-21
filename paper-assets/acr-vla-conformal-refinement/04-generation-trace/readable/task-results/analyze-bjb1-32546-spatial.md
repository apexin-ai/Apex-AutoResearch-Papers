# analyze bjb1 32546 spatial

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_bjb1-32546-spatial_20260519T231940_result.json`
- **Structured JSON:** [`3385da8c08a9b87fb3fb.json`](../../sessions/33/3385da8c08a9b87fb3fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总：

## eval-obs-only-spatial-norm02-seed43-r2 结果

**Overall SR: 34%** (34/100), 10 tasks × 10 rollouts 全部完成。

### Per-task breakdown

| Task | SR | Successes |
|------|----|-----------|
| between plate and ramekin | 90% | 9/10 |
| next to ramekin | **100%** | 10/10 |
| next to cookie box | **100%** | 10/10 |
| on cookie box | 30% | 3/10 |
| next to plate | 20% | 2/10 |
| from table center | 0% | 0/10 |
| in top drawer | 0% | 0/10 |
| on ramekin | 0% | 0/10 |
| on stove | 0% | 0/10 |
| on wooden cabinet | 0% | 0/10 |

### CRM Spatial 全 seed 汇总（obs_only, ε=0.2, K=10）

| Seed | SR |
|------|----|
| 42 | 36% |
| **43** | **34%** |
| 44 | 35% |
| 45 | 33% |
| 46 | 33% |

**5-seed 均值: 34.2%**（VLA-only baseline ~29.5%，CRM 提升约 +4.7pp）

seed43 与其他 seed 一致，无异常。

---
