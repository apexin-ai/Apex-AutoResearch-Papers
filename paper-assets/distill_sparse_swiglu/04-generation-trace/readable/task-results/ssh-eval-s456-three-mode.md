# ssh eval s456 three mode

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-s456-three-mode_20260515T164026_result.json`
- **Structured JSON:** [`dc29cb3258fd4a3ad9c8.json`](../../sessions/dc/dc29cb3258fd4a3ad9c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，registry 已更新。

**mvp_kl_norm_v2_s456 评估结果：**

| 指标 | 值 |
|------|-----|
| true_dense_ppl | 6.1173 |
| predictor_hard_mask_ppl | 9.14 |
| teal_sparse_ppl | 13.58 |
| model_level_sparsity | 0.498 |
| ppl_increase_vs_true_dense_pct | 121.9% |

true_dense_ppl = 6.1173，与其他 5 个 checkpoint 一致。teal_sparse_ppl = 13.58，高于 s42 (12.08) 和 s123 (11.91)，但在预期范围内。status/conclusion 已为 DONE/success，无需额外更新。

---
