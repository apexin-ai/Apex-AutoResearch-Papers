# diagnose perlayer kl 50 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_perlayer_kl_50_s42_20260522T021138_result.json`
- **Structured JSON:** [`9f40349afb5524080534.json`](../../sessions/9f/9f40349afb5524080534.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

| 项目 | 状态 |
|------|------|
| **PID 359439** | agent-ml job wrapper（bash），非原始训练进程。实际训练进程是 PID **359449**（`python -u src/train_perlayer_kl.py`），已运行约 42 分钟 |
| **训练状态** | **正在运行**，当前到 step **1300/10000**（13%），未完成 |
| **Checkpoint** | `checkpoints/perlayer_kl_50_s42/` 目录存在但**为空**（首次 save 在 step 2000） |
| **日志路径** | `/root/runs/distill_sparse_swiglu/perlayer_kl_50_s42.log`（31 行，每 100 步记录一次） |
| **GPU 状态** | cuda:0 占用 35754 MiB / 97887 MiB，利用率 100%；cuda:1 空闲 |

### 训练参数
- 模型: LLaMA-3.1-8B, sparsity=0.5, seed=42, 10000 steps
- lambda_max=5000, tau: 1.0→0.1, save_every=2000
- 每步约 1.82s，预计总时长 ~5.1h，完成时间约今天 **14:50** (UTC)

### 训练趋势
- avg_kl 从 0.020 上升到 ~0.028 后趋稳
- sparsity 从 0.406 逐渐逼近 0.50 目标（step 1000 时已达 0.508）
- lambda 自适应调节正常工作

---
