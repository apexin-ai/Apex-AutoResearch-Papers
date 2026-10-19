# ops collect c1 30pct downstream

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-c1-30pct-downstream_20260519T010824_result.json`
- **Structured JSON:** [`08d95c25200a25350a2e.json`](../../sessions/08/08d95c25200a25350a2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## C1 Ablation 30% Eval 完整结果

| Metric | Value |
|--------|-------|
| **WikiText-2 PPL** | 9.4463 |
| **ARC-Challenge acc_norm** (25-shot) | 0.4027 |
| **WinoGrande acc** (5-shot) | 0.6740 |
| **MMLU acc** (5-shot) | 0.4229 |
| **GSM8K exact_match** (5-shot) | 0.0758 |

配置确认：TEAL global, sparsity=30%, uniform allocation, checkpoint=`c1_ablation_30pct_s42/predictor_bce_kl_targets.pt`。进程已完成退出，结果保存于 `/root/distill_sparse_swiglu/results/benchmark/c1_ablation_30pct_s42_eval/results.json`。

---
