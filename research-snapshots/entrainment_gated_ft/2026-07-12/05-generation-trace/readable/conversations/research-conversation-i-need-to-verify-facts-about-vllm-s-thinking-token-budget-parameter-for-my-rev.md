# Research conversation: I need to verify facts about vLLM's thinking_token_budget parameter for my review of a paper. Please search for: 1. Does

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ae0e20c6a7fbe24a8.jsonl`
- **Structured JSON:** [`27b3a6211ef93d553ce3.json`](../../sessions/27/27b3a6211ef93d553ce3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-09T20:39:46.635Z_

I need to verify facts about vLLM's thinking_token_budget parameter for my review of a paper. Please search for:

1. Does vLLM have a thinking_token_budget parameter in SamplingParams? When was it added?
2. Is vLLM v0.19.0 or v0.20.1 a real version that exists? (The paper was written in early May 2026, so these versions should exist or be expected soon)
3. Search "vllm thinking_token_budget SamplingParams" to verify the API exists
4. Search "vllm 0.19" OR "vllm 0.20" changelog to check if these versions exist
5. Check github.com/vllm-project/vllm for thinking_token_budget

Also check: Does vLLM support per-request thinking_token_budget at all? The paper claims this is a native vLLM feature.

Report what you find about vLLM's actual support for this parameter.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "79e9f3ae-a839-4911-aceb-136b450e9e4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-09T20:39:47.588Z_

I'll help you verify the facts about vLLM's thinking_token_budget parameter. Let me search for this information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79e9f3ae-a839-4911-aceb-136b450e9e4d",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011Case8infubRFopqV4KJnN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7c1a3df-c21b-4dab-8080-0713fea361e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0159Hx5dNeHS7wBGo617D4Hp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-09T20:39:47.803Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QC21brmijFA2gf4Q5qTBZQ`</summary>

```json
{
  "query": "vLLM thinking_token_budget SamplingParams"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7c1a3df-c21b-4dab-8080-0713fea361e4",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011Case8infubRFopqV4KJnN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7893c36c-f1a6-4a51-b90f-d3dbd879f016",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0159Hx5dNeHS7wBGo617D4Hp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-09T20:39:48.005Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012iDZeHDE7tgUk4EMUxPcsP`</summary>

```json
{
  "query": "vLLM v0.19 v0.20 changelog releases"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7893c36c-f1a6-4a51-b90f-d3dbd879f016",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011Case8infubRFopqV4KJnN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a343e30a-7e25-4f78-a6de-41185d7356b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0159Hx5dNeHS7wBGo617D4Hp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-09T20:39:48.451Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VqhAsJXzFZXkkKK4mViEn5`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm",
  "prompt": "Does vLLM support thinking_token_budget parameter? Check releases and documentation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a343e30a-7e25-4f78-a6de-41185d7356b3",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011Case8infubRFopqV4KJnN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6c02ed48-cd3d-4392-8a2e-46c548fde15e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0159Hx5dNeHS7wBGo617D4Hp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-09T20:39:48.613Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NtCifBxaMzVhexx8cto7AR`</summary>

```json
{
  "query": "vLLM per-request thinking_token_budget native feature"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c02ed48-cd3d-4392-8a2e-46c548fde15e",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011Case8infubRFopqV4KJnN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5155cd47-e636-421d-820e-40acc73ab70a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0159Hx5dNeHS7wBGo617D4Hp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 16155,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 273,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 658,
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

_source line 7 · 2026-05-09T20:39:52.413Z_

<details><summary>↩ Tool result · `toolu_01VqhAsJXzFZXkkKK4mViEn5`</summary>

```text
# vLLM and thinking_token_budget Parameter

Based on the GitHub repository content provided, there is **no mention of a `thinking_token_budget` parameter** in vLLM's documentation or release notes.

The page shows vLLM as "a fast and easy-to-use library for LLM inference and serving" with extensive features like PagedAttention, quantization options, and speculative decoding. However, the excerpt does not reference any thinking token budget functionality.

To determine if this parameter exists, you would need to:
- Check the [official documentation](https://docs.vllm.ai)
- Review the latest [release notes](https://github.com/vllm-project/vllm/releases)
- Search the repository directly for this specific parameter

The content provided is insufficient to confirm whether vLLM supports this feature.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c02ed48-cd3d-4392-8a2e-46c548fde15e",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "69a739e1-2a41-4e82-bc36-03f7b2d22fbb",
  "sourceToolAssistantUUID": "6c02ed48-cd3d-4392-8a2e-46c548fde15e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-09T20:39:54.529Z_

<details><summary>↩ Tool result · `toolu_01NtCifBxaMzVhexx8cto7AR`</summary>

```text
Web search results for query: "vLLM per-request thinking_token_budget native feature"

Links: [{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"Reasoning Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/reasoning_outputs/"},{"title":"thinking_budget_state - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/v1/sample/thinking_budget_state/"},{"title":"Gemma 4 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html"},{"title":"[Feature]: GLM thinking budget · Issue #26091 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/26091"},{"title":"Adding Reasoning Budget to vLLM (Reasoning Token Limit) – Shuyo's Weblog","url":"https://shuyo.wordpress.com/2026/03/26/adding-reasoning-budget-to-vllm-reasoning-token-limit/"},{"title":"Understanding vLLM Scheduling: Token Budgets, Chunked Prefill, and Policies | by Audrey Wang | Mar, 2026 | Medium","url":"https://audreywongkg.medium.com/understanding-vllm-scheduling-token-budgets-chunked-prefill-and-policies-2c879e3980e3"},{"title":"[Feature]: Add Support for thinking_budget for Qwen3 Models · Issue #17887 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17887"},{"title":"BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens","url":"https://arxiv.org/html/2508.17196v1"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - #2 by RunLLM - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533/2"}]

Based on the search results, here's what I found about vLLM's `thinking_token_budget` as a native feature:

## Overview

vLLM has `thinking_token_budget` as a sampling parameter that sets the per-request reasoning token limit. Once the reasoning token count reaches the configured thinking_token_budget, vLLM forces the model to produce reasoning_end_str, effectively terminating the reasoning block.

## Implementation Details

The feature implements per-batch thinking token budget state applied after penalties at sample time, tracking thinking sections and forcing end tokens when budget is exceeded. Per-request state tracks nesting depth (handles `&lt;think>` in prompt), counts reasoning tokens, and switches to injection mode when budget is exceeded.

## Model Support

Some models, such as Qwen3, DeepSeek, and Nemotron3, support a thinking budget that limits the maximum number of tokens used for reasoning.

## Usage Example

You can use `thinking_token_budget` in chat completion requests, and it's also available as a SamplingParams parameter when using the Python API.

## Availability Note

The ability to cap reasoning tokens via thinking_token_budget was added in later PRs and is available in vLLM mainline after those merges, meaning this is a relatively recent feature addition to the codebase.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5155cd47-e636-421d-820e-40acc73ab70a",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "21b6ac01-7ddc-44cc-82cb-1de49ddcc5f1",
  "sourceToolAssistantUUID": "5155cd47-e636-421d-820e-40acc73ab70a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-09T20:39:54.951Z_

<details><summary>↩ Tool result · `toolu_01QC21brmijFA2gf4Q5qTBZQ`</summary>

```text
Web search results for query: "vLLM thinking_token_budget SamplingParams"

Links: [{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"Reasoning Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/reasoning_outputs/"},{"title":"How to pass `thinking_budget` for Qwen-3 Thinking models in offline AsyncLLMEngine? · Issue #25714 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/25714"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - #2 by RunLLM - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533/2"},{"title":"recipes/Google/Gemma4.md at main · vllm-project/recipes","url":"https://github.com/vllm-project/recipes/blob/main/Google/Gemma4.md"},{"title":"Inference Parameters — vLLM","url":"https://docs.vllm.ai/en/v0.8.4/api/inference_params.html"},{"title":"Gemma 4 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html"},{"title":"Sampling Parameters — vLLM","url":"https://docs.vllm.ai/en/v0.6.4/dev/sampling_params.html"},{"title":"vllm/vllm/sampling_params.py at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/blob/main/vllm/sampling_params.py"},{"title":"Understanding vLLM Scheduling: Token Budgets, Chunked Prefill, and Policies | by Audrey Wang | Mar, 2026 | Medium","url":"https://audreywongkg.medium.com/understanding-vllm-scheduling-token-budgets-chunked-prefill-and-policies-2c879e3980e3"}]

Based on the search results, here's what I found about `vLLM thinking_token_budget` and `SamplingParams`:

## Overview

vLLM's `SamplingParams` supports a `thinking_token_budget` parameter that can be used to cap reasoning tokens. This feature is used with reasoning models that generate internal thinking tokens.

## Usage

You can pass `thinking_token_budget` as a parameter to `SamplingParams` like this: `SamplingParams(thinking_token_budget=10)`. 

This parameter can also be passed in OpenAI-compatible chat completion requests with the field name `thinking_token_budget`.

## Implementation Notes

A reasoning_budget (similar to thinking_token_budget) introduces a way to cap the number of tokens generated within `&lt;think>...&lt;/think>` blocks, with a `ReasoningBudgetLogitsProcessor` handling the token counting and injection of a stop message when the budget is exceeded.

The `reasoning_end_str` can include a transition phrase before the reasoning end token, instructing the model to emit that phrase when the budget is exhausted, making the reasoning termination more natural.

## Important Compatibility Note

`thinking_token_budget` is not a native SamplingParams field in vLLM v0.18.0 and is not enforced if passed via extra_args; it only works when supported as a first-class parameter.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7893c36c-f1a6-4a51-b90f-d3dbd879f016",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "f91f0ab1-36cc-4ccb-8c39-ac30b87ea6b7",
  "sourceToolAssistantUUID": "7893c36c-f1a6-4a51-b90f-d3dbd879f016",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-09T20:39:56.597Z_

<details><summary>↩ Tool result · `toolu_012iDZeHDE7tgUk4EMUxPcsP`</summary>

```text
Web search results for query: "vLLM v0.19 v0.20 changelog releases"

Links: [{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"vLLM Release Notes - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html"},{"title":"vllm · PyPI","url":"https://pypi.org/project/vllm/"},{"title":"Release v0.19.0 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases/tag/v0.19.0"},{"title":"Releases · vllm-project/vllm-ascend","url":"https://github.com/vllm-project/vllm-ascend/releases"},{"title":"Previous vLLM Releases | vLLM","url":"https://vllm.ai/releases"},{"title":"vllm-project/vllm v0.19.0 on GitHub","url":"https://newreleases.io/project/github/vllm-project/vllm/release/v0.19.0"},{"title":"Release Notes — vllm-ascend","url":"https://docs.vllm.ai/projects/ascend/en/main/user_guide/release_notes.html"},{"title":"vLLM on X: \"vLLM v0.20.0 is here! 752 commits from 320 contributors (123 new). 🎉 Highlights: DeepSeek V4, Hunyuan v3 preview support, CUDA 13 / PyTorch 2.11 / Transformers v5 baseline, FA4 as default MLA prefill, TurboQuant 2-bit KV (4× capacity), vLLM IR foundation. Thread 👇 https://t.co/ZMpMWgGTHM\" / X","url":"https://x.com/vllm_project/status/2048918629144805619"},{"title":"vLLM release April 2026 release notes: v0.18.0, v0.19.0, and v0.19.1rc0 decoded, and the single Swift line that points a Mac agent at one","url":"https://fazm.ai/t/vllm-release-april-2026-release-notes"}]

Based on the search results, here's a summary of the vLLM v0.19 and v0.20 changelog releases:

## vLLM v0.19.0

This release features 448 commits from 197 contributors (54 new).

**Key highlights:**

- Gemma 4 support: Full Google Gemma 4 architecture support including MoE, multimodal, reasoning, and tool-use capabilities
- Zero-bubble async scheduling + speculative decoding: Async scheduling now supports speculative decoding with zero-bubble overlap, significantly improving throughput
- Model Runner V2 maturation: MRV2 gains piecewise CUDA graphs for pipeline parallelism, spec decode rejection sampler with greedy/logprobs support, multi-modal embeddings for spec decode, streaming inputs, and EPLB support
- ViT Full CUDA Graphs: Vision encoders (ViT) now support full CUDA graph capture for reduced overhead
- Transformers v5 compatibility across many models

## vLLM v0.20.0

752 commits from 320 contributors (123 new), with highlights including DeepSeek V4, Hunyuan v3 preview support, CUDA 13 / PyTorch 2.11 / Transformers v5 baseline, FA4 as default MLA prefill, TurboQuant 2-bit KV (4× capacity), and vLLM IR foundation.

CUDA 13.0 default: Default CUDA wheel on PyPI and vllm/vllm-openai:v0.20.0 image switched to CUDA 13.0.

PyTorch 2.11 upgrade: vLLM ships on torch 2.11 for CUDA, and XPU is now also on torch 2.11.

For more detailed information, you can visit the official GitHub releases page at https://github.com/vllm-project/vllm/releases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a343e30a-7e25-4f78-a6de-41185d7356b3",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "6474fb4b-03ac-4f63-9703-9bfccde0118e",
  "sourceToolAssistantUUID": "a343e30a-7e25-4f78-a6de-41185d7356b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-09T20:39:58.782Z_

Let me get more specific information about when this feature was added and check the actual SamplingParams implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6474fb4b-03ac-4f63-9703-9bfccde0118e",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011Case9TSierwyzD1wi3ALD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6bc705d1-da08-4364-af6e-8f3e6c534f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RhDH8VpfYsM6qage9Ug53b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1195,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 16813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-09T20:39:59.424Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Bu1Y7h7GKTrnUnJ1uWe76F`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/blob/main/vllm/sampling_params.py",
  "prompt": "Does this file contain thinking_token_budget parameter? When was it added?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bc705d1-da08-4364-af6e-8f3e6c534f66",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011Case9TSierwyzD1wi3ALD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3fbea797-c14a-4533-b07c-a492fac58886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RhDH8VpfYsM6qage9Ug53b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1195,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 16813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-09T20:39:59.628Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F7AumfudcasK4Ri7ARQMpc`</summary>

```json
{
  "url": "https://docs.vllm.ai/en/latest/features/reasoning_outputs/",
  "prompt": "What is the thinking_token_budget parameter and how does it work?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fbea797-c14a-4533-b07c-a492fac58886",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011Case9TSierwyzD1wi3ALD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "34a63fce-ed45-44f2-8518-4410efd9eb09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RhDH8VpfYsM6qage9Ug53b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1195,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 16813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-09T20:40:00.304Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014EQEEVVRUuT9CwrDrUQDim`</summary>

```json
{
  "query": "\"vLLM\" \"thinking_token_budget\" \"v0.18\" OR \"v0.19\" OR \"v0.20\" when added"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34a63fce-ed45-44f2-8518-4410efd9eb09",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011Case9TSierwyzD1wi3ALD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f3cecb2b-f979-4c47-931d-7836c980e382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RhDH8VpfYsM6qage9Ug53b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1195,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 16813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-09T20:40:00.404Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WSdXAPFPqThTSwpjjy7sCA`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/pull/37112",
  "prompt": "When was reasoning_budget/thinking_token_budget added? What PR merged it?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3cecb2b-f979-4c47-931d-7836c980e382",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011Case9TSierwyzD1wi3ALD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "44ccc9b1-c80c-43f9-9fb3-31b0dcbee18c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RhDH8VpfYsM6qage9Ug53b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1195,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 16813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-09T20:40:03.846Z_

<details><summary>↩ Tool result · `toolu_01F7AumfudcasK4Ri7ARQMpc`</summary>

````text
# Understanding thinking_token_budget

The `thinking_token_budget` parameter is a sampling feature that limits the maximum number of tokens used for reasoning in models like Qwen3, DeepSeek, and Nemotron3.

## How It Works

When you set a `thinking_token_budget`, vLLM counts tokens starting from the `reasoning_start_str` marker. Once the reasoning token count reaches your specified budget, the system forces the model to output `reasoning_end_str`, effectively terminating the reasoning block.

## Usage

You can apply this parameter in two ways:

**For online serving**, include it in API requests:
```json
"thinking_token_budget": 10
```

**For offline inference**, pass it through `SamplingParams`:
```python
sampling_params = SamplingParams(thinking_token_budget=10)
```

## Important Note

If you don't specify `thinking_token_budget`, no explicit reasoning limit applies beyond standard generation constraints like `max_tokens`. The feature requires `--reasoning-parser` to be enabled and optionally uses `--reasoning-config` to define the boundary tokens that mark where reasoning begins and ends.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34a63fce-ed45-44f2-8518-4410efd9eb09",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "dbad718c-c758-4989-a88e-6f9d5f9def81",
  "sourceToolAssistantUUID": "34a63fce-ed45-44f2-8518-4410efd9eb09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-09T20:40:04.341Z_

<details><summary>↩ Tool result · `toolu_01Bu1Y7h7GKTrnUnJ1uWe76F`</summary>

```text
# Response

Yes, this file contains the `thinking_token_budget` parameter. It appears in the `SamplingParams` class definition with this description:

"Maximum number of tokens allowed for thinking operations."

However, **the webpage content provided does not include git history or commit information that would indicate when this parameter was added**. To find the addition date, you would need to check the file's git history on GitHub or review the project's changelog/release notes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fbea797-c14a-4533-b07c-a492fac58886",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "dcd704e3-7e85-4ef8-8dda-212dc25c400a",
  "sourceToolAssistantUUID": "3fbea797-c14a-4533-b07c-a492fac58886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-09T20:40:04.360Z_

<details><summary>↩ Tool result · `toolu_01WSdXAPFPqThTSwpjjy7sCA`</summary>

```text
Based on the content provided, **PR #37112 was closed without being merged**. The original feature was merged through **PR #20859** instead.

The key evidence: njhill (a maintainer) commented on March 24, 2026: "Thanks @abhinand5. I've merged the original PR." This refers to PR #20859, which had been open since July 2025. The abhinand5 PR (#37112) was subsequently closed on March 29, 2026, with the author stating: "closing the PR" after the original was already merged.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44ccc9b1-c80c-43f9-9fb3-31b0dcbee18c",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "cc8bf9bb-4981-46aa-9558-94a9408eff1c",
  "sourceToolAssistantUUID": "44ccc9b1-c80c-43f9-9fb3-31b0dcbee18c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-09T20:40:06.560Z_

<details><summary>↩ Tool result · `toolu_014EQEEVVRUuT9CwrDrUQDim`</summary>

```text
Web search results for query: ""vLLM" "thinking_token_budget" "v0.18" OR "v0.19" OR "v0.20" when added"

Links: [{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533"},{"title":"[Bug]: Thinking token budget not enforced with MTP speculative decoding (works without MTP) · Issue #39573 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/39573"},{"title":"Adding Reasoning Budget to vLLM (Reasoning Token Limit) – Shuyo's Weblog","url":"https://shuyo.wordpress.com/2026/03/26/adding-reasoning-budget-to-vllm-reasoning-token-limit/"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - #2 by RunLLM - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533/2"},{"title":"thinking_budget_state - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/v1/sample/thinking_budget_state/"},{"title":"[Bug]: Qwen3.5 `thinking_token_budget` causes `reasoning_end_str` to leak into `content` field · Issue #39697 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/39697"},{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"[Feature]: GLM thinking budget · Issue #26091 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/26091"},{"title":"Thinking Token limit setting - General - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-limit-setting/2400"},{"title":"Gemma 4 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html"}]

Based on the search results, here's what I found about `thinking_token_budget` in vLLM versions 0.18-0.20:

## Status by Version

**vLLM v0.18.0:** thinking_token_budget is not a native SamplingParams field in vLLM v0.18.0 and is not enforced if passed via extra_args. The feature was not natively supported in this version.

**vLLM v0.19.0 and later:** The ability to cap reasoning tokens via thinking_token_budget (or reasoning_budget) was added in later PRs (e.g., #20859, #37112) and is available in vLLM mainline after those merges.

## Feature Implementation

A reasoning_budget parameter was added that allows capping reasoning tokens, which can be passed via API requests like curl http://localhost:8000/v1/chat/completions with "reasoning_budget": 50.

## Known Issues

More recent versions have had some issues with the feature:
- Thinking token budget (introduced in PR #20859) is not enforced when MTP speculative decoding is enabled in vLLM v0.19.0
- Issues with reasoning_end_str leaking into content field when using thinking_token_budget have been reported in newer versions

The feature appears to have been added between v0.18 and v0.19, with ongoing refinements in later versions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3cecb2b-f979-4c47-931d-7836c980e382",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "b7e47c4e-9e07-4a37-a75c-a32167d5523f",
  "sourceToolAssistantUUID": "f3cecb2b-f979-4c47-931d-7836c980e382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-09T20:40:07.964Z_

Now let me check for the exact timeline and PR #20859 details:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7e47c4e-9e07-4a37-a75c-a32167d5523f",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseACcGVmseicWPjEemp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "070d672a-99d2-4240-8a86-aba8c66c7f5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VYFgJm16WoGgPCiVVXVHkE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 159,
      "cache_creation_input_tokens": 3162,
      "cache_read_input_tokens": 19982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3162,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-09T20:40:08.383Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PxyRqpAGpWU8Zf3YPY8UND`</summary>

```json
{
  "query": "vLLM PR 20859 thinking_token_budget merged when 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "070d672a-99d2-4240-8a86-aba8c66c7f5a",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseACcGVmseicWPjEemp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e3742660-c850-4413-882f-83ea353b670e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VYFgJm16WoGgPCiVVXVHkE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 159,
      "cache_creation_input_tokens": 3162,
      "cache_read_input_tokens": 19982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3162,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-09T20:40:08.460Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HbDgreTQQcwwuu5Qxc1tWR`</summary>

```json
{
  "query": "vLLM v0.20.1 release version exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3742660-c850-4413-882f-83ea353b670e",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseACcGVmseicWPjEemp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf4b7848-f194-4420-94f2-60e8c97fc520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VYFgJm16WoGgPCiVVXVHkE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 159,
      "cache_creation_input_tokens": 3162,
      "cache_read_input_tokens": 19982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3162,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-09T20:40:11.850Z_

<details><summary>↩ Tool result · `toolu_01PxyRqpAGpWU8Zf3YPY8UND`</summary>

```text
Web search results for query: "vLLM PR 20859 thinking_token_budget merged when 2026"

Links: [{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"[Bug]: Thinking token budget not enforced with MTP speculative decoding (works without MTP) · Issue #39573 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/39573"},{"title":"Adding Reasoning Budget to vLLM (Reasoning Token Limit) – Shuyo's Weblog","url":"https://shuyo.wordpress.com/2026/03/26/adding-reasoning-budget-to-vllm-reasoning-token-limit/"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - #2 by RunLLM - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533/2"},{"title":"Understanding vLLM Scheduling: Token Budgets, Chunked Prefill, and Policies | by Audrey Wang | Mar, 2026 | Medium","url":"https://audreywongkg.medium.com/understanding-vllm-scheduling-token-budgets-chunked-prefill-and-policies-2c879e3980e3"},{"title":"thinking_budget_state - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/v1/sample/thinking_budget_state/"},{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"[Feature]: GLM thinking budget · Issue #26091 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/26091"},{"title":"[VLM] Enable tokenized inputs for merged multi-modal processor by DarkLight1337 · Pull Request #11900 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/11900"},{"title":"[Bug]: Qwen3.5 `thinking_token_budget` causes `reasoning_end_str` to leak into `content` field · Issue #39697 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/39697"}]

Based on the search results, vLLM PR #20859 "Limit thinking tokens (hard limit)" was merged on March 15, 2026.

The PR introduced functionality to cap thinking tokens (also referred to as reasoning tokens). The feature "Limit thinking tokens (hard limit) (#20859)" is included in the released features, and PR #20859 had been open since July 2025 before being merged.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3742660-c850-4413-882f-83ea353b670e",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "16f04636-fb77-4852-b396-ef6718ae473c",
  "sourceToolAssistantUUID": "e3742660-c850-4413-882f-83ea353b670e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-09T20:40:12.198Z_

<details><summary>↩ Tool result · `toolu_01HbDgreTQQcwwuu5Qxc1tWR`</summary>

```text
Web search results for query: "vLLM v0.20.1 release version exists"

Links: [{"title":"Release v0.20.1 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases/tag/v0.20.1"},{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"vllm · PyPI","url":"https://pypi.org/project/vllm/"},{"title":"Release v0.20.0 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases/tag/v0.20.0"},{"title":"v0.20.0 - vLLM","url":"https://docs.vllm.ai/en/v0.20.0/"},{"title":"vllm-project/vllm v0.20.0 on GitHub","url":"https://newreleases.io/project/github/vllm-project/vllm/release/v0.20.0"},{"title":"vLLM on X: \"vLLM v0.20.0 is here! 752 commits from 320 contributors (123 new). 🎉 Highlights: DeepSeek V4, Hunyuan v3 preview support, CUDA 13 / PyTorch 2.11 / Transformers v5 baseline, FA4 as default MLA prefill, TurboQuant 2-bit KV (4× capacity), vLLM IR foundation. Thread 👇 https://t.co/ZMpMWgGTHM\" / X","url":"https://x.com/vllm_project/status/2048918629144805619"},{"title":"vLLM - Browse /v0.20.1 at SourceForge.net","url":"https://sourceforge.net/projects/vllm.mirror/files/v0.20.1/"},{"title":"vLLM Release Notes - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html"},{"title":"GPU - vLLM-Omni","url":"https://docs.vllm.ai/projects/vllm-omni/en/latest/getting_started/installation/gpu/"}]

Yes, vLLM v0.20.1 exists as a patch release on top of v0.20.0 primarily focused on DeepSeek V4 stabilization and performance improvements, along with several important bug fixes. The release is available on PyPI with distribution files including vllm-0.20.1.tar.gz and various wheel files.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf4b7848-f194-4420-94f2-60e8c97fc520",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "112c20f3-fcac-4d8c-9590-5ded3f451840",
  "sourceToolAssistantUUID": "bf4b7848-f194-4420-94f2-60e8c97fc520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-09T20:40:13.647Z_

Perfect! Now let me verify v0.19.0 as well and get more details about the reasoning outputs:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "112c20f3-fcac-4d8c-9590-5ded3f451840",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseAbyhoZKdfdAV7fgET",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e5a741fd-6e3d-47ba-a635-f4bb4227feee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WHwiMW7MChkiQo2C1Jsf5M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1854,
      "cache_read_input_tokens": 23144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1854,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-09T20:40:14.292Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Jgy2YzsqhNxHoqbairYV3j`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/releases/tag/v0.19.0",
  "prompt": "When was v0.19.0 released? Does it mention thinking_token_budget or reasoning_budget?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5a741fd-6e3d-47ba-a635-f4bb4227feee",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseAbyhoZKdfdAV7fgET",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "662984a4-4df1-4121-b8f3-6b7a68dd0665",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WHwiMW7MChkiQo2C1Jsf5M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1854,
      "cache_read_input_tokens": 23144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1854,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-09T20:40:14.476Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L9DmPgfnavrXaUEx6GPvDF`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/releases/tag/v0.20.1",
  "prompt": "When was v0.20.1 released? Does it mention thinking_token_budget?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "662984a4-4df1-4121-b8f3-6b7a68dd0665",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseAbyhoZKdfdAV7fgET",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b1c724c8-324f-47b8-a2d6-db81aca133b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WHwiMW7MChkiQo2C1Jsf5M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1854,
      "cache_read_input_tokens": 23144,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1854
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 240,
          "cache_read_input_tokens": 23144,
          "cache_creation_input_tokens": 1854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1854,
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

_source line 28 · 2026-05-09T20:40:17.240Z_

<details><summary>↩ Tool result · `toolu_01L9DmPgfnavrXaUEx6GPvDF`</summary>

```text
# vLLM v0.20.1 Release Information

**Release Date:** May 4, 2024

According to the GitHub release page, "@khluu released this 04 May 10:36" UTC.

**Regarding `thinking_token_budget`:** No, the release notes do not mention `thinking_token_budget` at all. The patch release focused primarily on "DeepSeek V4 stabilization and performance improvements" along with various bug fixes, but this specific parameter is not discussed in the documented changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1c724c8-324f-47b8-a2d6-db81aca133b2",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "3241e076-ac4c-4556-ba99-cb00983d29a8",
  "sourceToolAssistantUUID": "b1c724c8-324f-47b8-a2d6-db81aca133b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-09T20:40:17.811Z_

<details><summary>↩ Tool result · `toolu_01Jgy2YzsqhNxHoqbairYV3j`</summary>

```text
# vLLM v0.19.0 Release Details

**Release Date:** April 3, 2024

According to the page, the release was published by @khluu on "03 Apr 02:19."

**Regarding thinking_token_budget or reasoning_budget:**

No, the release notes do not mention `thinking_token_budget` or `reasoning_budget`. The only reference to reasoning-related features is: "Limit thinking tokens (hard limit)" under the API & Frontend section, which appears as a feature addition but doesn't specify those particular parameter names in the documentation provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "662984a4-4df1-4121-b8f3-6b7a68dd0665",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "ae806fd0-51bf-42f8-97f5-61ea51fce8ec",
  "sourceToolAssistantUUID": "662984a4-4df1-4121-b8f3-6b7a68dd0665",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-09T20:40:18.978Z_

The dates returned appear to be incorrect (showing 2024 instead of 2026). Let me search more specifically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae806fd0-51bf-42f8-97f5-61ea51fce8ec",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseB1wbfrzsVxDtzkzNh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2e7e98ff-f4c4-400b-b526-8c58e7373f6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WeuYbHXZ5g3sZabbhFnNa2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 149,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 24998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 408,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-09T20:40:19.604Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Udmg3zbNzkdbWCSmvishE`</summary>

```json
{
  "query": "\"v0.19.0\" vLLM \"April 2026\" OR \"May 2026\" release date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e7e98ff-f4c4-400b-b526-8c58e7373f6a",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseB1wbfrzsVxDtzkzNh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ae750f29-0973-49c9-a27f-660261476ce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WeuYbHXZ5g3sZabbhFnNa2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 149,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 24998,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 408
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 149,
          "output_tokens": 158,
          "cache_read_input_tokens": 24998,
          "cache_creation_input_tokens": 408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 408,
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

_source line 32 · 2026-05-09T20:40:19.618Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nw7oZXUuxeyT4hrKJYNGTD`</summary>

```json
{
  "query": "\"v0.20.1\" vLLM \"May 2026\" release date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae750f29-0973-49c9-a27f-660261476ce2",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseB1wbfrzsVxDtzkzNh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5ce7c61d-f0ef-4da6-a0cf-d173274d2bc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WeuYbHXZ5g3sZabbhFnNa2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 149,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 24998,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 408
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 149,
          "output_tokens": 158,
          "cache_read_input_tokens": 24998,
          "cache_creation_input_tokens": 408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 408,
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

_source line 33 · 2026-05-09T20:40:23.759Z_

<details><summary>↩ Tool result · `toolu_019Udmg3zbNzkdbWCSmvishE`</summary>

```text
Web search results for query: ""v0.19.0" vLLM "April 2026" OR "May 2026" release date"

Links: [{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"vLLM Release Notes - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html"},{"title":"Release v0.19.0 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases/tag/v0.19.0"},{"title":"vLLM release 2026 update: three ships in 14 days, and why upgrading yours means zero changes to your Mac agent","url":"https://fazm.ai/t/vllm-release-2026-update"},{"title":"Previous vLLM Releases | vLLM","url":"https://vllm.ai/releases"},{"title":"vLLM release April 2026 release notes: v0.18.0, v0.19.0, and v0.19.1rc0 decoded, and the single Swift line that points a Mac agent at one","url":"https://fazm.ai/t/vllm-release-april-2026-release-notes"},{"title":"Release Notes — vllm-ascend","url":"https://docs.vllm.ai/projects/ascend/en/main/user_guide/release_notes.html"},{"title":"Versions | vllm | PyPI","url":"https://deps.dev/pypi/vllm/0.2.6/versions"},{"title":"vllm-project/vllm v0.19.0 on GitHub","url":"https://newreleases.io/project/github/vllm-project/vllm/release/v0.19.0"},{"title":"vllm · PyPI","url":"https://pypi.org/project/vllm/"}]

Based on the search results, I found information about the vLLM v0.19.0 release date:

v0.19.0 landed on April 2 with day-one Gemma 4 support. More specifically, the release occurred in April 2026, which aligns with your query timeframe.

The search results show this was a significant release that featured 448 commits from 197 contributors (54 new), with major highlights including full Google Gemma 4 architecture support including MoE, multimodal, reasoning, and tool-use capabilities, as well as improvements to the async scheduler and Model Runner V2.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae750f29-0973-49c9-a27f-660261476ce2",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "c7a8b132-6e62-46f0-98ad-0e8396713b0b",
  "sourceToolAssistantUUID": "ae750f29-0973-49c9-a27f-660261476ce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-09T20:40:24.014Z_

<details><summary>↩ Tool result · `toolu_01Nw7oZXUuxeyT4hrKJYNGTD`</summary>

```text
Web search results for query: ""v0.20.1" vLLM "May 2026" release date"

Links: [{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"vLLM Release Notes - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html"},{"title":"Releases · vllm-project/vllm - GitHub | Release Alert","url":"https://releasealert.dev/github/vllm-project/vllm"},{"title":"vllm · PyPI","url":"https://pypi.org/project/vllm/"},{"title":"Release v0.10.1 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases/tag/v0.10.1"},{"title":"Release v0.20.1 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases/tag/v0.20.1"},{"title":"v0.20.0 - vLLM","url":"https://docs.vllm.ai/en/v0.20.0/"},{"title":"Release v0.20.0 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases/tag/v0.20.0"},{"title":"vLLM - Browse /v0.20.1 at SourceForge.net","url":"https://sourceforge.net/projects/vllm.mirror/files/v0.20.1/"},{"title":"vLLM on X: \"vLLM v0.20.0 is here! 752 commits from 320 contributors (123 new). 🎉 Highlights: DeepSeek V4, Hunyuan v3 preview support, CUDA 13 / PyTorch 2.11 / Transformers v5 baseline, FA4 as default MLA prefill, TurboQuant 2-bit KV (4× capacity), vLLM IR foundation. Thread 👇 https://t.co/ZMpMWgGTHM\" / X","url":"https://x.com/vllm_project/status/2048918629144805619"}]

Based on the search results, I found information about vLLM v0.20.1:

v0.20.1 is a patch release on top of v0.20.0 primarily focused on DeepSeek V4 stabilization and performance improvements, along with several important bug fixes. 

While the search results don't provide an explicit release date for v0.20.1, one source indicates that the README was updated 2026-05-03, suggesting the release occurred around early May 2026. Additionally, the latest version v0.20.2 was last published on May 8, 2026, which places v0.20.1's release sometime before that date.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ce7c61d-f0ef-4da6-a0cf-d173274d2bc3",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "5eb51db4-c850-4aec-9796-642a604dee3d",
  "sourceToolAssistantUUID": "5ce7c61d-f0ef-4da6-a0cf-d173274d2bc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-09T20:40:25.951Z_

Excellent. Now let me verify the current status of thinking_token_budget in the latest versions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eb51db4-c850-4aec-9796-642a604dee3d",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseBUjALCbodqhBRJqj2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "998c9b5d-2122-4a39-b1f7-b8814daeac9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018Lg7z2PCf9JYkD7GeYQy1V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1791,
      "cache_read_input_tokens": 25406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1791,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-09T20:40:26.219Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017tGTFKVW7yyUUGkRZK8SaC`</summary>

```json
{
  "query": "vLLM thinking_token_budget SamplingParams latest version 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "998c9b5d-2122-4a39-b1f7-b8814daeac9e",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseBUjALCbodqhBRJqj2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "11ec1b62-0140-4700-a662-c6660a573a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018Lg7z2PCf9JYkD7GeYQy1V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1791,
      "cache_read_input_tokens": 25406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1791,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-09T20:40:32.583Z_

<details><summary>↩ Tool result · `toolu_017tGTFKVW7yyUUGkRZK8SaC`</summary>

```text
Web search results for query: "vLLM thinking_token_budget SamplingParams latest version 2026"

Links: [{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"Reasoning Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/reasoning_outputs/"},{"title":"sampling_params - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/sampling_params/"},{"title":"Understanding vLLM Scheduling: Token Budgets, Chunked Prefill, and Policies | by Audrey Wang | Mar, 2026 | Medium","url":"https://audreywongkg.medium.com/understanding-vllm-scheduling-token-budgets-chunked-prefill-and-policies-2c879e3980e3"},{"title":"Sampling Parameters — vLLM","url":"https://docs.vllm.ai/en/v0.6.4/dev/sampling_params.html"},{"title":"Adding Reasoning Budget to vLLM (Reasoning Token Limit) – Shuyo's Weblog","url":"https://shuyo.wordpress.com/2026/03/26/adding-reasoning-budget-to-vllm-reasoning-token-limit/"},{"title":"vllm/vllm/sampling_params.py at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/blob/main/vllm/sampling_params.py"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533"},{"title":"furiosa_llm.sampling_params — FuriosaAI Developer Center 2026.1.0 documentation","url":"https://developer.furiosa.ai/latest/en/_modules/furiosa_llm/sampling_params.html"},{"title":"Gemma 4 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html"}]

Based on the search results, here's what I found about vLLM's `thinking_token_budget` parameter in `SamplingParams` in 2026:

## Key Findings:

Some models, such as Qwen3, DeepSeek, and Nemotron3, support a thinking budget that limits the maximum number of tokens used for reasoning.

The `thinking_token_budget` parameter can be used in `SamplingParams`, as shown in the official vLLM documentation examples.

## Recent Implementation (2026):

A pull request introduced a `reasoning_budget` to cap the number of tokens generated within `&lt;think>...&lt;/think>` blocks. The implementation is well-integrated with the existing reasoning parser infrastructure, and a new `ReasoningBudgetLogitsProcessor` was added to handle the token counting and injection of a stop message when the budget is exceeded.

The feature was merged around March 15, 2026, with implementation of reasoning budget and messaging for chat completion and sampling parameters.

## How It Works:

When reasoning reaches a specified number of tokens, it inserts a message to prompt the termination of reasoning.

The latest version documentation shows that the `thinking_token_budget` can be passed as a parameter in API requests and in the `SamplingParams` class.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11ec1b62-0140-4700-a662-c6660a573a53",
  "isSidechain": true,
  "promptId": "a0e07855-e287-4ea8-b0a3-62fdbe8d160a",
  "agentId": "ae0e20c6a7fbe24a8",
  "type": "user",
  "uuid": "07822b30-3606-4408-ae94-c67079fe1dc8",
  "sourceToolAssistantUUID": "11ec1b62-0140-4700-a662-c6660a573a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-09T20:40:42.015Z_

Based on my comprehensive search, here's what I found about vLLM's `thinking_token_budget` parameter and the versions mentioned in the paper:

## Summary of Findings

### 1. Does vLLM have a `thinking_token_budget` parameter in SamplingParams?
**Yes** - vLLM has a `thinking_token_budget` parameter in `SamplingParams`. It's documented as "Maximum number of tokens allowed for thinking operations."

### 2. When was it added?
**March 15, 2026** - The feature was merged via PR #20859 ("Limit thinking tokens (hard limit)") on March 15, 2026. The PR had been in development since July 2025. Note that PR #37112 (another reasoning_budget PR) was closed on March 29, 2026, as a duplicate since the original functionality had already been merged.

### 3. Are versions v0.19.0 and v0.20.1 real?
**Yes, both are real versions that exist:**
- **v0.19.0** - Released April 2, 2026 (448 commits from 197 contributors). Features Gemma 4 support, async scheduling improvements, and Model Runner V2 maturation.
- **v0.20.1** - Released around May 3-4, 2026 (confirmed to exist on PyPI and GitHub). This is a patch release focusing on DeepSeek V4 stabilization and bug fixes.

Both versions are real and were released during the timeframe when the paper was written (early May 2026).

### 4. Is per-request `thinking_token_budget` a native vLLM feature?
**Yes** - vLLM supports per-request `thinking_token_budget` as a native feature. You can:
- Pass it in API requests: `"thinking_token_budget": 10`
- Use it in `SamplingParams`: `SamplingParams(thinking_token_budget=10)`
- It's supported in online serving (OpenAI-compatible chat completions) and offline inference

### 5. Important Compatibility Notes
- **v0.18.0** - The feature is NOT a native SamplingParams field and is silently ignored if passed via extra_args
- **v0.19.0 and later** - The feature IS fully supported as a native parameter after the March 15, 2026 merge

### 6. Known Issues
- In v0.19.0, thinking token budget is not enforced when MTP (Multi-Token Prediction) speculative decoding is enabled (Issue #39573)
- In newer versions, there are issues with `reasoning_end_str` leaking into the content field (Issue #39697)

### Verification Conclusion
The paper's claims about vLLM supporting native per-request `thinking_token_budget` in v0.19.0 and v0.20.1 are **technically accurate** - the feature exists as a native SamplingParams parameter in both versions. However, there are important caveats: the feature was only merged on March 15, 2026, and there are known bugs with certain decoding strategies and output formatting.

Sources:
- [vLLM Reasoning Outputs Documentation](https://docs.vllm.ai/en/latest/features/reasoning_outputs/)
- [vLLM SamplingParams API](https://docs.vllm.ai/en/latest/api/vllm/sampling_params/)
- [PR #37112: Add reasoning_budget](https://github.com/vllm-project/vllm/pull/37112)
- [PR #20859: Limit thinking tokens (merged March 15, 2026)](https://github.com/vllm-project/vllm/pull/20859)
- [Release v0.19.0](https://github.com/vllm-project/vllm/releases/tag/v0.19.0)
- [Release v0.20.1](https://github.com/vllm-project/vllm/releases/tag/v0.20.1)
- [vLLM Forum: thinking_token_budget in v0.18.0](https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533)
- [Issue #39573: Thinking token budget with MTP speculative decoding](https://github.com/vllm-project/vllm/issues/39573)
- [Understanding vLLM Scheduling (March 2026 Article)](https://audreywongkg.medium.com/understanding-vllm-scheduling-token-budgets-chunked-prefill-and-policies-2c879e3980e3)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07822b30-3606-4408-ae94-c67079fe1dc8",
  "isSidechain": true,
  "agentId": "ae0e20c6a7fbe24a8",
  "requestId": "req_011CaseC78RdbkC4Yv2mioDx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a2403e31-482c-4062-88cc-2638d15d243f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e4688cc-f562-4b26-8ec8-d1f666534745",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MySVoHB2RTKKLLcMTJAad2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1146,
      "cache_read_input_tokens": 27197,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1146
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1140,
          "cache_read_input_tokens": 27197,
          "cache_creation_input_tokens": 1146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1146,
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
