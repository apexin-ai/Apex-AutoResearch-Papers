# Research conversation: You are helping me with adversarial review of a research proposal. I need to search for competing/concurrent work that t

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4a05af61e888eb59.jsonl`
- **Structured JSON:** [`bade6493a885f743a97a.json`](../../sessions/ba/bade6493a885f743a97a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

64 recorded events

### User

_source line 1 · 2026-05-12T00:05:10.858Z_

You are helping me with adversarial review of a research proposal. I need to search for competing/concurrent work that the proposal might have missed. The proposal is about "Adaptive Structural Self-Consistency Scaling" for structured information extraction — sampling multiple schema-constrained extractions from a fine-tuned LLM and aggregating them via structural consistency, with adaptive compute allocation.

Please search for the following using WebSearch:

1. "self-consistency information extraction 2025 2026" — any work applying self-consistency specifically to IE
2. "test-time compute scaling NER relation extraction 2025 2026" — TTS for IE tasks
3. "structured output aggregation LLM 2025 2026" — aggregating structured LLM outputs
4. "confidence-gated sampling structured prediction" — adaptive sampling for structured outputs
5. "ensemble NER LLM 2025 2026" — ensemble methods for NER using LLMs
6. "schema-guided extraction self-consistency" — schema-guided approaches with consistency
7. "XGrammar constrained decoding information extraction" — constrained decoding for IE
8. Search for "Qwen3-8B information extraction fine-tuning" to verify this model is available and suitable
9. Search for recent ACL 2025, NAACL 2025, EMNLP 2025 accepted papers on "test-time scaling" or "self-consistency" to check if any address structured prediction
10. Search "arXiv best-of-N structured prediction 2025 2026" — best-of-N selection for structured outputs

Report all findings. I especially need to know about any work that does self-consistency or test-time scaling specifically for structured/non-scalar outputs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "5125d36f-4bfe-4bd3-9435-e3f8df30b85b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:05:10.862Z_

```json
{
  "parentUuid": "5125d36f-4bfe-4bd3-9435-e3f8df30b85b",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
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
  "uuid": "faff8c0d-ddc2-4d32-a213-6e8e4f7c121a",
  "timestamp": "2026-05-12T00:05:10.862Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:05:13.000Z_



I'll search for all 10 queries in parallel using WebSearch. Let me first load the tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faff8c0d-ddc2-4d32-a213-6e8e4f7c121a",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhR2XptGDRbQePcGuPE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "531f8e0c-4097-4032-b189-1d5c39579198",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJfZwpFvGRnWrcHXzqujyA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 918,
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

_source line 4 · 2026-05-12T00:05:13.493Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01K6mGJUKRqCQgwCu1boeWdc`</summary>

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
  "parentUuid": "531f8e0c-4097-4032-b189-1d5c39579198",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhR2XptGDRbQePcGuPE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "338aca7a-5a73-412f-a66f-2c16e0a98533",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJfZwpFvGRnWrcHXzqujyA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 7304,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 918
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 918,
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

_source line 5 · 2026-05-12T00:05:13.497Z_

<details><summary>↩ Tool result · `toolu_01K6mGJUKRqCQgwCu1boeWdc`</summary>

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
  "parentUuid": "338aca7a-5a73-412f-a66f-2c16e0a98533",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "bb81da22-a006-4e76-afc8-201dd32f9b58",
  "sourceToolAssistantUUID": "338aca7a-5a73-412f-a66f-2c16e0a98533",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:05:15.741Z_



Now let me run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb81da22-a006-4e76-afc8-201dd32f9b58",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhRDri3rRCLdN2sAeX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a81e3f6-0aff-4fb7-8f39-b811343d3ffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrPFccTMpXhMKgwKccAi7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 7 · 2026-05-12T00:05:16.425Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Duex411trJ9s1vhnn8ziby`</summary>

```json
{
  "query": "self-consistency information extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a81e3f6-0aff-4fb7-8f39-b811343d3ffd",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhRDri3rRCLdN2sAeX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2ec0ac0-8638-4a59-a63e-36e2da308815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrPFccTMpXhMKgwKccAi7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 8 · 2026-05-12T00:05:17.194Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018P9EgZHkiErkxBoZR6LTZz`</summary>

```json
{
  "query": "test-time compute scaling NER relation extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2ec0ac0-8638-4a59-a63e-36e2da308815",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhRDri3rRCLdN2sAeX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47451bc8-de6b-4b5e-9599-723a1812c357",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrPFccTMpXhMKgwKccAi7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 9 · 2026-05-12T00:05:17.651Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017cZokf2VPqJrErqUwVz6a9`</summary>

```json
{
  "query": "structured output aggregation LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47451bc8-de6b-4b5e-9599-723a1812c357",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhRDri3rRCLdN2sAeX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "faae334f-db63-4af7-94b2-b69023934375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrPFccTMpXhMKgwKccAi7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 10 · 2026-05-12T00:05:18.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mt2uD1yKpqZspddyr5qaNi`</summary>

```json
{
  "query": "confidence-gated sampling structured prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faae334f-db63-4af7-94b2-b69023934375",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhRDri3rRCLdN2sAeX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87e9306d-6c17-42a1-abeb-80b411a4a2fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrPFccTMpXhMKgwKccAi7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 11 · 2026-05-12T00:05:18.658Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rd15vyfRho4FrP1iCMzDWV`</summary>

```json
{
  "query": "ensemble NER LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87e9306d-6c17-42a1-abeb-80b411a4a2fa",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhRDri3rRCLdN2sAeX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf929f23-11c7-4278-84aa-43398231b150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrPFccTMpXhMKgwKccAi7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 12 · 2026-05-12T00:05:19.136Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G71bo6bXHMTXAUg93jQKHK`</summary>

```json
{
  "query": "schema-guided extraction self-consistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf929f23-11c7-4278-84aa-43398231b150",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhRDri3rRCLdN2sAeX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03206159-0ada-47c7-8c59-bbe4de5433ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrPFccTMpXhMKgwKccAi7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 13 · 2026-05-12T00:05:19.583Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014BFgzw2SQUoZFQazuJnarc`</summary>

```json
{
  "query": "XGrammar constrained decoding information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03206159-0ada-47c7-8c59-bbe4de5433ef",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhRDri3rRCLdN2sAeX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9dadf6db-4273-4709-9c5c-55942a123c24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrPFccTMpXhMKgwKccAi7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 14 · 2026-05-12T00:05:20.520Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0198L5m6cWh4GtXazjsUpk6P`</summary>

```json
{
  "query": "Qwen3-8B information extraction fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dadf6db-4273-4709-9c5c-55942a123c24",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhRDri3rRCLdN2sAeX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8b70a6f-388b-403d-81cd-f52fa8a2ecd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrPFccTMpXhMKgwKccAi7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 15 · 2026-05-12T00:05:21.524Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014AGHMDMko9G4YKutYqPkF8`</summary>

```json
{
  "query": "ACL 2025 NAACL 2025 EMNLP 2025 accepted papers test-time scaling self-consistency structured prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8b70a6f-388b-403d-81cd-f52fa8a2ecd0",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhRDri3rRCLdN2sAeX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fa461c6-745d-4aef-951d-228799d96df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrPFccTMpXhMKgwKccAi7x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 16 · 2026-05-12T00:05:21.911Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P9m22X2Z3EKYHN6CP7J9rM`</summary>

```json
{
  "query": "arXiv best-of-N structured prediction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fa461c6-745d-4aef-951d-228799d96df1",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhRDri3rRCLdN2sAeX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b0293c9-3925-42f9-8387-4911fe755f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrPFccTMpXhMKgwKccAi7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8222,
      "output_tokens": 509,
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
          "output_tokens": 509,
          "cache_read_input_tokens": 8222,
          "cache_creation_input_tokens": 1417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1417,
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

_source line 17 · 2026-05-12T00:05:24.496Z_

<details><summary>↩ Tool result · `toolu_018P9EgZHkiErkxBoZR6LTZz`</summary>

```text
Web search results for query: "test-time compute scaling NER relation extraction 2025 2026"

Links: [{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"[2512.02008] The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/abs/2512.02008"},{"title":"What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models","url":"https://testtimescaling.github.io/"},{"title":"[2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314"},{"title":"Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach | OpenReview","url":"https://openreview.net/forum?id=S3GhJooWIC"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"Evaluating Test-Time Scaling LLMs for Legal Reasoning","url":"https://aclanthology.org/2025.findings-emnlp.742.pdf"},{"title":"A brief history of LLM Scaling Laws and what to expect in 2025","url":"https://www.jonvet.com/blog/llm-scaling-in-2025"},{"title":"GitHub - testtimescaling/testtimescaling.github.io: \"what, how, where, and how well? a survey on test-time scaling in large language models\" repository","url":"https://github.com/testtimescaling/testtimescaling.github.io"},{"title":"Test-Time Scaling Makes Overtraining Compute-Optimal","url":"https://arxiv.org/html/2604.01411v1"}]

Based on the search results, I found relevant information about test-time compute scaling in 2025-2026, though the results focus primarily on general LLM reasoning tasks rather than specifically on NER (Named Entity Recognition) and relation extraction tasks.

## Test-Time Scaling Overview (2025-2026)

Test-time scaling (TTS) has emerged as a prominent research focus, with recent studies demonstrating that TTS can further elicit problem-solving capabilities of large language models, enabling significant breakthroughs in specialized reasoning tasks such as mathematics and coding, as well as in general tasks like open-ended Q&A.

## Recent Research Directions

Test-time scaling involves the dynamic allocation of compute during inference as a promising direction for improving reasoning in large language models. Recent research is structured along four core dimensions: what to scale, how to scale, where to scale, and how well to scale.

## Recent Papers (2025-2026)

Several recent papers address test-time compute scaling:
- A December 2025 paper titled "The Art of Scaling Test-Time Compute for Large Language Models" provides a systematic comparison of TTS strategies.
- A novel language model architecture has been studied that scales test-time computation by implicitly reasoning in latent space using recurrent blocks.

However, the search results do not contain specific information about applying test-time compute scaling techniques specifically to NER and relation extraction tasks. If you're interested in how these techniques apply to those specific NLP tasks, you may want to search for more specialized literature on information extraction with test-time computation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47451bc8-de6b-4b5e-9599-723a1812c357",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "0dc29930-d148-4920-b72a-a9e21857b351",
  "sourceToolAssistantUUID": "47451bc8-de6b-4b5e-9599-723a1812c357",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T00:05:24.875Z_

<details><summary>↩ Tool result · `toolu_01Duex411trJ9s1vhnn8ziby`</summary>

```text
Web search results for query: "self-consistency information extraction 2025 2026"

Links: [{"title":"Self-consistency, Extract and Rectify: Knowledge Graph Enhance Large Language Model for Electric Power Question Answering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-97-5615-5_40"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Difficulty-Adaptive Self-Consistency for Cost-Efficient ...","url":"https://aclanthology.org/2025.findings-naacl.383.pdf"},{"title":"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"Classifying legal interpretations using large language models | Artificial Intelligence and Law | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10506-025-09447-9"},{"title":"Frontiers in Psychology 01 frontiersin.org Self-consistency and congruence,","url":"https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1588734/pdf"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"}]

Based on the web search results, here's what I found about self-consistency in information extraction for 2025-2026:

## Recent Developments in Self-Consistency

Self-consistency has been adapted into a Self-Consistency, Extraction and Rectify framework (SCER) for knowledge graph-enhanced LLM usage in power operations and maintenance question answering scenarios.

## Advanced Self-Consistency Methods (2025-2026)

Recent research has introduced several sophisticated variants:

- Reliability-Aware ASC (ReASC) uses response-level model confidence to permit early halting on high-confidence single answers and weighted aggregation for ambiguous instances, yielding efficiency gains up to 70–80% cost saving versus naive SC

- Confidence-Informed Self-Consistency (CISC) replaces uniform voting with model-derived scalar weights, obtained via response probability, verbal confidence, or tokenwise probability, enabling cost reductions of 40–50% with minor accuracy gains

- Multi-Agent Consensus Alignment (MACA) uses ensembles of models that participate in debate, with trajectories attaining consensus reinforced via RL objectives, resulting in gains that can exceed +27.6 percentage points on GSM8K and +23.7 pp on MATH

## Application to Information Extraction

Research has explored robustifying information extraction via binomial distribution guided counterpart sequences, and LLMs combined with few-shot and zero-shot chain-of-thought prompting with self-consistency lead to robust outcomes for feature extraction while allowing greater resource and time efficiency compared to human annotation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2ec0ac0-8638-4a59-a63e-36e2da308815",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "4ab24b7f-6109-48a4-a943-28e14227faab",
  "sourceToolAssistantUUID": "d2ec0ac0-8638-4a59-a63e-36e2da308815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:05:25.341Z_

<details><summary>↩ Tool result · `toolu_017cZokf2VPqJrErqUwVz6a9`</summary>

```text
Web search results for query: "structured output aggregation LLM 2025 2026"

Links: [{"title":"[2512.23712] STED and Consistency Scoring: A Framework for Evaluating LLM Structured Output Reliability","url":"https://arxiv.org/abs/2512.23712"},{"title":"[2505.04016] SLOT: Structuring the Output of Large Language Models","url":"https://arxiv.org/abs/2505.04016"},{"title":"The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models","url":"https://arxiv.org/html/2604.25359"},{"title":"The guide to structured outputs and function calling with LLMs","url":"https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms"},{"title":"LLM Structured Outputs: The Practical Guide for Every Provider [2026]","url":"https://techsy.io/en/blog/llm-structured-outputs-guide"},{"title":"LLM 2026 statistics: performance analysis and benchmarks for 2026 - Incremys","url":"https://www.incremys.com/en/resources/blog/llm-statistics"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Method for aggregating unstructured data using LLM","url":"https://arxiv.org/html/2604.16425v1"},{"title":"Structured Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/structured_outputs/"},{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information | OpenReview","url":"https://openreview.net/forum?id=H1s6SBhzlg"}]

Based on the web search results, here's what I found regarding structured output aggregation with LLMs in 2025-2026:

## Recent Developments in LLM Structured Output

### Framework and Evaluation Methods

A comprehensive framework for evaluating and improving consistency in LLM-generated structured outputs combines STED (Semantic Tree Edit Distance), a novel similarity metric for comparing JSON outputs, and a consistency scoring framework that aggregates multiple STED measurements across repeated generations to quantify reliability.

### Industry Adoption

As of early 2026, OpenAI, Anthropic, and Google Gemini all support native structured output, with every major provider having adopted the approach by 2025-2026. Structured output uses constrained decoding to ensure every field, type, and constraint in your schema is met — 100% of the time, not "usually."

### Advanced Techniques

SLOT employs a fine-tuned lightweight language model as a post-processing layer, achieving flexibility across various LLMs and schema specifications. A fine-tuned Mistral-7B model with constrained decoding achieves near perfect schema accuracy (99.5%) and content similarity (94.0%), outperforming Claude-3.5-Sonnet by substantial margins.

### Multi-LLM Aggregation

New aggregation algorithms called Optimal Weight (OW) and Inverse Surprising Popularity (ISP) leverage both first-order and second-order information, with theoretical analysis showing these methods provably mitigate inherent limitations of majority voting.

### Data Extraction at Scale

Recent approaches integrate hybrid web scraping, data storage in MongoDB, and intelligent extraction using LLMs into predetermined JSON schemas, with a two-stage verification process to eliminate hallucinations by comparing embeddings of multiple LLM outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faae334f-db63-4af7-94b2-b69023934375",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "ee945264-d92c-4fa5-ac25-88bcf73451b0",
  "sourceToolAssistantUUID": "faae334f-db63-4af7-94b2-b69023934375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T00:05:26.033Z_

<details><summary>↩ Tool result · `toolu_01G71bo6bXHMTXAUg93jQKHK`</summary>

```text
Web search results for query: "schema-guided extraction self-consistency"

Links: [{"title":"TASER: Table Agents for Schema‑guided Extraction and Recommendation","url":"https://arxiv.org/html/2508.13404"},{"title":"GitHub - google/langextract: A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization. · GitHub","url":"https://github.com/google/langextract"},{"title":"Extraction Schema Best Practices: Get Clean, Structured Data from Your Documents - LandingAI","url":"https://landing.ai/developers/extraction-schema-best-practices-get-clean-structured-data-from-your-documents"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable ...","url":"https://aclanthology.org/2025.emnlp-industry.184.pdf"},{"title":"Generative Information Extraction","url":"https://www.emergentmind.com/topics/generative-information-extraction"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"Schema as Parameterized Tools for Universal Information Extraction","url":"https://openreview.net/pdf?id=yoPtjKVtoX"},{"title":"Schema-Driven Information Extraction from Heterogeneous Tables","url":"https://arxiv.org/html/2305.14336v3"},{"title":"Semantic Web 1 (0) 1–4 1 IOS Press 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11","url":"https://www.semantic-web-journal.net/system/files/swj3719.pdf"},{"title":"Structured Outputs: Reliable Schema-Validated Data Extraction from Language Models - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/structured-outputs-schema-validated-data-extraction-language-models"}]

Based on the search results, here's what I found about schema-guided extraction and self-consistency:

## Schema-Guided Extraction

Schema-guided extraction employs advanced sequence-to-sequence models with schema-guided prompts and constrained decoding to directly generate structured outputs like JSON, ensuring consistency and flexibility. In this approach, an LLM is prompted with the current schema embedded in the prompt context and instructed to return structured output, which is immediately parsed and validated against the schema.

## Self-Consistency in Extraction

Self-consistency prompting allows LLMs to consider multiple reasoning paths and offers a mechanism for identifying and correcting errors, enhancing the decision-making process by shifting from simplistic decoding strategy to a more comprehensive reasoning approach.

When applied to knowledge extraction, self-consistency prompting enhances prompts by incorporating an additional layer of reflection, where the instruction asks to first think about entities and relations to extract, then look at potential triples, think like a domain expert and check their validity, filter out the invalid ones, and return the valid triples in JSON format.

## Related Techniques

Recent frameworks like SCOPE implement a systematic validation framework with constrained decoding and static rule checking, enabling agents to self-correct through structured reflection, including checks for missing attributes, grounding verification, and rule compliance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03206159-0ada-47c7-8c59-bbe4de5433ef",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "bed1603f-8491-4e20-9db2-e3eea9365dba",
  "sourceToolAssistantUUID": "03206159-0ada-47c7-8c59-bbe4de5433ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T00:05:26.397Z_

<details><summary>↩ Tool result · `toolu_01Mt2uD1yKpqZspddyr5qaNi`</summary>

```text
Web search results for query: "confidence-gated sampling structured prediction"

Links: [{"title":"Confidence Estimation Techniques","url":"https://www.emergentmind.com/topics/confidence-estimation-techniques"},{"title":"Confidence-Gated Reasoning Methods","url":"https://www.emergentmind.com/topics/confidence-gated-reasoning"},{"title":"Forecasting When to Forecast: Accelerating Diffusion Models with Confidence-Gated Taylor - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705125016740"},{"title":"Confidence-Guided Test-Time Reasoning","url":"https://www.emergentmind.com/topics/confidence-guided-test-time-reasoning"},{"title":"[1111.1386] Confidence Estimation in Structured Prediction","url":"https://arxiv.org/abs/1111.1386"},{"title":"Sampling-free Uncertainty Estimation in Gated Recurrent Units with Applications to Normative Modeling in Neuroimaging - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7220220/"},{"title":"Learning Where to Sample in Structured Prediction","url":"https://cs.stanford.edu/~pliang/papers/sample-aistats2015.pdf"},{"title":"[2004.04361] Calibrating Structured Output Predictors for Natural Language Processing","url":"https://ar5iv.labs.arxiv.org/html/2004.04361"},{"title":"Confidence-Aware Scheduled Sampling for Neural ...","url":"https://aclanthology.org/2021.findings-acl.205.pdf"},{"title":"Introducing prediction intervals for sample means - PMC - NIH","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11334197/"}]

I found search results related to your query on confidence-gated sampling and structured prediction. Here's what I found:

## Overview

Confidence estimation encompasses a variety of algorithmic, statistical, and calibration strategies addressing the reliability of point predictions or structured outputs, spanning fields such as classification, structured prediction, sequence modeling, signal processing, localization, and practical safety-critical applications.

## Confidence-Gated Approaches

Confidence-guided test-time reasoning refers to the systematic use of model-internal confidence measures to shape, improve, and adapt a model's inference process when deployed on individual samples. Recent research has uncovered diverse paradigms for leveraging confidence at test time, ranging from dynamic control of reasoning depth, filtering or weighting of candidate outputs, to the modulation of computational resources according to sample difficulty and uncertainty.

## Application to Sampling

One specific implementation is a prediction confidence gating mechanism that dynamically decides when to trust Taylor-based approximations in diffusion models. This mechanism works by using the prediction error of the first block as a proxy to assess the confidence of the Taylor prediction at the current timestep. If the prediction error with respect to the ground truth is sufficiently small, the model state is considered sufficiently stable and Taylor approximation is applied for the remaining computation.

## Structured Prediction Context

Structured classification tasks such as sequence labeling and dependency parsing have seen much interest by the Natural Language Processing and the machine learning communities. Several online learning algorithms were adapted for structured tasks such as Perceptron, Passive-Aggressive and the recently introduced Confidence-Weighted learning.

The search results show that confidence-gated sampling is an emerging technique that combines confidence estimation with selective sampling strategies to improve efficiency and reliability in structured prediction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87e9306d-6c17-42a1-abeb-80b411a4a2fa",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "6c70176a-d6d6-46d0-bf20-9af5c1644429",
  "sourceToolAssistantUUID": "87e9306d-6c17-42a1-abeb-80b411a4a2fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T00:05:28.291Z_

<details><summary>↩ Tool result · `toolu_014BFgzw2SQUoZFQazuJnarc`</summary>

```text
Web search results for query: "XGrammar constrained decoding information extraction"

Links: [{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"XGrammar: Efficient, flexible and portable structured generation engine …","url":"https://jimmysong.io/ai/xgrammar/"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://pubmed.ncbi.nlm.nih.gov/39839970/"},{"title":"Flexible and Efficient Grammar-Constrained Decoding | OpenReview","url":"https://openreview.net/forum?id=L6CYAzpO1k"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"MLC | Achieving Efficient, Flexible, and Portable Structured Generation with XGrammar","url":"https://blog.mlc.ai/2024/11/22/achieving-efficient-flexible-portable-structured-generation-with-xgrammar"}]

Based on the search results, here's what I found about XGrammar, constrained decoding, and information extraction:

## XGrammar Overview

XGrammar is an open-source library for efficient, flexible, and portable structured generation that leverages constrained decoding to ensure 100% structural correctness of the output. XGrammar-2 was released in May 2026.

## Constrained Decoding for Information Extraction

In structured information extraction, there are typically semantic and syntactic constraints on the output of IE systems, but these constraints cannot typically be guaranteed using standard encoder-decoder architectures. This has led to the development of constrained decoding approaches which allow specifying constraints in form of context-free grammars.

Encoder-decoder models used for structure prediction for information extraction tasks in low-resource settings clearly benefit from grammar-constrained decoding guiding the output generation.

## How XGrammar Works

XGrammar is a flexible and efficient structure generation engine that accelerates context-free grammar execution by dividing the vocabulary into context-independent tokens that can be prechecked and context-dependent tokens that need to be interpreted during runtime.

## Performance and Adoption

XGrammar outperforms existing LLM engines up to 14x in JSON-schema generation and up to 80x in CFG-guided generation. XGrammar has been officially integrated into multiple major projects including vLLM, SGLang, MLC-LLM, TensorRT-LLM, Modular's MAX, OpenVINO GenAI, and Mirai.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dadf6db-4273-4709-9c5c-55942a123c24",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "2374c104-afea-42a5-85d3-411fb72c7600",
  "sourceToolAssistantUUID": "9dadf6db-4273-4709-9c5c-55942a123c24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T00:05:28.305Z_

<details><summary>↩ Tool result · `toolu_0198L5m6cWh4GtXazjsUpk6P`</summary>

```text
Web search results for query: "Qwen3-8B information extraction fine-tuning"

Links: [{"title":"Fine-Tuning Qwen3-VL 8B: A Step-by-Step Guide | DataCamp","url":"https://www.datacamp.com/tutorial/fine-tuning-qwen3-vl-8b"},{"title":"🚀 Fine-Tune Qwen3 8B with LoRA · Hugging Face","url":"https://huggingface.co/docs/optimum-neuron/training_tutorials/finetune_qwen3"},{"title":"unsloth/Qwen3-8B-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Qwen3-8B-GGUF"},{"title":"Qwen3 8B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-8b/"},{"title":"Qwen3 - How to Run & Fine-tune | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3-how-to-run-and-fine-tune"},{"title":"We Benchmarked 12 Small Language Models Across 8 Tasks to Find the Best Base Model for Fine-Tuning — distil labs","url":"https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/"},{"title":"Qwen3 Best Practices — swift 3.6.4 documentation","url":"https://swift.readthedocs.io/en/v3.6/BestPractices/Qwen3-Best-Practice.html"},{"title":"Fine-Tuning Qwen3-8B for Medical Reasoning on E2E Networks A100 GPU | E2E Networks","url":"https://www.e2enetworks.com/blog/fine-tuning-qwen3-8b-medical-reasoning-qlora-e2e-networks-a100"},{"title":"How to Fine-Tune Qwen3.5 0.8B Locally?","url":"https://sonusahani.com/blogs/fine-tune-qwen3-5-8b-locally"},{"title":"🚀[Fine-tuning] Qwen3-MoE Megatron Training Implementation and Best Practices👋 · QwenLM/Qwen3 · Discussion #1301","url":"https://github.com/QwenLM/Qwen3/discussions/1301"}]

Based on the search results, here's what I found about Qwen3-8B and information extraction fine-tuning:

## Model Overview

Qwen3-8B is a dense large language model (LLM) in the Qwen3 series, developed by the Qwen team at Alibaba Cloud, released in 2024 under the Apache 2.0 license. It's a dense transformer-based model with 8.2 billion parameters spanning 36 layers.

## Information Extraction Performance

Qwen3-8B has been fine-tuned across 8 diverse tasks including information extraction, along with classification, open-book QA, and closed-book QA. The Qwen3 family dominates in fine-tuned performance, with Qwen3-8B ranking at #2 for best fine-tuned performance across these tasks.

Additionally, in some retrieval-focused tasks, thinking-mode content can marginally impair extraction accuracy compared to non-thinking mode outputs.

## Fine-Tuning Approaches

Multiple fine-tuning methods are available for Qwen3-8B:

1. **LoRA (Low-Rank Adaptation)**: Unsloth supports fine-tuning of Qwen3 models at 2x faster speed, with 70% less VRAM, and 8x longer context lengths.

2. **Supervised Fine-Tuning (SFT)**: Self-awareness fine-tuning on Qwen3-8B can be performed within 30 minutes with a GPU having at least 22GB of VRAM.

3. **Domain-Specific Fine-Tuning**: Supervised fine-tuning (SFT) can be applied on domain-specific reasoning datasets designed for enhancement.

## Key Considerations

Because Qwen3 supports both reasoning and non-reasoning modes, you can fine-tune it with a non-reasoning dataset, but this may affect its reasoning ability. To maintain reasoning capabilities, a mix of 75% reasoning and 25% non-reasoning examples in your dataset is recommended.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8b70a6f-388b-403d-81cd-f52fa8a2ecd0",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "2d19ea4a-bdea-40a6-a016-c683aad94dea",
  "sourceToolAssistantUUID": "a8b70a6f-388b-403d-81cd-f52fa8a2ecd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T00:05:28.367Z_

<details><summary>↩ Tool result · `toolu_01P9m22X2Z3EKYHN6CP7J9rM`</summary>

```text
Web search results for query: "arXiv best-of-N structured prediction 2025 2026"

Links: [{"title":"Publications - People @EECS","url":"https://people.eecs.berkeley.edu/~jordan/publications.html"},{"title":"GitHub - ChaofanTao/Autoregressive-Models-in-Vision-Survey: [TMLR 2025🔥] A survey for the autoregressive models in vision.","url":"https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey"},{"title":"[2510.23077] Think before Recommendation: Autonomous Reasoning-enhanced Recommender","url":"https://arxiv.org/abs/2510.23077"},{"title":"Machine Learning Apr 2026","url":"https://arxiv.org/list/cs.LG/current"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/new"},{"title":"Trending Papers - Hugging Face","url":"https://huggingface.co/papers/trending"},{"title":"Published as a conference paper at ICLR 2025 VALID CONFORMAL PREDICTION FOR","url":"https://arxiv.org/pdf/2405.19230"},{"title":"Position: The Future of Bayesian Prediction Is Prior-Fitted","url":"https://arxiv.org/html/2505.23947v1"},{"title":"[2503.13522] Advanced Deep Learning Methods for Protein Structure Prediction and Design","url":"https://arxiv.org/abs/2503.13522"},{"title":"[2110.02057] Structured Prediction in NLP -- A survey","url":"https://arxiv.org/abs/2110.02057"}]

Based on the search results, I found some relevant papers from arXiv in the 2025-2026 timeframe, though the results don't specifically focus on "best-of-N structured prediction." Here's what I found:

**Recent arXiv papers related to structured prediction and related topics (2025-2026):**

1. **Structured Reasoning and Prediction**: RecZero is a reinforcement learning-based recommendation paradigm that trains a single LLM through pure RL to autonomously develop reasoning capabilities for rating prediction, submitted in October 2025.

2. **Autoregressive Learning**: Research has developed an online framework focusing on the mistake bound of learning the final output induced by an unknown next-token generator, distinguishing between an End-to-End model where learners observe only the final token produced after M autoregressive steps, and a Chain-of-Thought model where learners are additionally shown the entire M-step trajectory.

3. **Conformal Prediction Methods**: Several papers on conformal prediction frameworks were published in 2025, including work on multivariate conformal prediction and prediction set construction.

The search results include many relevant papers from 2025-2026, but don't contain a specific, prominent paper focused on "best-of-N structured prediction." If you're looking for a particular paper on this topic, you might want to search arXiv directly with more specific keywords or check recent conference proceedings (ICLR, NeurIPS, etc.) from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b0293c9-3925-42f9-8387-4911fe755f40",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "0e03b7df-1a84-49a4-8f33-66bafabe9399",
  "sourceToolAssistantUUID": "9b0293c9-3925-42f9-8387-4911fe755f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-12T00:05:28.518Z_

<details><summary>↩ Tool result · `toolu_01Rd15vyfRho4FrP1iCMzDWV`</summary>

```text
Web search results for query: "ensemble NER LLM 2025 2026"

Links: [{"title":"What Is Named Entity Recognition (NER)? Complete Guide 2026","url":"https://www.articsledge.com/post/named-entity-recognition-ner"},{"title":"Building an Ensemble LLM Semantic Tagger for UN Security Council Resolutions","url":"https://arxiv.org/html/2603.05895v1"},{"title":"Ensemble Large Language Models: A Survey","url":"https://www.mdpi.com/2078-2489/16/8/688"},{"title":"A Multi-LLM Approach for Supply Chain Risk Assessment | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-19343-8_4"},{"title":"GPT-NER: Named Entity Recognition via Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.239/"},{"title":"Frontiers | Intent-driven LLM ensemble planning for flexible multi-robot manipulation","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1727433/full"},{"title":"Full LLM Leaderboard 2026 — Advanced Explorer for 300+ AI Models","url":"https://llm-stats.com/leaderboards/llm-leaderboard"},{"title":"A novel large-language-model-driven framework for named entity recognition - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457324004138"},{"title":"Tech Trends 2026 update: Thinking outside the LLM box","url":"https://nextfutures.substack.com/p/tech-trends-2026-update-thinking"},{"title":"GitHub - junchenzhi/Awesome-LLM-Ensemble: A curated list of Awesome-LLM-Ensemble papers for the survey \"Harnessing Multiple Large Language Models: A Survey on LLM Ensemble\" · GitHub","url":"https://github.com/junchenzhi/Awesome-LLM-Ensemble"}]

Based on the search results, here's what I found about ensemble NER LLM approaches in 2025-2026:

## Recent Developments in Ensemble NER with LLMs

**LLM-Based NER Advances:**
As of January 2025, GPT-NER demonstrates that LLM-based approaches achieve comparable performance to supervised baselines while excelling in low-resource scenarios. GPT-NER addresses hallucination issues through a self-verification strategy and exhibits greater ability in low-resource and few-shot setups where training data is extremely scarce.

**Ensemble Approaches for NER:**
An ensemble of pretrained LLMs has been employed to extract biomedical entities and relations, emphasizing the robustness of combining multiple models to achieve superior performance in named entity recognition and relation extraction tasks.

A recent methodology introduces LLM-based systems for semantic tagging of documents, leveraging LLM performance variability to build ensemble systems for data cleaning and semantic tagging tasks. GPT-4.1 achieved high metrics for both cleaning and semantic tagging tasks, while smaller models like GPT-4.1-mini achieved comparable performance at only 20% of the cost.

**Future Trends:**
By 2025-2026, further breakthroughs are anticipated in handling low-resource languages, domain adaptation, and multimodal scenarios.

**Specialized Ensemble Applications:**
Recent research includes EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models, which represents a specialized approach combining ensemble methods with NER tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf929f23-11c7-4278-84aa-43398231b150",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "6549456a-8d3d-4308-939c-98931375da6e",
  "sourceToolAssistantUUID": "bf929f23-11c7-4278-84aa-43398231b150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T00:05:28.741Z_

<details><summary>↩ Tool result · `toolu_014AGHMDMko9G4YKutYqPkF8`</summary>

```text
Web search results for query: "ACL 2025 NAACL 2025 EMNLP 2025 accepted papers test-time scaling self-consistency structured prediction"

Links: [{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"2025 Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics - NAACL-HLT 2025","url":"https://2025.naacl.org/"},{"title":"Paper Digest: NAACL 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/05/naacl-2025-papers-highlights/"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"},{"title":"Paper Digest: ACL 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/07/acl-2025-papers-highlights/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"King's College London NLP","url":"https://kclnlp.github.io/publications.html"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"}]

Based on the search results, I found information about accepted papers at the major 2025 NLP conferences (ACL, NAACL, and EMNLP), though the results don't show papers specifically focused on all the topics you mentioned together.

Here's what I found:

## Conference Accepted Papers

NAACL-2025 accepted more than 700 papers, and EMNLP-2025 accepts more than 2,000 papers.

## Relevant Papers Found

One paper that appears relevant to your interests is "Too Consistent to Detect: A Study of Self-Consistent Errors in LLMs", which was accepted at EMNLP 2025 and directly addresses self-consistency in language models.

Additionally, there are papers related to reasoning and consistency:
- DCMKC (Dual Consistency Matching for KG and CoT) method, aiming to maintain semantic and structural consistency between KG and CoT
- Papers on chain-of-thought reasoning and structured prediction approaches

## Access to Papers

To find more specific papers on test-time scaling, self-consistency, and structured prediction, you can:
- The proceedings of NAACL 2025 are now available on the ACL Anthology
- Search for papers presented at NAACL-2025 on a specific topic using the search by venue service

The official conference proceedings pages (2025.naacl.org, 2025.emnlp.org, and ACL Anthology) would be the best resources for comprehensive access to all accepted papers organized by topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fa461c6-745d-4aef-951d-228799d96df1",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "d80291db-c62e-4de9-a938-5f46d204b3c4",
  "sourceToolAssistantUUID": "2fa461c6-745d-4aef-951d-228799d96df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-12T00:05:30.827Z_

Let me run a few more targeted searches to fill in gaps, especially around the most relevant competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d80291db-c62e-4de9-a938-5f46d204b3c4",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhSLhVxw2iHQp4yUMQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b173583-9c45-4002-8402-791615d5aff1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY4Fns65Wb8VPDNFuig9VG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 8898,
      "cache_read_input_tokens": 9639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8898,
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

_source line 28 · 2026-05-12T00:05:31.839Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WQBXaRnipCphu6V6VmDy5X`</summary>

```json
{
  "query": "STED semantic tree edit distance JSON consistency scoring structured generation LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b173583-9c45-4002-8402-791615d5aff1",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhSLhVxw2iHQp4yUMQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "902c7aff-3af8-45f4-9ca3-836e6e0bd181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY4Fns65Wb8VPDNFuig9VG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 8898,
      "cache_read_input_tokens": 9639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8898,
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

_source line 29 · 2026-05-12T00:05:32.835Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MVycwPgENmi7iw9pg13UAQ`</summary>

```json
{
  "query": "\"grammar-constrained decoding\" \"fine-tuned\" \"information extraction\" structured output clinical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "902c7aff-3af8-45f4-9ca3-836e6e0bd181",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhSLhVxw2iHQp4yUMQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3efe8798-42ff-436e-8c8a-e7188673218d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY4Fns65Wb8VPDNFuig9VG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 8898,
      "cache_read_input_tokens": 9639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8898,
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

_source line 30 · 2026-05-12T00:05:33.775Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QhwpgJwcnRPUXk3YAuvsZV`</summary>

```json
{
  "query": "PARSE LLM schema optimization entity extraction EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3efe8798-42ff-436e-8c8a-e7188673218d",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhSLhVxw2iHQp4yUMQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2798b9cb-1d4f-4401-9410-8d3d8c40ff10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY4Fns65Wb8VPDNFuig9VG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 8898,
      "cache_read_input_tokens": 9639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8898,
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

_source line 31 · 2026-05-12T00:05:34.264Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GPmFXXrnRzPCixCrepfSJz`</summary>

```json
{
  "query": "adaptive compute allocation difficulty LLM self-consistency early stopping 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2798b9cb-1d4f-4401-9410-8d3d8c40ff10",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhSLhVxw2iHQp4yUMQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b5d09fa-f5c9-46fd-b001-76d26cd872fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY4Fns65Wb8VPDNFuig9VG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 8898,
      "cache_read_input_tokens": 9639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8898,
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

_source line 32 · 2026-05-12T00:05:34.881Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Rfy3LGevrmFq3GxZKWRoT`</summary>

```json
{
  "query": "EL4NER ensemble small LLM named entity recognition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b5d09fa-f5c9-46fd-b001-76d26cd872fa",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhSLhVxw2iHQp4yUMQk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2435dae-148e-47bf-8a0b-c398f1571634",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY4Fns65Wb8VPDNFuig9VG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 8898,
      "cache_read_input_tokens": 9639,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8898
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 804,
          "output_tokens": 290,
          "cache_read_input_tokens": 9639,
          "cache_creation_input_tokens": 8898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8898,
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

_source line 33 · 2026-05-12T00:05:38.815Z_

<details><summary>↩ Tool result · `toolu_01MVycwPgENmi7iw9pg13UAQ`</summary>

```text
Web search results for query: ""grammar-constrained decoding" "fine-tuned" "information extraction" structured output clinical"

Links: [{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://pubmed.ncbi.nlm.nih.gov/39839970/"},{"title":"GitHub - ag-sc/Clinical-Trial-IE-GCD: Artifact \"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts\"","url":"https://github.com/ag-sc/clinical-trial-ie-gcd"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"},{"title":"(PDF) Flexible Grammar-Based Constrained Decoding for Language Models","url":"https://www.researchgate.net/publication/370981005_Flexible_Grammar-Based_Constrained_Decoding_for_Language_Models"},{"title":"https://www.frontiersin.org/journals/artificial-intelligence/articles/ ...","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/xml"},{"title":"A Guide to Structured Generation Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | OpenReview","url":"https://openreview.net/forum?id=KkHY1WGDII"},{"title":"[2305.13971] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/abs/2305.13971"}]

Based on the web search results, I found highly relevant research on this topic. Here's what the search revealed:

## Grammar-Constrained Decoding for Clinical Information Extraction

The research experimentally investigates the influence of grammar-constrained decoding and pointer generators on the performance of a domain-specific information extraction system, considering fine-tuned encoder-decoder models such as Longformer and Flan-T5.

The work focuses on inducing structured representations from abstracts describing clinical trials using the C-TrO ontology, framing the task as a slot filling problem where certain slots of templates need to be filled with token sequences occurring in the input text.

### Key Findings

The research shows the positive impact of grammar-constrained decoding on generative LLMs fine-tuned for structured information extraction in a low-resource setting, improving F1 scores from 0.062 to 0.413 and from 0.102 to 0.47 for type 2 diabetes and glaucoma datasets, respectively.

However, adding pointer generators on top of grammar-constrained decoding has a negative impact on the performance, decreasing F1 scores from 0.413 to 0.263 and from 0.47 to 0.292 for type 2 diabetes and glaucoma datasets.

The research specifically focuses on the extraction of PICO-related information from abstracts describing randomized clinical trials, where PICO refers to Patient, Intervention, Comparison and Outcomes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3efe8798-42ff-436e-8c8a-e7188673218d",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "be4d821a-1b8f-4af2-aa7a-449423802ebf",
  "sourceToolAssistantUUID": "3efe8798-42ff-436e-8c8a-e7188673218d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T00:05:39.616Z_

<details><summary>↩ Tool result · `toolu_01WQBXaRnipCphu6V6VmDy5X`</summary>

```text
Web search results for query: "STED semantic tree edit distance JSON consistency scoring structured generation LLM"

Links: [{"title":"[2512.23712] STED and Consistency Scoring: A Framework for Evaluating LLM Structured Output Reliability","url":"https://arxiv.org/abs/2512.23712"},{"title":"STED and Consistency Scoring: A Framework for Evaluating LLM Structured Output Reliability","url":"https://arxiv.org/html/2512.23712v1"},{"title":"STED and Consistency Scoring: A Framework for","url":"https://assets.amazon.science/a5/17/27fbb95042c898b20d31a0bc7fdb/scipub-approval152134-40675598-sted-and-consistency-scoring-a-framework-for-evaluating-llm-structured-output-reliability.pdf"},{"title":"STED and Consistency Scoring: A Framework for Evaluating LLM Structured Output Reliability | OpenReview","url":"https://openreview.net/forum?id=rSCV1hTZvF"},{"title":"GitHub - amazon-science/sted · GitHub","url":"https://github.com/amazon-science/sted"},{"title":"Large language model driven transferable key information extraction mechanism for nonstandardized tables | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-15627-z"},{"title":"LLM reliability assessment with STED and consistency scoring","url":"https://neuraking.com/en/45946/evaluation-de-la-fiabilite-des-sorties-structurees-des-modeles-de-langage-grace-au-cadre-sted/"},{"title":"Generalized Tree Edit Distance (GTED): A Faithful Evaluation Metric for Statement Autoformalization","url":"https://arxiv.org/html/2507.07399v1"},{"title":"Large language model driven transferable key information ...","url":"https://www.nature.com/articles/s41598-025-15627-z.pdf"},{"title":"Revisiting Code Similarity Evaluation with Abstract Syntax ...","url":"https://aclanthology.org/2024.acl-short.3.pdf"}]

Based on the search results, here's what I found about STED (Semantic Tree Edit Distance) and consistency scoring for structured generation with LLMs:

## Overview

STED and consistency scoring is a framework for evaluating and improving consistency in LLM-generated structured outputs.

## Key Components

The approach combines: (1) STED (Semantic Tree Edit Distance), a novel similarity metric balancing semantic flexibility with structural strictness when comparing JSON outputs, and (2) a consistency scoring framework aggregating multiple STED measurements across repeated generations to quantify reliability.

## Performance

STED achieves superior performance (0.86-0.90 similarity for semantic equivalents, 0.0 for structural breaks) compared to existing metrics including TED, BERTScore, and DeepDiff.

## Technical Approach

STED directly incorporates JSON semantics through three key innovations: (1) Semantic-Enhanced Tree Edit Distance that recognizes semantically equivalent keys and values while preserving structural constraints, (2) Order-Invariant Matching using Hungarian algorithm for optimal element pairing, and (3) Multi-Level Similarity integrating structural, key, value, and type similarities.

## Real-World Application

Applying the framework to benchmark six LLMs reveals significant variations: Claude-3.7-Sonnet demonstrates exceptional consistency, maintaining near-perfect structural reliability even at high temperatures (T=0.9), while models like Claude-3-Haiku and Nova-Pro exhibit substantial degradation requiring careful tuning.

The framework was accepted at NeurIPS 2025 Workshop on Structured Probabilistic Inference and Generative Modeling, and an open-source implementation is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "902c7aff-3af8-45f4-9ca3-836e6e0bd181",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "5f17724e-a9cf-40b6-8e28-1d21e76dea2a",
  "sourceToolAssistantUUID": "902c7aff-3af8-45f4-9ca3-836e6e0bd181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-12T00:05:41.190Z_

<details><summary>↩ Tool result · `toolu_01QhwpgJwcnRPUXk3YAuvsZV`</summary>

```text
Web search results for query: "PARSE LLM schema optimization entity extraction EMNLP 2025"

Links: [{"title":"[2510.08623] PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/abs/2510.08623"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"PARSE: LLM driven schema optimization for reliable entity extraction - Amazon Science","url":"https://www.amazon.science/publications/parse-llm-driven-schema-optimization-for-reliable-entity-extraction"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable ...","url":"https://aclanthology.org/2025.emnlp-industry.184.pdf"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=13775&show=25"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=3600&show=250"},{"title":"(PDF) PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://www.researchgate.net/publication/396458126_PARSE_LLM_Driven_Schema_Optimization_for_Reliable_Entity_Extraction"},{"title":"Accepted Industry Track Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/ind_papers/"},{"title":"Parse: LLM Driven Schema Optimization for Reliable Entity Extraction | Hacker News","url":"https://news.ycombinator.com/item?id=45683970"}]

Based on the search results, here's what I found about PARSE:

## PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction

PARSE has been accepted to EMNLP 2025 as an industry track paper.

### Overview

PARSE (Parameter Automated Refinement and Schema Extraction) is a novel system with two synergistic components: ARCHITECT, which autonomously optimizes JSON schemas for LLM consumption while maintaining backward compatibility through RELAY (an integrated code generation system), and SCOPE, which implements reflection-based extraction with combined static and LLM-based guardrails.

### Problem It Addresses

Structured information extraction from unstructured text is critical for emerging Software 3.0 systems where LLM agents autonomously interact with APIs and tools. Recent approaches apply large language models directly to extraction tasks using existing JSON schemas, often with constraint decoding or reinforcement learning approaches to ensure syntactic validity, but treat JSON schemas as static contracts designed for human developers, leading to suboptimal extraction performance, frequent hallucinations, and unreliable agent behavior when schemas contain ambiguous or incomplete specifications.

### Results

PARSE achieves up to 64.7% improvement in extraction accuracy on SWDE with combined framework improvements reaching 10% across models, while reducing extraction errors by 92% within the first retry and maintaining practical latency.

The paper was authored by Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, and Promod Yenigalla.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2798b9cb-1d4f-4401-9410-8d3d8c40ff10",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "f6c95cce-a817-448c-a098-de93c44895e8",
  "sourceToolAssistantUUID": "2798b9cb-1d4f-4401-9410-8d3d8c40ff10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-12T00:05:41.770Z_

<details><summary>↩ Tool result · `toolu_013Rfy3LGevrmFq3GxZKWRoT`</summary>

```text
Web search results for query: "EL4NER ensemble small LLM named entity recognition"

Links: [{"title":"[2505.23038] EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/abs/2505.23038"},{"title":"EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models","url":"https://arxiv.org/html/2505.23038v1"},{"title":"EL4NER: Ensemble Learning for Named Entity ...","url":"https://arxiv.org/pdf/2505.23038"},{"title":"llmNER: (Zero|Few)-Shot Named Entity Recognition, Exploiting the Power of Large Language Models","url":"https://arxiv.org/html/2406.04528v1"},{"title":"GitHub - chinhang0104/Ensemble-Learning-for-Named-Entity-Recognition: Utilize multiple Named Entity Recogniztion packages to detect human name and organization and # determine the final output by conducting a voting process among the NER packages.","url":"https://github.com/chinhang0104/Ensemble-Learning-for-Named-Entity-Recognition"},{"title":"MedAI #127: Improving LLMs for Clinical Named Entity ...","url":"https://www.youtube.com/watch?v=tk4ykvAvV7w"},{"title":"Local LLM Ensembles for Zero-shot Portuguese Named Entity Recognition","url":"https://arxiv.org/html/2512.10043v1"},{"title":"[2304.10428] GPT-NER: Named Entity Recognition via Large Language Models","url":"https://arxiv.org/abs/2304.10428"},{"title":"Ensemble Learning for Named Entity Recognition","url":"https://svn.aksw.org/papers/2014/ISWC_EL4NER/public.pdf"},{"title":"Day 37: Named Entity Recognition (NER) with LLMs - DEV Community","url":"https://dev.to/nareshnishad/day-37-named-entity-recognition-ner-with-llms-2g5p"}]

Based on the search results, here's what I found about EL4NER:

## EL4NER Overview

EL4NER is an Ensemble Learning Method for Named Entity Recognition that aims at aggregating the in-context learning (ICL) outputs of multiple open-source, small-parameter LLMs to enhance overall performance in NER tasks at less deployment and inference cost.

## Key Problem It Addresses

Most ICL-based NER methods depend on large-parameter LLMs: the open-source models demand substantial computational resources for deployment and inference, while the closed-source ones incur high API costs, raise data-privacy concerns, and hinder community collaboration.

## Core Components

The method comprises three key technical innovations:

1. **Task Decomposition**: EL4NER decomposes the NER task into two stages, the first of which uses multiple LLMs to extract potential entity spans and integrate them, and the second of which confirms entity types one by one by voting on multiple LLMs, thus enabling two integrations at a fine-grained level.

2. **Demonstration Retrieval**: A novel span-level sentence similarity algorithm is introduced to establish an ICL demonstration retrieval mechanism better suited for NER tasks.

3. **Noise Mitigation**: A self-validation mechanism is incorporated to mitigate the noise introduced during the ensemble process.

## Performance Results

EL4NER surpasses most closed-source, large-parameter LLM-based methods at a lower parameter cost and even attains state-of-the-art (SOTA) performance among ICL-based methods on certain datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2435dae-148e-47bf-8a0b-c398f1571634",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "296dbbb7-bb0b-45c8-9027-8a61393ecbc7",
  "sourceToolAssistantUUID": "f2435dae-148e-47bf-8a0b-c398f1571634",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-12T00:05:42.495Z_

<details><summary>↩ Tool result · `toolu_01GPmFXXrnRzPCixCrepfSJz`</summary>

```text
Web search results for query: "adaptive compute allocation difficulty LLM self-consistency early stopping 2025"

Links: [{"title":"GitHub - Eclipsess/Awesome-Efficient-Reasoning-LLMs: [TMLR 2025] Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models · GitHub","url":"https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs"},{"title":"Adaptive Thinking: Large Language Models Know When to Think in Latent Space | OpenReview","url":"https://openreview.net/forum?id=2i6Rp0gCq6"},{"title":"Difficulty-Adaptive Self-Consistency for Cost-Efficient ...","url":"https://aclanthology.org/2025.findings-naacl.383.pdf"},{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization","url":"https://arxiv.org/html/2604.14853"},{"title":"GitHub - fscdc/Awesome-Efficient-Reasoning-Models: [TMLR 2025] Efficient Reasoning Models: A Survey · GitHub","url":"https://github.com/fscdc/Awesome-Efficient-Reasoning-Models"},{"title":"Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better,","url":"https://arxiv.org/pdf/2410.02725"},{"title":"A Survey of Adaptive and Controllable Test-Time Compute ...","url":"https://arxiv.org/pdf/2507.02076"},{"title":"Deep Think with Confidence DEEP THINK WITH CONFIDENCE","url":"https://jiaweizzhao.github.io/deepconf/static/pdfs/deepconf_arxiv.pdf"},{"title":"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints | OpenReview","url":"https://openreview.net/forum?id=JMDCMf7mlF"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://arxiv.org/pdf/2505.11274"}]

Based on the search results, I found several highly relevant papers and resources from 2025 on adaptive compute allocation, difficulty-aware strategies, self-consistency, and early stopping for large language models:

## Key Research Areas Found:

**Difficulty-Adaptive Self-Consistency:**
Make every penny count: Difficulty-adaptive self-consistency for cost-efficient reasoning is a specific paper addressing this topic. DSC first ranks problem difficulty using LLM itself, then partitions problems into easy and hard to save sampling cost for easy ones, and finally pre-allocates sample sizes to reduce resampling costs for hard problems.

**Self-Consistency and Adaptive Allocation:**
Self-consistency, the agreement among multiple reasoning paths, is used as a proxy for thinking necessity. Lower self-consistency indicates when queries require extended thinking to reach correct answers. This insight leads to Sonata (Self-Consistency-Guided Adapter for Thinking Allocation), a lightweight approach that adaptively allocates thinking budgets to optimize the performance-efficiency tradeoff.

**Early Stopping Approaches:**
Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning is another relevant work. Additionally, Early Stopping Self-Consistency has been proposed, which terminate the sampling process early if a subset of responses shows strong consistency.

**Comprehensive Survey:**
A survey titled "Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models" was released on March 20, 2025, presenting the first structured survey that systematically investigates and organizes the current progress in achieving efficient reasoning in LLMs.

These resources provide a comprehensive view of the latest research in 2025 on adaptive compute allocation, difficulty-aware methods, and efficiency improvements for LLM reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b5d09fa-f5c9-46fd-b001-76d26cd872fa",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "884477af-0fcf-450f-a474-8d44732f333d",
  "sourceToolAssistantUUID": "3b5d09fa-f5c9-46fd-b001-76d26cd872fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-12T00:05:44.574Z_

Let me do a few more targeted searches to find the most directly competing/overlapping work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "884477af-0fcf-450f-a474-8d44732f333d",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhTMW9HBRUDmjr2LUPb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b42fab16-5e32-4260-9e35-f5fe5aa209e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVdYYqvxaFqGBuHx6wDwP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 4858,
      "cache_read_input_tokens": 18537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4858,
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

_source line 39 · 2026-05-12T00:05:45.727Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RkYqpqSJboMGXJTKBhQnRD`</summary>

```json
{
  "query": "Difficulty-Adaptive Self-Consistency DSC cost-efficient reasoning NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b42fab16-5e32-4260-9e35-f5fe5aa209e0",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhTMW9HBRUDmjr2LUPb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f7b6435-e0c4-4d68-ad64-5b82cd2669f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVdYYqvxaFqGBuHx6wDwP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 4858,
      "cache_read_input_tokens": 18537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4858,
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

_source line 40 · 2026-05-12T00:05:47.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AFetLnZk8YaXu3aqudbToU`</summary>

```json
{
  "query": "\"self-consistency\" \"structured output\" \"named entity\" OR \"relation extraction\" OR \"information extraction\" voting aggregation arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f7b6435-e0c4-4d68-ad64-5b82cd2669f0",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhTMW9HBRUDmjr2LUPb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca5aa82c-3653-4280-bb4f-39fa4446fd1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVdYYqvxaFqGBuHx6wDwP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 4858,
      "cache_read_input_tokens": 18537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4858,
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

_source line 41 · 2026-05-12T00:05:47.517Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VPQ8oWxi1zszixR7atX8vT`</summary>

```json
{
  "query": "Sonata self-consistency guided thinking allocation adaptive test-time compute 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca5aa82c-3653-4280-bb4f-39fa4446fd1c",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhTMW9HBRUDmjr2LUPb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83c5f8e6-284d-4da1-bacc-68869d1af052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVdYYqvxaFqGBuHx6wDwP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 4858,
      "cache_read_input_tokens": 18537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4858,
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

_source line 42 · 2026-05-12T00:05:48.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HrwXtcxntcYQ7hFneX4WaJ`</summary>

```json
{
  "query": "TASER table agents schema extraction recommendation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83c5f8e6-284d-4da1-bacc-68869d1af052",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhTMW9HBRUDmjr2LUPb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a4c0813-bf95-4e31-8f5e-9d24560d12c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVdYYqvxaFqGBuHx6wDwP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 4858,
      "cache_read_input_tokens": 18537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4858,
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

_source line 43 · 2026-05-12T00:05:48.940Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YTdx8TGaETH2JFAN1QSZhi`</summary>

```json
{
  "query": "\"majority voting\" \"information extraction\" LLM multiple samples structured 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a4c0813-bf95-4e31-8f5e-9d24560d12c3",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhTMW9HBRUDmjr2LUPb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39195b85-a469-4dfc-bf15-79c648b5abe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVdYYqvxaFqGBuHx6wDwP3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 4858,
      "cache_read_input_tokens": 18537,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 923,
          "output_tokens": 303,
          "cache_read_input_tokens": 18537,
          "cache_creation_input_tokens": 4858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4858,
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

_source line 44 · 2026-05-12T00:05:51.503Z_

<details><summary>↩ Tool result · `toolu_01RkYqpqSJboMGXJTKBhQnRD`</summary>

```text
Web search results for query: "Difficulty-Adaptive Self-Consistency DSC cost-efficient reasoning NAACL 2025"

Links: [{"title":"Difficulty-Adaptive Self-Consistency for Cost-Efficient ...","url":"https://aclanthology.org/2025.findings-naacl.383.pdf"},{"title":"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.383/"},{"title":"[2408.13457] Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning","url":"https://arxiv.org/abs/2408.13457"},{"title":"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning","url":"https://arxiv.org/html/2408.13457v1"},{"title":"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning [Quick Review]","url":"https://liner.com/review/make-every-penny-count-difficultyadaptive-selfconsistency-for-costefficient-reasoning"},{"title":"Leveraging Reasoning Paths for Efficient LLM Sampling","url":"https://aclanthology.org/2025.naacl-long.184.pdf"},{"title":"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning | alphaXiv","url":"https://www.alphaxiv.org/abs/2408.13457"},{"title":"Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://aclanthology.org/2025.emnlp-main.1750.pdf"},{"title":"[Literature Review] Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning","url":"https://www.themoonlight.io/en/review/make-every-penny-count-difficulty-adaptive-self-consistency-for-cost-efficient-reasoning"},{"title":"[PDF] Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Make-Every-Penny-Count:-Difficulty-Adaptive-for-Wang-Feng/19e00674c3b767f5388a7a9e080b2b97485099a4"}]

I found information about the paper "Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning" published at NAACL 2025. Here's what I found:

## Overview

The paper "Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning" was published in the Findings of the Association for Computational Linguistics: NAACL 2025 in Albuquerque, New Mexico.

## Main Contribution

The paper proposes Difficulty-Adaptive Self-Consistency (DSC), which leverages the difficulty information of batch queries from both prior and posterior perspectives to adaptively allocate inference resources, further reducing the overall cost of self-consistency (SC).

## Methodology

DSC first ranks problem difficulty using LLM itself (step 1), then partitions problems into easy and hard to save sampling cost for easy ones (step 2), and finally pre-allocates sample sizes to reduce resampling costs for hard problems (step 3).

## Results

The paper conducts extensive experiments on three popular categories of reasoning tasks: arithmetic, commonsense and symbolic reasoning on six benchmarks. The empirical results show that DSC consistently surpasses the strong baseline ASC and ESC in terms of costs by a significant margin, while attaining comparable performances.

DSC achieved an average cost reduction of 65.29% on GPT-4 and 56.04% on GPT-3.5-Turbo compared to SC, and 24.81% on GPT-4 and 21.86% on GPT-3.5-Turbo compared to the strongest baseline, ESC.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f7b6435-e0c4-4d68-ad64-5b82cd2669f0",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "0e7b36e9-2155-41db-9322-13e4bead26ec",
  "sourceToolAssistantUUID": "1f7b6435-e0c4-4d68-ad64-5b82cd2669f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-12T00:05:53.523Z_

<details><summary>↩ Tool result · `toolu_01AFetLnZk8YaXu3aqudbToU`</summary>

```text
Web search results for query: ""self-consistency" "structured output" "named entity" OR "relation extraction" OR "information extraction" voting aggregation arXiv"

Links: [{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"[2010.12812] A Frustratingly Easy Approach for Entity and Relation Extraction","url":"https://arxiv.org/abs/2010.12812"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Structured Entity Extraction Using Large Language Models","url":"https://arxiv.org/html/2402.04437v3"},{"title":"A Few-Shot Learning Focused Survey on Recent Named Entity Recognition and","url":"https://arxiv.org/pdf/2310.19055"},{"title":"A survey on Relation Extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2667305323000698"},{"title":"Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study","url":"https://arxiv.org/html/2401.10825v3"},{"title":"A survey on recent advances in Named Entity Recognition","url":"https://arxiv.org/html/2401.10825v1"},{"title":"Semi-supervised Relation Extraction via Data Augmentation and Consistency-training","url":"https://arxiv.org/html/2306.10153v1"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"}]

I found several relevant results for your search query. Here's a summary of what came up:

## Key Papers and Research

Large Language Models are used for generative information extraction, where they make predictions on unlabeled corpus and generate self-annotated datasets through self-consistency. The research spans multiple information extraction tasks including Named Entity Recognition (NER), Relation Extraction (RE), and Event Extraction (EE).

The focus in recent information extraction work is primarily on Named Entity Recognition (NER), Relation Extraction (RE), and Event Extraction (EE), with strategies to select reliable annotations and retrieve demonstrations from reliable self-annotated datasets for in-context learning.

Several approaches combine these elements:

- **Structured Output and Consistency**: Multi-instance learning approaches aggregate information from multiple mentions of the same entity to improve performance

- **Data Augmentation and Consistency Training**: Data augmentations applied to unlabelled data enable consistency training techniques for semi-supervised relation extraction

- **Self-Improvement Methods**: There have been efforts to employ LLMs for iterative self-verification and self-improvement, aiming to rectify results

The search results show these techniques being applied across multiple extraction tasks and emphasize the importance of proper aggregation and voting mechanisms for improving structured information extraction from language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca5aa82c-3653-4280-bb4f-39fa4446fd1c",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "82772fff-6b2d-4ad6-becf-f2a1bf363a45",
  "sourceToolAssistantUUID": "ca5aa82c-3653-4280-bb4f-39fa4446fd1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-12T00:05:54.937Z_

<details><summary>↩ Tool result · `toolu_01VPQ8oWxi1zszixR7atX8vT`</summary>

```text
Web search results for query: "Sonata self-consistency guided thinking allocation adaptive test-time compute 2025"

Links: [{"title":"Adaptive Thinking: Large Language Models Know When to Think in Latent Space | OpenReview","url":"https://openreview.net/forum?id=2i6Rp0gCq6"},{"title":"ADAPTIVE THINKING: LARGE LANGUAGE MODELS ...","url":"https://openreview.net/pdf?id=2i6Rp0gCq6"},{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization","url":"https://arxiv.org/html/2604.14853v1"},{"title":"A Survey of Adaptive and Controllable Test-Time Compute ...","url":"https://arxiv.org/pdf/2507.02076"},{"title":"GitHub - facebookresearch/sonata: [CVPR'25 Highlight] Official repository of Sonata: Self-Supervised Learning of Reliable Point Representations · GitHub","url":"https://github.com/facebookresearch/sonata"},{"title":"DiSCTT: Consensus-Guided Self-Curriculum for Efficient Test-Time Adaptation in Reasoning","url":"https://arxiv.org/html/2603.05357"},{"title":"arXiv:2503.16429v1 [cs.CV] 20 Mar 2025","url":"https://arxiv.org/pdf/2503.16429"},{"title":"Self-Supervised Learning of Reliable Point Representations","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_Sonata_Self-Supervised_Learning_of_Reliable_Point_Representations_CVPR_2025_paper.pdf"},{"title":"GitHub - Eclipsess/Awesome-Efficient-Reasoning-LLMs: [TMLR 2025] Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models · GitHub","url":"https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs"},{"title":"Difficulty-Adaptive Self-Consistency for Cost-Efficient ...","url":"https://aclanthology.org/2025.findings-naacl.383.pdf"}]

Based on the search results, I found information about **Sonata** in the context of adaptive test-time compute for reasoning LLMs:

Sonata (Self-Consistency-Guided Adapter for Thinking Allocation) is a lightweight approach that adaptively allocates thinking budgets to optimize the performance-efficiency tradeoff.

## How It Works

The approach utilizes self-consistency (the agreement among multiple reasoning paths) as a proxy for thinking necessity, identifying that lower self-consistency indicates when queries require extended thinking to reach correct answers.

Sonata includes an adapter trained offline on a calibration dataset to predict self-consistency directly from the last layer hidden representations during the query prefilling stage, with this prediction then guiding on-the-fly budget allocation before thinking.

## Key Advantages

The adapter is general, transferable across diverse tasks once trained, and introduces less than 1‰ computational overhead during inference. Notably, Sonata is compatible with existing CoT compression methods, enabling further efficiency gains when managing thinking budgets across queries.

## Performance Results

Extensive experiments on multiple models (Qwen3-8B, Qwen3-32B, GPT-OSS-120B, Qwen3-235B-A22B) and benchmarks (AIME25, GSM8K, MATH500, GPQA, LiveCodeBench) demonstrate that Sonata achieves 20% to 60% reduction in thinking tokens while maintaining the same accuracy, or up to 2% improvement in accuracy with the same token cost.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83c5f8e6-284d-4da1-bacc-68869d1af052",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "3d8c490e-068f-4561-aa1c-e0f2faa15d77",
  "sourceToolAssistantUUID": "83c5f8e6-284d-4da1-bacc-68869d1af052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-12T00:05:55.631Z_

<details><summary>↩ Tool result · `toolu_01HrwXtcxntcYQ7hFneX4WaJ`</summary>

```text
Web search results for query: "TASER table agents schema extraction recommendation 2025"

Links: [{"title":"[2508.13404] TASER: Table Agents for Schema-guided Extraction and Recommendation","url":"https://arxiv.org/abs/2508.13404"},{"title":"[2508.13404v4] TASER: Table Agents for Schema-guided Extraction and Recommendation","url":"https://arxiv.org/abs/2508.13404v4"},{"title":"[2508.13404v2] TASER: Table Agents for Schema-guided Extraction and Recommendation","url":"https://arxiv.org/abs/2508.13404v2"},{"title":"TASER: Table Agents for Schema‑guided Extraction and Recommendation","url":"https://arxiv.org/html/2508.13404"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=21275&show=25"},{"title":"TASER: Table Agents for Schema-guided Extraction and ...","url":"https://www.researchgate.net/publication/394687747_TASER_Table_Agents_for_Schema-guided_Extraction_and_Recommendation"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=6725&show=250"},{"title":"Information Retrieval","url":"https://www.arxiv.org/list/cs.IR/recent?skip=62&show=250"},{"title":"TabAgent: A Multi-Agent Table Extraction Framework for Unstructured Documents","url":"https://www.vldb.org/2025/Workshops/VLDB-Workshops-2025/DATAI/DATAI25_6.pdf"},{"title":"Table-as-Search: Formulate Long-Horizon Agentic Information Seeking as Table Completion","url":"https://arxiv.org/html/2602.06724"}]

Based on the search results, I found detailed information about TASER:

## TASER: Table Agents for Schema-guided Extraction and Recommendation

TASER (Table Agents for Schema-guided Extraction and Recommendation) is a continuously learning, agentic table extraction system designed to handle complex financial data extraction.

### Key Capabilities

The system addresses the challenge of extracting critical information from messy, multi-page, fragmented tables that are difficult to parse, with 99.4% of tables in the financial dataset lacking bounding boxes and the largest table spanning 44 pages.

### Performance and Recommendations

The system's Recommender Agent reviews unmatched outputs and proposes schema revisions, enabling TASER to outperform vision-based table detection models such as Table Transformer by 10.1%. 

Within the continuous learning process, larger batch sizes yield a 104.3% increase in useful schema recommendations and a 9.8% increase in total extractions.

### Training and Dataset

To train TASER, 22,584 pages and 3,213 tables covering $731.7 billion in holdings were manually labeled, culminating in TASERTab to facilitate research on real-world financial tables and structured outputs.

The paper was submitted in August 2025 and accepted for presentation at EACL 2026 Industry track as an oral presentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a4c0813-bf95-4e31-8f5e-9d24560d12c3",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "d65b8f1f-3b17-43a8-bc37-1c6846a16687",
  "sourceToolAssistantUUID": "9a4c0813-bf95-4e31-8f5e-9d24560d12c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-12T00:05:56.502Z_

<details><summary>↩ Tool result · `toolu_01YTdx8TGaETH2JFAN1QSZhi`</summary>

```text
Web search results for query: ""majority voting" "information extraction" LLM multiple samples structured 2025"

Links: [{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://arxiv.org/html/2510.01499"},{"title":"An LLM-based Multi-Agent Collaborative Approach for ...","url":"https://www.medrxiv.org/content/10.1101/2025.08.11.25333429v2.full.pdf"},{"title":"[2510.01499] Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://arxiv.org/abs/2510.01499"},{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information | OpenReview","url":"https://openreview.net/forum?id=H1s6SBhzlg"},{"title":"Artificially intelligent opinion polling | Royal Society Open Science | The Royal Society","url":"https://royalsocietypublishing.org/rsos/article/13/3/251150/481004/Artificially-intelligent-opinion-polling"},{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://www.arxiv.org/pdf/2510.01499"},{"title":"MajorityVoting - Swarms","url":"https://docs.swarms.world/en/latest/swarms/structs/majorityvoting/"},{"title":"GitHub - stephenc222/tutorial-llm-voting-systems · GitHub","url":"https://github.com/stephenc222/tutorial-llm-voting-systems"},{"title":"Majority vote performance when each method can use at most 40 total LLM... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Majority-vote-performance-when-each-method-can-use-at-most-40-total-LLM-generation_fig1_393685921"},{"title":"LLM Voting: Human Choices and AI Collective Decision Making","url":"https://ideas.repec.org/p/arx/papers/2402.01766.html"}]

I found several relevant research papers on majority voting for LLM aggregation in 2025. Here are the key findings:

## Recent Research on Majority Voting with LLMs (2025)

Previous works have mostly employed the simple majority voting (MV) rule as a natural first instinct to aggregate different LLMs' responses into a single answer. However, recent research has identified limitations with this approach.

### Beyond Simple Majority Voting

Majority voting can be viewed as a zero-order aggregation method that only depends on the observed answers and fails to account for heterogeneity and correlation among models, which are often captured by higher-order information such as LLMs' expected accuracies (first-order information) and answer correlation (second-order information).

### Advanced Aggregation Methods

New aggregation algorithms called Optimal Weight (OW) and Inverse Surprising Popularity (ISP) leverage both first-order and second-order information. These methods consistently outperform majority voting, offering both practical performance gains and conceptual insights for the design of robust multi-agent LLM pipelines.

### Practical Applications

Three multi-LLM collaboration strategies were proposed and evaluated, including majority voting by averaging opinions of peers, multi-agent debate (MAD) for answer refinement, and LLM-based adjudication against answers of individual QA baselines. Majority voting was the best collaboration strategy, achieving the highest MAP 0.4621 and 0.3409 on subsets of systematic reviews about clinical intervention and diagnostic technology assessment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39195b85-a469-4dfc-bf15-79c648b5abe4",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "94426610-c258-45f3-9602-9e41800796d6",
  "sourceToolAssistantUUID": "39195b85-a469-4dfc-bf15-79c648b5abe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-12T00:05:58.582Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G83ygQMHm2nps1QVTunMoq`</summary>

```json
{
  "query": "\"early stopping self-consistency\" ESC sampling reasoning LLM arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94426610-c258-45f3-9602-9e41800796d6",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhUPPHX9bMHKffrA2LL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d642b470-21a6-43eb-9528-35d96862df68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUysdZwVBdgccXsW5BRp6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5684,
      "cache_read_input_tokens": 23395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5684,
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

_source line 50 · 2026-05-12T00:05:59.641Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uz65hjYKg5bUWeSXhW7DCq`</summary>

```json
{
  "query": "\"Thought Pruning\" \"self-consistency\" EMNLP 2025 efficient scaling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d642b470-21a6-43eb-9528-35d96862df68",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhUPPHX9bMHKffrA2LL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d5facef-299b-4c80-90dd-3c5ffdc4267d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUysdZwVBdgccXsW5BRp6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5684,
      "cache_read_input_tokens": 23395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5684,
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

_source line 51 · 2026-05-12T00:06:00.506Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bz5G2Q3PMpEc6eVrexv5oE`</summary>

```json
{
  "query": "DiSCTT consensus self-curriculum test-time adaptation reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d5facef-299b-4c80-90dd-3c5ffdc4267d",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhUPPHX9bMHKffrA2LL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b1ac8aa-a69c-4a29-8a3f-0bdc575cb579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUysdZwVBdgccXsW5BRp6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5684,
      "cache_read_input_tokens": 23395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5684,
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

_source line 52 · 2026-05-12T00:06:01.077Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FKYfjA4Ghfcko4AUv9rx6o`</summary>

```json
{
  "query": "\"consistency-accuracy\" LLM entity relation extraction plant health 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b1ac8aa-a69c-4a29-8a3f-0bdc575cb579",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhUPPHX9bMHKffrA2LL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a8e1d84-20fd-40c7-8aa0-8b03b0127104",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUysdZwVBdgccXsW5BRp6o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5684,
      "cache_read_input_tokens": 23395,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5684
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 23395,
          "cache_creation_input_tokens": 5684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5684,
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

_source line 53 · 2026-05-12T00:06:07.119Z_

<details><summary>↩ Tool result · `toolu_01Bz5G2Q3PMpEc6eVrexv5oE`</summary>

```text
Web search results for query: "DiSCTT consensus self-curriculum test-time adaptation reasoning 2025"

Links: [{"title":"DiSCTT: Consensus-Guided Self-Curriculum for Efficient Test-Time Adaptation in Reasoning","url":"https://arxiv.org/html/2603.05357"},{"title":"[2603.05357] DiSCTT: Consensus-Guided Self-Curriculum for Efficient Test-Time Adaptation in Reasoning","url":"https://arxiv.org/abs/2603.05357"},{"title":"TTCS: Test-Time Curriculum Synthesis for Self-Evolving","url":"https://arxiv.org/html/2601.22628"},{"title":"[2601.22628] TTCS: Test-Time Curriculum Synthesis for Self-Evolving","url":"https://arxiv.org/abs/2601.22628"},{"title":"A Survey of Adaptive and Controllable Test-Time Compute ...","url":"https://arxiv.org/pdf/2507.02076"},{"title":"May 23, 2025 Seek in the Dark: Reasoning via Test-Time Instance-Level Policy","url":"http://www.stat.ucla.edu/~ywu/2025Henry.pdf"},{"title":"The Surprising Effectiveness of Test-Time Training for Few-Shot Learning","url":"https://ekinakyurek.github.io/papers/ttt.pdf"},{"title":"SELF-IMPROVING LLM AGENTS AT TEST-TIME","url":"https://openreview.net/pdf?id=M1zSTXY1xr"},{"title":"TTCS: Test-Time Curriculum Synthesis for Self-Evolving","url":"https://www.arxiv.org/pdf/2601.22628"},{"title":"TTCS: Test-Time Curriculum Synthesis for Self-Evolving | Papers | HyperAI","url":"https://hyper.ai/en/papers/2601.22628"}]

Based on the search results, here's what I found about DiSCTT:

## DiSCTT Overview

DiSCTT stands for Difficulty-aware Consensus-Guided Self-Curriculum Test-Time Adaptation. It is a difficulty-aware, consensus-guided self-curriculum framework that dynamically allocates test-time optimization strategies based on instance-level epistemic uncertainty estimated from agreement among sampled reasoning trajectories.

## How It Works

The algorithm periodically generates M independent reasoning traces for each input and computes a consensus score measuring agreement among final answers. Inputs with consensus above a threshold are treated as high-consensus (easy) instances, while the remainder are classified as low-consensus (hard).

Inputs with high consensus are consolidated via supervised fine-tuning using majority-agreed solutions as pseudo-labels, while low-consensus inputs are optimized via reinforcement learning with a consensus-regularized objective that encourages diversity under relevance constraints.

## Key Insights

Agreement among independently sampled reasoning trajectories can provide a useful proxy for epistemic uncertainty: high consensus indicates stable reasoning modes, while disagreement reflects uncertainty over inference strategies. This trajectory-level consensus therefore serves as an effective, label-free estimate of relative instance difficulty at test time.

## Results

DiSCTT consistently improves accuracy, stability, and computational efficiency across diverse mathematical and general reasoning benchmarks, model scales, and test-time budgets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b1ac8aa-a69c-4a29-8a3f-0bdc575cb579",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "33352f55-2fa3-465f-b789-8843b6318c11",
  "sourceToolAssistantUUID": "8b1ac8aa-a69c-4a29-8a3f-0bdc575cb579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-12T00:06:07.165Z_

<details><summary>↩ Tool result · `toolu_01Uz65hjYKg5bUWeSXhW7DCq`</summary>

```text
Web search results for query: ""Thought Pruning" "self-consistency" EMNLP 2025 efficient scaling"

Links: [{"title":"GitHub - hyscale-lab/slimsc: Official repository for the EMNLP 2025 paper \"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency\".","url":"https://github.com/hyscale-lab/slimsc"},{"title":"Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://aclanthology.org/2025.emnlp-main.1750.pdf"},{"title":"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1750/"},{"title":"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/slim-sc-thought-pruning-for-efficient-scaling-with-self-consistency/"},{"title":"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://arxiv.org/pdf/2509.13990"},{"title":"[2509.13990] Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://arxiv.org/abs/2509.13990"},{"title":"[Literature Review] Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://www.themoonlight.io/en/review/slim-sc-thought-pruning-for-efficient-scaling-with-self-consistency"},{"title":"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://www.researchgate.net/publication/397418864_Slim-SC_Thought_Pruning_for_Efficient_Scaling_with_Self-Consistency"}]

Based on the search results, I found detailed information about the paper you were searching for:

## Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency

This is the official EMNLP 2025 accepted paper titled "Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency", authored by Colin Hong, Xu Guo, Anand Chaanan Singh, Esha Choukse, and Dmitrii Ustiugov.

### Overview
Self-Consistency (SC) generates multiple reasoning chains in parallel and selects the final answer via majority voting, but the order-of-magnitude computational overhead limits its broad deployment.

### The Slim-SC Solution
Slim-SC is a dynamic thought-pruning method that identifies and removes redundant chains step-by-step during generation based on their semantic similarity. The approach is based on the observation that correct and incorrect chains form distinct semantic clusters, with incorrect chains often being highly redundant.

### Performance Results
The method achieves significant efficiency gains, reducing end-to-end latency by up to 45% (on GPQA) and token usage by up to 32% (on AIME-2024), while also lowering mean KV Cache usage by 10pp. Notably, these gains are achieved while maintaining or even slightly improving accuracy (+0.5pp on GPQA) by retaining a more effective set of diverse candidate chains for the final vote.

The paper was published at EMNLP 2025 in November 2025, and the official repository is available on GitHub (hyscale-lab/slimsc).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d5facef-299b-4c80-90dd-3c5ffdc4267d",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "fc955c25-3019-47a2-95e0-a0e1acf15c95",
  "sourceToolAssistantUUID": "7d5facef-299b-4c80-90dd-3c5ffdc4267d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-12T00:06:07.927Z_

<details><summary>↩ Tool result · `toolu_01FKYfjA4Ghfcko4AUv9rx6o`</summary>

```text
Web search results for query: ""consistency-accuracy" LLM entity relation extraction plant health 2025"

Links: [{"title":"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"},{"title":"Statistical Network Analysis for LLMs via Knowledge Graphs","url":"https://www.techrxiv.org/users/972913/articles/1347041/master/file/data/KG__Paper%20(4)/KG__Paper%20(4).pdf?inline=true"},{"title":"Advancing clinical information extraction with LLM-Augmenter | Truveta","url":"https://www.truveta.com/blog/research/advancing-clinical-information-extraction-with-llm-augmenter/"},{"title":"The construction and refined extraction techniques of knowledge graph based on large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-38066-w"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/html/2510.20345v1"},{"title":"CLINES: Clinical LLM-based Information Extraction and Structuring Agent","url":"https://www.medrxiv.org/content/10.64898/2025.12.01.25341355v1.full.pdf"},{"title":"Large language model augmented joint learning framework for entity-relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"From LLMs to Knowledge Graphs: Building Production-Ready Graph Systems in 2025 | by Claudiu Branzan | Medium","url":"https://medium.com/@claudiubranzan/from-llms-to-knowledge-graphs-building-production-ready-graph-systems-in-2025-2b4aff1ec99a"},{"title":"Leveraging large language models for the deidentification and temporal normalization of sensitive health information in electronic health records | npj Digital Medicine","url":"https://www.nature.com/articles/s41746-025-01921-7"}]

Based on the web search results, I found highly relevant research on your query topic. Here are the key findings:

## Main Research Finding

A systematic study examines the relationship between accuracy and consistency in hard-prompted generative LLMs applied to entity and relation extraction, conducting evaluation using four LLMs (GPT, DeepSeek, Qwen, Kimi) on the EPOP corpus, a plant-health dataset with rich entity types, long-range relations, overlapping relations, and strong argument constraints.

## Key Concept Definitions

While accuracy has traditionally been the main evaluation metric, consistency—defined as the stability of model outputs across repeated runs—has recently been proposed as a complementary signal of reliability.

## Methodological Approach

To refine the interpretation of consistency, researchers distinguish between recoverable output variations—those that preserve the meaning of the extracted information—and critical ones that result in semantic errors.

## Context for Entity and Relation Extraction

As large language models (LLMs) become increasingly popular for information extraction, concerns persist regarding the stability and reliability of their outputs. This research directly addresses these concerns in the plant-health domain, providing empirical findings on how consistency and accuracy correlate in LLM-based information extraction tasks.

The research appears to be published in 2025 and represents a comprehensive empirical investigation of these critical evaluation metrics for LLM applications in plant-health information extraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a8e1d84-20fd-40c7-8aa0-8b03b0127104",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "a797e66e-d73b-46ab-b2b5-7571de67ccfc",
  "sourceToolAssistantUUID": "0a8e1d84-20fd-40c7-8aa0-8b03b0127104",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-12T00:06:08.118Z_

<details><summary>↩ Tool result · `toolu_01G83ygQMHm2nps1QVTunMoq`</summary>

```text
Web search results for query: ""early stopping self-consistency" ESC sampling reasoning LLM arXiv"

Links: [{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"[2401.10480] Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning","url":"https://arxiv.org/abs/2401.10480"},{"title":"Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning","url":"https://arxiv.org/html/2401.10480v1"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM","url":"https://arxiv.org/pdf/2601.02970"},{"title":"Preprint. EARLY STOPPING CHAIN-OF-THOUGHTS IN LARGE LANGUAGE MODELS","url":"https://arxiv.org/pdf/2509.14004"},{"title":"Deep Think with Confidence DEEP THINK WITH CONFIDENCE","url":"https://arxiv.org/pdf/2508.15260"},{"title":"Reasoning-Aware Self-Consistency : Leveraging Reasoning Paths for Efficient LLM generation Sampling | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/reasoning-aware-self-consistency-leveraging-reasoning-paths-for-efficient-llm-generation-sampling-ea4ac310bd5e"},{"title":"[2408.17017] Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling","url":"https://arxiv.org/abs/2408.17017"},{"title":"CGES: Confidence-Guided Early Stopping for Efficient and Accurate Self-Consistency","url":"https://arxiv.org/html/2511.02603v1"},{"title":"Dynamic Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling","url":"https://arxiv.org/html/2408.17017v1"}]

Based on the search results, I found several relevant papers on early stopping self-consistency (ESC) and related methods for efficient LLM reasoning:

## Key Papers Found:

### 1. **Early-Stopping Self-Consistency (ESC) - Original Paper**
ESC is a simple and scalable sampling process to greatly reduce the cost of self-consistency (SC) without sacrificing performance. ESC performs early stopping when all responses in a fixed context window of size 4 converge to the same answer. 

ESC reduces the average number of sampling of chain-of-thought reasoning by a significant margin on six benchmarks, including MATH (-33.8%), GSM8K (-80.1%), StrategyQA (-76.8%), CommonsenseQA (-78.5%), Coin Flip (-84.2%) and Last Letters (-67.4%), while attaining comparable performances.

**Paper Details:** Li et al. 2024. Escape sky-high cost: Early-stopping self-consistency for multi-step reasoning. arXiv preprint arXiv:2401.10480.

### 2. **Related Adaptive Approaches**

- **ReASC (Reliability-Aware Adaptive Self-Consistency):** ReASC is an adaptive self-consistency method that dynamically adjusts the sampling process.

- **RASC (Reasoning-Aware Self-Consistency):** RASC is an innovative early-stopping framework that dynamically adjusts the number of sample generations by considering both the output answer and the reasoning paths from Chain of Thought prompting.

- **CGES (Confidence-Guided Early Stopping):** CGES is a Bayesian framework that forms posteriors over candidate answers from scalar confidence signals and adaptively halts sampling, reducing the average number of calls by 69.4% while maintaining accuracy within 0.06 percentage points of self-consistency.

These papers all address the high computational cost of self-consistency sampling while maintaining comparable accuracy through various early-stopping mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d642b470-21a6-43eb-9528-35d96862df68",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "26c4b80b-06c0-493b-be8e-41e2b04e77d9",
  "sourceToolAssistantUUID": "d642b470-21a6-43eb-9528-35d96862df68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-12T00:06:11.239Z_

Now let me get a few final searches for the most directly competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26c4b80b-06c0-493b-be8e-41e2b04e77d9",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhVF9hzNKWK3SfBCZLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "130c373f-431f-45a1-8e95-a9deddc39057",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kz871jgzSyDfPy6JajykmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2699,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 29079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 58 · 2026-05-12T00:06:12.765Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0181CjNyrAf959Fkfh4QpVkt`</summary>

```json
{
  "query": "\"test-time scaling\" OR \"test-time compute\" \"information extraction\" OR \"named entity recognition\" OR \"NER\" 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "130c373f-431f-45a1-8e95-a9deddc39057",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhVF9hzNKWK3SfBCZLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c76fb2f-2605-47b1-8fb7-e790adc316b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kz871jgzSyDfPy6JajykmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2699,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 29079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 59 · 2026-05-12T00:06:13.191Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SCxshoCWuzNktjsBTSvswx`</summary>

```json
{
  "query": "langextract Google structured information extraction grounding 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c76fb2f-2605-47b1-8fb7-e790adc316b5",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhVF9hzNKWK3SfBCZLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c710793-b27f-4e95-ac3b-06e7b6966da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kz871jgzSyDfPy6JajykmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2699,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 29079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 60 · 2026-05-12T00:06:14.051Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FJo6CmjE2rG2Be9JRznvWT`</summary>

```json
{
  "query": "\"ReASC\" \"reliability-aware\" adaptive self-consistency sampling LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c710793-b27f-4e95-ac3b-06e7b6966da8",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhVF9hzNKWK3SfBCZLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81d67542-b84c-41ec-89ea-c8e6eae971bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kz871jgzSyDfPy6JajykmF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2699,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 29079,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2699,
          "output_tokens": 206,
          "cache_read_input_tokens": 29079,
          "cache_creation_input_tokens": 1237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1237,
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

_source line 61 · 2026-05-12T00:06:21.097Z_

<details><summary>↩ Tool result · `toolu_01SCxshoCWuzNktjsBTSvswx`</summary>

```text
Web search results for query: "langextract Google structured information extraction grounding 2025"

Links: [{"title":"GitHub - google/langextract: A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization. · GitHub","url":"https://github.com/google/langextract"},{"title":"Introducing LangExtract: A Gemini powered information extraction library - Google Developers Blog","url":"https://developers.googleblog.com/introducing-langextract-a-gemini-powered-information-extraction-library/"},{"title":"A Technical Deep Dive into Google’s Langextract: Grounded, Visual, and Scalable Information Extraction | by Shubham | Medium","url":"https://shubh7.medium.com/a-technical-deep-dive-into-googles-langextract-grounded-visual-and-scalable-information-afb0e7216da0"},{"title":"Google Launched LangExtract, a Python Library for Structured Data Extraction from Unstructured Text - InfoQ","url":"https://www.infoq.com/news/2025/08/google-langextract-python/"},{"title":"LangExtract — Google's Open-Source IDP Python Library","url":"https://idp-software.com/vendors/langextract/"},{"title":"LangExtract: Production LLM-Powered Information Extraction with Source Grounding | Gian Paolo Santopaolo","url":"https://genmind.ch/posts/LangExtract-Production-LLM-Powered-Information-Extraction/"},{"title":"Google AI Releases LangExtract: An Open Source Python Library that Extracts Structured Data from Unstructured Text Documents - MarkTechPost","url":"https://www.marktechpost.com/2025/08/04/google-ai-releases-langextract-an-open-source-python-library-that-extracts-structured-data-from-unstructured-text-documents/"},{"title":"langextract/langextract/extraction.py at main · google/langextract","url":"https://github.com/google/langextract/blob/main/langextract/extraction.py"},{"title":"Google’s LangExtract Explained: Why Source Grounding Makes AI Extraction Trustworthy | by Kamal Dhungana | Medium","url":"https://medium.com/@kbdhunga/googles-langextract-explained-why-source-grounding-makes-ai-extraction-trustworthy-c4f64b48dd43"},{"title":"LangExtract | Health AI Developer Foundations | Google for Developers","url":"https://developers.google.com/health-ai-developer-foundations/libraries/langextract"}]

Based on the search results, here's what I found about LangExtract:

## Overview

LangExtract is a Python library that uses LLMs to extract structured information from unstructured text documents based on user-defined instructions. It was released by Google on July 30, 2025 as an open-source Python library for LLM-powered information extraction.

## Key Features

The library is built on three core capabilities:

1. **Precise Source Grounding**: Every extracted entity is mapped back to its exact character offsets in the source text, providing traceability by visually highlighting each extraction in the original text.

2. **Reliable Structured Outputs**: LangExtract uses schema enforcement, leveraging Controlled Generation in supported models like Gemini to ensure consistently structured outputs.

3. **Long-Document Processing**: LangExtract is built to handle large documents using a chunking strategy, parallel processing and multiple extraction passes over smaller, focused contexts.

## Use Cases and Domains

The library works in critical real-world domains—including health (clinical notes, medical reports), finance (summaries, risk documents), law (contracts), research literature, and even the arts (analyzing Shakespeare). Google developed RadExtract, an interactive demonstration for structured radiology reporting on Hugging Face that shows how LangExtract can process a free-text radiology report and automatically convert its key findings into a structured format.

## Model Support and Licensing

LangExtract is designed to help developers extract structured information using large language models such as the Gemini models, and can be integrated with various LLMs, including cloud-based models like Gemini and local models via platforms such as Ollama. The library is available via PyPI under the Apache 2.0 license, making it free for commercial and research use.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c710793-b27f-4e95-ac3b-06e7b6966da8",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "e0a03ebe-a119-4e1d-8a90-a98671a1a225",
  "sourceToolAssistantUUID": "3c710793-b27f-4e95-ac3b-06e7b6966da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-12T00:06:21.535Z_

<details><summary>↩ Tool result · `toolu_0181CjNyrAf959Fkfh4QpVkt`</summary>

```text
Web search results for query: ""test-time scaling" OR "test-time compute" "information extraction" OR "named entity recognition" OR "NER" 2025 2026 arXiv"

Links: [{"title":"Selecting and Merging: Towards Adaptable and Scalable Named Entity Recognition with Large Language Models","url":"https://arxiv.org/html/2506.22813v1"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"[2604.20447] Decoding Text Spans for Efficient and Accurate Named-Entity Recognition","url":"https://arxiv.org/abs/2604.20447"},{"title":"Advancing clinical information extraction with LLM-Augmenter | Truveta","url":"https://www.truveta.com/blog/research/advancing-clinical-information-extraction-with-llm-augmenter/"},{"title":"CyberNER: A Harmonized STIX Corpus for Cybersecurity Named Entity Recognition","url":"https://arxiv.org/html/2510.26499v1"},{"title":"[2511.11978] A Reasoning Paradigm for Named Entity Recognition","url":"https://arxiv.org/abs/2511.11978"},{"title":"Structured Language Generation Model: Loss Calibration and Formatted Decoding for Robust Structure Prediction and Knowledge Retrieval","url":"https://arxiv.org/html/2402.08971"},{"title":"[2510.03577] LLM, Reporting In! Medical Information Extraction Across Prompting, Fine-tuning and Post-correction","url":"https://arxiv.org/abs/2510.03577"},{"title":"Enhancing Clinical Named Entity Recognition via Fine-Tuned BERT and Dictionary-Infused Retrieval-Augmented Generation","url":"https://www.mdpi.com/2079-9292/14/18/3676"}]

I found relevant results for your search. Here's a summary of recent papers from 2025-2026 on arXiv involving test-time scaling/compute with information extraction and NER:

## Key Papers Found

**1. Test-Time Scaling Methods Applied to NER:**

Large commercial language models underperform smaller fine-tuned models for information extraction and other structure- and retrieval-related tasks even with test-time scaling methods like in-context learning and chain-of-thought reasoning, according to a December 2025 paper on structured language generation models.

**2. Recent NER Approaches (2025-2026):**

- The SaM framework dynamically selects and merges expert models at inference time for a target domain, selecting domain-specific experts pre-trained on existing domains based on domain similarity and performance on sampled instances (June 2025).

- A reasoning paradigm for NER generates task-relevant reasoning chains and uses them to tune the NER model to generate coherent rationales before deriving the final answer, with a reasoning enhancement stage to optimize the reasoning process (November 2025).

- SpanDec proposes an efficient span-based NER framework where span representation interactions are computed at the final transformer stage via a lightweight decoder, with a span filtering mechanism during enumeration to prune unlikely candidates (April 2026).

**3. Few-Shot/Low-Resource Settings:**

Recent work on the EvalLLM 2025 challenge combines large language models with annotation guidelines and synthetic data, using in-context learning with GPT-4.1 and fine-tuned systems like GLiNER (October 2025).

Would you like more detailed information on any of these specific papers or approaches?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c76fb2f-2605-47b1-8fb7-e790adc316b5",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "eb79f998-2bfb-4373-8cb9-5bf71b2b7686",
  "sourceToolAssistantUUID": "3c76fb2f-2605-47b1-8fb7-e790adc316b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-12T00:06:22.358Z_

<details><summary>↩ Tool result · `toolu_01FJo6CmjE2rG2Be9JRznvWT`</summary>

```text
Web search results for query: ""ReASC" "reliability-aware" adaptive self-consistency sampling LLM 2025"

Links: [{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"[2601.02970] Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/abs/2601.02970"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM","url":"https://arxiv.org/pdf/2601.02970"},{"title":"ReASC: Reliability-Aware Adaptive Self-Consistency","url":"https://www.emergentmind.com/topics/reliability-aware-adaptive-self-consistency-reasc"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.184/"},{"title":"Dynamic Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling","url":"https://arxiv.org/html/2408.17017v1"},{"title":"Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2603.08999"},{"title":"[2408.17017] Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling","url":"https://arxiv.org/abs/2408.17017"},{"title":"Leveraging Reasoning Paths for Efficient LLM Sampling","url":"https://aclanthology.org/2025.naacl-long.184.pdf"}]

Based on the search results, here's what I found about ReASC:

## Overview

ReASC (Reliability-Aware Adaptive Self-Consistency) is an adaptive self-consistency framework that incorporates a self-certainty variant as a response-level reliability signal to guide how evidence is accumulated at inference time.

## Problem It Addresses

Self-Consistency improves reasoning reliability through multi-sample aggregation, but incurs substantial inference cost. Adaptive self-consistency methods mitigate this issue by adjusting the sampling budget; however, they rely on count-based stopping rules that treat all responses equally, often leading to unnecessary sampling.

## How It Works

ReASC addresses this limitation by reframing adaptive sampling from response counting to evidence sufficiency, leveraging response-level confidence for principled information aggregation. ReASC operates in two stages: a single-sample decision stage that resolves instances confidently answerable from a single response, and a reliability-aware accumulation stage that aggregates responses by jointly leveraging their frequency and confidence.

More specifically, the model first attempts a Single-Sample Decision (Stage 1) by evaluating whether the response reliability is sufficient. If not, it proceeds to Reliability-Aware Accumulation (Stage 2), where responses are adaptively sampled and aggregated via confidence-weighted Beta updates.

## Performance Results

Across five models and four datasets, ReASC consistently achieves the best accuracy-cost trade-off compared to existing baselines, yielding improved inference efficiency across model scales from 3B to 27B parameters. As a concrete example, ReASC reduces inference cost by up to 70% relative to self-consistency while preserving accuracy on GSM8K using Gemma-3-4B-it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81d67542-b84c-41ec-89ea-c8e6eae971bf",
  "isSidechain": true,
  "promptId": "562e4283-2dc1-4994-bc87-44a3ea9a2195",
  "agentId": "a4a05af61e888eb59",
  "type": "user",
  "uuid": "ac61d16f-575b-4db8-9b7f-d36061c6e243",
  "sourceToolAssistantUUID": "81d67542-b84c-41ec-89ea-c8e6eae971bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-12T00:08:03.095Z_

Here is my comprehensive adversarial review report on competing and concurrent work.

---

## Adversarial Literature Review: Adaptive Structural Self-Consistency Scaling

### CRITICAL FINDING: No paper found that does exactly what the proposal describes

I found **no existing work** that combines all three elements: (1) self-consistency/majority-voting applied to (2) structured/non-scalar outputs like NER/RE with (3) adaptive compute allocation. However, there is a **dense field of closely adjacent work** that the proposal must carefully cite and differentiate from. Several papers partially overlap and represent real competitive threats.

---

### 1. DIRECTLY RELEVANT: Self-Consistency Variants with Adaptive Compute (for scalar outputs)

These papers solve the "adaptive" part of the proposal but only for scalar (single-answer) outputs like math reasoning. The proposal **must** cite and differentiate from all of them:

**a) DSC: Difficulty-Adaptive Self-Consistency (NAACL 2025 Findings)**
- [Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning](https://aclanthology.org/2025.findings-naacl.383/)
- Ranks problem difficulty using the LLM itself, partitions into easy/hard, pre-allocates sample sizes. 65% cost reduction on GPT-4.
- **Threat level: HIGH.** This is the closest precedent for "adaptive compute allocation for self-consistency." The proposal's novelty must clearly show why extending this to structured outputs is non-trivial.

**b) ReASC: Reliability-Aware Adaptive Self-Consistency (arXiv Jan 2025)**
- [Reliability-Aware Adaptive Self-Consistency](https://arxiv.org/abs/2601.02970)
- Uses response-level confidence for principled information aggregation via Beta updates. Reduces cost by up to 70% while preserving accuracy.
- **Threat level: HIGH.** The confidence-gated early stopping mechanism is very similar in spirit to the proposal's adaptive allocation.

**c) ESC: Early-Stopping Self-Consistency (arXiv Jan 2024)**
- [Escape Sky-high Cost: Early-stopping Self-Consistency](https://arxiv.org/abs/2401.10480)
- Stops sampling when responses in a fixed window converge. 33-84% reduction in samples across benchmarks.

**d) CGES: Confidence-Guided Early Stopping (arXiv Nov 2025)**
- [CGES: Confidence-Guided Early Stopping for Efficient and Accurate Self-Consistency](https://arxiv.org/html/2511.02603v1)
- Bayesian framework forming posteriors over candidate answers from scalar confidence signals. 69.4% reduction in calls.

**e) CISC: Confidence-Informed Self-Consistency**
- Replaces uniform voting with model-derived scalar weights (response probability, verbal confidence, tokenwise probability). 40-50% cost reduction.

**f) Slim-SC: Thought Pruning for Efficient Scaling (EMNLP 2025)**
- [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1750/)
- Dynamically prunes redundant reasoning chains during generation based on semantic similarity. Up to 45% latency reduction.
- **Threat level: MEDIUM-HIGH.** The semantic clustering of correct vs. incorrect chains is analogous to what the proposal would need for structural consistency detection.

**g) Sonata: Self-Consistency-Guided Adapter for Thinking Allocation**
- Trains an adapter to predict self-consistency from hidden representations, guiding on-the-fly budget allocation. Tested on Qwen3-8B among others. 20-60% thinking token reduction.
- **Threat level: MEDIUM.** Directly uses Qwen3-8B and uses self-consistency as a difficulty signal, but only for reasoning tasks.

**h) DiSCTT: Consensus-Guided Self-Curriculum for Test-Time Adaptation (arXiv Mar 2026)**
- [DiSCTT: Consensus-Guided Self-Curriculum](https://arxiv.org/abs/2603.05357)
- Uses agreement among sampled reasoning trajectories as an epistemic uncertainty proxy. High-consensus instances get SFT, low-consensus get RL.
- **Threat level: MEDIUM.** The consensus-as-difficulty-proxy idea parallels the proposal's structural consistency signal.

---

### 2. DIRECTLY RELEVANT: Structured Output Consistency and Aggregation

**a) STED: Semantic Tree Edit Distance for JSON Consistency (NeurIPS 2025 Workshop)**
- [STED and Consistency Scoring Framework](https://arxiv.org/abs/2512.23712) (Amazon Science)
- A novel similarity metric for comparing JSON outputs combining structural, key, value, and type similarities. Uses Hungarian algorithm for order-invariant matching. Benchmarks 6 LLMs for structured output reliability.
- **Threat level: VERY HIGH.** This is the closest work to the "structural consistency" component. The proposal's aggregation mechanism for structured outputs could (and arguably should) use STED or something like it. The proposal must cite this and explain how its approach differs or builds upon it.

**b) Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information (ICLR 2025)**
- [Beyond Majority Voting](https://arxiv.org/abs/2510.01499)
- Proposes Optimal Weight (OW) and Inverse Surprising Popularity (ISP) algorithms that leverage first-order (expected accuracy) and second-order (answer correlation) information. Provably better than majority voting.
- **Threat level: MEDIUM.** Addresses aggregation of LLM outputs beyond simple voting, though focused on classification rather than structured IE.

**c) Consistency-Accuracy Correlation in LLMs for Entity and Relation Extraction (PMC 2025)**
- [Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction](https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/)
- Empirical study on 4 LLMs (GPT, DeepSeek, Qwen, Kimi) measuring consistency vs. accuracy for IE on plant-health data (EPOP corpus). Distinguishes "recoverable" vs. "critical" output variations.
- **Threat level: HIGH.** This directly studies the relationship between consistency and accuracy for structured IE outputs -- the very premise the proposal relies on. The proposal must engage with these empirical findings.

---

### 3. DIRECTLY RELEVANT: Schema-Guided / Constrained Decoding for IE

**a) Grammar-Constrained Decoding for Structured IE (Frontiers in AI, Jan 2025)**
- [Grammar-constrained decoding for structured information extraction with fine-tuned generative models](https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/)
- Fine-tuned encoder-decoder models (Longformer, Flan-T5) with grammar-constrained decoding for clinical trial PICO extraction. F1 improvement from 0.062 to 0.413.
- **Threat level: MEDIUM.** Validates the core approach of combining fine-tuning with constrained decoding for IE, but does not do self-consistency sampling.

**b) PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction (EMNLP 2025 Industry)**
- [PARSE](https://arxiv.org/abs/2510.08623) (Amazon)
- ARCHITECT autonomously optimizes JSON schemas; SCOPE implements reflection-based extraction with static + LLM guardrails. 64.7% improvement on SWDE, 92% error reduction on retry.
- **Threat level: MEDIUM.** Addresses schema optimization and reflection for IE, but not multi-sample consistency.

**c) XGrammar (arXiv Nov 2024, widely adopted)**
- [XGrammar: Flexible and Efficient Structured Generation Engine](https://arxiv.org/abs/2411.15100)
- Up to 14x speedup for JSON-schema generation. Integrated into vLLM, SGLang, MLC-LLM, TensorRT-LLM. XGrammar-2 released May 2026.
- **Threat level: LOW (complementary).** This is infrastructure the proposal would use, not compete with.

**d) SLOT: Structuring the Output of LLMs (EMNLP 2025 Industry)**
- [SLOT](https://aclanthology.org/2025.emnlp-industry.32.pdf)
- Fine-tuned Mistral-7B as a post-processing layer for structured output. 99.5% schema accuracy, 94.0% content similarity.
- **Threat level: LOW-MEDIUM.** Alternative approach to ensuring structured output quality.

---

### 4. ENSEMBLE METHODS FOR NER WITH LLMs

**a) EL4NER: Ensemble Learning for NER via Multiple Small-Parameter LLMs (arXiv May 2025)**
- [EL4NER](https://arxiv.org/abs/2505.23038)
- Decomposes NER into span extraction + type voting across multiple small LLMs. Includes self-validation for noise mitigation. Achieves SOTA among ICL-based methods.
- **Threat level: HIGH.** This is directly doing ensemble/voting for NER with LLMs. The key difference from the proposal is that EL4NER uses *different* models rather than multiple samples from one model, and uses ICL rather than fine-tuning. But the multi-model span-level voting + type confirmation pipeline is conceptually very close.

**b) GPT-NER (NAACL 2025 Findings)**
- [GPT-NER: Named Entity Recognition via Large Language Models](https://aclanthology.org/2025.findings-naacl.239/)
- Self-verification strategy for hallucination mitigation. Excels in low-resource/few-shot NER.

---

### 5. GOOGLE LANGEXTRACT (July 2025)

- [LangExtract](https://github.com/google/langextract) - Google's open-source Gemini-powered IE library
- Uses schema enforcement via controlled generation, chunking strategy for long documents, precise source grounding with character offsets.
- **Threat level: LOW (different paradigm).** Production tool, not a research contribution on self-consistency.

---

### 6. TASER: Table Agents for Schema-guided Extraction (EACL 2026 Industry, Oral)

- [TASER](https://arxiv.org/abs/2508.13404)
- Continuous-learning agentic extraction with Recommender Agent for schema revisions. Outperforms Table Transformer by 10.1%.
- **Threat level: LOW.** Different domain (financial tables) and approach (agentic), but the schema-guided extraction + continuous improvement angle has parallels.

---

### 7. QWEN3-8B SUITABILITY

Qwen3-8B is confirmed as a strong choice:
- 8.2B parameter dense transformer, Apache 2.0 license
- **Ranked #2 for fine-tuned performance** across 8 diverse tasks including information extraction in a 12-model benchmark
- Supports both reasoning and non-reasoning modes
- Extensive fine-tuning ecosystem: LoRA via Unsloth (2x faster, 70% less VRAM), SFT in 30 min on 22GB VRAM
- Recommendation: use 75% reasoning / 25% non-reasoning mix to maintain reasoning capability
- Already used in Sonata experiments for adaptive self-consistency

---

### 8. MAJOR VENUE PAPERS ON TEST-TIME SCALING (ACL/NAACL/EMNLP 2025)

I found these relevant accepted papers:
- **DSC** at NAACL 2025 Findings (adaptive self-consistency)
- **Slim-SC** at EMNLP 2025 Main (thought pruning for self-consistency)
- **RASC** at NAACL 2025 Long (reasoning-aware self-consistency)
- **Confidence Improves Self-Consistency** at ACL 2025 Findings
- **PARSE** at EMNLP 2025 Industry (schema optimization for IE)
- **SLOT** at EMNLP 2025 Industry (structured output post-processing)

**None of these specifically address self-consistency for structured/non-scalar prediction tasks like NER or RE.** The gap remains open.

---

### 9. KEY GAP ANALYSIS

The proposal's core novelty -- applying self-consistency with adaptive compute to **structured, non-scalar outputs** -- appears genuinely novel. However, the adversarial concerns are:

1. **The aggregation problem is underspecified.** How do you do "majority voting" on structured outputs (entity sets, relation tuples)? STED (the Amazon paper) provides a similarity metric but not an aggregation/voting mechanism. The proposal needs to clearly specify the aggregation algorithm (union? intersection? weighted voting per entity/relation? graph alignment?).

2. **The consistency-accuracy correlation may not hold for IE.** The plant-health empirical study (PMC 2025) directly investigates this. The proposal should engage with its findings -- if consistency and accuracy are only weakly correlated for IE, the entire premise weakens.

3. **EL4NER is a near-competitor.** It does multi-model ensemble voting for NER at the span level. The proposal must differentiate clearly: single model + multiple samples + constrained decoding vs. multiple models + ICL.

4. **The "adaptive" component has many strong baselines.** DSC, ReASC, ESC, CGES, and Sonata all do adaptive compute allocation for self-consistency. The proposal's contribution here would need to show that the structured output setting creates unique challenges not addressed by these methods.

5. **The field is moving fast.** DiSCTT (March 2026) combines consensus-based difficulty estimation with RL -- the proposal should check whether its adaptive mechanism adds anything beyond what DiSCTT-style approaches would provide if adapted to structured outputs.

---

Sources:
- [DSC: Difficulty-Adaptive Self-Consistency (NAACL 2025)](https://aclanthology.org/2025.findings-naacl.383/)
- [ReASC: Reliability-Aware Adaptive Self-Consistency](https://arxiv.org/abs/2601.02970)
- [ESC: Early-Stopping Self-Consistency](https://arxiv.org/abs/2401.10480)
- [CGES: Confidence-Guided Early Stopping](https://arxiv.org/html/2511.02603v1)
- [Slim-SC: Thought Pruning (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1750/)
- [DiSCTT: Consensus-Guided Self-Curriculum](https://arxiv.org/abs/2603.05357)
- [STED: Semantic Tree Edit Distance for JSON Consistency](https://arxiv.org/abs/2512.23712)
- [Beyond Majority Voting: LLM Aggregation](https://arxiv.org/abs/2510.01499)
- [Consistency-Accuracy Correlation for IE (Plant Health)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/)
- [Grammar-Constrained Decoding for Clinical IE](https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/)
- [PARSE: Schema Optimization for Entity Extraction (EMNLP 2025)](https://arxiv.org/abs/2510.08623)
- [XGrammar: Structured Generation Engine](https://arxiv.org/abs/2411.15100)
- [SLOT: Structuring LLM Output (EMNLP 2025)](https://aclanthology.org/2025.emnlp-industry.32.pdf)
- [EL4NER: Ensemble NER via Small LLMs](https://arxiv.org/abs/2505.23038)
- [GPT-NER (NAACL 2025)](https://aclanthology.org/2025.findings-naacl.239/)
- [LangExtract (Google)](https://github.com/google/langextract)
- [TASER: Table Agents for Schema-guided Extraction](https://arxiv.org/abs/2508.13404)
- [Sonata: Self-Consistency-Guided Thinking Allocation](https://openreview.net/forum?id=2i6Rp0gCq6)
- [Confidence Improves Self-Consistency (ACL 2025)](https://aclanthology.org/2025.findings-acl.1030.pdf)
- [RASC: Reasoning-Aware Self-Consistency (NAACL 2025)](https://aclanthology.org/2025.naacl-long.184/)
- [Qwen3-8B Fine-Tuning Guide (Unsloth)](https://unsloth.ai/docs/models/qwen3-how-to-run-and-fine-tune)
- [Test-Time Scaling Survey](https://testtimescaling.github.io/)
- [Stop Overthinking: Efficient Reasoning Survey (TMLR 2025)](https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac61d16f-575b-4db8-9b7f-d36061c6e243",
  "isSidechain": true,
  "agentId": "a4a05af61e888eb59",
  "requestId": "req_011CawhWHxfEetkPxER4qES5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6424593e-3459-491f-b08e-b74a382bd27d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fea1c215-3bad-412a-bcfe-9331b47cbd96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAaLAisHgJmZm61n2oK71q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5926,
      "cache_read_input_tokens": 30316,
      "output_tokens": 4304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5926
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4304,
          "cache_read_input_tokens": 30316,
          "cache_creation_input_tokens": 5926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5926,
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
