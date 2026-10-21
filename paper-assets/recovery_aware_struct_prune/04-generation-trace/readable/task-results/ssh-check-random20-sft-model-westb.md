# ssh check random20 sft model westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_random20_sft_model_westb_20260521T142824_result.json`
- **Structured JSON:** [`0fc8aa9f44d58124e865.json`](../../sessions/0f/0fc8aa9f44d58124e865.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 服务器 | `sft_random_20` | 状态 |
|--------|-----------------|------|
| **westb-23072** | 不存在 | 目录列表中无任何 `random` 相关 SFT 目录 |
| **westd-29022** | **存在** | 完整 checkpoint |

**westd-29022 上的 `sft_random_20` 详情：**

路径：`/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20/`

| 文件 | 大小 |
|------|------|
| `model.safetensors` | **11.34 GB** (12,174,631,264 bytes) |
| `config.json` | 2,244 B |
| `tokenizer.json` | 10.9 MB |
| `tokenizer_config.json` | 419 B |
| `generation_config.json` | 240 B |
| `chat_template.jinja` | 2,246 B |
| `training_args.bin` | 5,777 B |

创建时间：2026-05-21 11:38。模型文件 ~11.3 GB，目录结构完整（含 config、tokenizer、training_args），是一个完整的 SFT checkpoint。

westb-23072 上无任何 random 相关的 safetensors 文件。如需使用，需从 westd-29022 拷贝。

---
