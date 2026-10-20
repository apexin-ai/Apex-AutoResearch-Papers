# train v4 random seed7

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_v4-random-seed7_20260515T154747_result.json`
- **Structured JSON:** [`ab56943b490e0dbf0ec1.json`](../../sessions/ab/ab56943b490e0dbf0ec1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`v4-random-seed7` 已在运行中，registry 已更新为 RUNNING。

**状态汇总：**
- **PID**: 164126，cuda:1，18.48 GiB 显存
- **进度**: 434/3387 (13%)，~2.0s/it
- **预计剩余**: ~1h40m
- **参数差异**（相比任务模板，已按 seed1 args.json 为准）：
  - `per_device_train_batch_size=1`（非 2）
  - `gradient_accumulation_steps=8`（非 4）
  - `warmup_ratio` 未设置（seed1 用的 0.0）
  - 额外参数：`--weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95 --lr_scheduler_type cosine --gradient_checkpointing true`

---
