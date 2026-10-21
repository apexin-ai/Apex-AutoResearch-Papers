# infra api model probe

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_api-model-probe_20260522T033428_result.json`
- **Structured JSON:** [`62e834dffd8d066e7800.json`](../../sessions/62/62e834dffd8d066e7800.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

API 可用。以下是探测结果：

## 探测报告

### 1. API endpoint 可达性
- **可达**，地址 `http://47.94.22.126/v1`
- **需要 API key**：`Authorization: [REDACTED] 使用 OpenAI 兼容格式

### 2. 完整模型列表（仅 chat 模型，按家族分类）

| 家族 | 模型 |
|------|------|
| GPT-3.5 | gpt-3.5-turbo, gpt-3.5-turbo-16k, gpt-3.5-turbo-0125, gpt-3.5-turbo-1106 |
| GPT-4 | gpt-4, gpt-4-0613, gpt-4-turbo, gpt-4-turbo-2024-04-09 |
| GPT-4o | gpt-4o, gpt-4o-mini, gpt-4o-2024-05-13, gpt-4o-2024-08-06, gpt-4o-2024-11-20 |
| GPT-4.1 | gpt-4.1, gpt-4.1-mini, gpt-4.1-nano |
| GPT-5 | gpt-5, gpt-5-mini, gpt-5-nano, gpt-5-pro |
| GPT-5.1~5.5 | gpt-5.1, gpt-5.2, gpt-5.2-pro, gpt-5.4, gpt-5.4-pro, gpt-5.4-mini, gpt-5.4-nano, gpt-5.5, gpt-5.5-pro |
| o-series | o1, o1-pro, o3, o3-mini, o4-mini |
| Embedding | text-embedding-ada-002, text-embedding-3-small, text-embedding-3-large |
| Audio/TTS | whisper-1, tts-1, gpt-4o-mini-tts, gpt-audio 等 |
| Image | gpt-image-1, gpt-image-1-mini, gpt-image-2 |
| Search | gpt-4o-search-preview, gpt-5-search-api |

### 3. 优先选择的模型（用于实验）

**注意：全部是 OpenAI 模型，没有 Claude / Gemini / DeepSeek。** 在可用范围内选择不同代际/能力层次：

| 优先级 | 模型 | 理由 |
|--------|------|------|
| 1 | **gpt-4o-mini** | 便宜快速，已验证可用 |
| 2 | **gpt-4o** | 强能力基线 |
| 3 | **o4-mini** | reasoning 模型，不同推理范式 |
| 4 | **gpt-4.1-mini** | 较新架构 |
| 5 | **gpt-5.4-mini** | 最新一代小模型 |
| 6 | **gpt-5.5** | 最新最强 |

### 4. 测试结果
`gpt-4o-mini` 请求成功，响应正常（返回 "Hello! How can I assist you today?"），延迟 ~3s。

---
