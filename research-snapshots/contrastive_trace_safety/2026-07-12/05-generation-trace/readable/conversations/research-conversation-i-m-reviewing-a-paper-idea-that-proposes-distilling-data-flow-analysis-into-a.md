# Research conversation: I'm reviewing a paper idea that proposes "distilling data-flow analysis into a neural context selector" for code repair.

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa38f008d49a94408.jsonl`
- **Structured JSON:** [`71b0f80dd73c88d40ca0.json`](../../sessions/71/71b0f80dd73c88d40ca0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

58 recorded events

### User

_source line 1 · 2026-05-10T17:50:51.151Z_

I'm reviewing a paper idea that proposes "distilling data-flow analysis into a neural context selector" for code repair. I've found several competing works and need to understand how close they are:

1. **REPOFILTER** (OpenReview 2025) - trains LLMs to evaluate polarity of retrieved code chunks. Search for more details about this paper - does it use static analysis signals for training? How does it compare to this idea of distilling data-flow analysis?

2. **SWE-Pruner** (arXiv:2601.16746, Jan 2026) - self-adaptive context pruning for coding agents. Search for details on this paper. Does it learn to select context in a way similar to distilling static analysis?

3. **RepoRepair** (arXiv:2603.01048, March 2026) - hierarchical documentation for code repair. Does it achieve strong localization and could subsume the proposed idea?

4. Search specifically for "distill program analysis neural" OR "learn data flow analysis" OR "neural program slicing" to find if anyone has already proposed distilling data-flow into a neural model.

5. Search for "knowledge distillation code repair 2025 2026" to find any competing distillation approaches.

6. Check if there's recent work combining tree-sitter based analysis with neural models for context selection.

Use WebSearch with multiple queries and WebFetch for the most relevant results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "e00684ca-1a26-4a00-a4ba-af783d7d235f",
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

_source line 2 · 2026-05-10T17:50:51.154Z_

```json
{
  "parentUuid": "e00684ca-1a26-4a00-a4ba-af783d7d235f",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
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
  "uuid": "b631a3ac-1839-4127-b2ed-a17660cd5a33",
  "timestamp": "2026-05-10T17:50:51.154Z",
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

_source line 3 · 2026-05-10T17:50:53.940Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RRpCEW2E485XFBU38i3ui2`</summary>

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
  "parentUuid": "b631a3ac-1839-4127-b2ed-a17660cd5a33",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK4WGHYy1LPCKAefcM7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "493c768b-f7b5-42d6-aac9-d26d5d8af229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Pd1XQth3dUYW3D8Un3Dsf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 8223,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 869
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 869,
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

_source line 4 · 2026-05-10T17:50:53.943Z_

<details><summary>↩ Tool result · `toolu_01RRpCEW2E485XFBU38i3ui2`</summary>

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
  "parentUuid": "493c768b-f7b5-42d6-aac9-d26d5d8af229",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "c0e41d9c-c39f-41b1-8b16-5cc290f07d96",
  "sourceToolAssistantUUID": "493c768b-f7b5-42d6-aac9-d26d5d8af229",
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

_source line 5 · 2026-05-10T17:50:57.894Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JvmFcjNXjtLRY8Bos9M96K`</summary>

```json
{
  "query": "REPOFILTER OpenReview 2025 LLM evaluate polarity retrieved code chunks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0e41d9c-c39f-41b1-8b16-5cc290f07d96",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK4iQHYSEJ2U3cKyttA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b93be6d-2939-4d24-b2e9-86cf45ea3d59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HcTsB8XXFkzL4CS2tGTDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T17:50:58.224Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AWWR16HrHsBFQ7AfGQqnuD`</summary>

```json
{
  "query": "SWE-Pruner arXiv 2601.16746 self-adaptive context pruning coding agents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b93be6d-2939-4d24-b2e9-86cf45ea3d59",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK4iQHYSEJ2U3cKyttA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0343b092-43e4-4f69-ac2b-ef2d0b116aa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HcTsB8XXFkzL4CS2tGTDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T17:50:58.701Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HtBt97nTR8naBKkVs5ZXTG`</summary>

```json
{
  "query": "RepoRepair arXiv 2603.01048 hierarchical documentation code repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0343b092-43e4-4f69-ac2b-ef2d0b116aa8",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK4iQHYSEJ2U3cKyttA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0abb5c7-a621-4d97-853c-80f5ad4cd558",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HcTsB8XXFkzL4CS2tGTDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T17:50:59.166Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q8NgkA3frSsSokNxvJ2C4j`</summary>

```json
{
  "query": "\"distill program analysis neural\" OR \"learn data flow analysis\" OR \"neural program slicing\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0abb5c7-a621-4d97-853c-80f5ad4cd558",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK4iQHYSEJ2U3cKyttA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ef54ffd-5e09-44bc-998f-dd62edbd7689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HcTsB8XXFkzL4CS2tGTDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T17:50:59.636Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AjTPihxybxGkz5g3naQXr2`</summary>

```json
{
  "query": "\"knowledge distillation\" \"code repair\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ef54ffd-5e09-44bc-998f-dd62edbd7689",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK4iQHYSEJ2U3cKyttA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bd68e1d-a4d3-49c7-9c65-28246882c8c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HcTsB8XXFkzL4CS2tGTDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T17:50:59.886Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F81JPMqJJGCkcY18SXX7TV`</summary>

```json
{
  "query": "tree-sitter neural context selection code repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bd68e1d-a4d3-49c7-9c65-28246882c8c3",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK4iQHYSEJ2U3cKyttA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c23f9b1f-d654-472b-bd72-be99c687adec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HcTsB8XXFkzL4CS2tGTDF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9092,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 339,
          "cache_read_input_tokens": 9092,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1888,
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

_source line 11 · 2026-05-10T17:51:04.587Z_

<details><summary>↩ Tool result · `toolu_01JvmFcjNXjtLRY8Bos9M96K`</summary>

```text
Web search results for query: "REPOFILTER OpenReview 2025 LLM evaluate polarity retrieved code chunks"

Links: [{"title":"Impact-driven Context Filtering For Cross-file Code ...","url":"https://www.arxiv.org/pdf/2508.05970"},{"title":"Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions","url":"https://openreview.net/pdf?id=ZgQ0t3zYTQ"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/b0c7546e92d381f99b83a0e93623e007c1088f4e.pdf"},{"title":"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems | OpenReview","url":"https://openreview.net/forum?id=pPjZIOuQuF"},{"title":"Position: Future Research and Challenges Remain Towards AI for Software","url":"https://openreview.net/pdf?id=RuLsq4LSZK"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=20JDhbJqn3"},{"title":"MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent | OpenReview","url":"https://openreview.net/forum?id=k5nIOvYGCL"},{"title":"The LLM Data Auditor: A Metric-oriented Survey on Quality ...","url":"https://openreview.net/pdf/c6bbc67ac84a995a4e59e64321913631d7328945.pdf"},{"title":"CodeRAG: Finding Relevant and Necessary Knowledge ...","url":"https://aclanthology.org/2025.emnlp-main.1187.pdf"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | OpenReview","url":"https://openreview.net/forum?id=dw9VUsSHGB"}]

Based on the web search results, I found relevant information about a paper that matches your query. The most relevant result is from arxiv.org:

## CODEFILTER: Repository-Level Code Completion Framework

The paper introduces CODEFILTER, a repository-level code completion framework designed to selectively retrieve and incrementally add code chunks and filter out irrelevant chunks for improved precision and interpretability.

### Polarity-Based Evaluation System

The framework includes polarity tokens (&lt;pos>, &lt;neg>, &lt;neu>), which mark a chunk's positive, negative, or neutral impact. During generation, the model learns to autonomously produce these tokens, allowing it to manage retrieval and filtering at each step.

### Methodology for Evaluating Retrieved Code Chunks

The researchers retrieved the top 10 cross-file code chunks using Jaccard Similarity and labeled the polarity of each chunk based on the likelihood-based metric. A retrieved code chunk that contains critical information for the current completion will significantly increase the LLM's likelihood over the ground truth.

The dataset construction involved retrieving the top 10 cross-file code chunks using Jaccard Similarity and labeling the polarity of each chunk based on the likelihood-based metric.

The paper appears to be available on arxiv.org (arxiv:2508.05970) and presents an innovative approach to filtering and evaluating retrieved code chunks using polarity-based metrics for repository-level code completion tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b93be6d-2939-4d24-b2e9-86cf45ea3d59",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "4bcb4892-90b6-4faa-920e-114e57f2ad59",
  "sourceToolAssistantUUID": "4b93be6d-2939-4d24-b2e9-86cf45ea3d59",
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

_source line 12 · 2026-05-10T17:51:04.899Z_

<details><summary>↩ Tool result · `toolu_01HtBt97nTR8naBKkVs5ZXTG`</summary>

```text
Web search results for query: "RepoRepair arXiv 2603.01048 hierarchical documentation code repair"

Links: [{"title":"[2603.01048] RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/abs/2603.01048"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/html/2603.01048"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair | Gist.Science","url":"https://gist.science/paper/2603.01048"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.01048"},{"title":"(PDF) RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://www.researchgate.net/publication/401470565_RepoRepair_Leveraging_Code_Documentation_for_Repository-Level_Automated_Program_Repair"},{"title":"RepoRepair: Leveraging Code Documentation for ...","url":"https://arxiv.org/pdf/2603.01048"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"Bug Fixing with Broader Context: Enhancing LLM-Based Program Repair via Layered Knowledge Injection","url":"https://arxiv.org/html/2506.24015v1"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"AutoCodeRover: Autonomous Program Improvement | Request PDF","url":"https://www.researchgate.net/publication/383959416_AutoCodeRover_Autonomous_Program_Improvement"}]

Based on the search results, here's what I found about RepoRepair (arXiv 2603.01048):

## Overview

RepoRepair is a novel documentation-enhanced approach for repository-level fault localization and program repair. The paper was submitted on March 1, 2026.

## Core Approach

The core insight is to leverage LLMs to generate hierarchical code documentation (from functions to files) for code repositories, creating structured semantic abstractions that enable LLMs to comprehend repository-level context and dependencies. RepoRepair first employs a text-based LLM (e.g., DeepSeek-V3) to generate file/function-level code documentation for repositories, which serves as auxiliary knowledge to guide fault localization.

## Two-Stage Operation

RepoRepair operates in two stages: (1) In the localization stage, the hierarchical documentation is exclusively utilized to achieve precise fault localization; (2) In the repair stage, we introduce a novel, context-aware pipeline. This pipeline first prunes the localized code to construct a dependency-preserving repair context, then generates minimal diff-formatted patches, and finally validates them through an iterative, combinatorial testing strategy.

## Performance

Evaluated on SWE-bench Lite, RepoRepair achieves a 45.7% repair rate at a low cost of $0.44 per fix. On SWE-bench Multimodal, it delivers state-of-the-art performance with a 37.1% repair rate despite a higher cost of $0.56 per fix, demonstrating robust and cost-effective performance across diverse problem domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0abb5c7-a621-4d97-853c-80f5ad4cd558",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "c49b81bd-52a1-4faa-ad35-8ddaf4573afa",
  "sourceToolAssistantUUID": "f0abb5c7-a621-4d97-853c-80f5ad4cd558",
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

_source line 13 · 2026-05-10T17:51:05.220Z_

<details><summary>↩ Tool result · `toolu_01AWWR16HrHsBFQ7AfGQqnuD`</summary>

```text
Web search results for query: "SWE-Pruner arXiv 2601.16746 self-adaptive context pruning coding agents"

Links: [{"title":"[2601.16746] SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/abs/2601.16746"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/html/2601.16746v1"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"GitHub - Ayanami1314/swe-pruner · GitHub","url":"https://github.com/Ayanami1314/swe-pruner"},{"title":"(PDF) SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.researchgate.net/publication/400071923_SWE-Pruner_Self-Adaptive_Context_Pruning_for_Coding_Agents"},{"title":"Paper page - SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://huggingface.co/papers/2601.16746"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.16746"},{"title":"Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://arxiv.org/html/2604.04979"},{"title":"ayanami-kitasan/code-pruner · Hugging Face","url":"https://huggingface.co/ayanami-kitasan/code-pruner"},{"title":"Software Engineering on X: \"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents Yuhang Wang, Yuling Shi, Mo Yang, Rongrui Zhang, Shilin He, Heng Lian, Yuting Chen, Siyu Ye, Kai Cai, Xiaodong Gu https://t.co/7gw9yLhyMf [𝚌𝚜.𝚂𝙴 𝚌𝚜.𝙲𝙻] https://t.co/kRlOYQc5jb\" / X","url":"https://x.com/ComputerPapers/status/2015694356875727079"}]

## SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents

I found the arXiv paper you're looking for. Here are the key details:

**Paper Overview:**

LLM agents have demonstrated remarkable capabilities in software development, but their performance is hampered by long interaction contexts, which incur high API costs and latency. While various context compression approaches such as LongLLMLingua have emerged to tackle this challenge, they typically rely on fixed metrics such as PPL, ignoring the task-specific nature of code understanding, and frequently disrupt syntactic and logical structure and fail to retain critical implementation details.

**The Proposed Solution:**

SWE-Pruner is a self-adaptive context pruning framework tailored for coding agents. Drawing inspiration from how human programmers "selectively skim" source code during development and debugging, SWE-Pruner performs task-aware adaptive pruning for long contexts. Given the current task, the agent formulates an explicit goal (e.g., "focus on error handling") as a hint to guide the pruning targets.

**Performance:**

SWE-Pruner can save 20~40% of your Claude Code cost without sacrificing performance.

**Availability:**

The paper (arXiv:2601.16746) was submitted on January 23, 2026, with a revised version on February 4, 2026. The code is available on GitHub and also as a pip package, with a model available on Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0343b092-43e4-4f69-ac2b-ef2d0b116aa8",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "38f9599d-9c98-4a4e-a3ed-59054091ad3c",
  "sourceToolAssistantUUID": "0343b092-43e4-4f69-ac2b-ef2d0b116aa8",
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

_source line 14 · 2026-05-10T17:51:06.766Z_

<details><summary>↩ Tool result · `toolu_01AjTPihxybxGkz5g3naQXr2`</summary>

```text
Web search results for query: ""knowledge distillation" "code repair" 2025 2026"

Links: [{"title":"Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross–Language Code Clone Detection","url":"https://arxiv.org/html/2605.02860"},{"title":"An Empirical Study of Knowledge Distillation for Code Understanding Tasks","url":"https://arxiv.org/html/2508.15423v1"},{"title":"(PDF) An Empirical Study of Knowledge Distillation for Code Understanding Tasks","url":"https://www.researchgate.net/publication/394831258_An_Empirical_Study_of_Knowledge_Distillation_for_Code_Understanding_Tasks"},{"title":"Improving the Learning of Code Review Successive Tasks with Cross-Task Knowledge Distillation | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3643775"},{"title":"Reinforcement Learning via Self-Distillation","url":"https://arxiv.org/pdf/2601.20802"},{"title":"Knowledge Distillation for Large Language Models","url":"https://arxiv.org/html/2603.13765"},{"title":"Knowledge Distillation: Teacher-Student Loss Explained 2026 | Label Your Data","url":"https://labelyourdata.com/articles/machine-learning/knowledge-distillation"},{"title":"A Comprehensive Survey on Knowledge Distillation | OpenReview","url":"https://openreview.net/forum?id=3cbJzdR78B"},{"title":"[2508.15423] An Empirical Study of Knowledge Distillation for Code Understanding Tasks","url":"https://arxiv.org/abs/2508.15423"},{"title":"GitHub - modelscope/easydistill: a toolkit on knowledge distillation for large language models · GitHub","url":"https://github.com/modelscope/easydistill"}]

I found several relevant results about knowledge distillation and code-related tasks in 2025-2026. Here's what the research shows:

## Knowledge Distillation for Code Tasks (2025-2026)

Knowledge distillation has been studied for different code understanding tasks, including code generation, code classification, code summarization, code search, and code clone detection.

### Recent Research Findings

Knowledge distillation is a promising model compression and acceleration technique that addresses deployment challenges by transferring knowledge from large teacher models to compact student models, enabling efficient inference while preserving most of the teacher models' capabilities.

One notable 2025 study found that knowledge distillation exhibits a non-linear effectiveness curve across model sizes, with mid-sized architectures (7M-30M parameters) achieving optimal efficiency, and domain-specialized teacher models outperform general-purpose architectures in knowledge transfer effectiveness.

### Code Clone Detection with Distillation

Researchers developed a knowledge-distillation pipeline using DeepSeek-R1 as the teacher model and fine-tuned two compact student models, Phi-3-Mini and Qwen2.5-Coder-3B, for cross-language code clone detection.

### Code Review Applications

A deep-learning architecture named DISCOREV employs cross-task knowledge distillation to address code review tasks simultaneously.

However, I should note that while the search results show knowledge distillation being applied to various code understanding tasks, I didn't find specific research directly combining knowledge distillation with "code repair" as a unified task in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bd68e1d-a4d3-49c7-9c65-28246882c8c3",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "dca5ca22-077f-4f2e-b8dd-ad8cbc47d420",
  "sourceToolAssistantUUID": "3bd68e1d-a4d3-49c7-9c65-28246882c8c3",
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

_source line 15 · 2026-05-10T17:51:06.961Z_

<details><summary>↩ Tool result · `toolu_01F81JPMqJJGCkcY18SXX7TV`</summary>

```text
Web search results for query: "tree-sitter neural context selection code repair 2025 2026"

Links: [{"title":"Tree-sitter MCP Server by Joshua M. Dotson | PulseMCP","url":"https://www.pulsemcp.com/servers/wrale-tree-sitter"},{"title":"Tree-sitter: AI Code Analysis & Contextual Understanding","url":"https://mcpmarket.com/server/tree-sitter"},{"title":"Codebase-Memory: Tree-Sitter-Based Knowledge Graphs for LLM Code Exploration via MCP","url":"https://arxiv.org/html/2603.27277v1"},{"title":"How I cut AI context usage by 50x with a Tree-sitter code index - DEV Community","url":"https://dev.to/uwe_c_39d9ab7d16ff8dfe67e/how-i-cut-ai-context-usage-by-50x-with-a-tree-sitter-code-index-plm"},{"title":"tree-sitter-analyzer · PyPI","url":"https://pypi.org/project/tree-sitter-analyzer/"},{"title":"nvim-treesitter · GitHub","url":"https://github.com/nvim-treesitter"},{"title":"mcp-server-tree-sitter: The Ultimate Guide for AI Engineers","url":"https://skywork.ai/skypage/en/mcp-server-tree-sitter-The-Ultimate-Guide-for-AI-Engineers/1972133047164960768"},{"title":"CAST: Enhancing Code Retrieval-Augmented Generation","url":"https://www.cs.cmu.edu/~sherryw/assets/pubs/2025-cast.pdf"},{"title":"Show HN: CodeRLM – Tree-sitter-backed code indexing for LLM agents | Hacker News","url":"https://news.ycombinator.com/item?id=46974515"},{"title":"Building Real-Time Semantic Code Search With Tree-sitter and Vector Embeddings | by Cocoindex | Towards AI","url":"https://pub.towardsai.net/building-real-time-semantic-code-search-with-tree-sitter-and-vector-embeddings-b9b1fc0a94f3?gi=40a46de49d4f"}]

Based on the search results, here's what I found about tree-sitter, neural context selection, and code repair in 2025-2026:

## Recent Developments

Prometheus combined Tree-Sitter-based knowledge graphs with unified memory for multilingual issue resolution, representing one approach to structured code understanding. Additionally, SemanticForge employed dual static-dynamic knowledge graphs with neural graph query generation, and the Code Graph Model integrated graph representations directly into LLM attention mechanisms.

## Context Selection and AI Integration

Several tools have emerged to optimize context usage. AiDex is an MCP server that pre-indexes codebases using Tree-sitter and gives AI assistants instant access, reducing token usage from 2000+ tokens to approximately 50 tokens for code searches. 

Tree-Sitter-based knowledge graphs have been used for both multilingual issue resolution and structured code understanding, addressing the challenge of selecting relevant code context for AI models.

## Practical Impact

Within four weeks of release in February 2026, one Tree-sitter-based project accumulated more than 900 stars and is automatically detected by 10 coding agents including Claude Code, Codex CLI, and VS Code, indicating growing adoption in AI-assisted code repair and understanding tasks.

The search results show active development in combining tree-sitter's structural parsing with neural approaches for better code context selection, particularly in the context of AI agents performing code repair and analysis tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c23f9b1f-d654-472b-bd72-be99c687adec",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "bc800e2f-2c4d-47c5-a97f-f2c96ec15544",
  "sourceToolAssistantUUID": "c23f9b1f-d654-472b-bd72-be99c687adec",
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

_source line 16 · 2026-05-10T17:51:07.479Z_

<details><summary>↩ Tool result · `toolu_01Q8NgkA3frSsSokNxvJ2C4j`</summary>

```text
Web search results for query: ""distill program analysis neural" OR "learn data flow analysis" OR "neural program slicing""

Links: [{"title":"Regression Testing Based on Neural Networks and Program Slicing Techniques | Springer Nature Link","url":"https://link.springer.com/content/pdf/10.1007/978-3-642-25658-5_50.pdf"},{"title":"Distill — Latest articles about machine learning","url":"https://distill.pub/"},{"title":"PROGRAML: GRAPH-BASED DEEP LEARNING FOR PROGRAM OPTIMIZATION AND ANALYSIS","url":"https://arxiv.org/pdf/2003.10536"},{"title":"Neural Software Analysis – Communications of the ACM","url":"https://cacm.acm.org/research/neural-software-analysis/"},{"title":"Chapter 22 Graph Neural Networks in Program Analysis Miltiadis Allamanis","url":"https://graph-neural-networks.github.io/static/file/chapter22.pdf"},{"title":"Demystifying Knowledge Distillation in Neural Networks | by Dagang Wei | Medium","url":"https://medium.com/@weidagang/demystifying-knowledge-distillation-in-neural-networks-0f4c82c070ed"},{"title":"Towards a theory of model distillation","url":"https://arxiv.org/html/2403.09053v1"},{"title":"Distilling Knowledge in Neural Network | Towards Data Science","url":"https://towardsdatascience.com/distilling-knowledge-in-neural-network-d8991faa2cdc/"},{"title":"Data distillation: Preserving essence when distilling smart and synthetic data | by Aparana Gupta | Data Science + AI at Microsoft | Medium","url":"https://medium.com/data-science-at-microsoft/data-distillation-preserving-essence-when-distilling-smart-and-synthetic-data-979d0bfc6189"},{"title":"Dataset Distillation using Neural Feature Regression | OpenReview","url":"https://openreview.net/forum?id=2clwrA2tfik"}]

I've performed the web search with your query. Here are the key findings:

## Research on Neural Program Analysis and Related Topics

The search results cover several relevant areas:

### Neural Program Analysis
Neural software analysis is a new way of creating tools for software developers, complementing traditional program analysis, representing an alternative approach based on neural machine learning models that reason about software. Graph-based vector representations of code provide rich structural and semantic information available for code to the neural model.

### Program Representations for Neural Networks
Recent approaches make the program's control, data, and call dependencies a central part of the program's representation when processing code with neural networks. Graph Neural Networks (GNNs) have shown the ability to learn to replicate some of the algorithms used in common program analysis techniques.

### Knowledge Distillation in Neural Networks
While your query included "distill," the results also covered knowledge distillation as a separate concept. Knowledge distillation involves training a compact neural network using distilled knowledge from a large model or ensemble, where the large model or ensemble is called the "Teacher network" and the small model is called the "Student network."

### Program Slicing with Neural Networks
Program slices serve to indicate the relevance of test cases to regression testing, with Artificial Neural Networks used as underlying technology, where ANN learns the count of times that a program segment will be visited in execution of a test case.

The search results show active research at the intersection of neural networks and program analysis, particularly using graph-based representations of programs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ef54ffd-5e09-44bc-998f-dd62edbd7689",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "c96aa85b-e98a-4bb2-a3fa-9962fa2e731b",
  "sourceToolAssistantUUID": "6ef54ffd-5e09-44bc-998f-dd62edbd7689",
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

_source line 17 · 2026-05-10T17:51:11.418Z_

Now let me fetch more details on the most relevant papers to get deeper information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c96aa85b-e98a-4bb2-a3fa-9962fa2e731b",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK5i4ixnad1NL6QGm6P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1fcbfd0-7c5b-4345-abd8-26e03c14d68d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtN5hjxXHTu9zwwRCXSYLU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1790,
      "cache_creation_input_tokens": 4111,
      "cache_read_input_tokens": 10980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4111,
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

_source line 18 · 2026-05-10T17:51:13.924Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DMghjvTNps9zcV8uBqX1Eo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.16746",
  "prompt": "Extract the full abstract, methodology details, and key contributions of SWE-Pruner. Does it use static analysis or data-flow analysis? How does it learn to prune context - is it trained via distillation from a larger model? What signals does it use to decide what context to keep or remove?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1fcbfd0-7c5b-4345-abd8-26e03c14d68d",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK5i4ixnad1NL6QGm6P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d105a568-1092-4a3b-ad22-5bbf11424042",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtN5hjxXHTu9zwwRCXSYLU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1790,
      "cache_creation_input_tokens": 4111,
      "cache_read_input_tokens": 10980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4111,
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

_source line 19 · 2026-05-10T17:51:16.155Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Cpgp8eAvM8k9d6F1mJr1bv`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.01048",
  "prompt": "Extract the full methodology of RepoRepair. How does it do fault localization? Does it use static analysis, data-flow analysis, or dependency analysis? How does it construct the repair context? What is the \"dependency-preserving repair context\" mechanism? Could this approach subsume the idea of distilling data-flow analysis into a neural context selector?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d105a568-1092-4a3b-ad22-5bbf11424042",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK5i4ixnad1NL6QGm6P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16c18f7f-9f57-4af7-ab4b-690cd5a49e4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtN5hjxXHTu9zwwRCXSYLU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1790,
      "cache_creation_input_tokens": 4111,
      "cache_read_input_tokens": 10980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4111,
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

_source line 20 · 2026-05-10T17:51:19.631Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WMnFNUapBks4gB1Hcdg1Ua`</summary>

```json
{
  "url": "https://www.arxiv.org/pdf/2508.05970",
  "prompt": "Extract the full details of this paper (CODEFILTER or REPOFILTER). What is the methodology? Does it use static analysis signals for training? How does it evaluate polarity of retrieved code chunks? What is the training procedure - is it distillation-based? How does it compare to using data-flow analysis for context selection?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16c18f7f-9f57-4af7-ab4b-690cd5a49e4d",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK5i4ixnad1NL6QGm6P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26bb962f-8adf-4401-ba15-7c0d1f604fec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtN5hjxXHTu9zwwRCXSYLU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1790,
      "cache_creation_input_tokens": 4111,
      "cache_read_input_tokens": 10980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4111,
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

_source line 21 · 2026-05-10T17:51:20.283Z_

<details><summary>↩ Tool result · `toolu_01DMghjvTNps9zcV8uBqX1Eo`</summary>

```text
# SWE-Pruner: Analysis Based on Available Information

## Full Abstract
The paper addresses how LLM agents in software development suffer from lengthy interaction contexts, causing high API costs and latency. While existing compression methods like LongLLMLingua use fixed metrics (PPL), they ignore task-specific code understanding needs. SWE-Pruner tackles this through "task-aware adaptive pruning" inspired by how programmers selectively review source code. The system uses "a lightweight neural skimmer (0.6B parameters)" trained to dynamically select relevant lines based on explicit goals. Results show "23-54% token reduction on agent tasks like SWE-Bench Verified while even improving success rates, and up to 14.84x compression on single-turn tasks like LongCodeQA with minimal performance impact."

## Key Methodology Details
The framework operates through:
1. **Task-aware goal formulation**: The agent creates explicit objectives (e.g., "focus on error handling") to guide pruning
2. **Neural skimmer**: A lightweight model dynamically selects context lines based on the stated goal
3. **Evaluation scope**: Tested across four benchmarks and multiple models

## Analysis Type
The available content does **not specify** whether static analysis or data-flow analysis is employed. These technical implementation details remain undisclosed in this abstract-level description.

## Training Approach
The document does not clarify whether distillation from larger models is used or describe the neural skimmer's specific training methodology.

## Decision Signals
The pruning decisions rely on **task-specific goal hints** rather than fixed metrics, but precise signal mechanisms aren't detailed in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d105a568-1092-4a3b-ad22-5bbf11424042",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "805a1a7b-b09b-4d5f-9701-50c77768f4fd",
  "sourceToolAssistantUUID": "d105a568-1092-4a3b-ad22-5bbf11424042",
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

_source line 22 · 2026-05-10T17:51:20.681Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EBUuP56yTWbWz4iLQXWbRZ`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.27277v1",
  "prompt": "Extract details about this paper on Tree-Sitter-Based Knowledge Graphs for LLM Code Exploration. How does it combine tree-sitter with neural models? Does it use program analysis like data-flow or control-flow? How does it select context for code understanding tasks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "805a1a7b-b09b-4d5f-9701-50c77768f4fd",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK5i4ixnad1NL6QGm6P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55f7d463-9923-405a-8c61-e4a3c807f026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtN5hjxXHTu9zwwRCXSYLU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1790,
      "cache_creation_input_tokens": 4111,
      "cache_read_input_tokens": 10980,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4111
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1790,
          "output_tokens": 571,
          "cache_read_input_tokens": 10980,
          "cache_creation_input_tokens": 4111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4111,
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

_source line 23 · 2026-05-10T17:51:24.476Z_

<details><summary>↩ Tool result · `toolu_01Cpgp8eAvM8k9d6F1mJr1bv`</summary>

```text
# RepoRepair Methodology: Fault Localization and Repair Context

## Overall Approach

RepoRepair operates through three sequential stages: documentation generation, localization, and repair. The system is **not** static-analysis or data-flow driven. Instead, it leverages hierarchical code documentation generated by LLMs to guide fault identification.

## Fault Localization Mechanism

RepoRepair uses a three-tiered hierarchical localization strategy:

1. **File Retrieval**: Uses embedding-based semantic similarity to match issue descriptions against "file-level code documentation" rather than raw code. The system retrieves the top-50 most relevant files using sentence-transformers with FAISS indexing.

2. **File Localization**: Provides the LLM with file-level documentation and asks it to identify the most suspicious files. The paper states: *"We input these elements to the LLM using a prompt...that instructs it to generate comprehensive documentation"* containing file summaries and architectural roles.

3. **Function-Level Localization**: Uses function-level documentation to pinpoint specific classes or functions requiring modification within suspicious files.

Notably, this approach eschews traditional fault localization techniques (SBFL, static analysis, or dynamic analysis). Instead, it relies on LLM reasoning over semantic abstractions.

## Dependency-Preserving Repair Context

The repair context construction uses a selective pruning strategy:

RepoRepair "preserve[s] three categories of content: (i) all localized functions or classes identified as primary edit targets; (ii) essential file-level constructs such as import/require statements and global variable declarations; and (iii) any non-localized functions or classes that are statically referenced by the preserved repair targets."

This mechanism preserves **intra-file dependencies** through static reference analysis while aggressively removing unrelated code, prioritizing efficiency over transitive completeness.

## Could This Subsume Data-Flow Analysis?

Theoretically, yes—but with caveats. The approach could potentially absorb neural-based context selection by embedding data-flow summaries into documentation. However, the current system relies on LLM semantic understanding rather than explicit data-flow graphs, making it less precise for complex inter-procedural analyses. The trade-off favors scalability over analytical rigor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16c18f7f-9f57-4af7-ab4b-690cd5a49e4d",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "1d399ea4-32b6-4e93-9f27-466cbe60286a",
  "sourceToolAssistantUUID": "16c18f7f-9f57-4af7-ab4b-690cd5a49e4d",
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

_source line 24 · 2026-05-10T17:51:26.430Z_

<details><summary>↩ Tool result · `toolu_01WMnFNUapBks4gB1Hcdg1Ua`</summary>

```text
# Impact-Driven Context Filtering For Cross-File Code Completion

## Methodology Overview

This paper presents **CODEFILTER**, an impact-driven context filtering approach for cross-file code completion. The system addresses a key challenge: retrieving relevant code context from repositories while avoiding noisy or irrelevant snippets.

## Static Analysis Signals

The approach leverages static analysis to identify impactful code dependencies. Rather than retrieving all potentially related code, CODEFILTER uses "impact-driven" filtering that prioritizes code chunks based on their likelihood of influencing the completion target. The system analyzes relationships between files and functions to determine which context matters most.

## Polarity Evaluation

The paper evaluates retrieved code chunks through relevance assessment, measuring how strongly each chunk correlates with generating accurate completions. The filtering mechanism distinguishes between helpful context and distracting noise that degrades model performance.

## Training Procedure

The training follows a **distillation-based approach**. The method trains a lightweight context filter by learning from signals provided by larger models or oracle rankings. This allows efficient identification of high-impact code without requiring exhaustive retrieval.

## Comparison to Data-Flow Analysis

While data-flow analysis provides detailed tracking of variable and control dependencies, CODEFILTER's impact-driven approach offers a more practical alternative focused on "what matters for completion generation" rather than comprehensive dependency mapping. This pragmatic orientation yields better performance-to-cost tradeoffs in production settings.

[Binary content (application/pdf, 709.9KB) also saved to /home/ubuntu/.claude-account-3/projects/-/89242a75-96eb-4c62-bd61-c8808bbe5e16/tool-results/webfetch-1778435479853-kn7bn5.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26bb962f-8adf-4401-ba15-7c0d1f604fec",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "9ac7307b-e524-430c-97a8-fae7a6f256fb",
  "sourceToolAssistantUUID": "26bb962f-8adf-4401-ba15-7c0d1f604fec",
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

_source line 25 · 2026-05-10T17:51:26.869Z_

<details><summary>↩ Tool result · `toolu_01EBUuP56yTWbWz4iLQXWbRZ`</summary>

```text
# Codebase-Memory: Tree-Sitter Knowledge Graphs for LLM Code Exploration

## Tree-Sitter Integration (No Neural Models)

Codebase-Memory uses Tree-Sitter parsing but **does not integrate neural models**. The system constructs a static knowledge graph through syntactic analysis alone. As the paper states: "parses codebases using Tree-Sitter, stores the resulting graph in SQLite across 66 languages."

The approach is fundamentally structural rather than learned—it extracts code entities and relationships deterministically from abstract syntax trees.

## Program Analysis Approach

The system employs **limited static analysis**:

- **Call-graph construction** via 6-strategy name resolution (import maps, module qualification, fuzzy matching)
- **LSP-style type resolution** for Go, C, and C++ to improve accuracy with method receivers and pointer indirection
- **Louvain community detection** for modular structure discovery

However, it explicitly **does not** implement data-flow or control-flow analysis. The paper notes the system "captures static structure only; runtime behavior, reflection, and dynamic dispatch are not represented."

## Context Selection Strategy

Rather than learning-based selection, Codebase-Memory uses **pre-materialized graph queries**:

- Hub detection and caller ranking via breadth-first search
- Call-path tracing with configurable depth
- Architectural summary via community membership

The key advantage: "resolves structural queries via pre-computed graph lookups (breadth-first search via SQL recursive Common Table Expression: ∼0.3 ms)," avoiding the token overhead of iterative file exploration that traditional retrieval requires.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55f7d463-9923-405a-8c61-e4a3c807f026",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "d5e383d4-f15a-4400-abbc-c9e3e599cf4a",
  "sourceToolAssistantUUID": "55f7d463-9923-405a-8c61-e4a3c807f026",
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

_source line 26 · 2026-05-10T17:51:30.977Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QfcqXHDDsddCTyQnocG2N2`</summary>

```json
{
  "query": "PrograML \"learn data flow\" graph neural network program analysis distillation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5e383d4-f15a-4400-abbc-c9e3e599cf4a",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK78vUYrW7r8nCWTAe9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "129171fa-0625-47f0-867b-4a083029c679",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXWnjezgjcZ8962j7q8Bv3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4127,
      "cache_read_input_tokens": 15091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4127,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T17:51:31.585Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BL9vqYHvoUT57xKy99v3Gy`</summary>

```json
{
  "query": "\"neural program slicing\" learned slicing context 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "129171fa-0625-47f0-867b-4a083029c679",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK78vUYrW7r8nCWTAe9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9f40786-e75b-41c9-bd6b-0bf2b2a16993",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXWnjezgjcZ8962j7q8Bv3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4127,
      "cache_read_input_tokens": 15091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4127,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-10T17:51:32.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018z7ySYt5DUXfkRSSXmr6dJ`</summary>

```json
{
  "query": "CODEFILTER \"impact-driven context filtering\" cross-file code static analysis polarity training 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9f40786-e75b-41c9-bd6b-0bf2b2a16993",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK78vUYrW7r8nCWTAe9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cc78c6e-8aeb-4f55-8178-b91596b6468c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXWnjezgjcZ8962j7q8Bv3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4127,
      "cache_read_input_tokens": 15091,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4127
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 15091,
          "cache_creation_input_tokens": 4127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4127,
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

_source line 29 · 2026-05-10T17:51:38.367Z_

<details><summary>↩ Tool result · `toolu_01QfcqXHDDsddCTyQnocG2N2`</summary>

```text
Web search results for query: "PrograML "learn data flow" graph neural network program analysis distillation"

Links: [{"title":"PROGRAML: GRAPH-BASED DEEP LEARNING FOR PROGRAM OPTIMIZATION AND ANALYSIS","url":"https://arxiv.org/pdf/2003.10536"},{"title":"[PDF] ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProGraML:-A-Graph-based-Program-Representation-for-Cummins-Fisches/7843876d45f4c6ac751039b198aade0ee9f94342"},{"title":"[2003.10536] ProGraML: Graph-based Deep Learning for Program Optimization and Analysis","url":"https://arxiv.org/abs/2003.10536"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis","url":"http://proceedings.mlr.press/v139/cummins21a/cummins21a.pdf"},{"title":"A Lightweight Method for Graph Neural Networks Based on Knowledge Distillation and Graph Contrastive Learning","url":"https://www.mdpi.com/2076-3417/14/11/4805"},{"title":"[PDF] ProGraML: Graph-based Deep Learning for Program Optimization and Analysis | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProGraML:-Graph-based-Deep-Learning-for-Program-and-Cummins-Fisches/73e8fc4292ecbd271db9c4229c1cc9736b053760"},{"title":"Learning to Distill Graph Neural Networks | Proceedings of the Sixteenth ACM International Conference on Web Search and Data Mining","url":"https://dl.acm.org/doi/10.1145/3539597.3570480"},{"title":"Graph-less Neural Networks: Teaching Old MLPs New Tricks Via Distillation | OpenReview","url":"https://openreview.net/forum?id=4p6_5HBWPCw"},{"title":"A Gentle Introduction to Graph Neural Networks","url":"https://distill.pub/2021/gnn-intro/"},{"title":"Concept Distillation in Graph Neural Networks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-44070-0_12"}]

Based on the search results, I found comprehensive information about ProGraML and related research on graph neural networks for program analysis:

## ProGraML Overview

ProGraML is a program representation called "Program Graphs for Machine Learning" - a novel graph-based program representation using a low level, language agnostic, and portable format; and machine learning models capable of performing complex downstream tasks over these graphs.

## Program Representation

The ProGraML representation is a directed attributed multigraph that captures control, data, and call relations, and summarizes instruction and operand types and ordering. Message Passing Neural Networks propagate information through this structured representation, enabling whole-program or per-vertex classification tasks.

## Data Flow Analysis and Performance

ProGraML evaluates performance on a suite of traditional compiler analysis tasks including control flow reachability, dominator trees, data dependencies, variable liveness, and common subexpression detection. On a benchmark dataset of 250k LLVM-IR files covering six source programming languages, ProGraML achieves an average 94.0 F1 score, significantly outperforming the state-of-the-art approaches.

## Model Architecture

The system is formulated in a Message Passing Neural Network (MPNN) framework and the design mimics the transfer functions and meet operators of classical iterative dataflow analysis, replacing the rule-based implementations with deep learning analogues (message and update functions).

## Applications

ProGraML is applied to two high-level tasks — heterogeneous device mapping and program classification — setting new state-of-the-art performance in both.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "129171fa-0625-47f0-867b-4a083029c679",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "b59c4423-cc18-47a5-aeb9-ba67bbff0994",
  "sourceToolAssistantUUID": "129171fa-0625-47f0-867b-4a083029c679",
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

_source line 30 · 2026-05-10T17:51:38.595Z_

<details><summary>↩ Tool result · `toolu_01BL9vqYHvoUT57xKy99v3Gy`</summary>

```text
Web search results for query: ""neural program slicing" learned slicing context 2024 2025 2026"

Links: [{"title":"NeurIPS: Neural Information Processing Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2212"},{"title":"Towards transparent 6G AI-RAN: A survey on explainable deep reinforcement learning for intelligent network slicing - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2949715925000757"},{"title":"Predictive Program Slicing via Execution Knowledge-Guided","url":"https://aashishyadavally.github.io/assets/pdf/pub-fse2024.pdf"},{"title":"[2409.12369] Program Slicing in the Era of Large Language Models","url":"https://arxiv.org/abs/2409.12369"},{"title":"Program Slicing in the Era of Large Language Models","url":"https://arxiv.org/html/2409.12369v1"},{"title":"ICONIP: International Conference on Neural Information Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1438"},{"title":"IJCNN: International Joint Conference on Neural Network 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1573"},{"title":"ICLR 2026 Workshop Proposal MemAgents: Memory for LLM-Based Agentic Systems","url":"https://openreview.net/pdf?id=U51WxL382H"},{"title":"[2407.20281] NeuSemSlice: Towards Effective DNN Model Maintenance via Neuron-level Semantic Slicing","url":"https://arxiv.org/abs/2407.20281"},{"title":"2026 Conference","url":"https://neurips.cc/"}]

Based on the search results, here are relevant findings related to neural program slicing and learned slicing context:

## Recent Work on Learning-Based Program Slicing

Recent research includes "Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning", published in July 2024. This work, called ND-Slicer, was evaluated extensively on both executable and non-executable Python programs. The approach uses a sequence-to-sequence framework where the decoder learns the conditional probability of generating discrete line numbers corresponding to program statements, and learns the subtleties of execution order with respect to the executing iteration of the slicing criterion.

## Large Language Models for Program Slicing

Another significant recent work from September 2024 investigates the application of LLMs to program slicing. The study investigates the application of large language models (LLMs) to both static and dynamic program slicing, with a focus on Java programs, evaluating four state-of-the-art LLMs—GPT-4o, GPT-3.5 Turbo, Llama-2, and Gemma-7B leveraging advanced prompting techniques, including few-shot learning and chain-of-thought reasoning. GPT-4o performed the best in both static and dynamic slicing, achieving an accuracy of 60.84% and 59.69%, respectively.

## Neural Network Semantic Slicing

NeuSemSlice is a framework that introduces the semantic slicing technique to effectively identify critical neuron-level semantic components in DNN models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9f40786-e75b-41c9-bd6b-0bf2b2a16993",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "b519b7dd-b122-479e-a5df-886c7b545840",
  "sourceToolAssistantUUID": "f9f40786-e75b-41c9-bd6b-0bf2b2a16993",
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

_source line 31 · 2026-05-10T17:51:40.602Z_

<details><summary>↩ Tool result · `toolu_018z7ySYt5DUXfkRSSXmr6dJ`</summary>

```text
Web search results for query: "CODEFILTER "impact-driven context filtering" cross-file code static analysis polarity training 2025"

Links: [{"title":"Impact-driven Context Filtering For Cross-file Code ...","url":"https://www.arxiv.org/pdf/2508.05970"},{"title":"Impact-driven Context Filtering For Cross-file Code Completion","url":"https://arxiv.org/html/2508.05970"},{"title":"(PDF) Impact-driven Context Filtering For Cross-file Code Completion","url":"https://www.researchgate.net/publication/394427057_Impact-driven_Context_Filtering_For_Cross-file_Code_Completion"},{"title":"[2508.05970] Impact-driven Context Filtering For Cross-file Code Completion","url":"https://arxiv.org/abs/2508.05970"},{"title":"Impact-driven Context Filtering For Cross-file Code Completion | OpenReview","url":"https://openreview.net/forum?id=0Y2zXLFBji"},{"title":"CoCoMIC: Code Completion by Jointly Modeling In-file and Cross-file Context | Request PDF","url":"https://www.researchgate.net/publication/401328373_CoCoMIC_Code_Completion_by_Jointly_Modeling_In-file_and_Cross-file_Context"},{"title":"Overview of our proposed model. READSUM consists of four phases:... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Overview-of-our-proposed-model-READSUM-consists-of-four-phases-embedding-layer-for-code_fig1_370454918"},{"title":"About me - Shangqing Liu’s Homepage","url":"https://shangqing-liu.github.io/"},{"title":"A Large-Scale Collection Of (Non-)Actionable Static Code Analysis Reports | Scientific Data","url":"https://www.nature.com/articles/s41597-025-06154-7"},{"title":"GitHub - codefuse-ai/Awesome-Code-LLM: [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. · GitHub","url":"https://github.com/codefuse-ai/Awesome-Code-LLM"}]

Based on the search results, I found comprehensive information about CODEFILTER and its approach to impact-driven context filtering for cross-file code completion:

## Overview

CODEFILTER is an adaptive retrieval context trimming framework designed to effectively select relevant retrieved contexts for repository-level code completion, trained on a constructed dataset where each retrieved cross-file chunk is annotated with its polarity to guide the model in determining whether it is beneficial for completion.

## Core Problem and Solution

A likelihood-based metric was introduced to evaluate the impact of each retrieved code chunk on the completion, revealing that despite retrieving numerous chunks, only a small subset positively contributes to the completion, while some chunks even degrade performance. To address this, researchers constructed a dataset with 43k instances from nearly 6k diverse Python repositories containing over 400k cross-file context chunks, each labeled as positive, neutral, or negative using a likelihood-based metric, which was used to train LLMs to evaluate the polarity of retrieved code chunks and retain only the positive ones.

## Technical Approach

The framework uses special signal tokens in two categories: adaptive-retrieval tokens (&lt;EC>, &lt;MC>) where &lt;EC> indicates sufficient context and &lt;MC> requests additional cross-file chunks, and polarity tokens (&lt;pos>, &lt;neg>, &lt;neu>) which mark a chunk's positive, negative, or neutral impact.

## Performance and Generalization

Extensive evaluation on the RepoEval and CrossCodeLongEval benchmarks demonstrates that CODEFILTER consistently improves completion accuracy compared to approaches without filtering operations, significantly reduces the length of the input prompt for enhanced computational efficiency, and exhibits strong generalizability across different models.

The paper "Impact-driven Context Filtering For Cross-file Code Completion" was accepted by COLM25 in July 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cc78c6e-8aeb-4f55-8178-b91596b6468c",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "65524842-3f80-43f4-8a22-04e3c72e20af",
  "sourceToolAssistantUUID": "6cc78c6e-8aeb-4f55-8178-b91596b6468c",
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

_source line 32 · 2026-05-10T17:51:47.176Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EYFEe9mEPaTiDj7JAseSqP`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.05970",
  "prompt": "Extract the full methodology details of CODEFILTER. Specifically: 1) Does it use any static analysis (data-flow, control-flow, dependency analysis) to determine polarity labels? Or is polarity purely based on likelihood metrics from the LLM? 2) How is the training data constructed - what signals determine if a chunk is positive/negative/neutral? 3) Is this a distillation approach where a larger model's behavior is distilled into a smaller one? 4) How does this compare to explicitly using data-flow analysis for context selection?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65524842-3f80-43f4-8a22-04e3c72e20af",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK89efTV52Jrg8M1eTa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b64e32b1-250d-49ff-9e11-5f6b33793f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQWKN2NwXCxQjmYS3eszGF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3040,
      "cache_read_input_tokens": 19218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3040,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T17:51:49.583Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C828A6BAwhwhEKvViLkVe1`</summary>

```json
{
  "url": "https://aashishyadavally.github.io/assets/pdf/pub-fse2024.pdf",
  "prompt": "Extract the full details of this paper on Predictive Program Slicing. What is the methodology? Does it learn/predict program slices using neural networks? How does it relate to data-flow analysis? Is this distilling program analysis into a learned model? What are the key contributions and how does it compare to traditional program slicing?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b64e32b1-250d-49ff-9e11-5f6b33793f40",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK89efTV52Jrg8M1eTa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50d8bc42-f4ac-46a8-b0da-04d22c7da00c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQWKN2NwXCxQjmYS3eszGF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3040,
      "cache_read_input_tokens": 19218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3040,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T17:51:51.271Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CvW9FMnWCq4fi23rk2cK9W`</summary>

```json
{
  "url": "https://arxiv.org/html/2409.12369v1",
  "prompt": "Extract the methodology and key findings of this paper on Program Slicing in the Era of Large Language Models. Does it train or fine-tune LLMs to perform program slicing? How accurate are LLMs at replicating traditional program analysis like data-flow-based slicing? What are the implications for using neural models as replacements for static analysis?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50d8bc42-f4ac-46a8-b0da-04d22c7da00c",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK89efTV52Jrg8M1eTa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f94ab945-469b-436a-964b-dd86237acfe6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQWKN2NwXCxQjmYS3eszGF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3040,
      "cache_read_input_tokens": 19218,
      "output_tokens": 492,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3040
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 492,
          "cache_read_input_tokens": 19218,
          "cache_creation_input_tokens": 3040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3040,
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

_source line 35 · 2026-05-10T17:51:54.018Z_

<details><summary>↩ Tool result · `toolu_01EYFEe9mEPaTiDj7JAseSqP`</summary>

```text
# CODEFILTER Methodology Analysis

## 1) Polarity Determination Method

CODEFILTER relies **exclusively on likelihood-based metrics** rather than static analysis. The approach defines a contribution score as:

> "the difference in log-likelihood between a prompt containing only the in-file context and a prompt containing both"

This metric measures how much a retrieved chunk increases the LLM's probability of generating the ground-truth completion. Chunks are classified as positive (>10% improvement), negative (<-5% impact), or neutral based on these thresholds. No data-flow, control-flow, or dependency analysis is employed.

## 2) Training Data Construction

The paper describes a three-step process:

- **Sampling**: 43,000 instances extracted from 6,000 Python repositories with 400,000+ labeled chunks
- **Labeling**: Each chunk is assigned a polarity using the likelihood-based metric computed against ground-truth completions
- **Quality filtering**: Instances retain only those where retrieved positive chunks achieve Edit Similarity >0.5, ensuring meaningful context

The authors note that "only 15% of retrieved chunks genuinely support completion, while 5.6% degrade performance," validating their labeling methodology.

## 3) Distillation Approach?

This is **not primarily a distillation method**. However, Section 6.4 demonstrates that a small model (StarCoderBase-3B) can filter contexts for larger models, showing generalization across architectures. The framework functions as a "plug-and-play module," but the smaller model isn't distilling a larger model's knowledge—rather, it's learning a universal filtering policy.

## 4) Comparison to Static Analysis

The paper provides **no explicit comparison** to static analysis approaches. The authors acknowledge this limitation, stating analysis is "limited to Python" and suggests extending methods to other tasks. They emphasize their metric's model-agnostic nature but don't evaluate against structural analysis baselines, representing a gap in the evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b64e32b1-250d-49ff-9e11-5f6b33793f40",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "b09c4c41-f9ef-44e1-bd23-05a336caf9eb",
  "sourceToolAssistantUUID": "b64e32b1-250d-49ff-9e11-5f6b33793f40",
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

_source line 36 · 2026-05-10T17:51:54.057Z_

<details><summary>↩ Tool result · `toolu_01C828A6BAwhwhEKvViLkVe1`</summary>

```text
# Predictive Program Slicing: Neural Network-Based Analysis

I apologize, but the provided content appears to be a PDF file encoded in binary format rather than readable text. The material consists primarily of PDF object streams and compression data that cannot be meaningfully parsed for research content extraction.

To properly analyze a paper on predictive program slicing, I would need:

1. **Plaintext or HTML version** of the research document
2. **Direct access to the abstract and methodology sections**
3. **Clear exposition of the technical approach**

## What I Can Help With

Once you provide readable source material, I can address your specific questions:

- **Methodology identification**: Whether the approach uses neural networks for slice prediction
- **Machine learning integration**: How learned models compare to traditional data-flow analysis
- **Technical contributions**: Key innovations and performance improvements
- **Comparative analysis**: Distinctions from conventional program slicing techniques

**Please share the paper in a readable format** (plain text, markdown, or accessible PDF), and I'll provide a detailed technical summary following your specification requirements.

[Binary content (application/pdf, 957.5KB) also saved to /home/ubuntu/.claude-account-3/projects/-/89242a75-96eb-4c62-bd61-c8808bbe5e16/tool-results/webfetch-1778435509990-u3sogz.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50d8bc42-f4ac-46a8-b0da-04d22c7da00c",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "8b7de5c5-ad5d-4605-ab13-81a81017d7ce",
  "sourceToolAssistantUUID": "50d8bc42-f4ac-46a8-b0da-04d22c7da00c",
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

_source line 37 · 2026-05-10T17:51:58.087Z_

<details><summary>↩ Tool result · `toolu_01CvW9FMnWCq4fi23rk2cK9W`</summary>

```text
# Program Slicing in the Era of Large Language Models: Analysis

## Methodology

This empirical study evaluates four state-of-the-art LLMs (GPT-4o, GPT-3.5 Turbo, Llama-2, Gemma-7B) on program slicing tasks using 100 Java programs from LeetCode. The researchers employed prompting techniques including zero-shot, one-shot, and chain-of-thought reasoning—**without training or fine-tuning the models**. Ground-truth slices were generated using traditional tools (JavaSlicer for static, Slicer4J for dynamic) and manually verified.

## Key Findings

**Performance Metrics:**
- GPT-4o achieved the best results: 60.84% accuracy (Accuracy-D) and 7.33% exact match accuracy for static slicing
- All models "struggled to achieve exact matches" across dynamic slicing tasks
- NS-Slicer baseline achieved 60.52% Accuracy-D but 0% exact matches

**Failure Analysis:**
Through manual analysis of 92 unsuccessful cases, researchers identified a taxonomy of failures:
- **Most common root cause:** Complex Control Flow (39 cases)
- **Most frequent error location:** Variable Declarations and Assignments (78 cases)
- Root causes categorized as: Lack of Logic Understanding, Code Complexity, and Model-specific Constraints

**Improvement Strategies:**
- Enhanced prompt crafting: 4% accuracy improvement
- Iterative prompting with human feedback: 3.9% improvement

## Implications

The findings suggest LLMs are **not ready as replacements for static analysis tools**. Despite GPT-4o's competitive dependency accuracy, the "0% exact match rates across models" indicates fundamental limitations in precision. The paper notes that "LLMs have yet to achieve reasonable performance" for program slicing, particularly struggling with nested control structures and data dependencies that traditional tools handle reliably.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f94ab945-469b-436a-964b-dd86237acfe6",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "3e8524ff-1d79-41ae-97b3-4ca2c4d447ea",
  "sourceToolAssistantUUID": "f94ab945-469b-436a-964b-dd86237acfe6",
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

_source line 38 · 2026-05-10T17:52:01.604Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012KKxjGwKJuA5hVVreDEcZb`</summary>

```json
{
  "query": "\"ND-Slicer\" \"predictive program slicing\" execution knowledge neural data-flow 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e8524ff-1d79-41ae-97b3-4ca2c4d447ea",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK9SQkd1da7w5jEmYzT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0f99e99-1330-49ab-93f4-02f0a80dcc93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pPwqVTykiKeLcpKRVaaS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1777,
      "cache_read_input_tokens": 22258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1777,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-10T17:52:02.527Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vsn2FVUXKSVYS69rbrfkdQ`</summary>

```json
{
  "query": "SWE-Pruner neural skimmer training methodology static analysis data-flow signals"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0f99e99-1330-49ab-93f4-02f0a80dcc93",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK9SQkd1da7w5jEmYzT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a26bb40-2abe-43fe-8c0f-6bfd416c7580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pPwqVTykiKeLcpKRVaaS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1777,
      "cache_read_input_tokens": 22258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1777,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-10T17:52:03.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SqmLXYA3YvmQuxKA5eajPK`</summary>

```json
{
  "query": "\"distill static analysis\" neural network code understanding context 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a26bb40-2abe-43fe-8c0f-6bfd416c7580",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauK9SQkd1da7w5jEmYzT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bb222cb-0f7a-455a-a7aa-f07ed5edfb00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pPwqVTykiKeLcpKRVaaS8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1777,
      "cache_read_input_tokens": 22258,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1777
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 22258,
          "cache_creation_input_tokens": 1777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1777,
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

_source line 41 · 2026-05-10T17:52:08.947Z_

<details><summary>↩ Tool result · `toolu_012KKxjGwKJuA5hVVreDEcZb`</summary>

```text
Web search results for query: ""ND-Slicer" "predictive program slicing" execution knowledge neural data-flow 2024"

Links: [{"title":"Predictive Program Slicing via Execution Knowledge-Guided","url":"https://aashishyadavally.github.io/assets/pdf/pub-fse2024.pdf"},{"title":"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning (FSE 2024 - Posters) - FSE 2024","url":"https://2024.esec-fse.org/details/fse-2024-posters/26/Predictive-Program-Slicing-via-Execution-Knowledge-Guided-Dynamic-Dependence-Learning"},{"title":"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3643739"},{"title":"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/yadavally2024predictive/"},{"title":"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning | Request PDF","url":"https://www.researchgate.net/publication/382221875_Predictive_Program_Slicing_via_Execution_Knowledge-Guided_Dynamic_Dependence_Learning"},{"title":"GitHub - aashishyadavally/nd-slicer: A learning-based approach to dynamic backward slicing","url":"https://github.com/aashishyadavally/nd-slicer"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Predictive+Program+Slicing+via+Execution+Knowledge-Guided+Dynamic+Dependence+Learning."},{"title":"Predictive Program Slicing via Execution Knowledge- ...","url":"https://dl.acm.org/doi/pdf/10.1145/3643739"},{"title":"A Learning-Based Approach to Static Program Slicing","url":"https://dl.acm.org/doi/pdf/10.1145/3649814"},{"title":"SLICET5: Static Program Slicing using Language Models with","url":"https://arxiv.org/pdf/2509.17338"}]

Based on the search results, here's what I found about ND-Slicer:

## Overview

ND-Slicer is a predictive backward slicing approach that is applicable to both complete and partial programs. ND-Slicer is the first neural network-based approach to dynamic program slicing.

## Purpose and Approach

ND-Slicer is a predictive slicing methodology that caters to specific executions based on a particular input, overcoming the need for actual execution. It enables this by leveraging execution-aware pre-training to learn the dynamic program dependencies, including both dynamic data and control dependencies.

## Technical Details

The approach leverages CodeExecutor, a model pre-trained on code execution, as the encoder in the framework. The model adopts a sequence-to-sequence framework for predictive slicing using Pointer-Transformer, which copies from the input sequence to generate the output sequence. This makes it suitable for the task, as the dynamic backward slice predicted by ND-Slicer is a sequence of line identifiers selected from the input sequence.

## Performance Results

Empirical evaluation revealed a high accuracy in predicting program slices, achieving an exact-match accuracy of 81.31% and a ROUGE-LCS score of 0.954 on Python programs. As an extrinsic evaluation, ND-Slicer demonstrated usefulness in crash detection, with it locating faults with an accuracy of 63.88%.

## Publication

The work was published in July 2024, and the code and dataset are publicly available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0f99e99-1330-49ab-93f4-02f0a80dcc93",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "cb62d418-bfc8-42bc-b369-d986511f8567",
  "sourceToolAssistantUUID": "f0f99e99-1330-49ab-93f4-02f0a80dcc93",
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

_source line 42 · 2026-05-10T17:52:11.055Z_

<details><summary>↩ Tool result · `toolu_01Vsn2FVUXKSVYS69rbrfkdQ`</summary>

```text
Web search results for query: "SWE-Pruner neural skimmer training methodology static analysis data-flow signals"

Links: [{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/html/2601.16746v1"},{"title":"(PDF) SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.researchgate.net/publication/400071923_SWE-Pruner_Self-Adaptive_Context_Pruning_for_Coding_Agents"},{"title":"Paper page - SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://huggingface.co/papers/2601.16746"},{"title":"GitHub - Ayanami1314/swe-pruner · GitHub","url":"https://github.com/Ayanami1314/swe-pruner"},{"title":"[2601.16746] SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/abs/2601.16746"},{"title":"A Soft-Pruning Method Applied During Training of Spiking Neural Networks for In-memory Computing Applications - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6497807/"},{"title":"A Method for Processing Static Analysis Alarms Based on Deep Learning","url":"https://www.mdpi.com/2076-3417/14/13/5542"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.16746v1"},{"title":"Understanding the Flows of Signals and Gradients: A Tutorial on Algorithms Needed to Implement a Deep Neural Network from Scratch","url":"https://www.mdpi.com/2076-3417/14/21/9972"}]

Based on the search results, here's information about SWE-Pruner's neural skimmer training methodology:

## Training Methodology

Training the neural skimmer requires data with line-level supervision that preserves both relevance and code structure. Since such dataset is unavailable, a polyglot training corpus is constructed following a teacher-student paradigm.

Code snippets are sampled from GitHub, and a teacher LLM (Qwen3-Coder-30B-A3B-Instruct) is utilized to synthesize task-oriented queries that target specific functional subsets of each snippet. This process produces training quadruplets (q, C, M, S), where M is a binary line-level mask indicating which lines to retain, designed based on a taxonomy of nine distinct agentic tasks, such as Code Debugging, Feature Addition, and Code Refactoring.

## Neural Skimmer Architecture

The neural skimmer extends the Qwen3-Reranker-0.6B backbone with two specialized heads: a CRF-based pruning head for line-level filtering and a reranking head for document-level scoring. To capture representations at different semantic levels, hidden states from three intermediate layers (layers 7, 14, and 28) of the backbone are extracted and concatenated, then processed through a self-attention block followed by a multi-head attention layer.

## Performance Results

By integrating seamlessly as middleware within agentic workflows, SWE-Pruner reduces token usage by 23–38% on SWE-Bench and 29–54% on SWE-QA, achieving up to 14.84× compression on single-turn benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a26bb40-2abe-43fe-8c0f-6bfd416c7580",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "4144461b-ea05-4541-bbab-13f293ed48f5",
  "sourceToolAssistantUUID": "2a26bb40-2abe-43fe-8c0f-6bfd416c7580",
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

_source line 43 · 2026-05-10T17:52:12.454Z_

<details><summary>↩ Tool result · `toolu_01SqmLXYA3YvmQuxKA5eajPK`</summary>

```text
Web search results for query: ""distill static analysis" neural network code understanding context 2024 2025 2026"

Links: [{"title":"GitHub - Guang000/Awesome-Dataset-Distillation: A curated list of awesome papers on dataset distillation and related applications. · GitHub","url":"https://github.com/Guang000/Awesome-Dataset-Distillation"},{"title":"Static Source Code Analysis Using Neural Networks - OSTI.GOV","url":"https://www.osti.gov/servlets/purl/1575163"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5bb87d5ecaf736d3798a277006dd8b00-Paper-Conference.pdf"},{"title":"NeurIPS: Neural Information Processing Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2212"},{"title":"Knowledge distillation and dataset distillation of large language models: emerging trends, challenges, and future directions | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11423-3"},{"title":"Data Distillation: A Survey | OpenReview","url":"https://openreview.net/forum?id=lmXMXP74TO"},{"title":"GitHub - zezhishao/DailyArXiv: Daily ArXiv Papers. · GitHub","url":"https://github.com/zezhishao/DailyArXiv"},{"title":"GitHub - DefangChen/Knowledge-Distillation-Paper: This resposity maintains a collection of important papers on knowledge distillation (awesome-knowledge-distillation)).","url":"https://github.com/DefangChen/Knowledge-Distillation-Paper"},{"title":"GitHub - shriramsb/Distilling-the-Knowledge-in-a-Neural-Network: Demonstration of transfer of knowledge and generalization with distillation · GitHub","url":"https://github.com/shriramsb/Distilling-the-Knowledge-in-a-Neural-Network"},{"title":"[1503.02531] Distilling the Knowledge in a Neural Network","url":"https://arxiv.org/abs/1503.02531"}]

Based on the search results, I found information related to dataset distillation and knowledge distillation research, though the results are more focused on general distillation techniques rather than specifically on static analysis of neural networks for code understanding.

## Key Findings:

**Dataset and Knowledge Distillation Research (2024-2026):**

The search revealed active research in distillation across multiple domains. Recent papers include work on dataset distillation from first principles (2024), information-guided diffusion sampling for dataset distillation (NeurIPS 2025 Workshop), dataset distillation via spectral filtering (ICLR 2026), and various other distillation approaches published at major conferences like CVPR, ICCV, and AAAI in 2024-2026.

**LLM Distillation:**

Research highlights the exponential growth of Large Language Models and the need for efficient compression strategies, with surveys examining both Knowledge Distillation (KD) and Dataset Distillation (DD) aimed at compressing LLMs while preserving their reasoning capabilities.

**General Data Distillation:**

Data distillation approaches aim to synthesize concise data summaries which can serve as effective replacements of the original dataset for scenarios like model training, inference, and architecture search.

However, the search results do not contain specific information about applying distillation techniques to static analysis for code understanding. To find research specifically connecting static analysis, neural networks, and code understanding in 2024-2026, you may need a more targeted search query focusing on program analysis, code representation, or software engineering applications of neural networks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bb222cb-0f7a-455a-a7aa-f07ed5edfb00",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "8a67489c-2e02-46a5-9d57-e1f9bb439c45",
  "sourceToolAssistantUUID": "5bb222cb-0f7a-455a-a7aa-f07ed5edfb00",
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

_source line 44 · 2026-05-10T17:52:18.538Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PX6ZyEXi2iswqHpV2mEZrK`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.16746v1",
  "prompt": "Extract detailed information about SWE-Pruner's training methodology. Specifically: 1) How is the teacher-student paradigm used? 2) Does the teacher use any static analysis or data-flow analysis signals? 3) How are the binary line-level masks (M) generated - are they based on program analysis or purely LLM-generated? 4) What are the nine distinct agentic tasks used for training? 5) How does this compare to distilling data-flow analysis into a neural model?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a67489c-2e02-46a5-9d57-e1f9bb439c45",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauKAVpAX43gbtXHuvQH4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04b66994-8ece-4c62-86be-76a01990e14b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MsMBvpdpn8xQj4bawAoiG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3103,
      "cache_read_input_tokens": 24035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3103,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-10T17:52:19.983Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017DKCzYMX3EUJgHp4tta8wE`</summary>

```json
{
  "query": "CAST \"enhancing code retrieval-augmented generation\" tree-sitter CMU 2025 context selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04b66994-8ece-4c62-86be-76a01990e14b",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauKAVpAX43gbtXHuvQH4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3fe6a59-243a-4ab2-b852-7e333fbbcf30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MsMBvpdpn8xQj4bawAoiG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3103,
      "cache_read_input_tokens": 24035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3103,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-10T17:52:20.816Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AM9NCpDfodAURMxiBEyFpQ`</summary>

```json
{
  "query": "\"learn program dependence\" OR \"neural dependency analysis\" OR \"learned code context\" repair localization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3fe6a59-243a-4ab2-b852-7e333fbbcf30",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauKAVpAX43gbtXHuvQH4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "085446a7-5582-4c7a-a9a6-784db015deb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MsMBvpdpn8xQj4bawAoiG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3103,
      "cache_read_input_tokens": 24035,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3103
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 24035,
          "cache_creation_input_tokens": 3103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3103,
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

_source line 47 · 2026-05-10T17:52:27.446Z_

<details><summary>↩ Tool result · `toolu_017DKCzYMX3EUJgHp4tta8wE`</summary>

```text
Web search results for query: "CAST "enhancing code retrieval-augmented generation" tree-sitter CMU 2025 context selection"

Links: [{"title":"CAST: Enhancing Code Retrieval-Augmented Generation","url":"https://www.cs.cmu.edu/~sherryw/assets/pubs/2025-cast.pdf"},{"title":"cAST: Enhancing Code Retrieval-Augmented Generation with Structural Chunking via Abstract Syntax Tree","url":"https://arxiv.org/html/2506.15655v1"},{"title":"cAST: Enhancing Code Retrieval-Augmented Generation ...","url":"https://arxiv.org/pdf/2506.15655"},{"title":"[Literature Review] cAST: Enhancing Code Retrieval-Augmented Generation with Structural Chunking via Abstract Syntax Tree","url":"https://www.themoonlight.io/en/review/cast-enhancing-code-retrieval-augmented-generation-with-structural-chunking-via-abstract-syntax-tree"},{"title":"[2506.15655] cAST: Enhancing Code Retrieval-Augmented Generation with Structural Chunking via Abstract Syntax Tree","url":"https://arxiv.org/abs/2506.15655"},{"title":"GitHub - yilinjz/astchunk: ASTChunk is a Python toolkit for code chunking using Abstract Syntax Trees (ASTs), designed to create structurally sound and meaningful code segments. · GitHub","url":"https://github.com/yilinjz/astchunk"},{"title":"cAST: Enhancing Code Retrieval-Augmented Generation with Structural Chunking via Abstract Syntax Tree - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.430/"},{"title":"Building code-chunk: AST Aware Code Chunking","url":"https://supermemory.ai/blog/building-code-chunk-ast-aware-code-chunking/"},{"title":"[PDF] cAST: Enhancing Code Retrieval-Augmented Generation with Structural Chunking via Abstract Syntax Tree | Semantic Scholar","url":"https://www.semanticscholar.org/paper/cAST:-Enhancing-Code-Retrieval-Augmented-Generation-Zhang-Zhao/4a1a13a7005beaaa506fe2f323e2ec0a7f0130b3"},{"title":"cAST: Enhancing Code Retrieval-Augmented Generation with Structural Chunking via Abstract Syntax Tree","url":"https://www.researchgate.net/publication/397421461_cAST_Enhancing_Code_Retrieval-Augmented_Generation_with_Structural_Chunking_via_Abstract_Syntax_Tree"}]

The search has found relevant results about the cAST (Chunking via Abstract Syntax Trees) paper from CMU. Here's a summary of what I found:

## cAST: Enhancing Code Retrieval-Augmented Generation

The paper was authored by Yilin Zhang, Xinran Zhao, Zora Zhiruo Wang, Chenyang Yang, Jiayi Wei, and Tongshuang Wu, published in the Findings of the Association for Computational Linguistics: EMNLP 2025.

### Core Problem and Solution

The paper addresses chunking—the process of dividing documents into retrievable units. Existing line-based chunking heuristics often break semantic structures, splitting functions or merging unrelated code, which can degrade generation quality.

The proposed method, cAST, is a structure-aware approach that recursively breaks large AST nodes into smaller chunks and merges sibling nodes while respecting size limits.

### Technical Implementation

The work uses the tree-sitter library for AST tree parsing. AST (Abstract Syntax Tree) representation captures the syntactic structure of source code in a way that is both hierarchical and semantically rich, encoding language constructs—like functions, classes, loops, and conditionals—as distinct nodes in a structured parse tree.

### Results

This approach generates self-contained, semantically coherent units across programming languages and tasks, improving performance on diverse code generation tasks, e.g., boosting Recall@5 by 4.3 points on RepoEval retrieval and Pass@1 by 2.67 points on SWE-bench generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3fe6a59-243a-4ab2-b852-7e333fbbcf30",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "7df9b225-3252-4752-9ae5-a82c3a73869c",
  "sourceToolAssistantUUID": "c3fe6a59-243a-4ab2-b852-7e333fbbcf30",
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

_source line 48 · 2026-05-10T17:52:28.012Z_

<details><summary>↩ Tool result · `toolu_01PX6ZyEXi2iswqHpV2mEZrK`</summary>

```text
# SWE-Pruner Training Methodology Analysis

## 1. Teacher-Student Paradigm

The framework employs a structured approach where "a teacher LLM (Qwen3-Coder-30B-A3B-Instruct) synthesizes task-oriented queries that target specific functional subsets of each snippet." The student model (lightweight 0.6B reranker) learns to perform line-level pruning by training on these synthetic annotations.

## 2. Static Analysis Signals

The training methodology relies **exclusively on LLM-generated signals** rather than static program analysis. The document contains no references to data-flow analysis, control-flow graphs, or AST-based dependency tracking during the label generation phase.

## 3. Binary Line-Level Mask Generation

The masks are "purely LLM-generated" through a synthetic data pipeline. The process involves:
- Sampling code from curated GitHub repositories
- Having the teacher LLM synthesize queries targeting "specific functional subsets"
- Producing training quadruplets "(q,C,M,S)" where M represents binary retention decisions

Quality control uses "Qwen3-Next-80B-A3B-Thinking as an LLM-as-a-Judge filter" to validate annotations.

## 4. Nine Agentic Tasks

The taxonomy includes: code-summarize, code-refactor, find-relevant-part, code-optimize, code-locate, code-explain, code-debug, feature-addition, and code-completion—"reflecting common information needs in software development workflows."

## 5. Comparison to Data-Flow Analysis Distillation

SWE-Pruner fundamentally differs from distilling static analysis:

| Aspect | SWE-Pruner | Data-Flow Approach |
|--------|-----------|-------------------|
| Signal Source | LLM-generated task-specific relevance | Program dependencies/data flow |
| Granularity | Line-level with task context | Often statement/variable-level |
| Adaptability | Dynamic per query/goal | Static program structure |

SWE-Pruner prioritizes **task-aware relevance** over structural program properties, enabling adaptive filtering based on evolving agent objectives rather than fixed computational dependencies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04b66994-8ece-4c62-86be-76a01990e14b",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "72bfd863-81f6-4e2a-b4e0-07cfc65512da",
  "sourceToolAssistantUUID": "04b66994-8ece-4c62-86be-76a01990e14b",
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

_source line 49 · 2026-05-10T17:52:28.368Z_

<details><summary>↩ Tool result · `toolu_01AM9NCpDfodAURMxiBEyFpQ`</summary>

```text
Web search results for query: ""learn program dependence" OR "neural dependency analysis" OR "learned code context" repair localization 2025 2026"

Links: [{"title":"DLFix: Context-based Code Transformation Learning for Automated Program Repair | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DLFix:-Context-based-Code-Transformation-Learning-Li-Wang/e24c70ebdcf7aba490fdbdc62bf6436ddc9721af"},{"title":"DLFix: context-based code transformation learning for automated program repair | Request PDF","url":"https://www.researchgate.net/publication/346044786_DLFix_context-based_code_transformation_learning_for_automated_program_repair"},{"title":"Improving Bug Detection and Fixing via Code ...","url":"https://dl.acm.org/doi/pdf/10.1145/3377812.3382172"},{"title":"Precise Learning of Source Code Contextual Semantics via Hierarchical Dependence Structure and Graph Attention Networks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0164121221002053"},{"title":"Revisiting Automated Program Repair via Zero-Shot Learning","url":"http://lingming.cs.illinois.edu/publications/fse2022a.pdf"},{"title":"DLFix: context-based code transformation learning ...","url":"https://dl.acm.org/doi/10.1145/3377811.3380345"},{"title":"Code generation with large language models: a survey from neural program synthesis to autonomous software development | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-026-07230-0"},{"title":"DLFix: Context-based Code Transformation Learning for Automated Program Repair (ICSE 2020 - Technical Papers) - ICSE 2020","url":"https://conf.researchr.org/details/icse-2020/icse-2020-papers/59/DLFix-Context-based-Code-Transformation-Learning-for-Automated-Program-Repair"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Deep learning-based software engineering: progress, challenges, and opportunities | Science China Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11432-023-4127-5"}]

Based on the search results, I found relevant research on automated program repair with learned code context and program dependence analysis. Here are the key findings:

## Key Research Areas

DLFix is a two-tier DL model that treats APR as code transformation learning from the prior bug fixes and the surrounding code contexts of the fixes. This approach directly addresses your search terms about learned code context in repair localization.

## Program Dependence in Repair

Program Dependence Graph (PDG) and Data Flow Graph (DFG) are used to connect the method under investigation with the other relevant methods that might contribute to the buggy code. The approach involves using program dependency and data flow graphs to catch code relationship among methods, which is central to neural dependency analysis for repair.

## Neural Dependency Analysis Techniques

MFGNN (Multi-Flow Graph Neural Network) is designed to obtain contextual semantics from source code models and integrates an attention-based graph learning layer evolved from GAT. This neural approach to dependency analysis aligns with your search query about neural dependency analysis in repair localization.

## Recent 2025 Developments

Recent 2025 work includes ReAPR: Automatic program repair via retrieval-augmented large language models and AdverIntent-Agent: Adversarial Reasoning for Repair Based on Inferred Program Intent, showing active research in this area through 2025-2026.

The search reveals that learning program dependencies through neural approaches for repair localization is an active and advancing research area, with both traditional dependency graph approaches and modern neural dependency analysis methods being employed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "085446a7-5582-4c7a-a9a6-784db015deb8",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "be70a710-f591-423d-a290-ad4a3feae12b",
  "sourceToolAssistantUUID": "085446a7-5582-4c7a-a9a6-784db015deb8",
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

_source line 50 · 2026-05-10T17:52:34.466Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019NxTEqXtdZXYYTKPXbDcGe`</summary>

```json
{
  "query": "SLICET5 \"static program slicing using language models\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be70a710-f591-423d-a290-ad4a3feae12b",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauKBfv9zBHazQsKqKX8i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35b297d8-9645-4d33-96ef-10f8c186a9d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RJHsxyGMesGV1Jnafk6fp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2990,
      "cache_read_input_tokens": 27138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2990,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-10T17:52:35.745Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UUDyqcAJ2x9gJZ9VpUrumS`</summary>

```json
{
  "query": "\"data flow\" \"context selection\" OR \"context pruning\" code LLM neural 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35b297d8-9645-4d33-96ef-10f8c186a9d3",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauKBfv9zBHazQsKqKX8i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e21ac1c-f3ae-4200-9251-e4edf51a8283",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RJHsxyGMesGV1Jnafk6fp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2990,
      "cache_read_input_tokens": 27138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2990,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-10T17:52:41.751Z_

<details><summary>↩ Tool result · `toolu_019NxTEqXtdZXYYTKPXbDcGe`</summary>

```text
Web search results for query: "SLICET5 "static program slicing using language models" 2025"

Links: [{"title":"[2509.17338] SLICET5: Static Program Slicing using Language Models with Copy Mechanism and Constrained Decoding","url":"https://arxiv.org/abs/2509.17338"},{"title":"SLICET5: Static Program Slicing using Language Models with","url":"https://arxiv.org/pdf/2509.17338"},{"title":"SliceT5: Static Program Slicing using Language Models with Copy Mechanism and Constrained Decoding","url":"https://arxiv.org/html/2509.17338v1"},{"title":"Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding","url":"https://arxiv.org/html/2604.26961"},{"title":"[2604.26961] Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding","url":"https://arxiv.org/abs/2604.26961"},{"title":"A Brief Survey of Program Slicing | Request PDF","url":"https://www.researchgate.net/publication/213876689_A_Brief_Survey_of_Program_Slicing"},{"title":"GrammarT5: Grammar-Integrated Pretrained Encoder-Decoder Neural Model for Code | Request PDF","url":"https://www.researchgate.net/publication/379790202_GrammarT5_Grammar-Integrated_Pretrained_Encoder-Decoder_Neural_Model_for_Code"},{"title":"A Learning-Based Approach to Static Program Slicing | Request PDF","url":"https://www.researchgate.net/publication/380202230_A_Learning-Based_Approach_to_Static_Program_Slicing"},{"title":"Program Slicing in the Era of Large Language Models","url":"https://www.computer.org/csdl/proceedings-article/compsac/2025/743400b224/29yDy35JQQg"},{"title":"(PDF) An Overview of Program Slicing","url":"https://www.researchgate.net/publication/2390528_An_Overview_of_Program_Slicing"}]

I found information about SLICET5. Here are the key findings:

## SLICET5: Static Program Slicing Using Language Models

SLICET5 is a novel slicing framework submitted on September 22, 2025 that reformulates static program slicing as a sequence-to-sequence task using lightweight language models (e.g., CodeT5+).

### Problem Being Addressed

Traditional static slicing tools rely on parsing complete source code, which limits their applicability to real-world scenarios where code snippets are incomplete or unparsable. Learning-based approaches face critical challenges including inaccurate dependency identification and unconstrained generation, where models produce slices with extraneous or hallucinated tokens not present in the input, violating the structural integrity of slices.

### Key Innovations

The approach incorporates two key innovations, which include a copy mechanism and constrained decoding mechanisms to address the identified limitations.

### Performance

SLICET5 consistently outperforms state-of-the-art baselines (e.g., FM-based slicer and NS-slicer) across different datasets and evaluation metrics, outperforming the best NS-slicer by at least 6.4% and 27% in terms of ExactMatch on the two datasets, respectively. SLICET5 also demonstrates robustness for unparsable code snippets.

### Authors

The paper is by Pengfei He, Shaowei Wang, and Tse-Hsun Chen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35b297d8-9645-4d33-96ef-10f8c186a9d3",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "0c05db44-ed42-48a2-8d4b-f2f16b91d24c",
  "sourceToolAssistantUUID": "35b297d8-9645-4d33-96ef-10f8c186a9d3",
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

_source line 53 · 2026-05-10T17:52:44.210Z_

<details><summary>↩ Tool result · `toolu_01UUDyqcAJ2x9gJZ9VpUrumS`</summary>

```text
Web search results for query: ""data flow" "context selection" OR "context pruning" code LLM neural 2025 2026"

Links: [{"title":"Pruning and Distilling LLMs Using NVIDIA TensorRT Model Optimizer | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/pruning-and-distilling-llms-using-nvidia-tensorrt-model-optimizer/"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"Advancing Long-Context LLM Performance in 2025 | Flow AI","url":"https://flow-ai.com/blog/advancing-long-context-llm-performance-in-2025"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf"},{"title":"arXiv:2506.08436v1 [cs.CL] 10 Jun 2025","url":"https://arxiv.org/pdf/2506.08436"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"LLM Inference Optimization Techniques | Clarifai Guide","url":"https://www.clarifai.com/blog/llm-inference-optimization/"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"Efficient self-attention with smart pruning for sustainable large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-92586-5"}]

Based on the web search results, here's what I found regarding data flow, context selection, and context pruning for code LLMs with neural approaches in 2025-2026:

## Context Pruning and Selection in LLMs

State-of-the-art compression techniques include pruning, quantization, knowledge distillation, and neural architecture search (NAS), which aim to reduce model size, enhance inference speed, and lower energy consumption while maintaining performance.

### Context-Level Pruning Approaches

A practical and efficient setting consists in fine-tuning a small-size model such as DeBERTa as an extractive pruner with a lightweight prediction head for selecting relevant context parts. This represents a neural approach to context selection that's more efficient than using large LLMs as pruners.

LLMLingua and Selective Context use LLMs to remove tokens with high generation probabilities, LLMLingua2 is a small BERT-based model finetuned to eliminate redundant tokens, and LongLLMLingua proposes query-dependent LLM-based token pruning based on contrastive perplexity.

### Data Flow and Attention-Based Selection

Infinite Retrieval leverages the LLM's attention mechanism to identify and retain the most critical tokens from an input sequence, picking the top-K tokens based on their importance to the query, then selecting the full sentences containing those tokens.

### Network Pruning in Code/Neural Networks

NVIDIA researchers have demonstrated a method combining structured weight pruning with knowledge distillation as a strategy for compressing large models into smaller, efficient variants without significant loss in quality. Width pruning eliminates internal structures such as individual neurons, attention heads, or embedding channels, slimming down the model's width.

The search results show active development in 2025-2026 across multiple fronts for efficient context handling and neural model compression.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e21ac1c-f3ae-4200-9251-e4edf51a8283",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "d97aeaac-6209-4ebd-97b7-4f5de3d0f972",
  "sourceToolAssistantUUID": "2e21ac1c-f3ae-4200-9251-e4edf51a8283",
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

_source line 54 · 2026-05-10T17:52:50.115Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UcqFY9eS3zgQZV7fDXaZtS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.26961",
  "prompt": "Extract the full abstract and key contributions of this paper on Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding. How does it use dataflow-aware pretraining? Does it distill data-flow analysis into a neural model? What is the relationship between data-flow analysis and the model's training? When was this published?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d97aeaac-6209-4ebd-97b7-4f5de3d0f972",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauKCqc6infS7miouKdG9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e76affcf-9a1d-4f58-bcbf-8ca8684005fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTD1kQxdw5gTCDQwBJyBMV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 30128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2093,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-10T17:52:50.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017QihAy7tr7UNrhMuxvwjJt`</summary>

```json
{
  "query": "\"dataflow-aware\" pretraining program slicing language model 2604.26961"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e76affcf-9a1d-4f58-bcbf-8ca8684005fc",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauKCqc6infS7miouKdG9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9070a350-e500-4b32-af0b-9796c1f50e83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTD1kQxdw5gTCDQwBJyBMV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 30128,
      "output_tokens": 219,
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
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 30128,
          "cache_creation_input_tokens": 2093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2093,
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

_source line 56 · 2026-05-10T17:52:54.345Z_

<details><summary>↩ Tool result · `toolu_017QihAy7tr7UNrhMuxvwjJt`</summary>

```text
Web search results for query: ""dataflow-aware" pretraining program slicing language model 2604.26961"

Links: [{"title":"Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding","url":"https://arxiv.org/html/2604.26961"},{"title":"[2604.26961] Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding","url":"https://arxiv.org/abs/2604.26961"}]

I found the paper you're looking for! Here's what I found:

The paper proposes Sliceformer, a novel approach that reformulates static program slicing as a sequence-to-sequence task using small language models such as CodeT5+. 

Static program slicing is a fundamental software engineering technique for isolating code relevant to specific variables, and while recent learning-based approaches using language models show promise in automating slice prediction, they suffer from inaccurate dependency modeling and unconstrained generation, where LMs fail to capture precise data flow relations and produce slices containing hallucinated tokens and statements.

The paper introduces two key innovations:

1. Dataflow-aware pretraining objectives that leverage data flow graphs (DFG) to teach models data dependencies through dataflow-preserving statement permutation and dataflow-aware span corruption.

2. A constrained decoding mechanism that enforces both lexical and syntactic constraints to eliminate hallucination.

The evaluation on Java and Python program slicing benchmarks demonstrates consistent improvements over state-of-the-art baselines with up to 22% gain in ExactMatch.

The paper was submitted on April 9, 2026, by Pengfei He, Shaowei Wang, Tse-Hsun (Peter) Chen, and Muhammad Asaduzzaman from the University of Manitoba, Concordia University, and University of Windsor.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9070a350-e500-4b32-af0b-9796c1f50e83",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "74cd205c-020e-45af-aa63-f601f059cd78",
  "sourceToolAssistantUUID": "9070a350-e500-4b32-af0b-9796c1f50e83",
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

_source line 57 · 2026-05-10T17:52:55.921Z_

<details><summary>↩ Tool result · `toolu_01UcqFY9eS3zgQZV7fDXaZtS`</summary>

```text
# Static Program Slicing with Language Models

## Full Abstract

"Static program slicing is a fundamental software engineering technique for isolating code relevant to specific variables. While recent learning-based approaches using language models (LMs) show promise in automating slice prediction, they suffer from inaccurate dependency modeling and unconstrained generation, where LMs fail to capture precise data flow relations and produce slices containing hallucinated tokens and statements. To address these challenges, we propose Sliceformer, a novel approach that reformulates static program slicing as a sequence-to-sequence task using small language models such as CodeT5+. Sliceformer introduces two key innovations that directly target the identified limitations. First, to improve dependency modeling, we design dataflow-aware pretraining objectives that leverage data flow graphs (DFG) to teach models data dependencies through dataflow-preserving statement permutation and dataflow-aware span corruption. Second, to eliminate hallucination, we develop a constrained decoding mechanism that enforces both lexical and syntactic constraints. We evaluate Sliceformer on Java and Python program slicing benchmarks, demonstrating consistent improvements over state-of-the-art baselines with up to 22% gain in ExactMatch."

## Key Contributions

The paper presents **Sliceformer**, introducing:

1. **Dataflow-aware pretraining** using two objectives: "dataflow-preserving statement permutation and dataflow-aware span corruption" to embed data dependencies into the model
2. **Constrained decoding** enforcing lexical and syntactic validity to prevent hallucination
3. Evaluation showing "up to 22% gain in ExactMatch" on Java and Python benchmarks

## Dataflow Integration Approach

Rather than distilling traditional data-flow analysis, the approach embeds dataflow concepts directly into pretraining by using "data flow graphs (DFG) to teach models data dependencies." This teaches the neural model to understand data relationships during training.

## Publication Date

**Accepted at ACL 2026** (submitted April 9, 2026)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e76affcf-9a1d-4f58-bcbf-8ca8684005fc",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "aa38f008d49a94408",
  "type": "user",
  "uuid": "f35cf107-ede2-478c-a606-3dc81b3f9369",
  "sourceToolAssistantUUID": "e76affcf-9a1d-4f58-bcbf-8ca8684005fc",
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

_source line 58 · 2026-05-10T17:54:05.976Z_

Now I have comprehensive information across all six questions. Let me compile the findings.

---

Here is my comprehensive analysis of the competing works relative to the proposed idea of "distilling data-flow analysis into a neural context selector" for code repair:

---

## 1. CODEFILTER (arXiv:2508.05970, accepted at COLM 2025)

**What it does:** An adaptive retrieval context filtering framework for cross-file code completion. It trains LLMs to evaluate the "polarity" (positive/negative/neutral) of retrieved code chunks using special tokens (`&lt;pos>`, `&lt;neg>`, `&lt;neu>`).

**Does it use static analysis signals for training?** No. Polarity labels are determined **purely through a likelihood-based metric** -- measuring how much a retrieved chunk increases the LLM's probability of generating the ground-truth completion. Chunks that improve log-likelihood by >10% are labeled positive; those degrading it by >5% are negative. No data-flow, control-flow, or dependency analysis is used.

**Comparison to your idea:** CODEFILTER is a **black-box empirical approach** to context filtering -- it learns "what helps completion" without understanding *why* (e.g., data dependencies). Your idea of distilling data-flow analysis would provide a more principled signal source (structural program dependencies) rather than an empirical proxy. CODEFILTER also targets code completion, not repair. However, the architecture (small model as plug-and-play filter) is similar in spirit.

**Key gap:** CODEFILTER has no structural program analysis basis, and operates only in the completion domain.

---

## 2. SWE-Pruner (arXiv:2601.16746, Jan 2026)

**What it does:** A self-adaptive context pruning framework using a lightweight 0.6B neural skimmer (based on Qwen3-Reranker-0.6B) that performs line-level filtering of agent contexts. Achieves 23-54% token reduction on SWE-Bench Verified while maintaining or improving success rates.

**Training methodology:** Uses a **teacher-student paradigm** where Qwen3-Coder-30B generates task-oriented queries and binary line-level masks across nine agentic task types (code-debug, feature-addition, code-refactor, etc.). Quality is validated by Qwen3-Next-80B as judge. The architecture uses a CRF-based pruning head and reranking head over concatenated hidden states from three backbone layers.

**Does it use static analysis?** No. Training signals are **purely LLM-generated**. There are no references to data-flow analysis, control-flow graphs, or AST-based dependency tracking. The masks are created by the teacher LLM reasoning about task relevance, not program structure.

**Comparison to your idea:** SWE-Pruner is the closest competitor architecturally (small neural model as context filter for coding agents), but its training signal is fundamentally different -- it uses LLM-generated task relevance rather than distilled program analysis. Your approach would use data-flow analysis as a more principled, deterministic training signal. The key differentiator for your idea would be: **data-flow provides ground-truth structural relevance** that LLM teachers may miss or hallucinate.

---

## 3. RepoRepair (arXiv:2603.01048, March 2026)

**What it does:** A documentation-enhanced approach to repository-level fault localization and repair. Achieves 45.7% repair rate on SWE-bench Lite at $0.44/fix.

**Methodology:**
- Generates hierarchical LLM-produced documentation (file-level and function-level)
- Three-tier localization: embedding-based file retrieval -> LLM-based file localization -> function-level localization
- Dependency-preserving repair context: retains (i) localized targets, (ii) imports/globals, (iii) statically referenced functions/classes

**Does it use data-flow analysis?** Only superficially. The "dependency-preserving" context preserves **static references** (import/call relationships) but does not perform data-flow or control-flow analysis. It relies on LLM semantic understanding over generated documentation rather than explicit dependency graphs.

**Could it subsume your idea?** Partially. RepoRepair's documentation-based localization achieves strong results but operates at a coarser granularity. It cannot capture fine-grained data dependencies (e.g., which variables flow into a buggy computation). Your idea could complement or improve upon RepoRepair's localization stage by providing more precise, data-flow-grounded context selection.

---

## 4. Direct Precedents for "Distilling Data-Flow into a Neural Model"

This is where I found the most relevant prior art:

**Sliceformer (arXiv:2604.26961, April 2026, accepted ACL 2026):** This paper is the closest to your idea conceptually. It proposes **dataflow-aware pretraining** that uses Data Flow Graphs (DFGs) to teach language models data dependencies through:
- Dataflow-preserving statement permutation
- Dataflow-aware span corruption

This effectively **distills data-flow knowledge into a neural model** for the task of program slicing. It achieves up to 22% ExactMatch improvement over baselines on Java/Python benchmarks. However, it targets **program slicing** (identifying relevant statements given a variable), not context selection for code repair.

**ND-Slicer (FSE 2024):** A neural approach to dynamic program slicing using execution-aware pre-training (CodeExecutor) and a Pointer-Transformer architecture. Achieves 81.31% exact-match accuracy on predicting program slices. This demonstrates that **neural models can effectively learn to replicate data-flow-based program analysis** tasks.

**ProGraML (ICML 2021):** Uses Message Passing Neural Networks over program graphs (control + data + call relations) to learn classical dataflow analyses (liveness, reaching definitions, etc.) with 94% F1. This is foundational evidence that **neural networks can learn data-flow analysis**.

**LLMs for Program Slicing (COMPSAC 2025, arXiv:2409.12369):** Showed that off-the-shelf LLMs (GPT-4o) achieve only ~60% accuracy on program slicing with 0% exact matches -- suggesting that **pre-training alone is insufficient** and that explicit data-flow training/distillation is needed.

---

## 5. Knowledge Distillation for Code Repair (2025-2026)

No paper was found that specifically combines knowledge distillation with code repair in the way you propose. The closest works are:
- **DISCOREV** (ACM 2024): Cross-task knowledge distillation for code review tasks
- **Knowledge distillation for code understanding** (arXiv:2508.15423): Empirical study finding mid-sized models (7M-30M params) achieve optimal distillation efficiency, with domain-specialized teachers outperforming general ones
- **Cross-language clone detection** (2025): Uses DeepSeek-R1 as teacher for compact student models

None of these specifically distill program analysis into a model for repair context selection.

---

## 6. Tree-Sitter + Neural Models for Context Selection

**cAST (EMNLP 2025 Findings, CMU):** Uses tree-sitter AST parsing for structure-aware code chunking. Improves Recall@5 by 4.3 points on RepoEval and Pass@1 by 2.67 on SWE-bench. However, it is purely a chunking strategy -- no neural learning of context relevance is involved.

**Codebase-Memory (arXiv:2603.27277):** Tree-sitter-based knowledge graphs with SQL-backed graph queries. Captures static structure only (call graphs, community detection) with no neural component and no data-flow/control-flow analysis.

**Tree-sitter MCP tools (2026):** Multiple tools (AiDex, CodeRLM, mcp-server-tree-sitter) use tree-sitter for code indexing to reduce token usage for AI agents, but none learn a neural context selector from these signals.

---

## Summary Assessment: Novelty of Your Proposed Idea

| Aspect | Existing Coverage | Your Novel Contribution |
|--------|------------------|------------------------|
| Neural context filtering for code | SWE-Pruner, CODEFILTER | Covered but with LLM-based signals only |
| Learning data-flow analysis | ProGraML, Sliceformer, ND-Slicer | Exists for slicing, NOT for repair context |
| Distilling analysis into small models | SWE-Pruner (LLM teacher) | No one distills *static analysis* specifically |
| Code repair context selection | RepoRepair (documentation-based) | No data-flow-grounded approach |

**The gap your paper fills:** No existing work distills **data-flow analysis specifically as a training signal for a neural context selector in code repair**. The closest works either:
- Learn data-flow for program slicing (Sliceformer, ND-Slicer) but don't apply it to repair context selection
- Do neural context pruning (SWE-Pruner) but use LLM-generated signals rather than program analysis
- Use structural analysis (RepoRepair, cAST) but without neural learning of relevance

**The strongest competitor to differentiate against is SWE-Pruner** (same architecture concept: small neural filter for coding agents) and **Sliceformer** (same knowledge source: data-flow graphs distilled into neural models, but for a different downstream task).

---

Sources:
- [CODEFILTER - Impact-driven Context Filtering](https://arxiv.org/abs/2508.05970)
- [CODEFILTER on OpenReview (COLM25)](https://openreview.net/forum?id=0Y2zXLFBji)
- [SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents](https://arxiv.org/abs/2601.16746)
- [SWE-Pruner HTML](https://arxiv.org/html/2601.16746v1)
- [RepoRepair: Leveraging Code Documentation for Repository-Level APR](https://arxiv.org/abs/2603.01048)
- [Sliceformer: Dataflow-Aware Pretraining for Program Slicing (ACL 2026)](https://arxiv.org/abs/2604.26961)
- [ND-Slicer: Predictive Program Slicing (FSE 2024)](https://dl.acm.org/doi/10.1145/3643739)
- [ProGraML: Graph-based Deep Learning for Program Analysis](https://arxiv.org/abs/2003.10536)
- [Program Slicing in the Era of LLMs](https://arxiv.org/abs/2409.12369)
- [SLICET5: Static Program Slicing Using Language Models](https://arxiv.org/abs/2509.17338)
- [cAST: Enhancing Code RAG with AST Chunking (EMNLP 2025)](https://arxiv.org/abs/2506.15655)
- [Codebase-Memory: Tree-Sitter Knowledge Graphs](https://arxiv.org/html/2603.27277v1)
- [Knowledge Distillation for Code Understanding](https://arxiv.org/abs/2508.15423)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f35cf107-ede2-478c-a606-3dc81b3f9369",
  "isSidechain": true,
  "agentId": "aa38f008d49a94408",
  "requestId": "req_011CauKDhg8aSKYADu8aMtFT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9113aa5b-f322-4ca3-9727-0957339b5c83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hwsi5HEzatH2NMMd4V4STe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 493,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 32221,
      "output_tokens": 2773,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 709
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 493,
          "output_tokens": 2773,
          "cache_read_input_tokens": 32221,
          "cache_creation_input_tokens": 709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 709,
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
