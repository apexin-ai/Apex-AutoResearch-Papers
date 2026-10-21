# ssh check mcmc status full

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-mcmc-status-full_20260525T131310_result.json`
- **Structured JSON:** [`3d1c21a9ab7a37cebf6f.json`](../../sessions/3d/3d1c21a9ab7a37cebf6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Exp-020 MCMC Phase 1 状态报告

**服务器**: autodl-8gpu  
**进程**: PID 2598 (parent, S) → PID 2605 (python, R, 99.7% CPU)  
**GPU 0**: 852 MiB (我们的进程) + 21530 MiB (PID 29577 其他任务), 99% utilization  
**日志**: `/root/gated_mfrm_judge_bias/logs/exp020_mcmc_phase1_v2.log`（注意不是 v1）

### 模型进度（4 个模型）

| 模型 | 状态 | 耗时 |
|------|------|------|
| raw_average | 完成 | 0s |
| mfrm_only | 完成 (15:55) | — |
| sequential | 完成 (18:49) | 10432s (~2h54m) |
| **joint_gmfrm** | **运行中** — warmup 54% (5409/10000) | 已跑 1h40m, 预计剩余 ~1h40m warmup + ~17m sampling |

### 收敛诊断（已完成的两个模型）— 严重问题

| 指标 | mfrm_only | sequential |
|------|-----------|------------|
| **R-hat max** | **2.9000** | **1.6700** |
| R-hat > 1.05 | 541/548 | 216/548 |
| R-hat > 1.01 | 548/548 | 441/548 |
| **ESS bulk min** | **4** | **6** |
| **ESS tail min** | **4** | **4** |
| Divergences | 0 | 0 |

**两个模型都完全没有收敛。** R-hat 远超 1.05 阈值，ESS 仅 4-6（应 >400）。4 chains × 6000 warmup + 4000 samples + target_accept=0.95 完全不够，链之间没有混合。

### 参数点估计（不可信，仅供参考）

| 文件 | shape | mean | std | min | max |
|------|-------|------|-----|-----|-----|
| mfrm_only_theta | (18,) | 0.0000 | 1.4452 | -2.8736 | 2.1636 |
| mfrm_only_b | (500,) | -0.6645 | 1.1389 | -3.5554 | 2.6527 |
| mfrm_only_d | (6,) | 0.0000 | 0.3947 | -0.5358 | 0.4230 |
| sequential_theta | (18,) | -0.0000 | 1.4837 | -2.8654 | 2.2665 |
| sequential_c | (18,) | -0.0084 | 0.0866 | -0.1098 | 0.2368 |
| sequential_b | (500,) | -0.8152 | 1.3262 | -3.8068 | 3.3267 |
| sequential_d | (6,) | -0.0000 | 0.3747 | -0.5162 | 0.3729 |

### 判断

- 0 divergences 说明不是 step size 问题，而是**链未混合**（可能是多模态后验或参数化问题）
- joint_gmfrm 复杂度更高，收敛大概率更差
- 当前结果**不可信**，需要重新检查模型参数化（reparameterization / non-centered parameterization 等）

---
