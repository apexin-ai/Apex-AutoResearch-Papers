# Research conversation: Search the web for the paper "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a04145d2cd85bfce8.jsonl`
- **Structured JSON:** [`fbefcefc15e78faf9a83.json`](../../sessions/fb/fbefcefc15e78faf9a83.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-10T17:48:56.995Z_

Search the web for the paper "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair" with arXiv ID 2605.03117. I need to verify:
1. Does this paper actually exist?
2. What are its actual claimed results on SWE-bench Lite?
3. Does it report 22.0% Pass@1 and 17pp function-level localization gain?
4. What model does it use?
5. Is its code publicly available?

Use WebSearch to find this paper and if possible WebFetch to read its abstract/details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "a04145d2cd85bfce8",
  "type": "user",
  "uuid": "eceaae9b-ff68-4036-a062-a0110479a13a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T17:48:56.998Z_

```json
{
  "parentUuid": "eceaae9b-ff68-4036-a062-a0110479a13a",
  "isSidechain": true,
  "agentId": "a04145d2cd85bfce8",
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
  "uuid": "c63d141d-ddb9-4a48-a7e0-9ed91ee54acd",
  "timestamp": "2026-05-10T17:48:56.998Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T17:48:59.781Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SugAQH9L5fP3Z8e8Rfbipe`</summary>

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
  "parentUuid": "c63d141d-ddb9-4a48-a7e0-9ed91ee54acd",
  "isSidechain": true,
  "agentId": "a04145d2cd85bfce8",
  "requestId": "req_011CauJv69jRggWe9NT8rLZV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8f4a3ec-e3e0-4618-9aba-6bae14ff2bc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6BHfLTwZk7m6PkiYQnfjr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8911,
      "cache_read_input_tokens": 0,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8911
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8911,
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

_source line 4 · 2026-05-10T17:48:59.786Z_

<details><summary>↩ Tool result · `toolu_01SugAQH9L5fP3Z8e8Rfbipe`</summary>

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
  "parentUuid": "f8f4a3ec-e3e0-4618-9aba-6bae14ff2bc8",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "a04145d2cd85bfce8",
  "type": "user",
  "uuid": "dfc832ba-e189-47ba-ad24-64716dfb9962",
  "sourceToolAssistantUUID": "f8f4a3ec-e3e0-4618-9aba-6bae14ff2bc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T17:49:03.063Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012ce8AtYmUoabwoxVkXggtU`</summary>

```json
{
  "query": "ARISE Repository-level Graph Representation Agentic Fault Localization Program Repair arXiv 2605.03117"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfc832ba-e189-47ba-ad24-64716dfb9962",
  "isSidechain": true,
  "agentId": "a04145d2cd85bfce8",
  "requestId": "req_011CauJvJMCzp8JDxQrqTz33",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48b03be9-ca8e-4798-b54b-b65d013601d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EsQGsFEvhMTkd6wDnRMngv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T17:49:03.373Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TkJXA2pJAufUBrJxPd1gXj`</summary>

```json
{
  "query": "arXiv 2605.03117 ARISE SWE-bench Lite"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48b03be9-ca8e-4798-b54b-b65d013601d5",
  "isSidechain": true,
  "agentId": "a04145d2cd85bfce8",
  "requestId": "req_011CauJvJMCzp8JDxQrqTz33",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f681ab9b-ace1-4721-8245-73cd43a34702",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EsQGsFEvhMTkd6wDnRMngv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-10T17:49:10.177Z_

<details><summary>↩ Tool result · `toolu_01TkJXA2pJAufUBrJxPd1gXj`</summary>

```text
Web search results for query: "arXiv 2605.03117 ARISE SWE-bench Lite"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419v2"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"SWE-bench Lite","url":"https://www.swebench.com/lite.html"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"ProgramBench: Can Language Models Rebuild Programs From Scratch?","url":"https://arxiv.org/html/2605.03546v1"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/html/2512.17419v1"},{"title":"SWE-Bench Lite: Bug-Fixing Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-lite-dataset"}]

Based on the search results, here's what I found about arXiv paper 2605.03117:

## Overview

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

## Key Innovation

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

## Evaluation Results on SWE-bench Lite

The paper evaluates on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone. Compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points. These localization gains translate directly into repair success, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.

The paper was published on May 4, 2026, and addresses the challenge of repository-level fault localization and automated program repair for software engineering agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f681ab9b-ace1-4721-8245-73cd43a34702",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "a04145d2cd85bfce8",
  "type": "user",
  "uuid": "ccea810a-af02-4e2f-8d58-af14f1457162",
  "sourceToolAssistantUUID": "f681ab9b-ace1-4721-8245-73cd43a34702",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T17:49:11.883Z_

<details><summary>↩ Tool result · `toolu_012ce8AtYmUoabwoxVkXggtU`</summary>

```text
Web search results for query: "ARISE Repository-level Graph Representation Agentic Fault Localization Program Repair arXiv 2605.03117"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://arxiv.org/html/2503.21710v1"},{"title":"A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion","url":"https://arxiv.org/html/2409.13642v2"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"Beyond Accuracy: Behavioral Dynamics of Agentic Multi-Hunk Repair","url":"https://arxiv.org/html/2511.11012"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"},{"title":"Graph neural networks for precise bug localization through structural program analysis | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00556-y"}]

Based on the search results, I found detailed information about the paper you're looking for. Here's what I found:

## ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

### Key Features

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

### Performance Results

The evaluation was conducted on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone. Compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points. These localization gains translate directly into repair success, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.

### Design Insights

Controlled ablations confirm that the improvement is driven by the data-flow graph rather than the tool schema, and that large code models consume structured slice output directly without requiring a natural-language summarization layer.

The paper addresses an important gap in existing graph-based systems by incorporating data-flow information at the statement level, which provides the semantic precision needed for precise fault localization and program repair at the repository level.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48b03be9-ca8e-4798-b54b-b65d013601d5",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "a04145d2cd85bfce8",
  "type": "user",
  "uuid": "9bfa70c0-647c-4458-8a87-b11b982931e5",
  "sourceToolAssistantUUID": "48b03be9-ca8e-4798-b54b-b65d013601d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T17:49:15.657Z_

Now let me fetch the arXiv abstract page directly for more details, and also check if there's a linked code repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bfa70c0-647c-4458-8a87-b11b982931e5",
  "isSidechain": true,
  "agentId": "a04145d2cd85bfce8",
  "requestId": "req_011CauJwBqKeWcVLywDJzcNz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dd8256b-caf9-4be5-b7c0-6d606b0f884d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6L64BDzwmwPrU2Ngyfpno",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 860,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 10799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
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

_source line 10 · 2026-05-10T17:49:17.862Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S4NEbAkSTT1DTxXswNvRY3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.03117",
  "prompt": "Extract: 1) The full title and authors, 2) The abstract text, 3) Any links to code/GitHub repositories, 4) The submission date, 5) Any specific numerical results mentioned (Pass@1, localization metrics, etc.), 6) What model/LLM is used as the backbone."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dd8256b-caf9-4be5-b7c0-6d606b0f884d",
  "isSidechain": true,
  "agentId": "a04145d2cd85bfce8",
  "requestId": "req_011CauJwBqKeWcVLywDJzcNz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d26892f6-af52-4d47-bb2e-3b89b072833e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6L64BDzwmwPrU2Ngyfpno",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 860,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 10799,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1124
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 860,
          "output_tokens": 178,
          "cache_read_input_tokens": 10799,
          "cache_creation_input_tokens": 1124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1124,
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

_source line 11 · 2026-05-10T17:49:22.881Z_

<details><summary>↩ Tool result · `toolu_01S4NEbAkSTT1DTxXswNvRY3`</summary>

```text
# ARISE Paper Summary

**Title & Authors:**
"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair" by Shahd Seddik and Fatemeh Fard

**Abstract:**
The paper presents a system that enhances LLM agents with a multi-granularity program graph extending to statement-level nodes with data-flow edges. This enables agents to "trace, in a single call, which statements define or consume a variable of interest" for fault localization and repair tasks.

**Code/GitHub:**
No code repositories or GitHub links are provided in the page content.

**Submission Date:**
May 4, 2026

**Key Numerical Results:**
- Function Recall@1 improved by 17.0 percentage points
- Line Recall@1 improved by 15.0 percentage points
- Pass@1 achievement: 22.0% (66/300 issues)
- Repair success improvement: 4.7 percentage points over SWE-agent baseline
- Evaluation conducted on SWE-bench Lite (300 real GitHub issues across 11 Python repositories)

**Backbone Model:**
Qwen2.5-Coder-32B-Instruct serves as the LLM backbone for the system.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d26892f6-af52-4d47-bb2e-3b89b072833e",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "a04145d2cd85bfce8",
  "type": "user",
  "uuid": "a10af00a-e71c-459f-b842-3f5479d0b506",
  "sourceToolAssistantUUID": "d26892f6-af52-4d47-bb2e-3b89b072833e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T17:49:34.957Z_

I now have comprehensive information to answer all your questions. Here is my findings:

---

## Verification Results for arXiv:2605.03117

### 1. Does this paper actually exist?

**Yes.** The paper "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair" exists on arXiv with ID 2605.03117. It was submitted on May 4, 2026, by Shahd Seddik and Fatemeh Fard.

### 2. What are its actual claimed results on SWE-bench Lite?

On SWE-bench Lite (300 real GitHub issues, 11 Python repositories):
- **Pass@1: 22.0%** (66/300 issues resolved), which is a 4.7 percentage-point improvement over the unmodified SWE-agent baseline.
- **Function Recall@1:** +17.0 percentage points over baseline
- **Line Recall@1:** +15.0 percentage points over baseline

### 3. Does it report 22.0% Pass@1 and 17pp function-level localization gain?

**Yes, confirmed.** The paper reports exactly:
- 22.0% Pass@1 (66/300)
- 17.0 percentage-point improvement in Function Recall@1

Both figures match what you asked about.

### 4. What model does it use?

The backbone LLM is **Qwen2.5-Coder-32B-Instruct**. The system augments this model with a multi-granularity program graph and a three-tier tool API that exposes data-flow slicing as a first-class queryable primitive.

### 5. Is its code publicly available?

**No.** Based on the arXiv page, no GitHub repository or code link is provided. The paper does not appear to have released its code publicly as of now.

---

Sources:
- [arXiv:2605.03117 Abstract](https://arxiv.org/abs/2605.03117)
- [arXiv:2605.03117 HTML Version](https://arxiv.org/html/2605.03117)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a10af00a-e71c-459f-b842-3f5479d0b506",
  "isSidechain": true,
  "agentId": "a04145d2cd85bfce8",
  "requestId": "req_011CauJwzt34eVjroTU38ejF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57fc243c-8916-4c37-b72e-549877b76a82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EeweQvDP5tXA27iBb5iymF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1350,
      "cache_read_input_tokens": 11923,
      "output_tokens": 523,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1350
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 523,
          "cache_read_input_tokens": 11923,
          "cache_creation_input_tokens": 1350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1350,
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
