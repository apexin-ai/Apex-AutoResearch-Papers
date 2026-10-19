# ssh fix method draft params

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_method_draft_params_20260520T202853_result.json`
- **Structured JSON:** [`a59ca22548831f715fd4.json`](../../sessions/a5/a59ca22548831f715fd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成，无残留旧值。汇报：

---

### 1. 参数量修正 ✅
- SDF decoder: 658K → **395K**（实际 395,777）
- EE extractor: ~1K → **~263K**（实际 263,171）
- 总辅助模块: 658,948 ≈ 659K（和之前总数一致，只是分配比例修正了）

### 2. action 维度 ✅
- `action_dim = 32`（模型内部 token 维度，默认值，`pi0_config.py:25`）
- 物理 action 维度 = 7（$\Delta x, \Delta y, \Delta z, \Delta q_1, \Delta q_2, \Delta q_3$, gripper），数据管道会 pad 到 32
- 文稿中 `W_out ∈ R^{1024 × 32}` 正确，32 是 action token space 的维度

### 3. LoRA 参数量 — **文稿有误**
从 JAX 配置分析计算（`gemma.py` 中的实际 LoRA shape）：
- PaliGemma (rank=16, 18 layers): **27.87M**
- Action Expert (rank=32, 18 layers): **22.12M**  
- **总计 ~50.0M**，不是文稿中的 ~26M

~26M 大致等于 PaliGemma 单独的 LoRA 量，可能是漏算了 action expert 的 LoRA。

### 4. 其他需修正的问题 — **重大发现**

**PyTorch 实现中实际没有 LoRA 参数。** 这是结构性问题：

- `gemma_pytorch.py` 使用 HuggingFace 标准 `PaliGemmaForConditionalGeneration` + `GemmaForCausalLM`，完全不读取 JAX 的 `lora_configs`
- 基础权重 (`pi0_base/model.safetensors`) 777 个 key，0 个 lora key
- `train_a1_sdf_aux.py` Phase 2 尝试 `if "lora" in name.lower(): p.requires_grad = True`，但找不到任何 lora 参数 → **backbone 在整个训练过程中始终冻结**
- Baseline (`train_pytorch.py`) 则训练全部参数（无 LoRA、无冻结）

**实际行为 vs 文稿描述：**

| | 文稿描述 | 实际实现 |
|---|---|---|
| Baseline (A0) | LoRA ~26M 参数 fine-tune | 全参数 fine-tune (~3.5B) |
| A1 Phase 1 | 冻结 backbone + LoRA，训 SDF+EE | 冻结全部 backbone，训 SDF+EE ✅ |
| A1 Phase 2 | 解冻 LoRA，端到端训练 | LoRA 不存在，backbone 保持冻结 ❌ |

建议：要么在 PyTorch 实现中加入 HuggingFace PEFT LoRA，要么修正文稿描述与实际实现一致。

---
