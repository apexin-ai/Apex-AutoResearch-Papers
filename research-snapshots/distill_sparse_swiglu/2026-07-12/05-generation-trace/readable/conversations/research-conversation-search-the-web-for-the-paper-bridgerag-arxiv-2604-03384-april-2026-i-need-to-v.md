# Research conversation: Search the web for the paper "BridgeRAG" (arxiv 2604.03384, April 2026). I need to verify: 1. Does this paper exist on a

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aadc9a8404668e13f.jsonl`
- **Structured JSON:** [`89654a6a81224aa3874e.json`](../../sessions/89/89654a6a81224aa3874e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-14T16:58:28.943Z_

Search the web for the paper "BridgeRAG" (arxiv 2604.03384, April 2026). I need to verify:
1. Does this paper exist on arXiv?
2. Does it use a "tripartite scorer s(q,b,c)" for bridge-conditioned retrieval?
3. What are its claimed R@5 results on HotpotQA, MuSiQue, and 2WikiMultiHopQA?
4. Does it demonstrate that bridge conditioning selectively helps bridge_comparison queries (+2.55pp) while showing ~0 gain on other subtypes?
5. Is it training-free as claimed?

Use WebSearch and WebFetch to verify. Report specific numbers and details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "aadc9a8404668e13f",
  "type": "user",
  "uuid": "e57f1869-5c9c-4c2a-82af-90836501aefb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T16:58:28.945Z_

```json
{
  "parentUuid": "e57f1869-5c9c-4c2a-82af-90836501aefb",
  "isSidechain": true,
  "agentId": "aadc9a8404668e13f",
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
  "uuid": "65aea1fa-a10a-47f6-89b9-5cec4f517d51",
  "timestamp": "2026-05-14T16:58:28.945Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T16:58:31.720Z_



I'll search for this paper using WebSearch and WebFetch. Let me start by loading those tool schemas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65aea1fa-a10a-47f6-89b9-5cec4f517d51",
  "isSidechain": true,
  "agentId": "aadc9a8404668e13f",
  "requestId": "req_011Cb2pJYP5Df2gzpqDvdWr5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e23851c8-69a9-4c30-8797-d33112f4e96b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018m3XN9MM2GDa77yTWFJawN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 714,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 714,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 4 · 2026-05-14T16:58:31.814Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HLS9RcJMKftvG84PzLAe3U`</summary>

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
  "parentUuid": "e23851c8-69a9-4c30-8797-d33112f4e96b",
  "isSidechain": true,
  "agentId": "aadc9a8404668e13f",
  "requestId": "req_011Cb2pJYP5Df2gzpqDvdWr5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bf23e0a-20c2-45aa-bf7a-b0b86c3d84ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018m3XN9MM2GDa77yTWFJawN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 714,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 714,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 5 · 2026-05-14T16:58:31.817Z_

<details><summary>↩ Tool result · `toolu_01HLS9RcJMKftvG84PzLAe3U`</summary>

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
  "parentUuid": "1bf23e0a-20c2-45aa-bf7a-b0b86c3d84ff",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "aadc9a8404668e13f",
  "type": "user",
  "uuid": "d0e77b50-38f0-43ba-88d3-895b2cd7d58e",
  "sourceToolAssistantUUID": "1bf23e0a-20c2-45aa-bf7a-b0b86c3d84ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T16:58:34.342Z_



Now let me search for the paper and fetch its arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0e77b50-38f0-43ba-88d3-895b2cd7d58e",
  "isSidechain": true,
  "agentId": "aadc9a8404668e13f",
  "requestId": "req_011Cb2pJkz7LJgbZ7BNs9tzp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad7ab53c-9255-4a43-bbdb-c32d4b642334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jHPDgwgvSLE84NkLKcJPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-14T16:58:34.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012uPQu7kAPH1cYVsG2qYpJu`</summary>

```json
{
  "query": "BridgeRAG arxiv 2604.03384 April 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad7ab53c-9255-4a43-bbdb-c32d4b642334",
  "isSidechain": true,
  "agentId": "aadc9a8404668e13f",
  "requestId": "req_011Cb2pJkz7LJgbZ7BNs9tzp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "631a1c08-bc29-4793-8faa-c53c4d17a008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jHPDgwgvSLE84NkLKcJPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-14T16:58:35.768Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017wbPDh1EASmyBGRJd9mi3t`</summary>

```json
{
  "query": "BridgeRAG bridge-conditioned retrieval multi-hop question answering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "631a1c08-bc29-4793-8faa-c53c4d17a008",
  "isSidechain": true,
  "agentId": "aadc9a8404668e13f",
  "requestId": "req_011Cb2pJkz7LJgbZ7BNs9tzp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31ae4af8-de8c-4c8a-a2e0-7432f7cfdfd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jHPDgwgvSLE84NkLKcJPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 9 · 2026-05-14T16:58:37.337Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014A1p9ovjdK3Hg8S8Foey3E`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03384",
  "prompt": "Extract the full title, authors, abstract, and any details about the paper's methodology (especially any \"tripartite scorer\" or scoring function s(q,b,c)), claimed results on HotpotQA, MuSiQue, and 2WikiMultiHopQA (especially R@5), whether it is training-free, and any analysis of bridge_comparison queries vs other subtypes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31ae4af8-de8c-4c8a-a2e0-7432f7cfdfd3",
  "isSidechain": true,
  "agentId": "aadc9a8404668e13f",
  "requestId": "req_011Cb2pJkz7LJgbZ7BNs9tzp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c6ef4bd-4d8b-4bdf-843d-2b36a8a74e6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jHPDgwgvSLE84NkLKcJPj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8937,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 294,
          "cache_read_input_tokens": 8937,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
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

_source line 10 · 2026-05-14T16:58:40.443Z_

<details><summary>↩ Tool result · `toolu_012uPQu7kAPH1cYVsG2qYpJu`</summary>

```text
Web search results for query: "BridgeRAG arxiv 2604.03384 April 2026"

Links: [{"title":"[2604.23425] When the Agent Is the Adversary: Architectural Requirements for Agentic AI Containment After the April 2026 Frontier Model Escape","url":"https://arxiv.org/abs/2604.23425"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1000&show=1000"},{"title":"Envisioning the Future, One Step at a Time","url":"https://arxiv.org/html/2604.09527v1"},{"title":"arXiv:2604.11364v1 [cs.AI] 13 Apr 2026","url":"https://arxiv.org/pdf/2604.11364"},{"title":"[2603.26668] Bridge-RAG: An Abstract Bridge Tree Based Retrieval Augmented Generation Algorithm With Cuckoo Filter","url":"https://arxiv.org/abs/2603.26668"},{"title":"Bridge-RAG: An Abstract Bridge Tree Based Retrieval Augmented Generation Algorithm With Cuckoo Filter","url":"https://arxiv.org/html/2603.26668"},{"title":"1 Invariant-mass distribution of selected 𝐵⁺→𝐾⁺⁢𝐽/𝜓⁢(𝑒⁺⁢𝑒⁻) candidates. The results of the fit are also shown. Some fit components are too small to be visible.","url":"https://arxiv.org/html/2604.26784"},{"title":"[2604.20496] Mythos and the Unverified Cage: Z3-Based Pre-Deployment Verification for Frontier-Model Sandbox Infrastructure","url":"https://arxiv.org/abs/2604.20496"},{"title":"[2604.19417] MER 2026: From Discriminative Emotion Recognition to Generative Emotion Understanding","url":"https://arxiv.org/abs/2604.19417"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2604.14199"}]

Based on the search results, I found information about BridgeRAG, though the exact arxiv ID you mentioned (2604.03384) doesn't appear in the results. However, I did find a closely related paper:

Bridge-RAG is a novel RAG framework that introduces the concept of abstract to bridge query entities and document chunks, providing robust semantic understanding. The framework organizes abstracts into a tree structure and designs a multi-level approach to overcome accuracy challenges in retrieval augmented generation.

The paper I found was published on arxiv as 2603.26668 (from January 12, 2026), not the specific arxiv ID you mentioned. The paper appears to present an abstract bridge tree-based retrieval augmented generation algorithm with a Cuckoo Filter.

If you're looking for a specific paper with the arxiv ID 2604.03384 from April 2026, it's possible that particular arxiv ID may not be indexed in the search results, or there may be a slight variation in the ID number. Would you like me to search with different terms or clarify which specific BridgeRAG paper you're interested in?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "631a1c08-bc29-4793-8faa-c53c4d17a008",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "aadc9a8404668e13f",
  "type": "user",
  "uuid": "65287b7a-21b9-4a84-8534-062cb98dfb0c",
  "sourceToolAssistantUUID": "631a1c08-bc29-4793-8faa-c53c4d17a008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T16:58:42.742Z_

<details><summary>↩ Tool result · `toolu_014A1p9ovjdK3Hg8S8Foey3E`</summary>

```text
# BridgeRAG Paper Summary

**Full Title:** "BridgeRAG: Training-Free Bridge-Conditioned Retrieval for Multi-Hop Question Answering"

**Author:** Andre Bacellar

**Core Methodology:**
The paper introduces a tripartite scoring function s(q,b,c) that evaluates relevance based on three components: question, bridge evidence, and candidate passages. Rather than ranking later-hop evidence solely by similarity to the original query, this approach conditions scoring on retrieved bridge evidence. The method combines "dual-entity ANN expansion" for broadening candidate pools with an LLM judge that identifies active reasoning chains.

**Key Experimental Findings:**
- The conditioning signal proves selective: showing "+2.55pp on parallel-chain queries" but negligible gains on single-chain subtypes
- Bridge conditioning produces meaningful re-ranking effects, with an "18.7% flip-win rate on parallel-chain vs. 0.6% on single-chain"

**Benchmark Results (R@5 metrics):**
- MuSiQue: 0.8146
- 2WikiMultiHopQA: 0.9527  
- HotpotQA: 0.9875

**Training-Free Status:** Yes, explicitly stated as "training-free, graph-free retrieval method"

**Submission Details:** arXiv:2604.03384, submitted April 3, 2026, revised April 28, 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c6ef4bd-4d8b-4bdf-843d-2b36a8a74e6b",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "aadc9a8404668e13f",
  "type": "user",
  "uuid": "e6c3e243-9670-4e89-adb4-c07b72194ae1",
  "sourceToolAssistantUUID": "8c6ef4bd-4d8b-4bdf-843d-2b36a8a74e6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T16:58:46.687Z_

<details><summary>↩ Tool result · `toolu_017wbPDh1EASmyBGRJd9mi3t`</summary>

```text
Web search results for query: "BridgeRAG bridge-conditioned retrieval multi-hop question answering 2026"

Links: [{"title":"BridgeRAG: Training-Free Bridge-Conditioned Retrieval for Multi-Hop Question Answering","url":"https://arxiv.org/html/2604.03384v1"},{"title":"2wikimultihopqa","url":"https://www.catalyzex.com/s/2wikimultihopqa"},{"title":"Constructing A Multi-hop QA Dataset for Comprehensive Evaluation of Reasoning Steps | Request PDF","url":"https://www.researchgate.net/publication/348345157_Constructing_A_Multi-hop_QA_Dataset_for_Comprehensive_Evaluation_of_Reasoning_Steps"},{"title":"MultiHop-RAG: Benchmarking Retrieval-Augmented Gener","url":"https://openreview.net/pdf/43ab88c33fb4e13c3e723aaf46617f8e731d97c9.pdf"},{"title":"CREDIBLE PLAN-DRIVEN RAG METHOD FOR MULTI-HOP QUESTION ANSWERING","url":"https://arxiv.org/pdf/2504.16787"},{"title":"[2603.07931] BRIDGE: Benchmark for multi-hop Reasoning In long multimodal Documents with Grounded Evidence","url":"https://arxiv.org/abs/2603.07931"},{"title":"Page 1/21 Structured Knowledge for Multi-hop QA: A","url":"https://www.researchsquare.com/article/rs-8283065/v1.pdf"},{"title":"BRIDGE: Benchmark for multi-hop Reasoning In long multimodal Documents with Grounded Evidence","url":"https://arxiv.org/html/2603.07931"},{"title":"DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop Question Answering","url":"https://arxiv.org/html/2504.18243v1"},{"title":"(PDF) BRIDGE: Benchmark for multi-hop Reasoning In long multimodal Documents with Grounded Evidence","url":"https://www.researchgate.net/publication/401720386_BRIDGE_Benchmark_for_multi-hop_Reasoning_In_long_multimodal_Documents_with_Grounded_Evidence"}]

Based on the search results, here's what I found about BridgeRAG:

## BridgeRAG Overview

BridgeRAG is a training-free, graph-free retrieval method for retrieval-augmented generation (RAG) over multi-hop questions that operationalizes bridge-conditioned scoring with a tripartite scorer s(q,b,c) over (question, bridge, candidate).

## Key Concept

Multi-hop retrieval is not a single-step relevance problem: later-hop evidence should be ranked by its utility conditioned on retrieved bridge evidence, not by similarity to the original query alone.

## Technical Approach

BridgeRAG separates coverage from scoring: dual-entity ANN expansion broadens the second-hop candidate pool, while a bridge-conditioned LLM judge identifies the active reasoning chain among competing candidates without any offline graph or proposition index. BridgeRAG requires no training; all reasoning is performed by an off-the-shelf LLM.

## Performance Results

BridgeRAG achieves the best published training-free R@5 under matched benchmark evaluation on all three standard MHQA benchmarks without a graph database or any training: 0.8146 on MuSiQue (+3.1pp vs. PropRAG, +6.8pp vs. HippoRAG2), 0.9527 on 2WikiMultiHopQA (+1.2pp vs. PropRAG), and 0.9875 on HotpotQA (+1.35pp vs. PropRAG).

The paper was published in April 2026 on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31ae4af8-de8c-4c8a-a2e0-7432f7cfdfd3",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "aadc9a8404668e13f",
  "type": "user",
  "uuid": "43102d36-5546-429c-92af-8ac3e8a8b27f",
  "sourceToolAssistantUUID": "31ae4af8-de8c-4c8a-a2e0-7432f7cfdfd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-14T16:58:49.882Z_

Good, I found the paper. Now let me fetch the full HTML version to get more specific details, especially about the bridge_comparison queries and the exact numbers claimed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43102d36-5546-429c-92af-8ac3e8a8b27f",
  "isSidechain": true,
  "agentId": "aadc9a8404668e13f",
  "requestId": "req_011Cb2pKrewyXkTXmv3FxwLV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60b27d28-a083-4071-93f1-96fd7372bf8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFZaEVV8czDDqBQvNtqqKv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 368,
      "cache_creation_input_tokens": 2117,
      "cache_read_input_tokens": 10850,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2117,
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

_source line 14 · 2026-05-14T16:58:53.784Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JAdq1xmfW6ZBjXPwV5JmP3`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.03384v1",
  "prompt": "Extract the following specific details:\n1. The exact definition of the tripartite scorer s(q,b,c) - what do q, b, and c stand for?\n2. The exact R@5 numbers on HotpotQA, MuSiQue, and 2WikiMultiHopQA - include comparison numbers vs baselines.\n3. Any analysis of bridge_comparison queries specifically - does it mention '+2.55pp' gain on bridge_comparison? What about gains on other subtypes? Is the gain on other subtypes approximately zero?\n4. Details about being training-free - what exactly does the paper claim?\n5. The full author list and submission date.\n6. Any tables with detailed results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60b27d28-a083-4071-93f1-96fd7372bf8b",
  "isSidechain": true,
  "agentId": "aadc9a8404668e13f",
  "requestId": "req_011Cb2pKrewyXkTXmv3FxwLV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d870c2df-0635-46a1-86df-2675d8aa2104",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFZaEVV8czDDqBQvNtqqKv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 368,
      "cache_creation_input_tokens": 2117,
      "cache_read_input_tokens": 10850,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2117,
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

_source line 15 · 2026-05-14T16:58:54.662Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N13xwTxZJ6o8DWVGr3nRjy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03384",
  "prompt": "Extract the full abstract, author list, submission date, and any version information for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d870c2df-0635-46a1-86df-2675d8aa2104",
  "isSidechain": true,
  "agentId": "aadc9a8404668e13f",
  "requestId": "req_011Cb2pKrewyXkTXmv3FxwLV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4816fffe-84ce-479e-95a4-7eb07da59ffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFZaEVV8czDDqBQvNtqqKv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 368,
      "cache_creation_input_tokens": 2117,
      "cache_read_input_tokens": 10850,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2117
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 368,
          "output_tokens": 364,
          "cache_read_input_tokens": 10850,
          "cache_creation_input_tokens": 2117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2117,
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

_source line 16 · 2026-05-14T16:58:59.207Z_

<details><summary>↩ Tool result · `toolu_01N13xwTxZJ6o8DWVGr3nRjy`</summary>

```text
# BridgeRAG Paper Information

**Author:** Andre Bacellar

**Submission Date:** Submitted on April 3, 2026 (v1); Last revised April 28, 2026 (v2)

**Abstract Summary:**
The paper addresses multi-hop retrieval for question answering by proposing that later-hop evidence should be ranked based on utility conditioned on previously retrieved bridge evidence, rather than similarity to the original query alone. BridgeRAG employs a "training-free, graph-free retrieval method" that uses a tripartite scoring function across question, bridge, and candidate elements. The approach combines dual-entity expansion with an LLM judge to identify reasoning chains. The research demonstrates selective improvements on parallel-chain queries (+2.55 percentage points) and achieves top performance across three benchmarks: MuSiQue (0.8146 R@5), 2WikiMultiHopQA (0.9527), and HotpotQA (0.9875), without requiring offline graphs or training data.

**Version Information:**
- v1: April 3, 2026
- v2: April 28, 2026 (current version)

**Classification:** Computer Science > Information Retrieval (cs.IR)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4816fffe-84ce-479e-95a4-7eb07da59ffa",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "aadc9a8404668e13f",
  "type": "user",
  "uuid": "c162af28-5683-4bd6-bf82-cbe5e1f49cb4",
  "sourceToolAssistantUUID": "4816fffe-84ce-479e-95a4-7eb07da59ffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T16:59:00.361Z_

<details><summary>↩ Tool result · `toolu_01JAdq1xmfW6ZBjXPwV5JmP3`</summary>

```text
# BridgeRAG Paper Details

## 1. Tripartite Scorer Definition

The tripartite scorer **s(q,b,c)** is defined as follows:
- **q** = the original natural-language query
- **b** = the bridge passage (top-1 result from hop-1 retrieval)
- **c** = a candidate passage for hop-2 retrieval

The paper states: "Later-hop evidence should be ranked by its utility conditioned on retrieved bridge evidence, not by similarity to the original query alone."

## 2. R@5 Results

**BridgeRAG vs. PropRAG (primary baseline):**
- **MuSiQue**: 0.8146 (+3.1pp)
- **2WikiMultiHopQA**: 0.9527 (+1.2pp)
- **HotpotQA**: 0.9875 (+1.35pp)

vs. HippoRAG2: MuSiQue +6.8pp advantage.

## 3. Bridge_Comparison Analysis

Yes, the paper explicitly documents: "Bridge conditioning improves exclusively bridge_comparison (+2.55pp, p<0.001)" while showing "≈0" gains on compositional, comparison, and inference subtypes. On the full 2WikiMultiHopQA dataset, the B→C gain is +0.90pp (p=3×10⁻⁶).

## 4. Training-Free Claims

The paper emphasizes: "training-free...method...without any offline graph or proposition index required" and "requires no training; all reasoning is performed by an off-the-shelf LLM."

## 5. Author and Date

**Author**: Andre Bacellar (andremi@gmail.com)
**Submission**: arXiv:2604.03384v1, April 3, 2026

## 6. Key Results Table

See Table 2 in the paper showing all three benchmark comparisons with ablation conditions A, B, and C across datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d870c2df-0635-46a1-86df-2675d8aa2104",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "aadc9a8404668e13f",
  "type": "user",
  "uuid": "3610afad-2b01-4e68-842e-b39be2f81f73",
  "sourceToolAssistantUUID": "d870c2df-0635-46a1-86df-2675d8aa2104",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T16:59:15.678Z_

I now have comprehensive details. Here is my verification report:

---

**Paper: "BridgeRAG: Training-Free Bridge-Conditioned Retrieval for Multi-Hop Question Answering"**

**1. Does this paper exist on arXiv?**

Yes. It exists at arXiv:2604.03384, classified under cs.IR (Information Retrieval). Author: Andre Bacellar. Submitted April 3, 2026 (v1), revised April 28, 2026 (v2). The full HTML version is available at `https://arxiv.org/html/2604.03384v1`.

**2. Does it use a "tripartite scorer s(q,b,c)" for bridge-conditioned retrieval?**

Yes. The paper defines a tripartite scoring function **s(q, b, c)** where:
- **q** = the original natural-language query
- **b** = the bridge passage (top-1 result from hop-1 retrieval)
- **c** = a candidate passage for hop-2 retrieval

The core idea is that later-hop evidence should be ranked by its utility conditioned on the retrieved bridge evidence, rather than by similarity to the original query alone.

**3. Claimed R@5 results on the three benchmarks:**

| Benchmark | R@5 | Gain vs. PropRAG | Gain vs. HippoRAG2 |
|---|---|---|---|
| HotpotQA | **0.9875** | +1.35 pp | -- |
| MuSiQue | **0.8146** | +3.1 pp | +6.8 pp |
| 2WikiMultiHopQA | **0.9527** | +1.2 pp | -- |

These are claimed as the best published training-free R@5 under matched benchmark evaluation on all three standard MHQA benchmarks.

**4. Does bridge conditioning selectively help bridge_comparison queries (+2.55pp) with ~0 gain on other subtypes?**

Yes, this is explicitly documented. The paper states that bridge conditioning improves **exclusively** the bridge_comparison subtype by **+2.55 pp (p < 0.001)**, while showing approximately zero ("~0") gains on compositional, comparison, and inference subtypes. Supporting this, the paper reports an 18.7% flip-win rate on parallel-chain (bridge_comparison) queries vs. only 0.6% on single-chain subtypes. On the full 2WikiMultiHopQA dataset, the aggregate B-to-C gain is +0.90 pp (p = 3 x 10^-6).

**5. Is it training-free as claimed?**

Yes. The paper explicitly and repeatedly claims it is "training-free" and "graph-free." It states: "requires no training; all reasoning is performed by an off-the-shelf LLM." There is no offline graph construction or proposition index required. The method relies on dual-entity ANN expansion for candidate broadening and an LLM judge for bridge-conditioned scoring.

---

**Summary:** All five claims you asked me to verify are confirmed by the paper. The arXiv ID, tripartite scorer formulation, R@5 numbers, selective bridge_comparison improvement (+2.55pp with ~0 on other subtypes), and training-free status all match what was described.

Sources:
- [BridgeRAG HTML (arXiv)](https://arxiv.org/html/2604.03384v1)
- [BridgeRAG Abstract (arXiv)](https://arxiv.org/abs/2604.03384)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3610afad-2b01-4e68-842e-b39be2f81f73",
  "isSidechain": true,
  "agentId": "aadc9a8404668e13f",
  "requestId": "req_011Cb2pLrgxkUrxHRAKgF8Jj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "956cb1a1-2eba-43fb-94ba-df94793455be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCc2vTQkUD1g1oAYikXW5P",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 316,
      "cache_creation_input_tokens": 1236,
      "cache_read_input_tokens": 12967,
      "output_tokens": 860,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1236
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 316,
          "output_tokens": 860,
          "cache_read_input_tokens": 12967,
          "cache_creation_input_tokens": 1236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1236,
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
