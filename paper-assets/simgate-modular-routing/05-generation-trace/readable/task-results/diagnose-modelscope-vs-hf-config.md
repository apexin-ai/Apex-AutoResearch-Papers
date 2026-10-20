# diagnose modelscope vs hf config

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_modelscope-vs-hf-config_20260514T063051_result.json`
- **Structured JSON:** [`3511154f131a574de5c5.json`](../../sessions/35/3511154f131a574de5c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成全部检查。以下是完整报告。

---

## 完整对比报告

### 1. config.json：ModelScope vs HuggingFace — **完全一致**

两个版本的 `config.json` 逐字节相同，关键字段：

| 字段 | ModelScope | HuggingFace |
|------|-----------|-------------|
| `vocab_size` | 151936 | 151936 |
| `pad_token_id` | **未设置 (None)** | **未设置 (None)** |
| `eos_token_id` | 151645 | 151645 |
| `bos_token_id` | 151643 | 151643 |
| `tie_word_embeddings` | true | true |
| `torch_dtype` | bfloat16 | bfloat16 |
| `hidden_size` | 2048 | 2048 |
| `num_hidden_layers` | 28 | 28 |
| `architectures` | Qwen3ForCausalLM | Qwen3ForCausalLM |
| `transformers_version` | 4.51.0 | 4.51.0 |

**结论：config.json 无差异。问题不在 ModelScope vs HuggingFace 的模型文件。**

### 2. tokenizer_config.json — **完全一致**

| 字段 | ModelScope | HuggingFace |
|------|-----------|-------------|
| `pad_token` | `<\|endoftext\|>` | `<\|endoftext\|>` |
| `eos_token` | `<\|im_end\|>` | `<\|im_end\|>` |
| `tokenizer_class` | Qwen2Tokenizer | Qwen2Tokenizer |
| `model_max_length` | 131072 | 131072 |

### 3. Tokenizer 加载后 — **完全一致**

| 字段 | ModelScope | HuggingFace |
|------|-----------|-------------|
| `pad_token` | `<\|endoftext\|>` (id=151643) | `<\|endoftext\|>` (id=151643) |
| `eos_token` | `<\|im_end\|>` (id=151645) | `<\|im_end\|>` (id=151645) |
| `vocab_size` | 151643 | 151643 |
| `len(tokenizer)` | 151669 | 151669 |
| special tokens | 14 个，完全一致 | 14 个，完全一致 |

### 4. generation_config.json — 仅 ModelScope 目录有

```json
{
    "bos_token_id": 151643,
    "do_sample": true,
    "eos_token_id": [151645, 151643],
    "pad_token_id": 151643,
    "temperature": 0.6,
    "top_k": 20,
    "top_p": 0.95
}
```

注意：`generation_config.json` 中的 `pad_token_id: 151643` **不会被 `AutoConfig.from_pretrained` 读取**，只影响生成。

### 5. 分类头初始化

```
Config num_labels: 2
Config problem_type: None
Config pad_token_id: None  ← ⚠️
Score head: Linear(in_features=2048, out_features=2, bias=False)
Score weight shape: [2, 2048]
Score weight stats: mean=0.000137, std=0.0201
Score weight range: [-0.069, 0.080]
```

分类头权重随机初始化，统计量正常。

### 6. 🔴 关键发现：Sequence Classification 的 pooling 逻辑

从源码提取的实际 pooling 逻辑：

```python
if self.config.pad_token_id is None and batch_size != 1:
    raise ValueError("Cannot handle batch sizes > 1 if no padding token is defined.")
if self.config.pad_token_id is None:
    last_non_pad_token = -1   # ← 始终取最后一个 position
elif input_ids is not None:
    # 找到最右边的非 pad token
    non_pad_mask = (input_ids != self.config.pad_token_id)
    last_non_pad_token = (token_indices * non_pad_mask).argmax(-1)
```

**`config.pad_token_id = None` 时：**
- batch_size > 1 → 直接 **raise ValueError**（训练应该崩溃）
- batch_size == 1 → 取最后一个 position（如果有 padding，取到的是 pad token 的 hidden state → 垃圾输入给分类头）

---

## 🔴 高亮结论

1. **ModelScope 与 HuggingFace 的 config/tokenizer 完全一致，零差异。** 原始假设"问题在 ModelScope 模型"不成立——两者是同一份文件。

2. **核心问题：`config.pad_token_id = None`，但 `tokenizer.pad_token_id = 151643`。** 这是 Qwen3 原始 config 的"设计"——config.json 中没有 `pad_token_id` 字段。这意味着：
   - `Qwen3ForSequenceClassification` 在 batch_size > 1 时会 **crash**
   - batch_size == 1 时，pooling 取最后一个 position（可能是 pad token）

3. **dryrun 与 v3/v4 的 loss 差异，原因不在模型文件差异，而在训练代码是否正确设置了 `config.pad_token_id = tokenizer.pad_token_id`。** 需要对比 dryrun 和 v3/v4 的训练脚本，看谁设了、谁没设。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "bos_token_id": 151643,
    "do_sample": true,
    "eos_token_id": [
      151645,
      151643
    ],
    "pad_token_id": 151643,
    "temperature": 0.6,
    "top_k": 20,
    "top_p": 0.95
  }
}
```

</details>

---
