# train multiseed kl50 cuda0

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_multiseed_kl50_cuda0_20260517T101855_result.json`
- **Structured JSON:** [`4eb320bb32741659cdf0.json`](../../sessions/4e/4eb320bb32741659cdf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交：
- **脚本**: `/root/distill_sparse_swiglu/scripts/multiseed_kl50.sh`
- **日志**: `/root/distill_sparse_swiglu/logs/multiseed_kl50.log`
- **PID**: 22258 (bash) → 22260 (seed=123 训练中)
- **GPU**: cuda:0 only (CUDA_VISIBLE_DEVICES=0)

串行流程：train s123 → eval s123 → train s456 → eval s456。预计 ~1h 完成，20 分钟后自动检查进度。

---
