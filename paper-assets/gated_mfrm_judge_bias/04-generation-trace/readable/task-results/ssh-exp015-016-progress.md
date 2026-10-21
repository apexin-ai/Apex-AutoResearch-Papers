# ssh exp015 016 progress

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp015_016_progress_20260523T070355_result.json`
- **Structured JSON:** [`9cb07fa2b84060f86716.json`](../../sessions/9c/9cb07fa2b84060f86716.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### exp-015 — synthetic N=8 (PID 291457, 运行 1h15m)

**进度：7/20 seeds** (seed 0–6 完成，正在跑 seed 7 sequential)

每 seed 约 10 分钟 (240s sequential + 340s joint_gmfrm)，剩余 13 seeds ≈ **~2h 估计完成**。

当前结果（joint_gmfrm vs sequential）：

| Metric | sequential (mean) | joint_gmfrm (mean) | 胜负 |
|--------|-------------------|---------------------|------|
| θ RMSE | 0.174 | 0.084 | joint **2x better** |
| θ tau | 0.854 | 0.959 | joint wins |
| c RMSE | 1.465 | 0.520 | joint **2.8x better** |
| c pearson | 0.897 | 0.910 | joint wins |
| Rhat | 1.0 | 1.0 | both converged |
| ESS | 3103 | 3351 | comparable |

joint_gmfrm 在所有指标上一致优于 sequential，尤其 contamination 参数恢复 (c_RMSE) 提升最大。

### exp-016 — prior sensitivity (PID 316023, 运行 4m45s)

**刚重启。** 前一次运行 (PID 293733) 在 HalfNormal(1.5) warmup 22% (1340/6000) 时被 Killed (EXIT_CODE=129)。当前 PID 316023 刚启动约 5 分钟，处于数据加载阶段。无 CSV 产出。

数据概况：8 models, 176 items, 9 judges, 5661 observations, sparsity 44.7%。

### GPU 状态

| GPU | Memory | Utilization |
|-----|--------|-------------|
| 0 | 73.5 GB | 69% |
| 1 | 73.5 GB | 64% |
| 2 | 667 MB | 69% |
| 3 | 0 MB | 0% |

GPU 0,1 被其他任务占满。exp-016 (cuda:2) 内存占用低（MCMC 主要在 CPU 跑）。前次被 kill 可能与 GPU 0,1 的大任务抢资源有关，需关注。

---
