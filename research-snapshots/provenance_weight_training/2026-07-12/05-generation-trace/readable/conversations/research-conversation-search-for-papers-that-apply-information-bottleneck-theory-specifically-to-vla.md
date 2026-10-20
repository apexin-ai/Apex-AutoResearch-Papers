# Research conversation: Search for papers that apply Information Bottleneck theory specifically to VLA (Vision-Language-Action) models or roboti

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a4e15c3fb5c71de91.jsonl`
- **Structured JSON:** [`fb5e6d9863ac4d4c7f73.json`](../../sessions/fb/fb5e6d9863ac4d4c7f73.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-13T04:58:36.596Z_

Search for papers that apply Information Bottleneck theory specifically to VLA (Vision-Language-Action) models or robotic visual learning. I need to assess whether the theoretical framing claimed in this idea — "token masking after the projector creates an implicit variational information bottleneck" — is truly novel.

Search queries:
1. "information bottleneck VLA vision language action"
2. "variational information bottleneck robot learning visual"
3. "CRAFT VLA force-aware curriculum finetuning information bottleneck arXiv 2602.12532"
4. "Gaze-Regularized VLA robotic manipulation arXiv 2603.23202"
5. "token masking information bottleneck frozen encoder"
6. "visual representation regularization information bottleneck robotics 2025 2026"

Also search for any work on "adaptive masking" or "learned token masking" in vision transformers more broadly:
7. "learned token masking vision transformer adaptive 2024 2025"
8. "differentiable token selection vision language model"

For any relevant papers, note the title, approach, and how close it is to "adaptive learned per-token masking with IB regularization." Use WebFetch on the most relevant 1-2 papers. Report concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "4df885fd-f2de-4254-a686-b7d1258471fe",
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

_source line 2 · 2026-05-13T04:58:36.600Z_

```json
{
  "parentUuid": "4df885fd-f2de-4254-a686-b7d1258471fe",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
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
  "uuid": "d6330ee5-e50e-40ad-bfee-0f2ce76b0bc3",
  "timestamp": "2026-05-13T04:58:36.600Z",
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

_source line 3 · 2026-05-13T04:58:40.344Z_



I'll conduct a systematic search across these queries to assess the novelty of the claimed theoretical framing. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6330ee5-e50e-40ad-bfee-0f2ce76b0bc3",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayybjSqtLFGXH8tTHFo9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "967412d0-c291-4485-a59d-137f41bf0c7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWgBkahH6PL5eJDQjZyzh1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 822,
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

_source line 4 · 2026-05-13T04:58:40.515Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016VY2pQmnmKw86N1sEf1T1a`</summary>

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
  "parentUuid": "967412d0-c291-4485-a59d-137f41bf0c7c",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayybjSqtLFGXH8tTHFo9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd139d37-a4cd-47b7-8456-3eb7b8fd7685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWgBkahH6PL5eJDQjZyzh1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 7304,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 822
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 116,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 822,
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

_source line 5 · 2026-05-13T04:58:40.517Z_

<details><summary>↩ Tool result · `toolu_016VY2pQmnmKw86N1sEf1T1a`</summary>

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
  "parentUuid": "dd139d37-a4cd-47b7-8456-3eb7b8fd7685",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "1af9a77b-b9b5-4949-8b6f-11befdce6ff3",
  "sourceToolAssistantUUID": "dd139d37-a4cd-47b7-8456-3eb7b8fd7685",
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

_source line 6 · 2026-05-13T04:58:43.767Z_



Now let me run all the search queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1af9a77b-b9b5-4949-8b6f-11befdce6ff3",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyc2UXwFXM8PfvMDFV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05c16bbc-f5e8-46ba-829f-7e9468588ca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyrHaLd4utV3tX1fVp9B8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1925,
      "cache_read_input_tokens": 8126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1925,
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

_source line 7 · 2026-05-13T04:58:44.696Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PV1yNoVWmbZKDy8ZgQU2d2`</summary>

```json
{
  "query": "information bottleneck VLA vision language action model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05c16bbc-f5e8-46ba-829f-7e9468588ca8",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyc2UXwFXM8PfvMDFV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a36f415b-7566-47be-80ae-d03933d6d7fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyrHaLd4utV3tX1fVp9B8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1925,
      "cache_read_input_tokens": 8126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1925,
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

_source line 8 · 2026-05-13T04:58:45.175Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FHRn4RYr6jCrV8PL2T7Lo1`</summary>

```json
{
  "query": "variational information bottleneck robot learning visual representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a36f415b-7566-47be-80ae-d03933d6d7fe",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyc2UXwFXM8PfvMDFV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df60e049-041f-4a8f-9037-41f3a298981c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyrHaLd4utV3tX1fVp9B8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1925,
      "cache_read_input_tokens": 8126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1925,
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

_source line 9 · 2026-05-13T04:58:46.108Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AtSMxK6fEV1bivTCg5UFAb`</summary>

```json
{
  "query": "CRAFT VLA force-aware curriculum finetuning information bottleneck arXiv 2602.12532"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df60e049-041f-4a8f-9037-41f3a298981c",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyc2UXwFXM8PfvMDFV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9d30827-232c-4110-81b8-4db725ee97af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyrHaLd4utV3tX1fVp9B8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1925,
      "cache_read_input_tokens": 8126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1925,
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

_source line 10 · 2026-05-13T04:58:47.050Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hq8zeLcmiYqwJpuuaYhXTE`</summary>

```json
{
  "query": "Gaze-Regularized VLA robotic manipulation arXiv 2603.23202"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9d30827-232c-4110-81b8-4db725ee97af",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyc2UXwFXM8PfvMDFV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8ed5a91-addf-4162-ac51-35e3d8c12226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyrHaLd4utV3tX1fVp9B8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1925,
      "cache_read_input_tokens": 8126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1925,
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

_source line 11 · 2026-05-13T04:58:47.563Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VUHa97Kqs85rGJLff5XgEr`</summary>

```json
{
  "query": "token masking information bottleneck frozen encoder vision language"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8ed5a91-addf-4162-ac51-35e3d8c12226",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyc2UXwFXM8PfvMDFV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05fb115e-ed43-41d7-91b9-3972e4ac5374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyrHaLd4utV3tX1fVp9B8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1925,
      "cache_read_input_tokens": 8126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1925,
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

_source line 12 · 2026-05-13T04:58:48.505Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DfJqesWb4AgB4XSa8cKukB`</summary>

```json
{
  "query": "visual representation regularization information bottleneck robotics 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05fb115e-ed43-41d7-91b9-3972e4ac5374",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyc2UXwFXM8PfvMDFV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1f37ebb-db10-4354-8ef6-b87cfbf515d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyrHaLd4utV3tX1fVp9B8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1925,
      "cache_read_input_tokens": 8126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1925,
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

_source line 13 · 2026-05-13T04:58:48.936Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HuHgA1kZzYNh1nwq2Jh3su`</summary>

```json
{
  "query": "learned token masking vision transformer adaptive 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1f37ebb-db10-4354-8ef6-b87cfbf515d6",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyc2UXwFXM8PfvMDFV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e07283d-bfb0-4f19-9d0a-ce8d6c445cbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyrHaLd4utV3tX1fVp9B8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1925,
      "cache_read_input_tokens": 8126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1925,
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

_source line 14 · 2026-05-13T04:58:49.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014zm4FKkuKc3Q37wLyvpgZ8`</summary>

```json
{
  "query": "differentiable token selection vision language model 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e07283d-bfb0-4f19-9d0a-ce8d6c445cbb",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyc2UXwFXM8PfvMDFV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa9069b0-6906-4fb5-b68f-6c0e4014799a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyrHaLd4utV3tX1fVp9B8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1925,
      "cache_read_input_tokens": 8126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1925,
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

_source line 15 · 2026-05-13T04:58:52.628Z_

<details><summary>↩ Tool result · `toolu_01AtSMxK6fEV1bivTCg5UFAb`</summary>

```text
Web search results for query: "CRAFT VLA force-aware curriculum finetuning information bottleneck arXiv 2602.12532"

Links: [{"title":"[2602.12532] CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning","url":"https://arxiv.org/abs/2602.12532"},{"title":"CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning","url":"https://arxiv.org/html/2602.12532"},{"title":"World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy","url":"https://arxiv.org/html/2602.06508v1"},{"title":"UaOR: Uncertainty-aware Observation Reinjection for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.18020"},{"title":"Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning","url":"https://arxiv.org/html/2602.08167v1"},{"title":"GitHub - cccedric/conrft: This is the official implementation of the paper \"ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy\".","url":"https://github.com/cccedric/conrft"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation","url":"https://arxiv.org/html/2505.22159v1"},{"title":"ConRFT: A Reinforced Fine-tuning Method for VLA Models via...","url":"https://arxiv.org/abs/2502.05450"},{"title":"ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy","url":"https://arxiv.org/html/2502.05450v1"}]

Based on the search results, here's information about the CRAFT paper (arXiv 2602.12532):

## CRAFT: Adapting VLA Models to Contact-rich Manipulation

CRAFT is a lightweight and model-agnostic framework for adapting pretrained VLA models to contact-rich manipulation.

### Key Technical Approach

CRAFT is a force-aware curriculum fine-tuning framework that integrates a variational information bottleneck module to regulate vision and language embeddings during early training.

More specifically, the VIB initially imposes a strong Kullback–Leibler (KL) penalty that suppresses high-entropy visual and language signals, compelling the policy to focus on low-entropy force inputs and thereby acquire stable, contact-aware behaviors. As training progresses, the weight of the VIB regularization is gradually annealed, releasing the bottleneck and allowing the model to reincorporate rich perceptual information while retaining the previously learned force-sensitive representations.

### Core Problem Being Addressed

CRAFT mitigates the imbalance between high-entropy perceptual signals (vision and language) and low-entropy force signals in contact-rich manipulation.

### Results

Extensive real-world experiments demonstrate that the proposed CRAFT enhances task success, improves generalization to unseen objects and novel tasks, and is broadly applicable across different VLA-based approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9d30827-232c-4110-81b8-4db725ee97af",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "989ae69b-5564-4055-8e25-9d0de6eb62b3",
  "sourceToolAssistantUUID": "f9d30827-232c-4110-81b8-4db725ee97af",
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

_source line 16 · 2026-05-13T04:58:53.426Z_

<details><summary>↩ Tool result · `toolu_01FHRn4RYr6jCrV8PL2T7Lo1`</summary>

```text
Web search results for query: "variational information bottleneck robot learning visual representation"

Links: [{"title":"Boosting Action-Information via a Variational Bottleneck on Unlabelled Robot Videos","url":"https://arxiv.org/html/2508.08743v1"},{"title":"Representation Learning in Deep RL via Discrete Information Bottleneck","url":"https://proceedings.mlr.press/v206/islam23a/islam23a.pdf"},{"title":"Revisiting the Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=w10KdRwcMk"},{"title":"Information Filtering via Variational Regularization for Robot Manipulation","url":"https://arxiv.org/html/2601.21926v1"},{"title":"[1612.00410] Deep Variational Information Bottleneck","url":"https://arxiv.org/abs/1612.00410"},{"title":"Multimodal information bottleneck for deep reinforcement learning with multiple sensors - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608024002715"},{"title":"Variational Geometric Information Bottleneck: Learning the Shape of Understanding","url":"https://arxiv.org/html/2511.02496"},{"title":"Contrastive Learning via Variational Information Bottleneck - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40392641/"},{"title":"[2212.13835] Representation Learning in Deep RL via Discrete Information Bottleneck","url":"https://arxiv.org/abs/2212.13835"},{"title":"Flexible variational information bottleneck: Achieving diverse compression with a single training - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231225008707"}]

Based on the web search results, here's what I found about variational information bottleneck approaches in robot learning and visual representation:

## Key Applications in Robot Learning

The variational information-bottleneck is used to extract action-relevant representations while discarding task-irrelevant information in robot learning contexts. 

### Action Learning from Video

Recent work presents a framework that increases the mutual information between latent actions inferred from unlabeled videos and the corresponding ground-truth actions, thereby improving robot policy performance. Specifically, a principled Variational Information Bottleneck formulation is tailored to latent–action extraction, where a novel framework explicitly maximizes the mutual information between latent actions and true actions, even in the absence of action labels.

### Visual Representation for Robot Manipulation

Variational Regularization imposes a timestep-conditioned Gaussian over backbone features and applies a KL-divergence regularizer, forming an adaptive information bottleneck. Intermediate backbone features in large decoders can be redundant and noisy for manipulation tasks, and Variational Regularization proposes a lightweight module that imposes a timestep-conditioned variational bottleneck on backbone features and regularizes it with a KL term for adaptive information filtering.

### Multimodal Sensor Integration

A model compresses and retains the predictive information in multimodal observations for learning a compressed joint representation, which fuses complementary information from visual and proprioceptive feedback and meanwhile filters out task-irrelevant information in raw multimodal observations.

### Representation Learning in RL

Information bottlenecks can be used to construct latent states efficiently in the presence of task-irrelevant information, with architectures that utilize variational and discrete information bottlenecks to learn structured factorized representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df60e049-041f-4a8f-9037-41f3a298981c",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "7379bfea-3deb-463c-8723-2a0a1e4308c7",
  "sourceToolAssistantUUID": "df60e049-041f-4a8f-9037-41f3a298981c",
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

_source line 17 · 2026-05-13T04:58:53.564Z_

<details><summary>↩ Tool result · `toolu_01Hq8zeLcmiYqwJpuuaYhXTE`</summary>

```text
Web search results for query: "Gaze-Regularized VLA robotic manipulation arXiv 2603.23202"

Links: [{"title":"[2603.23202] Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/abs/2603.23202"},{"title":"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2603.23202v1"},{"title":"[2603.23202v1] Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/abs/2603.23202v1"},{"title":"Gaze-Regularized Vision-Language-Action Models for Robot...","url":"https://bytez.com/docs/arxiv/2603.23202/paper"},{"title":"GitHub - BaiShuanghao/my_arXiv_daily · GitHub","url":"https://github.com/BaiShuanghao/my_arXiv_daily"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"[2603.15620] Towards Generalizable Robotic Manipulation in Dynamic Environments","url":"https://arxiv.org/abs/2603.15620"},{"title":"Tiny-VLA:Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation","url":"https://tiny-vla.github.io/"},{"title":"[2603.23190v1] Gaze-Regularized VLMs for Ego-Centric Behavior Understanding","url":"https://arxiv.org/abs/2603.23190v1"}]

Here are the search results for the arXiv paper 2603.23202:

## Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation

The paper addresses how current Vision-Language-Action (VLA) models struggle with fine-grained robotic manipulation tasks due to lacking mechanisms for active visual attention allocation.

### Key Innovation

The researchers introduce a gaze-regularized training framework that aligns VLA models' internal attention with human visual patterns without architectural modifications or inference-time overhead. Their method transforms temporally aggregated gaze heatmaps into patch-level distributions and regularizes the transformer's attention through KL divergence.

### Results and Benefits

When integrated into existing VLA architectures, the approach yields 4-12% improvements across manipulation benchmarks. Additionally, the gaze-regularized models reach equivalent performance with fewer training steps and maintain robustness under lighting variations and sensor noise.

The learned attention patterns produce interpretable visualizations that mirror human strategies, enhancing trust in robotic systems. The framework requires no eye-tracking equipment and applies directly to existing datasets.

### Authors and Publication

The paper was submitted on March 24, 2026 by Anupam Pani and Yanchao Yang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8ed5a91-addf-4162-ac51-35e3d8c12226",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "60a99395-7d26-4b89-b02f-e3e43b9a814e",
  "sourceToolAssistantUUID": "f8ed5a91-addf-4162-ac51-35e3d8c12226",
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

_source line 18 · 2026-05-13T04:58:53.785Z_

<details><summary>↩ Tool result · `toolu_01PV1yNoVWmbZKDy8ZgQU2d2`</summary>

```text
Web search results for query: "information bottleneck VLA vision language action model"

Links: [{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.28740"},{"title":"Vision-Language-Action Model","url":"https://www.emergentmind.com/topics/vision-language-action-vla-model"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models","url":"https://arxiv.org/html/2601.03309v1"},{"title":"VLA-ADAPTER: AN EFFECTIVE PARADIGM FOR TINY-SCALE VISION-LANGUAGE-ACTION MODEL","url":"https://arxiv.org/pdf/2509.09372"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"}]

Based on the search results, here are key findings related to information bottlenecks in Vision-Language-Action (VLA) models:

## Bottlenecks in VLA Models

A critical bottleneck in embodied AI exists without systems that could jointly perceive, understand, and act, which motivated the development of VLA models to unify these capabilities.

## Specific Information Bottlenecks

**Visual Information Processing:**
Current auto-regressive VLA policies are constrained by three bottlenecks: (1) architectural bias drives models to overlook visual details, (2) an excessive number of visual tokens makes attention difficult to focus on the correct regions, and (3) task-irrelevant visual information introduces substantial noise.

**Modality-Level Bottlenecks:**
The vision encoder, rather than the language component, is the primary performance bottleneck, and fine-tuning the vision encoder is essential for strong control performance.

**Inference and Computational Bottlenecks:**
VLA systems face inference bottlenecks, safety concerns, high computational demands, limited generalization, and ethical implications. Additionally, critical computational and memory-bound bottlenecks exist within contemporary Diffusion-based Vision-Language-Action architectures.

**Action Space Compression:**
Letting VLA directly predict high-dimensional visual states can distribute model capacity and incur prohibitive training cost, while compressing visual states into more compact supervisory signals inevitably incurs information bottlenecks.

These various bottlenecks represent key challenges researchers are actively addressing in VLA model design and optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a36f415b-7566-47be-80ae-d03933d6d7fe",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "6878deb2-0a94-4164-a5b4-6d7d5335d8ba",
  "sourceToolAssistantUUID": "a36f415b-7566-47be-80ae-d03933d6d7fe",
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

_source line 19 · 2026-05-13T04:58:54.276Z_

<details><summary>↩ Tool result · `toolu_01VUHa97Kqs85rGJLff5XgEr`</summary>

```text
Web search results for query: "token masking information bottleneck frozen encoder vision language"

Links: [{"title":"Vision-centric Token Compression in Large Language Model","url":"https://arxiv.org/html/2502.00791v5"},{"title":"Vision-centric Token Compression in Large Language Model","url":"https://openreview.net/pdf?id=YdggdEL41C"},{"title":"When LLaVA Meets Objects: Token Composition for Vision-Language-Models","url":"https://arxiv.org/html/2602.04864v1"},{"title":"IVTP: Instruction-guided Visual Token Pruning for Large Vision-Language Models","url":"https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02577.pdf"},{"title":"Token Bottleneck: One Token to Remember Dynamics","url":"https://arxiv.org/html/2507.06543v1"},{"title":"Frozen Transformers in Language Models Are Effective Visual Encoder Layers","url":"https://arxiv.org/html/2310.12973"},{"title":"Optical Context Compression Is Just (Bad) Autoencoding","url":"https://arxiv.org/html/2512.03643v1"},{"title":"End-to-End Vision Tokenizer Tuning","url":"https://arxiv.org/html/2505.10562"},{"title":"Vision Remember: Recovering Visual Information in Efficient LVLM with","url":"https://arxiv.org/pdf/2506.03928"},{"title":"[2502.00791] Vision-centric Token Compression in Large Language Model","url":"https://arxiv.org/abs/2502.00791"}]

Based on the search results, here's what I found about the topics related to your query:

## Vision-Language Models with Token Masking and Frozen Encoders

The search results reveal several relevant research papers on these interconnected topics:

### Vision-Centric Token Compression (VIST)

VIST is a slow-fast compression framework that mirrors human reading: the fast path renders distant tokens into images, letting a frozen, lightweight vision encoder skim the low-salience context; the slow path feeds the proximal window into the LLM for fine-grained reasoning.

A Probability-informed Visual Enhancement (PVE) objective masks high-frequency tokens during training, steering the Resampler to concentrate on semantically rich regions—just as skilled readers gloss over function words. VIST employs Frequency-based Masking on text token embeddings from text tokenizer, suppressing high-frequency but low-information token (e.g., "the" and "with").

### Information Bottleneck in Token Compression

Information Bottleneck in Token Compression occurs because the compression of vision tokens inevitably discards fine-grained visual details (e.g., texture patterns, small objects), while the surviving tokens lack the representational capacity to reconstruct such high-frequency visual information.

### Frozen Vision Encoders in Vision-Language Models

In vision-language model training, only the vision encoder is kept frozen, and the multimodal projection layer and the LLM are trained in an end-to-end manner. Pre-trained LLM transformer blocks discern informative visual tokens and further amplify their effect, supporting what's called the information filtering hypothesis.

These approaches represent recent advances in making vision-language models more efficient while preserving semantic information through careful token handling and masking strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05fb115e-ed43-41d7-91b9-3972e4ac5374",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "80ff04ff-d156-4a6e-bcc2-b154eb11abcf",
  "sourceToolAssistantUUID": "05fb115e-ed43-41d7-91b9-3972e4ac5374",
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

_source line 20 · 2026-05-13T04:58:55.653Z_

<details><summary>↩ Tool result · `toolu_01DfJqesWb4AgB4XSa8cKukB`</summary>

```text
Web search results for query: "visual representation regularization information bottleneck robotics 2025 2026"

Links: [{"title":"The Supervised Information Bottleneck","url":"https://www.mdpi.com/1099-4300/27/5/452"},{"title":"The Role of the Information Bottleneck in Representation Learning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8437679/"},{"title":"Graph-based Unsupervised Disentangled Representation ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf"},{"title":"GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).","url":"https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"},{"title":"1 Physical AI: Bridging the Sim-to-Real Divide Toward Embodied,","url":"https://www.techrxiv.org/users/913189/articles/1355704/master/file/data/physical%20aiv7_compressed/physical%20aiv7_compressed.pdf?inline=true"},{"title":"VSLAM-survey.pdf","url":"https://www.yufangwen.com/wp-content/uploads/2025/12/VSLAM-survey.pdf"},{"title":"Optimization research on the autonomous learning algorithm in field of intelligent manufacturing engineering-Robots | Proceedings of the 2025 2nd International Conference on Modeling, Natural Language Processing and Machine Learning","url":"https://dl.acm.org/doi/10.1145/3757110.3757132"},{"title":"Publications | Machine Learning | NEC Labs","url":"https://www.nec-labs.com/research/machine-learning/publications/"},{"title":"2026: The Most Powerful Wave of Artificial Intelligence to Hit as Sector Differentiation Intensifies","url":"https://eu.36kr.com/en/p/3578453650479235"}]

I've completed a web search for your query on visual representation regularization, information bottleneck, and robotics in 2025-2026. Here are the key findings:

## Recent Research Developments

The Information Bottleneck (IB) framework offers a theoretically optimal approach to data modeling, and recent efforts have optimized supervised deep neural networks using a variational upper bound on the IB objective, leading to enhanced robustness to adversarial attacks.

Applying information bottleneck bounds as an objective for supervised DNNs induces empirical improvements and provides an information-theoretic motivation for decoder regularization.

## Robotics Applications and World Models

In the robotics field, there are significant developments in 2025-2026. IDC predicts that by 2026, there will be breakthroughs in AI models, vision systems, and edge computing.

World foundation models (WFMs) are trained on multimodal data—images, videos, motion trajectories, audio, and sensor feeds—to build a latent representation of how the world behaves.

## Visual Representation Learning

Information Bottleneck (IB) theory, constraining the information input to disentangled representation learning models (e.g., via penalty coefficient) inherently enables them to identify and learn the most representative factors for successful reconstruction.

The research landscape shows growing integration of information-theoretic principles with regularization techniques to improve both robustness and efficiency in robotic learning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1f37ebb-db10-4354-8ef6-b87cfbf515d6",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "28b64218-47fd-4fc8-8017-a079ac574105",
  "sourceToolAssistantUUID": "e1f37ebb-db10-4354-8ef6-b87cfbf515d6",
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

_source line 21 · 2026-05-13T04:58:56.376Z_

<details><summary>↩ Tool result · `toolu_01HuHgA1kZzYNh1nwq2Jh3su`</summary>

```text
Web search results for query: "learned token masking vision transformer adaptive 2024 2025"

Links: [{"title":"[2306.07346] Learning to Mask and Permute Visual Tokens for Vision Transformer Pre-Training","url":"https://arxiv.org/abs/2306.07346"},{"title":"PixelPrune: Pixel-Level Adaptive Visual Token Reduction via Predictive Coding","url":"https://arxiv.org/html/2604.00886"},{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425010711"},{"title":"Don’t Look Twice: Faster Video Transformers with Run-Length Tokenization","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/3181db351fd3ced43cd589b0b572675d-Paper-Conference.pdf"},{"title":"[2407.15219] Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/abs/2407.15219"},{"title":"Vision Token Reduction","url":"https://www.emergentmind.com/topics/vision-token-reduction"},{"title":"ATMformer: An Adaptive Token Merging Vision Transformer for Remote Sensing Image Scene Classification","url":"https://www.mdpi.com/2072-4292/17/4/660"},{"title":"Beyond Masking: Demystifying Token-Based Pre-Training for Vision Transformers","url":"https://arxiv.org/pdf/2203.14313"},{"title":"Learning to mask and permute visual tokens for Vision Transformer pre-training - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1077314225000177"},{"title":"Salience-Based Adaptive Masking: Revisiting Token Dynamics for Enhanced Pre-training | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-031-73229-4_20"}]

Based on the search results, here are the key findings about learned token masking in vision transformers with adaptive approaches from 2024-2025:

## Recent Research Developments

A notable approach is Masked and Permuted Vision Transformer (MaPeT), which employs autoregressive and permuted predictions to capture intra-patch dependencies.

Another significant development is the Learnable Token Merging (LTM) Transformer, which performs token merging in a learnable scheme and reduces the FLOPs and inference time while maintaining or improving prediction accuracy. The LTM-Transformer is motivated by reduction of Information Bottleneck, with a mask module designed to generate token merging masks.

## Adaptive Masking Strategies

A 2025 approach called Salience-Based Adaptive Masking revisits token dynamics for enhanced pre-training.

The Adaptive Token Merging Transformer (ATMformer) preserves essential local features by estimating the importance score of each token.

## Broader Context

Dynamic, query-conditioned, or reinforcement learning-based reduction represents a frontier for adaptive and non-myopic token reduction. Research in this area is exploring multiple approaches to token reduction, including specialized reductions like Video-XL-Pro, FrameFusion, and TokenSwift that collapse spatial/temporal redundancy while preserving event structure.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e07283d-bfb0-4f19-9d0a-ce8d6c445cbb",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "1c09b82a-e33a-40f3-a963-74ce261e72df",
  "sourceToolAssistantUUID": "8e07283d-bfb0-4f19-9d0a-ce8d6c445cbb",
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

_source line 22 · 2026-05-13T04:58:57.146Z_

<details><summary>↩ Tool result · `toolu_014zm4FKkuKc3Q37wLyvpgZ8`</summary>

```text
Web search results for query: "differentiable token selection vision language model 2025"

Links: [{"title":"ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_ATP-LLaVA_Adaptive_Token_Pruning_for_Large_Vision_Language_Models_CVPR_2025_paper.pdf"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"The Model Knows Which Tokens Matter: Automatic Token Selection via Noise Gating","url":"https://arxiv.org/html/2603.07135"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Differentiable Hierarchical Visual Tokenization | OpenReview","url":"https://openreview.net/forum?id=y8VWYf5cVI"},{"title":"Layer- and Timestep-Adaptive Differentiable Token Compression Ratios for","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/You_Layer-_and_Timestep-Adaptive_Differentiable_Token_Compression_Ratios_for_Efficient_Diffusion_CVPR_2025_paper.pdf"},{"title":"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/html/2507.01925v1"},{"title":"Dynamic Token Reduction during Generation for Vision Language Models","url":"https://arxiv.org/html/2501.14204v1"}]

Based on the search results, here's what I found about differentiable token selection in vision language models in 2025:

## Key Research Areas

**Differentiable Token Pruning Methods:**

LightVLA is a differentiable token pruning framework for vision-language-action (VLA) models, which adopts Gumbel softmax to enable differentiable token selection. Through fine-tuning, LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution, thereby improving efficiency and performance simultaneously.

Dynamic Rate (DyRate) is the first method to connect the token reduction rate with the attention weights to achieve adaptive dynamic reduction during the VLM generation process and is designed to be differentiable, enabling end-to-end training. DyRate employs Gumbel-Softmax to overcome the non-differentiability challenges associated with traditional pruning methods.

**Adaptive Token Pruning:**

ATP-LLaVA dynamically selects the adaptive pruning ratio for each layer of the LLM decoder based on the instance-specific characteristics. The differentiable pruning masks are used within the ATP module.

**Recent Advances:**

AutoSelect attaches a lightweight Scorer and Denoiser to a frozen VLM and trains with only the standard next token prediction loss, where a variance preserving noise gate modulates each token's information flow according to its predicted importance so that gradients propagate through all tokens.

These approaches represent significant progress in making token selection differentiable, allowing models to learn adaptive, performance-driven token compression strategies during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa9069b0-6906-4fb5-b68f-6c0e4014799a",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "b6f91d76-1d18-40db-b025-b6a687b4f44f",
  "sourceToolAssistantUUID": "fa9069b0-6906-4fb5-b68f-6c0e4014799a",
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

_source line 23 · 2026-05-13T04:59:02.855Z_

Excellent -- several highly relevant papers surfaced. Let me now fetch the two most critical ones: (1) CRAFT (arXiv 2602.12532), which explicitly uses a VIB module in a VLA context, and (2) the "Information Filtering via Variational Regularization for Robot Manipulation" paper (arXiv 2601.21926), plus the LightVLA differentiable token pruning paper. Let me also look more specifically at a few more.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6f91d76-1d18-40db-b025-b6a687b4f44f",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayydFNT89VH3ajiaEjV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30d6a4fa-4c54-45e9-b1c0-1222721d597a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011drCdiEL9mGgfyjzctDLVQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7597,
      "cache_read_input_tokens": 10051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7597,
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

_source line 24 · 2026-05-13T04:59:06.493Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M4x4fgZAuEFc8XE4pacUzZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.12532",
  "prompt": "Extract the full technical details of how the Variational Information Bottleneck (VIB) is used in this paper. Specifically: 1) What modalities does VIB regulate? 2) Where in the architecture is the VIB module placed? 3) How is the KL penalty scheduled? 4) Is per-token masking used or is it applied at the embedding level? 5) What is the exact mathematical formulation? 6) How is this different from simple dropout or random masking?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30d6a4fa-4c54-45e9-b1c0-1222721d597a",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayydFNT89VH3ajiaEjV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39042213-8e53-4ba0-8dcc-9ea57be00ef0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011drCdiEL9mGgfyjzctDLVQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7597,
      "cache_read_input_tokens": 10051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7597,
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

_source line 25 · 2026-05-13T04:59:08.604Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018Xz7e4Dj9tv1Z4UCbHMnZQ`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.21926v1",
  "prompt": "Extract the full technical details of this paper. What is the approach? How is the variational information bottleneck or variational regularization applied? Where in the architecture (encoder, projector, decoder)? Is it applied to visual tokens specifically? How does it relate to information bottleneck theory? What is the mathematical formulation? How is it different from token masking?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39042213-8e53-4ba0-8dcc-9ea57be00ef0",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayydFNT89VH3ajiaEjV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2730ef9-9ee6-4aeb-abeb-965000bfb179",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011drCdiEL9mGgfyjzctDLVQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7597,
      "cache_read_input_tokens": 10051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7597,
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

_source line 26 · 2026-05-13T04:59:10.944Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WpzEGYJ1TAij5M6bBDzQYg`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.12594v1",
  "prompt": "Extract the full technical details of LightVLA's differentiable token pruning approach. How does it select tokens? Does it use Gumbel-Softmax for per-token masking? Is there any information bottleneck regularization? Where in the VLA architecture is pruning applied (after vision encoder, after projector, etc.)? What is the mathematical formulation for token selection? How close is this to \"adaptive learned per-token masking with IB regularization\"?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2730ef9-9ee6-4aeb-abeb-965000bfb179",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayydFNT89VH3ajiaEjV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09eb5b54-3ce7-47a2-a468-babd0e6763aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011drCdiEL9mGgfyjzctDLVQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7597,
      "cache_read_input_tokens": 10051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7597,
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

_source line 27 · 2026-05-13T04:59:11.051Z_

<details><summary>↩ Tool result · `toolu_01M4x4fgZAuEFc8XE4pacUzZ`</summary>

```text
I cannot provide the specific technical details you've requested based on the webpage content provided.

The arXiv abstract states that CRAFT uses "a variational information bottleneck module to regulate vision and language embeddings during early training" and employs "a curriculum strategy" that "encourages the model to prioritize force signals initially, before progressively restoring access to the full multimodal information."

However, the webpage only contains the paper's abstract and metadata. To answer your detailed questions about:
- The exact architectural placement of the VIB module
- The specific KL penalty scheduling mechanism
- Whether per-token or embedding-level masking is used
- The precise mathematical formulation
- How it differs from simpler regularization approaches

...I would need access to the full paper itself, which is not provided in this excerpt. The abstract provides only high-level conceptual information about what the module does, not the technical implementation details you're seeking.

To obtain these specifics, you would need to review the complete PDF or HTML version of the paper available through the arXiv links provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39042213-8e53-4ba0-8dcc-9ea57be00ef0",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "633cff56-7350-4123-8b2f-35a163c381db",
  "sourceToolAssistantUUID": "39042213-8e53-4ba0-8dcc-9ea57be00ef0",
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

_source line 28 · 2026-05-13T04:59:12.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QFWqjmMm3Vm6iUsy6cFhqg`</summary>

```json
{
  "query": "LTM-Transformer learnable token merging information bottleneck mask module arXiv 2407.15219"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "633cff56-7350-4123-8b2f-35a163c381db",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayydFNT89VH3ajiaEjV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d7619ea-6171-4689-9fa6-2f76a874dacd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011drCdiEL9mGgfyjzctDLVQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7597,
      "cache_read_input_tokens": 10051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7597,
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

_source line 29 · 2026-05-13T04:59:13.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Agk6tuzEvSM8qDgS9nSUUz`</summary>

```json
{
  "query": "\"Boosting Action-Information via Variational Bottleneck Unlabelled Robot Videos\" arXiv 2508.08743"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d7619ea-6171-4689-9fa6-2f76a874dacd",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayydFNT89VH3ajiaEjV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e221a0d8-f53d-4e03-937c-b320a7d77315",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011drCdiEL9mGgfyjzctDLVQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7597,
      "cache_read_input_tokens": 10051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7597,
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

_source line 30 · 2026-05-13T04:59:15.564Z_

<details><summary>↩ Tool result · `toolu_018Xz7e4Dj9tv1Z4UCbHMnZQ`</summary>

```text
# Technical Summary: Variational Regularization for Robot Manipulation

## Core Approach

The paper proposes Variational Regularization (VR), a lightweight module that filters noise from intermediate features in diffusion-based robot manipulation policies. The method targets the U-Net decoder's backbone features—the high-dimensional representations produced after downsampling.

## Architecture Placement

VR is inserted "immediately after the last downsampling features in the U-Net decoder" where noise accumulates most significantly. It operates on backbone features Z before they proceed through upsampling blocks, rather than on visual tokens or the encoder.

## Mathematical Formulation

The approach imposes a timestep-conditioned Gaussian distribution over backbone features:

**p_θ(Ẑ|Z,t) = 𝒩(μ_θ(Z,t), σ²_θ(Z,t))**

The training loss combines denoising and regularization:

**ℒ_policy = 𝔼[‖Â₀−A₀‖² + β·KL(p_θ(Ẑ|Z,t) ∥ q(Ẑ))]**

The KL-divergence regularizer encourages the learned distribution to match a standard normal, creating an information bottleneck that adaptively suppresses task-irrelevant noise.

## Information Bottleneck Connection

The paper theoretically grounds VR in the variational information bottleneck framework. They prove that minimizing their loss is equivalent to maximizing a variational evidence lower bound (ELBO) that balances prediction accuracy with information compression—ensuring Ẑ retains only decision-critical signals.

## Distinction from Token Masking

Unlike inference-time masking (which randomly zeros features), VR learns to continuously filter noise during training through a probabilistic bottleneck, with timestep conditioning accounting for noise variation across diffusion steps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2730ef9-9ee6-4aeb-abeb-965000bfb179",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "6fa613e2-90c8-406f-82af-13b9dae13624",
  "sourceToolAssistantUUID": "c2730ef9-9ee6-4aeb-abeb-965000bfb179",
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

_source line 31 · 2026-05-13T04:59:17.409Z_

<details><summary>↩ Tool result · `toolu_01Agk6tuzEvSM8qDgS9nSUUz`</summary>

```text
Web search results for query: ""Boosting Action-Information via Variational Bottleneck Unlabelled Robot Videos" arXiv 2508.08743"

Links: [{"title":"Boosting Action-Information via a Variational Bottleneck on Unlabelled Robot Videos","url":"https://arxiv.org/html/2508.08743v1"},{"title":"\\gradientRGBCoMo177, 31, 19231, 85, 192: Learning Continuous Latent Motion from Internet Videos for Scalable Robot Learning","url":"https://arxiv.org/html/2505.17006v1"},{"title":"ActionSink: Toward Precise Robot Manipulation with Dynamic Integration of Action Flow","url":"https://arxiv.org/html/2508.03218"},{"title":"Revisiting the Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=w10KdRwcMk"},{"title":"Learning an Actionable Discrete Diffusion Policy via Large-Scale Actionless Video Pre-Training","url":"https://arxiv.org/html/2402.14407v2"},{"title":"Generalist Robot Manipulation beyond Action Labeled Data","url":"https://arxiv.org/html/2509.19958v1"},{"title":"Large-Scale Actionless Video Pre-Training via Discrete Diffusion for Efficient Policy Learning","url":"https://arxiv.org/html/2402.14407v1"},{"title":"Towards Generalist Robot Learning from Internet Video: A Survey","url":"https://arxiv.org/html/2404.19664v4"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"},{"title":"Variational Information Bottleneck Regularized Deep Reinforcement Learning for Efficient Robotic Skill Adaptation","url":"https://www.mdpi.com/1424-8220/23/2/762"}]

Based on the search results, I found the paper you're looking for. The method leverages the variational information-bottleneck to extract action-relevant representations while discarding task-irrelevant information. 

The paper "Boosting Action-Information via a Variational Bottleneck on Unlabelled Robot Videos" (arXiv 2508.08743) appears to be a recent work published in August 2025 that focuses on learning action representations from unlabeled robot video data using information-theoretic principles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e221a0d8-f53d-4e03-937c-b320a7d77315",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "d9a91af9-7547-48cc-b3a3-41955506738f",
  "sourceToolAssistantUUID": "e221a0d8-f53d-4e03-937c-b320a7d77315",
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

_source line 32 · 2026-05-13T04:59:19.087Z_

<details><summary>↩ Tool result · `toolu_01WpzEGYJ1TAij5M6bBDzQYg`</summary>

````text
# LightVLA's Technical Token Pruning Approach

## Architecture Location
Pruning is applied **after the vision encoder but before the LLM backbone**. The framework processes initial visual tokens H_v from the encoder and selects a pruned subset H_v' to feed into the language model.

## Token Selection Mechanism

**Query Generation (Parameter-Free):**
The method generates "dynamic queries via cross attention between visual tokens and language tokens." Mathematically:

```
Q = softmax(H_v H_l^T / √D) H_l
```

This creates L_v queries—one per visual token—without introducing learnable parameters.

**Token Scoring:**
Each query scores all tokens: `S = Q H_v^T / √D`, producing an L_v × L_v score matrix where element s_i,j represents the i-th query's score for the j-th token.

**Gumbel-Softmax Differentiability:**
Rather than direct argmax (non-differentiable), the paper employs Gumbel-softmax with:
- Soft scores: `softmax(S + ε)` where ε ∈ U(0,α)
- Hard scores: one-hot(argmax(S + ε))
- Combined indicator matrix: `I = S_hard + S_soft - S_soft^SG`

This "enables differentiable token selection" during training while using direct argmax at inference.

## Key Differences from IB Regularization

**No information bottleneck regularization** is present. The approach is "purely performance-driven" with "no auxiliary losses." The model spontaneously learns token importance through end-to-end optimization, not through explicit information-theoretic constraints or reconstruction objectives.

The technique is closer to **learned discrete selection** than adaptive masking with information bottleneck regularization.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09eb5b54-3ce7-47a2-a468-babd0e6763aa",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "0b29ee7f-b371-45e5-ae45-b1346b4e6f05",
  "sourceToolAssistantUUID": "09eb5b54-3ce7-47a2-a468-babd0e6763aa",
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

_source line 33 · 2026-05-13T04:59:19.297Z_

<details><summary>↩ Tool result · `toolu_01QFWqjmMm3Vm6iUsy6cFhqg`</summary>

```text
Web search results for query: "LTM-Transformer learnable token merging information bottleneck mask module arXiv 2407.15219"

Links: [{"title":"1 Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/pdf/2407.15219"},{"title":"[2407.15219] Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/abs/2407.15219"},{"title":"Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/html/2407.15219v2"},{"title":"Efficient Visual Transformer by Learnable Token Merging - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40663671/"},{"title":"Importance-Based Token Merging for Efficient Image and Video Generation","url":"https://arxiv.org/html/2411.16720v2"},{"title":"GitHub - Statistical-Deep-Learning/LTM: Code for LTM.","url":"https://github.com/Statistical-Deep-Learning/LTM"},{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"Importance-based Token Merging for Diffusion Models","url":"https://arxiv.org/html/2411.16720v1"},{"title":"[Literature Review] Efficient Visual Transformer by Learnable Token Merging","url":"https://www.themoonlight.io/en/review/efficient-visual-transformer-by-learnable-token-merging"},{"title":"EFFICIENT VISION TRANSFORMER BY INFORMATION ...","url":"https://openreview.net/pdf?id=Jwgw3znxT3"}]

Based on the search results, I found comprehensive information about the paper arXiv 2407.15219 on LTM-Transformer (Learnable Token Merging):

## Overview

LTM-Transformer is a novel and compact transformer block that performs token merging in a learnable scheme.

## Key Concepts

The LTM-Transformer block generates an informative token merging mask, which reduces the Information Bottleneck (IB) loss for visual transformers. The token merging process is primarily inspired by the considerable redundancy in the original output tokens of transformer blocks.

## Information Bottleneck Approach

The LTM-Transformer is motivated by reduction of Information Bottleneck, with a novel and separable variational upper bound for the IB loss derived, and the architecture of the mask module in the LTM blocks is designed to reduce this derived upper bound.

## Architecture and Mechanism

In the LTM-Transformer block, the original attention output tokens are merged into fewer target tokens where every target token is an informative weighted average of the original output tokens, and these merged tokens are then fed to an MLP to produce the block's output.

## Performance and Compatibility

LTM-Transformer is compatible with many popular and compact transformer networks, reduces the FLOPs and inference time while maintaining or improving prediction accuracy, and has been integrated with backbones including MobileViT, EfficientViT, ViT, and Swin.

The code for LTM-Transformer is available at https://github.com/Statistical-Deep-Learning/LTM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d7619ea-6171-4689-9fa6-2f76a874dacd",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "a0a0ec85-a89f-48f8-a64a-9f3a988d5204",
  "sourceToolAssistantUUID": "1d7619ea-6171-4689-9fa6-2f76a874dacd",
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

_source line 34 · 2026-05-13T04:59:23.213Z_

Let me now fetch the CRAFT full paper and the LTM-Transformer paper for deeper technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0a0ec85-a89f-48f8-a64a-9f3a988d5204",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyet1d4G2uCQwx8jtd9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ec83099-8358-481f-be5b-52dd5decdd88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D8ndRYiXcD3ZcfB1yh3vK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 645,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 17648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2775,
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

_source line 35 · 2026-05-13T04:59:27.774Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Gh4PW5CwQYwGfU7dQYiq3j`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.12532",
  "prompt": "Extract ALL technical details about the Variational Information Bottleneck (VIB) module. Specifically: 1) What is the exact mathematical formulation of the VIB loss? 2) Where exactly in the architecture is VIB placed -- on vision tokens, language tokens, or both? 3) Does VIB operate per-token or on the full embedding? 4) How is the KL penalty weight (beta) scheduled during training? 5) Is there any learned masking component? 6) What is the relationship between the VIB and the curriculum strategy? 7) Any connection to token-level masking or selection?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ec83099-8358-481f-be5b-52dd5decdd88",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyet1d4G2uCQwx8jtd9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1059b901-05b7-4cb1-802a-f178499e91f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D8ndRYiXcD3ZcfB1yh3vK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 645,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 17648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2775,
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

_source line 36 · 2026-05-13T04:59:30.975Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YPDyQFWiHXEs69quW6MryE`</summary>

```json
{
  "url": "https://arxiv.org/html/2407.15219v2",
  "prompt": "Extract the technical details of how the information bottleneck theory is used in this paper. Specifically: 1) What is the variational upper bound for the IB loss they derive? 2) How does the mask module work -- is it a learned per-token mask? 3) What is the mathematical formulation connecting token merging to information bottleneck? 4) Is there a KL regularization term? 5) How does this relate to the concept of 'adaptive learned per-token masking with IB regularization'?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1059b901-05b7-4cb1-802a-f178499e91f2",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyet1d4G2uCQwx8jtd9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f937fb97-d25b-4b4d-8ee5-60c18b75b937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D8ndRYiXcD3ZcfB1yh3vK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 645,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 17648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2775,
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

_source line 37 · 2026-05-13T04:59:31.876Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QfftA5A72usZcYVooU9bQ1`</summary>

```json
{
  "query": "AutoSelect noise gate token importance frozen VLM information bottleneck arXiv 2603.07135"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f937fb97-d25b-4b4d-8ee5-60c18b75b937",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyet1d4G2uCQwx8jtd9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98f0dd3a-cd80-4dde-add9-14e324d95d25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D8ndRYiXcD3ZcfB1yh3vK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 645,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 17648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2775,
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

_source line 38 · 2026-05-13T04:59:32.722Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MBKaxY8hBK31MrLnHfgbtZ`</summary>

```json
{
  "query": "FocusVLA visual token selection attention allocation VLA model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98f0dd3a-cd80-4dde-add9-14e324d95d25",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011Cayyet1d4G2uCQwx8jtd9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1066bbb7-1cfc-403a-b4ad-978ed1fcebe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D8ndRYiXcD3ZcfB1yh3vK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 645,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 17648,
      "output_tokens": 537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2775
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 645,
          "output_tokens": 537,
          "cache_read_input_tokens": 17648,
          "cache_creation_input_tokens": 2775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2775,
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

_source line 39 · 2026-05-13T04:59:34.765Z_

<details><summary>↩ Tool result · `toolu_01Gh4PW5CwQYwGfU7dQYiq3j`</summary>

```text
# VIB Module Technical Details from CRAFT

## 1) Mathematical Formulation

The VIB loss is explicitly defined as:

**ℒ_VIB = ½∑ᵢ(−log σᵢ² + μᵢ² + σᵢ² − 1)**

This derives from minimizing mutual information I(F, F^c) between original and compressed features using KL divergence with a standard normal prior 𝒩(0,1) and learned posterior 𝒩(μ, σ²).

## 2) Placement in Architecture

VIB is applied "after the vision–language encoder" to compress "fused visual and language embeddings F_V and F_L" into compact features. The module processes both modalities jointly rather than separately.

## 3) Token-Level vs. Full Embedding

The formulation operates on **full embeddings** (indicated by the subscript indexing in the loss). The paper specifies that features are "compressed" collectively, not through per-token masking.

## 4) KL Penalty Weight Schedule

An exponential decay schedule controls the regularization strength:

**λ_VIB(t) = λ_init · exp(−t/T_decay)**

The paper states λ_VIB begins "relatively high" initially and is "gradually decreased according to an exponential decay schedule."

## 5) Learned Masking Component

**No learned masking exists.** The mechanism uses Gaussian reparameterization sampling (F^c = μ + σ·ϵ) but not selective token masking.

## 6) Relationship to Curriculum Strategy

VIB implements the curriculum directly: "strong KL penalty...suppresses high-entropy visual and language signals, compelling the policy to focus on low-entropy force inputs" early on, then gradually relaxes as λ_VIB decays.

## 7) Token-Level Selection Connection

**None.** The approach emphasizes information compression rather than discrete token selection mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1059b901-05b7-4cb1-802a-f178499e91f2",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "da841b43-e396-4bbb-8fa1-2e5ef1e370c3",
  "sourceToolAssistantUUID": "1059b901-05b7-4cb1-802a-f178499e91f2",
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

_source line 40 · 2026-05-13T04:59:39.987Z_

<details><summary>↩ Tool result · `toolu_01MBKaxY8hBK31MrLnHfgbtZ`</summary>

```text
Web search results for query: "FocusVLA visual token selection attention allocation VLA model 2026"

Links: [{"title":"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.28740"},{"title":"[2603.28740] FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.28740"},{"title":"Robotics arXiv Digest — 2026-03-30 - Kiru Park / Vision for Robotics","url":"https://www.visionforrobotics.com/robotics-digest/digest_2026-03-30.html"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"[2508.19257] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/abs/2508.19257"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.15618v2"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://arxiv.org/html/2503.22020v1"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/html/2508.19257v3"}]

I found detailed information about FocusVLA. Here's what the search results reveal:

## FocusVLA Overview

FocusVLA is a novel paradigm that directs the model's attention to task-relevant visual regions to effectively bridge vision to action.

## Core Challenges Addressed

Current auto-regressive policies in VLA models are constrained by three bottlenecks: (1) architectural bias drives models to overlook visual details, (2) an excessive number of visual tokens makes attention difficult to focus on the correct regions, and (3) task-irrelevant visual information introduces substantial noise.

## Key Technical Contributions

FocusVLA introduces two main approaches:

1. **Modality Cascaded Attention**: This eliminates shortcut pathways, thereby compelling VLA models to rely on task-relevant visual details for action generation.

2. **Focus Attention**: This dynamically selects task-relevant visual patches to control information quantity while explicitly modulating their influence to suppress task-irrelevant noise.

## Performance Results

Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that FocusVLA not only effectively leverages visual details to perform dexterous manipulations, but also substantially improves performance and accelerates convergence across a variety of tasks.

## Key Innovation

The paper's ablation reveals that a simple attention-focusing mechanism that restricts cross-attention to the top-K most task-relevant visual tokens outperforms standard attention by a larger margin than switching from a weaker to stronger visual encoder.

The paper was published on arXiv on March 30, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1066bbb7-1cfc-403a-b4ad-978ed1fcebe8",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "f6dcdb82-f59f-49eb-bdc1-344bdfa64d2c",
  "sourceToolAssistantUUID": "1066bbb7-1cfc-403a-b4ad-978ed1fcebe8",
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

_source line 41 · 2026-05-13T04:59:40.730Z_

<details><summary>↩ Tool result · `toolu_01QfftA5A72usZcYVooU9bQ1`</summary>

```text
Web search results for query: "AutoSelect noise gate token importance frozen VLM information bottleneck arXiv 2603.07135"

Links: [{"title":"THE MODEL KNOWS WHICH TOKENS MATTER: AUTOMATIC TOKEN SELECTION VIA NOISE GATING","url":"https://arxiv.org/pdf/2603.07135"},{"title":"[2603.07135] The Model Knows Which Tokens Matter: Automatic Token Selection via Noise Gating","url":"https://arxiv.org/abs/2603.07135"},{"title":"The Model Knows Which Tokens Matter: Automatic Token Selection via Noise Gating | Scilit","url":"https://www.scilit.com/publications/006f0ba5eaa3ff990cfb4f191686c92f"},{"title":"TIR-Flow: Active Video Search and Reasoning with Frozen VLMs","url":"https://arxiv.org/html/2601.06176"},{"title":"Stateful Token Reduction for Long-Video Hybrid VLMs","url":"https://arxiv.org/html/2603.00198"},{"title":"G-MemLLM: Gated Latent Memory Augmentation for Long-Context Reasoning in Large Language Models","url":"https://arxiv.org/html/2602.00015"},{"title":"[2503.21757] Fwd2Bot: LVLM Visual Token Compression with Double Forward Bottleneck","url":"https://arxiv.org/abs/2503.21757"},{"title":"[2603.05663] Keeping the Evidence Chain: Semantic Evidence Allocation for Training-Free Token Pruning in Video Temporal Grounding","url":"https://arxiv.org/abs/2603.05663"},{"title":"Token-level Inference-Time Alignment for Vision-Language Models","url":"https://arxiv.org/html/2510.21794v1"},{"title":"DeAR: Fine-Grained VLM Adaptation by Decomposing Attention Head Roles","url":"https://arxiv.org/html/2603.01111"}]

I found relevant information about arXiv paper 2603.07135. Here's what the search reveals:

## AutoSelect: Automatic Token Selection via Noise Gating

AutoSelect attaches a lightweight Scorer and Denoiser to a frozen VLM and trains with only the standard next token prediction loss, without auxiliary objectives or extra annotations.

### Key Framework Components

Visual tokens from the frozen Image Encoder pass through a learnable Scorer that assigns per-token importance scores. These scores are polarized by the differentiable Soft Top-K operator under a fixed bandwidth budget K. During training, a VP Noise Gate injects variance-preserving noise into each token in inverse proportion to its score; the Denoiser then maps the perturbed sequence back toward the LLM's expected input space. At inference, the Denoiser and noise injection are discarded: Hard Top-K retains the K highest-scoring tokens with their original position indices.

### Problem Formulation

The paper reformulates visual token pruning as capacity constrained communication: given a fixed budget K, the model must allocate limited bandwidth to maximally preserve visual information.

### Performance Results

On ten VLM benchmarks, AutoSelect retains 96.5% of full model accuracy while accelerating LLM prefill by 2.85x with only 0.69 ms overhead, and transfers to different VLM backbones without architecture-specific tuning.

The paper addresses the computational redundancy in vision-language models by proposing a trainable selection mechanism that works with frozen VLM architectures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98f0dd3a-cd80-4dde-add9-14e324d95d25",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "1832d149-a090-416a-aa5b-919b3ab05e65",
  "sourceToolAssistantUUID": "98f0dd3a-cd80-4dde-add9-14e324d95d25",
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

_source line 42 · 2026-05-13T04:59:42.304Z_

<details><summary>↩ Tool result · `toolu_01YPDyQFWiHXEs69quW6MryE`</summary>

````text
# Information Bottleneck Theory in LTM-Transformer

## 1. Variational Upper Bound for IB Loss

The paper derives a separable variational upper bound (IBB) for the IB loss defined as:
- **IB Loss**: `IB(G) = I(X̃(G),X) - I(X̃(G),Y)` where X̃(G) represents merged tokens, X is input, and Y is labels
- **Upper Bound** (Theorem 3.1): The authors establish that `IB(G) ≤ IBB(G) - C₀`, where IBB is computed as a weighted sum over training samples and classes using soft assignment functions

## 2. Mask Module Architecture

The mask module generates token merging masks through a two-step process:

**Step 1** (Equation 3): Update via gradient descent on IBB bound:
```
G̃(ℓ) = G(ℓ-1) - (2η/n)∑ᵢ∑ₐ Zᵢ[gradient terms]
```

**Step 2** (Equation 4): Apply learned binary mask:
```
G(ℓ) = G̃(ℓ) ∘ M(ℓ)
```

Where M(ℓ) is a binarized mask from LTMP using "Gumbel-Softmax operation on N×P learnable parameters." This represents **learned per-token masking** where each token's contribution is weighted adaptively.

## 3. Mathematical Connection: Token Merging to Information Bottleneck

The formulation interprets multi-layer transformers as iterative IB optimization:

- **Proposition 3.2** establishes that at step ℓ of gradient descent on IBB, the mask follows: `G(ℓ) = G(ℓ-1) - η∇_G IBB(G(ℓ-1))`
- Each LTM block performs "one-step gradient descent on IBB(G)" 
- The mask receives inputs from: previous layer's mask G(ℓ-1), current attention outputs Z, and class centroids

This grounds token merging in principled IB theory rather than heuristic similarity matching.

## 4. Regularization Structure

**No explicit KL regularization term** appears in the training loss. Instead:
- Training uses "regular cross-entropy loss"
- IB principles guide **mask generation architecture** via the derived bound IBB
- The gradient descent formulation (Eq. 3) implicitly incorporates the IB objective into mask updates
- A warmup phase (Algorithm 1, line 3-4) trains without token merging initially

## 5. Relation to Adaptive Learned Per-Token Masking with IB Regularization

This work instantiates adaptive per-token masking through:

1. **Adaptivity**: Masks G(ℓ) depend on current layer's attention outputs and evolve across layers
2. **Learning**: M(ℓ) parameters trained end-to-end via "standard SGD" 
3. **IB Regularization**: Rather than explicit penalty terms, the mask module architecture itself is "designed to reduce the derived upper bound for the IB loss"

The approach differs from typical regularization—it achieves IB-compliance through architectural design that makes masks directly optimize the separable IBB bound, enabling "end-to-end manner with standard SGD" without additional loss terms.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f937fb97-d25b-4b4d-8ee5-60c18b75b937",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "694574c5-9e9f-4577-8bbb-a18276f0a2ff",
  "sourceToolAssistantUUID": "f937fb97-d25b-4b4d-8ee5-60c18b75b937",
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

_source line 43 · 2026-05-13T04:59:51.023Z_

Let me do a couple more targeted searches to be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "694574c5-9e9f-4577-8bbb-a18276f0a2ff",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayygaNn95MKpTC8ZJT9h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70fc0be2-77af-41e8-94d6-b04d3bbea01c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4gWdtAvXKiA6btpBRDfS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1818,
      "cache_creation_input_tokens": 2637,
      "cache_read_input_tokens": 20423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2637,
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

_source line 44 · 2026-05-13T04:59:53.374Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ULrJnyFKV2EmiSPqND2zu1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.07135",
  "prompt": "Does this paper frame the noise gating mechanism as an information bottleneck? Is there any explicit IB regularization term in the loss? How is the noise injection related to variational information bottleneck theory? What is the mathematical connection, if any, to IB?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70fc0be2-77af-41e8-94d6-b04d3bbea01c",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayygaNn95MKpTC8ZJT9h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b94fa09-bc38-4e3e-9b02-2545706ffe24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4gWdtAvXKiA6btpBRDfS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1818,
      "cache_creation_input_tokens": 2637,
      "cache_read_input_tokens": 20423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2637,
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

_source line 45 · 2026-05-13T04:59:54.375Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016BLJHrEv61CVmTTxUh2A7U`</summary>

```json
{
  "query": "\"token masking after projector\" \"information bottleneck\" vision language model VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b94fa09-bc38-4e3e-9b02-2545706ffe24",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayygaNn95MKpTC8ZJT9h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "165da78b-746e-4e71-9031-6d84b9136c67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4gWdtAvXKiA6btpBRDfS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1818,
      "cache_creation_input_tokens": 2637,
      "cache_read_input_tokens": 20423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2637,
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

_source line 46 · 2026-05-13T04:59:55.460Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018zWcb9aykQ2tDj33BZALn8`</summary>

```json
{
  "query": "Fwd2Bot forward bottleneck LVLM visual token compression arXiv 2503.21757"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "165da78b-746e-4e71-9031-6d84b9136c67",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayygaNn95MKpTC8ZJT9h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7cd66a8-e187-461b-9d3e-39d52ef4d4c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4gWdtAvXKiA6btpBRDfS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1818,
      "cache_creation_input_tokens": 2637,
      "cache_read_input_tokens": 20423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2637,
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

_source line 47 · 2026-05-13T04:59:56.886Z_

<details><summary>↩ Tool result · `toolu_01ULrJnyFKV2EmiSPqND2zu1`</summary>

```text
# Response Based on Available Content

Based on the webpage content provided, I cannot definitively answer your questions about information bottleneck (IB) framing or variational IB theory connections.

The abstract describes the approach as "capacity constrained communication" where "the model must allocate limited bandwidth to maximally preserve visual information." While this conceptualization shares philosophical similarities with information bottleneck principles, the page does not explicitly mention IB theory, IB regularization terms, or variational information bottleneck frameworks.

The paper states training occurs "with only the standard next token prediction loss, without auxiliary objectives or extra annotations," suggesting no explicit IB regularization is used. However, the full technical details—including whether the noise gating mechanism has theoretical connections to IB—would require consulting the actual paper PDF or full text, which are not provided in this webpage excerpt.

**To properly address your questions, you would need to review the complete paper.**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b94fa09-bc38-4e3e-9b02-2545706ffe24",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "a95be323-aabd-400b-85a1-3a194b84ffdc",
  "sourceToolAssistantUUID": "5b94fa09-bc38-4e3e-9b02-2545706ffe24",
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

_source line 48 · 2026-05-13T05:00:02.034Z_

<details><summary>↩ Tool result · `toolu_018zWcb9aykQ2tDj33BZALn8`</summary>

```text
Web search results for query: "Fwd2Bot forward bottleneck LVLM visual token compression arXiv 2503.21757"

Links: [{"title":"[2503.21757] Fwd2Bot: LVLM Visual Token Compression with Double Forward Bottleneck","url":"https://arxiv.org/abs/2503.21757"},{"title":"Fwd2Bot: LVLM Visual Token Compression with Double Forward Bottleneck","url":"https://arxiv.org/html/2503.21757"},{"title":"Fwd2Bot: LVLM Visual Token Compression with Double Forward Bottleneck | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/fwd2bot-lvlm-visual-token-compression-double-forward"},{"title":"Computer Science Mar 2025","url":"https://arxiv.org/list/cs/2025-03?skip=10575&show=25"},{"title":"Persistent Visual Memory: Sustaining Perception for Deep Generation in LVLMs","url":"https://arxiv.org/pdf/2605.00814"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=3500&show=50"},{"title":"VISion On Request: Enhanced VLLM efficiency with sparse, dynamically selected, vision-language interactions","url":"https://arxiv.org/html/2603.23495"},{"title":"Rethinking Token Reduction for Large Vision-Language Models","url":"https://arxiv.org/html/2603.21701"},{"title":"LUVC: Lossless Ultimate Vision Compression","url":"https://www.emergentmind.com/topics/lossless-ultimate-vision-tokens-compression-luvc"},{"title":"Less Is More — Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models","url":"https://arxiv.org/html/2601.12042"}]

Based on the search results, I found detailed information about the paper you're looking for:

## Fwd2Bot: LVLM Visual Token Compression with Double Forward Bottleneck

The research aims to compress the vision tokens of a Large Vision Language Model (LVLM) into a representation that is suitable for both generative and discriminative tasks, nearly lossless, and storage-efficient. The proposed approach, called Fwd2Bot, uses the LVLM itself to compress the visual information in a task-agnostic manner.

### Core Technology

At the core of Fwd2Bot is a "double-forward pass" training strategy where, during the first forward pass, the LLM condenses the visual information into a small number of summary tokens. Then, using the same LLM, the second forward pass processes the language instruction(s) alongside the summary tokens, used as a direct replacement for the image ones.

### Key Results

The researchers developed a "token reduction" technique that cuts down the number of image tokens by 75% while maintaining almost the same level of performance. More specifically, the method reduces visual tokens by 75% (from 576 to 144) while maintaining 97-99% of the original performance across various tasks.

### Authors and Citation

The paper was authored by Adrian Bulat, Yassine Ouali, and Georgios Tzimiropoulos and was published on arXiv (2503.21757) in March 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7cd66a8-e187-461b-9d3e-39d52ef4d4c0",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "e7ee5719-433c-442c-a001-aca373667eaf",
  "sourceToolAssistantUUID": "b7cd66a8-e187-461b-9d3e-39d52ef4d4c0",
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

_source line 49 · 2026-05-13T05:00:08.071Z_

<details><summary>↩ Tool result · `toolu_016BLJHrEv61CVmTTxUh2A7U`</summary>

```text
Web search results for query: ""token masking after projector" "information bottleneck" vision language model VLA 2025 2026"

Links: [{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"Unified Vision-Language-Action Tokenization","url":"https://www.emergentmind.com/topics/unified-vision-language-action-vla-tokenization"},{"title":"(PDF) When LLaVA Meets Objects: Token Composition for Vision-Language-Models","url":"https://www.researchgate.net/publication/400459405_When_LLaVA_Meets_Objects_Token_Composition_for_Vision-Language-Models"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"ICML Poster The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering","url":"https://icml.cc/virtual/2025/poster/46338"},{"title":"When LLaVA Meets Objects: Token Composition for Vision-Language-Models","url":"https://arxiv.org/html/2602.04864v1"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering | OpenReview","url":"https://openreview.net/forum?id=7BKcLeHQsm"},{"title":"Vision Encoders in Vision-Language Models: A Survey Han Xiao Jina AI by Elastic","url":"https://jina.ai/vision-encoder-survey.pdf"}]

I found relevant research on token masking, projectors, and information bottlenecks in vision-language and vision-language-action models from 2025-2026. Here are the key findings:

## Information Bottleneck and Token Compression in VLMs/VLAs

Recent VLA research aims to break the "Perception-First bottleneck" prevalent in existing VLA pruning methods—the over-reliance on the static attention weights of pre-trained Vision-Language Models (VLMs). This reliance often causes models to prioritize semantic salience over physical affordances, inadvertently discarding geometric structures during compression that are visually sparse but critical for physical manipulation.

## Token Masking Approaches After Projection

Tokens from different granularity levels are passed into a multimodal projector, which enables the fusion of features. By incorporating hierarchical representations, models can significantly reduce the number of tokens required while maintaining performance.

Projection-based approaches compute alignment scores to adaptively select background-only filtering or conservative/aggressive masking, producing union masks for token selection.

## Visual Token Pruning in VLA Models

VLA model deployment on resource-constrained platforms is often bottlenecked by heavy attention-based computation over large sets of visual tokens. Recent approaches use adaptive, performance-driven pruning of visual tokens through dynamic queries to evaluate token importance, learning to preserve the most informative visual tokens while pruning tokens that do not contribute to task execution.

## Information Loss in VLMs

Research on LVLMs reveals patterns in how these models process information including gradual visual information loss—visually grounded tokens gradually become less favored throughout generation.

The search results show active research into efficient token handling in both VLMs and VLAs, with particular focus on maintaining task-critical information while reducing computational bottlenecks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "165da78b-746e-4e71-9031-6d84b9136c67",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "a4e15c3fb5c71de91",
  "type": "user",
  "uuid": "3db1dcd6-62ee-4d8e-b572-33814fcd05f2",
  "sourceToolAssistantUUID": "165da78b-746e-4e71-9031-6d84b9136c67",
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

_source line 50 · 2026-05-13T05:00:58.617Z_

Now I have a comprehensive picture. Here is my assessment:

---

## Novelty Assessment: "Token masking after the projector creates an implicit variational information bottleneck"

### Verdict: The specific combination is novel in its precise framing, but each individual component has close precedent. The novelty is incremental rather than fundamental.

---

### Most Directly Relevant Prior Work

**1. CRAFT (arXiv 2602.12532, Feb 2026)** -- **VERY CLOSE**
- Applies an explicit Variational Information Bottleneck (VIB) module to VLA models, placed *after the vision-language encoder*.
- Loss: `L_VIB = 1/2 * sum(-log(sigma_i^2) + mu_i^2 + sigma_i^2 - 1)` with KL divergence against standard normal prior.
- Uses exponential decay scheduling: `lambda_VIB(t) = lambda_init * exp(-t/T_decay)` to anneal the bottleneck strength.
- Operates on **full embeddings** (not per-token masking), compressing fused vision+language features via Gaussian reparameterization.
- **Key difference from the claimed idea**: CRAFT uses continuous Gaussian compression, not discrete token masking. But it does apply VIB theory explicitly in a VLA context, which directly undermines any claim that connecting IB theory to VLA is novel.

**2. Information Filtering via Variational Regularization (arXiv 2601.21926, Jan 2026)** -- **CLOSE**
- Applies a variational bottleneck to intermediate features in diffusion-based robot manipulation policies.
- Loss: `L = E[||A_hat - A||^2 + beta * KL(p_theta(Z_hat|Z,t) || q(Z_hat))]`
- Placed after downsampling in U-Net decoder; uses timestep-conditioned Gaussian over backbone features.
- Theoretically grounded in VIB framework. Explicitly proves the loss is equivalent to maximizing a variational ELBO that balances prediction accuracy with information compression.
- **Key difference**: Applied to diffusion policy architecture, not after a VLM projector. Not per-token masking.

**3. LTM-Transformer (arXiv 2407.15219, Jul 2024)** -- **ARCHITECTURALLY CLOSEST**
- Derives a separable variational upper bound for the IB loss and designs a mask module to minimize it.
- Uses **Gumbel-Softmax on learnable per-token parameters** to generate binary masks for token merging.
- Each LTM block performs one-step gradient descent on the IB bound, making token merging explicitly IB-optimal.
- **This is essentially "adaptive learned per-token masking with IB regularization"** -- but applied to vision transformers for classification, not to VLA models or after a projector.

**4. LightVLA (arXiv 2509.12594, Sep 2025)** -- **RELEVANT**
- Differentiable per-token pruning for VLA models using Gumbel-Softmax selection.
- Applied after the vision encoder, before the LLM backbone.
- **No IB regularization** -- purely performance-driven with no auxiliary losses.
- Close architecturally (learned token selection in VLA) but lacks the IB theoretical framing.

**5. AutoSelect / Noise Gating (arXiv 2603.07135, Mar 2026)** -- **RELEVANT**
- Frames visual token pruning as "capacity-constrained communication" (philosophically related to IB).
- Injects variance-preserving noise inversely proportional to learned token importance scores on a frozen VLM.
- No explicit IB regularization term; trained with standard next-token prediction loss only.
- The noise injection mechanism is reminiscent of VIB (adding noise to compress information) but not explicitly framed as such.

**6. FocusVLA (arXiv 2603.28740, Mar 2026)** -- **CONTEXTUALLY RELEVANT**
- Dynamically selects task-relevant visual patches in VLA models via attention-based top-K selection.
- No IB framing; purely attention-driven.

**7. Gaze-Regularized VLA (arXiv 2603.23202, Mar 2026)** -- **TANGENTIALLY RELEVANT**
- Regularizes attention via KL divergence against human gaze heatmaps.
- Not IB-framed; uses human priors rather than information-theoretic compression.

---

### Summary Assessment

| Component | Has precedent? | Where? |
|---|---|---|
| VIB applied to VLA | **Yes** | CRAFT (2602.12532) -- explicit VIB in VLA |
| VIB for robot manipulation | **Yes** | Variational Regularization (2601.21926) |
| Learned per-token masking with IB | **Yes** | LTM-Transformer (2407.15219) -- Gumbel-Softmax masks optimizing IB bound |
| Differentiable token selection in VLA | **Yes** | LightVLA (2509.12594) |
| Token masking *after projector* + IB | **Not found exactly** | No paper places learned IB-regularized masks specifically after the VLM projector layer |

The **exact combination** -- "learned per-token masking placed after the projector, framed as an implicit variational information bottleneck" -- does not appear verbatim in any single paper. However:

- CRAFT already applies VIB to vision-language embeddings in VLA (just not as discrete token masking).
- LTM-Transformer already does learned per-token masking with IB regularization (just not in VLA or after a projector).
- LightVLA already does differentiable per-token selection in VLA (just without IB framing).
- AutoSelect does noise-gated per-token selection on frozen VLMs with noise injection resembling VIB.

The claimed novelty is therefore best characterized as a **recombination of known ideas** rather than a genuinely new theoretical insight. The theoretical observation that "masking creates an information bottleneck" is well-established in the IB literature; applying it specifically after a projector in a VLA is a positional/architectural choice, not a new theoretical contribution.

Sources:
- [CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning](https://arxiv.org/abs/2602.12532)
- [Information Filtering via Variational Regularization for Robot Manipulation](https://arxiv.org/html/2601.21926v1)
- [LTM-Transformer: Efficient Visual Transformer by Learnable Token Merging](https://arxiv.org/abs/2407.15219)
- [LightVLA: Differentiable Token Pruning for VLA Models](https://arxiv.org/html/2509.12594v1)
- [AutoSelect: Automatic Token Selection via Noise Gating](https://arxiv.org/abs/2603.07135)
- [FocusVLA: Focused Visual Utilization for VLA Models](https://arxiv.org/abs/2603.28740)
- [Gaze-Regularized VLA Models for Robotic Manipulation](https://arxiv.org/abs/2603.23202)
- [Fwd2Bot: LVLM Visual Token Compression with Double Forward Bottleneck](https://arxiv.org/abs/2503.21757)
- [Boosting Action-Information via a Variational Bottleneck on Unlabelled Robot Videos](https://arxiv.org/html/2508.08743v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3db1dcd6-62ee-4d8e-b572-33814fcd05f2",
  "isSidechain": true,
  "agentId": "a4e15c3fb5c71de91",
  "requestId": "req_011CayyiUZqSsD6ir6ysR8ov",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "894817a3-3f0f-42af-b79a-d9744f3b6617",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkT9CbAJtK6dsARnu9ZqB7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 863,
      "cache_creation_input_tokens": 3321,
      "cache_read_input_tokens": 23060,
      "output_tokens": 1870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3321
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 863,
          "output_tokens": 1870,
          "cache_read_input_tokens": 23060,
          "cache_creation_input_tokens": 3321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3321,
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
