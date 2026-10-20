# ops check 8b sft completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_8b_sft_completion_20260516T090106_result.json`
- **Structured JSON:** [`bb498e698027678e3b54.json`](../../sessions/bb/bb498e698027678e3b54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃 cron，无需删除。所有更新完成。

**训练结果汇总：plan_006_qwen3_8b_sft_bf16 ✅ 成功**

| 指标 | 值 |
|------|-----|
| 模型 | Qwen3-8B, bf16 LoRA SFT |
| 总步数 | 570 steps (3 epochs) |
| train_loss | 0.5705 |
| eval_loss (ep1→3) | 0.6814 → 0.6853 → 0.7186 |
| eval_token_accuracy (ep1→3) | 0.8396 → 0.8404 → 0.8377 |
| 训练耗时 | 65 分 32 秒 |
| Checkpoints | checkpoint-190, checkpoint-570 |
| 最终模型 | `/root/autodl-tmp/sft_output_qwen3_8b_bf16/` (adapter_model.safetensors, 698MB) |

eval_loss 在 epoch 2-3 略有上升（0.685→0.719），token accuracy 微降，存在轻微过拟合迹象。最优 checkpoint 可能是 epoch 1（checkpoint-190）。

---
