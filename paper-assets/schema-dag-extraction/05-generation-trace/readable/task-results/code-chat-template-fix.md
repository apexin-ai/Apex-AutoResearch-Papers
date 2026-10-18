# code chat template fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_chat-template-fix_20260515T165850_result.json`
- **Structured JSON:** [`1cb9d9a368db0b89318d.json`](../../sessions/1c/1cb9d9a368db0b89318d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改正确。

## Qwen3 chat_template 检查
- has_chat_template: **true**（tokenizer_config.json 中存在）
- 结论: **需要模型名检测**（两者都有 chat_template，不能用通用检测区分）

## 代码修改
- 文件: `src/run_extraction.py`
- 方案: **模型名检测**（`['llama', 'mistral', 'gemma', 'phi']`）
- 修改位置:
  - **L218-222**: LLM 创建后，获取 tokenizer 并检测 `_needs_chat_template`
  - **L277-285**: `llm.generate` 前，条件性 `apply_chat_template`
- Qwen3 路径中不含 `llama/mistral/gemma/phi` → `_needs_chat_template=False` → 保持裸文本
- LLaMA 路径含 `llama` → `_needs_chat_template=True` → 包装 chat template

## 验证
- syntax check: **PASS**
- Qwen3 兼容性: **确认安全**（检测条件不命中，走原始 prompts 分支）

## 诊断脚本修复
- `diagnose_llama8b_freeform.py`: **已有 chat template**（L83-90 已经 apply_chat_template），无需修改

---
