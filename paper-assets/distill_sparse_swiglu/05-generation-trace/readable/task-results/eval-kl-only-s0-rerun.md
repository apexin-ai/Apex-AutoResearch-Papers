# eval kl only s0 rerun

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kl_only_s0_rerun_20260515T181141_result.json`
- **Structured JSON:** [`20f3b315b6c2d943ae71.json`](../../sessions/20/20f3b315b6c2d943ae71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。kl_only_s0 用 seq_len=2048 重跑结果：

| 指标 | 值 | 验证 |
|------|-----|------|
| true_dense_ppl | 6.12 | ≈6.12 ✓ |
| predictor_hard_mask_ppl | 9.19 | — |
| teal_sparse_ppl | 12.03 | — |
| model_level_sparsity | 0.499 | ≈0.498 ✓ |
| ppl_increase_vs_true_dense_pct | 96.57% | — |

结果与原 seq_len=1024 的 eval 一致（说明该 checkpoint 对 seq_len 不敏感）。Registry metrics 和 notes 已更新，标注了重跑原因（seq_len 1024→2048 修正）。

---
