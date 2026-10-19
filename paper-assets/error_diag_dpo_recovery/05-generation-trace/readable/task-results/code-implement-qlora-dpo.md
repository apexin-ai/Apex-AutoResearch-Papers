# code implement qlora dpo

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_implement-qlora-dpo_20260513T100406_result.json`
- **Structured JSON:** [`e4e51dc29317aa3bcb3c.json`](../../sessions/e4/e4e51dc29317aa3bcb3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改到位。

## 修改报告

| 行号 | 变更 |
|------|------|
| L2 | docstring 标题 → "QLoRA DPO training..." |
| L20 | dependencies 增加 peft, bitsandbytes |
| L36 | imports 增加 `BitsAndBytesConfig` |
| L39 | 新增 `from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training` |
| L316-329 | 模型加载改为 4-bit NF4 量化 (`BitsAndBytesConfig` + `quantization_config`) |
| L344-355 | ref logps 预计算后插入 `prepare_model_for_kbit_training` + LoRA adapter 包装（r=16, alpha=32, 7个target modules） |
| L369 | optimizer 改为 `[p for p in model.parameters() if p.requires_grad]` |
| L478-479 | 新增 `--lora_r` (default=16) 和 `--lora_alpha` (default=32) CLI 参数 |

**Trainable parameters 预估**: Qwen3-8B 约 8.03B 参数，LoRA r=16 覆盖 7 个 target modules × 32 层 ≈ 20-40M trainable（~0.3-0.5%）。

**Checkpoint 保存**: `model.save_pretrained()` 通过 PEFT wrapper 自动只保存 adapter weights，无需额外修改。

**Ref logps 设计**: 4-bit base model 先计算 ref logps → 存 CPU → 再套 LoRA adapter 训练。量化误差在 policy/ref log-ratio 中抵消。

**验证结果**:
- SYNTAX OK ✓
- `--help` 正常输出，含 `--lora_r` / `--lora_alpha` ✓
- All imports OK ✓

---
