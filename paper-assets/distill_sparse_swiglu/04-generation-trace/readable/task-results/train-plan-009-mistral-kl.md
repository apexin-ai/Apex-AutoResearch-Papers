# train plan 009 mistral kl

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan_009_mistral_kl_20260515T222754_result.json`
- **Structured JSON:** [`ae30ec7dc0f87e4f0e2a.json`](../../sessions/ae/ae30ec7dc0f87e4f0e2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中，已到 step 550/1000。指标健康：

- **KL loss**: ~0.19（稳定下降，初始约 0.25 → 目前 ~0.19）
- **Sparsity**: 0.480-0.496（目标 0.50，constraint_loss=0 说明在容差内）
- **Tau 退火**: 1.0 → 0.505（按预期线性下降）
- **Lambda**: 稳定在 1000（上限）

## 总结

1. **训练已在运行** — tmux session `mistral_kl_s42`，PID 147637，cuda:1，已完成 55%（550/1000 steps）
2. **Registry 已更新** — status=RUNNING，spec 已填充完整（command, server, data_path, model_name, seed）
3. 训练参数与任务要求完全一致（kl_normalized, sparsity_target=0.5, seed=42, gradient_checkpointing, lambda_max=1000）
4. 预计还需 ~15 分钟完成。训练结束后 cron 系统会自动回调。

---
