# code llama template dryrun

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_template_dryrun_20260516T100450_result.json`
- **Structured JSON:** [`95317fd2b519bf6f5fc0.json`](../../sessions/95/95317fd2b519bf6f5fc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证全部通过。

**结果：**

1. **Chat template**：LLaMA-3.1-8B base 无 `chat_template`，但词表含全部特殊 token（`<|start_header_id|>` 128006, `<|end_header_id|>` 128007, `<|eot_id|>` 128009, `<|begin_of_text|>` 128000）。使用标准 LLaMA 3.1 Instruct 格式模板。

2. **代码修改**：
   - `freige/training/__init__.py` — 新增 `LLAMA3_CHAT_TEMPLATE` 常量
   - `sft_trainer.py` / `rsft_generate.py` / `rsft_trainer.py` / `grpo_trainer.py` / `smoke_test.py` — 导入常量 + tokenizer 加载后 fallback 设置（`if not getattr(tokenizer, 'chat_template', None)`）

3. **Dry run**：
   - 3027 个训练文档全部处理成功
   - 10 个样本 tokenization 正确：均含 `<|start_header_id|>`、`<|eot_id|>`、`<|begin_of_text|>`
   - Token 长度：min=491, max=1537, mean=886（4096 max_length 下无截断问题）

---
