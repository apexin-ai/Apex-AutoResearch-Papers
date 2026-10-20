# Research conversation: Research SGLang's support for Qwen3 models and its custom LogitsProcessor API. Do web searches for: 1. "SGLang Qwen3 sup

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae97f643a35d5a194.jsonl`
- **Structured JSON:** [`63ea73165cebce27ad6c.json`](../../sessions/63/63ea73165cebce27ad6c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-13T19:16:48.201Z_

Research SGLang's support for Qwen3 models and its custom LogitsProcessor API. Do web searches for:

1. "SGLang Qwen3 support" - does SGLang support Qwen3-8B? Which version?
2. "SGLang custom LogitsProcessor" or "SGLang logit bias" - how to implement custom logits processing
3. "SGLang constrained decoding" or "SGLang XGrammar" - SGLang's built-in grammar-based decoding
4. SGLang LogitsProcessor API signature - __init__, __call__ methods, can you intercept logits at token level?
5. SGLang installation with CUDA 12.8 and Blackwell GPU (RTX PRO 6000) compatibility

Report findings concisely with code examples where available. Include version numbers and any limitations found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "8c186e24-8730-40b3-8094-6b8973fc0efd",
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

_source line 2 · 2026-05-13T19:16:48.208Z_

```json
{
  "parentUuid": "8c186e24-8730-40b3-8094-6b8973fc0efd",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
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
  "uuid": "877704f2-1bf5-4917-bd50-151b56a5e039",
  "timestamp": "2026-05-13T19:16:48.208Z",
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

_source line 3 · 2026-05-13T19:16:51.097Z_



I'll research these topics in parallel using web searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "877704f2-1bf5-4917-bd50-151b56a5e039",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb173QJxUzQdCtzqnDVNq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4865d787-c1fd-46e4-b4a2-9909ffc8315c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHWVwmHosvGkDA2vYkyHPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13311,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13311,
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

_source line 4 · 2026-05-13T19:16:51.397Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SF9ajrgoiyUGenuLASsTaf`</summary>

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
  "parentUuid": "4865d787-c1fd-46e4-b4a2-9909ffc8315c",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb173QJxUzQdCtzqnDVNq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d84c8cc0-746f-4a4e-bdc7-4993606563b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHWVwmHosvGkDA2vYkyHPA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13311,
      "cache_read_input_tokens": 0,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13311
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 13311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13311,
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

_source line 5 · 2026-05-13T19:16:51.401Z_

<details><summary>↩ Tool result · `toolu_01SF9ajrgoiyUGenuLASsTaf`</summary>

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
  "parentUuid": "d84c8cc0-746f-4a4e-bdc7-4993606563b3",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "46f5b37e-9f22-4fe8-ba84-457c48ce8ba2",
  "sourceToolAssistantUUID": "d84c8cc0-746f-4a4e-bdc7-4993606563b3",
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

_source line 6 · 2026-05-13T19:16:55.169Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UxEzGckzTpyS3jf8Mn4eAz`</summary>

```json
{
  "query": "SGLang Qwen3 support model serving 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46f5b37e-9f22-4fe8-ba84-457c48ce8ba2",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb173eKpUYbRXtKVV8Adz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98c683dd-a2e8-4e63-8c74-0065f3a3bfe9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KoEZCVjZXrfS8GoF7Yas7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 13311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 7 · 2026-05-13T19:16:56.115Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L97JuUfavMJx61RMuuzsFY`</summary>

```json
{
  "query": "SGLang custom LogitsProcessor API logit bias implementation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98c683dd-a2e8-4e63-8c74-0065f3a3bfe9",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb173eKpUYbRXtKVV8Adz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb0fa6b1-af55-47e4-9997-0462589004bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KoEZCVjZXrfS8GoF7Yas7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 13311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 8 · 2026-05-13T19:16:56.602Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014rDvZGz417kg9NooFWtQsX`</summary>

```json
{
  "query": "SGLang constrained decoding XGrammar grammar-based decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb0fa6b1-af55-47e4-9997-0462589004bf",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb173eKpUYbRXtKVV8Adz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f55dad46-2b96-496f-a66d-799cc12e5f96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KoEZCVjZXrfS8GoF7Yas7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 13311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 9 · 2026-05-13T19:16:57.056Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01APLHnVGiK4ogZ5cDk6wL9e`</summary>

```json
{
  "query": "SGLang LogitsProcessor __call__ signature token level intercept"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f55dad46-2b96-496f-a66d-799cc12e5f96",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb173eKpUYbRXtKVV8Adz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4a1842d-68c2-41ae-8f3e-0767ab15603e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KoEZCVjZXrfS8GoF7Yas7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 13311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 10 · 2026-05-13T19:16:57.985Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QZWbziMsRGHNNA2fbxrgxP`</summary>

```json
{
  "query": "SGLang install CUDA 12.8 Blackwell GPU RTX PRO 6000 compatibility 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4a1842d-68c2-41ae-8f3e-0767ab15603e",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb173eKpUYbRXtKVV8Adz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7ca4118-70f9-4a58-852a-81c69ed131be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KoEZCVjZXrfS8GoF7Yas7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 13311,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 274,
          "cache_read_input_tokens": 13311,
          "cache_creation_input_tokens": 1452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1452,
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

_source line 11 · 2026-05-13T19:17:01.867Z_

<details><summary>↩ Tool result · `toolu_01UxEzGckzTpyS3jf8Mn4eAz`</summary>

```text
Web search results for query: "SGLang Qwen3 support model serving 2026"

Links: [{"title":"SGLang - Qwen","url":"https://qwen.readthedocs.io/en/latest/deployment/sglang.html"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen 3.5 Usage — SGLang","url":"https://docs.sglang.io/basic_usage/qwen3_5.html"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Day 0 Support for Qwen3.6 on AMD Instinct GPUs","url":"https://www.amd.com/en/developer/resources/technical-articles/2026/day-0-support-for-qwen3-6-on-amd-instinct-gpus.html"},{"title":"Qwen3.6-27B: 27B Model Beats 397B on Coding (2026)","url":"https://www.buildfastwithai.com/blogs/qwen3-6-27b-review-2026"},{"title":"Qwen/Qwen3.5-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-27B"},{"title":"Qwen/Qwen3-Coder-Next · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Coder-Next"},{"title":"Qwen3.6 | SGLang Cookbook","url":"https://cookbook.sglang.io/autoregressive/Qwen/Qwen3.6"},{"title":"Qwen3.5 | SGLang Cookbook","url":"https://cookbook.sglang.io/autoregressive/Qwen/Qwen3.5"}]

Based on the search results, here's what I found about SGLang's support for Qwen3 model serving in 2026:

## SGLang Support for Qwen3 Models

Qwen3.6 is supported by multiple inference frameworks, with SGLang being a fast serving framework for large language models and vision language models that can be used to launch a server with OpenAI-compatible API service.

### Recent Qwen3 Releases (2026)

As of February 16, 2026, Qwen3.5 was released, with the first release including a 397B-A17B MoE model. More recently, Qwen3.6-27B became available in April 2026.

### SGLang Version Requirements

SGLang >=0.5.10 is required for Qwen3.6. SGLang version 0.5.10 is recommended for Qwen3.6.

### Deployment Features

SGLang can be used to launch a server with commands that support context lengths up to 262,144 tokens and include a reasoning-parser for qwen3. Additionally, SGLang (version 0.5.10+) supports Qwen3.6-27B with full tool-calling and reasoning parsing.

The search results show comprehensive support for Qwen3 models (both Qwen3.5 and Qwen3.6 variants) through SGLang as of 2026, with robust features for model serving and inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98c683dd-a2e8-4e63-8c74-0065f3a3bfe9",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "cf10d642-1b3b-4cf6-a7cf-c8855380cc90",
  "sourceToolAssistantUUID": "98c683dd-a2e8-4e63-8c74-0065f3a3bfe9",
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

_source line 12 · 2026-05-13T19:17:02.506Z_

<details><summary>↩ Tool result · `toolu_01L97JuUfavMJx61RMuuzsFY`</summary>

```text
Web search results for query: "SGLang custom LogitsProcessor API logit bias implementation 2026"

Links: [{"title":"How to Support New Models — SGLang","url":"https://sgl-project.github.io/supported_models/extending/support_new_models.html"},{"title":"[Feature] Support a custom logit processor · Issue #2291 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/2291"},{"title":"OpenAI APIs - Completions — SGLang","url":"https://docs.sglang.io/basic_usage/openai_api_completions.html"},{"title":"Sampling Parameters — SGLang","url":"https://docs.sglang.io/basic_usage/sampling_params.html"},{"title":"[Feature] Allow arbitrary logit processors · Issue #1036 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/1036"},{"title":"[Feature] Logit Bias Not Working · Issue #6749 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/6749"},{"title":"[RFC] Extensible Tokenizer and Logits Processor Architecture · Issue #94 · sgl-project/sglang-omni","url":"https://github.com/sgl-project/sglang-omni/issues/94"},{"title":"[Bug] `logit_bias` may not work as expected with OpenAI API · Issue #6171 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/6171"},{"title":"Logits Processors - vLLM","url":"https://docs.vllm.ai/en/latest/design/logits_processors/"},{"title":"Efficiently Programming Large Language Models using SGLang","url":"https://arxiv.org/html/2312.07104v1"}]

Based on the search results, here's what I found about SGLang's custom LogitsProcessor API and logit bias implementation:

## Custom LogitsProcessor API

SGLang supports custom logit processors by launching a server with the `--enable-custom-logit-processor` flag. Users can define custom logit processors by inheriting from the `CustomLogitProcessor` class.

The implementation involves creating a custom processor class with a `__call__` method. The processor receives logits and a list of custom parameters, allowing modifications to the logits tensor for each item in the batch. This can be used for various sampling techniques and constraints.

## Logit Bias Implementation

SGLang supports the logit_bias parameter for both chat completions and completions APIs, which allows modification of token likelihood by adding bias values to their logits, with values ranging from -100 to 100.

## Recent Development (2026)

SGLang's CustomLogitProcessor is described as a pragmatic extension point that unifies built-in and custom sampling into one composable pipeline, with design patterns that include custom_params passthrough and request state access.

It's worth noting that there have been some reported issues with logit_bias not working as expected in certain scenarios, but the API framework exists and is actively maintained as of 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb0fa6b1-af55-47e4-9997-0462589004bf",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "b6abe406-8a51-4e95-9f3d-8ac36a2ff3d5",
  "sourceToolAssistantUUID": "cb0fa6b1-af55-47e4-9997-0462589004bf",
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

_source line 13 · 2026-05-13T19:17:04.179Z_

<details><summary>↩ Tool result · `toolu_01APLHnVGiK4ogZ5cDk6wL9e`</summary>

````text
Web search results for query: "SGLang LogitsProcessor __call__ signature token level intercept"

Links: [{"title":"[RFC] Extensible Tokenizer and Logits Processor Architecture · Issue #94 · sgl-project/sglang-omni","url":"https://github.com/sgl-project/sglang-omni/issues/94"},{"title":"Sampling Parameters — SGLang","url":"https://docs.sglang.io/basic_usage/sampling_params.html"},{"title":"Model Execution and Forward Pass | sgl-project/sglang | DeepWiki","url":"https://deepwiki.com/sgl-project/sglang/4.3-server-configuration-(serverargs)"},{"title":"Welcome to SGLang - SGLang Documentation","url":"https://docs.sglang.io/"},{"title":"[Feature] Support a custom logit processor · Issue #2291 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/2291"},{"title":"GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub","url":"https://github.com/sgl-project/sglang"},{"title":"SGLang Documentation — SGLang","url":"https://sgl-project.github.io/"},{"title":"Efficiently Programming Large Language Models using SGLang","url":"https://arxiv.org/html/2312.07104v1"},{"title":"How to Install and Use SGLang","url":"https://www.gpu-mart.com/blog/how-to-install-and-use-sglang"},{"title":"[Feature] Get Input Token IDs and Output Token IDs with `Engine.generate()` · Issue #2634 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/2634"}]

Based on the search results, I found information about SGLang's LogitsProcessor `__call__` signature:

The LogitsProcessor `__call__` signature is defined as:

```python
def __call__(
    self,
    logits: torch.Tensor,  # [batch, vocab] in batch mode
    context: SamplingContext | list[SamplingContext],
) -> torch.Tensor:
```

In the current implementation for custom logit processors, the `__call__` method takes `logits` and `custom_param_list` as parameters, where the logits tensor contains the token probabilities that can be modified at the batch level.

Regarding token-level intercept specifically, SGLang's pattern involves processors receiving logits[batch, vocab] for the entire batch, with a mask tensor selecting relevant requests, enabling one kernel call for the whole batch. However, the current design uses per-request SamplingContext — the pipeline is called once per request with logits[1, vocab], which is simpler to implement and debug.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4a1842d-68c2-41ae-8f3e-0767ab15603e",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "1cac088d-af5f-4586-a1ec-cc785b551fc6",
  "sourceToolAssistantUUID": "c4a1842d-68c2-41ae-8f3e-0767ab15603e",
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

_source line 14 · 2026-05-13T19:17:04.386Z_

<details><summary>↩ Tool result · `toolu_01QZWbziMsRGHNNA2fbxrgxP`</summary>

```text
Web search results for query: "SGLang install CUDA 12.8 Blackwell GPU RTX PRO 6000 compatibility 2026"

Links: [{"title":"[Bug] RTX PRO 6000 Blackwell Cuda 13 · Issue #13342 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/13342"},{"title":"SGLang Release 25.11 - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/sglang-release-notes/rel-25-11.html"},{"title":"[Bug] RTX6000 pro (Blackwell) with FP8 · Issue #16816 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/16816"},{"title":"EP=8 on RTX PRO 6000 Blackwell Server Edition (SM120): garbage output with FP8 and INT4 models · Issue #21132 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/21132"},{"title":"SGL on RTX 6000 Pro Blackwell · sgl-project/sglang · Discussion #12923","url":"https://github.com/sgl-project/sglang/discussions/12923"},{"title":"RN-08516-001_v26.04 | April 2026 SGLang Release Notes","url":"https://docs.nvidia.com/deeplearning/frameworks/pdf/SGLang-Release-Notes.pdf"},{"title":"Disaggregated Prefill/Decode using SGlang and nixl (Dual NVIDIA RTX PRO 6000 Blackwell) - TensorRT - NVIDIA Developer Forums","url":"https://forums.developer.nvidia.com/t/disaggregated-prefill-decode-using-sglang-and-nixl-dual-nvidia-rtx-pro-6000-blackwell/361316"},{"title":"SGLang Release 26.03 - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/sglang-release-notes/rel-26-03.html"},{"title":"SGLang Release 26.02 - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/sglang-release-notes/rel-26-02.html"},{"title":"SGLang Release 25.10 - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/sglang-release-notes/rel-25-10.html"}]

Based on the search results, here's what I found regarding SGLang installation with CUDA 12.8 and RTX PRO 6000 Blackwell GPU compatibility:

## Compatibility Status

RTX PRO 6000 Blackwell Server Edition support is included in SGLang releases, with recent releases like SGLang 25.11, 26.02, and 26.03 all featuring this support. Real-world testing has confirmed the RTX PRO 6000 Blackwell GPU works with SGLang, with compute capability 12.0.

## CUDA 12.8 Driver Requirements

Regarding CUDA 12.8 specifically, it's important to note that users should upgrade from all R418, R440, R450, R460, R510, R520, R530, R545 and R555 and R560 drivers, which are not forward-compatible with CUDA 12.8. You'll need a compatible driver version to use CUDA 12.8 properly.

## Recent Usage Examples (2026)

Recent community reports from 2026 show successful deployments of SGLang with the RTX PRO 6000 Blackwell. For example, users have successfully configured the system with CUDA 13.0, PyTorch 2.9.1+cu128, and SGLang 0.5.7. Additionally, setup guides document installing SGLang with PyTorch using CUDA 13.0 support for RTX PRO 6000 Blackwell systems.

## Summary

The RTX PRO 6000 Blackwell is well-supported in current SGLang releases. However, ensure your NVIDIA drivers are compatible with CUDA 12.8, and consider that recent successful deployments have been documented with CUDA 13.0 as well.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7ca4118-70f9-4a58-852a-81c69ed131be",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "20443ade-5fc9-4753-9a70-b94244bd84f7",
  "sourceToolAssistantUUID": "d7ca4118-70f9-4a58-852a-81c69ed131be",
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

_source line 15 · 2026-05-13T19:17:05.403Z_

<details><summary>↩ Tool result · `toolu_014rDvZGz417kg9NooFWtQsX`</summary>

```text
Web search results for query: "SGLang constrained decoding XGrammar grammar-based decoding"

Links: [{"title":"Guided Decoding Performance on vLLM and SGLang - The official SqueezeBits Tech blog","url":"https://blog.squeezebits.com/guided-decoding-performance-vllm-sglang"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"Constrained Decoding | sgl-project/sgl-learning-materials | DeepWiki","url":"https://deepwiki.com/sgl-project/sgl-learning-materials/3.3-constrained-decoding"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.15100v3"},{"title":"SGLang Deep Dive: Inside SGLang - SugiV Blog","url":"https://blog.sugiv.fyi/sglang-deep-dive-inside-sglang"},{"title":"[Feature] Support llguidance for constrained decoding by JC1DA · Pull Request #3298 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/pull/3298"},{"title":"[PDF] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGrammar:-Flexible-and-Efficient-Structured-Engine-Dong-Ruan/274ca059ee4997f1e008bc8962aef3d22897f17a"},{"title":"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/html/2601.04426v2"},{"title":"Structured Outputs | sihyeong/Awesome-LLM-Inference-Engine | DeepWiki","url":"https://deepwiki.com/sihyeong/Awesome-LLM-Inference-Engine/4.7-structured-outputs"}]

Based on the search results, here's what I found about SGLang constrained decoding, XGrammar, and grammar-based decoding:

## Overview

Constrained decoding (also known as structured output) addresses the need to constrain generation to formats like JSON, XML, or regex-defined strings. Modern serving frameworks like vLLM and SGLang use powerful grammar backends to enforce these rules, with two prominent players being XGrammar and LLGuidance.

## How Constrained Decoding Works

Guided decoding works by restricting the model's next-token choices to only those that are grammatically valid given the context so far. Constrained decoding restricts an LLM's output to follow specific patterns or structures, and unlike standard generation where models can output any token in their vocabulary, constrained decoding enforces rules about what tokens can be generated at each step, ensuring outputs conform to predefined formats.

## XGrammar

XGrammar supports general context-free grammar to enable a broad range of structures, including JSON, regex, custom context-free grammar, etc. XGrammar uses a pushdown automaton to parse the prior LLM output, flexibly supporting diverse grammars and producing matching stack states, then uses the stack top to index into the adaptive token mask cache to retrieve a partial mask.

XGrammar can achieve up to 100x speedup over existing solutions. It is the default structured generation backend for most LLM inference engines, including vLLM, SGLang, TensorRT-LLM, and MLC-LLM.

## SGLang's Implementation

SGLang takes optimization a step further by also overlapping the per-step mask generation with the LLM inference step, more effectively hiding the latency of the grammar processing. SGLang's constrained decoding capabilities are complementary to XGrammar, which is described as a flexible and efficient structured generation engine for large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f55dad46-2b96-496f-a66d-799cc12e5f96",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "73c6e84d-035f-41f9-89f4-0c10343f83ad",
  "sourceToolAssistantUUID": "f55dad46-2b96-496f-a66d-799cc12e5f96",
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

_source line 16 · 2026-05-13T19:17:08.427Z_

Let me get more specific details on the LogitsProcessor API and the Qwen3-8B support.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73c6e84d-035f-41f9-89f4-0c10343f83ad",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb174fkfnfBnqtkKNhAps",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33e30406-d636-400f-aa5c-ae99bc923d5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fVdyzBBmf5d6iUHtxkDTc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1856,
      "cache_creation_input_tokens": 17828,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17828,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 17 · 2026-05-13T19:17:09.376Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019kkpHRJeH6E2EKmS4WL8u6`</summary>

```json
{
  "query": "SGLang CustomLogitProcessor example code __call__ custom_param_list 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33e30406-d636-400f-aa5c-ae99bc923d5c",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb174fkfnfBnqtkKNhAps",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6ce04a6-a872-4380-8b5f-b9471baedea4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fVdyzBBmf5d6iUHtxkDTc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1856,
      "cache_creation_input_tokens": 17828,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17828,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 18 · 2026-05-13T19:17:09.853Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B6AvHEPogx4DsjWQzZ8f4N`</summary>

```json
{
  "query": "SGLang Qwen3-8B model launch server command 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6ce04a6-a872-4380-8b5f-b9471baedea4",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb174fkfnfBnqtkKNhAps",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92d6f135-af0d-4054-b070-2605e75f0199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fVdyzBBmf5d6iUHtxkDTc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1856,
      "cache_creation_input_tokens": 17828,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17828,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 19 · 2026-05-13T19:17:10.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P41gzcNmKB7uWyDxv4WB2M`</summary>

```json
{
  "query": "SGLang --enable-custom-logit-processor usage example sampling params"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92d6f135-af0d-4054-b070-2605e75f0199",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb174fkfnfBnqtkKNhAps",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "355ccf47-a164-472c-9f8b-3aedf3b8f784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fVdyzBBmf5d6iUHtxkDTc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1856,
      "cache_creation_input_tokens": 17828,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17828,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 20 · 2026-05-13T19:17:11.364Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HBxDSd6E81EurQkyXtavSE`</summary>

```json
{
  "query": "SGLang XGrammar JSON schema constrained decoding API usage json_schema regex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "355ccf47-a164-472c-9f8b-3aedf3b8f784",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb174fkfnfBnqtkKNhAps",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "151bcab7-787a-43fc-80c6-8ffe4dadd396",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fVdyzBBmf5d6iUHtxkDTc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1856,
      "cache_creation_input_tokens": 17828,
      "cache_read_input_tokens": 0,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1856,
          "output_tokens": 252,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17828,
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

_source line 21 · 2026-05-13T19:17:15.109Z_

<details><summary>↩ Tool result · `toolu_01B6AvHEPogx4DsjWQzZ8f4N`</summary>

```text
Web search results for query: "SGLang Qwen3-8B model launch server command 2025"

Links: [{"title":"SGLang - Qwen","url":"https://qwen.readthedocs.io/en/latest/deployment/sglang.html"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen3-VL Usage — SGLang","url":"https://docs.sglang.io/basic_usage/qwen3_vl.html"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen3-Coder-Next | SGLang Cookbook","url":"https://cookbook.sglang.io/autoregressive/Qwen/Qwen3-Coder-Next"},{"title":"Qwen 3.5 Usage — SGLang","url":"https://docs.sglang.io/basic_usage/qwen3_5.html"},{"title":"sglang/docs/advanced_features/server_arguments.md at main · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/blob/main/docs/advanced_features/server_arguments.md"},{"title":"Qwen3.5 | SGLang Cookbook","url":"https://cookbook.sglang.io/autoregressive/Qwen/Qwen3.5"},{"title":"Qwen/Qwen3.5-0.8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-0.8B"},{"title":"unsloth/Qwen3-Coder-Next-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF"}]

Based on the search results, I found the SGLang launch server command for the Qwen3-8B model:

To launch a server with the Qwen3-8B model using SGLang, use: `python -m sglang.launch_server --model-path Qwen/Qwen3-8B`

By default, if the --model-path does not point to a valid local directory, it will download the model files from the Hugging Face Hub.

Additionally, for more advanced configurations, you can customize the command with various parameters:

- **Port configuration**: Add `--port 30000` (or your preferred port)
- **GPU acceleration**: Use `--tp-size` for tensor parallelism across multiple GPUs (e.g., `--tp 4` for 4 GPUs)
- **Memory optimization**: Use `--mem-fraction-static` to adjust memory allocation
- **Tool calling support**: Add `--tool-call-parser qwen3_coder` to enable tool calling capabilities

For example, a more complete command might look like:
`python -m sglang.launch_server --model-path Qwen/Qwen3-8B --port 30000 --tp 2`

Once the server is running, you can use the OpenAI-compatible API by making requests to `http://localhost:30000/v1/chat/completions`


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92d6f135-af0d-4054-b070-2605e75f0199",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "6e0f8974-9d3d-4e03-8a94-f3c2f6ff0412",
  "sourceToolAssistantUUID": "92d6f135-af0d-4054-b070-2605e75f0199",
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

_source line 22 · 2026-05-13T19:17:16.332Z_

<details><summary>↩ Tool result · `toolu_019kkpHRJeH6E2EKmS4WL8u6`</summary>

```text
Web search results for query: "SGLang CustomLogitProcessor example code __call__ custom_param_list 2025 2026"

Links: [{"title":"[RFC] Extensible Tokenizer and Logits Processor Architecture · Issue #94 · sgl-project/sglang-omni","url":"https://github.com/sgl-project/sglang-omni/issues/94"},{"title":"[Feature] Support a custom logit processor · Issue #2291 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/2291"},{"title":"SGLang Documentation — SGLang","url":"https://sgl-project.github.io/"},{"title":"Welcome to SGLang - SGLang Documentation","url":"https://docs.sglang.io/"},{"title":"GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub","url":"https://github.com/sgl-project/sglang"},{"title":"sglang/docs/basic_usage/deepseek_v3.md at main · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/blob/main/docs/basic_usage/deepseek_v3.md"},{"title":"[Feature] Allow arbitrary logit processors · Issue #1036 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/1036"},{"title":"sglang · PyPI","url":"https://pypi.org/project/sglang/0.1.7/"},{"title":"A custom logits processor of type... If you just want to change the default values of logits processor consider passing them as arguments to `.generate()` instead of using a custom logits processor - Beginners - Hugging Face Forums","url":"https://discuss.huggingface.co/t/a-custom-logits-processor-of-type-if-you-just-want-to-change-the-default-values-of-logits-processor-consider-passing-them-as-arguments-to-generate-instead-of-using-a-custom-logits-processor/85241"},{"title":"RFC: Command-Line Interface Architecture for SGLang · Issue #9853 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/9853"}]

Based on the search results, I found relevant information about SGLang's CustomLogitProcessor. Here's what I discovered:

## CustomLogitProcessor in SGLang

SGLang's CustomLogitProcessor is a pragmatic extension point for a client-server LLM serving engine, with custom_params passthrough and request state access capabilities.

### Key Design Pattern

SamplingParams.custom_params: Dict[str, Any] flows from user request all the way into the processor's custom_param_list. This is a core pattern for passing custom parameters through the system.

### Implementation Details

CustomLogitProcessor uses dill to serialize the entire class and transmit it as a hex string over HTTP, with serialization for remote execution.

### Usage Example

In SGLang, CustomLogitProcessor can be implemented with thinking budget, and you can launch a server with --enable-custom-logit-processor flag on.

The search results show references to the architecture and patterns, particularly from an RFC discussion in February 2026 about SGLang-omni's extensible architecture. However, the results don't contain a complete working code example showing the `__call__` method implementation with `custom_param_list`. For a concrete code example, you may want to check the SGLang GitHub repository directly at `python/sglang/srt/sampling/custom_logit_processor.py` as referenced in the documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6ce04a6-a872-4380-8b5f-b9471baedea4",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "ad2e2006-5a92-4416-8ccc-f04a7abe2719",
  "sourceToolAssistantUUID": "f6ce04a6-a872-4380-8b5f-b9471baedea4",
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

_source line 23 · 2026-05-13T19:17:18.718Z_

<details><summary>↩ Tool result · `toolu_01P41gzcNmKB7uWyDxv4WB2M`</summary>

````text
Web search results for query: "SGLang --enable-custom-logit-processor usage example sampling params"

Links: [{"title":"Sampling Parameters — SGLang","url":"https://docs.sglang.io/basic_usage/sampling_params.html"},{"title":"Sampling Parameters - SGLang Documentation","url":"https://docs.sglang.io/docs/basic_usage/sampling_params"},{"title":"[Feature] Support a custom logit processor · Issue #2291 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/2291"},{"title":"Launch GLM-4.5 / GLM-4.6 / GLM-4.7 with SGLang — SGLang","url":"https://docs.sglang.io/basic_usage/glm45.html"},{"title":"SGLang Deep Dive: Inside SGLang - SugiV Blog","url":"https://blog.sugiv.fyi/sglang-deep-dive-inside-sglang"},{"title":"[Feature] Allow arbitrary logit processors · Issue #1036 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/1036"},{"title":"SGLang Documentation — SGLang","url":"https://sgl-project.github.io/"},{"title":"sglang/docs/advanced_features/server_arguments.md at main · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/blob/main/docs/advanced_features/server_arguments.md"},{"title":"[RFC] Extensible Tokenizer and Logits Processor Architecture · Issue #94 · sgl-project/sglang-omni","url":"https://github.com/sgl-project/sglang-omni/issues/94"},{"title":"docs/basic_usage/sampling_params.md · dbb16bedd54ffc2d7d2a2eac8d8064711f0c7286 · change / sglang","url":"https://developer.sourcefind.cn/codes/change/sglang/-/blob/dbb16bedd54ffc2d7d2a2eac8d8064711f0c7286/docs/basic_usage/sampling_params.md"}]

Based on the search results, I found comprehensive information about SGLang's custom logit processor feature and how to use it with sampling parameters.

## Custom Logit Processor Usage with Sampling Parameters

SGLang provides a `CustomLogitProcessor` class that can be subclassed to create custom logit processors. Here's a basic example showing a `DeterministicLogitProcessor` that modifies logits to always sample a given token id:

```python
from sglang.srt.sampling.custom_logit_processor import CustomLogitProcessor

class DeterministicLogitProcessor(CustomLogitProcessor):
    """A dummy logit processor that changes the logits to always sample the given token id."""
    
    def __call__(self, logits, custom_param_list):
        # Check that the number of logits matches the number of custom parameters
        assert logits.shape[0] == len(custom_param_list)
        key = "token_id"
        for i, param_dict in enumerate(custom_param_list):
            # Mask all other tokens
            logits[i, :] = -float("inf")
            # Assign highest probability to the specified token
            logits[i, param_dict[key]] = 0.0
        return logits
```

### Integration with Sampling Parameters

To use a custom logit processor with the `/generate` endpoint, include both the `custom_logit_processor` and `custom_params` in your request along with standard sampling parameters like `temperature` and `max_new_tokens`:

```python
import requests

response = requests.post(
    "http://localhost:30000/generate",
    json={
        "text": "The capital of France is",
        "custom_logit_processor": DeterministicLogitProcessor().to_str(),
        "sampling_params": {
            "temperature": 0.0,
            "max_new_tokens": 32,
            "custom_params": {"token_id": 5},
        },
    },
)
print(response.json())
```

### OpenAI-Compatible API

You can also use custom logit processors with the OpenAI-compatible API by passing the processor and custom parameters in the `extra_body` parameter:

```python
import openai

client = openai.Client(base_url="http://127.0.0.1:30000/v1", api_key="[REDACTED]")
response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[{"role": "user", "content": "List 3 countries and their capitals."}],
    temperature=0.0,
    max_tokens=32,
    extra_body={
        "custom_logit_processor": DeterministicLogitProcessor().to_str(),
        "custom_params": {"token_id": 5},
    },
)
```


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "355ccf47-a164-472c-9f8b-3aedf3b8f784",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "1c9c49fd-c297-44c9-8196-ca5abc0f99d8",
  "sourceToolAssistantUUID": "355ccf47-a164-472c-9f8b-3aedf3b8f784",
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

_source line 24 · 2026-05-13T19:17:20.391Z_

<details><summary>↩ Tool result · `toolu_01HBxDSd6E81EurQkyXtavSE`</summary>

```text
Web search results for query: "SGLang XGrammar JSON schema constrained decoding API usage json_schema regex"

Links: [{"title":"Guided Decoding Performance on vLLM and SGLang - The official SqueezeBits Tech blog","url":"https://blog.squeezebits.com/guided-decoding-performance-vllm-sglang"},{"title":"MLC | XGrammar-2: Fast and Customizable Structured Generation for Tool Calling and Agents","url":"https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"GitHub - guidance-ai/llguidance: Super-fast Structured Outputs · GitHub","url":"https://github.com/guidance-ai/llguidance"},{"title":"Structured Outputs - SGLang Documentation","url":"https://docs.sglang.ai/advanced_features/structured_outputs.html"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"MLC | Achieving Efficient, Flexible, and Portable Structured Generation with XGrammar","url":"https://blog.mlc.ai/2024/11/22/achieving-efficient-flexible-portable-structured-generation-with-xgrammar"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Run SGLang: Fast LLM Inference with Structured Generation 2026 | Markaicode","url":"https://markaicode.com/sglang-fast-llm-inference-structured-generation/"},{"title":"Fast JSON Decoding for Local LLMs with Compressed Finite State Machine - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2024-02-05-compressed-fsm/"}]

Based on the search results, here's comprehensive information about SGLang, XGrammar, JSON schema constrained decoding, and related API usage:

## Structured Outputs in SGLang

SGLang allows you to specify a JSON schema, regular expression or EBNF to constrain the model output, with the model output guaranteed to follow the given constraints. If no backend is specified, XGrammar will be used as the default.

## XGrammar Overview

XGrammar is an open-source library for efficient, flexible, and portable structured generation that leverages constrained decoding to ensure 100% structural correctness of the output and supports general context-free grammar to enable a broad range of structures, including JSON, regex, custom context-free grammar, etc.

SGLang, vLLM, TensorRT-LLM, and MLC-LLM integrate XGrammar for strict tool calling and expose customization through API.

## JSON Schema and Regex Constraints

regex_constraint compiles to a finite automaton and is faster for small, fixed-shape outputs (dates, IDs), while json_schema builds a full context-free grammar via xgrammar and handles nested objects, arrays, and optional fields.

## XGrammar Structural Tags

JSON Schema, regex, literal strings, and token IDs are all first-class atomic types within the language, and by nesting and combining them, you can describe arbitrarily complex output structures, from a simple JSON response to a multi-part reasoning-plus-tool-call format.

## Performance and Integration

XGrammar is the default structured generation backend for vLLM, SGLang, and TensorRT-LLM as of March 2026, achieving under 40 microseconds per token with near-zero overhead in JSON generation.

The search results also show that SGLang supports XGrammar's latest structural tag format for complex response formats, allowing you to define triggered tags with JSON schema constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "151bcab7-787a-43fc-80c6-8ffe4dadd396",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "907da2e3-93ff-4c41-aa35-d70a2f7af13c",
  "sourceToolAssistantUUID": "151bcab7-787a-43fc-80c6-8ffe4dadd396",
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

_source line 25 · 2026-05-13T19:17:22.981Z_

Let me get a few more details on key points.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "907da2e3-93ff-4c41-aa35-d70a2f7af13c",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb175mo5hfzDYS6aTZHsb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00002e50-390d-4156-84fa-b8d8199e4910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgtGXEsGGptEM2eKC4myRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9348,
      "cache_read_input_tokens": 14763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9348,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 26 · 2026-05-13T19:17:23.493Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VGFmVAu7dSrcBNGk8CRJeh`</summary>

```json
{
  "query": "SGLang structured outputs json_schema response_format example python code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00002e50-390d-4156-84fa-b8d8199e4910",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb175mo5hfzDYS6aTZHsb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee312dca-c055-4d72-af61-461727824eae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgtGXEsGGptEM2eKC4myRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9348,
      "cache_read_input_tokens": 14763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9348,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 27 · 2026-05-13T19:17:25.008Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RweAXFsLUzQzvrFijypzu7`</summary>

```json
{
  "query": "SGLang RTX PRO 6000 Blackwell FP8 issues known bugs sm_120 compute capability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee312dca-c055-4d72-af61-461727824eae",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb175mo5hfzDYS6aTZHsb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b2f3a30-3c45-4c5e-a370-2bf953087119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgtGXEsGGptEM2eKC4myRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9348,
      "cache_read_input_tokens": 14763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9348,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 28 · 2026-05-13T19:17:25.446Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CcwiGrgcMhQxJxZg6pNAXy`</summary>

```json
{
  "query": "SGLang version 0.4 0.5 Qwen3-8B supported models list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b2f3a30-3c45-4c5e-a370-2bf953087119",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb175mo5hfzDYS6aTZHsb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "681205ea-accd-4c80-8c3e-430b0c91b961",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgtGXEsGGptEM2eKC4myRz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9348,
      "cache_read_input_tokens": 14763,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9348
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 14763,
          "cache_creation_input_tokens": 9348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9348,
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

_source line 29 · 2026-05-13T19:17:30.903Z_

<details><summary>↩ Tool result · `toolu_01VGFmVAu7dSrcBNGk8CRJeh`</summary>

````text
Web search results for query: "SGLang structured outputs json_schema response_format example python code"

Links: [{"title":"Structured Outputs — SGLang","url":"https://docs.sglang.io/advanced_features/structured_outputs.html"},{"title":"Structured Outputs For Reasoning Models — SGLang","url":"https://docs.sglang.io/advanced_features/structured_outputs_for_reasoning_models.html"},{"title":"Structured Outputs - SGLang Documentation","url":"https://docs.sglang.ai/advanced_features/structured_outputs.html"},{"title":"sgl-project.github.io/advanced_features/structured_outputs.ipynb at main · sgl-project/sgl-project.github.io","url":"https://github.com/sgl-project/sgl-project.github.io/blob/main/advanced_features/structured_outputs.ipynb?plain=1"},{"title":"Structured Output - Inspect AI","url":"https://inspect.aisi.org.uk/structured.html"},{"title":"Sampling Parameters — SGLang","url":"https://docs.sglang.io/basic_usage/sampling_params.html"},{"title":"Structured Outputs | sgl-project/sgl-project.github.io | DeepWiki","url":"https://deepwiki.com/sgl-project/sgl-project.github.io/4.1-structured-outputs"},{"title":"A Guide to Structured Outputs Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"[Bug] gpt-oss reasoning parser not working with Structured Outputs · Issue #9259 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/9259"},{"title":"How to add structure to your LLM Applications using SGLang","url":"https://read.theaimerge.com/p/how-to-add-structure-to-your-llm"}]

Based on the search results, here's information about SGLang structured outputs with JSON schema and response_format in Python:

## Overview

SGLang allows you to specify a JSON schema to constrain the model output, and the model output will be guaranteed to follow the given constraints.

## Using JSON Schema with OpenAI-Compatible API

The OpenAI-compatible API allows you to specify JSON Schema constraints using the response_format parameter with type: "json_schema".

### Example with Chat Completions

Here's a practical Python example using the OpenAI-compatible client:

```python
import openai
from pydantic import BaseModel, Field

client = openai.Client(base_url="http://127.0.0.1:30000/v1", api_key="[REDACTED]")

# Define schema using Pydantic
class CapitalInfo(BaseModel):
    name: str = Field(..., description="Name of the capital city")
    population: int = Field(..., description="Population of the capital city")

messages = [
    {"role": "user", "content": "Give me the information of the capital of France in JSON format."}
]

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=messages,
    response_format={
        "type": "json_schema",
        "json_schema": CapitalInfo.model_json_schema()
    }
)
```

### Example with Native HTTP API

You can also use requests with JSON schema by specifying the json_schema in sampling_params.

```python
import json
import requests

json_schema = json.dumps({
    "type": "object",
    "properties": {
        "name": {"type": "string", "pattern": "^[\\w]+$"},
        "population": {"type": "integer"},
    },
    "required": ["name", "population"],
})

response = requests.post(
    "http://localhost:30000/generate",
    json={
        "text": "Here is the information of the capital of France in the JSON format.\n",
        "sampling_params": {
            "temperature": 0,
            "max_new_tokens": 64,
            "json_schema": json_schema,
        },
    },
)

print(response.json())
```

## Grammar Backends

SGLang supports XGrammar (default) which supports JSON schema constraints, Outlines which supports JSON schema constraints, and XGrammar is suggested for its better performance and utility.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee312dca-c055-4d72-af61-461727824eae",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "02e3557e-aaaa-40c1-a833-7751c72dd2a4",
  "sourceToolAssistantUUID": "ee312dca-c055-4d72-af61-461727824eae",
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

_source line 30 · 2026-05-13T19:17:31.501Z_

<details><summary>↩ Tool result · `toolu_01CcwiGrgcMhQxJxZg6pNAXy`</summary>

```text
Web search results for query: "SGLang version 0.4 0.5 Qwen3-8B supported models list"

Links: [{"title":"SGLang - Qwen","url":"https://qwen.readthedocs.io/en/latest/deployment/sglang.html"},{"title":"Supported Models | SGLang","url":"https://www.sglang.io/models"},{"title":"Releases · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/releases"},{"title":"Qwen3.6 - SGLang Documentation","url":"https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.6"},{"title":"SGLang Cookbook - Production Deployment Guides","url":"https://cookbook.sglang.io/autoregressive/Qwen/Qwen3.6"},{"title":"GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub","url":"https://github.com/sgl-project/sglang"},{"title":"Qwen3.5 | SGLang Cookbook","url":"https://cookbook.sglang.io/autoregressive/Qwen/Qwen3.5"},{"title":"Qwen 3.5 Usage — SGLang","url":"https://docs.sglang.io/basic_usage/qwen3_5.html"},{"title":"SGLang Documentation — SGLang","url":"https://sgl-project.github.io/"},{"title":"GitHub - Oxen-AI/sglang-qwen3.5: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub","url":"https://github.com/Oxen-AI/sglang-qwen3.5"}]

Based on my search results, I found information about SGLang's support for Qwen models, though the results don't provide a specific list for versions 0.4 and 0.5 together with Qwen3-8B support.

Here's what I found:

**Recent SGLang Support for Qwen Models:**

SGLang's latest releases include day-0 support for models like Qwen3.6, with mentions of new model support including Qwen-related variants.

**Qwen3-8B with SGLang:**

The search results show that SGLang can serve models like Qwen/Qwen3-8B by specifying the model path directly. However, the specific version support requirements differ: SGLang >=0.5.10 is required for Qwen3.6, which is a newer model.

**Broader Model Support:**

SGLang supports a wide range of language models including Qwen, along with embedding models and diffusion models.

The search results don't contain a detailed compatibility matrix specifically comparing SGLang versions 0.4 and 0.5 with Qwen3-8B support. For a comprehensive supported models list for those specific versions, I'd recommend checking the official SGLang GitHub releases page or documentation directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "681205ea-accd-4c80-8c3e-430b0c91b961",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "d2141bfa-c306-4d39-838d-3e8eb0799b93",
  "sourceToolAssistantUUID": "681205ea-accd-4c80-8c3e-430b0c91b961",
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

_source line 31 · 2026-05-13T19:17:33.122Z_

<details><summary>↩ Tool result · `toolu_01RweAXFsLUzQzvrFijypzu7`</summary>

```text
Web search results for query: "SGLang RTX PRO 6000 Blackwell FP8 issues known bugs sm_120 compute capability"

Links: [{"title":"[Bug] RTX6000 pro (Blackwell) with FP8 · Issue #16816 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/16816"},{"title":"EP=8 on RTX PRO 6000 Blackwell Server Edition (SM120): garbage output with FP8 and INT4 models · Issue #21132 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/21132"},{"title":"SGL on RTX 6000 Pro Blackwell · sgl-project/sglang · Discussion #12923","url":"https://github.com/sgl-project/sglang/discussions/12923"},{"title":"[Bug] RTX PRO 6000 Blackwell Cuda 13 · Issue #13342 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/13342"},{"title":"[Benchmark] MiniMax-M2.5 FP8 on 8× RTX PRO 6000 (SM120): bench_serving results + tuned fused_moe_triton config · Issue #18870 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/18870"},{"title":"[Benchmark] Nemotron 3 Super 120B-FP8 on 8x RTX PRO 6000 (SM120): 3,215 tok/s burst, 150ms TTFT, 17.9M token KV capacity · Issue #20541 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/20541"},{"title":"[Benchmark] Qwen3.5-122B-A10B FP8 weights / bf16 KV on 8x RTX PRO 6000 (SM120): 1,985 tok/s burst, MTP 2.75x, fp8 KV silent corruption finding · Issue #19603 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/19603"},{"title":"[Feature] RTX 6000 Pro tuned profiles · Issue #14488 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/14488"},{"title":"[Bug] --fp4-gemm-backend flashinfer_cutlass does not disable DeepGemm on Blackwell · Issue #20775 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/20775"},{"title":"[Feature] Add support for block FP8 on SM120 (NVIDIA 5090 and RTX PRO 6000?) · Issue #9233 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/9233"}]

Based on the search results, I found several known issues and bugs related to SGLang with RTX PRO 6000 Blackwell GPUs and FP8 support:

## Key Issues Found:

### FP8 Configuration Problems
Missing config files for FP8 W8A8 block quantization on RTX PRO 6000 Blackwell result in warnings like "Config file not found" and "Performance might be sub-optimal!"

### Compute Capability SM_120 (12.0) Specific Issues
Multiple users reported garbage output with FP8 and INT4 models on RTX PRO 6000 Blackwell Server Edition (SM120)

Triton was the only working FP8 GEMM/MoE backend on SM120 in SGLang 0.5.8.post1, while DeepGemm and CUTLASS both crash

### Backend Compatibility
There is no way to disable DeepGemm via CLI flags when serving NVFP4 checkpoints on Blackwell, which leads to CUDA crashes at concurrency ≥ 64 when the checkpoint's scale format is not ue8m0

### Silent Data Corruption
FP8 KV cache produced corrupt output silently in some setups with no crash or explicit error, just wrong answers, only detectable by checking output quality

### Workaround Required
FP8 models on RTX PRO 6000 SM120 require specific flags: --fp8-gemm-backend triton --moe-runner-backend triton, and some models need additional flags like --attention-backend triton --kv-cache-dtype bf16


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b2f3a30-3c45-4c5e-a370-2bf953087119",
  "isSidechain": true,
  "promptId": "9fb02546-5877-426e-8b09-6c9146827d80",
  "agentId": "ae97f643a35d5a194",
  "type": "user",
  "uuid": "0f8920ff-a963-4f4f-9f6e-bfa67ccfd553",
  "sourceToolAssistantUUID": "1b2f3a30-3c45-4c5e-a370-2bf953087119",
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

_source line 32 · 2026-05-13T19:18:26.157Z_

Here are the consolidated findings:

---

## 1. SGLang Qwen3 Support

**Qwen3-8B is supported.** SGLang supports the full Qwen3 family (Qwen3-8B, Qwen3-14B, etc.) as well as newer Qwen3.5 and Qwen3.6 models.

- Qwen3 (original): supported since SGLang ~0.4.x
- Qwen3.5 (Feb 2026): requires SGLang >= 0.5.x
- Qwen3.6 (Apr 2026): requires SGLang >= 0.5.10

Launch command:
```bash
python -m sglang.launch_server --model-path Qwen/Qwen3-8B --port 30000
```

With reasoning parser:
```bash
python -m sglang.launch_server --model-path Qwen/Qwen3-8B --reasoning-parser qwen3
```

---

## 2. Custom LogitsProcessor API

SGLang supports custom logit processors via the `--enable-custom-logit-processor` server flag. The processor is serialized with `dill` and sent as a hex string over HTTP.

**API signature:**

```python
from sglang.srt.sampling.custom_logit_processor import CustomLogitProcessor

class MyProcessor(CustomLogitProcessor):
    def __call__(self, logits: torch.Tensor, custom_param_list: list[dict]) -> torch.Tensor:
        """
        Args:
            logits: shape [batch, vocab_size] - the raw logits from the model
            custom_param_list: list of per-request param dicts (len == batch size)
        Returns:
            modified logits tensor, same shape
        """
        assert logits.shape[0] == len(custom_param_list)
        for i, params in enumerate(custom_param_list):
            # Modify logits[i, :] based on params
            ...
        return logits
```

**Full working example** -- force a specific token:
```python
class DeterministicLogitProcessor(CustomLogitProcessor):
    def __call__(self, logits, custom_param_list):
        assert logits.shape[0] == len(custom_param_list)
        for i, param_dict in enumerate(custom_param_list):
            logits[i, :] = -float("inf")
            logits[i, param_dict["token_id"]] = 0.0
        return logits
```

**Client-side usage (native API):**
```python
import requests
response = requests.post("http://localhost:30000/generate", json={
    "text": "The capital of France is",
    "custom_logit_processor": DeterministicLogitProcessor().to_str(),  # dill-serialized
    "sampling_params": {
        "temperature": 0.0,
        "max_new_tokens": 32,
        "custom_params": {"token_id": 5},  # flows into custom_param_list
    },
})
```

**Client-side usage (OpenAI-compatible API):**
```python
import openai
client = openai.Client(base_url="http://127.0.0.1:30000/v1", api_key="[REDACTED]")
response = client.chat.completions.create(
    model="Qwen/Qwen3-8B",
    messages=[{"role": "user", "content": "List 3 countries."}],
    extra_body={
        "custom_logit_processor": MyProcessor().to_str(),
        "custom_params": {"my_key": "my_value"},
    },
)
```

**Key facts:**
- Yes, you can intercept logits at the token level -- the `__call__` is invoked at every decoding step
- `custom_params` dict flows from the user request all the way into the processor
- The processor receives `logits[batch, vocab]` and can modify any token's logit for any request in the batch
- Serialization uses `dill`, so the processor class must be self-contained (no external closure references)

---

## 3. Built-in Constrained Decoding (XGrammar)

SGLang uses **XGrammar** as its default structured generation backend. It supports:
- **JSON Schema** constraints
- **Regex** constraints  
- **EBNF** (context-free grammar)

Performance: under 40 microseconds per token overhead. SGLang overlaps mask generation with LLM inference to hide latency.

**JSON Schema example (OpenAI API):**
```python
from pydantic import BaseModel

class CapitalInfo(BaseModel):
    name: str
    population: int

response = client.chat.completions.create(
    model="Qwen/Qwen3-8B",
    messages=[{"role": "user", "content": "Capital of France in JSON."}],
    response_format={
        "type": "json_schema",
        "json_schema": {"schema": CapitalInfo.model_json_schema()}
    }
)
```

**JSON Schema example (native API):**
```python
import json, requests
response = requests.post("http://localhost:30000/generate", json={
    "text": "Capital of France in JSON:\n",
    "sampling_params": {
        "temperature": 0,
        "max_new_tokens": 64,
        "json_schema": json.dumps({
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "population": {"type": "integer"},
            },
            "required": ["name", "population"],
        }),
    },
})
```

**Regex example (native API):**
```python
response = requests.post("http://localhost:30000/generate", json={
    "text": "The date is ",
    "sampling_params": {
        "regex": r"\d{4}-\d{2}-\d{2}",
    },
})
```

Alternative backends: `--grammar-backend outlines` or `--grammar-backend llguidance` (PR #3298).

---

## 4. LogitsProcessor vs. Constrained Decoding -- Key Distinction

These are **two separate mechanisms**:

| Feature | CustomLogitProcessor | XGrammar constrained decoding |
|---|---|---|
| Invocation | `--enable-custom-logit-processor` | Built-in (default) |
| Control | Arbitrary Python logic on logits tensor | Grammar-based token masking |
| Params | `json_schema`, `regex`, `ebnf` in sampling_params | `custom_logit_processor` + `custom_params` |
| Overhead | Python loop per step | ~40us/token (C++ compiled) |
| Use case | Custom scoring, schema-semantic constraints | Structural format enforcement |

For a schema-semantic constrained IE project, you could combine both: XGrammar enforces structural validity (valid JSON), while a CustomLogitProcessor applies semantic constraints (boosting/suppressing specific entity types or values based on schema semantics).

---

## 5. CUDA 12.8 / Blackwell RTX PRO 6000 Compatibility

**Status: Functional but with caveats.**

- RTX PRO 6000 Blackwell = compute capability SM_120 (sm_120)
- Successful deployments reported with CUDA 12.8 and CUDA 13.0, PyTorch 2.9.1+cu128, SGLang 0.5.7+
- NVIDIA provides official SGLang container releases (25.11, 26.02, 26.03) with Blackwell support

**Known issues on SM_120:**

1. **FP8 problems**: FP8 and INT4 models produce garbage output unless specific backends are forced:
   ```bash
   --fp8-gemm-backend triton --moe-runner-backend triton
   ```
   Some models also need `--attention-backend triton --kv-cache-dtype bf16`

2. **Silent FP8 KV cache corruption**: FP8 KV cache can produce wrong answers with no error/crash -- only detectable by checking output quality

3. **DeepGemm crashes**: DeepGemm and CUTLASS backends crash on SM_120; only Triton works reliably for FP8

4. **BF16 works fine**: Standard BF16 inference (no quantization) works without issues on Blackwell

**Recommended install for Blackwell:**
```bash
pip install sglang[all] --find-links https://docs.sglang.io/whl/cu128/
# Or use NVIDIA NGC container: nvcr.io/nvidia/sglang:26.03
```

**For Qwen3-8B on RTX PRO 6000, BF16 is the safe choice.** Avoid FP8 quantization unless you verify output quality and use the Triton backend workarounds.

---

Sources:
- [SGLang - Qwen Deployment Guide](https://qwen.readthedocs.io/en/latest/deployment/sglang.html)
- [SGLang Sampling Parameters](https://docs.sglang.io/basic_usage/sampling_params.html)
- [SGLang Custom LogitProcessor Issue #2291](https://github.com/sgl-project/sglang/issues/2291)
- [SGLang Arbitrary Logit Processors Issue #1036](https://github.com/sgl-project/sglang/issues/1036)
- [SGLang Structured Outputs Docs](https://docs.sglang.io/advanced_features/structured_outputs.html)
- [XGrammar GitHub](https://github.com/mlc-ai/xgrammar)
- [XGrammar-2 Blog Post](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation)
- [Constrained Decoding DeepWiki](https://deepwiki.com/sgl-project/sgl-learning-materials/3.3-constrained-decoding)
- [SGLang RTX PRO 6000 Blackwell Discussion #12923](https://github.com/sgl-project/sglang/discussions/12923)
- [RTX PRO 6000 FP8 Bug #16816](https://github.com/sgl-project/sglang/issues/16816)
- [SM120 Garbage Output Bug #21132](https://github.com/sgl-project/sglang/issues/21132)
- [SGLang Release 26.03 NVIDIA Docs](https://docs.nvidia.com/deeplearning/frameworks/sglang-release-notes/rel-26-03.html)
- [Qwen3.5 SGLang Usage](https://docs.sglang.io/basic_usage/qwen3_5.html)
- [SGLang Logit Bias Issue #6749](https://github.com/sgl-project/sglang/issues/6749)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f8920ff-a963-4f4f-9f6e-bfa67ccfd553",
  "isSidechain": true,
  "agentId": "ae97f643a35d5a194",
  "requestId": "req_011Cb176iEJTDdjCY6pNzGZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec99e83b-8de9-4472-b77f-0ba9a704edf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "819451c5-2d4d-4dc4-9270-745d780ee883",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BLzZvDpGTfge99go48RzH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 795,
      "cache_creation_input_tokens": 2549,
      "cache_read_input_tokens": 24111,
      "output_tokens": 2729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2549
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 795,
          "output_tokens": 2729,
          "cache_read_input_tokens": 24111,
          "cache_creation_input_tokens": 2549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2549,
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
