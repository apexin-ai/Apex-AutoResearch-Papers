# train multiseed kl30 cuda1

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_multiseed_kl30_cuda1_20260517T101907_result.json`
- **Structured JSON:** [`f4e0af2c3b1b087d0892.json`](../../sessions/f4/f4e0af2c3b1b087d0892.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交，30 分钟后回来检查进度。

关键配置确认：
- **lambda_max**: 默认 1000（与 s42 一致，log 确认 `cap=1000.0`）
- **CUDA_VISIBLE_DEVICES=1**，eval 用 `--gpu 0`（逻辑 GPU）
- **nohup** 后台运行，日志 `logs/multiseed_kl30_cuda1.log`
- **PID 22730**

---
