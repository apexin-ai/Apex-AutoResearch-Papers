# Research conversation: I'm reviewing a research proposal about adaptive test-time scaling for structured prediction/information extraction (sub

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a9c05864599146c9a.jsonl`
- **Structured JSON:** [`f7707475a072969b5e8a.json`](../../sessions/f7/f7707475a072969b5e8a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

55 recorded events

### User

_source line 1 · 2026-05-12T00:26:49.163Z_

I'm reviewing a research proposal about adaptive test-time scaling for structured prediction/information extraction (submitted to EMNLP 2026). I need to find any very recent concurrent work from the past 3 months (February-May 2026).

Search for each of these queries:
1. "test-time scaling structured prediction 2026 arxiv"
2. "self-consistency information extraction NER 2026"
3. "adaptive sampling structured output LLM 2026"
4. "confidence-gated structured prediction 2026"
5. "self-consistency voting NER relation extraction event extraction"
6. "site:arxiv.org structured self-consistency 2026"
7. "best-of-N structured output LLM aggregation 2026"
8. "test-time compute information extraction named entity"

For any relevant papers found, report title, authors, date, and how they relate to applying self-consistency/TTS to structured prediction tasks.

The key question: has anyone in 2026 published or preprinted work that directly applies test-time self-consistency scaling to information extraction or structured prediction with structural similarity-based aggregation?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "294bb931-1b91-4ee5-a55b-b3e5c6d6a7d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:26:49.165Z_

```json
{
  "parentUuid": "294bb931-1b91-4ee5-a55b-b3e5c6d6a7d9",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
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
  "uuid": "5c159cbf-3ced-4f5b-91d7-92f71b34feba",
  "timestamp": "2026-05-12T00:26:49.165Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:26:52.853Z_



I'll search for all these queries in parallel to find any concurrent work. Let me first load the WebSearch tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c159cbf-3ced-4f5b-91d7-92f71b34feba",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj4jfVGBR39y3Tw3XDC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afa56f55-2a69-4442-954d-cf2e77b8ffa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhQ72fN7YKV1Rno4xwXf1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 814,
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

_source line 4 · 2026-05-12T00:26:53.298Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019hVZQ78uWgyLAEhDPMEYSi`</summary>

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
  "parentUuid": "afa56f55-2a69-4442-954d-cf2e77b8ffa8",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj4jfVGBR39y3Tw3XDC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1215dd7-95ad-4bd9-9b0b-312b8799fd37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhQ72fN7YKV1Rno4xwXf1s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 8223,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 814
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 814,
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

_source line 5 · 2026-05-12T00:26:53.300Z_

<details><summary>↩ Tool result · `toolu_019hVZQ78uWgyLAEhDPMEYSi`</summary>

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
  "parentUuid": "f1215dd7-95ad-4bd9-9b0b-312b8799fd37",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "8902936c-bfc6-4e5e-a535-2e08cbfa7ce4",
  "sourceToolAssistantUUID": "f1215dd7-95ad-4bd9-9b0b-312b8799fd37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:26:57.837Z_



Now let me run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8902936c-bfc6-4e5e-a535-2e08cbfa7ce4",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj537yD84durvbvZKsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c705b79b-bef0-4992-aa0a-f4af1de02f7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsoqxHo3nmgJSkj7uzght8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 7 · 2026-05-12T00:26:58.784Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014TXwdUhSZ6weWUgk3NskrA`</summary>

```json
{
  "query": "test-time scaling structured prediction 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c705b79b-bef0-4992-aa0a-f4af1de02f7b",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj537yD84durvbvZKsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15d6cf92-598b-4326-9d47-a13638556bde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsoqxHo3nmgJSkj7uzght8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 8 · 2026-05-12T00:26:59.261Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EhqsLfoTo8DR4BDMgtHLmn`</summary>

```json
{
  "query": "self-consistency information extraction NER 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15d6cf92-598b-4326-9d47-a13638556bde",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj537yD84durvbvZKsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "263fab1d-5da0-4ca8-b883-707d964f53c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsoqxHo3nmgJSkj7uzght8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 9 · 2026-05-12T00:26:59.779Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q4GT174S8ExxuRUnUMn61C`</summary>

```json
{
  "query": "adaptive sampling structured output LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "263fab1d-5da0-4ca8-b883-707d964f53c9",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj537yD84durvbvZKsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0c8d6d8-073a-4fb5-9a97-41e9c5656325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsoqxHo3nmgJSkj7uzght8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 10 · 2026-05-12T00:27:00.206Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DrJmhX5ApnKab4jh6txQS1`</summary>

```json
{
  "query": "confidence-gated structured prediction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0c8d6d8-073a-4fb5-9a97-41e9c5656325",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj537yD84durvbvZKsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4d6f2f8-31b0-401e-8502-f7a4f180eebb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsoqxHo3nmgJSkj7uzght8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 11 · 2026-05-12T00:27:00.705Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SJsS1ZwKko1ZKpzxuj9ooG`</summary>

```json
{
  "query": "self-consistency voting NER relation extraction event extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4d6f2f8-31b0-401e-8502-f7a4f180eebb",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj537yD84durvbvZKsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b0b5fbd-ca29-4bd5-b698-b839cbd1c45a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsoqxHo3nmgJSkj7uzght8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 12 · 2026-05-12T00:27:01.170Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NmoqyL6VFaREhhijQAF969`</summary>

```json
{
  "query": "site:arxiv.org structured self-consistency 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b0b5fbd-ca29-4bd5-b698-b839cbd1c45a",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj537yD84durvbvZKsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d117ebe-a5e3-44a6-97f6-eed0adad9ea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsoqxHo3nmgJSkj7uzght8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 13 · 2026-05-12T00:27:02.097Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015MqSwuwNTrBfmhMSzErA8a`</summary>

```json
{
  "query": "best-of-N structured output LLM aggregation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d117ebe-a5e3-44a6-97f6-eed0adad9ea6",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj537yD84durvbvZKsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0e6fc63-4a38-4df0-9a0a-58e10d9044b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsoqxHo3nmgJSkj7uzght8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 14 · 2026-05-12T00:27:02.263Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CAkzB6b87owrUQH6bnt4AM`</summary>

```json
{
  "query": "test-time compute information extraction named entity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0e6fc63-4a38-4df0-9a0a-58e10d9044b4",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj537yD84durvbvZKsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36c783bf-351e-4e71-aa89-85448e002f10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsoqxHo3nmgJSkj7uzght8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9037,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1418
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 390,
          "cache_read_input_tokens": 9037,
          "cache_creation_input_tokens": 1418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1418,
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

_source line 15 · 2026-05-12T00:27:05.801Z_

<details><summary>↩ Tool result · `toolu_01DrJmhX5ApnKab4jh6txQS1`</summary>

```text
Web search results for query: "confidence-gated structured prediction 2026"

Links: [{"title":"The top 5 predictions for 2026 are in","url":"https://www.accredible.com/newsletter/certified-insights-newsletter-issue-14"},{"title":"CGV | 26 Predictions on the Development of Prediction Markets in 2026","url":"https://www.cgv.fund/post/cgv-26-predictions-on-the-development-of-prediction-markets-in-2026"},{"title":"18 Predictions for 2026 - Jakob Nielsen on UX - Substack","url":"https://jakobnielsenphd.substack.com/p/2026-predictions"},{"title":"IGCSE ADDITIONAL MATH PAPER 1 NON-CALCULATOR 2026 PREDICTION | Teaching Resources","url":"https://www.tes.com/teaching-resource/igcse-additional-math-paper-1-non-calculator-2026-prediction-13440146"},{"title":"18 Predictions for 2026","url":"https://www.uxtigers.com/post/2026-predictions"},{"title":"CODAPO: CONFIDENCE AND DIFFICULTY-ADAPTIVE ...","url":"https://openreview.net/pdf/a1f7e78e41f2b403921361cd24ce0cc5a8ce41ac.pdf"},{"title":"GCSE Predicted Papers 2026 | A Star Equivalency","url":"https://astarequivalency.co.uk/gcse-predicted-papers-2026/"},{"title":"AI Predictions 2026: The Year Agents Get Real | Vastkind","url":"https://www.vastkind.com/ai-predictions-2026-memory-agents-evals/"},{"title":"Grading 2025’s Biggest Predictions and What They Signal for 2026 | News Center","url":"https://news.gatech.edu/news/2026/02/05/grading-2025s-biggest-predictions-and-what-they-signal-2026"},{"title":"AI Search Predictions for 2026 | Yext","url":"https://www.yext.com/blog/2026/01/ai-search-predictions-for-2026"}]

Based on the search results, I found one relevant academic paper related to your query. There is a paper titled "CODAPO: CONFIDENCE AND DIFFICULTY-ADAPTIVE POLICY OPTIMIZATION FOR LANGUAGE MODELS" under review as a conference paper at ICLR 2026.

The paper addresses reinforcement learning post-training for large language models. It introduces CoDaPO, a confidence- and difficulty-adaptive approach that emphasizes more confident trajectories for more difficult questions, where correct answers on complex questions receive proportionally stronger reinforcement, while overconfident errors are down-weighted.

However, the search results did not return information specifically about "confidence-gated structured prediction" as a standalone technique or research area. The CODAPO paper appears to be the closest match, focusing on confidence and difficulty adaptation, though it primarily addresses policy optimization for language models rather than structured prediction broadly. If you're looking for more specific information about confidence-gated structured prediction methods, you may want to search academic databases like arXiv or Google Scholar directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4d6f2f8-31b0-401e-8502-f7a4f180eebb",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "f8509342-b0c1-4815-8c2a-c13d7ca9b734",
  "sourceToolAssistantUUID": "d4d6f2f8-31b0-401e-8502-f7a4f180eebb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T00:27:06.685Z_

<details><summary>↩ Tool result · `toolu_014TXwdUhSZ6weWUgk3NskrA`</summary>

```text
Web search results for query: "test-time scaling structured prediction 2026 arxiv"

Links: [{"title":"[2510.03605] Understanding the Role of Training Data in Test-Time Scaling","url":"https://arxiv.org/abs/2510.03605"},{"title":"[2602.01485] Predicting and improving test-time scaling laws via reward tail-guided search","url":"https://arxiv.org/abs/2602.01485"},{"title":"ATTS: Asynchronous Test-Time Scaling via Conformal Prediction","url":"https://arxiv.org/html/2509.15148"},{"title":"Exploring Test-time Scaling via Prediction Merging on Large-Scale Recommendation","url":"https://arxiv.org/html/2512.07650v1"},{"title":"[2511.14772] Test-time Scaling of LLMs: A Survey from A Subproblem Structure Perspective","url":"https://arxiv.org/abs/2511.14772"},{"title":"The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/html/2512.02008v1"},{"title":"[2512.02008] The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/abs/2512.02008"},{"title":"s1: Simple test-time scaling","url":"https://arxiv.org/pdf/2501.19393"},{"title":"[2604.16529] Scaling Test-Time Compute for Agentic Coding","url":"https://arxiv.org/abs/2604.16529"},{"title":"Test-time Scaling of LLMs: A Survey from A Subproblem Structure Perspective","url":"https://arxiv.org/html/2511.14772v1"}]

I found several recent arxiv papers related to test-time scaling and structured prediction from 2026. Here are the most relevant results:

## Survey and Foundational Work

A comprehensive survey titled "Test-time Scaling of LLMs: A Survey from A Subproblem Structure Perspective" examines techniques for improving the predictive accuracy of pretrained large language models by allocating additional compute at inference time, with special emphasis on how a problem is decomposed into subproblems and their topological organization—whether sequential, parallel, or tree-structured.

## Recent 2026 Papers

One paper studies the performance of test-time scaling for transformers trained on an in-context weight prediction task for linear regression. The analysis shows that increasing test-time compute allows reducing the number of in-context examples in training prompts, and if the skills required to solve a downstream task are not sufficiently present in the training data, increasing test-time compute can harm performance.

Another paper introduces Scaling-Law Guided (SLG) Search, a new test-time algorithm that dynamically allocates compute to identify and exploit intermediate states with the highest predicted potential.

A paper titled "ATTS: Asynchronous Test-Time Scaling via Conformal Prediction" proposes a training-free, lossless acceleration method that achieves a 56.7x speedup in test-time scaling and a 4.14x throughput improvement in both sequential and parallel settings.

## Application Areas

For agentic coding, researchers propose a test-time scaling framework based on compact representations of rollout trajectories that converts each rollout into a structured summary preserving salient hypotheses, progress, and failure modes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15d6cf92-598b-4326-9d47-a13638556bde",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "212ffefc-93b5-4481-9406-e715afff6408",
  "sourceToolAssistantUUID": "15d6cf92-598b-4326-9d47-a13638556bde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T00:27:07.402Z_

<details><summary>↩ Tool result · `toolu_01Q4GT174S8ExxuRUnUMn61C`</summary>

```text
Web search results for query: "adaptive sampling structured output LLM 2026"

Links: [{"title":"LLM Temperature and Sampling: The Complete 2026 Reference Guide | SurePrompts","url":"https://sureprompts.com/blog/llm-temperature-sampling-complete-guide-2026"},{"title":"Structured Outputs - vLLM","url":"https://docs.vllm.ai/en/latest/features/structured_outputs/"},{"title":"Producing Structured Outputs from LLMs with Constrained Sampling - Zilliz blog","url":"https://zilliz.com/blog/producing-structured-outputs-from-llms-with-constrained-sampling"},{"title":"Learning Adaptive LLM Decoding","url":"https://arxiv.org/html/2603.09065v1"},{"title":"GitHub - RLHFlow/Reinforce-Ada: An adaptive sampling framework for Reinforce-style LLM post training. · GitHub","url":"https://github.com/RLHFlow/Reinforce-Ada"},{"title":"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning & Coding with LLMs","url":"https://sample-step-by-step.info/"},{"title":"(PDF) Learning Adaptive LLM Decoding","url":"https://www.researchgate.net/publication/401771956_Learning_Adaptive_LLM_Decoding"},{"title":"Adaptive Sampling for Efficient Softmax Approximation Tavor Z. Baharav†","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d52dbd66219dc4e432e0bd4f9c25c4c3-Paper-Conference.pdf"},{"title":"A Developer’s Guide to Systematic Prompting: Mastering Negative Constraints, Structured JSON Outputs, and Multi-Hypothesis Verbalized Sampling • Dev|Journal","url":"https://earezki.com/ai-news/2026-05-03-a-developers-guide-to-systematic-prompting-mastering-negative-constraints-structured-json-outputs-and-multi-hypothesis-verbalized-sampling/"},{"title":"Structured outputs in LLMs: Definition, techniques, applications, benefits","url":"https://www.leewayhertz.com/structured-outputs-in-llms/"}]

Based on the search results, here's what I found about adaptive sampling and structured output in LLMs in 2026:

## Adaptive Sampling for LLM Decoding

Researchers have proposed learning adaptive decoding policies that dynamically select sampling strategies at inference time, conditioned on available compute resources. Current decoding practice relies on fixed sampling hyperparameters such as temperature and top-p chosen statically for an entire model or dataset, which ignores substantial heterogeneity across prompts, reasoning styles, and individual tokens.

Rather than fine-tuning the language model itself, lightweight decoding adapters are trained with reinforcement learning and verifiable terminal rewards (e.g. correctness on math and coding tasks). At the sequence level, decoding is framed as a contextual bandit problem where a policy selects a decoding strategy for each prompt, while at the token level, it's modeled as a partially observable Markov decision process (POMDP).

## Adaptive Sampling in Training

Reinforce-Ada is an adaptive sampling framework that uses a successive elimination process to eliminate prompts with sufficient learning signals while keeping sampling of unsolved prompts, with the algorithm sampling in rounds and deactivating prompts once a sufficient learning signal is found to free up computation for difficult prompts.

## Structured Output Techniques

Guided sampling enhances basic multinomial sampling by applying constraints that guide generation, with these constraints enforced through binary masks that filter out invalid tokens at each step. Generating structured outputs relies on constrained sampling and Context-Free Grammar (CFG) to ensure the model adheres strictly to predefined formats like JSON schemas by selectively guiding the generation of each token.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0c8d6d8-073a-4fb5-9a97-41e9c5656325",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "f19ae210-b968-4dc6-a029-2b52b50d403d",
  "sourceToolAssistantUUID": "e0c8d6d8-073a-4fb5-9a97-41e9c5656325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T00:27:08.079Z_

<details><summary>↩ Tool result · `toolu_01SJsS1ZwKko1ZKpzxuj9ooG`</summary>

```text
Web search results for query: "self-consistency voting NER relation extraction event extraction"

Links: [{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"A review of named entity recognition: from learning methods to modelling paradigms and tasks | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11321-8"},{"title":"Named Entity Recognition and Relation Extraction: State-of-the-Art","url":"https://dl.acm.org/doi/fullHtml/10.1145/3445965"},{"title":"ERA-CoT: Improving Chain-of-Thought through Entity ...","url":"https://aclanthology.org/2024.acl-long.476.pdf"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"A survey on Relation Extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2667305323000698"},{"title":"A Survey of Information Extraction Based on Deep Learning","url":"https://www.mdpi.com/2076-3417/12/19/9691"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"}]

Based on the web search results, here's what I found regarding self-consistency voting in relation to NER, relation extraction, and event extraction:

## Self-Consistency in Information Extraction

Self-consistency voting (CoT-SC) involves retrieving multiple reasoning chains to make majority votes, which has been applied to reasoning tasks. In the context of information extraction tasks like NER, relation extraction, and event extraction, self-consistency approaches are being explored.

## NER, Relation Extraction, and Event Extraction Connection

NER is crucial for information extraction and supports various downstream tasks, including event extraction and relation extraction. These three tasks are interconnected components of information extraction:

- Named Entity Recognition (NER) is a critical initial step in relation extraction, involving identifying and categorizing named entities within a text, such as the names of individuals, organizations, locations, and other specific entities

- The sub-tasks of Information Extraction (IE) include Named Entity Recognition (NER), Event Extraction, Relation Extraction (RE), Sentiment Extraction, Opinion Extraction, Terminology Extraction, Reference Extraction, and so on

## Recent Approaches with Consistency

Recent research has been exploring consistency-based approaches for these tasks. There are papers addressing consistency-guided knowledge retrieval and denoising in LLMs for zero-shot document-level relation triplet extraction, and consistency-based approaches for named entity recognition.

The search results indicate that self-consistency voting and consistency-based methods are increasingly being applied to information extraction tasks, though the specific combination of these techniques across all three tasks (NER, relation extraction, and event extraction) represents an active area of research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b0b5fbd-ca29-4bd5-b698-b839cbd1c45a",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "98130502-3227-4215-b58d-991cee90deb1",
  "sourceToolAssistantUUID": "3b0b5fbd-ca29-4bd5-b698-b839cbd1c45a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:27:08.241Z_

<details><summary>↩ Tool result · `toolu_01NmoqyL6VFaREhhijQAF969`</summary>

```text
Web search results for query: "site:arxiv.org structured self-consistency 2026"

Links: [{"title":"nchellwig at SemEval-2026 Task 3: Self-Consistent Structured Generation","url":"https://arxiv.org/pdf/2603.01788"},{"title":"Consistency Meets Verification: Enhancing Test","url":"https://arxiv.org/pdf/2602.10522"},{"title":"Self-Consistency Is Losing Its Edge: Diminishing Returns and Rising Costs in Modern LLMs","url":"https://arxiv.org/html/2511.00751"},{"title":"Understanding Pure Textual Reasoning for Blind Image Quality Assessment","url":"https://www.arxiv.org/pdf/2601.02441"},{"title":"Published as a conference paper at ICLR 2026 Workshop on MALGAI","url":"https://arxiv.org/pdf/2603.11445"},{"title":"Reinforcing Consistency in Video MLLMs with Structured Rewards","url":"https://arxiv.org/pdf/2604.01460"},{"title":"[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://arxiv.org/abs/2203.11171"},{"title":"[2511.12309] Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://arxiv.org/abs/2511.12309"},{"title":"Mind the Gap: Structure-Aware Consistency in Preference Learning","url":"https://arxiv.org/pdf/2604.27733"},{"title":"The Impact of LLM Self-Consistency and Reasoning Effort ...","url":"https://arxiv.org/pdf/2604.26954"}]

Based on the search results, here are the findings for "structured self-consistency 2026" on arxiv.org:

## Key Papers Found:

1. **Self-Consistent Structured Generation** (SemEval-2026 Task 3)
   The paper describes self-consistency majority voting applied to structured generation tasks, where aspect-sentiment pairs appearing in at least half of the runs are aggregated by averaging their valence and arousal values. It compares vanilla prompting with self-consistency approaches using 5, 10, or 15 prompt executions with majority voting.

2. **Consistency Meets Verification: Enhancing Test** (February 2026)
   The ConVerTest method incorporates Self-Consistency and Chain-of-Verification to mitigate hallucinations, using structured self-correction that shifts generation toward a process analogous to human developer review.

3. **Self-Consistency Is Losing Its Edge** (November 2025)
   This study adopted a structured self-consistency framework to evaluate the marginal benefit of increasing sampled reasoning paths, with multiple independent Chain-of-Thought responses from the same model.

4. **Reinforcing Consistency in Video MLLMs with Structured Rewards** (April 2026)
   The training objective integrates three complementary components: an instance-aware scene-graph reward for factual objects, a temporal reward for event ordering, and a video-grounded VQA reward for hierarchical self-verification.

These papers represent recent work exploring structured approaches to self-consistency in various domains including sentiment analysis, code generation, reasoning, and video understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d117ebe-a5e3-44a6-97f6-eed0adad9ea6",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "7375ec10-bf9a-4ff8-a581-c6848dc02262",
  "sourceToolAssistantUUID": "3d117ebe-a5e3-44a6-97f6-eed0adad9ea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T00:27:10.025Z_

<details><summary>↩ Tool result · `toolu_01CAkzB6b87owrUQH6bnt4AM`</summary>

```text
Web search results for query: "test-time compute information extraction named entity"

Links: [{"title":"What is entity extraction? A beginner’s guide | Google Cloud","url":"https://cloud.google.com/discover/what-is-entity-extraction"},{"title":"Named-entity recognition - Wikipedia","url":"https://en.wikipedia.org/wiki/Named-entity_recognition"},{"title":"Configuring Named Entity Extraction through Real-Time Exploitation of Linked Data | Proceedings of the 4th International Conference on Web Intelligence, Mining and Semantics (WIMS14)","url":"https://dl.acm.org/doi/10.1145/2611040.2611085"},{"title":"Extract information | Elastic Docs","url":"https://www.elastic.co/docs/explore-analyze/machine-learning/nlp/ml-nlp-extract-info"},{"title":"Named Entity Recognition and Relation Detection for Biomedical Information Extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7485218/"},{"title":"Improving Information Extraction from Pathology Reports using Named Entity Recognition - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10350195/"},{"title":"Structured information extraction from scientific text with large language models | Nature Communications","url":"https://www.nature.com/articles/s41467-024-45563-x"},{"title":"Named-Entity evaluation metrics based on entity-level","url":"https://www.davidsbatista.net/blog/2018/05/09/Named_Entity_Evaluation/"},{"title":"Named Entity Recognition Calculator | MetricGate","url":"https://metricgate.com/docs/named-entity-recognition/"},{"title":"Named Entity Recognition - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/named-entity-recognition/"}]

I've completed a web search for "test-time compute information extraction named entity." Here's what the search revealed:

## Overview of Named Entity Recognition and Information Extraction

Named Entity Recognition (NER) is a natural language processing task that identifies and classifies named entities in text into predefined categories such as persons (PER), organizations (ORG), locations (LOC), dates, monetary values, and more, and is a foundational NLP component used in information extraction, knowledge graph construction, question answering, and document understanding.

The goal of entity extraction is to turn unstructured text into structured data.

## Recent Advances with Large Language Models

Pretrained large language models (GPT-3, Llama-2) can be fine-tuned to extract useful records of complex scientific knowledge through joint named entity recognition and relation extraction.

## Common Approaches

NER systems have been created that use linguistic grammar-based techniques as well as statistical models such as machine learning, with state of the art systems incorporating multiple approaches.

The search results primarily cover general NER and information extraction methods, but don't specifically address research papers or specialized work on "test-time compute" in the context of NER. If you're looking for more specific information about test-time computational approaches or recent research in this area, I may need to search with different terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36c783bf-351e-4e71-aa89-85448e002f10",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "29c70aa9-057f-4941-b303-cb5cbf841798",
  "sourceToolAssistantUUID": "36c783bf-351e-4e71-aa89-85448e002f10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T00:27:10.045Z_

<details><summary>↩ Tool result · `toolu_01EhqsLfoTo8DR4BDMgtHLmn`</summary>

```text
Web search results for query: "self-consistency information extraction NER 2026"

Links: [{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"Named Entity Recognition: Master Enterprise-Scale Deep Learning for NLP in 2026 - Murali Krishna Marimekala","url":"https://muralimarimekala.com/2026/02/09/named-entity-recognition-deep-learning-nlp-enterprise/"},{"title":"Large language models for generative information extraction: a survey","url":"https://journal.hep.com.cn/fcs/EN/10.1007/s11704-024-40555-y"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Named Entity Recognition Ner AI Models in 2026 – Capabilities & Comparisons","url":"https://aiportalx.com/models/task/named-entity-recognition-ner"},{"title":"Named Entity Recognition (NER): Finding the Needle in the Haystack (AI 2026)","url":"https://blog.weskill.org/2026/04/named-entity-recognition-ner-finding.html"},{"title":"A review of named entity recognition: from learning methods to modelling paradigms and tasks | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11321-8"},{"title":"A Survey of Information Extraction Based on Deep Learning","url":"https://www.mdpi.com/2076-3417/12/19/9691"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"},{"title":"A survey on recent advances in Named Entity Recognition","url":"https://arxiv.org/html/2401.10825v1"}]

I've performed the web search for "self-consistency information extraction NER 2026". Here are the results:

## Key Findings

The search returned several recent sources covering named entity recognition (NER) and information extraction in 2026:

### Self-Consistency in Information Extraction

One approach involves LLMs making predictions on unlabeled corpus to generate self-annotated datasets through self-consistency. There have been efforts to employ LLMs for iterative self-verification and self-improvement, aiming to rectify results.

### NER and Information Extraction in 2026

Language models (LLMs) have recently shown great promise for automated digitization and information extraction, greatly improving upon previous tools in terms of speed and accuracy, with recent tools being assessed for their suitability for use in clinical settings.

In 2026, enterprise adoption of NER has reached critical mass, with the technology now appearing in production systems for healthcare record processing, legal document analysis, financial services, customer service platforms, and content platforms.

### Recent Developments

Systems are extracting entities from combined text, images, and videos simultaneously, where a system looks at a product photo, reads the product description, and watches an advertisement video to identify mentioned entities, appearing in enterprise content platforms.

Recent work includes "ConsistNER: Towards Instructive NER Demonstrations for LLMs with the Consistency of Ontology and Context", which directly relates to consistency in NER tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "263fab1d-5da0-4ca8-b883-707d964f53c9",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "02a660f1-6ac5-4e7d-8b9e-ef10640b67b6",
  "sourceToolAssistantUUID": "263fab1d-5da0-4ca8-b883-707d964f53c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T00:27:10.364Z_

<details><summary>↩ Tool result · `toolu_015MqSwuwNTrBfmhMSzErA8a`</summary>

```text
Web search results for query: "best-of-N structured output LLM aggregation 2026"

Links: [{"title":"LLM Agent & Tool-Use Benchmarks — Function Calling, MCP, Structured Output Rankings (2026) | BenchLM.ai","url":"https://benchlm.ai/llm-agent-benchmarks"},{"title":"LLM Structured Output in 2026: Stop Parsing JSON with Regex and Do It Right - Pockit Blog","url":"https://pockit.tools/blog/llm-structured-output-complete-guide/"},{"title":"LLM Search API: Best Options for Developers in 2026 | Sona","url":"https://www.sona.com/blog/llm-search-api-best-options-for-developers-in-2026"},{"title":"Top 5 Structured Output Libraries for LLMs in 2026 - DEV Community","url":"https://dev.to/nebulagg/top-5-structured-output-libraries-for-llms-in-2026-48g0"},{"title":"LLM Structured Outputs: The Practical Guide for Every Provider [2026]","url":"https://techsy.io/en/blog/llm-structured-outputs-guide"},{"title":"7+ Best AI Aggregator Platforms for 2026 | Aymo AI","url":"https://aymo.ai/blog/ai-aggregator-platforms"},{"title":"LLM Benchmarks 2026: 30+ Models Ranked — MMLU, SWE-bench, Arena Elo & Pricing","url":"https://iternal.ai/llm-selection-guide"},{"title":"Best Local LLM Models 2026: Benchmarks & Use Cases","url":"https://www.aitooldiscovery.com/how-to/best-local-llm-models"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"Top 5 LLMs for March 2026: Benchmarks, Pricing, Picks","url":"https://alphacorp.ai/blog/top-5-llms-for-march-2026-benchmarks-pricing-picks"}]

I found relevant search results on LLM structured output and aggregation topics for 2026. Here's what the results show:

## Structured Output in LLMs (2026)

Every major LLM provider now offers native structured output, and every major provider now supports it natively. Structured output uses constrained decoding to ensure every field, type, and constraint in your schema is met -- 100% of the time, not "usually."

The top structured output libraries for LLMs are Instructor, PydanticAI, Outlines, Guidance, and Zod. Structured output libraries solve this by sitting between your code and the LLM API, ensuring every response matches your schema -- either by validating after generation and retrying on failure, or by constraining the model's token generation so invalid output is physically impossible.

## LLM Aggregation & Multi-Model Approaches

The optimal architecture in 2026 routes different requests to different models based on task complexity, latency requirements, and cost constraints. A well-designed routing system can reduce costs by 50-80% while maintaining quality. For example, sending simple classification tasks to Haiku, medium-complexity tasks to Sonnet, and only the hardest tasks to Opus produces a blended cost of ~$10.50/M output tokens vs. $25/M for Opus across the board -- a 58% savings.

AI aggregator platforms have different AI models under a single dashboard. You can switch between the models and get your responses.

The search results focus more on general structured output approaches and multi-model routing strategies rather than specific "best-of-N" aggregation techniques, but they show that 2026 emphasizes native structured output guarantees and intelligent model selection routing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0e6fc63-4a38-4df0-9a0a-58e10d9044b4",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "832b66db-5708-4476-83c1-2858725a488f",
  "sourceToolAssistantUUID": "d0e6fc63-4a38-4df0-9a0a-58e10d9044b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-12T00:27:14.707Z_

I found one very promising lead -- the SemEval-2026 paper on self-consistent structured generation. Let me dig deeper into that and run a few more targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "832b66db-5708-4476-83c1-2858725a488f",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj6HhbgB2iXQuCLLQZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d49447ea-9fac-42ce-99c3-5e92bdf2530f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VSzY9Su84xGubo2c39z6Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 793,
      "cache_creation_input_tokens": 6751,
      "cache_read_input_tokens": 10455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6751,
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

_source line 24 · 2026-05-12T00:27:15.687Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0195gzpwtxJXCb82bfSoX3fT`</summary>

```json
{
  "query": "arxiv 2603.01788 nchellwig SemEval self-consistent structured generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d49447ea-9fac-42ce-99c3-5e92bdf2530f",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj6HhbgB2iXQuCLLQZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68db92d7-7caa-481a-b59d-40ddc5a5ccdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VSzY9Su84xGubo2c39z6Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 793,
      "cache_creation_input_tokens": 6751,
      "cache_read_input_tokens": 10455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6751,
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

_source line 25 · 2026-05-12T00:27:16.653Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CcjkQsyCdTpeM4AebvTCeZ`</summary>

```json
{
  "query": "\"self-consistency\" \"structured prediction\" \"information extraction\" arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68db92d7-7caa-481a-b59d-40ddc5a5ccdb",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj6HhbgB2iXQuCLLQZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c861f59-6e84-4c31-b7a8-94027d2234bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VSzY9Su84xGubo2c39z6Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 793,
      "cache_creation_input_tokens": 6751,
      "cache_read_input_tokens": 10455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6751,
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

_source line 26 · 2026-05-12T00:27:17.070Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PCLGLWtKdDxB8yWyhwCzkD`</summary>

```json
{
  "query": "arxiv 2026 \"test-time\" \"named entity recognition\" OR \"relation extraction\" self-consistency sampling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c861f59-6e84-4c31-b7a8-94027d2234bd",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj6HhbgB2iXQuCLLQZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e67f176f-cbcd-4ebb-917a-49f18493fa6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VSzY9Su84xGubo2c39z6Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 793,
      "cache_creation_input_tokens": 6751,
      "cache_read_input_tokens": 10455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6751,
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

_source line 27 · 2026-05-12T00:27:17.668Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016z5fByJ711hwzaFSkkH8MD`</summary>

```json
{
  "query": "\"structural similarity\" aggregation \"information extraction\" LLM voting 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e67f176f-cbcd-4ebb-917a-49f18493fa6e",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj6HhbgB2iXQuCLLQZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54e1d4e6-d568-48f4-88bb-fb72f64ffbb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VSzY9Su84xGubo2c39z6Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 793,
      "cache_creation_input_tokens": 6751,
      "cache_read_input_tokens": 10455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6751,
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

### Tool result

_source line 28 · 2026-05-12T00:27:21.713Z_

<details><summary>↩ Tool result · `toolu_0195gzpwtxJXCb82bfSoX3fT`</summary>

```text
Web search results for query: "arxiv 2603.01788 nchellwig SemEval self-consistent structured generation"

Links: [{"title":"[2603.01788] nchellwig at SemEval-2026 Task 3: Self-Consistent Structured Generation (SCSG) for Dimensional Aspect-Based Sentiment Analysis using Large Language Models","url":"https://arxiv.org/abs/2603.01788"},{"title":"nchellwig at SemEval-2026 Task 3: Self-Consistent Structured Generation (SCSG) for Dimensional Aspect-Based Sentiment Analysis using Large Language Models","url":"https://arxiv.org/html/2603.01788"},{"title":"nchellwig at SemEval-2026 Task 3: Self-Consistent Structured Generation","url":"https://arxiv.org/pdf/2603.01788"},{"title":"[2603.29292v1] Self-Improving Code Generation via Semantic Entropy and Behavioral Consensus","url":"https://arxiv.org/abs/2603.29292v1"},{"title":"Self-StrAE at SemEval-2024 Task 1: Making Self-Structuring AutoEncoders Learn More With Less","url":"https://arxiv.org/html/2404.01860v1"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=767&show=2000"},{"title":"Span Modeling for Idiomaticity and Figurative Language Detection with Span Contrastive Loss","url":"https://arxiv.org/html/2603.22799"},{"title":"[2603.10700] Structured Linked Data as a Memory Layer for Agent-Orchestrated Retrieval","url":"https://arxiv.org/abs/2603.10700"},{"title":"[2603.29292] Self-Improving Code Generation via Semantic Entropy and Behavioral Consensus","url":"https://arxiv.org/abs/2603.29292"},{"title":"AILS-NTUA at SemEval-2026 Task 3: Efficient Dimensional Aspect-Based Sentiment Analysis","url":"https://arxiv.org/html/2603.04933"}]

I found the paper! Here's what I found about arxiv 2603.01788:

The paper is titled "nchellwig at SemEval-2026 Task 3: Self-Consistent Structured Generation (SCSG) for Dimensional Aspect-Based Sentiment Analysis using Large Language Models" by Nils Constantin Hellwig and 3 other authors.

**Key Details:**

SCSG enhances prediction reliability by executing a LoRA-adapted large language model multiple times per instance, retaining only tuples that achieve a majority consensus across runs. To mitigate the computational overhead of multiple forward passes, the approach leverages vLLM's PagedAttention mechanism for efficient key-value cache reuse.

**Results:**

Evaluation across 6 languages and 8 language-domain combinations demonstrates that self-consistency with 15 executions yields statistically significant improvements over single-inference prompting, with the system (leveraging Gemma 3) ranking in the top seven across all settings.

The paper was submitted on March 2, 2026 and addresses the SemEval-2026 Task 3 shared task on Dimensional Aspect-Based Sentiment Analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68db92d7-7caa-481a-b59d-40ddc5a5ccdb",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "dc6d4bac-2070-4519-a543-acde08050fdb",
  "sourceToolAssistantUUID": "68db92d7-7caa-481a-b59d-40ddc5a5ccdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-12T00:27:22.935Z_

<details><summary>↩ Tool result · `toolu_01PCLGLWtKdDxB8yWyhwCzkD`</summary>

```text
Web search results for query: "arxiv 2026 "test-time" "named entity recognition" OR "relation extraction" self-consistency sampling"

Links: [{"title":"A Few-Shot Learning Focused Survey on Recent Named Entity Recognition and","url":"https://arxiv.org/pdf/2310.19055"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study","url":"https://arxiv.org/html/2401.10825v3"},{"title":"A survey on recent advances in Named Entity Recognition","url":"https://arxiv.org/html/2401.10825v1"},{"title":"[1912.13415] End-to-end Named Entity Recognition and Relation Extraction using Pre-trained Language Models","url":"https://arxiv.org/abs/1912.13415"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"Selecting and Merging: Towards Adaptable and Scalable Named Entity Recognition with Large Language Models","url":"https://arxiv.org/html/2506.22813v1"},{"title":"[1910.11470] A Survey on Recent Advances in Named Entity Recognition from Deep Learning models","url":"https://ar5iv.labs.arxiv.org/html/1910.11470"},{"title":"A novel large-language-model-driven framework for named entity recognition - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457324004138"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"}]

The search results contain some relevant papers on named entity recognition and relation extraction, though they don't show many results specifically focused on "test-time" approaches with "self-consistency sampling" in 2026 publications. 

The most relevant finding is from result index 7, which discusses self-consistency (SC) approaches for NER, comparing traditional SC (T-SC) that adjusts temperature hyperparameters to ensemble outputs with expert-based SC (E-SC) that ensembles outputs from different experts, noting that traditional SC shows limited improvement for the NER task while E-SC offers more significant gains.

Additionally, there's research on using self-consistency for generating self-annotated datasets with LLMs, where LLMs make predictions on unlabeled corpora, different strategies explore selection of reliable annotations, and demonstrations from reliable self-annotated datasets are retrieved for in-context learning during inference.

The search results indicate that while self-consistency and sampling methods are being explored for NER and relation extraction tasks with language models, the specific combination of "test-time" self-consistency sampling for these tasks in 2026 papers may require more targeted research in the current literature.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e67f176f-cbcd-4ebb-917a-49f18493fa6e",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "153ab17d-b71d-4a61-9cd1-4376188943bc",
  "sourceToolAssistantUUID": "e67f176f-cbcd-4ebb-917a-49f18493fa6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T00:27:24.236Z_

<details><summary>↩ Tool result · `toolu_01CcjkQsyCdTpeM4AebvTCeZ`</summary>

```text
Web search results for query: ""self-consistency" "structured prediction" "information extraction" arxiv 2026"

Links: [{"title":"Self-Consistency Improves Chain of Thought Reasoning in ...","url":"https://arxiv.org/pdf/2203.11171"},{"title":"[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://arxiv.org/abs/2203.11171"},{"title":"[2505.12642] Two out of Three (ToT): using self-consistency to make robust predictions","url":"https://arxiv.org/abs/2505.12642"},{"title":"Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://arxiv.org/pdf/2511.12309"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"When Career Data Runs Out: Structured Feature Engineering and Signal Limits for Founder Success Prediction","url":"https://arxiv.org/html/2604.00339"},{"title":"[2511.12309] Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://arxiv.org/abs/2511.12309"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"[1608.00612v1] Structured prediction models for RNN based sequence labeling in clinical text","url":"https://arxiv.org/abs/1608.00612v1"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview","url":"https://openreview.net/forum?id=1PL1NIMMrw"}]

I've performed the web search for your query on "self-consistency" "structured prediction" "information extraction" arxiv 2026. Here are the results:

## Key Findings

The search returned several relevant papers from arXiv:

1. **"Self-Consistency Improves Chain of Thought Reasoning in Language Models"** (arxiv 2203.11171) - This paper proposes a decoding strategy called self-consistency that replaces greedy decoding, first sampling a diverse set of reasoning paths and then selecting the most consistent answer by marginalizing out the sampled reasoning paths.

2. **"Two out of Three (ToT): using self-consistency to make robust predictions"** (arxiv 2505.12642) - This algorithm creates two alternative predictions in addition to the original model prediction and uses the alternative predictions to decide whether it should provide an answer or not.

3. **"Optimal Self-Consistency for Efficient Reasoning with Large Language Models"** (arxiv 2511.12309) - This work explains that self-consistency involves sampling n chain-of-thought generations and selecting the most frequent answer, functioning as a plurality vote across sampled outputs.

4. **Grammar-constrained decoding for structured information extraction** (Frontiers in AI, 2024) - This paper presents a grammar-constrained decoding approach for structured information extraction with fine-tuned generative language models that predict complex output structures.

5. **Large language models for generative information extraction survey** - This appears to cover various approaches to structured prediction and information extraction using LLMs.

The most recent papers from 2025-2026 focus on improving self-consistency efficiency and robustness, while structured information extraction remains an active area combining constraint-based decoding with neural models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c861f59-6e84-4c31-b7a8-94027d2234bd",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "47287cad-a2f3-44fe-a137-fbe2c7193c2e",
  "sourceToolAssistantUUID": "4c861f59-6e84-4c31-b7a8-94027d2234bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-12T00:27:24.690Z_

<details><summary>↩ Tool result · `toolu_016z5fByJ711hwzaFSkkH8MD`</summary>

```text
Web search results for query: ""structural similarity" aggregation "information extraction" LLM voting 2026"

Links: [{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://arxiv.org/html/2510.01499v1"},{"title":"[2510.01499] Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://arxiv.org/abs/2510.01499"},{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information | OpenReview","url":"https://openreview.net/forum?id=H1s6SBhzlg"},{"title":"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information","url":"https://www.arxiv.org/pdf/2510.01499"},{"title":"SERE: Structural Example Retrieval for Enhancing LLMs in Event Causality Identification","url":"https://arxiv.org/html/2605.03701"},{"title":"Combining Information Extraction Systems Using Voting and Stacked Generalization","url":"https://www.jmlr.org/papers/v6/sigletos05a.html"},{"title":"Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis","url":"https://arxiv.org/html/2602.10881"},{"title":"Semantic Operators and Their Optimization: Enabling","url":"https://www.vldb.org/pvldb/vol18/p4171-patel.pdf"},{"title":"dblp: Combining Information Extraction Systems Using Voting and Stacked Generalization.","url":"https://dblp.org/rec/journals/jmlr/SigletosPSH05.html"},{"title":"Combining Information Extraction Systems Using Voting and Stacked Generalization | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/abs/10.5555/1046920.1194903"}]

I found several relevant research papers related to your search query. Here are the main findings:

## LLM Aggregation Methods (2025-2026)

Recent work on multi-agent LLM reasoning has introduced new aggregation algorithms called Optimal Weight (OW) and Inverse Surprising Popularity (ISP), leveraging both first-order and second-order information. Standard majority voting treats all answers equally, failing to consider latent heterogeneity and correlation across models, which these newer methods address.

## Structural Similarity and Information Extraction

The SERE framework uses structural similarity measures based on edit distance between conceptual paths from ConceptNet to enhance LLMs' performance on event causality identification tasks. The final score of corpus samples is obtained by weighting and aggregating scores from multiple structural metrics.

## Voting Approaches in Information Extraction

Voting has proven effective in most domains for combining information extraction systems, while stacking proved to be consistently effective over all domains, doing comparably or better than voting.

## LLM-Based Evidence Extraction Challenges

Recent work considers lightweight aggregation operations to probe whether extracted evidence can be coherently integrated at the corpus level in LLM-based evidence extraction pipelines.

The search results show active research in combining aggregation strategies, structural similarity measures, and voting mechanisms for improving LLM performance on information extraction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54e1d4e6-d568-48f4-88bb-fb72f64ffbb2",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "cdb92fa7-e55e-46f9-bad5-e8485046aa72",
  "sourceToolAssistantUUID": "54e1d4e6-d568-48f4-88bb-fb72f64ffbb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-12T00:27:29.121Z_

Let me run a few more targeted searches to make sure I haven't missed anything directly relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdb92fa7-e55e-46f9-bad5-e8485046aa72",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj7LyKtzJJ4xPG44dWM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb128f42-5f2c-466e-8d41-010895f548d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhxJ2iy2ZVWTNTYt6A5d7y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4463,
      "cache_read_input_tokens": 17206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4463,
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

_source line 33 · 2026-05-12T00:27:30.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KoTyjQ6F6br4SXXU4JPCm2`</summary>

```json
{
  "query": "arxiv 2026 \"test-time scaling\" NER \"named entity\" structured output aggregation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb128f42-5f2c-466e-8d41-010895f548d5",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj7LyKtzJJ4xPG44dWM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99654cbf-e611-4af4-9dd6-9150d6902a61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhxJ2iy2ZVWTNTYt6A5d7y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4463,
      "cache_read_input_tokens": 17206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4463,
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

_source line 34 · 2026-05-12T00:27:30.544Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RpfZJvwSN1oerdEbaMVTfT`</summary>

```json
{
  "query": "arxiv 2026 \"adaptive consistency\" OR \"adaptive self-consistency\" structured prediction information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99654cbf-e611-4af4-9dd6-9150d6902a61",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj7LyKtzJJ4xPG44dWM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3109c9bb-6220-42ca-bf61-392d186b932a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhxJ2iy2ZVWTNTYt6A5d7y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4463,
      "cache_read_input_tokens": 17206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4463,
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

_source line 35 · 2026-05-12T00:27:31.543Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NqrbAUf78LFYXj5YEKHZkg`</summary>

```json
{
  "query": "\"sample-step-by-step\" OR \"adaptive-consistency\" structured prediction NER 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3109c9bb-6220-42ca-bf61-392d186b932a",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj7LyKtzJJ4xPG44dWM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f395431-842c-4574-aeb5-f67048321507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhxJ2iy2ZVWTNTYt6A5d7y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4463,
      "cache_read_input_tokens": 17206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4463,
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

_source line 36 · 2026-05-12T00:27:32.075Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KHvzsxg4ro7hwHTxgzNCpC`</summary>

```json
{
  "query": "arxiv 2026 multiple sampling aggregation NER relation extraction structured"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f395431-842c-4574-aeb5-f67048321507",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj7LyKtzJJ4xPG44dWM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54d09fc6-6fb9-4a6d-bbbc-60f55d01255c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhxJ2iy2ZVWTNTYt6A5d7y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4463,
      "cache_read_input_tokens": 17206,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4463
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 17206,
          "cache_creation_input_tokens": 4463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4463,
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

_source line 37 · 2026-05-12T00:27:37.709Z_

<details><summary>↩ Tool result · `toolu_01NqrbAUf78LFYXj5YEKHZkg`</summary>

```text
Web search results for query: ""sample-step-by-step" OR "adaptive-consistency" structured prediction NER 2026"

Links: [{"title":"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | OpenReview","url":"https://openreview.net/forum?id=ETNa4Wb65J"},{"title":"[2305.11860] Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs","url":"https://arxiv.org/abs/2305.11860"},{"title":"GitHub - Pranjal2041/AdaptiveConsistency: Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning with LLMs · GitHub","url":"https://github.com/Pranjal2041/AdaptiveConsistency"},{"title":"Paper page - Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning with LLMs","url":"https://huggingface.co/papers/2305.11860"},{"title":"Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.761/"},{"title":"Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | Request PDF","url":"https://www.researchgate.net/publication/376401874_Let's_Sample_Step_by_Step_Adaptive-Consistency_for_Efficient_Reasoning_and_Coding_with_LLMs"},{"title":"GitHub - fscdc/Awesome-Efficient-Reasoning-Models: [TMLR 2025] Efficient Reasoning Models: A Survey · GitHub","url":"https://github.com/fscdc/Awesome-Efficient-Reasoning-Models"},{"title":"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning & Coding with LLMs","url":"https://sample-step-by-step.info/"},{"title":"(PDF) Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning with LLMs","url":"https://www.researchgate.net/publication/370938427_Let's_Sample_Step_by_Step_Adaptive-Consistency_for_Efficient_Reasoning_with_LLMs"},{"title":"[PDF] Let's Sample Step by Step: Adaptive-Consistency for ...","url":"https://www.semanticscholar.org/paper/Let's-Sample-Step-by-Step:-Adaptive-Consistency-for-Aggarwal-Madaan/b4a6c010724f0459c9791018e34a982cf96987cf"}]

Based on the search results, I found information about the "sample-step-by-step" and "adaptive-consistency" approaches:

## Adaptive-Consistency Technique

Adaptive-Consistency is a cost-efficient, model-agnostic technique that dynamically adjusts the number of samples per question using a lightweight stopping criterion. This approach improves upon Self-Consistency, which polls an LLM multiple times to output the most frequent solution, by non-uniformly distributing the available budget based on the amount of agreement in samples drawn so far.

## Performance Results

Experiments over 13 datasets and two LLMs demonstrate that Adaptive-Consistency reduces sample budget by up to 7.9 times with an average accuracy drop of less than 0.1%.

## Publication Information

The work was authored by Pranjal Aggarwal, Aman Madaan, Yiming Yang, and Mausam, and published in the Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing.

**Note:** The search results focus on Adaptive-Consistency for efficient reasoning and coding with LLMs rather than on structured prediction or Named Entity Recognition (NER) specifically. The 2023 publication predates 2026, so this appears to be an earlier work that's being referenced in the context of your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f395431-842c-4574-aeb5-f67048321507",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "ae3c0753-261c-41af-877d-1af22911c4fb",
  "sourceToolAssistantUUID": "9f395431-842c-4574-aeb5-f67048321507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-12T00:27:38.379Z_

<details><summary>↩ Tool result · `toolu_01KoTyjQ6F6br4SXXU4JPCm2`</summary>

```text
Web search results for query: "arxiv 2026 "test-time scaling" NER "named entity" structured output aggregation"

Links: [{"title":"Generalizing Test-time Compute-optimal Scaling as an Optimizable Graph","url":"https://arxiv.org/html/2511.00086"},{"title":"[2604.11753] Agentic Aggregation for Parallel Scaling of Long-Horizon Agentic Tasks","url":"https://arxiv.org/abs/2604.11753"},{"title":"SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition","url":"https://arxiv.org/html/2605.03706"},{"title":"[2601.17898] Assessment of Generative Named Entity Recognition in the Era of Large Language Models","url":"https://arxiv.org/abs/2601.17898"},{"title":"LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling","url":"https://arxiv.org/html/2605.08083"},{"title":"Agentic Test-Time Scaling for WebAgents","url":"https://arxiv.org/html/2602.12276"},{"title":"[2604.16529] Scaling Test-Time Compute for Agentic Coding","url":"https://arxiv.org/abs/2604.16529"},{"title":"[2602.12276v1] Agentic Test-Time Scaling for WebAgents","url":"https://arxiv.org/abs/2602.12276v1"},{"title":"Scaling Test-Time Compute for Agentic Coding","url":"https://www.emergentmind.com/papers/2604.16529"},{"title":"Benchmark Test-Time Scaling of General LLM Agents","url":"https://arxiv.org/html/2602.18998v1"}]

I've found several relevant papers from the 2026 arXiv corpus related to test-time scaling and structured output aggregation. Here are the key results:

## Test-Time Scaling & Aggregation Papers

One study examines searching for compute-optimal architecture and model combinations in test-time scaling for a given task, with a compute budget. This work formulates dynamic test-time scaling as constructing a multi-LLM collaboration graph, where nodes represent chosen LLM models with assigned roles (fuser for parallel aggregation, assistant for sequential refinement).

Another paper studies parallel test-time scaling for long-horizon agentic tasks such as agentic search and deep research, where multiple rollouts are generated in parallel and aggregated into a final response.

AutoTTS is an environment-driven paradigm for automatic test-time scaling strategy discovery that shifts from hand-crafting individual branching and pruning heuristics to constructing discovery environments where agents search for effective allocation policies.

## NER & Structured Output Papers

For NER (Named Entity Recognition) with structured outputs, one approach aggregates calibrated predictions across all extracted entities as the final output. Named entity recognition is evolving from a sequence labeling task into a generative paradigm with LLMs, and using structured formats like inline bracketed or XML, open-source LLMs achieve competitive performance with parameter-efficient fine-tuning.

## Agentic Coding & Test-Time Scaling

A framework for agentic coding converts each rollout into a structured summary that preserves salient hypotheses, progress, and failure modes while discarding low-signal trace details.

These papers collectively address test-time scaling with structured output aggregation across various domains including NER, agent-based tasks, and coding applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99654cbf-e611-4af4-9dd6-9150d6902a61",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "cd222ff5-094c-4014-a7b9-945e4bb726d8",
  "sourceToolAssistantUUID": "99654cbf-e611-4af4-9dd6-9150d6902a61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-12T00:27:39.610Z_

<details><summary>↩ Tool result · `toolu_01KHvzsxg4ro7hwHTxgzNCpC`</summary>

```text
Web search results for query: "arxiv 2026 multiple sampling aggregation NER relation extraction structured"

Links: [{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers","url":"https://arxiv.org/html/2306.02051v3"},{"title":"Retrieval over Classification: Integrating Relation Semantics for Multimodal Relation Extraction","url":"https://arxiv.org/html/2509.21151v1"},{"title":"1 A Comprehensive Survey on Relation Extraction: Recent","url":"https://arxiv.org/pdf/2306.02051"},{"title":"TCMIIES: A Browser-Based LLM-Powered Intelligent Information Extraction System for Academic Literature","url":"https://arxiv.org/html/2605.07507"},{"title":"Structured Semantic Information Helps Retrieve Better Examples for In-Context Learning in Few-Shot Relation Extraction","url":"https://arxiv.org/html/2601.20803"},{"title":"Neural Metric Learning for Fast End-to-End Relation Extraction Tung Tran","url":"https://arxiv.org/pdf/1905.07458"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"Maximizing Relation Extraction Potential: A Data-Centric Study to Unveil Challenges and Opportunities","url":"https://arxiv.org/html/2409.04934v1"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys","url":"https://dl.acm.org/doi/full/10.1145/3674501"}]

The search returned several arxiv papers related to NER and relation extraction. Here are the most relevant results:

1. **"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers"** (arxiv 2306.02051) - This is a comprehensive survey covering relation extraction approaches, including graph-based methods with aggregation and inference networks, and discussion of both pipeline-based and joint extraction approaches.

2. **"Structured Semantic Information Helps Retrieve Better Examples for In-Context Learning in Few-Shot Relation Extraction"** (arxiv 2601.20803, January 2026) - This paper proposes an example selection framework that retrieves relation-faithful demonstrations using structured syntactic–semantic representations, promotes diversity through clustering, and complements retrieval with LLM-generated examples.

3. **"Retrieval over Classification: Integrating Relation Semantics for Multimodal Relation Extraction"** (arxiv 2509.21151, September 2025) - This paper addresses multimodal relation extraction with structured entity type and position information.

4. **"Large Language Models for Generative Information Extraction: A Survey"** (arxiv 2312.17617) - A survey covering NER and relation extraction techniques using language models.

5. **"TCMIIES: A Browser-Based LLM-Powered Intelligent Information Extraction System for Academic Literature"** (arxiv 2605.07507, May 2026) - This work shows that fine-tuned LLMs could jointly perform NER and RE on materials science texts, outputting structured JSON records from single sentences or entire paragraphs.

The search results show active research in combining NER and relation extraction with structured approaches and multiple sampling/aggregation strategies, particularly in recent 2026 papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54d09fc6-6fb9-4a6d-bbbc-60f55d01255c",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "e1377fc9-ac2a-4d5f-bcf1-e95e9e6098b4",
  "sourceToolAssistantUUID": "54d09fc6-6fb9-4a6d-bbbc-60f55d01255c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-12T00:27:40.462Z_

<details><summary>↩ Tool result · `toolu_01RpfZJvwSN1oerdEbaMVTfT`</summary>

```text
Web search results for query: "arxiv 2026 "adaptive consistency" OR "adaptive self-consistency" structured prediction information extraction"

Links: [{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970"},{"title":"[2601.02970] Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/abs/2601.02970"},{"title":"[2505.12642] Two out of Three (ToT): using self-consistency to make robust predictions","url":"https://arxiv.org/abs/2505.12642"},{"title":"Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://arxiv.org/pdf/2511.12309"},{"title":"[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://arxiv.org/abs/2203.11171"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview","url":"https://openreview.net/forum?id=1PL1NIMMrw"},{"title":"[2511.12309] Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://arxiv.org/abs/2511.12309"},{"title":"Consistency Models Made Easy","url":"https://arxiv.org/html/2406.14548v2"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/pdf/2502.06233"},{"title":"[2303.01469] Consistency Models","url":"https://arxiv.org/abs/2303.01469"}]

Based on the search results, I found a highly relevant paper that matches your query:

## Main Result

**Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning** (arXiv paper 2601.02970)

This paper, published in January 2026, is directly relevant to your search terms. The paper proposes Reliability-Aware Adaptive Self-Consistency (ReASC), which addresses adaptive sampling from response counting to evidence sufficiency, leveraging response-level confidence for principled information aggregation.

ReASC operates in two stages: a single-sample decision stage that resolves instances confidently answerable from a single response, and a reliability-aware accumulation stage that aggregates responses by jointly leveraging their frequency and confidence.

While this paper focuses on LLM reasoning rather than explicitly on structured prediction and information extraction tasks, it directly addresses the core concept of "adaptive self-consistency" mentioned in your search query. The paper may be relevant to those application domains as well, though the search results don't provide specific details about structured prediction or information extraction applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3109c9bb-6220-42ca-bf61-392d186b932a",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "92791a4e-f895-4f75-82cb-6584d7dbe31d",
  "sourceToolAssistantUUID": "3109c9bb-6220-42ca-bf61-392d186b932a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-12T00:27:45.672Z_

Let me do a final round of targeted searches on the most relevant leads and any papers I may have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92791a4e-f895-4f75-82cb-6584d7dbe31d",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj8WQ94GNGbMaWoMk57",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8220d3d7-7894-4c9b-a00d-61e4c6f4a1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WE6tchJCFvCRWzuUEWwDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1919,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 21669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 42 · 2026-05-12T00:27:46.696Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Se1AmLAw5V6pd3nsj64EAS`</summary>

```json
{
  "query": "arxiv 2602.10522 \"Consistency Meets Verification\" test-time scaling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8220d3d7-7894-4c9b-a00d-61e4c6f4a1e8",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj8WQ94GNGbMaWoMk57",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ce0d6fc-74b8-40f2-9bed-77b78277b38d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WE6tchJCFvCRWzuUEWwDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1919,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 21669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 43 · 2026-05-12T00:27:48.201Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GU46JiY6pYrirDqVWcm5Zf`</summary>

```json
{
  "query": "arxiv 2026 \"test-time compute\" OR \"test-time scaling\" \"entity extraction\" OR \"information extraction\" OR \"structured output\" majority voting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ce0d6fc-74b8-40f2-9bed-77b78277b38d",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj8WQ94GNGbMaWoMk57",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47284dcd-a934-4eb6-b691-2e00f8f01d50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WE6tchJCFvCRWzuUEWwDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1919,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 21669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 44 · 2026-05-12T00:27:48.481Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PhgwRHom3r2x7hpGePGgJp`</summary>

```json
{
  "query": "arxiv 2026 self-consistency LLM structured output NER event extraction confidence aggregation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47284dcd-a934-4eb6-b691-2e00f8f01d50",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj8WQ94GNGbMaWoMk57",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b923270-4952-4393-94ac-928ac91e355f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WE6tchJCFvCRWzuUEWwDh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1919,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 21669,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1961
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1919,
          "output_tokens": 219,
          "cache_read_input_tokens": 21669,
          "cache_creation_input_tokens": 1961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1961,
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

_source line 45 · 2026-05-12T00:27:53.653Z_

<details><summary>↩ Tool result · `toolu_01Se1AmLAw5V6pd3nsj64EAS`</summary>

```text
Web search results for query: "arxiv 2602.10522 "Consistency Meets Verification" test-time scaling"

Links: [{"title":"[2602.10522] Consistency Meets Verification: Enhancing Test Generation Quality in Large Language Models Without Ground-Truth Solutions","url":"https://arxiv.org/abs/2602.10522"},{"title":"[2602.10522v1] Consistency Meets Verification: Enhancing Test Generation Quality in Large Language Models Without Ground-Truth Solutions","url":"https://arxiv.org/abs/2602.10522v1"},{"title":"Consistency Meets Verification: Enhancing Test Generation Quality in Large Language Models Without Ground-Truth Solutions","url":"https://arxiv.org/html/2602.10522"},{"title":"Consistency Meets Verification: Enhancing Test Generation Quality in Large Language Models Without Ground-Truth Solutions - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260210522T/abstract"},{"title":"SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling","url":"https://arxiv.org/html/2501.19306v3"},{"title":"Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling","url":"https://arxiv.org/html/2505.11730v1"},{"title":"Agentic Test-Time Scaling for WebAgents","url":"https://arxiv.org/html/2602.12276.pdf"},{"title":"Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification","url":"https://arxiv.org/html/2510.06135"},{"title":"Benchmark Test-Time Scaling of General LLM Agents","url":"https://arxiv.org/html/2602.18998v1"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v1"}]

Based on the search results, I found the paper you requested: **arxiv 2602.10522 "Consistency Meets Verification: Enhancing Test Generation Quality in Large Language Models Without Ground-Truth Solutions"**

## Overview

This paper addresses the challenge that Large Language Models (LLMs) have advanced automated test generation, but existing methods often rely on ground-truth code for verification. The authors present ConVerTest, a novel two-stage pipeline for synthesizing reliable tests without requiring prior code implementations.

## Key Components

ConVerTest integrates three core strategies: (i) Self-Consistency (SC) to generate convergent test cases via majority voting; (ii) Chain-of-Verification (CoVe) for iterative, reasoning-guided code refinement; and (iii) a Dual Execution Agreement to cross-validate code and tests through consensus.

## Results

Experiments on BIGCODEBENCH and LESS BASIC PYTHON PROBLEMS (LBPP) benchmarks demonstrate that ConVerTest improves test validity, line coverage, and mutation scores by up to 39%, 28%, and 18% respectively over baselines.

The paper was submitted on February 11, 2026, with authors including Hamed Taherkhani, Alireza DaghighFarsoodeh, Mohammad Chowdhury, Hung Viet Pham, and Hadi Hemmati.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ce0d6fc-74b8-40f2-9bed-77b78277b38d",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "2308d5f4-7b86-4900-a073-c0e4a6588897",
  "sourceToolAssistantUUID": "8ce0d6fc-74b8-40f2-9bed-77b78277b38d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-12T00:27:57.100Z_

<details><summary>↩ Tool result · `toolu_01GU46JiY6pYrirDqVWcm5Zf`</summary>

```text
Web search results for query: "arxiv 2026 "test-time compute" OR "test-time scaling" "entity extraction" OR "information extraction" OR "structured output" majority voting"

Links: [{"title":"Scaling LLM Test-Time Compute Optimally can be More Efective …","url":"https://arxiv.org/pdf/2408.03314"},{"title":"Parallel Test-Time Scaling for Latent Reasoning Models","url":"https://arxiv.org/html/2510.07745v2"},{"title":"[2510.07745] Parallel Test-Time Scaling for Latent Reasoning Models","url":"https://arxiv.org/abs/2510.07745"},{"title":"[2604.16529] Scaling Test-Time Compute for Agentic Coding","url":"https://arxiv.org/abs/2604.16529"},{"title":"Latency and Token-Aware Test-Time Compute","url":"https://arxiv.org/html/2509.09864v1"},{"title":"[2502.05171] Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach","url":"https://arxiv.org/abs/2502.05171"},{"title":"Scaling Test-time Compute for LLM Agents","url":"https://arxiv.org/html/2506.12928v1"},{"title":"The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/html/2512.02008v1"},{"title":"[2502.12215] Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?","url":"https://arxiv.org/abs/2502.12215"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"}]

I've found several relevant papers from arXiv related to test-time compute and test-time scaling. Here are the most relevant results:

## Key Findings

1. **"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"** (2408.03314, February 2026) - This paper discusses using both a verifier and majority voting to select answers, finding that generating answers sequentially with a revision model narrowly outperforms generating them in parallel.

2. **"Parallel Test-Time Scaling for Latent Reasoning Models"** (2510.07745, January 2026) - Parallel test-time scaling (TTS) is a pivotal approach for enhancing large language models (LLMs), typically by sampling multiple token-based chains-of-thought in parallel and aggregating outcomes through voting or search.

3. **"Scaling Test-Time Compute for Agentic Coding"** (2604.16529, April 2026) - This paper proposes a test-time scaling framework for agentic coding based on compact representations of rollout trajectories, converting each rollout into a structured summary that preserves salient hypotheses, progress, and failure modes.

4. **"Scaling Test-time Compute for LLM Agents"** (2506.12928, June 2025) - This framework includes four key strategies: (1) Parallel Sampling with BoN, BoN-wise, Beam Search, and DVTS; (2) Sequential Revision with reflection models; (3) Verifiers and Result Merging Methods including majority voting; and (4) Diversifying Rollouts across heterogeneous agents.

5. **"The Art of Scaling Test-Time Compute for Large Language Models"** (2512.02008, December 2025) - This paper shows that the optimal TTS strategy by compute budget varies: shortest for low compute, beam search for medium, majority voting for high, and that no single strategy is optimal with optimality depending on compute budget.

The search results don't specifically focus on entity extraction or information extraction tasks, but rather focus on mathematical reasoning and general LLM performance. You may want to refine the search if you're looking for papers specifically addressing structured output or information extraction with test-time scaling approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47284dcd-a934-4eb6-b691-2e00f8f01d50",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "ad8d2a61-f2c9-4e1d-b5e2-130195896fd3",
  "sourceToolAssistantUUID": "47284dcd-a934-4eb6-b691-2e00f8f01d50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-12T00:27:58.173Z_

<details><summary>↩ Tool result · `toolu_01PhgwRHom3r2x7hpGePGgJp`</summary>

```text
Web search results for query: "arxiv 2026 self-consistency LLM structured output NER event extraction confidence aggregation"

Links: [{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"Illusions of Confidence? Diagnosing LLM Truthfulness via Neighborhood Consistency","url":"https://arxiv.org/html/2601.05905"},{"title":"can llms express their uncertainty? an empirical evaluation ...","url":"https://arxiv.org/pdf/2306.13063"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/pdf/2502.06233"},{"title":"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction","url":"https://arxiv.org/html/2402.13364v1"},{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework","url":"https://arxiv.org/html/2503.02863v1"},{"title":"Uncertainty-Aware Structured Data Extraction from Full CMR Reports via Distilled LLMs","url":"https://arxiv.org/html/2605.08045"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2603.08999v2"},{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt","url":"https://arxiv.org/pdf/2503.02863v1"}]

Based on the search results, here are the key findings related to your query about self-consistency, LLM structured output, NER, event extraction, and confidence aggregation:

## Recent 2026 Advances in Self-Consistency with Confidence

Reliability-Aware Adaptive Self-Consistency (ReASC) addresses adaptive sampling limitations by reframing it from response counting to evidence sufficiency, leveraging response-level confidence for principled information aggregation. ReASC operates in two stages: a single-sample decision stage that resolves instances confidently answerable from a single response, and a reliability-aware accumulation stage that aggregates responses by jointly leveraging their frequency and confidence.

Another confidence-aware framework analyzes a single completed reasoning trajectory to adaptively select between single-path and multi-path reasoning.

## Confidence Aggregation Methods

Confidence-Informed Self-Consistency (CISC) replaces uniform voting with model-derived scalar weights, obtained via response probability, verbal confidence, or tokenwise probability, enabling the correct answer to dominate with fewer samples (cost reductions 40–50%).

SteeringConf comprises three components: a confidence steering mechanism that steers LLM confidence in specified directions through tailored prompts, an aggregation module that aggregates multiple steered confidences to produce a final output based on consistency of multiple steered answers and confidences, and a selection criteria to choose the steered answer with best confidence.

## Structured Output for Information Extraction

The Generate and Organize (G&O) methodology enhances LLM capability in structured zero-shot IE tasks for NER and RE by dividing generation into two components: generating IE responses in free-form natural language, followed by structuring these responses into a predefined format.

## Uncertainty-Aware Structured Extraction

CMR-EXTR couples extraction with per-field uncertainty that blends three complementary signals: distribution plausibility under reference ranges, stability across controlled stochastic generations, and consistency with physiologic constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b923270-4952-4393-94ac-928ac91e355f",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "6498caaf-23cc-4a43-8bdd-f2bac5b25529",
  "sourceToolAssistantUUID": "4b923270-4952-4393-94ac-928ac91e355f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-12T00:28:03.851Z_

Let me chase down a few more critical leads -- the "Learning When to Sample" paper and the G&O methodology paper, plus check for any very recent (April-May 2026) work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6498caaf-23cc-4a43-8bdd-f2bac5b25529",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj9p5nVonYLqypoP4kG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e3cb6e2-26b3-48a5-a03d-a279b135c9d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013smn3UkJMgiRAh2RZKg8Hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4969,
      "cache_read_input_tokens": 23630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4969,
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

_source line 49 · 2026-05-12T00:28:04.332Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011hdZbqK2tqmVWMQf4iXvgB`</summary>

```json
{
  "query": "arxiv 2603.08999 \"Learning When to Sample\" confidence-aware self-consistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e3cb6e2-26b3-48a5-a03d-a279b135c9d3",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj9p5nVonYLqypoP4kG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "301210e7-d84d-4c5a-997e-79168eb17b04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013smn3UkJMgiRAh2RZKg8Hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4969,
      "cache_read_input_tokens": 23630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4969,
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

_source line 50 · 2026-05-12T00:28:04.863Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XLJatFNxGwG4xa2brrQWJb`</summary>

```json
{
  "query": "arxiv \"Generate and Organize\" G&O structured zero-shot NER RE information extraction LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "301210e7-d84d-4c5a-997e-79168eb17b04",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj9p5nVonYLqypoP4kG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c24cdc0-f84c-460b-80bd-4ff278d7cb2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013smn3UkJMgiRAh2RZKg8Hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4969,
      "cache_read_input_tokens": 23630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4969,
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

_source line 51 · 2026-05-12T00:28:05.261Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Em4tFs79CNvzcbYgc7ktHo`</summary>

```json
{
  "query": "arxiv April May 2026 self-consistency structured prediction entity extraction scaling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c24cdc0-f84c-460b-80bd-4ff278d7cb2f",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011Cawj9p5nVonYLqypoP4kG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e033bb23-1b69-4079-ad0a-a65a76f4fb62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013smn3UkJMgiRAh2RZKg8Hu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4969,
      "cache_read_input_tokens": 23630,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4969
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 23630,
          "cache_creation_input_tokens": 4969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4969,
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

_source line 52 · 2026-05-12T00:28:11.692Z_

<details><summary>↩ Tool result · `toolu_011hdZbqK2tqmVWMQf4iXvgB`</summary>

```text
Web search results for query: "arxiv 2603.08999 "Learning When to Sample" confidence-aware self-consistency"

Links: [{"title":"[2603.08999] Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2603.08999"},{"title":"Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2603.08999"},{"title":"Learning When to Sample: Confidence-Aware Self-Consistency for","url":"https://arxiv.org/pdf/2603.08999"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/html/2502.06233v1"},{"title":"Self-Training Large Language Models with Confident Reasoning","url":"https://arxiv.org/html/2505.17454v1"},{"title":"Confidence Improves Self-Consistency in LLMs | alphaXiv","url":"https://www.alphaxiv.org/abs/2502.06233"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"Confidence Improves Self-Consistency in LLMs | by Ema Ilic | Medium","url":"https://medium.com/@ema.ilic9/confidence-improves-self-consistency-in-llms-313e80467168"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview","url":"https://openreview.net/forum?id=1PL1NIMMrw"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"}]

Based on the search results, here's information about the paper arxiv 2603.08999:

## Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning

This paper was submitted on March 9, 2026 with a revision on March 17, 2026 and was authored by Juming Xiong, Kevin Guo, Congning Ni, Chao Yan, Katherine Brown, Avinash Baidya, Xiang Gao, Bradley Malin, and Zhijun Yin.

### Problem Statement

Large language models (LLMs) achieve strong reasoning performance through chain-of-thought (CoT) reasoning, yet often generate unnecessarily long reasoning paths that incur high inference cost. Recent self-consistency-based approaches further improve accuracy but require sampling and aggregating multiple reasoning trajectories, leading to substantial additional computational overhead.

### Solution

The paper introduces a confidence-aware decision framework that analyzes a single completed reasoning trajectory to adaptively select between single-path and multi-path reasoning. The framework is trained using sentence-level numeric and linguistic features extracted from intermediate reasoning states in the MedQA dataset and generalizes effectively to MathQA, MedMCQA, and MMLU without additional fine-tuning.

The paper addresses the efficiency problem in LLM reasoning by providing a more targeted approach to deciding when multiple sampling paths are actually needed versus when a single reasoning path is sufficient.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "301210e7-d84d-4c5a-997e-79168eb17b04",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "a57ea9fb-3c6b-404e-8da7-2a63f38811a2",
  "sourceToolAssistantUUID": "301210e7-d84d-4c5a-997e-79168eb17b04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-12T00:28:11.700Z_

<details><summary>↩ Tool result · `toolu_01XLJatFNxGwG4xa2brrQWJb`</summary>

```text
Web search results for query: "arxiv "Generate and Organize" G&O structured zero-shot NER RE information extraction LLM"

Links: [{"title":"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction","url":"https://arxiv.org/html/2402.13364v1"},{"title":"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction","url":"https://arxiv.org/html/2506.00649"},{"title":"[2402.13364] A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction","url":"https://arxiv.org/abs/2402.13364"},{"title":"1 Zero-Shot Document-Level Biomedical Relation Extraction via","url":"https://arxiv.org/pdf/2505.01077"},{"title":"[2505.01077] Zero-Shot Document-Level Biomedical Relation Extraction via Scenario-based Prompt Design in Two-Stage with LLM","url":"https://arxiv.org/abs/2505.01077"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"llmNER: (Zero|Few)-Shot Named Entity Recognition, Exploiting the Power of Large Language Models","url":"https://arxiv.org/html/2406.04528v1"},{"title":"[2310.05028] Revisiting Large Language Models as Zero-shot Relation Extractors","url":"https://arxiv.org/abs/2310.05028"},{"title":"Unleashing the Power of Large Language Models in Zero-shot Relation Extraction via Self-Prompting","url":"https://arxiv.org/html/2410.01154v1"},{"title":"[2410.01154] Unleashing the Power of Large Language Models in Zero-shot Relation Extraction via Self-Prompting","url":"https://arxiv.org/abs/2410.01154"}]

I found the paper you're looking for! Here are the search results:

## Main Result

The paper introduces "Generate and Organize" (G&O), a methodology designed to enhance the capability of LLMs in performing structured zero-shot IE tasks, with a focus on NER and RE.

## How G&O Works

The approach divides the generation into two distinct components: 1) generating IE responses in a free-form natural language format; followed by 2) structuring these responses into a predefined format. Furthermore, it incorporates a clean-up component to eliminate any potential noise from the free-form responses before structuring.

Different from conventional prompting approaches, G&O separates the identification and formatting steps into two stages, which allows the model to focus on each step independently and facilitates the generation of organized results.

## Performance Results

Through extensive experimentation, the method boosts zero-shot IE performance across various LLMs. Tested under the zero-shot IE settings with GPT 3.5, this simple adjustment brings significant performance gains, demonstrating the effectiveness of G&O.

**Paper Details:**
- **Title:** A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction
- **ArXiv ID:** 2402.13364
- **Published:** February 20, 2024
- **URL:** https://arxiv.org/abs/2402.13364


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c24cdc0-f84c-460b-80bd-4ff278d7cb2f",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "6462b222-ea50-449d-a08b-721641dd0fa4",
  "sourceToolAssistantUUID": "7c24cdc0-f84c-460b-80bd-4ff278d7cb2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-12T00:28:14.734Z_

<details><summary>↩ Tool result · `toolu_01Em4tFs79CNvzcbYgc7ktHo`</summary>

```text
Web search results for query: "arxiv April May 2026 self-consistency structured prediction entity extraction scaling"

Links: [{"title":"Learning to Extract Structured Entities Using Language Models","url":"https://arxiv.org/html/2402.04437"},{"title":"[1608.00612v1] Structured prediction models for RNN based sequence labeling in clinical text","url":"https://arxiv.org/abs/1608.00612v1"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/html/2305.13971v6"},{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"},{"title":"[2502.06233] Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/abs/2502.06233"},{"title":"Scaling Self-Supervised and Cross-Modal Pretraining for Volumetric CT Transformers","url":"https://arxiv.org/html/2511.17209v1"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=875&show=2000"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/new?skip=25&show=1000"},{"title":"Predicting Program Correctness By Ensemble Semantic Entropy","url":"https://arxiv.org/html/2603.27098v1"}]

I found search results related to your query. Here's what the web search returned:

The search results include several relevant papers on self-consistency, structured prediction, and entity extraction:

A paper on "Confidence Improves Self-Consistency in LLMs" discusses how self-consistency decoding enhances LLMs' performance on reasoning tasks by sampling diverse reasoning paths and selecting the most frequent answer, though it is computationally expensive. The paper introduces Confidence-Informed Self-Consistency (CISC), which performs a weighted majority vote based on confidence scores obtained directly from the model to identify the correct answer with a significantly smaller sample size.

For structured prediction and entity extraction, one paper presents the MuSEE model, which consistently outperforms other baselines on entity extraction tasks, achieving high scores on various datasets like REBEL, NYT, and CoNLL04. Another paper notes that language models are not specifically designed for structured prediction tasks where only a small subset of the output space is valid, and structured prediction tasks present unique challenges because constrained output spaces demand both structural coherence and compliance with a predefined vocabulary.

Additionally, recent work discusses Semantic Entropy (SE) as a mainstream estimation technique that evaluates uncertainty by measuring entropy across clusters of semantically equivalent outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e033bb23-1b69-4079-ad0a-a65a76f4fb62",
  "isSidechain": true,
  "promptId": "ef462ecf-d496-411b-bcd4-dcba8917349f",
  "agentId": "a9c05864599146c9a",
  "type": "user",
  "uuid": "dfa34d7e-26b2-41a5-8b57-a1fab7c31505",
  "sourceToolAssistantUUID": "e033bb23-1b69-4079-ad0a-a65a76f4fb62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-12T00:29:00.059Z_

I now have a comprehensive picture. Here is my report.

---

## Concurrent Work Search Results: Adaptive Test-Time Scaling for Structured Prediction / Information Extraction (Feb-May 2026)

### Key Question Answer

**No paper from February-May 2026 was found that directly applies test-time self-consistency scaling to information extraction (NER, RE, event extraction) with structural similarity-based aggregation.** This appears to remain an open gap in the literature. However, several papers represent closely related or partially overlapping concurrent work that a reviewer could reasonably flag.

---

### Most Relevant Concurrent Paper

**1. "Self-Consistent Structured Generation (SCSG) for Dimensional Aspect-Based Sentiment Analysis using Large Language Models"**
- Authors: Nils Constantin Hellwig et al.
- Date: March 2, 2026
- ArXiv: [2603.01788](https://arxiv.org/abs/2603.01788)
- Venue: SemEval-2026 Task 3
- Relevance: **HIGH.** This paper applies self-consistency majority voting to structured generation (aspect-sentiment tuple extraction). It runs a LoRA-adapted LLM multiple times per instance, retains tuples appearing in at least half of runs, and aggregates by averaging numerical values. Uses vLLM PagedAttention for efficiency. Tests 5/10/15 executions with majority voting across 6 languages. This is the closest concurrent work -- it applies self-consistency to a structured extraction task (ABSA), though it targets sentiment tuples rather than IE tasks (NER/RE/EE) and uses simple majority voting rather than structural similarity-based aggregation.

---

### Closely Related Work on Adaptive/Efficient Self-Consistency (2026)

**2. "Reliability-Aware Adaptive Self-Consistency (ReASC)"**
- Date: January 2026
- ArXiv: [2601.02970](https://arxiv.org/abs/2601.02970)
- Relevance: **MODERATE.** Proposes adaptive sampling that shifts from response counting to evidence sufficiency, using response-level confidence for principled aggregation. Two-stage: single-sample decision stage + reliability-aware accumulation. Focuses on reasoning tasks, not IE/structured prediction, but the adaptive sampling methodology is directly relevant.

**3. "Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning"**
- Authors: Juming Xiong, Kevin Guo, et al.
- Date: March 9, 2026
- ArXiv: [2603.08999](https://arxiv.org/abs/2603.08999)
- Relevance: **MODERATE.** Introduces a confidence-aware decision framework that analyzes a single reasoning trajectory to decide whether multi-path sampling is needed. Trained on MedQA, generalizes to MathQA/MedMCQA/MMLU. Addresses the same efficiency concern (when to sample more) but for reasoning, not structured extraction.

**4. "Confidence Improves Self-Consistency in LLMs" (CISC)**
- Date: February 2026
- ArXiv: [2502.06233](https://arxiv.org/abs/2502.06233)
- Relevance: **MODERATE.** Replaces uniform voting with model-derived scalar weights (response probability, verbal confidence, tokenwise probability). Reports 40-50% cost reductions. Relevant methodology for weighted aggregation, though applied to reasoning rather than structured outputs.

**5. "Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search"**
- Date: February 2026
- ArXiv: [2602.01485](https://arxiv.org/abs/2602.01485)
- Relevance: **LOW-MODERATE.** Introduces Scaling-Law Guided (SLG) Search for dynamic compute allocation at test time. General TTS methodology.

---

### Related Work on Structured Outputs / Information Extraction (2026)

**6. "Uncertainty-Aware Structured Data Extraction from Full CMR Reports via Distilled LLMs"**
- Date: May 2026
- ArXiv: [2605.08045](https://arxiv.org/abs/2605.08045)
- Relevance: **MODERATE.** Couples structured extraction with per-field uncertainty that blends distribution plausibility, stability across stochastic generations, and consistency with constraints. This touches on uncertainty-aware structured extraction with multiple generations but in a medical domain-specific context.

**7. "A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction" (G&O)**
- Date: February 2024 (predates your window)
- ArXiv: [2402.13364](https://arxiv.org/abs/2402.13364)
- Relevance: **BACKGROUND.** Two-stage generate-then-organize for zero-shot NER/RE. Not self-consistency based but relevant prior work on structured IE output quality.

---

### Related Work on Aggregation / Voting Methods (2025-2026)

**8. "Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information"**
- Date: October 2025
- ArXiv: [2510.01499](https://arxiv.org/abs/2510.01499)
- Relevance: **LOW-MODERATE.** Proposes Optimal Weight and Inverse Surprising Popularity algorithms for multi-agent aggregation that go beyond simple majority voting. Relevant methodology for aggregation, though not applied to structured prediction.

**9. "Agentic Aggregation for Parallel Scaling of Long-Horizon Agentic Tasks"**
- Date: April 2026
- ArXiv: [2604.11753](https://arxiv.org/abs/2604.11753)
- Relevance: **LOW.** Parallel test-time scaling with aggregation for agentic tasks.

---

### Summary Assessment

The research landscape shows:

1. **Self-consistency for structured generation** is emerging (the SCSG/SemEval paper is the clearest example) but remains focused on simpler structured tasks (sentiment tuples) rather than full IE pipelines.

2. **Adaptive/efficient self-consistency** is a very active area in early 2026 (ReASC, CISC, Learning When to Sample), but all focus on reasoning tasks (math, QA), not structured prediction.

3. **Test-time scaling** research in 2026 has expanded to coding and agentic tasks but has not yet been applied systematically to information extraction.

4. **The specific combination** your proposal targets -- self-consistency with structural similarity-based aggregation for NER/RE/EE -- appears to be novel as of this search. The SCSG paper (2603.01788) is the closest concurrent work and should be discussed in a related work section, but it differs in task (ABSA vs. IE), aggregation method (simple majority voting vs. structural similarity), and does not address adaptive/confidence-gated sampling.

Sources:
- [SCSG - Self-Consistent Structured Generation (SemEval-2026)](https://arxiv.org/abs/2603.01788)
- [ReASC - Reliability-Aware Adaptive Self-Consistency](https://arxiv.org/abs/2601.02970)
- [Learning When to Sample](https://arxiv.org/abs/2603.08999)
- [CISC - Confidence Improves Self-Consistency](https://arxiv.org/abs/2502.06233)
- [Reward Tail-Guided Search for TTS](https://arxiv.org/abs/2602.01485)
- [Uncertainty-Aware Structured Data Extraction](https://arxiv.org/abs/2605.08045)
- [G&O for Structured IE](https://arxiv.org/abs/2402.13364)
- [Beyond Majority Voting](https://arxiv.org/abs/2510.01499)
- [Agentic Aggregation for Parallel Scaling](https://arxiv.org/abs/2604.11753)
- [ConVerTest - Consistency Meets Verification](https://arxiv.org/abs/2602.10522)
- [Scaling Test-Time Compute for Agentic Coding](https://arxiv.org/abs/2604.16529)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfa34d7e-26b2-41a5-8b57-a1fab7c31505",
  "isSidechain": true,
  "agentId": "a9c05864599146c9a",
  "requestId": "req_011CawjB2vUqkRDxAum3ogxf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5d158b4-11a9-4aa5-a0e5-086814263061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b638df9e-f96c-4b89-a7d5-8351d6634c53",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nsc9KMyiJd3PSCgPgqj1v4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2735,
      "cache_read_input_tokens": 28599,
      "output_tokens": 2022,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2735
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2022,
          "cache_read_input_tokens": 28599,
          "cache_creation_input_tokens": 2735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2735,
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
