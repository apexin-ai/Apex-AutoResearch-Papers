# Research conversation: I need to verify claims about a paper called "ARISE" (arXiv:2605.03117, May 2026) which is described as: - Repository-le

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a05ce09477ee6d5bb.jsonl`
- **Structured JSON:** [`2ca0f1f878a44822a2bb.json`](../../sessions/2c/2ca0f1f878a44822a2bb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-10T18:59:49.314Z_

I need to verify claims about a paper called "ARISE" (arXiv:2605.03117, May 2026) which is described as:
- Repository-level graph representation for agentic fault localization and repair
- Uses intra-procedural def-use edges via Python's ast module
- Does NOT cross call boundaries (explicitly limited to intra-procedural analysis)
- Achieves +17pp Function Recall@1
- Uses runtime tool calls only (not distilled)
- Requires Qwen2.5-Coder-32B at inference

Please search for this paper using WebSearch queries like:
1. "ARISE repository graph fault localization repair 2026 arxiv"
2. "arXiv 2605.03117"
3. "ARISE agentic fault localization def-use"

Then use WebFetch to read the abstract and key sections of the paper if you can find it. Report back:
- Does this paper exist?
- Are the claims about its limitations accurate?
- What exactly does it do with data-flow analysis?
- Any details about its scope of analysis (intra vs inter-procedural)?

Keep your response under 400 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a05ce09477ee6d5bb",
  "type": "user",
  "uuid": "13d480aa-1ac4-44bc-8ced-71e5bd63f29c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:59:49.318Z_

```json
{
  "parentUuid": "13d480aa-1ac4-44bc-8ced-71e5bd63f29c",
  "isSidechain": true,
  "agentId": "a05ce09477ee6d5bb",
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
  "uuid": "8598a65f-ad63-42d6-81bd-f2563662c18a",
  "timestamp": "2026-05-10T18:59:49.318Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:59:51.624Z_



I'll search for this paper using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8598a65f-ad63-42d6-81bd-f2563662c18a",
  "isSidechain": true,
  "agentId": "a05ce09477ee6d5bb",
  "requestId": "req_011CauQKYdferqhpyDnm5cLK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "527b99d9-99ef-4ab2-9436-8ada978db804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HoaYmKHyY2Tz7MJuncqxE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8097,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8097,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T18:59:52.168Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0145kDM1mDPkKSMwLghGm9Rw`</summary>

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
  "parentUuid": "527b99d9-99ef-4ab2-9436-8ada978db804",
  "isSidechain": true,
  "agentId": "a05ce09477ee6d5bb",
  "requestId": "req_011CauQKYdferqhpyDnm5cLK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "849c91a2-4cb8-4339-b920-25e2238b3d3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HoaYmKHyY2Tz7MJuncqxE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8097,
      "cache_read_input_tokens": 0,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8097
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8097,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8097,
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

_source line 5 · 2026-05-10T18:59:52.172Z_

<details><summary>↩ Tool result · `toolu_0145kDM1mDPkKSMwLghGm9Rw`</summary>

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
  "parentUuid": "849c91a2-4cb8-4339-b920-25e2238b3d3d",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a05ce09477ee6d5bb",
  "type": "user",
  "uuid": "b2ea810d-cb9d-4642-b2aa-1e4156a4d841",
  "sourceToolAssistantUUID": "849c91a2-4cb8-4339-b920-25e2238b3d3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:00:06.177Z_



Now let me run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2ea810d-cb9d-4642-b2aa-1e4156a4d841",
  "isSidechain": true,
  "agentId": "a05ce09477ee6d5bb",
  "requestId": "req_011CauQKmvs3PHvNjmMncrmH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "355e1dcb-86a0-4e71-a5b7-50c892ec0eff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eM1Yo64fPNq7TjLxGKT3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 8097,
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

_source line 7 · 2026-05-10T19:00:07.472Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DU7D2gKH9Q5GuQCZ6eR73h`</summary>

```json
{
  "query": "ARISE repository graph fault localization repair 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "355e1dcb-86a0-4e71-a5b7-50c892ec0eff",
  "isSidechain": true,
  "agentId": "a05ce09477ee6d5bb",
  "requestId": "req_011CauQKmvs3PHvNjmMncrmH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ffc176f-7667-4191-ace0-c4e5a80d85d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eM1Yo64fPNq7TjLxGKT3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 8097,
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

_source line 8 · 2026-05-10T19:00:07.852Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E61B11DmTWFgSQfP6ohb7d`</summary>

```json
{
  "query": "arXiv 2605.03117"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ffc176f-7667-4191-ace0-c4e5a80d85d6",
  "isSidechain": true,
  "agentId": "a05ce09477ee6d5bb",
  "requestId": "req_011CauQKmvs3PHvNjmMncrmH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad2870d9-433b-46c5-8b64-6cebcb7d8e9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eM1Yo64fPNq7TjLxGKT3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 8097,
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

_source line 9 · 2026-05-10T19:00:08.320Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QiyZE9eUfxre9fTnDiXcPV`</summary>

```json
{
  "query": "ARISE agentic fault localization def-use"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad2870d9-433b-46c5-8b64-6cebcb7d8e9b",
  "isSidechain": true,
  "agentId": "a05ce09477ee6d5bb",
  "requestId": "req_011CauQKmvs3PHvNjmMncrmH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7af6380-6d6b-461b-b74f-ad6b9c2bc6b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eM1Yo64fPNq7TjLxGKT3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 8097,
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

### Tool result

_source line 10 · 2026-05-10T19:00:13.975Z_

<details><summary>↩ Tool result · `toolu_01E61B11DmTWFgSQfP6ohb7d`</summary>

```text
Web search results for query: "arXiv 2605.03117"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.01172] A Theory of Generalization in Deep Learning","url":"https://arxiv.org/abs/2605.01172"},{"title":"AgentDyn: A Dynamic Open-Ended Benchmark for Evaluating Prompt","url":"https://arxiv.org/pdf/2602.03117"},{"title":"No Attacker Needed: Unintentional Cross-User Contamination in Shared-State LLM Agents","url":"https://arxiv.org/html/2604.01350v1"},{"title":"All-Electrostatic Valley Filtering by Barrier Rotation in Tilted Dirac/Weyl Semimetals","url":"https://arxiv.org/html/2603.03117"},{"title":"[2602.03117] AgentDyn: A Dynamic Open-Ended Benchmark for Evaluating Prompt Injection Attacks of Real-World Agent Security System","url":"https://arxiv.org/abs/2602.03117"},{"title":"PromptCOS: Towards Content-only System Prompt Copyright Auditing for LLMs","url":"https://arxiv.org/html/2509.03117"},{"title":"[2504.03117] Superresolution imaging with entanglement-enhanced telescopy","url":"https://arxiv.org/abs/2504.03117"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/new"}]

Based on the search results, arXiv paper 2605.03117 presents ARISE (Agentic Repository-level Issue Solving Engine), which augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

The paper addresses repository-level fault localization (FL) and automated program repair (APR), which require an agent to identify the relevant code units across files, follow call and data dependencies, and generate a valid patch. ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace which statements define or consume a variable of interest.

The paper was submitted on May 4, 2026, and is authored by Shahd Seddik and Fatemeh Fard from the University of British Columbia.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad2870d9-433b-46c5-8b64-6cebcb7d8e9b",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a05ce09477ee6d5bb",
  "type": "user",
  "uuid": "de8f6b9e-ba43-4275-9a61-23a89a2837bb",
  "sourceToolAssistantUUID": "ad2870d9-433b-46c5-8b64-6cebcb7d8e9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T19:00:15.157Z_

<details><summary>↩ Tool result · `toolu_01DU7D2gKH9Q5GuQCZ6eR73h`</summary>

```text
Web search results for query: "ARISE repository graph fault localization repair 2026 arxiv"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/abs/2604.00167"},{"title":"Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://arxiv.org/html/2503.21710v1"},{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"[2601.18044] RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/abs/2601.18044"},{"title":"[2604.05481] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481"}]

I found the paper you're looking for! Here's information about the ARISE repository paper:

## ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

### Key Technical Contribution

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

### Performance Results

Compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.

### Publication Details

The paper was submitted on May 4, 2026. The arXiv ID is 2605.03117.

The graph builder and slicing API are designed as a framework-agnostic, drop-in toolset for future APR research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ffc176f-7667-4191-ace0-c4e5a80d85d6",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a05ce09477ee6d5bb",
  "type": "user",
  "uuid": "7db6bb6f-7413-49d6-8cad-510c4f8b4f16",
  "sourceToolAssistantUUID": "8ffc176f-7667-4191-ace0-c4e5a80d85d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:00:18.697Z_

<details><summary>↩ Tool result · `toolu_01QiyZE9eUfxre9fTnDiXcPV`</summary>

```text
Web search results for query: "ARISE agentic fault localization def-use"

Links: [{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"Agentic Code Reasoning","url":"https://arxiv.org/html/2603.01896v1"},{"title":"[2505.08638] TRAIL: Trace Reasoning and Agentic Issue Localization","url":"https://arxiv.org/abs/2505.08638"},{"title":"Agentic Code Reasoning","url":"https://www.emergentmind.com/papers/2603.01896"},{"title":"TRAIL: Trace Reasoning and Agentic Issue Localization","url":"https://arxiv.org/html/2505.08638v3"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"Agentic Software Issue Resolution","url":"https://www.emergentmind.com/topics/agentic-software-issue-resolution"},{"title":"An Empirical Study on LLM-based Agents for Automated Bug Fixing","url":"https://arxiv.org/html/2411.10213v1"},{"title":"LLM Observability & Evaluation Platform","url":"https://arize.com/"}]

Based on the search results, I found relevant information about ARISE and its approach to agentic fault localization using def-use analysis:

## ARISE: Agentic Fault Localization with Definition-Use Chains

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

In its first phase, ARISE constructs a multi-granularity program graph that combines structural relationships with intra-procedural data-flow edges (definition-use chains at statement level).

### Key Capabilities

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

### Performance Results

Compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent. Controlled ablations confirm that the improvement is driven by the data-flow graph rather than the tool schema.

The framework represents a significant advancement in enabling agents to perform fine-grained fault localization through structured data-flow analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7af6380-6d6b-461b-b74f-ad6b9c2bc6b0",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a05ce09477ee6d5bb",
  "type": "user",
  "uuid": "ea2dd1dd-111e-4f11-95d9-93029419d564",
  "sourceToolAssistantUUID": "a7af6380-6d6b-461b-b74f-ad6b9c2bc6b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T19:00:22.705Z_

The paper exists. Let me fetch the full abstract and details about its analysis scope and model requirements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea2dd1dd-111e-4f11-95d9-93029419d564",
  "isSidechain": true,
  "agentId": "a05ce09477ee6d5bb",
  "requestId": "req_011CauQMiH9ZcypgULPVh8HP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a5a7818-206b-4bc0-a146-d9052a02f32a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BypZUum7cS1irwGEHPBEL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2584,
      "cache_read_input_tokens": 9999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2584,
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

_source line 14 · 2026-05-10T19:00:25.736Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018SNisqdWWPxF2gPZuPdN2s`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.03117",
  "prompt": "Extract the full abstract, the model used at inference (e.g. Qwen2.5-Coder-32B or GPT-4o or other), whether tool calls are runtime or distilled, and any mention of intra-procedural vs inter-procedural analysis scope. Also note any stated limitations about not crossing call boundaries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a5a7818-206b-4bc0-a146-d9052a02f32a",
  "isSidechain": true,
  "agentId": "a05ce09477ee6d5bb",
  "requestId": "req_011CauQMiH9ZcypgULPVh8HP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f3d4445-8134-444a-be52-7e419505cd04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BypZUum7cS1irwGEHPBEL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2584,
      "cache_read_input_tokens": 9999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2584,
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

_source line 15 · 2026-05-10T19:00:28.309Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VDPhSxEjRSf8bfwmgVxRpY`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.03117",
  "prompt": "Find and extract: 1) What LLM model is used at inference time (e.g. GPT-4o, Qwen2.5-Coder-32B, etc.)? 2) Are tool calls runtime or distilled? 3) Is the def-use analysis explicitly described as intra-procedural only, or does it also handle inter-procedural / cross-function analysis? 4) Any mention of crossing call boundaries or not crossing them. 5) Any stated limitations about the scope of def-use edges. 6) The exact Function Recall@1 improvement number."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f3d4445-8134-444a-be52-7e419505cd04",
  "isSidechain": true,
  "agentId": "a05ce09477ee6d5bb",
  "requestId": "req_011CauQMiH9ZcypgULPVh8HP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "944bc221-9572-4203-9f3e-34de2c83f627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BypZUum7cS1irwGEHPBEL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2584,
      "cache_read_input_tokens": 9999,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2584
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 373,
          "cache_read_input_tokens": 9999,
          "cache_creation_input_tokens": 2584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2584,
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

_source line 16 · 2026-05-10T19:00:34.092Z_

<details><summary>↩ Tool result · `toolu_018SNisqdWWPxF2gPZuPdN2s`</summary>

```text
# ARISE Paper Analysis

**Full Abstract:**
"Repository-level fault localization (FL) and automated program repair (APR) require an agent to identify the relevant code units across files, follow call and data dependencies, and generate a valid patch. Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization. We present ARISE (Agentic Repository-level Issue Solving Engine), which augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges. ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest. We evaluate on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone. Compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points. These localization gains translate directly into repair success, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent. Controlled ablations confirm that the improvement is driven by the data-flow graph rather than the tool schema, and that large code models consume structured slice output directly without requiring a natural-language summarization layer. The graph builder and slicing API are designed as a framework-agnostic, drop-in toolset for future APR research."

**Model Used at Inference:**
Qwen2.5-Coder-32B-Instruct

**Tool Calls:**
Runtime (tools integrated within the agent's execution flow)

**Analysis Scope:**
Intra-procedural analysis is emphasized: "intra-procedural definition-use edges" model variable flow within individual procedures, while inter-procedural aspects (call dependencies) are handled through the structural graph layer.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f3d4445-8134-444a-be52-7e419505cd04",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a05ce09477ee6d5bb",
  "type": "user",
  "uuid": "70c59a92-093e-4892-90a3-3a7dba420092",
  "sourceToolAssistantUUID": "7f3d4445-8134-444a-be52-7e419505cd04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T19:00:34.180Z_

<details><summary>↩ Tool result · `toolu_01VDPhSxEjRSf8bfwmgVxRpY`</summary>

```text
# ARISE Paper Analysis

## 1. LLM Model at Inference Time
The primary backbone is **Qwen2.5-Coder-32B-Instruct**. The paper states: "The backbone for all reported experiments is Qwen2.5-Coder-32B-Instruct" served locally via vLLM. A smaller model, Qwen3-4B-Instruct, is used only for generating natural-language summaries in the explain_slice tool.

## 2. Tool Calls: Runtime or Distilled
Tool calls are **runtime**. The agent executes tools dynamically during the multi-turn reasoning loop. The paper describes "the agent chooses which tools to call and in what order at each turn," and all tools are invoked on-demand rather than distilled offline.

## 3. Def-Use Analysis Scope
The analysis is **explicitly intra-procedural only**. The methodology section states: "For every Function and Method node, we first walk the function body and emit one Statement node per top-level AST statement" and connections are made "within the same function body, respecting lexical scope."

## 4. Crossing Call Boundaries
The system **does not cross call boundaries**. The paper explicitly states: "get_dataflow_slice stops at Calls edges, so bugs whose root cause is a value mutated inside a callee are invisible to the backward slice."

## 5. Stated Limitations on Def-Use Scope
The limitations section confirms: "The most significant architectural limitation of ARISE's data-flow layer is that get_dataflow_slice does not cross Calls edges."

## 6. Function Recall@1 Improvement
ARISE-Full achieves a **17.0 percentage-point improvement** in Function Recall@1 over the SWE-agent baseline (60.0 vs. 43.0).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "944bc221-9572-4203-9f3e-34de2c83f627",
  "isSidechain": true,
  "promptId": "e415714b-7a28-4c44-aefa-f517da24be8e",
  "agentId": "a05ce09477ee6d5bb",
  "type": "user",
  "uuid": "18c38ca5-a452-43b4-95cc-06949e781d05",
  "sourceToolAssistantUUID": "944bc221-9572-4203-9f3e-34de2c83f627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T19:00:46.835Z_

Here are my findings:

**The paper exists.** ARISE (arXiv:2605.03117, submitted May 4, 2026) is a real paper by Shahd Seddik and Fatemeh Fard (University of British Columbia).

**All claims listed are accurate:**

1. **Repository-level graph representation for agentic fault localization and repair** -- Confirmed. ARISE builds a multi-granularity program graph with statement-level nodes and exposes it via a three-tier tool API.

2. **Intra-procedural def-use edges via Python's `ast` module** -- Confirmed. The paper walks function bodies and emits statement nodes per top-level AST statement, connecting them with definition-use edges "within the same function body, respecting lexical scope."

3. **Does NOT cross call boundaries** -- Confirmed. The paper explicitly states: "get_dataflow_slice stops at Calls edges, so bugs whose root cause is a value mutated inside a callee are invisible to the backward slice." This is listed as "the most significant architectural limitation."

4. **+17pp Function Recall@1** -- Confirmed. ARISE-Full achieves 60.0 vs. 43.0 for the SWE-agent baseline, a 17.0 percentage-point improvement.

5. **Runtime tool calls (not distilled)** -- Confirmed. The agent dynamically chooses which tools to call at each turn during a multi-turn reasoning loop; nothing is pre-computed or distilled.

6. **Requires Qwen2.5-Coder-32B at inference** -- Confirmed. The backbone is Qwen2.5-Coder-32B-Instruct served via vLLM (a smaller Qwen3-4B model is used only for natural-language summaries in the explain_slice tool).

**Data-flow analysis details:** ARISE adds intra-procedural def-use chains on top of a structural graph (files, classes, functions). The data-flow slicing is exposed as a queryable tool primitive, letting the agent trace which statements define or consume a variable. Ablations confirm the improvement comes from the data-flow graph itself, not the tool schema.

Sources:
- [ARISE Abstract (arXiv)](https://arxiv.org/abs/2605.03117)
- [ARISE Full HTML (arXiv)](https://arxiv.org/html/2605.03117)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18c38ca5-a452-43b4-95cc-06949e781d05",
  "isSidechain": true,
  "agentId": "a05ce09477ee6d5bb",
  "requestId": "req_011CauQNrUoG84nbZHkG2JoG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05b2d61b-d2fb-47f5-b02d-04928cd21eb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a47aaa43-a429-47b7-80b6-f2738661f6aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDh4S2JEWk8fpnL7hJ1DH8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1379,
      "cache_read_input_tokens": 12583,
      "output_tokens": 567,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1379
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 567,
          "cache_read_input_tokens": 12583,
          "cache_creation_input_tokens": 1379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1379,
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
