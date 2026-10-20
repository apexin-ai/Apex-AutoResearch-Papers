# Research conversation: I need to verify the current landscape of VLA (Vision-Language-Action) token compression methods and robustness methods 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 1
- **Tool calls:** 33
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5b15f23100730701.jsonl`
- **Structured JSON:** [`fea1434f87edd0bf42e0.json`](../../sessions/fe/fea1434f87edd0bf42e0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

77 recorded events

### User

_source line 1 · 2026-05-14T06:37:53.012Z_

I need to verify the current landscape of VLA (Vision-Language-Action) token compression methods and robustness methods cited in a research proposal. Please use WebSearch to check:

1. Search for VLA-ADP (arXiv 2509.22093) — verify it exists and does action-trajectory-conditioned pruning
2. Search for AVA-VLA (arXiv 2511.18960) — verify it exists and does recurrent visual reweighting with robustness results
3. Search for LightVLA — verify it's accepted at ICRA 2026 with differentiable Gumbel pruning
4. Search for GridS / "See What Matters" — verify ICML 2026 acceptance
5. Search for VLA-Cache (NeurIPS 2025) — verify existence and temporal caching
6. Search for SmolVLA — verify it exists in HuggingFace/LeRobot and its parameter count (~450M)
7. Search for LIBERO-Plus (claimed CVPR 2026) and LIBERO-X (arXiv 2602.06556) — verify these robustness benchmarks exist
8. Search for RobustVLA (arXiv 2511.01331) — verify Jacobian/smoothness regularization approach
9. Search for EfficientVLA (arXiv 2506.10100) — verify training-free acceleration
10. Search for SP-VLA (arXiv 2506.12723, claimed ICLR 2026) — verify joint scheduling + pruning
11. Search for "Visual Token Compression Enhances Model Robustness" on OpenReview — verify this exists
12. Search for FastDriveVLA (arXiv 2507.23318, claimed AAAI 2026) — verify existence

For the most important ones (SmolVLA, LIBERO-Plus, VLA-ADP, AVA-VLA), use WebFetch to read more details. I need to verify these are real papers with correct venues and the claimed findings are accurate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "325ebb92-5376-46b7-a0a2-7d1fc7f68eda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T06:37:53.017Z_

```json
{
  "parentUuid": "325ebb92-5376-46b7-a0a2-7d1fc7f68eda",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
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
  "uuid": "40ddf98f-3ffd-4ee0-83fc-53fd46497f71",
  "timestamp": "2026-05-14T06:37:53.017Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T06:37:56.068Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then conduct systematic searches for all these papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40ddf98f-3ffd-4ee0-83fc-53fd46497f71",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb1zyir7nJEi8U1nEf8br",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac2b741d-b781-46ac-8f49-99385455d8da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLpMUtoxz7YPNe4ULKFdEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1006,
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

_source line 4 · 2026-05-14T06:37:56.179Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FF73xYN8qmCWjvsEAuuE2m`</summary>

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
  "parentUuid": "ac2b741d-b781-46ac-8f49-99385455d8da",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb1zyir7nJEi8U1nEf8br",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdbe7c29-c38a-479f-b707-750c8563d098",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLpMUtoxz7YPNe4ULKFdEJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 7304,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1006
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1006,
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

_source line 5 · 2026-05-14T06:37:56.181Z_

<details><summary>↩ Tool result · `toolu_01FF73xYN8qmCWjvsEAuuE2m`</summary>

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
  "parentUuid": "bdbe7c29-c38a-479f-b707-750c8563d098",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "7fcf2b0f-a111-40d6-9249-786f143b2643",
  "sourceToolAssistantUUID": "bdbe7c29-c38a-479f-b707-750c8563d098",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T06:37:59.875Z_



Now let me search for all these papers in parallel. I'll batch the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fcf2b0f-a111-40d6-9249-786f143b2643",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb1zyxarhK23VSj6UxCDK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "023423c9-17f3-4a51-9fd8-23fb2770e02b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKyg7ru4SaNTXvJ1FXnmbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 7 · 2026-05-14T06:38:01.303Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014N9Nf37uaCCA3pA5jLtm7i`</summary>

```json
{
  "query": "VLA-ADP arXiv 2509.22093 action-trajectory-conditioned pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "023423c9-17f3-4a51-9fd8-23fb2770e02b",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb1zyxarhK23VSj6UxCDK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65604e0d-f444-4751-b62d-a723d628d289",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKyg7ru4SaNTXvJ1FXnmbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 8 · 2026-05-14T06:38:02.303Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JFqpPRNr5AkGdHMYgqduFE`</summary>

```json
{
  "query": "AVA-VLA arXiv 2511.18960 recurrent visual reweighting robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65604e0d-f444-4751-b62d-a723d628d289",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb1zyxarhK23VSj6UxCDK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99b293aa-f454-4885-892e-74bfca94f024",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKyg7ru4SaNTXvJ1FXnmbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 9 · 2026-05-14T06:38:03.249Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Xw41GgGn3YrHeZE29Te5R`</summary>

```json
{
  "query": "LightVLA ICRA 2026 differentiable Gumbel pruning VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99b293aa-f454-4885-892e-74bfca94f024",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb1zyxarhK23VSj6UxCDK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee9e0197-8ae1-4a82-8796-f33628efbc27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKyg7ru4SaNTXvJ1FXnmbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 10 · 2026-05-14T06:38:03.777Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UZQYzWpL9xkfsE99LLSXKS`</summary>

```json
{
  "query": "GridS \"See What Matters\" ICML 2026 visual token compression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee9e0197-8ae1-4a82-8796-f33628efbc27",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb1zyxarhK23VSj6UxCDK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5144f9a6-09ce-465d-a3b4-4ff78d8546e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKyg7ru4SaNTXvJ1FXnmbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 11 · 2026-05-14T06:38:04.713Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HE9kFg8FUUDN4PdJtTiiyU`</summary>

```json
{
  "query": "VLA-Cache NeurIPS 2025 temporal caching vision language action"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5144f9a6-09ce-465d-a3b4-4ff78d8546e9",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb1zyxarhK23VSj6UxCDK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24fa4e02-1c38-458a-b9ea-77e3db9d9d5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKyg7ru4SaNTXvJ1FXnmbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 12 · 2026-05-14T06:38:05.399Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NUAGCVCbagF5UJr2RPwSqq`</summary>

```json
{
  "query": "SmolVLA HuggingFace LeRobot 450M parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24fa4e02-1c38-458a-b9ea-77e3db9d9d5e",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb1zyxarhK23VSj6UxCDK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "327d43b4-cab6-4e8c-bbf5-b1c294a3aac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKyg7ru4SaNTXvJ1FXnmbh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8310,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1914
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 8310,
          "cache_creation_input_tokens": 1914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1914,
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

_source line 13 · 2026-05-14T06:38:06.704Z_

<details><summary>↩ Tool result · `toolu_01UZQYzWpL9xkfsE99LLSXKS`</summary>

```text
Web search results for query: "GridS "See What Matters" ICML 2026 visual token compression"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"}]

Based on the search results, I found information about the research you're looking for:

GridS is a method that uses differentiable interpolation to preserve essential spatial information while achieving drastic compression with fewer than 10% of original visual tokens. This work appears to have been presented as a poster at ICML 2026 under the title "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model."

The search result shows this is related to visual token compression for vision-language-action models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5144f9a6-09ce-465d-a3b4-4ff78d8546e9",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "4a3675da-ba8a-48c5-bc25-fdf73b733c33",
  "sourceToolAssistantUUID": "5144f9a6-09ce-465d-a3b4-4ff78d8546e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T06:38:08.930Z_

<details><summary>↩ Tool result · `toolu_014N9Nf37uaCCA3pA5jLtm7i`</summary>

```text
Web search results for query: "VLA-ADP arXiv 2509.22093 action-trajectory-conditioned pruning"

Links: [{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/html/2509.22093v1"},{"title":"[2509.22093] Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/abs/2509.22093"},{"title":"GitHub - chen7086/VLA-ADP: Action aware Dynamic Pruning for Efficient Vision Language Action Manipulation · GitHub","url":"https://github.com/chen7086/VLA-ADP"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614"},{"title":"[2509.09090] SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models","url":"https://arxiv.org/abs/2509.09090"},{"title":"(PDF) Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://www.researchgate.net/publication/395944757_Action-aware_Dynamic_Pruning_for_Efficient_Vision-Language-Action_Manipulation"},{"title":"[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/abs/2509.05614"},{"title":"Each Complexity Deserves a Pruning Policy","url":"https://arxiv.org/html/2509.23931v1"},{"title":"[2603.06480] History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation","url":"https://arxiv.org/abs/2603.06480"}]

Based on the search results, here's what I found about VLA-ADP (arXiv 2509.22093):

## Overview

VLA-ADP is a multi-modal pruning framework that integrates text-driven token selection with action-aware trajectory gating, designed to improve the efficiency of Vision-Language-Action (VLA) models used in robotic manipulation.

## Key Innovation

The core insight of the work is that visual token redundancy is higher in coarse manipulation phase than in fine-grained operations, and is strongly correlated with the action dynamic. More specifically, during coarse-grained operations (e.g., relocating), global movement dominates and redundant tokens can be pruned; during fine-grained phases (e.g., grasping), local geometry and detailed cues dominate and preserving full vision is preferred.

## How It Works

The method introduces a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics.

## Performance Results

VLA-ADP achieves a stable accuracy–compute trade-off, with 50–70% keep ratio showing slightly decreased average success rate (≤0.9%) while improving LLM-side inference speed by up to 1.23×, and further compressing to 30–40% retention maintains 94.4–94.8% average success rate while achieving 1.29–1.35× speedup.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65604e0d-f444-4751-b62d-a723d628d289",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "3da6944e-f74f-41f8-8ab0-5724d2a88cd4",
  "sourceToolAssistantUUID": "65604e0d-f444-4751-b62d-a723d628d289",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T06:38:08.947Z_

<details><summary>↩ Tool result · `toolu_01JFqpPRNr5AkGdHMYgqduFE`</summary>

```text
Web search results for query: "AVA-VLA arXiv 2511.18960 recurrent visual reweighting robustness"

Links: [{"title":"[2511.18960] AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/abs/2511.18960"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/html/2511.18960"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.18960v1"},{"title":"[2602.01158] Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/abs/2602.01158"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/html/2602.01158"},{"title":"ADVLA: Attention-Guided, Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Model","url":"https://arxiv.org/html/2511.21663"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Eva-VLA: Evaluating Vision-Language-Action Models’ Robustness Under Real-World Physical Variations","url":"https://arxiv.org/html/2509.18953v1"}]

Based on the search results, here's what I found about arXiv paper 2511.18960:

## AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention

AVA-VLA is a framework that reformulates VLA policy learning from a Partially Observable Markov Decision Process perspective and conditions action generation on a recurrent state that serves as a neural approximation to the agent's belief over task history.

### Core Components

The framework introduces Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most relevant given both the instruction and execution history.

### Robustness Performance

The framework exhibits improved robustness across various environmental perturbations in the LIBERO+ benchmark, showing particular resilience to lighting and layout changes that typically challenge vision-based robotic systems.

### Key Results

AVA-VLA achieves state-of-the-art performance across LIBERO, CALVIN, and Mobile ALOHA benchmarks, enhancing generalization, robustness, and sim-to-real transferability. The system successfully performs complex manipulation tasks including object folding, sequenced instruction understanding, and dexterous manipulation, demonstrating robust sim-to-real transfer capabilities.

### Visual Attention Analysis

Visualization of attention patterns reveals that the framework effectively focuses on task-critical regions such as robot-object contact points and relevant environmental features, with attention dynamically shifting throughout task execution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99b293aa-f454-4885-892e-74bfca94f024",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "cb5615e9-70b5-40d4-bfe3-2e95d8e29c6a",
  "sourceToolAssistantUUID": "99b293aa-f454-4885-892e-74bfca94f024",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T06:38:09.588Z_

<details><summary>↩ Tool result · `toolu_013Xw41GgGn3YrHeZE29Te5R`</summary>

```text
Web search results for query: "LightVLA ICRA 2026 differentiable Gumbel pruning VLA"

Links: [{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"},{"title":"LightVLA","url":"https://liauto-research.github.io/LightVLA/"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"AI Bites | YouTube Channel on X: \"LightVLA, a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by https://t.co/bE0Zv0mb0c\" / X","url":"https://x.com/ai_bites/status/1970481721163313156"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop","url":"https://icra2026vlapipeline.github.io/"},{"title":"LiteVLA-H: Dual-Rate Vision-Language-Action Inference for Onboard Aerial Guidance and Semantic Perception","url":"https://arxiv.org/html/2605.00884"}]

Based on the web search results, here's information about LightVLA and its ICRA 2026 acceptance:

## Overview

LightVLA has been accepted by ICRA 2026. LightVLA is an innovative, simple yet effective differentiable token pruning framework designed for Vision-Language-Action (VLA) models.

## Core Mechanism

LightVLA's core lies in its unique adaptive pruning mechanism, which generates dynamic queries to assess the importance of visual tokens and utilizes Gumbel softmax for differentiable token selection. This approach enables the model to intelligently identify and retain crucial visual information for task execution while discarding redundant tokens.

## Key Results

By learning pruning strategies during fine-tuning, LightVLA not only significantly reduces computational overhead (FLOPs and latency) but also improves task success rates on the LIBERO benchmark, achieving a win-win in both efficiency and performance. More specifically, LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.9% improvement in task success rate.

## Technical Advantages

A major advantage of LightVLA is its design, which does not rely on any heuristic magic numbers and introduces no additional trainable parameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee9e0197-8ae1-4a82-8796-f33628efbc27",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "5b379a81-f3eb-4e46-98dd-97a8fc768455",
  "sourceToolAssistantUUID": "ee9e0197-8ae1-4a82-8796-f33628efbc27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T06:38:12.220Z_

<details><summary>↩ Tool result · `toolu_01NUAGCVCbagF5UJr2RPwSqq`</summary>

```text
Web search results for query: "SmolVLA HuggingFace LeRobot 450M parameters"

Links: [{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"lerobot/docs/source/smolvla.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"smolvla_base | AI Model Details","url":"https://www.aimodels.fyi/models/huggingFace/smolvla-base-lerobot"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"lerobot/examples/tutorial/smolvla/using_smolvla_example.py at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/examples/tutorial/smolvla/using_smolvla_example.py"}]

Based on the search results, here's what I found about SmolVLA, HuggingFace's LeRobot, and the 450M parameters:

## Overview

SmolVLA is Hugging Face's lightweight foundation model for robotics, designed for easy fine-tuning on LeRobot datasets to help accelerate your development. SmolVLA-450M is Hugging Face's open-source, compact yet capable VLA (Vision-Language-Action) model.

## Key Specifications

SmolVLA is a 450M parameter vision-language-action model designed for affordable and efficient robotics, optimized to run on consumer hardware while maintaining competitive performance.

## Architecture and Design

SmolVLA goes through a pretraining phase on general manipulation data, followed by task-specific post-training, combining Transformers with flow-matching decoders and optimized for speed and low-latency inference with design choices including skipping half of the layers of the vision model for faster inference and smaller size, and interleaving self-attention and cross-attention blocks.

## Training and Performance

Despite using fewer than 30k training episodes—an order of magnitude less than other VLAs—SmolVLA matches or exceeds the performance of much larger models, both in simulation and the real world. All training data used in SmolVLA comes from LeRobot Community Datasets, robotics datasets shared on the Hugging Face Hub under the lerobot tag, collected in diverse settings, from labs to living rooms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "327d43b4-cab6-4e8c-bbf5-b1c294a3aac2",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "f3401923-b235-4879-8954-da70da16f2a7",
  "sourceToolAssistantUUID": "327d43b4-cab6-4e8c-bbf5-b1c294a3aac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T06:38:13.178Z_

<details><summary>↩ Tool result · `toolu_01HE9kFg8FUUDN4PdJtTiiyU`</summary>

```text
Web search results for query: "VLA-Cache NeurIPS 2025 temporal caching vision language action"

Links: [{"title":"NeurIPS Poster VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118121"},{"title":"GitHub - siyuhsu/vla-cache: [NeurIPS 2025] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching · GitHub","url":"https://github.com/siyuhsu/vla-cache"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation ...","url":"https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf"},{"title":"[2502.02175] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/abs/2502.02175"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching | OpenReview","url":"https://openreview.net/forum?id=QZYZ0Xm58q"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://vla-cache.github.io/"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"GitHub - Zhangwenyao1/DreamVLA: [NeurIPS 2025] DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge · GitHub","url":"https://github.com/Zhangwenyao1/DreamVLA"}]

Based on the search results, here's what I found about VLA-Cache:

## Overview

VLA-Cache was accepted by NeurIPS 2025 and is a training-free, plug-and-play solution for accelerating vision-language-action models.

## Core Technology

VLA-Cache is a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames. It exploits the temporal continuity in robotic manipulation by identifying minimally changed tokens between adjacent frames and reuses their cached key-value representations, thereby circumventing redundant computations.

The approach addresses a specific challenge: VLA tasks involve sequentially processing a stream of temporally adjacent visual observations, where the environment often exhibits high spatial redundancy across time. Large portions of the visual scene, especially background regions, remain static and semantically irrelevant to action decisions, yet are processed repeatedly at each time step.

## Key Components

To further optimize efficiency, VLA-Cache introduces a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens for recomputation.

To maintain action precision, VLA-Cache selectively re-computes task-relevant tokens that are environmentally sensitive, ensuring the fidelity of critical visual information.

## Experimental Results

Extensive experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7x speedup in CUDA latency and a 15% increase in control frequency, with negligible loss on task success rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24fa4e02-1c38-458a-b9ea-77e3db9d9d5e",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "b96260b8-29fe-4e1e-a5d3-c546a8912c71",
  "sourceToolAssistantUUID": "24fa4e02-1c38-458a-b9ea-77e3db9d9d5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T06:38:17.009Z_

Good, first batch done. Now let me search for the remaining papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b96260b8-29fe-4e1e-a5d3-c546a8912c71",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb211D2YZ3xdX9q1KCUTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a49c843-2c02-4465-a4b7-62ffad71adb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsJyTXSeJSne1dNFvgyUcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 4385,
      "cache_read_input_tokens": 10224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4385,
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

_source line 20 · 2026-05-14T06:38:17.567Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AEmmaguwrwhXsEKvkaxx11`</summary>

```json
{
  "query": "LIBERO-Plus CVPR 2026 robustness benchmark VLA robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a49c843-2c02-4465-a4b7-62ffad71adb2",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb211D2YZ3xdX9q1KCUTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10ffafea-13f6-4a70-8f41-d0eaaf01aba0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsJyTXSeJSne1dNFvgyUcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 4385,
      "cache_read_input_tokens": 10224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4385,
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

_source line 21 · 2026-05-14T06:38:17.996Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015L4HUagCDM58az2b8SMXvy`</summary>

```json
{
  "query": "LIBERO-X arXiv 2602.06556 robustness benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10ffafea-13f6-4a70-8f41-d0eaaf01aba0",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb211D2YZ3xdX9q1KCUTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31f9fb59-21b3-4209-b532-a889e297b32f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsJyTXSeJSne1dNFvgyUcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 4385,
      "cache_read_input_tokens": 10224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4385,
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

_source line 22 · 2026-05-14T06:38:18.935Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JNceWBPx6yVWy9oPxLuNCF`</summary>

```json
{
  "query": "RobustVLA arXiv 2511.01331 Jacobian smoothness regularization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31f9fb59-21b3-4209-b532-a889e297b32f",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb211D2YZ3xdX9q1KCUTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc5cb01d-c73c-4a5d-a0e0-50bf9e9b8abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsJyTXSeJSne1dNFvgyUcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 4385,
      "cache_read_input_tokens": 10224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4385,
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

_source line 23 · 2026-05-14T06:38:19.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015kuAVy7KpiozUArZ5YZ31K`</summary>

```json
{
  "query": "EfficientVLA arXiv 2506.10100 training-free acceleration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc5cb01d-c73c-4a5d-a0e0-50bf9e9b8abe",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb211D2YZ3xdX9q1KCUTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4289b931-3201-40fd-86ff-c8ac6bbb24db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsJyTXSeJSne1dNFvgyUcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 4385,
      "cache_read_input_tokens": 10224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4385,
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

_source line 24 · 2026-05-14T06:38:20.512Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LAfeDKV5TnJdxwDNSkgFTs`</summary>

```json
{
  "query": "SP-VLA arXiv 2506.12723 ICLR 2026 joint scheduling pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4289b931-3201-40fd-86ff-c8ac6bbb24db",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb211D2YZ3xdX9q1KCUTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04ed956b-ac7c-4090-877c-b9823fa63b3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsJyTXSeJSne1dNFvgyUcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 4385,
      "cache_read_input_tokens": 10224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4385,
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

_source line 25 · 2026-05-14T06:38:21.400Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ds7dq4pcM9RVmJhgQzsjGV`</summary>

```json
{
  "query": "\"Visual Token Compression Enhances Model Robustness\" OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04ed956b-ac7c-4090-877c-b9823fa63b3e",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb211D2YZ3xdX9q1KCUTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8329aee1-41b3-4df4-bf79-aca4f01bb9e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsJyTXSeJSne1dNFvgyUcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 4385,
      "cache_read_input_tokens": 10224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4385,
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

_source line 26 · 2026-05-14T06:38:21.924Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S18nnhCoveoygKdCvYouB8`</summary>

```json
{
  "query": "FastDriveVLA arXiv 2507.23318 AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8329aee1-41b3-4df4-bf79-aca4f01bb9e9",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb211D2YZ3xdX9q1KCUTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a83071d6-48e8-426c-84a2-5568fe2c0573",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsJyTXSeJSne1dNFvgyUcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 4385,
      "cache_read_input_tokens": 10224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4385,
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

_source line 27 · 2026-05-14T06:38:24.611Z_

<details><summary>↩ Tool result · `toolu_015L4HUagCDM58az2b8SMXvy`</summary>

```text
Web search results for query: "LIBERO-X arXiv 2602.06556 robustness benchmark"

Links: [{"title":"[2602.06556] LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.06556"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"MultiFileTest: A Multi-File-Level LLM Unit Test Generation Benchmark and Impact of Error Fixing Mechanisms","url":"https://arxiv.org/html/2502.06556"},{"title":"LIBERO | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3668061"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"}]

Based on the search results, here's what I found about LIBERO-X (arXiv 2602.06556):

## Overview

LIBERO-X is a benchmark for advancing Vision-Language-Action (VLA) models, designed to reveal their generalization, robustness, and alignment of perception with language-driven manipulation tasks.

## Key Features

The benchmark features a hierarchical evaluation protocol with progressive difficulty levels targeting three core capabilities: spatial generalization, object recognition, and task instruction understanding. This design enables fine-grained analysis of performance degradation under increasing environmental and task complexity.

LIBERO-X includes a high-diversity training dataset collected via human teleoperation that increases scene and task diversity by incorporating variations in object attributes (e.g., size, color, texture) and spatial relations (e.g., left/right, near/far, front/behind), together with language instructions.

## Motivation

The benchmark addresses limitations in existing benchmarks that often provide limited or misleading assessments due to insufficient evaluation protocols that inadequately capture real-world distribution shifts.

The paper was submitted to arXiv on February 6, 2026, and is authored by Guodong Wang, Chenkai Zhang, Qingjie Liu, Jinjin Zhang, Jiancheng Cai, Junjie Liu, and Xinmin Liu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31f9fb59-21b3-4209-b532-a889e297b32f",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "d8b26c46-04c9-4f90-8f41-20491b7b2010",
  "sourceToolAssistantUUID": "31f9fb59-21b3-4209-b532-a889e297b32f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T06:38:25.847Z_

<details><summary>↩ Tool result · `toolu_01JNceWBPx6yVWy9oPxLuNCF`</summary>

```text
Web search results for query: "RobustVLA arXiv 2511.01331 Jacobian smoothness regularization"

Links: [{"title":"[2511.01331] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.01331"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"},{"title":"Robust Learning with Jacobian Regularization","url":"https://arxiv.org/pdf/1908.02729"},{"title":"[1908.02729] Robust Learning with Jacobian Regularization","url":"https://arxiv.org/abs/1908.02729"},{"title":"Robust Learning with Jacobian Regularization | OpenReview","url":"https://openreview.net/forum?id=ryl-RTEYvB"},{"title":"Jacobian Regularization in Machine Learning","url":"https://www.emergentmind.com/topics/jacobian-based-regularization-techniques"},{"title":"Low-Rank Tensor Recovery via Variational Schatten-𝑝 Quasi-Norm and Jacobian Regularization","url":"https://arxiv.org/html/2506.22134"},{"title":"From Robustness to Improved Generalization and Calibration in Pre-trained Language Models","url":"https://arxiv.org/html/2404.00758v1"},{"title":"[1803.08680] Improving DNN Robustness to Adversarial Attacks using Jacobian Regularization","url":"https://arxiv.org/abs/1803.08680"}]

Based on the search results, I found relevant information about RobustVLA arXiv paper 2511.01331:

## RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models

RobustVLA is a lightweight online RL post-training method designed to explicitly enhance the resilience of VLA models.

### Key Regularizations

The method identifies two key regularizations: Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations.

### Theoretical Basis

The robustness gap under observation perturbations is governed by the Jacobian sensitivity of the VLA model, whereas under action perturbations it is controlled by the smoothness of the VLA model update. This theoretical insight naturally motivates the introduction of Jacobian and smoothness regularization into the online RL fine-tuning process, which together constrain the worst-case robustness gap and promote robust decision-making.

### Problem Addressed

VLA models often fail to generalize reliably in out-of-distribution deployments where unavoidable disturbances such as observation noise, sensor errors, or actuation perturbations become prevalent. While recent RL-based post-training provides a practical means to adapt pre-trained VLA models, existing methods mainly emphasize reward maximization and overlook robustness to environmental uncertainty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc5cb01d-c73c-4a5d-a0e0-50bf9e9b8abe",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "a0e68739-b9d1-4e3f-a0ff-7268f729ce8a",
  "sourceToolAssistantUUID": "dc5cb01d-c73c-4a5d-a0e0-50bf9e9b8abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T06:38:26.006Z_

<details><summary>↩ Tool result · `toolu_01AEmmaguwrwhXsEKvkaxx11`</summary>

```text
Web search results for query: "LIBERO-Plus CVPR 2026 robustness benchmark VLA robotics"

Links: [{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"}]

Based on the search results, here's comprehensive information about LIBERO-Plus:

## Overview

LIBERO-Plus is an advanced robustness evaluation tool for Vision-Language-Action (VLA) models that allows researchers to understand how these models perform under various environmental perturbations.

## Key Findings

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

## Benchmark Structure

The benchmark performs a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise. LIBERO-plus introduces a comprehensive benchmark with 10,030 tasks spanning multiple perturbation categories.

## Core Weaknesses Identified

Core weaknesses in contemporary VLA models include vulnerability to visual shifts from over-reliance on fixed visual features, inadequate kinematic reasoning with limited generalization across different initial robot configurations, and superficial language interaction where linguistic inputs are often underutilized or even completely ignored.

## CVPR 2026 Presentation

LIBERO-Plus was presented at CVPR 2026, addressing how Visual–Language–Action models report impressive success rates exceeding 95% on robotic manipulation benchmarks, yet these results may mask fundamental weaknesses in robustness, with current simulation-based robustness evaluations suffering from narrow perturbation coverage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10ffafea-13f6-4a70-8f41-d0eaaf01aba0",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "b1a84eb6-cac0-4bb9-a36b-981a0e70da03",
  "sourceToolAssistantUUID": "10ffafea-13f6-4a70-8f41-d0eaaf01aba0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T06:38:26.687Z_

<details><summary>↩ Tool result · `toolu_015kuAVy7KpiozUArZ5YZ31K`</summary>

```text
Web search results for query: "EfficientVLA arXiv 2506.10100 training-free acceleration"

Links: [{"title":"[2506.10100] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"Paper page - EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.10100"},{"title":"[PDF] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/310b6b4048e36d5948de19fd26e112cbf05fa754"},{"title":"[Literature Review] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/efficientvla-training-free-acceleration-and-compression-for-vision-language-action-models"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"EffiVLM-Bench: A Comprehensive Benchmark for Evaluating Training-Free Acceleration in Large Vision-Language Models","url":"https://arxiv.org/html/2506.00479"},{"title":"Fast ECoT: Efficient Embodied Chain-of-Thought via Thoughts Reuse","url":"https://arxiv.org/html/2506.07639"},{"title":"Tiny-VLA:Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation","url":"https://tiny-vla.github.io/"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"}]

Based on the search results, here's information about EfficientVLA (arXiv 2506.10100):

## Overview

EfficientVLA is a structured and training-free inference acceleration framework that systematically eliminates barriers by cohesively exploiting multifaceted redundancies.

## Key Problem

Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent and inference-time redundancies.

## Core Approach

EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features.

## Results

When applied to a standard VLA model CogACT, EfficientVLA yields a 1.93X inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.

The work was submitted to arXiv on June 11, 2025, by authors including Yantai Yang, Yuhao Wang, and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4289b931-3201-40fd-86ff-c8ac6bbb24db",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "d4523bf2-08e4-4783-a500-1630014d6f12",
  "sourceToolAssistantUUID": "4289b931-3201-40fd-86ff-c8ac6bbb24db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T06:38:27.333Z_

<details><summary>↩ Tool result · `toolu_01LAfeDKV5TnJdxwDNSkgFTs`</summary>

```text
Web search results for query: "SP-VLA arXiv 2506.12723 ICLR 2026 joint scheduling pruning"

Links: [{"title":"[2506.12723] SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/abs/2506.12723"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"Preprint. SP-VLA: A JOINT MODEL SCHEDULING AND TOKEN","url":"https://arxiv.org/pdf/2506.12723"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration | OpenReview","url":"https://openreview.net/forum?id=RwdGIIjPlC"},{"title":"dblp: SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration.","url":"https://dblp.org/rec/journals/corr/abs-2506-12723.html"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.12723v3"},{"title":"(PDF) SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://www.researchgate.net/publication/392736853_SP-VLA_A_Joint_Model_Scheduling_and_Token_Pruning_Approach_for_VLA_Model_Acceleration"},{"title":"GitHub - ChildTang/SP-VLA · GitHub","url":"https://github.com/ChildTang/SP-VLA"},{"title":"Publications - Jiajun Fan","url":"https://www.jiajunfan.com/publications/"},{"title":"GitHub - KwanWaiPang/Awesome-VLA: Paper Survey for Visual Language Action · GitHub","url":"https://github.com/KwanWaiPang/Awesome-VLA"}]

I found information about the SP-VLA paper. Here are the key details:

**Paper Overview:**
SP-VLA is a unified framework that accelerates VLA (Vision-Language-Action) models by jointly scheduling models and pruning tokens.

**Main Problem:**
Vision-Language-Action (VLA) models have attracted increasing attention for their strong control capabilities, but their high computational cost and low execution frequency hinder their suitability for real-time tasks such as robotic manipulation and autonomous navigation.

**Technical Approach:**
The framework includes an action-aware model scheduling mechanism that reduces temporal redundancy by dynamically switching between VLA model and a lightweight generator.

**Authors and Affiliation:**
The paper is authored by Ye Li, Yuan Meng, Zewen Sun, Kangye Ji, Chen Tang, Jiajun Fan, Xinzhu Ma, Shutao Xia, Zhi Wang, and Wenwu Zhu from Tsinghua University, The Chinese University of Hong Kong, University of Illinois at Urbana-Champaign, and Beihang University.

The paper was submitted to arXiv on June 15, 2025 and is also available on OpenReview, suggesting it was submitted to a major conference like ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04ed956b-ac7c-4090-877c-b9823fa63b3e",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "6b385a1d-1226-480f-b502-4883edd148cb",
  "sourceToolAssistantUUID": "04ed956b-ac7c-4090-877c-b9823fa63b3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T06:38:28.990Z_

<details><summary>↩ Tool result · `toolu_01Ds7dq4pcM9RVmJhgQzsjGV`</summary>

```text
Web search results for query: ""Visual Token Compression Enhances Model Robustness" OpenReview"

No links found.

The search didn't return results with that exact phrase. Let me try a broader search:

Links: [{"title":"VISUAL TOKEN COMPRESSION ENHANCES MODEL ...","url":"https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf"},{"title":"Less Is More — Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models","url":"https://arxiv.org/html/2601.12042"},{"title":"Task-Related Token Compression in Multimodal Large Language Models from an Explainability Perspective | OpenReview","url":"https://openreview.net/forum?id=YULeQtSyiW"},{"title":"Vision-centric Token Compression in Large Language Model","url":"https://openreview.net/pdf/0d7442c68e585e718f4a9edb5254177d2345bc5f.pdf"},{"title":"Can visual input Be Compressed? A visual input token compression benchmark for large multimodal models | OpenReview","url":"https://openreview.net/forum?id=Vu7iQO3f9u"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"Less Is More, but Where? Dynamic Token Compression via LLM-Guided","url":"https://openreview.net/pdf/b4a33413bf051e6a2476bdf1b3f34a1cab246ff1.pdf"},{"title":"Vision-centric Token Compression in Large Language Model | OpenReview","url":"https://openreview.net/forum?id=YdggdEL41C"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"DeCo: Decoupling Token Compression from Semantic Abstraction in Multimodal Large Language Models | OpenReview","url":"https://openreview.net/forum?id=Rx5LhMMr0c"}]

I found a paper matching your search query on OpenReview. Here's what I found:

## "Visual Token Compression Enhances Model Robustness"

The paper proposes a visual token compression technique to enhance model robustness against jailbreak attacks and hallucinations. The method filters out-of-distribution visual tokens by measuring the distance between each visual token and the language feature space, and prunes the top r% visual tokens with the largest distances at a selected layer.

**Results:** On jailbreak defense tasks (SafeBench, HADES, and MM-SafetyBench), the approach achieves an average improvement of 13.46% over the Qwen-2.5-VL baseline. For hallucination evaluation on COCO2014 and HallusionBench, the method outperforms Qwen-2.5-VL by 0.23% and 8.00% on CHAIRi and CHAIRs, and by 0.75% on HallusionBench.

The paper is available as a PDF on OpenReview at: https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8329aee1-41b3-4df4-bf79-aca4f01bb9e9",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "0ee9a938-f903-4162-afa9-520d9f682f21",
  "sourceToolAssistantUUID": "8329aee1-41b3-4df4-bf79-aca4f01bb9e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T06:38:30.175Z_

<details><summary>↩ Tool result · `toolu_01S18nnhCoveoygKdCvYouB8`</summary>

```text
Web search results for query: "FastDriveVLA arXiv 2507.23318 AAAI 2026"

Links: [{"title":"[2507.23318] FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning","url":"https://arxiv.org/abs/2507.23318"},{"title":"FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play","url":"https://arxiv.org/pdf/2507.23318"},{"title":"FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning","url":"https://arxiv.org/html/2507.23318"},{"title":"XPENG-Peking University Collaborative Research Accepted by AAAI 2026:","url":"https://www.xpeng.com/news/019b649d31c59b49d00d8a028c720027"},{"title":"XPENG-Peking University Collaborative Research Accepted by AAAI 2026: Introducing a Novel Visual Token Pruning Framework for Autonomous Driving | Press Releases | shipnc.com","url":"https://www.shipnc.com/online_features/press_releases/article_7c5fd3a0-2f28-50f1-b6cf-7f708457ac9f.html"},{"title":"XPENG–Peking University Collaborative Research Accepted By AAAI 2026: Introducing A Novel Visual Token Pruning Framework For Autonomous Driving - CleanTechnica","url":"https://cleantechnica.com/2025/12/28/xpeng-peking-university-collaborative-research-accepted-by-aaai-2026-introducing-a-novel-visual-token-pruning-framework-for-autonomous-driving/"},{"title":"XPENG-Peking University Collaborative Research Accepted by AAAI 2026: Introducing a Novel Visual Token Pruning Framework for Autonomous Driving","url":"https://finance.yahoo.com/news/xpeng-peking-university-collaborative-research-053500417.html"},{"title":"XPeng and Peking University Paper Accepted to AAAI 2026, Proposing Efficient On-Vehicle Large Model Deployment - Pandaily","url":"https://pandaily.com/x-peng-and-peking-university-paper-accepted-to-aaai-2026-proposing-efficient-on-vehicle-large-model-deployment"},{"title":"XPENG-Peking University Collaborative Research Accepted by AAAI 2026: Introducing a Novel Visual Token Pruning Framework for Autonomous Driving","url":"https://www.prnewswire.com/news-releases/xpeng-peking-university-collaborative-research-accepted-by-aaai-2026-introducing-a-novel-visual-token-pruning-framework-for-autonomous-driving-302650038.html"},{"title":"Breakdown of the \"FastDriveVLA\" — AI-Led L4 Autonomous Driving from XPENG & Peking University - CleanTechnica","url":"https://cleantechnica.com/2025/12/29/breakdown-of-the-fastdrivevla-ai-led-l4-autonomous-driving-from-xpeng-peking-university/"}]

Based on the search results, here's what I found about FastDriveVLA (arXiv 2507.23318):

## Overview

FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning has been accepted by AAAI 2026, a major AI conference. The research is a collaboration between XPENG and Peking University.

## The Problem and Solution

Vision-Language-Action (VLA) models have demonstrated significant potential in autonomous driving, but the long visual tokens of VLA models greatly increase computational costs. FastDriveVLA is a novel reconstruction-based vision token pruning framework designed specifically for autonomous driving.

The framework is inspired by how human drivers focus on relevant foreground information (e.g., lanes, vehicles, pedestrians) while ignoring non-critical background areas.

## Key Technical Components

The framework includes a plug-and-play visual token pruner named ReconPruner, which is trained via MAE-style pixel reconstruction and assigned higher saliency scores to visual tokens containing critical foreground information. The team constructed the nuScenes-FG dataset with foreground segmentation annotations, comprising 241k image–mask pairs.

## Performance Results

FastDriveVLA achieved state-of-the-art performance on the nuScenes benchmark, and when visual tokens were reduced from 3,249 to 812, the framework achieved a nearly 7.5x reduction in computational load while maintaining high planning accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a83071d6-48e8-426c-84a2-5568fe2c0573",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "48394d5b-d263-4a2a-a37a-ece136beb4ac",
  "sourceToolAssistantUUID": "a83071d6-48e8-426c-84a2-5568fe2c0573",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-14T06:38:33.084Z_

Now let me fetch detailed information on the most important papers and verify some specific claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48394d5b-d263-4a2a-a37a-ece136beb4ac",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb212TftfMbWUGuQ2fhwd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c265261-0cde-4b45-a2ca-1f21267a5267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Gp2gNWPunbRvsXuwghswJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7935,
      "cache_read_input_tokens": 14609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7935,
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

_source line 35 · 2026-05-14T06:38:35.089Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ALiUmrd6y3hjCic3zf8nD9`</summary>

```json
{
  "url": "https://huggingface.co/blog/smolvla",
  "prompt": "What is the exact parameter count of SmolVLA? Is it exactly 450M? What are the component sizes (vision encoder, language model, etc.)? What datasets is it trained on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c265261-0cde-4b45-a2ca-1f21267a5267",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb212TftfMbWUGuQ2fhwd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca9c82e8-4697-4565-893e-fed04eb5e87c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Gp2gNWPunbRvsXuwghswJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7935,
      "cache_read_input_tokens": 14609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7935,
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

_source line 36 · 2026-05-14T06:38:36.916Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ds7RVdmsnAiFKQThU56otJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.13626",
  "prompt": "What is the exact title of this paper? Is it called LIBERO-Plus? Is it accepted at CVPR 2026? What are its key contributions as a robustness benchmark?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca9c82e8-4697-4565-893e-fed04eb5e87c",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb212TftfMbWUGuQ2fhwd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5576fd1-e5b1-4347-9198-cf6574bd10e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Gp2gNWPunbRvsXuwghswJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7935,
      "cache_read_input_tokens": 14609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7935,
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

_source line 37 · 2026-05-14T06:38:38.807Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016VLWvnv7zWLSLS6d8BQyXY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.22093",
  "prompt": "What is the exact title of this paper? Confirm it is VLA-ADP. Does it do action-trajectory-conditioned pruning? What venue was it published at? Who are the authors?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5576fd1-e5b1-4347-9198-cf6574bd10e1",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb212TftfMbWUGuQ2fhwd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11a4183c-4ef0-4b37-a30f-7437d419f86e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Gp2gNWPunbRvsXuwghswJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7935,
      "cache_read_input_tokens": 14609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7935,
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

_source line 38 · 2026-05-14T06:38:39.728Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V7ftEg4Ewm1PHHP9f59Lni`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.18960",
  "prompt": "What is the exact title of this paper? Is it AVA-VLA? Does it do recurrent visual reweighting? What robustness results does it show? What venue was it published at?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11a4183c-4ef0-4b37-a30f-7437d419f86e",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb212TftfMbWUGuQ2fhwd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf3a2b2f-08ee-4d99-a311-3275a3677d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Gp2gNWPunbRvsXuwghswJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7935,
      "cache_read_input_tokens": 14609,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7935
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 463,
          "cache_read_input_tokens": 14609,
          "cache_creation_input_tokens": 7935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7935,
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

_source line 39 · 2026-05-14T06:38:41.038Z_

<details><summary>↩ Tool result · `toolu_01Ds7RVdmsnAiFKQThU56otJ`</summary>

```text
# Paper Analysis

**Exact Title:** "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"

**Conference Acceptance:** The document does not indicate acceptance at CVPR 2026 or any other venue. This is an arXiv preprint (submitted October 2025, latest version December 2025).

**Key Contributions as a Robustness Benchmark:**

The paper introduces systematic vulnerability testing across seven dimensions: object placement, camera angles, robot starting positions, textual prompts, illumination, surface patterns, and measurement errors.

The authors discovered significant brittleness in state-of-the-art models. Notably, they found that "performance dropping from 95% to below 30% under modest perturbations" when varying camera viewpoints and initial robot states. 

A surprising finding was that models demonstrate "insensitivity to language variations," with evidence suggesting "models tend to ignore language instructions completely."

The work challenges the premise that benchmark performance reflects genuine capability, advocating instead for evaluation methodologies that test "reliability under realistic variation."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5576fd1-e5b1-4347-9198-cf6574bd10e1",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "f3c8f6eb-b525-408c-9f24-805b2a6e558f",
  "sourceToolAssistantUUID": "d5576fd1-e5b1-4347-9198-cf6574bd10e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T06:38:42.145Z_

<details><summary>↩ Tool result · `toolu_016VLWvnv7zWLSLS6d8BQyXY`</summary>

```text
# Paper Analysis

**Exact Title:** "Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation"

**Is it VLA-ADP?** No, not exactly. The acronym used in the paper is "ADP" (Action-aware Dynamic Pruning), though the project website references "vla-adp."

**Action-Trajectory-Conditioned Pruning:** Yes. The paper proposes "a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics."

**Venue:** The document does not specify a published venue. This is a preprint submitted to arXiv on September 26, 2025 (arXiv:2509.22093).

**Authors:** Xiaohuan Pei, Yuxing Chen, Siyu Xu, Yunke Wang, Yuheng Shi, and Chang Xu.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11a4183c-4ef0-4b37-a30f-7437d419f86e",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "34ec93cf-5353-459e-bee7-f6d68f8fb953",
  "sourceToolAssistantUUID": "11a4183c-4ef0-4b37-a30f-7437d419f86e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T06:38:42.536Z_

<details><summary>↩ Tool result · `toolu_01V7ftEg4Ewm1PHHP9f59Lni`</summary>

```text
# Paper Summary

**Exact Title:** "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention"

**Recurrent Visual Reweighting:** Yes. The paper introduces "Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most relevant given both the instruction and execution history."

**Robustness Results:** The document does not discuss robustness testing. Instead, it reports that the model "achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dual-arm manipulation tasks."

**Publication Venue:** "Accepted at CVPR 2026 (Highlight)"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf3a2b2f-08ee-4d99-a311-3275a3677d6b",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "af9b1ce1-f24b-4cd0-ae33-f1d553e7cdc0",
  "sourceToolAssistantUUID": "bf3a2b2f-08ee-4d99-a311-3275a3677d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T06:38:42.954Z_

<details><summary>↩ Tool result · `toolu_01ALiUmrd6y3hjCic3zf8nD9`</summary>

```text
# SmolVLA Parameter Count and Components

## Exact Parameter Count

**SmolVLA-450M is approximately 450M parameters total**, though the blog post doesn't break down the exact distribution. Here's what we know about the components:

### Component Sizes

1. **Vision-Language Model (VLM) Backbone: SmolVLM2-500M**
   - SigLIP vision encoder
   - SmolLM2-1.7B language decoder
   - This is the larger component

2. **Action Expert: ~100M parameters**
   - Compact transformer for action prediction
   - Hidden size reduced to **75% of the VLM's dimension** for efficiency
   - Uses flow matching objective for continuous action prediction

The blog states: *"reduce its hidden size to 75% of the VLM's, keeping the model lightweight for deployment."*

## Training Datasets

SmolVLA is trained on **community-contributed LeRobot datasets** exclusively:

- **487 high-quality curated datasets** focused on the SO100 robotic arm
- **~10 million frames total** (at least 1 order of magnitude smaller than other VLA benchmarks)
- **Standardized at 30 FPS**
- All datasets tagged with `lerobot` on Hugging Face Hub

### Dataset Curation Process

The datasets were selected and refined through:
- Custom filtering by frame count, visual quality, and task coverage
- Manual review for quality assurance
- Task annotation improvement using Qwen2.5-VL-3B-Instruct
- Standardization of camera view naming (OBS_IMAGE_1, OBS_IMAGE_2, etc.)

## Key Efficiency Metrics

Despite using **fewer than 30k training episodes** (order of magnitude less than other VLAs), SmolVLA achieves strong performance through:
- Visual token reduction (64 tokens per frame vs. 1024)
- Layer skipping (using only first half of VLM layers)
- Interleaved cross and self-attention in action expert
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca9c82e8-4697-4565-893e-fed04eb5e87c",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "34d42b45-d2df-4427-976c-3dced87bfc5c",
  "sourceToolAssistantUUID": "ca9c82e8-4697-4565-893e-fed04eb5e87c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-14T06:38:46.683Z_

Now let me verify a few more specific claims -- SP-VLA's ICLR 2026 status, the "Visual Token Compression Enhances Model Robustness" paper details, and check more about LIBERO-Plus at CVPR 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34d42b45-d2df-4427-976c-3dced87bfc5c",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb213QJkx1F8QAxXHHAwt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b86b97b8-7c0b-45f9-80bf-e6761d7be597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo3nqkLH6Vxed1VvqCXvzu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 699,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 22544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

_source line 44 · 2026-05-14T06:38:48.772Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018yEp1AZyL1GqCmr9ZJebwA`</summary>

```json
{
  "url": "https://openreview.net/forum?id=RwdGIIjPlC",
  "prompt": "Is SP-VLA accepted at ICLR 2026? What is its status on OpenReview? What venue is it for?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b86b97b8-7c0b-45f9-80bf-e6761d7be597",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb213QJkx1F8QAxXHHAwt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "216251ec-c510-4d18-bf95-54f17ef072e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo3nqkLH6Vxed1VvqCXvzu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 699,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 22544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

_source line 45 · 2026-05-14T06:38:50.932Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S577duHip1AoKRmTReZLNX`</summary>

```json
{
  "url": "https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf",
  "prompt": "What is the exact title of this paper? Who are the authors? What venue or conference is it submitted to? What are the key findings about visual token compression and robustness?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "216251ec-c510-4d18-bf95-54f17ef072e2",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb213QJkx1F8QAxXHHAwt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bac4e07-ff3c-44d7-b9cc-a5ff09c2d680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo3nqkLH6Vxed1VvqCXvzu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 699,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 22544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

### Tool result

_source line 46 · 2026-05-14T06:38:51.203Z_

<details><summary>↩ Tool result · `toolu_018yEp1AZyL1GqCmr9ZJebwA`</summary>

```text
# SP-VLA Status and Venue

Based on the webpage content:

**Venue:** The paper was submitted to "ICLR 2026 Conference"

**Status:** The paper is listed as an "ICLR 2026 Poster," indicating it has been accepted for presentation at the conference.

**Publication Details:** According to the page, it was "Published: 26 Jan 2026, Last Modified: 11 Apr 2026" and carries a "CC BY 4.0" license. The submission number is 944, and the primary research area is "applications to robotics, autonomy, planning."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "216251ec-c510-4d18-bf95-54f17ef072e2",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "71be21d7-6a79-4df2-9211-d4c4086d18c7",
  "sourceToolAssistantUUID": "216251ec-c510-4d18-bf95-54f17ef072e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T06:38:53.541Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Rn3X8K8z2JqatJN3vCeh6V`</summary>

```json
{
  "url": "https://cvpr.thecvf.com/virtual/2026/poster/38735",
  "prompt": "Confirm that LIBERO-Plus was accepted at CVPR 2026. What is the full title of the paper? Is it listed as a poster?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71be21d7-6a79-4df2-9211-d4c4086d18c7",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb213QJkx1F8QAxXHHAwt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f463e779-73fd-4b87-bbcd-417c27504a51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo3nqkLH6Vxed1VvqCXvzu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 699,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 22544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

_source line 48 · 2026-05-14T06:38:53.556Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018MDYT4uCgWtqEy1wwPkAic`</summary>

```json
{
  "query": "AVA-VLA CVPR 2026 LIBERO+ robustness results perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f463e779-73fd-4b87-bbcd-417c27504a51",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb213QJkx1F8QAxXHHAwt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90b0786a-a046-4478-b173-92e1202ed03b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo3nqkLH6Vxed1VvqCXvzu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 699,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 22544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

_source line 49 · 2026-05-14T06:38:53.635Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016mfiR6FmrVesim7gyUdYBd`</summary>

```json
{
  "query": "SP-VLA ICLR 2026 accepted decision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90b0786a-a046-4478-b173-92e1202ed03b",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb213QJkx1F8QAxXHHAwt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8a52b5d-07bf-454d-9d0d-af09f3f078bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo3nqkLH6Vxed1VvqCXvzu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 699,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 22544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

### Tool result

_source line 50 · 2026-05-14T06:38:56.047Z_

<details><summary>↩ Tool result · `toolu_01Rn3X8K8z2JqatJN3vCeh6V`</summary>

```text
# LIBERO-Plus at CVPR 2026

Yes, LIBERO-Plus was accepted at CVPR 2026 and is listed as a poster presentation.

**Full Title:** "LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models"

The page header explicitly confirms this is a "Poster" submission for CVPR 2026, and the paper is presented by Senyu Fei and eleven co-authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f463e779-73fd-4b87-bbcd-417c27504a51",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "f78a68e6-f761-47d7-9232-4a403e5424c2",
  "sourceToolAssistantUUID": "f463e779-73fd-4b87-bbcd-417c27504a51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T06:38:57.380Z_

<details><summary>↩ Tool result · `toolu_01S577duHip1AoKRmTReZLNX`</summary>

```text
I appreciate your request, but I'm unable to extract the information you're asking for from this document. What you've provided appears to be raw PDF binary data (the linearized PDF file structure with compressed streams), not readable text content.

To properly answer your questions about:
- The exact paper title
- Author names
- Venue/conference details
- Key findings on visual token compression and robustness

I would need the document in a format I can parse, such as:
- Plain text
- Properly rendered PDF text
- HTML or markdown conversion

If you have access to the paper, could you please share it in a more accessible format, or paste the text directly? Alternatively, if you can provide the paper's title or DOI, I'd be happy to help you locate and discuss its findings.

[Binary content (application/pdf, 4.2MB) also saved to /home/ubuntu/.claude-account-2/projects/-/80692553-208e-4dd4-a316-83b41ab9cfa1/tool-results/webfetch-1778740731508-oyi2it.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bac4e07-ff3c-44d7-b9cc-a5ff09c2d680",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "484c9365-1e6b-4670-b331-b48289b929eb",
  "sourceToolAssistantUUID": "9bac4e07-ff3c-44d7-b9cc-a5ff09c2d680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T06:38:58.449Z_

<details><summary>↩ Tool result · `toolu_018MDYT4uCgWtqEy1wwPkAic`</summary>

```text
Web search results for query: "AVA-VLA CVPR 2026 LIBERO+ robustness results perturbation"

Links: [{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2604.18107"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v3"},{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=6mEfYoMRpF"}]

The search results contain comprehensive information about LIBERO-Plus, a robustness benchmark for Vision-Language-Action (VLA) models presented at CVPR 2026. Here are the key findings regarding robustness results under perturbations:

## Key Robustness Findings

LIBERO-Plus introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise, to perform a systematic vulnerability analysis of VLA models.

### Critical Vulnerabilities

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

### Compositional Generalization Issues

While single-dimension perturbations demonstrate some level of robustness, real-world scenarios often involve multiple simultaneous perturbations, where models fail catastrophically. The concept of Compositional Generalization Gap was introduced to quantitatively measure model performance under combined perturbations.

### Related Robustness Methods

The search also reveals related work like ACoT-VLA, which shows pronounced robustness under challenging perturbations like camera-viewpoint shifts and sensor noise.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90b0786a-a046-4478-b173-92e1202ed03b",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "992ac322-f5fa-4b73-bb79-f3072423ab9c",
  "sourceToolAssistantUUID": "90b0786a-a046-4478-b173-92e1202ed03b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T06:38:59.250Z_

<details><summary>↩ Tool result · `toolu_016mfiR6FmrVesim7gyUdYBd`</summary>

```text
Web search results for query: "SP-VLA ICLR 2026 accepted decision"

Links: [{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"ICLR 2026 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"},{"title":"Spatially Guided Training for Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=eKhOrQWAVJ"},{"title":"ICLR 2026 Acceptance Prediction: Tabular ML Approach","url":"https://s-marton.github.io/TabICLR/"},{"title":"Moritz Reuss' Post - State of VLA Research at ICLR 2026","url":"https://www.linkedin.com/posts/moritzreuss_state-of-vla-research-at-iclr-2026-activity-7383813862816546816-V5yD"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"},{"title":"ICLR 2026 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/iclr-statistics/iclr-2026-statistics/"},{"title":"GitHub - PaperDecision/PaperDecision · GitHub","url":"https://github.com/PaperDecision/PaperDecision"},{"title":"GitHub - 2toinf/X-VLA: [ICLR 2026] The offical Implementation of \"Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" · GitHub","url":"https://github.com/2toinf/X-VLA"},{"title":"PaperDecision | Modeling the Complete Peer Review Process","url":"https://paperdecision.netlify.app/"}]

Based on the search results, I found information about SP-VLA and ICLR 2026:

SP-VLA is a dual-system Vision–Language–Action framework that leverages Spatial Priors as a bridge between linguistic instructions and embodiment-specific control. 

SP-VLA aligns action learning with spatial priors through two stages: spatial grounding pre-training and spatially guided action post-training.

SP-VLA achieves substantial improvements over vanilla VLA, with performance increasing from 66.1 to 84.6 on Google Robot and from 54.7 to 73.2 on WidowX, establishing new state-of-the-art results on SimplerEnv.

The paper appears on OpenReview (as of October 8, 2025), which is the review platform for ICLR 2026. However, the search results don't explicitly state the final acceptance decision for SP-VLA. The results show that 164 Vision-Language-Action model submissions were made to ICLR 2026, and SP-VLA is one of the VLA papers submitted, but I cannot confirm from these results whether SP-VLA was specifically accepted or rejected by the conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8a52b5d-07bf-454d-9d0d-af09f3f078bb",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "1967332b-e053-4635-b7a2-b925a8a87367",
  "sourceToolAssistantUUID": "d8a52b5d-07bf-454d-9d0d-af09f3f078bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-14T06:39:07.109Z_

Let me also search for the "Visual Token Compression Enhances Model Robustness" paper more specifically, and verify a couple of remaining details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1967332b-e053-4635-b7a2-b925a8a87367",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb214bwXfJRQAuC9qGmTd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12a4403d-195b-4a76-8512-a8e688d033a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxBgyrWX61JgM7qYHd4HJf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 23512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3543,
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

_source line 55 · 2026-05-14T06:39:07.651Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kiu3D6tVLKBe2ajTVXXRBw`</summary>

```json
{
  "query": "\"Visual Token Compression Enhances Model Robustness\" paper VLM jailbreak hallucination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12a4403d-195b-4a76-8512-a8e688d033a7",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb214bwXfJRQAuC9qGmTd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "046e9ca0-4aaa-4c89-a1c5-1bb64f40bd28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxBgyrWX61JgM7qYHd4HJf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 23512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3543,
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

_source line 56 · 2026-05-14T06:39:08.651Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KCK3FrsoaSsTLitz8Lxw6L`</summary>

```json
{
  "query": "AVA-VLA \"LIBERO+\" robustness benchmark results visual attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "046e9ca0-4aaa-4c89-a1c5-1bb64f40bd28",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb214bwXfJRQAuC9qGmTd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c527eab-c844-4a53-b28e-2c630051fa6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxBgyrWX61JgM7qYHd4HJf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 23512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3543,
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

_source line 57 · 2026-05-14T06:39:09.414Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AFRQMb6SQZut8sk7CVjuw4`</summary>

```json
{
  "query": "EfficientVLA venue conference acceptance NeurIPS ICML 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c527eab-c844-4a53-b28e-2c630051fa6b",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb214bwXfJRQAuC9qGmTd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f57d45e-2ef1-45f4-9752-09f425537963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxBgyrWX61JgM7qYHd4HJf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 23512,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3543
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 23512,
          "cache_creation_input_tokens": 3543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3543,
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

_source line 58 · 2026-05-14T06:39:14.744Z_

<details><summary>↩ Tool result · `toolu_01AFRQMb6SQZut8sk7CVjuw4`</summary>

```text
Web search results for query: "EfficientVLA venue conference acceptance NeurIPS ICML 2025 2026"

Links: [{"title":"2026 Conference","url":"https://icml.cc/"},{"title":"NeurIPS/ICLR/ICML Journal-to-Conference Track","url":"https://neurips.cc/public/JournalToConference"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"The NeurIPS/ICLR/ICML Journal-to-Conference Track","url":"https://iclr.cc/public/JournalToConference"},{"title":"International Conference on Machine Learning - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Machine_Learning"},{"title":"The NeurIPS/ICLR/ICML Journal-to-Conference Track","url":"https://icml.cc/public/JournalToConference"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"2026 Conference","url":"https://neurips.cc/"},{"title":"GitHub - lixin4ever/Conference-Acceptance-Rate: Acceptance rates for the major AI conferences · GitHub","url":"https://github.com/lixin4ever/conference-acceptance-rate"}]

I've completed the web search for your query. The search returned general information about NeurIPS and ICML 2025/2026 conferences, including details about conference dates, deadlines, and acceptance processes. However, the search results do not contain any specific information about "EfficientVLA" or its acceptance to these conferences.

Here's what the search did find:

- ICML 2026 is scheduled for July 6–11, 2026 at the COEX Convention & Exhibition Center, Seoul, South Korea
- NeurIPS 2026 is held December 6-12, 2026 at the International Convention Centre
- ICML 2026 received 24,371 submitted papers, more than doubling the previous year

If you're looking for specific information about EfficientVLA's acceptance status at these venues, you may want to check the official conference proceedings, the authors' affiliated institution announcements, or academic paper repositories like arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f57d45e-2ef1-45f4-9752-09f425537963",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "3e1e1d69-ad08-4759-81c8-c0c8c25967a2",
  "sourceToolAssistantUUID": "6f57d45e-2ef1-45f4-9752-09f425537963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T06:39:15.415Z_

<details><summary>↩ Tool result · `toolu_01Kiu3D6tVLKBe2ajTVXXRBw`</summary>

```text
Web search results for query: ""Visual Token Compression Enhances Model Robustness" paper VLM jailbreak hallucination"

Links: [{"title":"VISUAL TOKEN COMPRESSION ENHANCES MODEL ...","url":"https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"Revisiting Visual Token Pruning for Vision-Language Model ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Endo_Feather_the_Throttle_Revisiting_Visual_Token_Pruning_for_Vision-Language_Model_ICCV_2025_paper.pdf"},{"title":"Lightweight Visual Language Models","url":"https://www.emergentmind.com/topics/lightweight-visual-language-model-vlm"},{"title":"FlashVLM: Text-Guided Visual Token Selection for Large Multimodal Models","url":"https://arxiv.org/html/2512.20561"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering | OpenReview","url":"https://openreview.net/forum?id=7BKcLeHQsm"},{"title":"(PDF) HybridToken-VLM: Hybrid Token Compression for Vision-Language Models","url":"https://www.researchgate.net/publication/398512398_HybridToken-VLM_Hybrid_Token_Compression_for_Vision-Language_Models"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"[2502.03628] The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models via Visual Information Steering","url":"https://arxiv.org/abs/2502.03628"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/html/2410.04417v4"}]

Based on the search results, I found the paper you're looking for. "Visual Token Compression Enhances Model Robustness" is a novel work that investigates how visual token compression influences the robustness of VLMs against jailbreak attacks and hallucinations.

Here are the key findings from the paper:

**Main Contribution:** The paper's goal is to enhance the robustness of VLMs via visual token compression.

**Core Mechanism:** Intrinsically misaligned visual tokens can serve as out-of-distribution inputs, leading VLMs to produce highly uncertain responses. Such uncertainty can render their outputs unpredictable and unreliable, thereby increasing the risk of jailbreak attacks and hallucinations.

**Key Discovery:** The authors identify robust-pruning layers — specific layers where visual token pruning can significantly enhance model robustness against jailbreak attacks and hallucinations. Pruning visual tokens in layers of [13, 17] on SafeBench and [16, 21] on HallusionBench can obviously enhance model robustness.

**Evaluation:** The paper evaluates the effectiveness of their method on various vision-language models using comprehensive multimodal benchmarks that cover tasks such as jailbreak attacks, hallucination assessments, and general VLM capabilities.

The paper appears to have been submitted to OpenReview and presents a training-free approach to improve VLM safety by strategically compressing visual tokens in critical layers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "046e9ca0-4aaa-4c89-a1c5-1bb64f40bd28",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "e7d1abc8-f643-4bd5-8486-c9d089c5ebed",
  "sourceToolAssistantUUID": "046e9ca0-4aaa-4c89-a1c5-1bb64f40bd28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T06:39:15.548Z_

<details><summary>↩ Tool result · `toolu_01KCK3FrsoaSsTLitz8Lxw6L`</summary>

```text
Web search results for query: "AVA-VLA "LIBERO+" robustness benchmark results visual attention"

Links: [{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/html/2511.18960"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"[2511.18960] AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/abs/2511.18960"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.18960v1"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2603.23202v1"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"}]

## Search Results Summary

I found relevant information about AVA-VLA's robustness benchmark results on LIBERO+. Here are the key findings:

### AVA-VLA Performance on LIBERO+ Benchmark

AVA-VLA was evaluated on the LIBERO+ benchmark using models trained on the LIBERO benchmark, with results reported for two different settings: "one policy for all 4 suites" and "one policy per suite".

### Robustness Results

The proposed AVA-VLA method achieves the best total results over the seven perturbation types on two different settings, demonstrating the superiority of the proposed framework. More specifically, the AVA-VLA model exhibits strong robustness under the Light and the Layout perturbations, with the proposed AVA module helping the model enhance the important visual information and reduce the interference of unimportant parts on prediction, thereby improving the model's robustness under visual interference.

### Active Visual Attention Mechanism

The robustness improvements come from the Active Visual Attention (AVA) mechanism. AVA-VLA maintains strong performance even with 50-70% visual token pruning, suggesting that the attention mechanism effectively identifies and retains the most informative visual elements.

### Overall Framework

Extensive experiments show that AVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dual-arm manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c527eab-c844-4a53-b28e-2c630051fa6b",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "4be5e943-e076-4dbc-a711-85b7e03b59d2",
  "sourceToolAssistantUUID": "3c527eab-c844-4a53-b28e-2c630051fa6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-14T06:39:19.666Z_

Let me check for a few more details -- the "Visual Token Compression" paper's venue, and confirm RobustVLA's venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4be5e943-e076-4dbc-a711-85b7e03b59d2",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb215ofzp2AsMrygJDcyk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c250471-cf22-4121-b430-24cbfe8fa487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SEKjxwtxd9EULfJETw6JBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 629,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 27055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2093,
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

_source line 62 · 2026-05-14T06:39:20.692Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Kvnysh9ivd2M7frTvBXWp`</summary>

```json
{
  "query": "\"Visual Token Compression Enhances Model Robustness\" venue conference submission ICML NeurIPS ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c250471-cf22-4121-b430-24cbfe8fa487",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb215ofzp2AsMrygJDcyk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "510a480d-4766-44bd-91bd-e151f8d80671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SEKjxwtxd9EULfJETw6JBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 629,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 27055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2093,
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

_source line 63 · 2026-05-14T06:39:21.238Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G29ayr16wwDYKUgaZnjH42`</summary>

```json
{
  "query": "RobustVLA 2511.01331 venue conference acceptance ICLR ICML NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "510a480d-4766-44bd-91bd-e151f8d80671",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb215ofzp2AsMrygJDcyk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22c99a42-f9a8-4633-aa3d-c9000c6580c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SEKjxwtxd9EULfJETw6JBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 629,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 27055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2093,
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

_source line 64 · 2026-05-14T06:39:21.907Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RDojwJXYLcibwc4yLbg8S8`</summary>

```json
{
  "query": "LIBERO-X arXiv 2602.06556 venue conference acceptance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22c99a42-f9a8-4633-aa3d-c9000c6580c5",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb215ofzp2AsMrygJDcyk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f58e03a-9a3f-4a58-86fd-65a2b1a16140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SEKjxwtxd9EULfJETw6JBa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 629,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 27055,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2093
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 629,
          "output_tokens": 225,
          "cache_read_input_tokens": 27055,
          "cache_creation_input_tokens": 2093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2093,
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

_source line 65 · 2026-05-14T06:39:26.020Z_

<details><summary>↩ Tool result · `toolu_013Kvnysh9ivd2M7frTvBXWp`</summary>

```text
Web search results for query: ""Visual Token Compression Enhances Model Robustness" venue conference submission ICML NeurIPS ICLR 2026"

Links: [{"title":"VISUAL TOKEN COMPRESSION ENHANCES MODEL ...","url":"https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"GitHub - cokeshao/Awesome-Multimodal-Token-Compression: [TMLR 2026] Survey: https://arxiv.org/pdf/2507.20198 · GitHub","url":"https://github.com/cokeshao/Awesome-Multimodal-Token-Compression"},{"title":"An Efficient Token Compression Framework for Visual Object Tracking","url":"https://arxiv.org/html/2605.08329"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"[2605.08329] An Efficient Token Compression Framework for Visual Object Tracking","url":"https://arxiv.org/abs/2605.08329"},{"title":"GitHub - yaolinli/MLLM-Token-Compression: Towards Efficient Multimodal Large Language Models: A Survey on Token Compression · GitHub","url":"https://github.com/yaolinli/MLLM-Token-Compression"},{"title":"A Survey of Token Compression for Efficient Multimodal Large Language Models | OpenReview","url":"https://openreview.net/forum?id=G2od9JVHkE"},{"title":"Efficient Multi-modal Large Language Models via Visual Token Grouping | OpenReview","url":"https://openreview.net/forum?id=ym1dS37mZE"},{"title":"ICLR Poster Prune Redundancy, Preserve Essence: Vision Token Compression in VLMs via Synergistic Importance-Diversity","url":"https://iclr.cc/virtual/2026/poster/10008000"}]

Based on the search results, I found the paper you're looking for:

The paper "Visual Token Compression Enhances Model Robustness" focuses on enhancing the robustness of VLMs via visual token compression. 

According to the search results, the work investigates how visual token compression influences the robustness of VLMs against jailbreak attacks and hallucinations. The research paper is available on OpenReview (https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf).

While I found this specific paper on visual token compression for model robustness, the search results did not explicitly specify which specific 2026 venue (ICML, NeurIPS, or ICLR) this particular paper was submitted to or accepted at. The paper appears to be a recent submission addressing robustness in vision-language models through a novel approach to visual token compression that goes beyond just improving efficiency to directly enhance safety and reliability against adversarial attacks and hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "510a480d-4766-44bd-91bd-e151f8d80671",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "3a2e5ce7-9e06-4a94-92fa-45edfcff6246",
  "sourceToolAssistantUUID": "510a480d-4766-44bd-91bd-e151f8d80671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T06:39:26.421Z_

<details><summary>↩ Tool result · `toolu_01RDojwJXYLcibwc4yLbg8S8`</summary>

```text
Web search results for query: "LIBERO-X arXiv 2602.06556 venue conference acceptance"

Links: [{"title":"[2602.06556] LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.06556"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556"},{"title":"[2105.14838] Does the Venue of Scientific Conferences Leverage their Impact? A Large Scale study on Computer Science Conferences","url":"https://arxiv.org/abs/2105.14838"},{"title":"LIBERO | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3668061"},{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"Submit a Paper List for Conference Proceedings - arXiv info","url":"https://info.arxiv.org/help/submit_index.html"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"Position: The Current AI Conference Model is Unsustainable! Diagnosing the Crisis of Centralized AI Conferences","url":"https://arxiv.org/html/2508.04586v4"}]

Based on the search results, I found information about the LIBERO-X paper with arXiv ID 2602.06556:

LIBERO-X is titled "Robustness Litmus for Vision-Language-Action Models". The paper introduces a benchmark featuring a hierarchical evaluation protocol with progressive difficulty levels targeting three core capabilities: spatial generalization, object recognition, and task instruction understanding, along with a high-diversity training dataset collected via human teleoperation.

However, the search results do not contain information about the venue or conference acceptance status for this paper. The arXiv page shows the paper was posted on February 6, 2026, but does not indicate whether it has been accepted to any conference. To find this information, you may need to check the paper's arXiv abstract page directly or search for more specific conference proceedings information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f58e03a-9a3f-4a58-86fd-65a2b1a16140",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "063e84ae-143a-41d0-ad65-d29840dfc3f3",
  "sourceToolAssistantUUID": "9f58e03a-9a3f-4a58-86fd-65a2b1a16140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-14T06:39:28.617Z_

<details><summary>↩ Tool result · `toolu_01G29ayr16wwDYKUgaZnjH42`</summary>

```text
Web search results for query: "RobustVLA 2511.01331 venue conference acceptance ICLR ICML NeurIPS"

Links: [{"title":"The NeurIPS/ICLR/ICML Journal-to-Conference Track","url":"https://icml.cc/public/JournalToConference"},{"title":"NeurIPS/ICLR/ICML Journal-to-Conference Track","url":"https://neurips.cc/public/JournalToConference"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"Beyond NeurIPS: A Student's Guide to ICML, ICLR, AAAI, and Other AI Conferences | Algoverse AI Research","url":"https://algoverseairesearch.org/blog/icml-iclr-aaai-student-guide"},{"title":"GitHub - lixin4ever/Conference-Acceptance-Rate: Acceptance rates for the major AI conferences · GitHub","url":"https://github.com/lixin4ever/conference-acceptance-rate"},{"title":"International Conference on Machine Learning - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Machine_Learning"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"2022 - Call For Papers","url":"https://iclr.cc/Conferences/2022/CallForPapers"},{"title":"Going To Conferences","url":"https://nn.cs.utexas.edu/advice/GoingToConferences.html"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"}]

The search results returned general information about ICLR, ICML, and NeurIPS conferences and their Journal-to-Conference tracks, but did not contain specific information about the RobustVLA paper (arxiv 2511.01331) or its conference venue acceptance status.

To get more specific information about this paper, I would need to search for it more directly. Let me try another search:

Links: [{"title":"[2511.01331] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.01331"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/397231717_RobustVLA_Robustness-Aware_Reinforcement_Post-Training_for_Vision-Language-Action_Models"},{"title":"[2604.01331] Non-reduced components of global nilpotent cones","url":"https://arxiv.org/abs/2604.01331"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/html/2510.00037v4"},{"title":"[2501.01331] Quasi-parallel anti-sunward propagating whistler waves associated to the electron-deficit in the near-Sun solar wind: Particle-in-Cell simulation","url":"https://arxiv.org/abs/2501.01331"},{"title":"ROBUSTVLA: ROBUSTNESS-AWARE REINFORCE","url":"https://openreview.net/pdf/d2f9e3b68ce76261050b0db5ea64048b5e336142.pdf"},{"title":"[2512.01331] A Fast Heuristic Search Approach for Energy-Optimal Profile Routing for Electric Vehicles","url":"https://arxiv.org/abs/2512.01331"},{"title":"[2509.01331] Comparison between Supervised and Unsupervised Learning in Deep Unfolded Sparse Signal Recovery","url":"https://arxiv.org/abs/2509.01331"}]

Based on the search results, I found information about the RobustVLA paper (arXiv 2511.01331). However, the search results do not contain specific information about the paper's acceptance at ICLR, ICML, or NeurIPS conferences.

RobustVLA is a lightweight online RL post-training method designed to enhance the resilience of Vision-Language-Action (VLA) models, using Jacobian regularization to mitigate sensitivity to observation noise and smoothness regularization to stabilize policies under action perturbations.

The paper appears on arXiv as a preprint (submitted November 3, 2025, with a version update on December 1, 2025). While I found an OpenReview PDF link in the search results, which might indicate submission to a peer-reviewed venue, the search results do not explicitly confirm whether this paper has been accepted to ICLR, ICML, NeurIPS, or another specific conference venue. To find definitive information about its conference acceptance status, you would need to check the official OpenReview pages for these conferences or contact the authors directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22c99a42-f9a8-4633-aa3d-c9000c6580c5",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "bbd7076c-b348-4a7f-a821-83e0b722f614",
  "sourceToolAssistantUUID": "22c99a42-f9a8-4633-aa3d-c9000c6580c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-14T06:39:32.799Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DDNB7c7egNeVzUGDN78dU2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.01331",
  "prompt": "What is the exact title? Who are the authors? Has this paper been accepted at any conference or is it just an arXiv preprint? Does it use Jacobian regularization and smoothness regularization?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbd7076c-b348-4a7f-a821-83e0b722f614",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb216mkvxsVmKzzHav7TL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22881967-f4b0-40ea-bfe7-0b1d326affb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkseBkY7y7nPCkFEQ4Tuax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 766,
      "cache_creation_input_tokens": 3055,
      "cache_read_input_tokens": 29148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3055,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 69 · 2026-05-14T06:39:33.633Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017qn2aFCaS82dSuoqXJJeXn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.06556",
  "prompt": "What is the exact title? Is it LIBERO-X? Who are the authors? Has it been accepted at any conference?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22881967-f4b0-40ea-bfe7-0b1d326affb8",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb216mkvxsVmKzzHav7TL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a9ca7e2-f3af-4022-9b8a-a49b2272ac64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkseBkY7y7nPCkFEQ4Tuax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 766,
      "cache_creation_input_tokens": 3055,
      "cache_read_input_tokens": 29148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3055,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 70 · 2026-05-14T06:39:34.021Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Ax4wbK2RHXfUQ7xJsYDbA`</summary>

```json
{
  "query": "LightVLA arXiv 2509.12594 Gumbel softmax differentiable pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a9ca7e2-f3af-4022-9b8a-a49b2272ac64",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb216mkvxsVmKzzHav7TL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74a02f78-6958-42dd-ba09-08e84774d4ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkseBkY7y7nPCkFEQ4Tuax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 766,
      "cache_creation_input_tokens": 3055,
      "cache_read_input_tokens": 29148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3055,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 71 · 2026-05-14T06:39:36.211Z_

<details><summary>↩ Tool result · `toolu_01DDNB7c7egNeVzUGDN78dU2`</summary>

```text
# RobustVLA Paper Summary

**Exact Title:**
"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models"

**Authors:**
Hongyin Zhang, Shuo Zhang, Junxi Jin, Qixin Zeng, Runze Li, and Donglin Wang

**Publication Status:**
This is an arXiv preprint only. The webpage shows no conference acceptance—it was submitted November 3, 2025, with a revision on December 1, 2025. There is no mention of peer review or conference publication.

**Regularization Methods:**
Yes, the paper employs both techniques mentioned. According to the abstract, the work identifies "two key regularizations: Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22881967-f4b0-40ea-bfe7-0b1d326affb8",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "d89691a2-fd72-4e25-87bd-0e1e649e1210",
  "sourceToolAssistantUUID": "22881967-f4b0-40ea-bfe7-0b1d326affb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T06:39:37.091Z_

<details><summary>↩ Tool result · `toolu_017qn2aFCaS82dSuoqXJJeXn`</summary>

```text
# LIBERO-X Paper Summary

**Exact Title:** "LIBERO-X: Robustness Litmus for Vision-Language-Action Models"

**Authors:** The paper has seven authors: Guodong Wang, Chenkai Zhang, Qingjie Liu, Jinjin Zhang, Jiancheng Cai, Junjie Liu, and Xinmin Liu.

**Conference Acceptance:** The webpage does not indicate acceptance at any conference. The document shows it was submitted to arXiv on February 6, 2026, with submission metadata but no conference publication information. It remains a preprint classified under Computer Vision and Pattern Recognition (cs.CV), Artificial Intelligence (cs.AI), and Robotics (cs.RO) categories.

The paper presents a benchmarking framework for evaluating robustness in vision-language-action models through hierarchical evaluation protocols and diverse training datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a9ca7e2-f3af-4022-9b8a-a49b2272ac64",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "470f0e7f-5e8c-4f3a-b630-be69afd7c7f1",
  "sourceToolAssistantUUID": "4a9ca7e2-f3af-4022-9b8a-a49b2272ac64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-14T06:39:40.560Z_

<details><summary>↩ Tool result · `toolu_014Ax4wbK2RHXfUQ7xJsYDbA`</summary>

```text
Web search results for query: "LightVLA arXiv 2509.12594 Gumbel softmax differentiable pruning"

Links: [{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"},{"title":"LightVLA","url":"https://liauto-research.github.io/LightVLA/"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"AI Bites | YouTube Channel on X: \"LightVLA, a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by https://t.co/bE0Zv0mb0c\" / X","url":"https://x.com/ai_bites/status/1970481721163313156"},{"title":"The Gumbel-Softmax Distribution","url":"https://sassafras13.github.io/GumbelSoftmax/"},{"title":"[1611.01144] Categorical Reparameterization with Gumbel-Softmax","url":"https://arxiv.org/abs/1611.01144"},{"title":"Gumbel-Softmax - Niansong Zhang","url":"https://www.zzzdavid.tech/GumbelSoftmax/"}]

Based on the search results, here's what I found about LightVLA and arXiv paper 2509.12594:

## Overview

LightVLA is a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. The paper is titled "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning".

## Core Approach

LightVLA addresses this challenge through adaptive, performance-driven pruning of visual tokens: It generates dynamic queries to evaluate visual token importance, and adopts Gumbel softmax to enable differentiable token selection. Each query selects a useful token in a differentiable manner using the Gumbel-softmax technique.

## Results

LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.6% improvement in task success rate. LightVLA is the first work to apply adaptive visual token pruning to VLA tasks with the collateral goals of efficiency and performance.

## Key Features

LightVLA requires no heuristic "magic numbers" and introduces no additional trainable parameters, making it compatible with modern inference frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74a02f78-6958-42dd-ba09-08e84774d4ea",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "77be6502-054d-4b03-ade5-6658d5e083f8",
  "sourceToolAssistantUUID": "74a02f78-6958-42dd-ba09-08e84774d4ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-14T06:39:44.708Z_

Now I have comprehensive information on all 12 items. Let me also check one more thing -- the note about LIBERO-Plus at CVPR 2026, since there's a discrepancy in its title.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77be6502-054d-4b03-ade5-6658d5e083f8",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb217ebMacPMGoaA4EhRX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "012558ed-e57a-4a98-aea2-eec3892177b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXP3CsDbwJrjPaEdCNbZ3T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 32203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2482,
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

_source line 75 · 2026-05-14T06:39:46.253Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018My93pe8eWgsRVJBviDYbw`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.18960",
  "prompt": "Does this paper (AVA-VLA) mention LIBERO+ or LIBERO-Plus benchmark? Does it mention robustness results or robustness evaluation? Search for any mention of robustness, perturbation, LIBERO+, LIBERO-Plus in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "012558ed-e57a-4a98-aea2-eec3892177b7",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb217ebMacPMGoaA4EhRX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1affabe1-4597-4975-9c4a-044fbbdb5b99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXP3CsDbwJrjPaEdCNbZ3T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 32203,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2482
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 32203,
          "cache_creation_input_tokens": 2482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2482,
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

_source line 76 · 2026-05-14T06:39:50.581Z_

<details><summary>↩ Tool result · `toolu_018My93pe8eWgsRVJBviDYbw`</summary>

```text
# AVA-VLA Paper: LIBERO+ and Robustness Mentions

Yes, the paper does mention LIBERO+ and robustness evaluation.

## LIBERO+ Mention

The paper acknowledges LIBERO+ in the experimental setup section: "LIBERO+ is a challenging LIBERO-based benchmark, which offers a robust benchmarking framework with 7 perturbation dimensions and 21 sub-dimensions."

The authors conducted additional robustness experiments on this benchmark and state: "We conduct additional experiments on the LIBERO+ benchmark, and the results are put in Appendix D."

## Robustness Results

While detailed robustness findings are referenced as being in Appendix D (labeled "D.3 Robustness on LIBERO+ Benchmark"), the main paper content provided does not include the full appendix details. However, the paper demonstrates commitment to evaluating robustness through systematic perturbation testing across multiple dimensions.

The framework's effectiveness across different conditions is also suggested by its consistent performance gains on challenging scenarios like "LIBERO-Long," described as the most difficult task suite.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1affabe1-4597-4975-9c4a-044fbbdb5b99",
  "isSidechain": true,
  "promptId": "99c64880-afef-4e4d-b6ac-21ce4c23a24e",
  "agentId": "a5b15f23100730701",
  "type": "user",
  "uuid": "251b606d-4322-409b-b158-5a38b2f4c95c",
  "sourceToolAssistantUUID": "1affabe1-4597-4975-9c4a-044fbbdb5b99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-14T06:41:09.314Z_

I now have all the information needed. Here is my comprehensive verification report.

---

## Verification Report: VLA Token Compression & Robustness Papers

### 1. VLA-ADP (arXiv 2509.22093) -- VERIFIED (with caveats)
- **Exists:** Yes. Title: "Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation"
- **Action-trajectory-conditioned pruning:** Confirmed. It uses a gating mechanism conditioned on recent action trajectories to adaptively adjust token retention ratios.
- **Authors:** Xiaohuan Pei, Yuxing Chen, Siyu Xu, Yunke Wang, Yuheng Shi, Chang Xu
- **Venue caveat:** The paper is an arXiv preprint (Sept 2025). No confirmed conference acceptance was found. The GitHub repo uses the name "VLA-ADP" but the paper itself uses just "ADP."
- Sources: [arXiv abs](https://arxiv.org/abs/2509.22093), [GitHub](https://github.com/chen7086/VLA-ADP)

### 2. AVA-VLA (arXiv 2511.18960) -- VERIFIED
- **Exists:** Yes. Title: "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention"
- **Recurrent visual reweighting:** Confirmed. Uses Active Visual Attention (AVA) to dynamically reweight visual tokens conditioned on instruction and execution history via a recurrent belief state.
- **Robustness results:** Confirmed. The paper evaluates on the LIBERO+ benchmark with 7 perturbation dimensions. Shows improved robustness especially on lighting and layout perturbations.
- **Venue:** Accepted at **CVPR 2026 (Highlight)**.
- Sources: [arXiv abs](https://arxiv.org/abs/2511.18960), [arXiv HTML](https://arxiv.org/html/2511.18960)

### 3. LightVLA -- VERIFIED
- **Exists:** Yes. Title: "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning" (arXiv 2509.12594)
- **ICRA 2026:** Confirmed. GitHub repo explicitly states "[ICRA 2026]".
- **Differentiable Gumbel pruning:** Confirmed. Uses Gumbel-softmax for differentiable token selection with dynamic queries evaluating visual token importance.
- **Results:** Reduces FLOPs by 59.1%, latency by 38.2%, with 2.6-2.9% improvement in task success rate.
- Sources: [arXiv abs](https://arxiv.org/abs/2509.12594), [GitHub](https://github.com/LiAutoAD/LightVLA), [Project page](https://liauto-research.github.io/LightVLA/)

### 4. GridS / "See What Matters" -- VERIFIED
- **Exists:** Yes. Title: "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"
- **ICML 2026:** Confirmed. Listed as an ICML 2026 poster (poster ID 65010).
- **Description:** Uses differentiable interpolation to preserve spatial information while achieving compression with fewer than 10% of original visual tokens.
- Source: [ICML 2026 poster page](https://icml.cc/virtual/2026/poster/65010)

### 5. VLA-Cache (NeurIPS 2025) -- VERIFIED
- **Exists:** Yes. Title: "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching" (arXiv 2502.02175)
- **NeurIPS 2025:** Confirmed via NeurIPS virtual poster page and GitHub.
- **Temporal caching:** Confirmed. Training-free method that adaptively caches and reuses static visual tokens across frames, exploiting temporal continuity in robotic manipulation. Includes layer-adaptive token reuse strategy.
- **Results:** Up to 1.7x CUDA latency speedup and 15% increase in control frequency with negligible success rate loss.
- Sources: [NeurIPS 2025 poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/118121), [arXiv](https://arxiv.org/abs/2502.02175), [GitHub](https://github.com/siyuhsu/vla-cache)

### 6. SmolVLA -- VERIFIED
- **Exists:** Yes, in HuggingFace/LeRobot ecosystem.
- **Parameter count ~450M:** Confirmed. SmolVLA-450M is the official designation.
- **Architecture:** Built on SmolVLM2-500M backbone (SigLIP vision encoder + SmolLM2 language decoder) plus a ~100M parameter action expert. Uses flow matching for action prediction, interleaved self/cross-attention, skips half of vision model layers.
- **Training:** Trained on 487 curated LeRobot community datasets (~10M frames, <30k episodes), dramatically less data than comparable VLAs.
- Sources: [HuggingFace blog](https://huggingface.co/blog/smolvla), [HuggingFace docs](https://huggingface.co/docs/lerobot/smolvla), [Model card](https://huggingface.co/lerobot/smolvla_base)

### 7. LIBERO-Plus and LIBERO-X -- PARTIALLY VERIFIED

**LIBERO-Plus (arXiv 2510.13626):**
- **Exists:** Yes. Title: "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"
- **CVPR 2026:** Confirmed. Listed as a CVPR 2026 poster.
- **NOTE:** The CVPR poster title is "LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models" -- slightly different from the arXiv title but the same work.
- **Key finding:** Performance drops from 95% to below 30% under modest perturbations (camera viewpoints, robot initial states). Models largely ignore language instructions.
- Sources: [CVPR 2026 poster](https://cvpr.thecvf.com/virtual/2026/poster/38735), [arXiv](https://arxiv.org/abs/2510.13626), [GitHub](https://github.com/sylvestf/LIBERO-plus)

**LIBERO-X (arXiv 2602.06556):**
- **Exists:** Yes. Title: "LIBERO-X: Robustness Litmus for Vision-Language-Action Models"
- **Venue:** Appears to be an arXiv preprint only (Feb 2026). **No conference acceptance found.** The proposal's claim about a specific venue cannot be verified.
- Sources: [arXiv](https://arxiv.org/abs/2602.06556)

### 8. RobustVLA (arXiv 2511.01331) -- VERIFIED (content), VENUE UNCONFIRMED
- **Exists:** Yes. Title: "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models"
- **Jacobian/smoothness regularization:** Confirmed. Uses Jacobian regularization to mitigate sensitivity to observation noise and smoothness regularization to stabilize policies under action perturbations.
- **Authors:** Hongyin Zhang, Shuo Zhang, Junxi Jin, Qixin Zeng, Runze Li, Donglin Wang
- **Venue:** arXiv preprint only (Nov 2025). An OpenReview PDF exists, suggesting submission to a venue, but no confirmed acceptance was found.
- Sources: [arXiv](https://arxiv.org/abs/2511.01331)

### 9. EfficientVLA (arXiv 2506.10100) -- VERIFIED (content), VENUE UNCONFIRMED
- **Exists:** Yes. Title: "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models"
- **Training-free acceleration:** Confirmed. Integrates three strategies: (1) pruning inconsequential language module layers, (2) task-aware visual token selection, (3) caching in diffusion-based action head.
- **Results:** 1.93x inference speedup, FLOPs reduced to 28.9%, only 0.6% success rate drop on SIMPLER benchmark.
- **Venue:** arXiv preprint (June 2025). Also found on OpenReview. **No confirmed conference acceptance found.**
- Sources: [arXiv](https://arxiv.org/abs/2506.10100), [HuggingFace papers](https://huggingface.co/papers/2506.10100)

### 10. SP-VLA (arXiv 2506.12723) -- VERIFIED (with important caveat)
- **Exists:** Yes, BUT there appears to be a **name collision**. The arXiv paper 2506.12723 is titled "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration" -- this matches the claimed description of joint scheduling + pruning.
- **ICLR 2026:** Confirmed as an **ICLR 2026 Poster** (OpenReview submission 944, published Jan 26, 2026).
- **Joint scheduling + pruning:** Confirmed. Uses action-aware model scheduling to reduce temporal redundancy by switching between VLA model and a lightweight generator, combined with token pruning.
- **Caveat:** There is also a separate "SP-VLA" on OpenReview about "Spatially Guided Training" which is a different paper. Make sure the proposal references the correct one.
- Sources: [arXiv](https://arxiv.org/abs/2506.12723), [OpenReview](https://openreview.net/forum?id=RwdGIIjPlC), [GitHub](https://github.com/ChildTang/SP-VLA)

### 11. "Visual Token Compression Enhances Model Robustness" on OpenReview -- VERIFIED (partially)
- **Exists:** Yes, found as a PDF on OpenReview.
- **Content:** Proposes visual token compression to enhance VLM robustness against jailbreak attacks and hallucinations. Identifies "robust-pruning layers" where token pruning significantly improves robustness. Reports 13.46% average improvement on jailbreak defense benchmarks.
- **Venue:** The specific conference/venue it was submitted to on OpenReview could **not be confirmed**. The PDF is available but no acceptance decision page was found.
- **Important note:** This paper is about VLMs (vision-language models) broadly, not specifically VLA (vision-language-action) models for robotics. If the proposal cites it as VLA-specific, that would be inaccurate.
- Source: [OpenReview PDF](https://openreview.net/pdf/55b90f437cc9c2ca5ac998f826849508b9f0acc2.pdf)

### 12. FastDriveVLA (arXiv 2507.23318) -- VERIFIED
- **Exists:** Yes. Title: "FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning"
- **AAAI 2026:** Confirmed. Widely reported as accepted at AAAI 2026 (XPENG and Peking University collaboration).
- **Approach:** Reconstruction-based vision token pruner (ReconPruner) trained via MAE-style pixel reconstruction. Assigns higher saliency scores to foreground tokens. Achieves ~7.5x computation reduction (3,249 to 812 tokens).
- Sources: [arXiv](https://arxiv.org/abs/2507.23318), [XPENG announcement](https://www.xpeng.com/news/019b649d31c59b49d00d8a028c720027), [CleanTechnica](https://cleantechnica.com/2025/12/28/xpeng-peking-university-collaborative-research-accepted-by-aaai-2026-introducing-a-novel-visual-token-pruning-framework-for-autonomous-driving/)

---

## Summary of Flags / Issues for the Research Proposal

| # | Paper | Exists? | Venue Claimed | Venue Verified? | Content Accurate? |
|---|-------|---------|---------------|-----------------|-------------------|
| 1 | VLA-ADP | Yes | (none claimed?) | arXiv preprint only | Yes |
| 2 | AVA-VLA | Yes | CVPR 2026 | **Yes (Highlight)** | Yes |
| 3 | LightVLA | Yes | ICRA 2026 | **Yes** | Yes |
| 4 | GridS | Yes | ICML 2026 | **Yes** | Yes |
| 5 | VLA-Cache | Yes | NeurIPS 2025 | **Yes** | Yes |
| 6 | SmolVLA | Yes | HuggingFace/LeRobot | **Yes** | Yes (~450M confirmed) |
| 7a | LIBERO-Plus | Yes | CVPR 2026 | **Yes** | Yes |
| 7b | LIBERO-X | Yes | (claimed CVPR 2026?) | **NO -- arXiv preprint only** | Content OK |
| 8 | RobustVLA | Yes | (unclear) | arXiv preprint only | Yes (Jacobian + smoothness) |
| 9 | EfficientVLA | Yes | (unclear) | arXiv preprint only | Yes (training-free) |
| 10 | SP-VLA | Yes | ICLR 2026 | **Yes (Poster)** | Yes -- but beware name collision |
| 11 | Token Compression Robustness | Yes | OpenReview | Venue unclear | Covers VLMs, not VLAs specifically |
| 12 | FastDriveVLA | Yes | AAAI 2026 | **Yes** | Yes |

**Key concerns for the proposal:**
1. **LIBERO-X** has no confirmed conference venue -- if the proposal claims it is at a specific venue, that is unverifiable.
2. **RobustVLA** and **EfficientVLA** appear to be arXiv preprints with no confirmed venue acceptances.
3. **"Visual Token Compression Enhances Model Robustness"** is about general VLMs (jailbreak/hallucination defense), not VLA models for robotics -- the proposal should be careful about how it characterizes this work.
4. **SP-VLA name collision** -- there is a "Spatially Guided" SP-VLA and a "Scheduling + Pruning" SP-VLA. The ICLR 2026 poster is the scheduling+pruning one (2506.12723), which matches the proposal's description.
5. All papers that are confirmed as real do accurately describe the technical methods claimed in the proposal (action-trajectory-conditioned pruning, recurrent visual reweighting, Gumbel pruning, temporal caching, Jacobian regularization, etc.).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "251b606d-4322-409b-b158-5a38b2f4c95c",
  "isSidechain": true,
  "agentId": "a5b15f23100730701",
  "requestId": "req_011Cb218PRpKStHQzi7mk1Bb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f2fc792-7b65-4da5-8055-dfa64a3b9024",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "80692553-208e-4dd4-a316-83b41ab9cfa1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8vvXzeXZ12YEfYBQv8rVP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 34685,
      "output_tokens": 3767,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3767,
          "cache_read_input_tokens": 34685,
          "cache_creation_input_tokens": 452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 452,
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
