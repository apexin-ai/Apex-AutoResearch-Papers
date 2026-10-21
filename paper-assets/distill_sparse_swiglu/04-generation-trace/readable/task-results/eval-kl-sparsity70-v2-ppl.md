# eval kl sparsity70 v2 ppl

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kl_sparsity70_v2_ppl_20260515T220605_result.json`
- **Structured JSON:** [`57266e9c126e1d101989.json`](../../sessions/57/57266e9c126e1d101989.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**kl_sparsity70_s42_v2 评估结果（WikiText-2, seq_len=2048）：**
- **true_dense_ppl**: 6.12
- **predictor_hard_mask_ppl**: 13.84（per-token sparsity ~0.699，合理）
- **teal_sparse_ppl**: 136069.61（**异常**，已标记 `teal_ppl_anomaly: true`）
- **eval_model_level_sparsity**: 0.699

hard_mask 13.84 符合预期趋势（50%→9.19, 70%→13.84）。TEAL 全局 mask PPL 爆炸可能原因：70% 全局排序下，某些关键层（如 Layer 14-16 仅 0.508-0.557 sparsity）的 neuron 被全局 budget 重新分配后过度裁剪。需要检查 `teal_global_masks` 中实际分配给各层的 mask ratio 是否合理。

---
