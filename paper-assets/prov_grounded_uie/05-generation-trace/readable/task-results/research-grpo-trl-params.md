# research grpo trl params

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_grpo-trl-params_20260512T170255_result.json`
- **Structured JSON:** [`a4069459692a530c2d26.json`](../../sessions/a4/a4069459692a530c2d26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是报告：

---

## TRL 1.1.0 GRPOConfig 长度控制参数调查报告

**TRL 版本**: 1.1.0

### 可用的长度控制参数

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `max_completion_length` | 256 | 生成阶段 `max_new_tokens`，控制 completion 最大 token 数 |
| `mask_truncated_completions` | False | 若为 True，被截断（未生成 EOS）的 completion 在 loss 中被 mask 掉 |

### 关键发现

- **`max_prompt_length` 已被移除**，GRPOConfig 中不存在任何 prompt 长度截断参数。
- **`_tokenize_prompts()` 源码确认**：prompt 直接 tokenize，无任何截断逻辑。
- `max_completion_length` 作为 `max_new_tokens` 传给 generation，仅控制生成长度。
- tokenizer 初始化时设置了 `truncation_side="left"`，但 `_tokenize_prompts` 调用时未传 `truncation=True`，所以实际不截断。

### 推荐截断策略

**必须在数据预处理阶段自行截断 prompt**。建议实现：

```python
# 数据预处理时截断 prompt（对话格式）
max_prompt_tokens = 1024  # 根据模型 context 和 max_completion_length 计算
tokenized = tokenizer.apply_chat_template(prompt, tokenize=True)
if len(tokenized) > max_prompt_tokens:
    # 左截断：保留最后 max_prompt_tokens 个 token
    # 或直接跳过过长样本
    pass
```

上限参考：`model_max_length - max_completion_length`。

---
