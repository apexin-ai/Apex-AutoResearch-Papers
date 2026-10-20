# fix symlink 30k chkpt model

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_symlink_30k_chkpt_model_20260528T021111_result.json`
- **Structured JSON:** [`fc715bee23169c908206.json`](../../sessions/fc/fc715bee23169c908206.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。30000_chkpt 目录现在包含：

**Symlinks（5 个，指向 `/root/autodl-tmp/models/openvla-7b/`）：**
- `model-00001-of-00003.safetensors` → openvla-7b base
- `model-00002-of-00003.safetensors` → openvla-7b base
- `model-00003-of-00003.safetensors` → openvla-7b base
- `model.safetensors.index.json` → openvla-7b index
- `config.json` → openvla-7b config

**注意差异：** 原始 openvla-7b 是 **3 shards**（`*-of-00003`），而其他已完成的 checkpoint（如 25000_chkpt）是 **4 shards**（`*-of-00004`，LoRA merge 后重新分片）。这些 symlinks 提供的是 base model 权重（未合并 LoRA），不是 merged 权重。LoRA adapter 已存在于 `lora_adapter/` 子目录，后续可按需重新 merge。

---
