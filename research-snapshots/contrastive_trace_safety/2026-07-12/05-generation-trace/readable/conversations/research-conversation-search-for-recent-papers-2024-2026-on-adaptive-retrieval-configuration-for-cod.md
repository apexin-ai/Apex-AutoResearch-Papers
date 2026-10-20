# Research conversation: Search for recent papers (2024-2026) on adaptive retrieval configuration for code repair or code generation. I need to f

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aff9ac7a51a59e977.jsonl`
- **Structured JSON:** [`281748b992a8cb395cda.json`](../../sessions/28/281748b992a8cb395cda.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-12T00:19:27.266Z_

Search for recent papers (2024-2026) on adaptive retrieval configuration for code repair or code generation. I need to find any work the proposal may have missed. Use WebSearch with these queries:

1. "adaptive retrieval granularity code repair 2025 2026"
2. "fault localization context selection LLM program repair"
3. "retrieval-augmented code repair adaptive context"
4. "site:arxiv.org code repair retrieval configuration 2026"
5. "per-instance retrieval adaptation code generation"

Report any papers found that are relevant to dynamically selecting retrieval granularity or context configuration for code tasks. Include titles, venues, and brief descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "aff9ac7a51a59e977",
  "type": "user",
  "uuid": "6e49fb1e-b0cf-43d0-9b40-a962ccaedc58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-12T00:19:28.565Z_

I'll search for recent papers on adaptive retrieval configuration for code repair and code generation using the specified queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e49fb1e-b0cf-43d0-9b40-a962ccaedc58",
  "isSidechain": true,
  "agentId": "aff9ac7a51a59e977",
  "requestId": "req_011CawiW9otYJ4w3JQeswX6r",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "515afd65-3aec-4c02-9646-6c8ea7ec40af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhdBx7LUmQhxhoLur7nEyd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 577,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T00:19:28.815Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QhU5cLQGg4foP8eV39jdL7`</summary>

```json
{
  "query": "adaptive retrieval granularity code repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "515afd65-3aec-4c02-9646-6c8ea7ec40af",
  "isSidechain": true,
  "agentId": "aff9ac7a51a59e977",
  "requestId": "req_011CawiW9otYJ4w3JQeswX6r",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1b5025ce-38ab-46c1-9070-946baf9d45eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhdBx7LUmQhxhoLur7nEyd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 577,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T00:19:29.015Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GCuyZAVPLZuuw1poFCRY5Z`</summary>

```json
{
  "query": "fault localization context selection LLM program repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b5025ce-38ab-46c1-9070-946baf9d45eb",
  "isSidechain": true,
  "agentId": "aff9ac7a51a59e977",
  "requestId": "req_011CawiW9otYJ4w3JQeswX6r",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9bd8e07b-1b51-45fc-b49c-2a3d69c1f988",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhdBx7LUmQhxhoLur7nEyd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 577,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T00:19:29.019Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U3XJFu8F1WageFmQQQWeTu`</summary>

```json
{
  "query": "retrieval-augmented code repair adaptive context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bd8e07b-1b51-45fc-b49c-2a3d69c1f988",
  "isSidechain": true,
  "agentId": "aff9ac7a51a59e977",
  "requestId": "req_011CawiW9otYJ4w3JQeswX6r",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ea6c7fe3-dbc2-4619-8206-5e133c6af594",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhdBx7LUmQhxhoLur7nEyd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 577,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-12T00:19:29.226Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NvGZAgd13rmhh1ZXBND53m`</summary>

```json
{
  "query": "site:arxiv.org code repair retrieval configuration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea6c7fe3-dbc2-4619-8206-5e133c6af594",
  "isSidechain": true,
  "agentId": "aff9ac7a51a59e977",
  "requestId": "req_011CawiW9otYJ4w3JQeswX6r",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9a673fb6-5208-4013-beb0-06621a7e9578",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhdBx7LUmQhxhoLur7nEyd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 16153,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 265,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 577,
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

_source line 7 · 2026-05-12T00:19:29.291Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PxgsjB7JtaJQuvpaAZ6fbv`</summary>

```json
{
  "query": "per-instance retrieval adaptation code generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a673fb6-5208-4013-beb0-06621a7e9578",
  "isSidechain": true,
  "agentId": "aff9ac7a51a59e977",
  "requestId": "req_011CawiW9otYJ4w3JQeswX6r",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9b3fa189-98b4-4359-9e9a-2fead6c12c20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhdBx7LUmQhxhoLur7nEyd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 16153,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 265,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 577,
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

_source line 8 · 2026-05-12T00:19:36.119Z_

<details><summary>↩ Tool result · `toolu_01QhU5cLQGg4foP8eV39jdL7`</summary>

```text
Web search results for query: "adaptive retrieval granularity code repair 2025 2026"

Links: [{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"CIRAG: Construction-Integration Retrieval and Adaptive Generation for","url":"https://www.arxiv.org/pdf/2601.06799"},{"title":"Optimize the Chunking Granularity for Retrieval- ...","url":"https://aclanthology.org/2025.coling-main.384.pdf"},{"title":"Retrieval-Augmented Generation for AI-Generated Content: A Survey | Data Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41019-025-00335-5"},{"title":"Adaptive Granularity Retrieval for Retrieval-Augmented Generation - Fondazione Links","url":"https://linksfoundation.com/en/faq-items/adaptive-granularity-retrieval-for-retrieval-augmented-generation-2/"},{"title":"[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/abs/2510.04905"}]

Based on the web search results, here's what I found about adaptive retrieval granularity and code repair in 2025-2026:

## Recent Research on Adaptive Retrieval Granularity

A current research challenge is the "Granularity-Demand Mismatch," where current paradigms typically adopt a static evidence representation, failing to account for the heterogeneous information needs of different questions. This approach often leads to mismatches between the information need and the retrieved evidence: broad questions demand high-level summaries, while specific factoid queries require fine-grained snippets, making it challenging to design a retrieval system that can dynamically adapt to the level of detail a query requires.

## Code Repair Applications

Remaining challenges in code repair include pre-processing overhead, coverage of dynamic behavior, and balancing retrieval granularity against token economy. 

Recent work in 2025 has explored approaches that exploit the in-context learning capabilities of large language models and employ filtering mechanisms to select optimal repair examples generated by the model itself.

RelRepair introduces a novel approach that retrieves relevant code to enhance automated program repair, leveraging a specialized RAG strategy for program repair tasks by identifying and incorporating relevant function signatures and code snippets to guide LLMs to generate more accurate and informed patches.

## Survey Work

The diversity in retrieval strategies directly influences the quality and granularity of the generated code. A comprehensive survey covering the period through August 2025 provides extensive analysis of retrieval-augmented code generation approaches at repository scale.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b5025ce-38ab-46c1-9070-946baf9d45eb",
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "aff9ac7a51a59e977",
  "type": "user",
  "uuid": "052e1824-4d43-4d39-9eda-e2ff6db35e62",
  "sourceToolAssistantUUID": "1b5025ce-38ab-46c1-9070-946baf9d45eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-12T00:19:36.290Z_

<details><summary>↩ Tool result · `toolu_01U3XJFu8F1WageFmQQQWeTu`</summary>

```text
Web search results for query: "retrieval-augmented code repair adaptive context"

Links: [{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Optimizing Code Runtime Performance through Context-Aware Retrieval-Augmented Generation","url":"https://arxiv.org/html/2501.16692"},{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation | Proceedings of the 34th ACM International Conference on Information and Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3746252.3761035"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/abs/2510.04905"},{"title":"Enhancing Large Language Models with Retrieval Augmented Generation for Software Testing and Inspection Automation","url":"https://arxiv.org/html/2604.15270"},{"title":"CAST: Enhancing Code Retrieval-Augmented Generation","url":"https://www.cs.cmu.edu/~sherryw/assets/pubs/2025-cast.pdf"},{"title":"[2509.02330] ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2509.02330"}]

Based on the search results, I found several recent research papers on retrieval-augmented code repair with adaptive context. Here are the key findings:

## ReCode Framework

ReCode is a fine-grained retrieval-augmented generation framework that constructs modular representations for both source code and its accompanying textual descriptions. ReCode leverages an algorithm-aware hybrid retrieval mechanism that uses the LLM to analyze the user's query to infer the algorithm type, which is then utilized to retrieve the most relevant exemplars from a pre-constructed algorithm-specific knowledge corpus.

By integrating algorithmic categorization with the model's semantic modeling towards the defective code, ReCode significantly enhances the contextual relevance of retrieved in-context exemplars and supports more accurate and adaptive code repair generation.

## Key Advantages

Conventional retrieval strategies, which are often based on holistic code-text embeddings, fail to capture the structural intricacies of code, resulting in suboptimal retrieval quality. ReCode improves the relevance of retrieved exemplars and enables accurate, efficient repair without additional training, with experiments on RACodeBench and competitive programming datasets showing that ReCode outperforms existing methods in both repair accuracy and inference efficiency.

## Context-Aware Optimization

Beyond code repair, related work on guiding large language models with structural context enables them to produce optimizations that align more closely with real-world developer best practices. Recent works have explored iterative or agent-style RACG frameworks, where retrieval and generation are conducted in multi-step loops with intermediate reasoning, tool execution, or reflection, enhancing the adaptability and robustness of RACG systems in complex repository-scale environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea6c7fe3-dbc2-4619-8206-5e133c6af594",
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "aff9ac7a51a59e977",
  "type": "user",
  "uuid": "42aae485-69cc-4e87-ae2b-728277e7d3c4",
  "sourceToolAssistantUUID": "ea6c7fe3-dbc2-4619-8206-5e133c6af594",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T00:19:37.201Z_

<details><summary>↩ Tool result · `toolu_01NvGZAgd13rmhh1ZXBND53m`</summary>

```text
Web search results for query: "site:arxiv.org code repair retrieval configuration 2026"

Links: [{"title":"Learner-Tailored Program Repair: A Solution Generator with","url":"https://arxiv.org/pdf/2601.08545"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2505.23932"},{"title":"RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code","url":"https://arxiv.org/html/2509.16701"},{"title":"SCPatcher: Automated Smart Contract Code Repair via Retrieval-Augmented Generation and Knowledge Graph","url":"https://arxiv.org/html/2604.00687v1"},{"title":"Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/html/2601.08545.pdf"},{"title":"TopoEdge: Topology-Grounded Agentic Framework for Edge Networking Code Generation and Repair","url":"https://arxiv.org/html/2603.00569"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained","url":"https://arxiv.org/pdf/2509.02330"}]

The web search has returned several relevant results about code repair, retrieval, and configuration from arxiv.org. Here are the key findings:

## Notable Papers Found:

1. **"Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement"** (January 2026)
   - Utilizes a repair solution retrieval framework to construct a solution retrieval database and employs an edit-driven code retrieval approach to retrieve valuable solutions

2. **"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches"** (October 2025)
   - Discusses diverse RAG strategies including sparse and dense retrieval, graph-based retrieval, hybrid pipelines, and agent-style retrieval that integrates static code analysis, tool invocation, and iterative refinement

3. **"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair"** (Recent)
   - Builds on the agentic paradigm and targets the localization bottleneck by providing the agent with structured graph-based tools rather than relying on lexical retrieval or free-form code navigation

4. **"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation"** (September 2025)
   - Proposes a fine-grained retrieval-augmented in-context learning framework with an algorithm-aware retrieval strategy that narrows the search space using preliminary algorithm type predictions and a modular dual-encoding approach

5. **"SWINGARENA"** (Published at ICLR 2026)
   - For RACG, limits the number of retrieved files to 5 and allows a maximum of 16 code chunks per query, where each chunk corresponds to a syntactic code chunk, and the retrieval agent supports up to 3 retry attempts to handle transient failures or timeouts


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a673fb6-5208-4013-beb0-06621a7e9578",
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "aff9ac7a51a59e977",
  "type": "user",
  "uuid": "9c8ce679-3ac0-4e95-947b-b693fb8de946",
  "sourceToolAssistantUUID": "9a673fb6-5208-4013-beb0-06621a7e9578",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T00:19:37.628Z_

<details><summary>↩ Tool result · `toolu_01PxgsjB7JtaJQuvpaAZ6fbv`</summary>

```text
Web search results for query: "per-instance retrieval adaptation code generation"

Links: [{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"An Empirical Study of Retrieval-Augmented Code Generation: Challenges and Opportunities | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3717061"},{"title":"An Empirical Study of Retrieval-Augmented Code Generation: Challenges and Opportunities","url":"https://arxiv.org/html/2501.13742"},{"title":"CodeRAG-Bench: Can Retrieval Augment Code Generation?","url":"https://code-rag-bench.github.io/"},{"title":"[2503.20589] What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond","url":"https://arxiv.org/abs/2503.20589"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Preference-Guided Refactored Tuning for Retrieval Augmented Code Generation","url":"https://arxiv.org/html/2409.15895v1"},{"title":"Retrieval-Augmented Code Generation","url":"https://arks-codegen.github.io/"},{"title":"What to Retrieve for Effective Retrieval-Augmented Code ...","url":"https://arxiv.org/pdf/2503.20589"},{"title":"Cognitive-Level Adaptive Generation via Capability-Aware Retrieval and Style Adaptation","url":"https://arxiv.org/html/2509.19336"}]

Based on the search results, I found relevant information about retrieval adaptation and code generation. Here are the key findings:

## Retrieval-Augmented Code Generation Overview

Retrieval-Augmented Generation (RAG) dynamically retrieves relevant content to construct context-aware prompts, improving scalability, interpretability, and explainability while reducing reliance on model memorization. This approach has been extended to software engineering as Retrieval-Augmented Code Generation (RACG).

## Per-Instance Adaptation Approaches

Several recent works address per-instance or adaptive retrieval for code generation:

**EVOR Pipeline**: Existing retrieval-augmented code generation pipelines employ static knowledge bases with a single source, limiting adaptation capabilities. EVOR develops a novel pipeline that employs the synchronous evolution of both queries and diverse knowledge bases.

**Dynamic Retrieval Strategies**: Recent works have explored iterative or agent-style RACG frameworks, where retrieval and generation are conducted in multi-step loops with intermediate reasoning, tool execution, or reflection. These interactive paradigms further enhance the adaptability and robustness of RACG systems in complex repository-scale environments.

**Effective Retrieval Content**: In-context code and potential API information significantly enhance LLM performance, whereas retrieved similar code often introduces noise, degrading results by up to 15%.

## Training and Adaptation

There is growing recognition that aligning retrieval modules with generation tasks and adapting pre-trained models to code-specific domains is important. To adapt to the specific input form of combined query and retrieved code, generators can be fine-tuned, and refactorers can adapt to different requirements or scenarios by simply altering the retriever and generator combinations, maintaining robust performance while significantly reducing development and maintenance costs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b3fa189-98b4-4359-9e9a-2fead6c12c20",
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "aff9ac7a51a59e977",
  "type": "user",
  "uuid": "cf2b4987-58ae-47de-98e8-2981cab87043",
  "sourceToolAssistantUUID": "9b3fa189-98b4-4359-9e9a-2fead6c12c20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T00:19:38.137Z_

<details><summary>↩ Tool result · `toolu_01GCuyZAVPLZuuw1poFCRY5Z`</summary>

```text
Web search results for query: "fault localization context selection LLM program repair"

Links: [{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481"},{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"[2604.05481] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/html/2601.18044"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3660771"},{"title":"Improving LLM-Based Fault Localization with External Memory and Project Context","url":"https://arxiv.org/html/2506.03585v1"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"Hybrid Automated Program Repair by Combining Large Language","url":"https://xgdsmileboy.github.io/files/paper/tosem25-hybrid.pdf"},{"title":"Automated Repair of Programs from Large Language Models Zhiyu Fan","url":"https://people.cs.umass.edu/~brun/class/2024Fall/CS692P/aprllm.pdf"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260118044S/abstract"}]

I've performed the web search for "fault localization context selection LLM program repair" and found several highly relevant recent research papers and studies on this topic. Here's a summary of the key findings:

## Main Research Areas

### 1. **Impact of Fault Localization Context on LLM-Based Program Repair**

Fault Localization (FL) is a key component of Large Language Model (LLM)-based Automated Program Repair (APR), yet its impact remains underexplored. In particular, it is unclear how much localization is needed, whether additional context beyond the predicted buggy location is beneficial, and how such context should be retrieved.

A recent empirical study found that more context does not consistently improve repair performance, with file-level localization being the dominant factor, yielding a 15–17× improvement over a no-file baseline. Interestingly, line-level context expansion frequently degrades performance due to noise amplification.

### 2. **Optimal Context Strategy**

Expanding file context is often associated with improved performance, with successful repairs most commonly observed in configurations with approximately 6–10 relevant files. Additionally, LLM-based retrieval generally outperforms structural heuristics while using fewer files and tokens.

### 3. **Reasoning-Guided Fault Localization**

Recent work explores reasoning-guided approaches where the LLM is presented with one file or code element at a time, together with the problem statement, rather than providing the entire repository and asking the model to select relevant components, which prevents the LLM from being overwhelmed by large code contexts and encourages focused, fine-grained reasoning about each file or element.

### 4. **External Memory and Project Context**

Static Memory provides fixed project and class-level summaries prepared before fault localization to supply essential contextual information. To generate class summaries, the LLM is queried to summarize each class based on its content, with project summary then generated by providing the model with the project name and the aggregated class summaries.

These research findings collectively suggest that context selection for LLM-based program repair requires careful balancing between providing sufficient information and avoiding noise that could confuse the model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bd8e07b-1b51-45fc-b49c-2a3d69c1f988",
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "aff9ac7a51a59e977",
  "type": "user",
  "uuid": "f8ced471-c3c3-491b-ad71-42cfae3f6355",
  "sourceToolAssistantUUID": "9bd8e07b-1b51-45fc-b49c-2a3d69c1f988",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-12T00:19:51.600Z_

## Research Findings: Recent Papers on Adaptive Retrieval Configuration for Code Repair/Generation

Based on the web searches, I found several highly relevant papers from 2024-2026 that address adaptive retrieval configuration, context selection, and granularity for code tasks:

### Most Relevant Papers

**1. On the Role of Fault Localization Context for LLM-Based Program Repair** (2026)
- **Venue**: arXiv
- **Key Finding**: Empirical study showing that more context does not consistently improve repair performance. File-level localization is the dominant factor (15-17x improvement over no-file baseline), while line-level context expansion frequently degrades performance due to noise. Optimal results found with 6-10 relevant files.
- **Relevance**: Directly addresses dynamic context selection and granularity configuration for program repair.

**2. ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation** (September 2025)
- **Venue**: ACM CIKM 2025
- **Key Finding**: Proposes an algorithm-aware hybrid retrieval mechanism that analyzes user queries to infer algorithm type and retrieves relevant exemplars from algorithm-specific knowledge corpus. Uses modular representations for both code and descriptions.
- **Relevance**: Demonstrates adaptive retrieval based on problem characteristics rather than static configuration.

**3. RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code** (2025)
- **Venue**: arXiv
- **Key Finding**: Retrieves relevant code (function signatures and snippets) to guide LLM patch generation using specialized RAG strategies for program repair.
- **Relevance**: Focuses on optimized retrieval granularity specifically for repair tasks.

**4. Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement** (January 2026)
- **Venue**: arXiv
- **Key Finding**: Uses edit-driven code retrieval approach with iterative solution retrieval to dynamically select relevant repair solutions.
- **Relevance**: Per-instance retrieval adaptation through iterative refinement.

**5. ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair** (2026)
- **Venue**: arXiv
- **Key Finding**: Uses graph-based tools and structured representations instead of lexical retrieval, providing agentic systems with fine-grained navigational capabilities.
- **Relevance**: Structured approach to adaptive context selection via graph-based reasoning.

**6. What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond** (March 2025)
- **Venue**: arXiv (2503.20589)
- **Key Finding**: Empirical study finding that in-context code and API information significantly enhance performance (up to 15% improvement), while retrieved similar code introduces noise and degrades results.
- **Relevance**: Addresses what granularity/type of information should be retrieved per-instance.

**7. Improving LLM-Based Fault Localization with External Memory and Project Context** (2025)
- **Venue**: arXiv
- **Key Finding**: Uses static memory with fixed project and class-level summaries prepared before fault localization, dynamically selecting context depth.
- **Relevance**: Pre-computation of multi-level context summaries for dynamic selection.

**8. An Empirical Study of Retrieval-Augmented Code Generation: Challenges and Opportunities** (2025)
- **Venue**: ACM TOSEM
- **Key Finding**: Comprehensive empirical study on RACG identifying challenges and opportunities for adaptive retrieval in code generation.
- **Relevance**: Broad analysis of retrieval configuration challenges across code generation tasks.

### Survey Works Covering Adaptive Approaches

**9. Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches** (October 2025)
- **Venue**: arXiv
- **Coverage**: Discusses diverse RAG strategies including sparse/dense retrieval, graph-based retrieval, hybrid pipelines, and agent-style retrieval with iterative refinement.
- **Relevance**: Comprehensive overview of adaptive retrieval strategies at repository scale.

### Key Themes Across Papers

These papers collectively identify several adaptive retrieval dimensions:
- **Granularity adaptation**: File-level vs. line-level vs. function-level context
- **Type adaptation**: Algorithm-aware retrieval, API information vs. code examples
- **Quantity adaptation**: Optimal number of files/chunks per query
- **Iterative adaptation**: Multi-step retrieval refinement
- **Noise management**: Dynamic filtering to avoid degradation from irrelevant context

Sources:
- [On the Role of Fault Localization Context for LLM-Based Program Repair](https://arxiv.org/abs/2604.05481)
- [ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation](https://arxiv.org/abs/2509.02330)
- [RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code](https://arxiv.org/html/2509.16701)
- [Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement](https://arxiv.org/html/2601.08545.pdf)
- [ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair](https://arxiv.org/html/2605.03117)
- [What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond](https://arxiv.org/abs/2503.20589)
- [Improving LLM-Based Fault Localization with External Memory and Project Context](https://arxiv.org/html/2506.03585v1)
- [An Empirical Study of Retrieval-Augmented Code Generation: Challenges and Opportunities](https://arxiv.org/html/2501.13742)
- [Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches](https://arxiv.org/abs/2510.04905)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8ced471-c3c3-491b-ad71-42cfae3f6355",
  "isSidechain": true,
  "agentId": "aff9ac7a51a59e977",
  "requestId": "req_011CawiWxEeMYJkskioXP52N",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c26ac8a1-fd03-41a6-b315-db7f8228afa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NQBRkxqA4Quk28rezwXDwm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2754,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 16730,
      "output_tokens": 1496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2978
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2754,
          "output_tokens": 1496,
          "cache_read_input_tokens": 16730,
          "cache_creation_input_tokens": 2978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2978,
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
