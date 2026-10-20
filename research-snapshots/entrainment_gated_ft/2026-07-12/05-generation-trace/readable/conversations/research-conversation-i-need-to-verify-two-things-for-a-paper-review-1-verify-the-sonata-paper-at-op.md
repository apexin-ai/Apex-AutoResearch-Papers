# Research conversation: I need to verify two things for a paper review: 1. Verify the Sonata paper at openreview.net/pdf?id=2i6Rp0gCq6 - check i

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a080cedfb58bc3f30.jsonl`
- **Structured JSON:** [`9a3ffd179ea0ef0c7c99.json`](../../sessions/9a/9a3ffd179ea0ef0c7c99.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-09T21:32:08.157Z_

I need to verify two things for a paper review:

1. Verify the Sonata paper at openreview.net/pdf?id=2i6Rp0gCq6 - check if it actually exists and what it claims. Search for "Sonata dynamic thinking budget allocation reasoning models ICLR 2026" and "site:openreview.net Sonata thinking budget". Report the actual findings about this paper.

2. Verify vLLM's thinking_token_budget parameter status - search for "vLLM thinking_token_budget SamplingParams" and "vLLM per-request thinking budget parameter 2025 2026". Check if vLLM actually supports per-request thinking_token_budget as a native SamplingParams argument, and what version this was introduced in.

3. Also search for "TALE token budget aware LLM reasoning ACL 2025" to verify this paper exists.

4. Search for "SelfBudgeter arXiv 2505.11274 adaptive token allocation" to verify this paper.

Report actual findings with evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f42c4435-74a3-43b8-9fd9-c8b8f3b2cdbd",
  "agentId": "a080cedfb58bc3f30",
  "type": "user",
  "uuid": "64f545bc-c1e4-40e3-91f4-e6b71cf84f27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-09T21:32:09.272Z_

I'll help you verify these papers and the vLLM parameter. Let me search for each of these items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64f545bc-c1e4-40e3-91f4-e6b71cf84f27",
  "isSidechain": true,
  "agentId": "a080cedfb58bc3f30",
  "requestId": "req_011Casi8J5bKC6Y5AUQuhByk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa9d6b1b-9179-4840-a06a-653b0870dd47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CAAn7QdqH3no2WmGpwX6fw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-09T21:32:09.487Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L7KXQMg9KpM8d81pE8d1Ye`</summary>

```json
{
  "query": "Sonata dynamic thinking budget allocation reasoning models ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa9d6b1b-9179-4840-a06a-653b0870dd47",
  "isSidechain": true,
  "agentId": "a080cedfb58bc3f30",
  "requestId": "req_011Casi8J5bKC6Y5AUQuhByk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "53566cd0-852b-4d6c-bccf-08eca0ec74cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CAAn7QdqH3no2WmGpwX6fw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-09T21:32:09.705Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0183r5Z6a9WuB4mpwhHMAuDM`</summary>

```json
{
  "query": "site:openreview.net Sonata thinking budget"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53566cd0-852b-4d6c-bccf-08eca0ec74cd",
  "isSidechain": true,
  "agentId": "a080cedfb58bc3f30",
  "requestId": "req_011Casi8J5bKC6Y5AUQuhByk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "578cd78e-b54e-4b98-92eb-d6abf43ac4b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CAAn7QdqH3no2WmGpwX6fw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-09T21:32:09.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YHRPKiC9SBCEs8MXZDSvDH`</summary>

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
  "parentUuid": "578cd78e-b54e-4b98-92eb-d6abf43ac4b4",
  "isSidechain": true,
  "agentId": "a080cedfb58bc3f30",
  "requestId": "req_011Casi8J5bKC6Y5AUQuhByk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7e36d910-899e-415f-9d47-7c53625ed1b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CAAn7QdqH3no2WmGpwX6fw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-09T21:32:09.925Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MTEQRq6g3pVbphGaUdnVZn`</summary>

```json
{
  "query": "vLLM per-request thinking budget parameter 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e36d910-899e-415f-9d47-7c53625ed1b3",
  "isSidechain": true,
  "agentId": "a080cedfb58bc3f30",
  "requestId": "req_011Casi8J5bKC6Y5AUQuhByk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "128a210e-b539-423e-bc71-abc359dfd532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CAAn7QdqH3no2WmGpwX6fw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-09T21:32:10.132Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018AMrjDRV9PP2TfzX3vc13s`</summary>

```json
{
  "query": "TALE token budget aware LLM reasoning ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "128a210e-b539-423e-bc71-abc359dfd532",
  "isSidechain": true,
  "agentId": "a080cedfb58bc3f30",
  "requestId": "req_011Casi8J5bKC6Y5AUQuhByk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "15cc27e2-697b-4e31-94fc-532a3a3bf804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CAAn7QdqH3no2WmGpwX6fw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 676,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-09T21:32:10.225Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ERSY7tou38BpzuYpPGfLCY`</summary>

```json
{
  "query": "SelfBudgeter arXiv 2505.11274 adaptive token allocation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15cc27e2-697b-4e31-94fc-532a3a3bf804",
  "isSidechain": true,
  "agentId": "a080cedfb58bc3f30",
  "requestId": "req_011Casi8J5bKC6Y5AUQuhByk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8709161e-26b8-4f45-81eb-104b24086d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CAAn7QdqH3no2WmGpwX6fw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 16155,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 676
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 336,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 676,
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

_source line 9 · 2026-05-09T21:32:13.841Z_

<details><summary>↩ Tool result · `toolu_0183r5Z6a9WuB4mpwhHMAuDM`</summary>

```text
Web search results for query: "site:openreview.net Sonata thinking budget"

Links: [{"title":"HOW USER MEMORY ALTERS EMOTIONAL REASONING ...","url":"https://openreview.net/attachment?id=u9Qgn8xSx1&name=pdf"},{"title":"TRANSFORMERS AS INTRINSIC OPTIMIZERS","url":"https://openreview.net/pdf?id=UGB6JCl9lz"},{"title":"TREATMENT RULE OPTIMIZATION UNDER COUNTER","url":"https://openreview.net/attachment?id=jZffxvubJ9&name=pdf"},{"title":"Dormant Reasoning Circuits in RL-Trained Language Models","url":"https://openreview.net/pdf?id=mTjGBrkdtz"},{"title":"REVIEWERTOO: SHOULD AI JOIN THE PROGRAM COM","url":"https://openreview.net/pdf?id=RHby8yu1Tw"},{"title":"Better Test-Time Scaling by Unifying LLM Reasoners With ...","url":"https://openreview.net/pdf?id=kVOrGZM5N7"},{"title":"AuToMATo: An Out-Of-The-Box Persistence-Based Clus","url":"https://openreview.net/pdf?id=Qd7H5mAbzV"},{"title":"Careful at Estimation and Bold at Exploration for Deterministic...","url":"https://openreview.net/forum?id=3ukT8oODY0"},{"title":"Training Data Size Induced Double Descent For Denoising ...","url":"https://openreview.net/pdf?id=FdMWtpVT1I"},{"title":"Approximation to Smooth Functions by Low-Rank Swish ...","url":"https://openreview.net/pdf?id=ZWTb5UBdpG"}]

Based on the search results, I found one relevant result from OpenReview that mentions "Sonata thinking budget." In a paper on user memory and emotional reasoning, the thinking budget for Claude 3.7 Thinking was set to 16k.

The other search results mostly returned general metadata about papers on OpenReview without detailed content related to your specific query about "Sonata thinking budget." If you're looking for more specific information about Sonata or thinking budgets in particular papers, you may want to try a more targeted search or visit the OpenReview website directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "578cd78e-b54e-4b98-92eb-d6abf43ac4b4",
  "isSidechain": true,
  "promptId": "f42c4435-74a3-43b8-9fd9-c8b8f3b2cdbd",
  "agentId": "a080cedfb58bc3f30",
  "type": "user",
  "uuid": "07e675ba-d662-4a98-921b-8623bb42b7fa",
  "sourceToolAssistantUUID": "578cd78e-b54e-4b98-92eb-d6abf43ac4b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-09T21:32:16.163Z_

<details><summary>↩ Tool result · `toolu_01YHRPKiC9SBCEs8MXZDSvDH`</summary>

```text
Web search results for query: "vLLM thinking_token_budget SamplingParams"

Links: [{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"Reasoning Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/reasoning_outputs/"},{"title":"How to pass `thinking_budget` for Qwen-3 Thinking models in offline AsyncLLMEngine? · Issue #25714 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/25714"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - #2 by RunLLM - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533/2"},{"title":"recipes/Google/Gemma4.md at main · vllm-project/recipes","url":"https://github.com/vllm-project/recipes/blob/main/Google/Gemma4.md"},{"title":"Inference Parameters — vLLM","url":"https://docs.vllm.ai/en/v0.8.4/api/inference_params.html"},{"title":"Gemma 4 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html"},{"title":"Understanding vLLM Scheduling: Token Budgets, Chunked Prefill, and Policies | by Audrey Wang | Mar, 2026 | Medium","url":"https://audreywongkg.medium.com/understanding-vllm-scheduling-token-budgets-chunked-prefill-and-policies-2c879e3980e3"},{"title":"Sampling Parameters — vLLM","url":"https://docs.vllm.ai/en/v0.6.4/dev/sampling_params.html"},{"title":"vllm/vllm/sampling_params.py at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/blob/main/vllm/sampling_params.py"}]

Based on the search results, here's what I found about `vLLM`, `thinking_token_budget`, and `SamplingParams`:

## Overview

vLLM supports a `thinking_token_budget` parameter in `SamplingParams` that can be used to limit the number of tokens generated within reasoning/thinking blocks.

## Usage

There are two main ways to use this feature:

1. **OpenAI-compatible chat completion API**: You can pass `"thinking_token_budget": 10` in the request payload to the chat completions endpoint.

2. **Direct Python API**: You can set `sampling_params = SamplingParams(thinking_token_budget=10)` when creating sampling parameters.

## Implementation Details

The reasoning budget feature introduces functionality to cap the number of tokens generated within `&lt;think>...&lt;/think>` blocks, with a new `ReasoningBudgetLogitsProcessor` added to handle token counting and injection of a stop message when the budget is exceeded.

The `reasoning_end_str` parameter can include a transition phrase before the reasoning end token, such as "I have to give the solution based on the reasoning directly now.&lt;/think>" to make reasoning termination more natural when the budget is exhausted.

## Important Note

In vLLM v0.18.0, `thinking_token_budget` is not a native `SamplingParams` field and is not enforced if passed via `extra_args`; it only works when supported as a first-class parameter.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e36d910-899e-415f-9d47-7c53625ed1b3",
  "isSidechain": true,
  "promptId": "f42c4435-74a3-43b8-9fd9-c8b8f3b2cdbd",
  "agentId": "a080cedfb58bc3f30",
  "type": "user",
  "uuid": "bf51458c-a71d-4f9f-afdf-0edd5fa1a7f6",
  "sourceToolAssistantUUID": "7e36d910-899e-415f-9d47-7c53625ed1b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-09T21:32:16.470Z_

<details><summary>↩ Tool result · `toolu_01L7KXQMg9KpM8d81pE8d1Ye`</summary>

```text
Web search results for query: "Sonata dynamic thinking budget allocation reasoning models ICLR 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=2i6Rp0gCq6"},{"title":"Published at Latent & Implicit Thinking Workshop @ ICLR 2026","url":"https://openreview.net/pdf?id=frSSQ7fWFX"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"GitHub - junhongmit/P-and-B: 🧠Plan-and-Budget: Training-free test-time reasoning framework for adaptive token allocation in large language models (ICLR 2026).","url":"https://github.com/junhongmit/P-and-B"},{"title":"ICLR.2026 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2026"},{"title":"Claude Sonnet 4.6 Adaptive Thinking: Dynamic Reasoning Control | 2026 | Claude 5","url":"https://claude5.ai/news/claude-sonnet-46-adaptive-thinking-replaces-extended-thinking"},{"title":"ICLR 2026 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/iclr-statistics/iclr-2026-statistics/"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"Workshops at ICLR 2026 – ICLR Blog","url":"https://blog.iclr.cc/2026/01/13/iclr2026-workshops/"},{"title":"Published as a conference paper at ICLR 2025 LEARNING HOW HARD TO THINK:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf"}]

I found relevant information about Sonata. Here are the key findings:

## Sonata: Self-Consistency-Guided Adapter for Thinking Allocation

Sonata dynamically allocates thinking budgets on-the-fly, introducing negligible computational overhead (< 1‰) while being generalizable across diverse tasks without task-specific fine-tuning.

### Key Performance Results

Experimental results across multiple models (Qwen3-8B, Qwen3-32B, GPT-OSS-120B, Qwen3-235B-A22B) and challenging benchmarks (AIME25, GSM8K, MATH500, GPQA, LiveCodeBench) demonstrate that Sonata achieves up to 60% reduction in thinking tokens while maintaining or improving accuracy by up to 2%.

### Technical Approach

Sonata is a lightweight approach that first learns to predict self-consistency directly from query hidden representations in the last layer. During inference, Sonata adapter takes the query's last layer hidden representations as input during the prefilling stage and adaptively allocates thinking budgets before decoding.

### Compatibility and Efficiency

Sonata is compatible with existing CoT compression techniques, enabling further efficiency gains when combined with these methods.

The paper was published at ICLR 2026 and presents a practical solution for optimizing test-time compute in reasoning models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53566cd0-852b-4d6c-bccf-08eca0ec74cd",
  "isSidechain": true,
  "promptId": "f42c4435-74a3-43b8-9fd9-c8b8f3b2cdbd",
  "agentId": "a080cedfb58bc3f30",
  "type": "user",
  "uuid": "26914242-4015-497f-acfa-b6ca527b60fc",
  "sourceToolAssistantUUID": "53566cd0-852b-4d6c-bccf-08eca0ec74cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-09T21:32:16.585Z_

<details><summary>↩ Tool result · `toolu_01MTEQRq6g3pVbphGaUdnVZn`</summary>

```text
Web search results for query: "vLLM per-request thinking budget parameter 2025 2026"

Links: [{"title":"Reasoning Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/reasoning_outputs/"},{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"Adding Reasoning Budget to vLLM (Reasoning Token Limit) – Shuyo's Weblog","url":"https://shuyo.wordpress.com/2026/03/26/adding-reasoning-budget-to-vllm-reasoning-token-limit/"},{"title":"[Feature]: GLM thinking budget · Issue #26091 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/26091"},{"title":"thinking_budget_state - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/v1/sample/thinking_budget_state/"},{"title":"Seed-OSS-36B Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Seed/Seed-OSS-36B.html"},{"title":"[Feature]: Add Support for thinking_budget for Qwen3 Models · Issue #17887 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17887"},{"title":"vLLM x Qwen3-Next: Hybrid Attention, Multi-Token Prediction, and Thinking Controls for Production-Grade Inference | by Sai Dheeraj Gummadi | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/vllm-x-qwen3-next-hybrid-attention-multi-token-prediction-and-thinking-controls-for-a0f6b3dcc120"},{"title":"BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens","url":"https://arxiv.org/html/2508.17196v1"},{"title":"[Usage]: How to limit the thinking budget for reasoning mode · Issue #17700 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17700"}]

Based on the search results, I found information about vLLM's per-request thinking budget parameter:

## vLLM Thinking Budget Parameter

The `thinking_token_budget` is a sampling parameter that sets the per-request reasoning token limit.

### Implementation and Usage

The parameter can be used in API requests via the `thinking_token_budget` field, or in Python code through `SamplingParams(thinking_token_budget=&lt;value>)`.

### Recent Developments (2025-2026)

There have been recent efforts to enhance this functionality:

1. **PR #37112 (March 2026)**: A pull request addressing reasoning budget was open since July 2025, and a more recent PR reuses the existing `--reasoning-parser` infrastructure without introducing new CLI arguments or config classes.

2. **Alternative Parameter Name**: Some implementations use a `reasoning_budget` parameter in API requests for specifying reasoning token limits.

3. **Seed-OSS-36B Guidance**: For models like Seed-OSS, when a thinking budget is specified, values that are integer multiples of 512 are recommended.

### How It Works

When reasoning reaches a specified number of tokens, a message is inserted to prompt the termination of reasoning, such as "Let me stop thinking and answer now."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "128a210e-b539-423e-bc71-abc359dfd532",
  "isSidechain": true,
  "promptId": "f42c4435-74a3-43b8-9fd9-c8b8f3b2cdbd",
  "agentId": "a080cedfb58bc3f30",
  "type": "user",
  "uuid": "91e98d68-1486-474f-8798-a02c719d9a67",
  "sourceToolAssistantUUID": "128a210e-b539-423e-bc71-abc359dfd532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-09T21:32:17.551Z_

<details><summary>↩ Tool result · `toolu_01ERSY7tou38BpzuYpPGfLCY`</summary>

```text
Web search results for query: "SelfBudgeter arXiv 2505.11274 adaptive token allocation"

Links: [{"title":"[2505.11274] SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://arxiv.org/abs/2505.11274"},{"title":"Paper page - SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://huggingface.co/papers/2505.11274"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://arxiv.org/pdf/2505.11274"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250511274L/abstract"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=e7EBzbi8Qd"},{"title":"[PDF] SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SelfBudgeter:-Adaptive-Token-Allocation-for-LLM-Li-Dong/569a37483dd8ecebc66b145fdc8226f11474329d"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM ...","url":"https://www.alphaxiv.org/overview/2505.11274v1"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning - Consensus","url":"https://consensus.app/papers/selfbudgeter-adaptive-token-allocation-for-efficient-llm-sui/ca25b43e24bc551799a8452f58178e8c/"},{"title":"(PDF) SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://www.researchgate.net/publication/391857085_SelfBudgeter_Adaptive_Token_Allocation_for_Efficient_LLM_Reasoning"},{"title":"Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://bytez.com/docs/arxiv/2505.11274/datasets"}]

Based on the search results, here's what I found about SelfBudgeter (arXiv 2505.11274):

## Overview

SelfBudgeter is a novel user-friendly adaptive controllable reasoning framework that incorporates a budget estimation mechanism prior to reasoning. The paper addresses a significant challenge in large reasoning models: reasoning models often exhibit tendencies of overthinking on simple problems, which leads to excessive computational resource consumption and significantly degrades user experience.

## Training Approach

The framework adopts a dual-phase training paradigm: during the cold-start phase, the model learns to predict token budgets before executing reasoning in a standardized format; in the reinforcement learning phase, the model is trained to autonomously plan budgets based on problem difficulty and strictly adhere to them when generating responses.

## Key Features

Since the model outputs budget estimates at the initial stage, users can immediately anticipate waiting duration, enabling flexible decisions on whether to interrupt or continue the generation process. Notably, the method supports manual control of reasoning length through pre-filled budget fields.

## Performance Results

Experimental results demonstrate that SelfBudgeter can dynamically allocate budgets according to problem complexity, yielding an average response length compression of 61% for the 1.5B model on GSM8K, MATH500, and AIME2025, and 48% for the 7B model, while maintaining nearly undiminished accuracy.

## Authors

The paper was authored by Zheng Li, Qingxiu Dong, Jingyuan Ma, Di Zhang, and Zhifang Sui, and was published in arXiv in May 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8709161e-26b8-4f45-81eb-104b24086d5f",
  "isSidechain": true,
  "promptId": "f42c4435-74a3-43b8-9fd9-c8b8f3b2cdbd",
  "agentId": "a080cedfb58bc3f30",
  "type": "user",
  "uuid": "6aecb6dc-a72f-4e31-9684-826b4d987964",
  "sourceToolAssistantUUID": "8709161e-26b8-4f45-81eb-104b24086d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-09T21:32:17.634Z_

<details><summary>↩ Tool result · `toolu_018AMrjDRV9PP2TfzX3vc13s`</summary>

```text
Web search results for query: "TALE token budget aware LLM reasoning ACL 2025"

Links: [{"title":"Token-Budget-Aware LLM Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1274/"},{"title":"Token-Budget-Aware LLM Reasoning","url":"https://aclanthology.org/2025.findings-acl.1274.pdf"},{"title":"GitHub - GeniusHTX/TALE · GitHub","url":"https://github.com/GeniusHTX/TALE"},{"title":"arXiv:2412.18547v5 [cs.CL] 2 Jun 2025 Token-Budget-Aware LLM Reasoning","url":"https://arxiv.org/pdf/2412.18547"},{"title":"Token-Budget-Aware LLM Reasoning","url":"https://arxiv.org/html/2412.18547v1"},{"title":"Token-Budget-Aware LLM Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241218547H/abstract"},{"title":"[2412.18547] Token-Budget-Aware LLM Reasoning","url":"https://arxiv.org/abs/2412.18547"},{"title":"Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs","url":"https://arxiv.org/html/2507.02076v1"},{"title":"Summary: Token-Budget-Aware Llm Reasoning · GitHub","url":"https://gist.github.com/thehunmonkgroup/aceb859a819729711bdb815cc946a34c"},{"title":"[Literature Review] Token-Budget-Aware LLM Reasoning","url":"https://www.themoonlight.io/en/review/token-budget-aware-llm-reasoning"}]

I found detailed information about TALE (Token-Budget-Aware LLM Reasoning) from ACL 2025. Here's what the research is about:

## Overview

TALE is a paper by Tingxu Han, Zhenting Wang, Chunrong Fang, Shiyu Zhao, Shiqing Ma, and Zhenyu Chen, published in the Findings of the Association for Computational Linguistics: ACL 2025.

## Core Problem

Methods like Chain-of-Thought (CoT) reasoning enhance LLM performance by decomposing problems into intermediate steps, but they incur significant overhead in token usage, leading to increased costs. The reasoning process of current LLMs is unnecessarily lengthy and it can be compressed by including a reasonable token budget in the prompt, but the choice of token budget plays a crucial role in the actual compression effectiveness.

## Proposed Solution

The paper proposes a token-budget-aware LLM reasoning framework that dynamically adjusts the number of reasoning tokens based on the reasoning complexity of each problem. Experiments show that their method effectively reduces token costs in CoT reasoning with only a slight performance reduction, offering a practical solution to balance efficiency and accuracy in LLM reasoning.

## Implementation Variants

The authors propose two variants of this approach: TALE-EP (estimation+prompting) and TALE-PT (post-training). TALE-EP uses the reasoning LLM itself with a zero-shot estimation prompt as the token budget estimator, and then crafts a token-budget-aware prompt and feeds it into the LLM to generate the final answer.

## Results

TALE-EP reduces output token costs by 67%, lowers expenses by 59%, and maintains competitive performance compared to the vanilla CoT approach.

The code is available at: https://github.com/GeniusHTX/TALE


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15cc27e2-697b-4e31-94fc-532a3a3bf804",
  "isSidechain": true,
  "promptId": "f42c4435-74a3-43b8-9fd9-c8b8f3b2cdbd",
  "agentId": "a080cedfb58bc3f30",
  "type": "user",
  "uuid": "63efe6dd-ceec-495f-ba6a-4f305648afca",
  "sourceToolAssistantUUID": "15cc27e2-697b-4e31-94fc-532a3a3bf804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-09T21:32:29.124Z_

## Summary of Verification Findings

### 1. **Sonata Paper (openreview.net/pdf?id=2i6Rp0gCq6) - EXISTS**

**Status**: CONFIRMED - The paper exists and is published at ICLR 2026

**What it claims**: Sonata is a self-consistency-guided adapter for dynamic thinking allocation. It:
- Dynamically allocates thinking budgets on-the-fly with negligible computational overhead (< 1‰)
- Achieves up to 60% reduction in thinking tokens while maintaining or improving accuracy by up to 2%
- Works across diverse tasks without task-specific fine-tuning
- Is generalizable across models (Qwen3-8B, Qwen3-32B, GPT-OSS-120B, Qwen3-235B-A22B)
- Tests on benchmarks: AIME25, GSM8K, MATH500, GPQA, LiveCodeBench

The paper was indeed published as a conference paper at ICLR 2026.

### 2. **vLLM thinking_token_budget Parameter - PARTIALLY NATIVE**

**Status**: MIXED - The parameter is supported but implementation status varies

**Key findings**:
- vLLM does support `thinking_token_budget` as a sampling parameter that can be passed in SamplingParams
- However, it is **NOT a fully native first-class parameter in all versions**
- In vLLM v0.18.0, `thinking_token_budget` is not a native SamplingParams field and is silently ignored when passed via extra_args
- A recent PR (#37112 from March 2026) was working to add "reasoning_budget" to cap thinking tokens using existing reasoning parser infrastructure
- The feature was introduced as a per-request parameter but implementation has evolved across versions
- There's also a `ReasoningBudgetLogitsProcessor` for handling token counting and stop injection

**Caveat**: You should verify the specific vLLM version you're referencing, as the parameter status changed between 0.18.0 and more recent releases.

### 3. **TALE Paper (ACL 2025) - EXISTS**

**Status**: CONFIRMED - The paper exists and is published in ACL 2025 Findings

**What it claims**: TALE (Token-Budget-Aware LLM Reasoning) proposes a framework that:
- Dynamically adjusts the number of reasoning tokens based on problem complexity
- Reduces output token costs by 67% and expenses by 59%
- Has two variants: TALE-EP (estimation+prompting) and TALE-PT (post-training)
- Maintains competitive performance with vanilla CoT while reducing costs
- Code available at: https://github.com/GeniusHTX/TALE

Published in Findings of ACL 2025, arxiv ID: 2412.18547

### 4. **SelfBudgeter Paper (arXiv 2505.11274) - EXISTS**

**Status**: CONFIRMED - The paper exists and is published on arXiv (May 2025)

**What it claims**: SelfBudgeter is an adaptive token allocation framework that:
- Incorporates a budget estimation mechanism prior to reasoning
- Uses dual-phase training: cold-start phase for budget prediction, RL phase for autonomous budget planning
- Achieves 61% response length compression for 1.5B model, 48% for 7B model
- Tests on: GSM8K, MATH500, AIME2025
- Maintains nearly undiminished accuracy while compressing reasoning length
- Supports manual control of reasoning length through pre-filled budget fields

---

### Sources:
- [Sonata ICLR 2026](https://openreview.net/pdf?id=2i6Rp0gCq6)
- [vLLM Reasoning Outputs Documentation](https://docs.vllm.ai/en/latest/features/reasoning_outputs/)
- [vLLM PR #37112 - Reasoning Budget](https://github.com/vllm-project/vllm/pull/37112)
- [vLLM Issue #25714 - thinking_budget for Qwen-3](https://github.com/vllm-project/vllm/issues/25714)
- [TALE ACL 2025](https://aclanthology.org/2025.findings-acl.1274/)
- [TALE arXiv](https://arxiv.org/abs/2412.18547)
- [TALE GitHub](https://github.com/GeniusHTX/TALE)
- [SelfBudgeter arXiv 2505.11274](https://arxiv.org/abs/2505.11274)
- [SelfBudgeter OpenReview](https://openreview.net/forum?id=e7EBzbi8Qd)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63efe6dd-ceec-495f-ba6a-4f305648afca",
  "isSidechain": true,
  "agentId": "a080cedfb58bc3f30",
  "requestId": "req_011Casi8zctRoQPTT6iH2J8i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2e8118c4-e43d-4978-8735-673344e134de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dca20ed3-3ccc-40d7-84a2-9a4c60976a3e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AWJP4mzKcwmEePVrhJzuM4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 5540,
      "cache_read_input_tokens": 16831,
      "output_tokens": 1164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5540
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1018,
          "output_tokens": 1164,
          "cache_read_input_tokens": 16831,
          "cache_creation_input_tokens": 5540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5540,
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
