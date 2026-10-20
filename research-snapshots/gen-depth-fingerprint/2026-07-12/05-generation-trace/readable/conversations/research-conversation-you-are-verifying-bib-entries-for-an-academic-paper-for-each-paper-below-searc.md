# Research conversation: You are verifying bib entries for an academic paper. For each paper below, search the web to confirm: 1. The paper actua

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3fc236c170c1507c.jsonl`
- **Structured JSON:** [`45691e300019b52686fe.json`](../../sessions/45/45691e300019b52686fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-16T01:17:01.203Z_

You are verifying bib entries for an academic paper. For each paper below, search the web to confirm:
1. The paper actually exists (not hallucinated)
2. The year is correct
3. If it's an arXiv preprint, check if it has been formally published at a venue
4. If it's listed as a journal/conference paper, verify the venue and year

Papers to verify (provide a structured report for each):

1. `ld_score`: "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection" by Narayanasamy et al., arXiv:2605.01647, 2026

2. `diveye`: "Diversity Boosts AI-Generated Text Detection" by Basani and Chen, TMLR, 2026

3. `generator_barrier`: "Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection" by Pu et al., arXiv:2604.13692, 2026

4. `feat_aug_transformer`: "Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators" by Mady et al., arXiv:2605.03969, 2026

5. `markovian_chains`: "Markovian Generation Chains in Large Language Models" by Geng et al., arXiv:2603.11228, 2026

6. `chainwash`: "Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks" by Ameen et al., arXiv:2605.05503, 2026

For each paper, report: EXISTS (yes/no/uncertain), YEAR_CORRECT (yes/no), NEEDS_UPDATE (if preprint now published at venue), NOTES.

Use WebSearch for each paper. Search by arXiv ID when available, or by title.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5d54a633-ce2f-442c-b92b-456437643336",
  "agentId": "a3fc236c170c1507c",
  "type": "user",
  "uuid": "01c55014-de76-4f9c-9d1b-27db14f93ac5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T01:17:01.206Z_

```json
{
  "parentUuid": "01c55014-de76-4f9c-9d1b-27db14f93ac5",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
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
  "uuid": "ac803001-3b20-4b28-98d3-b2a139dcfab7",
  "timestamp": "2026-05-16T01:17:01.206Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-16T01:17:03.100Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DwXqzMLNdWXKhQJVSsitaV`</summary>

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
  "parentUuid": "ac803001-3b20-4b28-98d3-b2a139dcfab7",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
  "requestId": "req_011Cb5N8RH9cbM9PfncAtnj1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a0ea1bf-823f-4d71-9b83-c491a6bfc49d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FvwvbFUgkrnsm1VocBvUZc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15263,
      "cache_read_input_tokens": 0,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15263
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15263,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15263,
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

_source line 4 · 2026-05-16T01:17:03.105Z_

<details><summary>↩ Tool result · `toolu_01DwXqzMLNdWXKhQJVSsitaV`</summary>

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
  "parentUuid": "4a0ea1bf-823f-4d71-9b83-c491a6bfc49d",
  "isSidechain": true,
  "promptId": "5d54a633-ce2f-442c-b92b-456437643336",
  "agentId": "a3fc236c170c1507c",
  "type": "user",
  "uuid": "830b4195-98a9-4cf7-abca-d4022c72ea9e",
  "sourceToolAssistantUUID": "4a0ea1bf-823f-4d71-9b83-c491a6bfc49d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-16T01:17:04.824Z_

I'll search for all 6 papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "830b4195-98a9-4cf7-abca-d4022c72ea9e",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
  "requestId": "req_011Cb5N8ZhuGqef8mUdD6hRh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f7a805b-0b78-4755-b69a-f7b564c26d7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fun3jJqBPVCoc45ixBXLdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 15263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 6 · 2026-05-16T01:17:05.637Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E81vMGsAFr4bg8PnPjV75z`</summary>

```json
{
  "query": "arXiv:2605.01647 \"Beyond Perplexity\" MDTA Benchmark AI Text Detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f7a805b-0b78-4755-b69a-f7b564c26d7e",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
  "requestId": "req_011Cb5N8ZhuGqef8mUdD6hRh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db2c98e7-b43d-4ec9-a42d-218380496c69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fun3jJqBPVCoc45ixBXLdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 15263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 7 · 2026-05-16T01:17:05.773Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018EEZcBu1ay6e3egQYipiJZ`</summary>

```json
{
  "query": "\"Diversity Boosts AI-Generated Text Detection\" Basani Chen TMLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db2c98e7-b43d-4ec9-a42d-218380496c69",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
  "requestId": "req_011Cb5N8ZhuGqef8mUdD6hRh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f62eabf-7430-41d0-b76b-2ba09235812b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fun3jJqBPVCoc45ixBXLdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 15263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 8 · 2026-05-16T01:17:06.412Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dfy4mMPMGUDfKCU5VGbpkm`</summary>

```json
{
  "query": "arXiv:2604.13692 \"Breaking the Generator Barrier\" Disentangled Representation AI-Text Detection Pu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f62eabf-7430-41d0-b76b-2ba09235812b",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
  "requestId": "req_011Cb5N8ZhuGqef8mUdD6hRh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecc34ff6-d840-4758-bd43-9dfa4d0eecca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fun3jJqBPVCoc45ixBXLdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 15263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 9 · 2026-05-16T01:17:06.788Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U4NVUePmMqWzTqhpAsADR4`</summary>

```json
{
  "query": "arXiv:2605.03969 \"Feature-Augmented Transformers\" AI-Text Detection Domains Generators Mady"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecc34ff6-d840-4758-bd43-9dfa4d0eecca",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
  "requestId": "req_011Cb5N8ZhuGqef8mUdD6hRh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e747e3c-bfc9-4d74-80a2-f9333db0249d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fun3jJqBPVCoc45ixBXLdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 15263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 10 · 2026-05-16T01:17:07.177Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T2Atf2qgisdXSd1wWXLaKK`</summary>

```json
{
  "query": "arXiv:2603.11228 \"Markovian Generation Chains\" Large Language Models Geng 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e747e3c-bfc9-4d74-80a2-f9333db0249d",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
  "requestId": "req_011Cb5N8ZhuGqef8mUdD6hRh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e9d27f2-a349-494c-9e03-9cbc8c8c4e55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fun3jJqBPVCoc45ixBXLdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 15263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 11 · 2026-05-16T01:17:07.477Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012VG7LhPnr5bTWunrRn6nn8`</summary>

```json
{
  "query": "arXiv:2605.05503 \"Chainwash\" Rewriting Attacks Diffusion Language Model Watermarks Ameen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e9d27f2-a349-494c-9e03-9cbc8c8c4e55",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
  "requestId": "req_011Cb5N8ZhuGqef8mUdD6hRh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45e19728-32cc-42ce-8a54-0f4ea5900290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fun3jJqBPVCoc45ixBXLdC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 15263,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1439
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 405,
          "cache_read_input_tokens": 15263,
          "cache_creation_input_tokens": 1439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1439,
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

_source line 12 · 2026-05-16T01:17:12.517Z_

<details><summary>↩ Tool result · `toolu_01Dfy4mMPMGUDfKCU5VGbpkm`</summary>

```text
Web search results for query: "arXiv:2604.13692 "Breaking the Generator Barrier" Disentangled Representation AI-Text Detection Pu"

Links: [{"title":"[2604.13692v1] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692v1"},{"title":"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/html/2604.13692"},{"title":"[2604.13692] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692"},{"title":"Explainable Disentangled Representation Learning for Generalizable","url":"https://arxiv.org/pdf/2604.21300"},{"title":"Paper page - Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI","url":"https://huggingface.co/papers/2604.21300"},{"title":"[2604.21300] Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI","url":"https://arxiv.org/abs/2604.21300"},{"title":"AI Generated Text Detection Using Instruction Fine-tuned Large Language and Transformer-Based Models","url":"https://arxiv.org/html/2507.05157v1"},{"title":"Are AI-Generated Text Detectors Robust to Adversarial Perturbations?","url":"https://arxiv.org/html/2406.01179v2"},{"title":"A Practical Examination of AI-Generated Text Detectors for Large Language Models","url":"https://arxiv.org/html/2412.05139v4"},{"title":"Robust AI-Generated Text Detection by Restricted Embeddings","url":"https://arxiv.org/html/2410.08113v1"}]

I found the paper you're looking for. Here's what I found about arXiv:2604.13692:

## Paper Overview

The paper is titled "Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection" and was submitted on April 15, 2026. The authors are Xiao Pu, Zepeng Cheng, Lin Yuan, Yu Wu, and Xiuli Bi from Chongqing University of Posts and Telecommunications, China.

## Problem Statement

The paper addresses the challenge that as large language models generate text increasingly resembling human writing, it becomes difficult to capture the subtle cues distinguishing AI-generated content from human-written text. Reliance on generator-specific artifacts is inherently unstable, since new models emerge rapidly and reduce the robustness of such shortcuts.

## Proposed Solution

To tackle this challenge, the authors propose a progressively structured framework that disentangles AI-detection semantics from generator-aware artifacts. This is achieved through a compact latent encoding that encourages semantic minimality, followed by perturbation-based regularization to reduce residual entanglement, and finally a discriminative adaptation stage that aligns representations with task objectives.

The paper is available on arXiv at https://arxiv.org/abs/2604.13692.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecc34ff6-d840-4758-bd43-9dfa4d0eecca",
  "isSidechain": true,
  "promptId": "5d54a633-ce2f-442c-b92b-456437643336",
  "agentId": "a3fc236c170c1507c",
  "type": "user",
  "uuid": "2f68dd68-86a3-43c5-bdea-080204611aa4",
  "sourceToolAssistantUUID": "ecc34ff6-d840-4758-bd43-9dfa4d0eecca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T01:17:12.738Z_

<details><summary>↩ Tool result · `toolu_018EEZcBu1ay6e3egQYipiJZ`</summary>

```text
Web search results for query: ""Diversity Boosts AI-Generated Text Detection" Basani Chen TMLR 2026"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"},{"title":"Under review as submission to TMLR Diversity Boosts AI-Generated Text Detection","url":"https://openreview.net/pdf?id=WscAU9It1l"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"}]

I found the paper! Here are the key findings from the search results:

## Paper Overview

The paper "Diversity Boosts AI-Generated Text Detection" by Advik Raj Basani and Pin-Yu Chen was accepted at TMLR '26.

## Main Contribution

The authors propose DivEye, a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-based features. Human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs, which DivEye captures through interpretable statistical features.

## Key Results

The method outperforms existing zero-shot detectors by up to 33.2% and achieves competitive performance with fine-tuned baselines across multiple benchmarks. Additionally, when integrated into existing detectors as an auxiliary signal, this fusion significantly boosts performance, particularly on adversarial and out-of-distribution examples, without requiring retraining or modification of the original model.

## Motivation

Detecting AI-generated text is necessary to combat misuse of LLMs in education, business compliance, journalism, and social media. Prior detectors often rely on token-level likelihoods or opaque black-box classifiers, but these approaches struggle against high-quality generations and offer little interpretability.

The paper also has an official implementation available on GitHub and includes an online demo for testing the DivEye detector.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f62eabf-7430-41d0-b76b-2ba09235812b",
  "isSidechain": true,
  "promptId": "5d54a633-ce2f-442c-b92b-456437643336",
  "agentId": "a3fc236c170c1507c",
  "type": "user",
  "uuid": "2704fc73-e70f-4b72-89c9-1d16569622f4",
  "sourceToolAssistantUUID": "9f62eabf-7430-41d0-b76b-2ba09235812b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T01:17:13.750Z_

<details><summary>↩ Tool result · `toolu_01T2Atf2qgisdXSd1wWXLaKK`</summary>

```text
Web search results for query: "arXiv:2603.11228 "Markovian Generation Chains" Large Language Models Geng 2026"

Links: [{"title":"[2603.11228] Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/abs/2603.11228"},{"title":"Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/html/2603.11228"},{"title":"Markovian Generation Chains in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nTDn4OMiym"},{"title":"Large Language Models as Markov Chains","url":"https://arxiv.org/html/2410.02724v1"},{"title":"Markovian ODE-guided scoring can assess the quality of offline reasoning traces in language models","url":"https://arxiv.org/html/2603.01580"},{"title":"LARGE LANGUAGE MODELS AS MARKOV CHAINS","url":"https://openreview.net/pdf/f35700e63361517cc78796117093918493fb8e92.pdf"},{"title":"Beyond Via: Analysis and Estimation of the Impact of Large Language Models in Academic Papers","url":"https://arxiv.org/html/2603.25638v2"},{"title":"[2603.01580] Markovian ODE-guided scoring can assess the quality of offline reasoning traces in language models","url":"https://arxiv.org/abs/2603.01580"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.02724v2"},{"title":"[2410.02724] Large Language Models as Markov Chains","url":"https://arxiv.org/abs/2410.02724"}]

I found the paper you're looking for! Here's the information about arXiv:2603.11228:

**Paper Title:** Markovian Generation Chains in Large Language Models

**Authors and Details:** The paper is authored by Mingmeng Geng from ENS-PSL & CNRS-Lattice, along with Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, and Thierry Poibeau, and was posted on March 11, 2026.

**Core Concept:** The paper defines an iterative inference process as Markovian generation chains, where each step takes a specific prompt template and the previous output as input, without including any prior memory.

**Research Focus:** The paper investigates how texts evolve when they are repeatedly processed by LLMs. In iterative rephrasing and round-trip translation experiments, the output either converges to a small recurrent set or continues to produce novel sentences over a finite horizon.

**Key Findings:** Through sentence-level Markov chain modeling and analysis of simulated data, the researchers show that the iterative process can either increase or reduce sentence diversity depending on factors such as the temperature parameter.

The paper appears to be under review at conferences and is also available on OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e9d27f2-a349-494c-9e03-9cbc8c8c4e55",
  "isSidechain": true,
  "promptId": "5d54a633-ce2f-442c-b92b-456437643336",
  "agentId": "a3fc236c170c1507c",
  "type": "user",
  "uuid": "30bad70f-4117-471b-b2eb-43958fc43a23",
  "sourceToolAssistantUUID": "2e9d27f2-a349-494c-9e03-9cbc8c8c4e55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T01:17:14.498Z_

<details><summary>↩ Tool result · `toolu_01E81vMGsAFr4bg8PnPjV75z`</summary>

```text
Web search results for query: "arXiv:2605.01647 "Beyond Perplexity" MDTA Benchmark AI Text Detection"

Links: [{"title":"[2605.01647v1] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647v1"},{"title":"[2605.01647] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/html/2605.01647v1"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260501647N/abstract"},{"title":"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy","url":"https://arxiv.org/html/2603.23146v2"},{"title":"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/html/2605.03969"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Detecting AI-Generated Text: Factors Influencing Detectability with Current Methods","url":"https://arxiv.org/html/2406.15583v1"},{"title":"MELD: Multi-Task Equilibrated Learning Detector for AI-Generated Text","url":"https://arxiv.org/html/2605.06903"},{"title":"[2605.03969] Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/abs/2605.03969"}]

I found the paper you're looking for! Here's a summary of the research:

## Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection

**arXiv:2605.01647** is a paper by Priyadarshan Narayanasamy, Swastik Agrawal, Klint Faber, and Fardina Fathmiul Alam from the University of Maryland.

### Key Contributions:

**Problem:** Training-free AI text detection methods primarily rely on model log-probabilities, achieving strong performance through approaches like Binoculars and DNA-DetectLLM. However, these methods face a fundamental ceiling as models are optimized through RLHF to produce human-like probability distributions.

**Solution:** The authors introduce an alternative detection signal based on character distribution signatures, providing theoretical foundations showing that AI models, trained on massive domain-balanced corpora, approximate global character patterns while humans exhibit domain-specialized distributions, creating a "Wall of Separation" where human-AI divergence significantly exceeds AI-AI divergence.

**The MDTA Benchmark:** The Models-Domains-Temperatures-Adversarials (MDTA) benchmark comprises 642,274 prompt-aligned samples across 4 models, 5 domains, 3 temperature settings, and 3 adversarial strategies, substantially expanding the HC3 dataset with modern model responses, temperature variation, and adversarial augmentation.

**Results:** The Letter Distribution Score (LD-Score) demonstrates low correlation (r = 0.08-0.13) with perplexity methods. When integrated with DNA-DetectLLM, Binoculars and FastDetectGPT via a non-linear classifier, LD-Score yields consistent improvements in AUROC and F1, with particularly pronounced gains in specialized domains where vocabulary constraints amplify the detection signal.

The MDTA dataset can be accessed at: https://huggingface.co/datasets/nsp909/MDTA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db2c98e7-b43d-4ec9-a42d-218380496c69",
  "isSidechain": true,
  "promptId": "5d54a633-ce2f-442c-b92b-456437643336",
  "agentId": "a3fc236c170c1507c",
  "type": "user",
  "uuid": "023af1d1-7cf8-4454-bca1-d0578e4ac262",
  "sourceToolAssistantUUID": "db2c98e7-b43d-4ec9-a42d-218380496c69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T01:17:14.794Z_

<details><summary>↩ Tool result · `toolu_01U4NVUePmMqWzTqhpAsADR4`</summary>

```text
Web search results for query: "arXiv:2605.03969 "Feature-Augmented Transformers" AI-Text Detection Domains Generators Mady"

Links: [{"title":"[2605.03969] Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/abs/2605.03969"},{"title":"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/html/2605.03969"},{"title":"Modeling the Attack: Detecting AI-Generated Text by Quantifying Adversarial Perturbations","url":"https://arxiv.org/html/2510.02319v1"},{"title":"Adaptive Ensembles of Fine-Tuned Transformers for LLM-Generated Text Detection","url":"https://arxiv.org/html/2403.13335v1"},{"title":"Arxiv","url":"https://www.arxiv.org/pdf/2509.20375"},{"title":"Fine-Grained Detection of AI-Generated Text Using Sentence-Level Segmentation","url":"https://arxiv.org/html/2509.17830"},{"title":"[2509.20375] Assessing Classical Machine Learning and Transformer-based Approaches for Detecting AI-Generated Research Text","url":"https://arxiv.org/abs/2509.20375"},{"title":"Aggregated Text Transformer for Scene Text Detection","url":"https://arxiv.org/html/2211.13984"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/html/2605.01647"},{"title":"[2601.03812] AI Generated Text Detection","url":"https://arxiv.org/abs/2601.03812"}]

I found the paper you're looking for! Here's the information about arXiv:2605.03969:

## Paper Summary

The paper is titled "Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators", and the authors are Mohamed Mady, Johannes Reschke, and Björn Schuller.

### Main Research Problem

AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors.

### Methodology

The researchers train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift.

### Evaluation and Results

They evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with their best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e747e3c-bfc9-4d74-80a2-f9333db0249d",
  "isSidechain": true,
  "promptId": "5d54a633-ce2f-442c-b92b-456437643336",
  "agentId": "a3fc236c170c1507c",
  "type": "user",
  "uuid": "eb434200-b5d5-4594-96c1-4bc249a83f2a",
  "sourceToolAssistantUUID": "7e747e3c-bfc9-4d74-80a2-f9333db0249d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T01:17:15.810Z_

<details><summary>↩ Tool result · `toolu_012VG7LhPnr5bTWunrRn6nn8`</summary>

```text
Web search results for query: "arXiv:2605.05503 "Chainwash" Rewriting Attacks Diffusion Language Model Watermarks Ameen"

Links: [{"title":"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/html/2605.05503"},{"title":"[2605.05503] Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/abs/2605.05503"},{"title":"Character-Level Perturbations Disrupt LLM Watermarks","url":"https://arxiv.org/html/2509.09112v1"},{"title":"Watermarking Diffusion Language Models","url":"https://arxiv.org/html/2509.24368v1"},{"title":"LLM Watermark Evasion via Bias Inversion","url":"https://arxiv.org/html/2509.23019v1"},{"title":"WaterPark: A Robustness Assessment of Language Model Watermarking","url":"https://arxiv.org/html/2411.13425v1"},{"title":"Breaking Distortion-free Watermarks in Large Language Models","url":"https://arxiv.org/html/2502.18608v2"},{"title":"[2509.24368] Watermarking Diffusion Language Models","url":"https://arxiv.org/abs/2509.24368"},{"title":"Publicly-Detectable Watermarking for Language Models","url":"https://eprint.iacr.org/2023/1661.pdf"},{"title":"(PDF) Watermarking Diffusion Language Models","url":"https://www.researchgate.net/publication/395969737_Watermarking_Diffusion_Language_Models"}]

Based on the search results, I found the paper you're looking for:

## Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks

The paper is authored by Mohd Ruhul Ameen, Akif Islam, Nadim Mahmud, and Md. Ekramul Hamid, from Marshall University, University of Rajshahi, and Miami University.

**Key Overview:**

Statistical watermarking is the leading approach for verifying whether text was written by a language model. Diffusion language models generate text by denoising tokens in arbitrary order, and a recent watermark by Gloaguen et al. (ICLR 2026) addresses this gap and reports true positive detection above 99% on LLaDA-8B-Instruct outputs.

**Study Design:**

The paper studies what happens when watermarked text is rewritten multiple times, with 1,605 watermarked completions of about 300 tokens each produced across five WaterBench domains, then rewritten by four open-weight language models from 1.5B to 8B parameters. Five rewrite styles are tested: paraphrase, humanize, simplify, academic, and summarize-expand, with every style chained for up to five hops, producing 160,500 rewritten texts in total.

**Main Findings:**

Across all four rewriters and five rewrite styles, repeated rewriting substantially reduces detectability while semantic content is largely preserved. This process is referred to as chainwash: the watermark signal is washed out through a chain of model-mediated rewrites.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45e19728-32cc-42ce-8a54-0f4ea5900290",
  "isSidechain": true,
  "promptId": "5d54a633-ce2f-442c-b92b-456437643336",
  "agentId": "a3fc236c170c1507c",
  "type": "user",
  "uuid": "341250b5-d3f2-4637-84b0-1427994f8363",
  "sourceToolAssistantUUID": "45e19728-32cc-42ce-8a54-0f4ea5900290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-16T01:17:18.999Z_

Now I need to check the TMLR status for `diveye` more carefully — the search showed both TMLR acceptance and an ICML 2025 listing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "341250b5-d3f2-4637-84b0-1427994f8363",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
  "requestId": "req_011Cb5N9VjKHDVVHpbTFqfa7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b95736db-3ef0-40d7-a326-c103a0bf2ddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019buXTwUE5R5ra52Piv3Pa2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5587,
      "cache_read_input_tokens": 16702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5587,
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

_source line 19 · 2026-05-16T01:17:19.430Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QWm9iuJHhNWFsd1ajL8kvy`</summary>

```json
{
  "query": "\"Diversity Boosts AI-Generated Text Detection\" TMLR accepted OpenReview 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b95736db-3ef0-40d7-a326-c103a0bf2ddb",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
  "requestId": "req_011Cb5N9VjKHDVVHpbTFqfa7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "973930f7-1b4a-4b18-9c41-f96c6dd00ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019buXTwUE5R5ra52Piv3Pa2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5587,
      "cache_read_input_tokens": 16702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5587,
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

_source line 20 · 2026-05-16T01:17:26.636Z_

<details><summary>↩ Tool result · `toolu_01QWm9iuJHhNWFsd1ajL8kvy`</summary>

```text
Web search results for query: ""Diversity Boosts AI-Generated Text Detection" TMLR accepted OpenReview 2025 2026"

Links: [{"title":"Under review as submission to TMLR Diversity Boosts AI-Generated Text Detection","url":"https://openreview.net/pdf?id=WscAU9It1l"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"DIVERSITY BOOSTS AI-GENERATED TEXT DETECTION","url":"https://openreview.net/pdf/bea66b54008baeb2d59557b78604c3a155e3c7ae.pdf"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=12550&show=25"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.researchgate.net/publication/395771470_Diversity_Boosts_AI-Generated_Text_Detection"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=3550&show=50"}]

Based on the search results, I found comprehensive information about this paper:

## "Diversity Boosts AI-Generated Text Detection"

This paper has been accepted to Transactions on Machine Learning Research (TMLR '26). It was authored by Advik Raj Basani and Pin-Yu Chen.

### Overview

The paper proposes DivEye, a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-based features, motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs.

### Key Results

The method outperforms existing zero-shot detectors by up to 33.2% and achieves competitive performance with fine-tuned baselines across multiple benchmarks. DivEye is robust to paraphrasing and adversarial attacks, generalizes well across domains and models, and improves the performance of existing detectors by up to 18.7% when used as an auxiliary signal.

### Methodology

Instead of analyzing individual token probabilities in isolation, the work measures statistical diversity over token sequences, quantifying how text fluctuates in its use of surprising or predictable tokens, providing a more global signature of the generative process that is robust to paraphrasing, domain shifts, and even partial text corruption.

### Availability

The code is available as an official implementation with a project page for demos and examples.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "973930f7-1b4a-4b18-9c41-f96c6dd00ad9",
  "isSidechain": true,
  "promptId": "5d54a633-ce2f-442c-b92b-456437643336",
  "agentId": "a3fc236c170c1507c",
  "type": "user",
  "uuid": "a365e798-63bb-41ab-afa6-33dc4e332a88",
  "sourceToolAssistantUUID": "973930f7-1b4a-4b18-9c41-f96c6dd00ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T01:17:46.598Z_

Here are the verification results for all 6 papers:

---

**1. `ld_score` — "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection"**
- **EXISTS**: Yes — confirmed at https://arxiv.org/abs/2605.01647
- **YEAR_CORRECT**: Yes (submitted May 2026)
- **NEEDS_UPDATE**: No — remains arXiv preprint, no venue publication found
- **NOTES**: Authors are Narayanasamy, Agrawal, Faber, Alam (UMaryland). Title, arXiv ID, and year all match.

---

**2. `diveye` — "Diversity Boosts AI-Generated Text Detection"**
- **EXISTS**: Yes — confirmed at https://arxiv.org/abs/2509.18880 and OpenReview
- **YEAR_CORRECT**: Yes (TMLR '26 accepted)
- **NEEDS_UPDATE**: Minor — the arXiv preprint ID is **2509.18880** (September 2025), not a 2026 arXiv ID. The TMLR acceptance year is 2026. The bib entry should cite the TMLR version; the venue "TMLR, 2026" is correct per GitHub repo `[TMLR '26]`.
- **NOTES**: Also appeared at ICML 2025 as a workshop/shared task entry (PAN 2025). The main TMLR paper is the correct citation. Authors Basani and Chen confirmed.

---

**3. `generator_barrier` — "Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection"**
- **EXISTS**: Yes — confirmed at https://arxiv.org/abs/2604.13692
- **YEAR_CORRECT**: Yes (April 2026)
- **NEEDS_UPDATE**: No — remains arXiv preprint
- **NOTES**: Authors are Pu, Cheng, Yuan, Wu, Bi (Chongqing University of Posts and Telecommunications). Title, ID, year, and author surname all match.

---

**4. `feat_aug_transformer` — "Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators"**
- **EXISTS**: Yes — confirmed at https://arxiv.org/abs/2605.03969
- **YEAR_CORRECT**: Yes (May 2026)
- **NEEDS_UPDATE**: No — remains arXiv preprint
- **NOTES**: Authors are Mady, Reschke, Schuller. Title, ID, and year match.

---

**5. `markovian_chains` — "Markovian Generation Chains in Large Language Models"**
- **EXISTS**: Yes — confirmed at https://arxiv.org/abs/2603.11228 and OpenReview
- **YEAR_CORRECT**: Yes (March 2026)
- **NEEDS_UPDATE**: Possible — paper is on OpenReview (https://openreview.net/forum?id=nTDn4OMiym), suggesting it may be under review at a venue. No confirmed acceptance found yet.
- **NOTES**: Authors are Geng, Mohamed, Shang, Vazirgiannis, Poibeau (ENS-PSL / CNRS). Title, ID, and year match.

---

**6. `chainwash` — "Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks"**
- **EXISTS**: Yes — confirmed at https://arxiv.org/abs/2605.05503
- **YEAR_CORRECT**: Yes (May 2026)
- **NEEDS_UPDATE**: No — remains arXiv preprint
- **NOTES**: Authors are Ameen, Islam, Mahmud, Hamid (Marshall University / University of Rajshahi / Miami University). Title, ID, and year match.

---

**Summary of action items:**
- `diveye`: The arXiv preprint date is September 2025 — if your bib currently cites a 2026 arXiv ID, that's wrong; the correct arXiv ID is 2509.18880. The TMLR venue and year 2026 are correct.
- `markovian_chains`: Monitor for formal acceptance — it's on OpenReview and may get a venue update.
- All other 4 entries: no corrections needed.

Sources:
- [arXiv:2605.01647](https://arxiv.org/abs/2605.01647)
- [arXiv:2509.18880 (diveye)](https://arxiv.org/abs/2509.18880)
- [GitHub IBM/diveye — TMLR '26](https://github.com/IBM/diveye)
- [OpenReview diveye](https://openreview.net/forum?id=DNgsOhGZBI)
- [arXiv:2604.13692](https://arxiv.org/abs/2604.13692)
- [arXiv:2605.03969](https://arxiv.org/abs/2605.03969)
- [arXiv:2603.11228](https://arxiv.org/abs/2603.11228)
- [OpenReview markovian_chains](https://openreview.net/forum?id=nTDn4OMiym)
- [arXiv:2605.05503](https://arxiv.org/abs/2605.05503)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a365e798-63bb-41ab-afa6-33dc4e332a88",
  "isSidechain": true,
  "agentId": "a3fc236c170c1507c",
  "requestId": "req_011Cb5NAHyuhNWS2FizFr6pr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be6a1b9c-060d-4b47-b5bf-27b73494f0e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "c812adcb-41ff-44b3-9e50-ba4cebc5264c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Qdx7sGqaugQb7H4ydWA8Dv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 22289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1049,
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
