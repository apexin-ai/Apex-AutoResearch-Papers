# infra plan001 api model probe

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan001-api-model-probe_20260522T070038_result.json`
- **Structured JSON:** [`957af979d758fc1b2216.json`](../../sessions/95/957af979d758fc1b2216.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**API 可用模型（13个）：**

| 家族 | 可用模型 |
|------|----------|
| OpenAI GPT | gpt-4o-mini, gpt-4o, gpt-4.1, gpt-4.1-mini, gpt-4.1-nano |
| OpenAI GPT-5 | gpt-5.4-mini, gpt-5.5 |
| OpenAI o-series | o4-mini |
| Claude | claude-sonnet-4, claude-opus-4, claude-3-haiku |
| Gemini | gemini-2.5-flash, gemini-2.5-pro |

**不可用：** claude-3-5-sonnet 系列（需用 `claude-sonnet-4` 替代）、gemini-1.5-pro / gemini-2.0-flash（需用 `gemini-2.5-flash/pro` 替代）、DeepSeek 全系列不可用。

**本地 AWQ 模型（6个）：** Qwen2.5-72B/32B/14B、Llama-3.1-70B/8B、Mistral-Large-2407，均为 AWQ 量化版。

**注意：** `/v1/models` 只列出 118 个 OpenAI 模型，Claude/Gemini 通过代理路由可用但不在 catalog 中。API 需要 Bearer token 认证。

结果已保存至 `artifacts/results/api_model_availability.json`。

---
