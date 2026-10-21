# scan bjb1 32546 full harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan_bjb1-32546-full-harvest_20260523T194614_result.json`
- **Structured JSON:** [`83441cdbb64dfed221c5.json`](../../sessions/83/83441cdbb64dfed221c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

扫描完成。汇总如下：

---

## GPU 状态
| GPU | 显存占用 | 总显存 | 利用率 |
|-----|---------|--------|--------|
| 0 | 4100 MiB | 24564 MiB | 15% |

## 运行中进程
| tmux session | 实验 | 进度 |
|---|---|---|
| `eval-crm-obj-s45` | Object CRM obs_only seed45 (K=10, norm=0.05) | 正在跑 `pick_up_the_ketchup` task, rollout 10/20, 当前 8/10 成功 |

## 已完成结果（logs/ 目录，共 18 个 JSON）

| 文件 | Mode | Benchmark | SR |
|------|------|-----------|-----|
| eval_object_vla_only_pi05_seed42 | vla_only | object | **1.00** |
| eval_goal_vla_only_seed42 | vla_only | goal | **0.855** |
| eval_spatial_vla_only_seed44 | vla_only | spatial | **0.785** |
| eval_mag_obsonly_norm003 | crm_obs_only | spatial | 0.34 |
| eval_spatial_obs_only_norm02_seed44 | crm_obs_only | spatial | 0.32 |
| eval_adaptive_k_spatial_p50_seed42 | adaptive_k | spatial | 0.30 |
| eval_object_obs_only | crm_obs_only | object | 0.19 |
| eval_random_selection_object_seed43 | random_selection | object | 0.16 |
| eval_obs_only_object_norm02_seed55 | crm_obs_only | object | 0.15 |
| eval_adaptive_k_p25_seed44 | adaptive_k | object | 0.13 |
| eval_object_random_selection_seed42 | random_selection | object | 0.13 |
| eval_object_vla_only_seed44 | vla_only | object | 0.10 |
| eval_object_vla_only_seed48 | vla_only | object | 0.10 |
| eval_random_selection_object_seed48 | random_selection | object | 0.10 |
| eval_object_scalar_seed45_r2 | crm_scalar | object | 0.07 |
| eval_long_vla_only_seed42_r4 | vla_only | long | 0.00 |
| eval_pi05_baseline_object_seed42_r2 | vla_only | object | 0.00 |
| eval_object_vla_only_openvla_oft_seed42 | vla_only | object | 0.00 |

## 用户关注的 6 个实验状态

| 实验 | 文件 | 状态 |
|------|------|------|
| Long Adaptive s43 | eval_long_adaptive_conformal_crm_seed43.json | **不存在** |
| Long CRM s43 | eval_long_crm_obs_only_seed43.json | **不存在** |
| Long Reconvla s43 | eval_long_reconvla_seed43.json | **不存在** |
| Long K2mean s43 (vla_only) | eval_long_vla_only_seed43.json | **不存在** |
| Long VLA-only s44 | eval_long_vla_only_seed44.json | **不存在** |
| Object VLA-only s46 | eval_object_vla_only_seed46.json | **不存在** |

**这 6 个目标实验的结果文件在此服务器 (bjb2-40593) 上均不存在。** 当前服务器只有 1 个正在运行的实验 (Object CRM obs_only s45)，其余 18 个已完成的结果文件不包含用户关注的任何一个。这些实验可能部署在了其他服务器上。

---
