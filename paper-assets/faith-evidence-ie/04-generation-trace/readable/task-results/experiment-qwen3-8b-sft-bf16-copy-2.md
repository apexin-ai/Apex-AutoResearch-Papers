# experiment qwen3 8b sft bf16

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_qwen3_8b_sft_bf16_20260516T080803_result.json`
- **Structured JSON:** [`9b612e97024b4fb207f7.json`](../../sessions/9b/9b612e97024b4fb207f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**任务已完成** — `plan_006_qwen3_8b_sft_bf16` 已在 cuda:3 上 RUNNING（PID 317310，占用 29879 MiB）。

Registry 显示该实验在 `2026-05-16T07:51:04` 提交，配置与要求完全一致：

| 字段 | 值 |
|------|-----|
| model | `/root/autodl-tmp/models/Qwen/Qwen3-8B` |
| quantize | none (bf16 LoRA) |
| lora_rank / alpha | 64 / 128 |
| data_count | 3027 |
| epochs | 3 |
| lr | 2e-4 |
| seed | 42 |
| batch_size | 1, grad_accum=16 |
| output_dir | `/root/autodl-tmp/sft_output_qwen3_8b_bf16` |
| CUDA_VISIBLE_DEVICES | 3 |

无需重复提交。训练正在正常进行中。

---
