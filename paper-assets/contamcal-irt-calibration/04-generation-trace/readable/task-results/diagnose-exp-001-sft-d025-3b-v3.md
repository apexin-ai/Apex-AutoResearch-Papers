# diagnose exp 001 sft d025 3B v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_d025_3B_v3_20260515T202806_result.json`
- **Structured JSON:** [`013c80a16d0ea817ad59.json`](../../sessions/01/013c80a16d0ea817ad59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：exp_001_sft_d025_3B_v3 训练成功完成。**

| 指标 | 值 |
|------|-----|
| 完成步数 | 3384/3384 (100%) |
| train_loss | 1.1464 |
| mean_token_accuracy | 0.734 |
| 训练时长 | 14584s (≈4.05h) |
| epoch | 1.0 |
| checkpoint | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter/adapter_model.safetensors` (114MB) |

Registry 已更新：conclusion=success，checkpoint_path、log_path、metrics 均已修正。Cron 的 failed 判断是误报（进程正常退出但无 W&B/sentinel 文件）。

---
