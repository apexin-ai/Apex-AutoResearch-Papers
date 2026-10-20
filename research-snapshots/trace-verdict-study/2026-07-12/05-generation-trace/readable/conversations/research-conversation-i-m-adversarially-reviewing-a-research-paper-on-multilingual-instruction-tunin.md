# Research conversation: I'm adversarially reviewing a research paper on multilingual instruction tuning that uses typological distances to weigh

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 102
- **Recorded user turns:** 1
- **Tool calls:** 46
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6a68117d153347f2.jsonl`
- **Structured JSON:** [`f729c85b93005621088f.json`](../../sessions/f7/f729c85b93005621088f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

102 recorded events

### User

_source line 1 · 2026-05-10T07:25:29.350Z_

I'm adversarially reviewing a research paper on multilingual instruction tuning that uses typological distances to weight training data from multiple source languages (called "multi-pivot" instruction tuning). I need to find any papers that might compete with or invalidate this idea.

Please search for:

1. Papers on curriculum learning for multilingual/cross-lingual NLP published in 2025-2026:
   - "curriculum learning cross-lingual transfer 2025"
   - "staged training multilingual language model 2025 2026"
   - site:arxiv.org curriculum multilingual instruction tuning 2025

2. Papers on data selection/weighting for multilingual fine-tuning:
   - "data selection multilingual fine-tuning typological 2025"
   - "language-weighted data sampling cross-lingual NLP"
   - "source language selection instruction tuning 2025 2026"

3. Papers specifically on instruction tuning for Kazakh, Mongolian, Uyghur (to check if the gap still exists):
   - "Mongolian language model instruction tuning 2025 2026"
   - "Uyghur language model NLP 2025"
   - "Central Asian languages LLM 2025 2026"

4. Search for KazMMLU (arXiv:2502.12829) and TUMLU (arXiv:2502.11020) to verify they are real ACL 2025 papers

5. Search for MiLiC-Eval (arXiv:2503.01150) to verify it's real and covers Uyghur/Mongolian/Kazakh/Tibetan

6. Search openreview.net for EMNLP 2026 papers on cross-lingual instruction tuning to check for very recent accepted work in this space

7. Search for "Implicit Cross-Lingual Rewarding" (arXiv:2503.04647) to verify this is a real ACL 2025 Findings paper on DPO for cross-lingual alignment

Please be specific about what you find and what URLs/papers you actually locate vs. what returns no results. Report paper titles, IDs, and key content claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "1476e655-0a4f-41f2-8a5c-d5f4c90156d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T07:25:29.353Z_

```json
{
  "parentUuid": "1476e655-0a4f-41f2-8a5c-d5f4c90156d4",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
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
  "uuid": "8fe79757-baf5-4ec0-bd1e-e7c2b5565e35",
  "timestamp": "2026-05-10T07:25:29.353Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T07:25:31.928Z_

I'll search for all these papers systematically. Let me run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fe79757-baf5-4ec0-bd1e-e7c2b5565e35",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNcUkbbidTVHHjWpho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c0398da-8a0e-4750-b1a6-a83c145feb03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018LUnbaiiCiZzVZdLtQmyjz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 8088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1065,
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

_source line 4 · 2026-05-10T07:25:32.190Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XdEsv6uS67VfXLhHzBQhGZ`</summary>

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
  "parentUuid": "9c0398da-8a0e-4750-b1a6-a83c145feb03",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNcUkbbidTVHHjWpho",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37ae0f1f-1bea-4b57-aebf-a9423a789d41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018LUnbaiiCiZzVZdLtQmyjz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 8088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1065,
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

_source line 5 · 2026-05-10T07:25:32.194Z_

<details><summary>↩ Tool result · `toolu_01XdEsv6uS67VfXLhHzBQhGZ`</summary>

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
  "parentUuid": "37ae0f1f-1bea-4b57-aebf-a9423a789d41",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "be4b704b-5392-4976-a348-e15d3ab61a8e",
  "sourceToolAssistantUUID": "37ae0f1f-1bea-4b57-aebf-a9423a789d41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T07:25:35.825Z_

I'll run all searches in parallel to cover the full scope of your request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be4b704b-5392-4976-a348-e15d3ab61a8e",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94fa42b0-e259-463d-8669-2fcba80d1ea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 7 · 2026-05-10T07:25:36.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PGiVtu8TNLcfBd5DjBJvoC`</summary>

```json
{
  "query": "curriculum learning cross-lingual transfer 2025 instruction tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94fa42b0-e259-463d-8669-2fcba80d1ea0",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90a35b0d-53c8-47d9-933b-58d9f982f6f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 8 · 2026-05-10T07:25:37.005Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015xT49R2Ta6HuybMaCSwEc7`</summary>

```json
{
  "query": "staged training multilingual language model 2025 2026 instruction tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90a35b0d-53c8-47d9-933b-58d9f982f6f1",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7f534e5-dd0c-4bdd-9f83-b3b0dd18f3a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 9 · 2026-05-10T07:25:37.444Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hd9Q92399y3FDjvSRj8GeJ`</summary>

```json
{
  "query": "data selection multilingual fine-tuning typological distance 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7f534e5-dd0c-4bdd-9f83-b3b0dd18f3a2",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "894748dc-46cc-4094-b647-82103883e2c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 10 · 2026-05-10T07:25:38.434Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014tzc3A8ULZjtqcSjonQXJq`</summary>

```json
{
  "query": "source language selection instruction tuning cross-lingual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "894748dc-46cc-4094-b647-82103883e2c6",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18554f64-458a-4a49-a24f-e319c49794d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 11 · 2026-05-10T07:25:39.158Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y76xK2H7vyNZLKHuWUSkLR`</summary>

```json
{
  "query": "Mongolian language model instruction tuning LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18554f64-458a-4a49-a24f-e319c49794d7",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a83bb0f-d8d1-4e5f-bf57-2b1319a00538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 12 · 2026-05-10T07:25:39.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RPBth4Cm1h3svWzm9gqEnu`</summary>

```json
{
  "query": "Uyghur language model NLP instruction tuning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a83bb0f-d8d1-4e5f-bf57-2b1319a00538",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1c0164b-4417-4f3b-b9e9-31a68fea4e4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 13 · 2026-05-10T07:25:40.340Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0157tH81DyGJUg534TSR71ha`</summary>

```json
{
  "query": "Central Asian languages LLM instruction tuning Kazakh 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1c0164b-4417-4f3b-b9e9-31a68fea4e4c",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fb99beb-a34b-4795-b92a-fa8953c79211",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 14 · 2026-05-10T07:25:40.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EPJEALQVNJ3NMDENBkPqxi`</summary>

```json
{
  "query": "KazMMLU arXiv 2502.12829"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fb99beb-a34b-4795-b92a-fa8953c79211",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d78d1d3c-43bc-4efa-b441-0bab45d3b3b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 15 · 2026-05-10T07:25:41.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jnn9JZAfdybzxCjca6pboM`</summary>

```json
{
  "query": "TUMLU arXiv 2502.11020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d78d1d3c-43bc-4efa-b441-0bab45d3b3b2",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3624b8a3-5daf-4e38-af91-fab1493981d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 16 · 2026-05-10T07:25:42.460Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LAGptrrdF3W4zoYYxQ1ipk`</summary>

```json
{
  "query": "MiLiC-Eval arXiv 2503.01150 Uyghur Mongolian Kazakh Tibetan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3624b8a3-5daf-4e38-af91-fab1493981d1",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fd85472-a633-4e31-8f1c-9f755e808526",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 17 · 2026-05-10T07:25:43.316Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FuP1EiBDFvGCUwSSd8w8U9`</summary>

```json
{
  "query": "Implicit Cross-Lingual Rewarding arXiv 2503.04647 DPO ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fd85472-a633-4e31-8f1c-9f755e808526",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc41d552-3f95-4e1d-ad98-78290acf9abb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 18 · 2026-05-10T07:25:43.714Z_

<details><summary>↩ Tool result · `toolu_01PGiVtu8TNLcfBd5DjBJvoC`</summary>

```text
Web search results for query: "curriculum learning cross-lingual transfer 2025 instruction tuning"

Links: [{"title":"Code-Switching Curriculum Learning for Multilingual ...","url":"https://aclanthology.org/2025.findings-acl.407.pdf"},{"title":"XCOT: Cross-lingual Instruction Tuning for Cross-lingual","url":"https://ojs.aaai.org/index.php/AAAI/article/download/34524/36679"},{"title":"Cross-Lingual Knowledge Transfer","url":"https://www.emergentmind.com/topics/cross-lingual-knowledge-transfer"},{"title":"XCOT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34524"},{"title":"Enhancing LLM Language Adaption through Cross-lingual ...","url":"https://aclanthology.org/2025.emnlp-main.1380.pdf"},{"title":"Making LLMs Better Many-to-Many Speech-to-Text ...","url":"https://aclanthology.org/2025.acl-long.610.pdf"},{"title":"Published in Transactions on Machine Learning Research (11/2025)","url":"https://openreview.net/pdf?id=oapsbIO1Bd"},{"title":"Persian-Phi: Efficient Cross-Lingual Adaptation of Compact ...","url":"https://www.arxiv.org/pdf/2512.07454"},{"title":"(PDF) Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://www.researchgate.net/publication/397087634_Revisiting_Multilingual_Data_Mixtures_in_Language_Model_Pretraining"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"}]

Based on the search results, here's what I found about curriculum learning, cross-lingual transfer, and instruction tuning in 2025:

## Key Research Areas

Instruction tuning with human curriculum is an active area of research, and several 2025 papers combine curriculum learning approaches with cross-lingual transfer.

### Curriculum Learning Strategies for Cross-Lingual Transfer

Advanced frameworks like CCL-XCoT apply curriculum-based contrastive learning on large parallel corpora, aligning semantic spaces before task- or instruction-tuning. One approach demonstrates how a monolingual English model can be effectively adapted to Persian through a novel, resource-efficient curriculum learning pipeline that employs a "warm-up" stage using bilingual narratives to align embeddings prior to heavy training, followed by continual pretraining and instruction tuning via Parameter-Efficient Fine-Tuning.

### Cross-Lingual Instruction Tuning Methods

Cross-lingual in-context few-shot learning (xICL) accelerates multilingual agreement in instruction tuning where some fragments of source languages in examples are randomly substituted by their target language translations, with a randomly online CoT strategy to enhance the multilingual reasoning ability, and cross-lingual distillation to facilitate language transfer.

### Multilingual Data Mixture and Curriculum Learning

Controlled curriculum learning experiments investigate how the timing and order of language inclusion during training influence model dynamics of cross-lingual competition and knowledge transfer. However, recent findings show that curriculum learning fails to mitigate negative interference in some multilingual settings.

### Pivot Languages in Cross-Lingual Transfer

Using English as a pivot for cross-lingual instruction tuning, by first interpreting instructions in English before generating responses in the target language, can be highly effective.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90a35b0d-53c8-47d9-933b-58d9f982f6f1",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "54949f8e-006e-4e52-828e-b212a12c32e9",
  "sourceToolAssistantUUID": "90a35b0d-53c8-47d9-933b-58d9f982f6f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T07:25:43.867Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AXnNu5QyciSn7a47XeytvZ`</summary>

```json
{
  "query": "openreview.net EMNLP 2026 cross-lingual instruction tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54949f8e-006e-4e52-828e-b212a12c32e9",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVNpsPEh2pQYkXTs9Jt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8211045-dbc1-4a66-b02e-1bd9f900e7cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012oWEWZa7Y4kiuWmoJLYaid",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9153,
      "output_tokens": 659,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1906
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 659,
          "cache_read_input_tokens": 9153,
          "cache_creation_input_tokens": 1906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1906,
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

_source line 20 · 2026-05-10T07:25:45.008Z_

<details><summary>↩ Tool result · `toolu_01Hd9Q92399y3FDjvSRj8GeJ`</summary>

```text
Web search results for query: "data selection multilingual fine-tuning typological distance 2025"

Links: [{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090v2"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"How Multilingual Are Large Language Models Fine-Tuned for Translation?","url":"https://arxiv.org/html/2405.20512v1"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809"},{"title":"Zero-shot Cross-lingual Transfer Learning with Multiple Source and Target Languages for Information Extraction: Language Selection and Adversarial Training","url":"https://arxiv.org/html/2411.08785"},{"title":"Improving Translation Quality by Selecting Better Data for ...","url":"https://arxiv.org/pdf/2512.11388"},{"title":"Choosing Transfer Languages for Cross-Lingual Learning | Request PDF","url":"https://www.researchgate.net/publication/335779022_Choosing_Transfer_Languages_for_Cross-Lingual_Learning"},{"title":"A Rethinking on Data Selection for Fine-Tuning Large ...","url":"https://aclanthology.org/2025.naacl-long.336.pdf"},{"title":"A survey of multilingual large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666389924002903"},{"title":"A Primer on Pretrained Multilingual Language Models | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3727339"}]

Here are the search results for "data selection multilingual fine-tuning typological distance 2025":

## Key Findings

The search returned several recent research papers addressing data selection, multilingual fine-tuning, and the role of typological distance:

**Language Diversity in Fine-Tuning:**
Recent systematic investigations across 132 translation directions have resolved conflicting findings on language diversity in LLM fine-tuning. As diversity increases, single-target clusters show greater specialization while multi-language clusters exhibit enhanced representational overlap, suggesting improved cross-lingual transfer.

**Typological Distance and Language Selection:**
When selecting a set of fine-tuning languages, more typological diversity might support better generalization to new languages. Strategic selection of languages based on typology, geographical features, and language family features might provide benefits for cross-lingual transfer, depending on the model and task.

**Multilingual Data Composition:**
English benefits from cross-lingual transfer with high-resource, typologically related languages, which receive more data under natural distribution. Distances based on linguistic features, including phylogenetic and typological properties, between two languages are correlated with cross-lingual transfer capacity.

**Data Selection Strategies:**
Different data selection strategies affect the fine-tuning quality of large language models for translation, with semantic-based selectors like COMET-Kiwi consistently outperforming lexical or geometry-based heuristics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "894748dc-46cc-4094-b647-82103883e2c6",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "01d684e0-1491-4202-b195-68b2772e7595",
  "sourceToolAssistantUUID": "894748dc-46cc-4094-b647-82103883e2c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T07:25:45.678Z_

<details><summary>↩ Tool result · `toolu_015xT49R2Ta6HuybMaCSwEc7`</summary>

```text
Web search results for query: "staged training multilingual language model 2025 2026 instruction tuning"

Links: [{"title":"Exploring Two-Phase Continual Instruction Fine-tuning for Multilingual Adaptation in Large Language Models","url":"https://arxiv.org/html/2410.16006v3"},{"title":"Instruction Tuning for Large Language Models: A Survey","url":"https://dl.acm.org/doi/pdf/10.1145/3777411"},{"title":"Large language model based machine translation for universal multilingual understanding and translation quality enhancement | Discover Computing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10791-026-10027-x"},{"title":"GitHub - Wang-ML-Lab/llm-continual-learning-survey: [CSUR 2025] Continual Learning of Large Language Models: A Comprehensive Survey · GitHub","url":"https://github.com/Wang-ML-Lab/llm-continual-learning-survey"},{"title":"Fine‑tuning large language models (LLMs) in 2026 | by Kumar Nishant | Medium","url":"https://medium.com/@knish5790/fine-tuning-large-language-models-llms-in-2025-623567db84e9"},{"title":"STEP: Staged Parameter-Efficient Pre-training for Large Language Models","url":"https://arxiv.org/html/2504.04151v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=two-stage+training"},{"title":"Fine-tuning large language models (LLMs) in 2026 | SuperAnnotate","url":"https://www.superannotate.com/blog/llm-fine-tuning"},{"title":"[2504.04151] STEP: Staged Parameter-Efficient Pre-training for Large Language Models","url":"https://arxiv.org/abs/2504.04151"},{"title":"ICML Poster Parrot: Multilingual Visual Instruction Tuning","url":"https://icml.cc/virtual/2025/poster/44886"}]

I've completed the web search for "staged training multilingual language model 2025 2026 instruction tuning". Here are the key findings:

## Main Research Areas

**Staged/Two-Phase Training Approaches:**

A common fine-tuning strategy is to train LLMs on an instruction-following dataset that contains a mixture of languages. A two-stage training paradigm injects general medical knowledge in the first stage using MMed-IFT, while the second stage fine-tunes task-specific multiple-choice questions with MMed-IFT-MC.

**Staged Parameter-Efficient Pre-training (STEP):**

STEP integrates parameter-efficient tuning techniques with model growth. Models can be trained using STEP with multiple stages (STEP-2stages, STEP-3stages).

**Multilingual Challenges:**

While instruction-following datasets contain a mixture of languages, these datasets are often heavily skewed toward English and other high-resource languages, leading to a performance imbalance. Fine-tuning on a dataset containing only non-English languages can hurt the model's performance on English due to catastrophic forgetting.

**Recent Advances (2025-2026):**

A comprehensive survey on instruction tuning for large language models was published in January 2026. Fine-tuning can be done in stages so that translation models do not become obsolete, involving regular retraining with newly acquired corpora and incorporation of human editor feedback.

The research shows active work on balancing multilingual performance through staged training approaches and addressing catastrophic forgetting in instruction tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7f534e5-dd0c-4bdd-9f83-b3b0dd18f3a2",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "cf306f1c-2b9f-4ad1-b7f5-581a8b580d11",
  "sourceToolAssistantUUID": "d7f534e5-dd0c-4bdd-9f83-b3b0dd18f3a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T07:25:46.045Z_

<details><summary>↩ Tool result · `toolu_01Y76xK2H7vyNZLKHuWUSkLR`</summary>

```text
Web search results for query: "Mongolian language model instruction tuning LLM 2025 2026"

Links: [{"title":"MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs","url":"https://arxiv.org/html/2411.09492v1"},{"title":"Dorjzodovsuren/Mongolian_Llama3-v0.1 · Hugging Face","url":"https://huggingface.co/Dorjzodovsuren/Mongolian_Llama3-v0.1"},{"title":"Pre-training Language Model for Mongolian with Agglutinative Linguistic Knowledge Injection | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10650812/"},{"title":"Evaluating Large Language Models in Mongolian","url":"https://www.anlp.jp/proceedings/annual_meeting/2025/pdf_dir/Q1-12.pdf"},{"title":"How Large Language Models Enhance Low-Resource Mongolian-Chinese Machine Translation?","url":"https://www.sciengine.com/DI/doi/10.3724/2096-7004.di.2025.0116"},{"title":"Fine-tuning large language models (LLMs) in 2026 | SuperAnnotate","url":"https://www.superannotate.com/blog/llm-fine-tuning"},{"title":"Fine‑tuning large language models (LLMs) in 2026 | by Kumar Nishant | Medium","url":"https://medium.com/@knish5790/fine-tuning-large-language-models-llms-in-2025-623567db84e9"},{"title":"GitHub - tugstugi/mongolian-nlp: Useful resources for Mongolian NLP · GitHub","url":"https://github.com/tugstugi/mongolian-nlp"},{"title":"Egune AI, the LLM that specializes in Mongolia’s language, culture, and nomadic traditions - Rest of World","url":"https://restofworld.org/2025/mongolia-egune-ai-llm/"},{"title":"[2411.09492] MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs","url":"https://arxiv.org/abs/2411.09492"}]

Based on the search results, I found several relevant developments regarding Mongolian language models and instruction tuning:

## Recent Mongolian LLM Developments (2025-2026)

**Instruction-Tuned Models:**

Mongolian-Llama3 is the first open source instruction-tuned language model for Mongolian & English users with various abilities such as roleplaying & tool-using built upon the quantized Meta-Llama-3-8B model.

**Evaluation Benchmarks:**

MM-Eval comprises 569 syntax, 677 semantics, 344 knowledge, and 250 reasoning tasks to advance NLP and LLMs in low-resource languages like Mongolian. This benchmark was released in November 2024 and testing on models including Qwen2-7B-Instruct, GLM4-9b-chat, Llama3.1-8B-Instruct, GPT-4, and DeepseekV2.5 revealed that all models performed better on syntactic tasks than semantic tasks, highlighting a gap in deeper language understanding.

**Egune AI Initiative:**

Egune AI is part of a growing movement to build LLMs in low-resource languages to expand AI access for underserved populations. The latest Egune model has 70 billion parameters and improved coding and reasoning capability.

**Technical Approaches:**

A novel pre-training language model for Mongolian incorporates a three-stage agglutinative knowledge injection strategy. Additionally, LLM-CPTSymFT involves continual pre-training (CPT) of the base model using Mongolian and Chinese corpora, followed by symmetrical fine-tuning (SymFT), which leverages a mix of original Mongolian-Chinese parallel data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a83bb0f-d8d1-4e5f-bf57-2b1319a00538",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "38568306-709d-4abc-8537-5817b7212c32",
  "sourceToolAssistantUUID": "3a83bb0f-d8d1-4e5f-bf57-2b1319a00538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T07:25:46.365Z_

<details><summary>↩ Tool result · `toolu_01EPJEALQVNJ3NMDENBkPqxi`</summary>

```text
Web search results for query: "KazMMLU arXiv 2502.12829"

Links: [{"title":"[2502.12829] KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan","url":"https://arxiv.org/abs/2502.12829"},{"title":"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan","url":"https://arxiv.org/html/2502.12829"},{"title":"KazMMLU: Evaluating Language Models on Kazakh, Russian,","url":"https://arxiv.org/pdf/2502.12829v1"},{"title":"(PDF) KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan","url":"https://www.researchgate.net/publication/389130089_KazMMLU_Evaluating_Language_Models_on_Kazakh_Russian_and_Regional_Knowledge_of_Kazakhstan"},{"title":"KazMMLU: Evaluating Language Models on Kazakh, ...","url":"https://arxiv.org/pdf/2502.12829"},{"title":"Algebro-combinatorial generalizations of the Victoir method for constructing weighted designs","url":"https://arxiv.org/html/2505.12829"},{"title":"[2505.12829] Algebro-combinatorial generalizations of the Victoir method for constructing weighted designs","url":"https://arxiv.org/abs/2505.12829"},{"title":"[2512.12829] Towards a Systematic Taxonomy of Attacks against Space Infrastructures","url":"https://arxiv.org/abs/2512.12829"},{"title":"Towards a Systematic Taxonomy of Attacks against Space Infrastructures","url":"https://arxiv.org/html/2512.12829"},{"title":"[2510.12829] Mathematics with large language models as provers and verifiers","url":"https://arxiv.org/abs/2510.12829"}]

Based on the search results, here's what I found about KazMMLU (arXiv 2502.12829):

KazMMLU is the first MMLU-style dataset specifically designed for Kazakh language. KazMMLU comprises 23,000 questions that cover various educational levels, including STEM, humanities, and social sciences, sourced from authentic educational materials and manually validated by native speakers and educators.

The dataset includes 10,969 Kazakh questions and 12,031 Russian questions, reflecting Kazakhstan's bilingual education system and rich local context. KazMMLU is sourced from authentic educational materials, including national exams, textbooks, and professional certification repositories.

The evaluation of several state-of-the-art multilingual models (Llama3.1, Qwen-2.5, GPT-4, and DeepSeek V3) demonstrates substantial room for improvement. The paper was authored by Mukhammed Togmanov and 13 other researchers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d78d1d3c-43bc-4efa-b441-0bab45d3b3b2",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "ad4d0509-f87a-4bc7-99e8-d0a022ee6236",
  "sourceToolAssistantUUID": "d78d1d3c-43bc-4efa-b441-0bab45d3b3b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T07:25:47.826Z_

<details><summary>↩ Tool result · `toolu_01Jnn9JZAfdybzxCjca6pboM`</summary>

```text
Web search results for query: "TUMLU arXiv 2502.11020"

Links: [{"title":"[2502.11020] TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages","url":"https://arxiv.org/abs/2502.11020"},{"title":"[2502.11020v1] TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages","url":"https://arxiv.org/abs/2502.11020v1"},{"title":"TUMLU: A Unified and Native Language Understanding Benchmark for","url":"https://arxiv.org/pdf/2502.11020v1"},{"title":"TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages","url":"https://arxiv.org/html/2502.11020"},{"title":"arXiv:2502.11020v2 [cs.CL] 13 Jun 2025","url":"https://arxiv.org/pdf/2502.11020"},{"title":"TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250211020I/abstract"},{"title":"Paper page - TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages","url":"https://huggingface.co/papers/2502.11020"},{"title":"GitHub - ceferisbarov/TUMLU: TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages · GitHub","url":"https://github.com/ceferisbarov/TUMLU"},{"title":"Search | arXiv e-print repository","url":"https://arxiv.org/search/cs?searchtype=author&query=K%C3%B6ksal,+A"},{"title":"[2602.11020] When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging","url":"https://arxiv.org/abs/2602.11020"}]

Based on the search results, here's information about TUMLU arXiv 2502.11020:

## Overview

TUMLU is a comprehensive, multilingual, and natively developed language understanding benchmark specifically designed for Turkic languages.

## Dataset Contents

The benchmark consists of middle- and high-school level questions spanning 11 academic subjects in Azerbaijani, Crimean Tatar, Karakalpak, Kazakh, Kyrgyz, Tatar, Turkish, Uyghur, and Uzbek. The dataset contains 38,139 questions across 8 languages and 11 subjects.

It is the first such benchmark to include Uyghur, Karakalpak, Tatar, or Crimean Tatar, and also a significant improvement over existing benchmarks for Azerbaijani, Kazakh, Kyrgyz, and Uzbek.

## Key Innovation

The paper addresses the lack of native language MMLU benchmark especially in the under-represented Turkic language family with distinct morphosyntactic and cultural characteristics. Unlike previous efforts, these benchmarks are not built using machine translation from high-resource languages, which may introduce errors and fail to account for linguistic and cultural intricacies of target languages.

## Evaluation and Release

The authors systematically evaluate a diverse range of open and proprietary multilingual large language models (LLMs), including Claude, Gemini, GPT, and LLaMA. They also present TUMLU-mini, a more concise, balanced, and manually verified subset of the dataset, which they release along with all corresponding evaluation scripts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3624b8a3-5daf-4e38-af91-fab1493981d1",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "6e4b3cd1-2a52-4728-bc1a-0859ba9f81dc",
  "sourceToolAssistantUUID": "3624b8a3-5daf-4e38-af91-fab1493981d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T07:25:47.917Z_

<details><summary>↩ Tool result · `toolu_01RPBth4Cm1h3svWzm9gqEnu`</summary>

```text
Web search results for query: "Uyghur language model NLP instruction tuning 2025"

Links: [{"title":"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.559/"},{"title":"Advancing Language Understanding: A Review of Challenges and Solutions in Training Large Language Models for Low-Resource Languages - NHSJS","url":"https://nhsjs.com/2025/advancing-language-understanding-a-review-of-challenges-and-solutions-in-training-large-language-models-for-low-resource-languages/"},{"title":"Low-Resource Language Expansion and Translation ...","url":"https://aclanthology.org/2025.coling-main.559.pdf"},{"title":"CUTE: A Multilingual Dataset for Enhancing Cross-Lingual ...","url":"https://aclanthology.org/2025.coling-main.670.pdf"},{"title":"Optimizing Uyghur Speech Synthesis by Combining Pretrained Cross-Lingual Model | ACM Transactions on Asian and Low-Resource Language Information Processing","url":"https://dl.acm.org/doi/10.1145/3675397"},{"title":"Do Chinese models speak Chinese languages?","url":"https://arxiv.org/html/2504.00289v1"},{"title":"Research on morphological knowledge-guided low-resource agglutinative languages-Chinese translation | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-01780-5"},{"title":"Evaluating Uighur literary translation: A comparative study of ChatGPT, Google Translate, and Bing Translator | PLOS One","url":"https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335261"},{"title":"Exploring NLP Benchmarks in an Extremely Low-Resource Setting","url":"https://arxiv.org/html/2509.03962v1"},{"title":"Advancing Language Models through Instruction Tuning: Recent Progress and Challenges","url":"https://instruction-tuning-tutorial-2025.github.io/"}]

I've found several relevant research papers and articles on Uyghur language models and NLP instruction tuning from 2025. Here's a summary of the key findings:

## Recent Uyghur Language Model Research (2025)

A major 2025 study involves a four-stage process for low-resource language expansion: collecting and pre-processing monolingual data, continuous pre-training with extensive monolingual data, fine-tuning with parallel corpora using translation supervision, and proposing direct preference optimization based on translation self-evolution (DPOSE), which effectively expands low-resource languages supported by large language models and enhances translation ability in Uyghur.

Uyghur, a Turkic language spoken by over 13 million people, faces significant challenges as a low-resource language including limited digital resources, sparse annotated corpora, and geopolitical constraints that hinder open data collection.

## Instruction Tuning Approaches

Recent efforts to address Uyghur language challenges involve a four-stage strategy: extensive monolingual data collection, continual pre-training on a Chinese-optimized LLaMA2 model, translation-specific instruction fine-tuning, and Direct Preference Optimization based on translation self-evolution (DPOSE).

## Multilingual Dataset Development

A multilingual dataset (CUTE) includes 47,905 Uyghur samples and involves fine-tuning models for Chinese, Uyghur, and Tibetan languages.

## Model Performance Observations

Language identification experiments on Chinese minority languages reveal that most models cannot identify Uyghur, though Llama3-Instruct is uniquely good at Uyghur identification and is also top-performing in Tibetan and Mongolian.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1c0164b-4417-4f3b-b9e9-31a68fea4e4c",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "ed8440d5-e79e-48e4-ae18-69f6a4e4b50f",
  "sourceToolAssistantUUID": "f1c0164b-4417-4f3b-b9e9-31a68fea4e4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T07:25:49.214Z_

<details><summary>↩ Tool result · `toolu_0157tH81DyGJUg534TSR71ha`</summary>

```text
Web search results for query: "Central Asian languages LLM instruction tuning Kazakh 2025 2026"

Links: [{"title":"Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://arxiv.org/html/2503.01493v1"},{"title":"Fine-Tuning Large Language Models for Kazakh Text Simplification | MDPI","url":"https://www.mdpi.com/2076-3417/15/15/8344"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting","url":"https://arxiv.org/html/2503.01493"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting | OpenReview","url":"https://openreview.net/forum?id=wRcTCcb0H5"},{"title":"The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization","url":"https://www.mdpi.com/2504-2289/9/5/137"},{"title":"[2502.13647] Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh","url":"https://arxiv.org/abs/2502.13647"},{"title":"AI in Central Asia: Kazakhstan Unveils Multilingual GPT Model - The Times Of Central Asia","url":"https://timesca.com/ai-in-central-asia-kazakhstan-unveils-multilingual-gpt-model/"},{"title":"Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.706/"},{"title":"Case Study: What We Can Learn from ISSAI KAZ-LLM and the AI Potential for Low Resource Languages | by Dion Wiggins | Medium","url":"https://medium.com/@dion.wiggins/case-study-what-we-can-learn-from-issai-kaz-llm-and-the-ai-potential-for-low-resource-languages-6606fd5bc594"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh ...","url":"https://arxiv.org/pdf/2503.01493"}]

Based on the web search results, here's what I found about Central Asian languages, LLM instruction tuning, and Kazakh developments in 2025-2026:

## Recent Kazakh LLM Developments

Llama-3.1-Sherkala-8B-Chat is a state-of-the-art instruction-tuned LLM designed for Kazakh, trained on 45.3B tokens across Kazakh, English, Russian, and Turkish. A total of 3.5 million instruction examples in Kazakh were curated for instruction fine-tuning, combining translated English datasets and in-house datasets from cultural wiki sources and public governmental data.

## Instruction Tuning for Government and Cultural Data

A large-scale (10,600 samples) instruction-following dataset covering key institutional and cultural knowledge relevant to Kazakhstan was introduced, which enhances LLMs' understanding of procedural, legal, and structural governance topics. Fine-tuning Qwen, Falcon, and Gemma on this dataset leads to consistent performance improvements in both multiple-choice and generative tasks, demonstrating the potential of LLM-assisted instruction tuning for low-resource languages.

## Other Recent Models

KazSim is an instruction-tuned model built on multilingual large language models for Kazakh text simplification, addressing a morphologically rich, low-resource language. Additionally, a 1.94B parameter LLaMA-based model was developed that demonstrates how strong, culturally aligned performance can be achieved without massive infrastructure.

ISSAI KAZ-LLM, introduced by researchers at Nazarbayev University's Institute of Intelligent Systems and Artificial Intelligence, is tailored to Kazakhstan's multilingual environment, supporting Kazakh, Russian, and English, with additional functionality for Turkish.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fb99beb-a34b-4795-b92a-fa8953c79211",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "baafa0b5-d5e6-4370-a21c-162b8a75b929",
  "sourceToolAssistantUUID": "2fb99beb-a34b-4795-b92a-fa8953c79211",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T07:25:49.318Z_

<details><summary>↩ Tool result · `toolu_01LAGptrrdF3W4zoYYxQ1ipk`</summary>

```text
Web search results for query: "MiLiC-Eval arXiv 2503.01150 Uyghur Mongolian Kazakh Tibetan"

Links: [{"title":"MiLiC-Eval: Benchmarking Multilingual LLMs for China’s Minority Languages","url":"https://arxiv.org/html/2503.01150v1"},{"title":"[2503.01150] MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages","url":"https://arxiv.org/abs/2503.01150"},{"title":"GitHub - luciusssss/MiLiC-Eval: [ACL'25 Findings] MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages","url":"https://github.com/luciusssss/MiLiC-Eval"},{"title":"pkupie/milic-eval · Datasets at Hugging Face","url":"https://huggingface.co/datasets/pkupie/milic-eval"},{"title":"GitHub - luciusssss/mc2_corpus: [ACL'24] MC^2: A Multilingual Corpus of Minority Languages in China (Tibetan, Uyghur, Kazakh, and Mongolian)","url":"https://github.com/luciusssss/mc2_corpus"},{"title":"MiLiC-Eval: Benchmarking Multilingual LLMs for China's ...","url":"https://aclanthology.org/2025.findings-acl.578.pdf"},{"title":"MC2: Towards Transparent and Culturally-Aware NLP for ...","url":"https://aclanthology.org/2024.acl-long.479.pdf"},{"title":"Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages","url":"https://arxiv.org/html/2502.10852"},{"title":"MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs","url":"https://arxiv.org/html/2411.09492v1"},{"title":"TiBERT: Tibetan Pre-trained Language Model*","url":"https://arxiv.org/pdf/2205.07303"}]

Based on the search results, I found comprehensive information about MiLiC-Eval (arXiv 2503.01150):

## MiLiC-Eval Overview

MiLiC-Eval is a comprehensive framework with 24K instances across 9 tasks, focusing on 4 Minority Languages in China. These languages are Tibetan (bo), Uyghur (ug), Kazakh (kk, in the Kazakh Arabic script), and Mongolian (mn, in the traditional Mongolian script).

## Key Findings

Current LLMs exhibit a decent understanding of Uyghur, and a preliminary understanding of Tibetan and Kazakh, but struggle with comprehending Mongolian. Even the best-performing model, GPT-4o-mini, only achieves performance slightly better than random on several Mongolian tasks.

## Focus and Design

MiLiC-Eval focuses on underrepresented writing systems, and its parallelism between tasks and languages can provide a faithful and fine-grained assessment of linguistic and problem-solving skills.

## Writing System Challenges

The average token count for English (27 tokens) and Chinese (31 tokens) is much lower compared to the four minority languages, particularly Tibetan and traditional Mongolian, which require 70-430 tokens per sentence. Code-switching errors when generating content in minority languages is especially prevalent in Kazakh and Mongolian, both of which employ less commonly used writing systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fd85472-a633-4e31-8f1c-9f755e808526",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "27fe6167-883e-4ef4-a880-5220d9f071e8",
  "sourceToolAssistantUUID": "8fd85472-a633-4e31-8f1c-9f755e808526",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T07:25:50.012Z_

<details><summary>↩ Tool result · `toolu_01AXnNu5QyciSn7a47XeytvZ`</summary>

```text
Web search results for query: "openreview.net EMNLP 2026 cross-lingual instruction tuning"

Links: [{"title":"Translation and Fusion Improves Zero-shot Cross-lingual Information Extraction | OpenReview","url":"https://openreview.net/forum?id=qrTrnrEi9d"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"EMNLP 2026 Tutorials | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FTutorials"},{"title":"From English to Second Language Mastery: Enhancing LLMs with Cross-Lingual Continued Instruction Tuning | OpenReview","url":"https://openreview.net/forum?id=dqxXAgFjra"},{"title":"EMNLP | OpenReview","url":"https://openreview.net/group?id=EMNLP"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly | OpenReview","url":"https://openreview.net/forum?id=N9nfDhXiEbYy"},{"title":"EMNLP 2026 Workshop | OpenReview","url":"https://openreview.net/group?id=EMNLP/2026/Workshop"},{"title":"MULTILINGUAL FEDERATED PROMPT TUNING","url":"https://openreview.net/pdf?id=zzqn5G9fjn"},{"title":"EMNLP 2026 Workshop GroundLM | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FGroundLM"}]

Based on the web search results, I found several relevant papers on OpenReview related to cross-lingual instruction tuning:

1. **"Translation and Fusion Improves Zero-shot Cross-lingual Information Extraction"** - This paper introduces GoLLIE-TF, a cross-lingual instruction-tuned LLM for IE tasks, designed to close the performance gap between high and low-resource languages.

2. **"From English to Second Language Mastery: Enhancing LLMs with Cross-Lingual Continued Instruction Tuning"** - This work introduces Cross-Lingual Continued Instruction Tuning (X-CIT), which fully leverages translation-based parallel instruction data to enhance cross-lingual adaptability, emulating the human process of second language acquisition guided by Chomsky's Principles and Parameters Theory.

3. **"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly"** - This paper proposes CLiKA, a systematic framework to assess the cross-lingual knowledge alignment of LLMs, and shows that while both multilingual pretraining and instruction tuning are beneficial for cross-lingual knowledge alignment, the training strategy needs to be carefully designed.

These papers appear on OpenReview and address cross-lingual instruction tuning topics relevant to EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8211045-dbc1-4a66-b02e-1bd9f900e7cf",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "6b04e159-bb32-4954-8d01-3b423a0c94de",
  "sourceToolAssistantUUID": "c8211045-dbc1-4a66-b02e-1bd9f900e7cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T07:25:50.557Z_

<details><summary>↩ Tool result · `toolu_01FuP1EiBDFvGCUwSSd8w8U9`</summary>

```text
Web search results for query: "Implicit Cross-Lingual Rewarding arXiv 2503.04647 DPO ACL 2025"

Links: [{"title":"[2503.04647] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://arxiv.org/abs/2503.04647"},{"title":"GitHub - ZNLP/Implicit-Cross-Lingual-Rewarding: [ACL 2025 Findings] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://github.com/ZNLP/Implicit-Cross-Lingual-Rewarding"},{"title":"arXiv:2503.04647v2 [cs.CL] 5 Jun 2025 Implicit Cross-Lingual Rewarding","url":"https://nlpr.ia.ac.cn/cip/ZongPublications/2025/2025-YangWen-FindingsACL.pdf"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | Request PDF","url":"https://www.researchgate.net/publication/389649128_Implicit_Cross-Lingual_Rewarding_for_Efficient_Multilingual_Preference_Alignment"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1088/"},{"title":"[Literature Review] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://www.themoonlight.io/en/review/implicit-cross-lingual-rewarding-for-efficient-multilingual-preference-alignment"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/implicit-cross-lingual-rewarding-efficient-multilingual-preference"},{"title":"Multilingual Preference Alignment via Cross-Lingual Rewarding: A Novel Approach to Language Model Training – The Science Archive","url":"https://thesciencearchive.org/2503-04647v1/"},{"title":"(PDF) CAPO: Confidence Aware Preference Optimization Learning for Multilingual Preferences","url":"https://www.researchgate.net/publication/397521711_CAPO_Confidence_Aware_Preference_Optimization_Learning_for_Multilingual_Preferences"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"}]

Based on the search results, here's what I found about this paper:

## Overview

This is an arXiv paper (2503.04647) titled "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment", and it was published in the Findings of the Association for Computational Linguistics: ACL 2025 in Vienna, Austria.

## Main Contribution

The paper proposes an approach that captures learned preferences from well-aligned English models by implicit rewards and transfers them to other languages through iterative training. Specifically, they derive an implicit reward model from the logits of an English DPO-aligned model and its corresponding reference model.

This reward model is leveraged to annotate preference relations in cross-lingual instruction-following pairs, using English instructions to evaluate multilingual responses. The annotated data is subsequently used for multilingual DPO fine-tuning, facilitating preference knowledge transfer from English to other languages.

## Results

Fine-tuning Llama3 for two iterations resulted in a 12.72% average improvement in Win Rate and a 5.97% increase in Length Control Win Rate across all training languages on the X-AlpacaEval leaderboard.

## Motivation

While DPO has enabled significant progress in aligning English LLMs, multilingual preference alignment is hampered by data scarcity.

The authors are Wen Yang, Junhong Wu, Chen Wang, Chengqing Zong, and Jiajun Zhang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc41d552-3f95-4e1d-ad98-78290acf9abb",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "7193fab7-9f50-41a0-b24d-ff7c958ccc71",
  "sourceToolAssistantUUID": "bc41d552-3f95-4e1d-ad98-78290acf9abb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T07:25:52.303Z_

<details><summary>↩ Tool result · `toolu_014tzc3A8ULZjtqcSjonQXJq`</summary>

```text
Web search results for query: "source language selection instruction tuning cross-lingual 2025 2026"

Links: [{"title":"XCOT: Cross-lingual Instruction Tuning for Cross-lingual","url":"https://ojs.aaai.org/index.php/AAAI/article/download/34524/36679"},{"title":"Published in Transactions on Machine Learning Research (11/2025)","url":"https://openreview.net/pdf?id=oapsbIO1Bd"},{"title":"[2604.11096] Efficient Training for Cross-lingual Speech Language Models","url":"https://arxiv.org/abs/2604.11096"},{"title":"[2510.07074] LuxInstruct: A Cross-Lingual Instruction Tuning Dataset For Luxembourgish","url":"https://arxiv.org/abs/2510.07074"},{"title":"X-Instruction: Aligning Language Model in Low-resource Languages with Self-curated Cross-lingual Instructions | OpenReview","url":"https://openreview.net/forum?id=m83Vcel5Sez"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment - ACL Anthology","url":"https://aclanthology.org/2025.sumeval-2.2/"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809"},{"title":"[PDF] Aya Dataset: An Open-Access Collection for Multilingual Instruction Tuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Aya-Dataset:-An-Open-Access-Collection-for-Tuning-Singh-Vargus/88cd6e0f7c2f1fe2bd4796a6729447d60bfeffc9"},{"title":"[2404.11932] CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment","url":"https://arxiv.org/abs/2404.11932"}]

I found several relevant research papers and studies on source language selection, instruction tuning, and cross-lingual approaches from 2025-2026. Here's a summary of the key findings:

## Recent Research on Cross-Lingual Instruction Tuning (2025-2026)

### Language Selection Approaches

Studies have investigated various language selection techniques including typological feature vectors and language embeddings derived from semantic typology features, with k-means clustering algorithms used to select a fixed number of languages. Cross-lingual generalization capabilities vary significantly across different language subsets, indicating that linguistically informed selections can aid in better generalization to unseen languages.

### Selective Sampling Strategies

Recent work addresses adapting pre-trained multilingual language models to specific target languages by selectively sampling auxiliary language data that aligns with the target language's distribution gaps.

### CrossIn Approach

A novel approach called CrossIn utilizes a mixed composition of cross-lingual instruction tuning data, leveraging the compressed representation shared by various languages to efficiently enhance the model's task-solving capabilities and multilingual proficiency. Experimental results demonstrate substantial performance improvements across tasks and languages, with insights into the impact of cross-lingual data volume and translation data integration.

### XCOT Method

The XCOT (Cross-lingual Instruction Tuning) approach uses cross-lingual in-context few-shot learning with mixed language tokens in queries during multilingual instruction tuning, employing a randomly online Chain-of-Thought strategy to promote multilingual reasoning ability.

### Low-Resource Language Support

Cross-lingual instruction tuning improves both representational alignment across languages and the model's generative capabilities, with cross-lingual data curation avoiding the pitfalls of machine-translated data and directly benefiting low-resource language development.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18554f64-458a-4a49-a24f-e319c49794d7",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "1b031808-e813-4f9b-813f-a453f8cc89a1",
  "sourceToolAssistantUUID": "18554f64-458a-4a49-a24f-e319c49794d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T07:25:55.795Z_

Good initial results. Now let me fetch the actual arxiv pages for the specific papers that need verification, and dig deeper into the most relevant competing papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b031808-e813-4f9b-813f-a453f8cc89a1",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVQJdm3iPTFCgYnrUz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99257b7a-0d45-4599-a960-b7488d5d5ef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vfn3NgLqsm6Vx5XsWAdU4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7601,
      "cache_creation_input_tokens": 4444,
      "cache_read_input_tokens": 11059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4444,
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

_source line 32 · 2026-05-10T07:25:57.287Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LGeZK5jfm7Q7oeZyNCtjZW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.12829",
  "prompt": "Extract the full title, authors, abstract, venue/conference information, and submission/publication dates for this paper. Is it confirmed as ACL 2025?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99257b7a-0d45-4599-a960-b7488d5d5ef3",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVQJdm3iPTFCgYnrUz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37ca3d94-1f05-4309-b214-4b8d87c50de7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vfn3NgLqsm6Vx5XsWAdU4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7601,
      "cache_creation_input_tokens": 4444,
      "cache_read_input_tokens": 11059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4444,
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

_source line 33 · 2026-05-10T07:25:58.505Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019yXyJEQoSqwSBXBT3yxAxA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.11020",
  "prompt": "Extract the full title, authors, abstract, venue/conference information, and submission/publication dates. Is it confirmed as ACL 2025? Does it cover Uyghur, Kazakh, Mongolian?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37ca3d94-1f05-4309-b214-4b8d87c50de7",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVQJdm3iPTFCgYnrUz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a416d1a6-9621-46e1-addd-121ad14a2b87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vfn3NgLqsm6Vx5XsWAdU4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7601,
      "cache_creation_input_tokens": 4444,
      "cache_read_input_tokens": 11059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4444,
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

_source line 34 · 2026-05-10T07:25:59.724Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xrfcmm7xstuJ5YM7D42PBB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.01150",
  "prompt": "Extract the full title, authors, abstract, venue/conference information. Is it ACL 2025 Findings? What languages does it cover? What are the main evaluation results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a416d1a6-9621-46e1-addd-121ad14a2b87",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVQJdm3iPTFCgYnrUz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99f7851a-0495-430b-8e28-1855ddca9c13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vfn3NgLqsm6Vx5XsWAdU4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7601,
      "cache_creation_input_tokens": 4444,
      "cache_read_input_tokens": 11059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4444,
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

_source line 35 · 2026-05-10T07:26:01.093Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M26LjpkLroX9F2ZGEMNs8u`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.04647",
  "prompt": "Extract the full title, authors, abstract, venue/conference information. Is it ACL 2025 Findings? What is the main method and results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99f7851a-0495-430b-8e28-1855ddca9c13",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVQJdm3iPTFCgYnrUz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01a9e1e3-1333-4057-bc91-410a2b825ddc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vfn3NgLqsm6Vx5XsWAdU4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7601,
      "cache_creation_input_tokens": 4444,
      "cache_read_input_tokens": 11059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4444,
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

_source line 36 · 2026-05-10T07:26:02.006Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HT5a2z9VzBpBmMDFbJm4Ts`</summary>

```json
{
  "query": "language-weighted data sampling cross-lingual transfer multi-pivot instruction tuning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01a9e1e3-1333-4057-bc91-410a2b825ddc",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVQJdm3iPTFCgYnrUz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25dda32e-b468-4df8-9e0b-9a86a989b6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vfn3NgLqsm6Vx5XsWAdU4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7601,
      "cache_creation_input_tokens": 4444,
      "cache_read_input_tokens": 11059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4444,
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

_source line 37 · 2026-05-10T07:26:02.678Z_

<details><summary>↩ Tool result · `toolu_01LGeZK5jfm7Q7oeZyNCtjZW`</summary>

```text
# Paper Information Extraction

**Full Title:**
"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan"

**Authors:**
Mukhammed Togmanov, Nurdaulet Mukhituly, Diana Turmakhan, Jonibek Mansurov, Maiya Goloburda, Akhmed Sakip, Zhuohan Xie, Yuxia Wang, Bekassyl Syzdykov, Nurkhan Laiyk, Alham Fikri Aji, Ekaterina Kochmar, Preslav Nakov, Fajri Koto

**Abstract Summary:**
The paper introduces "the first MMLU-style dataset specifically designed for Kazakh language" containing 23,000 questions across educational levels. It evaluates multilingual models and shows substantial performance gaps in Kazakh and Russian compared to high-resource languages.

**Venue/Conference Information:**
No conference affiliation is mentioned. The paper is categorized under Computation and Language (cs.CL) on arXiv.

**Submission/Publication Dates:**
- v1 submitted: February 18, 2025
- v2 revised: July 21, 2025

**ACL 2025 Confirmation:**
The page does not confirm this as an ACL 2025 submission. The abstract notes "Data and code will be made available upon acceptance," suggesting it may be under review, but no specific venue confirmation appears.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37ca3d94-1f05-4309-b214-4b8d87c50de7",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "94ceff26-cee6-46d4-a888-5e3dad58f9c4",
  "sourceToolAssistantUUID": "37ca3d94-1f05-4309-b214-4b8d87c50de7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-10T07:26:02.974Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J2k5otaFLXex7sWVBLB2Pe`</summary>

```json
{
  "query": "\"typological distance\" OR \"typological similarity\" language weighting instruction tuning 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94ceff26-cee6-46d4-a888-5e3dad58f9c4",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVQJdm3iPTFCgYnrUz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a6958d0-bea1-475b-b4af-647b2b618824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vfn3NgLqsm6Vx5XsWAdU4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7601,
      "cache_creation_input_tokens": 4444,
      "cache_read_input_tokens": 11059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4444,
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

_source line 39 · 2026-05-10T07:26:02.978Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J9njdKq246ZHAKWWSXs55m`</summary>

```json
{
  "query": "curriculum multilingual instruction tuning arxiv 2025 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a6958d0-bea1-475b-b4af-647b2b618824",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVQJdm3iPTFCgYnrUz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c959d7a-2124-4a99-9f02-98a8284c5522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vfn3NgLqsm6Vx5XsWAdU4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7601,
      "cache_creation_input_tokens": 4444,
      "cache_read_input_tokens": 11059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4444,
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

_source line 40 · 2026-05-10T07:26:04.144Z_

<details><summary>↩ Tool result · `toolu_019yXyJEQoSqwSBXBT3yxAxA`</summary>

```text
# TUMLU Paper Summary

**Full Title:** "TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages"

**Authors:** Jafar Isbarov, Arofat Akhundjanova, Mammad Hajili, Kavsar Huseynova, Dmitry Gaynullin, Anar Rzayev, Osman Tursun, Aizirek Turdubaeva, Ilshat Saetov, Rinat Kharisov, Saule Belginova, Ariana Kenbayeva, Amina Alisheva, Abdullatif Köksal, Samir Rustamov, Duygu Ataman (16 total)

**Abstract:** The research introduces a comprehensive benchmark designed to evaluate multilingual language model capabilities across Turkic languages. Rather than relying on machine translation, the dataset comprises "middle- and high-school level questions spanning 11 academic subjects" in eight languages, with TUMLU-mini as a verified subset released for public research use.

**Venue & Status:** Yes, confirmed as "Accepted to ACL 2025, Main Conference"

**Submission Timeline:** 
- Initial submission: February 16, 2025
- Revision 2: June 13, 2025

**Language Coverage:** The benchmark includes **Uyghur and Kazakh**. However, **Mongolian is not covered**—the eight languages are Azerbaijani, Crimean Tatar, Karakalpak, Kazakh, Tatar, Turkish, Uyghur, and Uzbek.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a416d1a6-9621-46e1-addd-121ad14a2b87",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "6bde65c2-db20-4852-a101-a3f2cfe627b9",
  "sourceToolAssistantUUID": "a416d1a6-9621-46e1-addd-121ad14a2b87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T07:26:04.563Z_

<details><summary>↩ Tool result · `toolu_01Xrfcmm7xstuJ5YM7D42PBB`</summary>

```text
# MiLiC-Eval Paper Summary

**Full Title:** "MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages"

**Authors:** Chen Zhang, Mingxu Tao, Zhiyuan Liao, Yansong Feng

**Venue:** Yes, this is confirmed as "ACL 2025 (Findings)"

## Languages Covered

The benchmark addresses four minority language groups in China:
- Tibetan
- Uyghur
- Kazakh
- Mongolian

## Abstract Overview

The research introduces a benchmark with "24K instances across 9 tasks" designed to evaluate how large language models handle these underrepresented languages. The work emphasizes that "its parallelism between tasks and languages can provide a faithful and fine-grained assessment of linguistic and problem-solving skills."

## Main Evaluation Results

The evaluation demonstrated two key findings:

1. **Performance gaps:** "Open-source LLMs perform poorly on syntax-intensive tasks and multi-script languages"

2. **Research value:** The benchmark shows potential for advancing low-resource language research by addressing "diverse writing systems and understanding the process of language adaptation"

**Access:** Code and data are publicly available on GitHub at the provided repository link.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99f7851a-0495-430b-8e28-1855ddca9c13",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "19014330-ec80-4c9f-aa75-0bbb611b9ef6",
  "sourceToolAssistantUUID": "99f7851a-0495-430b-8e28-1855ddca9c13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T07:26:05.660Z_

<details><summary>↩ Tool result · `toolu_01M26LjpkLroX9F2ZGEMNs8u`</summary>

```text
# Paper Summary

**Full Title:** Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment

**Authors:** Wen Yang, Junhong Wu, Chen Wang, Chengqing Zong, Jiajun Zhang

**Venue:** Yes, this is ACL 2025 Findings (camera-ready version)

## Main Method

The researchers propose extracting preference knowledge from English-aligned language models through implicit reward signals. They "derive an implicit reward model from the logits of an English DPO-aligned model" and use it to evaluate multilingual responses generated from English instructions, creating annotated preference pairs for further fine-tuning.

## Key Results

When fine-tuning Llama3 for two iterations on the X-AlpacaEval leaderboard:
- **12.72%** average improvement in Win Rate across all training languages
- **5.97%** increase in Length Control Win Rate

The approach demonstrates that leveraging existing English models significantly reduces the need for extensive multilingual preference datasets while enabling effective cross-lingual knowledge transfer.

**Code Availability:** Published on GitHub (ZNLP/Implicit-Cross-Lingual-Rewarding)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01a9e1e3-1333-4057-bc91-410a2b825ddc",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "fabaf36d-313a-4bf8-9d79-c351456f7f5f",
  "sourceToolAssistantUUID": "01a9e1e3-1333-4057-bc91-410a2b825ddc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T07:26:10.182Z_

<details><summary>↩ Tool result · `toolu_01J9njdKq246ZHAKWWSXs55m`</summary>

```text
Web search results for query: "curriculum multilingual instruction tuning arxiv 2025 site:arxiv.org"

Links: [{"title":"[2511.10229] LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning","url":"https://arxiv.org/abs/2511.10229"},{"title":"LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning","url":"https://arxiv.org/html/2511.10229"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854"},{"title":"[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/abs/2402.13703"},{"title":"Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning","url":"https://arxiv.org/html/2509.13790"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"LuxIT: A Luxembourgish Instruction Tuning Dataset from Monolingual Seed Data","url":"https://arxiv.org/html/2510.24434"},{"title":"A Survey of Instruction Tuning in Large Language Models","url":"https://www.arxiv.org/pdf/2508.17184"},{"title":"[2401.01854] Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/abs/2401.01854"},{"title":"Improving Multilingual Capabilities with Cultural and Local Knowledge in Large Language Models While Enhancing Native Performance","url":"https://arxiv.org/html/2504.09753"}]

I found several relevant papers on arXiv related to curriculum multilingual instruction tuning. Here are the most notable results:

## Most Recent and Directly Relevant:

**LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning** (arXiv:2511.10229, November 2025)

This appears to be the most recent paper directly addressing curriculum multilingual instruction tuning. Language separability can serve as an effective signal for multilingual curriculum learning, where interleaving samples with diverse separability levels yields stable and generalizable gains. Language separability enables effective curriculum learning: interleaving training samples with diverse separability levels allows models to absorb both structured and entangled linguistic signals, improving training effectiveness.

## Other Related Papers:

**Multilingual Instruction Tuning With Just a Pinch of Multilinguality** (arXiv:2401.01854, January 2024)

This paper investigates multilingual instruction tuning and finds that only 40 multilingual examples integrated in an English tuning set substantially improve multilingual instruction-following, both in seen and unseen languages during tuning.

**Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning** (arXiv:2509.13790, November 2025)

This paper addresses curriculum learning for instruction tuning, discussing how curriculum strategies are used as data organization approaches in instruction tuning.

The LangGPS paper seems most directly aligned with your search query as it specifically combines curriculum learning with multilingual instruction tuning using language separability as a guiding principle.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c959d7a-2124-4a99-9f02-98a8284c5522",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "73ee4718-6256-4be7-a123-b0f15eef1689",
  "sourceToolAssistantUUID": "7c959d7a-2124-4a99-9f02-98a8284c5522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T07:26:10.255Z_

<details><summary>↩ Tool result · `toolu_01HT5a2z9VzBpBmMDFbJm4Ts`</summary>

```text
Web search results for query: "language-weighted data sampling cross-lingual transfer multi-pivot instruction tuning 2025"

Links: [{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10517622-plug-leveraging-pivot-language-cross-lingual-instruction-tuning"},{"title":"Published in Transactions on Machine Learning Research (11/2025)","url":"https://openreview.net/pdf?id=oapsbIO1Bd"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"(PDF) Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://www.researchgate.net/publication/397087634_Revisiting_Multilingual_Data_Mixtures_in_Language_Model_Pretraining"},{"title":"Zero-shot cross-lingual transfer in instruction tuning of large language models","url":"https://arxiv.org/html/2402.14778v2"},{"title":"Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"},{"title":"[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/abs/2311.08711"},{"title":"Multilingual Large Language Models: A Systematic Survey","url":"https://arxiv.org/html/2411.11072v1"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning | Request PDF","url":"https://www.researchgate.net/publication/384213466_PLUG_Leveraging_Pivot_Language_in_Cross-Lingual_Instruction_Tuning"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"}]

I found several relevant research papers and projects related to your search query. Here are the key findings:

## Multi-Pivot Instruction Tuning Approaches

PLUG (Pivot Language Guided Generation) is an approach that utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages, training the model to first process instructions in the pivot language, and then produce responses in the target language.

Many approaches augment multilingual tuning with cross-lingual alignment to further improve cross-lingual transfer, typically using English, the best resourced language, as the pivot language, aligning the understanding, reasoning, and generation capabilities of LLMs in non-English languages with those in English.

## Language-Weighted Data Sampling

Recent 2025 research addresses multilingual data composition more directly. Using multiple pivots that balance breadth and proximity provides the most consistent benefits across language families. Additionally, research on selective sampling focuses on selecting relevant cross-lingual data that mirrors the target language's usage patterns, addressing this by selectively sampling auxiliary language data that aligns with the target language's distribution gaps.

Under temperature sampling, the issue closely resembles a curse of data quality: oversampling very low-resource languages introduces more noisy data into training, which hurts performance. The curse of multilinguality, while measurable, likely arises not from simply adding more languages, but from the finite capacity of models and data distributions that too strongly amplify the impact of languages represented by lower-quality data.

## Cross-Lingual Transfer Effectiveness

Replacing even a small number of monolingual (English) training samples with multilingual ones significantly improves performance on these languages, aligning with research emphasizing the advantages of multilingual instruction tuning over monolingual instruction tuning, especially in resource-constrained settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25dda32e-b468-4df8-9e0b-9a86a989b6cc",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "37fe38d9-7fb5-46ef-b62b-760773f8df7c",
  "sourceToolAssistantUUID": "25dda32e-b468-4df8-9e0b-9a86a989b6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T07:26:17.369Z_

<details><summary>↩ Tool result · `toolu_01J2k5otaFLXex7sWVBLB2Pe`</summary>

```text
Web search results for query: ""typological distance" OR "typological similarity" language weighting instruction tuning 2025 arxiv"

Links: [{"title":"Less is More: The Effectiveness of Compact Typological Language Representations","url":"https://arxiv.org/html/2509.20129"},{"title":"Large Language Models are Easily Confused: A Quantitative Metric, Security Implications and Typological Analysis","url":"https://arxiv.org/html/2410.13237"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=2050&show=2000"},{"title":"Computation and Language Jan 2025","url":"https://www.arxiv.org/list/cs.CL/2025-01?skip=275&show=2000"},{"title":"[1309.4168] Exploiting Similarities among Languages for Machine Translation","url":"https://ar5iv.labs.arxiv.org/html/1309.4168"},{"title":"Predicting Machine Translation Performance on Low-Resource Languages: The Role of Domain Similarity","url":"https://arxiv.org/html/2402.02633v1"},{"title":"[2512.12063] Instruction-Tuning Open-Weight Language Models for BPMN Model Generation","url":"https://arxiv.org/abs/2512.12063"},{"title":"[2305.13401] A study of conceptual language similarity: comparison and evaluation","url":"https://arxiv.org/abs/2305.13401"},{"title":"On the Effect of Instruction Tuning Loss on Generalization Anwoy Chatterjee∗†","url":"https://arxiv.org/pdf/2507.07817"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854"}]

Based on the web search results, I found several relevant papers related to typological distance/similarity and language weighting in instruction tuning from 2025 and recent arxiv submissions:

## Key Papers Found:

1. **"Less is More: The Effectiveness of Compact Typological Language Representations"** (arxiv 2509.20129, September 2025)
   - This paper constructs a 5-nearest neighbour graph over languages, using a heat kernel to assign edge weights based on feature-space distance.
   - The paper discusses URIEL+ (Khan et al., 2025), an enhanced version that expands feature coverage and integrates additional databases (e.g. SAPhon for phonology, Grambank for morphology) to increase the number of features and languages covered.
   - Lower-scoring features are more stable across similar languages and thus more likely to encode intrinsic typological patterns.

2. **"Large Language Models are Easily Confused: A Quantitative Metric, Security Implications and Typological Analysis"** (arxiv 2410.13237, February 2025)
   - The findings show strong correlations between language confusion and semantic similarities among languages, with less confusion observed in low-resource languages and when training incorporates diverse scripts and language families, suggesting linguistic typology as a potential tool for enhancing model security.

3. **"Multilingual Instruction Tuning With Just a Pinch of Multilinguality"** (arxiv 2401.01854, July 2025)
   - The paper tests two potential factors that might influence the degree of cross-lingual transfer: language similarity and the amount of language-specific pre-training data, but finds no significant correlations.

These papers address the intersection of typological language properties and instruction tuning, though the specific focus on language weighting based on typological distance may require examining the full papers directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a6958d0-bea1-475b-b4af-647b2b618824",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "b6c2f70a-da77-48f2-8020-c842862188be",
  "sourceToolAssistantUUID": "2a6958d0-bea1-475b-b4af-647b2b618824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-10T07:26:19.537Z_

Now let me fetch a few more critical papers and check the EMNLP 2026 OpenReview page directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6c2f70a-da77-48f2-8020-c842862188be",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVS9mX6tNY9m6ScXj3F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46dc3b2e-5a39-4b74-9db8-d01e1046a37f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GBQYcHP3epaTNwHtHPARPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 18967,
      "cache_read_input_tokens": 8088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18967,
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

_source line 47 · 2026-05-10T07:26:21.258Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012aNeXXPB3GCg7NZmvZgMCk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.10229",
  "prompt": "Extract full title, authors, abstract, and venue/conference information. What is the core method? Does it compete with typological-distance-weighted data sampling for multilingual instruction tuning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46dc3b2e-5a39-4b74-9db8-d01e1046a37f",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVS9mX6tNY9m6ScXj3F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c1ec3b6-f8a5-4c69-ab26-f05b0ae6ee58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GBQYcHP3epaTNwHtHPARPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 18967,
      "cache_read_input_tokens": 8088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18967,
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

_source line 48 · 2026-05-10T07:26:23.658Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VpXsR6oYTxugg3K1EF2Xg9`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.07809",
  "prompt": "Extract full title, authors, abstract, venue, and key claims. Does this paper address which languages to use for multilingual instruction tuning and whether typological diversity matters? What are the main findings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c1ec3b6-f8a5-4c69-ab26-f05b0ae6ee58",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVS9mX6tNY9m6ScXj3F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6254f3a-5110-4df5-8e31-a05f83dfeb55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GBQYcHP3epaTNwHtHPARPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 18967,
      "cache_read_input_tokens": 8088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18967,
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

_source line 49 · 2026-05-10T07:26:24.728Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U8tagYBr4t4zsP8hhH54Hq`</summary>

```json
{
  "url": "https://openreview.net/group?id=EMNLP%2F2026%2FConference",
  "prompt": "Is there any list of accepted or submitted papers here? Are there papers on cross-lingual instruction tuning or multilingual fine-tuning? What is the status of the EMNLP 2026 conference submissions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6254f3a-5110-4df5-8e31-a05f83dfeb55",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVS9mX6tNY9m6ScXj3F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e6833a8-1eab-47f0-aaf9-45c6e92bbd50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GBQYcHP3epaTNwHtHPARPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 18967,
      "cache_read_input_tokens": 8088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18967,
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

_source line 50 · 2026-05-10T07:26:25.599Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HJ2ZDvcRb8o5FcrnspKYAd`</summary>

```json
{
  "query": "LangGPS language separability multilingual instruction tuning arxiv 2511.10229 ACL EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e6833a8-1eab-47f0-aaf9-45c6e92bbd50",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVS9mX6tNY9m6ScXj3F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "112e5e22-aa42-47b2-a0a4-9d3c8eedd772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GBQYcHP3epaTNwHtHPARPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 18967,
      "cache_read_input_tokens": 8088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18967,
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

_source line 51 · 2026-05-10T07:26:25.620Z_

<details><summary>↩ Tool result · `toolu_012aNeXXPB3GCg7NZmvZgMCk`</summary>

```text
# LangGPS Paper Summary

**Full Title:** LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning

**Authors:** Yangfan Ye, Xiaocheng Feng, Xiachong Feng, Lei Huang, Weitao Ma, Qichen Hong, Yunfei Lu, Duyu Tang, Dandan Tu, Bing Qin

**Venue:** AAAI 2026 Main Track (Accepted)

**Core Method:**
LangGPS implements "a lightweight two-stage pre-selection framework guided by language separability" that quantifies how distinguishable samples from different languages are in a model's representation space. The approach filters data based on separability scores, then refines selections using existing methods. Testing covered six benchmarks and 22 languages.

**Regarding Typological-Distance-Weighted Sampling:**
The provided abstract and paper metadata do not mention typological-distance-weighted data sampling or discuss direct competition with such approaches. The abstract focuses on language separability as a novel signal for data selection but does not compare against or reference typological distance methods specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c1ec3b6-f8a5-4c69-ab26-f05b0ae6ee58",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "5a183dfe-217c-45a5-9296-be9a90e71d5f",
  "sourceToolAssistantUUID": "5c1ec3b6-f8a5-4c69-ab26-f05b0ae6ee58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-10T07:26:26.412Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014QC4advpD6Ud5K4p4C92o8`</summary>

```json
{
  "query": "\"Linguistically-Informed Multilingual Instruction Tuning\" optimal languages tune arxiv 2410.07809"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a183dfe-217c-45a5-9296-be9a90e71d5f",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVS9mX6tNY9m6ScXj3F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be2d497b-2bf0-45a1-afd4-fa2eda1aa633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GBQYcHP3epaTNwHtHPARPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 18967,
      "cache_read_input_tokens": 8088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18967,
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

_source line 53 · 2026-05-10T07:26:27.035Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HrcHwR8JTrjTMdL3ai5HNm`</summary>

```json
{
  "query": "Sherkala-Chat Kazakh LLM instruction tuning arXiv 2503.01493 ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be2d497b-2bf0-45a1-afd4-fa2eda1aa633",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVS9mX6tNY9m6ScXj3F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ebfbce4-a05a-42b7-abc4-300ddd26f972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GBQYcHP3epaTNwHtHPARPB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 18967,
      "cache_read_input_tokens": 8088,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18967
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 902,
          "output_tokens": 571,
          "cache_read_input_tokens": 8088,
          "cache_creation_input_tokens": 18967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18967,
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

_source line 54 · 2026-05-10T07:26:27.155Z_

<details><summary>↩ Tool result · `toolu_01U8tagYBr4t4zsP8hhH54Hq`</summary>

```text
Based on the provided web page content, I cannot answer your questions about accepted or submitted papers, cross-lingual instruction tuning research, or the submission status of EMNLP 2026.

The page only displays OpenReview's navigation menu and footer information. It does not contain any conference details, paper listings, or submission information. The content shows that this is the EMNLP 2026 Conference venue page on OpenReview, but the actual conference details and paper database appear to be on a different page that wasn't included in the provided excerpt.

To find this information, you would need to visit the full EMNLP 2026 venue page on OpenReview.net directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e6833a8-1eab-47f0-aaf9-45c6e92bbd50",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "7e35acc4-64ba-4517-9aa2-a1fc8f89b79e",
  "sourceToolAssistantUUID": "0e6833a8-1eab-47f0-aaf9-45c6e92bbd50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-10T07:26:29.367Z_

<details><summary>↩ Tool result · `toolu_01VpXsR6oYTxugg3K1EF2Xg9`</summary>

```text
# Paper Summary

**Full Title:** "Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?"

**Authors:** Gürkan Soykan (Wageningen University and Research, Koç University), Gözde Gül Şahin (Koç University, KUIS AI)

**Venue:** arXiv:2410.07809v1

**Abstract:** The paper investigates whether strategically selecting languages based on linguistic features improves multilingual instruction tuning performance, compared to random selection or using all available languages.

## Key Claims

1. **Main Research Question:** The work systematically examines how language selection strategies affect instruction tuning outcomes across multiple models and tasks.

2. **Core Finding:** "Linguistically informed language selection for multilingual instruction tuning generally outperforms the random baseline" in terms of average performance across model families and sizes.

3. **Task and Model Dependency:** The optimal language subset varies by specific tasks and model families—"there exists no universally 'best selection' technique that consistently achieves the highest scores across tasks and models."

4. **Typological Diversity Matters:** The study tests multiple feature-based approaches including typological vectors, geographical features, learned embeddings, and semantic typology. Results show these linguistic features provide meaningful signals for language selection.

5. **Cross-lingual Generalization:** "Cross-lingual generalization capabilities vary significantly across different language subsets," suggesting linguistically informed selections improve transfer to unseen languages.

6. **Curse of Multilinguality:** "Increasing the number of languages beyond a certain threshold results in performance degradation" under fixed computational budgets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6254f3a-5110-4df5-8e31-a05f83dfeb55",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "3fc5d1c5-0de7-43fb-b81e-1a53288d78bf",
  "sourceToolAssistantUUID": "c6254f3a-5110-4df5-8e31-a05f83dfeb55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-10T07:26:32.354Z_

<details><summary>↩ Tool result · `toolu_01HJ2ZDvcRb8o5FcrnspKYAd`</summary>

```text
Web search results for query: "LangGPS language separability multilingual instruction tuning arxiv 2511.10229 ACL EMNLP 2025"

Links: [{"title":"[2511.10229] LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning","url":"https://arxiv.org/abs/2511.10229"},{"title":"LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning","url":"https://arxiv.org/html/2511.10229"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854v4"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"Language steering in latent space to mitigate unintended code-switching","url":"https://arxiv.org/html/2510.13849"},{"title":"[2401.01854] Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/abs/2401.01854"},{"title":"[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/abs/2402.13703"},{"title":"Linguistically-Informed Multilingual Instruction Tuning","url":"https://arxiv.org/pdf/2410.07809"},{"title":"[2401.01854v1] Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/abs/2401.01854v1"},{"title":"LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks","url":"https://arxiv.org/html/2412.12499v1"}]

Based on the search results, I found the paper you're looking for. Here's the information about LangGPS:

## LangGPS: Language Separability Guided Data Pre-Selection

LangGPS is a lightweight two-stage pre-selection framework guided by language separability which quantifies how well samples in different languages can be distinguished in the model's representation space.

**Problem Addressed:** Joint multilingual instruction tuning is a widely adopted approach to improve the multilingual instruction-following ability of large language models, but the resulting multilingual capability remains highly sensitive to the composition and selection of the training data, and existing selection methods often overlook the intrinsic linguistic structure of multilingual data.

**Approach:** LangGPS first filters training data based on separability scores and then refines the subset using existing selection methods.

**Results:** Extensive experiments across six benchmarks and 22 languages demonstrate that applying LangGPS on top of existing selection methods improves their effectiveness. Additionally, LangGPS can be seamlessly integrated with existing selection methods and improves their effectiveness and generalizability, especially for understanding tasks and low-resource languages.

**Paper Details:** The paper was submitted on November 13, 2025 (arxiv:2511.10229) and appears to be recent work in the field of multilingual instruction tuning for language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "112e5e22-aa42-47b2-a0a4-9d3c8eedd772",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "051bb4c3-8c0e-4adb-a2b1-a9b4fc3ae839",
  "sourceToolAssistantUUID": "112e5e22-aa42-47b2-a0a4-9d3c8eedd772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-10T07:26:34.961Z_

<details><summary>↩ Tool result · `toolu_01HrcHwR8JTrjTMdL3ai5HNm`</summary>

```text
Web search results for query: "Sherkala-Chat Kazakh LLM instruction tuning arXiv 2503.01493 ACL 2025"

Links: [{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh ...","url":"https://arxiv.org/pdf/2503.01493"},{"title":"[2503.01493] Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting","url":"https://arxiv.org/abs/2503.01493"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting","url":"https://arxiv.org/html/2503.01493"},{"title":"(PDF) Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://www.researchgate.net/publication/389580277_Llama-31-Sherkala-8B-Chat_An_Open_Large_Language_Model_for_Kazakh"},{"title":"inceptionai/Llama-3.1-Sherkala-8B-Chat · Hugging Face","url":"https://huggingface.co/inceptionai/Llama-3.1-Sherkala-8B-Chat"},{"title":"Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://arxiv.org/html/2503.01493v1"},{"title":"Paper page - Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://huggingface.co/papers/2503.01493"},{"title":"Fine-Tuning Large Language Models for Kazakh Text ...","url":"https://www.preprints.org/manuscript/202506.1947/v1/download"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250301493K/abstract"},{"title":"A Systematic Evaluation of Large Language Models and Retrieval-Augmented Generation for the Task of Kazakh Question Answering","url":"https://www.mdpi.com/2078-2489/16/11/943"}]

Based on the search results, I found detailed information about the Sherkala-Chat Kazakh LLM paper:

## Sherkala-Chat: Kazakh LLM with Instruction Tuning

Sherkala-Chat (8B) is a state-of-the-art instruction-tuned open generative large language model (LLM) designed for Kazakh. Adapted from the LLaMA-3.1-8B model, Sherkala-Chat (8B) is trained on 45.3B tokens across Kazakh, English, Russian, and Turkish.

### Model Architecture and Training Approach

The model continuously pretrains Sherkala (8B) starting from the LLaMA-3.1 model, and designs a custom tokenizer that balances Kazakh and English, expanding the vocabulary by 25% to capture Kazakh-specific words and expressions more effectively.

### Instruction Tuning Strategy

To develop a Kazakh instruction-tuning dataset, two strategies are employed: (1) translating existing English instruction-tuning datasets into Kazakh using machine translation and (2) constructing an in-house dataset from cultural wiki sources and public governmental data. To ensure effective and responsible alignment, the model leverages translated instruction datasets, a Kazakhstan-specific instruction dataset that is automatically constructed and manually verified, and Kazakh-specific safety data.

### Performance Results

With additional instruction fine-tuning (IFT) and safety tuning, Sherkala-Chat (8B) achieves the highest score of 47.6, making it a new benchmark for state-of-the-art Kazakh language models. This represents a +3.9 point improvement over KazLLM-1.0 (8B), a +9.9 point improvement over Irbis-v0.1 (7B), and a significant lead over all multilingual models.

The paper (arXiv:2503.01493) was submitted on March 3, 2025, and the model is released as an open-weight model on Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ebfbce4-a05a-42b7-abc4-300ddd26f972",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "fb1df685-e2b4-4d7c-8658-80877978d5c8",
  "sourceToolAssistantUUID": "1ebfbce4-a05a-42b7-abc4-300ddd26f972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T07:26:36.327Z_

<details><summary>↩ Tool result · `toolu_014QC4advpD6Ud5K4p4C92o8`</summary>

```text
Web search results for query: ""Linguistically-Informed Multilingual Instruction Tuning" optimal languages tune arxiv 2410.07809"

Links: [{"title":"[2410.07809] Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/abs/2410.07809"},{"title":"Linguistically-Informed Multilingual Instruction Tuning","url":"https://arxiv.org/pdf/2410.07809"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809v1"},{"title":"(PDF) Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://www.researchgate.net/publication/384811791_Linguistically-Informed_Multilingual_Instruction_Tuning_Is_There_an_Optimal_Set_of_Languages_to_Tune"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/linguistically-informed-multilingual-instruction-tuning-is-there"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/investigating-multilingual-instruction-tuning-do-polyglot-models"},{"title":"Improving Multilingual Instruction Finetuning via Linguistically Natural and Diverse Datasets","url":"https://arxiv.org/html/2407.01853v1"},{"title":"[2407.01853] Improving Multilingual Instruction Finetuning via Linguistically Natural and Diverse Datasets","url":"https://arxiv.org/abs/2407.01853"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854v4"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"}]

Based on the web search results, here is information about the paper "Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?" (arxiv 2410.07809):

## Overview

The paper addresses how multilingual language models often perform unevenly across different languages due to limited generalization capabilities. The research investigates how choosing different languages affects multilingual instruction tuning and proposes a method to select languages for instruction tuning in a linguistically informed way.

## Key Problem

The approach is challenged by high computational costs, a lack of quality tuning data for all languages, and the "curse of multilinguality" -- the performance drop per language after adding many languages.

## Methodology

The study hypothesizes that optimum language subset selection for multilingual instruction tuning can be achieved in a linguistically informed manner and investigates various language selection techniques compared to baselines such as randomly selected subsets and subsets curated by picking a single language from each language family. The linguistically informed selection techniques range from typological feature vectors to language embeddings derived from semantic typology features, with a simple k-means clustering algorithm applied to select a fixed number of languages.

## Results

The results show that careful language selection generally leads to better outcomes than choosing languages at random.

## Reproducibility

Code for language selection and multilingual instruction tuning is available at https://github.com/GGLAB-KU/ling-informed-mit.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be2d497b-2bf0-45a1-afd4-fa2eda1aa633",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "6b3a8976-9ca0-4d6e-accb-453771d26d07",
  "sourceToolAssistantUUID": "be2d497b-2bf0-45a1-afd4-fa2eda1aa633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-10T07:26:41.268Z_

Now let me check a few more important items: the ACL 2025 status of KazMMLU, the Code-Switching Curriculum paper, and the EMNLP 2026 OpenReview submissions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b3a8976-9ca0-4d6e-accb-453771d26d07",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVTYrrdJQWzvi7djJSh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "177b5961-c869-4972-8b37-529ee55888d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BMzA8rz7NsB6PfhxkN5arh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1143,
      "cache_creation_input_tokens": 4253,
      "cache_read_input_tokens": 27055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4253,
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

_source line 60 · 2026-05-10T07:26:43.817Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VPArsuDNwFxWzZ1HwD84gm`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-acl.407.pdf",
  "prompt": "Extract the full title, authors, abstract, and venue. What is the core method? Does it use curriculum learning for cross-lingual or multilingual instruction tuning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "177b5961-c869-4972-8b37-529ee55888d4",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVTYrrdJQWzvi7djJSh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b323abd3-a289-4a2f-9396-5e4c79b4d42d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BMzA8rz7NsB6PfhxkN5arh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1143,
      "cache_creation_input_tokens": 4253,
      "cache_read_input_tokens": 27055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4253,
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

_source line 61 · 2026-05-10T07:26:46.307Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014pYvNwdz4Hq14JBDP4Pdms`</summary>

```json
{
  "url": "https://openreview.net/pdf?id=oapsbIO1Bd",
  "prompt": "Extract full title, authors, abstract, venue (is this TMLR?), and key claims. Does this paper address multilingual instruction tuning with curriculum or data weighting approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b323abd3-a289-4a2f-9396-5e4c79b4d42d",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVTYrrdJQWzvi7djJSh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f03e2298-bb6e-48ca-b3fb-b85c04589766",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BMzA8rz7NsB6PfhxkN5arh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1143,
      "cache_creation_input_tokens": 4253,
      "cache_read_input_tokens": 27055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4253,
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

_source line 62 · 2026-05-10T07:26:46.408Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VW6oF74BA5zcSkmdoFYo5z`</summary>

```json
{
  "query": "KazMMLU ACL 2025 accepted \"2502.12829\" anthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f03e2298-bb6e-48ca-b3fb-b85c04589766",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVTYrrdJQWzvi7djJSh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8280441c-973e-4e2d-ad14-e2fea258118e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BMzA8rz7NsB6PfhxkN5arh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1143,
      "cache_creation_input_tokens": 4253,
      "cache_read_input_tokens": 27055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4253,
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

_source line 63 · 2026-05-10T07:26:46.454Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KtGUVeDLgDdT38rG797Kk7`</summary>

```json
{
  "query": "\"multi-pivot\" instruction tuning typological distance source language weighting arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8280441c-973e-4e2d-ad14-e2fea258118e",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVTYrrdJQWzvi7djJSh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b64d6576-078c-4dd9-a246-48123263cfac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BMzA8rz7NsB6PfhxkN5arh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1143,
      "cache_creation_input_tokens": 4253,
      "cache_read_input_tokens": 27055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4253,
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

_source line 64 · 2026-05-10T07:26:47.825Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XusNuoxzQpB2d56BQ7usD6`</summary>

```json
{
  "url": "https://openreview.net/forum?id=dqxXAgFjra",
  "prompt": "Extract full title, authors, abstract, venue/conference information. Is this EMNLP 2026? What is the method and does it compete with typological-distance-weighted multi-source instruction tuning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b64d6576-078c-4dd9-a246-48123263cfac",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVTYrrdJQWzvi7djJSh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e739d1e-4ded-46ab-9af1-9b2761f86151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BMzA8rz7NsB6PfhxkN5arh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1143,
      "cache_creation_input_tokens": 4253,
      "cache_read_input_tokens": 27055,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4253
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1143,
          "output_tokens": 508,
          "cache_read_input_tokens": 27055,
          "cache_creation_input_tokens": 4253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4253,
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

_source line 65 · 2026-05-10T07:26:49.488Z_

<details><summary>↩ Tool result · `toolu_01VPArsuDNwFxWzZ1HwD84gm`</summary>

```text
I apologize, but the content provided appears to be a PDF file encoded in binary/compressed format rather than readable text. The data shows PDF stream objects with FlateDecode compression, making it impossible to extract the title, authors, abstract, venue, or methodology information you've requested.

To properly analyze this paper, I would need:
- A plain text version of the document
- An uncompressed PDF that can be read directly
- The actual paper content in a readable format

**Could you provide:**
1. The paper title or DOI?
2. A text-based version of the abstract?
3. A link to the paper source?

Once you share readable content, I'll be happy to extract the requested information about the title, authors, abstract, venue, core methods, and whether it employs curriculum learning for cross-lingual or multilingual instruction tuning.

[Binary content (application/pdf, 2.5MB) also saved to /home/ubuntu/.claude-account-2/projects/-/58594df9-bda3-4ed6-a9ac-9ce91e2c084d/tool-results/webfetch-1778398006092-b8k2p3.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b323abd3-a289-4a2f-9396-5e4c79b4d42d",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "845c6db0-fbda-459d-9f78-4fd1c56ae651",
  "sourceToolAssistantUUID": "b323abd3-a289-4a2f-9396-5e4c79b4d42d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-10T07:26:50.644Z_

<details><summary>↩ Tool result · `toolu_01XusNuoxzQpB2d56BQ7usD6`</summary>

```text
I cannot extract the requested information from the provided content. The webpage shows only the OpenReview.net login and navigation pages—no actual research paper is present.

The content includes:
- Navigation menus
- Links to "About OpenReview," "All Venues," and other platform features
- Footer information stating "OpenReview is a long-term project to advance science through improved peer review"

**What's missing:**
- Paper title
- Authors
- Abstract
- Venue/conference details
- Method information
- Any comparison to typological-distance-weighted multi-source instruction tuning

To obtain this information, you would need to provide the actual paper webpage content from OpenReview, which would display the manuscript details, not the platform's login interface.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e739d1e-4ded-46ab-9af1-9b2761f86151",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "2dde08e5-2b86-4a8e-9342-270ba61cf3c2",
  "sourceToolAssistantUUID": "8e739d1e-4ded-46ab-9af1-9b2761f86151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-10T07:26:51.338Z_

<details><summary>↩ Tool result · `toolu_014pYvNwdz4Hq14JBDP4Pdms`</summary>

```text
I appreciate your request, but I need to be direct: the content you've provided is a PDF file in binary format (encoded as raw PDF objects), not readable text. The "web page content" consists of PDF internal structures (object streams, compression filters, font definitions, etc.) rather than extracted text.

To properly help you, I would need:
- The actual extracted text from the PDF
- Or a direct link to the paper
- Or the paper's DOI/arXiv identifier

**What I can tell you:** Based on the PDF metadata visible in the objects, this appears to be a substantial academic document (approximately 53 pages, 2155 objects), but I cannot extract:
- Title
- Authors
- Abstract
- Venue information
- Key claims
- Whether it addresses multilingual instruction tuning or curriculum learning

**Next steps:** Could you provide either:
1. The paper's title or arXiv ID?
2. Plain text extracted from the PDF?
3. A direct URL to the paper?

Then I can give you the specific analysis you're requesting about multilingual instruction tuning, curriculum approaches, and data weighting techniques, while respecting the 125-character quote limit.

[Binary content (application/pdf, 1.4MB) also saved to /home/ubuntu/.claude-account-2/projects/-/58594df9-bda3-4ed6-a9ac-9ce91e2c084d/tool-results/webfetch-1778398007010-xphxz3.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f03e2298-bb6e-48ca-b3fb-b85c04589766",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "a5273d2b-fe80-4620-9c58-7fea3a1b4e25",
  "sourceToolAssistantUUID": "f03e2298-bb6e-48ca-b3fb-b85c04589766",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-10T07:26:51.494Z_

<details><summary>↩ Tool result · `toolu_01VW6oF74BA5zcSkmdoFYo5z`</summary>

```text
Web search results for query: "KazMMLU ACL 2025 accepted "2502.12829" anthology"

Links: [{"title":"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.701/"},{"title":"[2502.12829] KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan","url":"https://arxiv.org/abs/2502.12829"},{"title":"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan","url":"https://arxiv.org/html/2502.12829"},{"title":"KazMMLU: Evaluating Language Models on Kazakh, Russian,","url":"https://arxiv.org/pdf/2502.12829v1"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.acl-short/"},{"title":"ACL Anthology","url":"https://aclanthology.org/"},{"title":"Annual Meeting of the Association for Computational Linguistics (2025) - ACL Anthology","url":"https://aclanthology.org/events/acl-2025/"},{"title":"Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 3: Industry Track) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.naacl-industry/"},{"title":"Findings of the Association for Computational Linguistics: NAACL 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-naacl/"}]

Based on the search results, I found information about the KazMMLU paper:

KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan was accepted and published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 14403–14416, Vienna, Austria.

The paper is available in the ACL Anthology at: https://aclanthology.org/2025.acl-long.701/

The arXiv preprint (2502.12829) can be found at: https://arxiv.org/abs/2502.12829

KazMMLU comprises 23,000 questions that cover various educational levels, including STEM, humanities, and social sciences, sourced from authentic educational materials and manually validated by native speakers and educators. The dataset includes 10,969 Kazakh questions and 12,031 Russian questions, reflecting Kazakhstan's bilingual education system and rich local context.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8280441c-973e-4e2d-ad14-e2fea258118e",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "a801b79d-00a2-434f-8fac-158a4f57b4d1",
  "sourceToolAssistantUUID": "8280441c-973e-4e2d-ad14-e2fea258118e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-10T07:26:56.585Z_

<details><summary>↩ Tool result · `toolu_01KtGUVeDLgDdT38rG797Kk7`</summary>

```text
Web search results for query: ""multi-pivot" instruction tuning typological distance source language weighting arxiv 2025"

Links: [{"title":"[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/abs/2311.08711"},{"title":"On the Effect of Instruction Tuning Loss on Generalization","url":"https://arxiv.org/html/2507.07817"},{"title":"Instruction-Tuning Open-Weight Language Models for BPMN Model Generation","url":"https://arxiv.org/html/2512.12063v1"},{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090v2"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854"},{"title":"On the Effect of Instruction Tuning Loss on Generalization | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.42/133798/On-the-Effect-of-Instruction-Tuning-Loss-on"},{"title":"[2512.12063] Instruction-Tuning Open-Weight Language Models for BPMN Model Generation","url":"https://arxiv.org/abs/2512.12063"},{"title":"Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages","url":"https://arxiv.org/html/2308.12038v3"},{"title":"Investigating Multi-Pivot Ensembling with Massively Multilingual Machine Translation Models","url":"https://arxiv.org/html/2311.07439v3"},{"title":"[2311.07439] Investigating Multi-Pivot Ensembling with Massively Multilingual Machine Translation Models","url":"https://arxiv.org/abs/2311.07439"}]

Based on the search results, I found several papers related to multi-pivot approaches and instruction tuning, though the specific combination of all your search terms doesn't appear to have an exact match. Here are the most relevant results:

**Related Work on Pivot Languages and Instruction Tuning:**

1. **PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning** - This approach utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages by training the model to first process instructions in the pivot language, and then produce responses in the target language.

2. **Multilingual Instruction Tuning Research** - Research investigates how multilinguality during instruction tuning affects general-purpose instruction-following across languages, including questions about monolingual instruction tuning transfer to other languages and the effects of increasing the number of languages on cross-lingual transfer.

3. **Multi-Pivot Ensembling in Machine Translation** - Massively multilingual machine translation models have limited performance on low- and very-low-resource translation directions, and pivoting via high-resource languages remains a strong strategy for low-resource directions.

4. **Language Diversity in Fine-Tuning** - Research addresses typological distance as a factor in multilingual fine-tuning, though with only partial explanations for observed variations.

The exact paper combining "multi-pivot," "typological distance," and "source language weighting" specifically doesn't appear in these results. You may want to try a more specific search or check the arXiv directly for 2025 papers matching this exact combination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b64d6576-078c-4dd9-a246-48123263cfac",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "8aa94d6f-0c24-4c5d-a5a0-49765eae2896",
  "sourceToolAssistantUUID": "b64d6576-078c-4dd9-a246-48123263cfac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-10T07:27:01.738Z_

Let me now check a few more items: the TMLR paper, the Code-Switching Curriculum paper via its ACL Anthology link, and dig deeper into any EMNLP 2026 submissions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8aa94d6f-0c24-4c5d-a5a0-49765eae2896",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVV3Rc7gKJqwefWGSQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa6ac051-f989-43df-b6ea-136ca9c7e5d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UixByuNba3eniB7dmNYDkD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 195,
      "cache_creation_input_tokens": 3985,
      "cache_read_input_tokens": 31308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3985,
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

_source line 71 · 2026-05-10T07:27:03.606Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SKyBZTfo5smY5paBouNCS1`</summary>

```json
{
  "url": "https://openreview.net/forum?id=oapsbIO1Bd",
  "prompt": "Extract full title, authors, abstract, venue (TMLR? EMNLP?), and key claims about multilingual instruction tuning or data weighting."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa6ac051-f989-43df-b6ea-136ca9c7e5d8",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVV3Rc7gKJqwefWGSQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6635d8a3-f8f7-4106-9ab9-35758e544a42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UixByuNba3eniB7dmNYDkD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 195,
      "cache_creation_input_tokens": 3985,
      "cache_read_input_tokens": 31308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3985,
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

_source line 72 · 2026-05-10T07:27:04.334Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EuukWiSQgCFQysEqgTYkvR`</summary>

```json
{
  "query": "\"Code-Switching Curriculum Learning\" multilingual LLM ACL 2025 Findings cross-lingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6635d8a3-f8f7-4106-9ab9-35758e544a42",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVV3Rc7gKJqwefWGSQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6628ae26-353c-4c22-9098-f98aeb3de8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UixByuNba3eniB7dmNYDkD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 195,
      "cache_creation_input_tokens": 3985,
      "cache_read_input_tokens": 31308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3985,
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

_source line 73 · 2026-05-10T07:27:05.178Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HgEvsqeCZAZVd73bgxnduc`</summary>

```json
{
  "query": "EMNLP 2026 accepted papers cross-lingual multilingual instruction tuning openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6628ae26-353c-4c22-9098-f98aeb3de8ac",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVV3Rc7gKJqwefWGSQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23046f37-b61b-44e5-bdec-fe1be5b8a992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UixByuNba3eniB7dmNYDkD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 195,
      "cache_creation_input_tokens": 3985,
      "cache_read_input_tokens": 31308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3985,
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

_source line 74 · 2026-05-10T07:27:06.034Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DjAw6DmAvXet34DmDVHEZx`</summary>

```json
{
  "query": "\"Instruction Tuning on Public Government and Cultural Data\" Kazakh 2502.13647 ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23046f37-b61b-44e5-bdec-fe1be5b8a992",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVV3Rc7gKJqwefWGSQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14d8e432-7a7f-4b38-a3c4-b2a412c8b68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UixByuNba3eniB7dmNYDkD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 195,
      "cache_creation_input_tokens": 3985,
      "cache_read_input_tokens": 31308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3985,
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

_source line 75 · 2026-05-10T07:27:06.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013STG6J8jVifGqPAmFo2zyi`</summary>

```json
{
  "query": "cross-lingual instruction tuning data weighting typological proximity negative transfer 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14d8e432-7a7f-4b38-a3c4-b2a412c8b68a",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVV3Rc7gKJqwefWGSQF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6098d7a-e3f0-4e89-9767-636988a069ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UixByuNba3eniB7dmNYDkD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 195,
      "cache_creation_input_tokens": 3985,
      "cache_read_input_tokens": 31308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3985,
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

### Tool result

_source line 76 · 2026-05-10T07:27:07.223Z_

<details><summary>↩ Tool result · `toolu_01SKyBZTfo5smY5paBouNCS1`</summary>

```text
# Paper Summary: COMPASS

**Full Title:**
COMPASS: COntinual Multilingual PEFT with Adaptive Semantic Sampling

**Author:**
Noah Flynn

**Venue:**
TMLR (Transactions on Machine Learning Research)

**Publication Date:**
08 Dec 2025

**Abstract:**
The work introduces a framework for adapting large language models across multiple languages. Rather than simply fine-tuning on all available data, the approach employs "parameter-efficient fine-tuning (PEFT) by training lightweight, language-specific adapters" on carefully selected multilingual data. The method identifies which auxiliary data to use through "a distribution-aware sampling strategy that uses multilingual embeddings and clustering."

**Key Claims About Multilingual Adaptation:**

1. **Problem Addressed:** The authors identify that "naive multilingual fine-tuning frequently" causes performance issues due to negative cross-lingual interference.

2. **Core Innovation:** The sampling strategy prioritizes data from "under-represented semantic clusters" to maximize beneficial knowledge transfer while reducing harmful interference.

3. **Continual Learning Extension:** An extended version monitors production environments for "data distribution shifts" and dynamically updates language adapters to prevent model degradation.

4. **Empirical Results:** Testing across three model architectures demonstrates the approach "consistently outperforms baseline methods guided by linguistic similarity."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6635d8a3-f8f7-4106-9ab9-35758e544a42",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "6e3f88cb-f3ac-48a2-b84f-538c94519b9f",
  "sourceToolAssistantUUID": "6635d8a3-f8f7-4106-9ab9-35758e544a42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-10T07:27:09.695Z_

<details><summary>↩ Tool result · `toolu_01EuukWiSQgCFQysEqgTYkvR`</summary>

```text
Web search results for query: ""Code-Switching Curriculum Learning" multilingual LLM ACL 2025 Findings cross-lingual"

Links: [{"title":"Code-Switching Curriculum Learning for Multilingual Transfer in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.407/"},{"title":"Code-Switching Curriculum Learning for Multilingual ...","url":"https://aclanthology.org/2025.findings-acl.407.pdf"},{"title":"[2411.02460] Code-Switching Curriculum Learning for Multilingual Transfer in LLMs","url":"https://arxiv.org/abs/2411.02460"},{"title":"Robust Generalization, Rigorous Evaluation, and Impactful ...","url":"https://haneul-yoo.github.io/rs/"},{"title":"OLA: Output Language Alignment in Code-Switched LLM Interactions Juhyun Oh","url":"https://arxiv.org/pdf/2601.03589"},{"title":"Investigating and Scaling up Code-Switching for ...","url":"https://aclanthology.org/2025.findings-acl.575.pdf"},{"title":"Code Switching for/with Multilingual LLMs","url":"http://web.stanford.edu/class/cs329x/slides/Lecture12_B_Codeswitching%20LLMs.pdf"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Code-Switching Red-Teaming: LLM Evaluation for Safety ...","url":"https://aclanthology.org/2025.acl-long.657.pdf"},{"title":"[Quick Review] Code-Switching Curriculum Learning for Multilingual Transfer in LLMs","url":"https://liner.com/review/codeswitching-curriculum-learning-for-multilingual-transfer-in-llms"}]

Based on the web search results, here's what I found about Code-Switching Curriculum Learning for multilingual LLMs at ACL 2025:

## Overview

The paper "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs" was authored by Haneul Yoo, Cheonbok Park, Sangdoo Yun, Alice Oh, and Hwaran Lee, and appears in Findings of the Association for Computational Linguistics: ACL 2025.

## Key Approach

Inspired by human second language acquisition, the paper proposes code-switching curriculum learning (CSCL) to enhance cross-lingual transfer for LLMs. CSCL mimics the stages of human language learning by progressively training models with a curriculum consisting of 1) token-level code-switching, 2) sentence-level code-switching, and 3) monolingual corpora.

## Main Findings

Ablation studies reveal that both token- and sentence-level code-switching significantly enhance cross-lingual transfer and that curriculum learning amplifies these effects. The findings extend to various languages, including Japanese (high-resource) and Indonesian (low-resource), and using two additional models (Gemma 2 and Phi 3.5).

## Impact and Benefits

CSCL mitigates spurious correlations between language resources and safety alignment, presenting a robust, efficient framework for more equitable language transfer in LLMs. CSCL is effective for low-resource settings where high-quality, monolingual corpora for language transfer are hardly available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6628ae26-353c-4c22-9098-f98aeb3de8ac",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "b66faefb-8bbf-433a-ac4c-05333ffa6ec0",
  "sourceToolAssistantUUID": "6628ae26-353c-4c22-9098-f98aeb3de8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-10T07:27:10.145Z_

<details><summary>↩ Tool result · `toolu_01HgEvsqeCZAZVd73bgxnduc`</summary>

```text
Web search results for query: "EMNLP 2026 accepted papers cross-lingual multilingual instruction tuning openreview"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"4TH MULTILINGUAL REPRESENTATION LEARNING (MRL) WORKSHOP @EMNLP 2024","url":"https://sigtyp.github.io/ws2024-mrl.html"},{"title":"Area Keywords at ARR","url":"http://aclrollingreview.org/areas"},{"title":"EMNLP.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2025"},{"title":"EMNLP 2023 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2023%2FConference"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"CoNLL 2026 | CoNLL","url":"https://conll.org/"},{"title":"Accepted Papers – EMNLP 2020","url":"https://2020.emnlp.org/papers/main/"},{"title":"EMNLP 2025 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2025%2FConference"}]

Based on the web search results, I found that EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. 

However, the search results do not contain specific information about accepted papers for EMNLP 2026 with a focus on cross-lingual multilingual instruction tuning. The results show references to the call for papers and the OpenReview submission system, but actual lists of accepted papers for EMNLP 2026 are not available in these results.

This is likely because EMNLP 2026 is still in the submission/review phase (based on the March 1, 2026 call for papers date in the results), and the final list of accepted papers may not yet be publicly available on OpenReview. You may want to:

1. Check the official EMNLP 2026 website (2026.emnlp.org) directly
2. Visit the OpenReview page for EMNLP 2026 once the conference decisions are finalized
3. Check back closer to the conference date when accepted papers are typically announced


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23046f37-b61b-44e5-bdec-fe1be5b8a992",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "7e8b6649-efaa-467f-bf09-22b8e2eaee61",
  "sourceToolAssistantUUID": "23046f37-b61b-44e5-bdec-fe1be5b8a992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-10T07:27:14.284Z_

<details><summary>↩ Tool result · `toolu_01DjAw6DmAvXet34DmDVHEZx`</summary>

```text
Web search results for query: ""Instruction Tuning on Public Government and Cultural Data" Kazakh 2502.13647 ACL 2025"

Links: [{"title":"[2502.13647] Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh","url":"https://arxiv.org/abs/2502.13647"},{"title":"Instruction Tuning on Public Government and Cultural Data ...","url":"https://arxiv.org/pdf/2502.13647"},{"title":"Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.706/"},{"title":"Instruction Tuning on Public Government and Cultural Data ...","url":"https://aclanthology.org/2025.acl-long.706.pdf"},{"title":"Search | arXiv e-print repository","url":"https://arxiv.org/search/cs?searchtype=author&query=Orel,+D"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh ...","url":"https://arxiv.org/pdf/2503.01493"},{"title":"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.701/"},{"title":"Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts","url":"https://aclanthology.org/2025.findings-acl.507.pdf"},{"title":"KazBench-KK: A Cultural-Knowledge Benchmark for Kazakh - ACL Anthology","url":"https://aclanthology.org/2025.fieldmatters-1.4/"},{"title":"Full article: Inclusive practices in Kazakhstan: validating the teacher efficacy for inclusive practice scale for the local context","url":"https://www.tandfonline.com/doi/full/10.1080/20473869.2025.2492091"}]

Based on the search results, I found the paper you're looking for:

## "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh"

This paper was authored by Nurkhan Laiyk, Daniil Orel, Rituraj Joshi, Maiya Goloburda, Yuxia Wang, Preslav Nakov, and Fajri Koto, and was published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in July 2025 in Vienna, Austria.

### Key Contributions:

The paper addresses instruction tuning in low-resource languages, which remains underexplored due to limited text data, particularly in government and cultural domains. To address this, the authors introduce and open-source a large-scale (10,600 samples) instruction-following (IFT) dataset, covering key institutional and cultural knowledge relevant to Kazakhstan.

The dataset enhances LLMs' understanding of procedural, legal, and structural governance topics. The authors employ LLM-assisted data generation, comparing open-weight and closed-weight models for dataset construction, and select GPT-4o as the backbone.

### Results:

Fine-tuning Qwen, Falcon, and Gemma on their dataset leads to consistent performance improvements in both multiple-choice and generative tasks, demonstrating the potential of LLM-assisted instruction tuning for low-resource languages.

The paper is available at arXiv (2502.13647) and on the ACL Anthology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14d8e432-7a7f-4b38-a3c4-b2a412c8b68a",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "8533196c-3c21-4eaa-a5c1-f35798283963",
  "sourceToolAssistantUUID": "14d8e432-7a7f-4b38-a3c4-b2a412c8b68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-10T07:27:17.649Z_

<details><summary>↩ Tool result · `toolu_013STG6J8jVifGqPAmFo2zyi`</summary>

```text
Web search results for query: "cross-lingual instruction tuning data weighting typological proximity negative transfer 2025 arxiv"

Links: [{"title":"Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages for Cross-Lingual POS Tagging","url":"https://arxiv.org/html/2503.19979"},{"title":"Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models","url":"https://arxiv.org/html/2410.01335v1"},{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090"},{"title":"Cross-Lingual Stability and Bias in Instruction-Tuned Language","url":"https://arxiv.org/pdf/2510.22823"},{"title":"Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"},{"title":"[2505.13908] Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology","url":"https://arxiv.org/abs/2505.13908"},{"title":"xCoT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2401.07037v1"},{"title":"Zero-shot cross-lingual transfer in instruction tuning of large language models","url":"https://arxiv.org/html/2402.14778v2"},{"title":"[2505.14297] Cross-Lingual Optimization for Language Transfer in Large Language Models","url":"https://arxiv.org/abs/2505.14297"},{"title":"[2404.11932] CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment","url":"https://arxiv.org/abs/2404.11932"}]

Based on the web search results, here are the most relevant papers from arXiv that relate to your query on cross-lingual instruction tuning, data weighting, typological proximity, and negative transfer in 2025:

## Most Directly Relevant Papers:

1. **Cross-Lingual Optimization for Language Transfer in Large Language Models** (2505.14297)
   - Proposes Cross-Lingual Optimization (CLO) that efficiently transfers an English-centric LLM to a target language while preserving its English capabilities, utilizing publicly available English SFT data and a translation model to enable cross-lingual transfer.

2. **The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation** (2505.13090)
   - Presents conflicting evidence on multilingual fine-tuning strategies, with some studies showing that scaling the number of tasks or languages during instruction tuning improves cross-lingual generalization, while others report that just 1–3 fine-tuning languages effectively trigger cross-lingual transfer.

3. **CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment** (2404.11932)
   - Proposes CrossIn, which utilizes a mixed composition of cross-lingual instruction tuning data, leveraging the compressed representation shared by various languages to efficiently enhance the model's task-solving capabilities and multilingual proficiency within a single process.

4. **Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology** (2505.13908)
   - A recent 2025 arXiv paper addressing the relationship between language typology and cross-lingual transfer.

5. **Cross-Lingual Stability and Bias in Instruction-Tuned Language Models** (2510.22823)
   - Shows that alignment, not scale, determines stability: aligned models maintain near-invariant accuracy and balanced calibration across typologically distant and low-resource languages.

The search results reveal active research on balancing negative transfer effects through data weighting strategies and understanding typological proximity effects in multilingual instruction tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6098d7a-e3f0-4e89-9767-636988a069ee",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "38b26d06-9b9d-4d62-8c76-bf954a350e62",
  "sourceToolAssistantUUID": "a6098d7a-e3f0-4e89-9767-636988a069ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-10T07:27:20.485Z_

Let me check a few more papers that look directly competitive or relevant, particularly the COMPASS paper and the new typological transfer paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38b26d06-9b9d-4d62-8c76-bf954a350e62",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVWbcPif5HxFVLS1mLy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4d58c20-8f2d-492b-bf4b-38523f1f16ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015jwKb3v6KEuRvYB3fbcLxE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4629,
      "cache_read_input_tokens": 35293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4629,
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

_source line 82 · 2026-05-10T07:27:22.638Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G3L8G2ZAgGqFunJxAqcn1P`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.19979",
  "prompt": "Extract full title, authors, abstract, and venue. Does this paper address typological distance for selecting source/transfer languages? What are the main findings about typology vs. data quantity vs. model architecture?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4d58c20-8f2d-492b-bf4b-38523f1f16ac",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVWbcPif5HxFVLS1mLy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d593f286-dee3-4ef1-b938-0ae22babebc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015jwKb3v6KEuRvYB3fbcLxE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4629,
      "cache_read_input_tokens": 35293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4629,
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

_source line 83 · 2026-05-10T07:27:23.471Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EACJnPKWUThbvtpeYZwKPj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.13908",
  "prompt": "Extract full title, authors, abstract, venue, and key findings. Does this paper challenge or support the use of typological distance for cross-lingual transfer in NLP?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d593f286-dee3-4ef1-b938-0ae22babebc5",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVWbcPif5HxFVLS1mLy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ac62d50-4569-4190-b478-a0d4976911e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015jwKb3v6KEuRvYB3fbcLxE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4629,
      "cache_read_input_tokens": 35293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4629,
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

_source line 84 · 2026-05-10T07:27:24.779Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PzLBrZdHUKg2zxs4x6HWxV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.02460",
  "prompt": "Extract full title, authors, abstract, and venue. What is the core curriculum learning method and how does it compare to typological-distance-based approaches for cross-lingual transfer?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ac62d50-4569-4190-b478-a0d4976911e5",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVWbcPif5HxFVLS1mLy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74b9230f-2d83-4c4c-b56e-85ae22f3f422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015jwKb3v6KEuRvYB3fbcLxE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4629,
      "cache_read_input_tokens": 35293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4629,
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

_source line 85 · 2026-05-10T07:27:26.246Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012dr4PRGLkTgChaYJuJdyTL`</summary>

```json
{
  "query": "COMPASS continual multilingual PEFT adaptive semantic sampling TMLR 2025 cross-lingual negative interference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74b9230f-2d83-4c4c-b56e-85ae22f3f422",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVWbcPif5HxFVLS1mLy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72a72806-676a-45c4-9abd-981ed4e1bc60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015jwKb3v6KEuRvYB3fbcLxE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4629,
      "cache_read_input_tokens": 35293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4629,
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

_source line 86 · 2026-05-10T07:27:26.419Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EtzDsbCU5M17FgowCj1giK`</summary>

```json
{
  "query": "arxiv 2026 multilingual instruction tuning pivot languages low-resource Turkic agglutinative"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72a72806-676a-45c4-9abd-981ed4e1bc60",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVWbcPif5HxFVLS1mLy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed701eca-a833-4d8c-8e45-ddc99d699e96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015jwKb3v6KEuRvYB3fbcLxE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4629,
      "cache_read_input_tokens": 35293,
      "output_tokens": 474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4629
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 474,
          "cache_read_input_tokens": 35293,
          "cache_creation_input_tokens": 4629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4629,
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

_source line 87 · 2026-05-10T07:27:27.675Z_

<details><summary>↩ Tool result · `toolu_01EACJnPKWUThbvtpeYZwKPj`</summary>

```text
# Paper Analysis

**Full Title:** Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology

**Authors:** Ajitesh Bankula, Praney Bankula

**Venue:** arXiv (cs.CL - Computation and Language), submitted May 20, 2025

**Abstract Summary:** The paper examines how language family proximity and morphological similarity influence transfer learning performance across NLP tasks. It evaluates massively multilingual models like mBERT and XLM-R, analyzing how linguistic distance metrics correlate with transfer outcomes.

## Regarding Typological Distance and Cross-Lingual Transfer

**The paper appears to SUPPORT the use of typological distance metrics.**

The abstract explicitly states the research "investigates cross-linguistic transfer through the lens of language families and morphology" and examines "how linguistic distance metrics correlate with transfer outcomes." Additionally, the authors discuss "emerging approaches that integrate typological and morphological information into model pre-training to improve transfer to diverse languages," suggesting these linguistic features are beneficial factors.

However, based on the abstract alone, specific empirical findings supporting or challenging this approach are not detailed. The full paper would be necessary to determine the strength and nature of their conclusions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ac62d50-4569-4190-b478-a0d4976911e5",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "e4fd710e-1acc-40e1-9ce9-729025ac177c",
  "sourceToolAssistantUUID": "0ac62d50-4569-4190-b478-a0d4976911e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-10T07:27:31.975Z_

<details><summary>↩ Tool result · `toolu_01PzLBrZdHUKg2zxs4x6HWxV`</summary>

```text
# Paper Summary

**Full Title:** Code-Switching Curriculum Learning for Multilingual Transfer in LLMs

**Authors:** Haneul Yoo, Cheonbok Park, Sangdoo Yun, Alice Oh, Hwaran Lee

**Venue:** Findings of ACL 2025

**Abstract:**
The paper proposes a three-stage curriculum for improving multilingual capabilities in large language models. The authors draw inspiration from "the human process of second language acquisition, particularly code-switching" and develop a training approach with progressive phases: token-level code-switching, sentence-level code-switching, and monolingual corpora training.

## Core Method vs. Typological Approaches

**Core Curriculum Learning Method:**
The CSCL approach uses staged training mimicking language acquisition progression, moving from mixed token-level data through sentence-level mixing to pure monolingual content. Testing on Qwen 2, Gemma 2, and Phi 3.5 demonstrates effectiveness across languages.

**Regarding Typological-Distance-Based Approaches:**
The provided content does not discuss typological-distance-based methods or comparative analysis with such approaches. The paper focuses on curriculum structure rather than linguistic similarity metrics for cross-lingual transfer selection.

The research emphasizes CSCL's particular value for "low-resource settings where high-quality, monolingual corpora for language transfer are hardly available."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74b9230f-2d83-4c4c-b56e-85ae22f3f422",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "1ab6e9c1-921b-4f38-9e4b-ca5f33500836",
  "sourceToolAssistantUUID": "74b9230f-2d83-4c4c-b56e-85ae22f3f422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-10T07:27:32.245Z_

<details><summary>↩ Tool result · `toolu_01G3L8G2ZAgGqFunJxAqcn1P`</summary>

```text
# Paper Summary

**Full Title:** Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages for Cross-Lingual POS Tagging

**Authors:** Enora Rice, Ali Marashian, Hannah Haynie, Katharina von der Wense, Alexis Palmer

**Venue:** NAACL 2025 Workshop Language Models for Underserved Communities

**Abstract:** The authors investigate how linguistic typology, training data, and model design collectively influence the selection of source languages for cross-lingual part-of-speech tagging. They evaluate both traditional biLSTM models and modern zero-shot approaches with pretrained multilingual models, using morphosyntactic features from two different sources.

## Does it Address Typological Distance?

Yes. The paper explicitly examines "how both dataset-specific and fine-grained typological features influence transfer language selection." Genealogical distance emerges as one of the top predictive features.

## Main Findings

The research reveals that **combining typological and dataset-dependent features produces optimal rankings**. Notably, the authors find that "good performance can be obtained with either feature group on its own," suggesting both factors independently contribute meaningfully. Key predictive features include word overlap, type-token ratio, and genealogical distance—factors that span both linguistic similarity and data characteristics across different model architectures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d593f286-dee3-4ef1-b938-0ae22babebc5",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "d5b9aaee-2588-4cfa-bc12-7b5f386750e8",
  "sourceToolAssistantUUID": "d593f286-dee3-4ef1-b938-0ae22babebc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-10T07:27:33.326Z_

<details><summary>↩ Tool result · `toolu_01EtzDsbCU5M17FgowCj1giK`</summary>

```text
Web search results for query: "arxiv 2026 multilingual instruction tuning pivot languages low-resource Turkic agglutinative"

Links: [{"title":"Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/html/2604.06202"},{"title":"Multilingual end-to-end ASR for low-resource Turkic languages with common alphabets | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-64848-1"},{"title":"[2604.06202] Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/abs/2604.06202"},{"title":"Building a Turkish Large Language Model via Continual Pre-Training and Parameter-Efficient Adaptation - ACL Anthology","url":"https://aclanthology.org/2026.sigturk-1.17/"},{"title":"TurkicNLP: An NLP Toolkit for Turkic Languages","url":"https://arxiv.org/html/2602.19174v4"},{"title":"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models","url":"https://arxiv.org/html/2603.21036v1"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"\\approachnameshort: High-Quality Instruction Tuning Datasets for Low-Resource Languages via Reverse Instructions","url":"https://arxiv.org/html/2409.12958v1"},{"title":"BayLing 2: A Multilingual Large Language Model with Efficient Language Alignment","url":"https://arxiv.org/html/2411.16300"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854v4"}]

The search results contain several relevant papers from 2026 and 2024-2025 related to multilingual instruction tuning, low-resource languages, Turkic languages, and agglutinative morphology. Here are the key findings:

## Recent Research on Turkic Languages and Multilingual Instruction Tuning

**Cross-Lingual Transfer in Turkic Languages:**
A 2026 arXiv paper proposes a theoretical framework for studying cross-lingual transfer and parameter-efficient adaptation within the Turkic language family, focusing on Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz, which share substantial typological and morphological similarity while differing greatly in available digital resources.

**Agglutinative Morphology Challenges:**
A defining feature of Turkic languages is their agglutinative morphology, in which grammatical relationships are expressed through sequences of suffixes attached to lexical stems, encoding tense, case, possession, evidentiality, and other grammatical categories within a single orthographic word.

**Pivot Language Strategies:**
Research has suggested instruction tuning LLMs by prepending the instruction and response translated into a pivot language (e.g., English) to the response in the target language. Additionally, one approach designates Chinese and English as pivot languages and applies cross-lingual tasks to align 100+ languages to these pivot languages, facilitating capabilities transfer from high-resource to low-resource languages.

**Instruction Datasets for Low-Resource Languages:**
A dataset called MURI-IT contains more than 2 million instruction-output pairs across 200 languages, offering the broadest language coverage for multilingual instruction tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed701eca-a833-4d8c-8e45-ddc99d699e96",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "71e0f6de-6848-47ce-b2ca-901a68c17265",
  "sourceToolAssistantUUID": "ed701eca-a833-4d8c-8e45-ddc99d699e96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-10T07:27:43.560Z_

<details><summary>↩ Tool result · `toolu_012dr4PRGLkTgChaYJuJdyTL`</summary>

```text
Web search results for query: "COMPASS continual multilingual PEFT adaptive semantic sampling TMLR 2025 cross-lingual negative interference"

Links: [{"title":"COMPASS: COntinual Multilingual PEFT with Adaptive Semantic Sampling","url":"https://arxiv.org/html/2604.20720"},{"title":"[2604.20720] COMPASS: COntinual Multilingual PEFT with Adaptive Semantic Sampling","url":"https://arxiv.org/abs/2604.20720"},{"title":"COMPASS: COntinual Multilingual PEFT with Adaptive Se","url":"https://openreview.net/pdf?id=oapsbIO1Bd"},{"title":"Paper page - COMPASS: COntinual Multilingual PEFT with Adaptive Semantic Sampling","url":"https://huggingface.co/papers/2604.20720"},{"title":"Towards Better Instruction Following Language Models for Chinese: Investigating the Impact of Training Data and Evaluation","url":"https://www.researchgate.net/publication/370071243_Towards_Better_Instruction_Following_Language_Models_for_Chinese_Investigating_the_Impact_of_Training_Data_and_Evaluation"},{"title":"Continual-learning for Modelling Low-Resource Languages from Large Language Models","url":"https://arxiv.org/html/2601.05874"},{"title":"GitHub - Wang-ML-Lab/llm-continual-learning-survey: [CSUR 2025] Continual Learning of Large Language Models: A Comprehensive Survey · GitHub","url":"https://github.com/Wang-ML-Lab/llm-continual-learning-survey"},{"title":"Scaling Multilingual LLMs with Multi-Way Parallel Corpora","url":"https://aclanthology.org/2025.emnlp-main.374.pdf"},{"title":"A survey of multilingual large language models - PMC - NIH","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11783891/"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"}]

I found comprehensive information about the COMPASS paper. Here are the search results:

## COMPASS: COntinual Multilingual PEFT with Adaptive Semantic Sampling

Large language models (LLMs) often exhibit performance disparities across languages, with naive multilingual fine-tuning frequently degrading performance due to negative cross-lingual interference.

COMPASS (COntinual Multilingual PEFT with Adaptive Semantic Sampling) is a novel data-centric framework for adapting LLMs to target languages that leverages parameter-efficient fine-tuning (PEFT) by training lightweight, language-specific adapters on a judiciously selected subset of auxiliary multilingual data.

### Core Methodology

The core of the method is a distribution-aware sampling strategy that uses multilingual embeddings and clustering to identify semantic gaps between existing training data and a target usage distribution. By prioritizing auxiliary data from under-represented semantic clusters, COMPASS maximizes positive cross-lingual transfer while minimizing interference.

### Key Features

The method clusters the data into semantic groups, which are used to compute cluster-level and instance-level importance weights that guide the stochastic sampling of auxiliary data to address distributional gaps, and lightweight, language-specific adapters are fine-tuned and deployed, with an identification model routing incoming queries.

The paper addresses a critical challenge in multilingual LLM adaptation by providing a data-centric solution that avoids the performance degradation that occurs with naive multilingual fine-tuning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72a72806-676a-45c4-9abd-981ed4e1bc60",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "5b9000a1-40ef-420d-b15c-a226a074c847",
  "sourceToolAssistantUUID": "72a72806-676a-45c4-9abd-981ed4e1bc60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-10T07:27:46.801Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KwcnKMLCsnUFjUf9cvW3rn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.06202",
  "prompt": "Extract full title, authors, abstract, submission date, and key claims. Is this a theoretical paper or empirical? Does it address cross-lingual transfer with typological similarity for Turkic languages (Kazakh, Uyghur, Mongolian)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b9000a1-40ef-420d-b15c-a226a074c847",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVYWDW9bm7n2SN4jGvN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bd5b530-f335-4fb9-ac20-e3c483ddd050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RQPHUdy3sn6LUgpx8gB8Ag",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 939,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 39922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2373,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-10T07:27:48.492Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MwLBTisTfy9WBxnHnvdwQU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.21036",
  "prompt": "Extract full title, authors, abstract, submission date, and venue. Does it address using pivot/source languages for cross-lingual transfer to low-resource languages? What are its main claims about which languages to use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bd5b530-f335-4fb9-ac20-e3c483ddd050",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVYWDW9bm7n2SN4jGvN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "514abdb1-01ac-464a-982e-b2a2c003075f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RQPHUdy3sn6LUgpx8gB8Ag",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 939,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 39922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2373,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-10T07:27:49.788Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017fhTWDnmq4dvaz1NLC4cQF`</summary>

```json
{
  "query": "\"multi-source\" OR \"multiple source languages\" instruction tuning low-resource 2025 2026 arxiv typological"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "514abdb1-01ac-464a-982e-b2a2c003075f",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVYWDW9bm7n2SN4jGvN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9fee924-19a5-4909-87ab-244b797de93f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RQPHUdy3sn6LUgpx8gB8Ag",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 939,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 39922,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2373
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 939,
          "output_tokens": 310,
          "cache_read_input_tokens": 39922,
          "cache_creation_input_tokens": 2373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2373,
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

_source line 95 · 2026-05-10T07:27:51.597Z_

<details><summary>↩ Tool result · `toolu_01KwcnKMLCsnUFjUf9cvW3rn`</summary>

```text
# Paper Summary

**Full Title:** Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models

**Authors:** O. Ibrahimzade, K. Tabasaransky

**Submission Date:** March 13, 2026

**Paper Type:** Theoretical framework (explicitly stated as such)

## Abstract Summary

The authors propose a conceptual framework examining how multilingual models can be adapted to underrepresented Turkic languages. They focus on five languages: Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz. The work integrates parameter-efficient fine-tuning methods, particularly Low-Rank Adaptation, with insights about multilingual representation learning.

## Key Claims

1. The framework introduces the "Turkic Transfer Coefficient (TTC)," a theoretical measure incorporating morphological similarity, lexical overlap, syntactic structure, and script compatibility.

2. "Typological similarity can enable efficient multilingual transfer while also identifying structural limits of parameter-efficient adaptation in extremely low-resource scenarios."

3. The research demonstrates how model capacity, adaptation data size, and adaptation module expressivity interact to determine performance outcomes.

## Does It Address Your Specific Question?

**Partially.** The paper examines Kazakh and other Turkic languages but does **not** include Uyghur or Mongolian. It focuses exclusively on five Turkic language family members and their typological relationships.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bd5b530-f335-4fb9-ac20-e3c483ddd050",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "23d65850-5a9e-4084-8fc2-f541f5a4c2c5",
  "sourceToolAssistantUUID": "7bd5b530-f335-4fb9-ac20-e3c483ddd050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-10T07:27:53.053Z_

<details><summary>↩ Tool result · `toolu_01MwLBTisTfy9WBxnHnvdwQU`</summary>

```text
# Paper Summary

**Full Title:** "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models"

**Author:** Abdul-Salem Beibitkhan

**Submission Date:** March 22, 2026

**Venue:** arXiv (cs.CL - Computation and Language)

## Does it address pivot/source languages for cross-lingual transfer?

Yes, the paper examines cross-lingual transfer strategies. Specifically, it investigates "cross-lingual transfer-prompting models to reason in English before translating back."

## Main Claims About Language Selection

The study's key finding regarding which languages to use is nuanced:

1. **English as an intermediary:** The research tested having models reason in English (a high-resource language) as an intermediate step before translating responses back to low-resource languages.

2. **Architecture-dependent effectiveness:** Results show this approach yields "selective gains for bilingual architectures (+2.2pp to +4.3pp) but provides no benefit to English-dominant models."

3. **Universal solutions don't exist:** The authors conclude that "effective mitigation strategies are architecture-dependent rather than universal," meaning no single language choice works optimally across all LLM types.

The paper demonstrates that the choice of pivot language and its effectiveness depends critically on the underlying model architecture rather than being universally beneficial.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "514abdb1-01ac-464a-982e-b2a2c003075f",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "5c3019dd-4f36-45e6-856b-c8931f01448b",
  "sourceToolAssistantUUID": "514abdb1-01ac-464a-982e-b2a2c003075f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-10T07:27:57.804Z_

<details><summary>↩ Tool result · `toolu_017fhTWDnmq4dvaz1NLC4cQF`</summary>

```text
Web search results for query: ""multi-source" OR "multiple source languages" instruction tuning low-resource 2025 2026 arxiv typological"

Links: [{"title":"Efficient Low-Resource Language Adaptation via Multi- ...","url":"https://arxiv.org/pdf/2604.18106"},{"title":"\\approachnameshort: High-Quality Instruction Tuning Datasets for Low-Resource Languages via Reverse Instructions","url":"https://arxiv.org/html/2409.12958v1"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809v1"},{"title":"Analysis of Multi-Source Language Training in Cross-Lingual Transfer","url":"https://arxiv.org/html/2402.13562v2"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"Zero-shot Cross-lingual Transfer Learning with Multiple Source and Target Languages for Information Extraction: Language Selection and Adversarial Training","url":"https://arxiv.org/html/2411.08785"},{"title":"LinguaLIFT: An Effective Two-stage Instruction Tuning Framework for Low-Resource Language Tasks","url":"https://arxiv.org/html/2412.12499v1"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854v1"},{"title":"[2401.01854] Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/abs/2401.01854"}]

I've found several relevant research papers on arXiv related to your query. Here are some key findings:

## Multi-Source Language Training and Instruction Tuning

Research shows that increasing the diversity of source languages in cross-lingual transfer can boost performance, with studies suggesting that pairing sentences written in different languages is beneficial for improving performance on cross-lingual tasks. Recent work by Kew et al. (2023) and Shaham et al. (2024) reveals that multi-source language training is also advantageous for instruction-tuned language models.

## Low-Resource Languages and Instruction Tuning

Instruction tuning enhances large language models by aligning them with human preferences across diverse tasks, but traditional approaches face serious challenges for low-resource languages due to their dependence on data annotation. A performance gap persists between high-resource and low-resource language tasks due to language imbalance, and frameworks like LinguaLIFT have been proposed to advance low-resource language tasks.

## Typological Approaches

Research hypothesizes that optimum language subset selection for multilingual instruction tuning can be achieved in a linguistically informed manner. Linguistically informed selection techniques range from common methods such as typological feature vectors to less conventional approaches, including language embeddings derived from semantic typology features.

Research demonstrates that distances based on linguistic features, including phylogenetic and typological properties, between two languages, are correlated with cross-lingual transfer capacity.

## Recent 2025-2026 Work

Recent advances explore early competition between languages with differing orthographic and typological properties, and demonstrate impressive performance across a wide range of non-English languages, including many that are considered low-resource.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9fee924-19a5-4909-87ab-244b797de93f",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "cff6289f-42cd-44f2-9702-d393db40d977",
  "sourceToolAssistantUUID": "c9fee924-19a5-4909-87ab-244b797de93f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-10T07:28:00.746Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D6YLZn1T7WxVZybZtFftNC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.18106",
  "prompt": "Extract full title, authors, abstract, submission date, and key claims. Does this paper address multi-source instruction tuning or data weighting for low-resource language adaptation? Does it use typological features?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cff6289f-42cd-44f2-9702-d393db40d977",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVZZAdRSShQ8BQw8Bat",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00153453-4d8c-4618-bd32-1ad56cf2dffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EDZ1XfKsUuj8LAVCB52vks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2850,
      "cache_read_input_tokens": 42295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2850,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-10T07:28:02.264Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Udnudv8xbMAWQ4iNuaRhxc`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.25947v1",
  "prompt": "Extract the full title, authors, venue, abstract, and key findings about multilingual data mixtures. Does this paper address whether typological distance or language weighting affects multilingual pretraining? What are the main conclusions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00153453-4d8c-4618-bd32-1ad56cf2dffd",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVZZAdRSShQ8BQw8Bat",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cda0895f-0800-4725-803f-05dd79e9565a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EDZ1XfKsUuj8LAVCB52vks",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2850,
      "cache_read_input_tokens": 42295,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2850
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 42295,
          "cache_creation_input_tokens": 2850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2850,
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

_source line 100 · 2026-05-10T07:28:05.691Z_

<details><summary>↩ Tool result · `toolu_01D6YLZn1T7WxVZybZtFftNC`</summary>

```text
# Paper Analysis

**Full Title:** Efficient Low-Resource Language Adaptation via Multi-Source Dynamic Logit Fusion

**Authors:** Chen Zhang, Jiuheng Lin, Zhiyuan Liao, Yansong Feng

**Submission Date:** April 20, 2026

**Abstract Summary:**
The paper proposes TriMix, a framework addressing LLM adaptation to low-resource languages. It combines "LRL competence from a continually pretrained small model, task competence from high-resource language instruction tuning" alongside large model capabilities through logit-level fusion at test time.

## Key Findings

**Multi-Source Instruction Tuning:** Yes, the approach incorporates task knowledge from high-resource language instruction tuning as one of three fusion sources, avoiding the need for low-resource language task annotations.

**Data Weighting:** The paper emphasizes dynamic balancing rather than explicit weighting schemes, "prioritizing the small LRL-specialized model's logits" as crucial for success.

**Typological Features:** The provided abstract and metadata contain no mention of typological linguistic features. The approach relies on model-based competence sources rather than linguistic typology.

**Novel Claim:** The work challenges conventional assumptions by demonstrating that "prioritizing the small LRL-specialized model's logits is crucial for success, challenging the prevalent large-model-dominant assumption."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00153453-4d8c-4618-bd32-1ad56cf2dffd",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "d714191a-ed9e-494c-9629-d86ac2786bca",
  "sourceToolAssistantUUID": "00153453-4d8c-4618-bd32-1ad56cf2dffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-10T07:28:10.061Z_

<details><summary>↩ Tool result · `toolu_01Udnudv8xbMAWQ4iNuaRhxc`</summary>

```text
# Revisiting Multilingual Data Mixtures in Language Model Pretraining

## Bibliographic Information
**Title:** Revisiting Multilingual Data Mixtures in Language Model Pretraining

**Authors:** Negar Foroutan, Paul Teiletche, Ayush Kumar Tarun, Antoine Bosselut (EPFL, Lausanne, Switzerland)

**Venue:** arXiv preprint (2510.25947v1)

## Abstract
The paper investigates how different multilingual data compositions affect large language model pretraining across 1.1B and 33B parameter models trained on up to 400 languages. The research challenges prevailing assumptions about multilingual training by demonstrating that "combining English and multilingual data does not necessarily degrade in-language performance" when sufficient tokens exist for each language group.

## Typological Distance and Language Weighting

**Does the paper address these factors?** Yes, extensively.

The research directly examines whether linguistic relatedness matters for cross-lingual transfer. Contrary to expectations, the authors found that "using English as a pivot language provides benefits across language families" and that "selecting a pivot language from within a specific family does not consistently enhance performance." This challenges the "stay in the family" assumption about typological proximity.

Regarding weighting, the paper compares natural data distribution sampling against temperature-based reweighting, finding that "under the natural distribution, performance remains stable" even when scaling from 25 to 400 languages, while temperature sampling (which artificially boosts low-resource languages) showed degradation.

## Key Findings

1. **English Integration:** Abundant English data doesn't harm multilingual capabilities if sufficient non-English tokens exist in the training mixture.

2. **Pivot Language Selection:** English serves as an effective universal pivot across language families, outperforming family-specific pivots in most scenarios.

3. **Curriculum Learning Ineffectiveness:** Staging language introduction during training "does not reduce negative interference" or improve non-English performance.

4. **Curse Reframing:** The curse of multilinguality stems from "finite model capacity and data distributions amplifying low-resource language noise," not simply from language count.

## Main Conclusions

The authors recommend prioritizing "scaling and cleaning low-resource data rather than costly data balancing operations" and argue against arbitrarily limiting language coverage, as "the curse is primarily a function of quality and quantity of the multilingual data, not language count."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cda0895f-0800-4725-803f-05dd79e9565a",
  "isSidechain": true,
  "promptId": "d16bd7a2-368a-450f-abff-4a9a76c297d6",
  "agentId": "a6a68117d153347f2",
  "type": "user",
  "uuid": "16ac7019-4dce-4853-bf38-f32e586440b2",
  "sourceToolAssistantUUID": "cda0895f-0800-4725-803f-05dd79e9565a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 102 · 2026-05-10T07:29:56.520Z_

I now have comprehensive information across all requested areas. Let me compile the full adversarial review report.

---

Here is a detailed, structured report on what was found and verified across all seven search areas.

---

## 1. Curriculum Learning for Multilingual / Cross-Lingual NLP (2025-2026)

### Code-Switching Curriculum Learning for Multilingual Transfer in LLMs
- **arXiv:** 2411.02460 | **Venue:** ACL 2025 Findings (confirmed, ACL Anthology: 2025.findings-acl.407)
- **Authors:** Haneul Yoo, Cheonbok Park, Sangdoo Yun, Alice Oh, Hwaran Lee
- **Core claim:** Proposes a 3-stage curriculum (token-level code-switching → sentence-level code-switching → monolingual), inspired by human L2 acquisition. Tested on Qwen 2, Gemma 2, Phi 3.5. Shows improved cross-lingual transfer for both high-resource (Japanese) and low-resource (Indonesian) languages.
- **Adversarial relevance:** Competes directly with any training-schedule-based or data-weighting approach for cross-lingual transfer. The curriculum is defined by *code-mixing stage*, not typological distance. Does not reference typological-distance weighting. Operates at the continual pretraining stage, not purely instruction tuning.

### Revisiting Multilingual Data Mixtures in Language Model Pretraining
- **arXiv:** 2510.25947 | **Venue:** arXiv preprint, EPFL group, October 2025
- **Authors:** Negar Foroutan et al.
- **Core claim:** Directly challenges typology-based assumptions. Finds that (a) English as pivot outperforms family-specific pivots across language families, (b) curriculum learning (staged language introduction) **does not reduce negative interference**, and (c) temperature-based reweighting to boost low-resource languages hurts performance due to noise. Recommends data cleaning and scaling over data balancing.
- **Adversarial relevance:** HIGH. This paper directly undermines both the curriculum learning and the language-weighting rationale. If you are weighting by typological distance, this paper says family-specific pivots don't beat English, and reweighting schemes fail on noisy low-resource data. This is a strong adversarial citation.

### STEP: Staged Parameter-Efficient Pre-training for Large Language Models
- **arXiv:** 2504.04151 | **Venue:** arXiv, April 2025
- Tangential — concerns staged growth of model capacity, not cross-lingual language ordering.

---

## 2. Data Selection / Weighting for Multilingual Fine-Tuning

### LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning
- **arXiv:** 2511.10229 | **Venue:** AAAI 2026 Main Track (confirmed)
- **Authors:** Yangfan Ye, Xiaocheng Feng et al. (Harbin Institute of Technology + Microsoft)
- **Core claim:** Proposes a 2-stage pre-selection framework using *language separability* (how distinguishable samples from different languages are in the model's representation space) rather than typological distance. Tested across 6 benchmarks and 22 languages. LangGPS improves on existing selection methods and generalizes especially well to low-resource languages and understanding tasks.
- **Adversarial relevance:** HIGH. This is a direct competitor: it addresses the same problem (what data to use for multilingual instruction tuning) but uses representation-space separability rather than external typological databases. Published at AAAI 2026, so it is peer-reviewed and concurrent. A reviewer could ask: "why use typological distance from URIEL/lang2vec rather than a model-internal signal like LangGPS?"

### Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?
- **arXiv:** 2410.07809 | **Venue:** arXiv (October 2024), no confirmed venue found
- **Authors:** Gürkan Soykan, Gözde Gül Şahin (Wageningen / Koç University)
- **Core claim:** Directly tests whether linguistically informed language *selection* (using typological feature vectors, semantic typology embeddings, geographic features, k-means clustering) outperforms random selection for multilingual instruction tuning. Key finding: linguistically informed selection *generally outperforms random* but there is **no universally best technique** — the optimal subset varies by model and task. Also confirms a curse of multilinguality beyond a language count threshold.
- **Adversarial relevance:** VERY HIGH. This is almost exactly the same research question as a multi-pivot typological-distance-weighted paper. It provides a baseline comparison set that any new paper must beat. Notably, they find no single technique wins universally, which weakens strong claims about typological distance as a silver bullet.

### COMPASS: COntinual Multilingual PEFT with Adaptive Semantic Sampling
- **arXiv:** 2604.20720 | **Venue:** TMLR (published December 2025, confirmed via OpenReview)
- **Author:** Noah Flynn
- **Core claim:** Uses multilingual embedding clustering and distribution-aware *semantic sampling* (not typological distance) to select auxiliary data for cross-lingual PEFT adapters. Claims to "consistently outperform baseline methods guided by linguistic similarity," implying it beats typological-similarity baselines.
- **Adversarial relevance:** HIGH. This paper explicitly claims to beat methods guided by linguistic similarity (which includes typological distance), using a semantic/embedding-based approach instead. The claim "outperforms baseline methods guided by linguistic similarity" is a direct adversarial statement against the typological weighting premise.

### The Effect of Language Diversity When Fine-Tuning LLMs for Translation
- **arXiv:** 2505.13090 | **Venue:** arXiv, May 2025
- Finds conflicting evidence — some studies show 1-3 fine-tuning languages transfer well, others show diversity helps. Not a clean competitor but raises doubt about how many source languages are needed.

### Analysis of Multi-Source Language Training in Cross-Lingual Transfer
- **arXiv:** 2402.13562 | Older paper (February 2024). Shows multi-source training helps but results are mixed by task.

### CrossIn
- **arXiv:** 2404.11932 | **Venue:** ACL Anthology 2025 (SumEval workshop)
- Proposes mixed cross-lingual instruction tuning data without explicit typological weighting.

---

## 3. Instruction Tuning for Kazakh, Mongolian, Uyghur

### Kazakh

**KazMMLU** (arXiv: 2502.12829)
- Confirmed real: ACL 2025 Main Conference, Long Papers, pp. 14403-14416. ACL Anthology: 2025.acl-long.701
- 23,000 questions, 10,969 Kazakh / 12,031 Russian, covering STEM/humanities/social sciences
- Shows substantial performance gaps for Kazakh in all tested models (Llama3.1, Qwen-2.5, GPT-4, DeepSeek V3)
- **Adversarial relevance:** Confirms the gap still exists as of ACL 2025, legitimizing motivation for instruction tuning work.

**Instruction Tuning on Public Government and Cultural Data for Kazakh** (arXiv: 2502.13647)
- Confirmed real: ACL 2025 Main Conference, Long Papers. ACL Anthology: 2025.acl-long.706
- 10,600-sample instruction dataset; fine-tuning Qwen/Falcon/Gemma improves Kazakh performance
- Shows Kazakh instruction tuning is an *active ACL 2025 track*, meaning the paper under review is entering a crowded, well-covered space.

**Sherkala-Chat / Llama-3.1-Sherkala-8B-Chat** (arXiv: 2503.01493)
- Submitted March 2025; accepted to OpenReview (TMLR candidate)
- Trained on 45.3B tokens (Kazakh/English/Russian/Turkish), 3.5M instruction examples in Kazakh
- State-of-the-art Kazakh LLM; SOTA on KazMMLU at 47.6. Demonstrates a competitive Kazakh-specific instruction-tuned model already exists.
- **Adversarial relevance:** A reviewer could ask what a multi-pivot method adds over a language-specific model like Sherkala-Chat.

**Cross-Lingual Transfer in the Turkic Language Family: A Theoretical Framework** (arXiv: 2604.06202)
- Submitted March 2026. Theoretical; proposes "Turkic Transfer Coefficient" incorporating morphological similarity, lexical overlap, syntactic structure, script compatibility. Covers Azerbaijani, Kazakh, Uzbek, Turkmen, Gagauz.
- Does NOT cover Uyghur or Mongolian.
- Adversarial relevance: Moderate — provides a theoretical framework that could make a typological-distance weighting scheme look atheoretical by comparison, or could be cited in support.

### Uyghur

**Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur**
- **Venue:** ACL Anthology 2025 (COLING 2025 main): 2025.coling-main.559
- 4-stage approach: monolingual data collection → continual pretraining → translation instruction fine-tuning → DPOSE (Direct Preference Optimization based on translation self-evolution)
- **Adversarial relevance:** Demonstrates a complete Uyghur LLM pipeline exists at COLING 2025. The gap for Uyghur is being closed independently of multi-pivot approaches.

**Do Chinese Models Speak Chinese Languages?** (arXiv: 2504.00289)
- April 2025. Shows most models fail to identify/generate Uyghur; Llama3-Instruct uniquely handles it. Confirms gap persists but also shows it's addressable via existing models.

### Mongolian

**MM-Eval: A Hierarchical Benchmark for Modern Mongolian Evaluation in LLMs** (arXiv: 2411.09492)
- November 2024. 569+677+344+250 tasks across syntax/semantics/knowledge/reasoning. All tested models (Qwen2-7B-Instruct, GLM4-9b-chat, Llama3.1-8B-Instruct, GPT-4) perform better on syntax than semantics, showing persistent gaps.

**Egune AI** — a 70B-parameter Mongolian LLM (commercial, Rest of World news article, 2025). Shows industry investment in Mongolian LLMs.

### MiLiC-Eval (covers all four target languages)
**arXiv: 2503.01150** — Confirmed real: **ACL 2025 Findings** (GitHub confirms: luciusssss/MiLiC-Eval, tagged [ACL'25 Findings])
- **Authors:** Chen Zhang, Mingxu Tao, Zhiyuan Liao, Yansong Feng (Peking University)
- 24K instances across 9 tasks for Tibetan, Uyghur, Kazakh (Arabic script), Mongolian (traditional script)
- Key findings: Current LLMs show decent Uyghur understanding, preliminary Tibetan/Kazakh understanding, but **struggle severely with Mongolian** (GPT-4o-mini barely beats random on several Mongolian tasks). Writing system complexity (70-430 tokens per sentence for minority scripts vs. 27-31 for English/Chinese) is a key barrier. Code-switching errors are especially prevalent in Kazakh and Mongolian.
- **Adversarial relevance:** This is the most directly relevant benchmark paper. It confirms the gap exists (legitimizes motivation) but also defines the baseline landscape any multi-pivot paper must beat. A reviewer will expect comparison against MiLiC-Eval results.

---

## 4. KazMMLU (arXiv: 2502.12829) — Verification

**Confirmed real and ACL 2025 Main Conference.** ACL Anthology: https://aclanthology.org/2025.acl-long.701/. Published in Vol. 1: Long Papers, pp. 14403-14416, Vienna, Austria. 23,000 questions, covers Kazakh and Russian, first MMLU-style dataset for Kazakh. 14 authors including Preslav Nakov and Fajri Koto.

---

## 5. TUMLU (arXiv: 2502.11020) — Verification

**Confirmed real and ACL 2025 Main Conference.** 38,139 questions across 8 Turkic languages (Azerbaijani, Crimean Tatar, Karakalpak, Kazakh, Kyrgyz, Tatar, Turkish, Uyghur, Uzbek) and 11 subjects. **Mongolian is NOT included.** First benchmark to include Uyghur, Karakalpak, Tatar, Crimean Tatar natively (not via machine translation). TUMLU-mini is released as a verified subset. 16 authors.

---

## 6. MiLiC-Eval (arXiv: 2503.01150) — Verification

**Confirmed real: ACL 2025 Findings.** GitHub repository explicitly tagged [ACL'25 Findings]. Covers Tibetan, Uyghur, Kazakh (Arabic script), and Mongolian (traditional script). 24K instances, 9 tasks. This is the most comprehensive evaluation framework specifically for the four minority languages of China that overlap with the target languages in any multi-pivot instruction tuning paper for this region.

---

## 7. Implicit Cross-Lingual Rewarding (arXiv: 2503.04647) — Verification

**Confirmed real: ACL 2025 Findings.** ACL Anthology: 2025.findings-acl.1088. GitHub: ZNLP/Implicit-Cross-Lingual-Rewarding, tagged [ACL 2025 Findings].
- **Method:** Derives an implicit reward model from the logits of an English DPO-aligned model, uses English instructions to annotate preference relations in multilingual instruction-following pairs, then performs multilingual DPO fine-tuning.
- **Results:** +12.72% average Win Rate improvement, +5.97% Length Control Win Rate on X-AlpacaEval, over 2 iterations fine-tuning Llama3.
- **Adversarial relevance:** This targets the *alignment* stage rather than the instruction tuning / cross-lingual transfer stage, so it's somewhat complementary to multi-pivot instruction tuning. However, it demonstrates that a principled English-to-multilingual transfer of preference knowledge works well, raising the question of whether you need multi-pivot data at all if English-pivot DPO suffices for alignment.

---

## 8. EMNLP 2026 OpenReview

The EMNLP 2026 Conference page exists on OpenReview (openreview.net/group?id=EMNLP%2F2026%2FConference) and submission infrastructure is live, but **no accepted papers are publicly listed yet** — the conference is still in review phase (call for papers issued with a March 2026 deadline). No EMNLP 2026 accepted papers on cross-lingual instruction tuning could be found. One submission visible on OpenReview that is relevant:

**"From English to Second Language Mastery: Enhancing LLMs with Cross-Lingual Continued Instruction Tuning"** (OpenReview: forum?id=dqxXAgFjra) — proposes X-CIT, a cross-lingual continued instruction tuning approach using translation-based parallel instruction data, framed via Chomsky's Principles and Parameters Theory. Venue not yet confirmed (under review). Partial adversarial relevance if accepted.

---

## Summary of Strongest Adversarial Papers

| Paper | Venue | Key Adversarial Threat |
|---|---|---|
| **Revisiting Multilingual Data Mixtures** (2510.25947) | arXiv, EPFL, Oct 2025 | Curriculum learning fails to reduce negative interference; family-specific pivots don't beat English; reweighting hurts with noisy low-resource data |
| **LangGPS** (2511.10229) | AAAI 2026 | Representation-space separability outperforms linguistic similarity for data selection |
| **COMPASS** (2604.20720) | TMLR, Dec 2025 | Explicitly claims to outperform "methods guided by linguistic similarity" using semantic clustering |
| **Linguistically-Informed MIT** (2410.07809) | arXiv, Oct 2024 | No single typological selection technique wins universally across models/tasks |
| **MiLiC-Eval** (2503.01150) | ACL 2025 Findings | Defines the benchmark landscape for the target languages; Mongolian remains near-random even for GPT-4o-mini |
| **Implicit Cross-Lingual Rewarding** (2503.04647) | ACL 2025 Findings | English-pivot DPO alone achieves strong multilingual alignment, reducing need for multi-source instruction data |
| **Code-Switching Curriculum** (2411.02460) | ACL 2025 Findings | Alternative curriculum (code-switching stages) without typological weighting achieves cross-lingual transfer |
| **KazMMLU** (2502.12829) | ACL 2025 Main | Real and confirmed; legitimizes motivation but also raises the bar for what "improvement" means |
| **TUMLU** (2502.11020) | ACL 2025 Main | Real and confirmed; covers Uyghur + Kazakh but not Mongolian |

Sources:
- [KazMMLU - ACL Anthology](https://aclanthology.org/2025.acl-long.701/)
- [KazMMLU - arXiv 2502.12829](https://arxiv.org/abs/2502.12829)
- [TUMLU - arXiv 2502.11020](https://arxiv.org/abs/2502.11020)
- [MiLiC-Eval - arXiv 2503.01150](https://arxiv.org/abs/2503.01150)
- [MiLiC-Eval - GitHub](https://github.com/luciusssss/MiLiC-Eval)
- [Implicit Cross-Lingual Rewarding - arXiv 2503.04647](https://arxiv.org/abs/2503.04647)
- [Implicit Cross-Lingual Rewarding - ACL Anthology](https://aclanthology.org/2025.findings-acl.1088/)
- [Code-Switching Curriculum Learning - ACL Anthology](https://aclanthology.org/2025.findings-acl.407/)
- [Code-Switching Curriculum Learning - arXiv 2411.02460](https://arxiv.org/abs/2411.02460)
- [LangGPS - arXiv 2511.10229](https://arxiv.org/abs/2511.10229)
- [Linguistically-Informed Multilingual Instruction Tuning - arXiv 2410.07809](https://arxiv.org/abs/2410.07809)
- [COMPASS - arXiv 2604.20720](https://arxiv.org/abs/2604.20720)
- [Revisiting Multilingual Data Mixtures - arXiv 2510.25947](https://arxiv.org/html/2510.25947v1)
- [Sherkala-Chat - arXiv 2503.01493](https://arxiv.org/abs/2503.01493)
- [Instruction Tuning Kazakh - ACL Anthology](https://aclanthology.org/2025.acl-long.706/)
- [Low-Resource Uyghur - ACL Anthology](https://aclanthology.org/2025.coling-main.559/)
- [Turkic Transfer Framework - arXiv 2604.06202](https://arxiv.org/abs/2604.06202)
- [Left Behind Cross-Lingual Transfer - arXiv 2603.21036](https://arxiv.org/html/2603.21036v1)
- [EMNLP 2026 Conference OpenReview](https://openreview.net/group?id=EMNLP%2F2026%2FConference)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16ac7019-4dce-4853-bf38-f32e586440b2",
  "isSidechain": true,
  "agentId": "a6a68117d153347f2",
  "requestId": "req_011CatVaTijrWKPTgtMFoosJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "661c4911-b5a0-4631-90b2-1672b1070db2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "58594df9-bda3-4ed6-a9ac-9ce91e2c084d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CNFx8PrY6X5xqMfCst37sp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1257,
      "cache_read_input_tokens": 45145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1257,
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
