# analysis rssm v3 results pickup

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rssm_v3_results_pickup_20260526T055256_result.json`
- **Structured JSON:** [`81ed248febb8ac1ee215.json`](../../sessions/81/81ed248febb8ac1ee215.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析进程已完成，4 个模型全部跑完。以下是完整结果：

## Provenance

| 参数 | 值 |
|---|---|
| script_version | v3_standardized |
| seed | 42 |
| n_samples | 1000 |
| task | dmc_walker_walk |
| method | sequential_rollout |
| device | cpu |
| obs_keys | height(1), orientations(14), velocity(9) |
| timestamp | 2026-05-26T05:32:54 UTC |

## RSSM 预测误差（dt=1 vs dt=2）

| Model | Exp ID | Checkpoint | Episodes | dt_emb | dt1 obs_mse | dt2 obs_mse | **obs ratio** | dt1 reward_mae | dt2 reward_mae | **reward ratio** |
|---|---|---|---|---|---|---|---|---|---|---|
| **baseline** | exp_009d_baseline_walker_s1 | latest.pt (219MB) | 116 | No | 9.60 | 15.11 | **1.57x** | 0.0294 | 0.0458 | **1.56x** |
| **trained_dt_emb** | exp_008d_civo_trigger_s4 | latest.pt (221MB) | 112 | Yes | 25.71 | 34.60 | **1.35x** | 0.0530 | 0.0865 | **1.63x** |
| **no_dt_emb** | exp_009c_no_dt_emb_s2 | latest.pt (220MB) | 20 | No | 19.82 | 20.67 | **1.04x** | 0.0611 | 0.0789 | **1.29x** |
| **frozen_dt_emb** | exp_084_frozen_dt_emb_walker_s0 | latest.pt (221MB) | 112 | Yes | 16.33 | 24.03 | **1.47x** | 0.3482 | 0.3561 | **1.02x** |

## Per-key obs ratio（dt2/dt1）

| Model | height | orientations | velocity |
|---|---|---|---|
| baseline | 1.31x | 1.86x | 1.57x |
| trained_dt_emb | 1.44x | 2.00x | 1.35x |
| no_dt_emb | 1.03x | 1.54x | 1.04x |
| frozen_dt_emb | 1.08x | 2.06x | 1.47x |

## 关键发现

1. **obs ratio 排序**: no_dt_emb (1.04x) < trained_dt_emb (1.35x) < frozen_dt_emb (1.47x) < baseline (1.57x)
   - `trained_dt_emb` 的 obs ratio 低于 baseline，说明 dt embedding 确实让 RSSM 对不同 dt 的观测预测更稳定

2. **但 no_dt_emb 的 ratio 最低 (1.04x)**——这看起来反直觉。注意它只有 **20 episodes**（其他模型 112-116），数据量差异大，结论需谨慎

3. **绝对误差**: baseline 的绝对 obs_mse 最低（dt1=9.60, dt2=15.11），trained_dt_emb 最高（dt1=25.71, dt2=34.60）。训练了 dt embedding 的模型整体预测质量反而更差

4. **frozen_dt_emb 的 reward 异常**: reward_mae 高出其他模型一个数量级（0.348 vs 0.03-0.06），但 reward ratio 反而最低 (1.02x)——reward 预测已经很差，dt 变化不再有区分度

5. **velocity 主导误差**: 各模型的 obs_mse 主要来自 velocity 维度（占 24 维中的 9 维但贡献 >99% 误差）

---
