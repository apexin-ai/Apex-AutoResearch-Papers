# ops verify standard25 tokenizer

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-standard25-tokenizer_20260516T051503_result.json`
- **Structured JSON:** [`a8872449b7da635f0120.json`](../../sessions/a8/a8872449b7da635f0120.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**tokenizer 状态：完整。**

`pruned_standard_25` 目录含 `tokenizer.json` + `tokenizer_config.json` + `chat_template.jinja`，与原始模型一致（原始模型本身也没有 `special_tokens_map.json` 等额外文件）。AutoTokenizer 加载成功，vocab_size=151643，无需修复。

---
