# analysis qwen06b uniform seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen06b_uniform_seed42_20260517T215356_result.json`
- **Structured JSON:** [`a0c5580ba5631a6296b4.json`](../../sessions/a0/a0c5580ba5631a6296b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。结果如下：

## 实验结果：`qwen06b_uniform_seed42` (v2 retrain)

| 指标 | 值 |
|---|---|
| **final train_loss** | 7.9894 |
| **total training steps** | 6103 |
| **train runtime** | 12860.1 s (~3h 34m) |
| **eval_ppl_holdout** | **17.6949** |
| **eval_loss_holdout** | **2.8733** |
| **eval_holdout_tokens** | 4,077,068 |
| **checkpoint_path** | `/root/autodl-tmp/provenance_weight_training/output/models/qwen06b_uniform_seed42_v2/final` |
| **log_path** | `~/runs/provenance_weight_training/qwen06b_uniform_seed42.log` |
| **W&B run_id** | 无（WANDB_MODE=disabled） |

## 与历史结果对比

| 指标 | 上次 uniform_seed42 | 本次 v2 retrain |
|---|---|---|
| eval_ppl_holdout | 17.6939 | 17.6949 |
| eval_loss_holdout | 2.8732 | 2.8733 |

PPL 差异仅 0.001（17.6939 vs 17.6949），loss 差异 < 0.0001。结果高度一致，retrain 可复现，去掉 inline eval 没有影响训练结果。

---
