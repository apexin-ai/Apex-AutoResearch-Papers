# code qwen14b d050 s0 retrain prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen14b-d050-s0-retrain-prep_20260521T070835_result.json`
- **Structured JSON:** [`7a1c8a7bb41df0edc1ab.json`](../../sessions/7a/7a1c8a7bb41df0edc1ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**d050_s0 不需要重训。** Checkpoint 已完整存在：

| 项目 | 状态 |
|------|------|
| adapter_model.safetensors | 275 MB，非空 |
| lora_alpha | 32 ✓ |
| lora_r | 16 ✓ |
| seed | 0 ✓ |
| gradient_checkpointing | true ✓ |
| .done 标记 | 存在 |
| checkpoint-3642 | 有 optimizer/scheduler/rng state |
| train_config.json | 参数全部匹配要求 |

**其他信息：**
- 数据文件：58,266 行
- 磁盘：36G 可用 (86% used)
- GPU：GPU 0/2/3 空闲，GPU 1 使用 32735/97887 MiB (93% util)

这个 checkpoint 看起来是已经成功训练完成的。可能是之前标记为"空 adapter"的信息已过时——也许 sweep 修复后已经重训成功了。建议先确认是否确实需要重训，或者这个 checkpoint 已经可以直接用于后续 eval/signals。

---
