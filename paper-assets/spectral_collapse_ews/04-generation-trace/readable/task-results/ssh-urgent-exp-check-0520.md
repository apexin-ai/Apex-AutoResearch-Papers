# ssh urgent exp check 0520

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-exp-check-0520_20260520T003110_result.json`
- **Structured JSON:** [`6f3da24db7441a8afb03.json`](../../sessions/6f/6f3da24db7441a8afb03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

### 进程状态
| 实验 | PID | 运行时间 | 状态 |
|------|-----|----------|------|
| exp_011 (fixed_mix r=0.2, seed42) | 319889 | 8h13m | **RUNNING** |
| exp_010 (pure_collapse, seed43) | 283142 | 18h39m | **RUNNING** |

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 97% | 65909/97887 MiB |
| cuda:1 | 92% | 25017/97887 MiB |

### 日志尾部
- **exp_011**: 训练中，Step 1700, avg_loss=1.3840（仍在当前 gen 训练阶段）
- **exp_010**: 生成中，11840/50000 samples（仍在当前 gen 生成阶段）

---

### exp_011 — fixed_mix r=0.2, seed42 (9 gens completed, still running)

| Gen | raw SLV | EMA SLV | Δ_t |
|-----|---------|---------|-----|
| 0 | 2366.68 | 2366.68 | --- |
| 1 | 2367.46 | 2367.07 | -0.000164 |
| 2 | 2358.31 | 2362.69 | **+0.001852** |
| 3 | 2362.52 | 2362.61 | +0.000035 |
| 4 | 2379.19 | 2370.90 | -0.003504 |
| 5 | 2398.93 | 2384.92 | -0.005923 |
| 6 | 2429.83 | 2407.37 | -0.009488 |
| 7 | 2436.35 | 2421.86 | -0.006122 |
| 8 | 2454.30 | 2438.08 | -0.006854 |

- **EMA non-decreasing from Gen 4 onward**
- Final SLV: 2454.30 (baseline: 2366.68, **+3.70%**)
- max Δ_t = **+0.001852 at Gen 2**（唯一显著正值，Gen 2-3 有微弱 collapse signal 后 SLV 反弹上升）
- Gen 4 起 Δ_t 全为负值 → controller 完全沉默，SLV 持续上升（r=0.2 的 real data 混入推动 diversity 增长）

---

### exp_010 — pure_collapse, seed43 (8 gens completed, still running)

| Gen | raw SLV | EMA SLV | Δ_t |
|-----|---------|---------|-----|
| 0 | 2366.68 | 2366.68 | --- |
| 1 | 2462.62 | 2414.65 | -0.020268 |
| 2 | 2466.63 | 2440.64 | -0.010981 |
| 3 | 2438.38 | 2439.51 | **+0.000478** |
| 4 | 2404.60 | 2422.05 | **+0.007375** |
| 5 | 2365.13 | 2393.59 | **+0.012025** |
| 6 | 2325.01 | 2359.30 | **+0.014490** |
| 7 | 2291.55 | 2325.42 | **+0.014314** |

- **No sustained EMA non-decreasing segment** — EMA 从 Gen 2 peak 后持续下降
- Final SLV: 2291.55 (baseline: 2366.68, **-3.17%**)
- max Δ_t = **+0.014490 at Gen 6**
- Gen 3 起 Δ_t 持续为正且递增 → **强烈 collapse signal**，controller 应在 Gen 3-4 区间触发
- PPL 从 9.55 爆涨到 37.44（近 4x），distinct4 从 0.74 降至 0.39 — 典型 model collapse 轨迹

---

### 关键对比

| 指标 | exp_011 (r=0.2) | exp_010 (pure) |
|------|-----------------|----------------|
| SLV 方向 | ↑ +3.70% | ↓ -3.17% |
| max Δ_t | +0.0019 (Gen 2) | +0.0145 (Gen 6) |
| Collapse signal | 微弱，仅 Gen 2-3 | 强烈，Gen 3 起持续 |
| PPL 变化 | 9.55 → 12.96 | 9.55 → 37.44 |

两个实验均仍在运行，exp_010 目前在 Gen 8 生成阶段（11840/50000），exp_011 在某个 gen 的训练阶段（Step 1700）。两块 GPU 都在满负载，无法启动 seed44。

---
