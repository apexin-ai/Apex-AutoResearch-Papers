# ssh urgent all status check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_all_status_check_20260523T070644_result.json`
- **Structured JSON:** [`9aa1971043b35dd75cc9.json`](../../sessions/9a/9aa1971043b35dd75cc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全量状态汇报

---

### 命令 1 — `tail -50 ~/runs/gated_mfrm_judge_bias/exp-017.log`

```
  Deduped /root/gated_mfrm_judge_bias/exp017/results/coverage_simulation.csv: 12 -> 7 rows
Coverage Simulation: 7 done, 793 remaining
N_models: [8, 20, 50, 100], seeds: 200
I=176, J=9, rho=0.6
MCMC: chains=4, warmup=2000, samples=4000, target_accept=0.95

  [8/800] N=  8 seed=  7 | 0s | ETA 0s   /root/gated_mfrm_judge_bias/exp017/run_exp017.py:107: UserWarning: There are not enough devices to run parallel chains: expected 4 but got 1. Chains will be drawn sequentially. If you are running MCMC in CPU, consider using `numpyro.set_host_device_count(4)` at the beginning of your program. You can double-check how many devices are available in your system using `jax.local_device_count()`.
  mcmc = MCMC(kernel, num_warmup=2000, num_samples=4000, num_chains=4,
```

**状态：运行中。** 800 个任务已完成 7 个（~1%），当前在 seed=7, N=8。有 warning 提示 4 chains 只能串行跑（单 GPU）。

---

### 命令 2 — `ls -la` 结果目录

`~/runs/gated_mfrm_judge_bias/exp-017*/` 路径不存在。实际结果在 `/root/gated_mfrm_judge_bias/exp017/results/`：

```
total 4
drwxr-xr-x 2 root root  45 May 23 14:56 .
drwxr-xr-x 4 root root  77 May 23 15:03 ..
-rw-r--r-- 1 root root 668 May 23 15:04 coverage_simulation.csv
```

只有一个文件 `coverage_simulation.csv`（668 bytes）。

---

### 命令 3 — `ps aux | grep exp.017`

三个实验都在运行：

| 实验 | PID | GPU | CPU% | MEM(RSS) | 启动时间 | 状态 |
|------|-----|-----|------|----------|----------|------|
| **exp-015** | 291466 | CUDA:1 | 103% | ~7.1GB | 13:49 | `Rl` (运行中) |
| **exp-016** | 316023 | CUDA:2 | 104% | ~1.7GB | 14:59 | `Rl` (运行中) |
| **exp-017** | 318082 | CUDA:0 | 112% | ~4.2GB | 15:04 | `Rl` (运行中) |

另有 tmux session `orchestrator2` 在跑 exp001 的 `run_remaining.sh`（PID 110804，自 May22 起）。

---

### 命令 4 — `tail -5 ~/runs/gated_mfrm_judge_bias/exp-015.log`

```
  sequential: theta_RMSE=0.1440 tau=0.9286 c_RMSE=1.1241 c_r=0.8063 Rhat=1.000 ESS=3391 237s
  joint_gmfrm: theta_RMSE=0.0623 tau=1.0000 c_RMSE=0.5691 c_r=0.7962 Rhat=1.000 ESS=3501 346s
  flushed 2 rows
[8/20] seed=7
  sequential: theta_RMSE=0.0777 tau=1.0000 c_RMSE=1.3410 c_r=0.4437 Rhat=1.000 ESS=3480 277s
```

**状态：运行中。** 20 个任务进行到第 8 个（seed=7），sequential 方法刚完成。

---

### 命令 5 — `tail -5 ~/runs/gated_mfrm_judge_bias/exp-016.log`

输出极长（被截断，含 >2M 字符的 warmup 进度条）。关键信息：

- 最后一个 Prior 正在处理：`Prior: HalfNormal(1.5)`
- warmup 进度在 22%（1340/6000），速度已降至 ~1.22s/it（从初始 ~4.7it/s 大幅减速）
- **末尾有前一轮被 kill 的记录：**
  ```
  bash: line 1: 293733 Killed   timeout 86400 env bash -c ...
  EXIT_CODE=129
  ```
  这是前一次 exp-016 进程被杀的残留日志。当前进程（PID 316023）是重启后的新实例，正在 warmup 阶段。

---

### 命令 6 — `wc -l` 结果文件行数

| 文件 | 行数 |
|------|------|
| `exp017/results/coverage_simulation.csv` | **8**（含 header，7 条数据） |
| `exp015/results/synthetic_n8.csv` | **15**（含 header，14 条数据） |
| `exp016/results/prior_sensitivity.csv` | **不存在**（No such file or directory） |

---

### 汇总

- **exp-015**：运行中，GPU:1，已完成 ~8/20 seeds，有结果文件 14 行
- **exp-016**：运行中，GPU:2，当前 Prior HalfNormal(1.5) 的 warmup 22%，**尚无结果文件**（前一轮被 kill 过，EXIT_CODE=129）
- **exp-017**：运行中，GPU:0，800 个任务完成 7 个（~1%），结果文件 7 行

---
