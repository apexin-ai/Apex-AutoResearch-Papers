# harvest cqa1 32758

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_cqa1-32758_20260524T032346_result.json`
- **Structured JSON:** [`2d110fcae37ff53af4f0.json`](../../sessions/2d/2d110fcae37ff53af4f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有重点实验的 registry 已是 DONE 状态，无需额外更新。汇总如下：

---

## cqa1-32758 扫描汇总

### GPU 状态
| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| 0 | 0% | 1/24564 MiB | 空闲 |
| 1 | 0% | 1/24564 MiB | 空闲 |
| 2 | 0% | 1/24564 MiB | 空闲 |
| 3 | 40% | 3710/24564 MiB | **eval-supp-long-vla-only-s46 运行中** |
| 4 | 0% | 1/24564 MiB | 空闲 |
| 5 | 0% | 1/24564 MiB | 空闲 |

### 2 个 RUNNING 实验状态
| 实验 | PID | 状态 | 说明 |
|------|-----|------|------|
| eval-supp-spatial-vla-only-s46 | 604290 | **已完成** | 进程已退出，JSON 已生成 (SR=0.805)，Registry 已为 DONE |
| eval-supp-long-vla-only-s46 | 601530 | **仍在运行** | 已跑 2h51m，当前在 STUDY_SCENE1 任务 (5/20 rollout) |

### 重点关注实验（被 cron 误标 failed → 实际均已完成）
| 实验 ID | JSON 文件 | SR | Registry 状态 |
|---------|-----------|-----|---------------|
| eval-supp-spatial-crm-norm005-s46 | eval_spatial_crm_obs_only_norm0.05_seed46.json | **0.81** | DONE/success ✓ |
| eval-supp-spatial-reconvla-s46 | eval_spatial_reconvla_seed46.json | **0.80** | DONE/success ✓ |
| eval-supp-spatial-adapt-tau025-s46 | eval_spatial_adaptive_...seed46.json | **0.80** | DONE/success ✓ |
| eval-supp-spatial-adapt-tau025-s45-r3 | eval_spatial_adaptive_...seed45.json | **0.80** | DONE/success ✓ |
| eval-supp-spatial-vla-only-s46 | eval_spatial_vla_only_seed46.json | **0.805** | DONE/success ✓ |

### 今日 (May 24) 生成的全部 JSON
| 文件名 | overall_SR | 时间 |
|--------|-----------|------|
| eval_spatial_vla_only_seed46 | 0.805 | 11:09 |
| eval_spatial_reconvla_seed46 | 0.800 | 11:01 |
| eval_spatial_crm_obs_only_norm0.05_seed46 | 0.810 | 10:59 |
| eval_spatial_adaptive_crm_...seed46 | 0.800 | 10:38 |
| eval_spatial_adaptive_crm_...seed45 | 0.800 | 09:14 |
| eval_spatial_vla_only_seed45 | 0.770 | 08:27 |
| eval_spatial_crm_obs_only_norm0.05_seed45 | 0.780 | 08:24 |
| eval_goal_k2mean_seed45 | 0.810 | 08:16 |
| eval_spatial_reconvla_seed45 | 0.795 | 08:14 |
| eval_object_reconvla_seed46 | 0.800 | 05:59 |
| eval_object_reconvla_seed45 | 0.740 | 05:57 |
| eval_object_vla_only_seed45 | 0.775 | 05:20 |
| eval_object_vla_only_seed46 | 0.765 | 05:15 |
| eval_long_crm_obs_only_norm0.05_seed44 | 0.565 | 05:11 |
| eval_long_adaptive_crm_...seed44 | 0.560 | 05:00 |
| eval_long_vla_only_seed43 | 0.595 | 02:07 |
| eval_long_vla_only_seed42 | 0.570 | 01:43 |

### 磁盘
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / | 30G | 4.9G | 26G | 17% |
| /root/autodl-tmp | 230G | 876M | 230G | 1% |

### 结论
- Registry 已全部更新到位，5 个误标实验均已修正为 DONE/success
- 唯一在跑的 eval-supp-long-vla-only-s46 预计还需 1-2 小时完成（当前在第 7/10 个 long-horizon 任务左右）
- 5 个 GPU 空闲，磁盘充裕

---
