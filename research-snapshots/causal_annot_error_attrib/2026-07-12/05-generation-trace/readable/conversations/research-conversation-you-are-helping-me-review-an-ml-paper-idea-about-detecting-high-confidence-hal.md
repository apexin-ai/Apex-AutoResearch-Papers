# Research conversation: You are helping me review an ML paper idea about detecting high-confidence hallucinations (CHOKE) in LLMs using perturba

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa317dd5ea5975184.jsonl`
- **Structured JSON:** [`303a8088843b50ddd9fc.json`](../../sessions/30/303a8088843b50ddd9fc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-16T10:00:16.758Z_

You are helping me review an ML paper idea about detecting high-confidence hallucinations (CHOKE) in LLMs using perturbation of intermediate layer residual streams and measuring output logit KL divergence. I need you to search for competing and concurrent work that the proposal might have missed.

Please do the following searches using WebSearch:

1. "intermediate layer perturbation hallucination detection LLM 2025 2026" - any work perturbing middle layers for hallucination detection?

2. "logit sensitivity probing language model" OR "output distribution sensitivity perturbation LLM" - has anyone proposed something similar?

3. "forward-only sharpness estimation language model" OR "gradient-free sharpness proxy neural network" - methods that estimate sharpness without backprop?

4. "CHOKE hallucination detection 2025 2026" OR "high-confidence hallucination mitigation" - any recent work specifically on high-confidence/stubborn hallucinations?

5. "residual stream perturbation transformer factual knowledge" - any work perturbing residual streams at factual recall layers?

6. Search for "inference-time hallucination detection perturbation 2026" on arxiv

7. Search for "knowledge localization perturbation hallucination" - combining knowledge localization with perturbation for hallucination work

For each search, report what you found, especially any papers that are highly similar to the proposed LSP method. I'm particularly looking for work that: (a) perturbs at intermediate layers, (b) measures output logit changes, and (c) targets high-confidence hallucinations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "6e0750bc-1d3a-4901-9b99-120e3f38b9bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T10:00:16.762Z_

```json
{
  "parentUuid": "6e0750bc-1d3a-4901-9b99-120e3f38b9bd",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
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
  "uuid": "07c58e21-966b-4e3b-af0a-3a20c208cce1",
  "timestamp": "2026-05-16T10:00:16.762Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T10:00:19.123Z_



I'll run all seven searches in parallel to find competing and concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07c58e21-966b-4e3b-af0a-3a20c208cce1",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb642ikrcqykUXcHM7veB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e8d88f2-9c98-4f68-9892-f4b70dcd8bf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJnibaWi9vx5tp64bXkjKG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 8223,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 919,
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

_source line 4 · 2026-05-16T10:00:19.171Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MNuizQJ9btFdr6RFwGPnAn`</summary>

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
  "parentUuid": "6e8d88f2-9c98-4f68-9892-f4b70dcd8bf0",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb642ikrcqykUXcHM7veB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2ce80cf-618f-40b5-9ce7-33df457fd642",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJnibaWi9vx5tp64bXkjKG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 8223,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 919,
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

_source line 5 · 2026-05-16T10:00:19.175Z_

<details><summary>↩ Tool result · `toolu_01MNuizQJ9btFdr6RFwGPnAn`</summary>

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
  "parentUuid": "c2ce80cf-618f-40b5-9ce7-33df457fd642",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "acdec128-933e-472a-b26d-22473e9ed125",
  "sourceToolAssistantUUID": "c2ce80cf-618f-40b5-9ce7-33df457fd642",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T10:00:21.617Z_



Now let me run all seven searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acdec128-933e-472a-b26d-22473e9ed125",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb642uGsysP1d44egbV4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9660fd76-1b0c-4f98-b7a6-98dc8583720a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcnJGScdhz1VrjfqtzQhgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 7 · 2026-05-16T10:00:22.147Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TXxsCi4Yw3beZCqLSVPyw7`</summary>

```json
{
  "query": "intermediate layer perturbation hallucination detection LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9660fd76-1b0c-4f98-b7a6-98dc8583720a",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb642uGsysP1d44egbV4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45cf7622-4d0e-409f-b3b4-8de78862cdc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcnJGScdhz1VrjfqtzQhgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 8 · 2026-05-16T10:00:22.992Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MBFkjfkXtuMapkuzJvQXkh`</summary>

```json
{
  "query": "\"logit sensitivity probing language model\" OR \"output distribution sensitivity perturbation LLM\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45cf7622-4d0e-409f-b3b4-8de78862cdc1",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb642uGsysP1d44egbV4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c007ee78-61f3-4958-a89d-f50eee560dbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcnJGScdhz1VrjfqtzQhgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 9 · 2026-05-16T10:00:24.725Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JpmJxk9xjAR6oRZfHk5Raf`</summary>

```json
{
  "query": "\"forward-only sharpness estimation language model\" OR \"gradient-free sharpness proxy neural network\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c007ee78-61f3-4958-a89d-f50eee560dbe",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb642uGsysP1d44egbV4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d971e75-4422-4ad6-b763-604ac4eb3d98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcnJGScdhz1VrjfqtzQhgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 10 · 2026-05-16T10:00:24.898Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MSSg6tx1JnQ8aLCX6Sej1L`</summary>

```json
{
  "query": "CHOKE hallucination detection 2025 2026 OR \"high-confidence hallucination mitigation\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d971e75-4422-4ad6-b763-604ac4eb3d98",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb642uGsysP1d44egbV4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b17b7d3-559f-4210-8ff3-6cdc98b8d4e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcnJGScdhz1VrjfqtzQhgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 11 · 2026-05-16T10:00:25.700Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017DpL8X11NvqQNLkw2jLoEu`</summary>

```json
{
  "query": "residual stream perturbation transformer factual knowledge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b17b7d3-559f-4210-8ff3-6cdc98b8d4e3",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb642uGsysP1d44egbV4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3559daa8-66c5-481b-ac6d-0e397d4fd1bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcnJGScdhz1VrjfqtzQhgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 12 · 2026-05-16T10:00:26.862Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012TanhYxLPhcoviUTBKvpK1`</summary>

```json
{
  "query": "inference-time hallucination detection perturbation 2026 arxiv",
  "allowed_domains": [
    "arxiv.org",
    "scholar.google.com",
    "semanticscholar.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3559daa8-66c5-481b-ac6d-0e397d4fd1bc",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb642uGsysP1d44egbV4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb9a0eb8-634f-4aa7-802b-ac1ae3f7a6e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcnJGScdhz1VrjfqtzQhgA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9142,
      "output_tokens": 431,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1409
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 431,
          "cache_read_input_tokens": 9142,
          "cache_creation_input_tokens": 1409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1409,
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

_source line 13 · 2026-05-16T10:00:26.893Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bubch4Z8ERHhocZ4SbeQEV`</summary>

```json
{
  "query": "knowledge localization perturbation hallucination LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb9a0eb8-634f-4aa7-802b-ac1ae3f7a6e5",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb642uGsysP1d44egbV4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06875fc3-c9b5-4866-b9c5-9a25fc42a532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcnJGScdhz1VrjfqtzQhgA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9142,
      "output_tokens": 431,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1409
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 431,
          "cache_read_input_tokens": 9142,
          "cache_creation_input_tokens": 1409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1409,
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

_source line 14 · 2026-05-16T10:00:30.406Z_

<details><summary>↩ Tool result · `toolu_01MBFkjfkXtuMapkuzJvQXkh`</summary>

```text
Web search results for query: ""logit sensitivity probing language model" OR "output distribution sensitivity perturbation LLM""

Links: [{"title":"Revisiting Prompt Sensitivity in Large Language Models for Text Classification: The Role of Prompt Underspecification","url":"https://arxiv.org/html/2602.04297"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed ...","url":"https://aclanthology.org/2025.emnlp-main.530.pdf"},{"title":"[2602.04297] Revisiting Prompt Sensitivity in Large Language Models for Text Classification: The Role of Prompt Underspecification","url":"https://arxiv.org/abs/2602.04297"},{"title":"Understanding the Prompt Sensitivity | OpenReview","url":"https://openreview.net/forum?id=pHscguBJS7"},{"title":"Large language models robustness against perturbation | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-29770-0"},{"title":"Perturbation analysis and LLMs: How sensitive are LLMs to their input? | by Daniel Ferguson | Data Science + AI at Microsoft | Medium","url":"https://medium.com/data-science-at-microsoft/perturbation-analysis-and-llms-how-sensitive-are-llms-to-their-input-91a8407a971f"},{"title":"logit2prompt","url":"https://learnprompting.org/docs/language-model-inversion/logit2prompt"},{"title":"Inside the Prediction Layers of Large Language Models | by Zaina Haider | Medium","url":"https://medium.com/@thekzgroupllc/inside-the-prediction-layers-of-large-language-models-13fe7c685d90"},{"title":"What Did I Do Wrong? Quantifying LLMs’ Sensitivity and Consistency to Prompt Engineering | Request PDF","url":"https://www.researchgate.net/publication/392503901_What_Did_I_Do_Wrong_Quantifying_LLMs'_Sensitivity_and_Consistency_to_Prompt_Engineering"}]

I found several relevant research papers on your query. Here are the key findings:

## Recent Research on Logit Sensitivity and Perturbation Analysis

### 1. **Calibrating LLM Confidence by Probing Perturbed Representation Stability**

The original entropy of the LLM's output distribution for a token emerges as an important feature, with higher original entropy typically showing a negative correlation with prediction correctness, indicating that greater initial uncertainty is indicative of potentially incorrect answers. The margin between the logits of the top-ranked and second-ranked tokens after perturbation often shows a positive correlation with correctness; a larger margin, even under adversarial stress, indicates a more decisive and less ambiguous output from the LLM.

### 2. **Prompt Sensitivity in Large Language Models for Text Classification**

Instruction-based formats significantly improve performance and logit distributions compared to minimal prompts. Logit analysis shows logit values are a good indicator of prompt quality, with positive correlation to accuracy as high as 0.757, while linear probe analysis shows internal representations are only marginally affected by prompt underspecification, with issues emerging primarily in the final layers.

### 3. **LLM Robustness Against Perturbation**

Even minor deviations–such as a single character substitution, misspelling, or word replacement–can cause unexpected outputs or degraded model performance.

These papers address the intersection of logit analysis, sensitivity probing, and perturbation analysis in language models, examining how small changes to inputs affect the output distribution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c007ee78-61f3-4958-a89d-f50eee560dbe",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "f255d27d-57e2-45fd-b36c-f7864ac956f1",
  "sourceToolAssistantUUID": "c007ee78-61f3-4958-a89d-f50eee560dbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T10:00:31.601Z_

<details><summary>↩ Tool result · `toolu_01TXxsCi4Yw3beZCqLSVPyw7`</summary>

```text
Web search results for query: "intermediate layer perturbation hallucination detection LLM 2025 2026"

Links: [{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Understanding, measuring and controlling LLM hallucinations","url":"https://angelo-lima.fr/en/llm-hallucinations-devoxx-2026-en/"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"How to evaluate LLM hallucination rates in engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/how-to-evaluate-llm-hallucination-rates-in-engineering/"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"Detecting Hallucination in Large Language Models Through","url":"https://www.ijcai.org/proceedings/2025/0929.pdf"},{"title":"Hallucinations","url":"https://www.aussieai.com/research/hallucinations"},{"title":"A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3703155"},{"title":"LLM-Check: Investigating Detection of Hallucinations in Large Language Models","url":"https://openreview.net/pdf?id=LYx4w3CAgy"}]

Based on my search results, here's what I found on **intermediate layer perturbation hallucination detection in LLMs (2025-2026)**:

## Key Research

A notable approach called Sample-Specific Prompting (SSP) improves hallucination detection by analyzing perturbation sensitivity at intermediate representations, dynamically generating noise prompts for each input and employing a lightweight encoder to amplify changes in representations caused by perturbation.

Recent methods train lightweight probes (3M–37M parameters) on intermediate hidden states instead of final-layer outputs, since middle layers retain uncertainty signals that the token-projection step throws away.

## Technical Approaches

The reasoning behind using intermediate layers is that as bias accumulates through the model's layers, the final output can diverge from the underlying reasoning process, while intermediate representations, being less influenced by model bias, offer a more faithful view of the model's latent reasoning process.

## 2025-2026 Developments

Research analyzes LLMs as dynamic graphs by examining structural properties of internal attention mechanisms, extracting spectral features (eigenvalues) from attention maps to predict hallucinations—factual retrieval produces stable eigen-structures, while hallucination leads to diffuse, chaotic patterns.

JPMorgan Chase's 2025 patent formalizes query perturbation: incoming queries are perturbed multiple times into semantically equivalent variations with independent agents sampling outputs, enabling hallucination probability prediction before the LLM generates any response.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45cf7622-4d0e-409f-b3b4-8de78862cdc1",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "f61aee7d-883c-4511-a0f5-7d36eb26394d",
  "sourceToolAssistantUUID": "45cf7622-4d0e-409f-b3b4-8de78862cdc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T10:00:31.976Z_

<details><summary>↩ Tool result · `toolu_01JpmJxk9xjAR6oRZfHk5Raf`</summary>

```text
Web search results for query: ""forward-only sharpness estimation language model" OR "gradient-free sharpness proxy neural network""

Links: [{"title":"(PDF) SharpZO: Hybrid Sharpness-Aware Vision Language Model Prompt Tuning via Forward-Only Passes","url":"https://www.researchgate.net/publication/393066281_SharpZO_Hybrid_Sharpness-Aware_Vision_Language_Model_Prompt_Tuning_via_Forward-Only_Passes"},{"title":"SharpZO: Hybrid Sharpness-Aware Vision Language Model Prompt Tuning via Forward-Only Passes","url":"https://arxiv.org/html/2506.20990v1"},{"title":"(PDF) GRADIENT-FREE PROXY FOR EFFICIENT LANGUAGE MODEL SEARCH","url":"https://www.researchgate.net/publication/376072656_GRADIENT-FREE_PROXY_FOR_EFFICIENT_LANGUAGE_MODEL_SEARCH"},{"title":"Sharpness aware vision language model prompt tuning via forward-only passes - Amazon Science","url":"https://www.amazon.science/publications/sharpness-aware-vision-language-model-prompt-tuning-via-forward-only-passes"},{"title":"Physical neural networks using sharpness-aware training | Nature Communications","url":"https://www.nature.com/articles/s41467-026-68470-9"},{"title":"Stabilizing Sharpness-Aware Minimization Through A ...","url":"https://www.jmlr.org/papers/volume26/24-0065/24-0065.pdf"},{"title":"[2506.20990] SharpZO: Hybrid Sharpness-Aware Vision Language Model Prompt Tuning via Forward-Only Passes","url":"https://arxiv.org/abs/2506.20990"},{"title":"Sharpness-Aware Minimization Improves Language Model ...","url":"https://aclanthology.org/2022.acl-long.508.pdf"},{"title":"Enhancing Sharpness-Aware Optimization Through Variance Suppression","url":"https://arxiv.org/html/2309.15639v3"},{"title":"ZeroGrads: Learning Local Surrogates for Non-Differentiable Graphics","url":"https://arxiv.org/html/2308.05739v2"}]

Based on the search results, I found several relevant papers addressing your query about forward-only sharpness estimation and gradient-free methods for neural networks:

## Key Results:

**SharpZO: Hybrid Sharpness-Aware Vision Language Model Prompt Tuning**

SharpZO is a hybrid Sharpness-aware Zeroth-order optimization approach specifically designed to enhance the performance of ZO VLM fine-tuning via a sharpness-aware warm-up training. It employs a two-stage framework where the first stage performs warm-up training using a sharpness-aware Covariance Matrix Adaptation Evolution Strategy (CMA-ES), which provides both a smoother loss landscape and a strong initialization for the second stage.

The second stage performs fine-grained local optimization using a sparse Zeroth-Order Stochastic Gradient Descent (ZO-SGD) method, and introduces a novel Z-pruning technique specifically designed for noisy ZO settings.

**W-PCA: Gradient-Free Proxy for Language Model Search**

Another relevant work introduces weight-weighted PCA (W-PCA), a novel zero-shot NAS method specifically tailored for lightweight language models, utilizing two evaluation proxies: the parameter count and principal component analysis (PCA) value of the feed-forward neural (FFN) layer.

These methods represent recent advances in enabling neural network optimization without backpropagation, addressing computational and memory constraints particularly relevant for edge devices and inference-only scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d971e75-4422-4ad6-b763-604ac4eb3d98",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "beaf2270-94d0-4cf4-bbe0-ef0b244933cd",
  "sourceToolAssistantUUID": "6d971e75-4422-4ad6-b763-604ac4eb3d98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T10:00:34.521Z_

<details><summary>↩ Tool result · `toolu_01Bubch4Z8ERHhocZ4SbeQEV`</summary>

```text
Web search results for query: "knowledge localization perturbation hallucination LLM"

Links: [{"title":"[2311.05232] A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions","url":"https://arxiv.org/abs/2311.05232"},{"title":"LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction","url":"https://arxiv.org/html/2512.18623"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689v4"},{"title":"A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3703155"},{"title":"Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs","url":"https://arxiv.org/html/2505.16894"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models","url":"https://arxiv.org/html/2401.01313v1"},{"title":"1 A Survey on Hallucination in Large Language Models:","url":"https://arxiv.org/pdf/2311.05232"},{"title":"You believe your LLM is not delusional? Think again! a study of LLM hallucination on foundation models under perturbation | Discover Data | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44248-025-00041-7"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"}]

Based on the search results, here's what I found about knowledge localization, perturbation, and hallucination in Large Language Models:

## Key Research Areas

**Knowledge Localization and Model Editing:**
The "locate-then-edit" paradigm involves identifying neurons or parameters most relevant to a piece of knowledge and then applying a calculated update. However, these approaches apply static and permanent perturbations to the model's weights and often struggle with context-dependent hallucinations and risk accumulating negative side effects that degrade unrelated knowledge.

**Perturbation-Based Hallucination Detection:**
Recent research has discovered that perturbing key entities in prompts affects LLM's generation of different hallucination types differently. Studies systematically perturb key entities to assess their impact on generated tokens, demonstrating how these perturbations can determine whether the generated tokens are hallucinated.

**Context Perturbation and Internal Dynamics:**
Research examines how context perturbations trigger systematic drift in LLM hidden representations leading to hallucinations. Injected contexts form an "attention shadow," gradually shifting model focus, causing representation drift, and ultimately generating incorrect answers.

**Sample-Specific Perturbation:**
A hallucination detection method induces internal representation shifts in LLMs by concatenating learnable, sample-specific noise prompts into the input, then designs a scoring function to quantify these representation changes as a discriminative signal.

These research directions represent emerging approaches to understanding and mitigating hallucinations through careful analysis of how models localize knowledge and respond to input perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06875fc3-c9b5-4866-b9c5-9a25fc42a532",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "12985f57-33fe-40db-b6a5-7fcc1fc6fb27",
  "sourceToolAssistantUUID": "06875fc3-c9b5-4866-b9c5-9a25fc42a532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T10:00:34.533Z_

<details><summary>↩ Tool result · `toolu_012TanhYxLPhcoviUTBKvpK1`</summary>

```text
Web search results for query: "inference-time hallucination detection perturbation 2026 arxiv"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"Hallucinations Live in Variance","url":"https://arxiv.org/html/2601.07058v1"},{"title":"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2601.02170v1"},{"title":"[2601.15652] Predictive Coding and Information Bottleneck for Hallucination Detection in Large Language Models","url":"https://arxiv.org/abs/2601.15652"},{"title":"Do We Really Need External Tools to Mitigate Hallucinations? Sira: Shared-Prefix Internal Reconstruction of Attribution","url":"https://arxiv.org/html/2605.14621"},{"title":"Hallucination Detection and Mitigation in Large Language Models","url":"https://arxiv.org/html/2601.09929v1"},{"title":"HALT: Hallucination Assessment via Log-probs as Time series","url":"https://arxiv.org/html/2602.02888v1"},{"title":"[2502.03799] Enhancing Hallucination Detection through Noise Injection","url":"https://arxiv.org/abs/2502.03799"},{"title":"LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction","url":"https://arxiv.org/html/2512.18623"},{"title":"Weakly Supervised Distillation of Hallucination Signals into Transformer Representations","url":"https://arxiv.org/html/2604.06277"}]

I found several highly relevant research papers on arxiv from 2026 related to inference-time hallucination detection and perturbation:

## Key Papers Found:

1. **Unified Theoretical Framework for Hallucination Detection** (ICLR 2026)
   This work addresses hallucinations from inference-time instabilities in multi-step generation, noting that existing detectors usually target only one source and lack solid theoretical foundation. The paper considers perturbations in a local neighborhood of the decoding process.

2. **"Hallucinations Live in Variance"** (January 2026)
   This paper addresses that existing methods don't directly measure variance-driven instability under semantic perturbation. The work defines hallucination as variance-driven instability under semantic perturbation.

3. **Streaming Hallucination Detection in Long Chain-of-Thought** (January 2026)
   The work analyzes over 10,000 long CoT trajectories with 200k+ reasoning steps, including 40k+ hallucinated steps. The approach enables online hallucination detection without additional inference cost.

4. **Enhancing Hallucination Detection through Noise Injection** (March 2026)
   This proposes a training-free approach based on perturbing an appropriate subset of model parameters, or equivalently hidden unit activations, during sampling. The approach significantly improves inference-time hallucination detection over standard sampling.

5. **HALT: Hallucination Assessment via Log-probs as Time series** (February 2026)
   This proposes treating token log-probabilities as a time series, classifying hallucinations based on temporal dynamics rather than absolute values.

These papers represent the latest work on detection methods combining inference-time analysis with perturbation techniques for hallucination identification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb9a0eb8-634f-4aa7-802b-ac1ae3f7a6e5",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "02554bc3-2ff3-4072-9d90-f0d6e85ec16f",
  "sourceToolAssistantUUID": "fb9a0eb8-634f-4aa7-802b-ac1ae3f7a6e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T10:00:36.171Z_

<details><summary>↩ Tool result · `toolu_01MSSg6tx1JnQ8aLCX6Sej1L`</summary>

```text
Web search results for query: "CHOKE hallucination detection 2025 2026 OR "high-confidence hallucination mitigation""

Links: [{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"🚨 AI Hallucinations Are Getting Smarter — Here’s How to Catch Them in Real-Time (Even in Agentic AI Systems, 2026) | by Yash Mishra | Feb, 2026 | Medium","url":"https://medium.com/@yash.mishra0501/ai-hallucinations-are-getting-smarter-heres-how-to-catch-them-in-real-time-even-in-agentic-3d75a9fc1ab3"},{"title":"AI Hallucination Rates & Benchmarks in 2026","url":"https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"},{"title":"LLM Hallucination: Understanding AI Text Errors in 2026 | Label Your Data","url":"https://labelyourdata.com/articles/llm-fine-tuning/llm-hallucination"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"[2601.09929] Hallucination Detection and Mitigation in Large Language Models","url":"https://arxiv.org/abs/2601.09929"},{"title":"How to evaluate LLM hallucination rates in engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/how-to-evaluate-llm-hallucination-rates-in-engineering/"},{"title":"On Hallucinations in Artificial Intelligence–Generated ...","url":"https://jnm.snmjournals.org/content/jnumed/early/2025/11/06/jnumed.125.270653.full.pdf"},{"title":"Clippers 9/23: Ash Lewis on Detection and Mitigation of Hallucination in AI Dialogues | CLLT","url":"https://u.osu.edu/cllt/2025/09/22/clippers-9-23-ash-lewis-on-detection-and-mitigation-of-hallucination-in-ai-dialogues/"},{"title":"AI Hallucination Statistics 2026: 50+ Sourced Data Points - Suprmind","url":"https://suprmind.ai/hub/insights/ai-hallucination-statistics-research-report-2026/"}]

I've completed the web search for "CHOKE hallucination detection 2025 2026 OR high-confidence hallucination mitigation". 

## Search Results Summary

The search returned 10 relevant sources covering recent hallucination detection and mitigation research from 2025-2026. Here are the key findings:

**Recent Hallucination Detection & Mitigation Approaches:**

Rewarding Doubt (2025) integrates confidence calibration into reinforcement learning, penalizing both over- and underconfidence so model certainty better matches correctness.

VeriFY, published at ICML 2025, teaches models to assess factual uncertainty during generation rather than relying on post-hoc checking, with the model learning to verify its own claims as it produces them.

RAG (Retrieval-Augmented Generation) remains the single best general-purpose mitigation for knowledge-related hallucinations, with enhanced RAG pipelines in domains like medicine, public health, or law showing significantly lower hallucination rates than vanilla RAG.

**High-Confidence Hallucination Mitigation:**

MIT research from January 2025 found that when AI models hallucinate, they use more confident language than when providing factual information, with models 34% more likely to use phrases like "definitely" and "certainly" when generating incorrect information.

**Patent Innovations (2025-2026):**

Microsoft Technology Licensing contributes both forward-backward hallucination detection technique and a calibrated confidence estimation filing covering model-agnostic and domain-calibrated approaches.

JPMorgan Chase Bank's 2025 patent on hallucination probability prediction allows a risk threshold to gate whether a query proceeds to the model or triggers human expert review.

However, I did not find specific results about a technique or framework called "CHOKE" in these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b17b7d3-559f-4210-8ff3-6cdc98b8d4e3",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "dd4eace7-53d8-4f2f-8568-ea184a430e65",
  "sourceToolAssistantUUID": "8b17b7d3-559f-4210-8ff3-6cdc98b8d4e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T10:00:36.994Z_

<details><summary>↩ Tool result · `toolu_017DpL8X11NvqQNLkw2jLoEu`</summary>

```text
Web search results for query: "residual stream perturbation transformer factual knowledge"

Links: [{"title":"Exploring the Residual Stream of Transformers","url":"https://arxiv.org/html/2312.12141v1"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://arxiv.org/html/2410.16090v1"},{"title":"Knowledge Circuits in Pretrained Transformers Yunzhi Yao1 Ningyu Zhang1∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d6df31b1be98e04be48af8bedb95b499-Paper-Conference.pdf"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Exploring the Residual Stream of Transformers for Mechanistic Interpretability — Explained | by Zeping Yu | Medium","url":"https://medium.com/@zepingyu/123-cb62513f5d50"},{"title":"Residual Stream Activations","url":"https://www.emergentmind.com/topics/residual-stream-activations"},{"title":"[2410.16090] Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://arxiv.org/abs/2410.16090"},{"title":"Mechanistic View of Transformers: Patterns, Messages, Residual Stream… and LSTMs | Towards Data Science","url":"https://towardsdatascience.com/mechanistic-view-of-transformers-patterns-messages-residual-stream-and-lstms/"},{"title":"[2405.15943] Transformers represent belief state geometry in their residual stream","url":"https://arxiv.org/abs/2405.15943"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Transformer+residual+stream"}]

I found several relevant research papers and resources about residual stream perturbation and factual knowledge in transformers. Here's what the search revealed:

## Key Findings

**Residual Stream and Factual Knowledge Storage:**

Research has hypothesized that factual knowledge is stored in FFN layers, with evaluation of contribution scores of each FFN subvalue using integrated gradients. However, analysis also shows that attention layers preserve important parameters, suggesting factual knowledge is distributed across multiple components.

**How Knowledge is Merged:**

For the example "The capital of France is Paris", knowledge is stored in both attention layers and FFN layers—some attention subvalues provide knowledge "Paris is related to France", while some FFN subvalues provide knowledge "Paris is a capital", which are mainly activated by attention subvalues related to "capitals/cities".

**Perturbation and Distribution Analysis:**

Research explores the distribution change of residual connections in vocabulary space, finding that the distribution change is caused by a direct addition function on before-softmax values. Perturbation experiments in GPT-2 demonstrate that real residual activations exhibit greater robustness and plateau width, reflecting rich geometric/statistical structure.

**Knowledge Conflicts Detection:**

Through probing tasks, researchers found that LLMs can internally register the signal of knowledge conflict in the residual stream, which can be accurately detected by probing the intermediate model activations.

These findings suggest that residual stream perturbation is a valuable technique for understanding how transformers store and retrieve factual knowledge across their architecture.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3559daa8-66c5-481b-ac6d-0e397d4fd1bc",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "796da0b1-8104-4e15-856a-3d259ce46898",
  "sourceToolAssistantUUID": "3559daa8-66c5-481b-ac6d-0e397d4fd1bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T10:00:39.446Z_

Let me now do a few targeted follow-up searches on the most directly relevant papers I spotted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "796da0b1-8104-4e15-856a-3d259ce46898",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb644DG8opBJRbyjvNAsR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b30c849-dd13-4e9e-81a4-4cc8e84a702d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7ajkV7iYXEKRoQLqjsDRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1820,
      "cache_creation_input_tokens": 5373,
      "cache_read_input_tokens": 10551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5373,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 22 · 2026-05-16T10:00:40.585Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kev2ULMhXSqNSKGon57f2N`</summary>

```json
{
  "query": "\"Probing LLM Hallucination from Within\" perturbation internal knowledge arxiv 2411.09689"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b30c849-dd13-4e9e-81a4-4cc8e84a702d",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb644DG8opBJRbyjvNAsR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29b075de-61c8-47f7-a73b-16510dcabb96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7ajkV7iYXEKRoQLqjsDRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1820,
      "cache_creation_input_tokens": 5373,
      "cache_read_input_tokens": 10551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5373,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 23 · 2026-05-16T10:00:41.431Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LrqCwDfJ4iFp3uuMEmeWqX`</summary>

```json
{
  "query": "\"Enhancing Hallucination Detection through Noise Injection\" hidden unit activations perturbation arxiv 2502.03799"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29b075de-61c8-47f7-a73b-16510dcabb96",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb644DG8opBJRbyjvNAsR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1bf469e-5916-487b-b187-a3e72d39ea3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7ajkV7iYXEKRoQLqjsDRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1820,
      "cache_creation_input_tokens": 5373,
      "cache_read_input_tokens": 10551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5373,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 24 · 2026-05-16T10:00:41.924Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FQ2zRcBGz63P1wmrH8Dd4n`</summary>

```json
{
  "query": "\"Calibrating LLM Confidence by Probing Perturbed Representation Stability\" arxiv 2505.21772"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1bf469e-5916-487b-b187-a3e72d39ea3c",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb644DG8opBJRbyjvNAsR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d73b0780-9a63-4675-b530-8ec9c944b8a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7ajkV7iYXEKRoQLqjsDRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1820,
      "cache_creation_input_tokens": 5373,
      "cache_read_input_tokens": 10551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5373,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 25 · 2026-05-16T10:00:43.062Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PsnMtj8VguvBLTd8ARkUsg`</summary>

```json
{
  "query": "\"LLM-CAS Dynamic Neuron Perturbation\" real-time hallucination correction arxiv 2512.18623"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d73b0780-9a63-4675-b530-8ec9c944b8a7",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb644DG8opBJRbyjvNAsR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20c62318-9504-4ae9-bc03-268366673369",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7ajkV7iYXEKRoQLqjsDRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1820,
      "cache_creation_input_tokens": 5373,
      "cache_read_input_tokens": 10551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5373,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 26 · 2026-05-16T10:00:43.412Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RDQBJhHoeVxSkzoyF3Rwtx`</summary>

```json
{
  "query": "\"Shaking to Reveal\" perturbation-based detection LLM hallucinations arxiv 2506.02696"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20c62318-9504-4ae9-bc03-268366673369",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb644DG8opBJRbyjvNAsR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "847a87d2-5916-440b-9fa3-2e2a42cac0e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7ajkV7iYXEKRoQLqjsDRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1820,
      "cache_creation_input_tokens": 5373,
      "cache_read_input_tokens": 10551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5373,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 27 · 2026-05-16T10:00:44.034Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UBZhzW7DE5oNwJJoy5XUmY`</summary>

```json
{
  "query": "\"Hallucinations Live in Variance\" semantic perturbation arxiv 2601.07058"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "847a87d2-5916-440b-9fa3-2e2a42cac0e6",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb644DG8opBJRbyjvNAsR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb13c8b8-beeb-42a9-a798-f634eaf91865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7ajkV7iYXEKRoQLqjsDRV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1820,
      "cache_creation_input_tokens": 5373,
      "cache_read_input_tokens": 10551,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5373
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1820,
          "output_tokens": 410,
          "cache_read_input_tokens": 10551,
          "cache_creation_input_tokens": 5373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5373,
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

_source line 28 · 2026-05-16T10:00:47.298Z_

<details><summary>↩ Tool result · `toolu_01Kev2ULMhXSqNSKGon57f2N`</summary>

```text
Web search results for query: ""Probing LLM Hallucination from Within" perturbation internal knowledge arxiv 2411.09689"

Links: [{"title":"[2411.09689] Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/abs/2411.09689"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge — Seongmin Lee","url":"https://seongmin.xyz/papers/llm-hallucination-probing"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Method via Internal Knowledge | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11402288/"},{"title":"LLM Hallucination Reasoning with Zero-shot Knowledge Test","url":"https://arxiv.org/html/2411.09689v1"},{"title":"Trust Me, I’m Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/html/2502.12964"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"Hallucination Detection via Internal States and Structured Reasoning Consistency in Large Language Models","url":"https://arxiv.org/html/2510.11529v1"},{"title":"Case Study: Predictive Coding and Information Bottleneck for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2601.15652"},{"title":"Hallucination Detection with the Internal Layers of LLMs","url":"https://www.arxiv.org/pdf/2509.14254"}]

I've found information about the paper "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge" (arXiv 2411.09689).

## Summary

LLM hallucination, where unfaithful text is generated, presents a critical challenge for LLMs' practical applications. Current detection methods often resort to external knowledge, LLM fine-tuning, or supervised training with large hallucination-labeled datasets, and these approaches do not distinguish between different types of hallucinations.

The paper proposes SHINE, a novel hallucination probing method driven by the discovery that perturbing key entities in prompts affects LLM's generation of three types of text differently, and it does not require external knowledge, supervised training, or LLM fine-tuning.

## Key Methodology

The paper introduces hallucination probing, a new task that classifies LLM-generated text into three categories: aligned, misaligned, and fabricated. The Model Knowledge Test consists of three steps: identifying the key subject, perturbing the subject tokens' embeddings, and measuring the perturbation's impact on text generation.

The approach leverages the insight that since LLMs tend to fabricate for unfamiliar subjects, perturbing embeddings should yield a small perturbation effect for such subjects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29b075de-61c8-47f7-a73b-16510dcabb96",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "aa21ac8d-4a54-4539-9977-f1e655ec539e",
  "sourceToolAssistantUUID": "29b075de-61c8-47f7-a73b-16510dcabb96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T10:00:47.386Z_

<details><summary>↩ Tool result · `toolu_01LrqCwDfJ4iFp3uuMEmeWqX`</summary>

```text
Web search results for query: ""Enhancing Hallucination Detection through Noise Injection" hidden unit activations perturbation arxiv 2502.03799"

Links: [{"title":"[2502.03799] Enhancing Hallucination Detection through Noise Injection","url":"https://arxiv.org/abs/2502.03799"},{"title":"Enhancing Hallucination Detection through Noise Injection","url":"https://arxiv.org/html/2502.03799v2"},{"title":"Enhancing Hallucination Detection through Noise Injection | alphaXiv","url":"https://www.alphaxiv.org/ja/overview/2502.03799v1"},{"title":"Enhancing Hallucination Detection with Noise Injection | OpenReview","url":"https://openreview.net/forum?id=2bWf4M5tRo"},{"title":"Noise Augmented Fine Tuning for Mitigating Hallucinations in Large Language Models","url":"https://arxiv.org/html/2504.03302v2"},{"title":"Demystifying Hallucination in Speech Foundation Models","url":"https://aclanthology.org/2025.findings-acl.1190.pdf"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v2"},{"title":"Hallucination Detection: A Probabilistic Framework Using Embeddings Distance Analysis","url":"https://arxiv.org/html/2502.08663v1"},{"title":"Hallucination Elimination and Semantic Enhancement Framework for Vision-Language Models in Traffic Scenarios","url":"https://arxiv.org/html/2412.07518v1"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"}]

I found the paper! Here's what I found about arxiv 2502.03799:

**Paper Title:** Enhancing Hallucination Detection through Noise Injection

**Key Findings:**

Large Language Models (LLMs) are prone to generating plausible yet incorrect responses, known as hallucinations, and effectively detecting hallucinations is crucial for the safe deployment of LLMs.

Recent research has linked hallucinations to model uncertainty, suggesting that hallucinations can be detected by measuring dispersion over answer distributions obtained from multiple samples drawn from a model. However, the authors argue that drawing from the distribution over tokens defined by the model is suboptimal for the purpose of detecting hallucinations.

**Proposed Approach:**

The paper proposes a simple, training-free approach based on perturbing an appropriate subset of model parameters, or equivalently hidden unit activations, during sampling. More specifically, by perturbing hidden unit activations in intermediate layers of the model is complementary to sampling and can significantly improve detection accuracy over mere sampling.

The paper was published in February 2025 and provides an approach for improving hallucination detection in LLMs by incorporating model uncertainty in the Bayesian sense through activation perturbation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1bf469e-5916-487b-b187-a3e72d39ea3c",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "9237b863-1bf9-440e-838e-4155785e013a",
  "sourceToolAssistantUUID": "e1bf469e-5916-487b-b187-a3e72d39ea3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T10:00:47.741Z_

<details><summary>↩ Tool result · `toolu_01FQ2zRcBGz63P1wmrH8Dd4n`</summary>

```text
Web search results for query: ""Calibrating LLM Confidence by Probing Perturbed Representation Stability" arxiv 2505.21772"

Links: [{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250521772K/abstract"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Calibrating LLM Confidence by Probing Perturbed ...","url":"https://www.alphaxiv.org/resources/2505.21772v2"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | alphaXiv","url":"https://www.alphaxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed ...","url":"https://bytez.com/docs/arxiv/2505.21772/paper"},{"title":"[Literature Review] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.themoonlight.io/en/review/calibrating-llm-confidence-by-probing-perturbed-representation-stability"},{"title":"Natural Language Processing Papers on X: \"Calibrating LLM Confidence by Probing Perturbed Representation Stability. https://t.co/e8jEwkURbh\" / X","url":"https://x.com/HEI/status/1928282977009611169"}]

I found the paper! Here's information about it:

## Paper Overview

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method analyzing internal representational stability in LLMs.

## Problem Addressed

Miscalibration in Large Language Models (LLMs) undermines their reliability, highlighting the need for accurate confidence estimation.

## Method

CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness.

## Evaluation

CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats.

## Results

Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points.

## Availability

The paper is available on arXiv at https://arxiv.org/abs/2505.21772, and there's also a GitHub repository with the implementation available at https://github.com/ledengary/CCPS.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d73b0780-9a63-4675-b530-8ec9c944b8a7",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "be376e9b-068c-47a8-af24-e0be5381d14c",
  "sourceToolAssistantUUID": "d73b0780-9a63-4675-b530-8ec9c944b8a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T10:00:50.298Z_

<details><summary>↩ Tool result · `toolu_01RDQBJhHoeVxSkzoyF3Rwtx`</summary>

```text
Web search results for query: ""Shaking to Reveal" perturbation-based detection LLM hallucinations arxiv 2506.02696"

Links: [{"title":"[2506.02696] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696"},{"title":"[2506.02696v1] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/pdf/2506.02696"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://www.researchgate.net/publication/392371301_Shaking_to_Reveal_Perturbation-Based_Detection_of_LLM_Hallucinations"},{"title":"[Literature Review] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://www.themoonlight.io/en/review/shaking-to-reveal-perturbation-based-detection-of-llm-hallucinations"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://www.alphaxiv.org/overview/2506.02696v1"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689v4"},{"title":"LLM Hallucination Detection: A Fast Fourier Transform Method Based on Hidden Layer Temporal Signals Citation: Authors. Title. Pages…. DOI:000000/11111.","url":"https://arxiv.org/html/2509.13154v1"},{"title":"Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs","url":"https://arxiv.org/html/2505.16894v1"}]

I found detailed information about the paper "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations" (arxiv 2506.02696).

## Summary

Hallucination remains a key obstacle to the reliable deployment of large language models in question answering tasks, and a widely adopted strategy to detect hallucination, known as self-assessment, relies on the model's own output confidence to estimate the factual accuracy of its answers. However, this strategy assumes that the model's output distribution closely reflects the true data distribution, which may not always hold in practice, as bias accumulates through the model's layers and the final output can diverge from the underlying reasoning process.

## The Proposed Method

The paper proposes Sample-Specific Prompting (SSP), a new framework that improves self-assessment by analyzing perturbation sensitivity at intermediate representations. These representations, being less influenced by model bias, offer a more faithful view of the model's latent reasoning process.

## Key Results

The method improves hallucination detection accuracy by 4.78% (AUROC) on the challenging TruthfulQA benchmark compared to state-of-the-art methods.

## Authors

The paper was authored by Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, and Ling Chen, with affiliations at the Australian Artificial Intelligence Institute and University of Wisconsin-Madison.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "847a87d2-5916-440b-9fa3-2e2a42cac0e6",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "b7f73436-15de-4a80-95b8-5a26b30ad398",
  "sourceToolAssistantUUID": "847a87d2-5916-440b-9fa3-2e2a42cac0e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T10:00:50.301Z_

<details><summary>↩ Tool result · `toolu_01PsnMtj8VguvBLTd8ARkUsg`</summary>

```text
Web search results for query: ""LLM-CAS Dynamic Neuron Perturbation" real-time hallucination correction arxiv 2512.18623"

Links: [{"title":"[2512.18623] LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction","url":"https://arxiv.org/abs/2512.18623"},{"title":"LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction","url":"https://arxiv.org/html/2512.18623"},{"title":"LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction","url":"https://ojs.aaai.org/index.php/AAAI/article/download/40776/44737"},{"title":"H-Neurons: On the Existence, Impact, and Origin of Hallucination-Associated Neurons in LLMs","url":"https://arxiv.org/html/2512.01797v2"},{"title":"Hallucination-Associated Neurons in LLMs","url":"https://www.emergentmind.com/topics/hallucination-associated-neurons-h-neurons"},{"title":"H-Neurons: On the Existence, Impact, and Origin of ...","url":"https://arxiv.org/pdf/2512.01797"},{"title":"Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning","url":"https://arxiv.org/html/2512.19920v3"},{"title":"H-Neurons: On the Existence, Impact, and Origin of Hallucination-Associated Neurons","url":"https://arxiv.org/html/2512.01797v1"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689v4"},{"title":"ArXiv Papers Browser - Teng Wang","url":"http://ttengwang.com/arxiv-papers.html"}]

Based on the search results, I found the paper you're looking for. Here's the information about LLM-CAS:

## LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction

LLM-CAS is a framework that formulates real-time hallucination correction as a hierarchical reinforcement learning problem, training an agent to learn a policy that dynamically selects temporary neuron perturbations during inference based on the current context.

### Problem it Addresses

Large language models often generate hallucinated content that lacks factual or contextual grounding, limiting their reliability in critical applications. Existing approaches such as supervised fine-tuning and reinforcement learning from human feedback are data intensive and computationally expensive, while static parameter editing methods struggle with context dependent errors and catastrophic forgetting.

### Key Innovation

LLM-CAS trains an agent to learn a sophisticated policy that dynamically selects optimal, temporary neuron perturbations during inference based on the immediate context, providing greater adaptability than prior dynamic methods that rely on heuristic or pre-defined approaches.

The paper (arxiv 2512.18623) was published on December 21, 2025, and represents a novel approach to handling hallucinations by using learned, context-aware neuron perturbations rather than static modifications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20c62318-9504-4ae9-bc03-268366673369",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "83ab2e11-15b7-45dd-8cbb-d665454a6f62",
  "sourceToolAssistantUUID": "20c62318-9504-4ae9-bc03-268366673369",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T10:00:51.558Z_

<details><summary>↩ Tool result · `toolu_01UBZhzW7DE5oNwJJoy5XUmY`</summary>

```text
Web search results for query: ""Hallucinations Live in Variance" semantic perturbation arxiv 2601.07058"

Links: [{"title":"[2601.07058] Hallucinations Live in Variance","url":"https://arxiv.org/abs/2601.07058"},{"title":"Hallucinations Live in Variance","url":"https://arxiv.org/html/2601.07058"},{"title":"Hallucinations Live in Variance Aaron R. Flouro Shawn P. Chadwick, PhD","url":"https://arxiv.org/pdf/2601.07058"},{"title":"Multi-Teacher Ensemble Distillation: A Mathematical Framework for Probability-Domain Knowledge Aggregation","url":"https://arxiv.org/html/2601.09165v1"},{"title":"Adaptive Weighting in Knowledge Distillation: An Axiomatic Framework for Multi-Scale Teacher Ensemble Optimization","url":"https://arxiv.org/html/2601.17910v1"},{"title":"Computer Science Jan 2026","url":"https://arxiv.org/list/cs/2026-01?skip=3400"},{"title":"Detecting Hallucinations in Retrieval-Augmented Generation via Semantic-level Internal Reasoning Graph","url":"https://arxiv.org/html/2601.03052"},{"title":"Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration","url":"https://arxiv.org/html/2603.22812v1"},{"title":"Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs","url":"https://arxiv.org/html/2505.16894"},{"title":"[2603.22812v1] Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration","url":"https://arxiv.org/abs/2603.22812v1"}]

Based on the search results, here's what I found about the paper "Hallucinations Live in Variance" (arXiv 2601.07058):

## Overview

Hallucinations live in variance: they arise when semantically equivalent prompts activate inconsistent internal pathways, producing divergent outputs.

## Key Concept

Throughout this paper, hallucination refers exclusively to variance-driven instability under semantic perturbation. The paper distinguishes this from other types of model failures: Consistent but incorrect outputs reflect bias or missing knowledge; confident guessing reflects calibration failure.

## Semantic Stability Metric

Semantic Stability directly measures variance-driven instability by evaluating agreement across paraphrased prompts under deterministic (greedy) decoding, without relying on ground truth, sampling randomness, or external resources.

## Main Contribution

They introduce a metric that exposes variance-driven unreliability, show how compression can reduce it, and map the regimes where this holds.

## Authors

The paper was submitted on January 11, 2026, by Aaron R. Flouro and Shawn P. Chadwick.

The paper addresses an important distinction: Benchmarks measure whether a model is correct but do not measure whether a model is reliable, a distinction that becomes critical for agentic AI systems, where a single rephrased prompt can trigger cascading failures in multi-step execution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb13c8b8-beeb-42a9-a798-f634eaf91865",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "fc96deca-31a3-42d2-a1ad-799878a67513",
  "sourceToolAssistantUUID": "cb13c8b8-beeb-42a9-a798-f634eaf91865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-16T10:00:54.133Z_

Now let me search for a couple more highly relevant angles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc96deca-31a3-42d2-a1ad-799878a67513",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb645HWtyofM4ZkrqSUaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "983dceb4-cf4e-4152-ae1b-fa84b7e42ad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8595ndoj3qRywTtrk2XQM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7438,
      "cache_read_input_tokens": 15924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7438,
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

_source line 35 · 2026-05-16T10:00:54.741Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018pA484WDk9sQdev6qgEC7k`</summary>

```json
{
  "query": "\"Shadows in the Attention\" contextual perturbation representation drift hallucination arxiv 2505.16894"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "983dceb4-cf4e-4152-ae1b-fa84b7e42ad8",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb645HWtyofM4ZkrqSUaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db27adac-fd3b-478f-ae86-a701427f04bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8595ndoj3qRywTtrk2XQM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7438,
      "cache_read_input_tokens": 15924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7438,
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

_source line 36 · 2026-05-16T10:00:56.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015W4FrWY2hzJsScJEAJcz1z`</summary>

```json
{
  "query": "KL divergence output logits perturbation intermediate layers hallucination detection LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db27adac-fd3b-478f-ae86-a701427f04bf",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb645HWtyofM4ZkrqSUaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6de70b0b-2a1c-489f-83be-9bbd71d3b8ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8595ndoj3qRywTtrk2XQM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7438,
      "cache_read_input_tokens": 15924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7438,
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

_source line 37 · 2026-05-16T10:00:56.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B7f1Dxq9e6UaR2FLNa8EVW`</summary>

```json
{
  "query": "\"logit sensitivity\" OR \"logit stability\" perturbation hallucination factual knowledge transformer 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6de70b0b-2a1c-489f-83be-9bbd71d3b8ee",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb645HWtyofM4ZkrqSUaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4c36818-8aac-4451-bd4d-ff32e5584033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8595ndoj3qRywTtrk2XQM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7438,
      "cache_read_input_tokens": 15924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7438,
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

### Tool result

_source line 38 · 2026-05-16T10:01:03.322Z_

<details><summary>↩ Tool result · `toolu_018pA484WDk9sQdev6qgEC7k`</summary>

```text
Web search results for query: ""Shadows in the Attention" contextual perturbation representation drift hallucination arxiv 2505.16894"

Links: [{"title":"[2505.16894] Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs","url":"https://arxiv.org/abs/2505.16894"},{"title":"Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs","url":"https://arxiv.org/html/2505.16894"},{"title":"Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-4088-4_32"},{"title":"Spotlight and Shadow: Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation","url":"https://arxiv.org/html/2604.10071v1"},{"title":"Fine-Grained Perturbation Guidance via Attention Head Selection","url":"https://arxiv.org/html/2506.10978v3"},{"title":"Attention Mechanisms in Dynamical Systems: A Case Study with","url":"https://arxiv.org/pdf/2505.06503"},{"title":"Regional Attention for Shadow Removal","url":"https://arxiv.org/html/2411.14201v1"},{"title":"AttnTrace: Attention-based Context Traceback for Long-Context LLMs","url":"https://arxiv.org/html/2508.03793v1"},{"title":"Structure Disruption: Subverting Malicious Diffusion-Based Inpainting via Self-Attention Query Perturbation","url":"https://arxiv.org/html/2505.19425v1"},{"title":"arXiv:2505.03856v1 [cs.CV] 6 May 2025","url":"https://arxiv.org/pdf/2505.03856"}]

I found the paper you're looking for! Here are the details:

## "Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs"

This paper, with arXiv identifier 2505.16894, was submitted on May 22, 2025 by Zeyu Wei, Shuo Wang, Xiaohui Rong, Xuemin Liu, and He Li.

**Key Research Overview:**

The paper presents the first systematic study linking hallucination incidence to internal-state drift induced by incremental context injection.

**Methodology:**

The researchers construct two 16-round "titration" tracks per question using TruthfulQA: one appends relevant but partially flawed snippets, the other injects deliberately misleading content. Across six open-source LLMs, they track overt hallucination rates with a tri-perspective detector and covert dynamics via cosine, entropy, JS and Spearman drifts of hidden states and attention maps.

**Key Findings:**

Results reveal that hallucination frequency and representation drift show monotonic growth that plateaus after 5-7 rounds; relevant context drives deeper semantic assimilation producing high-confidence "self-consistent" hallucinations, whereas irrelevant context induces topic-drift errors anchored by attention re-routing.

You can access the full paper on arXiv at https://arxiv.org/abs/2505.16894.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db27adac-fd3b-478f-ae86-a701427f04bf",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "cd4038b0-9f4f-4cfa-ac0b-248a9b27e19a",
  "sourceToolAssistantUUID": "db27adac-fd3b-478f-ae86-a701427f04bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-16T10:01:03.481Z_

<details><summary>↩ Tool result · `toolu_015W4FrWY2hzJsScJEAJcz1z`</summary>

```text
Web search results for query: "KL divergence output logits perturbation intermediate layers hallucination detection LLM"

Links: [{"title":"Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses","url":"https://arxiv.org/html/2407.05474v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"On LLM Knowledge Distillation - A Comparison between Forward KL and Reverse KL | ICLR Blogposts 2025","url":"https://d2jud02ci9yv69.cloudfront.net/2025-04-28-llm-knowledge-distil-157/blog/llm-knowledge-distil/"},{"title":"Diverging Towards Hallucination: Detection of Failures in Vision-Language Models via Multi-token Aggregation","url":"https://arxiv.org/html/2505.11741v1"},{"title":"Reducing LLM Hallucinations using Epistemic Neural Networks","url":"https://arxiv.org/html/2312.15576"},{"title":"Uncertainty, Confidence, and Hallucination in Large Language Models","url":"https://hungleai.substack.com/p/uncertainty-confidence-and-hallucination"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/pdf/2506.02696"},{"title":"Detect, Classify, and Fix: Zero-Shot Hallucination Reasoning for LLMs | by Anna Alexandra Grigoryan | Medium","url":"https://thegrigorian.medium.com/detect-classify-and-fix-zero-shot-hallucination-reasoning-for-llms-e1086bb11bca"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689"},{"title":"Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores","url":"https://arxiv.org/html/2603.22299"}]

I've found relevant research on your topic. Here's what the search results show about KL divergence, perturbation, intermediate layers, and hallucination detection in LLMs:

## Key Research Findings

**Perturbation-Based Detection Using Intermediate Layers:**

A framework called Sample-Specific Prompting (SSP) improves hallucination detection by analyzing perturbation sensitivity at intermediate representations, which are less influenced by model bias and offer a more faithful view of the model's latent reasoning process.

**KL Divergence as a Discrepancy Measure:**

KL divergence has been investigated as one of the alternative distance measures for detecting hallucinations, alongside Manhattan distance and Euclidean distance. However, cosine-based metrics consistently provide better separability between truthful and hallucinated responses across all evaluated datasets compared to KL divergence approaches.

**Entity Perturbation and KL Divergence:**

Low entity perturbation impact measured by KL divergence strongly indicates fabricated text, with fabricated text showing much lower mean KL divergence (0.21) than aligned text (0.92).

**Output Logits vs. Intermediate Representations:**

As bias accumulates through the model's layers, the final output can diverge from the underlying reasoning process, making output-level confidence an unreliable signal for hallucination detection.

**KL Divergence in Knowledge Distillation:**

Forward KL divergence used as a loss function in knowledge distillation has been shown to introduce hallucination issues in language models due to its tendency toward mean-seeking optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6de70b0b-2a1c-489f-83be-9bbd71d3b8ee",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "465d5be9-daea-4302-9fc2-538865a22d92",
  "sourceToolAssistantUUID": "6de70b0b-2a1c-489f-83be-9bbd71d3b8ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T10:01:07.740Z_

<details><summary>↩ Tool result · `toolu_01B7f1Dxq9e6UaR2FLNa8EVW`</summary>

```text
Web search results for query: ""logit sensitivity" OR "logit stability" perturbation hallucination factual knowledge transformer 2025 2026"

Links: [{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://seongheon-96.github.io/assets/pdf/shaking.pdf"},{"title":"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/html/2605.05686"},{"title":"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/html/2605.05025"},{"title":"Generalization or Hallucination? Understanding Out-of-Context Reasoning in Transformers","url":"https://arxiv.org/html/2506.10887v3"},{"title":"Mechanisms of Non-Factual Hallucination in Language Models","url":"https://arxiv.org/html/2403.18167v1"},{"title":"DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models","url":"https://arxiv.org/html/2509.13702"},{"title":"Mechanistic Understanding and Mitigation of Language ...","url":"https://aclanthology.org/2024.findings-emnlp.466.pdf"},{"title":"[2506.10887] Generalization or Hallucination? Understanding Out-of-Context Reasoning in Transformers","url":"https://arxiv.org/abs/2506.10887"},{"title":"Theoretical Foundations and Mitigation of Hallucination in Large Language Models","url":"https://arxiv.org/html/2507.22915v1"}]

I found several highly relevant recent research papers on this topic. Here are the key findings from the web search:

## Recent Research on Logit Sensitivity/Stability, Perturbations, and Hallucination Detection

### 1. **Gradient Sensitivity and Stubborn Hallucinations (2025)**

A recent study addresses the problem of "Stubborn Hallucinations" where LLMs generate factually incorrect content with high confidence and stability, proposing Embedding-Perturbed Gradient Sensitivity (EPGS) as a geometric framework that distinguishes between generalized knowledge in flat minima and brittle memorization in sharp minima by probing the loss landscape through continuous embedding perturbations. EPGS detects sharpness by perturbing input embeddings with Gaussian noise and measuring gradient magnitude spikes, acting as an efficient proxy for the Hessian spectrum to differentiate stable knowledge from unstable memorization.

### 2. **Attractor Geometry and Logit Gap (2025-2026)**

Research shows that geometric margin (based on hidden state geometry) detects errors that entropy cannot, and this advantage grows with scale, noting that the frozen LM head cannot distinguish failure states from correct recall as it reads only the output logit gap rather than the hidden-state geometry. Geometric margin—the hidden state's distance to the nearest memorized basin—separates correct recall from hallucination far more cleanly than output entropy, with zero false refusals where entropy-based detection cannot avoid rejecting the vast majority of correct outputs.

### 3. **Attention Divergence and Factual Knowledge (2025)**

Common uncertainty quantification methods rely on logit- and likelihood-based signals such as log-likelihood, perplexity, maximum token probability, or predictive entropy. Recent work finds that internal attention divergence signals are concentrated in middle layers and peak at factual tokens such as named entities and numbers, suggesting that internal attention dynamics provide an efficient white-box signal of model uncertainty.

### 4. **Logit-Space Optimization for Hallucination Suppression (2025)**

A framework called DSCC-HS operates through contrastive logit-space optimization during training, iteratively aligning proxy models into two adversarial roles through parameter-efficient LoRA adaptation.

### 5. **Out-of-Context Reasoning and Hallucination (2025-2026)**

Research argues that both generalization and hallucination stem from a single mechanism called out-of-context reasoning (OCR): the ability to deduce implications by associating concepts, with experiments confirming that OCR drives both behaviors depending on whether the associated concepts are causally related.

These papers collectively demonstrate a shift from confidence-based detection methods toward geometric and perturbation-based approaches for detecting hallucinations in transformers, with particular focus on logit sensitivity and stability metrics introduced in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4c36818-8aac-4451-bd4d-ff32e5584033",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "60e525e6-e03b-483f-9c15-a2feceef4ea4",
  "sourceToolAssistantUUID": "a4c36818-8aac-4451-bd4d-ff32e5584033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-16T10:01:11.411Z_

That last search returned a critically important hit. Let me dig into the two papers that appear most directly competitive.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60e525e6-e03b-483f-9c15-a2feceef4ea4",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb646Un6TNmownBY6W61J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef0ba668-4ed4-4c4d-9269-8080773925ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVNB99ZCSMSwWBVmrbCawB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3333,
      "cache_read_input_tokens": 23362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3333,
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

_source line 42 · 2026-05-16T10:01:13.142Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F4pTnqehu3BUaHcwUKpaa3`</summary>

```json
{
  "query": "\"From Flat Facts to Sharp Hallucinations\" gradient sensitivity stubborn errors arxiv 2605.00939"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef0ba668-4ed4-4c4d-9269-8080773925ec",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb646Un6TNmownBY6W61J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "375f82cb-4ae4-4a06-a5b9-48df0294c56c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVNB99ZCSMSwWBVmrbCawB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3333,
      "cache_read_input_tokens": 23362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3333,
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

_source line 43 · 2026-05-16T10:01:13.298Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UpL6LnvgSrWHJq3qggZ1jo`</summary>

```json
{
  "query": "\"Attractor Geometry of Transformer Memory\" confident hallucination arxiv 2605.05686"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "375f82cb-4ae4-4a06-a5b9-48df0294c56c",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb646Un6TNmownBY6W61J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83e806bb-3126-4fac-9db8-53fb7dde4cb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVNB99ZCSMSwWBVmrbCawB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3333,
      "cache_read_input_tokens": 23362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3333,
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

_source line 44 · 2026-05-16T10:01:14.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P9iJDMCx8AHtJ2yiHfwSwW`</summary>

```json
{
  "query": "\"Between the Layers Lies the Truth\" uncertainty estimation LLM intra-layer arxiv 2603.22299"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83e806bb-3126-4fac-9db8-53fb7dde4cb5",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb646Un6TNmownBY6W61J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "836d38ec-3e3b-42ce-ba44-79b5811f0c0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVNB99ZCSMSwWBVmrbCawB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3333,
      "cache_read_input_tokens": 23362,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3333
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 23362,
          "cache_creation_input_tokens": 3333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3333,
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

_source line 45 · 2026-05-16T10:01:18.910Z_

<details><summary>↩ Tool result · `toolu_01F4pTnqehu3BUaHcwUKpaa3`</summary>

```text
Web search results for query: ""From Flat Facts to Sharp Hallucinations" gradient sensitivity stubborn errors arxiv 2605.00939"

Links: [{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"The Phenomenology of Hallucinations","url":"https://arxiv.org/html/2603.13911"},{"title":"[2605.01428] Hallucinations Undermine Trust; Metacognition is a Way Forward","url":"https://arxiv.org/abs/2605.01428"},{"title":"HalluGen: Synthesizing Realistic and Controllable Hallucinations for Evaluating Image Restoration","url":"https://arxiv.org/html/2512.03345"},{"title":"[2605.13146] On Hallucinations in Inverse Problems: Fundamental Limits and Provable Assessment Methods","url":"https://arxiv.org/abs/2605.13146"},{"title":"Why Language Models Hallucinate","url":"https://arxiv.org/html/2509.04664v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2509.21473v1"},{"title":"[2604.04020v1] Unmasking Hallucinations: A Causal Graph-Attention Perspective on Factual Reliability in Large Language Models","url":"https://arxiv.org/abs/2604.04020v1"},{"title":"Last Update: September 29, 2025 Are Hallucinations Bad Estimations? Hude Liu∗1","url":"https://arxiv.org/pdf/2509.21473"}]

Based on the search results, I found the paper you're looking for:

"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity" is a recent arXiv paper (2605.00939).

The paper proposes a geometric solution called Embedding-Perturbed Gradient Sensitivity (EPGS). The core hypothesis is that "robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization."

To detect this difference in sharpness, EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude. This approach leverages the geometric properties of the loss landscape to distinguish between reliable factual knowledge and errors that are prone to hallucination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "375f82cb-4ae4-4a06-a5b9-48df0294c56c",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "756b27b8-9f95-48d8-8832-f56a91e994de",
  "sourceToolAssistantUUID": "375f82cb-4ae4-4a06-a5b9-48df0294c56c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T10:01:22.364Z_

<details><summary>↩ Tool result · `toolu_01UpL6LnvgSrWHJq3qggZ1jo`</summary>

```text
Web search results for query: ""Attractor Geometry of Transformer Memory" confident hallucination arxiv 2605.05686"

Links: [{"title":"[2605.05686] Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/abs/2605.05686"},{"title":"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/html/2605.05686"},{"title":"[2605.12466] Solve the Loop: Attractor Models for Language and Reasoning","url":"https://arxiv.org/abs/2605.12466"},{"title":"Understanding and controlling the geometry of memory organization in RNNs","url":"https://arxiv.org/html/2502.07256"},{"title":"Solve the Loop: Attractor Models for Language and Reasoning","url":"https://arxiv.org/html/2605.12466"},{"title":"[2605.07721] Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models","url":"https://arxiv.org/abs/2605.07721"},{"title":"Self-attention as an attractor network: transient memories without backpropagation M. N. acknowledges the support of PNRR MUR Project No. PE0000013-FAIR.","url":"https://arxiv.org/html/2409.16112v1"},{"title":"Attractor Memory for Long-Term Time Series Forecasting: A Chaos Perspective","url":"https://arxiv.org/html/2402.11463v7"},{"title":"The Bayesian Geometry of Transformer Attention","url":"https://arxiv.org/html/2512.22471"},{"title":"Revisiting Transformer Layer Parameterization Through Causal Energy Minimization","url":"https://arxiv.org/html/2605.07588"}]

I found the paper you requested! Here's information about "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination" (arxiv 2605.05686):

## Overview

The paper studies how language models draw on two knowledge sources—facts baked into weights (parametric memory) and information in context (working memory)—examining two failure modes: conflict when these disagree and interfere, and hallucination when the queried fact was never learned.

## Key Findings

The researchers show both failures share a unified geometric account: in the hidden-state space of autoregressive generation, learned facts form attractor basins. More specifically:

- Conflict is basin competition: working memory disrupts convergence to the correct basin without raising output entropy.
- Hallucination is basin absence: the hidden state drifts freely when no memorized basin exists.

## Why This Matters

Both failure modes produce confident output regardless, making output-based monitoring blind by design. Geometric margin—the hidden state's distance to the nearest memorized basin—reads this geometry directly and separates correct recall from hallucination far more cleanly than output entropy.

The paper was submitted to arXiv on May 7, 2026, and includes authors Qiyao Liang, Risto Miikkulainen, and Ila Fiete.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83e806bb-3126-4fac-9db8-53fb7dde4cb5",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "44030e2b-93ee-45e7-9314-11befed4b896",
  "sourceToolAssistantUUID": "83e806bb-3126-4fac-9db8-53fb7dde4cb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-16T10:01:22.885Z_

<details><summary>↩ Tool result · `toolu_01P9iJDMCx8AHtJ2yiHfwSwW`</summary>

```text
Web search results for query: ""Between the Layers Lies the Truth" uncertainty estimation LLM intra-layer arxiv 2603.22299"

Links: [{"title":"[2603.22299] Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores","url":"https://arxiv.org/abs/2603.22299"},{"title":"Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores","url":"https://arxiv.org/html/2603.22299v1"},{"title":"Between the Layers Lies the Truth:","url":"https://arxiv.org/pdf/2603.22299"},{"title":"Enhancing Uncertainty Estimation in LLMs with Expectation of Aggregated Internal Belief","url":"https://arxiv.org/html/2509.01564"},{"title":"Enhancing Uncertainty Estimation in LLMs with ...","url":"https://arxiv.org/pdf/2509.01564"},{"title":"Uncertainty Estimation and Quantification for LLMs: A Simple","url":"https://arxiv.org/pdf/2404.15993"},{"title":"Uncertainty Estimation and Quantification for LLMs: A Simple Supervised Approach","url":"https://arxiv.org/html/2404.15993v3"},{"title":"Towards Reliable Truth-Aligned Uncertainty Estimation in Large Language Models","url":"https://arxiv.org/html/2604.00445"},{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Ambiguous Prompts and Unanswerable Questions","url":"https://arxiv.org/html/2412.10246v2"}]

Great! I found the paper you're looking for. Here are the details:

## Paper Summary

The paper is titled "Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores" with the arXiv identifier 2603.22299.

### Key Contributions

The paper addresses the fact that large language models (LLMs) are often confidently wrong, making reliable uncertainty estimation essential. While output-based heuristics are cheap but brittle, and probing internal representations is effective yet high-dimensional and hard to transfer, the authors propose a compact, per-instance uncertainty estimation method that scores cross-layer agreement patterns in internal representations using a single forward pass.

### Methodology

The approach views each layer's post-MLP activation as a probability distribution (via temperature-scaled softmax over the hidden dimension) and computes a pairwise, directed KL divergence between layers at task-relevant tokens. The resulting L×L signature compactly captures cross-layer (dis)agreement. A small gradient-boosted tree (GBDT) model, trained on these maps, predicts whether the model's answer is correct.

### Performance Results

Across three models, the method matches probing in-distribution, with mean diagonal differences of at most -1.8 AUPRC percentage points and +4.9 Brier score points. Under cross-dataset transfer, it consistently outperforms probing, achieving off-diagonal gains up to +2.86 AUPRC and +21.02 Brier points. Under 4-bit weight-only quantization, it remains robust, improving over probing by +1.94 AUPRC points and +5.33 Brier points on average.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "836d38ec-3e3b-42ce-ba44-79b5811f0c0d",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "aa317dd5ea5975184",
  "type": "user",
  "uuid": "aaeff3c6-6b0b-4f91-a802-9678b9632e64",
  "sourceToolAssistantUUID": "836d38ec-3e3b-42ce-ba44-79b5811f0c0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-16T10:02:30.895Z_

Here is a comprehensive report of my findings across all seven searches, organized by relevance to the proposed LSP/CHOKE method.

---

## CRITICAL FINDINGS: Highly Similar / Directly Competing Work

### 1. "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity" (arXiv 2605.00939, May 2026)

**Threat level: VERY HIGH -- this is the closest competitor I found.**

This paper proposes Embedding-Perturbed Gradient Sensitivity (EPGS), which shares the exact same core hypothesis as your proposal: "robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization." EPGS perturbs input embeddings with Gaussian noise and measures the resulting spike in gradient magnitude as a proxy for loss landscape sharpness. It explicitly targets "stubborn errors" (high-confidence hallucinations). The key difference from LSP is that EPGS (a) perturbs at the embedding level rather than intermediate residual streams, and (b) requires gradient computation (backprop), whereas your proposal is forward-only. If your method is truly gradient-free, that is a meaningful differentiator, but you absolutely must cite and contrast with this paper.

- [From Flat Facts to Sharp Hallucinations](https://arxiv.org/abs/2605.00939)

### 2. "Enhancing Hallucination Detection through Noise Injection" (arXiv 2502.03799, Feb 2025)

**Threat level: HIGH -- overlaps on perturbation of hidden activations at intermediate layers.**

This paper proposes a training-free approach that perturbs hidden unit activations in intermediate layers during sampling and measures the effect on output distributions. It frames this as complementary to sampling-based uncertainty and shows significant improvement in hallucination detection accuracy. The overlap with LSP is substantial: (a) it perturbs intermediate layer activations, (b) it measures output distribution changes, and (c) it is training-free/forward-only. The difference may be that it focuses on sampling diversity rather than KL divergence of logits, and it does not specifically target high-confidence hallucinations. This is a must-cite.

- [Enhancing Hallucination Detection through Noise Injection](https://arxiv.org/abs/2502.03799)

### 3. "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations" (arXiv 2506.02696, June 2025)

**Threat level: HIGH -- proposes Sample-Specific Prompting (SSP) that analyzes perturbation sensitivity at intermediate representations.**

This paper improves hallucination detection by analyzing perturbation sensitivity at intermediate representations, arguing that these are less influenced by model bias than final-layer outputs. It uses a lightweight encoder to amplify changes in representations caused by perturbation. The method targets the same insight as LSP (intermediate layers are more informative than output-layer confidence), though it focuses on representation-level sensitivity rather than output logit KL divergence. Achieved +4.78% AUROC improvement on TruthfulQA.

- [Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations](https://arxiv.org/abs/2506.02696)

### 4. SHINE: "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge" (arXiv 2411.09689, Nov 2024)

**Threat level: HIGH -- perturbs entity embeddings and measures impact on generation.**

This paper proposes SHINE, which perturbs key subject-entity token embeddings and measures how the perturbation impacts text generation. It classifies outputs into aligned, misaligned, and fabricated categories. The key insight is that fabricated text (unfamiliar subjects) shows low KL divergence (0.21) after perturbation, while aligned text shows high KL divergence (0.92). This is essentially using KL divergence of output distributions after perturbation as a hallucination signal -- very close to your proposal. The difference is perturbation at the embedding layer rather than intermediate residual streams.

- [Probing LLM Hallucination from Within](https://arxiv.org/abs/2411.09689)

### 5. "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination" (arXiv 2605.05686, May 2026)

**Threat level: MODERATE-HIGH -- provides a geometric theory for exactly why high-confidence hallucinations occur.**

This paper models learned facts as attractor basins in hidden-state space. Hallucination is "basin absence" (the hidden state drifts freely when no memorized basin exists), while knowledge conflict is "basin competition." Crucially, both produce confident output, making output-based monitoring blind by design. They propose "geometric margin" (distance to nearest memorized basin) as a superior detector to output entropy. This provides a theoretical framework that could either support or compete with the flat/sharp minima framing. The paper explicitly argues that the frozen LM head cannot distinguish failure states because it only reads the output logit gap rather than hidden-state geometry -- this is a direct challenge to any method (including LSP) that relies on output logit changes.

- [Attractor Geometry of Transformer Memory](https://arxiv.org/abs/2605.05686)

---

## IMPORTANT RELATED WORK (should be cited)

### 6. "Calibrating LLM Confidence by Probing Perturbed Representation Stability" (CCPS) (arXiv 2505.21772, EMNLP 2025)

Applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response, and uses a lightweight classifier to predict answer correctness. Reduces Expected Calibration Error by ~55%. Perturbation is at final hidden states rather than intermediate layers, but the overall methodology (perturb representations, measure stability) is closely related.

- [Calibrating LLM Confidence by Probing Perturbed Representation Stability](https://arxiv.org/abs/2505.21772)

### 7. LLM-CAS: "Dynamic Neuron Perturbation for Real-Time Hallucination Correction" (arXiv 2512.18623, Dec 2025, AAAI)

Uses RL to train an agent that dynamically selects temporary neuron perturbations during inference for real-time hallucination correction. This goes beyond detection to correction, but the perturbation mechanism at the neuron level during inference is related.

- [LLM-CAS: Dynamic Neuron Perturbation](https://arxiv.org/abs/2512.18623)

### 8. "Shadows in the Attention: Contextual Perturbation and Representation Drift" (arXiv 2505.16894, May 2025)

First systematic study linking hallucination to internal-state drift induced by incremental context injection. Tracks cosine, entropy, JS, and Spearman drifts of hidden states and attention maps. Relevant context drives "self-consistent" high-confidence hallucinations -- directly relevant to the CHOKE framing.

- [Shadows in the Attention](https://arxiv.org/abs/2505.16894)

### 9. "Between the Layers Lies the Truth: Uncertainty Estimation Using Intra-Layer Local Information Scores" (arXiv 2603.22299, March 2026)

Computes pairwise KL divergence between layers at task-relevant tokens using a single forward pass. The L x L cross-layer KL divergence signature is exactly the kind of "inter-layer agreement" signal that relates to measuring how stable representations are across layers. This is complementary/competing to LSP's approach of perturbing at specific layers.

- [Between the Layers Lies the Truth](https://arxiv.org/abs/2603.22299)

### 10. "Hallucinations Live in Variance" (arXiv 2601.07058, Jan 2026)

Defines hallucination as variance-driven instability under semantic perturbation, proposing a "Semantic Stability" metric. Distinguishes itself from bias (consistent but incorrect) and calibration failure (confident guessing). Relevant framing for the CHOKE problem.

- [Hallucinations Live in Variance](https://arxiv.org/abs/2601.07058)

### 11. "Detecting Hallucinations via Internal Attention Divergence Signals" (arXiv 2605.05025, May 2026)

Finds that internal attention divergence signals are concentrated in middle layers and peak at factual tokens (named entities, numbers), suggesting middle-layer dynamics provide a white-box hallucination signal -- supports the layer selection strategy in your proposal.

- [Detecting Hallucinations via Internal Attention Divergence](https://arxiv.org/abs/2605.05025)

### 12. SharpZO: Forward-Only Sharpness-Aware Optimization (arXiv 2506.20990)

While not about hallucination detection, this paper demonstrates that forward-only (zeroth-order) methods can estimate sharpness for language models, which is relevant if your method claims to be a "gradient-free sharpness proxy."

- [SharpZO](https://arxiv.org/abs/2506.20990)

---

## SEARCH RESULT: "CHOKE" as a named method

No existing paper or framework named "CHOKE" was found in any search. The name appears to be available.

---

## KEY TAKEAWAYS FOR YOUR PROPOSAL

1. **The biggest risk is arXiv 2605.00939** ("From Flat Facts to Sharp Hallucinations"). It shares the same flat-minima-vs-sharp-minima hypothesis and targets the same "stubborn/high-confidence hallucination" problem. Your differentiator must be the forward-only/gradient-free nature of LSP and the perturbation at intermediate residual stream layers (vs. embedding-level perturbation with gradients).

2. **arXiv 2502.03799** ("Noise Injection") already perturbs hidden activations at intermediate layers and measures output effects -- very close mechanically to LSP. You need to clearly differentiate on (a) what you measure (KL divergence of logit distributions specifically), (b) which layers you target (knowledge-critical middle layers vs. generic intermediate layers), and (c) the focus on high-confidence hallucinations.

3. **arXiv 2411.09689** (SHINE) already uses KL divergence of output distributions after perturbation as a hallucination signal. Your differentiation is the perturbation site (residual streams at middle layers vs. input embeddings).

4. **arXiv 2605.05686** (Attractor Geometry) raises a theoretical objection: it argues that output logit gaps are fundamentally blind to high-confidence hallucinations because the frozen LM head cannot distinguish failure states. You may need to address why KL divergence after perturbation overcomes this limitation when static logit confidence does not.

5. The field is very active in 2025-2026 with multiple concurrent perturbation-based hallucination detection methods. The proposal should position itself carefully within this landscape, emphasizing the unique combination of: (a) forward-only / no gradients, (b) targeted perturbation at factual-recall layers in the residual stream, (c) KL divergence as the specific measurement, and (d) explicit focus on high-confidence/stubborn hallucinations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaeff3c6-6b0b-4f91-a802-9678b9632e64",
  "isSidechain": true,
  "agentId": "aa317dd5ea5975184",
  "requestId": "req_011Cb647bSxhWwdbzbTUgPqr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15dac48c-9f2b-4bda-a2c2-30bb33a15d02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3L4wzwN5PwAEKQrY4itpB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2656,
      "cache_read_input_tokens": 26695,
      "output_tokens": 2742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2656
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2742,
          "cache_read_input_tokens": 26695,
          "cache_creation_input_tokens": 2656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2656,
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
