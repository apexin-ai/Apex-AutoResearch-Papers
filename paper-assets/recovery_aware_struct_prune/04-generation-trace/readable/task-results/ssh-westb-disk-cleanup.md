# ssh westb disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westb_disk_cleanup_20260523T193526_result.json`
- **Structured JSON:** [`5cc7a8b2245189bb110a.json`](../../sessions/5c/5cc7a8b2245189bb110a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

**已删除：**
- `grpo_random_20_retrain/checkpoint-100/` 整目录（optimizer.pt 14.5GB + model.safetensors 11.3GB + 其他）→ 释放 ~26GB
- 5 个非保护目录的 `training_args.bin`（grpo_random_20_retrain, grpo_cka_only_20_seed123, sft_qwen_math_cka_only_20_final, sft_standard_20_qwen_math_final, grpo_qwen_math_cka_only_20）

**未动：**
- 所有 model.safetensors / 最终 checkpoint
- 所有 results/ 下的 eval 结果
- 所有保护目录（sft_rasp_alpha3p0_20/checkpoint-935, grpo_cka_only_20/checkpoint-100, sft_random_20, grpo_random_20_retrain/model.safetensors, sft_cka_only_20）

**当前磁盘状态：**
- `/root/autodl-tmp/`: 220GB used / 250GB total, **31GB 可用**（88%）
- 目标 30GB ✅ 达成

---
