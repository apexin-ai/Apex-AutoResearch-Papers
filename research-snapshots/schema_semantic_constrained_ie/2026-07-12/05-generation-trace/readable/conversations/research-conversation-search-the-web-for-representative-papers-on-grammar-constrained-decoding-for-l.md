# Research conversation: Search the web for representative papers on grammar-constrained decoding for LLMs (2023-2026). I need 4-5 key papers cov

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ab33888ae5255d2f0.jsonl`
- **Structured JSON:** [`2c1ad62f555008eb9ac6.json`](../../sessions/2c/2c1ad62f555008eb9ac6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-14T02:35:32.706Z_

Search the web for representative papers on grammar-constrained decoding for LLMs (2023-2026). I need 4-5 key papers covering:

1. **XGrammar** - the system for grammar-guided structured generation (likely from MLSys or similar venue)
2. **Guidance** (Microsoft) - constrained generation framework
3. **Outlines** (2024) - structured text generation with regular expressions/CFGs
4. **LMQL** - query language for LLMs with constraints
5. **SGLang** or other notable grammar-constrained decoding systems

For each paper, find:
- Full title
- Authors (first 2-3)
- Venue and year
- Core method in 1-2 sentences
- ArXiv ID if available

Also search for any survey papers on constrained decoding for LLMs (2024-2026).

Report all findings in a structured format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "e316cf3f-1143-4fc9-b1ed-cf701c464bcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T02:35:32.710Z_

```json
{
  "parentUuid": "e316cf3f-1143-4fc9-b1ed-cf701c464bcf",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "5b1fb58d-1d3f-4018-a9a6-270357222b27",
  "timestamp": "2026-05-14T02:35:32.710Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T02:35:35.007Z_



I'll search for each of these papers systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b1fb58d-1d3f-4018-a9a6-270357222b27",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gVuSyCUNeh9C95UVsm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65ae6849-931a-4d90-8e2d-6975c1f4de4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ezn5nqWFjfmogPZMqPbma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14280,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14280,
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

_source line 4 · 2026-05-14T02:35:35.564Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CAqRAhjiNaMeBVAZW2fnty`</summary>

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
  "parentUuid": "65ae6849-931a-4d90-8e2d-6975c1f4de4b",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gVuSyCUNeh9C95UVsm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29a50233-b68d-4b5a-9b05-c01cca625a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ezn5nqWFjfmogPZMqPbma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14280,
      "cache_read_input_tokens": 0,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14280
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 14280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14280,
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

_source line 5 · 2026-05-14T02:35:35.569Z_

<details><summary>↩ Tool result · `toolu_01CAqRAhjiNaMeBVAZW2fnty`</summary>

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
  "parentUuid": "29a50233-b68d-4b5a-9b05-c01cca625a86",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "76cc704e-aad9-422c-b567-dbe126a0ee19",
  "sourceToolAssistantUUID": "29a50233-b68d-4b5a-9b05-c01cca625a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T02:35:40.286Z_



I'll search for all these papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76cc704e-aad9-422c-b567-dbe126a0ee19",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gW7GsRpMGyp2YrBHwW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e7bef33-9444-4021-a288-6ec35e3a93d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gy5BddbBrQRCQpsB5S5Vgj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 14280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1452,
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

_source line 7 · 2026-05-14T02:35:40.721Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PW86jo9jWorkJQ2q2EyG8r`</summary>

```json
{
  "query": "XGrammar grammar-guided structured generation LLM paper arxiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e7bef33-9444-4021-a288-6ec35e3a93d6",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gW7GsRpMGyp2YrBHwW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9589331-d145-4806-b21f-76526130d8cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gy5BddbBrQRCQpsB5S5Vgj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 14280,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 14280,
          "cache_creation_input_tokens": 1452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1452,
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

_source line 8 · 2026-05-14T02:35:46.549Z_

<details><summary>↩ Tool result · `toolu_01PW86jo9jWorkJQ2q2EyG8r`</summary>

```text
Web search results for query: "XGrammar grammar-guided structured generation LLM paper arxiv 2024 2025"

Links: [{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"[PDF] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGrammar:-Flexible-and-Efficient-Structured-Engine-Dong-Ruan/274ca059ee4997f1e008bc8962aef3d22897f17a"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"[2411.15100v1] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.15100v1"},{"title":"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/html/2601.04426"},{"title":"Guided Decoding and Its Critical Role in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.06631v1"},{"title":"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241115100D/abstract"},{"title":"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/xgrammar-flexible-efficient-structured-generation-engine-large"}]

Based on the search results, here's what I found about XGrammar:

## XGrammar Paper Overview

XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models is an arXiv paper (2411.15100) published in November 2024.

### Key Technical Approach

XGrammar accelerates context-free grammar execution by dividing the vocabulary into context-independent tokens that can be prechecked and context-dependent tokens that need to be interpreted during runtime. The system builds transformations to expand the grammar context and reduce the number of context-independent tokens, and features an efficient persistent stack to accelerate context-dependent token checks.

### Performance

Evaluation results show that XGrammar can achieve up to 100x speedup over existing solutions. Combined with an LLM inference engine, it can generate near-zero overhead structure generation in end-to-end low-LLM serving.

### Authors and Availability

The paper was authored by Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ruihang Lai, Ziyi Xu, Yilong Zhao, and Tianqi Chen. XGrammar has been officially integrated into SGLang (2024/11), MLC-LLM (2024/11), vLLM (2024/12), and TensorRT-LLM (2025/01).

### Related Work

There's also a follow-up work: XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs, which was published in 2026 (arxiv 2601.04426).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9589331-d145-4806-b21f-76526130d8cf",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "55ac0cb2-42cf-4c28-8910-cf8cf76a42d1",
  "sourceToolAssistantUUID": "b9589331-d145-4806-b21f-76526130d8cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T02:35:49.335Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M4yMXt1oU8op26awJds2GG`</summary>

```json
{
  "query": "Outlines structured text generation regular expressions CFG paper arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55ac0cb2-42cf-4c28-8910-cf8cf76a42d1",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gWuw2A336EYVAbKiFS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2949887b-bcb9-4494-bff3-0f2274905e0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmhZDYT2YTKdaa4XGidSuB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 15732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1017,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 10 · 2026-05-14T02:35:50.328Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RiE6LwDN82jtgMRdubKsN9`</summary>

```json
{
  "query": "Microsoft Guidance constrained generation framework LLM paper arxiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2949887b-bcb9-4494-bff3-0f2274905e0a",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gWuw2A336EYVAbKiFS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f7a8b1c-8116-4177-8cef-7bcc276ca9e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmhZDYT2YTKdaa4XGidSuB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 15732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1017,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 11 · 2026-05-14T02:35:50.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VvKxQgp93RHiJHJ3tXZcDd`</summary>

```json
{
  "query": "LMQL query language LLM constraints paper arxiv 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f7a8b1c-8116-4177-8cef-7bcc276ca9e4",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gWuw2A336EYVAbKiFS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d949d34e-f239-42e7-ba9c-d9e4a4fad241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmhZDYT2YTKdaa4XGidSuB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 15732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1017,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 12 · 2026-05-14T02:35:51.170Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W9Xtij5bC2u9hXFic61Nry`</summary>

```json
{
  "query": "SGLang structured generation language LLM paper arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d949d34e-f239-42e7-ba9c-d9e4a4fad241",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gWuw2A336EYVAbKiFS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8be0f8fe-e22d-42e2-8d20-57035e4e92b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmhZDYT2YTKdaa4XGidSuB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 15732,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1017
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 15732,
          "cache_creation_input_tokens": 1017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1017,
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

_source line 13 · 2026-05-14T02:35:56.315Z_

<details><summary>↩ Tool result · `toolu_01W9Xtij5bC2u9hXFic61Nry`</summary>

```text
Web search results for query: "SGLang structured generation language LLM paper arxiv 2024"

Links: [{"title":"[2312.07104] SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/abs/2312.07104"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/pdf/2312.07104"},{"title":"SGLang: efficient execution of structured language model ...","url":"https://dl.acm.org/doi/10.5555/3737916.3739916"},{"title":"Paper page - Efficiently Programming Large Language Models using SGLang","url":"https://huggingface.co/papers/2312.07104"},{"title":"Efficiently Programming Large Language Models using SGLang","url":"https://arxiv.org/html/2312.07104v1"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs | Request PDF","url":"https://www.researchgate.net/publication/397203117_SGLang_Efficient_Execution_of_Structured_Language_Model_Programs"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs | OpenReview","url":"https://openreview.net/forum?id=VqkAKQibpq"},{"title":"GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub","url":"https://github.com/sgl-project/sglang"},{"title":"Efficiently programming large language models using SGLang | Awesome Papers","url":"https://paper.lingyunyang.com/reading-notes/miscellaneous/arxiv/2024/sglang"},{"title":"[PDF] SGLang: Efficient Execution of Structured Language Model Programs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SGLang:-Efficient-Execution-of-Structured-Language-Zheng-Yin/eb95c327260725498404eb43ec370d419b8d92c7"}]

Based on the search results, I found comprehensive information about the SGLang paper. Here's what I found:

## SGLang Paper Overview

SGLang is a system for efficient execution of complex language model programs. SGLang consists of a frontend language and a runtime, with the frontend simplifying programming with primitives for generation and parallelism control.

## Key Components and Optimizations

The runtime accelerates execution with novel optimizations like RadixAttention for KV cache reuse and compressed finite state machines for faster structured output decoding. SGLang is introduced as a domain-specific language embedded in Python.

## Performance Results

Experiments show that SGLang achieves up to 6.4x higher throughput compared to state-of-the-art inference systems on various large language and multi-modal models on tasks including agent control, logical reasoning, few-shot learning benchmarks, JSON decoding, retrieval-augmented generation pipelines, and multi-turn chat.

## Publication Details

The paper was originally submitted on December 12, 2023 as arXiv preprint 2312.07104, with an updated version in June 2024. The paper was accepted by NeurIPS 2024. The code is publicly available at https://github.com/sgl-project/sglang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8be0f8fe-e22d-42e2-8d20-57035e4e92b6",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "a526f840-e2c9-4328-acb1-76835bfbbb2d",
  "sourceToolAssistantUUID": "8be0f8fe-e22d-42e2-8d20-57035e4e92b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T02:35:56.904Z_

<details><summary>↩ Tool result · `toolu_01M4yMXt1oU8op26awJds2GG`</summary>

```text
Web search results for query: "Outlines structured text generation regular expressions CFG paper arxiv 2024"

Links: [{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.15100v1"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"[2307.09702v2] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v2"},{"title":"[2307.09702v1] Efficient Guided Generation for LLMs","url":"https://arxiv.org/abs/2307.09702v1"},{"title":"GitHub - dottxt-ai/outlines: Structured Outputs · GitHub","url":"https://github.com/dottxt-ai/outlines"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"[2309.10447] Toward Unified Controllable Text Generation via Regular Expression Instruction","url":"https://arxiv.org/abs/2309.10447"},{"title":"[2404.13919] Navigating the Path of Writing: Outline-guided Text Generation with Large Language Models","url":"https://arxiv.org/abs/2404.13919"},{"title":"[2404.13919v1] Navigating the Path of Writing: Outline-guided Text Generation with Large Language Models","url":"https://arxiv.org/abs/2404.13919v1"}]

Based on the search results, I found several relevant papers and resources on structured text generation using regular expressions and context-free grammars (CFGs):

## Key Papers and Resources

**1. Efficient Guided Generation for Large Language Models (2023)**

This paper describes an efficient approach to guiding language model text generation with regular expressions and context-free grammars, adding little to no overhead to the token sequence generation process, with an implementation provided in the open source Python library Outlines.

**2. XGrammar: Flexible and Efficient Structured Generation (2024)**

This recent paper compares constrained generation libraries including Outlines, the grammar engine in llama.cpp, and lm-format-enforcer (a regex-based method that does not support CFG). Context-free grammar (CFG) provides a general approach for defining structures through a set of rules, with each rule containing a sequence of characters or other rules, allowing recursive composition to represent complex structures, and offering greater flexibility than regular expressions by allowing recursive structures suitable for describing languages such as JSON, SQL, and domain-specific languages.

**3. Generating Structured Outputs from Language Models: Benchmark and Studies (2025)**

Recent constrained-decoding frameworks include Guidance, Outlines, XGrammar and the grammar module of Llamacpp, which provide broad support for different types of constraints, minimal overhead, and compatibility with various LM ecosystems.

The search results reveal active research in 2024-2025 on optimizing structured text generation with various constraint specification methods, with CFGs being particularly useful for complex recursive structures compared to simpler regex-based approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2949887b-bcb9-4494-bff3-0f2274905e0a",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "8c3e28c2-2599-4d78-8078-44fee6d00cbd",
  "sourceToolAssistantUUID": "2949887b-bcb9-4494-bff3-0f2274905e0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T02:35:57.293Z_

<details><summary>↩ Tool result · `toolu_01RiE6LwDN82jtgMRdubKsN9`</summary>

```text
Web search results for query: "Microsoft Guidance constrained generation framework LLM paper arxiv 2024 2025"

Links: [{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/html/2403.06988v1"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"},{"title":"[2403.06988] Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/abs/2403.06988"},{"title":"GitHub - guidance-ai/guidance: A guidance language for controlling large language models. · GitHub","url":"https://github.com/guidance-ai/guidance"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"guidance | control LM output – Microsoft Research","url":"https://www.microsoft.com/en-us/research/project/guidance-control-lm-output/"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Published as a conference paper at ICLR 2025 GUARANTEED GENERATION FROM","url":"https://openreview.net/pdf?id=8roRgrjbjv"}]

Based on the search results, I found several relevant papers related to Microsoft's Guidance framework and constrained generation for LLMs:

## Key Papers Found:

1. **"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation"** (2024)
   - The paper proposes Domino, a novel constrained decoding algorithm that enforces context-free grammars in a minimally-invasive way, which is highly efficient and can even increase throughput of LLM inference over unconstrained generation by leveraging pre-computation and speculative decoding
   - ArXiv ID: 2403.06988

2. **Microsoft Guidance Library**
   - Guidance is an open-source Python library for controlling outputs of any language model, allowing developers to express in Python the precise programmatic constraints the model must follow for structured output in JSON, Python, HTML, SQL, etc.
   - Fundamentally different from conventional prompting techniques, Guidance enforces constraints by steering the model token by token in the inference layer to deliver accurate outputs

3. **Recent Benchmarking Work** (2025)
   - A benchmark evaluates six state-of-the-art constrained decoding frameworks including Guidance, Outlines, Llamacpp, XGrammar, OpenAI, and Gemini, providing insights into the capabilities and limitations of constrained decoding on structured generation with real-world JSON schemas

The search results indicate that Guidance is a mature framework with significant community adoption, and recent research continues to advance constrained decoding techniques for LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f7a8b1c-8116-4177-8cef-7bcc276ca9e4",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "4754f85f-f123-4e2c-8db7-e8e8792ec397",
  "sourceToolAssistantUUID": "6f7a8b1c-8116-4177-8cef-7bcc276ca9e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T02:35:57.489Z_

<details><summary>↩ Tool result · `toolu_01VvKxQgp93RHiJHJ3tXZcDd`</summary>

```text
Web search results for query: "LMQL query language LLM constraints paper arxiv 2023"

Links: [{"title":"[2212.06094] Prompting Is Programming: A Query Language for Large Language Models","url":"https://arxiv.org/abs/2212.06094"},{"title":"Prompting Is Programming: A Query Language for Large Language Models 1","url":"https://arxiv.org/pdf/2212.06094"},{"title":"LMQL is a programming language for LLM interaction. | LMQL","url":"https://lmql.ai/"},{"title":"GitHub - eth-sri/lmql: A language for constraint-guided and efficient LLM programming. · GitHub","url":"https://github.com/eth-sri/lmql"},{"title":"Better Steering LLM Agents with LMQL | Unsupervised Thoughts","url":"https://vivien000.github.io/blog/journal/better-steering-LLM-agents-with-LMQL.html"},{"title":"LMQL — SQL for Language Models","url":"https://medium.com/data-science/lmql-sql-for-language-models-d7486d88c541"},{"title":"Large Language Models are Zero-Shot Multi-Tool Users","url":"https://files.sri.inf.ethz.ch/website/papers/lmql_actions.pdf"},{"title":"LMQL - SQL for Language Models | Towards Data Science","url":"https://towardsdatascience.com/lmql-sql-for-language-models-d7486d88c541/"},{"title":"Research | LMQL","url":"https://lmql.ai/research/index.html"},{"title":"Prompting Is Programming: A Query Language for Large Language Models | Proceedings of the ACM on Programming Languages","url":"https://dl.acm.org/doi/10.1145/3591300"}]

Based on the search results, I found the paper you're looking for:

## LMQL: A Query Language for Large Language Models

The paper is titled "Prompting Is Programming: A Query Language for Large Language Models", with arXiv ID 2212.06094. The paper was initially submitted on December 12, 2022, and updated versions were released on April 26, 2023, and May 30, 2023.

### Paper Overview

The paper presents Language Model Programming (LMP), which generalizes language model prompting from pure text prompts to an intuitive combination of text prompting and scripting, and allows constraints to be specified over the language model output.

To enable LMP, the authors implement LMQL (Language Model Query Language), which leverages the constraints and control flow from an LMP prompt to generate an efficient inference procedure that minimizes the number of expensive calls to the underlying language model.

### Key Results

The evaluation shows that LMQL retains or increases the accuracy on several downstream tasks, while also significantly reducing the required amount of computation or cost in the case of pay-to-use APIs (26-85% cost savings).

### Authors

The paper was written by Luca Beurer-Kellner, Marc Fischer, and Martin Vechev.

The paper is available on arXiv at https://arxiv.org/abs/2212.06094, and LMQL is now actively maintained as an open-source project.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d949d34e-f239-42e7-ba9c-d9e4a4fad241",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "e1be3bd1-dfb1-417e-9f0d-082738d582ef",
  "sourceToolAssistantUUID": "d949d34e-f239-42e7-ba9c-d9e4a4fad241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-14T02:36:00.590Z_

Now let me get more details on the authors and venues for the papers I still need specifics on.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1be3bd1-dfb1-417e-9f0d-082738d582ef",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gXih829Ym5mgicyMLh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d556b57e-aa7a-4902-8844-5dc2a3eca068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179Xt1dTSpioKNpcQ6qdwVs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 16749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2763,
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

_source line 18 · 2026-05-14T02:36:01.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K8EE7Cnqbe7GYuyw4KBgBu`</summary>

```json
{
  "query": "Outlines \"Efficient Guided Generation for LLMs\" arxiv 2307.09702 authors venue ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d556b57e-aa7a-4902-8844-5dc2a3eca068",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gXih829Ym5mgicyMLh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "216a75d2-1943-435e-b69e-63fa81635de1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179Xt1dTSpioKNpcQ6qdwVs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 16749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2763,
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

_source line 19 · 2026-05-14T02:36:02.541Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015jpNJMc3Uoh9KC77gWWYRe`</summary>

```json
{
  "query": "SGLang paper authors \"Lianmin Zheng\" NeurIPS 2024 arxiv 2312.07104"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "216a75d2-1943-435e-b69e-63fa81635de1",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gXih829Ym5mgicyMLh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67858f65-69a6-4a67-a1c1-f7f6ce1b2f2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179Xt1dTSpioKNpcQ6qdwVs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 16749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2763,
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

_source line 20 · 2026-05-14T02:36:03.069Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012e4eK6Gt5H2CvaNh1MyTxH`</summary>

```json
{
  "query": "survey constrained decoding LLM structured generation 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67858f65-69a6-4a67-a1c1-f7f6ce1b2f2e",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gXih829Ym5mgicyMLh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "462b648f-2210-44b1-8ca6-ebabae59988b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179Xt1dTSpioKNpcQ6qdwVs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 16749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2763,
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

_source line 21 · 2026-05-14T02:36:03.999Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017GzL7xvVz7bkhrinkpdjdn`</summary>

```json
{
  "query": "\"Guiding LLMs The Right Way\" Domino authors venue 2403.06988 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "462b648f-2210-44b1-8ca6-ebabae59988b",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gXih829Ym5mgicyMLh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09ae1aaf-d7ad-4600-8eb6-6f27e877bdc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179Xt1dTSpioKNpcQ6qdwVs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 16749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2763,
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

_source line 22 · 2026-05-14T02:36:06.774Z_

<details><summary>↩ Tool result · `toolu_015jpNJMc3Uoh9KC77gWWYRe`</summary>

```text
Web search results for query: "SGLang paper authors "Lianmin Zheng" NeurIPS 2024 arxiv 2312.07104"

Links: [{"title":"[2312.07104] SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/abs/2312.07104"},{"title":"Efficiently programming large language models using SGLang | Awesome Papers","url":"https://paper.lingyunyang.com/reading-notes/miscellaneous/arxiv/2024/sglang"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/pdf/2312.07104"},{"title":"Paper page - Efficiently Programming Large Language Models using SGLang","url":"https://huggingface.co/papers/2312.07104"},{"title":"Sglang: Efficient execution of structured language model programs | Stanford MAST Lab","url":"https://mast.stanford.edu/pubs/sglang_efficient_execution_of_structured_language_model_programs/"},{"title":"[PDF] SGLang: Efficient Execution of Structured Language Model Programs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SGLang:-Efficient-Execution-of-Structured-Language-Zheng-Yin/eb95c327260725498404eb43ec370d419b8d92c7"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs | OpenReview","url":"https://openreview.net/forum?id=VqkAKQibpq"},{"title":"NeurIPS Poster SGLang: Efficient Execution of Structured Language Model Programs","url":"https://neurips.cc/virtual/2024/poster/94872"},{"title":"SGLang: Efficient Execution of Structured Language Model ...","url":"http://theory.stanford.edu/~barrett/pubs/ZYX+24-abstract.html"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/724be4472168f31ba1c9ac630f15dec8-Abstract-Conference.html"}]

Based on the search results, I found comprehensive information about the SGLang paper:

## SGLang Paper Details

The authors of the SGLang paper are: Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Chuyue Sun, Jeff Huang, Cody Hao Yu, Shiyi Cao, Christos Kozyrakis, Ion Stoica, Joseph E. Gonzalez, Clark Barrett, and Ying Sheng.

**Publication Information:**
- The paper was accepted by NeurIPS 2024
- ArXiv identifier: 2312.07104

**Paper Overview:**
SGLang is a system for efficient execution of complex language model programs that consists of a frontend language and a runtime. The frontend simplifies programming with primitives for generation and parallelism control, while the runtime accelerates execution with novel optimizations like RadixAttention for KV cache reuse and compressed finite state machines for faster structured output decoding.

The authors are affiliated with UC Berkeley and Stanford, and the code is publicly available at https://github.com/sgl-project/sglang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67858f65-69a6-4a67-a1c1-f7f6ce1b2f2e",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "2ff1ba07-d10f-4e8b-bb65-59d90cb76392",
  "sourceToolAssistantUUID": "67858f65-69a6-4a67-a1c1-f7f6ce1b2f2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T02:36:07.876Z_

<details><summary>↩ Tool result · `toolu_01K8EE7Cnqbe7GYuyw4KBgBu`</summary>

```text
Web search results for query: "Outlines "Efficient Guided Generation for LLMs" arxiv 2307.09702 authors venue ICML 2024"

Links: [{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"Efficient Guided Generation for LLMs Brandon T. Willard1 and R´emi Louf2","url":"https://arxiv.org/pdf/2307.09702v1"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"[2307.09702v1] Efficient Guided Generation for LLMs","url":"https://arxiv.org/abs/2307.09702v1"},{"title":"(PDF) Efficient Guided Generation for LLMs","url":"https://www.researchgate.net/publication/372468267_Efficient_Guided_Generation_for_LLMs"},{"title":"[2307.09702v3] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v3"},{"title":"[2307.09702v2] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v2"},{"title":"GitHub - dottxt-ai/outlines: Structured Outputs · GitHub","url":"https://github.com/dottxt-ai/outlines"}]

Based on the search results, here's the information about "Efficient Guided Generation for LLMs":

## Paper Overview

**Authors:** Brandon T. Willard and Rémi Louf

**arXiv ID:** 2307.09702 (Submitted on July 19, 2023)

## Main Contribution

The paper shows how neural text generation can be reformulated in terms of transitions between states of a finite-state machine, leading to an efficient approach to guiding text generation with regular expressions and context-free grammars.

## Key Features

The approach is model agnostic, allows enforcement of domain-specific knowledge and constraints, and enables construction of reliable interfaces by guaranteeing the structure of generated text.

The method uses finite state machine formulation of regular expressions to arbitrarily start and stop guided generation, with an algorithm that scales as O(1) on average.

The FSM approach can be extended to context-free grammars (CFGs) and LALR(1) parsers to allow efficient guided generation according to popular data formats and programming languages like JSON, Python, and SQL.

## Implementation

An implementation is provided in the open source Python library Outlines.

**Note:** The search results do not contain information about an ICML 2024 venue publication. The paper was published on arXiv in July 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "216a75d2-1943-435e-b69e-63fa81635de1",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "5bd6a6f3-a181-4a75-a7e9-84ebb3e6931b",
  "sourceToolAssistantUUID": "216a75d2-1943-435e-b69e-63fa81635de1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T02:36:07.972Z_

<details><summary>↩ Tool result · `toolu_017GzL7xvVz7bkhrinkpdjdn`</summary>

```text
Web search results for query: ""Guiding LLMs The Right Way" Domino authors venue 2403.06988 2024"

Links: [{"title":"[2403.06988] Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/abs/2403.06988"},{"title":"2403.06988 - Guiding LLMs The Right Way","url":"https://www.emergentmind.com/papers/2403.06988"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/html/2403.06988v1"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://files.sri.inf.ethz.ch/website/papers/beurerkellner2024domino.pdf"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation [Quick Review]","url":"https://liner.com/review/guiding-llms-right-way-fast-noninvasive-constrained-generation"},{"title":"Guiding LLMs the right way | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692216"},{"title":"ICML Poster Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://icml.cc/virtual/2024/poster/33037"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation.","url":"https://cs.reviewer.ly/publication/a1828f67-6f12-492e-b89a-26291551486a"},{"title":"[2409.15241] Domino: Eliminating Communication in LLM Training via Generic Tensor Slicing and Overlapping","url":"https://arxiv.org/abs/2409.15241"},{"title":"Things we learned about LLMs in 2024 | Hacker News","url":"https://news.ycombinator.com/item?id=42560558"}]

Based on the search results, I found information about the paper "Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation":

**Authors:** Luca Beurer-Kellner, Marc Fischer, and Martin Vechev

**Venue:** ICML 2024

**Paper Identifier:** 2403.06988, published February 7, 2024

**Summary:** The paper addresses how to ensure that text generated by large language models (LLMs) is in an expected format through constrained decoding, which proposes to enforce strict formal language constraints during generation.

The paper introduces an algorithm called DOMINO for fast, non-invasive constrained generation in LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09ae1aaf-d7ad-4600-8eb6-6f27e877bdc9",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "da1a6dea-c546-4b91-8306-40391671d4a3",
  "sourceToolAssistantUUID": "09ae1aaf-d7ad-4600-8eb6-6f27e877bdc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T02:36:10.182Z_

<details><summary>↩ Tool result · `toolu_012e4eK6Gt5H2CvaNh1MyTxH`</summary>

```text
Web search results for query: "survey constrained decoding LLM structured generation 2024 2025 arxiv"

Links: [{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.15100v1"},{"title":"Guided Decoding and Its Critical Role in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.06631v1"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"},{"title":"Unveiling the Potential of Diffusion Large Language Model in Controllable Generation","url":"https://arxiv.org/html/2507.04504v1"}]

I've performed a web search for recent papers and resources on constrained decoding and structured generation in large language models from 2024-2025. Here are the key findings:

## Recent Survey and Benchmark Resources

There are recent papers on generating structured outputs from language models and benchmarks (January 2025), as well as papers on XGrammar, a flexible and efficient structured generation engine for large language models (November 2024).

## Key Papers and Frameworks

JSONSchemaBench evaluates six state-of-the-art constrained decoding frameworks, including Guidance, Outlines, Llamacpp, XGrammar, OpenAI, and Gemini.

Grammar-Aligned Decoding was submitted on May 31, 2024, and focuses on the problem of aligning sampling with grammar constraints.

Despite guaranteeing validity, constrained decoding often reduces semantic correctness on reasoning-intensive tasks.

## Technical Approaches

Recent works have introduced techniques to enforce LLM generations to adhere to a context-free grammar using constrained decoding. An adaptive constrained decoding approach can support various constrained decoding methods, including grammar-aligned techniques while preserving the LLM's expressivity by reasoning chains.

Outlines leverages finite-state machines (FSMs) to guide text generation efficiently, ensuring compliance with regular grammars while maintaining computational scalability.

## Resource Repository

There is an active curated list of papers on constrained decoding of LLMs along with code and resources, including papers on iterative semantic-aware structured generation, automata-based constraints, sketch-guided constrained decoding, and various benchmarks for evaluating structured generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "462b648f-2210-44b1-8ca6-ebabae59988b",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "03d6b0a5-e6e7-4509-8b93-02a01cbc8f3c",
  "sourceToolAssistantUUID": "462b648f-2210-44b1-8ca6-ebabae59988b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T02:36:12.502Z_

Let me get the remaining details -- the Guidance paper specifics and survey papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03d6b0a5-e6e7-4509-8b93-02a01cbc8f3c",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gYez9ik9HJtNqjJHZu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3e1fcc8-fd33-4734-974a-ee3ab1b2ad18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XooAgQ2HfHNxpBzk8CmFD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 19512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3793,
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

_source line 27 · 2026-05-14T02:36:14.059Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0118ipveexzjNTVvHeiRr9db`</summary>

```json
{
  "query": "\"Generating Structured Outputs from Language Models\" JSONSchemaBench arxiv 2501.10868 authors 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3e1fcc8-fd33-4734-974a-ee3ab1b2ad18",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gYez9ik9HJtNqjJHZu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd53f111-a68a-4942-b004-ae44ccba571c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XooAgQ2HfHNxpBzk8CmFD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 19512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3793,
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

_source line 28 · 2026-05-14T02:36:14.391Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013hivjN7oV6LQAtu775eYvK`</summary>

```json
{
  "query": "\"Grammar-Aligned Decoding\" arxiv 2405.21047 authors venue 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd53f111-a68a-4942-b004-ae44ccba571c",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gYez9ik9HJtNqjJHZu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b396fff1-285a-4f34-8e51-1d27dbd39068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XooAgQ2HfHNxpBzk8CmFD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 19512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3793,
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

_source line 29 · 2026-05-14T02:36:15.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K8NmFrgN1TMwwmmjyoUkTn`</summary>

```json
{
  "query": "Microsoft Guidance library academic paper \"guidance-ai\" constrained generation arxiv 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b396fff1-285a-4f34-8e51-1d27dbd39068",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gYez9ik9HJtNqjJHZu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "316cb2aa-c086-4763-a205-43c335852ad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XooAgQ2HfHNxpBzk8CmFD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 19512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3793,
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

_source line 30 · 2026-05-14T02:36:16.674Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FWD2uPpNx1sqbMrCycbyhQ`</summary>

```json
{
  "query": "XGrammar paper venue MLSys 2025 \"Yixin Dong\" \"Tianqi Chen\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "316cb2aa-c086-4763-a205-43c335852ad8",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gYez9ik9HJtNqjJHZu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b702b40-3dfe-44ab-a1b0-b1ecc9b2ad58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XooAgQ2HfHNxpBzk8CmFD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 19512,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3793
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 757,
          "output_tokens": 271,
          "cache_read_input_tokens": 19512,
          "cache_creation_input_tokens": 3793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3793,
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

_source line 31 · 2026-05-14T02:36:19.399Z_

<details><summary>↩ Tool result · `toolu_013hivjN7oV6LQAtu775eYvK`</summary>

```text
Web search results for query: ""Grammar-Aligned Decoding" arxiv 2405.21047 authors venue 2024"

Links: [{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"Grammar-Aligned Decoding - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240521047P/abstract"},{"title":"Grammar-Aligned Decoding","url":"https://arxiv.org/html/2405.21047"},{"title":"(PDF) Grammar-Aligned Decoding","url":"https://www.researchgate.net/publication/381108984_Grammar-Aligned_Decoding"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://arxiv.org/pdf/2405.21047"},{"title":"Approximately Aligned Decoding Daniel Melcer∗","url":"https://arxiv.org/pdf/2410.01103"},{"title":"Grammar-Aligned Decoding | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/grammar-aligned-decoding"},{"title":"Grammar-Aligned Decoding - Paper Reading","url":"https://paperreading.club/page?id=230674"},{"title":"Approximately Aligned Decoding","url":"https://arxiv.org/html/2410.01103v1"},{"title":"Grammar-Aligned Decoding","url":"https://www.popai.pro/chatwithdoc/paper/Grammar-Aligned-Decoding.html"}]

Based on the search results, here is the information about the paper:

**Title:** Grammar-Aligned Decoding

**ArXiv ID:** 2405.21047

**Authors:** Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, and Loris D'Antoni

**Venue:** Accepted to NeurIPS 2024

**Year:** 2024

**Summary:** The paper proposes adaptive sampling with approximate expected futures (ASAp), a decoding algorithm that guarantees the output to be grammatical while provably producing outputs that match the conditional probability of the LLM's distribution conditioned on the given grammar constraint. Their evaluation on code generation and structured NLP tasks shows how ASAp often produces outputs with higher likelihood (according to the LLM's distribution) than existing GCD techniques, while still enforcing the desired grammatical constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b396fff1-285a-4f34-8e51-1d27dbd39068",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "01dab1ac-54e0-416a-99f5-41da5ab1ade3",
  "sourceToolAssistantUUID": "b396fff1-285a-4f34-8e51-1d27dbd39068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T02:36:19.506Z_

<details><summary>↩ Tool result · `toolu_0118ipveexzjNTVvHeiRr9db`</summary>

```text
Web search results for query: ""Generating Structured Outputs from Language Models" JSONSchemaBench arxiv 2501.10868 authors 2025"

Links: [{"title":"[2501.10868] JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/abs/2501.10868"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"GitHub - guidance-ai/jsonschemabench · GitHub","url":"https://github.com/guidance-ai/jsonschemabench"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/html/2501.10868v3"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250110868G/abstract"},{"title":"(PDF) Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://www.researchgate.net/publication/388231978_Generating_Structured_Outputs_from_Language_Models_Benchmark_and_Studies"},{"title":"Paper page - Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://huggingface.co/papers/2501.10868"},{"title":"Generating Structured Outputs from Language Models","url":"https://nathanrchn.com/p/jsb"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for LLMs | OpenReview","url":"https://openreview.net/forum?id=GDKYFegWD3"},{"title":"GitHub - epfl-dlab/jsonschemabench","url":"https://github.com/epfl-dlab/jsonschemabench"}]

Based on the search results, here's information about the paper:

## Paper Overview

The paper titled "Generating Structured Outputs from Language Models: Benchmark and Studies" (arXiv:2501.10868) was submitted on January 18, 2025, with the latest revision on February 27, 2025, and has 9 authors including Saibo Geng, Hudson Cooper, Michał Moskal, Samuel Jenkins, Julian Berman, Nathan Ranchin, Robert West, Eric Horvitz, and Harsha Nori.

## Main Contribution

The paper addresses how reliably generating structured outputs has become a critical capability for modern language model applications, with constrained decoding having emerged as the dominant technology for enforcing structured outputs during generation.

## JSONSchemaBench Benchmark

The paper introduces JSONSchemaBench, a benchmark for constrained decoding comprising 10K real-world JSON schemas that encompass a wide range of constraints with varying complexity.

## Evaluation Framework

The benchmark is paired with the official JSON Schema Test Suite and evaluates six state-of-the-art constrained decoding frameworks: Guidance, Outlines, Llamacpp, XGrammar, OpenAI, and Gemini.

The evaluation framework assesses constrained decoding approaches across three critical dimensions: efficiency in generating constraint-compliant outputs, coverage of diverse constraint types, and quality of the generated outputs.

## Availability

JSONSchemaBench is released at https://github.com/guidance-ai/jsonschemabench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd53f111-a68a-4942-b004-ae44ccba571c",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "65a7df86-ad61-46de-85c7-a43d2b53d6f2",
  "sourceToolAssistantUUID": "bd53f111-a68a-4942-b004-ae44ccba571c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T02:36:21.054Z_

<details><summary>↩ Tool result · `toolu_01FWD2uPpNx1sqbMrCycbyhQ`</summary>

```text
Web search results for query: "XGrammar paper venue MLSys 2025 "Yixin Dong" "Tianqi Chen""

Links: [{"title":"Proceedings of Machine Learning and Systems 7","url":"https://proceedings.mlsys.org/paper_files/paper/2025"},{"title":"Track: Session 10: LLM and Diffusion Model Serving","url":"https://mlsys.org/virtual/2025/session/3161"},{"title":"Catalyst: XGrammar","url":"https://catalyst.cs.cmu.edu/projects/xgrammar.html"},{"title":"MLSys 2025 Thursday 05/15","url":"https://mlsys.org/virtual/2025/day/5/15"},{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"MLSys Poster XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://mlsys.org/virtual/2025/poster/3235"},{"title":"[PDF] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGrammar:-Flexible-and-Efficient-Structured-Engine-Dong-Ruan/274ca059ee4997f1e008bc8962aef3d22897f17a"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"8th MLSys 2025: Santa Clara, CA, USA","url":"https://dblp.org/db/conf/mlsys/mlsys2025.html"}]

Based on the search results, I can provide you with the information about the XGrammar paper:

The paper "XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models" is authored by Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ziyi Xu, Yilong Zhao, Ruihang Lai, and Tianqi Chen. The paper was published at MLSys 2025.

The paper proposes XGrammar, a flexible and efficient structure generation engine for large language models. XGrammar accelerates context-free grammar execution by dividing the vocabulary into context-independent tokens that can be prechecked and context-dependent tokens that need to be interpreted during runtime.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b702b40-3dfe-44ab-a1b0-b1ecc9b2ad58",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "e6138ae8-a6b1-4ba4-abaa-1df51843ec5d",
  "sourceToolAssistantUUID": "4b702b40-3dfe-44ab-a1b0-b1ecc9b2ad58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T02:36:23.169Z_

<details><summary>↩ Tool result · `toolu_01K8NmFrgN1TMwwmmjyoUkTn`</summary>

```text
Web search results for query: "Microsoft Guidance library academic paper "guidance-ai" constrained generation arxiv 2023 2024"

Links: [{"title":"GitHub - guidance-ai/llguidance: Super-fast Structured Outputs · GitHub","url":"https://github.com/guidance-ai/llguidance"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/html/2403.06988v1"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"guidance | control LM output – Microsoft Research","url":"https://www.microsoft.com/en-us/research/project/guidance-control-lm-output/"},{"title":"GitHub - guidance-ai/guidance: A guidance language for controlling large language models. · GitHub","url":"https://github.com/guidance-ai/guidance"},{"title":"111 A Survey of Controllable Text Generation using","url":"https://arxiv.org/pdf/2201.05337"},{"title":"Appropriate reliance on GenAI: Research synthesis Executive summary","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2024/03/GenAI_AppropriateReliance_Published2024-3-21.pdf"},{"title":"Controllable Text Generation for Large Language Models: A Survey","url":"https://arxiv.org/html/2408.12599v1"},{"title":"Generative AI Literacy: A Comprehensive Framework for Literacy and Responsible Use","url":"https://arxiv.org/html/2504.19038v1"},{"title":"From Generative AI to Innovative AI: An Evolutionary Roadmap","url":"https://arxiv.org/html/2503.11419v1"}]

I found relevant results about Microsoft's Guidance library and constrained generation research. Here are the key findings:

## Guidance Library Overview

The Guidance library implements constrained decoding (also called constrained sampling or structured outputs) for Large Language Models, enforcing arbitrary context-free grammar on LLM output with performance on the order of 50μs of CPU time per token for a 128k tokenizer with negligible startup costs.

## Academic Research on Constrained Generation

The search results include two relevant ArXiv papers from 2023-2024:

1. **"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation"** (ArXiv 2403.06988, March 2024): This paper constructs guidance programs to generate output in desired formats, comparing template-based programs (standard approach) and CFG-based variants which are whitespace agnostic.

2. **"Generating Structured Outputs from Language Models: Benchmark and Studies"** (ArXiv 2501.10868, January 2025): This benchmarking paper discusses various constrained-decoding frameworks including Guidance, Outlines, XGrammar, and the grammar module of Llamacpp, which provide broad support for different types of constraints, minimal overhead, and compatibility with various LM ecosystems.

## Related Framework Context

Constrained decoding refers to methods that guide language model generation by masking out tokens that do not adhere to predefined constraints at each step, with highly optimized grammar-constrained decoding frameworks having been developed to improve efficiency and usability.

The research demonstrates that Guidance is part of a broader ecosystem of constrained generation approaches developed around 2023-2024 for controlling LLM outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "316cb2aa-c086-4763-a205-43c335852ad8",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "ac9b1f97-d9d8-4a1f-9347-b10691964dca",
  "sourceToolAssistantUUID": "316cb2aa-c086-4763-a205-43c335852ad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T02:36:25.621Z_

Let me search for one more detail -- the LMQL venue and the Guidance paper by the same LMQL authors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac9b1f97-d9d8-4a1f-9347-b10691964dca",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gZcVcHBYXLwVg7GFsE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a834abf4-d155-4258-ba1e-f487a422708d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LS8jZ2pstarWWDoq7w13Qt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 711,
      "cache_creation_input_tokens": 3445,
      "cache_read_input_tokens": 23305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3445,
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

_source line 36 · 2026-05-14T02:36:27.037Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NWgH9P3Hh96jY6Wy66xrLK`</summary>

```json
{
  "query": "LMQL \"Prompting Is Programming\" venue PLDI 2023 Beurer-Kellner Fischer Vechev"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a834abf4-d155-4258-ba1e-f487a422708d",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gZcVcHBYXLwVg7GFsE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "492408ca-a372-43ce-b75a-fac2ca706e58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LS8jZ2pstarWWDoq7w13Qt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 711,
      "cache_creation_input_tokens": 3445,
      "cache_read_input_tokens": 23305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3445,
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

_source line 37 · 2026-05-14T02:36:27.693Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rui8vKxqPNU3RyztP2iSTC`</summary>

```json
{
  "query": "\"Controllable Text Generation\" survey LLM constrained decoding arxiv 2408.12599 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "492408ca-a372-43ce-b75a-fac2ca706e58",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gZcVcHBYXLwVg7GFsE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "caa0d9b3-7854-40a9-be31-8b5bb9dc2e4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LS8jZ2pstarWWDoq7w13Qt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 711,
      "cache_creation_input_tokens": 3445,
      "cache_read_input_tokens": 23305,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3445
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 711,
          "output_tokens": 170,
          "cache_read_input_tokens": 23305,
          "cache_creation_input_tokens": 3445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3445,
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

_source line 38 · 2026-05-14T02:36:31.906Z_

<details><summary>↩ Tool result · `toolu_01NWgH9P3Hh96jY6Wy66xrLK`</summary>

```text
Web search results for query: "LMQL "Prompting Is Programming" venue PLDI 2023 Beurer-Kellner Fischer Vechev"

Links: [{"title":"Prompting Is Programming: A Query Language for Large Language Models (PLDI 2023 - PLDI Research Papers) - PLDI 2023","url":"https://pldi23.sigplan.org/details/pldi-2023-pldi/81/Prompting-Is-Programming-A-Query-Language-for-Large-Language-Models"},{"title":"Prompting Is Programming: A Query Language for Large Language Models | Proceedings of the ACM on Programming Languages","url":"https://dl.acm.org/doi/10.1145/3591300"},{"title":"[2212.06094] Prompting Is Programming: A Query Language for Large Language Models","url":"https://arxiv.org/abs/2212.06094"},{"title":"Prompting Is Programming: A Query Language for Large Language Models 1","url":"https://arxiv.org/pdf/2212.06094"},{"title":"Research | LMQL","url":"https://lmql.ai/research/index.html"},{"title":"ETH Library Prompting Is Programming: A Query Language for Large","url":"https://www.research-collection.ethz.ch/server/api/core/bitstreams/9a54d4ba-8d99-47a9-b960-b6f33df0ee1d/content"},{"title":"Prompting Is Programming: A Query Language for Large Language Models | SRI Lab","url":"https://www.sri.inf.ethz.ch/publications/beurerkellner2023prompting"},{"title":"GitHub - lmql-lang/lmql: A query language for programming (large) language models. · GitHub","url":"https://github.com/lmql-lang/lmql"},{"title":"[2212.06094] Prompting Is Programming: A Query Language for Large Language Models","url":"https://ar5iv.labs.arxiv.org/html/2212.06094"},{"title":"Prompting Is Programming: A Query Language for Large Language Models","url":"https://www.researchgate.net/publication/371363896_Prompting_Is_Programming_A_Query_Language_for_Large_Language_Models"}]

Based on the web search results, I can provide you with information about the paper "Prompting Is Programming: A Query Language for Large Language Models":

## Paper Details

The paper "Prompting Is Programming: A Query Language for Large Language Models" was authored by Luca Beurer-Kellner, Marc Fischer, and Martin Vechev and published in June 2023 in the Proceedings of the ACM on Programming Languages, Vol. 7, PLDI, Article 186.

## Venue

The paper was presented at the 44th ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI 2023) in Orlando, Florida.

## Content Overview

The paper implements LMQL (short for Language Model Query Language), which leverages the constraints and control flow from an LMP prompt to generate an efficient inference procedure that minimizes the number of expensive calls to the underlying language model. The paper shows that LMQL can capture a wide range of state-of-the-art prompting methods in an intuitive way, especially facilitating interactive flows that are challenging to implement with existing high-level APIs.

The evaluation shows that they retain or increase the accuracy on several downstream tasks, while also significantly reducing the required amount of computation or cost in the case of pay-to-use APIs (26-85% cost savings).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "492408ca-a372-43ce-b75a-fac2ca706e58",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "0cb1c273-db6a-4e21-958a-e3cb2e83dfb6",
  "sourceToolAssistantUUID": "492408ca-a372-43ce-b75a-fac2ca706e58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T02:36:33.616Z_

<details><summary>↩ Tool result · `toolu_01Rui8vKxqPNU3RyztP2iSTC`</summary>

```text
Web search results for query: ""Controllable Text Generation" survey LLM constrained decoding arxiv 2408.12599 2024"

Links: [{"title":"[2408.12599] Controllable Text Generation for Large Language Models: A Survey","url":"https://arxiv.org/abs/2408.12599"},{"title":"Paper page - Controllable Text Generation for Large Language Models: A Survey","url":"https://huggingface.co/papers/2408.12599"},{"title":"Controllable Text Generation for Large Language Models: A Survey","url":"https://arxiv.org/html/2408.12599v1"},{"title":"GitHub - IAAR-Shanghai/CTGSurvey: Controllable Text Generation for Large Language Models: A Survey · GitHub","url":"https://github.com/IAAR-Shanghai/CTGSurvey"},{"title":"[2408.12599v1] Controllable Text Generation for Large Language Models: A Survey","url":"https://arxiv.org/abs/2408.12599v1"},{"title":"Controllable Text Generation for Large Language Models: A Survey - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240812599L/abstract"},{"title":"(PDF) Controllable Text Generation for Large Language Models: A Survey","url":"https://www.researchgate.net/publication/383308876_Controllable_Text_Generation_for_Large_Language_Models_A_Survey"},{"title":"[PDF] Controllable Text Generation for Large Language Models: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/7fbf028793a5252941e358366f57837888fcbf11"},{"title":"CTGSurvey/README.md at main · IAAR-Shanghai/CTGSurvey","url":"https://github.com/IAAR-Shanghai/CTGSurvey/blob/main/README.md"},{"title":"Controllable Text Generation for Large Language Models: A Survey | alphaXiv","url":"https://www.alphaxiv.org/resources/2408.12599v1"}]

I found the paper you're looking for! Here's what I found about arxiv 2408.12599:

## Paper Summary

The paper addresses how Large Language Models, while demonstrating high text generation quality, must meet increasingly complex requirements in real-world applications. LLMs are expected to meet specific user needs such as imitating particular writing styles or generating text with poetic richness. These demands have driven the development of Controllable Text Generation (CTG) techniques, which ensure that outputs adhere to predefined control conditions—such as safety, sentiment, thematic consistency, and linguistic style—while maintaining high standards of helpfulness, fluency, and diversity.

## Key Contributions

The paper categorizes CTG tasks into two primary types: content control and attribute control. The key methods discussed include model retraining, fine-tuning, reinforcement learning, prompt engineering, latent space manipulation, and decoding-time intervention.

## Publication Details

The paper was published on the arXiv platform on August 23, 2024. The authors include Xun Liang, Hanyu Wang, Yezhaohui Wang, Shichao Song, Jiawei Yang, Simin Niu, Jie Hu, Dan Liu, Shunyu Yao, Feiyu Xiong, and Zhiyu Li.

The paper provides a comprehensive survey of Controllable Text Generation techniques for LLMs with emphasis on both constrained decoding approaches and other methodologies for controlling LLM outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caa0d9b3-7854-40a9-be31-8b5bb9dc2e4d",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "9c575e01-9f51-401e-ace6-58512d70a49c",
  "sourceToolAssistantUUID": "caa0d9b3-7854-40a9-be31-8b5bb9dc2e4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-14T02:36:36.833Z_

Let me search for one more thing -- the Outlines paper venue and the Guidance-specific paper if one exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c575e01-9f51-401e-ace6-58512d70a49c",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gaPBCUwFEDPanjc2jP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b13f862-d9f2-4f06-963a-193a77de565c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xUEPdGRqG2hXeB7nK8Sxp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2679,
      "cache_read_input_tokens": 26750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2679,
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

_source line 41 · 2026-05-14T02:36:37.993Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ThYnqd7PLovM5pBAnjMfEp`</summary>

```json
{
  "query": "Outlines \"Efficient Guided Generation\" Willard Louf venue conference publication 2024 NeurIPS ICML workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b13f862-d9f2-4f06-963a-193a77de565c",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gaPBCUwFEDPanjc2jP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b89f0a5-8881-4b67-8ec1-f39d578daeb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xUEPdGRqG2hXeB7nK8Sxp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2679,
      "cache_read_input_tokens": 26750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2679,
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

_source line 42 · 2026-05-14T02:36:38.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013xrxvpXGNhhu6jU8PhcX1V`</summary>

```json
{
  "query": "\"Guaranteed Generation from Large Language Models\" ICLR 2025 constrained decoding grammar arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b89f0a5-8881-4b67-8ec1-f39d578daeb2",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gaPBCUwFEDPanjc2jP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bb3e4cc-e902-4709-a4be-e3a0b735d109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xUEPdGRqG2hXeB7nK8Sxp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2679,
      "cache_read_input_tokens": 26750,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2679
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 26750,
          "cache_creation_input_tokens": 2679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2679,
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

_source line 43 · 2026-05-14T02:36:43.854Z_

<details><summary>↩ Tool result · `toolu_01ThYnqd7PLovM5pBAnjMfEp`</summary>

```text
Web search results for query: "Outlines "Efficient Guided Generation" Willard Louf venue conference publication 2024 NeurIPS ICML workshop"

Links: [{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf"},{"title":"(PDF) Efficient Guided Generation for LLMs","url":"https://www.researchgate.net/publication/372468267_Efficient_Guided_Generation_for_LLMs"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"},{"title":"NeurIPS 2024 Papers","url":"https://nips.cc/virtual/2024/papers.html"},{"title":"ICLR 2024 Papers","url":"https://iclr.cc/virtual/2024/papers.html"},{"title":"icml-2024 · GitHub Topics · GitHub","url":"https://github.com/topics/icml-2024"},{"title":"GitHub - LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy: ✨✨Latest Advances on Neuro-Symbolic Learning in the era of Large Language Models","url":"https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy"}]

Based on the search results, here's what I found about "Efficient Guided Generation":

The paper "Efficient Guided Generation for Large Language Models" was authored by Brandon T. Willard and Rémi Louf. The paper shows how the problem of neural text generation can be constructively reformulated in terms of transitions between the states of a finite-state machine.

Regarding publication details: The paper was published on arXiv in 2023 (arXiv:2307.09702), not at a 2024 conference like NeurIPS or ICML.

The work is associated with "Outlines: Generative Model Programming", which is the implementation framework for this research.

The framework leads to an efficient approach to guiding text generation with regular expressions and context-free grammars by allowing the construction of an index over a language model's vocabulary, is model agnostic, allows enforcement of domain-specific knowledge and constraints, and adds little overhead to the token sequence generation process.

The search results do not show that this paper was published at a 2024 NeurIPS or ICML venue or workshop - it appears to be an arXiv preprint from 2023 that is now being cited in 2024 conference papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b89f0a5-8881-4b67-8ec1-f39d578daeb2",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "9ca87fd0-9122-4a90-a021-6b9845c93a0c",
  "sourceToolAssistantUUID": "2b89f0a5-8881-4b67-8ec1-f39d578daeb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T02:36:44.539Z_

<details><summary>↩ Tool result · `toolu_013xrxvpXGNhhu6jU8PhcX1V`</summary>

```text
Web search results for query: ""Guaranteed Generation from Large Language Models" ICLR 2025 constrained decoding grammar arxiv"

Links: [{"title":"ICML Poster Flexible and Efficient Grammar-Constrained Decoding","url":"https://icml.cc/virtual/2025/poster/45613"},{"title":"Guaranteed Generation from Large Language Models | OpenReview","url":"https://openreview.net/forum?id=8roRgrjbjv"},{"title":"Published as a conference paper at ICLR 2025 GUARANTEED GENERATION FROM","url":"https://openreview.net/pdf?id=8roRgrjbjv"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"Grammar-Constrained Decoding Makes Large Language ...","url":"https://aclanthology.org/2025.acl-industry.34.pdf"},{"title":"[2410.06716] Guaranteed Generation from Large Language Models","url":"https://arxiv.org/abs/2410.06716"},{"title":"Guaranteed Generation from Large Language Models","url":"https://arxiv.org/html/2410.06716"},{"title":"Grammar-Constrained Decoding Makes Large Language Models Better Logical Parsers - ACL Anthology","url":"https://aclanthology.org/2025.acl-industry.34/"}]

I found relevant results for your search. Here's what I found:

## "Guaranteed Generation from Large Language Models" - ICLR 2025

The paper proposes GUARD, a method that combines an autoregressive proposal distribution with rejection sampling to provide a principled approach to enforcing strict guarantees for LLMs without compromising their generative capabilities.

**Key Contribution:**
The paper defines the ideal distribution—the one closest to the original model that always satisfies the expressed constraint—as the ultimate goal of guaranteed generation. It states that it's impossible to reach this goal through autoregressive training alone, which motivates combining training-time and inference-time methods.

**Results:**
GUARD achieves perfect constraint satisfaction while almost preserving the ideal distribution with highly improved inference efficiency.

**ArXiv Details:**
The paper is available on arXiv as paper 2410.06716. The latest version (v2) was updated on July 2, 2025.

The paper addresses an important problem in constrained decoding for LLMs, though it focuses more on general constraint satisfaction through rejection sampling rather than grammar-specific constrained decoding approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bb3e4cc-e902-4709-a4be-e3a0b735d109",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "ab33888ae5255d2f0",
  "type": "user",
  "uuid": "4b225689-be34-424c-a03e-2ec28fddf05f",
  "sourceToolAssistantUUID": "2bb3e4cc-e902-4709-a4be-e3a0b735d109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-14T02:37:29.356Z_

Here are the findings, structured by paper.

---

## 1. XGrammar

- **Full title:** XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models
- **Authors:** Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ruihang Lai, Ziyi Xu, Yilong Zhao, Tianqi Chen
- **Venue:** MLSys 2025
- **ArXiv:** [2411.15100](https://arxiv.org/abs/2411.15100) (Nov 2024)
- **Core method:** Divides the vocabulary into context-independent tokens (pre-checkable offline) and context-dependent tokens (checked at runtime), combined with persistent stack-based pushdown automata for efficient CFG constraint enforcement. Achieves up to 100x speedup over prior grammar-constrained decoding approaches.
- **Note:** A follow-up, XGrammar-2 (arXiv [2601.04426](https://arxiv.org/html/2601.04426)), extends to dynamic structured generation for agentic LLMs.

---

## 2. Guidance / Domino (Microsoft / ETH Zurich)

Microsoft's **Guidance** library ([github.com/guidance-ai/guidance](https://github.com/guidance-ai/guidance)) is an open-source framework but does not have a standalone academic paper. The closest peer-reviewed work by the same research group is:

- **Full title:** Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation
- **Authors:** Luca Beurer-Kellner, Marc Fischer, Martin Vechev
- **Venue:** ICML 2024
- **ArXiv:** [2403.06988](https://arxiv.org/abs/2403.06988) (Mar 2024)
- **Core method:** Proposes the DOMINO algorithm for non-invasive constrained decoding that enforces CFG constraints while minimally distorting the LLM's original distribution. Leverages pre-computation and speculative decoding, achieving throughput that can even exceed unconstrained generation.

---

## 3. Outlines

- **Full title:** Efficient Guided Generation for Large Language Models
- **Authors:** Brandon T. Willard, Remi Louf
- **Venue:** arXiv preprint (no confirmed top-venue publication; widely cited)
- **ArXiv:** [2307.09702](https://arxiv.org/abs/2307.09702) (Jul 2023, updated 2024)
- **Core method:** Reformulates constrained text generation as transitions in a finite-state machine (FSM). Builds an offline index over the vocabulary for each FSM state, enabling O(1) amortized per-token constraint checking for regular expressions. Extends to context-free grammars via LALR(1) parsers. Implemented in the open-source Outlines library.

---

## 4. LMQL

- **Full title:** Prompting Is Programming: A Query Language for Large Language Models
- **Authors:** Luca Beurer-Kellner, Marc Fischer, Martin Vechev
- **Venue:** PLDI 2023 (ACM SIGPLAN Conference on Programming Language Design and Implementation)
- **ArXiv:** [2212.06094](https://arxiv.org/abs/2212.06094) (Dec 2022)
- **Core method:** Introduces LMQL, a SQL-like query language for LLMs where users combine natural language prompts with programmatic control flow and declarative constraints (type, length, regex, stopping conditions). The LMQL runtime compiles these constraints into an efficient token-level masking procedure, reducing API costs by 26-85% while maintaining or improving accuracy.

---

## 5. SGLang

- **Full title:** SGLang: Efficient Execution of Structured Language Model Programs
- **Authors:** Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Chuyue Sun, Jeff Huang, Cody Hao Yu, Shiyi Cao, Christos Kozyrakis, Ion Stoica, Joseph E. Gonzalez, Clark Barrett, Ying Sheng
- **Venue:** NeurIPS 2024
- **ArXiv:** [2312.07104](https://arxiv.org/abs/2312.07104) (Dec 2023)
- **Core method:** A domain-specific language embedded in Python with a co-designed runtime. Key innovations include RadixAttention for KV cache reuse across structured program branches and compressed finite state machines for faster structured output decoding. Achieves up to 6.4x higher throughput than SOTA inference systems on structured generation tasks.

---

## 6. Grammar-Aligned Decoding (bonus notable paper)

- **Full title:** Grammar-Aligned Decoding
- **Authors:** Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni
- **Venue:** NeurIPS 2024
- **ArXiv:** [2405.21047](https://arxiv.org/abs/2405.21047) (May 2024)
- **Core method:** Proposes ASAp (Adaptive Sampling with Approximate expected futures), a decoding algorithm that enforces grammar constraints while provably preserving the LLM's conditional distribution given the grammar, addressing the distribution distortion problem in naive token masking.

---

## Survey / Benchmark Papers

**JSONSchemaBench (Benchmark, 2025)**
- **Full title:** JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models
- **Authors:** Saibo Geng, Hudson Cooper, Michal Moskal, Samuel Jenkins, Julian Berman, Nathan Ranchin, Robert West, Eric Horvitz, Harsha Nori
- **ArXiv:** [2501.10868](https://arxiv.org/abs/2501.10868) (Jan 2025)
- **Summary:** Benchmark of 10K real-world JSON schemas evaluating six constrained decoding frameworks (Guidance, Outlines, Llamacpp, XGrammar, OpenAI, Gemini) across efficiency, coverage, and output quality.

**Controllable Text Generation Survey (2024)**
- **Full title:** Controllable Text Generation for Large Language Models: A Survey
- **Authors:** Xun Liang, Hanyu Wang, Yezhaohui Wang, Shichao Song, et al.
- **ArXiv:** [2408.12599](https://arxiv.org/abs/2408.12599) (Aug 2024)
- **Summary:** Broad survey categorizing CTG into content control and attribute control, covering methods from fine-tuning to decoding-time intervention including constrained decoding.

**GUARD (ICLR 2025)**
- **Full title:** Guaranteed Generation from Large Language Models
- **Authors:** (see paper)
- **Venue:** ICLR 2025
- **ArXiv:** [2410.06716](https://arxiv.org/abs/2410.06716)
- **Summary:** Defines the ideal constrained distribution as the closest to the original LLM satisfying constraints, proves autoregressive training alone cannot reach it, and proposes GUARD combining training-time and inference-time methods with rejection sampling.

**Awesome-LLM-Constrained-Decoding** (curated list): [github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding](https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding) -- comprehensive repository tracking all papers in this space.

---

Notable observation: Beurer-Kellner, Fischer, and Vechev (ETH Zurich) authored both LMQL (PLDI 2023) and Domino/Guidance (ICML 2024), making them a central group in this area. The SGLang system (NeurIPS 2024) now integrates XGrammar (MLSys 2025) as its grammar engine, forming the current highest-performance open-source stack for grammar-constrained serving.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b225689-be34-424c-a03e-2ec28fddf05f",
  "isSidechain": true,
  "agentId": "ab33888ae5255d2f0",
  "requestId": "req_011Cb1gbBuZTQ8JqPstrxWTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "916faced-3465-4066-8f22-5df573aaff45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkT96ULZakHVTZKwdJzdKZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2025,
      "cache_read_input_tokens": 29429,
      "output_tokens": 1984,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2025
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1984,
          "cache_read_input_tokens": 29429,
          "cache_creation_input_tokens": 2025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2025,
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
