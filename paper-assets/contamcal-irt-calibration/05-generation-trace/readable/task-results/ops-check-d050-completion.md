# ops check d050 completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-d050-completion_20260518T162759_result.json`
- **Structured JSON:** [`8e30c1188315cc726dd2.json`](../../sessions/8e/8e30c1188315cc726dd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**训练成功完成。**

### 日志确认
- 3642/3642 steps 全部跑完（100%），耗时 1h39m01s
- 最后一行：`2026-05-19 00:24:19 [INFO] Training complete.`

### 最终指标
| 指标 | 值 |
|---|---|
| train_loss | 0.9599 |
| mean_token_accuracy | 0.7641 |
| entropy | 1.008 |
| epoch | 1.0 |
| train_runtime | 5941s (~1h39m) |
| train_steps_per_second | 0.613 |

### Checkpoint 完整性
`lora_adapter/` 目录文件齐全：
- `adapter_model.safetensors` — 154MB
- `adapter_config.json` — lora_alpha=32, r=16 ✓
- `tokenizer.json` + `tokenizer_config.json`
- `training_args.bin`
- `checkpoint-3642/` 子目录（最终 step checkpoint）

### 问题
- **无 `.done` sentinel 文件** — 这就是 cron reconcile 误判的原因。训练脚本没有在完成后写 sentinel。如果需要自动检测完成状态，需要在训练脚本末尾加 `touch .done`。

---
