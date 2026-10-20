# Research conversation: Search the web for the paper on "Regime-Conditional Retrieval" (arxiv 2604.09019, April 2026). I need to verify: 1. Does

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae15a4c4824a5c36f.jsonl`
- **Structured JSON:** [`202f557a17067768def7.json`](../../sessions/20/202f557a17067768def7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-14T16:58:32.198Z_

Search the web for the paper on "Regime-Conditional Retrieval" (arxiv 2604.09019, April 2026). I need to verify:
1. Does this paper exist on arXiv?
2. Does it formalize Q-dominant vs B-dominant retrieval regimes for two-hop QA?
3. Does it train a binary router?
4. What are its claimed improvements (+5.6pp on MuSiQue, +5.3pp on HotpotQA)?
5. Is it limited to binary classification for hop-2 only as claimed?

Use WebSearch and WebFetch to verify. Report specific details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "ae15a4c4824a5c36f",
  "type": "user",
  "uuid": "65c99d88-bc2d-4906-b440-3b43410ce08f",
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

_source line 2 · 2026-05-14T16:58:32.199Z_

```json
{
  "parentUuid": "65c99d88-bc2d-4906-b440-3b43410ce08f",
  "isSidechain": true,
  "agentId": "ae15a4c4824a5c36f",
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
  "uuid": "00f55c4d-7a47-4a46-9a51-fb64144a0b86",
  "timestamp": "2026-05-14T16:58:32.199Z",
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

_source line 3 · 2026-05-14T16:58:35.252Z_



I'll search for this paper using WebSearch and WebFetch. Let me first load those tool schemas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00f55c4d-7a47-4a46-9a51-fb64144a0b86",
  "isSidechain": true,
  "agentId": "ae15a4c4824a5c36f",
  "requestId": "req_011Cb2pJnJjYTon5MYmcpUoZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39740680-2fb3-4698-aeb7-82d48b6696bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSZMt5TgqKr5gLSP3PxzhZ",
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
      "output_tokens": 6,
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

_source line 4 · 2026-05-14T16:58:35.385Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VFaMLbXRpfceoMX9RG6DRz`</summary>

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
  "parentUuid": "39740680-2fb3-4698-aeb7-82d48b6696bd",
  "isSidechain": true,
  "agentId": "ae15a4c4824a5c36f",
  "requestId": "req_011Cb2pJnJjYTon5MYmcpUoZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa6f5112-3344-44d1-8cc2-0521fa56a3b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSZMt5TgqKr5gLSP3PxzhZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 8223,
      "output_tokens": 103,
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
          "output_tokens": 103,
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
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T16:58:35.390Z_

<details><summary>↩ Tool result · `toolu_01VFaMLbXRpfceoMX9RG6DRz`</summary>

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
  "parentUuid": "fa6f5112-3344-44d1-8cc2-0521fa56a3b7",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "ae15a4c4824a5c36f",
  "type": "user",
  "uuid": "f36c626c-8a8b-4c0d-98c9-bbbcde7718b9",
  "sourceToolAssistantUUID": "fa6f5112-3344-44d1-8cc2-0521fa56a3b7",
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

_source line 6 · 2026-05-14T16:58:38.567Z_



Now let me search for the paper and try to fetch it directly from arXiv.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f36c626c-8a8b-4c0d-98c9-bbbcde7718b9",
  "isSidechain": true,
  "agentId": "ae15a4c4824a5c36f",
  "requestId": "req_011Cb2pK2DtMkBdj1gchWa12",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97f2d3ff-5342-4da7-8433-ccb677c8ec51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKYNyXBm8AfN3THZ2SBwbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 7 · 2026-05-14T16:58:39.033Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XXhGuj3Nfxj86GkeCz22xq`</summary>

```json
{
  "query": "arxiv 2604.09019 Regime-Conditional Retrieval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97f2d3ff-5342-4da7-8433-ccb677c8ec51",
  "isSidechain": true,
  "agentId": "ae15a4c4824a5c36f",
  "requestId": "req_011Cb2pK2DtMkBdj1gchWa12",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98cbaeab-4b7f-4600-9a50-2f9ba19f8b58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKYNyXBm8AfN3THZ2SBwbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 8 · 2026-05-14T16:58:39.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019nXDew2rTJqpDWQF15qaKA`</summary>

```json
{
  "query": "\"Regime-Conditional Retrieval\" two-hop QA Q-dominant B-dominant 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98cbaeab-4b7f-4600-9a50-2f9ba19f8b58",
  "isSidechain": true,
  "agentId": "ae15a4c4824a5c36f",
  "requestId": "req_011Cb2pK2DtMkBdj1gchWa12",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8568ce96-54c2-4445-87fe-29280e53a135",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKYNyXBm8AfN3THZ2SBwbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 9 · 2026-05-14T16:58:40.294Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ra9vSLuf3X7aF9yqiXAetH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.09019",
  "prompt": "Extract the full title, authors, abstract, and any details about: Q-dominant vs B-dominant retrieval regimes, binary router, improvements on MuSiQue and HotpotQA benchmarks, and whether the approach is limited to binary classification for hop-2 only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8568ce96-54c2-4445-87fe-29280e53a135",
  "isSidechain": true,
  "agentId": "ae15a4c4824a5c36f",
  "requestId": "req_011Cb2pK2DtMkBdj1gchWa12",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95dc34f6-9fa7-47a5-a692-1294822dc3dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKYNyXBm8AfN3THZ2SBwbm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8916,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1912
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 273,
          "cache_read_input_tokens": 8916,
          "cache_creation_input_tokens": 1912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1912,
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

_source line 10 · 2026-05-14T16:58:45.195Z_

<details><summary>↩ Tool result · `toolu_01Ra9vSLuf3X7aF9yqiXAetH`</summary>

```text
# Regime-Conditional Retrieval: Theory and a Transferable Router for Two-Hop QA

**Author:** Andre Bacellar

## Abstract Summary
The paper addresses two-hop question answering by categorizing queries into distinct regimes. The research formalizes this distinction through theoretical contributions and proposes a practical routing solution.

## Key Distinctions: Q-Dominant vs B-Dominant

The work divides retrieval into two categories:
- **Q-dominant:** The second-hop entity appears explicitly within the question itself
- **B-dominant:** The second-hop entity only surfaces in the bridge passage, not in the original question

## Binary Router Solution

RegimeRouter is described as "a lightweight binary router that selects between question-only and" the alternative approach using relation-bearing sentences. The system leverages five text-based features derived from predicate definitions to make routing decisions.

## Performance Improvements

Results across benchmarks show:
- 2WikiMultiHopQA (training set): +5.6 percentage points
- MuSiQue (zero-shot transfer): +5.3 percentage points  
- HotpotQA (zero-shot transfer): +1.1 percentage points (statistically non-significant)

## Scope Limitation

The approach specifically targets two-hop question answering scenarios and does not address multi-hop questions beyond the two-hop structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95dc34f6-9fa7-47a5-a692-1294822dc3dc",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "ae15a4c4824a5c36f",
  "type": "user",
  "uuid": "942765dc-30fa-47d1-8008-6c4f6bfbfac8",
  "sourceToolAssistantUUID": "95dc34f6-9fa7-47a5-a692-1294822dc3dc",
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

_source line 11 · 2026-05-14T16:58:47.230Z_

<details><summary>↩ Tool result · `toolu_019nXDew2rTJqpDWQF15qaKA`</summary>

```text
Web search results for query: ""Regime-Conditional Retrieval" two-hop QA Q-dominant B-dominant 2026"

Links: [{"title":"Retrieval–Reasoning Processes for Multi-hop Question Answering: A","url":"https://arxiv.org/pdf/2601.00536"},{"title":"Q-RAG: LONG CONTEXT MULTI-STEP RETRIEVAL","url":"https://openreview.net/pdf/b0c7546e92d381f99b83a0e93623e007c1088f4e.pdf"},{"title":"Retrieval–Reasoning Processes for Multi-hop Question Answering: A Four-Axis Design Framework and Empirical Trends","url":"https://arxiv.org/html/2601.00536v1"},{"title":"[2601.00536] Retrieval--Reasoning Processes for Multi-hop Question Answering: A Four-Axis Design Framework and Empirical Trends","url":"https://arxiv.org/abs/2601.00536"},{"title":"Scaling Biomedical Knowledge Graph Retrieval for Interpretable","url":"https://www.medrxiv.org/content/10.64898/2026.01.12.26343957v1.full.pdf"},{"title":"RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/db93ccb6cf392f352570dd5af0a223d3-Paper-Conference.pdf"},{"title":"Reinforcement Learning Enhanced Multi-hop Reasoning for Temporal Knowledge","url":"https://arxiv.org/pdf/2601.01195"},{"title":"Deep Retriever: Information Retrieval for Multi-hop Question Answering","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194/reports/custom/15744425.pdf"},{"title":"Generating multi-hop QA and fine-gRAined Difficulty matrix ...","url":"https://aclanthology.org/2025.findings-emnlp.236.pdf"},{"title":"Revisiting Query Variants: The Advantage of Retrieval Over ...","url":"https://www.arxiv.org/pdf/2510.02512"}]

Based on my web search results, I found research related to multi-hop question answering and retrieval systems, but I did not find a specific paper or work titled "Regime-Conditional Retrieval" with the exact terms "two-hop QA," "Q-dominant," and "B-dominant" that you searched for.

However, the search results do contain several highly relevant papers on multi-hop question answering and retrieval systems from 2025-2026:

1. **Retrieval-Reasoning Processes for Multi-hop QA**: A survey that introduces a four-axis framework covering overall execution plan, index structure, next-step control strategies and triggers, and stop/continue criteria.

2. **Q-RAG**: A system evaluated on open-domain multi-hop QA using HotpotQA, Musique, and RULER benchmarks.

3. **Multi-hop QA Evaluation**: Research examining RAG system performance across a 2D difficulty matrix considering both generator-side and retriever-side complexity.

If you're looking for a specific paper on "Regime-Conditional Retrieval," it's possible that:
- The paper uses different terminology in its title or abstract
- It may be a very recent preprint not yet widely indexed
- The specific terms "Q-dominant" and "B-dominant" might refer to conditions within the methodology rather than the title

Would you like me to search for more specific information about any of these papers, or do you have additional context about the "Regime-Conditional Retrieval" paper you're interested in?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8568ce96-54c2-4445-87fe-29280e53a135",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "ae15a4c4824a5c36f",
  "type": "user",
  "uuid": "34989930-7411-4e70-b9b5-60cebc777f5c",
  "sourceToolAssistantUUID": "8568ce96-54c2-4445-87fe-29280e53a135",
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

_source line 12 · 2026-05-14T16:58:48.131Z_

<details><summary>↩ Tool result · `toolu_01XXhGuj3Nfxj86GkeCz22xq`</summary>

```text
Web search results for query: "arxiv 2604.09019 Regime-Conditional Retrieval"

Links: [{"title":"[2604.09019] Regime-Conditional Retrieval: Theory and a Transferable Router for Two-Hop QA","url":"https://arxiv.org/abs/2604.09019"},{"title":"Regime-Conditional Retrieval: Theory and a Transferable Router for Two-Hop QA","url":"https://arxiv.org/html/2604.09019"},{"title":"Efficient Rationale-based Retrieval: On-policy Distillation from Generative Rerankers based on JEPA","url":"https://arxiv.org/html/2604.23336"},{"title":"Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models","url":"https://arxiv.org/html/2601.07372v1"},{"title":"Conditional Memory via Scalable Lookup: A New Axis of ...","url":"https://arxiv.org/pdf/2601.07372"},{"title":"Bootstrapping Conditional Retrieval for User-to-Item ...","url":"https://arxiv.org/pdf/2508.16793"},{"title":"Entities as Retrieval Signals: A Systematic Study of Coverage, Supervision, and Evaluation in Entity-Oriented Ranking","url":"https://arxiv.org/html/2604.05204v1"},{"title":"PRAG: End-to-End Privacy-Preserving Retrieval-Augmented Generation","url":"https://arxiv.org/html/2604.26525"},{"title":"One Pass, Any Order: Position-Invariant Listwise Reranking for LLM-Based Recommendation","url":"https://arxiv.org/html/2604.27599"},{"title":"A Sanity Check on Composed Image Retrieval","url":"https://arxiv.org/html/2604.12904v1"}]

Based on the search results, I found the paper you're looking for:

## Regime-Conditional Retrieval: Theory and a Transferable Router for Two-Hop QA

The paper addresses two-hop QA retrieval, splitting queries into two regimes determined by whether the hop-2 entity is explicitly named in the question (Q-dominant) or only in the bridge passage (B-dominant).

**Main Contributions:**

The authors formalize the split with three theorems: (T1) per-query AUC is a monotone function of the cosine separation margin, with R^2 >= 0.90 for six of eight type-encoder pairs; (T2) regime is characterized by two surface-text predicates, with P1 decisive for routing and P2 qualifying the B-dominant case; and (T3) bridge advantage requires the relation-bearing sentence, not entity name alone.

**Proposed Method:**

The authors propose RegimeRouter, a lightweight binary router that selects between question-only and question-plus-relation-sentence retrieval using five text features derived directly from the predicate definitions.

**Results:**

Trained on 2WikiMultiHopQA and applied zero-shot to MuSiQue and HotpotQA, RegimeRouter achieves +5.6 pp, +5.3 pp, and +1.1 pp R@5 improvement, respectively.

The paper was authored by Andre Bacellar and was last updated on April 28, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98cbaeab-4b7f-4600-9a50-2f9ba19f8b58",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "ae15a4c4824a5c36f",
  "type": "user",
  "uuid": "73b12e24-014a-4ecd-b3dd-ea2cc3b3e57a",
  "sourceToolAssistantUUID": "98cbaeab-4b7f-4600-9a50-2f9ba19f8b58",
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

_source line 13 · 2026-05-14T16:58:50.471Z_

Let me get more details by fetching the HTML version of the paper for deeper verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73b12e24-014a-4ecd-b3dd-ea2cc3b3e57a",
  "isSidechain": true,
  "agentId": "ae15a4c4824a5c36f",
  "requestId": "req_011Cb2pKxSDRDjW21ZhWc8e5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d8f7726-2818-4973-9873-33a613dfa003",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GA6dd2xso2q7DHEzMzBK9t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1294,
      "cache_creation_input_tokens": 1145,
      "cache_read_input_tokens": 10828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1145,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 14 · 2026-05-14T16:58:53.610Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NH718fMmUV3J7d1orvmmbV`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.09019",
  "prompt": "Extract detailed information about: 1) The three theorems (T1, T2, T3) and what they formalize. 2) The exact definition of Q-dominant vs B-dominant regimes. 3) The RegimeRouter architecture and whether it is strictly a binary classifier. 4) The exact numerical results on MuSiQue, HotpotQA, and 2WikiMultiHopQA (R@5 improvements). 5) Whether the approach is limited to hop-2 only or extends beyond. 6) Any limitations section discussing the binary/hop-2 restriction. 7) The author(s) and submission date."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d8f7726-2818-4973-9873-33a613dfa003",
  "isSidechain": true,
  "agentId": "ae15a4c4824a5c36f",
  "requestId": "req_011Cb2pKxSDRDjW21ZhWc8e5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bf7b7a9-bbff-411d-96bd-a7310d678b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GA6dd2xso2q7DHEzMzBK9t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1294,
      "cache_creation_input_tokens": 1145,
      "cache_read_input_tokens": 10828,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1145
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1294,
          "output_tokens": 247,
          "cache_read_input_tokens": 10828,
          "cache_creation_input_tokens": 1145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1145,
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

_source line 15 · 2026-05-14T16:59:03.122Z_

<details><summary>↩ Tool result · `toolu_01NH718fMmUV3J7d1orvmmbV`</summary>

```text
# Analysis of "Regime-Conditional Retrieval: Theory and a Transferable Router for Two-Hop QA"

## 1. The Three Theorems

**Theorem 1 (Separation-AUC Calibration):** Formalizes that per-query AUC follows a monotone relationship with cosine separation margin, approximating the standard normal CDF. Validation achieved R² ≥ 0.90 for six of eight encoder-type combinations.

**Theorem 2 (Regime Decomposition):** Establishes that retrieval regime is determined by two binary predicates (P1 and P2). "P1 is decisive for routing: ΔS < 0 (Q-dominant) when P1=True; when P1=False, P2=True identifies the B-dominant case."

**Theorem 3 (Relational Sentence Sufficiency):** Demonstrates bridge advantage depends specifically on relation-bearing sentences, not entity occurrence alone. Removing this sentence caused performance collapse of "8.6–14.1 pp (p<0.001)."

## 2. Regime Definitions

**Q-dominant regime:** "P1=True (both answer entities appear in the question)." The question embedding alone ranks gold passages correctly; bridge re-encoding is redundant.

**B-dominant regime:** "P1=False (the answer entity is not named in the question), P2=True (it is named in the bridge)." Bridge relation-bearing sentences must supplement question encoding.

## 3. RegimeRouter Architecture

RegimeRouter is a **binary logistic regression classifier** selecting between two retrieval strategies (Q-only vs. Union-based). It uses five surface-text features: comparison word presence, yes/no question structure, proper noun counts, novel entities in bridge, and relation-bearing sentence fraction. A separate sentence selector identifies relation-bearing sentences.

## 4. Numerical Results (R@5)

- **2WikiMultiHopQA (training):** +5.6 pp (p<0.001)
- **MuSiQue (zero-shot):** +5.3 pp (p=0.002)
- **HotpotQA (zero-shot):** +1.1 pp (p=0.143, non-significant)

## 5. Scope Limitation: Hop-2 Only

The approach is strictly limited to two-hop retrieval. The authors note: "questions are constructed by composing single-hop questions, making P1 and P2 binary and well-defined."

## 6. Limitations Section

The Limitations section explicitly states the theory "may not directly extend to: (1) questions with implicit rather than explicit compositional structure; (2) multi-hop chains beyond two hops; (3) encoders trained with bridge conditioning."

## 7. Author and Submission Date

**Author:** Andre Bacellar (andremi@gmail.com)  
**arXiv ID:** 2604.09019v2  
**Submission Date:** April 28, 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bf7b7a9-bbff-411d-96bd-a7310d678b47",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "ae15a4c4824a5c36f",
  "type": "user",
  "uuid": "181800b4-70d8-43ba-a5a6-491a646ab9e3",
  "sourceToolAssistantUUID": "0bf7b7a9-bbff-411d-96bd-a7310d678b47",
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

_source line 16 · 2026-05-14T16:59:17.165Z_

Here are the verified findings for each of your five questions:

---

**1. Does this paper exist on arXiv?**

Yes, confirmed. The paper is available at [arxiv.org/abs/2604.09019](https://arxiv.org/abs/2604.09019) with the full title "Regime-Conditional Retrieval: Theory and a Transferable Router for Two-Hop QA" by Andre Bacellar. The current version is v2, submitted/updated April 28, 2026.

---

**2. Does it formalize Q-dominant vs B-dominant retrieval regimes for two-hop QA?**

Yes, confirmed. The paper formalizes these regimes through three theorems:

- **Theorem 1 (Separation-AUC Calibration):** Per-query AUC is a monotone function of the cosine separation margin, with R-squared >= 0.90 for six of eight encoder-type combinations.
- **Theorem 2 (Regime Decomposition):** Regime is determined by two binary predicates P1 and P2. P1=True (both answer entities appear in the question) defines the **Q-dominant** case. P1=False and P2=True (the answer entity is named only in the bridge passage, not the question) defines the **B-dominant** case.
- **Theorem 3 (Relational Sentence Sufficiency):** Bridge advantage depends on relation-bearing sentences specifically, not entity occurrence alone. Removing the relation-bearing sentence collapses performance by 8.6--14.1 pp (p<0.001).

---

**3. Does it train a binary router?**

Yes, confirmed. The paper proposes **RegimeRouter**, which is a binary logistic regression classifier. It selects between two retrieval strategies: question-only encoding (for Q-dominant queries) vs. union-based encoding that incorporates relation-bearing sentences from the bridge passage (for B-dominant queries). It uses five surface-text features: comparison word presence, yes/no question structure, proper noun counts, novel entities in bridge, and relation-bearing sentence fraction.

---

**4. What are its claimed improvements?**

The claimed R@5 improvements are:

| Benchmark | Improvement | Significance |
|---|---|---|
| 2WikiMultiHopQA (training set) | **+5.6 pp** | p < 0.001 |
| MuSiQue (zero-shot transfer) | **+5.3 pp** | p = 0.002 |
| HotpotQA (zero-shot transfer) | **+1.1 pp** | p = 0.143 (non-significant) |

The numbers you cited (+5.6 pp on MuSiQue, +5.3 pp on HotpotQA) are **swapped from what the paper actually reports**. The paper claims +5.6 pp on 2WikiMultiHopQA and +5.3 pp on MuSiQue. The HotpotQA improvement is only +1.1 pp and is statistically non-significant.

---

**5. Is it limited to binary classification for hop-2 only?**

Yes, confirmed. The approach is strictly limited to two-hop retrieval with a binary regime classification. The paper's Limitations section explicitly states the theory "may not directly extend to: (1) questions with implicit rather than explicit compositional structure; (2) multi-hop chains beyond two hops; (3) encoders trained with bridge conditioning." The binary predicates P1 and P2 are well-defined specifically because two-hop questions are "constructed by composing single-hop questions."

---

Sources:
- [arXiv Abstract: 2604.09019](https://arxiv.org/abs/2604.09019)
- [arXiv HTML Full Paper: 2604.09019](https://arxiv.org/html/2604.09019)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "181800b4-70d8-43ba-a5a6-491a646ab9e3",
  "isSidechain": true,
  "agentId": "ae15a4c4824a5c36f",
  "requestId": "req_011Cb2pM4W7qgc41kY6nwxmA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a864bb2f-6b48-48a0-bdf8-d5af403b755d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmSyp1Zbd3UvKDosZYFDEd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 11973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2256,
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
