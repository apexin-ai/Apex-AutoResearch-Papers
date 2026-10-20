# Research conversation: I need to verify benchmark claims and search for competing work in the World Action Model (WAM) space. Use WebSearch and

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 1
- **Tool calls:** 31
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-acb79247c2bab8e03.jsonl`
- **Structured JSON:** [`446a956b96e439891311.json`](../../sessions/44/446a956b96e439891311.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

71 recorded events

### User

_source line 1 · 2026-05-10T18:08:55.407Z_

I need to verify benchmark claims and search for competing work in the World Action Model (WAM) space. Use WebSearch and WebFetch.

1. **LIBERO-PRO benchmark** - claimed to be a robustness benchmark where standard LIBERO-trained models collapse from 90% to 0% under perturbation. Claimed GitHub: github.com/Zxy-MLlab/LIBERO-PRO
   - Search: "LIBERO-PRO robust evaluation vision language action models" and "LIBERO-PRO benchmark robotics"
   - Verify: Does it exist? What are the actual performance drops?

2. **RoboCasa SOTA** - The proposal claims 67-79% SOTA on RoboCasa with meaningful headroom.
   - Search: "RoboCasa benchmark SOTA 2025 2026" and "RoboCasa success rate world action model"
   - What are the current best results?

3. **MotuBrain** - claimed to use three-stream MoT with H-bridge design. 
   - Search: "MotuBrain world action model robot control" and "MotuBrain H-bridge attention"
   - Verify: Is it commercial/closed-source? Does the H-bridge description match?

4. **Competing noise-conditioned attention work** - Search for ANY work that conditions cross-modal attention on noise levels in diffusion models:
   - Search: "noise level conditioned attention diffusion" and "timestep conditioned cross-modal gating diffusion"
   - Search: "adaptive attention noise level multi-modal diffusion 2025 2026"
   - Search: "noise-aware attention mechanism diffusion transformer"

5. **CoRL 2026 deadline** - Verify the abstract deadline is May 26 and paper deadline is May 29.
   - Search: "CoRL 2026 submission deadline" and "CoRL 2026 Austin"

Report everything you find with URLs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "f447297d-5160-4ec9-aad4-cffc1b1a0b1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:08:55.410Z_

```json
{
  "parentUuid": "f447297d-5160-4ec9-aad4-cffc1b1a0b1e",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
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
  "uuid": "5b519c02-22f0-4232-bcbe-d40e704c7f21",
  "timestamp": "2026-05-10T18:08:55.410Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:08:57.923Z_



I'll conduct all these searches in parallel to be efficient. Let me first load the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b519c02-22f0-4232-bcbe-d40e704c7f21",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSRvKbbFCfetM8kzCz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3a7b9be-eae6-4796-8dba-87f2c609e85b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rR6uiC1QmdUR7vNWV2ZWH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1002,
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

_source line 4 · 2026-05-10T18:08:58.256Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01J1ddh4TdsQz37F84sU8F7F`</summary>

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
  "parentUuid": "f3a7b9be-eae6-4796-8dba-87f2c609e85b",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSRvKbbFCfetM8kzCz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a221e7a-651c-48fe-bb3d-fc4d7279d50f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rR6uiC1QmdUR7vNWV2ZWH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1002,
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

_source line 5 · 2026-05-10T18:08:58.258Z_

<details><summary>↩ Tool result · `toolu_01J1ddh4TdsQz37F84sU8F7F`</summary>

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
  "parentUuid": "6a221e7a-651c-48fe-bb3d-fc4d7279d50f",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "0ce025f6-4d74-4847-939d-ef3b1e9f9be7",
  "sourceToolAssistantUUID": "6a221e7a-651c-48fe-bb3d-fc4d7279d50f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:09:00.788Z_



Now let me launch all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ce025f6-4d74-4847-939d-ef3b1e9f9be7",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e85f021-a0a0-4565-95ac-bbf1f82970d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 7 · 2026-05-10T18:09:01.265Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PrQDfe7nsuNc7rToQ8SJfM`</summary>

```json
{
  "query": "LIBERO-PRO robust evaluation vision language action models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e85f021-a0a0-4565-95ac-bbf1f82970d3",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bbd0209-07c7-4439-8471-bf888ee17099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 8 · 2026-05-10T18:09:02.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AxXXcng2jJLr4muZjy4S6o`</summary>

```json
{
  "query": "LIBERO-PRO benchmark robotics perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bbd0209-07c7-4439-8471-bf888ee17099",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "116582f9-223c-4607-b366-b6a6d0bb0ee5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 9 · 2026-05-10T18:09:02.743Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UQyAsdm87ktuxZXWyTiL4N`</summary>

```json
{
  "query": "RoboCasa benchmark SOTA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "116582f9-223c-4607-b366-b6a6d0bb0ee5",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47c61eba-792c-4f18-bd25-92b026cb380f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 10 · 2026-05-10T18:09:03.215Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CwSZkmgFWVr8tonA3ETYQk`</summary>

```json
{
  "query": "RoboCasa success rate world action model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47c61eba-792c-4f18-bd25-92b026cb380f",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9535d73-30c4-4bee-9980-2b1c03780134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 11 · 2026-05-10T18:09:04.530Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SSse7ovrKB27vYhXpaACU7`</summary>

```json
{
  "query": "MotuBrain world action model robot control"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9535d73-30c4-4bee-9980-2b1c03780134",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "800a2290-0a3b-4b83-80f4-39f6d13661b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 12 · 2026-05-10T18:09:04.842Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F42dZsZLhVGsXC81xosdmr`</summary>

```json
{
  "query": "MotuBrain H-bridge attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "800a2290-0a3b-4b83-80f4-39f6d13661b5",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "498fe43c-5d7e-45f2-b33d-d39e4b8d8173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 13 · 2026-05-10T18:09:05.160Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NiaSQWxuNCzfRt43NDAaSA`</summary>

```json
{
  "query": "noise level conditioned attention diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "498fe43c-5d7e-45f2-b33d-d39e4b8d8173",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3bd661c-143d-4388-bb0c-2b147ede4a6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 14 · 2026-05-10T18:09:05.671Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016UtN6XH7tZGTnQSUd5YJ9d`</summary>

```json
{
  "query": "timestep conditioned cross-modal gating diffusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3bd661c-143d-4388-bb0c-2b147ede4a6c",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83737c39-d9b6-4f7d-8f15-543cbd27d74a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 15 · 2026-05-10T18:09:08.302Z_

<details><summary>↩ Tool result · `toolu_01PrQDfe7nsuNc7rToQ8SJfM`</summary>

```text
Web search results for query: "LIBERO-PRO robust evaluation vision language action models"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"},{"title":"[2510.03827v1] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization | alphaXiv","url":"https://www.alphaxiv.org/abs/2510.03827v1"},{"title":"Paper page - LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://huggingface.co/papers/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251003827Z/abstract"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"}]

## Summary of Search Results

I found comprehensive information about LIBERO-PRO. Here are the key findings:

### Overview

LIBERO-PRO is an extended LIBERO benchmark that addresses problems with current VLA model evaluation by systematically evaluating model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments.

### Problem Being Addressed

The original LIBERO benchmark has problematic training and evaluation settings that often lead to inflated performance estimates and prevent fair model comparison.

### Key Findings

Although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under LIBERO-PRO's generalized setting. This discrepancy exposes the models' reliance on rote memorization of action sequences and environment layouts from the training set, rather than genuine task understanding or environmental perception.

### Specific Test Cases

The evaluation includes several perturbation types:
- Modifies object appearance, color, and scale to test adaptability to visual shifts
- Relocates objects within feasible spatial bounds to evaluate the model's adaptability to spatial position changes
- Paraphrases natural language commands to probe linguistic robustness
- Redefines task logic and target states to test procedural generalization
- Replaces working environments to evaluate cross-environment robustness

### Conclusion

These findings expose the severe flaws in current evaluation practices, and the authors call on the community to abandon misleading methodologies in favor of robust assessments of model generalization and comprehension.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bbd0209-07c7-4439-8471-bf888ee17099",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "c8257eb1-f423-4343-a6cf-53f261c9fd4d",
  "sourceToolAssistantUUID": "0bbd0209-07c7-4439-8471-bf888ee17099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:09:08.315Z_

<details><summary>↩ Tool result · `toolu_01UQyAsdm87ktuxZXWyTiL4N`</summary>

```text
Web search results for query: "RoboCasa benchmark SOTA 2025 2026"

Links: [{"title":"GitHub - robocasa/robocasa: RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots · GitHub","url":"https://github.com/robocasa/robocasa"},{"title":"RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots | OpenReview","url":"https://openreview.net/forum?id=tQJYKwc3n4"},{"title":"VLA SOTA Leaderboard","url":"https://sota.evomind-tech.com/benchmarks/robocasa_gr1_tabletop/"},{"title":"RoboCAS: A Benchmark for Robotic Manipulation in Complex Object Arrangement Scenarios","url":"https://arxiv.org/html/2407.06951v1"},{"title":"Robocasa","url":"https://robocasa.ai/assets/robocasa365_iclr26.pdf"},{"title":"RoboCasa: Scalable Household Robotics Simulation","url":"https://www.emergentmind.com/topics/robocasa"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/attachment?id=tQJYKwc3n4&name=pdf"},{"title":"Yuke Zhu on X: \"Today, we publicly released RoboCasa365, a large-scale simulation benchmark for training and systematically evaluating generalist robot models. Built upon our original RoboCasa framework, it offers: • 2,500 realistic kitchen environments; • 365 everyday tasks (basic skills + https://t.co/bVuUPr6pon\" / X","url":"https://x.com/yukez/status/2028546069500699075"},{"title":"[2407.06951] RoboCAS: A Benchmark for Robotic Manipulation in Complex Object Arrangement Scenarios","url":"https://arxiv.org/abs/2407.06951"},{"title":"nvidia/Cosmos-Policy-RoboCasa-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B"}]

Based on the search results, here's what I found about RoboCasa benchmark and state-of-the-art performance:

## RoboCasa365 Benchmark

RoboCasa365 was released on February 18, 2026, featuring 365 tasks, 2500+ kitchen scenes, 2200+ hours of robot demonstration data, and benchmarking support. The benchmark includes 365 everyday tasks across 2,500 diverse kitchen environments, with over 600 hours of human demonstration data and over 1600 hours of synthetically generated demonstration data.

## State-of-the-Art Results

The Cosmos-Policy-RoboCasa-Predict2-2B model achieves state-of-the-art performance on the RoboCasa simulation benchmark with a 67.1% average success rate across 24 kitchen manipulation tasks.

## Benchmark Design

RoboCasa365 supports popular policy learning methods including Diffusion Policy, pi, and GR00T, plus user-submitted models on the leaderboard. RoboCasa365 is designed to support systematic evaluations for different problem settings, including multi-task learning, robot foundation model training, and lifelong learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47c61eba-792c-4f18-bd25-92b026cb380f",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "b71e23ab-a18c-4e17-bbfc-db9bd10aac87",
  "sourceToolAssistantUUID": "47c61eba-792c-4f18-bd25-92b026cb380f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T18:09:09.303Z_

<details><summary>↩ Tool result · `toolu_01CwSZkmgFWVr8tonA3ETYQk`</summary>

```text
Web search results for query: "RoboCasa success rate world action model"

Links: [{"title":"RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots","url":"https://robocasa.ai/assets/robocasa_rss24.pdf"},{"title":"nvidia/Cosmos-Policy-RoboCasa-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B"},{"title":"RoboCasa: Scalable Household Robotics Simulation","url":"https://www.emergentmind.com/topics/robocasa"},{"title":"RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots","url":"https://arxiv.org/html/2603.04356v1"},{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"robocasa/robocasa at main · robocasa/robocasa","url":"https://github.com/robocasa/robocasa/tree/main/robocasa"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/attachment?id=tQJYKwc3n4&name=pdf"},{"title":"RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots","url":"https://arxiv.org/html/2406.02523.pdf"},{"title":"RoboCasa: Large-Scale Simulation of Household Tasks for Generalist Robots","url":"https://www.researchgate.net/publication/383894362_RoboCasa_Large-Scale_Simulation_of_Household_Tasks_for_Generalist_Robots"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Video World Models","url":"https://arxiv.org/html/2505.12705v2"}]

Based on the search results, here are the key findings regarding RoboCasa success rates for world action models:

## Success Rates on RoboCasa

X-WAM, a unified 4D world action model pretrained on over 5,800 hours of robotic data, achieves 79.2% average success rate on RoboCasa benchmark.

The Cosmos-Policy-RoboCasa-Predict2-2B model achieves 67.1% average success rate on RoboCasa with only 50 demos per task.

Cosmos Policy achieves state-of-the-art performance with 67.1% average success rate on RoboCasa simulation benchmarks.

Additionally, there are other notable results: Real Only models achieve a 61.8% average success rate, while Sim-and-Real training reaches 79.8%, demonstrating the value of combining simulation and real-world data for policy training.

These results show varying success rates depending on the specific model architecture and training approach, with world action models achieving success rates ranging from approximately 61.8% to 79.2% on the RoboCasa benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9535d73-30c4-4bee-9980-2b1c03780134",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "42f3d3e8-1698-4d72-8949-38be8fc2e73d",
  "sourceToolAssistantUUID": "e9535d73-30c4-4bee-9980-2b1c03780134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T18:09:09.404Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017rcAstXNDscPsByNCKjUw1`</summary>

```json
{
  "query": "adaptive attention noise level multi-modal diffusion 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42f3d3e8-1698-4d72-8949-38be8fc2e73d",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95c1b54a-de2c-4dd2-a312-408c1721a87d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 19 · 2026-05-10T18:09:09.454Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MN3oz4PmMiZgEzqnSiA8Vm`</summary>

```json
{
  "query": "noise-aware attention mechanism diffusion transformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95c1b54a-de2c-4dd2-a312-408c1721a87d",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5c43904-ea85-42f4-a37c-d34ef820e780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 20 · 2026-05-10T18:09:09.498Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y1DaS5sjP81GqKXH7tU6tu`</summary>

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
  "parentUuid": "f5c43904-ea85-42f4-a37c-d34ef820e780",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "587d668d-98f4-48ae-af5f-0a832ad5ee6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 21 · 2026-05-10T18:09:09.524Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UD7qSmgcNcXEF8pEN5Dyf7`</summary>

```json
{
  "query": "CoRL 2026 Austin"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "587d668d-98f4-48ae-af5f-0a832ad5ee6d",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLSeXMUtXYKV9tN3CCb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73487541-29d6-45e4-98c0-3fd0349cadd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D54o8sLzePktkEK7z37EBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 22 · 2026-05-10T18:09:11.980Z_

<details><summary>↩ Tool result · `toolu_01F42dZsZLhVGsXC81xosdmr`</summary>

```text
Web search results for query: "MotuBrain H-bridge attention"

Links: [{"title":"H-Bridges – the Basics | Modular Circuits","url":"https://www.modularcircuits.com/blog/articles/h-bridge-secrets/h-bridges-the-basics/"},{"title":"H-bridge and power — Device Programming 1 documentation","url":"https://cued-partib-device-programming.readthedocs.io/en/latest/h-bridge.html"},{"title":"Controlling DC Motors with the L298N H Bridge and Arduino - YouTube","url":"https://www.youtube.com/watch?v=dyjo_ggEtVU"},{"title":"H-bridge - Wikipedia","url":"https://en.wikipedia.org/wiki/H-bridge"},{"title":"H-bridge and power — Device Programming 1 documentation","url":"https://device-programming-course.readthedocs.io/en/latest/h-bridge.html"},{"title":"H Bridge Motor Speed Controller Tutorial - YouTube","url":"https://www.youtube.com/watch?v=iYafyPZ15g8"},{"title":"H Bridge Motor Control: A Complete Guide for Engineers 2025","url":"https://www.wevolver.com/article/h-bridge-motor-control-a-complete-guide-for-engineers-2025"},{"title":"BA-Net: Bridge Attention in Deep Neural Networks","url":"https://arxiv.org/html/2410.07860v1"},{"title":"L298N Motor Driver - Arduino Interface, How It Works, Codes, Schematics","url":"https://howtomechatronics.com/tutorials/arduino/arduino-dc-motor-control-tutorial-l298n-pwm-h-bridge/"},{"title":"H-Bridge on a Breadboard : 8 Steps - Instructables","url":"https://www.instructables.com/H-Bridge-on-a-Breadboard/"}]

Based on the search results, I found information about H-bridges and a separate research paper about attention mechanisms in neural networks, but no specific results for "MotuBrain H-bridge attention" as a unified topic.

The search results include:

1. **H-Bridge Information**: Multiple resources explain that an H-bridge is a circuit containing four switching elements with the load at the center in an H-like configuration. An H-Bridge circuit contains four switching elements, transistors or MOSFETs, with the motor at the center forming an H-like configuration.

2. **Bridge Attention in Neural Networks**: There is a research paper about bridge attention, a novel approach designed to facilitate more effective integration and information flow between different convolutional layers in deep neural networks.

However, the search results do not contain any information specifically about "MotuBrain" as a product, platform, or system. If you're looking for information about a specific MotuBrain product or application that combines H-bridge motor control with attention mechanisms, you may want to provide additional context or search with more specific terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "498fe43c-5d7e-45f2-b33d-d39e4b8d8173",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "13615c14-95b9-4e81-b98b-675f1857c547",
  "sourceToolAssistantUUID": "498fe43c-5d7e-45f2-b33d-d39e4b8d8173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T18:09:12.150Z_

<details><summary>↩ Tool result · `toolu_01AxXXcng2jJLr4muZjy4S6o`</summary>

```text
Web search results for query: "LIBERO-PRO benchmark robotics perturbation"

Links: [{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"},{"title":"Developing a Simulation Platform for the Benchmarking of ...","url":"https://www.ias.informatik.tu-darmstadt.de/uploads/Team/TimSchneider/msc_tristan_vla_generalization.pdf"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"}]

Based on the search results, here's what I found about LIBERO-PRO benchmark and robotics perturbation:

## Overview

LIBERO-PRO is a plug-and-play benchmark that incorporates carefully designed perturbations across four dimensions—manipulated objects, initial states, task instructions, and environments—and supports randomized combinations of these dimensions for more faithful evaluation.

## Purpose and Findings

LIBERO has emerged as a widely adopted benchmark for evaluating Vision-Language-Action (VLA) models; however, its current training and evaluation settings are problematic, often leading to inflated performance estimates and preventing fair model comparison. To address these issues, LIBERO-PRO systematically evaluates model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments.

## Key Results

The benchmark reveals a significant discrepancy between models' performance on standard LIBERO and LIBERO-PRO: Although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under the generalized setting. This discrepancy exposes the models' reliance on rote memorization of action sequences and environment layouts from the training set, rather than genuine task understanding or environmental perception.

## Perturbation Types

The benchmark extends the four original task categories in LIBERO by introducing object attribute perturbations, initial position perturbations, instruction perturbations, and environmental perturbations.

The benchmark serves as a more rigorous evaluation tool for Vision-Language-Action models in robotic manipulation tasks, moving beyond memorization toward genuine task understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "116582f9-223c-4607-b366-b6a6d0bb0ee5",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "4a6dfff3-75e2-4105-be77-d326e8e6c724",
  "sourceToolAssistantUUID": "116582f9-223c-4607-b366-b6a6d0bb0ee5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T18:09:12.166Z_

<details><summary>↩ Tool result · `toolu_01NiaSQWxuNCzfRt43NDAaSA`</summary>

```text
Web search results for query: "noise level conditioned attention diffusion"

Links: [{"title":"Multi-view Image Diffusion via Coordinate Noise and Fourier Attention","url":"https://arxiv.org/html/2412.03756"},{"title":"Simple Drop-in LoRA Conditioning on Attention Layers Will Improve Your Diffusion Model","url":"https://arxiv.org/html/2405.03958v3"},{"title":"Adaptive User Interest Modeling via Conditioned Denoising Diffusion For Click-Through Rate Prediction","url":"https://arxiv.org/html/2509.19876v1"},{"title":"1 Attention in Diffusion Model: A Survey","url":"https://arxiv.org/pdf/2504.03738"},{"title":"Attention-enhanced conditional-diffusion-based data synthesis for data augmentation in machine fault diagnosis - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197623018808"},{"title":"Attention-Conditional Diffusion (ACD)","url":"https://www.emergentmind.com/topics/attention-conditional-diffusion-acd"},{"title":"Diffusion model - Wikipedia","url":"https://en.wikipedia.org/wiki/Diffusion_model"},{"title":"What are Diffusion Models? | Lil'Log","url":"https://lilianweng.github.io/posts/2021-07-11-diffusion-models/"},{"title":"Attention in Diffusion Model: A Survey","url":"https://arxiv.org/html/2504.03738v1"},{"title":"Text-to-Image: Diffusion, Text Conditioning, Guidance, Latent Space","url":"https://eugeneyan.com/writing/text-to-image/"}]

Based on the web search results, here's what I found about "noise level conditioned attention diffusion":

## Key Findings

The search results reveal several relevant developments in this area:

### Noise Level Conditioning in Diffusion Models

There is ongoing research addressing how to assign basis structures to specific noise levels in diffusion models, particularly when considering a continuum of SNR (Signal-to-Noise Ratio) levels.

### Attention-Conditional Diffusion (ACD)

Attention-Conditional Diffusion (ACD) models leverage explicit attention manipulation to integrate conditioning signals, enabling controlled and multimodal generative outputs. A notable application includes channel estimation in non-stationary wireless signals, where ACD achieves improved performance metrics with SNR-matched truncated schedules and temporal self-conditioning.

### LoRA Conditioning on Attention Layers

Recent work shows that adding LoRA conditioning to the attention layers of diffusion models improves image generation quality, with FID scores of 1.91/1.75 for unconditional and class-conditional CIFAR-10 generation.

### Information Leakage at High Noise Levels

Research has investigated the gap in noise initialization between training and inference for diffusion models, noting that there is an information leak that occurs even at highest noise levels during training.

These developments collectively address how conditioning mechanisms, particularly attention-based approaches, interact with noise levels throughout the diffusion process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3bd661c-143d-4388-bb0c-2b147ede4a6c",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "9de4b525-7b47-4d41-ac12-6ad1cb58c84f",
  "sourceToolAssistantUUID": "c3bd661c-143d-4388-bb0c-2b147ede4a6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T18:09:13.097Z_

<details><summary>↩ Tool result · `toolu_01Y1DaS5sjP81GqKXH7tU6tu`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Vincent Vanhoucke's Post","url":"https://www.linkedin.com/posts/vanhoucke_corl-2026-website-is-officially-live-at-http-activity-7432112475480817664-gBos"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, here are the CoRL 2026 submission deadlines:

The abstract submission deadline is May 26, 2026 11:59 UTC, and the paper submission deadline is May 29, 2026 11:59 UTC. However, there's an important note: the paper submission deadline is Thursday (5/28) EOD rather than Friday, so the actual paper deadline appears to be May 28, 2026.

CoRL 2026 will be held in Austin, Texas, US, and the conference dates are November 9-12, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "587d668d-98f4-48ae-af5f-0a832ad5ee6d",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "be8532e1-e101-46cd-91d2-c74b201f47df",
  "sourceToolAssistantUUID": "587d668d-98f4-48ae-af5f-0a832ad5ee6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T18:09:13.919Z_

<details><summary>↩ Tool result · `toolu_016UtN6XH7tZGTnQSUd5YJ9d`</summary>

```text
Web search results for query: "timestep conditioned cross-modal gating diffusion"

Links: [{"title":"A Versatile Diffusion Transformer with Mixture of Noise ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/15f4cefb0e143c7ad9d40e879b0a9d0c-Paper-Conference.pdf"},{"title":"Cross-Modal Contextualized Diffusion Models for Text-Guided Visual Generation and Editing | OpenReview","url":"https://openreview.net/forum?id=nFMS6wF2xq"},{"title":"TAFG-MAN: Timestep-Adaptive Frequency-Gated Latent Diffusion for Efficient and High-Quality Low-Dose CT Image Denoising","url":"https://arxiv.org/html/2603.20868"},{"title":"Cross-Modal Contextualized Diffusion Models for Text-Guided Visual Generation and Editing","url":"https://arxiv.org/html/2402.16627v1"},{"title":"Watch Your Step: Information Injection in Diffusion Models via Shadow Timestep Embedding","url":"https://arxiv.org/html/2605.00935"},{"title":"Modulating Pretrained Diffusion Models for Multimodal Image Synthesis","url":"https://dl.acm.org/doi/fullHtml/10.1145/3588432.3591549"},{"title":"Unified Multimodal Understanding and Generation Models","url":"https://arxiv.org/pdf/2505.02567"},{"title":"GitHub - L-YeZhu/CDCD: [ICLR2023] Discrete Contrastive Diffusion for Cross-Modal Music and Image Generation (CDCD). · GitHub","url":"https://github.com/L-YeZhu/CDCD"},{"title":"Controllable Motion Generation via Diffusion Modal Coupling","url":"https://arxiv.org/html/2503.02353v2"},{"title":"Cross-Attention Makes Inference Cumbersome in Text-to-Image Diffusion Models","url":"https://arxiv.org/html/2404.02747v1"}]

Based on the search results, here are the key findings related to timestep-conditioned cross-modal gating in diffusion models:

## Timestep-Adaptive Frequency-Gated Diffusion

A lightweight timestep-adaptive frequency-gated conditioning mechanism improves how low- and high-frequency condition cues are injected into the latent diffusion U-Net. Specifically, this mechanism decomposes condition features into low- and high-frequency components, predicts timestep-adaptive gates from the current denoising feature and timestep embedding, and progressively releases high-frequency guidance in later denoising stages before cross-attention.

## Cross-Modal Context in Diffusion

A contextualized diffusion model propagates cross-modal context to all timesteps in both diffusion and reverse processes, adapting their trajectories for facilitating cross-modal synthesis. This approach differs from conventional models by incorporating cross-modal interactions between text condition and image/video sample into the forward process, serving as a context-aware adapter to optimize diffusion trajectories.

## Timestep-Dependent Cross-Attention Gating

A training-free method called Tgate caches the cross-attention output once it converges and keeps it fixed during the remaining inference steps. Research shows that cross-attention converges early during the inference process, characterized by semantics-planning and fidelity-improving stages, with cross-attention impact not being uniform across these stages.

These techniques represent different approaches to controlling how cross-modal information flows through diffusion models at different timesteps for improved generation quality and efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83737c39-d9b6-4f7d-8f15-543cbd27d74a",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "05b48909-6000-4b93-93ca-9a15e01d09bc",
  "sourceToolAssistantUUID": "83737c39-d9b6-4f7d-8f15-543cbd27d74a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T18:09:16.950Z_

<details><summary>↩ Tool result · `toolu_01UD7qSmgcNcXEF8pEN5Dyf7`</summary>

```text
Web search results for query: "CoRL 2026 Austin"

Links: [{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Organizing Committee","url":"https://www.corl.org/organizing-committee"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 — Conference on Robot Learning - Passion PA","url":"https://passionpa.com/event/corl-2026"},{"title":"CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz","url":"https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"},{"title":"CoRL 2026 | Open Source Robotics - Growbotics AI","url":"https://robotics.growbotics.ai/community/events/corl-2026"},{"title":"Yuke Zhu on X: \"CoRL is coming to Austin, TX this November! As General Chair, I'm thrilled to welcome the robot learning community. 2026 feels like a pivotal year as AI-powered robotic systems begin deploying at scale for real-world tasks. This year, I hope CoRL will be the forum that connects\" / X","url":"https://x.com/yukez/status/2027177754177728660"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"CoRL 2025","url":"https://2025.corl.org/"}]

Here are the search results for CoRL 2026 Austin:

The Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning. CoRL 2026 will be held in Austin, Texas, US.

**Key Details:**

- **Dates:** November 9–12, 2026, with a workshop day on November 9 and the main conference on November 10–12
- **Venue:** JW Marriott Austin
- **Submission Deadlines:** May 25 for abstract submission and May 28 for full paper submission

The conference proceedings are indexed in Scopus with a CORE ranking of A* (global top 5%), making it one of the most prestigious conferences in the field of robot learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73487541-29d6-45e4-98c0-3fd0349cadd6",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "bb4fa289-1912-4729-8946-187f0b8a76cb",
  "sourceToolAssistantUUID": "73487541-29d6-45e4-98c0-3fd0349cadd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T18:09:17.325Z_

<details><summary>↩ Tool result · `toolu_017rcAstXNDscPsByNCKjUw1`</summary>

```text
Web search results for query: "adaptive attention noise level multi-modal diffusion 2025 2026"

Links: [{"title":"Multimodal diffusion framework for collaborative text image audio generation and applications | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-05794-4"},{"title":"DiMSOD: A Diffusion-Based Framework for Multi-Modal Salient Object Detection","url":"https://ojs.aaai.org/index.php/AAAI/article/view/33096/35251"},{"title":"Supervised Attention Mechanism for Low-quality ...","url":"https://aclanthology.org/2025.emnlp-main.1084.pdf"},{"title":"A multi-modal diffusion model with dual-cross-attention for multi-omics data generation and translation | Nature Communications","url":"https://www.nature.com/articles/s41467-026-71744-x"},{"title":"Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Lv_Rethinking_Cross-Modal_Interaction_in_Multimodal_Diffusion_Transformers_ICCV_2025_paper.pdf"},{"title":"MODIFy : A multi-modal anomaly diagnosis framework with diffusion-enhanced adaptive fusion in microservices - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0164121226000786"},{"title":"1 Attention in Diffusion Model: A Survey","url":"https://arxiv.org/pdf/2504.03738"},{"title":"Adaptive graph signal processing for robust multimodal fusion with dynamic semantic alignment | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-44641-y"},{"title":"Multi-modal LLMs, Diffusions, and the Unification","url":"https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Multi-modal%20Generative%20AI%20Multi-modal%20LLMs%20Diffusions%20and%20the%20Unification.pdf"},{"title":"Downloads 2025","url":"https://iclr.cc/Downloads/2025"}]

I found several recent research papers related to your search query about adaptive attention, noise levels, and multi-modal diffusion models from 2025-2026:

## Key Findings:

**Multi-Modal Diffusion with Adaptive Attention:**

A hierarchical diffusion framework introduces an adaptive attention mechanism that dynamically balances information flow across modalities, focusing on collaborative generation across text, image, and audio modalities. This approach demonstrates significant improvements over state-of-the-art baselines, with an average 11.65% increase in tri-modal semantic alignment.

**Cross-Modal Interaction in Diffusion Transformers:**

TACA is a parameter-efficient method that dynamically rebalances cross-modal attention in multimodal diffusion models, presented at ICCV 2025.

**Noise and Attention in Multi-Modal Systems:**

A Feature Adaptive Network injects complementary depth or thermal information at all resolutions, avoids interference between different modalities, and enables efficient adaptive cross-modal information fusion through a Feature Injection Attention Network that facilitates interaction between diffusion noise embeddings and semantic features.

**Adaptive Mechanisms for Robust Multimodal Processing:**

The diffusion mechanism injects controllable noise during training and learns denoising objectives, thereby improving the model's robustness to noisy and incomplete trace data.

These recent publications demonstrate active research in combining adaptive attention mechanisms with multi-modal diffusion models to handle noise and improve cross-modal information processing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95c1b54a-de2c-4dd2-a312-408c1721a87d",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "dad6c24c-4eae-4cf2-b712-615b37bcbae9",
  "sourceToolAssistantUUID": "95c1b54a-de2c-4dd2-a312-408c1721a87d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T18:09:18.022Z_

<details><summary>↩ Tool result · `toolu_01MN3oz4PmMiZgEzqnSiA8Vm`</summary>

```text
Web search results for query: "noise-aware attention mechanism diffusion transformer"

Links: [{"title":"Noise-Informed Diffusion-Generated Image Detection with Anomaly Attention","url":"https://arxiv.org/html/2506.16743v1"},{"title":"Analysis of Attention in Video Diffusion Transformers","url":"https://arxiv.org/html/2504.10317v1"},{"title":"Attention-Only Transformers via Unrolled Subspace Denoising | OpenReview","url":"https://openreview.net/forum?id=RhAW7TRJUy"},{"title":"1 Attention in Diffusion Model: A Survey","url":"https://arxiv.org/pdf/2504.03738"},{"title":"Attention in Diffusion Model: A Survey","url":"https://arxiv.org/html/2504.03738v1"},{"title":"[2506.03790] Attention-Only Transformers via Unrolled Subspace Denoising","url":"https://arxiv.org/abs/2506.03790"},{"title":"Advanced transformer for high-noise image denoising: Enhanced attention and detail preservation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0923596525000335"},{"title":"Applying Transformers and Attention for Speech Denoising","url":"https://go.clearlyip.com/articles/pdfs/transformer-attention-speech-denoising.pdf"},{"title":"Diffusion model - Wikipedia","url":"https://en.wikipedia.org/wiki/Diffusion_model"},{"title":"Differential Transformer Explained: What is it and How Does It Work? | by Sahin Ahmed(Data Scientist/MLE) | Medium","url":"https://medium.com/@sahin.samia/differential-transformer-explained-what-is-it-and-how-does-it-work-437d91bd8724"}]

Based on the search results, here's what I found about noise-aware attention mechanisms in diffusion transformers:

## Noise-Aware Self-Attention (NASA) Module

A novel Noise-Aware Self-Attention (NASA) module has been introduced that focuses on noise regions to capture anomalous patterns. This NASA module is incorporated into Swin Transformer, forming a novel detection architecture called NASA-Swin.

### Application in Image Forgery Detection

Image noise from various diffusion models displays similar spatial and frequency patterns, such as structured grid textures in spatial domain and prominent highlights in high-frequency regions. The noise-aware self-attention (NASA) module is designed to enhance focus on noise-related information in the attention calculation in the self-attention mechanism.

## Attention in Video Diffusion Transformers

Another related area of research involves analyzing attention in video diffusion transformers. Research has conducted an in-depth analysis of attention in video diffusion transformers (VDiTs) and identified three key properties of attention in VDiTs: Structure, Sparsity, and Sinks.

## Differential Attention Mechanism

Related to noise handling, the DIFF Transformer uses a differential attention mechanism which improves the signal-to-noise ratio by subtracting two softmax outputs. This mechanism is inspired by differential amplifiers in electrical engineering and the concept of noise-canceling headphones.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5c43904-ea85-42f4-a37c-d34ef820e780",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "a6991082-8b56-4a63-b122-439a842e0d24",
  "sourceToolAssistantUUID": "f5c43904-ea85-42f4-a37c-d34ef820e780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T18:09:18.101Z_

<details><summary>↩ Tool result · `toolu_01SSse7ovrKB27vYhXpaACU7`</summary>

```text
Web search results for query: "MotuBrain world action model robot control"

Links: [{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://www.prnewswire.com/news-releases/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence-302757280.html"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/26497/"},{"title":"ShengShu Technology Unveils Motubrain: A Unified \"World Action Model\" to Solve the Robotics Scaling Problem | Humanoids Daily","url":"https://www.humanoidsdaily.com/news/shengshu-technology-unveils-motubrain-a-unified-world-action-model-to-solve-the-robotics-scaling-problem"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | The Manila Times","url":"https://www.manilatimes.net/2026/04/29/tmt-newswire/pr-newswire/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/2331652"},{"title":"Motubrain: a World Action Model by Shengshu Technology and Tsinghua University","url":"https://chinaresearchcollective.substack.com/p/motubrain-a-world-action-model-by"},{"title":"ShengShu Technology Unveils World Action Model “Motubrain”: One Brain, Infinite Possibilities for Robotic Intelligence – Digital Media Net","url":"https://digitalmedianet.com/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/"},{"title":"MotuBrain World Model Tops Two Global Benchmarks — A Breakthrough in Robot Intelligence - DeepInsightAI","url":"https://deepinsightai.io/motubrain-world-model/"},{"title":"ChinaPulse.com - ShengShu Technology Unveils World Action Model “Motubrain”: One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://www.chinapulse.com/data-news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/"},{"title":"ShengShu unveils Motubrain world action model for robotics","url":"https://vir.com.vn/shengshu-unveils-motubrain-world-action-model-for-robotics-151735.html"}]

## MotuBrain: World Action Model for Robot Control

ShengShu Technology announced Motubrain, a World Action Model that replaces multiple task-specific systems with a single, unified model that functions as a robotic brain for the physical world.

### Key Architecture and Capabilities

MotuBrain is built on a Unified Multimodal Model that treats video and action as two continuous modalities to be learned together, giving it five capabilities at once: vision-language-action control (VLA), world modelling, video generation, inverse dynamics modelling (IDM), and joint video-action prediction. A three-stream Mixture-of-Transformers (MoT) brings video, action, and language together by drawing on the strengths of existing pretrained models, enabling Motubrain to understand environments, follow language instructions, predict what happens next, and generate actions all at the same time.

### Core Features

**Long-horizon Task Execution:** It can handle complex, multi-step tasks involving up to 10 atomic actions, far beyond the typical 2–3 atomic actions, so the robot no longer sees isolated actions; it sees a complete, meaningful task from start to finish.

**Unified Learning:** MotuBrain learns from a far broader range of data than conventional AI models that train robots, including unlabelled video, task recordings without language annotations, and data from different robot embodiments, with a proprietary latent action framework that extracts physical motion directly from large-scale video without requiring the data to be labelled or tagged.

**Cross-robot Transfer:** MotuBrain can be adapted to new humanoid embodiments with only 50–100 same-embodiment trajectories, while retaining the ability to solve long-horizon and dexterous manipulation tasks.

### Performance

Ranking highly on both WorldArena and RoboTwin 2.0, two of the field's most rigorous benchmarks in embodied world models, Motubrain marks a decisive shift in an industry where robotic systems are typically built from task-specific or specialized systems. MotuBrain simultaneously topped two international benchmarks (WorldArena and RoboTwin2.0) in mid-April 2026, a feat no other model had previously achieved.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "800a2290-0a3b-4b83-80f4-39f6d13661b5",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "87dbe0e2-a0b0-459e-83ac-a7f71fb5b851",
  "sourceToolAssistantUUID": "800a2290-0a3b-4b83-80f4-39f6d13661b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T18:09:22.109Z_

Good, I have initial results. Let me now fetch more detailed information on several key items -- the MotuBrain architecture details, the LIBERO-PRO paper specifics, the RoboCasa leaderboard, and the CoRL 2026 deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87dbe0e2-a0b0-459e-83ac-a7f71fb5b851",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLU6wcxhy4Y842Ry7kZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fdcbafd-8335-46b7-821d-f5516c148920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWaCC8XTXSqDjRCvudfEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5520,
      "cache_creation_input_tokens": 5611,
      "cache_read_input_tokens": 11140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5611,
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

_source line 32 · 2026-05-10T18:09:24.740Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JCFtAevm5wvuwd8TzM7xmN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.03827",
  "prompt": "What are the exact performance drops reported? Which models were tested and what were their scores on standard LIBERO vs LIBERO-PRO? Is the 90% to 0% claim accurate? List all numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fdcbafd-8335-46b7-821d-f5516c148920",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLU6wcxhy4Y842Ry7kZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb984f18-d573-431f-aa1a-5bc33abb581a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWaCC8XTXSqDjRCvudfEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5520,
      "cache_creation_input_tokens": 5611,
      "cache_read_input_tokens": 11140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5611,
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

_source line 33 · 2026-05-10T18:09:26.155Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WkWBKSzrw9irNVAyAdy4r4`</summary>

```json
{
  "url": "https://github.com/Zxy-MLlab/LIBERO-PRO",
  "prompt": "Does this GitHub repository exist and what does it contain? What is its current status - number of stars, last update, README content?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb984f18-d573-431f-aa1a-5bc33abb581a",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLU6wcxhy4Y842Ry7kZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07cefb1b-ad7f-4d58-abfd-c026ac6ba5fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWaCC8XTXSqDjRCvudfEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5520,
      "cache_creation_input_tokens": 5611,
      "cache_read_input_tokens": 11140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5611,
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

_source line 34 · 2026-05-10T18:09:28.670Z_

<details><summary>↩ Tool result · `toolu_01JCFtAevm5wvuwd8TzM7xmN`</summary>

```text
# Performance Data from LIBERO-PRO

Based on the provided content, I cannot give you the specific model-by-model performance breakdowns you're requesting. The abstract contains only this summary statement:

"Although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under our generalized setting."

This indicates a dramatic drop from 90%+ to 0%, but the document excerpt doesn't include:
- Names of specific models tested
- Individual model scores on either benchmark
- Detailed performance metrics beyond this general claim
- Breakdown of results across the four perturbation dimensions (objects, initial states, instructions, environments)

To obtain the complete numerical data you're seeking, you would need to access the full paper via the PDF link or HTML version provided on the arXiv page, where the results tables and detailed findings are presumably presented.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb984f18-d573-431f-aa1a-5bc33abb581a",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "fc9a6ab3-1902-4c5a-ab1a-770cc026f70f",
  "sourceToolAssistantUUID": "bb984f18-d573-431f-aa1a-5bc33abb581a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-10T18:09:29.380Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0139gKCcZNgLUHxHdmEhzD4j`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.27792v2",
  "prompt": "Extract all details about the MotuBrain architecture: Does it use a three-stream Mixture-of-Transformers (MoT)? Is there an H-bridge design? What is the exact architecture description? What are the benchmark results on RoboCasa, WorldArena, and other benchmarks? Is it open-source or closed-source?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc9a6ab3-1902-4c5a-ab1a-770cc026f70f",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLU6wcxhy4Y842Ry7kZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1531470a-f9b5-4d4c-9840-53ba6f1ead82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWaCC8XTXSqDjRCvudfEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5520,
      "cache_creation_input_tokens": 5611,
      "cache_read_input_tokens": 11140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5611,
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

_source line 36 · 2026-05-10T18:09:30.356Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ScKwmTHgGxGdDxNiyW8GuN`</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "What are the exact submission deadlines for CoRL 2026? List the abstract deadline and paper deadline with dates and times."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1531470a-f9b5-4d4c-9840-53ba6f1ead82",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLU6wcxhy4Y842Ry7kZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5634861-757a-4042-8200-b50428f27de6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWaCC8XTXSqDjRCvudfEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5520,
      "cache_creation_input_tokens": 5611,
      "cache_read_input_tokens": 11140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5611,
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

_source line 37 · 2026-05-10T18:09:32.321Z_

<details><summary>↩ Tool result · `toolu_01WkWBKSzrw9irNVAyAdy4r4`</summary>

```text
# LIBERO-PRO Repository Overview

Yes, this GitHub repository exists and is actively maintained. Here's what it contains:

## Repository Status
- **Stars:** 247
- **Forks:** 19
- **Last Commit:** 121 commits to master branch
- **License:** MIT (codebase); CC BY 4.0 (datasets)

## Purpose
LIBERO-PRO is "an evaluation extension of the original LIBERO benchmark" designed to assess Vision-Language-Action models more rigorously. The project addresses a core problem: models achieve high performance on known tasks through "mechanical memorization of training scenarios rather than genuine acquisition of transferable task-solving strategies."

## Key Features
The repository implements five generalization dimensions tested through configurable perturbations:
- **Object:** Visual shifts in appearance and scale
- **Position:** Spatial relocation of objects
- **Semantic:** Language paraphrasing
- **Task:** Procedural logic changes
- **Environment:** Cross-environment evaluation

## Recent Updates
Notable recent milestones include:
- Released complete code on GitHub (October 2025)
- Published paper on arXiv (October 2025)
- Uploaded benchmark files to HuggingFace for faster parallel evaluation (November 2025)
- Launched official project website with demonstrations

## Repository Contents
The codebase includes benchmark scripts, perturbation tools, evaluation configurations, and comprehensive documentation for reproducing evaluation experiments on models like OpenVLA and others.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07cefb1b-ad7f-4d58-abfd-c026ac6ba5fe",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "e9a5ec18-6367-47f4-aa5e-5f5e9ee9ac63",
  "sourceToolAssistantUUID": "07cefb1b-ad7f-4d58-abfd-c026ac6ba5fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-10T18:09:32.482Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EPc98ZeXbYQbt2vYyvCiEZ`</summary>

```json
{
  "url": "https://sota.evomind-tech.com/benchmarks/robocasa_gr1_tabletop/",
  "prompt": "What are the current best results and SOTA scores on RoboCasa? List all models and their success rates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9a5ec18-6367-47f4-aa5e-5f5e9ee9ac63",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLU6wcxhy4Y842Ry7kZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f5b27b1-0ab7-441d-89b7-4b9860275882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWaCC8XTXSqDjRCvudfEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5520,
      "cache_creation_input_tokens": 5611,
      "cache_read_input_tokens": 11140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5611,
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

_source line 39 · 2026-05-10T18:09:33.397Z_

<details><summary>↩ Tool result · `toolu_01ScKwmTHgGxGdDxNiyW8GuN`</summary>

```text
Based on the provided web page content, the exact submission deadlines for CoRL 2026 are not specified. The page states: "For paper submission format and timeline, see: [Instruction for Authors](/contributions/instruction-for-authors)" but does not include the actual deadline dates and times on this particular page.

To find the abstract and paper deadlines, you would need to visit the "Instruction for Authors" section linked in the Call for Papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5634861-757a-4042-8200-b50428f27de6",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "067194a0-6303-42cd-a562-30a8dff36cbb",
  "sourceToolAssistantUUID": "c5634861-757a-4042-8200-b50428f27de6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-10T18:09:34.327Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UyMMuvkUHGwJAtr88ZeTaZ`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.20868",
  "prompt": "Extract all details about the timestep-adaptive frequency-gated mechanism. How does it condition attention on noise/timestep levels? Is this specifically for cross-modal attention in diffusion models?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "067194a0-6303-42cd-a562-30a8dff36cbb",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLU6wcxhy4Y842Ry7kZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb617a85-a3f7-4b78-8a6b-33e20b989f87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuWaCC8XTXSqDjRCvudfEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5520,
      "cache_creation_input_tokens": 5611,
      "cache_read_input_tokens": 11140,
      "output_tokens": 726,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5611
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5520,
          "output_tokens": 726,
          "cache_read_input_tokens": 11140,
          "cache_creation_input_tokens": 5611,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5611,
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

_source line 41 · 2026-05-10T18:09:34.597Z_

<details><summary>↩ Tool result · `toolu_01EPc98ZeXbYQbt2vYyvCiEZ`</summary>

```text
I cannot provide the information you're requesting based on the webpage content provided. The page appears to be a navigation/header section for a "VLA SOTA Leaderboard" but doesn't contain any actual benchmark results, model performance data, or success rates for RoboCasa or any other task.

To find current SOTA scores and model results for RoboCasa, you would need to visit the full leaderboard pages, likely through the "Benchmarks" or "Models" sections mentioned in the navigation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f5b27b1-0ab7-441d-89b7-4b9860275882",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "f92d36c8-e304-4a11-acc0-8a7a36ca67eb",
  "sourceToolAssistantUUID": "6f5b27b1-0ab7-441d-89b7-4b9860275882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T18:09:36.793Z_

<details><summary>↩ Tool result · `toolu_0139gKCcZNgLUHxHdmEhzD4j`</summary>

```text
# MotuBrain Architecture and Performance Summary

## Architecture Details

**Three-Stream Design:**
MotuBrain employs a three-stream Mixture-of-Transformers architecture with "text stream, a video stream, and an action stream." The text stream conditions the model without generating output, while video and action streams are trained with flow matching.

**H-Bridge Implementation:**
The model incorporates an H-bridge design where "full V-A joint attention is applied only in the middle 50% of Transformer layers, while the bottom and top 25% layers use decoupled attention." This reduces cross-modal attention costs while maintaining semantic alignment in intermediate layers.

**Multiview Support:**
A unified representation leverages "3D RoPE" with view-dependent offsets for supporting "an arbitrary number of camera views without modifying the backbone architecture."

## Benchmark Results

**RoboTwin 2.0 (Simulation):**
- Clean setting: 95.8% average success rate
- Randomized setting: 96.1% average success rate
- Surpasses 90% on 42 clean and 44 randomized tasks

**WorldArena:**
Achieves the highest EWMScore at 63.77, exceeding the strongest video-generation baseline by approximately four points.

**Real-World Performance:**
- Making Oden task: 98.54 overall score
- Mixing Cocktails: 97.34 overall score
- Adapts to new humanoid embodiments with 50-100 trajectories

## Open Source Status

The document does not explicitly state whether MotuBrain is open-source or closed-source. It references a URL (shengshu.com/en/motubrain) but provides no licensing information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1531470a-f9b5-4d4c-9840-53ba6f1ead82",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "aa80ef2e-cc40-4378-89f7-3b435538181c",
  "sourceToolAssistantUUID": "1531470a-f9b5-4d4c-9840-53ba6f1ead82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T18:09:45.365Z_

<details><summary>↩ Tool result · `toolu_01UyMMuvkUHGwJAtr88ZeTaZ`</summary>

```text
# Timestep-Adaptive Frequency-Gated (TAFG) Mechanism

## Overview
TAFG is a lightweight conditioning module that enhances how low-dose CT conditioning features are injected into latent diffusion's cross-attention layers. It operates specifically on the condition pathway before cross-attention integration.

## Core Design

**Frequency Decomposition:**
The mechanism separates condition features into components: "low- and high-frequency components" via a learnable low-pass operator, distinguishing stable structural information from detail-sensitive responses.

**Timestep-Adaptive Gating:**
TAFG predicts separate gates for each frequency component by combining:
- Current denoising U-Net features (via global average pooling)
- Timestep embeddings

"The two gates control how strongly the low- and high-frequency condition components should be injected" at each denoising step.

## Progressive Detail Release

A critical innovation is timestep-dependent modulation: high-frequency guidance is progressively released through a "release factor" defined as r(t) = (1−t̂)^γ, where t̂ represents normalized timestep progression.

This design ensures the model "relies more on stable structural guidance at early reverse steps and introduces fine details more cautiously as denoising proceeds."

## Implementation Context

TAFG operates exclusively within the conditional diffusion U-Net's conditioning pathway—it's not a general attention mechanism but specifically targets cross-attention feature preparation in medical image restoration, preserving the pretrained autoencoder and sampler unchanged.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb617a85-a3f7-4b78-8a6b-33e20b989f87",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "657e9479-e3b2-4c55-b535-c0b95c447b91",
  "sourceToolAssistantUUID": "cb617a85-a3f7-4b78-8a6b-33e20b989f87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-10T18:09:48.585Z_

Let me fetch the CoRL deadlines from the instructions page, and also get the full LIBERO-PRO paper for exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "657e9479-e3b2-4c55-b535-c0b95c447b91",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLW7UfdSAaFvi7n7YaU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "776bba3c-a5f7-4753-a002-82bf74c659db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3RcLiQHnP1ixFbreTwPZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7883,
      "cache_read_input_tokens": 16751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7883,
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

_source line 45 · 2026-05-10T18:09:50.010Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014kbbm4WPSCAiBPH4YCpBtk`</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "What are the exact submission deadlines for CoRL 2026? List the abstract deadline and paper deadline with exact dates and times."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "776bba3c-a5f7-4753-a002-82bf74c659db",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLW7UfdSAaFvi7n7YaU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05216fe9-8d77-4df2-b6db-4fa114b0c9db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3RcLiQHnP1ixFbreTwPZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7883,
      "cache_read_input_tokens": 16751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7883,
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

_source line 46 · 2026-05-10T18:09:52.479Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01652dgWqD9LZkvp7XEkUVZX`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.03827v1",
  "prompt": "Extract the exact performance numbers from the results tables. Which specific models were evaluated? What were their success rates on standard LIBERO vs LIBERO-PRO? Is the claim of 90% dropping to 0% accurate? List all numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05216fe9-8d77-4df2-b6db-4fa114b0c9db",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLW7UfdSAaFvi7n7YaU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a182d18-a63d-40f1-8372-95e24e862f91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3RcLiQHnP1ixFbreTwPZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7883,
      "cache_read_input_tokens": 16751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7883,
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

_source line 47 · 2026-05-10T18:09:53.916Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014i8E5wnGeEzV2hYP9obxyF`</summary>

```json
{
  "url": "https://sharinka0715.github.io/X-WAM/",
  "prompt": "What is X-WAM? What are its exact benchmark results on RoboCasa? What is its architecture? What success rates does it achieve?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a182d18-a63d-40f1-8372-95e24e862f91",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLW7UfdSAaFvi7n7YaU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4f173f9-cdf1-4bc8-b69a-912ee3a37464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3RcLiQHnP1ixFbreTwPZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7883,
      "cache_read_input_tokens": 16751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7883,
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

_source line 48 · 2026-05-10T18:09:54.832Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JvrsK3Y1jZbyNcRtzAg69U`</summary>

```json
{
  "query": "MotuBrain open source code weights release ShengShu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4f173f9-cdf1-4bc8-b69a-912ee3a37464",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLW7UfdSAaFvi7n7YaU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "472ffe1a-2592-4cdf-a6c7-e4ba5f30cefc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3RcLiQHnP1ixFbreTwPZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7883,
      "cache_read_input_tokens": 16751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7883,
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

_source line 49 · 2026-05-10T18:09:55.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JrB6bxdVYeHyq2y5aFYBHc`</summary>

```json
{
  "query": "\"noise conditioned\" \"cross attention\" \"diffusion policy\" robotics 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "472ffe1a-2592-4cdf-a6c7-e4ba5f30cefc",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLW7UfdSAaFvi7n7YaU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a634aa33-9c95-42e0-99b9-e978e877c2dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3RcLiQHnP1ixFbreTwPZW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7883,
      "cache_read_input_tokens": 16751,
      "output_tokens": 461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7883
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 461,
          "cache_read_input_tokens": 16751,
          "cache_creation_input_tokens": 7883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7883,
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

_source line 50 · 2026-05-10T18:09:56.008Z_

<details><summary>↩ Tool result · `toolu_014kbbm4WPSCAiBPH4YCpBtk`</summary>

```text
# CoRL 2026 Submission Deadlines

I cannot provide the exact abstract and paper submission deadlines with specific dates and times. While the instructions mention that "deadlines are final" and reference an abstract submission deadline and a paper deadline (noting that "the paper submission deadline is Thursday (5/28) EOD"), the complete deadline information with times is not explicitly listed in the provided content.

The document indicates deadlines exist but does not present them in a consolidated "Key Dates" section with all specific dates and times clearly stated. For accurate deadline information, you should consult the OpenReview submission portal directly at: https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05216fe9-8d77-4df2-b6db-4fa114b0c9db",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "44d47b3b-d123-4549-b4b9-33397863dd84",
  "sourceToolAssistantUUID": "05216fe9-8d77-4df2-b6db-4fa114b0c9db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-10T18:09:57.447Z_

<details><summary>↩ Tool result · `toolu_014i8E5wnGeEzV2hYP9obxyF`</summary>

```text
# X-WAM Overview

**What is X-WAM?**

X-WAM is "a unified 4D World Action Model that simultaneously targets high-fidelity video generation, 3D spatial reconstruction, and real-time policy execution." It combines video generation capabilities with robotic control by predicting multi-view RGB-D videos and extracting spatial information for policy decisions.

**Architecture**

The system builds on a pretrained video diffusion model (Wan2.2-5B) with two key innovations:

1. **Lightweight Depth Adaptation**: Rather than expanding the sequence length, the model replicates final diffusion transformer blocks into a dedicated depth branch using unilateral cross-attention, preserving visual priors while enabling spatial reconstruction.

2. **Asynchronous Noise Sampling (ANS)**: This technique decodes robot actions in just a few initial denoising steps for rapid execution, while continuing full denoising for high-quality video output.

**Benchmark Performance**

On the RoboCasa benchmark specifically, the model achieves "79.2% average success rate." It additionally reaches "90.7% average success rate on RoboTwin 2.0 benchmarks."

The system was trained on over 5,800 hours of robotic data and demonstrates strong performance on both simulation benchmarks and real-world robotic manipulation tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4f173f9-cdf1-4bc8-b69a-912ee3a37464",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "a5e3d5b1-b29c-49db-83c3-37c46f0adec0",
  "sourceToolAssistantUUID": "e4f173f9-cdf1-4bc8-b69a-912ee3a37464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-10T18:09:57.773Z_

<details><summary>↩ Tool result · `toolu_01652dgWqD9LZkvp7XEkUVZX`</summary>

```text
# LIBERO-PRO Performance Analysis

## Models Evaluated

Three state-of-the-art vision-language-action models were tested:
- **OpenVLA** (with four official checkpoints)
- **pi0** (single checkpoint)
- **pi0.5** (single checkpoint)

## Performance Numbers: Standard LIBERO vs LIBERO-PRO

### Claim Verification

The paper's assertion that performance "collapses to 0.0%" is partially accurate but requires nuance:

**Standard LIBERO Success Rates (Original/Ori column):**
- OpenVLA: 93-99% across benchmarks
- pi0: 82-98% across benchmarks  
- pi0.5: 93-98% across benchmarks

**LIBERO-PRO Spatial Position Perturbation Results (Pos column):**
- OpenVLA: **0.00%** across all four benchmark suites
- pi0: **0.00%** across all four benchmark suites
- pi0.5: 0.08-0.38% (slightly better resilience)

### Key Numerical Examples

From **libero-goal benchmark** (Table 2):
- OpenVLA original: 0.98 → position perturbed: 0.00
- pi0 original: 0.92 → position perturbed: 0.00
- pi0.5 original: 0.97 → position perturbed: 0.38

The paper accurately documents "the models cannot cope with changes in object positions," with near-complete collapse under spatial perturbations despite high baseline performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a182d18-a63d-40f1-8372-95e24e862f91",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "1440dba9-4e74-4ddf-9a5c-92f673b3d620",
  "sourceToolAssistantUUID": "0a182d18-a63d-40f1-8372-95e24e862f91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-10T18:10:02.082Z_

<details><summary>↩ Tool result · `toolu_01JvrsK3Y1jZbyNcRtzAg69U`</summary>

```text
Web search results for query: "MotuBrain open source code weights release ShengShu"

Links: [{"title":"ShengShu Technology Unveils Motubrain: A Unified \"World Action Model\" to Solve the Robotics Scaling Problem | Humanoids Daily","url":"https://www.humanoidsdaily.com/news/shengshu-technology-unveils-motubrain-a-unified-world-action-model-to-solve-the-robotics-scaling-problem"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://www.prnewswire.com/news-releases/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence-302757280.html"},{"title":"ChinaPulse.com - ShengShu Technology Unveils World Action Model “Motubrain”: One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://www.chinapulse.com/data-news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/"},{"title":"One brain for all: China builds unified AI model to handle complex multi-task robotics","url":"https://interestingengineering.com/ai-robotics/motubrain-unified-robot-ai-model"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://aithority.com/robots/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | The Manila Times","url":"https://www.manilatimes.net/2026/04/29/tmt-newswire/pr-newswire/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/2331652"},{"title":"ShengShu Technology Unveils World Action Model “Motubrain”: One Brain, Infinite Possibilities for Robotic Intelligence – Digital Media Net","url":"https://digitalmedianet.com/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/26497/"},{"title":"MotuBrain | ShengShu Technology","url":"https://www.roboticstomorrow.com/content.php?track=26497"},{"title":"Shengshu Technology Launches Motubrain World-Action Model - Pandaily","url":"https://pandaily.com/shengshu-technology-launches-motubrain-world-action-model"}]

Based on the search results, here's what I found about MotuBrain and ShengShu Technology:

## Overview

ShengShu Technology has announced Motubrain, a hardware-agnostic robotic brain that unifies perception and action to outperform traditional VLA models on global benchmarks.

## Model Architecture and Capabilities

The model leverages Mixture-of-Transformers architecture to jointly learn video generation, world modeling, and action control, achieving a 13.55x increase in data efficiency over traditional methods. At the architectural level, MotuBrain is built on the UniDiffuser unified modeling framework. Through cross-modal priors fusion, it integrates VLM, video generation models, and action experts into a single model.

## Performance and Rankings

Motubrain currently ranks top three on the WorldArena benchmark and RoboTwin 2.0, where it is the only model to exceed a 95% success rate in randomized environments.

## Current Deployment

Motubrain is not a research model awaiting commercialisation; it is operational. Several leading robotics companies are already using MotuBrain in active robot training programs, deploying its cross-embodiment, multi-skill capabilities on real hardware across industrial, commercial, and home environments.

## Funding

Backed by a $293 million Series B led by Alibaba Cloud, the startup is positioning Motubrain as a hardware-agnostic "intelligence layer" for industrial, commercial, and home robotics.

The search results do not contain specific information about open-source code or weight releases for MotuBrain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "472ffe1a-2592-4cdf-a6c7-e4ba5f30cefc",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "f563a063-8c22-45e7-9efd-e703a6b4c04e",
  "sourceToolAssistantUUID": "472ffe1a-2592-4cdf-a6c7-e4ba5f30cefc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-10T18:10:03.148Z_

<details><summary>↩ Tool result · `toolu_01JrB6bxdVYeHyq2y5aFYBHc`</summary>

```text
Web search results for query: ""noise conditioned" "cross attention" "diffusion policy" robotics 2025 2026"

Links: [{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"Diffusion Policy: Teaching Robots to Act by Denoising","url":"https://vizuara.substack.com/p/diffusion-policy-teaching-robots"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Video Generators are Robot Policies - Columbia University","url":"https://videopolicy.cs.columbia.edu/assets/video_policy.pdf"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11","url":"https://dl.acm.org/doi/10.1177/02783649241273668"},{"title":"Paper Review: Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | by Yutong Zhang | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/diffusion-policy-applying-diffusion-model-to-policy-learning-8ee16fc056bb"}]

I found several relevant results about diffusion policy in robotics. Here are the key findings:

## Diffusion Policy Overview

Diffusion Policy is a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process. It consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9% across 12 different tasks from 4 different robot manipulation benchmarks.

## Architecture and Conditioning

The approach uses two main architectural variants:

1. **CNN-based approach**: FiLM (feature-wise linear modulation) conditioning of the observation feature is applied to every convolution layer, channel-wise.

2. **Transformer-based approach**: The embedding of observation is passed into a multi-head cross-attention layer of each transformer decoder. More specifically, observation features are provided as a separate sequence that the action tokens attend to via cross-attention.

## Noise Conditioning in the Diffusion Process

The noisy action sequence is treated as a sequence of tokens, with the diffusion timestep k prepended as a special token. Starting from K drawn from Gaussian noise, the output of noise-prediction network is subtracted, repeating K times to get the denoised action sequence.

## Recent 2025-2026 Developments

Frans et al. (2025) conditions the model not only on the time-step, but also on the step-size. Additionally, there have been developments in optimizing diffusion transformers for on-device deployment and applying diffusion policy concepts to video-based policy learning for robotics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a634aa33-9c95-42e0-99b9-e978e877c2dc",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "cca9c453-2ee2-4082-8f1e-c416dacefadc",
  "sourceToolAssistantUUID": "a634aa33-9c95-42e0-99b9-e978e877c2dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-10T18:10:09.698Z_

Let me fetch the CoRL deadlines from OpenReview and verify if MotuBrain is open-source.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cca9c453-2ee2-4082-8f1e-c416dacefadc",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLXRZ8rbqi7fgEVD6Wc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e55fa41e-bffa-47cd-878a-4854a8bdf458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDRFjhXCBvLQde3psUvkfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3629,
      "cache_read_input_tokens": 24634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3629,
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

_source line 56 · 2026-05-10T18:10:12.681Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GmNo34XAYow9ipV7nKss6H`</summary>

```json
{
  "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf",
  "prompt": "What are the exact CoRL 2026 deadlines listed? Abstract deadline? Paper deadline? What are the exact dates?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e55fa41e-bffa-47cd-878a-4854a8bdf458",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLXRZ8rbqi7fgEVD6Wc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07b1a272-075a-4b9d-8077-e46e8d9ec37d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDRFjhXCBvLQde3psUvkfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3629,
      "cache_read_input_tokens": 24634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3629,
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

_source line 57 · 2026-05-10T18:10:15.777Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NH3ATX6nLBwt73cddbGUJf`</summary>

```json
{
  "url": "https://www.humanoidsdaily.com/news/shengshu-technology-unveils-motubrain-a-unified-world-action-model-to-solve-the-robotics-scaling-problem",
  "prompt": "Is MotuBrain open-source? Are model weights publicly available? Is the code open? Is it commercial/closed-source? Any mentions of code or weight release plans?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07b1a272-075a-4b9d-8077-e46e8d9ec37d",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLXRZ8rbqi7fgEVD6Wc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d597db8-4387-4b30-9fc6-d8aa945a0e30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDRFjhXCBvLQde3psUvkfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3629,
      "cache_read_input_tokens": 24634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3629,
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

_source line 58 · 2026-05-10T18:10:16.092Z_

<details><summary>↩ Tool result · `toolu_01GmNo34XAYow9ipV7nKss6H`</summary>

```text
# CoRL 2026 Deadlines

Based on the updated conference details, here are the exact deadlines for CoRL 2026:

## Abstract Submission Deadline
- **Date:** May 26, 2026
- **Time:** 11:59 UTC

## Paper Submission Deadline
- **Date:** May 29, 2026
- **Time:** 11:59 UTC

## Additional Conference Details
- **Conference Dates:** November 9-12, 2026
- **Venue:** JW Marriott Austin, 110 E 2nd St, Austin, TX 78701
- **Note:** Workshops on Nov 9, main conference Nov 10-12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07b1a272-075a-4b9d-8077-e46e8d9ec37d",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "f4ef5213-d099-4e97-b24c-ceaae811fb2d",
  "sourceToolAssistantUUID": "07b1a272-075a-4b9d-8077-e46e8d9ec37d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-10T18:10:17.103Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ESxAu4RWxiaU2CAhTkEU7s`</summary>

```json
{
  "query": "\"diffusion\" \"noise level\" OR \"timestep\" \"attention gate\" OR \"attention modulation\" \"cross-modal\" robot action 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4ef5213-d099-4e97-b24c-ceaae811fb2d",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLXRZ8rbqi7fgEVD6Wc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67fba340-ed50-4dbb-8332-8080bf49eb5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDRFjhXCBvLQde3psUvkfS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3629,
      "cache_read_input_tokens": 24634,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3629
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 375,
          "cache_read_input_tokens": 24634,
          "cache_creation_input_tokens": 3629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3629,
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

_source line 60 · 2026-05-10T18:10:19.093Z_

<details><summary>↩ Tool result · `toolu_01NH3ATX6nLBwt73cddbGUJf`</summary>

```text
# MotuBrain Open Source Status

The article does not contain any information regarding whether MotuBrain is open-source, if model weights are publicly available, or if there are plans to release code. 

The piece focuses on the technology's capabilities, architecture, and benchmark performance, but makes no mention of its licensing status or availability to the public. The article presents MotuBrain as a commercial offering deployed through partnerships with robotics firms, but provides no explicit statement about open-source release plans.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d597db8-4387-4b30-9fc6-d8aa945a0e30",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "40a25978-ca08-4d10-a6ab-d3d553ba810d",
  "sourceToolAssistantUUID": "6d597db8-4387-4b30-9fc6-d8aa945a0e30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-10T18:10:26.515Z_

<details><summary>↩ Tool result · `toolu_01ESxAu4RWxiaU2CAhTkEU7s`</summary>

```text
Web search results for query: ""diffusion" "noise level" OR "timestep" "attention gate" OR "attention modulation" "cross-modal" robot action 2025 2026"

Links: [{"title":"Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Lv_Rethinking_Cross-Modal_Interaction_in_Multimodal_Diffusion_Transformers_ICCV_2025_paper.pdf"},{"title":"Abstracting Robot Manipulation Skills via Mixture-of- ...","url":"https://arxiv.org/pdf/2601.21251"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"10 Open Challenges Steering the Future of Vision-Language-Action Models","url":"https://arxiv.org/html/2511.05936v1"},{"title":"Diffusion Transformer (DiT) — Architecture for Video & Robot Control | Claru","url":"https://claru.ai/glossary/diffusion-transformer"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"}]

I've successfully performed a web search with your query. Here's a summary of the relevant findings:

## Key Research Areas Found

**Cross-Modal Attention in Diffusion Models:**
TACA is a parameter-efficient method that dynamically rebalances cross-modal attention in multimodal diffusion models, which directly addresses attention modulation in diffusion-based systems.

**Diffusion-Based Robot Action Models:**
Diffusion-based decoders and hierarchical fusion significantly improve manipulation success in vision-language-action (VLA) systems. Skill Mixture-of-Experts Policy (SMP) is a diffusion-based mixture-of-experts policy that performs skill abstraction in a locally whitened action space.

**Timestep and Noise Level in Diffusion:**
AdaLN-Zero is a parameter-efficient method for injecting timestep and class information that outperformed cross-attention and in-context conditioning in diffusion transformers. This approach has been adopted for robot control systems.

**Diffusion Transformers for Robot Control:**
DiT architectures now power Sora, Stable Diffusion 3, and emerging robot control systems like pi-zero — generating everything from photorealistic video to multi-modal robot action trajectories. Physical Intelligence's pi-zero uses a DiT-like architecture where the denoising process generates multi-modal robot action sequences (arm position, gripper, base velocity) conditioned on image and language embeddings.

**Multi-Modal Cross-Conditioning:**
Low-level action experts can be implemented either as a diffusion-based or an autoregressive model trained on real robot action datasets, often incorporating multiple sensory modalities for robot control.

The search results show active research in 2025-2026 combining diffusion models, attention mechanisms, and cross-modal fusion for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67fba340-ed50-4dbb-8332-8080bf49eb5b",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "40acc938-a1b1-446d-88fe-40a9421b595b",
  "sourceToolAssistantUUID": "67fba340-ed50-4dbb-8332-8080bf49eb5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-10T18:10:30.682Z_

Let me do one more search to verify the CoRL deadline discrepancy (May 28 vs May 29 for paper submission), and check if MotuBrain has released anything open-source.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40acc938-a1b1-446d-88fe-40a9421b595b",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLZ9RLXTR6BNdWRHjNm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec37592d-f841-4b35-800e-fd1c3f16aadb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SN47HKUTogL1QNjNtEeDF9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1756,
      "cache_read_input_tokens": 28263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1756,
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

_source line 63 · 2026-05-10T18:10:32.170Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012Ng7eK6dksnZVGY6gtWpRQ`</summary>

```json
{
  "url": "https://www.corl.org/",
  "prompt": "What are the exact important dates and deadlines for CoRL 2026? Abstract deadline, paper submission deadline, notification dates, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec37592d-f841-4b35-800e-fd1c3f16aadb",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLZ9RLXTR6BNdWRHjNm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c853aa0c-9828-458c-b5d6-9c306c98eca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SN47HKUTogL1QNjNtEeDF9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1756,
      "cache_read_input_tokens": 28263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1756,
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

_source line 64 · 2026-05-10T18:10:32.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016odp2ABwZVADposZ9gbg8K`</summary>

```json
{
  "query": "MotuBrain arxiv paper code github open source weights huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c853aa0c-9828-458c-b5d6-9c306c98eca3",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLZ9RLXTR6BNdWRHjNm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e299e89b-c06b-42d1-ac43-cba0378c2bc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SN47HKUTogL1QNjNtEeDF9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1756,
      "cache_read_input_tokens": 28263,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1756
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 28263,
          "cache_creation_input_tokens": 1756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1756,
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

_source line 65 · 2026-05-10T18:10:35.797Z_

<details><summary>↩ Tool result · `toolu_012Ng7eK6dksnZVGY6gtWpRQ`</summary>

```text
Based on the webpage content provided, I cannot give you the specific deadlines you're asking about. 

The page only mentions that "The [Call for Papers](/contributions/call-for-papers) and [key dates](/home) are now available" as of January 25th, but the actual deadline dates themselves are not displayed on this homepage.

To find the exact abstract submission deadline, paper deadline, and notification dates, you would need to visit the full Call for Papers page or the key dates section, which are referenced but not detailed in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c853aa0c-9828-458c-b5d6-9c306c98eca3",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "7e4cb931-0948-46b3-9347-1bbdf795a87d",
  "sourceToolAssistantUUID": "c853aa0c-9828-458c-b5d6-9c306c98eca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-10T18:10:37.757Z_

<details><summary>↩ Tool result · `toolu_016odp2ABwZVADposZ9gbg8K`</summary>

```text
Web search results for query: "MotuBrain arxiv paper code github open source weights huggingface"

Links: [{"title":"Trending Papers - Hugging Face","url":"https://huggingface.co/papers/trending"},{"title":"BAAI/bge-m3 · Hugging Face","url":"https://huggingface.co/BAAI/bge-m3"},{"title":"Paper Pages · Hugging Face","url":"https://huggingface.co/docs/hub/en/paper-pages"},{"title":"GitHub - Shibli-Nomani/Open-Source-Models-with-Hugging-Face: Open Source Models With Hugging Face · GitHub","url":"https://github.com/Shibli-Nomani/Open-Source-Models-with-Hugging-Face"},{"title":"Paper page - Advancing Open-source World Models","url":"https://huggingface.co/papers/2601.20540"},{"title":"Forecasting Open-Weight AI Model Growth on Hugging Face","url":"https://arxiv.org/html/2502.15987v1"},{"title":"Paper page - Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Multimodal Models","url":"https://huggingface.co/papers/2409.17146"},{"title":"Hugging Face · GitHub","url":"https://github.com/huggingface"},{"title":"GitHub - ksm26/Open-Source-Models-with-Hugging-Face: \"Open Source Models with Hugging Face\" course empowers you with the skills to leverage open-source models from the Hugging Face Hub for various tasks in NLP, audio, image, and multimodal domains. · GitHub","url":"https://github.com/ksm26/Open-Source-Models-with-Hugging-Face"},{"title":"facebook/cwm · Hugging Face","url":"https://huggingface.co/facebook/cwm"}]

The search results don't contain specific information about MotuBrain. The results returned are general information about open-source models on Hugging Face, GitHub repositories, and various other AI models, but nothing specifically about MotuBrain's arxiv paper, code, or weights.

To find the MotuBrain project, you may want to try:

1. Searching directly on arXiv.org with "MotuBrain"
2. Searching on GitHub for "MotuBrain"
3. Checking Hugging Face Hub directly for MotuBrain models
4. Trying a more specific search query if you have additional details about the project (such as the authors' names or publication date)

Would you like me to perform a more targeted search with different keywords, or do you have any additional information about MotuBrain that could help narrow down the search?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e299e89b-c06b-42d1-ac43-cba0378c2bc3",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "007fa1b4-804c-4a7a-8656-077ae50d1d04",
  "sourceToolAssistantUUID": "e299e89b-c06b-42d1-ac43-cba0378c2bc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-10T18:10:42.563Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016ggndJbQf1gM3637Qk3qQU`</summary>

```json
{
  "url": "https://chinaresearchcollective.substack.com/p/motubrain-a-world-action-model-by",
  "prompt": "Is MotuBrain open-source or closed-source? Are model weights or code available? What are the exact architecture details about the H-bridge design and three-stream MoT? Any mention of commercial vs academic availability?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "007fa1b4-804c-4a7a-8656-077ae50d1d04",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLZyU5S43PCZ2bsp4rZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12de11fd-c567-4f15-a0d4-172de07f4359",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FAhMsmJYLKFKTQQco3MLwn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 30019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
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

_source line 68 · 2026-05-10T18:10:44.951Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XhKLcTghseRrxXcGv9G7AD`</summary>

```json
{
  "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Lv_Rethinking_Cross-Modal_Interaction_in_Multimodal_Diffusion_Transformers_ICCV_2025_paper.pdf",
  "prompt": "What is this paper about? Does it condition cross-modal attention on noise levels or timesteps in diffusion models? What is the TACA method? How does it modulate attention based on the denoising stage?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12de11fd-c567-4f15-a0d4-172de07f4359",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLZyU5S43PCZ2bsp4rZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d3b3261-932d-412f-b01c-be99ba2e59bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FAhMsmJYLKFKTQQco3MLwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 30019,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1070
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 310,
          "cache_read_input_tokens": 30019,
          "cache_creation_input_tokens": 1070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1070,
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

_source line 69 · 2026-05-10T18:10:47.272Z_

<details><summary>↩ Tool result · `toolu_016ggndJbQf1gM3637Qk3qQU`</summary>

```text
# MotuBrain Availability Status

Based on the provided content, **there is no information about whether MotuBrain is open-source or closed-source**, nor any details regarding model weights, code availability, or specific architecture particulars.

## What We Know

The article mentions that Shengshu "open-sourced **Motus**, a general-purpose foundation world model" in December 2025, which preceded MotuBrain. However, MotuBrain itself is described as "a comprehensively upgraded **commercial model**" that "inherits Motus's complete core technical architecture."

The distinction between the open-sourced predecessor (Motus) and the commercial successor (MotuBrain) suggests different availability models, but the document provides no explicit statement about MotuBrain's licensing or whether weights/code will be released.

## Architectural Details

The content describes MotuBrain's general approach—such as using "UniDiffuser" for unified video-action modeling and "MoT (Mixture-of-Transformers)" architecture—but does not provide implementation specifics, H-bridge design details, or technical depth required for reproduction.

**Bottom line:** This article is promotional rather than technical documentation and deliberately avoids exposing implementation details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12de11fd-c567-4f15-a0d4-172de07f4359",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "bdc12f1a-0b6b-468b-a9d9-537b7c89cf8f",
  "sourceToolAssistantUUID": "12de11fd-c567-4f15-a0d4-172de07f4359",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-10T18:10:53.318Z_

<details><summary>↩ Tool result · `toolu_01XhKLcTghseRrxXcGv9G7AD`</summary>

```text
# Summary of "Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers"

## Paper Focus

This paper addresses limitations in Multimodal Diffusion Transformers (MM-DiTs) for text-to-image generation. The authors identify that models like FLUX struggle with precise semantic alignment between text prompts and generated images.

## Key Problems Identified

The paper reveals two critical issues in MM-DiT attention mechanisms:

1. **Cross-modal attention suppression**: The overwhelming number of visual tokens dilutes textual guidance in the unified softmax function, causing visual tokens to pay less attention to text compared to traditional cross-attention approaches.

2. **Timestep insensitivity**: Current MM-DiTs employ static attention weighting across all denoising steps, which fails to account for the time-varying demands of semantic composition versus detail refinement.

## TACA Method

The authors propose **Temperature-Adjusted Cross-modal Attention (TACA)**, which introduces:

- **Modality-specific temperature scaling** to mitigate cross-attention suppression by rebalancing multimodal interactions
- **Timestep-dependent adjustments** that dynamically adapt attention based on the denoising stage

According to the paper, "TACA only requires a temperature coefficient that adapts to denoising timesteps, allowing for easy implementation with minimal code modifications."

## Results

When combined with LoRA fine-tuning, TACA achieves substantial improvements on benchmarks, including 16.4% gains in spatial relationship understanding and 28.3% improvements in shape accuracy across tested models.

[Binary content (application/pdf, 9.1MB) also saved to /home/ubuntu/.claude-account-2/projects/-/8e99552a-79ce-459a-a014-24550f7cb66f/tool-results/webfetch-1778436647417-qw7znr.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d3b3261-932d-412f-b01c-be99ba2e59bd",
  "isSidechain": true,
  "promptId": "e2a8fedd-be84-4490-ac49-7454b062e40b",
  "agentId": "acb79247c2bab8e03",
  "type": "user",
  "uuid": "5a7f0345-82ba-4a6e-a306-b412eddd1f0b",
  "sourceToolAssistantUUID": "3d3b3261-932d-412f-b01c-be99ba2e59bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-10T18:11:55.800Z_

Now I have comprehensive information. Here is the full report:

---

## Verification Report

### 1. LIBERO-PRO Benchmark

**Verdict: EXISTS and claims are largely ACCURATE.**

- The paper is real: [arXiv:2510.03827](https://arxiv.org/abs/2510.03827), published October 2025.
- The GitHub repo exists at [github.com/Zxy-MLlab/LIBERO-PRO](https://github.com/Zxy-MLlab/LIBERO-PRO) -- 247 stars, 19 forks, MIT license, actively maintained with 121 commits.
- **Performance drops verified:** Three models were tested -- OpenVLA, pi0, and pi0.5.
  - Standard LIBERO success rates: OpenVLA 93-99%, pi0 82-98%, pi0.5 93-98%.
  - Under spatial position perturbation: OpenVLA drops to **0.00%** across all four benchmark suites; pi0 drops to **0.00%**; pi0.5 drops to 0.08-0.38%.
  - The "90% to 0%" claim is **accurate for position perturbation** on OpenVLA and pi0. pi0.5 shows marginal resilience but still near-zero.
- The benchmark tests five perturbation dimensions: object appearance, spatial position, instruction paraphrasing, task logic, and environment replacement.

### 2. RoboCasa SOTA

**Verdict: The 67-79% range is ACCURATE and reflects current known results.**

- **67.1%**: NVIDIA's Cosmos-Policy-RoboCasa-Predict2-2B achieves 67.1% average success rate on the original RoboCasa 24-task benchmark ([HuggingFace model card](https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B)).
- **79.2%**: [X-WAM](https://sharinka0715.github.io/X-WAM/) (a unified 4D World Action Model pretrained on 5,800+ hours of robotic data) achieves 79.2% average success rate on RoboCasa. It also achieves 90.7% on RoboTwin 2.0.
- **RoboCasa365** was released February 2026 with 365 tasks across 2,500 kitchen environments, published at ICLR 2026 ([OpenReview](https://openreview.net/forum?id=tQJYKwc3n4)). There is now a VLA SOTA leaderboard at [sota.evomind-tech.com](https://sota.evomind-tech.com/benchmarks/robocasa_gr1_tabletop/).
- **MotuBrain** (see below) did NOT report RoboCasa numbers specifically -- it topped WorldArena and RoboTwin 2.0 instead.
- So the claim of "67-79% SOTA with meaningful headroom" is well-grounded: 67% is the Cosmos baseline, 79% is X-WAM's best, and headroom above 80% clearly exists.

### 3. MotuBrain

**Verdict: EXISTS, architecture claims are ACCURATE, it is COMMERCIAL/CLOSED-SOURCE.**

- MotuBrain was announced April 29, 2026 by ShengShu Technology (Shengshu AI), backed by $293M Series B from Alibaba Cloud.
- arXiv paper: [2604.27792](https://arxiv.org/html/2604.27792v2).
- **Three-stream MoT: CONFIRMED.** The architecture uses three streams in a Mixture-of-Transformers: text stream, video stream, and action stream. The text stream conditions without generating output; video and action are trained with flow matching.
- **H-bridge design: CONFIRMED.** The paper describes: "full V-A joint attention is applied only in the middle 50% of Transformer layers, while the bottom and top 25% layers use decoupled attention." This is the H-bridge pattern -- full cross-modal interaction in the middle layers, decoupled processing at the edges.
- **Benchmark results:** #1 on WorldArena (EWMScore 63.77) and RoboTwin 2.0 (95.8% clean, 96.1% randomized). Only model to exceed 95% success rate in randomized RoboTwin environments.
- **Open-source status:** MotuBrain itself is **commercial/closed-source**. ShengShu previously open-sourced **Motus** (the predecessor foundation world model) in December 2025, but MotuBrain is described as a "comprehensively upgraded commercial model." No code, weights, or GitHub repo for MotuBrain are publicly available. It is already deployed with partner robotics companies.

### 4. Competing Noise-Conditioned Attention Work

**Verdict: Related work exists but NO exact match to "conditioning cross-modal attention on noise levels in diffusion action models" was found.**

The closest relevant work:

- **TACA (Temperature-Adjusted Cross-modal Attention)** -- ICCV 2025 paper "[Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers](https://openaccess.thecvf.com/content/ICCV2025/papers/Lv_Rethinking_Cross-Modal_Interaction_in_Multimodal_Diffusion_Transformers_ICCV_2025_paper.pdf)." This is the most directly relevant: it introduces timestep-dependent temperature scaling for cross-modal attention in MM-DiTs. It identifies that static attention weighting across all denoising steps is suboptimal and proposes dynamic adjustment based on denoising stage. Achieves 16.4% spatial and 28.3% shape accuracy gains. However, this is for **text-to-image generation**, not robot action diffusion.

- **TAFG-MAN (Timestep-Adaptive Frequency-Gated)** -- [arXiv:2603.20868](https://arxiv.org/html/2603.20868). Decomposes condition features into low/high-frequency components and applies timestep-adaptive gates. Uses a release factor r(t) = (1-t_hat)^gamma for progressive detail injection. Applied to **medical imaging (low-dose CT)**, not robotics.

- **Tgate** -- A training-free method that caches cross-attention output once it converges during inference and keeps it fixed for remaining steps. Shows cross-attention has semantics-planning and fidelity-improving stages.

- **LoRA Conditioning on Attention Layers** -- [arXiv:2405.03958](https://arxiv.org/html/2405.03958v3). Shows LoRA conditioning on attention layers improves diffusion model quality, but this is general conditioning, not specifically noise-level-aware gating.

- In **diffusion policy for robotics** (Chi et al.), the timestep k is prepended as a special token but attention is NOT explicitly modulated based on noise level -- it is standard transformer cross-attention throughout.

**Bottom line:** The idea of explicitly conditioning cross-modal attention weights on the diffusion noise level/timestep in a **robotic action diffusion model** appears to be novel or at minimum very sparsely explored. TACA (ICCV 2025) is the closest conceptual predecessor but applies to image generation, not action prediction. No published work was found that does this specifically for VLA/diffusion policy models.

### 5. CoRL 2026 Deadlines

**Verdict: PARTIALLY CORRECT -- there is a discrepancy on the paper deadline.**

From the [HuggingFace AI Deadlines tracker](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf) and [CoRL 2026 official site](https://www.corl.org/):

- **Abstract submission deadline: May 26, 2026, 11:59 UTC** -- CONFIRMED
- **Paper submission deadline:** The AI deadlines tracker says **May 29, 2026, 11:59 UTC**, but the CoRL instructions page notes "the paper submission deadline is Thursday (5/28) EOD." May 28, 2026 is a Thursday; May 29 is a Friday. There is a **discrepancy** between sources -- the proposal's claim of May 29 may be off by one day. Recommend checking [OpenReview](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference) directly for the authoritative deadline.
- **Conference dates:** November 9-12, 2026 at JW Marriott Austin, TX. Workshops Nov 9, main conference Nov 10-12.
- CoRL is ranked **A*** (CORE global top 5%).

---

**Summary of key risk flags for the proposal:**
1. LIBERO-PRO claims check out.
2. RoboCasa 67-79% SOTA range is accurate.
3. MotuBrain is a direct competitor but is commercial/closed -- any open-source WAM approach has differentiation.
4. The noise-conditioned cross-modal attention idea appears to have no direct prior art in robotic diffusion policies specifically -- TACA (ICCV 2025) is the closest analog but in a different domain.
5. Double-check the CoRL paper deadline: it may be May 28 (Thursday EOD), not May 29.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a7f0345-82ba-4a6e-a306-b412eddd1f0b",
  "isSidechain": true,
  "agentId": "acb79247c2bab8e03",
  "requestId": "req_011CauLb82o4KqQCZqCe6j1n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2dcff29-2544-4c51-b503-62726699bd62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e99552a-79ce-459a-a014-24550f7cb66f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpZCXA6uEZKJwZivScDQc7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 31089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1089,
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
