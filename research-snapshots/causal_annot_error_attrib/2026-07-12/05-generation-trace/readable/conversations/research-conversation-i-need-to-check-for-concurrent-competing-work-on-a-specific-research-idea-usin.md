# Research conversation: I need to check for concurrent/competing work on a specific research idea: using sharpness of the loss landscape (or per

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 1
- **Tool calls:** 35
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aebbb5073ac9d69e3.jsonl`
- **Structured JSON:** [`cc256371375ce3d1b8d5.json`](../../sessions/cc/cc256371375ce3d1b8d5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

81 recorded events

### User

_source line 1 · 2026-05-16T06:07:18.598Z_

I need to check for concurrent/competing work on a specific research idea: using sharpness of the loss landscape (or perturbation-based sensitivity of residual streams/embeddings) to detect "stubborn hallucinations" in LLMs at inference time.

Use WebSearch to perform these searches and report back ALL relevant findings with paper titles, venues, dates, and key differences:

1. Search "sharpness aware hallucination detection LLM 2026"
2. Search "perturbation probing residual stream hallucination 2026"
3. Search "inference time sharpness estimation language model 2026"
4. Search "stubborn hallucination detection 2026"
5. Search arXiv for "embedding perturbation hallucination detection 2025 2026"
6. Search "EPGS hallucination gradient perturbation 2026"
7. Search "logit sensitivity perturbation hallucination abstention 2026"

For each search, report what you found. If you find highly similar concurrent work, describe it in detail. Also check OpenReview for ICML 2026, NeurIPS 2026, ICLR 2026 submissions related to sharpness-based hallucination detection.

Report everything you find — I need to know if someone is already doing this exact thing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "698fa2bf-6c5f-4ca6-9328-80181a69637a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T06:07:18.602Z_

```json
{
  "parentUuid": "698fa2bf-6c5f-4ca6-9328-80181a69637a",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "7ec620c5-ed09-4a9c-b4dc-181abfeb2782",
  "timestamp": "2026-05-16T06:07:18.602Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T06:07:21.823Z_



I'll start by loading the WebSearch tool schema, then run all the searches systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ec620c5-ed09-4a9c-b4dc-181abfeb2782",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kGL97gkt8FjHTXjjfg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d400b6ec-3310-4558-9584-32d8e494484f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CyKHnnfTpCy34bpE36VdLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8133,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8133,
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

_source line 4 · 2026-05-16T06:07:21.924Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TWApNWeVir1bW8A5KCRh3T`</summary>

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
  "parentUuid": "d400b6ec-3310-4558-9584-32d8e494484f",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kGL97gkt8FjHTXjjfg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9686e97-8160-4a4b-8861-81496ae4a332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CyKHnnfTpCy34bpE36VdLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8133,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8133,
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

### Tool result

_source line 5 · 2026-05-16T06:07:21.928Z_

<details><summary>↩ Tool result · `toolu_01TWApNWeVir1bW8A5KCRh3T`</summary>

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
  "parentUuid": "b9686e97-8160-4a4b-8861-81496ae4a332",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "ed52d38b-0a4a-471e-ac59-a951067e3eb7",
  "sourceToolAssistantUUID": "b9686e97-8160-4a4b-8861-81496ae4a332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T06:07:24.440Z_



Now let me run all 7 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed52d38b-0a4a-471e-ac59-a951067e3eb7",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kGaejuxsjRbq6Ef8NU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f073585e-ed44-4cfe-a41a-1867658364bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gith4Lb3H8YmfRrpcgDn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 7 · 2026-05-16T06:07:24.987Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vm8v8HAVwXp4BoUzWDkVKL`</summary>

```json
{
  "query": "sharpness aware hallucination detection LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f073585e-ed44-4cfe-a41a-1867658364bc",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kGaejuxsjRbq6Ef8NU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f26f4c85-2b47-464e-aa5c-e2185e2685fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gith4Lb3H8YmfRrpcgDn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 8 · 2026-05-16T06:07:25.445Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BBm2zPjKtjrmuxFRsKaEwm`</summary>

```json
{
  "query": "perturbation probing residual stream hallucination 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f26f4c85-2b47-464e-aa5c-e2185e2685fe",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kGaejuxsjRbq6Ef8NU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7cfae88-847e-4c1c-bfe7-361443ad5755",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gith4Lb3H8YmfRrpcgDn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 9 · 2026-05-16T06:07:25.961Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TipzYCWk2Vn9vDEMXg3jgK`</summary>

```json
{
  "query": "inference time sharpness estimation language model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7cfae88-847e-4c1c-bfe7-361443ad5755",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kGaejuxsjRbq6Ef8NU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea60f87e-6618-4981-9421-a3b56f87b373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gith4Lb3H8YmfRrpcgDn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 10 · 2026-05-16T06:07:25.965Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C6yxwAFPJrvpkwMzyVBU2c`</summary>

```json
{
  "query": "stubborn hallucination detection 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea60f87e-6618-4981-9421-a3b56f87b373",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kGaejuxsjRbq6Ef8NU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89d102e5-b6c2-4105-8aaf-aef4a291aae7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gith4Lb3H8YmfRrpcgDn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 11 · 2026-05-16T06:07:26.396Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VgJThNp7ZZ1h9UPPLbVViv`</summary>

```json
{
  "query": "arXiv embedding perturbation hallucination detection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89d102e5-b6c2-4105-8aaf-aef4a291aae7",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kGaejuxsjRbq6Ef8NU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b511a55-f7f7-4695-8459-7fc1c06390ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gith4Lb3H8YmfRrpcgDn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 12 · 2026-05-16T06:07:26.847Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0165EJqoMLg2RdMuoQvjpwGu`</summary>

```json
{
  "query": "EPGS hallucination gradient perturbation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b511a55-f7f7-4695-8459-7fc1c06390ab",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kGaejuxsjRbq6Ef8NU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58de7f33-f777-4820-8505-5bf76a1ffc50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gith4Lb3H8YmfRrpcgDn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 13 · 2026-05-16T06:07:26.914Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WBqQoyKBKwnR5GEab1HpeM`</summary>

```json
{
  "query": "logit sensitivity perturbation hallucination abstention 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58de7f33-f777-4820-8505-5bf76a1ffc50",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kGaejuxsjRbq6Ef8NU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5053cacc-3a74-4057-9810-2dabe284dbf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gith4Lb3H8YmfRrpcgDn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 14 · 2026-05-16T06:07:30.605Z_

<details><summary>↩ Tool result · `toolu_01Vm8v8HAVwXp4BoUzWDkVKL`</summary>

```text
Web search results for query: "sharpness aware hallucination detection LLM 2026"

Links: [{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/html/2604.04743"},{"title":"LLM Hallucination Statistics 2026: AI Gets Facts Wrong Up to 82% of the Time","url":"https://sqmagazine.co.uk/llm-hallucination-statistics/"},{"title":"A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3703155"},{"title":"Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments","url":"https://arxiv.org/html/2605.03971v1"},{"title":"Hallucination Detection in LLMs: Methods, Metrics, Benchmarks","url":"https://www.statsig.com/perspectives/hallucination-detection-llms-methods"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"A hallucination detection and mitigation framework for faithful text summarization using LLMs | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-31075-1"}]

Based on the search results, here's what I found about sharpness-aware hallucination detection in LLMs as of 2026:

## Sharpness-Aware Metrics for Hallucination Detection

Sharpness-dependent metrics argue that factual generations inherently correspond to lower entropy and thus more concentrated internal activations. This is a key approach referenced in recent research on hallucination detection.

One notable work in this area is cited as "In-context sharpness as alerts: An inner representation perspective for hallucination mitigation", which was presented at the International Conference on Machine Learning in 2024.

## Current State of Hallucination Detection

INSIDE shows that hidden states remain a predictive signal for hallucination detection, whereas LLM-Check systematically evaluates for probing-based detectors. However, these methods are largely empirical observations; they identify correlations with hallucinations but fail to provide a geometric or a dynamical setup explaining why these signals must exist.

More recent approaches in 2026 are attempting to address these limitations with more theoretical frameworks, such as using dynamical systems perspectives to understand hallucination basins in latent spaces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f26f4c85-2b47-464e-aa5c-e2185e2685fe",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "772b5b45-c65b-4d67-b9ca-ede712f71cae",
  "sourceToolAssistantUUID": "f26f4c85-2b47-464e-aa5c-e2185e2685fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T06:07:31.464Z_

<details><summary>↩ Tool result · `toolu_01TipzYCWk2Vn9vDEMXg3jgK`</summary>

```text
Web search results for query: "inference time sharpness estimation language model 2026"

Links: [{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Categories of Inference-Time Scaling for Improved LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling"},{"title":"Inference-Time Enhancements","url":"https://www.emergentmind.com/topics/inference-time-enhancements"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"Optimizing Language Models for Inference Time Objectives using Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=ZVWJO5YTz4&noteId=YQulYTjpwh"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"Inference-Time Scaling: How Modern AI Models Think Longer to Perform Better | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/inference-time-scaling-how-modern-ai-models-think-longer-to-perform-better-a1e1a8155fbd"},{"title":"Categories of Inference-Time Scaling for Improved LLM Reasoning | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/blog/2026/categories-of-inference-time-scaling.html"},{"title":"Inference-Time Techniques for LLM Reasoning Xinyun Chen","url":"https://rdi.berkeley.edu/adv-llm-agents/slides/inference_time_techniques_lecture_sp25.pdf"},{"title":"Inference-Time Scaling | Introl Blog","url":"https://introl.com/blog/inference-time-scaling-research-reasoning-models-december-2025"}]

Based on the search results, I found relevant information about inference-time scaling for language models in 2026, though the results don't specifically address "sharpness estimation." Here's what the current research landscape shows:

## Inference-Time Scaling in 2026

There is expected to be more focus on inference-time scaling in 2026, which means spending more time and money after training when the LLM generates the answer. Inference-time scaling is an umbrella term for methods that allocate more compute and time during inference to improve model performance.

### Key Development Areas

Recent techniques include Tree-of-Thought and Monte Carlo Tree Search for branching inference, probabilistic compute allocation that adaptively determines minimal samples to meet accuracy goals, and adaptive latency-quality trading with acceptance thresholds and dynamic parameterization.

### Infrastructure Implications

Inference demand is projected to exceed training by 118x in 2026, with inference demand shifting infrastructure planning toward inference-optimized architecture.

**Note:** While the search results provide comprehensive information about inference-time scaling methods for language models in 2026, they do not contain specific information about "sharpness estimation" techniques. If you're looking for information about a particular sharpness estimation method or paper, I would recommend searching with more specific terms or the paper title.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea60f87e-6618-4981-9421-a3b56f87b373",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "5e0b94cd-ff0d-40d3-bbcc-1c866a38cee5",
  "sourceToolAssistantUUID": "ea60f87e-6618-4981-9421-a3b56f87b373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T06:07:32.586Z_

<details><summary>↩ Tool result · `toolu_0165EJqoMLg2RdMuoQvjpwGu`</summary>

```text
Web search results for query: "EPGS hallucination gradient perturbation 2026"

Links: [{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"The Geometry of Hallucination. Gradient Conflict and the Topographic… | by Micheal Bee | Feb, 2026 | Medium","url":"https://medium.com/@mbonsign/the-geometry-of-hallucination-f725f41f7050"},{"title":"How to evaluate LLM hallucination rates in engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/how-to-evaluate-llm-hallucination-rates-in-engineering/"},{"title":"AI Hallucination Rates & Benchmarks in 2026","url":"https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"},{"title":"Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses","url":"https://arxiv.org/html/2407.05474v1"},{"title":"[2601.20279] Hallucination Begins Where Saliency Drops","url":"https://arxiv.org/abs/2601.20279"},{"title":"AI Hallucination Statistics 2026: 50+ Sourced Data Points - Suprmind","url":"https://suprmind.ai/hub/insights/ai-hallucination-statistics-research-report-2026/"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"}]

Based on the search results, here's what I found about EPGS hallucination gradient perturbation in 2026:

## EPGS: Embedding-Perturbed Gradient Sensitivity

EPGS stands for Embedding-Perturbed Gradient Sensitivity, a recent method for detecting hallucinations in large language models.

**How EPGS Works:**

EPGS detects sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude. This acts as an efficient proxy for the Hessian spectrum, differentiating stable knowledge from unstable memorization.

**The Core Insight:**

The hypothesis is that while robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization. Even a minor perturbation in a sharp basin induces a dramatic spike in the gradient magnitude, whereas a flat basin remains stable.

**Performance:**

EPGS significantly outperforms entropy-based and representation-based baselines, providing a robust signal for detecting high-confidence factual errors.

The research appears to have been published in May 2026 (the paper was released about 2 weeks ago according to the search results), representing a novel geometric approach to understanding and detecting hallucinations in LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58de7f33-f777-4820-8505-5bf76a1ffc50",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "087c99dc-c791-48e7-8da2-3c04ed9210ab",
  "sourceToolAssistantUUID": "58de7f33-f777-4820-8505-5bf76a1ffc50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T06:07:32.602Z_

<details><summary>↩ Tool result · `toolu_01BBm2zPjKtjrmuxFRsKaEwm`</summary>

```text
Web search results for query: "perturbation probing residual stream hallucination 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.20026"},{"title":"Cross-Layer Attention Probing for Fine-Grained Hallucination Detection","url":"https://arxiv.org/html/2509.09700v1/"},{"title":"[2601.02170] Streaming Hallucination Detection in Long Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2601.02170"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689v4"},{"title":"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2601.02170v1"},{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"Mitigating Hallucinations in Large Vision-Language Models via Dual Contrastive Decoding | Proceedings of the 7th ACM International Conference on Multimedia in Asia","url":"https://dl.acm.org/doi/10.1145/3743093.3770933"},{"title":"Self-Consistency and Probe-Based Hallucination Detection","url":"https://www.emergentmind.com/topics/self-consistency-probe-based-hallucination-detection"},{"title":"From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs","url":"https://www.mdpi.com/2673-2688/6/10/260"},{"title":"A Single Direction of Truth: An Observer Model’s Linear Residual Probe Exposes and Steers Contextual Hallucinations","url":"https://arxiv.org/html/2507.23221v1"}]

I found several relevant research papers on this topic. Here's what the search results show:

## Key Findings

The search results reveal several recent approaches combining perturbation, probing, residual stream analysis, and hallucination detection:

**Cross-Layer Attention Probing (CLAP):** A novel probing technique that consists of an attention mechanism operating on the LLM residual stream is proposed for improving hallucination detection. Leveraging responses in the sampled space at train time helps CLAP achieve fine-grained detection between hallucinated and non-hallucinated responses to the same prompt at test time.

**Perturbation-Driven Approach (SHINE):** A novel hallucination probing method is driven by the discovery that perturbing key entities in prompts affects LLM's generation of different types of text differently. The method is effective in hallucination probing and achieves state-of-the-art performance in hallucination detection across four datasets and four LLMs.

**Linear Residual Stream Probing:** A generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream. The consistent mid-layer plateau across observer models supports the hypothesis that contextual hallucinations are encoded along a common linear direction in activation space.

**Next-Token Gradient Sensitivity:** A gradient-based paradigm for hallucination detection probes next-token prediction sensitivity through a statistic called Next-token Gradient Sensitivity (NGS), which quantifies the first-order gradient of the maximum log-probability of the next token with respect to the current token's layer embedding, measuring local prediction fragility.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7cfae88-847e-4c1c-bfe7-361443ad5755",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "0c4d3375-efb8-4656-84f1-7e177f1f5cb3",
  "sourceToolAssistantUUID": "b7cfae88-847e-4c1c-bfe7-361443ad5755",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T06:07:34.549Z_

<details><summary>↩ Tool result · `toolu_01WBqQoyKBKwnR5GEab1HpeM`</summary>

```text
Web search results for query: "logit sensitivity perturbation hallucination abstention 2026"

Links: [{"title":"Hallucinate Less by Thinking More: Aspect-Based Causal Abstention","url":"https://arxiv.org/pdf/2511.17170"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"Evaluating large language models for accuracy incentivizes hallucinations | Nature","url":"https://www.nature.com/articles/s41586-026-10549-w"},{"title":"Hallucination in LLMs: Predictable Compression Failures","url":"https://www.emergentmind.com/papers/2509.11208"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.20026"},{"title":"From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs","url":"https://www.mdpi.com/2673-2688/6/10/260"},{"title":"Theoretical Foundations and Mitigation of Hallucination in ...","url":"https://www.arxiv.org/pdf/2507.22915"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"Why Language Models Hallucinate Adam Tauman Kalai∗ OpenAI Ofir Nachum OpenAI","url":"https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf"}]

I found several relevant research papers and resources related to your search query on logit sensitivity, perturbation, hallucination, and abstention. Here are the key findings:

## Recent Research Findings (2026)

Semantic entropy itself is not a reliable measure for identifying hallucinations because token sequence probabilities can be highly sensitive to model perturbations, warranting adjustments to confidence assessments of hallucinatory behavior.

Recent work introduces a quantum tensor network-based Hamiltonian approach for uncertainty quantification, leveraging perturbation theory to generate multi-resolution, local uncertainty estimates suited for hallucination detection.

## Perturbation-Based Methods

Perturbation-based methods explore input sensitivity, with examples like those studying how model predictions vary with input modifications.

Research links hallucinations to shifts in attention weights, where input perturbations can steer models toward specific outputs.

## Abstention and Hallucination Mitigation

Conformal prediction techniques can develop abstention procedures with theoretical guarantees on hallucination rates, reliably bounding hallucination rates while maintaining less conservative abstention rates compared to baselines using log-probability scores.

New reward schemes encourage abstention when evidence is thin, with confidence calibration being integrated into reinforcement learning to penalize both over- and underconfidence.

## Logit-Based Approaches

A practical regularizer has been proposed to minimize positional penalties by regularizing the squared differences between logits across different permutations.

The research indicates that understanding how models respond to perturbations—particularly in their logit outputs—is becoming increasingly important for both detecting and mitigating hallucinations through principled abstention mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5053cacc-3a74-4057-9810-2dabe284dbf7",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "18d7b73c-96cf-45d1-baa4-ac61d921a65b",
  "sourceToolAssistantUUID": "5053cacc-3a74-4057-9810-2dabe284dbf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T06:07:35.416Z_

<details><summary>↩ Tool result · `toolu_01C6yxwAFPJrvpkwMzyVBU2c`</summary>

```text
Web search results for query: "stubborn hallucination detection 2026"

Links: [{"title":"LLM Hallucination Statistics 2026: AI Gets Facts Wrong Up to 82% of the Time","url":"https://sqmagazine.co.uk/llm-hallucination-statistics/"},{"title":"🚨 AI Hallucinations Are Getting Smarter — Here’s How to Catch Them in Real-Time (Even in Agentic AI Systems, 2026) | by Yash Mishra | Feb, 2026 | Medium","url":"https://medium.com/@yash.mishra0501/ai-hallucinations-are-getting-smarter-heres-how-to-catch-them-in-real-time-even-in-agentic-3d75a9fc1ab3"},{"title":"GPTZero uncovers 50+ Hallucinations in ICLR 2026","url":"https://gptzero.me/news/iclr-2026/"},{"title":"AI Hallucination: Compare top LLMs like GPT-5.2","url":"https://aimultiple.com/ai-hallucination"},{"title":"Detecting hallucinations in large language models using semantic entropy | Nature","url":"https://www.nature.com/articles/s41586-024-07421-0"},{"title":"Hallucination Detection in Foundation Models for Decision-Making: A Flexible Definition and Review of the State of the Art | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3716846"},{"title":"AI Hallucination Rates & Benchmarks in 2026","url":"https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"},{"title":"A hallucination detection and mitigation framework for faithful text summarization using LLMs | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-31075-1"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"hallucination-detection · GitHub Topics · GitHub","url":"https://github.com/topics/hallucination-detection"}]

Based on the web search results, here's what I found about stubborn hallucination detection in 2026:

## Current State of Hallucination Detection

Automated detection tools identify hallucinations with ~85%–92% accuracy in benchmark datasets. However, hallucinations remain a persistent challenge for AI systems in 2026, with a 2026 benchmark across 37 models reporting hallucination rates between 15% and 52%.

## Why Hallucinations Are "Stubborn"

The challenge of detecting hallucinations is particularly acute because as agentic AI goes mainstream — LLM-powered agents that can plan, call tools, and take actions — hallucinations stop being "just text errors" and become system‑level failures: wrong plans, wrong API calls, wrong business actions. Additionally, some newer reasoning models show higher hallucination rates than earlier versions, indicating trade-offs between reasoning depth and accuracy.

## Detection Approaches in 2026

Several strategies have emerged to tackle stubborn hallucinations:

- Techniques such as Cross-Layer Attention Probing (CLAP) train lightweight classifiers on the model's own activations to flag likely hallucinations in real time. The MetaQA framework (ACM 2025) goes a step further: it uses metamorphic prompt mutations to detect hallucinations even in closed-source models without relying on token probabilities or external tools.

- With a layered approach — RAG, probes, LLM‑as‑judge, agentic guardrails, and continuous evaluation — you can drive effective hallucination rates to well under 1% in many real‑world workflows.

- The 2025 consensus is to aim for calibrated uncertainty: systems that transparently signal doubt and can safely refuse to answer when unsure, rather than chasing an unrealistic "zero error" goal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89d102e5-b6c2-4105-8aaf-aef4a291aae7",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "967c23a9-6ed5-47ea-b400-4547d7e6b3e7",
  "sourceToolAssistantUUID": "89d102e5-b6c2-4105-8aaf-aef4a291aae7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T06:07:39.258Z_

<details><summary>↩ Tool result · `toolu_01VgJThNp7ZZ1h9UPPLbVViv`</summary>

```text
Web search results for query: "arXiv embedding perturbation hallucination detection 2025 2026"

Links: [{"title":"VideoHEDGE: Entropy-Based Hallucination Detection for Video-VLMs via Semantic Clustering and Spatiotemporal Perturbations","url":"https://arxiv.org/html/2601.08557"},{"title":"A Graph Signal Processing Framework for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2510.19117"},{"title":"[2512.15068] The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems","url":"https://arxiv.org/abs/2512.15068"},{"title":"[2502.08663] Hallucination Detection: A Probabilistic Framework Using Embeddings Distance Analysis","url":"https://arxiv.org/abs/2502.08663"},{"title":"[2603.22812v1] Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration","url":"https://arxiv.org/abs/2603.22812v1"},{"title":"The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems","url":"https://arxiv.org/html/2512.15068v2"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.20026"},{"title":"Hallucination Detection: A Probabilistic Framework Using Embeddings Distance Analysis","url":"https://arxiv.org/html/2502.08663v1"},{"title":"Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/html/2510.06265v3"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"}]

Based on the search results, here are several recent arXiv papers on embedding perturbation and hallucination detection from 2025-2026:

## Key Recent Papers

### 1. **VideoHEDGE** (January 2026)
VideoHEDGE is a modular framework for hallucination detection in video question answering that generalizes entropy-based reliability estimation from images to temporally structured inputs. The framework treats perturbations as controlled probes of visual robustness by contrasting semantic distributions induced by clean versus degraded videos to detect answers whose validity depends on fragile or spurious visual cues.

### 2. **Graph Signal Processing Framework** (October 2025)
This work proposes a spectral analysis framework that models transformer layers as dynamic graphs induced by attention, with token embeddings as signals on these graphs, and defines diagnostics including Dirichlet energy, spectral entropy, and high-frequency energy ratios with theoretical connections to computational stability.

### 3. **Semantic Illusion in RAG Systems** (December 2025)
This paper applies conformal prediction to RAG hallucination detection, demonstrating that on synthetic hallucinations, embedding methods achieve 95% coverage with 0% False Positive Rate, but on real hallucinations from RLHF-aligned models, the same methods fail catastrophically, yielding 100% FPR at target coverage.

### 4. **Probabilistic Framework Using Embeddings Distance Analysis** (February 2025)
This paper introduces a mathematically sound methodology for hallucination detection and shows that hallucinated content has structural differences with respect to correct content, using Minkowski distances in the embedding space.

### 5. **Efficient Hallucination Detection with Bayesian Framework** (March 2026)
This work proposes an Adaptive Bayesian Estimation framework for Semantic Entropy with Guided Semantic Exploration, which dynamically adjusts sampling requirements based on observed uncertainty and develops a perturbation-based importance sampling strategy to systematically explore the semantic space.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b511a55-f7f7-4695-8459-7fc1c06390ab",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "ca2b411b-1388-4886-a302-7a64a380d158",
  "sourceToolAssistantUUID": "7b511a55-f7f7-4695-8459-7fc1c06390ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T06:07:46.747Z_

This is very significant. Search 6 returned a direct hit -- a paper that appears to be extremely close to your research idea. Let me dig deeper into this paper and the other closely related works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca2b411b-1388-4886-a302-7a64a380d158",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kHrPp9TbKLpCtM6rZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "414ed202-c3f7-4a23-9be4-cd2e937e3b1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TCj5xRZ7fhwuNiLhnLBw8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1793,
      "cache_creation_input_tokens": 5183,
      "cache_read_input_tokens": 9546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5183,
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

_source line 22 · 2026-05-16T06:07:47.232Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M3RysDU67kRu7xSkdyzhGn`</summary>

```json
{
  "query": "arxiv 2605.00939 \"From Flat Facts to Sharp Hallucinations\" gradient sensitivity EPGS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "414ed202-c3f7-4a23-9be4-cd2e937e3b1c",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kHrPp9TbKLpCtM6rZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f41f361e-f303-49b9-9a5f-32648a53d909",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TCj5xRZ7fhwuNiLhnLBw8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1793,
      "cache_creation_input_tokens": 5183,
      "cache_read_input_tokens": 9546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5183,
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

_source line 23 · 2026-05-16T06:07:47.694Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015wSffg3ZmFzW3yxYMa6PoA`</summary>

```json
{
  "query": "\"Next-Token Gradient Sensitivity\" NGS hallucination detection OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f41f361e-f303-49b9-9a5f-32648a53d909",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kHrPp9TbKLpCtM6rZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2562b21-5f52-4fe9-9f18-4645ff8849b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TCj5xRZ7fhwuNiLhnLBw8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1793,
      "cache_creation_input_tokens": 5183,
      "cache_read_input_tokens": 9546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5183,
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

_source line 24 · 2026-05-16T06:07:48.175Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015BMhfiKoutg3xHtqGMDZvz`</summary>

```json
{
  "query": "\"Hallucination Begins Where Saliency Drops\" arxiv 2601.20279"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2562b21-5f52-4fe9-9f18-4645ff8849b0",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kHrPp9TbKLpCtM6rZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdc2cce6-8a11-47e1-a0e1-6246a445328e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TCj5xRZ7fhwuNiLhnLBw8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1793,
      "cache_creation_input_tokens": 5183,
      "cache_read_input_tokens": 9546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5183,
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

_source line 25 · 2026-05-16T06:07:49.137Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J3uTmiTm1K7kMDnJWUq6Uw`</summary>

```json
{
  "query": "\"Hallucination Basins\" dynamic framework arxiv 2604.04743"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdc2cce6-8a11-47e1-a0e1-6246a445328e",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kHrPp9TbKLpCtM6rZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93055729-a4d7-4a56-b3ba-9fb67300e0ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TCj5xRZ7fhwuNiLhnLBw8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1793,
      "cache_creation_input_tokens": 5183,
      "cache_read_input_tokens": 9546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5183,
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

_source line 26 · 2026-05-16T06:07:49.474Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DwEt9fjijWCrdGEDGGqmcn`</summary>

```json
{
  "query": "\"Shaking to Reveal\" perturbation detection LLM hallucinations arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93055729-a4d7-4a56-b3ba-9fb67300e0ab",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kHrPp9TbKLpCtM6rZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08296839-7fe1-4b0e-a310-c8625df62d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TCj5xRZ7fhwuNiLhnLBw8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1793,
      "cache_creation_input_tokens": 5183,
      "cache_read_input_tokens": 9546,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5183
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1793,
          "output_tokens": 335,
          "cache_read_input_tokens": 9546,
          "cache_creation_input_tokens": 5183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5183,
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

_source line 27 · 2026-05-16T06:07:52.899Z_

<details><summary>↩ Tool result · `toolu_015wSffg3ZmFzW3yxYMa6PoA`</summary>

```text
Web search results for query: ""Next-Token Gradient Sensitivity" NGS hallucination detection OpenReview"

Links: [{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"LLM-Check: Investigating Detection of Hallucinations in Large Language Models","url":"https://openreview.net/pdf?id=LYx4w3CAgy"},{"title":"Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding | OpenReview","url":"https://openreview.net/forum?id=5fCDEz43ya"},{"title":"Detection and Mitigation of Hallucination in Large ...","url":"https://openreview.net/pdf?id=PTbH6uKwhm"},{"title":"A Taxonomic Survey of Hallucination Mitigation ...","url":"https://www.preprints.org/frontend/manuscript/c5286594616981962a5a361fb2f51efc/download_pub"},{"title":"From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs","url":"https://www.mdpi.com/2673-2688/6/10/260"},{"title":"Openreview","url":"https://openreview.net/pdf?id=4twbqwV4br"},{"title":"NeurIPS 2025 Schedule","url":"https://neurips.cc/virtual/2025/loc/san-diego/calendar?filter_events=Affinity+Poster+Session%2CAffinity+Workshop&filter_rooms="},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"What do Geometric Hallucination Detection Metrics Actually Measure? | OpenReview","url":"https://openreview.net/forum?id=OAb3kzatIV"}]

I found a direct match for your search query. Here's what I found:

## Next-Token Gradient Sensitivity (NGS) for Hallucination Detection

Next-token Gradient Sensitivity (NGS) is a statistic that quantifies the first-order gradient of the maximum log-probability of the next token with respect to the current token's layer embedding, measuring local prediction fragility.

The approach proposes a gradient-based paradigm for hallucination detection by probing next-token prediction sensitivity, and develops NGS-based Hallucination Detection (NGS-HD), a method that reframes detection as a token-level distribution comparison task. The norm of NGS bounds the prediction confidence changes under small perturbations.

This research was published on OpenReview in October 2025 and addresses the challenge that while large language models demonstrate remarkable text generation capabilities, they often produce hallucinations—factually inaccurate or unfaithful content—which remains challenging to detect due to their commonly subtle and localized nature.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2562b21-5f52-4fe9-9f18-4645ff8849b0",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "8a4c39f4-2698-4f83-a898-7bccfb83caca",
  "sourceToolAssistantUUID": "c2562b21-5f52-4fe9-9f18-4645ff8849b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T06:07:52.994Z_

<details><summary>↩ Tool result · `toolu_01M3RysDU67kRu7xSkdyzhGn`</summary>

```text
Web search results for query: "arxiv 2605.00939 "From Flat Facts to Sharp Hallucinations" gradient sensitivity EPGS"

Links: [{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"Laplacian Score Sharpening for Mitigating Hallucination in Diffusion Models","url":"https://arxiv.org/html/2511.07496v1"},{"title":"[2605.01428] Hallucinations Undermine Trust; Metacognition is a Way Forward","url":"https://arxiv.org/abs/2605.01428"},{"title":"On Hallucinations in Inverse Problems: Fundamental Limits and Provable Assessment Methods The authors gratefully acknowledge the Gauss Centre for Supercomputing e.V. (www.gauss-centre.eu) for funding this project by providing computing time through the John von Neumann Institute for Computing (NIC) on the GCS Supercomputer. D.I was supported by a PhD fellowship from the Deutsches Zentrum für Luft und Raumfahrt (DLR). N.M.G. acknowledges research sponsored by the Laboratory Directed Research and Development","url":"https://arxiv.org/html/2605.13146"},{"title":"Nested Sensitivity Envelopes for Transported Quantile Treatment Effects","url":"https://arxiv.org/html/2605.09264"},{"title":"Hallucination Score: Towards Mitigating Hallucinations in Generative Image Super-Resolution","url":"https://arxiv.org/html/2507.14367"},{"title":"From Hallucinations to Facts: Enhancing Language Models with Curated Knowledge Graphs","url":"https://arxiv.org/html/2412.18672"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v1"},{"title":"[2507.14367] Hallucination Score: Towards Mitigating Hallucinations in Generative Image Super-Resolution","url":"https://arxiv.org/abs/2507.14367"}]

Based on the search results, I found the arXiv paper 2605.00939. Here's what the paper is about:

**Title:** From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity

**Main Contribution:** The paper proposes a geometric solution called Embedding-Perturbed Gradient Sensitivity (EPGS).

**Core Hypothesis:** The authors hypothesize that while robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization.

**How EPGS Works:** EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude. This acts as an efficient proxy for the Hessian spectrum, differentiating stable knowledge from unstable memorization.

**Results:** The experiments show that EPGS significantly outperforms entropy-based and representation-based baselines, providing a robust signal for detecting high-confidence factual errors.

The paper addresses the problem of detecting "stubborn hallucinations"—errors where LLMs are confidently wrong—by using gradient sensitivity under embedding perturbation as a geometric indicator of the model's belief stability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f41f361e-f303-49b9-9a5f-32648a53d909",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "85a7b6c2-894f-4daf-b85e-727224da3ea2",
  "sourceToolAssistantUUID": "f41f361e-f303-49b9-9a5f-32648a53d909",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T06:07:56.182Z_

<details><summary>↩ Tool result · `toolu_01J3uTmiTm1K7kMDnJWUq6Uw`</summary>

```text
Web search results for query: ""Hallucination Basins" dynamic framework arxiv 2604.04743"

Links: [{"title":"[2604.04743] Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/abs/2604.04743"},{"title":"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/html/2604.04743v1"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"[2604.17982] Mitigating Multimodal Hallucination via Phase-wise Self-reward","url":"https://arxiv.org/abs/2604.17982"},{"title":"[2604.15400] Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/abs/2604.15400"},{"title":"Mitigating Multimodal Hallucination via Phase-wise Self-reward","url":"https://arxiv.org/html/2604.17982"},{"title":"[2604.16430] HalluSAE: Detecting Hallucinations in Large Language Models via Sparse Auto-Encoders","url":"https://arxiv.org/abs/2604.16430"},{"title":"Hallucination, Abstention, and Recursive Inseparability","url":"https://arxiv.org/html/2604.28067v1"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"Hallucination Detection in Foundation Models for Decision-Making: A Flexible Definition and Review of the State of the Art","url":"https://arxiv.org/html/2403.16527v1"}]

I found the paper! Here are the key details about "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations":

**Paper Information:**
- **arXiv ID:** 2604.04743
- **Authors:** Kalyan Cherukuri and Lav R. Varshney
- **Submission Date:** April 6, 2026

**Core Concept:**

The paper presents a geometric dynamical systems framework in which hallucinations arise from task-dependent basin structure in latent space.

**Key Findings:**

Using autoregressive hidden-state trajectories across multiple open-source models and benchmarks, the researchers find that separability is strongly task-dependent rather than universal: factoid settings can show clearer basin separation, whereas summarization and misconception-heavy settings are typically less stable and often overlap.

**Theoretical and Practical Contributions:**

The paper formalizes this behavior with task-complexity and multi-basin theorems, characterizes basin emergence in L-layer transformers, and shows that geometry-aware steering can reduce hallucination probability without retraining.

This work provides a novel geometric perspective on how language model hallucinations emerge from the structure of latent space basins, with implications for understanding and controlling hallucination behavior across different task types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93055729-a4d7-4a56-b3ba-9fb67300e0ab",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "68600c21-108a-41f2-8df9-0229419c0837",
  "sourceToolAssistantUUID": "93055729-a4d7-4a56-b3ba-9fb67300e0ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T06:07:56.627Z_

<details><summary>↩ Tool result · `toolu_01DwEt9fjijWCrdGEDGGqmcn`</summary>

```text
Web search results for query: ""Shaking to Reveal" perturbation detection LLM hallucinations arxiv"

Links: [{"title":"[2506.02696] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696"},{"title":"[2506.02696v1] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://www.researchgate.net/publication/392371301_Shaking_to_Reveal_Perturbation-Based_Detection_of_LLM_Hallucinations"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/pdf/2506.02696"},{"title":"[Literature Review] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://www.themoonlight.io/en/review/shaking-to-reveal-perturbation-based-detection-of-llm-hallucinations"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://www.alphaxiv.org/overview/2506.02696v1"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689v4"},{"title":"Trust Me, I’m Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/html/2502.12964"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://seongheon-96.github.io/assets/pdf/shaking.pdf"}]

I found the paper you're looking for! Here's what I found about "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations":

## Overview

Hallucination remains a key obstacle to the reliable deployment of large language models (LLMs) in real-world question answering tasks. A widely adopted strategy to detect hallucination, known as self-assessment, relies on the model's own output confidence to estimate the factual accuracy of its answers.

## The Problem

This strategy assumes that the model's output distribution closely reflects the true data distribution, which may not always hold in practice. As bias accumulates through the model's layers, the final output can diverge from the underlying reasoning process, making output-level confidence an unreliable signal for hallucination detection.

## The Solution: Sample-Specific Prompting (SSP)

The authors propose Sample-Specific Prompting (SSP), a new framework that improves self-assessment by analyzing perturbation sensitivity at intermediate representations. These representations, being less influenced by model bias, offer a more faithful view of the model's latent reasoning process.

Specifically, SSP dynamically generates noise prompts for each input and employs a lightweight encoder to amplify the changes in representations caused by the perturbation. A contrastive distance metric is then used to quantify these differences and separate truthful from hallucinated responses.

## Results

The method improves hallucination detection accuracy by 4.78% (AUROC) on a challenging TruthfulQA benchmark.

The paper was published on arXiv on June 3, 2025 (arxiv:2506.02696).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08296839-7fe1-4b0e-a310-c8625df62d7f",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "ec0a3841-1c44-4039-88fb-d7a73a297958",
  "sourceToolAssistantUUID": "08296839-7fe1-4b0e-a310-c8625df62d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T06:08:03.584Z_

<details><summary>↩ Tool result · `toolu_015BMhfiKoutg3xHtqGMDZvz`</summary>

```text
Web search results for query: ""Hallucination Begins Where Saliency Drops" arxiv 2601.20279"

Links: [{"title":"[2601.20279] Hallucination Begins Where Saliency Drops","url":"https://arxiv.org/abs/2601.20279"},{"title":"(PDF) Hallucination Begins Where Saliency Drops","url":"https://www.researchgate.net/publication/400178035_Hallucination_Begins_Where_Saliency_Drops"},{"title":"Computer Vision and Pattern Recognition Papers on X: \"Hallucination Begins Where Saliency Drops Xiaofeng Zhang, Yuanchao Zhu, Chaochen Gu, Xiaosong Yuan, Qiyan Zhao, Jiawei Cao, Feilong Tang, Sinan Fan, Yaomin Shen, Chen Shen, Hao Tang https://t.co/jWDrwdHFMe [𝚌𝚜.𝙲𝚅] https://t.co/eVlTkUT8GA\" / X","url":"https://x.com/CSVisionPapers/status/2017001728214778308"},{"title":"幻觉始于显著性下降之处 | alphaXiv","url":"https://www.alphaxiv.org/zh/overview/2601.20279v1"},{"title":"Hallucination Begins Where Saliency Drops | OpenReview","url":"https://openreview.net/forum?id=sjnErRHXf3"},{"title":"HALLUCINATION BEGINS WHERE SALIENCY DROPS","url":"https://openreview.net/pdf/5855c7ef79b8119b12f2a8950ea13499d47669d8.pdf"},{"title":"[Literature Review] Hallucination Begins Where Saliency ...","url":"https://www.themoonlight.io/review/hallucination-begins-where-saliency-drops"},{"title":"attention-mechanisms","url":"https://www.alphaxiv.org/?custom-categories=attention-mechanisms"},{"title":"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2601.02170v1"},{"title":"Towards Understanding Text Hallucination of Diffusion Models via Local Generation Bias","url":"https://arxiv.org/html/2503.03595v1"}]

I found the paper for you. Here's what I found about "Hallucination Begins Where Saliency Drops" (arxiv 2601.20279):

## Overview

Recent studies have examined attention dynamics in large vision-language models (LVLMs) to detect hallucinations. However, existing approaches remain limited in reliably distinguishing hallucinated from factually grounded outputs, as they rely solely on forward-pass attention patterns and neglect gradient-based signals that reveal how token influence propagates through the network.

## Key Contribution

The paper introduces LVLMs-Saliency, a gradient-aware diagnostic framework that quantifies the visual grounding strength of each output token by fusing attention weights with their input gradients.

## Main Finding

The analysis uncovers a decisive pattern: hallucinations frequently arise when preceding output tokens exhibit low saliency toward the prediction of the next token, signaling a breakdown in contextual memory retention.

## Proposed Solution

The paper proposes a dual-mechanism inference-time framework: (1) Saliency-Guided Rejection Sampling (SGRS), which dynamically filters candidate tokens during autoregressive decoding by rejecting those whose saliency falls below a context-adaptive threshold, thereby preventing coherence-breaking tokens from entering the output sequence; and (2) Local Coherence Reinforcement (LocoRE), a lightweight, plug-and-play module that strengthens attention from the current token to its most recent predecessors, actively counteracting the contextual forgetting behavior identified by LVLMs-Saliency.

The paper was published as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdc2cce6-8a11-47e1-a0e1-6246a445328e",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "cd7ac797-c960-4a23-b5d9-a2752dee16d8",
  "sourceToolAssistantUUID": "fdc2cce6-8a11-47e1-a0e1-6246a445328e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-16T06:08:07.297Z_

The EPGS paper is a critical find. Let me now get more details on it and check the conference submission venues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd7ac797-c960-4a23-b5d9-a2752dee16d8",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kKeRHian96CCR3ZwVY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ae71f76-0447-438d-9ab1-71ccbf52df05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQkZSL5UwVQ1kHg5UEFwXm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1798,
      "cache_creation_input_tokens": 4837,
      "cache_read_input_tokens": 14729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4837,
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

_source line 33 · 2026-05-16T06:08:08.496Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WLvW6A4p4FEWcKgDukm7gH`</summary>

```json
{
  "query": "arxiv 2605.00939 \"From Flat Facts to Sharp Hallucinations\" authors EPGS embedding perturbed gradient sensitivity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ae71f76-0447-438d-9ab1-71ccbf52df05",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kKeRHian96CCR3ZwVY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9af240c-6b0b-4bb9-9440-ec0d3bf1766f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQkZSL5UwVQ1kHg5UEFwXm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1798,
      "cache_creation_input_tokens": 4837,
      "cache_read_input_tokens": 14729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4837,
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

_source line 34 · 2026-05-16T06:08:08.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MFirAPJPHo2ED3QqpgXCp1`</summary>

```json
{
  "query": "OpenReview ICML 2026 sharpness hallucination detection gradient sensitivity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9af240c-6b0b-4bb9-9440-ec0d3bf1766f",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kKeRHian96CCR3ZwVY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e231673d-c5f8-4b46-85a1-1d3d30901dd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQkZSL5UwVQ1kHg5UEFwXm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1798,
      "cache_creation_input_tokens": 4837,
      "cache_read_input_tokens": 14729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4837,
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

_source line 35 · 2026-05-16T06:08:09.596Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013q8MazXmCTXnX1AqaGZMti`</summary>

```json
{
  "query": "OpenReview NeurIPS 2026 embedding perturbation hallucination sharpness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e231673d-c5f8-4b46-85a1-1d3d30901dd4",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kKeRHian96CCR3ZwVY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ceba3e60-25b9-480a-b5bf-8132d3832a74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQkZSL5UwVQ1kHg5UEFwXm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1798,
      "cache_creation_input_tokens": 4837,
      "cache_read_input_tokens": 14729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4837,
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

_source line 36 · 2026-05-16T06:08:10.065Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012NcrCPtL7JB3Uuv6i7YMdK`</summary>

```json
{
  "query": "OpenReview ICLR 2026 sharpness hallucination detection perturbation gradient"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceba3e60-25b9-480a-b5bf-8132d3832a74",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kKeRHian96CCR3ZwVY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "250672fe-025e-4444-acf9-11c9cd05c136",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQkZSL5UwVQ1kHg5UEFwXm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1798,
      "cache_creation_input_tokens": 4837,
      "cache_read_input_tokens": 14729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4837,
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

_source line 37 · 2026-05-16T06:08:10.350Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014TCFDUaJF17q5tWTesbBxH`</summary>

```json
{
  "query": "\"SHINE\" hallucination probing perturbation entities arxiv 2411.09689"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "250672fe-025e-4444-acf9-11c9cd05c136",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kKeRHian96CCR3ZwVY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a4f1553-61a1-4ce3-8b17-7c12e1497d31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQkZSL5UwVQ1kHg5UEFwXm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1798,
      "cache_creation_input_tokens": 4837,
      "cache_read_input_tokens": 14729,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4837
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1798,
          "output_tokens": 327,
          "cache_read_input_tokens": 14729,
          "cache_creation_input_tokens": 4837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4837,
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

_source line 38 · 2026-05-16T06:08:14.663Z_

<details><summary>↩ Tool result · `toolu_01WLvW6A4p4FEWcKgDukm7gH`</summary>

```text
Web search results for query: "arxiv 2605.00939 "From Flat Facts to Sharp Hallucinations" authors EPGS embedding perturbed gradient sensitivity"

Links: [{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"From Hallucinations to Facts: Enhancing Language Models with Curated Knowledge Graphs","url":"https://arxiv.org/html/2412.18672v1"},{"title":"[2605.01428] Hallucinations Undermine Trust; Metacognition is a Way Forward","url":"https://arxiv.org/abs/2605.01428"},{"title":"[2605.07723] LLM hallucinations in the wild: Large-scale evidence from non-existent citations","url":"https://arxiv.org/abs/2605.07723"},{"title":"[2605.07723v1] LLM hallucinations in the wild: Large-scale evidence from non-existent citations","url":"https://arxiv.org/abs/2605.07723v1"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"[2605.13146] On Hallucinations in Inverse Problems: Fundamental Limits and Provable Assessment Methods","url":"https://arxiv.org/abs/2605.13146"},{"title":"From Hallucinations to Facts: Enhancing Language Models with Curated","url":"https://arxiv.org/pdf/2412.18672"},{"title":"On Hallucinations in Inverse Problems: Fundamental Limits and Provable Assessment Methods The authors gratefully acknowledge the Gauss Centre for Supercomputing e.V. (www.gauss-centre.eu) for funding this project by providing computing time through the John von Neumann Institute for Computing (NIC) on the GCS Supercomputer. D.I was supported by a PhD fellowship from the Deutsches Zentrum für Luft und Raumfahrt (DLR). N.M.G. acknowledges research sponsored by the Laboratory Directed Research and Development","url":"https://arxiv.org/html/2605.13146"}]

Based on the search results, I found the paper you're looking for:

**Title:** From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity

**ArXiv ID:** 2605.00939

**Authors:** Yee Zhing Liew, Andrew Huey Ping Tan, and Anwar P.P Abdul Majeed

**Key Contribution:** The paper proposes Embedding-Perturbed Gradient Sensitivity (EPGS), a geometric solution for detecting hallucinations.

**Main Hypothesis:** The authors hypothesize that while robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization.

**Method:** EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude, acting as an efficient proxy for the Hessian spectrum to differentiate stable knowledge from unstable memorization.

The paper was submitted on May 1, 2026, and addresses the problem of detecting "stubborn hallucinations" where large language models are confidently wrong.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9af240c-6b0b-4bb9-9440-ec0d3bf1766f",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "66c8d059-d6af-48e0-97c6-64aae1c8c0de",
  "sourceToolAssistantUUID": "d9af240c-6b0b-4bb9-9440-ec0d3bf1766f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-16T06:08:15.381Z_

<details><summary>↩ Tool result · `toolu_012NcrCPtL7JB3Uuv6i7YMdK`</summary>

```text
Web search results for query: "OpenReview ICLR 2026 sharpness hallucination detection perturbation gradient"

Links: [{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"HALLUCINATION MITIGATION IN LARGE VISION","url":"https://openreview.net/pdf?id=Km4l2Fi2lc"},{"title":"ICLR 2026 Conference Submissions","url":"https://openreview.net/submissions?page=123&venue=ICLR.cc/2026/Conference"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"},{"title":"GPTZero uncovers 50+ Hallucinations in ICLR 2026","url":"https://gptzero.me/news/iclr-2026/"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"HADEMIF: HALLUCINATION DETECTION AND MITI","url":"https://openreview.net/pdf?id=VwOYxPScxB"},{"title":"Under review as a conference paper at ICLR 2023","url":"https://openreview.net/pdf?id=EW00yKKLiX"},{"title":"Exposing Hallucinations To Suppress Them: VLMs Representation Editing With Generative Anchors | OpenReview","url":"https://openreview.net/forum?id=cBhqgPtEqw"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"}]

Based on the web search results, I found several relevant papers from OpenReview related to hallucination detection at ICLR 2026:

## Key Findings

**Next-Token Gradient Sensitivity for Hallucination Detection:**

The paper proposes a gradient-based paradigm for hallucination detection by probing next-token prediction sensitivity, introducing a statistic called Next-token Gradient Sensitivity (NGS), which quantifies the first-order gradient of the maximum log-probability of the next token with respect to the current token's layer embedding, measuring local prediction fragility. The work proves that its norm bounds the prediction confidence changes under small perturbations.

**Other Hallucination Detection Approaches:**

The search also revealed several other relevant papers:
- A framework called HADEMIF that comprehensively captures hallucinations within both the output and internal spaces of LLMs through two compact networks and achieves prediction calibration based on the network outputs.
- An approach that introduces a novel hallucination amplification mechanism where a caption is projected into the visual space via a text-to-image model to reveal implicit hallucination signals, serving as a negative anchor.

These papers collectively explore gradient-based approaches, perturbation analysis, and various detection mechanisms related to hallucination detection at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "250672fe-025e-4444-acf9-11c9cd05c136",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "a0f9bcb4-c482-4824-9bbe-eb1f90f853f2",
  "sourceToolAssistantUUID": "250672fe-025e-4444-acf9-11c9cd05c136",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T06:08:16.292Z_

<details><summary>↩ Tool result · `toolu_014TCFDUaJF17q5tWTesbBxH`</summary>

```text
Web search results for query: ""SHINE" hallucination probing perturbation entities arxiv 2411.09689"

Links: [{"title":"[2411.09689] Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/abs/2411.09689"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge — Seongmin Lee","url":"https://seongmin.xyz/papers/llm-hallucination-probing"},{"title":"LLM Hallucination Reasoning with Zero-shot Knowledge Test","url":"https://arxiv.org/html/2411.09689v1"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/pdf/2506.02696"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"A Graph Signal Processing Framework for Hallucination Detection","url":"https://www.arxiv.org/pdf/2510.19117"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Cross-Layer Attention Probing for Fine-Grained Hallucination Detection","url":"https://arxiv.org/html/2509.09700v1/"},{"title":"[2506.02696v1] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696v1"}]

Based on the search results, here's information about the SHINE paper (arXiv 2411.09689):

## Overview

The paper is titled "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge".

## What is SHINE?

SHINE stands for Systematic Hallucination Inspection with Noisy Entity. SHINE is a novel hallucination probing method that does not require external knowledge, supervised training, or LLM fine-tuning.

## Key Innovation

The core innovation is based on entity perturbation: The method is driven by a novel discovery that perturbing key entities in prompts affects LLM's generation of three types of text differently.

## Task Definition

The paper introduces hallucination probing as a new task that classifies LLM-generated text into three categories: aligned, misaligned, and fabricated.

## Performance

SHINE achieves state-of-the-art performance in hallucination detection, outperforming seven competing methods across four datasets and four LLMs. The method was evaluated on four modern LLMs: LLaMA2-13B-Chat, LLaMA3-8B-Instruct, Mistral-7B-Instruct, and Qwen2.5-7B-Instruct.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a4f1553-61a1-4ce3-8b17-7c12e1497d31",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "f3ee7b08-3042-4bbd-b1e3-f2aa0ae922bd",
  "sourceToolAssistantUUID": "9a4f1553-61a1-4ce3-8b17-7c12e1497d31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T06:08:17.110Z_

<details><summary>↩ Tool result · `toolu_01MFirAPJPHo2ED3QqpgXCp1`</summary>

```text
Web search results for query: "OpenReview ICML 2026 sharpness hallucination detection gradient sensitivity"

Links: [{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"SENSITIVITY-GUIDED HALLUCINATION DETECTION IN ...","url":"https://openreview.net/pdf/66488d1ef8a4e92ad8ef067d06d95fd1ba248fd9.pdf"},{"title":"HADEMIF: HALLUCINATION DETECTION AND MITI","url":"https://openreview.net/pdf?id=VwOYxPScxB"},{"title":"HALLUCINATION MITIGATION IN LARGE VISION","url":"https://openreview.net/pdf?id=Km4l2Fi2lc"},{"title":"What do Geometric Hallucination Detection Metrics Actually Measure? | OpenReview","url":"https://openreview.net/forum?id=OAb3kzatIV"},{"title":"ICML 2026 Workshop | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop"},{"title":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/"},{"title":"ICML 2026 | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026"},{"title":"LLM-Check: Investigating Detection of Hallucinations in Large Language Models","url":"https://openreview.net/pdf?id=LYx4w3CAgy"}]

Based on the search results, I found several relevant papers on OpenReview related to ICML 2026, sharpness, hallucination detection, and gradient sensitivity:

## Key Findings:

**1. "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity"**

This paper addresses hallucination detection for "Stubborn Hallucinations"—errors where LLMs are confidently wrong—and proposes a geometric solution called Embedding-Perturbed Gradient Sensitivity (EPGS). The hypothesis is that while robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization. EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude. This work is associated with ICML.

**2. "Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection"**

This paper proposes a gradient-based paradigm for hallucination detection by probing next-token prediction sensitivity, introducing a statistic called Next-token Gradient Sensitivity (NGS), which quantifies the first-order gradient of the maximum log-probability of the next token with respect to the current token's layer embedding, measuring local prediction fragility. NGS-HD computes the Maximum Mean Discrepancy (MMD) between each NGS of test tokens and NGS distributions from referenced truthful and hallucinated tokens.

**3. "What do Geometric Hallucination Detection Metrics Actually Measure?"**

This paper studies geometric signals in the internal state of an LLM that are predictive of hallucination and examines what specific properties of hallucinations these geometric statistics capture. The work shows that many existing geometric detection methods have substantial sensitivity to shifts in task domain and introduces a normalization method to mitigate this effect.

These papers represent recent research combining the concepts of sharpness, gradient sensitivity, and hallucination detection for ICML 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e231673d-c5f8-4b46-85a1-1d3d30901dd4",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "b65a7b1c-896d-4602-90aa-150e074f6332",
  "sourceToolAssistantUUID": "e231673d-c5f8-4b46-85a1-1d3d30901dd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T06:08:22.646Z_

<details><summary>↩ Tool result · `toolu_013q8MazXmCTXnX1AqaGZMti`</summary>

```text
Web search results for query: "OpenReview NeurIPS 2026 embedding perturbation hallucination sharpness"

Links: [{"title":"NeurIPS 2026 | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026"},{"title":"NeurIPS 2026 Conference | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FConference"},{"title":"NeurIPS 2026 Workshop Proposals | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FWorkshop_Proposals"},{"title":"GHOST: Hallucination-Inducing Image Generation for Multimodal LLMs | OpenReview","url":"https://openreview.net/forum?id=f4TACE7HhU"},{"title":"Exposing Hallucinations To Suppress Them: VLMs Representation Editing With Generative Anchors | OpenReview","url":"https://openreview.net/forum?id=cBhqgPtEqw"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS 2026 Evaluations and Datasets Track | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FEvaluations_and_Datasets_Track"},{"title":"NeurIPS: Neuro-anatomical Inductive Priors for Sphere-based Vision Brain Decoding | OpenReview","url":"https://openreview.net/forum?id=CZQJl1bUf7"},{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"NeurIPS 2026 AI-Assisted Reviewing Experiment","url":"https://neurips.cc/Conferences/2026/ai-reviewing-experiment"}]

The search returned general information about NeurIPS 2026 on OpenReview and a few papers related to hallucinations, but no specific papers matching the exact combination of terms you searched for (embedding perturbation + hallucination + sharpness in the context of NeurIPS 2026).

The results show:

1. **OpenReview NeurIPS 2026 information** - General conference pages and submission details
2. **Papers on hallucinations** - Including work on hallucination-inducing image generation (GHOST) and hallucination suppression methods for multimodal models, but these don't specifically focus on embedding perturbation or sharpness
3. **General conference information** - Details about submission deadlines and AI-assisted reviewing experiments

If you're looking for a specific paper with those keywords, you may want to:
- Try searching directly on OpenReview at openreview.net with more specific terms
- Search for combinations of the terms (e.g., "embedding perturbation" and "sharpness" separately)
- Check if the paper exists yet, as NeurIPS 2026 submissions have abstract deadlines on May 4, 2026 and full paper deadlines on May 6, 2026

Would you like me to search for more specific variations of these terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceba3e60-25b9-480a-b5bf-8132d3832a74",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "5114fe7d-dc62-4fed-9374-784212acb61e",
  "sourceToolAssistantUUID": "ceba3e60-25b9-480a-b5bf-8132d3832a74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-16T06:08:25.873Z_

Let me do a few more targeted searches to get additional details on the most threatening concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5114fe7d-dc62-4fed-9374-784212acb61e",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kM3wBLSLz1xueZBGXh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f63879e0-1cd2-4c9d-9049-c2e730363f5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFo3cnQGG1c8cNiEzLvGz6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1639,
      "cache_creation_input_tokens": 4990,
      "cache_read_input_tokens": 19566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4990,
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

_source line 44 · 2026-05-16T06:08:26.418Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B2ruEUocn3dAsQA3vHemy6`</summary>

```json
{
  "query": "\"From Flat Facts to Sharp Hallucinations\" ICML 2026 submission accepted Liew Tan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f63879e0-1cd2-4c9d-9049-c2e730363f5b",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kM3wBLSLz1xueZBGXh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ca657d2-bda8-4136-a99b-748aff5e291d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFo3cnQGG1c8cNiEzLvGz6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1639,
      "cache_creation_input_tokens": 4990,
      "cache_read_input_tokens": 19566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4990,
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

_source line 45 · 2026-05-16T06:08:26.926Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MiZMVnfWc13NrY2htvNDe1`</summary>

```json
{
  "query": "OpenReview \"sensitivity-guided hallucination detection\" sharpness gradient"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ca657d2-bda8-4136-a99b-748aff5e291d",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kM3wBLSLz1xueZBGXh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f128196c-db8b-4e1c-a5b3-237ccc1c39fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFo3cnQGG1c8cNiEzLvGz6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1639,
      "cache_creation_input_tokens": 4990,
      "cache_read_input_tokens": 19566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4990,
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

_source line 46 · 2026-05-16T06:08:27.940Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P1g1BUb12fof1YpnD6tNve`</summary>

```json
{
  "query": "\"Geometry of Hallucination\" \"Gradient Conflict\" topographic medium 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f128196c-db8b-4e1c-a5b3-237ccc1c39fa",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kM3wBLSLz1xueZBGXh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6183da70-94ad-46c5-903b-bbd31b418904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFo3cnQGG1c8cNiEzLvGz6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1639,
      "cache_creation_input_tokens": 4990,
      "cache_read_input_tokens": 19566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4990,
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

_source line 47 · 2026-05-16T06:08:28.357Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R3tzmD4FR8JFW2q6JR478C`</summary>

```json
{
  "query": "\"Cross-Layer Attention Probing\" CLAP hallucination residual stream 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6183da70-94ad-46c5-903b-bbd31b418904",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kM3wBLSLz1xueZBGXh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a6757ce-ce9b-44c6-82c6-5450d38f12e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFo3cnQGG1c8cNiEzLvGz6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1639,
      "cache_creation_input_tokens": 4990,
      "cache_read_input_tokens": 19566,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4990
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1639,
          "output_tokens": 258,
          "cache_read_input_tokens": 19566,
          "cache_creation_input_tokens": 4990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4990,
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

_source line 48 · 2026-05-16T06:08:31.389Z_

<details><summary>↩ Tool result · `toolu_01B2ruEUocn3dAsQA3vHemy6`</summary>

```text
Web search results for query: ""From Flat Facts to Sharp Hallucinations" ICML 2026 submission accepted Liew Tan"

Links: [{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"}]

Based on the search results, I found the paper "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity." 

The paper proposes a geometric solution called Embedding-Perturbed Gradient Sensitivity (EPGS), which addresses errors where LLMs are confidently wrong. The researchers hypothesize that robust facts reside in flat minima while stubborn hallucinations sit in sharp minima, and EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude.

However, the search results show this paper on arXiv (with ID 2605.00939) from 2 weeks ago, but I cannot confirm from these results whether it has been formally accepted to ICML 2026 or details about author attribution to "Liew Tan" specifically. The ArXiv version is available, but the acceptance status and detailed author information would require additional confirmation from the ICML 2026 proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ca657d2-bda8-4136-a99b-748aff5e291d",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "cd2dcd2c-eb73-441a-b3c0-ea2a688fcc67",
  "sourceToolAssistantUUID": "9ca657d2-bda8-4136-a99b-748aff5e291d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T06:08:32.219Z_

<details><summary>↩ Tool result · `toolu_01MiZMVnfWc13NrY2htvNDe1`</summary>

```text
Web search results for query: "OpenReview "sensitivity-guided hallucination detection" sharpness gradient"

Links: [{"title":"Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs | OpenReview","url":"https://openreview.net/forum?id=aZdcNDf3pc"},{"title":"SENSITIVITY-GUIDED HALLUCINATION DETECTION IN ...","url":"https://openreview.net/pdf/66488d1ef8a4e92ad8ef067d06d95fd1ba248fd9.pdf"}]

I found the research paper you're looking for! Here are the results:

Hallucination detection is essential for ensuring the reliability of large language models. The paper studies the separability of the sensitivity to prompt-induced perturbations in internal representations, establishing a theory showing that each sample admits a prompt under which factual samples exhibit greater sensitivity to prompt-induced perturbations than hallucinatory samples.

The researchers propose a theory-informed method called Sample-Specific Prompting (SSP), which adaptively selects prompts to perturb the model. Instead of relying on static or handcrafted prompts, SSP dynamically generates tailored prompts for each question-answer pair to enhance the sensitivity of truthful samples to perturbations while reducing that of hallucinatory ones.

When applied to representative datasets, the probability that sensitivity to prompt-induced perturbations provides discriminative power reaches nearly 99%.

The paper was published on OpenReview on October 8, 2025, and can be found at: https://openreview.net/forum?id=aZdcNDf3pc


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f128196c-db8b-4e1c-a5b3-237ccc1c39fa",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "b73cfed0-1a93-4f56-b50e-fe6583e407c0",
  "sourceToolAssistantUUID": "f128196c-db8b-4e1c-a5b3-237ccc1c39fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T06:08:33.354Z_

<details><summary>↩ Tool result · `toolu_01P1g1BUb12fof1YpnD6tNve`</summary>

```text
Web search results for query: ""Geometry of Hallucination" "Gradient Conflict" topographic medium 2026"

Links: [{"title":"The Geometry of Hallucination. Gradient Conflict and the Topographic… | by Micheal Bee | Feb, 2026 | Medium","url":"https://medium.com/@mbonsign/the-geometry-of-hallucination-f725f41f7050"}]

I found the article you were searching for! Here's what the search returned:

The article "The Geometry of Hallucination" discusses how hallucinations live in "dents" of high-dimensional manifolds shaped by pretraining, which are smooth surfaces where nearby points correspond to mutually consistent beliefs about the world.

The author explains that training is conceptualized as "terrain shaping," where gradient descent carves grooves into a landscape until correct predictions roll downhill naturally.

The concept of "Gradient Conflict" is central to the analysis: when gradients oppose each other (cos(θ) ≈ −1), "high loss plus persistent gradient conflict means the model is being forced into a topological lie."

When constraints conflict with the learned geometry, the optimizer "dents the manifold," and when user queries wander into these warped regions, "the model still follows the math — but the path is no longer connected to reality. We experience that disconnection as a hallucination."

The article was published on Medium in February 2026 by Micheal Bee and explores the geometric foundations of why neural networks produce hallucinations when faced with incompatible training objectives.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6183da70-94ad-46c5-903b-bbd31b418904",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "695715cb-887e-4405-83de-d003c7957fb8",
  "sourceToolAssistantUUID": "6183da70-94ad-46c5-903b-bbd31b418904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-16T06:08:34.840Z_

<details><summary>↩ Tool result · `toolu_01R3tzmD4FR8JFW2q6JR478C`</summary>

```text
Web search results for query: ""Cross-Layer Attention Probing" CLAP hallucination residual stream 2025"

Links: [{"title":"[2509.09700] Cross-Layer Attention Probing for Fine-Grained Hallucination Detection","url":"https://arxiv.org/abs/2509.09700"},{"title":"Cross-Layer Attention Probing for Fine-Grained Hallucination Detection","url":"https://arxiv.org/html/2509.09700v1/"},{"title":"Hallucination detection performance of CLAP versus baselines, measured... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Hallucination-detection-performance-of-CLAP-versus-baselines-measured-in-AUC-scores_tbl1_395474068"},{"title":"Published as a conference paper at ICLR 2025 REDEEP: DETECTING HALLUCINATION IN","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf"},{"title":"VADE: Visual Attention Guided Hallucination Detection and ...","url":"https://aclanthology.org/2025.findings-acl.773.pdf"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable ...","url":"https://aclanthology.org/2025.acl-long.880.pdf"},{"title":"Self-Consistency and Probe-Based Hallucination Detection","url":"https://www.emergentmind.com/topics/self-consistency-probe-based-hallucination-detection"},{"title":"Probing Internals Behind Prompt Leakage Intents","url":"https://aclanthology.org/2025.emnlp-main.1082.pdf"},{"title":"Mitigating Hallucinations in MLLMs with Attention Causal ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_Seeing_Far_and_Clearly_Mitigating_Hallucinations_in_MLLMs_with_Attention_CVPR_2025_paper.pdf"},{"title":"GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub","url":"https://github.com/NishilBalar/Awesome-LVLM-Hallucination"}]

Based on the search results, I found recent research on Cross-Layer Attention Probing (CLAP) for hallucination detection:

## Cross-Layer Attention Probing (CLAP)

CLAP is a novel activation probing technique for hallucination detection, which processes the LLM activations across the entire residual stream as a joint sequence.

### Key Features

The technique builds on research indicating that due to residual connections in transformers, the outputs of individual LLM layers can be considered to be in the same embedding space, and it explores how the activation pattern across LLM layers can be exploited to better detect hallucinations compared to looking at activation patterns of individual layers.

### Performance and Applications

Empirical evaluations using five LLMs and three tasks show that CLAP improves hallucination detection compared to baselines on both greedy decoded responses as well as responses sampled at higher temperatures, thus enabling fine-grained detection, i.e. the ability to disambiguate hallucinations and non-hallucinations among different sampled responses to a given prompt.

CLAP can be applied as a fine-grained detector to reduce LLM hallucination rate by sampling alternative responses to a given prompt and distinguishing hallucinated outputs from non-hallucinated ones.

### Out-of-Distribution Generalization

An out-of-distribution study revealed that attending to different layers enables CLAP to generalise more effectively.

The paper (arXiv:2509.09700) was published on September 4, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a6757ce-ce9b-44c6-82c6-5450d38f12e4",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "3f82f492-6708-4f0f-a2f2-dfe2450028c1",
  "sourceToolAssistantUUID": "6a6757ce-ce9b-44c6-82c6-5450d38f12e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T06:08:37.760Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ah2xnPj5nmH5Px7f6oJnGk`</summary>

```json
{
  "query": "\"Perturbations Matter\" \"Sensitivity-Guided Hallucination Detection\" SSP ICLR 2026 OpenReview aZdcNDf3pc"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f82f492-6708-4f0f-a2f2-dfe2450028c1",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kMx3VvoKwhRgESWgxJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f38942c8-881a-45b7-89e2-7c4853a76497",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMkTGUwopJKkG8SL8nsANi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4168,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4168,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 53 · 2026-05-16T06:08:38.794Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NRCQXSZThQPR2r55PQ1UH2`</summary>

```json
{
  "query": "\"in-context sharpness\" hallucination mitigation inner representation ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f38942c8-881a-45b7-89e2-7c4853a76497",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kMx3VvoKwhRgESWgxJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5afe894-14db-4746-a5cb-de21578c4d30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMkTGUwopJKkG8SL8nsANi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4168,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4168,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 54 · 2026-05-16T06:08:39.487Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JAzBm1ySSrN9sWtLP69QAB`</summary>

```json
{
  "query": "arxiv 2605.00939 \"flat minima\" \"sharp minima\" hallucination Hessian proxy EPGS datasets benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5afe894-14db-4746-a5cb-de21578c4d30",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kMx3VvoKwhRgESWgxJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e995eb96-734b-4377-ae23-d4988d2c4d4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMkTGUwopJKkG8SL8nsANi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4168,
      "cache_read_input_tokens": 24556,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4168
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 24556,
          "cache_creation_input_tokens": 4168,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4168,
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

_source line 55 · 2026-05-16T06:08:44.297Z_

<details><summary>↩ Tool result · `toolu_01NRCQXSZThQPR2r55PQ1UH2`</summary>

```text
Web search results for query: ""in-context sharpness" hallucination mitigation inner representation ICML 2024"

Links: [{"title":"GitHub - hkust-nlp/Activation_Decoding: In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation (ICML 2024)","url":"https://github.com/hkust-nlp/Activation_decoding"},{"title":"ICML Poster In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://icml.cc/virtual/2024/poster/32930"},{"title":"Mitigating Hallucinations in Large Vision-Language Models with Internal Fact-based Contrastive Decoding","url":"https://arxiv.org/html/2502.01056v1"},{"title":"[2403.01548] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://arxiv.org/abs/2403.01548"},{"title":"[Quick Review] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://liner.com/review/incontext-sharpness-as-alerts-inner-representation-perspective-for-hallucination-mitigation"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation | OpenReview","url":"https://openreview.net/forum?id=s3e8poX3kb"},{"title":"IN-CONTEXT SHARPNESS AS ALERTS: AN INNER REP","url":"https://openreview.net/pdf?id=24U6vAHnYM"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://proceedings.mlr.press/v235/chen24av.html"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://paperreading.club/page?id=212632"},{"title":"Activation_Decoding/transformers/tests/models/blip/test_modeling_tf_blip.py at main · hkust-nlp/Activation_Decoding","url":"https://github.com/hkust-nlp/Activation_Decoding/blob/main/transformers/tests/models/blip/test_modeling_tf_blip.py"}]

I found comprehensive search results for this paper. Here's what the research is about:

## In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation (ICML 2024)

This paper was authored by Chen, Xiong, Liu, Wu, Xiao, Gao, and He, and published at ICML 2024.

### Key Finding

The researchers discovered a pattern associated with hallucinations: correct generations tend to have sharper context activations in the hidden states of the in-context tokens, compared to that of the incorrect generations.

### Methodology

The authors propose an entropy-based metric to quantify the sharpness among the in-context hidden states and incorporate it into the decoding process, using the entropy value to adjust the next token prediction distribution to improve the factuality and overall quality of the generated text.

### Experimental Results

Experiments on knowledge-seeking datasets (Natural Questions, HotpotQA, TriviaQA) and hallucination benchmark (TruthfulQA) demonstrate consistent effectiveness, with up to 8.6 absolute points improvement on TruthfulQA.

### Implementation

The method (called "Activation Decoding") leverages the observation that correct generations tend to have sharper context activations in the hidden states of the in-context tokens, compared to that of the incorrect generations. The code implementation is available on GitHub at hkust-nlp/Activation_Decoding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5afe894-14db-4746-a5cb-de21578c4d30",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "7a546416-b12b-4348-a380-76336332d05f",
  "sourceToolAssistantUUID": "c5afe894-14db-4746-a5cb-de21578c4d30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T06:08:44.710Z_

<details><summary>↩ Tool result · `toolu_01Ah2xnPj5nmH5Px7f6oJnGk`</summary>

```text
Web search results for query: ""Perturbations Matter" "Sensitivity-Guided Hallucination Detection" SSP ICLR 2026 OpenReview aZdcNDf3pc"

Links: [{"title":"Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs | OpenReview","url":"https://openreview.net/forum?id=aZdcNDf3pc"},{"title":"SENSITIVITY-GUIDED HALLUCINATION DETECTION IN ...","url":"https://openreview.net/pdf?id=aZdcNDf3pc"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/d00c6f1f6d607af7a3e0d0bfeebefe57d49fa18f.pdf"},{"title":"HALLUCINATION MITIGATION IN LARGE VISION","url":"https://openreview.net/pdf?id=Km4l2Fi2lc"},{"title":"GPTZero uncovers 50+ Hallucinations in ICLR 2026","url":"https://gptzero.me/news/iclr-2026/"},{"title":"NEXT-TOKEN GRADIENT SENSITIVITY PROBING FOR LLM ...","url":"https://openreview.net/pdf/2a19947788cf8ce29d6d587447ae7eb6c039d117.pdf"},{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"Robust and Cheap Hallucination Detection in LLMs","url":"https://openreview.net/pdf?id=Zd0XLr6JKn"},{"title":"Mitigating Hallucinations in Large Vision-Language Models via Dual Contrastive Decoding | Proceedings of the 7th ACM International Conference on Multimedia in Asia","url":"https://dl.acm.org/doi/10.1145/3743093.3770933"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"}]

I found the paper! Here's what I found about "Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs":

## Overview

Hallucination detection is essential for ensuring the reliability of large language models. Internal representation–based methods have emerged as the prevailing direction for detecting hallucinations, yet the internal representations often fail to yield clear separability between truthful and hallucinatory content.

## Key Innovation

The researchers study the separability of the sensitivity to prompt-induced perturbations in the internal representations, and establish a theory showing that, with non-negligible probability, each sample admits a prompt under which factual samples exhibit greater sensitivity to prompt-induced perturbations than hallucinatory samples. When the theory is applied to the representative datasets, the probability reaches nearly 99%, suggesting that sensitivity to perturbations provides a discriminative indicator.

## Method: Sample-Specific Prompting (SSP)

The proposed theory-informed method Sample-Specific Prompting (SSP) adaptively selects prompts to perturb the model's internal states and measures the resulting sensitivity as a detection indicator. Extensive experiments across multiple benchmarks demonstrate that SSP consistently outperforms existing hallucination detection methods.

The paper is available on OpenReview at the forum ID aZdcNDf3pc and has been published as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f38942c8-881a-45b7-89e2-7c4853a76497",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "0383ae8c-e772-44b5-b2f4-ba027277fe25",
  "sourceToolAssistantUUID": "f38942c8-881a-45b7-89e2-7c4853a76497",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-16T06:08:45.671Z_

<details><summary>↩ Tool result · `toolu_01JAzBm1ySSrN9sWtLP69QAB`</summary>

```text
Web search results for query: "arxiv 2605.00939 "flat minima" "sharp minima" hallucination Hessian proxy EPGS datasets benchmarks"

Links: [{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"Sharpness-Aware Minimization Can Hallucinate Minimizers","url":"https://arxiv.org/html/2509.21818v1"},{"title":"Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs","url":"https://arxiv.org/html/2601.16527v1"},{"title":"On Hallucinations in Inverse Problems: Fundamental Limits and Provable Assessment Methods The authors gratefully acknowledge the Gauss Centre for Supercomputing e.V. (www.gauss-centre.eu) for funding this project by providing computing time through the John von Neumann Institute for Computing (NIC) on the GCS Supercomputer. D.I was supported by a PhD fellowship from the Deutsches Zentrum für Luft und Raumfahrt (DLR). N.M.G. acknowledges research sponsored by the Laboratory Directed Research and Development","url":"https://arxiv.org/html/2605.13146"},{"title":"A Function Centric Perspective on Flat and Sharp Minima","url":"https://arxiv.org/html/2510.12451v1"},{"title":"How to Escape Sharp Minima with Random Perturbations","url":"https://arxiv.org/html/2305.15659v3"},{"title":"[2605.07723] LLM hallucinations in the wild: Large-scale evidence from non-existent citations","url":"https://arxiv.org/abs/2605.07723"},{"title":"[2202.00661] When Do Flat Minima Optimizers Work?","url":"https://ar5iv.labs.arxiv.org/html/2202.00661"},{"title":"Unique Properties of Flat Minima in Deep Networks","url":"https://arxiv.org/pdf/2002.04710"}]

Based on the web search results, I found the arXiv paper 2605.00939. Here's what I discovered:

## Paper Summary

The paper is titled "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity" and addresses traditional hallucination detection failures on "Stubborn Hallucinations" — errors where LLMs are confidently wrong.

## Key Concepts

The authors propose Embedding-Perturbed Gradient Sensitivity (EPGS), based on the hypothesis that while robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization.

## Methodology

EPGS detects sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude, acting as an efficient proxy for the Hessian spectrum to differentiate stable knowledge from unstable memorization.

## Results

The experiments show that EPGS significantly outperforms entropy-based and representation-based baselines, providing a robust signal for detecting high-confidence factual errors.

The paper connects loss landscape geometry (flat vs. sharp minima) to the reliability of language model outputs, proposing that understanding the curvature of the loss landscape around model predictions can help identify which "facts" the model confidently states are actually robust knowledge versus brittle memorized errors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e995eb96-734b-4377-ae23-d4988d2c4d4a",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "55221ee0-2e03-4d3d-b6ce-b4af812b2e07",
  "sourceToolAssistantUUID": "e995eb96-734b-4377-ae23-d4988d2c4d4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-16T06:08:48.552Z_

Now let me try to read the actual arXiv abstract page for the EPGS paper to get the full details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55221ee0-2e03-4d3d-b6ce-b4af812b2e07",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kNkSH57WYyP2RdeHki",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f63f4c9-0520-4f8c-bc52-a509dcdf3cf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QTiKmXMsrkPT95sCuLTc9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 28724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3069,
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

_source line 59 · 2026-05-16T06:08:48.811Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01G1HVMjJvGdU61A2nYK7LJj`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f63f4c9-0520-4f8c-bc52-a509dcdf3cf9",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kNkSH57WYyP2RdeHki",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc393d07-f5ce-4c6c-807a-cb4bb5e1ee86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QTiKmXMsrkPT95sCuLTc9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 28724,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3069
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 28724,
          "cache_creation_input_tokens": 3069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3069,
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

_source line 60 · 2026-05-16T06:08:48.814Z_

<details><summary>↩ Tool result · `toolu_01G1HVMjJvGdU61A2nYK7LJj`</summary>

````text
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
  "parentUuid": "fc393d07-f5ce-4c6c-807a-cb4bb5e1ee86",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "34f5ea48-5ade-49b7-bca0-8187e87d9f36",
  "sourceToolAssistantUUID": "fc393d07-f5ce-4c6c-807a-cb4bb5e1ee86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-16T06:08:52.124Z_



Let me fetch the full details of the most critical papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34f5ea48-5ade-49b7-bca0-8187e87d9f36",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kNzAmTSv56eyaKa7xW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbef9f5b-e341-426f-b0ee-bc9ef735103f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjZxj8bYCo3vF7CX9yGsuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 31793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 723,
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

_source line 62 · 2026-05-16T06:08:53.651Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SutmFqZyz3cgHmsUHduF87`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.00939",
  "prompt": "Extract the complete abstract, all author names and affiliations, submission date, and any mention of conference submission (ICML, NeurIPS, ICLR, etc.). Also extract the key methods, datasets used, baselines compared against, and main quantitative results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbef9f5b-e341-426f-b0ee-bc9ef735103f",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kNzAmTSv56eyaKa7xW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d0fb1d3-aa2d-4759-abff-9f95a62f91cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjZxj8bYCo3vF7CX9yGsuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 31793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 723,
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

_source line 63 · 2026-05-16T06:08:55.894Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016SRgbcapJtYzT1q5fccxCt`</summary>

```json
{
  "url": "https://openreview.net/forum?id=yzWGQNTbHQ",
  "prompt": "Extract the complete paper title, all author names, venue (ICML/NeurIPS/ICLR 2026 etc.), submission date, acceptance status, abstract, and key methodology details. What conference was this submitted to and was it accepted?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d0fb1d3-aa2d-4759-abff-9f95a62f91cc",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kNzAmTSv56eyaKa7xW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c889b47d-0a71-4b35-a7a1-ecdd9f5084ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjZxj8bYCo3vF7CX9yGsuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 31793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 723,
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

_source line 64 · 2026-05-16T06:08:56.869Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JRaBtrVeEKmckWFCdS3iko`</summary>

```json
{
  "url": "https://openreview.net/forum?id=aZdcNDf3pc",
  "prompt": "Extract the complete paper title, all author names, venue (ICML/NeurIPS/ICLR 2026 etc.), submission date, acceptance status, abstract, and key methodology details. What conference was this submitted to and was it accepted?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c889b47d-0a71-4b35-a7a1-ecdd9f5084ff",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kNzAmTSv56eyaKa7xW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "481c459c-c1ce-438a-aa12-34e2fafed61b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjZxj8bYCo3vF7CX9yGsuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 31793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 723,
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

_source line 65 · 2026-05-16T06:08:57.651Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X8EVWEKeMXorZ8VGKCVedW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.04743",
  "prompt": "Extract the complete abstract, all author names, submission date, and any mention of conference submission. Extract the key methods, how they relate to loss landscape geometry and hallucination detection, and main results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "481c459c-c1ce-438a-aa12-34e2fafed61b",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kNzAmTSv56eyaKa7xW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f56b23ba-d7a8-4bbb-afea-e3b45a82b19c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjZxj8bYCo3vF7CX9yGsuP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 31793,
      "output_tokens": 513,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 723
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 513,
          "cache_read_input_tokens": 31793,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 723,
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

_source line 66 · 2026-05-16T06:08:58.718Z_

<details><summary>↩ Tool result · `toolu_01SutmFqZyz3cgHmsUHduF87`</summary>

```text
# Paper Summary: Hallucination Detection via Gradient Sensitivity

## Abstract
"Traditional hallucination detection fails on 'Stubborn Hallucinations' - errors where LLMs are confidently wrong. We propose a geometric solution: Embedding-Perturbed Gradient Sensitivity (EPGS)."

## Authors
- Yee Zhing Liew
- Andrew Huey Ping Tan
- Anwar P.P. Abdul Majeed

(No institutional affiliations provided in the page content)

## Submission Information
- **Submission Date:** May 1, 2026
- **Revision:** May 12, 2026 (v2)
- **Conference:** Accepted to ICML 2026 (camera-ready version)
- **arXiv ID:** 2605.00939

## Key Method
The paper introduces EPGS, which detects problematic model outputs by "perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude" to differentiate stable knowledge from unstable memorization.

## Main Claim
The authors hypothesize that accurate facts occupy flat optimization minima while stubborn errors occupy sharp minima due to brittle memorization patterns.

## Results & Baselines
The document indicates "EPGS significantly outperforms entropy-based and representation-based baselines," though specific quantitative metrics are not provided in this excerpt.

**Note:** Full experimental details, dataset specifications, and numerical results are not available in the provided page content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d0fb1d3-aa2d-4759-abff-9f95a62f91cc",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "acb51c42-45e9-49b2-806f-267487a826ad",
  "sourceToolAssistantUUID": "5d0fb1d3-aa2d-4759-abff-9f95a62f91cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-16T06:08:59.156Z_

<details><summary>↩ Tool result · `toolu_016SRgbcapJtYzT1q5fccxCt`</summary>

```text
# Paper Details

**Title:** "Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection"

**Authors:** Shuhai Zhang, Xutao Wen, Jiahao Yang, Zhiquan Wen, Feng Liu, Bo Han, Yuanqing Li, Mingkui Tan

**Venue:** ICLR 2026 Conference

**Submission Date:** September 18, 2025 (modified February 11, 2026)

**Acceptance Status:** Unknown—the content indicates this is a submission under review on OpenReview, but does not specify whether it was accepted or rejected.

## Key Methodology

The authors propose a gradient-based approach using Next-token Gradient Sensitivity (NGS), which quantifies "the first-order gradient of the maximum log-probability of the next token w.r.t. the current token's layer embedding." Their detection method, NGS-HD, treats hallucination detection as a token-level distribution comparison task using Maximum Mean Discrepancy (MMD) to compute truthfulness scores with theoretical guarantees.

**Keywords:** Large Language Models; Hallucination Detection; Maximum Mean Discrepancy
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c889b47d-0a71-4b35-a7a1-ecdd9f5084ff",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "694df975-09e1-4c3d-8dc3-b6b5ced87210",
  "sourceToolAssistantUUID": "c889b47d-0a71-4b35-a7a1-ecdd9f5084ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T06:09:00.163Z_

<details><summary>↩ Tool result · `toolu_01JRaBtrVeEKmckWFCdS3iko`</summary>

```text
# Paper Information Summary

**Title:** "Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs"

**Authors:** Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, Ling Chen

**Venue:** ICLR 2026 Conference

**Submission Date:** September 3, 2025 (modified February 11, 2026)

**Acceptance Status:** Not indicated in the provided content. The page lists this as "Submitted to ICLR 2026" with a submission number (1365), but no acceptance decision is documented.

## Core Methodology

The researchers propose Sample-Specific Prompting (SSP), which operates on this principle: "with non-negligible probability, each sample admits a prompt under which factual samples exhibit greater sensitivity to prompt-induced perturbations than hallucinatory samples."

The approach adaptively selects prompts to perturb the model's internal representations and measures the resulting sensitivity as a detection metric. Testing across representative datasets showed approximately 99% probability that this sensitivity differential exists, validating perturbations as a discriminative hallucination indicator.

**Primary Research Area:** Unsupervised, self-supervised, semi-supervised, and supervised representation learning
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "481c459c-c1ce-438a-aa12-34e2fafed61b",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "9e5e8a26-83a2-4d1a-8e48-41e6c133ea5f",
  "sourceToolAssistantUUID": "481c459c-c1ce-438a-aa12-34e2fafed61b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-16T06:09:04.037Z_

<details><summary>↩ Tool result · `toolu_01X8EVWEKeMXorZ8VGKCVedW`</summary>

```text
# Paper Summary: Hallucination Basins

## Complete Abstract
"Large language models (LLMs) hallucinate: they produce fluent outputs that are factually incorrect. We present a geometric dynamical systems framework in which hallucinations arise from task-dependent basin structure in latent space. Using autoregressive hidden-state trajectories across multiple open-source models and benchmarks, we find that separability is strongly task-dependent rather than universal: factoid settings can show clearer basin separation, whereas summarization and misconception-heavy settings are typically less stable and often overlap. We formalize this behavior with task-complexity and multi-basin theorems, characterize basin emergence in L-layer transformers, and show that geometry-aware steering can reduce hallucination probability without retraining."

## Authors
- Kalyan Cherukuri
- Lav R. Varshney

## Submission Information
- **Date:** April 6, 2026
- **arXiv ID:** 2604.04743
- **No conference submission mentioned** in the provided content

## Key Methods
The authors employ a **geometric dynamical systems approach** analyzing autoregressive hidden-state trajectories across models. They trace how representations evolve during token generation, examining basin structure in latent space—regions where trajectories naturally converge toward factual or hallucinated outputs.

## Relation to Loss Landscape Geometry
The framework conceptualizes hallucinations through task-dependent basin structure, treating factuality and hallucination as distinct attractors in latent geometry. Basin separation varies by task type, reflecting underlying landscape topography.

## Main Results
- Basin separability is task-dependent, stronger for factoid tasks and weaker for summarization
- Formal characterization via task-complexity and multi-basin theorems
- Geometry-aware steering reduces hallucination without model retraining
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f56b23ba-d7a8-4bbb-afea-e3b45a82b19c",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "93516baa-243f-40b9-bd94-fa8bb8c08976",
  "sourceToolAssistantUUID": "f56b23ba-d7a8-4bbb-afea-e3b45a82b19c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-16T06:09:07.069Z_

This is extremely important -- the EPGS paper has been **accepted to ICML 2026**. Let me get a few more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93516baa-243f-40b9-bd94-fa8bb8c08976",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kQ6z5BESNe1EB6iFJ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0da12693-99f5-402f-a32b-c043e1aa1a6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmVs9ByGsW3YSmih72SqLb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 32516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1939,
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

_source line 71 · 2026-05-16T06:09:10.177Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01W7jD9fREuFvWW1b51gMACZ`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.00939",
  "prompt": "Extract ALL details about: (1) the specific datasets and benchmarks used for evaluation, (2) exact quantitative results (AUROC, accuracy, F1, etc.), (3) which baseline methods were compared against, (4) which LLMs were tested (model names), (5) how exactly EPGS works step by step (the perturbation process, gradient computation, Hessian proxy details), (6) any discussion of limitations, and (7) the specific definition of \"stubborn hallucinations\" used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0da12693-99f5-402f-a32b-c043e1aa1a6d",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kQ6z5BESNe1EB6iFJ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa11213b-e474-431f-bc59-73430d4f9dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmVs9ByGsW3YSmih72SqLb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 32516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1939,
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

### Tool result

_source line 72 · 2026-05-16T06:09:10.818Z_

<details><summary>↩ Tool result · `toolu_01W7jD9fREuFvWW1b51gMACZ`</summary>

```text
API Error: 400 {"type":"error","error":{"type":"invalid_request_error","message":"The request body is not valid JSON: no low surrogate in string: line 1 column 102415 (char 102414)"},"request_id":"req_011Cb5kQaoe7CWCp7BavdaWZ"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa11213b-e474-431f-bc59-73430d4f9dcf",
  "isSidechain": true,
  "promptId": "8761cb13-095f-462b-9661-148caf330ac3",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "540b75ca-ddda-4d7b-9307-187d6a5a0c09",
  "sourceToolAssistantUUID": "fa11213b-e474-431f-bc59-73430d4f9dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-16T06:09:13.265Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TUAdyVsjKFMens9HTLmh8H`</summary>

```json
{
  "url": "https://openreview.net/pdf/2a19947788cf8ce29d6d587447ae7eb6c039d117.pdf",
  "prompt": "Extract all details about: (1) the NGS method - how it works step by step, (2) datasets used, (3) quantitative results, (4) how it relates to perturbation-based sensitivity and sharpness of embeddings, (5) acceptance status at ICLR 2026, and (6) key differences from methods that perturb embeddings with noise."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "540b75ca-ddda-4d7b-9307-187d6a5a0c09",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kQ6z5BESNe1EB6iFJ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c73b9ae6-4b24-47dd-804b-847a0d600c5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmVs9ByGsW3YSmih72SqLb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 32516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1939,
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

_source line 74 · 2026-05-16T06:09:15.624Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011BwRXk6wRMWrYQdGwvszSo`</summary>

```json
{
  "query": "\"loss landscape sharpness\" OR \"flat minima\" hallucination LLM detection inference 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c73b9ae6-4b24-47dd-804b-847a0d600c5b",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kQ6z5BESNe1EB6iFJ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb0dea91-bb42-4fca-98ac-2d95bde9e03e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmVs9ByGsW3YSmih72SqLb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1939,
      "cache_read_input_tokens": 32516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1939,
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

### Tool result

_source line 75 · 2026-05-16T06:09:20.097Z_

<details><summary>↩ Tool result · `toolu_01TUAdyVsjKFMens9HTLmh8H`</summary>

```text
# NGS Method Analysis

## 1. NGS Method: Step-by-Step Operation

The document appears to be a PDF containing compressed/encoded content that prevents direct extraction of detailed NGS methodology. However, based on the structure visible in the object definitions, the method involves sequential processing steps applied to embeddings or data representations.

## 2. Datasets Used

The PDF structure references multiple object streams and font definitions but does not clearly expose dataset names in the extractable portions. Specific dataset identifications are embedded within compressed stream objects.

## 3. Quantitative Results

Numerical results are contained within the flattened content streams (objects 1150-1156) but are not directly readable due to compression and encoding. The document references "40" pages and contains measurement data, though specific metrics remain inaccessible.

## 4. Relationship to Perturbation-Based Sensitivity and Embedding Sharpness

The provided content does not yield clear information about explicit connections to perturbation analysis or embedding sharpness measures in extractable form.

## 5. ICLR 2026 Acceptance Status

The document is a linearized PDF with internal reference "/Info 376 0 R" and "/Prev 2627443," suggesting archival structure. The presence of page annotations and outlined content structure indicates a complete academic paper, but acceptance confirmation is not directly stated in accessible portions.

## 6. Key Differences from Perturbation-Based Noise Methods

Comparative methodology details remain embedded within the compressed streams and are not reliably extractable from the current document state.

**Note:** The provided PDF is heavily compressed with flattened content streams, preventing comprehensive extraction of technical details without proper decompression utilities.

[Binary content (application/pdf, 2.5MB) also saved to /home/ubuntu/.claude-account-3/projects/-/3bbc0513-910d-48c4-b837-41d3d647b4d5/tool-results/webfetch-1778911753965-yf7jrx.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c73b9ae6-4b24-47dd-804b-847a0d600c5b",
  "isSidechain": true,
  "promptId": "4a08558a-cd2d-4665-a2c8-0b4c9fe98c15",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "a9da4832-7bbe-458a-b361-ff02cce58e9b",
  "sourceToolAssistantUUID": "c73b9ae6-4b24-47dd-804b-847a0d600c5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-16T06:09:24.277Z_

<details><summary>↩ Tool result · `toolu_011BwRXk6wRMWrYQdGwvszSo`</summary>

```text
Web search results for query: ""loss landscape sharpness" OR "flat minima" hallucination LLM detection inference 2025 2026 arxiv"

Links: [{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"Understanding, measuring and controlling LLM hallucinations","url":"https://angelo-lima.fr/en/llm-hallucinations-devoxx-2026-en/"},{"title":"Hallucination Detection and Mitigation in Large Language Models","url":"https://arxiv.org/html/2601.09929v1"},{"title":"Mitigating LLM Hallucinations: A Comprehensive Review of Techniques and Architectures[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202505.1955"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"How to Detect Hallucinations in Your LLM Applications","url":"https://www.getmaxim.ai/articles/how-to-detect-hallucinations-in-your-llm-applications/"},{"title":"[2510.06265] Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/abs/2510.06265"},{"title":"LLM Hallucination Statistics 2026: AI Gets Facts Wrong Up to 82% of the Time","url":"https://sqmagazine.co.uk/llm-hallucination-statistics/"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"}]

I've completed a web search on hallucination detection and mitigation in LLMs for 2025-2026. Here are the key findings:

## Recent Research on LLM Hallucination Detection (2025-2026)

**Detection Approaches:**

Traditional uncertainty measures like token-level entropy fail when LLMs produce high-confidence hallucinations where the model consistently generates the same incorrect output with high certainty, as entropy remains low because the model's probability distribution is sharply peaked around wrong answers. Expected Calibration Error (ECE) addresses this by quantifying miscalibration—the disconnect between the model's confidence scores and actual accuracy—helping flag scenarios where models are confidently wrong.

**Mitigation Strategies:**

Rewarding Doubt (2025) integrates confidence calibration into reinforcement learning, penalizing both over- and underconfidence, while uncertainty-aware RLHF variants score cautious, evidence-backed answers higher than verbose but unsupported ones.

**Hallucination Detection Tools:**

HalluEval 2.0 is designed specifically for hallucination detection. HalluGraph (Devoteam, AAAI 2026) uses a knowledge-graph approach to legal verification; if the AI fails the knowledge graph consistency test, the system blocks the answer and requires human intervention.

**Current Landscape:**

By 2025, the field has shifted from chasing zero hallucinations to managing uncertainty in a measurable, predictable way. A 2025 leaderboard analysis found the top 5 models cluster between 10%–20% hallucination rates.

I note that the search results focus on hallucination detection and mitigation rather than connections to loss landscape sharpness or flat minima specifically. Would you like me to search more specifically for papers on loss landscape geometry and its relationship to hallucinations?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb0dea91-bb42-4fca-98ac-2d95bde9e03e",
  "isSidechain": true,
  "promptId": "4a08558a-cd2d-4665-a2c8-0b4c9fe98c15",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "bddf437a-c2ed-41f0-bf67-f44c9decd137",
  "sourceToolAssistantUUID": "bb0dea91-bb42-4fca-98ac-2d95bde9e03e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-16T06:09:27.411Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ty3VzzKuNvMALZWk9rmBis`</summary>

```json
{
  "query": "\"sharpness-aware\" OR \"SAM\" hallucination unlearning multimodal LLM 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bddf437a-c2ed-41f0-bf67-f44c9decd137",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kRbSchfW6tkGEW7jLb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "261b811b-da0b-409e-bb2b-e75e4046f2ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6Tuhh8MXPx1gBb4oZCui5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 34455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2063,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 78 · 2026-05-16T06:09:28.055Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017btkZqovntibrvh1kaRNKc`</summary>

```json
{
  "query": "arxiv 2601.16527 \"sharpness-aware robust erasure hallucinations multimodal\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "261b811b-da0b-409e-bb2b-e75e4046f2ce",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kRbSchfW6tkGEW7jLb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "595ed1f3-7277-482d-8ebf-52bac6774842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6Tuhh8MXPx1gBb4oZCui5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 34455,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2063
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 34455,
          "cache_creation_input_tokens": 2063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2063,
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

_source line 79 · 2026-05-16T06:09:34.000Z_

<details><summary>↩ Tool result · `toolu_017btkZqovntibrvh1kaRNKc`</summary>

```text
Web search results for query: "arxiv 2601.16527 "sharpness-aware robust erasure hallucinations multimodal""

Links: [{"title":"[2601.16527] Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs","url":"https://arxiv.org/abs/2601.16527"},{"title":"Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs","url":"https://arxiv.org/html/2601.16527v1"},{"title":"Sharpness-Aware Minimization Can Hallucinate Minimizers","url":"https://arxiv.org/html/2509.21818v1"},{"title":"Hallucination Detection in Foundation Models for Decision- ...","url":"https://arxiv.org/pdf/2403.16527"},{"title":"[2601.21181] MAD: Modality-Adaptive Decoding for Mitigating Cross-Modal Hallucinations in Multimodal Large Language Models","url":"https://arxiv.org/abs/2601.21181"},{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v2"},{"title":"MAD: Modality-Adaptive Decoding for Mitigating Cross-Modal Hallucinations in Multimodal Large Language Models","url":"https://arxiv.org/html/2601.21181"},{"title":"[2509.21818] Sharpness-Aware Minimization Can Hallucinate Minimizers","url":"https://arxiv.org/abs/2509.21818"},{"title":"Eliminating Hallucination in Diffusion-Augmented Interactive Text-to-Image Retrieval","url":"https://arxiv.org/html/2601.20391v1"},{"title":"Decoupling Contrastive Decoding: Robust Hallucination Mitigation in Multimodal Large Language Models","url":"https://arxiv.org/html/2504.08809"}]

I found the paper! Here's what I found:

**Paper Title:** Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs

**Authors:** Xianya Fang, Feiyang Ren, Xiang Chen, Yu Tian, Zhen Bi, Haiyang Yu, Sheng-Jun Huang

**Key Details:**
- Submitted on 23 Jan 2026

**Main Problem:** Multimodal LLMs are powerful but prone to object hallucinations, which describe non-existent entities and harm reliability.

**Key Finding:** Standard erasure achieves only superficial suppression, trapping the model in sharp minima where hallucinations catastrophically resurge after lightweight relearning.

**Proposed Solution:** SARE casts unlearning as a targeted min-max optimization problem and uses a Targeted-SAM mechanism to explicitly flatten the loss landscape around hallucinated concepts.

You can access the full paper at https://arxiv.org/abs/2601.16527.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "595ed1f3-7277-482d-8ebf-52bac6774842",
  "isSidechain": true,
  "promptId": "4a08558a-cd2d-4665-a2c8-0b4c9fe98c15",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "df838e51-ac60-4f74-a102-e86ba905615b",
  "sourceToolAssistantUUID": "595ed1f3-7277-482d-8ebf-52bac6774842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-16T06:09:34.558Z_

<details><summary>↩ Tool result · `toolu_01Ty3VzzKuNvMALZWk9rmBis`</summary>

```text
Web search results for query: ""sharpness-aware" OR "SAM" hallucination unlearning multimodal LLM 2025 2026 arxiv"

Links: [{"title":"[2601.16527] Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs","url":"https://arxiv.org/abs/2601.16527"},{"title":"Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs","url":"https://arxiv.org/html/2601.16527"},{"title":"[2509.21818] Sharpness-Aware Minimization Can Hallucinate Minimizers","url":"https://arxiv.org/abs/2509.21818"},{"title":"[2502.05374] Towards LLM Unlearning Resilient to Relearning Attacks: A Sharpness-Aware Minimization Perspective and Beyond","url":"https://arxiv.org/abs/2502.05374"},{"title":"Sharpness-Aware Minimization Can Hallucinate Minimizers","url":"https://arxiv.org/html/2509.21818v2"},{"title":"SAKED: Mitigating Hallucination in Large Vision-Language Models via Stability-Aware Knowledge Enhanced Decoding","url":"https://arxiv.org/html/2602.09825"},{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v2"},{"title":"Hallucination of Multimodal Large Language Models: A Survey","url":"https://arxiv.org/pdf/2404.18930"},{"title":"When Semantics Mislead Vision: Mitigating Large Multimodal Models Hallucinations in Scene Text Spotting and Understanding","url":"https://arxiv.org/html/2506.05551v1"},{"title":"Combating Multimodal LLM Hallucination via Bottom-up Holistic Reasoning","url":"https://arxiv.org/html/2412.11124v1"}]

I found several relevant papers on arxiv matching your search query. Here are the key results:

## Highly Relevant Papers

**1. Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs (SARE)**

This paper (arXiv 2601.16527) was published on January 23, 2026. The paper addresses how multimodal LLMs are prone to object hallucinations while recent unlearning methods have a critical flaw: structural fragility. The authors propose SARE, which casts unlearning as a targeted min–max optimization problem and uses a Targeted-SAM mechanism to explicitly flatten the loss landscape around hallucinated concepts.

**2. LLM Unlearning Resilient to Relearning Attacks: A Sharpness-Aware Minimization Perspective**

This paper (arXiv 2502.05374) was last updated on May 27, 2025. The paper establishes a connection between robust unlearning and sharpness-aware minimization (SAM) through a unified robust optimization framework, in analogy to adversarial training designed to defend against adversarial attacks.

**3. Sharpness-Aware Minimization Can Hallucinate Minimizers**

This paper (arXiv 2509.21818) was last updated on February 5, 2026. The paper shows that SAM can stall at points where the shifted gradient vanishes despite a nonzero original gradient, and calls these "hallucinated minimizers," proving their existence under simple nonconvex landscape conditions.

These papers represent cutting-edge research combining sharpness-aware optimization techniques with hallucination mitigation and unlearning in multimodal language models from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "261b811b-da0b-409e-bb2b-e75e4046f2ce",
  "isSidechain": true,
  "promptId": "4a08558a-cd2d-4665-a2c8-0b4c9fe98c15",
  "agentId": "aebbb5073ac9d69e3",
  "type": "user",
  "uuid": "5cb2494b-dd56-4323-8264-78d22a1a153c",
  "sourceToolAssistantUUID": "261b811b-da0b-409e-bb2b-e75e4046f2ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-16T06:10:52.764Z_

I now have a comprehensive picture. Here is the full report.

---

## Competitive Landscape Report: Sharpness / Perturbation-Based Hallucination Detection

### CRITICAL FINDING -- DIRECT CONCURRENT WORK

**"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity"**
- arXiv: [2605.00939](https://arxiv.org/abs/2605.00939)
- Authors: Yee Zhing Liew, Andrew Huey Ping Tan, Anwar P.P. Abdul Majeed
- Date: May 1, 2026 (revised May 12, 2026)
- Status: **ACCEPTED to ICML 2026** (camera-ready version on arXiv)

This paper is an extremely close match to your research idea. The overlap is as follows:

- **Same core hypothesis:** Robust facts reside in flat minima; "stubborn hallucinations" reside in sharp minima supported by brittle memorization.
- **Same mechanism:** They propose **Embedding-Perturbed Gradient Sensitivity (EPGS)**, which perturbs input embeddings with Gaussian noise and measures the resulting spike in gradient magnitude.
- **Same framing:** EPGS is explicitly described as an efficient proxy for the Hessian spectrum, differentiating stable knowledge from unstable memorization.
- **Same target:** The paper specifically targets "stubborn hallucinations" -- high-confidence factual errors where entropy-based methods fail.
- **Same claim:** EPGS significantly outperforms entropy-based and representation-based baselines.

This is essentially the exact idea you described: using sharpness of the loss landscape via perturbation-based sensitivity of embeddings to detect stubborn hallucinations at inference time. It was posted ~2 weeks ago and is already accepted at ICML 2026.

---

### HIGHLY RELATED WORK (Tier 1 -- Strong Overlap)

**1. "Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs"**
- OpenReview: [aZdcNDf3pc](https://openreview.net/forum?id=aZdcNDf3pc)
- Authors: Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, Ling Chen
- Venue: **Submitted to ICLR 2026** (submitted Sep 3, 2025; revised Feb 11, 2026)
- Method: **Sample-Specific Prompting (SSP)** -- proves theoretically that with ~99% probability, each sample admits a prompt under which factual samples exhibit greater sensitivity to prompt-induced perturbations than hallucinatory samples in internal representations. Adaptively selects prompts to perturb the model and measures sensitivity as detection signal.
- Key difference from your idea: Operates on prompt-level perturbations rather than embedding-space Gaussian noise, but shares the core insight that perturbation sensitivity in internal representations discriminates hallucinations.

**2. "Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection"**
- OpenReview: [yzWGQNTbHQ](https://openreview.net/forum?id=yzWGQNTbHQ)
- Authors: Shuhai Zhang, Xutao Wen, Jiahao Yang, Zhiquan Wen, Feng Liu, Bo Han, Yuanqing Li, Mingkui Tan
- Venue: **Submitted to ICLR 2026** (submitted Sep 18, 2025; revised Feb 11, 2026)
- Method: **Next-token Gradient Sensitivity (NGS)** -- computes the first-order gradient of max log-probability of the next token w.r.t. the current token's layer embedding. Proves that the norm of NGS bounds prediction confidence changes under small perturbations. Uses MMD between NGS distributions of test tokens vs. reference truthful/hallucinated tokens.
- Key difference: Focuses on next-token prediction gradient rather than explicit embedding perturbation, but the underlying signal (local prediction fragility measured via gradient w.r.t. embeddings) is conceptually very close.

---

### RELATED WORK (Tier 2 -- Partial Overlap)

**3. "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations"**
- arXiv: [2604.04743](https://arxiv.org/abs/2604.04743)
- Authors: Kalyan Cherukuri, Lav R. Varshney
- Date: April 6, 2026
- Venue: Not yet submitted to a conference (based on available info)
- Overview: Geometric dynamical systems framework where hallucinations arise from task-dependent basin structure in latent space. Formalizes basin separation with task-complexity theorems and shows geometry-aware steering reduces hallucination without retraining.
- Key difference: Focuses on trajectory-level dynamics and basin structure rather than gradient sensitivity under perturbation, but shares the geometric/landscape framing.

**4. "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations"**
- arXiv: [2506.02696](https://arxiv.org/abs/2506.02696)
- Date: June 3, 2025
- Method: **Sample-Specific Prompting (SSP)** framework that analyzes perturbation sensitivity at intermediate representations. Uses a lightweight encoder to amplify representation changes from perturbation and a contrastive distance metric.
- Result: +4.78% AUROC on TruthfulQA.
- Key difference: Perturbation at prompt level and contrastive analysis of intermediate representations, rather than gradient-magnitude measurement.

**5. "Hallucination Begins Where Saliency Drops"**
- arXiv: [2601.20279](https://arxiv.org/abs/2601.20279)
- Venue: **Published at ICLR 2026**
- Method: LVLMs-Saliency, a gradient-aware diagnostic framework that fuses attention weights with input gradients to quantify visual grounding strength. Proposes Saliency-Guided Rejection Sampling (SGRS) for inference-time filtering.
- Key difference: Targets vision-language models and uses gradient-attention fusion rather than embedding perturbation. But shares the gradient-based inference-time detection philosophy.

**6. "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation"**
- arXiv: [2403.01548](https://arxiv.org/abs/2403.01548)
- Venue: **ICML 2024**
- Authors: Chen, Xiong, Liu, Wu, Xiao, Gao, He (HKUST)
- Method: Uses entropy-based metric to quantify "sharpness" among in-context hidden states. Correct generations have sharper context activations. Incorporates this into decoding (Activation Decoding).
- Key difference: "Sharpness" here refers to concentration/entropy of hidden-state activations, not loss-landscape curvature or gradient sensitivity under perturbation. This is a predecessor that established the "sharpness" vocabulary in this domain.

**7. "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge" (SHINE)**
- arXiv: [2411.09689](https://arxiv.org/abs/2411.09689)
- Date: November 2024
- Method: SHINE (Systematic Hallucination Inspection with Noisy Entity) perturbs key entities in prompts and observes how LLM generation of different text types is affected differently. No external knowledge or fine-tuning needed.
- Key difference: Prompt-level entity perturbation rather than embedding-space perturbation; text-output-level observation rather than gradient measurement.

**8. "Cross-Layer Attention Probing for Fine-Grained Hallucination Detection" (CLAP)**
- arXiv: [2509.09700](https://arxiv.org/abs/2509.09700)
- Date: September 2025
- Method: Attention mechanism operating on the full residual stream across layers. Exploits the fact that layer outputs share embedding space due to residual connections.
- Key difference: Probes residual stream activations directly rather than measuring perturbation sensitivity, but operates in the same internal-representation space.

---

### RELATED WORK (Tier 3 -- Tangential but Noteworthy)

**9. "Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs" (SARE)**
- arXiv: [2601.16527](https://arxiv.org/abs/2601.16527)
- Date: January 2026
- Uses Targeted-SAM to flatten the loss landscape around hallucinated concepts during training/unlearning. Shows standard erasure traps models in sharp minima where hallucinations resurge.
- Key difference: Training-time intervention (unlearning), not inference-time detection.

**10. "A Single Direction of Truth: An Observer Model's Linear Residual Probe"**
- arXiv: [2507.23221](https://arxiv.org/abs/2507.23221)
- Method: Generator-agnostic observer model detects hallucinations via a linear probe on residual stream. Finds hallucinations encoded along a common linear direction.
- Key difference: Linear probe, no perturbation or sharpness analysis.

**11. "Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration"**
- arXiv: [2603.22812](https://arxiv.org/abs/2603.22812)
- Date: March 2026
- Method: Perturbation-based importance sampling to explore semantic space efficiently.
- Key difference: Perturbation in semantic/output space, not embedding/gradient space.

---

### OpenReview Conference Submission Check

- **ICML 2026:** The EPGS paper (2605.00939) is confirmed accepted. The OpenReview ICML 2026 page is live. No other sharpness-based hallucination detection papers found in the ICML 2026 listings beyond EPGS.
- **ICLR 2026:** Two closely related papers were submitted -- NGS (gradient sensitivity) and SSP (perturbation sensitivity). "Hallucination Begins Where Saliency Drops" was published at ICLR 2026 (gradient-aware, but vision-language focused). Acceptance status of NGS and SSP is not confirmed from available data.
- **NeurIPS 2026:** Submissions opened with abstract deadline May 4, 2026 and paper deadline May 6, 2026. No specific sharpness-hallucination papers found yet (too early for public listings).

---

### Bottom Line Assessment

**Someone is already doing this exact thing.** The EPGS paper (Liew, Tan, & Abdul Majeed, ICML 2026) is a near-perfect overlap with your described research idea:

1. Same hypothesis (flat minima = robust facts, sharp minima = stubborn hallucinations)
2. Same mechanism (perturb embeddings, measure gradient sensitivity as Hessian proxy)
3. Same target (stubborn/high-confidence hallucinations that defeat entropy-based methods)
4. Same framing (inference-time sharpness estimation)
5. It was posted May 1, 2026 and is already accepted at ICML 2026

Additionally, NGS (ICLR 2026 submission) and SSP (ICLR 2026 submission) attack the same problem from slightly different angles (gradient sensitivity of next-token prediction, and prompt-perturbation sensitivity of internal representations, respectively).

If you want to proceed, you would need to clearly differentiate from EPGS. Possible angles might include: (a) perturbation of residual streams at specific intermediate layers rather than input embeddings, (b) a different sharpness estimator (e.g., second-order/Hessian-vector products rather than gradient magnitude), (c) focus on abstention/selective prediction rather than just detection scoring, (d) application to chain-of-thought or agentic settings, or (e) theoretical analysis that EPGS does not provide. But the core idea as described is now published and accepted.

Sources:
- [From Flat Facts to Sharp Hallucinations (EPGS) - arXiv 2605.00939](https://arxiv.org/abs/2605.00939)
- [From Flat Facts to Sharp Hallucinations - HTML version](https://arxiv.org/html/2605.00939)
- [Perturbations Matter: Sensitivity-Guided Hallucination Detection (SSP) - OpenReview](https://openreview.net/forum?id=aZdcNDf3pc)
- [Next-Token Gradient Sensitivity Probing (NGS) - OpenReview](https://openreview.net/forum?id=yzWGQNTbHQ)
- [Hallucination Basins - arXiv 2604.04743](https://arxiv.org/abs/2604.04743)
- [Shaking to Reveal - arXiv 2506.02696](https://arxiv.org/abs/2506.02696)
- [Hallucination Begins Where Saliency Drops - arXiv 2601.20279](https://arxiv.org/abs/2601.20279)
- [In-Context Sharpness as Alerts (ICML 2024) - arXiv 2403.01548](https://arxiv.org/abs/2403.01548)
- [SHINE: Perturbation-Driven Hallucination Probing - arXiv 2411.09689](https://arxiv.org/abs/2411.09689)
- [Cross-Layer Attention Probing (CLAP) - arXiv 2509.09700](https://arxiv.org/abs/2509.09700)
- [Beyond Superficial Unlearning (SARE) - arXiv 2601.16527](https://arxiv.org/abs/2601.16527)
- [The Geometry of Hallucination - Medium blog post](https://medium.com/@mbonsign/the-geometry-of-hallucination-f725f41f7050)
- [Semantic Illusion in RAG Systems - arXiv 2512.15068](https://arxiv.org/abs/2512.15068)
- [Efficient Hallucination Detection via Bayesian Semantic Entropy - arXiv 2603.22812](https://arxiv.org/abs/2603.22812)
- [EdinburghNLP Awesome Hallucination Detection - GitHub](https://github.com/EdinburghNLP/awesome-hallucination-detection)
- [ICML 2026 - OpenReview](https://openreview.net/group?id=ICML.cc%2F2026)
- [NeurIPS 2026 - OpenReview](https://openreview.net/group?id=NeurIPS.cc%2F2026)
- [ICLR 2026 Papers](https://iclr.cc/virtual/2026/papers.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cb2494b-dd56-4323-8264-78d22a1a153c",
  "isSidechain": true,
  "agentId": "aebbb5073ac9d69e3",
  "requestId": "req_011Cb5kSMQo4kSddbvyw7NnL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a185f6c-3133-47c3-9baa-cfb63e898099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bbc0513-910d-48c4-b837-41d3d647b4d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6cqhSAqU6x6wF4eC9Cjce",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 829,
      "cache_creation_input_tokens": 1241,
      "cache_read_input_tokens": 36518,
      "output_tokens": 3751,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1241
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 829,
          "output_tokens": 3751,
          "cache_read_input_tokens": 36518,
          "cache_creation_input_tokens": 1241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1241,
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
