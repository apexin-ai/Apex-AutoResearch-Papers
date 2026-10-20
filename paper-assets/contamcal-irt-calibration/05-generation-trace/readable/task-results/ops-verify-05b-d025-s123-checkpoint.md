# ops verify 05B d025 s123 checkpoint

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-05B-d025-s123-checkpoint_20260515T055118_result.json`
- **Structured JSON:** [`87e9e0da8c00cc73699b.json`](../../sessions/87/87e9e0da8c00cc73699b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。**exp_001_sft_05B_d025_s123_v2 是 cron 误判，实际已正常完成。**

汇总：
- **训练状态**：epoch=1.0 完整训练，train_loss=1.548，mean_token_accuracy=0.697，耗时 5930s (~99min)
- **Checkpoint**：adapter_model.safetensors (35MB)、adapter_config.json、tokenizer 文件齐全，LoRA r=16 alpha=32
- **GPU 0**：已释放，0 MiB / 0% util
- **Registry**：已更正为 conclusion=success，清除 failure_reason，写入 metrics

---
