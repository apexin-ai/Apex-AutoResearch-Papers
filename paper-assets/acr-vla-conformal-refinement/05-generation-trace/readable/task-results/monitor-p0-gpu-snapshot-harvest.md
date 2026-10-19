# monitor p0 gpu snapshot harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_p0-gpu-snapshot-harvest_20260523T082511_result.json`
- **Structured JSON:** [`b6b1d96bf8ba27427a84.json`](../../sessions/b6/b6b1d96bf8ba27427a84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。汇总如下：

---

## bjb2-40593 状态

**eval-supp-k2mean-goal-s42: 失败** ❌
- Exit code 127: `bash: python: command not found`
- conda 环境未正确激活，脚本使用了 `python` 而非 `python3`
- 无结果 JSON 产出
- GPU 0: **完全空闲** (0%, 0 MiB / 24564 MiB)

**建议**：修复 conda 激活后重新部署 k2mean-goal-s42。该卡现在空闲，可以立即重跑。

---

## GPU 利用率快照

### bjb1-32546 (6/6 GPU 在用 ✅)
| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 24% | 1978/24564 MiB | 正常 |
| 1 | 21% | 1978/24564 MiB | 正常 |
| 2 | 24% | 1976/24564 MiB | 正常 |
| 3 | 10% | 544/24564 MiB | ⚠️ 低显存，可能是 CRM 训练进程 |
| 4 | 28% | 2072/24564 MiB | 正常 |
| 5 | 38% | 1526/24564 MiB | 正常 |

6 个 python 进程均存活。GPU 3 的 PID 668382 仅占 534 MiB，可能是 train-crm-4suite-r6（CRM 训练占用显存较小）。

### bjb2-28827 (6/6 GPU 在用 ✅)
| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 21% | 3776/24564 MiB | 正常 (obj-adapt-tau025-s42) |
| 1 | 19% | 3774/24564 MiB | 正常 (k2mean-object-s42) |
| 2 | 0% | 1888/24564 MiB | ⚠️ 瞬时 0%，进程 alive (Rl), goal-adapt-tau025-s42 |
| 3 | 30% | 3312/24564 MiB | 正常 (goal-reconvla-s42) |
| 4 | 18% | 3564/24564 MiB | 正常 (k2mean-spatial-s42) |
| 5 | 18% | 3250/24564 MiB | 正常 (goal-vla-only-s42) |

GPU 2 进程 PID 603667 状态 Rl（运行中，elapsed 1:49），利用率 0% 为采样瞬时值，正常。

### bjb2-40593 (0/1 GPU 空闲 🔴)
| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 0% | 0/24564 MiB | 空闲，k2mean-goal-s42 已失败 |

### cqa1-32758 (6/6 GPU 在用 ✅)
| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 7% | 5943/24564 MiB | k2mean_spatial_s43 |
| 1 | 0% | 6499/24564 MiB | reconvla-spatial-s43 |
| 2 | 7% | 5896/24564 MiB | k2mean_object_s43 |
| 3 | 22% | 6499/24564 MiB | reconvla-spatial-s44 |
| 4 | 0% | 5774/24564 MiB | k2mean_goal_s43 |
| 5 | 11% | 5802/24564 MiB | reconvla-goal-s43 |

全部 6 个进程 Rl+ 状态，运行约 18min-10h 不等，无异常。

---

## 已完成实验结果（今天 2026-05-23 新产出）

### bjb1-32546 — 11 个新结果

| 实验 | Success Rate |
|------|-------------|
| goal_vla_only_seed43_r4 | **0.980** |
| goal_vla_only_seed44_r4 | **0.975** |
| spatial_adaptive_conformal_crm_norm0.2_tau0.25_s42 | **0.820** |
| spatial_adaptive_conformal_crm_tau0.074855_s42 | **0.810** |
| spatial_adaptive_conformal_crm_norm0.2_tau0.15_s42 | **0.805** |
| spatial_crm_obs_only_norm0.05_s42 | **0.800** |
| spatial_adaptive_conformal_crm_norm0.2_tau0.35_s42 | **0.800** |
| spatial_crm_obs_only_norm0.1_s42 | **0.790** |
| spatial_reconvla_s42 | **0.790** |
| spatial_crm_obs_only_norm0.2_s42 | **0.790** |
| object_crm_obs_only_norm0.05_s42 | **0.770** |

### bjb2-28827 — 12 个新结果

| 实验 | Success Rate |
|------|-------------|
| goal_crm_obs_only_norm0.05_s42 | **0.855** |
| spatial_vla_only_seed43 | **0.805** |
| spatial_vla_only_seed44 | **0.805** |
| object_vla_only_seed42 | **0.790** |
| object_reconvla_seed42 | **0.790** |
| spatial_vla_only_seed42 | **0.785** |
| object_adaptive_conformal_crm_norm0.2_tau0.074855_s42 | **0.775** |
| object_vla_only_seed44 | **0.775** |
| object_vla_only_seed43 | **0.770** |
| object_crm_obs_only_seed43 | **0.535** |
| object_crm_obs_only_seed44 | **0.515** |
| object_crm_obs_only_seed42 | **0.505** |

### cqa1-32758 — 无新结果（6 个实验仍在跑）

---

## 关键发现

1. **bjb2-40593 空卡**：k2mean-goal-s42 因 `python: command not found` 失败，GPU 空闲。需修复后重跑。
2. **object_crm_obs_only 异常低**：bjb2-28827 上 3 个 seed 的 object_crm_obs_only 结果仅 0.505-0.535，远低于其他方法（~0.77-0.79），值得关注。
3. **spatial 最佳方法**：adaptive_conformal_crm (tau=0.25, norm=0.2) 在 spatial 上达到 **0.82**，优于 crm_obs_only 和 reconvla (均 0.79)。
4. **goal_vla_only r4** 结果极高 (0.975-0.98)，确认 goal benchmark 上 VLA baseline 很强。

---
