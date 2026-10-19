# code starcoder2 support

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_starcoder2_support_20260513T000505_result.json`
- **Structured JSON:** [`e7f0beb55912687fdb9d.json`](../../sessions/e7/e7f0beb55912687fdb9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

原始路径也能正常加载。

## 结果汇总

### 1. 模型对比

| | Qwen2.5-Coder-3B | StarCoder2-3B |
|---|---|---|
| model_type | qwen2 | starcoder2 |
| hidden_size | 2048 | 3072 |
| params | ~3B | 3,030,371,328 |
| attention modules | q_proj, v_proj | **q_proj, v_proj** (相同) |
| pad_token | `<\|endoftext\|>` | None → 设为 eos |
| vocab_size | 151,643 | 49,152 |

### 2. 代码修改

**无需修改。** 现有代码已完全兼容 StarCoder2-3B：
- `AutoModel` / `AutoTokenizer` 自动适配架构
- `hidden_size` 从 config 动态读取
- LoRA target `["q_proj", "v_proj"]` 两个模型都有
- `train.py` 已有 `if tokenizer.pad_token is None: tokenizer.pad_token = tokenizer.eos_token`

### 3. Dry-run 结果

- **模型加载**: OK
- **LoRA**: Trainable 14,773,505 / 3,045,144,833 (0.49%)
- **Encode**: shape `[2, 256]` — 正确
- **Forward pass**: `loss=2.7674, logits=[2,4]` — 正确

### 4. StarCoder2-3B 可用路径

- `/root/autodl-tmp/.hf_cache/starcoder2-3b/`（原始路径，已补全权重）
- `/root/autodl-tmp/.ms_cache/AI-ModelScope/starcoder2-3b`（ModelScope 下载）

训练时直接 `--model-name /root/autodl-tmp/.hf_cache/starcoder2-3b/` 即可。

---
