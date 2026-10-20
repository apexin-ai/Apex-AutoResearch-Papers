# Research conversation: I'm reviewing a paper idea called "SpectralWatch" that proposes monitoring spectral dynamics of attention-graph Laplacia

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a91a20d33dc5ad48e.jsonl`
- **Structured JSON:** [`821bc29de5b0dacc251e.json`](../../sessions/82/821bc29de5b0dacc251e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-15T13:30:07.760Z_

I'm reviewing a paper idea called "SpectralWatch" that proposes monitoring spectral dynamics of attention-graph Laplacian eigenvalues during autoregressive LLM generation to predict hallucination onset 3-5 tokens before emission. I need to find competing or concurrent work that the authors may have missed.

Do the following WebSearch queries and report what you find for each:

1. Search: "online hallucination detection LLM decoding time 2025 2026"
2. Search: "attention spectral analysis hallucination prediction real-time"
3. Search: "incremental eigenvalue attention hallucination"
4. Search: "predictive hallucination detection before generation LLM"
5. Search: "early warning hallucination LLM token-level 2026"
6. Search: "spectral attention dynamics language model 2026"
7. Search: "proactive hallucination intervention decoding LLM"
8. Search: "attention graph topology hallucination online monitoring"
9. Search: "token-level hallucination prediction internal representations 2025 2026"
10. Search: "look-ahead hallucination detection LLM generation"

For each search, report the top 3-5 most relevant results, especially any papers that are close to the SpectralWatch idea (i.e., they do online/predictive hallucination detection using attention or spectral features during generation). I need to know if someone has already done something very similar.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "1ae53bb1-5db3-4eab-a70b-5a355d686501",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T13:30:07.764Z_

```json
{
  "parentUuid": "1ae53bb1-5db3-4eab-a70b-5a355d686501",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
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
  "uuid": "5443b856-45bf-48c7-bf73-13e22348d07a",
  "timestamp": "2026-05-15T13:30:07.764Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T13:30:10.520Z_



I'll load the WebSearch tool first, then run all 10 searches. Let me start by fetching the tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5443b856-45bf-48c7-bf73-13e22348d07a",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SDwbPa5wgLwGi5dLyW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b4cfef4-e750-4e27-b491-bf80e5182c0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Higrkowfi9mdKyqw3VFvy4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 887,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 4 · 2026-05-15T13:30:10.879Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SoZdCknickGouLKxF1GG2B`</summary>

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
  "parentUuid": "1b4cfef4-e750-4e27-b491-bf80e5182c0c",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SDwbPa5wgLwGi5dLyW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "684bc099-08c7-4b5f-b985-ef9b1a2b8e01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Higrkowfi9mdKyqw3VFvy4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 8223,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 887,
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

_source line 5 · 2026-05-15T13:30:10.882Z_

<details><summary>↩ Tool result · `toolu_01SoZdCknickGouLKxF1GG2B`</summary>

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
  "parentUuid": "684bc099-08c7-4b5f-b985-ef9b1a2b8e01",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "9c11fa0e-05cd-4f53-a7f5-9c3da829658f",
  "sourceToolAssistantUUID": "684bc099-08c7-4b5f-b985-ef9b1a2b8e01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T13:30:13.575Z_



Now let me run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c11fa0e-05cd-4f53-a7f5-9c3da829658f",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SEBLsuXGwYV8DJ6hTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe547ed3-bfc8-4334-bf54-85296adfece6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg9KsAKNM8Udrr7AQqQxad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 7 · 2026-05-15T13:30:14.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EzCS7RmajeTeDgXv7fT3AJ`</summary>

```json
{
  "query": "online hallucination detection LLM decoding time 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe547ed3-bfc8-4334-bf54-85296adfece6",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SEBLsuXGwYV8DJ6hTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f85e9e4-4644-4f9e-9959-a17738be9047",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg9KsAKNM8Udrr7AQqQxad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 8 · 2026-05-15T13:30:14.547Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VJ2Zp8SgrdBmgRoewPb4yr`</summary>

```json
{
  "query": "attention spectral analysis hallucination prediction real-time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f85e9e4-4644-4f9e-9959-a17738be9047",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SEBLsuXGwYV8DJ6hTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfd66867-da0e-4290-9235-3dabe184bdf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg9KsAKNM8Udrr7AQqQxad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 9 · 2026-05-15T13:30:14.568Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EtC2Ee96m2Ah5pbCfuokcL`</summary>

```json
{
  "query": "incremental eigenvalue attention hallucination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfd66867-da0e-4290-9235-3dabe184bdf6",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SEBLsuXGwYV8DJ6hTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43f693de-60ae-49eb-a666-8938a5c65c9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg9KsAKNM8Udrr7AQqQxad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 10 · 2026-05-15T13:30:15.006Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011wzALVGY2UxYBRxcbwpAtP`</summary>

```json
{
  "query": "predictive hallucination detection before generation LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43f693de-60ae-49eb-a666-8938a5c65c9d",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SEBLsuXGwYV8DJ6hTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d0e6912-bc04-4d3f-b0b8-0485daae0fa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg9KsAKNM8Udrr7AQqQxad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 11 · 2026-05-15T13:30:15.181Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bx4KZ5fwGBsJ7ishDegiaY`</summary>

```json
{
  "query": "early warning hallucination LLM token-level 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d0e6912-bc04-4d3f-b0b8-0485daae0fa1",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SEBLsuXGwYV8DJ6hTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de884b49-23e7-4ca2-8969-1b8ff4bb181e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg9KsAKNM8Udrr7AQqQxad",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9110,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 9110,
          "cache_creation_input_tokens": 1421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1421,
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

_source line 12 · 2026-05-15T13:30:22.456Z_

<details><summary>↩ Tool result · `toolu_01EtC2Ee96m2Ah5pbCfuokcL`</summary>

```text
Web search results for query: "incremental eigenvalue attention hallucination"

Links: [{"title":"[2502.17598] Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/abs/2502.17598"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1239/"},{"title":"LLM-Check: Investigating Detection of Hallucinations in Large Language Models","url":"https://par.nsf.gov/servlets/purl/10574407"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v2"},{"title":"Hallucination Detection in LLMs Using Spectral Features of ...","url":"https://aclanthology.org/2025.emnlp-main.1239.pdf"},{"title":"[Literature Review] Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://www.themoonlight.io/en/review/hallucination-detection-in-llms-using-spectral-features-of-attention-maps"},{"title":"llms' internal states retain the power of hallucination detection","url":"https://arxiv.org/pdf/2402.03744"},{"title":"EigenTrack: Temporal Spectral Analysis of Hidden Activations for Hallucination and OOD Detection","url":"https://arxiv.org/html/2509.15735v4"},{"title":"[2509.15735] EigenTrack: Spectral Activation Feature Tracking for Hallucination and Out-of-Distribution Detection in LLMs and VLMs","url":"https://arxiv.org/abs/2509.15735"},{"title":"GitHub - graphml-lab-pwr/lapeigvals: Implementation of the paper \"Hallucination Detection in LLMs Using Spectral Features of Attention Maps\" · GitHub","url":"https://github.com/graphml-lab-pwr/lapeigvals"}]

Based on the search results, here's what I found about incremental eigenvalue attention hallucination:

## Overview

The search results primarily reveal research on using eigenvalue-based spectral analysis of attention maps for detecting hallucinations in Large Language Models (LLMs). There are several key approaches in this area:

### LapEigvals Method

The LapEigvals method utilises the top-k eigenvalues of the Laplacian matrix derived from the attention maps as an input to hallucination detection probes. This approach interprets attention maps as adjacency matrices of graph structures.

### EigenTrack: Incremental Approach

A more recent method directly relevant to "incremental" eigenvalue analysis is EigenTrack, a real-time detector that models the temporal evolution of multi-layer spectral features to identify hallucination and OOD behavior. This appears to be the incremental/temporal variant, as it extracts covariance spectrum statistics including leading eigenvalues, spectral gaps, entropy, and Random Matrix Theory features based on divergence from the Marchenko-Pastur law.

### Performance

On LLaMa-7B, EigenTrack reaches 0.89 AUROC for hallucination and 0.92 for OOD, outperforming baselines such as HaloScope, LapEigvals, and SelfCheckGPT while using only a lightweight recurrent head.

These methods leverage the insight that spectral features (eigenvalues) encapsulate significant structural properties regarding the information flow within the neural network, potentially revealing the presence of hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43f693de-60ae-49eb-a666-8938a5c65c9d",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "3753f53d-3077-49c1-ade8-72b7f5883b27",
  "sourceToolAssistantUUID": "43f693de-60ae-49eb-a666-8938a5c65c9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T13:30:22.682Z_

<details><summary>↩ Tool result · `toolu_01VJ2Zp8SgrdBmgRoewPb4yr`</summary>

```text
Web search results for query: "attention spectral analysis hallucination prediction real-time"

Links: [{"title":"[2502.17598] Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/abs/2502.17598"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v2"},{"title":"Hallucination Detection in LLMs Using Spectral Features of ...","url":"https://aclanthology.org/2025.emnlp-main.1239.pdf"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1239/"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://openreview.net/pdf?id=YYYiHkFKJs"},{"title":"[Literature Review] Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://www.themoonlight.io/en/review/hallucination-detection-in-llms-using-spectral-features-of-attention-maps"},{"title":"EigenTrack: Temporal Spectral Analysis of Hidden Activations for Hallucination and OOD Detection","url":"https://arxiv.org/html/2509.15735v4"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps | Request PDF","url":"https://www.researchgate.net/publication/397421008_Hallucination_Detection_in_LLMs_Using_Spectral_Features_of_Attention_Maps"},{"title":"GitHub - graphml-lab-pwr/lapeigvals: Implementation of the paper \"Hallucination Detection in LLMs Using Spectral Features of Attention Maps\" · GitHub","url":"https://github.com/graphml-lab-pwr/lapeigvals"},{"title":"Detecting Contextual Hallucinations in Large Language Models with Frequency-Aware Attention","url":"https://arxiv.org/html/2602.18145"}]

Based on the web search results, I found several relevant research papers and methods related to attention spectral analysis for hallucination prediction. Here are the key findings:

## Main Research Approaches

**LapEigvals Method - Hallucination Detection via Attention Spectral Features:**

Researchers investigate spectral features of attention maps by interpreting them as adjacency matrices of graph structures, proposing the LapEigvals method which utilizes the top-k eigenvalues of the Laplacian matrix derived from attention maps as input to hallucination detection probes. Empirical evaluations demonstrate that this approach achieves state-of-the-art hallucination detection performance among attention-based methods.

**EigenTrack - Real-Time Hallucination Detection:**

EigenTrack is an interpretable real-time detector that characterizes model dynamics through the spectral geometry of hidden activations. It constructs sliding-window activation matrices, extracts covariance spectrum statistics including leading eigenvalues, spectral gaps, entropy, and Random Matrix Theory features based on divergence from the Marchenko-Pastur law, and streams these signals into a lightweight recurrent classifier to model temporal evolution. Unlike black-box and grey-box methods that require multiple generations or log-probability access, EigenTrack operates with a single forward pass and no resampling.

**Frequency-Aware Attention Analysis:**

A frequency-aware attention modeling framework extracts high-frequency attention signals using spectral operators, improving hallucination detection at both token and span levels, with findings suggesting that hallucinations are reflected not only in where attention is placed, but also in how it varies across tokens over time.

These research directions demonstrate that spectral analysis of attention patterns and hidden activations provides effective signals for detecting hallucinations in real-time scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfd66867-da0e-4290-9235-3dabe184bdf6",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "7f38352d-ce66-420b-aaf6-3b01632371a6",
  "sourceToolAssistantUUID": "bfd66867-da0e-4290-9235-3dabe184bdf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T13:30:23.263Z_

<details><summary>↩ Tool result · `toolu_01Bx4KZ5fwGBsJ7ishDegiaY`</summary>

```text
Web search results for query: "early warning hallucination LLM token-level 2026"

Links: [{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"LLM Hallucination Statistics 2026: AI Gets Facts Wrong Up to 82% of the Time","url":"https://sqmagazine.co.uk/llm-hallucination-statistics/"},{"title":"Eliminating LLM Hallucinations: A Multi-Layer Defense Strategy That Actually Works | by Dr. Murali Nandigama | Apr, 2026 | Medium","url":"https://medium.com/@murali.nandigama/eliminating-llm-hallucinations-a-multi-layer-defense-strategy-that-actually-works-1702febb9e4d"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"LLM Hallucination Rates 2026: Best and Worst Models | AI Blog API for Developers","url":"https://modelslab.com/blog/llm/llm-hallucination-rates-2026"},{"title":"Detecting Hallucinations in LLM Responses Using Token-Level Log-Probability Signals | OpenReview","url":"https://openreview.net/forum?id=1DJGWKtDmi"},{"title":"AI Hallucination Rates & Benchmarks in 2026","url":"https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"},{"title":"Token-Level Truth: Real-Time Hallucination Detection for Production LLMs | vLLM Blog","url":"https://blog.vllm.ai/2025/12/14/halugate.html"},{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"Prevent Hallucinations in LLM — Best Practices 2026","url":"https://www.anavcloudsanalytics.ai/blog/prevent-hallucinations-in-llm/"}]

Based on the search results, here's what I found about early warning hallucination detection at the token level in LLM systems as of 2026:

## Token-Level Early Warning Detection

Research addresses early detection of hallucinating answers based on user input, the LLM answer, and token-level probability signals that can be extracted during inference time. Researchers have constructed datasets combining textual information with sequences of token log-probabilities and their statistics (mean, min, variance, percentiles, etc.), and trained lightweight classifiers that output the probability that a given response is a hallucination.

## Advanced Token-Level Approaches

One system monitors token-by-token generation uncertainty against a predetermined threshold and injects "think tokens" — additional computation prompts — whenever generated tokens exhibit uncertainty exceeding expected bounds, operating during streaming rather than post-hoc.

Another key development is a gradient-based paradigm for hallucination detection that introduces a statistic called Next-token Gradient Sensitivity (NGS), which quantifies the first-order gradient of the maximum log-probability of the next token with respect to the current token's layer embedding, measuring local prediction fragility.

HaluGate is a conditional, token-level hallucination detection pipeline that catches unsupported claims before they reach users, providing binary labels (0=Supported, 1=Hallucinated) for each answer token.

## Practical Application

These detection systems return a probability-of-hallucination value before the LLM generates any response — allowing a risk threshold to gate whether the query proceeds to the model or triggers human expert review.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de884b49-23e7-4ca2-8969-1b8ff4bb181e",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "cb7ca539-5b56-4057-b1a4-aa225fe4d8c3",
  "sourceToolAssistantUUID": "de884b49-23e7-4ca2-8969-1b8ff4bb181e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T13:30:23.449Z_

<details><summary>↩ Tool result · `toolu_01EzCS7RmajeTeDgXv7fT3AJ`</summary>

```text
Web search results for query: "online hallucination detection LLM decoding time 2025 2026"

Links: [{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"Token-Level Truth: Real-Time Hallucination Detection for Production LLMs | vLLM Blog","url":"https://blog.vllm.ai/2025/12/14/halugate.html"},{"title":"LLM Hallucination Statistics 2026: AI Gets Facts Wrong Up to 82% of the Time","url":"https://sqmagazine.co.uk/llm-hallucination-statistics/"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"Internal Representations as Indicators of Hallucinations in Agent Tool Selection | OpenReview","url":"https://openreview.net/forum?id=QbuBZvwcDZ"},{"title":"Detecting LLM Hallucinations at Generation Time with UQLM | by Dylan Bouchard | CVS Health Tech Blog | Medium","url":"https://medium.com/cvs-health-tech-blog/detecting-llm-hallucinations-at-generation-time-with-uqlm-cd749d2338ec"},{"title":"How to Detect Hallucinations in Your LLM Applications","url":"https://www.getmaxim.ai/articles/how-to-detect-hallucinations-in-your-llm-applications/"},{"title":"Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments","url":"https://arxiv.org/html/2605.03971v1"}]

Based on the search results, here's what the latest research shows about online hallucination detection in LLMs with focus on decoding time in 2025-2026:

## Key Findings on Real-Time Detection

For a 4K token RAG context, detection takes approximately 125ms; for 16K tokens, roughly 365ms. The total overhead (76-162ms) is negligible compared to typical LLM generation times (5-30 seconds), making detection practical for synchronous request processing.

## Current Detection Approaches

Recent approaches include monitoring and detecting with internal probes when no external ground truth exists. Additionally, 2025 research like REACTSCORE integrates entropy with intermediate reasoning traces to detect failures in multi-step decision-making.

HaluGate—a token-level hallucination detection pipeline—catches unsupported claims before they reach users through fast, explainable verification at the point of delivery. A conditional two-stage pipeline approach reduces costs: in production workloads where approximately 35% of queries are non-factual, pre-classification achieves a 72.2% efficiency gain.

## Latency Challenges

Detection latency remains a challenge, with average delays of 200–500 ms per response.

## Efficiency Trade-offs

White-box scorers that use token probabilities from the original generated response add no additional cost and have negligible impact on latency, making them a strong, minimal-latency default.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f85e9e4-4644-4f9e-9959-a17738be9047",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "fd36d8e6-734a-4d26-bba9-753e00c84bcb",
  "sourceToolAssistantUUID": "1f85e9e4-4644-4f9e-9959-a17738be9047",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:30:24.791Z_

<details><summary>↩ Tool result · `toolu_011wzALVGY2UxYBRxcbwpAtP`</summary>

```text
Web search results for query: "predictive hallucination detection before generation LLM"

Links: [{"title":"Detecting hallucinations in large language models using semantic entropy | Nature","url":"https://www.nature.com/articles/s41586-024-07421-0"},{"title":"Detecting hallucinations with LLM-as-a-judge: Prompt engineering and beyond | Datadog","url":"https://www.datadoghq.com/blog/ai/llm-hallucination-detection/"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"LLM-Check: Investigating Detection of Hallucinations in Large Language Models","url":"https://openreview.net/pdf?id=LYx4w3CAgy"},{"title":"How to evaluate LLM hallucination rates in engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/how-to-evaluate-llm-hallucination-rates-in-engineering/"},{"title":"LLM Hallucinations: Detect and Quantify before you apply RAG | Google Cloud - Community","url":"https://medium.com/google-cloud/hallucinations-in-llms-can-you-even-measure-the-problem-932e23b1873b"},{"title":"Must-Attend AI LLM Hallucination Detection And Mitigation | Deepchecks","url":"https://deepchecks.com/llm-hallucination-detection-and-mitigation-best-techniques/"},{"title":"Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://arxiv.org/pdf/2504.07863"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"}]

Based on the web search results, here's what I found about predictive hallucination detection before generation in LLMs:

## Pre-Generation Hallucination Detection Approaches

Pre-generation hallucination probability estimation is a class of techniques that compute a risk score for a query before the LLM generates any response. Rather than detecting errors after output, these methods use query perturbation, multi-agent sampling, and statistical simulation to estimate the likelihood that a given input will elicit a hallucinated response.

### Key Methods

**Query Perturbation and Statistical Simulation**

JPMorgan Chase Bank's 2025 patent on hallucination probability prediction uses an approach where an incoming query is perturbed n times into lexically divergent but semantically equivalent variations; n+1 independent agents then sample outputs for each variant; and a statistical simulation algorithm is applied across those sampled outputs to determine the ground truth label for training.

**Input-Based Hidden State Classifiers**

One approach introduces a lightweight classifier that detects hallucinations preemptively conditioning only on the input hidden states, before any text is generated. When hallucinations are predicted, it intervenes in these hidden states to steer the model toward more factual outputs. Experiments show consistent improvements in factual accuracy across various LLMs, with minimal computational overhead.

**Intermediate Layer Probes**

Another technique trains a lightweight probe (3M–37M params) on intermediate hidden states instead of final-layer outputs, since middle layers retain uncertainty signals that the token-projection step throws away. Two modes are available: question-only (runs before or alongside generation, no added latency) and question+answer (waits for the full response, more accurate).

These pre-generation approaches enable threshold-based gating, allowing systems to prevent high-risk queries from proceeding to the LLM entirely.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d0e6912-bc04-4d3f-b0b8-0485daae0fa1",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "8ac29c0b-da30-48f3-93e7-f88b370ac91b",
  "sourceToolAssistantUUID": "3d0e6912-bc04-4d3f-b0b8-0485daae0fa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T13:30:27.392Z_

Good, I have results for the first 5 searches. Now let me run the remaining 5 searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ac29c0b-da30-48f3-93e7-f88b370ac91b",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SFCPuQDgRXLhNhkevn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1ddb911-bcf1-4921-b102-ee26d1b15b7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XvZmhqvAgmpX4gWxftXP9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1011,
      "cache_creation_input_tokens": 4171,
      "cache_read_input_tokens": 10531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4171,
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

_source line 18 · 2026-05-15T13:30:27.874Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014B1EDWSHDJxWg9XAbyRpUP`</summary>

```json
{
  "query": "spectral attention dynamics language model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1ddb911-bcf1-4921-b102-ee26d1b15b7b",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SFCPuQDgRXLhNhkevn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b3220e6-6493-47de-82eb-4e540b019230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XvZmhqvAgmpX4gWxftXP9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1011,
      "cache_creation_input_tokens": 4171,
      "cache_read_input_tokens": 10531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4171,
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

_source line 19 · 2026-05-15T13:30:28.341Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KTkAdoAykEeUpe65SYP5Ur`</summary>

```json
{
  "query": "proactive hallucination intervention decoding LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b3220e6-6493-47de-82eb-4e540b019230",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SFCPuQDgRXLhNhkevn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49f0e9b4-e478-43db-b891-b77730e911c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XvZmhqvAgmpX4gWxftXP9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1011,
      "cache_creation_input_tokens": 4171,
      "cache_read_input_tokens": 10531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4171,
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

_source line 20 · 2026-05-15T13:30:29.283Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01532oyA52TDLPfBEiFC2HDV`</summary>

```json
{
  "query": "attention graph topology hallucination online monitoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49f0e9b4-e478-43db-b891-b77730e911c5",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SFCPuQDgRXLhNhkevn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e986655-6c77-45d0-b5f8-6f8521e42dbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XvZmhqvAgmpX4gWxftXP9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1011,
      "cache_creation_input_tokens": 4171,
      "cache_read_input_tokens": 10531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4171,
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

_source line 21 · 2026-05-15T13:30:29.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NQCo1moxExPcNSD4Kb5XNK`</summary>

```json
{
  "query": "token-level hallucination prediction internal representations 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e986655-6c77-45d0-b5f8-6f8521e42dbf",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SFCPuQDgRXLhNhkevn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9cdc66d-d658-4ee6-9259-784e20da009b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XvZmhqvAgmpX4gWxftXP9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1011,
      "cache_creation_input_tokens": 4171,
      "cache_read_input_tokens": 10531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4171,
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

_source line 22 · 2026-05-15T13:30:29.939Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QoLf1XrCu8uciPDXLvnksj`</summary>

```json
{
  "query": "look-ahead hallucination detection LLM generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9cdc66d-d658-4ee6-9259-784e20da009b",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SFCPuQDgRXLhNhkevn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4550105e-1cc4-4480-aa79-c89e12a3a475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XvZmhqvAgmpX4gWxftXP9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1011,
      "cache_creation_input_tokens": 4171,
      "cache_read_input_tokens": 10531,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4171
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1011,
          "output_tokens": 266,
          "cache_read_input_tokens": 10531,
          "cache_creation_input_tokens": 4171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4171,
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

_source line 23 · 2026-05-15T13:30:35.205Z_

<details><summary>↩ Tool result · `toolu_014B1EDWSHDJxWg9XAbyRpUP`</summary>

```text
Web search results for query: "spectral attention dynamics language model 2026"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/82e3509393670d9d478c359b4ce6f950-Paper-Conference.pdf"},{"title":"[2507.19595] Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/abs/2507.19595"},{"title":"SPECTRAL ATTENTION STEERING FOR PROMPT HIGH","url":"https://openreview.net/pdf/61b1d6aa10b647458c65499b860d5a264e38c178.pdf"},{"title":"Towards Attention-Aware Large Language Models: Integrating Real-Time Eye-Tracking and EEG for Adaptive AI Responses","url":"https://arxiv.org/html/2511.06468v1"},{"title":"Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/pdf/2507.19595"},{"title":"Selective Attention: Enhancing Transformer through Principled Context Control","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf"},{"title":"The Mechanism of Attention in Large Language Models: A Comprehensive Guide - Magnimind Academy","url":"https://magnimindacademy.com/blog/the-mechanism-of-attention-in-large-language-models-a-comprehensive-guide/"},{"title":"Spectral Analysis of Attention Patterns","url":"https://www.emergentmind.com/topics/spectral-analysis-of-attention-patterns"},{"title":"Deep autoregressive models with spectral attention - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320322004940"},{"title":"Large Vision–Language Models Get Lost in Attention","url":"https://arxiv.org/html/2605.05668v1"}]

Based on the search results, here's what I found about spectral attention dynamics in language models from 2026 research:

## Key Findings on Spectral Attention Dynamics

Recent research examines the dynamics of language models through the lens of dynamical systems, with spectral analysis serving as the primary analytical tool to examine components including attention blocks and feed-forward blocks.

### DIFFEQFORMER Model
A notable approach proposes a model that generates all weights of attention and feed-forward blocks through hyper-neural networks, specifically considering weights as functions of a continuous layer index (or time). The observed spectral dynamics tend to exhibit increasing magnitudes of eigenvalues.

### Spectral Attention for Steering
A novel framework called Spectral Editing Key Amplification (SEKA) steers attention by directly modifying key vectors before attention scores are calculated, using spectral decomposition to learn a universal "relevance subspace" for a given task by applying spectral decomposition to key embeddings derived from contrastive prompts.

### Reliability and Diagnostics
Spectral properties of attention patterns are highly predictive of model reliability, factuality, and reasoning validity, with Laplacian eigenvalues of attention maps enabling logistic regression probes to achieve state-of-the-art hallucination detection.

These developments represent recent advances in understanding and applying spectral methods to analyze and improve attention mechanisms in language models through 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b3220e6-6493-47de-82eb-4e540b019230",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "637c561b-e1a6-4d0e-8b36-90339825f71e",
  "sourceToolAssistantUUID": "1b3220e6-6493-47de-82eb-4e540b019230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T13:30:35.915Z_

<details><summary>↩ Tool result · `toolu_01532oyA52TDLPfBEiFC2HDV`</summary>

```text
Web search results for query: "attention graph topology hallucination online monitoring"

Links: [{"title":"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063v3"},{"title":"[2504.10063] Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/abs/2504.10063"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=4twbqwV4br"},{"title":"Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063v1"},{"title":"[2509.24770] Neural Message-Passing on Attention Graphs for Hallucination Detection","url":"https://arxiv.org/abs/2509.24770"},{"title":"(PDF) Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://www.researchgate.net/publication/390772361_Hallucination_Detection_in_LLMs_via_Topological_Divergence_on_Attention_Graphs"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection","url":"https://arxiv.org/html/2509.24770v1"},{"title":"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://openreview.net/pdf?id=cJ0KbB0U7Q"},{"title":"[2601.03051] Temporal Graph Network: Hallucination Detection in Multi-Turn Conversation","url":"https://arxiv.org/abs/2601.03051"},{"title":"Spectral Guardrails for Agents in the Wild: Detecting Tool Use Hallucinations via Attention Topology","url":"https://arxiv.org/html/2602.08082"}]

Based on the search results, here's what I found about attention graph topology, hallucination detection, and online monitoring:

## Key Research Areas

**Hallucination Detection via Attention Graph Topology:**

TOHA is a topology-based hallucination detector in the RAG setting which leverages a topological divergence metric to quantify the structural properties of graphs induced by attention matrices. Examining the topological divergence between prompt and response subgraphs reveals consistent patterns: higher divergence values in specific attention heads correlate with hallucinated outputs, independent of the dataset.

**Graph-Based Approaches:**

By representing signals as attributed graphs where tokens are nodes and edges follow attentional flows, the CHARM approach casts hallucination detection as a graph learning task by applying GNNs over the attributed graphs.

**Online Monitoring and Real-time Detection:**

A complementary approach uses spectral analysis of attention topology by treating attention matrices as dynamic graphs and computing properties of their Laplacian spectrum to detect hallucinations without any learned parameters. On Llama 3.1 8B, this method achieves 97.7% recall with multi-feature detection and 86.1% recall with 81.0% precision for balanced deployment without requiring labeled training data, with single layer spectral features achieving near-perfect hallucination detection performance.

These methods represent recent advances in detecting hallucinations by analyzing the structural and spectral properties of attention mechanisms in language models, enabling both training-free and computationally efficient hallucination monitoring.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e986655-6c77-45d0-b5f8-6f8521e42dbf",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "ca6cf49a-0903-4c0f-ac7a-e2df82ec335e",
  "sourceToolAssistantUUID": "5e986655-6c77-45d0-b5f8-6f8521e42dbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T13:30:37.221Z_

<details><summary>↩ Tool result · `toolu_01KTkAdoAykEeUpe65SYP5Ur`</summary>

```text
Web search results for query: "proactive hallucination intervention decoding LLM"

Links: [{"title":"Constructing Benchmarks and Interventions for Combating Hallucinations in LLMs","url":"https://arxiv.org/pdf/2404.09971"},{"title":"Reducing hallucinations in large language models with custom intervention using Amazon Bedrock Agents | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/reducing-hallucinations-in-large-language-models-with-custom-intervention-using-amazon-bedrock-agents/"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models","url":"https://arxiv.org/html/2401.01313v1"},{"title":"Understanding and Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention | OpenReview","url":"https://openreview.net/forum?id=Bjq4W7P2Us"},{"title":"strategies for mitigating hallucinations","url":"https://www.vectara.com/blog/reducing-hallucinations-in-llms"},{"title":"Frontiers | Survey and analysis of hallucinations in large language models: attribution to prompting strategies or model behavior","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1622292/full"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions","url":"https://arxiv.org/html/2509.18970v1"},{"title":"From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs","url":"https://www.mdpi.com/2673-2688/6/10/260"}]

Based on the web search results, here's what I found about proactive hallucination intervention decoding for LLMs:

## Recent Research Approaches

PCNet is a tractable density estimator based on Probabilistic Circuits, paired with PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding), which together resolve the Detection-Correction Asymmetry in LLM hallucination mitigation. By framing hallucinations as geometric anomalies on the factual manifold and computing exact Negative Log-Likelihood in a single forward pass, PCNet achieves near-perfect detection across CoQA, SQuAD v2.0, and TriviaQA, with AUROC reaching up to 99%.

PC-LDCD only intervenes when the latent geometry deviates from factual regions, while leaving correct generations untouched. Crucially, using PCNet as a dynamic gate prevents indiscriminate corrections from corrupting factual generations, reducing the mean corruption rate to approximately 79.3%.

## Broader Intervention Strategies

Mitigation strategies can be broadly divided into two categories: prompt-based interventions and model-based architectural or training improvements. Decoding by Contrasting Layers (DoLa) is a simple decoding strategy designed to mitigate hallucinations in pre-trained LLMs without the need for external knowledge conditioning or additional fine-tuning.

For vision-language models, methods include training-free approaches applied directly during decoding and fine-tuning approaches, both targeted for hallucination heads to reduce their reliance on text tokens, achieving up to 1.7x reduction in hallucination rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49f0e9b4-e478-43db-b891-b77730e911c5",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "553b00d9-d9b1-4dc0-9718-01b464fa59ad",
  "sourceToolAssistantUUID": "49f0e9b4-e478-43db-b891-b77730e911c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T13:30:38.690Z_

<details><summary>↩ Tool result · `toolu_01QoLf1XrCu8uciPDXLvnksj`</summary>

```text
Web search results for query: "look-ahead hallucination detection LLM generation"

Links: [{"title":"Must-Attend AI LLM Hallucination Detection And Mitigation | Deepchecks","url":"https://deepchecks.com/llm-hallucination-detection-and-mitigation-best-techniques/"},{"title":"Detecting hallucinations with LLM-as-a-judge: Prompt engineering and beyond | Datadog","url":"https://www.datadoghq.com/blog/ai/llm-hallucination-detection/"},{"title":"Detecting hallucinations in large language models using semantic entropy | Nature","url":"https://www.nature.com/articles/s41586-024-07421-0"},{"title":"LLM Hallucinations Explained: Why They Happen, How to Detect Them, and the Risks Ahead","url":"https://www.allaboutai.com/resources/understanding-llm-hallucinations/"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"A hallucination detection and mitigation framework for faithful text summarization using LLMs | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-31075-1"},{"title":"Reducing hallucinations in large language models with custom intervention using Amazon Bedrock Agents | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/reducing-hallucinations-in-large-language-models-with-custom-intervention-using-amazon-bedrock-agents/"},{"title":"Detect hallucinations in your RAG LLM applications with Datadog LLM Observability | Datadog","url":"https://www.datadoghq.com/blog/llm-observability-hallucination-detection/"},{"title":"LLM-Check: Investigating Detection of Hallucinations in Large Language Models","url":"https://openreview.net/pdf?id=LYx4w3CAgy"}]

Based on the search results, here's what I found about look-ahead hallucination detection in LLM generation:

## Overview of Hallucination Detection Methods

Multiple techniques have been developed for detecting hallucinations in general, and unfaithful answers specifically. White-box and gray-box detection methods require visibility into the generating LLM.

## Key Detection Approaches

Token probability approaches estimate the confidence of the answer based on the final-layer logits, while sparse autoencoder and simpler attention-mapping approaches attempt to find specific combinations of neural activations that are correlated with hallucination.

Entropy-based uncertainty estimators for LLMs have been proposed to detect a subset of hallucinations—confabulations—which are arbitrary and incorrect generations.

## Advanced Detection Techniques

Factual retrieval produces stable eigen-structures, while hallucination leads to diffuse, chaotic patterns when analyzing attention mechanisms. Additionally, Cross-Layer Attention Probing (CLAP) trains lightweight classifiers on the model's own activations to flag likely hallucinations in real time. The MetaQA framework goes a step further by using metamorphic prompt mutations to detect hallucinations even in closed-source models without relying on token probabilities or external tools.

## Real-Time Detection in Production

Best-of-N style reranking can catch hallucinations after generation. An ACL Findings 2025 study showed that evaluating multiple candidate responses with a lightweight factuality metric and choosing the most faithful one significantly lowers error rates, without retraining the model.

These methods represent the state-of-the-art in detecting hallucinations during or immediately after LLM generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4550105e-1cc4-4480-aa79-c89e12a3a475",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "32474e89-519b-415d-8252-f3d4fc83938c",
  "sourceToolAssistantUUID": "4550105e-1cc4-4480-aa79-c89e12a3a475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T13:30:38.745Z_

<details><summary>↩ Tool result · `toolu_01NQCo1moxExPcNSD4Kb5XNK`</summary>

```text
Web search results for query: "token-level hallucination prediction internal representations 2025 2026"

Links: [{"title":"Token-Level Hallucination Detection","url":"https://www.emergentmind.com/topics/token-level-hallucination-detection"},{"title":"[2504.07863] Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://arxiv.org/abs/2504.07863"},{"title":"ICML Poster The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering","url":"https://icml.cc/virtual/2025/poster/46338"},{"title":"GitHub - mala-lab/HaMI: [NeurIPS 2025] Official implementation for ''Robust Hallucination Detection in LLMs via Adaptive Token Selection'' https://arxiv.org/abs/2504.07863 · GitHub","url":"https://github.com/mala-lab/HaMI"},{"title":"Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://arxiv.org/html/2504.07863v2"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering | OpenReview","url":"https://openreview.net/forum?id=7BKcLeHQsm"},{"title":"Token-Level Self-Consistency for Hallucination Detection","url":"https://aclanthology.org/2025.semeval-1.38.pdf"},{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"First Hallucination Tokens Are Different from Conditional Ones","url":"https://arxiv.org/html/2507.20836v4"},{"title":"Towards Token-Level Hallucination Control via Self- ...","url":"https://www.arxiv.org/pdf/2601.21969"}]

I've completed a web search for "token-level hallucination prediction internal representations 2025 2026". Here are the key findings:

## Recent Research on Token-Level Hallucination Detection

Recent work (2025-2026) shows significant advances in predicting hallucinations at the token level using internal representations:

**Hidden-State Probing Methods:**
Linear or neural probes are attached to internal representations (e.g., hidden states) to predict hallucination probability per token, with nonlinear MLP probes providing superior accuracy and recall due to better modeling of semantic nonlinearities.

**Adaptive Token Selection (HaMI):**
HaMI enables robust detection of hallucinations through adaptive selection and learning of critical tokens that are most indicative of hallucinations by formulating hallucination detection as Multiple Instance learning over token-level representations within a sequence.

**Vision-Language Model Research:**
Research investigating the internal dynamics of hallucination in vision-language models reveals patterns including gradual visual information loss and early excitation, where semantically meaningful tokens achieve peak activation in layers earlier than the final layer.

**Gradient-Based Detection:**
A gradient-based paradigm for hallucination detection probes next-token prediction sensitivity using a statistic called Next-token Gradient Sensitivity (NGS), which measures local prediction fragility, framing detection as a token-level distribution comparison task.

**Position-Aware Analysis:**
Research suggests that the first token carries a stronger hallucination signal and achieves higher detection accuracy than subsequent, conditionally generated tokens.

These methods leverage the finding that LLMs' internal representations contain truthfulness hints, which can be harnessed for detector training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9cdc66d-d658-4ee6-9259-784e20da009b",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "78bda4ad-d376-4cc7-9521-f28e87db2ff6",
  "sourceToolAssistantUUID": "c9cdc66d-d658-4ee6-9259-784e20da009b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T13:30:41.909Z_

Now let me do a few targeted follow-up searches on the most relevant papers I found, to get more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78bda4ad-d376-4cc7-9521-f28e87db2ff6",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SGE4eEhExNdz9VNWEw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a60e8e54-2c5d-4fcf-afe6-515d24233005",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012drNakXfBPbu4CvqJCyWRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 5050,
      "cache_read_input_tokens": 14702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5050,
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

_source line 29 · 2026-05-15T13:30:43.055Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GgPmWSCfBXCYueQcJ2jR82`</summary>

```json
{
  "query": "EigenTrack spectral activation feature tracking hallucination detection arxiv 2509.15735"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a60e8e54-2c5d-4fcf-afe6-515d24233005",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SGE4eEhExNdz9VNWEw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "284c6630-6f1d-438a-b36c-63d7b237653a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012drNakXfBPbu4CvqJCyWRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 5050,
      "cache_read_input_tokens": 14702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5050,
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

_source line 30 · 2026-05-15T13:30:44.046Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019VsWJZsZdC1QhkECVCgaRK`</summary>

```json
{
  "query": "\"Spectral Guardrails\" attention topology tool use hallucination arxiv 2602.08082"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "284c6630-6f1d-438a-b36c-63d7b237653a",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SGE4eEhExNdz9VNWEw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "480796f7-b507-43c3-b858-20f1adc3e412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012drNakXfBPbu4CvqJCyWRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 5050,
      "cache_read_input_tokens": 14702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5050,
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

_source line 31 · 2026-05-15T13:30:44.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012qNitNw8TQGaSaEiCsnH7C`</summary>

```json
{
  "query": "TOHA topological divergence attention hallucination detection arxiv 2504.10063"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "480796f7-b507-43c3-b858-20f1adc3e412",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SGE4eEhExNdz9VNWEw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40ed5489-e0cc-4059-8531-8747d65e1507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012drNakXfBPbu4CvqJCyWRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 5050,
      "cache_read_input_tokens": 14702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5050,
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

_source line 32 · 2026-05-15T13:30:45.534Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011bdcLTEv5HrHmdvUFRiweA`</summary>

```json
{
  "query": "HaluGate token-level hallucination detection vLLM production pipeline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40ed5489-e0cc-4059-8531-8747d65e1507",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SGE4eEhExNdz9VNWEw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45115f05-5645-4176-a6ee-c6eb846cae54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012drNakXfBPbu4CvqJCyWRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 5050,
      "cache_read_input_tokens": 14702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5050,
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

_source line 33 · 2026-05-15T13:30:45.908Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JRpD5GaVMU3PAEDgazjmFE`</summary>

```json
{
  "query": "\"frequency-aware attention\" hallucination detection spectral operators arxiv 2602.18145"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45115f05-5645-4176-a6ee-c6eb846cae54",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SGE4eEhExNdz9VNWEw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19dd3c47-8b26-4531-8eae-b8a80e76defa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012drNakXfBPbu4CvqJCyWRS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 5050,
      "cache_read_input_tokens": 14702,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5050
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1018,
          "output_tokens": 316,
          "cache_read_input_tokens": 14702,
          "cache_creation_input_tokens": 5050,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5050,
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

_source line 34 · 2026-05-15T13:30:51.468Z_

<details><summary>↩ Tool result · `toolu_012qNitNw8TQGaSaEiCsnH7C`</summary>

```text
Web search results for query: "TOHA topological divergence attention hallucination detection arxiv 2504.10063"

Links: [{"title":"[2504.10063] Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/abs/2504.10063"},{"title":"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063v3"},{"title":"Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063v1"},{"title":"(PDF) Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://www.researchgate.net/publication/390772361_Hallucination_Detection_in_LLMs_via_Topological_Divergence_on_Attention_Graphs"},{"title":"[Literature Review] Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://www.themoonlight.io/en/review/hallucination-detection-in-llms-via-topological-divergence-on-attention-graphs"},{"title":"arXiv:2504.10063v2 [cs.CL] 22 May 2025","url":"https://www.arxiv.org/pdf/2504.10063"},{"title":"Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2604.10697"},{"title":"Hallucination Detection in LLMs with Topological Divergence on ...","url":"https://www.semanticscholar.org/paper/1ec4be9cd511fc87e66e15233c16fa177c10aa86"},{"title":"(PDF) Attention Head Embeddings with Trainable Deep Kernels for Hallucination Detection in LLMs","url":"https://www.researchgate.net/publication/392598893_Attention_Head_Embeddings_with_Trainable_Deep_Kernels_for_Hallucination_Detection_in_LLMs"},{"title":"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://openreview.net/pdf?id=cJ0KbB0U7Q"}]

Based on the search results, I found detailed information about the paper arxiv 2504.10063:

## TOHA: Topological Divergence Attention Hallucination Detection

TOHA is a TOpology-based HAllucination detector in the RAG setting, which leverages a topological divergence metric to quantify the structural properties of graphs induced by attention matrices.

### Key Concept

Examining the topological divergence between prompt and response subgraphs reveals consistent patterns: higher divergence values in specific attention heads correlate with hallucinated outputs, independent of the dataset.

### Methodology

TOHA leverages topological data analysis (TDA) to quantify the structural properties of graphs derived from attention matrices, specifically focusing on the divergence between prompt and response subgraphs. The core approach involves treating attention matrices as weighted graphs where tokens are vertices and attention weights represent edges.

### Performance

Extensive experiments - including evaluation on question answering and summarization tasks - show that the approach achieves state-of-the-art or competitive results on several benchmarks while requiring minimal annotated data and computational resources.

### Key Finding

The existence of hallucination-aware attention heads is discovered: calculating topological divergences from just a few specific heads is enough for reliable hallucination detection, irrespective of the dataset.

The paper also includes the release of new annotated datasets to facilitate further research in hallucination detection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40ed5489-e0cc-4059-8531-8747d65e1507",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "496778f0-b6b4-47c6-8ceb-0a02b248e033",
  "sourceToolAssistantUUID": "40ed5489-e0cc-4059-8531-8747d65e1507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T13:30:51.678Z_

<details><summary>↩ Tool result · `toolu_019VsWJZsZdC1QhkECVCgaRK`</summary>

```text
Web search results for query: ""Spectral Guardrails" attention topology tool use hallucination arxiv 2602.08082"

Links: [{"title":"[2602.08082] Spectral Guardrails for Agents in the Wild: Detecting Tool Use Hallucinations via Attention Topology","url":"https://arxiv.org/abs/2602.08082"},{"title":"Spectral Guardrails for Agents in the Wild: Detecting Tool Use Hallucinations via Attention Topology","url":"https://arxiv.org/html/2602.08082"},{"title":"Spectral Guardrails for Agents in the Wild: Detecting Tool ...","url":"https://arxiv.org/pdf/2602.08082"},{"title":"HalluGuard: LLM Hallucination Mitigation","url":"https://www.emergentmind.com/topics/halluguard-framework"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v2"},{"title":"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063v2"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps | Request PDF","url":"https://www.researchgate.net/publication/397421008_Hallucination_Detection_in_LLMs_Using_Spectral_Features_of_Attention_Maps"},{"title":"[2502.17598] Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/abs/2502.17598"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250217598B/abstract"},{"title":"Grounding the Ungrounded: A Spectral-Graph Framework for Quantifying Hallucinations in multimodal LLMs","url":"https://arxiv.org/html/2508.19366v1"}]

I found the paper you're looking for! Here's a summary of the key information about arxiv:2602.08082:

## Spectral Guardrails for Agents in the Wild

The paper proposes a training-free guardrail based on spectral analysis of attention topology to provide safeguards against tool use failures in autonomous agents.

**Key Results:**
- On Llama 3.1 8B, the method achieves 97.7% recall with multi-feature detection and 86.1% recall with 81.0% precision for balanced deployment, without requiring any labeled training data.
- Single layer spectral features act as near-perfect hallucination detectors: Llama L26 Smoothness achieves 98.2% recall (213/217 hallucinations caught) with a single threshold, and Mistral L3 Entropy achieves 94.7% recall.

**Core Insight:**
The key finding is that hallucination is not merely a wrong token but a thermodynamic state change: the model's attention becomes noise when it errs.

**Additional Findings:**
Through controlled cross-model evaluation, the paper reveals the "Loud Liar" phenomenon: Llama 3.1 8B's failures are spectrally catastrophic and dramatically easier to detect, while Mistral 7B achieves the best discrimination (AUC 0.900).

The paper was submitted on February 8, 2026, by Valentin Noël.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "480796f7-b507-43c3-b858-20f1adc3e412",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "e787ca11-e1a8-46f8-a870-ef51e72dc617",
  "sourceToolAssistantUUID": "480796f7-b507-43c3-b858-20f1adc3e412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T13:30:51.851Z_

<details><summary>↩ Tool result · `toolu_01GgPmWSCfBXCYueQcJ2jR82`</summary>

```text
Web search results for query: "EigenTrack spectral activation feature tracking hallucination detection arxiv 2509.15735"

Links: [{"title":"[2509.15735] EigenTrack: Spectral Activation Feature Tracking for Hallucination and Out-of-Distribution Detection in LLMs and VLMs","url":"https://arxiv.org/abs/2509.15735"},{"title":"EigenTrack: Temporal Spectral Analysis of Hidden Activations for Hallucination and OOD Detection","url":"https://arxiv.org/html/2509.15735v4"},{"title":"EigenTrack: Spectral Activation Feature Tracking for Hallucination and Out-of-Distribution Detection in LLMs and VLMs","url":"https://arxiv.org/html/2509.15735v1"},{"title":"(PDF) EigenTrack: Spectral Activation Feature Tracking for Hallucination and Out-of-Distribution Detection in LLMs and VLMs","url":"https://www.researchgate.net/publication/395709442_EigenTrack_Spectral_Activation_Feature_Tracking_for_Hallucination_and_Out-of-Distribution_Detection_in_LLMs_and_VLMs"},{"title":"EigenTrack: Spectral Activation Feature Tracking for ...","url":"https://arxiv.org/pdf/2509.15735"},{"title":"[PDF] EigenTrack: Spectral Activation Feature Tracking for Hallucination and Out-of-Distribution Detection in LLMs and VLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/EigenTrack:-Spectral-Activation-Feature-Tracking-in-Ettori-Darabi/dbd5adcae163620f5aa2ac258818485aebe2ff0a"},{"title":"1. Introduction","url":"https://arxiv.org/html/2602.22345"},{"title":"EigenTrack: Spectral Activation Feature Tracking for Hallucination and Out-of-Distribution Detection in LLMs and VLMs - Paper Detail","url":"https://deeplearn.org/arxiv/640439/eigentrack:-spectral-activation-feature-tracking-for-hallucination-and-out-of-distribution-detection-in-llms-and-vlms"},{"title":"Spectral Activation Feature Tracking for Hallucination and Out-of- ...","url":"https://www.aimodels.fyi/papers/arxiv/eigentrack-spectral-activation-feature-tracking-hallucination-out"},{"title":"au:Ettori_D in:cs - SciRate Search","url":"https://scirate.com/search?q=au:Ettori_D+in:cs"}]

## Search Results for EigenTrack (arXiv 2509.15735)

I found comprehensive information about the paper. Here are the key details:

### Overview
EigenTrack is an interpretable real-time detector that uses the spectral geometry of hidden activations, a compact global signature of model dynamics.

### Methodology
EigenTrack constructs sliding-window activation matrices, extracts covariance spectrum statistics including leading eigenvalues, spectral gaps, entropy, and Random Matrix Theory features based on divergence from the Marchenko-Pastur law, and streams these signals into a lightweight recurrent classifier to model temporal evolution.

Prior spectral methods such as RankFeat, SpectralGap, and SNoJoE discriminate OOD from in-distribution samples using singular values or spectral gaps, but operate on static snapshots and ignore temporal evolution. In contrast, EigenTrack transforms streaming spectral features into low-dimensional temporal trajectories that reveal how uncertainty accumulates during generation.

### Performance
EigenTrack achieves AUROC values of 0.82 to 0.94 for hallucination detection and 0.85 to 0.96 for OOD detection across LLMs and VLMs. On LLaMa-7B, it reaches 0.89 AUROC for hallucination and 0.92 for OOD, outperforming baselines such as HaloScope, LapEigvals, and SelfCheckGPT while using only a lightweight recurrent head.

### Advantages
EigenTrack operates with a single forward pass and no resampling.

The paper was submitted on September 19, 2025, with the latest version (v4) revised on February 6, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "284c6630-6f1d-438a-b36c-63d7b237653a",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "0e500405-3d06-46da-bea8-6cb5f6eccd2e",
  "sourceToolAssistantUUID": "284c6630-6f1d-438a-b36c-63d7b237653a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T13:30:52.562Z_

<details><summary>↩ Tool result · `toolu_01JRpD5GaVMU3PAEDgazjmFE`</summary>

```text
Web search results for query: ""frequency-aware attention" hallucination detection spectral operators arxiv 2602.18145"

Links: [{"title":"Detecting Contextual Hallucinations in Large Language Models with Frequency-Aware Attention","url":"https://arxiv.org/html/2602.18145"},{"title":"[2602.18145] Detecting Contextual Hallucinations in LLMs with Frequency-Aware Attention","url":"https://arxiv.org/abs/2602.18145"},{"title":"[2502.17598] Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/abs/2502.17598"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v1"},{"title":"[Literature Review] Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://www.themoonlight.io/en/review/hallucination-detection-in-llms-using-spectral-features-of-attention-maps"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1239/"},{"title":"Revision History for Hallucination Detection in LLMs Using...","url":"https://openreview.net/revisions?id=rFGUrBibMK"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250217598B/abstract"},{"title":"[2602.08082] Spectral Guardrails for Agents in the Wild: Detecting Tool Use Hallucinations via Attention Topology","url":"https://arxiv.org/abs/2602.08082"},{"title":"EigenTrack: Spectral Activation Feature Tracking for Hallucination and Out-of-Distribution Detection in LLMs and VLMs","url":"https://arxiv.org/html/2509.15735v1"}]

Based on the search results, I found the paper you're looking for. Here's what the research is about:

Hallucination detection is critical for ensuring the reliability of large language models (LLMs) in context-based generation, and prior work has explored intrinsic signals available during generation, among which attention offers a direct view of grounding behavior. However, existing approaches typically rely on coarse summaries that fail to capture fine-grained instabilities in attention.

The paper arxiv 2602.18145 addresses this by proposing a novel approach: Inspired by signal processing, the authors introduce a frequency-aware perspective on attention by analyzing its variation during generation, modeling attention distributions as discrete signals and extracting high-frequency components that reflect rapid local changes in attention.

The analysis reveals that hallucinated tokens are associated with high-frequency attention energy, reflecting fragmented and unstable grounding behavior. Based on this insight, the authors introduce a frequency-aware attention modeling framework that extracts high-frequency attention signals using spectral operators.

Across multiple models and tasks, their approach improves hallucination detection at both token and span levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19dd3c47-8b26-4531-8eae-b8a80e76defa",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "f451b99a-21d1-4eda-9072-ac6ff0d1bac3",
  "sourceToolAssistantUUID": "19dd3c47-8b26-4531-8eae-b8a80e76defa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T13:30:54.026Z_

<details><summary>↩ Tool result · `toolu_011bdcLTEv5HrHmdvUFRiweA`</summary>

```text
Web search results for query: "HaluGate token-level hallucination detection vLLM production pipeline"

Links: [{"title":"Token-Level Truth: Real-Time Hallucination Detection for Production LLMs | vLLM Blog","url":"https://blog.vllm.ai/2025/12/14/halugate.html"},{"title":"vLLM Semantic Router v0.1 Iris: The First Major Release | vLLM Blog","url":"https://blog.vllm.ai/2026/01/05/vllm-sr-iris.html"},{"title":"Token-Level Truth: Real-Time Hallucination Detection for Production LLMs | vLLM Semantic Router","url":"https://vllm-semantic-router.com/blog/halugate/"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.04444v1"},{"title":"llm-semantic-router/halugate-sentinel · Hugging Face","url":"https://huggingface.co/llm-semantic-router/halugate-sentinel"},{"title":"vLLM Semantic Router: Signal Driven Decision Routing for ...","url":"https://arxiv.org/pdf/2603.04444"},{"title":"The Workload–Router–Pool Architecture for LLM Inference Optimization A Vision Paper from the vLLM Semantic Router Project","url":"https://arxiv.org/html/2603.21354v1"},{"title":"HalLoc: Token-level Localization of Hallucinations for Vision Language Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Park_HalLoc_Token-level_Localization_of_Hallucinations_for_Vision_Language_Models_CVPR_2025_paper.pdf"},{"title":"(PDF) HalLoc: Token-level Localization of Hallucinations for Vision Language Models","url":"https://www.researchgate.net/publication/392629473_HalLoc_Token-level_Localization_of_Hallucinations_for_Vision_Language_Models"},{"title":"(PDF) Detecting and Preventing Hallucinations in Large Vision Language Models","url":"https://www.researchgate.net/publication/373117275_Detecting_and_Preventing_Hallucinations_in_Large_Vision_Language_Models"}]

Based on the search results, here's comprehensive information about HaluGate:

## HaluGate: Token-Level Hallucination Detection for Production LLMs

HaluGate is a conditional, token-level hallucination detection pipeline that catches unsupported claims before they reach users, integrated into the vLLM Semantic Router system.

### Architecture

HaluGate is a three-stage pipeline consisting of sentinel gating, token-level detection, and NLI-based explanation that avoids unnecessary verification on non-factual queries while providing span-level diagnostics when hallucination is detected.

The three stages are:
1. **HaluGate Sentinel**: A ModernBERT-based classifier that answers whether a prompt warrants factual verification
2. **HaluGate Detector**: Token-level detection identifying exactly which tokens in the response are unsupported by the provided context
3. **HaluGate Explainer**: NLI-based classification explaining why each flagged span is problematic

### Production Pipeline Performance

In production workloads where approximately 35% of queries are non-factual, pre-classification achieves a 72.2% efficiency gain by skipping expensive detection entirely for creative, coding, and opinion queries. The total overhead of HaluGate (76-162ms) is negligible compared to typical LLM generation times (5-30 seconds), making it practical for synchronous request processing.

### Implementation Details

All three models run natively via Candle (Hugging Face's Rust ML framework) with CGO bindings to Go, eliminating the need for a separate Python service, sidecars, or model servers—everything runs in-process.

HaluGate specifically targets extrinsic hallucinations where tool/RAG context provides grounding for verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45115f05-5645-4176-a6ee-c6eb846cae54",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "e2a98451-a0c8-47b5-9e25-14a772f2051c",
  "sourceToolAssistantUUID": "45115f05-5645-4176-a6ee-c6eb846cae54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-15T13:30:56.985Z_

Let me do a couple more targeted searches on papers that seem very close to the SpectralWatch idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2a98451-a0c8-47b5-9e25-14a772f2051c",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SHMPhbkn5oiz15GkgD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5e047a7-980a-4e1b-8271-8eb09cf539e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AFXj5aKZtFukx3yY9BK1Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 5361,
      "cache_read_input_tokens": 19752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5361,
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

_source line 40 · 2026-05-15T13:30:58.017Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ThZWxYx9JtcEbJM96j2jpM`</summary>

```json
{
  "query": "LapEigvals Laplacian eigenvalues attention maps hallucination detection EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5e047a7-980a-4e1b-8271-8eb09cf539e8",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SHMPhbkn5oiz15GkgD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3d2d564-2d78-49f6-b58a-93a300932dd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AFXj5aKZtFukx3yY9BK1Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 5361,
      "cache_read_input_tokens": 19752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5361,
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

_source line 41 · 2026-05-15T13:30:59.411Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NCfeXATeJTf8tHd3FFh76h`</summary>

```json
{
  "query": "\"PCNet\" \"PC-LDCD\" hallucination anomaly probabilistic circuits dynamic intervention decoding 2605.05953"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3d2d564-2d78-49f6-b58a-93a300932dd9",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SHMPhbkn5oiz15GkgD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d493984-549d-44e0-948a-65c7f06319e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AFXj5aKZtFukx3yY9BK1Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 5361,
      "cache_read_input_tokens": 19752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5361,
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

_source line 42 · 2026-05-15T13:31:00.425Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019UzAZmymeXus9hhE5zEPV1`</summary>

```json
{
  "query": "CHARM neural message passing attention graphs hallucination GNN 2509.24770"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d493984-549d-44e0-948a-65c7f06319e9",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SHMPhbkn5oiz15GkgD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f47caa74-325f-4427-a4a6-6bf154bea346",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AFXj5aKZtFukx3yY9BK1Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 5361,
      "cache_read_input_tokens": 19752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5361,
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

_source line 43 · 2026-05-15T13:31:00.661Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NyvjAVZUv4De345g3mgqLH`</summary>

```json
{
  "query": "\"attention sinks\" hallucination detection internal signals 2604.10697"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f47caa74-325f-4427-a4a6-6bf154bea346",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SHMPhbkn5oiz15GkgD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f78d2cca-351d-43cd-aceb-dbfa17a256f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AFXj5aKZtFukx3yY9BK1Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 5361,
      "cache_read_input_tokens": 19752,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5361
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 832,
          "output_tokens": 266,
          "cache_read_input_tokens": 19752,
          "cache_creation_input_tokens": 5361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5361,
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

_source line 44 · 2026-05-15T13:31:02.841Z_

<details><summary>↩ Tool result · `toolu_01ThZWxYx9JtcEbJM96j2jpM`</summary>

```text
Web search results for query: "LapEigvals Laplacian eigenvalues attention maps hallucination detection EMNLP 2025"

Links: [{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1239/"},{"title":"[2502.17598] Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/abs/2502.17598"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250217598B/abstract"},{"title":"GitHub - graphml-lab-pwr/lapeigvals: Implementation of the paper \"Hallucination Detection in LLMs Using Spectral Features of Attention Maps\" · GitHub","url":"https://github.com/graphml-lab-pwr/lapeigvals"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-main.1239@ACL"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v2"},{"title":"Hallucination Detection in LLMs Using Spectral Features of ...","url":"https://aclanthology.org/2025.emnlp-main.1239.pdf"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://openreview.net/pdf?id=YYYiHkFKJs"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps | Request PDF","url":"https://www.researchgate.net/publication/397421008_Hallucination_Detection_in_LLMs_Using_Spectral_Features_of_Attention_Maps"},{"title":"[2502.17598v1] Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/abs/2502.17598v1"}]

I found comprehensive information about the LapEigvals paper. Here are the search results:

## Overview

The LapEigvals method utilises the top-k eigenvalues of the Laplacian matrix derived from the attention maps as an input to hallucination detection probes.

## Publication Details

The paper was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing in Suzhou, China. The authors are Jakub Binkowski, Denis Janiak, Albert Sawczyn, Bogdan Gabrys, and Tomasz Jan Kajdanowicz.

## Key Contributions

The work investigates the spectral features of attention maps by interpreting them as adjacency matrices of graph structures. Empirical evaluations demonstrate that the approach achieves state-of-the-art hallucination detection performance among attention-based methods, with extensive ablation studies highlighting the robustness and generalisation of LapEigvals.

## Implementation

The official implementation of the paper has been made publicly available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3d2d564-2d78-49f6-b58a-93a300932dd9",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "423b32af-0191-4306-9e6c-a8217b3e14a8",
  "sourceToolAssistantUUID": "a3d2d564-2d78-49f6-b58a-93a300932dd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T13:31:05.504Z_

<details><summary>↩ Tool result · `toolu_01NCfeXATeJTf8tHd3FFh76h`</summary>

```text
Web search results for query: ""PCNet" "PC-LDCD" hallucination anomaly probabilistic circuits dynamic intervention decoding 2605.05953"

Links: [{"title":"[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/abs/2605.05953"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"[2503.03106] Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation","url":"https://arxiv.org/abs/2503.03106"},{"title":"Mitigating Hallucinations in Multi-modal Large Language ...","url":"https://aclanthology.org/2025.naacl-long.75.pdf"},{"title":"Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation","url":"https://arxiv.org/html/2503.03106v1"},{"title":"[2504.12137] Efficient Contrastive Decoding with Probabilistic Hallucination Detection - Mitigating Hallucinations in Large Vision Language Models -","url":"https://ar5iv.labs.arxiv.org/html/2504.12137"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=5650&show=25"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=18875&show=25"},{"title":"Activation Steering Decoding: Mitigating Hallucination in ...","url":"https://aclanthology.org/2025.acl-long.634.pdf"},{"title":"Why Language Models Hallucinate Adam Tauman Kalai∗ OpenAI Ofir Nachum OpenAI","url":"https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf"}]

Based on the search results, I found the paper you're looking for:

The paper is titled "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" (arXiv 2605.05953).

Here's an overview of the research:

**Main Contributions:**

The paper proposes PCNet, a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream. The method detects hallucinations as geometric anomalies on the factual manifold via exact Negative Log-Likelihood computation, without the need for sampling, external verifiers, or weight modifications.

The second main contribution is PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding), which intervenes only when the latent geometry deviates from factual regions, while leaving correct generations untouched.

**Key Results:**

PCNet achieves near-perfect hallucination detection across CoQA, SQuAD v2.0, and TriviaQA, with AUROC reaching up to 99%. PC-LDCD obtains the highest scores on TruthfulQA in three out of four models, while reducing the mean corruption rate and achieving a preservation rate of 79.3%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d493984-549d-44e0-948a-65c7f06319e9",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "54dcbe7f-9778-4c51-8f7f-6b3436f163eb",
  "sourceToolAssistantUUID": "4d493984-549d-44e0-948a-65c7f06319e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T13:31:06.907Z_

<details><summary>↩ Tool result · `toolu_019UzAZmymeXus9hhE5zEPV1`</summary>

```text
Web search results for query: "CHARM neural message passing attention graphs hallucination GNN 2509.24770"

Links: [{"title":"[2509.24770] Neural Message-Passing on Attention Graphs for Hallucination Detection","url":"https://arxiv.org/abs/2509.24770"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection","url":"https://arxiv.org/html/2509.24770v1"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=4twbqwV4br"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection | alphaXiv","url":"https://www.alphaxiv.org/resources/2509.24770"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection | Request PDF","url":"https://www.researchgate.net/publication/395972306_Neural_Message-Passing_on_Attention_Graphs_for_Hallucination_Detection"},{"title":"[PDF] Neural Message-Passing on Attention Graphs for Hallucination Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Neural-Message-Passing-on-Attention-Graphs-for-Frasca-Bar-Shalom/abb40a4db2c93c8bfffdb0072dc0ca4a040347ab"},{"title":"Neural Message-Passing on Attention Graphs for ...","url":"https://arxiv.org/pdf/2509.24770"},{"title":"GitHub - Noired/charm: Neural Message-Passing on Attention Graphs for Hallucination Detection · GitHub","url":"https://github.com/Noired/charm"},{"title":"[Literature Review] Neural Message-Passing on Attention Graphs for Hallucination Detection","url":"https://www.themoonlight.io/en/review/neural-message-passing-on-attention-graphs-for-hallucination-detection"},{"title":"NEURAL MESSAGE-PASSING ON ATTENTION GRAPHS","url":"https://openreview.net/pdf?id=4twbqwV4br"}]

Based on the search results, here's what I found about the paper with ID 2509.24770:

## Overview

This is an arXiv paper titled "Neural Message-Passing on Attention Graphs for Hallucination Detection", published on September 29, 2025.

## Key Contribution

CHARM casts hallucination detection as a graph learning task and tackles it by applying GNNs over attributed graphs, where tokens are nodes, edges follow attentional flows, and both carry features from attention scores and activations.

## Main Results

CHARM provably subsumes prior attention-based heuristics and experimentally outperforms other leading approaches across diverse benchmarks. The results show the relevant role played by the graph structure and the benefits of combining computational traces, with CHARM exhibiting promising zero-shot performance on cross-dataset transfer.

## Authors

The paper is authored by Fabrizio Frasca, Guy Bar-Shalom, Yftah Ziser, and Haggai Maron.

The paper represents an approach to detecting hallucinations in Large Language Models by leveraging graph neural networks to process the internal computational structures of LLMs in a unified framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f47caa74-325f-4427-a4a6-6bf154bea346",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "1d6854b6-9fd0-491a-9c9e-4cdb7ba14f03",
  "sourceToolAssistantUUID": "f47caa74-325f-4427-a4a6-6bf154bea346",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T13:31:08.308Z_

<details><summary>↩ Tool result · `toolu_01NyvjAVZUv4De345g3mgqLH`</summary>

```text
Web search results for query: ""attention sinks" hallucination detection internal signals 2604.10697"

Links: [{"title":"[2604.10697] Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/abs/2604.10697"},{"title":"Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2604.10697"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps | Request PDF","url":"https://www.researchgate.net/publication/397421008_Hallucination_Detection_in_LLMs_Using_Spectral_Features_of_Attention_Maps"},{"title":"Spotlight and Shadow: Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation","url":"https://arxiv.org/html/2604.10071v1"},{"title":"What drives attention sinks? A study of massive activations and rotational positional encoding in large vision–language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325003723"},{"title":"Hallucination Attack on Multi-modal Large Language ...","url":"https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-1176-wang-yining.pdf"},{"title":"Interpretable Signals for Detecting Hallucinations in ...","url":"https://arxiv.org/pdf/2510.21538"},{"title":"VADE: Visual Attention Guided Hallucination Detection and ...","url":"https://aclanthology.org/2025.findings-acl.773.pdf"},{"title":"RAGognizer: Hallucination-Aware Fine-Tuning via Detection Head Integration","url":"https://arxiv.org/html/2604.15945v1"},{"title":"FACTUM: Mechanistic Detection of Citation Hallucination in Long-Form RAG","url":"https://arxiv.org/pdf/2601.05866"}]

Based on the search results, I found the paper you were looking for. Here's what I found about arXiv:2604.10697:

## Paper Overview

The paper is titled "Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models" by Jakub Binkowski, Kamil Adamczewski, and Tomasz Kajdanowicz, submitted on April 12, 2026.

## Main Contribution

The authors propose SinkProbe, a hallucination detection method grounded in the observation that hallucinations are deeply entangled with attention sinks - tokens that accumulate disproportionate attention mass during generation - indicating a transition from distributed, input-grounded attention to compressed, prior-dominated computation.

## Key Findings

Although sink scores are computed solely from attention maps, the classifier preferentially relies on sinks whose associated value vectors have large norms. Additionally, previous methods implicitly depend on attention sinks by establishing their mathematical relationship to sink scores.

## Results

The findings yield a novel hallucination detection method grounded in theory that produces state-of-the-art results across popular datasets and LLMs.

The paper is available on arXiv at https://arxiv.org/abs/2604.10697.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f78d2cca-351d-43cd-aceb-dbfa17a256f8",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "ae019216-bd62-4744-a8d2-618818c9c99d",
  "sourceToolAssistantUUID": "f78d2cca-351d-43cd-aceb-dbfa17a256f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-15T13:31:12.829Z_

Let me do one final search to make sure I haven't missed the closest competitor -- a paper that specifically does *predictive/early* detection during autoregressive generation using spectral methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae019216-bd62-4744-a8d2-618818c9c99d",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SJQUX9GCgXsuv4J3DP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b01ef0bc-e0ff-4a8e-94b5-f8178df5c56e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqbjm6qvJcP1CGG8Gi1i39",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4652,
      "cache_read_input_tokens": 25113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4652,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 49 · 2026-05-15T13:31:13.445Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QpLDvkhmcu4Tnb25g6M6iF`</summary>

```json
{
  "query": "\"Monitoring Decoding\" hallucination factuality partial response generation 2503.03106"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b01ef0bc-e0ff-4a8e-94b5-f8178df5c56e",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SJQUX9GCgXsuv4J3DP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ef633fe-24ba-4a62-ab9d-59b14b09114e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqbjm6qvJcP1CGG8Gi1i39",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4652,
      "cache_read_input_tokens": 25113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4652,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 50 · 2026-05-15T13:31:13.757Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017AF3x8vQK2wqpvE66shrPG`</summary>

```json
{
  "query": "Laplacian spectrum attention autoregressive generation hallucination prediction tokens ahead"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ef633fe-24ba-4a62-ab9d-59b14b09114e",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SJQUX9GCgXsuv4J3DP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c465f985-9ce2-4d87-8c12-e602455e4fa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aqbjm6qvJcP1CGG8Gi1i39",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4652,
      "cache_read_input_tokens": 25113,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4652
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 25113,
          "cache_creation_input_tokens": 4652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4652,
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

_source line 51 · 2026-05-15T13:31:20.972Z_

<details><summary>↩ Tool result · `toolu_017AF3x8vQK2wqpvE66shrPG`</summary>

```text
Web search results for query: "Laplacian spectrum attention autoregressive generation hallucination prediction tokens ahead"

Links: [{"title":"[2502.17598] Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/abs/2502.17598"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v2"},{"title":"Hallucination Detection in LLMs Using Spectral Features of ...","url":"https://aclanthology.org/2025.emnlp-main.1239.pdf"},{"title":"Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/html/2510.06265v2"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1239/"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"GitHub - graphml-lab-pwr/lapeigvals: Implementation of the paper \"Hallucination Detection in LLMs Using Spectral Features of Attention Maps\" · GitHub","url":"https://github.com/graphml-lab-pwr/lapeigvals"},{"title":"Hallucination of Multimodal Large Language Models: A Survey","url":"https://arxiv.org/pdf/2404.18930"},{"title":"Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://arxiv.org/pdf/2504.07863"},{"title":"1 A Survey on Hallucination in Large Language Models:","url":"https://arxiv.org/pdf/2311.05232"}]

Based on the web search results, here's what I found about the query regarding Laplacian spectrum attention and autoregressive generation:

## Hallucination Detection in LLMs Using Laplacian Spectral Features

The most relevant research involves a method that investigates the spectral features of attention maps by interpreting them as adjacency matrices of graph structures, utilizing the top-k eigenvalues of the Laplacian matrix derived from the attention maps as an input to hallucination detection probes. This approach is called **LapEigvals**.

### Key Findings:

**Performance:** The approach achieves state-of-the-art hallucination detection performance among attention-based methods.

**Why Laplacian Eigenvalues Work:** Laplacian eigenvalues may be better predictors of hallucinations, as feature values across more heads exhibit statistically significant differences between hallucinated and non-hallucinated examples.

**Theoretical Foundation:** The attention matrix can be considered as an adjacency matrix representing a set of Markov chains, and hallucinations may arise from disruptions in information flow, such as bottlenecks, which could be detected through the graph Laplacian.

### Connection to Autoregressive Generation:

The research relates to autoregressive LLMs which process text unidirectionally in a left-to-right fashion, a behavior that inherently limits their capacity to comprehensively capture and integrate contextual information from both preceding and subsequent tokens, which can contribute to hallucinations.

The full paper and implementation are available through academic databases and GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c465f985-9ce2-4d87-8c12-e602455e4fa3",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "217a4723-4a21-4400-98da-55f7ea827868",
  "sourceToolAssistantUUID": "c465f985-9ce2-4d87-8c12-e602455e4fa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T13:31:21.999Z_

<details><summary>↩ Tool result · `toolu_01QpLDvkhmcu4Tnb25g6M6iF`</summary>

```text
Web search results for query: ""Monitoring Decoding" hallucination factuality partial response generation 2503.03106"

Links: [{"title":"[2503.03106] Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation","url":"https://arxiv.org/abs/2503.03106"},{"title":"Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation","url":"https://arxiv.org/html/2503.03106"},{"title":"Monitoring Decoding: Mitigating Hallucination via Evaluating the","url":"https://www.researchgate.net/publication/389617318_Monitoring_Decoding_Mitigating_Hallucination_via_Evaluating_the_Factuality_of_Partial_Response_during_Generation/fulltext/67c9beef32265243f583202b/Monitoring-Decoding-Mitigating-Hallucination-via-Evaluating-the-Factuality-of-Partial-Response-during-Generation.pdf?origin=scientificContributions"},{"title":"[Quick Review] Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation","url":"https://liner.com/review/monitoring-decoding-mitigating-hallucination-via-evaluating-factuality-partial-response-during"},{"title":"Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation","url":"https://www.researchgate.net/publication/394269763_Monitoring_Decoding_Mitigating_Hallucination_via_Evaluating_the_Factuality_of_Partial_Response_during_Generation"},{"title":"Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/monitoring-decoding-mitigating-hallucination-via-evaluating-factuality"},{"title":"Mitigating Hallucination via Evaluating the Factuality of ...","url":"https://aclanthology.org/2025.findings-acl.752.pdf"},{"title":"A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3703155"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Detecting hallucinations in large language models using semantic entropy | Nature","url":"https://www.nature.com/articles/s41586-024-07421-0"}]

Based on the search results, here's what I found about the paper (arXiv:2503.03106):

## Overview

The paper introduces Monitoring Decoding (MD), a novel framework that dynamically monitors the generation process and selectively applies in-process interventions, focusing on revising crucial tokens responsible for hallucinations.

## Problem Being Addressed

Large language models remain susceptible to hallucinations -- generating plausible yet factually incorrect contents. Existing methods to mitigating such risk often rely on sampling multiple full-length generations, which introduces significant response latency and becomes ineffective when the model consistently produces hallucinated outputs with high confidence.

## Key Approach

The framework identifies hallucination-prone tokens during generation using a monitor function, and further refines these tokens through a tree-based decoding strategy. The monitor function acts as a supervisory component to assess the factual consistency of intermediate tokens during partial decoding, flagging and rejecting those with hallucination risk.

## Results

Experimental results demonstrate that MD consistently outperforms self-consistency-based approaches in both effectiveness and efficiency, achieving higher factual accuracy while significantly reducing computational overhead.

## Authors

The paper is authored by Yurui Chang, Bochuan Cao, and Lu Lin from the College of Information Sciences and Technology at Pennsylvania State University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ef633fe-24ba-4a62-ab9d-59b14b09114e",
  "isSidechain": true,
  "promptId": "da773450-88fb-4e62-8bf1-d5f26e7dcb6a",
  "agentId": "a91a20d33dc5ad48e",
  "type": "user",
  "uuid": "18bf0f0a-5782-4d41-bb97-f35bb5717cea",
  "sourceToolAssistantUUID": "8ef633fe-24ba-4a62-ab9d-59b14b09114e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-15T13:32:58.423Z_

I now have comprehensive results across all 10 searches plus follow-ups. Here is the full report.

---

## Literature Search Report: Competing and Concurrent Work to SpectralWatch

I ran 10 primary searches and 6 follow-up searches. Below are the results organized by search query, followed by a critical synthesis identifying the papers most threatening to SpectralWatch's novelty.

---

### Search 1: "online hallucination detection LLM decoding time 2025 2026"

**Top relevant results:**

1. **HaluGate** (vLLM Blog, Dec 2025) -- A conditional, token-level hallucination detection pipeline integrated into vLLM Semantic Router. Three-stage pipeline (sentinel gating, token-level detection, NLI explanation) that catches unsupported claims before they reach users. Overhead is 76-162ms, negligible vs. typical 5-30s generation times. Targets extrinsic hallucinations in RAG settings. [vLLM Blog](https://blog.vllm.ai/2025/12/14/halugate.html)

2. **UQLM** (CVS Health Tech Blog, Medium) -- Detects hallucinations at generation time using uncertainty quantification. [Medium](https://medium.com/cvs-health-tech-blog/detecting-llm-hallucinations-at-generation-time-with-uqlm-cd749d2338ec)

3. **Logical Consistency as a Bridge** (arXiv 2605.03971) -- Uses label constraint modeling between responses and self-judgments. [arXiv](https://arxiv.org/html/2605.03971v1)

---

### Search 2: "attention spectral analysis hallucination prediction real-time"

**Top relevant results -- THIS SEARCH FOUND THE CLOSEST COMPETITORS:**

1. **LapEigvals** (Binkowski et al., EMNLP 2025, arXiv 2502.17598) -- **VERY HIGH OVERLAP WITH SPECTRALWATCH.** Uses top-k eigenvalues of the Laplacian matrix derived from attention maps (interpreted as adjacency matrices of graph structures) as input to hallucination detection probes. Achieves SOTA among attention-based methods. Code available at [GitHub](https://github.com/graphml-lab-pwr/lapeigvals). Published at [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1239/).

2. **EigenTrack** (Ettori et al., arXiv 2509.15735, revised Feb 2026) -- **HIGH OVERLAP.** An interpretable real-time detector that uses spectral geometry of hidden activations with sliding-window activation matrices, extracts covariance spectrum statistics (leading eigenvalues, spectral gaps, entropy, Random Matrix Theory features), and streams them into a lightweight recurrent classifier to model temporal evolution. Achieves 0.82-0.94 AUROC for hallucination detection. Operates with a single forward pass and no resampling. [arXiv](https://arxiv.org/abs/2509.15735)

3. **Frequency-Aware Attention** (arXiv 2602.18145, Feb 2026) -- **HIGH OVERLAP.** Models attention distributions as discrete signals, extracts high-frequency components reflecting rapid local changes in attention during generation. Finds that hallucinated tokens are associated with high-frequency attention energy (fragmented and unstable grounding behavior). Improves detection at both token and span levels. [arXiv](https://arxiv.org/abs/2602.18145)

---

### Search 3: "incremental eigenvalue attention hallucination"

Results largely overlapped with Search 2. Key additions:

1. **LLM-Check** (NSF/OpenReview) -- Investigates detection of hallucinations using various internal signals. [NSF](https://par.nsf.gov/servlets/purl/10574407)

2. **"LLMs' Internal States Retain the Power of Hallucination Detection"** (arXiv 2402.03744) -- Shows that internal states are strong signals for detecting hallucinations. [arXiv](https://arxiv.org/pdf/2402.03744)

---

### Search 4: "predictive hallucination detection before generation LLM"

**Top relevant results:**

1. **Semantic Entropy** (Nature, 2024) -- Detects hallucinations using semantic entropy across sampled outputs. Foundational work. [Nature](https://www.nature.com/articles/s41586-024-07421-0)

2. **Input-Based Hidden State Classifiers** -- Lightweight classifier that detects hallucinations *preemptively* conditioning only on input hidden states before text is generated, then intervenes in hidden states to steer toward factual outputs.

3. **Intermediate Layer Probes** -- Trains lightweight probes (3M-37M params) on intermediate hidden states. Question-only mode runs before/alongside generation with no added latency. [Deepchecks](https://deepchecks.com/llm-hallucination-detection-and-mitigation-best-techniques/)

4. **Adaptive Token Selection (HaMI)** (arXiv 2504.07863, NeurIPS 2025) -- Formulates hallucination detection as multiple instance learning over token-level representations. [arXiv](https://arxiv.org/abs/2504.07863), [GitHub](https://github.com/mala-lab/HaMI)

---

### Search 5: "early warning hallucination LLM token-level 2026"

**Top relevant results:**

1. **Next-Token Gradient Sensitivity (NGS)** (OpenReview) -- Quantifies the first-order gradient of the maximum log-probability of the next token w.r.t. the current token's layer embedding, measuring local prediction fragility. Frames detection as token-level distribution comparison. [OpenReview](https://openreview.net/forum?id=yzWGQNTbHQ)

2. **"Think Token" Injection System** -- Monitors token-by-token generation uncertainty against a threshold and injects additional computation prompts during streaming when uncertainty exceeds bounds.

3. **"First Hallucination Tokens Are Different from Conditional Ones"** (arXiv 2507.20836) -- Shows the first token in a hallucinated span carries a stronger hallucination signal than subsequent tokens, achieving higher detection accuracy. [arXiv](https://arxiv.org/html/2507.20836v4)

---

### Search 6: "spectral attention dynamics language model 2026"

**Top relevant results:**

1. **Spectral Editing Key Amplification (SEKA)** -- Steers attention by modifying key vectors using spectral decomposition to learn a "relevance subspace." [OpenReview](https://openreview.net/pdf/61b1d6aa10b647458c65499b860d5a264e38c178.pdf)

2. **DiffEqFormer** -- Models attention/FFN block weights as functions of continuous layer index; observed spectral dynamics show increasing eigenvalue magnitudes. [ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/82e3509393670d9d478c359b4ce6f950-Paper-Conference.pdf)

3. **Emergent Mind topic page on "Spectral Analysis of Attention Patterns"** -- Aggregates research in this area. [EmergentMind](https://www.emergentmind.com/topics/spectral-analysis-of-attention-patterns)

---

### Search 7: "proactive hallucination intervention decoding LLM"

**Top relevant results:**

1. **PCNet + PC-LDCD** (arXiv 2605.05953, May 2026) -- **NOTABLE.** Frames hallucinations as geometric anomalies on the factual manifold. PCNet (Probabilistic Circuits) computes exact NLL in a single forward pass, achieving up to 99% AUROC. PC-LDCD intervenes only when latent geometry deviates from factual regions. [arXiv](https://arxiv.org/abs/2605.05953)

2. **DoLa (Decoding by Contrasting Layers)** -- Contrastive decoding strategy between early and late layers. No external knowledge or fine-tuning needed.

3. **Hallucination Head Intervention for VLMs** -- Targets specific attention heads to reduce reliance on text tokens, achieving up to 1.7x reduction in hallucination rate.

---

### Search 8: "attention graph topology hallucination online monitoring"

**Top relevant results -- MORE CLOSE COMPETITORS:**

1. **TOHA** (arXiv 2504.10063, Apr 2025) -- **HIGH OVERLAP.** Topology-based hallucination detector using topological divergence metric between prompt and response subgraphs of attention-induced graphs. Discovers "hallucination-aware attention heads." SOTA or competitive results with minimal annotated data. [arXiv](https://arxiv.org/abs/2504.10063)

2. **Spectral Guardrails** (Noel, arXiv 2602.08082, Feb 2026) -- **VERY HIGH OVERLAP.** Training-free guardrail based on spectral analysis of attention topology. Treats attention matrices as dynamic graphs and computes Laplacian spectrum properties. Achieves 97.7% recall without labeled training data. Key insight: "hallucination is not merely a wrong token but a thermodynamic state change: the model's attention becomes noise when it errs." Discovers the "Loud Liar" phenomenon. [arXiv](https://arxiv.org/abs/2602.08082)

3. **CHARM** (Frasca et al., arXiv 2509.24770, Sep 2025) -- Casts hallucination detection as a graph learning task applying GNNs over attributed attention graphs. Tokens are nodes, edges follow attentional flows. Subsumes prior attention-based heuristics. Promising zero-shot cross-dataset transfer. [arXiv](https://arxiv.org/abs/2509.24770)

4. **Temporal Graph Network for Multi-Turn Conversation** (arXiv 2601.03051, Jan 2026) -- Uses temporal graph networks for hallucination detection across conversation turns. [arXiv](https://arxiv.org/abs/2601.03051)

---

### Search 9: "token-level hallucination prediction internal representations 2025 2026"

**Top relevant results:**

1. **SinkProbe** (Binkowski et al., arXiv 2604.10697, Apr 2026) -- **NOTABLE.** Detects hallucinations using attention sinks (tokens accumulating disproportionate attention mass). Proposes that hallucination involves a transition from distributed, input-grounded attention to compressed, prior-dominated computation. SOTA results. Same research group as LapEigvals. [arXiv](https://arxiv.org/abs/2604.10697)

2. **"First Hallucination Tokens Are Different"** (arXiv 2507.20836) -- Position-aware analysis showing first hallucinated token carries stronger signal. [arXiv](https://arxiv.org/html/2507.20836v4)

3. **Token-Level Self-Consistency** (SemEval/ACL 2025) -- Self-consistency methods applied at token level. [ACL Anthology](https://aclanthology.org/2025.semeval-1.38.pdf)

---

### Search 10: "look-ahead hallucination detection LLM generation"

**Top relevant results:**

1. **Monitoring Decoding (MD)** (Chang et al., arXiv 2503.03106, Mar 2025, ACL Findings 2025) -- **CONCEPTUALLY CLOSE.** Dynamically monitors the generation process and selectively applies in-process interventions, focusing on revising crucial tokens responsible for hallucinations. Uses a monitor function to assess factual consistency of intermediate tokens during partial decoding, flagging and rejecting those with hallucination risk. Tree-based decoding strategy for refinement. [arXiv](https://arxiv.org/abs/2503.03106)

2. **MetaQA** -- Uses metamorphic prompt mutations to detect hallucinations even in closed-source models.

---

## Critical Synthesis: What SpectralWatch Authors Must Cite and Differentiate From

### Tier 1 -- Papers with VERY HIGH overlap (potential prior art / scooping risk):

| Paper | Key Overlap | Key Difference from SpectralWatch |
|-------|------------|----------------------------------|
| **LapEigvals** (EMNLP 2025) | Uses Laplacian eigenvalues of attention-as-graph for hallucination detection -- essentially the same core feature | Appears to be a post-hoc classifier, not explicitly monitoring *dynamics* during autoregressive generation or claiming predictive 3-5 token lead time |
| **EigenTrack** (arXiv, Sep 2025, rev. Feb 2026) | Temporal spectral tracking during generation using sliding windows and eigenvalue-based features with a recurrent classifier | Operates on hidden activations (not attention graphs); uses covariance spectrum rather than graph Laplacian; does model temporal dynamics |
| **Spectral Guardrails** (arXiv, Feb 2026) | Training-free spectral analysis of attention topology using Laplacian spectrum; framing of "thermodynamic state change" | Focused on tool-use hallucinations in agents; does not claim predictive lead time; appears more of a concurrent detection than prediction |
| **Frequency-Aware Attention** (arXiv, Feb 2026) | Spectral operators on attention dynamics during generation; hallucinated tokens associated with high-frequency attention energy | Uses Fourier-domain analysis rather than graph Laplacian eigenvalues; complementary spectral perspective |

### Tier 2 -- Papers with HIGH overlap (must cite, substantial conceptual overlap):

- **TOHA** (arXiv 2504.10063) -- Topological divergence on attention graphs
- **CHARM** (arXiv 2509.24770) -- GNN message-passing on attention graphs
- **SinkProbe** (arXiv 2604.10697) -- Attention sink dynamics as hallucination signal (same group as LapEigvals)
- **Monitoring Decoding** (arXiv 2503.03106) -- Dynamic monitoring during generation with intervention
- **PCNet/PC-LDCD** (arXiv 2605.05953) -- Dynamic anomaly detection on latent geometry during decoding

### Tier 3 -- Important context papers:

- **HaluGate** (vLLM, Dec 2025) -- Production token-level detection pipeline
- **NGS** (Next-Token Gradient Sensitivity) -- Token-level fragility measurement
- **"First Hallucination Tokens Are Different"** -- Early token signals
- **HaMI** (NeurIPS 2025) -- Adaptive token selection for hallucination detection

### Bottom Line Assessment:

**LapEigvals is the single most threatening prior work** -- it uses the exact same feature (Laplacian eigenvalues of attention-as-graph) for the exact same purpose (hallucination detection). SpectralWatch's claimed novelty must rest on (a) the *temporal monitoring* aspect (tracking eigenvalue dynamics across tokens during autoregressive generation), (b) the *predictive* claim (3-5 tokens ahead), and (c) the *online/streaming* nature. LapEigvals appears to be a static, post-hoc classifier.

**EigenTrack is the second most threatening** -- it already does temporal spectral tracking during generation with a recurrent classifier, but on hidden activation covariance spectra rather than attention graph Laplacians. The temporal/streaming aspect that SpectralWatch might claim as novel over LapEigvals is already present in EigenTrack, just on different representations.

**Spectral Guardrails** (Feb 2026) is concurrent work that also uses attention Laplacian spectrum features in a training-free manner, though focused on agent tool-use rather than general text generation.

The SpectralWatch authors should carefully position their contribution as the combination of: (1) graph Laplacian eigenvalues specifically from attention matrices (unlike EigenTrack's hidden activation covariance), (2) temporal dynamics tracking during autoregressive generation (unlike LapEigvals' static classification), and (3) predictive capability with a claimed 3-5 token lead time (which none of the above papers explicitly claim). The predictive lead-time claim appears to be the most distinctive element, but it needs rigorous empirical validation against these baselines.

Sources:
- [LapEigvals - EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1239/)
- [LapEigvals - arXiv](https://arxiv.org/abs/2502.17598)
- [LapEigvals - GitHub](https://github.com/graphml-lab-pwr/lapeigvals)
- [EigenTrack - arXiv](https://arxiv.org/abs/2509.15735)
- [Spectral Guardrails - arXiv](https://arxiv.org/abs/2602.08082)
- [Frequency-Aware Attention - arXiv](https://arxiv.org/abs/2602.18145)
- [TOHA - arXiv](https://arxiv.org/abs/2504.10063)
- [CHARM - arXiv](https://arxiv.org/abs/2509.24770)
- [SinkProbe - arXiv](https://arxiv.org/abs/2604.10697)
- [Monitoring Decoding - arXiv](https://arxiv.org/abs/2503.03106)
- [PCNet/PC-LDCD - arXiv](https://arxiv.org/abs/2605.05953)
- [HaluGate - vLLM Blog](https://blog.vllm.ai/2025/12/14/halugate.html)
- [HaMI - arXiv](https://arxiv.org/abs/2504.07863)
- [NGS - OpenReview](https://openreview.net/forum?id=yzWGQNTbHQ)
- [First Hallucination Tokens - arXiv](https://arxiv.org/html/2507.20836v4)
- [Semantic Entropy - Nature](https://www.nature.com/articles/s41586-024-07421-0)
- [SEKA - OpenReview](https://openreview.net/pdf/61b1d6aa10b647458c65499b860d5a264e38c178.pdf)
- [Temporal Graph Network - arXiv](https://arxiv.org/abs/2601.03051)
- [Spectral Analysis of Attention Patterns - EmergentMind](https://www.emergentmind.com/topics/spectral-analysis-of-attention-patterns)
- [UQLM - Medium](https://medium.com/cvs-health-tech-blog/detecting-llm-hallucinations-at-generation-time-with-uqlm-cd749d2338ec)
- [Lakera Hallucination Guide](https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18bf0f0a-5782-4d41-bb97-f35bb5717cea",
  "isSidechain": true,
  "agentId": "a91a20d33dc5ad48e",
  "requestId": "req_011Cb4SKR2Y8QZUQNUKWtmvC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a19d52f6-4828-4c32-a77f-c41e1c124dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2e288cf-f020-4acf-bcc2-bbb95af18633",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FmCzg8DcDEPQ56fjnQ94Ak",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 869,
      "cache_creation_input_tokens": 1210,
      "cache_read_input_tokens": 29765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1210,
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
