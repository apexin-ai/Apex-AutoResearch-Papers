# research llama grpo qlora compat

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_llama_grpo_qlora_compat_20260516T124128_result.json`
- **Structured JSON:** [`f7af8772e236455c9ba4.json`](../../sessions/f7/f7af8772e236455c9ba4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已足够。汇报如下：

---

## 验证结果

### 1. `_apply_chat_template` — 已兼容 LLaMA

```python
def _apply_chat_template(tokenizer, messages, **kwargs):
    tmpl = getattr(tokenizer, 'chat_template', None) or ''
    if 'enable_thinking' not in tmpl:
        kwargs.pop('enable_thinking', None)
    return tokenizer.apply_chat_template(messages, **kwargs)
```

该函数只处理 Qwen3 的 `enable_thinking` 参数兼容问题。LLaMA tokenizer 自带 `chat_template`，`apply_chat_template` 直接可用，**无需适配**。

### 2. QLoRA 4-bit 配置 — 已存在且完整

- 默认启用（`--quantize` 默认 True，`--no_quantize` 禁用）
- BitsAndBytesConfig: `load_in_4bit=True`, `nf4`, `double_quant`, `bf16 compute`
- `device_map = {"": local_rank}` — 单卡绑定，符合 C002/C003 约束

### 3. LoRA 配置 — target modules 兼容 LLaMA

```python
target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
```

这些 module 名在 LLaMA-3.1 架构中完全一致，**无需修改**。默认 `lora_rank=64`。

### 4. 显存估算 — 32GB 可 fit

| 组件 | 估算 |
|------|------|
| LLaMA-3.1-8B 4-bit weights | ~5 GB |
| LoRA adapters (r=64, 7 modules) | ~0.5 GB |
| Optimizer states (AdamW on LoRA params) | ~1 GB |
| G=4 generations × 1024 tokens KV cache | ~8-10 GB |
| Activations + gradients (batch=1) | ~4-6 GB |
| **总计** | **~19-23 GB** |

RTX 5090 32GB 有 ~9-13GB 余量，**可行**。但如果 `max_length=4096` 的长 prompt 导致 KV cache 增大，余量会缩小到 ~5GB。建议保持 `per_device_batch_size=1`。

### 5. LLaMA base model — 已存在

`/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B/config.json` ✓

### 6. 需要的适配

**零适配**。直接传参即可运行：

```bash
CUDA_VISIBLE_DEVICES=X python -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B \
  --stage 1 --num_generations 4 --lora_rank 64 \
  --per_device_batch_size 1 --gradient_accumulation_steps 16 \
  --max_length 4096 --max_new_tokens 1024
```

脚本对模型架构无硬编码假设，LoRA target modules 与 LLaMA-3.1 一致，chat template 通过 tokenizer 自带处理。唯一注意点：如果有 LLaMA SFT adapter 需要加载，传 `--sft_adapter` 路径。

---
