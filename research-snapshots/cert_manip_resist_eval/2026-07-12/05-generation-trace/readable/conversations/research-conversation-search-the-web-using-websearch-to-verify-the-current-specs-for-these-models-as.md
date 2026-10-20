# Research conversation: Search the web (using WebSearch) to verify the current specs for these models as of May 2026: 1. DeepSeek V4-Pro - is it

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a59a0ee9de1ecb7a5.jsonl`
- **Structured JSON:** [`9697abc5f4039988c299.json`](../../sessions/96/9697abc5f4039988c299.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-19T09:44:08.189Z_

Search the web (using WebSearch) to verify the current specs for these models as of May 2026:
1. DeepSeek V4-Pro - is it 1.6T MoE? When released?
2. Kimi K2.6 - is it 1T MoE? When released?
3. GLM-5 - is it 745B MoE? When released?
4. Gemma 4 31B - confirmed specs?

Just give me a brief factual summary of each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "981eb41c-cc98-461c-bf39-d4d8e38239f0",
  "agentId": "a59a0ee9de1ecb7a5",
  "type": "user",
  "uuid": "1ac22d99-4437-4966-99f6-878e4b6c89b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T09:44:08.196Z_

```json
{
  "parentUuid": "1ac22d99-4437-4966-99f6-878e4b6c89b9",
  "isSidechain": true,
  "agentId": "a59a0ee9de1ecb7a5",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "28defb0c-7155-4820-b863-7debc8d74f8b",
  "timestamp": "2026-05-19T09:44:08.196Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-19T09:44:09.149Z_

I'll search for the current specifications for these AI models as of May 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28defb0c-7155-4820-b863-7debc8d74f8b",
  "isSidechain": true,
  "agentId": "a59a0ee9de1ecb7a5",
  "requestId": "req_011CbBiE53zegsp1jGMrFVAX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29f1130a-c120-4a8b-96bf-600ff9bb40ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019KPa4ScHJ2VZ79bqD439YV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13251,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13251,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T09:44:09.355Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KZgpTrCvwHPrJ5dvBFHcDE`</summary>

```json
{
  "query": "DeepSeek V4-Pro specs MoE release date 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29f1130a-c120-4a8b-96bf-600ff9bb40ea",
  "isSidechain": true,
  "agentId": "a59a0ee9de1ecb7a5",
  "requestId": "req_011CbBiE53zegsp1jGMrFVAX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "495cce8e-6911-415c-871c-7acf6afa361e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019KPa4ScHJ2VZ79bqD439YV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13251,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13251,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T09:44:09.569Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RLu1GRJUQkhACxyzM8mgMk`</summary>

```json
{
  "query": "Kimi K2.6 specs MoE release date 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "495cce8e-6911-415c-871c-7acf6afa361e",
  "isSidechain": true,
  "agentId": "a59a0ee9de1ecb7a5",
  "requestId": "req_011CbBiE53zegsp1jGMrFVAX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33ff5c30-d02d-4c54-bafc-2e505c93e7be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019KPa4ScHJ2VZ79bqD439YV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13251,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13251,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T09:44:09.764Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LHHgJ6ByyhJz9dtFLAXYJS`</summary>

```json
{
  "query": "GLM-5 specs MoE parameters release date 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33ff5c30-d02d-4c54-bafc-2e505c93e7be",
  "isSidechain": true,
  "agentId": "a59a0ee9de1ecb7a5",
  "requestId": "req_011CbBiE53zegsp1jGMrFVAX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be9eda3c-cd01-45c4-9e4e-5abd11bc3678",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019KPa4ScHJ2VZ79bqD439YV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13251,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13251,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T09:44:09.856Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GLyLqqfK18twx3AJ8UH43v`</summary>

```json
{
  "query": "Gemma 4 31B specs release date 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be9eda3c-cd01-45c4-9e4e-5abd11bc3678",
  "isSidechain": true,
  "agentId": "a59a0ee9de1ecb7a5",
  "requestId": "req_011CbBiE53zegsp1jGMrFVAX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf7e3fba-2630-4507-9f05-023072417bc0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019KPa4ScHJ2VZ79bqD439YV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13251,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13251,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T09:44:15.377Z_

<details><summary>↩ Tool result · `toolu_01KZgpTrCvwHPrJ5dvBFHcDE`</summary>

```text
Web search results for query: "DeepSeek V4-Pro specs MoE release date 2026"

Links: [{"title":"deepseek-ai/DeepSeek-V4-Pro · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"},{"title":"DeepSeek V4 Pro: Model Overview, Features & Performance Guide","url":"https://deepinfra.com/blog/deepseek-v4-pro-model-overview"},{"title":"DeepSeek V4 Pro Review & Pricing 2026","url":"https://codersera.com/blog/deepseek-v4-pro-review-benchmarks-pricing-2026/"},{"title":"DeepSeek V4 (1.6T MoE, Multimodal) | Guides | Clore.ai","url":"https://docs.clore.ai/guides/language-models/deepseek-v4"},{"title":"DeepSeek V4 (2026): Specs, Benchmarks, API Pricing, and Architecture Guide | Morph","url":"https://www.morphllm.com/deepseek-v4"},{"title":"DeepSeek V4 (2026): 1T Parameters, 81% SWE-bench, $0.30/MTok — Full Specs | NxCode","url":"https://www.nxcode.io/resources/news/deepseek-v4-release-specs-benchmarks-2026"},{"title":"deepseek-ai / deepseek-v4-pro","url":"https://docs.api.nvidia.com/nim/reference/deepseek-ai-deepseek-v4-pro"},{"title":"DeepSeek V4 Released: 1.6T Open-Source, 1M Context, MIT","url":"https://www.modemguides.com/blogs/ai-news/deepseek-v4-pro-flash-open-source-release"},{"title":"DeepSeek V4 Launches: 1.6T MoE, 1M Context, 10% KV","url":"https://www.digitalapplied.com/blog/deepseek-v4-preview-launch-1m-context-efficiency"},{"title":"DeepSeek V4: Features, Benchmarks & API Pricing (2026)","url":"https://ghost.codersera.com/blog/deepseek-v4-release-date-features-benchmarks/"}]

Based on the search results, here's comprehensive information about DeepSeek V4-Pro:

## Release Date

DeepSeek V4 Pro was released on April 24, 2026 under the MIT license.

## MoE Architecture & Specs

DeepSeek-V4-Pro is a Mixture-of-Experts (MoE) language model with 1.6 trillion total parameters and 49 billion activated parameters, supporting a context length of one million tokens.

## Key Architectural Features

The V4 series incorporates a hybrid attention mechanism combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) to dramatically improve long-context efficiency.

In the 1M-token context setting, DeepSeek-V4-Pro requires only 27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2.

## Two-Model Release

DeepSeek-V4-Pro is designed for advanced reasoning, complex software engineering, and long-running agentic tasks, and arrives alongside DeepSeek-V4-Flash, a lighter 284B-parameter variant built for faster, lower-cost inference.

## Availability

The models are available as open-source weights on Hugging Face and through the DeepSeek API, with both supporting configurable reasoning modes (Non-Think, Think High, and Think Max).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "495cce8e-6911-415c-871c-7acf6afa361e",
  "isSidechain": true,
  "promptId": "981eb41c-cc98-461c-bf39-d4d8e38239f0",
  "agentId": "a59a0ee9de1ecb7a5",
  "type": "user",
  "uuid": "6be3055a-21f4-4311-a478-826a909e999b",
  "sourceToolAssistantUUID": "495cce8e-6911-415c-871c-7acf6afa361e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T09:44:16.116Z_

<details><summary>↩ Tool result · `toolu_01RLu1GRJUQkhACxyzM8mgMk`</summary>

```text
Web search results for query: "Kimi K2.6 specs MoE release date 2026"

Links: [{"title":"Kimi K2.6 Model Overview: Architecture, Features & Capabilities","url":"https://deepinfra.com/blog/kimi-k2-6-model-overview"},{"title":"Kimi K2.6: Complete Guide (2026)","url":"https://codersera.com/blog/kimi-k2-6-complete-guide-2026/"},{"title":"How to Use Kimi K2.6: Complete Guide to Moonshot AI's New 1T-Parameter Open-Source Coding Model | Tosea.ai","url":"https://tosea.ai/blog/kimi-k2-6-complete-guide"},{"title":"Kimi K2.6 Code Preview Benchmark Results, Specs & Pricing | DataLearnerAI","url":"https://www.datalearner.com/en/ai-models/pretrained-models/kimi-k2.6-code-preview"},{"title":"Kimi K2.6 Officially Released: The Agentic Coding Era Enters Production","url":"https://kimi-k2.org/blog/24-kimi-k2-6-release"},{"title":"What Is Kimi K2.6? Moonshot AI's Open-Weight Agent Model Explained - Verdent Guides","url":"https://www.verdent.ai/guides/what-is-kimi-k2-6"},{"title":"Kimi K2.6 Benchmark Results, Specs & Pricing | DataLearnerAI","url":"https://www.datalearner.com/en/ai-models/pretrained-models/kimi-k2-6"},{"title":"Kimi K2.6 Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/kimi-k2.6"},{"title":"Kimi K2.6 is here: the open model that refuses to clock out | WhatLLM.org","url":"https://whatllm.org/blog/kimi-k2-6"},{"title":"Kimi K2.6 is Now on Overchat AI | AI Hub","url":"https://overchat.ai/ai-hub/kimi-k2-6"}]

Based on the search results, here's the information about Kimi K2.6 specs and release date:

## Release Date
Kimi K2.6 was released on April 20, 2026 by Moonshot AI under a Modified MIT license.

## Architecture & Specs
It is a native multimodal agentic model built on a 1-trillion parameter Mixture-of-Experts (MoE) architecture, with 32 billion parameters activated per token.

Key architectural details include:
- A sparse Mixture-of-Experts design with 384 total experts, of which 8 are routed per token plus 1 shared expert, giving it the parameter breadth of a 1T-parameter model at the inference cost of roughly a 32B dense model.
- 262K context window and open weights under a Modified MIT license.

## Key Features
Kimi K2.6 includes an Agent Swarm system that scales to 300 domain-specialized sub-agents, executing up to 4,000 coordinated steps in a single autonomous run — up from 100 sub-agents and 1,500 steps in K2.5.

Native video input is a notable addition, with K2.5 handling images while K2.6 adds video (mp4, mov, avi, webm, and others, recommended up to 2K resolution).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33ff5c30-d02d-4c54-bafc-2e505c93e7be",
  "isSidechain": true,
  "promptId": "981eb41c-cc98-461c-bf39-d4d8e38239f0",
  "agentId": "a59a0ee9de1ecb7a5",
  "type": "user",
  "uuid": "f99d32de-a753-4a4b-a339-c3dc161ba900",
  "sourceToolAssistantUUID": "33ff5c30-d02d-4c54-bafc-2e505c93e7be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T09:44:16.333Z_

<details><summary>↩ Tool result · `toolu_01GLyLqqfK18twx3AJ8UH43v`</summary>

```text
Web search results for query: "Gemma 4 31B specs release date 2026"

Links: [{"title":"Gemma 4 31B - Specs & Pricing [2026]","url":"https://getdeploying.com/llms/gemma-4-31b"},{"title":"google/gemma-4-31B · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B"},{"title":"Gemma 4: How a 31B Model Beats 400B Rivals [2026]","url":"https://tech-insider.org/google-gemma-4-open-model-benchmarks-2026/"},{"title":"Gemma 4 31B Model Specs, Costs & Benchmarks (April 2026) | Galaxy.ai","url":"https://blog.galaxy.ai/model/gemma-4-31b-it"},{"title":"Gemma 4 by Google: Specs, Benchmarks, Model Sizes, and How to Run It Locally (2026 Guide)","url":"https://aurigait.com/blog/gemma-4-features-benchmarks-guide/"},{"title":"Gemma 4: A Practical Guide for Developers - DEV Community","url":"https://dev.to/arshtechpro/gemma-4-a-practical-guide-for-developers-2co5"},{"title":"Google Gemma 4 Developer Guide: Benchmarks & Local Setup | Lushbinary","url":"https://lushbinary.com/blog/gemma-4-developer-guide-benchmarks-architecture-local-deployment-2026/"},{"title":"gemma-4-31b-it Model by Google | NVIDIA NIM","url":"https://build.nvidia.com/google/gemma-4-31b-it/modelcard"},{"title":"Gemma 4 31B IT by Google on Vercel AI Gateway, Specs, Pricing & API","url":"https://vercel.com/ai-gateway/models/gemma-4-31b-it"},{"title":"Gemma 4 31B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/gemma-4-31b"}]

Based on the web search results, here's what I found about Gemma 4 31B:

## Release Date
Gemma 4 31B was released on April 2, 2026, making it Google's latest and largest dense model in the Gemma 4 family.

## Key Specifications

**Model Size & Architecture:**
- The model contains 30.7B parameters
- All 31B parameters are active during every forward pass (dense architecture, not mixture-of-experts)

**Context Window & Languages:**
- Context window of 256K tokens
- Supports over 140 languages with cultural context understanding

**Multimodal Capabilities:**
- Accepts image and video input
- Supports text, image, and video input formats

**License:**
- Open-weight under Apache 2.0

## Performance Benchmarks
- Scores 89.2% on AIME 2026
- Scores 85.2% on MMLU Pro
- Ranks 3rd among all open models on the Arena AI text leaderboard with an estimated score of 1452

## Special Features
- Built-in reasoning mode that lets the model think step-by-step before answering
- Optimized for consumer GPUs


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf7e3fba-2630-4507-9f05-023072417bc0",
  "isSidechain": true,
  "promptId": "981eb41c-cc98-461c-bf39-d4d8e38239f0",
  "agentId": "a59a0ee9de1ecb7a5",
  "type": "user",
  "uuid": "08e7f90e-8c82-49f0-8e46-2516438f3a8c",
  "sourceToolAssistantUUID": "bf7e3fba-2630-4507-9f05-023072417bc0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T09:44:17.001Z_

<details><summary>↩ Tool result · `toolu_01LHHgJ6ByyhJz9dtFLAXYJS`</summary>

```text
Web search results for query: "GLM-5 specs MoE parameters release date 2026"

Links: [{"title":"GLM-5.1: #1 Open Source AI Model? Full Review (2026)","url":"https://www.buildfastwithai.com/blogs/glm-5-1-open-source-review-2026"},{"title":"GLM-5 Deep Dive: 745B MoE Beast Crushing SWE-Bench (Code + Benchmarks) | by Sai Dheeraj Gummadi | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/glm-5-deep-dive-745b-moe-beast-crushing-swe-bench-code-benchmarks-5757a3022251"},{"title":"Deploy GLM-5.1 on GPU Cloud: Self-Host the 754B MoE Model (2026 Guide) | Spheron Blog","url":"https://www.spheron.network/blog/deploy-glm-5-1-gpu-cloud/"},{"title":"GLM-5.1 Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/glm-5.1"},{"title":"GLM 5.0 | GLM 5 Verified Specs & MoE Architecture (GLM5)","url":"https://glm5.xyz/"},{"title":"Mastering GLM-5 API Calls: 5-Minute Getting Started Guide for the 744B MoE Open Source Flagship Model - Apiyi.com Blog","url":"https://help.apiyi.com/en/glm-5-api-guide-744b-moe-agent-tutorial-en.html"},{"title":"GLM-5 - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/glm-5"},{"title":"GLM-5.1 Review: Open-Source Model Tops SWE-Bench Pro | Awesome Agents","url":"https://awesomeagents.ai/reviews/review-glm-5-1/"},{"title":"GLM-5.1 - Model Info, Parameters, Benchmarks - SiliconFlow\"","url":"https://www.siliconflow.com/models/glm-5-1"},{"title":"GLM-5 Release Status: What’s Available Now - Verdent Guides","url":"https://www.verdent.ai/guides/glm-5-release-tracker-status"}]

Based on the web search results, here's what I found about GLM-5 specs, MoE parameters, and release dates in 2026:

## GLM-5 Release Timeline

GLM-5 is Zhipu AI's (Z.ai) latest flagship large language model, released on February 11, 2026. GLM-5.1 is an open-source AI model released by Z.ai (formerly Zhipu AI) on April 7, 2026, which is a post-training upgrade to the base GLM-5 model.

## MoE Architecture & Parameters

**GLM-5 (base model):**
With 744B total parameters in a Mixture of Experts (MoE) setup activating only ~40–44B per inference, it delivers frontier-level performance in complex system tasks while keeping costs low. Parameters: 744–745B total; 40–44B active per token (MoE with 256 experts, top-8 activated ~5.9% sparsity).

**GLM-5.1 (refined version):**
GLM-5.1 is built on a 754-billion parameter Mixture-of-Experts (MoE) architecture with 40 billion active parameters per token, a 200,000 token context window, and the ability to generate up to 128,000 output tokens in a single response.

## Key Technical Specs

Context Window: 200K input tokens; up to 128K output tokens. Attention Mechanism: Integrates DeepSeek Sparse Attention (DSA) for lossless long-context handling at reduced compute/token efficiency.

Both models use the MIT license and are designed for agentic engineering and long-horizon coding tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be9eda3c-cd01-45c4-9e4e-5abd11bc3678",
  "isSidechain": true,
  "promptId": "981eb41c-cc98-461c-bf39-d4d8e38239f0",
  "agentId": "a59a0ee9de1ecb7a5",
  "type": "user",
  "uuid": "b6184039-3618-47a6-b3c0-566e3f3e1120",
  "sourceToolAssistantUUID": "be9eda3c-cd01-45c4-9e4e-5abd11bc3678",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T09:44:22.135Z_

## Summary

**1. DeepSeek V4-Pro** — Confirmed 1.6T MoE with 49B activated parameters. Released April 24, 2026 under MIT license. Supports 1M context window with efficient attention mechanisms.

**2. Kimi K2.6** — Confirmed 1T MoE architecture with 32B activated parameters. Released April 20, 2026 by Moonshot AI under Modified MIT license. Features 262K context window and agent swarm system for up to 300 domain-specialized sub-agents.

**3. GLM-5** — Confirmed 745B (also cited as 744B or 754B in variants) MoE architecture with 40-44B activated parameters. Base GLM-5 released February 11, 2026; GLM-5.1 (refined version) released April 7, 2026. Both under MIT license with 200K context window.

**4. Gemma 4 31B** — Confirmed 30.7B dense (NOT MoE) parameters, all active during inference. Released April 2, 2026 by Google under Apache 2.0. Features 256K context window, multimodal input (image/video), and step-by-step reasoning mode.

Sources:
- [DeepSeek V4 on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [Kimi K2.6 Model Overview](https://deepinfra.com/blog/kimi-k2-6-model-overview)
- [GLM-5 Deep Dive](https://medium.com/data-science-in-your-pocket/glm-5-deep-dive-745b-moe-beast-crushing-swe-bench-code-benchmarks-5757a3022251)
- [Gemma 4 31B Specs](https://getdeploying.com/llms/gemma-4-31b)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6184039-3618-47a6-b3c0-566e3f3e1120",
  "isSidechain": true,
  "agentId": "a59a0ee9de1ecb7a5",
  "requestId": "req_011CbBiEifS2keBDvV5y7Bs4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a83264a9-5fc8-4024-ac5d-06bd7d84c1db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "94059999-277e-4cd9-8c73-4bb52522c5d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GaazsM9JgLqbntEDtaTwym",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 870,
      "cache_creation_input_tokens": 3178,
      "cache_read_input_tokens": 13251,
      "output_tokens": 477,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3178
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 870,
          "output_tokens": 477,
          "cache_read_input_tokens": 13251,
          "cache_creation_input_tokens": 3178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3178,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
