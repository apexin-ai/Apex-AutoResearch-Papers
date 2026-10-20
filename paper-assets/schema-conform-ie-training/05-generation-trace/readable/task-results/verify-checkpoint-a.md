# verify checkpoint a

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_checkpoint_a_20260513T032321_result.json`
- **Structured JSON:** [`fb5cc2110aaf679b6a5e.json`](../../sessions/fb/fb5cc2110aaf679b6a5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Group A Checkpoint 情况

**checkpoint-250 不存在。** save_steps=100，所以只有整百的 checkpoint。

### 可用 checkpoint 列表

| Checkpoint | 大小 | 时间 |
|---|---|---|
| checkpoint-100 | 1.4G | May 12 22:08 |
| checkpoint-200 | 1.4G | May 13 00:28 |
| checkpoint-300 | 1.4G | May 13 02:13 |
| checkpoint-400 | 1.4G | May 13 04:01 |
| checkpoint-500 | 1.4G | May 13 05:48 |

### Checkpoint 完整性

以 checkpoint-300 为例，内容完整：
- `adapter_model.safetensors` — 465MB（LoRA adapter 权重）
- `adapter_config.json` — LoRA 配置
- `optimizer.pt` — 931MB
- `tokenizer.json` + `tokenizer_config.json`
- `trainer_state.json`, `training_args.bin`, `scheduler.pt`, `rng_state.pth`

训练已完成（共 500 steps），还生成了 `merged/` 目录和 `completions/` 目录。最近可用的 checkpoint 是 **checkpoint-200** 和 **checkpoint-300**。

---
