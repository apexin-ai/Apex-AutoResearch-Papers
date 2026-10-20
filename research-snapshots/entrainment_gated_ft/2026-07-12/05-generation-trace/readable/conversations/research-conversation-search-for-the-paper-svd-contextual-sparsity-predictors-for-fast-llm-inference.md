# Research conversation: Search for the paper "SVD Contextual Sparsity Predictors for Fast LLM Inference" (arXiv 2603.14110, March 2026). Verify:

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a9d21ee8a60f2959b.jsonl`
- **Structured JSON:** [`5b3e0a0baf929f077650.json`](../../sessions/5b/5b3e0a0baf929f077650.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-12T03:50:11.066Z_

Search for the paper "SVD Contextual Sparsity Predictors for Fast LLM Inference" (arXiv 2603.14110, March 2026). Verify:

1. Does it exist? Is it from March 2026?
2. Does it find that learned predictors suffer from out-of-distribution sensitivity?
3. Does it use truncated SVD of gate projections?
4. Does it target ReGLU-based models specifically?
5. What models does it evaluate on?

Try:
- "SVD contextual sparsity predictors arXiv 2603.14110"
- "site:arxiv.org 2603.14110"

Report findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "agentId": "a9d21ee8a60f2959b",
  "type": "user",
  "uuid": "a079443f-cf31-4517-a16c-a096ce6fcecb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T03:50:11.070Z_

```json
{
  "parentUuid": "a079443f-cf31-4517-a16c-a096ce6fcecb",
  "isSidechain": true,
  "agentId": "a9d21ee8a60f2959b",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f333a13d-fc01-49b7-9e98-05f5fdc0b25e",
  "timestamp": "2026-05-12T03:50:11.070Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T03:50:13.390Z_



I'll search for this paper using multiple strategies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f333a13d-fc01-49b7-9e98-05f5fdc0b25e",
  "isSidechain": true,
  "agentId": "a9d21ee8a60f2959b",
  "requestId": "req_011CawzaBTpmwH4ez19wcWgw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42078e18-7e9a-4883-bea4-649a1b5427d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01534D1Qs7AQMc1VBcvqkR8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 711,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 711,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T03:50:14.004Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RW8NRJ9EBRoNFHWmA5UEj3`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42078e18-7e9a-4883-bea4-649a1b5427d6",
  "isSidechain": true,
  "agentId": "a9d21ee8a60f2959b",
  "requestId": "req_011CawzaBTpmwH4ez19wcWgw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "844eee47-82df-4f01-b7d5-be1f178bae2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01534D1Qs7AQMc1VBcvqkR8n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 711,
      "cache_read_input_tokens": 8223,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 711
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 711,
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

_source line 5 · 2026-05-12T03:50:14.007Z_

<details><summary>↩ Tool result · `toolu_01RW8NRJ9EBRoNFHWmA5UEj3`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "844eee47-82df-4f01-b7d5-be1f178bae2a",
  "isSidechain": true,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "agentId": "a9d21ee8a60f2959b",
  "type": "user",
  "uuid": "66623d5c-d680-4523-b394-3f1ed4639a0c",
  "sourceToolAssistantUUID": "844eee47-82df-4f01-b7d5-be1f178bae2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T03:50:16.803Z_



Now let me run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66623d5c-d680-4523-b394-3f1ed4639a0c",
  "isSidechain": true,
  "agentId": "a9d21ee8a60f2959b",
  "requestId": "req_011CawzaQkY1FpewFsScMzPc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31562f1c-1915-4c12-8c95-641bc0c24450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYnxNS118ZyYTY9RpT4jCS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1900,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T03:50:17.240Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JWmfTPSqrUXcnhKYaC4cyZ`</summary>

```json
{
  "query": "SVD contextual sparsity predictors arXiv 2603.14110"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31562f1c-1915-4c12-8c95-641bc0c24450",
  "isSidechain": true,
  "agentId": "a9d21ee8a60f2959b",
  "requestId": "req_011CawzaQkY1FpewFsScMzPc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a47a5e84-d858-48de-a65b-4c07df7be186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYnxNS118ZyYTY9RpT4jCS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1900,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-12T03:50:17.866Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F3xrjiEJaxs1LXRiYaeTgN`</summary>

```json
{
  "query": "site:arxiv.org 2603.14110"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a47a5e84-d858-48de-a65b-4c07df7be186",
  "isSidechain": true,
  "agentId": "a9d21ee8a60f2959b",
  "requestId": "req_011CawzaQkY1FpewFsScMzPc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "235f9e6c-de0e-4045-900a-998e37b305c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYnxNS118ZyYTY9RpT4jCS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8934,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 184,
          "cache_read_input_tokens": 8934,
          "cache_creation_input_tokens": 1900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1900,
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

_source line 9 · 2026-05-12T03:50:17.885Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VKeauqZTQYm62qTuFRb9c1`</summary>

```json
{
  "query": "\"SVD Contextual Sparsity Predictors for Fast LLM Inference\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "235f9e6c-de0e-4045-900a-998e37b305c2",
  "isSidechain": true,
  "agentId": "a9d21ee8a60f2959b",
  "requestId": "req_011CawzaQkY1FpewFsScMzPc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ca81c1f-c4aa-42d7-839d-97a755125bc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYnxNS118ZyYTY9RpT4jCS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8934,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 184,
          "cache_read_input_tokens": 8934,
          "cache_creation_input_tokens": 1900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1900,
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

_source line 10 · 2026-05-12T03:50:23.367Z_

<details><summary>↩ Tool result · `toolu_01F3xrjiEJaxs1LXRiYaeTgN`</summary>

```text
Web search results for query: "site:arxiv.org 2603.14110"

Links: [{"title":"[2603.14110] SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/abs/2603.14110"},{"title":"[2604.14110] Non-Gaussian fluctuations in relativistic hydrodynamics: Confluent equations for three-point correlations","url":"https://arxiv.org/abs/2604.14110"},{"title":"Value Sensitive Design for Fair Online Recruitment: A Conceptual Framework Informed by Job Seekers’ Fairness Concerns","url":"https://arxiv.org/html/2501.14110"},{"title":"[2601.14110] Adsorption-Driven Symmetry Lowering in Single Molecules Revealed by Ångstrom-scale Tip-Enhanced Raman Imaging","url":"https://arxiv.org/abs/2601.14110"},{"title":"Non-Gaussian fluctuations in relativistic hydrodynamics: Confluent equations for three-point correlations","url":"https://arxiv.org/html/2604.14110"},{"title":"[2501.14110] Value Sensitive Design for Fair Online Recruitment: A Conceptual Framework Informed by Job Seekers' Fairness Concerns","url":"https://arxiv.org/abs/2501.14110"},{"title":"[2509.14110] Local existence theory for a class of CMC gauges for the Einstein-non-linear scalar field equations","url":"https://arxiv.org/abs/2509.14110"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2203.14110.pdf"},{"title":"[2508.14110] Mott transition from the non-analyticity of the one-body reduced density-matrix functional","url":"https://arxiv.org/abs/2508.14110"},{"title":"DROID: Dual Representation for Out-of-Scope Intent Detection","url":"https://arxiv.org/html/2510.14110"}]

Based on the search results, I found the paper you're looking for:

**The paper "SVD Contextual Sparsity Predictors for Fast LLM Inference" (arXiv:2603.14110) presents a framework for accelerating inference of ReGLU-based feed-forward networks (FFNs) within LLMs using a training-free method for building sparse pattern predictors based on truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm.**

The experiments on three sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores.

The paper was submitted on March 14, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "235f9e6c-de0e-4045-900a-998e37b305c2",
  "isSidechain": true,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "agentId": "a9d21ee8a60f2959b",
  "type": "user",
  "uuid": "c6a886d8-e807-4ae3-8702-f899dc4ccf8f",
  "sourceToolAssistantUUID": "235f9e6c-de0e-4045-900a-998e37b305c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T03:50:24.204Z_

<details><summary>↩ Tool result · `toolu_01VKeauqZTQYm62qTuFRb9c1`</summary>

```text
Web search results for query: ""SVD Contextual Sparsity Predictors for Fast LLM Inference" 2026"

Links: [{"title":"[2603.14110] SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/abs/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/html/2603.14110"},{"title":"GitHub - z-lab/sparselora: [ICML 2025] SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://github.com/z-lab/sparselora"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity - Z Lab","url":"https://z-lab.ai/projects/sparselora/"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/html/2506.16500v1"},{"title":"Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/pdf/2506.16500"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time | OpenReview","url":"https://openreview.net/forum?id=wIPIhHd00i"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://openreview.net/pdf?id=z83rodY0Pw"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/html/2406.16635v2"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"}]

I found the research paper you're looking for. Here are the key details:

## SVD Contextual Sparsity Predictors for Fast LLM Inference

This is an arXiv paper (2603.14110) from March 14, 2026.

### Overview
Contextual sparsity is one of the approaches used to reduce computational complexity in the inference process of large language models (LLMs). Existing techniques for efficient LLM inference acceleration based on contextual sparsity with minimal accuracy degradation require training sparse pattern predictors.

### Main Contribution
The paper presents a framework for accelerating inference of ReGLU-based feed-forward networks (FFNs) within LLMs. The proposed framework provides a fast, training-free method for building sparse pattern predictors using truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm, and inference executors supporting conditional computation on CUDA and CANN devices.

### Results
Experiments on three sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on tasks involving complex math.

You can access the full paper at: https://arxiv.org/abs/2603.14110


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ca81c1f-c4aa-42d7-839d-97a755125bc7",
  "isSidechain": true,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "agentId": "a9d21ee8a60f2959b",
  "type": "user",
  "uuid": "33061c8e-53ec-415a-8a5a-746b6689787a",
  "sourceToolAssistantUUID": "6ca81c1f-c4aa-42d7-839d-97a755125bc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T03:50:26.310Z_

<details><summary>↩ Tool result · `toolu_01JWmfTPSqrUXcnhKYaC4cyZ`</summary>

```text
Web search results for query: "SVD contextual sparsity predictors arXiv 2603.14110"

Links: [{"title":"[2603.14110] SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/abs/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/html/2603.14110"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/html/2506.16500.pdf"},{"title":"Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/pdf/2506.16500"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/html/2406.16635v2"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"},{"title":"1 Introduction","url":"https://arxiv.org/html/2502.12444v1"},{"title":"Catchup results for stat from Sat, 21 Jan 2023","url":"https://arxiv.org/catchup?smonth=1&sday=21&group=grp_&archive=stat&num=2000&order=reverse&method=without&syear=2023"},{"title":"TurboESM: Ultra-Efficient 3-Bit KV Cache Quantization for ...","url":"https://arxiv.org/pdf/2603.26110"},{"title":"Sparse autoencoders reveal organized biological knowledge but minimal regulatory logic in single-cell foundation models: a comparative atlas of Geneformer and scGPT","url":"https://arxiv.org/html/2603.02952v1"}]

I found the paper you're looking for. Here's what I found about arXiv 2603.14110:

## SVD Contextual Sparsity Predictors for Fast LLM Inference

This paper presents a framework for accelerating inference of ReGLU-based feed-forward networks (FFNs) within LLMs. The proposed framework provides a fast, training-free method for building sparse pattern predictors using truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm, and inference executors supporting conditional computation on CUDA and CANN devices.

**Key Details:**
- **Authors:** Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, and C.C. Korikov
- **Date:** March 14, 2026
- **Topic:** Contextual sparsity is one of the approaches used to reduce computational complexity in the inference process of large language models (LLMs).

**Results:** Experiments on three sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on tasks involving complex math.

The paper is available at https://arxiv.org/abs/2603.14110 and https://arxiv.org/html/2603.14110.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a47a5e84-d858-48de-a65b-4c07df7be186",
  "isSidechain": true,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "agentId": "a9d21ee8a60f2959b",
  "type": "user",
  "uuid": "34269a59-c177-4d95-ad6f-c6e943aa87fc",
  "sourceToolAssistantUUID": "a47a5e84-d858-48de-a65b-4c07df7be186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-12T03:50:30.267Z_

The paper is confirmed to exist. Let me now fetch the full paper to answer the detailed questions about out-of-distribution sensitivity, specific models evaluated, and the other claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34269a59-c177-4d95-ad6f-c6e943aa87fc",
  "isSidechain": true,
  "agentId": "a9d21ee8a60f2959b",
  "requestId": "req_011CawzbJbE5MaxKFVSqpjTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90ecfb5b-c874-4601-9c1f-24f679ca118a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMNiMjEQzB1WpYQ2Ck8azR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1618,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 10834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1072,
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

_source line 14 · 2026-05-12T03:50:32.169Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TtHoSvajtKY3wnxxq8vc9m`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.14110",
  "prompt": "Extract the full abstract, list of authors, submission date, and any details about: (1) out-of-distribution sensitivity of learned predictors, (2) use of truncated SVD of gate projections, (3) whether it targets ReGLU-based models specifically, (4) what specific models are evaluated in experiments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90ecfb5b-c874-4601-9c1f-24f679ca118a",
  "isSidechain": true,
  "agentId": "a9d21ee8a60f2959b",
  "requestId": "req_011CawzbJbE5MaxKFVSqpjTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b4c5b6b-f44f-4c57-9b58-3e65f9a3cea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMNiMjEQzB1WpYQ2Ck8azR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1618,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 10834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1072,
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

_source line 15 · 2026-05-12T03:50:34.511Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015GKWt4tWwjdczgnKThxfcr`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.14110",
  "prompt": "Extract detailed information about: (1) Does the paper find that learned predictors suffer from out-of-distribution sensitivity? What exactly does it say about this? (2) Does it use truncated SVD of gate projections? (3) Does it target ReGLU-based models specifically? (4) What specific models (e.g., Llama, Mistral, etc.) does it evaluate on? (5) What are the main results and speedups reported? Please include relevant quotes where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b4c5b6b-f44f-4c57-9b58-3e65f9a3cea9",
  "isSidechain": true,
  "agentId": "a9d21ee8a60f2959b",
  "requestId": "req_011CawzbJbE5MaxKFVSqpjTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b40254c-dcb2-4526-b22d-965dcaa3a6e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMNiMjEQzB1WpYQ2Ck8azR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1618,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 10834,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1072
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1618,
          "output_tokens": 362,
          "cache_read_input_tokens": 10834,
          "cache_creation_input_tokens": 1072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1072,
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

_source line 16 · 2026-05-12T03:50:38.524Z_

<details><summary>↩ Tool result · `toolu_01TtHoSvajtKY3wnxxq8vc9m`</summary>

```text
# Paper Summary: SVD Contextual Sparsity Predictors for Fast LLM Inference

**Full Abstract:**
"Contextual sparsity is one of the approaches used to reduce computational complexity in the inference process of large language models (LLMs). Existing techniques for efficient LLM inference acceleration based on contextual sparsity with minimal accuracy degradation require training sparse pattern predictors. This paper presents a framework for accelerating inference of ReGLU-based feed-forward networks (FFNs) within LLMs. The proposed framework provides a fast, training-free method for building sparse pattern predictors using truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm, and inference executors supporting conditional computation on CUDA and CANN devices. Experiments on three sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on tasks involving complex math and code generation. This work advances the deployment of LLMs on edge devices."

**Authors:**
Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, C.C. Korikov

**Submission Date:**
March 14, 2026

---

## Key Details:

**(1) Out-of-Distribution Sensitivity:**
Not discussed in the provided content.

**(2) Truncated SVD of Gate Projections:**
Yes—the method employs "truncation-aware singular value decomposition (SVD) of the gate projection matrix" as a core technique for building sparse pattern predictors without requiring training.

**(3) ReGLU-Based Models:**
Yes, specifically confirmed: the framework targets "ReGLU-based feed-forward networks (FFNs) within LLMs."

**(4) Specific Models Evaluated:**
The abstract mentions "three sparse LLMs" but does not name them explicitly in the available content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b4c5b6b-f44f-4c57-9b58-3e65f9a3cea9",
  "isSidechain": true,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "agentId": "a9d21ee8a60f2959b",
  "type": "user",
  "uuid": "97166938-0ed0-4306-acba-b419997356d2",
  "sourceToolAssistantUUID": "5b4c5b6b-f44f-4c57-9b58-3e65f9a3cea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T03:50:40.727Z_

<details><summary>↩ Tool result · `toolu_015GKWt4tWwjdczgnKThxfcr`</summary>

```text
# SVD Contextual Sparsity Predictors: Key Findings

## (1) Out-of-Distribution Sensitivity in Learned Predictors

Yes, the paper explicitly identifies this issue. In the ROC-AUC analysis section, it states:

> "Trained predictors may suffer from out-of-distribution sensitivity due to their data-dependent nature, while SVD predictors directly leverage the LLM's internal weight structure."

This observation supports their argument that training-free SVD approaches offer advantages over learned predictors like Deja Vu and PowerInfer.

## (2) Truncated SVD of Gate Projections

Yes, the approach is fundamentally built on this technique. The paper describes their method as using "low-rank singular value decomposition (SVD) of the gate projection matrix" with data-aware truncation to create lightweight predictors for contextual sparsity estimation.

## (3) ReGLU-Based Models

Confirmed. The work specifically targets ReGLU-activated FFNs. The paper notes that "A key characteristic of ReGLU-based LLMs is dynamic (or contextual) sparsity," and their method leverages this property where "computations for the remaining neurons can be safely skipped" due to ReLU's behavior.

## (4) Evaluated Models

The paper evaluates on three 7B-parameter sparse models:
- **ProSparse-LLaMA2-7B**
- **SparseQwen2-7B** (instruction-tuned)
- **TurboSparse-Mistral-Instruct** (instruction-tuned)

## (5) Main Results and Speedups

The key achievement: "up to 1.8× end-to-end decoding acceleration with minimal accuracy degradation" while maintaining "less than 1% degradation in benchmark scores on tasks involving complex math and code generation."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b40254c-dcb2-4526-b22d-965dcaa3a6e8",
  "isSidechain": true,
  "promptId": "6b75caff-9e8f-4914-a49c-e6cefa1414d7",
  "agentId": "a9d21ee8a60f2959b",
  "type": "user",
  "uuid": "c6322654-25df-4afc-8b13-8b667b6b6693",
  "sourceToolAssistantUUID": "1b40254c-dcb2-4526-b22d-965dcaa3a6e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-12T03:50:50.405Z_

Here are the findings for each of your questions:

---

**1. Does the paper exist? Is it from March 2026?**

Yes, confirmed. The paper "SVD Contextual Sparsity Predictors for Fast LLM Inference" exists at arXiv:2603.14110. It was submitted on **March 14, 2026**. Authors: Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, and C.C. Korikov.

**2. Does it find that learned predictors suffer from out-of-distribution sensitivity?**

Yes. The paper explicitly states: *"Trained predictors may suffer from out-of-distribution sensitivity due to their data-dependent nature, while SVD predictors directly leverage the LLM's internal weight structure."* This is a key motivation for their training-free SVD-based approach over learned predictors like Deja Vu and PowerInfer.

**3. Does it use truncated SVD of gate projections?**

Yes. The core method uses "truncation-aware singular value decomposition (SVD) of the gate projection matrix" to build lightweight, training-free sparse pattern predictors. This is the central technical contribution of the paper.

**4. Does it target ReGLU-based models specifically?**

Yes. The paper explicitly targets ReGLU-activated feed-forward networks (FFNs) within LLMs. It notes that "a key characteristic of ReGLU-based LLMs is dynamic (or contextual) sparsity," leveraging the fact that ReLU gating zeroes out neurons whose computations can be safely skipped.

**5. What models does it evaluate on?**

Three 7B-parameter sparse models:
- **ProSparse-LLaMA2-7B**
- **SparseQwen2-7B** (instruction-tuned)
- **TurboSparse-Mistral-Instruct** (instruction-tuned)

The experiments demonstrate up to **1.8x end-to-end decoding speedup** at ~90% FFN activation sparsity, with less than 1% degradation on benchmarks involving complex math and code generation. The framework supports inference on both CUDA and CANN devices.

---

Sources:
- [arXiv abstract page: 2603.14110](https://arxiv.org/abs/2603.14110)
- [arXiv HTML full paper: 2603.14110](https://arxiv.org/html/2603.14110)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6322654-25df-4afc-8b13-8b667b6b6693",
  "isSidechain": true,
  "agentId": "a9d21ee8a60f2959b",
  "requestId": "req_011CawzcNMUK54t8CCi3mUBE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7194e508-818d-4ae2-8fe4-b4f34441da91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bdf522a6-a8a8-46bb-9a44-de1ead278b20",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkrighB5vuFYiiWYDzkeX5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 11906,
      "output_tokens": 600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 600,
          "cache_read_input_tokens": 11906,
          "cache_creation_input_tokens": 2942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2942,
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
