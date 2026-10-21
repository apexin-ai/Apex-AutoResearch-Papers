# ssh exp018 017 status check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp018_017_status_check_20260523T110651_result.json`
- **Structured JSON:** [`25ef84008ea2a039abed.json`](../../sessions/25/25ef84008ea2a039abed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### exp-018 — 仍在运行，未完成

- **进程**: PID 345307, 104% CPU, 已运行 137 分钟，tmux session `exp018` 存在
- **进度**: CSV 有 **16/20 seeds**（seed 0-15）。日志显示 `[17/20] seed=16` 的 sequential 已完成，正在跑 joint_gmfrm
- **GPU 2**: 0% 利用率, 73615 MiB 显存占用（MCMC 采样阶段 CPU 密集）
- **ETA**: 剩余 4 seeds × ~8 min/seed ≈ **30-35 分钟**完成

CSV 目前的内容（16 seeds × 2 methods = 32 行）：

| 指标 | sequential (mean) | joint_gmfrm (mean) |
|------|-------------------|---------------------|
| theta_RMSE | 0.171 | 0.091 |
| theta_tau | 0.894 | 0.949 |
| c_RMSE | 1.334 | 0.612 |
| c_pearson | 0.835 | 0.869 |
| R_hat | 1.008 | 1.003 |
| ESS | 640 | 1081 |

joint_gmfrm 在所有指标上都优于 sequential（theta_RMSE 降低 47%，c_RMSE 降低 54%）。Wilcoxon 统计还没输出（需等 20 seeds 全部跑完）。

---

### exp-017 — 仍在运行，进度较慢

- **进程**: PID 318082, 103% CPU, 已运行 **4 小时 3 分钟**, state=R
- **进度**: **49/800 fits** 完成（6.1%），当前在 n_models=8, seed≈48
- **GPU 0**: 69% 利用率, 73615 MiB 显存
- **ETA**: 按当前速率（~5 min/fit），剩余 751 fits ≈ **62-65 小时**

---

### GPU 总览

| GPU | 利用率 | 显存 | 用途 |
|-----|--------|------|------|
| 0 | 69% | 73615 MiB | exp-017 |
| 1 | 0% | 0 MiB | 空闲 |
| 2 | 0% | 73615 MiB | exp-018 (CPU phase) |
| 3 | 0% | 0 MiB | 空闲 |

---
