# research api fallback

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_api_fallback_20260520T091159_result.json`
- **Structured JSON:** [`1c7fc2fd0d61f34d8b14.json`](../../sessions/1c/1c7fc2fd0d61f34d8b14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/api_fallback_comparison.md`。

核心结论：
- **方案 3 (OpenRouter 官方)** 代码改动最小 — 只改一行 `base_url` + 换 API key，总成本 ~$17.66
- **方案 1+2 (双直连)** 最便宜 (~$16.74, 无加价) 但改动最大，需维护两套 SDK
- **方案 4 (Together/Fireworks)** 不可行，不支持 Claude/GPT 闭源模型

---
