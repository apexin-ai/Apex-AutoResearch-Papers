# infra download qwen instruct

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download_qwen_instruct_20260521T151825_result.json`
- **Structured JSON:** [`84242cfccd1bed7302e2.json`](../../sessions/84/84242cfccd1bed7302e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：**`Qwen/Qwen3-8B-Instruct` 在 HuggingFace 上不存在。**

Qwen3 系列所有模型（0.6B、1.7B、4B、8B、14B、30B-A3B）均只有 base 名称（如 `Qwen/Qwen3-8B`），没有单独的 `-Instruct` 变体。Qwen3 模型本身已经是指令微调+思考模式的，不再区分 base/instruct。

服务器上已有 `/root/models/Qwen3-8B`（当前正在被 `verify_parametric_knowledge.py` 和 `translate_to_zh.py` 使用）。`Qwen/Qwen3-8B` 即等效于你想要的 Instruct 模型。

需要我做什么？
1. 如果你确实需要一个不同的模型（比如 Qwen2.5-8B-Instruct），我可以下载
2. 如果 Qwen3-8B 就是目标，服务器上已经有了，无需额外下载

---
