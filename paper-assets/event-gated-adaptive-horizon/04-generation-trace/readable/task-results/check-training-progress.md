# check training progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training-progress_20260513T095021_result.json`
- **Structured JSON:** [`1d86d99e2a5ac9ff6f44.json`](../../sessions/1d/1d86d99e2a5ac9ff6f44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部收集完毕。汇总如下：

---

## 1. 进程 & GPU 状态

| | exp_001 (baseline) | exp_003 (event_gated_v2) |
|---|---|---|
| PID | 9409 | 27009 |
| GPU | cuda:0 (RTX PRO 6000) | cuda:1 (RTX PRO 6000) |
| VRAM | 4165 MiB / 97887 MiB | 4433 MiB / 97887 MiB |
| GPU Util | 19% | 12% |
| Uptime | 07:47:09 | 02:45:55 |
| Current Step | **215K** (eval) / 216K (train) | **116K** (eval) / 120K (train) |
| FPS | 8.30 | 6.52 |

---

## 2. exp_003 Gate 指标演化

| Step | gate_scale | dt_mean | dt_std | entropy | e_ratio | dt1_frac |
|------|-----------|---------|--------|---------|---------|----------|
| 5K | 0.00 | 1.00 | 0.00 | 0.000 | 0.000 | 1.000 |
| 15K | 0.00 | 1.00 | 0.00 | 0.000 | 0.000 | 1.000 |
| 25K | 0.00 | 1.00 | 0.00 | 0.000 | 0.000 | 1.000 |
| 35K | 0.00 | 1.00 | 0.00 | 0.000 | 0.000 | 1.000 |
| 45K | 0.00 | 1.00 | 0.00 | 0.000 | 0.000 | 1.000 |
| 56K | **0.06** | **4.51** | 2.25 | **2.078** | 0.999 | 0.118 |
| 66K | 0.16 | 3.66 | 1.93 | 1.961 | 0.943 | 0.156 |
| 76K | 0.26 | 3.09 | 1.67 | 1.830 | 0.880 | 0.188 |
| 86K | 0.36 | 2.83 | 1.52 | 1.727 | 0.830 | 0.205 |
| 96K | 0.46 | 2.67 | 1.43 | 1.654 | 0.795 | 0.218 |
| 106K | **0.51** | **2.57** | 1.40 | **1.612** | 0.775 | 0.235 |
| 116K | **0.61** | **2.67** | 1.46 | **1.655** | 0.796 | 0.218 |

**趋势**：gate 在 50K 开始激活（scale ramp-up），初始 dt_mean 很高 (~4.5, 近似均匀分布)，随着 gate_scale 增大逐步收敛到 ~2.6-2.7，entropy 从峰值 2.08 降至 ~1.65 并趋于稳定。dt1_frac 稳定在 ~22%，说明 gate 学会了有选择性地使用不同时间步长。

---

## 3. Eval Return 对比

| Step | Baseline | Event-Gated | 比值 |
|------|----------|-------------|------|
| 5K | 31.8 | 31.0 | 0.98 |
| 15K | 206.6 | 153.9 | 0.74 |
| 25K | 395.3 | 254.2 | 0.64 |
| 35K | 388.5 | 290.8 | 0.75 |
| 45K | 513.8 | 443.0 | 0.86 |
| 55K | 625.7 | 416.4* | 0.67 |
| 65K | 615.9 | 210.7 | 0.34 |
| 75K | 596.3 | 387.3 | 0.65 |
| 85K | 713.9 | 299.2 | 0.42 |
| 95K | 871.1 | 317.8 | 0.36 |
| 105K | 915.7 | 92.3 | 0.10 |
| 115K | 919.8 | 118.7 | 0.13 |

*gate 激活 (56K) 后 return 大幅下降，从峰值 443 跌至 ~92-119。

---

## 4. MVP 4 项标准

| # | 标准 | 状态 | 详情 |
|---|------|------|------|
| 1 | Return ≥ 80% baseline | **FAIL** | 比值 0.284 (257.6 vs 907.1) |
| 2 | Gate entropy > 0.3 nats | **PASS** | 1.655 nats |
| 3 | H_eff > 1.2× H_nominal | **PASS** | 2.667× |
| 4 | dt 时序结构 (std>0.5, autocorr>0.15) | **PASS** | std=1.456, autocorr=0.652 |

**3/4 PASS**，唯一 FAIL 是 return 标准。

---

## 5. 距离 150K Step 估算

- exp_003 当前 120K，剩余 30K steps
- FPS = 6.52 → 30000 / 6.52 ≈ **4602 秒 ≈ 1 小时 17 分钟**
- exp_001 已超过 150K（当前 216K），baseline 数据充足

**核心问题**：gate 激活后 return 崩塌严重（从 443 降到 ~100），gate_scale 的 ramp-up 速率或 gate_loss 权重可能过大，导致 agent 在适应新的 temporal abstraction 时性能无法恢复。

---
