# harvest server status all

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_server-status-all_20260526T010556_result.json`
- **Structured JSON:** [`f35ad324d6e967bf0724.json`](../../sessions/f3/f35ad324d6e967bf0724.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整报告：

---

## 服务器状态总览

### 1. bjb1-18228 (4 GPU)

| GPU | Util | VRAM | 实验 |
|-----|------|------|------|
| 0 | 24% | 10209/24564 MiB | π0.5 CRM obs_only, Long, s42, K=2 |
| 1 | 23% | 10209/24564 MiB | π0.5 CRM obs_only, Long, s43, K=2 |
| 2 | 21% | 10209/24564 MiB | π0.5 CRM obs_only, Long, s44, K=2 |
| 3 | 20% | 1900/24564 MiB | adaptive_conformal_crm, Goal, s45, τ=0.25 |

**空闲GPU: 0**

**最近24h产出 (9个):**
- `eval_long_crm_seed42.json`
- `eval_object_vla_only_pi05_seed42.json`
- `eval_spatial_vla_only_pi05_seed43.json`
- `eval_goal_vla_only_pi05_seed42_paired.json`
- `eval_spatial_vla_only_pi05_seed42_paired.json`
- `eval_goal_adaptive_pi05_seed42.json`
- `eval_spatial_vla_only_seed47_n20.json`
- `eval_spatial_adaptive_seed47_bjb1.json`
- `eval_object_vla_only_seed42_pi05_v2.json`

**磁盘:** / 15G avail (53%) | autodl-tmp 51G avail (80%)

---

### 2. bjb1-32546 (6 GPU)

| GPU | Util | VRAM | 实验 |
|-----|------|------|------|
| 0 | 23% | 2508/24564 MiB | Spatial τ=0.05 s42 |
| 1 | 13% | 2508/24564 MiB | Spatial τ=0.10 s42 |
| 2 | 14% | 1978/24564 MiB | Spatial τ=0.15 s42 |
| 3 | 18% | 2508/24564 MiB | Spatial τ=0.20 s42 |
| 4 | 22% | 1978/24564 MiB | Spatial τ=0.30 s42 |
| 5 | 20% | 2508/24564 MiB | Spatial τ=0.35 s42 |

**空闲GPU: 0**

**最近24h产出 (33个):** 包括大批已完成结果：
- Spatial paired r2: `eval_spatial_vla_only_seed{42,43,44}_paired_r2.json`, `eval_spatial_adaptive_k2_tau025_seed{42,43,44}_paired_r2.json`
- Spatial K2/K10 seeds: `eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed{46,48,49}.json`, `K10_seed46.json`
- Spatial VLA only: `seed{46,48,49}.json`
- CRM variants: `eval_object_crm_seed{42,43,44}.json`, `eval_goal_crm_seed{43,44}.json`, `eval_spatial_crm_seed48.json`
- π0.5 CRM: `eval_pi05_spatial_crm_seed{42,43}.json`, `eval_pi05_object_crm_seed44.json`
- π0.5 K2: `eval_object_crm_obs_only_norm0.05_seed{42,43,44}_pi05_K2.json`, `eval_spatial_crm_obs_only_norm0.05_seed44_pi05_K2.json`
- 其他: `eval_long_crm_obs_only_norm0.05_seed44.json`, `eval_goal_crm_obs_only_norm0.05_seed42.json`, `eval_goal_crm_norm005_seed44.json`

**磁盘:** / 20G avail (34%) | autodl-tmp 151G avail (40%)

---

### 3. bjb2-28827 (6 GPU)

| GPU | Util | VRAM | 实验 |
|-----|------|------|------|
| 0 | 18% | 2507/24564 MiB | Spatial τ=0.40 s42 |
| 1 | 18% | 2507/24564 MiB | Spatial τ=0.45 s42 |
| 2 | 18% | 2799/24564 MiB | Goal VLA only s45 paired_r2 |
| 3 | 19% | 2805/24564 MiB | Goal adaptive τ=0.25 s45 paired_r2 |
| 4 | 19% | 2799/24564 MiB | Goal VLA only s47 paired_r2 |
| 5 | 18% | 2805/24564 MiB | Goal adaptive τ=0.25 s47 paired_r2 |

**空闲GPU: 0**

**最近24h产出 (28个):**
- Spatial τ variants: `tau0.1_seed42`, `tau0.15_seed42`, `tau0.25_seed{45,47}`
- Goal paired: `eval_goal_vla_only_seed{45,46,47}_paired.json`, `eval_goal_adaptive_k2_tau025_seed{45,46,47}_paired.json`
- π0.5: `eval_spatial_vla_only_seed{42,43,43_v2}_pi05.json`, `eval_object_vla_only_seed{42,44}_pi05.json`, `eval_goal_vla_only_pi05_seed44.json`
- Adaptive: `eval_goal_adaptive_seed42.json`, `eval_spatial_adaptive_seed47.json`, `eval_object_adaptive_seed42.json`, `eval_long_adaptive_seed{42,44}.json`
- CRM: `eval_spatial_crm_seed47.json`, `eval_spatial_crm_obs_only_norm0.05_seed49.json`
- `eval_spatial_adaptive_seed42_pi05.json`

**磁盘:** / **4.3G avail (86%)** ⚠️ 根分区快满 | autodl-tmp 136G avail (46%)

---

### 4. cqa1-32758 (6 GPU)

| GPU | Util | VRAM | 实验 |
|-----|------|------|------|
| 0 | 15% | 5324/24564 MiB | Goal τ=0.05 s42 |
| 1 | 26% | 5324/24564 MiB | Goal τ=0.10 s42 |
| 2 | 12% | 5324/24564 MiB | Goal τ=0.15 s42 |
| 3 | 16% | 5324/24564 MiB | Goal τ=0.20 s42 |
| 4 | 29% | 5324/24564 MiB | Goal τ=0.30 s42 |
| 5 | 14% | 5324/24564 MiB | Goal τ=0.35 s42 |

**空闲GPU: 0**

**最近24h产出 (11个):**
- `eval_long_vla_only_seed48.json`
- π0.5: `eval_pi05_spatial_vla_only_seed44.json`, `eval_pi05_goal_adaptive_seed42.json`, `eval_pi05_goal_vla_only_seed42.json`, `eval_pi05_adaptive_goal_dryrun.json`
- π0.5 K2 CRM: `eval_spatial_crm_obs_only_norm0.05_seed{42,43}_pi05_K2.json`, `eval_goal_crm_obs_only_norm0.05_seed{42,43,44}_pi05_K2.json`
- `eval_spatial_vla_only_seed42_pi05.json`

**磁盘:** / 26G avail (14%) | autodl-tmp 223G avail (4%)

---

### 5. bjb2-40593 (1 GPU)

| GPU | Util | VRAM | 实验 |
|-----|------|------|------|
| 0 | 11% | 1977/24564 MiB | Long VLA only s43 v2 |

**空闲GPU: 0**

**最近24h产出 (1个):**
- `eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.075_seed42.json`

**磁盘:** / 9.7G avail (68%) | autodl-tmp 72G avail (72%)

---

## 总结

### GPU 占用
**23/23 GPU 全部在用，0空闲。** 情况与预期不同——不是只有3个实验，而是全部GPU都在跑：

| 服务器 | GPU数 | 实验类型 |
|--------|-------|---------|
| bjb1-18228 | 4/4 | 3× π0.5 CRM Long (s42-44) + 1× Goal adaptive s45 |
| bjb1-32546 | 6/6 | Spatial τ-sweep (0.05~0.35, s42) |
| bjb2-28827 | 6/6 | Spatial τ-sweep (0.40, 0.45) + Goal paired (s45, s47) |
| cqa1-32758 | 6/6 | Goal τ-sweep (0.05~0.35, s42) |
| bjb2-40593 | 1/1 | Long VLA only s43 v2 |

### 最近24h待harvest的结果总数: ~82个文件
这些结果分散在5台服务器上，主要包含：
- **π0.5 实验结果**: CRM/VLA/adaptive 多benchmark多seed
- **Spatial paired/K2/K10 results**
- **Goal paired results**
- **CRM obs_only 各benchmark**

### 异常发现
1. **bjb2-28827 根分区仅剩 4.3G (86%)** — 需要清理，否则可能影响正在运行的实验
2. GPU 3 on bjb1-18228 跑了一个额外的 Goal adaptive s45 实验（不在预期的3个之内）
3. τ-sweep 实验（Spatial 8个τ值 + Goal 6个τ值）正在全力运行中，尚未产出结果文件

---
