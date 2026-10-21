# ssh kill exp014 start exp017 fix exp016

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_exp014_start_exp017_fix_exp016_20260523T065649_result.json`
- **Structured JSON:** [`fb964ec90f17ff3d7d90.json`](../../sessions/fb/fb964ec90f17ff3d7d90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

旧进程已清理。GPU 2 上只剩新 exp-016 进程（PID 316023, 658 MiB）。

---

## 汇总

### 操作 1: Kill exp-014 ✅
- tmux session `exp-014` 已 kill
- GPU 0 上残留进程 PID 283059, 289630 已 `kill -9`
- **cuda:0 已完全释放**: 0 MiB, 0% utilization

### 操作 2: 启动 exp-017 ⚠️ 需确认
- **exp-017 已在运行**（tmux session 创建于 14:57:04，进度 3/800）
- 脚本 `run_exp017.py` 是 Murphy-Topel Coverage Simulation，**硬编码 `JAX_PLATFORMS="cpu"`**，使用 CPU 多链并行（`numpyro.set_host_device_count(4)`）
- 即使提交到 cuda:0，脚本也不会使用 GPU
- MCMC 参数：chains=4, warmup=2000, samples=4000 — 与预期一致

**请确认**：保留当前 CPU 运行的 exp-017，还是需要改成 GPU 模式重跑？

### 操作 3: 调整 exp-016 ✅
- 脚本已修改：
  - **HalfNormal**: warmup=2000, samples=4000, chains=4（原参数不变）
  - **Exponential / LogNormal / Gamma**: warmup=1000, samples=2000, chains=2
- 旧 exp-016 已 kill，新 exp-016 已重启（PID 316023, cuda:2）
- 旧残留进程已清理

---
