# exp mistral kl30 s123 train eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mistral_kl30_s123_train_eval_20260520T121812_result.json`
- **Structured JSON:** [`6246ab40057867a3349a.json`](../../sessions/62/6246ab40057867a3349a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动，运行正常。

- **PID**: 212471
- **日志**: `~/runs/distill_sparse_swiglu/mistral_kl30_s123.log`
- **状态**: Step 10/1000, loss=0.5664, sparsity=0.406, lambda 正在收敛

注意：命令中 `--gpu 0` 实际使用的是 cuda:0 而非 cuda:1。如果确实需要跑在 cuda:1 上，需要在命令前加 `CUDA_VISIBLE_DEVICES=1`。当前 cuda:0 也是空闲的，训练已在 cuda:0 上正常进行。

---
