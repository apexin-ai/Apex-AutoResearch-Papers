# research model selection rope10k

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_model-selection-rope10k_20260518T053036_result.json`
- **Structured JSON:** [`ba459e9dd1964057db7c.json`](../../sessions/ba/ba459e9dd1964057db7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/model_selection_rope10k_report.md` 并注册。

**核心结论：**

同时满足 rope_theta=10K + d_head=128 + 7B级 的模型只有 3 个：**Mistral-7B-v0.1**、**Llama-2-7B**、OLMo-7B。

**MVP 首选：Mistral-7B-v0.1**，全面优于 Llama-2-7B：
- rope_theta = 10,000, d_head = 128（精确匹配）
- GQA 架构（32Q/8KV），比 Llama-2 的 MHA 更高效
- 32K 上下文（Llama-2 仅 4K，multi-turn 不够用）
- Apache 2.0 无限制（Llama-2 有 Meta License 限制）
- 有官方 Instruct-v0.1 版本
- ~1M 月下载，生态极活跃

**关键发现：2023 年底后发布的 7B 模型全部将 rope_theta 提升到 500K-50M。** Llama-3 = 500K, Mistral-v0.3 = 1M, Qwen2.5 = 1M, Yi-1.5 = 5M, InternLM2.5 = 50M。不存在 "新且 rope_theta=10K" 的 7B 模型。

---
