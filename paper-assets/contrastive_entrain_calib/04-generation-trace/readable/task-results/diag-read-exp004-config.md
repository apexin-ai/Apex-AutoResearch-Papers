# diag read exp004 config

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_read-exp004-config_20260518T171155_result.json`
- **Structured JSON:** [`9c1c778226245d9d8cef.json`](../../sessions/9c/9c1c778226245d9d8cef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-004 ACT baseline 配置如下：

| 配置项 | 值 |
|---|---|
| **learning_rate** | `5e-5` |
| **lora_rank (r)** | `64` |
| **lora_alpha** | `128` (`lora_rank * 2`) |
| **lora_target_modules** | `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj` |
| **warmup_steps** | `200` |
| **batch_size / grad_accum** | batch_size=`1`, gradient_accumulation_steps=`16` (effective batch=16) |
| **max_steps** | `8000` |
| **optimizer** | `AdamW` (weight_decay=0.01, grad_clip=1.0) |
| **scheduler** | `linear` (get_linear_schedule_with_warmup) |

补充：lora_dropout=0.05, bf16 精度, gradient_checkpointing 开启。

---
