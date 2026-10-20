# status 47453 gpu audit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_47453-gpu-audit_20260516T184844_result.json`
- **Structured JSON:** [`e99c698bb9a3435f81aa.json`](../../sessions/e9/e99c698bb9a3435f81aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### GPU 占用

| GPU | PID | 进程 | 显存占用 | GPU利用率 |
|-----|-----|------|----------|-----------|
| **0** | 324550 | threshold_q07_seed42 (resume) | 75007/97887 MiB | 100% |
| **1** | 316988 | rho02_uniform_seed42 | 75007/97887 MiB | 78% |
| **2** | 326280 | batch_adaptive_tau_rho04_seed42 | 75007/97887 MiB | 99% |
| **3** | 325202 | threshold_q03_seed42 | 75007/97887 MiB | 80% |

**空闲 GPU：无。4 卡全部满载。**

---

### 各实验 step_metrics 行数 & 进度

| 实验 | step_metrics 行数 | 最新 step | 状态 |
|------|-------------------|-----------|------|
| **threshold_q07_seed42** | 24,940 | 5999 | 🔴 运行中（从 checkpoint-2000 恢复），无 final/，无 eval 结果 |
| **rho02_uniform_seed42** | 20,000 | 4999 | 🔴 运行中 |
| **threshold_q03_seed42** | 16,000 | 3999 | 🔴 运行中（wandb=offline） |
| **batch_adaptive_tau_rho04_seed42** | 16,000 | 3999 | 🔴 运行中 |
| random_reweight_seed42 | 2,000 | — | 已完成/停止（无进程） |

> step_metrics 行数 ≈ step × (batch_size 内的子记录)。6000 step 目标约 24,000 行，threshold_q07 的 24,940 行对应 step 5999，接近完成。

---

### threshold_q07 详情

- **进度**：step 5999/6000（接近完成，差最后 1 step）
- **final/ 目录**：不存在
- **eval_perplexity_results.json**：不存在
- **wandb/ 目录**：不存在（之前 no space left on device 问题后可能被清理）
- **checkpoint 目录**：checkpoint-4500, checkpoint-5000, checkpoint-5500
- **从 checkpoint-2000 恢复**，目前在 tmux session `threshold_q07_seed42` 中运行

---

### 磁盘

| 分区 | 已用 | 可用 | 占比 |
|------|------|------|------|
| / (overlay) | 24G | 7.0G | 77% |
| /root/autodl-tmp (/dev/sda2) | 21G | 813G | 3% |

根分区 77%，还可以但需关注。数据盘充裕。

---
