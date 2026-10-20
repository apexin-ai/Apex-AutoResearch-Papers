# Research conversation: Search for major ML/AI/SE conference submission deadlines that are AFTER 2026-05-10. I need venues where a paper on "exe

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a60fd13a59176a15b.jsonl`
- **Structured JSON:** [`6b6d0e1887f48155874b.json`](../../sessions/6b/6b6d0e1887f48155874b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

49 recorded events

### User

_source line 1 · 2026-05-10T17:15:51.636Z_

Search for major ML/AI/SE conference submission deadlines that are AFTER 2026-05-10. I need venues where a paper on "execution simulation as verifier for code repair scaling" would fit.

Use WebSearch to find:
1. "NeurIPS 2026 submission deadline"
2. "EMNLP 2026 submission deadline"
3. "AAAI 2027 submission deadline"
4. "ICLR 2027 submission deadline"
5. "ASE 2026 submission deadline" (Automated Software Engineering)
6. "FSE 2026 submission deadline" or "ESEC/FSE 2026"
7. "ISSTA 2026 submission deadline"
8. "ICSE 2027 submission deadline"
9. "COLM 2026 submission deadline" (Conference on Language Modeling)
10. "ACL 2026 submission deadline"

For each venue, report the exact submission deadline date and whether it's after May 10, 2026. Only include venues whose deadlines have NOT yet passed as of 2026-05-10.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "22b93466-e87e-46e9-81cf-2fc4c7b8235a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T17:15:51.640Z_

```json
{
  "parentUuid": "22b93466-e87e-46e9-81cf-2fc4c7b8235a",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
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
  "uuid": "7e095d97-e343-4837-a991-e9ef8955efe7",
  "timestamp": "2026-05-10T17:15:51.640Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T17:15:54.047Z_



I'll search for all these conference deadlines. Let me first load the WebSearch tool, then run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e095d97-e343-4837-a991-e9ef8955efe7",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPjyDy2CLhBFNmDLvv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5611099b-60f9-495d-a459-6d497a32ce8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128YDjVznir6SS4x7fB3YEw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 783,
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

_source line 4 · 2026-05-10T17:15:54.528Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RdtQQJRuErfAhEhr1D9u7s`</summary>

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
  "parentUuid": "5611099b-60f9-495d-a459-6d497a32ce8e",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPjyDy2CLhBFNmDLvv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f6e1f35-0ec6-48e8-8b6f-ee171edbcc34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128YDjVznir6SS4x7fB3YEw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 7304,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 783
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 783,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 783,
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

_source line 5 · 2026-05-10T17:15:54.531Z_

<details><summary>↩ Tool result · `toolu_01RdtQQJRuErfAhEhr1D9u7s`</summary>

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
  "parentUuid": "2f6e1f35-0ec6-48e8-8b6f-ee171edbcc34",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "3674a26b-02a8-4078-b0df-989d0a50327f",
  "sourceToolAssistantUUID": "2f6e1f35-0ec6-48e8-8b6f-ee171edbcc34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T17:15:58.085Z_



Now let me run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3674a26b-02a8-4078-b0df-989d0a50327f",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPxeDeurxGxW25DcfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b5e3bf7-6025-4aa2-be24-fc87a12a7a66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GsQcHZJuRG2JcNNQxsZs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 7 · 2026-05-10T17:15:58.629Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KTnu5CMWuhX6VFjhVgr4Xp`</summary>

```json
{
  "query": "NeurIPS 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b5e3bf7-6025-4aa2-be24-fc87a12a7a66",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPxeDeurxGxW25DcfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76228ebe-65ac-409e-9286-8dbef1726e8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GsQcHZJuRG2JcNNQxsZs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 8 · 2026-05-10T17:15:58.635Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QDRPUFYJpZHH3Jp3nazS6o`</summary>

```json
{
  "query": "EMNLP 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76228ebe-65ac-409e-9286-8dbef1726e8b",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPxeDeurxGxW25DcfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7510e638-f7aa-46f1-a2e9-2ab6ce76e413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GsQcHZJuRG2JcNNQxsZs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 9 · 2026-05-10T17:15:59.125Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013f52ZqJ65KE23gR6wDQcyu`</summary>

```json
{
  "query": "AAAI 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7510e638-f7aa-46f1-a2e9-2ab6ce76e413",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPxeDeurxGxW25DcfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3b438d6-892b-44d2-9053-1cdec96390ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GsQcHZJuRG2JcNNQxsZs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 10 · 2026-05-10T17:15:59.740Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QffcDo586bRNZuRHQKyhtz`</summary>

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
  "parentUuid": "b3b438d6-892b-44d2-9053-1cdec96390ea",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPxeDeurxGxW25DcfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38ca422d-f1de-4e44-afa3-d9eb016e44da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GsQcHZJuRG2JcNNQxsZs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 11 · 2026-05-10T17:16:00.055Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LWDu25XQc1qBgkB194nBEf`</summary>

```json
{
  "query": "ASE 2026 submission deadline automated software engineering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38ca422d-f1de-4e44-afa3-d9eb016e44da",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPxeDeurxGxW25DcfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d859275d-07a7-4581-838c-1ffdd3908381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GsQcHZJuRG2JcNNQxsZs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 12 · 2026-05-10T17:16:00.555Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CSZWZ69TYe1NbE4r1Kmoog`</summary>

```json
{
  "query": "FSE 2026 submission deadline ESEC/FSE 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d859275d-07a7-4581-838c-1ffdd3908381",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPxeDeurxGxW25DcfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99a3c0a7-c97b-4343-b3ca-ac734917898a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GsQcHZJuRG2JcNNQxsZs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 13 · 2026-05-10T17:16:00.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JV9o2jN9eVGDwcEFvYyjJA`</summary>

```json
{
  "query": "ISSTA 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99a3c0a7-c97b-4343-b3ca-ac734917898a",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPxeDeurxGxW25DcfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8708a5fb-0c88-424a-88f4-908d8e8d07f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GsQcHZJuRG2JcNNQxsZs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 14 · 2026-05-10T17:16:01.452Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CqhhWw8Wv5riyJePGTpyxi`</summary>

```json
{
  "query": "ICSE 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8708a5fb-0c88-424a-88f4-908d8e8d07f3",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPxeDeurxGxW25DcfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4ffcdde-17b2-4c0a-a21c-ca67c758a6cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GsQcHZJuRG2JcNNQxsZs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

### Tool result

_source line 15 · 2026-05-10T17:16:01.667Z_

<details><summary>↩ Tool result · `toolu_01KTnu5CMWuhX6VFjhVgr4Xp`</summary>

```text
Web search results for query: "NeurIPS 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"NeurIPS 2026 Conference | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FConference"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"2026 Conference","url":"https://neurips.cc/Conferences/2026"},{"title":"NeurIPS Conference (@NeurIPSConf) / X","url":"https://x.com/NeurIPSConf"},{"title":"NeurIPS: Neural Information Processing Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2212"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"}]

Based on the search results, here are the key submission deadlines for NeurIPS 2026:

Abstract submission deadline: May 4, 2026 (AOE)

Full paper submission deadline, including all supplementary materials: May 6, 2026 AOE

Note that the different tracks (main, evaluations and datasets, position papers) have different calls for papers, different submission portals, and possibly different timelines.

The conference will be held December 6th through 12th, 2026 at the International Convention Centre.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76228ebe-65ac-409e-9286-8dbef1726e8b",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "f140fd29-1dab-4e4b-9abd-6bfdb09c3ea0",
  "sourceToolAssistantUUID": "76228ebe-65ac-409e-9286-8dbef1726e8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-10T17:16:01.948Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016hamPKCqfEaWymMBJbftTS`</summary>

```json
{
  "query": "COLM 2026 submission deadline conference on language modeling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f140fd29-1dab-4e4b-9abd-6bfdb09c3ea0",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPxeDeurxGxW25DcfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0db87e2-984e-4b2a-be00-b26669704c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GsQcHZJuRG2JcNNQxsZs4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
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

_source line 17 · 2026-05-10T17:16:02.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VedpQKsnCzcCruGSFu9kUp`</summary>

```json
{
  "query": "ACL 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0db87e2-984e-4b2a-be00-b26669704c75",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGPxeDeurxGxW25DcfF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f7c47b2-4b59-4ad8-9ee0-f8cbe0bfa8a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GsQcHZJuRG2JcNNQxsZs4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 8087,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 479,
          "cache_read_input_tokens": 8087,
          "cache_creation_input_tokens": 1421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1421,
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

_source line 18 · 2026-05-10T17:16:02.941Z_

<details><summary>↩ Tool result · `toolu_013f52ZqJ65KE23gR6wDQcyu`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's what I found about the AAAI 2027 submission deadline:

The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027. However, the AAAI 2027 paper submission deadline is TBD (to be determined).

Submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns, but the official deadline has not yet been announced. For the most current information, you can check the official AAAI conference website at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3b438d6-892b-44d2-9053-1cdec96390ea",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "49cb1884-c9f1-4baa-92f0-1e80ddb44215",
  "sourceToolAssistantUUID": "b3b438d6-892b-44d2-9053-1cdec96390ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T17:16:03.612Z_

<details><summary>↩ Tool result · `toolu_01QffcDo586bRNZuRHQKyhtz`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline"

Links: [{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, I was unable to find specific information about the ICLR 2027 submission deadline. The search results primarily contain information about ICLR 2026 and other conferences, but do not include details about ICLR 2027's submission deadline.

The most recent information available is for ICLR 2026, which had a deadline for paper submissions on September 24.

To find the ICLR 2027 submission deadline, I recommend:
1. Checking the official ICLR website (iclr.cc) when the call for papers is announced
2. Monitoring AI conference deadline trackers like those mentioned in the search results
3. Keeping an eye on OpenReview, which is where submissions to ICLR are uploaded

The 2027 conference dates and deadlines are likely to be announced in the coming months as the conference planning progresses.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38ca422d-f1de-4e44-afa3-d9eb016e44da",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "dab008bc-e40b-4770-969f-6875e6ec49da",
  "sourceToolAssistantUUID": "38ca422d-f1de-4e44-afa3-d9eb016e44da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T17:16:04.128Z_

<details><summary>↩ Tool result · `toolu_01LWDu25XQc1qBgkB194nBEf`</summary>

```text
Web search results for query: "ASE 2026 submission deadline automated software engineering"

Links: [{"title":"ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/ase-2026"},{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"ASE: Automated Software Engineering 2027 2026 2025 .. ...","url":"http://www.wikicfp.com/cfp/program?id=233"},{"title":"ASE 2026","url":"https://ase26.hotcrp.com/"},{"title":"ASE conference series - ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/series/ase"},{"title":"Home | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/journal/10515"},{"title":"ASE 2026 - Tools and Datasets - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2026/ase-2026-tools-and-data-sets"},{"title":"Automated Software Engineering Homepage | The Website of the Automated Software Engineering Conference","url":"https://ase-conferences.org/"},{"title":"Collections and calls for papers | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/journal/10515/collections"},{"title":"ASE 2026 - Research Papers - ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2026/ase-2026-research-track"}]

Based on the search results, here are the submission deadlines for ASE 2026:

ASE 2026 is the 41st IEEE/ACM International Conference on Automated Software Engineering, which will take place in Munich, Germany during October 12–16, 2026.

The submission deadlines vary by track:

- **Research Paper Track**: Deadline is April 15, 2026
- **Journal-First Track**: Deadline is March 26, 2026
- **Industry Showcase**: Deadline is April 23, 2026
- **New Ideas and Emerging Results Track**: Deadline is May 12, 2026
- **Tools and Datasets Track**: Deadline is May 11, 2026

For more detailed information about each track and submission requirements, you can visit the official conference website at https://conf.researchr.org/home/ase-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d859275d-07a7-4581-838c-1ffdd3908381",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "8e868810-fb50-4ce3-84da-7a4282b2f533",
  "sourceToolAssistantUUID": "d859275d-07a7-4581-838c-1ffdd3908381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T17:16:04.168Z_

<details><summary>↩ Tool result · `toolu_01QDRPUFYJpZHH3Jp3nazS6o`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here's what I found about EMNLP 2026:

The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026) will be held in Budapest, Hungary from October 24th to October 29th, 2026.

Regarding submissions, starting from 2024, all main *ACL conferences used ARR exclusively, including EMNLP 2026. This means that EMNLP 2026 uses the ACL Rolling Review (ARR) system for submissions rather than direct conference submissions.

The search results reference various important dates including a reviewer registration deadline (May 27, 2026), author response period dates (July 7-13, 2026), and meta review release date (July 30, 2026), but the specific paper submission deadline for ARR is not clearly shown in these results. For the most current and complete submission deadlines through ARR, I'd recommend checking the official EMNLP 2026 website at https://2026.emnlp.org/ or the ARR dates page at http://aclrollingreview.org/dates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7510e638-f7aa-46f1-a2e9-2ab6ce76e413",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "8d45b1d9-346f-4031-9866-82696fc995af",
  "sourceToolAssistantUUID": "7510e638-f7aa-46f1-a2e9-2ab6ce76e413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T17:16:05.033Z_

<details><summary>↩ Tool result · `toolu_01JV9o2jN9eVGDwcEFvYyjJA`</summary>

```text
Web search results for query: "ISSTA 2026 submission deadline"

Links: [{"title":"ISSTA 2026","url":"https://issta2026.hotcrp.com/"},{"title":"Deadlines - ISSTA 2026","url":"https://issta2026.hotcrp.com/deadlines"},{"title":"35th ACM International Symposium on Software Testing and Analysis (ISSTA'2026)","url":"https://people.cs.kuleuven.be/~dirk.craeynest/ada-belgium/events/26/261003-issta.html"},{"title":"ISSTA 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/issta-2026"},{"title":"SPLASH/ISSTA 2026 - Workshops - SPLASH 2026","url":"https://2026.splashcon.org/track/splash-issta-2026-workshops"},{"title":"Important Dates - ISSTA 2026 - conf.researchr.org","url":"https://conf.researchr.org/dates/issta-2026"},{"title":"ISSTA conference series - ISSTA 2026","url":"https://2023.issta.org/series/issta"},{"title":"International Symposium on Software Testing and Analysis - Accepted Papers, Deadline, Impact Factor & Score 2026 | Research.com","url":"https://research.com/conference/international-symposium-on-software-testing-and-analysis"},{"title":"SPLASH/ISSTA 2026 - Doctoral symposium - SPLASH 2026","url":"https://2026.splashcon.org/track/splash-issta-2026-doctoral-symposium"},{"title":"ISDA 2026 Submission Deadline Extended to 28 May 2026","url":"https://www.hkasd.org/post/isda-2026-submission-deadline-extended-to-28-may-2026"}]

Based on the search results, here's the information about the ISSTA 2026 submission deadline:

The submission deadline for ISSTA 2026 is Friday, January 30, 2026, 6:59:59 AM EST. However, note that the deadline for registering submissions has passed (since today is May 10, 2026).

For reference, the important dates also include author response from March 24-26, 2026 (AoE), initial notification on April 16, 2026 (AoE), major revision deadline on May 21, 2026 (AoE), and final notification on June 25, 2026 (AoE).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8708a5fb-0c88-424a-88f4-908d8e8d07f3",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "83371c27-c639-4d1c-b850-7256838bfe47",
  "sourceToolAssistantUUID": "8708a5fb-0c88-424a-88f4-908d8e8d07f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T17:16:06.052Z_

<details><summary>↩ Tool result · `toolu_01CqhhWw8Wv5riyJePGTpyxi`</summary>

```text
Web search results for query: "ICSE 2027 submission deadline"

Links: [{"title":"ICSE 2027 - Research Track - ICSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/track/icse-2027/icse-2027-research-track"},{"title":"ICSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/home/icse-2027"},{"title":"ICSE 2027 - Important Dates - conf.researchr.org","url":"https://conf.researchr.org/dates/icse-2027"},{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"ICSE: International Conference on Software Engineering 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1462"},{"title":"ICSE Home Page","url":"https://www.icse-conferences.org/"},{"title":"ICSE 2027 - Journal-first Papers - ICSE 2027","url":"https://conf.researchr.org/track/icse-2027/icse-2027-journal-first-papers"},{"title":"ICSE News","url":"http://www.icse-conferences.org/news.html"},{"title":"ICSE 2027: International Conference on Software Engineering","url":"https://www.myhuiban.com/conference/160?lang=en_us"},{"title":"49th International Conference on Software Engineering (ICSE 2027)","url":"https://www.academicjobs.com/conferences/49th-international-conference-on-software-engineering-icse-2027--20270425-architecture-and-design"}]

Based on the search results, here's the submission deadline information for ICSE 2027:

For the Research Track, there is a mandatory abstract deadline on June 23, 2026. The search results indicate ICSE 2027 will follow a single deadline structure with submissions occurring in one cycle, though the exact full paper submission deadline date wasn't explicitly specified in the retrieved results.

For specific track information: The Journal-first Papers submission deadline is Friday, October 30, 2026.

ICSE 2027 will be held from April 25 to May 1, 2027, in Dublin, Ireland, with core conference days being April 28-30.

For the most current and complete deadline information for all tracks, I recommend visiting the official ICSE 2027 conference website at conf.researchr.org/home/icse-2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4ffcdde-17b2-4c0a-a21c-ca67c758a6cb",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "43eb42d3-b37b-4ba0-9995-27924b25e2d8",
  "sourceToolAssistantUUID": "f4ffcdde-17b2-4c0a-a21c-ca67c758a6cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T17:16:06.060Z_

<details><summary>↩ Tool result · `toolu_01CSZWZ69TYe1NbE4r1Kmoog`</summary>

```text
Web search results for query: "FSE 2026 submission deadline ESEC/FSE 2026"

Links: [{"title":"FSE 2026","url":"https://fse2026.hotcrp.com/"},{"title":"FSE 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/fse-2026"},{"title":"Important Dates - FSE 2026 - conf.researchr.org","url":"https://conf.researchr.org/dates/fse-2026"},{"title":"FSE 2026 - How to Submit - FSE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/fse-2026/fse-2026-how-to-submit"},{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"Deadlines - FSE 2026","url":"https://fse2026.hotcrp.com/deadlines"},{"title":"FSE 2026 - IACR","url":"https://fse.iacr.org/2026/"},{"title":"The deadline for FSE 2026 Research Paper submission is ...","url":"https://www.facebook.com/fseconference/posts/the-deadline-for-fse-2026-research-paper-submission-is-approaching-in-three-week/782885284237049/"},{"title":"Home | FSE","url":"https://www.esec-fse.org/"},{"title":"Call for papers - FSE 2026 - IACR","url":"https://fse.iacr.org/2026/callforpapers.php"}]

Based on the search results, here's what I found about FSE 2026 submission deadlines:

There are actually two different conferences with the FSE 2026 acronym:

**1. ACM International Conference on the Foundations of Software Engineering (FSE 2026):**
The submission deadline is Wednesday February 25, 2026, 6:59:59 AM EST. This conference will be held in Montreal, Canada in July 2026. The deadline for registering submissions has passed as of the current date (May 10, 2026), meaning this deadline has already been missed.

**2. IACR Fast Software Encryption (FSE 2026):**
FSE 2026 will take place in Singapore on 23-27 March 2026, and is organized by the International Association for Cryptologic Research (IACR) and will be the 32nd Fast Software Encryption conference. However, the search results don't provide a specific submission deadline for this event.

The ACM conference's submission deadline has already passed, so if you're looking to submit, you may need to clarify which FSE 2026 conference you're interested in or contact the organizers for any extension options.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99a3c0a7-c97b-4343-b3ca-ac734917898a",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "cdd07706-656a-4faa-a37f-02a806fa214c",
  "sourceToolAssistantUUID": "99a3c0a7-c97b-4343-b3ca-ac734917898a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T17:16:06.683Z_

<details><summary>↩ Tool result · `toolu_01VedpQKsnCzcCruGSFu9kUp`</summary>

```text
Web search results for query: "ACL 2026 submission deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL 2026","url":"http://aideadlines.org/conference/?id=acl26"},{"title":"ACL 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=acl26"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"LINGUIST List 37.181 Confs: 64th Annual Meeting of the Association for Computational Linguistics: Industry Track (USA)","url":"https://linguistlist.org/issues/37/181/"},{"title":"ACL 2026 in California: Dates, Deadline, Fees & Registration Steps - Conference Inc.","url":"https://conferenceinc.net/post/acl/"},{"title":"LINGUIST List 36.2630 Confs: Joint Call for Tutorial Proposals: EACL/ACL 2026 (Online)","url":"https://linguistlist.org/issues/36/2630/"}]

Based on the search results, here's what I found regarding ACL 2026 submission deadlines:

ACL 2026 uses the ACL Rolling Review (ARR) exclusively for its main conference submissions. Starting in May 2025, ARR moved to 10-week review cycles, with authors needing to take action by specific key dates for upcoming cycles.

However, the ACL 2026 Industry Track does not use ARR and has its own deadline: the Industry Track paper submission deadline is February 14, 2026.

The main ACL 2026 conference will take place in San Diego, California, from July 2-7, 2026, with all deadlines at 11:59 pm UTC-12h (anywhere on earth).

For the most specific and up-to-date submission deadlines for the main conference, I recommend checking the official ACL 2026 website at https://2026.aclweb.org/ or the ARR dates page at http://aclrollingreview.org/dates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f7c47b2-4b59-4ad8-9ee0-f8cbe0bfa8a2",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "8e8f3c5f-ec01-47f8-afdf-628b5266b2fd",
  "sourceToolAssistantUUID": "9f7c47b2-4b59-4ad8-9ee0-f8cbe0bfa8a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T17:16:08.509Z_

<details><summary>↩ Tool result · `toolu_016hamPKCqfEaWymMBJbftTS`</summary>

```text
Web search results for query: "COLM 2026 submission deadline conference on language modeling"

Links: [{"title":"COLM 2026: Call for Papers","url":"https://colmweb.org/cfp.html"},{"title":"COLM 2026","url":"https://colmweb.org/"},{"title":"Conference on Language Modeling on X: \"COLM 2026 is just around the corner! Mark your calendars for: 💡Abstract deadline: Thursday, March 26, 2026 📄Full paper submission deadline: Tuesday, March 31, 2026 Call for papers in thread (website coming soon). https://t.co/YfjLxzCqxO\" / X","url":"https://x.com/COLM_conf/status/2000952051212415394"},{"title":"COLM 2026 Conference | OpenReview","url":"https://openreview.net/group?id=colmweb.org%2FCOLM%2F2026%2FConference"},{"title":"When is COLM 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/colm"},{"title":"Conference on Language Modeling (COLM), 2026 | ServiceNow AI Research","url":"https://www.servicenow.com/research/event/2026-colm.html"},{"title":"COLM 2026 - Conference on Language Modeling Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/colm"},{"title":"COLM 2026: Key Dates","url":"https://colmweb.org/dates.html"},{"title":"Conference on Language Modeling (@COLM_conf) / Posts ...","url":"https://x.com/COLM_conf"},{"title":"COLM 2026: Call for Workshops","url":"https://colmweb.org/cfw.html"}]

Based on the search results, here's the information about COLM 2026 submission deadlines:

## COLM 2026 Submission Deadlines

The abstract deadline is Thursday, March 26, 2026, and the full paper submission deadline is Tuesday, March 31, 2026.

## Conference Details

COLM 2026 will take place at the Hilton Union Square in San Francisco, USA from October 6-9, 2026.

## Additional Important Dates

Reviews will be released on May 22, 2026, the rebuttal deadline is June 8, 2026, and the final decision date is July 8, 2026.

The submission link through OpenReview opens in February 2026, and questions can be directed to colm-pcs@googlegroups.com.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0db87e2-984e-4b2a-be00-b26669704c75",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "9a3384c7-6996-42c2-87ab-f8c76d63d29e",
  "sourceToolAssistantUUID": "c0db87e2-984e-4b2a-be00-b26669704c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T17:16:11.955Z_

Let me get more details on a few venues where I need clarification on exact dates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a3384c7-6996-42c2-87ab-f8c76d63d29e",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGQz5KU398v6EF4Mbgr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4537d8af-a18f-40e7-8983-c7e8da258c66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L66dBULp6dRL82rADDRJBq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 735,
      "cache_creation_input_tokens": 6653,
      "cache_read_input_tokens": 9508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6653,
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

_source line 28 · 2026-05-10T17:16:12.555Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lzy41vEjZ3cq8xvJWnFE6f`</summary>

```json
{
  "query": "ICSE 2027 research track full paper submission deadline date June 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4537d8af-a18f-40e7-8983-c7e8da258c66",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGQz5KU398v6EF4Mbgr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d6ef7c9-1021-4ead-a968-8f587cb0683d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L66dBULp6dRL82rADDRJBq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 735,
      "cache_creation_input_tokens": 6653,
      "cache_read_input_tokens": 9508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6653,
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

_source line 29 · 2026-05-10T17:16:13.465Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XLiRQyCJHktiA6aZM1HX1Z`</summary>

```json
{
  "query": "ACL rolling review ARR June 2026 cycle deadline commitment deadline ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d6ef7c9-1021-4ead-a968-8f587cb0683d",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGQz5KU398v6EF4Mbgr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a468583c-1f0c-4458-867b-75c2dd938fa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L66dBULp6dRL82rADDRJBq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 735,
      "cache_creation_input_tokens": 6653,
      "cache_read_input_tokens": 9508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6653,
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

_source line 30 · 2026-05-10T17:16:13.872Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VMgetq8PJH9UwNvfJWVyJk`</summary>

```json
{
  "query": "EMNLP 2026 ARR commitment deadline submission cycle June 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a468583c-1f0c-4458-867b-75c2dd938fa9",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGQz5KU398v6EF4Mbgr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11507094-6222-4882-9ce8-2e9dd41625b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L66dBULp6dRL82rADDRJBq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 735,
      "cache_creation_input_tokens": 6653,
      "cache_read_input_tokens": 9508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6653,
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

_source line 31 · 2026-05-10T17:16:14.855Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HntfprGRi7T7QrFHzfWU9U`</summary>

```json
{
  "query": "AAAI 2027 expected submission deadline August 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11507094-6222-4882-9ce8-2e9dd41625b1",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGQz5KU398v6EF4Mbgr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03e22c5d-58da-49b7-9c0e-9b53439fe910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L66dBULp6dRL82rADDRJBq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 735,
      "cache_creation_input_tokens": 6653,
      "cache_read_input_tokens": 9508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6653,
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

_source line 32 · 2026-05-10T17:16:15.213Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KEQmn1zRax9vaFq7NWDnNa`</summary>

```json
{
  "query": "ASE 2026 \"new ideas\" \"emerging results\" deadline May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03e22c5d-58da-49b7-9c0e-9b53439fe910",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGQz5KU398v6EF4Mbgr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60aaa8c0-69e2-441f-9851-5ccf48e867f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L66dBULp6dRL82rADDRJBq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 735,
      "cache_creation_input_tokens": 6653,
      "cache_read_input_tokens": 9508,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6653
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 735,
          "output_tokens": 297,
          "cache_read_input_tokens": 9508,
          "cache_creation_input_tokens": 6653,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6653,
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

_source line 33 · 2026-05-10T17:16:17.030Z_

<details><summary>↩ Tool result · `toolu_01Lzy41vEjZ3cq8xvJWnFE6f`</summary>

```text
Web search results for query: "ICSE 2027 research track full paper submission deadline date June 2026"

Links: [{"title":"ICSE 2027 - Research Track - ICSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/track/icse-2027/icse-2027-research-track"},{"title":"ICSE 2027 - Journal-first Papers - ICSE 2027","url":"https://conf.researchr.org/track/icse-2027/icse-2027-journal-first-papers"},{"title":"ICSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/home/icse-2027"},{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"ICSE 2027 - Important Dates - conf.researchr.org","url":"https://conf.researchr.org/dates/icse-2027"},{"title":"ICSE 2027 - Competitions - conf.researchr.org","url":"https://conf.researchr.org/track/icse-2027/icse-2027-competition-track"},{"title":"ICSE 2027 - Software Engineering in Society (SEIS) - ICSE 2027","url":"https://conf.researchr.org/track/icse-2027/icse-2027-seis"},{"title":"ICSE 2026 - Research Track - ICSE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/icse-2026/icse-2026-research-track"},{"title":"ICSE: International Conference on Software Engineering 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1462"},{"title":"ICSE 2027: International Conference on Software Engineering","url":"https://www.myhuiban.com/conference/160?lang=en_us"}]

I found information about the ICSE 2027 Research Track. Looking at the search results, the official ICSE 2027 website mentions that ICSE 2027 will have one submission cycle, but the specific deadline date in June 2026 is not displayed in the excerpts I retrieved.

The search results show deadlines for other ICSE 2027 tracks (such as SEIS with a deadline of October 23, 2026, and Journal-first Papers with a deadline of October 30, 2026), but the specific full paper submission deadline for the Research Track that you're looking for is not visible in these results.

For the most accurate and complete deadline information for the ICSE 2027 Research Track, I recommend checking the official ICSE 2027 Research Track Call for Papers directly at: https://conf.researchr.org/track/icse-2027/icse-2027-research-track


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d6ef7c9-1021-4ead-a968-8f587cb0683d",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "bbf66246-97bf-4576-b805-b953f36bda7a",
  "sourceToolAssistantUUID": "9d6ef7c9-1021-4ead-a968-8f587cb0683d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T17:16:18.411Z_

<details><summary>↩ Tool result · `toolu_01HntfprGRi7T7QrFHzfWU9U`</summary>

```text
Web search results for query: "AAAI 2027 expected submission deadline August 2026"

Links: [{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"MPC Deadlines Hub","url":"https://mpc-deadlines.github.io/"},{"title":"AAAI 2026","url":"http://aideadlines.org/conference/?id=aaai26"}]

Based on the search results, I found information about the expected AAAI 2027 submission deadline:

Submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns. More specifically, the paper deadline is August 1, 2026, with an abstract deadline of July 25, 2026.

The conference will be held in Montréal, Québec, Canada from February 16-23, 2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03e22c5d-58da-49b7-9c0e-9b53439fe910",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "0af67cbe-d085-4875-8e88-03467a4418bc",
  "sourceToolAssistantUUID": "03e22c5d-58da-49b7-9c0e-9b53439fe910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T17:16:19.125Z_

<details><summary>↩ Tool result · `toolu_01XLiRQyCJHktiA6aZM1HX1Z`</summary>

```text
Web search results for query: "ACL rolling review ARR June 2026 cycle deadline commitment deadline ACL 2026"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the web search results, I found relevant information about ACL 2026 deadlines related to ARR review cycles:

## ACL 2026 and ARR Deadlines

ARR switched to 10-week review cycles starting in May 2025, which differs from the previous 8-week cycles.

### Key Deadlines for ACL 2026:

The submission deadline for papers to ARR is January 5, 2026.

Following the January submission cycle:
- Reviews must be completed by February 7th, and meta-reviews by March 3rd
- ARR reviews and meta-reviews will be available to authors of the January cycle on March 10, 2026

### Commitment Deadline for ACL 2026:

The commitment deadline for ACL 2026 is March 14, 2026. This is the deadline by which authors with completed ARR reviews can commit their papers to the ACL 2026 conference for final acceptance decisions.

The search results indicate that ACL 2026 will use ACL Rolling Review (ARR) as a reviewing system, with both submissions and commitments performed via the OpenReview platform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a468583c-1f0c-4458-867b-75c2dd938fa9",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "0475762f-5d1f-4a1b-8125-86c081c4e89a",
  "sourceToolAssistantUUID": "a468583c-1f0c-4458-867b-75c2dd938fa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T17:16:19.154Z_

<details><summary>↩ Tool result · `toolu_01VMgetq8PJH9UwNvfJWVyJk`</summary>

```text
Web search results for query: "EMNLP 2026 ARR commitment deadline submission cycle June 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"The First Call for Industry Track Papers for EMNLP 2026 is officially out! Are you deploying NLP in real-world applications? Share your insights, challenges, and deployed systems with the community. 🗓️ Deadline: June 16, 2026 🔗 Link: https://t.co/ga3k6CJcm0 #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2048750521696072166"}]

Based on my search results, here's what I found regarding EMNLP 2026 and ARR commitment deadlines:

## EMNLP 2026 ARR Submission and Commitment Deadlines

The ARR submission deadline for EMNLP 2026 is May 25, 2026, with a reviewer registration deadline for all authors on May 27, 2026.

The EMNLP commitment deadline is August 2, 2026.

## June 2026 ARR Cycle Policy

For the ARR 2026 May cycle, which is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time. This choice is binding for EMNLP 2026: ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

It's important to note that the primary ARR submission deadline for EMNLP 2026 is May 25, 2026, not a June 2026 deadline. The search results do not show a June 2026 submission cycle specifically for EMNLP 2026's main conference track.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11507094-6222-4882-9ce8-2e9dd41625b1",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "ee4943e4-438f-4e7a-83d5-7040f41599b8",
  "sourceToolAssistantUUID": "11507094-6222-4882-9ce8-2e9dd41625b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T17:16:19.446Z_

<details><summary>↩ Tool result · `toolu_01KEQmn1zRax9vaFq7NWDnNa`</summary>

```text
Web search results for query: "ASE 2026 "new ideas" "emerging results" deadline May 2026"

Links: [{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"EASE 2026 - Short Papers and Emerging Results - EASE 2026","url":"https://conf.researchr.org/track/ease-2026/ease-2026-short-papers-and-emerging-results"},{"title":"EASE 2026 - Posters and Vision - EASE 2026","url":"https://conf.researchr.org/track/ease-2026/ease-2026-posters-and-vision"},{"title":"ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/ase-2026"},{"title":"ASE 2026 - Industry Showcase - ASE 2026","url":"https://conf.researchr.org/track/ase-2026/ase-2026-industry-showcase"},{"title":"ASE: Automated Software Engineering 2027 2026 2025 .. ...","url":"http://www.wikicfp.com/cfp/program?id=233"},{"title":"ASE 2026 - Tools and Datasets - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2026/ase-2026-tools-and-data-sets"},{"title":"ASE 2026","url":"https://ase26.hotcrp.com/"},{"title":"ASE 2026 - Research Papers - ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2026/ase-2026-research-track"},{"title":"ASE 2026 Annual Meeting Program - The Association for Surgical Education","url":"https://www.surgicaleducation.com/ase-2026-annual-meeting-program/"}]

Based on the search results, here's what I found:

The International Conference on Automated Software Engineering (ASE) - New Ideas and Emerging Results Track is scheduled for October 12 – October 16, 2026 in Munich, Germany.

However, the search results do not show a specific May 2026 deadline for the ASE 2026 "New Ideas and Emerging Results" track. The results do indicate that the ASE 2026 Tools and Datasets Track has a deadline of May 11th 2026, but this is for a different track.

To find the specific deadline for the ASE 2026 New Ideas and Emerging Results track, you may want to check the official ASE 2026 conference website or the specific track page on conf.researchr.org, as the exact deadline for that particular track is not clearly specified in these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60aaa8c0-69e2-441f-9851-5ccf48e867f2",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "e6df9c1f-b5a7-48b6-9c12-c169aabcbf2f",
  "sourceToolAssistantUUID": "60aaa8c0-69e2-441f-9851-5ccf48e867f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-10T17:16:22.951Z_

Now let me get the exact ICSE 2027 research track deadline and confirm the ASE 2026 NIER deadline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6df9c1f-b5a7-48b6-9c12-c169aabcbf2f",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGRo9mixVQbNwX9XgoV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "671ff6fb-edc9-444d-a6f2-dc4d15bd1450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvE9ddNW3xBmRQJhp8Tmmc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4712,
      "cache_read_input_tokens": 16161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4712,
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

_source line 39 · 2026-05-10T17:16:23.502Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JHue2gP2GatGrBJPLUV1eb`</summary>

```json
{
  "query": "site:conf.researchr.org ICSE 2027 research track abstract deadline \"June 23\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "671ff6fb-edc9-444d-a6f2-dc4d15bd1450",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGRo9mixVQbNwX9XgoV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21f9b42d-d6c4-43a7-926d-e2ae7f56ef67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvE9ddNW3xBmRQJhp8Tmmc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4712,
      "cache_read_input_tokens": 16161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4712,
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

_source line 40 · 2026-05-10T17:16:23.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A7PXxRT9tQnWpzKxbyuZB2`</summary>

```json
{
  "query": "site:conf.researchr.org ASE 2026 NIER \"new ideas\" deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21f9b42d-d6c4-43a7-926d-e2ae7f56ef67",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGRo9mixVQbNwX9XgoV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "636c3481-a702-4bb6-b82b-ec2a49b764ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvE9ddNW3xBmRQJhp8Tmmc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4712,
      "cache_read_input_tokens": 16161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4712,
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

_source line 41 · 2026-05-10T17:16:24.477Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AcuBrNbjD7HTRXzTjZdqkW`</summary>

```json
{
  "query": "NeurIPS 2026 datasets benchmarks track deadline separate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "636c3481-a702-4bb6-b82b-ec2a49b764ff",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGRo9mixVQbNwX9XgoV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a15567f4-732d-4439-a410-002f7697c8be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvE9ddNW3xBmRQJhp8Tmmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4712,
      "cache_read_input_tokens": 16161,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4712
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 16161,
          "cache_creation_input_tokens": 4712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4712,
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

_source line 42 · 2026-05-10T17:16:27.613Z_

<details><summary>↩ Tool result · `toolu_01JHue2gP2GatGrBJPLUV1eb`</summary>

```text
Web search results for query: "site:conf.researchr.org ICSE 2027 research track abstract deadline "June 23""

Links: [{"title":"ICSE 2027 - Research Track - ICSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/track/icse-2027/icse-2027-research-track"},{"title":"ICSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/home/icse-2027"},{"title":"ICSE 2027 - Important Dates - conf.researchr.org","url":"https://conf.researchr.org/dates/icse-2027"},{"title":"ICSE 2027 - Journal-first Papers - ICSE 2027","url":"https://conf.researchr.org/track/icse-2027/icse-2027-journal-first-papers"},{"title":"ICSE 2027 - Tutorials and Technical Briefings - ICSE 2027","url":"https://conf.researchr.org/track/icse-2027/icse-2027-tutorials-and-technical-briefings"},{"title":"ICSE 2027 - SRC - ACM Student Research Competition - ICSE 2027","url":"https://conf.researchr.org/track/icse-2027/icse-2027-src"},{"title":"Program Committee - ICSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/committee/icse-2027/icse-2027-research-track-program-committee"},{"title":"ICSE 2027 - Competitions - conf.researchr.org","url":"https://conf.researchr.org/track/icse-2027/icse-2027-competition-track"},{"title":"ICSE 2027 - Artifact Evaluation - ICSE 2027","url":"https://conf.researchr.org/track/icse-2027/icse-2027-artifact-evaluation"},{"title":"ICSE 2027 - Workshops - conf.researchr.org","url":"https://conf.researchr.org/track/icse-2027/icse-2027-workshops"}]

Based on the search results from conf.researchr.org, I found information about ICSE 2027. However, the search results provided don't show a specific abstract deadline of "June 23" for the Research Track. 

The search results indicate that ICSE 2027 will have one submission cycle with dates listed as 23:59:59 AoE (UTC-12h), but the specific dates aren't fully displayed in the search results retrieved.

To find the exact Research Track abstract deadline of June 23, you may want to visit the ICSE 2027 Research Track page directly at https://conf.researchr.org/track/icse-2027/icse-2027-research-track or check the Important Dates page at https://conf.researchr.org/dates/icse-2027, which should have the complete submission timeline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21f9b42d-d6c4-43a7-926d-e2ae7f56ef67",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "7b3508e4-02e9-44b6-9596-f7d7aede878e",
  "sourceToolAssistantUUID": "21f9b42d-d6c4-43a7-926d-e2ae7f56ef67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T17:16:29.251Z_

<details><summary>↩ Tool result · `toolu_01AcuBrNbjD7HTRXzTjZdqkW`</summary>

```text
Web search results for query: "NeurIPS 2026 datasets benchmarks track deadline separate"

Links: [{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"NeurIPS 2026 Evaluations & Datasets FAQ","url":"https://neurips.cc/Conferences/2026/EvaluationsDatasetsFAQ"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"NeurIPS 2026 Evaluations and Datasets Track | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FEvaluations_and_Datasets_Track"},{"title":"Datasets and Benchmarks Track: Call for Papers – KDD 2026","url":"https://kdd2026.kdd.org/datasets-and-benchmarks-track-call-for-papers/"},{"title":"Call For Datasets & Benchmarks","url":"https://neurips.cc/Conferences/2023/CallForDatasetsBenchmarks"},{"title":"Introducing the Evaluations & Datasets Track at NeurIPS 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/03/23/introducing-the-evaluations-datasets-track-at-neurips-2026/"},{"title":"NeurIPS Datasets & Benchmarks Track: From Art to Science in AI Evaluations – NeurIPS Blog","url":"https://blog.neurips.cc/2025/12/05/neurips-datasets-benchmarks-track-from-art-to-science-in-ai-evaluations/"},{"title":"NeurIPS 2026 Evaluations & Datasets Hosting Guidelines","url":"https://neurips.cc/Conferences/2026/EvaluationsDatasetsHosting"}]

Based on the search results, here's what I found about NeurIPS 2026 Evaluations & Datasets Track deadlines:

## Key Deadlines for NeurIPS 2026 Evaluations & Datasets Track

The abstract submission deadline is May 4, 2026 (AoE), and the full paper submission deadline (including all supplementary materials) is May 6, 2026 (AoE).

## Separate Track Status

The Evaluations & Datasets Track operates on the same timeline as the main conference. The Evaluations and Datasets Track follows the NeurIPS Main Track Call for Papers in terms of requirements and timelines, with the following track-specific additions. However, the Datasets & Benchmarks Track at NeurIPS 2026 has been officially renamed the Evaluations & Datasets (ED) Track, and the submission portal opens on April 15, 2026 (at the same time as the main track).

So while the E&D Track is a separate track with its own call for papers and scope, it shares the same submission deadlines as the main conference rather than having separate deadlines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a15567f4-732d-4439-a410-002f7697c8be",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "7540e8b5-ba9d-4362-a0a9-462f59e4ab9f",
  "sourceToolAssistantUUID": "a15567f4-732d-4439-a410-002f7697c8be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T17:16:29.938Z_

<details><summary>↩ Tool result · `toolu_01A7PXxRT9tQnWpzKxbyuZB2`</summary>

```text
Web search results for query: "site:conf.researchr.org ASE 2026 NIER "new ideas" deadline"

Links: [{"title":"ASE 2026 - NIER - ASE 2026","url":"https://conf.researchr.org/track/ase-2026/ase-2026-nier"},{"title":"ICSE 2026 - New Ideas and Emerging Results (NIER) - ICSE 2026","url":"https://conf.researchr.org/track/icse-2026/icse-2026-nier"},{"title":"ASE 2020 - New Ideas and Emerging Results (NIER) track - ASE 2020","url":"https://conf.researchr.org/track/ase-2020/ase-2020-nier-track"},{"title":"ASE 2026 - Industry Showcase - ASE 2026","url":"https://conf.researchr.org/track/ase-2026/ase-2026-industry-showcase"},{"title":"ASE 2025 - New Ideas and Emerging Results - ASE 2025","url":"https://conf.researchr.org/track/ase-2025/ase-2025-nier-track"},{"title":"ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/ase-2026"},{"title":"ASE 2023 - NIER Track - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2023/ase-2023-nier-track"},{"title":"Program Committee - ICSE 2026","url":"https://conf.researchr.org/committee/icse-2026/icse-2026-nier-new-ideas-and-emerging-results"},{"title":"ASE 2026 - Research Papers - ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2026/ase-2026-research-track"},{"title":"Towards Bridging Language Gaps in OSS with LLM-Driven Documentation Translation (ICSE 2026 - New Ideas and Emerging Results (NIER)) - ICSE 2026","url":"https://conf.researchr.org/details/icse-2026/icse-2026-nier/30/Towards-Bridging-Language-Gaps-in-OSS-with-LLM-Driven-Documentation-Translation"}]

I found the ASE 2026 NIER track page, but the search results don't show the specific deadline information. Let me search more specifically for the deadline dates on that page.

Links: [{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"ASE 2026 - Research Papers - ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/ase-2026/ase-2026-research-track"},{"title":"ASE 2026 NIER","url":"https://ase2026-nier.hotcrp.com/"},{"title":"ASE 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/ase-2026"},{"title":"ASE Call For Abstracts - The Association for Surgical Education","url":"https://www.surgicaleducation.com/call-for-abstracts/"},{"title":"ASE 2026 - NIER - ASE 2026","url":"https://conf.researchr.org/track/ase-2026/ase-2026-nier"},{"title":"Guidelines For Abstract Preparation & Submission - ASE","url":"https://www.asecho.org/education-events/scientific-sessions/call-for-science/abstract-guidelines/"},{"title":"conf.researchr.org conference management system -","url":"https://conf.researchr.org/submissiondates"},{"title":"ASE 2026 - Industry Showcase - ASE 2026","url":"https://conf.researchr.org/track/ase-2026/ase-2026-industry-showcase"},{"title":"Call for Abstracts - ISEE 2026","url":"https://www.isee26.org/call-for-abstracts/"}]

Based on my web search results, I found information about the ASE 2026 NIER track. However, I should note that the specific deadline information is not explicitly shown on the main ASE 2026 NIER track page that was returned in the search results.

According to one of the search results from a software engineering conferences deadline tracking site, there is an abstract deadline on May 8, 2026 for ASE 2026. This appears to be the submission deadline for the ASE 2026 NIER track.

For more detailed and complete submission deadline information, I recommend checking the official ASE 2026 NIER submission page directly at https://ase2026-nier.hotcrp.com/ or the main track information page at https://conf.researchr.org/track/ase-2026/ase-2026-nier.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "636c3481-a702-4bb6-b82b-ec2a49b764ff",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "e71bd781-0d9f-4860-a9a5-10454b1b8a94",
  "sourceToolAssistantUUID": "636c3481-a702-4bb6-b82b-ec2a49b764ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-10T17:16:35.139Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pd8gtJzjiFBFq2sYb6EpxQ`</summary>

```json
{
  "query": "ICSE 2027 research track paper submission deadline June 30 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e71bd781-0d9f-4860-a9a5-10454b1b8a94",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGSZgvcCE7jgZmr6FW4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f25db40-7c1f-4e65-85ed-55956815e3a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W4F4gZC6xT3yE6TZgx31pW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 817,
      "cache_creation_input_tokens": 2336,
      "cache_read_input_tokens": 20873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2336,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-10T17:16:35.293Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G1gZcnxAvTcv6sDjXkrWWK`</summary>

```json
{
  "query": "EMNLP 2026 industry track deadline June 16 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f25db40-7c1f-4e65-85ed-55956815e3a0",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGSZgvcCE7jgZmr6FW4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61b68ce4-a402-48c2-b652-dacac9126b74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W4F4gZC6xT3yE6TZgx31pW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 817,
      "cache_creation_input_tokens": 2336,
      "cache_read_input_tokens": 20873,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2336
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 817,
          "output_tokens": 121,
          "cache_read_input_tokens": 20873,
          "cache_creation_input_tokens": 2336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2336,
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

_source line 47 · 2026-05-10T17:16:38.721Z_

<details><summary>↩ Tool result · `toolu_01G1gZcnxAvTcv6sDjXkrWWK`</summary>

```text
Web search results for query: "EMNLP 2026 industry track deadline June 16 2026"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 on X: \"The First Call for Industry Track Papers for EMNLP 2026 is officially out! Are you deploying NLP in real-world applications? Share your insights, challenges, and deployed systems with the community. 🗓️ Deadline: June 16, 2026 🔗 Link: https://t.co/ga3k6CJcm0 #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2048750521696072166"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://hlr.github.io/deadlines/"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"Update EMNLP System Demonstrations Track with 2026 conference data · huggingface/ai-deadlines at 6a94f2c","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/6a94f2c940ba976564775b34f6b224b0f9ad638d"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in Natural Language Processing","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=192857&copyownerid=692"}]

Based on the search results, I can confirm the information about the EMNLP 2026 Industry Track deadline:

The EMNLP 2026 Industry Track has a paper submission deadline of June 16, 2026 (11:59 PM UTC-12:00, AoE), with the conference scheduled for October 24–29, 2026 in Budapest, Hungary.

The Industry Track is seeking submissions that not only address research but also demonstrate the application of systems in real-world scenarios, irrespective of whether they involve proprietary data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61b68ce4-a402-48c2-b652-dacac9126b74",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "3b229dbe-f4d0-4722-8aa7-5d9ed2f2a9b7",
  "sourceToolAssistantUUID": "61b68ce4-a402-48c2-b652-dacac9126b74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-10T17:16:38.758Z_

<details><summary>↩ Tool result · `toolu_01Pd8gtJzjiFBFq2sYb6EpxQ`</summary>

```text
Web search results for query: "ICSE 2027 research track paper submission deadline June 30 2026"

Links: [{"title":"ICSE 2027 - Research Track - ICSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/track/icse-2027/icse-2027-research-track"},{"title":"Software Engineering Research Venues Deadlines","url":"https://se-deadlines.github.io/"},{"title":"ICSE 2027 - conf.researchr.org","url":"https://conf.researchr.org/home/icse-2027"},{"title":"ICSE 2027 - Important Dates - conf.researchr.org","url":"https://conf.researchr.org/dates/icse-2027"},{"title":"ICSE 2026 industry challenge submission deadline extended","url":"https://www.facebook.com/groups/softengcom/posts/10173039972005184/"},{"title":"ICSE 2026 - Research Track - ICSE 2026 - conf.researchr.org","url":"https://conf.researchr.org/track/icse-2026/icse-2026-research-track"},{"title":"Deadlines - ICSE 2026, Research Track","url":"https://icse2026.hotcrp.com/deadlines"},{"title":"ICSE: International Conference on Software Engineering 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1462"},{"title":"ICSE Home Page","url":"https://www.icse-conferences.org/"},{"title":"From April 12–18, 2026, the world's premier software ...","url":"https://www.instagram.com/p/DVbkx_vFezh/"}]

Based on the search results, I found the information about the ICSE 2027 research track paper submission deadline:

The ICSE 2027 research track has a paper submission deadline of June 30, 2026. Additionally, there is a mandatory abstract deadline on June 23, 2026.

All submission dates are at 23:59:59 AoE (UTC-12h). The subsequent review timeline includes an author response period from September 23-25, 2026, with notification of decisions on October 20, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f25db40-7c1f-4e65-85ed-55956815e3a0",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a60fd13a59176a15b",
  "type": "user",
  "uuid": "08d67b4c-3314-44f4-ab9e-531afaf8589d",
  "sourceToolAssistantUUID": "0f25db40-7c1f-4e65-85ed-55956815e3a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-10T17:17:17.153Z_

Here is a comprehensive summary of all 10 conference venues, their submission deadlines, and whether they are still open as of May 10, 2026. I have focused on identifying which deadlines your paper on "execution simulation as verifier for code repair scaling" could still target.

---

## DEADLINES STILL OPEN (after May 10, 2026)

### 1. EMNLP 2026 (ARR Main Track)
- **ARR Submission Deadline:** May 25, 2026
- **Commitment Deadline:** August 2, 2026
- **Conference:** October 24--29, 2026, Budapest, Hungary
- **Status: OPEN** -- You have until May 25 to submit via ARR, or commit reviews by August 2.
- **Fit:** Strong fit for NLP + code generation / reasoning work.

### 2. EMNLP 2026 (Industry Track)
- **Submission Deadline:** June 16, 2026
- **Conference:** October 24--29, 2026, Budapest, Hungary
- **Status: OPEN** -- Direct submission (not through ARR).
- **Fit:** Good if the paper has a deployed-system or applied angle.

### 3. ICSE 2027 (Research Track)
- **Abstract Deadline:** June 23, 2026
- **Paper Deadline:** June 30, 2026
- **Conference:** April 25 -- May 1, 2027, Dublin, Ireland
- **Status: OPEN**
- **Fit:** Excellent fit -- premier SE venue; code repair and scaling are core ICSE topics.

### 4. AAAI 2027
- **Expected Abstract Deadline:** ~July 25, 2026
- **Expected Paper Deadline:** ~August 1, 2026
- **Conference:** February 16--23, 2027, Montreal, Canada
- **Status: OPEN (expected)** -- Official CFP not yet released, but dates are projected from historical patterns and early listings.
- **Fit:** Good fit for AI-for-code / verification / scaling work.

### 5. ASE 2026 -- NIER Track (New Ideas and Emerging Results)
- **Deadline:** May 12, 2026
- **Conference:** October 12--16, 2026, Munich, Germany
- **Status: OPEN (barely)** -- 2 days remain.
- **Fit:** Strong fit for a shorter paper presenting the novel idea of execution simulation as a verifier.

### 6. ASE 2026 -- Tools and Datasets Track
- **Deadline:** May 11, 2026
- **Conference:** October 12--16, 2026, Munich, Germany
- **Status: OPEN (barely)** -- 1 day remains.
- **Fit:** Good if the paper has a tool or benchmark component.

---

## DEADLINES ALREADY PASSED (before or on May 10, 2026)

### 7. NeurIPS 2026
- **Abstract Deadline:** May 4, 2026 (AoE)
- **Full Paper Deadline:** May 6, 2026 (AoE)
- **Conference:** December 6--12, 2026
- **Status: PASSED** -- Missed by ~4 days.

### 8. ACL 2026
- **ARR Submission Deadline (for ACL commitment):** January 5, 2026
- **Commitment Deadline:** March 14, 2026
- **Industry Track Deadline:** February 14, 2026
- **Conference:** July 2--7, 2026, San Diego, CA
- **Status: PASSED** -- All deadlines have passed.

### 9. COLM 2026
- **Abstract Deadline:** March 26, 2026
- **Full Paper Deadline:** March 31, 2026
- **Conference:** October 6--9, 2026, San Francisco, CA
- **Status: PASSED**

### 10. FSE 2026 (ESEC/FSE -- Foundations of Software Engineering)
- **Submission Deadline:** February 25, 2026
- **Conference:** July 2026, Montreal, Canada
- **Status: PASSED**

### 11. ISSTA 2026
- **Submission Deadline:** January 30, 2026
- **Conference:** Co-located with SPLASH 2026
- **Status: PASSED**

### 12. ASE 2026 (Research Track)
- **Deadline:** April 15, 2026
- **Status: PASSED**

### 13. ICLR 2027
- **Status:** Not yet announced. ICLR 2026 had a September 2025 deadline. ICLR 2027 deadline is likely around September/October 2026 -- worth monitoring.

---

## RECOMMENDATIONS FOR YOUR PAPER

A paper on **"execution simulation as verifier for code repair scaling"** sits at the intersection of AI/ML and software engineering. The best upcoming targets, ranked by fit and prestige:

1. **ICSE 2027** (deadline June 30) -- Premier SE venue. Code repair + verification is a flagship topic. Highly recommended.
2. **EMNLP 2026 ARR** (deadline May 25) -- If the paper has a strong NLP/LLM angle (e.g., LLM-based code repair with execution-based verification). Submit to the May ARR cycle and commit to EMNLP.
3. **AAAI 2027** (expected ~August 1) -- Broad AI venue; good for AI-for-code papers with a scaling/verification angle.
4. **ASE 2026 NIER** (deadline May 12) -- If you can prepare a short paper (4 pages) in 2 days, this is an excellent venue for presenting the core idea.
5. **ICLR 2027** (expected ~September 2026) -- Worth watching for; strong fit if the paper emphasizes learning representations for code.

Sources:
- [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)
- [EMNLP 2026](https://2026.emnlp.org/)
- [EMNLP 2026 Main Conference Papers Call](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 Industry Track Call](https://2026.emnlp.org/calls/industry_track/)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)
- [ACL 2026](https://2026.aclweb.org/)
- [AAAI Conference Page](https://aaai.org/conference/aaai/)
- [AAAI 2027 Deadline Tracker](https://www.getpaperpilot.com/deadlines/aaai-2027.html)
- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)
- [ASE 2026](https://conf.researchr.org/home/ase-2026)
- [ASE 2026 NIER Track](https://conf.researchr.org/track/ase-2026/ase-2026-nier)
- [ASE 2026 Tools and Datasets](https://conf.researchr.org/track/ase-2026/ase-2026-tools-and-data-sets)
- [FSE 2026](https://conf.researchr.org/home/fse-2026)
- [ISSTA 2026](https://conf.researchr.org/home/issta-2026)
- [ICSE 2027 Research Track](https://conf.researchr.org/track/icse-2027/icse-2027-research-track)
- [ICSE 2027 Important Dates](https://conf.researchr.org/dates/icse-2027)
- [COLM 2026](https://colmweb.org/)
- [COLM 2026 Key Dates](https://colmweb.org/dates.html)
- [SE Deadlines Tracker](https://se-deadlines.github.io/)
- [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08d67b4c-3314-44f4-ab9e-531afaf8589d",
  "isSidechain": true,
  "agentId": "a60fd13a59176a15b",
  "requestId": "req_011CauGTDLr53KqNkghDwZEA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96e2b97c-ce80-4fc3-bd76-0ebfd658a206",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6bJUHLbfgrHtAo5sdHd8c",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 833,
      "cache_creation_input_tokens": 1562,
      "cache_read_input_tokens": 23209,
      "output_tokens": 2038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1562
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 833,
          "output_tokens": 2038,
          "cache_read_input_tokens": 23209,
          "cache_creation_input_tokens": 1562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1562,
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
