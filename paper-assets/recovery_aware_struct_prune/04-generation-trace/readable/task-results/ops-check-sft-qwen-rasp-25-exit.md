# ops check sft qwen rasp 25 exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_sft_qwen_rasp_25_exit_20260516T120219_result.json`
- **Structured JSON:** [`74e636d48f28776e866c.json`](../../sessions/74/74e636d48f28776e866c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练成功完成。**

### 结果摘要

| 指标 | 值 |
|------|-----|
| 状态 | ✅ 正常完成（"SFT recovery complete."） |
| final train_loss | **0.6062** |
| final mean_token_accuracy | **0.8673**（最后一步）|
| epoch | **2.0**（完整 2 epochs，1870/1870 steps） |
| train_runtime | **1652s**（~27.5 分钟） |
| throughput | 9.046 samples/s, 1.132 steps/s |
| 模型输出路径 | `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25/` |

模型文件完整：`model.safetensors`（10.8GB）+ config.json + tokenizer + generation_config。无 checkpoint 子目录（训练结束后仅保存最终模型）。

---
