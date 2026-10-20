# ops cls repo nan diagnose

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cls-repo-nan-diagnose_20260516T164100_result.json`
- **Structured JSON:** [`0267a78a8175cdf062dd.json`](../../sessions/02/0267a78a8175cdf062dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cls-repo nan 诊断报告

**train_loss 状态**: 正常。从 3.33 (step 50) 稳步降至 0.0146 (step 2200)，grad_norm 始终在合理范围。

**当前 step**: ~3177/6633 (48%)，仍在正常推进，~10-11s/it

**checkpoint 状态**: `checkpoint-2211`（epoch 1 完整，含 adapter_model.safetensors 64MB + optimizer.pt 128MB）

**eval_loss nan 原因**: **数据截断导致 labels 全为 -100 的空标签 batch。**

具体机制：
- max_seq_length=2048，val 集有 21/9335 条样本被截断
- cls 任务的 target 只有 "pass"/"fail"（1-2 token）。当某条样本的 prompt 部分（system + user 含长 patch/test）≥ 2048 token 时，`full_ids[:2048]` 完全是 prompt token，target 被完全截掉
- 此时 `labels = [-100] * 2048`，全部被 mask
- eval_batch_size=2，如果一个 batch 里两条样本的 labels 全为 -100 → CrossEntropyLoss 在 0 个有效 token 上算 loss → NaN
- HF Trainer 对 eval_loss 取 mean，任何一个 batch NaN → 整体 NaN
- 训练不受影响，因为 train 的 1559 条截断样本中 target 只是被截短（不是完全消失），仍有有效 label token

**潜在风险**: `load_best_model_at_end=True` + `metric_for_best_model="eval_loss"`，但 `best_model_checkpoint=null`（因为 NaN 无法比较）。如果后续 epoch eval 仍是 NaN（大概率），训练结束时 Trainer 尝试 load best model 可能出错。

**建议**: **继续跑，不要 kill。** 模型完全没有崩溃。训练结束后直接用最后一个 checkpoint（或 checkpoint-2211），不依赖 Trainer 自动选 best。后续如需修复，在 `preprocess_split` 中过滤掉 `labels` 全为 -100 的样本即可。

---
