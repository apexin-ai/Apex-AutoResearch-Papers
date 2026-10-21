# ops harvest all servers round2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-all-servers-round2_20260519T022133_result.json`
- **Structured JSON:** [`c0e102a32fd026db4369.json`](../../sessions/c0/c0e102a32fd026db4369.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是汇总报告：

---

## 服务器: bjb2-40593

### GPU 状态
| GPU | Util% | VRAM | 运行中实验 |
|-----|-------|------|-----------|
| 0 | 99% | 15094/24564 MiB | 3 个 tmux session 排队/共享 |

### 已完成（有 JSON 结果）
| 文件名 | SR | 完成时间 |
|--------|-----|---------|
| eval_object_random_selection_seed42.json | **0.13** | May 18 20:17 |

### 仍在运行
| tmux session | 说明 |
|-------------|------|
| eval-random-selection-seed46-t16 | random selection seed46（目标实验） |
| eval-scalar-seed45-r2 | scalar seed45 |
| eval-spatial-obs-only-norm02-seq | spatial norm02 seed43/44/45 顺序执行（目标实验） |

### 空闲 GPU slot
无（1 GPU 全满）

---

## 服务器: bjb1-18228

### GPU 状态
| GPU | Util% | VRAM | 运行中实验 |
|-----|-------|------|-----------|
| 0 | 99% | 8069/24564 MiB | 运行中 |
| 1 | 99% | 7604/24564 MiB | 运行中 |
| 2 | 99% | 5742/24564 MiB | 运行中 |
| 3 | 99% | 8533/24564 MiB | 运行中 |

### 已完成（有 JSON 结果）
| 文件名 | SR | 完成时间 |
|--------|-----|---------|
| eval_object_perdof_norm02_seed45_r3.json | **0.12** | May 18 18:14 |
| eval_object_obs_only_norm01_seed48.json | **0.18** | May 18 19:39 |
| eval_object_obs_only_norm03_seed48.json | **0.16** | May 18 21:10 |
| eval_object_vla_only_seed45_r2.json | **0.11** | May 18 21:28 |
| eval_object_obs_only_norm02_seed48.json | **0.18** | May 19 00:49 |
| eval_object_perdof_default_seed43.json | **0.00** | May 19 08:49 |

### 仍在运行
| tmux session | 说明 |
|-------------|------|
| eval-obs-only-norm003-seed45-t16 | norm003 系列 |
| eval-obs-only-norm003-seed46 | norm003 系列 |
| eval-obs-only-norm003-seed47 | norm003 系列 |
| eval-obs-only-norm003-seed49-t16 | norm003 系列 |
| eval-obs-only-norm005-seed46 | norm005 系列 |
| eval-obs-only-object-norm003-seed43 | norm003 系列（object） |
| eval-perdof-norm03-seed48 | perdof norm03 |

### 空闲 GPU slot
无（4 GPU 全满）

---

## 服务器: bjb1-32546

### GPU 状态
| GPU | Util% | VRAM | 运行中实验 |
|-----|-------|------|-----------|
| 0 | 99% | 7141/24564 MiB | 运行中 |
| 1 | 99% | 10585/24564 MiB | 运行中 |
| 2 | 99% | 5775/24564 MiB | 运行中 |
| 3 | 99% | 7608/24564 MiB | 运行中 |
| 4 | 99% | 14197/24564 MiB | 运行中 |
| 5 | 83% | 6676/24564 MiB | 运行中 |

### 已完成（有 JSON 结果）
| 文件名 | SR | 完成时间 |
|--------|-----|---------|
| eval_object_perdof_norm02_seed43_bjb1-32546.json | **0.09** | May 18 18:34 |
| eval_object_perdof_norm005_seed44.json | **0.09** | May 18 20:32 |
| eval_object_obs_only_norm005_seed44.json | **0.16** | May 18 21:03 |
| eval_object_obs_only_norm01_seed46.json | **0.18** | May 18 21:17 |
| eval_object_obs_only_norm005_seed45.json | **0.14** | May 18 22:11 |
| eval_object_perdof_norm01_seed43.json | **0.12** | May 18 22:32 |
| eval_object_perdof_default_seed45.json | **0.00** | May 19 08:56 |

### 仍在运行
| tmux session | 说明 |
|-------------|------|
| eval-obs-only-default-seed48-t16 | obs-only default seed48（目标实验） |
| eval-obs-only-norm003-seed44-t16 | norm003 系列 |
| eval-obs-only-norm003-seed46-t16 | norm003 系列 |
| eval-obs-only-object-default-seed47 | obs-only default（object） |
| eval-obs-only-object-norm01-seed47 | obs-only norm01（object） |
| eval-perdof-norm003-seed48-t16 | perdof norm003（目标实验） |
| eval-perdof-norm005-seed45-t16 | perdof norm005 seed45（目标实验） |
| eval-perdof-object-norm003-seed43 | perdof norm003（object） |
| eval-perdof-object-norm005-seed43 | perdof norm005（object） |
| eval-perdof-object-norm005-seed46 | perdof norm005（object） |
| eval-perdof-object-norm01-seed48 | perdof norm01（object） |
| eval-perdof-object-norm03-seed46 | perdof norm03（object） |
| eval-scalar-object-seed46 | scalar seed46（目标实验） |
| eval-spatial-obs-only-norm02-seed45 | spatial norm02 seed45（目标实验） |

### 空闲 GPU slot
无（6 GPU 全满）

---

## 服务器: bjb2-28827

### GPU 状态
| GPU | Util% | VRAM | 运行中实验 |
|-----|-------|------|-----------|
| 0 | 99% | 7571/24564 MiB | 运行中 |
| 1 | 84% | 4813/24564 MiB | 运行中 |
| 2 | 99% | 9893/24564 MiB | 运行中 |
| 3 | 99% | 11049/24564 MiB | 运行中 |
| 4 | 99% | 7142/24564 MiB | 运行中 |
| 5 | 99% | 7140/24564 MiB | 运行中 |

### 已完成（有 JSON 结果）
| 文件名 | SR | 完成时间 |
|--------|-----|---------|
| eval_object_perdof_norm02_seed47.json | **0.11** | May 18 12:34 |
| eval_object_obs_only_norm02_k5_seed43.json | **0.19** | May 18 20:28 |
| eval_object_perdof_norm02_seed48.json | **0.07** | May 18 22:34 |
| eval_object_perdof_norm01_seed42.json | **0.11** | May 18 23:12 |
| eval_object_obs_only_norm01_seed42.json | **0.19** | May 18 23:16 |
| eval_object_random_selection_seed43.json | **0.09** | May 18 23:45 |
| eval_object_random_selection_seed44.json | **0.13** | May 19 02:00 |
| eval_object_obs_only_norm02_k5_seed44.json | **0.17** | May 19 04:49 |
| eval_object_obs_only_norm02_k5_seed45.json | **0.15** | May 19 08:38 |

### 仍在运行
| tmux session | 说明 |
|-------------|------|
| eval-obs-only-norm003-seed44-t16 | norm003 系列 |
| eval-obs-only-object-default-seed45-r2 | obs-only default（object） |
| eval-obs-only-object-default-seed48 | obs-only default（object） |
| eval-obs-only-object-norm005-seed47 | obs-only norm005（object） |
| eval-obs-only-object-norm01-seed45-r2 | obs-only norm01（object） |
| eval-perdof-norm005-seed45-t16 | perdof norm005 |
| eval-perdof-norm03-seed43-t16 | perdof norm03 |
| eval-perdof-object-default-seed47 | perdof default（object） |
| eval-perdof-object-norm003-seed46 | perdof norm003（object） |
| eval-perdof-object-norm03-seed47 | perdof norm03（object） |
| eval-random-seed46-t16 | random selection seed46（目标实验） |
| eval-random-selection-object-seed45 | random selection seed45（目标实验） |
| eval-spatial-obs-only-norm02-seed44 | spatial norm02 seed44（目标实验） |

### 空闲 GPU slot
无（6 GPU 全满）

---

## 汇总

### 新收割到的结果（共 23 个 JSON）

| 文件名 | SR | 服务器 |
|--------|-----|--------|
| eval_object_random_selection_seed42 | 0.13 | bjb2-40593 |
| eval_object_perdof_norm02_seed45_r3 | 0.12 | bjb1-18228 |
| eval_object_obs_only_norm01_seed48 | 0.18 | bjb1-18228 |
| eval_object_obs_only_norm03_seed48 | 0.16 | bjb1-18228 |
| eval_object_obs_only_norm02_seed48 | 0.18 | bjb1-18228 |
| eval_object_vla_only_seed45_r2 | 0.11 | bjb1-18228 |
| eval_object_perdof_default_seed43 | **0.00** | bjb1-18228 |
| eval_object_perdof_norm02_seed43 | 0.09 | bjb1-32546 |
| eval_object_perdof_norm005_seed44 | 0.09 | bjb1-32546 |
| eval_object_obs_only_norm005_seed44 | 0.16 | bjb1-32546 |
| eval_object_obs_only_norm01_seed46 | 0.18 | bjb1-32546 |
| eval_object_obs_only_norm005_seed45 | 0.14 | bjb1-32546 |
| eval_object_perdof_norm01_seed43 | 0.12 | bjb1-32546 |
| eval_object_perdof_default_seed45 | **0.00** | bjb1-32546 |
| eval_object_perdof_norm02_seed47 | 0.11 | bjb2-28827 |
| eval_object_obs_only_norm02_k5_seed43 | 0.19 | bjb2-28827 |
| eval_object_perdof_norm02_seed48 | 0.07 | bjb2-28827 |
| eval_object_perdof_norm01_seed42 | 0.11 | bjb2-28827 |
| eval_object_obs_only_norm01_seed42 | 0.19 | bjb2-28827 |
| eval_object_random_selection_seed43 | 0.09 | bjb2-28827 |
| eval_object_random_selection_seed44 | 0.13 | bjb2-28827 |
| eval_object_obs_only_norm02_k5_seed44 | 0.17 | bjb2-28827 |
| eval_object_obs_only_norm02_k5_seed45 | 0.15 | bjb2-28827 |

### 关注实验状态

| 实验 | 状态 | 位置 |
|------|------|------|
| spatial_obs_only_norm02_seed43 | **运行中** | bjb2-40593 (seq session) |
| spatial_obs_only_norm02_seed44 | **运行中** | bjb2-28827 |
| spatial_obs_only_norm02_seed45 | **运行中** | bjb1-32546 |
| random_selection_seed45 | **运行中** | bjb2-28827 |
| random_selection_seed46 | **运行中** | bjb2-40593 + bjb2-28827 |
| scalar_seed46 (object) | **运行中** | bjb1-32546 |
| obs_only_default_seed48 | **运行中** | bjb1-32546 |
| perdof_norm005_seed45 | **运行中** | bjb1-32546 + bjb2-28827 |
| norm003 系列 | **运行中** | bjb1-18228 (4个) + bjb1-32546 (2个) + bjb2-28827 (1个) |

### 空闲 GPU slot
**0 个**。全部 17 GPU（1+4+6+6）满载运行，共 47 个 tmux session 分布在 4 台服务器上。

### 关键发现
- `perdof_default` 两个 seed（43, 45）SR 均为 **0.00**，该配置可能有问题
- `obs_only` 系列整体表现较好（0.14-0.19），其中 `norm01` 和 `norm02` 最优
- `perdof_norm02` 表现不稳定（0.07-0.12）
- Spatial seed43/44/45 均刚部署约 30min，尚未完成

---
