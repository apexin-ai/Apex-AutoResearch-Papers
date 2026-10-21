# ssh mcmc phase1 status

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mcmc-phase1-status_20260525T032336_result.json`
- **Structured JSON:** [`0a72a1f7cdd742f09dba.json`](../../sessions/0a/0a72a1f7cdd742f09dba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## MCMC Phase 1 状态报告

**状态：仍在运行**（PID 614592，已运行 6h50m）

### 进度详情

| 方法 | 状态 |
|------|------|
| raw_average | 已完成（无 MCMC） |
| mfrm_only | 已完成（4 chains） |
| sequential | 已完成（4 chains） |
| **joint_gmfrm** | **chain 3/4 采样 99%，chain 4 待跑** |

**证据**：log 中 11 个 warmup 完成、10 个 sample 完成 → 10/12 chains 完成，第 11 chain 采样即将结束，还剩 1 个 chain。

### MCMC 配置
- warmup=6000, samples=4000, chains=4, target_accept=0.95
- 模型 N=18, Items=500, Judges=7, Observations=33974
- 每 chain ~40 min（~3.5-4.2 it/s × 10000 steps）

### 剩余时间估计
- 当前 chain 3 完成：~1 min
- Chain 4（最后一个）：~40 min
- **预计总完成时间：~41 分钟后**（约 UTC 11:30 左右）

### GPU 使用
- GPU 0: 861 MiB, 81% 利用率
- GPU 1-3: 空闲

---

输出目录目前为空（脚本在全部方法完成后才写文件）。我设置一个 45 分钟后的轮询，完成后立即跑分析 pipeline。是否要我这么做？

---
