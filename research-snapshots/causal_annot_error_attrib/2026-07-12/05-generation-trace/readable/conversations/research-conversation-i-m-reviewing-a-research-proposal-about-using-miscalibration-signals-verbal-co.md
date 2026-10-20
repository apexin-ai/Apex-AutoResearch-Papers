# Research conversation: I'm reviewing a research proposal about using miscalibration signals (verbal confidence vs. internal probe uncertainty) 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a7fa97b3924f82a62.jsonl`
- **Structured JSON:** [`f4562d20c87c8776f39f.json`](../../sessions/f4/f4562d20c87c8776f39f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

58 recorded events

### User

_source line 1 · 2026-05-16T09:00:30.742Z_

I'm reviewing a research proposal about using miscalibration signals (verbal confidence vs. internal probe uncertainty) to trigger logit-level interventions during LLM generation to reduce hallucinations. I need to find competing and potentially overlooked work from 2025-2026. 

Do multiple WebSearch queries for:

1. "hallucination detection internal representations logit intervention 2025 2026" - find any work that uses internal model signals to modify logits during generation
2. "calibration-aware decoding LLM 2025 2026" - methods that use calibration signals during decoding
3. "uncertainty-guided generation language model 2026" - uncertainty-based generation control
4. "probe-guided decoding hallucination 2025 2026" - using trained probes to guide decoding
5. "verbal confidence mismatch hallucination 2025 2026" - work on verbal vs internal confidence gaps
6. "logit bias hallucination reduction LLM" - logit manipulation for hallucination reduction
7. "site:arxiv.org contrastive decoding hallucination 2026" - latest contrastive decoding work
8. "training-free hallucination mitigation inference time 2026" - training-free inference-time methods

For any highly relevant papers you find that are NOT in this list of already-cited works, report them with title, venue/arXiv ID, and a brief description of what they do:
- Ji et al. EMNLP 2025 (VUF)
- PC-LDCD (arXiv 2605.05953)
- DoLa (ICLR 2024)
- ActLCD (EMNLP 2025)
- Monitoring Decoding (ACL 2025)
- CAG (arXiv 2605.01749)
- CURE (arXiv 2604.12046)
- CSS (arXiv 2604.17487)
- CLC (arXiv 2502.19110)
- obalcells probes (EMNLP 2025)
- Tao et al. logit steering (arXiv 2601.10960)
- Streaming hallucination detection (arXiv 2601.02170)

I want to know: is there any work that SPECIFICALLY combines internal uncertainty probes with logit-level intervention during generation? That's the core of the proposal I'm reviewing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "2e1bff86-d948-43a7-aa53-7bad0081f795",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T09:00:30.746Z_

```json
{
  "parentUuid": "2e1bff86-d948-43a7-aa53-7bad0081f795",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
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
  "uuid": "a25b6485-11e7-4320-8893-993b116799b1",
  "timestamp": "2026-05-16T09:00:30.746Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T09:00:33.543Z_



I'll run all 8 searches in parallel to find relevant work efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a25b6485-11e7-4320-8893-993b116799b1",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yUP1c267oyJhxr3Kga",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba63ccd4-0932-45a6-8d46-5ab46d2a8675",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETdVHufxTwRY5zggHXecCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 4 · 2026-05-16T09:00:33.697Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BP3hxKVW9dNyNgy8EHu2no`</summary>

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
  "parentUuid": "ba63ccd4-0932-45a6-8d46-5ab46d2a8675",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yUP1c267oyJhxr3Kga",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2867f806-f74c-457d-bcf8-d97b94300f55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETdVHufxTwRY5zggHXecCL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8223,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 1115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1115,
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

_source line 5 · 2026-05-16T09:00:33.700Z_

<details><summary>↩ Tool result · `toolu_01BP3hxKVW9dNyNgy8EHu2no`</summary>

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
  "parentUuid": "2867f806-f74c-457d-bcf8-d97b94300f55",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "922988ea-1bff-48da-9a68-b88c6901804c",
  "sourceToolAssistantUUID": "2867f806-f74c-457d-bcf8-d97b94300f55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T09:00:35.980Z_



Now let me run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "922988ea-1bff-48da-9a68-b88c6901804c",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yUc1SmTcy4f1Yy5A6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa15b56f-0e60-4f0a-a8ca-91e3bd661960",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZz9neqXnf8HhzQhj3xDfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 9338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1410,
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

_source line 7 · 2026-05-16T09:00:36.431Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M3y3LPD675D1qKQJvcmtVj`</summary>

```json
{
  "query": "hallucination detection internal representations logit intervention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa15b56f-0e60-4f0a-a8ca-91e3bd661960",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yUc1SmTcy4f1Yy5A6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f64b4e06-1b26-401a-a2a3-4d69cdb4c6fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZz9neqXnf8HhzQhj3xDfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 9338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1410,
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

_source line 8 · 2026-05-16T09:00:36.934Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SxL2DvZEth5cmNhgkG5MaW`</summary>

```json
{
  "query": "calibration-aware decoding LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f64b4e06-1b26-401a-a2a3-4d69cdb4c6fd",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yUc1SmTcy4f1Yy5A6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53580b46-518d-4b30-92cd-757128f19237",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZz9neqXnf8HhzQhj3xDfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 9338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1410,
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

_source line 9 · 2026-05-16T09:00:36.978Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A3K17LLTyEeHtPVMTrR6WG`</summary>

```json
{
  "query": "uncertainty-guided generation language model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53580b46-518d-4b30-92cd-757128f19237",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yUc1SmTcy4f1Yy5A6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b14bcab5-585c-4cbc-a643-86bd8078af89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZz9neqXnf8HhzQhj3xDfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 9338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1410,
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

_source line 10 · 2026-05-16T09:00:37.402Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JU6r1kXHYRvsW44X8dbJWK`</summary>

```json
{
  "query": "probe-guided decoding hallucination 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b14bcab5-585c-4cbc-a643-86bd8078af89",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yUc1SmTcy4f1Yy5A6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01bd7fc4-1193-4d86-8c83-8de21b2bdbdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZz9neqXnf8HhzQhj3xDfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 9338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1410,
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

_source line 11 · 2026-05-16T09:00:37.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ULqXSmY6KdSFUFNunLmqeQ`</summary>

```json
{
  "query": "verbal confidence mismatch hallucination 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01bd7fc4-1193-4d86-8c83-8de21b2bdbdd",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yUc1SmTcy4f1Yy5A6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a3531c9-44c2-4143-afa3-f9695f484dbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZz9neqXnf8HhzQhj3xDfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 9338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1410,
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

_source line 12 · 2026-05-16T09:00:38.343Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Xfok3Pg6qEngCVmR8isLj`</summary>

```json
{
  "query": "logit bias hallucination reduction LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a3531c9-44c2-4143-afa3-f9695f484dbb",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yUc1SmTcy4f1Yy5A6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29947639-ac9f-4dc5-9c14-5c2638f506a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZz9neqXnf8HhzQhj3xDfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 9338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1410,
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

_source line 13 · 2026-05-16T09:00:38.386Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SL7TkVUzhscVWNaA9RLQ9b`</summary>

```json
{
  "query": "site:arxiv.org contrastive decoding hallucination 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29947639-ac9f-4dc5-9c14-5c2638f506a4",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yUc1SmTcy4f1Yy5A6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c621573-3dbe-4205-b23c-76f7c37b7ce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZz9neqXnf8HhzQhj3xDfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 9338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1410,
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

_source line 14 · 2026-05-16T09:00:38.646Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012mffRnyjpXK8CofAAuzMpd`</summary>

```json
{
  "query": "training-free hallucination mitigation inference time 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c621573-3dbe-4205-b23c-76f7c37b7ce2",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yUc1SmTcy4f1Yy5A6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a6b6aa4-ddc1-4e58-a3d3-16002a4525ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZz9neqXnf8HhzQhj3xDfF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 9338,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1410
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 410,
          "cache_read_input_tokens": 9338,
          "cache_creation_input_tokens": 1410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1410,
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

_source line 15 · 2026-05-16T09:00:43.600Z_

<details><summary>↩ Tool result · `toolu_01A3K17LLTyEeHtPVMTrR6WG`</summary>

```text
Web search results for query: "uncertainty-guided generation language model 2026"

Links: [{"title":"Towards Uncertainty Quantification in Generative Model Learning","url":"https://arxiv.org/html/2511.10710v1"},{"title":"UGFF-VLM: Uncertainty-Guided and Frequency-Fused Vision-Language Model for Remote Sensing Farmland Segmentation","url":"https://www.mdpi.com/2072-4292/18/2/282"},{"title":"Enhancing Trust in Large Language Models with Uncertainty-Aware Fine-Tuning | OpenReview","url":"https://openreview.net/forum?id=dSTSl6QK5m"},{"title":"IUQ: Interrogative Uncertainty Quantification for Long-Form Large Language Model Generation","url":"https://arxiv.org/html/2604.15109"},{"title":"A Survey on Uncertainty Quantification of Large Language Models: Taxonomy, Open Research Challenges, and Future Directions | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3744238"},{"title":"Black-Box Uncertainty Quantification for Large Language Models via Ensemble-of-Ensembles for AAAI 2026 - IBM Research","url":"https://research.ibm.com/publications/black-box-uncertainty-quantification-for-large-language-models-via-ensemble-of-ensembles"},{"title":"Uncertainty quantification by large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666827025001562"},{"title":"Uncertainty Quantification for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-tutorials.3/"},{"title":"Large language model uncertainty proxies: discrimination and calibration for medical diagnosis and treatment - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11648734/"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"}]

Based on the search results, here's what I found regarding uncertainty-guided generation in language models for 2026:

## Recent Research Areas

The search revealed several active research directions in uncertainty-guided language model generation:

**Uncertainty-Aware Fine-Tuning for LLMs:**
An uncertainty-aware fine-tuning approach for LLMs has been proposed to achieve reliable and well-calibrated uncertainty quantification in open-ended and free-form natural language generation, enhancing the model's ability to provide reliable uncertainty estimates without compromising accuracy.

**Vision-Language Models with Uncertainty Guidance:**
A recent approach utilizes semantic prior knowledge from textual descriptions in vision-language models and proposes an Uncertainty-Guided and Frequency-Fused Vision-Language Model (UGFF-VLM) that combines uncertainty guidance with adaptive alignment mechanisms.

**Black-Box Uncertainty Quantification:**
A two-level ensemble framework for black-box uncertainty estimation has been introduced that operates entirely at inference time without retraining, decomposing total predictive uncertainty into aleatoric and epistemic components through stochastic decoding and semantically perturbed prompts.

**Broader Context:**
Uncertainty quantification for LLMs in text generation tasks represents a conceptual and methodological framework that provides tools for communicating the reliability of model answers.

These developments in 2026 suggest a growing focus on making language model outputs more reliable and trustworthy through uncertainty-guided approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b14bcab5-585c-4cbc-a643-86bd8078af89",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "62490758-6465-4563-8cc5-e92d518f62c6",
  "sourceToolAssistantUUID": "b14bcab5-585c-4cbc-a643-86bd8078af89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T09:00:44.525Z_

<details><summary>↩ Tool result · `toolu_01SxL2DvZEth5cmNhgkG5MaW`</summary>

```text
Web search results for query: "calibration-aware decoding LLM 2025 2026"

Links: [{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"Benchmarking LLM Uncertainty and Calibration with ...","url":"https://aclanthology.org/2026.eacl-long.106.pdf"},{"title":"Calibrating Translation Decoding with Quality Estimation ...","url":"https://arxiv.org/pdf/2504.19044"},{"title":"ICML Poster Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach","url":"https://icml.cc/virtual/2025/poster/46448"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=2i6Rp0gCq6"},{"title":"Mixed-Precision Quantization for Language Models: Techniques and Prospects","url":"https://arxiv.org/html/2510.16805v1"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"vLLM Blog | vLLM is a fast and easy-to-use library for LLM ...","url":"https://blog.vllm.ai/"},{"title":"Towards Efficient LLM Inference via Collective and Adaptive Speculative Decoding | Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis","url":"https://dl.acm.org/doi/10.1145/3712285.3759834"},{"title":"Calibrating Translation Decoding with Quality Estimation on LLMs","url":"https://arxiv.org/html/2504.19044v1"}]

Based on the search results, here's what I found about calibration-aware decoding for LLMs in 2025-2026:

## Key Research Areas

**Calibration-Aware Approaches in LLM Training and Decoding**

Researchers are focusing on calibration-aware metrics and reward schemes—approaches that give models credit for signaling uncertainty and treat refusal as a valid outcome. The latest research emphasizes fixing incentives first with calibration-aware rewards and uncertainty-friendly evaluation metrics.

**Training and Inference Improvements**

OpenAI's September 2025 paper shows that next-token training objectives and common leaderboards reward confident guessing over calibrated uncertainty, so models learn to bluff. Rewarding Doubt (2025) integrates confidence calibration into reinforcement learning, penalizing both over- and underconfidence so model certainty better matches correctness. Uncertainty-aware RLHF variants likewise score a cautious, evidence-backed answer higher than a verbose but unsupported one.

**Calibration-Aware Fine-Tuning**

During preference alignment—when a model is trained to generate human-preferred answers—it can lose its ability to judge uncertainty accurately. A new method called Calibration-Aware Fine-Tuning (CFT) has been designed to address this.

**Application to Machine Translation**

In translation tasks, researchers propose optimizing calibration during training by encouraging the likelihood of translation hypotheses to align more closely with their quality. This approach yields substantial performance improvements with limited training—using only 2K instances per language.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53580b46-518d-4b30-92cd-757128f19237",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "1f2f1274-75ab-4b25-8e6e-0a57c8eab933",
  "sourceToolAssistantUUID": "53580b46-518d-4b30-92cd-757128f19237",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T09:00:44.916Z_

<details><summary>↩ Tool result · `toolu_015Xfok3Pg6qEngCVmR8isLj`</summary>

```text
Web search results for query: "logit bias hallucination reduction LLM"

Links: [{"title":"Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression","url":"https://arxiv.org/html/2505.16411"},{"title":"Theoretical Foundations and Mitigation of Hallucination in Large Language Models","url":"https://arxiv.org/html/2507.22915v1"},{"title":"Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/html/2510.06265v2"},{"title":"Mitigating Hallucination in Large Vision-Language Models via Adaptive Attention Calibration","url":"https://arxiv.org/html/2505.21472v2"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"LLM hallucination risks and prevention","url":"https://www.k2view.com/blog/llm-hallucination/"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"Survey and analysis of hallucinations in large language models","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12518350/"},{"title":"A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models","url":"https://arxiv.org/html/2401.01313v1"},{"title":"How to Measure and Prevent LLM Hallucinations","url":"https://www.promptfoo.dev/docs/guides/prevent-llm-hallucations/"}]

Based on the search results, here's what I found about logit bias and hallucination reduction in LLMs:

## Logit-Based Approaches to Hallucination Reduction

### Logit Manipulation Techniques

Logit penalties or masks can be applied to prevent unsupported tokens from being generated unless certain conditions are met, which is one strategy for addressing hallucinations.

### Detecting Hallucinations via Logit Analysis

Token probability scores derived from LLM's logit outputs can be used to measure uncertainty, enabling hallucination detection. One approach uses logit output values from models to identify possible hallucinations before moving on to creation of sentences, validate their accuracy, and then mitigate any hallucinations that are found.

### Advanced Decoding Methods

Several decoding-based techniques leverage logit information:

- DoLa (Decoding by Contrasting Layers) amplifies factual content by contrasting logit distributions from mature (later) and premature (earlier) layers, suppressing shallow patterns and emphasizing deep semantic knowledge.

- PAI refines logit scores by subtracting logits computed without image prior to eliminate the text bias in vision-language models.

- CAD (Context-Aware Decoding) forces the model to attend to provided evidence by penalizing tokens that would have been generated in the absence of context, encouraging grounding in retrieved information and reducing reliance on parametric priors.

These logit-based methods represent inference-time techniques that intervene directly in the model's output probabilities to reduce hallucinations without requiring retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29947639-ac9f-4dc5-9c14-5c2638f506a4",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "656920d0-0d92-404e-9913-3cffeefcbbdc",
  "sourceToolAssistantUUID": "29947639-ac9f-4dc5-9c14-5c2638f506a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T09:00:45.109Z_

<details><summary>↩ Tool result · `toolu_01ULqXSmY6KdSFUFNunLmqeQ`</summary>

```text
Web search results for query: "verbal confidence mismatch hallucination 2025 2026"

Links: [{"title":"Hallucination Rates in 2025 — Accuracy, Refusal, and Liability | by Markus Brinsa | Medium","url":"https://medium.com/@markus_brinsa/hallucination-rates-in-2025-accuracy-refusal-and-liability-aa0032019ca1"},{"title":"AI Hallucination Statistics 2026: 50+ Sourced Data Points - Suprmind","url":"https://suprmind.ai/hub/insights/ai-hallucination-statistics-research-report-2026/"},{"title":"AI Hallucination Rates & Benchmarks in 2026","url":"https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"},{"title":"Why language models hallucinate | OpenAI","url":"https://openai.com/index/why-language-models-hallucinate/"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"AI Hallucinations in 2026: Why AI Still Gets Things Wrong and How to Protect Yourself","url":"https://renovateqr.com/blog/ai-hallucinations"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v2"},{"title":"Frontiers | Survey and analysis of hallucinations in large language models: attribution to prompting strategies or model behavior","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1622292/full"}]

Based on the search results, here's what recent research (2025-2026) reveals about verbal confidence mismatch and hallucination in AI models:

## Key Finding: The Confidence Paradox

MIT research from January 2025 found that when AI models hallucinate, they tend to use more confident language than when providing factual information—models were 34% more likely to use phrases like "definitely," "certainly," and "without doubt" when generating incorrect information.

## Verbal vs. Semantic Uncertainty Mismatch

Recent research identifies a specific mechanism underlying this problem. Research found that "verbal uncertainty" is governed by a single linear feature in the representation space of LLMs, and this has only moderate correlation with the actual "semantic uncertainty" of the model. 

The mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone, and interventions on verbal uncertainty at inference time can reduce hallucinations on short-form answers, achieving an average relative reduction of 32%.

## Systemic Root Causes

The underlying issue is structural. A major driver of hallucinations is evaluation design that punishes uncertainty; if scoring penalizes confident errors more heavily and rewards appropriate uncertainty, it pushes models toward safer behavior.

OpenAI's September 2025 paper shows that next-token training objectives and common leaderboards reward confident guessing over calibrated uncertainty, so models learn to bluff.

This verbal confidence mismatch represents a critical safety issue, as confident-sounding hallucinations are particularly dangerous in high-stakes domains like medicine and law.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a3531c9-44c2-4143-afa3-f9695f484dbb",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "743f6129-dbf5-47e3-a7f7-d50fb91d380f",
  "sourceToolAssistantUUID": "3a3531c9-44c2-4143-afa3-f9695f484dbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T09:00:45.382Z_

<details><summary>↩ Tool result · `toolu_012mffRnyjpXK8CofAAuzMpd`</summary>

```text
Web search results for query: "training-free hallucination mitigation inference time 2026"

Links: [{"title":"[2604.03556] Focus Matters: Phase-Aware Suppression for Hallucination in Vision-Language Models","url":"https://arxiv.org/abs/2604.03556"},{"title":"Mitigating Multimodal LLMs Hallucinations via Relevance Propagation at Inference Time","url":"https://arxiv.org/html/2605.01766"},{"title":"Hallucination Mitigation Techniques","url":"https://www.emergentmind.com/topics/hallucination-mitigation-techniques"},{"title":"Focus Matters: Phase-Aware Suppression for Hallucination in Vision-Language Models","url":"https://arxiv.org/html/2604.03556"},{"title":"A hallucination detection and mitigation framework for faithful text summarization using LLMs | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-31075-1"},{"title":"hallucination-mitigation · GitHub Topics · GitHub","url":"https://github.com/topics/hallucination-mitigation"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"GitHub - showlab/Awesome-MLLM-Hallucination: 📖 A curated list of resources dedicated to hallucination of multimodal large language models (MLLM).","url":"https://github.com/showlab/awesome-mllm-hallucination"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v2/download"}]

Based on the search results, here's what I found about training-free hallucination mitigation at inference time in 2026:

## Key Approaches

Learning Inference-time Modality Enhancement (LIME) is a training-free framework designed to bolster multimodal grounding by explicitly enhancing modality usage during decoding. This objective is enforced through inference-time updates to the model's key-value representations, without modifying model parameters or requiring additional training data.

One approach proposes a lightweight inference-time intervention that selectively suppresses tokens during the focus phase, operating in a training-free manner using statistics from a single forward pass and employing a Determinantal Point Process (DPP) to preserve diverse visual cues while filtering redundant tokens.

## Recent Progress

Training-free mitigating solutions are getting popular, probably thanks to its resource-friendly property. Contrastive decoding becomes a cornerstone technique with various ideas developed based on it.

Recent methods achieve gains up to 20% relative reduction in CHAIR scores over state-of-the-art training-free methods.

## Broader Context

The latest research drives a new generation of mitigations by fixing incentives first with calibration-aware rewards and uncertainty-friendly evaluation metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a6b6aa4-ddc1-4e58-a3d3-16002a4525ff",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "cbd89aa9-af85-4b1f-ae03-14601aeb3cab",
  "sourceToolAssistantUUID": "9a6b6aa4-ddc1-4e58-a3d3-16002a4525ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T09:00:45.747Z_

<details><summary>↩ Tool result · `toolu_01SL7TkVUzhscVWNaA9RLQ9b`</summary>

```text
Web search results for query: "site:arxiv.org contrastive decoding hallucination 2026"

Links: [{"title":"Delve into Visual Contrastive Decoding for Hallucination Mitigation of Large Vision-Language Models","url":"https://arxiv.org/html/2412.06775v1"},{"title":"Mitigating Hallucinations in Large Vision-Language Models with Internal Fact-based Contrastive Decoding","url":"https://arxiv.org/html/2502.01056v1"},{"title":"[2602.11737v1] Mask What Matters: Mitigating Object Hallucinations in Multimodal Large Language Models with Object-Aligned Visual Contrastive Decoding","url":"https://arxiv.org/abs/2602.11737v1"},{"title":"[2602.11737] Mask What Matters: Mitigating Object Hallucinations in Multimodal Large Language Models with Object-Aligned Visual Contrastive Decoding","url":"https://arxiv.org/abs/2602.11737"},{"title":"[2601.03500] SDCD: Structure-Disrupted Contrastive Decoding for Mitigating Hallucinations in Large Vision-Language Models","url":"https://arxiv.org/abs/2601.03500"},{"title":"[2509.25177] Mitigating Hallucination in Multimodal LLMs with Layer Contrastive Decoding","url":"https://arxiv.org/abs/2509.25177"},{"title":"[2412.06775] Delve into Visual Contrastive Decoding for Hallucination Mitigation of Large Vision-Language Models","url":"https://arxiv.org/abs/2412.06775"},{"title":"Mitigating Hallucination in Multimodal LLMs with Layer Contrastive Decoding","url":"https://www.arxiv.org/pdf/2509.25177"},{"title":"[2403.18715] Mitigating Hallucinations in Large Vision-Language Models with Instruction Contrastive Decoding","url":"https://arxiv.org/abs/2403.18715"},{"title":"Do We Really Need External Tools to Mitigate Hallucinations? Sira: Shared-Prefix Internal Reconstruction of Attribution","url":"https://arxiv.org/html/2605.14621"}]

I found several recent papers on arXiv about contrastive decoding and hallucination mitigation in vision-language models from 2026 and late 2025. Here are the key results:

## Recent Papers (2026)

**"Mask What Matters"** - This paper studies object hallucination in Multimodal Large Language Models (MLLMs) and improves visual contrastive decoding (VCD) by constructing an object-aligned auxiliary view. The method removes the most salient visual evidence to construct an auxiliary view that disrupts unsupported tokens and produces a stronger contrast signal. (Published February 12, 2026)

**"SDCD: Structure-Disrupted Contrastive Decoding"** - This introduces a training-free algorithm that performs contrastive calibration of the output distribution by introducing a shuffled structure-disrupted view. (Published January 7, 2026)

**"Internal Fact-based Contrastive Decoding (IFCD)"** - A novel model-agnostic approach that leverages hallucinations to mitigate further hallucination. (Published February 3, 2025)

## Older Papers

Recent approaches apply contrastive decoding to calibrate the model's response via contrasting output distributions with original and visually distorted samples, demonstrating promising hallucination mitigation in a training-free manner. (December 2024)

These papers demonstrate an active research area focused on using contrastive decoding techniques to address hallucination problems in vision-language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c621573-3dbe-4205-b23c-76f7c37b7ce2",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "5cb1847d-ebe4-4ffd-9c36-69c3427d09e4",
  "sourceToolAssistantUUID": "0c621573-3dbe-4205-b23c-76f7c37b7ce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T09:00:45.898Z_

<details><summary>↩ Tool result · `toolu_01JU6r1kXHYRvsW44X8dbJWK`</summary>

```text
Web search results for query: "probe-guided decoding hallucination 2025 2026"

Links: [{"title":"HALP: Detecting Hallucinations in Vision-Language ...","url":"https://aclanthology.org/2026.eacl-long.287.pdf"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models","url":"https://arxiv.org/html/2604.06165v2"},{"title":"Mitigating Hallucinations in Large Vision-Language Models via Dual Contrastive Decoding | Proceedings of the 7th ACM International Conference on Multimedia in Asia","url":"https://dl.acm.org/doi/10.1145/3743093.3770933"},{"title":"🚨 AI Hallucinations Are Getting Smarter — Here’s How to Catch Them in Real-Time (Even in Agentic AI Systems, 2026) | by Yash Mishra | Feb, 2026 | Medium","url":"https://medium.com/@yash.mishra0501/ai-hallucinations-are-getting-smarter-heres-how-to-catch-them-in-real-time-even-in-agentic-3d75a9fc1ab3"},{"title":"A hallucination detection and mitigation framework for faithful text summarization using LLMs | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-31075-1"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"}]

Based on the web search results, I found relevant information about probe-guided decoding and hallucination research from 2025-2026. Here's what the current research shows:

## Probe-Based Hallucination Detection

Recent studies show that linear and MLP-based probes can predict hallucinations using hidden states before or during generation, often achieving strong AUC scores across various tasks. This represents a shift toward using internal model representations to detect hallucinations proactively.

One approach involves training a linear probe (or LoRA-enhanced head) on hidden activations at a late transformer layer to predict the hallucination label for each token in real time.

## Decoding-Time Interventions

Research into decoding-guided approaches includes various methods to reduce hallucinations during generation. Some methods aim to reduce hallucinations during generation through decoding-time interventions such as HALC, Uncertainty-Guided Dropout Decoding, and perception-driven grounding augmentation.

However, these techniques still depend on autoregressive decoding and cannot estimate hallucination risk before generation begins, revealing a critical gap where few existing methods exploit internal model representations to anticipate hallucinations preemptively and enable real-time risk detection prior to decoding.

## Recent Frameworks

HALP (Hallucination Prediction via Pre-Generation Probing) is a lightweight framework that predicts hallucination risk from pre-generative internal states of vision-language models.

The research direction for 2025-2026 emphasizes proactive detection using internal probes and moving toward calibrated uncertainty: systems that transparently signal doubt and can safely refuse to answer when unsure, rather than chasing an unrealistic "zero error" goal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01bd7fc4-1193-4d86-8c83-8de21b2bdbdd",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "6ee77f66-f38a-47da-a166-6afae2b6aefc",
  "sourceToolAssistantUUID": "01bd7fc4-1193-4d86-8c83-8de21b2bdbdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T09:00:46.149Z_

<details><summary>↩ Tool result · `toolu_01M3y3LPD675D1qKQJvcmtVj`</summary>

```text
Web search results for query: "hallucination detection internal representations logit intervention 2025 2026"

Links: [{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"Token-Level Hallucination Detection","url":"https://www.emergentmind.com/topics/token-level-hallucination-detection"},{"title":"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/html/2605.05025"},{"title":"Interpreting and Editing Vision-Language Representations to ...","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-45.pdf"},{"title":"Review Not peer-reviewed version A Survey on Hallucination in Large","url":"https://www.preprints.org/manuscript/202510.0540/v1/download"},{"title":"(PDF) A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation","url":"https://www.researchgate.net/publication/396593833_A_Survey_on_Hallucination_in_Large_Language_Models_Definitions_Detection_and_Mitigation"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Internal Representations as Indicators of Hallucinations in Agent Tool Selection | OpenReview","url":"https://openreview.net/forum?id=QbuBZvwcDZ"},{"title":"A Head to Predict and a Head to Question: Pre-trained Uncertainty Quantification Heads for Hallucination Detection in LLM Outputs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1809/"},{"title":"From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs","url":"https://www.mdpi.com/2673-2688/6/10/260"}]

I've found comprehensive research on hallucination detection using internal representations and logit intervention methods from 2025-2026. Here are the key findings:

## Hallucination Detection via Internal Representations and Logit Intervention

### Detection Methods Using Internal Representations

Recent approaches detect hallucinations directly on logits without requiring fine-tuning, and use hidden-state probes attached to internal representations to predict hallucination probability per token. Nonlinear MLP probes provide superior accuracy and recall in low false-positive-rate regimes due to better modeling of semantic nonlinearities.

### Token-Level Detection Approaches

Neural probes are attached to internal representations to predict hallucination probability per token, with nonlinear MLP probes showing superior performance when modeling semantic nonlinearities. ACT-ViT (Activation Tensor Vision Transformer) processes full activation tensors as "images" using a ViT-derived architecture, surpassing classic layer-token probes in ROC-AUC and supporting cross-model portability.

### Logit-Based Intervention Strategies

DoLa (Decoding by Contrasting Layers) amplifies factual content by contrasting logit distributions from mature (later) and premature (earlier) layers, suppressing shallow patterns and emphasizing deep semantic knowledge. These techniques intervene directly in the model's output probabilities or internal representations, typically requiring logit or layer-level access, with a class of inference-time methods involving direct intervention in the model's internal activations.

### Recent Advances (2025-2026)

A recent approach proposes computing Kullback–Leibler divergence between each attention head's distribution and a uniform reference distribution representing maximum uncertainty. Using the logit lens on image features can detect hallucinations in vision-language models, improving mAP by 22.45% and 47.17% in two models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f64b4e06-1b26-401a-a2a3-4d69cdb4c6fd",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "968ca4f9-5bcc-46cd-884b-49e29462198a",
  "sourceToolAssistantUUID": "f64b4e06-1b26-401a-a2a3-4d69cdb4c6fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T09:00:49.400Z_

Let me run a few more targeted searches to find specific papers that might be closer to the core proposal idea (combining internal uncertainty probes with logit-level intervention).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "968ca4f9-5bcc-46cd-884b-49e29462198a",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yVWrffKyyjFijusB4b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7295aa7d-4c59-4e66-aa54-c64584c951c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNt9EaEFbSaSRr6mKm3i3u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6476,
      "cache_creation_input_tokens": 1553,
      "cache_read_input_tokens": 10748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1553,
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

_source line 24 · 2026-05-16T09:00:50.568Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MuVU5mg7cAqxfozDJ6ViZw`</summary>

```json
{
  "query": "arxiv \"verbal uncertainty\" \"linear feature\" hallucination intervention logit 2503.14477"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7295aa7d-4c59-4e66-aa54-c64584c951c1",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yVWrffKyyjFijusB4b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "842925cd-9bbe-4fe0-bdd3-f965947efddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNt9EaEFbSaSRr6mKm3i3u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6476,
      "cache_creation_input_tokens": 1553,
      "cache_read_input_tokens": 10748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1553,
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

_source line 25 · 2026-05-16T09:00:51.241Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L8TmXQXBpb2S2FRdPcoiDa`</summary>

```json
{
  "query": "arxiv HALP pre-generation probing hallucination vision language 2601.18753"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "842925cd-9bbe-4fe0-bdd3-f965947efddf",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yVWrffKyyjFijusB4b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b93a4e30-c344-4c85-8c34-cf2513dcf33e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNt9EaEFbSaSRr6mKm3i3u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6476,
      "cache_creation_input_tokens": 1553,
      "cache_read_input_tokens": 10748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1553,
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

_source line 26 · 2026-05-16T09:00:51.909Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018fBb46JWZh8BnNMhZbq1mr`</summary>

```json
{
  "query": "arxiv \"internal representations\" \"decoding\" \"probe\" hallucination reduction token-level 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b93a4e30-c344-4c85-8c34-cf2513dcf33e",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yVWrffKyyjFijusB4b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9cfe36cd-d4fb-4f16-91f7-f40c319a6060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNt9EaEFbSaSRr6mKm3i3u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6476,
      "cache_creation_input_tokens": 1553,
      "cache_read_input_tokens": 10748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1553,
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

_source line 27 · 2026-05-16T09:00:52.792Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JEBe5Q3ynnoPaXEtEVWbfi`</summary>

```json
{
  "query": "arxiv \"activation steering\" hallucination truthfulness logit 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cfe36cd-d4fb-4f16-91f7-f40c319a6060",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yVWrffKyyjFijusB4b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cac74469-dc45-4c46-9db3-2ad8fd2df3e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNt9EaEFbSaSRr6mKm3i3u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6476,
      "cache_creation_input_tokens": 1553,
      "cache_read_input_tokens": 10748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1553,
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

_source line 28 · 2026-05-16T09:00:53.161Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CXi6SBhtBdKXhp94Sz152P`</summary>

```json
{
  "query": "arxiv \"inference time intervention\" \"hidden states\" hallucination factuality decoding 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cac74469-dc45-4c46-9db3-2ad8fd2df3e7",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yVWrffKyyjFijusB4b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc87233c-6578-4da6-9e4a-b9ece8eb059c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNt9EaEFbSaSRr6mKm3i3u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6476,
      "cache_creation_input_tokens": 1553,
      "cache_read_input_tokens": 10748,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1553
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6476,
          "output_tokens": 334,
          "cache_read_input_tokens": 10748,
          "cache_creation_input_tokens": 1553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1553,
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

_source line 29 · 2026-05-16T09:00:55.060Z_

<details><summary>↩ Tool result · `toolu_01MuVU5mg7cAqxfozDJ6ViZw`</summary>

```text
Web search results for query: "arxiv "verbal uncertainty" "linear feature" hallucination intervention logit 2503.14477"

Links: [{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/pdf/2503.14477"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations | alphaXiv","url":"https://www.alphaxiv.org/overview/2503.14477"},{"title":"dblp: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations.","url":"https://dblp.org/rec/journals/corr/abs-2503-14477.html"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to ...","url":"https://aclanthology.org/2025.emnlp-main.187.pdf"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"VL-Uncertainty: Detecting Hallucination in Large Vision-Language Model via Uncertainty Estimation","url":"https://arxiv.org/html/2411.11919v1"}]

I found the paper you're looking for! Here are the key details about arxiv paper 2503.14477:

**Title:** Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations

**Main Findings:**

Verbal uncertainty is governed by a single linear feature in the representation space of LLMs, and this has only moderate correlation with the actual semantic uncertainty of the model.

**Key Contributions:**

The mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone, and the researchers can intervene on verbal uncertainty at inference time and reduce confident hallucinations on short-form answers, achieving an average relative reduction of ~30%.

**Authors:** Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejik Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, Nicola Cancedda

The paper was published in the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "842925cd-9bbe-4fe0-bdd3-f965947efddf",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "57e0e81f-1215-4649-b7d5-0cd602df4670",
  "sourceToolAssistantUUID": "842925cd-9bbe-4fe0-bdd3-f965947efddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T09:00:57.861Z_

<details><summary>↩ Tool result · `toolu_01L8TmXQXBpb2S2FRdPcoiDa`</summary>

```text
Web search results for query: "arxiv HALP pre-generation probing hallucination vision language 2601.18753"

Links: [{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"HALP: Catching Hallucinations Before They Happen / HALP:在幻觉发生之前就将其捕获 | Alan Hou","url":"https://alanhou.org/blog/arxiv-halp-detecting-hallucinations-in-vision-language/"},{"title":"[2603.05465] HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/abs/2603.05465"},{"title":"HALP: Detecting Hallucinations in Vision-Language ...","url":"https://aclanthology.org/2026.eacl-long.287.pdf"},{"title":"AutoHallusion: Automatic Generation of Hallucination Benchmarks for Vision-Language Models","url":"https://arxiv.org/html/2406.10900v1"},{"title":"Visual hallucination detection in large vision-language models via evidential conflict1footnote 11footnote 1This paper is a revised and extended version of a paper [55] presented at BELIEF 2024.","url":"https://arxiv.org/html/2506.19513v1"},{"title":"HalluGuard: Demystifying Data-Driven and Reasoning-Driven Hallucinations in LLMs","url":"https://arxiv.org/html/2601.18753"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.287/"},{"title":"[2601.05201] Mechanisms of Prompt-Induced Hallucination in Vision-Language Models","url":"https://arxiv.org/abs/2601.05201"},{"title":"Who Brings the Frisbee: Probing Hidden Hallucination Factors in Large Vision-Language Model via Causality Analysis","url":"https://arxiv.org/html/2412.02946v1"}]

Based on the search results, I found information about the arXiv papers related to your query:

## HALP: Pre-Generation Probing

HALP (HALlucination Prediction via Pre-Generation Probing) is a lightweight framework that predicts hallucination risk from pre-generative internal states of vision–language models. The approach investigates whether hallucination risk can be predicted before any token is generated by probing a model's internal representations in a single forward pass.

HALP performs a single forward pass over an image–query pair and extracts three types of representations: (1) pooled visual features from the vision encoder, (2) decoder states at the last vision tokens across multiple layers, and (3) decoder states at the final text query token at corresponding depths.

### Key Results

Probes trained on these representations achieve strong hallucination-detection performance without decoding, reaching up to 0.93 AUROC on Gemma-3-12B, Phi-4-VL 5.6B, and Molmo 7B. The research examines eight modern VLMs, including Llama-3.2-Vision, Gemma-3, Phi-4-VL, and Qwen2.5-VL.

## HalluGuard: arXiv 2601.18753

However, I should note that the arXiv ID 2601.18753 you mentioned in your query actually refers to a different paper: HalluGuard, which addresses hallucinations in Large Language Models in high-stakes domains such as healthcare, law, and scientific discovery, stemming from two sources: data-driven hallucinations and reasoning-driven hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b93a4e30-c344-4c85-8c34-cf2513dcf33e",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "111d4aea-b912-47df-b815-f2e899db5fac",
  "sourceToolAssistantUUID": "b93a4e30-c344-4c85-8c34-cf2513dcf33e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T09:00:59.686Z_

<details><summary>↩ Tool result · `toolu_018fBb46JWZh8BnNMhZbq1mr`</summary>

```text
Web search results for query: "arxiv "internal representations" "decoding" "probe" hallucination reduction token-level 2025 2026"

Links: [{"title":"Towards Token-Level Hallucination Control via Self- ...","url":"https://www.arxiv.org/pdf/2601.21969"},{"title":"Neural Probe–Based Hallucination Detection for Large Language Models","url":"https://arxiv.org/html/2512.20949v1"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"Mitigating Hallucinations in Large Vision-Language Models with Internal Fact-based Contrastive Decoding","url":"https://arxiv.org/html/2502.01056v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://arxiv.org/html/2504.07863v2"},{"title":"[2504.07863] Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://arxiv.org/abs/2504.07863"},{"title":"GRAD: Graph-Retrieved Adaptive Decoding for Hallucination Mitigation","url":"https://arxiv.org/html/2511.03900v1"},{"title":"[2603.05465] HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/abs/2603.05465"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"}]

I found several highly relevant arxiv papers on this topic. Here's a summary of the search results:

## Key Papers Found

**1. Token-Level Hallucination Control via Self-Checking (2601.21969)**
Token-level self-checking reduces expected hallucination of generated sequences. This paper addresses hallucination reduction through token-level interventions.

**2. Neural Probe-Based Hallucination Detection (2512.20949)**
Probe-based methods operate internally by training lightweight classifiers on intermediate hidden states. Traditional linear probes capture only shallow local patterns and miss the nonlinear semantics encoded in deep hidden states.

**3. HALP: Detecting Hallucinations in Vision-Language Models (2603.05465 - March 2026)**
Few existing methods exploit internal model representations to anticipate hallucinations preemptively and enable real-time risk detection prior to decoding. The work investigates whether hallucination risk can instead be predicted before any token is generated by probing a model's internal representations in a single forward pass.

**4. IFCD: Internal Fact-based Contrastive Decoding (2502.01056 - Feb 2025)**
IFCD first edits the internal representation of the LVLMs to construct counterfactual logits for comparison by deliberately injecting hallucinations into the model trained by contrastive learning.

**5. HaMI: Robust Hallucination Detection via Adaptive Token Selection (2504.07863 - June 2025)**
HaMI enables robust detection of hallucinations through adaptive selection and learning of critical tokens that are most indicative of hallucinations. This is achieved through formulation of the Hallucination detection task as Multiple Instance learning over token-level representations within a sequence.

These papers collectively address the intersection of internal representations, decoding strategies, probes, and token-level hallucination reduction from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cfe36cd-d4fb-4f16-91f7-f40c319a6060",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "bd84212d-a10e-470c-b78e-d3fede02dbef",
  "sourceToolAssistantUUID": "9cfe36cd-d4fb-4f16-91f7-f40c319a6060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T09:01:01.628Z_

<details><summary>↩ Tool result · `toolu_01JEBe5Q3ynnoPaXEtEVWbfi`</summary>

```text
Web search results for query: "arxiv "activation steering" hallucination truthfulness logit 2025 2026"

Links: [{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/html/2602.21704v1"},{"title":"Steered LLM Activations are Non-Surjective","url":"https://arxiv.org/html/2604.09839v1"},{"title":"Decoupling Entropy from Hallucination in Quantized LLMs ...","url":"https://arxiv.org/pdf/2602.17691"},{"title":"Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering","url":"https://arxiv.org/html/2602.17691v1"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/html/2602.08169v1"},{"title":"Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments","url":"https://arxiv.org/html/2605.03971v1"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories","url":"https://arxiv.org/html/2406.00034v2"},{"title":"[2502.03628] The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models via Visual Information Steering","url":"https://arxiv.org/abs/2502.03628"},{"title":"[2406.00034] Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories","url":"https://arxiv.org/abs/2406.00034"}]

I found several highly relevant recent papers on arXiv about activation steering, hallucination, truthfulness, and logits. Here are the key papers from 2025-2026:

## Recent Papers on Activation Steering for Hallucination & Truthfulness

**1. Dynamic Multimodal Activation Steering (DMAS) - February 2026**

A training-free approach for hallucination mitigation in Large Vision-Language Models that focuses on two types of attention heads: truthfulness-related and visual perception-related. The method extracts truthfulness steering vectors by contrasting attention activations between factual and hallucination-prone samples.

**2. Tethered Reasoning / Helix - February 2026**

This paper introduces a geometric framework that decouples output entropy from hallucination by tethering hidden-state trajectories to a pre-computed truthfulness manifold, and uses graduated steering vectors to redirect activations when trajectory divergence is detected. Steering intervention adds logit modification only for 0.2–2.5% of tokens below threshold.

**3. Spherical Steering - February 2026**

Brings geometry-consistent control to activation steering by extracting a contrastive truthfulness signal from positive/negative examples to define a truthfulness axis in representation space.

**4. Adaptive Activation Steering (ACT) - February 2025**

Treats truthfulness as a linearly encoded concept within LLMs and is a tuning-free method that adaptively shifts LLM activations in the "truthful" direction during inference, addressing diverse hallucination categories.

**5. Visual Information Steering (VISTA) - February 2025**

Investigates internal dynamics of hallucination by examining token logits ranking throughout generation, and proposes a training-free inference-time intervention framework that reduces hallucination.

**6. Steered LLM Activations are Non-Surjective - April 2026**

A comprehensive overview of activation steering research, noting that steering can reliably modify model behavior by adding directions to internal representations, commonly the residual stream.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cac74469-dc45-4c46-9db3-2ad8fd2df3e7",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "c057c578-18d1-44e0-83fc-4badf5ce24fb",
  "sourceToolAssistantUUID": "cac74469-dc45-4c46-9db3-2ad8fd2df3e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T09:01:02.444Z_

<details><summary>↩ Tool result · `toolu_01CXi6SBhtBdKXhp94Sz152P`</summary>

```text
Web search results for query: "arxiv "inference time intervention" "hidden states" hallucination factuality decoding 2025 2026"

Links: [{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"FactCheckmate: Preemptively Detecting and Mitigating Hallucinations in LMs","url":"https://arxiv.org/html/2410.02899"},{"title":"Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments","url":"https://arxiv.org/html/2605.03971v1"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"arXiv:2410.02899v2 [cs.CL] 24 Jun 2025","url":"https://arxiv.org/pdf/2410.02899"},{"title":"HALT: Hallucination Assessment via Latent Testing","url":"https://arxiv.org/html/2601.14210v1"},{"title":"Causal Decoding for Hallucination-Resistant Multimodal Large Language Models","url":"https://arxiv.org/html/2602.21441"},{"title":"LayerCake: Token-Aware Contrastive Decoding within Large Language Model Layers","url":"https://arxiv.org/html/2507.04404v1"}]

I found several highly relevant arXiv papers from 2025-2026 on inference-time interventions, hidden states, hallucination detection, and factuality in language models. Here are the key findings:

## Recent Papers on Inference-Time Intervention and Hidden States

**1. Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (2025)**

This work integrates PCNet into the LLM inference pipeline to detect hallucinations by executing a standard forward pass and isolating the final-layer hidden state corresponding to the last valid token. The approach computes the NLL (negative log-likelihood) of the current state as an uncertainty metric by exploiting the circuit's guarantee of exact marginal inference.

**2. FactCheckmate: Preemptively Detecting and Mitigating Hallucinations in LMs (2025)**

FactCheckmate preemptively detects hallucinations by learning a classifier that predicts whether the LM will hallucinate based on the model's hidden states produced over the inputs, and if hallucination is detected, it intervenes by adjusting the LM's hidden states. Using the LMs' hidden states over the input questions, FactCheckmate can successfully predict whether or not the LMs will hallucinate over 70% of the time.

**3. HALT: Hallucination Assessment via Latent Testing (2026)**

This paper proposes lightweight residual probes that read hallucination risk directly from intermediate hidden states of question tokens. Early layers capture surface-level features while deeper layers encode higher-level semantics, and intermediate-to-late layers, which are believed to encode higher-level semantic and factual information, provide the strongest signals for detecting hallucinations.

**4. Causal Decoding for Hallucination-Resistant Multimodal Large Language Models (2026)**

Recent approaches include intervention-based decoding strategies that penalize overconfident token predictions associated with hallucinated content, and methods that improve factual alignment by comparing generation logits from early and late transformer layers.

These papers demonstrate an active research direction focusing on detecting and mitigating hallucinations through hidden state analysis and inference-time interventions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc87233c-6578-4da6-9e4a-b9ece8eb059c",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "e4161bad-bc57-474c-8391-b6dcf3d3edad",
  "sourceToolAssistantUUID": "dc87233c-6578-4da6-9e4a-b9ece8eb059c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-16T09:01:05.896Z_

Let me do a few more targeted searches to find the most directly relevant work -- specifically papers that close the loop from probe detection to logit intervention.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4161bad-bc57-474c-8391-b6dcf3d3edad",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yWiWvNSyG41MWFGiXk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f830a959-abad-425b-b5cb-feb650a6817c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCXRgPuiy4R7ikH6SoCKgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11576,
      "cache_read_input_tokens": 12301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11576,
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

_source line 35 · 2026-05-16T09:01:06.367Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SJy8KjFK4rpsKHTmQTJjwC`</summary>

```json
{
  "query": "FactCheckmate arxiv 2410.02899 hidden state intervention hallucination preemptive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f830a959-abad-425b-b5cb-feb650a6817c",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yWiWvNSyG41MWFGiXk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9441e97-2e2a-4525-87db-8b1708618155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCXRgPuiy4R7ikH6SoCKgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11576,
      "cache_read_input_tokens": 12301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11576,
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

_source line 36 · 2026-05-16T09:01:06.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PE2wdRrXUauhDhA8Wzmw3V`</summary>

```json
{
  "query": "arxiv 2601.21969 \"token-level hallucination control\" self-checking decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9441e97-2e2a-4525-87db-8b1708618155",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yWiWvNSyG41MWFGiXk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52cd0700-296f-4c7e-843a-15ed17612713",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCXRgPuiy4R7ikH6SoCKgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11576,
      "cache_read_input_tokens": 12301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11576,
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

_source line 37 · 2026-05-16T09:01:07.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01USHviV1TpdV7UpsRjqKygv`</summary>

```json
{
  "query": "\"Tethered Reasoning\" arxiv 2602.17691 \"manifold steering\" hallucination logit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52cd0700-296f-4c7e-843a-15ed17612713",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yWiWvNSyG41MWFGiXk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37418c42-0c48-4d2d-9bcb-dd3f23cf641f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCXRgPuiy4R7ikH6SoCKgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11576,
      "cache_read_input_tokens": 12301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11576,
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

_source line 38 · 2026-05-16T09:01:08.370Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YTNnnnUK1QzKauzbg14giK`</summary>

```json
{
  "query": "arxiv \"HALT\" \"hallucination assessment latent testing\" 2601.14210 probe residual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37418c42-0c48-4d2d-9bcb-dd3f23cf641f",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yWiWvNSyG41MWFGiXk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db4d930e-2c74-4ed3-bab1-492710902e07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCXRgPuiy4R7ikH6SoCKgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11576,
      "cache_read_input_tokens": 12301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11576,
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

_source line 39 · 2026-05-16T09:01:08.880Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EKUSZ9E7uKE6eCcnkDyX7a`</summary>

```json
{
  "query": "arxiv \"Adaptive Activation Steering\" 2406.00034 truthfulness hallucination intervention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db4d930e-2c74-4ed3-bab1-492710902e07",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yWiWvNSyG41MWFGiXk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b8bb485-59f7-4e22-944f-89db1b4c5f4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCXRgPuiy4R7ikH6SoCKgS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11576,
      "cache_read_input_tokens": 12301,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11576
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 12301,
          "cache_creation_input_tokens": 11576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11576,
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

_source line 40 · 2026-05-16T09:01:13.441Z_

<details><summary>↩ Tool result · `toolu_01SJy8KjFK4rpsKHTmQTJjwC`</summary>

```text
Web search results for query: "FactCheckmate arxiv 2410.02899 hidden state intervention hallucination preemptive"

Links: [{"title":"[2410.02899] FactCheckmate: Preemptively Detecting and Mitigating Hallucinations in LMs","url":"https://arxiv.org/abs/2410.02899"},{"title":"arXiv:2410.02899v2 [cs.CL] 24 Jun 2025","url":"https://arxiv.org/pdf/2410.02899"},{"title":"FactCheckmate: Preemptively Detecting and Mitigating Hallucinations in LMs","url":"https://arxiv.org/html/2410.02899v2"},{"title":"[Literature Review] FactCheckmate: Preemptively Detecting and Mitigating Hallucinations in LMs","url":"https://www.themoonlight.io/en/review/factcheckmate-preemptively-detecting-and-mitigating-hallucinations-in-lms"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Distinguishing Ignorance from Error in LLM Hallucinations","url":"https://arxiv.org/html/2410.22071v2"},{"title":"Mitigating Hallucination via Evaluating the Factuality of ...","url":"https://aclanthology.org/2025.findings-acl.752.pdf"},{"title":"HALT: Hallucination Assessment via Latent Testing","url":"https://arxiv.org/html/2601.14210v1"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/html/2507.16488"}]

Based on the search results, here's what I found about FactCheckmate (arxiv 2410.02899):

## Overview

FactCheckmate preemptively detects hallucinations by learning a classifier that predicts whether the LM will hallucinate, based on the model's hidden states produced over the inputs, before decoding begins.

## How It Works

The system operates in two key stages:

1. **Detection**: FactCheckmate learns a classifier that, taking the models' hidden states over the inputs, predicts whether the model is about to hallucinate.

2. **Hidden State Intervention**: If a hallucination is detected, FactCheckmate then intervenes by adjusting the LM's hidden states such that the model will produce more factual outputs.

## Key Insights and Performance

FactCheckmate provides fresh insights that the inner workings of LMs can be revealed by their hidden states. The results demonstrate the effectiveness of FactCheckmate, achieving over 70% preemptive detection accuracy. On average, outputs generated by LMs with intervention are 34.4% more factual compared to those without.

## Efficiency

Both its detection and mitigation models are lightweight, adding little inference overhead; FactCheckmate proves a more efficient approach for mitigating hallucinations compared to many post-hoc alternatives.

The paper was evaluated across multiple language models and datasets including Llama, Mistral, Qwen, and Gemma.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9441e97-2e2a-4525-87db-8b1708618155",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "35dc7703-6aeb-4553-93c1-63b8b15ea4d0",
  "sourceToolAssistantUUID": "f9441e97-2e2a-4525-87db-8b1708618155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T09:01:15.498Z_

<details><summary>↩ Tool result · `toolu_01EKUSZ9E7uKE6eCcnkDyX7a`</summary>

```text
Web search results for query: "arxiv "Adaptive Activation Steering" 2406.00034 truthfulness hallucination intervention"

Links: [{"title":"[2406.00034] Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories","url":"https://arxiv.org/abs/2406.00034"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories","url":"https://arxiv.org/html/2406.00034v1"},{"title":"[2406.00034] Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories","url":"https://ar5iv.labs.arxiv.org/html/2406.00034"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM ...","url":"https://arxiv.org/pdf/2406.00034"},{"title":"AFTER: Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing","url":"https://arxiv.org/html/2601.01957"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/adaptive-activation-steering-tuning-free-llm-truthfulness"},{"title":"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/html/2602.21704v1"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714640"}]

I found the arXiv paper for you. Here are the key details about **Adaptive Activation Steering (ACT)**, paper 2406.00034:

## Overview

ACT is a tuning-free method that adaptively shifts LLM's activations in the "truthful" direction during inference, treating truthfulness as a linearly encoded concept within LLMs.

## Key Problem and Approach

Large Language Models harbor an inherent understanding of truthfulness, yet often fail to consistently express it and generate false statements, creating a gap between "knowing" and "telling".

## Core Methodology

ACT addresses diverse categories of hallucinations by utilizing diverse truthfulness-related steering vectors and adjusting the steering intensity adaptively. ACT generates diverse steering vectors through unsupervised clustering to enable customized interventions for various categories of hallucinations.

## Results

Applied as an add-on across various models, ACT significantly improves truthfulness in LLaMA (↑ 142%), LLaMA2 (↑ 24%), Alpaca (↑ 36%), Vicuna (↑ 28%), LLaMA2-Chat (↑ 19%), and LLaMA3 (↑ 34%).

The paper is available on arXiv at https://arxiv.org/abs/2406.00034, with the latest revision from February 26, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b8bb485-59f7-4e22-944f-89db1b4c5f4b",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "866b5fb4-e0ce-44c6-9f36-435f578b9b58",
  "sourceToolAssistantUUID": "7b8bb485-59f7-4e22-944f-89db1b4c5f4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T09:01:15.573Z_

<details><summary>↩ Tool result · `toolu_01YTNnnnUK1QzKauzbg14giK`</summary>

```text
Web search results for query: "arxiv "HALT" "hallucination assessment latent testing" 2601.14210 probe residual"

Links: [{"title":"HALT: Hallucination Assessment via Latent Testing","url":"https://arxiv.org/html/2601.14210v1"},{"title":"Halt: Residual Probes Achieve Near-Instantaneous LLM Hallucination Risk Estimation","url":"https://quantumzeitgeist.com/halt-residual-probes-near-instantaneous/"},{"title":"[2601.14210] DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness","url":"https://arxiv.org/abs/2601.14210"},{"title":"HALT: Hallucination Assessment via Log-probs as Time series","url":"https://arxiv.org/html/2602.02888v1"},{"title":"[2602.02888] HALT: Hallucination Assessment via Log-probs as Time series","url":"https://arxiv.org/abs/2602.02888"},{"title":"HALT: Hallucination Assessment via Log-probs as Time series","url":"https://www.arxiv.org/pdf/2602.02888"},{"title":"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness","url":"https://arxiv.org/html/2601.14210"},{"title":"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2601.02170"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"(PDF) HALT: Hallucination Assessment via Log-probs as Time series","url":"https://www.researchgate.net/publication/400415154_HALT_Hallucination_Assessment_via_Log-probs_as_Time_series"}]

Based on the search results, I found the paper you're looking for. The arxiv paper 2601.14210 is titled "HALT: Hallucination Assessment via Latent Testing" and proposes lightweight residual probes that read hallucination risk directly from intermediate hidden states of question tokens.

Here are the key details about this research:

**Core Approach:** The method is motivated by the hypothesis that intermediate layers retain epistemic signals that are attenuated in the final decoding stage.

**Technical Implementation:** The probe is a small auxiliary network whose computation is orders of magnitude cheaper than token generation and can be evaluated fully in parallel with inference, enabling near-instantaneous hallucination risk estimation with effectively zero added latency in low-risk cases.

**Computational Efficiency:** The probe adds less than 0.1% computational overhead and can run fully in parallel with generation, enabling hallucination detection before the answer is produced.

**Performance:** The method achieves SOTA AUROC on 10 out of 12 settings across four QA benchmarks and three LLM families, with gains of up to 13 points over prior methods, and generalizes across dataset shifts without retraining.

**Application:** The probe is deployed as an agentic critic for fast selective generation and routing, allowing LLMs to immediately answer confident queries while delegating uncertain ones to stronger verification pipelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db4d930e-2c74-4ed3-bab1-492710902e07",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "8181fcd2-18cb-4781-8319-3b2f0d3bf4de",
  "sourceToolAssistantUUID": "db4d930e-2c74-4ed3-bab1-492710902e07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-16T09:01:16.129Z_

<details><summary>↩ Tool result · `toolu_01USHviV1TpdV7UpsRjqKygv`</summary>

```text
Web search results for query: ""Tethered Reasoning" arxiv 2602.17691 "manifold steering" hallucination logit"

Links: [{"title":"Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering","url":"https://arxiv.org/html/2602.17691v1"},{"title":"[2602.17691] Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering","url":"https://arxiv.org/abs/2602.17691"},{"title":"Tethered Reasoning: Decoupling Entropy from Hallucination","url":"https://arxiv.org/pdf/2602.17691"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models via Visual Information Steering","url":"https://arxiv.org/html/2502.03628v2"},{"title":"Mitigating Overthinking in Large Reasoning Models via Manifold Steering","url":"https://arxiv.org/html/2505.22411v2"},{"title":"[2505.22411] Mitigating Overthinking in Large Reasoning Models via Manifold Steering","url":"https://arxiv.org/abs/2505.22411"},{"title":"Residual Decoding: Mitigating Hallucinations in Large Vision-Language Models via History-Aware Residual Guidance","url":"https://arxiv.org/html/2602.01047v1"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"Steering Large Reasoning Models towards Concise Reasoning via Flow Matching","url":"https://arxiv.org/html/2602.05539"},{"title":"Mitigating Overthinking in Large Reasoning Models via Manifold Steering","url":"https://openreview.net/pdf/e526209110869ec8c63cf89731300146395ff4a2.pdf"}]

I found the paper! Here are the key findings from the search results about "Tethered Reasoning" (arxiv 2602.17691):

## Overview

HELIX is a geometric framework that decouples output entropy from hallucination by tethering hidden-state trajectories to a pre-computed truthfulness manifold and computes a Unified Truth Score (UTS) combining token-level semantic entropy with Mahalanobis distance from the manifold.

## The Problem Addressed

Quantized language models face a fundamental dilemma: low sampling temperatures yield repetitive, mode-collapsed outputs, while high temperatures (T > 2.0) cause trajectory divergence and semantic incoherence.

## How It Works

When UTS indicates trajectory divergence, graduated steering vectors redirect activations toward structurally coherent regions while affecting only 0.2-2.5% of tokens. When entropy saturation flattens logits, manifold distance remains stable: tokens leading to hallucinations produce activations far from the manifold, and logit penalization redistributes probability mass when UTS indicates low confidence.

## Performance Results

On 4-bit quantized Granite 4.0 H Small (32B/9B active, hybrid Mamba-Transformer): GSM8K maintains 88.84% accuracy at T = 3.0 (2.81pp degradation from T = 0.5); MMLU maintains 72.49% across 14,042 questions (1.24pp degradation).

## Efficiency

In practice, steering activates for only 0.2–2.5% of tokens, preserving the model's natural distribution while pruning hallucination signatures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37418c42-0c48-4d2d-9bcb-dd3f23cf641f",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "d0cbe702-95a8-4cbc-9cb4-16f4899c8e22",
  "sourceToolAssistantUUID": "37418c42-0c48-4d2d-9bcb-dd3f23cf641f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T09:01:17.305Z_

<details><summary>↩ Tool result · `toolu_01PE2wdRrXUauhDhA8Wzmw3V`</summary>

```text
Web search results for query: "arxiv 2601.21969 "token-level hallucination control" self-checking decoding"

Links: [{"title":"[2601.21969] Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding","url":"https://arxiv.org/abs/2601.21969"},{"title":"Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding","url":"https://arxiv.org/html/2601.21969"},{"title":"Towards Token-Level Hallucination Control via Self- ...","url":"https://www.arxiv.org/pdf/2601.21969"},{"title":"GitHub - RongHuiQiang/Token-Guard: [ICLR 2026] Official resources of \"Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding\" · GitHub","url":"https://github.com/rhq945/Token-Guard"},{"title":"Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding | OpenReview","url":"https://openreview.net/forum?id=5fCDEz43ya"},{"title":"Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models","url":"https://arxiv.org/html/2502.06130v2"},{"title":"DHI: Leveraging Diverse Hallucination Induction for Enhanced Contrastive Factuality Control in Large Language Models","url":"https://arxiv.org/html/2601.01156v1"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models via Visual Information Steering","url":"https://arxiv.org/html/2502.03628v1"},{"title":"[2605.05166] The First Token Knows: Single-Decode Confidence for Hallucination Detection","url":"https://arxiv.org/abs/2605.05166"},{"title":"Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation","url":"https://arxiv.org/html/2503.03106v1"}]

Based on the search results, I found the paper you're looking for:

**Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding** (arXiv:2601.21969)

**Overview:**
Token-Guard is a token-level hallucination control method based on self-checking decoding that performs internal verification at each reasoning step to detect hallucinated tokens before they propagate.

**Key Features:**
Candidate fragments are further evaluated in a latent space with explicit hallucination risk scoring, while iterative pruning and regeneration dynamically correct detected errors.

**Motivation:**
Large Language Models often hallucinate, generating content inconsistent with the input. While Retrieval-Augmented Generation (RAG) and Reinforcement Learning with Human Feedback (RLHF) can mitigate hallucinations, they require resource-intensive retrieval or large-scale fine-tuning, and decoding-based methods are lighter yet lack explicit hallucination control.

**Status:**
The paper has been accepted to the International Conference on Learning Representations (ICLR) 2026, and official resources are available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52cd0700-296f-4c7e-843a-15ed17612713",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "35facecc-afe1-4bc6-b597-e8c3248f95de",
  "sourceToolAssistantUUID": "52cd0700-296f-4c7e-843a-15ed17612713",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-16T09:01:21.380Z_

Now let me do a final set of searches specifically targeting the exact combination described in the proposal -- probes detecting miscalibration that then trigger logit-level corrections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35facecc-afe1-4bc6-b597-e8c3248f95de",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yXpDzegPe6jFTUXdQU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db2b87fe-eb66-4d59-9c7c-c09f17e583ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtRdc8CQyytcSDxmojdELu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2702,
      "cache_creation_input_tokens": 2183,
      "cache_read_input_tokens": 23877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2183,
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

_source line 46 · 2026-05-16T09:01:22.276Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Uu7ZkkAhS6xXDykXCJhGB`</summary>

```json
{
  "query": "arxiv \"probe\" \"logit\" \"correction\" OR \"adjustment\" hallucination \"during generation\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db2b87fe-eb66-4d59-9c7c-c09f17e583ea",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yXpDzegPe6jFTUXdQU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2025326-055c-4159-9660-e11d3e083cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtRdc8CQyytcSDxmojdELu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2702,
      "cache_creation_input_tokens": 2183,
      "cache_read_input_tokens": 23877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2183,
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

_source line 47 · 2026-05-16T09:01:22.744Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tst7FgUXByEMFo7E6S3Pft`</summary>

```json
{
  "query": "arxiv \"miscalibration\" \"probe\" \"decoding\" hallucination confidence gap LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2025326-055c-4159-9660-e11d3e083cbc",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yXpDzegPe6jFTUXdQU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17d6e68d-556b-4c20-82d4-7605680a94ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtRdc8CQyytcSDxmojdELu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2702,
      "cache_creation_input_tokens": 2183,
      "cache_read_input_tokens": 23877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2183,
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

_source line 48 · 2026-05-16T09:01:26.355Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019coM2Fnbq3TnEivbM2eyM5`</summary>

```json
{
  "query": "arxiv \"DRIFT\" \"Detecting Representational Inconsistencies\" factual truthfulness 2601.14210"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17d6e68d-556b-4c20-82d4-7605680a94ef",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yXpDzegPe6jFTUXdQU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f057f99-429d-49d9-8f84-85236d244e22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtRdc8CQyytcSDxmojdELu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2702,
      "cache_creation_input_tokens": 2183,
      "cache_read_input_tokens": 23877,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2183
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2702,
          "output_tokens": 240,
          "cache_read_input_tokens": 23877,
          "cache_creation_input_tokens": 2183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2183,
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

_source line 49 · 2026-05-16T09:01:30.871Z_

<details><summary>↩ Tool result · `toolu_01Tst7FgUXByEMFo7E6S3Pft`</summary>

```text
Web search results for query: "arxiv "miscalibration" "probe" "decoding" hallucination confidence gap LLM 2025 2026"

Links: [{"title":"Hallucination Detection and Mitigation in Large Language Models","url":"https://arxiv.org/html/2601.09929v1"},{"title":"The Dunning-Kruger Effect in Large Language Models: An Empirical Study of Confidence Calibration","url":"https://arxiv.org/html/2603.09985v1"},{"title":"Hallucination, Monofacts, and Miscalibration: An Empirical Investigation","url":"https://arxiv.org/html/2502.08666v2"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"[2512.19920] Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning","url":"https://arxiv.org/abs/2512.19920"},{"title":"Mathematical Analysis of Hallucination Dynamics in Large Language Models: Uncertainty Quantification, Advanced Decoding, and Principled Mitigation","url":"https://arxiv.org/html/2511.15005v1"},{"title":"The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination","url":"https://arxiv.org/html/2510.22977v1"},{"title":"Neural Probe–Based Hallucination Detection for Large Language Models","url":"https://arxiv.org/html/2512.20949v1"},{"title":"How Much Do LLMs Hallucinate in Document Q&A Scenarios? A 172-Billion-Token Study Across Temperatures, Context Lengths, and Hardware Platforms","url":"https://arxiv.org/html/2603.08274v1"}]

I found several highly relevant papers from arXiv on your query. Here are the key findings:

## Recent Papers on Miscalibration and Hallucination Detection in LLMs

**Hallucination Detection and Miscalibration (2026)**
Expected Calibration Error (ECE) quantifies miscalibration—the disconnect between the model's confidence scores and its actual accuracy. LLMs produce high-confidence hallucinations where the model consistently generates the same incorrect output with high certainty.

**Confidence Calibration Studies**
Severe miscalibration in models likely stems from training dynamics that reward confident responses regardless of correctness, as models may learn to produce high confidence scores because such responses are perceived as more helpful or authoritative during training. Recent work (Park et al., 2026) proposed fine-tuning methods to improve metacognitive alignment, enabling models to more accurately report what they actually know.

**Theoretical Framework on Hallucination**
Studies prove that hallucination rate has a statistical lower bound tied to the monofact rate minus model miscalibration, where model miscalibration is the sum of bin-wise absolute difference between the model's predicted confidence scores and the corresponding probability mass under the true data distribution.

**Probe-Based Detection (December 2025)**
A neural network-based framework proposes lightweight MLP probes to perform nonlinear modeling for token-level hallucination detection. Current hallucination detection methods based on uncertainty estimation still produce erroneous content at high confidence levels.

**Decoding and Hallucination Dynamics (2025)**
Hallucinations in LLMs stem from deep probabilistic, information-theoretic, and architectural issues including miscalibration and epistemic ignorance.

These papers represent cutting-edge research on understanding and addressing the confidence-accuracy gap in LLMs from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17d6e68d-556b-4c20-82d4-7605680a94ef",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "6383879e-9f5a-4541-b2e5-9dbae141fdbd",
  "sourceToolAssistantUUID": "17d6e68d-556b-4c20-82d4-7605680a94ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T09:01:31.179Z_

<details><summary>↩ Tool result · `toolu_014Uu7ZkkAhS6xXDykXCJhGB`</summary>

```text
Web search results for query: "arxiv "probe" "logit" "correction" OR "adjustment" hallucination "during generation" 2025 2026"

Links: [{"title":"Generate, but Verify: Reducing Hallucination in Vision-Language Models with Retrospective Resampling","url":"https://arxiv.org/html/2504.13169v2"},{"title":"HALT: Hallucination Assessment via Log-probs as Time series","url":"https://arxiv.org/html/2602.02888v1"},{"title":"Hallucination Detection and Mitigation in Large Language Models","url":"https://arxiv.org/html/2601.09929v1"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language","url":"https://arxiv.org/pdf/2601.05547"},{"title":"Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation","url":"https://arxiv.org/html/2503.03106v1"},{"title":"[2503.03106] Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation","url":"https://arxiv.org/abs/2503.03106"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments","url":"https://arxiv.org/html/2605.03971v1"},{"title":"Neural Probe–Based Hallucination Detection for Large Language Models","url":"https://arxiv.org/html/2512.20949v1"}]

Based on the web search results, I found several recent arXiv papers from 2025-2026 that match your query about using probes and logit-based methods for hallucination detection and correction during generation:

## Key Papers Found:

1. **VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language** (January 2026)
   The VIB-Probe framework uses Information Bottleneck (IB) theory to detect and mitigate hallucinations by probing internal attention features, and achieves inference-time mitigation by suppressing attention heads with high risks of hallucination during token generation.

2. **HALT: Hallucination Assessment via Log-probs as Time series** (February 2026)
   This work uses token-level log-probabilities as a lightweight signal for uncertainty, noting that certain APIs for LLMs expose this metadata which represents the model's confidence at each generation step.

3. **Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation** (March 2025)
   This paper introduces Monitoring Decoding (MD), a framework that dynamically monitors the generation process and selectively applies in-process interventions, identifying hallucination-prone tokens during generation using a monitor function and refining them through tree-based decoding.

4. **Hallucination Detection and Mitigation in Large Language Models** (January 2026)
   The work discusses probing hidden layers, attention weights, and logit dynamics of models, noting that divergent attention maps or abnormally high logit variance may indicate unstable reasoning trajectories, and monitoring such internal states can reveal hallucinations before they surface in text.

5. **HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token** (March 2026)
   This paper trains probes on Transformer internal representations to predict hallucinatory behavior, finding that probes can reliably detect hallucinations at many transformer layers.

6. **Neural Probe–Based Hallucination Detection for Large Language Models** (December 2025)
   The work addresses limitations of traditional linear probes, noting they capture only shallow local patterns and miss the nonlinear semantics encoded in deep hidden states.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2025326-055c-4159-9660-e11d3e083cbc",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "e64b1859-9fce-4d77-8e85-0133b61442ca",
  "sourceToolAssistantUUID": "f2025326-055c-4159-9660-e11d3e083cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-16T09:01:33.953Z_

<details><summary>↩ Tool result · `toolu_019coM2Fnbq3TnEivbM2eyM5`</summary>

```text
Web search results for query: "arxiv "DRIFT" "Detecting Representational Inconsistencies" factual truthfulness 2601.14210"

Links: [{"title":"[2601.14210] DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness","url":"https://arxiv.org/abs/2601.14210"},{"title":"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness","url":"https://arxiv.org/html/2601.14210v2"},{"title":"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.14210v2"},{"title":"Rohan Bhatnagar's research works","url":"https://www.researchgate.net/scientific-contributions/Rohan-Bhatnagar-2307525189"},{"title":"Awesome-LM-SSP/collection/paper/safety/hallucination.md at main · CryptoAILab/Awesome-LM-SSP","url":"https://github.com/CryptoAILab/Awesome-LM-SSP/blob/main/collection/paper/safety/hallucination.md"},{"title":"Know When To Stop: A Study of Semantic Drift in Text Generation","url":"https://arxiv.org/html/2404.05411v1"},{"title":"ARREST: Adversarial Resilient Regulation Enhancing Safety and Truth in Large Language Models","url":"https://arxiv.org/html/2601.04394"},{"title":"The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection","url":"https://arxiv.org/pdf/2510.04933"},{"title":"When Truthful Representations Flip Under Deceptive Instructions?","url":"https://arxiv.org/html/2507.22149v1"},{"title":"The Geometric Canary: Predicting Steerability and Detecting Drift via Representational Stability","url":"https://arxiv.org/html/2604.17698"}]

Based on the search results, here's what I found about the paper:

## DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness

DRIFT (arXiv:2601.14210) was submitted on January 20, 2026 and last revised on January 29, 2026.

### Core Approach
The paper addresses the problem that LLMs often produce fluent but incorrect answers, yet detecting such hallucinations typically requires multiple sampling passes or post-hoc verification, adding significant latency and cost. The authors hypothesize that intermediate layers encode confidence signals that are lost in the final output layer, and propose a lightweight probe to read these signals directly from hidden states.

### Key Features
The probe adds less than 0.1% computational overhead and can run fully in parallel with generation, enabling hallucination detection before the answer is produced. Building on this, the authors develop an LLM router that answers confident queries immediately while delegating uncertain ones to stronger models.

### Performance
Despite its simplicity, the method achieves SOTA (state-of-the-art) AUROC on 10 out of 12 settings across four QA benchmarks and three LLM families, with gains of up to 13 points over prior methods, and generalizes across dataset shifts without retraining.

The paper was authored by Rohan Bhatnagar and four other collaborators.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f057f99-429d-49d9-8f84-85236d244e22",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "787b96e6-b8b1-4215-850f-d0d1117b8e90",
  "sourceToolAssistantUUID": "3f057f99-429d-49d9-8f84-85236d244e22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T09:01:36.728Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mvko9Ghqkvp2UvcH1PP3c5`</summary>

```json
{
  "query": "arxiv VIB-Probe 2601.05547 information bottleneck hallucination attention head suppression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "787b96e6-b8b1-4215-850f-d0d1117b8e90",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yZ3DNHXzhXiYAZTGxQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0584cd2d-c307-4eb8-9e70-1cad6bda785b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5E2gTPxokAiACc814yWkM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 26060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5851,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 53 · 2026-05-16T09:01:37.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017BhAfxqgd8QUiajk6oQBe3`</summary>

```json
{
  "query": "arxiv \"Dynamic Multimodal Activation Steering\" DMAS 2602.21704 hallucination truthfulness steering vector"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0584cd2d-c307-4eb8-9e70-1cad6bda785b",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yZ3DNHXzhXiYAZTGxQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aff8d34c-db54-434d-a3d6-af7bdabb9522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5E2gTPxokAiACc814yWkM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 26060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5851,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 54 · 2026-05-16T09:01:38.246Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ATeukaUiGCzGZfh5b6xdAf`</summary>

```json
{
  "query": "arxiv \"Detecting Representational Inconsistencies\" OR \"internal probe\" \"logit adjustment\" OR \"logit penalty\" hallucination generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aff8d34c-db54-434d-a3d6-af7bdabb9522",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yZ3DNHXzhXiYAZTGxQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fa6bb5a-de7b-4abf-9c17-2f091ff4d8f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5E2gTPxokAiACc814yWkM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 26060,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5851
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 26060,
          "cache_creation_input_tokens": 5851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5851,
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

_source line 55 · 2026-05-16T09:01:42.903Z_

<details><summary>↩ Tool result · `toolu_01ATeukaUiGCzGZfh5b6xdAf`</summary>

```text
Web search results for query: "arxiv "Detecting Representational Inconsistencies" OR "internal probe" "logit adjustment" OR "logit penalty" hallucination generation 2025 2026"

Links: [{"title":"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness","url":"https://arxiv.org/html/2601.14210v2"},{"title":"[2601.14210] DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness","url":"https://arxiv.org/abs/2601.14210"}]

I found a highly relevant paper for you! Here are the search results:

## DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness

The paper addresses the problem of LLMs producing fluent but incorrect answers by proposing a lightweight probe that reads confidence signals directly from hidden states, based on the hypothesis that intermediate layers encode confidence signals that are lost in the final output layer.

**Key Features:**

- The probe adds less than 0.1% computational overhead and can run fully in parallel with generation, enabling hallucination detection before the answer is produced.

- The method evaluates hallucination risk in parallel with generation, enabling zero-latency responses for confident queries and supporting selective prediction and compute allocation while routing uncertain ones to stronger verification pipelines.

- The method achieves SOTA AUROC on 10 out of 12 settings across four QA benchmarks and three LLM families, with gains of up to 13 points over prior methods, and generalizes across dataset shifts without retraining.

**Methodology:**

The paper formulates hallucination detection as a knowledge prediction task, focusing on closed-book question answering where the model generates answers solely from its parametric knowledge without access to external sources.

The paper was published on arxiv on January 20, 2026 (arxiv ID: 2601.14210).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fa6bb5a-de7b-4abf-9c17-2f091ff4d8f9",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "4c683ae2-9572-4b75-b10b-1a57dd046aee",
  "sourceToolAssistantUUID": "9fa6bb5a-de7b-4abf-9c17-2f091ff4d8f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T09:01:44.478Z_

<details><summary>↩ Tool result · `toolu_017BhAfxqgd8QUiajk6oQBe3`</summary>

```text
Web search results for query: "arxiv "Dynamic Multimodal Activation Steering" DMAS 2602.21704 hallucination truthfulness steering vector"

Links: [{"title":"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/html/2602.21704v1"},{"title":"[2602.21704] Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/abs/2602.21704"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"DYNAMIC MULTIMODAL ACTIVATION STEERING FOR ...","url":"https://openreview.net/pdf/07c00654c7e18fa21deb56218948c8c6522ede71.pdf"},{"title":"[2602.07276] Steer2Adapt: Dynamically Composing Steering Vectors Elicits Efficient Adaptation of LLMs","url":"https://arxiv.org/abs/2602.07276"},{"title":"Steer2Adapt: Dynamically Composing Steering Vectors Elicits Efficient Adaptation of LLMs","url":"https://arxiv.org/html/2602.07276"},{"title":"SteerVLM: Robust Model Control through Lightweight Activation Steering for Vision Language Models","url":"https://arxiv.org/html/2510.26769v1"},{"title":"Multi-property Steering of Large Language Models with Dynamic Activation Composition Warning: This paper contains unsafe generations used for demonstrative purposes.","url":"https://arxiv.org/html/2406.17563v1"},{"title":"Surgical Activation Steering via Generative Causal Mediation","url":"https://arxiv.org/html/2602.16080v1"},{"title":"MLLMEraser: Achieving Test-Time Unlearning in Multimodal Large Language Models through Activation Steering","url":"https://arxiv.org/html/2510.04217v2"}]

Based on the search results, I found the paper you were looking for. Here's information about "Dynamic Multimodal Activation Steering" (DMAS):

## Overview

DMAS is a training-free approach for hallucination mitigation in Large Vision-Language Models (LVLMs), published on arXiv as paper 2602.21704.

## Key Research Findings

The research reveals that truthfulness and visual perception capabilities predominantly engage different subsets of attention heads within the model architecture, and truthfulness steering vectors vary significantly across different semantic contexts.

## Methodology

The method focuses on two types of attention heads in LVLMs: truthfulness-related and visual perception-related. For truthfulness heads, the researchers explicitly model how truthfulness steering vectors vary across semantic contexts by contrasting attention activations between factual and hallucination-prone samples to extract truthfulness steering vectors.

These vectors are stored alongside their cluster embeddings in a key-value database. For visual perception, activation differences between noise-free and noisy image inputs are used to derive perception steering vectors that enhance visual attention.

## Performance Results

The experimental results demonstrate significant improvements: increasing total scores by 94.66 on MME and reducing 20.2% hallucinations on CHAIR.

The method has faster inference speed compared to other decoding-based methods like VCD, while achieving better hallucination mitigation effects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aff8d34c-db54-434d-a3d6-af7bdabb9522",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "65471691-5775-4dc8-a7b2-78b4d4bd120f",
  "sourceToolAssistantUUID": "aff8d34c-db54-434d-a3d6-af7bdabb9522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-16T09:01:44.812Z_

<details><summary>↩ Tool result · `toolu_01Mvko9Ghqkvp2UvcH1PP3c5`</summary>

```text
Web search results for query: "arxiv VIB-Probe 2601.05547 information bottleneck hallucination attention head suppression"

Links: [{"title":"[2601.05547] VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language Models via Variational Information Bottleneck","url":"https://arxiv.org/abs/2601.05547"},{"title":"VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language Models via Variational Information Bottleneck","url":"https://arxiv.org/html/2601.05547"},{"title":"VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language","url":"https://arxiv.org/pdf/2601.05547"},{"title":"VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language Models via Variational Information Bottleneck | Request PDF","url":"https://www.researchgate.net/publication/399666840_VIB-Probe_Detecting_and_Mitigating_Hallucinations_in_Vision-Language_Models_via_Variational_Information_Bottleneck"},{"title":"Case Study: Predictive Coding and Information Bottleneck for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2601.15652"},{"title":"Mitigating Hallucinations in Large Vision-Language Models by Adaptively Constraining Information Flow","url":"https://arxiv.org/html/2502.20750"},{"title":"[2601.15652] Predictive Coding and Information Bottleneck for Hallucination Detection in Large Language Models","url":"https://arxiv.org/abs/2601.15652"},{"title":"Case Study: Predictive Coding and Information Bottleneck","url":"https://arxiv.org/pdf/2601.15652"},{"title":"DHI: Leveraging Diverse Hallucination Induction for Enhanced Contrastive Factuality Control in Large Language Models","url":"https://arxiv.org/html/2601.01156v1"},{"title":"DEEP VARIATIONAL INFORMATION BOTTLENECK","url":"https://openreview.net/pdf?id=HyxQzBceg"}]

Based on the search results, here's information about the paper arXiv:2601.05547:

## VIB-Probe: Overview

The paper "VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language Models via Variational Information Bottleneck" addresses hallucinations in Vision-Language Models (VLMs), where generated text deviates from the underlying visual content.

## Core Approach

The research investigates the outputs of internal attention heads, postulating that specific heads carry primary signals for truthful generation, though directly probing these high-dimensional states is challenging due to entanglement of visual-linguistic syntax and noise.

VIB-Probe leverages Variational Information Bottleneck (VIB) theory to extract discriminative patterns across layers and heads while filtering out semantic nuisances through the information bottleneck principle.

## Methodology and Attention Head Suppression

The framework operates in stages: extracting raw output vectors from all attention heads across Transformer layers, feeding features into an IB Encoder to compress high-dimensional input into compact latent representation while filtering out task-irrelevant noise.

By leveraging gradients of the VIB probe, the researchers identify attention heads with strong causal influence on hallucinations and introduce an inference-time intervention strategy for hallucination mitigation.

The inference-time mitigation is achieved by suppressing the attention heads with high risks of hallucination for each token, producing more faithful output generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0584cd2d-c307-4eb8-9e70-1cad6bda785b",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a7fa97b3924f82a62",
  "type": "user",
  "uuid": "6f9443d3-63de-431f-847b-3c70e6efd3a2",
  "sourceToolAssistantUUID": "0584cd2d-c307-4eb8-9e70-1cad6bda785b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-16T09:02:43.469Z_

Here is my comprehensive report from the literature search across all 8 queries plus follow-up searches.

---

## Potentially Overlooked Papers NOT in Your Cited List

### TIER 1 -- MOST DIRECTLY RELEVANT (probe/internal signal -> intervention during generation)

**1. FactCheckmate (arXiv 2410.02899, revised June 2025)**
This is arguably the closest existing work to the proposal's core idea. It trains a classifier on the model's hidden states to *preemptively detect* whether the LM will hallucinate, and then *intervenes by adjusting the LM's hidden states* so the model produces more factual outputs. It achieves over 70% preemptive detection accuracy, and outputs after intervention are 34.4% more factual. The detection-then-hidden-state-intervention pipeline is structurally very similar to "probe detects miscalibration -> logit/activation correction." This paper should absolutely be cited and differentiated from the proposal.

**2. Token-Guard (arXiv 2601.21969, ICLR 2026)**
A token-level hallucination control method via "self-checking decoding." It performs internal verification at each reasoning step, evaluates candidate fragments in a latent space with explicit hallucination risk scoring, and uses iterative pruning and regeneration to dynamically correct detected errors during generation. Published at ICLR 2026 -- a strong venue paper that closes the loop from detection to correction at generation time.

**3. VIB-Probe (arXiv 2601.05547, January 2026)**
Uses Variational Information Bottleneck theory to probe internal attention head outputs, identifies which heads carry hallucination risk, and then performs *inference-time mitigation by suppressing attention heads with high hallucination risk* for each token during generation. This is a direct probe-to-intervention pipeline, though it operates on attention heads rather than logits.

**4. HELIX / Tethered Reasoning (arXiv 2602.17691, February 2026)**
A geometric framework that computes a Unified Truth Score (UTS) combining token-level semantic entropy with Mahalanobis distance from a pre-computed "truthfulness manifold." When UTS indicates trajectory divergence, graduated steering vectors redirect activations, and *logit penalization redistributes probability mass* when UTS indicates low confidence. Steering activates for only 0.2-2.5% of tokens. This directly combines internal uncertainty signals with logit-level intervention. Focused on quantized models specifically.

**5. Adaptive Activation Steering / ACT (arXiv 2406.00034, ACM Web Conference 2025)**
Treats truthfulness as a linearly encoded concept within LLMs and adaptively shifts activations in the "truthful" direction during inference using diverse steering vectors from unsupervised clustering. Tuning-free. Large improvements on TruthfulQA. While it steers activations rather than logits per se, the mechanism is closely related.

**6. Dynamic Multimodal Activation Steering / DMAS (arXiv 2602.21704, February 2026)**
Training-free approach that identifies truthfulness-related and visual-perception-related attention heads, extracts context-specific truthfulness steering vectors by contrasting factual vs. hallucination-prone activations, and applies them during inference. Reduces hallucinations by 20.2% on CHAIR. Focused on vision-language models but the mechanism generalizes.

### TIER 2 -- HIGHLY RELEVANT (detection via probes/internal signals, but stops short of logit intervention)

**7. DRIFT (arXiv 2601.14210, January 2026)**
Lightweight residual probes that read hallucination risk directly from intermediate hidden states. Achieves SOTA AUROC on 10/12 settings. Crucially, the probe runs in parallel with generation at <0.1% overhead, but uses the signal for *routing* (answer immediately vs. delegate to stronger model) rather than for logit correction. The detection mechanism is almost exactly what the proposal describes on the detection side, but the intervention is routing rather than logit modification.

**8. HALP (arXiv 2603.05465, EACL 2026)**
Predicts hallucination risk from pre-generative internal states of VLMs via probes on pooled visual features and decoder states. Achieves up to 0.93 AUROC without any decoding. Detection only -- no generation-time intervention. But a natural upstream component for the kind of system the proposal describes.

**9. Neural Probe-Based Hallucination Detection (arXiv 2512.20949, December 2025)**
Shows that nonlinear MLP probes significantly outperform linear probes for hallucination detection on hidden states, because linear probes miss nonlinear semantics in deep hidden states. Important methodological finding for anyone building the probe component of a probe-to-intervention system.

**10. Calibrating Verbal Uncertainty as a Linear Feature (arXiv 2503.14477, EMNLP 2025)**
This appears to be Ji et al. (VUF) which is already in your cited list. Confirms that verbal uncertainty is governed by a single linear feature, that the mismatch between verbal and semantic uncertainty predicts hallucinations better than either alone, and that inference-time interventions on verbal uncertainty reduce hallucinations by ~30%. If this IS the Ji et al. VUF paper you already cite, then it is covered.

**11. Hallucination, Monofacts, and Miscalibration (arXiv 2502.08666, February 2025)**
Proves a theoretical lower bound on hallucination rate tied to the monofact rate minus model miscalibration. Provides theoretical grounding for why miscalibration-based signals should be useful for hallucination detection.

### TIER 3 -- ADJACENT WORK WORTH KNOWING

**12. SDCD: Structure-Disrupted Contrastive Decoding (arXiv 2601.03500, January 2026)**
Training-free algorithm performing contrastive calibration of output distributions using a shuffled structure-disrupted view. Text-based contrastive decoding for VLMs.

**13. DHI: Diverse Hallucination Induction (arXiv 2601.01156, January 2026)**
Leverages diverse hallucination induction for enhanced contrastive factuality control in LLMs.

**14. Predictive Coding and Information Bottleneck for Hallucination Detection (arXiv 2601.15652, January 2026)**
A case study applying predictive coding and IB theory to hallucination detection in LLMs.

---

## Answer to Your Core Question

**Is there any work that SPECIFICALLY combines internal uncertainty probes with logit-level intervention during generation?**

**Yes, but not in exactly the form the proposal describes.** Here is the landscape:

- **FactCheckmate** (2410.02899) comes closest: it uses a probe on hidden states to detect impending hallucinations and then *adjusts hidden states* (not logits directly) to correct them. The proposal should clearly differentiate its logit-level intervention from FactCheckmate's hidden-state intervention.

- **HELIX/Tethered Reasoning** (2602.17691) explicitly combines an internal uncertainty signal (Mahalanobis distance from a truthfulness manifold + semantic entropy) with *logit penalization* to redistribute probability mass. However, it is specifically designed for quantized models and uses a geometric framework rather than trained probes.

- **Token-Guard** (2601.21969, ICLR 2026) performs internal latent-space hallucination risk scoring and then prunes/regenerates tokens, operating at generation time. The detection is self-checking rather than a trained probe.

- **VIB-Probe** (2601.05547) trains probes on attention heads and then suppresses high-risk heads during generation -- probe-to-intervention, but at the attention level rather than logit level.

- **ACT/DMAS** steer activations toward truthfulness directions but use contrastive vectors rather than uncertainty probes.

**The specific combination of (a) a trained uncertainty probe that detects verbal-vs-internal confidence mismatch, which (b) triggers token-level logit adjustments during autoregressive generation, does NOT appear to exist as a published paper.** The proposal occupies a genuine gap. However, the individual components (probe-based detection, logit-level intervention, miscalibration signals) each have strong recent precedent, and **FactCheckmate** and **HELIX** in particular are close enough that the proposal must clearly articulate how it differs.

The most critical citations to add would be:
1. **FactCheckmate** (2410.02899) -- hidden-state probe -> hidden-state intervention
2. **Token-Guard** (2601.21969, ICLR 2026) -- self-checking -> token correction at generation time
3. **HELIX** (2602.17691) -- uncertainty signal -> logit penalization
4. **VIB-Probe** (2601.05547) -- trained probe -> attention head suppression
5. **DRIFT** (2601.14210) -- residual probe detection (no intervention, but strongest detection-only comparison)
6. **ACT** (2406.00034) -- activation steering for truthfulness

Sources:
- [FactCheckmate](https://arxiv.org/abs/2410.02899)
- [Token-Guard (ICLR 2026)](https://arxiv.org/abs/2601.21969)
- [VIB-Probe](https://arxiv.org/abs/2601.05547)
- [HELIX / Tethered Reasoning](https://arxiv.org/abs/2602.17691)
- [Adaptive Activation Steering (ACT)](https://arxiv.org/abs/2406.00034)
- [DMAS](https://arxiv.org/abs/2602.21704)
- [DRIFT](https://arxiv.org/abs/2601.14210)
- [HALP (EACL 2026)](https://arxiv.org/abs/2603.05465)
- [Neural Probe-Based Hallucination Detection](https://arxiv.org/abs/2512.20949)
- [Calibrating Verbal Uncertainty as a Linear Feature (EMNLP 2025)](https://arxiv.org/abs/2503.14477)
- [Hallucination, Monofacts, and Miscalibration](https://arxiv.org/abs/2502.08666)
- [SDCD](https://arxiv.org/abs/2601.03500)
- [DHI](https://arxiv.org/abs/2601.01156)
- [Predictive Coding and IB for Hallucination Detection](https://arxiv.org/abs/2601.15652)
- [Detecting Hallucinations via Internal Attention Divergence](https://arxiv.org/abs/2605.05025)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f9443d3-63de-431f-847b-3c70e6efd3a2",
  "isSidechain": true,
  "agentId": "a7fa97b3924f82a62",
  "requestId": "req_011Cb5yZqe8dViwY4NK82Bmc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8478833e-5f80-44cf-a278-5f2c2e7c0848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01292pxRa9d9wpBmkSF7prVF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1364,
      "cache_creation_input_tokens": 1156,
      "cache_read_input_tokens": 31911,
      "output_tokens": 2625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1156
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1364,
          "output_tokens": 2625,
          "cache_read_input_tokens": 31911,
          "cache_creation_input_tokens": 1156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1156,
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
