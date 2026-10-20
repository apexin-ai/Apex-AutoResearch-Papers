# ssh westd olmo d005v2 analysis

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-olmo-d005v2-analysis_20260519T060740_result.json`
- **Structured JSON:** [`3ca881a8741cf241b499.json`](../../sessions/3c/3ca881a8741cf241b499.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## OLMo-2-7B d005 v2 训练最终指标

| 指标 | 值 |
|---|---|
| **train_loss** | 0.9506 |
| **mean_token_accuracy** | 0.7808 |
| **entropy** | 0.94 |
| **total steps** | 3177 |
| **epoch** | 1.0 |
| **train_runtime** | 6636s (1h50m35s) |
| **train_samples_per_second** | 7.66 |
| **train_steps_per_second** | 0.479 |

**状态确认**:
- `.done` 文件存在 (May 19 13:48)
- `adapter_model.safetensors` 完整，152.5 MB，位于 `lora_adapter/` 子目录（非 checkpoint 根目录）
- EXIT_CODE=0，训练正常完成

---
