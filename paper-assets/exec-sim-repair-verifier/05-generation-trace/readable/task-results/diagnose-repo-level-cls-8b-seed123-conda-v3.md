# diagnose repo level cls 8b seed123 conda v3

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_repo-level-cls-8b-seed123-conda-v3_20260515T062544_result.json`
- **Structured JSON:** [`cd8fffecd811c71a6e53.json`](../../sessions/cd/cd8fffecd811c71a6e53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

### 1. 失败原因
**训练实际已完成，EXIT_CODE=129 不影响结果。** 日志显示 6633/6633 steps 全部跑完，最终 eval 和 checkpoint 保存均成功，之后才收到 SIGHUP。原因是 SSH 会话断开（或终端关闭）导致进程收到 SIGHUP 信号，但此时训练已经结束，所有持久化操作都已完成。

最终训练指标：
- `train_loss`: 0.162
- `eval_loss`: 0.464
- `train_runtime`: 45210s (~12.5h)

### 2. 最新可用 checkpoint
- **最终 checkpoint**: `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6633/` (176M, 包含 adapter_model.safetensors + optimizer + scheduler，完整)
- **Best model**: `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/best/` (74M, 包含 adapter + tokenizer，完整)
- 其他可用 checkpoints: 6200, 6400, 6600

### 3. 是否需要 resume
**不需要。** 训练已 100% 完成（epoch 3.0），无需继续。

### 4. GPU cuda:3 当前状态
**空闲可用。** 0MiB 显存占用，0% 利用率。GPU 0 也空闲。GPU 1 和 GPU 2 被其他进程占用。

---
