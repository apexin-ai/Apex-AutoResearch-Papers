# Research conversation: Search for concurrent and recent work (2025-2026) on using instruction invariance, paraphrase consistency, or language i

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a732ab29303cd0b0a.jsonl`
- **Structured JSON:** [`5be7f8361496dc66b40c.json`](../../sessions/5b/5be7f8361496dc66b40c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

59 recorded events

### User

_source line 1 · 2026-05-18T18:44:15.403Z_

Search for concurrent and recent work (2025-2026) on using instruction invariance, paraphrase consistency, or language invariance as self-supervision for affordance learning in Vision-Language-Action models (VLAs). I need to confirm no one is doing the same thing.

Perform these searches:
1. WebSearch: "instruction invariance affordance self-supervised VLA 2026"
2. WebSearch: "paraphrase consistency affordance grounding robot 2026"
3. WebSearch: "self-supervised affordance learning language invariance 2025 2026"
4. WebSearch: "arxiv affordance VLA self-supervised 2026"
5. WebSearch: "instruction paraphrase invariance robot manipulation affordance"
6. WebSearch: "openreview affordance VLA self-supervised 2026 ICML NeurIPS"
7. WebSearch: "language grounding consistency loss affordance robot learning"

For each search, report:
- The exact papers found (title, venue, date, arXiv ID if available)
- Whether any paper uses instruction paraphrase invariance as self-supervision for affordance learning
- How similar each found paper is to the proposed idea

Be thorough — this is critical for novelty verification. Report all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "23eba695-0d48-4260-8d71-721799e6518e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T18:44:15.407Z_

```json
{
  "parentUuid": "23eba695-0d48-4260-8d71-721799e6518e",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
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
  "uuid": "a29fa47b-2a4e-46e1-8961-861446a9c024",
  "timestamp": "2026-05-18T18:44:15.407Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T18:44:17.735Z_



I'll load the WebSearch tool first, then run all searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a29fa47b-2a4e-46e1-8961-861446a9c024",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXc2hh2QKptkxVrN6kQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6aa8b300-4c9b-4698-9995-015461f0e30b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGUBZ9KgsQkeibpStdBi2V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8119,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8119,
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

_source line 4 · 2026-05-18T18:44:18.028Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QBjvsz2mcw5ba71uCfCbnB`</summary>

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
  "parentUuid": "6aa8b300-4c9b-4698-9995-015461f0e30b",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXc2hh2QKptkxVrN6kQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3013d7cc-ca06-4781-9ec5-30faff6a4e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGUBZ9KgsQkeibpStdBi2V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8119,
      "cache_read_input_tokens": 0,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8119
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8119,
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

_source line 5 · 2026-05-18T18:44:18.032Z_

<details><summary>↩ Tool result · `toolu_01QBjvsz2mcw5ba71uCfCbnB`</summary>

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
  "parentUuid": "3013d7cc-ca06-4781-9ec5-30faff6a4e0e",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "2be3ba34-6c75-4430-b1fd-c65e2c5bf15d",
  "sourceToolAssistantUUID": "3013d7cc-ca06-4781-9ec5-30faff6a4e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T18:44:21.928Z_



Now I'll run all 7 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2be3ba34-6c75-4430-b1fd-c65e2c5bf15d",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXcF3LkdtSh8wn86eMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bdf5488-f63b-4060-8b33-731b4181476d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ffbcv4sbQg9ZJAsh5b5YPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 8119,
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

_source line 7 · 2026-05-18T18:44:22.879Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019qEW2bV6U5XPT4d4gHNPhw`</summary>

```json
{
  "query": "instruction invariance affordance self-supervised VLA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bdf5488-f63b-4060-8b33-731b4181476d",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXcF3LkdtSh8wn86eMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8413df0b-efcf-4519-a6be-9eb31881153f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ffbcv4sbQg9ZJAsh5b5YPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 8119,
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

_source line 8 · 2026-05-18T18:44:23.351Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GvC2i4GnDFyNHDvBfqrsNC`</summary>

```json
{
  "query": "paraphrase consistency affordance grounding robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8413df0b-efcf-4519-a6be-9eb31881153f",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXcF3LkdtSh8wn86eMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b56a057-07ed-4883-a599-7642516881db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ffbcv4sbQg9ZJAsh5b5YPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 8119,
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

_source line 9 · 2026-05-18T18:44:23.825Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WhHrZtQtxRnMpXoSMXJ1ko`</summary>

```json
{
  "query": "self-supervised affordance learning language invariance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b56a057-07ed-4883-a599-7642516881db",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXcF3LkdtSh8wn86eMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0859c3d2-b4e1-42ad-bd0e-830cc730a209",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ffbcv4sbQg9ZJAsh5b5YPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 8119,
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

_source line 10 · 2026-05-18T18:44:24.297Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UNT5SpjRPSSzhwtHPKdhZ9`</summary>

```json
{
  "query": "arxiv affordance VLA self-supervised 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0859c3d2-b4e1-42ad-bd0e-830cc730a209",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXcF3LkdtSh8wn86eMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2145e428-5d43-4709-8e7c-29984671f0cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ffbcv4sbQg9ZJAsh5b5YPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 8119,
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

_source line 11 · 2026-05-18T18:44:24.893Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BNCB8LTBeHX8S8aKizcrYQ`</summary>

```json
{
  "query": "instruction paraphrase invariance robot manipulation affordance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2145e428-5d43-4709-8e7c-29984671f0cd",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXcF3LkdtSh8wn86eMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbfeb75d-19ce-4849-8316-c254b0f7fff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ffbcv4sbQg9ZJAsh5b5YPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 8119,
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

_source line 12 · 2026-05-18T18:44:25.769Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CDUNmRo4NTXWEGnyzuAAKQ`</summary>

```json
{
  "query": "openreview affordance VLA self-supervised 2026 ICML NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbfeb75d-19ce-4849-8316-c254b0f7fff4",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXcF3LkdtSh8wn86eMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "571838b4-c801-4085-b0e3-2b915708fdb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ffbcv4sbQg9ZJAsh5b5YPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 8119,
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

_source line 13 · 2026-05-18T18:44:26.112Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SjQnBaCiP1zktSdLnZfs9L`</summary>

```json
{
  "query": "language grounding consistency loss affordance robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "571838b4-c801-4085-b0e3-2b915708fdb3",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXcF3LkdtSh8wn86eMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db420fa6-fac0-4f46-8a67-444da985f36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ffbcv4sbQg9ZJAsh5b5YPp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 8119,
      "output_tokens": 361,
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
          "output_tokens": 361,
          "cache_read_input_tokens": 8119,
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

_source line 14 · 2026-05-18T18:44:30.163Z_

<details><summary>↩ Tool result · `toolu_01GvC2i4GnDFyNHDvBfqrsNC`</summary>

```text
Web search results for query: "paraphrase consistency affordance grounding robot 2026"

Links: [{"title":"Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | OpenReview","url":"https://openreview.net/forum?id=bdHkMjBJG_w"},{"title":"Towards Helpful Robots: Grounding Language in Robotic Affordances","url":"https://research.google/blog/towards-helpful-robots-grounding-language-in-robotic-affordances/"},{"title":"Enhancing task-oriented robotic grasping via 3D affordance grounding from vision-language models | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02169-0"},{"title":"Empowering Large Language Models on Robotic Manipulation with Affordance   Prompting","url":"https://arxiv.org/pdf/2404.11027"},{"title":"Affordance Equivalences in Robotics: A Formalism","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6002533/"},{"title":"SayCan: Grounding Language in Robotic Affordances","url":"https://say-can.github.io/"},{"title":"Do As I Can, Not As I Say: Grounding Language in Robotic Affordances","url":"https://research.google/pubs/do-as-i-can-not-as-i-say-grounding-language-in-robotic-affordances/"},{"title":"Which objects help me to act effectively? Reasoning about   physically-grounded affordances","url":"https://arxiv.org/pdf/2407.13811"},{"title":"Knowledge enhanced bottom-up affordance grounding for robotic interaction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11232630/"}]

The search results cover several relevant topics in robotic affordance grounding and language grounding:

**Key Research Areas:**

1. **Language Grounding in Robotic Affordances**: A novel approach called PaLM-SayCan leverages advanced language model knowledge to enable physical agents, such as robots, to follow high-level textual instructions while grounding the language model in tasks that are feasible within a specific real-world context.

2. **Affordance Functions**: Affordance functions enable real-world grounding and determine which actions are possible to execute in a given environment.

3. **Recent 2026 Research**: A 2026 study on "Enhancing task-oriented robotic grasping via 3D affordance grounding from vision-language models" proposes a system that generates semantic heatmaps and mask labels to improve grasp prediction.

4. **Knowledge-Enhanced Approaches**: The KBAG-Net framework enhances natural language understanding through external knowledge, improving accuracy in object grasping affordance segmentation.

While the search results don't specifically address "paraphrase consistency" in the title, they do cover the intersection of language grounding, affordances, and robotics from multiple recent publications, including 2026 research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b56a057-07ed-4883-a599-7642516881db",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "0f6595da-9567-47e3-aaf6-6b567c8e917e",
  "sourceToolAssistantUUID": "6b56a057-07ed-4883-a599-7642516881db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T18:44:30.712Z_

<details><summary>↩ Tool result · `toolu_019qEW2bV6U5XPT4d4gHNPhw`</summary>

```text
Web search results for query: "instruction invariance affordance self-supervised VLA 2026"

Links: [{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"},{"title":"Egocentric Instruction-oriented Affordance Prediction via Large Multimodal Model","url":"https://arxiv.org/pdf/2508.17922"},{"title":"Learning Instruction-Guided Manipulation Affordance via Large Models for   Embodied Robotic Tasks","url":"https://arxiv.org/pdf/2408.10658"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.19752"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"},{"title":"Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning","url":"https://arxiv.org/pdf/2602.08167"},{"title":"Affordance Learning from Play for Sample-Efficient Policy Learning","url":"https://arxiv.org/pdf/2203.00352"}]

Based on the search results, I found several relevant papers and research related to your query about instruction invariance, affordance, self-supervised learning, and Vision-Language-Action (VLA) models in 2026:

## Key Findings:

**Instruction-Oriented Affordance Prediction:**
Affordance is argued to be dynamic and closely related to the purpose of interaction, and should be instruction- or task-oriented. A new egocentric instruction-oriented affordance grounding task has been introduced, which requires predicting contact regions and motion directions according to a given manipulation instruction, with a dataset named EIVA (Egocentric Instruction-oriented Visual Affordance).

**Self-Supervised Learning for VLAs:**
A novel approach called Act from Visual Language Post-Training refines Visual Language Models through visual and linguistic guidance in a self-supervised manner. Additionally, R&B-EnCoRe enables models to bootstrap embodied reasoning from internet-scale knowledge through self-supervised refinement, using VLA models' generative probabilities to weigh reasoning strategies based on information benefit.

**Action Invariance for Robustness:**
PAIR-VLA proposes an RL fine-tuning framework with an invariance term that reduces the discrepancy between action distributions for task-preserving pairs and a sensitivity objective that encourages separable action distributions for task-altering pairs.

These represent cutting-edge research in VLA models focusing on making them more robust and adaptable through instruction understanding, affordance prediction, and self-supervised learning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8413df0b-efcf-4519-a6be-9eb31881153f",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "63536905-15a8-4f9b-bc72-8be51020ae6f",
  "sourceToolAssistantUUID": "8413df0b-efcf-4519-a6be-9eb31881153f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T18:44:31.844Z_

<details><summary>↩ Tool result · `toolu_01WhHrZtQtxRnMpXoSMXJ1ko`</summary>

```text
Web search results for query: "self-supervised affordance learning language invariance 2025 2026"

Links: [{"title":"GitHub - HCPLab-SYSU/Embodied_AI_Paper_List: [Embodied-AI-Survey-2025] Paper List and Resource Repository for Embodied AI · GitHub","url":"https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List"},{"title":"(PDF) Idiographic self-regulated affordance uptake in AI-mediated language learning","url":"https://www.researchgate.net/publication/397176147_Idiographic_self-regulated_affordance_uptake_in_AI-mediated_language_learning"},{"title":"Weakly-Supervised Affordance Grounding Guided by Part-Level Semantic Priors | OpenReview","url":"https://openreview.net/forum?id=0823rvTIhs"},{"title":"WEAKLY-SUPERVISED AFFORDANCE GROUNDING ...","url":"https://openreview.net/pdf/2551c99500000f40bd07dc3c4c3d1111d11b9c1a.pdf"},{"title":"Affordance embeddings for situated language understanding","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9538673/"},{"title":"Grounding Language with Visual Affordances over Unstructured Data","url":"https://arxiv.org/pdf/2210.01911"},{"title":"Weakly Supervised Learning of Affordances","url":"https://arxiv.org/pdf/1605.02964"}]

Based on the search results, here's what I found regarding self-supervised affordance learning and language invariance in 2025-2026:

## Recent Research

Recent work includes "Learning 2D Invariant Affordance Knowledge for 3D Affordance Grounding" (arxiv, 2024) by Xianqiang Gao et al., which addresses invariant affordance knowledge. Additionally, "DSPNet: Dual-vision Scene Perception for Robust 3D Question Answering" was published at CVPR 2025.

## Self-Supervised and Language-Conditioned Approaches

The research landscape includes work on self-supervised affordance learning combined with language understanding. One approach extracts a self-supervised visual affordance model and extends it to learn language-conditioned affordances, enabling robots to follow manipulation tasks directly from images.

## Weakly-Supervised Methods

Recent work proposes a pipeline to generate affordance heatmaps using off-the-shelf visual foundation models and introduces the first pseudo-supervised training framework for weakly-supervised affordance grounding.

## Language Learning Context

Recent work on AI-mediated language learning discusses how affordances are not static features but emergent relations, and suggests that effective pedagogy requires preparing learners to notice and creatively combine affordances.

The field appears to be actively developing methods that combine self-supervised learning, visual affordance understanding, and language grounding, with recent publications throughout 2024-2025 advancing these approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0859c3d2-b4e1-42ad-bd0e-830cc730a209",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "7d2165e3-7af3-4464-abd6-38dcac2d0c44",
  "sourceToolAssistantUUID": "0859c3d2-b4e1-42ad-bd0e-830cc730a209",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T18:44:33.459Z_

<details><summary>↩ Tool result · `toolu_01SjQnBaCiP1zktSdLnZfs9L`</summary>

```text
Web search results for query: "language grounding consistency loss affordance robot learning"

Links: [{"title":"Towards Helpful Robots: Grounding Language in Robotic Affordances","url":"https://research.google/blog/towards-helpful-robots-grounding-language-in-robotic-affordances/"},{"title":"[PDF] Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Do-As-I-Can,-Not-As-I-Say:-Grounding-Language-in-Ahn-Brohan/cb5e3f085caefd1f3d5e08637ab55d39e61234fc"},{"title":"Do As I Can, Not As I Say: Grounding Language in Robotic Affordances","url":"https://proceedings.mlr.press/v205/ichter23a.html"},{"title":"Grounding Language with Visual Affordances over Unstructured Data","url":"https://arxiv.org/pdf/2210.01911"},{"title":"Knowledge enhanced bottom-up affordance grounding for robotic interaction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11232630/"},{"title":"[Robotics] Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | by Ming-Hao Hsu | Medium","url":"https://medium.com/@amiable_cardinal_crocodile_398/robotics-do-as-i-can-not-as-i-say-grounding-language-in-robotic-affordances-e6d1b74035fd"},{"title":"SayCan: Grounding Language in Robotic Affordances","url":"https://say-can.github.io/"}]

Based on the search results, here's what I found about language grounding, consistency loss, affordance, and robot learning:

## Key Research and Approaches

A notable approach called "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances" leverages advanced language model knowledge to enable physical agents like robots to follow high-level textual instructions for physically-grounded tasks, while grounding the language model in tasks that are feasible within a specific real-world context.

## Core Methodology

The approach provides real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are both feasible and contextually appropriate. If each skill has an accompanying affordance function that quantifies how likely it is to succeed from the current state (such as a learned value function), its value can be used to weight the skill's likelihood.

## Learning from Unstructured Data

A novel approach efficiently learns general-purpose language-conditioned robot skills from unstructured, offline and reset-free data in the real world by exploiting a self-supervised visuo-lingual affordance model, which requires annotating as little as 1% of the total data with language.

## Affordance Grounding

Knowledge enhanced bottom-up affordance grounding networks enhance natural language understanding through external knowledge, improving accuracy in object grasping affordance segmentation.

These approaches address the core challenge of bridging the gap between language models and robotic systems through affordance-based grounding mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db420fa6-fac0-4f46-8a67-444da985f36b",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "32442692-1ff2-4057-8fbb-d8220e73199b",
  "sourceToolAssistantUUID": "db420fa6-fac0-4f46-8a67-444da985f36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T18:44:35.146Z_

<details><summary>↩ Tool result · `toolu_01CDUNmRo4NTXWEGnyzuAAKQ`</summary>

```text
Web search results for query: "openreview affordance VLA self-supervised 2026 ICML NeurIPS"

Links: [{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"OpenReviewer: A Specialized Large Language Model for Generating Critical   Scientific Paper Reviews","url":"https://arxiv.org/pdf/2412.11948"},{"title":"GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.","url":"https://github.com/keon/awesome-physical-ai"},{"title":"Venues | OpenReview","url":"https://openreview.net/"}]

The search results show several relevant papers related to vision-language-action (VLA) models and affordances from OpenReview and related venues. Here's what I found:

1. **Self-Improving VLA Models**: One paper on OpenReview demonstrates a method achieving 99% task success on the LIBERO benchmark and offering "a scalable path toward self-improving VLA models" through RL-generated data.

2. **Affordance Field Intervention for VLAs**: Another paper demonstrates an affordance-based method achieving 23.5% average improvement across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms.

3. **Recent VLA Research**: Multiple 2025-2026 papers on VLA and affordance-related topics have been published, including works on affordance distillation and vision-language reward models for robotics.

4. **ICLR 2026 Submissions**: There are ICLR 2026 submissions including FASTer and OmniSAT, which focus on improved action tokenization and autoregression for vision-language-action models.

The search results cover VLAs, affordances, and self-supervised learning approaches being submitted to or published on OpenReview and major venues like ICLR, though the results don't specifically isolate papers matching all the exact keywords in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "571838b4-c801-4085-b0e3-2b915708fdb3",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "b607504a-ab46-4ec2-872e-621b31207969",
  "sourceToolAssistantUUID": "571838b4-c801-4085-b0e3-2b915708fdb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T18:44:36.089Z_

<details><summary>↩ Tool result · `toolu_01UNT5SpjRPSSzhwtHPKdhZ9`</summary>

```text
Web search results for query: "arxiv affordance VLA self-supervised 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.10109"},{"title":"Affordance-Graphed Task Worlds: Self-Evolving Task Generation for Scalable","url":"https://arxiv.org/pdf/2602.12065"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving","url":"https://arxiv.org/pdf/2510.12796"},{"title":"Self-Supervised Learning of Action Affordances as Interaction Modes","url":"https://arxiv.org/pdf/2305.17565"}]

I found several relevant papers on arXiv related to affordances, VLAs (Vision-Language-Action models), and self-supervised learning from 2026 and recent years. Here are the key results:

1. **Spatial-Aware VLA for Robotic Control** (ICLR 2026): By reformatting all robotic data into a unified QA structure consistent with web-scale pre-training, they enable the VLM to develop a spatially-aware representation space under a standard supervised fine-tuning framework, with applications to affordance recognition.

2. **Affordance-Graphed Task Worlds** (February 2026): This work adopts affordance-graphed task generation, which enables planning and execution of action sequences in arbitrary scenes, and introduces VLM-supervised self-evolution to iteratively correct task actions.

3. **Affordance Field Intervention for VLAs**: This method identifies memory traps through proprioception, repositions the robot to recent high-affordance regions, and proposes affordance-driven waypoints that anchor VLA-generated actions, with a SAF-based scorer selecting trajectories with the highest cumulative affordance.

4. **CoA-VLA (Chain-of-Affordance)**: This proposes Chain-of-Affordance, a novel perspective on generalizing model reasoning at test-time and leverages such generated reasoning to facilitate the policy learning process.

5. **DriveVLA-W0**: This training paradigm employs world modeling to predict future images, generating a dense, self-supervised signal, with instantiations for both autoregressive and diffusion world models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2145e428-5d43-4709-8e7c-29984671f0cd",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "ab35ce50-089a-438b-807d-05a9b86d9970",
  "sourceToolAssistantUUID": "2145e428-5d43-4709-8e7c-29984671f0cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T18:44:46.103Z_

<details><summary>↩ Tool result · `toolu_01BNCB8LTBeHX8S8aKizcrYQ`</summary>

```text
Web search results for query: "instruction paraphrase invariance robot manipulation affordance"

Links: [{"title":"EqvAfford: SE(3) Equivariance for Point-Level Affordance Learning","url":"https://arxiv.org/pdf/2408.01953"},{"title":"Affordance-Centric Policy Learning: Sample Efficient and Generalisable Robot Policy Learning using Affordance-Centric Task Frames","url":"https://arxiv.org/html/2410.12124v1"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://www.researchgate.net/publication/395222047_RT-Affordance_Affordances_are_Versatile_Intermediate_Representations_for_Robot_Manipulation"},{"title":"Learning Instruction-Guided Manipulation Affordance via Large Models for   Embodied Robotic Tasks","url":"https://arxiv.org/pdf/2408.10658"},{"title":"Egocentric Instruction-oriented Affordance Prediction via Large Multimodal Model","url":"https://arxiv.org/pdf/2508.17922"},{"title":"RT-Affordance: Reasoning about Robotic Manipulation with Affordances","url":"https://openreview.net/pdf?id=s8VMLXKH1X"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/html/2409.01083v4"}]

Based on the search results, here's what I found about instruction paraphrase invariance in robot manipulation affordance:

## Key Findings

Affordance should be task-/instruction-dependent, as different instructions can lead to different manipulation regions and directions even for the same object. This highlights an important distinction: affordance is not static but varies based on how a task is specified.

In previous studies, the predicted manipulation regions typically do not change with language instructions, whereas in human behavioral patterns, the manipulation regions of the same object will change for different language instructions.

## Recent Research Approaches

Several recent works address instruction-guided affordance learning:

1. **Instruction-Guided Affordance Net (IGANet)**: IGANet predicts affordance maps of instruction-guided robotic manipulation tasks by utilizing powerful priors from vision and language encoders pre-trained on large-scale datasets.

2. **Large Multimodal Models for Affordance**: Large multimodal models (LMMs) can serve as affordance predictors through a "search against verifiers" pipeline, where an LMM progressively predicts affordances with outputs verified iteratively.

3. **Affordance-Centric Policy Learning**: Affordance-centric approaches can achieve both intra-category invariance—where policies generalize across different instances within the same object category—and spatial invariance.

These approaches represent the field's growing recognition that instruction paraphrase invariance is crucial for building robots that can understand semantic variations in task instructions while generating appropriate manipulation affordances.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbfeb75d-19ce-4849-8316-c254b0f7fff4",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "5799720b-6819-4414-9da7-a51299aa311c",
  "sourceToolAssistantUUID": "bbfeb75d-19ce-4849-8316-c254b0f7fff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-18T18:44:49.454Z_

Let me run additional targeted searches to dig deeper into the most relevant threads, particularly PAIR-VLA, CoA-VLA, RT-Affordance, and any work specifically on paraphrase-based self-supervision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5799720b-6819-4414-9da7-a51299aa311c",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXeHu3dLcwpWsSBCutq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76b7fd47-1ab1-4bc9-80a8-aeec2219a392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3fQugbnXMGtAWutLVBau5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1630,
      "cache_creation_input_tokens": 4092,
      "cache_read_input_tokens": 9529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4092,
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

_source line 22 · 2026-05-18T18:44:50.003Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HbWC4cc9L8hkqPT2TUzjbh`</summary>

```json
{
  "query": "PAIR-VLA instruction invariance action distribution robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76b7fd47-1ab1-4bc9-80a8-aeec2219a392",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXeHu3dLcwpWsSBCutq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd67a74f-b025-48d5-9750-bd7c8e28c63e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3fQugbnXMGtAWutLVBau5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1630,
      "cache_creation_input_tokens": 4092,
      "cache_read_input_tokens": 9529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4092,
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

_source line 23 · 2026-05-18T18:44:50.942Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LpPbqETXWHUiis2Nsx2s7T`</summary>

```json
{
  "query": "CoA-VLA chain of affordance visual textual reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd67a74f-b025-48d5-9750-bd7c8e28c63e",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXeHu3dLcwpWsSBCutq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab16f353-eebc-484d-9037-9ae7a5c22f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3fQugbnXMGtAWutLVBau5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1630,
      "cache_creation_input_tokens": 4092,
      "cache_read_input_tokens": 9529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4092,
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

_source line 24 · 2026-05-18T18:44:51.481Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X3XBKG4rZNRGc9mnjPMbca`</summary>

```json
{
  "query": "RT-Affordance intermediate representation robot manipulation Google 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab16f353-eebc-484d-9037-9ae7a5c22f7c",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXeHu3dLcwpWsSBCutq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de97bd91-b54b-412f-b991-2e51a2bf99af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3fQugbnXMGtAWutLVBau5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1630,
      "cache_creation_input_tokens": 4092,
      "cache_read_input_tokens": 9529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4092,
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

_source line 25 · 2026-05-18T18:44:52.033Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FirXYT1zMXd5eer9SBEcwD`</summary>

```json
{
  "query": "\"instruction invariance\" OR \"paraphrase invariance\" robot policy learning self-supervision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de97bd91-b54b-412f-b991-2e51a2bf99af",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXeHu3dLcwpWsSBCutq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1502cddd-4636-4958-959c-bb94828bdc3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3fQugbnXMGtAWutLVBau5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1630,
      "cache_creation_input_tokens": 4092,
      "cache_read_input_tokens": 9529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4092,
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

_source line 26 · 2026-05-18T18:44:52.653Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014ufKJ9PDA5tP5vQB7wPNyX`</summary>

```json
{
  "query": "affordance prediction consistency regularization language conditioned manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1502cddd-4636-4958-959c-bb94828bdc3f",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXeHu3dLcwpWsSBCutq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "224c74d9-e114-4f59-9aa8-f1f59ef7ffb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3fQugbnXMGtAWutLVBau5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1630,
      "cache_creation_input_tokens": 4092,
      "cache_read_input_tokens": 9529,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4092
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1630,
          "output_tokens": 319,
          "cache_read_input_tokens": 9529,
          "cache_creation_input_tokens": 4092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4092,
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

_source line 27 · 2026-05-18T18:44:57.268Z_

<details><summary>↩ Tool result · `toolu_01HbWC4cc9L8hkqPT2TUzjbh`</summary>

```text
Web search results for query: "PAIR-VLA instruction invariance action distribution robustness 2025 2026"

Links: [{"title":"[2502.18975] Invariance Pair-Guided Learning: Enhancing Robustness in Neural Networks","url":"https://arxiv.org/abs/2502.18975"},{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/pdf/2512.01715"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://arxiv.org/pdf/2601.15197"},{"title":"PI-VLA: A Symmetry-Aware Predictive and Interactive Vision--Language--Action Framework for Robust Robotic Manipulation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202601.0682"},{"title":"Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2602.20200"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/pdf/2510.00037"}]

Based on the search results, I found several relevant papers related to Vision-Language-Action (VLA) models and robustness in 2025-2026, though no paper specifically titled "PAIR-VLA" appears in these results. Here's what I found:

**Related VLA Robustness Research (2025-2026):**

1. **DiG-Flow** - DiG-Flow computes a discrepancy measure between empirical distributions of observation and action embeddings, maps it to a modulation weight via a monotone function, and applies residual updates to the observation embeddings before flow matching. Recent studies reveal concerning fragility: performance degrades substantially under modest distribution shifts such as lighting changes, texture variations, or camera angle perturbations.

2. **RobustVLA** - For input robustness, it enforces consistent actions across input variations that preserve task semantics.

3. **PI-VLA** - This model jointly generates discrete and continuous action chunks with predictive world-model features, enforcing cross-modal action consistency as an implicit symmetry constraint, while encouraging invariance to task-relevant transformations.

4. **LangForce** - Current VLA models still face challenges in generalizing to novel instructions or complex multi-task scenarios, particularly in out-of-distribution (OOD) environments.

The search results show active research on instruction-following robustness and action distribution challenges in VLA models, though the specific "PAIR-VLA" framework wasn't found in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd67a74f-b025-48d5-9750-bd7c8e28c63e",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "a35c7d92-c5ae-4d97-a9cd-5205c00b2766",
  "sourceToolAssistantUUID": "cd67a74f-b025-48d5-9750-bd7c8e28c63e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T18:44:58.473Z_

<details><summary>↩ Tool result · `toolu_01X3XBKG4rZNRGc9mnjPMbca`</summary>

```text
Web search results for query: "RT-Affordance intermediate representation robot manipulation Google 2025"

Links: [{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation – UT Austin Robot Perception and Learning Lab","url":"https://rpl.cs.utexas.edu/publications/2025/05/19/nasiriany-icra25-rta/"},{"title":"[2411.02704] RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/abs/2411.02704"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://www.researchgate.net/publication/385560182_RT-Affordance_Affordances_are_Versatile_Intermediate_Representations_for_Robot_Manipulation"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/html/2411.02704v1"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot","url":"https://openreview.net/pdf?id=y4KugwU0qU"},{"title":"RT-Affordance: A New Approach by Google DeepMind to Robust Robot Manipulation with Versatile Policy Representations – AI Toolhouse Blog","url":"https://blog.aitoolhouse.com/rt-affordance-a-new-approach-by-google-deepmind-to-robust-robot-manipulation-with-versatile-policy-representations/"},{"title":"Google DeepMind Researchers Propose RT-Affordance: A Hierarchical Method that Uses Affordances as an Intermediate Representation for Policies - MarkTechPost","url":"https://www.marktechpost.com/2024/11/08/google-deepmind-researchers-propose-rt-affordance-a-hierarchical-method-that-uses-affordances-as-an-intermediate-representation-for-policies/"}]

Based on the search results, here's what I found about RT-Affordance:

## Overview

RT-Affordance explores how intermediate policy representations can facilitate generalization by providing guidance on how to perform manipulation tasks. The hierarchical model first creates an affordance plan given the task language, and then uses the policy on this affordance plan to guide the robot's actions for manipulation.

## Key Innovation

The method conditions policies on affordances, which capture the pose of the robot at key stages of the task, offering expressive yet lightweight abstractions that are easy for users to specify and facilitate efficient learning by transferring knowledge from large internet datasets.

## How It Works

The hierarchical model first predicts the affordance plan given the task language and initial image of the task, overlaying the affordance onto the image, and subsequently conditioning the policy on images overlaid with the affordance plan.

## Training Approach

The model can flexibly bridge heterogeneous sources of supervision including large web datasets and robot trajectories, and can be trained on cheap-to-collect in-domain affordance images, allowing it to learn new tasks without collecting additional costly robot trajectories.

## Performance

RT-Affordance exceeds the performance of existing methods by over 50% on a diverse set of novel tasks, and affordances are robust to novel settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de97bd91-b54b-412f-b991-2e51a2bf99af",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "3b08a53b-13ae-4af6-8ffd-ab1e2fa95648",
  "sourceToolAssistantUUID": "de97bd91-b54b-412f-b991-2e51a2bf99af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T18:44:59.482Z_

<details><summary>↩ Tool result · `toolu_01FirXYT1zMXd5eer9SBEcwD`</summary>

```text
Web search results for query: ""instruction invariance" OR "paraphrase invariance" robot policy learning self-supervision"

Links: [{"title":"TransMASK: Masked State Representation through Learned Transformation","url":"https://arxiv.org/pdf/2603.05670"},{"title":"Published as a conference paper at ICLR 2021 SELF-SUPERVISED POLICY ADAPTATION","url":"https://arxiv.org/pdf/2007.04309"},{"title":"Published at 2nd Conference on Lifelong Learning Agents (CoLLAs), 2023","url":"https://arxiv.org/pdf/2306.08537"},{"title":"Domain adaptation for robotic control using self-supervised learning","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12353993"},{"title":"Salience-Invariant Consistent Policy Learning for Generalization","url":"https://arxiv.org/pdf/2502.08336"},{"title":"MILES: Making Imitation Learning Easy with Self-Supervision","url":"https://arxiv.org/pdf/2410.19693"},{"title":"Invariance Co-training for Robot Visual Generalization","url":"https://arxiv.org/pdf/2512.05230"}]

I found several relevant research papers on instruction/paraphrase invariance and robot policy learning with self-supervision:

## Key Research Areas

**Invariance in Robot Learning:**

Learning invariance improves generalization by making robots ignore irrelevant state components, and self-supervised methods can learn masks to transform observed states into latent representations biased towards relevant elements.

Robot policies need to reason from diverse observations to operate across environments, though many remain sensitive to observational variations like camera perspective, lighting, and distractor objects.

**Self-Supervised Approaches:**

Self-supervised and RL objectives can be jointly optimized during training, with policy adaptation during deployment using observations collected from the test environment online, allowing policies to adapt to new environments with naturally revealed observational data.

For learning state-goal invariances, key capabilities include mapping varied observation configurations to the same underlying state and distinguishing whether observation changes were induced by state changes or state-invariant perturbations, using contrastive learning frameworks that encourage invariant embeddings.

The search results show active research in this area, particularly around learning visual invariances, adaptation to domain shifts, and self-supervised representation learning for robotic control tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1502cddd-4636-4958-959c-bb94828bdc3f",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "90cb8830-bfc4-46da-a246-e79fc4749e96",
  "sourceToolAssistantUUID": "1502cddd-4636-4958-959c-bb94828bdc3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T18:45:08.206Z_

<details><summary>↩ Tool result · `toolu_01LpPbqETXWHUiis2Nsx2s7T`</summary>

```text
Web search results for query: "CoA-VLA chain of affordance visual textual reasoning 2025"

Links: [{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"},{"title":"ICCV Poster CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance","url":"https://iccv.thecvf.com/virtual/2025/poster/542"},{"title":"Add CoA-VLA (Chain-of-Affordance) · Issue #5 · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/issues/5"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"[PDF] CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoT-VLA:-Visual-Chain-of-Thought-Reasoning-for-Zhao-Lu/2d7f3a99e916fc80ff890d109699f9682253e66d"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/394511717_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models"},{"title":"[PDF] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoA-VLA:-Improving-Vision-Language-Action-Models-Li-Zhu/5760cc722b5eabc14487e9c497a78038ab46f37d"}]

Based on the search results, here's what I found about CoA-VLA:

## Overview

CoA-VLA (Chain-of-Affordance) is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion. The paper was presented at ICCV 2025.

## Key Components

The method prompts the model to consider four types of affordances before taking action: (1) object affordance — what object to manipulate and where it is; (2) grasp affordance — the specific object part to grasp; (3) spatial affordance — the optimal space to place the object; and (4) movement affordance — the collision-free path for movement.

Each affordance has visual and textual formats, injected via a novel vision-language co-injection module. This allows the robot to leverage essential contextual information during action inference, resulting in improved precision and robustness.

## Performance

CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks. Furthermore, CoA-VLA exhibits strong generalization capabilities to handle unseen object poses, adjust motion when obstacles appear, and identify free space for placement.

The paper's arXiv identifier is 2412.20451.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab16f353-eebc-484d-9037-9ae7a5c22f7c",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "5421eec6-abea-4048-a08f-9e7b040f5235",
  "sourceToolAssistantUUID": "ab16f353-eebc-484d-9037-9ae7a5c22f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T18:45:11.760Z_

<details><summary>↩ Tool result · `toolu_014ufKJ9PDA5tP5vQB7wPNyX`</summary>

```text
Web search results for query: "affordance prediction consistency regularization language conditioned manipulation 2025 2026"

Links: [{"title":"Empowering Large Language Models on Robotic Manipulation with Affordance   Prompting","url":"https://arxiv.org/pdf/2404.11027"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"Reasoning Mamba: Hypergraph-Guided Region Relation Calculating for Weakly Supervised Affordance Grounding | Request PDF","url":"https://www.researchgate.net/publication/394663626_Reasoning_Mamba_Hypergraph-Guided_Region_Relation_Calculating_for_Weakly_Supervised_Affordance_Grounding"},{"title":"Learning Instruction-Guided Manipulation Affordance via Large Models for   Embodied Robotic Tasks","url":"https://arxiv.org/pdf/2408.10658"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

I found relevant research on affordance prediction for language-conditioned robotic manipulation. Here are the key findings:

## Recent Work in Affordance-Based Language-Conditioned Manipulation

RT-Affordance is a policy conditioned on both language specifications and visual affordances, where the visual affordances show the pose of the robot end effector at key stages of the task, visually projected onto the image input of the policy. This approach achieves 69% overall success rate compared to 15% success rate for language-conditioned policies.

Another framework called LLM+A uses the LLM as both a sub-task planner and motion controller, with an affordance prompting technique that stimulates the LLM to predict the consequences of generated plans and generate affordance values for relevant objects.

Recent progress in large language models and multi-modal models makes it easier to incorporate language instructions for manipulation affordance prediction, with methods like CLIPORT integrating semantic understanding of CLIP and spatial precision together into a convolutional architecture to predict manipulation affordance based on language instructions.

The search results also show that as of 2025-2026, there are multiple recent papers on vision-language-action models for robotic manipulation, including approaches focused on affordance distillation and 3D affordance detection.

However, the search results do not contain specific papers explicitly focused on "consistency regularization" combined with affordance prediction. If you're looking for work specifically on consistency regularization techniques in this domain, that may be a more specialized area that warrants a more targeted search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "224c74d9-e114-4f59-9aa8-f1f59ef7ffb2",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "f220d605-e098-4780-ad3d-55a12d9e8bb1",
  "sourceToolAssistantUUID": "224c74d9-e114-4f59-9aa8-f1f59ef7ffb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-18T18:45:15.660Z_

Let me do a few more targeted searches to cover the most critical angles -- specifically RobustVLA, and any work using paraphrases for representation learning in robotics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f220d605-e098-4780-ad3d-55a12d9e8bb1",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXgBd5B41LVJ6UpvHyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f834cde5-9b5a-4c50-8252-6d828516ee1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MGecnBAXkjkUrgsK3yNEUZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5910,
      "cache_read_input_tokens": 13621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5910,
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

_source line 33 · 2026-05-18T18:45:16.607Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L1XzbcdNBwP2k5DweNqpBA`</summary>

```json
{
  "query": "RobustVLA consistent actions input variations task semantics arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f834cde5-9b5a-4c50-8252-6d828516ee1d",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXgBd5B41LVJ6UpvHyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "900240cc-f6a1-4fd2-b4af-fa579a29a170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MGecnBAXkjkUrgsK3yNEUZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5910,
      "cache_read_input_tokens": 13621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5910,
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

_source line 34 · 2026-05-18T18:45:17.550Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011966R3UFsiGpcVkqZmD8UA`</summary>

```json
{
  "query": "\"language augmentation\" OR \"instruction augmentation\" affordance map consistency robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "900240cc-f6a1-4fd2-b4af-fa579a29a170",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXgBd5B41LVJ6UpvHyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74ed0edd-d532-41f9-8a10-fb9b44a0767e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MGecnBAXkjkUrgsK3yNEUZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5910,
      "cache_read_input_tokens": 13621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5910,
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

_source line 35 · 2026-05-18T18:45:18.021Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qq5fLNbBkNJoU3Ji8Y8re4`</summary>

```json
{
  "query": "paraphrase augmentation vision language action model robotic policy generalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74ed0edd-d532-41f9-8a10-fb9b44a0767e",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXgBd5B41LVJ6UpvHyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4ad56c7-1c3c-4c2c-a179-b9c10c1746a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MGecnBAXkjkUrgsK3yNEUZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5910,
      "cache_read_input_tokens": 13621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5910,
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

_source line 36 · 2026-05-18T18:45:18.367Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NxWQgxgcHFNycGbPKSSQNg`</summary>

```json
{
  "query": "IGANet instruction guided affordance manipulation 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4ad56c7-1c3c-4c2c-a179-b9c10c1746a2",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXgBd5B41LVJ6UpvHyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3b90325-dca0-4ceb-8ceb-59fcb83f6832",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MGecnBAXkjkUrgsK3yNEUZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5910,
      "cache_read_input_tokens": 13621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5910,
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

### Tool result

_source line 37 · 2026-05-18T18:45:21.779Z_

<details><summary>↩ Tool result · `toolu_01L1XzbcdNBwP2k5DweNqpBA`</summary>

```text
Web search results for query: "RobustVLA consistent actions input variations task semantics arxiv 2025"

Links: [{"title":"[2510.00037v4] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037v4"},{"title":"[2510.00037] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/pdf/2510.00037"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/html/2510.00037"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.01331"}]

Based on the search results, I found the paper you're looking for:

RobustVLA is proposed against perturbations in VLA inputs and outputs. Specifically, for input robustness, consistent actions are enforced across input variations that preserve task semantics.

The paper is titled "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations" (arXiv:2510.00037). The authors evaluate the robustness of mainstream VLAs under 17 perturbations across four modalities, and their RobustVLA delivers absolute gains over baselines of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "900240cc-f6a1-4fd2-b4af-fa579a29a170",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "4cfc7fff-c1ef-46d2-a0ee-82d330ea6e52",
  "sourceToolAssistantUUID": "900240cc-f6a1-4fd2-b4af-fa579a29a170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T18:45:24.499Z_

<details><summary>↩ Tool result · `toolu_011966R3UFsiGpcVkqZmD8UA`</summary>

```text
Web search results for query: ""language augmentation" OR "instruction augmentation" affordance map consistency robot learning"

Links: [{"title":"Semantically Controllable Augmentations for Generalizable Robot Learning","url":"https://arxiv.org/html/2409.00951v1/"},{"title":"Learning Instruction-Guided Manipulation Affordance via Large Models for   Embodied Robotic Tasks","url":"https://arxiv.org/pdf/2408.10658"},{"title":"Learning Instruction-Guided Manipulation Affordance via Large Models for Embodied Robotic Tasks","url":"https://arxiv.org/html/2408.10658v1"},{"title":"Object-Centric Instruction Augmentation for Robotic Manipulation","url":"https://arxiv.org/html/2401.02814v2"},{"title":"Robotic Skill Acquisition via Instruction Augmentation with   Vision-Language Models","url":"https://arxiv.org/pdf/2211.11736"},{"title":"General Flow as Foundation Affordance for Scalable Robot Learning","url":"https://arxiv.org/html/2401.11439v2"},{"title":"Object-Centric Instruction Augmentation for Robotic Manipulation","url":"https://arxiv.org/pdf/2401.02814"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/html/2409.01083v4"}]

Based on the search results, here's what I found related to language/instruction augmentation, affordance maps, and robot learning:

## Key Research Areas

Several recent papers address the intersection of language augmentation, instruction augmentation, and affordance map consistency in robot learning:

**Instruction-Guided Affordance Prediction:**
IGANet (Instruction-Guided Affordance Net) predicts affordance maps of instruction-guided robotic manipulation tasks by utilizing powerful priors from vision and language encoders pre-trained on large-scale datasets. The approach develops a Vision-Language-Models (VLMs)-based data augmentation pipeline, which can generate a large amount of data automatically for model training.

**Object-Centric Augmentation:**
Recent work uses Multimodal Large Language Models (MLLM) to augment language instruction with object-centric information, informing the robot with visual information via transferred language instruction that allows inference of high-level features around affordances and intents.

**Affordance-Based Manipulation:**
A framework extracts instruction-relevant manipulation affordances from the same visual scene with different language instructions using a prompt tuning method with a frozen vision foundation model, and then uses a flow matching policy to transform random waypoints to desired action trajectories guided by task-relevant affordance maps.

**Skill Acquisition via Augmentation:**
One approach implements instruction augmentation with CLIP on real-world robotic manipulation with 80,000 teleoperated demonstrations and 5,600 crowd-sourced instruction labels, with evaluation across 1,300+ real world robot evaluations.

These papers collectively address how to maintain consistency between language instructions and affordance predictions in robot learning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74ed0edd-d532-41f9-8a10-fb9b44a0767e",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "907f9103-fc4f-436d-9cd5-1fa44cb06a66",
  "sourceToolAssistantUUID": "74ed0edd-d532-41f9-8a10-fb9b44a0767e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T18:45:30.261Z_

<details><summary>↩ Tool result · `toolu_01NxWQgxgcHFNycGbPKSSQNg`</summary>

```text
Web search results for query: "IGANet instruction guided affordance manipulation 2024 arxiv"

Links: [{"title":"Learning Instruction-Guided Manipulation Affordance via Large Models for Embodied Robotic Tasks","url":"https://arxiv.org/html/2408.10658v1"},{"title":"Learning Instruction-Guided Manipulation Affordance via Large Models for Embodied Robotic Tasks | Request PDF","url":"https://www.researchgate.net/publication/383266785_Learning_Instruction-Guided_Manipulation_Affordance_via_Large_Models_for_Embodied_Robotic_Tasks"},{"title":"Learning Instruction-Guided Manipulation Affordance via Large Models for   Embodied Robotic Tasks","url":"https://arxiv.org/pdf/2408.10658"},{"title":"Egocentric Instruction-oriented Affordance Prediction via Large Multimodal Model","url":"https://arxiv.org/html/2508.17922v1"},{"title":"Egocentric Instruction-oriented Affordance Prediction via Large Multimodal Model","url":"https://arxiv.org/pdf/2508.17922"}]

I found the paper you're looking for! Here's the information:

IGANet (Instruction-Guided Affordance Net) is a novel method for learning instruction-guided manipulation affordance by utilizing powerful priors from vision and language encoders pre-trained on large-scale datasets.

The paper addresses the task of language instruction-guided robotic manipulation, where an embodied robot manipulates target objects based on language instructions. Unlike previous studies where predicted manipulation regions typically don't change based on language instructions, the paper recognizes that in human behavior, manipulation regions change for different language instructions.

Key contributions include:

- A Vision-Language-Models (VLMs)-based data augmentation pipeline that can generate large amounts of data automatically for model training
- Integration with Large-Language-Models (LLMs) to effectively execute actions for task completion
- Real-world experiments showing improved performance with generated data and better generalization to unseen objects and language instructions

The paper was published on arXiv in August 2024 (arxiv 2408.10658) and is authored by researchers from Shandong University and Meituan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3b90325-dca0-4ceb-8ceb-59fcb83f6832",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "e4c95efb-f683-42fb-a89d-618a1f185ba4",
  "sourceToolAssistantUUID": "a3b90325-dca0-4ceb-8ceb-59fcb83f6832",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T18:45:34.797Z_

<details><summary>↩ Tool result · `toolu_01Qq5fLNbBkNJoU3Ji8Y8re4`</summary>

```text
Web search results for query: "paraphrase augmentation vision language action model robotic policy generalization"

Links: [{"title":"Enhancing Generalization in Vision-Language-Action ...","url":"https://arxiv.org/pdf/2509.11417"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v2"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"LACY: A Vision-Language Model-based Language-Action Cycle for Self-Improving Robotic Manipulation","url":"https://arxiv.org/pdf/2511.02239"},{"title":"π0.5: a Vision-Language-Action Model with Open-World Generalization","url":"https://www.pi.website/download/pi05.pdf"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic   Control","url":"https://arxiv.org/pdf/2307.15818"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"}]

Based on the search results, I found relevant research on paraphrase augmentation and vision-language-action models for robotic policy generalization:

The research evaluates policies under original and paraphrased instructions, with "w/ Inst. Aug." indicating training with instruction augmentations. This appears to be part of work focused on enhancing generalization in vision-language-action (VLA) models.

One approach proposes a language-aligned action tokenizer that casts numerical robot actions into character sequences, enabling maximal reuse of pretrained language representations and allowing actions to be refined step by step.

More broadly, research has demonstrated that broadening the training data distribution for robot manipulation policies from narrow, single-task datasets to diverse datasets that span many scenes and tasks allows resulting policies to not only solve a wider range of tasks out of the box, but also improves their ability to generalize to new scenes and tasks.

Additionally, VLA approaches involve fine-tuning large vision-language models trained on web-scale data to directly act as generalizable and semantically aware robotic policies.

The search results indicate that paraphrase augmentation and instruction augmentation are techniques being explored to improve the robustness and generalization capabilities of vision-language-action models for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4ad56c7-1c3c-4c2c-a179-b9c10c1746a2",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "5b188e01-60b2-4571-8121-8e9998132518",
  "sourceToolAssistantUUID": "e4ad56c7-1c3c-4c2c-a179-b9c10c1746a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-18T18:45:39.251Z_

Let me do a final round of highly targeted searches on the specific combination you're proposing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b188e01-60b2-4571-8121-8e9998132518",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXht7BBNyBoxcrmBjaH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a75a035-3419-44ad-ac37-bba05153bbbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BD9CMC5huLLcX5iv91eDJF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 576,
      "cache_creation_input_tokens": 2170,
      "cache_read_input_tokens": 19531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2170,
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

_source line 42 · 2026-05-18T18:45:40.659Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018NHzERqDpknRwWfeUK2Hhy`</summary>

```json
{
  "query": "arxiv 2510.00037 RobustVLA language perturbation invariance affordance detail"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a75a035-3419-44ad-ac37-bba05153bbbf",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXht7BBNyBoxcrmBjaH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afe57365-a8cd-41b1-b6aa-bb25f4956963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BD9CMC5huLLcX5iv91eDJF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 576,
      "cache_creation_input_tokens": 2170,
      "cache_read_input_tokens": 19531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2170,
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

_source line 43 · 2026-05-18T18:45:41.942Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YEtwC6Dr5Hgd7AhpoR1Bdc`</summary>

```json
{
  "query": "\"affordance invariance\" OR \"affordance equivariance\" language instruction self-supervised contrastive 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afe57365-a8cd-41b1-b6aa-bb25f4956963",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXht7BBNyBoxcrmBjaH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aabd9926-076c-49f4-ab5c-1b40b061c8ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BD9CMC5huLLcX5iv91eDJF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 576,
      "cache_creation_input_tokens": 2170,
      "cache_read_input_tokens": 19531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2170,
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

_source line 44 · 2026-05-18T18:45:42.546Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Gw2xDYSdZx7LVXyLKngaR`</summary>

```json
{
  "query": "Enhancing Generalization Vision-Language-Action instruction augmentation paraphrase arxiv 2509.11417"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aabd9926-076c-49f4-ab5c-1b40b061c8ef",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXht7BBNyBoxcrmBjaH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0115cd6f-a62a-4532-b263-875f9515e331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BD9CMC5huLLcX5iv91eDJF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 576,
      "cache_creation_input_tokens": 2170,
      "cache_read_input_tokens": 19531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2170,
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

_source line 45 · 2026-05-18T18:45:43.303Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014kiSXZCB5eTwUL9cA5Z1yh`</summary>

```json
{
  "query": "\"self-supervised affordance\" \"language invariance\" OR \"instruction invariance\" OR \"paraphrase\" contrastive loss 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0115cd6f-a62a-4532-b263-875f9515e331",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXht7BBNyBoxcrmBjaH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c58b7992-aa64-4bf3-862f-a189ced9daaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BD9CMC5huLLcX5iv91eDJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 576,
      "cache_creation_input_tokens": 2170,
      "cache_read_input_tokens": 19531,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2170
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 576,
          "output_tokens": 287,
          "cache_read_input_tokens": 19531,
          "cache_creation_input_tokens": 2170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2170,
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

_source line 46 · 2026-05-18T18:45:47.696Z_

<details><summary>↩ Tool result · `toolu_018NHzERqDpknRwWfeUK2Hhy`</summary>

```text
Web search results for query: "arxiv 2510.00037 RobustVLA language perturbation invariance affordance detail"

Links: [{"title":"[2510.00037] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037"},{"title":"[2510.00037v4] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037v4"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331v2"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.01331"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"}]

I found the paper arxiv 2510.00037. Based on the search results, here's what I found:

## Paper Overview

The paper is titled "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations" and was published as a conference paper at ICLR 2026.

## Key Contributions

The paper evaluates the robustness of mainstream VLAs under 17 perturbations across four modalities, finding that actions are the most fragile modality and that pi0 demonstrates superior robustness.

## The RobustVLA Method

The paper proposes RobustVLA to address perturbations in VLA inputs and outputs. The approach has two components:

- **Input Robustness**: For input robustness, they enforce consistent actions across input variations that preserve task semantics
- **Output Robustness**: For output robustness, they perform offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective, which can be seen as adversarial training, label smoothing, and outlier penalization

## Results

On LIBERO benchmark, RobustVLA delivers absolute gains of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afe57365-a8cd-41b1-b6aa-bb25f4956963",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "5ecbd201-4f7c-4703-bdb7-ddee9f28168a",
  "sourceToolAssistantUUID": "afe57365-a8cd-41b1-b6aa-bb25f4956963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-18T18:45:50.291Z_

<details><summary>↩ Tool result · `toolu_01YEtwC6Dr5Hgd7AhpoR1Bdc`</summary>

```text
Web search results for query: ""affordance invariance" OR "affordance equivariance" language instruction self-supervised contrastive 2025 2026"

Links: [{"title":"Amortised Invariance Learning for Contrastive Self-Supervision","url":"https://arxiv.org/pdf/2302.12712"},{"title":"Self Supervised Contrastive Learning Combining Equivariance and Invariance | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-97-7244-5_22"},{"title":"Weakly-Supervised Affordance Grounding Guided by Part-Level Semantic Priors","url":"https://www.researchgate.net/publication/392314511_Weakly-Supervised_Affordance_Grounding_Guided_by_Part-Level_Semantic_Priors"},{"title":"[2508.07877] Selective Contrastive Learning for Weakly Supervised Affordance Grounding","url":"https://arxiv.org/abs/2508.07877"},{"title":"[2111.00899] Equivariant Contrastive Learning","url":"https://arxiv.org/abs/2111.00899"}]

I found several relevant research papers on this topic. Here are the search results:

## Key Findings

**Affordance and Contrastive Learning (2025):**
Recent work on affordance grounding uses contrastive learning with vision-language model embeddings for text-conditioned affordance map generation to enhance robustness. Other approaches introduce selective prototypical and pixel contrastive objectives that adaptively learn affordance-relevant cues at both the part and object levels.

**Invariance and Equivariance in Self-Supervised Learning:**
Contrastive self-supervised learning methods produce high quality transferable representations by learning invariances to different data augmentations. However, pre-training that encourages non-trivial equivariance to some transformations while maintaining invariance to other transformations can improve the semantic quality of representations.

Models can learn invariant transformations by learning equivariance at the same time, which represents a more nuanced approach than using invariance alone.

The search results show active research into combining affordance learning with self-supervised contrastive methods, with emphasis on both invariance and equivariance properties in 2024-2025 publications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aabd9926-076c-49f4-ab5c-1b40b061c8ef",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "dd026dcc-af5a-441b-b16f-1a31d0b7be6d",
  "sourceToolAssistantUUID": "aabd9926-076c-49f4-ab5c-1b40b061c8ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T18:45:55.870Z_

<details><summary>↩ Tool result · `toolu_011Gw2xDYSdZx7LVXyLKngaR`</summary>

```text
Web search results for query: "Enhancing Generalization Vision-Language-Action instruction augmentation paraphrase arxiv 2509.11417"

Links: [{"title":"Enhancing Generalization in Vision-Language-Action Models","url":"https://gen-vla.github.io/"},{"title":"Enhancing Generalization in Vision-Language-Action ...","url":"https://arxiv.org/pdf/2509.11417"},{"title":"[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/abs/2509.11417"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"},{"title":"[PDF] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Enhancing-Generalization-in-Vision-Language-Action-Grover-Gopalkrishnan/272525654b60ab7f4366e58244feadcfd2675aaf"}]

I found the paper! Here are the key details about arxiv 2509.11417:

## Paper Overview

The paper titled "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" addresses how Vision-Language-Action (VLA) models can better leverage pretrained representations through three main components: a dual-encoder design with one frozen vision encoder, a string-based action tokenizer that converts continuous actions into character sequences, and a co-training strategy combining robot demonstrations with vision-language datasets.

## Key Problem

Baseline models show a significant drop in performance when backgrounds change or instructions are paraphrased. Direct fine-tuning on robot data often disrupts these representations and limits generalization.

## Main Approach

The framework better preserves pretrained features while adapting them for robot manipulation. Despite receiving no language augmentations, the models substantially outperform baselines trained with augmentation by achieving stronger instruction generalization through leveraging pretrained representations via the string-based action tokenizer.

## Results

Evaluations in simulation and on real robots show that the method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines.

The paper was published on September 14, 2025, by Shresth Grover and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0115cd6f-a62a-4532-b263-875f9515e331",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "61f697e4-93bc-4d0a-b92f-ad6e4e02e395",
  "sourceToolAssistantUUID": "0115cd6f-a62a-4532-b263-875f9515e331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T18:45:57.510Z_

<details><summary>↩ Tool result · `toolu_014kiSXZCB5eTwUL9cA5Z1yh`</summary>

```text
Web search results for query: ""self-supervised affordance" "language invariance" OR "instruction invariance" OR "paraphrase" contrastive loss 2024 2025 2026"

Links: [{"title":"WEAKLY-SUPERVISED AFFORDANCE GROUNDING ...","url":"https://openreview.net/pdf/2551c99500000f40bd07dc3c4c3d1111d11b9c1a.pdf"},{"title":"[2302.12712] Amortised Invariance Learning for Contrastive Self-Supervision","url":"https://arxiv.org/abs/2302.12712"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2403.18699"},{"title":"amortised invariance learning for contrastive self-supervision","url":"https://arxiv.org/pdf/2302.12712"},{"title":"Why Do Self-Supervised Models Transfer? Investigating the Impact of   Invariance on Downstream Tasks","url":"https://arxiv.org/pdf/2111.11398"},{"title":"Published as a conference paper at ICLR 2024 LEARNING CONDITIONAL INVARIANCES","url":"https://arxiv.org/pdf/2402.11682"},{"title":"Impact of Language Guidance: A Reproducibility Study","url":"https://arxiv.org/pdf/2504.08140"}]

I've performed the web search for your query on self-supervised affordance learning with language/instruction invariance and contrastive loss. Here are the key results:

**Recent Work on Affordance and Contrastive Learning (2024-2026):**

Recent work focuses on weakly supervised 2D affordance grounding, which has potential to efficiently scale data size and diversity while mimicking how humans perceive affordances. Some approaches design invariance mining modules to extract knowledge while aligning ego-/exo-centric image features.

**Contrastive Learning and Invariance:**

Contrastive self-supervised learning methods produce high-quality transferable representations by learning invariances to different data augmentations. Studies confirm that contrastive methods learn invariance to augmentations and that this invariance largely transfers to related real-world changes in pose and lighting.

**Language Guidance in Self-Supervised Learning:**

Recent approaches propose using caption similarity based on embeddings generated using a pre-trained language encoder to sample image pairs for contrastive learning. Language appears to be a good proxy for conceptual similarity.

The search results show ongoing research in contrastive self-supervised learning with various forms of invariance and some exploration of language guidance, though specific papers directly combining all your keywords (self-supervised affordance with language/instruction invariance using contrastive loss in 2024-2026) appear limited in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c58b7992-aa64-4bf3-862f-a189ced9daaa",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "25d2f0e9-e5f7-45f4-a7fe-203f0c734c92",
  "sourceToolAssistantUUID": "c58b7992-aa64-4bf3-862f-a189ced9daaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-18T18:46:02.414Z_

Let me do one final batch of searches to ensure completeness, specifically looking at the most recent 2026 work and the specific intersection you care about.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25d2f0e9-e5f7-45f4-a7fe-203f0c734c92",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXjZQqhW5exKuNTFiXS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6356e197-4e14-441a-aa65-10a39e665c3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHmyYhWYLrdKERrVZv4WS5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 21701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 51 · 2026-05-18T18:46:03.431Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018jtuiKxxAp51mxp49j1B8N`</summary>

```json
{
  "query": "arxiv 2603.16044 synthetic instruction augmentation OpenVLA fine-tuning linguistic generalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6356e197-4e14-441a-aa65-10a39e665c3f",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXjZQqhW5exKuNTFiXS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7abac0c4-29b0-4355-b459-cf7853132d1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHmyYhWYLrdKERrVZv4WS5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 21701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 52 · 2026-05-18T18:46:04.372Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SwTZj7eYHhiNpcs7oZh7un`</summary>

```json
{
  "query": "\"Learning Affordances at Inference-Time\" VLA arxiv 2510.19752 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7abac0c4-29b0-4355-b459-cf7853132d1a",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXjZQqhW5exKuNTFiXS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b21293ed-ca66-4f9b-9012-e3d74b8b75bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHmyYhWYLrdKERrVZv4WS5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 21701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 53 · 2026-05-18T18:46:05.315Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NkDBxMn5Z39BHeypEmRYwx`</summary>

```json
{
  "query": "EIVA egocentric instruction-oriented visual affordance 2025 arxiv 2508.17922"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b21293ed-ca66-4f9b-9012-e3d74b8b75bb",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXjZQqhW5exKuNTFiXS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "399b3418-47e6-44a3-a9dc-123af71ce151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHmyYhWYLrdKERrVZv4WS5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 21701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3509,
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

_source line 54 · 2026-05-18T18:46:05.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013MGZitLjeuND9TUQkgRsK6`</summary>

```json
{
  "query": "invariance contrastive affordance heatmap language instruction robot 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "399b3418-47e6-44a3-a9dc-123af71ce151",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXjZQqhW5exKuNTFiXS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "763c251d-7c72-4df1-8cfc-518d032677da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHmyYhWYLrdKERrVZv4WS5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 21701,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3509
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 279,
          "cache_read_input_tokens": 21701,
          "cache_creation_input_tokens": 3509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3509,
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

_source line 55 · 2026-05-18T18:46:09.809Z_

<details><summary>↩ Tool result · `toolu_018jtuiKxxAp51mxp49j1B8N`</summary>

```text
Web search results for query: "arxiv 2603.16044 synthetic instruction augmentation OpenVLA fine-tuning linguistic generalization"

Links: [{"title":"[2603.16044] Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/abs/2603.16044"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/html/2603.16044"},{"title":"Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"},{"title":"A New Path: Scaling Vision-and-Language Navigation with Synthetic   Instructions and Imitation Learning","url":"https://arxiv.org/pdf/2210.03112"},{"title":"IA-VLA: Input Augmentation for Vision-Language-Action models in settings with semantically complex tasks","url":"https://arxiv.org/html/2509.24768v1"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"}]

Based on the search results, I found the paper you're looking for:

## Paper Summary

The paper proposes a parameter-efficient fine-tuning strategy to enhance the linguistic generalization of OpenVLA by synthesizing a general instruction set for the Bridge Dataset V2.

### Key Approach

The paper leverages a Large Language Model (LLM) to generate a rich variety of semantically equivalent but structurally diverse commands for existing trajectories. Low-Rank Adaptation (LoRA) is implemented to fine-tune OpenVLA on augmented pairs, allowing the model to bridge the gap between complex natural language intent and robotic actions.

### Motivation

While OpenVLA represents the State-of-the-Art (SOTA) in Vision-Language-Action models by leveraging large-scale pre-training, its zero-shot performance can be limited when encountering completely new environments. This process allows the model to adapt to a general instruction space, preventing it from overfitting to specific, rigid phrasing.

The paper (arxiv:2603.16044) was submitted on March 17, 2026, and is authored by Dongik Shin.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7abac0c4-29b0-4355-b459-cf7853132d1a",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "19860124-92c2-4809-ac80-9e996930831d",
  "sourceToolAssistantUUID": "7abac0c4-29b0-4355-b459-cf7853132d1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-18T18:46:11.540Z_

<details><summary>↩ Tool result · `toolu_01SwTZj7eYHhiNpcs7oZh7un`</summary>

```text
Web search results for query: ""Learning Affordances at Inference-Time" VLA arxiv 2510.19752 2025"

Links: [{"title":"[2510.19752] Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.19752"},{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251019752S/abstract"},{"title":"Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.19752"},{"title":"LITEN: Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://liten-vla.github.io/"},{"title":"[Literature Review] Learning Affordances at Inference-Time for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/learning-affordances-at-inference-time-for-vision-language-action-models"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"}]

I found the paper you're looking for! Here are the key details:

**Title:** Learning Affordances at Inference-Time for Vision-Language-Action Models

**arXiv ID:** 2510.19752

**Submission Date:** October 22, 2025

**Authors:** Ameesh Shah, William Chen, Adwait Godbole, Federico Mora, Sanjit A. Seshia, Sergey Levine

**Overview:**

The paper introduces Learning from Inference-Time Execution (LITEN), which connects a VLA low-level policy to a high-level VLM that conditions on past experiences by including them in-context, allowing it to learn the affordances and capabilities of the low-level VLA.

The approach iterates between a reasoning phase that generates and executes plans for the low-level VLA, and an assessment phase that reflects on the resulting execution and draws useful conclusions to be included in future reasoning contexts.

LITEN requires no additional training and can be used by off-the-shelf VLMs. The method is demonstrated on long-horizon manipulation tasks using the DROID Franka robot setup.

You can access the paper directly at: https://arxiv.org/abs/2510.19752


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b21293ed-ca66-4f9b-9012-e3d74b8b75bb",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "405dbbfc-79a4-4627-9f68-25ee2d336b55",
  "sourceToolAssistantUUID": "b21293ed-ca66-4f9b-9012-e3d74b8b75bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-18T18:46:13.311Z_

<details><summary>↩ Tool result · `toolu_013MGZitLjeuND9TUQkgRsK6`</summary>

```text
Web search results for query: "invariance contrastive affordance heatmap language instruction robot 2025 2026 arxiv"

Links: [{"title":"More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks","url":"https://arxiv.org/html/2510.10912v1"},{"title":"More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks","url":"https://arxiv.org/pdf/2510.10912"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/html/2409.01083v4"},{"title":"arXiv:2406.11786v1 [cs.RO] 17 Jun 2024","url":"https://arxiv.org/pdf/2406.11786"},{"title":"[2411.02704] RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/abs/2411.02704"},{"title":"WEAKLY-SUPERVISED AFFORDANCE GROUNDING ...","url":"https://openreview.net/pdf/2551c99500000f40bd07dc3c4c3d1111d11b9c1a.pdf"}]

I found several relevant research papers on arXiv related to affordance heatmaps and language instruction for robots. Here are the key results:

## Primary Match

RoboMAP (More than A Point) is a framework that generates adaptive affordance heatmaps. This heatmap models the entire workspace as a continuous probability distribution, quantifying the suitability of each region for a given language-conditioned task. RoboMAP surpasses the previous state-of-the-art on a majority of grounding benchmarks with up to a 50x speed improvement, and achieves an 82% success rate in real-world manipulation. This paper was published on October 13, 2025.

## Related Research

Additionally, I found papers on:

- A framework that uses language instructions to extract instruction-relevant manipulation affordances (from "Affordance-based Robot Manipulation with Flow Matching", February 1, 2025)

- RT-Affordance, a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation (November 5, 2024)

- Research on invariance mining modules to extract useful knowledge in exocentric images, while aligning ego-/exocentric image features (from a paper on weakly-supervised affordance grounding)

The search results show active research in 2025-2026 combining language instructions, affordance representations, and heatmap-based spatial grounding for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "763c251d-7c72-4df1-8cfc-518d032677da",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "8aa9a2b4-faaf-4dc1-823c-18171d6b45a6",
  "sourceToolAssistantUUID": "763c251d-7c72-4df1-8cfc-518d032677da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T18:46:14.760Z_

<details><summary>↩ Tool result · `toolu_01NkDBxMn5Z39BHeypEmRYwx`</summary>

```text
Web search results for query: "EIVA egocentric instruction-oriented visual affordance 2025 arxiv 2508.17922"

Links: [{"title":"[Literature Review] Egocentric Instruction-oriented Affordance Prediction via Large Multimodal Model","url":"https://www.themoonlight.io/en/review/egocentric-instruction-oriented-affordance-prediction-via-large-multimodal-model"},{"title":"Egocentric Instruction-oriented Affordance Prediction via Large Multimodal Model","url":"https://arxiv.org/html/2508.17922v1"},{"title":"[2508.17922] Egocentric Instruction-oriented Affordance Prediction via Large Multimodal Model","url":"https://arxiv.org/abs/2508.17922"},{"title":"Egocentric Instruction-oriented Affordance Prediction via ...","url":"https://arxiv.org/pdf/2508.17922"},{"title":"[2404.02523] Text-driven Affordance Learning from Egocentric Vision","url":"https://arxiv.org/abs/2404.02523"}]

Based on the search results, here's what I found about EIVA and the arxiv paper 2508.17922:

## Overview
The paper introduces a new task and dataset named EIVA (Egocentric Instruction-oriented Visual Affordance), which necessitates models to predict affordances based on an egocentric image and an open-vocabulary instruction. The affordance includes the contact region and the motion direction of manipulation.

## Key Contributions
The paper argues that affordance should be task-/instruction-dependent, noting that different instructions can lead to different manipulation regions and directions even for the same object.

## Dataset Details
EIVA contains 14,861 egocentric scenes, with each scene featuring an object-instruction-affordance triplet, involving a total of 146 object-instruction combinations. The data sources include Ego4D, Epic-Kitchens, and HOI4D.

## Methodology
The paper investigates how to enable large multimodal models (LMMs) to serve as affordance predictors by implementing a "search against verifiers" pipeline, where an LMM is asked to progressively predict affordances, with the output at each step being verified by itself during the iterative process. The paper evaluates the advanced open-source model Qwen2.5-VL and the closed-source model GPT-4o as the backbone.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "399b3418-47e6-44a3-a9dc-123af71ce151",
  "isSidechain": true,
  "promptId": "53b3880e-93bb-4f5d-8446-5c39f5e8cb3f",
  "agentId": "a732ab29303cd0b0a",
  "type": "user",
  "uuid": "3a7690a6-9b41-4267-81b1-47323caeecc8",
  "sourceToolAssistantUUID": "399b3418-47e6-44a3-a9dc-123af71ce151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-18T18:47:13.073Z_

I now have comprehensive findings across all searches. Here is my detailed report.

---

## Novelty Verification Report: Instruction Paraphrase Invariance as Self-Supervision for Affordance Learning in VLAs

### Summary Verdict

**No existing paper was found that uses instruction paraphrase invariance as a self-supervised signal specifically for affordance learning in VLAs.** Several papers touch on adjacent ideas -- instruction-conditioned affordance, VLA robustness to language perturbations, instruction augmentation for VLA generalization -- but none combine all three core elements of your proposal: (1) paraphrase/instruction invariance, (2) used as a self-supervised loss, (3) applied specifically to affordance representations.

---

### Detailed Paper-by-Paper Analysis

#### CLOSEST RELATED WORK (HIGH RELEVANCE)

**1. RobustVLA: "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations"**
- arXiv: [2510.00037](https://arxiv.org/abs/2510.00037), ICLR 2026
- Authors evaluate VLA robustness under 17 perturbation types across 4 modalities. They enforce consistent **actions** across input variations that preserve task semantics.
- **Similarity: MODERATE-HIGH.** This paper enforces action consistency under input perturbations (including linguistic ones), but the invariance target is the **action output**, not an **affordance representation**. It is a robustness/adversarial training method, not a self-supervised affordance learning method. It does not explicitly use paraphrased instructions as a self-supervision signal for learning affordance maps or affordance features.
- **Key distinction from your idea:** RobustVLA is about action-level robustness via consistency regularization, not about learning better affordance representations through language invariance as a self-supervised objective.

**2. "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations"**
- arXiv: [2509.11417](https://arxiv.org/abs/2509.11417), September 2025
- Evaluates VLA performance under paraphrased instructions. Uses a string-based action tokenizer and co-training strategy. Finds that preserving pretrained representations enables instruction generalization **without** explicit language augmentation.
- **Similarity: MODERATE.** This paper acknowledges the paraphrase robustness problem but solves it architecturally (freezing pretrained representations), not through a self-supervised affordance invariance loss.
- **Key distinction:** No affordance learning component; no invariance loss; purely architectural solution.

**3. "Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation"**
- arXiv: [2603.16044](https://arxiv.org/abs/2603.16044), March 2026
- Uses an LLM to generate semantically equivalent but structurally diverse instruction paraphrases, then fine-tunes OpenVLA with LoRA on augmented instruction-trajectory pairs.
- **Similarity: MODERATE.** This is the closest to your paraphrase idea in terms of **generating paraphrases**, but it uses them purely as data augmentation for supervised fine-tuning of action prediction, **not** as a self-supervised invariance signal for affordance learning.
- **Key distinction:** Data augmentation for action prediction vs. self-supervised affordance invariance loss. No affordance representation is learned.

**4. IGANet: "Learning Instruction-Guided Manipulation Affordance via Large Models for Embodied Robotic Tasks"**
- arXiv: [2408.10658](https://arxiv.org/abs/2408.10658), August 2024
- Predicts instruction-dependent affordance maps. Uses VLM-based data augmentation to generate training data. Recognizes that affordance regions change with different instructions.
- **Similarity: MODERATE.** This paper is about instruction-conditioned affordance prediction, but does **not** use paraphrase invariance as a self-supervised signal. The data augmentation is for generating more training examples, not for enforcing consistency across paraphrases.
- **Key distinction:** Supervised affordance learning with data augmentation, not self-supervised invariance.

#### RELATED BUT LOWER SIMILARITY

**5. CoA-VLA: "Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance"**
- arXiv: [2412.20451](https://arxiv.org/abs/2412.20451), ICCV 2025
- Decomposes affordance into four types (object, grasp, spatial, movement) and uses chain-of-affordance reasoning at test time.
- **Similarity: LOW-MODERATE.** Uses affordance as an intermediate reasoning step in VLAs, but no invariance or self-supervised learning component.

**6. RT-Affordance: "Affordances are Versatile Intermediate Representations for Robot Manipulation"**
- arXiv: [2411.02704](https://arxiv.org/abs/2411.02704), ICRA 2025
- Uses affordances (end-effector poses at key stages) as intermediate representations between language and action. Hierarchical model: language -> affordance plan -> policy.
- **Similarity: LOW-MODERATE.** Affordance as intermediate representation is relevant conceptually, but no invariance or self-supervised component.

**7. LITEN: "Learning Affordances at Inference-Time for Vision-Language-Action Models"**
- arXiv: [2510.19752](https://arxiv.org/abs/2510.19752), October 2025
- Learns affordances at inference time by having a VLM reflect on VLA execution results in-context. No additional training required.
- **Similarity: LOW.** Inference-time affordance learning, no paraphrase invariance, no self-supervised training loss.

**8. EIVA: "Egocentric Instruction-oriented Affordance Prediction via Large Multimodal Model"**
- arXiv: [2508.17922](https://arxiv.org/abs/2508.17922), 2025
- Task-dependent affordance prediction from egocentric views. Uses LMMs as affordance predictors with iterative self-verification.
- **Similarity: LOW.** Instruction-dependent affordance prediction, but no invariance or self-supervised learning.

**9. Affordance Field Intervention for VLAs**
- arXiv: [2512.07472](https://arxiv.org/abs/2512.07472)
- Identifies memory traps in VLA execution and uses spatial affordance fields to propose waypoints.
- **Similarity: LOW.** Addresses VLA failure modes via affordance-based recovery, unrelated to language invariance.

**10. DiG-Flow: "Discrepancy-Guided Flow Matching for Robust VLA Models"**
- arXiv: [2512.01715](https://arxiv.org/abs/2512.01715)
- Uses discrepancy between observation/action embeddings to modulate flow matching for VLA robustness.
- **Similarity: LOW.** Distribution shift robustness without language invariance or affordance self-supervision.

**11. PI-VLA: "A Symmetry-Aware Predictive and Interactive Vision-Language-Action Framework"**
- Preprints.org, January 2026
- Enforces cross-modal action consistency as an implicit symmetry constraint, encouraging invariance to task-relevant transformations.
- **Similarity: LOW-MODERATE.** Uses invariance concepts but focused on visual/spatial symmetries, not linguistic invariance for affordance learning.

**12. "Selective Contrastive Learning for Weakly Supervised Affordance Grounding"**
- arXiv: [2508.07877](https://arxiv.org/abs/2508.07877), 2025
- Uses selective prototypical and pixel contrastive objectives for affordance grounding.
- **Similarity: LOW.** Contrastive learning for affordance, but focused on visual features, not language invariance.

**13. "Grounding Language with Visual Affordances over Unstructured Data"**
- arXiv: [2210.01911](https://arxiv.org/abs/2210.01911)
- Self-supervised visual affordance model extended with language conditioning. Only 1% of data needs language annotation.
- **Similarity: LOW-MODERATE.** Self-supervised affordance + language, but no paraphrase invariance mechanism.

---

### Gap Analysis

The specific combination you propose -- using **instruction paraphrase invariance as a self-supervised signal for learning affordance representations in VLAs** -- occupies a clear gap in the literature:

| Component | Existing Work | Your Proposal |
|---|---|---|
| Instruction-conditioned affordance | IGANet, EIVA, CoA-VLA, RT-Affordance | Yes |
| Paraphrase/instruction augmentation for VLAs | arXiv 2603.16044, arXiv 2509.11417 | Yes |
| Action consistency under perturbations | RobustVLA (ICLR 2026), PI-VLA | N/A (affordance-level, not action-level) |
| Self-supervised affordance learning | Grounding Language with Visual Affordances | Yes |
| **Paraphrase invariance loss on affordance representations** | **NOT FOUND** | **Core contribution** |

The closest threats to novelty are:
1. **RobustVLA** (ICLR 2026) -- but it enforces action consistency, not affordance representation invariance.
2. **arXiv 2603.16044** (March 2026) -- but it uses paraphrases for data augmentation, not as a self-supervised invariance signal on affordance features.
3. **IGANet** -- but it is supervised, not self-supervised via invariance.

**None of these papers propose using the principle that semantically equivalent instructions should produce invariant affordance representations as a self-supervised training objective.** This appears to be a novel contribution.

Sources:
- [RobustVLA - On Robustness of VLA against Multi-Modal Perturbations (ICLR 2026)](https://arxiv.org/abs/2510.00037)
- [Enhancing Generalization in VLA Models by Preserving Pretrained Representations](https://arxiv.org/abs/2509.11417)
- [Enhancing Linguistic Generalization of VLA via Synthetic Instruction Augmentation](https://arxiv.org/abs/2603.16044)
- [IGANet - Learning Instruction-Guided Manipulation Affordance](https://arxiv.org/abs/2408.10658)
- [CoA-VLA - Chain-of-Affordance for VLAs (ICCV 2025)](https://arxiv.org/abs/2412.20451)
- [RT-Affordance (ICRA 2025)](https://arxiv.org/abs/2411.02704)
- [LITEN - Learning Affordances at Inference-Time](https://arxiv.org/abs/2510.19752)
- [EIVA - Egocentric Instruction-oriented Visual Affordance](https://arxiv.org/abs/2508.17922)
- [Affordance Field Intervention for VLAs](https://arxiv.org/abs/2512.07472)
- [DiG-Flow](https://arxiv.org/abs/2512.01715)
- [PI-VLA](https://www.preprints.org/manuscript/202601.0682)
- [Selective Contrastive Learning for Weakly Supervised Affordance Grounding](https://arxiv.org/abs/2508.07877)
- [Grounding Language with Visual Affordances over Unstructured Data](https://arxiv.org/abs/2210.01911)
- [RobustVLA Reinforcement Post-Training](https://arxiv.org/abs/2511.01331)
- [SayCan - Do As I Can, Not As I Say](https://say-can.github.io/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a7690a6-9b41-4267-81b1-47323caeecc8",
  "isSidechain": true,
  "agentId": "a732ab29303cd0b0a",
  "requestId": "req_011CbAXkpyFNYG7jLLSxa99Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "510dcb6e-7730-4fa2-bf9d-09a00e2a0d29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "666a6b62-b3dd-46de-82c2-26662f83e249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018t51yJ9ccDp3QajASuit2h",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 716,
      "cache_creation_input_tokens": 2154,
      "cache_read_input_tokens": 25210,
      "output_tokens": 2929,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2154
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 716,
          "output_tokens": 2929,
          "cache_read_input_tokens": 25210,
          "cache_creation_input_tokens": 2154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2154,
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
