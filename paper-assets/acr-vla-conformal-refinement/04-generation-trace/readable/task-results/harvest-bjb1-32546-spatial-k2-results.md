# harvest bjb1 32546 spatial k2 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315_result.json`
- **Structured JSON:** [`470abd3c08adec87fa53.json`](../../sessions/47/470abd3c08adec87fa53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个 K=2 Spatial 实验已完成（包括 s49 Adaptive）。

## 状态总览

| exp | mode | seed | SR | trials | 状态 |
|-----|------|------|----|--------|------|
| Adaptive τ=0.25 K=2 | adaptive_conformal_crm | 46 | **0.800** | 200 | ✅ 完成 |
| Adaptive τ=0.25 K=2 | adaptive_conformal_crm | 48 | **0.805** | 200 | ✅ 完成 |
| Adaptive τ=0.25 K=2 | adaptive_conformal_crm | 49 | **0.810** | 200 | ✅ 完成 |
| VLA-only | vla_only | 46 | **0.800** | 200 | ✅ 完成 |
| VLA-only | vla_only | 48 | **0.775** | 200 | ✅ 完成 |
| VLA-only | vla_only | 49 | **0.795** | 200 | ✅ 完成 |

**配对 Δ (Adaptive − VLA-only)**: s46: 0.000 ｜ s48: +0.030 ｜ s49: +0.015 ｜ **均值: Adaptive 0.805 vs VLA 0.790, Δ=+0.015**

## Per-task SR

任务简写：T1=between_plate_ramekin, T2=next_to_ramekin, T3=from_table_center, T4=on_cookie_box, T5=in_top_drawer, T6=on_ramekin, T7=next_to_cookie_box, T8=on_stove, T9=next_to_plate, T10=on_wooden_cabinet

**Adaptive K=2 τ=0.25**
| seed | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 |
|------|----|----|----|----|----|----|----|----|----|-----|
| 46 | 1.00 | 0.95 | 0.95 | 0.90 | 0.75 | 0.00 | 0.95 | 0.80 | 0.80 | 0.90 |
| 48 | 1.00 | 1.00 | 1.00 | 0.95 | 0.65 | 0.00 | 0.95 | 0.80 | 0.85 | 0.85 |
| 49 | 0.95 | 1.00 | 1.00 | 1.00 | 0.70 | 0.00 | 1.00 | 0.80 | 0.80 | 0.85 |

**VLA-only**
| seed | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 |
|------|----|----|----|----|----|----|----|----|----|-----|
| 46 | 0.95 | 0.95 | 1.00 | 1.00 | 0.75 | 0.00 | 0.95 | 0.80 | 0.75 | 0.85 |
| 48 | 1.00 | 0.95 | 0.95 | 0.95 | 0.70 | 0.00 | 0.95 | 0.70 | 0.75 | 0.80 |
| 49 | 1.00 | 0.95 | 1.00 | 0.95 | 0.70 | 0.00 | 1.00 | 0.75 | 0.80 | 0.80 |

## Adaptive Stats (K=2)
| seed | mean_unc | trigger_rate | tau | total_steps | crm_steps |
|------|----------|--------------|-----|-------------|-----------|
| 46 | 0.1826 | 19.06% | 0.25 | 28553 | 5442 |
| 48 | 0.1869 | 20.00% | 0.25 | 28244 | 5650 |
| 49 | 0.1878 | 19.99% | 0.25 | 28134 | 5624 |

**关键观察**：
- T6 (on_ramekin) 在所有 6 个实验里全部 0%，是 task-level 失败（与方法无关）
- Adaptive 提升主要来自 T8/T9 等中等难度任务的稳定性
- trigger_rate 均稳定在 ~20%，与 τ=0.25 设计一致
- s49 (last running on cuda:2/3) 实际已写入 JSON 并附 final overall 81.0% 行，进程已结束

---
