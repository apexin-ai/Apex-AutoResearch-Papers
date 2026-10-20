# analysis eval analyzing batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-analyzing-batch_20260515T230306_result.json`
- **Structured JSON:** [`de410b1c898923ef96ba.json`](../../sessions/de/de410b1c898923ef96ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验 registry 已更新为 DONE(success) + metrics。

---

## 汇总报告

### 1. 实验 1: 1.5B Qwen2.5 s123 para_aligned eval batch

| Dosage | MMLU | GSM8K | ARC-Challenge | HumanEval |
|--------|------|-------|---------------|-----------|
| d000 | 0.6111 | 0.5921 | 0.7547 | 0.1538 |
| d005 | 0.6140 | 0.5439 | 0.7475 | 0.0769 |
| d025 | 0.6145 | 0.5482 | 0.7504 | 0.1923 |
| d100 | **0.6290** | 0.5307 | **0.7834** | **0.2308** |

d100 在 MMLU/ARC/HumanEval 上明显高于 d000，但 GSM8K 反而下降 (0.5921→0.5307)。HumanEval 样本量太小 (n=26) 波动大。

### 2. 实验 2: 3B d005 s123 GSM8K rerun

- **GSM8K exact_match: 0.6308** (832/1319)

### 3. Extreme gamma sweep

**已完成** (11.1h, 8 conditions)。结果写入 `exp004_sim_sweep/results_extreme_gamma/sweep_summary.json`。

| Condition | γ_bias | γ_RMSE | CI95% | θ_corr |
|-----------|--------|--------|-------|--------|
| g2.0_auc0.7_n20 | 0.0337 | 0.1163 | 1.000 | 0.9560 |
| g2.0_auc0.7_n50 | 0.0178 | 0.0944 | 1.000 | 0.9484 |
| g2.0_auc0.9_n20 | 0.0048 | 0.0907 | 1.000 | 0.9688 |
| g2.0_auc0.9_n50 | 0.0109 | 0.1013 | 1.000 | 0.9616 |
| g4.0_auc0.7_n20 | **-0.2286** | **0.2946** | 0.900 | 0.9193 |
| g4.0_auc0.7_n50 | -0.0958 | 0.1867 | 0.900 | 0.9147 |
| g4.0_auc0.9_n20 | -0.1365 | 0.2431 | 1.000 | 0.9610 |
| g4.0_auc0.9_n50 | 0.0358 | 0.1811 | 0.900 | 0.9483 |

γ=2.0 recovery 良好；γ=4.0 出现负 bias 和更大 RMSE，尤其低 AUC+小 n 时 CI 覆盖率降到 0.90。

### 4. GPU 状态

| GPU | 显存占用 | Util | 状态 |
|-----|---------|------|------|
| cuda:0 | 23258/24564 MiB | 99% | BUSY (PID 642763, 643167) |
| cuda:1 | 13341/24564 MiB | 86% | BUSY (PID 628668) |
| **cuda:2** | **0/24564 MiB** | **0%** | **IDLE** |
| cuda:3 | 7803/24564 MiB | 73% | BUSY (PID 630891) |
| cuda:4 | 7535/24564 MiB | 57% | BUSY (PID 648627) |
| cuda:5 | 18665/24564 MiB | 29% | BUSY (PID 633041) |

**cuda:2 空闲，cuda:3 有活跃进程**。

---
