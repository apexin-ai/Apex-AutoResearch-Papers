# code d019 kill v2 launch rasp v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d019-kill-v2-launch-rasp-v3_20260515T075721_result.json`
- **Structured JSON:** [`990b0e761dcaf1631ab0.json`](../../sessions/99/990b0e761dcaf1631ab0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 执行报告

### 1. v2 进程 Kill
- PID 274151 (GRPO v2 RASP) + PID 274156 (子进程 python) → 已 kill
- PID 276973 (GRPO v2 Standard) + PID 276978 (子进程 python) → 已 kill
- GPU 内存已完全释放（cuda:0: 3MiB, cuda:1: 0MiB）

### 2. v3 脚本修改
- `src/train_grpo_v3.py` line 253: 在 GRPOConfig 中添加 `gradient_checkpointing=True`（紧接 `save_strategy="steps"` 之后）
- shell 脚本无需修改（gradient_checkpointing 已硬编码在 Python 中）

### 3. v3 RASP 启动状态
- **tmux session**: `grpo_stage2_rasp_20_v3`
- **PID**: 233484 (wrapper) → 233489 (python)
- **日志**: `~/runs/recovery_aware_struct_prune/grpo_stage2_rasp_20_v3.log`
- **当前状态**: 模型从磁盘加载中（CPU RSS 9.1GB 持续增长，加载完成后 dispatch 到 cuda:0）
- 日志已确认 `Non-uniform MLP detected: intermediate_size range [8128, 18944]`

### 4. 磁盘空间
- `/root`: 30G 总量，8.6G 已用，**22G 可用 (29%)**

### 注意
- cuda:1 上有一个 `sft_standard_20_retrain` 任务（PID 239077）正在运行，也在模型加载阶段
- 两个旧 `eval_gsm8k.py` 进程（PID 279598, 279950）仍在 CPU 上运行（各占 ~15GB RAM），无 GPU 占用，可能是僵尸进程

---
