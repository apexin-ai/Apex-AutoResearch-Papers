# scan cqa1 gpu check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan_cqa1-gpu-check_20260523T173649_result.json`
- **Structured JSON:** [`c5aad8030a43869b4a93.json`](../../sessions/c5/c5aad8030a43869b4a93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-32758 状态汇总

### GPU 使用情况（全部 6 个 GPU 满载）

| GPU | 显存占用 | 实验 | 进度 |
|-----|---------|------|------|
| **cuda:0** | 6549/24564 MiB | `long_k2mean_s44` (vla_only, K=2 mean, seed44) | **刚启动**（01:27创建，还没完成任何 task） |
| **cuda:1** | 3714/24564 MiB | `eval-supp-long-adapt-tau025-s44` (adaptive_conformal_crm, τ=0.25, seed44) | **task 6/10** 进行中 |
| **cuda:2** | 2131/24564 MiB | `eval-supp-long-vla-only-s43` (vla_only, seed43) | **task 9/10** 完成，正在跑最后 1 个 task |
| **cuda:3** | 6577/24564 MiB | `long_reconvla_s44` (reconvla, K=10, seed44) | **刚启动**（01:27创建） |
| **cuda:4** | 2135/24564 MiB | `eval-supp-long-k2mean-s42` (vla_only, K=2 mean, seed42) | **task 9/10** 完成，正在跑最后 1 个 task |
| **cuda:5** | 3776/24564 MiB | `eval-supp-long-crm-norm005-s44` (crm_obs_only, norm=0.05, K=10, seed44) | **task 6/10** 进行中 |

**没有空闲 GPU。** cuda:0 和 cuda:3 在 01:27 新启动了实验。

### 当前运行中实验的部分结果（long benchmark, 已完成 task 的 SR）

**k2mean-s42** (9/10 完成):
`25% | 85% | 100% | 95% | 35% | 90% | 15% | 60% | 0%` → 当前均值 ≈ **50.6%**

**vla-only-s43** (9/10 完成):
`25% | 80% | 100% | 95% | 40% | 85% | 25% | 70% | 10%` → 当前均值 ≈ **58.9%**

**adapt-tau025-s44** (5/10 完成):
`25% | 75% | 95% | 90% | 25%` → 当前均值 ≈ **62.0%**

**crm-norm005-s44** (5/10 完成):
`20% | 80% | 90% | 100% | 40%` → 当前均值 ≈ **66.0%**

### 今日已完成的结果文件（已保存 JSON）

| 时间 | SR | Benchmark | Mode | 文件 |
|------|-----|-----------|------|------|
| 22:57 | **76.0%** | object | reconvla(single) | eval_object_reconvla_seed44 |
| 22:56 | **75.0%** | object | vla_only(mean) | eval_object_vla_only_seed44 |
| 22:34 | **79.0%** | spatial | vla_only(single) | eval_spatial_vla_only_seed43 |
| 22:22 | **81.0%** | spatial | vla_only(mean) | eval_spatial_vla_only_seed44 |
| 19:50 | **78.0%** | object | vla_only(mean) | eval_k2mean_object_seed43 |
| 19:28 | **81.0%** | goal | reconvla(single) | eval_goal_reconvla_seed43 |
| 19:22 | **78.0%** | spatial | vla_only(mean) | eval_k2mean_spatial_seed43 |
| 19:21 | **79.5%** | spatial | reconvla(single) | eval_spatial_reconvla_seed44 |
| 19:18 | **81.5%** | spatial | reconvla(single) | eval_spatial_reconvla_seed43 |
| 19:17 | **81.5%** | goal | vla_only(mean) | eval_k2mean_goal_seed43 |

cuda:2 和 cuda:4 的实验（vla-only-s43、k2mean-s42）预计很快完成（还剩最后 1 个 task）。

---
