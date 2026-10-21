# code apply chat template patch

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_apply-chat-template-patch_20260515T170551_result.json`
- **Structured JSON:** [`2569134fb1778ca50f8f.json`](../../sessions/25/2569134fb1778ca50f8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**补丁已存在。** `run_extraction.py` 中已经有 chat template 逻辑（约第 248-287 行）：

```python
tokenizer = llm.get_tokenizer()
_model_id = getattr(tokenizer, 'name_or_path', '') or model_path
_needs_chat_template = any(kw in _model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])
...
if _needs_chat_template:
    prompts = [
        tokenizer.apply_chat_template(
            [{"role": "user", "content": p}],
            tokenize=False,
            add_generation_prompt=True,
        )
        for p in prompts
    ]
```

这段代码在 `llm.generate()` 之前，功能和任务要求的补丁一致。

**区别**：现有实现用模型名关键词（`llama/mistral/gemma/phi`）检测是否需要 chat template，任务要求的版本用 `hasattr(tokenizer, 'chat_template') and tokenizer.chat_template` 检测。后者更通用——对任何带 chat template 的模型都生效，不依赖名字匹配。

是否需要将检测方式从名字匹配改为 `hasattr` 检查？还是现有实现已经满足需求，不再修改？

---
