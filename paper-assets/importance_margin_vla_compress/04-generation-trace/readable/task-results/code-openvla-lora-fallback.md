# code openvla lora fallback

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla_lora_fallback_20260519T172518_result.json`
- **Structured JSON:** [`c9866fd2c443be291381.json`](../../sessions/c9/c9866fd2c443be291381.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

| 项目 | 状态 |
|------|------|
| **peft** | v0.19.1 已安装 |
| **LoRA 脚本** | `train_openvla_smart_compress_lora.py` (667行) 已部署，语法检查通过 |
| **LoRA config** | `configs/openvla_smart_compress_m128_lora.yaml` 已部署 |
| **batch_size 修正** | `configs/openvla_smart_compress_m128.yaml` 已从 4 → 8 |

LoRA 脚本关键改动点：
- L34: `from peft import LoraConfig, get_peft_model`
- L474-488: `apply_lora_to_backbone()` 函数，对 LLM backbone 的 `q_proj`/`v_proj` 注入 LoRA (r=16, alpha=32)
- L521-526: `main()` 中根据 `config.model.use_lora` 有条件应用 LoRA
- L576-578: wandb run name 自动加 `_lora` 后缀

训练方式不变：VTC compressor + LoRA adapters 可训练，其余 backbone frozen。未启动任何训练。

---
