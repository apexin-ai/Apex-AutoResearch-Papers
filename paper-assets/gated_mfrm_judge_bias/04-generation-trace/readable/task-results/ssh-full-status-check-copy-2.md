# ssh full status check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full_status_check_20260522T005145_result.json`
- **Structured JSON:** [`c5097156b7a7f766783a.json`](../../sessions/c5/c5097156b7a7f766783a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面状态报告

### 1. exp-012 — 运行中

- **进程**: 运行中（PID 54823，GPU 1，CPU 105%，已运行 ~114 分钟）
- **CSV**: 37 行（1 header + 36 数据行）
- **列**: `sigma, seed, theta_rmse, theta_tau, cn_rmse, cn_corr, r_hat, ess`
- **summary.csv**: 不存在（实验未结束）
- **预估**: 具体总行数取决于 sigma 级数 × seed 数，进程仍在跑

### 2. exp-009 — Part A 运行中，Part B 未开始

- **进程**: 运行中（PID 70789，GPU 0，tmux session `exp-009`，已运行 ~79 分钟）
- **Part A** (`bias_vs_rho.csv`): 21 行（1 header + 20 数据行）。目标 800 行，完成 **2.5%**
- **Part B** (`cn_recovery.csv`): **不存在**，尚未开始
- **日志进度**: `[13/400] rho=0.0 seed=12 | 4213s | ETA 125424s`（~35 小时 ETA）
- **警告**: MCMC 链在 CPU 上串行执行（仅 1 设备），4 chains 顺序跑，速度受限

### 3. Llama 下载 — 进行中，部分超时

- **进程**: 运行中（PID 89309，~37 分钟）
- **已下载**: 23GB / ~35GB（5/17 文件完成，29%）
- **缺失分片**: model-00002, 00004, 00008, 00009 尚未下载
- **问题**: model-00002 下载超时（`The read operation timed out`），正在重试
- **风险**: HF 未认证下载（`unauthenticated requests`），限速可能导致持续超时

### 4. 跳过

### 5. nvidia-smi

| GPU | 型号 | 显存占用 | GPU利用率 | 温度 | 进程 |
|-----|------|---------|----------|------|------|
| 0 | RTX PRO 6000 Blackwell (96GB) | 73.6G / 96G | 67% | 40°C | exp-009 (PID 70789) |
| 1 | RTX PRO 6000 Blackwell (96GB) | 73.6G / 96G | 65% | 42°C | exp-012 (PID 54823) |
| 2 | RTX PRO 6000 Blackwell (96GB) | 0 / 96G | 0% | 31°C | 空闲 |
| 3 | RTX PRO 6000 Blackwell (96GB) | 0 / 96G | 0% | 31°C | 空闲 |

### 6. 磁盘空间

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/`（系统） | 30G | 9.6G | 21G | 32% |
| `/root/autodl-tmp`（数据盘） | 250G | 36G | 215G | 15% |

---

**要点汇总**:
- GPU 0/1 被 exp-009/012 占用，GPU 2/3 空闲可用
- exp-009 ETA ~35h，瓶颈是 MCMC 4链串行跑 CPU
- Llama 下载遇到超时在重试，建议关注是否需要设 HF_TOKEN 提速
- 磁盘充裕，Llama 下载完成后数据盘约用 ~50G/250G

---
