# analyze pi05 adaptive goal s44 bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-adaptive-goal-s44-bjb1_20260526T140311_result.json`
- **Structured JSON:** [`e69f8fa5611feb4b7668.json`](../../sessions/e6/e69f8fa5611feb4b7668.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。结果汇总：

## pi05-adaptive-goal-s44-bjb1 实验结果

**Conclusion: NEGATIVE** — SR 86.5% 远低于 VLA-only baseline (~96%)

### 总体指标
| 指标 | 值 |
|------|-----|
| Overall SR | **86.5%** (173/200) |
| Trigger Rate | 10.0% (2785/27810 steps) |
| Mean Uncertainty | 0.1269 |
| Mean Correction Norm | 0.20 |
| τ (conformal threshold) | 0.25 |

### Per-task Breakdown
| Task | SR | Successes/Total |
|------|-----|-----------------|
| open_the_middle_drawer_of_the_cabinet | 85% | 17/20 |
| put_the_bowl_on_the_stove | **100%** | 20/20 |
| put_the_wine_bottle_on_top_of_the_cabinet | **60%** | 12/20 |
| open_the_top_drawer_and_put_the_bowl_inside | **65%** | 13/20 |
| put_the_bowl_on_top_of_the_cabinet | **100%** | 20/20 |
| push_the_plate_to_the_front_of_the_stove | 90% | 18/20 |
| put_the_cream_cheese_in_the_bowl | **100%** | 20/20 |
| turn_on_the_stove | **100%** | 20/20 |
| put_the_bowl_on_the_plate | 95% | 19/20 |
| put_the_wine_bottle_on_the_rack | **70%** | 14/20 |

### 诊断
- 无 OOM/CUDA error，EXIT_CODE=0，实验执行正常
- 损失主要集中在 3 个 task：wine_bottle_on_cabinet (60%)、drawer_bowl (65%)、wine_bottle_on_rack (70%)
- trigger_rate 仅 10%，说明 τ=0.25 阈值较高，大部分时间 CRM 未介入，但即使低介入率仍导致了显著性能下降——Adaptive Conformal 在 π0.5 + Goal 上的 correction 方向可能有害

---
