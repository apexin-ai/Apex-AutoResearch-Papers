# infra openrouter verify

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_openrouter-verify_20260522T125727_result.json`
- **Structured JSON:** [`b1565efc6332b2dec042.json`](../../sessions/b1/b1565efc6332b2dec042.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. API 连通性
- **模型列表接口** (`GET /models`): HTTP 200，正常返回 358 个模型
- **Chat Completions 接口**: **HTTP 403** — `"This model is not available in your region."`
- 无论走代理还是直连，出口 IP 都是中国（116.172.96.185，宁夏），被 OpenRouter 区域封锁

### 2. 目标模型 OpenRouter ID

| 目标 | OpenRouter ID | 状态 | Prompt/Completion 价格 (/M tokens) |
|------|--------------|------|-----------------------------------|
| gpt-4o | `openai/gpt-4o` | 存在 | $2.50 / $10.00 |
| gpt-4o-mini | `openai/gpt-4o-mini` | 存在 | $0.15 / $0.60 |
| gpt-4.1 | `openai/gpt-4.1` | 存在 | $2.00 / $8.00 |
| claude-sonnet-4 | `anthropic/claude-sonnet-4` | 存在 | $3.00 / $15.00 |
| claude-opus-4 | `anthropic/claude-opus-4` | 存在 | $15.00 / $75.00 |
| claude-3-haiku | `anthropic/claude-3-haiku` | 存在 | $0.25 / $1.25 |
| gemini-2.5-pro | `google/gemini-2.5-pro` | 存在 | $1.25 / $10.00 |
| gemini-2.5-flash | `google/gemini-2.5-flash` | 存在 | $0.30 / $2.50 |

### 3. 不可用模型
- **gpt-5.5**: OpenRouter 上存在 `openai/gpt-5.5` 和 `openai/gpt-5.5-pro`（非你列的 ID，但可用）
- **gpt-4.5**: **不存在**，OpenRouter 已无此模型

### 4. 核心问题
**所有模型的 chat completions 调用均返回 403 区域限制。** AutoDL 服务器（无论走代理还是直连）出口 IP 都在中国大陆，OpenRouter 对中国 IP 封锁了推理接口。

**解决方案**：需要一个非中国出口的代理/VPN，或改用不限区域的 API 服务（如直接用各厂商官方 API + 国内代理转发）。

---
