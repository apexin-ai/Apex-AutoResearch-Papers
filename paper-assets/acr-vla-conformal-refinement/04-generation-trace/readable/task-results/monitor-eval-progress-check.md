# monitor eval progress check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_eval-progress-check_20260514T072245_result.json`
- **Structured JSON:** [`162db56c0c3f776bbe1f.json`](../../sessions/16/162db56c0c3f776bbe1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总如下：

## 实验进度汇总

| exp_id | mode | K | tasks_done/10 | current_task | interim_SR | est_remaining |
|--------|------|---|---------------|--------------|-----------|---------------|
| eval-k5-spatial | ACR-VLA | 5 | **5/10** | Task 6 (starting) | 26.0% (13/50) | ~5-6h |
| eval-acr-spatial-v2 | ACR-VLA | 10 | **6/10** | Task 7 (starting) | 23.3% (14/60) | ~7-8h |
| eval-reconvla-spatial-v3 | SampleConsensus | 10 | **7/10** | Task 8 (starting) | **42.9% (30/70)** | ~5h |
| eval-scalar-unc-spatial | scalar CRM | 10 | **4.5/10** | Task 5 (rollout 5/10, 0/5) | 35.0% (14/40) | ~10-11h |
| eval-vla-mean-spatial | VLA mean | 10 | **2.5/10** | Task 3 (rollout 5/10, 0/5) | 85.0%\* (17/20) | ~24h |

\* VLA mean 的 85% 严重虚高——只完成了最简单的 2 个 task (next_to_ramekin 100%, between_plate_ramekin 70%)，后续难 task 会大幅拉低。

## 各实验已完成 task 明细

### eval-k5-spatial (ACR-VLA K=5)
| Task | Success |
|------|---------|
| bowl_between_plate_ramekin | 50% (5/10) |
| bowl_next_to_ramekin | 70% (7/10) |
| bowl_from_table_center | 0% (0/10) |
| bowl_on_cookie_box | 10% (1/10) |
| bowl_in_top_drawer | 0% (0/10) |

### eval-acr-spatial-v2 (ACR-VLA K=10)
| Task | Success |
|------|---------|
| bowl_between_plate_ramekin | 40% (4/10) |
| bowl_next_to_ramekin | 70% (7/10) |
| bowl_from_table_center | 0% (0/10) |
| bowl_on_cookie_box | 30% (3/10) |
| bowl_in_top_drawer | 0% (0/10) |
| bowl_on_ramekin | 0% (0/10) |

### eval-reconvla-spatial-v3 (SampleConsensus K=10) — 领先
| Task | Success |
|------|---------|
| bowl_between_plate_ramekin | 60% (6/10) |
| bowl_next_to_ramekin | **100% (10/10)** |
| bowl_from_table_center | 0% (0/10) |
| bowl_on_cookie_box | 30% (3/10) |
| bowl_in_top_drawer | 10% (1/10) |
| bowl_on_ramekin | 10% (1/10) |
| bowl_next_to_cookie_box | **90% (9/10)** |

### eval-scalar-unc-spatial (scalar CRM K=10)
| Task | Success |
|------|---------|
| bowl_between_plate_ramekin | 50% (5/10) |
| bowl_next_to_ramekin | 50% (5/10) |
| bowl_from_table_center | 10% (1/10) |
| bowl_on_cookie_box | 30% (3/10) |
| *bowl_in_top_drawer (running)* | *0/5 at rollout 5* |

### eval-vla-mean-spatial (VLA mean K=10)
| Task | Success |
|------|---------|
| bowl_between_plate_ramekin | 70% (7/10) |
| bowl_next_to_ramekin | **100% (10/10)** |
| *bowl_from_table_center (running)* | *0/5 at rollout 5* |

## 关键发现

**vs baseline 30%：**
- **SampleConsensus (reconvla) 42.9% 显著超越 baseline**，在简单 task 上有 90-100% 的高分，且在难 task 上也有 10% 的非零表现
- **Scalar CRM 35.0% 略高于 baseline**，但 next_to_ramekin 只有 50%（其他方法 70-100%），说明 scalar 置信度校准不如 conformal
- **ACR-VLA K=10 (23.3%) 和 K=5 (26.0%) 均低于 baseline**，令人意外——K=10 反而比 K=5 更低，可能 CRM 在 K=10 时过度筛选导致选到差样本

**跨方法一致模式：**
- `bowl_from_table_center` 和 `bowl_in_top_drawer` 对所有方法都是 0-10%（本身就是极难 task）
- `bowl_next_to_ramekin` 是最容易的 task（50%-100%），方法间差异最大的也在这里

**eval-reconvla-spatial-v3 进展最快**（7/10），预计还需 ~5h 完成。eval-vla-mean-spatial 最慢（2.5/10），预计还需 ~24h，需要关注 bjb2 机器是否撑得住。

---
