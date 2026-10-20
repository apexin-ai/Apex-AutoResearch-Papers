# Research conversation: I'm reviewing a paper idea that distills data-flow (def-use) signals into a lightweight neural model for repository-leve

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a1c6187e43302749f.jsonl`
- **Structured JSON:** [`140704fab1156a23fbcd.json`](../../sessions/14/140704fab1156a23fbcd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-10T18:40:38.306Z_

I'm reviewing a paper idea that distills data-flow (def-use) signals into a lightweight neural model for repository-level code repair context selection. I need to find competing or closely related work that the authors may have missed.

Search for the following using WebSearch:
1. "data-flow context selection code repair 2025 2026 site:arxiv.org"
2. "def-use analysis neural code understanding 2025 2026"
3. "code property graph context pruning LLM 2025 2026"
4. "repository level fault localization graph neural 2025 2026"
5. "program analysis guided code generation context 2025 2026"
6. Search for "CodeQL code repair" or "CodeQL LLM" to see if anyone has used CodeQL for similar purposes
7. Search for any work combining BM25/retrieval with structural code features for code tasks

Report all relevant papers you find, with titles, venues, and brief descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "92b5214b-c007-4e30-a46e-78442b457134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:40:38.309Z_

```json
{
  "parentUuid": "92b5214b-c007-4e30-a46e-78442b457134",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
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
  "uuid": "d2bc550c-51e1-4b0a-947e-2369b864ad30",
  "timestamp": "2026-05-10T18:40:38.309Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:40:41.773Z_



I'll search for all these topics in parallel to find related work efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2bc550c-51e1-4b0a-947e-2369b864ad30",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNrhc3jjE7BVry1UpwD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebc8b429-a8af-4e62-933b-28a4dc9056fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mi3ofTJdruraTH3veFdQuz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 768,
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

_source line 4 · 2026-05-10T18:40:41.890Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01P3jJncghCQEHhYpu6mBVWE`</summary>

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
  "parentUuid": "ebc8b429-a8af-4e62-933b-28a4dc9056fd",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNrhc3jjE7BVry1UpwD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a9f5075-3ae0-40b8-af77-249fa5255ba9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mi3ofTJdruraTH3veFdQuz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 8223,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 768
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 768,
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

_source line 5 · 2026-05-10T18:40:41.893Z_

<details><summary>↩ Tool result · `toolu_01P3jJncghCQEHhYpu6mBVWE`</summary>

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
  "parentUuid": "7a9f5075-3ae0-40b8-af77-249fa5255ba9",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "3670d624-94b6-4e4d-9c91-f843dcaba2fa",
  "sourceToolAssistantUUID": "7a9f5075-3ae0-40b8-af77-249fa5255ba9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:40:44.377Z_



Now let me run all seven searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3670d624-94b6-4e4d-9c91-f843dcaba2fa",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNryARc2NTyyuLscWxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b8cb5c9-686a-4d67-b7f7-ab2be95cb3ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TWYXC7VmVFcsbKk8RoNbx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 7 · 2026-05-10T18:40:45.385Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014TiscJzYGFhNdtMYW8yo3n`</summary>

```json
{
  "query": "data-flow context selection code repair 2025 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b8cb5c9-686a-4d67-b7f7-ab2be95cb3ca",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNryARc2NTyyuLscWxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "347cbb00-aa4a-4268-a440-d47cf5f2cffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TWYXC7VmVFcsbKk8RoNbx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 8 · 2026-05-10T18:40:45.853Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0176WtoPYDv5hDTT1MZ46zCZ`</summary>

```json
{
  "query": "def-use analysis neural code understanding 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "347cbb00-aa4a-4268-a440-d47cf5f2cffc",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNryARc2NTyyuLscWxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23c1f0d9-67dd-44f1-b67e-5d81172f6646",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TWYXC7VmVFcsbKk8RoNbx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 9 · 2026-05-10T18:40:46.796Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Mg6XKfLid9h9ZucA3Yc2A`</summary>

```json
{
  "query": "code property graph context pruning LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23c1f0d9-67dd-44f1-b67e-5d81172f6646",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNryARc2NTyyuLscWxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3379257a-9192-4e1c-b373-4b325a97b2f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TWYXC7VmVFcsbKk8RoNbx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 10 · 2026-05-10T18:40:47.274Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H748CKWHow49Y2zRH5c4hT`</summary>

```json
{
  "query": "repository level fault localization graph neural 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3379257a-9192-4e1c-b373-4b325a97b2f9",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNryARc2NTyyuLscWxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dca3a6db-afe0-47b8-b538-b01bb07cc6ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TWYXC7VmVFcsbKk8RoNbx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 11 · 2026-05-10T18:40:47.737Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RQCjFosMygKQrKjUhUjJAT`</summary>

```json
{
  "query": "program analysis guided code generation context 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dca3a6db-afe0-47b8-b538-b01bb07cc6ed",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNryARc2NTyyuLscWxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b55e9c58-b34e-4e27-9613-e65adc7bfd03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TWYXC7VmVFcsbKk8RoNbx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 12 · 2026-05-10T18:40:48.719Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S6nNSjBfqpvd1VKaJ8uQZf`</summary>

```json
{
  "query": "CodeQL code repair LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b55e9c58-b34e-4e27-9613-e65adc7bfd03",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNryARc2NTyyuLscWxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77ae7cc9-78ef-4ef8-8d06-2c954ff7bc64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TWYXC7VmVFcsbKk8RoNbx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 13 · 2026-05-10T18:40:49.157Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012cSFLuqiKDCyLcgMjPaMoe`</summary>

```json
{
  "query": "BM25 retrieval structural code features code repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77ae7cc9-78ef-4ef8-8d06-2c954ff7bc64",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNryARc2NTyyuLscWxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f05e54dc-860b-4462-b901-7bfc1cb432df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TWYXC7VmVFcsbKk8RoNbx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8991,
      "output_tokens": 370,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1409
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 370,
          "cache_read_input_tokens": 8991,
          "cache_creation_input_tokens": 1409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1409,
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

_source line 14 · 2026-05-10T18:40:52.729Z_

<details><summary>↩ Tool result · `toolu_014TiscJzYGFhNdtMYW8yo3n`</summary>

```text
Web search results for query: "data-flow context selection code repair 2025 2026 site:arxiv.org"

Links: [{"title":"A Survey of LLM-based Automated Program Repair","url":"https://arxiv.org/pdf/2506.23749"},{"title":"Dive into Claude Code: The Design Space of Today’s and Future AI Agent Systems","url":"https://arxiv.org/html/2604.14228v1"},{"title":"Towards an Understanding of Context Utilization in Code Intelligence","url":"https://arxiv.org/pdf/2504.08734"},{"title":"Detecting Performance-Relevant Changes in Configurable Software Systems","url":"https://arxiv.org/pdf/2511.17271"},{"title":"arXiv:2503.22625v1 [cs.SE] 28 Mar 2025 Challenges and Paths Towards","url":"https://arxiv.org/pdf/2503.22625"},{"title":"Computer Science Jan 2025","url":"https://www.arxiv.org/list/cs/2025-01?skip=6950&show=50"},{"title":"arXiv:2405.05455v1 [cs.SE] 8 May 2024","url":"https://arxiv.org/pdf/2405.05455"},{"title":"DSBC : Data Science task Benchmarking with Context engineering","url":"https://arxiv.org/html/2507.23336"},{"title":"[2512.01389] Syndrome-Flow Consistency Model Achieves One-step Denoising Error Correction Codes","url":"https://arxiv.org/abs/2512.01389"},{"title":"Feature-Interaction Aware Conﬁguration Prioritization for Conﬁgurable Code","url":"https://arxiv.org/pdf/1911.07779"}]

Based on the search results from arXiv, I found several relevant papers on code repair and context-related topics from 2025-2026. Here are the key findings:

## Primary Results

A survey of LLM-based automated program repair covering 63 systems published from January 2022 to June 2025 categorizes recent work into four paradigms and shows how retrieval- or analysis-augmented contexts strengthen them.

Analysis artifacts used in code repair typically appear in three forms: failing-test evidence that exposes runtime failures, semantics-aware slices that prune unrelated code, and concise execution traces that embed dynamic behavior, with systems like D4C, Appatch, and TracePrompt representing each approach.

## Context Selection and Data Flow

Context selection is identified as a key architectural layer in coding agents, activated alongside tool invocation, permission checks, iterative repair, delegation, and session persistence.

Researchers have embedded abstract syntax trees, data flow graphs, and program dependency graphs to capture local and global context for bug detection.

## Recent Challenges

Richer semantic, dynamic, historical, and inter-procedural dependency graph contexts can materially improve LLM-based repair, though the cost of gathering and encoding such information remains significant, and ever-longer inputs challenge current context windows.

The search results also include a 2026 paper on Claude Code's architecture that discusses context selection in AI agent systems for code repair tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "347cbb00-aa4a-4268-a440-d47cf5f2cffc",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "2e41b56d-cc2d-4f19-a7b2-4cfac2603acf",
  "sourceToolAssistantUUID": "347cbb00-aa4a-4268-a440-d47cf5f2cffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T18:40:53.686Z_

<details><summary>↩ Tool result · `toolu_0176WtoPYDv5hDTT1MZ46zCZ`</summary>

```text
Web search results for query: "def-use analysis neural code understanding 2025 2026"

Links: [{"title":"Cracking the Brain's Code: Unlocking Neuron Memory to Advance AI - USC Viterbi | School of Engineering","url":"https://viterbischool.usc.edu/news/2026/02/cracking-the-brains-code-unlocking-neuron-memory-to-advance-ai/"},{"title":"Neural Methods for Programming: A Comprehensive Survey and Future Directions","url":"https://www.mdpi.com/2076-3417/15/22/12150"},{"title":"Mechanistic Interpretability Workshop at ICML 2026","url":"https://mechinterpworkshop.com/"},{"title":"Cracking the code: How neural networks might actually “think” | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/04/22/how-neural-networks-might-actually-think"},{"title":"Neural population activity for memory: Properties, computations, and codes - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0896627325008542"},{"title":"NeurIPS: Neural Information Processing Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2212"},{"title":"Mechanistic Interpretability Workshop at NeurIPS 2025","url":"https://mechinterpworkshop.com/neurips2025/"},{"title":"Introducing the Evaluations & Datasets Track at NeurIPS 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/03/23/introducing-the-evaluations-datasets-track-at-neurips-2026/"},{"title":"A survey on neuro-mimetic deep learning via predictive coding - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S089360802501041X"},{"title":"Fei-Fei, Adeli, Durante, Johnson, Xiang Lecture 7 - April 21, 2025 1 Lecture 7:","url":"https://cs231n.stanford.edu/slides/2026/lecture_7.pdf"}]

Based on the search results, here's what I found regarding neural code understanding and related topics in 2025-2026:

## Neural Methods for Programming

The advancement of neural-based models has driven significant progress in modern code intelligence, accelerating the development of intelligent programming tools such as code assistants and automated software engineering systems. A comprehensive survey of neural methods for programming tasks has been published within the broader context of software development. The analysis spans 18 major programming tasks, including code generation, code translation, code clone detection, code classification, and vulnerability detection.

## Recent Research on Neural Networks and Code Understanding

The survey synthesizes insights from more than 250 scientific papers, the majority of which were published between 2015 and 2025, with earlier foundational works dating back to the late 1990s included for historical context.

## Neural Network Interpretability 

In related areas, mechanistic interpretability addresses the challenge by developing principled methods to analyze and understand a model's internals–weights and activations–and to use this understanding to gain greater insight into its behavior. The field has grown rapidly, with sizable communities in academia, industry and independent research, dedicated startups, and a rich ecosystem of tools and techniques.

The search results show active ongoing research in neural methods for code understanding and related interpretability work in 2025-2026, though the specific topic of "def-use analysis" in neural code understanding contexts was not prominent in these particular results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23c1f0d9-67dd-44f1-b67e-5d81172f6646",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "af4deaa8-2c1e-4817-bcd5-b93a41844d26",
  "sourceToolAssistantUUID": "23c1f0d9-67dd-44f1-b67e-5d81172f6646",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:40:54.565Z_

<details><summary>↩ Tool result · `toolu_015Mg6XKfLid9h9ZucA3Yc2A`</summary>

```text
Web search results for query: "code property graph context pruning LLM 2025 2026"

Links: [{"title":"LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models | USENIX","url":"https://www.usenix.org/conference/usenixsecurity25/presentation/lekssays"},{"title":"The LLM context problem in 2026: strategies for memory, relevance, and scale - LogRocket Blog","url":"https://blog.logrocket.com/llm-context-problem-strategies-2026/"},{"title":"Bridging Code Property Graphs and Language Models for Program Analysis","url":"https://arxiv.org/html/2603.24837"},{"title":"LLM+Graph@VLDB’2025 Workshop Summary","url":"https://arxiv.org/html/2604.02861v2"},{"title":"CodexGraph: LLM-Driven Code Graphs","url":"https://www.emergentmind.com/topics/codexgraph"},{"title":"[2507.16585] LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models","url":"https://arxiv.org/abs/2507.16585"},{"title":"CODEXGRAPH: Bridging Large Language Models and ...","url":"https://aclanthology.org/2025.naacl-long.7.pdf"},{"title":"LLMxCPG: context-aware vulnerability detection through ...","url":"https://dl.acm.org/doi/10.5555/3766078.3766104"},{"title":"[Research] “LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models” Paper Review (EN) - hackyboiz","url":"https://hackyboiz.github.io/2025/09/22/l0ch/llmxcpg_paper_review/en/"},{"title":"Code-Generated Graph Representations Using Multiple LLM Agents for Material Properties Prediction | OpenReview","url":"https://openreview.net/forum?id=lvvMwGUam6&noteId=glxGx3Nq7y"}]

I've found several relevant results about code property graphs, context pruning, and LLMs from 2025-2026. Here's a summary of the key findings:

## Key Research Areas

### LLMxCPG: Context-Aware Vulnerability Detection
LLMxCPG is a novel framework integrating Code Property Graphs (CPG) with Large Language Models (LLM) for robust vulnerability detection. The most significant innovation is in context pruning: the CPG-based slice construction technique reduces code size by 67.84-90.93% while preserving vulnerability-relevant context. Empirical evaluation demonstrates LLMxCPG's effectiveness across verified datasets, achieving 15-40% improvements in F1-score over state-of-the-art baselines.

### CodeBadger: Repository-Level Program Analysis
CodeBadger enables LLMs to reason about code semantically across entire repositories, supporting vulnerability discovery, patching, and program comprehension at scale. This addresses the fundamental challenge that token limits prevent loading entire repositories, as modern codebases contain thousands of files and millions of lines of code, with an 8,000-method repository requiring hundreds of millions of tokens.

### CodexGraph: LLM-Driven Code Graphs
CodexGraph is a system that integrates LLM agents with property graph databases to enable multi-hop, structure-aware code retrieval and reasoning, employing a two-stage static analysis and a dual-agent workflow to construct and traverse a comprehensive code property graph.

### LLM Context Management in 2026
Successful production systems treat context engineering as a first-class discipline and deliberately filter, rank, prune, summarize, and isolate information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3379257a-9192-4e1c-b373-4b325a97b2f9",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "712753a4-069a-4074-9e78-76c9df669392",
  "sourceToolAssistantUUID": "3379257a-9192-4e1c-b373-4b325a97b2f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T18:40:54.709Z_

<details><summary>↩ Tool result · `toolu_01H748CKWHow49Y2zRH5c4hT`</summary>

```text
Web search results for query: "repository level fault localization graph neural 2025 2026"

Links: [{"title":"[2602.13921v1] GREPO: A Benchmark for Graph Neural Networks on Repository-Level Bug Localization","url":"https://arxiv.org/abs/2602.13921v1"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"Graph neural network for fault localization in sequence-based models | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10666-6"},{"title":"[2602.13921] GREPO: A Benchmark for Graph Neural Networks on Repository-Level Bug Localization","url":"https://arxiv.org/abs/2602.13921"},{"title":"Multi-view adaptive contrastive learning for information retrieval based fault localization | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00573-x"},{"title":"Graph-Based Deep Learning for Fault Localization in ...","url":"https://sprcopen.org/index.php/FAIR/article/download/270/277"},{"title":"Explainable Neural Network meets Graph Neural Network: Recent advances in process fault detection and diagnosis - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0098135425005319"},{"title":"CoverFL: Enhancing Fault Localization via Deep Coverage Relation | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3787964"},{"title":"Graph neural networks for the localization of faults in a partially observed regional transmission system - Rimkus - 2025 - Scandinavian Journal of Statistics - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/sjos.12763"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Special+Session:+Using+Graph+Neural+Networks+for+Tier-Level+Fault+Localization+in+Monolithic+3D+ICs+*."}]

I've found several relevant recent papers and research on repository-level fault localization using graph neural networks from 2025-2026:

## Key Research Findings

**GREPO: A Benchmark for GNN-Based Bug Localization (2026)**

GREPO is the first GNN benchmark for repository-scale bug localization tasks, comprising 86 Python repositories and 47,294 bug-fixing tasks with graph-based data structures ready for direct GNN processing. Graph Neural Networks offer a promising alternative for repository-level bug localization due to their ability to model complex, repository-wide dependencies.

**Fault Localization Granularity Research (2026)**

Recent research suggests that LLMs used for code repair exhibit an implicit bias toward the granularity of code at which they were pre-trained or instruction-tuned. This study examines the impact of different levels of fault localization granularity on repository-scale code repair tasks.

**Information Retrieval with Graph Neural Networks (2025-2026)**

A novel approach named MACL-IRFL was proposed to learn relationships for software fault localization by generating data augmentations from multiple views and adopting graph neural networks to aggregate information about bug reports and source code.

**Fault Localization in Sequence-Based Models (2025)**

LocatorGraph, a novel graph neural network-based framework, was designed to identify root causes of faults in sequence-based models and was published in Empirical Software Engineering in 2025.

These research efforts demonstrate significant progress in applying GNNs to repository-level fault localization, addressing the limitations of traditional approaches and LLMs with context window constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dca3a6db-afe0-47b8-b538-b01bb07cc6ed",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "23a84232-5afb-4220-a2e2-f7cced53b4a2",
  "sourceToolAssistantUUID": "dca3a6db-afe0-47b8-b538-b01bb07cc6ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T18:40:56.176Z_

<details><summary>↩ Tool result · `toolu_012cSFLuqiKDCyLcgMjPaMoe`</summary>

```text
Web search results for query: "BM25 retrieval structural code features code repair 2025 2026"

Links: [{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"Integrating Attention Mechanism with Code Structural Affinity and ...","url":"https://www.techscience.com/cmc/online/detail/25086/pdf"},{"title":"What is BM25 (Best Matching 25) Algorithm - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/what-is-bm25-best-matching-25-algorithm/"},{"title":"Dense vs Sparse Retrieval: Mastering FAISS, BM25, and Hybrid Search - DEV Community","url":"https://dev.to/qvfagundes/dense-vs-sparse-retrieval-mastering-faiss-bm25-and-hybrid-search-4kb1"},{"title":"BM25: Complete Guide to the Search Algorithm Behind Elasticsearch - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/bm25-search-algorithm-elasticsearch-implementation"},{"title":"BM25","url":"https://arpitbhayani.me/blogs/bm25/"},{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and ...","url":"https://aclanthology.org/2025.findings-acl.62.pdf"},{"title":"bm25 · GitHub Topics · GitHub","url":"https://github.com/topics/bm25"},{"title":"Retrieval Augmented Generation (RAG) 06 :- BM25 Retriever: When and Why to Use It (With Code Demo)? | by Yashwanth S | Medium","url":"https://medium.com/@yashwanths_29644/retrieval-augmented-generation-rag-06-bm25-retriever-when-and-why-to-use-it-with-code-demo-132ed70c6bfd"},{"title":"BM25 Retriever | LlamaIndex Python Documentation","url":"https://developers.llamaindex.ai/python/examples/retrievers/bm25_retriever/"}]

I found several relevant results combining BM25 retrieval with code-related applications. Here are the key findings:

## BM25 in Code Retrieval and Repair

BM25 retrieval achieves the best performance for code matching, and research from 2025-2026 demonstrates its effectiveness in code repair tasks.

### Recent Code Repair Applications (2025-2026)

Recent work uses BM25-retrieved buggy code/trace pairs as input to a Transformer encoder-decoder model, incorporating retrieved contexts into the encoder input for code repair. This approach combines structural features with retrieval:

- Replacing BM25 with random retrieval lowered accuracy to ~47%, demonstrating BM25's importance
- Performance peaked at k=5 retrieved contexts (62.3%), with little gain beyond

### Integration with Structural Code Features

Hybrid retrievers combine BM25 with dense retrievers initialized by GraphCodeBERT and further pre-trained using contrastive learning and semantics-preserving augmentations such as identifier renaming and dead code insertion.

### Software Engineering Tasks (2025)

For code file retrieval, BM25-retrieved file documentation is limited to 30 files within a 64K context window, showing practical application in real-world software engineering benchmarks like SWE-Bench.

The search results show that BM25 remains a practical and effective component in modern code repair and retrieval systems, often combined with neural methods for enhanced performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f05e54dc-860b-4462-b901-7bfc1cb432df",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "21f82cd2-f2de-4426-b8f3-aad4788c0d58",
  "sourceToolAssistantUUID": "f05e54dc-860b-4462-b901-7bfc1cb432df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T18:40:59.318Z_

<details><summary>↩ Tool result · `toolu_01RQCjFosMygKQrKjUhUjJAT`</summary>

```text
Web search results for query: "program analysis guided code generation context 2025 2026"

Links: [{"title":"CGO: Symposium on Code Generation and Optimization 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=429"},{"title":"TYPE Original Research PUBLISHED 17 October 2025 DOI 10.3389/frai.2025.1660912","url":"https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1660912/pdf"},{"title":"Frontiers | Editorial: Advancing AI-driven code generation and synthesis: challenges, metrics, and ethical implications","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1816684/full"},{"title":"CGO 2025 – Proceedings","url":"https://www.conference-publishing.com/toc/CGO25/noabs"},{"title":"2026 Agentic Coding Trends Report How coding agents are reshaping","url":"https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf?hsLang=en"},{"title":"Performance and interpretability analysis of code generation large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0925231225021332"},{"title":"AI coding is now everywhere. But not everyone is convinced. | MIT Technology Review","url":"https://www.technologyreview.com/2025/12/15/1128352/rise-of-ai-coding-developers-2026/"},{"title":"AI Code Generators: The Future of Software Development","url":"https://zencoder.ai/blog/ai-code-generators-future-software-development"},{"title":"Program - CGO 2026","url":"https://2026.cgo.org/program/program-cgo-2026/"},{"title":"CGO 2025 - Main Conference - CGO 2025","url":"https://2025.cgo.org/track/cgo-2025-papers"}]

Based on the web search results, here's what I found regarding program analysis guided code generation in the 2025-2026 context:

## Recent Developments in Code Generation with Program Analysis

### Integration of Program Analysis Techniques

Recent approaches combine backtracking algorithms with program analysis techniques, allowing models to revise and refine generated code iteratively, resulting in more robust and accurate code output that better meets developer specifications.

### Context-Aware Code Generation

Advanced platforms offer embedded agents that can analyze repository structure and refine output iteratively using syntactic and semantic analysis, conducting deep analysis of entire codebases to understand project context, patterns, and conventions.

### LLM-Based Code Generation Advances

Recent advances in large language models have substantially expanded the scope of program synthesis, enabling systems that generate executable code directly from natural language descriptions. However, LLM-based systems often struggle with complex programming tasks that require precise interpretation of problem intent, multi-step reasoning, and iterative refinement.

### Interactive and Self-Improving Methodologies

TiCoder is an interactive workflow that uses LLM-generated tests to clarify user intent and improve code generation accuracy by 45.97% through guided intent clarification. Additionally, when code fails, the LLM uses self-reflection to identify errors, review its output, and utilize test results to guide revisions, with this cycle continuing until a successful solution is found or a maximum number of iterations is reached.

### Context Window Limitations

A significant challenge remains: LLMs can hold only a limited amount of information in their context window—essentially their working memory—meaning they struggle to parse large code bases and are prone to forgetting what they're doing on longer tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b55e9c58-b34e-4e27-9613-e65adc7bfd03",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "0bc02403-a199-40dc-af18-9da296a6fbf4",
  "sourceToolAssistantUUID": "b55e9c58-b34e-4e27-9613-e65adc7bfd03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T18:40:59.521Z_

<details><summary>↩ Tool result · `toolu_01S6nNSjBfqpvd1VKaJ8uQZf`</summary>

```text
Web search results for query: "CodeQL code repair LLM 2025 2026"

Links: [{"title":"Code Generation Security in LLMs: A Hybrid Detection and Post ...","url":"http://poster-openaccess.com/files/ICIC2025/2583.pdf"},{"title":"An evaluation study of large language models for addressing code quality issues | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-026-10858-8"},{"title":"CQLLM: A Framework for Generating CodeQL Security Vulnerability Detection Code Based on Large Language Model","url":"https://www.mdpi.com/2076-3417/16/1/517"},{"title":"CodeQL documentation - GitHub","url":"https://codeql.github.com/docs/"},{"title":"Guiding AI to Fix Its Own Flaws: An Empirical Study on LLM-Driven Secure Code Generation","url":"https://arxiv.org/html/2506.23034v1"},{"title":"GitHub - github/codeql: CodeQL: the libraries and queries that power security researchers around the world, as well as code scanning in GitHub Advanced Security · GitHub","url":"https://github.com/github/codeql"},{"title":"CodeQL","url":"https://codeql.github.com/"},{"title":"CodeQL 2.23.5 (2025-11-13) — CodeQL","url":"https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.5/"},{"title":"iris: llm-assisted static analysis for detecting security ...","url":"https://arxiv.org/pdf/2405.17238"},{"title":"CORE: Resolving Code Quality Issues using LLMs","url":"https://dl.acm.org/doi/pdf/10.1145/3643762"}]

I've completed the web search for "CodeQL code repair LLM 2025 2026". Here are the key findings:

## Recent Research on CodeQL and LLM-Based Code Repair

### Hybrid Vulnerability Detection and Repair Framework (2025)
A hybrid framework integrates static analysis (Bandit/CodeQL), dynamic fuzzing (AFL++), and syntax-aware repair rules to mitigate vulnerabilities in LLM-generated code without requiring model retraining. The framework achieved a 68.2% reduction in vulnerabilities while preserving 92.1% functional integrity across four state-of-the-art LLMs.

### CORE System for Code Quality Issues
A system targets issues reported by rule-based analyzers such as CodeQL, automatically filtering out suggestions that fail to satisfy the original rules. CORE achieved strong results on the Python benchmark (CQPy), successfully revising 88.81% of Python files such that they passed all relevant CodeQL static checks.

### CQLLM Framework (January 2026)
CQLLM is a novel framework for automating the generation of CodeQL security vulnerability detection code by leveraging LLM. While CodeQL stands as the premier static code analysis tool currently available on the market, its high barrier to entry poses challenges, and LLMs often face issues such as syntactic inaccuracies and references to non-existent modules.

### Post-hoc Vulnerability Repair with Explained Feedback (2025)
Researchers propose to perform post-hoc vulnerable code repair with explanations of direct CodeQL feedback, feeding the direct feedback from CodeQL along with contextual information to GPT-4o to explain the feedback and provide actionable suggestions for code repair.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77ae7cc9-78ef-4ef8-8d06-2c954ff7bc64",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "d691cf93-d7b4-4981-85ff-c97c324dc5c2",
  "sourceToolAssistantUUID": "77ae7cc9-78ef-4ef8-8d06-2c954ff7bc64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T18:41:02.764Z_

Let me run a few more targeted searches to fill in gaps and find additional specific papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d691cf93-d7b4-4981-85ff-c97c324dc5c2",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNtHgBoPxajuheLKSPV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e4eb528-d7fe-4d37-a653-c71c0e4f9297",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BdoJrbzBGw1mVXKBdXEiHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 5974,
      "cache_read_input_tokens": 10400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5974,
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

_source line 22 · 2026-05-10T18:41:03.966Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L2snY9DwUKAJo8gEh7AurG`</summary>

```json
{
  "query": "CodexGraph bridging code property graphs language models program analysis arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e4eb528-d7fe-4d37-a653-c71c0e4f9297",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNtHgBoPxajuheLKSPV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8ea0dba-379b-40ad-b328-fb34985a59b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BdoJrbzBGw1mVXKBdXEiHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 5974,
      "cache_read_input_tokens": 10400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5974,
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

_source line 23 · 2026-05-10T18:41:04.659Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pujq4z3XiMyQCvXJbPxtEa`</summary>

```json
{
  "query": "GREPO benchmark graph neural network repository bug localization arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8ea0dba-379b-40ad-b328-fb34985a59b7",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNtHgBoPxajuheLKSPV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10c996f9-71d1-41a8-bd8f-d0f414eea08f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BdoJrbzBGw1mVXKBdXEiHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 5974,
      "cache_read_input_tokens": 10400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5974,
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

_source line 24 · 2026-05-10T18:41:05.720Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013YVjbrYRWj5mhdoseKv5Ku`</summary>

```json
{
  "query": "data flow graph distillation code repair lightweight model 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10c996f9-71d1-41a8-bd8f-d0f414eea08f",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNtHgBoPxajuheLKSPV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03b6fd22-6d7a-4bae-9f1d-9a417cecc43d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BdoJrbzBGw1mVXKBdXEiHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 5974,
      "cache_read_input_tokens": 10400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5974,
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

_source line 25 · 2026-05-10T18:41:06.208Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T9TMFhYHwKaFJchdbk38uJ`</summary>

```json
{
  "query": "program slicing LLM code repair context window 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03b6fd22-6d7a-4bae-9f1d-9a417cecc43d",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNtHgBoPxajuheLKSPV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00106fd0-d38c-46a8-8061-16a3f4efab0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BdoJrbzBGw1mVXKBdXEiHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 5974,
      "cache_read_input_tokens": 10400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5974,
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

_source line 26 · 2026-05-10T18:41:07.091Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XtrkshSsBdWPJkBUPkD6ej`</summary>

```json
{
  "query": "SWE-Fixer repository level bug fix retrieval augmented 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00106fd0-d38c-46a8-8061-16a3f4efab0e",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNtHgBoPxajuheLKSPV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4043811f-da41-46ae-aa0d-325f769a793f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BdoJrbzBGw1mVXKBdXEiHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 5974,
      "cache_read_input_tokens": 10400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5974,
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

_source line 27 · 2026-05-10T18:41:10.747Z_

<details><summary>↩ Tool result · `toolu_01L2snY9DwUKAJo8gEh7AurG`</summary>

```text
Web search results for query: "CodexGraph bridging code property graphs language models program analysis arxiv 2025"

Links: [{"title":"[2603.24837] Bridging Code Property Graphs and Language Models for Program Analysis","url":"https://arxiv.org/abs/2603.24837"},{"title":"Bridging Code Graphs and Large Language Models for Better Code Understanding","url":"https://arxiv.org/html/2512.07666v1"},{"title":"[2408.03910] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910"},{"title":"Bridging Code Property Graphs and Language Models for Program Analysis","url":"https://arxiv.org/html/2603.24837v1"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/html/2408.03910v2"},{"title":"CODEXGRAPH: Bridging Large Language Models and ...","url":"https://aclanthology.org/2025.naacl-long.7.pdf"},{"title":"CODEXGRAPH: Bridging Large Language Models","url":"https://arxiv.org/pdf/2408.03910v2"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/codexgraph-bridging-large-language-models-code-repositories"},{"title":"[2408.03910v2] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910v2"},{"title":"(PDF) Bridging Code Property Graphs and Language Models for Program Analysis","url":"https://www.researchgate.net/publication/403193710_Bridging_Code_Property_Graphs_and_Language_Models_for_Program_Analysis"}]

Based on the search results, I found several relevant papers on bridging code property graphs and language models:

## CodexGraph (2024)

CodexGraph is a system that integrates LLM agents with graph database interfaces extracted from code repositories. By leveraging the structural properties of graph databases and the flexibility of the graph query language, CodexGraph enables the LLM agent to construct and execute queries, allowing for precise, code structure-aware context retrieval and code navigation.

CodexGraph utilizes static analysis to extract code graphs from repositories using a task-agnostic schema that defines the nodes and edges within the code graphs. In these graphs, nodes represent source code symbols such as MODULE, CLASS, and FUNCTION, and each node is enriched with relevant meta-information. The edges between nodes represent the relationships among these symbols, such as CONTAINS, INHERITS, and USES.

CodexGraph was assessed using three benchmarks: CrossCodeEval, SWE-bench, and EvoCodeBench. Additionally, the developers created five real-world coding applications. With a unified graph database schema, CodexGraph demonstrates competitive performance and potential in both academic and real-world environments, showcasing its versatility and efficacy in software engineering.

## codebadger (2026)

A more recent paper (March 2026) introduces codebadger, an open source Model Context Protocol (MCP) server that integrates Joern's Code Property Graph (CPG) engine with LLMs. Rather than requiring LLMs to generate complex CPG queries, codebadger provides high level tools for program slicing, taint tracking, data flow analysis, and semantic code navigation, enabling targeted exploration of large codebases without exhaustive file reading.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8ea0dba-379b-40ad-b328-fb34985a59b7",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "d8e1d550-d710-4e68-9f5b-92fe40d7e4c8",
  "sourceToolAssistantUUID": "d8ea0dba-379b-40ad-b328-fb34985a59b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T18:41:13.115Z_

<details><summary>↩ Tool result · `toolu_013YVjbrYRWj5mhdoseKv5Ku`</summary>

```text
Web search results for query: "data flow graph distillation code repair lightweight model 2025 2026 arxiv"

Links: [{"title":"[2601.10987] Reasoning Distillation for Lightweight Automated Program Repair","url":"https://arxiv.org/abs/2601.10987"},{"title":"Machine Learning Mar 2025","url":"https://www.arxiv.org/list/cs.LG/2025-03?skip=500&show=2000"},{"title":"Knowledge Distillation and Dataset Distillation of Large ...","url":"https://arxiv.org/pdf/2504.14772"},{"title":"GitHub - Guang000/Awesome-Dataset-Distillation: A curated list of awesome papers on dataset distillation and related applications. · GitHub","url":"https://github.com/Guang000/Awesome-Dataset-Distillation"},{"title":"Artificial Intelligence May 2025","url":"https://arxiv.org/list/cs.AI/2025-05?skip=975&show=2000"},{"title":"Published in Transactions on Machine Learning Research (09/2025)","url":"https://arxiv.org/pdf/2503.12067"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=5250&show=2000"},{"title":"Machine Learning Jun 2025","url":"https://arxiv.org/list/cs.LG/2025-06?skip=2425&show=2000"},{"title":"[2602.12233] Categorical Flow Maps","url":"https://arxiv.org/abs/2602.12233"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=1100&show=2000"}]

Based on the search results, here are the key findings:

## Most Relevant Result

The most directly relevant paper to your query is:

"Reasoning Distillation for Lightweight Automated Program Repair" (arXiv:2601.10987, January 2026)

This paper addresses the intersection of your search terms. The researchers study whether lightweight symbolic reasoning supervision can improve fix type classification in compact automated program repair models. They propose a reasoning distillation approach in which a large teacher model provides structured symbolic reasoning tags alongside fix-type labels that capture high-level causal properties of bugs without relying on free-form explanations. They train a CodeT5-based student model under label-only and reasoning-distilled settings on the IntroClass benchmark.

## Key Findings

The results suggest that symbolic reasoning distillation is a practical way to improve interpretability and robustness in lightweight program repair models. Reasoning supervision consistently improves macro averaged performance, particularly on less frequent bug categories, without increasing model size or complexity.

While the search results include many papers on knowledge distillation, dataset distillation, and code models from 2025-2026, this paper appears to be the most directly aligned with your specific query combining data flow considerations, code repair, lightweight models, and distillation techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03b6fd22-6d7a-4bae-9f1d-9a417cecc43d",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "2cef71f3-53e5-4577-85b9-ff318b1c68fc",
  "sourceToolAssistantUUID": "03b6fd22-6d7a-4bae-9f1d-9a417cecc43d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T18:41:13.736Z_

<details><summary>↩ Tool result · `toolu_01XtrkshSsBdWPJkBUPkD6ej`</summary>

```text
Web search results for query: "SWE-Fixer repository level bug fix retrieval augmented 2025"

Links: [{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and ...","url":"https://aclanthology.org/2025.findings-acl.62.pdf"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"2025-4-22 SWE-Synth: Synthesizing Verifiable Bug-Fix","url":"https://arxiv.org/pdf/2504.14757"},{"title":"[2504.14757] SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs","url":"https://arxiv.org/abs/2504.14757"},{"title":"SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/html/2512.17419v1"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"SWE-Fixer/README.md at main · InternLM/SWE-Fixer","url":"https://github.com/InternLM/SWE-Fixer/blob/main/README.md"},{"title":"SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents","url":"https://arxiv.org/html/2504.08703v1"},{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution","url":"https://www.researchgate.net/publication/394273882_SWE-Fixer_Training_Open-Source_LLMs_for_Effective_and_Efficient_GitHub_Issue_Resolution"}]

Based on the search results, here's what I found about SWE-Fixer and repository-level bug fix retrieval augmented approaches in 2025:

## SWE-Fixer Overview

SWE-Fixer is a simple yet effective solution for addressing real-world GitHub issues by training open-source LLMs, featuring a streamlined retrieve-then-edit pipeline with two core components: a Code File Retriever and a Code Editor.

## Key Components

The SWE-Fixer framework contains two components: code file retrieval and code editing, with a coarse-to-fine retrieval method using BM25 and a fine-tuned retriever. SWE-Fixer employs a coarse-to-fine retriever that combines BM25 with a fine-tuned 7B model to enhance retrieval precision.

## Models and Training

The implementation fine-tunes Qwen2.5-7b and Qwen2.5-72b for the retriever and the editor respectively, leveraging a curated dataset of 110K instances. Additionally, SWE-Fixer's edit model generates patch completions using chain-of-thought (CoT) training data.

## Performance

The approach achieves 32.8% on SWE-Bench Verified.

## Repository Context

SWE-Fixer aggregates massive datasets by scraping GitHub history, operating as a retrieval-based pipeline without execution environments, prioritizing raw volume over execution-based verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4043811f-da41-46ae-aa0d-325f769a793f",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "3b571624-0afe-41c1-8e9a-0b2c463e78f3",
  "sourceToolAssistantUUID": "4043811f-da41-46ae-aa0d-325f769a793f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T18:41:13.968Z_

<details><summary>↩ Tool result · `toolu_01T9TMFhYHwKaFJchdbk38uJ`</summary>

```text
Web search results for query: "program slicing LLM code repair context window 2025 2026"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Context-aware prompting for LLM-based program repair | Automated Software Engineering","url":"https://link.springer.com/article/10.1007/s10515-025-00512-w"},{"title":"Repairing LLM Executions for Secure Automatic Programming Ali El Husseini","url":"https://abhikrc.com/pdf/ICSE26-security.pdf"},{"title":"8 Things You Didn't Know About Code Mode | goose","url":"https://block.github.io/goose/blog/2026/02/06/8-things-you-didnt-know-about-code-mode/"},{"title":"Challenges to Using LLMs in Code Generation and Repair","url":"https://web.mit.edu/ha22286/www/papers/IEEESP25_1.pdf"},{"title":"LLMs for Code Repair: How AI Fixes Broken Code Efficiently","url":"https://www.guvi.in/blog/llms-for-code-repair/"},{"title":"DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging","url":"https://arxiv.org/html/2604.19305v1"},{"title":"My LLM coding workflow going into 2026 | by Addy Osmani | Medium","url":"https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e"},{"title":"Code Repair with LLMs gives an Exploration-Exploitation Tradeoff | OpenReview","url":"https://openreview.net/forum?id=o863gX6DxA"}]

Based on the search results, here's what I found about program slicing, LLM code repair, and context window approaches from 2025-2026:

## Key Findings

**Analysis-Augmented Generation and Program Slicing:**

Analysis-augmented generation (AAG) feeds frozen language models with artifacts from program analysis, which typically appear in three forms: failing-test evidence, semantics-aware slices that prune unrelated code, and concise execution traces. Recent systems include Appatch (Nong et al., 2024) which applies semantics-aware slices, and TracePrompt (Haque et al., 2025b) which contributes concise execution traces.

**Context Window Management:**

Compared to plain zero-shot prompts, AAG consistently improves repair accuracy and keeps edits focused on fault-relevant code, while ensuring that extra context remains within the model window. This is particularly important given LLMs have a prompt input and output size threshold (e.g., GPT-4 can take up to 128,000 tokens), but considering real software systems' complexity and size, these thresholds are insufficient, and LLMs may miss the broader context of a project and can generate a limited repair size.

**Context-Aware Prompting Approaches:**

CodeCorrector is a context-aware APR approach which designs a Chain-of-Thought approach where it analyzes why tests fail, selects relevant context information, and builds context-aware repair prompts to guide LLMs for patch generation.

The search results show active research in 2025-2026 on leveraging program analysis techniques like slicing to manage context windows effectively in LLM-based code repair systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00106fd0-d38c-46a8-8061-16a3f4efab0e",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "4b0e7fa6-931e-4d35-aea0-f7b18d80d4d9",
  "sourceToolAssistantUUID": "00106fd0-d38c-46a8-8061-16a3f4efab0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T18:41:18.523Z_

<details><summary>↩ Tool result · `toolu_01Pujq4z3XiMyQCvXJbPxtEa`</summary>

```text
Web search results for query: "GREPO benchmark graph neural network repository bug localization arxiv 2026"

Links: [{"title":"[2602.13921v1] GREPO: A Benchmark for Graph Neural Networks on Repository-Level Bug Localization","url":"https://arxiv.org/abs/2602.13921v1"},{"title":"GREPO: A Benchmark for Graph Neural Networks on Repository-Level Bug Localization","url":"https://arxiv.org/html/2602.13921"},{"title":"[2602.13921] GREPO: A Benchmark for Graph Neural Networks on Repository-Level Bug Localization","url":"https://arxiv.org/abs/2602.13921"},{"title":"GREPO: A Benchmark for Graph Neural Networks on Repository-Level Bug Localization | OpenReview","url":"https://openreview.net/forum?id=2tDLQuz0H6"},{"title":"GitHub - qingpingmo/GREPO: This repository is the official code implementation for the paper \"GREPO: A Benchmark for Graph Neural Networks on Repository-Level Bug Localization\". · GitHub","url":"https://github.com/qingpingmo/GREPO"},{"title":"[2603.01447] A Cascaded Graph Neural Network for Joint Root Cause Localization and Analysis in Edge Computing Environments","url":"https://arxiv.org/abs/2603.01447"},{"title":"GitHub - graphdeeplearning/benchmarking-gnns: Repository for benchmarking graph neural networks (JMLR 2023) · GitHub","url":"https://github.com/graphdeeplearning/benchmarking-gnns"},{"title":"[2003.00982] Benchmarking Graph Neural Networks","url":"https://arxiv.org/abs/2003.00982"},{"title":"Revisiting the Necessity of Graph Learning and Common Graph Benchmarks","url":"https://arxiv.org/html/2412.06173v1"},{"title":"A Cascaded Graph Neural Network for Joint Root Cause Localization and Analysis in Edge Computing Environments","url":"https://arxiv.org/html/2603.01447"}]

Based on the search results, here's what I found about the GREPO benchmark:

## GREPO: Graph Neural Networks for Repository-Level Bug Localization

GREPO is the first GNN benchmark for repository-scale bug localization tasks, comprising 86 Python repositories and 47294 bug-fixing tasks, providing graph-based data structures ready for direct GNN processing.

### Context and Motivation

Repository-level bug localization is the task of identifying where code must be modified to fix a bug, and standard Large Language Models (LLMs) are often unsuitable for this task due to context window limitations that prevent them from processing entire code repositories. Graph Neural Networks (GNNs) offer a promising alternative due to their ability to model complex, repository-wide dependencies; however, their application has been hindered by the lack of a dedicated benchmark.

### Key Features

The benchmark extracts four types of code entities (Directory, File, Class, and Function), and defines three primary relation types: Contain/ContainedIn (encoding hierarchical nesting), Call/Called (representing function or method invocations), and Child/Parent (modeling class inheritance).

### Results and Availability

Evaluation of various GNN architectures shows outstanding performance compared to established information retrieval baselines, and the code is available online.

The paper was published on arXiv in February 2026 (arxiv preprint 2602.13921).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10c996f9-71d1-41a8-bd8f-d0f414eea08f",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "05b02621-8301-467e-8729-7f494568353c",
  "sourceToolAssistantUUID": "10c996f9-71d1-41a8-bd8f-d0f414eea08f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-10T18:41:21.162Z_

Let me run a few final targeted searches to capture more specific related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05b02621-8301-467e-8729-7f494568353c",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNufZMQXZ5D6f5mqXfP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97b7dfe9-d1b5-4ad4-90f2-68c750f724e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013X8aEv3RzrFbyeLRWcGLPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2732,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 16374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3021,
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

_source line 33 · 2026-05-10T18:41:22.090Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VBMWq81j762oXcHYvaWNMX`</summary>

```json
{
  "query": "codebadger Joern code property graph MCP server LLM program slicing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97b7dfe9-d1b5-4ad4-90f2-68c750f724e5",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNufZMQXZ5D6f5mqXfP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6783f061-42e5-4001-99ac-41e3b4588a4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013X8aEv3RzrFbyeLRWcGLPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2732,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 16374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3021,
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

_source line 34 · 2026-05-10T18:41:23.095Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WBAinxqV3y7nbMdmwhApCf`</summary>

```json
{
  "query": "\"fault localization granularity\" repository code repair LLM arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6783f061-42e5-4001-99ac-41e3b4588a4b",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNufZMQXZ5D6f5mqXfP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55d0fc54-df22-41c7-b668-9395cd44a773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013X8aEv3RzrFbyeLRWcGLPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2732,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 16374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3021,
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

_source line 35 · 2026-05-10T18:41:23.564Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LTBgDiYg7fm5569GJj71xK`</summary>

```json
{
  "query": "GraphCodeBERT contrastive learning code retrieval structural features 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55d0fc54-df22-41c7-b668-9395cd44a773",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNufZMQXZ5D6f5mqXfP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "979b3959-c542-4af1-a672-d7f80828d64f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013X8aEv3RzrFbyeLRWcGLPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2732,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 16374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3021,
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

_source line 36 · 2026-05-10T18:41:24.258Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UXzbRZFCRcMmh6ydHemii4`</summary>

```json
{
  "query": "context-aware prompting CodeCorrector automated program repair 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "979b3959-c542-4af1-a672-d7f80828d64f",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNufZMQXZ5D6f5mqXfP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ab98944-77f3-499d-91bf-83318c1160e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013X8aEv3RzrFbyeLRWcGLPA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2732,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 16374,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3021
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2732,
          "output_tokens": 244,
          "cache_read_input_tokens": 16374,
          "cache_creation_input_tokens": 3021,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3021,
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

_source line 37 · 2026-05-10T18:41:29.874Z_

<details><summary>↩ Tool result · `toolu_01VBMWq81j762oXcHYvaWNMX`</summary>

```text
Web search results for query: "codebadger Joern code property graph MCP server LLM program slicing 2026"

Links: [{"title":"GitHub - Lekssays/codebadger: A containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift. · GitHub","url":"https://github.com/Lekssays/codebadger"},{"title":"Bridging Code Property Graphs and Language Models for Program Analysis","url":"https://arxiv.org/html/2603.24837"},{"title":"[2603.24837] Bridging Code Property Graphs and Language Models for Program Analysis","url":"https://arxiv.org/abs/2603.24837"},{"title":"codebadger | MCP Servers","url":"https://lobehub.com/mcp/lekssays-codebadger"},{"title":"CodeBadger by Lekssays | Glama","url":"https://glama.ai/mcp/servers/Lekssays/codebadger"},{"title":"Codebadger Toolkit: AI Static Code Analysis with Joern CPG","url":"https://mcpmarket.com/server/codebadger-toolkit"},{"title":"(PDF) Bridging Code Property Graphs and Language Models for Program Analysis","url":"https://www.researchgate.net/publication/403193710_Bridging_Code_Property_Graphs_and_Language_Models_for_Program_Analysis"},{"title":"codebadger — Assay","url":"https://assay.tools/packages/codebadger"},{"title":"Code Property Graph | Joern Documentation","url":"https://docs.joern.io/code-property-graph/"},{"title":"Glama – MCP Hosting Platform","url":"https://glama.ai/mcp/servers/@Lekssays/codebadger-toolkit"}]

## Search Results Summary

I found comprehensive information about codebadger, the Joern Code Property Graph MCP server, and LLM program slicing from 2026. Here are the key findings:

### Overview
CodeBadger is a containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) technology with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift.

### Research and Publication
CodeBadger and its accompanying paper — Bridging Code Property Graphs and Language Models for Program Analysis — have been accepted at the Software Vulnerability Management Workshop @ ICSE 2026. The paper is published as an arXiv preprint (arXiv:2603.24837) in 2026.

### Core Functionality
CodeBadger is an open-source Model Context Protocol (MCP) server that integrates Joern's Code Property Graph (CPG) engine with LLMs, providing high-level tools for program slicing, taint tracking, data flow analysis, and semantic code navigation, enabling targeted exploration of large codebases without exhaustive file reading.

### Architecture
CodeBadger acts as an intermediary service between an LLM agent and the Joern static analysis engine, with a session-based workflow managed via MCP over HTTP. The agent can make subsequent tool calls such as get_program_slice or get_data_dependencies, and the MCP server translates these high-level functions into specific CPGQL queries, executes them via Joern, and returns structured results to the LLM.

### Notable Achievements
CodeBadger demonstrated effectiveness in discovering and exploiting a previously unreported buffer overflow in libtiff, and generating a correct patch for an integer overflow vulnerability (CVE-2025-6021) in libxml2 on the first attempt.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6783f061-42e5-4001-99ac-41e3b4588a4b",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "af38de2c-10bf-4671-89cf-9aeafba86eb9",
  "sourceToolAssistantUUID": "6783f061-42e5-4001-99ac-41e3b4588a4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T18:41:31.265Z_

<details><summary>↩ Tool result · `toolu_01WBAinxqV3y7nbMdmwhApCf`</summary>

```text
Web search results for query: ""fault localization granularity" repository code repair LLM arxiv 2026"

Links: [{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/abs/2604.00167"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale","url":"https://arxiv.org/pdf/2604.00167"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"[2604.05481] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/html/2601.18044v1"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"}]

I found several relevant research papers from arXiv 2026 on fault localization granularity for repository-scale code repair with LLMs:

## Key Papers Found:

### 1. "A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks" (arXiv:2604.00167)

Under this configuration at least function-level granularity yields the highest resolve rate for the SWE-Bench-Mini subset of the SWE-Bench Verified benchmark overall, but a deeper dive suggests that the ideal granularity may in fact be task-dependent. The study examines how the impact of granularity is explored for smaller datasets, isolating this issue from the separate question of localization accuracy by testing code repair under the assumption of perfect fault localization, with no repository-scale studies previously explicitly investigating granularity under this assumption.

### 2. "On the Role of Fault Localization Context for LLM-Based Program Repair" (arXiv:2604.05481)

This study provides complementary findings: Expanding file context is often associated with improved performance, with successful repairs most commonly observed in configurations with approximately 6-10 relevant files. Additionally, element-level context expansion provides conditional gains that depend strongly on the file context quality, while line-level context expansion frequently degrades performance due to noise amplification.

### 3. "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair"

Repository-level fault localization and automated program repair require an agent to identify the relevant code units across files, follow call and data dependencies, and generate a valid patch.

These papers all address the critical question of how fault localization granularity impacts LLM-based code repair at the repository scale.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55d0fc54-df22-41c7-b668-9395cd44a773",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "a6cb1fcd-e5f1-4a9d-b127-d10be5b10b74",
  "sourceToolAssistantUUID": "55d0fc54-df22-41c7-b668-9395cd44a773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T18:41:31.349Z_

<details><summary>↩ Tool result · `toolu_01UXzbRZFCRcMmh6ydHemii4`</summary>

```text
Web search results for query: "context-aware prompting CodeCorrector automated program repair 2025"

Links: [{"title":"Context-aware prompting for LLM-based program repair | Automated Software Engineering","url":"https://link.springer.com/article/10.1007/s10515-025-00512-w"},{"title":"Context-aware prompting for LLM-based program repair: Context-aware prompting for LLM-based program repair: Automated Software Engineering: Vol 32, No 2","url":"https://dl.acm.org/doi/10.1007/s10515-025-00512-w"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"[PDF] Automated Program Repair in the Era of Large Pre-trained Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automated-Program-Repair-in-the-Era-of-Large-Models-Xia-Wei/5aec1050fd62971f2b40b597ef7526fbc820beab"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Advancements in automated program repair: a comprehensive review | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02383-9"},{"title":"Code Vulnerability Repair with Large Language Model Using Context-Aware Prompt Tuning | Request PDF","url":"https://www.researchgate.net/publication/393389800_Code_Vulnerability_Repair_with_Large_Language_Model_Using_Context-Aware_Prompt_Tuning"},{"title":"A Survey of LLM-based Automated Program Repair","url":"https://arxiv.org/pdf/2506.23749"},{"title":"Context-aware patch generation for better automated program repair | Proceedings of the 40th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3180155.3180233"},{"title":"Context-aware patch generation for better automated program repair | Request PDF","url":"https://www.researchgate.net/publication/329639259_Context-aware_patch_generation_for_better_automated_program_repair"}]

Based on the search results, here's what I found about context-aware prompting and CodeCorrector for automated program repair in 2025:

## CodeCorrector: Context-Aware APR Approach

CodeCorrector is a context-aware APR approach that designs a Chain-of-Thought (CoT) approach to follow developers' program repair behaviors. Given a failing test and its buggy file, CodeCorrector first analyzes why the test fails based on the failure message to infer repair direction; then selects the relevant context information to this repair direction; finally builds the context-aware repair prompt to guide LLMs for patch generation.

## Motivation and Key Innovation

LLM-based APR effectiveness is constrained by casually-determined context, being unable to adaptively select the specific context according to the situation of each defect, and a more effective APR approach is needed which provides more precise and comprehensive context for the given defect to enhance the robustness of LLM-based APRs.

## Performance Results

CodeCorrector outperforms all state-of-the-art baselines on the more complex defects in Defects4J v2.0 and the defects without fine-grained defect localization information in Defects4J v1.2, with a total of 38 defects fixed by only CodeCorrector.

The research was published in 2025 in the journal Automated Software Engineering, representing a significant advancement in how large language models can be guided with context-aware prompting techniques for automated program repair.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ab98944-77f3-499d-91bf-83318c1160e5",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "55062696-83f7-42fc-8473-7afc36921d79",
  "sourceToolAssistantUUID": "7ab98944-77f3-499d-91bf-83318c1160e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T18:41:34.528Z_

<details><summary>↩ Tool result · `toolu_01LTBgDiYg7fm5569GJj71xK`</summary>

```text
Web search results for query: "GraphCodeBERT contrastive learning code retrieval structural features 2025 2026"

Links: [{"title":"SCL-CVD: : Supervised contrastive learning for code vulnerability detection via GraphCodeBERT: Computers and Security: Vol 145, No C","url":"https://dl.acm.org/doi/10.1016/j.cose.2024.103994"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/pdf/2301.09072"},{"title":"LLMSniffer: Detecting LLM-Generated Code via GraphCodeBERT and Supervised Contrastive Learning","url":"https://arxiv.org/html/2604.16058"},{"title":"SCL-CVD: Supervised contrastive learning for code vulnerability detection via GraphCodeBERT - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0167404824002992"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10172726/"},{"title":"Archaeology at SemEval-2026 Task 13: Fine-Tuning Pre-Trained Code Models for AI-Generated Code Detection","url":"https://arxiv.org/html/2605.01596"},{"title":"SCL-CVD: Supervised contrastive learning for code vulnerability detection via GraphCodeBERT | Request PDF","url":"https://www.researchgate.net/publication/382290815_SCL-CVD_Supervised_contrastive_learning_for_code_vulnerability_detection_via_GraphCodeBERT"},{"title":"[PDF] GraphCodeBERT: Pre-training Code Representations with Data Flow | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCodeBERT:-Pre-training-Code-Representations-Guo-Ren/4083958684292f6fa2f5c7fd4f9be975e80145b6"},{"title":"Learning to represent code semantics","url":"http://scis.scichina.com/en/2025/172101.pdf"},{"title":"graphcodebert: pre-training code represen","url":"https://huang.isis.vanderbilt.edu/cs8395/readings/graphcodebert.pdf"}]

Based on the web search results, here's what I found regarding GraphCodeBERT, contrastive learning, code retrieval, and structural features in 2025-2026:

## Recent Applications of GraphCodeBERT with Contrastive Learning

GraphCodeBERT has been combined with supervised contrastive learning to cluster same-class representations while separating different-class ones, with data-flow structure encoding. Recent research demonstrates several key developments:

### Vulnerability Detection
A novel approach called SCL-CVD leverages GraphCodeBERT fine-tuned using a supervised contrastive loss function combined with R-Drop. In 2025, MCL-VD (Multi-modal Contrastive Learning) extended this with LoRA-enhanced GraphCodeBERT for effective vulnerability detection.

### AI-Generated Code Detection
LLMSniffer fine-tunes GraphCodeBERT using a two-stage supervised contrastive learning pipeline, achieving significant improvements in detecting machine-generated versus human-written code.

### Code Representation and Retrieval
GraphCodeBERT is a pre-trained model for code that considers structures in code by incorporating the data flow of code to encode relations between variables in the pre-training stage. It is fine-tuned on downstream tasks including code search, clone detection, code translation and code refinement.

### Recent 2026 Developments
Research comparing code models shows that CodeBERT and GraphCodeBERT, with their focus on code understanding, perform best on binary detection tasks, with exploration of additional syntactic features and contrastive learning objectives underway.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "979b3959-c542-4af1-a672-d7f80828d64f",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "7fcfc7f7-117c-4871-b519-59248e9b5813",
  "sourceToolAssistantUUID": "979b3959-c542-4af1-a672-d7f80828d64f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-10T18:41:38.127Z_

Let me do a final round of searches to pick up a few more key papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fcfc7f7-117c-4871-b519-59248e9b5813",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNvqyCEBDs64pAjDaR2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47767fb7-40f2-443f-876e-2088aec3a2fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YayV5BvZYVPxN2BhbPdVHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1022,
      "cache_creation_input_tokens": 6030,
      "cache_read_input_tokens": 19395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6030,
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

_source line 42 · 2026-05-10T18:41:39.082Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RjGiXCa1ofjkne9B6HceSc`</summary>

```json
{
  "query": "ARISE repository graph representation agentic fault localization program repair arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47767fb7-40f2-443f-876e-2088aec3a2fd",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNvqyCEBDs64pAjDaR2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04e4c5ce-f419-407e-8584-15ed895ab349",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YayV5BvZYVPxN2BhbPdVHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1022,
      "cache_creation_input_tokens": 6030,
      "cache_read_input_tokens": 19395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6030,
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

_source line 43 · 2026-05-10T18:41:39.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018J63krd1QnyP9TFexrTUyX`</summary>

```json
{
  "query": "D4C data dependency driven code repair context arxiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04e4c5ce-f419-407e-8584-15ed895ab349",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNvqyCEBDs64pAjDaR2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff078b55-1f9b-4349-80fe-c21b98f8131e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YayV5BvZYVPxN2BhbPdVHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1022,
      "cache_creation_input_tokens": 6030,
      "cache_read_input_tokens": 19395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6030,
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

_source line 44 · 2026-05-10T18:41:40.298Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N6DtG841eXPinTTjGxwpTe`</summary>

```json
{
  "query": "RGFL reasoning guided fault localization automated program repair LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff078b55-1f9b-4349-80fe-c21b98f8131e",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNvqyCEBDs64pAjDaR2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c379c265-1c85-4de1-a54a-9c6fb90dbf84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YayV5BvZYVPxN2BhbPdVHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1022,
      "cache_creation_input_tokens": 6030,
      "cache_read_input_tokens": 19395,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6030
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1022,
          "output_tokens": 189,
          "cache_read_input_tokens": 19395,
          "cache_creation_input_tokens": 6030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6030,
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

_source line 45 · 2026-05-10T18:41:47.489Z_

<details><summary>↩ Tool result · `toolu_01RjGiXCa1ofjkne9B6HceSc`</summary>

```text
Web search results for query: "ARISE repository graph representation agentic fault localization program repair arxiv 2026"

Links: [{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749"},{"title":"A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion","url":"https://arxiv.org/html/2409.13642v2"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"Doctor-RAG: Failure-Aware Repair for Agentic Retrieval-Augmented Generation","url":"https://arxiv.org/html/2604.00865"},{"title":"Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://arxiv.org/html/2503.21710v1"},{"title":"[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/abs/2604.00167"}]

I found the paper you were searching for! Here's what I found:

## ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

### Key Results

The system was evaluated on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone. Compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points. These localization gains translate directly into repair success, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.

The paper is available on arXiv as [2605.03117](https://arxiv.org/abs/2605.03117).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04e4c5ce-f419-407e-8584-15ed895ab349",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "f3220d0c-220e-4b9f-ab57-b4e30dbbf345",
  "sourceToolAssistantUUID": "04e4c5ce-f419-407e-8584-15ed895ab349",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-10T18:41:47.907Z_

<details><summary>↩ Tool result · `toolu_01N6DtG841eXPinTTjGxwpTe`</summary>

```text
Web search results for query: "RGFL reasoning guided fault localization automated program repair LLM 2025"

Links: [{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair","url":"https://www.arxiv.org/pdf/2601.18044"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2601.18044"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/html/2601.18044"},{"title":"[2601.18044] RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/abs/2601.18044"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260118044S/abstract"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models | Scilit","url":"https://www.scilit.com/publications/93a4ab9613be0ae41a0609c084a46a24"},{"title":"Assessing the effectiveness of recent closed-source large language models in fault localization and automated program repair | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00549-x"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481"},{"title":"Explainable Fault Localization for Programming Assignments via LLM-Guided Annotation","url":"https://arxiv.org/html/2509.25676v1"}]

Based on the search results, I found comprehensive information about RGFL:

## RGFL: Reasoning Guided Fault Localization

RGFL is a novel approach that improves fault localization (FL), which is a critical step in automated program repair (APR). In realistic project-level repair scenarios where software repositories span millions of tokens far exceeding current LLM context limits, accurate FL is essential for effective repair.

### Key Innovation

RGFL introduces an explicit per-candidate reasoning stage where, for each file or element individually, the LLM explains its functionality and how this explanation is causally related to the reported symptom. These reasoning outputs are then used as ranking signals.

### Technical Approach

The method introduces a hierarchical reasoning module that (i) generates structured, bug-specific explanations for candidate files and elements, and (ii) leverages these explanations in a two-stage ranking scheme combining LLM-based and embedding-based signals.

### Integration and Pipeline

RGFL integrates the LLM-based reasoning approach into the modular APR framework Agentless, changing both the file-level and element-level localization modules. The pipeline proceeds in four stages: (1) file localization using code+reasoning ranking, (2) element localization using reasoning within the top-k files (k=3), (3) line localization, and (4) patch generation and validation.

### Evaluation

The approach is evaluated on SWE-bench Verified, SWE-bench Lite, and SWE-bench Java to test generalizability across different datasets and programming languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c379c265-1c85-4de1-a54a-9c6fb90dbf84",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "57e2a5e1-50fb-400f-a414-d209cd630a22",
  "sourceToolAssistantUUID": "c379c265-1c85-4de1-a54a-9c6fb90dbf84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-10T18:41:48.042Z_

<details><summary>↩ Tool result · `toolu_018J63krd1QnyP9TFexrTUyX`</summary>

```text
Web search results for query: "D4C data dependency driven code repair context arxiv 2024 2025"

Links: [{"title":"GitHub - CUHK-Shenzhen-SE/D4C: [ICSE'25] Aligning the Objective of LLM-based Program Repair","url":"https://github.com/CUHK-Shenzhen-SE/D4C"},{"title":"arXiv:2506.23749v1 [cs.SE] 30 Jun 2025","url":"https://arxiv.org/pdf/2506.23749"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"ml4se/README.md at master · saltudelft/ml4se","url":"https://github.com/saltudelft/ml4se/blob/master/README.md"},{"title":"A Systematic Literature Review on Large Language Models","url":"https://arxiv.org/pdf/2405.01466"},{"title":"[2510.11059] Defects4C: Benchmarking Large Language Model Repair Capability with C/C++ Bugs","url":"https://arxiv.org/abs/2510.11059"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants","url":"https://arxiv.org/html/2602.00180v1"},{"title":"Computer Science Apr 2024","url":"https://arxiv.org/list/cs/2024-04?skip=4600&show=2000"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"}]

I found information about D4C! Here are the search results:

## D4C: Data Dependency-Driven Code Repair

D4C is a straightforward prompting framework for automated program repair (APR) that can repair 180 bugs correctly in Defects4J with each patch sampled only 10 times, surpassing state-of-the-art APR methods with perfect fault localization by 10% and reducing the patch sampling number by 90%.

### Key Insights

The research reveals that objective alignment is crucial for fully exploiting LLM's pre-trained capability, and replacing the traditional localize-buggy-hunks-then-repair workflow with direct debugging is more effective for LLM-based APR methods.

### Technical Details

The paper explores how decoder-only LLMs' next token prediction training objective is misaligned with masked span prediction objectives of current infilling-style methods, impeding LLMs from fully leveraging pre-trained knowledge for program repair, and notes that while some LLMs can locate and repair bugs in certain functions using related artifacts like test cases, existing methods still depend on statement-level fault localization.

### Publication Status

The work is cited as "Aligning the Objective of LLM-based Program Repair" with arXiv preprint arXiv:2404.08877, year 2024, and D4C is accepted at ICSE 2025 and uses GPT-4 and Mixtral on Java, C++, and Python.

The GitHub repository indicates this is an ICSE'25 submission providing artifacts for D4C.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff078b55-1f9b-4349-80fe-c21b98f8131e",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "87b4ddb8-13e1-485f-95f0-cb42d4852b43",
  "sourceToolAssistantUUID": "ff078b55-1f9b-4349-80fe-c21b98f8131e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-10T18:41:51.093Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014fthVTrFX5ZKjBcptKtTKi`</summary>

```json
{
  "query": "\"repository-aware knowledge graph\" software repair arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87b4ddb8-13e1-485f-95f0-cb42d4852b43",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNwqkaEjD86w1o13Yzq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac6190c6-b9ff-4109-9b83-3c39974467c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dKjpa3SMAvVC9ULVG95Nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 3059,
      "cache_read_input_tokens": 25425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3059,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-10T18:41:51.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016dAKf8PKAJTU6922uRzeTn`</summary>

```json
{
  "query": "Appatch semantics-aware slicing program repair LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac6190c6-b9ff-4109-9b83-3c39974467c1",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNwqkaEjD86w1o13Yzq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75fc991d-447a-47f6-b4cb-73338e6f5b66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dKjpa3SMAvVC9ULVG95Nw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 3059,
      "cache_read_input_tokens": 25425,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3059
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 959,
          "output_tokens": 119,
          "cache_read_input_tokens": 25425,
          "cache_creation_input_tokens": 3059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3059,
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

_source line 50 · 2026-05-10T18:41:58.638Z_

<details><summary>↩ Tool result · `toolu_014fthVTrFX5ZKjBcptKtTKi`</summary>

```text
Web search results for query: ""repository-aware knowledge graph" software repair arxiv 2025"

Links: [{"title":"[2503.21710] Enhancing repository-level software repair via repository-aware knowledge graphs","url":"https://arxiv.org/abs/2503.21710"},{"title":"Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://arxiv.org/html/2503.21710v1"},{"title":"KGCompass: Knowledge Graph Enhanced Repository-Level Software Repair","url":"https://arxiv.org/html/2503.21710v2"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2503.21710v1] Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://arxiv.org/abs/2503.21710v1"},{"title":"Enhancing repository-level software repair via repository-aware knowledge graphs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250321710Y/abstract"},{"title":"[Literature Review] Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://www.themoonlight.io/en/review/enhancing-repository-level-software-repair-via-repository-aware-knowledge-graphs"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"(PDF) Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://www.researchgate.net/publication/390247861_Enhancing_Repository-Level_Software_Repair_via_Repository-Aware_Knowledge_Graphs"},{"title":"Paper summary: Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://konradb.substack.com/p/paper-summary-enhancing-repository"}]

Based on the search results, I found a highly relevant research paper on this topic:

## "Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs"

This paper was submitted to arXiv on March 27, 2025, and presents a system called **KGCompass**.

### Key Problem
Repository-level software repair faces challenges in bridging semantic gaps between issue descriptions and code patches, and existing approaches that primarily rely on large language models (LLMs) are hindered by semantic ambiguities, limited understanding of structural context, and insufficient reasoning capabilities.

### Main Contributions
The paper proposes KGCompass with two innovations: (1) a novel repository-aware knowledge graph (KG) that accurately links repository artifacts (issues and pull requests) and codebase entities (files, classes, and functions), allowing the system to narrow down the vast search space to only 20 most relevant functions with accurate candidate fault locations and contextual information, and (2) a path-guided repair mechanism that leverages KG-mined entity paths to augment LLMs with relevant contextual information to generate precise patches along with their explanations.

### Performance Results
Experimental results on the SWE-Bench-Lite benchmark demonstrate that KGCompass achieves state-of-the-art repair performance (45.67%) and function-level localization accuracy (51.33%) across open-source approaches, costing only $0.20 per repair.

### Key Insight
89.7% of successful fault locations require 2+ hops, which means the knowledge graph successfully bridges the semantic gap between natural-language bug reports and codebase by capturing indirect structural relations that text-only LLMs miss.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac6190c6-b9ff-4109-9b83-3c39974467c1",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "0243ba51-8672-4794-83e5-c364bc3f6e41",
  "sourceToolAssistantUUID": "ac6190c6-b9ff-4109-9b83-3c39974467c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-10T18:41:58.809Z_

<details><summary>↩ Tool result · `toolu_016dAKf8PKAJTU6922uRzeTn`</summary>

```text
Web search results for query: "Appatch semantics-aware slicing program repair LLM 2024 2025"

Links: [{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"A Survey of LLM-based Automated Program Repair","url":"https://arxiv.org/pdf/2506.23749"},{"title":"APPATCH: Automated Adaptive Prompting Large Language Models for","url":"https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-1174-nong.pdf"},{"title":"AppAtch: Automated Adaptive Prompting Large Language ...","url":"https://chapering.github.io/pubs/sec25.pdf"},{"title":"(PDF) APPATCH: Automated Adaptive Prompting Large Language Models for Real-World Software Vulnerability Patching","url":"https://www.researchgate.net/publication/388657788_APPATCH_Automated_Adaptive_Prompting_Large_Language_Models_for_Real-World_Software_Vulnerability_Patching"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Appatch: Automated Adaptive Prompting Large Language Models for Real-World Software Vulnerability Patching","url":"https://arxiv.org/html/2408.13597v2"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"},{"title":"GitHub - GLEAM-Lab/ProgramRepair: A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications · GitHub","url":"https://github.com/GLEAM-Lab/ProgramRepair"},{"title":"Advancements in automated program repair: a comprehensive review | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02383-9"}]

Based on the search results, I found comprehensive information about Appatch. Here's what I found:

## Appatch Overview

Appatch applies semantics-aware scoping and adaptive exemplar prompting to vulnerability repair. It slices the program to include only code relevant to the vulnerability, mines an exemplar database, and selects examples on the fly to guide patch generation.

## How It Works

Given a vulnerable program with a known vulnerability location, Appatch first narrows down the scope of analysis to only the relevant subset of the program via semantics-aware scoping. This allows LLMs to analyze a smaller code snippet that includes all the essential information necessary for reasoning about the vulnerability-related code behaviors.

In Phase 1: Exemplar Mining, through semantics-aware scoping, it union-slices each given vulnerable sample to capture its vulnerability semantics. Then, Appatch proceeds with exemplar generation, producing a pool of exemplars each including the root cause analysis, fixing strategy, and ground-truth patch.

## Performance Results

In evaluations on 306 real vulnerabilities, it raised F1 from 44.9% to 57.2% across four LLMs, outpacing baseline prompting by up to 98.9% and surpassing state-of-the-art static approaches by as much as 65.4%. Appatch also fixed seven of eleven zero-day vulnerabilities that none of the baselines could handle.

## Publication

Appatch was published at USENIX Security 2025, making it one of the most recent approaches in LLM-based program repair.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75fc991d-447a-47f6-b4cb-73338e6f5b66",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a1c6187e43302749f",
  "type": "user",
  "uuid": "c41daaa0-ec25-4f7d-bac9-95340db80c37",
  "sourceToolAssistantUUID": "75fc991d-447a-47f6-b4cb-73338e6f5b66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-10T18:43:14.323Z_

Here is the comprehensive landscape of competing and closely related work that the authors should consider referencing or differentiating from. I have organized the papers by thematic relevance.

---

## 1. Graph-Based Repository-Level Fault Localization and Repair (Most Directly Competing)

**ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair**
- arXiv:2605.03117, May 2026
- Augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges. Exposes data-flow slicing as a first-class queryable agent primitive. Evaluated on SWE-bench Lite with Qwen2.5-Coder-32B, improving Function Recall@1 by 17 points and achieving 22.0% Pass@1.
- **Why critical:** This paper uses def-use edges in a repository-level graph for code repair context selection -- essentially the same core idea. The authors must cite and differentiate from it.
- [Paper](https://arxiv.org/abs/2605.03117)

**KGCompass: Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs**
- arXiv:2503.21710, March 2025
- Builds a repository-aware knowledge graph linking issues, PRs, files, classes, and functions. Uses path-guided repair with KG-mined entity paths to augment LLMs. Achieves 45.67% on SWE-Bench-Lite. Found that 89.7% of successful fault locations require 2+ hops in the graph.
- **Why relevant:** Uses structural code graphs for context selection in repair, though at a coarser granularity than def-use.
- [Paper](https://arxiv.org/abs/2503.21710)

**GREPO: A Benchmark for Graph Neural Networks on Repository-Level Bug Localization**
- arXiv:2602.13921, February 2026
- First GNN benchmark for repository-scale bug localization: 86 Python repos, 47,294 bug-fixing tasks. Extracts directory/file/class/function entities with contain, call, and inheritance relations. GNN architectures outperform IR baselines.
- **Why relevant:** Directly benchmarks GNNs for repo-level bug localization -- the evaluation methodology is relevant even if the task framing differs.
- [Paper](https://arxiv.org/abs/2602.13921)

---

## 2. Code Property Graphs + LLMs

**CodeBadger: Bridging Code Property Graphs and Language Models for Program Analysis**
- arXiv:2603.24837, March 2026; accepted at Software Vulnerability Management Workshop @ ICSE 2026
- An MCP server integrating Joern's Code Property Graph engine with LLMs. Provides high-level tools for program slicing, taint tracking, data flow analysis, and semantic code navigation. Demonstrated discovering a buffer overflow in libtiff and patching CVE-2025-6021 in libxml2.
- **Why relevant:** Operationalizes CPG-based data-flow analysis (including def-use) for LLM-driven code tasks, though focused on vulnerability analysis rather than distillation into a lightweight model.
- [Paper](https://arxiv.org/abs/2603.24837)

**LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided LLMs**
- USENIX Security 2025 (arXiv:2507.16585)
- Integrates CPGs with LLMs for vulnerability detection. CPG-based slice construction reduces code size by 67-91% while preserving vulnerability-relevant context. Achieves 15-40% F1 improvements over SOTA.
- **Why relevant:** Demonstrates CPG-guided context pruning for LLMs -- the pruning/selection mechanism is analogous to what a def-use distillation model would learn.
- [Paper](https://arxiv.org/abs/2507.16585)

**CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases**
- NAACL 2025 (arXiv:2408.03910)
- Integrates LLM agents with graph database interfaces. Uses static analysis to extract code graphs (MODULE, CLASS, FUNCTION nodes; CONTAINS, INHERITS, USES edges). Agents construct and execute graph queries for structure-aware context retrieval. Evaluated on CrossCodeEval, SWE-bench, and EvoCodeBench.
- **Why relevant:** Pioneering work on graph-database-mediated code context retrieval for LLMs.
- [Paper](https://arxiv.org/abs/2408.03910)

---

## 3. Fault Localization Context and Granularity for LLM Repair

**A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks**
- arXiv:2604.00167, April 2026
- Studies how fault localization granularity (file, function, line) affects repair under perfect FL assumptions on SWE-Bench. Finds function-level granularity yields the highest resolve rate overall, but optimal granularity is task-dependent.
- **Why relevant:** Directly relevant to the question of what granularity of context selection is optimal for repo-level repair.
- [Paper](https://arxiv.org/abs/2604.00167)

**On the Role of Fault Localization Context for LLM-Based Program Repair**
- arXiv:2604.05481, April 2026
- Finds that expanding file context to approximately 6-10 relevant files improves repair, but element-level and line-level expansion can degrade performance through noise amplification.
- **Why relevant:** Empirically characterizes the context selection problem that the proposed distillation approach aims to solve.
- [Paper](https://arxiv.org/abs/2604.05481)

**RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models**
- arXiv:2601.18044, January 2026
- Introduces per-candidate reasoning where the LLM explains each file/element's functionality and its causal relation to the bug symptom, then uses these explanations as ranking signals in a two-stage scheme. Evaluated on SWE-bench Verified, Lite, and Java.
- **Why relevant:** An alternative approach to context selection for repair that uses reasoning rather than data-flow signals.
- [Paper](https://arxiv.org/abs/2601.18044)

---

## 4. Semantics-Aware Slicing and Analysis-Augmented Repair

**Appatch: Automated Adaptive Prompting LLMs for Real-World Software Vulnerability Patching**
- USENIX Security 2025
- Uses semantics-aware scoping (union slicing) to narrow code to vulnerability-relevant subsets, then applies adaptive exemplar prompting. Raised F1 from 44.9% to 57.2% on 306 real vulnerabilities.
- **Why relevant:** Demonstrates that program slicing (a form of data-flow-guided context selection) significantly improves LLM repair, but uses it at inference time rather than distilling it into a model.
- [Paper](https://arxiv.org/abs/2408.13597)

**D4C: Aligning the Objective of LLM-based Program Repair**
- ICSE 2025 (arXiv:2404.08877)
- A prompting framework that replaces localize-then-repair with direct debugging. Repairs 180 bugs on Defects4J with only 10 samples per patch, surpassing SOTA by 10%.
- **Why relevant:** Challenges the standard pipeline where data-flow context is explicitly extracted, instead letting the LLM perform implicit localization.
- [Paper](https://github.com/CUHK-Shenzhen-SE/D4C)

**CodeCorrector: Context-Aware Prompting for LLM-Based Program Repair**
- Automated Software Engineering journal, 2025
- Uses Chain-of-Thought to analyze test failures, select relevant context, and build context-aware repair prompts. Fixes 38 unique defects that no baseline can handle.
- **Why relevant:** Another context-selection approach for repair, using test-failure-driven reasoning rather than data-flow analysis.
- [Paper](https://link.springer.com/article/10.1007/s10515-025-00512-w)

---

## 5. Distillation for Lightweight Code Models

**Reasoning Distillation for Lightweight Automated Program Repair**
- arXiv:2601.10987, January 2026
- Distills structured symbolic reasoning tags from a large teacher model into a CodeT5-based student for fix-type classification. Improves macro-averaged performance on rare bug categories without increasing model size.
- **Why relevant:** The most directly comparable methodological approach -- distilling program analysis signals into a lightweight model for repair. The paper under review does the same but with data-flow signals specifically.
- [Paper](https://arxiv.org/abs/2601.10987)

---

## 6. Retrieval-Augmented Code Repair (BM25 + Structural Features)

**SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution**
- ACL Findings 2025
- Uses a coarse-to-fine retrieval pipeline combining BM25 with a fine-tuned 7B retriever (initialized from GraphCodeBERT-style embeddings) for code file retrieval, followed by a fine-tuned 72B editor. Achieves 32.8% on SWE-Bench Verified.
- **Why relevant:** Combines sparse retrieval (BM25) with neural structural code features in a retrieval pipeline for repo-level repair.
- [Paper](https://aclanthology.org/2025.findings-acl.62.pdf)

---

## 7. CodeQL + LLM Integration

**CORE: Resolving Code Quality Issues using LLMs**
- ACM, 2024-2025
- Uses CodeQL to identify code quality issues, then applies LLMs to generate fixes, filtering suggestions that fail original CodeQL rules. Achieves 88.81% success on Python files passing CodeQL checks.
- **Why relevant:** Uses a static analysis tool (CodeQL) to both identify and validate repair context -- a pipeline the authors should compare against.
- [Paper](https://dl.acm.org/doi/pdf/10.1145/3643762)

**CQLLM: A Framework for Generating CodeQL Security Vulnerability Detection Code Based on LLM**
- Applied Sciences, January 2026
- Uses LLMs to generate CodeQL queries for vulnerability detection, addressing CodeQL's high barrier to entry.
- [Paper](https://www.mdpi.com/2076-3417/16/1/517)

**Guiding AI to Fix Its Own Flaws: LLM-Driven Secure Code Generation with CodeQL Feedback**
- arXiv:2506.23034, 2025
- Feeds CodeQL feedback and contextual information to GPT-4o for post-hoc vulnerability repair.
- [Paper](https://arxiv.org/abs/2506.23034)

---

## 8. Surveys

**A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications**
- arXiv:2506.23749, June 2025; published in TOSEM 2026
- Covers 63 systems across four paradigms. Categorizes analysis-augmented generation into failing-test evidence, semantics-aware slices, and execution traces.
- [Paper](https://arxiv.org/abs/2506.23749)

**Towards an Understanding of Context Utilization in Code Intelligence**
- arXiv:2504.08734, April 2025
- Studies how LLMs utilize different types of context (AST, data flow, dependency graphs) for code tasks.
- [Paper](https://arxiv.org/abs/2504.08734)

---

## Summary of Coverage Gaps the Authors Should Address

The most critical papers to cite and differentiate from are:

1. **ARISE** (May 2026) -- uses def-use edges in a repo-level graph for agentic repair; the closest competitor.
2. **Reasoning Distillation for Lightweight APR** (Jan 2026) -- distills analysis signals into a lightweight model; the closest methodological analog.
3. **LLMxCPG** (USENIX Security 2025) -- CPG-based context pruning achieving 67-91% code reduction.
4. **CodeBadger** (ICSE 2026 workshop) -- operationalizes CPG data-flow analysis for LLM code tasks.
5. **KGCompass** (March 2025) -- knowledge-graph-based context selection for repo-level repair.
6. **GREPO** (Feb 2026) -- GNN benchmark for repo-level bug localization.
7. **Appatch** (USENIX Security 2025) -- semantics-aware slicing for LLM repair.
8. **The fault localization granularity studies** (April 2026) -- empirical evidence on optimal context granularity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c41daaa0-ec25-4f7d-bac9-95340db80c37",
  "isSidechain": true,
  "agentId": "a1c6187e43302749f",
  "requestId": "req_011CauNxeWvUamNG2eTZEosL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63bee4db-2144-4511-9dff-8ff9a5ce887b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiAawPiqQqsEFpfVFQGM2S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3022,
      "cache_read_input_tokens": 28484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3022,
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
