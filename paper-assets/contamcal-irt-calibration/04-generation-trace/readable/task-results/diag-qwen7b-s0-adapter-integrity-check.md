# diag qwen7b s0 adapter integrity check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen7b-s0-adapter-integrity-check_20260520T220206_result.json`
- **Structured JSON:** [`b3f79250f6a5ba54ea61.json`](../../sessions/b3/b3f79250f6a5ba54ea61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

## Qwen-7B s0 Adapter 完整性检查

| Dosage | adapter_model.safetensors | 大小 | 状态 |
|--------|--------------------------|------|------|
| d000 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s0/lora_adapter/adapter_model.safetensors` | 155M | ✅ |
| d005 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d005_s0/lora_adapter/adapter_model.safetensors` | 155M | ✅ |
| d025 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d025_s0/lora_adapter/adapter_model.safetensors` | 155M | ✅ |
| d050 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d050_s0/lora_adapter/adapter_model.safetensors` | 155M | ✅ |
| d100 | 尚未生成（训练中） | — | ⏳ 训练中 |

**OOM/Error 记录**: 无。唯一的 ERROR 是 bitsandbytes 的 `libnvJitLink.so.13` 加载警告（非致命，不影响训练）。无 OOM、无 CUDA error、无 killed。

**当前训练进度**: d100_s0, step 3554/4159 (85%), 预计剩余 ~36 分钟。loss ~0.98, token accuracy ~0.76。

**LoRA 配置确认**: lora_alpha=32, r=16（符合标准）。

**结论**: Qwen-7B s0 无 Gemma-2 类似问题。4 个已完成 dosage 的 adapter 均为 155MB（一致且非空），d100 正在正常训练中。

---
