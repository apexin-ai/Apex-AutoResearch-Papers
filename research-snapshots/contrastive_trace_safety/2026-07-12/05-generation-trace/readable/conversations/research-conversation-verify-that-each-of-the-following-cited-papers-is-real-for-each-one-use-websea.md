# Research conversation: Verify that each of the following cited papers is real. For each one, use WebSearch to confirm the title, arXiv ID, auth

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a5e36231a69814593.jsonl`
- **Structured JSON:** [`d2b44be68692b91f23ad.json`](../../sessions/d2/d2b44be68692b91f23ad.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-10T17:15:39.047Z_

Verify that each of the following cited papers is real. For each one, use WebSearch to confirm the title, arXiv ID, authors, and venue/year. Report what you find for each.

1. "Self-Execution Simulation" - arXiv:2604.03253, Apr 2026
2. "SolidCoder" - arXiv:2604.19825, execution grounding for code generation
3. "VG-Search" and "S*" - arXiv:2502.14382, imperfect verifiers for test-time scaling
4. "CodeScaler" - arXiv:2602.17684, execution-free rewards, +11.72 points on Qwen3-8B
5. "FunPRM" - arXiv:2601.22249, process-level verification for generation
6. "Scaling Test-Time Compute for Agentic Coding" - arXiv:2604.16529, Claude Opus 4.5 70.9% to 77.6% on SWE-bench Verified

For each paper, report:
- Whether the arXiv ID and title match
- The actual title if different
- The actual venue if published
- Whether the claims made about the paper are accurate

Be precise — I need to drop any reference I cannot verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a5e36231a69814593",
  "type": "user",
  "uuid": "af3bc73a-2857-4a9b-a07c-f6702d0d381f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T17:15:39.053Z_

```json
{
  "parentUuid": "af3bc73a-2857-4a9b-a07c-f6702d0d381f",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
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
  "uuid": "224e4d10-7c05-4fca-9157-bb9848d3ab8f",
  "timestamp": "2026-05-10T17:15:39.053Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T17:15:41.311Z_



I'll search for each paper systematically. Let me start by searching for all six papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "224e4d10-7c05-4fca-9157-bb9848d3ab8f",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGNpBT7EeQm2D14cJ2F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b27f56e0-1e34-475c-8e8b-56b89f679667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGrkBdPjEu4yCGU3txkU9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 828,
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

_source line 4 · 2026-05-10T17:15:41.663Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XxKBiFfMxL3Pd9MGEU42mZ`</summary>

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
  "parentUuid": "b27f56e0-1e34-475c-8e8b-56b89f679667",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGNpBT7EeQm2D14cJ2F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bfdc8f9-80bd-4b63-9a47-016f54d54aa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGrkBdPjEu4yCGU3txkU9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 828,
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

### Tool result

_source line 5 · 2026-05-10T17:15:41.666Z_

<details><summary>↩ Tool result · `toolu_01XxKBiFfMxL3Pd9MGEU42mZ`</summary>

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
  "parentUuid": "5bfdc8f9-80bd-4b63-9a47-016f54d54aa8",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a5e36231a69814593",
  "type": "user",
  "uuid": "8df78f2c-e2d9-47c3-a104-dd8ddf70d67b",
  "sourceToolAssistantUUID": "5bfdc8f9-80bd-4b63-9a47-016f54d54aa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T17:15:44.102Z_



Now let me search for all six papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8df78f2c-e2d9-47c3-a104-dd8ddf70d67b",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGP1vPexb1RSR8bGupB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcc65b8d-399d-4d6f-9412-c6c8d7bb0470",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCgGEZAHv1BFw8Amb4uaJt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 7 · 2026-05-10T17:15:44.642Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W5eD34GTJcfgPL75HB2iNg`</summary>

```json
{
  "query": "arXiv 2604.03253 \"Self-Execution Simulation\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcc65b8d-399d-4d6f-9412-c6c8d7bb0470",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGP1vPexb1RSR8bGupB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b14faf82-9a9c-440e-b41b-7b7e1545ef1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCgGEZAHv1BFw8Amb4uaJt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 8 · 2026-05-10T17:15:45.630Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SAGWQDs5NvrgdSTzPHRYgA`</summary>

```json
{
  "query": "arXiv 2604.19825 \"SolidCoder\" execution grounding code generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b14faf82-9a9c-440e-b41b-7b7e1545ef1d",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGP1vPexb1RSR8bGupB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "471d029f-fa99-4869-afa0-fda8c843881c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCgGEZAHv1BFw8Amb4uaJt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 9 · 2026-05-10T17:15:47.249Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014hP8DD4o2gStjAoj5k9ynj`</summary>

```json
{
  "query": "arXiv 2502.14382 \"VG-Search\" \"S*\" imperfect verifiers test-time scaling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "471d029f-fa99-4869-afa0-fda8c843881c",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGP1vPexb1RSR8bGupB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21cde5c3-84f8-4316-8e7e-4beb04a52a4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCgGEZAHv1BFw8Amb4uaJt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 10 · 2026-05-10T17:15:47.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qe6eVfo8Yra3bxafA1oe21`</summary>

```json
{
  "query": "arXiv 2602.17684 \"CodeScaler\" execution-free rewards"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21cde5c3-84f8-4316-8e7e-4beb04a52a4e",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGP1vPexb1RSR8bGupB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af784e73-4e25-4b60-830d-c4e256e0407f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCgGEZAHv1BFw8Amb4uaJt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 11 · 2026-05-10T17:15:48.405Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VjeyTFd6RAanSsbMF795oA`</summary>

```json
{
  "query": "arXiv 2601.22249 \"FunPRM\" process-level verification generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af784e73-4e25-4b60-830d-c4e256e0407f",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGP1vPexb1RSR8bGupB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd074f63-1cad-4b74-8f4a-98cd43316f72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCgGEZAHv1BFw8Amb4uaJt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 12 · 2026-05-10T17:15:49.460Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C9TxMbfaVtdUjRho3tSi8j`</summary>

```json
{
  "query": "arXiv 2604.16529 \"Scaling Test-Time Compute for Agentic Coding\" SWE-bench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd074f63-1cad-4b74-8f4a-98cd43316f72",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGP1vPexb1RSR8bGupB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c62fe855-29cb-4e98-90ed-acddabcb0cf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCgGEZAHv1BFw8Amb4uaJt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8132,
      "output_tokens": 374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1415
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 374,
          "cache_read_input_tokens": 8132,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1415,
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

_source line 13 · 2026-05-10T17:15:50.699Z_

<details><summary>↩ Tool result · `toolu_01W5eD34GTJcfgPL75HB2iNg`</summary>

```text
Web search results for query: "arXiv 2604.03253 "Self-Execution Simulation""

Links: [{"title":"[2604.03253] Self-Execution Simulation Improves Coding Models","url":"https://arxiv.org/abs/2604.03253"},{"title":"Self-Execution Simulation Improves Coding Models","url":"https://arxiv.org/html/2604.03253"},{"title":"Paper page - Self-Execution Simulation Improves Coding Models","url":"https://huggingface.co/papers/2604.03253"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2604.03253"},{"title":"[2604.26423] Large-Scale Quantum Circuit Simulation on an Exascale System for QPU Benchmarking","url":"https://arxiv.org/abs/2604.26423"},{"title":"[2604.19825] SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution","url":"https://arxiv.org/abs/2604.19825"},{"title":"[2604.28181] Synthetic Computers at Scale for Long-Horizon Productivity Simulation","url":"https://arxiv.org/abs/2604.28181"},{"title":"SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution","url":"https://arxiv.org/html/2604.19825"},{"title":"The Self-Execution Benchmark: Measuring LLMs’ Attempts to Overcome Their Lack of Self-Execution","url":"https://arxiv.org/html/2508.12277v1"},{"title":"[2604.26653] AgentSim: A Platform for Verifiable Agent-Trace Simulation","url":"https://arxiv.org/abs/2604.26653"}]

I found the paper you're looking for! Here's information about arXiv 2604.03253:

**Title:** Self-Execution Simulation Improves Coding Models

**Authors:** Gallil Maimon, Ori Yoran, Felix Kreuk, Michael Hassid, Gal Cohen, Pierre Chambon, and Yossi Adi

**Publication Date:** March 11, 2026

**Overview:**
Code LLMs can be trained to simulate program execution in a step-by-step manner and this capability can be leveraged to improve competitive programming performance.

**Methodology:**
The approach combines supervised fine-tuning on natural language execution traces, textual explanations grounded in true execution, with reinforcement learning using verifiable rewards. The work introduces two complementary objectives: output prediction given code and inputs, and solving competitive programming tasks with either ground-truth or self-predicted execution feedback. These objectives enable models to perform self-verification over multiple candidate solutions, and iterative self-fixing by simulating test execution.

**Results:**
Across multiple competitive programming benchmarks, the method yields consistent improvements over standard reasoning approaches.

You can access the paper directly at https://arxiv.org/abs/2604.03253


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b14faf82-9a9c-440e-b41b-7b7e1545ef1d",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a5e36231a69814593",
  "type": "user",
  "uuid": "da57f827-34ee-476d-8519-a18838a70a8b",
  "sourceToolAssistantUUID": "b14faf82-9a9c-440e-b41b-7b7e1545ef1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T17:15:52.770Z_

<details><summary>↩ Tool result · `toolu_01SAGWQDs5NvrgdSTzPHRYgA`</summary>

```text
Web search results for query: "arXiv 2604.19825 "SolidCoder" execution grounding code generation"

Links: [{"title":"[2604.19825] SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution","url":"https://arxiv.org/abs/2604.19825"},{"title":"SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution","url":"https://arxiv.org/html/2604.19825"},{"title":"Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis","url":"https://arxiv.org/html/2604.10800v1"},{"title":"Towards Execution-Grounded Automated AI Research","url":"https://arxiv.org/html/2601.14525v1"},{"title":"Grounding Data Science Code Generation with Input-Output Specifications","url":"https://arxiv.org/html/2402.08073v2"},{"title":"[2402.08073] Grounding Data Science Code Generation with Input-Output Specifications","url":"https://arxiv.org/abs/2402.08073"},{"title":"[2604.10800v1] Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis","url":"https://arxiv.org/abs/2604.10800v1"},{"title":"Execution Guided Line-by-Line Code Generation Boaz Lavon Shahar Katz Lior Wolf","url":"https://arxiv.org/pdf/2506.10948"},{"title":"RLEF: GROUNDING CODE LLMS IN EXECUTION FEEDBACK WITH REINFORCEMENT LEARNING","url":"https://www.arxiv.org/pdf/2410.02089"},{"title":"Grounding Data Science Code Generation with Input- ...","url":"https://arxiv.org/pdf/2402.08073"}]

Based on the search results, here's what I found about arXiv paper 2604.19825:

## SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation

SolidCoder addresses a fundamental limitation in code generation where state-of-the-art frameworks rely on mental simulation (where LLMs internally trace execution), but models hallucinate execution traces and confidently validate buggy code.

**The Problem:** The Mental-Reality Gap manifests along two orthogonal dimensions: the Specification Gap (overlooking edge cases during planning) and the Verification Gap (hallucinating correct behavior for flawed code).

**The Solution:** SolidCoder operates on the principle "don't imagine -- execute," with its S.O.L.I.D. architecture addressing both dimensions by forcing edge-case awareness before algorithm design and replacing imagined traces with sandboxed execution using property-based oracles.

**Performance Results:** With GPT-4o, SolidCoder achieves state-of-the-art pass@1 performance: 95.7% on HumanEval (+0.6%p), 77.0% on CodeContests (+4.3%p), and 26.7% on APPS (+3.4%p).

**Key Insight:** Execution grounding catches categorically different errors that specification improvements cannot address.

The paper was submitted on April 20, 2026, and represents a shift toward grounding code generation verification in concrete execution rather than relying on LLM hallucination-prone mental simulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "471d029f-fa99-4869-afa0-fda8c843881c",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a5e36231a69814593",
  "type": "user",
  "uuid": "935c514f-fd61-456a-962c-6ac521caba1f",
  "sourceToolAssistantUUID": "471d029f-fa99-4869-afa0-fda8c843881c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T17:15:53.292Z_

<details><summary>↩ Tool result · `toolu_014hP8DD4o2gStjAoj5k9ynj`</summary>

```text
Web search results for query: "arXiv 2502.14382 "VG-Search" "S*" imperfect verifiers test-time scaling"

Links: [{"title":"[2502.14382] S*: Test Time Scaling for Code Generation","url":"https://arxiv.org/abs/2502.14382"},{"title":"Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling","url":"https://arxiv.org/html/2505.11730v1"},{"title":"[2502.12118] Scaling Test-Time Compute Without Verification or RL is Suboptimal","url":"https://arxiv.org/abs/2502.12118"},{"title":"Inference Scaling fLaws: The Limits of LLM Resampling with Imperfect Verifiers","url":"https://arxiv.org/html/2411.17501v2"},{"title":"[2505.11730] Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling","url":"https://arxiv.org/abs/2505.11730"},{"title":"[2502.00271] Scaling Flaws of Verifier-Guided Search in Mathematical Reasoning","url":"https://arxiv.org/abs/2502.00271"},{"title":"[2502.12118v2] Scaling Test-Time Compute Without Verification or RL is Suboptimal","url":"https://arxiv.org/abs/2502.12118v2"},{"title":"Verifier Threshold: An Efficient Test-Time Scaling Approach for Image Generation","url":"https://arxiv.org/html/2512.08985"},{"title":"Scaling Flaws of Verifier-Guided Search in Mathematical Reasoning","url":"https://arxiv.org/pdf/2502.00271"},{"title":"[2510.03149] Taming Imperfect Process Verifiers: A Sampling Perspective on Backtracking","url":"https://arxiv.org/abs/2510.03149"}]

Based on the search results, I found information about your query:

arXiv paper 2502.14382 presents "S*: Test Time Scaling for Code Generation," which is the first hybrid test-time scaling framework that substantially improves the coverage and selection accuracy of generated code. S* extends the existing parallel scaling paradigm with sequential scaling and leverages a novel selection mechanism that adaptively generates distinguishing inputs for pairwise comparison, combined with execution-grounded information to robustly identify correct solutions.

Regarding VG-Search and imperfect verifiers mentioned in your query: The search results also returned information about Variable Granularity Search (VG-Search), a unified algorithm that generalizes verifier-guided Beam Search and Best-of-N methods, from a different paper (2505.11730). Additionally, there are several related papers addressing challenges with imperfect verifiers, where there is a nonzero probability of false positives: incorrect solutions that pass the verifier, which is a key concern in test-time scaling research.

Would you like more specific information about any of these papers or concepts?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21cde5c3-84f8-4316-8e7e-4beb04a52a4e",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a5e36231a69814593",
  "type": "user",
  "uuid": "78c529f3-b224-41bb-9709-4e89e46c5194",
  "sourceToolAssistantUUID": "21cde5c3-84f8-4316-8e7e-4beb04a52a4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T17:15:54.284Z_

<details><summary>↩ Tool result · `toolu_01Qe6eVfo8Yra3bxafA1oe21`</summary>

```text
Web search results for query: "arXiv 2602.17684 "CodeScaler" execution-free rewards"

Links: [{"title":"[2602.17684] CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models","url":"https://arxiv.org/abs/2602.17684"},{"title":"CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models","url":"https://arxiv.org/html/2602.17684"},{"title":"CodeScaler: Scaling Code LLM Training and Test-Time ...","url":"https://arxiv.org/pdf/2602.17684"},{"title":"GitHub - LARK-AI-Lab/CodeScaler: The official repo for \"CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models\" · GitHub","url":"https://github.com/LARK-AI-Lab/CodeScaler"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1834&show=25"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/recent?skip=651&show=50"},{"title":"Learning to Generate Secure Code via Token-Level Rewards","url":"https://arxiv.org/html/2602.23407"},{"title":"[2602.03201] From Scalar Rewards to Potential Trends: Shaping Potential Landscapes for Model-Based Reinforcement Learning","url":"https://arxiv.org/abs/2602.03201"},{"title":"[2602.11399v1] Can We Really Learn One Representation to Optimize All Rewards?","url":"https://arxiv.org/abs/2602.11399v1"},{"title":"[2301.09043] CodeScore: Evaluating Code Generation by Learning Code Execution","url":"https://arxiv.org/abs/2301.09043"}]

Based on the search results, here's what I found about arXiv paper 2602.17684:

## CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models

CodeScaler is an execution-free reward model designed to scale both reinforcement learning training and test-time inference for code generation.

### Key Features:

CodeScaler is trained on carefully curated preference data derived from verified code problems and incorporates syntax-aware code extraction and validity-preserving reward shaping to ensure stable and robust optimization.

### Performance Results:

Across five coding benchmarks, CodeScaler improves Qwen3-8B-Base by an average of +11.72 points, outperforming binary execution-based RL by +1.82 points. At inference time, CodeScaler serves as an effective test-time scaling method, achieving performance comparable to unit test approaches while providing a 10-fold reduction in latency.

### Broader Impact:

CodeScaler surpasses existing reward models on RM-Bench not only in the code domain (+3.3 points), but also in general and reasoning domains (+2.7 points on average).

The paper was submitted on February 4, 2026, and the official code and models have been released on GitHub at https://github.com/LARK-AI-Lab/CodeScaler.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af784e73-4e25-4b60-830d-c4e256e0407f",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a5e36231a69814593",
  "type": "user",
  "uuid": "45fff770-70ee-4077-b0d7-18b7d9304ede",
  "sourceToolAssistantUUID": "af784e73-4e25-4b60-830d-c4e256e0407f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T17:15:56.371Z_

<details><summary>↩ Tool result · `toolu_01VjeyTFd6RAanSsbMF795oA`</summary>

```text
Web search results for query: "arXiv 2601.22249 "FunPRM" process-level verification generation"

Links: [{"title":"[2601.22249] FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/abs/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/html/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward","url":"https://www.arxiv.org/pdf/2601.22249"},{"title":"(PDF) FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://www.researchgate.net/publication/400340056_FunPRM_Function-as-Step_Process_Reward_Model_with_Meta_Reward_Correction_for_Code_Generation"},{"title":"STELLAR: Structure-guided LLM Assertion Retrieval and Generation for Formal Verification","url":"https://arxiv.org/html/2601.19903"},{"title":"[2601.12845] Automatic Generation of Formal Specification and Verification Annotations Using LLMs and Test Oracles","url":"https://arxiv.org/abs/2601.12845"},{"title":"[2601.19903] STELLAR: Structure-guided LLM Assertion Retrieval and Generation for Formal Verification","url":"https://arxiv.org/abs/2601.19903"},{"title":"[2601.00513] When Small Models Are Right for Wrong Reasons: Process Verification for Trustworthy Agents","url":"https://arxiv.org/abs/2601.00513"},{"title":"[2601.17223] Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning","url":"https://arxiv.org/abs/2601.17223"},{"title":"Automatic Generation of Formal Specification and Verification Annotations Using LLMs and Test Oracles1footnote 11footnote 1Preprint. Intended for submission to Science of Computer Programming.","url":"https://arxiv.org/html/2601.12845v1"}]

Based on the search results, here's what I found about arXiv paper 2601.22249:

## FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation

Code generation is a core application of large language models (LLMs), yet LLMs still frequently fail on complex programming tasks. Given its success in mathematical reasoning, test-time scaling approaches such as Process Reward Model (PRM)-based Best-of-N selection offer a promising way to improve performance.

However, existing PRMs remain ineffective for code generation due to the lack of meaningful step decomposition in code and the noise of Monte Carlo-estimated partial-solution correctness scores (rewards).

### The FunPRM Solution

FunPRM prompts LLMs to encourage modular code generation organized into functions, with functions treated as PRM reasoning steps. Additionally, FunPRM introduces a novel meta-learning-based reward correction mechanism that leverages clean final-solution rewards obtained via a unit-test-based evaluation system to purify noisy partial-solution rewards.

### Results

Experiments on LiveCodeBench and BigCodeBench demonstrate that FunPRM consistently outperforms existing test-time scaling methods across five base LLMs, notably achieving state-of-the-art performance on LiveCodeBench when combined with O4-mini. Furthermore, FunPRM produces code that is more readable and reusable for developers.

The paper was submitted on January 29, 2026, with authors Ruiyi Zhang, Peijia Qin, Qi Cao, Eric Xue, and Pengtao Xie.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd074f63-1cad-4b74-8f4a-98cd43316f72",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a5e36231a69814593",
  "type": "user",
  "uuid": "acc77ded-3b05-465d-b46f-8766f308b41e",
  "sourceToolAssistantUUID": "bd074f63-1cad-4b74-8f4a-98cd43316f72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T17:15:57.402Z_

<details><summary>↩ Tool result · `toolu_01C9TxMbfaVtdUjRho3tSi8j`</summary>

```text
Web search results for query: "arXiv 2604.16529 "Scaling Test-Time Compute for Agentic Coding" SWE-bench"

Links: [{"title":"[2604.16529] Scaling Test-Time Compute for Agentic Coding","url":"https://arxiv.org/abs/2604.16529"},{"title":"Scaling Test-Time Compute for Agentic Coding","url":"https://www.emergentmind.com/papers/2604.16529"},{"title":"[Paper Note] Scaling Test-Time Compute for Agentic Coding, Joongwon Kim+, arXiv'26, 2026.04 · Issue #5307 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/5307"},{"title":"Scaling Test-Time Compute for Agentic Coding - ArXivIQ","url":"https://arxiviq.substack.com/p/scaling-test-time-compute-for-agentic"},{"title":"Paper page - Scaling Test-Time Compute for Agentic Coding","url":"https://huggingface.co/papers/2604.16529"},{"title":"Test-Time Compute Orchestration for SWE-bench with AI21 Maestro","url":"https://www.ai21.com/blog/test-time-compute-swe-bench/"},{"title":"Scaling Test-Time Compute for Agentic Coding Kim et al. ...","url":"https://www.facebook.com/ceobillionairetv/posts/scaling-test-time-compute-for-agentic-codingkim-et-al-httpsarxivorgabs260416529a/26668407972789426/"},{"title":"CodeMonkeys: Scaling Test-Time Compute for Software Engineering","url":"https://arxiv.org/html/2501.14723v1"},{"title":"Thinking Longer, Not Larger: Enhancing Software Engineering Agents via Scaling Test-Time Compute","url":"https://arxiv.org/html/2503.23803v1"},{"title":"Scaling Test-Time Compute for Coding Agents - YouTube","url":"https://www.youtube.com/watch?v=IbbQajQ5tI8"}]

I found comprehensive information about the arXiv paper 2604.16529. Here's a summary:

## "Scaling Test-Time Compute for Agentic Coding"

This paper is authored by Joongwon Kim and 15 other researchers, published on April 16, 2026.

### Core Problem
While test-time scaling has become powerful for improving large language models, existing methods work best for short, bounded outputs. Long-horizon coding agents violate this premise—each attempt produces an extended trajectory of actions, observations, errors, and partial progress.

### Proposed Solution
The paper proposes a test-time scaling framework for agentic coding based on compact representations of rollout trajectories, converting each rollout into a structured summary that preserves salient hypotheses, progress, and failure modes while discarding low-signal trace details.

The framework introduces two complementary approaches:
- Recursive Tournament Voting (RTV) for parallel scaling, which recursively narrows a population of rollout summaries through small-group comparisons
- Parallel-Distill-Refine (PDR) for sequential scaling, conditioning new rollouts on summaries distilled from prior attempts

### Results
Using the method, Claude-4.5-Opus improves from 70.9% to 77.6% on SWE-Bench Verified (mini-SWE-agent) and 46.9% to 59.1% on Terminal-Bench v2.0 (Terminus 1).

The results suggest that test-time scaling for long-horizon agents is fundamentally a problem of representation, selection, and reuse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c62fe855-29cb-4e98-90ed-acddabcb0cf8",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a5e36231a69814593",
  "type": "user",
  "uuid": "5f6c9785-2a2c-4c2e-bf2c-d9d6e1b168b1",
  "sourceToolAssistantUUID": "c62fe855-29cb-4e98-90ed-acddabcb0cf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T17:16:01.148Z_

Now let me do a few follow-up searches to clarify specific details -- particularly for paper #3 (the S* paper) to check whether "VG-Search" is actually part of that paper, and to verify the "imperfect verifiers" claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f6c9785-2a2c-4c2e-bf2c-d9d6e1b168b1",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGQAY5ykpfdxUXCmKe4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6758c9d-1fbf-4f16-b265-f6dd24243550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EyYrLagomZfQYjhGbbdRaR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5596,
      "cache_read_input_tokens": 9547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5596,
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

_source line 20 · 2026-05-10T17:16:02.565Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EEgHosU8mVJhG73H9jiX9d`</summary>

```json
{
  "query": "arXiv 2502.14382 \"S*\" test time scaling code generation authors details",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6758c9d-1fbf-4f16-b265-f6dd24243550",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGQAY5ykpfdxUXCmKe4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb076653-fc40-4374-8311-5cf468281056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EyYrLagomZfQYjhGbbdRaR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5596,
      "cache_read_input_tokens": 9547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5596,
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

_source line 21 · 2026-05-10T17:16:02.836Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LCHbKEwwn9XsnuLLQF95Wu`</summary>

```json
{
  "query": "\"VG-Search\" imperfect verifiers test-time scaling arXiv paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb076653-fc40-4374-8311-5cf468281056",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGQAY5ykpfdxUXCmKe4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e33a5881-6071-42cf-a941-28e2e06d0973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EyYrLagomZfQYjhGbbdRaR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5596,
      "cache_read_input_tokens": 9547,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5596
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 9547,
          "cache_creation_input_tokens": 5596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5596,
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

_source line 22 · 2026-05-10T17:16:09.000Z_

<details><summary>↩ Tool result · `toolu_01EEgHosU8mVJhG73H9jiX9d`</summary>

```text
Web search results for query: "arXiv 2502.14382 "S*" test time scaling code generation authors details"

Links: [{"title":"[2502.14382] S*: Test Time Scaling for Code Generation","url":"https://arxiv.org/abs/2502.14382"},{"title":"[2502.14382v1] S*: Test Time Scaling for Code Generation","url":"https://arxiv.org/abs/2502.14382v1"},{"title":"𝑆^∗: Test Time Scaling for Code Generation","url":"https://arxiv.org/html/2502.14382"},{"title":"arXiv:2502.14382v1 [cs.LG] 20 Feb 2025","url":"https://arxiv.org/pdf/2502.14382"},{"title":"\\name: Scaling LLMs with Reasoning Data and Test-Time Compute for Accurate RTL Code Generation","url":"https://arxiv.org/html/2506.05566v1"},{"title":"[2502.12018] Atom of Thoughts for Markov LLM Test-Time Scaling","url":"https://arxiv.org/abs/2502.12018"},{"title":"[2502.17407] Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning","url":"https://arxiv.org/abs/2502.17407"},{"title":"[2502.06703] Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling","url":"https://arxiv.org/abs/2502.06703"},{"title":"s1: Simple test-time scaling","url":"https://arxiv.org/html/2501.19393v1"},{"title":"A1: Asynchronous Test-Time Scaling via Conformal Prediction","url":"https://arxiv.org/html/2509.15148v1"}]

Based on the search results, here are the details about arXiv paper 2502.14382:

## Paper Details

**Title:** S*: Test Time Scaling for Code Generation

**Submission Date:** February 20, 2025

## Authors

The authors are: Dacheng Li, Shiyi Cao, Chengkun Cao, Xiuyu Li, Shangyin Tan, Kurt Keutzer, Jiarong Xing, Joseph E. Gonzalez, and Ion Stoica

## Overview

S* is the first hybrid test-time scaling framework that substantially improves the coverage and selection accuracy of generated code. S* extends the existing parallel scaling paradigm with sequential scaling to push performance boundaries and leverages a novel selection mechanism that adaptively generates distinguishing inputs for pairwise comparison, combined with execution-grounded information to robustly identify correct solutions.

## Key Results

S* shows: (1) consistent improvements across model families and sizes, enabling a 3B model to outperform GPT-4o-mini; (2) enabling non-reasoning models to surpass reasoning models - GPT-4o-mini with S* outperforms o1-preview by 3.7% on LiveCodeBench


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb076653-fc40-4374-8311-5cf468281056",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a5e36231a69814593",
  "type": "user",
  "uuid": "6139dcb3-6be8-4a7a-ba7e-76c97aeb14d2",
  "sourceToolAssistantUUID": "cb076653-fc40-4374-8311-5cf468281056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T17:16:09.952Z_

<details><summary>↩ Tool result · `toolu_01LCHbKEwwn9XsnuLLQF95Wu`</summary>

```text
Web search results for query: ""VG-Search" imperfect verifiers test-time scaling arXiv paper"

Links: [{"title":"[2505.11730] Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling","url":"https://arxiv.org/abs/2505.11730"},{"title":"Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling","url":"https://arxiv.org/html/2505.11730v2"},{"title":"[2510.03149] Taming Imperfect Process Verifiers: A Sampling Perspective on Backtracking","url":"https://arxiv.org/abs/2510.03149"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v1"},{"title":"Inference Scaling FLaws: The Limits of LLM Resampling with Imperfect Verifiers","url":"https://arxiv.org/html/2411.17501v1"},{"title":"Scaling Agentic Verifier for Competitive Coding","url":"https://arxiv.org/html/2602.04254"},{"title":"Scaling Flaws of Verifier-Guided Search in Mathematical Reasoning","url":"https://arxiv.org/html/2502.00271"},{"title":"Variation in Verification: Understanding Verification Dynamics in Large Language Models","url":"https://arxiv.org/html/2509.17995v1"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"[2411.17501] The Limits of Inference Scaling Through Resampling","url":"https://arxiv.org/abs/2411.17501"}]

Based on the search results, I found relevant papers about VG-Search and imperfect verifiers in test-time scaling. Here's what I found:

## VG-Search Paper

VG-Search (Variable Granularity Search) is a unified algorithm that generalizes beam search and Best-of-N sampling via a tunable granularity parameter g. The work investigates the impact of verification granularity—how frequently the verifier is invoked during generation, beyond verifying only the final output or individual generation steps.

Adaptive VG-Search strategies achieve accuracy gains of up to 3.1% over Beam Search and 3.6% over Best-of-N, while reducing FLOPs by over 52%.

**Paper Details:** The arXiv paper is **2505.11730** titled "Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling"

## Related Work on Imperfect Verifiers

There are several complementary papers on imperfect verifiers in test-time scaling:

1. VGB is a process-guided test-time sampling algorithm which uses theoretically grounded backtracking to achieve provably better robustness to verifier errors. (arXiv 2510.03149)

2. Verifier failures occur where imperfect verifiers misrank candidates and erroneously prune all valid paths. (arXiv 2502.00271: "Scaling Flaws of Verifier-Guided Search in Mathematical Reasoning")

3. When verifiers are imperfect with a non-zero probability of producing false positives, resampling cannot decrease this probability, imposing an upper bound to accuracy regardless of compute budget. (arXiv 2411.17501)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e33a5881-6071-42cf-a941-28e2e06d0973",
  "isSidechain": true,
  "promptId": "9fc09f6e-c6a7-46eb-ad6b-8ab468d0bc70",
  "agentId": "a5e36231a69814593",
  "type": "user",
  "uuid": "7e2811a0-09a3-4a4a-a5ed-e56a4f1d763a",
  "sourceToolAssistantUUID": "e33a5881-6071-42cf-a941-28e2e06d0973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T17:16:52.960Z_

Now I have all the information needed. Here is my verification report for each paper:

---

## Paper-by-Paper Verification Report

### 1. "Self-Execution Simulation" -- arXiv:2604.03253

- **arXiv ID match:** YES. 2604.03253 is correct.
- **Actual title:** "Self-Execution Simulation Improves Coding Models" (slightly longer than cited).
- **Authors:** Gallil Maimon, Ori Yoran, Felix Kreuk, Michael Hassid, Gal Cohen, Pierre Chambon, Yossi Adi.
- **Date:** Submitted March 11, 2026 (labeled April 2026 in the citation -- the 2604 prefix does indicate April 2026 in the arXiv ID scheme, so this is consistent with the arXiv listing even if the actual submission was March).
- **Claims accuracy:** The citation is minimal ("Self-Execution Simulation, arXiv:2604.03253, Apr 2026") and is accurate. The paper does concern execution simulation for code LLMs.
- **Verdict: VERIFIED.** Minor note: the full title includes "Improves Coding Models."

### 2. "SolidCoder" -- arXiv:2604.19825

- **arXiv ID match:** YES. 2604.19825 is correct.
- **Actual title:** "SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution."
- **Date:** Submitted April 20, 2026.
- **Claim check -- "execution grounding for code generation":** Accurate. The paper's core thesis is replacing mental/imagined execution traces with concrete sandboxed execution ("don't imagine -- execute"). "Execution grounding" is an accurate description.
- **Verdict: VERIFIED.** The description is accurate.

### 3. "VG-Search" and "S\*" -- arXiv:2502.14382, imperfect verifiers for test-time scaling

- **arXiv ID match:** PARTIAL MISMATCH. arXiv:2502.14382 is the paper titled **"S\*: Test Time Scaling for Code Generation"** (authors: Dacheng Li et al., Feb 2025). This paper does exist and does concern test-time scaling for code generation.
- **"VG-Search" is NOT part of this paper.** VG-Search comes from a completely different paper: arXiv:2505.11730, "Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling."
- **"Imperfect verifiers" claim:** The S\* paper (2502.14382) is about test-time scaling for code generation using hybrid parallel+sequential scaling and a novel selection mechanism. It does not focus on "imperfect verifiers" as a central theme. The imperfect verifiers topic is addressed in other papers (e.g., arXiv:2411.17501).
- **Verdict: PROBLEMATIC.** The arXiv ID 2502.14382 correctly maps to the S\* paper, but "VG-Search" is from a different paper entirely, and the characterization "imperfect verifiers for test-time scaling" does not accurately describe 2502.14382. These appear to be two separate works conflated under one citation. **Drop or split this reference.**

### 4. "CodeScaler" -- arXiv:2602.17684

- **arXiv ID match:** YES. 2602.17684 is correct.
- **Actual title:** "CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models."
- **Date:** Submitted February 4, 2026.
- **Claim check -- "execution-free rewards, +11.72 points on Qwen3-8B":** Accurate. The paper reports CodeScaler improves Qwen3-8B-Base by an average of +11.72 points across five coding benchmarks, outperforming binary execution-based RL by +1.82 points.
- **Verdict: VERIFIED.** All claims match.

### 5. "FunPRM" -- arXiv:2601.22249

- **arXiv ID match:** YES. 2601.22249 is correct.
- **Actual title:** "FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation."
- **Authors:** Ruiyi Zhang, Peijia Qin, Qi Cao, Eric Xue, Pengtao Xie.
- **Date:** Submitted January 29, 2026.
- **Claim check -- "process-level verification for generation":** Mostly accurate but slightly imprecise. FunPRM is a Process Reward Model (PRM) for code generation that treats functions as reasoning steps and includes a meta-learning reward correction mechanism. "Process-level verification" is a reasonable shorthand for process reward modeling, though technically it is a reward/scoring model rather than a formal verifier.
- **Verdict: VERIFIED.** The description is substantively accurate.

### 6. "Scaling Test-Time Compute for Agentic Coding" -- arXiv:2604.16529

- **arXiv ID match:** YES. 2604.16529 is correct.
- **Actual title:** "Scaling Test-Time Compute for Agentic Coding" -- exact match.
- **Authors:** Joongwon Kim and 15 co-authors.
- **Date:** April 16, 2026.
- **Claim check -- "Claude Opus 4.5 70.9% to 77.6% on SWE-bench Verified":** The paper reports Claude-4.5-Opus (i.e., Claude Opus 4.5) improves from 70.9% to 77.6% on SWE-Bench Verified. This matches exactly.
- **Venue:** Preprint (arXiv), no conference venue identified.
- **Verdict: VERIFIED.** All claims match precisely.

---

## Summary

| # | Paper | Status | Action |
|---|-------|--------|--------|
| 1 | Self-Execution Simulation | VERIFIED | Keep (note full title) |
| 2 | SolidCoder | VERIFIED | Keep |
| 3 | VG-Search + S\* | PROBLEMATIC | **Drop or fix** -- VG-Search is NOT from 2502.14382; "imperfect verifiers" misdescribes the S\* paper |
| 4 | CodeScaler | VERIFIED | Keep |
| 5 | FunPRM | VERIFIED | Keep |
| 6 | Scaling Test-Time Compute for Agentic Coding | VERIFIED | Keep |

**Recommendation:** Papers 1, 2, 4, 5, and 6 are safe to cite. Paper 3 (arXiv:2502.14382) needs correction: the S\* paper is real, but "VG-Search" belongs to a different paper (arXiv:2505.11730), and the "imperfect verifiers" framing does not describe either paper accurately. If you intended to cite S\*, update the description. If you intended to cite VG-Search, use arXiv:2505.11730 instead.

Sources:
- [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)
- [Self-Execution Simulation Improves Coding Models](https://arxiv.org/abs/2604.03253)
- [SolidCoder: Bridging the Mental-Reality Gap](https://arxiv.org/abs/2604.19825)
- [CodeScaler: Scaling Code LLM Training](https://arxiv.org/abs/2602.17684)
- [FunPRM: Function-as-Step Process Reward Model](https://arxiv.org/abs/2601.22249)
- [Scaling Test-Time Compute for Agentic Coding](https://arxiv.org/abs/2604.16529)
- [VG-Search: Rethinking Optimal Verification Granularity](https://arxiv.org/abs/2505.11730)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e2811a0-09a3-4a4a-a5ed-e56a4f1d763a",
  "isSidechain": true,
  "agentId": "a5e36231a69814593",
  "requestId": "req_011CauGR6DuXi5AWUdRpmExg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e28d8d6-7e5f-4e58-bee9-8d974eeb3d33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a947e8fc-a30b-4332-9b56-2e5b071ae1d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WvzG7xmPimUbN5NXspxBU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1929,
      "cache_read_input_tokens": 15143,
      "output_tokens": 1999,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1929
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1999,
          "cache_read_input_tokens": 15143,
          "cache_creation_input_tokens": 1929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1929,
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
