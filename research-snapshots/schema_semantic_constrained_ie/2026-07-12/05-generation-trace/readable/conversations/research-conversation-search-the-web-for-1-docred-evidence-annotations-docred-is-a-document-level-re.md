# Research conversation: Search the web for: 1. DocRED evidence annotations: DocRED is a document-level relation extraction dataset. Verify that 

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 98
- **Recorded user turns:** 1
- **Tool calls:** 43
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab6fbd4eb426f749b.jsonl`
- **Structured JSON:** [`ddc2c9919bb497a792ce.json`](../../sessions/dd/ddc2c9919bb497a792ce.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

98 recorded events

### User

_source line 1 · 2026-05-11T23:01:12.750Z_

Search the web for:

1. DocRED evidence annotations: DocRED is a document-level relation extraction dataset. Verify that it includes "supporting evidence sentences" for each relation instance. Search for recent work (2025-2026) on evidence-guided document-level relation extraction.

2. Current SOTA on ACE05, SciERC, and DocRED benchmarks (2025-2026). Search:
   - "ACE05 state of the art 2025 2026 NER RE event extraction"
   - "SciERC state of the art 2025 2026"
   - "DocRED state of the art 2025 2026"
   - site:paperswithcode.com ACE05, SciERC, DocRED

3. Search for any work combining attribution/provenance with structured information extraction:
   - "attribution information extraction structured"
   - "evidence span prediction relation extraction 2025 2026"
   - "grounded extraction NER 2025 2026"

Use WebSearch and WebFetch. Report exact numbers and paper titles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "4b3a65f7-a146-4b87-af9d-c6f403b8d53f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:01:12.755Z_

```json
{
  "parentUuid": "4b3a65f7-a146-4b87-af9d-c6f403b8d53f",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
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
  "uuid": "c91d7dac-7746-4683-b47d-c5466e938204",
  "timestamp": "2026-05-11T23:01:12.755Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:01:15.749Z_



I'll start by loading the WebSearch and WebFetch tools, then conduct the searches systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c91d7dac-7746-4683-b47d-c5466e938204",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcY6gyPxQyEiSqofcWV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ca45da2-9535-4d81-84c4-f3a93e093b40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LKyE3sPwBTQHEjjGdhubKe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 772,
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

_source line 4 · 2026-05-11T23:01:16.049Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YMBRFGwfpGKgaDBQKGfb3N`</summary>

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
  "parentUuid": "6ca45da2-9535-4d81-84c4-f3a93e093b40",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcY6gyPxQyEiSqofcWV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37b8e3b5-5c6c-4369-9bfa-8de5c38eb972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LKyE3sPwBTQHEjjGdhubKe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 7304,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 772
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 772,
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

_source line 5 · 2026-05-11T23:01:16.051Z_

<details><summary>↩ Tool result · `toolu_01YMBRFGwfpGKgaDBQKGfb3N`</summary>

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
  "parentUuid": "37b8e3b5-5c6c-4369-9bfa-8de5c38eb972",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "57555c0e-d941-4af3-a33c-89f2f35bc5dc",
  "sourceToolAssistantUUID": "37b8e3b5-5c6c-4369-9bfa-8de5c38eb972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:01:18.481Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57555c0e-d941-4af3-a33c-89f2f35bc5dc",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcYLzCLr6SvU3CKyZSJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abab4736-4461-412b-b782-75bdbd0ea68d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArKXFGRbZ92tHYn3zgfaFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8076,
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

_source line 7 · 2026-05-11T23:01:18.972Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Spzu5rYRJ4oC2jwtLrNTGx`</summary>

```json
{
  "query": "DocRED dataset supporting evidence sentences relation extraction annotations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abab4736-4461-412b-b782-75bdbd0ea68d",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcYLzCLr6SvU3CKyZSJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4f847f9-2797-4099-896d-3c70eba4414b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArKXFGRbZ92tHYn3zgfaFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8076,
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

_source line 8 · 2026-05-11T23:01:19.907Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TwrxoaRJsJxXRn2CBg692L`</summary>

```json
{
  "query": "evidence-guided document-level relation extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4f847f9-2797-4099-896d-3c70eba4414b",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcYLzCLr6SvU3CKyZSJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16f5cdf8-61f3-4b31-95e2-f40b9e4e8d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArKXFGRbZ92tHYn3zgfaFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8076,
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

_source line 9 · 2026-05-11T23:01:20.847Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BHszdPDZBR7esvXdeaxDrf`</summary>

```json
{
  "query": "ACE05 state of the art 2025 2026 NER RE event extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16f5cdf8-61f3-4b31-95e2-f40b9e4e8d9e",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcYLzCLr6SvU3CKyZSJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36415ff5-688d-430f-ad28-6bdd7fc05212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArKXFGRbZ92tHYn3zgfaFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8076,
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

_source line 10 · 2026-05-11T23:01:21.371Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011uHGprXqsPv5WG3HJtpViJ`</summary>

```json
{
  "query": "SciERC state of the art 2025 2026 relation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36415ff5-688d-430f-ad28-6bdd7fc05212",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcYLzCLr6SvU3CKyZSJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7282b815-0c3a-42ff-9c3d-357f956044c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArKXFGRbZ92tHYn3zgfaFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8076,
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

_source line 11 · 2026-05-11T23:01:21.786Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0128kqhnjYsEkgWYKoML44AD`</summary>

```json
{
  "query": "DocRED state of the art 2025 2026 F1 score"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7282b815-0c3a-42ff-9c3d-357f956044c7",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcYLzCLr6SvU3CKyZSJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e97c983-65dd-4eb3-bc37-9aa4785eaa37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArKXFGRbZ92tHYn3zgfaFG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8076,
      "output_tokens": 278,
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
          "output_tokens": 278,
          "cache_read_input_tokens": 8076,
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

_source line 12 · 2026-05-11T23:01:26.034Z_

<details><summary>↩ Tool result · `toolu_01TwrxoaRJsJxXRn2CBg692L`</summary>

```text
Web search results for query: "evidence-guided document-level relation extraction 2025 2026"

Links: [{"title":"Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3511808.3557313"},{"title":"Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-026-12099-8"},{"title":"[PDF] Entity and Evidence Guided Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Document-Level-Relation-Huang-Qi/e4179bf0963012f9f13ce0ca61d3cdd12a87b336"},{"title":"Toward Better Document-Level Relation Extraction: De-sampling and Mixture of Experts in Action | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-04549-2_12"},{"title":"Document-level relation extraction model guided by global information and external contextual knowledge | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-07467-5"},{"title":"Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"},{"title":"Evidence Reasoning and Curriculum Learning for Document-Level Relation Extraction | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10174655/"},{"title":"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning | OpenReview","url":"https://openreview.net/forum?id=SVl9tIADWV"},{"title":"Three-stage document-level entity relation extraction | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-07068-2"},{"title":"Evidence and Axial Attention Guided Document-level Relation Extraction | Computer Speech and Language","url":"https://dl.acm.org/doi/10.1016/j.csl.2024.101728"}]

Based on the search results, here's what I found regarding evidence-guided document-level relation extraction in 2025-2026:

## Recent Research and Developments

Document-level Relation Extraction (DocRE) aims to extract semantic relations between entity pairs, spanning multiple sentences, paragraphs or even the entire document.

### Key 2025-2026 Publications

In 2025, Yuan et al. published "Evidence and Axial Attention Guided Document-level Relation Extraction" in Computer Speech and Language, and Mao et al. (2025) presented "GEGA: Graph convolutional networks and evidence retrieval guided attention for enhanced document-level relation extraction."

Tran et al. (2025) introduced "VaeDiff-DocRE: End-to-end data augmentation framework for document-level relation extraction" at the 31st International Conference on Computational Linguistics in Abu Dhabi.

### Evidence-Guided Approaches

Huang et al. proposed an entity and evidence-guided RE framework that focuses the model on the relevant regions of the document, helping the model direct its attention towards the sections of the document that hold greater relevance to the head entity.

Zhang et al. published "Dual reasoning enhanced document-level relation extraction" in Neural Computing and Applications in 2026.

These recent publications demonstrate an active research area focusing on incorporating evidence and attention mechanisms to improve document-level relation extraction performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16f5cdf8-61f3-4b31-95e2-f40b9e4e8d9e",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "ba3c5c09-47cf-4514-9195-2aed273c9e92",
  "sourceToolAssistantUUID": "16f5cdf8-61f3-4b31-95e2-f40b9e4e8d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-11T23:01:26.981Z_

<details><summary>↩ Tool result · `toolu_01Spzu5rYRJ4oC2jwtLrNTGx`</summary>

```text
Web search results for query: "DocRED dataset supporting evidence sentences relation extraction annotations"

Links: [{"title":"GitHub - thunlp/DocRED: Dataset and codes for ACL 2019 DocRED: A Large-Scale Document-Level Relation Extraction Dataset. · GitHub","url":"https://github.com/thunlp/DocRED"},{"title":"thunlp/docred · Datasets at Hugging Face","url":"https://huggingface.co/datasets/thunlp/docred"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"},{"title":"(PDF) DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://www.researchgate.net/publication/333815327_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/abs/1906.06127"},{"title":"A Large-Scale Document-Level Relation Extraction Dataset","url":"https://aclanthology.org/P19-1074.pdf"},{"title":"[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://ar5iv.labs.arxiv.org/html/1906.06127"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"docred · Datasets at Hugging Face","url":"https://huggingface.co/datasets/docred"},{"title":"[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"}]

Based on the search results, here's information about the DocRED dataset's supporting evidence sentences and relation extraction annotations:

## Overview

DocRED is a large-scale human-annotated dataset for document-level relation extraction from plain text constructed from Wikipedia and Wikidata.

## Annotation Components

Each document in DocRED is annotated with named entity mentions, coreference information, intra- and inter-sentence relations, and supporting evidence. DocRED consists of human-annotated triplets (head entity, relation, tail entity)—for example, (Albert Einstein, educated at, University of Zurich).

## Supporting Evidence

To facilitate more RE settings, supporting evidence information is provided for relation instances. The dataset includes specific annotations for which sentences serve as evidence for each relation. According to the data structure, each relation annotation includes an "evidence" field that lists the sentence indices that support that relation.

## Dataset Characteristics

DocRED requires reading multiple sentences in a document to extract entities and infer their relations by synthesizing all information of the document. The dataset includes 97 relation types, with approximately 40.7% of relational facts requiring extraction from multiple sentences.

The dataset also offers large-scale distantly supervised data, which enables DocRED to be adopted for both supervised and weakly supervised scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4f847f9-2797-4099-896d-3c70eba4414b",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "f21c6cf5-74de-47d4-a7d1-a6f5dd5b0b5c",
  "sourceToolAssistantUUID": "f4f847f9-2797-4099-896d-3c70eba4414b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T23:01:27.416Z_

<details><summary>↩ Tool result · `toolu_01BHszdPDZBR7esvXdeaxDrf`</summary>

```text
Web search results for query: "ACE05 state of the art 2025 2026 NER RE event extraction"

Links: [{"title":"[2210.12720] Span-based joint entity and relation extraction augmented with sequence tagging mechanism","url":"https://ar5iv.labs.arxiv.org/html/2210.12720"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"},{"title":"GitHub - michaelmoju/ace05_ERE: Entity/Relation/Event extraction on ACE 2005 corpus","url":"https://github.com/michaelmoju/ace05_ERE"},{"title":"GitHub - jeremytanjianle/event-extraction-oneie: Event extraction of ACE05 dataset","url":"https://github.com/jeremytanjianle/event-extraction-oneie"},{"title":"ACE 2005 Multilingual Training Corpus - Linguistic Data Consortium","url":"https://catalog.ldc.upenn.edu/LDC2006T06"},{"title":"Event extraction results on ACE05 dataset and ERE dataset (F-score, %). | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Event-extraction-results-on-ACE05-dataset-and-ERE-dataset-F-score_tbl1_355234254"},{"title":"[PDF] The ACE 2005 ( ACE 05 ) Evaluation Plan Evaluation of the Detection and Recognition of ACE Entities , Values , Temporal Expressions , Relations , and Events 1 | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-ACE-2005-(-ACE-05-)-Evaluation-Plan-Evaluation-Ntroduction/3a9b136ca1ab91592df36f148ef16095f74d009e"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"GitHub - nlpcl-lab/ace2005-preprocessing: ACE 2005 corpus preprocessing for Event Extraction task · GitHub","url":"https://github.com/nlpcl-lab/ace2005-preprocessing"},{"title":"Span-based joint entity and relation extraction augmented with ...","url":"https://www.sciengine.com/parse/pdf/1674-733X/67BEF209E86040EA858E546B3960D818.pdf?attname=67BEF209E86040EA858E546B3960D818.pdf"}]

Based on the search results, here's what I found regarding ACE05 state of the art for NER, RE (Relation Extraction), and Event Extraction:

## Recent State-of-the-Art Approaches

### For NER and RE on ACE05:

A span-based model with sequence tagging mechanism (STSN) obtained +0.7%, +1.9%, and +1.1% F1 gains on NER, RE, and RE+ respectively compared to the strongest baselines on ACE05. The UNIRE model, based on BERT-base-uncased, ALBERT, and SciBERT encoding, achieves state-of-the-art performance on the ACE04 and ACE05 datasets.

### For Event Extraction on ACE05:

Wang et al. proposed DAO (Debate as Optimization), a multi-agent system that refines LLM event extraction outputs through debate without tuning, significantly narrowing the gap between tuning-free and supervised methods on ACE05 and CASIE.

## General Trends (2025):

BERT-based methods dominate in achieving state-of-the-art results for relation extraction, while emerging Large Language Models like T5 show promise in few-shot relation extraction scenarios.

The search results provide references from 2024-2025, indicating these are recent developments in the field. If you need more specific information about particular models or approaches, I can search for additional details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36415ff5-688d-430f-ad28-6bdd7fc05212",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "1ed4031b-98dc-4822-a60e-ca0dc53e3388",
  "sourceToolAssistantUUID": "36415ff5-688d-430f-ad28-6bdd7fc05212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T23:01:28.795Z_

<details><summary>↩ Tool result · `toolu_011uHGprXqsPv5WG3HJtpViJ`</summary>

```text
Web search results for query: "SciERC state of the art 2025 2026 relation extraction"

Links: [{"title":"SciER: An Entity and Relation Extraction Dataset for Datasets, Methods, and Tasks in Scientific Documents","url":"https://arxiv.org/html/2410.21155v1"},{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys","url":"https://dl.acm.org/doi/full/10.1145/3674501"},{"title":"SciIE: Scientific Information Extractor","url":"https://www.emergentmind.com/topics/scientific-information-extractor-sciie"},{"title":"Information Extraction from Multi-Domain Scientific Documents: Methods and Insights","url":"https://www.mdpi.com/2076-3417/15/16/9086"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"[2410.21155] SciER: An Entity and Relation Extraction Dataset for Datasets, Methods, and Tasks in Scientific Documents","url":"https://arxiv.org/abs/2410.21155"},{"title":"A Joint Entity and Relation Extraction Model based on Efficient Sampling and Explicit Interaction | ACM Transactions on Intelligent Systems and Technology","url":"https://dl.acm.org/doi/10.1145/3604811"},{"title":"SciNLP: A Domain-Specific Benchmark for Full-Text Scientific Entity and Relation Extraction in NLP","url":"https://arxiv.org/html/2509.07801"},{"title":"FSN: Joint Entity and Relation Extraction Based on Filter Separator Network - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10887558/"},{"title":"LLMs Underperform Graph-Based Parsers on Supervised Relation Extraction for Complex Graphs","url":"https://arxiv.org/html/2604.08752"}]

Based on the search results, here's what I found about the state of the art in SciERC relation extraction for 2025-2026:

## Current State-of-the-Art Models

Span-based models such as PURE (pipeline) and HGERE (joint, hypergraph-based) achieve state-of-the-art, with SciBERT as the backbone encoder. On SciER, HGERE attains NER F1 = 86.85% and relation (Rel+) F1 = 61.10% (in-domain), with moderate drops on OOD (NER = 81.32%, Rel+ = 58.32%).

## Recent Developments

A new domain-specific benchmark called SciNLP defines four entity types (Task, Method, Dataset, Metric) and 11 relation types (MeasuredBy, UsedFor, TrainedWith, EnhancedBy, SubclassOf, SubtaskOf, PartOf, EvaluatedBy, EvaluatedOn, SimilarWith, CompareWith), and is constructed from 60 ACL conference papers spanning 2001–2024, containing 6,409 entities and 1,648 relations.

## LLM vs. Traditional Models

Recent research has compared LLMs with traditional graph-based approaches. Overall, the much lighter graph-based parser outperforms all LLMs on the complex graphs comprising enEWT, SciDTB, and ERFGC, while the LLMs match its performance on CoNLL04 and surpass it on ADE and SciERC.

## Document-Level Improvements

The PL-Marker model achieves a 17.62 point improvement on the strict relation classification (Rel+) task compared to the cross-disciplinary SciERC dataset when trained on the new full-text SciNLP dataset, highlighting the benefits of document-level context over abstract-only datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7282b815-0c3a-42ff-9c3d-357f956044c7",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "934035c5-d8b3-4d06-aff5-e813885735cb",
  "sourceToolAssistantUUID": "7282b815-0c3a-42ff-9c3d-357f956044c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T23:01:37.468Z_

<details><summary>↩ Tool result · `toolu_0128kqhnjYsEkgWYKoML44AD`</summary>

```text
Web search results for query: "DocRED state of the art 2025 2026 F1 score"

Links: [{"title":"F1 standings 2026 - Formula 1 points","url":"https://www.formula1points.com/season"},{"title":"How different do the Teams’ Championship standings look after the first four rounds?","url":"https://www.formula1.com/en/latest/article/how-different-do-the-teams-championship-standings-look-after-the-first-four-rounds.2krqaNWKbdCIDXD4CWqead"},{"title":"2025 - Formula 1 F1 Standings - ESPN","url":"https://www.espn.com/racing/standings/_/series/f1/year/2025"},{"title":"2026 • STATS F1","url":"https://www.statsf1.com/en/2026.aspx"},{"title":"best f1 stats website for F1 Standings 2025 | Racing Statistics","url":"https://www.racingstatisticsf1.com/f1-standings-2025"},{"title":"F1 driver standings 2026 | RacingNews365","url":"https://racingnews365.com/f1/standings/2026/drivers"},{"title":"STATS F1","url":"https://www.statsf1.com/"},{"title":"F1 - The Official Home of Formula 1® Racing","url":"https://www.formula1.com/en/results/2026/drivers"},{"title":"2025 • STATS F1","url":"https://www.statsf1.com/en/2025.aspx"},{"title":"GLiM: Integrating Graph Transformer and LLM for ...","url":"https://aclanthology.org/2025.findings-acl.727.pdf"}]

I see that the search results are returning Formula 1 racing results instead of information about DocRED, which is a machine learning/NLP dataset. Let me search more specifically for the DocRED dataset benchmark results.

Links: [{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"(PDF) DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://www.researchgate.net/publication/333815327_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"Document-Level Zero-Shot Relation Extraction with Entity Side Information","url":"https://arxiv.org/html/2601.07271"},{"title":"GitHub - zjunlp/DocuNet: [IJCAI 2021] Document-level Relation Extraction as Semantic Segmentation · GitHub","url":"https://github.com/zjunlp/DocuNet"},{"title":"Revisiting DocRED - Addressing the False Negative Problem in Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.580/"},{"title":"[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://ar5iv.labs.arxiv.org/html/1906.06127"},{"title":"[2205.12696] Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/abs/2205.12696"},{"title":"(PDF) Revisiting DocRED -- Addressing the Overlooked False Negative Problem in Relation Extraction","url":"https://www.researchgate.net/publication/360859401_Revisiting_DocRED_--_Addressing_the_Overlooked_False_Negative_Problem_in_Relation_Extraction"},{"title":"Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/html/2205.12696"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"}]

Let me search for more recent state-of-the-art results on DocRED from 2025-2026.

Links: [{"title":"DocRED Benchmark (Relation Extraction)","url":"https://paperswithcode.com/sota/relation-extraction-on-docred"},{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"GitHub - BurgerBurgerBurger/AA: Code for EMNLP 2023 paper \"Anaphor Assisted Document-Level Relation Extraction\"","url":"https://github.com/BurgerBurgerBurger/AA"},{"title":"[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283"},{"title":"DocRED","url":"https://competitions.codalab.org/competitions/20717"},{"title":"Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.132/"},{"title":"Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/html/2205.12696"},{"title":"tonytan48/Re-DocRED · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tonytan48/Re-DocRED"},{"title":"thunlp/docred · Datasets at Hugging Face","url":"https://huggingface.co/datasets/thunlp/docred"},{"title":"[2203.10900] Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation","url":"https://arxiv.org/abs/2203.10900"}]

Let me search for the most recent papers and benchmarks on DocRED from 2025-2026.

Links: [{"title":"[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"}]

Let me do one more search to find the most recent specific F1 scores from 2025-2026.

Links: [{"title":"DocRED Benchmark (Relation Extraction)","url":"https://paperswithcode.com/sota/relation-extraction-on-docred"},{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"Papers with Code is Dead — Best Alternatives 2026 by Use Case | Codesota | CodeSOTA","url":"https://www.codesota.com/papers-with-code"},{"title":"Journal Title Here, 2025, pp. 1–10 doi: DOI HERE","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"Papers with code · GitHub","url":"https://github.com/paperswithcode"},{"title":"Papers with Code - DocRED Benchmark (Few-Shot Relation Classification)","url":"https://paperswithcode.com/sota/few-shot-relation-classification-on-docred"},{"title":"Papers with Code - DocRED Dataset","url":"https://paperswithcode.com/dataset/docred"},{"title":"Trending Papers - Hugging Face","url":"https://paperswithcode.com/"},{"title":"What is F1 Score in Machine Learning?","url":"https://www.analyticsvidhya.com/blog/2025/12/what-is-f1-score-in-machine-learning/"},{"title":"Exploring AI Benchmarks & Leaderboards &middot;","url":"https://main--dasarpai.netlify.app/dsblog/exploring-ai-benchmarks-and-leaderboards/"}]

Based on my search results, I can provide you with information about DocRED state-of-the-art performance, though I should note that Papers with Code was shut down by Meta in July 2025, which has made accessing current leaderboard data more difficult.

From the available research literature:

**General Performance Range:**
On DocRED benchmark datasets, state-of-the-art methods achieve F1 scores in the range of 75-85%.

**Recent Notable Results:**

The GLiM model, which integrates Graph Transformer and LLM for biomedical relation extraction, was tested across ChemDisGene, BioRED, and DocRED datasets, demonstrating the continuing evolution of approaches on this benchmark.

**Dataset Context:**
DocRED contains 132,375 entities and 56,354 relational facts annotated on 5,053 Wikipedia documents, making it a substantial benchmark for document-level relation extraction.

**Related Development:**
Models trained and evaluated on Re-DocRED (a revised version addressing false negatives in the original DocRED) achieve performance improvements of around 13 F1 points, indicating that the evolution of the dataset itself has significantly impacted reported performance metrics.

Unfortunately, due to the shutdown of Papers with Code, I cannot access the most up-to-date 2025-2026 leaderboard results. For the latest state-of-the-art scores, you may want to check arXiv, academic conferences, or Hugging Face, which has inherited some of Papers with Code's functions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e97c983-65dd-4eb3-bc37-9aa4785eaa37",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "0eabe2c0-8b54-4d11-ba98-1688d01611ab",
  "sourceToolAssistantUUID": "0e97c983-65dd-4eb3-bc37-9aa4785eaa37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-11T23:01:40.235Z_

Let me now search for Papers with Code leaderboards and the remaining queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0eabe2c0-8b54-4d11-ba98-1688d01611ab",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcZvPAE2z1qZBWZLgvW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f616f2f-8ccb-41a9-8526-cb5051b61aed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFwDcTMdo1X42tSiPzi3LD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6658,
      "cache_read_input_tokens": 9987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6658,
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

_source line 18 · 2026-05-11T23:01:41.663Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019pysXrEmsXDPCggiNeHAVX`</summary>

```json
{
  "url": "https://paperswithcode.com/sota/relation-extraction-on-docred",
  "prompt": "Extract all model names, F1 scores, and paper titles from the DocRED leaderboard. List them in order of best to worst performance. Include dates if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f616f2f-8ccb-41a9-8526-cb5051b61aed",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcZvPAE2z1qZBWZLgvW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d55b5ee-b4b9-4b90-9b5a-ef2fefb2b777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFwDcTMdo1X42tSiPzi3LD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6658,
      "cache_read_input_tokens": 9987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6658,
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

_source line 19 · 2026-05-11T23:01:41.886Z_

<details><summary>↩ Tool result · `toolu_019pysXrEmsXDPCggiNeHAVX`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://paperswithcode.com/sota/relation-extraction-on-docred
Redirect URL: https://huggingface.co/papers/trending
Status: 302 Found

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://huggingface.co/papers/trending"
- prompt: "Extract all model names, F1 scores, and paper titles from the DocRED leaderboard. List them in order of best to worst performance. Include dates if available."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d55b5ee-b4b9-4b90-9b5a-ef2fefb2b777",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "dae7cba8-7499-4b2e-9668-240b0b6a80f9",
  "sourceToolAssistantUUID": "8d55b5ee-b4b9-4b90-9b5a-ef2fefb2b777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-11T23:01:42.189Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AfuebnyFGwCMiayJYgAQxV`</summary>

```json
{
  "query": "site:paperswithcode.com ACE05 entity relation extraction leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dae7cba8-7499-4b2e-9668-240b0b6a80f9",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcZvPAE2z1qZBWZLgvW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71b64cc9-1682-4af2-8daa-5096ca721868",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFwDcTMdo1X42tSiPzi3LD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6658,
      "cache_read_input_tokens": 9987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6658,
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

_source line 21 · 2026-05-11T23:01:43.133Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ByV7bywuBPjzcYvyBayXAw`</summary>

```json
{
  "query": "site:paperswithcode.com SciERC relation extraction leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71b64cc9-1682-4af2-8daa-5096ca721868",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcZvPAE2z1qZBWZLgvW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e51412e-9d14-4c02-b87e-c19bcc9f1ba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFwDcTMdo1X42tSiPzi3LD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6658,
      "cache_read_input_tokens": 9987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6658,
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

_source line 22 · 2026-05-11T23:01:43.743Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GLAuMbxQ9M5C68hm8yQJaU`</summary>

```json
{
  "query": "\"attribution information extraction structured\" provenance NLP 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e51412e-9d14-4c02-b87e-c19bcc9f1ba6",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcZvPAE2z1qZBWZLgvW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ded0f398-c22f-49f5-9143-d8d7b2000c1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFwDcTMdo1X42tSiPzi3LD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6658,
      "cache_read_input_tokens": 9987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6658,
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

_source line 23 · 2026-05-11T23:01:44.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012zgHyRWng1mTTbbef7cScF`</summary>

```json
{
  "query": "\"evidence span prediction\" relation extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ded0f398-c22f-49f5-9143-d8d7b2000c1c",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcZvPAE2z1qZBWZLgvW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37af37de-8766-4474-a320-f92e922b86f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFwDcTMdo1X42tSiPzi3LD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6658,
      "cache_read_input_tokens": 9987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6658,
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

_source line 24 · 2026-05-11T23:01:44.839Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019S4WWTE4N4Sz1p7mxpBcJ8`</summary>

```json
{
  "query": "\"grounded extraction\" NER evidence provenance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37af37de-8766-4474-a320-f92e922b86f4",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcZvPAE2z1qZBWZLgvW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ed0d242-2cc6-4df0-95be-9911adb86333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFwDcTMdo1X42tSiPzi3LD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6658,
      "cache_read_input_tokens": 9987,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 390,
          "cache_read_input_tokens": 9987,
          "cache_creation_input_tokens": 6658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6658,
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

_source line 25 · 2026-05-11T23:01:46.526Z_

<details><summary>↩ Tool result · `toolu_01AfuebnyFGwCMiayJYgAQxV`</summary>

```text
Web search results for query: "site:paperswithcode.com ACE05 entity relation extraction leaderboard"

Links: [{"title":"ACE 2005 Benchmark (Relation Extraction)","url":"https://paperswithcode.com/sota/relation-extraction-on-ace-2005"},{"title":"Papers with Code - A Frustratingly Easy Approach for Entity and Relation Extraction","url":"https://paperswithcode.com/paper/a-frustratingly-easy-approach-for-joint"},{"title":"Entity, Relation, and Event Extraction with Contextualized ...","url":"https://paperswithcode.com/paper/entity-relation-and-event-extraction-with/review/"},{"title":"Joint Entity and Relation Extraction","url":"https://paperswithcode.com/task/joint-entity-and-relation-extraction"},{"title":"Relation Extraction | Papers With Code","url":"https://paperswithcode.com/task/relation-extraction/codeless"},{"title":"Papers with Code - Joint Entity and Relation Extraction Based on Table Labeling Using Convolutional Neural Networks","url":"https://paperswithcode.com/paper/joint-entity-and-relation-extraction-based-on"},{"title":"Papers with Code - Joint Entity and Relation Extraction","url":"https://paperswithcode.com/task/joint-entity-and-relation-extraction/latest"},{"title":"Trending Papers - Hugging Face","url":"https://paperswithcode.com/dataset/ace-2005"},{"title":"Papers with Code - Paper tables with annotated results for Two are Better than One: Joint Entity and Relation Extraction with Table-Sequence Encoders","url":"https://paperswithcode.com/paper/two-are-better-than-one-joint-entity-and/review/"},{"title":"Papers with Code - Packed Levitated Marker for Entity and Relation Extraction","url":"https://paperswithcode.com/paper/pack-together-entity-and-relation-extraction"}]

I found search results related to ACE05 entity and relation extraction on Papers with Code. The first result appears to be the leaderboard page you're looking for:

The ACE 2005 Benchmark (Relation Extraction) leaderboard is available at paperswithcode.com/sota/relation-extraction-on-ace-2005. 

Several papers in the results reference performance on ACE05, including a pipelined approach that established state-of-the-art results on ACE05 with improvements in relation F1, and another model that obtained a 4.1%-4.3% strict relation F1 improvement over previous state-of-the-art models on ACE05.

You can visit the leaderboard directly at: https://paperswithcode.com/sota/relation-extraction-on-ace-2005


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71b64cc9-1682-4af2-8daa-5096ca721868",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "6cc53a08-30c2-49cb-ac1c-70c499fc475c",
  "sourceToolAssistantUUID": "71b64cc9-1682-4af2-8daa-5096ca721868",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T23:01:47.585Z_

<details><summary>↩ Tool result · `toolu_01ByV7bywuBPjzcYvyBayXAw`</summary>

```text
Web search results for query: "site:paperswithcode.com SciERC relation extraction leaderboard"

Links: [{"title":"Joint Entity and Relation Extraction on SciERC","url":"https://paperswithcode.com/sota/joint-entity-and-relation-extraction-on"},{"title":"Trending Papers - Hugging Face","url":"https://paperswithcode.com/sota/relation-extraction-on-scierc"},{"title":"Relation Extraction | Papers With Code","url":"https://paperswithcode.com/task/relation-extraction/codeless"},{"title":"Machine Learning Datasets - Relation Extraction","url":"https://paperswithcode.com/datasets?q=&v=lst&o=newest&task=relation-extraction&page=1"},{"title":"SciERC Dataset","url":"https://paperswithcode.com/dataset/scierc"},{"title":"Papers with Code - Joint Entity and Relation Extraction","url":"https://paperswithcode.com/task/joint-entity-and-relation-extraction/latest"},{"title":"SciERC Benchmark (Named Entity Recognition (NER))","url":"https://paperswithcode.com/sota/named-entity-recognition-ner-on-scierc"},{"title":"Papers with Code - FREDo Dataset","url":"https://paperswithcode.com/dataset/fredo"},{"title":"Relation Extraction","url":"https://paperswithcode.com/task/relation-extraction"},{"title":"SciERC Benchmark (Joint Entity and Relation Extraction) | Papers With Code","url":"https://paperswithcode.com/sota/joint-entity-and-relation-extraction-on?p=entity-relation-and-event-extraction-with"}]

Based on the search results, I found relevant information about SciERC relation extraction leaderboards on Papers with Code:

The search results reference the Papers with Code website which hosts leaderboards for tracking progress in relation extraction tasks. The results show that there are multiple benchmarks available, including:

1. **Relation Extraction on SciERC** - SciERC is listed among the relation extraction datasets tracked on Papers with Code

2. **Joint Entity and Relation Extraction on SciERC** - SciERC is one of the benchmarks used to track progress in Joint Entity and Relation Extraction tasks on Papers with Code. The current state-of-the-art on SciERC for Joint Entity and Relation Extraction is PL-Marker, with a full comparison of 11 papers with code available

The specific leaderboard pages are:
- For joint entity and relation extraction: `https://paperswithcode.com/sota/joint-entity-and-relation-extraction-on`
- For relation extraction alone: `https://paperswithcode.com/sota/relation-extraction-on-scierc`

These leaderboards allow you to track and compare different models' performance on the SciERC dataset for relation extraction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e51412e-9d14-4c02-b87e-c19bcc9f1ba6",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "645dc660-44cb-494c-99c3-b9492acaf06c",
  "sourceToolAssistantUUID": "8e51412e-9d14-4c02-b87e-c19bcc9f1ba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-11T23:01:50.700Z_

<details><summary>↩ Tool result · `toolu_01GLAuMbxQ9M5C68hm8yQJaU`</summary>

```text
Web search results for query: ""attribution information extraction structured" provenance NLP 2025 2026"

Links: [{"title":"What Structured NLP Does That LLMs Still Can't: Precision Extraction at Billion-Document Scale - John Snow Labs","url":"https://www.johnsnowlabs.com/what-structured-nlp-does-that-llms-still-cant-precision-extraction-at-billion-document-scale/"},{"title":"EXTENDING PROVENANCE FOR UNDERSTANDING CLAIMS AND DATA ANALYSES Yi Zhang","url":"https://cogcomp.seas.upenn.edu/papers/Zhang22.pdf"},{"title":"NLPIR 2026","url":"https://nlpir.net/"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"NeurIPS Poster Model Provenance Testing for Large Language Models","url":"https://neurips.cc/virtual/2025/poster/118754"},{"title":"Evaluation of Attribution Bias in Generator-Aware Retrieval ...","url":"https://aclanthology.org/2025.findings-acl.1087.pdf"},{"title":"What is Information Extraction? | IBM","url":"https://www.ibm.com/think/topics/information-extraction"},{"title":"Information Extraction from Visually Rich Documents using ...","url":"https://aclanthology.org/2025.acl-long.844.pdf"},{"title":"Survey on legal information extraction: current status and open challenges | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02600-5"},{"title":"Construction of Knowledge Graphs: Current State and Challenges","url":"https://www.mdpi.com/2078-2489/15/8/509"}]

Based on the web search results, here's what I found regarding attribution information extraction, structured data, and provenance in NLP for 2025-2026:

## Key Findings:

**Provenance and Attribution in Healthcare NLP:**
Regulatory-grade auditability and provenance involves every extracted entity linking back to source document ID, text span, extraction timestamp, model version, and confidence score. Models trained on clinical text with assertion detection, relation extraction, and temporal reasoning components reliably identify negation, temporality, and subject attribution (such as distinguishing "mother has diabetes" versus "patient has diabetes") that general-purpose models frequently miss.

**Structured Information Extraction:**
Information extraction (IE) is the automated process of extracting structured information from semi-structured or unstructured text data, transforming human language text sources such as PDFs into a format that's organized, searchable and machine-readable. The goal of information extraction is to extract structural knowledge (such as entities, relations and events) from plain and unstructured texts.

**Attribution and Retrieval Systems:**
Recent 2025 research has focused on attribution quality in retrieval-augmented generation systems, examining how models attribute information to sources and potential biases in authorship attribution.

**Knowledge Graph Provenance:**
Metadata Management involves the acquisition and management of different kinds of metadata, including about the provenance of entities, structural metadata, temporal information, quality reports, or process logs.

These developments reflect growing emphasis on explainability, auditability, and proper source attribution in NLP systems for 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ded0f398-c22f-49f5-9143-d8d7b2000c1c",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "61fad1e4-2852-4601-bb89-e1120bf6a3ee",
  "sourceToolAssistantUUID": "ded0f398-c22f-49f5-9143-d8d7b2000c1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-11T23:01:52.395Z_

<details><summary>↩ Tool result · `toolu_019S4WWTE4N4Sz1p7mxpBcJ8`</summary>

```text
Web search results for query: ""grounded extraction" NER evidence provenance 2025 2026"

Links: [{"title":"Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking","url":"https://www.mdpi.com/2073-431X/15/3/178"},{"title":"Forensics And Futures: Navigating Digital Evidence, AI, And Risk In 2026 - Part 1 : LCG Discovery Experts","url":"https://lcgdiscovery.com/forensics-and-futures-navigating-digital-evidence-ai-and-risk-in-2026-part-1/"},{"title":"Zero-shot evidence-grounded extraction of blood–brain barrier nanoparticle design parameters with open-weight language models - IOPscience","url":"https://iopscience.iop.org/article/10.1088/2632-2153/ae5442"},{"title":"Exploring LLMs for Scientific Information Extraction using the SciEx Framework","url":"https://arxiv.org/pdf/2512.10004"},{"title":"From Prompt Engineering to Knowledge Graphs — Part 1 | by Fanghua (Joshua) Yu | Medium","url":"https://medium.com/@yu-joshua/from-prompt-engineering-to-knowledge-graphs-part-1-8b6fa01fd06e"},{"title":"FactReview: Evidence-Grounded Reviews with Literature Positioning and Execution-Based Claim Verification","url":"https://arxiv.org/html/2604.04074v2"},{"title":"GutenOCR: Our Approach to Grounded OCR for Production Workflows","url":"https://www.roots.ai/blog/gutenocr-our-approach-grounded-ocr-production-workflows"},{"title":"Google Open-Sources LangExtract for Accurate Document ...","url":"https://www.linkedin.com/posts/pankajmath_github-googlelangextract-a-python-library-activity-7426097480095789056-rld6"},{"title":"MedScribe: Clinically Grounded CT Reporting through Agentic Workflows","url":"https://arxiv.org/html/2605.01779v1"},{"title":"Grounded Theory Guide (2026) | Explained Step-by-Step","url":"https://www.maxqda.com/research-guides/grounded-theory"}]

Based on the web search results, here are the key findings on grounded extraction, NER, evidence, and provenance from recent 2025-2026 research:

## Knowledge Graph Extraction with Grounding and Provenance

The AEVS framework grounds every triplet element to the source text, addressing a critical challenge in extraction. The root cause of LLM hallucination is the lack of provenance: existing methods produce triplets without explicit links to their textual origins, making faithfulness unverifiable.

## Grounded Extraction Approach

Triplets are extracted with explicit constraints requiring each element to be linked to discovered anchors. The verification uses a novel "extract-then-restore" paradigm with a hierarchy of matching strategies: exact matching, fuzzy matching for minor variations, schema-based matching for relation normalization, and text search as a fallback.

## Evidence-Based Information Extraction

Each extracted parameter value is accompanied by a direct quotation from the source text, ensuring data provenance and enabling subsequent verification, either manually or through automated judge models.

## Scientific Information Extraction

Elements are annotated with provenance metadata, including document identifiers, chunk indices, and figure references, which ensures full traceability and verifiable linkage.

## Atomic Fact Extraction

First extract atomic, verifiable facts, then convert them into triples/graph updates, separating "what is claimed" from "how we structure it," enabling better verification and provenance.

These approaches from 2025-2026 research consistently emphasize linking extracted information directly to source evidence to ensure verifiability and prevent hallucination in NER and information extraction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ed0d242-2cc6-4df0-95be-9911adb86333",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "6d728e82-2418-4111-b797-b2cfa6b2a6cc",
  "sourceToolAssistantUUID": "3ed0d242-2cc6-4df0-95be-9911adb86333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-11T23:01:53.387Z_

<details><summary>↩ Tool result · `toolu_012zgHyRWng1mTTbbef7cScF`</summary>

```text
Web search results for query: ""evidence span prediction" relation extraction 2025 2026"

Links: [{"title":"Entity and Relationship Extraction with High-quality Spans and Enhanced Marker Strategies | Machine Intelligence Research | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11633-024-1515-3"},{"title":"[PDF] Entity, Relation, and Event Extraction with Contextualized Span Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Entity,-Relation,-and-Event-Extraction-with-Span-Wadden-Wennberg/fac2368c2ec81ef82fd168d49a0def2f8d1ec7d8"},{"title":"GitHub - dwadden/dygiepp: Span-based system for named entity, relation, and event extraction.","url":"https://github.com/dwadden/dygiepp"},{"title":"Entity, Relation, and Event Extraction with Contextualized Span Representations | Paper to HTML | Allen Institute for AI","url":"https://papertohtml.org/paper?id=fac2368c2ec81ef82fd168d49a0def2f8d1ec7d8"},{"title":"Entity, Relation, and Event Extraction with Contextualized Span Representations | Request PDF","url":"https://www.researchgate.net/publication/336996545_Entity_Relation_and_Event_Extraction_with_Contextualized_Span_Representations"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Closed-Domain Event Extraction Literature Review January 2025 v1.0","url":"https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf"},{"title":"Span-based Joint Entity and Relation Extraction with ...","url":"https://arxiv.org/pdf/1909.07755"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"},{"title":"Span-Level Model for Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/335781051_Span-Level_Model_for_Relation_Extraction"}]

Based on the search results, here's what I found about evidence span prediction and relation extraction in 2025-2026:

## Recent Developments (2025-2026)

Entity and relation extraction is a critical task in information extraction, with recent approaches emphasizing improved span representations. 

### Key Approaches

**Span-Based Methods:**
Recent work proposes enhancing entity and relation extraction with high-quality spans and enhanced marker (HSEM) strategies, which assign adaptive weights to different spans to make models more focused on high quality spans.

**Evidence Selection in Document-Level Extraction:**
Evidence selection refers to identifying and selecting relevant sentences or text from a document that provides crucial information to determine relationships between entities, with models like E2GRE tackling the challenge of handling relations spanning multiple sentences by jointly extracting relations and their supporting evidence sentences.

E2GRE uses the last four layers of BERT for relation extraction and evidence prediction, and enhances BERT's attention mechanism to focus on relevant context, using attention probabilities as supplementary features for evidence prediction.

### Current Challenges

There is an overabundance of low-quality candidate spans, which hinders the effective extraction of information from high-quality candidate spans.

### Broader Context

Recent surveys examining the latest advancements in Relation Extraction from 2020 to 2023 highlight the dominance of BERT-based methods in achieving state-of-the-art results, while also noting the promising capabilities of emerging Large Language Models like T5.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37af37de-8766-4474-a320-f92e922b86f4",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "8cbdf5f2-b36f-4c4d-ae20-e0759245e498",
  "sourceToolAssistantUUID": "37af37de-8766-4474-a320-f92e922b86f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-11T23:01:55.767Z_

Good findings so far. Let me now fetch the specific leaderboard pages and get more detailed numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cbdf5f2-b36f-4c4d-ae20-e0759245e498",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcb6VQ1qWbMFYWSUvVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db641168-87bd-4e74-8916-7d45b2f18248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8ovWUUPb6b4CxFmJ51M1B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3840,
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

_source line 31 · 2026-05-11T23:01:57.824Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LUpNkfQVDuBBoecikMzcG6`</summary>

```json
{
  "url": "https://paperswithcode.com/sota/relation-extraction-on-ace-2005",
  "prompt": "Extract all model names, F1 scores, and paper titles from the ACE 2005 relation extraction leaderboard. List them in order of best to worst performance. Include dates if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db641168-87bd-4e74-8916-7d45b2f18248",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcb6VQ1qWbMFYWSUvVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84c07773-60db-451c-89fa-54d76f522d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8ovWUUPb6b4CxFmJ51M1B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3840,
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

_source line 32 · 2026-05-11T23:01:57.860Z_

<details><summary>↩ Tool result · `toolu_01LUpNkfQVDuBBoecikMzcG6`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://paperswithcode.com/sota/relation-extraction-on-ace-2005
Redirect URL: https://huggingface.co/papers/trending
Status: 302 Found

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://huggingface.co/papers/trending"
- prompt: "Extract all model names, F1 scores, and paper titles from the ACE 2005 relation extraction leaderboard. List them in order of best to worst performance. Include dates if available."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84c07773-60db-451c-89fa-54d76f522d84",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "4f3e3838-7376-4d7d-b11a-992bd3c88b6e",
  "sourceToolAssistantUUID": "84c07773-60db-451c-89fa-54d76f522d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-11T23:01:58.893Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016AEL7XADAGtpnhK5jA6aUC`</summary>

```json
{
  "url": "https://paperswithcode.com/sota/joint-entity-and-relation-extraction-on",
  "prompt": "Extract all model names, F1 scores (both NER and RE), and paper titles from the SciERC joint entity and relation extraction leaderboard. List them in order. Include dates if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f3e3838-7376-4d7d-b11a-992bd3c88b6e",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcb6VQ1qWbMFYWSUvVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad58c8dd-d20d-4e54-b168-66c748fe40ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8ovWUUPb6b4CxFmJ51M1B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3840,
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

_source line 34 · 2026-05-11T23:01:58.919Z_

<details><summary>↩ Tool result · `toolu_016AEL7XADAGtpnhK5jA6aUC`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://paperswithcode.com/sota/joint-entity-and-relation-extraction-on
Redirect URL: https://huggingface.co/papers/trending
Status: 302 Found

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://huggingface.co/papers/trending"
- prompt: "Extract all model names, F1 scores (both NER and RE), and paper titles from the SciERC joint entity and relation extraction leaderboard. List them in order. Include dates if available."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad58c8dd-d20d-4e54-b168-66c748fe40ec",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "5b50909e-a4e1-4487-9f44-0a736ae9295b",
  "sourceToolAssistantUUID": "ad58c8dd-d20d-4e54-b168-66c748fe40ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-11T23:02:00.829Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ECa1xGWbEtrQWdQojtZwni`</summary>

```json
{
  "url": "https://www.mdpi.com/2073-431X/15/3/178",
  "prompt": "Extract the full title, authors, publication date, and key methodology for this paper about grounded knowledge graph extraction with provenance tracking. What datasets were used? What were the main results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b50909e-a4e1-4487-9f44-0a736ae9295b",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcb6VQ1qWbMFYWSUvVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fa4af44-a2eb-4f18-887b-88cf306736c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8ovWUUPb6b4CxFmJ51M1B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3840,
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

_source line 36 · 2026-05-11T23:02:00.864Z_

<details><summary>↩ Tool result · reported error · `toolu_01ECa1xGWbEtrQWdQojtZwni`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fa4af44-a2eb-4f18-887b-88cf306736c6",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "cb39b4bf-14c4-4c6d-84ad-37c0054e759f",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "7fa4af44-a2eb-4f18-887b-88cf306736c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-11T23:02:01.694Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014dY6on3sLVU1rawyZNPGBE`</summary>

```json
{
  "query": "DocRED document relation extraction best model 2025 F1 score ATLOP KD-DocRE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb39b4bf-14c4-4c6d-84ad-37c0054e759f",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcb6VQ1qWbMFYWSUvVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af4234b9-07ad-4252-97b1-caa771567cbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8ovWUUPb6b4CxFmJ51M1B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3840,
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

_source line 38 · 2026-05-11T23:02:02.128Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015EqbBXH6qWfzdeTjwCdRey`</summary>

```json
{
  "query": "GLiM graph transformer LLM DocRED relation extraction 2025 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af4234b9-07ad-4252-97b1-caa771567cbe",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcb6VQ1qWbMFYWSUvVh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8dc8a0f-41ea-4f99-a680-a138cba65362",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8ovWUUPb6b4CxFmJ51M1B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16645,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3840
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 992,
          "output_tokens": 488,
          "cache_read_input_tokens": 16645,
          "cache_creation_input_tokens": 3840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3840,
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

_source line 39 · 2026-05-11T23:02:08.445Z_

<details><summary>↩ Tool result · `toolu_015EqbBXH6qWfzdeTjwCdRey`</summary>

```text
Web search results for query: "GLiM graph transformer LLM DocRED relation extraction 2025 results"

Links: [{"title":"GLiM: Integrating Graph Transformer and LLM for Document-Level Biomedical Relation Extraction with Incomplete Labeling - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.727/"},{"title":"GLiM: Integrating Graph Transformer and LLM for ...","url":"https://aclanthology.org/2025.findings-acl.727.pdf"},{"title":"GLiM: Integrating Graph Transformer and LLM for Document-Level Biomedical Relation Extraction with Incomplete Labeling | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.findings-acl.727@ACL"},{"title":"GLiM: Integrating Graph Transformer and LLM for Document-Level Biomedical Relation Extraction with Incomplete Labeling | Request PDF","url":"https://www.researchgate.net/publication/394273241_GLiM_Integrating_Graph_Transformer_and_LLM_for_Document-Level_Biomedical_Relation_Extraction_with_Incomplete_Labeling"},{"title":"GitHub - HaoFang10/GLiM","url":"https://github.com/HaoFang10/GLiM"},{"title":"GLiM: Integrating Graph Transformer and LLM for ...","url":"https://chatpaper.com/paper/178080"},{"title":"A Temporal Knowledge Graph Generation Dataset Supervised Distantly by Large Language Models | Scientific Data","url":"https://www.nature.com/articles/s41597-025-05062-0"},{"title":"LLMGraphTransformer — 🦜🔗 LangChain documentation","url":"https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.llm.LLMGraphTransformer.html"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"}]

Based on the search results, here are the 2025 results for GLiM (Graph Transformer LLM for Document-Level Relation Extraction):

## Overview

GLiM is a novel framework that reduces the problem space using a graph-enhanced Transformer-based model and leverages large language models (LLMs) for reasoning. The research was published in the Findings of ACL 2025.

## Methodology

GLiM employs a cascaded approach: first, a graph-enhanced Transformer processes entity-pair relations with finer granularity by dynamically adjusting the graph size based on the number of entities; then, LLM inference handles challenging cases.

## Key Results

Experiments show that GLiM boosts average recall and F1 scores by +6.34 and +4.41, respectively, outperforming state-of-the-art models on biomedical benchmarks.

## Datasets Evaluated

The research evaluated performance across test datasets: ChemDisGene, BioRED, and DocRED.

## Implementation

Code is being released at https://github.com/HaoFang10/GLiM.

The paper addresses a critical challenge in document-level relation extraction where the problem space expands quadratically as the number and complexity of entities and entity-pair relations grow, causing incomplete annotations and frequent false negatives, especially in biomedical datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8dc8a0f-41ea-4f99-a680-a138cba65362",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "07f1d09a-9d80-4d01-a59e-df53288282c5",
  "sourceToolAssistantUUID": "c8dc8a0f-41ea-4f99-a680-a138cba65362",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-11T23:02:12.545Z_

<details><summary>↩ Tool result · `toolu_014dY6on3sLVU1rawyZNPGBE`</summary>

```text
Web search results for query: "DocRED document relation extraction best model 2025 F1 score ATLOP KD-DocRE"

Links: [{"title":"Document-level Relation Extraction via Separate Relation Representation and Logical Reasoning | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3597610"},{"title":"Toward Better Document-Level Relation Extraction: De-sampling and Mixture of Experts in Action | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-04549-2_12"},{"title":"GitHub - Hytn/DocRED-HWE: Paper of ACL2023 - Benchmarking Models for Language Understanding in Document-Level Relation Extraction","url":"https://github.com/hytn/docred-hwe"},{"title":"Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757"},{"title":"Self-distillation framework for document-level relation extraction in low-resource environments - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11042033/"},{"title":"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/17717"},{"title":"Document-Level Relation Extraction with Relation Correlation Enhancement","url":"https://arxiv.org/html/2310.13000"},{"title":"[2205.01909] Modeling Task Interactions in Document-Level Joint Entity and Relation Extraction","url":"https://ar5iv.labs.arxiv.org/html/2205.01909"}]

Based on the search results, here's what I found regarding DocRED document relation extraction models and their F1 scores:

## Key Models and Performance

ATLOP (Adaptive Thresholding and Localized cOntext Pooling) model achieves an F1 score of 63.4 on the DocRED dataset.

KD-DocRE leverages an axial attention module to model entity-pairs interdependency across sentences, applies an adaptive focal loss to mitigate class imbalance and uses knowledge distillation to incorporate distantly supervised data. A more recent model, GLiDRE, attains a test F1 score of 77.83, placing it in close competition with established DocRE models like ATLOP and KD-DocRE.

## Recent State-of-the-Art (2025)

While models like DREEAM and TTM-RE incorporate additional mechanisms, such as evidence information for DREEAM and the Turing Token Machine for TTM-RE that is designed to scale better with large datasets.

## Other Notable Models

SRLR improves F1 by 18.10, 8.60, 7.10, 5.90, and 1.70 compared with CNN, BRAN, EoG, LSR, ATLOP respectively on the Test set.

ATLOP-DME model achieved improvements of 24.02%, 10.19%, 7.5%, and 2.9% compared to the ATLOP model on the DocRED, Re-DocRED, CDR, and GDA datasets respectively.

The search results indicate there are multiple competitive models, with more recent approaches showing incremental improvements over the foundational ATLOP model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af4234b9-07ad-4252-97b1-caa771567cbe",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "ae920f75-2ccb-4bc2-b523-2a070b92c12f",
  "sourceToolAssistantUUID": "af4234b9-07ad-4252-97b1-caa771567cbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-11T23:02:16.915Z_

Papers with Code is now redirecting to Hugging Face. Let me search for more specific benchmark numbers and fetch some key papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae920f75-2ccb-4bc2-b523-2a070b92c12f",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawccWSakZF4tZqDESFX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "829aa9a7-f640-4a11-a363-70783601398e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4FwRRqxS2zZabzgR1kgat",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 2886,
      "cache_read_input_tokens": 20485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2886,
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

_source line 42 · 2026-05-11T23:02:18.532Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014Fp9bNeFE5YXMbmNf9YhjP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.00757",
  "prompt": "Extract the full title, authors, and all reported F1 scores on DocRED and Re-DocRED benchmarks. What is the state of the art result they compare against?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "829aa9a7-f640-4a11-a363-70783601398e",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawccWSakZF4tZqDESFX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f000cf14-dd78-4e52-a945-a26010ee73d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4FwRRqxS2zZabzgR1kgat",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 2886,
      "cache_read_input_tokens": 20485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2886,
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

_source line 43 · 2026-05-11T23:02:20.003Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E4NQSjGrhP7GmU4q3zek45`</summary>

```json
{
  "query": "PL-Marker ACE05 SciERC F1 score NER relation extraction results 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f000cf14-dd78-4e52-a945-a26010ee73d0",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawccWSakZF4tZqDESFX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13710b81-ec68-41e1-a0b4-4aa57c396902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4FwRRqxS2zZabzgR1kgat",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 2886,
      "cache_read_input_tokens": 20485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2886,
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

_source line 44 · 2026-05-11T23:02:20.798Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WKd7dzGnVvJwBgupV1URxS`</summary>

```json
{
  "query": "DREEAM DocRED evidence extraction F1 score 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13710b81-ec68-41e1-a0b4-4aa57c396902",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawccWSakZF4tZqDESFX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd274122-b4df-4fcf-bec4-75c9b68bf7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4FwRRqxS2zZabzgR1kgat",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 2886,
      "cache_read_input_tokens": 20485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2886,
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

_source line 45 · 2026-05-11T23:02:21.307Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NaYomjXTszhVL6VADJAoaP`</summary>

```json
{
  "query": "Re-DocRED state of the art F1 2024 2025 leaderboard best model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd274122-b4df-4fcf-bec4-75c9b68bf7a3",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawccWSakZF4tZqDESFX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50b3fe39-605c-4a9c-986f-719739853e9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4FwRRqxS2zZabzgR1kgat",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 2886,
      "cache_read_input_tokens": 20485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2886,
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

_source line 46 · 2026-05-11T23:02:22.277Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R5JaHDXrP14fx42oqzhB4P`</summary>

```json
{
  "query": "ACE05 joint entity relation extraction SOTA 2024 2025 F1 PURE UniRE PL-Marker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50b3fe39-605c-4a9c-986f-719739853e9b",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawccWSakZF4tZqDESFX5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4877a824-883a-44a8-bbad-fab4edde4c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4FwRRqxS2zZabzgR1kgat",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 959,
      "cache_creation_input_tokens": 2886,
      "cache_read_input_tokens": 20485,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 959,
          "output_tokens": 388,
          "cache_read_input_tokens": 20485,
          "cache_creation_input_tokens": 2886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2886,
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

_source line 47 · 2026-05-11T23:02:23.993Z_

<details><summary>↩ Tool result · `toolu_014Fp9bNeFE5YXMbmNf9YhjP`</summary>

```text
# GLiDRE Paper Summary

**Full Title:** "GLiDRE: Generalist Lightweight model for Document-level Relation Extraction"

**Authors:** Robin Armingaud and Romaric Besançon

**F1 Scores:** The webpage content provided does not include specific F1 score results on DocRED and Re-DocRED benchmarks. The abstract only states the model "outperforms existing methods in data-constrained scenarios," but numerical performance metrics are not disclosed on this page.

**State-of-the-Art Comparison:** The page does not detail which specific prior methods or their results are used as comparison baselines. The abstract mentions the work "establishing a new state-of-the-art in few-shot document-level relation extraction," but the actual competing approaches and their performance figures are not provided in this arXiv abstract page.

To obtain detailed benchmark results and baseline comparisons, you would need to access the full paper PDF or HTML version linked on this page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f000cf14-dd78-4e52-a945-a26010ee73d0",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "ba0372a1-f96c-4258-b32e-966397a4f1e3",
  "sourceToolAssistantUUID": "f000cf14-dd78-4e52-a945-a26010ee73d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-11T23:02:26.052Z_

<details><summary>↩ Tool result · `toolu_01E4NQSjGrhP7GmU4q3zek45`</summary>

```text
Web search results for query: "PL-Marker ACE05 SciERC F1 score NER relation extraction results 2024 2025"

Links: [{"title":"[2109.06067] Packed Levitated Marker for Entity and Relation Extraction","url":"https://ar5iv.labs.arxiv.org/html/2109.06067"},{"title":"GitHub - thunlp/PL-Marker: Source code for \"Packed Levitated Marker for Entity and Relation Extraction\" · GitHub","url":"https://github.com/thunlp/PL-Marker"},{"title":"Packed Levitated Marker for Entity and Relation Extraction","url":"https://openreview.net/pdf?id=0YD1VAUGZ-X"},{"title":"GitHub - princeton-nlp/PURE: [NAACL 2021] A Frustratingly Easy Approach for Entity and Relation Extraction https://arxiv.org/abs/2010.12812","url":"https://github.com/princeton-nlp/PURE"},{"title":"Iterative Transformer-based Entity Recognition and ...","url":"https://aclanthology.org/2024.findings-emnlp.655.pdf"},{"title":"SciER: An Entity and Relation Extraction Dataset for ...","url":"https://aclanthology.org/2024.emnlp-main.726.pdf"},{"title":"Position-aware Joint Entity and Relation Extraction with Attention Mechanism","url":"https://www.ijcai.org/proceedings/2022/0624.pdf"},{"title":"Packed Levitated Marker for Entity and Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.337/"},{"title":"Full article: An entity and relation extraction model based on context query and axial attention towards patent texts","url":"https://www.tandfonline.com/doi/full/10.1080/09540091.2024.2426816"},{"title":"GitHub - Hiaa1/SURE: Source code for COLING 2025 long paper \"SURE: Mutually Visible Objects and Self-generated Candidate Labels For Relation Extraction\" · GitHub","url":"https://github.com/Hiaa1/SURE"}]

Based on the search results, I found information about PL-Marker's F1 scores on ACE05 and SciERC datasets for NER and relation extraction tasks:

## PL-Marker Results

### Relation Extraction Performance
Compared to PURE, PL-Marker achieves a 2.8%-4.0% relation F1 (boundaries) improvement on ACE05 and SciERC.

PL-Marker obtains a 4.1%-4.3% strict relation F1 improvement with higher speed over previous state-of-the-art models on ACE04 and ACE05.

### Named Entity Recognition Performance
PL-Marker with neighborhood-oriented packing scheme performs much better than the model with random packing scheme on NER.

### Comparative Performance
In a more recent study (2024), PERE-CA outperformed PL-Marker by 0.2% of F1 on TFH-2020 and by 0.5% of F1 on SciERC, and both SpERT and PL-Marker performed well on entity recognition, with PL-Marker achieving the highest entity recall rate among all models on TFH-2020, reaching 82.3%.

The search results primarily contain information from the original PL-Marker paper (published in 2022) and comparative studies through 2024-2025, though specific exact F1 scores are not fully listed in these excerpts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13710b81-ec68-41e1-a0b4-4aa57c396902",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "1617266e-e761-4ffe-9a27-734342c4eccb",
  "sourceToolAssistantUUID": "13710b81-ec68-41e1-a0b4-4aa57c396902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-11T23:02:26.828Z_

<details><summary>↩ Tool result · `toolu_01WKd7dzGnVvJwBgupV1URxS`</summary>

```text
Web search results for query: "DREEAM DocRED evidence extraction F1 score 2023 2024 2025"

Links: [{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/373811777_DREEAM_Guiding_Attention_with_Evidence_for_Improving_Document-Level_Relation_Extraction"},{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"DREEAM: Guiding Attention with Evidence for Improving ...","url":"https://aclanthology.org/2023.eacl-main.145.pdf"},{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://ar5iv.labs.arxiv.org/html/2302.08675"},{"title":"Semantic-guided attention and adaptive gating for document-level relation extraction | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-78051-9"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.eacl-main.145/"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757"},{"title":"GitHub - YoumiMa/dreeam: source code for {D}ocument-level {R}elation {E}xtraction with {E}vidence-guided {A}ttention {M}echanism · GitHub","url":"https://github.com/YoumiMa/dreeam"},{"title":"[PDF] Revisiting DocRED - Addressing the False Negative Problem in Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Revisiting-DocRED-Addressing-the-False-Negative-in-Tan-Xu/c86754c01fc64a8e8b445f530fe95c1dbab4eb03"},{"title":"Enhanced Heterogeneous Graph Attention Network with a Novel Multilabel Focal Loss for Document-Level Relation Extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10969296/"}]

Based on the web search results, here's what I found regarding DREEAM DocRED evidence extraction F1 scores:

## DREEAM Overview

DREEAM is a memory-efficient approach that adopts evidence information as the supervisory signal, thereby guiding the attention modules of the DocRE system to assign high weights to evidence. The approach exhibits state-of-the-art performance on the DocRED benchmark for both DocRE and ER.

## Evidence Extraction (ER) F1 Score Performance

DREEAM improves over the state-of-the-art supervised approaches by approximately 2.0 points on Evi F1 (evidence F1 score on DocRED).

## Recent Comparisons (2024-2025)

More recent work has compared DREEAM against newer models:
- The DREEAM model uses an attention mechanism that focuses on evidence sentences.
- In few-shot settings, newer models like GLiDRE surpass DREEAM by a margin of over 14 F1 points.

The search results show that DREEAM was published in 2023 and has been cited as a baseline in subsequent research through 2025, though more recent models have achieved higher performance on various DocRED benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd274122-b4df-4fcf-bec4-75c9b68bf7a3",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "cda25b4c-e54f-42ee-b569-f1dfd9624f36",
  "sourceToolAssistantUUID": "bd274122-b4df-4fcf-bec4-75c9b68bf7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-11T23:02:34.880Z_

<details><summary>↩ Tool result · `toolu_01R5JaHDXrP14fx42oqzhB4P`</summary>

```text
Web search results for query: "ACE05 joint entity relation extraction SOTA 2024 2025 F1 PURE UniRE PL-Marker"

Links: [{"title":"[1905.05529] Entity-Relation Extraction as Multi-Turn Question Answering","url":"https://arxiv.org/abs/1905.05529"},{"title":"Position-aware Joint Entity and Relation Extraction with Attention Mechanism","url":"https://www.ijcai.org/proceedings/2022/0624.pdf"},{"title":"An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction","url":"https://arxiv.org/html/2401.01326v1"},{"title":"Joint entity and relation extraction based on a hybrid neural network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231217301613"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Multi-classification results of ACE05 dataset. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Multi-classification-results-of-ACE05-dataset_tbl1_353798698"},{"title":"Relation extraction: advancements through deep learning and entity-related features | Social Network Analysis and Mining | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13278-023-01095-8"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"},{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"A Frustratingly Easy Approach for Entity and Relation ...","url":"https://aclanthology.org/2021.naacl-main.5.pdf"}]

Let me search for more specific information about these models (PURE, UniRE, PL-Marker) and their 2024-2025 results.

Links: [{"title":"GitHub - princeton-nlp/PURE: [NAACL 2021] A Frustratingly Easy Approach for Entity and Relation Extraction https://arxiv.org/abs/2010.12812","url":"https://github.com/princeton-nlp/PURE"},{"title":"[2107.04292] UniRE: A Unified Label Space for Entity Relation Extraction","url":"https://ar5iv.labs.arxiv.org/html/2107.04292"},{"title":"GitHub - sailfish009/PURE: NAACL'2021: A Frustratingly Easy Approach for Entity and Relation Extraction","url":"https://github.com/sailfish009/PURE"},{"title":"UNIRE: A Unified Label Space for Entity Relation Extraction","url":"https://aclanthology.org/2021.acl-long.19.pdf"},{"title":"Packed Levitated Marker for Entity and Relation Extraction","url":"https://openreview.net/pdf?id=0YD1VAUGZ-X"},{"title":"GitHub - thunlp/PL-Marker: Source code for \"Packed Levitated Marker for Entity and Relation Extraction\" · GitHub","url":"https://github.com/thunlp/PL-Marker"},{"title":"A marker collaborating model for entity and relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1319157822003214"},{"title":"[PDF] UniRE: A Unified Label Space for Entity Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/UniRE:-A-Unified-Label-Space-for-Entity-Relation-Wang-Sun/360426953357dba87b99f3dedefae2337a671543"},{"title":"[Quick Review] UniRE: A Unified Label Space for Entity Relation Extraction","url":"https://liner.com/review/unire-unified-label-space-for-entity-relation-extraction"},{"title":"Iterative Transformer-based Entity Recognition and ...","url":"https://aclanthology.org/2024.findings-emnlp.655.pdf"}]

Let me search for more recent 2024-2025 SOTA benchmarks.

Links: [{"title":"Iterative Transformer-based Entity Recognition and ...","url":"https://aclanthology.org/2024.findings-emnlp.655.pdf"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"[1905.05529] Entity-Relation Extraction as Multi-Turn Question Answering","url":"https://arxiv.org/abs/1905.05529"},{"title":"[2010.12812] A Frustratingly Easy Approach for Entity and Relation Extraction","url":"https://arxiv.org/abs/2010.12812"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"A Frustratingly Easy Approach for Entity and Relation Extraction - Princeton University","url":"https://collaborate.princeton.edu/en/publications/a-frustratingly-easy-approach-for-entity-and-relation-extraction/"},{"title":"Entity & Relation Extraction","url":"https://www.emergentmind.com/topics/entity-and-relation-extraction"},{"title":"Relation extraction: advancements through deep learning and entity-related features | Social Network Analysis and Mining | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13278-023-01095-8"},{"title":"Position-aware Joint Entity and Relation Extraction with Attention Mechanism","url":"https://www.ijcai.org/proceedings/2022/0624.pdf"},{"title":"Proceedings of the 2021 Conference of the North American Chapter of the","url":"https://aclanthology.org/2021.naacl-main.5.pdf"}]

Based on my web search results, I found relevant information about the joint entity and relation extraction SOTA models on ACE05. Here's what I found:

## ACE05 Joint Entity Relation Extraction - Key Models and Results

### Notable Models:

**PURE (A Frustratingly Easy Approach for Entity and Relation Extraction)**: Established state-of-the-art on standard benchmarks (ACE04, ACE05 and SciERC), obtaining a 1.7%-2.8% absolute improvement in relation F1 over previous joint models with the same pre-trained encoders. On the ACE05 test set, PURE achieved Entity F1: 0.886587 and Relation F1: 0.670536 (strict Relation F1: 0.646429).

**UniRE (A Unified Label Space for Entity Relation Extraction)**: Based on BERT-base-uncased, ALBERT, and SciBERT as encoding depending on the dataset and achieves state-of-the-art performance on the ACE04 and ACE05 datasets, outperforming several baseline models. UniRE achieves the best performance on ACE04 and SciERC and a comparable result on ACE05, with significant advances in absolute F1 of +0.9 and +0.7 for entity as well as +3.4 and +1.7 for relation on ACE04 and ACE05 respectively compared with the previous best joint model.

**PL-Marker (Packed Levitated Marker)**: Applies BERTBASE on ACE04/05.

### Recent 2024 Results:

On ACE05: TriMF reaches Relation F1 = 66.49, GraphER achieves 66.4 (strict) and 68.4 (boundary), and memory-enhanced document-level methods push strict F1 into the 40s on cross-sentence benchmarks.

Unfortunately, I couldn't find specific 2025 SOTA results in the search results, but the information above shows the state-of-the-art as of 2024 and earlier.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4877a824-883a-44a8-bbad-fab4edde4c44",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "7a852322-8aa4-4040-974c-695972e8bfdb",
  "sourceToolAssistantUUID": "4877a824-883a-44a8-bbad-fab4edde4c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-11T23:02:39.805Z_

<details><summary>↩ Tool result · `toolu_01NaYomjXTszhVL6VADJAoaP`</summary>

```text
Web search results for query: "Re-DocRED state of the art F1 2024 2025 leaderboard best model"

Links: [{"title":"F1 standings 2024 - Formula 1 points","url":"https://www.formula1points.com/season/2024"},{"title":"best f1 stats website for F1 Standings 2025 | Racing Statistics","url":"https://www.racingstatisticsf1.com/f1-standings-2025"},{"title":"F1 - The Official Home of Formula 1® Racing","url":"https://www.formula1.com/en/results/2026/drivers"},{"title":"F1 standings 2026 - Formula 1 points","url":"https://www.formula1points.com/season"},{"title":"2024 F1 standings: Verstappen wins Drivers' Championship while McLaren takes Constructors' title","url":"https://www.motorauthority.com/news/1142473_2024-f1-standings"},{"title":"2024 • STATS F1","url":"https://www.statsf1.com/en/2024.aspx"},{"title":"2024 - Formula 1 F1 Standings - ESPN","url":"https://www.espn.com/racing/standings/_/series/f1/year/2024"},{"title":"2024 F1 Driver Standings","url":"https://www.gpfans.com/en/f1-standings/2024/"},{"title":"F1 2024 Driver Results Table and Progression Chart","url":"https://f1.dg42.net/"},{"title":"2025 - Formula 1 F1 Standings - ESPN","url":"https://www.espn.com/racing/standings/_/series/f1/year/2025"}]

The search results are returning information about Formula 1 racing standings rather than the Re-DocRED benchmark, which is a machine learning/NLP dataset. Let me search with a more specific query to find information about the Re-DocRED leaderboard.

Links: [{"title":"Computer Vision Model Leaderboard | Object Detection Benchmarks","url":"https://leaderboard.roboflow.com/"},{"title":"tonytan48/Re-DocRED · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tonytan48/Re-DocRED"},{"title":"AI Model Leaderboards & Benchmarks | Scale Labs","url":"https://labs.scale.com/leaderboard"},{"title":"What is F1 Score? An Essential Metric in LLM Evaluation","url":"https://datasciencedojo.com/blog/understanding-f1-score/"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"F1 Score in Machine Learning: Formula, Range & Interpretation","url":"https://futurense.com/blog/f1-score-in-machine-learning"},{"title":"Model benchmarks and leaderboards in Microsoft Foundry - Microsoft Foundry | Microsoft Learn","url":"https://learn.microsoft.com/en-us/azure/foundry/concepts/model-benchmarks?view=foundry-classic"},{"title":"RAG Benchmarks Leaderboard: Retrieval Rankings 2026 | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/rag-benchmarks-leaderboard/"},{"title":"Open LLM Leaderboard: DROP deep dive","url":"https://huggingface.co/blog/open-llm-leaderboard-drop"},{"title":"Arena | Benchmark & Compare the Best AI Models","url":"https://web.lmarena.ai/leaderboard"}]

I found a reference to Re-DocRED, but not the leaderboard with specific F1 scores. Let me search more specifically for the Re-DocRED benchmark results and leaderboard.

Links: [{"title":"GitHub - tonytan48/Re-DocRED","url":"https://github.com/tonytan48/Re-DocRED"},{"title":"[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/abs/1906.06127"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"},{"title":"Revisiting DocRED - Addressing the False Negative Problem in Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.580/"},{"title":"[2205.12696] Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/abs/2205.12696"},{"title":"GitHub - thunlp/DocRED: Dataset and codes for ACL 2019 DocRED: A Large-Scale Document-Level Relation Extraction Dataset. · GitHub","url":"https://github.com/thunlp/DocRED"},{"title":"(PDF) DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://www.researchgate.net/publication/333815327_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"[2401.11800] Revisiting Document-Level Relation Extraction with Context-Guided Link Prediction","url":"https://arxiv.org/abs/2401.11800"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/html/2205.12696"}]

Let me search for a specific leaderboard or recent benchmark results with F1 scores.

Links: [{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"tonytan48/Re-DocRED · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tonytan48/Re-DocRED"},{"title":"GitHub - BurgerBurgerBurger/AA: Code for EMNLP 2023 paper \"Anaphor Assisted Document-Level Relation Extraction\"","url":"https://github.com/BurgerBurgerBurger/AA"},{"title":"[2205.12696] Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction","url":"https://ar5iv.labs.arxiv.org/html/2205.12696"},{"title":"GitHub - tonytan48/Re-DocRED","url":"https://github.com/tonytan48/Re-DocRED"}]

Great! I found a reference to the Papers with Code leaderboard. Let me search for the specific leaderboard data.

Links: [{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"DocRED Benchmark (Relation Extraction)","url":"https://paperswithcode.com/sota/relation-extraction-on-docred"},{"title":"Relation Extraction | Papers With Code","url":"https://paperswithcode.com/task/relation-extraction/latest"},{"title":"ReDocRED Benchmark (Relation Extraction)","url":"https://paperswithcode.com/sota/relation-extraction-on-redocred"},{"title":"Papers with Code - DocRED Dataset","url":"https://paperswithcode.com/dataset/docred"},{"title":"GitHub - thunlp/DocRED: Dataset and codes for ACL 2019 DocRED: A Large-Scale Document-Level Relation Extraction Dataset. · GitHub","url":"https://github.com/thunlp/DocRED"},{"title":"Papers with Code - Joint Entity and Relation Extraction","url":"https://paperswithcode.com/task/joint-entity-and-relation-extraction/latest"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"},{"title":"Papers with Code - Paper tables with annotated results for DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://paperswithcode.com/paper/docred-a-large-scale-document-level-relation/review/"},{"title":"thunlp/docred · Datasets at Hugging Face","url":"https://huggingface.co/datasets/thunlp/docred"}]

Based on my search results, I found information about the Re-DocRED benchmark and its leaderboard. Let me provide you with the information I found:

The leaderboard of Re-DocRED is hosted on Paperswithcode. However, the specific F1 scores and current 2024-2025 state-of-the-art results were not fully detailed in the accessible search results.

What I can tell you about Re-DocRED:

Re-DocRED is a revised version of the DocRED dataset created from an EMNLP 2022 research paper that revised 4,053 documents in the DocRED dataset. The Re-DocRED Dataset resolved incompleteness problems by supplementing relation triples, addressed logical inconsistencies, and corrected coreferential errors.

Models trained and evaluated on Re-DocRED achieve performance improvements of around 13 F1 points compared to the original DocRED dataset.

For accessing the actual leaderboard with current F1 scores and state-of-the-art models for 2024-2025, you would need to visit the Papers with Code leaderboard directly at the URL referenced in the search results: https://paperswithcode.com/sota/relation-extraction-on-redocred

The search results indicate there are active research efforts on Re-DocRED, including models like GLiDRE mentioned in recent work, but the specific ranking and F1 scores were not accessible in these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50b3fe39-605c-4a9c-986f-719739853e9b",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "76940f9b-078b-49f7-b4c1-41af7497a6fa",
  "sourceToolAssistantUUID": "50b3fe39-605c-4a9c-986f-719739853e9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-11T23:02:42.354Z_

Let me get more specific numbers by fetching key papers and searching for additional details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76940f9b-078b-49f7-b4c1-41af7497a6fa",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawceWrwC8HKg6EnR8pyR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbe08b99-9782-47dd-aae6-d37f6638e605",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uytstxw586Rhc2PJsWS7RB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2102,
      "cache_creation_input_tokens": 6064,
      "cache_read_input_tokens": 23371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6064,
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

_source line 53 · 2026-05-11T23:02:44.316Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PNTNYtGafcwqR5P9z5vFzr`</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2109.06067",
  "prompt": "Extract ALL reported F1 scores from the results tables for ACE05 and SciERC benchmarks. Include Entity F1, Relation F1, and Strict Relation F1 for all models compared. Focus on the main results tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbe08b99-9782-47dd-aae6-d37f6638e605",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawceWrwC8HKg6EnR8pyR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d80c3f9b-f63e-4dc0-a7ce-c30f1f2192ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uytstxw586Rhc2PJsWS7RB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2102,
      "cache_creation_input_tokens": 6064,
      "cache_read_input_tokens": 23371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6064,
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

_source line 54 · 2026-05-11T23:02:45.799Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EZwQBVtd9gR3dZPHG6xp1K`</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2302.08675",
  "prompt": "Extract ALL reported F1 scores from the results tables for DocRED and Re-DocRED benchmarks. Include Ign F1, F1, and Evidence F1 for all models compared. Focus on the main results tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d80c3f9b-f63e-4dc0-a7ce-c30f1f2192ec",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawceWrwC8HKg6EnR8pyR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02d385c1-7bed-4832-aec2-e9ad6e849915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uytstxw586Rhc2PJsWS7RB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2102,
      "cache_creation_input_tokens": 6064,
      "cache_read_input_tokens": 23371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6064,
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

_source line 55 · 2026-05-11T23:02:47.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NJxAE51jvUtZJWW164bSPn`</summary>

```json
{
  "query": "DocRED leaderboard 2024 2025 best model Ign F1 test score KD-DocRE DREEAM SAIS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02d385c1-7bed-4832-aec2-e9ad6e849915",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawceWrwC8HKg6EnR8pyR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f677ff43-69aa-4ef0-8818-ba0db253b7a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uytstxw586Rhc2PJsWS7RB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2102,
      "cache_creation_input_tokens": 6064,
      "cache_read_input_tokens": 23371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6064,
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

_source line 56 · 2026-05-11T23:02:48.768Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CJkjSAPYJ1NkvP6uoHGRoW`</summary>

```json
{
  "url": "https://github.com/tonytan48/Re-DocRED",
  "prompt": "Extract the leaderboard table showing all models and their F1/Ign F1 scores on Re-DocRED. Include all numbers from the results table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f677ff43-69aa-4ef0-8818-ba0db253b7a8",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawceWrwC8HKg6EnR8pyR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75716f28-a17d-4fbe-92d8-402296d78142",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uytstxw586Rhc2PJsWS7RB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2102,
      "cache_creation_input_tokens": 6064,
      "cache_read_input_tokens": 23371,
      "output_tokens": 452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6064
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2102,
          "output_tokens": 452,
          "cache_read_input_tokens": 23371,
          "cache_creation_input_tokens": 6064,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6064,
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

_source line 57 · 2026-05-11T23:02:50.429Z_

<details><summary>↩ Tool result · `toolu_01PNTNYtGafcwqR5P9z5vFzr`</summary>

```text
# F1 Scores from ACE05 and SciERC Results Tables

## ACE05 Results (Table 3)

**With BERT-BASE encoder:**
- Li and Ji (2014): Entity 80.8, Relation 52.1, Strict 49.5
- DYGIE: Entity 88.4, Relation 63.2
- Multi-turn QA: Entity 84.8, Relation 60.2
- OneIE: Entity 88.8, Relation 67.5
- DYGIE++: Entity 88.6, Relation 63.4
- TriMF: Entity 87.6, Relation 66.5, Strict 62.8
- UniRE: Entity 88.8, Strict 64.3
- PURE-F: Entity 90.1, Relation 67.7, Strict 64.8
- PURE-A: Relation 66.5
- **PL-Marker: Entity 89.8, Relation 69.0, Strict 66.5**

**With ALBERT-XXLARGE encoder:**
- TableSeq: Entity 89.5, Relation 67.6, Strict 64.3
- UniRE: Entity 90.2, Strict 66.0
- PURE-F: Entity 90.9, Relation 69.4, Strict 67.0
- **PL-Marker: Entity 91.1, Relation 73.0, Strict 71.1**

## SciERC Results (Table 3)

**With SciBERT encoder:**
- DYGIE: Entity 65.2, Relation 41.6
- DYGIE++: Entity 88.6 (ACE only)
- TriMF: Entity 70.2, Relation 52.4
- UniRE: Entity 68.4, Relation 36.9
- PURE-F: Entity 68.9, Relation 50.1, Strict 36.8
- PURE-A: Relation 48.1
- **PL-Marker: Entity 69.9, Relation 53.2, Strict 41.6**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d80c3f9b-f63e-4dc0-a7ce-c30f1f2192ec",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "98de69aa-6527-469c-a3ac-b5de9f55a088",
  "sourceToolAssistantUUID": "d80c3f9b-f63e-4dc0-a7ce-c30f1f2192ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-11T23:02:51.668Z_

<details><summary>↩ Tool result · `toolu_01CJkjSAPYJ1NkvP6uoHGRoW`</summary>

```text
I cannot extract a leaderboard table with model F1/Ign F1 scores from the provided content, as **no such table is present** in the GitHub repository page.

The page contains:
- Repository metadata (stars, forks, contributors)
- Dataset statistics showing document counts, average triples, entities, and sentences
- Citation information for the EMNLP 2022 paper
- File listings

The actual research paper with results tables would be found at the arxiv link mentioned: https://arxiv.org/pdf/2205.12696.pdf, but that document is not included in the content provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75716f28-a17d-4fbe-92d8-402296d78142",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "e9c94875-08c5-44d0-85b4-11a8d3cafbaa",
  "sourceToolAssistantUUID": "75716f28-a17d-4fbe-92d8-402296d78142",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-11T23:02:53.921Z_

<details><summary>↩ Tool result · `toolu_01EZwQBVtd9gR3dZPHG6xp1K`</summary>

```text
# F1 Scores from DocRED and Re-DocRED Benchmarks

## DocRED Results (Table 2)

### Without Distantly-Supervised Data

**BERTbase:**
- SSAN: Ign F1=57.03, F1=59.19
- ATLOP: Ign F1=59.22, F1=61.09
- E2GRE: Ign F1=55.22, F1=58.72, Evi F1=47.12
- DocuNet: Ign F1=59.86, F1=61.83
- EIDER: Ign F1=60.51, F1=62.48, Evi F1=50.71
- SAIS: Ign F1=59.98, F1=62.96, Evi F1=53.70
- DREEAM (teacher): Ign F1=59.60, F1=61.42, Evi F1=52.08
- DREEAM + Fusion: Ign F1=60.51, F1=62.55

**RoBERTalarge:**
- SSAN: Ign F1=60.25, F1=62.08
- ATLOP: Ign F1=61.32, F1=63.18
- DocuNet: Ign F1=62.23, F1=64.12
- EIDER: Ign F1=62.34, F1=64.27, Evi F1=52.54
- SAIS: Ign F1=62.23, F1=65.17, Evi F1=55.84
- DREEAM (teacher): Ign F1=61.71, F1=63.49, Evi F1=54.15
- DREEAM + Fusion: Ign F1=62.29, F1=64.20

### With Distantly-Supervised Data

**BERTbase:**
- KD-DocRE: Ign F1=63.38, F1=64.81
- DREEAM (student): Ign F1=63.47, F1=65.30, Evi F1=55.68
- DREEAM + Fusion: Ign F1=63.92, F1=65.83

**RoBERTalarge:**
- SSAN: Ign F1=63.76, F1=65.69
- KD-DocRE: Ign F1=65.27, F1=67.12
- DREEAM (student): Ign F1=65.24, F1=67.09, Evi F1=57.55
- DREEAM + Fusion: Ign F1=65.52, F1=67.41

## Re-DocRED Results (Table 6)

### Without Distantly-Supervised Data

- ATLOP: Ign F1=76.82, F1=77.56
- DocuNet: Ign F1=77.26, F1=77.87
- KD-DocRE: Ign F1=77.60, F1=78.28
- DREEAM: Ign F1=77.34, F1=77.94
- DREEAM + Fusion: Ign F1=79.66, F1=80.73

### With Distantly-Supervised Data

- ATLOP: Ign F1=78.52, F1=79.46
- DocuNet: Ign F1=78.52, F1=79.46
- KD-DocRE: Ign F1=80.32, F1=81.04
- DREEAM: Ign F1=78.67, F1=79.35
- DREEAM + Fusion: Ign F1=80.39, F1=81.44
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02d385c1-7bed-4832-aec2-e9ad6e849915",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "c585cb2d-6406-44fe-b3ea-2ebb6a75668d",
  "sourceToolAssistantUUID": "02d385c1-7bed-4832-aec2-e9ad6e849915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-11T23:03:01.978Z_

<details><summary>↩ Tool result · `toolu_01NJxAE51jvUtZJWW164bSPn`</summary>

```text
Web search results for query: "DocRED leaderboard 2024 2025 best model Ign F1 test score KD-DocRE DREEAM SAIS"

Links: [{"title":"F1 2025 Mathematical Driver Rankings | F1 Analysis","url":"https://f1-analysis.com/2025/12/09/f1-2025-mathematical-driver-rankings/"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"POWER RANKINGS final scores for 2025: Where do the drivers rank on the final leaderboard after an exhilarating 2025 season?","url":"https://www.formula1.com/en/latest/article/power-rankings-where-do-the-drivers-rank-on-the-final-leaderboard-after-an.RBWmq73lkM5CKZ0hgztOI"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"2025 F1 Driver Ratings – F1 Mathematical Model","url":"https://f1mathematicalmodel.com/2025/12/20/2025-f1-driver-ratings/"},{"title":"F1 standings 2026 - Formula 1 points","url":"https://www.formula1points.com/season"},{"title":"F1 standings teams 2025 - Formula 1 points","url":"https://www.formula1points.com/season/season-teams/2025"},{"title":"F1 2025 Mid-Season Mathematical Driver Rankings | F1 Analysis","url":"https://f1-analysis.com/2025/07/16/f1-2025-mid-season-mathematical-driver-rankings/"},{"title":"What is F1 Score in Machine Learning?","url":"https://www.analyticsvidhya.com/blog/2025/12/what-is-f1-score-in-machine-learning/"}]

The search results are about Formula 1 racing and general F1 score metrics in machine learning, not about the DocRED dataset. Let me search more specifically for DocRED:

Links: [{"title":"thunlp/docred · Datasets at Hugging Face","url":"https://huggingface.co/datasets/thunlp/docred"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"},{"title":"GitHub - thunlp/DocRED: Dataset and codes for ACL 2019 DocRED: A Large-Scale Document-Level Relation Extraction Dataset. · GitHub","url":"https://github.com/thunlp/DocRED"},{"title":"DocRED Benchmark (Relation Extraction)","url":"https://paperswithcode.com/sota/relation-extraction-on-docred"},{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.132/"},{"title":"Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/html/2205.12696"},{"title":"(PDF) DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://www.researchgate.net/publication/333815327_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/abs/1906.06127"}]

Now let me search more specifically for recent leaderboard results with the models you mentioned:

Links: [{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://ar5iv.labs.arxiv.org/html/2302.08675"},{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"DREEAM: Guiding Attention with Evidence for Improving ...","url":"https://aclanthology.org/2023.eacl-main.145.pdf"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/html/2407.21384"},{"title":"Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/html/2205.12696"},{"title":"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/362262962_SAIS_Supervising_and_Augmenting_Intermediate_Steps_for_Document-Level_Relation_Extraction"},{"title":"Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-026-12099-8"},{"title":"Building a Japanese Document-Level Relation Extraction Dataset Assisted by Cross-Lingual Transfer","url":"https://arxiv.org/html/2404.16506"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757"}]

Let me search for more recent 2024-2025 leaderboard results:

Links: [{"title":"DocRED Benchmark (Relation Extraction)","url":"https://paperswithcode.com/sota/relation-extraction-on-docred"},{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"Papers with Code - DocRED Dataset","url":"https://paperswithcode.com/dataset/docred"},{"title":"An Exploratory Study of Foundation Model Leaderboards","url":"https://www.computer.org/csdl/journal/ts/2025/04/10855627/23QQWoayUFy"},{"title":"Papers with Code is Dead — Best Alternatives 2026 by Use Case | Codesota | CodeSOTA","url":"https://www.codesota.com/papers-with-code"},{"title":"DocRED: A Large-Scale Document-Level Relation ...","url":"https://paperswithcode.com/paper/docred-a-large-scale-document-level-relation"},{"title":"Papers with code · GitHub","url":"https://github.com/paperswithcode"},{"title":"Trending Papers - Hugging Face","url":"https://paperswithcode.com/"},{"title":"Re-DocRED Dataset","url":"https://paperswithcode.com/dataset/re-docred"},{"title":"thunlp/docred · Datasets at Hugging Face","url":"https://huggingface.co/datasets/thunlp/docred"}]

Based on my search results, I can provide you with information about the DocRED leaderboard and the models you mentioned:

## DocRED Leaderboard Information

DocRED is the largest human-annotated dataset for document-level relation extraction from plain text, constructed from Wikipedia and Wikidata.

### Key Models and Performance:

**KD-DocRE:** KD-DocRE's model consistently outperforms strong baselines and its performance exceeds the previous SOTA by 1.36 F1 and 1.46 Ign_F1 score on the DocRED leaderboard (as of 2022).

**DREEAM:** When adopting BERTbase as the PLM encoder, DREEAM performs better than KD-DocRE, the previous state-of-the-art system, by 0.6/1.0 points on Ign F1/F1 for the development set. On the test set, the improvement reaches 1.1 F1 points on both Ign F1 and F1 (2023).

**SAIS:** Although there is a performance gap between DREEAM and SAIS, the difference is attributed to the difference in supervisory signals. SAIS enhances RE by explicitly supervising intermediate steps through four tasks: Coreference Resolution, Entity Typing, Pooled Evidence Retrieval, and Fine-grained Evidence Retrieval.

### Recent Developments:

The DocRED dataset is incompletely annotated with more than 60% of the triples not annotated in the evaluation split. Models trained and evaluated on Re-DocRED (a revised version) gain around 13 F1 compared to DocRED.

Note: Meta shut down Papers with Code in July 2025, and the leaderboards are now gone, though the Re-DocRED leaderboard was previously hosted on that platform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f677ff43-69aa-4ef0-8818-ba0db253b7a8",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "75d299d1-c8ee-4151-b71a-be23865558f8",
  "sourceToolAssistantUUID": "f677ff43-69aa-4ef0-8818-ba0db253b7a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-11T23:03:04.626Z_

Let me fetch more details on the latest models and the grounded extraction paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75d299d1-c8ee-4151-b71a-be23865558f8",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcg9jWFa8qqzHirGmjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1da0eec0-9f8c-419f-a243-8baef4b12182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAbxBKVjbFm2BH9aZBJgEt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 169,
      "cache_creation_input_tokens": 6615,
      "cache_read_input_tokens": 29435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6615,
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

_source line 62 · 2026-05-11T23:03:07.013Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JnBw6F5gFTWPXS5FnPi4n9`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.00757",
  "prompt": "Extract ALL reported F1 scores from the results tables for DocRED and Re-DocRED benchmarks. Include Ign F1, F1 for all models and settings (few-shot, full). List every model name and its scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1da0eec0-9f8c-419f-a243-8baef4b12182",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcg9jWFa8qqzHirGmjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38b0d1af-3235-4b04-8258-92110293c18d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAbxBKVjbFm2BH9aZBJgEt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 169,
      "cache_creation_input_tokens": 6615,
      "cache_read_input_tokens": 29435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6615,
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

_source line 63 · 2026-05-11T23:03:08.457Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E11tHzH3QMTYQdQWFv2vQM`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.06529",
  "prompt": "Extract the full title, authors, year, and ALL reported F1 scores from the results tables on DocRED and Re-DocRED. Include Ign F1, F1, and Evidence F1 for all models compared."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38b0d1af-3235-4b04-8258-92110293c18d",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcg9jWFa8qqzHirGmjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5064ac1f-3b42-404e-9e3c-f5d209d362e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAbxBKVjbFm2BH9aZBJgEt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 169,
      "cache_creation_input_tokens": 6615,
      "cache_read_input_tokens": 29435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6615,
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

_source line 64 · 2026-05-11T23:03:09.367Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EiZdMybDekUsZW1hYZbSLJ`</summary>

```json
{
  "query": "ACE05 event extraction state of the art 2024 2025 trigger argument F1 OneIE DEGREE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5064ac1f-3b42-404e-9e3c-f5d209d362e3",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcg9jWFa8qqzHirGmjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e420cc8e-79f1-4338-9368-d801d3cc54c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAbxBKVjbFm2BH9aZBJgEt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 169,
      "cache_creation_input_tokens": 6615,
      "cache_read_input_tokens": 29435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6615,
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

_source line 65 · 2026-05-11T23:03:10.354Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013n2uk8wCgTE7qxRs5inwuD`</summary>

```json
{
  "query": "\"grounded knowledge graph extraction\" \"anchor-constrained\" provenance tracking LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e420cc8e-79f1-4338-9368-d801d3cc54c0",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcg9jWFa8qqzHirGmjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "503de3d6-c238-4c99-9e34-57b443e65e74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAbxBKVjbFm2BH9aZBJgEt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 169,
      "cache_creation_input_tokens": 6615,
      "cache_read_input_tokens": 29435,
      "output_tokens": 387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 169,
          "output_tokens": 387,
          "cache_read_input_tokens": 29435,
          "cache_creation_input_tokens": 6615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6615,
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

_source line 66 · 2026-05-11T23:03:14.055Z_

<details><summary>↩ Tool result · `toolu_01E11tHzH3QMTYQdQWFv2vQM`</summary>

```text
# CDER: Document-Level Relation Extraction Study

**Title:** "CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction"

**Authors:** Khai Phan Tran, Xue Li

**Year:** 2025 (arxiv submission date: April 6, 2025)

**Institution:** School of Electrical Engineering and Computer Science, The University of Queensland

## DocRED Results Summary

The paper reports results only on the **DocRED dataset**. No Re-DocRED results are included.

### Development Set Performance (Table 1)

| Model | Ign F1 | F1 | Evi F1 |
|-------|--------|-----|---------|
| EIDER + CDER | 60.31±0.10 | 62.32±0.07 | 52.92±0.11 |
| DREEAM + CDER | 60.42±0.03 | 62.42±0.02 | 52.86±0.10 |

### Test Set Performance (Table 1)

| Model | Ign F1 | F1 | Evi F1 |
|-------|--------|-----|---------|
| EIDER + CDER | 59.98 | 62.33 | 52.89 |
| DREEAM + CDER | 60.22 | 62.45 | 53.03 |

### Evidence Retrieval on Positive Pairs (Table 2)

- **CDER Pos Evi F1:** 84.75±0.05 (development set)
- Improvement over DREEAM: +0.11 points
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5064ac1f-3b42-404e-9e3c-f5d209d362e3",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "241d2e42-f100-4caa-9ef9-8167ddb8099c",
  "sourceToolAssistantUUID": "5064ac1f-3b42-404e-9e3c-f5d209d362e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-11T23:03:15.638Z_

<details><summary>↩ Tool result · `toolu_01JnBw6F5gFTWPXS5FnPi4n9`</summary>

```text
# F1 Scores from Re-DocRED and Related Benchmarks

## Low-Resource Supervised Setting (Table 1)

| Model | N=1 | N=5 | N=10 | N=50 | N=100 | N=500 | N=1000 |
|-------|-----|-----|------|------|-------|-------|--------|
| ATLOP | 4.32±3.19 | 18.76±4.93 | 29.48±3.91 | 50.36±1.18 | 57.17±0.37 | 68.91±0.43 | 71.70±0.20 |
| DREEAM | 4.27±3.50 | 16.02±7.46 | 27.07±5.81 | 52.05±2.00 | 58.14±0.86 | 69.32±0.31 | 71.67±0.32 |
| GLiDRE | 24.45±6.37 | 33.71±6.11 | 41.73±2.94 | 54.54±1.39 | 60.04±0.50 | 69.26±0.37 | 72.09±0.31 |

## Fully Supervised Setting (Table 3 - Re-DocRED)

| Model | Dev F1 | Dev Ign F1 | Test F1 | Test Ign F1 |
|-------|--------|-----------|---------|------------|
| ATLOP | 76.15±0.23 | 75.88±0.23 | 77.81±0.71 | 76.13±0.28 |
| KD-DocRE | 77.88±0.42 | 77.12±0.49 | 78.28±0.72 | 77.60±0.25 |
| TTM-RE | 78.13±0.12 | 78.05±0.17 | 79.95±0.13 | 78.20±0.34 |
| DREEAM | 79.42±0.18 | 78.36±0.19 | 80.20±0.45 | 78.56±0.39 |
| LMRC (LLaMA2-13B) | — | — | 74.63 | 74.08 |
| GLiREL | — | — | 54.13 | 53.24 |
| GLiDRE | 77.76±0.35 | 76.70±0.37 | 77.83±0.23 | 76.80±0.22 |

## Zero-Shot Setting (Table 4 - Re-DocRED)

| Model | Dev F1 | Dev Ign F1 | Test F1 | Test Ign F1 |
|-------|--------|-----------|---------|------------|
| Qwen 2.5 72B | 18.24 | 18.09 | 18.00 | 17.86 |
| Llama 3.3 70B | 15.67 | 15.57 | 15.81 | 15.71 |
| Mistral-Large 123B | 18.49 | 18.33 | 18.61 | 18.50 |
| Mistral-Small 24B | 14.39 | 14.27 | 14.38 | 14.27 |
| GPT-3.5 Turbo | — | — | 6.68 | — |
| GLiDRE | 16.72 | 16.37 | 17.32 | 16.41 |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38b0d1af-3235-4b04-8258-92110293c18d",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "82da07ea-7c30-4b7b-81ae-a75f86c10719",
  "sourceToolAssistantUUID": "38b0d1af-3235-4b04-8258-92110293c18d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-11T23:03:16.838Z_

<details><summary>↩ Tool result · `toolu_01EiZdMybDekUsZW1hYZbSLJ`</summary>

```text
Web search results for query: "ACE05 event extraction state of the art 2024 2025 trigger argument F1 OneIE DEGREE"

Links: [{"title":"Closed-Domain Event Extraction Literature Review January 2025 v1.0","url":"https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf"},{"title":"arXiv:2408.16932v1 [cs.CL] 29 Aug 2024 Event Extraction for Portuguese:","url":"https://arxiv.org/pdf/2408.16932"},{"title":"DEGAP: Dual Event-Guided Adaptive Prefixes for Templated-Based Event Argument Extraction with Slot Querying","url":"https://arxiv.org/html/2405.13325"},{"title":"[2408.16932] Event Extraction for Portuguese: A QA-driven Approach using ACE-2005","url":"https://arxiv.org/abs/2408.16932"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"},{"title":"XLLM ACL 2025 Shared Task-II: Speech Event Extraction","url":"https://xllms.github.io/SpeechEE/"},{"title":"Event Extraction for Portuguese: A QA-driven Approach using ACE-2005 | OpenReview","url":"https://openreview.net/forum?id=BGVylhQ1CO"},{"title":"DEGAP: Dual Event-Guided Adaptive Prefixes for Templated-Based Event Argument Extraction Model with Slot Querying","url":"https://arxiv.org/html/2405.13325v1"},{"title":"Bi-directional feature learning-based approach for zero-shot event argument extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325001402"},{"title":"KC-GEE: knowledge-based conditioning for generative event extraction | World Wide Web | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11280-023-01216-5"}]

Based on the search results, I found relevant information about ACE05 event extraction research and state-of-the-art approaches. Here are the key findings:

## Recent State-of-the-Art Results on ACE05

Using retrieval-augmented examples (RAE), a prompting method achieves the highest F1 score of 81.1 for trigger classification (TC) on the ACE-2005 dataset according to recent 2024 research.

### Key Methods and Performance Improvements

**DEGAP Method:** A recent approach improves the argument classification (Arg-C) F1 score by 1.0% on ACE05 compared to previous state-of-the-art, achieving new SOTA results through dual event-guided adaptive prefixes.

**BiTer Method:** BiTer achieves state-of-the-art performance on ACE2005 in the zero-shot setting, outperforming the baseline model by 0.4% F1.

### Important Evaluation Considerations

Recent research identifies a precision issue in the standard argument classification (AC) definition: if there are multiple event triggers of the same type, the standard AC definition doesn't distinguish whether an identified argument belongs to the correct trigger, prompting researchers to introduce AC+ evaluation.

Reports show significant variation in performance on ACE-2005 for argument classification across different approaches, while some studies report the highest F1 scores for trigger classification.

The search results mention OneIE as a foundational method in the event extraction literature, though specific 2024-2025 performance metrics for OneIE and DEGREE on ACE05 weren't prominently detailed in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e420cc8e-79f1-4338-9368-d801d3cc54c0",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "27b6a1e0-e87a-4a6f-be57-8807c5cae04a",
  "sourceToolAssistantUUID": "e420cc8e-79f1-4338-9368-d801d3cc54c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-11T23:03:18.277Z_

<details><summary>↩ Tool result · `toolu_013n2uk8wCgTE7qxRs5inwuD`</summary>

```text
Web search results for query: ""grounded knowledge graph extraction" "anchor-constrained" provenance tracking LLM 2025 2026"

Links: [{"title":"Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking","url":"https://www.mdpi.com/2073-431X/15/3/178"},{"title":"Grounding LLM Reasoning with Knowledge Graphs","url":"https://arxiv.org/html/2502.13247v3"},{"title":"[2502.13247] Grounding LLM Reasoning with Knowledge Graphs","url":"https://arxiv.org/abs/2502.13247"},{"title":"Grounding LLM Reasoning with Knowledge Graphs | OpenReview","url":"https://openreview.net/forum?id=2OPS6uhnw6"},{"title":"Ontology-Grounded LLM Construction","url":"https://www.emergentmind.com/topics/ontology-grounded-llm-construction"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/html/2510.20345v1"},{"title":"Grounding LLM Reasoning with Knowledge Graphs - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2502.13247"},{"title":"GitHub - zjukg/KG-LLM-Papers: [Paper List] Papers integrating knowledge graphs (KGs) and large language models (LLMs) · GitHub","url":"https://github.com/zjukg/kg-llm-papers"},{"title":"[2410.13080] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080"},{"title":"OntoLLM: Enhancing LLM grounding and digression prevention with ontologies and knowledge graphs - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417426004185"}]

The search successfully retrieved relevant results on grounded knowledge graph extraction with anchor-constrained approaches and provenance tracking. Here are the key findings:

## Primary Finding: AEVS Framework

The most directly relevant result is the Anchor-Extraction-Verification-Supplement (AEVS) framework, which grounds every triplet element to the source text. AEVS operates in three stages: anchor discovery identifies entities, relation phrases, and attribute values with precise positions forming a constrained extraction vocabulary; grounded extraction generates triplets linked to discovered anchors; and restoration-based verification validates triplets through hierarchical matching, with a coverage-aware supplement ensuring comprehensive extraction.

## Addressing the Hallucination Problem

LLMs frequently hallucinate—generating plausible triplets unsupported by the source text. The root cause is the lack of provenance: existing methods produce triplets without explicit links to their textual origins, making faithfulness unverifiable. Ablation studies confirm that anchor-based constraints are the primary mechanism for hallucination reduction.

## Recent Publication

The paper was published on March 9, 2026, with submission received January 13, 2026.

## Performance Metrics

Experiments on WebNLG, REBEL, and Wiki-NRE demonstrate consistent improvements over both trained models and LLM-based baselines. Computational analysis shows 2.83–4.28 LLM calls per sample with hallucination rates of 0.23–20.23% across model–dataset configurations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "503de3d6-c238-4c99-9e34-57b443e65e74",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "a7ced29a-6533-43ad-86a9-875f558c5e82",
  "sourceToolAssistantUUID": "503de3d6-c238-4c99-9e34-57b443e65e74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-11T23:03:22.846Z_

Now let me get the remaining details on ACE05 event extraction numbers and any more recent 2025 work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7ced29a-6533-43ad-86a9-875f558c5e82",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawchMP1uZ2MVGPpZXjW3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bc7d62f-d778-4abf-a333-9745558932e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TnxUcbfxSjMBvJhrURr8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3812,
      "cache_read_input_tokens": 36050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3812,
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

_source line 71 · 2026-05-11T23:03:25.514Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QUkJ49CshXoEhYXBaBFnb4`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.19537v1",
  "prompt": "Extract the state-of-the-art results tables for ACE05 event extraction. Include Trigger Identification (TI), Trigger Classification (TC), Argument Identification (AI), and Argument Classification (AC) F1 scores for all models listed. Focus on the leaderboard/comparison tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bc7d62f-d778-4abf-a333-9745558932e7",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawchMP1uZ2MVGPpZXjW3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a72c133d-1647-4c05-880d-f360634c8288",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TnxUcbfxSjMBvJhrURr8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3812,
      "cache_read_input_tokens": 36050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3812,
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

_source line 72 · 2026-05-11T23:03:26.296Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014N1hzwBnFKuai3Ein6LZMP`</summary>

```json
{
  "query": "SciERC NER entity recognition best model F1 2024 2025 SciBERT SpanBERT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a72c133d-1647-4c05-880d-f360634c8288",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawchMP1uZ2MVGPpZXjW3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e20fe742-e6e9-4eb7-ad1e-b5200e1a53cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TnxUcbfxSjMBvJhrURr8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3812,
      "cache_read_input_tokens": 36050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3812,
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

_source line 73 · 2026-05-11T23:03:26.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TXoVDa8Hhwm8AzpBVaTdbe`</summary>

```json
{
  "query": "\"document-level relation extraction\" \"evidence prediction\" joint model 2025 DocRED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e20fe742-e6e9-4eb7-ad1e-b5200e1a53cd",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawchMP1uZ2MVGPpZXjW3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd477770-4e7b-4df1-b8bd-15917693e629",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TnxUcbfxSjMBvJhrURr8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3812,
      "cache_read_input_tokens": 36050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3812,
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

_source line 74 · 2026-05-11T23:03:30.523Z_

<details><summary>↩ Tool result · `toolu_01QUkJ49CshXoEhYXBaBFnb4`</summary>

```text
# State-of-the-Art Results for ACE05 Event Extraction

Based on the survey document, **Table I** provides performance comparisons across different methodological paradigms. Here are the key results:

## Performance Metrics by Category

**Classic ML Methods:**
- Cross-Event Inference (2010): Trigger Classification F1 = 68.8%, Argument Classification F1 = 44.6%
- JointBeam (2013): Trigger ID F1 = 70.4%, Trigger Classification F1 = 67.5%, Argument ID F1 = 56.8%, Argument Classification F1 = 52.7%

**Deep Learning Methods:**
- JMEE (2018): Trigger ID F1 = 75.9%, Trigger Classification F1 = 73.7%, Argument ID F1 = 68.4%, Argument Classification F1 = 60.3%

**Pretrained Language Models:**
- PLMEE (2019): Trigger ID F1 = 84.2%, Trigger Classification F1 = 80.7%, Argument ID F1 = 65.3%, Argument Classification F1 = 58.0%
- DyGIE++ (2019): Trigger Classification F1 = 69.7%, Argument ID F1 = 55.4%, Argument Classification F1 = 52.5%

The progression demonstrates substantial improvements from traditional machine learning through transformer-based models, with PLMEE achieving the highest reported trigger classification scores at 84.2% F1.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a72c133d-1647-4c05-880d-f360634c8288",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "5512276d-b5a2-4d79-bd0b-a0060620d98e",
  "sourceToolAssistantUUID": "a72c133d-1647-4c05-880d-f360634c8288",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-11T23:03:32.297Z_

<details><summary>↩ Tool result · `toolu_01TXoVDa8Hhwm8AzpBVaTdbe`</summary>

```text
Web search results for query: ""document-level relation extraction" "evidence prediction" joint model 2025 DocRED"

Links: [{"title":"[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200812283H/abstract"},{"title":"Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"},{"title":"(PDF) DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://www.researchgate.net/publication/333815327_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED | Request PDF","url":"https://www.researchgate.net/publication/343931511_Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED | DeepAI","url":"https://deepai.org/publication/entity-and-evidence-guided-relation-extraction-for-docred"},{"title":"Document-level Relation Extraction via Separate Relation Representation and Logical Reasoning | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3597610"},{"title":"thunlp/docred · Datasets at Hugging Face","url":"https://huggingface.co/datasets/thunlp/docred"},{"title":"[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED - Paper Detail","url":"https://deeplearn.org/arxiv/153393/entity-and-evidence-guided-relation-extraction-for-docred"}]

Based on the search results, I found relevant information about document-level relation extraction with evidence prediction on DocRED:

## Key Findings

The E2GRE (Entity and Evidence Guided Relation Extraction) framework is a joint training approach for document-level relation extraction. It introduces entity-guided sequences as inputs to a pre-trained language model (e.g., BERT, RoBERTa), which help the language model focus on areas of the document related to the entity. 

The approach guides the fine-tuning of the pre-trained language model by using its internal attention probabilities as additional features for evidence prediction. This approach achieved state-of-the-art results on the public leaderboard across all metrics, demonstrating that E2GRE is both effective and synergistic on relation extraction and evidence prediction.

Another notable approach is the Enhancing Cross-evidence Reasoning Graph (ECRG) model for document-level relation extraction, which uses a center-sentence based evidence extraction rule to pre-extract higher-quality evidence. This evidence is constructed into evidence graphs to mine connections between mentions within the same evidence, and entity-level graphs are constructed by aggregating mentions from the same entities.

Note: The search results primarily contain works from 2019-2020 rather than recent 2025 publications. For more recent 2025-specific research on this topic, you may want to search directly on arxiv.org or recent conference proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd477770-4e7b-4df1-b8bd-15917693e629",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "52b7d4ce-e0aa-4f9a-baf5-b2432d5cbe23",
  "sourceToolAssistantUUID": "dd477770-4e7b-4df1-b8bd-15917693e629",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-11T23:03:32.920Z_

<details><summary>↩ Tool result · `toolu_014N1hzwBnFKuai3Ein6LZMP`</summary>

```text
Web search results for query: "SciERC NER entity recognition best model F1 2024 2025 SciBERT SpanBERT"

Links: [{"title":"Enhancing named entity recognition in low-resource scenarios using diffusion variational autoencoder and knowledge graphs | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-025-00314-w"},{"title":"Full article: An entity and relation extraction model based on context query and axial attention towards patent texts","url":"https://www.tandfonline.com/doi/full/10.1080/09540091.2024.2426816"},{"title":"Trusted Knowledge Extraction for Operations and Maintenance Intelligence","url":"https://arxiv.org/html/2507.22935v3"},{"title":"A diffusion enhanced CRF and BiLSTM framework for accurate entity recognition | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-04036-x"},{"title":"A review of named entity recognition: from learning ...","url":"https://sentic.net/named-entity-recognition.pdf"},{"title":"[2203.14710] Hierarchical Transformer Model for Scientific Named Entity Recognition","url":"https://ar5iv.labs.arxiv.org/html/2203.14710"},{"title":"Evaluating LLMs for Named Entity Recognition in Scientific ...","url":"https://ceur-ws.org/Vol-3979/paper1.pdf"},{"title":"What Is Named Entity Recognition (NER)? Complete Guide 2026","url":"https://www.articsledge.com/post/named-entity-recognition-ner"},{"title":"Best Models For Entity Recognition | Restackio","url":"https://www.restack.io/p/entity-recognition-best-models-answer-cat-ai"},{"title":"A review of named entity recognition: from learning methods to modelling paradigms and tasks | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11321-8"}]

I've found several relevant results about SciERC NER entity recognition performance. Here's what I discovered:

## Recent Performance Results on SciERC

A diffusion enhanced CRF and BiLSTM model achieved an F1 score of 69.97% on SciERC with precision of 67.39% and recall of 72.85% (published June 2025).

A hierarchical transformer model achieved 70.91 on F1-micro on SciERC while SPERT, the previous state of the art, achieved 70.33 (as of March 2024).

## SciBERT Performance

On SciERC, a hierarchical transformer model was able to surpass SciBERT by a significant margin (+2 on F1-macro).

## Additional Approaches (2024-2025)

A context query and axial attention-based model achieved an F1 value of 41.8% on the SciERC dataset (published November 2024).

A DV-KG-NER model was assessed on SciERC and compared against recent transformer-based models (XLNet, RoBERTa, T5, ERNIE, DeBERTaV3) and diffusion methods (published October 2025).

The search results show that the best-performing models on SciERC in 2024-2025 are achieving F1 scores in the range of **69.97%-70.91%**, with hierarchical transformer-based approaches and diffusion-enhanced CRF+BiLSTM models representing the current state-of-the-art.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e20fe742-e6e9-4eb7-ad1e-b5200e1a53cd",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "2d82d6a6-350e-47fd-b3d1-5ac2263deae4",
  "sourceToolAssistantUUID": "e20fe742-e6e9-4eb7-ad1e-b5200e1a53cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-11T23:03:36.786Z_

Let me get a few more details on the latest ACE05 event extraction numbers and the AEVS paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d82d6a6-350e-47fd-b3d1-5ac2263deae4",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawciS2qKsaRR6rs1Yg75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a1c7d87-2b32-439d-90f4-31717c2606ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015x4Q8YPUYqbh5YxTXqgosv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 39862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1603,
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

_source line 78 · 2026-05-11T23:03:37.741Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rz8ofLUYHm6MSe891zR4BA`</summary>

```json
{
  "query": "ACE05 event extraction OneIE DEGREE TextEE SOTA F1 trigger argument 2024 2025 best results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a1c7d87-2b32-439d-90f4-31717c2606ca",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawciS2qKsaRR6rs1Yg75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b253a1b2-98ad-4970-b5ca-c483157d303b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015x4Q8YPUYqbh5YxTXqgosv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 39862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1603,
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

_source line 79 · 2026-05-11T23:03:40.522Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WX1HY1JynNG6J4VBKaVGNc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.21384",
  "prompt": "Extract the title, authors, and all reported F1 scores on DocRED for GEGA and compared models. Include Ign F1, F1, and Evi F1."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b253a1b2-98ad-4970-b5ca-c483157d303b",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawciS2qKsaRR6rs1Yg75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fec1c654-841c-460e-b946-857f437a2d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015x4Q8YPUYqbh5YxTXqgosv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 39862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1603,
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

_source line 80 · 2026-05-11T23:03:40.606Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PdQPDKSDjXNHQpbYSGgFms`</summary>

```json
{
  "query": "\"faithful information extraction\" \"source attribution\" \"evidence grounding\" NLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fec1c654-841c-460e-b946-857f437a2d6b",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawciS2qKsaRR6rs1Yg75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75758c04-a13c-400f-adef-7612528d8ca6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015x4Q8YPUYqbh5YxTXqgosv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 39862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1603,
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

_source line 81 · 2026-05-11T23:03:43.878Z_

<details><summary>↩ Tool result · `toolu_01WX1HY1JynNG6J4VBKaVGNc`</summary>

```text
# GEGA Paper Information

**Title:** "GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction"

**Authors:** Yanxu Mao, Xiaohui Chen, Peipei Liu, Tiehan Cui, Zuhui Yue, and Zheng Li

**F1 Scores on DocRED:**

Unfortunately, the webpage content provided does not include specific F1 score metrics for GEGA or comparison models. While the abstract mentions that "experimental results indicate that our model has achieved comprehensive improvements compared to the existing SOTA model," the actual numerical results for Ign F1, F1, and Evi F1 scores are not displayed on this arXiv abstract page.

To obtain these specific performance metrics, you would need to access the full PDF or HTML version of the paper using the links provided on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fec1c654-841c-460e-b946-857f437a2d6b",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "40c635da-ccbc-420b-a2f0-2697eab62001",
  "sourceToolAssistantUUID": "fec1c654-841c-460e-b946-857f437a2d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-11T23:03:44.795Z_

<details><summary>↩ Tool result · `toolu_01Rz8ofLUYHm6MSe891zR4BA`</summary>

```text
Web search results for query: "ACE05 event extraction OneIE DEGREE TextEE SOTA F1 trigger argument 2024 2025 best results"

Links: [{"title":"Closed-Domain Event Extraction Literature Review January 2025 v1.0","url":"https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf"},{"title":"GitHub - jeremytanjianle/event-extraction-oneie: Event extraction of ACE05 dataset","url":"https://github.com/jeremytanjianle/event-extraction-oneie"},{"title":"DEGREE: A Data-Efficient Generation-Based Event Extraction Model","url":"https://openreview.net/pdf?id=3eNATGzQIK7"},{"title":"Event Extraction as Question Generation and Answering","url":"https://aclanthology.org/2023.acl-short.143.pdf"},{"title":"A Data-Efficient Generation-Based Event Extraction Model","url":"https://aclanthology.org/2022.naacl-main.138.pdf"},{"title":"GitHub - ZUCC-AI/UMIE: Code and model for AAAI 2024: UMIE: Unified Multimodal Information Extraction with Instruction Tuning","url":"https://github.com/ZUCC-AI/UMIE"},{"title":"event-extraction-oneie/ONEIE demo.ipynb at main · jeremytanjianle/event-extraction-oneie","url":"https://github.com/jeremytanjianle/event-extraction-oneie/blob/main/ONEIE%20demo.ipynb"},{"title":"TextEE: A Standardized, Fair, and Reproducible Benchmark for Event Extraction","url":"https://khhuang.me/TextEE/"},{"title":"GitHub - PlusLabNLP/DEGREE: Code for our NAACL-2022 paper DEGREE: A Data-Efficient Generation-Based Event Extraction Model.","url":"https://github.com/pluslabnlp/degree"},{"title":"GEMS: Generation-Based Event Argument Extraction via ...","url":"https://aclanthology.org/2025.findings-acl.1353.pdf"}]

I've successfully searched for information about ACE05 event extraction models and their performance metrics. Here are the key findings:

## ACE05 Event Extraction Models and SOTA Results

Research from 2024 evaluates approaches on ACE-2005 for sentence-level event extraction, finding improvements in F1 scores for both trigger detection and argument classification for supervised models OneIE and DEGREE.

### Key Models Mentioned:

1. **OneIE** - OneIE achieved an F1 score of 74.7% in referenced benchmarks.

2. **DEGREE** - DEGREE is a data-efficient generation-based event extraction model from NAACL 2022.

3. **TextEE** - TextEE was released as a standardized, fair, and reproducible benchmark in November 2023, and it supports the CEDAR approach as of February 2024.

### Performance Considerations:

Some recent studies report F1 scores on ACE-2005 for argument classification that are significantly lower than SOTA supervised models, whereas others report the highest F1 scores on ACE-2005 for trigger classification.

Recent research identifies a lack of precision in the standard definition of argument classification: if there are multiple event triggers in the input text which belong to the same event type, the standard definition does not distinguish whether an identified argument belongs to the correct event trigger.

The search results show that ACE05 event extraction remains an active research area with multiple approaches being evaluated and improved through 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b253a1b2-98ad-4970-b5ca-c483157d303b",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "26c7204c-6a07-4140-938e-cc4e0b2455fa",
  "sourceToolAssistantUUID": "b253a1b2-98ad-4970-b5ca-c483157d303b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-11T23:03:50.029Z_

<details><summary>↩ Tool result · `toolu_01PdQPDKSDjXNHQpbYSGgFms`</summary>

```text
Web search results for query: ""faithful information extraction" "source attribution" "evidence grounding" NLP 2025"

Links: [{"title":"CiteGuard: Faithful Citation Attribution for LLMs via Retrieval-Augmented Validation","url":"https://arxiv.org/html/2510.17853v1"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Dependency Matters: Enhancing LLM Reasoning with Explicit Knowledge Grounding","url":"https://openreview.net/pdf?id=DlkM0q4Cvk"},{"title":"[Quick Review] CiteGuard: Faithful Citation Attribution for LLMs via\\n Retrieval-Augmented Validation","url":"https://liner.com/review/citeguard-faithful-citation-attribution-for-llms-via-retrievalaugmented-validation"},{"title":"Faithful Fact Decomposition in NLP","url":"https://www.emergentmind.com/topics/faithful-context-enhanced-fact-decomposition"},{"title":"Research article When automated fact-checking meets","url":"https://hal.science/hal-05017906/file/wang-et-al-2025-when-automated-fact-checking-meets-argumentation-unveiling-fake-news-through-argumentative-evidence.pdf"},{"title":"FACTS Grounding Benchmark Overview","url":"https://www.emergentmind.com/topics/facts-grounding-benchmark"},{"title":"FACTS Grounding: A new benchmark for evaluating the factuality of large language models — Google DeepMind","url":"https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/"},{"title":"The 15th International Conference on Recent Advances in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/ranlp-2025/"},{"title":"Google langextract: Advanced Language Detection in Python","url":"https://www.thepurplestruct.com/blog/google-langextract-advanced-language-detection-in-python"}]

Based on the search results, here's an overview of recent work on faithful information extraction, source attribution, and evidence grounding in NLP for 2025:

## Key Research Areas

**Citation Attribution and Grounding:**
CiteGuard proposes an agent that provides more faithful and generalizable citation attribution through retrieval-augmented validation. When integrated with open-source models like DeepSeek-R1 and Kimi-K2, CiteGuard achieves accuracy reaching up to 65.4% and 60.0% respectively, which closely approaches human-level performance of 69.7%, demonstrating that the framework is robust and model-agnostic.

**Evidence Grounding Benchmarks:**
The FACTS Grounding Benchmark is an evaluation framework and leaderboard that measures the ability of LLMs to generate long-form responses that are factually accurate and strictly grounded in a supplied context document, emphasizing high-fidelity attribution in extended-generation scenarios. Each prompt in the benchmark contains a user request paired with a full-length document (up to 32k tokens) and demands output that not only meets the user's informational needs but also adheres to stringent constraints: all substantive claims must be directly supported by the provided context, and no extraneous knowledge may be introduced.

**Knowledge Grounding in Reasoning:**
Grounding each reasoning step in intrinsic knowledge ensures accurate and reliable extraction, improves interpretability, anchors reasoning in known facts, and enables consistency checks.

**Fact Decomposition with Attribution:**
Systems such as FIDES introduce a two-stage pipeline, initially segmenting answers into sentences with explicit coreference resolution, then further decomposing each sentence into atomic sub-facts, with these atomic claims serving as queries for evidence retrieval.

**Information Extraction Tools:**
Grounded extraction maps every entity to exact text offsets for traceability, a capability now featured in tools like Google's LangExtract library released in July 2025.

These advances collectively address the critical challenge of ensuring NLP systems produce outputs that are verifiable, traceable, and grounded in source documents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75758c04-a13c-400f-adef-7612528d8ca6",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "1ba72c1d-f04d-4f6c-ae01-909efd0bdc21",
  "sourceToolAssistantUUID": "75758c04-a13c-400f-adef-7612528d8ca6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-11T23:03:54.403Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017cBrZmGZmtYYPjSvt4HfRG`</summary>

```json
{
  "url": "https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf",
  "prompt": "Extract the state-of-the-art results on ACE05 for event extraction. List ALL models with their Trigger Identification F1, Trigger Classification F1, Argument Identification F1, and Argument Classification F1 scores. Focus on the comparison tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ba72c1d-f04d-4f6c-ae01-909efd0bdc21",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcjh9xHxBevifkQfbu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "986ad7c8-d64b-4b2c-b733-3d68afcb70d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PaUuwuYd5wbuZDa7G4gUfb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3433,
      "cache_read_input_tokens": 41465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3433,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-11T23:03:55.518Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V7CsTKKnfxmZEBnCL1SwcV`</summary>

```json
{
  "query": "DocRED Re-DocRED 2025 newest model GEGA CDER evidence F1 Ign test results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "986ad7c8-d64b-4b2c-b733-3d68afcb70d8",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011Cawcjh9xHxBevifkQfbu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc4f4515-9fdf-4bac-89d7-4627d5d72583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PaUuwuYd5wbuZDa7G4gUfb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3433,
      "cache_read_input_tokens": 41465,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3433
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 41465,
          "cache_creation_input_tokens": 3433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3433,
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

_source line 86 · 2026-05-11T23:03:59.151Z_

<details><summary>↩ Tool result · `toolu_017cBrZmGZmtYYPjSvt4HfRG`</summary>

```text
I appreciate your request, but I must inform you that the provided content is a PDF file rendered as binary/encoded text, which makes it impossible for me to extract meaningful information about state-of-the-art results on ACE05 for event extraction.

The document appears to be encoded in PDF format with compressed streams (indicated by the FlateDecode filters and binary data). While the file structure shows it contains 32 pages with various fonts and resources, I cannot reliably decode the actual textual content to identify comparison tables or specific model performance metrics.

To help you effectively, I would need:

1. **Plain text or structured format** of the comparison tables showing SOTA results
2. **PDF conversion to readable text** (using proper text extraction tools)
3. **Direct access to the relevant section** discussing ACE05 event extraction benchmarks

If you can provide the document in a readable format or share the specific comparison table data, I'd be happy to compile the state-of-the-art results with Trigger and Argument identification/classification F1 scores for all listed models, while adhering to your character limits and quotation requirements.

[Binary content (application/pdf, 743.5KB) also saved to /home/ubuntu/.claude-account-2/projects/-/efd9a69d-53ac-4eea-b205-15bb0fe42a60/tool-results/webfetch-1778540634907-hjwlvo.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "986ad7c8-d64b-4b2c-b733-3d68afcb70d8",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "1be81712-882d-4d06-8dc1-018e03865995",
  "sourceToolAssistantUUID": "986ad7c8-d64b-4b2c-b733-3d68afcb70d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-11T23:04:02.430Z_

<details><summary>↩ Tool result · `toolu_01V7CsTKKnfxmZEBnCL1SwcV`</summary>

```text
Web search results for query: "DocRED Re-DocRED 2025 newest model GEGA CDER evidence F1 Ign test results"

Links: [{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/html/2407.21384"},{"title":"Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-026-12099-8"},{"title":"[2205.12696] Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/abs/2205.12696"},{"title":"Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/html/2205.12696v3"},{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"Revisiting DocRED - Addressing the False Negative Problem in Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.580/"},{"title":"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/362262962_SAIS_Supervising_and_Augmenting_Intermediate_Steps_for_Document-Level_Relation_Extraction"},{"title":"GitHub - tonytan48/Re-DocRED","url":"https://github.com/tonytan48/Re-DocRED"},{"title":"(PDF) DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://www.researchgate.net/publication/333815327_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"}]

Based on the search results, here's information about recent models and test results for DocRED and Re-DocRED datasets:

## GEGA Model (2025)

GEGA achieves superior Ign-F1 and F1 metrics compared to the established DocRE Baselines on both the development set and the test set. GEGA achieves state-of-the-art results on RE-DocRED compared to other methods utilizing BERT-base as a pre-trained language model.

GEGA secured the highest Ign F1 and F1 scores in the fusion stage with Distant Supervision (Student), with improvements of 2.08% (Ign F1) and 2.52% (F1) respectively on the development set, and by 1.58% (Ign F1) and 1.97% (F1) respectively on the test set. GEGA is a novel model for DocRE that leverages graph neural networks to construct multiple weight matrices, guiding attention allocation to evidence sentences.

## CDER Model (2025)

CDER is a novel evidence retrieval framework that employs an attentional graph-based architecture to capture collaborative patterns and incorporates a dynamic sub-structure for additional robustness in evidence retrieval. The integration of CDER substantially enhances the performance of the EIDER model with a 0.23 increase in F1, and contributes an additional 0.07 increase in F1 to the DREEAM model to accomplish peak performance.

## Re-DocRED Dataset Improvements

Models trained and evaluated on Re-DocRED achieve performance improvements of around 13 F1 points.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc4f4515-9fdf-4bac-89d7-4627d5d72583",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "def3399a-f95d-4f15-a6a8-aa98a4a92d37",
  "sourceToolAssistantUUID": "cc4f4515-9fdf-4bac-89d7-4627d5d72583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-11T23:04:05.429Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FqDCJBv2rEeAqsbMs3ZzUm`</summary>

```json
{
  "url": "https://arxiv.org/html/2407.21384",
  "prompt": "Extract ALL F1 scores from ALL results tables. Include model names, Ign F1, F1, and Evi F1 scores for DocRED and Re-DocRED. List every number in the tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "def3399a-f95d-4f15-a6a8-aa98a4a92d37",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawckcAMAYEH9A3bCQXMt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a0ff12a-6919-4a00-a2cc-2b68f629f294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01378a9RBXqYBVYjBrFvHcSt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 44898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1568,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-11T23:04:06.453Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UqUXjAS9oNTdrKvYSv9YhP`</summary>

```json
{
  "query": "ACE 2005 event extraction leaderboard 2024 2025 trigger classification F1 73 74 75 argument classification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a0ff12a-6919-4a00-a2cc-2b68f629f294",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawckcAMAYEH9A3bCQXMt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "995d1ea7-93f4-408b-8807-700faaa3973b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01378a9RBXqYBVYjBrFvHcSt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 44898,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1568
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 44898,
          "cache_creation_input_tokens": 1568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1568,
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

_source line 90 · 2026-05-11T23:04:13.101Z_

<details><summary>↩ Tool result · `toolu_01UqUXjAS9oNTdrKvYSv9YhP`</summary>

```text
Web search results for query: "ACE 2005 event extraction leaderboard 2024 2025 trigger classification F1 73 74 75 argument classification"

Links: [{"title":"[2408.16932] Event Extraction for Portuguese: A QA-driven Approach using ACE-2005","url":"https://arxiv.org/abs/2408.16932"},{"title":"Event Extraction for Portuguese: A QA-driven Approach using ACE-2005 | OpenReview","url":"https://openreview.net/forum?id=BGVylhQ1CO"},{"title":"GitHub - nlpcl-lab/bert-event-extraction: Pytorch Solution of Event Extraction Task using BERT on ACE 2005 corpus","url":"https://github.com/nlpcl-lab/bert-event-extraction"},{"title":"Event Extraction for Portuguese: A QA-Driven Approach Using ACE-2005 | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-031-49008-8_32"},{"title":"GitHub - nlpcl-lab/ace2005-preprocessing: ACE 2005 corpus preprocessing for Event Extraction task · GitHub","url":"https://github.com/nlpcl-lab/ace2005-preprocessing"},{"title":"Reading the Manual: Event Extraction as Definition ...","url":"https://aclanthology.org/2020.spnlp-1.9.pdf"},{"title":"Event Extraction - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/computer-science/event-extraction"},{"title":"Event Extraction for Portuguese: A QA-driven Approach using ACE-2005","url":"https://arxiv.org/html/2408.16932"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset","url":"https://arxiv.org/pdf/2004.13590"},{"title":"DEGREE: A Data-Efficient Generation-Based Event Extraction Model","url":"https://openreview.net/pdf?id=3eNATGzQIK7"}]

Based on the search results, I found relevant information about ACE 2005 event extraction performance metrics. Here are the results:

## ACE 2005 Event Extraction Results

For trigger classification, baseline models show F1 scores ranging from 69.3% (JRNN) to 73.7% (JMEE), while argument classification F1 scores range from 55.5% to 60.3%.

More recent work from 2024 includes a framework that obtained F1 marks of 64.4 for trigger classification and 46.7 for argument classification for Portuguese event extraction, which represents adaptation of the ACE-2005 task to a different language.

The search results show various approaches being evaluated on the ACE 2005 dataset for both trigger classification and argument classification tasks, with F1 scores in the ranges you specified (73-75 for trigger classification and in the 40s-60s for argument classification depending on the specific approach).

If you're looking for specific leaderboard rankings or more recent 2024-2025 results with those exact F1 score ranges, the available search results don't contain a comprehensive leaderboard organized by date. Would you like me to search for more specific recent publications or leaderboards?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "995d1ea7-93f4-408b-8807-700faaa3973b",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "49697d09-3139-4647-9349-4bf5f17b3349",
  "sourceToolAssistantUUID": "995d1ea7-93f4-408b-8807-700faaa3973b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-11T23:04:16.077Z_

<details><summary>↩ Tool result · `toolu_01FqDCJBv2rEeAqsbMs3ZzUm`</summary>

```text
# F1 Score Extraction from GEGA Paper

## DocRED Results (Table 1)

**Development Set:**
- CNN: Ign-F1=41.58, F1=43.45
- BiLSTM: Ign-F1=48.87, F1=50.94
- GAIN: Ign-F1=59.14, F1=61.22
- MRN: Ign-F1=59.74, F1=61.61
- DocuNet: Ign-F1=59.86, F1=61.83
- GTN: Ign-F1=60.86, F1=62.73
- SD-DocRE: Ign-F1=60.85, F1=62.81
- ATLOP: Ign-F1=59.22, F1=61.09
- EIDER: Ign-F1=60.51, F1=62.48, Evi-F1=50.71
- SAIS: Ign-F1=59.98, F1=62.96, Evi-F1=53.70
- DREEAM: Ign-F1=60.51, F1=62.55, Evi-F1=52.08
- GEGA-single: Ign-F1=59.98, F1=61.95, Evi-F1=52.19
- GEGA-fusion: Ign-F1=60.55, F1=62.65
- KD-DocRE: Ign-F1=62.62, F1=64.81
- DREEAM (distant): Ign-F1=63.92, F1=65.83, Evi-F1=55.68
- GEGA-single (student): Ign-F1=64.02, F1=65.83, Evi-F1=56.09
- GEGA-fusion (student): Ign-F1=64.26, F1=66.38

**Test Set:**
- CNN: Ign-F1=40.33, F1=42.26
- BiLSTM: Ign-F1=48.78, F1=51.06
- GAIN: Ign-F1=59.00, F1=61.24
- MRN: Ign-F1=59.52, F1=61.74
- DocuNet: Ign-F1=59.93, F1=61.86
- GTN: Ign-F1=60.77, F1=62.75
- SD-DocRE: Ign-F1=60.91, F1=62.85
- ATLOP: Ign-F1=59.31, F1=61.30
- EIDER: Ign-F1=60.42, F1=62.47, Evi-F1=51.27
- SAIS: Ign-F1=60.96, F1=62.77, Evi-F1=52.88
- DREEAM: Ign-F1=60.03, F1=62.49, Evi-F1=51.71
- GEGA-single: Ign-F1=59.31, F1=61.52, Evi-F1=51.90
- GEGA-fusion: Ign-F1=60.11, F1=62.53
- KD-DocRE: Ign-F1=62.56, F1=64.76
- DREEAM (distant): Ign-F1=63.73, F1=65.87, Evi-F1=55.43
- GEGA-single (student): Ign-F1=63.82, F1=65.85, Evi-F1=55.89
- GEGA-fusion (student): Ign-F1=63.90, F1=66.31

## Re-DocRED Results (Table 2)

**Development Set:**
- GAIN-BERT: Ign-F1=71.99, F1=73.49
- DocuNet-BERT: Ign-F1=73.68, F1=74.65
- GTN-BERT: Ign-F1=75.03, F1=75.85
- ATLOP-BERT: Ign-F1=73.35, F1=74.22
- KMGRE-BERT: Ign-F1=73.33, F1=74.44
- KD-DocRE-BERT: Ign-F1=73.76, F1=74.69
- PRiSM-BERT: Ign-F1=72.92, F1=74.25
- GEGA-single (teacher): Ign-F1=73.69, F1=74.53
- GEGA-fusion (teacher): Ign-F1=76.06, F1=77.41
- GEGA-single (student): Ign-F1=75.72, F1=76.64
- GEGA-fusion (student): Ign-F1=77.11, F1=78.37

**Test Set:**
- GAIN-BERT: Ign-F1=71.88, F1=73.44
- DocuNet-BERT: Ign-F1=73.60, F1=74.49
- GTN-BERT: Ign-F1=74.85, F1=75.77
- ATLOP-BERT: Ign-F1=73.22, F1=74.02
- KMGRE-BERT: Ign-F1=73.39, F1=74.46
- KD-DocRE-BERT: Ign-F1=73.67, F1=74.55
- PRiSM-BERT: Ign-F1=72.35, F1=73.69
- GEGA-single (teacher): Ign-F1=73.42, F1=74.21
- GEGA-fusion (teacher): Ign-F1=75.28, F1=76.61
- GEGA-single (student): Ign-F1=75.25, F1=76.21
- GEGA-fusion (student): Ign-F1=76.43, F1=77.74
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a0ff12a-6919-4a00-a2cc-2b68f629f294",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "a5f8d012-a3cd-4867-9e4c-9d9a038f3e43",
  "sourceToolAssistantUUID": "5a0ff12a-6919-4a00-a2cc-2b68f629f294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-11T23:04:18.627Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CsRv1pW9fVohCDFZBDEuSK`</summary>

```json
{
  "query": "OneIE ACE05 event extraction F1 score trigger argument 2020 2021 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5f8d012-a3cd-4867-9e4c-9d9a038f3e43",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcmcUEAgGrCRv9uq7te",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73f95a4c-a460-4142-8bb2-f6498efbf59b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5QGd7JMcLvPvzh2xT5QF8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 838,
      "cache_creation_input_tokens": 1819,
      "cache_read_input_tokens": 46466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1819,
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

_source line 93 · 2026-05-11T23:04:19.079Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wn5W9Kxnrk8WzeLCs3p8YZ`</summary>

```json
{
  "query": "TextEE ACE05 benchmark 2024 event extraction best model results comparison table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73f95a4c-a460-4142-8bb2-f6498efbf59b",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcmcUEAgGrCRv9uq7te",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37e795cb-cd32-4f3c-a601-dd64ef794b24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5QGd7JMcLvPvzh2xT5QF8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 838,
      "cache_creation_input_tokens": 1819,
      "cache_read_input_tokens": 46466,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1819
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 838,
          "output_tokens": 127,
          "cache_read_input_tokens": 46466,
          "cache_creation_input_tokens": 1819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1819,
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

_source line 94 · 2026-05-11T23:04:24.466Z_

<details><summary>↩ Tool result · `toolu_01Wn5W9Kxnrk8WzeLCs3p8YZ`</summary>

```text
Web search results for query: "TextEE ACE05 benchmark 2024 event extraction best model results comparison table"

Links: [{"title":"GitHub - ej0cl6/TextEE: A standardized, fair, and reproducible benchmark for evaluating event extraction approaches · GitHub","url":"https://github.com/ej0cl6/TextEE"},{"title":"TextEE: Benchmark, Reevaluation, Reflections, and Future Challenges in Event Extraction - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.760/"},{"title":"TextEE: A Standardized, Fair, and Reproducible Benchmark for Event Extraction","url":"https://khhuang.me/TextEE/"},{"title":"[2311.09562] TextEE: Benchmark, Reevaluation, Reflections, and Future Challenges in Event Extraction","url":"https://arxiv.org/abs/2311.09562"},{"title":"TextEE: Benchmark, Reevaluation, Reflections, and Future Challenges in Event Extraction | Request PDF","url":"https://www.researchgate.net/publication/384214615_TextEE_Benchmark_Reevaluation_Reflections_and_Future_Challenges_in_Event_Extraction"},{"title":"TEXTEE: Benchmark, Reevaluation, Reflections, and ...","url":"https://aclanthology.org/2024.findings-acl.760.pdf"},{"title":"SpeechEE: A Novel Benchmark for Speech Event Extraction","url":"https://arxiv.org/html/2408.09462"},{"title":"Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines","url":"https://arxiv.org/html/2502.16377v1"},{"title":"TEXTEE: A Benchmark for Event Extraction | PDF","url":"https://www.scribd.com/document/919286428/TEXTEE"},{"title":"TextEE: Benchmark, Reevaluation, Reflections, and Future Challenges in Event Extraction","url":"http://web.cs.ucla.edu/~kwchang/bibliography/huang2024textee/"}]

Based on my search results, I found information about the TextEE benchmark for event extraction. Here's what I discovered:

## TextEE Benchmark Overview

TextEE is a standardized, fair, and reproducible benchmark for event extraction that comprises standardized data preprocessing scripts and splits for 16 datasets spanning eight diverse domains and includes 14 recent methodologies, conducting a comprehensive benchmark reevaluation.

## ACE05 Dataset

ACE05 is the most widely used benchmark dataset for event extraction.

## Model Evaluation on TextEE Benchmark

TextEE evaluated five varied large language models on the benchmark and demonstrated how they struggle to achieve satisfactory performance. Additionally, the benchmark includes 14 recent methodologies conducting comprehensive reevaluation and also evaluates large language models on the TextEE benchmark.

## Publication Details

The TextEE paper was published in 2024 as "TextEE: Benchmark, Reevaluation, Reflections, and Future Challenges in Event Extraction" in Findings of the Association for Computational Linguistics: ACL 2024, pages 12804–12825, Bangkok, Thailand.

The search results indicate that while TextEE provides a comprehensive benchmarking framework with ACE05 as a key dataset, the specific detailed comparison table with best model results you requested is contained in the full paper. You may need to access the full paper directly from the ACL Anthology or arXiv to view the complete results tables.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37e795cb-cd32-4f3c-a601-dd64ef794b24",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "ec679f89-f30b-4092-b278-f59c5e563452",
  "sourceToolAssistantUUID": "37e795cb-cd32-4f3c-a601-dd64ef794b24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-11T23:04:25.961Z_

<details><summary>↩ Tool result · `toolu_01CsRv1pW9fVohCDFZBDEuSK`</summary>

```text
Web search results for query: "OneIE ACE05 event extraction F1 score trigger argument 2020 2021 results"

Links: [{"title":"GitHub - jeremytanjianle/event-extraction-oneie: Event extraction of ACE05 dataset","url":"https://github.com/jeremytanjianle/event-extraction-oneie"},{"title":"DEGREE: A Data-Efficient Generation-Based Event Extraction Model","url":"https://openreview.net/pdf?id=3eNATGzQIK7"},{"title":"Closed-Domain Event Extraction Literature Review January 2025 v1.0","url":"https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf"},{"title":"Joint Neural Model for Information Extraction","url":"https://aclanthology.org/2020.acl-main.713.pdf"},{"title":"JSEEGraph: Joint Structured Event Extraction as Graph Parsing","url":"https://arxiv.org/html/2306.14633"},{"title":"Event Extraction by Answering (Almost) Natural Questions","url":"https://aclanthology.org/2020.emnlp-main.49.pdf"},{"title":"Event Extraction as Question Generation and Answering","url":"https://arxiv.org/html/2307.05567"},{"title":"XLLM ACL 2025 Shared Task-II: Speech Event Extraction","url":"https://xllms.github.io/SpeechEE/"},{"title":"DEGAP: Dual Event-Guided Adaptive Prefixes for Templated-Based Event Argument Extraction with Slot Querying","url":"https://arxiv.org/html/2405.13325"},{"title":"[Quick Review] A Joint Neural Model for Information Extraction with Global Features","url":"https://liner.com/review/joint-neural-model-for-information-extraction-with-global-features"}]

Based on the search results, I found detailed F1 score information for OneIE on ACE05 event extraction. Here are the key results:

## OneIE ACE05 Event Extraction Results

On ACE05-E, OneIE achieves 78.2% for Trigger Identification (Trig-I), 74.7% for Trigger Classification (Trig-C), 59.2% for Argument Identification (Arg-I), and 56.8% for Argument Classification (Arg-C).

Additionally, OneIE reaches 74.7 F1 on trigger detection and 56.8 on argument extraction (affected by trigger detection).

OneIE (Lin et al., 2020) is a model that can be applied to multiple IE tasks, including event extraction, and the ONEIE framework consistently outperforms both the state-of-the-art end-to-end IE model (DYGIE++) and baseline models across all subtasks on the ACE05 datasets.

The results demonstrate that OneIE achieved strong performance on event trigger detection and argument extraction tasks when evaluated on the ACE05 benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73f95a4c-a460-4142-8bb2-f6498efbf59b",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "eba2844a-2091-4976-9a00-92a15ca134bd",
  "sourceToolAssistantUUID": "73f95a4c-a460-4142-8bb2-f6498efbf59b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-11T23:04:29.527Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QEP13isYvfeZ2LECN2hnge`</summary>

```json
{
  "url": "https://arxiv.org/html/2311.09562",
  "prompt": "Extract ALL F1 scores from the ACE05 results tables. List every model with Trigger Classification F1 and Argument Classification F1. Focus on the main comparison table for ACE05."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eba2844a-2091-4976-9a00-92a15ca134bd",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcnLkwmUuq8tp4iBU3L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "488ca7d7-a583-48bb-9e8e-240fbc83cb7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zMD98LEonecTgzXDbdB7u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 904,
      "cache_creation_input_tokens": 1750,
      "cache_read_input_tokens": 48285,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1750
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 904,
          "output_tokens": 124,
          "cache_read_input_tokens": 48285,
          "cache_creation_input_tokens": 1750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1750,
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

_source line 97 · 2026-05-11T23:04:34.075Z_

<details><summary>↩ Tool result · `toolu_01QEP13isYvfeZ2LECN2hnge`</summary>

```text
# ACE05 F1 Scores from TextEE Benchmark

Based on Table 3 (End-to-End Event Extraction results), here are the ACE05 performance metrics:

## Trigger Classification (TC) F1 Scores
- DyGIE++: 71.3
- OneIE: 71.1
- AMR-IE: 71.1
- EEQA: 70.0
- RCEE: 70.5
- Query&Extract: 65.1
- TagPrime: 69.9
- DEGREE-E2E: 66.8
- DEGREE-PIPE: 68.4

## Argument Classification (AC) F1 Scores
- DyGIE++: 56.0
- OneIE: 59.9
- AMR-IE: 60.6
- EEQA: 55.3
- RCEE: 55.5
- Query&Extract: 55.0
- TagPrime: 59.8
- DEGREE-E2E: 55.1
- DEGREE-PIPE: 56.3

**Note:** All scores represent averages across 5 standardized data splits to reduce bias from single fixed partitions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "488ca7d7-a583-48bb-9e8e-240fbc83cb7b",
  "isSidechain": true,
  "promptId": "1431e9c3-5c72-47c2-a5d0-7ca9c7f0398e",
  "agentId": "ab6fbd4eb426f749b",
  "type": "user",
  "uuid": "3dc90323-4353-4c06-b780-6cc800a46d84",
  "sourceToolAssistantUUID": "488ca7d7-a583-48bb-9e8e-240fbc83cb7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 98 · 2026-05-11T23:05:39.243Z_

Now I have comprehensive data. Let me compile the final report.

---

Here is a consolidated report of findings across all three research questions.

---

## 1. DocRED Evidence Annotations

**Confirmed:** DocRED includes "supporting evidence sentences" for each relation instance. Each annotated relation triplet (head entity, relation, tail entity) has an `"evidence"` field listing the indices of sentences that support that relation. Approximately 40.7% of relational facts in DocRED require extraction from multiple sentences, making evidence annotation essential. The dataset contains 97 relation types, 132,375 entities, and 56,354 relational facts across 5,053 Wikipedia documents.

**Recent work on evidence-guided document-level RE (2025-2026):**

- **GEGA** (Mao et al., 2025) -- "Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction." Uses GCNs to construct multiple weight matrices guiding attention to evidence sentences. On DocRED test (BERT-base, with distant supervision): Ign F1 = 63.90, F1 = 66.31, Evi F1 = 55.89.
- **CDER** (Tran & Li, April 2025) -- "Collaborative Evidence Retrieval for Document-level Relation Extraction." An attentional graph-based evidence retrieval framework. On DocRED test: DREEAM + CDER achieves Ign F1 = 60.22, F1 = 62.45, Evi F1 = 53.03.
- **GLiM** (Fang et al., ACL 2025 Findings) -- "Integrating Graph Transformer and LLM for Document-Level Biomedical Relation Extraction with Incomplete Labeling." Boosts average recall and F1 by +6.34 and +4.41 on biomedical DocRE benchmarks (ChemDisGene, BioRED, DocRED).
- **"Dual reasoning enhanced document-level relation extraction"** (Zhang et al., Neural Computing and Applications, 2026).
- **"Evidence and Axial Attention Guided Document-level Relation Extraction"** (Yuan et al., Computer Speech and Language, 2025).

---

## 2. Current SOTA on ACE05, SciERC, and DocRED

### ACE05

**Joint Entity and Relation Extraction (PL-Marker, ACL 2022 -- still leading):**

| Model | Encoder | Entity F1 | Relation F1 | Strict Rel F1 |
|---|---|---|---|---|
| PL-Marker | ALBERT-xxlarge | **91.1** | **73.0** | **71.1** |
| PURE-F | ALBERT-xxlarge | 90.9 | 69.4 | 67.0 |
| UniRE | ALBERT-xxlarge | 90.2 | -- | 66.0 |
| PL-Marker | BERT-base | 89.8 | 69.0 | 66.5 |
| PURE-F | BERT-base | 90.1 | 67.7 | 64.8 |
| OneIE | BERT-base | 88.8 | 67.5 | -- |

**Event Extraction (TextEE benchmark, standardized 5-split averages):**

| Model | Trigger Classification F1 | Argument Classification F1 |
|---|---|---|
| DyGIE++ | 71.3 | 56.0 |
| OneIE | 71.1 | 59.9 |
| AMR-IE | 71.1 | **60.6** |
| TagPrime | 69.9 | 59.8 |
| DEGREE-PIPE | 68.4 | 56.3 |

Note: Some individual-split papers report higher numbers (e.g., OneIE: TC = 74.7, AC = 56.8; PLMEE: TI = 84.2, TC = 80.7), but TextEE's standardized evaluation shows AMR-IE as best on Arg-C at 60.6 and DyGIE++/OneIE tied on TC at ~71.

### SciERC

**Joint Entity and Relation Extraction:**

| Model | Encoder | Entity F1 | Relation F1 | Strict Rel F1 |
|---|---|---|---|---|
| **PL-Marker** | SciBERT | **69.9** | **53.2** | **41.6** |
| TriMF | SciBERT | 70.2 | 52.4 | -- |
| PURE-F | SciBERT | 68.9 | 50.1 | 36.8 |
| UniRE | SciBERT | 68.4 | -- | 36.9 |

**NER only:** Best reported ~70.91 F1 (hierarchical transformer, 2024).

### DocRED / Re-DocRED

**DocRED (BERT-base, test set):**

| Model | Ign F1 | F1 | Evi F1 | Notes |
|---|---|---|---|---|
| GEGA-fusion (student) | **63.90** | **66.31** | -- | 2025, with distant supervision |
| DREEAM (student) | 63.73 | 65.87 | 55.43 | 2023, with distant supervision |
| GEGA-single (student) | 63.82 | 65.85 | **55.89** | 2025, best evidence F1 |
| KD-DocRE | 62.56 | 64.76 | -- | with distant supervision |
| DREEAM + Fusion | 60.03 | 62.49 | 51.71 | without distant supervision |
| ATLOP | 59.31 | 61.30 | -- | baseline |

**Re-DocRED (BERT-base, test set, fully supervised):**

| Model | Ign F1 | F1 |
|---|---|---|
| **DREEAM** | **78.56** | **80.20** |
| TTM-RE | 78.20 | 79.95 |
| KD-DocRE | 77.60 | 78.28 |
| ATLOP | 76.13 | 77.81 |
| GLiDRE | 76.80 | 77.83 |
| GEGA-fusion (student) | 76.43 | 77.74 |

**Re-DocRED (BERT-base, with distant supervision, GEGA paper):**
- GEGA-fusion (student): Ign F1 = 77.11, F1 = 78.37 (dev set)

**Zero-shot (Re-DocRED test):** Mistral-Large 123B = 18.61 F1; Qwen 2.5 72B = 18.00 F1 -- showing LLMs still dramatically lag supervised models.

**Note:** Papers with Code was shut down by Meta in July 2025; leaderboards are no longer accessible.

---

## 3. Attribution/Provenance Combined with Structured Information Extraction

### Direct matches:

1. **AEVS Framework** (published March 2026) -- "Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking" (in MDPI Computers, 15(3), 178). This is the most directly relevant paper. It grounds every extracted triplet element to the source text via an Anchor-Extraction-Verification-Supplement pipeline. Key features:
   - Each triplet element must link to a discovered text anchor
   - "Extract-then-restore" verification with hierarchical matching (exact, fuzzy, schema-based, text search fallback)
   - Hallucination rates of 0.23-20.23% across model-dataset configs
   - Tested on WebNLG, REBEL, Wiki-NRE
   - 2.83-4.28 LLM calls per sample

2. **E2GRE** -- "Entity and Evidence Guided Relation Extraction for DocRED." Jointly trains relation extraction and evidence sentence prediction, using BERT attention probabilities as features for evidence prediction. The model explicitly links each predicted relation to its supporting evidence sentences.

3. **DREEAM** (EACL 2023) -- "Guiding Attention with Evidence for Improving Document-Level Relation Extraction." Uses evidence annotations as supervisory signals to guide attention, jointly predicting relations and evidence.

4. **SAIS** -- "Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction." Supervises four intermediate tasks including Pooled Evidence Retrieval and Fine-grained Evidence Retrieval.

5. **Google LangExtract** (July 2025) -- Open-source library that maps every extracted entity to exact text offsets for traceability/grounded extraction.

6. **Zero-shot evidence-grounded extraction** (IOP Science, 2025) -- Applied to blood-brain barrier nanoparticle design parameters; each extracted value accompanied by a direct quotation from source text.

7. **CiteGuard** (2025) -- "Faithful Citation Attribution for LLMs via Retrieval-Augmented Validation." With DeepSeek-R1 reaches 65.4% accuracy approaching human-level 69.7%.

8. **FACTS Grounding Benchmark** (Google DeepMind) -- Evaluates LLM factuality with strict requirement that all claims be grounded in supplied context.

---

### Key Sources:

- [DocRED (ACL 2019)](https://aclanthology.org/P19-1074/)
- [DocRED GitHub](https://github.com/thunlp/DocRED)
- [PL-Marker (ACL 2022)](https://ar5iv.labs.arxiv.org/html/2109.06067)
- [DREEAM (EACL 2023)](https://aclanthology.org/2023.eacl-main.145/)
- [GEGA (2025)](https://arxiv.org/html/2407.21384)
- [CDER (April 2025)](https://arxiv.org/html/2504.06529)
- [GLiM (ACL 2025 Findings)](https://aclanthology.org/2025.findings-acl.727/)
- [GLiDRE (2025)](https://arxiv.org/abs/2508.00757)
- [Re-DocRED](https://github.com/tonytan48/Re-DocRED)
- [TextEE Benchmark (ACL 2024 Findings)](https://aclanthology.org/2024.findings-acl.760/)
- [AEVS Grounded KG Extraction (March 2026)](https://www.mdpi.com/2073-431X/15/3/178)
- [SciERC / SciNLP](https://arxiv.org/html/2509.07801)
- [Event Extraction Survey (Dec 2025)](https://arxiv.org/html/2512.19537v1)
- [Relation Extraction Survey (2025)](https://link.springer.com/article/10.1007/s10462-025-11280-0)
- [CiteGuard (2025)](https://arxiv.org/html/2510.17853v1)
- [FACTS Grounding Benchmark (Google DeepMind)](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dc90323-4353-4c06-b780-6cc800a46d84",
  "isSidechain": true,
  "agentId": "ab6fbd4eb426f749b",
  "requestId": "req_011CawcnwUkUr1g4vFiB6cPG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9694bb92-8679-4a75-8d34-5b7df130b41c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "efd9a69d-53ac-4eea-b205-15bb0fe42a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYue7EUTrrj1YGkDa2MezB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1333,
      "cache_read_input_tokens": 50035,
      "output_tokens": 2911,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1333
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2911,
          "cache_read_input_tokens": 50035,
          "cache_creation_input_tokens": 1333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1333,
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
