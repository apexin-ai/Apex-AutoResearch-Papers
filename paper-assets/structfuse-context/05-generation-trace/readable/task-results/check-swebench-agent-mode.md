# check swebench agent mode

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_swebench-agent-mode_20260515T041700_result.json`
- **Structured JSON:** [`6c1689db6947538a707d.json`](../../sessions/6c/6c1689db6947538a707d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：

`eval_swebench_e2e.py` 中 agent（Qwen3.6-27B）通过 **OpenAI-compatible API 调用**，不是本地推理。具体配置通过环境变量控制：
- `STRUCTFUSE_LLM_BACKEND=api`
- `STRUCTFUSE_LLM_API_BASE` 指定 API endpoint（如本地 vLLM 服务地址）
- `STRUCTFUSE_LLM_API_KEY` 提供 API key
- `STRUCTFUSE_LLM_MODEL` 指定模型名

因此 retrieval model 和 27B agent **不需要同时加载到同一 GPU**——retriever 加载 StructFuse checkpoint 做 embedding，agent 推理走独立的 API 服务（可以是另一台机器上的 vLLM，也可以是外部 API）。

---
