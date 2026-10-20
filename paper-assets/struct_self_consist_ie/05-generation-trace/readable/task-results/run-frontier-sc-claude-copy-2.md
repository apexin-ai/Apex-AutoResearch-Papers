# run frontier sc claude

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_frontier_sc_claude_20260521T044812_result.json`
- **Structured JSON:** [`917e094cbab6b45771ee.json`](../../sessions/91/917e094cbab6b45771ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

TUM 代理上**没有 Claude/Anthropic 模型**，也没有 Gemini 或 DeepSeek。全部是 OpenAI 系列（GPT-5.x, o1/o3/o4 等）。

按任务指示："如果 Anthropic 模型不在 TUM 代理上，汇报给 Agent（我会向 Director 申请 Anthropic API key）"

同时，`run_frontier_sc.py` 脚本也不存在于服务器上。需要：

1. **获取 Anthropic API key**（或将 Claude 模型添加到 TUM 代理）才能运行 Claude 实验
2. **创建 `run_frontier_sc.py`** — 服务器上只有基于 vLLM 的 `run_mvp_pilot.py`，没有 API-based 的 frontier SC 脚本

如果你希望我先把 `run_frontier_sc.py` 写好（基于 OpenAI-compatible API 的 SC 实验脚本），等拿到 API key 后直接跑，我可以现在开始写。或者你可以先向 Director 申请 key，拿到后我再一起搞定。

**可用的替代 fallback 选项**（TUM 代理上的非 GPT 系列）：
- `o3` / `o3-mini` / `o1-pro` — 但这些仍属于 OpenAI family，不满足"cross-family"验证目的
- 没有任何非 OpenAI frontier 模型可用

---
