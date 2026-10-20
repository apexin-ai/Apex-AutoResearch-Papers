# code fix chat template

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_chat_template_20260514T043155_result.json`
- **Structured JSON:** [`60fec92a7a9828ec1762.json`](../../sessions/60/60fec92a7a9828ec1762.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

改动总结：

1. **`__init__`**：保存 `_model_path`，初始化 `_tokenizer = None`
2. **`_get_tokenizer()`**：lazy import `transformers.AutoTokenizer`，首次调用时加载，后续复用
3. **`format_chat_prompt()`**：用 `apply_chat_template` 包裹单条 prompt，添加 generation prompt
4. **`sample()`**：新增 `use_chat_template=True` 参数，在调用 `llm.generate()` 前包裹所有 prompts
5. **`run_sampling_pipeline()`**：新增 `use_chat_template=True` 参数，透传给两次 `sample()` 调用

所有 import 都是 lazy 的，无 vllm/transformers 环境下 import 正常。默认启用 chat template，传 `use_chat_template=False` 可关闭。

---
