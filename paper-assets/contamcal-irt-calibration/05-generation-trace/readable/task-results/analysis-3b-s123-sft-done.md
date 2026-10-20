# analysis 3B s123 sft done

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3B_s123_sft_done_20260514T001819_result.json`
- **Structured JSON:** [`21355e1d1b0254301d31.json`](../../sessions/21/21355e1d1b0254301d31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**exp_001_sft_0pct_3B_s123 — 训练成功**

| Metric | Value |
|--------|-------|
| mean_train_loss | 1.1309 |
| final_loss | 1.114 |
| mean_token_accuracy | 75.05% |
| training_time | 213.1 min (3h33m) |
| steps | 3125/3125 (1 epoch) |
| throughput | 3.91 samples/s |
| total_tokens | 19.6M |
| checkpoint_size | 488 MB |
| adapter_model | 114 MB |

Checkpoint 验证通过：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter/adapter_model.safetensors` 存在，114 MB。

Registry 状态：conclusion=success, metrics/checkpoint_path 已写入。

---
