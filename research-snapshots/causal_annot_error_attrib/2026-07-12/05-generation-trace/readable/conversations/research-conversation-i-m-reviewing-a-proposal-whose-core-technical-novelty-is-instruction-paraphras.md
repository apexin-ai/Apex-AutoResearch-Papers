# Research conversation: I'm reviewing a proposal whose core technical novelty is "Instruction-Paraphrase Affordance Consistency" (IPAC) — forcin

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac9b50b1441f2ff22.jsonl`
- **Structured JSON:** [`c9e91dd97f99cdcc0b74.json`](../../sessions/c9/c9e91dd97f99cdcc0b74.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-18T19:23:04.000Z_

I'm reviewing a proposal whose core technical novelty is "Instruction-Paraphrase Affordance Consistency" (IPAC) — forcing a robot learning model to produce identical affordance maps for paraphrased instructions (e.g., "grab the mug handle" vs "grasp the cup by its handle"). This is claimed as a novel self-supervised training objective for VLAs.

Search thoroughly for prior work on:
1. "instruction paraphrase consistency" robot learning
2. "paraphrase invariance" robot policy OR VLA
3. "instruction augmentation" robot learning 2024 2025 2026
4. "language robustness" VLA OR "vision language action"
5. "instruction perturbation" imitation learning
6. ST4VLA paraphrase robustness (arXiv 2602.10109)

Also search for:
7. "contrastive instruction" robot manipulation
8. "instruction discriminative" robot learning

I need to know: has anyone already used paraphrase consistency as a training objective in robot learning / VLA / imitation learning? Or is this genuinely novel? Report findings concisely, under 300 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "d6337516-7a3f-4e8a-a74a-6f1d228a1238",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T19:23:04.002Z_

```json
{
  "parentUuid": "d6337516-7a3f-4e8a-a74a-6f1d228a1238",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
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
  "uuid": "df34daa2-ec10-4d53-bfda-1cf59f6c1f17",
  "timestamp": "2026-05-18T19:23:04.002Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T19:23:07.057Z_



I'll search thoroughly across the web for prior work on paraphrase consistency as a training objective in robot learning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df34daa2-ec10-4d53-bfda-1cf59f6c1f17",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAaZgRLaDVxFfmS39UNZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2c5fad0-4a58-4a48-9177-c2e796e845fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011UtqV4rhdVCFDBjxMb9U2s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 818,
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

_source line 4 · 2026-05-18T19:23:07.175Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MS5inApS5VjETnj5bjAW3g`</summary>

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
  "parentUuid": "d2c5fad0-4a58-4a48-9177-c2e796e845fd",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAaZgRLaDVxFfmS39UNZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1298d386-6ba6-4ac0-a95e-dcedb9d60f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011UtqV4rhdVCFDBjxMb9U2s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 8223,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 818
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 818,
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

_source line 5 · 2026-05-18T19:23:07.183Z_

<details><summary>↩ Tool result · `toolu_01MS5inApS5VjETnj5bjAW3g`</summary>

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
  "parentUuid": "1298d386-6ba6-4ac0-a95e-dcedb9d60f7c",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "01e19f1b-bd67-4458-8fed-7df10c524cd4",
  "sourceToolAssistantUUID": "1298d386-6ba6-4ac0-a95e-dcedb9d60f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T19:23:09.791Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01e19f1b-bd67-4458-8fed-7df10c524cd4",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAaZvkoNKT2hfLtP1bqn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77d27ac8-fa96-4cb0-ad22-54da0f7388dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7MCEuHyJfsPmwgW1JYjki",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9041,
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

_source line 7 · 2026-05-18T19:23:10.281Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019QAusHDrtvAJqojuYArCQ4`</summary>

```json
{
  "query": "\"instruction paraphrase consistency\" robot learning VLA affordance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77d27ac8-fa96-4cb0-ad22-54da0f7388dc",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAaZvkoNKT2hfLtP1bqn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b54ba73-9e61-4921-9559-5a93cf8d0520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7MCEuHyJfsPmwgW1JYjki",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9041,
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

_source line 8 · 2026-05-18T19:23:10.910Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gxub4Zfnd8cxMfazGS5TsH`</summary>

```json
{
  "query": "\"paraphrase invariance\" robot policy OR VLA training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b54ba73-9e61-4921-9559-5a93cf8d0520",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAaZvkoNKT2hfLtP1bqn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "417a8276-e66f-44ac-b5c1-7eafea2c728c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7MCEuHyJfsPmwgW1JYjki",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9041,
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

_source line 9 · 2026-05-18T19:23:11.258Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ed9xLd4VPajRd6XtkFJZ8Y`</summary>

```json
{
  "query": "\"instruction augmentation\" robot learning paraphrase 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "417a8276-e66f-44ac-b5c1-7eafea2c728c",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAaZvkoNKT2hfLtP1bqn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01b1fe7f-9c55-4cfc-a407-b41201aa5525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7MCEuHyJfsPmwgW1JYjki",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9041,
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

_source line 10 · 2026-05-18T19:23:11.658Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012s2HRS4MVFuNM7KC7pNBdb`</summary>

```json
{
  "query": "\"language robustness\" VLA OR \"vision language action\" paraphrase"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01b1fe7f-9c55-4cfc-a407-b41201aa5525",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAaZvkoNKT2hfLtP1bqn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e5f487e-7f2c-4e8f-9858-88a1eff51e1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7MCEuHyJfsPmwgW1JYjki",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9041,
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

_source line 11 · 2026-05-18T19:23:12.141Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01436mWUGJQjRh5dxtvP6uca`</summary>

```json
{
  "query": "\"instruction perturbation\" imitation learning consistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e5f487e-7f2c-4e8f-9858-88a1eff51e1f",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAaZvkoNKT2hfLtP1bqn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ea7e605-a409-4f54-9a6f-822165259c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7MCEuHyJfsPmwgW1JYjki",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9041,
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

_source line 12 · 2026-05-18T19:23:12.632Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S9KnEtWUeQZgitVdh9sMJq`</summary>

```json
{
  "query": "ST4VLA paraphrase robustness arXiv 2602.10109"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ea7e605-a409-4f54-9a6f-822165259c6d",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAaZvkoNKT2hfLtP1bqn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "267eaf40-d80f-4f95-8aa8-0e2e70d72670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7MCEuHyJfsPmwgW1JYjki",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9041,
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

_source line 13 · 2026-05-18T19:23:12.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018P2QezzsnzRUnqbg7ESKtT`</summary>

```json
{
  "query": "\"contrastive instruction\" robot manipulation language grounding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "267eaf40-d80f-4f95-8aa8-0e2e70d72670",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAaZvkoNKT2hfLtP1bqn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a51fb73-1ed1-4292-a4ad-190394e2174d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7MCEuHyJfsPmwgW1JYjki",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9041,
      "output_tokens": 410,
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
          "output_tokens": 410,
          "cache_read_input_tokens": 9041,
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

### Tool call

_source line 14 · 2026-05-18T19:23:12.988Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019h9FABNUpicRmxouaCXDom`</summary>

```json
{
  "query": "\"instruction discriminative\" robot learning language conditioned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a51fb73-1ed1-4292-a4ad-190394e2174d",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAaZvkoNKT2hfLtP1bqn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d029f429-edf8-4516-bede-1d8f8f0ed67d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7MCEuHyJfsPmwgW1JYjki",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9041,
      "output_tokens": 410,
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
          "output_tokens": 410,
          "cache_read_input_tokens": 9041,
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

_source line 15 · 2026-05-18T19:23:16.484Z_

<details><summary>↩ Tool result · `toolu_019QAusHDrtvAJqojuYArCQ4`</summary>

```text
Web search results for query: ""instruction paraphrase consistency" robot learning VLA affordance"

Links: [{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"},{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/html/2510.19752v1"},{"title":"[2510.19752] Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.19752"},{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.19752"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01623v1"},{"title":"Learning Instruction-Guided Manipulation Affordance via Large Models for   Embodied Robotic Tasks","url":"https://arxiv.org/pdf/2408.10658"},{"title":"ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency   Policy","url":"https://arxiv.org/pdf/2502.05450"}]

I found several relevant research papers on instruction-guided robot learning, Vision-Language-Action (VLA) models, and affordance learning. Here are the key results:

## Recent Work on VLA and Affordance Learning

LITEN (Learning from Inference-Time Execution) connects a VLA low-level policy to a high-level VLM that conditions on past experiences, allowing it to learn the affordances and capabilities of the low-level VLA.

One approach models robot affordance in the format of natural language as intermediate outputs, which relates directly to instruction consistency. Recent work aligns Chain-of-Thought (CoT) with affordance and trajectory annotations, encouraging the model to learn task-consistent reasoning.

## Instruction-Guided Affordance Learning

IGANet (Instruction-Guided Affordance Net) predicts affordance maps for instruction-guided robotic manipulation tasks and includes a VLM-based data augmentation pipeline that can generate large amounts of training data automatically.

## Consistency in VLA Models

Recent work focuses on utilizing pre-trained VLA models to provide high-quality policy initialization for fine-tuning, which relates to achieving consistency across different instruction formulations.

The search results show active research combining instruction understanding, affordance prediction, and VLA models, with particular emphasis on consistency between reasoning steps and task execution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b54ba73-9e61-4921-9559-5a93cf8d0520",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "c5839f34-a68a-465a-b860-2cbbfbc45c0d",
  "sourceToolAssistantUUID": "7b54ba73-9e61-4921-9559-5a93cf8d0520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T19:23:17.567Z_

<details><summary>↩ Tool result · `toolu_01Gxub4Zfnd8cxMfazGS5TsH`</summary>

```text
Web search results for query: ""paraphrase invariance" robot policy OR VLA training"

Links: [{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"Toward Embodiment Equivariant Vision-Language-Action Policy","url":"https://arxiv.org/pdf/2509.14630"},{"title":"PI-VLA: Adaptive Symmetry-Aware Decision-Making for Long-Horizon Vision–Language–Action Manipulation","url":"https://www.mdpi.com/2073-8994/18/3/394"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting","url":"https://arxiv.org/pdf/2509.22195"},{"title":"A VLA that Learns from Experience","url":"https://www.pi.website/blog/pistar06"},{"title":"Invariance Co-training for Robot Visual Generalization","url":"https://arxiv.org/pdf/2512.05230"}]

I found relevant search results for your query about paraphrase invariance, robot policies, and VLA training. Here are the key findings:

## Paraphrase Robustness in VLA Models

One notable research effort is LIBERO-Para, a diagnostic benchmark for studying paraphrase robustness in VLA models. The research found that because models are fine-tuned exclusively on fixed object references, they are never exposed to lexical variation during training, which reinforces surface-level keyword matching and contributes to sharp performance drops when object nouns are replaced with semantically equivalent alternatives.

## Vision-Language-Action (VLA) Policies

The search results reveal several approaches to improving VLA models:

1. **Embodiment Equivariance**: Vision-language-action (VLA) policies are typically pre-trained on large-scale cross-embodiment datasets spanning diverse tasks and environments, then fine-tuned for specific embodiments and downstream tasks.

2. **Symmetry-Aware Learning**: One framework combines imitation learning, reinforcement learning, and state prediction loss to promote invariance to task-relevant transformations while enabling adaptive behavior beyond pure behavior cloning.

3. **Visual Generalization**: Research investigates how co-training robot policies with large-scale, visually diverse synthetic data can improve generalization along camera perspective, distractor clutter, and lighting variation.

The results show that paraphrase invariance and robustness are active research areas in making VLA models more generalizable and reliable for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "417a8276-e66f-44ac-b5c1-7eafea2c728c",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "d0d1357c-57ed-4892-b722-59b1047a90fc",
  "sourceToolAssistantUUID": "417a8276-e66f-44ac-b5c1-7eafea2c728c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T19:23:18.236Z_

<details><summary>↩ Tool result · `toolu_012s2HRS4MVFuNM7KC7pNBdb`</summary>

```text
Web search results for query: ""language robustness" VLA OR "vision language action" paraphrase"

Links: [{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming","url":"https://arxiv.org/html/2604.05595"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/pdf/2510.00037"},{"title":"LADEV: A Language-Driven Testing and Evaluation Platform for Vision-Language-Action Models in Robotic Manipulation","url":"https://arxiv.org/html/2410.05191"},{"title":"VLA Model (Vision-Language-Action) — Definition & Training Data | Claru","url":"https://claru.ai/glossary/vla"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.01331"}]

I've found several recent research papers on language robustness in Vision-Language-Action (VLA) models. Here are the key findings:

## Paraphrase Robustness in VLA Models

Vision-Language-Action (VLA) models achieve strong performance in robotic manipulation, but when fine-tuned with limited data in downstream robotic settings, they overfit to specific instruction formulations, leaving robustness to paraphrased instructions underexplored.

LIBERO-Para is a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization.

## Broader Robustness Challenges

VLA models have achieved remarkable success in robotic manipulation, but their robustness to linguistic nuances remains a critical, under-explored safety concern.

VLAs remain vulnerable to multi-modal uncertainties including language vulnerabilities like synonymous or ambiguous instructions.

## Testing and Evaluation Platforms

LADEV is a comprehensive platform designed for evaluating VLA models, featuring a language-driven approach that automatically generates simulation environments and a paraphrase mechanism that produces diverse natural language task instructions for testing.

Best practices for improving robustness include augmenting datasets with language paraphrases, camera viewpoint variations, and object substitutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e5f487e-7f2c-4e8f-9858-88a1eff51e1f",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "6d61320d-e35f-4a12-a4ae-a8563a870c01",
  "sourceToolAssistantUUID": "5e5f487e-7f2c-4e8f-9858-88a1eff51e1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T19:23:18.272Z_

<details><summary>↩ Tool result · `toolu_01436mWUGJQjRh5dxtvP6uca`</summary>

```text
Web search results for query: ""instruction perturbation" imitation learning consistency"

Links: [{"title":"[2402.15833] Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/abs/2402.15833"},{"title":"Does Instruction Tuning Make LLMs More Consistent?","url":"https://arxiv.org/pdf/2404.15206"},{"title":"Diff-Control: A Stateful Diffusion-based Policy for Imitation Learning","url":"https://diff-control.github.io/"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/pdf/2402.15833"},{"title":"The Pitfalls of Imitation Learning when Actions are Continuous","url":"https://arxiv.org/pdf/2503.09722"},{"title":"Robust Imitation Learning against Variations in Environment Dynamics","url":"https://arxiv.org/pdf/2206.09314"},{"title":"Prompt Perturbation Consistency Learning for Robust ...","url":"https://aclanthology.org/2024.findings-eacl.91.pdf"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-eacl.91/"},{"title":"Environmental Consistency Modulation of Error Sensitivity During Motor Adaptation is Explicitly Controlled","url":"https://www.biorxiv.org/content/10.1101/528752.full.pdf"}]

The web search returned results related to instruction perturbation, imitation learning, and consistency. Here's what I found:

## Key Results:

**Instruction Tuning and Consistency:**
Research on instruction tuning examines the impact on consistency—the sensitivity of language models to small perturbations in the input—and shows that instruction-tuned LLaMA models become more consistent in their representations and predictions compared to the original model.

**Prompt Perturbation Consistency Learning:**
Prompt Perturbation Consistency Learning (PPCL) works by regularizing the divergence between losses from clean and perturbed samples, and analyzes performance deterioration due to three types of input perturbations: oronyms, synonyms, and paraphrasing.

**Imitation Learning and Perturbations:**
Several papers address robustness in imitation learning:
- A robust imitation learning framework improves robustness when environment dynamics are perturbed by imitating multiple experts in sampled environment dynamics to enhance robustness against general variations in environment dynamics.
- Diff-Control, a diffusion-based policy for imitation learning, utilizes diffusion models to learn action representations, demonstrating improved robustness through a Bayesian formulation.

The search results show active research on how instruction-based systems and imitation learning handle perturbations and maintain consistency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ea7e605-a409-4f54-9a6f-822165259c6d",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "602dfa45-b605-499b-9ac2-d0eb38244806",
  "sourceToolAssistantUUID": "2ea7e605-a409-4f54-9a6f-822165259c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T19:23:18.343Z_

<details><summary>↩ Tool result · `toolu_01S9KnEtWUeQZgitVdh9sMJq`</summary>

```text
Web search results for query: "ST4VLA paraphrase robustness arXiv 2602.10109"

Links: [{"title":"[2602.10109] ST4VLA: Spatially Guided Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.10109"},{"title":"ST4VLA: Spatially Guided Training for Vision-Language-Action Model","url":"https://arxiv.org/html/2602.10109"},{"title":"st4vla: spatially guided training for vision","url":"https://arxiv.org/pdf/2602.10109"},{"title":"Robustness to Modification with Shared Words in Paraphrase   Identification","url":"https://arxiv.org/pdf/1909.02560"},{"title":"[1909.02560] Robustness to Modification with Shared Words in Paraphrase Identification","url":"https://ar5iv.labs.arxiv.org/html/1909.02560"},{"title":"StealthRL: Reinforcement Learning Paraphrase Attacks for Multi-Detector Evasion of AI-Text Detectors","url":"https://arxiv.org/html/2602.08934"},{"title":"ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation","url":"https://arxiv.org/pdf/2603.13788"}]

Based on the search results, I found the paper you're looking for. ST4VLA is a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in vision-language models.

Regarding paraphrase robustness specifically, the model demonstrates stronger generalization to unseen objects and paraphrased instructions, as well as robustness to long-horizon perturbations in real-world settings. More specifically, under highly challenging conditions, such as interference from visually similar distractors, novel object instances, and paraphrased instructions, ST4VLA achieves strong results through spatial pretraining and spatially guided post-training.

ST4VLA includes two stages: spatial grounding pre-training, which equips the VLM with transferable priors via scalable point, box, and trajectory prediction from both web-scale and robot-specific data, and spatially guided action post-training, which encourages the model to produce richer spatial priors to guide action generation via spatial prompting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "267eaf40-d80f-4f95-8aa8-0e2e70d72670",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "beb385da-30e8-4740-b86d-992bfa146c95",
  "sourceToolAssistantUUID": "267eaf40-d80f-4f95-8aa8-0e2e70d72670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T19:23:19.313Z_

<details><summary>↩ Tool result · `toolu_01Ed9xLd4VPajRd6XtkFJZ8Y`</summary>

```text
Web search results for query: ""instruction augmentation" robot learning paraphrase 2024 2025"

Links: [{"title":"Journal of Information Systems Engineering and Management 2025, 10(59s)","url":"https://jisem-journal.com/index.php/journal/article/download/12888/6010/21703"},{"title":"Robotic Skill Acquisition via Instruction Augmentation with   Vision-Language Models","url":"https://arxiv.org/pdf/2211.11736"},{"title":"Object-Centric Instruction Augmentation for Robotic Manipulation","url":"https://arxiv.org/pdf/2401.02814"},{"title":"Editorial: Advances in robots for learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12005985/"},{"title":"How Many Data Samples is an Additional Instruction Worth?","url":"https://arxiv.org/pdf/2203.09161"}]

Based on the search results, I found relevant research on instruction augmentation in robot learning:

Robotic skill acquisition via instruction augmentation involves learning robotic manipulation policies that follow natural language instructions. Traditional methods typically learn from corpora of robot-language data that was either collected with specific tasks in mind or expensively re-labelled by humans with rich language descriptions.

A key approach in this area is using large-scale pretrained vision-language models (VLMs) like CLIP or ViLD as automatic labelers for robot data, effectively importing Internet-scale knowledge into existing datasets to make them useful even for tasks not reflected in their ground truth annotations.

Recent work from 2024 includes using Multi-modal Large Language Models (MLLMs) to weave knowledge of object locations into natural language instructions, and integrating vision-language features from pre-trained MLLMs into policy networks. Robotic manipulator imitation policies trained with these enhanced instructions outperform those relying solely on traditional language instructions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01b1fe7f-9c55-4cfc-a407-b41201aa5525",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "ca372176-9f14-441b-b7a7-84d16430365f",
  "sourceToolAssistantUUID": "01b1fe7f-9c55-4cfc-a407-b41201aa5525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T19:23:19.570Z_

<details><summary>↩ Tool result · `toolu_019h9FABNUpicRmxouaCXDom`</summary>

```text
Web search results for query: ""instruction discriminative" robot learning language conditioned"

Links: [{"title":"Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks","url":"http://ais.informatik.uni-freiburg.de/publications/papers/mees22rsspi.pdf"},{"title":"What Matters in Language Conditioned Robotic Imitation ...","url":"https://arxiv.org/pdf/2204.06252"},{"title":"Robotic Skill Acquisition via Instruction Augmentation with   Vision-Language Models","url":"https://arxiv.org/pdf/2211.11736"},{"title":"[2109.01115] Learning Language-Conditioned Robot Behavior from Offline Data and Crowd-Sourced Annotation","url":"https://arxiv.org/abs/2109.01115"},{"title":"Language-Conditioned Robotic Manipulation with Fast and Slow Thinking","url":"https://arxiv.org/pdf/2401.04181"},{"title":"Learning Language-Conditioned Robot Behavior from ...","url":"https://arxiv.org/pdf/2109.01115"},{"title":"Language-Conditioned Models in AI","url":"https://www.emergentmind.com/topics/language-conditioned-models"},{"title":"CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision","url":"https://clip-rt.github.io/"}]

I've found relevant research on instruction discriminative approaches to robot learning with language conditioning. Here are the key findings:

## Main Concepts

Language-conditioned models are machine learning architectures where external linguistic inputs—ranging from discrete control tokens to full natural language instructions—dynamically modulate or specify the model's behavior, foundational across modern reinforcement learning, robotics, and other application domains.

Discriminative conditioning uses language to modulate the policy, reward, or prediction function at each decision point.

## Key Approaches

**CLIP-RT**: CLIP-RT is a discriminative VLA (vision-language-action) model that predicts language-based motion primitives from a predefined list of motion primitives. The contrastive imitation learning approach optimizes pairwise similarity between language supervision and contextual information (the current scene and language instruction).

**Fast and Slow Thinking Framework**: One approach consists of an instruction discriminator to determine which system should be activated based on the current user's instruction, alongside a slow-thinking system with a fine-tuned vision-language model.

**Language-Conditioned Reward Learning**: Research has developed simple classifiers that predict if a change in state completes a language instruction, providing a language-conditioned reward function for offline multi-task reinforcement learning.

These approaches address the core challenge of symbol grounding—relating language instructions to a robot's onboard perception and actions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d029f429-edf8-4516-bede-1d8f8f0ed67d",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "0c93de00-9e16-4df8-b860-23df549189b2",
  "sourceToolAssistantUUID": "d029f429-edf8-4516-bede-1d8f8f0ed67d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T19:23:23.281Z_

<details><summary>↩ Tool result · `toolu_018P2QezzsnzRUnqbg7ESKtT`</summary>

```text
Web search results for query: ""contrastive instruction" robot manipulation language grounding"

Links: [{"title":"Size-aware Contrastive Imitation Learning for Language- ...","url":"https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_716/paper.pdf"},{"title":"Contrastive Imitation Learning for Language-guided Multi-Task Robotic Manipulation","url":"https://arxiv.org/html/2406.09738v1"},{"title":"Language-Grounded Decoupled Action Representation for Robotic Manipulation","url":"https://arxiv.org/pdf/2603.12967"},{"title":"Visually Grounding Language Instruction for History-Dependent   Manipulation","url":"https://arxiv.org/pdf/2012.08977"},{"title":"CONTRASTIVE REPRESENTATION REGULARIZATION","url":"https://openreview.net/pdf/620347d848a1d02068b859e759f37dd50a4304b9.pdf"},{"title":"Grounding Object Relations in Language-Conditioned Robotic Manipulation   with Semantic-Spatial Reasoning","url":"https://arxiv.org/pdf/2303.17919"}]

I found several relevant research papers on contrastive instruction methods for robot manipulation and language grounding. Here's what the search revealed:

## Key Research Areas

Language-conditioned robotic manipulation requires agents to translate abstract instructions into geometrically consistent actions, with the objective of training robots to perform manipulation tasks specified by natural language instructions, grounded in geometric and perceptual observations.

## Contrastive Approaches

Recent work incorporates contrastive imitation learning (contrastive IL) modules to strengthen vision-language and current-future representations. One approach, SACIL, introduces dual contrastive imitation learning to align linguistic instructions with geometrically consistent actions.

Another framework employs a semantic-guided soft-label contrastive learning objective to align similar action primitives across tasks, with an adaptive weighting strategy that dynamically balances contrastive and imitation objectives.

## Core Challenge

A fundamental challenge is achieving efficient and generalizable alignment among visual, linguistic, and action representations, as a persistent gap remains between high-level semantic instructions and fine-grained motor execution.

These papers demonstrate that contrastive learning methods are being actively applied to improve how robots ground language instructions to actual manipulation behaviors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a51fb73-1ed1-4292-a4ad-190394e2174d",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "6e81e8e3-e8df-4937-ac5a-26f909c3751f",
  "sourceToolAssistantUUID": "3a51fb73-1ed1-4292-a4ad-190394e2174d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-18T19:23:26.541Z_

Let me do a few more targeted searches to specifically check for paraphrase consistency as a *training objective* (not just evaluation) and to look more closely at LIBERO-Para and related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e81e8e3-e8df-4937-ac5a-26f909c3751f",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAab6pZGKrCvi24bPmAu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab671022-ff23-4e0a-be40-ea470c48037a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgmRxXncEowSk2w7tvMS3V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 699,
      "cache_creation_input_tokens": 5026,
      "cache_read_input_tokens": 10458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5026,
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

_source line 24 · 2026-05-18T19:23:27.015Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019HTssHDsKJkMs48ssADqpr`</summary>

```json
{
  "query": "LIBERO-Para paraphrase robustness VLA training objective consistency loss"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab671022-ff23-4e0a-be40-ea470c48037a",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAab6pZGKrCvi24bPmAu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5ad6d27-ea8c-4b54-b3df-bcfb8f516dd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgmRxXncEowSk2w7tvMS3V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 699,
      "cache_creation_input_tokens": 5026,
      "cache_read_input_tokens": 10458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5026,
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

_source line 25 · 2026-05-18T19:23:27.965Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D38GpvNkfnQNwyKw9Upi1F`</summary>

```json
{
  "query": "paraphrase consistency loss training objective robot policy language conditioned 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5ad6d27-ea8c-4b54-b3df-bcfb8f516dd7",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAab6pZGKrCvi24bPmAu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c441894a-4615-4ada-ace2-64cbbdb2bec0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgmRxXncEowSk2w7tvMS3V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 699,
      "cache_creation_input_tokens": 5026,
      "cache_read_input_tokens": 10458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5026,
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

_source line 26 · 2026-05-18T19:23:28.965Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cpg3JMi7qEH5CfVCgbyG3f`</summary>

```json
{
  "query": "\"affordance consistency\" paraphrase instruction robot learning self-supervised"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c441894a-4615-4ada-ace2-64cbbdb2bec0",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAab6pZGKrCvi24bPmAu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf813805-3a0e-409a-95fe-8e34d4042133",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgmRxXncEowSk2w7tvMS3V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 699,
      "cache_creation_input_tokens": 5026,
      "cache_read_input_tokens": 10458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5026,
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

_source line 27 · 2026-05-18T19:23:29.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WoiqZT6rMYYo24wceHD1h6`</summary>

```json
{
  "query": "RobustVLA paraphrase instruction augmentation training robustness VLA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf813805-3a0e-409a-95fe-8e34d4042133",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAab6pZGKrCvi24bPmAu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cdb6871-23ec-4e49-a656-5fac431a5b09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgmRxXncEowSk2w7tvMS3V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 699,
      "cache_creation_input_tokens": 5026,
      "cache_read_input_tokens": 10458,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5026
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 699,
          "output_tokens": 268,
          "cache_read_input_tokens": 10458,
          "cache_creation_input_tokens": 5026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5026,
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

_source line 28 · 2026-05-18T19:23:34.987Z_

<details><summary>↩ Tool result · `toolu_01D38GpvNkfnQNwyKw9Upi1F`</summary>

```text
Web search results for query: "paraphrase consistency loss training objective robot policy language conditioned 2024 2025 2026"

Links: [{"title":"Improving the Robustness of Large Language Models via Consistency Alignment","url":"https://arxiv.org/html/2403.14221"},{"title":"Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks","url":"http://ais.informatik.uni-freiburg.de/publications/papers/mees22rsspi.pdf"},{"title":"Language-Conditioned Representations and Mixture-of-Experts Policy for Robust Multi-Task Robotic Manipulation","url":"https://arxiv.org/html/2510.24055"},{"title":"Modularity through Attention: Efficient Training and Transfer of   Language-Conditioned Policies for Robot Manipulation","url":"https://arxiv.org/pdf/2212.04573"},{"title":"Language-Conditioned Imitation Learning for Robot Manipulation Tasks","url":"https://arxiv.org/pdf/2010.12083"},{"title":"Improving Consistency in Pretrained Language Models","url":"https://www.emergentmind.com/papers/2102.01017"},{"title":"GitHub - mees/calvin: CALVIN - A benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks · GitHub","url":"https://github.com/mees/calvin"}]

Based on the search results, I found several relevant papers on language-conditioned robot policies and consistency training objectives:

## Key Findings:

**Recent Work on Language-Conditioned Robot Policies:**

A 2025 paper addresses language-conditioned representations for robotic manipulation, investigating whether language can resolve perceptual ambiguity, whether mixture-of-experts architectures mitigate task conflict, and whether gradient modulation stabilizes training. The framework consists of a language-conditioned visual representation (LCVR) module, a mixture-of-experts policy, and gradient modulation via the FAMO algorithm to stabilize training.

**Paraphrase Consistency in Language Models:**

A consistency loss leverages KL Divergence to align predicted distributions across paraphrases and aims to fortify the representational integrity of extracted knowledge. Research shows that pretrained language models often produce inconsistent outputs for paraphrased inputs, with a novel KL Divergence-based loss function applied during pretraining to align predictions across different paraphrase patterns.

**Language-Conditioned Imitation Learning:**

A foundational approach for language-conditioned robot policies incorporates unstructured natural language into imitation learning, where experts provide demonstrations with verbal descriptions to interrelate language, perception, and motion modalities.

The search results show active research in both paraphrase consistency methods for language models and language-conditioned policy learning for robotics, though I didn't find papers explicitly combining a "paraphrase consistency loss" specifically as a training objective for robot policies in the 2024-2026 timeframe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c441894a-4615-4ada-ace2-64cbbdb2bec0",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "b0718870-a5f2-44ab-b978-3a5a5d9be70d",
  "sourceToolAssistantUUID": "c441894a-4615-4ada-ace2-64cbbdb2bec0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T19:23:35.329Z_

<details><summary>↩ Tool result · `toolu_01Cpg3JMi7qEH5CfVCgbyG3f`</summary>

```text
Web search results for query: ""affordance consistency" paraphrase instruction robot learning self-supervised"

Links: [{"title":"Computational models of affordance in robotics: a taxonomy and systematic classification - Philipp Zech, Simon Haller, Safoura Rezapour Lakani, Barry Ridge, Emre Ugur, Justus Piater, 2017","url":"https://journals.sagepub.com/doi/10.1177/1059712317726357"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/html/2409.01083v4"},{"title":"Grounding Language with Visual Affordances over Unstructured Data","url":"https://arxiv.org/pdf/2210.01911"},{"title":"Unsupervised Affordance Distillation for Generalization in ...","url":"https://openreview.net/pdf?id=an953WOpo2"},{"title":"Learning Instruction-Guided Manipulation Affordance via Large Models for   Embodied Robotic Tasks","url":"https://arxiv.org/pdf/2408.10658"},{"title":"Contextual Imagined Goals for Self-Supervised Robotic Learning","url":"https://arxiv.org/pdf/1910.11670"},{"title":"Affordance Learning from Play for Sample-Efficient Policy Learning","url":"https://arxiv.org/pdf/2203.00352"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/pdf/2506.09284"}]

Based on the search results, I found relevant information about affordance learning in robot manipulation with connections to instruction-guided tasks, paraphrasing, and self-supervised approaches. Here's what the research shows:

## Key Research Areas

**Affordance Learning in Robotic Manipulation:**

Understanding object affordances underpins a robot's capability to perform purposeful interactions in unstructured environments, and given an open-ended task instruction specified in natural language, a robot must identify action possibilities afforded by the environment based on visual perception.

**Self-Supervised Approaches:**

Self-supervised learning is a form of learning where information from one data view, such as a particular sensory modality, is used to direct the learning procedure in another data view. A self-supervised visual affordance model can be extracted from human teleoperated play data and leveraged to enable efficient policy learning and motion planning.

**Instruction-Guided Affordance Learning:**

Recent work has combined language instructions with affordance prediction. Instruction-Guided Affordance Net (IGANet) predicts affordance maps of instruction-guided robotic manipulation tasks by utilizing powerful priors from vision and language encoders pre-trained on large-scale datasets.

**Advanced Methods:**

Unsupervised Affordance Distillation (UAD) is a method that extracts affordance knowledge from foundation models and distills it into a task-conditioned affordance model, all without manual annotation.

These approaches combine multiple concepts: self-supervised learning enables robots to learn from unlabeled data, affordance understanding helps identify what actions are possible, and language grounding through instructions makes the learned affordances task-relevant.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf813805-3a0e-409a-95fe-8e34d4042133",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "6f2d7519-f114-4979-8404-cb6251588481",
  "sourceToolAssistantUUID": "bf813805-3a0e-409a-95fe-8e34d4042133",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T19:23:35.818Z_

<details><summary>↩ Tool result · `toolu_019HTssHDsKJkMs48ssADqpr`</summary>

```text
Web search results for query: "LIBERO-Para paraphrase robustness VLA training objective consistency loss"

Links: [{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://huggingface.co/papers/2603.28301"},{"title":"LIBERO-Para: Measuring VLA Paraphrase Robustness - YouTube","url":"https://www.youtube.com/watch?v=Yg-GVm-kdk4"},{"title":"GitHub - cau-hai-lab/LIBERO-Para · GitHub","url":"https://github.com/cau-hai-lab/LIBERO-Para"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO-Object: Lifelong Learning in Robotic Manipulation","url":"https://www.emergentmind.com/topics/libero-object"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/pdf/2510.00037"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"}]

I found comprehensive information about LIBERO-Para. Here are the key findings:

## LIBERO-Para Overview

LIBERO-Para is a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization.

## Key Findings

Across seven VLA configurations (0.6B-7.5B), there is consistent performance degradation of 22-52 percentage points under paraphrasing, primarily driven by object-level lexical variation, where even simple synonym substitutions cause large drops indicating reliance on surface-level matching rather than semantic grounding.

Performance consistently degrades under paraphrased instructions across architectures, scales, and fine-tuning strategies.

## Methodology

LIBERO-Para decomposes paraphrases along two essential axes: object-referring expressions and action-referring expressions, with each axis independently varied to yield compositional paraphrases.

The benchmark introduces PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation), a metric that combines keyword similarity and structural similarity with task success to enable fine-grained robustness analysis.

## Root Cause Analysis

80-96% of failures arise from planning-level trajectory divergence rather than execution errors, showing that paraphrasing disrupts task identification.

The paper was published on arXiv on March 30-31, 2026, and has garnered significant attention in the AI community for exposing critical fragility in Vision-Language-Action models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5ad6d27-ea8c-4b54-b3df-bcfb8f516dd7",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "2fe33fa2-6642-4668-836d-9976d0a8e513",
  "sourceToolAssistantUUID": "e5ad6d27-ea8c-4b54-b3df-bcfb8f516dd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T19:23:39.372Z_

<details><summary>↩ Tool result · `toolu_01WoiqZT6rMYYo24wceHD1h6`</summary>

```text
Web search results for query: "RobustVLA paraphrase instruction augmentation training robustness VLA 2025"

Links: [{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/html/2603.16044"},{"title":"[2511.01331] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.01331"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.01331"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"}]

Based on the web search results, here's what I found:

## RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models

RobustVLA is a robustness-aware reinforcement learning post-training method for Vision-Language-Action (VLA) models. Extensive experiments across diverse robotic environments demonstrate that RobustVLA significantly outperforms prior state-of-the-art methods in robustness and reliability.

## Key Problem It Addresses

Recent studies reveal that the generalization ability of pre-trained VLA models remains limited when deployed in Out-of-Distribution (OOD) scenarios, as VLA models often struggle with unseen objects, novel environments, and different robot embodiments, with even minor changes in object placement or environmental conditions such as lighting variations significantly degrading performance.

## Related Work on Paraphrase Robustness

The search results also reveal related research on paraphrase robustness in VLA models. Models may perform well on seen instruction phrasings yet fail to generalize to unseen paraphrased instructions at deployment. Additionally, research has implemented Low-Rank Adaptation (LoRA) to fine-tune OpenVLA on augmented instruction pairs, with results demonstrating that enriching the linguistic space of specialized datasets is crucial for embodied agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cdb6871-23ec-4e49-a656-5fac431a5b09",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "f7c49836-042e-4668-9529-4fe744d2100b",
  "sourceToolAssistantUUID": "1cdb6871-23ec-4e49-a656-5fac431a5b09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-18T19:23:42.685Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VWWyCnKuHQRJtSCgYbKpfG`</summary>

```json
{
  "query": "\"Enhancing Linguistic Generalization of VLA\" \"Synthetic Instruction Augmentation\" OpenVLA arXiv 2603.16044"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7c49836-042e-4668-9529-4fe744d2100b",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAacHdU94o7pvrFJnb64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ffe4e3c-8a3d-4f4c-ae48-2b0bb7974621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GAvSjm2sn1umGLezbytcSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4065,
      "cache_read_input_tokens": 15484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4065,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 33 · 2026-05-18T19:23:43.312Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YbefuMWe4Ea7kTCuPqTAMU`</summary>

```json
{
  "query": "\"Prompt Perturbation Consistency Learning\" PPCL paraphrase consistency regularization loss 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ffe4e3c-8a3d-4f4c-ae48-2b0bb7974621",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAacHdU94o7pvrFJnb64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44ef5292-0560-4fa7-8041-d7578d63d47b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GAvSjm2sn1umGLezbytcSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4065,
      "cache_read_input_tokens": 15484,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4065
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 15484,
          "cache_creation_input_tokens": 4065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4065,
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

_source line 34 · 2026-05-18T19:23:48.495Z_

<details><summary>↩ Tool result · `toolu_01VWWyCnKuHQRJtSCgYbKpfG`</summary>

```text
Web search results for query: ""Enhancing Linguistic Generalization of VLA" "Synthetic Instruction Augmentation" OpenVLA arXiv 2603.16044"

Links: [{"title":"[2603.16044] Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/abs/2603.16044"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/html/2603.16044"},{"title":"Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"},{"title":"Enhancing Generalization in Vision–Language–Action Models by","url":"https://arxiv.org/pdf/2509.11417"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://arxiv.org/pdf/2601.15197"}]

I found the research paper you're looking for. Here's what the search revealed:

"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation" proposes a parameter-efficient fine-tuning strategy to enhance the linguistic generalization of OpenVLA by synthesizing a general instruction set for the Bridge Dataset V2.

While OpenVLA represents the State-of-the-Art in Vision-Language-Action models, its zero-shot performance can be limited when encountering completely new environments. 

The paper leverages a Large Language Model to generate a rich variety of semantically equivalent but structurally diverse commands for existing trajectories. Low-Rank Adaptation (LoRA) is implemented to fine-tune OpenVLA on augmented pairs, allowing the model to bridge the gap between complex natural language intent and robotic actions.

The paper was submitted on March 17, 2026, and is authored by Dongik Shin. You can access it directly at arxiv.org/abs/2603.16044.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ffe4e3c-8a3d-4f4c-ae48-2b0bb7974621",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "1cd6af69-be61-4b51-a048-213fdce48d2b",
  "sourceToolAssistantUUID": "4ffe4e3c-8a3d-4f4c-ae48-2b0bb7974621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T19:23:51.789Z_

<details><summary>↩ Tool result · `toolu_01YbefuMWe4Ea7kTCuPqTAMU`</summary>

```text
Web search results for query: ""Prompt Perturbation Consistency Learning" PPCL paraphrase consistency regularization loss 2024"

Links: [{"title":"[2402.15833] Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/abs/2402.15833"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-eacl.91/"},{"title":"Prompt Perturbation Experiments","url":"https://www.emergentmind.com/topics/prompt-perturbation-experiments"},{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/html/2510.14242v1"},{"title":"[Literature Review] Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://www.themoonlight.io/en/review/prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"Prompt perturbation consistency learning for robust language models - Amazon Science","url":"https://www.amazon.science/publications/prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/pdf/2402.15833"},{"title":"Google Académico","url":"https://scholar.google.com/scholar?q=Prompt+Perturbation+Consistency+Learning+for+Robust+Language+Models."},{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/pdf/2510.14242"}]

Based on the search results, here's comprehensive information about Prompt Perturbation Consistency Learning (PPCL):

## Overview

PPCL is an efficient mitigation approach that works by regularizing the divergence between losses from clean and perturbed samples. The approach was published in 2024 and addresses robustness issues in language models.

## Core Concept

PPCL's core idea is to encourage the LLM to produce consistent predictions when given an original utterance and a perturbed version of that utterance. The method specifically handles three types of input perturbations: oronyms, synonyms, and paraphrasing.

## Technical Approach

During fine-tuning, PPCL feeds both a clean utterance and its perturbed version and adds a Jensen-Shannon (JS) divergence term between their token-level output distributions. This formalization of Jensen–Shannon consistency is essential for alignment between clean and perturbed samples, and the regularization alone supplies an additional 6–12 percentage points recovery in SF tasks.

## Performance Results

PPCL can recover on average 59% and 69% of the performance drop for Intent Classification and Slot Filling tasks, respectively, and beats the data augmentation approach while using ten times fewer augmented data samples.

## Publication Details

The research was authored by Yao Qiang, Subhrangshu Nandi, Ninareh Mehrabi, Greg Ver Steeg, Anoop Kumar, Anna Rumshisky, and Aram Galstyan, and published in the Findings of the Association for Computational Linguistics: EACL 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44ef5292-0560-4fa7-8041-d7578d63d47b",
  "isSidechain": true,
  "promptId": "d7baa623-bbed-44db-943d-1b134b9153a2",
  "agentId": "ac9b50b1441f2ff22",
  "type": "user",
  "uuid": "0f9eb9fd-4089-4bc6-bfa4-2a1f171d090a",
  "sourceToolAssistantUUID": "44ef5292-0560-4fa7-8041-d7578d63d47b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-18T19:24:12.735Z_

Here is my assessment based on thorough searching:

---

**The IPAC idea is novel in its specific formulation but sits in a rapidly converging neighborhood. It is not cleanly "already done," but several very close pieces of prior work exist.**

**Directly relevant prior work:**

1. **Shin (Mar 2026), arXiv 2603.16044** -- "Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation." Uses an LLM to generate paraphrased instructions for existing trajectories and fine-tunes OpenVLA with LoRA on these augmented pairs. This is *data augmentation* with paraphrases, not an explicit consistency loss on affordance maps, but the goal is identical: make the VLA invariant to instruction rephrasing.

2. **LIBERO-Para (Mar 2026), arXiv 2603.28301** -- A diagnostic benchmark showing VLAs suffer 22-52 point drops under paraphrased instructions. It identifies the problem IPAC claims to solve but does not propose a consistency training objective.

3. **ST4VLA (Feb 2026), arXiv 2602.10109** -- Demonstrates robustness to paraphrased instructions as an *evaluation result* of spatial pretraining, not as an explicit training objective.

4. **PPCL (EACL 2024)** -- Prompt Perturbation Consistency Learning uses a JS-divergence regularization between clean and perturbed prompt outputs in NLP. This is the same core idea (consistency loss across paraphrases) but applied to LLMs for intent classification/slot filling, not robot affordance maps.

5. **Flip-Flop Consistency (Oct 2025), arXiv 2510.14242** -- Unsupervised consistency training for robustness to prompt perturbations in LLMs. Again, same principle, different domain.

**Verdict:** No one has published an explicit *consistency loss on affordance maps* across paraphrased instructions for robot learning/VLAs. However, (a) paraphrase augmentation for VLAs already exists (Shin 2026), (b) consistency regularization across paraphrases exists in NLP (PPCL 2024), and (c) the problem is well-documented (LIBERO-Para 2026). IPAC's novelty is the specific combination -- enforcing identical *affordance map outputs* via a self-supervised consistency objective. This is a valid incremental contribution, but the proposal should clearly differentiate from Shin 2026's augmentation approach and acknowledge PPCL as conceptual prior art from NLP.

Sources:
- [Shin 2026 - Synthetic Instruction Augmentation for OpenVLA](https://arxiv.org/abs/2603.16044)
- [LIBERO-Para - Paraphrase Robustness Benchmark](https://arxiv.org/abs/2603.28301)
- [ST4VLA - Spatially Guided Training](https://arxiv.org/abs/2602.10109)
- [PPCL - Prompt Perturbation Consistency Learning](https://arxiv.org/abs/2402.15833)
- [Flip-Flop Consistency](https://arxiv.org/abs/2510.14242)
- [RobustVLA](https://arxiv.org/abs/2511.01331)
- [LADEV - VLA Testing Platform](https://arxiv.org/abs/2410.05191)
- [Contrastive Imitation Learning for Multi-Task Manipulation](https://arxiv.org/abs/2406.09738)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f9eb9fd-4089-4bc6-bfa4-2a1f171d090a",
  "isSidechain": true,
  "agentId": "ac9b50b1441f2ff22",
  "requestId": "req_011CbAadCia6Jt8Fo7eM75Cw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "574fe19f-1f60-48fc-8b23-d04e81f15110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "af248400-588b-43bf-bd53-91a9f73469de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKHGhsH9chajyBnts64Hf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1615,
      "cache_read_input_tokens": 19549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1615,
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
