# Research conversation: I need to find two things: **Part 1: Conference venue deadlines after 2026-05-10** Use WebSearch to find submission dead

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a29aae6d27db48991.jsonl`
- **Structured JSON:** [`8e9f027fd2ab3033b0cd.json`](../../sessions/8e/8e9f027fd2ab3033b0cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

40 recorded events

### User

_source line 1 · 2026-05-10T17:49:50.737Z_

I need to find two things:

**Part 1: Conference venue deadlines after 2026-05-10**
Use WebSearch to find submission deadlines for these ML/robotics venues. Only report venues whose deadline is AFTER May 10, 2026:
1. Search "NeurIPS 2026 submission deadline"
2. Search "ICLR 2027 submission deadline"
3. Search "CoRL 2026 submission deadline"
4. Search "ICRA 2027 submission deadline"
5. Search "IROS 2026 submission deadline"
6. Search "RSS 2026 submission deadline"
7. Search "AAAI 2027 submission deadline"
8. Search "CVPR 2027 submission deadline"

For each, report the exact deadline date if found, or "not yet announced."

**Part 2: Current SOTA open-source models**
9. Search "best open source video generation model 2026"
10. Search "SOTA open source diffusion model video 2026"
11. Search "best open source vision language model robotics 2026"
12. Search "open source video diffusion transformer 2026 state of the art"

Report the top current models with their names and capabilities.

Be thorough and report all findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "82491b08-546f-4d37-931d-79436ef33d98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T17:49:50.739Z_

```json
{
  "parentUuid": "82491b08-546f-4d37-931d-79436ef33d98",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
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
  "uuid": "12f8fe8e-b281-4a49-bb87-cc3c28339178",
  "timestamp": "2026-05-10T17:49:50.739Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T17:49:53.104Z_



I'll start by loading the WebSearch tool schema, then run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12f8fe8e-b281-4a49-bb87-cc3c28339178",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJz3uudZ19XJ6D42gxc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c02f02a8-270a-4f8a-a81b-8af201931386",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tMTadaudj2aSQz5Qs6sDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 848,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 848,
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

_source line 4 · 2026-05-10T17:49:53.585Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014QigZsv9aT8FpLsk3rVjTS`</summary>

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
  "parentUuid": "c02f02a8-270a-4f8a-a81b-8af201931386",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJz3uudZ19XJ6D42gxc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec31c742-c082-4640-93f2-86ba4f65ffc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tMTadaudj2aSQz5Qs6sDi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 848,
      "cache_read_input_tokens": 8223,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 848,
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

_source line 5 · 2026-05-10T17:49:53.590Z_

<details><summary>↩ Tool result · `toolu_014QigZsv9aT8FpLsk3rVjTS`</summary>

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
  "parentUuid": "ec31c742-c082-4640-93f2-86ba4f65ffc2",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "6db7650f-1be7-46eb-9fc6-62a6b3220462",
  "sourceToolAssistantUUID": "ec31c742-c082-4640-93f2-86ba4f65ffc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T17:49:55.926Z_



Now let me run all 12 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6db7650f-1be7-46eb-9fc6-62a6b3220462",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f94291d-49ad-4dc9-b270-1cd17b7b6a45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 7 · 2026-05-10T17:49:56.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LBqmHHpjsftJ5cpQFwG6oT`</summary>

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
  "parentUuid": "6f94291d-49ad-4dc9-b270-1cd17b7b6a45",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df0654f5-5538-4d4b-a069-d983b7f92c23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 8 · 2026-05-10T17:49:56.882Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EzK2c4kEuHsQTuvHoTscgL`</summary>

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
  "parentUuid": "df0654f5-5538-4d4b-a069-d983b7f92c23",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "913e8294-d5e1-48ac-abfc-f85ced2bd3eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 9 · 2026-05-10T17:49:57.354Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WJm5zPJwdYdrpjF73KjWpW`</summary>

```json
{
  "query": "CoRL 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "913e8294-d5e1-48ac-abfc-f85ced2bd3eb",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75587a36-7009-4b3c-9adf-c8a496b905db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 10 · 2026-05-10T17:49:57.367Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015xqaRwjQYxqfeEwZtjX5wF`</summary>

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
  "parentUuid": "75587a36-7009-4b3c-9adf-c8a496b905db",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af328868-fc37-4ce3-a131-8ac25ee1236c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 11 · 2026-05-10T17:49:57.918Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DQGoN5YiyTfwSkPhCbvGU5`</summary>

```json
{
  "query": "IROS 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af328868-fc37-4ce3-a131-8ac25ee1236c",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c666479-2922-40a4-ae57-8e8adbc67928",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 12 · 2026-05-10T17:49:58.415Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0152Sno1kMwTUuCY2teHfjZr`</summary>

```json
{
  "query": "RSS 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c666479-2922-40a4-ae57-8e8adbc67928",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac48c331-077a-4d12-af9b-ab12d7a3eb77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 13 · 2026-05-10T17:49:58.424Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RtZRGga7Z4ThaF86RFp3Be`</summary>

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
  "parentUuid": "ac48c331-077a-4d12-af9b-ab12d7a3eb77",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed3a24f6-e668-4dfe-aeea-c49337731d2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 14 · 2026-05-10T17:49:58.889Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MYELyLMyRF6nRqahov9G2d`</summary>

```json
{
  "query": "CVPR 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed3a24f6-e668-4dfe-aeea-c49337731d2e",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "056d5a77-8301-4ea8-9915-15bd42425af6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 15 · 2026-05-10T17:49:59.390Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015hvWXekmjsKrZVEAHJ3HCJ`</summary>

```json
{
  "query": "best open source video generation model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "056d5a77-8301-4ea8-9915-15bd42425af6",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be1e1ca1-c992-4e52-86d0-6477f2bb2d99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 16 · 2026-05-10T17:49:59.985Z_

<details><summary>↩ Tool result · `toolu_01EzK2c4kEuHsQTuvHoTscgL`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline"

Links: [{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, I found information about ICLR 2027. ICLR 2027 will be held May 16-21, 2027 in Toronto, Canada. However, the specific submission deadline for ICLR 2027 was not provided in the search results.

For reference, I can tell you that ICLR 2026 has a paper submission deadline of September 24, but the exact deadline for the 2027 conference has not yet been officially announced or is not available in these search results. I recommend checking the official ICLR website (iclr.cc) when it posts the 2027 call for papers for the most current deadline information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "913e8294-d5e1-48ac-abfc-f85ced2bd3eb",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "d72e8fa2-14ac-477f-b8e0-ed6c943f506c",
  "sourceToolAssistantUUID": "913e8294-d5e1-48ac-abfc-f85ced2bd3eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T17:50:00.116Z_

<details><summary>↩ Tool result · `toolu_015xqaRwjQYxqfeEwZtjX5wF`</summary>

```text
Web search results for query: "ICRA 2027 submission deadline"

Links: [{"title":"IEEE ICRA 2027 | Calls for Papers and Posters","url":"https://2027.ieee-icra.org/contribute/"},{"title":"2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"},{"title":"ICRA - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"},{"title":"IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com","url":"https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1454"},{"title":"Conference Calender 2027 in Kanazawa Institute of Technology","url":"https://wwwr.kanazawa-it.ac.jp/kawai/calendar/2027/cal27.html"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Timetable 2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853/timetable.html"},{"title":"International Conference on Robotics and Automation","url":"https://roboticsforum.org/Conference/2027/ICRA/"}]

Based on the search results, I found that ICRA 2027 will be held May 24-28, 2027 in Seoul, South Korea. However, the search results do not contain specific information about the paper submission deadline for ICRA 2027.

The official ICRA 2027 website (2027.ieee-icra.org) appears in the search results, but the detailed deadline information wasn't captured in the excerpts. For the most current and accurate submission deadline, I recommend visiting the official ICRA 2027 website directly at https://2027.ieee-icra.org/contribute/ or checking the IEEE Robotics and Automation Society website for updated call for papers information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af328868-fc37-4ce3-a131-8ac25ee1236c",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "b625644b-344f-4371-a8b9-c4705dcd0097",
  "sourceToolAssistantUUID": "af328868-fc37-4ce3-a131-8ac25ee1236c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T17:50:00.301Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MaP6xWyarVuMpqU3maDtW2`</summary>

```json
{
  "query": "SOTA open source diffusion model video 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b625644b-344f-4371-a8b9-c4705dcd0097",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ed6b461-d714-4fe4-9a70-33664eb94870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 19 · 2026-05-10T17:50:00.775Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BG8wHDErTXPPnaBLz2yckH`</summary>

```json
{
  "query": "best open source vision language model robotics 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ed6b461-d714-4fe4-9a70-33664eb94870",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "177e7f30-8341-45c0-bd69-f563c10b8cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 20 · 2026-05-10T17:50:01.044Z_

<details><summary>↩ Tool result · `toolu_01LBqmHHpjsftJ5cpQFwG6oT`</summary>

```text
Web search results for query: "NeurIPS 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"NeurIPS 2026 Conference | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FConference"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"2026 Conference","url":"https://neurips.cc/Conferences/2026"},{"title":"NeurIPS Conference (@NeurIPSConf) / X","url":"https://x.com/NeurIPSConf"},{"title":"NeurIPS: Neural Information Processing Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2212"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"}]

Based on the search results, here are the submission deadlines for NeurIPS 2026:

The abstract submission deadline is May 4, 2026 (AOE), and the full paper submission deadline, including all supplementary materials, is May 6, 2026 AOE.

Note that the different tracks (main, evaluations and datasets, position papers) have different calls for papers, different submission portals, and possibly different timelines.

The Fortieth annual conference is held from Sunday, December 6th through Saturday the 12th, 2026, and author notification is September 24, 2026 (AoE).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df0654f5-5538-4d4b-a069-d983b7f92c23",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "c3957f2e-4446-441c-9a57-4c1bcfaba80a",
  "sourceToolAssistantUUID": "df0654f5-5538-4d4b-a069-d983b7f92c23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T17:50:00.834Z_

<details><summary>↩ Tool result · `toolu_01DQGoN5YiyTfwSkPhCbvGU5`</summary>

```text
Web search results for query: "IROS 2026 submission deadline"

Links: [{"title":"IROS 2026 | IEEE/RSJ International Conference on Intelligent Robots and Systems","url":"https://2026.ieee-iros.org/"},{"title":"The Call for Papers for IROS 2026 is officially OPEN! Join ...","url":"https://www.facebook.com/ieeeiros/posts/-the-call-for-papers-for-iros-2026-is-officially-openjoin-one-of-the-worlds-larg/862566436746807/"},{"title":"Start Page of the Conference Management System - PaperPlaza","url":"https://ras.papercept.net/conferences/scripts/start.pl"},{"title":"Update IROS 2026 conference data with official deadlines · huggingface/ai-deadlines at f5a1d9a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f5a1d9a7d8b4274d4c60ae755f25de60c466079d"},{"title":"International Conference on Intelligent Robots and Systems (IROS)","url":"https://www.allconferencealert.com/event/1870021"},{"title":"IROS: Intelligent RObots and Systems 2027 2026 2025 .. ...","url":"http://www.wikicfp.com/cfp/program?id=1660"},{"title":"IROS 2026 : Intelligent RObots and Systems","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?copyownerid=90704&eventid=191959"},{"title":"ieeeIROS (@ieeeiros) / X","url":"https://x.com/ieeeiros"},{"title":"Call for Papers - IROS 2026 | IEEE/RSJ International Conference on Intelligent Robots and Systems","url":"https://2026.ieee-iros.org/contribute/call-for-papers/"},{"title":"Important Dates - IROS 2026 | IEEE/RSJ International Conference on Intelligent Robots and Systems","url":"https://2026.ieee-iros.org/about/important-dates/"}]

Based on the search results, the paper submission deadline for IROS 2026 is March 2, 2026. Additionally, the paper video submission deadline is March 5, 2026.

IROS 2026 is being held September 27–October 1, 2026 in Pittsburgh, USA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c666479-2922-40a4-ae57-8e8adbc67928",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "6047757f-4a98-447d-8a69-bda3b16c4b1d",
  "sourceToolAssistantUUID": "2c666479-2922-40a4-ae57-8e8adbc67928",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-10T17:50:01.307Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WcrjvdzUBhevwUJvEYapNK`</summary>

```json
{
  "query": "open source video diffusion transformer 2026 state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6047757f-4a98-447d-8a69-bda3b16c4b1d",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauJzGKH6xzdpJ93d8cD6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b88cc7f7-dee2-4340-a0f3-5e7b391ff23f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3E182HynRd2NYS32VCJzi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9071,
      "output_tokens": 556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 556,
          "cache_read_input_tokens": 9071,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1413,
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

_source line 23 · 2026-05-10T17:50:01.337Z_

<details><summary>↩ Tool result · `toolu_01WJm5zPJwdYdrpjF73KjWpW`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Vincent Vanhoucke's Post","url":"https://www.linkedin.com/posts/vanhoucke_corl-2026-website-is-officially-live-at-http-activity-7432112475480817664-gBos"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, here are the CoRL 2026 submission deadlines:

The abstract submission deadline is May 26, 2026 11:59 UTC and the paper submission deadline is May 29, 2026 11:59 UTC.

Note that there's a clarification in the submission guidelines: The paper submission deadline is Thursday (5/28) EOD rather than Friday, which indicates the actual paper submission date may be May 28, 2026.

CoRL 2026 will be held in Austin, Texas, US, with conference dates of November 9-12, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75587a36-7009-4b3c-9adf-c8a496b905db",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "f203eb95-0fbd-4f22-98e7-ef812f162861",
  "sourceToolAssistantUUID": "75587a36-7009-4b3c-9adf-c8a496b905db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T17:50:01.732Z_

<details><summary>↩ Tool result · `toolu_0152Sno1kMwTUuCY2teHfjZr`</summary>

```text
Web search results for query: "RSS 2026 submission deadline"

Links: [{"title":"[Meetings] RSS 2026 Call for Papers","url":"https://groups.google.com/g/rl-list/c/NDYhLboynpg"},{"title":"Robotics: Science and Systems · A Robotics Conference","url":"https://roboticsconference.org/"},{"title":"Important dates – 10th Road Safety and Simulation Conference","url":"https://www.rss2026.org/important-dates/"},{"title":"Call for Papers · Robotics: Science and Systems","url":"https://roboticsconference.org/information/cfp/"},{"title":"Robotics: Science and Systems on X: \"📢 Save the Date! RSS 2026 will take place July 13–17, 2026 in Sydney, Australia. Submission deadlines to be announced soon (likely mid–late January 2026). 🦾 Prepare your best work! https://t.co/ybIds7mOMq\" / X","url":"https://x.com/RoboticsSciSys/status/1976107492808482875"},{"title":"RSS - Call for invited topic sessions for 2026 RSS International Conference now open","url":"https://rss.org.uk/news-publication/news-publications/2025/general-news/call-opens-for-invited-topic-sessions-for-rss-2026/"},{"title":"Call for Workshops · Robotics: Science and Systems","url":"https://roboticsconference.org/information/cfw/"},{"title":"RSS 2026 Conference Bournemouth, 7-10 September 2026","url":"https://rss.org.uk/getattachment/Training-Events/conference2026/Invited-topic-sessions/Guidance-for-Invited-Session-organisers-RSS-2026.pdf.aspx/?lang=en-GB"},{"title":"RSS 2026 Conference | OpenReview","url":"https://openreview.net/group?id=roboticsfoundation.org%2FRSS%2F2026%2FConference"},{"title":"Calendar - RSS Foundation","url":"https://roboticsfoundation.org/policies/calendar/"}]

Based on the search results, here are the submission deadlines for RSS 2026 (Robotics: Science and Systems):

**January 23, 2026, 11:59pm AoE:** Abstract/Title Submission Deadline
**January 30, 2026, 11:59pm AoE:** Paper Submission Deadline
**February 6, 2026, 11:59pm AoE:** Supplementary Material Submission Deadline

The RSS 2026 conference will be held July 13-17, 2026 in Sydney, Australia at the University of Technology Sydney.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac48c331-077a-4d12-af9b-ab12d7a3eb77",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "87523964-9240-4230-8ca9-26378a9f5325",
  "sourceToolAssistantUUID": "ac48c331-077a-4d12-af9b-ab12d7a3eb77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T17:50:02.686Z_

<details><summary>↩ Tool result · `toolu_01MYELyLMyRF6nRqahov9G2d`</summary>

```text
Web search results for query: "CVPR 2027 submission deadline"

Links: [{"title":"CVPR: Computer Vision and Pattern Recognition 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=628"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"2025 Dates and Deadlines - CVPR 2026","url":"https://cvpr.thecvf.com/Conferences/2025/Dates"},{"title":"Conference Calendar for Computer Vision, Image Analysis and Related Topics","url":"http://conferences.visionbib.com/Iris-Conferences.html"},{"title":"2027 IEEE/CVF Conference on Computer Vision and Pattern Recognition CVPR","url":"https://www.aconf.org/conf_182232.2027_IEEE/CVF_Conference_on_Computer_Vision_and_Pattern_Recognition.html"},{"title":"2027 Conference","url":"https://wacv.thecvf.com/"},{"title":"One Year Calendar of Computer Image Analysis, Computer Vision Conferences","url":"https://conferences.visionbib.com/Browse-data.php?year=2027"},{"title":"Important Dates and Deadlines - CVPR 2026","url":"https://cvpr.thecvf.com/Conferences/2026/Dates"},{"title":"CVPR 2026 - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, I found that CVPR 2027 will be held June 19-26, 2027. However, the specific submission deadline for CVPR 2027 is not yet available in the search results. The search results show information about CVPR 2026 submission deadlines, but the official CVPR 2027 submission deadline has not been announced yet.

For the most current information about CVPR 2027 submission deadlines, I recommend checking the official CVPR website at cvpr.thecvf.com or monitoring conference deadline tracking sites that will be updated once the organizers announce the specific dates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "056d5a77-8301-4ea8-9915-15bd42425af6",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "02f56670-a2ca-4a13-9bef-6cd612e8fe5e",
  "sourceToolAssistantUUID": "056d5a77-8301-4ea8-9915-15bd42425af6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T17:50:06.715Z_

<details><summary>↩ Tool result · `toolu_01RtZRGga7Z4ThaF86RFp3Be`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, the Forty-first Conference on Artificial Intelligence (AAAI 2027) will be held in Montréal, Québec, Canada from February 16-23, 2027.

However, regarding the submission deadline specifically, the AAAI 2027 paper submission deadline is TBD (to be determined). The official deadline has not yet been announced. That said, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

For the most up-to-date information, you can check the official AAAI conference website at aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed3a24f6-e668-4dfe-aeea-c49337731d2e",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "a72f8ae0-bec8-4b26-81b0-a5d1aa148a9a",
  "sourceToolAssistantUUID": "ed3a24f6-e668-4dfe-aeea-c49337731d2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T17:50:07.366Z_

<details><summary>↩ Tool result · `toolu_015hvWXekmjsKrZVEAHJ3HCJ`</summary>

```text
Web search results for query: "best open source video generation model 2026"

Links: [{"title":"7 Best Open Source Video Generation Models in 2026 [Updated February] | Hyperstack","url":"https://www.hyperstack.cloud/blog/case-study/best-open-source-video-generation-models"},{"title":"Best Open Source AI Video Generation Models in 2026 | Pixazo","url":"https://www.pixazo.ai/blog/best-open-source-ai-video-generation-models"},{"title":"Ultimate Guide - The Top Open Source AI Video Generation Models in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-models-for-video-to-text-transcription"},{"title":"Best Open Source Video Models 2026","url":"https://wavespeed.ai/landing/models/best-open-source-video-models-2026"},{"title":"31 Open-Source AI Video Models: Free Tools to Make Videos in 2026 — AI Free Forever","url":"https://aifreeforever.com/blog/open-source-ai-video-models-free-tools-to-make-videos"},{"title":"Ultimate Guide - The Top Open Source Video Generation Models in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-video-generation-models-2025"},{"title":"8 Best Open Source AI Video Generator Alternatives (2026)","url":"https://resource.digen.ai/open-source-ai-video-generator-alternatives/"},{"title":"Ultimate Guide - The Fastest Open Source Video Generation Models in 2026","url":"https://www.siliconflow.com/articles/en/fastest-open-source-video-generation-models"},{"title":"Best Open-Source AI Video Generators in 2026: Complete Rankings and Comparison Guide","url":"https://videodubber.ai/blogs/best-opensource-ai-video-generator-2026/"},{"title":"Ultimate Guide - The Best Open Source Models for Video Summarization in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-models-for-video-summarization"}]

Based on the search results, here are the best open-source video generation models in 2026:

## Top Models

The top open-source AI video generation models in 2026 include SkyReels V1, LTXVideo, Mochi 1, HunyuanVideo, Wan 2.1, MAGI-1 and Waver 1.0.

### Leading Performers by Category

**Best for Cinematic Quality:**
Wan 2.2 is widely regarded as one of the most cinematic open-source video generation models currently available. Wan2.2-T2V-A14B is ideal for text-to-video generation with its industry-first MoE architecture. For image-to-video transformation with cutting-edge MoE technology, Wan2.2-I2V-A14B leads the field. For fast, high-quality 720P video generation, Wan2.1-I2V-14B-720P-Turbo offers the best speed-to-quality ratio.

**Best for Speed:**
LTXVideo by Lightricks brings rapid, efficient and professional-grade video synthesis to any creator. Unlike heavyweight AI models that demand extensive computational power, LTXVideo is optimised to run smoothly on cost-effective GPUs like the NVIDIA RTX A6000.

**Best for Natural Motion:**
Mochi 1's asymmetric diffusion architecture produces the most natural motion physics of any open-source video model in 2026.

**Best for Longer Videos:**
Tencent built HunyuanVideo as their flagship open video model. The original release packed 13 billion parameters and needed serious GPU power. Version 1.5 trimmed this to 8.3 billion parameters while boosting speed. Now it runs on GPUs with 14GB of VRAM when using offloading.

The choice between models depends on your specific priorities—whether you prioritize cinematic realism, speed, motion quality, or longer video generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be1e1ca1-c992-4e52-86d0-6477f2bb2d99",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "28b5e364-fd2c-434d-98e5-4f573adb41a2",
  "sourceToolAssistantUUID": "be1e1ca1-c992-4e52-86d0-6477f2bb2d99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T17:50:09.100Z_

<details><summary>↩ Tool result · `toolu_01BG8wHDErTXPPnaBLz2yckH`</summary>

```text
Web search results for query: "best open source vision language model robotics 2026"

Links: [{"title":"Best Open-Source Vision Language Models of 2026","url":"https://www.labellerr.com/blog/top-open-source-vision-language-models/"},{"title":"Multimodal AI: The Best Open-Source Vision Language Models in 2026","url":"https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models"},{"title":"Top 10 Vision Language Models in 2026 | Benchmark, Use Cases","url":"https://dextralabs.com/blog/top-10-vision-language-models/"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Ultimate Guide - The Best Open Source Multimodal Models in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-multimodal-models-2025"},{"title":"The Fastest Open Source Multimodal Models in 2026","url":"https://www.siliconflow.com/articles/en/fastest-open-source-multimodal-models"},{"title":"Top 10 Vision Language Models in 2026 | DataCamp","url":"https://www.datacamp.com/blog/top-vision-language-models"},{"title":"RLWRLD Previews Open-Source Vision-Language-Action Model for Robotics at GTC 2026 - TipRanks.com","url":"https://www.tipranks.com/news/private-companies/rlwrld-previews-open-source-vision-language-action-model-for-robotics-at-gtc-2026"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"}]

Based on the web search results, here are the best open-source vision language models for robotics in 2026:

## Leading Models for Robotics

**Vision-Language-Action (VLA) Models:**

OpenVLA is a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations, building on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP. OpenVLA typically requires fine-tuning on a small demonstration dataset (~100 demos) from your target domain robot, though out-of-the-box it only works well on domains from the training dataset.

RLDX is described as RLWRLD's next-generation Vision-Language-Action model, and is expected to be released as open source with early access registration already being promoted.

**General Vision-Language Models for Robotics:**

DeepSeek-VL has strong reasoning capabilities designed for scientific and real-world vision tasks with use cases including visual reasoning for robotics and logical scene understanding.

GLM-4.6V closes the loop between perception, reasoning, and action, making it an ideal option for building visual agents that require both multimodal understanding and real-world task execution.

Gemma 3 is a strong open-source option with OCR and multilingual support for document analysis, medical imaging, and content moderation.

These models represent the cutting edge of open-source robotics vision technology available in 2026, with VLA models being specifically optimized for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "177e7f30-8341-45c0-bd69-f563c10b8cb8",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "7761dfe1-4087-40cb-8613-fa8ea94c43f2",
  "sourceToolAssistantUUID": "177e7f30-8341-45c0-bd69-f563c10b8cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T17:50:09.364Z_

<details><summary>↩ Tool result · `toolu_01WcrjvdzUBhevwUJvEYapNK`</summary>

```text
Web search results for query: "open source video diffusion transformer 2026 state of the art"

Links: [{"title":"7 Best Open Source Video Generation Models in 2026 [Updated February] | Hyperstack","url":"https://www.hyperstack.cloud/blog/case-study/best-open-source-video-generation-models"},{"title":"Ultimate Guide - The Top Open Source Video Generation Models in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-video-generation-models-2025"},{"title":"31 Open-Source AI Video Models: Free Tools to Make Videos in 2026 — AI Free Forever","url":"https://aifreeforever.com/blog/open-source-ai-video-models-free-tools-to-make-videos"},{"title":"Top 5 Open Source Video Generation Models - KDnuggets","url":"https://www.kdnuggets.com/top-5-open-source-video-generation-models"},{"title":"Best Open Source AI Video Generation Models in 2026 | Pixazo","url":"https://www.pixazo.ai/blog/best-open-source-ai-video-generation-models"},{"title":"Photorealistic Video Generation with Diffusion Models","url":"https://walt-video-diffusion.github.io/"},{"title":"State of open video generation models in Diffusers","url":"https://huggingface.co/blog/video_gen"},{"title":"LTX-2: The First Open-Source Model That Generates | Introl Blog","url":"https://introl.com/blog/ltx-2-audiovisual-diffusion-synchronized-video-audio-2026"},{"title":"Ultimate Guide - The Best Open Source Models for Video Summarization in 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-models-for-video-summarization"},{"title":"SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer | OpenReview","url":"https://openreview.net/forum?id=mzAchylAtf"}]

Here's what the search reveals about the state-of-the-art in open-source video diffusion transformers for 2026:

## Leading Models

HunyuanVideo is a 13-billion-parameter model that has set a new standard for open-source video generation, with performance beating state-of-the-art models like Runway Gen-3, excelling in cinematic quality, motion accuracy and ecosystem support.

Wan 2.2 upgrades its diffusion backbone with a Mixture-of-Experts (MoE) architecture that splits denoising across timesteps into specialized experts, and compared to Wan 2.1, training scaled substantially, with Wan 2.2 reporting top-tier performance among both open and closed systems.

Mochi 1 is a 10-billion-parameter diffusion model that has redefined open-source video generation. It's an Asymmetric Diffusion Transformer (AsymmDiT) trained from scratch, released under Apache 2.0, coupling with an Asymmetric VAE that compresses videos 8x8 spatially and 6x temporally into a 12-channel latent.

## Recent Innovations

LTX-2, released January 6, 2026, generates synchronized video and audio in a single unified pass, delivering native 4K resolution at 50 frames per second with expressive sound, accurate lip sync, and rich ambient audio.

SANA-Video achieves competitive performance compared to modern state-of-the-art small diffusion models while being 16x faster in measured latency, and can be deployed on RTX 5090 GPUs, accelerating the inference speed of generating a 5-second 720p video from 71s to 29s.

## Key Architectural Trends

Modern models utilize a diffusion transformer architecture and enhance generation capabilities through innovative spatiotemporal variational autoencoders (VAE), scalable training strategies, and large-scale data construction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b88cc7f7-dee2-4340-a0f3-5e7b391ff23f",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "1aacecbf-bd42-4f8f-87a7-4b773c0ce0d4",
  "sourceToolAssistantUUID": "b88cc7f7-dee2-4340-a0f3-5e7b391ff23f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T17:50:10.090Z_

<details><summary>↩ Tool result · `toolu_01MaP6xWyarVuMpqU3maDtW2`</summary>

```text
Web search results for query: "SOTA open source diffusion model video 2026"

Links: [{"title":"Five Open-Source Models for Video Generation | by Mayur Jain | MLWorks | Medium","url":"https://medium.com/mlworks/five-open-source-models-for-video-generation-608ce4fe8698"},{"title":"GitHub - NVlabs/rcm: [ICLR 2026] rCM: SOTA JVP-Based Diffusion Distillation & Few-Step Video Generation & Scaling Up sCM/MeanFlow · GitHub","url":"https://github.com/NVlabs/rcm"},{"title":"Top 5 Open Source Video Generation Models - KDnuggets","url":"https://www.kdnuggets.com/top-5-open-source-video-generation-models"},{"title":"Text-to-video model - Wikipedia","url":"https://en.wikipedia.org/wiki/Text-to-video_model"},{"title":"GitHub - Yaofang-Liu/Pusa-VidGen: Pusa: Thousands Timesteps Video Diffusion Model · GitHub","url":"https://github.com/Yaofang-Liu/Pusa-VidGen"},{"title":"How Much Power does a SOTA Open Video Model Use? ⚡🎥","url":"https://huggingface.co/blog/jdelavande/text-to-video-energy-cost"},{"title":"What Are the SOTA AI Models? | Machine Learning Glossary","url":"https://maddevs.io/glossary/state-of-the-art-models/"},{"title":"Allegro New Open Source SOTA Text to Video Model 27 Amazing Examples With Prompts Apache License · FurkanGozukara/Stable-Diffusion Wiki · GitHub","url":"https://github.com/FurkanGozukara/Stable-Diffusion/wiki/Allegro-New-Open-Source-SOTA-Text-to-Video-Model-27-Amazing-Examples-With-Prompts-Apache-License"},{"title":"Genmo Mochi 1 — SOTA Video Generation Model — Full ...","url":"https://www.linkedin.com/pulse/genmo-mochi-1-sota-video-generation-model-full-swarmui-g%C3%B6z%C3%BCkara-bshhf"},{"title":"GitHub - VideoVerses/VideoTuna: Let's finetune video generation models! · GitHub","url":"https://github.com/VideoVerses/VideoTuna"}]

Based on the search results, here's what I found about state-of-the-art open-source diffusion models for video generation in 2026:

## Leading Open-Source Video Diffusion Models

Wan 2.2 reports top-tier performance among both open and closed systems. Wan 2.2 upgrades its diffusion backbone with a Mixture-of-Experts (MoE) architecture that splits denoising across timesteps into specialized experts, increasing effective capacity without a compute penalty. The model also includes aesthetic enhancements, with training scaled substantially (+65.6% images, +83.2% videos), improving motion, semantics, and aesthetics compared to its predecessor.

Other notable open-source models include:

- **Mochi 1**: A 10B Asymmetric Diffusion Transformer (AsymmDiT) trained from scratch, released under Apache 2.0, coupled with an Asymmetric VAE that compresses videos 8x8 spatially and 6x temporally into a 12-channel latent.

- **HunyuanVideo**: A 13B-parameter open video foundation model trained in a spatial–temporal latent space via a causal 3D variational autoencoder (VAE).

- **Allegro**: A powerful text-to-video model that generates high-quality videos up to 6 seconds at 15 FPS and 720p resolution from simple text input, currently open source state-of-the-art (SOTA) text to video model.

Additionally, rCM: SOTA JVP-Based Diffusion Distillation & Few-Step Video Generation & Scaling Up sCM/MeanFlow represents recent research advances, with continuous-time consistency distillation scaled up to 10B+ parameter video diffusion models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ed6b461-d714-4fe4-9a70-33664eb94870",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "6365b6ea-1de8-4fe5-a433-ace0078f72ac",
  "sourceToolAssistantUUID": "4ed6b461-d714-4fe4-9a70-33664eb94870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T17:50:13.245Z_

Let me get more details on the ICRA 2027 and ICLR 2027 deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6365b6ea-1de8-4fe5-a433-ace0078f72ac",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauK1UfDMEgYjYRDDhbDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6370b66d-820b-40d2-9e61-af56ef4c3dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y75ag4Ln8fsLr3ZNAmTxiC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1932,
      "cache_creation_input_tokens": 10026,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10026,
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

_source line 32 · 2026-05-10T17:50:14.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Qrsm5tFqPVjQZt7SFB3X2`</summary>

```json
{
  "query": "ICRA 2027 paper submission deadline date September October 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6370b66d-820b-40d2-9e61-af56ef4c3dfd",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauK1UfDMEgYjYRDDhbDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c26111c-36d3-4ce3-9b66-4b300776f7c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y75ag4Ln8fsLr3ZNAmTxiC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1932,
      "cache_creation_input_tokens": 10026,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10026,
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

_source line 33 · 2026-05-10T17:50:14.021Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TJdnMe4des1x2fXCtksq5S`</summary>

```json
{
  "query": "ICLR 2027 paper submission deadline date October 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c26111c-36d3-4ce3-9b66-4b300776f7c4",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauK1UfDMEgYjYRDDhbDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33fb1380-28e0-4a2d-a9da-95ffbd383738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y75ag4Ln8fsLr3ZNAmTxiC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1932,
      "cache_creation_input_tokens": 10026,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10026,
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

_source line 34 · 2026-05-10T17:50:14.534Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X2ufLWuHLoP71s6YDjCtQW`</summary>

```json
{
  "query": "AAAI 2027 paper submission deadline date August 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33fb1380-28e0-4a2d-a9da-95ffbd383738",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauK1UfDMEgYjYRDDhbDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4d199db-052f-4926-8dd0-1cd84ba60e48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y75ag4Ln8fsLr3ZNAmTxiC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1932,
      "cache_creation_input_tokens": 10026,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10026,
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

_source line 35 · 2026-05-10T17:50:14.878Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T8CUgXSPPKavhFesUyxHHA`</summary>

```json
{
  "query": "CVPR 2027 paper submission deadline date November 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4d199db-052f-4926-8dd0-1cd84ba60e48",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauK1UfDMEgYjYRDDhbDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72c3b884-51b5-4df3-91d6-3b719853d653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y75ag4Ln8fsLr3ZNAmTxiC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1932,
      "cache_creation_input_tokens": 10026,
      "cache_read_input_tokens": 8223,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10026
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1932,
          "output_tokens": 243,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 10026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10026,
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

_source line 36 · 2026-05-10T17:50:17.472Z_

<details><summary>↩ Tool result · `toolu_01X2ufLWuHLoP71s6YDjCtQW`</summary>

```text
Web search results for query: "AAAI 2027 paper submission deadline date August 2026"

Links: [{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"The 40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"MPC Deadlines Hub","url":"https://mpc-deadlines.github.io/"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"}]

Based on the search results, here's what I found about the AAAI 2027 paper submission deadline:

The AAAI 2027 paper submission deadline is August 1, 2026, with an abstract deadline of July 25, 2026.

Additionally, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns. AAAI 2027 will be held February 16-23, 2027 in Montréal, Québec, Canada.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4d199db-052f-4926-8dd0-1cd84ba60e48",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "3def4978-492c-4829-b372-0e4bfb74d00c",
  "sourceToolAssistantUUID": "e4d199db-052f-4926-8dd0-1cd84ba60e48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T17:50:17.873Z_

<details><summary>↩ Tool result · `toolu_01TJdnMe4des1x2fXCtksq5S`</summary>

```text
Web search results for query: "ICLR 2027 paper submission deadline date October 2026"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"2025 Dates and Deadlines","url":"https://iclr.cc/Conferences/2025/Dates"},{"title":"International Conference on Learning Representations ICLR in October 2027 in Lisbon","url":"https://waset.org/learning-representations-conference-in-october-2027-in-lisbon"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"International Conference on Learning Representations (ICLR)","url":"https://waset.org/learning-representations-conference"}]

Based on the search results, I found information about ICLR 2027. However, the results show various conferences affiliated with "International Conference on Learning Representations," but they appear to be hosted by WASET (World Academy of Science, Engineering and Technology) rather than the official ICLR conference.

For the official ICLR 2027 conference, the abstract/full-text paper submission deadline is April 01, 2026, with a notification of acceptance/rejection on May 01, 2026, and a conference date of October 28-29, 2027.

Note: I couldn't find a submission deadline specifically in October 2026 for ICLR 2027 in the official ICLR sources. The official deadline appears to be in April 2026. If you're looking for information about a different submission deadline or a satellite/partner conference event in October 2026, please let me know and I can search for more specific information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33fb1380-28e0-4a2d-a9da-95ffbd383738",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "a72b4ff5-a034-488a-963d-d96b6ab6ebb8",
  "sourceToolAssistantUUID": "33fb1380-28e0-4a2d-a9da-95ffbd383738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T17:50:19.051Z_

<details><summary>↩ Tool result · `toolu_01T8CUgXSPPKavhFesUyxHHA`</summary>

```text
Web search results for query: "CVPR 2027 paper submission deadline date November 2026"

Links: [{"title":"CVPR 2026 - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/"},{"title":"CVPR: Computer Vision and Pattern Recognition 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=628"},{"title":"Important Dates and Deadlines - CVPR 2026","url":"https://cvpr.thecvf.com/Conferences/2026/Dates"},{"title":"CVPR 2026 Call for Papers - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/Conferences/2026/CallForPapers"},{"title":"2025 Dates and Deadlines - CVPR 2026","url":"https://cvpr.thecvf.com/Conferences/2025/Dates"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"2026 Conference - CVPR - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/Conferences/2026"},{"title":"Conference Calendar for Computer Vision, Image Analysis and Related Topics","url":"http://conferences.visionbib.com/Iris-Conferences.html"},{"title":"CVPR 2026 Guide: Dates, Deadlines, Topics & Tips for Denver","url":"https://conferenceinc.net/post/cvpr-2026/"}]

Based on the search results, I found information about CVPR 2026, but the search did not return specific details about CVPR 2027 submission deadlines. The results show that the CVPR 2026 submission deadline was November 13, 2025, and there is a pattern of CVPR holding deadlines in November.

However, the search results do not contain published information about the CVPR 2027 paper submission deadline in November 2026. CVPR 2027 details may not yet be officially announced, as conference organizers typically announce these deadlines several months in advance. I recommend checking the official CVPR website (cvpr.thecvf.com) or contacting the conference organizers directly for the most current information about CVPR 2027 submission deadlines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72c3b884-51b5-4df3-91d6-3b719853d653",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "790cc0d1-d81a-4aef-992c-facad1bd2dcf",
  "sourceToolAssistantUUID": "72c3b884-51b5-4df3-91d6-3b719853d653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T17:50:23.353Z_

<details><summary>↩ Tool result · `toolu_018Qrsm5tFqPVjQZt7SFB3X2`</summary>

```text
Web search results for query: "ICRA 2027 paper submission deadline date September October 2026"

Links: [{"title":"ICARA 2027 | Automation, Robotics and Applications","url":"https://www.icara.us/"},{"title":"2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"IEEE ICRA 2027 | Calls for Papers and Posters","url":"https://2027.ieee-icra.org/contribute/"},{"title":"ICRA 2026 Papers - Submission closed - IEEE ICRA 2026","url":"https://2026.ieee-icra.org/contribute/call-for-icra-2026-papers-now-accepting-submissions/"},{"title":"ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1454"},{"title":"ICRA - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"},{"title":"ICRA (@IEEE.RAS.ICRA)","url":"https://www.facebook.com/IEEE.RAS.ICRA/"},{"title":"IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com","url":"https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"},{"title":"Workshop on Field Robotics - ICRA 2026","url":"https://norlab-ulaval.github.io/icra_workshop_field_robotics/"}]

Let me search for more specific information about ICRA 2027's paper submission deadline.

Links: [{"title":"IEEE ICRA 2026 | Calls for Papers and Posters","url":"https://2026.ieee-icra.org/contribute/"},{"title":"IEEE ICRA on X: \"Final Reminder: ICRA 2026 Paper Submission Deadline – 15 September 2025 (23:59 PST)! Submit your cutting-edge robotics research to the flagship IEEE Robotics &amp; Automation conference. Learn more about the submission process: https://t.co/lopnwGFNTd https://t.co/4FMfIL93Tl\" / X","url":"https://x.com/ieee_ras_icra/status/1966540573549973863"},{"title":"2027 IEEE International Conference on Robotics ... - ICRA 2026","url":"https://2027.ieee-icra.org/"},{"title":"Paper Submission Deadline is Extended to Sept 16, 23:59 PST","url":"https://2026.ieee-icra.org/announcements/paper-submission-deadline-is-extended-to-sept-16-2359-pst/"},{"title":"Final Reminder: ICRA 2026 Paper Submission Deadline – 15 September 2025 (23:59 PST)! Submit your cutting-edge robotics research to the flagship IEEE Robotics & Automation conference. 📄 8-page limit… | IEEE International Conference on Robotics and Automation (ICRA)","url":"https://www.linkedin.com/posts/ieee-icra_final-reminder-icra-2026-paper-submission-activity-7372306265139474432-Ath8"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"},{"title":"ICRA - Final Reminder: ICRA 2026 Paper Submission ...","url":"https://www.facebook.com/IEEE.RAS.ICRA/photos/final-reminder-icra-2026-paper-submission-deadline-15-september-2025-2359-pstsub/1188552156639438/"},{"title":"ICRA - Final Reminder: ICRA 2026 Paper Submission Deadline...","url":"https://www.facebook.com/IEEE.RAS.ICRA/posts/final-reminder-icra-2026-paper-submission-deadline-15-september-2025-2359-pstsub/1188552229972764/"},{"title":"Workshop on Field Robotics - ICRA 2026","url":"https://norlab-ulaval.github.io/icra_workshop_field_robotics/"}]

Let me search more specifically for ICRA 2027 call for papers and deadlines.

No links found.

Let me try another search to find the ICRA 2027 official call for papers.

Links: [{"title":"IEEE ICRA 2027 | Calls for Papers and Posters","url":"https://2027.ieee-icra.org/contribute/"},{"title":"2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"},{"title":"2026 IEEE International Conference on Robotics and Automation (ICRA)","url":"https://2026.ieee-icra.org/"},{"title":"ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1454"},{"title":"IEEE ICRA 2025 | Calls for Papers and Posters","url":"https://2025.ieee-icra.org/contribute/"},{"title":"IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com","url":"https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"},{"title":"ICRA (@ieee_ras_icra) / X","url":"https://twitter.com/ieee_ras_icra?lang=en"},{"title":"Call for Papers | ICRA 2019","url":"https://ewh.ieee.org/soc/ras/conf/fullysponsored/icra/ICRA2019/www.icra2019.org/contribute/call-for-papers.html"},{"title":"ICRA - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"}]

Based on my search results, I found that the ICRA 2027 official website at 2027.ieee-icra.org/contribute/ currently shows information that appears to be outdated (showing 2024 and 2025 deadlines). However, I can provide you with some information about the conference:

IEEE ICRA 2027 will be held in Seoul, South Korea, from May 24-28, 2027.

Unfortunately, the official call for papers and submission deadline for ICRA 2027 have not yet been formally announced on the official website or in the search results. Based on the pattern from previous years, ICRA typically announces paper submission deadlines in the September timeframe for conferences held in May/June of the following year. ICRA 2026 had submissions due by September 15, 2025, and ICRA 2025 had submissions due by September 15, 2024.

I recommend checking the official ICRA 2027 website directly at 2027.ieee-icra.org or following the IEEE Robotics and Automation Society's official channels for the most current announcement of the ICRA 2027 paper submission deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c26111c-36d3-4ce3-9b66-4b300776f7c4",
  "isSidechain": true,
  "promptId": "da64154d-656a-4564-986a-8025bbe1fefd",
  "agentId": "a29aae6d27db48991",
  "type": "user",
  "uuid": "e51d5ac0-7679-41f6-8f8c-c804d4bc8a9e",
  "sourceToolAssistantUUID": "4c26111c-36d3-4ce3-9b66-4b300776f7c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-10T17:51:09.918Z_

Here is a comprehensive report of all findings.

---

## Part 1: Conference Venue Deadlines After May 10, 2026

Only venues with submission deadlines **after** May 10, 2026 are listed as actionable. The rest are noted as either already passed or not yet announced.

### Deadlines AFTER May 10, 2026 (actionable)

| Venue | Deadline | Notes |
|-------|----------|-------|
| **CoRL 2026** | Abstract: **May 26, 2026**; Paper: **May 28-29, 2026** (11:59 UTC) | Conference: Nov 9-12, 2026, Austin, TX |
| **AAAI 2027** | Abstract: **July 25, 2026**; Paper: **August 1, 2026** | Conference: Feb 16-23, 2027, Montreal, Canada |
| **ICRA 2027** | Expected **~September 2026** (not yet officially announced) | Conference: May 24-28, 2027, Seoul, South Korea. Based on pattern (ICRA 2026 was Sep 15, 2025) |
| **CVPR 2027** | Expected **~November 2026** (not yet officially announced) | Conference: June 19-26, 2027. Based on pattern (CVPR 2026 was Nov 13, 2025) |
| **ICLR 2027** | **Not yet announced** | Conference: May 16-21, 2027, Toronto, Canada. Expected ~October 2026 based on prior years |

### Deadlines BEFORE May 10, 2026 (already passed)

| Venue | Deadline | Status |
|-------|----------|--------|
| **NeurIPS 2026** | Abstract: May 4, 2026; Paper: May 6, 2026 (AOE) | **Already passed** |
| **IROS 2026** | Paper: March 2, 2026 | **Already passed** |
| **RSS 2026** | Abstract: Jan 23, 2026; Paper: Jan 30, 2026 | **Already passed** |

---

## Part 2: Current SOTA Open-Source Models

### Video Generation Models

| Model | Parameters | Key Capabilities |
|-------|-----------|------------------|
| **Wan 2.2** | 14B (MoE) | Industry-first Mixture-of-Experts architecture for video diffusion. Top-tier performance among both open and closed systems. Splits denoising across timesteps into specialized experts. Variants: T2V-A14B (text-to-video), I2V-A14B (image-to-video). Training scaled +65.6% images, +83.2% videos over Wan 2.1. |
| **HunyuanVideo (Tencent)** | 13B (v1), 8.3B (v1.5) | Open video foundation model trained in spatial-temporal latent space via causal 3D VAE. Beats Runway Gen-3 in benchmarks. V1.5 runs on GPUs with 14GB VRAM using offloading. |
| **Mochi 1 (Genmo)** | 10B | Asymmetric Diffusion Transformer (AsymmDiT) trained from scratch. Apache 2.0 license. Asymmetric VAE compresses 8x8 spatially, 6x temporally. Best natural motion physics among open-source models. |
| **LTX-2 (Lightricks)** | -- | Released Jan 6, 2026. First open-source model generating synchronized video and audio in a single pass. Native 4K at 50fps with lip sync and ambient audio. Optimized for consumer GPUs (RTX A6000). |
| **SANA-Video** | -- | 16x faster than comparable models. Competitive with SOTA small diffusion models. Can deploy on RTX 5090, generating 5-sec 720p video in 29 seconds. |
| **SkyReels V1** | -- | Notable open-source video generation model for 2026. |

### Vision-Language Models for Robotics

| Model | Parameters | Key Capabilities |
|-------|-----------|------------------|
| **OpenVLA** | 7B | Vision-Language-Action model trained on 970k real-world robot demonstrations. Built on Llama 2 + DINOv2 + SigLIP. Fine-tunable with ~100 demos for target domain. Apache 2.0. |
| **RLDX (RLWRLD)** | -- | Next-gen VLA model previewed at GTC 2026. Expected open-source release. Designed for robotic manipulation. |
| **DeepSeek-VL** | -- | Strong reasoning for scientific and real-world vision tasks including visual reasoning for robotics and logical scene understanding. |
| **GLM-4.6V** | -- | Closes the loop between perception, reasoning, and action. Suitable for visual agents requiring multimodal understanding and real-world task execution. |

### Key Architectural Trends (2026)
- **Diffusion Transformers (DiT)** are the dominant architecture for video generation
- **Mixture-of-Experts (MoE)** is being adopted to increase effective capacity without compute penalty
- **Spatiotemporal VAEs** compress video into efficient latent spaces
- **Vision-Language-Action (VLA)** models are bridging the gap between perception and robotic control
- **Distillation methods** (rCM) are scaling consistency models to 10B+ parameters for few-step generation

---

Sources:
- [NeurIPS 2026 Dates and Deadlines](https://neurips.cc/Conferences/2026/Dates)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [IROS 2026 Important Dates](https://2026.ieee-iros.org/about/important-dates/)
- [RSS 2026 Call for Papers](https://roboticsconference.org/information/cfp/)
- [ICRA 2027 Official Site](https://2027.ieee-icra.org/contribute/)
- [ICLR Conference](https://iclr.cc/)
- [AAAI Conference on AI](https://aaai.org/conference/aaai/)
- [AAAI 2027 Deadline Tracker](https://www.getpaperpilot.com/deadlines/aaai-2027.html)
- [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)
- [CVPR 2026 Dates](https://cvpr.thecvf.com/Conferences/2026/Dates)
- [Best Open Source Video Generation Models 2026 (Hyperstack)](https://www.hyperstack.cloud/blog/case-study/best-open-source-video-generation-models)
- [Best Open Source AI Video Generation Models (Pixazo)](https://www.pixazo.ai/blog/best-open-source-ai-video-generation-models)
- [Open Source Video Generation Models (SiliconFlow)](https://www.siliconflow.com/articles/en/best-open-source-video-generation-models-2025)
- [rCM: SOTA Diffusion Distillation (NVlabs)](https://github.com/NVlabs/rcm)
- [LTX-2 Audiovisual Diffusion (Introl)](https://introl.com/blog/ltx-2-audiovisual-diffusion-synchronized-video-audio-2026)
- [SANA-Video (OpenReview)](https://openreview.net/forum?id=mzAchylAtf)
- [OpenVLA (arXiv)](https://arxiv.org/abs/2406.09246)
- [OpenVLA GitHub](https://github.com/openvla/openvla)
- [RLWRLD VLA Model Preview](https://www.tipranks.com/news/private-companies/rlwrld-previews-open-source-vision-language-action-model-for-robotics-at-gtc-2026)
- [Best Open-Source Vision Language Models 2026 (Labellerr)](https://www.labellerr.com/blog/top-open-source-vision-language-models/)
- [Multimodal AI VLMs (BentoML)](https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models)
- [State of Open Video Generation in Diffusers (Hugging Face)](https://huggingface.co/blog/video_gen)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e51d5ac0-7679-41f6-8f8c-c804d4bc8a9e",
  "isSidechain": true,
  "agentId": "a29aae6d27db48991",
  "requestId": "req_011CauK2TNbhejcZG9vfUVzd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4765bd43-b213-4243-8c3f-4f877f442bb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6812a6c8-90b0-483e-bdcc-09921dacbad0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxJHLShMkpNxqRgv7rU8WR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1967,
      "cache_creation_input_tokens": 4223,
      "cache_read_input_tokens": 18249,
      "output_tokens": 2157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4223
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1967,
          "output_tokens": 2157,
          "cache_read_input_tokens": 18249,
          "cache_creation_input_tokens": 4223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4223,
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
