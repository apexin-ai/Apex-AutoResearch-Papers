# Research conversation: Research PAHQ (arXiv:2510.23264) which claims to accelerate ACDC circuit discovery using mixed-precision. I need to unde

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a97febb1e84474d24.jsonl`
- **Structured JSON:** [`540288afcb832179aead.json`](../../sessions/54/540288afcb832179aead.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

40 recorded events

### User

_source line 1 · 2026-05-12T10:20:26.294Z_

Research PAHQ (arXiv:2510.23264) which claims to accelerate ACDC circuit discovery using mixed-precision.

I need to understand:
1. Does PAHQ have an open-source code repository? Search GitHub for PAHQ circuit discovery repos.
2. What speedup does PAHQ claim over standard ACDC?
3. Does PAHQ work with TransformerLens or its own framework?
4. Could it bring ACDC runtime on Qwen-2.5 0.5B from ~42-127h down to ≤10h per task?
5. Is PAHQ edge-level or node-level?
6. What is the algorithm family - is it still "causal intervention" like ACDC?

Also search for any other methods that accelerate ACDC (e.g., SP-ACDC, hierarchical ACDC, etc.).

Use WebSearch and WebFetch to find the paper abstract, any code repos, and speedup claims. Report concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "7ae38842-ff9a-4254-b704-548763eca1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T10:20:26.298Z_

```json
{
  "parentUuid": "7ae38842-ff9a-4254-b704-548763eca1e8",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
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
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "a55be394-0ab6-4fb4-ab5e-9e766e8783f8",
  "timestamp": "2026-05-12T10:20:26.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T10:20:30.022Z_



I'll search for PAHQ and related ACDC acceleration methods. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a55be394-0ab6-4fb4-ab5e-9e766e8783f8",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWLE1UdqxCyoFuPJg2q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92b739a3-19b4-451d-94f4-787123c87b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9NUg4ZroC6fdM1Amnj4dk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6024,
      "cache_read_input_tokens": 8258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6024,
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

_source line 4 · 2026-05-12T10:20:30.551Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Nkm5onVTzFKggCJpyH2rPr`</summary>

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
  "parentUuid": "92b739a3-19b4-451d-94f4-787123c87b39",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWLE1UdqxCyoFuPJg2q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af228b11-3690-495c-ba21-d3bbe9ca3354",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9NUg4ZroC6fdM1Amnj4dk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6024,
      "cache_read_input_tokens": 8258,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6024
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 8258,
          "cache_creation_input_tokens": 6024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6024,
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

_source line 5 · 2026-05-12T10:20:30.554Z_

<details><summary>↩ Tool result · `toolu_01Nkm5onVTzFKggCJpyH2rPr`</summary>

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
  "parentUuid": "af228b11-3690-495c-ba21-d3bbe9ca3354",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "a2cc3867-020b-41d2-95dc-ddb956a91973",
  "sourceToolAssistantUUID": "af228b11-3690-495c-ba21-d3bbe9ca3354",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T10:20:35.772Z_



Let me search for PAHQ and related ACDC acceleration methods in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2cc3867-020b-41d2-95dc-ddb956a91973",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWLY1hHKgjWz2Le97JA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9eac6b73-d5e0-4117-8bb5-5da64de6f9d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNvH9LSCpH5wawdjicG3Wq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 14282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 7 · 2026-05-12T10:20:36.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WAfAYNCyFtifwWBpEuAgF1`</summary>

```json
{
  "query": "PAHQ arXiv 2510.23264 mixed-precision ACDC circuit discovery"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9eac6b73-d5e0-4117-8bb5-5da64de6f9d4",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWLY1hHKgjWz2Le97JA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c491511-5780-4cb9-894f-dcb6d2084474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNvH9LSCpH5wawdjicG3Wq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 14282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 8 · 2026-05-12T10:20:36.741Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SMY8j4Bz4XFdzEqZgKXTeq`</summary>

```json
{
  "query": "PAHQ circuit discovery GitHub code repository"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c491511-5780-4cb9-894f-dcb6d2084474",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWLY1hHKgjWz2Le97JA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1652721-3175-4902-ab7e-6b324bf7dd81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNvH9LSCpH5wawdjicG3Wq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 14282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 9 · 2026-05-12T10:20:37.682Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019ykym7xEk4bocjcjpbQogy`</summary>

```json
{
  "query": "accelerate ACDC circuit discovery speedup methods SP-ACDC hierarchical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1652721-3175-4902-ab7e-6b324bf7dd81",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWLY1hHKgjWz2Le97JA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed273d9a-d04f-4a95-9858-8ea669b62435",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNvH9LSCpH5wawdjicG3Wq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 14282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 10 · 2026-05-12T10:20:38.150Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ERzsR9vRZxNWyQgteMBQ4z`</summary>

```json
{
  "query": "PAHQ mixed precision mechanistic interpretability TransformerLens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed273d9a-d04f-4a95-9858-8ea669b62435",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWLY1hHKgjWz2Le97JA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81d34a3f-b8ef-4b85-8855-21e3e4b90634",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNvH9LSCpH5wawdjicG3Wq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1961,
      "cache_read_input_tokens": 14282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1961,
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

_source line 11 · 2026-05-12T10:20:41.728Z_

<details><summary>↩ Tool result · `toolu_01SMY8j4Bz4XFdzEqZgKXTeq`</summary>

```text
Web search results for query: "PAHQ circuit discovery GitHub code repository"

Links: [{"title":"PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/html/2510.23264"},{"title":"(PDF) PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://www.researchgate.net/publication/396967828_PAHQ_Accelerating_Automated_Circuit_Discovery_through_Mixed-Precision_Inference_Optimization"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through ...","url":"https://arxiv.org/pdf/2510.23264"},{"title":"[2510.23264] PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/abs/2510.23264"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery · GitHub","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery"},{"title":"circuit · GitHub Topics · GitHub","url":"https://github.com/topics/circuit"},{"title":"circuit-simulator · GitHub Topics · GitHub","url":"https://github.com/topics/circuit-simulator"},{"title":"Automatic circuit discovery | Arthur’s Site","url":"https://arthurconmy.github.io/automatic_circuit_discovery/"},{"title":"circuits · GitHub Topics · GitHub","url":"https://github.com/topics/circuits"},{"title":"circuit-design · GitHub Topics · GitHub","url":"https://github.com/topics/circuit-design"}]

Based on the search results, here's what I found about PAHQ circuit discovery:

## PAHQ GitHub Repository

The PAHQ code is available at https://github.com/626619403/PAHQ.

## About PAHQ

PAHQ (Per Attention Head Quantization) is a method for accelerating automated circuit discovery by optimizing the efficiency of each individual patching operation. 

PAHQ leverages an alignment between activation patching and mixed-precision quantization (MPQ), maintaining high precision exclusively for investigated components while safely reducing precision elsewhere in the network.

## Performance Improvements

PAHQ-accelerated ACDC reduces runtime by up to 80% and memory consumption by up to 30% compared to unaccelerated ACDC while maintaining faithfulness.

The work was published recently as an arXiv paper in October 2025 and represents a significant advancement in making circuit discovery methods more computationally efficient.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1652721-3175-4902-ab7e-6b324bf7dd81",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "33e1f25e-5b93-4a3a-ac23-9c435a5a90ce",
  "sourceToolAssistantUUID": "f1652721-3175-4902-ab7e-6b324bf7dd81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T10:20:43.238Z_

<details><summary>↩ Tool result · `toolu_01WAfAYNCyFtifwWBpEuAgF1`</summary>

```text
Web search results for query: "PAHQ arXiv 2510.23264 mixed-precision ACDC circuit discovery"

Links: [{"title":"[2510.23264] PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/abs/2510.23264"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through ...","url":"https://arxiv.org/pdf/2510.23264"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/html/2510.23264"},{"title":"(PDF) PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://www.researchgate.net/publication/396967828_PAHQ_Accelerating_Automated_Circuit_Discovery_through_Mixed-Precision_Inference_Optimization"},{"title":"[Literature Review] PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://www.themoonlight.io/en/review/pahq-accelerating-automated-circuit-discovery-through-mixed-precision-inference-optimization"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery · GitHub","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT AUTOMATED CIRCUIT","url":"https://arxiv.org/pdf/2407.00886"},{"title":"IBCircuit: Towards Holistic Circuit Discovery with Information Bottleneck","url":"https://arxiv.org/html/2602.22581"}]

Based on the search results, here's information about the paper you're looking for:

## PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization

PAHQ is a method for accelerating automated circuit discovery through mixed-precision inference optimization, authored by Xinhai Wang and colleagues. The paper was published on arXiv on October 27, 2025 (arXiv identifier: 2510.23264).

### Overview

Circuit discovery involves identifying sparse and task-relevant subnetworks in pre-trained language models and is a cornerstone of mechanistic interpretability. Automated Circuit Discovery (ACDC) has emerged as a pivotal methodology in circuit discovery, but its application to large language models is severely limited by computational inefficiency and prohibitively high memory requirements.

### The PAHQ Method

PAHQ, which stands for Per Attention Head Quantization, takes a fundamentally different approach by optimizing the efficiency of each individual patching operation. PAHQ leverages a fundamental alignment between activation patching and mixed-precision quantization (MPQ): interpretability analysis through patching essentially performs targeted ablation studies. Therefore, high precision can be maintained exclusively for investigated components while safely reducing precision elsewhere in the network.

### Performance Results

PAHQ-accelerated ACDC reduces runtime by up to 80% and memory consumption by up to 30% compared to unaccelerated ACDC while maintaining faithfulness. This training-free approach provides a practical and novel pathway for accelerating mechanistic interpretability methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c491511-5780-4cb9-894f-dcb6d2084474",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "0ca07346-d5d4-4b1b-a939-6eb2efa2f342",
  "sourceToolAssistantUUID": "1c491511-5780-4cb9-894f-dcb6d2084474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T10:20:45.354Z_

<details><summary>↩ Tool result · `toolu_01ERzsR9vRZxNWyQgteMBQ4z`</summary>

```text
Web search results for query: "PAHQ mixed precision mechanistic interpretability TransformerLens"

Links: [{"title":"PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/html/2510.23264v1"},{"title":"GitHub - TransformerLensOrg/TransformerLens: A library for mechanistic interpretability of GPT-style language models · GitHub","url":"https://github.com/TransformerLensOrg/TransformerLens"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through ...","url":"https://arxiv.org/pdf/2510.23264"},{"title":"[2510.23264] PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/abs/2510.23264"},{"title":"(PDF) PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://www.researchgate.net/publication/396967828_PAHQ_Accelerating_Automated_Circuit_Discovery_through_Mixed-Precision_Inference_Optimization"},{"title":"Getting Started in Mechanistic Interpretability - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/content/getting_started_mech_interp.html"},{"title":"TransformerLens/README.md at 9321ca07753f816eaa210a5c7a2cf094c47421fb · TransformerLensOrg/TransformerLens","url":"https://github.com/TransformerLensOrg/TransformerLens/blob/9321ca07753f816eaa210a5c7a2cf094c47421fb/README.md"},{"title":"GitHub - ayyucekizrak/Mechanistic-Interpretability: Mechanistic Interpretability in Transformers: This repository explores advanced techniques like Induction Head Detection and QK Circuit Analysis to uncover the inner workings of transformer-based models. · GitHub","url":"https://github.com/ayyucekizrak/Mechanistic-Interpretability"},{"title":"TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/"},{"title":"GitHub - htlou/TransformerLens-V: A library for mechanistic interpretability of GPT-style language models","url":"https://github.com/htlou/TransformerLens-V"}]

I found comprehensive information about these topics. Here's what the search revealed:

## PAHQ Overview

PAHQ (Per Attention Head Quantization) is a method for accelerating automated circuit discovery by optimizing the efficiency of each individual patching operation. PAHQ leverages a fundamental alignment between activation patching and mixed-precision quantization (MPQ): interpretability analysis through patching essentially performs targeted ablation studies.

## Key Capabilities

PAHQ achieves an optimal balance between performance and compression by maintaining high-precision computation for critical attention heads, delivering superior results without additional training through mechanistic interpretability insights. This method requires no additional training and can be used as a plug-and-play solution.

## Performance Results

Experimental results demonstrate that PAHQ achieves an average reduction of approximately 80% in time consumption and 30% in memory usage when implemented within the ACDC framework with only slight performance loss, providing an acceleration approach for mechanistic interpretability research without sacrificing analytical quality.

## TransformerLens Integration

PAHQ is designed specifically for mechanistic interpretability research and maintains compatibility with the original intended uses of all utilized artifacts: TransformerLens is applied precisely for its intended purpose of mechanistic interpretability analysis.

## TransformerLens Context

TransformerLens is a library for doing mechanistic interpretability of GPT-2 style language models, with the goal of mechanistic interpretability being to take a trained model and reverse engineer the algorithms the model learned during training from its weights.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81d34a3f-b8ef-4b85-8855-21e3e4b90634",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "29db1189-6ab8-4011-8961-bf530ee911e6",
  "sourceToolAssistantUUID": "81d34a3f-b8ef-4b85-8855-21e3e4b90634",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T10:20:45.920Z_

<details><summary>↩ Tool result · `toolu_019ykym7xEk4bocjcjpbQogy`</summary>

```text
Web search results for query: "accelerate ACDC circuit discovery speedup methods SP-ACDC hierarchical"

Links: [{"title":"Automatic Circuit Discovery","url":"https://sidn.baulab.info/autocircuits/"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/html/2510.23264"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through ...","url":"https://arxiv.org/pdf/2510.23264"},{"title":"[2510.23264] PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/abs/2510.23264"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery · GitHub","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery"},{"title":"(PDF) Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://www.researchgate.net/publication/370417693_Towards_Automated_Circuit_Discovery_for_Mechanistic_Interpretability"},{"title":"Automatic Circuit Discovery (ACDC)","url":"https://www.emergentmind.com/topics/automatic-circuit-discovery-acdc"},{"title":"Automatic circuit discovery | Arthur’s Site","url":"https://arthurconmy.github.io/automatic_circuit_discovery/"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"}]

Based on the search results, here's what I found about accelerating ACDC circuit discovery and speedup methods:

## Overview of ACDC

Automated Circuit DisCovery (ACDC) is an attempt to formalize and automate the process of circuit discovery. The ACDC algorithm uses activation patching to prune out edges from the computation graph to get the circuit responsible for performing a specific task.

## Key Computational Challenge

Computing the relevance of an edge in the computation graph requires one forward pass, implying the number of forward passes required to get the entire circuit grows with the size of the model, hence making the ACDC algorithm intractable for larger models.

## Speedup Methods

### SP-ACDC and HISP Baselines

The authors introduce two baselines: Subnetwork Probing (SP) and Head Importance Score for Pruning (HISP), where SP optimizes a mask over model components using gradient descent, while HISP uses a first-order Taylor approximation to estimate the effect of replacing a head's output with corrupted inputs.

### Attribution Patching (EAP)

Attribution patching approximates the impact of activation patching on model's output using the first-order Taylor series, and this work proposes to use attribution patching to estimate the relevance of an edge in the computation graph to speed up the circuit discovery algorithm. Attribution patching is a technique to estimate the impact of activation patching using only two forward passes and one backward pass.

### PAHQ (Per Attention Head Quantization)

A more recent acceleration approach is PAHQ (Per Attention Head Quantization), which takes a fundamentally different approach by optimizing the efficiency of each individual patching operation. PAHQ-accelerated ACDC reduces runtime by up to 80% and memory consumption by up to 30% compared to unaccelerated ACDC while maintaining faithfulness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed273d9a-d04f-4a95-9858-8ea669b62435",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "177066de-7f98-47cf-808c-cce521101e35",
  "sourceToolAssistantUUID": "ed273d9a-d04f-4a95-9858-8ea669b62435",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-12T10:20:50.388Z_

Good, I have initial results. Let me now fetch the paper details and check the GitHub repo.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "177066de-7f98-47cf-808c-cce521101e35",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWMfXuzyPY2xLHz1qAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd0f1c38-0a27-453c-ad9b-5ac48f7ac943",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xew7e4Fr2KH4XXdmhCgNzN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 987,
      "cache_creation_input_tokens": 2656,
      "cache_read_input_tokens": 16243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2656,
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

_source line 16 · 2026-05-12T10:20:53.466Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XnJTHpHndAB5sL6KD1KyEP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.23264",
  "prompt": "Extract: 1) Full title and authors. 2) Abstract text. 3) Exact speedup numbers claimed. 4) What models were tested (GPT-2, Llama, Qwen?). 5) Is it edge-level or node-level circuit discovery? 6) Does it use TransformerLens? 7) What is the algorithm - still causal intervention / activation patching?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd0f1c38-0a27-453c-ad9b-5ac48f7ac943",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWMfXuzyPY2xLHz1qAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e05c4a85-d949-4bf9-9d87-f06b698f7494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xew7e4Fr2KH4XXdmhCgNzN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 987,
      "cache_creation_input_tokens": 2656,
      "cache_read_input_tokens": 16243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2656,
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

_source line 17 · 2026-05-12T10:20:55.722Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MBgwuDFJjkdQWEcaKixeg9`</summary>

```json
{
  "url": "https://github.com/626619403/PAHQ",
  "prompt": "Extract: 1) Repository contents - what files/directories exist. 2) README contents. 3) Dependencies - does it use TransformerLens? 4) What models are supported? 5) Installation instructions. 6) Is there working code or just a placeholder?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e05c4a85-d949-4bf9-9d87-f06b698f7494",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWMfXuzyPY2xLHz1qAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e714afd-d8e9-4150-a705-d7707f89cecb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xew7e4Fr2KH4XXdmhCgNzN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 987,
      "cache_creation_input_tokens": 2656,
      "cache_read_input_tokens": 16243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2656,
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

_source line 18 · 2026-05-12T10:20:56.780Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KrAkwJWJsF35xraRXzBdrW`</summary>

```json
{
  "query": "EAP-IG edge attribution patching ACDC speedup circuit discovery large language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e714afd-d8e9-4150-a705-d7707f89cecb",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWMfXuzyPY2xLHz1qAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47ca7306-b784-4e68-84c1-c1cebbba06a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xew7e4Fr2KH4XXdmhCgNzN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 987,
      "cache_creation_input_tokens": 2656,
      "cache_read_input_tokens": 16243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2656,
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

_source line 19 · 2026-05-12T10:20:57.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DmHenou8fCgGkERK3P1saq`</summary>

```json
{
  "query": "\"efficient automated circuit discovery\" EACDC arXiv 2407 speedup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47ca7306-b784-4e68-84c1-c1cebbba06a7",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWMfXuzyPY2xLHz1qAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01e708d6-0b7f-4a4c-89d2-3c3d6d632e21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xew7e4Fr2KH4XXdmhCgNzN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 987,
      "cache_creation_input_tokens": 2656,
      "cache_read_input_tokens": 16243,
      "output_tokens": 426,
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
          "input_tokens": 987,
          "output_tokens": 426,
          "cache_read_input_tokens": 16243,
          "cache_creation_input_tokens": 2656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2656,
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

_source line 20 · 2026-05-12T10:20:58.672Z_

<details><summary>↩ Tool result · `toolu_01XnJTHpHndAB5sL6KD1KyEP`</summary>

```text
# PAHQ Paper Analysis

**1) Full Title and Authors:**
"PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization" by Xinhai Wang, Shu Yang, Liangyu Wang, Lin Zhang, Huanyi Xie, Lijie Hu, and Di Wang.

**2) Abstract:**
The paper addresses computational inefficiency in Automated Circuit Discovery (ACDC) for large language models. It proposes Per Attention Head Quantization (PAHQ), which "leverages a fundamental alignment between activation patching and mixed-precision quantization" by maintaining high precision for investigated components while reducing precision elsewhere.

**3) Exact Speedup Numbers:**
"PAHQ-accelerated ACDC reduces runtime by up to 80% and memory consumption by up to 30% compared to unaccelerated ACDC while maintaining faithfulness."

**4) Models Tested:**
The webpage content does not specify which language models were evaluated in experiments.

**5) Circuit Discovery Level:**
The abstract notes the method "readily integrates with existing edge-based circuit discovery techniques," indicating it addresses edge-level discovery.

**6) TransformerLens Usage:**
Not mentioned in the provided content.

**7) Algorithm Approach:**
Yes, it employs the same core mechanism: "interpretability analysis through patching essentially performs targeted ablation studies," confirming continued use of activation patching methodology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e05c4a85-d949-4bf9-9d87-f06b698f7494",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "0b1ba36c-d1fe-4426-a812-f90bbb9ae67e",
  "sourceToolAssistantUUID": "e05c4a85-d949-4bf9-9d87-f06b698f7494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T10:21:02.747Z_

<details><summary>↩ Tool result · `toolu_01DmHenou8fCgGkERK3P1saq`</summary>

```text
Web search results for query: ""efficient automated circuit discovery" EACDC arXiv 2407 speedup"

Links: [{"title":"[2407.00886] Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/abs/2407.00886"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT AUTOMATED CIRCUIT","url":"https://arxiv.org/pdf/2407.00886"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition","url":"https://arxiv.org/html/2407.00886v2"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/html/2510.23264v1"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"[2510.23264] PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/abs/2510.23264"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through ...","url":"https://arxiv.org/pdf/2510.23264"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/html/2510.03282v1"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240700886H/abstract"},{"title":"Rethinking Circuit Completeness in Language Models: AND, OR, and ADDER Gates","url":"https://arxiv.org/html/2505.10039v1"}]

I found the paper you're looking for! The research achieves a significant speedup in circuit discovery, reducing runtime from hours to seconds compared to state-of-the-art baselines through recursively computing contribution of all nodes in a computational graph using CD-T (Contextual Decomposition for Transformers) followed by pruning.

The paper, titled "Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition," was published on arXiv as 2407.00886. CD-T is designed to build interpretable circuits in large language models and can produce circuits of arbitrary level of abstraction, with the ability to produce circuits as fine-grained as attention heads at specific sequence positions efficiently.

The method outperforms ACDC and EAP by better recovering manual circuits with an average of 97% ROC AUC under low runtimes on three standard circuit evaluation datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01e708d6-0b7f-4a4c-89d2-3c3d6d632e21",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "a634157c-08e1-4faf-88f7-a378c8d237d8",
  "sourceToolAssistantUUID": "01e708d6-0b7f-4a4c-89d2-3c3d6d632e21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T10:21:02.752Z_

<details><summary>↩ Tool result · `toolu_01MBgwuDFJjkdQWEcaKixeg9`</summary>

```text
# PAHQ Repository Analysis

## 1) Repository Contents
The repository includes:
- `PAHQ_ACDC/` directory (main implementation)
- `transformer_lens/transformer_lens/` subdirectory
- `cmapy.py` file
- `requirements.txt`
- `LICENSE` and `readme.md`

## 2) README Contents
The project focuses on "Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization." It modifies the ACDC codebase and transformer_lens library to optimize circuit discovery performance.

## 3) Dependencies - TransformerLens Usage
Yes, the project explicitly depends on transformer_lens. The README states: "Replace the original transformer_lens library...with the modified versions provided in this directory."

## 4) Supported Models
The configuration supports three model types:
- `attn-only-4l`
- `redwood_attn_2l`
- `gpt2`

## 5) Installation Instructions
Basic setup involves: (1) installing dependencies via pip, (2) replacing transformer_lens and cmapy.py files in your Python environment, and (3) navigating to the PAHQ_ACDC directory.

## 6) Working Code Status
The repository appears functional—it provides executable scripts (`run_experiments.sh`) and detailed command-line parameters for running experiments, suggesting active, working implementation rather than placeholder code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e714afd-d8e9-4150-a705-d7707f89cecb",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "de0d80df-16d8-44fb-8116-1b4d2de029a9",
  "sourceToolAssistantUUID": "8e714afd-d8e9-4150-a705-d7707f89cecb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T10:21:04.321Z_

<details><summary>↩ Tool result · `toolu_01KrAkwJWJsF35xraRXzBdrW`</summary>

```text
Web search results for query: "EAP-IG edge attribution patching ACDC speedup circuit discovery large language models"

Links: [{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://www.researchgate.net/publication/386190657_Attribution_Patching_Outperforms_Automated_Circuit_Discovery"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery Aaquib Syed","url":"https://openreview.net/pdf?id=tiLbFR4bJW"},{"title":"[2310.10348] Attribution Patching Outperforms Automated Circuit Discovery","url":"https://arxiv.org/abs/2310.10348"},{"title":"Automatic Circuit Discovery","url":"https://sidn.baulab.info/autocircuits/"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/html/2510.23264"},{"title":"Edge Attribution Patching (EAP)","url":"https://www.emergentmind.com/topics/edge-attribution-patching-eap"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://aclanthology.org/2024.blackboxnlp-1.25.pdf"},{"title":"Published as a conference paper at ICLR 2025 EFFICIENT AUTOMATED CIRCUIT","url":"https://arxiv.org/pdf/2407.00886"},{"title":"EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification","url":"https://arxiv.org/html/2502.06852v1"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through ...","url":"https://arxiv.org/pdf/2510.23264"}]

Based on the search results, here's information about the topics you queried:

## Edge Attribution Patching (EAP) and EAP-IG

Edge Attribution Patching (EAP) is a gradient-based automated circuit discovery method central to mechanistic interpretability of neural networks, particularly transformer LLMs. EAP assigns edge-level importance scores by linearly approximating the causal impact of substituting (patching) each edge's internal activation between clean and corrupted model runs—enabling efficient identification of circuits underlying specific model behaviors.

Edge Attribution Patching with Integrated Gradients (EAP-IG) was proposed for more faithful circuit recovery. EAP-IG linearly interpolates between activations induced by the paired slices and accumulates gradients along the path, yielding scores for heterogeneous circuit elements.

## ACDC and Speedup Improvements

The Automatic Circuit Discovery (ACDC) method proposed by Conmy et al. (2023) served as the first scalable, end-to-end approach for identifying behavior-related circuits in models. However, EAP only takes a constant number of forward and backwards passes while the number of forward passes required by ACDC is scaling exponentially with the number of nodes.

Recent work has focused on speedup improvements. PAHQ-accelerated ACDC reduces runtime by up to 80% and memory consumption by up to 30% compared to unaccelerated ACDC while maintaining faithfulness.

## Circuit Discovery and Large Language Models

A main method for understanding model behavior is to decompose a model into circuits—interpretable computational subgraphs responsible for specific model behaviors. These techniques are particularly relevant for mechanistic interpretability research on large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47ca7306-b784-4e68-84c1-c1cebbba06a7",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "7ba92f1b-2462-4519-84b0-4b5f796dd921",
  "sourceToolAssistantUUID": "47ca7306-b784-4e68-84c1-c1cebbba06a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-12T10:21:08.525Z_

Let me fetch more details on the PAHQ paper (the full HTML version) and the EACDC paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ba92f1b-2462-4519-84b0-4b5f796dd921",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWP2EdXDynFcoXMdkTX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d6a7445-b07c-43d6-b617-f2cef0378a81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WLivQdB1sctqXSMcYq77Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 707,
      "cache_creation_input_tokens": 2979,
      "cache_read_input_tokens": 18899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2979,
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

_source line 25 · 2026-05-12T10:21:13.128Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GsWiX4WF98q6XS2yaNRTrT`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.23264",
  "prompt": "Extract: 1) What specific models were tested in experiments (GPT-2 small? Llama? Qwen? What sizes?). 2) Exact speedup numbers - wall-clock time comparisons. 3) Is it edge-level or node-level? Quote any relevant sentences. 4) What tasks/benchmarks were used? 5) Does PAHQ modify ACDC's algorithm or just accelerate each forward pass? 6) What quantization bit-widths are used (FP16, INT8, INT4?)? 7) Any mention of scaling to models larger than GPT-2?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d6a7445-b07c-43d6-b617-f2cef0378a81",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWP2EdXDynFcoXMdkTX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bd8c9da-2ed4-459b-99c4-2918afa5218a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WLivQdB1sctqXSMcYq77Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 707,
      "cache_creation_input_tokens": 2979,
      "cache_read_input_tokens": 18899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2979,
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

_source line 26 · 2026-05-12T10:21:14.638Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SabM1agoSBuKQS1Zg1MPFG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.00886",
  "prompt": "Extract: 1) Title and authors. 2) Abstract. 3) What speedup does it claim over ACDC? 4) What models were tested? 5) Is it edge-level or node-level? 6) Does it use TransformerLens?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bd8c9da-2ed4-459b-99c4-2918afa5218a",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWP2EdXDynFcoXMdkTX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65b30a62-ccd7-4bb0-aa14-c6a90c0fd2f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WLivQdB1sctqXSMcYq77Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 707,
      "cache_creation_input_tokens": 2979,
      "cache_read_input_tokens": 18899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2979,
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

_source line 27 · 2026-05-12T10:21:15.121Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WzgMrX5YoKdMErUKabSA1v`</summary>

```json
{
  "query": "circuit discovery Qwen model mechanistic interpretability 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65b30a62-ccd7-4bb0-aa14-c6a90c0fd2f5",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWP2EdXDynFcoXMdkTX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9efb443-8b5b-4276-8b08-88fdb0855927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WLivQdB1sctqXSMcYq77Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 707,
      "cache_creation_input_tokens": 2979,
      "cache_read_input_tokens": 18899,
      "output_tokens": 422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 707,
          "output_tokens": 422,
          "cache_read_input_tokens": 18899,
          "cache_creation_input_tokens": 2979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2979,
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

_source line 28 · 2026-05-12T10:21:19.363Z_

<details><summary>↩ Tool result · `toolu_01SabM1agoSBuKQS1Zg1MPFG`</summary>

```text
# Paper Analysis: Efficient Automated Circuit Discovery in Transformers

**1) Title and Authors:**
"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition" by Aliyah R. Hsu, Georgia Zhou, Yeshwanth Cherapanamjeri, Yaxuan Huang, Anobel Y. Odisho, Peter R. Carroll, and Bin Yu.

**2) Abstract:**
The paper introduces contextual decomposition for transformers (CD-T) to build interpretable circuits in large language models. It demonstrates that CD-T can "reduce circuit discovery runtime from hours to seconds compared to state-of-the-art baselines" while achieving "an average of 97% ROC AUC" on evaluation datasets.

**3) Speedup over ACDC:**
The document states CD-T reduces runtime "from hours to seconds" compared to ACDC but does not specify an exact numerical speedup factor.

**4) Models Tested:**
The paper evaluated CD-T on "three standard circuit evaluation datasets (indirect object identification, greater-than comparisons, and docstring completion)" but does not name specific model architectures tested.

**5) Edge-level or Node-level:**
CD-T operates at the node level, producing "circuits as fine-grained as attention heads at specific sequence positions."

**6) TransformerLens:**
The webpage content does not mention TransformerLens.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65b30a62-ccd7-4bb0-aa14-c6a90c0fd2f5",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "f673876a-0aab-424e-8769-ee8b48baac9c",
  "sourceToolAssistantUUID": "65b30a62-ccd7-4bb0-aa14-c6a90c0fd2f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-12T10:21:21.435Z_

<details><summary>↩ Tool result · `toolu_01GsWiX4WF98q6XS2yaNRTrT`</summary>

```text
# PAHQ Paper Analysis

## 1) Models Tested
The experiments evaluated three primary models: **GPT-2 (small)**, **Attn-4l** (4-layer attention-only), and **Redwood-2l** (2-layer). Appendix C demonstrates scalability to GPT-2-medium, GPT-2-large, and GPT-2-XL.

## 2) Speedup Numbers
On GPT-2, PAHQ achieves approximately **80% runtime reduction** compared to unaccelerated ACDC. Specifically: standard ACDC required 99:18 minutes; PAHQ reduced this to 20:36 minutes. Memory consumption decreased by roughly **30%** (6.23 GB to 4.24 GB).

## 3) Edge vs. Node Level
The method operates at **edge-level**. The paper states: *"automated circuit discovery algorithms typically evaluate only one edge at a time."* Each evaluation involves a specific edge e=(u→v), maintaining high precision exclusively for the source node's activations.

## 4) Tasks/Benchmarks
Three standard circuit discovery tasks were evaluated:
- **Indirect Object Identification (IOI)**
- **Docstring** (Python function documentation)
- **Greater Than** (numerical comparison)

## 5) Algorithm Modification Scope
PAHQ doesn't alter ACDC's core algorithm; rather, it *"optimizes the efficiency of each individual patching operation"* through mixed-precision quantization and computation-communication overlap scheduling.

## 6) Quantization Bit-Widths
Primary precision levels: **FP32** (critical components) and **FP8_E4M3** (non-critical). Non-attention components use **bfloat16 (bf16)**. Ablation studies tested 4-bit (severely compromised) and 16-bit alternatives.

## 7) Large Model Scaling
Yes, Appendix C demonstrates effectiveness on larger models, achieving average KL divergence of 0.89 across GPT-2-medium/large/XL compared to 0.79 on GPT-2-small ACDC.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bd8c9da-2ed4-459b-99c4-2918afa5218a",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "0d067621-627b-45f4-ba6e-fc18341f287a",
  "sourceToolAssistantUUID": "2bd8c9da-2ed4-459b-99c4-2918afa5218a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T10:21:22.045Z_

<details><summary>↩ Tool result · `toolu_01WzgMrX5YoKdMErUKabSA1v`</summary>

```text
Web search results for query: "circuit discovery Qwen model mechanistic interpretability 2025 2026"

Links: [{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Circuit-Tracer: A New Library for Finding Feature Circuits | Request PDF","url":"https://www.researchgate.net/publication/397423219_Circuit-Tracer_A_New_Library_for_Finding_Feature_Circuits"},{"title":"Corti introduces GIM: Benchmark-leading method for understanding AI model behavior | Corti","url":"https://www.corti.ai/stories/gim-a-new-standard-for-mechanistic-interpretability"},{"title":"Mechanistic Interpretability Explained: Circuits, Sparse Autoencoders, Causal Tracing, and AI Safety | by Adnan Masood, PhD. | Apr, 2026 | Medium","url":"https://medium.com/@adnanmasood/mechanistic-interpretability-explained-circuits-sparse-autoencoders-causal-tracing-and-ai-88ecc8d70b72"},{"title":"Circuit Tracing for the Rest of Us: From Probes to Attribution Graphs and What It Means for Production Safety | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/circuit-tracing-production/"},{"title":"RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching | OpenReview","url":"https://openreview.net/forum?id=5PKPy82sWN"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/html/2510.14936"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://arxiv.org/html/2603.18353"},{"title":"Open problems in mechanistic interpretability: 2026 status report","url":"https://gist.github.com/bigsnarfdude/629f19f635981999c51a8bd44c6e2a54"}]

Based on the web search results, here's what I found regarding circuit discovery, Qwen models, and mechanistic interpretability in 2025-2026:

## Key Findings

**Qwen Models in Mechanistic Interpretability Research:**

The Mechanistic Interpretability Benchmark (MIB) evaluates circuit localization and causal variable localization across diverse tasks and models including Qwen-2.5. Additionally, feature circuits have been traced through the Qwen-3 family (0.6B, 4B, 8B, 14B) to investigate memory system operations.

Probes for detecting AI sandbagging achieved 90-96% accuracy across Mistral, Gemma, and Qwen models, and the community needs circuit tracing capability on Llama, Mistral, Qwen, and Gemma.

**Circuit Discovery Advances:**

Recent advances in mechanistic interpretability have shifted towards automated circuit discovery (Hanna et al., 2025; Hasani et al., 2026), aiming to reverse-engineer LLM behaviors into sparse computational subgraphs. 

Automated circuit discovery is a central tool in mechanistic interpretability for identifying internal components responsible for specific behaviors, though prior methods typically depend on heuristics or approximations and do not offer provable guarantees.

**Current Challenges:**

Circuit discovery faces fundamental complexity barriers, with a 2025 ICLR paper proving many circuit-finding queries are NP-hard and remain fixed-parameter intractable, and Anthropic's attribution graphs can successfully trace computational paths for only about 25% of prompts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9efb443-8b5b-4276-8b08-88fdb0855927",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "c8a2f8b5-5c1f-4eca-9bcf-d3615b8fdd34",
  "sourceToolAssistantUUID": "a9efb443-8b5b-4276-8b08-88fdb0855927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T10:21:25.332Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NN1wc1Nx685KsyduuCcauU`</summary>

```json
{
  "query": "ACDC circuit discovery runtime hours GPT-2 small scaling larger models Llama Qwen wall clock time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8a2f8b5-5c1f-4eca-9bcf-d3615b8fdd34",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWQKzzifUQxfDGSpmBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2a9c62a-3849-4e2c-a628-edcd308065b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Wh9BxperL3KPSLAgy7yur",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3004,
      "cache_read_input_tokens": 21878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3004,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-12T10:21:26.020Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EWyKUM8M3jAPx9WwppxpDJ`</summary>

```json
{
  "query": "IBCircuit arXiv 2602.22581 circuit discovery information bottleneck speedup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2a9c62a-3849-4e2c-a628-edcd308065b9",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWQKzzifUQxfDGSpmBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23640029-968f-4bdc-9187-9e13047f9589",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Wh9BxperL3KPSLAgy7yur",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3004,
      "cache_read_input_tokens": 21878,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3004
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 21878,
          "cache_creation_input_tokens": 3004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3004,
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

_source line 33 · 2026-05-12T10:21:32.938Z_

<details><summary>↩ Tool result · `toolu_01EWyKUM8M3jAPx9WwppxpDJ`</summary>

```text
Web search results for query: "IBCircuit arXiv 2602.22581 circuit discovery information bottleneck speedup"

Links: [{"title":"[2602.22581] IBCircuit: Towards Holistic Circuit Discovery with Information Bottleneck","url":"https://arxiv.org/abs/2602.22581"},{"title":"IBCircuit: Towards Holistic Circuit Discovery with Information Bottleneck","url":"https://arxiv.org/html/2602.22581"},{"title":"IBCircuit: Towards Holistic Circuit Discovery with Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=APElRzkmGY"},{"title":"IBCircuit: Towards Holistic Circuit Discovery with Information Bottleneck","url":"https://openreview.net/pdf?id=APElRzkmGY"},{"title":"ICML Poster IBCircuit: Towards Holistic Circuit Discovery with Information Bottleneck","url":"https://icml.cc/virtual/2025/poster/46175"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/html/2510.23264"},{"title":"Differentiable Logical Programming for Quantum Circuit Discovery and Optimization","url":"https://arxiv.org/html/2602.08880"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"The Computational Complexity of Circuit Discovery for Inner Interpretability","url":"https://arxiv.org/html/2410.08025v1"},{"title":"[2504.16999] Learning to decode logical circuits","url":"https://arxiv.org/abs/2504.16999"}]

Based on the search results, I found detailed information about IBCircuit (arXiv 2602.22581):

## Overview

IBCircuit is an end-to-end approach based on the principle of Information Bottleneck, designed to identify informative circuits holistically.

## Key Features

IBCircuit is an optimization framework for holistic circuit discovery and can be applied to any given task without tediously corrupted activation design. IBCircuit injects controllable Gaussian noise with learnable IB weights into various model components (e.g., the activations of attention heads and MLPs). It modulates the flow of clean information from the original pretrained model to its distorted version. The IBCircuit objective encourages the distorted flow to retain its informativeness. Therefore, IBCircuit preserves the most informative components with minimal noise injection.

## Advantages Over Existing Methods

Most existing studies overlook the holistic nature of these circuits and require designing specific corrupted activations for different tasks, which is inaccurate and inefficient. In contrast, IBCircuit identifies more faithful and minimal circuits in terms of critical node components and edge components compared to recent related work.

## Applications

In both the Indirect Object Identification (IOI) and Greater-Than tasks, IBCircuit identifies more faithful and minimal circuits in terms of critical node components and edge components.

The paper was submitted to arXiv on February 26, 2026, and the code is available at GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23640029-968f-4bdc-9187-9e13047f9589",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "a2170150-45b8-4635-904c-1b4980084d37",
  "sourceToolAssistantUUID": "23640029-968f-4bdc-9187-9e13047f9589",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T10:21:35.341Z_

<details><summary>↩ Tool result · `toolu_01NN1wc1Nx685KsyduuCcauU`</summary>

```text
Web search results for query: "ACDC circuit discovery runtime hours GPT-2 small scaling larger models Llama Qwen wall clock time"

Links: [{"title":"PAHQ: Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization","url":"https://arxiv.org/html/2510.23264"},{"title":"PAHQ: Accelerating Automated Circuit Discovery through ...","url":"https://arxiv.org/pdf/2510.23264"},{"title":"LLM Architecture Gallery | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/llm-architecture-gallery/"},{"title":"Accelerating LLaMA-2 Inference with ONNX Runtime","url":"https://onnxruntime.ai/blogs/accelerating-llama-2"},{"title":"Model Catalog - LM Studio","url":"https://lmstudio.ai/models"},{"title":"Automatic Discovery of Visual Circuits","url":"https://arxiv.org/html/2404.14349v1"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Reproducing GPT-2 (124M) in llm.c in 90 minutes for $20 · karpathy/llm.c · Discussion #481","url":"https://github.com/karpathy/llm.c/discussions/481"},{"title":"Automatic Circuit Discovery (ACDC)","url":"https://www.emergentmind.com/topics/automatic-circuit-discovery-acdc"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"}]

I've performed the web search for your query. Based on the results, here's what I found:

The search returned relevant information about ACDC (Automatic Circuit Discovery) and its runtime performance. The most relevant result is from a recent paper on PAHQ (Accelerating Automated Circuit Discovery through Mixed-Precision Inference Optimization), which directly addresses your query about runtime hours for circuit discovery.

Key findings:

When applied to GPT-2, ACDC accelerated by PAHQ reduces computation time by approximately 80% while achieving memory compression ratios exceeding 30% compared to unaccelerated ACDC.

The paper also discusses scalability to larger models, though the search results show this information is covered in Appendix C of the paper, which wasn't fully captured in the excerpt.

Additionally, results remain consistent across different model sizes (Attn-4l and Redwood-2l), indicating that the ACDC method has been tested on models of varying sizes.

For information about scaling ACDC to larger models like Llama and Qwen with specific wall clock time measurements, the search results reference that such analysis exists in the paper's appendix, but the detailed runtime hours for these larger models weren't included in the retrieved excerpts. You may want to consult the full PAHQ paper (arxiv:2510.23264) for complete runtime comparisons across different model scales.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2a9c62a-3849-4e2c-a628-edcd308065b9",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "c4bc1b07-7f88-488e-a346-a1eca04833d8",
  "sourceToolAssistantUUID": "a2a9c62a-3849-4e2c-a628-edcd308065b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-12T10:21:39.359Z_

Now let me check the PAHQ paper more carefully for scaling analysis and see if there's any data on models beyond GPT-2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4bc1b07-7f88-488e-a346-a1eca04833d8",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWRJobJh7zcMdV4RB7d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d19b645c-eba3-41f1-a1c7-5ece38b68538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Qa7V5UXpDWo4FbhtwQYFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 822,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 24882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 916,
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

_source line 36 · 2026-05-12T10:21:42.678Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VSDRURSebpZpNfVm886woW`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.23264",
  "prompt": "Focus on Appendix C and any discussion of scaling to larger models. What are the exact wall-clock times reported for GPT-2-medium, GPT-2-large, GPT-2-XL? How does runtime scale with model size? Is there any discussion of models beyond GPT-2 family (e.g., Llama, Qwen, Pythia)? What GPU was used for experiments? What is the computational complexity analysis - how does ACDC runtime scale with number of edges?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d19b645c-eba3-41f1-a1c7-5ece38b68538",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWRJobJh7zcMdV4RB7d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7cad8a9-1aa9-4119-b230-e8b32e6124f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Qa7V5UXpDWo4FbhtwQYFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 822,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 24882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 916,
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

_source line 37 · 2026-05-12T10:21:44.582Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015GTZzfpcynqTaGBZxBD3D7`</summary>

```json
{
  "url": "https://github.com/626619403/PAHQ",
  "prompt": "Look at the README more carefully. What models are supported? Is there any mention of adding new models? What version of TransformerLens is used? Is there a requirements.txt content visible? How is the ACDC code structured - is it a fork of ArthurConmy/Automatic-Circuit-Discovery?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7cad8a9-1aa9-4119-b230-e8b32e6124f3",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWRJobJh7zcMdV4RB7d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ceb9ac4-0033-4b28-a084-4b99e46e069f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Qa7V5UXpDWo4FbhtwQYFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 822,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 24882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 916,
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

### Tool result

_source line 38 · 2026-05-12T10:21:47.983Z_

<details><summary>↩ Tool result · `toolu_01VSDRURSebpZpNfVm886woW`</summary>

```text
# PAHQ Scalability Analysis: Key Findings

## Wall-Clock Times for Larger Models

Appendix C does **not report wall-clock times** for GPT-2-medium, GPT-2-large, or GPT-2-XL. Instead, Table 7 only provides KL divergence metrics comparing PAHQ against the EAP baseline across these models. The paper states: "Due to computational constraints on larger models, we implemented a batched version of edge evaluation."

## Runtime Scaling Discussion

The paper explicitly acknowledges scaling limitations: "The original ACDC method becomes computationally prohibitive on larger models, even with batch processing optimizations; therefore, we are unable to provide ACDC results on larger models."

No quantitative runtime scaling analysis is provided.

## Non-GPT-2 Models

The work is **limited to the GPT-2 family only**. No experiments on Llama, Qwen, Pythia, or other architectures are discussed.

## GPU Hardware

Experiments used "NVIDIA H20-NVLink GPU (96GB)" and "a single NVIDIA H20 GPU" for larger model experiments (Appendix B.1 and D.2).

## Computational Complexity Analysis

The paper does **not provide explicit complexity analysis** for how ACDC runtime scales with edge count. It only notes that ACDC has "quadratic complexity with respect to model components" and is "O(|E|)" in the preliminaries, without deriving scaling coefficients or empirical complexity curves for larger graphs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7cad8a9-1aa9-4119-b230-e8b32e6124f3",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "1e75e24e-332c-4270-a316-3629184f1b83",
  "sourceToolAssistantUUID": "f7cad8a9-1aa9-4119-b230-e8b32e6124f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-12T10:21:48.073Z_

<details><summary>↩ Tool result · `toolu_015GTZzfpcynqTaGBZxBD3D7`</summary>

```text
# Analysis of PAHQ Repository README

## Supported Models
The README lists three supported models: `attn-only-4l`, `redwood_attn_2l`, and `gpt2`. These appear as configuration options in the experimental parameters section.

## Adding New Models
There is **no mention** of procedures for adding new models to the framework.

## TransformerLens Version
The README does not specify which version of TransformerLens is used. It only states that the implementation "is based on modifications to the original ACDC codebase and the transformer_lens library."

## Requirements.txt Content
While a `requirements.txt` file is listed in the repository, **its contents are not visible** in the provided webpage content.

## ACDC Code Structure
The README indicates the implementation involves "modifications to the original ACDC codebase" but does not explicitly confirm whether this is a fork of ArthurConmy/Automatic-Circuit-Discovery. The directory structure shows a `PAHQ_ACDC` folder, suggesting custom modifications rather than a direct fork, but the exact relationship to the original repository is not clearly stated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ceb9ac4-0033-4b28-a084-4b99e46e069f",
  "isSidechain": true,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "agentId": "a97febb1e84474d24",
  "type": "user",
  "uuid": "c4838cc4-0939-4238-84f1-f0dab9100723",
  "sourceToolAssistantUUID": "0ceb9ac4-0033-4b28-a084-4b99e46e069f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-12T10:22:28.670Z_

Now I have enough information. Here is my report.

---

## PAHQ (arXiv:2510.23264) - Research Summary

### 1. Open-source code

Yes. GitHub repo: [https://github.com/626619403/PAHQ](https://github.com/626619403/PAHQ). It contains working code with `PAHQ_ACDC/` directory, a modified `transformer_lens/` copy, `run_experiments.sh`, and `requirements.txt`. It is a modification of the original ACDC codebase, not a clean fork.

### 2. Speedup claims

- **Up to 80% runtime reduction** (5x speedup): on GPT-2 small IOI task, standard ACDC took 99:18 min, PAHQ reduced to 20:36 min.
- **~30% memory reduction**: 6.23 GB down to 4.24 GB.
- The speedup comes from mixed-precision quantization of each forward pass, not from changing ACDC's algorithmic structure.

### 3. TransformerLens integration

Yes, PAHQ builds on top of TransformerLens. The repo includes a **modified copy** of TransformerLens that must replace the original installation. This is a concern - it's not a plugin but a fork of the library.

### 4. Can it bring Qwen-2.5 0.5B ACDC from ~42-127h to ≤10h?

**Almost certainly not.** Critical limitations:

- PAHQ was only tested on GPT-2 small (124M params, 12 layers, 12 heads). The largest model tested was GPT-2-XL (1.5B) but **only for KL divergence metrics, not ACDC runtime** - the paper explicitly states "The original ACDC method becomes computationally prohibitive on larger models... we are unable to provide ACDC results on larger models."
- The repo only supports `gpt2`, `attn-only-4l`, and `redwood_attn_2l`.
- PAHQ's 5x speedup on GPT-2 small (99 min -> 20 min) addresses a ~1.5h baseline. Your baseline is 42-127h on Qwen-2.5 0.5B. Even a 5x speedup gives 8-25h, not ≤10h for the worst case.
- PAHQ uses a **modified TransformerLens fork** - adapting it to Qwen architecture would require significant engineering.
- The quantization scheme (FP32 for critical heads, FP8_E4M3 for others, bf16 for non-attention) is GPU-dependent (tested on H20 96GB with FP8 support).

### 5. Edge-level or node-level?

**Edge-level.** The paper states: "automated circuit discovery algorithms typically evaluate only one edge at a time." Each evaluation maintains high precision for the source node's activations of a specific edge e=(u->v).

### 6. Algorithm family

**Still causal intervention / activation patching.** PAHQ does not change ACDC's algorithm. It accelerates each individual patching forward pass by quantizing non-critical components to lower precision. The core loop remains: iterate over edges, patch activations, measure KL divergence, prune.

---

## Other ACDC Acceleration Methods

### EAP / Attribution Patching (arXiv:2310.10348)
- Replaces ACDC's O(|E|) forward passes with **2 forward passes + 1 backward pass** using first-order Taylor approximation.
- Dramatically faster but **less faithful** - it's an approximation, not exact causal intervention.
- Edge-level. Works with TransformerLens.

### CD-T / Efficient Automated Circuit Discovery (arXiv:2407.00886, ICLR 2025)
- Uses Contextual Decomposition for Transformers.
- Claims to reduce runtime **from hours to seconds**.
- Node-level (attention head granularity). 97% ROC AUC on standard benchmarks.
- Different algorithmic family - not activation patching but decomposition-based.

### IBCircuit (arXiv:2602.22581, ICML 2025)
- Information Bottleneck-based optimization framework.
- Injects learnable Gaussian noise; optimizes to preserve informative components.
- Both node and edge level. End-to-end optimization, no need for hand-designed corrupted activations.
- More recent (Feb 2026), potentially more scalable.

### EAP-GP (arXiv:2502.06852)
- Mitigates saturation effects in gradient-based circuit identification (improving EAP-IG).

---

## Bottom Line for Your Use Case

For Qwen-2.5 0.5B circuit discovery in ≤10h per task, PAHQ alone is insufficient. The most promising directions are:

1. **EAP/Attribution Patching**: orders of magnitude faster than ACDC, but approximate. Could serve as a first-pass filter followed by targeted ACDC on a reduced graph.
2. **CD-T**: claims hours-to-seconds reduction, but node-level only.
3. **IBCircuit**: optimization-based, potentially more scalable to larger models, but very new.
4. **Hybrid approach**: Use EAP to identify candidate edges, then run ACDC (possibly PAHQ-accelerated) only on the top-k edges. This is the most realistic path to ≤10h.

PAHQ's 5x speedup is real but modest relative to your target, and the engineering cost of porting its modified TransformerLens fork to Qwen is non-trivial.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4838cc4-0939-4238-84f1-f0dab9100723",
  "isSidechain": true,
  "agentId": "a97febb1e84474d24",
  "requestId": "req_011CaxWSFEZNfNHUbeJ6L9ra",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18871f52-e1e4-4c28-b206-dff4c021b8b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdZBcuy5njqhocPPoRnPmg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1839,
      "cache_read_input_tokens": 25798,
      "output_tokens": 1370,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1839
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1370,
          "cache_read_input_tokens": 25798,
          "cache_creation_input_tokens": 1839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1839,
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
