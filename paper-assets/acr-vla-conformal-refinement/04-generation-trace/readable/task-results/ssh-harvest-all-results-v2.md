# ssh harvest all results v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest-all-results-v2_20260520T035237_result.json`
- **Structured JSON:** [`fe8fe6f1056f9a95275e.json`](../../sessions/fe/fe8fe6f1056f9a95275e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据采集完毕。以下是全服务器实验结果汇总：

---

## 一、按 Benchmark 分组汇总

### 1. CRM-Spatial (obs_only_spatial)

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_spatial_obs_only_norm02_seed44 | 0.36 | 已注册 |
| bjb2-28827 | eval_spatial_obs_only_norm02_seed46_r2 | 0.33 | **未注册** |
| bjb2-28827 | eval_spatial_obs_only_norm02_k5_seed42 | 0.35 | 已注册 |
| bjb2-28827 | eval_spatial_obs_only_norm02_k5_seed44 | 0.37 | 已注册 |
| bjb2-28827 | eval_spatial_obs_only_norm02_k5_seed45 | 0.34 | 已注册 |
| bjb1-18228 | eval_spatial_obs_only_norm02_seed47 | 0.32 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed43_r2 | 0.34 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed45 | 0.34 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed47 | 0.32 | 已注册 |
| bjb1-32546 | eval_spatial_obs_only_norm02_seed48 | 0.35 | **未注册** |
| bjb1-32546 | eval_spatial_obs_only_norm02_k5_seed43 | 0.32 | 已注册 |
| bjb2-40593 | eval_spatial_obs_only_norm02_seed44 | 0.32 | 重复/不同seed |

### 2. VLA-only-Spatial

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_spatial_vla_only_seed44 | 0.31 | 已注册 |
| bjb1-18228 | eval_spatial_vla_only_seed43 | 0.29 | 已注册 |
| bjb1-18228 | eval_spatial_vla_only_seed50 | 0.30 | **未注册** |
| bjb1-32546 | eval_spatial_vla_only_seed42 | 0.30 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed45 | 0.27 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed46 | 0.30 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed47 | 0.30 | 已注册 |
| bjb1-32546 | eval_spatial_vla_only_seed48 | 0.30 | **未注册** |
| bjb1-32546 | eval_spatial_vla_only_seed49 | 0.29 | **未注册** |

### 3. CRM-Long (long_obs_only)

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_long_obs_only_norm02_seed42 | 0.17 | 已注册 |
| bjb2-28827 | eval_long_obs_only_norm02_seed43 | 0.15 | 已注册 |
| bjb2-28827 | eval_long_obs_only_norm02_seed44 | 0.20 | 已注册 |
| bjb2-28827 | eval_crm_long_seed47 | 0.17 | 已注册 |
| bjb1-18228 | eval_long_obs_only_norm02_seed45 | 0.18 | 已注册 |
| bjb1-18228 | eval_long_obs_only_norm02_seed46 | 0.18 | 已注册 |

### 4. VLA-only-Long

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb1-18228 | eval_long_vla_only_seed45 | 0.17 | 已注册 |
| bjb1-18228 | eval_long_vla_only_seed48 | 0.14 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed42 | 0.11 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed43 | 0.13 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed44 | 0.12 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed46 | 0.18 | 已注册 |
| bjb1-32546 | eval_long_vla_only_seed47 | 0.11 | 已注册 |

### 5. CRM-Goal / Goal-ObsOnly

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_crm_goal_seed46 | 0.72 | 已注册 |
| bjb2-28827 | eval_crm_goal_seed45_r2 | 0.65 | 已注册 |
| bjb2-28827 | eval_crm_goal_seed44_r2 | 0.64 | 已注册 |
| bjb1-18228 | eval_goal_obs_only_norm02_seed42 | 0.67 | 可能=crm-goal-seed42(已注册) |
| bjb1-18228 | eval_goal_obs_only_norm02_seed43 | 0.72 | 可能=crm-goal-seed43(已注册) |
| bjb1-32546 | eval_goal_obs_only_norm02_seed44 | 0.64 | 可能=crm-goal-seed44-r2(已注册) |
| bjb1-32546 | eval_goal_obs_only_norm02_seed45 | 0.65 | 可能=crm-goal-seed45-r2(已注册) |

### 6. VLA-only-Goal

| 服务器 | 文件名 | SR | 备注 |
|--------|--------|-----|------|
| bjb2-28827 | eval_goal_vla_only_seed44_r2 | 0.73 | 已注册 |
| bjb2-28827 | eval_goal_vla_only_seed45 | 0.63 | 已注册 |
| bjb1-32546 | eval_goal_vla_only_seed42 | 0.71 | 已注册 |
| bjb1-32546 | eval_goal_vla_only_seed43 | 0.69 | 已注册 |
| bjb1-32546 | eval_goal_vla_only_seed46 | 0.71 | 已注册 |

### 7. Adaptive-K

| 服务器 | 文件名 | SR | avg_K | fast_path | 备注 |
|--------|--------|-----|-------|-----------|------|
| bjb2-28827 | eval_adaptive_k_p25_seed43 | 0.13 | 4.788 | 0.652 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p50_seed42 | 0.16 | 3.722 | 0.785 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p75_seed42 | 0.12 | 3.070 | 0.866 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p75_seed43 | 0.13 | 3.150 | 0.856 | **未注册** |
| bjb2-28827 | eval_adaptive_k_p90_seed43 | 0.14 | 2.612 | 0.923 | 已注册 |
| bjb2-28827 | eval_adaptive_k_p90_seed44 | 0.14 | 2.579 | 0.928 | **未注册** |
| bjb1-18228 | eval_adaptive_k_p50_seed43 | 0.16 | 3.810 | 0.774 | **未注册** |
| bjb1-32546 | eval_adaptive_k_p25_seed42 | 0.15 | 4.797 | 0.650 | 已注册 |
| bjb1-32546 | eval_adaptive_k_p50_seed44 | 0.14 | 3.909 | 0.761 | 已注册 |
| bjb1-32546 | eval_adaptive_k_p75_seed44 | 0.16 | 3.022 | 0.872 | 已注册 |
| bjb1-32546 | eval_adaptive_k_p90_seed42 | 0.12 | 2.672 | 0.916 | 已注册 |

---

## 二、未注册结果汇总

| Benchmark | 文件 | SR | 服务器 |
|-----------|------|-----|--------|
| CRM-Spatial | seed46_r2 | 0.33 | bjb2-28827 |
| CRM-Spatial | seed48 | 0.35 | bjb1-32546 |
| VLA-Spatial | seed48 | 0.30 | bjb1-32546 |
| VLA-Spatial | seed49 | 0.29 | bjb1-32546 |
| VLA-Spatial | seed50 | 0.30 | bjb1-18228 |
| Adaptive-K | p25_seed43 | 0.13 | bjb2-28827 |
| Adaptive-K | p50_seed42 | 0.16 | bjb2-28827 |
| Adaptive-K | p50_seed43 | 0.16 | bjb1-18228 |
| Adaptive-K | p75_seed42 | 0.12 | bjb2-28827 |
| Adaptive-K | p75_seed43 | 0.13 | bjb2-28827 |
| Adaptive-K | p90_seed44 | 0.14 | bjb2-28827 |

**Adaptive-K P25-seed44：四台服务器均未找到此文件。**

---

## 三、关键发现

1. **CRM-Spatial** 全 seed 平均 SR ≈ 0.33-0.37 (k3) / 0.32-0.37 (k5)，一致性好
2. **VLA-only-Spatial** 平均 SR ≈ 0.29-0.31，低于 CRM-Spatial 约 5pp
3. **CRM-Long** 平均 SR ≈ 0.15-0.20
4. **VLA-only-Long** 平均 SR ≈ 0.11-0.18
5. **CRM-Goal** SR ≈ 0.64-0.72；**VLA-only-Goal** SR ≈ 0.63-0.73 — 差距小
6. **Adaptive-K** 趋势清晰：p25(avg_K≈4.8, SR≈0.14) → p50(avg_K≈3.8, SR≈0.15) → p75(avg_K≈3.1, SR≈0.14) → p90(avg_K≈2.6, SR≈0.13)，K 随 percentile 下降，SR 差异不大
7. 共 **11 个实验未注册到 registry**，以 Adaptive-K 新 seed 和 Spatial 高编号 seed 为主

---
