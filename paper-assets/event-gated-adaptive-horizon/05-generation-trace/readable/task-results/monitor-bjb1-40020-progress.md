# monitor bjb1 40020 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb1-40020-progress_20260519T202550_result.json`
- **Structured JSON:** [`77adfcc86d1a44b5aea3.json`](../../sessions/77/77adfcc86d1a44b5aea3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-40020 Status

### GPU
| GPU | Temp | Power | Memory | Util |
|-----|------|-------|--------|------|
| 0 (RTX 4090) | 42°C | 145W/450W | 7122MiB / 24564MiB (29%) | 69% |
| 1 (RTX 4090) | 45°C | 137W/450W | 5040MiB / 24564MiB (21%) | 75% |

6 个 python 进程分布在 2 张卡上，显存余量充足。

### tmux sessions
```
exp_025_s1: 1 windows (created Wed May 20 01:07:28 2026)
exp_025_s2: 1 windows (created Wed May 20 01:07:34 2026)
exp_026_s0: 1 windows (created Wed May 20 04:20:47 2026)
exp_026_s1: 1 windows (created Wed May 20 04:20:49 2026)
```
4 个 session 全部存活。

### exp_025_obs_sgs_walker_s1
- Current step: **88000 / 210000** (42%)
- Latest eval_return: **490.87** (step 85K, 前值 521.96@75K → 略回落)
- Latest value_mean: **315.11** (step 85K)
- ve_ratio: **0.642** (315.11 / 490.87)
- NVE status: **healthy** — ve_ratio 在合理范围，eval_return 稳步上升

### exp_025_obs_sgs_walker_s2
- Current step: **85000 / 210000** (40%)
- Latest eval_return: **312.44** (step 85K, 持续上升中)
- Latest value_mean: **226.33** (step 85K)
- ve_ratio: **0.724** (226.33 / 312.44)
- NVE status: **healthy** — ve_ratio 健康，eval_return 单调递增

### exp_026_obs_sgs_cheetah_s0
- Current step: **5000 / 105000** (5%)
- Latest eval_return: **8.26** (step 5K)
- Latest value_mean: **0.00076**
- Early signal: **on track** — 刚启动，ve_ratio 接近 0 是正常的（value function 尚未学到）

### exp_026_obs_sgs_cheetah_s1
- Current step: **5000 / 105000** (5%)
- Latest eval_return: **13.64** (step 5K)
- Latest value_mean: **0.00077**
- Early signal: **on track** — 同上，s1 初始 return 略高于 s0

**总结**: 4 个实验全部正常运行。exp_025 两个 seed 在 85-88K 步，进度约 40%；exp_026 两个 seed 刚起步约 5K。GPU 显存和温度均无压力。

---
