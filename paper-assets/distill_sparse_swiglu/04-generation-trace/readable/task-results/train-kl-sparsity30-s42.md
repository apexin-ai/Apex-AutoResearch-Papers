# train kl sparsity30 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_kl_sparsity30_s42_20260515T202333_result.json`
- **Structured JSON:** [`ca362fd096bc378c8746.json`](../../sessions/ca/ca362fd096bc378c8746.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**总结：**
- 实验 `kl_sparsity30_s42` 已在 westd-34887 cuda:1 上启动（cuda:0 被 `bce_isocompute_v2_s42` 占满）
- 因 OOM 自动加了 `--gradient_checkpointing` 标志
- Step 1/1000 已正常输出：loss=1.1875, sparsity=0.406
- Registry 状态已更新为 RUNNING
- 注意：任务描述指定 cuda:0 但实际用了 cuda:1（cuda:0 无可用显存），GPU 仍在约束 C001 允许范围内

---
