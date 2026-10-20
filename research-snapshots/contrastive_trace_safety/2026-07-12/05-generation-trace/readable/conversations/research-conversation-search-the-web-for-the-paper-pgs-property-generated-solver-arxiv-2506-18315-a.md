# Research conversation: Search the web for the paper "PGS Property-Generated Solver arXiv 2506.18315" — a paper that supposedly uses high-level 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a20bbcc43498984e4.jsonl`
- **Structured JSON:** [`9fa4e9320d4bb53c1e06.json`](../../sessions/9f/9fa4e9320d4bb53c1e06.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-12T01:17:28.512Z_

Search the web for the paper "PGS Property-Generated Solver arXiv 2506.18315" — a paper that supposedly uses high-level program properties instead of test cases as feedback for LLM code refinement. I need to verify:
1. Does this paper actually exist?
2. What exactly does it do?
3. What results does it claim (13.4% pass@1 improvement over TDD methods, 1.4-1.6x higher bug fix rate)?
4. How does it compare to an approach that uses execution-grounded behavioral specifications (preconditions, postconditions, invariants, type constraints) as intermediate reasoning?

Search for: "PGS property-generated solver arXiv 2506", "property-based feedback LLM code generation 2025 2026", "property guided code refinement LLM". Also try fetching the arxiv page if the paper exists.

Report your findings in detail, including whether the paper exists, its actual claims, and how closely it overlaps with using execution-verified behavioral specifications for code tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "2c990222-b8c3-411a-81bf-74fc5a31cca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T01:17:28.515Z_

```json
{
  "parentUuid": "2c990222-b8c3-411a-81bf-74fc5a31cca3",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
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
  "uuid": "beb75c20-fa72-449f-b47a-0032e50b234b",
  "timestamp": "2026-05-12T01:17:28.515Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T01:17:30.701Z_



I'll search for this paper using multiple approaches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "beb75c20-fa72-449f-b47a-0032e50b234b",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnvmcZTv9ct42gPmXFL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d340f2d6-a1ec-4d46-ac1b-2083bd1e7ae8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2LpBACDTYKkK2fsSmP9Qv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9008,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9008,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T01:17:31.321Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TSkFTk4dFHWevwzdV3twYN`</summary>

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
  "parentUuid": "d340f2d6-a1ec-4d46-ac1b-2083bd1e7ae8",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnvmcZTv9ct42gPmXFL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21ba6dd8-bd31-4175-9c27-7e5cff3b321c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2LpBACDTYKkK2fsSmP9Qv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9008,
      "cache_read_input_tokens": 0,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9008
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9008,
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

_source line 5 · 2026-05-12T01:17:31.326Z_

<details><summary>↩ Tool result · `toolu_01TSkFTk4dFHWevwzdV3twYN`</summary>

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
  "parentUuid": "21ba6dd8-bd31-4175-9c27-7e5cff3b321c",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "a25e28e7-b2cc-4f2a-abe7-1e5f7f3a5342",
  "sourceToolAssistantUUID": "21ba6dd8-bd31-4175-9c27-7e5cff3b321c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T01:17:33.850Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a25e28e7-b2cc-4f2a-abe7-1e5f7f3a5342",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011Cawnvz1wQcK99uMmyCeSm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5232895f-d62f-4ec5-8a87-a408e35f1c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWMGxKtioryk6s1LmVZB3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 7 · 2026-05-12T01:17:34.801Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013qgjetrbNRg92gEnjpnMLt`</summary>

```json
{
  "query": "PGS property-generated solver arXiv 2506.18315"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5232895f-d62f-4ec5-8a87-a408e35f1c28",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011Cawnvz1wQcK99uMmyCeSm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "387a0d7a-4892-4296-9631-4a432bfeca34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWMGxKtioryk6s1LmVZB3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 8 · 2026-05-12T01:17:35.279Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019dD8B9oU2so3unjDs7kr1E`</summary>

```json
{
  "query": "\"property-generated solver\" LLM code refinement arXiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "387a0d7a-4892-4296-9631-4a432bfeca34",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011Cawnvz1wQcK99uMmyCeSm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dd9fe06-3e8d-463a-94b5-70e5844cb610",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWMGxKtioryk6s1LmVZB3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 9 · 2026-05-12T01:17:36.222Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bieb9V2tJmu8gSRpZYwf4u`</summary>

```json
{
  "query": "property-based feedback LLM code generation 2025 2026 pass@1 improvement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dd9fe06-3e8d-463a-94b5-70e5844cb610",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011Cawnvz1wQcK99uMmyCeSm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48d3143f-924d-4002-b1ea-0033410d6c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWMGxKtioryk6s1LmVZB3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 10 · 2026-05-12T01:17:37.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TparQtqnXHcQ62vhbSq4q7`</summary>

```json
{
  "query": "property guided code refinement LLM test-driven development alternative"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48d3143f-924d-4002-b1ea-0033410d6c97",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011Cawnvz1wQcK99uMmyCeSm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14e74683-a1cb-4ac9-b3cd-cb634121d256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWMGxKtioryk6s1LmVZB3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 9008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 11 · 2026-05-12T01:17:38.951Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018DHejeG3CBDEuJxtods7Qf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.18315",
  "prompt": "Extract the full title, authors, abstract, and any key claims or results from this paper. What is it about? Does it discuss property-based feedback, LLM code generation, pass@1 improvements, bug fix rates, or TDD comparisons?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14e74683-a1cb-4ac9-b3cd-cb634121d256",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011Cawnvz1wQcK99uMmyCeSm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93cf5a36-0fd0-4d85-8942-503ebe0971f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWMGxKtioryk6s1LmVZB3q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 9008,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1902
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 355,
          "cache_read_input_tokens": 9008,
          "cache_creation_input_tokens": 1902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1902,
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

_source line 12 · 2026-05-12T01:17:40.901Z_

<details><summary>↩ Tool result · `toolu_013qgjetrbNRg92gEnjpnMLt`</summary>

```text
Web search results for query: "PGS property-generated solver arXiv 2506.18315"

Links: [{"title":"[2506.18315] Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/abs/2506.18315"},{"title":"Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/html/2506.18315"},{"title":"[2506.17747] Pix2Geomodel: A Next-Generation Reservoir Geomodeling with Property-to-Property Translation","url":"https://arxiv.org/abs/2506.17747"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=3075&show=2000"},{"title":"PCG-Informed Neural Solvers for High-Resolution Homogenization of Periodic Microstructures","url":"https://arxiv.org/html/2506.17087v2"},{"title":"[1503.07025] Property-based Polynomial Invariant Generation using Sums-of-Squares Optimization","url":"https://arxiv.org/abs/1503.07025"},{"title":"An approximate Riemann Solver Approach in Physics-Informed Neural Networks for hyperbolic conservation laws","url":"https://arxiv.org/html/2506.11959v1"},{"title":"Machine Learning Jun 2025","url":"https://arxiv.org/list/cs.LG/2025-06?skip=2900&show=2000"},{"title":"Computer Science Jan 2024","url":"https://arxiv.org/list/cs/2024-01?skip=7050&show=2000"},{"title":"[2506.17087] PCG-Informed Neural Solvers for High-Resolution Homogenization of Periodic Microstructures","url":"https://arxiv.org/abs/2506.17087"}]

Based on the search results, here's information about the arXiv paper 2506.18315:

## Property-Generated Solver (PGS)

Property-Generated Solver is a novel framework that leverages Property-Based Testing (PBT) to validate high-level program properties or invariants, instead of relying on specific input-output examples.

### Framework Overview

Property-Generated Solver employs two collaborative LLM-based agents: a Generator dedicated to code generation and iterative refinement, and a Tester that manages the PBT life-cycle and formulate semantically rich feedback from property violations. The resulting comprehensive and actionable feedback then guides the Generator in its refinement efforts. By establishing PBT as the core validation engine within this iterative, closed-loop paradigm, Property-Generated Solver provides a robust mechanism for steering LLMs towards more correct and generalizable code.

### Performance Results

Extensive experimental results on multiple code generation benchmarks demonstrate that Property-Generated Solver achieves substantial pass@1 improvements, ranging from 23.1% to 37.3% relative gains over established TDD methods.

The paper was submitted on June 23, 2025, and addresses the challenge of ensuring that LLM-generated code is functionally correct, particularly for complex programming tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "387a0d7a-4892-4296-9631-4a432bfeca34",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "c4f33ef1-fb1c-4185-8b3d-f08d1b0d3d12",
  "sourceToolAssistantUUID": "387a0d7a-4892-4296-9631-4a432bfeca34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T01:17:42.550Z_

<details><summary>↩ Tool result · `toolu_019dD8B9oU2so3unjDs7kr1E`</summary>

```text
Web search results for query: ""property-generated solver" LLM code refinement arXiv 2025 2026"

Links: [{"title":"[2505.08783] CodePDE: An Inference Framework for LLM-driven PDE Solver Generation","url":"https://arxiv.org/abs/2505.08783"},{"title":"Solver-Informed RL: Grounding Large Language Models for Authentic Optimization Modeling","url":"https://arxiv.org/html/2505.11792v3"},{"title":"CodePDE: An Inference Framework for LLM-driven PDE Solver Generation","url":"https://arxiv.org/html/2505.08783v2"},{"title":"LLM Research Papers: The 2025 List (January to June)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-list-one"},{"title":"Bridging Code Property Graphs and Language Models for Program Analysis","url":"https://arxiv.org/html/2603.24837"},{"title":"A Survey on Code Generation with LLM-based Agents","url":"https://arxiv.org/html/2508.00083v1"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"Improving LLM Code Generation via Requirement-Aware Curriculum Reinforcement Learning","url":"https://arxiv.org/html/2605.00433v1"},{"title":"Towards Formal Verification of LLM-Generated Code from Natural Language Prompts","url":"https://arxiv.org/html/2507.13290v1"},{"title":"Position: LLM Serving Needs Mathematical Optimization and Algorithmic Foundations, Not Just Heuristics","url":"https://arxiv.org/html/2605.01280v1"}]

I found several relevant papers related to LLM code refinement and solver generation from 2025-2026. Here are the key results:

## Main Findings

The search returned several papers related to LLM-driven code generation and refinement:

1. **CodePDE** - An inference framework for generating PDE solvers using large language models (LLMs). This framework evaluates critical capacities of LLM for PDE solving: reasoning, debugging, self-refinement, and test-time scaling. Notably, LLMs can improve code for better accuracy using simple performance feedback, and the best models at generating code are not always the best at refining it, suggesting these are two different skills.

2. **Solver-Informed RL** - This work leverages the LLM to refine the entire result by regenerating both the mathematical model and its corresponding code when infeasible solutions are obtained after executing code using the solver.

3. **Code Generation with LLM-based Agents** - A survey covering various code refinement approaches, including CodeChain, which introduces a modular self-revision framework that guides the model to iteratively refine code by identifying and clustering representative sub-modules from initial outputs, and leveraging these sub-modules to enhance subsequent generations.

These papers appear to address code refinement through iterative feedback and verification mechanisms, though the specific "property-generated solver" technique you mentioned wasn't explicitly found in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dd9fe06-3e8d-463a-94b5-70e5844cb610",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "60b1a166-2d5a-4cef-852b-5521baaf1cfc",
  "sourceToolAssistantUUID": "4dd9fe06-3e8d-463a-94b5-70e5844cb610",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T01:17:43.687Z_

<details><summary>↩ Tool result · `toolu_01Bieb9V2tJmu8gSRpZYwf4u`</summary>

```text
Web search results for query: "property-based feedback LLM code generation 2025 2026 pass@1 improvement"

Links: [{"title":"Improving LLM Code Generation via Requirement-Aware Curriculum Reinforcement Learning","url":"https://arxiv.org/html/2605.00433"},{"title":"LLMLOOP: Improving LLM-Generated Code and Tests ...","url":"https://valerio-terragni.github.io/assets/pdf/ravi-icsme-2025.pdf"},{"title":"My LLM coding workflow going into 2026 | by Addy Osmani | Medium","url":"https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e"},{"title":"Improving LLM Code Generation via Requirement-Aware ...","url":"https://arxiv.org/pdf/2605.00433"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"LLM-Generated Code in 2025: Trends and Predictions - Revelo","url":"https://www.revelo.com/blog/llm-code-generation-2025-trends-predictions-human-data"},{"title":"Self-Planning Code Generation with Large Language Models | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3672456"},{"title":"Improving LLM-Generated Code via Genetic Improvement","url":"https://ceur-ws.org/Vol-4121/Ital-IA_2025_paper_111.pdf"},{"title":"Reinforcement Learning for Safe LLM Code Generation Roy Huang","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-123.pdf"},{"title":"Towards LLM-Driven Code Generation: The Impact of Process ...","url":"https://spectrum.library.concordia.ca/id/eprint/995585/1/LIN_MA_S2025.pdf"}]

## Web Search Results Summary

I found several relevant research papers and articles on LLM code generation with Pass@1 improvements. Here are the key findings:

### Recent Research on Pass@1 Improvements (2025-2026)

**1. Requirement-Aware Curriculum Reinforcement Learning (RECRL)**

RECRL achieves an average Pass@1 improvement of 1.23%∼5.62% over all baselines across all 25 subjects. RECRL improves the average Pass@1 of the smaller Qwen2.5-Coder-3B from 60.07% to 66.50%, enabling it to slightly outperform the substantially larger Qwen2.5-Coder-7B (66.05%).

**2. Self-Planning Code Generation**

Self-planning approach showed a relative improvement of up to 25.4% in Pass@1 over the direct generation approach and up to 11.9% over CoT approach of code generation.

**3. Process-Based Approaches (FlowGen)**

FlowGenScrum outperforms the other process models, achieving a 15% improvement in Pass@1 over RawGPT on average.

### Feedback Mechanisms and Training Approaches

LLMs will provide real-time feedback during code development, catching errors instantly and offering suggestions for improvement, transforming code reviews into a more collaborative and efficient process.

CRL has been widely adopted to fundamentally enhance the performance of LLM-based code generation, where each training instance corresponds to a programming requirement, and the model is trained following a curriculum schedule defined by task difficulty.

These research directions from 2025-2026 show that Pass@1 improvements are being driven by curriculum learning strategies, requirement optimization, planning-based approaches, and structured feedback mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48d3143f-924d-4002-b1ea-0033410d6c97",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "21a3a7d7-58cb-493a-8a02-47e695d2ce51",
  "sourceToolAssistantUUID": "48d3143f-924d-4002-b1ea-0033410d6c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T01:17:43.885Z_

<details><summary>↩ Tool result · `toolu_018DHejeG3CBDEuJxtods7Qf`</summary>

```text
# Paper Summary: Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback

**Full Title:** "Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback"

**Authors:** Lehan He, Zeren Chen, Zhe Zhang, Xiang Gao, Lu Sheng

## Abstract Overview

The paper addresses functional correctness challenges in LLM-generated code by introducing the Property-Generated Solver (PGS), a novel approach that prioritizes feedback quality over quantity. Rather than relying on numerous test cases, PGS generates targeted feedback by:

1. Checking high-level program properties (such as sorting functions producing non-decreasing sequences)
2. Providing the simplest failing counterexample to guide the model

## Key Claims & Results

The research demonstrates substantial improvements:

- **Pass@1 enhancement:** Up to 13.4% improvement compared to other Test-Driven Development methods
- **Fix rate:** Over 64% success rate on initially failing problems
- **Benchmark performance:** Bug fix rates 1.4x-1.6x higher than the strongest debugging approaches
- Claims establishment of "state-of-the-art in automated code refinement"

## Core Focus Areas

The paper directly addresses property-based feedback, LLM code generation refinement, pass@1 metrics, bug fix rates, and TDD comparisons—all key themes mentioned in your question.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93cf5a36-0fd0-4d85-8942-503ebe0971f1",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "ec3b66a2-8d3b-4d8d-a73a-8ed8047184d0",
  "sourceToolAssistantUUID": "93cf5a36-0fd0-4d85-8942-503ebe0971f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T01:17:44.983Z_

<details><summary>↩ Tool result · `toolu_01TparQtqnXHcQ62vhbSq4q7`</summary>

```text
Web search results for query: "property guided code refinement LLM test-driven development alternative"

Links: [{"title":"Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/html/2506.18315"},{"title":"Test-Driven Development and LLM-based Code Generation | Request PDF","url":"https://www.researchgate.net/publication/385286907_Test-Driven_Development_and_LLM-based_Code_Generation"},{"title":"[2506.18315] Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/abs/2506.18315"},{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878v1"},{"title":"Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants","url":"https://arxiv.org/html/2602.00180v1"},{"title":"Understanding Specification-Driven Code Generation with ...","url":"https://arxiv.org/pdf/2601.03878"},{"title":"LLM-based Test-driven Interactive Code Generation","url":"https://www.seas.upenn.edu/~asnaik/assets/papers/tse24_ticoder.pdf"},{"title":"Paper page - Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://huggingface.co/papers/2506.18315"},{"title":"The complete guide for TDD with LLMs | by Rogério Chaves | Medium","url":"https://rchavesferna.medium.com/the-complete-guide-for-tdd-with-llms-1dfea9041998"},{"title":"DEVELOPMENT BENCHMARK FOR LLM CODE GEN- ...","url":"https://openreview.net/pdf/aaa6516c648f0940262aaffdaae17c7f4597da8a.pdf"}]

Based on the search results, I found comprehensive information about property guided code refinement with LLMs and test-driven development alternatives.

## Key Findings

Property-Generated Solver (PGS) is a novel framework that is the first to systematically apply Property-Based Testing as the primary driver for LLM-based code generation and refinement, using two collaborative agents: a Generator for code generation and a Tester for property-driven validation.

### How It Works as a TDD Alternative

Property-Generated Solver leverages Property-Based Testing (PBT) to validate high-level program properties or invariants, instead of relying on specific input-output examples. These properties are often simpler to define and verify than directly predicting exhaustive test oracles, breaking the "cycle of self-deception" where tests might share flaws with the code they are meant to validate.

### Performance Advantages

Property-Generated Solver achieves substantial pass@1 improvements, ranging from 23.1% to 37.3% relative gains over established TDD methods. Feedback derived from property-driven validation provides more effective guidance for LLM-based code generation compared to feedback from conventional TDD methods.

### Why It's Better Than Traditional TDD

While traditional Test-Driven Development offers a path for code refinement, its efficacy with LLMs is often undermined by the scarcity of high-quality test cases or the pitfalls of automated test generation, including biased tests or inaccurate output predictions that can misdirect the correction process.

The research demonstrates that property-based approaches offer a more robust alternative to conventional test-driven development for guiding LLM code generation and refinement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14e74683-a1cb-4ac9-b3cd-cb634121d256",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "d708e04f-cb87-4919-9ac5-3878f14584ba",
  "sourceToolAssistantUUID": "14e74683-a1cb-4ac9-b3cd-cb634121d256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-12T01:17:48.170Z_

Excellent. The paper exists. Let me now fetch the full HTML version for more detailed information, and also search for the specification-driven approaches to compare against.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d708e04f-cb87-4919-9ac5-3878f14584ba",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnwyzyFA6HHwJXuY99m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe0776b4-5c76-4732-a8b8-8b9706e9b7f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDjXuE21p1gR3mJBhsCA5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 362,
      "cache_creation_input_tokens": 3934,
      "cache_read_input_tokens": 10910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3934,
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

_source line 18 · 2026-05-12T01:17:51.925Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016FF6AAF279EQTAgLAg7teY`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.18315",
  "prompt": "Extract the complete abstract, all key results with exact numbers, the methodology details (how the Generator and Tester agents work, what properties are used, how counterexamples are generated), the benchmarks used, the baselines compared against, and any discussion of related work involving formal specifications, preconditions, postconditions, invariants, or behavioral specifications. Also extract any limitations discussed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe0776b4-5c76-4732-a8b8-8b9706e9b7f7",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnwyzyFA6HHwJXuY99m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72ef2cfd-87b7-4d1e-a3e2-4e3b3d568055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDjXuE21p1gR3mJBhsCA5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 362,
      "cache_creation_input_tokens": 3934,
      "cache_read_input_tokens": 10910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3934,
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

_source line 19 · 2026-05-12T01:17:52.666Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MqtMqhxCvgKtgsGY92TGA3`</summary>

```json
{
  "query": "execution-grounded behavioral specifications preconditions postconditions invariants LLM code generation refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72ef2cfd-87b7-4d1e-a3e2-4e3b3d568055",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnwyzyFA6HHwJXuY99m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef6f041a-5594-461a-8935-bce261ba631b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDjXuE21p1gR3mJBhsCA5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 362,
      "cache_creation_input_tokens": 3934,
      "cache_read_input_tokens": 10910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3934,
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

_source line 20 · 2026-05-12T01:17:53.074Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CbJXedcBjxKR2Ch2b6Be44`</summary>

```json
{
  "query": "\"Spec-Driven Development\" OR \"specification-driven code generation\" LLM preconditions postconditions invariants 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef6f041a-5594-461a-8935-bce261ba631b",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnwyzyFA6HHwJXuY99m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b02893f-2635-4db0-a43a-c266fe9f9c1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDjXuE21p1gR3mJBhsCA5T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 362,
      "cache_creation_input_tokens": 3934,
      "cache_read_input_tokens": 10910,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3934
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 362,
          "output_tokens": 318,
          "cache_read_input_tokens": 10910,
          "cache_creation_input_tokens": 3934,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3934,
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

_source line 21 · 2026-05-12T01:18:01.504Z_

<details><summary>↩ Tool result · `toolu_01MqtMqhxCvgKtgsGY92TGA3`</summary>

```text
Web search results for query: "execution-grounded behavioral specifications preconditions postconditions invariants LLM code generation refinement"

Links: [{"title":"Integrating Symbolic Execution with LLMs for Automated Generation of Program Specifications","url":"https://arxiv.org/html/2506.09550v4"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268"},{"title":"Potential Runtime Error-Guided Specification Synthesis for ...","url":"https://www.arxiv.org/pdf/2512.24594"},{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"[2506.09550] Integrating Symbolic Execution with LLMs for Automated Generation of Program Specifications","url":"https://arxiv.org/abs/2506.09550"},{"title":"FormalSpecCpp: A Dataset of C++ Formal Specifications created using LLMs","url":"https://arxiv.org/pdf/2502.15217"},{"title":"CodeLLMPaper/data/papers/labels/program_verification.md at main · PurCL/CodeLLMPaper","url":"https://github.com/PurCL/CodeLLMPaper/blob/main/data/papers/labels/program_verification.md"},{"title":"Transactions on Artificial Intelligence https://www.sciltp.com/journals/tai","url":"https://media.sciltp.com/articles/2505000685/2505000685.pdf"},{"title":"ClassInvGen: Class Invariant Synthesis Using Large Language Models | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99991-8_4"}]

Based on the search results, I found several highly relevant papers and resources on execution-grounded behavioral specifications, preconditions, postconditions, invariants, and LLM-based code generation and refinement:

## Key Research Areas

**1. Integrating Symbolic Execution with LLMs for Program Specifications**

A novel framework integrates symbolic execution with large language models to automatically synthesize formally verified program specifications. This method employs symbolic execution to derive precise strongest postconditions for loop-free code segments, and these results along with automatically generated invariant templates guide the LLM to propose and iteratively refine loop invariants until a correct specification is obtained.

**2. Execution-Based Behavioral Specification Evaluation**

One approach mandates fixed function names (preconditions and postconditions), requires the exclusive use of assert statements, forbids return values, and enforces a strictly defined output format limited to a single Python code block. Unlike some alternatives, execution-based evaluation approaches support preconditions in addition to postconditions.

**3. Model-Authored Specifications (Self-Spec)**

A formal specification methodology targets precise pre-/post-conditions and type/refinement invariants, along with input domain restrictions, corner cases, error/exception policy, and resource/complexity constraints. This approach involves the model designing its own specification schema, instantiating it from natural language with placeholders, running a minimal interviewer loop to resolve unknowns, and then generating code only from that contract.

**4. Iterative Refinement Mechanisms**

During the refinement process depending on verifier feedback, syntax errors are repaired directly, weak invariants are strengthened, invariants failing certain checks are weakened or adjusted, and invariants failing all checks are discarded and regenerated.

**5. Formal Specifications for C++ Programs**

Preconditions and postconditions serve as formal specifications that define the expected state of a program before and after code execution, ensuring software correctness, formal verification, and code reliability.

These resources demonstrate the active intersection of behavioral specifications, program verification, and large language models in contemporary software engineering research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef6f041a-5594-461a-8935-bce261ba631b",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "b75c8f66-630e-458e-b62c-15879ebdb319",
  "sourceToolAssistantUUID": "ef6f041a-5594-461a-8935-bce261ba631b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T01:18:02.771Z_

<details><summary>↩ Tool result · `toolu_01CbJXedcBjxKR2Ch2b6Be44`</summary>

```text
Web search results for query: ""Spec-Driven Development" OR "specification-driven code generation" LLM preconditions postconditions invariants 2025 2026"

Links: [{"title":"Spec-driven development. Unpacking one of 2025’s key new… | by Thoughtworks | Medium","url":"https://thoughtworks.medium.com/spec-driven-development-d85995a81387"},{"title":"Spec-driven development: Unpacking one of 2025’s key new AI-assisted engineering practices | Thoughtworks United States","url":"https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices"},{"title":"Spec-Driven Development with AI: Write the Spec First, Then Prompt the Implementation - Java Code Geeks","url":"https://www.javacodegeeks.com/2026/05/spec-driven-development-with-ai-write-the-spec-first-then-prompt-the-implementation.html"},{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878v1"},{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"Automatic Generation of Formal Specification and Verification Annotations Using LLMs and Test Oracles1footnote 11footnote 1Preprint. Intended for submission to Science of Computer Programming.","url":"https://arxiv.org/html/2601.12845v1"},{"title":"Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants","url":"https://arxiv.org/html/2602.00180v1"},{"title":"What Is Spec-Driven Development? A Complete Guide | Augment Code","url":"https://www.augmentcode.com/guides/what-is-spec-driven-development"},{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"Towards Specification-Driven LLM-Based Generation of Embedded Automotive Software","url":"https://arxiv.org/html/2411.13269v1"}]

I found comprehensive results on Spec-Driven Development with LLMs, preconditions, postconditions, and invariants. Here's what the search revealed:

## Overview of Spec-Driven Development

A specification should explicitly define the external behavior of the target software — things like input/output mappings, preconditions/postconditions, invariants, constraints, interface types, integration contracts and sequential logic/state machines.

Today, with the help of LLMs, we can describe them using natural language.

## Recent Research and Evolution (2025-2026)

Spec-driven development remains an emerging practice as 2025 draws to a close; we're likely to see even more change in 2026. Peer-reviewed research presented at ICSE 2026 made this case quantitatively: incorporating architectural documentation substantially improves LLM-assisted code generation, with measurable gains in functional correctness, architectural conformance, and code modularity.

## Challenges and Considerations

Code generation from spec to LLMs isn't deterministic; this poses challenges when it comes to upgrades and maintenance. Spec drift and hallucination are inherently difficult to avoid, so we still need highly deterministic CI/CD practices to ensure software quality and safeguard our architectures.

## Formal Specification Generation

Recent work has focused on automatically generating formal specifications. LLMs can automatically generate annotations for programs written in Dafny, a verification-aware programming language, starting from conventional code accompanied by natural language specifications (in comments) and test code. A multimodel approach combining Claude Opus 4.5 and GPT-5.2 generated correct annotations for 98.2% of the programs within at most 8 repair iterations, using verifier feedback.

## Benchmark Development

While models achieve high pass rates in solution generation, their performance drops sharply for executable behavioral specification generation. CodeSpecBench is a benchmark for executable behavioral specification generation with an execution-based evaluation protocol that covers both function-level and repository-level tasks, represents specifications as executable Python preconditions and postconditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b02893f-2635-4db0-a43a-c266fe9f9c1e",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "c4efa8b5-44cf-40cf-aae7-0331ff0877f0",
  "sourceToolAssistantUUID": "1b02893f-2635-4db0-a43a-c266fe9f9c1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T01:18:07.488Z_

<details><summary>↩ Tool result · `toolu_016FF6AAF279EQTAgLAg7teY`</summary>

```text
# PGS: Effective LLM Code Refinement - Key Findings

## Abstract

The paper introduces the Property-Generated Solver (PGS), a framework addressing functional correctness in LLM-generated code. The researchers argue that "effective feedback for LLM-based code refinement must be both property-oriented and structurally minimal," shifting focus from test quantity to quality. PGS achieves a bug fix rate "1.4x-1.6x higher than the strongest debugging-based approaches."

## Core Methodology

**Generator-Tester Architecture:**
The framework employs two collaborative agents. The Generator produces and refines code; the Tester validates against high-level properties and provides minimal counterexample feedback. The cycle continues for up to five refinement iterations.

**Key Process Steps:**
1. Initial code generation from problem specifications
2. Property definition based on problem descriptions (5 candidate properties per round)
3. Input synthesis using LLM-driven techniques (64 test inputs per round)
4. Property-driven validation via instrumented code with assertion checks
5. Minimal counterexample selection using input token count as the primary metric
6. Feedback-driven refinement based on property violations

**Property-Oriented Approach:**
Properties encode high-level semantic rules (e.g., "sorted output must be non-decreasing"). The framework validates these properties rather than relying solely on input-output pairs, leveraging the "asymmetry of verification" principle where verification accuracy (87.0%) substantially exceeds generation accuracy (63.0%).

**Structural Minimality:**
The paper establishes that minimal input token count provides the optimal proxy for complexity. Across three candidate metrics (line coverage, runtime, token count), the "min" strategy consistently outperformed alternatives, with token count proving most effective.

## Key Results

**Benchmark Performance (pass@1 scores, DeepSeek-R1-32B model):**
- HumanEval: 97.6% (vs. Reflexion baseline at 95.1%)
- MBPP: 87.2% (vs. Self-Debug baseline at 84.4%)
- LiveCodeBench: 76.5% (vs. Self-Debug baseline at 72.5%)
- CodeContests: 49.7% (vs. Self-Debug baseline at 45.8%)
- SWE-Bench: 37.3% (vs. SWE-agent baseline at 34.4%)

**Fix Rates (percentage of initially-failed cases resolved):**
- HumanEval: 53.8% to 67.9% depending on model capability
- LiveCodeBench: Framework closes 71% of the gap between baseline and oracle ceiling

**Cost-Effectiveness:**
PGS consumes 1.6× more tokens per iteration than simpler baselines but achieves superior performance after only 2 iterations while matching final performance of competitors after 5 iterations.

## Benchmarks Evaluated

- **HumanEval:** 164 handwritten Python problems
- **MBPP:** ~500 crowd-sourced entry-level problems
- **LiveCodeBench (v5):** 880 live programming contest problems
- **CodeContests:** 117 competition-level problems from the official valid split
- **SWE-Bench (Verified split):** 500 real-world bug-fixing scenarios from GitHub repositories

## Models Tested

- DeepSeek-Coder-V2
- Qwen2.5-Coder
- DeepSeek-R1-Distilled-32B
- Qwen3-30B
- DeepSeek-V3.1
- Claude-Sonnet-4

## Baselines Compared

**TDD Frameworks:** Code-T, Reflexion
**Self-Correction Methods:** Self-Edit, Self-Debugger, MGDebugger, LDB
**Repository-Level:** SWE-agent

## Related Work Discussion

The paper acknowledges prior work on specification-based testing and formal specifications. It references research on "generating formal specifications" and "properties for program verification," but positions its contribution as the first to systematically investigate "how to leverage property violations as actionable feedback for automated refinement." The work distinguishes itself from prior property-based testing research by emphasizing minimized counterexamples as essential refinement signals.

The framework builds upon delta-debugging principles for input minimization but extends this "into a property-driven paradigm: instead of minimizing inputs for I/O mismatches, PGS minimizes counterexamples violating high-level semantic properties."

## Limitations

The paper does not explicitly discuss limitations but notes that future work should focus on "enhancing autonomous property discovery," suggesting current property generation relies on LLM synthesis rather than fully autonomous derivation. The framework's effectiveness depends on synthesizing semantically rich test inputs—a capability that "simple random or fuzzing techniques often prove insufficient" for achieving.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72ef2cfd-87b7-4d1e-a3e2-4e3b3d568055",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "c28d6313-b532-45e6-b19a-84065d43fdae",
  "sourceToolAssistantUUID": "72ef2cfd-87b7-4d1e-a3e2-4e3b3d568055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-12T01:18:09.989Z_

Now let me fetch a couple more key related papers for the comparison analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c28d6313-b532-45e6-b19a-84065d43fdae",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnyeDeT4eCmaR9sJpoT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0f161ae-409f-4717-92d6-75c91eb43878",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QMKbKAddjWsvwX1aDTyioQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2126,
      "cache_creation_input_tokens": 1941,
      "cache_read_input_tokens": 14844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1941,
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

_source line 25 · 2026-05-12T01:18:12.501Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015skFqL4s54x79ifdoaKNhH`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.12268",
  "prompt": "Extract the abstract, key methodology, and results of CodeSpecBench. How does it define behavioral specifications (preconditions, postconditions)? How do LLMs perform at generating executable specifications? What is the gap between code generation and specification generation performance?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0f161ae-409f-4717-92d6-75c91eb43878",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnyeDeT4eCmaR9sJpoT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0da9fda0-6024-48bc-96e9-4e5074692b32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QMKbKAddjWsvwX1aDTyioQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2126,
      "cache_creation_input_tokens": 1941,
      "cache_read_input_tokens": 14844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1941,
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

_source line 26 · 2026-05-12T01:18:13.920Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01W1CUYf7aNVUkpFc9zVSSEt`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.00180v1",
  "prompt": "Extract the abstract, methodology, and key findings of this Spec-Driven Development paper. How does it use contracts (preconditions, postconditions, invariants) with AI coding assistants? What results does it report? How does it compare to test-driven approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0da9fda0-6024-48bc-96e9-4e5074692b32",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnyeDeT4eCmaR9sJpoT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf64ada5-9a1d-416c-9d7a-bbcfd6ef1ec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QMKbKAddjWsvwX1aDTyioQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2126,
      "cache_creation_input_tokens": 1941,
      "cache_read_input_tokens": 14844,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1941,
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

_source line 27 · 2026-05-12T01:18:15.737Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CLPXetwpSPJ81XWpW2ARWt`</summary>

```json
{
  "url": "https://openreview.net/pdf?id=6pr7BUGkLp",
  "prompt": "Extract the abstract, methodology, and key results of Self-Spec. How does it use model-authored specifications (preconditions, postconditions, invariants, type constraints) for LLM code generation? What improvements does it claim? How does it compare to test-based approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf64ada5-9a1d-416c-9d7a-bbcfd6ef1ec3",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnyeDeT4eCmaR9sJpoT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f10767fb-5989-4b11-9ddd-427ad7f08c94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QMKbKAddjWsvwX1aDTyioQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2126,
      "cache_creation_input_tokens": 1941,
      "cache_read_input_tokens": 14844,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1941
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2126,
          "output_tokens": 410,
          "cache_read_input_tokens": 14844,
          "cache_creation_input_tokens": 1941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1941,
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

_source line 28 · 2026-05-12T01:18:18.042Z_

<details><summary>↩ Tool result · `toolu_015skFqL4s54x79ifdoaKNhH`</summary>

```text
# CodeSpecBench: Executable Behavioral Specification Generation

## Abstract

CodeSpecBench is a benchmark evaluating how well large language models can generate executable behavioral specifications from natural language. The researchers assessed 15 state-of-the-art LLMs across function-level and repository-level tasks, finding that "specification generation is substantially more challenging than code generation" and that models achieve only 20.2% pass rate on repository-level tasks.

## Definition of Behavioral Specifications

The benchmark represents specifications through two complementary components:

**Preconditions** define input validity and constraints. They "specify the conditions that a function's inputs and relevant program state must satisfy before execution."

**Postconditions** characterize expected outputs and state changes. They "specify the properties that must hold after a function executes successfully."

These are expressed as executable Python functions, enabling direct evaluation against test cases.

## LLM Performance Results

**Function-level tasks (CodeSpecBench-Func):** Best-performing models achieve 47% pass rate (GPT-5-mini), with strong correctness but weak completeness—models generate overly permissive specifications accepting invalid behaviors.

**Repository-level tasks (CodeSpecBench-Repo):** Performance drops sharply, with Claude-4.5-Sonnet achieving only 20.2% pass rate. Here, specifications become overly restrictive, rejecting valid behaviors.

## Specification vs. Code Generation Gap

The performance disparity is striking: while Claude-4.5-Sonnet achieves 77.2% on code generation, its specification generation reaches only 21%. This indicates that "solving tasks does not necessarily imply the ability to generate precise executable behavioral constraints."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0da9fda0-6024-48bc-96e9-4e5074692b32",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "9b704151-d099-4cbd-83bd-752b970788e4",
  "sourceToolAssistantUUID": "0da9fda0-6024-48bc-96e9-4e5074692b32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-12T01:18:20.339Z_

<details><summary>↩ Tool result · `toolu_01W1CUYf7aNVUkpFc9zVSSEt`</summary>

```text
# Spec-Driven Development: Abstract, Methodology & Key Findings

## Abstract

The paper presents an approach where specifications—rather than code—serve as the primary development artifact. As noted: "make the specification the source of truth, and let code derive from it." The work addresses how AI coding assistants benefit from unambiguous, executable contracts that reduce guesswork during code generation.

## Methodology

The paper establishes a three-tier specification framework:

1. **Spec-First**: Specifications guide initial development but may drift afterward
2. **Spec-Anchored**: Specifications evolve alongside code with enforced synchronization
3. **Spec-as-Source**: Specifications are the only human-edited artifact; code is entirely generated

A four-phase workflow governs implementation: Specify (define behavior), Plan (establish constraints), Implement (produce code), and Validate (verify alignment).

## Key Findings on AI Integration

The research suggests "controlled studies showing error reductions of up to 50%" when AI receives refined specifications rather than vague prompts. AI agents benefit because specifications "break down complex problems into modular components aligned with agents' context windows," enabling parallel execution across non-overlapping tasks.

**Contract Implementation**: While the paper emphasizes specifications rather than formal contracts (preconditions/postconditions/invariants), it demonstrates how API specifications like OpenAPI function as executable contracts validated through automated testing tools such as Specmatic and Pact.

## Comparison to Test-Driven Development

The relationship is evolutionary: "SDD is not a replacement for existing development practices—it builds on and extends them." Test-driven development operates at unit scope; spec-driven development applies similar "specify-first" discipline at feature, system, and architectural levels. The paper treats BDD as "the most direct ancestor of modern SDD," with Gherkin scenarios serving as executable specifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf64ada5-9a1d-416c-9d7a-bbcfd6ef1ec3",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "ac71aa7c-dcae-4e42-96dc-3f435847419c",
  "sourceToolAssistantUUID": "cf64ada5-9a1d-416c-9d7a-bbcfd6ef1ec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T01:18:20.596Z_

<details><summary>↩ Tool result · `toolu_01CLPXetwpSPJ81XWpW2ARWt`</summary>

```text
I appreciate your request, but I'm unable to extract the information you're seeking from the provided content. The document appears to be a PDF file encoded in binary format containing compressed streams and object references, which renders as unreadable data rather than accessible text.

The content shows PDF structural elements (objects, streams, filters like /FlateDecode) but doesn't display the human-readable article text about Self-Spec that would allow me to identify:

- The abstract describing the work
- Methodology details about model-authored specifications
- Key results and performance improvements
- Comparative analysis with test-based approaches

**To help you effectively, I would need:**

1. The article text in a readable format (plain text, properly extracted PDF, or HTML)
2. Direct access to the Self-Spec paper or its published version

If you can provide the source material in readable form, I'd be happy to extract the abstract, methodology, key results, and comparative insights while adhering to your character limits for quotations and attribution requirements.

[Binary content (application/pdf, 413.5KB) also saved to /home/ubuntu/.claude-account-1/projects/-/0c4993e7-0796-4f8d-9f5d-3891a1eae067/tool-results/webfetch-1778548696532-3w8hj1.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f10767fb-5989-4b11-9ddd-427ad7f08c94",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "a87fe807-7623-4b5f-bf56-db616dd312a2",
  "sourceToolAssistantUUID": "f10767fb-5989-4b11-9ddd-427ad7f08c94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-12T01:18:26.146Z_

Let me search for Self-Spec in a more accessible format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a87fe807-7623-4b5f-bf56-db616dd312a2",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnzcHbDPRqarBhuKG7X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a54f7c1-e2eb-47c9-8915-3ea59c09c951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018B1c54AGRcgS1vqqN4w8NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3711,
      "cache_read_input_tokens": 16785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3711,
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

_source line 32 · 2026-05-12T01:18:26.597Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FLKUrnSCxYPme3qgdq7xSF`</summary>

```json
{
  "query": "Self-Spec model-authored specifications reliable LLM code generation preconditions postconditions results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a54f7c1-e2eb-47c9-8915-3ea59c09c951",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011CawnzcHbDPRqarBhuKG7X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d8f06ff-4bbf-44ac-b9c5-f973c4d7a3f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018B1c54AGRcgS1vqqN4w8NC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3711,
      "cache_read_input_tokens": 16785,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3711
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 16785,
          "cache_creation_input_tokens": 3711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3711,
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

_source line 33 · 2026-05-12T01:18:34.824Z_

<details><summary>↩ Tool result · `toolu_01FLKUrnSCxYPme3qgdq7xSF`</summary>

```text
Web search results for query: "Self-Spec model-authored specifications reliable LLM code generation preconditions postconditions results"

Links: [{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation | OpenReview","url":"https://openreview.net/forum?id=6pr7BUGkLp"},{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"SpecGen: Automated Generation of Formal Program Specifications via Large Language Models","url":"https://arxiv.org/html/2401.08807v1"},{"title":"FormalSpecCpp: A Dataset of C++ Formal Specifications created using LLMs","url":"https://arxiv.org/pdf/2502.15217"},{"title":"Beyond Postconditions: Can Large Language Models infer Formal Contracts for","url":"https://arxiv.org/pdf/2510.12702"},{"title":"Clover: Closed-Loop Verifiable Code Generation Chuyue Sun1⋆ Ying Sheng1∗","url":"https://theory.stanford.edu/~barrett/pubs/SSP+24.pdf"},{"title":"Benchmarking Large Language Models for Compositional ...","url":"https://arxiv.org/pdf/2509.23061"},{"title":"DafnyBench: A Benchmark for Formal Software Verification Chloe Loughridge∗","url":"https://namin.seas.harvard.edu/pubs/dafnybench.pdf"},{"title":"Supporting Software Formal Verification with Large ...","url":"https://arxiv.org/pdf/2507.04857"}]

Based on the search results, I found comprehensive information about **Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation**. Here are the key findings:

## Overview

Self-Spec investigates whether large language models (LLMs) code more reliably when they first author a task-specific specification language and then implement strictly from that spec.

## Methodology

Self-Spec uses a lightweight, deterministic (T=0) orchestration that prompts a model to (i) design a compact spec schema it prefers, (ii) instantiate that schema from a problem's docstring and signature, (iii) resolve ambiguities via a minimal Q&A loop, and (iv) generate code only from the confirmed spec.

## Key Insight

The intuition is distributional: a self-authored spec better aligns with a model's internal representational bias, reducing docstring drift and format/edge-case mistakes.

## Results

On HumanEval (pass@1, single sample), Self-Spec improves over direct NL→code for stronger models: GPT-4o 87%→92% (+5) and Claude 3.7 92%→94% (+2); Claude 3.5 dips 90%→89% (-1), which returns to baseline once we remove over-defensive guards in generated code.

## Significance

This is the first systematic study that lets an LLM design its own spec language for coding. The method is simple (no finetuning), model-agnostic (each model chooses its spec shape), and practical (assumptions are made explicit).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d8f06ff-4bbf-44ac-b9c5-f973c4d7a3f6",
  "isSidechain": true,
  "promptId": "b0b8e258-9af8-4c3c-8dcb-bf36ed135cca",
  "agentId": "a20bbcc43498984e4",
  "type": "user",
  "uuid": "272d6f65-a2bd-4533-9449-d33b4642bbba",
  "sourceToolAssistantUUID": "4d8f06ff-4bbf-44ac-b9c5-f973c4d7a3f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-12T01:19:42.990Z_

I now have comprehensive information to provide a detailed report. Here is my analysis:

---

## 1. Does the paper exist?

**Yes, it exists.** The paper is at arXiv:2506.18315, submitted June 23, 2025. However, its actual title is **"Use Property-Based Testing to Bridge LLM Code Generation and Validation"** -- not "PGS Property-Generated Solver" as a title. The framework introduced in the paper is called **Property-Generated Solver (PGS)**. The authors are **Lehan He, Zeren Chen, Zhe Zhang, Xiang Gao, and Lu Sheng**.

- arXiv page: https://arxiv.org/abs/2506.18315
- HTML version: https://arxiv.org/html/2506.18315

## 2. What exactly does it do?

PGS is a two-agent framework for iterative LLM code refinement:

- **Generator agent**: Produces and iteratively refines code.
- **Tester agent**: Manages the Property-Based Testing (PBT) lifecycle -- it synthesizes high-level semantic properties (e.g., "a sorted output must be non-decreasing"), generates test inputs (64 per round), validates code against those properties via instrumented assertion checks, and selects the **structurally minimal failing counterexample** (measured by input token count) to feed back to the Generator.

The key thesis is that **effective feedback must be both property-oriented and structurally minimal**. Rather than relying on specific input-output test cases (as TDD methods do), PGS validates against high-level invariants and provides the simplest failing input as feedback. This exploits a "verification asymmetry" -- the paper reports that property verification accuracy (87.0%) substantially exceeds code generation accuracy (63.0%), meaning LLMs are better at checking properties than writing correct code.

The loop runs for up to 5 refinement iterations per problem, generating 5 candidate properties per round.

## 3. What results does it actually claim?

The specific numbers you asked about are **partially correct but partially wrong**:

**The 13.4% pass@1 improvement claim**: The paper does report "up to 13.4% improvement" over TDD methods in some framing, but the more prominent headline result in the full paper is **23.1% to 37.3% relative gains** in pass@1 over established TDD methods. The 13.4% figure appears to be an absolute improvement number in certain benchmark configurations, while the 23-37% figures are relative gains.

**The 1.4-1.6x bug fix rate claim**: **Confirmed.** The paper explicitly claims bug fix rates 1.4x-1.6x higher than the strongest debugging-based approaches.

**Specific benchmark results (using DeepSeek-R1-32B)**:
- HumanEval: 97.6% pass@1 (vs. 95.1% Reflexion baseline)
- MBPP: 87.2% (vs. 84.4% Self-Debug)
- LiveCodeBench: 76.5% (vs. 72.5% Self-Debug)
- CodeContests: 49.7% (vs. 45.8% Self-Debug)
- SWE-Bench Verified: 37.3% (vs. 34.4% SWE-agent)

**Fix rate**: Over 64% success rate on initially failing problems. On LiveCodeBench, PGS closes 71% of the gap between baseline and oracle ceiling.

**Cost**: PGS consumes 1.6x more tokens per iteration than simpler baselines but reaches superior performance after only 2 iterations.

**Baselines compared against**: Code-T, Reflexion (TDD frameworks); Self-Edit, Self-Debugger, MGDebugger, LDB (self-correction methods); SWE-agent (repository-level).

**Models tested**: DeepSeek-Coder-V2, Qwen2.5-Coder, DeepSeek-R1-Distilled-32B, Qwen3-30B, DeepSeek-V3.1, Claude Sonnet 4.

## 4. How does PGS compare to an approach using execution-grounded behavioral specifications (preconditions, postconditions, invariants, type constraints) as intermediate reasoning?

This is the most important question, and the answer requires nuance. There are several related but distinct lines of work:

### PGS vs. Behavioral Specifications -- Conceptual Overlap and Differences

**Overlap**: PGS's "high-level program properties" are conceptually close to postconditions and invariants. When PGS checks that "a sorting function produces a non-decreasing sequence," that is essentially a postcondition. The framework is validating semantic properties that the output must satisfy -- this is the same conceptual space as behavioral specifications.

**Key differences**:

| Dimension | PGS (Property-Based Testing) | Execution-Grounded Behavioral Specs |
|---|---|---|
| **Specification type** | LLM-synthesized properties checked via assertion + random inputs | Formal or semi-formal preconditions, postconditions, invariants, type constraints |
| **Verification method** | Property-based testing (generate many inputs, check assertions) | Execution against spec contracts, potentially with symbolic execution or runtime monitoring |
| **Feedback mechanism** | Minimal failing counterexample | Spec violation diagnosis (which precondition/postcondition/invariant failed and why) |
| **Specification completeness** | Partial -- 5 properties per round, may miss edge cases | Aims for complete behavioral contracts |
| **Role of specs** | Feedback signal for iterative refinement | Intermediate reasoning artifact that structures the generation process |
| **Expressiveness** | Limited to properties testable via assertion on concrete inputs | Can express relational properties, state transitions, resource constraints, exception contracts |

### Closely Related Work in the Specification Space

Several recent papers are directly relevant to the behavioral specification approach you described:

1. **Self-Spec (OpenReview, 2025-2026)**: Has the LLM design its own specification schema, then instantiate preconditions/postconditions from the problem description, resolve ambiguities via Q&A, and generate code only from the confirmed spec. Results: +5 pass@1 on HumanEval for GPT-4o (87% to 92%), +2 for Claude 3.7 (92% to 94%). This is the closest to "using behavioral specifications as intermediate reasoning" but focuses on the generation phase rather than iterative refinement.

2. **CodeSpecBench (arXiv:2604.12268, April 2026)**: A benchmark specifically for executable behavioral specification generation. Key finding: specification generation is much harder than code generation. Claude 4.5 Sonnet achieves 77.2% on code generation but only 21% on specification generation. This suggests a fundamental bottleneck -- LLMs struggle to generate precise, executable behavioral specs even when they can write the code.

3. **Spec-Driven Development (arXiv:2602.00180, Feb 2026)**: A framework where specifications are the primary development artifact. Reports error reductions of up to 50% when AI receives refined specifications. Treats BDD/Gherkin as executable specifications.

4. **Symbolic Execution + LLM Specs (arXiv:2506.09550)**: Integrates symbolic execution to derive strongest postconditions for loop-free segments, then uses LLMs to propose loop invariants. Achieves formally verified specifications.

### Critical Assessment

The PGS approach and the behavioral-specification approach occupy overlapping but distinct niches:

- **PGS is pragmatic**: It sidesteps the difficulty of generating complete formal specifications (which CodeSpecBench shows LLMs are bad at) by instead generating partial, testable properties and using them as a feedback signal. It does not require the specifications to be complete or formally verified -- just accurate enough to catch bugs.

- **Behavioral specifications as intermediate reasoning** is more ambitious: It aims to have the LLM reason through preconditions/postconditions/invariants/type constraints as a structured thinking step before or during code generation. This could potentially be more powerful (richer feedback, more systematic reasoning), but faces the specification-generation bottleneck identified by CodeSpecBench (only ~20% pass rate on repo-level spec generation).

- **PGS's main advantage** is that it only needs properties to be *approximately correct* and *partially covering* -- the verification asymmetry means even imperfect properties catch real bugs. A full behavioral specification approach demands higher spec quality.

- **A behavioral specification approach's main advantage** would be richer, more structured feedback (not just "this input fails property X" but "this function violates its postcondition under these preconditions, which implies the invariant is broken at this point"). This could yield more targeted fixes, especially for complex multi-function or stateful code.

- **Neither approach has been directly compared** in the literature as of mid-2026. PGS compares against TDD and self-debugging baselines, not against specification-driven generation. Self-Spec compares against direct NL-to-code, not against PGS-style property feedback.

### Bottom Line

The paper is real and its claims are substantiated by experiments across 5 benchmarks and 6 models. The reported improvements (23-37% relative pass@1 gains over TDD, 1.4-1.6x fix rates over debugging approaches) are specific to comparing against test-case-based feedback, not against specification-based approaches. An approach using execution-verified behavioral specifications as intermediate reasoning would be a conceptually related but methodologically distinct alternative that has not been directly benchmarked against PGS. The CodeSpecBench results suggest that the main challenge for spec-based approaches is the difficulty LLMs have in generating precise executable specifications, which PGS avoids by only requiring partial, approximately-correct properties.

Sources:
- [PGS paper (arXiv:2506.18315)](https://arxiv.org/abs/2506.18315)
- [PGS full HTML](https://arxiv.org/html/2506.18315)
- [CodeSpecBench (arXiv:2604.12268)](https://arxiv.org/html/2604.12268)
- [Spec-Driven Development (arXiv:2602.00180)](https://arxiv.org/html/2602.00180v1)
- [Self-Spec (OpenReview)](https://openreview.net/forum?id=6pr7BUGkLp)
- [Symbolic Execution + LLM Specs (arXiv:2506.09550)](https://arxiv.org/abs/2506.09550)
- [Understanding Specification-Driven Code Generation (arXiv:2601.03878)](https://arxiv.org/html/2601.03878v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "272d6f65-a2bd-4533-9449-d33b4642bbba",
  "isSidechain": true,
  "agentId": "a20bbcc43498984e4",
  "requestId": "req_011Cawo1f6HZKQDiHuNwotQX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "430a877f-2bde-4fa2-bf6c-9da0c866c7e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c4993e7-0796-4f8d-9f5d-3891a1eae067",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBpiB7kyVnLZfrx4LN48oi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 20496,
      "output_tokens": 2571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 937
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2571,
          "cache_read_input_tokens": 20496,
          "cache_creation_input_tokens": 937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 937,
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
