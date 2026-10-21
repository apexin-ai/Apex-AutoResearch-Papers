# ops check sft qwen standard 25 exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_sft_qwen_standard_25_exit_20260516T120239_result.json`
- **Structured JSON:** [`4c20bb16e3b8b7c8d89a.json`](../../sessions/4c/4c20bb16e3b8b7c8d89a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练成功完成。**

## 结果摘要

| 指标 | 值 |
|------|-----|
| 状态 | ✓ 正常完成 |
| final train_loss | 0.6122 (avg), 末 step ~0.499 |
| final mean_token_accuracy | 0.8607 |
| epochs completed | 2.0 |
| train_runtime | 1666s (~27.8 min) |
| train_samples_per_second | 8.973 |
| train_steps_per_second | 1.123 |

## 输出模型路径

`/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25/`

包含完整模型文件：`model.safetensors` (10.8GB) + config.json + tokenizer + chat_template。无 checkpoint 子目录（仅保存了最终模型）。

---
