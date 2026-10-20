# Research conversation: You are helping me verify claims in an ML research proposal about ontology-constrained decoding for information extracti

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a668acc4d944c984b.jsonl`
- **Structured JSON:** [`31b6dea84347563ccf85.json`](../../sessions/31/31b6dea84347563ccf85.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-12T00:43:21.889Z_

You are helping me verify claims in an ML research proposal about ontology-constrained decoding for information extraction (IE). I need you to search for and verify the following:

1. Search for "IterGen ICLR 2025 Ugare semantic-aware backtracking" - verify this paper exists and its claims about grammar+semantic callback paradigm with backtracking
2. Search for "Synchromesh ICLR 2022 Poesia constrained semantic decoding" - verify it's the foundational work on combining syntactic+semantic constraints
3. Search for "LLM+ASP workflow Tran ICLP 2025 entity relation extraction" or "arXiv 2508.12611" - verify this post-hoc type constraint checking paper and its SciERC results (35.37% RE F1 with 10% training data)
4. Search for "BoostCD BoostIE EMNLP 2025 constrained unconstrained decoding" - verify this paper and whether it's limited to vocabulary membership constraints
5. Search for "ODKE+ Apple ontology knowledge extraction arXiv 2025" - verify this paper and its 98.8% precision claim
6. Search for "The Format Tax constrained decoding 2026" - verify this paper and its finding about prompt-level vs decoder-level accuracy drops
7. Search for "CRANE ICML 2025 Banerjee constrained decoding TC0" - verify this theoretical result
8. Search for "EnriCo Zaratiana ASP entity relation extraction 2024" - verify this paper

For each paper, report: does it exist? Are the claims about it accurate? What venue/year? Any key details the proposal might have wrong?

Use WebSearch extensively. Report your findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "36c250cd-18a9-40fb-8ee8-8c3434062894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:43:21.893Z_

```json
{
  "parentUuid": "36c250cd-18a9-40fb-8ee8-8c3434062894",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
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
  "uuid": "979b94db-93b4-4d54-906a-ec8922477979",
  "timestamp": "2026-05-12T00:43:21.893Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-12T00:43:23.967Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FqMtC6JTstPkA8Uoyo1J2F`</summary>

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
  "parentUuid": "979b94db-93b4-4d54-906a-ec8922477979",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkKuQAYbkLb7Hcwy3ph",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e11dc7e7-a89f-4a30-b46e-a8c1424a7cab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WScXDuPaakUuoHPhoLRK4H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8153,
      "cache_read_input_tokens": 0,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8153
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8153,
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

_source line 4 · 2026-05-12T00:43:23.971Z_

<details><summary>↩ Tool result · `toolu_01FqMtC6JTstPkA8Uoyo1J2F`</summary>

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
  "parentUuid": "e11dc7e7-a89f-4a30-b46e-a8c1424a7cab",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "5f264cf2-84ea-4b55-9b1d-ad88b79f601b",
  "sourceToolAssistantUUID": "e11dc7e7-a89f-4a30-b46e-a8c1424a7cab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-12T00:43:26.633Z_

I'll search for all 8 papers simultaneously to verify the claims efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f264cf2-84ea-4b55-9b1d-ad88b79f601b",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkL4Z5W1rDbTM1KZLgC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d45a910-2d6c-4e00-9c95-5ee2e2b48758",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Px32ATysii8RfTzb4gQhc9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 6 · 2026-05-12T00:43:27.541Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PJBURwyzZ7bQmAEk4Fm3wy`</summary>

```json
{
  "query": "IterGen ICLR 2025 Ugare semantic-aware backtracking grammar constraints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d45a910-2d6c-4e00-9c95-5ee2e2b48758",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkL4Z5W1rDbTM1KZLgC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7c70319-296c-4781-bd6f-2637c753c0d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Px32ATysii8RfTzb4gQhc9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 7 · 2026-05-12T00:43:28.538Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NePuSCQPn5ycjiGQGnoock`</summary>

```json
{
  "query": "Synchromesh ICLR 2022 Poesia constrained semantic decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7c70319-296c-4781-bd6f-2637c753c0d9",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkL4Z5W1rDbTM1KZLgC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "328602f6-4cb7-46fe-8346-e885baccf831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Px32ATysii8RfTzb4gQhc9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 8 · 2026-05-12T00:43:29.620Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DWFGAYHTBJ39dNRBc5SyBK`</summary>

```json
{
  "query": "LLM ASP workflow Tran ICLP 2025 entity relation extraction SciERC arXiv 2508.12611"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "328602f6-4cb7-46fe-8346-e885baccf831",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkL4Z5W1rDbTM1KZLgC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "173c3190-3f5a-4ee8-83b5-7637418965bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Px32ATysii8RfTzb4gQhc9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 9 · 2026-05-12T00:43:30.280Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013nqLxLMCcm3dDaiz1ZyY6L`</summary>

```json
{
  "query": "BoostCD BoostIE EMNLP 2025 constrained unconstrained decoding vocabulary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "173c3190-3f5a-4ee8-83b5-7637418965bb",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkL4Z5W1rDbTM1KZLgC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d643265e-2c18-4231-a42b-7ca71d269e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Px32ATysii8RfTzb4gQhc9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8153,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 272,
          "cache_read_input_tokens": 8153,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 10 · 2026-05-12T00:43:34.464Z_

<details><summary>↩ Tool result · `toolu_01PJBURwyzZ7bQmAEk4Fm3wy`</summary>

```text
Web search results for query: "IterGen ICLR 2025 Ugare semantic-aware backtracking grammar constraints"

Links: [{"title":"[2410.07295] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://arxiv.org/abs/2410.07295"},{"title":"IterGen: Iterative Semantic-aware Structured LLM ...","url":"https://iclr.cc/media/iclr-2025/Slides/29157.pdf"},{"title":"Shubham Ugare","url":"https://shubhamugare.github.io/"},{"title":"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking | OpenReview","url":"https://openreview.net/forum?id=ac93gRzxxV"},{"title":"ITERGEN: ITERATIVE SEMANTIC-AWARE STRUCTURED ...","url":"https://openreview.net/pdf?id=ac93gRzxxV"},{"title":"[PDF] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/8f918a87d0f1bc090fca1dbdfbc4d06a9dc88a66"},{"title":"ICLR Poster IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://iclr.cc/virtual/2025/poster/29157"},{"title":"[Literature Review] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://www.themoonlight.io/en/review/itergen-iterative-semantic-aware-structured-llm-generation-with-backtracking"},{"title":"Shubham Ugare shubhamdugare@gmail.com https://shubhamugare.github.io Education","url":"https://shubhamugare.github.io/assets/pdf/resume.pdf"},{"title":"[Quick Review] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://liner.com/review/itergen-iterative-semanticaware-structured-llm-generation-with-backtracking"}]

I found comprehensive information about IterGen. Here's what the search revealed:

## IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking

IterGen is authored by Shubham Ugare and 4 other authors, and it was presented at ICML 2025.

### Overview

IterGen is a user-friendly library for iterative, grammar-guided LLM generation that enables users to move both forward and backward within the generated output based on grammar symbols, while leveraging a symbol-to-position mapping and maintaining the key-value (KV) cache state to ensure efficient and structured generation while allowing for corrections during the process.

### Problem Addressed

Large Language Models are widely used for natural language and code generation, but their outputs often suffer from hallucination, toxicity, and incorrect results, and current libraries for structured LLM generation rely on left-to-right decoding without support for backtracking, limiting the ability to correct or refine outputs mid-generation.

### Key Applications and Results

IterGen demonstrates its effectiveness in two important applications: reducing privacy leakage in LLM outputs and improving the accuracy of LLM-generated SQL and Vega-Lite queries. IterGen achieves 18.5% mean improvement over the state-of-the-art grammar-guided generation technique, and it reduces privacy leaks in LLM-generated text from 51.4% to 0%.

### Code Availability

IterGen code is available at https://github.com/structuredllm/itergen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7c70319-296c-4781-bd6f-2637c753c0d9",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "af8058c5-48af-4298-9fdd-4a4e7fbbed79",
  "sourceToolAssistantUUID": "a7c70319-296c-4781-bd6f-2637c753c0d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T00:43:36.866Z_

<details><summary>↩ Tool result · `toolu_01DWFGAYHTBJ39dNRBc5SyBK`</summary>

```text
Web search results for query: "LLM ASP workflow Tran ICLP 2025 entity relation extraction SciERC arXiv 2508.12611"

Links: [{"title":"[2508.12611] An LLM + ASP Workflow for Joint Entity-Relation Extraction","url":"https://arxiv.org/abs/2508.12611"},{"title":"An LLM + ASP Workflow for Joint Entity-Relation Extraction","url":"https://arxiv.org/html/2508.12611v2"},{"title":"Entity Quality Enhancement in Knowledge Graphs through ...","url":"https://aclanthology.org/2025.genaik-1.14.pdf"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Full article: An entity and relation extraction model based on context query and axial attention towards patent texts","url":"https://www.tandfonline.com/doi/full/10.1080/09540091.2024.2426816"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"A Few-Shot Approach for Relation Extraction Domain Adaptation using Large Language Models","url":"https://arxiv.org/html/2408.02377"},{"title":"Iterative Transformer-based Entity Recognition and ...","url":"https://aclanthology.org/2024.findings-emnlp.655.pdf"},{"title":"An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction","url":"https://arxiv.org/html/2401.01326v1"},{"title":"Large language model augmented joint learning framework for entity-relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073"}]

Based on the search results, I found information about the paper you're looking for:

The paper proposes harnessing the capabilities of generative pre-trained large language models (LLMs) and Answer Set Programming (ASP) to perform joint entity-relation extraction (JERE), presenting a generic workflow for JERE using LLMs and ASP.

The paper is authored by Trang Tran, Trung Hoang Le, Huiping Cao, and Tran Cao Son from New Mexico State University.

The workflow is generic in the sense that it can be applied for JERE in any domain and takes advantage of LLM's capability in natural language understanding by working directly with unannotated text. It exploits the elaboration tolerant feature of ASP in that no modification of its core program is required when additional domain specific knowledge, in the form of type specifications, is found and needs to be used.

**Results:**

The results of experiments show that the LLM + ASP workflow is better than state-of-the-art JERE systems in several categories with only 10% of training data. It is able to achieve a 2.5 times (35% over 15%) improvement in the Relation Extraction task for the SciERC corpus, one of the most difficult benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "173c3190-3f5a-4ee8-83b5-7637418965bb",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "5d53ae78-a4a9-4f00-848f-8704e1f7a83f",
  "sourceToolAssistantUUID": "173c3190-3f5a-4ee8-83b5-7637418965bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T00:43:37.979Z_

<details><summary>↩ Tool result · `toolu_013nqLxLMCcm3dDaiz1ZyY6L`</summary>

```text
Web search results for query: "BoostCD BoostIE EMNLP 2025 constrained unconstrained decoding vocabulary"

Links: [{"title":"Combining Constrained and Unconstrained Decoding via ...","url":"https://aclanthology.org/2025.emnlp-main.926.pdf"},{"title":"[2506.14901] Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/abs/2506.14901"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/html/2506.14901"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting:","url":"https://openreview.net/pdf?id=3Qbw5Ja6Sc"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=8575&show=50"},{"title":"Marija Sakota's research works | Swiss Federal Institute of Technology in Lausanne and other places","url":"https://www.researchgate.net/scientific-contributions/Marija-Sakota-2168060164"},{"title":"EMNLP.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2025"},{"title":"Low-Hallucination and Efficient Coreference Resolution ...","url":"https://aclanthology.org/2025.findings-emnlp.934.pdf"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"}]

Based on the search results, I found information about BoostCD and BoostIE from the EMNLP 2025 conference:

## Overview

BoostCD (Boosted Constrained Decoding) combines constrained and unconstrained decoding in two phases: Phase 1 decodes from the base model twice, in constrained and unconstrained mode, obtaining two weak predictions. In phase 2, a learned autoregressive boosted model combines the two weak predictions into one final prediction.

## Key Mechanism

The mistakes made by the base model with vs. without constraints tend to be complementary, which the boosted model learns to exploit for improved performance.

## Application to Information Extraction

BoostCD is demonstrated by applying it to closed information extraction. The model, BoostIE, outperforms prior approaches both in and out of distribution, addressing several common errors identified in those approaches.

## Vocabulary Constraints

BoostCD is applied to closed information extraction (cIE) as an example of a structured task with constraints (defined by the content of the knowledge base) that tend to change dynamically in real-life settings.

The paper was accepted to EMNLP 2025 main conference and represents a novel approach to handling structured NLP tasks where output constraints may change without requiring model retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d643265e-2c18-4231-a42b-7ca71d269e63",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "6b71f084-6317-4b79-adc9-d4ca708ae128",
  "sourceToolAssistantUUID": "d643265e-2c18-4231-a42b-7ca71d269e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:43:42.542Z_

<details><summary>↩ Tool result · `toolu_01NePuSCQPn5ycjiGQGnoock`</summary>

```text
Web search results for query: "Synchromesh ICLR 2022 Poesia constrained semantic decoding"

Links: [{"title":"[PDF] Synchromesh: Reliable code generation from pre-trained language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Synchromesh:-Reliable-code-generation-from-language-Poesia-Polozov/b62d63580b81a2cbb20c3c1593dd62d118e4cb07"},{"title":"GitHub - kanishkg/synchromesh: Get language models to generate responses in a specific format reliably. Open source implementation of Synchromesh: Reliable code generation from pre-trained language models.","url":"https://github.com/kanishkg/synchromesh"},{"title":"[Quick Review] Synchromesh: Reliable code generation from pre-trained language models","url":"https://liner.com/review/synchromesh-reliable-code-generation-from-pretrained-language-models"},{"title":"Published as a conference paper at ICLR 2022","url":"https://www.vuminhle.com/pdf/iclr22.pdf"},{"title":"ITERGEN: ITERATIVE SEMANTIC-AWARE STRUCTURED ...","url":"https://openreview.net/pdf?id=ac93gRzxxV"},{"title":"Synchromesh: Reliable code generation from pre-trained language models · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/poesia2022synchromesh/"},{"title":"Synchromesh: Reliable Code Generation from Pre-trained Language Models | OpenReview","url":"https://openreview.net/forum?id=KmtVD97J43e"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf"},{"title":"SYNCHROMESH: RELIABLE CODE GENERATION FROM PRE-TRAINED LANGUAGE MODELS","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2022/01/csd_arxiv.pdf"},{"title":"Under review as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=ICSvW69W5K"}]

Based on the search results, here's what I found about Synchromesh, ICLR 2022, and the work by Poesia on constrained semantic decoding:

## Synchromesh: Overview

Synchromesh is a framework for substantially improving the reliability of pre-trained models for code generation. This ICLR 2022 paper summarizes SYNCHROMESH, a framework enhancing code generation reliability using semantic decoding and tuning.

## Key Components

Synchromesh comprises two components. First, it retrieves few-shot examples from a training bank using Target Similarity Tuning (TST), a novel method for semantic example selection. Then, Synchromesh feeds the examples to a pre-trained language model and samples programs using Constrained Semantic Decoding (CSD): a general framework for constraining the output to a set of valid programs in the target language.

## Constrained Semantic Decoding (CSD)

Constrained Semantic Decoding (CSD) is presented as a general framework for constraining the output of a language model to a set of valid programs in the target language by leveraging constraints on partial outputs. Completion Engines (CEs) are defined as an abstraction capable of implementing rich classes of semantic program constraints, including syntax, scope, typing rules, and contextual logic, aligned with the language model's token vocabulary.

## Evaluation and Results

The method is evaluated across SQL, Vega-Lite, and SMCalFlow, demonstrating that SYNCHROMESH provides complementary gains from both TST and CSD in prediction accuracy and in preventing runtime errors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "328602f6-4cb7-46fe-8346-e885baccf831",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "6656ac86-4f39-4c8f-9987-941ec3171df2",
  "sourceToolAssistantUUID": "328602f6-4cb7-46fe-8346-e885baccf831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-12T00:43:46.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RVT1AxThd2ob4P2DSm9ugg`</summary>

```json
{
  "query": "ODKE+ Apple ontology knowledge extraction arXiv 2025 precision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6656ac86-4f39-4c8f-9987-941ec3171df2",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkMRj5JDpTZ8SdPck6A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbd08057-7164-45cc-8391-550beaa28e66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UDFNeujy4eQpuXcweVJJ3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1686,
      "cache_creation_input_tokens": 2250,
      "cache_read_input_tokens": 9545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2250,
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

_source line 15 · 2026-05-12T00:43:47.159Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LkkYBS8TTAnGwjXxqh69D3`</summary>

```json
{
  "query": "\"Format Tax\" constrained decoding 2026 prompt decoder accuracy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbd08057-7164-45cc-8391-550beaa28e66",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkMRj5JDpTZ8SdPck6A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70032181-fdb4-4fb0-9349-d89a2d328850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UDFNeujy4eQpuXcweVJJ3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1686,
      "cache_creation_input_tokens": 2250,
      "cache_read_input_tokens": 9545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2250,
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

_source line 16 · 2026-05-12T00:43:47.984Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lsg7NvvLdXpUb7DKqGtzgS`</summary>

```json
{
  "query": "CRANE ICML 2025 Banerjee constrained decoding TC0 complexity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70032181-fdb4-4fb0-9349-d89a2d328850",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkMRj5JDpTZ8SdPck6A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "705f7b19-0d94-4093-9ebd-97975fb2f594",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UDFNeujy4eQpuXcweVJJ3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1686,
      "cache_creation_input_tokens": 2250,
      "cache_read_input_tokens": 9545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2250,
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

_source line 17 · 2026-05-12T00:43:48.529Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CYu3eo8EhRWX97PXfurpdC`</summary>

```json
{
  "query": "EnriCo Zaratiana ASP entity relation extraction 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "705f7b19-0d94-4093-9ebd-97975fb2f594",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkMRj5JDpTZ8SdPck6A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6702411-68fa-453c-a4d4-2f9ace000cf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UDFNeujy4eQpuXcweVJJ3K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1686,
      "cache_creation_input_tokens": 2250,
      "cache_read_input_tokens": 9545,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2250
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1686,
          "output_tokens": 222,
          "cache_read_input_tokens": 9545,
          "cache_creation_input_tokens": 2250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2250,
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

_source line 18 · 2026-05-12T00:43:54.290Z_

<details><summary>↩ Tool result · `toolu_01LkkYBS8TTAnGwjXxqh69D3`</summary>

```text
Web search results for query: ""Format Tax" constrained decoding 2026 prompt decoder accuracy"

Links: [{"title":"The Format Tax","url":"https://arxiv.org/html/2604.03616v1"},{"title":"A Guide to Structured Generation Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Grammar-Constrained Decoding Makes Large Language ...","url":"https://aclanthology.org/2025.acl-industry.34.pdf"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"Part 6: Implementing Constrained Decoding | by Albersj | Medium","url":"https://medium.com/@albersj66/part-6-implementing-constrained-decoding-for-phi-3-vision-2c72a1be6a17"},{"title":"Constrained Decoding with Triton Inference Server — NVIDIA Triton Inference Server","url":"https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Constrained_Decoding/README.html"},{"title":"Taming LLM Outputs: Your Guide to Structured Text Generation","url":"https://www.dataiku.com/stories/blog/your-guide-to-structured-text-generation"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/html/2403.06988v1"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"}]

Based on the search results, I've found comprehensive information about "The Format Tax" and its relationship to constrained decoding and prompt decoder accuracy. Here are the key findings:

## Overview of The Format Tax

Structured output requirements—JSON, XML, LaTeX, Markdown—substantially degrade reasoning and writing performance across open-weight models. This phenomenon is known as the "format tax."

## The Root Cause: Prompt vs. Decoder

Interestingly, format-requesting instructions alone cause most of the accuracy loss, before any decoder constraint is applied. The research response has focused on constrained decoding, but sampling bias accounts for only a fraction of the degradation. This means the format tax is paid at the prompt—not the decoder.

## Impact on Decoder Accuracy

Across most open-weight model–task–format combinations, structured output reduces accuracy compared to freeform generation, whether or not constrained decoding is applied. Additionally, standard prompt-level mitigations—few-shot examples and explicit schema descriptions—leave the majority of the degradation intact.

## Solutions

Decoupling reasoning from formatting works, with the model reasoning freely before producing structured output—either via a second reformatting pass or extended thinking—recovers most of the lost accuracy. Recent closed-weight models show near-zero degradation, suggesting that the tax is not inherent to structured generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70032181-fdb4-4fb0-9349-d89a2d328850",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "5af6af2c-6583-42c0-a1c9-5a2ee4584001",
  "sourceToolAssistantUUID": "70032181-fdb4-4fb0-9349-d89a2d328850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:43:54.522Z_

<details><summary>↩ Tool result · `toolu_01Lsg7NvvLdXpUb7DKqGtzgS`</summary>

```text
Web search results for query: "CRANE ICML 2025 Banerjee constrained decoding TC0 complexity"

Links: [{"title":"ICML Poster CRANE: Reasoning with constrained LLM generation","url":"https://icml.cc/virtual/2025/poster/43624"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://debangshu-banerjee.github.io/assets/pdf/CRANE.pdf"},{"title":"Reasoning with constrained LLM generation - CRANE","url":"https://arxiv.org/pdf/2502.09061"},{"title":"[2502.09061] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.09061v3"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://par.nsf.gov/servlets/purl/10633770"},{"title":"CRANE: Reasoning with constrained LLM generation | OpenReview","url":"https://openreview.net/forum?id=wKs9fHYxCV"},{"title":"ICML Poster Flexible and Efficient Grammar-Constrained Decoding","url":"https://icml.cc/virtual/2025/poster/45613"},{"title":"Improving Procedural Skill Explanations via Constrained Generation: A","url":"https://arxiv.org/pdf/2511.20942"}]

Based on the search results, I can provide you with information about CRANE:

## Overview

CRANE is a paper by Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, and Gagandeep Singh, presented as a 2025 ICML poster.

## Main Contributions

The paper addresses the observation that strict enforcement of formal constraints often diminishes the reasoning capabilities of LLMs, and provides a theoretical explanation for why constraining LLM outputs to very restrictive grammars that only allow syntactically valid final answers reduces the reasoning capabilities of the model.

## TC0 Complexity Analysis

The key theoretical insight is formalized in Proposition 3.1, which shows that LLMs under such constraints can only solve problems within the TC0 complexity class (constant-depth threshold circuits). TC0 is a class of computational problems that can be recognized by constant-depth, polynomial-size circuits composed of threshold gates.

## The CRANE Solution

By augmenting the output grammar with carefully designed additional rules, it is possible to preserve the reasoning capabilities of the LLM while ensuring syntactic and semantic correctness in its outputs. CRANE effectively alternates between unconstrained generation for reasoning and constrained generation for producing structurally correct outputs, allowing the model to produce syntactically valid outputs while enabling the LLM to reason.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "705f7b19-0d94-4093-9ebd-97975fb2f594",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "cb9c2018-54d4-4cf2-b1e3-d53c3868603a",
  "sourceToolAssistantUUID": "705f7b19-0d94-4093-9ebd-97975fb2f594",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T00:43:54.661Z_

<details><summary>↩ Tool result · `toolu_01CYu3eo8EhRWX97PXfurpdC`</summary>

```text
Web search results for query: "EnriCo Zaratiana ASP entity relation extraction 2024"

Links: [{"title":"GitHub - urchade/EnriCo: EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://github.com/urchade/EnriCo"},{"title":"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/html/2404.12493v1"},{"title":"[2404.12493] EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/abs/2404.12493"},{"title":"urchade (Urchade Zaratiana) · GitHub","url":"https://github.com/urchade"},{"title":"Paper page - EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://huggingface.co/papers/2404.12493"},{"title":"Urchade Zaratiana","url":"https://urchade.github.io/"},{"title":"GitHub - urchade/ATG: Official code for our paper \"An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction\" which will be published at AAAI 2024.","url":"https://github.com/urchade/ATG"},{"title":"An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/29919"},{"title":"An Entity-Relation Extraction Framework via Symmetry-Aware Augmentation and Priority-Constrained Optimization | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-981-95-3453-1_29"},{"title":"Iterative Transformer-based Entity Recognition and ...","url":"https://aclanthology.org/2024.findings-emnlp.655.pdf"}]

Based on the search results, here's what I found about EnriCo, Zaratiana, ASP, and entity relation extraction in 2024:

## Overview

EnriCo (Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction) is a 2024 research work by Urchade Zaratiana, Nadi Tomeh, Yann Dauxais, Pierre Holat, and Thierry Charnois.

## Key Features

EnriCo is designed for joint entity and relation extraction, which plays a pivotal role in constructing knowledge graphs. The approach addresses two main limitations of existing methods:

1. **Rich Representation**: The model leverages attention mechanisms that allow both entities and relations to dynamically determine the pertinent information required for accurate extraction.

2. **Structural Coherence**: To ensure structural coherence of the output, the model formulates entity and relation prediction using an Answer Set Programming (ASP) solver, enabling the derivation of exact solutions.

## Performance

EnriCo achieves competitive performance on Joint IE datasets, with code available on GitHub at the official repository.

The work represents an important contribution to the field of information extraction by combining neural attention mechanisms with logical constraint solving through ASP to improve both the quality of learned representations and the validity of extracted outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6702411-68fa-453c-a4d4-2f9ace000cf4",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "390aba2e-8d65-4f81-8739-6d7fb2f7aca7",
  "sourceToolAssistantUUID": "a6702411-68fa-453c-a4d4-2f9ace000cf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T00:43:55.380Z_

<details><summary>↩ Tool result · `toolu_01RVT1AxThd2ob4P2DSm9ugg`</summary>

```text
Web search results for query: "ODKE+ Apple ontology knowledge extraction arXiv 2025 precision"

Links: [{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"},{"title":"[2509.04696] ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/abs/2509.04696"},{"title":"(PDF) ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://www.researchgate.net/publication/395338944_ODKE_Ontology-Guided_Open-Domain_Knowledge_Extraction_with_LLMs"},{"title":"Connected Data on X: \"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs Knowledge graphs (KGs) are foundational to many AI applications, but maintaining their freshness and completeness remains costly. ODKE+ is a production-grade system designed by Apple researchers that automatically https://t.co/C6SC3ariNs\" / X","url":"https://x.com/Connected_Data/status/1972610312214819248"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/odke"},{"title":"[PDF] ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ODKE+:-Ontology-Guided-Open-Domain-Knowledge-with-Khorshidi-Nikfarjam/23991e9d5ab7780527a1753633a7f065c5da4663"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/odke-ontology-guided-open-domain-knowledge-extraction"},{"title":"Jackson Atkins on X: \"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs by @Apple Submitted on 4 Sep 2025 https://t.co/6InGsY5Hrm\" / X","url":"https://x.com/JacksonAtkinsX/status/1975029498740650346"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge ...","url":"https://www.facebook.com/connecteddata/posts/odke-ontology-guided-open-domain-knowledge-extraction-with-llmsknowledge-graphs-/1237598545079177/"},{"title":"Odke+: An ontoloty-oriented open-domain and knowledge extraction with llms - Dataforcee Digital","url":"https://dataforcee.us/2025/10/27/odke-an-ontoloty-oriented-open-domain-and-knowledge-extraction-with-llms/"}]

Based on the search results, I found comprehensive information about ODKE+. Here are the key findings:

## Overview

ODKE+ is a production-grade system that automatically extracts and ingests millions of open-domain facts from web sources with high precision.

## Architecture

ODKE+ combines modular components into a scalable pipeline: (1) the Extraction Initiator detects missing or stale facts, (2) the Evidence Retriever collects supporting documents, (3) hybrid Knowledge Extractors apply both pattern-based rules and ontology-guided prompting for large language models (LLMs), (4) a lightweight Grounder validates extracted facts using a second LLM, and (5) the Corroborator ranks and normalizes candidate facts for ingestion.

## Ontology-Guided Approach

ODKE+ dynamically generates ontology snippets tailored to each entity type to align extractions with schema constraints, enabling scalable, type-consistent fact extraction across 195 predicates.

## Performance Metrics

The precision metrics are particularly strong:

- The system supports batch and streaming modes, processing over 9 million Wikipedia pages and ingesting 19 million high-confidence facts with 98.8% precision.
- Weekly audits consistently show over 95% factual accuracy.

## Production Deployment

ODKE+ has been deployed in a production knowledge graph infrastructure since May 2025, running both batch and near-real-time streaming updates. In production, ODKE+ processes an average of 150-250 K new facts per day in streaming mode for high-priority entities, with end-to-end latency under 2 hours for most updates.

The paper was submitted to arXiv on September 4, 2025 (arXiv:2509.04696).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbd08057-7164-45cc-8391-550beaa28e66",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "5bef9dd9-ca39-4ebd-b03b-4ffec7c486ed",
  "sourceToolAssistantUUID": "bbd08057-7164-45cc-8391-550beaa28e66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-12T00:44:01.296Z_

Now let me do a few follow-up searches to get more specific details on some of the papers to check accuracy of specific claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bef9dd9-ca39-4ebd-b03b-4ffec7c486ed",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkNNdpk3ZRktMYAtJCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78576d40-ac4f-4427-b73b-7852b8bd888a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C5nEa3e3dyrbeRF2YpkeWx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2492,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 11795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3117,
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

_source line 23 · 2026-05-12T00:44:02.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ktf5YRxgPGYBwJCRZ4HZm4`</summary>

```json
{
  "query": "IterGen ICLR 2025 venue confirmation grammar semantic callback paradigm"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78576d40-ac4f-4427-b73b-7852b8bd888a",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkNNdpk3ZRktMYAtJCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37e52396-30e6-4941-a46b-c345d6672529",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C5nEa3e3dyrbeRF2YpkeWx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2492,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 11795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3117,
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

_source line 24 · 2026-05-12T00:44:03.042Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NnjUnZkhJMfoTL5KbUVvMf`</summary>

```json
{
  "query": "arXiv 2508.12611 LLM ASP SciERC 35.37 relation extraction F1 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37e52396-30e6-4941-a46b-c345d6672529",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkNNdpk3ZRktMYAtJCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55e9b172-4020-41fe-8808-939e5519709b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C5nEa3e3dyrbeRF2YpkeWx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2492,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 11795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3117,
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

_source line 25 · 2026-05-12T00:44:03.836Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QHYjqpupX645ZKMhFiNy8X`</summary>

```json
{
  "query": "BoostCD BoostIE vocabulary membership constraints information extraction closed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55e9b172-4020-41fe-8808-939e5519709b",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkNNdpk3ZRktMYAtJCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08f16178-e2ff-4375-af99-086283784eb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C5nEa3e3dyrbeRF2YpkeWx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2492,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 11795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3117,
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

_source line 26 · 2026-05-12T00:44:04.532Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NSjn4HP3Dr1pqDsuRSSh2e`</summary>

```json
{
  "query": "\"Format Tax\" arXiv 2604.03616 2026 prompt-level decoder-level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08f16178-e2ff-4375-af99-086283784eb7",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkNNdpk3ZRktMYAtJCE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "419670c9-2986-4536-b7d0-401bb41838b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C5nEa3e3dyrbeRF2YpkeWx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2492,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 11795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3117,
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

_source line 27 · 2026-05-12T00:44:06.817Z_

<details><summary>↩ Tool result · `toolu_01Ktf5YRxgPGYBwJCRZ4HZm4`</summary>

```text
Web search results for query: "IterGen ICLR 2025 venue confirmation grammar semantic callback paradigm"

Links: [{"title":"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking | OpenReview","url":"https://openreview.net/forum?id=ac93gRzxxV"},{"title":"IterGen: Iterative Semantic-aware Structured LLM ...","url":"https://iclr.cc/media/iclr-2025/Slides/29157.pdf"},{"title":"ICLR Poster IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://iclr.cc/virtual/2025/poster/29157"},{"title":"Shubham Ugare","url":"https://shubhamugare.github.io/"},{"title":"[2410.07295] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://arxiv.org/abs/2410.07295"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"itergen: iterative semantic-aware structured llm generation ...","url":"https://www.arxiv.org/pdf/2410.07295"},{"title":"[Quick Review] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://liner.com/review/itergen-iterative-semanticaware-structured-llm-generation-with-backtracking"},{"title":"[PDF] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/8f918a87d0f1bc090fca1dbdfbc4d06a9dc88a66"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"}]

Based on the search results, I can confirm that IterGen is a paper published at ICLR 2025. 

Here are the key details about the paper:

**Venue Confirmation:** IterGen was published at ICLR 2025 as a poster, and it is a 2025 poster.

**Core Concept:** IterGen is a user-friendly library for iterative, grammar-guided LLM generation that enables users to move both forward and backward within the generated output based on grammar symbols.

**Key Features:** By leveraging a symbol-to-position mapping and maintaining the key-value (KV) cache state, IterGen ensures efficient and structured generation while allowing for corrections during the process.

**Applications:** IterGen demonstrates effectiveness in two important applications: reducing privacy leakage in LLM outputs, improving the accuracy of LLM-generated SQL and Vega-Lite queries.

The research addresses the limitation that current libraries for structured LLM generation rely on left-to-right decoding without support for backtracking, limiting the ability to correct or refine outputs mid-generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37e52396-30e6-4941-a46b-c345d6672529",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "b02e1915-a652-443e-93a0-ebb98234235b",
  "sourceToolAssistantUUID": "37e52396-30e6-4941-a46b-c345d6672529",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T00:44:10.073Z_

<details><summary>↩ Tool result · `toolu_01NnjUnZkhJMfoTL5KbUVvMf`</summary>

```text
Web search results for query: "arXiv 2508.12611 LLM ASP SciERC 35.37 relation extraction F1 results"

Links: [{"title":"[2508.12611] An LLM + ASP Workflow for Joint Entity-Relation Extraction","url":"https://arxiv.org/abs/2508.12611"},{"title":"An LLM + ASP Workflow for Joint Entity-Relation Extraction","url":"https://arxiv.org/html/2508.12611v2"},{"title":"LLMs Underperform Graph-Based Parsers on Supervised Relation Extraction for Complex Graphs","url":"https://arxiv.org/html/2604.08752"},{"title":"A Few-Shot Approach for Relation Extraction Domain Adaptation using Large Language Models","url":"https://arxiv.org/html/2408.02377v1"},{"title":"SciER: An Entity and Relation Extraction Dataset for Datasets, Methods, and Tasks in Scientific Documents","url":"https://arxiv.org/html/2410.21155v1"},{"title":"Hallucination-Resistant Relation Extraction via ...","url":"https://arxiv.org/pdf/2508.14391"},{"title":"HyperPIE: Hyperparameter Information Extraction from Scientific Publications","url":"https://arxiv.org/html/2312.10638"},{"title":"Evaluating LLMs for Named Entity Recognition in Scientific ...","url":"https://oro.open.ac.uk/105348/1/105348.pdf"},{"title":"[2305.02105] GPT-RE: In-context Learning for Relation Extraction using Large Language Models","url":"https://ar5iv.labs.arxiv.org/html/2305.02105"},{"title":"LLM-as-classifier: Semi-Supervised, Iterative Framework ...","url":"https://www.semanticscholar.org/paper/75386bcdac0a1d01d857b466e94209ddb89e3103"}]

Based on the web search results, I found detailed information about the arXiv paper 2508.12611.

## Summary

The paper proposes harnessing the capabilities of generative pre-trained large language models (LLMs) and the knowledge representation and reasoning capabilities of Answer Set Programming (ASP) to perform joint entity-relation extraction (JERE).

### SciERC F1 Results

On the SciErc dataset, the GPT+ASP workflow achieves 35.37% F1-macro. More specifically, it is able to achieve a 2.5 times (35% over 15%) improvement in the Relation Extraction task for the SciERC corpus, one of the most difficult benchmarks.

### Key Findings

The results of experiments show that the LLM + ASP workflow is better than state-of-the-art JERE systems in several categories with only 10% of training data. It excels over ASPER by 20% raw score, and the workflow outperforms ITER by more than 25% raw score, with improvement attributed to the ASP consistency checker, which reduces false positives and enhances the quality of entity-relation resolutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55e9b172-4020-41fe-8808-939e5519709b",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "da2f54be-c9ff-48e2-a37c-741f49ba2a22",
  "sourceToolAssistantUUID": "55e9b172-4020-41fe-8808-939e5519709b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-12T00:44:10.098Z_

<details><summary>↩ Tool result · `toolu_01NSjn4HP3Dr1pqDsuRSSh2e`</summary>

```text
Web search results for query: ""Format Tax" arXiv 2604.03616 2026 prompt-level decoder-level"

Links: [{"title":"[2604.03616] The Format Tax","url":"https://arxiv.org/abs/2604.03616"},{"title":"The Format Tax","url":"https://arxiv.org/html/2604.03616"},{"title":"[2604.03616v1] The Format Tax","url":"https://arxiv.org/abs/2604.03616v1"},{"title":"The Format Tax | Trending arXiv papers – Ribbit Ribbit","url":"https://ribbitribbit.co/paper/arxiv.2604.03616-The-Format-Tax"}]

I found the paper! Here's what the search revealed about "The Format Tax" (arXiv 2604.03616):

**Overview:**
The paper is authored by Ivan Yee Lee, Loris D'Antoni, and Taylor Berg-Kirkpatrick from UC San Diego, submitted on April 4, 2026.

**Main Findings:**
The research finds that structured output requirements—JSON, XML, LaTeX, Markdown—substantially degrade reasoning and writing performance across open-weight models.

**Prompt-Level vs. Decoder-Level Analysis:**
This is where your specific query terms come in. The dominant cost enters at the prompt: format-requesting instructions alone cause most of the accuracy loss, before any decoder constraint is applied. While the research response has focused on constrained decoding, sampling bias accounts for only a fraction of the degradation.

**Proposed Solution:**
The diagnosis points to a simple principle: decouple reasoning from formatting, and separating the two concerns substantially recovers lost accuracy—whether by generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation.

**Key Results:**
Across six open-weight models, four API models, four formats, and tasks spanning math, science, logic, and writing, decoupling recovers most lost accuracy. Notably, most recent closed-weight models show little to no format tax.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "419670c9-2986-4536-b7d0-401bb41838b7",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "c86bcdfb-3d4f-4da9-a09d-9b65a6c8bfd2",
  "sourceToolAssistantUUID": "419670c9-2986-4536-b7d0-401bb41838b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T00:44:12.938Z_

<details><summary>↩ Tool result · `toolu_01QHYjqpupX645ZKMhFiNy8X`</summary>

```text
Web search results for query: "BoostCD BoostIE vocabulary membership constraints information extraction closed"

Links: [{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/html/2506.14901"},{"title":"[2506.14901] Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/abs/2506.14901"},{"title":"Combining Constrained and Unconstrained Decoding via ...","url":"https://aclanthology.org/2025.emnlp-main.926.pdf"},{"title":"Marija Sakota's research works | Swiss Federal Institute of Technology in Lausanne and other places","url":"https://www.researchgate.net/scientific-contributions/Marija-Sakota-2168060164"},{"title":"BoostCD and Its Application to Information Extraction","url":"https://openreview.net/pdf?id=3Qbw5Ja6Sc"},{"title":"Vocabulary Booster Volume I - Vocabulary List | Vocabulary.com","url":"https://www.vocabulary.com/lists/175238"},{"title":"EPFL Data Science & AI Lab (dlab) · GitHub","url":"https://github.com/epfl-dlab"},{"title":"Product Update: AI Insights, Universal Candidate Profile Preview & More - Boostie","url":"https://boostie.com/blog/august-product-update-2025/"},{"title":"GitHub - boostcd/boost-ui: Front-end application for the Estafet Boost project build using React","url":"https://github.com/boostcd/boost-ui"},{"title":"Boost · GitHub","url":"https://github.com/boostcd"}]

Based on the search results, here's comprehensive information about BoostCD and BoostIE:

## Overview

BoostCD is a new method for training autoregressive language models for structured NLP tasks. It combines constrained and unconstrained decoding in two phases: Phase 1 decodes from the base model twice in constrained and unconstrained mode, obtaining two weak predictions. In phase 2, a learned autoregressive boosted model combines the two weak predictions into one final prediction.

## The Problem It Solves

During training, approaches using constrained decoding do not require the model to be aware of the constraints, which are merely implicit in the training outputs. This is advantageous as it allows for dynamic constraints without requiring retraining, but can lead to low-quality output during constrained decoding at test time.

## How It Works

BoostCD trains a new model, the boosted model, to predict the ground-truth output based on both the constrained and the unconstrained generation from the autoregressive base model together with the input text. This way of training allows the boosted model to recover from systematic mistakes made by the base model without requiring explicit knowledge of the constraints at training time.

The mistakes made by the base model with vs. without constraints tend to be complementary, which the boosted model learns to exploit for improved performance.

## Application to Information Extraction: BoostIE

BoostCD was applied to closed information extraction (cIE) as an example of a structured task with constraints (defined by the content of the knowledge base) that tend to change dynamically in real-life settings. The resulting cIE model, BoostIE, was further enhanced with Direct Preference Optimization (DPO).

## Performance Results

BoostIE outperforms prior approaches both in and out of distribution, addressing several common errors identified in those approaches. BoostIE outperforms previous methods both in-distribution (on synthetic data it was trained on) and out-of-distribution (on random Wikipedia paragraphs). It also lowers the rate of common errors made by earlier techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08f16178-e2ff-4375-af99-086283784eb7",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "51f3afb2-36f5-45b0-a766-e32a535c28d9",
  "sourceToolAssistantUUID": "08f16178-e2ff-4375-af99-086283784eb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T00:44:17.933Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Cpnbka9a6rud2EZ5GctQe`</summary>

```json
{
  "query": "EnriCo Zaratiana 2024 venue publication EMNLP ACL published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51f3afb2-36f5-45b0-a766-e32a535c28d9",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkPffXspz92MiZ3YZKt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae2d3cb0-5e70-4037-8b87-b3d8c87f78e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KHUWQCp6qCYLbhtFyDhRkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 533,
      "cache_creation_input_tokens": 5318,
      "cache_read_input_tokens": 14912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5318,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-12T00:44:18.857Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MmbrMxjwejwB1tjMuPNKqd`</summary>

```json
{
  "query": "Synchromesh Poesia 2022 ICLR constrained semantic decoding syntactic semantic constraints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae2d3cb0-5e70-4037-8b87-b3d8c87f78e8",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkPffXspz92MiZ3YZKt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ccb3506-c900-45cd-b7b1-b5eaebc23fba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KHUWQCp6qCYLbhtFyDhRkV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 533,
      "cache_creation_input_tokens": 5318,
      "cache_read_input_tokens": 14912,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5318
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 533,
          "output_tokens": 132,
          "cache_read_input_tokens": 14912,
          "cache_creation_input_tokens": 5318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5318,
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

_source line 33 · 2026-05-12T00:44:24.997Z_

<details><summary>↩ Tool result · `toolu_011Cpnbka9a6rud2EZ5GctQe`</summary>

```text
Web search results for query: "EnriCo Zaratiana 2024 venue publication EMNLP ACL published"

Links: [{"title":"Urchade Zaratiana","url":"https://urchade.github.io/"},{"title":"dblp: Urchade Zaratiana","url":"https://dblp.org/pid/304/2028.html"},{"title":"Urchade Zaratiana - ACL Anthology","url":"https://aclanthology.org/people/u/urchade-zaratiana/"},{"title":"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.300/"},{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - EMNLP 2024","url":"https://2024.emnlp.org/"},{"title":"Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/venues/emnlp/"},{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2024/"},{"title":"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/volumes/2024.emnlp-main/"},{"title":"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track - ACL Anthology","url":"https://aclanthology.org/volumes/2024.emnlp-industry/"},{"title":"Transactions of the Association for Computational Linguistics","url":"https://transacl.org/"}]

Based on the search results, I found information about Urchade Zaratiana's 2024 publications:

EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction was published as a CoRR arXiv paper (abs/2404.12493) in 2024.

Additionally, Zaratiana published "GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer" in 2024 in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (which is NAACL, not EMNLP or ACL).

The search results also show that an autoregressive text-to-graph framework for joint entity and relation extraction was published at AAAI 2024.

However, I did not find a specific 2024 publication by Zaratiana at EMNLP or in the main ACL conference in the search results provided.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae2d3cb0-5e70-4037-8b87-b3d8c87f78e8",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "a694768c-4738-40f7-9c14-5a3d20fd64fc",
  "sourceToolAssistantUUID": "ae2d3cb0-5e70-4037-8b87-b3d8c87f78e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T00:44:25.993Z_

<details><summary>↩ Tool result · `toolu_01MmbrMxjwejwB1tjMuPNKqd`</summary>

```text
Web search results for query: "Synchromesh Poesia 2022 ICLR constrained semantic decoding syntactic semantic constraints"

Links: [{"title":"[PDF] Synchromesh: Reliable code generation from pre-trained language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Synchromesh:-Reliable-code-generation-from-language-Poesia-Polozov/b62d63580b81a2cbb20c3c1593dd62d118e4cb07"},{"title":"Published as a conference paper at ICLR 2022","url":"https://www.vuminhle.com/pdf/iclr22.pdf"},{"title":"[Quick Review] Synchromesh: Reliable code generation from pre-trained language models","url":"https://liner.com/review/synchromesh-reliable-code-generation-from-pretrained-language-models"},{"title":"SYNTACTIC AND SEMANTIC CONTROL OF LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf"},{"title":"Synchromesh: Reliable code generation from pre-trained language models · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/poesia2022synchromesh/"},{"title":"[2201.11227] Synchromesh: Reliable code generation from pre-trained language models","url":"https://arxiv.org/abs/2201.11227"},{"title":"GitHub - kanishkg/synchromesh: Get language models to generate responses in a specific format reliably. Open source implementation of Synchromesh: Reliable code generation from pre-trained language models.","url":"https://github.com/kanishkg/synchromesh"},{"title":"TreeCoder: Systematic Exploration and Optimisation of Decoding and Constraints for LLM Code Generation","url":"https://arxiv.org/html/2511.22277"},{"title":"[2201.11227v1] Synchromesh: Reliable code generation from pre-trained language models","url":"https://arxiv.org/abs/2201.11227v1"},{"title":"SYNCHROMESH: RELIABLE CODE GENERATION FROM PRE-TRAINED LANGUAGE MODELS","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2022/01/csd_arxiv.pdf"}]

Based on the search results, here's information about Synchromesh and its approach to constrained semantic decoding:

## Overview

Synchromesh is a framework for substantially improving the reliability of pre-trained models for code generation. This ICLR 2022 paper proposes SYNCHROMESH, a framework enhancing code generation reliability using semantic decoding and tuning.

## Core Components

Synchromesh comprises two components: it retrieves few-shot examples from a training bank using Target Similarity Tuning (TST), a novel method for semantic example selection, then feeds the examples to a pre-trained language model and samples programs using Constrained Semantic Decoding (CSD), a general framework for constraining the output to a set of valid programs in the target language.

## Constrained Semantic Decoding (CSD)

The method generates programs with Constrained Semantic Decoding (CSD), a novel method for enforcing rich syntactic and semantic constraints during code generation on top of a frozen language model. The CEs (Completion Engines) are implemented in two layers: a context-free layer, which enforces syntactic validity, and a context-sensitive layer, which encodes semantic constraints that depend on language semantics and the user's context (e.g., the database).

## Evaluation Domains

The methods were evaluated by synthesizing code from natural language descriptions using GPT-3 and Codex in three real-world languages: SQL queries, Vega-Lite visualizations and SMCalFlow programs, which showcase rich constraints that CSD is able to enforce, including syntax, scope, typing rules, and contextual logic.

## Performance

Substantial complementary gains were observed from CSD and TST in prediction accuracy and in effectively preventing run-time errors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ccb3506-c900-45cd-b7b1-b5eaebc23fba",
  "isSidechain": true,
  "promptId": "164edafb-b1e2-4eda-bd1c-eb4caf68892e",
  "agentId": "a668acc4d944c984b",
  "type": "user",
  "uuid": "f25e4c07-7e0c-48d4-b43f-3678294dbf87",
  "sourceToolAssistantUUID": "2ccb3506-c900-45cd-b7b1-b5eaebc23fba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-12T00:45:25.229Z_

I now have enough information to provide a thorough verification report. Here are my findings:

---

## Verification Report: ML Research Proposal Claims

---

### 1. IterGen (ICLR 2025, Ugare) — grammar+semantic callback paradigm with backtracking

**Exists: YES. Claims are largely accurate, with one nuance.**

- Venue/Year: ICLR 2025 poster (arXiv:2410.07295). Confirmed via iclr.cc and OpenReview.
- Authors: Shubham Ugare et al.
- The paper does introduce iterative, grammar-guided LLM generation with backtracking — users can move forward and backward in generated output based on grammar symbols, using symbol-to-position mapping and KV cache maintenance.
- The "grammar + semantic callback" framing is accurate in spirit — IterGen supports semantic constraints alongside grammar constraints.
- One issue: the first search result summary incorrectly said "ICML 2025" — confirmed by iclr.cc poster page it is ICLR 2025.
- Key results: 18.5% mean improvement over prior grammar-guided methods; reduces privacy leaks from 51.4% to 0%.

---

### 2. Synchromesh (ICLR 2022, Poesia) — foundational work combining syntactic+semantic constraints

**Exists: YES. Claims are accurate.**

- Venue/Year: ICLR 2022 (arXiv:2201.11227). Confirmed by multiple sources including the conference paper PDF.
- Authors: Giovanni Poesia, Alex Polozov, et al. (Microsoft Research).
- The "foundational" characterization is well-supported: Synchromesh introduced Constrained Semantic Decoding (CSD) — a two-layer approach with a context-free layer for syntactic validity and a context-sensitive layer for semantic constraints (scope, typing, contextual logic). This is exactly the syntactic+semantic constraint combination the proposal attributes to it.
- Evaluated on SQL, Vega-Lite, SMCalFlow using GPT-3/Codex.
- No significant inaccuracies found in the proposal's characterization.

---

### 3. LLM+ASP Workflow (Tran, arXiv 2508.12611) — post-hoc type constraint checking, SciERC 35.37% RE F1 with 10% training data

**Exists: YES. Claims are accurate.**

- Venue: arXiv preprint, described as ICLP 2025 — the proposal's "ICLP 2025" attribution needs verification (the paper exists on arXiv; the ICLP venue claim is plausible but not definitively confirmed in search results).
- Authors: Trang Tran, Trung Hoang Le, Huiping Cao, Tran Cao Son (New Mexico State University).
- The 35.37% RE F1-macro on SciERC with 10% training data is confirmed by the arXiv HTML page.
- The "2.5 times improvement" (35% over 15%) vs baselines is confirmed.
- The description as "post-hoc type constraint checking" is essentially accurate — ASP is used as a consistency/type checker that reduces false positives rather than as an in-decoding constraint.
- The paper does use type specifications from an ontology to enforce validity.

---

### 4. BoostCD / BoostIE (EMNLP 2025) — limited to vocabulary membership constraints

**Exists: YES. The "limited to vocabulary membership" characterization is partially misleading.**

- Venue/Year: EMNLP 2025 main conference (ACL Anthology: 2025.emnlp-main.926; arXiv:2506.14901).
- The paper introduces BoostCD (combining constrained and unconstrained decoding via boosting) and applies it as BoostIE for closed information extraction (cIE).
- The constraints in the cIE setting are defined by knowledge base entity membership — which could be described as "vocabulary membership" constraints. However, the paper's approach is more general: it is designed to handle dynamically changing constraints without retraining. The proposal's characterization that BoostCD is "limited to vocabulary membership constraints" is technically accurate for the application demonstrated, but may be overly narrow — the framework is presented as applicable to any structured task with constraints.
- BoostIE outperforms prior methods both in-distribution and out-of-distribution.

---

### 5. ODKE+ (Apple, arXiv:2509.04696) — 98.8% precision claim

**Exists: YES. The 98.8% precision claim is accurate.**

- Venue: arXiv preprint submitted September 4, 2025 (arXiv:2509.04696). Also published on Apple Machine Learning Research.
- Authors: Apple researchers.
- The 98.8% precision figure is confirmed: the system processes 9M+ Wikipedia pages, ingests 19M high-confidence facts at 98.8% precision. Weekly audits also show >95% factual accuracy.
- The system supports 195 predicates, uses ontology-guided prompting + pattern-based rules + LLM-based grounding.
- Production-deployed since May 2025 in streaming mode.
- No inaccuracies in the proposal's claims about this paper.

---

### 6. "The Format Tax" (2026) — prompt-level vs. decoder-level accuracy drops

**Exists: YES. Claims are accurate.**

- Venue: arXiv preprint, submitted April 4, 2026 (arXiv:2604.03616).
- Authors: Ivan Yee Lee, Loris D'Antoni, Taylor Berg-Kirkpatrick (UC San Diego).
- The central finding matches the proposal's claim: structured output requirements (JSON, XML, LaTeX, Markdown) substantially degrade performance, and crucially, the dominant cost enters at the prompt level (format-requesting instructions alone cause most accuracy loss), not at the decoder level. Constrained decoding's contribution is described as only "a fraction" of the degradation.
- The solution — decoupling reasoning from formatting (two-pass or extended thinking) — recovers most accuracy.
- Recent closed-weight models show near-zero degradation.
- No significant inaccuracies in the proposal's characterization.

---

### 7. CRANE (ICML 2025, Banerjee) — TC0 complexity result

**Exists: YES. Claims are accurate.**

- Venue/Year: ICML 2025 poster (arXiv:2502.09061). Confirmed via icml.cc poster page.
- Authors: Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, Gagandeep Singh.
- The TC0 complexity result is confirmed: Proposition 3.1 formally shows that LLMs constrained to restrictive grammars (only syntactically valid final answers) can only solve problems within the TC0 complexity class (constant-depth threshold circuits). This is the key theoretical result the proposal references.
- CRANE's solution: augment grammars to allow reasoning steps, alternating between unconstrained generation (for reasoning) and constrained generation (for structured output).
- No inaccuracies found.

---

### 8. EnriCo (Zaratiana, ASP for entity-relation extraction, 2024)

**Exists: YES. Venue characterization needs a caveat.**

- The paper exists: arXiv:2404.12493, submitted April 2024.
- Authors: Urchade Zaratiana, Nadi Tomeh, Yann Dauxais, Pierre Holat, Thierry Charnois.
- The paper does combine enriched neural representations with ASP-based global constraint inference for joint entity and relation extraction.
- Venue concern: Based on search results, EnriCo appears to be an arXiv preprint with no confirmed publication at a major venue (no ACL Anthology entry found for this specific paper). Zaratiana's other 2024 work (GLiNER) appeared at NAACL 2024, and his ATG paper at AAAI 2024 — but EnriCo itself appears to remain a preprint as of available records. The proposal should not imply it was accepted at a named venue without verification.
- The core claims about ASP usage for global constraint solving are accurate.

---

## Summary Table

| Paper | Exists | Venue/Year Accurate | Key Claims Accurate | Issues |
|---|---|---|---|---|
| IterGen (Ugare) | YES | ICLR 2025 — correct | Yes | None material |
| Synchromesh (Poesia) | YES | ICLR 2022 — correct | Yes | None |
| LLM+ASP / arXiv 2508.12611 (Tran) | YES | ICLP 2025 — plausible, confirm needed | Yes (35.37% confirmed) | Venue not definitively confirmed |
| BoostCD/BoostIE | YES | EMNLP 2025 — correct | Partially — "vocabulary membership" is narrow but accurate for cIE demo | Framework is more general than described |
| ODKE+ (Apple) | YES | arXiv Sep 2025 — correct | Yes (98.8% confirmed) | None |
| The Format Tax | YES | arXiv Apr 2026 — correct | Yes (prompt > decoder cost confirmed) | None |
| CRANE (Banerjee) | YES | ICML 2025 — correct | Yes (TC0 confirmed) | None |
| EnriCo (Zaratiana) | YES | 2024 arXiv — likely preprint only | Yes (ASP + NER/RE accurate) | No confirmed major venue publication found |

Sources:
- [IterGen: ICLR 2025 Poster](https://iclr.cc/virtual/2025/poster/29157)
- [IterGen arXiv:2410.07295](https://arxiv.org/abs/2410.07295)
- [IterGen OpenReview](https://openreview.net/forum?id=ac93gRzxxV)
- [Synchromesh ICLR 2022 PDF](https://www.vuminhle.com/pdf/iclr22.pdf)
- [Synchromesh arXiv:2201.11227](https://arxiv.org/abs/2201.11227)
- [Synchromesh OpenReview](https://openreview.net/forum?id=KmtVD97J43e)
- [LLM+ASP arXiv:2508.12611](https://arxiv.org/abs/2508.12611)
- [LLM+ASP HTML full text](https://arxiv.org/html/2508.12611v2)
- [BoostCD arXiv:2506.14901](https://arxiv.org/abs/2506.14901)
- [BoostCD EMNLP 2025 ACL Anthology](https://aclanthology.org/2025.emnlp-main.926.pdf)
- [ODKE+ arXiv:2509.04696](https://arxiv.org/abs/2509.04696)
- [ODKE+ Apple ML Research](https://machinelearning.apple.com/research/odke)
- [The Format Tax arXiv:2604.03616](https://arxiv.org/abs/2604.03616)
- [CRANE arXiv:2502.09061](https://arxiv.org/abs/2502.09061)
- [CRANE ICML 2025 Poster](https://icml.cc/virtual/2025/poster/43624)
- [EnriCo arXiv:2404.12493](https://arxiv.org/abs/2404.12493)
- [EnriCo GitHub](https://github.com/urchade/EnriCo)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f25e4c07-7e0c-48d4-b43f-3678294dbf87",
  "isSidechain": true,
  "agentId": "a668acc4d944c984b",
  "requestId": "req_011CawkQdU6utzqhopCn9Ku1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2ac446b-da68-45d3-aae3-c9c3cd2dd02f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "97a2a3da-40b6-46b0-ac5f-f9da9f7da22d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Rr1VjGAgKRkbcZH5uvkUCX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2447,
      "cache_read_input_tokens": 20230,
      "output_tokens": 2920,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2920,
          "cache_read_input_tokens": 20230,
          "cache_creation_input_tokens": 2447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2447,
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
