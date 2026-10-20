# Research conversation: Research the current status of vLLM support for Qwen3 models. Do web searches for: 1. "vLLM Qwen3 support" - is Qwen3 su

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a9a4b2c95e11b9fd6.jsonl`
- **Structured JSON:** [`7567a2f92bf349e213be.json`](../../sessions/75/7567a2f92bf349e213be.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-13T19:16:51.904Z_

Research the current status of vLLM support for Qwen3 models. Do web searches for:

1. "vLLM Qwen3 support" - is Qwen3 supported in vLLM?
2. "vLLM Qwen3ForCausalLM" - architecture support
3. Check vLLM GitHub issues/PRs for Qwen3 support (search "site:github.com vllm-project vllm Qwen3")
4. "vLLM 0.8 Qwen3" or "vLLM 0.9 Qwen3" - which version adds support?
5. Any nightly build or specific branch that supports Qwen3?
6. Expected timeline for official Qwen3 support

Report findings concisely with version numbers and links where available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "a9a4b2c95e11b9fd6",
  "type": "user",
  "uuid": "7880c5e8-3e98-4211-b5e9-d7391a4e685c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T19:16:51.908Z_

```json
{
  "parentUuid": "7880c5e8-3e98-4211-b5e9-d7391a4e685c",
  "isSidechain": true,
  "agentId": "a9a4b2c95e11b9fd6",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "83e60f5f-08f1-4b6e-9712-96286179abeb",
  "timestamp": "2026-05-13T19:16:51.908Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T19:16:54.977Z_



I'll search for vLLM Qwen3 support status across multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83e60f5f-08f1-4b6e-9712-96286179abeb",
  "isSidechain": true,
  "agentId": "a9a4b2c95e11b9fd6",
  "requestId": "req_011Cb173g2WcToHpuS13ALtR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96355ff4-644b-4c04-9e7b-58a996917d68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CYAnM1VvM9p1fZCMXMuaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5976,
      "cache_read_input_tokens": 7333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5976,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 4 · 2026-05-13T19:16:55.495Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Bv2kmyfJpKT5TdsCmLy4os`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96355ff4-644b-4c04-9e7b-58a996917d68",
  "isSidechain": true,
  "agentId": "a9a4b2c95e11b9fd6",
  "requestId": "req_011Cb173g2WcToHpuS13ALtR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d9986ee-add4-4401-93f9-0408c5e641c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CYAnM1VvM9p1fZCMXMuaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5976,
      "cache_read_input_tokens": 7333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5976,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 5 · 2026-05-13T19:16:55.498Z_

<details><summary>↩ Tool result · `toolu_01Bv2kmyfJpKT5TdsCmLy4os`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d9986ee-add4-4401-93f9-0408c5e641c2",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "a9a4b2c95e11b9fd6",
  "type": "user",
  "uuid": "b35809ef-022b-4bc9-b414-2d127aef03ea",
  "sourceToolAssistantUUID": "6d9986ee-add4-4401-93f9-0408c5e641c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-13T19:17:01.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JmJYtDKyh9LoJPoZU6sw1N`</summary>

```json
{
  "query": "vLLM Qwen3 support 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b35809ef-022b-4bc9-b414-2d127aef03ea",
  "isSidechain": true,
  "agentId": "a9a4b2c95e11b9fd6",
  "requestId": "req_011Cb173wrkyVLPryDF9cza6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1dceda98-f916-4fe4-ad73-6da0c356a52d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHrA6FjzgLrRRLs1squ2A2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 13309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 7 · 2026-05-13T19:17:01.801Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JWS7HDHQyXe32G24C7Je6K`</summary>

```json
{
  "query": "vLLM Qwen3ForCausalLM architecture support"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dceda98-f916-4fe4-ad73-6da0c356a52d",
  "isSidechain": true,
  "agentId": "a9a4b2c95e11b9fd6",
  "requestId": "req_011Cb173wrkyVLPryDF9cza6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b83097a-6ec4-41fb-898f-8cf6a12bebee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHrA6FjzgLrRRLs1squ2A2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 13309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 8 · 2026-05-13T19:17:01.929Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NKx13NaWQ57CvRjVu7jeFB`</summary>

```json
{
  "query": "site:github.com vllm-project vllm Qwen3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b83097a-6ec4-41fb-898f-8cf6a12bebee",
  "isSidechain": true,
  "agentId": "a9a4b2c95e11b9fd6",
  "requestId": "req_011Cb173wrkyVLPryDF9cza6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec33c4fa-1928-456f-92c3-f6e660174599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHrA6FjzgLrRRLs1squ2A2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 13309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 9 · 2026-05-13T19:17:02.011Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EXViB3VGCVFsuzJAkiEhpZ`</summary>

```json
{
  "query": "vLLM 0.8 0.9 Qwen3 version support"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec33c4fa-1928-456f-92c3-f6e660174599",
  "isSidechain": true,
  "agentId": "a9a4b2c95e11b9fd6",
  "requestId": "req_011Cb173wrkyVLPryDF9cza6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7d2510c-0664-428a-92c9-4ec7ea5c2c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHrA6FjzgLrRRLs1squ2A2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 13309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 10 · 2026-05-13T19:17:07.314Z_

<details><summary>↩ Tool result · `toolu_01JWS7HDHQyXe32G24C7Je6K`</summary>

```text
Web search results for query: "vLLM Qwen3ForCausalLM architecture support"

Links: [{"title":"[Usage]: Model architectures ['Qwen3ForCausalLM'] are not supported for now. · Issue #22231 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/22231"},{"title":"Supported Models — vLLM","url":"https://docs.vllm.ai/en/v0.8.5/models/supported_models.html"},{"title":"[Usage]: Qwen3ForCausalLM has no vLLM implementation, falling back to Transformers implementation. Some features may not be supported and performance may not be optimal. · Issue #17630 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17630"},{"title":"Can Support Qwen3-VL or Qwen2.5 VL 72B on Vllm-ascend 0.11.0? - Ascend Support - vLLM Forums","url":"https://discuss.vllm.ai/t/can-support-qwen3-vl-or-qwen2-5-vl-72b-on-vllm-ascend-0-11-0/1869"},{"title":"[Usage]: does vllm support Qwen3_5ForCausalLM architecture inference? not just Qwen3_5ForConditionalGeneration? · Issue #39993 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/39993"},{"title":"[Bug]: Error in inspecting model architecture 'Qwen3ForCausalLM' · Issue #20122 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/20122"},{"title":"Supported Models - vLLM","url":"https://docs.vllm.ai/en/v0.10.1/models/supported_models.html"},{"title":"vLLM - Qwen","url":"https://qwen.readthedocs.io/en/latest/deployment/vllm.html"},{"title":"List of Supported Models — vLLM","url":"https://docs.vllm.ai/en/v0.7.0/models/supported_models.html"},{"title":"Qwen3.5 & Qwen3.6 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html"}]

Based on the search results, here's what I found about vLLM's support for the Qwen3ForCausalLM architecture:

## Current Status

The Qwen3ForCausalLM model architecture is not supported natively in vLLM. When attempting to use this architecture, Qwen3ForCausalLM has no vLLM implementation and vLLM falls back to the Transformers implementation, with some features not being supported and performance not being optimal.

## How vLLM Handles Unsupported Architectures

Models do not need to be natively supported to be used in vLLM, as the Transformers backend enables you to run models directly using their Transformers implementation. This means while Qwen3ForCausalLM isn't natively optimized in vLLM, it can still be used through the fallback mechanism, though with reduced performance compared to natively supported architectures.

## Related Observations

There have been multiple GitHub issues and forum discussions about Qwen3 variants lacking native vLLM support, indicating this is an ongoing limitation. The Qwen documentation does mention vLLM support for Qwen models, but native support specifically for the Qwen3ForCausalLM architecture has not been implemented as of the latest available information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b83097a-6ec4-41fb-898f-8cf6a12bebee",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "a9a4b2c95e11b9fd6",
  "type": "user",
  "uuid": "67c40f20-61ce-46aa-9fd5-9cd643bb2a47",
  "sourceToolAssistantUUID": "2b83097a-6ec4-41fb-898f-8cf6a12bebee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T19:17:07.862Z_

<details><summary>↩ Tool result · `toolu_01EXViB3VGCVFsuzJAkiEhpZ`</summary>

```text
Web search results for query: "vLLM 0.8 0.9 Qwen3 version support"

Links: [{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"[Usage] Qwen3 Usage Guide · Issue #17327 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17327"},{"title":"Qwen3.5 & Qwen3.6 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html"},{"title":"vLLM - Qwen","url":"https://qwen.readthedocs.io/en/latest/deployment/vllm.html"},{"title":"Releases · vllm-project/vllm-ascend","url":"https://github.com/vllm-project/vllm-ascend/releases"},{"title":"[Bug]: Value error, Model architectures ['Qwen3_5ForConditionalGeneration'] are not supported for now · Issue #35391 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/35391"},{"title":"Release note — vllm-ascend","url":"https://docs.vllm.ai/projects/ascend/en/v0.9.2rc1/user_guide/release_notes.html"},{"title":"Supported Models - vLLM","url":"https://docs.vllm.ai/en/v0.13.0/models/supported_models/"},{"title":"[Usage]: Support Qwen3 inference in vLLM==0.8.5 with CUDA 11.8 (currently only vLLM==0.6.1.post1 works) · Issue #17578 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17578"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3"}]

Based on the search results, here's what I found regarding vLLM version support for Qwen3 models:

## vLLM Version Support for Qwen3

vLLM v0.8.4 and higher natively supports all Qwen3 and Qwen3MoE models.

### Specific Version Improvements

**Version 0.8.5:** If you are seeing an error when running fp8 dense models on vLLM v0.8.4, please upgrade to v0.8.5.

**Version 0.9.0:** Since vLLM v0.9.0, FP8 Marlin has supported block-wise quants (running as w8a16) and you can also run Qwen3 FP8 models on Ampere cards. Additionally, enable_thinking=False incompatibility is resolved in vLLM 0.9.0 with the qwen3 reasoning parser.

### Summary
- **Minimum version:** vLLM >= 0.8.4 for Qwen3 support
- **Recommended versions:** 0.8.5 or higher for better compatibility and bug fixes
- **Latest improvements:** v0.9.0 includes enhanced FP8 support and reasoning parser improvements


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7d2510c-0664-428a-92c9-4ec7ea5c2c44",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "a9a4b2c95e11b9fd6",
  "type": "user",
  "uuid": "923951e3-a538-49d1-a0c0-98fee355c181",
  "sourceToolAssistantUUID": "d7d2510c-0664-428a-92c9-4ec7ea5c2c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T19:17:08.402Z_

<details><summary>↩ Tool result · `toolu_01JmJYtDKyh9LoJPoZU6sw1N`</summary>

```text
Web search results for query: "vLLM Qwen3 support 2026"

Links: [{"title":"Qwen/Qwen3.5-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-27B"},{"title":"Qwen/Qwen3.6-35B-A3B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-35B-A3B"},{"title":"Qwen3.5 & Qwen3.6 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen/Qwen3.6-27B | vLLM Recipes","url":"https://recipes.vllm.ai/Qwen/Qwen3.6-27B"},{"title":"Supported Models - vLLM","url":"https://docs.vllm.ai/en/latest/models/supported_models/"},{"title":"Day 0 Support for Qwen3.6 on AMD Instinct GPUs","url":"https://www.amd.com/en/developer/resources/technical-articles/2026/day-0-support-for-qwen3-6-on-amd-instinct-gpus.html"},{"title":"Qwen/Qwen3.6-27B-FP8 · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B-FP8"},{"title":"Release Notes — vllm-ascend","url":"https://docs.vllm.ai/projects/ascend/en/main/user_guide/release_notes.html"}]

Based on the search results, here's what I found about vLLM Qwen3 support in 2026:

## vLLM Support for Qwen3 Models

Qwen3.5 and Qwen3.6 artifacts are compatible with vLLM. In fact, for production workloads or high-throughput scenarios, vLLM is strongly recommended as a dedicated serving engine.

### Qwen3.5 Support
vLLM supports serving Qwen3.5 models with command-line options for tensor parallelism, context length configuration, and reasoning parsing.

### Qwen3.6 Support
vllm>=0.19.0 is recommended for Qwen3.6. vLLM provides guidance on how to efficiently deploy and serve both Qwen3.5 and Qwen3.6 models. The integration is comprehensive, with Qwen3.6-27B as the flagship dense model that supports vision+text input and natively serves 262K context.

### Recent Updates
The integration of ROCm 7 software and vLLM allows users to fully exploit GPU capabilities, with vLLM being used for Day 0 deployment support on AMD Instinct GPUs. Additionally, experimental support for Qwen3.x models was added without requiring any code modification in vLLM-Ascend.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1dceda98-f916-4fe4-ad73-6da0c356a52d",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "a9a4b2c95e11b9fd6",
  "type": "user",
  "uuid": "fa10ce6b-fbfc-42a0-9186-4c64b724700f",
  "sourceToolAssistantUUID": "1dceda98-f916-4fe4-ad73-6da0c356a52d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T19:17:11.101Z_

<details><summary>↩ Tool result · `toolu_01NKx13NaWQ57CvRjVu7jeFB`</summary>

```text
Web search results for query: "site:github.com vllm-project vllm Qwen3"

Links: [{"title":"[Usage] Qwen3 Usage Guide · Issue #17327 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17327"},{"title":"recipes/Qwen/Qwen3.5.md at main · vllm-project/recipes","url":"https://github.com/vllm-project/recipes/blob/main/Qwen/Qwen3.5.md"},{"title":"GitHub - QwenLM/Qwen3-VL: Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3-VL"},{"title":"vllm-ascend/docs/source/tutorials/Qwen3-Next.md at v0.13.0rc1 · vllm-project/vllm-ascend","url":"https://github.com/vllm-project/vllm-ascend/blob/v0.13.0rc1/docs/source/tutorials/Qwen3-Next.md"},{"title":"[Performance]: qwen3.5 vs qwen3 · Issue #36627 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/36627"},{"title":"recipes/Qwen/Qwen3.md at main · vllm-project/recipes","url":"https://github.com/vllm-project/recipes/blob/main/Qwen/Qwen3.md"},{"title":"vllm/vllm/model_executor/models/qwen3.py at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/qwen3.py"},{"title":"recipes/Qwen/Qwen3-Next.md at main · vllm-project/recipes","url":"https://github.com/vllm-project/recipes/blob/main/Qwen/Qwen3-Next.md"},{"title":"[Bug]: Qwen 3.5 fails to load from GGUF · Issue #38122 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/38122"},{"title":"vllm/examples/pooling/score/qwen3_reranker.py at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/qwen3_reranker.py"}]

The search results show several GitHub resources related to vLLM and Qwen3 model support:

## Key Findings:

1. **Native Support**: vLLM v0.8.4 and higher natively supports all Qwen3 and Qwen3MoE models.

2. **Usage and Documentation**:
   - Example commands show using `vllm serve Qwen/...` with flags like `--enable-reasoning` and `--reasoning-parser deepseek_r1` or `qwen3`
   - A dedicated guide provides step-by-step instructions for running the Qwen3 series using vLLM, intended for developers seeking high-throughput or low-latency inference.

3. **Qwen3 Variants Supported**:
   - Qwen3 (base models)
   - Qwen3.5 and Qwen3.6 are multimodal mixture-of-experts models featuring a gated delta networks architecture.
   - Qwen3-Next is an advanced large language model created by the Qwen team from Alibaba Cloud.
   - Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud.

4. **Recipes and Examples**: The vllm-project/recipes repository contains detailed deployment guides for Qwen3, Qwen3.5, Qwen3-Next, and other Qwen3 variants with specific optimization strategies for different hardware configurations.

The search results include GitHub issues, documentation, example code, and deployment guides specifically for using Qwen3 models with vLLM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec33c4fa-1928-456f-92c3-f6e660174599",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "a9a4b2c95e11b9fd6",
  "type": "user",
  "uuid": "c723c958-f4a0-4996-9c04-d0aaafaf37ab",
  "sourceToolAssistantUUID": "ec33c4fa-1928-456f-92c3-f6e660174599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T19:17:13.758Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LtK11WvrTNfTyKezzr7eqe`</summary>

```json
{
  "query": "vLLM Qwen3 native implementation qwen3.py merged PR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c723c958-f4a0-4996-9c04-d0aaafaf37ab",
  "isSidechain": true,
  "agentId": "a9a4b2c95e11b9fd6",
  "requestId": "req_011Cb17565eNskPweoszXHX1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f00ade56-41d3-44da-80d8-88b3f5023d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3AbhR1pkxCsEtPaWSpLQ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 928,
      "cache_creation_input_tokens": 3273,
      "cache_read_input_tokens": 14771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3273,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 15 · 2026-05-13T19:17:14.224Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QZimYRqoYzr8xaQfE3qnmd`</summary>

```json
{
  "query": "github.com vllm-project vllm issues 17327 Qwen3 usage guide"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f00ade56-41d3-44da-80d8-88b3f5023d6b",
  "isSidechain": true,
  "agentId": "a9a4b2c95e11b9fd6",
  "requestId": "req_011Cb17565eNskPweoszXHX1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fcf8eab-a2b4-4213-8784-01bcae8343db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3AbhR1pkxCsEtPaWSpLQ5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 928,
      "cache_creation_input_tokens": 3273,
      "cache_read_input_tokens": 14771,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3273
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 928,
          "output_tokens": 126,
          "cache_read_input_tokens": 14771,
          "cache_creation_input_tokens": 3273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3273,
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

### Tool result

_source line 16 · 2026-05-13T19:17:18.752Z_

<details><summary>↩ Tool result · `toolu_01LtK11WvrTNfTyKezzr7eqe`</summary>

```text
Web search results for query: "vLLM Qwen3 native implementation qwen3.py merged PR"

Links: [{"title":"Qwen3.5 & Qwen3.6 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html"},{"title":"Qwen3-VL Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-VL.html"},{"title":"vLLM - Qwen","url":"https://qwen.readthedocs.io/en/latest/deployment/vllm.html"},{"title":"[Model] Add Qwen3 and Qwen3MoE by YamPengLi · Pull Request #15289 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/15289"},{"title":"Qwen/Qwen3.6-27B | vLLM Recipes","url":"https://recipes.vllm.ai/Qwen/Qwen3.6-27B"},{"title":"vllm/vllm/model_executor/models/qwen3.py at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/qwen3.py"},{"title":"Qwen3 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.html"},{"title":"GitHub - QwenLM/Qwen3-VL: Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3-VL"},{"title":"【main】SP For Qwen3 MoE by lbk-sys · Pull Request #2209 · vllm-project/vllm-ascend","url":"https://github.com/vllm-project/vllm-ascend/pull/2209"},{"title":"Qwen3-Coder Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Coder-480B-A35B.html"}]

Based on the search results, I found information about the vLLM Qwen3 native implementation:

The implementation of Qwen3 and Qwen3MoE model structure is provided through two files: qwen3.py and qwen3_moe.py. This was contributed through Pull Request #15289 on the vLLM project.

The search results show that the qwen3.py file is available in the vLLM repository at vllm/model_executor/models/qwen3.py, indicating that the native implementation has been integrated into the main vLLM codebase.

The PR included comprehensive model support, with the contributor having submitted a pull request to Hugging Face Transformers containing the implementation of the Qwen3 and Qwen3MoE models, and seeking to contribute these new models to vLLM as well.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f00ade56-41d3-44da-80d8-88b3f5023d6b",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "a9a4b2c95e11b9fd6",
  "type": "user",
  "uuid": "4c4b6fef-8ac5-4c62-b8dd-9727d1a8069b",
  "sourceToolAssistantUUID": "f00ade56-41d3-44da-80d8-88b3f5023d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T19:17:20.356Z_

<details><summary>↩ Tool result · `toolu_01QZimYRqoYzr8xaQfE3qnmd`</summary>

```text
Web search results for query: "github.com vllm-project vllm issues 17327 Qwen3 usage guide"

Links: [{"title":"[Usage] Qwen3 Usage Guide · Issue #17327 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17327"},{"title":"Qwen3.5 & Qwen3.6 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html"},{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"recipes/Qwen/Qwen3.md at main · vllm-project/recipes","url":"https://github.com/vllm-project/recipes/blob/main/Qwen/Qwen3.md"},{"title":"recipes/Qwen/Qwen3.5.md at main · vllm-project/recipes","url":"https://github.com/vllm-project/recipes/blob/main/Qwen/Qwen3.5.md"},{"title":"GitHub - QwenLM/Qwen3-VL: Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3-VL"},{"title":"[Performance]: qwen3.5 vs qwen3 · Issue #36627 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/36627"},{"title":"vLLM - Qwen","url":"https://qwen.readthedocs.io/en/latest/deployment/vllm.html"},{"title":"Qwen3-VL Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-VL.html"},{"title":"Qwen3 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.html"}]

I found the GitHub issue you were looking for! Here are the key findings from the search results:

## GitHub Issue #17327: Qwen3 Usage Guide

vLLM v0.8.4 and higher natively supports all Qwen3 and Qwen3MoE models. The example command is: vllm serve Qwen/... --enable-reasoning --reasoning-parser deepseek_r1

### Key Points from the Issue:

**Testing the Reasoning Parser:**
You can test the reasoning parser with the example script at https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_with_reasoning_streaming.py

**MoE Model Configuration:**
Some MoE models might not be divisible by TP 8. Either lower your TP size or use --enable-expert-parallel.

**Known Issues:**

If you are seeing an error when running fp8 dense models on vLLM v0.8.4, please upgrade to v0.8.5.

The issue also documents various error messages and solutions for running Qwen3 models with different quantization schemes and tensor parallelization configurations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fcf8eab-a2b4-4213-8784-01bcae8343db",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "a9a4b2c95e11b9fd6",
  "type": "user",
  "uuid": "4cf2ad46-598b-496b-b7e8-588e36410fab",
  "sourceToolAssistantUUID": "6fcf8eab-a2b4-4213-8784-01bcae8343db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-13T19:17:40.283Z_

Here are the findings on vLLM Qwen3 support:

---

## vLLM Qwen3 Support Status

### Native Support: YES, since v0.8.4

vLLM **natively supports** all Qwen3 and Qwen3MoE models starting from **v0.8.4**. The implementation lives at `vllm/model_executor/models/qwen3.py` and `qwen3_moe.py`, added via [PR #15289](https://github.com/vllm-project/vllm/pull/15289).

### Version Details

| Version | Qwen3 Status |
|---------|-------------|
| **v0.8.4** | First version with native Qwen3/Qwen3MoE support. Has a bug with FP8 dense models. |
| **v0.8.5** | Fixes FP8 dense model errors. Recommended minimum. |
| **v0.9.0** | FP8 Marlin block-wise quants (w8a16), Qwen3 FP8 on Ampere cards, fixed `enable_thinking=False` with qwen3 reasoning parser. |
| **v0.19.0+** | Recommended for Qwen3.5/Qwen3.6 (newer model generations). |

### Usage

```bash
vllm serve Qwen/Qwen3-30B-A3B --enable-reasoning --reasoning-parser qwen3
```

For MoE models not divisible by TP 8, use `--enable-expert-parallel` or lower TP size.

### The "Qwen3ForCausalLM not supported" Error

GitHub issues [#22231](https://github.com/vllm-project/vllm/issues/22231), [#17630](https://github.com/vllm-project/vllm/issues/17630), and [#20122](https://github.com/vllm-project/vllm/issues/20122) report this error. This occurs when using an **older vLLM version** (< 0.8.4). The fix is to upgrade to v0.8.4+. On older versions, vLLM falls back to the Transformers backend with degraded performance.

### Qwen3 Model Family Coverage in vLLM

- **Qwen3** (dense + MoE): native support since v0.8.4
- **Qwen3-VL**: supported, with [dedicated recipe](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-VL.html)
- **Qwen3.5 / Qwen3.6**: newer generations, require vLLM >= 0.19.0
- **Qwen3-Coder**: supported, with [dedicated recipe](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Coder-480B-A35B.html)

### Key Resources

- Official usage guide: [Issue #17327](https://github.com/vllm-project/vllm/issues/17327)
- Qwen3 recipe: [vllm-project/recipes Qwen3.md](https://github.com/vllm-project/recipes/blob/main/Qwen/Qwen3.md)
- vLLM docs recipe: [Qwen3 Usage Guide](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.html)
- Qwen official vLLM docs: [qwen.readthedocs.io/deployment/vllm](https://qwen.readthedocs.io/en/latest/deployment/vllm.html)
- Supported models list: [docs.vllm.ai/models/supported_models](https://docs.vllm.ai/en/latest/models/supported_models/)

### Bottom Line

For the original Qwen3 series: **use vLLM >= 0.8.5** (or >= 0.9.0 for FP8/reasoning parser improvements). No nightly/special branch needed -- it's in stable releases.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cf2ad46-598b-496b-b7e8-588e36410fab",
  "isSidechain": true,
  "agentId": "a9a4b2c95e11b9fd6",
  "requestId": "req_011Cb175meQMM9KnqxoS1K2L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3f54fe0-9f4d-4822-b6d8-67413b98ac7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNtEjDpRWjUyRh2q398Cxs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2833,
      "cache_read_input_tokens": 18044,
      "output_tokens": 1034,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1034,
          "cache_read_input_tokens": 18044,
          "cache_creation_input_tokens": 2833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2833,
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
