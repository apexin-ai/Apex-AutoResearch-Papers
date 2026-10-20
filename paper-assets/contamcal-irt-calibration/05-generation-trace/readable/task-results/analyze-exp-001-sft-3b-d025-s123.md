# analyze exp 001 sft 3B d025 s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_sft_3B_d025_s123_20260515T144534_result.json`
- **Structured JSON:** [`1b7fa761839c6dd4b2ba.json`](../../sessions/1b/1b7fa761839c6dd4b2ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

**exp_001_sft_3B_d025_s123 训练成功完成：**

| 指标 | 值 |
|------|-----|
| status | DONE (success) |
| final_train_loss | 1.1452 |
| mean_token_accuracy | 0.7719 |
| total_steps | 3384 |
| runtime | 9751s (~2.7h) |
| checkpoint | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/adapter_model.safetensors` (119MB) |
| W&B | 未启用 |

注意：日志显示实际 LoRA alpha=32（代码 `train_sft.py` 默认值），与提交命令中 `--lora-alpha 16` 不一致，可能是参数未生效，建议后续确认。

---
