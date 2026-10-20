# Research conversation: Search for DeepSeek V4 Pro API pricing. Specifically: 1. Does "DeepSeek V4 Pro" exist? Or is it "DeepSeek-V3" or somethi

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a58547d8258137022.jsonl`
- **Structured JSON:** [`223792dbdf4dac75d363.json`](../../sessions/22/223792dbdf4dac75d363.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

9 recorded events

### User

_source line 1 · 2026-05-10T19:06:55.172Z_

Search for DeepSeek V4 Pro API pricing. Specifically:
1. Does "DeepSeek V4 Pro" exist? Or is it "DeepSeek-V3" or something else?
2. What is the current promotional pricing?
3. When does the promotional pricing expire?
4. What is the standard pricing?

Search: "DeepSeek V4 Pro API pricing" and "DeepSeek API pricing 2026" and "DeepSeek promotional pricing May 2026"

Report findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "302e9c8f-60f8-4f8a-9c96-184dcca47d43",
  "agentId": "a58547d8258137022",
  "type": "user",
  "uuid": "17c019b4-c0ac-4891-b51e-2a16a54860ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T19:06:56.266Z_

I'll search for information about DeepSeek API pricing, focusing on the current offerings and promotional details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17c019b4-c0ac-4891-b51e-2a16a54860ec",
  "isSidechain": true,
  "agentId": "a58547d8258137022",
  "requestId": "req_011CauQrwLGxit8nBaob6ED6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a9ca8d49-b47a-49ff-9d59-2230362dce02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CXN2xTGnB2bumqPdjvVB9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 545,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T19:06:56.271Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cmyogt7CBMSVSYt3H8Rzqb`</summary>

```json
{
  "query": "DeepSeek V4 Pro API pricing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9ca8d49-b47a-49ff-9d59-2230362dce02",
  "isSidechain": true,
  "agentId": "a58547d8258137022",
  "requestId": "req_011CauQrwLGxit8nBaob6ED6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b8414856-995d-4cc1-bb05-02846fa2fa41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CXN2xTGnB2bumqPdjvVB9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 545,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:06:56.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01APvFiNSkXw25jrdGUEMKvr`</summary>

```json
{
  "query": "DeepSeek API pricing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8414856-995d-4cc1-bb05-02846fa2fa41",
  "isSidechain": true,
  "agentId": "a58547d8258137022",
  "requestId": "req_011CauQrwLGxit8nBaob6ED6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "05b2922a-aeb6-463d-b015-aaf46e6105f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CXN2xTGnB2bumqPdjvVB9c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 13789,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 545
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 545,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T19:06:56.536Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01REmR7ihKtV8f6wz1DyTwFB`</summary>

```json
{
  "query": "DeepSeek promotional pricing May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05b2922a-aeb6-463d-b015-aaf46e6105f3",
  "isSidechain": true,
  "agentId": "a58547d8258137022",
  "requestId": "req_011CauQrwLGxit8nBaob6ED6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "caf5892a-458b-4809-b2b6-3510c1293cf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CXN2xTGnB2bumqPdjvVB9c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 13789,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 545
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 545,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-10T19:07:02.453Z_

<details><summary>↩ Tool result · `toolu_01REmR7ihKtV8f6wz1DyTwFB`</summary>

```text
Web search results for query: "DeepSeek promotional pricing May 2026"

Links: [{"title":"DeepSeek Pricing 2026: API Cost, Free Tier & Plans Guide","url":"https://felloai.com/deepseek-pricing/"},{"title":"Models & Pricing | DeepSeek API Docs","url":"https://api-docs.deepseek.com/quick_start/pricing"},{"title":"Current DeepSeek API Pricing 2026: V4 Flash & Pro Cost per 1M Tokens - DevTk.AI","url":"https://devtk.ai/en/blog/deepseek-api-pricing-guide-2026/"},{"title":"DeepSeek V4 API Pricing Guide 2026: Flash vs Pro Cost Comparison, Cache Hit Math & Setup","url":"https://ofox.ai/blog/deepseek-api-pricing-guide-2026/"},{"title":"DeepSeek API Pricing 2026: The Cheapest AI API | AI Pricing Guru","url":"https://www.aipricing.guru/deepseek-pricing/"},{"title":"DeepSeek Launches 75% Price Reduction on V4-Pro AI Model Through 2026 - Computing.net","url":"https://computing.net/news/stocks/deepseek-launches-75-price-reduction-on-v4-pro-ai-model-through-2026/"},{"title":"DeepSeek V4 Pro API Pricing 2026: Official V4 Prices per 1M Tokens","url":"https://devtk.ai/en/models/deepseek-v4/"},{"title":"DeepSeek cuts V4-Pro prices by 75%","url":"https://thenextweb.com/news/deepseek-v4-pro-price-cut-75-percent"},{"title":"Deepseek API Pricing (Updated 2026) – All Models & Token Costs","url":"https://pricepertoken.com/pricing-page/provider/deepseek"},{"title":"DeepSeek API Pricing Calculator & Cost Guide (May 2026)","url":"https://costgoat.com/pricing/deepseek-api"}]

Based on the search results, here's what I found about DeepSeek promotional pricing in May 2026:

## Current Promotional Pricing

The deepseek-v4-pro model is currently offered at a 75% discount, extended until 2026/05/31 15:59 UTC.

### V4 Pro Discounted Pricing
DeepSeek V4 Pro is currently 75% off until May 5, 2026: $0.435/M input and $0.87/M output. After the promotional period ends, prices will rise to $1.74 and $3.48 after May 5, 2026.

Note: There appears to be a discrepancy in sources regarding the exact end date—some sources indicate May 5, 2026, while the official DeepSeek API documentation states the discount extends until May 31, 2026 at 15:59 UTC.

### V4 Flash Pricing
DeepSeek V4 Flash costs $0.14 per million input tokens (cache miss) and $0.28 per million output tokens.

### Additional Cache Discounts
Beyond the V4 Pro promotional pricing, DeepSeek simultaneously introduced a 90% reduction for input cache hit charges throughout its complete API portfolio, with this adjustment becoming effective immediately.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caf5892a-458b-4809-b2b6-3510c1293cf1",
  "isSidechain": true,
  "promptId": "302e9c8f-60f8-4f8a-9c96-184dcca47d43",
  "agentId": "a58547d8258137022",
  "type": "user",
  "uuid": "9cf9149b-b11a-4036-ac25-7bcd947d1f18",
  "sourceToolAssistantUUID": "caf5892a-458b-4809-b2b6-3510c1293cf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-10T19:07:03.508Z_

<details><summary>↩ Tool result · `toolu_01APvFiNSkXw25jrdGUEMKvr`</summary>

```text
Web search results for query: "DeepSeek API pricing 2026"

Links: [{"title":"Models & Pricing | DeepSeek API Docs","url":"https://api-docs.deepseek.com/quick_start/pricing"},{"title":"Current DeepSeek API Pricing 2026: V4 Flash & Pro Cost per 1M Tokens - DevTk.AI","url":"https://devtk.ai/en/blog/deepseek-api-pricing-guide-2026/"},{"title":"DeepSeek API Pricing Calculator & Cost Guide (May 2026)","url":"https://costgoat.com/pricing/deepseek-api"},{"title":"pricing-details-usd | DeepSeek API Docs","url":"https://api-docs.deepseek.com/quick_start/pricing-details-usd"},{"title":"DeepSeek AI Pricing - Free Chat & Affordable API | 2025 Guide","url":"https://deepseek.ai/pricing"},{"title":"DeepSeek API Pricing 2026 — Cheapest LLM ($0.14/M Input) | TLDL | TLDL","url":"https://www.tldl.io/resources/deepseek-api-pricing"},{"title":"DeepSeek API Pricing 2026: Complete Cost Guide (V4, R1 & Chat) | NxCode","url":"https://www.nxcode.io/resources/news/deepseek-api-pricing-complete-guide-2026"},{"title":"Deepseek API Pricing (Updated 2026) – All Models & Token Costs","url":"https://pricepertoken.com/pricing-page/provider/deepseek"},{"title":"DeepSeek API Pricing: V4 Flash, V4 Pro, Cache Hit, Cache Miss & Output Costs","url":"https://chat-deep.ai/pricing/"},{"title":"DeepSeek API Pricing 2026 — Model-by-Model Breakdown | MarginDash","url":"https://www.margindash.com/deepseek-api-pricing"}]

Based on the search results, here's the current DeepSeek API pricing for 2026:

## Current Models and Pricing

DeepSeek V4 Flash costs $0.0028/M cached input, $0.14/M cache-miss input, and $0.28/M output. DeepSeek V4 Pro is discounted to $0.003625/M cached input, $0.435/M cache-miss input, and $0.87/M output until 2026-05-31 15:59 UTC.

Additionally, DeepSeek V3.2 costs $0.28 per million input tokens and $0.42 per million output tokens, while the reasoning model DeepSeek R1 costs $0.70 per million input tokens and $2.50 per million output tokens.

## Key Updates

For all models, the input cache hit price has been reduced to 1/10 of the launch price, with this price adjustment taking effect from 2026/4/26 12:15 UTC.

Cache-hit input can be 50x cheaper than cache-miss input on V4 Flash, which represents a significant cost advantage for workloads that benefit from context caching.

DeepSeek offers a free tier with 5 million tokens with no credit card required to validate the service before committing to paid usage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05b2922a-aeb6-463d-b015-aaf46e6105f3",
  "isSidechain": true,
  "promptId": "302e9c8f-60f8-4f8a-9c96-184dcca47d43",
  "agentId": "a58547d8258137022",
  "type": "user",
  "uuid": "3fbf7e3c-fc91-48e4-86a6-2c74d0032d48",
  "sourceToolAssistantUUID": "05b2922a-aeb6-463d-b015-aaf46e6105f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T19:07:07.219Z_

<details><summary>↩ Tool result · `toolu_01Cmyogt7CBMSVSYt3H8Rzqb`</summary>

```text
Web search results for query: "DeepSeek V4 Pro API pricing"

Links: [{"title":"Models & Pricing | DeepSeek API Docs","url":"https://api-docs.deepseek.com/quick_start/pricing"},{"title":"DeepSeek V4 Pro - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/deepseek/deepseek-v4-pro"},{"title":"DeepSeek V4 Pro (Max) API Benchmarks: Latency, Throughput & Cost Analysis","url":"https://deepinfra.com/blog/deepseek-v4-pro-max-api-benchmarks-latency-throughput-cost"},{"title":"DeepSeek is back among the leading open weights models with V4 Pro and V4 Flash","url":"https://artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash"},{"title":"DeepSeek-V4-Pro API & Playground | Fireworks AI","url":"https://fireworks.ai/models/deepseek-ai/deepseek-v4-pro"},{"title":"DeepSeek V4—almost on the frontier, a fraction of the price","url":"https://simonwillison.net/2026/apr/24/deepseek-v4/"},{"title":"DeepSeek V4 Pro (High) - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/deepseek-v4-pro-high"},{"title":"DeepSeek V4 Pro API Pricing 2026: Official V4 Prices per 1M Tokens","url":"https://devtk.ai/en/models/deepseek-v4/"},{"title":"DeepSeek V4 API Guide: Pricing, Setup & Code Examples (2026) | NxCode","url":"https://www.nxcode.io/resources/news/deepseek-v4-api-guide-pricing-setup-2026"},{"title":"DeepSeek V4 Pricing: 20-50x Cheaper Than OpenAI (Cost Breakdown) | WaveSpeed Blog","url":"https://wavespeed.ai/blog/posts/blog-deepseek-v4-pricing-cost/"}]

Based on the search results, here's the current pricing information for DeepSeek V4 Pro API:

## Current Discounted Pricing

The deepseek-v4-pro model is currently offered at a 75% discount, extended until 2026/05/31 15:59 UTC.

With this discount, DeepSeek V4 Pro costs $0.435/M cache-miss input, $0.003625/M cached input, $0.87/M output.

## Regular List Pricing

List price is $1.74/M cache-miss input and $3.48/M output after the discount expires.

## Additional Details

- The model supports 1M context window with 384K max output
- Cache hit input token pricing is $0.145 for V4 Pro per 1M tokens at regular pricing
- For a blended rate (3:1 input to output ratio), this is $2.17 per 1M tokens at list price

The pricing can also vary slightly across different providers. The official DeepSeek API documentation is the most authoritative source for current pricing rates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8414856-995d-4cc1-bb05-02846fa2fa41",
  "isSidechain": true,
  "promptId": "302e9c8f-60f8-4f8a-9c96-184dcca47d43",
  "agentId": "a58547d8258137022",
  "type": "user",
  "uuid": "209b4121-aa2a-4d7b-b63c-31b2ac8b43b1",
  "sourceToolAssistantUUID": "b8414856-995d-4cc1-bb05-02846fa2fa41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T19:07:12.731Z_

## Findings

Based on my search results, here are the answers to your questions:

### 1. Does "DeepSeek V4 Pro" exist?

**Yes, DeepSeek V4 Pro exists.** DeepSeek released V4 models in April 2026, which includes:
- DeepSeek V4 Pro (the high-performance model)
- DeepSeek V4 Flash (the faster, more economical variant)

This is distinct from the earlier DeepSeek-V3.2 model.

### 2. Current Promotional Pricing

DeepSeek V4 Pro is currently offered at a **75% discount**:
- Input tokens (cache-miss): **$0.435 per million tokens**
- Output tokens: **$0.87 per million tokens**
- Cached input: **$0.003625 per million tokens** (additional 90% cache hit discount also applied)

### 3. Promotional Pricing Expiration

**May 31, 2026 at 15:59 UTC** (Note: There appears to be one source mentioning May 5, 2026, but the official DeepSeek API documentation confirms May 31, 2026)

### 4. Standard Pricing (After Promotion Ends)

- Input tokens (cache-miss): **$1.74 per million tokens**
- Output tokens: **$3.48 per million tokens**
- Cached input: **$0.145 per million tokens**

This represents approximately 4x the promotional pricing for standard input and output tokens.

---

Sources:
- [Models & Pricing | DeepSeek API Docs](https://api-docs.deepseek.com/quick_start/pricing)
- [DeepSeek V4 Pro API Pricing 2026: Official V4 Prices per 1M Tokens](https://devtk.ai/en/models/deepseek-v4/)
- [Current DeepSeek API Pricing 2026: V4 Flash & Pro Cost per 1M Tokens - DevTk.AI](https://devtk.ai/en/blog/deepseek-api-pricing-guide-2026/)
- [DeepSeek Launches 75% Price Reduction on V4-Pro AI Model Through 2026](https://computing.net/news/stocks/deepseek-launches-75-price-reduction-on-v4-pro-ai-model-through-2026/)
- [DeepSeek API Pricing Calculator & Cost Guide (May 2026)](https://costgoat.com/pricing/deepseek-api)
- [DeepSeek V4 API Guide: Pricing, Setup & Code Examples (2026) | NxCode](https://www.nxcode.io/resources/news/deepseek-v4-api-guide-pricing-setup-2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "209b4121-aa2a-4d7b-b63c-31b2ac8b43b1",
  "isSidechain": true,
  "agentId": "a58547d8258137022",
  "requestId": "req_011CauQspsN3sxigSxW1HSm7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c0020245-1235-4f77-96be-00341f18666a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AxVqn3T5r4t8gegpw8Ag8z",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1728,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 14334,
      "output_tokens": 679,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1832
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1728,
          "output_tokens": 679,
          "cache_read_input_tokens": 14334,
          "cache_creation_input_tokens": 1832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1832,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---
