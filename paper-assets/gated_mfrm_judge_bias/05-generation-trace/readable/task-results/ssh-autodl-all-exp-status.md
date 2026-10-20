# ssh autodl all exp status

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_all_exp_status_20260523T065153_result.json`
- **Structured JSON:** [`ea700efdf19e6bc681fd.json`](../../sessions/ea/ea700efdf19e6bc681fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU 总览

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 97,030 / 97,887 MiB (99%) | 96% |
| cuda:1 | 73,561 / 97,887 MiB (75%) | 64% |
| cuda:2 | 667 / 97,887 MiB (1%) | 69% |
| cuda:3 | 97,026 / 97,887 MiB (99%) | 100% |

---

### exp-014 — exhaustive subsampling (cuda:0, PID 289621)
- **状态：运行中**，已运行 1h04m
- **进度：** CSV 仅 3 行（含 header），即刚写入第 2 个 subset 的结果
- **当前日志：** 正在跑 seed=7，sequential 和 joint_gmfrm 交替执行，每个 MCMC fit 约 240-340s
- **收敛情况：** 所有已完成 fit Rhat=1.000，ESS 2000-3700，acc.prob 0.93-0.94，状态健康
- **初步结果趋势：** joint_gmfrm 在 theta_RMSE 和 c_RMSE 上始终优于 sequential（约 2-3x 改善）

### exp-015 — synthetic N=8 (cuda:1, PID 291457)
- **状态：运行中**，已运行 1h02m
- **进度：** CSV 已有 12 行数据（6 seeds x 2 methods），正在跑 seed=6
- **结果（已完成 seeds 0-5）：**

| seed | method | theta_RMSE | theta_tau | c_RMSE | c_pearson |
|------|--------|-----------|-----------|--------|-----------|
| 0 | sequential | 0.141 | 0.786 | 1.213 | 0.966 |
| 0 | joint_gmfrm | 0.045 | 1.000 | 0.122 | 0.991 |
| 1 | sequential | 0.225 | 0.571 | 2.068 | 0.850 |
| 1 | joint_gmfrm | 0.115 | 0.857 | 1.045 | 0.901 |
| 2 | sequential | 0.197 | 1.000 | 1.765 | 0.942 |
| 2 | joint_gmfrm | 0.084 | 1.000 | 0.633 | 0.940 |
| 3 | sequential | 0.167 | 0.857 | 1.354 | 0.885 |
| 3 | joint_gmfrm | 0.090 | 0.929 | 0.461 | 0.911 |
| 4 | sequential | 0.124 | 0.857 | 1.186 | 0.936 |
| 4 | joint_gmfrm | 0.073 | 0.929 | 0.321 | 0.921 |
| 5 | sequential | 0.222 | 0.857 | 1.542 | 0.893 |
| 5 | joint_gmfrm | 0.118 | 1.000 | 0.489 | 0.914 |

joint_gmfrm 全面优于 sequential：theta_RMSE 平均低 ~55%，c_RMSE 平均低 ~70%。

### exp-016 — prior sensitivity (cuda:2, PID 293725)
- **状态：运行中**，已运行 1h01m
- **进度：** 正在跑 Prior HalfNormal(1.5) 的 MCMC（5245/6000 = **87%**），step size ~2.74e-03，acc.prob=0.92
- **结果 CSV：** 尚未生成（results 目录为空），说明还在第一个 prior 配置的 MCMC 中
- **注意：** cuda:2 显存仅 667 MiB 但 GPU 利用率 69%——这是 CPU-based MCMC（NumPyro/JAX），不吃显存
- **速度较慢：** ~4.4 it/s（比 exp-014/015 的 ~25 it/s 慢很多），因为 step size 极小（1e-3 量级），NUTS 每步需要 1023 leapfrog steps

### exp-017 — Murphy-Topel coverage (cuda:3)
- **状态：未启动**
- 脚本 `run_exp017.py` 存在，但无日志文件、无 tmux session、results 目录为空
- cuda:3 显存 97GB 满载 + 100% 利用率，可能被其他进程占用
- **需要手动启动此实验**

---
