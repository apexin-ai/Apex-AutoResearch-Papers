# Research conversation: I'm reviewing a paper proposal about "GranRoute" — learning to route retrieval configurations (granularity + context bud

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 88
- **Recorded user turns:** 1
- **Tool calls:** 40
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a091ca136193f2c66.jsonl`
- **Structured JSON:** [`94baf0cf05c4585fb77e.json`](../../sessions/94/94baf0cf05c4585fb77e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

88 recorded events

### User

_source line 1 · 2026-05-11T23:38:10.092Z_

I'm reviewing a paper proposal about "GranRoute" — learning to route retrieval configurations (granularity + context budget) for repository-level code repair. I need to find competitors the proposal may have missed. Search for:

1. Search: "adaptive retrieval configuration code repair 2025 2026" — are there other papers that adaptively select retrieval strategies for code repair?

2. Search: "retrieval routing LLM code 2026" — anything about routing retrieval for code tasks?

3. Search: "configuration selection software engineering LLM 2025 2026" — automatic configuration selection for SE agents?

4. Search: "context window optimization code repair 2025 2026" — optimizing context for code repair?

5. Search: "SWE-bench adaptive agent 2026" — any SWE-bench agents that adaptively change their strategies?

6. Search: "meta-learning code repair retrieval 2025 2026" — meta-learning approaches for code repair?

7. Search: "dynamic fault localization LLM 2026" — dynamic/adaptive fault localization?

8. Search: "Agentless adaptive configuration 2026" — any work extending Agentless with adaptive configs?

9. Search for "MASAI" or "CodeR" or "AutoCodeRover adaptive" — known SWE-bench agents that might have adaptive retrieval.

10. Search: "learn to retrieve code generation 2025 2026" — learning retrieval strategies for code tasks.

For each search, report the most relevant results. Focus on papers from 2025-2026 that are NOT already cited in the proposal. The cited papers include: RouteLLM, RADAR, BEST-Route, Route-To-Reason, LTRR, Triage, SIADAFIX, AdaPatcher, AdaEdit, SWEzze, SWE-Pruner, CodeScout, ARISE, RPO, DRO, ReCode, RGFL.

Report concisely: paper title, venue/arXiv, and why it's relevant or not.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "ecfaed85-11ae-4592-a9a4-0bffa974b66b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:38:10.096Z_

```json
{
  "parentUuid": "ecfaed85-11ae-4592-a9a4-0bffa974b66b",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
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
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "5020d014-a0b8-45c6-bc9b-64354b5ee170",
  "timestamp": "2026-05-11T23:38:10.096Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:38:15.716Z_



I'll conduct all 10 searches in parallel to find potential competitors for the GranRoute proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5020d014-a0b8-45c6-bc9b-64354b5ee170",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMYn9unDyeDaWJaSLv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "376c1ae6-944b-4445-94c7-b03198b6fa57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaTJgg8PnZecyh1xDsPtDb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1024,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T23:38:15.803Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013gXbGFJxJPHmk9qexnv6s3`</summary>

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
  "parentUuid": "376c1ae6-944b-4445-94c7-b03198b6fa57",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMYn9unDyeDaWJaSLv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48c33248-f53e-4a41-b7dd-9c19f842b86e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaTJgg8PnZecyh1xDsPtDb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1024,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-11T23:38:15.809Z_

<details><summary>↩ Tool result · `toolu_013gXbGFJxJPHmk9qexnv6s3`</summary>

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
  "parentUuid": "48c33248-f53e-4a41-b7dd-9c19f842b86e",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "f6e3cb9e-ecfa-453b-8f55-a3d1e413f370",
  "sourceToolAssistantUUID": "48c33248-f53e-4a41-b7dd-9c19f842b86e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:38:18.607Z_



Now let me run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6e3cb9e-ecfa-453b-8f55-a3d1e413f370",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMyWgrDMzWd87vLviJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a46f56bf-9b27-4464-9304-43540bcf66b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkVpyKoeVFFv9QoDX5vktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 7 · 2026-05-11T23:38:19.157Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0153viw5N1aiiBQHwnVakxMn`</summary>

```json
{
  "query": "adaptive retrieval configuration code repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a46f56bf-9b27-4464-9304-43540bcf66b8",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMyWgrDMzWd87vLviJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d4fd765-e1ec-494c-a780-eedbf4467dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkVpyKoeVFFv9QoDX5vktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 8 · 2026-05-11T23:38:19.619Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012kuNGrP4eqfxuhxwTQVbef`</summary>

```json
{
  "query": "retrieval routing LLM code 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d4fd765-e1ec-494c-a780-eedbf4467dc2",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMyWgrDMzWd87vLviJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6726bae-30e2-4cd7-ae16-1e9b2863b246",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkVpyKoeVFFv9QoDX5vktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 9 · 2026-05-11T23:38:20.561Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NHCAQkzBVhaGPnvnAnTx55`</summary>

```json
{
  "query": "configuration selection software engineering LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6726bae-30e2-4cd7-ae16-1e9b2863b246",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMyWgrDMzWd87vLviJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d446fc0-30d4-47b1-ab63-2b78012c1421",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkVpyKoeVFFv9QoDX5vktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 10 · 2026-05-11T23:38:21.057Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DoaKHAFGrn5wP4394xQjNw`</summary>

```json
{
  "query": "context window optimization code repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d446fc0-30d4-47b1-ab63-2b78012c1421",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMyWgrDMzWd87vLviJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e31d239-333a-421e-8141-c123bdda6afd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkVpyKoeVFFv9QoDX5vktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 11 · 2026-05-11T23:38:21.506Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bh76EguZxs3mPt97Fx2rDL`</summary>

```json
{
  "query": "SWE-bench adaptive agent 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e31d239-333a-421e-8141-c123bdda6afd",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMyWgrDMzWd87vLviJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "345efb33-04d8-415a-8108-76354bde726e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkVpyKoeVFFv9QoDX5vktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 12 · 2026-05-11T23:38:21.978Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QrCVL4am7uJ6VADowYZhMZ`</summary>

```json
{
  "query": "meta-learning code repair retrieval 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "345efb33-04d8-415a-8108-76354bde726e",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMyWgrDMzWd87vLviJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97079d5b-edd5-4c8f-9cfd-6dac76c78740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkVpyKoeVFFv9QoDX5vktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 13 · 2026-05-11T23:38:22.457Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XVCNvirb6AegNXX7rs1J1u`</summary>

```json
{
  "query": "dynamic fault localization LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97079d5b-edd5-4c8f-9cfd-6dac76c78740",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMyWgrDMzWd87vLviJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43b56fcd-b68f-48b0-9b28-73e3a3731f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkVpyKoeVFFv9QoDX5vktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 14 · 2026-05-11T23:38:23.389Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LSSK5Bt743VYp5XNxZaQvi`</summary>

```json
{
  "query": "Agentless adaptive configuration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43b56fcd-b68f-48b0-9b28-73e3a3731f77",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMyWgrDMzWd87vLviJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2ee5f96-eb90-4655-ab88-56f3d358e69e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkVpyKoeVFFv9QoDX5vktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 15 · 2026-05-11T23:38:24.341Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kb9hvWgvnJAU669Zd25yKi`</summary>

```json
{
  "query": "MASAI CodeR AutoCodeRover adaptive retrieval SWE-bench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2ee5f96-eb90-4655-ab88-56f3d358e69e",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMyWgrDMzWd87vLviJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83797a16-6e88-4842-9b47-846e01c4c7a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkVpyKoeVFFv9QoDX5vktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 16 · 2026-05-11T23:38:24.674Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CurJhYYngmApyMjEYp7LEV`</summary>

```json
{
  "query": "learn to retrieve code generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83797a16-6e88-4842-9b47-846e01c4c7a1",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfMyWgrDMzWd87vLviJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e43d2aa3-8c37-487a-b6c1-ed13f67c5b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkVpyKoeVFFv9QoDX5vktL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 9247,
      "output_tokens": 487,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1415
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 487,
          "cache_read_input_tokens": 9247,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1415,
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

_source line 17 · 2026-05-11T23:38:27.213Z_

<details><summary>↩ Tool result · `toolu_0153viw5N1aiiBQHwnVakxMn`</summary>

```text
Web search results for query: "adaptive retrieval configuration code repair 2025 2026"

Links: [{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/html/2603.01048v1"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-026-09751-w"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"[2503.06510] Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://arxiv.org/abs/2503.06510"},{"title":"A survey on large language models for software engineering","url":"https://files.sciengine.com/gridfs/1987700388211458048/edit_SCIS-2025-0100-appendix.pdf"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"}]

Based on the web search results, here's what I found about adaptive retrieval configuration and code repair research from 2025-2026:

## Key Research Areas

**Retrieval-Augmented Generation (RAG) for Code Repair:**

RAG refers to augmenting the LLM's input with external knowledge (such as relevant code snippets, documentation, or historical fixes), and this has become a central approach in automated program repair. Several recent systems demonstrate this:

1. **RELREPAIR** - This approach focuses on retrieving highly relevant, project-specific data essential for effective program repair. The system uses adaptive adjustment of parameters based on their contributions toward minimizing the gap between current similarity and predefined target similarity.

2. **ReCode** - By integrating algorithmic categorization with the model's semantic modeling towards the defective code, ReCode significantly enhances the contextual relevance of retrieved in-context exemplars and supports more accurate and adaptive code repair generation.

3. **RepoRepair** - This system uses a streamlined two-stage pipeline—first retrieving relevant files via embedding models, then iteratively generating repairs based on the top retrieved files.

**Broader Landscape:**

Recent surveys map the design space across four paradigms (fine-tuning, prompting, procedural pipelines, and agentic frameworks), incorporating cross-cutting Retrieval Augmented Generation (RAG) and Analysis Augmented Generation (AAG) enhancements, covering papers from January 2022 to June 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d4fd765-e1ec-494c-a780-eedbf4467dc2",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "d7123d7f-c7dd-410a-88e8-599afd074fd8",
  "sourceToolAssistantUUID": "0d4fd765-e1ec-494c-a780-eedbf4467dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-11T23:38:28.059Z_

<details><summary>↩ Tool result · `toolu_012kuNGrP4eqfxuhxwTQVbef`</summary>

```text
Web search results for query: "retrieval routing LLM code 2026"

Links: [{"title":"MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents","url":"https://arxiv.org/html/2605.00356v1"},{"title":"GitHub - ulab-uiuc/LLMRouter: LLMRouter: An Open-Source Library for LLM Routing · GitHub","url":"https://github.com/ulab-uiuc/LLMRouter"},{"title":"Multi-LLM Tools for Production: Routing, Evals, and Failover in 2026 | Logic","url":"https://logic.inc/resources/best-tools-multi-llm-applications"},{"title":"Router - Load Balancing | liteLLM","url":"https://docs.litellm.ai/docs/routing"},{"title":"An LLM-Based Multi-Path Question Answering System with XGBoost Routing and Threshold-Based Refusal","url":"https://www.mdpi.com/2079-9292/15/9/1845"},{"title":"llm-wiki · GitHub","url":"https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"},{"title":"State of AI Engineering | Datadog","url":"https://www.datadoghq.com/state-of-ai-engineering/"},{"title":"Training-Free LLM Routing for Knowledge Graph Retrieval ...","url":"https://aclanthology.org/2025.findings-emnlp.606.pdf"},{"title":"RAGRouter: Learning to Route Queries to Multiple ...","url":"https://arxiv.org/pdf/2505.23052"},{"title":"OpenRouter","url":"https://openrouter.ai/"}]

Based on the web search results, here's what I found about retrieval routing for LLMs in 2026:

## Key Developments in Retrieval Routing

**MemRouter** - A recent system that outperforms LLM-based memory managers on every question category while reducing memory-management latency from 970 ms to 58 ms. The code is available on GitHub.

**RAGRouter** - A system designed to route queries across LLMs by modeling key factors that affect post-retrieval performance, incorporating a document encoder and cross encoder to capture document semantics and query interactions, and assigning each LLM a RAG capability embedding.

**SkewRoute** - A training-free LLM routing approach for knowledge graph retrieval-augmented generation that utilizes the score skewness of retrieved contexts.

## LLMRouter Library

LLMRouter supports over 16 routing models, organized into four major categories—single-round routers, multi-round routers, agentic routers, and personalized routers—covering strategies such as KNN, SVM, MLP, Matrix Factorization, Elo Rating, and graph-based routing. In May 2026, RouteProfile was released as a general framework for designing LLM profiles for routing, supporting flat, embedding-based, text-GNN, and trainable GNN profiles.

## Production Considerations

Teams moving from experimentation to production are managing model fleets, orchestration frameworks, tool calls, long prompts, retries, and multiple service boundaries—including routing, life cycle management, capacity planning, cost control, and debugging.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6726bae-30e2-4cd7-ae16-1e9b2863b246",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "46e94159-9185-42ac-8478-872f18a7cd7f",
  "sourceToolAssistantUUID": "f6726bae-30e2-4cd7-ae16-1e9b2863b246",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-11T23:38:29.013Z_

<details><summary>↩ Tool result · `toolu_01Bh76EguZxs3mPt97Fx2rDL`</summary>

```text
Web search results for query: "SWE-bench adaptive agent 2026"

Links: [{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? | OpenReview","url":"https://openreview.net/forum?id=9R2iUHhVfr"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"[2509.16941] SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?","url":"https://arxiv.org/abs/2509.16941"},{"title":"[Leaderboard] AI Agent Framework Scorecard 2026 | Rapid Claw","url":"https://rapidclaw.dev/blog/ai-agent-benchmarks-2026"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"}]

Based on the search results, here's what I found about SWE-bench adaptive agents in 2026:

## Current SWE-Bench Landscape in 2026

Claude Opus 4.7 leads SWE-bench Verified at 87.6%, with GPT-5.3 Codex scoring 85.0% and Claude Opus 4.5 at 80.9%.

### Key Developments:

**Adaptive Agent Frameworks**: The Verified leaderboard features results from a wide variety of AI coding systems, from simple LM agent loops to RAG systems to multi-rollout and review type systems, and to make apples-to-apples comparisons easier, language models are evaluated using mini-SWE-agent in a minimal bash environment with just a simple ReAct agent loop.

**More Challenging Benchmarks**: SWE-Bench Pro has been introduced as a substantially more challenging benchmark that builds upon SWE-BENCH best practices and contains 1,865 problems sourced from 41 actively maintained repositories spanning business applications, B2B services, and developer tools.

### Important Caveats:

Berkeley/RDI broke all 8 major benchmarks via reward hacking on April 12, 2026, and third-party Epoch AI / BenchLM scores are preferred. Additionally, frontier models are improving fast enough that static benchmarks saturate within months of release, and frameworks and scaffolding now contribute as much as the underlying model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "345efb33-04d8-415a-8108-76354bde726e",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "babb6463-ed33-4449-af26-12772d380c71",
  "sourceToolAssistantUUID": "345efb33-04d8-415a-8108-76354bde726e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-11T23:38:29.165Z_

<details><summary>↩ Tool result · `toolu_01QrCVL4am7uJ6VADowYZhMZ`</summary>

```text
Web search results for query: "meta-learning code repair retrieval 2025 2026"

Links: [{"title":"How Meta Used AI to Map Tribal Knowledge in Large-Scale Data Pipelines - Engineering at Meta","url":"https://engineering.fb.com/2026/04/06/developer-tools/how-meta-used-ai-to-map-tribal-knowledge-in-large-scale-data-pipelines/"},{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"},{"title":"Explainable Recommendation of Software Vulnerability Repair Based on Metadata Retrieval and Multifaceted LLMs","url":"https://www.mdpi.com/2504-4990/7/4/149"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/abs/2510.04905"},{"title":"Peer-aided repairer: empowering large language models to repair advanced student assignments | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10716-z"},{"title":"[2509.02330] ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2509.02330"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"RESCUE: Retrieval Augmented Secure Code Generation","url":"https://www.researchgate.net/publication/396747221_RESCUE_Retrieval_Augmented_Secure_Code_Generation"}]

Based on the search results, here are the key findings on meta-learning, code repair, and retrieval from 2025-2026:

## Recent Developments in Code Repair with Retrieval

Recent studies have demonstrated impressive results in utilizing Large Language Models (LLMs) for software bug fixing. Several approaches have emerged combining retrieval mechanisms with code repair:

### ReAPR: Retrieval-Augmented Program Repair
ReAPR is an approach for automatic program repair via retrieval-augmented large language models published in 2025.

### ReCode: Fine-Grained Retrieval Strategies
ReCode is a fine-grained retrieval-augmented in-context learning framework designed for accurate and efficient code repair. Conventional retrieval strategies, which are often based on holistic code-text embeddings, fail to capture the structural intricacies of code, resulting in suboptimal retrieval quality.

### Vulnerability Repair with Metadata Retrieval
Key factors in retrieval-based code repair include the retrieval of the most relevant context to a specific vulnerable code snippet, augmenting LLM prompts with the retrieved context, and the generated artifact form. Metadata-driven retrieval is noted as the best-performing retrieval strategy for certain use cases.

### Broader Trends in LLM-Based APR
Recent LLM-based APR systems are categorized into four paradigms, with fine-tuning delivering strong task alignment at high training cost, prompting enabling rapid deployment, procedural pipelines offering reproducible control, and agentic frameworks tackling multi-hunk or cross-file bugs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97079d5b-edd5-4c8f-9cfd-6dac76c78740",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "b78130be-66d2-4c0a-b70b-195bb8259b32",
  "sourceToolAssistantUUID": "97079d5b-edd5-4c8f-9cfd-6dac76c78740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-11T23:38:30.093Z_

<details><summary>↩ Tool result · `toolu_01DoaKHAFGrn5wP4394xQjNw`</summary>

```text
Web search results for query: "context window optimization code repair 2025 2026"

Links: [{"title":"GitHub - mksglu/context-mode: Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 15 platforms · GitHub","url":"https://github.com/mksglu/context-mode"},{"title":"Context Window Optimization: Techniques, Benchmarks, and Costs","url":"https://www.statsig.com/perspectives/context-window-optimization-techniques"},{"title":"Context Window Optimization Strategies | DataHub","url":"https://datahub.com/blog/context-window-optimization/"},{"title":"context-optimization · GitHub Topics · GitHub","url":"https://github.com/topics/context-optimization"},{"title":"Mastering Claude's Context Window: A 2025 Deep Dive","url":"https://sparkco.ai/blog/mastering-claudes-context-window-a-2025-deep-dive"},{"title":"GitHub - mksglu/context-mode: Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 14 platforms · GitHub","url":"https://github.com/mksglu/context-mode/tree/main"},{"title":"AI Agent Context Compression: Strategies for Long-Running Sessions | Zylos Research","url":"https://zylos.ai/research/2026-02-28-ai-agent-context-compression-strategies"},{"title":"AI Context Windows: 4K vs 128K vs 1M vs 10M Tokens (2026) | Local AI Master","url":"https://localaimaster.com/models/context-windows-coding-explained"},{"title":"Effective context engineering for AI agents","url":"https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"},{"title":"What Is Context Window in AI? The Simple Guide Everyone Needs in 2026","url":"https://gleecus.com/blogs/what-is-context-window-in-ai-guide-2026/"}]

Based on the search results, here's what I found regarding context window optimization and code repair in 2025-2026:

## Key Developments in Context Window Optimization (2025-2026)

### Practical Tools and Frameworks

Context-mode is a tool for context window optimization for AI coding agents that automatically repairs missing bindings through a postinstall script and runtime hook, eliminating the need for manual npm rebuild. The tool requires OpenClaw gateway (version >2026.1.29) and Node.js 22+, and runs as a native OpenClaw gateway plugin targeting Pi Agent sessions.

### Advanced Compression Techniques

In 2025–2026, the field has converged on concrete compression techniques including anchored iterative summarization, failure-driven guideline optimization (ACON), and provider-native compaction APIs. 

ACON (Agent Context Optimization) treats compression as an optimization problem through paired trajectory analysis and failure analysis, achieving 26–54% reduction in peak token usage while preserving 95%+ accuracy.

### Anthropic's Native Solutions

Anthropic's compaction API (compact-2026-01-12) provides production-ready automatic compaction that works across Claude API, AWS Bedrock, Google Vertex AI, and Microsoft Foundry.

### Best Practices for 2025

Optimizing Claude's context window in 2025 involves strategic approaches focusing on maximizing context quality through advanced context management tools, dynamic context editing, efficient memory management, and robust tool calling systems. Context should be relevant, accurate, and current, involving removal of outdated logs, irrelevant commands, and any information that does not directly contribute to the current task.

### Industry Shift

The industry is shifting from expanding context windows to smarter context management, with 2026 trends suggesting context window size is plateauing as focus shifts to inference-time scaling, hybrid compression+caching, and memory-augmented architectures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e31d239-333a-421e-8141-c123bdda6afd",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "44794471-aff9-4839-978b-35bbd9ecb978",
  "sourceToolAssistantUUID": "1e31d239-333a-421e-8141-c123bdda6afd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-11T23:38:30.562Z_

<details><summary>↩ Tool result · `toolu_01NHCAQkzBVhaGPnvnAnTx55`</summary>

```text
Web search results for query: "configuration selection software engineering LLM 2025 2026"

Links: [{"title":"Enterprise Local LLM Deployment: vLLM, GPUs ...","url":"https://www.sitepoint.com/the-2026-definitive-guide-to-running-local-llms-in-production/"},{"title":"Best LLM for Coding in 2026: Ranked by Real Benchmarks | WhatLLM.org","url":"https://whatllm.org/best-llm-for-coding"},{"title":"Ultimate Guide - The Best Open Source LLM for Engineering in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLM-for-engineering"},{"title":"Best LLM for Coding in 2026: Why There's No Single Winner","url":"https://www.decodesfuture.com/articles/best-llm-for-coding-2026-review"},{"title":"My LLM coding workflow going into 2026 - by Addy Osmani","url":"https://addyo.substack.com/p/my-llm-coding-workflow-going-into"},{"title":"My LLM coding workflow going into 2026 | by Addy Osmani | Medium","url":"https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"LLM Benchmarks 2026: 30+ Models Ranked — MMLU, SWE-bench, Arena Elo & Pricing","url":"https://iternal.ai/llm-selection-guide"},{"title":"Evaluation of LLM-Based Software Engineering Tools: Practices, Challenges, and Future Directions","url":"https://arxiv.org/html/2604.24621v1"},{"title":"Best LLMs for Coding in 2026: Top 15 Models Compared","url":"https://www.edenai.co/post/best-llms-for-coding"}]

Here are the search results for "configuration selection software engineering LLM 2025 2026":

## Key Findings

**Model Selection Architecture:**
The optimal architecture in 2026 routes different requests to different models based on task complexity, latency requirements, and cost constraints. No single model dominates every task.

**Top Models for Software Engineering:**
The best LLMs for software engineering in 2026 are Claude Opus 4.5, Gemini 3.1 Pro, Minimax, M2.5, GPT-5.2, and GLM-5. The top three picks for 2026 are moonshotai/Kimi-Dev-72B, Qwen/Qwen3-Coder-480B-A35B-Instruct, and zai-org/GLM-4.5-Air.

**Configuration for LLM Deployment:**
Hardware selection includes H100 vs A100 vs RTX 4090 clusters, inference engine selection (vLLM vs TGI vs TensorRT-LLM), and observability pipelines. The disaggregated prefill/decode architecture, introduced in vLLM's 2025-2026 releases, separates the compute-intensive prompt processing phase from the memory-bandwidth-intensive token generation phase, which allows different hardware or scheduling policies for each phase, improving overall GPU utilization.

**Open-Source vs. Proprietary Gap:**
The gap between open-source and proprietary has effectively closed for coding tasks, with MiniMax M2.5 achieving 80.2% on SWE-bench Verified, matching Claude Opus 4.6 (80.8%).

**LLM Selection for Coding Workflows:**
Part of the workflow is choosing the model or service best suited to each task, and it can be valuable to even try two or more LLMs in parallel to cross-check how they might approach the same problem differently.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d446fc0-30d4-47b1-ab63-2b78012c1421",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "92a8782a-b89f-423c-ace6-018e012cf119",
  "sourceToolAssistantUUID": "6d446fc0-30d4-47b1-ab63-2b78012c1421",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-11T23:38:30.947Z_

<details><summary>↩ Tool result · `toolu_01LSSK5Bt743VYp5XNxZaQvi`</summary>

```text
Web search results for query: "Agentless adaptive configuration 2026"

Links: [{"title":"12 Best Network Configuration Management Software in 2026 MSP Blog - Domotz blog for MSPs","url":"https://blog.domotz.com/all/best-network-configuration-management-software/"},{"title":"Venice secures $33m to modernise enterprise access","url":"https://fintech.global/2026/02/19/venice-secures-33m-to-modernise-enterprise-access/"},{"title":"Top 10 Agentless Monitoring Tools for IT Teams in 2026 MSP Blog - Domotz blog for MSPs","url":"https://blog.domotz.com/all/agentless-monitoring-tools/"},{"title":"Illumio Delivers the First Platform to Combine Agentless Visibility and Breach Containment for Hybrid Environments - Illumio News | Illumio","url":"https://www.illumio.com/news/illumio-delivers-agentless-visibility-and-breach-containment-for-hybrid-environments"},{"title":"Top 13 MFA Providers in 2026: Features, Pricing & Comparison","url":"https://www.miniorange.com/blog/mfa-providers/"},{"title":"Algomox Blog | Why Your Configuration Management Needs Both Agent and Agentless Modes—Driven by AI","url":"https://www.algomox.com/resources/blog/agent_vs_agentless_configuration_ai_management/"},{"title":"Agentless Asset & Vulnerability Discovery: Complete Guide (2026)","url":"https://www.secure.com/blog/infrastructure-security/agentless-asset-vulnerability-discovery"},{"title":"Fortinet fights quantum harvesting and shadow AI with new updates - SDxCentral","url":"https://www.sdxcentral.com/news/fortinet-fights-quantum-harvesting-and-shadow-ai-with-new-updates/"},{"title":"Download HPE Agentless Management Software (AMS) Solution | HPE Store","url":"https://buy.hpe.com/us/en/software/server-management-software/server-ilo-management/ilo-management-engine/hpe-agentless-management/p/5219980"},{"title":"AI Agent Security: Why Only Microsegmentation Can Stop Them","url":"https://www.elisity.com/blog/ai-agent-network-security-microsegmentation-2026"}]

Based on the web search results, here's what I found about "Agentless adaptive configuration 2026":

## Key Findings

**Agentless Configuration Management Trends:**

Agentless monitoring tools are now the standard for modern IT environments. In 2026, networks are larger, more distributed, and filled with devices you cannot install agents on.

**AI-Driven Adaptive Approaches:**

AI orchestration becomes crucial in determining the optimal approach for different layers of the infrastructure stack, analyzing factors such as deployment frequency, infrastructure lifetime, interdependency complexity, and operational patterns. Machine learning algorithms can process historical scaling patterns, resource utilization trends, and operational metrics to predict when different parts of the infrastructure will benefit from each approach. The AI system can automatically transition infrastructure components between agent and agentless management modes as their characteristics change.

**Adaptive MFA and Security:**

In the security realm, SecureAuth specializes in context-aware adaptive MFA that analyzes behavioral biometrics, IP reputation, device fingerprinting, and environmental signals to dynamically adjust authentication requirements across complex hybrid environments.

**Hybrid Configuration Management:**

The future of configuration management lies not in choosing between agent and agentless approaches, but in leveraging AI to orchestrate both methodologies in optimal combinations that address specific operational requirements, security constraints, performance demands, and business objectives.

The 2026 trend appears to be toward intelligent, adaptive systems that automatically optimize between agentless and agent-based approaches based on real-time infrastructure needs and AI analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2ee5f96-eb90-4655-ab88-56f3d358e69e",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "08dc8a1f-4851-4217-932c-f00a89d38d8e",
  "sourceToolAssistantUUID": "c2ee5f96-eb90-4655-ab88-56f3d358e69e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-11T23:38:31.142Z_

<details><summary>↩ Tool result · `toolu_01XVCNvirb6AegNXX7rs1J1u`</summary>

```text
Web search results for query: "dynamic fault localization LLM 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"LLM4FL: Multi-Agent Repository-Level Software Fault Localization via Graph-Based Retrieval and Iterative Refinement | OpenReview","url":"https://openreview.net/forum?id=z91EvZbSI1"},{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"[2604.05481] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481"},{"title":"Large Language Models for Test-Free Fault Localization Aidan Z.H. Yang","url":"https://aidanby.github.io/files/icse24.pdf"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/html/2403.16362v1"},{"title":"Improving LLM-Based Fault Localization with External Memory and Project Context","url":"https://arxiv.org/html/2506.03585v1"},{"title":"[2403.16362] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/abs/2403.16362"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3660771"},{"title":"FlexFL: Flexible and Effective Fault Localization with Open- ...","url":"https://arxiv.org/pdf/2411.10714"}]

I found several recent papers and research on dynamic fault localization using LLMs in 2026. Here are the key findings:

## Recent 2026 Research on LLM-Based Fault Localization

### ICST 2026 Paper: Robustness of LLMs' Fault Localizability

A major empirical investigation evaluates LLMs' ability to reason about code for fault localization by designing an automated evaluation framework that dynamically generates controlled, previously unseen fault localization tasks. The research addresses dataset contamination by dynamically injecting faults into real-world seed programs to create unseen fault localization tasks using classical mutation testing.

Key findings include: Semantic-preserving mutations cause an LLM to fail to localize the same fault it correctly localized earlier in 78% of cases, suggesting that LLMs' code-reasoning is tied to code features irrelevant to semantics.

### LLM-Based Program Repair Context Study

A large-scale empirical study examines how Fault Localization impacts LLM-based Automated Program Repair, investigating how much localization is needed and whether additional context beyond the predicted buggy location is beneficial. File-level localization is the dominant factor, yielding a 15-17x improvement over a no-file baseline.

### Other 2026 Advances

Recent work also includes projects like MemFL, which incorporates project-specific knowledge through external memory knowledge editing using both static memory and dynamic memory, and LLM4FL, a multi-LLM-agent-based fault localization approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43b56fcd-b68f-48b0-9b28-73e3a3731f77",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "67cd5ef6-2daf-450d-a3da-4b3c597df4e9",
  "sourceToolAssistantUUID": "43b56fcd-b68f-48b0-9b28-73e3a3731f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-11T23:38:32.931Z_

<details><summary>↩ Tool result · `toolu_01CurJhYYngmApyMjEYp7LEV`</summary>

```text
Web search results for query: "learn to retrieve code generation 2025 2026"

Links: [{"title":"Context-Augmented Code Generation Using Programming Knowledge Graphs | OpenReview","url":"https://openreview.net/forum?id=EHfn5fbFHw"},{"title":"AI Code Generators: The Future of Software Development","url":"https://zencoder.ai/blog/ai-code-generators-future-software-development"},{"title":"[2504.17192] Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning","url":"https://arxiv.org/abs/2504.17192"},{"title":"How I’m Learning to Code in 2026 (And Why Everything Changed) | by ThinkChain | Medium","url":"https://medium.com/@thinkchain/how-im-learning-to-code-in-2026-and-why-everything-changed-de1a6d40b47e"},{"title":"How I’m Learning to Code in the AI Age (2025-2026 Edition) - DEV Community","url":"https://dev.to/the_mj_super/how-im-learning-to-code-in-the-ai-age-2025-2026-edition-3b8l"},{"title":"AI-Generated Code Statistics 2026: Can AI Replace Your Development Team?","url":"https://www.netcorpsoftwaredevelopment.com/blog/ai-generated-code-statistics"},{"title":"How to Learn Coding in 2026 (Coding Roadmap 2026): What to Learn, What to Ignore & How to Win - Devnquizi - Medium","url":"https://medium.com/@devnquizi/how-to-learn-coding-in-2026-coding-roadmap-2026-what-to-learn-what-to-ignore-how-to-win-27df270eb668"},{"title":"How to Learn Coding in 2026: A Practical Guide That Actually Works - DEV Community","url":"https://dev.to/farhadrahimiklie/how-to-learn-coding-in-2026-a-practical-guide-that-actually-works-3f2l"},{"title":"10 Best Generative AI Code Generation Tools to Try in 2026","url":"https://zencoder.ai/blog/generative-ai-code-generation-tools"},{"title":"LLM-Generated Code in 2025: Trends and Predictions - Revelo","url":"https://www.revelo.com/blog/llm-code-generation-2025-trends-predictions-human-data"}]

Here's a summary of what the web search found on learning, code generation, and retrieval-based approaches for 2025-2026:

## Code Generation and Retrieval Research

A novel framework has been developed that leverages a Programming Knowledge Graph to semantically represent and retrieve code, enabling fine-grained code retrieval by focusing on the most relevant segments while reducing irrelevant context through a tree-pruning technique.

Another approach, called PaperCoder, is a multi-agent LLM framework that transforms machine learning papers into operational code repositories, operating in three stages: planning (constructing a high-level roadmap and designing system architecture), analysis (interpreting implementation-specific details), and generation (producing modular, dependency-aware code).

## Current State of Code Generation in 2025-2026

As of early 2026, the share of AI-generated code has surged to near 50%, with adoption curves steepening faster than initial projections. One report suggests that nearly half of all code in 2025 was AI-generated or assisted.

## Learning to Code with AI Tools

Learning to code in 2026 is fundamentally different from how it was taught in the past, with old advice to finish a language, watch full tutorials, and memorize syntax no longer matching reality, as what matters is how effectively you can think, debug, and build rather than how much syntax you know.

The developers who master fundamentals AND AI tools are unstoppable, while ones who only know prompting will struggle as AI gets better.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e43d2aa3-8c37-487a-b6c1-ed13f67c5b9e",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "4f221e3a-f7e8-4607-a9f7-5d486875f533",
  "sourceToolAssistantUUID": "e43d2aa3-8c37-487a-b6c1-ed13f67c5b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T23:38:34.050Z_

<details><summary>↩ Tool result · `toolu_01Kb9hvWgvnJAU669Zd25yKi`</summary>

```text
Web search results for query: "MASAI CodeR AutoCodeRover adaptive retrieval SWE-bench"

Links: [{"title":"MASAI: Modular Architecture for Software-engineering AI Agents","url":"https://arxiv.org/pdf/2406.11638"},{"title":"GitHub - AutoCodeRoverSG/auto-code-rover: A project structure aware autonomous software engineer aiming for autonomous program improvement. Resolved 37.3% tasks (pass@1) in SWE-bench lite and 46.2% tasks (pass@1) in SWE-bench verified with each task costs less than $0.7. · GitHub","url":"https://github.com/AutoCodeRoverSG/auto-code-rover"},{"title":"MASAI: Modular Architecture for Software-engineering AI Agents","url":"https://openreview.net/pdf?id=NSINt8lLYB"},{"title":"AutoCodeRover: Autonomous Program Improvement","url":"https://arxiv.org/html/2404.05427v1"},{"title":"AutoCodeRover: Autonomous Program Improvement Yuntong Zhang","url":"https://arxiv.org/pdf/2404.05427"},{"title":"AutoCodeRover: Autonomous Program Improvement Yuntong Zhang","url":"https://haifengruan.com/assets/pdf/autocoderover_issta24.pdf"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"Why AutoCodeRover not mentioned? · Issue #115 · SWE-bench/SWE-bench","url":"https://github.com/SWE-bench/SWE-bench/issues/115"},{"title":"GitHub - itsnauman/autocoderover: A project structure aware autonomous software engineer aiming for autonomous program improvement. Resolved 15.95% tasks in full SWE-bench","url":"https://github.com/itsnauman/autocoderover"},{"title":"SWE-bench Results Viewer","url":"https://www.swebench.com/viewer.html"}]

Based on the search results, here's what I found about these systems:

## MASAI (Modular Architecture for Software-engineering AI Agents)

MASAI modularizes the problem into sub-problems and delegates them to different sub-agents, with a MASAI agent being a composition of several MASAI sub-agents. MASAI achieves the highest resolution rate of 28.33% on SWE-bench Lite, establishing state-of-the-art on the benchmark leaderboard alongside CodeR.

## CodeR

CodeR is a multi-agent solution which reproduces and resolves the issue iteratively, using BM25 along with test coverage statistics for fault localization.

## AutoCodeRover

AutoCodeRover provides the LLM with code search APIs to navigate the codebase and collect relevant context, then the LLM tries to write a patch based on retrieved context. AutoCodeRover's code search APIs are program structure aware—it searches for relevant code context (methods/classes) in the abstract syntax tree instead of searching over files by plain string matching. AutoCodeRover achieved 30.67% efficacy (pass@1) on SWE-bench-lite as of June 20, 2024.

## Adaptive Retrieval

AutoCodeRover integrates AST traversal, iterative retrieval, and SBFL (Spectrum-Based Fault Localization) for enhanced performance, representing an approach to adaptive retrieval in code generation systems.

All three systems are evaluated on the SWE-bench benchmark, which consists of real-world GitHub issues requiring code generation and modification capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83797a16-6e88-4842-9b47-846e01c4c7a1",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "bc02c949-5e69-495c-9cde-3a9ae367428e",
  "sourceToolAssistantUUID": "83797a16-6e88-4842-9b47-846e01c4c7a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-11T23:38:36.658Z_

Let me run some more targeted follow-up searches to find specific papers that might be direct competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc02c949-5e69-495c-9cde-3a9ae367428e",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfPKE8PrRVVYWmUTKHb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34875b77-3c15-43be-89f2-7c73b12a9850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mvSJMvvkZTLFLkPiqk5dy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 8871,
      "cache_read_input_tokens": 10662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8871,
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

_source line 28 · 2026-05-11T23:38:37.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UdL5MtMqW7EaBGGDhnkiKk`</summary>

```json
{
  "query": "RAGRouter learning route queries retrieval augmented generation 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34875b77-3c15-43be-89f2-7c73b12a9850",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfPKE8PrRVVYWmUTKHb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6490fe1a-22b6-4aa0-a17d-cba16507b414",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mvSJMvvkZTLFLkPiqk5dy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 8871,
      "cache_read_input_tokens": 10662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8871,
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

_source line 29 · 2026-05-11T23:38:38.607Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HgETRr6LDZDzkPw3eBEtc3`</summary>

```json
{
  "query": "RELREPAIR retrieving relevant code program repair arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6490fe1a-22b6-4aa0-a17d-cba16507b414",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfPKE8PrRVVYWmUTKHb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0aa79ada-da75-440f-8a25-990e4b5c4351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mvSJMvvkZTLFLkPiqk5dy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 8871,
      "cache_read_input_tokens": 10662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8871,
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

_source line 30 · 2026-05-11T23:38:39.080Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BJJ5eY2o2hcHAdw9QvBieY`</summary>

```json
{
  "query": "RepoRepair repository level automated program repair 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0aa79ada-da75-440f-8a25-990e4b5c4351",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfPKE8PrRVVYWmUTKHb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5607dff8-13c6-4f92-aa39-daf194709f3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mvSJMvvkZTLFLkPiqk5dy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 8871,
      "cache_read_input_tokens": 10662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8871,
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

_source line 31 · 2026-05-11T23:38:39.623Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LJgcUKc8ENBhZKotEDn5AH`</summary>

```json
{
  "query": "ReAPR retrieval augmented program repair LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5607dff8-13c6-4f92-aa39-daf194709f3f",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfPKE8PrRVVYWmUTKHb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "273911e2-60fd-49c7-bce9-1571742aa913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mvSJMvvkZTLFLkPiqk5dy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 8871,
      "cache_read_input_tokens": 10662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8871,
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

_source line 32 · 2026-05-11T23:38:40.573Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011hhM3ATtJv94VyC7Zk2LTh`</summary>

```json
{
  "query": "LLM4FL multi-agent fault localization graph retrieval 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "273911e2-60fd-49c7-bce9-1571742aa913",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfPKE8PrRVVYWmUTKHb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89ce79c0-de68-4bf3-8156-5cf02d08a3b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mvSJMvvkZTLFLkPiqk5dy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 8871,
      "cache_read_input_tokens": 10662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8871,
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

_source line 33 · 2026-05-11T23:38:41.498Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KnZXhGhneHifop69AraKDs`</summary>

```json
{
  "query": "\"defect-type-aware\" adaptive program repair LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89ce79c0-de68-4bf3-8156-5cf02d08a3b3",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfPKE8PrRVVYWmUTKHb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa477d5a-0ad1-493f-af8f-9c8d76ccedaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mvSJMvvkZTLFLkPiqk5dy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 8871,
      "cache_read_input_tokens": 10662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8871,
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

_source line 34 · 2026-05-11T23:38:41.987Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XktXM4tVFoZyzJHqxgrcKH`</summary>

```json
{
  "query": "MemFL external memory fault localization LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa477d5a-0ad1-493f-af8f-9c8d76ccedaa",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfPKE8PrRVVYWmUTKHb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6312af94-b908-491b-86e2-58d1b8ca3a7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mvSJMvvkZTLFLkPiqk5dy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 8871,
      "cache_read_input_tokens": 10662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8871,
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

_source line 35 · 2026-05-11T23:38:42.412Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FC8C4UEQBPZ3CTQ88Ds3QZ`</summary>

```json
{
  "query": "FlexFL flexible fault localization open-source LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6312af94-b908-491b-86e2-58d1b8ca3a7b",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfPKE8PrRVVYWmUTKHb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9c07a22-eefd-4136-bf62-12c8e94af888",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mvSJMvvkZTLFLkPiqk5dy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 8871,
      "cache_read_input_tokens": 10662,
      "output_tokens": 441,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8871
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1000,
          "output_tokens": 441,
          "cache_read_input_tokens": 10662,
          "cache_creation_input_tokens": 8871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8871,
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

_source line 36 · 2026-05-11T23:38:43.322Z_

<details><summary>↩ Tool result · `toolu_01UdL5MtMqW7EaBGGDhnkiKk`</summary>

```text
Web search results for query: "RAGRouter learning route queries retrieval augmented generation 2025 arXiv"

Links: [{"title":"[2505.23052] RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://arxiv.org/abs/2505.23052"},{"title":"RAGRouter: Learning to Route Queries to Multiple ...","url":"https://arxiv.org/pdf/2505.23052"},{"title":"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2505.23052v2"},{"title":"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models | OpenReview","url":"https://openreview.net/forum?id=4VKVUmE1I8"},{"title":"Query Routing for Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2505.23052v1"},{"title":"RAGRouter: Learning to Route Queries to Multiple ...","url":"https://openreview.net/pdf?id=4VKVUmE1I8"},{"title":"NeurIPS Poster RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://neurips.cc/virtual/2025/poster/119935"},{"title":"Learning Agent Routing From Early Experience","url":"https://arxiv.org/html/2605.07180"},{"title":"RouteRAG: Efficient Retrieval-Augmented Generation from Text and Graph via Reinforcement Learning","url":"https://arxiv.org/html/2512.09487v1"},{"title":"Paper page - Query Routing for Retrieval-Augmented Language Models","url":"https://huggingface.co/papers/2505.23052"}]

I've found comprehensive information about RAGRouter. Here's what the search results reveal:

## RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models

Retrieval-Augmented Generation (RAG) significantly improves the performance of Large Language Models (LLMs) on knowledge-intensive tasks. However, varying response quality across LLMs under RAG necessitates intelligent routing mechanisms, which select the most suitable model for each query from multiple retrieval-augmented LLMs via a dedicated router model.

### The Problem

External documents dynamically affect LLMs' ability to answer queries, while existing routing methods, which rely on static parametric knowledge representations, exhibit suboptimal performance in RAG scenarios.

### The Solution

RAGRouter is a RAG-aware routing design, which leverages document embeddings and RAG capability embeddings with contrastive learning to capture knowledge representation shifts and enable informed routing decisions.

### Key Contributions and Results

This is the first work exploring LLM routing in the RAG setting, proposing a contrastive learning-based routing mechanism that is aware of knowledge shifts, incorporating RAG capability and document-aware representations to effectively address the failure modes of existing routing strategies in RAG.

Results show that RAGRouter outperforms the best individual LLM and existing non-RAG-aware routing methods by 1.67%–9.33%.

With an extended score-threshold-based mechanism, it also achieves strong performance-efficiency trade-offs under low-latency constraints.

The paper (arXiv:2505.23052) was initially published in May 2025 and updated in October 2025, and has been accepted as a NeurIPS 2025 poster presentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6490fe1a-22b6-4aa0-a17d-cba16507b414",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "d145d905-8f70-4d2a-b214-928d54b3f502",
  "sourceToolAssistantUUID": "6490fe1a-22b6-4aa0-a17d-cba16507b414",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-11T23:38:43.867Z_

<details><summary>↩ Tool result · `toolu_01BJJ5eY2o2hcHAdw9QvBieY`</summary>

```text
Web search results for query: "RepoRepair repository level automated program repair 2026"

Links: [{"title":"[2603.01048] RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/abs/2603.01048"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/html/2603.01048"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"(PDF) RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://www.researchgate.net/publication/401470565_RepoRepair_Leveraging_Code_Documentation_for_Repository-Level_Automated_Program_Repair"},{"title":"RepoFixEval: A Repository-Level Program Repair Benchmark From Issue Discovering to Bug Fixing | OpenReview","url":"https://openreview.net/forum?id=LaNCeNmoHR"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair | Gist.Science","url":"https://gist.science/paper/2603.01048"},{"title":"Automated Program Repair in the Era of Large Pre-trained Language Models","url":"https://www.researchgate.net/publication/372380003_Automated_Program_Repair_in_the_Era_of_Large_Pre-trained_Language_Models"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.01048"},{"title":"AutoCodeRover: Autonomous Program Improvement | Request PDF","url":"https://www.researchgate.net/publication/383959416_AutoCodeRover_Autonomous_Program_Improvement"},{"title":"Measuring program comprehension: a large-scale field study with professionals | Request PDF","url":"https://www.researchgate.net/publication/329635134_Measuring_program_comprehension_a_large-scale_field_study_with_professionals"}]

Based on the search results, here's what I found about RepoRepair:

## RepoRepair Overview

RepoRepair is a novel documentation-enhanced approach for repository-level fault localization and program repair. Automated program repair (APR) struggles to scale from isolated functions to full repositories, as it demands a global, task-aware understanding to locate necessary changes.

## Core Approach

RepoRepair leverages LLMs to generate hierarchical code documentation (from functions to files) for code repositories, creating structured semantic abstractions that enable LLMs to comprehend repository-level context and dependencies. Specifically, RepoRepair first employs a text-based LLM (e.g., DeepSeek-V3) to generate file/function-level code documentation for repositories, which serves as auxiliary knowledge to guide fault localization. Subsequently, based on the fault localization results and the issue description, a powerful LLM (e.g., Claude-4) attempts to repair the identified suspicious code snippets.

## Performance Results

Evaluated on SWE-bench Lite, RepoRepair achieves a 45.7% repair rate at a low cost of $0.44 per fix. On SWE-bench Multimodal, it delivers state-of-the-art performance with a 37.1% repair rate despite a higher cost of $0.56 per fix.

The paper was submitted on March 1, 2026, and represents recent work in the field of automated program repair using large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5607dff8-13c6-4f92-aa39-daf194709f3f",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "9d64eed3-cb65-4c36-9ad5-dacc54d101c8",
  "sourceToolAssistantUUID": "5607dff8-13c6-4f92-aa39-daf194709f3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-11T23:38:45.732Z_

<details><summary>↩ Tool result · `toolu_01HgETRr6LDZDzkPw3eBEtc3`</summary>

```text
Web search results for query: "RELREPAIR retrieving relevant code program repair arXiv 2025"

Links: [{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"[2509.16701] RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code","url":"https://arxiv.org/abs/2509.16701"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/html/2603.01048"},{"title":"[2604.10481] PatchRecall: Patch-Driven Retrieval for Automated Program Repair","url":"https://arxiv.org/abs/2604.10481"},{"title":"Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/html/2601.08545.pdf"},{"title":"Learner-Tailored Program Repair: A Solution Generator with","url":"https://arxiv.org/pdf/2601.08545"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"}]

Based on the search results, I found relevant information about RELREPAIR:

## RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code

RELREPAIR is a novel approach that retrieves relevant project-specific code to enhance automated program repair. The approach proposes a specialized RAG (Retrieval-Augmented Generation) approach tailored to program repair tasks, focusing on retrieving highly relevant, project-specific data essential for effective program repair.

### Key Components

The method retrieves: (1) relevant function signatures, facilitating simpler repairs involving direct modifications or replacements of function signatures without extensive code analysis, and (2) relevant code snippets, capturing semantically aligned fix logic or illustrating function usage.

### Methodology

RELREPAIR follows a unified three-step process: (1) Query Rewriting, which reformulates search queries to improve retrieval precision; (2) Dataset Creation and Indexing, which builds a targeted index of functions and code snippets from the project; and (3) Retrieval, where similarity-based search identifies the most relevant entries.

### Performance Results

RELREPAIR successfully repairs 101 bugs in Defects4J V1.2 and achieves a 17.1% improvement in the ManySStuBs4J dataset, increasing the overall fix rate to 48.3%.

The paper was published on arXiv on September 20, 2025 (arXiv:2509.16701).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0aa79ada-da75-440f-8a25-990e4b5c4351",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "80729171-8e06-4ee2-96a4-fda493d6dd7e",
  "sourceToolAssistantUUID": "0aa79ada-da75-440f-8a25-990e4b5c4351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-11T23:38:47.359Z_

<details><summary>↩ Tool result · `toolu_01LJgcUKc8ENBhZKotEDn5AH`</summary>

```text
Web search results for query: "ReAPR retrieval augmented program repair LLM 2025"

Links: [{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"[2506.23749v1] A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/abs/2506.23749v1"},{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330"},{"title":"GitHub - GLEAM-Lab/ProgramRepair: A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications · GitHub","url":"https://github.com/GLEAM-Lab/ProgramRepair"},{"title":"Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/html/2601.08545"},{"title":"[2509.02330] ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2509.02330"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749"},{"title":"Automatic Program Repair Using Large Language Models in Model-Based Development","url":"https://www.scitepress.org/Papers/2026/144911/144911.pdf"}]

Based on the search results, here's what I found about ReAPR:

## ReAPR Overview

ReAPR is an automatic program repair framework via retrieval-augmented large language models. Automatic Program Repair (APR) aims to automatically fix software defects, significantly reducing the efforts of manual debugging.

## Key Challenge and Solution

Current LLM-based approaches depend solely on the pre-trained knowledge of LLMs, overlooking the prior knowledge contained in historical bug repair records, which increases the likelihood of hallucinations. To address this challenge, ReAPR proposes a retrieval-augmented framework that first curates a high-quality retrieval database by carefully compiling and filtering existing datasets for APR, then leverages a retriever to fetch bug-fix pairs similar to the target bug from a retrieval database, providing contextual hints to guide the LLMs in the repair process.

## Technical Approach

ReAPR investigates two techniques to retrieve bug-fix pairs associated with the function to be fixed: BM25 and Dense Passage Retrieval (DPR).

## Performance Results

The framework was validated using the widely-used benchmark dataset Defects4j 2.0 as well as the latest benchmark GitBug-Java, showing that ReAPR, based on the CodeLlama(7B) backbone, successfully fixes 68 and 59 bugs in the DPR and BM25 settings, respectively, in Defects4j 2.0, outperforming the best baseline approach by 18 and 9 bugs under the same repair settings.

The paper was published in 2025 in the Software Quality Journal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "273911e2-60fd-49c7-bce9-1571742aa913",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "1f31ee84-9eaa-4552-a101-3d33468f7498",
  "sourceToolAssistantUUID": "273911e2-60fd-49c7-bce9-1571742aa913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-11T23:38:48.008Z_

<details><summary>↩ Tool result · `toolu_01KnZXhGhneHifop69AraKDs`</summary>

```text
Web search results for query: ""defect-type-aware" adaptive program repair LLM 2025 2026"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-026-09751-w"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"An empirical evaluation of pre-trained large language models for repairing declarative formal specifications | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10687-1"},{"title":"Specification-Guided Repair of Arithmetic Errors in Dafny Programs Using LLMs | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-10444-1_16"},{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"},{"title":"Can test cases generated by large language models facilitate automated program repair? | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-026-10802-w"},{"title":"Hybrid Automated Program Repair by Combining Large Language","url":"https://xgdsmileboy.github.io/files/paper/tosem25-hybrid.pdf"},{"title":"GitHub - GLEAM-Lab/ProgramRepair: A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications · GitHub","url":"https://github.com/GLEAM-Lab/ProgramRepair"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | Request PDF","url":"https://www.researchgate.net/publication/392956389_RepairAgent_An_Autonomous_LLM-Based_Agent_for_Program_Repair"}]

I found relevant results for your search query. Here's what I discovered:

## Main Finding

There is a paper titled "Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models" by Zhang, R., Zhang, S. & Xie, L., published in Software Quality Journal in 2026.

## Related Research Context

Your search query aligns with a significant research area in automated program repair (APR) using LLMs. The field has seen substantial activity in 2025-2026:

- "Less is More: Adaptive Program Repair with Bug Localization and Preference Learning" was published in 2025 at AAAI

- Multiple recent works on LLM-based program repair include "Template-Guided Program Repair in the Era of Large Language Models" (2025-ICSE) and "APPATCH: Automated Adaptive Prompting Large Language Models for Real-World Software Vulnerability Patching" (2025-USENIX Security)

- LLM-based APR systems are categorized into four major paradigms: Fine-Tuning, Prompting, Procedural, and Agentic approaches

The research landscape shows a strong focus on adaptive and context-aware approaches to program repair, which aligns with the defect-type-aware methodology in your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa477d5a-0ad1-493f-af8f-9c8d76ccedaa",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "0ed1576c-44c4-442b-b170-37e0fc0e750c",
  "sourceToolAssistantUUID": "fa477d5a-0ad1-493f-af8f-9c8d76ccedaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-11T23:38:48.732Z_

<details><summary>↩ Tool result · `toolu_011hhM3ATtJv94VyC7Zk2LTh`</summary>

```text
Web search results for query: "LLM4FL multi-agent fault localization graph retrieval 2025 2026"

Links: [{"title":"LLM4FL: Multi-Agent Repository-Level Software Fault Localization via Graph-Based Retrieval and Iterative Refinement | OpenReview","url":"https://openreview.net/forum?id=z91EvZbSI1"},{"title":"A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion","url":"https://arxiv.org/html/2409.13642v2"},{"title":"[2409.13642] A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion","url":"https://arxiv.org/abs/2409.13642"},{"title":"A Multi-Agent Approach to Fault Localization via Graph-Based","url":"https://www.arxiv.org/pdf/2409.13642"},{"title":"LIDL: LLM Integration Defect Localization via Knowledge Graph-Enhanced Multi-Agent Analysis","url":"https://arxiv.org/html/2601.05539"},{"title":"Enhancing Fault Localization Through Ordered Code Analysis with LLM Agents and Self-Reflection | OpenReview","url":"https://openreview.net/forum?id=tgn8gG2hRZ"},{"title":"LLM4FL: Multi-Agent Repository-Level Software Fault Lo","url":"https://openreview.net/pdf?id=z91EvZbSI1#:~:text=Recent%20advancements%20in%20Large%20Language,fault%20localization%20without%20additional%20training."},{"title":"[2403.16362] AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/abs/2403.16362"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/html/2403.16362v1"},{"title":"LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3712003"}]

Based on the search results, here's what I found about LLM4FL:

## Overview

LLM4FL is a multi-LLM-agent-based fault localization approach designed to address challenges in software fault localization. LLM4FL is a multi-agent LLM-based fault localization technique designed to analyze large-scale software projects at the repository level, leveraging a multi-agent framework that emulates developers' fault localization process.

## Architecture

LLM4FL employs three LLM agents, each with a specialized role. The Context Extraction Agent divides the methods covered by the failing test cases into smaller groups, each within LLM's token limitation, then analyzes the test code and test failure messages to reason about possible failure causes and prioritize the most suspicious covered methods.

The Debugger Agent analyzes each covered method and performs graph-based, retrieval-augmented (Graph-RAG) code navigation, traversing the prioritized methods' code iteratively along call dependencies to analyze and rank suspicious methods.

The Reviewer Agent re-evaluates the identified faulty methods using verbal reinforcement learning, engaging in self-criticism and iterative refinement.

## Performance Results

Evaluated on the Defects4J (V2.0.0) benchmark, which includes 675 faults from 14 Java projects, LLM4FL achieves an 18.55% improvement in Top-1 accuracy over AutoFL and 4.82% over SoapFL, and outperforms supervised techniques such as DeepFL and Grace, all without requiring task-specific training.

LLM4FL is also the cheapest among the three, costing only $0.05 per fault.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89ce79c0-de68-4bf3-8156-5cf02d08a3b3",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "260d09cf-b14f-42c9-8cd7-3d72863aed7f",
  "sourceToolAssistantUUID": "89ce79c0-de68-4bf3-8156-5cf02d08a3b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-11T23:38:48.967Z_

<details><summary>↩ Tool result · `toolu_01XktXM4tVFoZyzJHqxgrcKH`</summary>

```text
Web search results for query: "MemFL external memory fault localization LLM 2026"

Links: [{"title":"Improving LLM-Based Fault Localization with External Memory and Project Context","url":"https://arxiv.org/html/2506.03585v1"},{"title":"[Literature Review] Improving LLM-Based Fault Localization with External Memory and Project Context","url":"https://www.themoonlight.io/en/review/improving-llm-based-fault-localization-with-external-memory-and-project-context"},{"title":"Improving LLM-Based Fault Localization with External ...","url":"https://www.arxiv.org/pdf/2506.03585"},{"title":"[2506.03585] Improving LLM-Based Fault Localization with External Memory and Project Context","url":"https://arxiv.org/abs/2506.03585"},{"title":"(PDF) Improving LLM-Based Fault Localization with External Memory and Project Context","url":"https://www.researchgate.net/publication/392406435_Improving_LLM-Based_Fault_Localization_with_External_Memory_and_Project_Context"},{"title":"Impact of Large Language Models of Code on Fault Localization | Request PDF","url":"https://www.researchgate.net/publication/391915573_Impact_of_Large_Language_Models_of_Code_on_Fault_Localization"},{"title":"GitHub - mem0ai/mem0: Universal memory layer for AI Agents · GitHub","url":"https://github.com/mem0ai/mem0"},{"title":"GitHub - MemTensor/MemOS: Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings · GitHub","url":"https://github.com/MemTensor/MemOS"},{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Improving LLM-Based Fault Localization with External ...","url":"https://www.semanticscholar.org/paper/Improving-LLM-Based-Fault-Localization-with-Memory-Yeo-Ryu/c2bca4faccf4a01d33e4f2412d3651377f4e38c9"}]

Based on the search results, here's what I found about MemFL:

## MemFL: External Memory Fault Localization with LLMs

MemFL is a novel LLM-based fault localization technique that incorporates project-specific knowledge through external memory knowledge editing.

### How It Works

The external memory consists of two parts: static memory, which holds pre-generated summaries of the project and its classes, and dynamic memory, which iteratively gather debugging guidance from prior attempts. These memory components enhance the LLM's ability to reason effectively about complex, project-specific contexts, enabling MemFL to structure the debugging process into three simple steps that significantly reduce debugging costs while enhancing accuracy.

### Key Performance Results

MemFL using GPT-4o-mini localized 12.7% more buggy methods than existing LLM-based baselines, achieving this improvement with only 21% of the execution time (17.4 seconds per bug) and 33% of the API cost ($0.0033 per bug). The performance gain was even more pronounced on complex projects where LLM-based baselines struggled, localizing 27.6% more buggy methods.

### Advantages Over Existing Approaches

Existing LLM-based fault localization techniques rely solely on the generic capabilities of the LLM without incorporating project-specific knowledge, limiting their effectiveness, and these methods depend on complex workflow to analyze the project from scratch, and they also perform poorly on complex software projects that require domain-specific knowledge for successful debugging.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6312af94-b908-491b-86e2-58d1b8ca3a7b",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "c349893c-8cdf-4fbb-bc67-e0e2afcbe451",
  "sourceToolAssistantUUID": "6312af94-b908-491b-86e2-58d1b8ca3a7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-11T23:38:49.528Z_

<details><summary>↩ Tool result · `toolu_01FC8C4UEQBPZ3CTQ88Ds3QZ`</summary>

```text
Web search results for query: "FlexFL flexible fault localization open-source LLM 2025"

Links: [{"title":"FlexFL: Flexible and Effective Fault Localization With Open-Source Large Language Models | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1109/TSE.2025.3553363"},{"title":"[2411.10714] FlexFL: Flexible and Effective Fault Localization with Open-Source Large Language Models","url":"https://arxiv.org/abs/2411.10714"},{"title":"GitHub - ZJU-CTAG/FlexFL: Replication code of Paper \"FlexFL: Flexible and Effective Fault Localization with Open-Source Large Language Models\"","url":"https://github.com/ZJU-CTAG/FlexFL"},{"title":"FlexFL: Flexible and Effective Fault Localization With Open-Source Large Language Models | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/32/4359463/10934742.pdf"},{"title":"FlexFL: Flexible and Effective Fault Localization with Open- ...","url":"https://arxiv.org/pdf/2411.10714"},{"title":"FlexFL: Flexible and Effective Fault Localization With Open ...","url":"https://www.researchgate.net/publication/390001196_FlexFL_Flexible_and_Effective_Fault_Localization_with_Open-Source_Large_Language_Models"},{"title":"ZJU-CTAG · GitHub","url":"https://github.com/ZJU-CTAG"},{"title":"[Literature Review] FlexFL: Flexible and Effective Fault Localization with Open-Source Large Language Models","url":"https://www.themoonlight.io/en/review/flexfl-flexible-and-effective-fault-localization-with-open-source-large-language-models"},{"title":"Explainable Fault Localization for Programming Assignments via LLM-Guided Annotation","url":"https://arxiv.org/html/2509.25676v1"},{"title":"FlexFL: Flexible and Effective Fault Localization With Open ...","url":"https://www.computer.org/csdl/journal/ts/2025/05/10934742/25d5dKOD78c"}]

Based on the search results, here's what I found about FlexFL:

## Overview

FlexFL is a novel LLM-based fault localization framework that can flexibly leverage different types of bug-related information and effectively work with open-source LLMs. The paper was accepted to IEEE Transactions on Software Engineering (TSE) in 2025.

## Key Limitations Addressed

Existing LLM-based fault localization methods are limited in flexibility as they rely on bug-triggering test cases and cannot make use of other available bug-related information like bug reports, and are built upon proprietary LLMs which are confronted with risks in data privacy.

## Two-Stage Architecture

In the first stage, FlexFL reduces the search space of buggy code using state-of-the-art fault localization techniques and provides a candidate list of bug-related methods. In the second stage, FlexFL leverages LLMs to delve deeper to double-check the code snippets of methods suggested by the first stage and refine fault localization results.

## Performance Results

FlexFL with a lightweight open-source LLM Llama3-8B can locate 42 and 63 more bugs than state-of-the-art LLM-based FL approaches AutoFL and AgentFL that both use GPT-3.5. Extensive experimental results on Defects4J demonstrate that FlexFL outperforms the baselines and can work with different open-source LLMs.

## Open Source Availability

The replication code for FlexFL is available on GitHub, accompanying the paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9c07a22-eefd-4136-bf62-12c8e94af888",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "1aebc769-988a-4a52-ab23-06563867689a",
  "sourceToolAssistantUUID": "b9c07a22-eefd-4136-bf62-12c8e94af888",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-11T23:38:57.331Z_

Let me search for a few more specific papers that could be highly relevant competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aebc769-988a-4a52-ab23-06563867689a",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfQTMJjgDUGjkUssjRL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e3e1fce-9382-4b27-aefe-c606e0ebd09f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWme2JZJA4Due1JFkB9G9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9040,
      "cache_read_input_tokens": 19533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9040,
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

_source line 45 · 2026-05-11T23:38:58.340Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JBLnDoaYR4LvcXvFBStwZR`</summary>

```json
{
  "query": "PatchRecall patch-driven retrieval automated program repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e3e1fce-9382-4b27-aefe-c606e0ebd09f",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfQTMJjgDUGjkUssjRL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e1fef74-dfdc-4ece-8785-c9c7cedb6b94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWme2JZJA4Due1JFkB9G9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9040,
      "cache_read_input_tokens": 19533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9040,
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

_source line 46 · 2026-05-11T23:38:58.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017PJ2wbVy3HD1htPWxJ98CL`</summary>

```json
{
  "query": "\"context budget\" OR \"context allocation\" code repair LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e1fef74-dfdc-4ece-8785-c9c7cedb6b94",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfQTMJjgDUGjkUssjRL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5745cfa4-d839-4426-9c7b-dbb3124d03f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWme2JZJA4Due1JFkB9G9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9040,
      "cache_read_input_tokens": 19533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9040,
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

_source line 47 · 2026-05-11T23:38:59.753Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019gzyGTngFmX2ZnGLp194pC`</summary>

```json
{
  "query": "RouteRAG reinforcement learning retrieval routing 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5745cfa4-d839-4426-9c7b-dbb3124d03f9",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfQTMJjgDUGjkUssjRL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1767011d-5221-4be6-ab18-ab2d55be8d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWme2JZJA4Due1JFkB9G9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9040,
      "cache_read_input_tokens": 19533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9040,
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

_source line 48 · 2026-05-11T23:39:00.279Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KRk1NsBu6cdevuuEHtGgct`</summary>

```json
{
  "query": "adaptive granularity retrieval code repository 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1767011d-5221-4be6-ab18-ab2d55be8d75",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfQTMJjgDUGjkUssjRL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "040d89c7-3d27-4862-b534-52f873da9377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWme2JZJA4Due1JFkB9G9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9040,
      "cache_read_input_tokens": 19533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9040,
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

_source line 49 · 2026-05-11T23:39:00.769Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WqsWYF5H8dZJhfQYuw58xf`</summary>

```json
{
  "query": "LIDL knowledge graph LLM integration defect localization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "040d89c7-3d27-4862-b534-52f873da9377",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfQTMJjgDUGjkUssjRL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75007d02-ae07-4e5c-bbe3-7cb5f3d9f587",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWme2JZJA4Due1JFkB9G9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9040,
      "cache_read_input_tokens": 19533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9040,
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

_source line 50 · 2026-05-11T23:39:01.499Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MRo9Lz6ehK2aU6pD4kRGWL`</summary>

```json
{
  "query": "RepoFixEval repository level program repair benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75007d02-ae07-4e5c-bbe3-7cb5f3d9f587",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfQTMJjgDUGjkUssjRL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e13c08ae-e800-4397-bccd-ecf993c6740f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWme2JZJA4Due1JFkB9G9u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9040,
      "cache_read_input_tokens": 19533,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9040
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 332,
          "cache_read_input_tokens": 19533,
          "cache_creation_input_tokens": 9040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9040,
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

_source line 51 · 2026-05-11T23:39:04.674Z_

<details><summary>↩ Tool result · `toolu_01JBLnDoaYR4LvcXvFBStwZR`</summary>

```text
Web search results for query: "PatchRecall patch-driven retrieval automated program repair 2025 2026"

Links: [{"title":"[2604.10481] PatchRecall: Patch-Driven Retrieval for Automated Program Repair","url":"https://arxiv.org/abs/2604.10481"},{"title":"PatchRecall: Patch-Driven Retrieval for Automated Program Repair","url":"https://arxiv.org/html/2604.10481"},{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"A comprehensive study of code-removal patches in automated program repair | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-021-10100-7"},{"title":"Patch correctness assessment in automated program repair based on the impact of patches on production and test code | Proceedings of the 31st ACM SIGSOFT International Symposium on Software Testing and Analysis","url":"https://dl.acm.org/doi/10.1145/3533767.3534368"},{"title":"Patch correctness assessment in automated program repair based on the impact of patches on production and test code | Request PDF","url":"https://www.researchgate.net/publication/362078016_Patch_correctness_assessment_in_automated_program_repair_based_on_the_impact_of_patches_on_production_and_test_code"},{"title":"Automated Vulnerability Patching Techniques","url":"https://www.emergentmind.com/topics/automated-vulnerability-patching"},{"title":"Automated patch assessment for program repair at scale | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-020-09920-w"}]

Based on the search results, I found detailed information about PatchRecall:

## PatchRecall: Patch-Driven Retrieval for Automated Program Repair

Retrieving the correct set of files from a large codebase is a crucial step in Automated Program Repair (APR), where high recall is necessary to ensure that the relevant files are included, but simply increasing the number of retrieved files introduces noise and degrades efficiency.

PatchRecall combines two complementary strategies: (1) codebase retrieval, where the current issue description is matched against the codebase to surface potentially relevant files, and (2) history-based retrieval, where similar past issues are leveraged to identify edited files as candidate targets. Candidate files from both strategies are merged and reranked to produce the final retrieval set.

**Key Results:**
Experiments on SWE-Bench demonstrate that PatchRecall achieves higher recall without significantly increasing retrieved file count, enabling more effective APR.

**Publication Details:**
The paper (arXiv:2604.10481) appears to have been submitted in April 2026, with authors including Mahir Labib Dihan and two others. This research represents a hybrid approach designed to address the fundamental challenge of balancing retrieval precision with coverage in automated program repair systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e1fef74-dfdc-4ece-8785-c9c7cedb6b94",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "62755ad5-098d-4662-8cd6-c57cdcefd69b",
  "sourceToolAssistantUUID": "0e1fef74-dfdc-4ece-8785-c9c7cedb6b94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-11T23:39:07.915Z_

<details><summary>↩ Tool result · `toolu_019gzyGTngFmX2ZnGLp194pC`</summary>

```text
Web search results for query: "RouteRAG reinforcement learning retrieval routing 2025"

Links: [{"title":"[2512.09487] RouteRAG: Efficient Retrieval-Augmented Generation from Text and Graph via Reinforcement Learning","url":"https://arxiv.org/abs/2512.09487"},{"title":"RouteRAG: Efficient Retrieval-Augmented Generation from Text and Graph via Reinforcement Learning","url":"https://arxiv.org/html/2512.09487v1"},{"title":"RouteRAG: Adaptive Routing in RAG Systems","url":"https://www.emergentmind.com/topics/routerag"},{"title":"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models | OpenReview","url":"https://openreview.net/forum?id=4VKVUmE1I8"},{"title":"RouteRAG: Efficient Retrieval-Augmented Generation from Text and Graph via Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/398559506_RouteRAG_Efficient_Retrieval-Augmented_Generation_from_Text_and_Graph_via_Reinforcement_Learning"},{"title":"[2505.23052] RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://arxiv.org/abs/2505.23052"},{"title":"Learning Agent Routing From Early Experience","url":"https://arxiv.org/html/2605.07180"},{"title":"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2505.23052v2"},{"title":"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning","url":"https://ulab-uiuc.github.io/Router-R1/"},{"title":"GraphRAG-Router: Learning Cost-Efficient Routing over GraphRAGs and LLMs with Reinforcement Learning","url":"https://arxiv.org/html/2604.16401v1"}]

Based on the search results, here's what I found about RouteRAG and related reinforcement learning retrieval routing work:

## RouteRAG: Efficient Retrieval-Augmented Generation

RouteRAG is a framework for Retrieval-Augmented Generation (RAG) that integrates non-parametric knowledge into Large Language Models (LLMs), typically from unstructured texts and structured graphs.

### Key Technical Approach

While recent progress has advanced text-based RAG to multi-turn reasoning through Reinforcement Learning (RL), extending these advances to hybrid retrieval introduces additional challenges. RouteRAG extends retrieval to passage, graph, and hybrid modes, and is trained with a two-stage RL framework that optimizes both accuracy and efficiency.

RouteRAG unifies reasoning, retrieval mode choice, and answer production in an end-to-end RL framework and demonstrates the feasibility and practical gain of learned, dynamic RouteRAG for both structured and unstructured sources.

### Implementation Details

The training uses Qwen2.5-3B-Instruct and Qwen2.5-7B-Instruct as the backbone models, with training data consisting of 10k sampled queries from the HotpotQA training set.

### Publication

The paper was submitted on December 10, 2025, by authors including Yucan Guo and others.

### Broader Context

RouteRAG is part of a larger research direction in adaptive routing for RAG systems. This adaptive routing is enabled by various methods: score-based heuristics, resource/complexity estimation, contrastive learning over model capabilities, or reinforcement learning over multi-turn reasoning policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1767011d-5221-4be6-ab18-ab2d55be8d75",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "78db72a9-e882-4946-b351-6bb29c10f5cd",
  "sourceToolAssistantUUID": "1767011d-5221-4be6-ab18-ab2d55be8d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-11T23:39:08.089Z_

<details><summary>↩ Tool result · `toolu_01KRk1NsBu6cdevuuEHtGgct`</summary>

```text
Web search results for query: "adaptive granularity retrieval code repository 2025 2026"

Links: [{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/abs/2510.04905"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"GitHub - DEEP-PolyU/Awesome-GraphRAG: Awesome-GraphRAG: A curated list of resources (surveys, papers, benchmarks, and opensource projects) on graph-based retrieval-augmented generation. · GitHub","url":"https://github.com/DEEP-PolyU/Awesome-GraphRAG"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"Optimize the Chunking Granularity for Retrieval- ...","url":"https://aclanthology.org/2025.coling-main.384.pdf"},{"title":"A Survey of Graph Retrieval-Augmented Generation for ...","url":"https://arxiv.org/pdf/2501.13958"},{"title":"RAG in 2025: 7 Proven Strategies to Deploy Retrieval-Augmented Generation at Scale | Morphik Blog","url":"https://www.morphik.ai/blog/retrieval-augmented-generation-strategies"},{"title":"Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers","url":"https://arxiv.org/html/2506.00054v1"},{"title":"awesome-generative-ai-guide/research_updates/rag_research_table.md at main · aishwaryanr/awesome-generative-ai-guide","url":"https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/research_updates/rag_research_table.md"}]

Based on the search results, here are the findings related to adaptive granularity retrieval in code repositories for 2025-2026:

## Key Research and Resources

### Recent Surveys and Papers

A comprehensive survey on Retrieval-Augmented Code Generation (RACG) with emphasis on repository-level approaches was published in October 2025. The diversity in retrieval strategies directly influences the quality and granularity of the generated code.

The survey discusses code entities at different granularity levels including: Directory (top-level physical organization), Module (single source file), Class/Function (core units), and Line (smallest addressable unit, indicating support for fine-grained retrieval).

### Adaptive Granularity Approaches

Recent works include "You Don't Need Pre-built Graphs for RAG: Retrieval Augmented Generation with Adaptive Reasoning Structures" (AAAI 2026) and "MaGiX: A Multi-Granular Adaptive Graph Intelligence Framework for Enhancing Cross-Lingual RAG" (CIKM 2025).

An agentic RAG framework has been introduced that exposes hierarchical retrieval interfaces (keyword search, semantic search, and chunk read) directly to the model, allowing it to dynamically adapt retrieval decisions across multiple granularities.

### Repository Resources

Awesome-GraphRAG is a curated list of resources on graph-based retrieval-augmented generation available on GitHub at DEEP-PolyU/Awesome-GraphRAG, which tracks papers and open-source projects from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "040d89c7-3d27-4862-b534-52f873da9377",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "62c4a356-f5d3-43ec-8920-1e39020d75b2",
  "sourceToolAssistantUUID": "040d89c7-3d27-4862-b534-52f873da9377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-11T23:39:08.254Z_

<details><summary>↩ Tool result · `toolu_01MRo9Lz6ehK2aU6pD4kRGWL`</summary>

```text
Web search results for query: "RepoFixEval repository level program repair benchmark 2026"

Links: [{"title":"RepoFixEval: A Repository-Level Program Repair Benchmark From Issue Discovering to Bug Fixing | OpenReview","url":"https://openreview.net/forum?id=LaNCeNmoHR"},{"title":"Awesome-Code-Benchmark/README.md at main · tongye98/Awesome-Code-Benchmark","url":"https://github.com/tongye98/Awesome-Code-Benchmark/blob/main/README.md"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/html/2603.01048v1"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"REPOFIXEVAL:AREPOSITORY-LEVEL PROGRAM RE","url":"https://openreview.net/pdf?id=LaNCeNmoHR"},{"title":"[2403.00448] When Large Language Models Confront Repository-Level Automatic Program Repair: How Well They Done?","url":"https://arxiv.org/abs/2403.00448"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair | Gist.Science","url":"https://gist.science/paper/2603.01048"},{"title":"(PDF) RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://www.researchgate.net/publication/401470565_RepoRepair_Leveraging_Code_Documentation_for_Repository-Level_Automated_Program_Repair"},{"title":"[2604.27148] CI-Repair-Bench: A Repository-Aware Benchmark for Automated Patch Validation via CI Workflows","url":"https://arxiv.org/abs/2604.27148"},{"title":"CI-Repair-Bench: A Repository-Aware Benchmark for Automated Patch Validation via CI Workflows","url":"https://arxiv.org/html/2604.27148"}]

Based on the search results, here's what I found about RepoFixEval:

## RepoFixEval Overview

RepoFixEval is a repository-level APR (Automatic Program Repair) benchmark consisting of 160 real-world bug fixing suites from popular Python projects. RepoFixEval provides the original buggy programs, associated issue reports, corresponding fixes, and unit tests to verify the correctness of each fix.

## Purpose and Scope

While current research demonstrates that Large Language Models (LLMs) excel in file-level program repair, their effectiveness in repository-level program repair remains unexplored. Real-world software projects, which often consist of multiple files, present significant challenges for LLMs in identifying bugs and generating fixes due to the intricate project structures.

## Evaluation Framework

The benchmark proposes a three-step evaluation framework for LLM-based APR tools, encompassing (1) discovering issues from execution failures, (2) localizing buggy code segments (and patch generation).

RepoFixEval is an issue-aware benchmark for practical repository-level automatic program repair, and evaluates 16 LLMs' performance in fixing multi-file software bugs.

The research was published on OpenReview in 2024 and represents an important step toward evaluating how well LLMs can handle real-world, multi-file software bug fixing tasks at the repository level.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e13c08ae-e800-4397-bccd-ecf993c6740f",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "39bec869-16a8-4a5b-84ce-35f71fe0fa5b",
  "sourceToolAssistantUUID": "e13c08ae-e800-4397-bccd-ecf993c6740f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-11T23:39:08.736Z_

<details><summary>↩ Tool result · `toolu_01WqsWYF5H8dZJhfQYuw58xf`</summary>

```text
Web search results for query: "LIDL knowledge graph LLM integration defect localization 2026"

Links: [{"title":"[2601.05539] LIDL: LLM Integration Defect Localization via Knowledge Graph-Enhanced Multi-Agent Analysis","url":"https://arxiv.org/abs/2601.05539"},{"title":"LIDL: LLM Integration Defect Localization via Knowledge Graph-Enhanced Multi-Agent Analysis","url":"https://arxiv.org/html/2601.05539"},{"title":"From LLMs to Knowledge Graphs: Building Production-Ready Graph Systems in 2025 | by Claudiu Branzan | Medium","url":"https://medium.com/@claudiubranzan/from-llms-to-knowledge-graphs-building-production-ready-graph-systems-in-2025-2b4aff1ec99a"},{"title":"Combining Knowledge Graphs With LLMs | Complete Guide","url":"https://atlan.com/know/combining-knowledge-graphs-llms/"},{"title":"Exploiting knowledge graph communities to fine-tune large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425034311"},{"title":"Knowledge Base vs Knowledge Graph for LLM Systems (2026 Guide) | Kloia","url":"https://www.kloia.com/blog/knowledge-base-vs-knowledge-graph-llm"},{"title":"How can the integration of AI large language models and knowledge graph enhance fault diagnosis? A systematic literature review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S156849462600356X"},{"title":"The construction and refined extraction techniques of knowledge graph based on large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-38066-w"},{"title":"LLM Knowledge Graph Builder — First Release of 2025 - Graph Database & Analytics","url":"https://neo4j.com/blog/developer/llm-knowledge-graph-builder-release/"},{"title":"Knowledge Graph and LLM Integration: Benefits & Challenges","url":"https://www.falkordb.com/blog/knowledge-graph-llm/"}]

Based on the web search results, I found relevant information about LIDL, which is a research paper submitted in January 2026.

## LIDL: LLM Integration Defect Localization

LIDL is a multi-agent framework for defect localization in LLM-integrated software.

### The Problem

LLM-integrated software, which embeds or interacts with large language models (LLMs) as functional components, exhibits probabilistic and context-dependent behaviors that fundamentally differ from those of traditional software. This shift introduces a new category of integration defects that arise not only from code errors but also from misaligned interactions among LLM-specific artifacts, including prompts, API calls, configurations, and model outputs.

### Why Existing Approaches Fall Short

Existing defect localization techniques are ineffective at identifying these LLM-specific integration defects because they fail to capture cross-layer dependencies across heterogeneous artifacts, cannot exploit incomplete or misleading error traces, and lack semantic reasoning capabilities for identifying root causes.

### LIDL's Innovation

LIDL is the first to propose integrating a code knowledge graph with LLM-based semantic reasoning to address the unique challenges of localizing LLM integration defects. The framework combines knowledge graph, multi-source evidence fusion, and counterfactual validation in a unified workflow.

### Performance Results

LIDL was evaluated on 146 real-world defect instances and significantly outperforms five state-of-the-art baselines in both accuracy and cost efficiency. Additionally, LIDL achieves substantial cost savings, reducing cost by 92.5% compared to AutoCodeRover, incurring only $0.008 per localization task.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75007d02-ae07-4e5c-bbe3-7cb5f3d9f587",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "7c85bc19-e3ba-4862-a5c4-82f0a2b4cee3",
  "sourceToolAssistantUUID": "75007d02-ae07-4e5c-bbe3-7cb5f3d9f587",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-11T23:39:10.277Z_

<details><summary>↩ Tool result · `toolu_017PJ2wbVy3HD1htPWxJ98CL`</summary>

```text
Web search results for query: ""context budget" OR "context allocation" code repair LLM 2025 2026"

Links: [{"title":"Compressing Code Context for LLM-based Issue Resolution","url":"https://arxiv.org/html/2603.28119"},{"title":"The LLM context problem in 2026: strategies for memory, relevance, and scale - LogRocket Blog","url":"https://blog.logrocket.com/llm-context-problem/"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Context as Infrastructure: Why Most LLM Production Systems Fail at Architecture, Not at Prompts - The CIO Magazine","url":"https://www.theciomagazine.com/context-as-infrastructure-why-most-llm-production-systems-fail-at-architecture-not-at-prompts/"},{"title":"Beyond Prompts: 4 Context Engineering Secrets for Claude Code | The road","url":"https://kane.mx/posts/2025/context-engineering-secrets-claude-code/"},{"title":"The Best Open Source LLM for Context Engineering in 2026","url":"https://www.siliconflow.com/articles/en/the-best-open-source-llm-for-context-enginneering"},{"title":"State of AI Engineering | Datadog","url":"https://www.datadoghq.com/state-of-ai-engineering/"},{"title":"Effective context engineering for AI agents","url":"https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"},{"title":"1 CigaR: Cost-efficient Program Repair with LLMs","url":"https://arxiv.org/pdf/2402.06598"}]

Based on the search results, here are the key findings about context budget and context allocation in LLM-based code repair for 2025-2026:

## Context Compression and Allocation in Code Repair

Recent work like LongCodeZip (Shi et al., 2025) introduced a code-specific compression framework that ranks function-level chunks using conditional perplexity and applies fine-grained block-level pruning via knapsack algorithm. Additionally, SWE-Pruner (Wang et al., 2026) fine-tunes a lightweight reranker to score each token's task-conditioned relevance, and prunes lines whose aggregated scores fall below a threshold.

A promising mitigation is to compress retrieved contexts by distilling overapproximate retrieval output into concise form that retains only essential information. However, existing compression strategies are ineffective for patch generation, as generic compressors treating code as natural language tend to disrupt program structure and break semantic links.

## Context Budget and Allocation Principles

More broadly, how much of the available context window is being used at inference time and how that budget is allocated across instructions, retrieved documents, conversation history, and output space is a critical concern. Systems with no explicit utilisation model tend to hit ceiling issues under load — as conversations lengthen or retrieval returns more chunks, the window fills and earlier content is silently truncated.

## Token Cost Optimization

For practical implementations, tools like CIGAR optimize prompts and prompt settings to maximize the information given to LLMs using the smallest possible number of tokens, achieving 73% reduction in token cost on program repair tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5745cfa4-d839-4426-9c7b-dbb3124d03f9",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "d87047f5-8f4b-42b4-b436-181285fc669e",
  "sourceToolAssistantUUID": "5745cfa4-d839-4426-9c7b-dbb3124d03f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-11T23:39:15.722Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q2FHV4eci4ypqes2ACVtvq`</summary>

```json
{
  "query": "\"compressing code context\" LLM issue resolution SWE-bench 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d87047f5-8f4b-42b4-b436-181285fc669e",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfRzQNr9C77eLdrEti8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6251b3db-5739-4378-9ef6-d93e78e0c3e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017K2hWxRBMLsrdR9GtoVGvS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3782,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 28573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2177,
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

_source line 58 · 2026-05-11T23:39:16.171Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017JvsqWu9MwiSTxL6xBUF6T`</summary>

```json
{
  "query": "CigaR cost efficient program repair LLM token optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6251b3db-5739-4378-9ef6-d93e78e0c3e5",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfRzQNr9C77eLdrEti8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65e558cc-b414-44a7-be65-41d32eb227ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017K2hWxRBMLsrdR9GtoVGvS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3782,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 28573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2177,
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

_source line 59 · 2026-05-11T23:39:17.072Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QbLEEPhfKYa6XSffardvjS`</summary>

```json
{
  "query": "\"learning agent routing\" early experience arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65e558cc-b414-44a7-be65-41d32eb227ac",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfRzQNr9C77eLdrEti8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87c1faa5-efda-4cd5-8e25-3847caf9c18a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017K2hWxRBMLsrdR9GtoVGvS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3782,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 28573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2177,
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

_source line 60 · 2026-05-11T23:39:17.468Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JwsBjuoQzwjpJSa7mAeNC3`</summary>

```json
{
  "query": "GraphRAG-Router cost efficient routing reinforcement learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87c1faa5-efda-4cd5-8e25-3847caf9c18a",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfRzQNr9C77eLdrEti8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19732eb1-6fc0-41c5-8416-d2701fab0f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017K2hWxRBMLsrdR9GtoVGvS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3782,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 28573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2177,
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

_source line 61 · 2026-05-11T23:39:18.415Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lo6sW98jTjd5By4x27wZu7`</summary>

```json
{
  "query": "Router-R1 multi-round routing aggregation reinforcement learning LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19732eb1-6fc0-41c5-8416-d2701fab0f56",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfRzQNr9C77eLdrEti8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd0a4991-f0af-48f0-8339-7579b938ecc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017K2hWxRBMLsrdR9GtoVGvS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3782,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 28573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2177,
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

_source line 62 · 2026-05-11T23:39:18.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BtzoQtK83Y7x7kR1Ehr2FH`</summary>

```json
{
  "query": "\"optimize chunking granularity\" retrieval augmented generation COLING 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd0a4991-f0af-48f0-8339-7579b938ecc0",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfRzQNr9C77eLdrEti8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05892713-1848-4f57-984d-b338c2722e83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017K2hWxRBMLsrdR9GtoVGvS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3782,
      "cache_creation_input_tokens": 2177,
      "cache_read_input_tokens": 28573,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2177
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3782,
          "output_tokens": 319,
          "cache_read_input_tokens": 28573,
          "cache_creation_input_tokens": 2177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2177,
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

_source line 63 · 2026-05-11T23:39:23.734Z_

<details><summary>↩ Tool result · `toolu_01QbLEEPhfKYa6XSffardvjS`</summary>

```text
Web search results for query: ""learning agent routing" early experience arXiv 2026"

Links: [{"title":"[2605.07180] Learning Agent Routing From Early Experience","url":"https://arxiv.org/abs/2605.07180"},{"title":"Learning Agent Routing From Early Experience","url":"https://arxiv.org/html/2605.07180"},{"title":"Agent Learning via Early Experience","url":"https://arxiv.org/pdf/2510.08558"},{"title":"[2510.08558] Agent Learning via Early Experience","url":"https://arxiv.org/abs/2510.08558"},{"title":"[2510.08558v1] Agent Learning via Early Experience","url":"https://arxiv.org/abs/2510.08558v1"},{"title":"Preprint. Experiential Reinforcement Learning","url":"https://arxiv.org/pdf/2602.13949"},{"title":"Learning to Route: A Rule-Driven Agent Framework for Hybrid-Source Retrieval-Augmented Generation","url":"https://arxiv.org/html/2510.02388"},{"title":"The Richness of Experience: Agent-Based Learning Reveals the Mechanisms of Early Language Acquisition | bioRxiv","url":"https://www.biorxiv.org/content/10.64898/2026.03.28.715023v1"},{"title":"Learning to Continually Learn via Meta-learning Agentic Memory Designs","url":"https://arxiv.org/pdf/2602.07755"},{"title":"Building Self-Evolving Agents via Experience-Driven Lifelong Learning: A Framework and Benchmark","url":"https://arxiv.org/html/2508.19005v5"}]

I found a highly relevant arXiv paper matching your search query. Here are the key findings:

## Learning Agent Routing From Early Experience

The paper "Learning Agent Routing From Early Experience" was submitted on May 8, 2026 and is available on arXiv as paper 2605.07180.

### Main Contribution

The paper proposes BoundaryRouter, a training-free routing framework that uses early behavioral experience and rubric-guided reasoning to decide whether to answer a query with direct LLM inference or escalate to an agent.

### Key Method

BoundaryRouter builds a compact experience memory by executing both systems on a shared seed set and retrieves similar cases at inference time to guide routing decisions.

### Results

Experiments show that BoundaryRouter reduces inference time by 60.6% compared to the agent while improving performance by 28.6% over direct LLM inference, outperforming prompt-based and retrieval-only routing by an average of 37.9% and 8.2%, respectively.

### Evaluation

The authors introduce RouteBench, a benchmark covering in-domain, paraphrased, and out-of-domain route settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87c1faa5-efda-4cd5-8e25-3847caf9c18a",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "0d5f12b8-edc6-48ff-9d4d-44929013e0cf",
  "sourceToolAssistantUUID": "87c1faa5-efda-4cd5-8e25-3847caf9c18a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-11T23:39:23.740Z_

<details><summary>↩ Tool result · `toolu_01Lo6sW98jTjd5By4x27wZu7`</summary>

```text
Web search results for query: "Router-R1 multi-round routing aggregation reinforcement learning LLM 2026"

Links: [{"title":"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=DWf4vroKWJ"},{"title":"[2506.09033] Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning","url":"https://arxiv.org/abs/2506.09033"},{"title":"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning","url":"https://ulab-uiuc.github.io/Router-R1/"},{"title":"Paper page - Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning","url":"https://huggingface.co/papers/2506.09033"},{"title":"Router-R1: Teaching LLMs Multi-Round Routing and ...","url":"https://arxiv.org/pdf/2506.09033"},{"title":"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning","url":"https://arxiv.org/html/2506.09033v3"},{"title":"Tao Feng","url":"https://ft2023.github.io/taofeng.github.io/"},{"title":"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.09033v1"},{"title":"NeurIPS Poster Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119214"},{"title":"[2506.09033v2] Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning","url":"https://arxiv.org/abs/2506.09033v2"}]

I found comprehensive information about Router-R1. Here's what the search results reveal:

## Overview

Router-R1 is a reinforcement learning (RL)-based framework that formulates multi-LLM routing and aggregation as a sequential decision process.

## Key Innovation

Router-R1 instantiates the router itself as a capable LLM, leveraging its reasoning ability to interleave "think" actions (internal deliberation) with "route" actions (dynamic model invocation), and integrates each response into its evolving context. This addresses a key limitation: existing LLM routers typically perform a single-round, one-to-one mapping (assigning each query to a single model in isolation), which limits their capability to tackle complex tasks that demand the complementary strengths of multiple LLMs.

## Training Approach

The framework employs a lightweight rule-based reward comprising format rewards, final outcome rewards, and a novel cost reward for optimizing the balance between performance and cost. Router-R1 also conditions only on simple model descriptors such as pricing, latency, and example performance, enabling strong generalization to unseen model selection.

## Performance and Impact

Experiments on seven general and multi-hop QA benchmarks show that Router-R1 outperforms several strong baselines, achieving superior performance while maintaining robust generalization and cost management. Router-R1 was accepted at NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd0a4991-f0af-48f0-8339-7579b938ecc0",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "2e71540c-a2b2-40ac-bc86-4ffa53b3da69",
  "sourceToolAssistantUUID": "bd0a4991-f0af-48f0-8339-7579b938ecc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-11T23:39:24.365Z_

<details><summary>↩ Tool result · `toolu_017JvsqWu9MwiSTxL6xBUF6T`</summary>

```text
Web search results for query: "CigaR cost efficient program repair LLM token optimization"

Links: [{"title":"1 CigaR: Cost-efficient Program Repair with LLMs","url":"https://arxiv.org/pdf/2402.06598"},{"title":"[2402.06598] CigaR: Cost-efficient Program Repair with LLMs","url":"https://arxiv.org/abs/2402.06598"},{"title":"CigaR: Cost-efficient Program Repair with LLMs","url":"https://arxiv.org/html/2402.06598v2"},{"title":"[2402.06598v1] CigaR: Cost-efficient Program Repair with LLMs","url":"https://arxiv.org/abs/2402.06598v1"},{"title":"CigaR: Cost-efficient Program Repair with LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240206598H/abstract"},{"title":"CigaR: Cost-efficient Program Repair with LLMs","url":"https://github.com/ASSERT-KTH/cigar"},{"title":"[Literature Review] CigaR: Cost-efficient Program Repair with LLMs","url":"https://www.themoonlight.io/en/review/cigar-cost-efficient-program-repair-with-llms"},{"title":"Optimizing Token Consumption in LLMs: A Nano Surge Approach for Code Reasoning Efficiency * Corresponding authors","url":"https://arxiv.org/html/2504.15989v2"},{"title":"Reducing Token Usage of Software Engineering Agents DIPLOMARBEIT","url":"https://repositum.tuwien.at/bitstream/20.500.12708/224666/1/Hrubec%20Nicolas%20-%202025%20-%20Reducing%20Token%20Usage%20of%20Software%20Engineering%20Agents.pdf"},{"title":"Cut LLM Costs 50%: 6 Token Optimization Strategies","url":"https://www.linkedin.com/pulse/token-per-task-economics-6-techniques-cut-llm-spend-50-ercin-dedeoglu-x1o8f"}]

Based on the search results, here's comprehensive information about CigaR:

## Overview

CigaR is the first LLM-based APR (automated program repair) tool that focuses on minimizing the repair cost. Using LLMs can be costly, with companies invoicing users by the number of tokens.

## How It Works

CigaR works in two major steps: generating a first plausible patch and multiplying plausible patches. CigaR optimizes the prompts and the prompt setting to maximize the information given to LLMs using the smallest possible number of tokens.

More specifically, CigaR achieves cost-effectiveness with the help of its three delicately designed prompts: an 'initiation prompt', an 'improvement prompt', and a 'multiplication prompt'. The initiation prompt initializes the repair process. The improvement prompt improves partial patches until a plausible patch is generated, avoiding throwing away potentially useful patches. Finally, the multiplication prompt builds upon the already generated plausible patches to synthesize more plausible patches with diversity maximization.

## Performance Results

CigaR reduces the token cost by 73% on experiments on 429 bugs from the Defects4J and HumanEval-Java datasets. On average, CigaR spends 127k tokens per bug while the baseline uses 467k tokens per bug. In even more optimal cases, on the subset of bugs that are fixed by both, CigaR spends 20k per bug while the baseline uses 608k tokens, a cost saving of 96%.

## Additional Features

CigaR also uses a reboot strategy to allow the model to look into various parts of its search space, instead of spending tokens in dead-ends.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65e558cc-b414-44a7-be65-41d32eb227ac",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "d22db6f4-ca0b-4d76-baca-644ee292d4fc",
  "sourceToolAssistantUUID": "65e558cc-b414-44a7-be65-41d32eb227ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-11T23:39:24.701Z_

<details><summary>↩ Tool result · `toolu_01JwsBjuoQzwjpJSa7mAeNC3`</summary>

```text
Web search results for query: "GraphRAG-Router cost efficient routing reinforcement learning 2026"

Links: [{"title":"GraphRAG-Router: Learning Cost-Efficient Routing over GraphRAGs and LLMs with Reinforcement Learning","url":"https://arxiv.org/html/2604.16401v1"},{"title":"GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs | OpenReview","url":"https://openreview.net/forum?id=ZdGB7MNQDT"},{"title":"Published as a conference paper at ICLR 2026 GRAPHPLANNER:","url":"https://openreview.net/pdf?id=ZdGB7MNQDT"},{"title":"ICLR Poster GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs","url":"https://iclr.cc/virtual/2026/poster/10008792"},{"title":"Graph-R1: An Agentic GraphRAG Framework for Structured, Multi-Turn Reasoning with Reinforcement Learning - MarkTechPost","url":"https://www.marktechpost.com/2025/08/09/graph-r1-an-agentic-graphrag-framework-for-structured-multi-turn-reasoning-with-reinforcement-learning/"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"GraphRouter: A Graph-based Router for LLM Selections | OpenReview","url":"https://openreview.net/forum?id=eU39PDsZtT"},{"title":"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=PkwJjGJ7aN"},{"title":"RouteRAG: Efficient Retrieval-Augmented Generation from Text and Graph via Reinforcement Learning","url":"https://arxiv.org/html/2512.09487v1"},{"title":"GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs [Quick Review]","url":"https://liner.com/review/graphplanner-graph-memoryaugmented-agentic-routing-for-multiagent-llms"}]

Based on the search results, I found detailed information about GraphRAG-Router, a cost-efficient routing framework using reinforcement learning.

## GraphRAG-Router: Cost-Efficient Routing Framework

GraphRAG-Router is a cost-efficient framework that adopts a hierarchical routing strategy to coordinate heterogeneous GraphRAGs and generator LLMs.

### Key Problem
Existing GraphRAG systems are typically built in a one-size-fits-all manner, relying on a fixed retrieval framework and a single, often large and costly, generator LLM for all queries, which limits their ability to adapt to the complexity of varying questions and often incurs unnecessary computational cost.

### Training Approach
GraphRAG-Router is first warmed up through supervised fine-tuning and then optimized with a two-stage reinforcement learning procedure, whose second stage introduces a curriculum cost-aware reward to encourage difficulty-aware and economical generation.

### Evaluation Setup
The framework was evaluated across multiple GraphRAG systems. Five representative GraphRAG frameworks were selected: GraphRAG, RAPTOR, HippoRAG2, HyperGraphRAG, and LinearRAG. For generator LLMs, five cutting-edge LLMs covering three scale ranges were selected: Small models including Qwen2.5-7B-Instruct, LLaMA3.1-8B-Instruct, and Ministral-8B-2512.

This research represents a 2026 advance in making GraphRAG systems more efficient by dynamically routing queries to appropriate retrieval and generation combinations based on query complexity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19732eb1-6fc0-41c5-8416-d2701fab0f56",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "9d9bd622-cb0d-4548-953e-823c486cc18f",
  "sourceToolAssistantUUID": "19732eb1-6fc0-41c5-8416-d2701fab0f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-11T23:39:24.709Z_

<details><summary>↩ Tool result · `toolu_01Q2FHV4eci4ypqes2ACVtvq`</summary>

```text
Web search results for query: ""compressing code context" LLM issue resolution SWE-bench 2026"

Links: [{"title":"Compressing Code Context for LLM-based Issue Resolution","url":"https://arxiv.org/html/2603.28119"},{"title":"[2603.28119] Compressing Code Context for LLM-based Issue Resolution","url":"https://arxiv.org/abs/2603.28119"},{"title":"Compressing Code Context for LLM-based Issue Resolution Haoxiang Jia","url":"https://arxiv.org/pdf/2603.28119"},{"title":"A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression","url":"https://arxiv.org/html/2604.19572v1"},{"title":"Best LLMs in May 2026, What Actually Matters in Production","url":"https://futureagi.substack.com/p/best-llms-in-may-2026-what-actually"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios","url":"https://arxiv.org/html/2512.18470v5"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"SWE Context Bench: A Benchmark for Context Learning in Coding","url":"https://arxiv.org/html/2602.08316"}]

Based on the search results, I found highly relevant information about compressing code context for LLM-based issue resolution on SWE-bench. Here's what I found:

## Overview

A recent study evaluated on SWE-Bench Verified demonstrates that SWEzze significantly reduces the cost of LLM-based issue resolution while at the same time improving success rate.

## The Problem

Current approaches overapproximate the code context and suffer from two compounding problems: the prohibitive cost of processing massive inputs, and low effectiveness as noise floods the context window and distracts the model from the bug-fixing signal.

## The Solution: SWEzze

The approach uses Oracle-guided Code Distillation (OCD), a context distillation algorithm that combines genetic search and delta debugging to systematically reduce code contexts to their minimal sufficient subsequence - retaining only the ingredients required for a successful fix, and fine-tunes SWEzze, a lightweight model that learns to compress code context at inference time.

## Key Results

Evaluated on SWE-bench Verified across three frontier LLMs, SWEzze maintains a stable compression rate of about 6 times across models, reduces the total token budget by 51.8%-71.3% relative to the uncompressed setting, and improves issue resolution rates by 5.0%-9.2%.

## Why This Matters

Unlike prior compressors that rely on perplexity or lexical similarity, SWEzze is trained on minimal sufficient contexts produced by Oracle-guided Code Distillation, which identifies the smallest context subsequence that still enables a correct patch, thus capturing ingredients required for issue resolution rather than surface-level relatedness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6251b3db-5739-4378-9ef6-d93e78e0c3e5",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "ffd7173d-abf3-4ba0-92d0-daff9c167d28",
  "sourceToolAssistantUUID": "6251b3db-5739-4378-9ef6-d93e78e0c3e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-11T23:39:26.111Z_

<details><summary>↩ Tool result · `toolu_01BtzoQtK83Y7x7kR1Ehr2FH`</summary>

```text
Web search results for query: ""optimize chunking granularity" retrieval augmented generation COLING 2025"

Links: [{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.384/"},{"title":"GitHub - ZGChung/Mix-of-Granularity: [COLING 2025] Mix-of-Granularity paper","url":"https://github.com/ZGChung/Mix-of-Granularity"},{"title":"Optimize the Chunking Granularity for Retrieval- ...","url":"https://aclanthology.org/2025.coling-main.384.pdf"},{"title":"[2406.00456] Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2406.00456"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2406.00456v1"},{"title":"Computation and Language Jun 2024","url":"https://web3.arxiv.org/list/cs.CL/2024-06?skip=1785&show=2000"},{"title":"Computer Science Jun 2024","url":"https://arxiv.org/list/cs/2024-06?skip=200&show=100"},{"title":"Chunking Optimization for Retrieval-Augmented Generation","url":"https://www.squareboat.com/blog/chunking-optimization-for-retrieval-augmented-generation"},{"title":"Chunking Strategies for Retrieval-Augmented Generation (RAG): A Comprehensive Guide | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/chunking-strategies-for-retrieval-augmented-generation-rag-a-comprehensive-guide-5522c4ea2a90"},{"title":"RAG in 2025: 7 Proven Strategies to Deploy Retrieval-Augmented Generation at Scale | Morphik Blog","url":"https://www.morphik.ai/blog/retrieval-augmented-generation-strategies"}]

Based on the web search results, I found detailed information about the paper you're looking for. Here's what I found:

## Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation

This paper was authored by Zijie Zhong, Hanwen Liu, Xiaoya Cui, Xiaofan Zhang, and Zengchang Qin and was accepted to COLING 2025.

### Main Approach

The paper introduces Mix-of-Granularity (MoG), a method that dynamically determines the optimal granularity of a knowledge source based on input queries using a router. The router is efficiently trained with a newly proposed loss function employing soft labels.

### Extensions and Results

The authors further extend MoG to MoG-Graph (MoGG), where reference documents are pre-processed as graphs, enabling the retrieval of distantly situated snippets. Experiments demonstrate that MoG and MoGG effectively predict optimal granularity levels, significantly enhancing the performance of the RAG system in downstream tasks.

### Problem Motivation

The work addresses the challenge that integrating information from various reference databases is difficult because each knowledge source adopts a unique data structure and follows different conventions, and retrieving from multiple knowledge sources with one fixed strategy usually leads to under-exploitation of information.

The code of both MoG and MoGG will be made public.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05892713-1848-4f57-984d-b338c2722e83",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "caf66ca8-7acc-4ad3-90b6-425230cafab1",
  "sourceToolAssistantUUID": "05892713-1848-4f57-984d-b338c2722e83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-11T23:39:29.598Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012BRQyKDSoL15fA25JzmXEE`</summary>

```json
{
  "query": "\"SWE Context Bench\" benchmark context learning coding 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caf66ca8-7acc-4ad3-90b6-425230cafab1",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfT9tfLDCVJ89sST5C7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "984b1219-2b03-4402-8380-ed77b6ec10c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5RSTURptuhUbE7wQDWgps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9525,
      "cache_read_input_tokens": 30750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9525,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-11T23:39:30.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NADVHGwqSGuBXeFRi5kDFB`</summary>

```json
{
  "query": "LongCodeZip code compression function level perplexity 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "984b1219-2b03-4402-8380-ed77b6ec10c7",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfT9tfLDCVJ89sST5C7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13b04f3b-c8a5-40fd-9a75-f72b8b372e9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5RSTURptuhUbE7wQDWgps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9525,
      "cache_read_input_tokens": 30750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9525,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-11T23:39:31.427Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016NvJqgpBFpeCPKWnCRTo4m`</summary>

```json
{
  "query": "\"less is more\" adaptive program repair bug localization preference learning AAAI 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13b04f3b-c8a5-40fd-9a75-f72b8b372e9a",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfT9tfLDCVJ89sST5C7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69c6ceef-6d66-4ce3-8d86-309c82a1a0f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5RSTURptuhUbE7wQDWgps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9525,
      "cache_read_input_tokens": 30750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9525,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-11T23:39:31.757Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KrgGWnnLEjKsn95PrvCUVD`</summary>

```json
{
  "query": "RepairAgent autonomous LLM agent program repair 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69c6ceef-6d66-4ce3-8d86-309c82a1a0f8",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfT9tfLDCVJ89sST5C7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "377c346d-710f-40b1-8253-79d14c078cc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5RSTURptuhUbE7wQDWgps",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9525,
      "cache_read_input_tokens": 30750,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9525
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 30750,
          "cache_creation_input_tokens": 9525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9525,
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

_source line 73 · 2026-05-11T23:39:37.065Z_

<details><summary>↩ Tool result · `toolu_01NADVHGwqSGuBXeFRi5kDFB`</summary>

```text
Web search results for query: "LongCodeZip code compression function level perplexity 2025"

Links: [{"title":"LongCodeZip: Compress Long Context for Code Language Models","url":"https://www.arxiv.org/pdf/2510.00446"},{"title":"GitHub - YerbaPage/LongCodeZip: LongCodeZip: Compress Long Context for Code Language Models [ASE2025] · GitHub","url":"https://github.com/YerbaPage/LongCodeZip"},{"title":"LongCodeZip: Compress Long Context for Code Language Models (ASE 2025 - Research Papers) - ASE 2025","url":"https://conf.researchr.org/details/ase-2025/ase-2025-papers/121/LongCodeZip-Compress-Long-Context-for-Code-Language-Models"},{"title":"[2510.00446v1] LongCodeZip: Compress Long Context for Code Language Models","url":"https://arxiv.org/abs/2510.00446v1"},{"title":"[2510.00446] LongCodeZip: Compress Long Context for Code Language Models","url":"https://arxiv.org/abs/2510.00446"},{"title":"LongCodeZip: Compress Long Context for Code Language Models","url":"https://arxiv.org/html/2510.00446v1"},{"title":"Paper page - LongCodeZip: Compress Long Context for Code Language Models","url":"https://huggingface.co/papers/2510.00446"},{"title":"(PDF) LongCodeZip: Compress Long Context for Code Language Models","url":"https://www.researchgate.net/publication/396094482_LongCodeZip_Compress_Long_Context_for_Code_Language_Models"},{"title":"[Quick Review] LongCodeZip: Compress Long Context for Code Language Models","url":"https://liner.com/review/longcodezip-compress-long-context-for-code-language-models"},{"title":"LongCodeZip: Compress Long Context for Code Language Models | by Dixon | Medium","url":"https://medium.com/@huguosuo/longcodezip-compress-long-context-for-code-language-models-6253d836e599"}]

I found comprehensive information about LongCodeZip and its use of perplexity for code compression. Here's what the search results show:

## LongCodeZip Overview

LongCodeZip is a novel plug-and-play code compression framework designed specifically for code LLMs. LongCodeZip is the first framework specifically designed for long-context code compression and to introduce perplexity-based block detection, providing an efficient and general-purpose solution that preserves task-critical content within strict token limitations.

## Function-Level Perplexity Compression

The framework employs a two-stage compression strategy:

1. **Coarse-Grained Compression**: The source code is divided into function-level chunks, which are ranked by their relevance to the instruction using conditional perplexity.

2. **Fine-Grained Compression**: Each retained function is further segmented into semantic blocks via perplexity-based chunking.

## Adaptive Budget Allocation

An adaptive budget allocation mechanism distributes the fine-grained token budget proportionally to function importance. Functions with higher AMI scores receive more token budgets, preserving greater detail, while very small functions are kept in full.

## Performance Results

Evaluations across multiple tasks, including code completion, summarization, and question answering, show that LongCodeZip consistently outperforms baseline methods, achieving up to a 5.6x compression ratio without degrading task performance.

The paper was accepted to ASE 2025 and represents a significant advancement in code-specific compression for long contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13b04f3b-c8a5-40fd-9a75-f72b8b372e9a",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "3fb49dd0-5678-4e6d-9953-1f80fd834084",
  "sourceToolAssistantUUID": "13b04f3b-c8a5-40fd-9a75-f72b8b372e9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-11T23:39:38.759Z_

<details><summary>↩ Tool result · `toolu_01KrgGWnnLEjKsn95PrvCUVD`</summary>

```text
Web search results for query: "RepairAgent autonomous LLM agent program repair 2025"

Links: [{"title":"[2403.17134] RepairAgent: An Autonomous, LLM-Based Agent for Program Repair","url":"https://arxiv.org/abs/2403.17134"},{"title":"GitHub - sola-st/RepairAgent: RepairAgent is an autonomous LLM-based agent for software repair. · GitHub","url":"https://github.com/sola-st/RepairAgent"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair Islem Bouzenia","url":"https://software-lab.org/publications/icse2025_RepairAgent.pdf"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00157"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair Islem Bouzenia","url":"https://arxiv.org/pdf/2403.17134"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11029914/"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | Request PDF","url":"https://www.researchgate.net/publication/392956389_RepairAgent_An_Autonomous_LLM-Based_Agent_for_Program_Repair"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair","url":"https://arxiv.org/html/2403.17134"},{"title":"GitHub - GLEAM-Lab/ProgramRepair: A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications · GitHub","url":"https://github.com/GLEAM-Lab/ProgramRepair"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair | ELLIS Unit Stuttgart","url":"https://ellis-stuttgart.eu/publications/icse2025-RepairAgent/"}]

I found comprehensive information about RepairAgent. Here are the key findings:

## Overview

RepairAgent is the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM).

## How It Works

Unlike existing deep learning-based approaches, which prompt a model with a fixed prompt or in a fixed feedback loop, RepairAgent treats the LLM as an agent capable of autonomously planning and executing actions to fix bugs by invoking suitable tools. RepairAgent freely interleaves gathering information about the bug, gathering repair ingredients, and validating fixes, while deciding which tools to invoke based on the gathered information and feedback from previous fix attempts.

## Key Components

Key contributions that enable RepairAgent include a set of tools that are useful for program repair, a dynamically updated prompt format that allows the LLM to interact with these tools, and a finite state machine that guides the agent in invoking the tools.

## Performance Results

RepairAgent's evaluation on the popular Defects4J dataset demonstrates its effectiveness in autonomously repairing 164 bugs, including 39 bugs not fixed by prior techniques.

## Costs

Interacting with the LLM imposes an average cost of 270,000 tokens per bug, which, under the current pricing of OpenAI's GPT-3.5 model, translates to 14 cents of USD per bug.

## Publication

The research was published in the Proceedings of the 47th International Conference on Software Engineering (ICSE) in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "377c346d-710f-40b1-8253-79d14c078cc2",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "d778a473-de6e-45c1-b455-092e16f36874",
  "sourceToolAssistantUUID": "377c346d-710f-40b1-8253-79d14c078cc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-11T23:39:39.272Z_

<details><summary>↩ Tool result · `toolu_012BRQyKDSoL15fA25JzmXEE`</summary>

```text
Web search results for query: ""SWE Context Bench" benchmark context learning coding 2026"

Links: [{"title":"[2602.08316] SWE Context Bench: A Benchmark for Context Learning in Coding","url":"https://arxiv.org/abs/2602.08316"},{"title":"SWE Context Bench: A Benchmark for Context Learning in Coding","url":"https://arxiv.org/html/2602.08316v3"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"SWE Context Bench: A Benchmark for Context Learning in Coding Jared Zhu","url":"https://www.arxiv.org/pdf/2602.08316"},{"title":"Overview - SWE-bench","url":"https://www.swebench.com/SWE-bench/"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"Paper page - SWE Context Bench: A Benchmark for Context Learning in Coding","url":"https://huggingface.co/papers/2602.08316"}]

Based on the search results, here's what I found about SWE Context Bench:

## Overview

SWE-ContextBench is a benchmark designed to explicitly evaluate context understanding and retrieval in coding agents. The benchmark was submitted on February 9, 2026, with the latest revision on May 6, 2026.

## Benchmark Composition

SWE-ContextBench consists of 1,100 base tasks with another 376 related tasks derived from real dependency and reference relationships among GitHub issues and pull requests, grouped across 51 unique repositories and 9 programming languages.

## Purpose and Evaluation

Current benchmarks mainly evaluate whether the agent can correctly solve the request or fix bugs, and they largely treat tasks as independent and do not assess whether agents can reuse previous experience across related problems. The SWE-ContextBench benchmark evaluates how accurately and efficiently agents solve related issues when prior cases are available in context.

## Key Findings

Accurately summarized and retrieved previous experience can significantly improve resolution accuracy and reduce runtime and token cost, particularly on harder tasks, while unfiltered or incorrectly selected context provides limited or negative benefits.

In tests on the benchmark's Lite version, Supermemory performed best overall, achieving a 55.95% FAIL_TO_PASS test rate and the highest resolution rate of 30.30%, while maintaining strong PASS_TO_PASS scores of 90.23% at test level, suggesting gains without performance regressions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "984b1219-2b03-4402-8380-ed77b6ec10c7",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "78d81213-facb-4420-b922-f62d7bce4fba",
  "sourceToolAssistantUUID": "984b1219-2b03-4402-8380-ed77b6ec10c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-11T23:39:39.619Z_

<details><summary>↩ Tool result · `toolu_016NvJqgpBFpeCPKWnCRTo4m`</summary>

```text
Web search results for query: ""less is more" adaptive program repair bug localization preference learning AAAI 2025"

Links: [{"title":"Less Is More: Adaptive Program Repair with Bug Localization and Preference Learning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/31988"},{"title":"[2503.06510] Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://arxiv.org/abs/2503.06510"},{"title":"Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://arxiv.org/html/2503.06510v1"},{"title":"dblp: AAAI 2025","url":"https://dblp.org/db/conf/aaai/aaai2025.html"},{"title":"(PDF) Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://www.researchgate.net/publication/389715232_Less_is_More_Adaptive_Program_Repair_with_Bug_Localization_and_Preference_Learning"},{"title":"Less is More: Adaptive Program Repair","url":"https://arxiv.org/pdf/2503.06510"},{"title":"GitHub - zhenlongDai/AdaPatcher: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://github.com/zhenlongDai/AdaPatcher"},{"title":"AAAI-25 Full Poster Schedule 2.23.25.xlsx","url":"https://aaai.org/wp-content/uploads/2025/02/AAAI-25-Thursday-Poster-Session-All-Tracks-2.23.pdf"},{"title":"[Literature Review] Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://www.themoonlight.io/en/review/less-is-more-adaptive-program-repair-with-bug-localization-and-preference-learning"},{"title":"Date/Time Paper ID Paper Title Authors Thursday February 27, 12:30pm-2:30pm","url":"https://aaai.org/wp-content/uploads/2025/02/AAAI-25-Main-Track-Poster-Schedule-2.21.pdf"}]

I found the paper you're looking for! Here's a summary of the search results:

## "Less Is More: Adaptive Program Repair with Bug Localization and Preference Learning"

The paper proposes AdaPatcher (Adaptive Patch Generator), a two-stage approach where the first stage utilizes a Bug Locator with self-debug learning to accurately pinpoint bug locations, and the second stage trains a Program Modifier to ensure consistency between the post-modified fixed code and the pre-modified buggy code.

The Program Modifier is enhanced with a location-aware repair learning strategy to generate patches based on identified buggy lines, a hybrid training strategy for selective reference, and an adaptive preference learning to prioritize fewer changes.

The paper introduces a novel task called AdaPR (Adaptive Program Repair). Most existing research focuses on generating correct patches while ignoring the consistency between the fixed code and the original buggy code, and how to conduct adaptive bug fixing and generate patches with minimal modifications have seldom been investigated.

The experimental results show that the approach outperforms a set of baselines by a large margin, validating the effectiveness of the two-stage framework for the AdaPR task.

The paper was published at AAAI 2025 and is available on both the AAAI conference proceedings and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69c6ceef-6d66-4ce3-8d86-309c82a1a0f8",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "78c6c47c-d232-426d-9c91-6934675c19a2",
  "sourceToolAssistantUUID": "69c6ceef-6d66-4ce3-8d86-309c82a1a0f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-11T23:39:43.459Z_

Now let me search for a few final potentially highly-relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78c6c47c-d232-426d-9c91-6934675c19a2",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfU9Z6fwbRknxsPMQ1m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b53487a4-79e8-4cf0-94e1-ed8f3fe90776",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY8DaNHTjjPR4bPJ2ZSayZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 2861,
      "cache_read_input_tokens": 40275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2861,
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

_source line 78 · 2026-05-11T23:39:44.957Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JWVkXhRNquHYugFvFRSmMp`</summary>

```json
{
  "query": "\"fault localization context\" LLM program repair empirical study 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b53487a4-79e8-4cf0-94e1-ed8f3fe90776",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfU9Z6fwbRknxsPMQ1m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d61d4b0-711d-4e52-8345-069ad2d28962",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY8DaNHTjjPR4bPJ2ZSayZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 2861,
      "cache_read_input_tokens": 40275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2861,
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

_source line 79 · 2026-05-11T23:39:45.099Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S8MtcTu5ATAozmfWDYP4XV`</summary>

```json
{
  "query": "RouteProfile LLM routing profile framework 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d61d4b0-711d-4e52-8345-069ad2d28962",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfU9Z6fwbRknxsPMQ1m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d683be73-b4e6-44a9-95eb-377bc382e36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY8DaNHTjjPR4bPJ2ZSayZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 2861,
      "cache_read_input_tokens": 40275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2861,
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

_source line 80 · 2026-05-11T23:39:45.451Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LFz5xwbDzeVRD2VHWn2WpC`</summary>

```json
{
  "query": "GraphRouter graph-based router LLM selection 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d683be73-b4e6-44a9-95eb-377bc382e36b",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfU9Z6fwbRknxsPMQ1m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e8cfd2a-e8ca-4d20-8afa-cbcbc58ea8b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY8DaNHTjjPR4bPJ2ZSayZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 2861,
      "cache_read_input_tokens": 40275,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2861
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 950,
          "output_tokens": 180,
          "cache_read_input_tokens": 40275,
          "cache_creation_input_tokens": 2861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2861,
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

_source line 81 · 2026-05-11T23:39:51.991Z_

<details><summary>↩ Tool result · `toolu_01JWVkXhRNquHYugFvFRSmMp`</summary>

```text
Web search results for query: ""fault localization context" LLM program repair empirical study 2026 arXiv"

Links: [{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481"},{"title":"[2604.05481] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481"},{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260118044S/abstract"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372v3"},{"title":"Order Matters! An Empirical Study on Large Language Models’ Input Order Bias in Software Fault Localization","url":"https://arxiv.org/html/2412.18750"},{"title":"Assessing the effectiveness of recent closed-source large language models in fault localization and automated program repair | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00549-x"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"Large Language Models in Fault Localisation","url":"https://arxiv.org/pdf/2308.15276"}]

Based on the search results, I found the paper you were looking for! Here are the key findings:

## "On the Role of Fault Localization Context for LLM-Based Program Repair"

This is a large-scale empirical study on 500 SWE-bench Verified instances using GPT-5-mini, evaluating 61 configurations that vary file-level, element-level, and line-level context. The paper was published on arXiv on April 7, 2026 (arXiv:2604.05481).

### Key Findings:

1. **Context Quality Over Quantity**: The results show that more context does not consistently improve repair performance, with file-level localization being the dominant factor, yielding a 15-17x improvement over a no-file baseline.

2. **Optimal File Context**: Expanding file context is often associated with improved performance, with successful repairs most commonly observed in configurations with approximately 6-10 relevant files.

3. **Element and Line-Level Context Effects**: Element-level context expansion provides conditional gains that depend strongly on the file context quality, while line-level context expansion frequently degrades performance due to noise amplification.

4. **Best Strategy**: The most effective FL context strategy typically combines a broad semantic understanding at higher abstraction levels with precise line-level localization.

5. **Retrieval Method**: LLM-based retrieval generally outperforms structural heuristics while using fewer files and tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d61d4b0-711d-4e52-8345-069ad2d28962",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "effe1055-e959-4f52-9dde-a323b3686325",
  "sourceToolAssistantUUID": "7d61d4b0-711d-4e52-8345-069ad2d28962",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-11T23:39:53.228Z_

<details><summary>↩ Tool result · `toolu_01LFz5xwbDzeVRD2VHWn2WpC`</summary>

```text
Web search results for query: "GraphRouter graph-based router LLM selection 2025"

Links: [{"title":"[2410.03834] GraphRouter: A Graph-based Router for LLM Selections","url":"https://arxiv.org/abs/2410.03834"},{"title":"GraphRouter: A Graph-based Router for LLM Selections | OpenReview","url":"https://openreview.net/forum?id=eU39PDsZtT"},{"title":"GitHub - ulab-uiuc/GraphRouter: [ICLR 2025] \"GraphRouter: A Graph-based Router for LLM Selections\", Tao Feng, Yanzhen Shen, Jiaxuan You","url":"https://github.com/ulab-uiuc/GraphRouter"},{"title":"ICLR Poster GraphRouter: A Graph-based Router for LLM Selections","url":"https://iclr.cc/virtual/2025/poster/28926"},{"title":"GraphRouter: A Graph-based Router for LLM Selections","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/41b6674c28a9b93ec8d22a53ca25bc3b-Abstract-Conference.html"},{"title":"graphrouter:agraph-based router for llm selections","url":"https://arxiv.org/pdf/2410.03834"},{"title":"GRAPHROUTER:AGRAPH-BASED ROUTER FOR LLM ...","url":"https://openreview.net/pdf?id=eU39PDsZtT"},{"title":"(PDF) GraphRouter: A Graph-based Router for LLM Selections","url":"https://www.researchgate.net/publication/384699790_GraphRouter_A_Graph-based_Router_for_LLM_Selections"},{"title":"Graph Routers for LLM selection | by Girish Kurup | Medium","url":"https://girishkurup21.medium.com/graph-routers-gnn-50cfe1e63c08"},{"title":"GitHub - ulab-uiuc/LLMRouter: LLMRouter: An Open-Source Library for LLM Routing · GitHub","url":"https://github.com/ulab-uiuc/LLMRouter"}]

## Search Results for GraphRouter: Graph-Based Router for LLM Selection

I found comprehensive information about GraphRouter and its 2025 developments:

### Overview

GraphRouter is a novel inductive graph framework which fully utilizes the contextual information among tasks, queries, and LLMs to enhance the LLM selection process. GraphRouter was accepted for ICLR 2025.

### How It Works

GraphRouter constructs a heterogeneous graph comprising task, query, and LLM nodes, with interactions represented as edges, which efficiently captures the contextual information between the query's requirements and the LLM's capabilities. Through an innovative edge prediction mechanism, GraphRouter is able to predict attributes (the effect and cost of LLM response) of potential edges, allowing for optimized recommendations that adapt to both existing and newly introduced LLMs without requiring retraining.

### Performance Results

Comprehensive experiments across three distinct effect-cost weight scenarios have shown that GraphRouter substantially surpasses existing routers, delivering a minimum performance improvement of 12.3%. It achieves enhanced generalization across new LLMs settings and supports diverse tasks with at least a 9.5% boost in effect and a significant reduction in computational demands.

### Recent 2025 Updates

Router-R1 has officially been released, which is a cutting-edge, reinforcement learning-driven LLM router designed to enable seamless collaboration among multiple LLMs to tackle complex problems efficiently. The code and paper are available on GitHub at the ulab-uiuc/GraphRouter repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e8cfd2a-e8ca-4d20-8afa-cbcbc58ea8b5",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "6e8b7f38-266c-48ba-ba74-5cef925d29e3",
  "sourceToolAssistantUUID": "9e8cfd2a-e8ca-4d20-8afa-cbcbc58ea8b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-11T23:39:53.811Z_

<details><summary>↩ Tool result · `toolu_01S8MtcTu5ATAozmfWDYP4XV`</summary>

```text
Web search results for query: "RouteProfile LLM routing profile framework 2026"

Links: [{"title":"[2605.00180] RouteProfile: Elucidating the Design Space of LLM Profiles for Routing","url":"https://arxiv.org/abs/2605.00180"},{"title":"RouteProfile: Elucidating the Design Space of LLM Profiles for Routing","url":"https://arxiv.org/html/2605.00180"},{"title":"GitHub - ulab-uiuc/LLMRouter: LLMRouter: An Open-Source Library for LLM Routing · GitHub","url":"https://github.com/ulab-uiuc/LLMRouter"},{"title":"GitHub - lm-sys/RouteLLM: A framework for serving and evaluating LLM routers - save LLM costs without compromising quality · GitHub","url":"https://github.com/lm-sys/RouteLLM"},{"title":"RouteLLM: Learning to Route LLMs from Preference Data | OpenReview","url":"https://openreview.net/forum?id=8sSqNntaMr"},{"title":"GitHub - NVIDIA-AI-Blueprints/llm-router: Route LLM requests to the best model for the task at hand. · GitHub","url":"https://github.com/NVIDIA-AI-Blueprints/llm-router"},{"title":"RouteLLM: An Open-Source Framework for Cost-Effective LLM Routing - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2024-07-01-routellm/"},{"title":"RouteLLM – UC Berkeley Sky Computing Lab","url":"https://sky.cs.berkeley.edu/project/routellm/"},{"title":"[2406.18665] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665"},{"title":"RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/pdf/2406.18665"}]

Based on the web search results, here's information about RouteProfile:

## RouteProfile: LLM Routing Profile Framework

RouteProfile is a general design space of LLM profiles developed along four key dimensions: organizational form, representation type, aggregation depth, and learning configuration.

### Key Dimensions

The framework includes:
- **Organizational form** - specifying how interaction histories are organized before integration, such as flat collections or structured relational forms
- **Representation type** - determining whether profiles are expressed as textual summaries or dense embeddings
- **Aggregation depth** - controlling the scope of information integration, ranging from local evidence to broader contextual structure
- **Learning configuration** - indicating whether the profiling process is training-free or optimized through learning

### Research Findings

Through systematic evaluation across three representative routers under both standard and new-LLM generalization settings, the research shows that: (1) structured profiles consistently outperform flat ones; (2) query-level signals are more reliable than coarse domain-level signals; and (3) generalization to newly introduced models benefits most from structured profiles under trainable configurations.

### Recent Release

In May 2026, RouteProfile code and paper were released as a general framework for designing LLM profiles for routing that enables structured profile construction from heterogeneous interaction histories, supports flat, embedding-based, text-GNN, and trainable GNN profiles, and evaluates routing performance across SimRouter, MLPRouter, and GraphRouter under both standard and new-LLM settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d683be73-b4e6-44a9-95eb-377bc382e36b",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "63d52e15-e988-4ce6-ae87-bdf2c9683aed",
  "sourceToolAssistantUUID": "d683be73-b4e6-44a9-95eb-377bc382e36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-11T23:39:56.586Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DvUdREkg5HnheNwJ7jFfeP`</summary>

```json
{
  "query": "\"fault localization granularity\" repository code repair 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63d52e15-e988-4ce6-ae87-bdf2c9683aed",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfVCF73Rggdxp3poEiT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2b41003-6084-4e62-8b5e-7b8fe0569a51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gi3xv2JAF9qrQ1ZfVWZPhV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 943,
      "cache_creation_input_tokens": 2935,
      "cache_read_input_tokens": 43136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2935,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-11T23:39:57.362Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AhFpryrcEU3YCnmWqjV7bA`</summary>

```json
{
  "query": "CodeScout SWE-bench code retrieval agent 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2b41003-6084-4e62-8b5e-7b8fe0569a51",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfVCF73Rggdxp3poEiT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "699f69d7-57c7-4666-b388-efb9c0ee3911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gi3xv2JAF9qrQ1ZfVWZPhV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 943,
      "cache_creation_input_tokens": 2935,
      "cache_read_input_tokens": 43136,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2935
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 943,
          "output_tokens": 121,
          "cache_read_input_tokens": 43136,
          "cache_creation_input_tokens": 2935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2935,
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

_source line 86 · 2026-05-11T23:40:04.797Z_

<details><summary>↩ Tool result · `toolu_01AhFpryrcEU3YCnmWqjV7bA`</summary>

```text
Web search results for query: "CodeScout SWE-bench code retrieval agent 2025 2026"

Links: [{"title":"[2603.17829] CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents","url":"https://arxiv.org/abs/2603.17829"},{"title":"[Paper Note] CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents, Lintang Sutawika+, arXiv'26, 2026.03 · Issue #4983 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4983"},{"title":"GitHub - OpenHands/codescout: Repo for collaboration on OSS agentic code search · GitHub","url":"https://github.com/OpenHands/codescout"},{"title":"CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents","url":"https://arxiv.org/html/2603.17829"},{"title":"CodeScout: Contextual Problem Statement Enhancement for Software Agents","url":"https://arxiv.org/html/2603.05744v1"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"Auggie tops SWE-Bench Pro | Augment Code","url":"https://www.augmentcode.com/blog/auggie-tops-swe-bench-pro"},{"title":"Rethinking Coding Agent Benchmarks | by Stephanie Jarmak | Medium","url":"https://medium.com/@steph.jarmak/rethinking-coding-agent-benchmarks-5cde3c696e4a"},{"title":"SWE-Bench Coding Agent Leaderboard 2026: Claude vs GPT | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/swe-bench-coding-agent-leaderboard/"}]

I found detailed information about CodeScout. Here's what the search reveals:

## CodeScout: A Code Retrieval Agent for SWE-Bench

CodeScout is a model family released with code and data for the community, focused on code localization for software engineering tasks.

### Key Capabilities

CodeScout navigates repositories via a terminal using Unix command-line utilities (like rg, sed, and cat) to localize relevant files, classes, and functions of code. The coding agent is equipped with nothing more than a standard Unix terminal and trained with reinforcement learning to achieve strong results.

### Performance

On three benchmarks (SWE-Bench Verified, Pro, and Lite), CodeScout models consistently achieve superior or competitive performance over 2-18x larger base and post-trained LLMs and sometimes approach performance provided by closed models like Claude Sonnet.

### Technical Approach

The work focuses on techniques for re-purposing existing coding agent environments for code search, reward design, and RL optimization. CodeScout offers multiple model sizes: CodeScout-14B, CodeScout-4B, CodeScout-1.7B, and CodeScout-1.7B-RFT.

### Publication

The research paper was published on March 18, 2026, with the title "CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "699f69d7-57c7-4666-b388-efb9c0ee3911",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "22a7dcec-c61e-4cae-9a0d-f8e4d4360d24",
  "sourceToolAssistantUUID": "699f69d7-57c7-4666-b388-efb9c0ee3911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-11T23:40:05.132Z_

<details><summary>↩ Tool result · `toolu_01DvUdREkg5HnheNwJ7jFfeP`</summary>

```text
Web search results for query: ""fault localization granularity" repository code repair 2026 arXiv"

Links: [{"title":"[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/abs/2604.00167"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale","url":"https://arxiv.org/pdf/2604.00167"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260118044S/abstract"},{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"[2601.18044] RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/abs/2601.18044"},{"title":"[2604.05481] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481"}]

Based on the search results, I found several relevant arXiv papers from 2026 on fault localization granularity and repository-scale code repair:

## Key Papers Found

**1. "A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks" (arXiv:2604.00167)**

This study shows that function-level granularity yields the highest repair rate against line-level and file-level on the SWE-Bench-Mini dataset, though a deeper dive suggests the ideal granularity may be task dependent. The authors modified the localization phase of the Agentless framework to retrieve ground-truth localization data and include it as context in the repair phase.

**2. "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair" (arXiv:2605.03117)**

ARISE augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges, exposing this graph through a three-tier tool API for data-flow slicing. Compared to the SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points, achieving 22.0% Pass@1.

**3. "On the Role of Fault Localization Context for LLM-Based Program Repair" (arXiv:2604.05481)**

The most effective fault localization context strategy typically combines broad semantic understanding at higher abstraction levels with precise line-level localization. Element-level context expansion provides conditional gains that depend strongly on file context quality, while line-level context expansion frequently degrades performance due to noise amplification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2b41003-6084-4e62-8b5e-7b8fe0569a51",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a091ca136193f2c66",
  "type": "user",
  "uuid": "8e0a6132-d732-4cae-9da7-763b7779265d",
  "sourceToolAssistantUUID": "d2b41003-6084-4e62-8b5e-7b8fe0569a51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 88 · 2026-05-11T23:41:23.312Z_

Now I have comprehensive results. Here is my consolidated report.

---

## Competitor Analysis for GranRoute: Papers Potentially Missing from the Proposal

Below are papers found across 10 search queries, organized by relevance category. I have excluded the 17 already-cited papers (RouteLLM, RADAR, BEST-Route, Route-To-Reason, LTRR, Triage, SIADAFIX, AdaPatcher, AdaEdit, SWEzze, SWE-Pruner, CodeScout, ARISE, RPO, DRO, ReCode, RGFL).

---

### TIER 1: HIGH RELEVANCE -- Directly overlapping with GranRoute's contributions

**1. "A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks"**
- arXiv:2604.00167, April 2026
- **Why critical:** This paper directly studies the impact of different FL granularity levels (file, function, line) on repository-scale repair using SWE-bench Mini, finding function-level yields the highest repair rate but the ideal granularity is task-dependent. This is extremely close to GranRoute's core thesis about routing granularity. If not cited, it should be.

**2. "On the Role of Fault Localization Context for LLM-Based Program Repair"**
- arXiv:2604.05481, April 2026
- **Why critical:** Large-scale empirical study on 500 SWE-bench Verified instances evaluating 61 configurations varying file-level, element-level, and line-level context. Finds more context does not consistently help, file-level localization gives 15-17x improvement, and line-level context can degrade performance via noise. Directly validates GranRoute's premise that retrieval configuration matters.

**3. Mix-of-Granularity (MoG)**
- COLING 2025, arXiv:2406.00456
- **Why critical:** Proposes a router that dynamically selects optimal chunking granularity for RAG based on input queries, trained with soft labels. The granularity routing concept is very similar to GranRoute's granularity selection, though applied to general QA rather than code repair.

**4. RAGRouter**
- NeurIPS 2025, arXiv:2505.23052
- **Why relevant:** Routes queries to the best retrieval-augmented LLM using document embeddings and RAG capability embeddings with contrastive learning. First work on LLM routing in the RAG setting. The routing-over-retrieval-configurations concept overlaps with GranRoute.

**5. LongCodeZip**
- ASE 2025, arXiv:2510.00446
- **Why relevant:** Code-specific compression framework with two-stage strategy: coarse-grained (function-level ranking by conditional perplexity) then fine-grained (block-level pruning via knapsack). Uses adaptive budget allocation proportional to function importance. The adaptive context budget idea parallels GranRoute's context budget routing.

**6. "Compressing Code Context for LLM-based Issue Resolution" (the paper describing SWEzze training)**
- arXiv:2603.28119, March 2026
- **Why relevant:** Although SWEzze is already cited, this paper introduces Oracle-guided Code Distillation (OCD) which finds minimal sufficient context subsequences for code repair. The method of learning what context is necessary vs. noise is conceptually related to GranRoute's context budget optimization. Check whether this specific paper (vs. just the SWEzze tool) is cited.

---

### TIER 2: STRONG RELEVANCE -- Overlapping techniques or problem formulation

**7. RouteRAG**
- arXiv:2512.09487, December 2025
- Routes between passage, graph, and hybrid retrieval modes using two-stage RL. End-to-end learned routing over retrieval strategies is conceptually close to GranRoute's retrieval configuration routing.

**8. Router-R1**
- NeurIPS 2025, arXiv:2506.09033
- RL-based multi-round routing and aggregation framework that interleaves "think" and "route" actions. Uses cost-aware reward. The cost-performance trade-off optimization parallels GranRoute's budget-aware routing.

**9. GraphRouter**
- ICLR 2025, arXiv:2410.03834
- Graph-based router for LLM selection using heterogeneous graphs of tasks, queries, and LLMs. Generalizes to new LLMs without retraining. Relevant as a routing methodology competitor.

**10. GraphRAG-Router**
- arXiv:2604.16401, April 2026
- Hierarchical routing over heterogeneous GraphRAGs and generator LLMs using RL with curriculum cost-aware reward. Routes based on query complexity. Relevant for its cost-efficient routing over retrieval configurations.

**11. BoundaryRouter ("Learning Agent Routing From Early Experience")**
- arXiv:2605.07180, May 2026
- Training-free routing framework using early behavioral experience to decide between direct LLM inference vs. agent escalation. Reduces inference time by 60.6%. Relevant as a lightweight routing alternative.

**12. RouteProfile**
- arXiv:2605.00180, May 2026
- General framework for designing LLM profiles for routing across four dimensions (organizational form, representation type, aggregation depth, learning configuration). Systematic study of routing design choices that could inform GranRoute's design.

**13. CigaR**
- arXiv:2402.06598, 2024 (ICSE track)
- Cost-efficient program repair with three-stage prompt design (initiation, improvement, multiplication). Achieves 73% token cost reduction. Relevant as a baseline for cost-efficient repair without adaptive routing.

---

### TIER 3: MODERATE RELEVANCE -- Related problem domain

**14. RepoRepair**
- arXiv:2603.01048, March 2026
- Uses LLM-generated hierarchical code documentation (function-to-file) for repository-level FL and repair. Achieves 45.7% on SWE-bench Lite. Relevant as a retrieval-based repo-level repair competitor.

**15. RelRepair**
- arXiv:2509.16701, September 2025
- RAG approach for program repair with query rewriting, dataset indexing, and similarity retrieval of function signatures and code snippets. Relevant as a retrieval-augmented repair system.

**16. PatchRecall**
- arXiv:2604.10481, April 2026
- Combines codebase retrieval (issue-to-code matching) with history-based retrieval (similar past issues) for file retrieval in APR, with reranking. Directly addresses retrieval quality for code repair.

**17. ReAPR**
- Software Quality Journal 2025
- Retrieval-augmented program repair using BM25/DPR to fetch similar bug-fix pairs from a curated database. Relevant as a retrieval-augmented repair baseline.

**18. MemFL**
- arXiv:2506.03585, 2025
- LLM-based fault localization with external memory (static project summaries + dynamic debugging guidance). Localizes 12.7% more bugs than baselines. Relevant for adaptive, memory-augmented FL.

**19. FlexFL**
- IEEE TSE 2025, arXiv:2411.10714
- Two-stage FL framework: first reduces search space with traditional FL, then uses LLMs to refine. Works with open-source LLMs. Relevant as a flexible FL approach.

**20. LLM4FL**
- OpenReview (under review)
- Multi-agent FL with three specialized agents (Context Extraction, Debugger with Graph-RAG navigation, Reviewer with verbal RL). 18.55% improvement in Top-1 accuracy. Relevant for multi-agent adaptive FL.

**21. LIDL**
- arXiv:2601.05539, January 2026
- Knowledge graph + multi-agent analysis for LLM integration defect localization. First to combine code knowledge graphs with LLM semantic reasoning. Relevant for graph-enhanced FL.

**22. "Towards Defect-Type-Aware Adaptive Program Repair"**
- Software Quality Journal 2026
- Stage-wise approach that adapts repair strategy based on defect type using LLMs. The defect-type-aware adaptation is philosophically similar to GranRoute's per-instance routing.

**23. RepairAgent**
- ICSE 2025, arXiv:2403.17134
- Autonomous LLM agent that dynamically interleaves information gathering, repair ingredient collection, and fix validation using a finite state machine. Relevant as an adaptive repair agent baseline.

**24. SWE-ContextBench**
- arXiv:2602.08316, February 2026
- Benchmark evaluating how accurately/efficiently agents solve related issues when prior context is available. Finds correctly selected context improves resolution while unfiltered context hurts. Validates the premise that context selection matters.

**25. "Learning to Route: A Rule-Driven Agent Framework for Hybrid-Source Retrieval-Augmented Generation"**
- arXiv:2510.02388, October 2025
- Rule-driven routing agent for hybrid-source RAG. Relevant for learned routing over heterogeneous retrieval sources.

---

### TIER 4: CONTEXTUAL / SURVEY PAPERS

**26. "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches"**
- arXiv:2510.04905, October 2025
- Comprehensive survey covering retrieval granularity levels (directory, module, class/function, line) for code generation. Useful for positioning GranRoute's contribution.

**27. "A Survey of LLM-based Automated Program Repair" (TOSEM 2026)**
- arXiv:2506.23749
- Systematic survey categorizing APR into fine-tuning, prompting, procedural, and agentic paradigms with RAG/AAG cross-cutting concerns. Useful for situating GranRoute.

---

### Summary of Most Critical Missing Competitors

The papers most likely to be flagged by reviewers as missing are:

1. **"Impact of FL Granularity for Repository-Scale Code Repair"** (arXiv:2604.00167) -- directly studies the same granularity question on SWE-bench
2. **"On the Role of FL Context for LLM-Based Program Repair"** (arXiv:2604.05481) -- 61-configuration empirical study on context impact
3. **Mix-of-Granularity** (COLING 2025) -- routes optimal chunking granularity, very close concept
4. **RAGRouter** (NeurIPS 2025) -- routing in RAG settings with contrastive learning
5. **LongCodeZip** (ASE 2025) -- adaptive budget allocation for code compression
6. **Router-R1** (NeurIPS 2025) -- RL-based multi-round routing with cost-aware reward
7. **RouteRAG** (arXiv Dec 2025) -- RL for routing between retrieval modes
8. **PatchRecall** (arXiv Apr 2026) -- hybrid retrieval for APR on SWE-bench
9. **RepoRepair** (arXiv Mar 2026) -- hierarchical documentation for repo-level repair

Sources:
- [FL Granularity Study](https://arxiv.org/abs/2604.00167)
- [FL Context Role](https://arxiv.org/abs/2604.05481)
- [Mix-of-Granularity](https://aclanthology.org/2025.coling-main.384/)
- [RAGRouter](https://arxiv.org/abs/2505.23052)
- [LongCodeZip](https://arxiv.org/abs/2510.00446)
- [Router-R1](https://arxiv.org/abs/2506.09033)
- [RouteRAG](https://arxiv.org/abs/2512.09487)
- [PatchRecall](https://arxiv.org/abs/2604.10481)
- [RepoRepair](https://arxiv.org/abs/2603.01048)
- [GraphRouter](https://arxiv.org/abs/2410.03834)
- [GraphRAG-Router](https://arxiv.org/html/2604.16401v1)
- [BoundaryRouter](https://arxiv.org/abs/2605.07180)
- [RouteProfile](https://arxiv.org/abs/2605.00180)
- [CigaR](https://arxiv.org/abs/2402.06598)
- [RelRepair](https://arxiv.org/abs/2509.16701)
- [ReAPR](https://link.springer.com/article/10.1007/s11219-025-09728-1)
- [MemFL](https://arxiv.org/abs/2506.03585)
- [FlexFL](https://arxiv.org/abs/2411.10714)
- [LLM4FL](https://openreview.net/forum?id=z91EvZbSI1)
- [LIDL](https://arxiv.org/abs/2601.05539)
- [Defect-Type-Aware APR](https://link.springer.com/article/10.1007/s11219-026-09751-w)
- [RepairAgent](https://arxiv.org/abs/2403.17134)
- [SWE-ContextBench](https://arxiv.org/abs/2602.08316)
- [SWEzze/OCD paper](https://arxiv.org/abs/2603.28119)
- [RACG Survey](https://arxiv.org/abs/2510.04905)
- [LLM4APR Survey](https://arxiv.org/abs/2506.23749)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e0a6132-d732-4cae-9da7-763b7779265d",
  "isSidechain": true,
  "agentId": "a091ca136193f2c66",
  "requestId": "req_011CawfW2eg5FEktFrsAp5Rz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51bd6586-274c-402e-985c-0fc079f3401b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eixTuKm1bva4VcSU6kLdF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 876,
      "cache_creation_input_tokens": 2046,
      "cache_read_input_tokens": 46071,
      "output_tokens": 3417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2046
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 876,
          "output_tokens": 3417,
          "cache_read_input_tokens": 46071,
          "cache_creation_input_tokens": 2046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2046,
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
