# verify mistral teal ppl

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_mistral_teal_ppl_20260516T042626_result.json`
- **Structured JSON:** [`a9cddfe345fddc012f09.json`](../../sessions/a9/a9cddfe345fddc012f09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

**结论：`mistral_kl_s42` 的 `teal_sparse_ppl=8.98` 无污染，与原始日志 `eval_mistral_kl_s42.log` 完全一致。** 三项 ppl 指标（5.52 / 7.30 / 8.98）均已核实。D032 中 `kl_sparsity30_s42_v3` 被误录的 8.98 确实来自本实验的正确数据，只是被错误地 copy 到了 Llama 30% 的条目。

Registry 已添加验证注释。

---
