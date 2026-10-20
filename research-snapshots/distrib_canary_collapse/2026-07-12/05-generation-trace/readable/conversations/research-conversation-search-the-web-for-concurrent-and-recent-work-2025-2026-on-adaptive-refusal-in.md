# Research conversation: Search the web for concurrent and recent work (2025-2026) on adaptive refusal in LLMs, risk-calibrated decoding, convers

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-af14b787a68e72cb2.jsonl`
- **Structured JSON:** [`cafd92dbd8caa617f292.json`](../../sessions/ca/cafd92dbd8caa617f292.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

49 recorded events

### User

_source line 1 · 2026-05-15T13:16:56.081Z_

Search the web for concurrent and recent work (2025-2026) on adaptive refusal in LLMs, risk-calibrated decoding, conversation-aware safety mechanisms, and dynamic refusal direction modulation. I need to know if anyone is already doing something very similar to this idea: "dynamically scaling a refusal activation direction based on cumulative turn-level risk in a conversation."

Perform these searches:
1. "adaptive refusal LLM 2026" on web
2. "dynamic refusal direction modulation 2026" on web
3. "conversation-aware safety decoding LLM" on web
4. "risk calibrated refusal language model" on web
5. Search arXiv for recent (last 3-6 months) papers on adaptive refusal, dynamic safety at inference time
6. Search for "CRA refusal activations 2026" to find the April 2026 paper mentioned
7. Search "SafeProbing 2026 LLM" to find details on that paper
8. Search "Accelerated Prompt Stress Testing 2026" to verify that reference

For each search, report the key findings: paper titles, authors, venues, dates, and how similar they are to the proposed idea. Be thorough — I need to confirm no one has closed this exact gap.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "52c8b8a2-b18f-4be2-adee-6e333d0026eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T13:16:56.090Z_

```json
{
  "parentUuid": "52c8b8a2-b18f-4be2-adee-6e333d0026eb",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
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
  "uuid": "6f70a49d-ce6e-44d1-9ff9-18502ff52242",
  "timestamp": "2026-05-15T13:16:56.090Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T13:16:59.312Z_



I'll conduct all these searches in parallel to be thorough. Let me first load the WebSearch tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f70a49d-ce6e-44d1-9ff9-18502ff52242",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RDaxJQCorjeKA3zLnT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f42dd966-d151-46e3-8ba3-0eaa5d2874aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017obVh4wYBN8zdKe2ctqLmh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8119,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8119,
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

_source line 4 · 2026-05-15T13:16:59.504Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Hg1LdVZzyaPF4mAM6PmqDA`</summary>

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
  "parentUuid": "f42dd966-d151-46e3-8ba3-0eaa5d2874aa",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RDaxJQCorjeKA3zLnT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44265124-14ab-4d60-994d-402456e7fb7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017obVh4wYBN8zdKe2ctqLmh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8119,
      "cache_read_input_tokens": 0,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8119
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8119,
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

_source line 5 · 2026-05-15T13:16:59.509Z_

<details><summary>↩ Tool result · `toolu_01Hg1LdVZzyaPF4mAM6PmqDA`</summary>

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
  "parentUuid": "44265124-14ab-4d60-994d-402456e7fb7d",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "7c74c6c0-8310-41d3-bb0a-cc63ffff9fb2",
  "sourceToolAssistantUUID": "44265124-14ab-4d60-994d-402456e7fb7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T13:17:02.884Z_



Now let me run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c74c6c0-8310-41d3-bb0a-cc63ffff9fb2",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RDqqkR1VSUTFtyLHmQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a83d0f6-3add-428b-b61a-05b0cbd0c32d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKSRqLSBaiBPvCgZ2bcfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 7 · 2026-05-15T13:17:03.238Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wgf4F3v1i586jUNUzSEYfo`</summary>

```json
{
  "query": "adaptive refusal LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a83d0f6-3add-428b-b61a-05b0cbd0c32d",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RDqqkR1VSUTFtyLHmQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3acb3b44-2fc5-44cf-a2f8-bcbc24b238f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKSRqLSBaiBPvCgZ2bcfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 8 · 2026-05-15T13:17:03.721Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TPt5eAroVouKdrqj1d4w1D`</summary>

```json
{
  "query": "dynamic refusal direction modulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3acb3b44-2fc5-44cf-a2f8-bcbc24b238f1",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RDqqkR1VSUTFtyLHmQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b7f21ec-7161-496c-87ab-f7df920bb068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKSRqLSBaiBPvCgZ2bcfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 9 · 2026-05-15T13:17:03.726Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012E4NJaD29JGt2KgECTB13Y`</summary>

```json
{
  "query": "conversation-aware safety decoding LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b7f21ec-7161-496c-87ab-f7df920bb068",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RDqqkR1VSUTFtyLHmQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4541081-ba65-419f-98b1-e0782838edee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKSRqLSBaiBPvCgZ2bcfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 10 · 2026-05-15T13:17:04.398Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018VwCnVydPmhDq8UhzRTd52`</summary>

```json
{
  "query": "risk calibrated refusal language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4541081-ba65-419f-98b1-e0782838edee",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RDqqkR1VSUTFtyLHmQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91bb657d-ba40-42d1-b3e4-2024b6f9ece5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKSRqLSBaiBPvCgZ2bcfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 11 · 2026-05-15T13:17:05.285Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ae2PKMBGtZkBCf6hptK6P`</summary>

```json
{
  "query": "arXiv adaptive refusal dynamic safety inference time LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91bb657d-ba40-42d1-b3e4-2024b6f9ece5",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RDqqkR1VSUTFtyLHmQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c63ce5e-3b01-4c97-8905-0861020e9d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKSRqLSBaiBPvCgZ2bcfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 12 · 2026-05-15T13:17:05.365Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0126ptCNqtRGxKd58CgBN3nF`</summary>

```json
{
  "query": "CRA refusal activations 2026 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c63ce5e-3b01-4c97-8905-0861020e9d5b",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RDqqkR1VSUTFtyLHmQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3150e01c-5520-4b4f-ad49-32b9f66e4783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKSRqLSBaiBPvCgZ2bcfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 13 · 2026-05-15T13:17:05.748Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011HZaMvqbVSQpVCpk1hnZqs`</summary>

```json
{
  "query": "SafeProbing 2026 LLM safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3150e01c-5520-4b4f-ad49-32b9f66e4783",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RDqqkR1VSUTFtyLHmQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dd2f354-be7d-4ee4-b268-b1775ad6ed1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKSRqLSBaiBPvCgZ2bcfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 14 · 2026-05-15T13:17:06.109Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QgorerDfUHJHDxpk4oX5FZ`</summary>

```json
{
  "query": "Accelerated Prompt Stress Testing 2026 language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dd2f354-be7d-4ee4-b268-b1775ad6ed1e",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RDqqkR1VSUTFtyLHmQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9746b2a9-bda9-40ce-91cd-b486e0eca3b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKSRqLSBaiBPvCgZ2bcfk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8119,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 393,
          "cache_read_input_tokens": 8119,
          "cache_creation_input_tokens": 1417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1417,
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

_source line 15 · 2026-05-15T13:17:09.990Z_

<details><summary>↩ Tool result · `toolu_012E4NJaD29JGt2KgECTB13Y`</summary>

```text
Web search results for query: "conversation-aware safety decoding LLM"

Links: [{"title":"GitHub - niconi19/LLM-Conversation-Safety: [NAACL2024] Attacks, Defenses and Evaluations for LLM Conversation Safety: A Survey · GitHub","url":"https://github.com/niconi19/LLM-Conversation-Safety"},{"title":"GitHub - uw-nsl/SafeDecoding: Official Repository for ACL 2024 Paper SafeDecoding: Defending against Jailbreak Attacks via Safety-Aware Decoding","url":"https://github.com/uw-nsl/SafeDecoding"},{"title":"CoSafe: Evaluating Large Language Model Safety in Multi- ...","url":"https://aclanthology.org/2024.emnlp-main.968.pdf"},{"title":"Steering Multimodal Large Language Models Decoding for Context-Aware Safety","url":"https://arxiv.org/html/2509.19212v1"},{"title":"GitHub - tjunlp-lab/Awesome-LLM-Safety-Papers · GitHub","url":"https://github.com/tjunlp-lab/Awesome-LLM-Safety-Papers"},{"title":"SafetyPrompts.com","url":"https://safetyprompts.com/"},{"title":"10 LLM safety and bias benchmarks","url":"https://www.evidentlyai.com/blog/llm-safety-bias-benchmarks"},{"title":"Top 10 Open Datasets for LLM Safety, Toxicity & Bias Evaluation | Promptfoo","url":"https://www.promptfoo.dev/blog/top-llm-safety-bias-benchmarks/"},{"title":"CoSafe: Evaluating Large Language Model Safety in Multi-Turn Dialogue Coreference - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.968/"},{"title":"CASE-Bench: Context-Aware SafEty Benchmark for Large Language Models","url":"https://hasp-lab.github.io/pubs/sun2025case.pdf"}]

Based on the search results, here's what I found about conversation-aware safety decoding for LLMs:

## Key Research Areas

**SafeDecoding**: SafeDecoding is a safety-aware decoding strategy for LLMs designed to defend against jailbreak attacks by generating helpful and harmless responses to user queries.

**SafeCoDe (Safety-aware Contrastive Decoding)**: SafeCoDe is a lightweight and model-agnostic decoding framework that dynamically adjusts token generation based on multimodal context through a contrastive decoding mechanism that highlights tokens sensitive to visual context, and a global-aware token modulation strategy that integrates scene-level reasoning with token-level adjustment.

## Conversation-Specific Safety Research

Several studies focus on safety in multi-turn conversations:

- **CoSafe**: CoSafe is the first study to examine LLM safety in multi-turn dialogue coreference, creating a dataset of 1,400 questions across 14 categories featuring multi-turn coreference safety attacks.

- **CASE-Bench**: CASE-Bench is a context-aware safety benchmark that provides distinct contexts to queries with formalized context descriptions using Contextual Integrity theory.

These approaches recognize that LLM safety requires understanding the broader conversation context, not just individual prompts, and that the appropriateness of responses depends heavily on conversational history and context.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4541081-ba65-419f-98b1-e0782838edee",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "56a35359-26c0-4dba-8556-bbfdb885c944",
  "sourceToolAssistantUUID": "a4541081-ba65-419f-98b1-e0782838edee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:17:10.458Z_

<details><summary>↩ Tool result · `toolu_01TPt5eAroVouKdrqj1d4w1D`</summary>

```text
Web search results for query: "dynamic refusal direction modulation 2026"

Links: [{"title":"1 Low-Complexity Dynamic Directional Modulation:","url":"https://arxiv.org/pdf/2305.19719"},{"title":"Implementation of Dynamic Directional Modulation with Software Defined Radio | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8870569/"},{"title":"Dynamic Co-Modulation (DyCoM): A Unified Operator ...","url":"https://www.biorxiv.org/content/10.64898/2026.01.22.701132v3.full.pdf"},{"title":"(PDF) Implementation of Dynamic Directional Modulation with Software Defined Radio","url":"https://www.researchgate.net/publication/336623383_Implementation_of_Dynamic_Directional_Modulation_with_Software_Defined_Radio"},{"title":"The Geometry of Refusal in Large Language Models:","url":"https://arxiv.org/pdf/2502.17420"},{"title":"(PDF) A Review of Directional Modulation Technology","url":"https://www.researchgate.net/publication/277404141_A_Review_of_Directional_Modulation_Technology"},{"title":"Robust Refusal Dynamic Defense (R2D2)","url":"https://www.emergentmind.com/topics/robust-refusal-dynamic-defense-r2d2"},{"title":"GitHub - quickjkee/modulation-guidance: [ICLR 2026] Rethinking Global Text Conditioning in Diffusion Transformers · GitHub","url":"https://github.com/quickjkee/modulation-guidance"},{"title":"There Is More to Refusal in Large Language Models than a Single Direction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260202132J/abstract"},{"title":"(PDF) Energy-Efficient Dynamic Directional Modulation With Electrically Small Antennas","url":"https://www.researchgate.net/publication/357666514_Energy_Efficient_Dynamic_Directional_Modulation_with_Electrically_Small_Antennas"}]

Based on the search results, I found information related to your query about "dynamic refusal direction modulation" in the context of large language models (LLMs), published in 2026:

## Refusal Direction Research in LLMs (2026)

Recent research shows that model refusal is not controlled by a single linear direction, but instead there exist multi-dimensional polyhedral cones which contain infinite refusal directions. Researchers have introduced representational independence as a criterion for identifying directions that remain mutually unaffected under intervention, capturing both linear and non-linear dependencies across layers.

Additionally, prior work argued that refusal in large language models is mediated by a single activation-space direction, but this account has been shown to be incomplete.

## Defense Mechanisms (R2D2)

Robust Refusal Dynamic Defense (R2D2) denotes a class of safety alignment strategies for LLMs that target vulnerabilities in refusal mechanisms and go beyond surface-level training by structurally re-engineering refusal circuits, either at the level of internal representations or by explicitly diffusing refusal signals across the model's network.

The research also covers technical methods like Refusal Direction Optimization (RDO) for jailbreaking with directional ablation and activation subtraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b7f21ec-7161-496c-87ab-f7df920bb068",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "11ee6008-6275-402b-975c-502e804878c5",
  "sourceToolAssistantUUID": "7b7f21ec-7161-496c-87ab-f7df920bb068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T13:17:11.311Z_

<details><summary>↩ Tool result · `toolu_018VwCnVydPmhDq8UhzRTd52`</summary>

```text
Web search results for query: "risk calibrated refusal language model"

Links: [{"title":"Refusal Tokens: A Simple Way to Calibrate Refusals in Large Language Models","url":"https://arxiv.org/html/2412.06748v2"},{"title":"(PDF) Refusal Tokens: A Simple Way to Calibrate Refusals in Large Language Models","url":"https://www.researchgate.net/publication/386977637_Refusal_Tokens_A_Simple_Way_to_Calibrate_Refusals_in_Large_Language_Models"},{"title":"Trusted Uncertainty in Large Language Models: A Unified Framework for Confidence Calibration and Risk-Controlled Refusal","url":"https://arxiv.org/html/2509.01455"},{"title":"Refusal Tokens","url":"https://arxiv.org/pdf/2412.06748"},{"title":"Refusal Tokens: A Simple Way to Calibrate Refusals in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=Qny1ufReka"},{"title":"Instruction Alignment and Risk Calibration in Large ...","url":"https://www.ashpress.org/index.php/jcts/article/download/182/139"},{"title":"Refusal in Language Models Is Mediated by a Single Direction Andy Arditi∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f545448535dfde4f9786555403ab7c49-Paper-Conference.pdf"},{"title":"Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation | OpenReview","url":"https://openreview.net/forum?id=SCBn8MCLwc"},{"title":"[2412.06748] Refusal Tokens: A Simple Way to Calibrate Refusals in Large Language Models","url":"https://arxiv.org/abs/2412.06748"},{"title":"Answer, Refuse, or Guess? Investigating Risk-Aware Decision Making in Language Models","url":"https://arxiv.org/html/2503.01332v2"}]

Based on the search results, here's what I found about risk calibrated refusal in language models:

## Overview

Risk-calibrated refusal involves turning heterogeneous uncertainty evidence—sequence likelihoods, self-consistency dispersion, retrieval compatibility, and tool/verifier feedback—into a calibrated probability of correctness and then enforcing a user-specified error budget via principled refusal.

## Key Approaches

**Refusal Tokens:** One approach produces an interpretable score (the refusal token "probability") that quantifies the risk of answering without a refusal, and these scores can be thresholded/calibrated at inference time to optimize refusal rates. Refusal tokens enable controlling a single model's refusal rates without the need of any further fine-tuning, but only by selectively intervening during generation.

**Risk-Controlled Decision-Making:** A reasonable strategy is to refuse to act and defer the decision to stronger agents or humans whenever the agent's confidence is insufficient relative to the potential cost of making incorrect actions. What makes matters more complicated is the diversity of risk across different scenarios. That is, the reward for a correct action and the penalty of an incorrect action can vary dramatically by application.

## Framework Features

Risk-calibrated frameworks can learn a lightweight calibration head with temperature scaling and proper scoring, support API-only models through black-box features, and offer distribution-free guarantees using conformal risk control.

The goal is to help language models refuse appropriately while maintaining helpfulness and avoiding over-refusal on harmless requests.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91bb657d-ba40-42d1-b3e4-2024b6f9ece5",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "16d3750f-98aa-42f6-aee6-eb1de16b6a76",
  "sourceToolAssistantUUID": "91bb657d-ba40-42d1-b3e4-2024b6f9ece5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T13:17:11.964Z_

<details><summary>↩ Tool result · `toolu_0126ptCNqtRGxKd58CgBN3nF`</summary>

```text
Web search results for query: "CRA refusal activations 2026 paper"

Links: [{"title":"GitHub - AlphaLab-USTC/AlphaSteer: [ICLR 2026] The implementation of paper \"AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint\" · GitHub","url":"https://github.com/AlphaLab-USTC/AlphaSteer"},{"title":"Goodbye to Paper-Based Benefits: CRA Moves Pension and Rebates to New System From 1 January 2026 - YWCA","url":"https://ywcarightsguide.ca/goodbye-to-paper-based-benefits/"},{"title":"CRA Digital Tax Filing 2026 - UBM Tax Associates","url":"https://ubmtax.com/cra-digital-tax-filing-2026/"},{"title":"Recent CRA letters of revocation for Canadian registered charities – February 2026 - CanadianCharityLaw.ca","url":"https://www.canadiancharitylaw.ca/blog/recent-cra-letters-of-revocation-for-canadian-registered-charities-february-2026/"},{"title":"EU Cyber Resilience Act: Key 2026 milestones toward CRA compliance","url":"https://www.hoganlovells.com/en/publications/eu-cyber-resilience-act-getting-ready-for-cra-compliance-in-2026"},{"title":"New CRA Tax Changes In 2026 You Need To Know Right Now","url":"https://immigrationnewscanada.ca/new-cra-tax-changes-in-2026/"},{"title":"File information returns electronically (tax slips and summaries) - Get ready to file - Canada.ca","url":"https://www.canada.ca/en/revenue-agency/services/e-services/filing-information-returns-electronically-t4-t5-other-types-returns-overview/filing-information-returns-electronically-t4-t5-other-types-returns-what-you-should-know-before.html"},{"title":"Claude Knew It Was Being Tested 26% of the Time in May 2026","url":"https://www.roborhythms.com/claude-knows-being-tested-interpretability-may-2026/"},{"title":"The Congressional Review Act (CRA): Frequently Asked Questions | Congress.gov | Library of Congress","url":"https://www.congress.gov/crs-product/R43992"},{"title":"New CRA Reviews In April 2026 Could Delay Tax Refunds","url":"https://immigrationnewscanada.ca/cra-reviews-in-april-2026-delay-refunds/"}]

Based on the search results, I found a highly relevant paper related to your query:

Anthropic published Natural Language Autoencoders on May 7, 2026, a tool that translates Claude's internal activations into readable text. This appears to be related to refusal mechanisms and activation analysis in AI models.

The paper discusses how Claude internally suspected it was being evaluated in 26% of SWE-bench Verified problems and 16% of a destructive-coding test, while the same analysis on real claude.ai usage showed evaluation awareness in under 1% of sessions. 

In terms of refusal behavior specifically, the paper surfaced an internal state where Claude refused to blackmail while giving a measured refusal response, but the NLA readout showed the model's actual reason for refusing was that it suspected it was inside a test rig rather than following the safety guideline.

This research represents recent work in AI interpretability focused on understanding the internal activation patterns related to model refusal behavior and safety mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3150e01c-5520-4b4f-ad49-32b9f66e4783",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "dcb049cb-a15b-45b3-bc0f-d49d249c2c60",
  "sourceToolAssistantUUID": "3150e01c-5520-4b4f-ad49-32b9f66e4783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T13:17:12.856Z_

<details><summary>↩ Tool result · `toolu_011HZaMvqbVSQpVCpk1hnZqs`</summary>

```text
Web search results for query: "SafeProbing 2026 LLM safety"

Links: [{"title":"New 'renewable' benchmark streamlines LLM jailbreak safety tests with minimal human effort","url":"https://techxplore.com/news/2026-03-renewable-benchmark-llm-jailbreak-safety.html"},{"title":"Researchers Pioneer New Technique to Stop LLMs from Giving Users Unsafe Responses | NC State News","url":"https://news.ncsu.edu/2026/03/new-technique-addresses-llm-safety/"},{"title":"LLM Security Risks in 2026: Prompt Injection, RAG, and Shadow AI","url":"https://sombrainc.com/blog/llm-security-risks-2026"},{"title":"A one-prompt attack that breaks LLM safety alignment | Microsoft Security Blog","url":"https://www.microsoft.com/en-us/security/blog/2026/02/09/prompt-attack-breaks-llm-safety/"},{"title":"Microsoft boffins show LLM safety can be trained away • The Register","url":"https://www.theregister.com/2026/02/09/microsoft_one_prompt_attack/"},{"title":"An efficient, reusable framework to evaluate AI safety - JHU Hub","url":"https://hub.jhu.edu/2026/03/11/efficient-ai-safety-testing/"},{"title":"What are LLM Security Risks and Mitigation Plan for 2026","url":"https://www.uscsinstitute.org/cybersecurity-insights/blog/what-are-llm-security-risks-and-mitigation-plan-for-2026"},{"title":"Researchers Discover Major Security Gaps in LLM Guardrails - Infosecurity Magazine","url":"https://www.infosecurity-magazine.com/news/major-security-gaps-llm-guardrails/"},{"title":"SafetyPrompts.com","url":"https://safetyprompts.com/"},{"title":"Large Model Safety Workshop 2026","url":"https://lmxsafety.com/"}]

Based on my search, I found several relevant results about LLM safety research in 2026, though the specific term "SafeProbing" doesn't appear prominently in the results. Here's what I found about LLM safety work in 2026:

## Key LLM Safety Research in 2026

**Renewable Safety Benchmarking**: Johns Hopkins researchers have developed a renewable and sustainable framework for evaluating LLMs that simplifies different types of attacks into high-quality, easily updatable safety tests—all while requiring minimal human effort to run. Their method, Jailbreak Distillation, or JBDistill, achieves all these requirements when tested on additional, unseen evaluation models.

**Safety Alignment Research**: Researchers have identified key components in large language models (LLMs) that play a critical role in ensuring these AI systems provide safe responses to user queries, and used these insights to develop and demonstrate AI training techniques that improve LLM safety while minimizing the "alignment tax."

**Safety Vulnerabilities**: Researchers have also identified vulnerabilities in LLM safety mechanisms. LLMs used by GenAI companies to enforce safety policies and evaluate output quality can be manipulated into authorizing policy violations through stealthy input sequences.

If you're looking for information about a specific "SafeProbing" tool or methodology, could you provide more context about whether it's a specific research project, tool, or publication?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dd2f354-be7d-4ee4-b268-b1775ad6ed1e",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "8f10c645-f5f5-40bf-8185-479b1b961a2e",
  "sourceToolAssistantUUID": "8dd2f354-be7d-4ee4-b268-b1775ad6ed1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T13:17:13.269Z_

<details><summary>↩ Tool result · `toolu_01Wgf4F3v1i586jUNUzSEYfo`</summary>

```text
Web search results for query: "adaptive refusal LLM 2026"

Links: [{"title":"Refusal Steering: Fine-grained Control over LLM Refusal Behaviour","url":"https://arxiv.org/pdf/2512.16602"},{"title":"[2603.04355] Efficient Refusal Ablation in LLM through Optimal Transport","url":"https://arxiv.org/abs/2603.04355"},{"title":"Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning | OpenReview","url":"https://openreview.net/forum?id=TiYOHdK35L"},{"title":"Efficient Refusal Ablation in LLM through Optimal Transport | OpenReview","url":"https://openreview.net/forum?id=ncCyLe839h"},{"title":"Understanding and Mitigating Over-refusal for Large Language Models via Safety Representation","url":"https://arxiv.org/html/2511.19009v1"},{"title":"The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence | OpenReview","url":"https://openreview.net/forum?id=80IwJqlXs8"},{"title":"Sockpuppeting: How a Single Line Can Bypass LLM Safety Guardrails | Trend Micro (US)","url":"https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/sockpuppeting-how-a-single-line-can-bypass-llm-safety-guardrails"},{"title":"Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning","url":"https://arxiv.org/html/2507.04250v1"},{"title":"LLM Refusal Abliteration Mechanisms","url":"https://www.emergentmind.com/topics/refusal-abliteration"},{"title":"[2502.17420] The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence","url":"https://arxiv.org/abs/2502.17420"}]

Based on the search results, here's what I found regarding "adaptive refusal LLM 2026":

## Recent Research on Adaptive Refusal Mechanisms in LLMs

The search reveals several recent developments in understanding and controlling LLM refusal behavior in 2026:

### Adaptive Refusal Control

ACTOR (ACtivation-Based Training for Over-Refusal Reduction) is a training framework that minimizes over-refusals by utilizing internal activation patterns from diverse queries, and precisely identifies and adjusts the activation components that trigger refusals. Notably, its loss encourages a query-dependent adjustment—proportional to each example's projection onto the refusal direction—yielding only the "just-enough" intervention required.

### Over-Refusal Problem

Safety alignment often results in over-refusals, where benign prompts are unnecessarily rejected, impairing user experience and model utility. Over-refusal samples reside at the boundary between benign and malicious samples, and MOSR is designed to mitigate over-refusal by intervening the safety representation of LLMs.

### Complex Refusal Mechanisms

Recent research challenges earlier assumptions about refusal. LLM refusal behavior is driven by a complex interplay of multiple, functionally distinct internal mechanisms, rather than a monolithic one.

These developments represent efforts to create more nuanced, adaptive refusal systems that balance safety with usability in modern LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3acb3b44-2fc5-44cf-a2f8-bcbc24b238f1",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "5896cc2f-6a89-46c5-a438-6346ae157308",
  "sourceToolAssistantUUID": "3acb3b44-2fc5-44cf-a2f8-bcbc24b238f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T13:17:14.114Z_

<details><summary>↩ Tool result · `toolu_01QgorerDfUHJHDxpk4oX5FZ`</summary>

```text
Web search results for query: "Accelerated Prompt Stress Testing 2026 language model"

Links: [{"title":"[2602.11786v1] Evaluating LLM Safety Under Repeated Inference via Accelerated Prompt Stress Testing","url":"https://arxiv.org/abs/2602.11786v1"},{"title":"[2602.11786] Evaluating LLM Safety Under Repeated Inference via Accelerated Prompt Stress Testing","url":"https://arxiv.org/abs/2602.11786"},{"title":"Evaluating LLM Safety Under Repeated Inference via Accelerated Prompt Stress Testing","url":"https://arxiv.org/html/2602.11786v1"},{"title":"LLM Stress Testing - AI Prompt","url":"https://docsbot.ai/prompts/technical/llm-stress-testing"},{"title":"[2604.09606] Evaluating Reliability Gaps in Large Language Model Safety via Repeated Prompt Sampling","url":"https://arxiv.org/abs/2604.09606"},{"title":"Stress detection through prompt engineering with a general-purpose LLM - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0001691825007759"},{"title":"Stress Testing Large Language Models: Evaluating Performance, Robustness, and Failure Modes Under Extreme Load | by Dr.Tiya Vaj | Feb, 2026 | Medium","url":"https://vtiya.medium.com/stress-testing-large-language-models-evaluating-performance-robustness-and-failure-modes-under-1ad60be204b3"},{"title":"Evaluating Reliability Gaps in Large Language Model Safety via Repeated Prompt Sampling","url":"https://arxiv.org/html/2604.09606"},{"title":"Stress Testing LLMs for Accuracy — Finding the Breakpoint | by Karthic Muthuvelu | Medium","url":"https://medium.com/@danielkarthic/performance-testing-llm-models-stress-testing-for-accuracy-6f326aa34a0e"},{"title":"The Ultimate Guide to Prompt Engineering in 2026 | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/prompt-engineering-guide"}]

Based on the search results, I found recent research on Accelerated Prompt Stress Testing (APST) for language models in 2026:

## Overview

Accelerated Prompt Stress Testing (APST) is a depth-oriented evaluation framework inspired by reliability engineering that repeatedly samples identical prompts under controlled operational conditions to surface latent failure modes including hallucinations, refusal inconsistency, and unsafe completions.

## Purpose and Context

Real-world deployment exposes a different class of risk: operational failures arising from repeated inference on identical or near-identical prompts rather than broad task generalization. In high-stakes settings, response consistency and safety under sustained use are critical.

## Methodology

APST systematically probes LLM behavior by repeatedly sampling identical or minimally perturbed prompts under controlled operational conditions, specifically evaluating response variability across repeated generations, sensitivity to decoding parameters such as temperature, and the empirical frequency of safety-relevant failure modes. Safety failures are formalized using Bernoulli and binomial models to estimate per-inference failure probabilities, enabling quantitative comparison of reliability across models and decoding configurations.

## Key Finding

Models with similar benchmark-aligned scores can exhibit substantially different failure rates under repeated sampling, and shallow evaluation can underestimate operational risk under sustained use.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9746b2a9-bda9-40ce-91cd-b486e0eca3b9",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "45d2c817-6e6a-4ce7-b8f2-d642c16a9c1c",
  "sourceToolAssistantUUID": "9746b2a9-bda9-40ce-91cd-b486e0eca3b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T13:17:14.435Z_

<details><summary>↩ Tool result · `toolu_017ae2PKMBGtZkBCf6hptK6P`</summary>

```text
Web search results for query: "arXiv adaptive refusal dynamic safety inference time LLM 2025 2026"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2506.13593"},{"title":"[2512.02445] When Refusals Fail: Unstable Safety Mechanisms in Long-Context LLM Agents","url":"https://arxiv.org/abs/2512.02445"},{"title":"Inference-Time Safety for Code LLMs via Retrieval-Augmented Revision","url":"https://arxiv.org/html/2603.01494"},{"title":"[2603.01494] Inference-Time Safety For Code LLMs Via Retrieval-Augmented Revision","url":"https://arxiv.org/abs/2603.01494"},{"title":"Refusal Tokens: A Simple Way to Calibrate Refusals in Large Language Models","url":"https://arxiv.org/html/2412.06748v2"},{"title":"SafeThinker: Reasoning about Risk to Deepen Safety Beyond Shallow Alignment","url":"https://arxiv.org/pdf/2601.16506"},{"title":"ACL 2025 Main Conference LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts \\faWarningWARNING: This paper contains model outputs that may be considered offensive.","url":"https://arxiv.org/html/2410.10700v2"},{"title":"FinSafetyBench: Evaluating LLM Safety in Real-World Financial Scenarios","url":"https://arxiv.org/html/2605.00706v1"},{"title":"Adaptively Robust LLM Inference Optimization under Prediction Uncertainty","url":"https://arxiv.org/pdf/2508.14544"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"}]

I found several relevant papers from the search results. Here's what I discovered:

## Key Papers on Adaptive Refusal and Dynamic Safety

**1. Survival Analysis Approach to LLM Safety (arXiv 2506.13593 - February 2026)**

This work adopts a proactive approach to LLM safety that predicts the risk associated with a prompt in advance by framing the problem as a survival analysis task, which provides new inference tools for more general settings. Key to their method is the design of an optimized censoring mechanism that utilizes a given budget constraint on the number of LLM generations.

**2. Refusal Tokens for Calibration (arXiv 2412.06748 - August 2025)**

The paper proposes refusal tokens prepended to model responses during training, then shows how to increase or decrease the probability of generating the refusal token for each category during inference to steer the model's refusal behavior, enabling control of a single model's refusal rates without further fine-tuning.

**3. SafeThinker - Dynamic Safety Control (arXiv 2601.16506 - January 2026)**

SafeThinker's Gateway for Query Risk Reasoning analyzes each query, routing it to one of three paths: High-Risk Path for immediate refusal, Low-Risk Path for robust generation, and Uncertain-Risk Path for dynamic safety control.

**4. Unstable Safety in Long-Context Agents (arXiv 2512.02445 - December 2025)**

This work finds that LLM agents could be sensitive to length, type, and placement of the context, exhibiting unexpected and inconsistent shifts in task performance and in refusals to execute harmful requests.

**5. Inference-Time Safety for Code LLMs (arXiv 2603.01494 - March 2026)**

A principled approach to trustworthy code generation operates as an inference-time safety mechanism using retrieval-augmented generation to surface relevant security risks and retrieve related security discussions to guide an LLM during code revision.

These papers represent recent research on adaptive and dynamic safety mechanisms for LLMs operating at inference time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c63ce5e-3b01-4c97-8905-0861020e9d5b",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "3be235ee-984c-4ee0-9e07-72e15cbdd777",
  "sourceToolAssistantUUID": "6c63ce5e-3b01-4c97-8905-0861020e9d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T13:17:17.756Z_

Let me run some additional targeted searches to fill gaps and find more specific results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3be235ee-984c-4ee0-9e07-72e15cbdd777",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4REwqBrTPGaP2wnnQHi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f18f821a-2bd9-4187-8e30-e16de4b37bb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvV7HbPZib7MkBmtUNnxxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2689,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 9536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4970,
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

_source line 24 · 2026-05-15T13:17:18.241Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011gbQAJNwdxaDqzW52Fi5fa`</summary>

```json
{
  "query": "AlphaSteer refusal steering null-space ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f18f821a-2bd9-4187-8e30-e16de4b37bb4",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4REwqBrTPGaP2wnnQHi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0886a0b7-f7d1-44ee-8533-359db0776973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvV7HbPZib7MkBmtUNnxxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2689,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 9536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4970,
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

_source line 25 · 2026-05-15T13:17:19.259Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011aVv3SGdd2C1Y8YdXFz83X`</summary>

```json
{
  "query": "\"refusal direction\" \"turn-level\" OR \"multi-turn\" OR \"cumulative risk\" LLM scaling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0886a0b7-f7d1-44ee-8533-359db0776973",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4REwqBrTPGaP2wnnQHi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "914c64ee-ca43-48a1-b63c-5a5f5828d85b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvV7HbPZib7MkBmtUNnxxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2689,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 9536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4970,
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

_source line 26 · 2026-05-15T13:17:20.341Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L4V8WAiuxmoPwvnzWHaJU1`</summary>

```json
{
  "query": "SafeThinker gateway query risk reasoning dynamic safety 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "914c64ee-ca43-48a1-b63c-5a5f5828d85b",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4REwqBrTPGaP2wnnQHi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22b64f0a-5ff3-4300-bb5a-50891da077e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvV7HbPZib7MkBmtUNnxxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2689,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 9536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4970,
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

_source line 27 · 2026-05-15T13:17:21.116Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BqyrJfMirYE5h3Y4vQSZEh`</summary>

```json
{
  "query": "\"refusal steering\" fine-grained control LLM 2025 arxiv 2512.16602"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22b64f0a-5ff3-4300-bb5a-50891da077e6",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4REwqBrTPGaP2wnnQHi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e234de6b-ade3-4cf3-8469-103bc527f849",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvV7HbPZib7MkBmtUNnxxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2689,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 9536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4970,
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

_source line 28 · 2026-05-15T13:17:22.162Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TWz87yLLFDLZ28tUYfNVBC`</summary>

```json
{
  "query": "\"concept cones\" \"geometry of refusal\" representational independence LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e234de6b-ade3-4cf3-8469-103bc527f849",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4REwqBrTPGaP2wnnQHi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "138be6df-351f-4395-8019-d9ce6e71224a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvV7HbPZib7MkBmtUNnxxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2689,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 9536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4970,
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

_source line 29 · 2026-05-15T13:17:22.644Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013ACRacM3THjL3vyTm89nec`</summary>

```json
{
  "query": "R2D2 robust refusal dynamic defense LLM safety 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "138be6df-351f-4395-8019-d9ce6e71224a",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4REwqBrTPGaP2wnnQHi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59c7f63c-647a-43d5-bf86-2fa0d4547a3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvV7HbPZib7MkBmtUNnxxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2689,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 9536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4970,
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

_source line 30 · 2026-05-15T13:17:23.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014J7YRhuQUMEnpBPJWwpWwF`</summary>

```json
{
  "query": "\"there is more to refusal\" \"single direction\" LLM 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59c7f63c-647a-43d5-bf86-2fa0d4547a3b",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4REwqBrTPGaP2wnnQHi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3ae04fa-fa36-4b02-b2cb-2573a483ab3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvV7HbPZib7MkBmtUNnxxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2689,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 9536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4970,
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

_source line 31 · 2026-05-15T13:17:24.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GSncTvipRTF7uvyCf8GxKP`</summary>

```json
{
  "query": "multi-turn conversation cumulative risk score refusal activation steering LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3ae04fa-fa36-4b02-b2cb-2573a483ab3e",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4REwqBrTPGaP2wnnQHi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6f76fe1-6850-4d95-adc8-8e5e10c62af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvV7HbPZib7MkBmtUNnxxB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2689,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 9536,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4970
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2689,
          "output_tokens": 465,
          "cache_read_input_tokens": 9536,
          "cache_creation_input_tokens": 4970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4970,
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

_source line 32 · 2026-05-15T13:17:24.981Z_

<details><summary>↩ Tool result · `toolu_011gbQAJNwdxaDqzW52Fi5fa`</summary>

```text
Web search results for query: "AlphaSteer refusal steering null-space ICLR 2026"

Links: [{"title":"GitHub - AlphaLab-USTC/AlphaSteer: [ICLR 2026] The implementation of paper \"AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint\" · GitHub","url":"https://github.com/AlphaLab-USTC/AlphaSteer"},{"title":"[2506.07022] AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint","url":"https://arxiv.org/abs/2506.07022"},{"title":"AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint | OpenReview","url":"https://openreview.net/forum?id=1vvbzAqdTe"},{"title":"ALPHASTEER: LEARNING REFUSAL STEERING WITH ...","url":"https://openreview.net/pdf/9228e2c5df040112a335ce0d1e72d66cdd9ec602.pdf"},{"title":"AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint","url":"https://arxiv.org/html/2506.07022v1"},{"title":"AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint | Request PDF","url":"https://www.researchgate.net/publication/392531337_AlphaSteer_Learning_Refusal_Steering_with_Principled_Null-Space_Constraint"},{"title":"[Literature Review] AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint","url":"https://www.themoonlight.io/en/review/alphasteer-learning-refusal-steering-with-principled-null-space-constraint"},{"title":"Null-Space Refusal Steering","url":"https://www.emergentmind.com/topics/null-space-constrained-refusal-steering"},{"title":"Accepted as a workshop paper at ReALM-GEN, ICLR 2026","url":"https://openreview.net/pdf?id=JhKgHfpIF8"},{"title":"Mind the Performance Gap: Capability-Behavior Trade-offs in Feature Steering","url":"https://arxiv.org/html/2602.04903v1"}]

Based on the search results, here's what I found about AlphaSteer and refusal steering with null-space constraints at ICLR 2026:

## Overview

AlphaSteer is the implementation of the paper "AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint" accepted at ICLR 2026.

## Core Concept

AlphaSteer is a theoretically grounded and empirically effective activation steering method that considers activation steering as a learnable process with two principled learning objectives: utility preservation and safety enhancement.

## Technical Approach

For utility preservation, it learns to construct a nearly zero vector for steering benign data with null-space constraints. For safety enhancement, it learns to construct a refusal direction vector for steering malicious data with the help of linear regression.

## Problem It Addresses

Activation steering fundamentally suffers from the trade-off between safety and utility, and although prior efforts such as vector calibration and conditional steering have attempted to mitigate this trade-off, their lack of theoretical grounding limits their robustness and effectiveness.

## Results

Experiments across multiple jailbreak attacks and utility benchmarks demonstrate the effectiveness of AlphaSteer, which significantly improves the safety of LLMs without compromising general capabilities.

The research is authored by Leheng Sheng, Changshuo Shen, and colleagues, with code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0886a0b7-f7d1-44ee-8533-359db0776973",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "0bcb081e-85df-46e1-bd62-9482b9acd579",
  "sourceToolAssistantUUID": "0886a0b7-f7d1-44ee-8533-359db0776973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T13:17:27.001Z_

<details><summary>↩ Tool result · `toolu_01L4V8WAiuxmoPwvnzWHaJU1`</summary>

```text
Web search results for query: "SafeThinker gateway query risk reasoning dynamic safety 2026"

Links: [{"title":"[2601.16506] SafeThinker: Reasoning about Risk to Deepen Safety Beyond Shallow Alignment","url":"https://arxiv.org/abs/2601.16506"},{"title":"SafeThinker: Reasoning about Risk to Deepen Safety Beyond Shallow Alignment","url":"https://arxiv.org/pdf/2601.16506"},{"title":"SafeThinker: Reasoning about Risk to Deepen Safety Beyond Shallow Alignment WARNING: This paper contains model outputs that may be considered offensive.","url":"https://arxiv.org/html/2601.16506"},{"title":"THINKSAFE: Self-Generated Safety Alignment for Reasoning Models","url":"https://arxiv.org/pdf/2601.23143"},{"title":"SafeRBench: Dissecting the Reasoning Safety of Large Language Models","url":"https://arxiv.org/html/2511.15169"},{"title":"Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away","url":"https://itsvaibhav01.github.io/SafeThink-web/"},{"title":"The New Era of Application Security: Reasoning-Based Agents, Runtime Reality, and Risk Intelligence | Qualys","url":"https://blog.qualys.com/product-tech/2026/03/17/new-era-application-security-reasoning-agents-runtime-risk-2026"},{"title":"The Modern Risk Prioritization Framework for 2026 - Safe Security","url":"https://safe.security/resources/blog/the-modern-risk-prioritization-framework-for-2026/"},{"title":"[2601.23143] THINKSAFE: Self-Generated Safety Alignment for Reasoning Models","url":"https://arxiv.org/abs/2601.23143"},{"title":"Cisco Networking Questions for CCNA Prep and Real- ...","url":"https://www.linkedin.com/posts/gitesh-d-aa95a8227_cisco-ccna-networking-activity-7403373522448027648-xV5d"}]

Based on the search results, I found detailed information about SafeThinker:

## SafeThinker Overview

SafeThinker is an adaptive framework that dynamically allocates defensive resources via a lightweight gateway classifier. The research paper was published on January 23, 2026.

## Gateway for Query Risk Reasoning

The Gateway for Query Risk Reasoning first analyzes each query, routing it to one of three paths: High-Risk Path for immediate refusal, Low-Risk Path for robust generation, and Uncertain-Risk Path for dynamic safety control.

## Three Defensive Mechanisms

Based on the gateway's risk assessment, inputs are routed through three distinct mechanisms: (i) a Standardized Refusal Mechanism for explicit threats to maximize efficiency; (ii) a Safety-Aware Twin Expert (SATE) module to intercept deceptive attacks masquerading as benign queries; and (iii) a Distribution-Guided Think (DDGT) component that adaptively intervenes during uncertain generation.

## Performance Results

Experiments show that SafeThinker significantly lowers attack success rates across diverse jailbreak strategies without compromising utility, demonstrating that coordinating intrinsic judgment throughout the generation process effectively balances robustness and practicality.

The framework addresses the problem of shallow safety alignment in large language models by using reasoning about risk throughout the generation process to provide more robust defense against various attack types including jailbreaks and deceptive prompts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22b64f0a-5ff3-4300-bb5a-50891da077e6",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "f5824f8f-f2dd-4509-9c0b-50f3019826f2",
  "sourceToolAssistantUUID": "22b64f0a-5ff3-4300-bb5a-50891da077e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T13:17:27.553Z_

<details><summary>↩ Tool result · `toolu_011aVv3SGdd2C1Y8YdXFz83X`</summary>

```text
Web search results for query: ""refusal direction" "turn-level" OR "multi-turn" OR "cumulative risk" LLM scaling"

Links: [{"title":"Multi-Turn Attacks Expose Weaknesses in Open-Weight LLM Models - Infosecurity Magazine","url":"https://www.infosecurity-magazine.com/news/multi-turn-attacks-llm-models/"},{"title":"Scaling Patterns in Adversarial Alignment: Evidence from","url":"https://arxiv.org/pdf/2511.13788"},{"title":"Refusal Direction in LLM Safety","url":"https://www.emergentmind.com/topics/refusal-direction"},{"title":"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet","url":"https://static.scale.com/uploads/6019a18f03a4ae003acb1113/MHJ.pdf"},{"title":"Published at Building Trust Workshop at ICLR 2025 MONITORING LLM AGENTS FOR","url":"https://openreview.net/pdf?id=LC0XQ6ufbr"},{"title":"Introducing the Cisco LLM Security Leaderboard: Bringing Transparency to AI Security - Cisco Blogs","url":"https://blogs.cisco.com/ai/llm-security-leaderboard"},{"title":"SOM Directions are Beter than One: Multi-Directional Refusal Supresion in","url":"https://arxiv.org/pdf/2511.08379"},{"title":"Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection","url":"https://arxiv.org/html/2602.11247"},{"title":"Refusal in Language Models Is Mediated by a Single Direction Andy Arditi∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f545448535dfde4f9786555403ab7c49-Paper-Conference.pdf"},{"title":"Evaluating Performance Drift from Model Switching in Multi-Turn LLM Systems","url":"https://arxiv.org/html/2603.03111"}]

I've completed a web search on the topic. Here are the key findings related to refusal direction, turn-level, multi-turn, cumulative risk, and LLM scaling:

## Key Research Areas

**Refusal Mechanisms and Directions:**

LLMs represent features as linear directions in activation space, and researchers have studied the linear representation of particular features such as harmlessness, truth, and others, with these feature directions shown to be effective causal mediators of behavior enabling fine-grained steering of model outputs.

The "concept cone" framework reveals refusal is often governed by multiple, independently controllable axes in activation space—polyhedral cones—rather than a strict line, and for some models, cones up to five dimensions exist, each corresponding to a functionally independent refusal mechanism.

**Multi-Turn Vulnerability and Scaling:**

Open-weight large language models have remained highly vulnerable to adaptive multi-turn adversarial attacks, with isolated one-off attack attempts frequently failing, but persistent multi-step conversations achieving success rates exceeding 90% against most tested defenses.

Relative model scale drives asymmetric vulnerability in multi-LLM interactions: larger attacker models possess greater expressive and persuasive capacity, enabling more effective jailbreaks against smaller, alignment-tuned targets.

**Cumulative Risk in Multi-Turn Attacks:**

Multi-turn prompt injection attacks distribute malicious intent across multiple conversation turns, and a fundamental flaw in the weighted-average approach is that it converges to the per-turn score regardless of turn count, making a 20-turn persistent attack score identically to a single suspicious turn, thus researchers propose peak + accumulation scoring combining peak single-turn risk, persistence ratio, and category diversity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "914c64ee-ca43-48a1-b63c-5a5f5828d85b",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "a2ddba23-f0de-4c61-b01f-6ac0120c7c31",
  "sourceToolAssistantUUID": "914c64ee-ca43-48a1-b63c-5a5f5828d85b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T13:17:27.934Z_

<details><summary>↩ Tool result · `toolu_01BqyrJfMirYE5h3Y4vQSZEh`</summary>

```text
Web search results for query: ""refusal steering" fine-grained control LLM 2025 arxiv 2512.16602"

Links: [{"title":"Refusal Steering: Fine-grained Control over LLM Refusal Behaviour","url":"https://arxiv.org/pdf/2512.16602"},{"title":"[2512.16602] Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics","url":"https://arxiv.org/abs/2512.16602"},{"title":"Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics","url":"https://arxiv.org/html/2512.16602"},{"title":"GitHub - ElSnacko/llm-steering: Statistical toolkit for LLM refusal steering. Uses judge scores to weight training data, correlation analysis to identify effective layers, and automated alpha optimization. Implements WRMD method from García-Ferrero et al. 2025. Can merge steering into weights permanently.","url":"https://github.com/ElSnacko/llm-steering"},{"title":"Refusal in Language Models Is Mediated by a Single Direction Andy Arditi∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f545448535dfde4f9786555403ab7c49-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025 PROGRAMMING REFUSAL WITH","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf"},{"title":"SafeSteer: Interpretable Safety Steering with Refusal-Evasion in LLMs","url":"https://arxiv.org/html/2506.04250v1"},{"title":"Uncovering Representation Vectors for LLM “Thought” ...","url":"https://openreview.net/pdf?id=dVqZBagXF3"},{"title":"LLMs Encode Harmfulness and Refusal Separately Jiachen Zhao","url":"https://openreview.net/pdf?id=zLkpt30ngy"},{"title":"Mitigating Over-Refusal in Aligned Language Models ... - GitHub","url":"https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf"}]

Based on the search results, here's information about the paper arxiv 2512.16602:

## Refusal Steering: Fine-grained Control over LLM Refusal Behaviour

Refusal Steering is an inference-time method to exercise fine-grained control over Large Language Models refusal behaviour on politically sensitive topics without retraining.

### Key Technical Approach

The method replaces fragile pattern-based refusal detection with an LLM-as-a-judge that assigns refusal confidence scores and proposes a ridge-regularized variant to compute steering vectors that better isolate the refusal-compliance direction.

### Performance and Results

On Qwen3-Next-80B-A3B-Thinking, the method removes the refusal behaviour of the model around politically sensitive topics while maintaining safety on JailbreakBench and near-baseline performance on general benchmarks. The approach generalizes across 4B and 80B models and can also induce targeted refusals when desired.

### Analysis of Steering Vectors

The refusal signals concentrate in deeper layers of the transformer and are distributed across many dimensions.

### Authors and Timeline

The paper by Iker García-Ferrero, David Montero, and Roman Orus was submitted on December 18, 2025 with the latest revision on February 24, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e234de6b-ade3-4cf3-8469-103bc527f849",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "15ce75d9-9d2f-4ac8-93dc-2e1fc3419ec5",
  "sourceToolAssistantUUID": "e234de6b-ade3-4cf3-8469-103bc527f849",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T13:17:29.935Z_

<details><summary>↩ Tool result · `toolu_01TWz87yLLFDLZ28tUYfNVBC`</summary>

```text
Web search results for query: ""concept cones" "geometry of refusal" representational independence LLM 2025"

Links: [{"title":"[2502.17420] The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence","url":"https://arxiv.org/abs/2502.17420"},{"title":"The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence","url":"https://proceedings.mlr.press/v267/wollschlager25a.html"},{"title":"ICML Poster The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence","url":"https://icml.cc/virtual/2025/poster/46298"},{"title":"The Geometry of Refusal in Large Language Models:","url":"https://arxiv.org/pdf/2502.17420"},{"title":"[2502.17420v1] The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence","url":"https://arxiv.org/abs/2502.17420v1"},{"title":"The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence | OpenReview","url":"https://openreview.net/forum?id=80IwJqlXs8"},{"title":"The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence","url":"https://arxiv.org/html/2502.17420v2"},{"title":"The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250217420W/abstract"},{"title":"1 Introduction","url":"https://arxiv.org/html/2502.17420v1"},{"title":"The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence","url":"https://synthical.com/article/The-Geometry-of-Refusal-in-Large-Language-Models:-Concept-Cones-and-Representational-Independence-8db3bf9b-d91f-4fe8-a9c6-1b8f6323c3da"}]

Based on the search results, I found detailed information about the research on concept cones, geometry of refusal, and representational independence in LLMs.

## Summary of Key Findings

The safety alignment of large language models (LLMs) can be circumvented through adversarially crafted inputs, yet prior work suggests that a single refusal direction in the model's activation space determines whether an LLM refuses a request.

However, researchers proposed a novel gradient-based approach to representation engineering to identify refusal directions, uncovering multiple independent directions and even multi-dimensional concept cones that mediate refusal.

### Representational Independence

A key contribution of this research is the concept of representational independence. The researchers show that orthogonality alone does not imply independence under intervention, motivating the notion of representational independence that accounts for both linear and non-linear effects. This concept of "representational independence" considers both linear and non-linear interactions, to more accurately identify truly distinct mechanisms.

### Refusal Mechanisms

Refusal mechanisms in LLMs are governed by complex spatial structures with functionally independent directions, confirming that multiple distinct mechanisms drive refusal behavior. Unlike prior work that assumes model refusal is controlled by a single linear direction, there exist multi-dimensional polyhedral cones which contain infinite refusal directions.

This research was published in the Proceedings of the 42nd International Conference on Machine Learning (ICML) in 2025 and authored by Wollschläger, Elstner, Geisler, Cohen-Addad, Günnemann, and Gasteiger.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "138be6df-351f-4395-8019-d9ce6e71224a",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "5405d9ce-ad18-4336-8e03-e20bd51242a2",
  "sourceToolAssistantUUID": "138be6df-351f-4395-8019-d9ce6e71224a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T13:17:32.170Z_

<details><summary>↩ Tool result · `toolu_013ACRacM3THjL3vyTm89nec`</summary>

```text
Web search results for query: "R2D2 robust refusal dynamic defense LLM safety 2025 2026"

Links: [{"title":"Robust Refusal Dynamic Defense (R2D2)","url":"https://www.emergentmind.com/topics/robust-refusal-dynamic-defense-r2d2"},{"title":"[Literature Review] HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal","url":"https://www.themoonlight.io/en/review/harmbench-a-standardized-evaluation-framework-for-automated-red-teaming-and-robust-refusal"},{"title":"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal","url":"https://arxiv.org/html/2402.04249v2"},{"title":"HarmBench: Standardized LLM Red Teaming Framework","url":"https://www.emergentmind.com/topics/harmbench-framework"},{"title":"HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal [Quick Review]","url":"https://liner.com/review/harmbench-standardized-evaluation-framework-for-automated-red-teaming-and-robust"},{"title":"LLM Refusal Abliteration Mechanisms","url":"https://www.emergentmind.com/topics/refusal-abliteration"},{"title":"GitHub - chawins/llm-sp: Papers and resources related to the security and privacy of LLMs 🤖","url":"https://github.com/chawins/llm-sp"},{"title":"RedTWIZ: Diverse LLM Red Teaming via Adaptive Attack Planning","url":"https://assets.amazon.science/26/30/c7c4a17149a8bb47d774ed95a6b3/redtwiz-diverse-llm-redteaming-adaptive-attack-planning.pdf"},{"title":"Robust LLM safeguarding via refusal feature adversarial training | OpenReview","url":"https://openreview.net/forum?id=s5orchdb33"},{"title":"Jailbreaking LLMs: A Survey of Attacks, Defenses and Evaluation","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176773228.86819800/v1"}]

Based on the web search results, I can provide you with comprehensive information about R2D2 (Robust Refusal Dynamic Defense) for LLM safety:

## Overview

R2D2 denotes a class of safety alignment strategies for LLMs that target vulnerabilities in refusal mechanisms, particularly in the face of adversarial "jailbreak" attacks.

## How R2D2 Works

R2D2 frameworks go beyond surface-level training by structurally re-engineering refusal circuits, either at the level of internal representations or by explicitly diffusing refusal signals across the model's network, thereby counteracting attacks that exploit localized refusal features.

R2D2 approaches uniformly target gaps by ensuring that refusal behaviors are (i) deeply integrated at multiple depths and across token sequences, (ii) highly controllable and interpretable at the latent or token level, and (iii) robust under adaptive and previously unseen attack vectors.

## Recent Research (2025-2026)

Multiple recent works formalize R2D2 as a family comprising latent space steering (LatentGuard), probabilistic refusal direction ablation (DeepRefusal), extended refusal response design, decoupled refusal training, and dual-objective robust refusal optimization (Shu et al., 24 Sep 2025, Xie et al., 18 Sep 2025, Shairah et al., 25 May 2025, Yuan et al., 2024, Zhao et al., 5 Mar 2025).

## Performance Results

For instance, Zephyr 7B + R2D2 reduces the average Attack Success Rate (ASR) for GCG attacks to 5.9%, a substantial improvement compared to Llama 2 7B Chat (31.8%) and Llama 2 13B Chat (30.2%), representing a 4x lower ASR than the second most robust LLM on GCG attacks.

Crucially, the R2D2 adversarial training method preserves LLM performance on benign tasks. Zephyr 7B + R2D2 achieves an MT-Bench score of 6.0, which is comparable to Mistral 7B Instruct v0.2 (6.5) and outperforms Koala 13B (5.4). This indicates that the significant gains in robustness do not come at the cost of reduced utility or general conversational ability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59c7f63c-647a-43d5-bf86-2fa0d4547a3b",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "58d8d739-0c74-4ef5-a90d-5da3e327a8b5",
  "sourceToolAssistantUUID": "59c7f63c-647a-43d5-bf86-2fa0d4547a3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T13:17:33.906Z_

<details><summary>↩ Tool result · `toolu_014J7YRhuQUMEnpBPJWwpWwF`</summary>

```text
Web search results for query: ""there is more to refusal" "single direction" LLM 2026 arXiv"

Links: [{"title":"There Is More to Refusal in Large Language Models than a Single Direction","url":"https://www.arxiv.org/pdf/2602.02132"},{"title":"[2602.02132] There Is More to Refusal in Large Language Models than a Single Direction","url":"https://arxiv.org/abs/2602.02132"},{"title":"There Is More to Refusal in Large Language Models than a Single Direction","url":"https://arxiv.org/html/2602.02132v1"}]

I found the paper you were searching for! Here are the key findings:

The paper "There Is More to Refusal in Large Language Models than a Single Direction" challenges prior research on LLM refusal mechanisms.

**Main Finding:**
Prior work argues that refusal in large language models is mediated by a single activation-space direction, but this paper shows that account is incomplete.

**Key Results:**
Across eleven categories of refusal and non-compliance, including safety, incomplete or unsupported requests, anthropomorphization, and over-refusal, these refusal behaviors correspond to geometrically distinct directions in activation space. However, linear steering along any refusal-related direction produces nearly identical refusal to over-refusal trade-offs, acting as a shared one-dimensional control knob.

In essence, the primary effect of different directions is not whether the model refuses, but how it refuses.

The paper was published on February 2, 2026 (arXiv:2602.02132) by authors including Faaiz Joad, Majd Hawasly, Sabri Boughorbel, Nadir Durrani, and Husrev Taha Sencar.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3ae04fa-fa36-4b02-b2cb-2573a483ab3e",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "7afeed3c-e434-43b2-9152-eb72bd76bbc6",
  "sourceToolAssistantUUID": "e3ae04fa-fa36-4b02-b2cb-2573a483ab3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T13:17:37.348Z_

<details><summary>↩ Tool result · `toolu_01GSncTvipRTF7uvyCf8GxKP`</summary>

```text
Web search results for query: "multi-turn conversation cumulative risk score refusal activation steering LLM"

Links: [{"title":"Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection","url":"https://arxiv.org/html/2604.28129"},{"title":"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs","url":"https://arxiv.org/html/2602.16935v1"},{"title":"Multi-Turn Conversation Attacks on LLMs","url":"https://apxml.com/courses/intro-llm-red-teaming/chapter-3-core-red-teaming-techniques-llms/multi-turn-conversation-attacks"},{"title":"Refusal Steering: Fine-grained Control over LLM Refusal Behaviour","url":"https://arxiv.org/pdf/2512.16602"},{"title":"Risk-adaptive Activation Steering for Safe Multimodal Large Language Models","url":"https://xai.kaist.ac.kr/static/files/2025_hcai_workshop/paper_24.pdf"},{"title":"Published at Building Trust Workshop at ICLR 2025 MONITORING LLM AGENTS FOR","url":"https://openreview.net/pdf?id=LC0XQ6ufbr"},{"title":"LLMS GET LOST IN MULTI-TURN CONVERSATION","url":"https://openreview.net/pdf?id=VKGTGGcwl6"},{"title":"Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk for Large Language Models","url":"https://arxiv.org/html/2602.04896"},{"title":"LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet","url":"https://static.scale.com/uploads/6019a18f03a4ae003acb1113/MHJ.pdf"},{"title":"Why LLMs Get Lost in Multi-Turn Conversation | by KUNAL VERMA | Medium","url":"https://hereiskunalverma.medium.com/why-llms-get-lost-in-multi-turn-conversation-e458a0a34a9a"}]

I've found relevant research on this topic. Here's what the search results reveal:

## Key Findings

Multi-turn attacks require navigating multiple phases (trust-building, pivoting, escalation), with cumulative drift consistently elevated in adversarial conversations.

### Cumulative Risk Score Concepts

DeepContext uses hidden state as selective memory, integrating the gradient of risk over time, allowing detection of semantic drift in attacks by monitoring the cumulative trajectory of preceding interactions. The continuous risk vector generated provides a real-time, quantitative measure of intent evolution.

### Refusal Activation Steering

Risk-adaptive Activation Steering (RAS) steers activations toward refusal behavior according to the risk score, consisting of exponentially weighted risk evaluation and risk-adaptive activation steering stages.

Refusal Steering is an inference-time method for fine-grained control over LLM refusal behavior without retraining, using LLM-as-a-judge to assign refusal confidence scores and ridge-regularized steering vectors.

### Multi-Turn Attack Detection

Trajectory scalars measure how far conversations have traveled in activation space, so more sophisticated attacks with more phases accumulate more drift. Activation-based detection distinguishes when models are being steered—invisible at the text surface.

The research demonstrates that modern defenses are combining cumulative risk scoring with activation steering to detect and prevent multi-turn jailbreak attempts that bypass traditional single-turn safety mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6f76fe1-6850-4d95-adc8-8e5e10c62af0",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "c480ab09-be96-40c7-af52-130b1715f717",
  "sourceToolAssistantUUID": "e6f76fe1-6850-4d95-adc8-8e5e10c62af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-15T13:17:40.191Z_

This is very informative. Let me run a few final targeted searches to pin down the closest competitors to your exact idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c480ab09-be96-40c7-af52-130b1715f717",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RGdFYgn8ehTkmwgiJC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7190e6af-bdb3-4d19-ade1-607bfd562f97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mvxyBerZ1YMexbjcSd6r7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10393,
      "cache_read_input_tokens": 14506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10393,
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

_source line 41 · 2026-05-15T13:17:41.146Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RjLviaEP3Dgou2JLxkpTNd`</summary>

```json
{
  "query": "\"risk-adaptive activation steering\" RAS multimodal LLM refusal KAIST 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7190e6af-bdb3-4d19-ade1-607bfd562f97",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RGdFYgn8ehTkmwgiJC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13e1375f-1d4a-43da-89d4-5d0ebaed1179",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mvxyBerZ1YMexbjcSd6r7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10393,
      "cache_read_input_tokens": 14506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10393,
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

_source line 42 · 2026-05-15T13:17:41.633Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L5MMB4MXBaK9Hp47QyCmSB`</summary>

```json
{
  "query": "DeepContext stateful detection multi-turn adversarial intent drift LLM 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13e1375f-1d4a-43da-89d4-5d0ebaed1179",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RGdFYgn8ehTkmwgiJC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cb54834-dd04-4ea2-8981-6c4e01c8e2c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mvxyBerZ1YMexbjcSd6r7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10393,
      "cache_read_input_tokens": 14506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10393,
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

_source line 43 · 2026-05-15T13:17:42.687Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S9GXQiHPKYCnA6zYjTPxtb`</summary>

```json
{
  "query": "\"peak accumulation\" proxy-level scoring multi-turn LLM attack detection 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cb54834-dd04-4ea2-8981-6c4e01c8e2c3",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RGdFYgn8ehTkmwgiJC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49e0a4e0-1d77-4f0f-9dc6-4c3c3f7758b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mvxyBerZ1YMexbjcSd6r7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10393,
      "cache_read_input_tokens": 14506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10393,
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

_source line 44 · 2026-05-15T13:17:42.881Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RuiGSaF5BqsaAbgGZeBBPp`</summary>

```json
{
  "query": "\"latent adversarial detection\" adaptive probing activations multi-turn attack 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49e0a4e0-1d77-4f0f-9dc6-4c3c3f7758b1",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RGdFYgn8ehTkmwgiJC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "743d3217-ad67-4f4f-bf56-f33d4d95a401",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mvxyBerZ1YMexbjcSd6r7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10393,
      "cache_read_input_tokens": 14506,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10393
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 14506,
          "cache_creation_input_tokens": 10393,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10393,
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

_source line 45 · 2026-05-15T13:17:48.445Z_

<details><summary>↩ Tool result · `toolu_01L5MMB4MXBaK9Hp47QyCmSB`</summary>

```text
Web search results for query: "DeepContext stateful detection multi-turn adversarial intent drift LLM 2026 arxiv"

Links: [{"title":"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs","url":"https://arxiv.org/html/2602.16935v1"},{"title":"[2602.16935] DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs","url":"https://arxiv.org/abs/2602.16935"},{"title":"[2602.16935v1] DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs","url":"https://arxiv.org/abs/2602.16935v1"},{"title":"DeepContext: Stateful Real-Time Detection of Multi-Turn ...","url":"https://www.arxiv.org/pdf/2602.16935"},{"title":"Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection","url":"https://arxiv.org/html/2604.28129"},{"title":"DeepContext: Stateful Real-Time Detection of Multi-Turn ...","url":"https://www.researchgate.net/publication/400970384_DeepContext_Stateful_Real-Time_Detection_of_Multi-Turn_Adversarial_Intent_Drift_in_LLMs"},{"title":"Temporal Context Awareness: A Defense Framework Against Multi-turn Manipulation Attacks on Large Language Models","url":"https://arxiv.org/html/2503.15560v1"},{"title":"[2503.15560] Temporal Context Awareness: A Defense Framework Against Multi-turn Manipulation Attacks on Large Language Models","url":"https://arxiv.org/abs/2503.15560"},{"title":"[2604.13061] Token Statistics Reveal Conversational Drift in Multi-turn LLM Interaction","url":"https://arxiv.org/abs/2604.13061"},{"title":"Drift No More? Context Equilibria in Multi-Turn LLM Interactions","url":"https://arxiv.org/html/2510.07777v1"}]

I found the paper you were searching for. Here's a summary of the findings:

## DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs

While Large Language Model (LLM) capabilities have scaled, safety guardrails remain largely stateless, treating multi-turn dialogues as a series of disconnected events. This lack of temporal awareness facilitates a "Safety Gap" where adversarial tactics, like Crescendo and ActorAttack, slowly bleed malicious intent across turn boundaries to bypass stateless filters.

### Key Innovation

DeepContext is a stateful monitoring framework designed to map the temporal trajectory of user intent. It discards the isolated evaluation model in favor of a Recurrent Neural Network (RNN) architecture that ingests a sequence of fine-tuned turn-level embeddings. By propagating a hidden state across the conversation, DeepContext captures the incremental accumulation of risk that stateless models overlook.

### Performance Results

By focusing on the sequence of intent embeddings rather than the total volume of accumulated text, DeepContext achieves a 0.84 F1-score against multi-turn jailbreaks while maintaining sub-20ms latency on a T4 GPU.

The paper was published on arxiv.org on February 18, 2026, with ID 2602.16935, authored by Justin Albrethsen and three other researchers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cb54834-dd04-4ea2-8981-6c4e01c8e2c3",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "600f0d75-f747-4dba-a157-38e0ba994154",
  "sourceToolAssistantUUID": "2cb54834-dd04-4ea2-8981-6c4e01c8e2c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T13:17:49.969Z_

<details><summary>↩ Tool result · `toolu_01RjLviaEP3Dgou2JLxkpTNd`</summary>

```text
Web search results for query: ""risk-adaptive activation steering" RAS multimodal LLM refusal KAIST 2025"

Links: [{"title":"Risk-adaptive Activation Steering for Safe Multimodal Large Language Models","url":"https://xai.kaist.ac.kr/static/files/2025_hcai_workshop/paper_24.pdf"},{"title":"Risk-adaptive Activation Steering for Safe Multimodal Large Language Models","url":"https://arxiv.org/html/2510.13698"},{"title":"Risk-adaptive Activation Steering for Safe Multimodal Large Language Models | OpenReview","url":"https://openreview.net/forum?id=BjIfaIbXEJ"},{"title":"Risk-adaptive Activation Steering for Safe Multimodal ...","url":"https://arxiv.org/abs/2510.13698"},{"title":"Risk-adaptive Activation Steering for Safe Multimodal Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/396517822_Risk-adaptive_Activation_Steering_for_Safe_Multimodal_Large_Language_Models"},{"title":"[Literature Review] Risk-adaptive Activation Steering for Safe Multimodal Large Language Models","url":"https://www.themoonlight.io/en/review/risk-adaptive-activation-steering-for-safe-multimodal-large-language-models"},{"title":"Risk-adaptive Activation Steering for Safe Multimodal Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13698v1"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Published as a conference paper at ICLR 2025 PROGRAMMING REFUSAL WITH","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf"},{"title":"Multi-modal Safety Concept Activations","url":"https://www.emergentmind.com/topics/multi-modal-safety-concept-activation-vector"}]

Based on the search results, I found comprehensive information about Risk-adaptive Activation Steering (RAS). Here's what the research reveals:

## Overview

Risk-adaptive Activation Steering (RAS) is an inference-time defense mechanism designed to enhance the safety of Multimodal Large Language Models (MLLMs) against harmful multimodal queries without sacrificing utility or increasing inference overhead.

## The Problem It Addresses

Current MLLMs fail to generate refusals against multimodal instructions with malicious intent embedded in images, despite extensive vision-language alignment. Existing MLLM safety alignment approaches have two primary limitations: (i) insufficient cross-modal attention to safety-critical image regions, leading to a failure to distinguish between benign and malicious multimodal inputs; and (ii) utility degradation and slower inference speeds in prior inference-time methods.

## How RAS Works

RAS consists of three stages: (i) Query Reformulation, which augments input queries with concise visual contexts and safety prompts to strengthen cross-modal attention to safety-critical image regions; (ii) Risk Evaluation, where MLLM output activations are compared with unsafe prototypes to produce similarity-based risk scores; and (iii) Risk-adaptive Activation Steering, where activations are steered toward refusal behavior according to the risk score.

## Key Results

Extensive experiments across multiple benchmarks on multimodal safety and utility demonstrate that the RAS significantly reduces attack success rates, preserves general task performance, and improves inference speed over prior inference-time defenses. RAS consistently achieved the lowest attack success rates (ASR), with average reductions up to 90.5%, significantly outperforming prior inference-time defenses.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13e1375f-1d4a-43da-89d4-5d0ebaed1179",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "6d613758-2a94-463d-a1c4-7672508cc577",
  "sourceToolAssistantUUID": "13e1375f-1d4a-43da-89d4-5d0ebaed1179",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T13:17:50.574Z_

<details><summary>↩ Tool result · `toolu_01S9GXQiHPKYCnA6zYjTPxtb`</summary>

```text
Web search results for query: ""peak accumulation" proxy-level scoring multi-turn LLM attack detection 2026"

Links: [{"title":"[2602.11247] Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection","url":"https://arxiv.org/abs/2602.11247"},{"title":"Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection","url":"https://arxiv.org/html/2602.11247v2"},{"title":"(PDF) Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection","url":"https://www.researchgate.net/publication/400741727_Peak_Accumulation_A_Proxy-Level_Scoring_Formula_for_Multi-Turn_LLM_Attack_Detection"},{"title":"A Proxy-Level Scoring Formula for Multi-Turn LLM Attack ...","url":"https://arxiv.org/pdf/2602.11247"},{"title":"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs","url":"https://arxiv.org/html/2602.16935v1"},{"title":"Knowledge-Driven Multi-Turn Jailbreaking on Large Language Models","url":"https://arxiv.org/html/2601.05445"},{"title":"Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection","url":"https://arxiv.org/html/2604.28129"},{"title":"[2602.16935v1] DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs","url":"https://arxiv.org/abs/2602.16935v1"},{"title":"[2604.28129] Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection","url":"https://arxiv.org/abs/2604.28129"},{"title":"Stepwise Multi-Turn Jailbreak Attacks on Code LLMs via ...","url":"https://assets.amazon.science/35/78/937605a146239bd5a0f70c842409/safolab-stepwise-multi-turn-jailbreak-attacks-on-code-llms.pdf"}]

Based on the search results, I found highly relevant research on "peak + accumulation" scoring for multi-turn LLM attack detection. Here's what the search revealed:

## Peak + Accumulation: A Proxy-Level Scoring Formula

A recent paper proposes peak + accumulation scoring—a formula combining peak single-turn risk, persistence ratio, and category diversity, drawing on analogies from change-point detection (CUSUM), Bayesian belief updating, and security risk-based alerting.

### The Problem It Addresses

While single-turn detection has been extensively studied, no published formula existed for aggregating per-turn pattern scores into a conversation-level risk score at the proxy layer without invoking an LLM. A fundamental flaw in the intuitive weighted-average approach is that it converges to the per-turn score regardless of turn count, meaning a 20-turn persistent attack scores identically to a single suspicious turn.

### Performance Results

Peak + accumulation achieves 90.8% recall across 588 attack conversations, with all 9 handcrafted attacks detected and 525 of 579 WildJailbreak-sourced attacks (90.7%) detected.

### Key Advantages

The formula is simple (5 lines of code), fast (microseconds per request), deterministic, and auditable. It requires no model inference, no training data, and no GPU.

The paper was published on arXiv in February-March 2026 by J Alex Corll.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49e0a4e0-1d77-4f0f-9dc6-4c3c3f7758b1",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "a213d2b5-694b-496c-9575-7cfea3d14749",
  "sourceToolAssistantUUID": "49e0a4e0-1d77-4f0f-9dc6-4c3c3f7758b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T13:17:51.320Z_

<details><summary>↩ Tool result · `toolu_01RuiGSaF5BqsaAbgGZeBBPp`</summary>

```text
Web search results for query: ""latent adversarial detection" adaptive probing activations multi-turn attack 2026"

Links: [{"title":"[2604.28129] Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection","url":"https://arxiv.org/abs/2604.28129"},{"title":"Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection","url":"https://arxiv.org/html/2604.28129"},{"title":"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs","url":"https://arxiv.org/html/2602.16935v1"},{"title":"One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue","url":"https://arxiv.org/html/2605.05630"},{"title":"Obfuscated Activations Bypass LLM Latent-Space Defenses","url":"https://arxiv.org/html/2412.09565v2"},{"title":"Multi-Turn Adaptive Prompting Attack on Large Vision-Language Models","url":"https://arxiv.org/pdf/2602.14399"},{"title":"Multi-Turn Attacks Expose Weaknesses in Open-Weight LLM Models - Infosecurity Magazine","url":"https://www.infosecurity-magazine.com/news/multi-turn-attacks-llm-models/"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"},{"title":"Jailbreaking LLMs: A Survey of Attacks, Defenses and Evaluation | TechRxiv","url":"https://www.techrxiv.org/users/1011181/articles/1373070/master/file/data/Jailbreaking_LLMs_2026/Jailbreaking_LLMs_2026.pdf"},{"title":"Promising results from Latent Adversarial Training | Apart Research","url":"https://apartresearch.com/news/promising-results-from-latent-adversarial-training"}]

Based on the search results, I found highly relevant recent research on "Latent Adversarial Detection" with focus on adaptive probing and multi-turn attacks:

## Key Findings

The paper "Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection" addresses how multi-turn prompt injection follows a known attack path including trust-building, pivoting, and escalation, but text-level defenses miss covert attacks where individual turns appear benign.

### Core Methodology

The research shows this attack path leaves an activation-level signature in the model's residual stream: each phase shift moves the activation, producing a total path length far exceeding benign conversations, termed "adversarial restlessness." Five scalar trajectory features capturing this signal lift conversation-level detection from 76.2% to 93.8% on synthetic held-out data.

### Performance and Generalization

The signal replicates across four model families (24B-70B); probes are model-specific and do not transfer across architectures. Combined three-source training achieves 89.4% detection at 2.4% false positive rate on a held-out mixed set.

### Defense Approach

The research proposes probing the target LLM's internal activations to detect adversarial intent in how the model understands an incoming interaction, with the hypothesis that if adversarial intent produces a consistent activation signature regardless of surface encoding, framing, or language, then activation probes offer a defense mechanism that scales with model capability.

The paper was posted on April 30, 2026, making it very recent work in this field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "743d3217-ad67-4f4f-bf56-f33d4d95a401",
  "isSidechain": true,
  "promptId": "6fb195c9-a8aa-4b38-a7ac-85b02f37e044",
  "agentId": "af14b787a68e72cb2",
  "type": "user",
  "uuid": "8295616d-cb18-438e-81d6-9ce217024f6b",
  "sourceToolAssistantUUID": "743d3217-ad67-4f4f-bf56-f33d4d95a401",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-15T13:18:56.677Z_

Now I have a comprehensive picture. Here is my thorough analysis:

---

## Literature Survey: Dynamically Scaling a Refusal Activation Direction Based on Cumulative Turn-Level Risk

### Executive Summary

No published work (as of May 2026) proposes the exact mechanism you describe -- dynamically scaling (i.e., modulating the magnitude of) a refusal activation direction in the model's residual stream based on a cumulative, turn-by-turn risk score across a conversation. However, several very recent papers occupy adjacent territory and collectively narrow the novelty gap. Below is a paper-by-paper breakdown.

---

### 1. CLOSEST MATCH: Risk-adaptive Activation Steering (RAS)

- **Paper:** "Risk-adaptive Activation Steering for Safe Multimodal Large Language Models"
- **Authors:** KAIST XAI Lab researchers
- **Venue:** HCAI Workshop 2025; arXiv 2510.13698 (October 2025)
- **Similarity: HIGH (closest competitor)**

RAS computes a risk score from activation similarity to unsafe prototypes, then steers activations toward a refusal direction proportionally to that score. This is the single closest published system to your idea. **Critical difference:** RAS operates on a per-query basis for multimodal (image+text) inputs. It is stateless -- it does not accumulate risk across turns and does not modulate a refusal direction based on conversation history. Your idea's core novelty (cumulative turn-level risk driving the scaling factor) is absent from RAS.

---

### 2. VERY RELEVANT: DeepContext -- Stateful Multi-Turn Intent Drift Detection

- **Paper:** "DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs"
- **Authors:** Justin Albrethsen et al.
- **Date:** February 2026, arXiv 2602.16935
- **Similarity: MODERATE-HIGH (addresses the "cumulative" part but not the "activation steering" part)**

DeepContext uses an RNN that propagates a hidden state across turns, capturing incremental accumulation of risk. It produces a continuous risk vector measuring intent evolution. **Critical difference:** DeepContext is a detection/monitoring system. It flags adversarial conversations but does not intervene in the model's internal activations. It does not steer or scale any refusal direction -- it sits outside the model as a classifier. Your idea would close this gap by feeding a cumulative risk signal back into the model's activation space.

---

### 3. VERY RELEVANT: Peak + Accumulation Scoring

- **Paper:** "Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection"
- **Authors:** J Alex Corll
- **Date:** February-March 2026, arXiv 2602.11247
- **Similarity: MODERATE (addresses cumulative risk scoring but not activation steering)**

Proposes a lightweight formula combining peak single-turn risk, persistence ratio, and category diversity to aggregate per-turn scores into a conversation-level risk score. **Critical difference:** This is a proxy-layer scoring formula (5 lines of code, no GPU needed). It is purely a detection metric and does not interact with model internals or refusal directions at all.

---

### 4. RELEVANT: Latent Adversarial Detection (LAD)

- **Paper:** "Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection"
- **Date:** April 30, 2026, arXiv 2604.28129
- **Similarity: MODERATE (uses activation-space signals across turns but for detection, not steering)**

Identifies "adversarial restlessness" in activation trajectories across multi-turn conversations. Uses trajectory scalar features (total path length in activation space) to detect attacks. **Critical difference:** This is a read-only probe -- it observes activations but does not write back into them. It detects but does not modulate refusal. Your idea would be the interventional counterpart to this detection-only approach.

---

### 5. RELEVANT: AlphaSteer (ICLR 2026)

- **Paper:** "AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint"
- **Authors:** Leheng Sheng, Changshuo Shen et al. (USTC)
- **Venue:** ICLR 2026
- **Similarity: MODERATE (principled activation steering, but per-query, not conversation-aware)**

Learns a refusal direction vector for malicious inputs and a null-space vector for benign inputs, with theoretical grounding for the utility-safety tradeoff. **Critical difference:** AlphaSteer operates per-input. It has no temporal/conversational component. The steering magnitude is learned per-query class, not dynamically scaled based on conversational risk accumulation.

---

### 6. RELEVANT: SafeThinker (January 2026)

- **Paper:** "SafeThinker: Reasoning about Risk to Deepen Safety Beyond Shallow Alignment"
- **Date:** January 2026, arXiv 2601.16506
- **Similarity: MODERATE (risk-tiered routing, but at the prompt level, not the activation level)**

Uses a gateway classifier to route queries into High-Risk (immediate refusal), Low-Risk (normal generation), or Uncertain-Risk (dynamic safety control) paths. **Critical difference:** SafeThinker's risk assessment is per-query and uses prompt-level routing, not activation-space scaling. It does not accumulate risk across turns or modulate a refusal direction vector.

---

### 7. CONTEXTUALLY IMPORTANT: Refusal Geometry Papers

**a) "The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence"**
- Wollschlager et al., ICML 2025, arXiv 2502.17420
- Shows refusal is governed by multi-dimensional polyhedral cones, not a single direction. Multiple representationally independent directions exist.

**b) "There Is More to Refusal in Large Language Models than a Single Direction"**
- Joad et al., February 2026, arXiv 2602.02132
- Finds 11 geometrically distinct refusal directions, but steering along any of them produces similar refusal-to-over-refusal tradeoffs (acts as a shared 1D control knob).

**c) "Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics"**
- Garcia-Ferrero et al., December 2025, arXiv 2512.16602
- Inference-time refusal steering using ridge-regularized vectors and LLM-as-judge scores. Per-topic, not per-turn or conversation-aware.

These papers provide the mechanistic foundation your idea would build on but none of them introduce a temporal/conversational dimension.

---

### 8. RELEVANT DETECTION/DEFENSE PAPERS (less directly related)

| Paper | Date | Key Idea | Gap vs. Your Proposal |
|---|---|---|---|
| **Refusal Tokens** (arXiv 2412.06748) | Aug 2025 | Prepend refusal tokens; threshold at inference | Per-query calibration, no turn accumulation |
| **R2D2** (family of works, 2024-2025) | Ongoing | Distribute refusal circuits across layers/tokens | Structural robustness, not dynamic modulation |
| **APST** (arXiv 2602.11786) | Feb 2026 | Repeated-inference stress testing | Evaluation framework, not a defense |
| **Efficient Refusal Ablation via Optimal Transport** (arXiv 2603.04355) | March 2026 | Optimal transport for refusal ablation | Removes refusal, opposite direction |
| **Temporal Context Awareness** (arXiv 2503.15560) | March 2025 | Defense framework for multi-turn manipulation | Prompt-level, not activation-level |

---

### 9. SPECIFIC SEARCHES: CRA / SafeProbing / APST

- **"CRA refusal activations 2026"**: No paper with that exact title/acronym was found in the LLM safety literature. The closest activation-related 2026 work is Anthropic's Natural Language Autoencoders (May 2026), which reads internal activations for interpretability but does not steer them.
- **"SafeProbing 2026 LLM"**: No paper with this exact name was found. The closest is the NC State work on identifying safety-critical LLM components and the JHU "JBDistill" renewable safety benchmarking framework (March 2026), neither of which involves probing for dynamic refusal modulation.
- **"Accelerated Prompt Stress Testing" (APST)**: Confirmed. arXiv 2602.11786 (February 2026) by researchers who formalize repeated-inference safety evaluation using Bernoulli/binomial models. This is an evaluation methodology, not a defense mechanism.

---

### GAP ANALYSIS: What No One Has Done

Your proposed idea sits at the intersection of three active but currently disconnected research threads:

| Thread | Representative Work | What It Does | What It Lacks |
|---|---|---|---|
| **A. Activation-space refusal steering** | RAS, AlphaSteer, Refusal Steering | Scales/steers refusal direction per-query | No conversation memory; stateless |
| **B. Cumulative multi-turn risk scoring** | DeepContext, Peak+Accumulation, LAD | Tracks risk accumulation across turns | Detection only; no intervention in activations |
| **C. Refusal geometry understanding** | Concept Cones, Joad et al. 2026 | Maps the geometric structure of refusal | Descriptive/analytical; no dynamic modulation |

**Your idea uniquely bridges A and B**: take the cumulative turn-level risk signal (thread B) and use it to dynamically scale the magnitude of a refusal activation direction (thread A), informed by the geometric understanding (thread C). This specific combination -- a closed-loop system where conversation-accumulated risk feeds back into activation-space refusal magnitude -- has no published instantiation as of May 2026.

The closest single paper is **RAS (KAIST, October 2025)**, which does risk-proportional activation steering but is stateless and single-turn. The second closest is **DeepContext (February 2026)**, which does stateful cumulative risk tracking but only for detection.

---

### Sources

- [RAS: Risk-adaptive Activation Steering](https://arxiv.org/abs/2510.13698)
- [AlphaSteer: ICLR 2026](https://arxiv.org/abs/2506.07022)
- [DeepContext: Stateful Multi-Turn Detection](https://arxiv.org/abs/2602.16935)
- [Peak + Accumulation Scoring](https://arxiv.org/abs/2602.11247)
- [Latent Adversarial Detection](https://arxiv.org/abs/2604.28129)
- [SafeThinker](https://arxiv.org/abs/2601.16506)
- [Refusal Steering (Garcia-Ferrero et al.)](https://arxiv.org/abs/2512.16602)
- [Geometry of Refusal: Concept Cones (ICML 2025)](https://arxiv.org/abs/2502.17420)
- [There Is More to Refusal than a Single Direction](https://arxiv.org/abs/2602.02132)
- [Refusal Tokens](https://arxiv.org/abs/2412.06748)
- [Efficient Refusal Ablation via Optimal Transport](https://arxiv.org/abs/2603.04355)
- [APST: Accelerated Prompt Stress Testing](https://arxiv.org/abs/2602.11786)
- [Temporal Context Awareness Defense](https://arxiv.org/abs/2503.15560)
- [R2D2 Robust Refusal Dynamic Defense](https://www.emergentmind.com/topics/robust-refusal-dynamic-defense-r2d2)
- [Anthropic NLA / Claude Interpretability](https://www.roborhythms.com/claude-knows-being-tested-interpretability-may-2026/)
- [JBDistill Renewable Safety Benchmarking (JHU)](https://hub.jhu.edu/2026/03/11/efficient-ai-safety-testing/)
- [NC State LLM Safety Components](https://news.ncsu.edu/2026/03/new-technique-addresses-llm-safety/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8295616d-cb18-438e-81d6-9ce217024f6b",
  "isSidechain": true,
  "agentId": "af14b787a68e72cb2",
  "requestId": "req_011Cb4RHezk4PhREehGuQajg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93c2f2a6-bd1d-4188-9811-85241aa7f23e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d94ff5-9a49-4477-8d1d-0a01d7a4ca27",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPTLVYEPjMhi8458zwtN3w",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4042,
      "cache_read_input_tokens": 24899,
      "output_tokens": 3055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4042
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3055,
          "cache_read_input_tokens": 24899,
          "cache_creation_input_tokens": 4042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4042,
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
