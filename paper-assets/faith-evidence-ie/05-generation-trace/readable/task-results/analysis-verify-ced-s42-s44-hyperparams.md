# analysis verify ced s42 s44 hyperparams

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify_ced_s42_s44_hyperparams_20260516T002605_result.json`
- **Structured JSON:** [`cdad97ebf24552940052.json`](../../sessions/cd/cdad97ebf24552940052.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。所有证据来源：`training_args.bin`、`adapter_config.json`、训练日志。

## 对比结果

| 参数 | s42 实际 | s44 实际 | s43/s45 r3 目标 | 一致？ |
|------|---------|---------|----------------|--------|
| per_device_batch_size | 4 | 4 | 4 | ✓ |
| gradient_accumulation_steps | 4 | 4 | 4 | ✓ |
| weighted_sampling | True | True | True | ✓ |
| data_path | rsft_filtered/rsft_train.jsonl | rsft_filtered/rsft_train.jsonl | rsft_filtered/rsft_train.jsonl | ✓ |
| data_count | 2718 | 2718 | 2718 | ✓ |
| learning_rate | 2e-5 | 2e-5 | 2e-5 | ✓ |
| num_epochs | 3 | 3 | 3 | ✓ |
| lora_rank | 64 | 64 | 64 | ✓ |
| lora_alpha | 128 | 128 | 128 | ✓ |
| seed | 42 | 44 | 43/45 | ✓ |
| bf16 | True | True | — | ✓ |
| warmup_steps | 100 | 100 | — | ✓ |
| lr_scheduler | LINEAR | LINEAR | — | ✓ |

**结论：s42/s44 原始训练超参与 s43/s45 r3 完全一致。** 四个 seed 的 paired t-test 前提条件满足。

---
