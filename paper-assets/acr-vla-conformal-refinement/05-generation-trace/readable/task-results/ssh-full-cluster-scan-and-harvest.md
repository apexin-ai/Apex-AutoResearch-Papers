# ssh full cluster scan and harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full-cluster-scan-and-harvest_20260520T054720_result.json`
- **Structured JSON:** [`179fbfc8ee5ef0bb1e71.json`](../../sessions/17/179fbfc8ee5ef0bb1e71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 个实验已更新为 DONE。以下是完整汇总：

---

## GPU 状态

| 服务器 | GPU | Util | 显存 | 实验 |
|--------|-----|------|------|------|
| **bjb2-40593** | 0 | 19% | 2.7/24G | calibrate_crm_signal.py |
| **bjb1-18228** | 0 | 0% | 0/24G | **空闲** |
| | 1 | 15% | 5.1/24G | spatial_vla_only_seed52 |
| | 2 | 22% | 5.7/24G | spatial_vla_only_seed53 |
| | 3 | 35% | 6.4/24G | long_obs_only_norm02_seed53 |
| **bjb1-32546** | 0 | 19% | 5.7/24G | spatial_vla_only_seed54 |
| | 1 | 21% | 5.0/24G | long_obs_only_norm02_seed51 |
| | 2 | 19% | 4.9/24G | long_vla_only_seed53 |
| | 3 | 34% | 6.4/24G | goal_vla_only_seed52 + long_obs_only_norm02_seed54 |
| | 4 | 19% | 4.9/24G | (进程截断未识别) |
| | 5 | 21% | 3.7/24G | (进程截断未识别) |
| **bjb2-28827** | 0 | 10% | 4.2/24G | goal_vla_only_seed50 |
| | 1 | 3% | 6.4/24G | adaptive_k_p75_seed42 (08:11 起) |
| | 2 | 0% | 0/24G | long_obs_only_norm02_seed52 |
| | 3 | 7% | 4.2/24G | goal_vla_only_seed51 |
| | 4 | 0% | 5.6/24G | goal_obs_only_norm02_seed49 |
| | 5 | 5% | 5.2/24G | goal_obs_only_norm02_seed50 |

## 已收割结果

| 实验 | SR | avg_K | fast_path% | 结论 |
|------|-----|-------|-----------|------|
| adaptive_k_p25_seed42 | 15% | 4.80 | 65.0% | success (已注册) |
| **adaptive_k_p25_seed43** | **13%** | **4.79** | **65.2%** | success |
| **adaptive_k_p25_seed44** | **15%** | **4.74** | **65.8%** | success |
| **CRM-Long seed50** | **14%** | - | - | success |
| **VLA-Long seed49** | **16%** | - | - | success (baseline) |
| **VLA-Long seed50** | **16%** | - | - | success (baseline) |
| **VLA-Long seed51** | **15%** | - | - | success (baseline) |
| **VLA-Long seed52** | **17%** | - | - | success (baseline) |
| **VLA-Goal seed49** | **65%** | - | - | success (baseline) |
| **CRM-Spatial seed51** | **36%** | - | - | success (CRM > VLA ~30%) |

## 仍在运行（14 个进程）

| 服务器:GPU | 实验 | 预计产出 |
|-----------|------|---------|
| bjb2-40593:0 | calibrate_crm_signal.py | calibration 数据 |
| bjb1-18228:1 | spatial_vla_only_seed52 | 已启动 ~30min |
| bjb1-18228:2 | spatial_vla_only_seed53 | 已启动 ~30min |
| bjb1-18228:3 | long_obs_only_norm02_seed53 | 已启动 ~30min |
| bjb1-32546:0 | spatial_vla_only_seed54 | 已启动 ~30min |
| bjb1-32546:1 | long_obs_only_norm02_seed51 | 已启动 ~1h |
| bjb1-32546:2 | long_vla_only_seed53 | 已启动 ~1h |
| bjb1-32546:3 | goal_vla_only_seed52 | 已启动 ~1h |
| bjb1-32546:3 | long_obs_only_norm02_seed54 | GPU 冲突！同 GPU3 |
| bjb2-28827:0 | goal_vla_only_seed50 | 已启动 ~50min |
| bjb2-28827:1 | adaptive_k_p75_seed42 | 运行 ~6h |
| bjb2-28827:2 | long_obs_only_norm02_seed52 | 已启动 ~35min |
| bjb2-28827:3 | goal_vla_only_seed51 | 已启动 ~50min |
| bjb2-28827:4 | goal_obs_only_norm02_seed49 | 已启动 ~30min |
| bjb2-28827:5 | goal_obs_only_norm02_seed50 | 已启动 ~30min |

## 未部署

| 实验 | 状态 |
|------|------|
| eval_long_vla_only_seed54 | Registry 中 PREPARING，未部署到任何服务器 |

## 空闲 GPU

| 服务器:GPU |
|-----------|
| **bjb1-18228:GPU0** — 完全空闲，可立即部署 |

## 注意事项

1. **GPU 冲突**: bjb1-32546 GPU3 上跑了两个实验（goal_vla_only_seed52 + long_obs_only_norm02_seed54），显存 6.4G/24G 暂未溢出，但可能互相拖慢
2. **eval_long_vla_only_seed54 未部署**: 可部署到 bjb1-18228:GPU0
3. **calibrate_crm_signal.py** 在 bjb2-40593 已运行 ~10h (598min CPU time)，单卡全占
4. **Adaptive K P25 sweep 已完成**: 3 seeds 均值 SR=14.3%, avg_K≈4.77, fast_path≈65.3%

---
