# ssh cwm v10 emergency restart

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-v10-emergency-restart_20260512T234911_result.json`
- **Structured JSON:** [`cfa60104ea3939c122a2.json`](../../sessions/cf/cfa60104ea3939c122a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已有 CWM 训练进程在跑，**无需启动新进程**。

## 状态报告

### 1. 已存在的训练进程

**v10 训练（目标任务）**：
- PID: **106091**
- 启动时间: 07:45，通过 tmux session `repo-level-cwm-v10`
- 命令: `train_repo_cwm.py --output_dir checkpoints_repo_cwm_v10/ --no_wandb --save_steps 100`
- GPU: `CUDA_VISIBLE_DEVICES=2`
- CPU 占用: 106%，内存 ~4.6GB

**v9 训练（另一个运行中的任务）**：
- PID: **105205**（+ 4 个 worker 子进程 106032-106035）
- 从 checkpoint-200 恢复，输出到 `checkpoints_repo_cwm_v9/`

### 2. v10 日志（4 行，刚启动正在加载模型）
```
2026-05-13 07:45:55 INFO Loading tokenizer: Qwen3-4B
2026-05-13 07:45:55 INFO Chat template kwargs: {'enable_thinking': False}
2026-05-13 07:45:57 INFO Loaded train=70748, val=9335
2026-05-13 07:45:57 INFO Class weights: fail=1.7009, pass=0.2991
```
日志正常，无报错。正在模型加载/训练初始化阶段。

### 3. Checkpoint 目录状态
- **v10**: 目录尚未创建（训练刚启动，还没到第一个 save_steps）
- **v9**: 有 3 个 checkpoint（100, 200, 205），最新 checkpoint-205 于 07:34 保存

### 结论
v10 训练已在运行中（PID 106091），不需要启动新进程。

---
