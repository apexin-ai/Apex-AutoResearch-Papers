# Research conversation: I need to verify several things for an ML paper review: 1. **AAAI 2027 deadline**: Search for "AAAI 2027 submission dead

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac0a4e9fdc4a9af28.jsonl`
- **Structured JSON:** [`b01a32685ec076620daa.json`](../../sessions/b0/b01a32685ec076620daa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-15T14:33:03.292Z_

I need to verify several things for an ML paper review:

1. **AAAI 2027 deadline**: Search for "AAAI 2027 submission deadline" or "AAAI 2027 call for papers". The proposal claims abstract deadline July 25, paper deadline August 1, 2026. Verify this.

2. **EMNLP 2026 ARR deadline**: Search for "EMNLP 2026 ARR submission deadline May 2026". The user requires targeting EMNLP 2026 with ARR deadline May 25, 2026. Verify whether this deadline exists.

3. **Counter-evidence for temporal attention sink tracking**: Search for:
   - "attention sink static vs dynamic hallucination" — is there evidence that static sink features are already sufficient?
   - "trajectory commitment hallucination first token" — does the trajectory commitment paper's finding (hallucination decided at first token) undermine gradual temporal monitoring?
   - "Before the First Token hallucination arxiv 2604.13068"

4. **TDGNet verification**: Search for "TDGNet temporal dynamic graphs hallucination diffusion language models arxiv 2602.08048"

5. **Attractor Geometry of Transformer Memory arxiv 2605.05686** — verify this exists

6. **Frequency-Aware Attention hallucination arxiv 2602.18145** — verify

Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "1d5557a9-57f0-4801-86fb-334b63b802de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T14:33:03.295Z_

```json
{
  "parentUuid": "1d5557a9-57f0-4801-86fb-334b63b802de",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
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
  "uuid": "86b0ddca-ad40-452d-8e1c-83469a44bf99",
  "timestamp": "2026-05-15T14:33:03.295Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T14:33:05.956Z_



I'll search for all of these in parallel. Let me start by loading the WebSearch tool, then run all the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86b0ddca-ad40-452d-8e1c-83469a44bf99",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X2GKmF84CNvkshHV7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c84e618-94a2-4031-873c-0571755f3b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKjdsgtgZxmWF24x3yWGTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 889,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-15T14:33:06.522Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SXXL6mtBJqPoYypGf2iSx6`</summary>

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
  "parentUuid": "7c84e618-94a2-4031-873c-0571755f3b39",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X2GKmF84CNvkshHV7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6248844-c780-491c-a46a-6324bcf09dde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKjdsgtgZxmWF24x3yWGTm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 8223,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 889
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 107,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 889,
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

_source line 5 · 2026-05-15T14:33:06.526Z_

<details><summary>↩ Tool result · `toolu_01SXXL6mtBJqPoYypGf2iSx6`</summary>

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
  "parentUuid": "a6248844-c780-491c-a46a-6324bcf09dde",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "88d97292-8628-4e17-a4bc-0943328c759e",
  "sourceToolAssistantUUID": "a6248844-c780-491c-a46a-6324bcf09dde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T14:33:09.442Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88d97292-8628-4e17-a4bc-0943328c759e",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X2VgBxJz3ErDnp9svT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f48d9b9a-d980-4bb5-b02d-8e68d753341b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVWWtZgs7ne15JuSUvrhVa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 7 · 2026-05-15T14:33:09.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R2qPkLYxoqbfkPW8G5nz8G`</summary>

```json
{
  "query": "AAAI 2027 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f48d9b9a-d980-4bb5-b02d-8e68d753341b",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X2VgBxJz3ErDnp9svT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ef8e71d-823c-47a9-a87b-b97430ce95dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVWWtZgs7ne15JuSUvrhVa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 8 · 2026-05-15T14:33:10.416Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015JEWAaVFcLLrtjx8HPhWsT`</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ef8e71d-823c-47a9-a87b-b97430ce95dd",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X2VgBxJz3ErDnp9svT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa596351-0aaa-4033-a014-a8db40e34df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVWWtZgs7ne15JuSUvrhVa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 9 · 2026-05-15T14:33:11.351Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SCLgd4GHZJcYF3TKe8Ldwr`</summary>

```json
{
  "query": "attention sink static vs dynamic hallucination language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa596351-0aaa-4033-a014-a8db40e34df1",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X2VgBxJz3ErDnp9svT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a95f32f-3907-4dd1-a782-a626206e2cc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVWWtZgs7ne15JuSUvrhVa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 10 · 2026-05-15T14:33:11.813Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013vzs8i465dStBLrGjJq9au`</summary>

```json
{
  "query": "trajectory commitment hallucination first token language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a95f32f-3907-4dd1-a782-a626206e2cc6",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X2VgBxJz3ErDnp9svT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce2b9e1a-6d32-4554-9ab6-0cd7806f4166",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVWWtZgs7ne15JuSUvrhVa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 11 · 2026-05-15T14:33:12.283Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LtF7erSEBJj2oEugRHk6pR`</summary>

```json
{
  "query": "arxiv 2604.13068 \"Before the First Token\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce2b9e1a-6d32-4554-9ab6-0cd7806f4166",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X2VgBxJz3ErDnp9svT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab10add7-f465-49cc-9e60-ccd7013a1ee5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVWWtZgs7ne15JuSUvrhVa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 12 · 2026-05-15T14:33:13.714Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0192Fw7LavzmVbjkFHq8SEBc`</summary>

```json
{
  "query": "TDGNet temporal dynamic graphs hallucination diffusion language models arxiv 2602.08048"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab10add7-f465-49cc-9e60-ccd7013a1ee5",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X2VgBxJz3ErDnp9svT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88f5a52e-25d7-4d6d-a722-6bc203457ee9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVWWtZgs7ne15JuSUvrhVa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

### Tool result

_source line 13 · 2026-05-15T14:33:13.971Z_

<details><summary>↩ Tool result · `toolu_01R2qPkLYxoqbfkPW8G5nz8G`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline call for papers"

Links: [{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"}]

Based on the search results, here's what I found about AAAI 2027:

AAAI 2027 is being held in Montréal, Québec, Canada on February 16-23, 2027.

Regarding the submission deadline: The AAAI 2027 paper submission deadline is TBD (UTC-12). The official deadline has not yet been announced. However, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

The official AAAI 2027 call for papers is at https://aaai.org/conference/aaai/aaai-27/. You can check that page for the most up-to-date information once the official deadline is announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ef8e71d-823c-47a9-a87b-b97430ce95dd",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "c91e266a-e8ce-4f06-b7fb-d63ccb951160",
  "sourceToolAssistantUUID": "6ef8e71d-823c-47a9-a87b-b97430ce95dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T14:33:14.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GifyyoZbaWbLYGaaDSpGoF`</summary>

```json
{
  "query": "arxiv 2605.05686 \"Attractor Geometry of Transformer Memory\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c91e266a-e8ce-4f06-b7fb-d63ccb951160",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X2VgBxJz3ErDnp9svT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12114e47-6e24-4694-9dfd-8842aeaf7bd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVWWtZgs7ne15JuSUvrhVa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

### Tool result

_source line 15 · 2026-05-15T14:33:15.007Z_

<details><summary>↩ Tool result · `toolu_015JEWAaVFcLLrtjx8HPhWsT`</summary>

```text
Web search results for query: "EMNLP 2026 ARR submission deadline May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"}]

Based on the search results, here's the information about the EMNLP 2026 ARR submission deadline in May 2026:

## EMNLP 2026 ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

### Additional Important Dates:

- Reviewer registration deadline for all authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026
- Camera-ready papers due: September 20, 2026

### Important Policy Note:

Since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time, and this choice will be binding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa596351-0aaa-4033-a014-a8db40e34df1",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "71e0c53d-5c16-4fed-a90a-024507db1d3a",
  "sourceToolAssistantUUID": "aa596351-0aaa-4033-a014-a8db40e34df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T14:33:15.035Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NLPcsijwsWd1SbRZ6VjzxM`</summary>

```json
{
  "query": "arxiv 2602.18145 \"Frequency-Aware Attention\" hallucination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71e0c53d-5c16-4fed-a90a-024507db1d3a",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X2VgBxJz3ErDnp9svT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fe2c354-cadc-4461-b2d1-dcc4526b7af7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVWWtZgs7ne15JuSUvrhVa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 9112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

### Tool result

_source line 17 · 2026-05-15T14:33:16.096Z_

<details><summary>↩ Tool result · `toolu_01LtF7erSEBJj2oEugRHk6pR`</summary>

```text
Web search results for query: "arxiv 2604.13068 "Before the First Token""

Links: [{"title":"[2604.13068] Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models","url":"https://arxiv.org/abs/2604.13068"}]

Here are the search results for arxiv 2604.13068 "Before the First Token":

The paper is titled "Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models".

It was submitted on March 20, 2026, by authors including Dip Roy, Rajiv Misra, Sanjay Kumar Singh, and Anisha Roy.

**Summary of the research:**

The paper examines when hallucination-indicative internal representations peak across autoregressive transformers, studying their temporal dynamics across 7 models ranging from 117M to 7B parameters using three fact-based datasets.

**Key findings:**

The authors identify a scale-dependent phase transition: models below 400M parameters show chance-level probe accuracy at every generation position with no reliable factuality signal, while above ~1B parameters a different regime emerges where peak detectability occurs at position zero—before any tokens are generated—then declines during generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab10add7-f465-49cc-9e60-ccd7013a1ee5",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "a4141276-8441-49e7-b244-f5f3f24282cf",
  "sourceToolAssistantUUID": "ab10add7-f465-49cc-9e60-ccd7013a1ee5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T14:33:19.028Z_

<details><summary>↩ Tool result · `toolu_01NLPcsijwsWd1SbRZ6VjzxM`</summary>

```text
Web search results for query: "arxiv 2602.18145 "Frequency-Aware Attention" hallucination"

Links: [{"title":"[2602.18145] Detecting Contextual Hallucinations in LLMs with Frequency-Aware Attention","url":"https://arxiv.org/abs/2602.18145"},{"title":"Detecting Contextual Hallucinations in Large Language Models with Frequency-Aware Attention","url":"https://arxiv.org/html/2602.18145"}]

I found the research paper you're searching for! Here's what the paper is about:

The paper addresses hallucination detection in large language models (LLMs) in context-based generation. It introduces a frequency-aware perspective on attention by analyzing its variation during generation, modeling attention distributions as discrete signals and extracting high-frequency components that reflect rapid local changes in attention.

The key finding is that hallucinated tokens are associated with high-frequency attention energy, reflecting fragmented and unstable grounding behavior, and the authors develop a lightweight hallucination detector using these high-frequency attention features.

Experiments on the RAGTruth and HalluRAG benchmarks show that their approach achieves performance gains over verification-based, internal-representation-based, and attention-based methods across models and tasks.

The paper was submitted on February 20, 2026, with authors including Siya Qi, Yudong Chen, and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fe2c354-cadc-4461-b2d1-dcc4526b7af7",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "da4173a0-fb71-4f1f-91f8-87c346eae17b",
  "sourceToolAssistantUUID": "4fe2c354-cadc-4461-b2d1-dcc4526b7af7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T14:33:19.578Z_

<details><summary>↩ Tool result · `toolu_01SCLgd4GHZJcYF3TKe8Ldwr`</summary>

```text
Web search results for query: "attention sink static vs dynamic hallucination language models"

Links: [{"title":"Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2604.10697"},{"title":"When Attention Dynamics Matter: Revealing and Enhancing Core Visual Regions for Hallucination Mitigation in LVLMs","url":"https://arxiv.org/html/2602.15556v1"},{"title":"SinkTrack: Attention Sink based Context Anchoring for Large Language Models","url":"https://arxiv.org/html/2604.10027"},{"title":"Catch Me if You Search: When Contextual Web Search Results Affect the Detection of Hallucinations","url":"https://arxiv.org/html/2504.01153v4"},{"title":"[2604.10697] Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/abs/2604.10697"},{"title":"Catch me if you search: When contextual web search results affect the detection of hallucinations - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0747563225002109"},{"title":"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/html/2602.21704v1"},{"title":"[2604.10027] SinkTrack: Attention Sink based Context Anchoring for Large Language Models","url":"https://arxiv.org/abs/2604.10027"},{"title":"Detecting Contextual Hallucinations in Large Language Models with Frequency-Aware Attention","url":"https://arxiv.org/html/2602.18145"},{"title":"Attention Sink Phenomenon in Transformers","url":"https://www.emergentmind.com/topics/attention-sink-phenomenon"}]

Based on the search results, here's what I found about attention sink static vs dynamic approaches in relation to hallucination in language models:

## Key Distinction: Static vs Dynamic Approaches

Static internal signal enhancement methods are often vulnerable to the attention sink phenomenon, while researchers have been developing dynamic alternatives that are more effective.

### Dynamic Approaches

Internal Positive Attention Dynamics (PAD) in LVLMs naturally reveal semantically core visual regions under the distortions of attention sinks. PAD provides a more reliable signal for identifying semantically core visual regions than static attention maps, by leveraging the model's internal attention evolution.

Similarly, a static intervention approach would be insufficient for hallucination mitigation, as it cannot account for the semantic-dependent nature of hallucinations, which directly motivates dynamic multimodal activation steering methods that can adaptively select appropriate steering vectors based on the semantic content of the input query.

### Limitations of Static Design

Static designs reveal fundamental limitations—their performance is contingent on manually tuned hyperparameters, restricting applicability. Furthermore, by uniformly aggregating all contextual information, they lack the capacity to adaptively select the most salient content, and this indiscriminate fusion can introduce noise and degrade performance.

### Detection of Hallucinations Using Attention Sinks

On the detection side, hallucinations are deeply entangled with attention sinks—tokens that accumulate disproportionate attention mass during generation—indicating a transition from distributed, input-grounded attention to compressed, prior-dominated computation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a95f32f-3907-4dd1-a782-a626206e2cc6",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "9a43d7d5-5870-4095-bff1-6411936de888",
  "sourceToolAssistantUUID": "3a95f32f-3907-4dd1-a782-a626206e2cc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T14:33:19.644Z_

<details><summary>↩ Tool result · `toolu_013vzs8i465dStBLrGjJq9au`</summary>

```text
Web search results for query: "trajectory commitment hallucination first token language models"

Links: [{"title":"[2604.15400] Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/abs/2604.15400"},{"title":"[2604.13068] Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models","url":"https://arxiv.org/abs/2604.13068"},{"title":"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/html/2605.13772"},{"title":"A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3703155"},{"title":"Hallucination Detection via Internal States and Structured Reasoning Consistency in Large Language Models","url":"https://arxiv.org/html/2510.11529v1"},{"title":"Hallucinations in LLMs Are Not a Bug in the Data | Towards Data Science","url":"https://towardsdatascience.com/hallucinations-in-llms-are-not-a-bug-in-the-data/"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"First Hallucination Tokens Are Different from Conditional Ones","url":"https://arxiv.org/html/2507.20836v4"},{"title":"[2505.11741] MTRE: Multi-Token Reliability Estimation for Hallucination Detection in VLMs","url":"https://arxiv.org/abs/2505.11741"},{"title":"AgentHallu: Benchmarking Automated Hallucination Attribution of LLM-based Agents","url":"https://arxiv.org/html/2601.06818"}]

Here are the key research findings from your search on trajectory commitment hallucination and first token dynamics in language models:

## Main Research on Trajectory Commitment and Hallucination

Hallucination in autoregressive language models is an early trajectory commitment governed by asymmetric attractor dynamics. Using bifurcation analysis, researchers found that on Qwen2.5-1.5B, 27 prompts (44.3%) bifurcate with factual and hallucinated trajectories diverging at the first generated token.

Activation patching reveals a pronounced causal asymmetry: injecting a hallucinated activation into a correct trajectory corrupts output in 87.5% of trials (layer 20), while the reverse recovers only 33.3% (layer 24). This asymmetry suggests hallucinations create stable attractor states that are difficult to escape once entered.

## First Token Signals

Above ~1B parameters, peak hallucination signal detectability occurs at position zero—before any tokens are generated—then declines during generation, with this pre-generation signal statistically significant in both Pythia-1.4B and Qwen2.5-7B.

Additionally, the first hallucinated token is far more detectable than later ones, and this structural property holds across models, suggesting that first hallucination tokens play a key role in token-level hallucination detection.

## Mechanistic Insights

Hallucination can be characterized as a locally stable attractor basin: entry is probabilistic and rapid, exit demands coordinated intervention across layers and steps, and the relevant basins are selected by clusterable regimes already discernible at step 0.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce2b9e1a-6d32-4554-9ab6-0cd7806f4166",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "bfe0feca-3f22-49c1-8409-5eb198200304",
  "sourceToolAssistantUUID": "ce2b9e1a-6d32-4554-9ab6-0cd7806f4166",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T14:33:20.311Z_

<details><summary>↩ Tool result · `toolu_0192Fw7LavzmVbjkFHq8SEBc`</summary>

```text
Web search results for query: "TDGNet temporal dynamic graphs hallucination diffusion language models arxiv 2602.08048"

Links: [{"title":"TDGNet: Hallucination Detection in Diffusion Language Models via Temporal Dynamic Graphs","url":"https://arxiv.org/html/2602.08048v1"},{"title":"[2602.08048] TDGNet: Hallucination Detection in Diffusion Language Models via Temporal Dynamic Graphs","url":"https://arxiv.org/abs/2602.08048"},{"title":"TDGNet: Hallucination Detection in Diffusion Language ...","url":"https://arxiv.org/pdf/2602.08048"},{"title":"GitHub - VILA-Lab/Awesome-DLMs: The official GitHub repo for the survey paper \"A Survey on Diffusion Language Models\". · GitHub","url":"https://github.com/VILA-Lab/Awesome-DLMs"},{"title":"Temporal Graph Network: Hallucination Detection in Multi-Turn Conversation","url":"https://arxiv.org/html/2601.03051v1"},{"title":"Unifying Text Semantics and Graph Structures for Temporal Text-attributed Graphs with Large Language Models","url":"https://arxiv.org/html/2503.14411v1"},{"title":"Time Is a Feature: Exploiting Temporal Dynamics in Diffusion Language Models","url":"https://arxiv.org/html/2508.09138v1"},{"title":"[2601.03051] Temporal Graph Network: Hallucination Detection in Multi-Turn Conversation","url":"https://arxiv.org/abs/2601.03051"},{"title":"Grounding the Ungrounded: A Spectral-Graph Framework for Quantifying Hallucinations in multimodal LLMs","url":"https://arxiv.org/html/2508.19366v1"},{"title":"[2006.10637] Temporal Graph Networks for Deep Learning on Dynamic Graphs","url":"https://arxiv.org/abs/2006.10637"}]

Based on the search results, I found detailed information about the paper you're looking for:

TDGNet is a temporal dynamic graph framework that formulates hallucination detection as learning over evolving token-level attention graphs. Diffusion language models (D-LLMs) offer parallel denoising and bidirectional context, but hallucination detection for D-LLMs remains underexplored.

At each denoising step, the framework sparsifies the attention graph and updates per-token memories via message passing, then applies temporal attention to aggregate trajectory-wide evidence for final prediction.

The paper visualizes four diffusion dynamics that confound static baselines: Self-Correction, Correctness Decay and Semantic Drift, and Persistent Error, and TDGNet aggregates structural signals across the trajectory sequences to distinguish these evolving patterns.

Experiments on LLaDA-8B and Dream-7B across QA benchmarks show consistent AUROC improvements over output-based, latent-based, and static-graph baselines, with single-pass inference and modest overhead.

The paper was published on February 8, 2026, and addresses the important problem of detecting hallucinations in diffusion-based language models by explicitly modeling temporal patterns in token interactions during the denoising process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88f5a52e-25d7-4d6d-a722-6bc203457ee9",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "58b82f04-2425-482e-9f11-481cae158542",
  "sourceToolAssistantUUID": "88f5a52e-25d7-4d6d-a722-6bc203457ee9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T14:33:22.789Z_

<details><summary>↩ Tool result · `toolu_01GifyyoZbaWbLYGaaDSpGoF`</summary>

```text
Web search results for query: "arxiv 2605.05686 "Attractor Geometry of Transformer Memory""

Links: [{"title":"[2605.05686] Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/abs/2605.05686"},{"title":"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/html/2605.05686"},{"title":"[2605.12466] Solve the Loop: Attractor Models for Language and Reasoning","url":"https://arxiv.org/abs/2605.12466"},{"title":"The Bayesian Geometry of Transformer Attention","url":"https://arxiv.org/html/2512.22471v1"},{"title":"Understanding and controlling the geometry of memory organization in RNNs","url":"https://arxiv.org/html/2502.07256v1"},{"title":"Transformers learn factored representations","url":"https://arxiv.org/html/2602.02385v1"},{"title":"Revisiting Transformer Layer Parameterization Through Causal Energy Minimization","url":"https://arxiv.org/html/2605.07588"},{"title":"Back to the Continuous Attractor","url":"https://arxiv.org/html/2408.00109v2"},{"title":"Self-attention as an attractor network: transient memories without backpropagation M. N. acknowledges the support of PNRR MUR Project No. PE0000013-FAIR.","url":"https://arxiv.org/html/2409.16112v1"},{"title":"[2605.07721] Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models","url":"https://arxiv.org/abs/2605.07721"}]

I found the paper! Here's what I found about arxiv 2605.05686:

## "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination"

**Authors:** Qiyao Liang (MIT), Risto Miikkulainen (University of Texas Austin), and Ila Fiete (MIT)

**Submission Date:** May 7, 2026

**Main Research Focus:**

Language models draw on two knowledge sources: facts baked into weights (parametric memory, PM) and information in context (working memory, WM). The paper studies two mechanistically distinct failure modes--conflict, when PM and WM disagree and interfere; and hallucination, when the queried fact was never learned.

**Key Findings:**

In the hidden-state space of autoregressive generation, learned facts form attractor basins. Conflict is basin competition: WM disrupts convergence to the correct basin without raising output entropy. Hallucination is basin absence: the hidden state drifts freely when no memorized basin exists.

**Methodology and Results:**

The paper verifies this account in a controlled synthetic task—entity identifiers mapped to unique codes with PM installed via LoRA adapters—where geometric margin reads the geometry directly and separates correct recall from hallucination far more cleanly than output entropy.

The paper can be accessed at https://arxiv.org/abs/2605.05686.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12114e47-6e24-4694-9dfd-8842aeaf7bd7",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "438b2f05-a3bd-4d64-8eaa-98a82d60eea8",
  "sourceToolAssistantUUID": "12114e47-6e24-4694-9dfd-8842aeaf7bd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T14:33:26.006Z_

Let me get more precise details on the AAAI 2027 deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "438b2f05-a3bd-4d64-8eaa-98a82d60eea8",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X3hPfxKwutirs5zK4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b02215a3-c495-492a-af51-3dac94e22b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RcuGDevoykfHjPsbq6UAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 382,
      "cache_creation_input_tokens": 6078,
      "cache_read_input_tokens": 11028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6078,
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

_source line 24 · 2026-05-15T14:33:27.907Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F684DKhb87NYfxqk7TkwAd`</summary>

```json
{
  "url": "https://www.getpaperpilot.com/deadlines/aaai-2027.html",
  "prompt": "What are the exact submission deadlines for AAAI 2027? List the abstract deadline, full paper deadline, and any other key dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b02215a3-c495-492a-af51-3dac94e22b13",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X3hPfxKwutirs5zK4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff6570e4-e36f-4fe7-b9f6-c9d8d1a9c73c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RcuGDevoykfHjPsbq6UAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 382,
      "cache_creation_input_tokens": 6078,
      "cache_read_input_tokens": 11028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6078,
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

_source line 25 · 2026-05-15T14:33:29.027Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017kQGLLi5pYyeVsceDxhCqZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.13068",
  "prompt": "Extract the full title, authors, and submission date of this paper. Also summarize the key finding about hallucination signals appearing before the first token."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff6570e4-e36f-4fe7-b9f6-c9d8d1a9c73c",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X3hPfxKwutirs5zK4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f233cd1-a7ed-4c3a-b939-69142bb699de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RcuGDevoykfHjPsbq6UAe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 382,
      "cache_creation_input_tokens": 6078,
      "cache_read_input_tokens": 11028,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6078
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 382,
          "output_tokens": 237,
          "cache_read_input_tokens": 11028,
          "cache_creation_input_tokens": 6078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6078,
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

_source line 26 · 2026-05-15T14:33:30.064Z_

<details><summary>↩ Tool result · `toolu_01F684DKhb87NYfxqk7TkwAd`</summary>

```text
# AAAI 2027 Submission Deadlines

Based on the provided content, the specific submission deadlines for AAAI 2027 have not yet been finalized. The page indicates that "Paper deadline TBD (UTC-12)" and "Abstract deadline TBD (UTC-12)."

**Confirmed dates:**
- Conference dates: February 16-23, 2027
- Location: Montréal, Québec, Canada

The official call for papers is available at https://aaai.org/conference/aaai/aaai-27/, where the deadlines will be announced once they are determined.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff6570e4-e36f-4fe7-b9f6-c9d8d1a9c73c",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "ff771876-5033-4708-9232-678852f81948",
  "sourceToolAssistantUUID": "ff6570e4-e36f-4fe7-b9f6-c9d8d1a9c73c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T14:33:33.333Z_

<details><summary>↩ Tool result · `toolu_017kQGLLi5pYyeVsceDxhCqZ`</summary>

```text
# Paper Details

**Full Title:** "Detection Without Correction: A Robust Asymmetry in Activation-Based Hallucination Probing"

**Authors:** Dip Roy, Rajiv Misra, Sanjay Kumar Singh, and Anisha Roy

**Submission Date:** March 20, 2026 (v1); revised May 9, 2026 (v2)

## Key Finding on Pre-Token Hallucination Signals

The research demonstrates that probe-derived signals can detect hallucination indicators "at position zero (before any output tokens are produced)," enabling what the authors call "pre-generation flagging." This temporal advantage is statistically significant in two of the seven models tested (Pythia-1.4B and Qwen2.5-7B), distinguishing activation-based probes from output-confidence methods that can only operate after tokens are generated. However, this signal is absent in smaller models below 400M parameters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f233cd1-a7ed-4c3a-b939-69142bb699de",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "8d099cb9-1099-43ce-922a-b1317035e6c2",
  "sourceToolAssistantUUID": "6f233cd1-a7ed-4c3a-b939-69142bb699de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T14:33:36.137Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011W8vHRtCnTtQc79o5qLg65`</summary>

```json
{
  "url": "http://aideadlines.org/conference/?id=aaai27",
  "prompt": "What are the exact submission deadlines for AAAI 2027? List abstract deadline and paper deadline with exact dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d099cb9-1099-43ce-922a-b1317035e6c2",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X4TzYT2FQhooiGvoAc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "927c0b28-07b8-478e-aef8-b238398e7387",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EY2iGHemW364vEyVY83fKq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 17106,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 17106,
          "cache_creation_input_tokens": 1039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1039,
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

_source line 29 · 2026-05-15T14:33:36.580Z_

<details><summary>↩ Tool result · reported error · `toolu_011W8vHRtCnTtQc79o5qLg65`</summary>

```text
ECONNREFUSED
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "927c0b28-07b8-478e-aef8-b238398e7387",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "320c0497-d03a-40f8-a89e-864c384750ec",
  "toolUseResult": "Error: ECONNREFUSED",
  "sourceToolAssistantUUID": "927c0b28-07b8-478e-aef8-b238398e7387",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T14:33:38.874Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TsTofnR6nivXWh4DbVa7JM`</summary>

```json
{
  "query": "AAAI 2027 abstract deadline \"July 2026\" paper deadline \"August 2026\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "320c0497-d03a-40f8-a89e-864c384750ec",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X4htTxrVhn2HY6TVUn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd230d7d-0a5a-4766-b1bc-5612a8e0653d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X19ySfJEXptkDR6fY3VWFp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 135,
      "cache_read_input_tokens": 18145,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 135
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 18145,
          "cache_creation_input_tokens": 135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 135,
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

_source line 31 · 2026-05-15T14:33:42.584Z_

<details><summary>↩ Tool result · `toolu_01TsTofnR6nivXWh4DbVa7JM`</summary>

```text
Web search results for query: "AAAI 2027 abstract deadline "July 2026" paper deadline "August 2026""

Links: [{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"},{"title":"MPC Deadlines Hub","url":"https://mpc-deadlines.github.io/"},{"title":"The 40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"}]

Based on the search results, I found the AAAI 2027 submission deadlines:

For AAAI-27, abstracts are due July 21, 2026 and full papers are due July 28, 2026. The conference will be held February 16–February 23, 2027 in Montréal, Canada.

Note that the actual deadlines are slightly different from the dates you mentioned in your query (July 21 for abstracts instead of July 2026 generally, and July 28 for papers instead of August 2026). All deadlines are "anywhere on earth" (UTC-12).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd230d7d-0a5a-4766-b1bc-5612a8e0653d",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "c6f535d6-fb9a-48c9-8b16-520310191d58",
  "sourceToolAssistantUUID": "dd230d7d-0a5a-4766-b1bc-5612a8e0653d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T14:33:45.600Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0141bWy6dQ6UGKuCE3mAy8Tg`</summary>

```json
{
  "url": "https://aaai.org/conference/aaai/aaai-27/",
  "prompt": "Extract the exact submission deadlines for AAAI 2027 - abstract deadline, paper deadline, and all other important dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6f535d6-fb9a-48c9-8b16-520310191d58",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X59eWoisEn5KwcpyFP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da616fc4-5845-4c3f-9358-20c0bb6d8b31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1iTfEBVPdG6HnyACCd1P9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 18280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 728,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 33 · 2026-05-15T14:33:46.298Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011XqYFWceGL4Hg3kCFqA7pC`</summary>

```json
{
  "url": "https://trybibby.com/conference-deadlines",
  "prompt": "Find the AAAI 2027 submission deadlines - abstract deadline and paper/full submission deadline. Report exact dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da616fc4-5845-4c3f-9358-20c0bb6d8b31",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X59eWoisEn5KwcpyFP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c33d6e4-0eb1-4be5-ade9-2ed25af3d6a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1iTfEBVPdG6HnyACCd1P9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 18280,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 728
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 18280,
          "cache_creation_input_tokens": 728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 728,
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

_source line 34 · 2026-05-15T14:33:49.642Z_

<details><summary>↩ Tool result · `toolu_0141bWy6dQ6UGKuCE3mAy8Tg`</summary>

```text
# AAAI-27 Submission Deadlines

Based on the conference information provided, here are the key submission deadlines for AAAI-27 (February 16-23, 2027):

**Registration & Submission Opening:**
- June 17, 2026: "Open Review submission site opens for author registration"
- June 24, 2026: "Open Review submission site opens for paper submission"

**Submission Deadlines:**
- July 21, 2026: "Abstracts due at 11:59 PM UTC-12"
- July 28, 2026: "Full papers due at 11:59 PM UTC-12"
- July 31, 2026: "Supplementary material and code due by 11:59 PM UTC-12"

**Review & Notification Timeline:**
- September 24, 2026: Notification of Phase 1 rejections
- October 19-25, 2026: Author feedback window
- November 30, 2026: "Notification of final acceptance or rejection (Main Technical Track)"
- December 14, 2026: Camera-ready file submission deadline

**Important Note:** The page indicates that "Deadlines are track-specific and may differ from those listed above," so authors should verify deadlines for their specific submission track.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da616fc4-5845-4c3f-9358-20c0bb6d8b31",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "d99428c9-3578-400c-9e2a-32e67a03bca8",
  "sourceToolAssistantUUID": "da616fc4-5845-4c3f-9358-20c0bb6d8b31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T14:33:50.925Z_

<details><summary>↩ Tool result · `toolu_011XqYFWceGL4Hg3kCFqA7pC`</summary>

```text
# AAAI 2027 Submission Deadlines

Based on the conference deadlines page, AAAI 2027 has two submission phases:

**Abstract Deadline:**
- "Abstract in 71d:21h:26m:11s" from the page timestamp
- **Due: July 26, 2026 at 11:59 AM UTC**

**Full Paper Deadline:**
- "Full Paper in 78d:21h:26m:11s" from the page timestamp
- **Due: August 2, 2026 at 11:59 AM UTC**

**Conference Details:**
The conference itself takes place February 16–23, 2027 in Montréal, Canada. The event is categorized under "AIA" (Artificial Intelligence) in the conference registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c33d6e4-0eb1-4be5-ade9-2ed25af3d6a3",
  "isSidechain": true,
  "promptId": "bc2bb4b2-dfb0-4c24-9c86-9e54eefca217",
  "agentId": "ac0a4e9fdc4a9af28",
  "type": "user",
  "uuid": "bf709997-f3de-4ab5-a3bf-1996e014fa6a",
  "sourceToolAssistantUUID": "5c33d6e4-0eb1-4be5-ade9-2ed25af3d6a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-15T14:34:37.761Z_

Good. Now I have all the information needed. The official AAAI source gives the most authoritative dates. Let me compile the findings.

Here are the consolidated findings for each item:

---

## 1. AAAI 2027 Deadline

**The proposal's claimed dates are INCORRECT.**

Per the official AAAI-27 page at [aaai.org/conference/aaai/aaai-27/](https://aaai.org/conference/aaai/aaai-27/):

| Milestone | Official Date | Proposal's Claim |
|---|---|---|
| Abstract deadline | **July 21, 2026** (11:59 PM UTC-12) | July 25, 2026 |
| Full paper deadline | **July 28, 2026** (11:59 PM UTC-12) | August 1, 2026 |
| Supplementary material | July 31, 2026 | (not mentioned) |

The proposal overstates both deadlines by 4 days. The submission site opens June 24, 2026. Note: one third-party tracker (trybibby.com) showed different dates (July 26 / Aug 2), likely using a different timezone convention. The official AAAI site is authoritative.

---

## 2. EMNLP 2026 ARR Deadline

**CONFIRMED.** The ARR submission deadline for EMNLP 2026 is **May 25, 2026**, matching the proposal's claim exactly. This was confirmed via the [official EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/) and the [EMNLP 2026 Twitter/X announcement](https://x.com/emnlpmeeting/status/2029508292637061462).

Important caveat: EMNLP and AACL share the ARR May cycle, so authors must select a target conference at submission time, and the choice is binding.

---

## 3. Counter-Evidence for Temporal Attention Sink Tracking

### 3a. Static vs. Dynamic Attention Sinks

There is **relevant literature on both sides**, but the evidence does **not** straightforwardly show that static features are "already sufficient":

- [Attention Sinks as Internal Signals for Hallucination Detection (arXiv:2604.10697)](https://arxiv.org/abs/2604.10697) shows that hallucinations are entangled with attention sinks (tokens accumulating disproportionate attention), indicating a transition from distributed to compressed computation. This supports monitoring sink dynamics.
- [When Attention Dynamics Matter (arXiv:2602.15556)](https://arxiv.org/html/2602.15556v1) demonstrates that **dynamic** attention analysis (PAD) reveals semantically core regions more reliably than static maps, arguing against static-only approaches.
- [Dynamic Multimodal Activation Steering (arXiv:2602.21704)](https://arxiv.org/html/2602.21704v1) explicitly argues static intervention is insufficient because it cannot account for semantic-dependent hallucination patterns.

**Verdict:** The literature actually favors dynamic over static approaches, which would support (not undermine) temporal monitoring proposals.

### 3b. "Before the First Token" (arXiv:2604.13068)

**CONFIRMED to exist.** Full title: *"Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models"* by Dip Roy, Rajiv Misra, Sanjay Kumar Singh, and Anisha Roy. Submitted March 20, 2026.

Key finding: Above ~1B parameters, peak hallucination signal detectability occurs at **position zero** (before any tokens are generated), then declines during generation. Below ~400M parameters, no reliable signal exists at any position.

**This does represent potential counter-evidence** for gradual temporal monitoring: if hallucination is largely decided before generation begins, continuous temporal tracking during generation may be less useful than pre-generation detection.

### 3c. Trajectory Commitment

The paper [*"Hallucination as Trajectory Commitment"* (arXiv:2604.15400)](https://arxiv.org/abs/2604.15400) finds that factual and hallucinated trajectories diverge at the **first generated token** in 44.3% of cases, and hallucinations create stable attractor states that are hard to escape (87.5% corruption rate when injecting hallucinated activations vs. only 33.3% recovery the other way). This **does challenge** gradual temporal monitoring, since the "damage" is often done at step 0/1 and subsequent monitoring may be too late to intervene.

---

## 4. TDGNet (arXiv:2602.08048)

**CONFIRMED to exist.** Full title: *"TDGNet: Hallucination Detection in Diffusion Language Models via Temporal Dynamic Graphs"*. Published February 8, 2026. It formulates hallucination detection as learning over evolving token-level attention graphs in diffusion language models (D-LLMs), using message passing at each denoising step and temporal attention for trajectory-wide aggregation. Tested on LLaDA-8B and Dream-7B with AUROC improvements over static baselines.

Paper: [arxiv.org/abs/2602.08048](https://arxiv.org/abs/2602.08048)

---

## 5. Attractor Geometry of Transformer Memory (arXiv:2605.05686)

**CONFIRMED to exist.** Full title: *"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination"* by Qiyao Liang (MIT), Risto Miikkulainen (UT Austin), and Ila Fiete (MIT). Submitted May 7, 2026.

Key finding: Learned facts form attractor basins in hidden-state space. Conflict (PM vs. WM disagreement) = basin competition. Hallucination (unlearned fact) = basin absence, where hidden state drifts freely.

Paper: [arxiv.org/abs/2605.05686](https://arxiv.org/abs/2605.05686)

---

## 6. Frequency-Aware Attention (arXiv:2602.18145)

**CONFIRMED to exist.** Full title: *"Detecting Contextual Hallucinations in LLMs with Frequency-Aware Attention"* by Siya Qi, Yudong Chen, et al. Submitted February 20, 2026.

Key finding: Hallucinated tokens are associated with high-frequency attention energy (fragmented, unstable grounding). A lightweight detector using high-frequency attention features outperforms verification-based, internal-representation, and attention-based baselines on RAGTruth and HalluRAG benchmarks.

Paper: [arxiv.org/abs/2602.18145](https://arxiv.org/abs/2602.18145)

---

## Summary

| Item | Status |
|---|---|
| AAAI 2027 deadlines | **INCORRECT in proposal** -- abstract is July 21 (not 25), paper is July 28 (not Aug 1) |
| EMNLP 2026 ARR May 25 | **Confirmed correct** |
| arXiv:2604.13068 (Before the First Token) | **Exists** -- potential counter-evidence to gradual monitoring |
| Trajectory Commitment (2604.15400) | **Exists** -- supports "hallucination decided early" thesis |
| Static vs. Dynamic sinks | Literature favors dynamic approaches (supports, not undermines, temporal monitoring) |
| TDGNet (2602.08048) | **Exists and verified** |
| Attractor Geometry (2605.05686) | **Exists and verified** |
| Frequency-Aware Attention (2602.18145) | **Exists and verified** |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf709997-f3de-4ab5-a3bf-1996e014fa6a",
  "isSidechain": true,
  "agentId": "ac0a4e9fdc4a9af28",
  "requestId": "req_011Cb4X5mG9EBz55WF4eoakH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b097995-f4fa-40dd-bf3c-a7d7736be6ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "72b372b1-b1c8-4d03-9826-6e7e6ce63e9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtzG8khjCWvS5WvcHx6vTN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 19008,
      "output_tokens": 1927,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 752
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1927,
          "cache_read_input_tokens": 19008,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 752,
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
