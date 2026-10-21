# analyze exp 001 sft llama32 3B d025 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_sft_llama32_3B_d025_s42_20260516T173112_result.json`
- **Structured JSON:** [`6c16eb307f743cc60a44.json`](../../sessions/6c/6c16eb307f743cc60a44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。实验分析结果：

| 字段 | 值 |
|------|-----|
| conclusion | **success** |
| final_train_loss | 1.5265 |
| mean_token_accuracy | 0.6755 |
| training_duration | 139.2 min (8349s) |
| checkpoint_path | `/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d025_s42/merged` |
| checkpoint_size | ~6.0 GB (2 safetensors shards) |
| LoRA config | r=16, alpha=32 (合规) |
| training_samples | 54,133 |
| W&B | 未启用 |

训练 1 epoch 完成，loss 从初始 ~2.3 降至最终 ~1.45-1.50 区间（summary=1.5265），收敛正常。Merged checkpoint 含完整模型文件和 tokenizer，可直接用于下游 eval。

---
