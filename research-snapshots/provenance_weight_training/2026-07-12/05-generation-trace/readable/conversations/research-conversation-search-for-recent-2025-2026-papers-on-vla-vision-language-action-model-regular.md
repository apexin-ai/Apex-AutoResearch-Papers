# Research conversation: Search for recent (2025-2026) papers on VLA (Vision-Language-Action) model regularization, token operations, and general

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a58843e9da9a4c725.jsonl`
- **Structured JSON:** [`66780f1d457cee14151e.json`](../../sessions/66/66780f1d457cee14151e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-13T04:58:05.681Z_

Search for recent (2025-2026) papers on VLA (Vision-Language-Action) model regularization, token operations, and generalization that might compete with or overlap with the idea of "adaptive token masking for VLA finetuning." I need to find papers the idea might have missed.

Search queries to use:
1. "VLA token pruning generalization 2025 2026 site:arxiv.org"
2. "vision language action model regularization finetuning 2026"
3. "VLA visual token dropout masking regularization"
4. "adaptive token masking transformer regularization 2025 2026"
5. "visual token selection VLA robotic manipulation"
6. "VLA-Pruner temporal visual token pruning"
7. "information bottleneck visual tokens robot learning"
8. "counterfactual augmentation robot imitation learning"

For any relevant papers found, note: title, venue, date, approach, and how it relates to adaptive token masking for VLA finetuning. Use WebFetch on the most relevant 2-3 papers. Report concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "7bb1e957-e3e1-49d5-847c-bd689ac084dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T04:58:05.694Z_

```json
{
  "parentUuid": "7bb1e957-e3e1-49d5-847c-bd689ac084dc",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
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
  "uuid": "ade642a2-7b9f-49c8-bedf-f5b12a0f084c",
  "timestamp": "2026-05-13T04:58:05.694Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T04:58:12.924Z_



I'll start by loading the WebSearch and WebFetch tools, then run the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ade642a2-7b9f-49c8-bedf-f5b12a0f084c",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayyZTPtowXNu7wuWMSFW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "430001ab-f2ec-4029-9e76-4b917cf788bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoSWe965Zn7LynhtPP1wRT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 781,
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

_source line 4 · 2026-05-13T04:58:13.426Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JGctE3joM3K9nozXVTxxG8`</summary>

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
  "parentUuid": "430001ab-f2ec-4029-9e76-4b917cf788bd",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayyZTPtowXNu7wuWMSFW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2592d38d-1208-4b8f-904d-cfdfb9ae9dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoSWe965Zn7LynhtPP1wRT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 7304,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 781
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 781,
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

_source line 5 · 2026-05-13T04:58:13.429Z_

<details><summary>↩ Tool result · `toolu_01JGctE3joM3K9nozXVTxxG8`</summary>

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
  "parentUuid": "2592d38d-1208-4b8f-904d-cfdfb9ae9dba",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "463b7fd0-bf9c-44d2-878b-973bea69639e",
  "sourceToolAssistantUUID": "2592d38d-1208-4b8f-904d-cfdfb9ae9dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T04:58:16.736Z_



Now let me run all 8 search queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "463b7fd0-bf9c-44d2-878b-973bea69639e",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011Cayya2SVS3s9tg93yBCxE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d6d4194-24da-4ed2-801d-1839aa9ddcbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP7cgmnYtrdnAC4zJR8vts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 7 · 2026-05-13T04:58:18.095Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qo34KCrwRUuqFojpKzbZSd`</summary>

```json
{
  "query": "VLA token pruning generalization 2025 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d6d4194-24da-4ed2-801d-1839aa9ddcbe",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011Cayya2SVS3s9tg93yBCxE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f1f87fc-7380-4d13-8b99-f85367ec65bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP7cgmnYtrdnAC4zJR8vts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 8 · 2026-05-13T04:58:18.645Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JBPnj5tjQFCuC4GcrR6VN9`</summary>

```json
{
  "query": "vision language action model regularization finetuning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f1f87fc-7380-4d13-8b99-f85367ec65bd",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011Cayya2SVS3s9tg93yBCxE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6495f61a-728d-43c2-88bd-589d881a4607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP7cgmnYtrdnAC4zJR8vts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 9 · 2026-05-13T04:58:19.088Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lin17KHxLmpRqFkqrtCGLV`</summary>

```json
{
  "query": "VLA visual token dropout masking regularization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6495f61a-728d-43c2-88bd-589d881a4607",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011Cayya2SVS3s9tg93yBCxE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc91edc6-0e34-4dd5-970d-f5c292195045",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP7cgmnYtrdnAC4zJR8vts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 10 · 2026-05-13T04:58:19.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AsyJk6uYWC8Ur4E9irLPGa`</summary>

```json
{
  "query": "adaptive token masking transformer regularization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc91edc6-0e34-4dd5-970d-f5c292195045",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011Cayya2SVS3s9tg93yBCxE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac669e09-f857-4210-97ea-782fb02b8ce4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP7cgmnYtrdnAC4zJR8vts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 11 · 2026-05-13T04:58:20.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JhqKqUGi78AeeT5XBpjmqr`</summary>

```json
{
  "query": "visual token selection VLA robotic manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac669e09-f857-4210-97ea-782fb02b8ce4",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011Cayya2SVS3s9tg93yBCxE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a135274a-9bb9-40b2-9dbf-13b52f2fd653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP7cgmnYtrdnAC4zJR8vts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 12 · 2026-05-13T04:58:20.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UUjBvBdJpytiehvubxa2Xz`</summary>

```json
{
  "query": "VLA-Pruner temporal visual token pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a135274a-9bb9-40b2-9dbf-13b52f2fd653",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011Cayya2SVS3s9tg93yBCxE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5f0e8ec-d8a3-4a88-808b-5da591e12933",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP7cgmnYtrdnAC4zJR8vts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 13 · 2026-05-13T04:58:21.186Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YSt5auu6D2Ai1YY3bnKQvQ`</summary>

```json
{
  "query": "information bottleneck visual tokens robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5f0e8ec-d8a3-4a88-808b-5da591e12933",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011Cayya2SVS3s9tg93yBCxE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3687a4d1-2020-4a17-8e51-6d433cabeaa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP7cgmnYtrdnAC4zJR8vts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 14 · 2026-05-13T04:58:21.489Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QjzKDYKesdbZWyH8XAB6Ps`</summary>

```json
{
  "query": "counterfactual augmentation robot imitation learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3687a4d1-2020-4a17-8e51-6d433cabeaa2",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011Cayya2SVS3s9tg93yBCxE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c97c14dd-c923-4a20-a18b-6f58752b49ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP7cgmnYtrdnAC4zJR8vts",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8085,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 396,
          "cache_read_input_tokens": 8085,
          "cache_creation_input_tokens": 1909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1909,
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

_source line 15 · 2026-05-13T04:58:26.860Z_

<details><summary>↩ Tool result · `toolu_01Lin17KHxLmpRqFkqrtCGLV`</summary>

```text
Web search results for query: "VLA visual token dropout masking regularization"

Links: [{"title":"Enhancing Vision-Language Model Reliability with Uncertainty-Guided Dropout Decoding","url":"https://arxiv.org/html/2412.06474"},{"title":"From Uncertainty to Trust: Enhancing Reliability in Vision-Language Models with Uncertainty-Guided Dropout Decoding","url":"https://arxiv.org/html/2412.06474v1"},{"title":"Alignment, Mixture, and Regularization - BeingBeyond","url":"https://research.beingbeyond.com/rethink_vla"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/html/2410.04417v4"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"When LLaVA Meets Objects: Token Composition for Vision-Language-Models","url":"https://arxiv.org/html/2602.04864v1"},{"title":"TLM: Token-Level Masking for Transformers | OpenReview","url":"https://openreview.net/forum?id=7CTp2gwqin"},{"title":"FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning","url":"https://arxiv.org/html/2507.23318v3"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference | OpenReview","url":"https://openreview.net/forum?id=80faIPZ67S"}]

Based on the search results, here are the key findings related to VLA visual token dropout, masking, and regularization:

## Uncertainty-Guided Token Dropout

After quantifying the uncertainty in visual inputs, Dropout Decoding drops out visual tokens to regularize uncertainty and employs an ensemble-based decoding approach to stabilize generation. This approach introduces uncertainty-guided token dropout, which applies the dropout principle to input visual tokens instead of model parameters, and during inference rather than training.

## Token Dropout in Vision-Language-Action Models

In the context of VLA (Vision-Language-Action) models for robotics, research has explored sensory dropout approaches. However, stochastic modality dropout does not consistently improve performance, suggesting that simple dropout regularization strategies may have limited benefits at scale.

## Visual Token Pruning and Compression

Beyond dropout, researchers have developed more sophisticated visual token masking techniques. VLA-IAP (Interaction-Aligned Pruning) is a training-free method that shifts embodied visual compression toward an Explicit Interaction-First paradigm. The method develops an Interaction-Aligned Dynamic Strategy that adjusts pruning intensity based on semantic-motion alignment.

## Token-Level Masking for Transformers

More broadly, Token-Level Masking (TLM) is a training strategy for Transformers to regularize the connections of self-attention, consisting of two masking techniques that are effective and easy to implement.

The research suggests that while visual token dropout and masking are important techniques for improving efficiency and robustness in vision-language and vision-language-action models, their effectiveness varies depending on the specific application and implementation approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc91edc6-0e34-4dd5-970d-f5c292195045",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "ca6a94c9-229a-451d-b784-251b313de7a5",
  "sourceToolAssistantUUID": "cc91edc6-0e34-4dd5-970d-f5c292195045",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T04:58:26.933Z_

<details><summary>↩ Tool result · `toolu_01AsyJk6uYWC8Ur4E9irLPGa`</summary>

```text
Web search results for query: "adaptive token masking transformer regularization 2025 2026"

Links: [{"title":"[2505.11746] Token Masking Improves Transformer-Based Text Classification","url":"https://arxiv.org/abs/2505.11746"},{"title":"TLM: Token-Level Masking for Transformers | OpenReview","url":"https://openreview.net/forum?id=7CTp2gwqin"},{"title":"[2310.18738] TLM: Token-Level Masking for Transformers","url":"https://arxiv.org/abs/2310.18738"},{"title":"Token Masking Improves Transformer-Based Text Classification","url":"https://arxiv.org/html/2505.11746v1"},{"title":"A-ViT: Adaptive Tokens for Efﬁcient Vision Transformer Hongxu Yin Arash Vahdat","url":"https://openaccess.thecvf.com/content/CVPR2022/papers/Yin_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer_CVPR_2022_paper.pdf"},{"title":"Adaptive layer and token selection for efficient fine-tuning of vision transformers - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0925231225018880"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Layer- and Timestep-Adaptive Differentiable Token Compression Ratios for","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/You_Layer-_and_Timestep-Adaptive_Differentiable_Token_Compression_Ratios_for_Efficient_Diffusion_CVPR_2025_paper.pdf"},{"title":"Token Masking Improves Transformer-Based Text ...","url":"https://www.arxiv.org/pdf/2505.11746"},{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"}]

Here are the search results for "adaptive token masking transformer regularization 2025 2026":

## Recent Research on Token Masking and Transformer Regularization

**Token Masking for Text Classification (2025)**

A recent paper proposes token masking regularization, which randomly replaces input tokens with a special [MASK] token at probability p, introducing stochastic perturbations during training that lead to implicit gradient averaging to encourage deeper inter-token dependencies. Experiments on language identification and sentiment analysis across diverse models (mBERT, Qwen2.5-0.5B, TinyLlama-1.1B) show consistent improvements over standard regularization techniques, with p = 0.1 identified as a strong general default.

**Token-Level Masking (TLM) Strategy**

A token-level masking strategy for Transformers proposes a regularization scheme based on token-level rather than structure-level to reduce overfitting, devising a Token-Level Masking (TLM) training strategy to regularize the connections of self-attention.

**Adaptive Token Compression (2025-2026)**

The search results also reveal several 2025-2026 works on adaptive token handling, including a DiffCR framework with token-level routing schemes and differentiable compression ratios, and recent research on adaptive layer and token selection for efficient fine-tuning of vision transformers.

The field shows active research interest in combining adaptivity with token masking and regularization techniques for more efficient and effective transformer models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac669e09-f857-4210-97ea-782fb02b8ce4",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "87adc40a-d437-401e-9d3b-88ae7f478f1b",
  "sourceToolAssistantUUID": "ac669e09-f857-4210-97ea-782fb02b8ce4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T04:58:27.208Z_

<details><summary>↩ Tool result · `toolu_01Qo34KCrwRUuqFojpKzbZSd`</summary>

```text
Web search results for query: "VLA token pruning generalization 2025 2026 site:arxiv.org"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"[2506.12723] SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/abs/2506.12723"},{"title":"Efficient Long-Horizon Vision-Language-Action Models via Static-Dynamic","url":"https://arxiv.org/pdf/2602.03983"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"DTP:A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models","url":"https://arxiv.org/html/2601.16065"},{"title":"[2602.02212] MAIN-VLA: Modeling Abstraction of Intention and eNvironment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.02212"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"}]

Based on the search results from arXiv, here are recent papers on VLA (Vision-Language-Action) token pruning and generalization from 2025-2026:

## Key Recent Papers:

1. **VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment** (March 2026)
   - Evaluation spans three VLA backbones and three benchmarks focusing on generalization, long-horizon actions, and complex reasoning. While all methods degrade with lower retention, VLA-IAP demonstrates superior robustness, and at 70% retention, VLA-IAP surpasses the unpruned baseline on multiple metrics.

2. **LightVLA: Differentiable Token Pruning** (September 2025)
   - LightVLA is a differentiable token pruning framework for VLA models that generates dynamic queries to evaluate visual token importance and adopts Gumbel softmax to enable differentiable token selection, learning to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution.

3. **VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning** (February 2026)
   - VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention for action-level importance, proposing a novel dual-level token selection strategy that adaptively preserves a compact, informative set of visual tokens.

4. **SP-VLA: Joint Model Scheduling and Token Pruning** (June 2025)
   - The LIBERO-Goal task allows a relatively large degree of token pruning while maintaining accuracy, while the LIBERO-Long task only supports a smaller pruning rate, indicating that as task complexity increases, higher spatial perception capability is required from the VLA model.

5. **SpecPrune-VLA: Action-Aware Pruning** (February 2026)
   - EfficientVLA prunes visual tokens using single-layer attention heuristics and supplements with diverse patches, yet this risks introducing task-irrelevant content and lacks global context awareness.

These papers collectively address the challenge of efficient VLA inference while maintaining generalization across diverse robotic tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f1f87fc-7380-4d13-8b99-f85367ec65bd",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "449c7504-b4f5-4309-ab20-465926a41750",
  "sourceToolAssistantUUID": "1f1f87fc-7380-4d13-8b99-f85367ec65bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T04:58:27.696Z_

<details><summary>↩ Tool result · `toolu_01JBPnj5tjQFCuC4GcrR6VN9`</summary>

```text
Web search results for query: "vision language action model regularization finetuning 2026"

Links: [{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"RL4VLM","url":"https://rl4vlm.github.io/"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v2"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://arxiv.org/html/2603.03818"},{"title":"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2603.23202v1"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly","url":"https://arxiv.org/pdf/2603.03818"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior","url":"https://arxiv.org/html/2604.01570v1"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging","url":"https://arxiv.org/html/2512.08333v1"}]

The search has returned several relevant results about vision-language-action (VLA) models with focus on regularization and finetuning techniques from 2025-2026. Here are the key findings:

## Recent VLA Finetuning and Regularization Research (2025-2026)

**Fine-Tuning Approaches:**

Recent vision-language-action models (VLAs) build upon pretrained vision-language models and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization.

**Gaze-Regularized Training:**
A gaze-regularized training framework aligns VLA models' internal attention with human visual patterns without architectural modifications or inference-time overhead, transforming temporally aggregated gaze heatmaps into patch-level distributions and regularizing the transformer's attention through KL divergence. This approach yields 4-12% improvements across manipulation benchmarks.

**Feasible Action Neighborhood (FAN) Regularization:**
Prevalent VLA training methodologies do not exploit the feasible action neighborhood property, leading to poor generalization and low sample efficiency; a FAN-guided regularizer shapes the model's output distribution to align with the geometry of FAN. This method achieves significant improvement in sample efficiency and success rate in both in-distribution and out-of-distribution scenarios across supervised and reinforced finetuning.

**Parameter Merging for Robust Finetuning:**
By interpolating the weights of the pre-trained generalist policy before and after finetuning on the target task, checkpoints can match the performance of the finetuned policy while generalizing significantly better to unseen variations; this approach also preserves the generalist capabilities of the pre-trained policy on other tasks.

**Continual Learning with Pretrained VLAs:**
Simple experience replay achieves near-zero forgetting with surprisingly small buffers in large-scale pretrained VLAs, and large-scale pretraining fundamentally changes the stability–plasticity dynamics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6495f61a-728d-43c2-88bd-589d881a4607",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "43cdd69a-6a30-4cb9-b0cb-7dd04ec7d8e7",
  "sourceToolAssistantUUID": "6495f61a-728d-43c2-88bd-589d881a4607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T04:58:28.105Z_

<details><summary>↩ Tool result · `toolu_01UUjBvBdJpytiehvubxa2Xz`</summary>

```text
Web search results for query: "VLA-Pruner temporal visual token pruning"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation","url":"https://arxiv.org/html/2603.06480"},{"title":"[2603.06480] History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation","url":"https://arxiv.org/abs/2603.06480"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"}]

Based on the search results, here's what I found about VLA-Pruner:

## Overview

VLA-Pruner is a method for accelerating Vision-Language-Action (VLA) models by using token pruning to efficiently process continuous visual streams, which has emerged as an effective approach for efficient VLA inference.

## Key Innovation

VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention, estimated via temporal smoothing, for action-level importance.

## Problem It Addresses

Traditional VLM-specific token pruning methods select tokens based solely on semantic salience metrics like prefill attention, overlooking VLA's dual-system nature of semantic understanding and action execution, which causes these methods to bias token retention toward semantic cues and discard critical information for action generation.

## Technical Approach

VLA-Pruner selects tokens using last-layer prefill attention and temporal smoothing of action-to-vision attention averaged over the latter half layers, with pruned tokens dropped from the rest of the prefill layers.

## Performance

VLA-Pruner achieves state-of-the-art performance across multiple VLA architectures and diverse robotic tasks. The method is designed as "a versatile plug-and-play VLA-specific token prune method" and "a single, plug-and-play token pruning module."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5f0e8ec-d8a3-4a88-808b-5da591e12933",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "21a17098-d18d-44f8-9af4-dfe721db1f2a",
  "sourceToolAssistantUUID": "b5f0e8ec-d8a3-4a88-808b-5da591e12933",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T04:58:28.698Z_

<details><summary>↩ Tool result · `toolu_01YSt5auu6D2Ai1YY3bnKQvQ`</summary>

```text
Web search results for query: "information bottleneck visual tokens robot learning"

Links: [{"title":"Token Bottleneck: One Token to Remember Dynamics","url":"https://arxiv.org/html/2507.06543v1"},{"title":"Token Bottleneck: One Token to Remember Dynamics Taekyung Kim1 Dongyoon Han1","url":"https://arxiv.org/pdf/2507.06543"},{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"[2507.06543] Token Bottleneck: One Token to Remember Dynamics","url":"https://arxiv.org/abs/2507.06543"},{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy","url":"https://arxiv.org/html/2605.07931v1"},{"title":"NeurIPS Poster Token Bottleneck: One Token to Remember Dynamics","url":"https://neurips.cc/virtual/2025/poster/115268"},{"title":"Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/html/2407.15219v1"},{"title":"Token Bottleneck: One Token to Remember Dynamics","url":"https://token-bottleneck.github.io/"},{"title":"Token Bottleneck: One Token to Remember Dynamics | OpenReview","url":"https://openreview.net/forum?id=x7t7B5CFHm"},{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"}]

Here are the search results for "information bottleneck visual tokens robot learning":

## Key Research Areas

**Token Bottleneck (ToBo) for Robot Learning:**

Token Bottleneck (ToBo) is a self-supervised learning pipeline that squeezes a scene into a bottleneck token and predicts the subsequent scene using minimal patches as hints. The ToBo pipeline facilitates learning of sequential scene representations by conservatively encoding the reference scene into a compact bottleneck token during the squeeze step, and in the expansion step, guides the model to capture temporal dynamics by predicting the target scene using the bottleneck token along with few target patches as hints. 

This method significantly surpasses previous self-supervised visual representation learning methods designed for static and dynamic scenes on various robot manipulation and locomotion tasks. Deploying the pre-trained model on physical robots confirms its robustness and effectiveness in real-world environments.

**Information Bottleneck-Inspired Token Efficiency:**

Beyond the specific ToBo approach, there are related techniques using information bottleneck principles. IBTM (Transformer with Information Bottleneck inspired Token Merging) proposes a novel and compact transformer block that performs token merging in a learnable scheme. IBTM is compatible with popular compact transformer networks such as MobileViT and EfficientViT, and reduces the FLOPs and inference time of vision transformers while maintaining or even improving prediction accuracy.

**Recent Applications to VLA Models:**

The significant computational overhead of processing redundant visual tokens remains a critical bottleneck for real-time robotic deployment in Vision-Language-Action models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3687a4d1-2020-4a17-8e51-6d433cabeaa2",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "b1b6b723-acb0-4a78-bc79-69a57e820902",
  "sourceToolAssistantUUID": "3687a4d1-2020-4a17-8e51-6d433cabeaa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T04:58:29.566Z_

<details><summary>↩ Tool result · `toolu_01QjzKDYKesdbZWyH8XAB6Ps`</summary>

```text
Web search results for query: "counterfactual augmentation robot imitation learning"

Links: [{"title":"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations","url":"https://arxiv.org/html/2411.16959"},{"title":"[2411.16959] RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations","url":"https://arxiv.org/abs/2411.16959"},{"title":"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations | alphaXiv","url":"https://www.alphaxiv.org/resources/2411.16959v2"},{"title":"Offline Imitation Learning with Variational Counterfactual Reasoning","url":"https://arxiv.org/html/2310.04706v4"},{"title":"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations","url":"https://www.researchgate.net/publication/386143974_RoCoDA_Counterfactual_Data_Augmentation_for_Data-Efficient_Robot_Learning_from_Demonstrations"},{"title":"Offline Imitation Learning with Variational Counterfactual Reasoning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/8833c8aa10542d24d693bbaf6a4598f5-Paper-Conference.pdf"},{"title":"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations | Request PDF","url":"https://www.researchgate.net/publication/395230290_RoCoDA_Counterfactual_Data_Augmentation_for_Data-Efficient_Robot_Learning_from_Demonstrations"},{"title":"JUICER: Data-Efficient Imitation Learning for Robotic Assembly","url":"https://imitation-juicer.github.io/"},{"title":"Counterfactual Behavior Cloning: Offline Imitation Learning from Imperfect Human Demonstrations","url":"https://arxiv.org/html/2505.10760"},{"title":"Counterfactual Behavior Cloning: Offline Imitation Learning from Imperfect Human Demonstrations | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.10760"}]

I found several highly relevant research papers on counterfactual augmentation in robot imitation learning. Here are the key findings:

## RoCoDA: Counterfactual Data Augmentation

RoCoDA is a novel method that unifies the concepts of invariance, equivariance, and causality within a single framework to enhance data augmentation for imitation learning. RoCoDA leverages causal invariance by modifying task-irrelevant subsets of the environment state, and exploits SE(3) equivariance by applying rigid body transformations to object poses and adjusting corresponding actions to generate synthetic demonstrations.

The method demonstrates improvements in policy performance, generalization, and sample efficiency on robotic manipulation tasks, with policies exhibiting robust generalization to unseen object poses, textures, and distractors. The policies trained with RoCoDA exhibit emergent behaviors such as re-grasping, indicating they possess a deeper understanding of task dynamics.

## Offline Imitation Learning with Variational Counterfactual Reasoning

Another approach uses counterfactual reasoning for offline imitation learning. This method generates counterfactual expert data to improve the generalization of the learned agent.

## Counterfactual Behavior Cloning

A recent technique enables robots to extrapolate what a human teacher meant by expanding the dataset to include actions close to demonstrated behaviors (counterfactual actions that the human teacher could have intended).

These approaches represent active research directions in making robot imitation learning more sample-efficient and robust by leveraging counterfactual reasoning and causal structure.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c97c14dd-c923-4a20-a18b-6f58752b49ac",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "0dde8a8b-0678-4d4b-9f97-621bc088ceb0",
  "sourceToolAssistantUUID": "c97c14dd-c923-4a20-a18b-6f58752b49ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T04:58:30.638Z_

<details><summary>↩ Tool result · `toolu_01JhqKqUGi78AeeT5XBpjmqr`</summary>

```text
Web search results for query: "visual token selection VLA robotic manipulation"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/html/2602.20566"},{"title":"(PDF) VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://www.researchgate.net/publication/388685612_VLA-Cache_Towards_Efficient_Vision-Language-Action_Model_via_Adaptive_Token_Caching_in_Robotic_Manipulation/fulltext/67a2d84c8311ce680c52f13c/VLA-Cache-Towards-Efficient-Vision-Language-Action-Model-via-Adaptive-Token-Caching-in-Robotic-Manipulation.pdf?origin=scientificContributions"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"}]

Based on the search results, I found several recent papers on visual token selection for Vision-Language-Action (VLA) models in robotic manipulation:

## Key Research Areas

**Visual Token Pruning and Selection Methods:**

VLA-IAP proposes a training-free visual token pruning framework that shifts embodied visual compression from a passive Perception-First bias to an explicit Interaction-First paradigm. Research reveals that relying solely on semantic saliency leads to catastrophic failures in precise robotic manipulation, highlighting the critical need to preserve geometric continuity by integrating edge-enhanced structural anchors with an adaptive semantic-motion alignment strategy.

VLA-Pruner adopts a dual-objective importance criterion for visual token retention: vision-language prefill attention scores for semantic relevance and action decode attention scores for execution precision.

Compressor-VLA proposes a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models. Experimentally, Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline.

**Temporal and Interaction-Aware Approaches:**

VLA-Cache is a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames, exploiting the temporal continuity in robotic manipulation.

BFA++ introduces a hierarchical pruning strategy guided by two-level importance predictors: an intra-view predictor highlights task-relevant regions within each image to suppress spatial noise, while an inter-view predictor identifies critical camera views throughout different manipulation phases to reduce cross-view redundancy.

**Learnable Pruning:**

LightVLA addresses efficiency through adaptive, performance-driven pruning of visual tokens by generating dynamic queries to evaluate visual token importance and adopting Gumbel softmax to enable differentiable token selection, learning to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a135274a-9bb9-40b2-9dbf-13b52f2fd653",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "c0db9ffd-8248-4865-8dd9-c79527588d78",
  "sourceToolAssistantUUID": "a135274a-9bb9-40b2-9dbf-13b52f2fd653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-13T04:58:37.131Z_

Excellent results. Now let me fetch the most relevant papers in detail. I'll pick the top 3-4 that most directly compete with or overlap with "adaptive token masking for VLA finetuning": (1) Gaze-Regularized VLA, (2) FAN regularization for VLA finetuning, (3) VLA-Pruner, and (4) the "Rethink VLA" page on alignment/regularization. Let me also check the Token Bottleneck and the robust finetuning via parameter merging papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0db9ffd-8248-4865-8dd9-c79527588d78",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayybHzA1NtCjTyERqMRx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f979b36e-b7bf-44d2-9d3a-4b512784e6f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EU7kQAiLyFVMPyXGsNxB8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2731,
      "cache_creation_input_tokens": 5517,
      "cache_read_input_tokens": 9994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5517,
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

_source line 24 · 2026-05-13T04:58:39.524Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0119imk6QPGDLLMLVhkr9K9q`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.23202",
  "prompt": "Extract the full title, authors, date, abstract, and key method details for this paper on gaze-regularized VLA models. What regularization technique do they use? How does it improve generalization? What benchmarks are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f979b36e-b7bf-44d2-9d3a-4b512784e6f4",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayybHzA1NtCjTyERqMRx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6e9784e-51d9-4977-a386-d343797053a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EU7kQAiLyFVMPyXGsNxB8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2731,
      "cache_creation_input_tokens": 5517,
      "cache_read_input_tokens": 9994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5517,
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

_source line 25 · 2026-05-13T04:58:41.325Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H1f3WWDoJkCD5nt78hsL6n`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.01570",
  "prompt": "Extract the full title, authors, date, abstract, and key method details for this paper on Feasible Action Neighborhood (FAN) regularization for VLA finetuning. What regularization technique do they propose? How does it relate to generalization during finetuning? What are the key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6e9784e-51d9-4977-a386-d343797053a0",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayybHzA1NtCjTyERqMRx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c69b037f-be3f-4c81-a5b5-62f38b92f2ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EU7kQAiLyFVMPyXGsNxB8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2731,
      "cache_creation_input_tokens": 5517,
      "cache_read_input_tokens": 9994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5517,
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

_source line 26 · 2026-05-13T04:58:42.400Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WCtCiaa19Y3wjmT3TsEXC5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.08333",
  "prompt": "Extract the full title, authors, date, abstract, and key method details for this paper on robust finetuning of VLA robot policies via parameter merging. How does weight interpolation improve generalization? What are the key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c69b037f-be3f-4c81-a5b5-62f38b92f2ba",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayybHzA1NtCjTyERqMRx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8b878b0-4bf9-4787-8380-175f26360ab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EU7kQAiLyFVMPyXGsNxB8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2731,
      "cache_creation_input_tokens": 5517,
      "cache_read_input_tokens": 9994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5517,
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

### Tool result

_source line 27 · 2026-05-13T04:58:44.558Z_

<details><summary>↩ Tool result · `toolu_0119imk6QPGDLLMLVhkr9K9q`</summary>

```text
# Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation

**Full Title:** Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation

**Authors:** Anupam Pani, Yanchao Yang

**Date:** Submitted March 24, 2026; revised April 7, 2026

## Abstract Summary

The researchers address limitations in robotic manipulation by introducing a framework that leverages human visual attention patterns. The work proposes "aligning VLA models' internal attention with human visual patterns without architectural modifications or inference-time overhead."

## Key Method Details

**Regularization Technique:** The approach uses KL divergence to regularize transformer attention patterns. Specifically, they "transform temporally aggregated gaze heatmaps into patch-level distributions and regularize the transformer's attention through KL divergence."

**Mechanism:** This creates "an inductive bias toward task-relevant features while preserving deployment efficiency," guiding the model toward human-like visual strategies without requiring eye-tracking equipment.

## Performance Improvements & Generalization

The method demonstrates "4-12% improvements across manipulation benchmarks" and achieves "equivalent performance with fewer training steps." Notably, models maintain "robustness under lighting variations and sensor noise," indicating improved generalization capabilities.

## Benchmarks

The abstract references "manipulation benchmarks" but doesn't specify particular benchmark names in the provided excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6e9784e-51d9-4977-a386-d343797053a0",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "a5f1ee52-79dd-41f6-b785-4ad4a63a5252",
  "sourceToolAssistantUUID": "b6e9784e-51d9-4977-a386-d343797053a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-13T04:58:46.342Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PHDKX3uv9aeAT4VCrDmryS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.16449",
  "prompt": "Extract the full title, authors, date, abstract, and key method details for VLA-Pruner. What is the dual-level importance criterion? How does temporal smoothing work? What are the key results on generalization vs efficiency? What VLA architectures does it support?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5f1ee52-79dd-41f6-b785-4ad4a63a5252",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayybHzA1NtCjTyERqMRx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4d478a8-eefb-4d1b-8e6a-9df0096ceb9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EU7kQAiLyFVMPyXGsNxB8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2731,
      "cache_creation_input_tokens": 5517,
      "cache_read_input_tokens": 9994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5517,
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

_source line 29 · 2026-05-13T04:58:46.416Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UAwniaasJreLxa9cNZK8pw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.06543",
  "prompt": "Extract the full title, authors, date, abstract, and key method details for Token Bottleneck (ToBo). How does squeezing a scene into a bottleneck token help robot learning? What tasks and environments were tested? What are the key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4d478a8-eefb-4d1b-8e6a-9df0096ceb9a",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayybHzA1NtCjTyERqMRx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b0f4058-3c34-484c-9c1a-287b3ac37a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EU7kQAiLyFVMPyXGsNxB8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2731,
      "cache_creation_input_tokens": 5517,
      "cache_read_input_tokens": 9994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5517,
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

### Tool result

_source line 30 · 2026-05-13T04:58:47.464Z_

<details><summary>↩ Tool result · `toolu_01WCtCiaa19Y3wjmT3TsEXC5`</summary>

```text
# Paper Summary: Robust Finetuning of Vision-Language-Action Robot Policies

## Full Title
"Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging"

## Authors & Date
**Authors:** Yajat Yadav, Zhiyuan Zhou, Andrew Wagenmaker, Karl Pertsch, Sergey Levine

**Submission:** December 9, 2025 (latest revision: February 27, 2026)

**Venue:** The Fourteenth International Conference on Learning Representations 2026

## Abstract
The researchers address overfitting during finetuning of generalist robot policies. They note that "generalist robot policies, trained on large and diverse datasets, have demonstrated the ability to generalize across a wide spectrum of behaviors" but struggle when adapted to new tasks with limited data.

## Core Method
The key innovation involves **weight interpolation between finetuned and pretrained model parameters**. Rather than using only the finetuned weights, the method blends them with the original pretrained weights to create a single unified policy.

## How Weight Interpolation Improves Generalization
By averaging model parameters, the technique preserves the broad competencies learned during pretraining while incorporating new task-specific knowledge. This prevents catastrophic forgetting of previously learned abilities while maintaining robustness to task variations.

## Key Results
- The merged model outperforms both purely pretrained and purely finetuned versions on out-of-distribution task variations
- Performance scales with the amount of pretraining data
- Enables continual skill acquisition without sacrificing existing generalist capabilities
- Validated through both simulated and real-world experiments
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8b878b0-4bf9-4787-8380-175f26360ab3",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "a893289c-1ab7-45b6-afd6-d72fdcf60327",
  "sourceToolAssistantUUID": "a8b878b0-4bf9-4787-8380-175f26360ab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T04:58:47.503Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ue9AbSqfbrsmZ2Fut8xyci`</summary>

```json
{
  "url": "https://research.beingbeyond.com/rethink_vla",
  "prompt": "Extract any information about VLA regularization, token masking, dropout, or alignment techniques discussed on this page. What methods are covered? What is the main thesis?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a893289c-1ab7-45b6-afd6-d72fdcf60327",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayybHzA1NtCjTyERqMRx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f69ae68-c9fd-4db1-81dd-88caa80e1830",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EU7kQAiLyFVMPyXGsNxB8Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2731,
      "cache_creation_input_tokens": 5517,
      "cache_read_input_tokens": 9994,
      "output_tokens": 852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5517
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2731,
          "output_tokens": 852,
          "cache_read_input_tokens": 9994,
          "cache_creation_input_tokens": 5517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5517,
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

_source line 32 · 2026-05-13T04:58:49.750Z_

<details><summary>↩ Tool result · `toolu_01H1f3WWDoJkCD5nt78hsL6n`</summary>

```text
# Paper Summary: Feasible Action Neighborhood Prior for VLA Finetuning

**Full Title:** "Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior"

**Authors:** Haochen Niu, Kanyu Zhang, Shuyu Yin, Qinghai Guo, Peilin Liu, Fei Wen

**Submission Date:** April 2, 2026

**Venue:** CVPR 2026

## Abstract Overview

The researchers address a fundamental challenge in robotic manipulation: states typically have multiple near-equivalent actions rather than single correct solutions. They note that "prevalent VLA training methodologies are directly inherited from linguistic settings and do not exploit the FAN property."

## Proposed Regularization Technique

The core contribution is a **FAN-guided regularizer** that shapes model outputs to align with action feasibility. Specifically, they employ "a Gaussian prior that promotes locally smooth and unimodal predictions around the preferred direction and magnitude."

This approach exploits the inherent action tolerance in physical manipulation tasks, where slight variations in motion yield indistinguishable results.

## Generalization Connection

By recognizing that feasible action neighborhoods exist within manipulation tasks, their method improves generalization by encouraging the model to learn robust, smooth decision boundaries rather than overfitting to single correct actions.

## Key Results

The method demonstrates:
- Significant improvements in sample efficiency
- Enhanced success rates in both in-distribution and out-of-distribution scenarios
- Effectiveness across both reinforced and supervised finetuning settings
- Better alignment with realistic physical manipulation constraints
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c69b037f-be3f-4c81-a5b5-62f38b92f2ba",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "08b59591-bdfa-4510-b75e-b8814d8aacae",
  "sourceToolAssistantUUID": "c69b037f-be3f-4c81-a5b5-62f38b92f2ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-13T04:58:51.298Z_

<details><summary>↩ Tool result · `toolu_01PHDKX3uv9aeAT4VCrDmryS`</summary>

```text
# VLA-Pruner: Research Summary

## Title & Authors
**Full Title:** "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference"

**Authors:** Ziyan Liu, Yeqiu Chen, Hongyi Cai, Tao Lin, Shuo Yang, Zheng Liu, Bo Zhao

**Submission Date:** November 20, 2025 (latest revision: February 10, 2026)

## Abstract Overview
The paper addresses computational efficiency in Vision-Language-Action models for embodied AI. The authors note that existing pruning methods focusing solely on semantic salience "bias token retention toward semantic cues, discard critical information for action generation."

## Dual-Level Importance Criterion
VLA-Pruner employs two complementary metrics:
1. **Vision-language prefill attention** – captures semantic-level relevance
2. **Action decode attention** – estimated via temporal smoothing to assess action-level importance

## Temporal Smoothing Mechanism
The document indicates that temporal smoothing estimates action decode attention by exploiting "temporal continuity in robot manipulation," though specific mathematical details aren't provided in this abstract.

## Key Results
The paper reports "state-of-the-art performance across multiple VLA architectures and diverse robotic tasks," balancing computational efficiency with maintained performance.

## Supported Architectures
The abstract confirms compatibility across "multiple VLA architectures" but doesn't enumerate specific model names in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4d478a8-eefb-4d1b-8e6a-9df0096ceb9a",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "c8a1ddb1-55b0-4e05-9597-de2eba9f395f",
  "sourceToolAssistantUUID": "e4d478a8-eefb-4d1b-8e6a-9df0096ceb9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T04:58:52.287Z_

<details><summary>↩ Tool result · `toolu_01Ue9AbSqfbrsmZ2Fut8xyci`</summary>

```text
# VLA Regularization and Alignment Techniques

## Methods Covered

The paper examines three primary dimensions:

1. **Physical Alignment**: Tests four coordinate parameterizations (World-Relative, World-Delta, EEF-Relative, EEF-Delta), finding that "EEF-Relative reaches the highest average success rate (75.1%) with the largest improvement (+8.2%)" in frozen-VLM settings.

2. **Embodiment Mixture**: Evaluates progressively richer data combinations, from public datasets alone through simulated and real proprietary data.

3. **Training Regularization**: Investigates sensory dropout techniques and multi-stage fine-tuning approaches, including stochastic masking of visual and proprioceptive modalities.

## Main Thesis

The research challenges conventional scaling assumptions in robotic learning. The authors argue that "naively pooling heterogeneous robot datasets often induces negative transfer rather than gains," contradicting language model scaling patterns. Their key finding: "complex regularization strategies do not reliably translate into gains at scale," with direct end-to-end fine-tuning outperforming multi-stage curricula.

The overarching message emphasizes that **embodiment heterogeneity creates interference**, requiring careful architectural choices rather than simple data accumulation for effective VLA scaling.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f69ae68-c9fd-4db1-81dd-88caa80e1830",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "b6d0182e-c2d5-4925-a950-26b0fdb3d929",
  "sourceToolAssistantUUID": "2f69ae68-c9fd-4db1-81dd-88caa80e1830",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-13T04:58:52.375Z_

<details><summary>↩ Tool result · `toolu_01UAwniaasJreLxa9cNZK8pw`</summary>

```text
# Token Bottleneck (ToBo) Paper Summary

**Full Title:** Token Bottleneck: One Token to Remember Dynamics

**Authors:** Taekyung Kim, Dongyoon Han, Byeongho Heo, Jeongeun Park, Sangdoo Yun

**Date:** Submitted July 9, 2025; revised March 6, 2026 (NeurIPS 2025)

## Abstract Overview

The paper introduces a self-supervised learning approach that "squeezes a scene into a bottleneck token and predicts the subsequent scene using minimal patches as hints." This method helps models learn temporal dynamics in visual sequences.

## How Bottleneck Compression Supports Robot Learning

The squeeze-and-reconstruct design encourages the model to encode temporal dependencies into a compact representation. During the squeeze phase, a reference scene compresses into one bottleneck token. In reconstruction, this token guides prediction of future scenes alongside sparse patch hints. This forces the model to capture scene transitions and dynamics essential for sequential tasks.

## Tested Tasks and Environments

- Video label propagation
- Robot manipulation in simulated environments
- Real-world physical robot deployment
- Evaluation across different model scales

## Key Results

The research demonstrates ToBo's "superiority over baselines" across diverse sequential tasks. The approach proved robust in both simulated and real-world robotic applications, validating that the learned temporal representations effectively transfer to practical manipulation scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b0f4058-3c34-484c-9c1a-287b3ac37a20",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "f4d18a3a-0210-42ac-818c-9a6e5afcb58a",
  "sourceToolAssistantUUID": "8b0f4058-3c34-484c-9c1a-287b3ac37a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-13T04:58:57.079Z_

Now let me fetch a few more highly relevant ones -- the "Rethink VLA" paper itself on arxiv, the ETA-VLA paper (efficient token adaptation via temporal fusion), and the DTP paper (distracting token pruning).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4d18a3a-0210-42ac-818c-9a6e5afcb58a",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayyctueAiyDFJnSEojPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e42abef3-bbf1-4980-b097-5d3935cb571c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tjwyoFtgt3Pdnh88n8s2R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 327,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 15511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 37 · 2026-05-13T04:58:59.080Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014sQaC8UNZJrCTCgv1Gmjb3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.25766",
  "prompt": "Extract the full title, authors, date, abstract, and key method details for ETA-VLA. How does it handle temporal fusion and token sparsification inside the LLM? What are the key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e42abef3-bbf1-4980-b097-5d3935cb571c",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayyctueAiyDFJnSEojPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd0e1339-12bc-4a50-a79a-9032e3b65248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tjwyoFtgt3Pdnh88n8s2R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 327,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 15511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 38 · 2026-05-13T04:59:00.583Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KNuhsfPeXmEhh1n4df8LSS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.16065",
  "prompt": "Extract the full title, authors, date, abstract, and key method details for DTP (Distracting Token Pruning). How does it identify distracting tokens? How does removal of distracting tokens improve VLA generalization? What are the key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd0e1339-12bc-4a50-a79a-9032e3b65248",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayyctueAiyDFJnSEojPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e7b035b-fa2b-4256-b302-5414b2009bf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tjwyoFtgt3Pdnh88n8s2R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 327,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 15511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 39 · 2026-05-13T04:59:02.195Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G81cyXEkuFYs2PNV89AJxX`</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.16959",
  "prompt": "Extract the full title, authors, date, abstract, and key method details for RoCoDA (Counterfactual Data Augmentation for robot learning). How does it use causal invariance and equivariance? How does it improve generalization and sample efficiency? What are the key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e7b035b-fa2b-4256-b302-5414b2009bf2",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayyctueAiyDFJnSEojPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9050bfd-dd63-4e61-90fb-eb53f67e5bd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tjwyoFtgt3Pdnh88n8s2R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 327,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 15511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 40 · 2026-05-13T04:59:05.043Z_

<details><summary>↩ Tool result · `toolu_014sQaC8UNZJrCTCgv1Gmjb3`</summary>

```text
# ETA-VLA: Efficient Token Adaptation Summary

**Full Title:**
"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models"

**Authors:**
Yiru Wang, Anqing Jiang, Shuo Wang, Yuwen Heng, Zichong Gu, Hao Sun

**Submission Date:**
March 26, 2026

## Abstract Overview
The work addresses computational bottlenecks in Vision-Language-Action models used for autonomous driving. The system processes multi-view frames while managing the quadratic complexity burden of self-attention in large language models.

## Key Methodology

**Temporal Fusion & Token Sparsification:**
The core innovation is an "Intra-LLM Sparse Aggregator (ILSA)" that dynamically identifies and removes redundant visual tokens. The approach draws inspiration from human driver attention by using two mechanisms:
1. Text-guided scoring to rank token importance
2. Diversity-preserving strategies to maintain scene awareness

The system selects "a sparse subset of critical tokens" while eliminating redundancy guided by textual context and temporal patterns.

## Key Results

- **FLOPs Reduction:** Approximately 32% computational savings versus baselines
- **Token Pruning:** Removes 85% of visual tokens
- **Inference Speed:** 61% reduction in inference FLOPs
- **Accuracy Retention:** Maintains 94% of original performance on NAVSIM v2 benchmark
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd0e1339-12bc-4a50-a79a-9032e3b65248",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "ffc3da19-948c-4623-be36-e8069345ca06",
  "sourceToolAssistantUUID": "dd0e1339-12bc-4a50-a79a-9032e3b65248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-13T04:59:06.049Z_

<details><summary>↩ Tool result · `toolu_01KNuhsfPeXmEhh1n4df8LSS`</summary>

```text
# DTP: Distracting Token Pruning Framework

**Full Title:** "DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models"

**Authors:** Chenyang Li, Jieyuan Liu, Bin Li, Bo Gao, Yilin Yuan, Yangfan He, Yuchen Li, Jingqun Tang

**Submission Date:** January 22, 2026

## Abstract Summary
The researchers address a challenge in Vision-Language Action models where excessive attention to irrelevant image regions interferes with generating correct robotic actions. Their framework dynamically removes these problematic tokens to refocus the model's visual processing.

## Method for Identifying Distracting Tokens
The paper describes the core issue as: "VLA models may overly attend to image tokens in the task-irrelevant region, which we describe as 'distracting tokens'." The framework operates as a plug-and-play mechanism that "dynamically detects and prunes these distracting image tokens" without modifying the original architecture.

## Impact on Generalization
By correcting attention patterns, the approach aims to improve performance while "exploring the performance upper boundaries of the model without altering its original architecture." The work demonstrates that this correction enhances applicability across different VLA model types.

## Key Results
- Consistent relative improvements across diverse VLA models tested on SIMPLER Benchmark
- Demonstrated generalizability to transformer-based architectures
- Analysis revealed inverse correlation: "a negative correlation between the task success rate and the amount of attentions in the task-irrelevant region"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e7b035b-fa2b-4256-b302-5414b2009bf2",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "bb13441e-30ad-4f8c-acb6-845a84c3a7e1",
  "sourceToolAssistantUUID": "0e7b035b-fa2b-4256-b302-5414b2009bf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T04:59:10.370Z_

<details><summary>↩ Tool result · `toolu_01G81cyXEkuFYs2PNV89AJxX`</summary>

```text
# RoCoDA: Counterfactual Data Augmentation for Robot Learning

**Full Title:** RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations

**Authors:** Ezra Ameperosa, Jeremy A. Collins, Mrinal Jain, Animesh Garg

**Submission Date:** November 25, 2024 (v1); May 20, 2025 (v2)

**Acceptance:** 2025 IEEE International Conference on Robotics and Automation (ICRA)

## Key Method Details

RoCoDA integrates three core concepts:

1. **Causal Invariance:** The method modifies "task-irrelevant subsets of the environment state" without affecting policy outputs, preserving task-critical information.

2. **SE(3) Equivariance:** The system applies rigid body transformations to object positions and correspondingly adjusts actions to generate synthetic training data while maintaining geometric consistency.

3. **Unified Framework:** These principles combine to create principled data augmentation that bridges geometric symmetries with causal reasoning.

## Key Results

- Improved performance across five robotic manipulation tasks
- Enhanced generalization to unseen object poses, textures, and distractors
- Better sample efficiency compared to existing data augmentation methods
- Emergent behaviors including re-grasping, suggesting deeper task understanding by trained policies

The approach addresses the critical challenge of "generalization due to the complexity of robotic environments and the high cost of data collection" in imitation learning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9050bfd-dd63-4e61-90fb-eb53f67e5bd3",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "dbba0e90-75f5-4443-a09f-8819e8000b40",
  "sourceToolAssistantUUID": "f9050bfd-dd63-4e61-90fb-eb53f67e5bd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-13T04:59:15.022Z_

Let me also grab the "Rethink VLA" paper and the OpenVLA-OFT paper for completeness on the regularization/finetuning angle.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbba0e90-75f5-4443-a09f-8819e8000b40",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayyeDvATcCuwnnjpUJhE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4132590-68a4-4fce-8862-84025b8b91b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HGk2XvMc6bLX9CCm6Ls9ME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2022,
      "cache_read_input_tokens": 20950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2022,
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

_source line 44 · 2026-05-13T04:59:17.432Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y7L1CfGZZhAKgiFpyoMBLt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.19645",
  "prompt": "Extract the full title, authors, date, abstract, and key method details for OpenVLA-OFT (Fine-Tuning VLA models). What finetuning techniques do they use? What regularization is applied? How does it improve generalization and speed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4132590-68a4-4fce-8862-84025b8b91b3",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayyeDvATcCuwnnjpUJhE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebcbecde-1ae3-4989-91d7-33ba56144235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HGk2XvMc6bLX9CCm6Ls9ME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2022,
      "cache_read_input_tokens": 20950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2022,
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

_source line 45 · 2026-05-13T04:59:18.467Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HXyFgzKQBzoVCGCktUyWcL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.11746",
  "prompt": "Extract title, authors, date, abstract, and method details. How does token masking regularization work for transformers? What masking probability is optimal? What improvements are seen?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebcbecde-1ae3-4989-91d7-33ba56144235",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayyeDvATcCuwnnjpUJhE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3180edca-14cd-4990-8ded-7ad02b97407a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HGk2XvMc6bLX9CCm6Ls9ME",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2022,
      "cache_read_input_tokens": 20950,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2022
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 20950,
          "cache_creation_input_tokens": 2022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2022,
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

_source line 46 · 2026-05-13T04:59:22.943Z_

<details><summary>↩ Tool result · `toolu_01Y7L1CfGZZhAKgiFpyoMBLt`</summary>

```text
# OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models

## Title & Authors
**"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"**
- Moo Jin Kim, Chelsea Finn, Percy Liang

## Date
Submitted February 27, 2025; revised April 28, 2025

## Abstract Summary
The research addresses how to effectively fine-tune vision-language-action models (VLAs) for novel robot setups. The team developed an optimized recipe that achieves state-of-the-art performance on simulation benchmarks and real robotic systems.

## Fine-Tuning Techniques
The OFT (Optimized Fine-Tuning) recipe integrates four key components:

1. **Parallel decoding** - enables more efficient action generation
2. **Action chunking** - groups sequential actions for improved learning
3. **Continuous action representation** - uses continuous rather than discrete outputs
4. **L1 regression objective** - a "simple L1 regression-based learning objective"

## Performance Improvements

**Simulation Results (LIBERO benchmark):**
- Success rate improved from 76.5% to 97.1%
- Action generation throughput increased by 26×

**Real-world Robot Results:**
- Successfully executes complex bimanual dexterous control tasks
- Outperforms competing VLAs (π₀, RDT-1B) by up to 15% in success rate
- Exceeds imitation learning baselines (Diffusion Policy, ACT)

The approach balances inference efficiency, policy performance, and flexible input-output specifications without requiring additional regularization techniques beyond the core L1 loss function.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebcbecde-1ae3-4989-91d7-33ba56144235",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "ac5adbd9-bd2b-431e-976e-0f266afff6db",
  "sourceToolAssistantUUID": "ebcbecde-1ae3-4989-91d7-33ba56144235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-13T04:59:23.219Z_

<details><summary>↩ Tool result · `toolu_01HXyFgzKQBzoVCGCktUyWcL`</summary>

```text
# Token Masking Improves Transformer-Based Text Classification

**Title:** Token Masking Improves Transformer-Based Text Classification

**Authors:** Xianglong Xu, John Bowen, Rojin Taheri

**Date:** Submitted May 16, 2025

**arXiv ID:** 2505.11746

## Abstract Summary

The researchers propose token masking regularization for enhanced text classification. The method "randomly replaces input tokens with a special [MASK] token at probability p," introducing stochastic perturbations during training.

## How Token Masking Works

The technique operates through two mechanisms:

1. **Input perturbation** reduces overfitting by adding noise to training data
2. **Gradient-level smoothing** functions as implicit ensembling, encouraging the model to learn deeper inter-token relationships

This approach leverages implicit gradient averaging to strengthen dependency capture between tokens.

## Optimal Masking Probability

The research identifies "p = 0.1 as a strong general default," though task-specific rates may vary depending on the application.

## Performance Improvements

Testing across diverse models (mBERT, Qwen2.5-0.5B, TinyLlama-1.1B) on language identification and sentiment analysis tasks demonstrated "consistent improvements over standard regularization techniques."

The work demonstrates that simple masking-based regularization can meaningfully enhance transformer performance on text classification tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3180edca-14cd-4990-8ded-7ad02b97407a",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a58843e9da9a4c725",
  "type": "user",
  "uuid": "22cf0c6b-23d5-48f4-8691-06c4880fbf23",
  "sourceToolAssistantUUID": "3180edca-14cd-4990-8ded-7ad02b97407a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-13T05:00:22.860Z_

I now have comprehensive coverage. Here is the consolidated report.

---

## Landscape Report: Papers Competing With / Overlapping "Adaptive Token Masking for VLA Finetuning"

I searched 8 queries and deeply reviewed 10+ papers. Below are the most relevant, organized by how directly they threaten or overlap with the idea.

---

### TIER 1 -- Direct Competitors (token-level operations on VLA visual tokens)

**1. DTP: Distracting Token Pruning for VLA Models**
- Authors: Chenyang Li et al.
- Date: January 2026
- Approach: Plug-and-play framework that dynamically detects and prunes "distracting" visual tokens -- tokens in task-irrelevant regions that VLA models over-attend to. Shows a negative correlation between success rate and attention to irrelevant regions.
- Overlap: Very high. This is essentially the same intuition as adaptive token masking (suppress irrelevant visual tokens to improve action prediction), but frames it as inference-time pruning rather than training-time regularization. A reviewer could cite this as closely related.
- [arXiv 2601.16065](https://arxiv.org/abs/2601.16065)

**2. VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning**
- Authors: Ziyan Liu et al.
- Date: November 2025 (revised February 2026)
- Approach: Dual-level importance criterion -- (a) vision-language prefill attention for semantic relevance, (b) action-decode attention estimated via temporal smoothing for action-level importance. Plug-and-play, works across multiple VLA architectures.
- Overlap: High. Uses adaptive, importance-based token selection (not random masking), but the core mechanism of reducing visual tokens to improve VLA efficiency/performance is shared. The temporal smoothing angle is distinct.
- [arXiv 2511.16449](https://arxiv.org/abs/2511.16449)

**3. VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment**
- Authors: (March 2026)
- Approach: Shifts from "Perception-First" to "Interaction-First" paradigm. Develops an Interaction-Aligned Dynamic Strategy that adjusts pruning intensity based on semantic-motion alignment. At 70% token retention, actually surpasses unpruned baselines.
- Overlap: High. Demonstrates that adaptive (not uniform) token reduction helps VLA generalization, which validates the core premise of adaptive token masking.
- [arXiv 2603.22991](https://arxiv.org/abs/2603.22991)

**4. LightVLA (Differentiable Token Pruning)**
- Authors: (September 2025)
- Approach: Generates dynamic queries to evaluate visual token importance; uses Gumbel-softmax for differentiable, learnable token selection during training.
- Overlap: Very high -- this is learned adaptive token selection during training, which is essentially adaptive token masking with a differentiable selection mechanism rather than stochastic masking. A key paper to differentiate from.
- [arXiv 2509.12594](https://arxiv.org/abs/2509.12594)

**5. ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification**
- Authors: Yiru Wang et al.
- Date: March 2026
- Approach: Intra-LLM Sparse Aggregator (ILSA) that uses text-guided scoring + diversity-preserving strategies to remove 85% of visual tokens inside the LLM layers. Applied to autonomous driving VLAs.
- Overlap: Moderate-high. Text-guided adaptive token removal inside the LLM backbone is closely related to adaptive masking, though the application domain (driving vs. manipulation) differs.
- [arXiv 2603.25766](https://arxiv.org/abs/2603.25766)

---

### TIER 2 -- Closely Related (VLA finetuning regularization, not token-focused)

**6. Boosting VLA Finetuning with Feasible Action Neighborhood (FAN) Prior** -- CVPR 2026
- Authors: Haochen Niu et al.
- Date: April 2026
- Approach: Gaussian prior regularizer that exploits the fact that nearby actions are often equally feasible in manipulation. Shapes the output distribution to be locally smooth/unimodal. Improves both in-distribution and OOD generalization, plus sample efficiency.
- Overlap: Moderate. Different mechanism (action-space regularization vs. input token masking), but solves the same problem: improving VLA finetuning generalization. A reviewer would expect this to be cited.
- [arXiv 2604.01570](https://arxiv.org/abs/2604.01570)

**7. Robust Finetuning of VLA Policies via Parameter Merging** -- ICLR 2026
- Authors: Yajat Yadav, Karl Pertsch, Sergey Levine et al.
- Date: December 2025
- Approach: Interpolates weights between pretrained and finetuned VLA models. The merged model outperforms both on OOD task variations. Simple, no architectural changes.
- Overlap: Moderate. Addresses the same finetuning-generalization tradeoff but through weight-space regularization rather than input-space token masking.
- [arXiv 2512.08333](https://arxiv.org/abs/2512.08333)

**8. Gaze-Regularized VLA Models for Robotic Manipulation**
- Authors: Anupam Pani, Yanchao Yang
- Date: March 2026
- Approach: KL-divergence regularization that aligns transformer attention with human gaze heatmaps during training. 4-12% improvement on manipulation benchmarks. No inference overhead.
- Overlap: Moderate. Both methods regularize visual attention during training, but the mechanism is different (human gaze supervision vs. stochastic token masking).
- [arXiv 2603.23202](https://arxiv.org/abs/2603.23202)

**9. Rethink VLA (BeingBeyond Research)**
- Approach: Empirical study testing sensory dropout / stochastic modality masking at scale. Key finding: "complex regularization strategies do not reliably translate into gains at scale" and "stochastic modality dropout does not consistently improve performance."
- Overlap: Directly relevant as a potential negative result for the adaptive token masking idea. This paper argues that naive dropout-style regularization may not help at scale, which adaptive (non-random) masking would need to overcome.
- [BeingBeyond](https://research.beingbeyond.com/rethink_vla)

---

### TIER 3 -- Tangentially Related (alternative generalization approaches)

**10. Token Bottleneck (ToBo)** -- NeurIPS 2025
- Compresses a scene into a single bottleneck token for self-supervised pretraining. Strong results on robot manipulation/locomotion. Information bottleneck angle is conceptually related but operates at pretraining, not finetuning.
- [arXiv 2507.06543](https://arxiv.org/abs/2507.06543)

**11. RoCoDA: Counterfactual Data Augmentation** -- ICRA 2025
- Uses causal invariance + SE(3) equivariance for data augmentation in imitation learning. Improves generalization to unseen poses/textures/distractors. Orthogonal approach (data augmentation vs. token masking) but solves the same generalization challenge.
- [arXiv 2411.16959](https://arxiv.org/abs/2411.16959)

**12. Token Masking Improves Transformer-Based Text Classification** (May 2025)
- Random [MASK] token replacement at p=0.1 as regularization for text transformers. Provides theoretical grounding (implicit gradient averaging) that could support the adaptive token masking idea in VLAs.
- [arXiv 2505.11746](https://arxiv.org/abs/2505.11746)

**13. OpenVLA-OFT** (February 2025)
- Optimized finetuning recipe for VLAs (parallel decoding, action chunking, L1 loss). No token masking, but establishes a strong finetuning baseline that any new method must beat.
- [arXiv 2502.19645](https://arxiv.org/abs/2502.19645)

---

### Key Takeaways for Positioning "Adaptive Token Masking for VLA Finetuning"

1. **The field is crowded with token pruning/selection for VLAs** (DTP, VLA-Pruner, VLA-IAP, LightVLA, ETA-VLA, Compressor-VLA, SpecPrune-VLA, BFA++, SP-VLA). Most frame it as an efficiency technique. Your differentiation should emphasize **regularization for generalization during finetuning** rather than inference speedup.

2. **LightVLA is the closest competitor** -- it does learnable, adaptive token selection during training. You must clearly differentiate from it.

3. **The "Rethink VLA" negative result** is a risk: they found stochastic modality dropout doesn't help at scale. You need to argue that *adaptive* (not random) masking overcomes this limitation.

4. **FAN regularization (CVPR 2026) and parameter merging (ICLR 2026)** solve the same finetuning-generalization problem through different mechanisms. These are natural baselines/comparisons rather than direct competitors.

5. **The token masking as regularization angle** (from the NLP side, arXiv 2505.11746) provides theoretical support -- the implicit gradient averaging argument could be extended to vision tokens in VLAs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22cf0c6b-23d5-48f4-8691-06c4880fbf23",
  "isSidechain": true,
  "agentId": "a58843e9da9a4c725",
  "requestId": "req_011CayyfAnRijNwUxppQRfN7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bceece99-9fc1-4b0d-b050-17580127013f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Thq43RhGFw3WTQj5VGwkYw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 22972,
      "output_tokens": 2419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1057
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2419,
          "cache_read_input_tokens": 22972,
          "cache_creation_input_tokens": 1057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1057,
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
