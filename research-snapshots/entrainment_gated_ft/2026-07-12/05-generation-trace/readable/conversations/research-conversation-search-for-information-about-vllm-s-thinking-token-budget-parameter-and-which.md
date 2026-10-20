# Research conversation: Search for information about vLLM's thinking_token_budget parameter and which version correctly supports it via Sampling

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a975e6a647a2e7708.jsonl`
- **Structured JSON:** [`bf6f1d95dd3291d9658f.json`](../../sessions/bf/bf6f1d95dd3291d9658f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-09T20:34:18.054Z_

Search for information about vLLM's thinking_token_budget parameter and which version correctly supports it via SamplingParams.

Specifically look for:
1. Any known bugs where thinking_token_budget is silently ignored when passed via extra_args in vLLM 0.18.0
2. What vLLM version introduced thinking_token_budget support via SamplingParams
3. Any PR #37112 in vLLM that relates to thinking_token_budget
4. The current stable vLLM version as of 2026

Try searching:
- "vLLM thinking_token_budget SamplingParams version"
- "vLLM PR 37112 thinking_token_budget"
- vLLM GitHub releases page or changelog

Report what you find about the correct vLLM version to cite for thinking_token_budget support.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "ea584cd7-da12-4d54-9d5f-6c3d0a568a1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-09T20:34:20.149Z_

I'll search for information about vLLM's thinking_token_budget parameter support. Let me start with web searches to find the relevant information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea584cd7-da12-4d54-9d5f-6c3d0a568a1b",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdiWDTHj9eCgmnijdFT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a50be16b-d19a-4f83-b5f9-70952881570b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QAfsW22anXTdNfscPWFBrw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 3 · 2026-05-09T20:34:20.355Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016AwboJ9igZozTuVFaMrSXK`</summary>

```json
{
  "query": "vLLM thinking_token_budget SamplingParams version support"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a50be16b-d19a-4f83-b5f9-70952881570b",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdiWDTHj9eCgmnijdFT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e864313b-c0d1-45a1-a96b-4d8903d1a4b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QAfsW22anXTdNfscPWFBrw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 4 · 2026-05-09T20:34:20.597Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lt4whWmEzEBGZPgDfpgPKi`</summary>

```json
{
  "query": "vLLM PR 37112 thinking_token_budget"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e864313b-c0d1-45a1-a96b-4d8903d1a4b2",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdiWDTHj9eCgmnijdFT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d691278b-f15c-4c71-889b-210dd899897b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QAfsW22anXTdNfscPWFBrw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 5 · 2026-05-09T20:34:20.792Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KQwiBMq4MwMi9cbBTe2Jfj`</summary>

```json
{
  "query": "vLLM 0.18.0 thinking_token_budget extra_args ignored bug"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d691278b-f15c-4c71-889b-210dd899897b",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdiWDTHj9eCgmnijdFT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d45087f3-16f6-4d7f-a4a6-fa43d032c235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QAfsW22anXTdNfscPWFBrw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 6 · 2026-05-09T20:34:20.918Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WUqdZo69dMrXzXivyqy9fb`</summary>

```json
{
  "query": "vLLM stable version 2026 releases changelog"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d45087f3-16f6-4d7f-a4a6-fa43d032c235",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdiWDTHj9eCgmnijdFT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "962ee843-6946-4875-ae65-c53aacec7a47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QAfsW22anXTdNfscPWFBrw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 16155,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 247,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 624,
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

_source line 7 · 2026-05-09T20:34:26.628Z_

<details><summary>↩ Tool result · `toolu_01KQwiBMq4MwMi9cbBTe2Jfj`</summary>

```text
Web search results for query: "vLLM 0.18.0 thinking_token_budget extra_args ignored bug"

Links: [{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - #2 by RunLLM - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533/2"},{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"[Bug]: Thinking token budget not enforced with MTP speculative decoding (works without MTP) · Issue #39573 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/39573"},{"title":"[Bug]: Qwen3-30B-A3B on vLLM-OpenAI v0.12.0 “hangs” in thinking mode: keeps reasoning until token cap · Issue #30599 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/30599"},{"title":"[Bug]: Qwen3.5 `thinking_token_budget` causes `reasoning_end_str` to leak into `content` field · Issue #39697 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/39697"},{"title":"[Bug]:GLM-5-W4A8 Still display&lt;/think> token in output when thinking mode is disabled · Issue #6772 · vllm-project/vllm-ascend","url":"https://github.com/vllm-project/vllm-ascend/issues/6772"},{"title":"Bug: Speculative Decoding (MTP) Causes &lt;/think> Detection Failure in Structured Output + Reasoning Mode · Issue #34650 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/34650"},{"title":"[Bug]: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 21.1%, Prefix cache hit rate: 11.9% · Issue #22731 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/22731"},{"title":"[Bug]: Qwen3-VL-Thinking / Qwen3-Thinking-2507 reasoning parser doesn't account for &lt;think> (start token) appended to input / chat template · Issue #27118 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/27118"}]

Based on the search results, here's what I found about the vLLM 0.18.0 `thinking_token_budget` `extra_args` ignored bug:

## Bug Summary

In vLLM v0.18.0, `thinking_token_budget` is not a native SamplingParams field and is not enforced if passed via extra_args; it only works when supported as a first-class parameter.

## Root Cause

The ability to cap reasoning tokens via `thinking_token_budget` (or `reasoning_budget`) was added in later PRs and is available in vLLM mainline after those merges, not in v0.18.0.

## Context

This issue was documented in the vLLM forums, where users running Qwen models with thinking mode enabled reported that some pages are data-dense and cause the model to enter long reasoning loops, exhausting all output tokens on content without ever producing the actual JSON response. They attempted to use `thinking_token_budget` to cap reasoning tokens, but the parameter was silently ignored when passed via `extra_args`.

## Workaround

There is no supported way to enforce a thinking token cap in v0.18.0 without modifying vLLM internals or upgrading to a newer version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d45087f3-16f6-4d7f-a4a6-fa43d032c235",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "2c793e92-913c-4455-b8ce-69f468c4978a",
  "sourceToolAssistantUUID": "d45087f3-16f6-4d7f-a4a6-fa43d032c235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-09T20:34:27.403Z_

<details><summary>↩ Tool result · `toolu_016AwboJ9igZozTuVFaMrSXK`</summary>

```text
Web search results for query: "vLLM thinking_token_budget SamplingParams version support"

Links: [{"title":"Gemma 4 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html"},{"title":"Sampling Params — vLLM","url":"https://docs.vllm.ai/en/v0.4.1/dev/sampling_params.html"},{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"Sampling Parameters — vLLM","url":"https://docs.vllm.ai/en/v0.6.4/dev/sampling_params.html"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - #2 by RunLLM - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533/2"},{"title":"recipes/Google/Gemma4.md at main · vllm-project/recipes","url":"https://github.com/vllm-project/recipes/blob/main/Google/Gemma4.md"},{"title":"sampling_params - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/sampling_params/"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533"},{"title":"Inference Parameters — vLLM","url":"https://docs.vllm.ai/en/v0.8.4/api/inference_params.html"},{"title":"vLLM x Qwen3-Next: Hybrid Attention, Multi-Token Prediction, and Thinking Controls for Production-Grade Inference | by Sai Dheeraj Gummadi | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/vllm-x-qwen3-next-hybrid-attention-multi-token-prediction-and-thinking-controls-for-a0f6b3dcc120"}]

Based on the web search results, here's what I found about `vLLM thinking_token_budget` and `SamplingParams` version support:

## Key Findings:

thinking_token_budget is not a native SamplingParams field in vLLM v0.18.0 and is not enforced if passed via extra_args; it only works when supported as a first-class parameter.

The ability to cap reasoning tokens via thinking_token_budget (or reasoning_budget) was added in later PRs (e.g., #20859, #37112) and is available in vLLM mainline after those merges, not in v0.18.0.

## Related Feature: reasoning_budget

A related feature called `reasoning_budget` was introduced in a pull request. This pull request introduces a reasoning_budget to cap the number of tokens generated within &lt;think>...&lt;/think> blocks. A new ReasoningBudgetLogitsProcessor is added to handle the token counting and injection of a stop message when the budget is exceeded.

The feature can be used in SamplingParams with: SamplingParams(reasoning_budget=50, reasoning_budget_message="Wrap it up.")

## Summary:

If you're using vLLM v0.18.0 or earlier, `thinking_token_budget` as a direct SamplingParams parameter is not supported. You would need to upgrade to a more recent version where this feature has been properly implemented as a first-class parameter in SamplingParams, or use the newer `reasoning_budget` alternative that was added in later pull requests.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e864313b-c0d1-45a1-a96b-4d8903d1a4b2",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "ab438fdb-6f9c-438b-b229-a5681e9b29c6",
  "sourceToolAssistantUUID": "e864313b-c0d1-45a1-a96b-4d8903d1a4b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-09T20:34:28.315Z_

<details><summary>↩ Tool result · `toolu_01WUqdZo69dMrXzXivyqy9fb`</summary>

```text
Web search results for query: "vLLM stable version 2026 releases changelog"

Links: [{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"vLLM Release Notes - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html"},{"title":"vllm · PyPI","url":"https://pypi.org/project/vllm/"},{"title":"stable - vLLM","url":"https://docs.vllm.ai/en/stable/"},{"title":"vLLM release 2026 update: three ships in 14 days, and why upgrading yours means zero changes to your Mac agent","url":"https://fazm.ai/t/vllm-release-2026-update"},{"title":"Release Notes — vllm-ascend","url":"https://docs.vllm.ai/projects/ascend/en/latest/user_guide/release_notes.html"},{"title":"Versions | vllm | PyPI","url":"https://deps.dev/pypi/vllm/0.2.6/versions"},{"title":"vLLM Releases - All Versions","url":"https://vllm.ai/releases"},{"title":"vLLM/RELEASE.md at main · bowang-lab/vLLM","url":"https://github.com/bowang-lab/vLLM/blob/main/RELEASE.md"},{"title":"Releases · micytao/vllm-playground","url":"https://github.com/micytao/vllm-playground/releases"}]

Based on the search results, I found information about vLLM releases from 2026. Here's what I found:

## Latest vLLM Release (2026)

The latest version is vLLM 0.20.1, released on May 3, 2026.

## Key 2026 Release Highlights

Recent 2026 releases include several significant updates:

**Major Features:**
- v0.18.0 (late March 2026) included gRPC serving behind the new --grpc flag, GPU-based NGram speculative decoding, and a new KV cache offload backend named FlexKV
- v0.19.0 (April 2) brought day-one Gemma 4 support across E2B, E4B, 26B MoE, and 31B Dense, plus async scheduler on by default and Model Runner V2

**Python and Dependency Updates:**
- PyTorch 2.11 upgrade with CUDA and XPU support, and Python 3.14 was added to the supported Python version list
- vLLM now runs on HuggingFace transformers>=5, with continued v4/v5 compatibility fixes

**Bug Fixes and Improvements:**
- Patch protobuf for CVE-2026-0994, huggingface-hub updates for Transformers v5 preparation, and Transformers v5 compatibility fixes across multiple models

For a complete and detailed changelog, you can visit the official [vLLM releases page on GitHub](https://github.com/vllm-project/vllm/releases) or [vLLM.ai releases page](https://vllm.ai/releases).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "962ee843-6946-4875-ae65-c53aacec7a47",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "a90bc72c-50f3-44b9-88e6-efbc08041c97",
  "sourceToolAssistantUUID": "962ee843-6946-4875-ae65-c53aacec7a47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-09T20:34:31.758Z_

<details><summary>↩ Tool result · `toolu_01Lt4whWmEzEBGZPgDfpgPKi`</summary>

```text
Web search results for query: "vLLM PR 37112 thinking_token_budget"

Links: [{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"[Bug]: Thinking token budget not enforced with MTP speculative decoding (works without MTP) · Issue #39573 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/39573"},{"title":"thinking_budget_state - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/v1/sample/thinking_budget_state/"},{"title":"Reasoning Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/reasoning_outputs/"},{"title":"[Feature]: GLM thinking budget · Issue #26091 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/26091"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533"},{"title":"BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens","url":"https://arxiv.org/html/2508.17196v1"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - #2 by RunLLM - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533/2"},{"title":"[Feature]: Add Support for thinking_budget for Qwen3 Models · Issue #17887 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17887"},{"title":"Adding Reasoning Budget to vLLM (Reasoning Token Limit) – Shuyo's Weblog","url":"https://shuyo.wordpress.com/2026/03/26/adding-reasoning-budget-to-vllm-reasoning-token-limit/"}]

Based on the search results, here's what I found about vLLM PR 37112:

## Overview

This pull request introduces a reasoning_budget to cap the number of tokens generated within &lt;think>...&lt;/think> blocks.

## Key Features

The implementation is well-integrated with the existing reasoning parser infrastructure, avoiding new configuration flags as requested in feedback on a previous PR. A new ReasoningBudgetLogitsProcessor is added to handle the token counting and injection of a stop message when the budget is exceeded.

## How It Works

Per-request state tracks nesting depth (handles &lt;think> in prompt), counts reasoning tokens, and switches to injection mode when budget is exceeded. An injection feature force-injects a configurable message (default: "Reasoning budget exceeded, need to answer.") followed by the &lt;/think> end token by setting logits to -inf for all tokens except the forced one.

## API Usage

The feature can be used through both OpenAI-compatible endpoints and SamplingParams:
- Via OpenAI-compatible chat completion: `{"reasoning_budget": 50}` or via SamplingParams: `SamplingParams(reasoning_budget=50, reasoning_budget_message="Wrap it up.")`

PR 37112 was authored by abhinand5 in March 2026, and this ability to cap reasoning tokens was added in later PRs (e.g., #20859, #37112) and is available in vLLM mainline after those merges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d691278b-f15c-4c71-889b-210dd899897b",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "80c24f4f-5ed6-4ac4-92ee-e13cfa75b72d",
  "sourceToolAssistantUUID": "d691278b-f15c-4c71-889b-210dd899897b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-09T20:34:33.144Z_

Let me get more specific information about the thinking_token_budget forum discussion and PR 37112 details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80c24f4f-5ed6-4ac4-92ee-e13cfa75b72d",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdjWTci62eMoUwvbWed",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1dcbace0-5bc2-4e5e-9c68-7f418cfb5a45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UV4RwVHSYLSZDyGJnX1Dbp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2018,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 16779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3136,
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

_source line 12 · 2026-05-09T20:34:33.779Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PNofZer3tueY2yeXugEVci`</summary>

```json
{
  "url": "https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533",
  "prompt": "What is the issue with thinking_token_budget in vLLM 0.18.0? What is the solution or workaround?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dcbace0-5bc2-4e5e-9c68-7f418cfb5a45",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdjWTci62eMoUwvbWed",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f14d3293-1c48-4a1f-9d01-72bb19db4b7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UV4RwVHSYLSZDyGJnX1Dbp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2018,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 16779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3136,
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

_source line 13 · 2026-05-09T20:34:34.321Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018V7Rhtzcw2t5Qyf7Lkqr3a`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/pull/37112",
  "prompt": "What does this PR do? When was it merged? What version supports reasoning_budget?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f14d3293-1c48-4a1f-9d01-72bb19db4b7f",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdjWTci62eMoUwvbWed",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "542a3933-6643-42b0-bc49-51e945d64598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UV4RwVHSYLSZDyGJnX1Dbp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2018,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 16779,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3136
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2018,
          "output_tokens": 259,
          "cache_read_input_tokens": 16779,
          "cache_creation_input_tokens": 3136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3136,
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

_source line 14 · 2026-05-09T20:34:38.509Z_

<details><summary>↩ Tool result · `toolu_01PNofZer3tueY2yeXugEVci`</summary>

```text
# Issue with thinking_token_budget in vLLM 0.18.0

## The Problem

In vLLM version 0.18.0, `thinking_token_budget` is not a native field in `SamplingParams`. When users attempt to pass it via the `extra_args` dictionary, the parameter is accepted without error but **is not actually enforced by the engine**. This results in models with thinking mode enabled exhausting all output tokens on reasoning content without transitioning to producing the actual response—the exact failure mode occurs whether the parameter is included or not.

## The Solution

According to the forum response, there is **no supported workaround in v0.18.0**. The options are:

1. **Upgrade vLLM**: Move to a version after PR #20859 and #37112 are merged, where `thinking_token_budget` becomes a first-class `SamplingParams` field with actual engine enforcement

2. **Use ThinkingTokenBudgetLogitsProcessor**: In newer versions, this dedicated logits processor handles reasoning token caps

3. **Modify vLLM internals**: Implement custom code changes (not recommended for production)

The forum explicitly states: "There is no supported way to enforce a thinking token cap in v0.18.0 without modifying vLLM internals or upgrading."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f14d3293-1c48-4a1f-9d01-72bb19db4b7f",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "659c22f6-f372-4b00-88ad-9f82cd426035",
  "sourceToolAssistantUUID": "f14d3293-1c48-4a1f-9d01-72bb19db4b7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-09T20:34:40.384Z_

<details><summary>↩ Tool result · `toolu_018V7Rhtzcw2t5Qyf7Lkqr3a`</summary>

```text
# PR Summary

## What It Does
This PR introduces a `reasoning_budget` feature to cap the number of tokens generated within `&lt;think>...&lt;/think>` blocks for reasoning models like DeepSeek-R1 and Qwen3. The implementation adds:

- New `reasoning_budget` and `reasoning_budget_message` parameters to the API
- A `ReasoningBudgetLogitsProcessor` that automatically integrates with existing reasoning parsers
- Automatic injection of a custom message when the token budget is exceeded

The design reuses existing infrastructure rather than introducing new configuration classes, addressing architectural feedback from maintainers.

## Merge Status
**The PR was closed without merging.** On March 24, 2026, maintainer @njhill commented: "I've merged the original PR," referring to PR #20859, which appears to have been the superseding implementation. The author (@abhinand5) subsequently closed this PR on March 29, 2026.

## Version Support
The webpage does not specify which vLLM version includes `reasoning_budget`. Since this PR itself was not merged into the main repository, the feature would be available in whatever version incorporated the merged original PR (#20859).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "542a3933-6643-42b0-bc49-51e945d64598",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "160e4e5a-dd1a-454d-afc3-2bbffd39b1e2",
  "sourceToolAssistantUUID": "542a3933-6643-42b0-bc49-51e945d64598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-09T20:34:41.536Z_

Let me search for more information about PR #20859, which appears to be the actual merged PR for thinking/reasoning token budget support.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "160e4e5a-dd1a-454d-afc3-2bbffd39b1e2",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011Casdk9Kui3kd3xNpQwARQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2f5244b0-f937-4ef6-88d7-9bf83f1e15b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JpPEyTmneLdgsawhdFjJok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2902,
      "cache_read_input_tokens": 19915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2902,
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

_source line 17 · 2026-05-09T20:34:41.763Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T1wDSsQkxLpKLjpVQgS5pq`</summary>

```json
{
  "query": "vLLM PR 20859 thinking_token_budget reasoning_budget merged"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f5244b0-f937-4ef6-88d7-9bf83f1e15b4",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011Casdk9Kui3kd3xNpQwARQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04deb604-b291-45e3-bd98-058463e18530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JpPEyTmneLdgsawhdFjJok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2902,
      "cache_read_input_tokens": 19915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2902,
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

_source line 18 · 2026-05-09T20:34:42.191Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XbTLCqn4495zmbHFhSFdWx`</summary>

```json
{
  "query": "\"thinking_token_budget\" vLLM version support \"SamplingParams\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04deb604-b291-45e3-bd98-058463e18530",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011Casdk9Kui3kd3xNpQwARQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d13b1e9f-4707-4d19-b97a-1f819de56e39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JpPEyTmneLdgsawhdFjJok",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2902,
      "cache_read_input_tokens": 19915,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2902
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 151,
          "cache_read_input_tokens": 19915,
          "cache_creation_input_tokens": 2902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2902,
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

_source line 19 · 2026-05-09T20:34:48.096Z_

<details><summary>↩ Tool result · `toolu_01XbTLCqn4495zmbHFhSFdWx`</summary>

```text
Web search results for query: ""thinking_token_budget" vLLM version support "SamplingParams""

Links: [{"title":"Reasoning Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/reasoning_outputs/"},{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - #2 by RunLLM - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533/2"},{"title":"How to pass `thinking_budget` for Qwen-3 Thinking models in offline AsyncLLMEngine? · Issue #25714 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/25714"},{"title":"Understanding vLLM Scheduling: Token Budgets, Chunked Prefill, and Policies | by Audrey Wang | Mar, 2026 | Medium","url":"https://audreywongkg.medium.com/understanding-vllm-scheduling-token-budgets-chunked-prefill-and-policies-2c879e3980e3"},{"title":"recipes/Google/Gemma4.md at main · vllm-project/recipes","url":"https://github.com/vllm-project/recipes/blob/main/Google/Gemma4.md"},{"title":"vLLM x Qwen3-Next: Hybrid Attention, Multi-Token Prediction, and Thinking Controls for Production-Grade Inference | by Sai Dheeraj Gummadi | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/vllm-x-qwen3-next-hybrid-attention-multi-token-prediction-and-thinking-controls-for-a0f6b3dcc120"},{"title":"Inference Parameters — vLLM","url":"https://docs.vllm.ai/en/v0.8.4/api/inference_params.html"},{"title":"vLLM - Qwen","url":"https://qwen.readthedocs.io/en/latest/deployment/vllm.html"},{"title":"Sampling Parameters — vLLM","url":"https://docs.vllm.ai/en/v0.6.4/dev/sampling_params.html"}]

Based on the search results, here's what I found regarding `thinking_token_budget` support in vLLM's `SamplingParams`:

## Version Support

The `thinking_token_budget` parameter can be used with `SamplingParams`, as shown in vLLM's official documentation examples where `sampling_params = SamplingParams(thinking_token_budget=10)` is used.

However, there's an important caveat: `thinking_token_budget` is not a native `SamplingParams` field in vLLM v0.18.0 and is not enforced if passed via extra_args; it only works when supported as a first-class parameter.

## Alternative Parameter Name

It's worth noting that a more recent feature introduces `reasoning_budget` to cap the number of tokens generated within `&lt;think>...&lt;/think>` blocks, with a new `ReasoningBudgetLogitsProcessor` added to handle the token counting.

## Current Status

The search results show that changes to the API surface in `ChatCompletionRequest` and `SamplingParams` for reasoning budget support are appropriate, indicating this functionality has been integrated into the codebase.

For the most up-to-date information on which specific vLLM versions support `thinking_token_budget` as a native `SamplingParams` field versus requiring `extra_args`, I'd recommend checking the vLLM official documentation or release notes for your specific version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d13b1e9f-4707-4d19-b97a-1f819de56e39",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "1c2cf5c8-c92e-4c9c-86c9-476560544d5e",
  "sourceToolAssistantUUID": "d13b1e9f-4707-4d19-b97a-1f819de56e39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-09T20:34:50.907Z_

<details><summary>↩ Tool result · `toolu_01T1wDSsQkxLpKLjpVQgS5pq`</summary>

```text
Web search results for query: "vLLM PR 20859 thinking_token_budget reasoning_budget merged"

Links: [{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - #2 by RunLLM - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533/2"},{"title":"Reasoning Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/reasoning_outputs/"},{"title":"Adding Reasoning Budget to vLLM (Reasoning Token Limit) – Shuyo's Weblog","url":"https://shuyo.wordpress.com/2026/03/26/adding-reasoning-budget-to-vllm-reasoning-token-limit/"},{"title":"[Bug]: Thinking token budget not enforced with MTP speculative decoding (works without MTP) · Issue #39573 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/39573"},{"title":"BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens","url":"https://arxiv.org/html/2508.17196v1"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533"},{"title":"thinking_budget_state - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/v1/sample/thinking_budget_state/"},{"title":"[Feature]: GLM thinking budget · Issue #26091 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/26091"},{"title":"[Feature]: Add Support for thinking_budget for Qwen3 Models · Issue #17887 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17887"}]

Based on the search results, here's what I found about vLLM PR #20859 and the thinking_token_budget/reasoning_budget features:

## PR #20859 Status

PR #20859 has been open since July 2025 and the main blocker from maintainer @njhill is architectural: it introduces a separate ReasoningConfig with --reasoning-config CLI arg requiring users to manually specify think_start_str/think_end_str.

## reasoning_budget Feature (PR #37112)

Rather than PR #20859 being merged as-is, a newer PR #37112 was created to address the architectural concerns. The ability to cap reasoning tokens via thinking_token_budget (or reasoning_budget) was added in later PRs (e.g., #20859, #37112) and is available in vLLM mainline after those merges.

The newer approach in PR #37112 reuses the existing --reasoning-parser infrastructure...no new CLI args, no new config classes. The logits processor obtains start/end token IDs directly from ReasoningParserManager, so it works automatically with any registered reasoning parser (deepseek_r1, qwen3, etc.).

## Current Usage

Once the reasoning token count reaches the configured thinking_token_budget, vLLM forces the model to produce reasoning_end_str, effectively terminating the reasoning block. thinking_token_budget (a sampling parameter) sets the per-request reasoning token limit.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04deb604-b291-45e3-bd98-058463e18530",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "746cafd1-1871-4659-8ca0-287b9a3cfce5",
  "sourceToolAssistantUUID": "04deb604-b291-45e3-bd98-058463e18530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-09T20:34:52.106Z_

Let me fetch the official vLLM reasoning outputs documentation to get more specific version information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "746cafd1-1871-4659-8ca0-287b9a3cfce5",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdkvLqXurigRDcdVmJ7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bd9cde30-23df-43a1-a859-c7d9b248dee8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ChCr4a7B8SMKrdaSgSujD2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1055,
      "cache_creation_input_tokens": 1299,
      "cache_read_input_tokens": 22817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1299,
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

_source line 22 · 2026-05-09T20:34:52.780Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018TBtYTBQpbCCuxxZ4u1qDo`</summary>

```json
{
  "url": "https://docs.vllm.ai/en/latest/features/reasoning_outputs/",
  "prompt": "What version of vLLM introduced thinking_token_budget or reasoning_budget support? How do you use it?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd9cde30-23df-43a1-a859-c7d9b248dee8",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdkvLqXurigRDcdVmJ7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a7e40c7c-edbe-4642-a017-d8a77d42cdf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ChCr4a7B8SMKrdaSgSujD2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1055,
      "cache_creation_input_tokens": 1299,
      "cache_read_input_tokens": 22817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1299,
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

_source line 23 · 2026-05-09T20:34:53.157Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G19DAdraad6KwFstNYaovr`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/releases",
  "prompt": "What are the recent releases? Which version introduced thinking_token_budget support? What was released in 2026?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7e40c7c-edbe-4642-a017-d8a77d42cdf1",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdkvLqXurigRDcdVmJ7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9216561a-0b60-4097-82c0-a801ef682562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ChCr4a7B8SMKrdaSgSujD2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1055,
      "cache_creation_input_tokens": 1299,
      "cache_read_input_tokens": 22817,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1299
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1055,
          "output_tokens": 225,
          "cache_read_input_tokens": 22817,
          "cache_creation_input_tokens": 1299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1299,
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

_source line 24 · 2026-05-09T20:34:58.717Z_

<details><summary>↩ Tool result · `toolu_018TBtYTBQpbCCuxxZ4u1qDo`</summary>

```text
Based on the documentation provided, **the specific vLLM version that introduced `thinking_token_budget` is not mentioned**. The page you've shared appears to be from the "latest developer preview docs," but no version number is explicitly stated.

However, the documentation does explain how to use this feature:

**Usage Method:**
The `thinking_token_budget` parameter limits reasoning tokens by forcing the model to produce an end token once the budget is exhausted. You can implement it in two ways:

1. **Online Serving**: Pass `"thinking_token_budget": 10` in your curl request to `/v1/chat/completions`

2. **Offline Inference**: Use `SamplingParams(thinking_token_budget=10)` when calling the LLM

As the docs state: "Once the reasoning token count reaches the configured `thinking_token_budget`, vLLM forces the model to produce `reasoning_end_str`."

This feature requires setting `--reasoning-parser` and optionally `--reasoning-config` with boundary tokens like `&lt;think>` and `&lt;/think>`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7e40c7c-edbe-4642-a017-d8a77d42cdf1",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "d0673cc0-b3cb-470e-8301-cb59103c804d",
  "sourceToolAssistantUUID": "a7e40c7c-edbe-4642-a017-d8a77d42cdf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-09T20:34:59.764Z_

<details><summary>↩ Tool result · `toolu_01G19DAdraad6KwFstNYaovr`</summary>

```text
# Recent vLLM Releases

Based on the provided content, here are the recent releases:

1. **v0.20.1** (May 4) - Patch release focused on DeepSeek V4 stabilization and performance improvements
2. **v0.20.0** (April 27) - Major release with 752 commits featuring DeepSeek V4 support, CUDA 13.0 default, and PyTorch 2.11 upgrade
3. **v0.19.1** (April 18) - Patch release with Transformers v5 upgrade and Gemma4 bug fixes
4. **v0.19.0** (April 3) - Major release introducing Gemma 4 support and async scheduling with speculative decoding
5. **v0.18.1** (March 31) - Patch release addressing SM100 MLA prefill and accuracy issues
6. **v0.18.0** (March 20) - Major release with gRPC serving support and GPU-less render serving

## Thinking Token Budget Support

The "thinking_token_budget" feature is mentioned in v0.19.0 release notes as a "hard limit" for limiting thinking tokens ([#20859](https://github.com/vllm-project/vllm/pull/20859)).

## 2026 Releases

No releases from 2026 are shown in the provided content—all documented releases are from 2024 and early 2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9216561a-0b60-4097-82c0-a801ef682562",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "e83cfc75-5479-41b0-9f59-bdbe895a3490",
  "sourceToolAssistantUUID": "9216561a-0b60-4097-82c0-a801ef682562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-09T20:35:00.686Z_

Let me search for more specific information about which version introduced thinking_token_budget support.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e83cfc75-5479-41b0-9f59-bdbe895a3490",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdmaARB38h7LEZjvtro",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a22cbbb8-bb40-4c53-b754-28bf517726db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CG1ZEYH3pq6XE9yweLid55",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 24116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
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

_source line 27 · 2026-05-09T20:35:00.937Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0164kDtnRokkUdeqnmYDHJw3`</summary>

```json
{
  "query": "vLLM v0.19.0 thinking_token_budget support release notes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a22cbbb8-bb40-4c53-b754-28bf517726db",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdmaARB38h7LEZjvtro",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c991721-f9db-4941-9a46-26ed96c0700e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CG1ZEYH3pq6XE9yweLid55",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 24116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
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

_source line 28 · 2026-05-09T20:35:01.097Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011BEZC9YMufpxbTTDywMwkk`</summary>

```json
{
  "query": "vLLM \"thinking_token_budget\" first introduced version April 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c991721-f9db-4941-9a46-26ed96c0700e",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdmaARB38h7LEZjvtro",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2f3cb8b4-2120-41fb-ad08-318cafdaea92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CG1ZEYH3pq6XE9yweLid55",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 24116,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1923
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 141,
          "cache_read_input_tokens": 24116,
          "cache_creation_input_tokens": 1923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1923,
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

_source line 29 · 2026-05-09T20:35:10.103Z_

<details><summary>↩ Tool result · `toolu_011BEZC9YMufpxbTTDywMwkk`</summary>

```text
Web search results for query: "vLLM "thinking_token_budget" first introduced version April 2026"

Links: [{"title":"[Bug]: Thinking token budget not enforced with MTP speculative decoding (works without MTP) · Issue #39573 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/39573"},{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"},{"title":"BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens","url":"https://arxiv.org/html/2508.17196v1"},{"title":"Adding Reasoning Budget to vLLM (Reasoning Token Limit) – Shuyo's Weblog","url":"https://shuyo.wordpress.com/2026/03/26/adding-reasoning-budget-to-vllm-reasoning-token-limit/"},{"title":"thinking_budget_state - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/v1/sample/thinking_budget_state/"},{"title":"[Feature]: GLM thinking budget · Issue #26091 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/26091"},{"title":"[Feature]: Add Support for thinking_budget for Qwen3 Models · Issue #17887 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17887"},{"title":"Understanding vLLM Scheduling: Token Budgets, Chunked Prefill, and Policies | by Audrey Wang | Mar, 2026 | Medium","url":"https://audreywongkg.medium.com/understanding-vllm-scheduling-token-budgets-chunked-prefill-and-policies-2c879e3980e3"},{"title":"Reasoning Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/reasoning_outputs/"},{"title":"vLLM Update April 2026: v0.18, v0.19, Gemma 4, and gRPC Serving - Fazm Blog","url":"https://fazm.ai/blog/vllm-update-april-2026"}]

Based on the search results, I found information about vLLM's `thinking_token_budget` feature:

The `thinking_token_budget` is a sampling parameter that sets the per-request reasoning token limit. According to the documentation referenced in the search results, you can make requests with `thinking_token_budget` to limit the reasoning tokens.

The feature appears to be documented as part of vLLM's reasoning outputs functionality as of April 2026 (based on the documentation dated April 1, 2026). Additionally, thinking token budget was introduced in PR #20859.

However, the search results show that there was also earlier work on a related feature: A pull request introduced a reasoning_budget to cap the number of tokens generated within thinking blocks, well-integrated with the existing reasoning parser infrastructure, which was submitted in March 2026.

The feature is actively used in vLLM v0.19.0 and appears to be a key part of the reasoning outputs capability for models like Qwen3.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f3cb8b4-2120-41fb-ad08-318cafdaea92",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "3add181a-4a38-4b8c-859e-2838bc3f3a02",
  "sourceToolAssistantUUID": "2f3cb8b4-2120-41fb-ad08-318cafdaea92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-09T20:35:17.053Z_

<details><summary>↩ Tool result · `toolu_0164kDtnRokkUdeqnmYDHJw3`</summary>

```text
Web search results for query: "vLLM v0.19.0 thinking_token_budget support release notes"

Links: [{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"Release v0.19.0 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases/tag/v0.19.0"},{"title":"vLLM Release Notes - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html"},{"title":"[Bug]: Thinking token budget not enforced with MTP speculative decoding (works without MTP) · Issue #39573 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/39573"},{"title":"vllm-project/vllm v0.19.0 on GitHub","url":"https://newreleases.io/project/github/vllm-project/vllm/release/v0.19.0"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533"},{"title":"Release Notes — vllm-ascend","url":"https://docs.vllm.ai/projects/ascend/en/main/user_guide/release_notes.html"},{"title":"thinking_token_budget silently ignored when passed via extra_args in vLLM 0.18.0 - #2 by RunLLM - Features - vLLM Forums","url":"https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533/2"},{"title":"Reasoning Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/reasoning_outputs/"},{"title":"[Feature] Add reasoning_budget to cap thinking tokens via existing reasoning parser by abhinand5 · Pull Request #37112 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/37112"}]

Based on the search results, I found information about vLLM v0.19.0 and the `thinking_token_budget` support:

vLLM v0.19.0 features 448 commits from 197 contributors (54 new). While the official v0.19.0 release notes don't explicitly mention `thinking_token_budget` as a new feature in the highlights, the documentation and related discussions indicate that this functionality was already in development.

According to the vLLM documentation, some models such as Qwen3, DeepSeek, and Nemotron3 support a thinking budget that limits the maximum number of tokens used for reasoning, and once the reasoning token count reaches the configured thinking_token_budget, vLLM forces the model to produce the reasoning end string.

However, it's worth noting that thinking_token_budget was not a native SamplingParams field in vLLM v0.18.0 and was not enforced if passed via extra_args, and the ability to cap reasoning tokens via thinking_token_budget was added in later PRs and is available in vLLM mainline after those merges.

The search results suggest that v0.19.0 included reasoning and thinking capabilities, but `thinking_token_budget` support as a first-class parameter appears to have been a recent addition around the time of v0.19.0 or shortly before.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c991721-f9db-4941-9a46-26ed96c0700e",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "bc3869fc-c9f8-4eef-b833-aae89f404c89",
  "sourceToolAssistantUUID": "9c991721-f9db-4941-9a46-26ed96c0700e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-09T20:35:18.341Z_

Let me get the specific v0.19.0 release notes to confirm when thinking_token_budget support was introduced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc3869fc-c9f8-4eef-b833-aae89f404c89",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011Casdnr5fEvALdZ9FDrNGr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0a8d91c4-d410-467d-8933-46561b87c0af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K7sfckW4V8dTzFd7jKJGKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 26039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1131,
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

_source line 32 · 2026-05-09T20:35:18.859Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NDDWexmZi64fNMdFp6JW2i`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/releases/tag/v0.19.0",
  "prompt": "What features were added in v0.19.0? Does it mention thinking_token_budget or PR 20859?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a8d91c4-d410-467d-8933-46561b87c0af",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011Casdnr5fEvALdZ9FDrNGr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "05aa38b6-aa27-4aa4-9e4d-14da37100adf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K7sfckW4V8dTzFd7jKJGKT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 26039,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1131
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 893,
          "output_tokens": 147,
          "cache_read_input_tokens": 26039,
          "cache_creation_input_tokens": 1131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1131,
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

_source line 33 · 2026-05-09T20:35:23.110Z_

<details><summary>↩ Tool result · `toolu_01NDDWexmZi64fNMdFp6JW2i`</summary>

```text
# vLLM v0.19.0 Features

Yes, the release notes mention thinking tokens. Under the **API & Frontend** section, it states:

"Limit thinking tokens (hard limit) (#20859)"

This PR added the ability to enforce a hard limit on thinking tokens. The release includes 448 commits and highlights major features like:

- **Gemma 4 support** with MoE and multimodal capabilities
- **Zero-bubble async scheduling** with speculative decoding
- **Model Runner V2** improvements including CUDA graphs for pipeline parallelism
- **ViT Full CUDA Graphs** for vision encoders
- **General CPU KV cache offloading** with pluggable cache policies
- **NVIDIA B300/GB300** support with optimized all-reduce
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05aa38b6-aa27-4aa4-9e4d-14da37100adf",
  "isSidechain": true,
  "promptId": "95a7d68e-c2ab-4a68-9d2b-73df3c4255fb",
  "agentId": "a975e6a647a2e7708",
  "type": "user",
  "uuid": "6efe5593-cf1b-44a4-a2b1-8d76a8a4a55f",
  "sourceToolAssistantUUID": "05aa38b6-aa27-4aa4-9e4d-14da37100adf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-09T20:35:31.309Z_

Perfect! Now I have the comprehensive information needed. Let me compile the findings.

## Summary of Findings

Based on my research, here's what I found about vLLM's `thinking_token_budget` parameter support:

### 1. **Known Bug in vLLM 0.18.0**

Yes, there is a confirmed bug where `thinking_token_budget` is **silently ignored when passed via `extra_args`** in vLLM 0.18.0:
- The parameter is not a native `SamplingParams` field in v0.18.0
- When passed via `extra_args`, it is accepted without error but **not enforced by the engine**
- This was documented in the [vLLM Forums discussion](https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533)
- The workaround is to upgrade to a newer version that supports it as a first-class parameter

### 2. **Version That Introduced `thinking_token_budget` Support**

**vLLM v0.19.0 (released April 3, 2026)** introduced proper `thinking_token_budget` support via SamplingParams:
- PR #20859 added "Limit thinking tokens (hard limit)" functionality
- This was listed as an API & Frontend feature in the v0.19.0 release notes
- The feature allows enforcing a hard limit on thinking tokens through `SamplingParams(thinking_token_budget=&lt;value>)`

### 3. **About PR #37112**

PR #37112 was an alternative implementation that introduced a `reasoning_budget` feature to cap thinking tokens via a `ReasoningBudgetLogitsProcessor`. However:
- **This PR was closed without merging** on March 29, 2026
- Maintainer @njhill had already merged the original PR #20859, which superseded it
- The feature ultimately came through PR #20859, not PR #37112

### 4. **Current Stable vLLM Version (May 2026)**

**vLLM v0.20.1** (released May 4, 2026) is the current stable version:
- v0.20.0 was released April 27, 2026 with major features including DeepSeek V4 support
- v0.20.1 is a patch release focused on DeepSeek V4 stabilization
- All versions from v0.19.0 onwards support `thinking_token_budget` properly

### Key Takeaway for Citation

**For correct `thinking_token_budget` support via SamplingParams, cite vLLM v0.19.0 or later.** vLLM v0.18.0 and earlier do not properly support this parameter and will silently ignore it when passed via `extra_args`.

Sources:
- [vLLM v0.19.0 Release Notes](https://github.com/vllm-project/vllm/releases/tag/v0.19.0)
- [thinking_token_budget silently ignored in v0.18.0 - vLLM Forums](https://discuss.vllm.ai/t/thinking-token-budget-silently-ignored-when-passed-via-extra-args-in-vllm-0-18-0/2533)
- [PR #37112: Feature for reasoning_budget](https://github.com/vllm-project/vllm/pull/37112)
- [vLLM Releases](https://github.com/vllm-project/vllm/releases)
- [vLLM Reasoning Outputs Documentation](https://docs.vllm.ai/en/latest/features/reasoning_outputs/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6efe5593-cf1b-44a4-a2b1-8d76a8a4a55f",
  "isSidechain": true,
  "agentId": "a975e6a647a2e7708",
  "requestId": "req_011CasdoHytaaeYJ1hkWbU95",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "639e577f-1141-420f-86c4-522f6912d54e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "51cc101a-f4af-41df-b8a3-35cf057dccbc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VtCtcgRaJER7UvNjYXb381",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 27170,
      "output_tokens": 900,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1226
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 900,
          "cache_read_input_tokens": 27170,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1226,
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
