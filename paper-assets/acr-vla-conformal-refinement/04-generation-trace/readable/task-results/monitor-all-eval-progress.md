# monitor all eval progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_all-eval-progress_20260514T071455_result.json`
- **Structured JSON:** [`f175163db384d57622d8.json`](../../sessions/f1/f175163db384d57622d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 5 个进程均在运行，无需手动处理。** 汇总如下：

## 进度总览

| # | 实验 | 服务器 | 模式 | 运行时间 | 完成 tasks | 当前进度 | 预估剩余 |
|---|------|--------|------|----------|-----------|---------|---------|
| 1 | eval-acr-spatial-v2 | bjb1 cuda:1 | acr_vla K=10 | 7h32m | 6/10 | 跑 T7 | ~5h |
| 2 | eval-reconvla-spatial-v3 | bjb1 cuda:2 | reconvla K=10 | 7h32m | 7/10 | 跑 T8 | ~3.2h |
| 3 | eval-scalar-unc-spatial | bjb1 cuda:3 | crm_scalar K=10 | 4h53m | 4/10 | 跑 T5 | ~7.4h |
| 4 | eval-k5-spatial | bjb1 cuda:0 | acr_vla K=5 | 3h02m | 5/10 | 跑 T6 | ~3h |
| 5 | eval-vla-mean-spatial | bjb2 cuda:0 | vla_only mean K=10 | 4h06m | 2/10 (T3 半程) | T3 rollout 5/10 | ~12h |

## 逐 Task 成功率

Task 简写：T1=between_plate_ramekin, T2=next_to_ramekin, T3=from_table_center, T4=on_cookie_box, T5=in_top_drawer, T6=on_ramekin, T7=next_to_cookie_box

| Task | acr_vla K=10 | reconvla K=10 | crm_scalar K=10 | acr_vla K=5 | vla_only mean K=10 |
|------|-------------|---------------|-----------------|-------------|-------------------|
| T1 between_plate_ramekin | **40%** (4/10) | **60%** (6/10) | **50%** (5/10) | **50%** (5/10) | **70%** (7/10) |
| T2 next_to_ramekin | **70%** (7/10) | **100%** (10/10) | **50%** (5/10) | **70%** (7/10) | **100%** (10/10) |
| T3 from_table_center | **0%** (0/10) | **0%** (0/10) | **10%** (1/10) | **0%** (0/10) | running |
| T4 on_cookie_box | **30%** (3/10) | **30%** (3/10) | **30%** (3/10) | **10%** (1/10) | - |
| T5 in_top_drawer | **0%** (0/10) | **10%** (1/10) | - | **0%** (0/10) | - |
| T6 on_ramekin | **0%** (0/10) | **10%** (1/10) | - | - | - |
| T7 next_to_cookie_box | - | **90%** (9/10) | - | - | - |
| T8-T10 | - | - | - | - | - |
| **已完成均值** | **23.3%** | **42.9%** | **35.0%** | **26.0%** | **85.0%** (仅2任务) |

## 初步观察

- **T3 (from_table_center)** 所有方法近乎 0%，是最难的 task
- **T2 (next_to_ramekin)** 表现最好，reconvla 和 vla_only 均达 100%
- **reconvla** 目前均值领先其他 CRM 方法（42.9% vs 23-35%）
- **vla_only mean** 前 2 个 task 均值 85%，但样本太少，后续 hard task 会拉低
- **bjb2 单卡** 速度约 2h/task，是 bjb1 的 ~1.6x 慢，预计还需 ~12h 完成
- **K=5 vs K=10**（acr_vla）：K=5 在 T4 上明显更差（10% vs 30%），其他差异不大

---
