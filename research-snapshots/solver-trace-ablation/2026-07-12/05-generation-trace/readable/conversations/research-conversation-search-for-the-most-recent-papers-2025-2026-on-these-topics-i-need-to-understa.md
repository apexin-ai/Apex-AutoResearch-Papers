# Research conversation: Search for the most recent papers (2025-2026) on these topics. I need to understand the current landscape for a research

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a1a848061a6c1817c.jsonl`
- **Structured JSON:** [`c51428bec222078525b4.json`](../../sessions/c5/c51428bec222078525b4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-12T00:33:25.899Z_

Search for the most recent papers (2025-2026) on these topics. I need to understand the current landscape for a research proposal revision:

1. Search for "VERGE arXiv 2601.20055" - I need to understand how VERGE routes claims during iterative refinement vs. post-hoc verification.

2. Search for recent work on "step-level autoformalization" or "step-level formal verification" for logic reasoning (specifically on FOLIO, ProofWriter benchmarks) published in 2025-2026.

3. Search for "neuro-symbolic verification routing" or "hybrid verification routing" in reasoning — any work that routes between symbolic and neural verifiers.

4. Search for the latest FOLIO benchmark results / leaderboard to understand current SOTA accuracy.

5. Search for any papers that specifically analyze when autoformalization helps vs. hurts for logic reasoning.

Use WebSearch for each query, and WebFetch to read key papers. Report findings concisely (under 500 words), focusing on: what exists, what's missing, and whether there's a genuine gap for error complementarity analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "8208ab5b-094d-4ef3-8e86-c4fad3169f5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:33:25.904Z_

```json
{
  "parentUuid": "8208ab5b-094d-4ef3-8e86-c4fad3169f5e",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
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
  "uuid": "9a8cc002-b438-4173-b7cd-2a6fa01d54b1",
  "timestamp": "2026-05-12T00:33:25.904Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:33:28.271Z_



I'll start by loading the WebSearch and WebFetch tools, then run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a8cc002-b438-4173-b7cd-2a6fa01d54b1",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjZyRXe1fmWiPVMdsnD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e103e376-e86d-438c-999f-0aabbc8c29a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JcxDDTMLjG2PiY5v5fuKaE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 774,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 774,
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

_source line 4 · 2026-05-12T00:33:28.576Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016Lv5psN9rd1FzXbeTdgrfy`</summary>

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
  "parentUuid": "e103e376-e86d-438c-999f-0aabbc8c29a0",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjZyRXe1fmWiPVMdsnD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da006da9-8b54-4783-8458-13bd4b685b98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JcxDDTMLjG2PiY5v5fuKaE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 774,
      "cache_read_input_tokens": 7304,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 774
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 774,
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

_source line 5 · 2026-05-12T00:33:28.582Z_

<details><summary>↩ Tool result · `toolu_016Lv5psN9rd1FzXbeTdgrfy`</summary>

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
  "parentUuid": "da006da9-8b54-4783-8458-13bd4b685b98",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "c7dcffee-5cd5-426c-96f6-f62a0e8ac872",
  "sourceToolAssistantUUID": "da006da9-8b54-4783-8458-13bd4b685b98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:33:32.331Z_



Now let me run all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7dcffee-5cd5-426c-96f6-f62a0e8ac872",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjaAvaixAQCpXrCiVqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f1f44e1-c616-4ca0-a5ee-45c627567ad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmFtLxxu7rWuGBgNcihqLG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 7 · 2026-05-12T00:33:33.281Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YLGg7BPmrn7gu5gv86GjPv`</summary>

```json
{
  "query": "VERGE arXiv 2601.20055 iterative refinement verification routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f1f44e1-c616-4ca0-a5ee-45c627567ad6",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjaAvaixAQCpXrCiVqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "164c9bc1-ad9c-46c9-9820-7bae67351e72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmFtLxxu7rWuGBgNcihqLG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 8 · 2026-05-12T00:33:34.290Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vn9BVXgrEaan5RozdGbzmT`</summary>

```json
{
  "query": "step-level autoformalization formal verification logic reasoning FOLIO ProofWriter 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "164c9bc1-ad9c-46c9-9820-7bae67351e72",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjaAvaixAQCpXrCiVqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7410a36d-5221-408b-85c0-f0f61bdd16c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmFtLxxu7rWuGBgNcihqLG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 9 · 2026-05-12T00:33:35.224Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019k9vSdMcWAH1y2RrNnn2jZ`</summary>

```json
{
  "query": "neuro-symbolic verification routing hybrid verification routing reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7410a36d-5221-408b-85c0-f0f61bdd16c9",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjaAvaixAQCpXrCiVqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0cb28c8-b704-42fd-b542-c737f3eaff58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmFtLxxu7rWuGBgNcihqLG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 10 · 2026-05-12T00:33:36.167Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KqJFkqwvDWHE1y2kH1afQB`</summary>

```json
{
  "query": "FOLIO benchmark leaderboard SOTA accuracy 2025 2026 natural language reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0cb28c8-b704-42fd-b542-c737f3eaff58",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjaAvaixAQCpXrCiVqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "729a2368-febf-405d-a4be-2938fc6040d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmFtLxxu7rWuGBgNcihqLG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
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

_source line 11 · 2026-05-12T00:33:36.594Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HY2YWasyqtXxGKwBiGbon5`</summary>

```json
{
  "query": "autoformalization helps hurts logic reasoning analysis error complementarity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "729a2368-febf-405d-a4be-2938fc6040d5",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjaAvaixAQCpXrCiVqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0640e20c-ff93-4deb-ba69-5a9bca112079",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmFtLxxu7rWuGBgNcihqLG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8078,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1911
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 294,
          "cache_read_input_tokens": 8078,
          "cache_creation_input_tokens": 1911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1911,
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

_source line 12 · 2026-05-12T00:33:40.754Z_

<details><summary>↩ Tool result · `toolu_01YLGg7BPmrn7gu5gv86GjPv`</summary>

```text
Web search results for query: "VERGE arXiv 2601.20055 iterative refinement verification routing"

Links: [{"title":"[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.20055"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055"},{"title":"Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://huggingface.co/papers/2601.20055"},{"title":"[2601.05897] The Modal Logic of Abstraction Refinement","url":"https://arxiv.org/abs/2601.05897"},{"title":"dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"},{"title":"[2601.15286v1] Iterative Refinement Improves Compositional Image Generation","url":"https://arxiv.org/abs/2601.15286v1"},{"title":"ReVeal: Self-Evolving Code Agents via Iterative Generation-Verification","url":"https://arxiv.org/html/2506.11442v1"},{"title":"Iterative Refinement Improves Compositional Image Generation","url":"https://arxiv.org/html/2601.15286"},{"title":"[2601.15808v1] Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification","url":"https://arxiv.org/abs/2601.15808v1"},{"title":"Verina: Benchmarking Verifiable Code Generation","url":"https://arxiv.org/html/2505.23135v1"}]

## VERGE: arXiv 2601.20055

I found the paper you're looking for. Here's what the research presents:

**Overview:**
VERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement. The approach decomposes LLM outputs into atomic claims, autoformalizes them into first-order logic, and verifies their logical consistency using automated theorem proving.

**Key Innovations:**
The framework introduces three key innovations: (1) multi-sample consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, eliminating the syntactic bias of surface-form metrics, (2) semantic routing that directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning, and (3) precise logical error localization via Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise, transforming binary failure signals into actionable feedback.

**How It Works:**
The framework classifies claims by their logical status and aggregates multiple verification signals into a unified score with variance-based penalty. The system iteratively refines answers using structured feedback until acceptance criteria are met or convergence is achieved.

**Results:**
With the GPT-OSS-120B model, VERGE demonstrates an average performance uplift of 18.7% at convergence across a set of reasoning benchmarks compared to single-pass approaches.

The paper was published on January 27, 2026, by researchers from Case Western Reserve University and Amazon Web Services.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "164c9bc1-ad9c-46c9-9820-7bae67351e72",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "2ed8dfb9-73ab-4a85-a70c-9d4f5f4fff4c",
  "sourceToolAssistantUUID": "164c9bc1-ad9c-46c9-9820-7bae67351e72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:33:42.473Z_

<details><summary>↩ Tool result · `toolu_01Vn9BVXgrEaan5RozdGbzmT`</summary>

```text
Web search results for query: "step-level autoformalization formal verification logic reasoning FOLIO ProofWriter 2025 2026"

Links: [{"title":"stepproof: step-by-step verification of","url":"https://arxiv.org/pdf/2506.10558"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"Training Step-Level Reasoning Verifiers with Formal ...","url":"https://arxiv.org/pdf/2505.15960"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=zHuV3Vatov"},{"title":"Towards a Common Framework for Autoformalization","url":"https://arxiv.org/pdf/2509.09810"},{"title":"Intermediate Languages Matter: Formal Languages and LLMs affect Neurosymbolic Reasoning","url":"https://arxiv.org/html/2509.04083v1"},{"title":"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries","url":"https://arxiv.org/html/2603.29500v1"},{"title":"Enhancing Mathematical Reasoning in Large Language ...","url":"https://aclanthology.org/2025.acl-long.594.pdf"},{"title":"StepProof: Step-by-step verification of natural language mathematical proofs | OpenReview","url":"https://openreview.net/forum?id=EXaKfdsw04"},{"title":"Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM","url":"https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"}]

Based on the search results, here are the key findings related to your query about step-level autoformalization, formal verification, logic reasoning, FOLIO, and ProofWriter:

## Recent Developments in Step-Level Autoformalization

StepProof is an autoformalization method designed for granular, step-by-step verification that breaks down complete proofs into multiple verifiable subproofs, enabling sentence-level verification. Experimental results demonstrate that StepProof significantly improves proof success rates and efficiency compared to traditional methods.

## Formal Verification Approaches

FOVER is a novel approach to create PRM (Process Reward Model) training data using formal verification tools, such as Z3 and Isabelle. Additionally, the FoVer pipeline operates in two main steps: (1) LLM-driven translation of natural language into executable logical expressions, and (2) automated logical verification using the Z3 theorem prover.

## Datasets (FOLIO and ProofWriter)

FOLIO is a human-annotated, logically complex, and diverse dataset designed for natural language reasoning with first-order logic, and compared to ProofWriter, premises and conclusions in FOLIO are expressed more naturally. ProofWriter is a dataset containing numerous rulebases of facts and rules expressed in English, with each rulebase including a set of questions that can be proven True, False, or Unknown using proofs of various depths.

## Step-Level Reasoning Verification (2025-2026)

PRoSFI is a novel reward method that enhances reasoning reliability by having models output structured intermediate steps aligned with natural language reasoning, with each step verified by a formal prover, where only fully validated reasoning chains receive high rewards.

These developments represent recent advances in combining autoformalization with step-level verification for improved formal reasoning in LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7410a36d-5221-408b-85c0-f0f61bdd16c9",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "a6c17ed2-62fa-4d21-a6f7-ab5542da82d8",
  "sourceToolAssistantUUID": "7410a36d-5221-408b-85c0-f0f61bdd16c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T00:33:43.406Z_

<details><summary>↩ Tool result · `toolu_019k9vSdMcWAH1y2RrNnn2jZ`</summary>

```text
Web search results for query: "neuro-symbolic verification routing hybrid verification routing reasoning 2025 2026"

Links: [{"title":"FregeLogic at SemEval 2026 Task 11: A Hybrid Neuro-Symbolic Architecture for Content-Robust Syllogistic Validity Prediction","url":"https://arxiv.org/html/2604.18328"},{"title":"A Comprehensive Review of Neuro-symbolic AI for Robustness, Uncertainty Quantification, and Intervenability | Arabian Journal for Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13369-025-10887-3"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055v2"},{"title":"Hybrid neuro-symbolic learning and reasoning for resilient load restoration in smart microgrids - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0960148125020658"},{"title":"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks | OpenReview","url":"https://openreview.net/forum?id=zHuV3Vatov"},{"title":"Neuro-Symbolic AI Architecture","url":"https://www.emergentmind.com/topics/neuro-symbolic-ai-architecture"},{"title":"Designing a neuro-symbolic dual-model architecture for explainable and resilient intrusion detection in IoT networks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-27076-9"},{"title":"Hybrid Neuro-Symbolic Models for Ethical AI in Risk-Sensitive Domains","url":"https://arxiv.org/html/2511.17644v1"},{"title":"Cogent | Blog | The Year of Neuro-Symbolic AI: How 2026 Makes Machines Actually Understand","url":"https://www.cogentinfo.com/resources/the-year-of-neuro-symbolic-ai-how-2026-makes-machines-actually-understand"},{"title":"The Rise of Neuro-Symbolic AI: A Spotlight in Gartner’s 2025 AI Hype Cycle - AllegroGraph","url":"https://allegrograph.com/the-rise-of-neuro-symbolic-ai-a-spotlight-in-gartners-2025-ai-hype-cycle/"}]

I found several relevant results about neuro-symbolic verification, routing, and reasoning systems in 2025-2026. Here's what the search reveals:

## Key Recent Developments

### Hybrid Routing and Verification Systems

A semantic routing framework balances the precision of SMT solvers with the flexibility of LLMs, avoiding forcing undecidable language into decidable theories. This approach is exemplified by **VERGE** (Formal Refinement and Guidance Engine), which uses neuro-symbolic methods to achieve verifiable reasoning.

### Selective Verification Through Routing

FregeLogic is a hybrid neuro-symbolic system that exploits complementary strengths of LLM ensembles and formal logic solvers, using a five-member ensemble paired with the Z3 SMT solver as a tiebreaker when the ensemble produces a narrow vote split. The key innovation is that close votes in the ensemble disproportionately coincide with content-biased errors, precisely where a content-neutral formal verifier adds value.

### Chain-of-Thought Verification

VeriCoT is a neuro-symbolic method that extracts and verifies formal logical arguments from CoT reasoning by formalizing each reasoning step into first-order logic and identifying premises that ground the argument.

### Broader Paradigm Shift

Neuro-symbolic AI is a hybrid paradigm that combines the learning capabilities of neural networks with the reasoning strengths of symbolic AI. By 2026, this shift reaches a point where businesses no longer ask whether AI can perform a task; they ask whether AI can explain, defend, and refine its decisions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0cb28c8-b704-42fd-b542-c737f3eaff58",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "7d9738b7-0163-44ba-bcc6-ed0ed2856db4",
  "sourceToolAssistantUUID": "d0cb28c8-b704-42fd-b542-c737f3eaff58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T00:33:44.608Z_

<details><summary>↩ Tool result · `toolu_01HY2YWasyqtXxGKwBiGbon5`</summary>

```text
Web search results for query: "autoformalization helps hurts logic reasoning analysis error complementarity 2025 2026"

Links: [{"title":"LTRAG: Enhancing Autoformalization and Self-refinement ...","url":"https://aclanthology.org/2025.findings-acl.126.pdf"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=Njrkeo3DiJ"},{"title":"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach | OpenReview","url":"https://openreview.net/forum?id=hUb2At2DsQ"},{"title":"A NEUROSYMBOLIC APPROACH TO NATURAL LANGUAGE FORMALIZATION AND VERIFICATION","url":"https://arxiv.org/pdf/2511.09008"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"Unspoken Logic: Understanding and bridging the gap between free-form and LLM-interpretable natural language mathematical proofs | OpenReview","url":"https://openreview.net/forum?id=0IsLjMjD0P"},{"title":"Towards Advanced Mathematical Reasoning for LLMs via ...","url":"https://aclanthology.org/2025.emnlp-main.628.pdf"},{"title":"LTRAG: Enhancing Autoformalization and Self-refinement for Logical Reasoning with Thought-Guided RAG - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.126/"},{"title":"Towards a Common Framework for Autoformalization","url":"https://arxiv.org/html/2509.09810v3"},{"title":"Autoformalization: Bridging Informal and Formal Math","url":"https://www.emergentmind.com/topics/autoformalization"}]

I've found several recent research papers and resources on autoformalization and its relationship to logic reasoning. Here are key findings from 2025-2026:

## Autoformalization and Logic Reasoning: Recent Developments

### Error and Challenges
Incorrect autoformalization undermines validity, which is a central concern in the field. Autoformalization, the translation of natural language into formal language, is challenging because humans express logic in a rich and diverse set of ways, and autoformalization of a mathematical proof can fail even if the proof is rigorous from the perspective of other humans.

### Complementary Approaches
Recent advances in large language model–driven theorem proving not only complement autoformalization but also expand its scope—by generating formal derivations that validate the translated statements. Autoformalization leverages a task that large language models naturally excel at—translation—by mapping informal language into formal representations, offering a potentially more efficient and interpretable alternative, or at least a complementary approach to other reasoning methods.

### Recent Solutions and Improvements
Research in 2025 has addressed key problems: Critical gaps include absence of faithful and universal automated evaluation for autoformalization results and lack of awareness of contextual information, inducing severe hallucination of formal definitions and theorems. Solutions include augmenting statement autoformalization by Dependency Retrieval, retrieving potentially dependent objects from formal libraries.

LTRAG, a framework to enhance autoformalization and self-refinement for logical reasoning with Retrieval-Augmented Generation, shows that it consistently outperforms Logic-LM and LINC across different models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0640e20c-ff93-4deb-ba69-5a9bca112079",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "66c6a75e-1d97-4694-a49e-b30958f87927",
  "sourceToolAssistantUUID": "0640e20c-ff93-4deb-ba69-5a9bca112079",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T00:33:52.069Z_

<details><summary>↩ Tool result · `toolu_01KqJFkqwvDWHE1y2kH1afQB`</summary>

```text
Web search results for query: "FOLIO benchmark leaderboard SOTA accuracy 2025 2026 natural language reasoning"

Links: [{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"Speech AI Leaderboard 2026: Best STT, ASR and TTS Models | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/speech"},{"title":"SOTA AI Models: Benchmarks, Metrics & Deployment Guide","url":"https://huggingface.co/blog/daya-shankar/sota-ai-models"},{"title":"OCR Benchmark Leaderboard 2026: Best OCR Models Compared | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/ocr"},{"title":"Codesota — the open, callable registry of SOTA","url":"https://www.codesota.com/"},{"title":"Papers with Code is Dead — Best Alternatives 2026 by Use Case | Codesota | CodeSOTA","url":"https://www.codesota.com/papers-with-code"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"}]

Let me search more specifically for the FOLIO benchmark:

Links: [{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1229/"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://aclanthology.org/2024.emnlp-main.1229.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://github.com/Yale-LILY/FOLIO"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.20973"},{"title":"Paper page - FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://huggingface.co/papers/2209.00840"},{"title":"[PDF] FOLIO: Natural Language Reasoning with First-Order Logic | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FOLIO:-Natural-Language-Reasoning-with-First-Order-Han-Schoelkopf/5581bf85386737bd3378eec68189759a05280bea"}]

Let me search for more recent FOLIO leaderboard results and SOTA accuracy scores:

Links: [{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"Arena Leaderboard | Compare & Benchmark the Best Frontier AI Models","url":"https://arena.ai/leaderboard/"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"Best AI Models: April + May 2026 Leaderboard (GPT-5.5, Claude Opus 4.7, DeepSeek V4)","url":"https://www.buildfastwithai.com/blogs/best-ai-models-may-2026-leaderboard"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"AI Model Benchmarks May 2026 | Compare GPT-5, Claude 4.5, Gemini 2.5, Grok 4 | LM Council","url":"https://lmcouncil.ai/benchmarks"},{"title":"GDPval-AA Leaderboard | Artificial Analysis","url":"https://artificialanalysis.ai/evaluations/gdpval-aa"},{"title":"SWE-Bench Leaderboard May 2026 | GPT-5.5 Leads at 88.7%","url":"https://www.marc0.dev/en/leaderboard"},{"title":"AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"Best LLM for Coding in 2026: Ranked by Real Benchmarks | WhatLLM.org","url":"https://whatllm.org/best-llm-for-coding"}]

Let me search more specifically for FOLIO benchmark results:

Links: [{"title":"GPT-5 vs Gemini in 2026: Full Benchmark Breakdown | BenchLM.ai","url":"https://benchlm.ai/blog/posts/gpt5-vs-gemini-2026"}]

Based on my search results, I can provide you with information about the FOLIO benchmark, though I wasn't able to find a specific active leaderboard with 2025-2026 SOTA scores:

## FOLIO Benchmark Overview

FOLIO is a human-annotated, logically complex and diverse dataset for reasoning in natural language (NL), equipped with first-order logic (FOL) annotations. FOLIO consists of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion.

FOLIO is the first reasoning dataset to combine natural language with FOL annotations. FOLIO is the first large-scale first-order logical (FOL) reasoning dataset with formal logic annotations in FOL. FOLIO is logically diverse and complex with abundant natural language variations and a rich vocabulary.

## Benchmark Results

Based on research from the original FOLIO paper, a subset of FOLIO remains a challenge for one of the most capable Large Language Model (LLM) publicly available, GPT-4. More specifically, GPT-3 davinci achieves only slightly better than random results with few-shot prompting on a subset of FOLIO, and the model is especially bad at predicting the correct truth values for False and Unknown conclusions.

However, I was unable to locate a current active FOLIO benchmark leaderboard with specific 2025-2026 SOTA accuracy scores. The most recent comprehensive AI model leaderboards I found focus on benchmarks like SWE-bench, GPQA Diamond, AIME, and others, but do not prominently feature FOLIO scores. If you're looking for the latest FOLIO results, you may want to check the official GitHub repository at https://github.com/Yale-LILY/FOLIO or academic papers that cite this benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "729a2368-febf-405d-a4be-2938fc6040d5",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "c913efad-ba37-465e-8dcf-f95469085063",
  "sourceToolAssistantUUID": "729a2368-febf-405d-a4be-2938fc6040d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-12T00:33:54.697Z_

Let me fetch the key papers for deeper details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c913efad-ba37-465e-8dcf-f95469085063",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjbuCLcLxbTz3pZWWxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f778479f-8aa6-44d0-a60f-2bed374697d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhJrx2eArfd7gMBPocjQTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 881,
      "cache_creation_input_tokens": 5157,
      "cache_read_input_tokens": 9989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5157,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-12T00:33:57.601Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Hdr7ELJzsc2UXi8cY7YFSE`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.20055",
  "prompt": "Extract the key details about VERGE: (1) How does semantic routing work -- how does it decide which claims go to symbolic vs neural verifiers? (2) Does it analyze error complementarity between symbolic and neural paths? (3) What benchmarks and results are reported, especially on FOLIO? (4) What are the limitations acknowledged?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f778479f-8aa6-44d0-a60f-2bed374697d2",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjbuCLcLxbTz3pZWWxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f08778ab-97ae-4a9c-ab37-78adcdd78baa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhJrx2eArfd7gMBPocjQTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 881,
      "cache_creation_input_tokens": 5157,
      "cache_read_input_tokens": 9989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5157,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-12T00:33:59.972Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015JFL4J7i5yHz3CS8RH5UjR`</summary>

```json
{
  "url": "https://openreview.net/forum?id=zHuV3Vatov",
  "prompt": "Extract: (1) What is VeriCoT's approach to verifying chain-of-thought reasoning? (2) Does it perform step-level formalization? (3) What benchmarks does it use (FOLIO, ProofWriter)? (4) What are its FOLIO results? (5) Does it analyze when formalization helps vs hurts?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f08778ab-97ae-4a9c-ab37-78adcdd78baa",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjbuCLcLxbTz3pZWWxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9b8d045-f7fd-4c8d-b362-ec225a20e27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhJrx2eArfd7gMBPocjQTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 881,
      "cache_creation_input_tokens": 5157,
      "cache_read_input_tokens": 9989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5157,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T00:34:01.497Z_

<details><summary>↩ Tool result · `toolu_01Hdr7ELJzsc2UXi8cY7YFSE`</summary>

```text
# VERGE Framework: Key Details

Based on the abstract provided, here's what can be determined:

## 1. Semantic Routing Mechanism
The paper describes "semantic routing that directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning." However, the specific decision-making criteria for routing are not detailed in this abstract excerpt.

## 2. Error Complementarity Analysis
The abstract does not discuss whether the framework analyzes complementary strengths between symbolic and neural verification paths.

## 3. Benchmarks and Results
The document states: "With the GPT-OSS-120B model, VERGE demonstrates an average performance uplift of 18.7% at convergence across a set of reasoning benchmarks compared to single-pass approaches."

However, FOLIO is not specifically mentioned in this excerpt. The abstract references "reasoning benchmarks" generically without naming individual datasets.

## 4. Acknowledged Limitations
The provided content does not explicitly list acknowledged limitations. The abstract focuses on innovations and performance gains rather than constraints or failure modes.

---

**Note:** This response is constrained to information visible in the abstract and webpage metadata. Fuller details would require accessing the complete paper PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f08778ab-97ae-4a9c-ab37-78adcdd78baa",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "df172408-3d3d-4b4b-8635-daafdbff864d",
  "sourceToolAssistantUUID": "f08778ab-97ae-4a9c-ab37-78adcdd78baa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-12T00:34:01.968Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XDSzdXhUeHf7HbWMM6DfeY`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.18328",
  "prompt": "Extract: (1) How does FregeLogic route between neural ensemble and Z3 solver? (2) What is the routing criterion? (3) What results does it achieve? (4) Does it analyze error complementarity between symbolic and neural approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df172408-3d3d-4b4b-8635-daafdbff864d",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjbuCLcLxbTz3pZWWxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ccd7509-87be-4750-b39b-f49972978140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhJrx2eArfd7gMBPocjQTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 881,
      "cache_creation_input_tokens": 5157,
      "cache_read_input_tokens": 9989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5157,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T00:34:03.391Z_

<details><summary>↩ Tool result · `toolu_015JFL4J7i5yHz3CS8RH5UjR`</summary>

```text
# VeriCoT Analysis Based on Available Content

Based on the OpenReview abstract provided, here's what can be addressed:

**(1) Verification Approach:**
VeriCoT uses a neuro-symbolic method that "extracts and verifies formal logical arguments from CoT reasoning." It converts reasoning steps into first-order logic and identifies premises grounded in source context, common knowledge, or prior steps.

**(2) Step-Level Formalization:**
Yes. The method "formalizes each CoT reasoning step into first-order logic" to enable automated solver verification of logical validity.

**(3) Benchmarks Used:**
The abstract specifies three datasets: ProofWriter, LegalBench-SARA, and BioASQ. **FOLIO is not mentioned** in this content.

**(4) FOLIO Results:**
No FOLIO results are provided in this abstract excerpt.

**(5) Analysis of When Formalization Helps vs. Hurts:**
The abstract does not discuss conditions where formalization may be counterproductive or comparative analysis of effectiveness across different reasoning types.

**Note:** The content provided is limited to the abstract. Fuller details addressing all your questions likely appear in the complete paper, which would require access to the full PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9b8d045-f7fd-4c8d-b362-ec225a20e27c",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "0a06f5d2-4146-436d-aabb-a13a87d73cb8",
  "sourceToolAssistantUUID": "f9b8d045-f7fd-4c8d-b362-ec225a20e27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T00:34:04.907Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AqxcJ3hm7NPpyNdofspQtF`</summary>

```json
{
  "url": "https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural",
  "prompt": "Extract: (1) What is FoVer's approach? (2) Does it do step-level verification? (3) What are its FOLIO and ProofWriter results (specific accuracy numbers)? (4) Does it analyze when autoformalization helps vs hurts? (5) What are its limitations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a06f5d2-4146-436d-aabb-a13a87d73cb8",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjbuCLcLxbTz3pZWWxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce84f089-c2f8-4525-8db4-ffed170a419c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhJrx2eArfd7gMBPocjQTX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 881,
      "cache_creation_input_tokens": 5157,
      "cache_read_input_tokens": 9989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5157,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T00:34:05.109Z_

<details><summary>↩ Tool result · reported error · `toolu_01AqxcJ3hm7NPpyNdofspQtF`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce84f089-c2f8-4525-8db4-ffed170a419c",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "9114142b-85dc-47f4-8710-29fd4bfdc16c",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "ce84f089-c2f8-4525-8db4-ffed170a419c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-12T00:34:05.740Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fu7yjbnC5EHzx59y1KH3SL`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-acl.126/",
  "prompt": "Extract: (1) What is LTRAG's approach to autoformalization for logical reasoning? (2) What benchmarks does it use (FOLIO, ProofWriter)? (3) What are the specific accuracy results? (4) Does it analyze when autoformalization helps vs hurts reasoning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9114142b-85dc-47f4-8710-29fd4bfdc16c",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjbuCLcLxbTz3pZWWxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2e678ca-33c9-41a1-87a2-172022a5d217",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhJrx2eArfd7gMBPocjQTX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 881,
      "cache_creation_input_tokens": 5157,
      "cache_read_input_tokens": 9989,
      "output_tokens": 737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5157
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 881,
          "output_tokens": 737,
          "cache_read_input_tokens": 9989,
          "cache_creation_input_tokens": 5157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5157,
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

_source line 26 · 2026-05-12T00:34:08.277Z_

<details><summary>↩ Tool result · `toolu_01XDSzdXhUeHf7HbWMM6DfeY`</summary>

```text
# FregeLogic: Neural-Symbolic Routing Analysis

## (1) Routing Mechanism
FregeLogic employs a **vote-margin based decision module**. When the five-member LLM ensemble produces predictions, the system calculates a margin metric reflecting consensus strength. This margin determines whether to defer to Z3's formal verification or trust the ensemble majority.

## (2) Routing Criterion
The routing threshold is a margin of ≤1, corresponding to **3–2 vote splits**. As stated: "If m≤1: use Z3 verdict (if available) Else: use ensemble majority." This selective intervention targets cases where ensemble disagreement likely signals content bias, the system's core hypothesis.

## (3) Results Achieved
- **Combined score: 41.88** (vs. 39.12 for pure ensemble)
- **Accuracy: 94.3%** (0.9-point improvement)
- **Content effect reduction: 16%** (3.39 → 2.85)
- The tiebreaker triggers on only **7.9% of cases** (76 of 960), producing 19 correct flips versus 11 incorrect ones

## (4) Error Complementarity Analysis
The paper identifies **directional asymmetry** in error patterns: Z3 exhibits strong invalidity bias (97.6% accuracy on invalid syllogisms vs. 52.2% on valid ones), traced to LLM extraction errors that disproportionately break entailment chains in valid structures. The tiebreaker design exploits this by restricting Z3 authority to low-consensus cases where ensemble benefits from symbolic correction outweigh extraction risks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ccd7509-87be-4750-b39b-f49972978140",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "d29c65e1-64a5-4e7e-9e6e-a0f59ca27204",
  "sourceToolAssistantUUID": "3ccd7509-87be-4750-b39b-f49972978140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T00:34:09.666Z_

<details><summary>↩ Tool result · `toolu_01Fu7yjbnC5EHzx59y1KH3SL`</summary>

```text
# LTRAG Analysis Based on Available Information

## (1) Autoformalization Approach

LTRAG enhances autoformalization by "building knowledge bases of thought-guided examples" combined with Retrieval-Augmented Generation (RAG). The framework integrates formalization with large language models and symbolic solvers to address limitations in accurately converting natural language problems to formal representations.

## (2) Benchmarks

The paper evaluates LTRAG on **FOLIO and AR-LSAT** datasets. ProofWriter is not mentioned in the provided web content.

## (3) Accuracy Results

The documented performance improvement is: "On GPT-4 and AR-LSAT, it achieves an accuracy gain of 13% over Logic-LM." The abstract also states that "LTRAG consistently outperforms Logic-LM and LINC across different models," but specific accuracy figures for FOLIO or other metrics are not provided in this webpage excerpt.

## (4) Analysis of When Autoformalization Helps vs Hurts

The available content does not contain analysis distinguishing scenarios where autoformalization provides benefits versus cases where it may impair reasoning performance. This type of detailed breakdown would require reviewing the full paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2e678ca-33c9-41a1-87a2-172022a5d217",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "bbb8b310-4a72-47dd-b53e-1f997e402fd4",
  "sourceToolAssistantUUID": "f2e678ca-33c9-41a1-87a2-172022a5d217",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-12T00:34:15.539Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01798KWMGQnmkgN7zbrT3mYV`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.20055",
  "prompt": "Extract: (1) Exactly how does semantic routing classify claims as symbolic vs neural? What features/criteria? (2) What specific benchmarks are used (list all), and is FOLIO among them? (3) Are there any results on FOLIO specifically? (4) Does VERGE analyze error complementarity -- when symbolic helps vs when neural helps? (5) What limitations are acknowledged?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbb8b310-4a72-47dd-b53e-1f997e402fd4",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjdCNUyeA1DXYr4DFZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb399a8b-089f-4306-999e-aa03ea6f79b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WF5uPKkpKTL22vgBkeB9JR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2958,
      "cache_read_input_tokens": 15146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2958,
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

_source line 29 · 2026-05-12T00:34:16.576Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WmVQBmnNJur7isPru3WJLy`</summary>

```json
{
  "query": "FoVer first-order logic verification FOLIO ProofWriter accuracy results 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb399a8b-089f-4306-999e-aa03ea6f79b8",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjdCNUyeA1DXYr4DFZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79ac7bc4-33e9-4c58-833e-7e67d506cf97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WF5uPKkpKTL22vgBkeB9JR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2958,
      "cache_read_input_tokens": 15146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2958,
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

_source line 30 · 2026-05-12T00:34:17.085Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01777ZjynwJWwMjvLcSk9ARf`</summary>

```json
{
  "query": "FOLIO benchmark accuracy results GPT-4 Claude 2025 2026 first-order logic reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79ac7bc4-33e9-4c58-833e-7e67d506cf97",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjdCNUyeA1DXYr4DFZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "865f34ed-bcf1-4de3-8dbf-c9dd9674fe97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WF5uPKkpKTL22vgBkeB9JR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2958,
      "cache_read_input_tokens": 15146,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2958
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 279,
          "cache_read_input_tokens": 15146,
          "cache_creation_input_tokens": 2958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2958,
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

_source line 31 · 2026-05-12T00:34:23.455Z_

<details><summary>↩ Tool result · `toolu_01WmVQBmnNJur7isPru3WJLy`</summary>

```text
Web search results for query: "FoVer first-order logic verification FOLIO ProofWriter accuracy results 2025"

Links: [{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.tacl-1.61/"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/article/view/8211"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning","url":"https://www.researchgate.net/publication/397118426_FoVer_First-Order_Logic_Verification_for_Natural_Language_Reasoning"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning Yu Pei1, 2","url":"https://direct.mit.edu/tacl/article-pdf/doi/10.1162/TACL.a.41/2561649/tacl.a.41.pdf"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | Request PDF","url":"https://www.researchgate.net/publication/363269585_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic"},{"title":"GitHub - peiyu-cn/FoVer: Official code repository for the paper: \"FoVer: First-Order Logic Verification for Natural Language Reasoning\" (TACL) · GitHub","url":"https://github.com/peiyu-cn/FoVer"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs:","url":"https://arxiv.org/pdf/2409.16461"},{"title":"ProofWriter Dataset","url":"https://www.emergentmind.com/topics/proofwriter-dataset"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://www.researchgate.net/publication/386192415_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbCwic3ViUGFnZSI6bnVsbH19"}]

Based on the search results, I found information about FoVer and its accuracy results on ProofWriter and FOLIO datasets from 2025:

## Overview

FoVer (First-order logic Verification) is an automated pipeline that verifies the logical correctness of reasoning texts using first-order logic, operating through LLM-driven translation of natural language into executable logical expressions and automated logical verification using the Z3 theorem prover.

## Evaluation and Results

FoVer was evaluated on specialized logical datasets (ProofWriter and FOLIO) and real-world LLM outputs (REVEAL). The performance was compared against two baselines: 2-shot CoT and Logic-LM.

### Key Accuracy Findings

FoVer outperforms existing methods in logical verification significantly, showing notable improvements in accuracy across both ideal and practical scenarios.

Accuracies of the executable part remain 100% in relaxed evaluation, suggesting the robustness of FoVer. 

On the FOLIO dataset specifically, when considering inexecutable samples, accuracies of Logic-LM and FoVer are both lower than those of CoT; however, when considering only executable samples, both outperform CoT.

## Publication

The research was published by Yu Pei, Yongping Du, and Xingnan Jin in Transactions of the Association for Computational Linguistics in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79ac7bc4-33e9-4c58-833e-7e67d506cf97",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "e7fcb15d-2e0a-4429-8cc5-86dfde58049a",
  "sourceToolAssistantUUID": "79ac7bc4-33e9-4c58-833e-7e67d506cf97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T00:34:28.899Z_

<details><summary>↩ Tool result · `toolu_01777ZjynwJWwMjvLcSk9ARf`</summary>

```text
Web search results for query: "FOLIO benchmark accuracy results GPT-4 Claude 2025 2026 first-order logic reasoning"

Links: [{"title":"AI Model Benchmarks May 2026 | Compare GPT-5, Claude 4.5, Gemini 2.5, Grok 4 | LM Council","url":"https://lmcouncil.ai/benchmarks"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"Best AI Models: April + May 2026 Leaderboard (GPT-5.5, Claude Opus 4.7, DeepSeek V4)","url":"https://www.buildfastwithai.com/blogs/best-ai-models-may-2026-leaderboard"},{"title":"ChatGPT vs Claude 2026: Full Comparison [Tested]","url":"https://tech-insider.org/claude-vs-chatgpt-2026/"},{"title":"Artificial Analysis Intelligence Index | Artificial Analysis","url":"https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"},{"title":"Comparison of AI Models across Intelligence, Performance, and Price","url":"https://artificialanalysis.ai/models"},{"title":"Best AI Models April 2026: GPT-5.5, Claude & Gemini Compared","url":"https://www.buildfastwithai.com/blogs/best-ai-models-april-2026-comparison"},{"title":"Best AI Models in 2026: GPT-5.5 vs Claude vs Gemini - Complete Ranking | by Sanjeev Patel | Medium","url":"https://medium.com/@sanjeevpatel3007/best-ai-models-in-2026-the-complete-honest-ranking-d67b63cf3543"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"GDPval-AA Leaderboard | Artificial Analysis","url":"https://artificialanalysis.ai/evaluations/gdpval-aa"}]

Based on my search results, I wasn't able to find specific information about FOLIO benchmark results for GPT-4, Claude 2025/2026, or other models. The search results returned information about various other benchmarks (GPQA Diamond, SWE-bench, Terminal-Bench, etc.) and model comparisons from 2025-2026, but did not include FOLIO benchmark data specifically.

Let me try a more targeted search for FOLIO benchmark results:

Links: [{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/abs/2209.00840"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1229/"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://arxiv.org/html/2209.00840v2"},{"title":"[2209.00840] FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://ar5iv.labs.arxiv.org/html/2209.00840"},{"title":"Agentified Assessment of Logical Reasoning Agents","url":"https://arxiv.org/html/2603.02788v1"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://www.researchgate.net/publication/386192415_FOLIO_Natural_Language_Reasoning_with_First-Order_Logic?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbCwic3ViUGFnZSI6bnVsbH19"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic","url":"https://github.com/Yale-LILY/FOLIO"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"[2603.02788v1] Agentified Assessment of Logical Reasoning Agents","url":"https://arxiv.org/abs/2603.02788v1"},{"title":"FOLIO: Natural Language Reasoning with First-Order Logic | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/folio-natural-language-reasoning-first-order-logic"}]

Based on my search results, I can provide you with information about FOLIO benchmark results, though the available data focuses on earlier models rather than the newest 2026 releases you asked about.

## FOLIO Benchmark Overview

FOLIO is a human-annotated, logically complex dataset for reasoning in natural language, equipped with first-order logic (FOL) annotations, consisting of 1,430 examples (unique conclusions), each paired with one of 487 sets of premises used to deductively reason for the validity of each conclusion.

## GPT-4 Results

A subset of FOLIO remains a challenge for one of the most capable Large Language Model (LLM) publicly available, GPT-4. More specifically, the original research found that with few-shot prompting, GPT-4 achieved reasonable performance, though advanced prompting techniques improved results.

## Recent 2026 Results

For more recent results, an auto-formalization agent achieved 86.70% accuracy on the FOLIO validation set, outperforming a chain-of-thought baseline (73.89%). This represents a specialized agent approach rather than direct LLM performance.

Additionally, GPT-4o and Claude 3.5 Sonnet were evaluated on FOLIO, though specific accuracy numbers for these models on FOLIO were not clearly detailed in the available search results.

Unfortunately, the search results do not contain detailed, direct comparisons of GPT-4, Claude 2, and newer 2025-2026 Claude/GPT models on the FOLIO benchmark with specific accuracy percentages. You may want to check the official FOLIO leaderboard or recent papers on logical reasoning benchmarks for the most current comparative results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "865f34ed-bcf1-4de3-8dbf-c9dd9674fe97",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "65b8d17e-33d3-4e34-8ec2-84456bd6c174",
  "sourceToolAssistantUUID": "865f34ed-bcf1-4de3-8dbf-c9dd9674fe97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-12T00:34:29.219Z_

<details><summary>↩ Tool result · `toolu_01798KWMGQnmkgN7zbrT3mYV`</summary>

```text
# VERGE Analysis: Semantic Routing, Benchmarks, and Error Complementarity

## (1) Semantic Routing Classification

VERGE classifies claims into six semantic types via an LLM classifier (Equation 2). The routing function (Equation 4) operates as follows:

- **SMT-Verify** for Mathematical, Logical, and Temporal claims
- **Soft-Verify** for Commonsense, Vague, and Probabilistic claims  
- **Hybrid** as fallback for SMT errors

The routing mechanism uses "semantic type τᵢ" determined by the model's probability distribution over claim categories. Table 6 provides formal definitions: Mathematical claims involve "arithmetic operations, algebraic constraints, numerical comparisons"; Logical claims concern "formal entailment, set theory inclusion, boolean logic"; Temporal claims involve "linear sequencing, specific timestamps, duration, or precedence constraints."

The authors report 94% router accuracy on a stress-test dataset of 54 claims with F1=0.93 for SMT and F1=0.95 for Soft categories.

## (2) Benchmarks Evaluated

VERGE evaluates six benchmarks:
1. **FOLIO** (logical reasoning)
2. **ProofWriter** (deductive reasoning)
3. **ZebraLogic** (constraint satisfaction)
4. **AR-LSAT** (legal reasoning)
5. **BBEH** (Big-Bench Extra Hard)
6. **HLE** (Humanity's Last Exam)

## (3) FOLIO Results

Yes, FOLIO is prominently featured. Results across three models:

| Model | VERGE Performance |
|-------|-------------------|
| GPT-OSS-20B | 89.2% ± 1.1 |
| GPT-OSS-120B | 84.7% ± 0.9 |
| Claude Sonnet-3.7 | 87.9% ± 0.7 |

VERGE outperforms standard prompting (CoT: 32-40%) and most neuro-symbolic baselines (LogicLM: 27.5-71.6%).

## (4) Error Complementarity Analysis

The paper does not systematically analyze when symbolic versus neural verification succeeds or fails. However, ablation studies (Table 3) reveal:

- **Soft-Only removal** causes average 22.8% performance drop, especially on ZebraLogic (91.0% → 70.2%) and ProofWriter (89.9% → 75.8%), indicating "formal verification is necessary...for complex logical dependencies"

- **Removing semantic routing** halves HLE performance (30.5% → 15.2%), suggesting symbolic verification alone "fails on ambiguous domains"

The paper acknowledges a "formalization barrier" at 70B+ parameters where models achieve >90% SMT syntax validity. Models under 20B achieve only ~30% validity, limiting symbolic effectiveness to "spell-checking" rather than semantic reasoning.

## (5) Acknowledged Limitations

**Computational Overhead**: "VERGE incurs significantly higher latency than single-pass generation. Each iteration requires claim decomposition, multiple formalization attempts (K=3), consensus computation, SMT solver calls, and feedback generation. For problems with n>20 atomic claims, the pipeline requires 15-30 seconds per iteration compared to >2 seconds for standard Chain-of-Thought prompting."

**Formalization Barrier**: Models under 20B parameters restrict the solver to "syntax checking rather than semantic verification," creating "a capability threshold where only organizations with access to frontier models (≥70B parameters) can leverage VERGE's full potential."

**Expressiveness Constraints**: "Restricting to decidable logics (QF-UF, LIA) sacrifices expressiveness—claims requiring universal quantification, non-linear arithmetic, or recursive definitions cannot be formally verified."

**Ethical Risks**: The framework verifies "internal consistency and logical entailment, not moral soundness or factual truth" and warns of "verified hallucinations" if autoformalization produces "syntactically valid but semantically incorrect SMT code."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb399a8b-089f-4306-999e-aa03ea6f79b8",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "2715f249-fae3-4308-8312-dc4b6de3f5fb",
  "sourceToolAssistantUUID": "eb399a8b-089f-4306-999e-aa03ea6f79b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-12T00:34:33.338Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GcRUPzS8TVjaoYehyXMVQs`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.02788v1",
  "prompt": "Extract any FOLIO benchmark accuracy results for recent models. What are the best reported accuracies? What methods achieve SOTA on FOLIO?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2715f249-fae3-4308-8312-dc4b6de3f5fb",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011Cawjee2cUaAokSgL8QSpk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f130c88-7209-4dd2-bf9e-d9a7413ccf13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DZY98ujZYSGG8GY5TFQTr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2708,
      "cache_creation_input_tokens": 1273,
      "cache_read_input_tokens": 18104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1273,
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

_source line 35 · 2026-05-12T00:34:35.430Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012ADKALeoWhbfghgS3a8bWu`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.29500v1",
  "prompt": "Extract: (1) What is this paper's approach to step-level formalization for logic reasoning? (2) Does it evaluate on FOLIO or ProofWriter? (3) What accuracy results are reported? (4) Does it analyze when formalization helps vs hurts?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f130c88-7209-4dd2-bf9e-d9a7413ccf13",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011Cawjee2cUaAokSgL8QSpk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd29eb2a-c9ca-471c-a4d0-e775eb034261",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DZY98ujZYSGG8GY5TFQTr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2708,
      "cache_creation_input_tokens": 1273,
      "cache_read_input_tokens": 18104,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1273
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2708,
          "output_tokens": 241,
          "cache_read_input_tokens": 18104,
          "cache_creation_input_tokens": 1273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1273,
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

_source line 36 · 2026-05-12T00:34:37.274Z_

<details><summary>↩ Tool result · `toolu_01GcRUPzS8TVjaoYehyXMVQs`</summary>

```text
# FOLIO Benchmark Results

Based on the provided paper, here are the reported accuracies on FOLIO:

## Performance Results

**Auto-formalization agent:** 86.70% accuracy (176/203 correct on cleaned validation set)

**Chain-of-thought baseline:** 73.89% accuracy (150/203 correct)

The paper states: "the auto-formalization agent achieves 86.70% accuracy under the assessor protocol, outperforming a chain-of-thought baseline (73.89%)."

## Method Details

The top-performing approach combines:
- Natural language-to-Z3Py code generation using Gemini 2.5 Flash
- Satisfiability modulo theories (SMT) solving via the Z3 solver
- Self-repair loops for handling syntax errors

The largest performance gap appears in the "False" category, where the auto-formalization method improved from 44.26% to 77.05%.

**Note:** These results are evaluated on a cleaned and verified subset of FOLIO (203 validation examples), with potential label errors identified and corrected using the Vampire theorem prover.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f130c88-7209-4dd2-bf9e-d9a7413ccf13",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "c6e9af49-4d75-4c75-97c0-cd6f7e484f1b",
  "sourceToolAssistantUUID": "6f130c88-7209-4dd2-bf9e-d9a7413ccf13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-12T00:34:42.134Z_

<details><summary>↩ Tool result · `toolu_012ADKALeoWhbfghgS3a8bWu`</summary>

```text
# Research Paper Analysis: PRoSFI

## (1) Step-Level Formalization Approach

The paper introduces **PRoSFI** (Process Reward over Structured Formal Intermediates), which sidesteps direct formal proof generation. Instead of requiring models to produce complete Lean code, the method asks models to "output a series of reasoning blocks where each block contains a natural language explanation and a corresponding structured intermediate representation" in JSON/YAML format. Each step includes dependencies, conclusions in formal language, and the logical rule applied, which are then verified by formal provers.

## (2) Evaluation Datasets

The paper does **not** evaluate on FOLIO or ProofWriter. Instead, it uses:
- **ProverQA**: A synthetic first-order logic benchmark with difficulty levels (easy, medium, hard)
- **Knights and Knaves dataset**: Algorithmic logic puzzles with controlled complexity
- **ProverQA-Extra**: 128 out-of-distribution examples for generalization testing

## (3) Reported Accuracy Results

On ProverQA-Hard:
- Answer Correct Rate: **92.97%**
- GPT Soundness: **76.07%** (compared to 21.97% for outcome-only rewards)

On ProverQA-Extra:
- Answer Correct Rate: **91.94%**
- GPT Soundness: **56.10%** (vs. 11.87% baseline)

## (4) Formalization Help vs. Harm Analysis

The paper demonstrates that structured formalization **helps significantly**. Outcome-reward methods achieved high answer accuracy (91.31%) but low soundness (21.97%), revealing flawed reasoning paths. PRoSFI maintained comparable accuracy while improving soundness by 54 percentage points, showing that formal verification provides crucial step-level supervision distinguishing valid from invalid reasoning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd29eb2a-c9ca-471c-a4d0-e775eb034261",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a1a848061a6c1817c",
  "type": "user",
  "uuid": "70348291-d523-44c9-bf89-2833d961ef7c",
  "sourceToolAssistantUUID": "dd29eb2a-c9ca-471c-a4d0-e775eb034261",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-12T00:35:19.281Z_

Here is a concise synthesis of findings across all five queries:

---

**1. VERGE (arXiv 2601.20055)**

VERGE is the closest existing work to a verification routing system. It classifies claims into six semantic types (mathematical, logical, temporal, commonsense, vague, probabilistic) via an LLM classifier, then routes: SMT solvers for decidable claims, LLM ensembles for soft/commonsense claims. It evaluates on FOLIO (84.7-89.2%), ProofWriter, ZebraLogic, AR-LSAT, BBEH, and HLE. Ablation shows removing soft-verify drops performance 22.8% and removing routing halves HLE performance. However, **VERGE does not perform systematic error complementarity analysis** -- it does not characterize which claim types each verifier gets right/wrong or when autoformalization introduces errors.

**2. Step-Level Autoformalization**

Several recent systems exist: **VeriCoT** (ICLR 2026) formalizes each CoT step into FOL and verifies with solvers (tested on ProofWriter, not FOLIO). **PRoSFI** uses structured formal intermediaries with step-level prover verification (tested on ProverQA, not FOLIO/ProofWriter). **FoVer** (TACL 2025) translates NL to FOL and verifies with Z3, noting that on FOLIO, executable samples outperform CoT but inexecutable samples drag overall accuracy below CoT -- a critical finding about formalization failure modes. **StepProof** does step-by-step proof decomposition into verifiable subproofs.

**3. Neuro-Symbolic Verification Routing**

Beyond VERGE, **FregeLogic** (SemEval 2026) uses a vote-margin routing criterion: when a 5-member LLM ensemble splits 3-2, it defers to Z3. This triggers on only 7.9% of cases but produces a net positive (19 correct flips vs. 11 incorrect). It explicitly identifies **directional error asymmetry**: Z3 has 97.6% accuracy on invalid syllogisms but only 52.2% on valid ones due to LLM extraction errors breaking entailment chains. This is the closest existing work to error complementarity analysis, but it is limited to syllogistic reasoning.

**4. FOLIO SOTA**

No centralized leaderboard exists. Best reported results: VERGE achieves ~84-89% (depending on model). An autoformalization agent using Gemini 2.5 Flash + Z3 achieves **86.7%** on a cleaned FOLIO validation subset (vs. 73.9% CoT baseline). The biggest gain is on "False" conclusions (44.3% to 77.1%). FOLIO remains unsaturated and challenging.

**5. When Autoformalization Helps vs. Hurts**

FoVer's finding is key: on executable samples, formalization beats CoT; on inexecutable samples (formalization failures), it hurts. **LTRAG** (ACL Findings 2025) improves formalization quality via thought-guided RAG, gaining 13% over Logic-LM on AR-LSAT. VERGE acknowledges a "formalization barrier" -- models under 20B parameters produce only ~30% valid SMT code. No paper performs a **systematic, fine-grained error complementarity analysis** characterizing exactly which problem features predict formalization success/failure and how symbolic vs. neural errors are distributed.

---

**What exists:** Routing frameworks (VERGE, FregeLogic), step-level formalization (VeriCoT, FoVer, PRoSFI), and evidence that formalization helps on some instances but hurts on others.

**What is genuinely missing:** A systematic **error complementarity analysis** that (a) characterizes at the instance level when symbolic verification succeeds where neural fails and vice versa, (b) identifies predictive features for routing decisions beyond coarse claim-type heuristics, and (c) quantifies the complementarity gap on standard benchmarks like FOLIO. FregeLogic's directional asymmetry finding is suggestive but limited to syllogisms. VERGE routes by claim type but never analyzes whether its routing decisions are optimal or where errors concentrate. This represents a clear gap for a proposal focused on principled error complementarity analysis.

Sources:
- [VERGE: arXiv 2601.20055](https://arxiv.org/abs/2601.20055)
- [VeriCoT (ICLR 2026)](https://openreview.net/forum?id=zHuV3Vatov)
- [FregeLogic (SemEval 2026)](https://arxiv.org/html/2604.18328)
- [FoVer (TACL 2025)](https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural)
- [LTRAG (ACL Findings 2025)](https://aclanthology.org/2025.findings-acl.126/)
- [PRoSFI](https://arxiv.org/html/2603.29500v1)
- [Agentified Assessment of Logical Reasoning Agents](https://arxiv.org/abs/2603.02788v1)
- [FOLIO Dataset](https://github.com/Yale-LILY/FOLIO)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70348291-d523-44c9-bf89-2833d961ef7c",
  "isSidechain": true,
  "agentId": "a1a848061a6c1817c",
  "requestId": "req_011CawjfbGh52vo3zCK1F3DV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "026e378e-b3cf-4d44-a747-8e722d167d5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XPYzbSWfUnosobXgdH1j2M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3687,
      "cache_read_input_tokens": 19377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3687,
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
