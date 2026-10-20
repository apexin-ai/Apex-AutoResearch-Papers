# Research conversation: Search the web for the paper "ARISE: Repository-level Graph Representation for Agentic Fault Localization and Repair" (a

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a33c9ea291d6d06b2.jsonl`
- **Structured JSON:** [`e9635af75a85ece6d191.json`](../../sessions/e9/e9635af75a85ece6d191.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-10T18:40:23.540Z_

Search the web for the paper "ARISE: Repository-level Graph Representation for Agentic Fault Localization and Repair" (arXiv:2605.03117). I need to verify:
1. Does this paper actually exist on arXiv?
2. Does it use def-use edges as runtime tool calls?
3. Does it report +17pp Function Recall@1 on SWE-bench Lite?
4. Does it report 4.7pp Pass@1 improvement?

Use WebSearch to find this paper and WebFetch to read its abstract/details if possible. Report exactly what you find — do not fabricate details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a33c9ea291d6d06b2",
  "type": "user",
  "uuid": "bbef29f4-cbbc-4727-8e9d-55d08167be58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:40:23.543Z_

```json
{
  "parentUuid": "bbef29f4-cbbc-4727-8e9d-55d08167be58",
  "isSidechain": true,
  "agentId": "a33c9ea291d6d06b2",
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
  "uuid": "0e6e46d6-f76d-4e45-bcd0-0482f09f2b43",
  "timestamp": "2026-05-10T18:40:23.543Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:40:26.074Z_



I'll search for this paper. Let me first load the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e6e46d6-f76d-4e45-bcd0-0482f09f2b43",
  "isSidechain": true,
  "agentId": "a33c9ea291d6d06b2",
  "requestId": "req_011CauNqdBMt584m8UGFb6X9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23968620-a6a1-42ee-9878-78df7debfbab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VunEciJyRx5RULgHYbnNuq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 693,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T18:40:26.597Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01J4MhHPUrsa23NM6LVerVaF`</summary>

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
  "parentUuid": "23968620-a6a1-42ee-9878-78df7debfbab",
  "isSidechain": true,
  "agentId": "a33c9ea291d6d06b2",
  "requestId": "req_011CauNqdBMt584m8UGFb6X9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0654b5c-6871-4b56-8789-d0397741ab4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VunEciJyRx5RULgHYbnNuq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 8223,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 693
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 693,
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

_source line 5 · 2026-05-10T18:40:26.601Z_

<details><summary>↩ Tool result · `toolu_01J4MhHPUrsa23NM6LVerVaF`</summary>

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
  "parentUuid": "f0654b5c-6871-4b56-8789-d0397741ab4f",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a33c9ea291d6d06b2",
  "type": "user",
  "uuid": "2b6f4791-f7b3-46d2-a270-71701e76fc77",
  "sourceToolAssistantUUID": "f0654b5c-6871-4b56-8789-d0397741ab4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:40:29.476Z_



Now let me search for this paper and fetch its arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b6f4791-f7b3-46d2-a270-71701e76fc77",
  "isSidechain": true,
  "agentId": "a33c9ea291d6d06b2",
  "requestId": "req_011CauNqr4mDGeTgTETsutw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9084e3bb-7e64-4255-b515-5d2e08fc0465",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016akHpMB2HrEHE59uzpsxJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-10T18:40:30.989Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017PLMHv8YoofVejMmLzwomo`</summary>

```json
{
  "query": "ARISE Repository-level Graph Representation Agentic Fault Localization Repair arXiv 2605.03117"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9084e3bb-7e64-4255-b515-5d2e08fc0465",
  "isSidechain": true,
  "agentId": "a33c9ea291d6d06b2",
  "requestId": "req_011CauNqr4mDGeTgTETsutw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65b0bb33-6b07-418c-b7c7-f26d2c02ae08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016akHpMB2HrEHE59uzpsxJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-10T18:40:31.512Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L8SwwbzytnnFQXkk5EYowu`</summary>

```json
{
  "query": "arXiv 2605.03117 ARISE def-use edges SWE-bench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65b0bb33-6b07-418c-b7c7-f26d2c02ae08",
  "isSidechain": true,
  "agentId": "a33c9ea291d6d06b2",
  "requestId": "req_011CauNqr4mDGeTgTETsutw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f72f871-b7ba-4f87-ae0f-b174acd16ba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016akHpMB2HrEHE59uzpsxJE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8916,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 151,
          "cache_read_input_tokens": 8916,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-10T18:40:38.735Z_

<details><summary>↩ Tool result · `toolu_01L8SwwbzytnnFQXkk5EYowu`</summary>

```text
Web search results for query: "arXiv 2605.03117 ARISE def-use edges SWE-bench"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.05417] Signature structure of quadratic response under Zeno-Schur coarse graining in open quantum systems","url":"https://arxiv.org/abs/2605.05417"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving","url":"https://arxiv.org/html/2504.02605v1"},{"title":"ProgramBench: Can Language Models Rebuild Programs From Scratch?","url":"https://arxiv.org/html/2605.03546v1"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"Enhancing Agent Safety Judgment: Controlled Benchmark Rewriting and Analogical Reasoning for Deceptive Out-of-Distribution Scenarios","url":"https://arxiv.org/html/2605.03242"},{"title":"Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving ByteDance Seed","url":"https://arxiv.org/pdf/2504.02605v1"},{"title":"[2512.17419] SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/abs/2512.17419"}]

Based on the search results, here's information about the arXiv paper 2605.03117:

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

The paper addresses a key limitation in existing systems: existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization.

In terms of evaluation, the authors evaluate on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone. The results show significant improvements: ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f72f871-b7ba-4f87-ae0f-b174acd16ba1",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a33c9ea291d6d06b2",
  "type": "user",
  "uuid": "a8282b09-e7fd-4bd4-86f7-ef1c4ef18afb",
  "sourceToolAssistantUUID": "7f72f871-b7ba-4f87-ae0f-b174acd16ba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T18:40:39.352Z_

<details><summary>↩ Tool result · `toolu_017PLMHv8YoofVejMmLzwomo`</summary>

```text
Web search results for query: "ARISE Repository-level Graph Representation Agentic Fault Localization Repair arXiv 2605.03117"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion","url":"https://arxiv.org/html/2409.13642v2"},{"title":"Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://arxiv.org/html/2503.21710v1"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/abs/2604.00167"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"},{"title":"Agentic Code Reasoning","url":"https://arxiv.org/html/2603.01896v1"}]

I found comprehensive information about the paper you searched for. Here's a summary:

## ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges. ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

### Key Problem Addressed

Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization.

### Research Results

The paper evaluates on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone. Compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points. These localization gains translate directly into repair success, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.

The paper was published on arXiv on May 4, 2026 (arXiv 2605.03117) by researchers Shahd Seddik and Fatemeh Fard from the University of British Columbia.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65b0bb33-6b07-418c-b7c7-f26d2c02ae08",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a33c9ea291d6d06b2",
  "type": "user",
  "uuid": "d4ca7f3f-263d-4d87-8da9-43fd79e3ead1",
  "sourceToolAssistantUUID": "65b0bb33-6b07-418c-b7c7-f26d2c02ae08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T18:40:41.820Z_

Let me also fetch the actual arXiv abstract page directly to confirm the details firsthand.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4ca7f3f-263d-4d87-8da9-43fd79e3ead1",
  "isSidechain": true,
  "agentId": "a33c9ea291d6d06b2",
  "requestId": "req_011CauNrn3Si9MwxaqyUcSLA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71600161-d17f-4565-acb0-2af32748194c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TevfNacMtNHDmDNbAE5kDS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 879,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 10826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1131,
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

_source line 12 · 2026-05-10T18:40:43.781Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B3zXt5WymBhPzvBmeDhvpQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.03117",
  "prompt": "Extract the full title, authors, submission date, and complete abstract of this paper. Also note any specific claims about def-use edges, Function Recall@1 improvements, Pass@1 improvements, and SWE-bench Lite results. Report exactly what the page says."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71600161-d17f-4565-acb0-2af32748194c",
  "isSidechain": true,
  "agentId": "a33c9ea291d6d06b2",
  "requestId": "req_011CauNrn3Si9MwxaqyUcSLA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b429df73-1508-4318-a2fe-3422ea9ed905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TevfNacMtNHDmDNbAE5kDS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 879,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 10826,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1131
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 879,
          "output_tokens": 160,
          "cache_read_input_tokens": 10826,
          "cache_creation_input_tokens": 1131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1131,
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

_source line 13 · 2026-05-10T18:40:48.944Z_

<details><summary>↩ Tool result · `toolu_01B3zXt5WymBhPzvBmeDhvpQ`</summary>

```text
# Paper Summary: ARISE

**Full Title:**
"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair"

**Authors:**
Shahd Seddik and Fatemeh Fard

**Submission Date:**
May 4, 2026

**Abstract:**
The paper addresses repository-level fault localization and automated program repair by presenting an LLM-based agent system. It "augments an LLM-based agent with a multi-granularity program graph" that extends from structural relationships down to statement-level nodes with intra-procedural definition-use edges. The system exposes this graph through a tool API enabling data-flow slicing queries.

**Key Performance Claims:**

- **Function Recall@1:** Improved by 17.0 percentage points compared to the baseline
- **Line Recall@1:** Improved by 15.0 percentage points compared to the baseline  
- **Pass@1:** Achieved 22.0% (66/300 issues), representing a 4.7 percentage-point improvement over SWE-agent

**Evaluation:**
Testing occurred on "SWE-bench Lite (300 real GitHub issues, 11 Python repositories)" using Qwen2.5-Coder-32B-Instruct.

The ablations confirmed that the data-flow graph infrastructure, rather than the tool schema alone, drove the improvements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b429df73-1508-4318-a2fe-3422ea9ed905",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "a33c9ea291d6d06b2",
  "type": "user",
  "uuid": "0a56e426-3c11-44e6-bab2-451b882cb8a0",
  "sourceToolAssistantUUID": "b429df73-1508-4318-a2fe-3422ea9ed905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T18:41:01.642Z_

Here are my findings for each of your four questions:

**1. Does this paper actually exist on arXiv?**

Yes. The paper is real and accessible at [arXiv:2605.03117](https://arxiv.org/abs/2605.03117). Its full title is "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair," authored by Shahd Seddik and Fatemeh Fard (University of British Columbia), submitted May 4, 2026.

**2. Does it use def-use edges as runtime tool calls?**

Yes, but with a nuance worth noting. The paper builds a multi-granularity program graph that extends structural relationships down to **statement-level nodes connected by intra-procedural definition-use edges**. These def-use edges are not themselves "tool calls" in the LLM sense; rather, the graph (including the def-use edges) is **exposed to the agent through a three-tier tool API**. This makes data-flow slicing a first-class, queryable agent primitive -- the agent can issue a tool call to trace which statements define or consume a variable. So the def-use edges are the underlying graph data that the agent queries via tool calls at runtime.

**3. Does it report +17pp Function Recall@1 on SWE-bench Lite?**

Yes. The paper reports that ARISE improves **Function Recall@1 by 17.0 percentage points** over the unmodified SWE-agent baseline on SWE-bench Lite (300 real GitHub issues, 11 Python repositories). It also reports a 15.0 percentage-point improvement in Line Recall@1.

**4. Does it report 4.7pp Pass@1 improvement?**

Yes. The paper reports ARISE achieves **22.0% Pass@1 (66/300)**, which is a **4.7 percentage-point improvement** over SWE-agent. The backbone model used was Qwen2.5-Coder-32B-Instruct.

All four claims check out against the actual arXiv listing.

Sources:
- [ARISE paper on arXiv (abstract)](https://arxiv.org/abs/2605.03117)
- [ARISE paper on arXiv (HTML version)](https://arxiv.org/html/2605.03117)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a56e426-3c11-44e6-bab2-451b882cb8a0",
  "isSidechain": true,
  "agentId": "a33c9ea291d6d06b2",
  "requestId": "req_011CauNsV51fa42UL48EhFcb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bb7f638-5860-41c2-b0fa-6a830afbdbae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3fkdfnFCmdzZeBdt9Shtn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1378,
      "cache_read_input_tokens": 11957,
      "output_tokens": 561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1378
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 561,
          "cache_read_input_tokens": 11957,
          "cache_creation_input_tokens": 1378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1378,
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
