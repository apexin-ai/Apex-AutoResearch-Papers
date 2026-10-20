# Research conversation: I need to verify conference deadlines for robotics/AI venues in 2026-2027. Please search for: 1. "CoRL 2026 deadline sub

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aac89d5f08aeef3c3.jsonl`
- **Structured JSON:** [`d3a1c4f0f59e8f2415e8.json`](../../sessions/d3/d3a1c4f0f59e8f2415e8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-13T06:56:54.021Z_

I need to verify conference deadlines for robotics/AI venues in 2026-2027. Please search for:

1. "CoRL 2026 deadline submission date" - verify the exact paper submission deadline
2. "AAAI 2027 call for papers deadline" 
3. "ICLR 2027 submission deadline"
4. "ICRA 2027 submission deadline"
5. "RSS 2026 deadline" or "RSS 2027 deadline"
6. "NeurIPS 2026 deadline"

Also search for: "robotics AI conference deadlines 2026 2027"

Report the exact deadlines you find, noting which are confirmed vs estimated. Today's date is 2026-05-13.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "a895214c-6d52-4af3-81c9-4740df4d4460",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T06:56:54.024Z_

```json
{
  "parentUuid": "a895214c-6d52-4af3-81c9-4740df4d4460",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
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
  "uuid": "8edf2dfc-fccb-4129-83cd-8e9c0ec24e9e",
  "timestamp": "2026-05-13T06:56:54.024Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T06:56:56.787Z_



I'll search for all these conference deadlines in parallel. Let me first load the WebSearch tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8edf2dfc-fccb-4129-83cd-8e9c0ec24e9e",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8cuzBYd32zwJ3Ct3mf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6121c5b6-c6ce-464a-9d86-230171ac1ee5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dqen8BcJq1T5DMbrsNgjkS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 721,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-13T06:56:57.035Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XukERs8c9DEakygpr7GNyM`</summary>

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
  "parentUuid": "6121c5b6-c6ce-464a-9d86-230171ac1ee5",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8cuzBYd32zwJ3Ct3mf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee561a40-84f6-42cf-8afe-1f9614b5e54d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dqen8BcJq1T5DMbrsNgjkS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 8223,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 721
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 721,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 721,
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

_source line 5 · 2026-05-13T06:56:57.038Z_

<details><summary>↩ Tool result · `toolu_01XukERs8c9DEakygpr7GNyM`</summary>

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
  "parentUuid": "ee561a40-84f6-42cf-8afe-1f9614b5e54d",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "804eb8d8-1947-405b-a80f-e50e2eb64c55",
  "sourceToolAssistantUUID": "ee561a40-84f6-42cf-8afe-1f9614b5e54d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T06:56:59.325Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "804eb8d8-1947-405b-a80f-e50e2eb64c55",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8d96UUrAG1Vi7F2Tup",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16800b7e-598b-4b15-8c9b-ea21e4305d67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfzEs5VFm23uMxtCAoKMHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 7 · 2026-05-13T06:56:59.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pb1cxfdGguHzud18m7Z3Zt`</summary>

```json
{
  "query": "CoRL 2026 deadline submission date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16800b7e-598b-4b15-8c9b-ea21e4305d67",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8d96UUrAG1Vi7F2Tup",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05ad9d4a-0806-4acd-82ed-3ae08260e14a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfzEs5VFm23uMxtCAoKMHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 8 · 2026-05-13T06:57:00.278Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0162gnARyQPSSSqN61iYXowD`</summary>

```json
{
  "query": "AAAI 2027 call for papers deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05ad9d4a-0806-4acd-82ed-3ae08260e14a",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8d96UUrAG1Vi7F2Tup",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44e73a73-d92a-40fd-9f27-0a013f860d14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfzEs5VFm23uMxtCAoKMHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 9 · 2026-05-13T06:57:00.283Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EeDcFvUiUTQFeQfexSmD2F`</summary>

```json
{
  "query": "ICLR 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44e73a73-d92a-40fd-9f27-0a013f860d14",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8d96UUrAG1Vi7F2Tup",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa4762ed-2077-44c1-be77-d57770109ec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfzEs5VFm23uMxtCAoKMHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 10 · 2026-05-13T06:57:00.749Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013XAC1w5oozQ7Y3wu6uzJmj`</summary>

```json
{
  "query": "ICRA 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa4762ed-2077-44c1-be77-d57770109ec3",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8d96UUrAG1Vi7F2Tup",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f19c4076-c551-4396-9311-5aa4327e1867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfzEs5VFm23uMxtCAoKMHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 11 · 2026-05-13T06:57:01.242Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018YjP8FTUnoruGZn6sHG2CL`</summary>

```json
{
  "query": "RSS 2026 2027 robotics deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f19c4076-c551-4396-9311-5aa4327e1867",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8d96UUrAG1Vi7F2Tup",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f1fe217-5475-4207-aaa9-6a7b2dcb63ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfzEs5VFm23uMxtCAoKMHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 12 · 2026-05-13T06:57:01.743Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014GaveUqtQphZsGbwkmmETi`</summary>

```json
{
  "query": "NeurIPS 2026 deadline submission date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f1fe217-5475-4207-aaa9-6a7b2dcb63ae",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8d96UUrAG1Vi7F2Tup",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec9b4c91-1aba-45dc-a810-84bc9e8b3a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfzEs5VFm23uMxtCAoKMHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 13 · 2026-05-13T06:57:01.796Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A4V8UNcG62uG8NEa7mnR5F`</summary>

```json
{
  "query": "robotics AI conference deadlines 2026 2027"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec9b4c91-1aba-45dc-a810-84bc9e8b3a20",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8d96UUrAG1Vi7F2Tup",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46b045f2-0047-49f3-b4ee-74dd80ac262c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfzEs5VFm23uMxtCAoKMHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 14 · 2026-05-13T06:57:03.282Z_

<details><summary>↩ Tool result · `toolu_01Pb1cxfdGguHzud18m7Z3Zt`</summary>

```text
Web search results for query: "CoRL 2026 deadline submission date"

Links: [{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Vincent Vanhoucke's Post","url":"https://www.linkedin.com/posts/vanhoucke_corl-2026-website-is-officially-live-at-http-activity-7432112475480817664-gBos"},{"title":"CoRL 2026 - Registration","url":"https://www.corl.org/attending/registration"}]

Based on the search results, here are the CoRL 2026 submission deadlines:

The abstract submission deadline is May 26, 2026 at 11:59 UTC and the paper submission deadline is May 29, 2026 at 11:59 UTC.

Note: There appears to be a slight discrepancy in one source that mentions May 25 for abstract submission and May 28 for paper submission, but the more recent and detailed sources confirm May 26 and May 29, 2026 respectively.

The CoRL 2026 conference itself will be held November 9-12, 2026 in Austin, Texas, US.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05ad9d4a-0806-4acd-82ed-3ae08260e14a",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "7f65a835-cd18-4b89-a8a0-eed5c9ec06cb",
  "sourceToolAssistantUUID": "05ad9d4a-0806-4acd-82ed-3ae08260e14a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-13T06:57:04.315Z_

<details><summary>↩ Tool result · `toolu_0162gnARyQPSSSqN61iYXowD`</summary>

```text
Web search results for query: "AAAI 2027 call for papers deadline"

Links: [{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, the AAAI 2027 paper submission deadline and abstract deadline are both TBD (To Be Determined). However, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027. For the official call for papers and confirmed deadlines, you can check the official AAAI 2027 call for papers at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44e73a73-d92a-40fd-9f27-0a013f860d14",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "6803e954-6dab-4815-805b-faa1eeddf207",
  "sourceToolAssistantUUID": "44e73a73-d92a-40fd-9f27-0a013f860d14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T06:57:04.369Z_

<details><summary>↩ Tool result · `toolu_01EeDcFvUiUTQFeQfexSmD2F`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline"

Links: [{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"2025 Dates and Deadlines","url":"https://iclr.cc/Conferences/2025/Dates"}]

Based on the search results, I was unable to find specific information about the ICLR 2027 submission deadline. The search results primarily contain information about ICLR 2026 and earlier years, but no official announcement about ICLR 2027's submission deadline appears to be available yet.

ICLR is typically held in late April or early May each year, and based on the pattern from ICLR 2026 where the deadline for paper submissions was September 24, future years would likely follow a similar timeline. However, the official ICLR 2027 Call for Papers and specific submission deadlines have not yet been announced.

For the most current information about ICLR 2027 deadlines, I recommend checking the official ICLR website at iclr.cc or subscribing to their conference announcements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa4762ed-2077-44c1-be77-d57770109ec3",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "94ac12fe-6c4f-4137-b42c-bb9efc032918",
  "sourceToolAssistantUUID": "aa4762ed-2077-44c1-be77-d57770109ec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T06:57:04.387Z_

<details><summary>↩ Tool result · `toolu_013XAC1w5oozQ7Y3wu6uzJmj`</summary>

```text
Web search results for query: "ICRA 2027 submission deadline"

Links: [{"title":"IEEE ICRA 2027 | Calls for Papers and Posters","url":"https://2027.ieee-icra.org/contribute/"},{"title":"2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"},{"title":"ICRA - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"},{"title":"IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com","url":"https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1454"},{"title":"Conference Calender 2027 in Kanazawa Institute of Technology","url":"https://wwwr.kanazawa-it.ac.jp/kawai/calendar/2027/cal27.html"},{"title":"ICRA 2030: Submit Your Proposal! The IEEE #Robotics ...","url":"https://www.facebook.com/ieee.ras/posts/icra-2030-submit-your-proposalthe-ieee-robotics-and-automation-society-ras-invit/697022755988706/"},{"title":"Start Page of the Conference Management System","url":"https://ras.papercept.net/conferences/scripts/start.pl"},{"title":"Timetable 2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853/timetable.html"}]

Based on the search results, I found that ICRA 2027 is held in Seoul, South Korea, from May 24-28, 2027. However, the search results did not contain the specific submission deadline for ICRA 2027. 

The official ICRA 2027 website (2027.ieee-icra.org) appears in the results, but the content shown only references older submission deadlines. For the most current and accurate ICRA 2027 submission deadline, I recommend visiting the official ICRA 2027 website directly or checking the IEEE Robotics and Automation Society's official conference page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f19c4076-c551-4396-9311-5aa4327e1867",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "8752b098-b1b8-4c54-9598-d0bcbc5525a2",
  "sourceToolAssistantUUID": "f19c4076-c551-4396-9311-5aa4327e1867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T06:57:05.666Z_

<details><summary>↩ Tool result · `toolu_014GaveUqtQphZsGbwkmmETi`</summary>

```text
Web search results for query: "NeurIPS 2026 deadline submission date"

Links: [{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"NeurIPS Conference on X: \"The NeurIPS 2026 submission site opening has been moved to April 15th. Note that all tracks (Main Submission, Evaluations &amp; Datasets, and Position Papers) share the same dates. The final submission deadlines remain unchanged: • Paper Abstracts: May 4th (AOE) • Full Papers:\" / X","url":"https://x.com/NeurIPSConf/status/2041303457554940336"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"Neural Information Processing Systems (NeurIPS), 2026 | ServiceNow AI Research","url":"https://www.servicenow.com/research/event/2026-neurips.html"},{"title":"NeurIPS 2026 Conference | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FConference"}]

Based on the search results, here are the NeurIPS 2026 paper submission deadlines:

The abstract submission deadline is May 4, 2026 (AOE), and the full paper submission deadline, including all supplementary materials, is May 6, 2026 AOE.

The submission site opening has been moved to April 15th, and all tracks (Main Submission, Evaluations & Datasets, and Position Papers) share the same dates.

The conference itself will be held from Sunday, December 6th through Saturday the 12th, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec9b4c91-1aba-45dc-a810-84bc9e8b3a20",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "1e3548c8-b27d-4654-8560-424c746e773c",
  "sourceToolAssistantUUID": "ec9b4c91-1aba-45dc-a810-84bc9e8b3a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T06:57:06.155Z_

<details><summary>↩ Tool result · `toolu_018YjP8FTUnoruGZn6sHG2CL`</summary>

```text
Web search results for query: "RSS 2026 2027 robotics deadline submission"

Links: [{"title":"Call for Papers · Robotics: Science and Systems","url":"https://roboticsconference.org/information/cfp/"},{"title":"RSS: Robotics: Science and Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2506&f=Robotics"},{"title":"Robotics: Science and Systems · A Robotics Conference","url":"https://roboticsconference.org/"},{"title":"RSS 2026 Conference - Robotics","url":"https://openreview.net/group?id=roboticsfoundation.org%2FRSS%2F2026%2FConference"},{"title":"[Meetings] RSS 2026 Call for Papers","url":"https://groups.google.com/g/rl-list/c/NDYhLboynpg"},{"title":"Robotics: Science and Systems (@RoboticsSciSys) / Posts ...","url":"https://x.com/RoboticsSciSys"},{"title":"RSS SemRob 2026","url":"https://semrob.github.io/"},{"title":"Robotics: Science and Systems on X: \"📢 Save the Date! RSS 2026 will take place July 13–17, 2026 in Sydney, Australia. Submission deadlines to be announced soon (likely mid–late January 2026). 🦾 Prepare your best work! https://t.co/ybIds7mOMq\" / X","url":"https://x.com/RoboticsSciSys/status/1976107492808482875"},{"title":"Calendar - RSS Foundation","url":"https://roboticsfoundation.org/policies/calendar/"},{"title":"Calls for papers | Science | AAAS","url":"https://www.science.org/content/page/calls-papers"}]

Based on the search results, here's what I found about RSS submission deadlines:

## RSS 2026 Submission Deadlines

For RSS 2026, the deadlines are: Abstract January 23, full paper January 30, and supplementary materials February 6 (Anywhere on Earth). Additionally, workshops and tutorials have a February 12 deadline, and Early Career Spotlight nominations are due March 1.

## Conference Details

RSS 2026 will be held July 13-17, 2026 in Sydney, Australia.

## Paper Submission Requirements

RSS 2026 has a maximum paper length of 8 pages, excluding references. The conference continues the tradition of double-blind reviews, and authors should not list their names on the title page with anonymity maintained in the paper.

However, I did not find specific information about RSS 2027 submission deadlines in the search results, as those would likely be announced closer to that conference date.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f1fe217-5475-4207-aaa9-6a7b2dcb63ae",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "6c97c518-c198-4eed-a57e-286227c25a3b",
  "sourceToolAssistantUUID": "9f1fe217-5475-4207-aaa9-6a7b2dcb63ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T06:57:07.756Z_

<details><summary>↩ Tool result · `toolu_01A4V8UNcG62uG8NEa7mnR5F`</summary>

```text
Web search results for query: "robotics AI conference deadlines 2026 2027"

Links: [{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"2026 IEEE International Conference on Robotics and Automation (ICRA)","url":"https://2026.ieee-icra.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Global Guide to 2026 AI & Robotics Conferences (with Urgent Deadlines & Official Websites)--iConf","url":"https://www.iconf.org/news/729"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"RAAI 2026 | Robotics, Automation, and Artificial Intelligence","url":"https://www.raai.net/"},{"title":"AI Conference Deadlines","url":"https://llv22.github.io/ai-deadlines/"},{"title":"AI Conference Deadlines 2026 | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/"},{"title":"AI Conference Deadlines","url":"https://nunoduarte.github.io/deadlines/"},{"title":"Best Robotics Conferences and Events to Attend in 2026 - Clearpath Robotics","url":"https://clearpathrobotics.com/blog/2025/12/best-robotics-conferences-and-events-to-attend-in-2026/"}]

Based on the search results, here's information about robotics and AI conference deadlines for 2026 and 2027:

## Major 2026 Robotics & AI Conferences

The Conference on Robot Learning has a paper submission deadline of May 29, 2026, with the conference taking place November 9–12, 2026, in Austin, TX.

The 2026 IEEE International Conference on Robotics & Automation (ICRA) will be held June 1–5, 2026, in Vienna, Austria.

The IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) will take place September 28 – October 1, 2026, in Pittsburgh, Pennsylvania.

The RAAI 2026 conference has a submission deadline of August 1st, 2026, with notifications on September 1st, 2026, and registration due September 20th, 2026.

## Deadline Tracking Resources

A standing register at trybibby.com maintains submission deadlines across computer science, neuroscience, physics, and mathematics — ticking down in real time, through end of 2027.

ConferenceDeadlines.com allows you to track ACL, NeurIPS, CVPR, ICRA, CHI, SIGGRAPH and 40+ AI/ML/Robotics/HCI conference deadlines and venues.

The search results show various conferences throughout 2026 and some 2027 dates are confirmed, though specific 2027 deadline details appear limited at this time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46b045f2-0047-49f3-b4ee-74dd80ac262c",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "d9c41443-b8db-43d8-9962-9deb2fe5d9ad",
  "sourceToolAssistantUUID": "46b045f2-0047-49f3-b4ee-74dd80ac262c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-13T06:57:10.343Z_

Let me fetch more details on ICRA 2027 and AAAI 2027 deadlines, and also the aggregate deadline tracker pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9c41443-b8db-43d8-9962-9deb2fe5d9ad",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8dvi7sMZoPadoNS4Nn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b8958af-2eab-4f8e-a5a3-7f6e935e3010",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPSPjiNqL8Fam7q37d3qLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5309,
      "cache_read_input_tokens": 10855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5309,
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

_source line 22 · 2026-05-13T06:57:11.443Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PDS11KqTTddebN63udmeia`</summary>

```json
{
  "url": "https://2027.ieee-icra.org/contribute/",
  "prompt": "Extract the exact paper submission deadline dates for ICRA 2027, including any abstract deadlines and full paper deadlines. List all important dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b8958af-2eab-4f8e-a5a3-7f6e935e3010",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8dvi7sMZoPadoNS4Nn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19bc5828-850a-4114-8242-76e4f55ea15f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPSPjiNqL8Fam7q37d3qLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5309,
      "cache_read_input_tokens": 10855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5309,
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

_source line 23 · 2026-05-13T06:57:13.095Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ta8EnfRWeK9PV1E915eoDe`</summary>

```json
{
  "url": "https://trybibby.com/conference-deadlines",
  "prompt": "Extract all conference deadlines listed for 2026 and 2027, especially for: CoRL, AAAI, ICLR, ICRA, RSS, NeurIPS, IROS. List the exact submission deadline dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19bc5828-850a-4114-8242-76e4f55ea15f",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8dvi7sMZoPadoNS4Nn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4276c3f-bac4-486f-bcc0-a94cdb5eabe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPSPjiNqL8Fam7q37d3qLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5309,
      "cache_read_input_tokens": 10855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5309,
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

_source line 24 · 2026-05-13T06:57:14.215Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UfSenBChZJXe9Yu3iNmbdS`</summary>

```json
{
  "url": "http://aideadlines.org/conference/?id=aaai27",
  "prompt": "Extract the exact submission deadline dates for AAAI 2027 including abstract deadline, paper deadline, and conference dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4276c3f-bac4-486f-bcc0-a94cdb5eabe8",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8dvi7sMZoPadoNS4Nn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec37842d-0ff8-4a99-923a-ccf15a54bfb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPSPjiNqL8Fam7q37d3qLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5309,
      "cache_read_input_tokens": 10855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5309,
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

_source line 25 · 2026-05-13T06:57:14.745Z_

<details><summary>↩ Tool result · reported error · `toolu_01UfSenBChZJXe9Yu3iNmbdS`</summary>

```text
ECONNREFUSED
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec37842d-0ff8-4a99-923a-ccf15a54bfb3",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "3a189bd8-2719-49bf-ade6-efa2141a3996",
  "toolUseResult": "Error: ECONNREFUSED",
  "sourceToolAssistantUUID": "ec37842d-0ff8-4a99-923a-ccf15a54bfb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-13T06:57:15.165Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KDG33Gh484gfBQsDMisZmz`</summary>

```json
{
  "url": "https://neurips.cc/Conferences/2026/Dates",
  "prompt": "Extract all exact dates and deadlines for NeurIPS 2026 including abstract deadline, paper submission deadline, review dates, notification dates, and conference dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a189bd8-2719-49bf-ade6-efa2141a3996",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8dvi7sMZoPadoNS4Nn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f644e473-2d4c-4c73-95ee-57b340479bdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPSPjiNqL8Fam7q37d3qLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5309,
      "cache_read_input_tokens": 10855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5309,
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

_source line 27 · 2026-05-13T06:57:15.255Z_

<details><summary>↩ Tool result · `toolu_01PDS11KqTTddebN63udmeia`</summary>

```text
# ICRA 2027 Paper Submission Deadlines

Based on the provided content, **specific submission deadlines for ICRA 2027 are not yet available**. The webpage indicates that "ICRA 2027 Website under Construction" as of May 5, 2026.

However, the page does reference **ICRA 2025 deadlines** for reference:

- **Paper Submission:** "15 September 2024 (11:59 PST)"
- **Accompanying Videos:** August 5–September 9, 2024, and September 17–22, 2024

The site advises visitors to "Check our Media Room for the latest 'contribute' posts" and recommends using "the calendar to keep track of our deadlines" once ICRA 2027 details are finalized.

For current ICRA 2027 submission information, check the official website directly or contact the organizing committee through their contact page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19bc5828-850a-4114-8242-76e4f55ea15f",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "bfbacf30-3d86-47ff-b50b-3c3ae00ea8de",
  "sourceToolAssistantUUID": "19bc5828-850a-4114-8242-76e4f55ea15f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-13T06:57:15.959Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GETBy5hH15Vtrf4eZNnt3t`</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract all exact submission deadline dates for CoRL 2026 including abstract deadline, paper submission deadline, supplementary materials deadline, and conference dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfbacf30-3d86-47ff-b50b-3c3ae00ea8de",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8dvi7sMZoPadoNS4Nn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c773b85-60a5-40fc-a203-96a02067a9d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPSPjiNqL8Fam7q37d3qLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5309,
      "cache_read_input_tokens": 10855,
      "output_tokens": 551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5309
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 551,
          "cache_read_input_tokens": 10855,
          "cache_creation_input_tokens": 5309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5309,
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

_source line 29 · 2026-05-13T06:57:18.174Z_

<details><summary>↩ Tool result · `toolu_01Ta8EnfRWeK9PV1E915eoDe`</summary>

```text
# Conference Deadlines for 2026-2027

Based on the page content, here are the key submission deadlines:

**2026 Deadlines:**

- **CoRL 2026** (Abstract): May 26, 2026, 11:59 AM UTC
- **CoRL 2026** (Full Paper): May 29, 2026, 11:59 AM UTC
- **AAAI 2027** (Abstract): July 26, 2026, 11:59 AM UTC
- **AAAI 2027** (Full Paper): August 2, 2026, 11:59 AM UTC
- **ICLR 2027** (Abstract): September 19, 2026, 11:59 AM UTC
- **ICLR 2027** (Full Paper): September 24, 2026, 11:59 AM UTC
- **ICRA 2027**: September 16, 2026, 11:59 AM UTC

**2027 Deadlines:**

- **RSS 2027**: February 1, 2027, 11:59 AM UTC
- **NeurIPS 2027**: May 16, 2027, 11:59 AM UTC
- **IROS 2027**: March 2, 2027, 11:59 AM UTC

The page notes that "tentative entries" marked "[EST.]" are "projected from prior-year schedules where the official CFP has not yet posted," and recommends: "Always verify against the official CFP before submitting."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4276c3f-bac4-486f-bcc0-a94cdb5eabe8",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "20b7e5e1-8b4a-46e2-b9a9-310b70d8dbde",
  "sourceToolAssistantUUID": "d4276c3f-bac4-486f-bcc0-a94cdb5eabe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T06:57:18.609Z_

<details><summary>↩ Tool result · `toolu_01GETBy5hH15Vtrf4eZNnt3t`</summary>

```text
# CoRL 2026 Submission Deadlines

Based on the provided web page content, **no specific submission deadline dates are listed**. The page states: "For paper submission format and timeline, see: [Instruction for Authors](/contributions/instruction-for-authors)" but does not include the actual deadlines.

To find the abstract deadline, paper submission deadline, supplementary materials deadline, and conference dates, you would need to visit the "Instruction for Authors" page referenced in the Call for Papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c773b85-60a5-40fc-a203-96a02067a9d3",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "5fcd1105-4908-4cc3-8025-adc3e55896be",
  "sourceToolAssistantUUID": "3c773b85-60a5-40fc-a203-96a02067a9d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T06:57:19.159Z_

<details><summary>↩ Tool result · `toolu_01KDG33Gh484gfBQsDMisZmz`</summary>

```text
# NeurIPS 2026 Key Dates and Deadlines

**Conference Dates:**
"The Fortieth annual conference is held Sun. Dec 6th through Sat the 12th, 2026"

**Paper Submission:**
- Abstract deadline: May 04, 2026 (Anywhere on Earth)
- Full paper deadline: May 06, 2026 (Anywhere on Earth)

**Review Periods:**
- Author + Reviewer + AC discussion: July 27 – August 03, 2026
- Reviewer + AC discussion: August 03 – August 10, 2026

**Author Notification:**
- September 24, 2026 (Anywhere on Earth)

**Other Tracks:**
- Competitions: Submission May 15, notification June 15, 2026
- Workshops: Application opens April 20, deadline June 06, acceptance July 11, 2026
- Position Papers: Same deadlines as main conference papers

**Program Schedule:**
- Tutorials: Monday, December 7th
- Main sessions: Tuesday–Thursday, December 8–10
- Workshops: Friday–Saturday, December 11–12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f644e473-2d4c-4c73-95ee-57b340479bdb",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "cd2cee9c-4fb0-45a7-add4-79abe5a0d22c",
  "sourceToolAssistantUUID": "f644e473-2d4c-4c73-95ee-57b340479bdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-13T06:57:22.296Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018FQkoNPAbmyq2GwSGe8rRu`</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract all exact submission deadline dates for CoRL 2026 including abstract deadline, paper submission deadline, supplementary materials deadline, review timeline, notification dates, and conference dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd2cee9c-4fb0-45a7-add4-79abe5a0d22c",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8emTGw4Zz5NFYvQVcU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fa13f0d-a0b9-4301-ba77-513671441f62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YLkg7BX1m8f1TRQDHSrx6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 138,
      "cache_creation_input_tokens": 1512,
      "cache_read_input_tokens": 16164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1512,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 33 · 2026-05-13T06:57:22.449Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018YZYi32mX4HkwWqD9ALeqh`</summary>

```json
{
  "query": "AAAI 2027 abstract deadline August 2026 submission date confirmed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fa13f0d-a0b9-4301-ba77-513671441f62",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8emTGw4Zz5NFYvQVcU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad8e40a1-b73b-483b-8a3d-8934b633f6aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YLkg7BX1m8f1TRQDHSrx6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 138,
      "cache_creation_input_tokens": 1512,
      "cache_read_input_tokens": 16164,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1512
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 138,
          "output_tokens": 171,
          "cache_read_input_tokens": 16164,
          "cache_creation_input_tokens": 1512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1512,
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

_source line 34 · 2026-05-13T06:57:25.134Z_

<details><summary>↩ Tool result · `toolu_018FQkoNPAbmyq2GwSGe8rRu`</summary>

```text
# CoRL 2026 Submission Deadlines

Based on the provided content, the document mentions **only one specific deadline date**:

**Camera-Ready Paper Submission:** "Oct 12, 2026 (23:59 Anywhere on Earth)"

Additionally, there is a reference to the paper submission deadline being "Thursday (5/28) EOD" with a note that "the paper submission deadline is Thursday (5/28) EOD rather than Friday," though the full year context suggests this refers to 2026.

**Notable gaps:** The document does not explicitly state the abstract deadline, review timeline, acceptance notification dates, or official conference dates. While these sections are referenced in the table of contents ("Key Dates"), the actual specific dates are not provided in the content shown.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fa13f0d-a0b9-4301-ba77-513671441f62",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "fce07a18-f58c-4d9a-be1d-eaad8d3f3d00",
  "sourceToolAssistantUUID": "8fa13f0d-a0b9-4301-ba77-513671441f62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-13T06:57:26.030Z_

<details><summary>↩ Tool result · `toolu_018YZYi32mX4HkwWqD9ALeqh`</summary>

```text
Web search results for query: "AAAI 2027 abstract deadline August 2026 submission date confirmed"

Links: [{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"},{"title":"MPC Deadlines Hub","url":"https://mpc-deadlines.github.io/"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"The 40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"}]

Based on the search results, I found information about AAAI 2027 submission deadlines:

AAAI 2027 has a full paper deadline of August 1, 2026 (23:59) and an abstract deadline of July 25, 2026. The conference will be held January 20-27, 2027 in Montreal, Canada.

So to clarify: the abstract deadline for AAAI 2027 is **July 25, 2026**, not August 2026. The full paper submission deadline is August 1, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad8e40a1-b73b-483b-8a3d-8934b633f6aa",
  "isSidechain": true,
  "promptId": "efd6247c-bcef-4484-aa3b-8bc01b07e69d",
  "agentId": "aac89d5f08aeef3c3",
  "type": "user",
  "uuid": "f2e325ff-b748-4275-93bf-24b5a689788e",
  "sourceToolAssistantUUID": "ad8e40a1-b73b-483b-8a3d-8934b633f6aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-13T06:57:54.045Z_

Now I have a comprehensive picture. Here is the full report.

---

## Robotics / AI Conference Deadlines: 2026-2027

### 1. CoRL 2026 (Conference on Robot Learning)
- **Abstract deadline:** May 26, 2026 (11:59 UTC) -- one source also references May 28 for paper submission (Thursday EOD)
- **Paper submission deadline:** May 29, 2026 (11:59 UTC)
- **Camera-ready:** October 12, 2026 (23:59 AoE)
- **Conference:** November 9-12, 2026, Austin, Texas
- **Status:** CONFIRMED. Note: the deadline is imminent (about 2 weeks from today, May 13, 2026).

### 2. AAAI 2027
- **Abstract deadline:** ~July 25-26, 2026 (11:59 UTC)
- **Paper submission deadline:** ~August 1-2, 2026 (11:59 UTC)
- **Conference:** February 16-23, 2027, Montreal, Quebec, Canada
- **Status:** ESTIMATED. The trybibby.com deadline tracker lists abstract July 26 and paper August 2, while another source lists abstract July 25 and paper August 1. These are projected from prior-year patterns and marked as estimates. The official AAAI 2027 CFP has not yet been posted with confirmed dates. Always verify against the official CFP at aaai.org.

### 3. ICLR 2027
- **Abstract deadline:** ~September 19, 2026 (11:59 UTC)
- **Paper submission deadline:** ~September 24, 2026 (11:59 UTC)
- **Conference:** Likely April/May 2027 (venue/dates not yet announced)
- **Status:** ESTIMATED. These dates are projected from ICLR 2026's pattern (which had a September 24, 2025 deadline). No official ICLR 2027 announcement exists yet.

### 4. ICRA 2027
- **Paper submission deadline:** ~September 16, 2026 (11:59 UTC)
- **Conference:** May 24-28, 2027, Seoul, South Korea
- **Status:** ESTIMATED for the submission deadline. The conference dates and venue (Seoul) appear confirmed, but the ICRA 2027 website is still "under construction" as of May 2026. The September 16 deadline is projected from prior-year patterns. ICRA 2025 had a September 15, 2024 deadline, so mid-September is consistent.

### 5. RSS 2026 (Robotics: Science and Systems)
- **Abstract deadline:** January 23, 2026 (AoE) -- ALREADY PASSED
- **Full paper deadline:** January 30, 2026 (AoE) -- ALREADY PASSED
- **Supplementary materials:** February 6, 2026 (AoE) -- ALREADY PASSED
- **Conference:** July 13-17, 2026, Sydney, Australia
- **Status:** CONFIRMED. All submission deadlines have already passed.

**RSS 2027:**
- **Paper deadline:** ~February 1, 2027 (estimated, projected from prior years)
- **Status:** ESTIMATED. No official announcement yet.

### 6. NeurIPS 2026
- **Submission site opens:** April 15, 2026
- **Abstract deadline:** May 4, 2026 (AoE) -- ALREADY PASSED
- **Full paper deadline:** May 6, 2026 (AoE) -- ALREADY PASSED
- **Author/Reviewer/AC discussion:** July 27 - August 10, 2026
- **Author notification:** September 24, 2026 (AoE)
- **Conference:** December 6-12, 2026
- **Status:** CONFIRMED. Submission deadlines have already passed (1 week ago).

### Bonus: Other Notable Venues
- **IROS 2026:** September 28 - October 1, 2026, Pittsburgh, PA (submission deadline already passed)
- **IROS 2027:** ~March 2, 2027 (estimated submission deadline)

---

### Summary of Upcoming Actionable Deadlines

| Conference | Deadline | Date | Status |
|---|---|---|---|
| **CoRL 2026** | Abstract | May 26, 2026 | CONFIRMED -- 13 days away |
| **CoRL 2026** | Paper | May 29, 2026 | CONFIRMED -- 16 days away |
| **AAAI 2027** | Abstract | ~July 25-26, 2026 | ESTIMATED |
| **AAAI 2027** | Paper | ~Aug 1-2, 2026 | ESTIMATED |
| **ICRA 2027** | Paper | ~Sep 16, 2026 | ESTIMATED |
| **ICLR 2027** | Abstract | ~Sep 19, 2026 | ESTIMATED |
| **ICLR 2027** | Paper | ~Sep 24, 2026 | ESTIMATED |
| **RSS 2027** | Paper | ~Feb 1, 2027 | ESTIMATED |
| **NeurIPS 2027** | Paper | ~May 16, 2027 | ESTIMATED |

NeurIPS 2026 and RSS 2026 deadlines have already passed. CoRL 2026 is the most urgent upcoming deadline.

Sources:
- [CoRL 2026 Official Site](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [NeurIPS 2026 Dates and Deadlines](https://neurips.cc/Conferences/2026/Dates)
- [NeurIPS 2026 on X (deadline update)](https://x.com/NeurIPSConf/status/2041303457554940336)
- [AAAI Conference Page](https://aaai.org/conference/aaai/)
- [ICRA 2027 Official Site](https://2027.ieee-icra.org/contribute/)
- [RSS 2026 Call for Papers](https://roboticsconference.org/information/cfp/)
- [RSS 2026 OpenReview](https://openreview.net/group?id=roboticsfoundation.org%2FRSS%2F2026%2FConference)
- [AI & ML Conference Deadlines 2026-2027 (trybibby.com)](https://trybibby.com/conference-deadlines)
- [AI Deadlines (aideadlines.org)](http://aideadlines.org/)
- [WikiCFP - AAAI](http://www.wikicfp.com/cfp/program?id=3)
- [HuggingFace AI Deadlines Tracker](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32)
- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2e325ff-b748-4275-93bf-24b5a689788e",
  "isSidechain": true,
  "agentId": "aac89d5f08aeef3c3",
  "requestId": "req_011Caz8fGodBCuVzGgUbv8d5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af07ea6d-c738-4914-8247-b9b6c03b578a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ef00f600-bedf-4847-823d-d1099b32bbc3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1nX69NLmzPsgqbmvAvPkJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1171,
      "cache_read_input_tokens": 17676,
      "output_tokens": 1803,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1171
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1803,
          "cache_read_input_tokens": 17676,
          "cache_creation_input_tokens": 1171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1171,
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
