# Research conversation: You are helping review an ML paper about routing retrieval configurations for code repair. The paper proposes learning t

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aab2b9a0d81eac379.jsonl`
- **Structured JSON:** [`dcce6a0fc1d705dfefee.json`](../../sessions/dc/dcce6a0fc1d705dfefee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

59 recorded events

### User

_source line 1 · 2026-05-11T23:55:34.486Z_

You are helping review an ML paper about routing retrieval configurations for code repair. The paper proposes learning to select (fault-localization granularity, context budget) per issue for code repair.

Search for papers the generator may have MISSED. Use WebSearch for each of these queries:

1. "adaptive retrieval configuration code repair 2025 2026" — any recent work on adaptive retrieval for code repair
2. "fault localization granularity adaptive selection" — anyone else doing adaptive FL granularity
3. "SWE-bench routing configuration selection 2026" — routing for SWE-bench tasks
4. "retrieval augmented code repair adaptive context 2025 2026"
5. "code repair context window optimization"
6. "mix of experts code repair retrieval"
7. "ICSE 2026 accepted papers adaptive code repair" or "ASE 2025 adaptive code repair"
8. "learning to route retrieval code" — exact topic match

For each search, report the most relevant results — especially papers that do the SAME or very similar thing to what GranRoute proposes (learning to select retrieval configuration for code tasks). Focus on 2025-2026 papers. Report titles, venues, and key findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "de365e01-68f9-4a64-9226-251a7140e5e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:55:34.488Z_

```json
{
  "parentUuid": "de365e01-68f9-4a64-9226-251a7140e5e7",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
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
  "uuid": "49889104-26db-42cd-9954-b20eb7ff2a3d",
  "timestamp": "2026-05-11T23:55:34.488Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:55:37.457Z_



I'll search for potentially missed related work across all these queries. Let me start by loading the WebSearch tool, then run all searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49889104-26db-42cd-9954-b20eb7ff2a3d",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawggY3toqdqEB4dX738o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adcaca54-249c-4b03-9589-8207144e50c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01724W5M41kNFLcm6cXRoJo5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 826,
      "cache_read_input_tokens": 8223,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 826
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 826,
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

### Tool call

_source line 4 · 2026-05-11T23:55:37.504Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01D5dJvobKkzLPba4muKFAxo`</summary>

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
  "parentUuid": "adcaca54-249c-4b03-9589-8207144e50c2",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawggY3toqdqEB4dX738o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39104ffc-be4d-44dc-a3fe-5b3a28f8dd85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01724W5M41kNFLcm6cXRoJo5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 826,
      "cache_read_input_tokens": 8223,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 826
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 826,
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

_source line 5 · 2026-05-11T23:55:37.509Z_

<details><summary>↩ Tool result · `toolu_01D5dJvobKkzLPba4muKFAxo`</summary>

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
  "parentUuid": "39104ffc-be4d-44dc-a3fe-5b3a28f8dd85",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "3a513abc-6d72-4a1e-abb0-7acd9f93ec65",
  "sourceToolAssistantUUID": "39104ffc-be4d-44dc-a3fe-5b3a28f8dd85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:55:40.418Z_



Now let me run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a513abc-6d72-4a1e-abb0-7acd9f93ec65",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawggmH8PA3m4W4gm8rQE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b082fafa-5c1d-4170-b22f-1917f238264c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019F1eqm7PErAPXhmtjxbadu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 7 · 2026-05-11T23:55:40.863Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012XzPWuwdkDmGRPtjHqgTCs`</summary>

```json
{
  "query": "adaptive retrieval configuration code repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b082fafa-5c1d-4170-b22f-1917f238264c",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawggmH8PA3m4W4gm8rQE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f020ea9-dbc9-46e7-881c-8dde40899258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019F1eqm7PErAPXhmtjxbadu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 9049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 8 · 2026-05-11T23:55:48.419Z_

<details><summary>↩ Tool result · `toolu_012XzPWuwdkDmGRPtjHqgTCs`</summary>

```text
Web search results for query: "adaptive retrieval configuration code repair 2025 2026"

Links: [{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/html/2603.01048v1"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-026-09751-w"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"[2503.06510] Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://arxiv.org/abs/2503.06510"},{"title":"A survey on large language models for software engineering","url":"https://files.sciengine.com/gridfs/1987700388211458048/edit_SCIS-2025-0100-appendix.pdf"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"}]

Based on the search results, I found several relevant papers and resources on adaptive retrieval configuration and code repair from 2025-2026:

## Key Findings:

**Recent Research Papers:**

1. **RELREPAIR** - A novel approach that retrieves relevant code to enhance automated program repair, through a specialized RAG approach tailored to program repair tasks. The system uses adaptive parameter adjustment for retrieval optimization.

2. **ReCode** - Integrating algorithmic categorization with the model's semantic modeling towards defective code to significantly enhance the contextual relevance of retrieved in-context exemplars and support more accurate and adaptive code repair generation.

3. **RepoRepair** - A streamlined two-stage pipeline—first retrieving relevant files via embedding models, then iteratively generating repairs based on the top retrieved files—which shares key design principles with retrieval-augmented, context-aware repair.

4. **Comprehensive Survey** - A comprehensive survey mapping the design space across four paradigms (fine-tuning, prompting, procedural pipelines, and agentic frameworks), incorporating cross-cutting Retrieval Augmented Generation (RAG) and Analysis Augmented Generation (AAG) enhancements, covering papers from January 2022 to June 2025.

5. **Adaptive Program Repair** - Automated Program Repair (APR) is a task to automatically generate patches for the buggy code, with recent work exploring adaptive approaches with bug localization and preference learning.

These recent works demonstrate an active research area focused on improving code repair through adaptive retrieval strategies and configuration mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f020ea9-dbc9-46e7-881c-8dde40899258",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "05d1f01e-2555-4d9e-92e8-75550806d2f4",
  "sourceToolAssistantUUID": "9f020ea9-dbc9-46e7-881c-8dde40899258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-11T23:55:50.701Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BA7RFdsd4QL2aWnBRuAB2x`</summary>

```json
{
  "query": "fault localization granularity adaptive selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05d1f01e-2555-4d9e-92e8-75550806d2f4",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawghaLqQVmtbGpaqMGmF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62aaa191-7c22-476f-a7d9-9d43e6285b6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sAr9smLBUBkt5Ght4LJQx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 987,
      "cache_read_input_tokens": 10471,
      "output_tokens": 59,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 987
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 59,
          "cache_read_input_tokens": 10471,
          "cache_creation_input_tokens": 987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 987,
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

_source line 10 · 2026-05-11T23:55:58.179Z_

<details><summary>↩ Tool result · `toolu_01BA7RFdsd4QL2aWnBRuAB2x`</summary>

```text
Web search results for query: "fault localization granularity adaptive selection"

Links: [{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167v1"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"Software Fault Localization through Aggregation-Based Neural Ranking for Static and Dynamic Features Selection - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8587821/"},{"title":"[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/abs/2604.00167"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale","url":"https://arxiv.org/pdf/2604.00167"},{"title":"Fault Localization - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/computer-science/fault-localization"},{"title":"What to Blame? On the Granularity of Fault Localization for Deep Neural Networks | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9700265/"},{"title":"Variable-based Fault Localization via Enhanced Decision Tree | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3624741"},{"title":"An Empirical Study of Fault Localization in Python Programs","url":"https://arxiv.org/pdf/2305.19834"}]

Based on the search results, here's what I found about fault localization granularity adaptive selection:

## Overview

Fault localization granularity refers to the kinds of program entity that a fault localization (FL) technique ranks. Fault localization techniques consider different granularities such as function-level (also called method-level) and module-level (also called file-level).

## Adaptive Granularity Selection

Recent research has identified the need for adaptive granularity selection. While function-level granularity dominates on average, the relative ordering across granularities shifts with difficulty tier, suggesting that the optimal level of localization granularity is not fixed but instance-dependent, which motivates investigation into whether difficulty-aware or adaptive granularity selection could improve repair outcomes.

Different configurations resolve different subsets of instances, indicating that no single strategy is universally optimal, and some bugs benefit from broader context while others require more focused localization, suggesting that adaptive or ensemble context strategies, which dynamically adjust localization based on bug characteristics, may outperform any fixed configuration.

## Key Findings

Different granularities benefit from complementary localization strategies, with the best performance coming from combining LLM-based file and element context with precise "buggy lines", showing that broader context helps at higher levels, while line-level localization should remain precise.

The research suggests that rather than using a single fixed granularity level, adaptive approaches that adjust the level of detail based on the specific characteristics of the bug or repair task may be more effective.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62aaa191-7c22-476f-a7d9-9d43e6285b6f",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "c8a3d733-ed0f-4740-b41a-e2896c4e56e1",
  "sourceToolAssistantUUID": "62aaa191-7c22-476f-a7d9-9d43e6285b6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-11T23:56:00.319Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016ktVLuVWAtvfyjDVSy9LNq`</summary>

```json
{
  "query": "SWE-bench routing configuration selection 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8a3d733-ed0f-4740-b41a-e2896c4e56e1",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgiHLfucmkApawQGytc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae8b89bf-bec9-47ad-9256-7889886125dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wkttymSGk1xKGEDXSuMQE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 908,
      "cache_read_input_tokens": 11458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 908,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:56:08.705Z_

<details><summary>↩ Tool result · `toolu_016ktVLuVWAtvfyjDVSy9LNq`</summary>

```text
Web search results for query: "SWE-bench routing configuration selection 2026"

Links: [{"title":"LLM Benchmarks 2026: 30+ Models Ranked — MMLU, SWE-bench, Arena Elo & Pricing","url":"https://iternal.ai/llm-selection-guide"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench 2026: Claude 77.2% vs GPT-5 74.9% | Full Leaderboard | Local AI Master","url":"https://localaimaster.com/models/swe-bench-explained-ai-benchmarks"},{"title":"SWE-Bench Live Leaderboard Q2 2026: Complete Deep Analysis","url":"https://www.digitalapplied.com/blog/swe-bench-live-leaderboard-q2-2026-analysis"},{"title":"SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 Leaderboard","url":"https://www.morphllm.com/swe-benchmark"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"Overview - SWE-bench","url":"https://www.swebench.com/SWE-bench/"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-Bench 2026: Claude Opus 4.7 Wins 87.6% vs GPT-5.3 85.0% - TokenMix Blog","url":"https://tokenmix.ai/blog/swe-bench-2026-claude-opus-4-7-wins"},{"title":"SWE-rebench Leaderboard","url":"https://swe-rebench.com/"}]

Based on the search results, here's what I found about SWE-bench routing configuration selection in 2026:

## Model Routing Strategy for SWE-bench

Model routing sends different requests to different models based on task complexity, latency requirements, and cost constraints. A well-designed routing system can reduce costs by 50-80% while maintaining quality.

### Practical Routing Approach

The practical routing play is to use Opus 4.7 for hard tasks where success rate matters, fall back to Qwen3.6 Plus or DeepSeek V4 for bulk bug fixes. Qwen3.6 Plus and DeepSeek V4 offer the cheapest cost-per-successful-fix, roughly 7× cheaper than Opus 4.7 while only 10-12 points behind on success rate. For production code-fixing pipelines where success rate differences of 7-10% are tolerable, the cheap options dominate on dollars per merged PR.

### Configuration Considerations

Important factors when selecting routing configurations include:

- Models with 1M context (Opus 4.7, Gemini) handle large repos better regardless of their benchmark numbers.
- Production systems like Cursor, Claude Code, and Aider stack model calls with tool use, retrieval, and human-in-the-loop review. A 3-point benchmark gap often disappears when both models run inside the same scaffolding.
- Agent scaffolding around a model such as iteration budget, tool availability, reflection loops, and repository navigation heuristics can swing results by ten to twenty percentage points on identical underlying models.

The key insight is that routing decisions should balance model performance on SWE-bench scores with cost efficiency and task-specific requirements rather than simply choosing the highest-scoring model for all tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae8b89bf-bec9-47ad-9256-7889886125dd",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "78981045-a36e-467b-9769-d6e279745ac0",
  "sourceToolAssistantUUID": "ae8b89bf-bec9-47ad-9256-7889886125dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-11T23:56:10.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YBTvodnySY2QbGBakUN2T5`</summary>

```json
{
  "query": "retrieval augmented code repair adaptive context 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78981045-a36e-467b-9769-d6e279745ac0",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011Cawgj4LMXoZLCxCXQJMw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58a37b7c-5255-4b0b-a35a-08e67b95a457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QH7g3cGpbyznn9xAxZZoq6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 958,
      "cache_read_input_tokens": 12366,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 958
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 12366,
          "cache_creation_input_tokens": 958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 958,
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

_source line 14 · 2026-05-11T23:56:18.436Z_

<details><summary>↩ Tool result · `toolu_01YBTvodnySY2QbGBakUN2T5`</summary>

```text
Web search results for query: "retrieval augmented code repair adaptive context 2025 2026"

Links: [{"title":"[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/abs/2510.04905"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"Retrieval-augmented code completion for local projects using large language models | Expert Systems with Applications: An International Journal","url":"https://dl.acm.org/doi/10.1016/j.eswa.2025.128596"},{"title":"RAG is DEAD!. Retrieval-Augmented Generation ruled… | by Reliable Data Engineering | Medium","url":"https://medium.com/@reliabledataengineering/rag-is-dead-and-why-thats-the-best-news-you-ll-hear-all-year-0f3de8c44604"},{"title":"Enhancing Large Language Models with Retrieval Augmented Generation for Software Testing and Inspection Automation","url":"https://arxiv.org/html/2604.15270"},{"title":"[2504.20434] ARCS: Agentic Retrieval-Augmented Code Synthesis with Iterative Refinement","url":"https://arxiv.org/abs/2504.20434"},{"title":"Retrieval-augmented code completion for local projects using large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425022158"}]

Based on the web search results, here's what I found regarding retrieval-augmented code repair with adaptive context in 2025-2026:

## Key Research Developments

ReCode is an approach that analyzes queries to infer algorithm types and retrieves relevant exemplars from an algorithm-specific knowledge corpus, enhancing contextual relevance of retrieved in-context exemplars for more accurate and adaptive code repair generation.

Automatic Program Repair (APR) aims to automatically fix software defects, and recent studies have demonstrated impressive results in utilizing Large Language Models for software bug fixing. ReAPR (Retrieval-Augmented Program Repair) is an approach for automatic program repair via retrieval-augmented large language models published in 2025.

## Broader Context on RAG in Code Applications

Retrieval-Augmented Generation (RAG) has emerged as a powerful paradigm that integrates external retrieval mechanisms with LLMs, enhancing context-awareness and scalability. Recent works explore iterative or agent-style RACG frameworks where retrieval and generation are conducted in multi-step loops with intermediate reasoning, tool execution, or reflection, further enhancing the adaptability and robustness of RACG systems in complex repository-scale environments.

ARCS (Agentic Retrieval-Augmented Code Synthesis) operates through a synthesize-execute-repair loop that retrieves relevant code context before generation, proposes candidates, executes them against tests, and repairs based on execution feedback, with a retrieval-before-generation design that reduces hallucination and accelerates convergence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58a37b7c-5255-4b0b-a35a-08e67b95a457",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "addf07bc-1c80-4c19-9f9f-9f7b9c5932a9",
  "sourceToolAssistantUUID": "58a37b7c-5255-4b0b-a35a-08e67b95a457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-11T23:56:20.240Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015UMYpdZZeKzuWkC7PqoWUc`</summary>

```json
{
  "query": "code repair context window optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "addf07bc-1c80-4c19-9f9f-9f7b9c5932a9",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgjmxtaD4cfyyfT9ZRB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf05168d-a955-425c-84a9-82507e9ebcfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tp2uDHXeSPMDWAfa888ALW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 996,
      "cache_read_input_tokens": 13324,
      "output_tokens": 56,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 996
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 56,
          "cache_read_input_tokens": 13324,
          "cache_creation_input_tokens": 996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 996,
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

_source line 16 · 2026-05-11T23:56:27.977Z_

<details><summary>↩ Tool result · `toolu_015UMYpdZZeKzuWkC7PqoWUc`</summary>

```text
Web search results for query: "code repair context window optimization"

Links: [{"title":"GitHub - mksglu/context-mode: Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 15 platforms · GitHub","url":"https://github.com/mksglu/context-mode"},{"title":"Claude Code Context Window: Optimize Your Token Usage","url":"https://claudefa.st/blog/guide/mechanics/context-management"},{"title":"Automated Program Repair via Conversation:","url":"https://lingming.cs.illinois.edu/publications/issta2024.pdf"},{"title":"claude code context window optimization | self.md","url":"https://self.md/guides/context-optimization/"},{"title":"Context Window Optimization: Techniques, Benchmarks, and Costs","url":"https://www.statsig.com/perspectives/context-window-optimization-techniques"},{"title":"Context Window Optimization Strategies | DataHub","url":"https://datahub.com/blog/context-window-optimization/"},{"title":"GitHub - scottconverse/context-mode: Context window optimization plugin for Claude Code in Cowork. Sandbox execution, FTS5 knowledge base, session continuity. 98% context reduction. · GitHub","url":"https://github.com/scottconverse/context-mode"},{"title":"context-window-optimization · GitHub Topics · GitHub","url":"https://github.com/topics/context-window-optimization"},{"title":"Releases · mksglu/context-mode","url":"https://github.com/mksglu/context-mode/releases"},{"title":"Explore the context window - Claude Code Docs","url":"https://code.claude.com/docs/en/context-window"}]

I found several relevant results about code repair context window optimization. Here's a summary of the key findings:

## Context Window Optimization for Code Repair

**Overview:**
Context Mode provides context window optimization for AI coding agents, achieving sandboxing of tool output with 98% reduction.

**Key Challenges:**
ChatRepair, an automated program repair system, faces limitations due to context window size, lacking access to project-specific information that has been shown to be important for boosting LLM repair performance.

**Optimization Strategies:**

1. **Sandboxing and Data Isolation:** Context Mode operates at the MCP protocol layer — raw data stays in a sandboxed subprocess and never enters your context window, with web pages, API responses, file analysis, and log files processed in complete isolation.

2. **Session Continuity:** Every file edit, git operation, task, error, and user decision is tracked in SQLite, and when the conversation compacts, context-mode doesn't dump data back into context but instead indexes events into FTS5 and retrieves only what's relevant via BM25 search.

3. **Code-Driven Analysis:** Rather than reading files into context to perform analysis, the LLM should program the analysis — agents write scripts that do the counting and only output the result, replacing ten tool calls and saving 100x context.

4. **Conversation-Based Repair:** ChatRepair introduces a conversation-based repair paradigm to incorporate both patch generation history with immediate validation feedback to perform repair.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf05168d-a955-425c-84a9-82507e9ebcfb",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "04eb9070-1613-467d-af52-bdb6e8aea66a",
  "sourceToolAssistantUUID": "cf05168d-a955-425c-84a9-82507e9ebcfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-11T23:56:29.871Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016s8xnopbNWsSfnCL8KxEib`</summary>

```json
{
  "query": "mixture of experts code repair retrieval routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04eb9070-1613-467d-af52-bdb6e8aea66a",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgkUh6qLpqyQ4zYvDfY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53e9973a-2ca9-4110-ad1a-709c0e1d996e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JhERPCrRb1o11arxK1C2pb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 14320,
      "output_tokens": 59,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 821
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 59,
          "cache_read_input_tokens": 14320,
          "cache_creation_input_tokens": 821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 821,
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

_source line 18 · 2026-05-11T23:56:36.499Z_

<details><summary>↩ Tool result · `toolu_016s8xnopbNWsSfnCL8KxEib`</summary>

```text
Web search results for query: "mixture of experts code repair retrieval routing"

Links: [{"title":"[2202.09368] Mixture-of-Experts with Expert Choice Routing","url":"https://arxiv.org/abs/2202.09368"},{"title":"Mixture-of-Experts with Expert Choice Routing | OpenReview","url":"https://openreview.net/forum?id=jdJo1HIVinI"},{"title":"Mixture of Experts in Large Language Models †: Corresponding author: Junhao Song (junhao.song23@imperial.ac.uk)","url":"https://arxiv.org/html/2507.11181v1"},{"title":"Mixture-of-Experts with Expert Choice Routing","url":"https://arxiv.org/pdf/2202.09368"},{"title":"Applying Mixture of Experts in LLM Architectures | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/"},{"title":"Rewiring Experts on the Fly: Continuous Rerouting for Better Online Adaptation in Mixture-of-Expert models","url":"https://arxiv.org/html/2510.14853v1"},{"title":"1 ExpertRAG: Efficient RAG with Mixture of Experts – Optimizing","url":"https://arxiv.org/pdf/2504.08744"},{"title":"Mixture-of-experts with expert choice routing | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/abs/10.5555/3600270.3600785"},{"title":"Hierarchical Mixture-of-Experts model for unified code search - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525005627"},{"title":"Mixture-of-Experts with Expert Choice Routing","url":"https://research.google/blog/mixture-of-experts-with-expert-choice-routing/"}]

Based on the search results, I found relevant information about mixture of experts with routing mechanisms. Here's what the research shows:

## Mixture of Experts with Expert Choice Routing

Sparsely-activated Mixture-of-experts (MoE) models allow the number of parameters to greatly increase while keeping the amount of computation for a given token or a given sample unchanged. However, a poor expert routing strategy can cause certain experts to be under-trained, leading to an expert being under or over-specialized.

To address this, researchers propose a heterogeneous mixture-of-experts employing an expert choice method. Instead of letting tokens select the top-k experts, experts select the top-k tokens. This method improves training convergence time by more than 2x when compared to prior work.

## Integration with Retrieval

Recent work has begun combining mixture of experts with retrieval mechanisms. Modern systems increasingly integrate expert routing with paradigms like retrieval, instruction tuning, and agent-based control, indicating that MoE now plays a central role in large-scale AI development.

## Code Search Application

More specifically for code-related tasks, a hierarchical mixture-of-experts (HMoE) model has been introduced to enhance the representation and retrieval processes in code search tasks, incorporating a hierarchical-level architecture with Macro Mixture-of-Experts and Micro Mixture-of-Experts strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53e9973a-2ca9-4110-ad1a-709c0e1d996e",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "c67d02b0-1ac7-433a-b5a3-30a07746175d",
  "sourceToolAssistantUUID": "53e9973a-2ca9-4110-ad1a-709c0e1d996e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-11T23:56:38.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vg47fqWfhBVyVYuUmcj4ur`</summary>

```json
{
  "query": "ICSE 2026 accepted papers adaptive code repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c67d02b0-1ac7-433a-b5a3-30a07746175d",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011Cawgm7ApkQktjHUzokaMF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2a9c334-8de3-436e-9127-93bc7ff221e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rv3z9J1mpRU3cdHnPsnjrP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 890,
      "cache_read_input_tokens": 15141,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 890
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 15141,
          "cache_creation_input_tokens": 890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 890,
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

_source line 20 · 2026-05-11T23:56:43.388Z_

<details><summary>↩ Tool result · `toolu_01Vg47fqWfhBVyVYuUmcj4ur`</summary>

```text
Web search results for query: "ICSE 2026 accepted papers adaptive code repair"

Links: [{"title":"ICSE 2026 - Journal-first Papers - ICSE 2026","url":"https://conf.researchr.org/track/icse-2026/icse-2026-journal-first-papers"},{"title":"ICSE 2026 - Research Track - ICSE 2026","url":"https://conf.researchr.org/track/icse-2026/icse-2026-research-track"},{"title":"Accepted Papers | LLM4Code 2026","url":"https://llm4code.github.io/papers/"},{"title":"ICSE 2025 - Research Track - ICSE 2025","url":"https://conf.researchr.org/track/icse-2025/icse-2025-research-track"},{"title":"ICSE 2026, Research Track","url":"https://icse2026.hotcrp.com/"},{"title":"ICSE 2026 - Future of Software Engineering - ICSE 2026","url":"https://conf.researchr.org/track/icse-2026/icse-2026-future-of-software-engineering"},{"title":"FORGE 2026 - Research Papers - conf.researchr.org","url":"https://conf.researchr.org/track/forge-2026/forge-2026-papers"},{"title":"Call for Papers | LLM4Code 2026","url":"https://llm4code.github.io/call/"},{"title":"ICSE 2026 - conf.researchr.org","url":"https://conf.researchr.org/home/icse-2026"},{"title":"ICSE 2026 - New Ideas and Emerging Results (NIER) - ICSE 2026","url":"https://conf.researchr.org/track/icse-2026/icse-2026-nier"}]

Based on the search results, I found general information about ICSE 2026 accepted papers, but the results don't contain a specific list of papers related to "adaptive code repair."

Here's what I found about ICSE 2026 accepted papers:

After peer review, 72 papers were directly accepted, and 88 were accepted after major revision, with a total of 321 papers accepted for ICSE 2026 out of 1469 submissions, representing a 19.8% acceptance rate.

The search results show that ICSE 2026 has various tracks including the Research Track, Journal-first Papers, Demonstrations, and several specialized workshops like LLM4Code 2026 and FORGE 2026. The FORGE 2026 workshop specifically focuses on AI Foundation Models and Software Engineering, and LLMs achieved remarkable performance in various tasks, including code generation, testing, code review, and program repair.

However, the search results don't provide access to the complete list of accepted papers or specifically identify which papers focus on adaptive code repair. To find papers on that specific topic, you would need to visit the ICSE 2026 conference website directly or access the full proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2a9c334-8de3-436e-9127-93bc7ff221e7",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "1acf908c-7175-498b-853b-b55fcec6a457",
  "sourceToolAssistantUUID": "a2a9c334-8de3-436e-9127-93bc7ff221e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-11T23:56:46.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ETpqo4622sepGGbmzjqMrS`</summary>

```json
{
  "query": "learning to route retrieval code generation repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1acf908c-7175-498b-853b-b55fcec6a457",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgmdTUXLwxYU5EJoY94",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8edc34b3-2398-4149-b00f-4bdf6c9ed306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQhFHu42oWnu48HXDcQRs1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 942,
      "cache_read_input_tokens": 16031,
      "output_tokens": 59,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 59,
          "cache_read_input_tokens": 16031,
          "cache_creation_input_tokens": 942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 942,
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

_source line 22 · 2026-05-11T23:56:54.108Z_

<details><summary>↩ Tool result · `toolu_01ETpqo4622sepGGbmzjqMrS`</summary>

```text
Web search results for query: "learning to route retrieval code generation repair"

Links: [{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330"},{"title":"Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/html/2601.08545.pdf"},{"title":"Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback","url":"https://arxiv.org/html/2601.00509"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2505.23052v2"},{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation | Proceedings of the 34th ACM International Conference on Information and Knowledge Management","url":"https://doi.org/10.1145/3746252.3761035"},{"title":"[2509.02330] ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2509.02330"},{"title":"RAILS: Retrieval-Augmented Intelligence for Learning Software Development","url":"https://arxiv.org/html/2506.22742"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained","url":"https://arxiv.org/pdf/2509.02330"}]

The web search results provide information about several relevant research papers and approaches in the area of retrieval-augmented code generation and repair. Here's what I found:

## Key Research Areas

### ReCode: Fine-Grained Retrieval-Augmented Code Repair
ReCode is a fine-grained retrieval-augmented in-context learning framework designed for accurate and efficient code repair. It introduces two key innovations: (1) an algorithm-aware retrieval strategy that narrows the search space using preliminary algorithm type predictions; and (2) a modular dual-encoder architecture that separately processes code and textual inputs, enabling fine-grained semantic matching between input and retrieved contexts.

### RAGRouter: Learning to Route Queries in RAG
RAGRouter is the first RAG-aware routing method that leverages contrastive learning to capture knowledge representation shifts induced by external documents, enabling effective routing decisions. This is the first work exploring LLM routing in the RAG setting.

### Learner-Tailored Program Repair (LSGen)
LSGen proposes an iterative retrieval enhancement method, which iteratively retrieves repair strategies that match the current generated incorrect code, thereby improving both usability and repair performance.

### Other Approaches
Some systems propose a retrieval-augmented, multi-tool repair workflow in which a code-generating LLM iteratively refines its outputs using compiler diagnostics, CodeQL security scanning, and KLEE symbolic execution, with a lightweight embedding model used for semantic retrieval of previously successful repairs.

These research works address the challenge of using retrieval mechanisms to improve code generation and repair, with emphasis on learning effective routing strategies and retrieval approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8edc34b3-2398-4149-b00f-4bdf6c9ed306",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "1743f7a8-4b31-432a-8556-34699beb15cc",
  "sourceToolAssistantUUID": "8edc34b3-2398-4149-b00f-4bdf6c9ed306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-11T23:56:56.345Z_

Now let me do a few more targeted searches to dig deeper into the most relevant hits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1743f7a8-4b31-432a-8556-34699beb15cc",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgnQRfznofoteKsGsWV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2675e64-1239-4fdd-a907-79c2239567b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMaqi3q1UjrDK4VdTdoEXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 16973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 944,
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

_source line 24 · 2026-05-11T23:56:56.943Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VUbroRAECZhVnTqdTrEhuP`</summary>

```json
{
  "query": "RAGRouter learning to route queries retrieval augmented language models 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2675e64-1239-4fdd-a907-79c2239567b8",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgnQRfznofoteKsGsWV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c017b0e-0516-48a1-b1c1-0bd23f54b2c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMaqi3q1UjrDK4VdTdoEXH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 16973,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 16973,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 944,
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

_source line 25 · 2026-05-11T23:57:04.529Z_

<details><summary>↩ Tool result · `toolu_01VUbroRAECZhVnTqdTrEhuP`</summary>

```text
Web search results for query: "RAGRouter learning to route queries retrieval augmented language models 2025"

Links: [{"title":"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models | OpenReview","url":"https://openreview.net/forum?id=4VKVUmE1I8"},{"title":"[2505.23052] RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://arxiv.org/abs/2505.23052"},{"title":"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2505.23052v2"},{"title":"NeurIPS Poster RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119935"},{"title":"RAGRouter: Learning to Route Queries to Multiple ...","url":"https://arxiv.org/pdf/2505.23052"},{"title":"[PDF] RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RAGRouter:-Learning-to-Route-Queries-to-Multiple-Zhang-Liu/bbc2dcac1d4e52e607dc17104414b6b0cee5fb44"},{"title":"Query Routing for Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2505.23052v1"},{"title":"GitHub - OwwO99/RAGRouter: Code and data for \"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models\" · GitHub","url":"https://github.com/OwwO99/RAGRouter"},{"title":"RAGRouter: Retrieval-Augmented Routing","url":"https://www.emergentmind.com/topics/ragrouter"},{"title":"Learning Agent Routing From Early Experience","url":"https://arxiv.org/html/2605.07180"}]

Based on the search results, here's what I found about RAGRouter:

## Overview

RAGRouter is a RAG-aware routing design that leverages document embeddings and RAG capability embeddings with contrastive learning to capture knowledge representation shifts and enable informed routing decisions.

## Problem Statement

Retrieval-Augmented Generation (RAG) significantly improves the performance of Large Language Models (LLMs) on knowledge-intensive tasks. However, varying response quality across LLMs under RAG necessitates intelligent routing mechanisms, which select the most suitable model for each query from multiple retrieval-augmented LLMs via a dedicated router model.

External documents dynamically affect LLMs' ability to answer queries, while existing routing methods, which rely on static parametric knowledge representations, exhibit suboptimal performance in RAG scenarios.

## Key Innovation

The work formally defines the new retrieval-augmented LLM routing problem, incorporating the influence of retrieved documents into the routing framework.

## Results

Extensive experiments on diverse knowledge-intensive tasks and retrieval settings, covering open and closed-source LLMs, show that RAGRouter outperforms the best individual LLM and existing routing methods. RAGRouter outperforms the best individual LLM by 3.61% on average and existing routing methods by 3.29%–9.33%.

With an extended score-threshold-based mechanism, it also achieves strong performance-efficiency trade-offs under low-latency constraints.

## Publication

The paper was published on September 18, 2025 (last modified October 29, 2025) and is a NeurIPS 2025 poster.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c017b0e-0516-48a1-b1c1-0bd23f54b2c3",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "606554b8-6a04-4d3b-88a5-ee464eed3d19",
  "sourceToolAssistantUUID": "2c017b0e-0516-48a1-b1c1-0bd23f54b2c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-11T23:57:07.201Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lg6PFmdQ79wxMtDANf2DWJ`</summary>

```json
{
  "query": "\"ReCode\" fine-grained retrieval augmented code repair algorithm-aware CIKM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "606554b8-6a04-4d3b-88a5-ee464eed3d19",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgoAzKAab647BjvAaKQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44ce4032-6979-4906-a164-721648efed75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vY3SZB4TsHr1ugaizHcmb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1000,
      "cache_read_input_tokens": 17917,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1000
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 17917,
          "cache_creation_input_tokens": 1000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1000,
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

_source line 27 · 2026-05-11T23:57:13.538Z_

<details><summary>↩ Tool result · `toolu_01Lg6PFmdQ79wxMtDANf2DWJ`</summary>

```text
Web search results for query: ""ReCode" fine-grained retrieval augmented code repair algorithm-aware CIKM"

Links: [{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation | Proceedings of the 34th ACM International Conference on Information and Knowledge Management","url":"https://doi.org/10.1145/3746252.3761035"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained","url":"https://arxiv.org/pdf/2509.02330"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250902330Z/abstract"},{"title":"[2509.02330] ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2509.02330"},{"title":"[Literature Review] ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://www.themoonlight.io/en/review/recode-improving-llm-based-code-repair-with-fine-grained-retrieval-augmented-generation"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Accelerating Automatic Program Repair with Dual Retrieval-Augmented Fine-Tuning and Patch Generation on Large Language Models","url":"https://arxiv.org/html/2507.10103"},{"title":"Retrieval-augmented code completion for local projects using large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425022158"}]

I found comprehensive information about ReCode. Here's what the search reveals:

## ReCode: Overview

ReCode is a fine-grained retrieval-augmented generation framework that constructs modular representations for both source code and its accompanying textual descriptions. It is designed as a fine-grained retrieval-augmented in-context learning framework for accurate and efficient code repair.

## Key Innovations

ReCode introduces two key innovations: (1) an algorithm-aware retrieval strategy that narrows the search space using preliminary algorithm type predictions; and (2) a modular dual-encoder architecture that separately processes code and textual inputs, enabling fine-grained semantic matching between input and retrieved contexts.

**Algorithm-Aware Retrieval:** ReCode uses the LLM to analyze the user's query to infer the algorithm type, which is then utilized to retrieve the most relevant exemplars from a pre-constructed algorithm-specific knowledge corpus.

## Performance and Benchmarks

Extensive experiments on RACodeBench and competitive programming datasets show that ReCode outperforms existing methods in both repair accuracy and inference efficiency. The authors also propose RACodeBench, a new benchmark constructed from real-world user-submitted buggy code, which addresses the limitations of synthetic benchmarks and supports realistic evaluation.

## Publication

This work was published in CIKM '25: Proceedings of the 34th ACM International Conference on Information and Knowledge Management.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44ce4032-6979-4906-a164-721648efed75",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "31877e49-9548-47a5-bac1-5a1036749e23",
  "sourceToolAssistantUUID": "44ce4032-6979-4906-a164-721648efed75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-11T23:57:16.079Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PMKeAbRMLHGkokXgKGPtG7`</summary>

```json
{
  "query": "\"Less is More\" adaptive program repair bug localization preference learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31877e49-9548-47a5-bac1-5a1036749e23",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgoqZnt6SMCVMAv3vS8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8dc0a25-33d0-497b-b79a-736d9af2541b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NvdUmPhcmLw1W5Phg6t4N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 18917,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 986
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 18917,
          "cache_creation_input_tokens": 986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 986,
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

_source line 29 · 2026-05-11T23:57:22.924Z_

<details><summary>↩ Tool result · `toolu_01PMKeAbRMLHGkokXgKGPtG7`</summary>

```text
Web search results for query: ""Less is More" adaptive program repair bug localization preference learning 2025"

Links: [{"title":"[2503.06510] Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://arxiv.org/abs/2503.06510"},{"title":"Less Is More: Adaptive Program Repair with Bug Localization and Preference Learning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/31988"},{"title":"Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://arxiv.org/html/2503.06510"},{"title":"Less is More: Adaptive Program Repair","url":"https://arxiv.org/pdf/2503.06510"},{"title":"GitHub - zhenlongDai/AdaPatcher: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://github.com/zhenlongDai/AdaPatcher"},{"title":"(PDF) Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://www.researchgate.net/publication/389715232_Less_is_More_Adaptive_Program_Repair_with_Bug_Localization_and_Preference_Learning"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"[Literature Review] Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://www.themoonlight.io/en/review/less-is-more-adaptive-program-repair-with-bug-localization-and-preference-learning"},{"title":"Computer Science Mar 2025","url":"https://arxiv.org/list/cs/2025-03?skip=3300"},{"title":"Jingyuan Chen's research works | Zhejiang University and other places","url":"https://www.researchgate.net/scientific-contributions/Jingyuan-Chen-2282216795"}]

I found the paper! Here's what the search revealed:

## "Less is More: Adaptive Program Repair with Bug Localization and Preference Learning"

This paper was authored by Zhenlong Dai, Bingrui Chen, Zhuoluo Zhao, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, and Jingyuan Chen, and was published in the Proceedings of the AAAI Conference on Artificial Intelligence in 2025.

### Core Contribution

The paper introduces a novel task called AdaPR (Adaptive Program Repair) and proposes a two-stage approach called AdaPatcher (Adaptive Patch Generator) to enhance program repair while maintaining consistency.

### Problem Being Addressed

While most research focuses on generating correct patches, the paper addresses the overlooked challenge of consistency between fixed code and original buggy code, specifically how to conduct adaptive bug fixing and generate patches with minimal modifications.

### Two-Stage Approach

1. **Bug Localization Stage**: The first stage utilizes a Bug Locator with self-debug learning to accurately pinpoint bug locations.

2. **Program Repair Stage**: The second stage trains a Program Modifier to ensure consistency between the post-modified fixed code and the pre-modified buggy code.

The Program Modifier is enhanced with a location-aware repair learning strategy to generate patches based on identified buggy lines, a hybrid training strategy for selective reference and an adaptive preference learning to prioritize fewer changes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8dc0a25-33d0-497b-b79a-736d9af2541b",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "a2169f97-db1f-405c-8154-df3f9aabc6d0",
  "sourceToolAssistantUUID": "e8dc0a25-33d0-497b-b79a-736d9af2541b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-11T23:57:25.306Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HpLYNnNpuzHkqWdcW8TtTq`</summary>

```json
{
  "query": "fault localization granularity impact repository code repair arxiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2169f97-db1f-405c-8154-df3f9aabc6d0",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgpXeovzDDirj5WrXzJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b14df143-cb8e-4790-a943-733bc5e38537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KktCFT5UTLf2bNfpGHygnE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 19903,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 981
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 19903,
          "cache_creation_input_tokens": 981,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 981,
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

_source line 31 · 2026-05-11T23:57:33.031Z_

<details><summary>↩ Tool result · `toolu_01HpLYNnNpuzHkqWdcW8TtTq`</summary>

```text
Web search results for query: "fault localization granularity impact repository code repair arxiv 2604"

Links: [{"title":"[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/abs/2604.00167"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale","url":"https://arxiv.org/pdf/2604.00167"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"[2604.05481] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481"},{"title":"CI-Repair-Bench: A Repository-Aware Benchmark for Automated Patch Validation via CI Workflows","url":"https://arxiv.org/html/2604.27148"},{"title":"Exploring Generalizable Automated Program Repair with Large Language Models","url":"https://arxiv.org/html/2506.03283"},{"title":"[2601.18044] RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/abs/2601.18044"}]

I found relevant papers matching your search query. Here are the key results:

## Primary Result

The most directly relevant paper is "A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks" (arxiv 2604.00167), which shows that function-level granularity yields the highest repair rate against line-level and file-level. 

The study addresses a gap where the impact of granularity is explored to some degree for smaller datasets, but no repository-scale studies have explicitly investigated granularity under the assumption of perfect fault localization, nor conducted a systematic empirical comparison of granularity levels in isolation.

The authors propose a framework for performing such tests by modifying the localization phase of the Agentless framework to retrieve ground-truth localization data and include this as context in the prompt fed to the repair phase. However, a deeper dive suggests that the ideal granularity may in fact be task dependent.

## Related Paper

Another highly relevant work is "On the Role of Fault Localization Context for LLM-Based Program Repair" (arxiv 2604.05481), which notes that Fault Localization is a key component of LLM-based Automated Program Repair, yet its impact remains underexplored, particularly regarding how much localization is needed and whether additional context beyond the predicted buggy location is beneficial.

This study found that more context does not consistently improve repair performance, and file-level localization is the dominant factor, yielding a 15-17x improvement over a no-file baseline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b14df143-cb8e-4790-a943-733bc5e38537",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "023bdc11-95e1-405d-b6d6-c06272d01e9a",
  "sourceToolAssistantUUID": "b14df143-cb8e-4790-a943-733bc5e38537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-11T23:57:34.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EPr8DYwKnWfdvntHGBpPAX`</summary>

```json
{
  "query": "ARISE repository-level agentic fault localization program repair 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "023bdc11-95e1-405d-b6d6-c06272d01e9a",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgqGqMWQ6erQv1VteEA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edcfb646-53a0-4b79-b916-d249ddf4b487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATs8YghRKLz824phxh5UQh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 925,
      "cache_read_input_tokens": 20884,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 925
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 20884,
          "cache_creation_input_tokens": 925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 925,
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

_source line 33 · 2026-05-11T23:57:42.566Z_

<details><summary>↩ Tool result · `toolu_01EPr8DYwKnWfdvntHGBpPAX`</summary>

```text
Web search results for query: "ARISE repository-level agentic fault localization program repair 2025"

Links: [{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Evaluating Agent-based Program Repair at Google","url":"https://arxiv.org/html/2501.07531v1"},{"title":"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair Islem Bouzenia","url":"https://software-lab.org/publications/icse2025_RepairAgent.pdf"},{"title":"HAFixAgent: History-Aware Program Repair Agent","url":"https://arxiv.org/html/2511.01047"},{"title":"Agent-Based Program Repair","url":"https://www.emergentmind.com/topics/agent-based-program-repair"},{"title":"LLM-based Agents for Automated Bug Fixing: How Far Are We?","url":"https://arxiv.org/html/2411.10213v2"}]

Based on the search results, here's information about ARISE:

## ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

### Key Innovation

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest. The common limitation across existing systems is that none constructs statement-level nodes, none models definition-use relationships, and none exposes a first-class data-flow slicing primitive to the agent. ARISE addresses this gap by extending the graph to statement granularity and adding intra-procedural def-use edges.

### Performance Results

Compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points. These localization gains translate directly into repair success, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.

### Evaluation

ARISE was evaluated on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edcfb646-53a0-4b79-b916-d249ddf4b487",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "142a9abd-6b3c-4439-9960-6a2092e989d6",
  "sourceToolAssistantUUID": "edcfb646-53a0-4b79-b916-d249ddf4b487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-11T23:57:45.350Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EML8rmKfYM7sLZSmJnXbhh`</summary>

```json
{
  "query": "\"defect-type-aware adaptive program repair\" stage-wise LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "142a9abd-6b3c-4439-9960-6a2092e989d6",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgqyeGvYJ9BesgNSCxv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfa9059e-e16f-43d2-be7c-90bd49442239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AddPmq1x9RA7aCj9cDRPm7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 21809,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 945
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 21809,
          "cache_creation_input_tokens": 945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 945,
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

_source line 35 · 2026-05-11T23:57:52.492Z_

<details><summary>↩ Tool result · `toolu_01EML8rmKfYM7sLZSmJnXbhh`</summary>

```text
Web search results for query: ""defect-type-aware adaptive program repair" stage-wise LLM 2026"

Links: [{"title":"Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-026-09751-w"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Impact of Large Language Models of Code on Fault Localization | Request PDF","url":"https://www.researchgate.net/publication/391915573_Impact_of_Large_Language_Models_of_Code_on_Fault_Localization"},{"title":"Can test cases generated by large language models facilitate automated program repair? | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-026-10802-w"},{"title":"Specification-Guided Repair of Arithmetic Errors in Dafny Programs Using LLMs | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-10444-1_16"},{"title":"An empirical evaluation of pre-trained large language models for repairing declarative formal specifications | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10687-1"},{"title":"Less is More: Adaptive Program Repair","url":"https://arxiv.org/pdf/2503.06510"},{"title":"Hybrid Automated Program Repair by Combining Large Language","url":"https://xgdsmileboy.github.io/files/paper/tosem25-hybrid.pdf"},{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"},{"title":"HELO-APR: Enhancing Low-Resource Program Repair through Cross-Lingual Knowledge Transfer","url":"https://arxiv.org/html/2604.17016"}]

Based on the web search results, I found relevant information about your query:

## Defect-Type-Aware Adaptive Program Repair with Stage-Wise LLM Approach

The paper "Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models" by Zhang, R., Zhang, S. & Xie, L. was published in Software Quality Journal in 2026.

### Key Contributions

The research proposes TypeRepair, a defect-type-aware, multi-stage adaptive framework for code repair. The framework divides the automated program repair (APR) process into four key stages: defect localization, defect type identification, context selection, and patch generation.

The framework defines ten common defect types and provides tailored repair guidance for each specific type, thereby enabling LLMs to perform fine-grained reasoning.

### Performance Results

TypeRepair outperforms state-of-the-art APR tools in overall performance, and independently repairs 33 bugs on the Defects4J dataset that no other method successfully fixes. On the Defects4J v2.0 dataset, TypeRepair achieves a 272.73% improvement over the baseline LLM when using GPT-3.5 and a 257.89% improvement when using GPT-4.

The approach was evaluated on Defects4J v1.2/v2.0 and QuixBugs datasets, comparing against multiple state-of-the-art baseline methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfa9059e-e16f-43d2-be7c-90bd49442239",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "fbe148d9-2e0d-4003-b535-51e91c66ed2f",
  "sourceToolAssistantUUID": "bfa9059e-e16f-43d2-be7c-90bd49442239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-11T23:57:58.454Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014DeFsqogZY4vbWT1jQdjiK`</summary>

```json
{
  "query": "learning agent routing early experience arxiv 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbe148d9-2e0d-4003-b535-51e91c66ed2f",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011Cawgri3gxskUwMbuLtPRH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dba4f61-e99b-423d-ac16-a86e6950a7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013iiAf7tqoB4i7vuhDme2F8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 22754,
      "output_tokens": 61,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1025
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 61,
          "cache_read_input_tokens": 22754,
          "cache_creation_input_tokens": 1025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1025,
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

_source line 37 · 2026-05-11T23:58:05.264Z_

<details><summary>↩ Tool result · `toolu_014DeFsqogZY4vbWT1jQdjiK`</summary>

```text
Web search results for query: "learning agent routing early experience arxiv 2605"

Links: [{"title":"[2605.07180] Learning Agent Routing From Early Experience","url":"https://arxiv.org/abs/2605.07180"},{"title":"Learning Agent Routing From Early Experience","url":"https://arxiv.org/html/2605.07180"},{"title":"Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation","url":"https://arxiv.org/html/2605.05007"},{"title":"Queue-Aware and Resilient Routing in LEO Satellite Networks Using Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2605.04448"},{"title":"[2605.07395] Unsolvability Ceiling in Multi-LLM Routing: An Empirical Study of Evaluation Artifacts","url":"https://arxiv.org/abs/2605.07395"},{"title":"[2605.07260] When Are Experts Misrouted? Counterfactual Routing Analysis in Mixture-of-Experts Language Models","url":"https://arxiv.org/abs/2605.07260"},{"title":"Group Cognition Learning: Making Everything Better Through Governed Two-Stage Agents Collaboration","url":"https://arxiv.org/html/2605.00370"},{"title":"MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents","url":"https://arxiv.org/html/2605.00356v1"},{"title":"Toward Packet Routing with Fully-distributed Multi-agent ...","url":"https://arxiv.org/pdf/1905.03494"},{"title":"SkillOS: Learning Skill Curation for Self-Evolving Agents","url":"https://arxiv.org/html/2605.06614"}]

I found the paper! Here's information about the search results:

The primary match for your search is **"Learning Agent Routing From Early Experience"** (arXiv:2605.07180), which proposes BoundaryRouter, a training-free routing framework that uses early behavioral experience and rubric-guided reasoning to decide whether to answer a query with direct LLM inference or escalate to an agent.

Key details about the paper:

- **Authors**: The work is by Yimin Wang and 8 other authors, from institutions including Princeton University, University of Michigan, Tsinghua University, Shanghai Jiao Tong University, University of Edinburgh, and King's College London

- **Problem**: Many queries fall within the capability boundary of cutting-edge LLMs and do not require full agent execution, making effective routing between LLMs and agents a key challenge

- **Method**: BoundaryRouter builds a compact experience memory by executing both systems on a shared seed set and retrieves similar cases at inference time to guide routing decisions

- **Evaluation**: The authors introduce RouteBench, a benchmark covering in-domain, paraphrased, and out-of-domain route settings

- **Results**: Experiments show that BoundaryRouter reduces inference time by 60.6% compared to the agent while improving performance by 28.6% over direct LLM inference


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dba4f61-e99b-423d-ac16-a86e6950a7a3",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "86e50578-861f-4a0c-9af5-db193b977407",
  "sourceToolAssistantUUID": "0dba4f61-e99b-423d-ac16-a86e6950a7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-11T23:58:08.632Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vcp1A2v47eKLPeBJ4g1vS6`</summary>

```json
{
  "query": "RelRepair enhancing automated program repair retrieving relevant code 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86e50578-861f-4a0c-9af5-db193b977407",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgsehoFYSEXWmSjtnEA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0ba877e-1be5-40cb-be74-e1a9bcf36b65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wb558jDa2WPVCifWWRSYbG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 23779,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 831
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 23779,
          "cache_creation_input_tokens": 831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 831,
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

_source line 39 · 2026-05-11T23:58:15.391Z_

<details><summary>↩ Tool result · `toolu_01Vcp1A2v47eKLPeBJ4g1vS6`</summary>

```text
Web search results for query: "RelRepair enhancing automated program repair retrieving relevant code 2025"

Links: [{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"[2509.16701] RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code","url":"https://arxiv.org/abs/2509.16701"},{"title":"S3: Syntax-and Semantic-Guided Repair Synthesis via Programming by Examples | Request PDF","url":"https://www.researchgate.net/publication/318318641_S3_Syntax-and_Semantic-Guided_Repair_Synthesis_via_Programming_by_Examples"},{"title":"How Often Do Single-Statement Bugs Occur?: The ManySStuBs4J Dataset","url":"https://www.researchgate.net/publication/347307320_How_Often_Do_Single-Statement_Bugs_Occur_The_ManySStuBs4J_Dataset"},{"title":"Paper page - HAFixAgent: History-Aware Automated Program Repair Agent","url":"https://huggingface.co/papers/2511.01047"},{"title":"Practical program repair via bytecode mutation | Request PDF","url":"https://www.researchgate.net/publication/334410407_Practical_program_repair_via_bytecode_mutation"},{"title":"Boosting Redundancy-based Automated Program Repair by Fine-grained Pattern Mining","url":"https://arxiv.org/html/2312.15955"},{"title":"Accelerating Automatic Program Repair with Dual Retrieval-Augmented Fine-Tuning and Patch Generation on Large Language Models","url":"https://arxiv.org/html/2507.10103"},{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"},{"title":"[2507.10103] Accelerating Automatic Program Repair with Dual Retrieval-Augmented Fine-Tuning and Patch Generation on Large Language Models","url":"https://arxiv.org/abs/2507.10103"}]

Based on the search results, here's information about RelRepair:

## Overview

RelRepair is a novel approach that retrieves relevant project-specific code to enhance automated program repair. It addresses the limitation that LLMs often lack the capacity to perform project-specific repairs by first identifying relevant function signatures by analyzing function names and code comments within the project.

## Methodology

RelRepair identifies relevant function signatures by analyzing function names and code comments within the project, conducts deeper code analysis to retrieve code snippets relevant to the repair context, and then incorporates the retrieved relevant information into the LLM's input prompt, guiding the model to generate more accurate and informed patches.

RelRepair consists of three incremental stages: BaseRepair, SigRepair, and SnipRepair. The retrieval processes consist of three structured phases: Query Rewriting, optimizing queries based on the buggy function context; Dataset Creation and Indexing, constructing customized datasets from the project codebase; and Retrieval, selecting contextually relevant functions or code snippets.

## Performance Results

RelRepair achieves an improved total fix rate of 48.3%, significantly exceeding the BaseRepair approach which resolves 31.2% of the bugs, with the integration of relevant information adding an additional 83 bug fixes beyond those achieved by BaseRepair alone. The approach was evaluated on two widely studied datasets, Defects4J V1.2 and ManySStuBs4J.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0ba877e-1be5-40cb-be74-e1a9bcf36b65",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "585e73fb-2e34-4b9a-92e5-62a5b46f7c99",
  "sourceToolAssistantUUID": "e0ba877e-1be5-40cb-be74-e1a9bcf36b65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-11T23:58:17.826Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VX89XDEiCib6c2qR9RMVHP`</summary>

```json
{
  "query": "ExpertRAG efficient RAG mixture of experts retrieval routing 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "585e73fb-2e34-4b9a-92e5-62a5b46f7c99",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgtPxKGWjpCMsB47K59",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "560cd90f-5c5a-4624-8d9f-4cb0c6922e02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7uS7jRvM9J1vhpWqudkJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 24610,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1086
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 24610,
          "cache_creation_input_tokens": 1086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1086,
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

_source line 41 · 2026-05-11T23:58:24.277Z_

<details><summary>↩ Tool result · `toolu_01VX89XDEiCib6c2qR9RMVHP`</summary>

```text
Web search results for query: "ExpertRAG efficient RAG mixture of experts retrieval routing 2025"

Links: [{"title":"1 ExpertRAG: Efficient RAG with Mixture of Experts – Optimizing","url":"https://arxiv.org/pdf/2504.08744"},{"title":"[2504.08744] ExpertRAG: Efficient RAG with Mixture of Experts -- Optimizing Context Retrieval for Adaptive LLM Responses","url":"https://arxiv.org/abs/2504.08744"},{"title":"[PDF] ExpertRAG: Efficient RAG with Mixture of Experts - Optimizing Context Retrieval for Adaptive LLM Responses | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ExpertRAG:-Efficient-RAG-with-Mixture-of-Experts-Gumaan/fdc0f4e23f823c11c43d097894314392a272ae3e"},{"title":"MIXRAG : Mixture-of-Experts Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250921391L/abstract"},{"title":"Paper page - ExpertRAG: Efficient RAG with Mixture of Experts -- Optimizing Context Retrieval for Adaptive LLM Responses","url":"https://huggingface.co/papers/2504.08744"},{"title":"Mixture-of-Experts for Knowledge Graph Retrieval-Augmented Generation | OpenReview","url":"https://openreview.net/forum?id=1KkIChhCv7"},{"title":"ExpertRAG: Efficient RAG with Mixture of Experts -- Optimizing Context Retrieval for Adaptive LLM Responses","url":"https://www.researchgate.net/publication/390771886_ExpertRAG_Efficient_RAG_with_Mixture_of_Experts_--_Optimizing_Context_Retrieval_for_Adaptive_LLM_Responses"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"ExpertRAG: Efficient RAG with Mixture of Experts -- Optimizing Context Retrieval for Adaptive LLM Responses","url":"http://www.paperreading.club/page?id=299086"},{"title":"ExpRAG: Experience-Based RAG Framework","url":"https://www.emergentmind.com/topics/exprag"}]

Based on the search results, here's what I found about ExpertRAG:

## Overview

ExpertRAG is a novel theoretical framework that integrates Mixture-of-Experts (MoE) architectures with Retrieval Augmented Generation (RAG) to advance the efficiency and accuracy of knowledge-intensive language modeling.

## Key Mechanisms

The framework proposes a dynamic retrieval gating mechanism coupled with expert routing, enabling the model to selectively consult an external knowledge store or rely on specialized internal experts based on the query's needs.

Different MoE experts can handle different topical domains or subtasks, allowing the parametric component to generalize better; for example, a science question might be routed to a "science expert" layer and also trigger retrieval from a scientific literature database, whereas a simple commonsense query might be handled by a general expert without any retrieval.

## Efficiency Advantages

A major improvement over standard RAG is that conventional RAG systems typically always perform retrieval for each query, incurring extra latency, whereas ExpertRAG aims to improve upon this by making retrieval conditional via a gating expert.

## Theoretical Foundations

The paper lays out the theoretical foundations of ExpertRAG, including a probabilistic formulation that treats retrieval and expert selection as latent decisions, and mathematical justifications for its efficiency in both computation and knowledge utilization.

The paper was published on March 23, 2025, and presents ExpertRAG as a theoretical framework with a roadmap for empirical validation rather than as an already-implemented system.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "560cd90f-5c5a-4624-8d9f-4cb0c6922e02",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "729a59cf-9798-4105-abb4-1a1e3d1dca3b",
  "sourceToolAssistantUUID": "560cd90f-5c5a-4624-8d9f-4cb0c6922e02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-11T23:58:26.332Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0143aSriD7RgNnJejvuzXF8N`</summary>

```json
{
  "query": "ASE 2025 adaptive retrieval code repair context selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "729a59cf-9798-4105-abb4-1a1e3d1dca3b",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011Cawgu3yJpjtk1gXBSh2Rb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7916d251-3663-43a9-bda4-277c475d888d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BECiZSSCAaZEAxWWRmeDe1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 25696,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1111
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 25696,
          "cache_creation_input_tokens": 1111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1111,
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

_source line 43 · 2026-05-11T23:58:33.879Z_

<details><summary>↩ Tool result · `toolu_0143aSriD7RgNnJejvuzXF8N`</summary>

```text
Web search results for query: "ASE 2025 adaptive retrieval code repair context selection"

Links: [{"title":"dblp: ASE 2025","url":"https://dblp.org/db/conf/kbse/ase2025.html"},{"title":"Relative Positioning Based Code Chunking Method For Rich Context Retrieval In Repository Level Code Completion Task With Code Language Model","url":"https://arxiv.org/html/2510.08610v1"},{"title":"LAURA: Enhancing Code Review Generation with Context-Enriched Retrieval-Augmented LLM (ASE 2025 - Research Papers) - ASE 2025","url":"https://conf.researchr.org/details/ase-2025/ase-2025-papers/107/LAURA-Enhancing-Code-Review-Generation-with-Context-Enriched-Retrieval-Augmented-LLM"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"AlignCoder: Aligning Retrieval with Target Intent for Repository-Level Code Completion (ASE 2025 - Research Papers) - ASE 2025","url":"https://conf.researchr.org/details/ase-2025/ase-2025-papers/34/AlignCoder-Aligning-Retrieval-with-Target-Intent-for-Repository-Level-Code-Completio"},{"title":"GitHub - allanj/repo-level-codegen-papers: Repo-Level Code generation papers · GitHub","url":"https://github.com/allanj/repo-level-codegen-papers"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"Aligning Retrieval with Target Intent for Repository-Level ...","url":"https://dl.acm.org/doi/abs/10.1109/ASE63991.2025.00085"}]

Based on the web search results, I found several relevant papers and research projects related to ASE 2025 that involve adaptive retrieval, code repair, and context selection:

## Key Findings:

**AlignCoder - Repository-Level Code Completion:**
AlignCoder addresses the challenge that repository-level code completion remains difficult due to limited understanding of repository context. While retrieval-augmented generation approaches show promise, they suffer from misalignment between query and target code. AlignCoder proposes a framework that introduces a query enhancement mechanism and reinforcement learning-based retriever training.

**Code Repair with Adaptive Retrieval:**
ReCode uses the LLM to analyze the user's query to infer the algorithm type, which is then used to retrieve the most relevant exemplars from an algorithm-specific knowledge corpus. By integrating algorithmic categorization with the model's semantic modeling, ReCode significantly enhances the contextual relevance of retrieved in-context exemplars and supports more accurate and adaptive code repair generation.

**Context Selection for Code Completion:**
JetBrains Research organized a workshop co-located with ASE 2025 and asked the community to develop an effective context collection strategy. The objective is to create a context collection strategy that supplements completion points with useful information from across the whole repository.

**LAURA - Code Review with Context:**
LAURA is an LLM-based framework for code review generation that integrates review exemplar retrieval, context augmentation, and systematic guidance to enhance the performance of ChatGPT-4o and DeepSeek v3.

These works collectively address key challenges in adaptive retrieval, context selection, and their application to code repair and completion tasks at ASE 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7916d251-3663-43a9-bda4-277c475d888d",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "c2a4d082-94bf-42ae-a767-a70b3c2398c1",
  "sourceToolAssistantUUID": "7916d251-3663-43a9-bda4-277c475d888d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-11T23:58:36.026Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q4mTgKMH66jsrbPS6vJnML`</summary>

```json
{
  "query": "GranRoute routing retrieval configuration code repair granularity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2a4d082-94bf-42ae-a767-a70b3c2398c1",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgukzdDjS7X5g5Z3MZ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87b0157c-14d3-4f37-ae60-c9f87695155c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXZDqUdBx1ytNJtjQa3YB6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 26807,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1082
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 26807,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1082,
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

_source line 45 · 2026-05-11T23:58:42.046Z_

<details><summary>↩ Tool result · `toolu_01Q4mTgKMH66jsrbPS6vJnML`</summary>

```text
Web search results for query: "GranRoute routing retrieval configuration code repair granularity"

Links: [{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"Advanced Routing Engine - PAN-OS","url":"https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-new-features/networking-features/advanced-routing-engine"},{"title":"fix routing · Issue #2787 · gdsfactory/gdsfactory","url":"https://github.com/gdsfactory/gdsfactory/issues/2787"},{"title":"Route point granularity (Path) - Route Optimization API - GraphHopper Forum","url":"https://discuss.graphhopper.com/t/route-point-granularity-path/7746"},{"title":"Optimize the Chunking Granularity for Retrieval- ...","url":"https://aclanthology.org/2025.coling-main.384.pdf"},{"title":"[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/abs/2604.00167"},{"title":"Unable to Retrieve Routing information When Using Neo4j Python Driver · Issue #628 · neo4j/neo4j-python-driver","url":"https://github.com/neo4j/neo4j-python-driver/issues/628"},{"title":"UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities","url":"https://universalrag.github.io/"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"Configuring Graceful Routing Engine Switchover | Junos OS | Juniper Networks","url":"https://www.juniper.net/documentation/us/en/software/junos/high-availability/topics/task/gres-configuring.html"}]

Based on the search results, here's what I found regarding your query about GranRoute routing retrieval configuration code repair granularity:

The search results reveal relevant research on code repair and granularity in retrieval systems:

## Code Repair and Fault Localization Granularity

Source file context can be constructed from fault localization output, with granularity varying from file-level (entire file) to function-level (relevant functions with context window) to line-level (specific lines).

Function-level granularity yields the highest repair rate against line-level and file-level in repository-scale code repair tasks, though the ideal granularity may in fact be task dependent.

## Retrieval-Augmented Generation with Granularity-Aware Routing

A related system called UniversalRAG addresses similar concepts: It organizes each corpus by granularity—from passages to full documents, or from short clips to full videos—so the retrieval process matches both the semantic intent and the scope of the user's query.

However, I should note that the search results do not contain specific information about a system called "GranRoute" directly. If you're looking for more specific information about GranRoute, please provide additional context or clarify what system you're inquiring about.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87b0157c-14d3-4f37-ae60-c9f87695155c",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "42da2c6c-b6c9-411b-aa6b-58e627f32767",
  "sourceToolAssistantUUID": "87b0157c-14d3-4f37-ae60-c9f87695155c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-11T23:58:45.340Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WAhbDZwCrGnx73j2WX5DFq`</summary>

```json
{
  "query": "Agentless SWE-bench context budget selection per-instance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42da2c6c-b6c9-411b-aa6b-58e627f32767",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgvMw5jzyM6jNV6sRe9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e16e6bc5-2e94-43ac-98fd-dfb646562ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExdkJUtdutYfweXKmRznG8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 893,
      "cache_read_input_tokens": 27889,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 893
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 27889,
          "cache_creation_input_tokens": 893,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 893,
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

_source line 47 · 2026-05-11T23:58:52.369Z_

<details><summary>↩ Tool result · `toolu_01WAhbDZwCrGnx73j2WX5DFq`</summary>

```text
Web search results for query: "Agentless SWE-bench context budget selection per-instance 2025 2026"

Links: [{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"GitHub - sorendunn/Agentless-Lite: Agentless Lite: RAG-based SWE-Bench software engineering scaffold · GitHub","url":"https://github.com/sorendunn/Agentless-Lite"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"[2407.01489] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489"},{"title":"GitHub - OpenAutoCoder/Agentless: Agentless🐱: an agentless approach to automatically solve software development problems","url":"https://github.com/OpenAutoCoder/Agentless"},{"title":"SWE-Bench Coding Agent Leaderboard 2026: Claude vs GPT | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/swe-bench-coding-agent-leaderboard/"},{"title":"LLM Benchmarks 2026: 30+ Models Ranked — MMLU, SWE-bench, Arena Elo & Pricing","url":"https://iternal.ai/llm-selection-guide"},{"title":"SWE-Bench Leaderboards","url":"https://www.emergentmind.com/topics/swe-bench-leaderboards"},{"title":"GitHub - murataslan1/ai-agent-benchmark: AI coding agents comparison - 80+ agents, SWE-Bench leaderboard, pricing. Devin, Cursor, Claude Code, Copilot, and more. December 2025. · GitHub","url":"https://github.com/murataslan1/ai-agent-benchmark"}]

Based on the search results, here's what I found regarding Agentless and SWE-bench:

## Agentless Approach

Agentless is a research scaffold built on the premise that less orchestration is sometimes more, using a fixed three-stage pipeline - fault localization (identifying which files and lines are relevant), patch generation (producing multiple candidate patches in parallel), and patch selection (ranking candidates by test results).

## Recent Performance (2025-2026)

In February 2025, Agentless Lite 1.0 was released as the top-performing RAG-only scaffold for SWE-bench, increasing RAG performance on the lite subset from 4.33% to 32.33% and costing only $0.21 per instance. In February 2026, Agentless Lite more than doubled SOTA on SWE-bench Multimodal from 12.19% to 25.34% for a fourth of the cost without requiring a runtime environment.

## Per-Instance Cost Efficiency

The search results indicate cost metrics per instance rather than specific context budget selection mechanisms. On the SWE-bench Lite benchmark, Agentless achieved 32.00% (96 correct fixes) and low cost ($0.70).

However, the search results don't contain detailed information about specific context budget selection algorithms or per-instance adaptive mechanisms. If you're looking for more technical details about how context budgets are allocated per instance in Agentless, you may need to consult the original research papers or GitHub repositories directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e16e6bc5-2e94-43ac-98fd-dfb646562ff8",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "3e4792b7-0b78-42fa-8971-5f420b4e93cb",
  "sourceToolAssistantUUID": "e16e6bc5-2e94-43ac-98fd-dfb646562ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-11T23:58:54.616Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JfLvrajV5feJciW3w8WjWC`</summary>

```json
{
  "query": "\"optimize chunking granularity retrieval\" adaptive COLING 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e4792b7-0b78-42fa-8971-5f420b4e93cb",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011Cawgw86f3oBmwoh6DZw3p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55912456-df7d-43b1-bc78-5499c1c4d8c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JcmUjff3DXzWFoFFzyeSGs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 973,
      "cache_read_input_tokens": 28782,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 973
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 28782,
          "cache_creation_input_tokens": 973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 973,
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

_source line 49 · 2026-05-11T23:59:00.987Z_

<details><summary>↩ Tool result · `toolu_01JfLvrajV5feJciW3w8WjWC`</summary>

```text
Web search results for query: ""optimize chunking granularity retrieval" adaptive COLING 2025"

Links: [{"title":"Optimize the Chunking Granularity for Retrieval- ...","url":"https://aclanthology.org/2025.coling-main.384.pdf"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.384/"},{"title":"GitHub - ZGChung/Mix-of-Granularity: [COLING 2025] Mix-of-Granularity paper","url":"https://github.com/ZGChung/Mix-of-Granularity"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2406.00456v1"},{"title":"[2406.00456] Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2406.00456"},{"title":"Computer Science Jun 2024","url":"https://arxiv.org/list/cs/2024-06?skip=200&show=100"},{"title":"Reconstructing Context Evaluating Advanced Chunking Strategies for","url":"https://arxiv.org/pdf/2504.19754"},{"title":"Comparative Evaluation of Advanced Chunking for Retrieval ...","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12649634/"},{"title":"Chunking Optimization for Retrieval-Augmented Generation","url":"https://www.squareboat.com/blog/chunking-optimization-for-retrieval-augmented-generation"},{"title":"Document Chunking for RAG: 9 Strategies Tested (70% Accuracy Boost 2025) | LLM Practical Experience Hub","url":"https://langcopilot.com/posts/2025-10-11-document-chunking-for-rag-practical-guide"}]

I found relevant information about the paper you're searching for. Here are the key results:

## Mix-of-Granularity (COLING 2025)

The paper "Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation" was presented at COLING 2025. The authors are Zijie Zhong, Hanwen Liu, Xiaoya Cui, Xiaofan Zhang, and Zengchang Qin.

### Core Contribution

Mix-of-Granularity (MoG) is a method that dynamically determines the optimal granularity of a knowledge source based on input queries using a router. The router is efficiently trained with a newly proposed loss function employing soft labels.

### Extensions and Methods

The paper extends MoG to MoG-Graph (MoGG), where reference documents are pre-processed as graphs, enabling the retrieval of distantly situated snippets.

### Results

Experiments demonstrate that MoG and MoGG effectively predict optimal granularity levels, significantly enhancing the performance of the RAG system in downstream tasks.

### Availability

The code of both MoG and MoGG will be made public. You can find the GitHub repository at [ZGChung/Mix-of-Granularity](https://github.com/ZGChung/Mix-of-Granularity).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55912456-df7d-43b1-bc78-5499c1c4d8c7",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "49f0a209-0b30-4ea3-93c0-820c74ebe72c",
  "sourceToolAssistantUUID": "55912456-df7d-43b1-bc78-5499c1c4d8c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-11T23:59:03.748Z_

This is a very important find. Let me get more details on Mix-of-Granularity and also search for a few more potentially relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49f0a209-0b30-4ea3-93c0-820c74ebe72c",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011Cawgwkuinzy7ofhRu5g6Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07b9fbad-99b7-4847-a89c-1dafd83f5cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XW9QFhzTbuAdGwjjyfkMq9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 29755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 957,
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

_source line 51 · 2026-05-11T23:59:04.152Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012mJUpGpR5HPYQpqmXUUdJ1`</summary>

```json
{
  "query": "Mix-of-Granularity MoG router optimal granularity retrieval augmented generation Zhong"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07b9fbad-99b7-4847-a89c-1dafd83f5cbc",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011Cawgwkuinzy7ofhRu5g6Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b115ad29-906c-4992-91e3-d037680c958c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XW9QFhzTbuAdGwjjyfkMq9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 29755,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 29755,
          "cache_creation_input_tokens": 957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 957,
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

_source line 52 · 2026-05-11T23:59:11.251Z_

<details><summary>↩ Tool result · `toolu_012mJUpGpR5HPYQpqmXUUdJ1`</summary>

```text
Web search results for query: "Mix-of-Granularity MoG router optimal granularity retrieval augmented generation Zhong"

Links: [{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2406.00456v1"},{"title":"[2406.00456] Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2406.00456"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.384/"},{"title":"GitHub - ZGChung/Mix-of-Granularity: [COLING 2025] Mix-of-Granularity paper","url":"https://github.com/ZGChung/Mix-of-Granularity"},{"title":"Paper page - Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://huggingface.co/papers/2406.00456"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://powerdrill.ai/discover/discover-Mix-of-Granularity-Optimize-the-clx4ktn2104l6019n4h6q5sy2"},{"title":"Optimize the Chunking Granularity for Retrieval- ...","url":"https://aclanthology.org/2025.coling-main.384.pdf"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/mix-granularity-optimize-chunking-granularity-retrieval-augmented"},{"title":"FreeChunker: A Cross-Granularity Chunking Framework","url":"https://arxiv.org/html/2510.20356v1"},{"title":"Chunking Optimization for Retrieval-Augmented Generation","url":"https://www.squareboat.com/blog/chunking-optimization-for-retrieval-augmented-generation"}]

The search has returned comprehensive results about Mix-of-Granularity (MoG) and its related research. Here's a summary of the key findings:

## Mix-of-Granularity (MoG): Overview

Mix-of-Granularity (MoG) is a method that dynamically determines the optimal granularity of a knowledge database based on input queries using a router. The research was conducted by Zijie Zhong from Shanghai Artificial Intelligence Laboratory along with collaborators from Beihang University.

## Core Problem

Integrating information from different reference data sources is a major challenge for RAG systems because each knowledge source adopts a unique data structure. Retrieving from multiple knowledge sources with one fixed strategy usually leads to under-exploitation of information.

## Technical Approach

The router is efficiently trained with a newly proposed loss function employing soft labels. MoG is inspired by the Mix-of-Experts architecture and employs a trained router to select and combine reference snippets of varying granularity levels dynamically.

## Extended Version: MoGG

The research further extends MoG to Mix-of-Granularity-Graph (MoGG), where reference documents are pre-processed into graphs, enabling the retrieval of relevant information from distantly situated chunks.

## Performance Results

Extensive experiments demonstrate that both MoG and MoGG effectively predict optimal granularity levels, significantly enhancing the performance of the RAG system in downstream tasks.

## Publication

The paper was presented at the 31st International Conference on Computational Linguistics (COLING 2025) in Abu Dhabi, UAE.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b115ad29-906c-4992-91e3-d037680c958c",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "5025648d-a778-4a99-9eab-d81594fa6655",
  "sourceToolAssistantUUID": "b115ad29-906c-4992-91e3-d037680c958c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-11T23:59:13.743Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JA3U4anS66HeCeok1GCcPS`</summary>

```json
{
  "query": "UniversalRAG retrieval augmented generation diverse modalities granularities adaptive routing 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5025648d-a778-4a99-9eab-d81594fa6655",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgxWow1fqTXTcWGgJk9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "898c1455-2d35-441d-b5d8-82062a8d4dd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019L8girYroHq7mu8mbiE14B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 30712,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1105
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 30712,
          "cache_creation_input_tokens": 1105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1105,
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

_source line 54 · 2026-05-11T23:59:23.991Z_

<details><summary>↩ Tool result · `toolu_01JA3U4anS66HeCeok1GCcPS`</summary>

```text
Web search results for query: "UniversalRAG retrieval augmented generation diverse modalities granularities adaptive routing 2025"

Links: [{"title":"UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities","url":"https://universalrag.github.io/"},{"title":"[2504.20734] UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities","url":"https://arxiv.org/abs/2504.20734"},{"title":"[PDF] UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities | Semantic Scholar","url":"https://www.semanticscholar.org/paper/UniversalRAG:-Retrieval-Augmented-Generation-over-Yeo-Kim/94cf17cdb8df7016ebe7decb91257a2d0b14d1e8"},{"title":"GitHub - wgcyeo/UniversalRAG: UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities","url":"https://github.com/wgcyeo/UniversalRAG"},{"title":"[2504.20734v1] UniversalRAG: Retrieval-Augmented Generation over Multiple Corpora with Diverse Modalities and Granularities","url":"http://arxiv.org/abs/2504.20734v1"},{"title":"Paper page - UniversalRAG: Retrieval-Augmented Generation over Multiple Corpora with Diverse Modalities and Granularities","url":"https://huggingface.co/papers/2504.20734"},{"title":"UniversalRAG: Retrieval-Augmented Generation over Multiple Corpora with Diverse Modalities and Granularities","url":"https://vladbogo.substack.com/p/universalrag-retrieval-augmented"},{"title":"UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities | OpenReview","url":"https://openreview.net/forum?id=mXtV92SPxW"},{"title":"UniversalRAG: Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2504.20734"},{"title":"UniversalRAG: Dynamic Multimodal Retrieval for Smarter AI Responses","url":"https://kiadev.net/news/2025-05-05-universalrag-dynamic-multimodal-retrieval-smarter-ai-responses"}]

Based on the web search results, here's a comprehensive overview of UniversalRAG:

## Overview

UniversalRAG is designed to retrieve and integrate knowledge from heterogeneous sources with diverse modalities and granularities. The research was published in 2025 by Yeo, Kim, Jeong, Baek, and Hwang.

## Key Innovation: Modality-Aware Routing

The core innovation of UniversalRAG addresses a critical limitation in existing RAG systems. Forcing all modalities into a unified representation space derived from a single aggregated corpus causes a modality gap, where the retrieval tends to favor items from the same modality as the query. 

To solve this, UniversalRAG overcomes these limitations via a modality- and granularity-aware routing mechanism over diverse corpora. Rather than forcing heterogeneous data into a single shared space, UniversalRAG dynamically identifies the most relevant modality-specific corpus and performs targeted retrieval within it.

## Multiple Granularities

Beyond modality, UniversalRAG organizes each modality into multiple granularity levels, enabling fine-tuned retrieval tailored to the complexity and scope of the query. This includes granularity organization from passages to full documents, or from short clips to full videos.

## Evaluation and Performance

UniversalRAG was validated on 10 benchmarks of multiple modalities, showing its superiority over various modality-specific and unified baselines.

## Technical Implementation

The framework organizes knowledge into multiple modality-specific corpora: text, image, and video, with each modality broken down into multiple granularity levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "898c1455-2d35-441d-b5d8-82062a8d4dd2",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "43e3e2f8-1d5d-4d71-a47f-53f5c0cc2965",
  "sourceToolAssistantUUID": "898c1455-2d35-441d-b5d8-82062a8d4dd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-11T23:59:27.080Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C184ZKYtyYdSkLoaBPejr5`</summary>

```json
{
  "query": "per-instance adaptive configuration selection software engineering LLM repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43e3e2f8-1d5d-4d71-a47f-53f5c0cc2965",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgyTGPATSidkvvqvTzY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25758eec-e0e3-47f6-a81e-d99d0fcce149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K29hhEdfe9chNbbMsdQ5sZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 31817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

### Tool result

_source line 56 · 2026-05-11T23:59:33.599Z_

<details><summary>↩ Tool result · `toolu_01C184ZKYtyYdSkLoaBPejr5`</summary>

```text
Web search results for query: "per-instance adaptive configuration selection software engineering LLM repair 2025 2026"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Aligning the Objective of LLM-based Program Repair (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/148/Aligning-the-Objective-of-LLM-based-Program-Repair"},{"title":"An empirical evaluation of pre-trained large language models for repairing declarative formal specifications | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10687-1"},{"title":"Aligning the Objective of LLM-Based Program Repair | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00169"},{"title":"Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-026-09751-w"},{"title":"Aligning the Objective of LLM-Based Program Repair | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/11029684/11029718/11029731.pdf"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Speed at the Cost of Quality","url":"https://courtney-e-miller.github.io/papers/SpeedAtTheCostofQuality_TheImpactofLLMAgentAssistantonSoftwareDevelopment.pdf"},{"title":"[2404.08877] Aligning the Objective of LLM-based Program Repair","url":"https://arxiv.org/abs/2404.08877"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"}]

I found relevant research on LLM-based program repair with adaptive approaches from 2025-2026. Here are the key findings:

## Recent Work on Adaptive Program Repair with LLMs

**Defect-Type-Aware Adaptive Repair:**
A 2026 publication titled "Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models" appears in Software Quality Journal, suggesting active research on adaptive configuration approaches for different defect types.

**Objective Alignment in LLM-Based APR:**
A key approach improving LLM's APR capability involves aligning the output to their training objective and allowing them to refine the whole program without first identifying faulty statements. This was published at ICSE 2025.

**Emerging Trends (2025-2026):**
The search results indicate several active research areas:
- Context-aware prompting for LLM-based program repair (2025)
- 63 recent state-of-the-art APR systems published between Jan 2022 and June 2025, showing active development in the field
- Automated adaptive prompting for real-world software vulnerability patching (APPATCH) at USENIX Security 2025

The research appears to be moving toward more instance-aware and adaptive strategies that better leverage LLM capabilities rather than using static configuration across all repair instances.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25758eec-e0e3-47f6-a81e-d99d0fcce149",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "a4918342-a03e-462b-8e42-53c86de309fc",
  "sourceToolAssistantUUID": "25758eec-e0e3-47f6-a81e-d99d0fcce149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-11T23:59:35.880Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N3AWCdhjSxV3Xv1muexqat`</summary>

```json
{
  "query": "Uno Orchestra parsimonious agent routing selective delegation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4918342-a03e-462b-8e42-53c86de309fc",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011CawgzALgiK7HHKx2xSP8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb40b261-6b28-4292-bc11-50e321c1147e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01499E1bQKGdfrd9GdFa9xit",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 32936,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1076
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 32936,
          "cache_creation_input_tokens": 1076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1076,
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

_source line 58 · 2026-05-11T23:59:43.834Z_

<details><summary>↩ Tool result · `toolu_01N3AWCdhjSxV3Xv1muexqat`</summary>

```text
Web search results for query: "Uno Orchestra parsimonious agent routing selective delegation 2025"

Links: [{"title":"Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation","url":"https://arxiv.org/html/2605.05007"},{"title":"[2605.05007] Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation","url":"https://arxiv.org/abs/2605.05007"},{"title":"5 Multi-Agent Orchestration Patterns You MUST Know in 2025! - YouTube","url":"https://www.youtube.com/watch?v=l_i7icCA56c"},{"title":"Multi-Agent Orchestration: How to Coordinate AI Agents at","url":"https://gurusup.com/blog/multi-agent-orchestration-guide"},{"title":"Multi-Agent Frameworks Explained for Enterprise AI Systems [2026]","url":"https://www.adopt.ai/blog/multi-agent-frameworks"},{"title":"Join the UN Symphony Orchestra the UN Singers | United Nations","url":"https://www.un.org/en/delegate/join-un-symphony-orchestra-un-singers"},{"title":"AI Agent Orchestration Patterns - Azure Architecture Center | Microsoft Learn","url":"https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns"},{"title":"Payment Orchestration: Infrastructure on a Global Scale | Yuno","url":"https://y.uno/"},{"title":"Top Payment Orchestration Platforms 2026 | Yuno","url":"https://y.uno/post/top-payment-orchestration-platforms-2026"},{"title":"Multi-agent system: Frameworks & step-by-step tutorial – n8n Blog","url":"https://blog.n8n.io/multi-agent-systems/"}]

Based on the search results, I found relevant information about Uno-Orchestra:

## Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation

Uno-Orchestra is a unified orchestration policy that selectively decomposes a task and dispatches each subtask to an admissible (model, primitive) pair, with both decisions learned together from curated RL trajectories grounded in real worker interactions.

### Key Features and Performance

On a 13-benchmark suite, Uno-Orchestra attains 77.0% macro pass@1, roughly 16% above the strongest workflow baseline at roughly an order of magnitude lower per-query cost.

### Technical Approach

The system formulates selective delegation as a unified causal-LM policy that jointly emits subtask decomposition and per-subtask (model, primitive) routing decisions, and introduces Agentic-GRPO, an agent-adaptive RL objective with structured credit assignment for multi-turn orchestration.

### Efficiency Improvements

The remaining gains come from better delegation decisions rather than longer trajectories, since the controller stays near the same token budget while improving accuracy. Agentic-GRPO trims per-query cost slightly below Uno-tree-GRPO while still raising accuracy, indicating that turn-level credit removes redundant dispatches faster than it introduces new ones.

### Core Principle

Selective delegation, the ability to both decompose and abstain from decomposing under one objective, offers a useful organising principle for advancing the accuracy-efficiency frontier of cost-aware multi-agent systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb40b261-6b28-4292-bc11-50e321c1147e",
  "isSidechain": true,
  "promptId": "ebc3868d-0b48-4422-8f63-4c4b12778e2d",
  "agentId": "aab2b9a0d81eac379",
  "type": "user",
  "uuid": "006e1c4a-846a-466c-9622-9c8ead85417e",
  "sourceToolAssistantUUID": "bb40b261-6b28-4292-bc11-50e321c1147e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-12T00:00:54.609Z_

Now I have comprehensive results from all searches. Here is my consolidated report.

---

## Comprehensive Related Work Search Results

I ran 18 web searches across 8 query categories. Below are the most relevant papers organized by how closely they match GranRoute's core idea of **learning to select (fault-localization granularity, context budget) per issue for code repair**.

---

### TIER 1: VERY HIGH RELEVANCE -- Papers doing the same or very similar thing

**1. "A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks"** (arXiv:2604.00167, April 2026)
- This is the **most directly relevant** paper. It systematically compares file-level, function-level, and line-level FL granularity on repository-scale repair using a modified Agentless pipeline with ground-truth localization on SWE-bench.
- Key finding: function-level granularity yields the highest repair rate on average, BUT the relative ordering shifts with difficulty tier, i.e., **the optimal granularity is instance-dependent**.
- The paper explicitly motivates adaptive/difficulty-aware granularity selection but appears to stop at the empirical study (does not build a learned router). GranRoute should cite this as direct motivation and compare against its fixed-granularity baselines.
- [Link](https://arxiv.org/abs/2604.00167)

**2. "On the Role of Fault Localization Context for LLM-Based Program Repair"** (arXiv:2604.05481, April 2026)
- Studies how much localization context is needed and whether additional context beyond the predicted buggy location helps.
- Finding: more context does not consistently improve repair; file-level localization is the dominant factor (15-17x improvement over no-file baseline). Different configurations resolve different subsets of instances.
- Directly supports GranRoute's thesis that context/granularity should be adapted per instance.
- [Link](https://arxiv.org/abs/2604.05481)

**3. Mix-of-Granularity (MoG)** -- "Optimize the Chunking Granularity for Retrieval-Augmented Generation" (COLING 2025, arXiv:2406.00456)
- Authors: Zijie Zhong et al. (Shanghai AI Lab / Beihang)
- **Trains a router (inspired by Mixture-of-Experts) to dynamically select the optimal retrieval granularity per query** for RAG systems. Uses soft-label loss to train the router efficiently.
- This is the **closest methodological analog** to GranRoute outside the code-repair domain. The core mechanism (learning a router to pick granularity) is essentially the same idea applied to general QA instead of code repair.
- GranRoute should compare/contrast with MoG's approach and discuss whether their router design draws on or improves upon MoG.
- [Link](https://aclanthology.org/2025.coling-main.384/)

---

### TIER 2: HIGH RELEVANCE -- Routing/adaptive selection for retrieval or code tasks

**4. RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models** (NeurIPS 2025, arXiv:2505.23052)
- First RAG-aware routing method. Uses contrastive learning to capture how retrieved documents shift knowledge representations, then routes queries to the best-suited LLM.
- Outperforms best individual LLM by 3.61% and existing routing methods by 3.29-9.33%.
- Relevant to GranRoute because it learns to route in a retrieval-augmented setting, though it routes across models rather than across retrieval configurations.
- [Link](https://arxiv.org/abs/2505.23052)

**5. UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities** (arXiv:2504.20734, 2025)
- Implements a **modality- and granularity-aware routing mechanism** that dynamically identifies the most relevant corpus and granularity level per query.
- Organizes each modality into multiple granularity levels (passages to full documents). Validated on 10 benchmarks.
- Relevant as another instance of learning to route across granularities for RAG.
- [Link](https://arxiv.org/abs/2504.20734)

**6. ExpertRAG: Efficient RAG with Mixture of Experts** (arXiv:2504.08744, March 2025)
- Proposes a dynamic retrieval gating mechanism coupled with expert routing, making retrieval conditional via a gating expert (different topical domains get different experts + retrieval decisions).
- Theoretical framework with probabilistic formulation treating retrieval and expert selection as latent decisions.
- [Link](https://arxiv.org/abs/2504.08744)

**7. TypeRepair: "Towards Defect-Type-Aware Adaptive Program Repair"** (Software Quality Journal, 2026)
- A stage-wise framework that classifies the defect type first, then selects type-specific repair guidance.
- Defines 10 defect types with tailored repair strategies. 272% improvement over baseline GPT-3.5 on Defects4J.
- Relevant because it also does **per-instance adaptive selection**, but routes on defect type rather than FL granularity/context budget.
- [Link](https://link.springer.com/article/10.1007/s11219-026-09751-w)

**8. BoundaryRouter: "Learning Agent Routing From Early Experience"** (arXiv:2605.07180, May 2026)
- Training-free routing framework that uses early behavioral experience to decide whether to use direct LLM inference or escalate to a full agent.
- Reduces inference time by 60.6% vs. agent while improving performance 28.6% over direct LLM.
- Relevant as a routing-for-code-tasks approach, though routes between LLM vs. agent rather than between retrieval configurations.
- [Link](https://arxiv.org/abs/2605.07180)

**9. Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation** (arXiv:2605.05007, May 2026)
- Learns a unified orchestration policy that jointly decomposes tasks and routes subtasks to (model, primitive) pairs. Uses RL with structured credit assignment.
- 77.0% macro pass@1 on a 13-benchmark suite, ~16% above the strongest workflow baseline at ~10x lower cost.
- Relevant as a learned routing/delegation framework for multi-step tasks.
- [Link](https://arxiv.org/abs/2605.05007)

---

### TIER 3: MODERATELY RELEVANT -- Retrieval-augmented code repair (but not adaptive routing)

**10. ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation** (CIKM 2025, arXiv:2509.02330)
- Algorithm-aware retrieval: classifies the algorithm type of a query, then retrieves from an algorithm-specific corpus. Dual-encoder architecture for fine-grained semantic matching.
- Does adaptive retrieval but at the level of algorithm-type classification, not FL granularity routing.
- [Link](https://arxiv.org/abs/2509.02330)

**11. RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code** (arXiv:2509.16701, 2025)
- Three-stage retrieval pipeline (BaseRepair -> SigRepair -> SnipRepair) retrieving function signatures and code snippets.
- Achieves 48.3% fix rate vs. 31.2% baseline on Defects4J. Not adaptive per-instance but uses progressive retrieval stages.
- [Link](https://arxiv.org/abs/2509.16701)

**12. AdaPatcher: "Less is More: Adaptive Program Repair with Bug Localization and Preference Learning"** (AAAI 2025, arXiv:2503.06510)
- Two-stage: Bug Locator with self-debug learning + Program Modifier with location-aware repair and adaptive preference learning.
- "Adaptive" here means minimizing patch size while maintaining correctness, not adapting retrieval configuration.
- [Link](https://arxiv.org/abs/2503.06510)

**13. ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair** (arXiv:2605.03117, May 2026)
- Augments LLM agents with a multi-granularity program graph (down to statement-level nodes with def-use edges). Three-tier tool API exposes data-flow slicing.
- Improves Function Recall@1 by 17.0 points on SWE-bench Lite. Relevant for its multi-granularity graph design.
- [Link](https://arxiv.org/abs/2605.03117)

**14. ReAPR: Automatic Program Repair via Retrieval-Augmented Large Language Models** (Software Quality Journal, 2025)
- RAG for APR but with fixed retrieval strategy, not adaptive.
- [Link](https://link.springer.com/article/10.1007/s11219-025-09728-1)

**15. ARCS: Agentic Retrieval-Augmented Code Synthesis with Iterative Refinement** (arXiv:2504.20434, 2025)
- Synthesize-execute-repair loop with retrieval-before-generation. Reduces hallucination.
- [Link](https://arxiv.org/abs/2504.20434)

**16. Agentless-Lite** (2025-2026)
- RAG-only scaffold for SWE-bench. Achieved 32.33% on SWE-bench Lite, $0.21/instance. In Feb 2026, doubled SOTA on SWE-bench Multimodal to 25.34%.
- Uses a fixed pipeline (localization -> generation -> selection), not adaptive per-instance configuration.
- [Link](https://github.com/sorendunn/Agentless-Lite)

---

### KEY RECOMMENDATIONS FOR THE PAPER

The three papers GranRoute is most at risk of missing or insufficiently differentiating from:

1. **Mix-of-Granularity (COLING 2025)** -- Does almost exactly the same thing (learns a router to select retrieval granularity) but for general QA RAG rather than code repair. GranRoute must cite this and explain how its approach differs or extends MoG for the code repair domain.

2. **arXiv:2604.00167 (April 2026)** -- The empirical study on FL granularity impact for repository-scale repair. This paper provides the empirical motivation that GranRoute's router exploits. Must be cited; GranRoute should position itself as the natural next step (learning to select, not just studying the effect).

3. **arXiv:2604.05481 (April 2026)** -- Complementary study on FL context role. Confirms per-instance variation. Must be cited alongside the above.

Secondary papers to consider citing: RAGRouter (NeurIPS 2025), UniversalRAG, TypeRepair, BoundaryRouter, and Uno-Orchestra as evidence that learned routing/configuration selection is a growing paradigm across ML and SE.

Sources:
- [FL Granularity Impact Study](https://arxiv.org/abs/2604.00167)
- [FL Context Role Study](https://arxiv.org/abs/2604.05481)
- [Mix-of-Granularity (COLING 2025)](https://aclanthology.org/2025.coling-main.384/)
- [RAGRouter (NeurIPS 2025)](https://arxiv.org/abs/2505.23052)
- [UniversalRAG](https://arxiv.org/abs/2504.20734)
- [ExpertRAG](https://arxiv.org/abs/2504.08744)
- [TypeRepair](https://link.springer.com/article/10.1007/s11219-026-09751-w)
- [BoundaryRouter](https://arxiv.org/abs/2605.07180)
- [Uno-Orchestra](https://arxiv.org/abs/2605.05007)
- [ReCode (CIKM 2025)](https://arxiv.org/abs/2509.02330)
- [RelRepair](https://arxiv.org/abs/2509.16701)
- [AdaPatcher (AAAI 2025)](https://arxiv.org/abs/2503.06510)
- [ARISE](https://arxiv.org/abs/2605.03117)
- [ReAPR](https://link.springer.com/article/10.1007/s11219-025-09728-1)
- [ARCS](https://arxiv.org/abs/2504.20434)
- [Agentless-Lite](https://github.com/sorendunn/Agentless-Lite)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "006e1c4a-846a-466c-9622-9c8ead85417e",
  "isSidechain": true,
  "agentId": "aab2b9a0d81eac379",
  "requestId": "req_011Cawgzv7wnz7ENAtFnWzpG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76c9e6ba-f04c-4a24-8c21-44ce4d3ded7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "814ac75a-c3b1-4f47-9a69-4e25d98c82d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013TwRJ1JZE5exNt5ChyFh7z",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 987,
      "cache_read_input_tokens": 34012,
      "output_tokens": 3205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 987
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3205,
          "cache_read_input_tokens": 34012,
          "cache_creation_input_tokens": 987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 987,
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
