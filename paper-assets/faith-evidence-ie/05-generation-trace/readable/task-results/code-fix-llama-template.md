# code fix llama template

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_llama_template_20260516T095532_result.json`
- **Structured JSON:** [`dcdcce4f45f64a68d881.json`](../../sessions/dc/dcdcce4f45f64a68d881.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

**修改的文件：**

| 文件 | 修改内容 |
|------|----------|
| `training/sft_trainer.py` | 添加 `_apply_chat_template()` 兼容函数（L63-67），替换 L89 的直接调用 |
| `eval/inference.py` | 添加 `_apply_chat_template()` 兼容函数（L105-109），替换 L119 的直接调用 |

**兼容逻辑：**
```python
def _apply_chat_template(tokenizer, messages, **kwargs):
    tmpl = getattr(tokenizer, "chat_template", None) or ""
    if "enable_thinking" not in tmpl:
        kwargs.pop("enable_thinking", None)
    return tokenizer.apply_chat_template(messages, **kwargs)
```

检查 tokenizer 的 Jinja 模板是否引用 `enable_thinking` 变量：
- Qwen3 模板包含 → 正常传递 `enable_thinking=False`
- LLaMA/其他不包含 → 自动移除该参数

**测试结果：**
- Qwen3: `enable_thinking=False` 正常传递，行为不变
- LLaMA-3.1-8B（设模板后）: 参数被安全移除，正常工作

**注意**：LLaMA-3.1-8B 是 base 模型，本身没有 `chat_template`。实际使用时需要设置模板（或用 Instruct 版本）。

**其他有同样 `enable_thinking` 的文件**（未修改）：
- `training/grpo_trainer.py:334`
- `training/rsft_trainer.py:72, 110, 132`
- `training/rsft_generate.py:102`
- `training/dpo_trainer.py:69, 75, 79`
- `training/smoke_test.py:150`

如果这些也需要 LLaMA 兼容，告诉我统一修复。

---
