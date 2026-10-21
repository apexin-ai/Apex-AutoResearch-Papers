# eval sparsity30 v3 ppl

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_sparsity30_v3_ppl_20260515T223513_result.json`
- **Structured JSON:** [`b1071741503902ce28cf.json`](../../sessions/b1/b1071741503902ce28cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。kl_sparsity30_s42_v3 WikiText-2 PPL 评估结果：

| 指标 | 值 |
|------|-----|
| true_dense_ppl | 6.12 |
| predictor_hard_mask_ppl | 7.30 |
| teal_sparse_ppl | 8.76 |
| model_level_sparsity | 0.285 |

验证通过：
- true_dense_ppl = 6.12（与其他实验一致）
- predictor_hard_mask_ppl = 7.30（28.5% sparsity 较温和，符合预期 7-9 范围）
- teal_sparse_ppl = 8.76（28.5% 下 TEAL 正常，未触发高 sparsity 的 normalization bug）
- model_level_sparsity = 0.285（符合训练收敛值）

Registry 已更新，plan_008 sparsity sweep 三个数据点（28.5%/50%/70%）齐全。

---
