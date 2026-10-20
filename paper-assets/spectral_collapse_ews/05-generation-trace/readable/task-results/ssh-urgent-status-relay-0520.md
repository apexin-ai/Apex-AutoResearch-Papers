# ssh urgent status relay 0520

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-status-relay-0520_20260520T025140_result.json`
- **Structured JSON:** [`096726d897b0d3872313.json`](../../sessions/09/096726d897b0d3872313.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 实验运行状态

| 实验 | PID | 状态 | GPU | 显存占用 |
|------|-----|------|-----|----------|
| **EXP011** fixed_mix r=0.2 seed42 (gen5→10 resume) | 319889 | **运行中** — 训练阶段, step 5400, loss=1.3897 | GPU 0 | 65909/97887 MiB (67%) |
| **EXP010** pure_collapse seed43 | 283142 | **运行中** — gen9 生成阶段, 6400/50000 samples | GPU 1 | 25017/97887 MiB (26%) |
| r=0.3 seed43 | — | **未启动** (脚本已就绪，等 EXP011 释放 GPU 0) | — | — |

### EXP011: fixed_mix r=0.2 seed42 — 10 gens 已完成（正在 resume 训练更多）

| gen | raw_SLV | EMA_SLV | delta_t | PPL | eff_rank | distinct_4 |
|-----|---------|---------|---------|-----|----------|------------|
| gen0 | 2366.68 | 2366.68 | — | 9.55 | 417.55 | 0.7414 |
| gen1 | 2367.46 | 2367.07 | -0.39 | 10.28 | 476.73 | 0.6737 |
| gen2 | 2358.31 | 2362.69 | **+4.38** | 10.74 | 481.62 | 0.4978 |
| gen3 | 2362.52 | 2362.61 | +0.08 | 11.14 | 486.54 | 0.4665 |
| gen4 | 2379.19 | 2370.90 | -8.29 | 11.51 | 490.35 | 0.4515 |
| gen5 | 2398.93 | 2384.92 | -14.02 | 11.83 | 492.65 | 0.4384 |
| gen6 | 2429.83 | 2407.37 | -22.46 | 12.19 | 496.42 | 0.4627 |
| gen7 | 2436.35 | 2421.86 | -14.49 | 12.54 | 496.24 | 0.4877 |
| gen8 | 2454.30 | 2438.08 | -16.22 | 12.96 | 501.49 | 0.5015 |
| gen9 | 2463.14 | 2450.61 | -12.53 | 13.39 | 504.86 | 0.5077 |

r=0.2 控制器行为：gen0→2 有短暂正 delta_t（SLV 小幅下降），gen4 起持续负 delta_t（SLV 单调上升），PPL 缓慢增长 9.55→13.39，distinct_4 先降后稳。控制器在 r=0.2 抑制了崩塌速度但未能逆转趋势。

### EXP010: pure_collapse seed43 — 9/10 gens（gen9 生成中，~13%）

| gen | raw_SLV | EMA_SLV | delta_t | PPL | eff_rank | distinct_4 |
|-----|---------|---------|---------|-----|----------|------------|
| gen0 | 2366.68 | 2366.68 | — | 9.55 | 417.55 | 0.7415 |
| gen1 | 2462.62 | 2414.65 | -47.97 | 11.37 | 490.83 | 0.5997 |
| gen2 | 2466.63 | 2440.64 | -25.99 | 13.57 | 496.24 | 0.5048 |
| gen3 | 2438.38 | 2439.51 | **+1.13** | 16.22 | 494.04 | 0.4778 |
| gen4 | 2404.60 | 2422.05 | **+17.45** | 19.94 | 489.23 | 0.4154 |
| gen5 | 2365.13 | 2393.59 | **+28.46** | 24.60 | 480.07 | 0.4172 |
| gen6 | 2325.01 | 2359.30 | **+34.29** | 30.06 | 471.88 | 0.4082 |
| gen7 | 2291.55 | 2325.42 | **+33.88** | 37.44 | 464.18 | 0.3905 |
| gen8 | 2248.26 | 2286.84 | **+38.58** | 46.94 | 456.18 | 0.3880 |

pure_collapse seed43：经典崩塌模式。SLV gen1-2 冲高后 gen3 起持续下降（delta_t 持续为正且加速），PPL 爆炸性增长 9.55→46.94，eff_rank 持续下降。gen9 预计 ~1 小时完成。

### 接力状态

- **r=0.3 seed43 启动脚本** `/root/spectral_collapse_ews/scripts/launch_mixed_r0.3_seed43.sh` 已就绪
- **阻塞条件**：EXP011 正在占用 GPU 0（65.9GB 显存），需等其完成后启动
- EXP011 当前在 step 5400（看起来是某个 gen 的训练中段），预计还需数小时

---
