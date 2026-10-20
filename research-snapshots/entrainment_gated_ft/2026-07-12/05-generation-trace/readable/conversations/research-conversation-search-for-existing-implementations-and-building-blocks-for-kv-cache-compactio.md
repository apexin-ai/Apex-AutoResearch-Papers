# Research conversation: Search for existing implementations and building blocks for KV cache compaction in LLM agent inference. Use WebSearch fo

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 1
- **Tool calls:** 34
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a1745bfe9686c9b9a.jsonl`
- **Structured JSON:** [`ab702baec9e82fe0f468.json`](../../sessions/ab/ab702baec9e82fe0f468.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

77 recorded events

### User

_source line 1 · 2026-05-11T21:23:54.925Z_

Search for existing implementations and building blocks for KV cache compaction in LLM agent inference. Use WebSearch for:

1. "github.com attention matching KV cache compaction"
2. "github.com KV cache compression LLM agent"
3. "github.com incremental KV compaction transformer"
4. "github.com vllm KV cache management agent"
5. "github.com sglang KV cache compaction"
6. "vllm prefix caching KV reuse agent" - to understand existing KV management in serving frameworks
7. "sglang radix attention KV cache" - to understand existing multi-turn KV management
8. Search for any open-source implementations of the papers: Attention Matching, CacheTTL, PBKV, CacheClip

For each result, report: repo URL, stars, what it implements, and whether it could serve as a building block for incremental KV compaction between agent tool calls. Also note the serving framework landscape (vLLM, SGLang, TensorRT-LLM) and how they currently handle multi-turn KV caching.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "346301d1-1fc3-406a-bfc4-b95cbb092cf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T21:23:54.927Z_

```json
{
  "parentUuid": "346301d1-1fc3-406a-bfc4-b95cbb092cf3",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
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
  "uuid": "71144968-7935-49f3-adf9-85525f83c35a",
  "timestamp": "2026-05-11T21:23:54.927Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T21:23:57.085Z_



I'll conduct a comprehensive search across all these queries. Let me start by loading the WebSearch tool and then running the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71144968-7935-49f3-adf9-85525f83c35a",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV7mXK67gkLqph221S3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25f9f298-01a0-46c3-876a-5c3dc335e245",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4EsaudCP8ufYmwFvYRWJh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 786,
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

_source line 4 · 2026-05-11T21:23:57.680Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KXPDbksyJk2V5vqvDsYXTU`</summary>

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
  "parentUuid": "25f9f298-01a0-46c3-876a-5c3dc335e245",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV7mXK67gkLqph221S3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61c6ea28-d74b-48f1-9821-5f62d96cb066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4EsaudCP8ufYmwFvYRWJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 7304,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 786
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 107,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 786,
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

_source line 5 · 2026-05-11T21:23:57.685Z_

<details><summary>↩ Tool result · `toolu_01KXPDbksyJk2V5vqvDsYXTU`</summary>

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
  "parentUuid": "61c6ea28-d74b-48f1-9821-5f62d96cb066",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "c55e2fce-0e3d-4dfd-8113-3b7f84c575b1",
  "sourceToolAssistantUUID": "61c6ea28-d74b-48f1-9821-5f62d96cb066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T21:24:05.796Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c55e2fce-0e3d-4dfd-8113-3b7f84c575b1",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV7yfpD11Z9c9c9acRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24e7d995-8796-487a-9aa8-effe34737614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136C4cDpuEUEdu48zZ6393L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 7 · 2026-05-11T21:24:06.374Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WdyzxjCTBHiAcRasFTPQtM`</summary>

```json
{
  "query": "github.com attention matching KV cache compaction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24e7d995-8796-487a-9aa8-effe34737614",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV7yfpD11Z9c9c9acRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0239134-3789-4a61-b2a1-9fe9a5f38e8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136C4cDpuEUEdu48zZ6393L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 8 · 2026-05-11T21:24:06.722Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SYS61kGb2Zr7L9c5mDbbFQ`</summary>

```json
{
  "query": "github.com KV cache compression LLM agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0239134-3789-4a61-b2a1-9fe9a5f38e8c",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV7yfpD11Z9c9c9acRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a3c9969-4c65-4868-b5ba-ad0d1e946ffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136C4cDpuEUEdu48zZ6393L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 9 · 2026-05-11T21:24:07.174Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BcqS9g7GyipCAZJNJEYUkU`</summary>

```json
{
  "query": "github.com incremental KV compaction transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a3c9969-4c65-4868-b5ba-ad0d1e946ffd",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV7yfpD11Z9c9c9acRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19a5fd50-d5e0-41cf-9581-7cb130fd59d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136C4cDpuEUEdu48zZ6393L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 10 · 2026-05-11T21:24:07.811Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PyFufdgtimUxvJWxEXauSc`</summary>

```json
{
  "query": "github.com vllm KV cache management agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19a5fd50-d5e0-41cf-9581-7cb130fd59d1",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV7yfpD11Z9c9c9acRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41e1eaf6-df6c-4b5f-9369-a40f3c1100dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136C4cDpuEUEdu48zZ6393L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 11 · 2026-05-11T21:24:08.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NE1qmQbzSuTYTv4jRQtv3P`</summary>

```json
{
  "query": "github.com sglang KV cache compaction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41e1eaf6-df6c-4b5f-9369-a40f3c1100dd",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV7yfpD11Z9c9c9acRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86d941a0-7a61-4fa9-abdb-12357350ac12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136C4cDpuEUEdu48zZ6393L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 12 · 2026-05-11T21:24:08.624Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YKBurHNqZMNPfTodBLMBWb`</summary>

```json
{
  "query": "vllm prefix caching KV reuse agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86d941a0-7a61-4fa9-abdb-12357350ac12",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV7yfpD11Z9c9c9acRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "909e5a18-b37f-4855-bf1b-69fd82df49e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136C4cDpuEUEdu48zZ6393L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 13 · 2026-05-11T21:24:09.063Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MsPXN4rj8AvtKVowYwTUd1`</summary>

```json
{
  "query": "sglang radix attention KV cache multi-turn"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "909e5a18-b37f-4855-bf1b-69fd82df49e8",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV7yfpD11Z9c9c9acRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8586554-ac2c-47ca-8156-09c8687a1952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136C4cDpuEUEdu48zZ6393L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 14 · 2026-05-11T21:24:09.781Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S1S1vSTaZ5DKcAt3gkpguu`</summary>

```json
{
  "query": "github Attention Matching KV cache paper implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8586554-ac2c-47ca-8156-09c8687a1952",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV7yfpD11Z9c9c9acRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3175955d-b112-4aa6-80b7-d84e121ebc5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136C4cDpuEUEdu48zZ6393L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8090,
      "output_tokens": 387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1916
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 387,
          "cache_read_input_tokens": 8090,
          "cache_creation_input_tokens": 1916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1916,
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

_source line 15 · 2026-05-11T21:24:12.769Z_

<details><summary>↩ Tool result · `toolu_01WdyzxjCTBHiAcRasFTPQtM`</summary>

```text
Web search results for query: "github.com attention matching KV cache compaction"

Links: [{"title":"GitHub - adamzweiger/compaction: Algorithms for latent compaction · GitHub","url":"https://github.com/adamzweiger/compaction"},{"title":"Research: Implement \"Fast KV Compaction via Attention Matching\" for extreme VRAM savings · Issue #20037 · ggml-org/llama.cpp","url":"https://github.com/ggml-org/llama.cpp/issues/20037"},{"title":"[2602.16284] Fast KV Compaction via Attention Matching","url":"https://arxiv.org/abs/2602.16284"},{"title":"Fast KV Compaction via Attention Matching","url":"https://arxiv.org/pdf/2602.16284"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"TriAttention | Efficient KV Cache Compression for Long-Context Reasoning","url":"https://weianmao.github.io/tri-attention-project-page/"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"Fast KV Compaction via Attention Matching | Hacker News","url":"https://news.ycombinator.com/item?id=47083882"},{"title":"[2602.16284v1] Fast KV Compaction via Attention Matching","url":"https://arxiv.org/abs/2602.16284v1"},{"title":"Fast KV Compaction via Attention Matching | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.16284"}]

Based on the search results, here's what I found about attention matching KV cache compaction:

## Main Repository

The primary GitHub repository is adamzweiger/compaction, which contains code for Fast KV Compaction via Attention Matching. Attention Matching compacts a KV cache in latent space by constructing a smaller set of keys and values that reproduce the original attention behavior.

## Technical Approach

This approach performs fast context compaction in latent space through Attention Matching, which constructs compact keys and values to reproduce attention outputs and preserve attention mass at a per-KV-head level.

The method compresses the K and V matrices into much smaller representations that stay in the latent space, and the model directly queries against these compact matrices during generation without needing to decompress them.

## Performance

Applying AM-OMP can achieve up to approximately 200× total compaction when combined with summarization, and the attention-matching methods form a Pareto frontier for speed-quality tradeoff, outperforming prior token-selection baselines.

## Research Publication

The work was published by Adam Zweiger, Xinghong Fu, Han Guo, and Yoon Kim in 2026 (arXiv paper 2602.16284).

You can find the official repository at https://github.com/adamzweiger/compaction and the paper on arXiv at https://arxiv.org/abs/2602.16284.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0239134-3789-4a61-b2a1-9fe9a5f38e8c",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "d20bb7a7-619b-464b-a3c7-a777762bc9d1",
  "sourceToolAssistantUUID": "a0239134-3789-4a61-b2a1-9fe9a5f38e8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T21:24:15.276Z_

<details><summary>↩ Tool result · `toolu_01SYS61kGb2Zr7L9c5mDbbFQ`</summary>

```text
Web search results for query: "github.com KV cache compression LLM agent"

Links: [{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"GitHub - IsaacRe/vllm-kvcompress: KV cache compression for high-throughput LLM inference · GitHub","url":"https://github.com/IsaacRe/vllm-kvcompress"},{"title":"GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub","url":"https://github.com/LMCache/LMCache"},{"title":"GitHub - aivrar/multi-turboquant: Unified KV cache compression for LLM inference — TurboQuant, IsoQuant, PlanarQuant, TriAttention. 10 methods, GPU-validated, multi-GPU planner. Compress KV cache 5-80x to run bigger models, longer context, more agents on your GPU.","url":"https://github.com/aivrar/multi-turboquant"},{"title":"GitHub - NVlabs/RocketKV: [ICML 2025] RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression · GitHub","url":"https://github.com/NVlabs/RocketKV"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"},{"title":"GitHub - Zefan-Cai/Awesome-LLM-KV-Cache: Awesome-LLM-KV-Cache: A curated list of 📙Awesome LLM KV Cache Papers with Codes.","url":"https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache"},{"title":"GitHub - opengear-project/GEAR: GEAR: An Efficient KV Cache Compression Recipefor Near-Lossless Generative Inference of LLM · GitHub","url":"https://github.com/opengear-project/GEAR"},{"title":"GitHub - SharpAI/SwiftLM: ⚡ Native MLX Swift LLM inference server for Apple Silicon. OpenAI-compatible API, SSD streaming for 100B+ MoE models, TurboQuant KV cache compression, MACOS + iOS iPhone app.","url":"https://github.com/SharpAI/SwiftLM"},{"title":"GitHub - lloydchang/NVIDIA-kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/lloydchang/NVIDIA-kvpress"}]

I found several relevant GitHub repositories for KV cache compression in LLMs. Here are the key projects:

## Major KV Cache Compression Projects

**1. NVIDIA KVPress**
KVPress implements multiple KV cache compression methods and benchmarks using transformers, aiming to simplify the development of new methods for researchers and developers in this field. The repository includes various compression techniques like KVzipPress, KVComposePress, PyramidKVPress, and others.

**2. vLLM KVCompress**
This is a KV cache compression implementation for high-throughput LLM inference, built on top of vLLM and featuring continual compression capabilities.

**3. LMCache**
LMCache is an LLM serving engine extension to reduce TTFT and increase throughput, especially under long-context scenarios, by storing the KV caches of reusable texts all over the datacenter (including GPU, CPU, Disk and even S3) with a wide range of acceleration techniques.

**4. Multi-TurboQuant**
This unified KV cache compression toolkit provides 10 methods, GPU-validated with a multi-GPU planner, and can compress KV cache 5-80x to run bigger models, longer context, and more agents on your GPU.

**5. RocketKV**
RocketKV provides a compression ratio of up to 400×, end-to-end speedup of up to 3.7× as well as peak memory reduction of up to 32.6% in the decode phase on an NVIDIA A100 GPU compared to the full KV cache baseline, while achieving negligible accuracy loss.

**6. Curated Collections**
The Awesome-KV-Cache-Management repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links.

These projects offer various approaches to reduce the memory overhead of KV caches, which is critical for deploying long-context LLMs efficiently.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a3c9969-4c65-4868-b5ba-ad0d1e946ffd",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "372d4b74-9817-42d6-b816-e27ceaa19755",
  "sourceToolAssistantUUID": "1a3c9969-4c65-4868-b5ba-ad0d1e946ffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-11T21:24:15.724Z_

<details><summary>↩ Tool result · `toolu_01BcqS9g7GyipCAZJNJEYUkU`</summary>

```text
Web search results for query: "github.com incremental KV compaction transformer"

Links: [{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"Research: Implement \"Fast KV Compaction via Attention Matching\" for extreme VRAM savings · Issue #20037 · ggml-org/llama.cpp","url":"https://github.com/ggml-org/llama.cpp/issues/20037"},{"title":"GitHub - adamzweiger/compaction: Algorithms for latent compaction · GitHub","url":"https://github.com/adamzweiger/compaction"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"[RFC]: Support KV Cache Compaction · Issue #10646 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/10646"},{"title":"Fast KV Compaction via Attention Matching","url":"https://arxiv.org/pdf/2602.16284"},{"title":"blog/kv-cache-quantization.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/kv-cache-quantization.md"},{"title":"GitHub - Kaleemullahqasim/KV-Direct: KV-Direct: Bounded-Memory Transformer Inference via Residual Stream Checkpointing · GitHub","url":"https://github.com/Kaleemullahqasim/KV-Direct"},{"title":"GitHub - vllm-project/llm-compressor: Transformers-compatible library for applying various compression algorithms to LLMs for optimized deployment with vLLM · GitHub","url":"https://github.com/vllm-project/llm-compressor"},{"title":"Effective one-shot KV context compaction","url":"https://www.emergentmind.com/open-problems/effective-one-shot-kv-context-compaction"}]

Based on the search results, here are the key findings about incremental KV compaction for transformers:

## Key Projects and Resources

**Primary Implementation:**
Fast KV Compaction via Attention Matching provides code for compacting a KV cache in latent space by constructing a smaller set of keys and values that reproduce the original attention behavior. This is available at https://github.com/adamzweiger/compaction.

**Comprehensive Frameworks:**

1. **NVIDIA KVPress** (https://github.com/NVIDIA/kvpress): KVPress provides a set of "presses" that compress the KV cache during the prefilling-phase. It includes multiple compression methods like CompactorPress, CURPress, and DecodingPress for incremental compression during token generation.

2. **vLLM LLM Compressor** (https://github.com/vllm-project/llm-compressor): Offers a comprehensive set of quantization algorithms and transforms for weight, activation, KV Cache, and attention quantization with seamless integration with Hugging Face models.

3. **Awesome KV Cache Compression** (https://github.com/October2001/Awesome-KV-Cache-Compression): Implements multiple KV cache pruning methods and benchmarks using transformers.

## Key Concepts

KV cache compaction (i.e., token dropping) can significantly reduce memory footprint in llm serving, especially for long generation and large batch size workloads. DecodingPress compresses the KV cache periodically during token generation, optionally maintaining a buffer of recent hidden states with configurable compression intervals and target cache sizes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19a5fd50-d5e0-41cf-9581-7cb130fd59d1",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "ee5dc35c-c6be-4645-9bac-e2ab702ef4dd",
  "sourceToolAssistantUUID": "19a5fd50-d5e0-41cf-9581-7cb130fd59d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-11T21:24:15.990Z_

<details><summary>↩ Tool result · `toolu_01NE1qmQbzSuTYTv4jRQtv3P`</summary>

```text
Web search results for query: "github.com sglang KV cache compaction"

Links: [{"title":"How to turn on the kv cache disk? · Issue #10017 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/10017"},{"title":"[Feature] TurboQuant: High-performance 4-bit KV cache compression with fused Triton kernels · Issue #23134 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/23134"},{"title":"[RFC] Remote KV Connector for SGLang Global Cache Reuse and PD · Issue #7746 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/7746"},{"title":"[RFC] [Feature] Fast KV-cache pruning · Issue #19887 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/19887"},{"title":"[Feature] KV Cache Quantization · Issue #1351 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/1351"},{"title":"Quantized KV Cache — SGLang","url":"https://sgl-project.github.io/advanced_features/quantized_kv_cache.html"},{"title":"[Feature] Integrate KVPress in order to try more KV cache optimization heuristics easily · Issue #10585 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/10585"},{"title":"How can I enable CPU/RAM and disk caching for the KV cache? · Issue #10053 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/10053"},{"title":"[Feature] Support for Evicting Specific KV Cache to Save GPU Memory · Issue #2510 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/2510"},{"title":"Complete Guide: SGLang HiCache with Mooncake Backend — Mooncake","url":"https://kvcache-ai.github.io/Mooncake/getting_started/examples/sglang-integration/hicache-integration-v1.html"}]

Based on the search results, I found several relevant topics related to KV cache management in SGLang on GitHub:

## KV Cache Compression and Optimization

SGLang architecture controls the amount of video memory and places oom through "LRU elimination algorithm" and "quantization compression technology".

## Key Features and Initiatives

1. **Quantized KV Cache**: Quantized KV cache reduces the memory footprint of key-value cache storage by using lower-precision data types (FP8 or FP4) instead of the default model precision in BF16. FP4 with block size 16 supports approximately 1.78× more tokens than FP8, and approximately 3.56× more tokens than BF16.

2. **KV Cache Pruning**: As sequence lengths grow to tens or hundreds of thousands of tokens, the KV cache size becomes a main bottleneck for efficient LLM inference. SGLang implements pruning methods to retain only KV pairs likely to be accessed.

3. **TurboQuant**: The existing TurboQuant PR implements Google's TurboQuant algorithm (Zandieh et al., ICLR 2026) for KV cache compression.

4. **KVPress Integration**: KVPress provides a set of "presses" that compress the KV cache during the prefilling-phase.

5. **HiCache Multi-Tier Storage**: HiCache introduces a HiRadixTree that acts as a page table for referencing KV caches across different memory tiers: GPU Memory (L1), CPU Memory (L2), Mooncake and other Storage Backends (L3).

These features represent SGLang's comprehensive approach to KV cache management through various compression, pruning, and multi-tier storage strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86d941a0-7a61-4fa9-abdb-12357350ac12",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "358ddded-aa94-4c4c-9296-78230288a1b8",
  "sourceToolAssistantUUID": "86d941a0-7a61-4fa9-abdb-12357350ac12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-11T21:24:16.319Z_

<details><summary>↩ Tool result · `toolu_01MsPXN4rj8AvtKVowYwTUd1`</summary>

```text
Web search results for query: "sglang radix attention KV cache multi-turn"

Links: [{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/pdf/2312.07104"},{"title":"Fast and Expressive LLM Inference with RadixAttention and SGLang - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2024-01-17-sglang/"},{"title":"SGLang Documentation — SGLang","url":"https://sgl-project.github.io/"},{"title":"When to Choose SGLang Over vLLM: Multi-Turn Conversations and KV Cache Reuse | Runpod Blog","url":"https://www.runpod.io/blog/sglang-vs-vllm-kv-cache"},{"title":"Efficiently Programming Large Language Models using SGLang","url":"https://arxiv.org/html/2312.07104v1"},{"title":"SGLang Learning Series — Part 1: Shared Prefix, KV Cache, and RadixAttention | by Dharamendra Kumar | Medium","url":"https://medium.com/@dharamendra1314.kumar/sglang-learning-series-part-1-shared-prefix-kv-cache-and-radixattention-d7a847d20b1f"},{"title":"SGLang in Production: A Developer’s Guide to Structured Generation, RadixAttention, and Multi-Step LLM Pipelines","url":"https://www.runpod.io/articles/guides/blog-sglang-production-llm-pipelines"},{"title":"Inside SGLang: Anatomy of a High-Performance Structured LLM Inference System - SugiV Blog","url":"https://blog.sugiv.fyi/inside-sglang-anatomy-high-performance-structured-llm-inference-system"},{"title":"SGLang Production Deployment Guide: RadixAttention and Multi-Turn Inference on GPU Cloud (2026) | Spheron Blog","url":"https://www.spheron.network/blog/sglang-production-deployment-guide/"},{"title":"Efficient LLM Inference with SGLang Speaker: Ying Sheng (xAI, LMSYS, UCLA)","url":"https://llmsystem.github.io/llmsystem2025spring/assets/files/llmsys-25-sglang-72edc5043338f59db34d47e5b96ac870.pdf"}]

Based on the search results, here's what I found about SGLang's RadixAttention and KV cache for multi-turn conversations:

## RadixAttention Overview

RadixAttention enables the automatic reuse of the KV cache across multiple generation calls. The system maintains an LRU cache of the KV cache for all requests within a radix tree, managing it as a traditional cache and using a radix tree for efficient matching, insertion, and eviction.

## How It Works

RadixAttention stores KV cache entries in a radix tree where each node represents a sequence of tokens. When a new request arrives, the runtime walks the tree from the root, matching the request's prompt tokens against existing nodes. RadixAttention reuses KV cache for the shared prefix and computes only the suffix.

## Benefits for Multi-Turn Conversations

SGLang emerges as the clear winner for a specific but increasingly important use case: multi-turn conversations with shared context. vLLM is fast—but SGLang might be faster for multi-turn conversations, giving about a 10% boost over vLLM at the same context loads.

SGLang shines in unpredictable, dynamic scenarios where conversation flows vary. Its radix tree approach automatically discovers caching opportunities that would require manual optimization in vLLM.

For multi-turn scenarios specifically, for multi-turn, pass the full conversation history as a single prefix before the new user turn. This ensures the radix tree can match previous conversation state and maximize cache reuse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8586554-ac2c-47ca-8156-09c8687a1952",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "69d7035b-865a-489f-8d12-d530aae11c94",
  "sourceToolAssistantUUID": "c8586554-ac2c-47ca-8156-09c8687a1952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-11T21:24:17.340Z_

<details><summary>↩ Tool result · `toolu_01YKBurHNqZMNPfTodBLMBWb`</summary>

```text
Web search results for query: "vllm prefix caching KV reuse agent"

Links: [{"title":"Automatic Prefix Caching - vLLM","url":"https://docs.vllm.ai/en/stable/design/prefix_caching/"},{"title":"KV-Cache Wins You Can See: From Prefix Caching in vLLM to Distributed Scheduling with llm-d | llm-d","url":"https://llm-d.ai/blog/kvcache-wins-you-can-see"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://arxiv.org/html/2507.07400v1"},{"title":"Exposing KV cache for recomposition / reuse beyond prefix caching? - KV-Cache - vLLM Forums","url":"https://discuss.vllm.ai/t/exposing-kv-cache-for-recomposition-reuse-beyond-prefix-caching/2208"},{"title":"Automatic Prefix Caching — vLLM","url":"https://docs.vllm.ai/en/v0.8.5/design/v1/prefix_caching.html"},{"title":"Prefix caching | LLM Inference Handbook","url":"https://bentoml.com/llm/inference-optimization/prefix-caching"},{"title":"How prompt caching works - Paged Attention and Automatic Prefix Caching plus practical tips | sankalp's blog","url":"https://sankalp.bearblog.dev/how-prompt-caching-works/"},{"title":"[Feature]: Generalized KV cache reuse · Issue #25672 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/25672"},{"title":"Introduction — vLLM","url":"https://docs.vllm.ai/en/v0.5.4/automatic_prefix_caching/apc.html"},{"title":"[vLLM — Prefix KV Caching] vLLM’s Automatic Prefix Caching vs ChunkAttention | by Don Moon | Byte-Sized AI | Medium","url":"https://medium.com/byte-sized-ai/vllm-prefix-caching-vllms-automatic-prefix-caching-vs-chunkattention-749108317621"}]

Based on the web search results, here's a comprehensive overview of vLLM prefix caching and KV reuse in agent systems:

## vLLM Prefix Caching Overview

Automatic Prefix Caching (APC) caches the KV cache of existing queries, so that a new query can directly reuse the KV cache if it shares the same prefix with one of the existing queries, allowing the new query to skip the computation of the shared part.

## How It Works

vLLM takes this further with Automatic Prefix Caching: it intelligently identifies when requests share the same token sequence prefix. Instead of recomputing, it reuses the exact same memory pages from the cache through hash-based block matching.

The implementation uses a block-based approach where the prefix caching in vLLM v1 is implemented in the KV cache manager. The basic building block is the "Block" data class.

## Benefits for Agent Workflows

Prefix caching reuses the key-value (KV) tensors produced by self-attention layers for static prompt tokens across decoding steps and requests. This is particularly beneficial in agentic workflows, where each agent is initialized with a fixed prompt specifying its name, responsibilities, and behavioral traits. Since these prompts remain constant across iterations, prefix caching avoids redundant computation on static content and significantly reduces per-agent inference latency.

In a simple test sending a request with a ~10,000 token prompt to a Qwen/Qwen3-32B instance a second time, time-to-first-token drops from 4.3 seconds to just 0.6 seconds.

## Challenges with Limited GPU Memory

However, prefix caching alone is insufficient in the presence of limited GPU memory. Existing systems typically adopt a Least Recently Used (LRU) policy to evict KV caches that have not been accessed recently. This strategy can lead to suboptimal performance in agentic workflows.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "909e5a18-b37f-4855-bf1b-69fd82df49e8",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "658c8138-a2ff-4e74-bfbf-826889943795",
  "sourceToolAssistantUUID": "909e5a18-b37f-4855-bf1b-69fd82df49e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-11T21:24:17.568Z_

<details><summary>↩ Tool result · `toolu_01PyFufdgtimUxvJWxEXauSc`</summary>

```text
Web search results for query: "github.com vllm KV cache management agent"

Links: [{"title":"GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub","url":"https://github.com/LMCache/LMCache"},{"title":"GitHub - llm-d/llm-d-kv-cache: Distributed KV cache scheduling & offloading libraries · GitHub","url":"https://github.com/llm-d/llm-d-kv-cache-manager"},{"title":"[Misc] Allow initializing KV cache transfer agent when `kv_parallel_size==1` by KuntaiDu · Pull Request #11480 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/11480"},{"title":"vllm/vllm/v1/core/single_type_kv_cache_manager.py at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/blob/main/vllm/v1/core/single_type_kv_cache_manager.py"},{"title":"[RFC]: Sparse KV cache management framework · Issue #12254 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/12254"},{"title":"KV-Cache Wins You Can See: From Prefix Caching in vLLM to Distributed Scheduling with llm-d | llm-d","url":"https://llm-d.ai/blog/kvcache-wins-you-can-see"},{"title":"[Feature]: Implement vAttention: Virtual Memory Management for KV Cache on NVIDIA GPUs · Issue #17612 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17612"},{"title":"Understanding vllm kv cache - KV-Cache - vLLM Forums","url":"https://discuss.vllm.ai/t/understanding-vllm-kv-cache/2061"},{"title":"Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://arxiv.org/html/2511.02230v2"},{"title":"[Feature]: Generalized KV cache reuse · Issue #25672 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/25672"}]

Based on the search results, I found several relevant resources related to vLLM and KV cache management:

## Key Projects and Implementations

### 1. **LMCache** - KV Cache Layer for vLLM
LMCache is an LLM serving engine extension to reduce TTFT and increase throughput, especially under long-context scenarios, by storing the KV caches of reusable texts across the datacenter (including GPU, CPU, Disk and even S3).

### 2. **llm-d-kv-cache** - Distributed KV Cache Management
The llmd-fs-backend is a storage backend for vLLM's OffloadingConnector that moves KV-cache blocks between GPU and shared storage. The system is powered by KVEvents streamed from vLLM, which allow the indexer to track which blocks reside on which nodes and on which tier (e.g., GPU or CPU), and this metadata is the foundation for intelligent routing, enabling schedulers to make optimal, KV-cache-aware placement decisions.

### 3. **vLLM Core KV Cache Management**
vLLM has a SingleTypeKVCacheManager, an abstract base class for a manager that handles the kv cache management logic of one specific type of attention layer.

### 4. **Advanced KV Cache Features**
vLLM supports initializing the KV cache transfer agent even when kv_parallel_size==1, which is useful when connecting to a KV cache database where each process acts as an independent database reader/writer.

### 5. **Emerging Technologies**
- CacheTTL is a KV cache retention and scheduling system that balances the benefit of cache reuse and the cost of blocking GPU memory through a time-to-live mechanism, integrating TTL-aware pinning with program-level FCFS.
- vAttention is a memory management approach without PagedAttention that uses CUDA virtual memory APIs to decouple virtual and physical memory, retaining a contiguous virtual memory layout while mitigating physical memory fragmentation.

These projects show the diverse approaches being developed in the vLLM ecosystem for managing KV caches across different hardware configurations and use cases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41e1eaf6-df6c-4b5f-9369-a40f3c1100dd",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "23fc3564-3163-4b1c-86d0-e155fd88cc16",
  "sourceToolAssistantUUID": "41e1eaf6-df6c-4b5f-9369-a40f3c1100dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-11T21:24:17.838Z_

<details><summary>↩ Tool result · `toolu_01S1S1vSTaZ5DKcAt3gkpguu`</summary>

```text
Web search results for query: "github Attention Matching KV cache paper implementation"

Links: [{"title":"Research: Implement \"Fast KV Compaction via Attention Matching\" for extreme VRAM savings · Issue #20037 · ggml-org/llama.cpp","url":"https://github.com/ggml-org/llama.cpp/issues/20037"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"Fast KV Compaction via Attention Matching","url":"https://arxiv.org/pdf/2602.16284"},{"title":"Paper page - ChunkAttention: Efficient Self-Attention with Prefix-Aware KV Cache and Two-Phase Partition","url":"https://huggingface.co/papers/2402.15220"},{"title":"GitHub - ksheth96/BalanceKV: [NeurIPS 2025 Spotlight] Official implementation of our KV cache compression algorithm BalanceKV in our NeurIPS 2025 Spotlight paper \"Streaming Attention Approximation via Discrepancy Theory\" https://arxiv.org/abs/2502.07861 · GitHub","url":"https://github.com/ksheth96/BalanceKV"},{"title":"SharedContextBench: Evaluating Long-Context Methods in KV Cache Reuse","url":"https://neurips2024-enlsp.github.io/papers/paper_93.pdf"},{"title":"A Survey on Large Language Model Acceleration based on KV Cache Management","url":"https://arxiv.org/html/2412.19442v3"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"KV Caching Explained: Optimizing Transformer Inference Efficiency","url":"https://huggingface.co/blog/not-lain/kv-caching"},{"title":"GitHub - Zefan-Cai/Awesome-LLM-KV-Cache: Awesome-LLM-KV-Cache: A curated list of 📙Awesome LLM KV Cache Papers with Codes.","url":"https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache"}]

Based on the search results, I found relevant information about the "Fast KV Compaction via Attention Matching" paper and its implementation status:

## Paper Details

The paper introduces "Fast KV Compaction via Attention Matching," which presents a method to compress the K and V matrices into much smaller representations that stay in the latent space, allowing the model to directly query against these compact matrices during generation without needing to decompress them.

## Key Technical Aspects

The algorithm requires calculating the Moore-Penrose pseudoinverse of a matrix to solve an overdetermined system (least-squares problem) for the Attention Matching step. The attention-matching (AM) methods trace a speed–quality tradeoff and form the Pareto frontier, outperforming prior token-selection baselines and exceeding the performance of Cartridges while being 2 orders of magnitude faster.

## Implementation Status

There is an RFC (Request for Comments) open on the ggml-org/llama.cpp repository to implement "Fast KV Compaction via Attention Matching," though no PR is ready yet. According to the paper's benchmarks (tested on Qwen and Llama models), the proposed implementation maintains near-lossless generation quality on tasks like long-document analysis and coding, while drastically reducing the memory footprint.

The main challenge for implementation appears to be integrating the Moore-Penrose pseudoinverse calculation efficiently within the ggml architecture across different backends.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3175955d-b112-4aa6-80b7-d84e121ebc5e",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "a557fd13-8dbb-4e48-ad5b-476bd3fc6d66",
  "sourceToolAssistantUUID": "3175955d-b112-4aa6-80b7-d84e121ebc5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-11T21:24:21.400Z_

Now let me search for the specific papers mentioned (CacheTTL, PBKV, CacheClip) and get more details on some of the key repos.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a557fd13-8dbb-4e48-ad5b-476bd3fc6d66",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV9TSBnvYne2aoFLcti",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfe6d250-a16d-4994-974b-9d9168ed9707",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEQYLt1sXRet7VQj2KL8PE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8715,
      "cache_read_input_tokens": 10006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8715,
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

_source line 24 · 2026-05-11T21:24:21.948Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012L9toteLjjW5QL4MTCdgCe`</summary>

```json
{
  "query": "github CacheTTL KV cache time-to-live LLM agent implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfe6d250-a16d-4994-974b-9d9168ed9707",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV9TSBnvYne2aoFLcti",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b7b359a-89f7-4a09-b6c3-e49f2526a536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEQYLt1sXRet7VQj2KL8PE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8715,
      "cache_read_input_tokens": 10006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8715,
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

_source line 25 · 2026-05-11T21:24:22.353Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LUhPVXgCAVxaNYQpRbfepm`</summary>

```json
{
  "query": "github PBKV \"page-based KV cache\" implementation paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b7b359a-89f7-4a09-b6c3-e49f2526a536",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV9TSBnvYne2aoFLcti",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c295deef-6c59-435e-853a-cadc82e692b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEQYLt1sXRet7VQj2KL8PE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8715,
      "cache_read_input_tokens": 10006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8715,
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

_source line 26 · 2026-05-11T21:24:22.824Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gu7pg431dwRqqMXrJhSoBC`</summary>

```json
{
  "query": "github CacheClip KV cache clipping implementation paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c295deef-6c59-435e-853a-cadc82e692b8",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV9TSBnvYne2aoFLcti",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0909edb3-fd84-4a3b-bfb3-f703a3cb61be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEQYLt1sXRet7VQj2KL8PE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8715,
      "cache_read_input_tokens": 10006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8715,
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

_source line 27 · 2026-05-11T21:24:23.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016myjnpGTaVkx9EcpX9eqC4`</summary>

```json
{
  "query": "github BalanceKV NeurIPS 2025 KV cache compression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0909edb3-fd84-4a3b-bfb3-f703a3cb61be",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawV9TSBnvYne2aoFLcti",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71081544-171b-414b-bd10-9817c725d584",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEQYLt1sXRet7VQj2KL8PE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8715,
      "cache_read_input_tokens": 10006,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8715
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 10006,
          "cache_creation_input_tokens": 8715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8715,
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

_source line 28 · 2026-05-11T21:24:28.214Z_

<details><summary>↩ Tool result · `toolu_016myjnpGTaVkx9EcpX9eqC4`</summary>

```text
Web search results for query: "github BalanceKV NeurIPS 2025 KV cache compression"

Links: [{"title":"GitHub - ksheth96/BalanceKV: [NeurIPS 2025 Spotlight] Official implementation of our KV cache compression algorithm BalanceKV in our NeurIPS 2025 Spotlight paper \"Streaming Attention Approximation via Discrepancy Theory\" https://arxiv.org/abs/2502.07861 · GitHub","url":"https://github.com/ksheth96/BalanceKV"},{"title":"NeurIPS Poster KVLink: Accelerating Large Language Models via Efficient KV Cache Reuse","url":"https://neurips.cc/virtual/2025/poster/116061"},{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub","url":"https://github.com/FFY0/AdaKV"},{"title":"NeurIPS Poster ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/120181"},{"title":"GitHub - snu-mllab/KVzip: [NeurIPS'25 Oral] Query-agnostic KV cache eviction: 3–4× reduction in memory and 2× decrease in latency (Qwen3/2.5, Gemma3, LLaMA3)","url":"https://github.com/snu-mllab/KVzip"},{"title":"NeurIPS Poster Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://neurips.cc/virtual/2025/poster/119605"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"NeurIPS Poster Improving Model Representation and Reducing KV Cache via Skip Connections with First Value Heads","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/117156"},{"title":"Efficient LLMs at Scale: My NeurIPS Week in KV Caches, Spec Decoding, and FP4","url":"https://kaitchup.substack.com/p/efficient-llms-at-scale-my-neurips"}]

Based on the search results, I found relevant information about BalanceKV:

BalanceKV is a KV cache compression algorithm featured as a NeurIPS 2025 Spotlight paper titled "Streaming Attention Approximation via Discrepancy Theory". 

The official implementation repository contains code for evaluating the BalanceKV algorithm on the LongBench and NIAH benchmarks.

The GitHub repository (https://github.com/ksheth96/BalanceKV) includes several key components:
- A balanced walk algorithm implementation
- Functions for inference using the Llama model with custom KV cache patching
- Main evaluation scripts for running LongBench and NIAH (Needle In A Haystack) evaluations

The LongBench evaluation can be run with the default Llama-3.1-8B-Instruct model, and the repository includes additional ablation study experiments in a notebook for single layer attention approximation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71081544-171b-414b-bd10-9817c725d584",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "880cdf04-ee8d-4de1-a1e5-ab74c4fbdc33",
  "sourceToolAssistantUUID": "71081544-171b-414b-bd10-9817c725d584",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-11T21:24:29.726Z_

<details><summary>↩ Tool result · `toolu_012L9toteLjjW5QL4MTCdgCe`</summary>

```text
Web search results for query: "github CacheTTL KV cache time-to-live LLM agent implementation"

Links: [{"title":"Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://arxiv.org/html/2511.02230v3"},{"title":"CacheTTL: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://arxiv.org/html/2511.02230v4"},{"title":"[2511.02230] Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://arxiv.org/abs/2511.02230"},{"title":"(PDF) Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://www.researchgate.net/publication/397279804_Continuum_Efficient_and_Robust_Multi-Turn_LLM_Agent_Scheduling_with_KV_Cache_Time-to-Live"},{"title":"Paper page - Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://huggingface.co/papers/2511.02230"},{"title":"CacheTTL: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV","url":"https://arxiv.org/pdf/2511.02230"},{"title":"GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub","url":"https://github.com/LMCache/LMCache"},{"title":"KV Cache System — TensorRT LLM","url":"https://nvidia.github.io/TensorRT-LLM/latest/features/kvcache.html"},{"title":"Understanding and Coding the KV Cache in LLMs from Scratch","url":"https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms"},{"title":"EFFICIENT AND ROBUST MULTI-TURN LLM AGENT ...","url":"https://openreview.net/pdf/5c6ed290be90eea7b75202124c5bffecac714a4c.pdf"}]

Based on the search results, I found comprehensive information about CacheTTL and KV cache time-to-live implementations for LLM agent systems:

## CacheTTL: KV Cache Time-to-Live for LLM Agents

CacheTTL is a KV cache retention and scheduling system that balances both the benefit of cache reuse and the cost of blocking GPU memory through a time-to-live mechanism.

### Key Implementation Details

CacheTTL introduces a KV cache time-to-live (TTL) mechanism to retain KV cache inside GPU after request finishes. For each LLM request that generates a tool call during the inference step, CacheTTL models both the prefill/reload cost and the per-turn queueing delay reduction brought by retaining KV cache, and compares this with the cost of occupying GPU memory space during the TTL time to decide how long the KV cache can stay in GPU memory before being automatically evicted.

### How TTL Works

CacheTTL implemented a tool call handler that is called each time a request enters or leaves the serving engine. It identifies the tool call, predicts the duration, and decides the timeout of the KV cache pin based on both throughput and request ordering concerns.

### Performance Benefits

CacheTTL achieves up to 8.18x improvements in both latency and throughput over previous methods in both emulated and real cases.

### GitHub Repository

The implementation will be open-sourced upon publication. Additionally, preview code is available at: https://github.com/Hanchenli/vllm-continuum

### Architecture Integration

The implementation is built on top of vLLM and shows consistent improvements in end-to-end job completion time across model sizes, hardware configurations, and real-world agent workloads.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b7b359a-89f7-4a09-b6c3-e49f2526a536",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "d097360e-3f49-43d9-be56-a0ea4c9228f7",
  "sourceToolAssistantUUID": "7b7b359a-89f7-4a09-b6c3-e49f2526a536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-11T21:24:30.414Z_

<details><summary>↩ Tool result · `toolu_01LUhPVXgCAVxaNYQpRbfepm`</summary>

```text
Web search results for query: "github PBKV "page-based KV cache" implementation paper"

Links: [{"title":"GitHub - Zefan-Cai/Awesome-LLM-KV-Cache: Awesome-LLM-KV-Cache: A curated list of 📙Awesome LLM KV Cache Papers with Codes.","url":"https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache"},{"title":"GitHub - thu-nics/PM-KVQ: The official code implementation for paper \"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs\"","url":"https://github.com/thu-nics/PM-KVQ"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | OpenReview","url":"https://openreview.net/forum?id=jZVNmDiU86"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"},{"title":"GitHub - Zefan-Cai/KVCache-Factory: Unified KV Cache Compression Methods for Auto-Regressive Models · GitHub","url":"https://github.com/Zefan-Cai/KVCache-Factory"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/html/2406.02069v1"},{"title":"kv-cache · GitHub Topics · GitHub","url":"https://github.com/topics/kv-cache?l=python&o=desc&s=updated"},{"title":"[2406.02069] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069"}]

Based on the search results, I found several resources related to page-based KV cache implementations, though I should note that the exact term "PBKV" didn't appear in these results. However, I found related implementations and papers:

## Key Findings:

**GitHub Repositories for KV Cache Compression:**

1. Awesome-LLM-KV-Cache: A curated list of Awesome LLM KV Cache Papers with Codes (https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache)

2. NVIDIA/kvpress includes multiple KV cache compression methods, including PyramidKVPress which maintains pyramid-like cache sizes, allocating more cache budget to lower layers and less to higher layers (https://github.com/NVIDIA/kvpress)

3. KVCache-Factory provides unified KV cache compression methods supporting pyramidkv, snapkv, streamingllm, and h2o (https://github.com/Zefan-Cai/KVCache-Factory)

**Paper on Page-Based Approaches:**

PyramidKV investigates attention-based information flow patterns in LLMs and develops a KV cache compression method that dynamically adjusts KV cache size across different layers, allocating more cache in lower layers and less in higher ones (arXiv:2406.02069)

If you're looking for a specific "PBKV" implementation, you may want to search more specifically or check recent arXiv papers, as the exact term didn't appear in these results but page-based or layer-aware KV cache methods like PyramidKV appear to be the most relevant implementations available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c295deef-6c59-435e-853a-cadc82e692b8",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "4529ca39-bc7d-4950-bad3-fe0e2e25e5b9",
  "sourceToolAssistantUUID": "c295deef-6c59-435e-853a-cadc82e692b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-11T21:24:31.395Z_

<details><summary>↩ Tool result · `toolu_01Gu7pg431dwRqqMXrJhSoBC`</summary>

```text
Web search results for query: "github CacheClip KV cache clipping implementation paper"

Links: [{"title":"CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://arxiv.org/html/2510.10129v1"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"[2510.10129] CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://arxiv.org/abs/2510.10129"},{"title":"[PDF] CacheClip: Accelerating RAG with Effective KV Cache Reuse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CacheClip:-Accelerating-RAG-with-Effective-KV-Cache-Yang-Leng/ce9587ac624800977c412c8e19d995141fded68d"},{"title":"blog/kv-cache-quantization.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/kv-cache-quantization.md"},{"title":"Paper page - KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems","url":"https://huggingface.co/papers/2510.12872"},{"title":"CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://www.researchgate.net/publication/396458373_CacheClip_Accelerating_RAG_with_Effective_KV_Cache_Reuse"},{"title":"GitHub - Zefan-Cai/Awesome-LLM-KV-Cache: Awesome-LLM-KV-Cache: A curated list of 📙Awesome LLM KV Cache Papers with Codes.","url":"https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"GitHub - Zefan-Cai/KVCache-Factory: Unified KV Cache Compression Methods for Auto-Regressive Models · GitHub","url":"https://github.com/Zefan-Cai/KVCache-Factory"}]

Based on the search results, I found information about CacheClip, which is a KV cache optimization technique for RAG systems:

## CacheClip: KV Cache Clipping Implementation

CacheClip is a novel framework designed to achieve both fast time-to-first-token (TTFT) and high generation quality in RAG systems.

### Key Components

CacheClip integrates three techniques: (1) auxiliary-model-guided token selection for selective KV cache recomputation, where the auxiliary model is finetuned to improve selection accuracy, (2) shared prefixes to eliminate redundant attention sinks, and (3) grouping strategy to maintain local coherence during partial KV cache updates.

### Performance Results

Experiments show CacheClip retains up to 94.8% and 85.0% of full-attention performance on NIAH and LongBench, outperforming APE and CacheBlend by 25.2% and 35.1% on NIAH (with reomp% = 20%), while accelerating LLM inference by up to 1.92× in prefill time.

### Technical Approach

The key insight is that small auxiliary LLMs exhibit similar last-layer attention distributions to primary LLMs (the target model for generation), enabling efficient identification of tokens critical for restoring inter-chunk attention.

The research paper was published on arXiv (arXiv:2510.10129) in October 2025 by authors including Bin Yang and Qiuyu Leng.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0909edb3-fd84-4a3b-bfb3-f703a3cb61be",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "ec7530c5-0811-43e5-9df7-6b62be3d5514",
  "sourceToolAssistantUUID": "0909edb3-fd84-4a3b-bfb3-f703a3cb61be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-11T21:24:33.799Z_

Now let me fetch more details on the key repositories and get star counts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec7530c5-0811-43e5-9df7-6b62be3d5514",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVATQymbGNbTKqDFZg3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2220fd06-ac3b-4198-a3fb-91da98090916",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011c8chtmmt9HVb46i14X1mM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 933,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 18721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3350,
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

_source line 33 · 2026-05-11T21:24:35.748Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017yVhqzWG6D37hc4wfoB4K9`</summary>

```json
{
  "url": "https://github.com/adamzweiger/compaction",
  "prompt": "Extract: repository description, star count, what it implements, programming language, last updated date, and any details about incremental/online compaction support."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2220fd06-ac3b-4198-a3fb-91da98090916",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVATQymbGNbTKqDFZg3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0056b97a-89ca-4f39-a35b-2a4f8206f5e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011c8chtmmt9HVb46i14X1mM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 933,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 18721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3350,
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

_source line 34 · 2026-05-11T21:24:37.304Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NDNfkG7ogtLS8gLjrjE7Tr`</summary>

```json
{
  "url": "https://github.com/NVIDIA/kvpress",
  "prompt": "Extract: repository description, star count, list of all compression methods/presses available, programming language, last updated date. Focus on methods that could support incremental or online KV compaction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0056b97a-89ca-4f39-a35b-2a4f8206f5e1",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVATQymbGNbTKqDFZg3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed7e69bd-c995-48f4-a237-ebd40da35a76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011c8chtmmt9HVb46i14X1mM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 933,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 18721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3350,
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

_source line 35 · 2026-05-11T21:24:38.734Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MuGLByXmdJPfqWrZ7z99fb`</summary>

```json
{
  "url": "https://github.com/IsaacRe/vllm-kvcompress",
  "prompt": "Extract: repository description, star count, what it implements, programming language, and whether it supports continual/incremental compression during generation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed7e69bd-c995-48f4-a237-ebd40da35a76",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVATQymbGNbTKqDFZg3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13236596-3f82-4dfc-aef9-0286f380b640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011c8chtmmt9HVb46i14X1mM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 933,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 18721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3350,
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

_source line 36 · 2026-05-11T21:24:40.123Z_

<details><summary>↩ Tool result · `toolu_017yVhqzWG6D37hc4wfoB4K9`</summary>

```text
# Compaction Repository Summary

**Repository Description:**
"Algorithms for latent compaction" focusing on KV cache compression techniques.

**Star Count:**
217 stars

**What It Implements:**
The project implements Attention Matching (AM), an algorithm that "compacts a KV cache in latent space by constructing a smaller set of keys and values that reproduce the original attention behavior." It's based on the paper "Fast KV Compaction via Attention Matching."

**Programming Language:**
Python (93.5%) and Shell (6.5%)

**Last Updated:**
The repository shows 5 commits on the main branch, but no explicit last-update timestamp is visible in the provided content.

**Incremental/Online Compaction Support:**
The page content does not mention support for incremental or online compaction. The examples and evaluation scripts focus on batch compaction of prefilled KV caches for question-answering and reasoning tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0056b97a-89ca-4f39-a35b-2a4f8206f5e1",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "4de9d9b3-2ad2-45cf-a008-b36157cb48b9",
  "sourceToolAssistantUUID": "0056b97a-89ca-4f39-a35b-2a4f8206f5e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-11T21:24:40.543Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JrhLHmfwjT6uMyFu2kY8kF`</summary>

```json
{
  "url": "https://github.com/LMCache/LMCache",
  "prompt": "Extract: repository description, star count, what it implements, programming language, supported backends (vLLM, SGLang), and any features related to agent/multi-turn KV cache reuse."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4de9d9b3-2ad2-45cf-a008-b36157cb48b9",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVATQymbGNbTKqDFZg3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "252c5ada-64b1-4ce4-b8db-21d9ee92e1cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011c8chtmmt9HVb46i14X1mM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 933,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 18721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3350,
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

_source line 38 · 2026-05-11T21:24:42.066Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01A8P828rGWozd5YYLobwFRZ`</summary>

```json
{
  "url": "https://github.com/Hanchenli/vllm-continuum",
  "prompt": "Extract: repository description, star count, what it implements (CacheTTL/Continuum), programming language, and details about agent-aware KV cache management."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "252c5ada-64b1-4ce4-b8db-21d9ee92e1cb",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVATQymbGNbTKqDFZg3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02f129e9-557b-486f-9bb4-fa447eb497f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011c8chtmmt9HVb46i14X1mM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 933,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 18721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3350,
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

_source line 39 · 2026-05-11T21:24:43.086Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KeAUbgkeVGA9pxLMgwVoUy`</summary>

```json
{
  "url": "https://github.com/ksheth96/BalanceKV",
  "prompt": "Extract: repository description, star count, what algorithm it implements, programming language, and whether it supports streaming/incremental KV cache compression."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02f129e9-557b-486f-9bb4-fa447eb497f5",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVATQymbGNbTKqDFZg3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b3b0aca-f12b-4775-9bd2-c3cb351cb534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011c8chtmmt9HVb46i14X1mM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 933,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 18721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3350,
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

_source line 40 · 2026-05-11T21:24:44.388Z_

<details><summary>↩ Tool result · `toolu_01NDNfkG7ogtLS8gLjrjE7Tr`</summary>

```text
# KVPress Repository Summary

**Repository Description:**
"LLM KV cache compression made easy" – implements multiple KV cache compression methods and benchmarks using Hugging Face transformers to simplify development of new compression approaches.

**Star Count:** 1.1k stars

**Programming Language:** Python (98.4%)

**Last Updated:** April 9, 2026 (v0.5.3)

---

## Available Compression Methods (Presses)

**Scoring-Based Methods:**
RandomPress, KnormPress, SnapKVPress, ExpectedAttentionPress, StreamingLLMPress, TOVAPress, ObservedAttentionPress, QFilterPress, PyramidKVPress, LagKVPress, KeyDiffPress, NonCausalAttnPress, LeverageScorePress, CompactorPress, CURPress, KVzapPress, FastKVzipPress

**Dimension/Architecture-Based:**
ThinKPress, SimLayerKVPress, DuoAttentionPress, FinchPress, KVzipPress, KVComposePress

**Wrapper/Composable Methods:**
AdaKVPress, PerLayerCompressionPress, ComposedPress, KeyRerotationPress, ChunkKVPress, ChunkPress, CriticalKVPress, BlockPress, DecodingPress, PrefillDecodingPress, DMSPress, CAMPress

---

## Methods Supporting Incremental/Online Compression

**DecodingPress** is the primary candidate: "compresses the KV cache periodically during token generation" with configurable `compression_interval` and `target_size` parameters, enabling compression throughout generation rather than only prefilling.

**CAMPress** also supports decoding-phase compression and "merges the kv cache of evicted tokens into keep tokens."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed7e69bd-c995-48f4-a237-ebd40da35a76",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "d5c04d4c-21ee-4413-b4de-cf00230ee9d9",
  "sourceToolAssistantUUID": "ed7e69bd-c995-48f4-a237-ebd40da35a76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-11T21:24:43.589Z_

<details><summary>↩ Tool result · `toolu_01MuGLByXmdJPfqWrZ7z99fb`</summary>

```text
# vllm-kvcompress Repository Summary

**Repository Description:**
"KV cache compression for high-throughput LLM inference" – a fork of vLLM v0.6.0 implementing a novel compression method to boost throughput in memory-constrained deployments.

**Star Count:** 157 stars

**What It Implements:**
The project introduces KV-Compress, a paged KV-cache compression technique that enables variable compression rates across attention heads. This allows sequences to maintain smaller cache footprints while preserving generation quality, as demonstrated through LongBench evaluations and throughput benchmarks.

**Primary Programming Language:**
Python (79.2%), with supporting CUDA (15.8%) and C++ (2.7%) components.

**Continual/Incremental Compression Support:**
Yes. The documentation explicitly mentions "continual compression (compressing during decoding as well as on prefill)" as an optional feature configurable via the `--continual-compression` flag during experiments. Standard usage compresses primarily during prefill, but this extension enables ongoing compression throughout generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13236596-3f82-4dfc-aef9-0286f380b640",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "b0339d65-635b-4eb6-b395-87e0a82c76c7",
  "sourceToolAssistantUUID": "13236596-3f82-4dfc-aef9-0286f380b640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-11T21:24:44.522Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016jq93VNPDHTsc4DFmufcx2`</summary>

```json
{
  "url": "https://github.com/snu-mllab/KVzip",
  "prompt": "Extract: repository description, star count, what it implements, compression ratio, supported models, and whether it could be used for incremental KV compaction between agent tool calls."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0339d65-635b-4eb6-b395-87e0a82c76c7",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVATQymbGNbTKqDFZg3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ce09974-322f-4f70-a05f-bba555239444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011c8chtmmt9HVb46i14X1mM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 933,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 18721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3350,
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

_source line 43 · 2026-05-11T21:24:45.148Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01W3VWwuUV6LVAXDTn6UM3Gq`</summary>

```json
{
  "url": "https://github.com/NVlabs/RocketKV",
  "prompt": "Extract: repository description, star count, what it implements, the two-stage compression approach, and whether it supports incremental/online compression."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ce09974-322f-4f70-a05f-bba555239444",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVATQymbGNbTKqDFZg3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e648adab-5a2e-4a91-abef-7c5c7630dfb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011c8chtmmt9HVb46i14X1mM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 933,
      "cache_creation_input_tokens": 3350,
      "cache_read_input_tokens": 18721,
      "output_tokens": 824,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3350
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 933,
          "output_tokens": 824,
          "cache_read_input_tokens": 18721,
          "cache_creation_input_tokens": 3350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3350,
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

_source line 44 · 2026-05-11T21:24:45.912Z_

<details><summary>↩ Tool result · `toolu_01JrhLHmfwjT6uMyFu2kY8kF`</summary>

```text
# LMCache Repository Summary

**Repository Description:**
"Supercharge Your LLM with the Fastest KV Cache Layer"

**Star Count:** 8.2k stars

**What It Implements:**
LMCache is an LLM serving engine extension designed to reduce Time-To-First-Token (TTFT) and boost throughput in long-context scenarios. It stores KV caches of reusable text across distributed infrastructure (GPU, CPU, disk, S3) and reuses them across any serving instance, achieving 3-10x latency improvements in applications like multi-round QA and RAG.

**Primary Programming Language:** Python (89.9%)

**Supported Serving Backends:**
- vLLM (v1) - with CPU offloading, disaggregated prefill, and P2P sharing
- SGLang - for KV cache offloading

**Storage Backends Supported:**
- CPU memory
- Disk storage
- NIXL acceleration

**Agent/Multi-Turn Features:**
The project explicitly targets multi-round QA and RAG use cases where KV cache reuse across conversation turns provides significant performance gains. The system reuses cached KV pairs from "any reused text" not restricted to prefixes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "252c5ada-64b1-4ce4-b8db-21d9ee92e1cb",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "dd74e2ef-bf36-485b-bede-5eac75a27434",
  "sourceToolAssistantUUID": "252c5ada-64b1-4ce4-b8db-21d9ee92e1cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-11T21:24:47.737Z_

<details><summary>↩ Tool result · `toolu_01KeAUbgkeVGA9pxLMgwVoUy`</summary>

```text
# BalanceKV Repository Summary

**Repository Description:** "[NeurIPS 2025 Spotlight] Official implementation of our KV cache compression algorithm BalanceKV" for the paper "Streaming Attention Approximation via Discrepancy Theory."

**Star Count:** 9 stars

**Algorithm Implemented:** BalanceKV - a KV cache compression technique based on balanced walk and discrepancy theory principles for attention approximation.

**Programming Language:** Python (100%)

**Streaming/Incremental KV Cache Support:** Yes. The repository implements streaming attention approximation through its balanced walk algorithm, enabling incremental KV cache compression during inference without requiring full context access.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b3b0aca-f12b-4775-9bd2-c3cb351cb534",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "634906e8-82fe-46b2-8c92-f4be06b73dd1",
  "sourceToolAssistantUUID": "1b3b0aca-f12b-4775-9bd2-c3cb351cb534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-11T21:24:48.397Z_

<details><summary>↩ Tool result · `toolu_01A8P828rGWozd5YYLobwFRZ`</summary>

```text
# vLLM-Continuum Repository Summary

**Repository Description:** "Preview Code for Continuum Paper" - a modified version of vLLM implementing Continuum-style scheduling for enhanced inference performance.

**Star Count:** 75 stars

**Implementation:** The repository implements **Continuum scheduling** (without estimation from the original paper) rather than CacheTTL. Users can enable it via the `--scheduling-policy continuum` flag when starting the server.

**Primary Language:** Python (86.7%), with supporting CUDA (7.7%) and C++ (4.1%) components.

**Agent-Aware KV Cache Management:**

The system includes agent-aware capabilities through integration with mini-swe-agent. Key features include:

- **Sticky-session routing** for multi-node support to maintain request affinity
- **CPU offload capability** using lmcache for extended KV cache storage: "LMCACHE_MAX_LOCAL_CPU_SIZE=&lt;CPU_SIZE_GB>"
- **Tunable pin logic** allowing users to "use this as a base-repo to tune KV cache pin logic on different workloads"
- **SWE-bench evaluation integration** demonstrating agent-based task handling with configurable concurrency models (fixed workers or Poisson arrival rates)

The design enables optimized KV cache management across distributed inference scenarios while maintaining compatibility with agentic workloads.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02f129e9-557b-486f-9bb4-fa447eb497f5",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "574068d0-6bd0-4ab0-8fb9-fad5bf86bdae",
  "sourceToolAssistantUUID": "02f129e9-557b-486f-9bb4-fa447eb497f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-11T21:24:49.537Z_

<details><summary>↩ Tool result · `toolu_016jq93VNPDHTsc4DFmufcx2`</summary>

```text
# KVzip Repository Summary

**Repository Description:**
"Query-agnostic KV cache compression with context reconstruction" designed to optimize inference in large language models by reducing memory footprint and latency.

**Star Count:**
218 stars

**What It Implements:**
KVzip provides query-agnostic KV cache eviction through two approaches: context-dependent compression (eliminating 70% of cache entries) and context-independent head-level compression. The system reconstructs context for diverse future queries without requiring advance knowledge of what those queries will be.

**Compression Ratio:**
Achieves "3–4× reduction in memory and 2× decrease in decoding latency" with minimal performance degradation. Context-independent mode operates at a compression ratio of 0.6 with negligible runtime overhead.

**Supported Models:**
- Qwen 2.5/3
- LLaMA3/3.1
- Gemma3

**Suitability for Incremental KV Compaction Between Agent Tool Calls:**
The architecture appears well-suited for this use case. The system supports "multi-turn inference, retaining full interaction histories" and offers selective eviction of "KV pairs corresponding to the queries and generated tokens." The `update_cache=True` parameter enables cache management across sequential operations, making it viable for agent workflows involving sequential tool calls.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ce09974-322f-4f70-a05f-bba555239444",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "80fe4d88-c0c8-42d5-aa1b-d4bbabd781bc",
  "sourceToolAssistantUUID": "2ce09974-322f-4f70-a05f-bba555239444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-11T21:24:49.934Z_

<details><summary>↩ Tool result · `toolu_01W3VWwuUV6LVAXDTn6UM3Gq`</summary>

```text
# RocketKV Repository Summary

**Repository Description:**
Official implementation of RocketKV, an ICML 2025 paper on accelerating long-context LLM inference.

**Star Count:**
46 stars

**What It Implements:**
A training-free KV cache compression method that delivers "end-to-end speedup by up to 3.7×, as well as peak memory reduction by up to 32.6%" during the decode phase on NVIDIA A100 GPUs, with "negligible accuracy loss on a variety of long-context tasks."

**Two-Stage Compression Approach:**

1. **First Stage (SnapKV):** Performs coarse-grain permanent removal of low-importance KV tokens from input sequences while preserving critical ones.

2. **Second Stage (Hybrid Sparse Attention):** Conducts fine-grain dynamic token selection on remaining KV tokens followed by top-k attention scoring, with K-tensor compression along both sequence and head dimensions.

**Incremental/Online Compression Support:**
The repository documentation does not explicitly address whether RocketKV supports incremental or online compression capabilities. No clear evidence of this feature appears in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e648adab-5a2e-4a91-abef-7c5c7630dfb8",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "21aaddbe-e201-46d2-925e-ac28619df3e6",
  "sourceToolAssistantUUID": "e648adab-5a2e-4a91-abef-7c5c7630dfb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-11T21:24:53.359Z_

Let me get a few more details on remaining repos and framework-level KV cache management.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21aaddbe-e201-46d2-925e-ac28619df3e6",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVBpfC4Ehe7nX8PajzW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e52ff416-aeb2-4c91-8f51-8854443a4eab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xAs4kPkpTkiCH1a991yca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 22071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4271,
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

_source line 50 · 2026-05-11T21:24:54.809Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CfSZTKscawEpfJiGsdKoVu`</summary>

```json
{
  "url": "https://github.com/aivrar/multi-turboquant",
  "prompt": "Extract: repository description, star count, what methods it implements, and any features related to agent or multi-turn KV cache management."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e52ff416-aeb2-4c91-8f51-8854443a4eab",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVBpfC4Ehe7nX8PajzW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5141c62-0c03-4351-9d9e-ada85e395ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xAs4kPkpTkiCH1a991yca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 22071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4271,
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

_source line 51 · 2026-05-11T21:24:55.810Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015Rc4qJjQj5JEZayg95HG1o`</summary>

```json
{
  "url": "https://github.com/llm-d/llm-d-kv-cache-manager",
  "prompt": "Extract: repository description, star count, what it implements for distributed KV cache management, and relevance to agent workflows."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5141c62-0c03-4351-9d9e-ada85e395ab1",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVBpfC4Ehe7nX8PajzW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5c8adc5-0500-4cf3-8b4b-ec4cc04ef975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xAs4kPkpTkiCH1a991yca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 22071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4271,
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

_source line 52 · 2026-05-11T21:24:58.108Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XSM1ymhqSEy7p3kRULmTYJ`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/issues/10646",
  "prompt": "Extract the full RFC discussion about KV cache compaction support in vLLM: what was proposed, current status, which approaches were discussed, and whether this has been implemented or is still open."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5c8adc5-0500-4cf3-8b4b-ec4cc04ef975",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVBpfC4Ehe7nX8PajzW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0099ab8d-1ba8-4849-9bc6-70a53bd12d2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xAs4kPkpTkiCH1a991yca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 22071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4271,
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

_source line 53 · 2026-05-11T21:24:59.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S7gHHGKo4gXjWu63SVhH5f`</summary>

```json
{
  "query": "TensorRT-LLM KV cache management multi-turn agent reuse 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0099ab8d-1ba8-4849-9bc6-70a53bd12d2d",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVBpfC4Ehe7nX8PajzW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31e51400-c246-4f10-af11-9df58d7a1cc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xAs4kPkpTkiCH1a991yca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 22071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4271,
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

_source line 54 · 2026-05-11T21:25:00.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0182KXqVkGQPSSWswoH92vA5`</summary>

```json
{
  "query": "github Kaleemullahqasim KV-Direct residual stream checkpointing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31e51400-c246-4f10-af11-9df58d7a1cc6",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVBpfC4Ehe7nX8PajzW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "959238fc-62c0-4de1-b4ee-fdc4eabf573b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xAs4kPkpTkiCH1a991yca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 22071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4271,
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

_source line 55 · 2026-05-11T21:25:00.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017u9AyZFaE8wB8MqSaaU8aM`</summary>

```json
{
  "query": "github KVFlow prefix caching multi-agent workflow LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "959238fc-62c0-4de1-b4ee-fdc4eabf573b",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVBpfC4Ehe7nX8PajzW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ae1df29-c498-4367-a3db-07cde5730a01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xAs4kPkpTkiCH1a991yca",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 22071,
      "output_tokens": 497,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4271
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 497,
          "cache_read_input_tokens": 22071,
          "cache_creation_input_tokens": 4271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4271,
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

_source line 56 · 2026-05-11T21:25:00.685Z_

<details><summary>↩ Tool result · `toolu_01CfSZTKscawEpfJiGsdKoVu`</summary>

```text
# Multi-TurboQuant Repository Summary

**Repository Description:**
"Unified KV cache compression toolkit for LLM inference" that provides twelve different compression methods under one API for optimizing large language model inference.

**Star Count:** 22 stars

**Compression Methods Implemented:**
The toolkit includes 12 methods across 5 families:
- **TurboQuant family:** turbo2, turbo3, turbo4 (Walsh-Hadamard transforms, 2.25-4.25 bits)
- **TCQ family:** turbo2_tcq, turbo3_tcq (with Viterbi trellis encoding)
- **IsoQuant:** iso3, iso4 (quaternion-based 4D rotations, no calibration needed)
- **PlanarQuant:** planar3, planar4 (Givens 2D rotations, no calibration needed)
- **RotorQuant:** rotor3, rotor4 (Clifford algebra SO(3) operations)
- **TriAttention:** Token eviction method achieving 10-16x compression

**Multi-Agent & Multi-Turn Features:**
The library includes a dedicated capacity planner supporting multi-agent deployments. Key features include preset configurations like "agents_8x16k" (8 agents at 16K context) and "agents_4x8k_70b" (4 agents on 70B models), plus automated planning across any number of GPUs with tensor-splitting and parallel slot management.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5141c62-0c03-4351-9d9e-ada85e395ab1",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "f103844a-ca37-45c2-94fb-65bbffdd56a3",
  "sourceToolAssistantUUID": "b5141c62-0c03-4351-9d9e-ada85e395ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-11T21:25:02.235Z_

<details><summary>↩ Tool result · `toolu_015Rc4qJjQj5JEZayg95HG1o`</summary>

```text
# llm-d-kv-cache Repository Analysis

**Repository Description:**
This project provides "Distributed KV cache scheduling & offloading libraries" designed to optimize LLM inference through intelligent caching mechanisms.

**Star Count:** 141 stars

**Key Implementations for Distributed KV Cache Management:**

1. **KV-Cache Indexer**: A high-performance library maintaining "a global, near-real-time view of KV-Cache block locality across a fleet of vLLM pods." It tracks which blocks reside on specific nodes and storage tiers (GPU or CPU).

2. **KV-Cache Aware Routing**: Enables schedulers to make "optimal, KV-cache-aware placement decisions" by scoring pods based on cached block availability.

3. **Event-Driven Architecture**: Processes KVEvents from vLLM instances to monitor real-time creation and eviction of cache blocks.

4. **Storage Connectors**: Includes an llmd-fs-backend for moving KV-cache blocks between GPU and shared storage systems.

5. **Kubernetes Integration**: Features a PVC Evictor utility for automatic disk space management on persistent volumes.

**Relevance to Agent Workflows:**

This repository has limited direct relevance to agent workflows. It focuses on LLM inference optimization through cache management. However, it could indirectly support agent systems by reducing latency and improving throughput in underlying LLM serving infrastructure that agents depend upon.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5c8adc5-0500-4cf3-8b4b-ec4cc04ef975",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "b9f8fc69-6203-4e7b-8584-2dc6a5093802",
  "sourceToolAssistantUUID": "a5c8adc5-0500-4cf3-8b4b-ec4cc04ef975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-11T21:25:03.212Z_

<details><summary>↩ Tool result · `toolu_01XSM1ymhqSEy7p3kRULmTYJ`</summary>

```text
# KV Cache Compaction Support RFC in vLLM

## Proposal Overview
User YaoJiayi opened RFC #10646 on November 25, 2024, proposing support for "KV cache compaction (i.e., token dropping)" to reduce memory usage in LLM serving, particularly for long-generation and large-batch scenarios.

## Proposed Approaches
The RFC mentions implementing recent methods including:
- **FastGen** (referenced paper: arxiv.org/pdf/2310.01801)
- **DuoAttention** (referenced paper: arxiv.org/abs/2410.10819)
- A flexible interface for custom compaction implementations

## Required Changes
Three main requirements were outlined:
1. "Expose intermediate logits (i.e. attetnion weights) from attention kernels"
2. Implement `free_and_reallocate` functionality to minimize memory fragmentation
3. Support non-uniform memory layouts across heads and layers, as some methods require selective token dropping

## Current Status
**Closed as Not Planned** with a "stale" label (over 90 days of inactivity). A prototype was referenced at the LMCache repository, but no implementation appears to have been merged into the main vLLM codebase based on the issue status.

## Conclusion
This RFC remains an unfulfilled feature request, suggesting KV cache compaction is not yet natively supported in vLLM's standard distribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0099ab8d-1ba8-4849-9bc6-70a53bd12d2d",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "5a8ab49a-e916-4c25-8169-1fe73ef8bce7",
  "sourceToolAssistantUUID": "0099ab8d-1ba8-4849-9bc6-70a53bd12d2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-11T21:25:07.309Z_

<details><summary>↩ Tool result · `toolu_0182KXqVkGQPSSWswoH92vA5`</summary>

```text
Web search results for query: "github Kaleemullahqasim KV-Direct residual stream checkpointing"

Links: [{"title":"GitHub - Kaleemullahqasim/KV-Direct: KV-Direct: Bounded-Memory Transformer Inference via Residual Stream Checkpointing · GitHub","url":"https://github.com/Kaleemullahqasim/KV-Direct"},{"title":"[2603.19664] The Residual Stream Is All You Need: On the Redundancy of the KV Cache in Transformer Inference","url":"https://arxiv.org/abs/2603.19664"},{"title":"(PDF) The Residual Stream Is All You Need: On the Redundancy of the KV Cache in Transformer Inference","url":"https://www.researchgate.net/publication/403032170_The_Residual_Stream_Is_All_You_Need_On_the_Redundancy_of_the_KV_Cache_in_Transformer_Inference"},{"title":"The Residual Stream Is All You Need: On the Redundancy of the KV Cache in Transformer Inference","url":"https://arxiv.org/html/2603.19664"},{"title":"Universal Checkpointing: Efficient and Flexible Checkpointing for Large Scale Distributed Training","url":"https://minjiazhang.github.io/ucp.github.io/"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference","url":"https://arxiv.org/html/2509.04377v1"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"Towards 10 Million Context Length LLM Inference with KV ...","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/neurips-2024-kvquant.pdf"},{"title":"Enable Partial Prompt Cache Reuse for Recurrent Models via State Checkpointing · ggml-org/llama.cpp · Discussion #19264","url":"https://github.com/ggml-org/llama.cpp/discussions/19264"},{"title":"NeurIPS Poster KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization","url":"https://neurips.cc/virtual/2024/poster/96936"}]

Based on the search results, I found detailed information about the KV-Direct project by Kaleemullahqasim:

## KV-Direct: Bounded-Memory Transformer Inference via Residual Stream Checkpointing

KV-Direct is a bounded-memory inference scheme that replaces evicted KV entries with residual checkpoints and recomputes keys and values on demand.

### Key Innovation

The research proves that the key-value (KV) cache state is entirely redundant: keys and values at every layer are deterministic projections of the residual stream, and recomputing them from a single residual vector per token incurs exactly zero reconstruction error, not approximately, but bit-identically.

### Performance Benefits

Over 20 conversation turns, KV-Direct bounds peak memory to 42 MB while the standard cache grows past 103 MB. Compared with five eviction baselines, KV-Direct preserves 100% token match at every cache budget; all baselines degrade to 5-28%.

Recomputation from checkpoints runs up to 5x faster than reading cached tensors at moderate batch sizes, showing that the assumed computation-memory tradeoff can be inverted.

### Memory Efficiency

KV-Direct checkpoints residual vectors (5 KB per token on Gemma 3-4B) instead of full KV pairs (136 KB), recomputing keys and values on demand.

The code is available at the GitHub repository: https://github.com/Kaleemullahqasim/KV-Direct


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "959238fc-62c0-4de1-b4ee-fdc4eabf573b",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "94fd7b1f-1ef6-4f0b-b7ed-9d44de4e37f5",
  "sourceToolAssistantUUID": "959238fc-62c0-4de1-b4ee-fdc4eabf573b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-11T21:25:07.866Z_

<details><summary>↩ Tool result · `toolu_01S7gHHGKo4gXjWu63SVhH5f`</summary>

```text
Web search results for query: "TensorRT-LLM KV cache management multi-turn agent reuse 2025 2026"

Links: [{"title":"KV cache reuse — TensorRT-LLM","url":"https://nvidia.github.io/TensorRT-LLM/advanced/kv-cache-reuse.html"},{"title":"KV Cache System — TensorRT LLM","url":"https://nvidia.github.io/TensorRT-LLM/latest/features/kvcache.html"},{"title":"Introducing New KV Cache Reuse Optimizations in NVIDIA TensorRT-LLM | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/"},{"title":"CacheTTL: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://arxiv.org/html/2511.02230v4"},{"title":"5x Faster Time to First Token with NVIDIA TensorRT-LLM KV Cache Early Reuse | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/5x-faster-time-to-first-token-with-nvidia-tensorrt-llm-kv-cache-early-reuse/"},{"title":"Releases · NVIDIA/TensorRT-LLM","url":"https://github.com/NVIDIA/TensorRT-LLM/releases"},{"title":"Triton + TensorRT-LLM (Llama 3.1 8B) – Feasibility of Stateful Serving + KV Cache Reuse + Priority Caching - JAX - NVIDIA Developer Forums","url":"https://forums.developer.nvidia.com/t/triton-tensorrt-llm-llama-3-1-8b-feasibility-of-stateful-serving-kv-cache-reuse-priority-caching/343960"},{"title":"[2511.02230] Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://arxiv.org/abs/2511.02230"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://arxiv.org/html/2507.07400v1"}]

Based on the search results, here's what I found regarding TensorRT-LLM KV cache management for multi-turn agent workloads:

## KV Cache Reuse in TensorRT-LLM

TensorRT-LLM supports KV cache reuse where KV cache pages can be shared and reused by requests that start with the same prompt, which can greatly lower first token latency. The KV cache stores previously computed key-value pairs for reuse during generation to avoid redundant calculations, and the TensorRT LLM KV cache system supports reuse across requests using tools like offloading and prioritized eviction to increase reuse.

## Multi-Turn Agent Challenges (2025-2026)

Recent research highlights specific challenges with multi-turn agentic workloads. For agentic workloads which interleave LLM calls with tools, traditional KV cache eviction policies introduce pauses that prevent effective KV reuse across turns. Most modern agentic workloads follow the ReAct-agent loop, alternating between reasoning steps and action steps with external tools.

An important trend is that agentic applications increasingly scale this loop into long-horizon, multi-turn iterations, repeatedly interleaving thought, tool call, and context update across dozens or even hundreds of turns.

## Recent Optimizations (2025)

TensorRT-LLM introduces priority-based KV cache eviction, allowing users to specify priority and duration for discrete token ranges, improving cache hit rates by around 20%. The KV cache event API enables tracking updates to the KV cache and facilitating KV-aware routing decisions.

NVIDIA TensorRT-LLM offers three key features to optimize KV cache reuse: early KV cache reuse, flexible KV cache block sizing, and efficient KV cache eviction protocols. Early KV cache reuse enables sharing of system prompts across users during a surge in interactions, accelerating inference by up to 5x.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31e51400-c246-4f10-af11-9df58d7a1cc6",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "aa2c6303-5fc1-4304-a0e8-90a004141d22",
  "sourceToolAssistantUUID": "31e51400-c246-4f10-af11-9df58d7a1cc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-11T21:25:10.814Z_

<details><summary>↩ Tool result · `toolu_017u9AyZFaE8wB8MqSaaU8aM`</summary>

```text
Web search results for query: "github KVFlow prefix caching multi-agent workflow LLM"

Links: [{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM- ...","url":"https://arxiv.org/pdf/2507.07400"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows | OpenReview","url":"https://openreview.net/forum?id=5Iw1nDtYmT"},{"title":"[2507.07400] KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://arxiv.org/abs/2507.07400"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://arxiv.org/html/2507.07400"},{"title":"NeurIPS Poster KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://neurips.cc/virtual/2025/poster/119883"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250707400P/abstract"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/c8adae36c42059677552b1255da2411e2839f58a.pdf"},{"title":"(PDF) KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://www.researchgate.net/publication/393586543_KVFlow_Efficient_Prefix_Caching_for_Accelerating_LLM-Based_Multi-Agent_Workflows"},{"title":"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/html/2603.04428"},{"title":"KV-Cache Wins You Can See: From Prefix Caching in vLLM to Distributed Scheduling with llm-d | llm-d","url":"https://llm-d.ai/blog/kvcache-wins-you-can-see"}]

Based on the search results, here's what I found about KVFlow:

## KVFlow: Efficient Prefix Caching for LLM-Based Multi-Agent Workflows

KVFlow is a workflow-aware KV cache management framework tailored for agentic workloads. LLM-based agentic workflows coordinate multiple specialized agents to solve complex tasks, and existing systems employ prefix caching to reuse key-value (KV) tensors corresponding to agents' fixed prompts.

### The Problem It Solves

Current systems typically evict KV caches using a Least Recently Used (LRU) policy, which fails to anticipate future agent usage and often discards KV caches shortly before their reuse, leading to frequent cache misses and substantial recomputation or swapping overhead.

### Key Features

KVFlow abstracts the agent execution schedule as an Agent Step Graph and assigns each agent a steps-to-execution value that estimates its temporal proximity to future activation. These values guide a fine-grained eviction policy at the KV node level and KVFlow introduces a fully overlapped KV prefetching mechanism, which proactively loads required tensors from CPU to GPU in background threads for agents scheduled in the next step.

### Performance Results

Compared to SGLang with hierarchical radix cache, KVFlow achieves up to 1.83× speedup for single workflows with large prompts, and up to 2.19× speedup for scenarios with many concurrent workflows.

The research was published in July 2025 and is available through arxiv and academic venues like NeurIPS.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ae1df29-c498-4367-a3db-07cde5730a01",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "8f65cf0f-3251-4ef2-9370-520d744c0230",
  "sourceToolAssistantUUID": "1ae1df29-c498-4367-a3db-07cde5730a01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-11T21:25:14.768Z_

Let me get the remaining repo details and search for a couple more items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f65cf0f-3251-4ef2-9370-520d744c0230",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVDMxePSZuaHyZYZKUQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9375dc7-762a-45bd-8db9-984e62d4ff50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THUKZXY5qW29Q4bVEVUS3R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4713,
      "cache_read_input_tokens": 26342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4713,
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

_source line 63 · 2026-05-11T21:25:16.978Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Hkzt8pP5qUgJSKATsBz9Sw`</summary>

```json
{
  "url": "https://github.com/Kaleemullahqasim/KV-Direct",
  "prompt": "Extract: star count, repository description, what it implements, programming language, and whether code is actually present or just a placeholder."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9375dc7-762a-45bd-8db9-984e62d4ff50",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVDMxePSZuaHyZYZKUQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da9d011e-5f99-4f8d-a175-f337aa3fa3a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THUKZXY5qW29Q4bVEVUS3R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4713,
      "cache_read_input_tokens": 26342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4713,
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

_source line 64 · 2026-05-11T21:25:17.640Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018j7uvRwNYqd17ykMaC212C`</summary>

```json
{
  "query": "github KVCOMM cross-context KV cache communication multi-agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da9d011e-5f99-4f8d-a175-f337aa3fa3a7",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVDMxePSZuaHyZYZKUQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59f936c5-3255-481f-8063-da1c69f8d0e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THUKZXY5qW29Q4bVEVUS3R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4713,
      "cache_read_input_tokens": 26342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4713,
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

_source line 65 · 2026-05-11T21:25:18.110Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NAdXGoPg19RymVBd1rjoCk`</summary>

```json
{
  "query": "github \"agent memory\" \"KV cache\" persistent edge device multi-agent Q4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59f936c5-3255-481f-8063-da1c69f8d0e7",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVDMxePSZuaHyZYZKUQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96237c5b-a8f0-4089-b128-8b4fdf6c6a33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THUKZXY5qW29Q4bVEVUS3R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4713,
      "cache_read_input_tokens": 26342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4713,
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

_source line 66 · 2026-05-11T21:25:19.973Z_

<details><summary>↩ Tool result · `toolu_01Hkzt8pP5qUgJSKATsBz9Sw`</summary>

```text
# KV-Direct Repository Analysis

**Star Count:** 8 stars

**Repository Description:** "KV-Direct: Bounded-Memory Transformer Inference via Residual Stream Checkpointing"

**What It Implements:** A memory-efficient inference scheme for transformer models that replaces evicted key-value cache entries with residual stream checkpoints. The method achieves a 27x memory reduction per token (5 KB vs. 136 KB) while maintaining 100% token accuracy during autoregressive decoding.

**Programming Language:** Not explicitly specified in the provided content.

**Code Status:** Placeholder only. The README explicitly states: "Code and experimental scripts are coming soon. Stay tuned." The repository contains only documentation files (README.md and MethodDiagram.png) with no actual implementation code present.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da9d011e-5f99-4f8d-a175-f337aa3fa3a7",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "7051a3db-d844-49c2-907b-3ae856be2fc5",
  "sourceToolAssistantUUID": "da9d011e-5f99-4f8d-a175-f337aa3fa3a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-11T21:25:20.905Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KHGpyis7by3bKDS4CGeVAc`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/issues/12254",
  "prompt": "Extract the RFC discussion about sparse KV cache management framework in vLLM: what was proposed, current status, and which compression methods it would support."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7051a3db-d844-49c2-907b-3ae856be2fc5",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVDMxePSZuaHyZYZKUQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1da5f373-02a7-4555-9141-25ca9a1d7ede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THUKZXY5qW29Q4bVEVUS3R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4713,
      "cache_read_input_tokens": 26342,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4713
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 332,
          "cache_read_input_tokens": 26342,
          "cache_creation_input_tokens": 4713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4713,
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

_source line 68 · 2026-05-11T21:25:26.264Z_

<details><summary>↩ Tool result · `toolu_01NAdXGoPg19RymVBd1rjoCk`</summary>

```text
Web search results for query: "github "agent memory" "KV cache" persistent edge device multi-agent Q4"

Links: [{"title":"[2603.04428] Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/abs/2603.04428"},{"title":"GitHub - yshk-mxim/agent-memory: Persistent KV cache for multi-agent LLM systems on Apple Silicon · GitHub","url":"https://github.com/yshk-mxim/agent-memory"},{"title":"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/html/2603.04428v1"},{"title":"Persistent Q4 KV Cache for Multi-Agent LLM Inference on ...","url":"https://arxiv.org/pdf/2603.04428"},{"title":"GitHub - rohitg00/agentmemory: #1 Persistent memory for AI coding agents based on real-world benchmarks · GitHub","url":"https://github.com/rohitg00/agentmemory"},{"title":"AgenTEE: Confidential LLM Agent Execution on Edge Devices","url":"https://agentee-paper.github.io/"},{"title":"GitHub - TsinghuaC3I/Awesome-Memory-for-Agents: A Collection of Papers about Memory for Language Agents · GitHub","url":"https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents"},{"title":"GitHub - agentscope-ai/ReMe: ReMe: Memory Management Kit for Agents - Remember Me, Refine Me. · GitHub","url":"https://github.com/agentscope-ai/ReMe"},{"title":"GitHub - VoltAgent/awesome-ai-agent-papers: A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, and autonomous systems. · GitHub","url":"https://github.com/VoltAgent/awesome-ai-agent-papers"},{"title":"GitHub - TeleAI-UAGI/Awesome-Agent-Memory: Curated systems, benchmarks, and papers etc. on memory for LLMs/MLLMs --- long-term context, retrieval, and reasoning. · GitHub","url":"https://github.com/TeleAI-UAGI/Awesome-Agent-Memory"}]

I found highly relevant results for your search query! The most prominent result is a research paper and open-source implementation about persistent KV cache management for multi-agent LLM systems on edge devices.

## Key Findings:

**Paper & Repository:**
The paper "Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices" addresses the memory management problem where device RAM is too small to hold every agent's KV cache simultaneously. The open-source implementation is available at https://github.com/yshk-mxim/agent-memory.

**Problem Statement:**
On Apple M4 Pro with 10.2 GB of cache budget, only 3 agents fit at 8K context in FP16, and a 10-agent workflow must constantly evict and reload caches, with every eviction forcing a full re-prefill through the model—15.7 seconds per agent at 4K context.

**Solution:**
The approach persists each agent's KV cache to disk in 4-bit quantized format and reloads it directly into the attention layer, eliminating redundant O(n) prefill computation via direct cache restoration.

**Performance Benefits:**
Q4 quantization fits 4x more agent contexts into fixed device memory than FP16. Cache restoration reduces time-to-first-token by up to 136x across different architectures.

**Compatibility:**
The agent-memory system persists KV caches to disk as Q4-quantized safetensors files, and when an agent returns with the same conversation prefix, the server reloads the cache and skips directly to decoding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96237c5b-a8f0-4089-b128-8b4fdf6c6a33",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "8806093c-029c-40d4-a143-928b6c2ef006",
  "sourceToolAssistantUUID": "96237c5b-a8f0-4089-b128-8b4fdf6c6a33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-11T21:25:27.040Z_

<details><summary>↩ Tool result · `toolu_01KHGpyis7by3bKDS4CGeVAc`</summary>

```text
# Sparse KV Cache Management Framework RFC Summary

## Proposed Solution

The RFC introduces a flexible KV cache management framework centered on a **CachePolicy interface** that "manages KV cache allocations" and generalizes cache behavior from basic token appending to sophisticated strategies like sliding window and H2O approaches.

The architecture employs two key data structures:
- **PhysicalBlockTable**: Tracks physical block IDs
- **VirtualBlockTable**: Maps tokens to blocks bidirectionally with slot and token mappings

## Core Components

Two initial concrete policies were implemented:
1. **DefaultCachePolicyBase** - Standard allocation
2. **CachePolicySlidingWindow** - "keeps context of sliding window" during both prefill and decode phases

The framework includes "per layer cache management capability" and aims to extract "attention weights from attention backend."

## Current Status

The RFC was opened January 21, 2025, with a draft PR (#11928) worked on V0. The proposal outlined four tasks:
- Unifying prefill and decode token addition methods
- Abstracting the cache policy interface
- Coordinating with the Hybrid Memory Allocator
- Obtaining attention weights from the backend

The issue is currently marked as stale (over 90 days inactive) and closed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1da5f373-02a7-4555-9141-25ca9a1d7ede",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "d39b612c-d909-48f9-b079-6e226341be94",
  "sourceToolAssistantUUID": "1da5f373-02a7-4555-9141-25ca9a1d7ede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-11T21:25:29.097Z_

<details><summary>↩ Tool result · `toolu_018j7uvRwNYqd17ykMaC212C`</summary>

```text
Web search results for query: "github KVCOMM cross-context KV cache communication multi-agent"

Links: [{"title":"GitHub - HankYe/KVCOMM: [NeurIPS'25] KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems","url":"https://github.com/HankYe/KVCOMM"},{"title":"GitHub - FastMAS/KVCOMM: [NeurIPS'25] KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems","url":"https://github.com/FastMAS/KVCOMM"},{"title":"KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems | OpenReview","url":"https://openreview.net/forum?id=yGOytgjurF"},{"title":"KVCOMM: Online Cross-context KV-cache Communication ...","url":"https://openreview.net/pdf/81561154949bf17e7f12ee6dc0485c10a2415686.pdf"},{"title":"Paper page - KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems","url":"https://huggingface.co/papers/2510.12872"},{"title":"NeurIPS Poster KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems","url":"https://neurips.cc/virtual/2025/poster/115164"},{"title":"[2510.12872] KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems","url":"https://arxiv.org/abs/2510.12872"},{"title":"KVComm: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems","url":"https://arxiv.org/html/2510.12872v1"},{"title":"[2510.12872v1] KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems","url":"https://arxiv.org/abs/2510.12872v1"},{"title":"GitHub - Zephyroam/KVComm: [ICLR 2026] KVComm: Enabling Efficient LLM Communication through Selective KV Sharing · GitHub","url":"https://github.com/Zephyroam/KVComm"}]

Based on the search results, here's what I found about KVCOMM:

## Overview

KVCOMM is a novel adaptive serving paradigm for LLM-based Multi-agent Systems, which highlights the online cross-context KV-cache reuse for the shared text among dependent LLM agents. It was published at NeurIPS'25 (The Thirty-Ninth Annual Conference on Neural Information Processing Systems).

## The Problem

Multi-agent LLM systems suffer substantial overhead from repeated reprocessing of overlapping contexts across agents, as once an agent receives a message from its predecessor, the full context must be reprocessed from scratch. While key-value (KV) caching is effective in single-agent settings where prefixes remain unchanged, it cannot be directly reused in multi-agent scenarios due to diverging prefixes introduced by agent-specific context extensions.

## The Solution

KVCOMM is a training-free framework that enables efficient prefilling in multi-agent inference by reusing KV-caches and aligning cache offsets of overlapping contexts under diverse prefix contexts, by estimating and adjusting KV-caches for shared content through referencing a pool of cached examples—termed anchors—that store observed cache deviations under varying prefixes.

## Performance

KVCOMM achieves over 70% reuse rate across diverse multi-agent workloads, including retrieval-augmented generation, math reasoning, and collaborative coding tasks, and achieves up to 7.8× speedup compared to the standard prefill pipeline, reducing TTFT from ∼430ms to ∼55ms.

## Code Availability

Code is available at https://github.com/FastMAS/KVCOMM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59f936c5-3255-481f-8063-da1c69f8d0e7",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "b2705819-930c-4df7-af90-40688a27fb77",
  "sourceToolAssistantUUID": "59f936c5-3255-481f-8063-da1c69f8d0e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-11T21:25:32.925Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016nL9JsmVrdq9F5PXJPUNPo`</summary>

```json
{
  "url": "https://github.com/yshk-mxim/agent-memory",
  "prompt": "Extract: star count, repository description, what it implements, programming language, supported models, and how it handles multi-agent KV cache persistence and Q4 quantization."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2705819-930c-4df7-af90-40688a27fb77",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVEi8ruM1xoxzRMJXtD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "728565ea-a273-422c-be3c-dd0b34e4da74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSsmgNRyDRF8EWaYch5DLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1330,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 31055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1684,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-11T21:25:34.235Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EVA7EBzT9dSEMeMxfFhNew`</summary>

```json
{
  "url": "https://github.com/FastMAS/KVCOMM",
  "prompt": "Extract: star count, repository description, what it implements, programming language, and how it enables cross-context KV cache reuse in multi-agent systems."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "728565ea-a273-422c-be3c-dd0b34e4da74",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVEi8ruM1xoxzRMJXtD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9903349-363a-4475-869c-a6bdc7d17a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSsmgNRyDRF8EWaYch5DLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1330,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 31055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1684,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-11T21:25:35.510Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01A6cT1doB2CZsCHPDx3sFbv`</summary>

```json
{
  "url": "https://github.com/Zefan-Cai/KVCache-Factory",
  "prompt": "Extract: star count, repository description, what compression methods it implements, programming language, and whether it supports online/incremental compression."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9903349-363a-4475-869c-a6bdc7d17a4c",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVEi8ruM1xoxzRMJXtD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef1c43ed-2357-4cc5-9eb6-455481d5510c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSsmgNRyDRF8EWaYch5DLX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1330,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 31055,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1684
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1330,
          "output_tokens": 314,
          "cache_read_input_tokens": 31055,
          "cache_creation_input_tokens": 1684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1684,
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

_source line 74 · 2026-05-11T21:25:38.344Z_

<details><summary>↩ Tool result · `toolu_016nL9JsmVrdq9F5PXJPUNPo`</summary>

```text
# Agent-Memory Repository Summary

**Star Count:** 11 stars

**Repository Description:** "Persistent KV cache for multi-agent LLM systems on Apple Silicon"

**Programming Language:** Python (98.9%)

**Core Implementation:**
The project implements a persistent key-value cache system designed to accelerate multi-agent LLM inference. Rather than recomputing attention caches from scratch for each request, it stores quantized KV caches to disk, enabling rapid reloads when agents return with matching conversation prefixes.

**Supported Models:**
- Gemma 3 12B IT (Q4, 6.5 GB)
- DeepSeek-Coder-V2-Lite (Q4, 8 GB)
- Llama 3.1 8B Instruct (Q4, 4.5 GB)

**Multi-Agent KV Cache Persistence & Q4 Quantization:**
The system uses a three-tier cache architecture: hot caches in GPU memory, warm metadata caches, and cold caches persisted as Q4-quantized safetensors files on disk. The "Block Pool Batch Engine" manages memory budgets and evicts least-recently-used caches. Quantization reduces storage overhead by approximately 75% while introducing roughly 3% perplexity impact. Performance gains range from 4.4x to 35.3x faster time-to-first-token on cache hits, depending on context length.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "728565ea-a273-422c-be3c-dd0b34e4da74",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "44d1b445-bee1-4395-bab5-8026b14df409",
  "sourceToolAssistantUUID": "728565ea-a273-422c-be3c-dd0b34e4da74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-11T21:25:38.828Z_

<details><summary>↩ Tool result · `toolu_01A6cT1doB2CZsCHPDx3sFbv`</summary>

```text
# KVCache-Factory Repository Summary

**Star Count:** 1.3k stars

**Repository Description:** "Unified KV Cache Compression Methods for Auto-Regressive Models"

**Compression Methods Implemented:** The repository supports four primary techniques:
- PyramidKV
- SnapKV
- H2O
- StreamingLLM

**Programming Language:** Python (98.4%)

**Online/Incremental Compression Support:** The codebase does not explicitly support online or incremental compression. The TODO section lists "Support KV cache compression at decoding stage" as a future enhancement, indicating this capability is not yet available. Current implementations appear to focus on compression during the inference phase rather than dynamic, streaming compression.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef1c43ed-2357-4cc5-9eb6-455481d5510c",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "03d082bb-07c6-44ac-9009-65cd9c6a8494",
  "sourceToolAssistantUUID": "ef1c43ed-2357-4cc5-9eb6-455481d5510c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-11T21:25:39.298Z_

<details><summary>↩ Tool result · `toolu_01EVA7EBzT9dSEMeMxfFhNew`</summary>

```text
# KVCOMM Repository Analysis

**Star Count:** 162 stars

**Repository Description:** 
"[NeurIPS'25] KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems"

**Programming Language:** Python (100%)

**What It Implements:**
KVCOMM is a serving paradigm that optimizes LLM-based multi-agent systems through intelligent cache management. The system achieves "over 70% reuse rate across diverse multi-agent workloads" including retrieval-augmented generation, mathematical reasoning, and collaborative coding tasks. Performance gains are substantial, with the paper reporting "up to 7.8× speedup" in time-to-first-token metrics on single H100 GPUs.

**How It Enables Cross-Context KV Cache Reuse:**
The approach operates through three key mechanisms:

1. **Anchor Matching:** Identifies nearest anchors (cached examples) for requested content segments
2. **Offset Approximation:** Predicts cache deviations by weighting stored anchor variations
3. **Anchor Prediction:** Determines whether newly-generated caches can be shared or should become new anchors

The system maintains "a pool of cached examples—termed anchors—that store observed cache deviations under varying prefixes" and updates dynamically based on incoming requests and context structures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9903349-363a-4475-869c-a6bdc7d17a4c",
  "isSidechain": true,
  "promptId": "9d92b139-0e57-4366-ae79-a6326d2c2517",
  "agentId": "a1745bfe9686c9b9a",
  "type": "user",
  "uuid": "84611acd-7cee-4698-8e98-789440a40854",
  "sourceToolAssistantUUID": "b9903349-363a-4475-869c-a6bdc7d17a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-11T21:27:34.968Z_

Now I have comprehensive data. Let me compile the full report.

---

## Comprehensive Report: KV Cache Compaction Implementations and Building Blocks for LLM Agent Inference

### 1. DIRECT KV COMPACTION / COMPRESSION IMPLEMENTATIONS

#### A. adamzweiger/compaction -- Attention Matching
- **URL:** https://github.com/adamzweiger/compaction
- **Stars:** 217
- **What it implements:** "Fast KV Compaction via Attention Matching" (arXiv 2602.16284, Zweiger et al. 2026). Constructs a smaller set of keys and values in latent space that reproduce the original attention behavior. Uses Orthogonal Matching Pursuit (AM-OMP) and pseudoinverse-based methods to achieve up to 200x total compaction when combined with summarization. Forms the Pareto frontier for speed-quality tradeoff, outperforming token-selection baselines.
- **Language:** Python (93.5%)
- **Building block potential:** HIGH. This is the most promising single algorithm for between-tool-call compaction. It operates directly in latent space (no decompression needed), is training-free, and could in principle be applied incrementally to the KV cache accumulated after each tool call. However, the current implementation is batch-mode only (compacts a prefilled cache), so integration work is needed for incremental use. There is also an open issue on llama.cpp (ggml-org/llama.cpp#20037) requesting integration but no PR yet.

#### B. NVIDIA/kvpress
- **URL:** https://github.com/NVIDIA/kvpress
- **Stars:** 1,100
- **What it implements:** A comprehensive library of 30+ KV cache compression "presses" built on HuggingFace Transformers. Includes scoring-based methods (SnapKV, StreamingLLM, TOVA, ObservedAttention, ExpectedAttention, PyramidKV, etc.), dimension-based methods (ThinK, SimLayerKV, DuoAttention, KVzip), and composable wrappers.
- **Key for incremental compaction:** **DecodingPress** compresses the KV cache periodically *during* token generation with configurable `compression_interval` and `target_size`. **CAMPress** merges evicted tokens into retained tokens. **PrefillDecodingPress** combines prefill and decoding compression.
- **Language:** Python (98.4%)
- **Building block potential:** VERY HIGH. The DecodingPress and CAMPress methods are the closest existing building blocks for incremental compaction between agent tool calls. The composable architecture (ComposedPress, PerLayerCompressionPress) makes it easy to experiment with different strategies. However, it is built on HuggingFace Transformers, not on serving frameworks like vLLM/SGLang.

#### C. IsaacRe/vllm-kvcompress
- **URL:** https://github.com/IsaacRe/vllm-kvcompress
- **Stars:** 157
- **What it implements:** KV-Compress -- a paged KV cache compression technique for vLLM v0.6.0 with variable compression rates across attention heads. Supports **continual compression** (compressing during decoding, not just prefill) via `--continual-compression` flag.
- **Language:** Python (79.2%), CUDA (15.8%), C++ (2.7%)
- **Building block potential:** HIGH. This is the only existing implementation that integrates KV compaction directly into vLLM with continual compression support. However, it is pinned to vLLM v0.6.0 (now quite old -- vLLM has moved to v1 architecture). Would need significant porting work for modern vLLM.

#### D. NVlabs/RocketKV
- **URL:** https://github.com/NVlabs/RocketKV
- **Stars:** 46
- **What it implements:** Two-stage KV compression (ICML 2025). Stage 1: coarse-grain permanent token removal via SnapKV. Stage 2: fine-grain dynamic top-k attention scoring with K-tensor head-dimension compression. Achieves up to 400x compression, 3.7x speedup, 32.6% peak memory reduction.
- **Language:** Python/CUDA
- **Building block potential:** MODERATE. Strong compression ratios but no explicit incremental/online mode. The two-stage architecture could potentially be adapted for between-tool-call compaction.

#### E. ksheth96/BalanceKV
- **URL:** https://github.com/ksheth96/BalanceKV
- **Stars:** 9
- **What it implements:** NeurIPS 2025 Spotlight paper "Streaming Attention Approximation via Discrepancy Theory." Uses a balanced walk algorithm for streaming KV cache compression.
- **Language:** Python (100%)
- **Building block potential:** MODERATE-HIGH. The "streaming" aspect is relevant -- it applies compression incrementally without requiring full context access. Theoretical foundations in discrepancy theory provide formal approximation guarantees. Small community but strong academic backing.

#### F. snu-mllab/KVzip
- **URL:** https://github.com/snu-mllab/KVzip
- **Stars:** 218
- **What it implements:** NeurIPS 2025 Oral. Query-agnostic KV cache eviction with context reconstruction. 3-4x memory reduction, 2x latency decrease. Supports Qwen 2.5/3, LLaMA 3/3.1, Gemma 3.
- **Language:** Python
- **Building block potential:** HIGH for agent use case. Explicitly supports multi-turn inference with `update_cache=True` parameter. Query-agnostic design means it can compress without knowing future queries (ideal for agent tool-call boundaries). Selectively evicts KV pairs for generated tokens while retaining important context.

#### G. Zefan-Cai/KVCache-Factory
- **URL:** https://github.com/Zefan-Cai/KVCache-Factory
- **Stars:** 1,300
- **What it implements:** Unified framework for PyramidKV, SnapKV, H2O, and StreamingLLM compression methods.
- **Language:** Python (98.4%)
- **Building block potential:** LOW for incremental use. Compression during decoding is listed as a TODO. Currently prefill-only.

#### H. Kaleemullahqasim/KV-Direct
- **URL:** https://github.com/Kaleemullahqasim/KV-Direct
- **Stars:** 8
- **What it implements:** Bounded-memory inference via residual stream checkpointing. Stores 5 KB residual vectors per token instead of 136 KB full KV pairs (27x reduction). Recomputes KV on demand. Claims 100% token accuracy (zero reconstruction error) and 5x faster recomputation than reading cached tensors.
- **Language:** Placeholder only -- no code released yet ("coming soon").
- **Building block potential:** CONCEPTUALLY HIGH. Over 20 conversation turns, bounds peak memory to 42 MB vs. 103 MB for standard cache. Perfect fit for multi-turn agent scenarios. However, no code is available.

#### I. aivrar/multi-turboquant
- **URL:** https://github.com/aivrar/multi-turboquant
- **Stars:** 22
- **What it implements:** 12 quantization methods across 5 families (TurboQuant, TCQ, IsoQuant, PlanarQuant, RotorQuant) plus TriAttention token eviction. Includes a multi-agent capacity planner with presets like "agents_8x16k" and "agents_4x8k_70b."
- **Language:** Python
- **Building block potential:** MODERATE. The multi-agent capacity planner is unique and directly relevant. Quantization-based compression (2.25-4.25 bits) is complementary to token-dropping approaches.

---

### 2. AGENT-SPECIFIC KV CACHE MANAGEMENT

#### A. Hanchenli/vllm-continuum (CacheTTL / Continuum)
- **URL:** https://github.com/Hanchenli/vllm-continuum
- **Stars:** 75
- **Paper:** "Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live" (arXiv 2511.02230)
- **What it implements:** TTL-based KV cache pinning for agent tool calls on vLLM. When a request generates a tool call, the system predicts tool execution duration and decides how long to retain the KV cache in GPU memory. Achieves up to 8.18x improvements in latency and throughput.
- **Building block potential:** VERY HIGH. This is the most directly relevant project for agent-aware KV management. It integrates with vLLM and LMCache, supports sticky-session routing for multi-node, and includes SWE-bench evaluation with real agent workloads. The TTL mechanism is complementary to compaction -- you could compact the cache AND set a TTL for the compacted version.

#### B. FastMAS/KVCOMM
- **URL:** https://github.com/FastMAS/KVCOMM
- **Stars:** 162
- **Paper:** NeurIPS 2025 -- "Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems"
- **What it implements:** Cross-context KV cache reuse for multi-agent systems. Uses "anchors" to estimate cache deviations under varying prefixes, achieving 70%+ reuse rate and up to 7.8x TTFT speedup.
- **Building block potential:** MODERATE for single-agent compaction, HIGH for multi-agent scenarios. The anchor-based offset approximation is a novel approach to reusing KV caches across agents with different prefixes.

#### C. yshk-mxim/agent-memory
- **URL:** https://github.com/yshk-mxim/agent-memory
- **Stars:** 11
- **Paper:** "Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices" (arXiv 2603.04428)
- **What it implements:** Three-tier cache (hot GPU / warm metadata / cold Q4 disk) for multi-agent inference on Apple Silicon. Q4 quantization reduces storage by ~75%. Achieves 4.4x-35.3x faster TTFT on cache hits.
- **Building block potential:** MODERATE. Focused on edge/Apple Silicon. The Q4 quantized persistence is relevant for offline KV cache storage between tool calls. Supports Gemma 3 12B, DeepSeek-Coder-V2-Lite, LLaMA 3.1 8B.

#### D. KVFlow (paper only, no standalone repo found)
- **Paper:** "KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows" (arXiv 2507.07400, NeurIPS 2025)
- **What it proposes:** Workflow-aware KV cache management using an "Agent Step Graph" to predict future agent activation. Guides eviction at the KV node level and overlaps prefetching from CPU to GPU. Up to 2.19x speedup over SGLang's hierarchical radix cache.
- **Building block potential:** HIGH conceptually. The Agent Step Graph concept is directly applicable to agent orchestrators that know the workflow DAG.

---

### 3. SERVING FRAMEWORK LANDSCAPE

#### vLLM
- **KV cache management:** Block-based paged attention. Automatic Prefix Caching (APC) uses hash-based block matching to reuse KV cache for shared token prefixes. Drops TTFT from 4.3s to 0.6s on cache hits for 10K-token prompts.
- **Multi-turn support:** Prefix caching only -- reuses KV for the common prefix of conversation history. No native compaction.
- **Compaction status:** Two RFCs were opened (#10646 for KV cache compaction, #12254 for sparse KV cache management framework) -- both closed as stale/not planned. A recent feature request (#25672) for "Generalized KV cache reuse" beyond prefix caching is open.
- **Agent-aware features:** The llm-d project (141 stars) provides distributed KV cache indexing and KV-aware routing across vLLM pods.
- **Ecosystem:** LMCache (8,200 stars) extends vLLM with multi-tier KV storage (GPU/CPU/disk/S3) and non-prefix reuse.

#### SGLang
- **KV cache management:** RadixAttention -- stores KV cache entries in a radix tree. Automatically discovers caching opportunities across multi-turn conversations by walking the tree and matching prompt tokens. ~10% faster than vLLM for multi-turn workloads.
- **Multi-turn support:** Best-in-class for dynamic conversation flows. Full conversation history is matched as a prefix in the radix tree to maximize cache reuse.
- **Compression features:** FP8/FP4 quantized KV cache (3.56x more tokens with FP4 vs BF16), KV cache pruning (issue #19887), TurboQuant integration (issue #23134), KVPress integration (issue #10585). HiCache provides multi-tier storage (GPU L1, CPU L2, Mooncake L3).
- **Agent-aware features:** No native agent-aware scheduling, but RadixAttention's automatic prefix matching handles multi-turn agent conversations implicitly.

#### TensorRT-LLM
- **KV cache management:** Priority-based KV cache eviction with user-specified priority and duration for discrete token ranges. ~20% improved cache hit rates. KV cache event API for external routing.
- **Multi-turn support:** KV cache reuse for shared prefixes. "Early KV cache reuse" enables sharing system prompts during interaction surges (up to 5x TTFT improvement).
- **Agent-aware features:** Priority and duration-based cache management is the closest to agent-aware features among the three frameworks. Users can pin important cache ranges.
- **Limitations:** Closed-source core, harder to extend than vLLM/SGLang.

---

### 4. PAPER IMPLEMENTATION STATUS SUMMARY

| Paper | GitHub Repo | Stars | Code Available | Incremental Support |
|---|---|---|---|---|
| **Attention Matching** (Zweiger et al. 2026) | adamzweiger/compaction | 217 | Yes (batch mode) | No (batch only) |
| **CacheTTL / Continuum** (Li et al. 2025) | Hanchenli/vllm-continuum | 75 | Yes (vLLM fork) | Yes (TTL-based pinning) |
| **PBKV** | Not found | -- | -- | -- |
| **CacheClip** (Yang et al. 2025) | No public repo found | -- | Paper only (arXiv 2510.10129) | N/A |
| **KV-Direct** (Qasim 2026) | Kaleemullahqasim/KV-Direct | 8 | No ("coming soon") | Yes (by design) |
| **BalanceKV** (NeurIPS 2025 Spotlight) | ksheth96/BalanceKV | 9 | Yes | Yes (streaming) |
| **KVzip** (NeurIPS 2025 Oral) | snu-mllab/KVzip | 218 | Yes | Yes (update_cache) |
| **KVCOMM** (NeurIPS 2025) | FastMAS/KVCOMM | 162 | Yes | Yes (online cross-context) |
| **RocketKV** (ICML 2025) | NVlabs/RocketKV | 46 | Yes | No (prefill-time) |

Note: I could not find a specific paper or implementation called "PBKV" (page-based KV cache). The closest match may be PyramidKV (dynamic per-layer cache budgets) which is implemented in both kvpress and KVCache-Factory.

---

### 5. RECOMMENDED BUILDING BLOCKS FOR INCREMENTAL KV COMPACTION BETWEEN AGENT TOOL CALLS

**Tier 1 -- Most directly applicable:**
1. **NVIDIA/kvpress (DecodingPress + CAMPress):** Already supports periodic compression during generation with configurable intervals. CAMPress merges evicted tokens into retained ones. Composable architecture. The main gap is that it runs on HuggingFace Transformers, not serving frameworks.
2. **adamzweiger/compaction (Attention Matching):** Highest theoretical compaction quality. Could be applied at tool-call boundaries to compress the accumulated KV cache before the next turn. Needs adaptation from batch to incremental mode.
3. **snu-mllab/KVzip:** Query-agnostic eviction with multi-turn support and `update_cache=True`. Directly handles the "compress without knowing future queries" requirement of agent boundaries.

**Tier 2 -- Agent-aware scheduling (complementary):**
4. **Hanchenli/vllm-continuum (CacheTTL):** Solves the *when to keep/evict* question for agent tool calls. Best combined with a compaction method that solves the *how to compress* question.
5. **FastMAS/KVCOMM:** Solves cross-agent KV reuse. Relevant for multi-agent orchestration rather than single-agent tool-call compaction.

**Tier 3 -- Framework integration targets:**
6. **IsaacRe/vllm-kvcompress:** Proof that continual compression can work inside vLLM, but needs porting to modern vLLM v1.
7. **LMCache/LMCache:** The multi-tier storage layer. Could store compacted KV caches between tool calls across GPU/CPU/disk.

Sources:
- [adamzweiger/compaction](https://github.com/adamzweiger/compaction)
- [NVIDIA/kvpress](https://github.com/NVIDIA/kvpress)
- [IsaacRe/vllm-kvcompress](https://github.com/IsaacRe/vllm-kvcompress)
- [LMCache/LMCache](https://github.com/LMCache/LMCache)
- [NVlabs/RocketKV](https://github.com/NVlabs/RocketKV)
- [ksheth96/BalanceKV](https://github.com/ksheth96/BalanceKV)
- [snu-mllab/KVzip](https://github.com/snu-mllab/KVzip)
- [Zefan-Cai/KVCache-Factory](https://github.com/Zefan-Cai/KVCache-Factory)
- [Kaleemullahqasim/KV-Direct](https://github.com/Kaleemullahqasim/KV-Direct)
- [aivrar/multi-turboquant](https://github.com/aivrar/multi-turboquant)
- [Hanchenli/vllm-continuum](https://github.com/Hanchenli/vllm-continuum)
- [FastMAS/KVCOMM](https://github.com/FastMAS/KVCOMM)
- [yshk-mxim/agent-memory](https://github.com/yshk-mxim/agent-memory)
- [llm-d/llm-d-kv-cache-manager](https://github.com/llm-d/llm-d-kv-cache-manager)
- [vLLM KV Cache Compaction RFC #10646](https://github.com/vllm-project/vllm/issues/10646)
- [vLLM Sparse KV Cache Framework RFC #12254](https://github.com/vllm-project/vllm/issues/12254)
- [vLLM Generalized KV Cache Reuse #25672](https://github.com/vllm-project/vllm/issues/25672)
- [llama.cpp Attention Matching Issue #20037](https://github.com/ggml-org/llama.cpp/issues/20037)
- [SGLang KV Cache Pruning #19887](https://github.com/sgl-project/sglang/issues/19887)
- [SGLang KVPress Integration #10585](https://github.com/sgl-project/sglang/issues/10585)
- [Fast KV Compaction via Attention Matching (arXiv)](https://arxiv.org/abs/2602.16284)
- [CacheTTL / Continuum (arXiv)](https://arxiv.org/abs/2511.02230)
- [CacheClip (arXiv)](https://arxiv.org/abs/2510.10129)
- [KVFlow (arXiv)](https://arxiv.org/abs/2507.07400)
- [KV-Direct (arXiv)](https://arxiv.org/abs/2603.19664)
- [vLLM Prefix Caching Design](https://docs.vllm.ai/en/stable/design/prefix_caching/)
- [SGLang RadixAttention Blog](https://www.lmsys.org/blog/2024-01-17-sglang/)
- [TensorRT-LLM KV Cache Reuse](https://nvidia.github.io/TensorRT-LLM/advanced/kv-cache-reuse.html)
- [TensorRT-LLM Early KV Cache Reuse Blog](https://developer.nvidia.com/blog/5x-faster-time-to-first-token-with-nvidia-tensorrt-llm-kv-cache-early-reuse/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84611acd-7cee-4698-8e98-789440a40854",
  "isSidechain": true,
  "agentId": "a1745bfe9686c9b9a",
  "requestId": "req_011CawVFTiU9ek1NbBzGsdoE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81d9ca83-9041-4c09-8147-c71164397f86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a61503d0-f477-4b98-9571-97202616b706",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5sAgV4XqEfieiekxMQ33G",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 193,
      "cache_creation_input_tokens": 2341,
      "cache_read_input_tokens": 32739,
      "output_tokens": 5368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2341
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 193,
          "output_tokens": 5368,
          "cache_read_input_tokens": 32739,
          "cache_creation_input_tokens": 2341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2341,
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
