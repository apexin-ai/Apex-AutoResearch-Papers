# Research conversation: Search for competing and concurrent work that may overlap with the idea of "RL co-training test generator and fixer for 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae184d7f2b108c704.jsonl`
- **Structured JSON:** [`6006f2af4178b74c4c3b.json`](../../sessions/60/6006f2af4178b74c4c3b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-16T05:53:46.934Z_

Search for competing and concurrent work that may overlap with the idea of "RL co-training test generator and fixer for repo-level code repair." I need to find papers the generator may have missed.

Do these searches:
1. WebSearch: "reinforcement learning test generation code repair 2025 2026"
2. WebSearch: "co-training test generator code fixer reinforcement learning"
3. WebSearch: "SWE-bench reinforcement learning training 2026"
4. WebSearch: "learned test generation software repair arxiv 2026"
5. WebSearch: "RL reward signal SWE-bench docker execution"
6. WebSearch: "test-driven code repair large language model 2026"
7. WebSearch: "execution feedback guided repair LLM 2025 2026"
8. WebSearch: "site:arxiv.org repo-level code repair test generation 2026"

For each search, report the top results with titles, venues, and brief descriptions. I'm looking for papers that are doing essentially the same thing as "RL-CoTest" (co-training test generator + fixer with RL for repo-level repair).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5c7d4218-6234-48e7-a63c-54cbc067a333",
  "agentId": "ae184d7f2b108c704",
  "type": "user",
  "uuid": "2502d8bf-8de7-412e-922e-ed022a0508ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T05:53:46.941Z_

```json
{
  "parentUuid": "2502d8bf-8de7-412e-922e-ed022a0508ae",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "dbc4dc5a-7279-4db0-b654-cf60d8883238",
  "timestamp": "2026-05-16T05:53:46.941Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T05:53:49.706Z_



I'll load the WebSearch tool first, then run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbc4dc5a-7279-4db0-b654-cf60d8883238",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jEVvZT9yw6p95wkzTX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1014479a-c107-4103-bcf0-1cac9804ec49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZ8pmMns6YuuwKyoDThbXh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 787,
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

_source line 4 · 2026-05-16T05:53:49.854Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015gh83LE1XJ7qx6PU7FVTXi`</summary>

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
  "parentUuid": "1014479a-c107-4103-bcf0-1cac9804ec49",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jEVvZT9yw6p95wkzTX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0c95daf-fd96-4dd1-a45f-3bcd8d357dff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZ8pmMns6YuuwKyoDThbXh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 7304,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 787
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 787,
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

_source line 5 · 2026-05-16T05:53:49.862Z_

<details><summary>↩ Tool result · `toolu_015gh83LE1XJ7qx6PU7FVTXi`</summary>

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
  "parentUuid": "a0c95daf-fd96-4dd1-a45f-3bcd8d357dff",
  "isSidechain": true,
  "promptId": "5c7d4218-6234-48e7-a63c-54cbc067a333",
  "agentId": "ae184d7f2b108c704",
  "type": "user",
  "uuid": "65cc8ddf-6153-4697-96c9-df3117214e65",
  "sourceToolAssistantUUID": "a0c95daf-fd96-4dd1-a45f-3bcd8d357dff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T05:53:52.574Z_



Now let me run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65cc8ddf-6153-4697-96c9-df3117214e65",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jEinxr474qM1F3fh4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef5dac52-d859-480d-b339-5b865b65179f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcMTd32BSywZm7XjB1tQHP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8091,
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

_source line 7 · 2026-05-16T05:53:53.042Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Yatpm654SjcBcDzb9b7utA`</summary>

```json
{
  "query": "reinforcement learning test generation code repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef5dac52-d859-480d-b339-5b865b65179f",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jEinxr474qM1F3fh4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f02f5f7-d3ad-4f68-a1a6-7e7e7b909b07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcMTd32BSywZm7XjB1tQHP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8091,
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

_source line 8 · 2026-05-16T05:53:53.176Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RgKjNC4o8dyVJpXDLjoKp8`</summary>

```json
{
  "query": "co-training test generator code fixer reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f02f5f7-d3ad-4f68-a1a6-7e7e7b909b07",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jEinxr474qM1F3fh4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4592462f-adf7-4974-a78a-9080f2b73fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcMTd32BSywZm7XjB1tQHP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8091,
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

_source line 9 · 2026-05-16T05:53:53.515Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WiMqa1U3M4VtbxAyk2HecQ`</summary>

```json
{
  "query": "SWE-bench reinforcement learning training 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4592462f-adf7-4974-a78a-9080f2b73fea",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jEinxr474qM1F3fh4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fb45faa-2625-4209-ab61-b11e2a839441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcMTd32BSywZm7XjB1tQHP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8091,
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

_source line 10 · 2026-05-16T05:53:53.954Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017Yduo8NYScqN4DhjdzuWEh`</summary>

```json
{
  "query": "learned test generation software repair arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fb45faa-2625-4209-ab61-b11e2a839441",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jEinxr474qM1F3fh4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e410b357-a0b9-44d3-8c46-ae690aa799dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcMTd32BSywZm7XjB1tQHP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8091,
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

_source line 11 · 2026-05-16T05:53:54.454Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JPcjmZtuorqLwHzQrEqD6H`</summary>

```json
{
  "query": "RL reward signal SWE-bench docker execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e410b357-a0b9-44d3-8c46-ae690aa799dd",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jEinxr474qM1F3fh4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "692b5909-571c-4840-b4fd-e1d0c28c06eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcMTd32BSywZm7XjB1tQHP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8091,
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

_source line 12 · 2026-05-16T05:53:54.461Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J9KeiyKLWdqoTf1QzFi552`</summary>

```json
{
  "query": "test-driven code repair large language model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "692b5909-571c-4840-b4fd-e1d0c28c06eb",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jEinxr474qM1F3fh4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb746483-e65b-4334-8f8f-60945ac77bc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcMTd32BSywZm7XjB1tQHP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8091,
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

_source line 13 · 2026-05-16T05:53:54.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AKmciD8GccywobtT6XRC8P`</summary>

```json
{
  "query": "execution feedback guided repair LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb746483-e65b-4334-8f8f-60945ac77bc6",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jEinxr474qM1F3fh4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3a61701-6891-4682-b0ce-93b29f28a645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcMTd32BSywZm7XjB1tQHP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8091,
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

_source line 14 · 2026-05-16T05:53:55.084Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BheMSdQzL2xiyDqTwnGowR`</summary>

```json
{
  "query": "site:arxiv.org repo-level code repair test generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3a61701-6891-4682-b0ce-93b29f28a645",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jEinxr474qM1F3fh4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e1ac25f-2730-405a-bb49-8b4ffd6f3182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcMTd32BSywZm7XjB1tQHP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 8091,
      "output_tokens": 400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 400,
          "cache_read_input_tokens": 8091,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1413,
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

_source line 15 · 2026-05-16T05:53:59.967Z_

<details><summary>↩ Tool result · `toolu_01RgKjNC4o8dyVJpXDLjoKp8`</summary>

```text
Web search results for query: "co-training test generator code fixer reinforcement learning"

Links: [{"title":"ATGen: Adversarial Reinforcement Learning for Test Case Generation","url":"https://arxiv.org/html/2510.14635v1"},{"title":"Learning to Generate Unit test via Adversarial Reinforcement Learning","url":"https://arxiv.org/html/2508.21107"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/html/2506.03136v2"},{"title":"An Iterative Test-and-Repair Framework for Competitive Code Generation","url":"https://arxiv.org/html/2604.05560"},{"title":"Preprint LEARNING TO GENERATE UNIT TEST VIA ADVERSAR-","url":"https://arxiv.org/pdf/2508.21107"},{"title":"[2506.03136] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/abs/2506.03136"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=wPdBe9zxNr"},{"title":"[2508.21107] Learning to Generate Unit Test via Adversarial Reinforcement Learning","url":"https://arxiv.org/abs/2508.21107"},{"title":"Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://arxiv.org/html/2603.15611"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250603136W/abstract"}]

Based on the search results, here are the key research works on co-training test generators and code fixers using reinforcement learning:

## Key Frameworks

**CURE (Co-Evolving LLM Coder and Unit Tester)**: A novel reinforcement learning framework with a dedicated reward design that co-evolves coding and unit test generation capabilities based on their interaction outcomes, without any ground-truth code as supervision. It leverages the code generator to provide supervision for the unit test generator, while simultaneously improving the code generator itself to produce more accurate outputs that guide the generation of correct unit tests.

**UTRL (Unit Test Reinforcement Learning)**: This framework iteratively trains two LLMs, the unit test generator and the code generator, in an adversarial manner via RL: the unit test generator is trained to maximize a discrimination reward, encouraging it to produce tests that reveal faults in the code generator's solutions; and the code generator is trained to maximize a code reward, encouraging it to produce solutions that pass the unit tests generated by the unit test generator.

**FixAudit**: A framework that trains two roles within a single shared model: a Fixer that performs localized repair while preserving correct logic, and an Auditor that reads the candidate code to generate tests targeting its specific bugs. Through a four-stage training pipeline, including execution-aligned supervised fine-tuning followed by three stages of reinforcement learning, FixAudit first equips the model with execution reasoning and then progressively trains it for initial repair, test generation, and closed-loop refinement.

**Code-A1**: A novel reinforcement learning framework that orchestrates the adversarial co-evolution of a Code LLM and a Test LLM. By decoupling code and test generation into two models with opposing objectives, Code-A1 circumvents the limitations arising from self-play to avoid self-collusion and safely enables white-box testing.

These frameworks represent recent advances in using reinforcement learning to jointly optimize code generation and test case generation through adversarial co-evolution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4592462f-adf7-4974-a78a-9080f2b73fea",
  "isSidechain": true,
  "promptId": "5c7d4218-6234-48e7-a63c-54cbc067a333",
  "agentId": "ae184d7f2b108c704",
  "type": "user",
  "uuid": "c0d84b20-af5a-4d08-be4e-24631de233a1",
  "sourceToolAssistantUUID": "4592462f-adf7-4974-a78a-9080f2b73fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T05:54:01.513Z_

<details><summary>↩ Tool result · `toolu_01WiMqa1U3M4VtbxAyk2HecQ`</summary>

```text
Web search results for query: "SWE-bench reinforcement learning training 2026"

Links: [{"title":"[2512.18552] Toward Training Superintelligent Software Agents through Self-Play SWE-RL","url":"https://arxiv.org/abs/2512.18552"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL","url":"https://www.together.ai/blog/deepswe"},{"title":"Meet SWE-rebench-V2: A multilingual, executable dataset for training Software Engineering Agents","url":"https://nebius.com/blog/posts/meet-swe-rebench-v2"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution | OpenReview","url":"https://openreview.net/forum?id=ULblO61XZ0"},{"title":"SWE-bench February 2026 leaderboard update","url":"https://simonwillison.net/2026/Feb/19/swe-bench/"},{"title":"AI Agent Benchmarking Infrastructure on GPU Cloud: Run SWE-bench, GAIA, Terminal-Bench, and OSWorld at Scale (2026 Guide) | Spheron Blog","url":"https://www.spheron.network/blog/ai-agent-benchmarking-gpu-cloud-swebench-gaia/"},{"title":"Self-play SWE-RL Framework","url":"https://www.emergentmind.com/topics/self-play-swe-rl-ssr"},{"title":"[2602.23866] SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale","url":"https://arxiv.org/abs/2602.23866"}]

Based on the search results, here's what I found about SWE-bench reinforcement learning training in 2026:

## Recent RL Training Approaches for SWE-bench

Self-play SWE-RL (SSR) is a framework that trains LLM agents via reinforcement learning in a self-play setting to iteratively inject and repair software bugs of increasing complexity. On the SWE-bench Verified and SWE-Bench Pro benchmarks, SSR achieves notable self-improvement (+10.4 and +7.8 points, respectively).

## DeepSWE and RL at Scale

DeepSWE-Preview, a reasoning-enabled coding agent trained from Qwen3-32B with only reinforcement learning (RL), achieves an impressive 59% on SWE-Bench-Verified with test-time scaling, reaching state-of-the-art for open-weight coding agents (42.2% Pass@1, 71.0% Pass@16). With just 200 steps of RL training, SWE-Bench-Verified score increases from 23→42% (+20%) for Pass@1.

## New Training Datasets

SWE-rebench-V2 is the next iteration of a large-scale dataset of reinforcement learning (RL) environments for training autonomous software engineering agents. SWE-rebench-V2 includes: 32,000+ executable tasks, each with a pre-built Docker environment; Coverage across 20 programming languages; 100,000+ additional tasks derived from pull requests.

## General RL Advances

SWE-RL is the first approach to scale RL-based LLM reasoning for real-world software engineering, enabling models to learn from extensive open-source software evolution data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fb45faa-2625-4209-ab61-b11e2a839441",
  "isSidechain": true,
  "promptId": "5c7d4218-6234-48e7-a63c-54cbc067a333",
  "agentId": "ae184d7f2b108c704",
  "type": "user",
  "uuid": "b3ca5799-2cbc-4669-9741-6366a9a68fe1",
  "sourceToolAssistantUUID": "0fb45faa-2625-4209-ab61-b11e2a839441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T05:54:01.523Z_

<details><summary>↩ Tool result · `toolu_01J9KeiyKLWdqoTf1QzFi552`</summary>

```text
Web search results for query: "test-driven code repair large language model 2026"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Can test cases generated by large language models facilitate automated program repair? | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-026-10802-w"},{"title":"Large Language Models for Unit Test Generation:","url":"https://arxiv.org/pdf/2511.21382"},{"title":"Large Language Models (LLMs) for Source Code Analysis: applications, models and datasets","url":"https://arxiv.org/html/2503.17502v1"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"A Systematic Literature Review on Large Language Models for Automated Program Repair","url":"https://arxiv.org/html/2405.01466v4"},{"title":"The use of large language models for program repair - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S092054892400120X"},{"title":"A Review of Large Language Models for Automated Test Case Generation","url":"https://www.mdpi.com/2504-4990/7/3/97"},{"title":"Automated Repair of C Programs Using Large Language Models","url":"https://arxiv.org/html/2509.01947v1"},{"title":"Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead","url":"https://arxiv.org/html/2511.21382v1"}]

I found relevant research on test-driven code repair with large language models in 2026. Here are the key findings:

## Recent Research on Test-Driven LLM-Based Code Repair (2026)

A 2026 study in Empirical Software Engineering titled "Can test cases generated by large language models facilitate automated program repair?" explores how LLM-generated test cases impact program repair.

In a typical test-driven repair scenario, automated program repair (APR) aims to find a minimal program variant that passes the available test suite, which contains at least one test case that the original buggy program fails to satisfy.

### Key Trends and Approaches

The dominant approach involves capturing error messages from external toolchains and feeding them back to the LLM for self-correction, with frameworks like ChatUniTest and CasModaTest implementing this by parsing compiler errors and runtime exceptions before injecting feedback into a new prompt.

Prompt engineering has emerged as the dominant utilization strategy accounting for 89% of studies due to its flexibility, and iterative validation and repair loops have become the standard mechanism to ensure robust usability with significant improvements in compilation and execution.

The emergence of agent-aware and multimodal LLMs (e.g., GPT-4o and Claude-3.5) during 2024–2025 represents a new phase emphasizing interactive, repository-level, and tool-integrated APR, with these models being actively explored for autonomous reasoning and end-to-end repair.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb746483-e65b-4334-8f8f-60945ac77bc6",
  "isSidechain": true,
  "promptId": "5c7d4218-6234-48e7-a63c-54cbc067a333",
  "agentId": "ae184d7f2b108c704",
  "type": "user",
  "uuid": "fba9c0d4-eb8c-4573-a132-4cbe5ffb2c06",
  "sourceToolAssistantUUID": "cb746483-e65b-4334-8f8f-60945ac77bc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T05:54:01.527Z_

<details><summary>↩ Tool result · `toolu_01Yatpm654SjcBcDzb9b7utA`</summary>

```text
Web search results for query: "reinforcement learning test generation code repair 2025 2026"

Links: [{"title":"An Iterative Test-and-Repair Framework for Competitive Code Generation","url":"https://arxiv.org/html/2604.05560"},{"title":"Enhancing queries for code generation with reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-21271-4"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"CodeReasoner: Enhancing the Code Reasoning Ability with Reinforcement Learning","url":"https://arxiv.org/html/2507.17548v1"},{"title":"Agentic Reinforcement Learning for Real-World Code Repair","url":"https://arxiv.org/html/2510.22075"},{"title":"Scaling Code-Repair Agents with Reinforcement Learning","url":"https://www.cerebras.ai/blog/scaling-code-repair-agents-with-reinforcement-learning-extending-openhands-for-real-world"},{"title":"Preprint, September 2025 CODERL+: Improving Code Generation via Reinforce-","url":"https://www.arxiv.org/pdf/2510.18471"},{"title":"RLEF: GROUNDING CODE LLMS IN EXECUTION FEEDBACK WITH REINFORCEMENT LEARNING","url":"https://www.arxiv.org/pdf/2410.02089"},{"title":"RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=PzSG5nKe1q"}]

I found relevant research on reinforcement learning for test generation and code repair from 2025-2026. Here's a summary of the key findings:

## Recent Frameworks and Approaches

Reinforcement learning (RL) has emerged as a natural approach for improving code generation by using execution feedback as reward signals.

### Notable 2025-2026 Systems

**FixAudit**: A framework treating competitive code generation as a continuous, targeted test-and-repair debugging process centered on the current candidate solution. After training and test-time scaling, FixAudit built on Qwen2.5-Coder-7B-Instruct achieves 30.40% average Pass@1 and 56.77% average AvgPassRatio.

**CURE**: CURE (Wang et al., 2025), the state-of-the-art RL-based framework that jointly trains a Coder and a Tester within a single model.

**Agentic RL Systems**: Agentic systems structure repair as a multi-turn decision-making process. RLEF Gehring et al. (2024b) uses PPO-trained LLM agents receiving execution results during iterative code generation, achieving state-of-the-art on CodeContests, HumanEval+, and MBPP+.

### Code Reasoning and Repair

Reinforcement learning has been applied to program repair (Wei et al., 2025b), where a simple reward based on the line-level similarity between the generated and correct patches leads to significant performance improvements after training.

### Broad Applications

Reinforcement learning has been increasingly applied in software engineering to enhance the performance of various tasks. In fuzz testing, researchers use reinforcement learning to guide fuzzers toward generating more effective inputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f02f5f7-d3ad-4f68-a1a6-7e7e7b909b07",
  "isSidechain": true,
  "promptId": "5c7d4218-6234-48e7-a63c-54cbc067a333",
  "agentId": "ae184d7f2b108c704",
  "type": "user",
  "uuid": "c5085396-d494-40ea-8e5e-9f7e101d4d1f",
  "sourceToolAssistantUUID": "2f02f5f7-d3ad-4f68-a1a6-7e7e7b909b07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T05:54:01.936Z_

<details><summary>↩ Tool result · `toolu_017Yduo8NYScqN4DhjdzuWEh`</summary>

```text
Web search results for query: "learned test generation software repair arxiv 2026"

Links: [{"title":"Agentic Program Repair from Test Failures at Scale: A Neuro-symbolic approach with static analysis and test execution feedback","url":"https://arxiv.org/html/2507.18755v1"},{"title":"[1408.2103] A Critical Review of “Automatic Patch Generation Learned from Human-Written Patches”: Essay on the Problem Statement and the Evaluation of Automatic Software Repair","url":"https://ar5iv.labs.arxiv.org/html/1408.2103"},{"title":"Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead","url":"https://arxiv.org/html/2511.21382v1"},{"title":"Enhancing Large Language Models with Retrieval Augmented Generation for Software Testing and Inspection Automation","url":"https://arxiv.org/html/2604.15270"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"Optimization-Aware Test Generation for Deep Learning Compilers","url":"https://arxiv.org/html/2511.18918"},{"title":"Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection","url":"https://arxiv.org/html/2508.06365"},{"title":"Dynamic Cogeneration of Bug Reproduction Test in Agentic Program Repair","url":"https://arxiv.org/html/2601.19066v1"},{"title":"[2408.03095] TestART: Improving LLM-based Unit Testing via Co-evolution of Automated Generation and Repair Iteration","url":"https://arxiv.org/abs/2408.03095"},{"title":"Enhancing LLM-Based Test Generation by Eliminating Covered Code Weizhe Xu","url":"https://arxiv.org/pdf/2602.21997"}]

The search results show several recent papers on arXiv (from 2025-2026) related to learned test generation and software repair. Here are some key findings:

## Recent Work on Test Generation and Software Repair

A comprehensive survey analyzing 115 publications reveals that the research community has rapidly integrated classic SE techniques with LLMs, with context enrichment techniques based on program analysis and post-generation repair techniques centered on feedback loops becoming the standard for improving the quality of LLM-generated tests.

Recent work addresses test generation for software engineering issues, which are usually informal and lack automated tests but are invaluable for software development, as such tests can reproduce issues, make them more concrete, and help stakeholders agree upon desired behavior following test-driven development practices.

Bug reproduction test (BRT) generation has gained more interest as BRTs are increasingly used to assess AI-generated fixes, with researchers proposing various LLM-based BRT generation techniques including inverting LLM-generated assertions, combining search-based software testing with LLMs, using feedback to improve bug reproducibility, and training BRT generation LLMs.

TestART is a novel unit test generation method that improves LLM-based unit testing via co-evolution of automated generation and repair iteration, leveraging template-based repair strategy to fix bugs in LLM-generated test cases.

With the advent of LLMs, sophisticated agentic program repair has become viable, with work developing Engineering Agents that fix source code based on test failures at scale across diverse software offerings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e410b357-a0b9-44d3-8c46-ae690aa799dd",
  "isSidechain": true,
  "promptId": "5c7d4218-6234-48e7-a63c-54cbc067a333",
  "agentId": "ae184d7f2b108c704",
  "type": "user",
  "uuid": "6a29b5f4-e475-4508-8fcb-792e6c2b4a73",
  "sourceToolAssistantUUID": "e410b357-a0b9-44d3-8c46-ae690aa799dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T05:54:02.812Z_

<details><summary>↩ Tool result · `toolu_01BheMSdQzL2xiyDqTwnGowR`</summary>

```text
Web search results for query: "site:arxiv.org repo-level code repair test generation 2026"

Links: [{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Automated Benchmark Generation for Repository-Level Coding Tasks","url":"https://arxiv.org/pdf/2503.07701"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/html/2603.01048v1"},{"title":"[2603.01048] RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/abs/2603.01048"},{"title":"Code Agents are State of the Art Software Testers","url":"https://arxiv.org/html/2406.12952v1"},{"title":"Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints","url":"https://arxiv.org/html/2604.04580"},{"title":"CatCoder: Repository-Level Code Generation with Relevant Code and Type Context","url":"https://arxiv.org/pdf/2406.03283"},{"title":"Evaluating and Improving Automated Repository-Level Rust Issue Resolution with LLM-based Agents","url":"https://arxiv.org/html/2602.22764v1"},{"title":"In Line with Context: Repository-Level Code Generation via Context Inlining","url":"https://arxiv.org/pdf/2601.00376"}]

I've completed the web search for "site:arxiv.org repo-level code repair test generation 2026". Here are the key findings:

## Recent ArXiv Papers (2026)

**RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair** (March 2026)
RepoRepair is a documentation-enhanced approach for repository-level fault localization and program repair that leverages LLMs to generate hierarchical code documentation to enable comprehensive understanding of repository-level context and dependencies. On SWE-bench Lite, RepoRepair achieves a 45.7% repair rate at $0.44 per fix, and on SWE-bench Multimodal, it delivers state-of-the-art performance with a 37.1% repair rate at $0.56 per fix.

**Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints** (April 2026)
This framework treats tests as dynamic constraints that guide and are revised by the repair process, and through mutual evaluation and semantic recombination, candidate code and test artifacts progressively narrow behavior space, enabling the system to produce both code patches and corresponding test patches within the same search process.

**Evaluating and Improving Automated Repository-Level Rust Issue Resolution with LLM-based Agents** (February 2026)
This work addresses repository-level code understanding, targeted search, issue-reproducing test generation, and precise code editing.

**Retrieval-Augmented Code Generation Survey** (October 2025)
APT leverages newly generated test cases to guide subsequent test generation.

These papers demonstrate active research in combining repo-level code repair with test generation as complementary tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e1ac25f-2730-405a-bb49-8b4ffd6f3182",
  "isSidechain": true,
  "promptId": "5c7d4218-6234-48e7-a63c-54cbc067a333",
  "agentId": "ae184d7f2b108c704",
  "type": "user",
  "uuid": "3a5a4f5e-6726-494d-a3b8-6eb480658d5c",
  "sourceToolAssistantUUID": "6e1ac25f-2730-405a-bb49-8b4ffd6f3182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T05:54:03.599Z_

<details><summary>↩ Tool result · `toolu_01AKmciD8GccywobtT6XRC8P`</summary>

```text
Web search results for query: "execution feedback guided repair LLM 2025 2026"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair Islem Bouzenia","url":"https://arxiv.org/pdf/2403.17134"},{"title":"An empirical evaluation of pre-trained large language models for repairing declarative formal specifications | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10687-1"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate","url":"https://arxiv.org/html/2604.02647v1"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair Islem Bouzenia","url":"https://software-lab.org/publications/icse2025_RepairAgent.pdf"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | Request PDF","url":"https://www.researchgate.net/publication/392956389_RepairAgent_An_Autonomous_LLM-Based_Agent_for_Program_Repair"},{"title":"Template-guided interpretable reasoning with execution feedback for LLM-based program repair - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950584926000479"},{"title":"CodeLLMPaper/data/papers/labels/program_repair.md at main · PurCL/CodeLLMPaper","url":"https://github.com/PurCL/CodeLLMPaper/blob/main/data/papers/labels/program_repair.md"},{"title":"GitHub - GLEAM-Lab/ProgramRepair: A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications · GitHub","url":"https://github.com/GLEAM-Lab/ProgramRepair"}]

Based on the search results, I found several relevant papers and frameworks on execution feedback-guided repair using LLMs in 2025-2026:

## Key Recent Works

**TRACE Framework (2026)**: TRACE is a template-guided reasoning framework that enhances LLMs' bug-fixing performance across multiple programming languages while improving repair interpretability, by integrating both successful patterns from repair templates and failure experiences from previous execution results into the LLM-driven repair reasoning process.

**TraceRepair (2026)**: TraceRepairDSV3.2 correctly resolves 392 defects (217 on v1.2 and 175 on v2.0), outperforming all compared methods in terms of the number of correctly fixed defects. This work offers a perspective on combining dynamic analysis with LLM-based repair, encouraging further exploration of execution-driven approaches.

**Feedback-Driven Approaches**: Lightweight conversational loops, exemplified by ChatRepair, feed failing assertions back to the LLM and regenerate patches in the loop. Additionally, Analysis-augmented pipelines invoke compilers, debuggers, or security analyzers to feed diagnostics or traces that steer regeneration toward the root cause.

**DynaFix (2025)**: DynaFix is an execution-level dynamic information-driven APR method that iteratively leverages runtime information to refine the repair process, capturing execution-level dynamic information such as variable states, control-flow paths, and call stacks.

## Research Trends

A curated collection of 62 representative papers on LLM-based Automated Program Repair is organized by sub-paradigm, spanning from January 2022 to October 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3a61701-6891-4682-b0ce-93b29f28a645",
  "isSidechain": true,
  "promptId": "5c7d4218-6234-48e7-a63c-54cbc067a333",
  "agentId": "ae184d7f2b108c704",
  "type": "user",
  "uuid": "d5e78098-c73e-4f6e-8c8b-374f78426c55",
  "sourceToolAssistantUUID": "b3a61701-6891-4682-b0ce-93b29f28a645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T05:54:07.962Z_

<details><summary>↩ Tool result · `toolu_01JPcjmZtuorqLwHzQrEqD6H`</summary>

```text
Web search results for query: "RL reward signal SWE-bench docker execution"

Links: [{"title":"SWE-World: Building Software Engineering Agents in Docker-Free Environments","url":"https://arxiv.org/html/2602.03419v1"},{"title":"GitHub - RUCAIBox/SWE-World · GitHub","url":"https://github.com/RUCAIBox/SWE-World"},{"title":"Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards","url":"https://arxiv.org/html/2508.10548"},{"title":"Nanbeige SWE-World: Building Software Engineering Agents in","url":"https://arxiv.org/pdf/2602.03419"},{"title":"DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL","url":"https://www.together.ai/blog/deepswe"},{"title":"SWE-MiniSandbox: Container-Free Reinforcement Learning for Building Software Engineering Agents","url":"https://arxiv.org/html/2602.11210"},{"title":"RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale","url":"https://arxiv.org/html/2508.01550"},{"title":"ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents","url":"https://arxiv.org/html/2603.18815v1"},{"title":"SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution","url":"https://arxiv.org/html/2502.18449v1"},{"title":"GitHub - multi-swe-bench/multi-swe-bench: Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving · GitHub","url":"https://github.com/multi-swe-bench/multi-swe-bench"}]

I found comprehensive results about RL reward signals and SWE-bench Docker execution. Here's what the search revealed:

## Key Findings

### Docker-Free vs. Docker-Based Approaches

Upon episode termination, when the agent submits its final code patch, an LLM-based reward model replaces containerized test execution by acting as a virtual test runner that evaluates the patch and produces structured test feedback together with a binary success signal. This represents a significant shift in how reward signals are generated for SWE-bench tasks.

### Reward Signal Design

A robust and faithful reward signal is critical for stable Docker-free reinforcement learning, and CoT provides an effective way to enhance it. The research shows that CoT provides asymmetric benefits: it yields only marginal gains for SWT, but substantially improves SWR's reward prediction quality (Accuracy/Precision/Recall/F1), making the reward signal more reliable.

### Common Approaches

Different frameworks use various reward signal mechanisms:

- Successful execution of all tests yields a positive reward (pull request resolved), while test failures incur zero reward.
- RL training adopts a rule-based reward design with the detailed reward signal defined in Appendix A.1.
- Leveraging a lightweight rule-based reward (e.g., the similarity score between ground-truth and LLM-generated solutions), SWE-RL enables LLMs to autonomously recover a developer's reasoning processes and solutions.

### Infrastructure Challenges

During the final training run each RL iteration spawned 512 (BS=64, 8 passes) Docker containers in parallel. The demanding nature of RL, together with parallel experiments, generated thousands of containers at any given time, overloading Docker's API server and eventually crashing the Docker daemon (dockerd).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "692b5909-571c-4840-b4fd-e1d0c28c06eb",
  "isSidechain": true,
  "promptId": "5c7d4218-6234-48e7-a63c-54cbc067a333",
  "agentId": "ae184d7f2b108c704",
  "type": "user",
  "uuid": "2745debd-8f09-48a7-9900-05d966d476d1",
  "sourceToolAssistantUUID": "692b5909-571c-4840-b4fd-e1d0c28c06eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T05:55:19.311Z_

Here is a comprehensive landscape of competing and concurrent work that overlaps with the "RL-CoTest" idea of co-training a test generator and fixer with RL for repo-level code repair. I have organized the results by relevance, from the most directly overlapping work to more tangentially related efforts.

---

## TIER 1: Directly Competing / Near-Identical Ideas

These papers are doing essentially the same thing as RL-CoTest -- co-training or adversarially evolving a test generator and a code fixer/coder using RL.

### 1. CURE: Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning
- **Venue:** arXiv (June 2025), also on OpenReview
- **Description:** A reinforcement learning framework that co-evolves coding and unit test generation capabilities within a single model based on their interaction outcomes, without ground-truth code supervision. The code generator provides supervision for the unit test generator, while simultaneously improving itself. This is very close to the RL-CoTest concept.
- [arXiv page](https://arxiv.org/abs/2506.03136) | [OpenReview](https://openreview.net/forum?id=wPdBe9zxNr)

### 2. Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning
- **Venue:** arXiv (March 2026)
- **Description:** Orchestrates adversarial co-evolution of a Code LLM and a Test LLM as two separate models with opposing objectives. Explicitly decouples code and test generation to avoid self-collusion that arises from self-play. This directly addresses the same two-agent co-training paradigm.
- [arXiv page](https://arxiv.org/html/2603.15611)

### 3. UTRL: Learning to Generate Unit Test via Adversarial Reinforcement Learning
- **Venue:** arXiv (August 2025)
- **Description:** Iteratively trains two LLMs (unit test generator and code generator) in an adversarial manner via RL. The test generator maximizes a discrimination reward (produce tests that reveal faults), while the code generator maximizes a code reward (produce solutions that pass tests). Very close to RL-CoTest's dual-agent structure.
- [arXiv page](https://arxiv.org/abs/2508.21107)

### 4. ATGen: Adversarial Reinforcement Learning for Test Case Generation
- **Venue:** arXiv (October 2025)
- **Description:** Uses adversarial RL specifically for test case generation, pitting a test generator against a code generator.
- [arXiv page](https://arxiv.org/html/2510.14635v1)

### 5. FixAudit: An Iterative Test-and-Repair Framework for Competitive Code Generation
- **Venue:** arXiv (April 2026)
- **Description:** Trains two roles (Fixer and Auditor) within a single shared model. The Auditor generates tests targeting specific bugs in candidate code, and the Fixer performs localized repair. Uses a four-stage training pipeline: execution-aligned SFT followed by three stages of RL (initial repair, test generation, closed-loop refinement). This is arguably the closest to RL-CoTest applied to repair rather than just code generation.
- [arXiv page](https://arxiv.org/html/2604.05560)

---

## TIER 2: RL for SWE-bench / Repo-Level Code Repair (without explicit test co-training)

These papers apply RL to repo-level repair tasks (SWE-bench), which is the same target domain as RL-CoTest, but may not co-train a test generator.

### 6. SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution
- **Venue:** arXiv (February 2025), OpenReview
- **Description:** The first approach to scale RL-based LLM reasoning for real-world software engineering. Uses a lightweight rule-based reward (similarity between ground-truth and LLM-generated solutions) to enable LLMs to autonomously recover developer reasoning processes.
- [arXiv page](https://arxiv.org/html/2502.18449v1) | [OpenReview](https://openreview.net/forum?id=ULblO61XZ0)

### 7. Self-play SWE-RL (SSR)
- **Venue:** arXiv (December 2025)
- **Description:** Trains LLM agents via RL in a self-play setting to iteratively inject and repair software bugs of increasing complexity. Achieves +10.4 on SWE-bench Verified and +7.8 on SWE-Bench Pro. The self-play mechanism (inject bug, then repair it) is a different form of co-training.
- [arXiv page](https://arxiv.org/abs/2512.18552)

### 8. DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL
- **Venue:** Together AI blog / arXiv (2025-2026)
- **Description:** Trains from Qwen3-32B with only RL, achieves 59% on SWE-Bench-Verified with test-time scaling (42.2% Pass@1). Just 200 steps of RL training boosts score from 23% to 42%.
- [Together AI blog](https://www.together.ai/blog/deepswe)

### 9. RepoForge: Training a SOTA Fast-thinking SWE Agent with End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale
- **Venue:** arXiv (August 2025)
- **Description:** Combines SFT and RL at scale for SWE agent training with an end-to-end data curation pipeline.
- [arXiv page](https://arxiv.org/html/2508.01550)

### 10. Agentic Reinforcement Learning for Real-World Code Repair
- **Venue:** arXiv (October 2025) / Cerebras blog
- **Description:** Structures repair as a multi-turn decision-making process using agentic RL. Extends OpenHands for real-world code repair tasks.
- [arXiv page](https://arxiv.org/html/2510.22075) | [Cerebras blog](https://www.cerebras.ai/blog/scaling-code-repair-agents-with-reinforcement-learning-extending-openhands-for-real-world)

---

## TIER 3: Test Generation for Repo-Level Repair (without RL co-training)

These papers generate tests to guide repo-level repair but do not use RL to co-train the generator and fixer.

### 11. Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints
- **Venue:** arXiv (April 2026)
- **Description:** Treats tests as dynamic constraints that guide and are revised by the repair process. Candidate code and test artifacts progressively narrow behavior space through mutual evaluation and semantic recombination. Produces both code patches and test patches. This is conceptually very similar to RL-CoTest but may not use RL for the co-evolution.
- [arXiv page](https://arxiv.org/html/2604.04580)

### 12. Dynamic Cogeneration of Bug Reproduction Test in Agentic Program Repair
- **Venue:** arXiv (January 2026)
- **Description:** Co-generates bug reproduction tests alongside program repair in an agentic setting.
- [arXiv page](https://arxiv.org/html/2601.19066v1)

### 13. Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection
- **Venue:** arXiv (August 2025)
- **Description:** Focuses on generating and selecting tests for SWE-bench issues using heterogeneous prompting and execution feedback.
- [arXiv page](https://arxiv.org/html/2508.06365)

### 14. TestART: Improving LLM-based Unit Testing via Co-evolution of Automated Generation and Repair Iteration
- **Venue:** arXiv (August 2024)
- **Description:** Co-evolves test generation and repair through iterative template-based repair of LLM-generated test cases. Does not use RL but the co-evolution framing is relevant.
- [arXiv page](https://arxiv.org/abs/2408.03095)

### 15. RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair
- **Venue:** arXiv (March 2026)
- **Description:** Documentation-enhanced approach for repo-level fault localization and repair. Achieves 45.7% on SWE-bench Lite at $0.44/fix.
- [arXiv page](https://arxiv.org/abs/2603.01048)

---

## TIER 4: Execution Feedback / RL Infrastructure for Code Repair

### 16. RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning
- **Venue:** arXiv (October 2024), OpenReview
- **Description:** Uses PPO-trained LLM agents receiving execution results during iterative code generation. Achieves SOTA on CodeContests, HumanEval+, and MBPP+. The execution-as-reward-signal paradigm is foundational to RL-CoTest.
- [arXiv page](https://www.arxiv.org/pdf/2410.02089) | [OpenReview](https://openreview.net/forum?id=PzSG5nKe1q)

### 17. SWE-World / SWE-MiniSandbox: Docker-Free RL Environments
- **Venue:** arXiv (February 2026)
- **Description:** SWE-World replaces containerized test execution with an LLM-based reward model as a virtual test runner. SWE-MiniSandbox provides container-free RL for SWE agents. Relevant to the infrastructure challenges of RL-CoTest.
- [SWE-World](https://arxiv.org/html/2602.03419v1) | [SWE-MiniSandbox](https://arxiv.org/html/2602.11210)

### 18. SWE-rebench-V2: Language-Agnostic SWE Task Collection at Scale
- **Venue:** arXiv / Nebius (February 2026)
- **Description:** 32,000+ executable tasks with pre-built Docker environments across 20 programming languages. A training data resource for RL-based SWE agents.
- [arXiv page](https://arxiv.org/abs/2602.23866) | [Nebius blog](https://nebius.com/blog/posts/meet-swe-rebench-v2)

### 19. ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents
- **Venue:** arXiv (March 2026)
- **Description:** Infrastructure for RL training of multi-turn LLM agents, directly relevant to the scalability challenges of running Docker-based RL loops.
- [arXiv page](https://arxiv.org/html/2603.18815v1)

### 20. TraceRepair / TRACE: Execution-Feedback-Guided Repair
- **Venue:** arXiv (April 2026) / ScienceDirect (2026)
- **Description:** TraceRepair uses runtime execution traces with multi-agent debate for repair. TRACE is a template-guided reasoning framework integrating execution feedback. Not RL-based but relevant to the feedback-loop paradigm.
- [TraceRepair](https://arxiv.org/html/2604.02647v1) | [TRACE](https://www.sciencedirect.com/science/article/abs/pii/S0950584926000479)

### 21. Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards
- **Venue:** arXiv (August 2025)
- **Description:** Addresses reward stability in multi-turn RL for code agents, which is a key technical challenge for any RL-CoTest-style system.
- [arXiv page](https://arxiv.org/html/2508.10548)

---

## Key Surveys

### 22. A Systematic Literature Review on LLMs for Automated Program Repair [TOSEM 2026]
- 115 publications analyzed. Covers the full landscape.
- [GitHub](https://github.com/iSEngLab/AwesomeLLM4APR) | [arXiv](https://arxiv.org/html/2405.01466v4)

### 23. Can test cases generated by LLMs facilitate automated program repair? [EMSE 2026]
- Empirical study on whether LLM-generated tests improve repair outcomes.
- [Springer](https://link.springer.com/article/10.1007/s10664-026-10802-w)

### 24. A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications
- 62 papers curated, organized by sub-paradigm.
- [arXiv](https://arxiv.org/html/2506.23749v1)

---

## Summary Assessment

The space is **crowded and fast-moving**. The most dangerous competitors to RL-CoTest are:

1. **CURE** (June 2025) -- co-evolves coder + tester with RL, single model. Very close match.
2. **Code-A1** (March 2026) -- adversarial co-evolution of separate Code LLM and Test LLM. Explicitly addresses self-collusion. Very close match.
3. **UTRL** (August 2025) -- adversarial RL with two LLMs (test gen + code gen). Very close match.
4. **FixAudit** (April 2026) -- single-model Fixer+Auditor with 4-stage RL pipeline including closed-loop refinement. Closest match for the *repair* setting specifically.
5. **Beyond Fixed Tests** (April 2026) -- coevolution of code and tests for repo-level issue resolution. Close conceptual match, may or may not use RL.

The key differentiator for RL-CoTest would need to be either: (a) applying the co-training paradigm specifically to **repo-level repair** (SWE-bench) rather than competitive programming, (b) a novel reward design or training procedure, or (c) demonstrating that co-training outperforms the single-model approaches (like FixAudit) on real-world benchmarks. Papers 1-4 above mostly evaluate on competitive programming benchmarks (APPS, MBPP, HumanEval), not SWE-bench, so there may still be a gap for repo-level application -- but paper 11 ("Beyond Fixed Tests") is closing that gap without RL.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2745debd-8f09-48a7-9900-05d966d476d1",
  "isSidechain": true,
  "agentId": "ae184d7f2b108c704",
  "requestId": "req_011Cb5jG3ojdDgZvCGL6BK6b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89a721b1-134a-47cd-9d35-758b14b13fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d049a72e-f744-45a0-a48a-2e56e759ae29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9bksrctvEqdQJbvCpDve8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2760,
      "cache_creation_input_tokens": 5121,
      "cache_read_input_tokens": 9504,
      "output_tokens": 3683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2760,
          "output_tokens": 3683,
          "cache_read_input_tokens": 9504,
          "cache_creation_input_tokens": 5121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5121,
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
