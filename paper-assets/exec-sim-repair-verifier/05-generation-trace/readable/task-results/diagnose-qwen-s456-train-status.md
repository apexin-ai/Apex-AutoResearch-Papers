# diagnose qwen s456 train status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen-s456-train-status_20260521T215744_result.json`
- **Structured JSON:** [`229065a8ca0bf6b099fa.json`](../../sessions/22/229065a8ca0bf6b099fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen CWM s456 训练状态

### 1. 训练进度
- **PID 83243 仍在运行**，已运行 3h20m
- 当前 step: **6601/6633**（99.5%），刚完成 step 6600 的 eval
- 剩余 32 步 × ~12s/step ≈ **~6 min 训练 + ~19 min 最终 eval ≈ 25 min 后完成**

### 2. 指标
- train_loss: **0.0032–0.0036**（step 6200, epoch 2.78–2.80）
- eval_loss: **0.5061**（step 6600, epoch 2.94）

### 3. Checkpoints
- 路径: `/root/autodl-tmp/checkpoints_repo_cwm_8b_s456/`
- 已保存: checkpoint-6200, 6300, 6400, **6500**（最新, May 22 05:19）
- **best model: 无**（目录不存在）

### 4. 原 PID 4561 失败原因
```
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
```
首次 resume 未加 `--no_wandb`，wandb init 失败。当前运行已修复（加了 `--no_wandb`）。

### 5. GPU 3 状态
- PID 83243 占用 **27128 MiB**，正在训练

---
