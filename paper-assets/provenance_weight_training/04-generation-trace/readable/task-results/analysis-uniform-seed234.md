# analysis uniform seed234

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_uniform_seed234_20260524T082207_result.json`
- **Structured JSON:** [`77850efd63b1203e0cc5.json`](../../sessions/77/77850efd63b1203e0cc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments complete. Summary:

## uniform_seed234

| Metric | Value |
|--------|-------|
| train_loss | 8.008 |
| total_steps | 6103 |
| train_duration_s | 12,780 (3h33m) |
| eval_ppl_holdout | **17.7082** |
| eval_loss_holdout | **2.8740** |
| eval_holdout_tokens | 4,077,068 |
| checkpoint | `/root/autodl-tmp/provenance_weight_training/output/models/uniform_seed234/final` |

## uniform_seed789

| Metric | Value |
|--------|-------|
| train_loss | 7.959 |
| total_steps | 6103 |
| train_duration_s | 12,790 (3h33m) |
| eval_ppl_holdout | **17.6954** |
| eval_loss_holdout | **2.8733** |
| eval_holdout_tokens | 4,077,068 |
| checkpoint | `/root/autodl-tmp/provenance_weight_training/output/models/uniform_seed789/final` |

两个 seed 的 holdout PPL 非常接近（17.71 vs 17.70），差异 <0.1%，训练正常无异常。Checkpoints 均包含 checkpoint-6000、checkpoint-6103 和 final。

---
