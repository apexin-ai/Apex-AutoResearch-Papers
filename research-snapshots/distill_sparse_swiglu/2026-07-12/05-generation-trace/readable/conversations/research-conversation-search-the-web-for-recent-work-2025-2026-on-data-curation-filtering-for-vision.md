# Research conversation: Search the web for recent work (2025-2026) on data curation/filtering for Vision-Language-Action (VLA) models. I need to

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af6755c1db562422f.jsonl`
- **Structured JSON:** [`a267f7d806ba3575701c.json`](../../sessions/a2/a267f7d806ba3575701c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-13T19:39:41.977Z_

Search the web for recent work (2025-2026) on data curation/filtering for Vision-Language-Action (VLA) models. I need to find work the generator may have missed. Use these searches:

1. "VLA data curation 2026 site:arxiv.org"
2. "vision language action noisy demonstrations filtering 2025 2026"
3. "importance weighting robot imitation learning 2025 2026"
4. "density ratio estimation robot learning 2025 2026"
5. "discriminator weighted imitation learning VLA"
6. "VLA fine-tuning data quality 2026"
7. "demonstration quality scoring robot manipulation 2026"

For each relevant paper found, report: title, venue/status, what it does, and how it relates to density-ratio weighted BC for VLA training. Focus especially on papers from the last 6 months (Dec 2025 - May 2026).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "acfb4818-c471-4ab3-b987-7588485ca640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T19:39:41.979Z_

```json
{
  "parentUuid": "acfb4818-c471-4ab3-b987-7588485ca640",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
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
  "uuid": "6fca54cc-f426-4155-a58e-0fef600187c1",
  "timestamp": "2026-05-13T19:39:41.979Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T19:39:45.009Z_



I'll search the web for recent work on data curation/filtering for VLA models. Let me first load the WebSearch tool, then run all searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fca54cc-f426-4155-a58e-0fef600187c1",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18nfpRN74pL654CWRav",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f17e7f3f-c825-4489-b2bb-afa726bb3ff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xdzDrdzMCx99Y4cxXNWGP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 759,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 759,
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

_source line 4 · 2026-05-13T19:39:45.341Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016hsKGhWbqDDfxbVJ5MSoXZ`</summary>

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
  "parentUuid": "f17e7f3f-c825-4489-b2bb-afa726bb3ff3",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18nfpRN74pL654CWRav",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "159a212f-84db-449f-8958-8f10a02a7c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xdzDrdzMCx99Y4cxXNWGP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 759,
      "cache_read_input_tokens": 8223,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 759
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 759,
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

_source line 5 · 2026-05-13T19:39:45.344Z_

<details><summary>↩ Tool result · `toolu_016hsKGhWbqDDfxbVJ5MSoXZ`</summary>

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
  "parentUuid": "159a212f-84db-449f-8958-8f10a02a7c75",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "4b62fb96-a4b8-4545-b5d2-752228f07b7c",
  "sourceToolAssistantUUID": "159a212f-84db-449f-8958-8f10a02a7c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T19:39:48.014Z_



Now let me run all seven searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b62fb96-a4b8-4545-b5d2-752228f07b7c",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18nvHKekezcp2y2ywcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27421128-ca28-41d4-a57e-7b61e89b0afb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013j1V5TSd4z1n82xvVfAYHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 7 · 2026-05-13T19:39:48.576Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jfv5qtvEoic8CPa5dddjDp`</summary>

```json
{
  "query": "VLA data curation 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27421128-ca28-41d4-a57e-7b61e89b0afb",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18nvHKekezcp2y2ywcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "034284d0-a311-46e7-b460-302a866c6311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013j1V5TSd4z1n82xvVfAYHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 8 · 2026-05-13T19:39:49.502Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XZh597H4nz9S6PawR2ov3z`</summary>

```json
{
  "query": "vision language action noisy demonstrations filtering 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "034284d0-a311-46e7-b460-302a866c6311",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18nvHKekezcp2y2ywcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4d54912-f3c4-45fc-b212-3020641f6204",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013j1V5TSd4z1n82xvVfAYHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 9 · 2026-05-13T19:39:49.976Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Ujo2m3WUQy41sww3oc3JE`</summary>

```json
{
  "query": "importance weighting robot imitation learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4d54912-f3c4-45fc-b212-3020641f6204",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18nvHKekezcp2y2ywcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b96d8741-c192-46e9-b8ad-c701fed36ac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013j1V5TSd4z1n82xvVfAYHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 10 · 2026-05-13T19:39:50.447Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P3bGuDUbwSc12GDkSt4s9h`</summary>

```json
{
  "query": "density ratio estimation robot learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b96d8741-c192-46e9-b8ad-c701fed36ac3",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18nvHKekezcp2y2ywcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3f28100-9a02-4509-be9e-42a9940c1fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013j1V5TSd4z1n82xvVfAYHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 11 · 2026-05-13T19:39:50.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MNWXL4a6NqGHYSQKavbPJm`</summary>

```json
{
  "query": "discriminator weighted imitation learning VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3f28100-9a02-4509-be9e-42a9940c1fb6",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18nvHKekezcp2y2ywcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1dc2fb76-4e3c-491b-af41-b5364c538896",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013j1V5TSd4z1n82xvVfAYHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 12 · 2026-05-13T19:39:51.857Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011hACsJEW6bVXUrR44A5Jsr`</summary>

```json
{
  "query": "VLA fine-tuning data quality 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dc2fb76-4e3c-491b-af41-b5364c538896",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18nvHKekezcp2y2ywcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf8663f3-85b9-4525-8238-d9e0d37d0573",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013j1V5TSd4z1n82xvVfAYHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 13 · 2026-05-13T19:39:51.964Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VHHWRsqwrx4hbNMQ99ZEW6`</summary>

```json
{
  "query": "demonstration quality scoring robot manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf8663f3-85b9-4525-8238-d9e0d37d0573",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18nvHKekezcp2y2ywcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af040359-eaab-4365-aec9-d6cebdc677b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013j1V5TSd4z1n82xvVfAYHt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 8982,
      "output_tokens": 346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1427
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 346,
          "cache_read_input_tokens": 8982,
          "cache_creation_input_tokens": 1427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1427,
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

_source line 14 · 2026-05-13T19:39:55.782Z_

<details><summary>↩ Tool result · `toolu_01Jfv5qtvEoic8CPa5dddjDp`</summary>

```text
Web search results for query: "VLA data curation 2026 site:arxiv.org"

Links: [{"title":"A Pragmatic VLA Foundation Model","url":"https://arxiv.org/html/2601.18692"},{"title":"Automated Data Curation Using GPS & NLP to Generate Instruction-Action Pairs for Autonomous Vehicle Vision-Language Navigation Datasets","url":"https://arxiv.org/html/2505.03174"},{"title":"How VLAs (Really) Work In Open-World Environments","url":"https://arxiv.org/html/2604.21192"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models","url":"https://arxiv.org/html/2505.23757v1"},{"title":"Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures","url":"https://arxiv.org/html/2603.01063"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919"},{"title":"Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines","url":"https://arxiv.org/html/2604.23001v1"},{"title":"DriveAction: A Benchmark for Exploring Human-like Driving Decisions in VLA Models","url":"https://arxiv.org/html/2506.05667v1"},{"title":"[2505.23757] Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models","url":"https://arxiv.org/abs/2505.23757"}]

Based on the search results from arXiv, I found several papers related to VLA (Vision-Language-Action) data curation from 2026 and recent 2025 publications. Here are the key findings:

## Recent VLA Data Curation Research (2026)

Recent VLA research provides empirical evidence of favorable scaling properties in real-world robot learning, offering critical insights for future VLA development and large-scale data curation.

To ensure high-quality training data, researchers have employed the DataQA pipeline for robotic dataset curation and quality assessment, which enables focus on high-quality demonstrations, improving both sample efficiency and final policy performance.

## Notable Data Curation Approaches

Advanced data curation pipelines leverage Vision-Language Models (VLMs) with Chain-of-Thought reasoning for nuanced understanding, followed by comprehensive human verification to ensure high-quality, reliable labels.

Efficient difficult-sample curation techniques are being employed before reinforcement learning training to maximize training efficiency.

## Key Datasets with Curated Data

The Impromptu VLA Dataset comprises over 80,000 meticulously curated video clips, distilled from over 2M source clips sourced from 8 open-source large-scale datasets.

Current research proposes architecture-agnostic strategies including safety-aware data curation, structured curriculum design, and deployment-oriented validation for improving robustness and safety in real-world VLA applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "034284d0-a311-46e7-b460-302a866c6311",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "51db02e1-9eb0-42a5-be28-898b90c566e2",
  "sourceToolAssistantUUID": "034284d0-a311-46e7-b460-302a866c6311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-13T19:39:56.895Z_

<details><summary>↩ Tool result · `toolu_01XZh597H4nz9S6PawR2ov3z`</summary>

```text
Web search results for query: "vision language action noisy demonstrations filtering 2025 2026"

Links: [{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v2"},{"title":"Thinking in Text and Images: Interleaved Vision–Language Reasoning Traces for Long-Horizon Robot Manipulation","url":"https://arxiv.org/html/2605.00438v1"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"ICCV 2025 Papers Advancing Vision Language Models | Voxel51","url":"https://voxel51.com/blog/iccv-papers-vision-language-models"},{"title":"10 Open Challenges Steering the Future of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.05936"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines","url":"https://arxiv.org/html/2604.23001v1"},{"title":"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/html/2507.01925v1"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666v1"}]

Based on the search results, I've found several recent papers and research on vision-language-action (VLA) models with relevant work on handling noisy demonstrations and filtering. Here are the key findings:

## Key Research Areas:

**1. Filtering Noisy Predictions in VLA Systems**

One approach uses voting logic to filter noisy predictions through System 2 stage tracking, where task stages are predicted as an auxiliary output to provide non-Markovian context.

**2. Data Quality and Filtering**

BLIP includes a data bootstrapping strategy that synthesizes captions and filters noisy web data into high-quality image-text pairs. Another method uses random manual inspection as a sanity check, treating labels as pseudo-supervision rather than ground truth symbolic annotations, with specific filtering rules applied.

**3. Handling Noisy Training Data**

To reduce over-reliance on perfect traces, researchers apply random trace noise and dynamic context masking during training.

**4. Mode-Seeking Objectives for Filtering Uncertainty**

A bounded mode-seeking objective filters out the teacher's epistemic uncertainty while maintaining action diversity, preventing entropy explosion while avoiding premature entropy collapse.

**5. Environmental Noise Challenges**

Environmental noise and artifacts remain open challenges, including reflections, lens flares, and environment-induced noisy camera feeds due to water, dust, or debris.

The research from 2025-2026 shows increasing focus on making VLA systems robust to noisy demonstrations through various filtering and validation strategies during both training and inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4d54912-f3c4-45fc-b212-3020641f6204",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "c7d83c1d-982e-4a79-a461-8d3fd30ecd1f",
  "sourceToolAssistantUUID": "f4d54912-f3c4-45fc-b212-3020641f6204",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T19:39:57.293Z_

<details><summary>↩ Tool result · `toolu_01P3bGuDUbwSc12GDkSt4s9h`</summary>

```text
Web search results for query: "density ratio estimation robot learning 2025 2026"

Links: [{"title":"Density Ratio Estimation in Machine Learning | Request PDF","url":"https://www.researchgate.net/publication/215705204_Density_Ratio_Estimation_in_Machine_Learning"},{"title":"Density Ratio Estimation in Machine Learning: | Guide books | ACM Digital Library","url":"https://dl.acm.org/doi/book/10.5555/2181148"},{"title":"ICML Poster Projection Pursuit Density Ratio Estimation","url":"https://icml.cc/virtual/2025/poster/45537"},{"title":"Density Ratio Estimation in Machine Learning: Sugiyama, Masashi, Suzuki, Taiji, Kanamori, Takafumi: 9780521190176: Amazon.com: Books","url":"https://www.amazon.com/Density-Ratio-Estimation-Machine-Learning/dp/0521190177"},{"title":"Accepted Papers · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/"},{"title":"Continual Density Ratio Estimation in an Online Setting - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210305276C/abstract"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Korea Robot Density 2026: Why It Leads the World by 6x - SeoulzKorea Robot Density 2026: Why It Leads the World by 6x","url":"https://www.seoulz.com/korea-robot-density-2026/"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"IFR reports robot density increase across Europe, Asia, and the Americas - The Robot Report","url":"https://www.therobotreport.com/ifr-reports-robot-density-increase-across-europe-asia-americas/"}]

Based on the search results, here's what I found regarding density ratio estimation and robot learning:

## Density Ratio Estimation in Machine Learning

Density ratio estimation (DRE) is a paramount task in machine learning, with broad applications across multiple domains, such as covariate shift adaptation, causal inference, independence tests and beyond.

Recent work in this area includes a novel approach for DRE based on projection pursuit approximation that leverages PP to mitigate the impact of high dimensionality while retaining the model flexibility needed for the accuracy of DRE. This approach was presented as an ICML 2025 poster.

Additionally, direct density ratio estimation (DRE) is the process of estimating the ratio between two probability densities by directly minimizing a single empirical risk functional.

## Robot Learning and Robotics

While the search results discuss robot density (the number of robots per workers in different countries), they don't contain specific recent research on the intersection of density ratio estimation and robot learning for 2025-2026. The results do show that diffusion generative models have recently emerged as a promising approach in robotics, especially in robot manipulations, leveraging a probabilistic framework and standing out with their ability to model multi-modal distributions and robustness to high-dimensional input and output spaces.

To find more specific research connecting density ratio estimation directly to robot learning in 2025-2026, a more specialized search of robotics conferences or publications would be helpful.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3f28100-9a02-4509-be9e-42a9940c1fb6",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "452df437-195c-4af4-9625-f1a4f8a7d9b9",
  "sourceToolAssistantUUID": "f3f28100-9a02-4509-be9e-42a9940c1fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T19:39:57.608Z_

<details><summary>↩ Tool result · `toolu_01MNWXL4a6NqGHYSQKavbPJm`</summary>

```text
Web search results for query: "discriminator weighted imitation learning VLA"

Links: [{"title":"Discriminator-Weighted Offline Imitation Learning from ...","url":"https://proceedings.mlr.press/v162/xu22l/xu22l.pdf"},{"title":"[2207.10050] Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/abs/2207.10050"},{"title":"Discriminator-weighted offline imitation learning with unlabeled demonstrations for robotic tasks: Journal of the Chinese Institute of Engineers: Vol 48 , No 6 - Get Access","url":"https://www.tandfonline.com/doi/full/10.1080/02533839.2025.2517354"},{"title":"[2504.13368] An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://arxiv.org/abs/2504.13368"},{"title":"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://arxiv.org/html/2504.13368"},{"title":"[2207.10050v1] Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/abs/2207.10050v1"},{"title":"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=9JtG4nN7ql"},{"title":"Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations | OpenReview","url":"https://openreview.net/forum?id=XfK0p2TSIB"},{"title":"Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations","url":"https://proceedings.mlr.press/v162/xu22l.html"},{"title":"Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations | DeepAI","url":"https://deepai.org/publication/discriminator-weighted-offline-imitation-learning-from-suboptimal-demonstrations"}]

Based on the search results, I found information about discriminator-weighted imitation learning. However, I notice your query also mentions "VLA" (Vision Language Agent), which doesn't appear in these results. The search results focus on discriminator-weighted imitation learning in the context of offline reinforcement learning and robotic tasks. Let me provide what I found:

## Discriminator-Weighted Imitation Learning

Discriminator-weighted imitation learning introduces an additional discriminator to distinguish expert and non-expert data, with the outputs of the discriminator serving as weights of the behavioral cloning (BC) loss.

This approach addresses the problem of offline imitation learning where an agent aims to learn an optimal expert behavior policy without additional online environment interactions, using a supplementary offline dataset from suboptimal behaviors.

### Recent Applications

More recent work has extended this approach: Iterative Dual Reinforcement Learning (IDRL) introduces a method that takes an optimal discriminator-weighted imitation view of solving reinforcement learning. A discriminator can analytically weigh all data to distinguish between optimal and suboptimal instances, with this discriminative weighting influencing policy learning and preventing suboptimal behavior.

**Regarding VLA (Vision Language Agent):** The search results don't contain information specifically about applying discriminator-weighted imitation learning to VLAs. If you're looking for information about how these techniques are being applied to vision language agents, you may want to search for more specific papers combining these topics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1dc2fb76-4e3c-491b-af41-b5364c538896",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "df80952c-4d4e-49dc-a69f-c42b4ddd9e0e",
  "sourceToolAssistantUUID": "1dc2fb76-4e3c-491b-af41-b5364c538896",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T19:39:58.990Z_

<details><summary>↩ Tool result · `toolu_011hACsJEW6bVXUrR44A5Jsr`</summary>

```text
Web search results for query: "VLA fine-tuning data quality 2026"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"Scaling VLA Model Training on a Budget: Lessons From 100+ Fine-Tunes | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/scaling-vla-training-on-a-budget"},{"title":"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts","url":"https://arxiv.org/html/2605.06175v1"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA","url":"https://www.airoa.org/updates/2026-02-10"},{"title":"From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop","url":"https://icra2026vlapipeline.github.io/"},{"title":"Efficient Fine-Tuning of VLA Models for Industrial Manipulation","url":"https://publica.fraunhofer.de/entities/publication/2a61fc6e-190b-4383-bb04-808d7415f3ae"},{"title":"ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=Mzz4BhdIFb"}]

Based on the search results, here's what I found about VLA fine-tuning and data quality in 2026:

## Key Findings on VLA Fine-Tuning Data Quality in 2026

**Data Quality as Critical Priority:**
The scarce resource is almost never compute—it is clean, well-labeled, well-bucketed demonstration data. What separates teams that succeed from teams that struggle is not compute — it is the discipline of treating data, evaluation, and hardware calibration as first-class engineering.

**Training Data Challenges:**
The variable quality of training data often constrains the performance of these models. Recent research has introduced approaches like ReinboT to address this, where the model achieves a deeper understanding of the data quality distribution by predicting dense returns that capture the nuances of manipulation tasks, enabling the robot to generate more robust decision-making actions.

**Standardization Efforts:**
Most pipelines lack rigorous data curation, principled training regimes, and standardized evaluation, leading to inconsistent performance and safety concerns on physical robots. Performance on real robots is dictated by the underlying "data engine", highlighting the importance of scalable data collection, domain randomization, procedural synthesis, and human-in-the-loop feedback.

**Community Focus:**
The AI Robotic Association (AIRoA) announced that its workshop proposal "From Data to Decisions: VLA Pipelines for Real Robots" has been accepted for presentation at ICRA 2026 in Vienna, Austria, from June 1–5, 2026. The competition involves training on over 10,000 hours of data and evaluating VLA systems on real robot hardware.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf8663f3-85b9-4525-8238-d9e0d37d0573",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "7af09c4a-9170-4c56-a107-1118eeb06035",
  "sourceToolAssistantUUID": "cf8663f3-85b9-4525-8238-d9e0d37d0573",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T19:40:00.409Z_

<details><summary>↩ Tool result · `toolu_01VHHWRsqwrx4hbNMQ99ZEW6`</summary>

```text
Web search results for query: "demonstration quality scoring robot manipulation 2026"

Links: [{"title":"RoCo Challenge at AAAI 2026: Benchmarking Robotic Collaborative Manipulation for Assembly Towards Industrial Automation","url":"https://arxiv.org/html/2603.15469"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"Competitions - IEEE ICRA 2026","url":"https://2026.ieee-icra.org/program/competitions/"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/152/"},{"title":"[2603.15469] RoCo Challenge at AAAI 2026: Benchmarking Robotic Collaborative Manipulation for Assembly Towards Industrial Automation","url":"https://arxiv.org/abs/2603.15469"},{"title":"REGULAR PAPER 1 Trustworthy Evaluation of Robotic Manipulation: A New Benchmark","url":"https://arxiv.org/pdf/2601.18723"},{"title":"Trustworthy Evaluation of Robotic Manipulation: A New Benchmark and AutoEval Methods","url":"https://arxiv.org/html/2601.18723"},{"title":"RoCo Challenge at AAAI 2026: Benchmarking Robotic Collaborative Manipulation for Assembly Towards Industrial Automation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260315469L/abstract"},{"title":"Abstracting Robot Manipulation Skills via Mixture-of- ...","url":"https://arxiv.org/pdf/2601.21251"}]

Based on the search results, here are the key findings related to demonstration quality scoring in robot manipulation in 2026:

## Demonstration Quality Scoring Approaches

There has been significant interest in dataset curation tools, episode quality scoring, and demonstration filtering in 2026 robot manipulation research.

The Open-X Embodiment quality rubric, extended by SVRC and several academic partners, has become the most widely cited framework, covering trajectory smoothness, demonstration diversity, and labeling confidence.

## Quality-Based Curation Methods

One notable approach is Quality over Quantity (QoQ), which defines data quality as the contribution of each training sample to reducing loss on validation demonstrations. This method implements trajectory-wise curation, which aggregates influence scores of state-action pairs within the same trajectory and then selects high-quality trajectories based on the aggregated scores, which significantly reduces noise in the influence signal while ensuring broad state coverage.

## Importance of Demonstration Quality

A well-curated 500-demo fine-tune of a 7B VLA outperforms a poorly curated fine-tune of a 70B model on most manipulation benchmarks, highlighting the critical importance of demonstration quality over quantity.

## Benchmark Datasets with Quality Annotations

Recent benchmarks incorporate fine-grained quality scoring. The Eval-Actions dataset contains approximately 52 hours of manipulation videos across 150 distinct robotic tasks, comprising 13k annotated action trajectories, with domain experts providing not only numerical quality scores but also detailed Chain-of-Thought reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af040359-eaab-4365-aec9-d6cebdc677b7",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "0c26e635-83a5-4f44-971a-fbe47c3e447e",
  "sourceToolAssistantUUID": "af040359-eaab-4365-aec9-d6cebdc677b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T19:40:00.413Z_

<details><summary>↩ Tool result · `toolu_014Ujo2m3WUQy41sww3oc3JE`</summary>

```text
Web search results for query: "importance weighting robot imitation learning 2025 2026"

Links: [{"title":"Discriminator-weighted offline imitation learning with unlabeled demonstrations for robotic tasks: Journal of the Chinese Institute of Engineers: Vol 48 , No 6 - Get Access","url":"https://www.tandfonline.com/doi/full/10.1080/02533839.2025.2517354"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"Frontiers | Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1682437/full"},{"title":"Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions","url":"https://arxiv.org/html/2604.15395v1"},{"title":"Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12757213/"},{"title":"A survey on imitation learning for contact-rich tasks in robotics - Toshiaki Tsuji, Yasuhiro Kato, Gokhan Solak, Heng Zhang, Tadej Petrič, Francesco Nori, Arash Ajoudani, 2026","url":"https://journals.sagepub.com/doi/10.1177/02783649261417694"},{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://arxiv.org/html/2509.01657"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Frontiers | Imitation learning for legged robot locomotion: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/full"}]

I've found several recent papers and research on importance weighting in robot imitation learning from 2025-2026. Here are the key findings:

## Recent Work on Importance Weighting in Robot Imitation Learning

Existing methods like Two-step Importance Weighting IL (2IWIL) and Trajectory-ranked Reward EXtrapolation (T-REX) require manual labeling or interaction with the environment to filter out suboptimal data, which is time-consuming and laborious.

A recent approach introduces an additional discriminator to behavioral cloning that analytically weighs all data to distinguish between optimal and suboptimal instances, with this discriminative weighting influencing policy learning and preventing suboptimal behavior.

## Intervention Weighted Regression

Intervention Weighted Regression (IWR) addresses the problem of substantial policy changes by storing all generated data, where during policy training, an equal number of samples from both agent-generated and supervisor-generated datasets are used to update the policy, with samples from interventions weighted more heavily to indicate bottlenecks in state space.

## Data Retrieval with Importance Weights

One approach for learning from limited demonstrations is retrieval from prior datasets, where retrieval-based methods augment small demonstration datasets with relevant samples taken from large, widely available robotics datasets.

The research landscape shows active development in importance weighting techniques to improve robotic imitation learning efficiency and data quality, particularly in handling suboptimal demonstrations and leveraging diverse data sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b96d8741-c192-46e9-b8ad-c701fed36ac3",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "bdabf86c-db1a-4a2f-9eb5-37aae60725ea",
  "sourceToolAssistantUUID": "b96d8741-c192-46e9-b8ad-c701fed36ac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-13T19:40:04.035Z_

Now let me do some follow-up searches on the most promising leads to get more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdabf86c-db1a-4a2f-9eb5-37aae60725ea",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18p2Tvao21UUkpm3aDx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cab390d-0a0d-455b-a7f7-7d81d15c3f7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014p8XQDTmpN2HXmDvjsFx4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3629,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 10409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 22 · 2026-05-13T19:40:05.062Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QY7jK1mRogwSRaZTHWZUBP`</summary>

```json
{
  "query": "Quality over Quantity demonstration curation influence functions robot learning arxiv 2603.09056"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cab390d-0a0d-455b-a7f7-7d81d15c3f7b",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18p2Tvao21UUkpm3aDx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52ea7d5e-1f80-49b8-b16a-fb3d7671c64e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014p8XQDTmpN2HXmDvjsFx4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3629,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 10409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 23 · 2026-05-13T19:40:06.042Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013zvJFJ28Ydou9NyptSetx3`</summary>

```json
{
  "query": "discriminator-weighted offline imitation learning unlabeled demonstrations robotic tasks 2025 Chinese Institute Engineers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52ea7d5e-1f80-49b8-b16a-fb3d7671c64e",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18p2Tvao21UUkpm3aDx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e458ea2c-5916-4617-b2b4-aa5598696ee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014p8XQDTmpN2HXmDvjsFx4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3629,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 10409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 24 · 2026-05-13T19:40:06.866Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TAgTaZBtqfZ5ZEcG3V4YjL`</summary>

```json
{
  "query": "VLA-RFT reinforcement fine-tuning verified rewards world simulators 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e458ea2c-5916-4617-b2b4-aa5598696ee7",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18p2Tvao21UUkpm3aDx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e393258-1861-40ad-9c14-e930773b12f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014p8XQDTmpN2HXmDvjsFx4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3629,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 10409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 25 · 2026-05-13T19:40:07.867Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TARAWVwsvcjj3uke6izs2f`</summary>

```json
{
  "query": "DataQA pipeline robotic dataset curation quality assessment VLA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e393258-1861-40ad-9c14-e930773b12f3",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18p2Tvao21UUkpm3aDx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02ca5fc4-48cd-4ccd-b496-a48e0b49340e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014p8XQDTmpN2HXmDvjsFx4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3629,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 10409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
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

_source line 26 · 2026-05-13T19:40:08.327Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012AMa61moCzytgu1YBpVoFV`</summary>

```json
{
  "query": "ReinboT robot visual language manipulation reinforcement learning data quality 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02ca5fc4-48cd-4ccd-b496-a48e0b49340e",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18p2Tvao21UUkpm3aDx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "726d47d9-2da9-4a40-9129-d9c51221444f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014p8XQDTmpN2HXmDvjsFx4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3629,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 10409,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3023
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3629,
          "output_tokens": 300,
          "cache_read_input_tokens": 10409,
          "cache_creation_input_tokens": 3023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3023,
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

_source line 27 · 2026-05-13T19:40:10.495Z_

<details><summary>↩ Tool result · `toolu_01QY7jK1mRogwSRaZTHWZUBP`</summary>

```text
Web search results for query: "Quality over Quantity demonstration curation influence functions robot learning arxiv 2603.09056"

Links: [{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121"},{"title":"Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration","url":"https://arxiv.org/html/2412.14309v1"},{"title":"Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation","url":"https://arxiv.org/html/2502.08211"},{"title":"Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250208211X/abstract"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://arxiv.org/html/2506.13536v1"},{"title":"Quantifying Demonstration Quality for Robot Learning and Generalization | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel7/7083369/7339444/09832744.pdf"},{"title":"IF-CPS: Influence Functions for Cyber-Physical Systems— A Unified Framework for Diagnosis, Curation, and Safety Attribution","url":"https://arxiv.org/html/2603.21543"},{"title":"[2203.13843] Quantifying Demonstration Quality for Robot Learning and Generalization","url":"https://arxiv.org/abs/2203.13843"}]

Based on the search results, I found the paper you're looking for:

"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning" was submitted to arXiv on March 10, 2026, with authors Haeone Lee, Taywon Min, Junsu Kim, Sinjae Kang, Fangchen Liu, Lerrel Pinto, and Kimin Lee from KAIST, UC Berkeley, and New York University.

The paper addresses how the quality of demonstration data, often collected through human teleoperation, remains a critical bottleneck for effective data-driven robot learning, with human errors, operational constraints, and teleoperator variability introducing noise and suboptimal behaviors.

The proposed approach, Quality over Quantity (QoQ), is a systematic method for identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations.

The paper is available on arXiv at: https://arxiv.org/abs/2603.09056


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52ea7d5e-1f80-49b8-b16a-fb3d7671c64e",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "16ae76e6-0f3a-4799-af43-97719657b51e",
  "sourceToolAssistantUUID": "52ea7d5e-1f80-49b8-b16a-fb3d7671c64e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T19:40:12.769Z_

<details><summary>↩ Tool result · `toolu_013zvJFJ28Ydou9NyptSetx3`</summary>

```text
Web search results for query: "discriminator-weighted offline imitation learning unlabeled demonstrations robotic tasks 2025 Chinese Institute Engineers"

Links: [{"title":"Discriminator-weighted offline imitation learning with unlabeled demonstrations for robotic tasks: Journal of the Chinese Institute of Engineers: Vol 48 , No 6 - Get Access","url":"https://www.tandfonline.com/doi/full/10.1080/02533839.2025.2517354"},{"title":"Discriminator-Weighted Offline Imitation Learning from ...","url":"https://proceedings.mlr.press/v162/xu22l/xu22l.pdf"},{"title":"DISCRIMINATOR-WEIGHTED OFFLINE IMITATION ...","url":"https://openreview.net/pdf?id=hW2kwAcXq5w"},{"title":"Offline Imitation Learning from Imperfect Human Demonstrations","url":"https://collab.me.vt.edu/pdfs/losey_thri2025.pdf"},{"title":"Discriminator-Weighted Ofﬂine Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/pdf/2207.10050"},{"title":"Unlabeled Imperfect Demonstrations in Adversarial Imitation Learning","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26222/25994"},{"title":"Offline Imitation Learning with Variational Counterfactual Reasoning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/8833c8aa10542d24d693bbaf6a4598f5-Paper-Conference.pdf"},{"title":"Robust Offline Imitation Learning from Diverse Auxiliary Data","url":"https://arxiv.org/html/2410.03626"},{"title":"[2207.10050] Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/abs/2207.10050"},{"title":"Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations","url":"https://proceedings.mlr.press/v162/xu22l.html"}]

I found a directly relevant research article published in 2025. Here are the key findings from the web search:

## Recent 2025 Publication

A paper titled "Discriminator-weighted offline imitation learning with unlabeled demonstrations for robotic tasks" was published online on June 17, 2025, in the Journal of the Chinese Institute of Engineers (Volume 48, Issue 6, pages 718-731).

## Research Overview

The research addresses the problem that imitation learning algorithms for robotic applications generally require adequate and optimal data to learn well-performing policies, but existing methods such as Two-step Importance Weighting IL (2IWIL) and Trajectory-ranked Reward EXtrapolation (T-REX) require manual labeling or interaction with the environment to filter out suboptimal data, which is time-consuming and laborious.

## Proposed Solution

The paper proposes an alternative solution that eliminates the need for manual labeling or environmental interaction by introducing an additional discriminator to the behavioral cloning method, which analytically weighs all data to distinguish between optimal and suboptimal instances, with this discriminative weighting influencing policy learning and preventing suboptimal behavior.

This work appears to be an application and extension of the discriminator-weighted behavioral cloning (DWBC) framework to robotic tasks with unlabeled demonstrations, addressing a significant practical challenge in imitation learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e458ea2c-5916-4617-b2b4-aa5598696ee7",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "67e20388-9916-4edb-9a48-80d1889096b9",
  "sourceToolAssistantUUID": "e458ea2c-5916-4617-b2b4-aa5598696ee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T19:40:13.115Z_

<details><summary>↩ Tool result · `toolu_01TAgTaZBtqfZ5ZEcG3V4YjL`</summary>

```text
Web search results for query: "VLA-RFT reinforcement fine-tuning verified rewards world simulators 2026"

Links: [{"title":"[2510.00406] VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators","url":"https://arxiv.org/abs/2510.00406"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"[2510.00406v1] VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators","url":"https://arxiv.org/abs/2510.00406v1"},{"title":"VLA-RFT: Vision-language-action Reinforcement fine-tuning with verified rewards in world simulators","url":"https://arxiv.org/html/2510.00406v1"},{"title":"Paper page - VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators","url":"https://huggingface.co/papers/2510.00406"},{"title":"VLA-RFT: VISION-LANGUAGE-ACTION REINFORCE- MENT FINE-TUNING WITH VERIFIED","url":"https://arxiv.org/pdf/2510.00406"},{"title":"VLA-RFT","url":"https://vla-rft.github.io/"},{"title":"[Quick Review] VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified\\n Rewards in World Simulators","url":"https://liner.com/review/vlarft-visionlanguageaction-reinforcement-finetuning-with-verified-rewards-in-world-simulators"},{"title":"[Literature Review] VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators","url":"https://www.themoonlight.io/en/review/vla-rft-vision-language-action-reinforcement-fine-tuning-with-verified-rewards-in-world-simulators"},{"title":"GitHub - OpenHelix-Team/VLA-RFT: VLA-RFT: Vision-Language-Action Models with Reinforcement Fine-Tuning","url":"https://github.com/OpenHelix-Team/VLA-RFT"}]

I found comprehensive information about VLA-RFT. Here's what the search reveals:

## Overview

VLA-RFT is a reinforcement fine-tuning framework that leverages a data-driven world model as a controllable simulator, trained from real interaction data to predict future visual observations conditioned on actions, allowing policy rollouts with dense, trajectory-level rewards derived from goal-achieving references.

## Key Problem

Vision-Language-Action (VLA) models enable embodied decision-making but rely heavily on imitation learning, leading to compounding errors and poor robustness under distribution shift. Reinforcement learning (RL) can mitigate these issues yet typically demands costly real-world interactions or suffers from sim-to-real gaps.

## Technical Approach

The framework employs a controllable world simulator that, once trained on a dataset of robot interactions, can predict future visual observations conditioned on an action sequence. Unlike conventional simulation environments restricted to handcrafted scenarios, this simulator is entirely data-driven, capturing the diversity of real-world interactions while avoiding the prohibitive cost and safety risks of training directly in the physical world.

## Results

With fewer than 400 fine-tuning steps, VLA-RFT surpasses strong supervised baselines and achieves greater efficiency than simulator-based RL. In perturbed or adversarial scenarios, VLA-RFT exhibits superior action robustness, sustaining stable task execution even under unexpected environmental variations.

## Limitations

The verified reward signal is still largely defined by the similarity between generated trajectories and expert demonstrations. Consequently, the policy remains constrained by the quality of the expert dataset, limiting its ability to discover strategies that surpass expert performance.

The paper was published on arXiv in October 2025 (preprint 2510.00406).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e393258-1861-40ad-9c14-e930773b12f3",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "f31ee13e-7006-4443-84d0-1f638d23fa1e",
  "sourceToolAssistantUUID": "8e393258-1861-40ad-9c14-e930773b12f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T19:40:14.688Z_

<details><summary>↩ Tool result · `toolu_01TARAWVwsvcjj3uke6izs2f`</summary>

```text
Web search results for query: "DataQA pipeline robotic dataset curation quality assessment VLA 2026"

Links: [{"title":"From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop","url":"https://icra2026vlapipeline.github.io/"},{"title":"AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA","url":"https://www.airoa.org/updates/2026-02-10"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"},{"title":"ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning","url":"https://arxiv.org/html/2602.11236v1"},{"title":"Frontiers | A roadmap for improving data quality through standards for collaborative intelligence in human-robot applications","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1434351/full"},{"title":"2025-9-18 ThinkAct: Vision-Language-Action Reasoning via","url":"https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey","url":"https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"}]

Based on the search results, I found relevant information about the DataQA pipeline for robotic dataset curation and quality assessment in the context of VLA (Vision-Language-Action) models:

## DataQA Pipeline Overview

The DataQA pipeline is used for robotic dataset curation and quality assessment, enabling focus on high-quality demonstrations to improve both sample efficiency and final policy performance.

## Key Features

The DataQA pipeline filters and smooths heterogeneous demonstrations and aligns temporal dynamics via optical flow–based resampling. This approach is particularly important for handling the challenges of working with multiple diverse robotic datasets.

## Application Context

The DataQA pipeline has been applied in recent VLA research, specifically in the Green-VLA framework. The corpus combines large-scale open datasets (e.g., AgibotWorld, DROID, Galaxea) with internally collected humanoid and dexterous-hand data.

## Related VLA 2026 Context

Your search also appears related to the broader VLA 2026 community focus on standardizing practices. Most pipelines lack rigorous data curation, principled training regimes, and standardized evaluation, leading to inconsistent performance and safety concerns on physical robots. A VLA workshop aims to examine the entire end-to-end VLA pipeline, from scalable data collection and systematic curation to training strategies and inference-time reasoning.

The DataQA pipeline represents an important step toward addressing these challenges in VLA system development.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02ca5fc4-48cd-4ccd-b496-a48e0b49340e",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "14ccd341-3582-4082-ad19-450d4d81f2ff",
  "sourceToolAssistantUUID": "02ca5fc4-48cd-4ccd-b496-a48e0b49340e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T19:40:15.040Z_

<details><summary>↩ Tool result · `toolu_012AMa61moCzytgu1YBpVoFV`</summary>

```text
Web search results for query: "ReinboT robot visual language manipulation reinforcement learning data quality 2026"

Links: [{"title":"ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=Mzz4BhdIFb"},{"title":"[2505.07395] ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning","url":"https://arxiv.org/abs/2505.07395"},{"title":"ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning","url":"https://arxiv.org/html/2505.07395v1"},{"title":"[2505.07395v1] ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning","url":"https://arxiv.org/abs/2505.07395v1"},{"title":"[Literature Review] ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning","url":"https://www.themoonlight.io/en/review/reinbot-amplifying-robot-visual-language-manipulation-with-reinforcement-learning"},{"title":"ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/391676842_ReinboT_Amplifying_Robot_Visual-Language_Manipulation_with_Reinforcement_Learning"},{"title":"ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning","url":"https://proceedings.mlr.press/v267/zhang25dr.html"},{"title":"ICML Poster ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning","url":"https://icml.cc/virtual/2025/poster/45523"},{"title":"ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/reinbot-amplifying-robot-visual-language-manipulation-reinforcement"},{"title":"ReinboT: Amplifying Robot Visual-Language Manipulation with","url":"https://openreview.net/pdf?id=Mzz4BhdIFb"}]

Based on the search results, here's what I found about ReinboT:

## ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning

ReinboT is a novel end-to-end Vision-Language-Action (VLA) model that integrates the RL principle of maximizing cumulative reward.

### Key Innovation

The core problem ReinboT addresses is that Vision-Language-Action models have shown great potential in robotic decision-making tasks via imitation learning, but the variable quality of training data often constrains performance.

### How It Works

ReinboT achieves a deeper understanding of data quality distribution by predicting dense returns that capture manipulation task nuances, and this dense return prediction capability enables robots to generate more robust decision-making actions oriented towards maximizing future benefits.

The approach efficiently decomposes long-horizon manipulation task trajectories into segments with single sub-goals and designs dense rewards that capture task characteristics, remaining widely applicable to various manipulation tasks.

### Results

Extensive experiments show ReinboT achieves state-of-the-art performance on the CALVIN mixed-quality dataset and exhibits superior few-shot learning and out-of-distribution generalization capabilities in real-world tasks.

The research was published in May 2025 on arXiv and was presented at ICML 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "726d47d9-2da9-4a40-9129-d9c51221444f",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "0dbca7ef-1776-4775-97a3-e68b2b7df522",
  "sourceToolAssistantUUID": "726d47d9-2da9-4a40-9129-d9c51221444f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-13T19:40:17.621Z_

Let me do a few more targeted searches to find additional recent papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dbca7ef-1776-4775-97a3-e68b2b7df522",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18q723LYG7ERKMtiECN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c04c8a8a-b6d6-4c73-a52a-ae02613f46f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReDEQKkZ83tqEi2e9qCnCQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8447,
      "cache_read_input_tokens": 13432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8447,
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

_source line 33 · 2026-05-13T19:40:18.716Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JakAJ7CHYpJUezcxHEyiDs`</summary>

```json
{
  "query": "CUPID curating data robot influence functions arxiv 2506"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c04c8a8a-b6d6-4c73-a52a-ae02613f46f1",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18q723LYG7ERKMtiECN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12ad280b-e85e-4830-b055-957bb0b5565f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReDEQKkZ83tqEi2e9qCnCQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8447,
      "cache_read_input_tokens": 13432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8447,
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

_source line 34 · 2026-05-13T19:40:19.720Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HKtQ1x5LG4cYLuCyXqo2Rk`</summary>

```json
{
  "query": "Green-VLA DataQA optical flow resampling data curation 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12ad280b-e85e-4830-b055-957bb0b5565f",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18q723LYG7ERKMtiECN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fe87c58-8cb8-4091-94e8-c488d9b37254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReDEQKkZ83tqEi2e9qCnCQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8447,
      "cache_read_input_tokens": 13432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8447,
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

_source line 35 · 2026-05-13T19:40:20.041Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013jiyekKqaXw5uCdTXQpXd9`</summary>

```json
{
  "query": "\"data retrieval importance weights few-shot imitation learning\" arxiv 2509.01657"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fe87c58-8cb8-4091-94e8-c488d9b37254",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18q723LYG7ERKMtiECN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e75cc1a6-20a8-4c9a-84a3-c0f45abbf01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReDEQKkZ83tqEi2e9qCnCQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8447,
      "cache_read_input_tokens": 13432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8447,
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

_source line 36 · 2026-05-13T19:40:21.450Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VZUa4RJoZg5QxHQJh9Uez3`</summary>

```json
{
  "query": "VLA-OPD on-policy distillation offline SFT online RL VLA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e75cc1a6-20a8-4c9a-84a3-c0f45abbf01b",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18q723LYG7ERKMtiECN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69ccfd82-f721-4f43-b7f0-49114d689d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReDEQKkZ83tqEi2e9qCnCQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8447,
      "cache_read_input_tokens": 13432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8447,
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

_source line 37 · 2026-05-13T19:40:21.896Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LgUBBV96WNcZy3swF8KdL2`</summary>

```json
{
  "query": "\"optimal discriminator weighted imitation\" reinforcement learning arxiv 2504.13368"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69ccfd82-f721-4f43-b7f0-49114d689d64",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18q723LYG7ERKMtiECN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22cf9e5a-2f4e-4c5c-b03e-7becba9c44dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReDEQKkZ83tqEi2e9qCnCQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8447,
      "cache_read_input_tokens": 13432,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 301,
          "cache_read_input_tokens": 13432,
          "cache_creation_input_tokens": 8447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8447,
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

_source line 38 · 2026-05-13T19:40:25.859Z_

<details><summary>↩ Tool result · `toolu_01JakAJ7CHYpJUezcxHEyiDs`</summary>

```text
Web search results for query: "CUPID curating data robot influence functions arxiv 2506"

Links: [{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"[2506.19121] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121"},{"title":"[2506.19121v2] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121v2"},{"title":"GitHub - agiachris/cupid: Official repository for \"CUPID: Curating Data your Robot Loves with Influence Functions,\" accepted to CoRL 2025. · GitHub","url":"https://github.com/agiachris/cupid"},{"title":"CUPID: Robot Data Curation via Influence Functions","url":"https://www.emergentmind.com/papers/2506.19121"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions | OpenReview","url":"https://openreview.net/forum?id=TqevdDMqrK"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"[PDF] CUPID: Curating Data your Robot Loves with Influence Functions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CUPID:-Curating-Data-your-Robot-Loves-with-Agia-Sinha/666481cd9e72de8e90e3dd12fb826338f5ce17f0"},{"title":"Revisiting Data Attribution for Influence Functions","url":"https://arxiv.org/html/2508.07297v1"}]

Based on the search results, here's what I found about CUPID:

## Overview

CUPID is a robot data curation method based on a novel influence function-theoretic formulation for imitation learning policies. The paper was accepted to CoRL 2025.

## How It Works

Given a set of evaluation rollouts, CUPID estimates the influence of each training demonstration on the policy's expected return. CUPID uses influence functions to predictively answer counterfactual questions about the effect of each demonstration on downstream policy performance, enabling questions like "How would my policy's expected return change if I upweighted the loss on a demonstration during training?" without needing to retrain any policies.

## Applications

CUPID curates data by 1) filtering out training demonstrations that harm policy performance and 2) subselecting newly collected trajectories that will most improve the policy.

## Experimental Results

Training with less than 33% of curated data can yield state-of-the-art diffusion policies on the simulated RoboMimic benchmark, with similar gains observed in hardware. Hardware experiments show that the method can identify robust strategies under distribution shift, isolate spurious correlations, and even enhance the post-training of generalist robot policies.

The paper is available on arXiv as 2506.19121, with code and resources available at https://cupid-curation.github.io/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12ad280b-e85e-4830-b055-957bb0b5565f",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "4d572729-079d-42db-98e5-a5058d6db11f",
  "sourceToolAssistantUUID": "12ad280b-e85e-4830-b055-957bb0b5565f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-13T19:40:27.027Z_

<details><summary>↩ Tool result · `toolu_01HKtQ1x5LG4cYLuCyXqo2Rk`</summary>

```text
Web search results for query: "Green-VLA DataQA optical flow resampling data curation 2026 arxiv"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"Flow-Anything: Learning Real-World Optical Flow Estimation from Large-Scale Single-view Images","url":"https://arxiv.org/html/2506.07740v1"},{"title":"SciFlow: Empowering Lightweight Optical Flow Models with Self-Cleaning Iterations","url":"https://arxiv.org/html/2404.08135v1"},{"title":"Efficient Correlation Volume Sampling for Ultra-High-Resolution Optical Flow Estimation","url":"https://arxiv.org/html/2505.16942v1"},{"title":"CompactFlowNet: Efficient Real-time Optical Flow Estimation on Mobile Devices","url":"https://arxiv.org/html/2412.13273v1"},{"title":"FlowSeek: Optical Flow Made Easier with Depth Foundation Models and Motion Bases","url":"https://arxiv.org/html/2509.05297v1"},{"title":"[2503.14880] DPFlow: Adaptive Optical Flow Estimation with a Dual-Pyramid Framework","url":"https://arxiv.org/abs/2503.14880"},{"title":"DA-Flow: Degradation-Aware Optical Flow Estimation with Diffusion Models","url":"https://arxiv.org/html/2603.23499"},{"title":"Memory-Efficient Optical Flow via Radius-Distribution Orthogonal Cost Volume","url":"https://arxiv.org/html/2312.03790v1"}]

I found relevant information about Green-VLA with DataQA and optical flow-based resampling! Here are the key findings:

Green-VLA is a staged vision–language–action framework that moves beyond raw scale toward quality alignment, action unification, and reinforcement learning fine-tuning.

The DataQA pipeline filters and smooths heterogeneous demonstrations and aligns temporal dynamics via optical flow–based resampling. This data curation approach is central to the system's design.

To ensure high-quality training data, the DataQA pipeline is employed for robotic dataset curation and quality assessment, which enables the model training to focus on high-quality demonstrations, improving both sample efficiency and final policy performance.

The corpus combines large-scale open datasets (e.g., AgibotWorld, DROID, Galaxea) with internally collected humanoid and dexterous-hand data.

The paper also demonstrates strong results: Green-VLA matches or exceeds prior pretrains at R0, is competitive with other VLA models after embodiment tuning, and achieves the largest gains after RL alignment (R2), especially on long-horizon success, recovery, and precise task following.

The arxiv paper is from March 7, 2026 (arxiv ID: 2602.00919).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fe87c58-8cb8-4091-94e8-c488d9b37254",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "a15a7f79-c04c-4465-aa30-e7d1ced35046",
  "sourceToolAssistantUUID": "2fe87c58-8cb8-4091-94e8-c488d9b37254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T19:40:28.026Z_

<details><summary>↩ Tool result · `toolu_01LgUBBV96WNcZy3swF8KdL2`</summary>

```text
Web search results for query: ""optimal discriminator weighted imitation" reinforcement learning arxiv 2504.13368"

Links: [{"title":"[2504.13368] An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://arxiv.org/abs/2504.13368"},{"title":"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://arxiv.org/html/2504.13368"},{"title":"Imitation Learning from Suboptimal Demonstrations via Meta-Learning An Action Ranker","url":"https://arxiv.org/html/2412.20193v1"},{"title":"AN OPTIMAL DISCRIMINATOR WEIGHTED IMITATION ...","url":"https://openreview.net/pdf/599e783547a2ce1b35d5540a0162a0641b26f45b.pdf"},{"title":"[2207.10050] Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/abs/2207.10050"},{"title":"[2207.10050v1] Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/abs/2207.10050v1"},{"title":"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=9JtG4nN7ql"},{"title":"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/3ef61f7e4afacf9a2c5b71c726172b86-Abstract-Conference.html"},{"title":"Discriminator-Weighted Ofﬂine Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/pdf/2207.10050"},{"title":"Discriminator-Weighted Offline Imitation Learning from ...","url":"https://proceedings.mlr.press/v162/xu22l/xu22l.pdf"}]

The search results show that Iterative Dual Reinforcement Learning (IDRL) is a new method that takes an optimal discriminator-weighted imitation view of solving RL.

Here are the key findings about this arXiv paper (2504.13368):

**Core Contribution:**
The method is motivated by a simple experiment in which training a discriminator using the offline dataset plus an additional expert dataset and then performing discriminator-weighted behavior cloning gives strong results on various types of datasets.

**Key Insight:**
The optimal discriminator weight is quite similar to the learned visitation distribution ratio in Dual-RL, however, current Dual-RL methods do not correctly estimate that ratio.

**Proposed Solution:**
IDRL proposes a correction method to iteratively approach the optimal visitation distribution ratio in the offline dataset given no additional expert dataset. During each iteration, IDRL removes zero-weight suboptimal transitions using the learned ratio from the previous iteration and runs Dual-RL on the remaining subdataset.

**Publication Status:**
The paper is part of the International Conference on Representation Learning 2025 (ICLR 2025), with submission date of April 17, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22cf9e5a-2f4e-4c5c-b03e-7becba9c44dc",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "46a72e98-cd9f-4ce2-bb3f-a92ee3134dda",
  "sourceToolAssistantUUID": "22cf9e5a-2f4e-4c5c-b03e-7becba9c44dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-13T19:40:28.984Z_

<details><summary>↩ Tool result · `toolu_01VZUa4RJoZg5QxHQJh9Uez3`</summary>

```text
Web search results for query: "VLA-OPD on-policy distillation offline SFT online RL VLA 2026"

Links: [{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666v1"},{"title":"[2603.26666] VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/abs/2603.26666"},{"title":"Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe","url":"https://arxiv.org/html/2605.03677"},{"title":"[2604.13010] Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation","url":"https://arxiv.org/abs/2604.13010"},{"title":"Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation","url":"https://arxiv.org/html/2604.13010"},{"title":"Rethinking On-Policy Distillation 2026-04-15","url":"https://arxiv.org/pdf/2604.13016"},{"title":"SOD: Step-wise On-policy Distillation for Small Language Model Agents","url":"https://arxiv.org/html/2605.07725"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"[2604.13010v1] Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation","url":"https://arxiv.org/abs/2604.13010v1"},{"title":"(PDF) Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe","url":"https://www.researchgate.net/publication/404476798_Uni-OPD_Unifying_On-Policy_Distillation_with_a_Dual-Perspective_Recipe"}]

I found highly relevant results for your search. Here's what the research shows:

## VLA-OPD: Bridging Offline SFT and Online RL

VLA-OPD is a unified post-training framework that bridges SFT and RL for Vision-Language-Action models. 

### Key Problem It Addresses

Standard offline Supervised Fine-Tuning (SFT) suffers from distribution shifts and catastrophic forgetting of pre-trained capabilities, while online Reinforcement Learning (RL) struggles with sparse rewards and poor sample efficiency.

### Solution Approach

VLA-OPD is a framework bridging the efficiency of SFT with the robustness of RL, leveraging an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories.

The distillation paradigm decouples the computationally prohibitive process of RL exploration from the student's policy optimization, and capitalizes on existing expert resources by providing a highly sample-efficient distillation pipeline that enables seamless transfer of robust behaviors from diverse teachers into new, upgraded, or unified generalist student backbones.

### Technical Innovation

Unlike standard Forward-KL that induces mode-covering entropy explosion, or Hard-CE that causes premature entropy collapse, the bounded mode-seeking objective ensures stable policy learning by filtering out the teacher's epistemic uncertainty while maintaining action diversity.

### Experimental Results

Experiments on LIBERO and RoboTwin2.0 benchmarks demonstrate that VLA-OPD significantly improves sample efficiency over RL and robustness over SFT, while effectively mitigating catastrophic forgetting during post-training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69ccfd82-f721-4f43-b7f0-49114d689d64",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "f9a8cb0c-5532-4307-a213-884423650df7",
  "sourceToolAssistantUUID": "69ccfd82-f721-4f43-b7f0-49114d689d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T19:40:30.971Z_

<details><summary>↩ Tool result · `toolu_013jiyekKqaXw5uCdTXQpXd9`</summary>

```text
Web search results for query: ""data retrieval importance weights few-shot imitation learning" arxiv 2509.01657"

Links: [{"title":"[2509.01657] Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://arxiv.org/abs/2509.01657"},{"title":"Data Retrieval with Importance Weights for Few-Shot Imitation Learning","url":"https://arxiv.org/html/2509.01657"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2406.01657"},{"title":"[2506.01657] State Similarity in Modular Superconducting Quantum Processors with Classical Communications","url":"https://arxiv.org/abs/2506.01657"},{"title":"[2511.01657] Measurement Strategies and Estimation Precision in Quantum Network Tomography","url":"https://arxiv.org/abs/2511.01657"},{"title":"[2604.01657] What Do Claim Verification Datasets Actually Test? A Reasoning Trace Analysis","url":"https://arxiv.org/abs/2604.01657"},{"title":"[2102.01657] Construction of Nahm data and BPS monopoles with continuous symmetries","url":"https://arxiv.org/abs/2102.01657"},{"title":"arXiv:2505.01657v1 [cs.IR] 3 May 2025","url":"https://arxiv.org/pdf/2505.01657"},{"title":"[2503.01657] Nonparanormal Adjusted Marginal Inference","url":"https://arxiv.org/abs/2503.01657"},{"title":"[2502.01657] Improving Rule-based Reasoning in LLMs using Neurosymbolic Representations","url":"https://arxiv.org/abs/2502.01657"}]

I found the paper you're looking for! The arxiv paper 2509.01657 is titled "Data Retrieval with Importance Weights for Few-Shot Imitation Learning".

Here's a summary of the paper:

While large-scale robot datasets have propelled recent progress in imitation learning, learning from smaller task-specific datasets remains critical for deployment in new environments and unseen tasks. One approach to few-shot imitation learning is retrieval-based imitation learning, which extracts relevant samples from large, widely available prior datasets to augment a limited demonstration dataset.

Retrieval-based approaches most commonly calculate a prior data point's minimum distance to a point in the target dataset in latent space. While retrieval-based methods have shown success using this metric for data selection, the paper demonstrates its equivalence to the limit of a Gaussian kernel density (KDE) estimate of the target data distribution.

The paper was submitted in September 2025 and appears to address limitations in how prior work selects relevant data for few-shot imitation learning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e75cc1a6-20a8-4c9a-84a3-c0f45abbf01b",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "69517ea8-1794-48cc-9247-0e8c4a8cc6f3",
  "sourceToolAssistantUUID": "e75cc1a6-20a8-4c9a-84a3-c0f45abbf01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-13T19:40:34.357Z_

Let me run a few final targeted searches for the most recent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69517ea8-1794-48cc-9247-0e8c4a8cc6f3",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18rJLTeWtsTJ3JeQREX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc91155d-3086-47bf-b3b2-1b267599d4db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4DyzfroGsRs3RQAQxdtv4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1845,
      "cache_creation_input_tokens": 2663,
      "cache_read_input_tokens": 21879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2663,
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

_source line 44 · 2026-05-13T19:40:35.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P2UvEdEB9z5iAXkQfsPNW5`</summary>

```json
{
  "query": "\"What Matters in Learning from Large-Scale Datasets for Robot Manipulation\" arxiv 2506"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc91155d-3086-47bf-b3b2-1b267599d4db",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18rJLTeWtsTJ3JeQREX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12cb31b1-f9d0-48d5-85c8-c574284fe12d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4DyzfroGsRs3RQAQxdtv4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1845,
      "cache_creation_input_tokens": 2663,
      "cache_read_input_tokens": 21879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2663,
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

_source line 45 · 2026-05-13T19:40:36.243Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X4DBvkA5Pr88TuiVYdxxW5`</summary>

```json
{
  "query": "pragmatic VLA foundation model data curation 2601.18692 arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12cb31b1-f9d0-48d5-85c8-c574284fe12d",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18rJLTeWtsTJ3JeQREX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b77dc42-22d0-4ffa-a546-5d46c38fd420",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4DyzfroGsRs3RQAQxdtv4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1845,
      "cache_creation_input_tokens": 2663,
      "cache_read_input_tokens": 21879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2663,
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

_source line 46 · 2026-05-13T19:40:37.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HwZmFfoYMox8hxK49zzWoY`</summary>

```json
{
  "query": "consistency matters demonstration data quality metrics robot learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b77dc42-22d0-4ffa-a546-5d46c38fd420",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18rJLTeWtsTJ3JeQREX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f45ad6d8-2eeb-4523-b095-f5cc7ead1967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4DyzfroGsRs3RQAQxdtv4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1845,
      "cache_creation_input_tokens": 2663,
      "cache_read_input_tokens": 21879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2663,
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

_source line 47 · 2026-05-13T19:40:37.892Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HzzVZfL5MFsx4YX78uAhgt`</summary>

```json
{
  "query": "SimpleVLA-RL scaling VLA training reinforcement learning ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f45ad6d8-2eeb-4523-b095-f5cc7ead1967",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18rJLTeWtsTJ3JeQREX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a42e8e69-276a-42b7-9faf-a80a954b5df2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4DyzfroGsRs3RQAQxdtv4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1845,
      "cache_creation_input_tokens": 2663,
      "cache_read_input_tokens": 21879,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2663
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1845,
          "output_tokens": 245,
          "cache_read_input_tokens": 21879,
          "cache_creation_input_tokens": 2663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2663,
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

_source line 48 · 2026-05-13T19:40:42.119Z_

<details><summary>↩ Tool result · `toolu_01P2UvEdEB9z5iAXkQfsPNW5`</summary>

```text
Web search results for query: ""What Matters in Learning from Large-Scale Datasets for Robot Manipulation" arxiv 2506"

Links: [{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://arxiv.org/html/2506.13536v1"},{"title":"[2506.13536] What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://arxiv.org/abs/2506.13536"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250613536S/abstract"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://robo-mimiclabs.github.io/"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=LqhorpRLIm"},{"title":"ARMADA: Autonomous Online Failure Detection and Human Shared Control Empower Scalable Real-world Deployment and Adaptation","url":"https://arxiv.org/html/2510.02298v1"},{"title":"Robotics Jun 2025","url":"https://arxiv.org/list/cs.RO/2025-06?skip=350&show=250"},{"title":"(PDF) What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://www.researchgate.net/publication/392736873_What_Matters_in_Learning_from_Large-Scale_Datasets_for_Robot_Manipulation"},{"title":"Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation","url":"https://arxiv.org/html/2503.24361v2"},{"title":"[Literature Review] What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://www.themoonlight.io/en/review/what-matters-in-learning-from-large-scale-datasets-for-robot-manipulation"}]

I found the paper! Here's information about "What Matters in Learning from Large-Scale Datasets for Robot Manipulation" (arXiv 2506.13536):

## Overview

The paper addresses the gap in systematic understanding of what data should be collected to improve the utility of robotics datasets for imitation learning from large multi-task demonstration datasets.

## Methodology

The authors developed a data generation framework to procedurally emulate common sources of diversity in existing datasets such as sensor placements and object types and arrangements, enabling dataset composition studies that would be prohibitively expensive in the real world.

## Key Findings

The research identifies several important dimensions of variation (DVs) for dataset composition:

- **Camera Pose**: Camera pose alignment and diversity significantly impact performance, with aligning camera poses in retrieved datasets substantially boosting transfer learning by providing relevant examples for target viewpoints. When perfect alignment is impossible, high diversity in camera poses can still improve performance by preventing overfitting to specific hand-eye coordinations.

- **Object Texture**: Object texture has limited impact in retrieval, as it did not matter for either alignment or diversity.

- **Spatial Arrangement**: Spatial arrangement alignment and diversity are crucial for performance, as aligning spatial arrangements between co-training and target datasets significantly boosts downstream performance.

## Publication

The paper was published as a conference paper at ICLR 2025 by Vaibhav Saxena, Matthew Bronars, and colleagues from Georgia Institute of Technology, University of Texas at Austin, and NVIDIA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12cb31b1-f9d0-48d5-85c8-c574284fe12d",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "5b5d0cff-7ae7-4d27-89b7-020250855880",
  "sourceToolAssistantUUID": "12cb31b1-f9d0-48d5-85c8-c574284fe12d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-13T19:40:45.410Z_

<details><summary>↩ Tool result · `toolu_01HwZmFfoYMox8hxK49zzWoY`</summary>

```text
Web search results for query: "consistency matters demonstration data quality metrics robot learning 2024 2025"

Links: [{"title":"Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration","url":"https://arxiv.org/html/2412.14309v1"},{"title":"[2412.14309] Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration","url":"https://arxiv.org/abs/2412.14309"},{"title":"Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration | ACM Transactions on Human-Robot Interaction","url":"https://dl.acm.org/doi/abs/10.1145/3773904"},{"title":"Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration | Request PDF","url":"https://www.researchgate.net/publication/396997300_Consistency_Matters_Defining_Demonstration_Data_Quality_Metrics_in_Robot_Learning_from_Demonstration"},{"title":"(PDF) Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration","url":"https://www.researchgate.net/publication/387222678_Consistency_Matters_Defining_Demonstration_Data_Quality_Metrics_in_Robot_Learning_from_Demonstration"},{"title":"Maram Sakr's research works","url":"https://www.researchgate.net/scientific-contributions/Maram-Sakr-2329156489"},{"title":"Beyond Success: Quantifying Demonstration Quality in Learning from","url":"https://wafa.johal.org/files/papers/bilal2024.pdf"},{"title":"Quantifying Demonstration Quality for Robot Learning and Generalization","url":"https://arxiv.org/pdf/2203.13843"},{"title":"Robotics Dec 2024","url":"https://arxiv.org/list/cs.RO/2024-12?skip=350&show=500"},{"title":"Human-Computer Interaction Dec 2024","url":"https://arxiv.org/list/cs.HC/2024-12?skip=325&show=25"}]

The search results reveal a significant research paper on this topic. Here's what I found:

## Key Research Finding

A study titled "Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration" found that demonstration consistency significantly impacts success rates in both learning and generalization, with 70% and 89% of task success rates in two studies predicted using consistency metrics, and the metrics estimated generalized performance success rates with 76% and 91% accuracy.

## Research Overview

Learning from Demonstration (LfD) enables robots to acquire new skills through human demonstrations, making it feasible for everyday users to teach robots. However, the success of learning and generalization heavily depends on the quality of demonstrations, and while consistency is often used to indicate quality in LfD, the factors that define this consistency remain underexplored.

## Methodology

The research was validated with two user studies involving participants with diverse levels of robotics expertise. In the first study (N = 24), users taught a PR2 robot to perform a button-pressing task in a constrained environment, while in the second study (N = 30), participants trained a UR5 robot on a pick-and-place task.

## Practical Impact

The findings suggest that the proposed measures provide an intuitive, practical way to assess demonstration data quality before training, without requiring expert data or algorithm-specific modifications, offering a systematic way to evaluate demonstration quality and addressing a critical gap in LfD by formalizing consistency metrics.

This research was published in December 2024 in the ACM Transactions on Human-Robot Interaction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f45ad6d8-2eeb-4523-b095-f5cc7ead1967",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "3df6c714-c496-4117-9390-6eaeab8e40d4",
  "sourceToolAssistantUUID": "f45ad6d8-2eeb-4523-b095-f5cc7ead1967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-13T19:40:45.611Z_

<details><summary>↩ Tool result · `toolu_01HzzVZfL5MFsx4YX78uAhgt`</summary>

```text
Web search results for query: "SimpleVLA-RL scaling VLA training reinforcement learning ICLR 2026"

Links: [{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"ICLR Poster SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://iclr.cc/virtual/2026/poster/10009314"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"Activity · PRIME-RL/SimpleVLA-RL","url":"https://github.com/PRIME-RL/SimpleVLA-RL/activity"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"},{"title":"PRIME-RL · GitHub","url":"https://github.com/PRIME-RL"},{"title":"SIMPLEVLA-RL: SCALING VLA TRAINING VIA RE","url":"https://openreview.net/pdf/ec4796d06d4fb6583b2800d1782e89edf90d594e.pdf"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"Issues · PRIME-RL/SimpleVLA-RL","url":"https://github.com/PRIME-RL/SimpleVLA-RL/issues"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement ...","url":"https://arxiv.org/pdf/2509.09674"}]

Based on the search results, here's what I found about SimpleVLA-RL:

## Overview

SimpleVLA-RL is an efficient RL framework tailored for VLA models. SimpleVLA-RL is an efficient RL framework for VLA that improves long-horizon planning under data scarcity.

## Research Motivation

VLA models face challenges including the scarcity and high cost of large-scale robotic trajectories required for SFT scaling, and limited generalization to tasks under distribution shift. To overcome these limitations, the framework explores reinforcement learning (RL) as a pathway to scaling VLA training beyond limited datasets.

## Key Technical Components

Building upon veRL, the framework introduces VLA-specific trajectory sampling, scalable parallelization, multi-environment rendering, and optimized loss computation.

## Performance Results

Applied to OpenVLA-OFT, SimpleVLA-RL achieves 99% of SoTA performance on LIBERO and 80% relative improvement on RoboTwin 1.0&2.0, outperforming π0 with exploration-enhancing strategies. Additionally, using only one trajectory per task for cold-start SFT, SimpleVLA-RL raises the performance of OpenVLA-OFT from 17.3 to 91.7, yielding an improvement of 74.4 points (430.1%).

## Novel Discovery

The researchers identified a novel phenomenon "pushcut" during RL training, wherein the policy discovers unseen patterns beyond those seen in previous training process.

The paper was presented at ICLR 2026 and has code available on GitHub at PRIME-RL/SimpleVLA-RL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a42e8e69-276a-42b7-9faf-a80a954b5df2",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "66f930f6-fb54-4376-8804-0367a9de310b",
  "sourceToolAssistantUUID": "a42e8e69-276a-42b7-9faf-a80a954b5df2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-13T19:40:46.712Z_

<details><summary>↩ Tool result · `toolu_01X4DBvkA5Pr88TuiVYdxxW5`</summary>

```text
Web search results for query: "pragmatic VLA foundation model data curation 2601.18692 arxiv 2026"

Links: [{"title":"[2601.18692] A Pragmatic VLA Foundation Model","url":"https://arxiv.org/abs/2601.18692"},{"title":"A Pragmatic VLA Foundation Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260118692W/abstract"},{"title":"Paper page - A Pragmatic VLA Foundation Model","url":"https://huggingface.co/papers/2601.18692"},{"title":"robbyant/lingbot-vla-4b · Hugging Face","url":"https://huggingface.co/robbyant/lingbot-vla-4b"},{"title":"A Pragmatic VLA Foundation Model | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.18692"},{"title":"VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model","url":"https://arxiv.org/pdf/2602.10098"},{"title":"GraspVLA: a Grasping Foundation Model","url":"https://arxiv.org/pdf/2505.03233v1"},{"title":"[Quick Review] A Pragmatic VLA Foundation Model","url":"https://liner.com/review/pragmatic-vla-foundation-model"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"}]

I found the arxiv paper you're looking for! Here's what I found:

## A Pragmatic VLA Foundation Model (arXiv:2601.18692)

This paper develops LingBot-VLA, a Vision-Language-Action (VLA) foundation model designed to generalize across robotic manipulation tasks and platforms while ensuring cost efficiency in terms of data and GPU hours required for adaptation.

**Data Curation:**
The model was developed using around 20,000 hours of real-world data from 9 popular dual-arm robot configurations. This research emphasizes the value of extensive real-world data for large-scale data curation efforts.

**Performance and Results:**
Through systematic assessment on 3 robotic platforms, each completing 100 tasks with 130 post-training episodes per task, the model achieves clear superiority over competitors, showcasing strong performance and broad generalizability.

**Efficiency:**
The researchers built an efficient codebase that delivers a throughput of 261 samples per second with an 8-GPU training setup, representing a 1.5~2.8x speedup over existing VLA-oriented codebases.

The paper was submitted on January 26, 2026, with a revised version on February 26, 2026. You can access it at https://arxiv.org/abs/2601.18692


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b77dc42-22d0-4ffa-a546-5d46c38fd420",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "af6755c1db562422f",
  "type": "user",
  "uuid": "14c4b787-cf43-4cf2-b9b3-ff43984960e6",
  "sourceToolAssistantUUID": "5b77dc42-22d0-4ffa-a546-5d46c38fd420",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-13T19:42:08.355Z_

Here is a comprehensive report of recent work (2025-2026) on data curation/filtering for Vision-Language-Action (VLA) models, organized by relevance to density-ratio weighted behavioral cloning for VLA training.

---

## HIGHLY RELEVANT: Direct Data Weighting/Filtering for Imitation Learning

### 1. Quality over Quantity (QoQ) -- March 2026
- **Title**: "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning"
- **Venue/Status**: arXiv preprint, March 2026 (arxiv:2603.09056)
- **Authors**: Haeone Lee, Taywon Min, Junsu Kim, et al. (KAIST, UC Berkeley, NYU)
- **What it does**: Defines data quality as the contribution of each training sample to reducing loss on validation demonstrations. Uses trajectory-wise curation that aggregates influence scores of state-action pairs within the same trajectory, then selects high-quality trajectories. This reduces noise in the influence signal while ensuring broad state coverage.
- **Relation to density-ratio weighted BC**: This is a close alternative to density-ratio weighting. Instead of re-weighting by a density ratio, it uses influence functions to score each demonstration's contribution. Both approaches aim to up-weight good data and down-weight harmful data, but QoQ uses a loss-reduction criterion rather than a distributional one. Could be a strong baseline or complementary method.

### 2. CUPID -- June 2025 (CoRL 2025)
- **Title**: "CUPID: Curating Data your Robot Loves with Influence Functions"
- **Venue/Status**: CoRL 2025 (accepted), arXiv:2506.19121
- **What it does**: Estimates the influence of each training demonstration on the policy's expected return via influence functions. Curates data by (1) filtering out demonstrations that harm policy performance and (2) sub-selecting newly collected trajectories that will most improve the policy. Training with less than 33% of curated data can yield SOTA diffusion policies on RoboMimic.
- **Relation to density-ratio weighted BC**: A predecessor/parallel approach to QoQ. Like density-ratio methods, it provides per-demonstration importance scores, but derived from influence functions on downstream returns rather than density ratios. The two approaches could be combined (density-ratio as a cheaper proxy for influence).

### 3. IDRL (Iterative Dual RL) -- April 2025 (ICLR 2025)
- **Title**: "An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning"
- **Venue/Status**: ICLR 2025, arXiv:2504.13368
- **What it does**: Shows that the optimal discriminator weight in discriminator-weighted BC is closely related to the visitation distribution ratio in Dual-RL. Proposes iteratively removing zero-weight suboptimal transitions and re-running Dual-RL on the remaining data, approaching the optimal visitation distribution ratio without an additional expert dataset.
- **Relation to density-ratio weighted BC**: This is directly relevant -- it formally connects discriminator-weighted BC to density ratio estimation and proposes an iterative refinement of the ratio estimate. It provides theoretical grounding for why density-ratio weighting works and how to improve it iteratively.

### 4. Discriminator-Weighted Offline IL for Robotic Tasks -- June 2025
- **Title**: "Discriminator-weighted offline imitation learning with unlabeled demonstrations for robotic tasks"
- **Venue/Status**: Journal of the Chinese Institute of Engineers, Vol 48(6), pp. 718-731, June 2025
- **What it does**: Extends DWBC (discriminator-weighted behavioral cloning) to robotic tasks with unlabeled demonstrations. Introduces a discriminator to analytically weigh all data to distinguish between optimal and suboptimal instances, without requiring manual labeling or environmental interaction.
- **Relation to density-ratio weighted BC**: This is essentially an application of discriminator-weighted BC (which is a form of density-ratio weighting) to robotic tasks. Directly validates the approach in a robotics context with mixed-quality, unlabeled data.

### 5. Data Retrieval with Importance Weights -- September 2025
- **Title**: "Data Retrieval with Importance Weights for Few-Shot Imitation Learning"
- **Venue/Status**: arXiv:2509.01657
- **What it does**: Shows that the common retrieval metric (minimum distance in latent space) is equivalent to the limit of a Gaussian kernel density estimate. Proposes importance-weighted retrieval from large prior datasets to augment limited demonstration datasets.
- **Relation to density-ratio weighted BC**: Directly connects data retrieval/selection to density estimation. The importance weights used for retrieval are conceptually related to density ratios -- both identify which data points from a large pool are most relevant for the target task distribution.

---

## HIGHLY RELEVANT: VLA-Specific Data Quality and RL Fine-Tuning

### 6. Green-VLA with DataQA Pipeline -- February 2026
- **Title**: "Green-VLA" (Staged VLA framework)
- **Venue/Status**: arXiv:2602.00919, February/March 2026
- **What it does**: Introduces the DataQA pipeline for robotic dataset curation and quality assessment. Filters and smooths heterogeneous demonstrations and aligns temporal dynamics via optical flow-based resampling. Combines large-scale open datasets (AgibotWorld, DROID, Galaxea) with internally collected data. Shows large gains after RL alignment, especially on long-horizon tasks.
- **Relation to density-ratio weighted BC**: DataQA is a rule-based/heuristic curation pipeline, whereas density-ratio weighting is a learned, principled approach. Density-ratio methods could replace or augment the hand-designed filtering rules in DataQA with data-driven weighting.

### 7. ReinboT -- May 2025 (ICML 2025)
- **Title**: "ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning"
- **Venue/Status**: ICML 2025, arXiv:2505.07395
- **What it does**: Integrates RL into VLA training to handle variable data quality. Predicts dense returns that capture manipulation task nuances, enabling the model to understand the data quality distribution. Decomposes long-horizon trajectories into segments with single sub-goals with dense rewards.
- **Relation to density-ratio weighted BC**: ReinboT addresses the same problem (variable training data quality) but through RL and dense return prediction rather than density-ratio weighting. The dense return prediction could potentially be combined with density-ratio methods -- using predicted returns to inform the "expert" distribution in the ratio.

### 8. VLA-RFT -- October 2025
- **Title**: "VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators"
- **Venue/Status**: arXiv:2510.00406
- **What it does**: Uses a data-driven world model as a simulator for RL fine-tuning of VLAs. Achieves strong results with fewer than 400 fine-tuning steps. However, the reward signal is still constrained by expert demonstration quality.
- **Relation to density-ratio weighted BC**: VLA-RFT's limitation (being constrained by expert data quality) is exactly where density-ratio weighting could help -- by pre-filtering the expert dataset used to define rewards, or by weighting the world model training data.

### 9. VLA-OPD -- March 2026
- **Title**: "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation"
- **Venue/Status**: arXiv:2603.26666, March 2026
- **What it does**: Bridges SFT and RL via on-policy distillation from an expert teacher. Uses a bounded mode-seeking objective that filters out teacher epistemic uncertainty while maintaining action diversity. Addresses distribution shift and catastrophic forgetting.
- **Relation to density-ratio weighted BC**: The mode-seeking objective that filters teacher uncertainty is conceptually related to density-ratio weighting -- both aim to selectively use training signal. Density-ratio methods could potentially be used to weight the distillation loss.

### 10. SimpleVLA-RL -- ICLR 2026
- **Title**: "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning"
- **Venue/Status**: ICLR 2026, arXiv:2509.09674
- **What it does**: Efficient RL framework for VLAs. Achieves 99% SOTA on LIBERO and 80% relative improvement on RoboTwin. With only 1 trajectory per task for cold-start SFT, raises performance from 17.3 to 91.7. Discovers novel "pushcut" patterns beyond training data.
- **Relation to density-ratio weighted BC**: Demonstrates that RL can compensate for limited/poor SFT data. Density-ratio weighted BC could serve as a better initialization for RL fine-tuning by producing a higher-quality SFT policy to start from.

---

## MODERATELY RELEVANT: Data Quality Metrics and Benchmarking

### 11. Consistency Matters -- December 2024
- **Title**: "Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration"
- **Venue/Status**: ACM Transactions on Human-Robot Interaction, arXiv:2412.14309
- **What it does**: Formalizes consistency metrics for demonstration quality. Predicts 70-89% of task success rates using consistency metrics alone. Provides an intuitive, pre-training way to assess demonstration quality without requiring expert data.
- **Relation to density-ratio weighted BC**: These consistency metrics could serve as features for the density-ratio estimator, or as an independent pre-filtering step before applying density-ratio weighting.

### 12. What Matters in Learning from Large-Scale Datasets -- June 2025 (ICLR 2025)
- **Title**: "What Matters in Learning from Large-Scale Datasets for Robot Manipulation"
- **Venue/Status**: ICLR 2025, arXiv:2506.13536
- **What it does**: Systematic study of what data dimensions of variation matter (camera pose alignment/diversity, spatial arrangement, object texture). Finds camera pose and spatial arrangement alignment are critical; object texture is not.
- **Relation to density-ratio weighted BC**: Identifies which data characteristics matter most. Density-ratio methods could implicitly learn these factors, but this work suggests that explicit alignment of camera poses and spatial arrangements may be at least as important as quality-based weighting.

### 13. LingBot-VLA (A Pragmatic VLA Foundation Model) -- January 2026
- **Title**: "A Pragmatic VLA Foundation Model"
- **Venue/Status**: arXiv:2601.18692, January 2026
- **What it does**: VLA foundation model trained on ~20,000 hours of real-world data from 9 dual-arm robot configurations. Emphasizes cost efficiency in data collection and GPU hours for adaptation. Achieves 261 samples/sec throughput with 8-GPU setup.
- **Relation to density-ratio weighted BC**: At this scale of data (~20K hours), data curation becomes essential. Density-ratio weighting could help identify which portions of this massive dataset are most valuable for specific downstream tasks.

---

## KEY COMMUNITY EVENTS

### ICRA 2026 Workshop: "From Data to Decisions: VLA Pipelines for Real Robots"
- **Date**: June 1-5, 2026, Vienna, Austria
- **Organizer**: AI Robotic Association (AIRoA)
- **Significance**: Competition on VLA pipelines with 10,000+ hours of data. Explicitly focuses on the gap between data collection, curation, training, and evaluation. This is the premier venue for data-centric VLA work in 2026.

---

## SUMMARY OF GAPS AND OPPORTUNITIES

The most directly relevant papers to density-ratio weighted BC for VLA training are:

1. **IDRL (ICLR 2025)** -- provides the theoretical connection between discriminator-weighted BC and density ratio estimation
2. **DWBC for robotic tasks (JCIE 2025)** -- validates discriminator-weighted BC in robotics
3. **QoQ and CUPID (2026 and CoRL 2025)** -- demonstrate influence-function-based alternatives that achieve strong results with aggressive data filtering

The key observation is that while influence-function methods (CUPID, QoQ) have gained traction, density-ratio estimation has been underexplored specifically for VLA models. The RL fine-tuning line (SimpleVLA-RL, VLA-RFT, VLA-OPD, ReinboT) addresses data quality indirectly through RL, but none of these directly apply density-ratio weighting to the SFT/BC stage. This represents a clear gap and opportunity.

Sources:
- [Quality over Quantity (QoQ)](https://arxiv.org/abs/2603.09056)
- [CUPID](https://arxiv.org/abs/2506.19121)
- [IDRL - Optimal Discriminator Weighted Imitation](https://arxiv.org/abs/2504.13368)
- [DWBC for Robotic Tasks](https://www.tandfonline.com/doi/full/10.1080/02533839.2025.2517354)
- [Data Retrieval with Importance Weights](https://arxiv.org/abs/2509.01657)
- [Green-VLA / DataQA](https://arxiv.org/html/2602.00919)
- [ReinboT](https://arxiv.org/abs/2505.07395)
- [VLA-RFT](https://arxiv.org/abs/2510.00406)
- [VLA-OPD](https://arxiv.org/abs/2603.26666)
- [SimpleVLA-RL](https://arxiv.org/abs/2509.09674)
- [Consistency Matters](https://arxiv.org/abs/2412.14309)
- [What Matters in Large-Scale Datasets](https://arxiv.org/abs/2506.13536)
- [LingBot-VLA](https://arxiv.org/abs/2601.18692)
- [ICRA 2026 VLA Workshop](https://icra2026vlapipeline.github.io/)
- [VLA Datasets Survey](https://arxiv.org/html/2604.23001v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14c4b787-cf43-4cf2-b9b3-ff43984960e6",
  "isSidechain": true,
  "agentId": "af6755c1db562422f",
  "requestId": "req_011Cb18sSTeAViGEuzYQLKjR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7238062a-b4dc-4cf4-9c44-2d1b630b194e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnH1wcYXLD2GyWJhgnE8r4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1831,
      "cache_creation_input_tokens": 3754,
      "cache_read_input_tokens": 24542,
      "output_tokens": 3542,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3754
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1831,
          "output_tokens": 3542,
          "cache_read_input_tokens": 24542,
          "cache_creation_input_tokens": 3754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3754,
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
