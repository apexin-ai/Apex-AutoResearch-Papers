# Research conversation: I need you to verify the following academic paper citations by searching the web. For each paper, confirm whether the ti

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a9b1c8509187f2b63.jsonl`
- **Structured JSON:** [`947a1602f61a92803e4c.json`](../../sessions/94/947a1602f61a92803e4c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-22T12:55:50.296Z_

I need you to verify the following academic paper citations by searching the web. For each paper, confirm whether the title, authors, venue, and year are correct. Report back in this format for each:

| bib_key | Status | Notes |

Status: ✅ correct, ⚠️ minor issue, ❌ serious error

Papers to verify:

1. ACL Anthology 2023.findings-emnlp.425 - claimed title: "Schema-adaptable Knowledge Graph Construction", authors: Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang, Ningyu, venue: EMNLP 2023 Findings

2. ACL Anthology 2024.acl-long.475 - claimed title: "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction", authors: Li, Zixuan and Zeng, Yutao and others, venue: ACL 2024

3. OpenReview Y3wpuxd7u9 - claimed title: "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction Modeling", authors: Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko, venue: ICLR 2024

4. ACL Anthology 2023.acl-long.855 - claimed title: "CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors", authors: Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng, venue: ACL 2023

5. NeurIPS 2024 - claimed title: "Grammar-Aligned Decoding", authors: Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris, arXiv:2405.21047

6. ACL Anthology 2023.acl-long.868 - claimed title: "Revisiting Relation Extraction in the era of Large Language Models", authors: Wadhwa, Somin and Amir, Silvio and Wallace, Byron, venue: ACL 2023

7. OpenReview r65xfUb76p - claimed title: "UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition", authors: Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung, venue: ICLR 2024

8. AAAI 2023 doi:10.1609/aaai.v37i11.26563 - claimed title: "Universal Information Extraction as Unified Semantic Matching", authors: Lou, Jie and Lu, Yaojie and Dai, Dai and Jia, Wei and Lin, Hongyu and Han, Xianpei and Sun, Le and Wu, Hua, venue: AAAI 2023

Search each one on the web and confirm accuracy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "42061f37-e83a-4f81-9c47-a74b17635dd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T12:55:50.299Z_

```json
{
  "parentUuid": "42061f37-e83a-4f81-9c47-a74b17635dd6",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
  "uuid": "ac5dd315-9ab1-4d10-b472-01666d0b7504",
  "timestamp": "2026-05-22T12:55:50.299Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-22T12:55:53.338Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Nz4RzScrUfMvrSFtVhibqQ`</summary>

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
  "parentUuid": "ac5dd315-9ab1-4d10-b472-01666d0b7504",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeGgr9sSVAPvw7r8i6A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a2bc45b-2f20-47dc-9e5b-3c6df493a3dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StTVWcbAogNTXSvptRdwQP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7344,
      "cache_read_input_tokens": 7333,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7344
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 7333,
          "cache_creation_input_tokens": 7344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7344,
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

_source line 4 · 2026-05-22T12:55:53.340Z_

<details><summary>↩ Tool result · `toolu_01Nz4RzScrUfMvrSFtVhibqQ`</summary>

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
  "parentUuid": "4a2bc45b-2f20-47dc-9e5b-3c6df493a3dc",
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "070f4cfc-f98a-4860-8478-5319a19a3dae",
  "sourceToolAssistantUUID": "4a2bc45b-2f20-47dc-9e5b-3c6df493a3dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T12:55:56.917Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U4LHCB8nd8ggcX4KKoZVfz`</summary>

```json
{
  "query": "ACL Anthology 2023.findings-emnlp.425 \"Schema-adaptable Knowledge Graph Construction\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "070f4cfc-f98a-4860-8478-5319a19a3dae",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeGvKH1heP56roaqZ4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9664147-0531-4aeb-a369-f47cc5258061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kUPaeru8JRzKp6ZSJeTTc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 6 · 2026-05-22T12:55:57.599Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LYQbPLAkbRgfZWAy6eKhYs`</summary>

```json
{
  "query": "ACL Anthology 2024.acl-long.475 \"KnowCoder\" universal information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9664147-0531-4aeb-a369-f47cc5258061",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeGvKH1heP56roaqZ4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0de4419e-825c-4e17-bcc2-85d130b56bc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kUPaeru8JRzKp6ZSJeTTc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 7 · 2026-05-22T12:55:57.919Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QwR1HpRzRLg1muzgKzx7av`</summary>

```json
{
  "query": "OpenReview Y3wpuxd7u9 GoLLIE annotation guidelines zero-shot information extraction ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0de4419e-825c-4e17-bcc2-85d130b56bc3",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeGvKH1heP56roaqZ4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef4309c8-27a7-45be-98ce-7da578ed34ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kUPaeru8JRzKp6ZSJeTTc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 8 · 2026-05-22T12:55:58.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P7GQ2S9mQaGaqWvFikmikY`</summary>

```json
{
  "query": "ACL Anthology 2023.acl-long.855 \"CodeIE\" code generation information extractors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef4309c8-27a7-45be-98ce-7da578ed34ac",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeGvKH1heP56roaqZ4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "687d2887-944a-460b-b5be-3e02d57cfab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kUPaeru8JRzKp6ZSJeTTc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14677,
      "output_tokens": 261,
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
          "output_tokens": 261,
          "cache_read_input_tokens": 14677,
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

_source line 9 · 2026-05-22T12:56:03.420Z_

<details><summary>↩ Tool result · `toolu_01LYQbPLAkbRgfZWAy6eKhYs`</summary>

```text
Web search results for query: "ACL Anthology 2024.acl-long.475 "KnowCoder" universal information extraction"

Links: [{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.475/"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal   Information Extraction","url":"https://arxiv.org/pdf/2403.07969"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - Zixuan Li","url":"https://lee-zix.github.io/publications/2024-08-16-ACL/"},{"title":"TRUE-UIE: Two Universal Relations Unify Information Extraction Tasks - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.103/"},{"title":"Retrieval-Augmented Code Generation for Universal Information Extraction","url":"https://arxiv.org/pdf/2311.02962"},{"title":"Statements: Universal Information Extraction from Tables with Large Language Models for ESG KPIs - ACL Anthology","url":"https://aclanthology.org/2024.climatenlp-1.15/"},{"title":"Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) - ACL Anthology","url":"https://aclanthology.org/volumes/2024.naacl-long/"}]

Based on the search results, I found the paper you're looking for:

**KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction** is a paper by Li et al., published at ACL 2024 (the 62nd Annual Meeting of the Association for Computational Linguistics), appearing in Volume 1: Long Papers, pages 8758–8779, in Bangkok, Thailand.

The paper addresses challenges in Universal Information Extraction (UIE). Large Language Models have demonstrated general understanding abilities, but their performance on UIE is limited due to: (1) the lack of a unified schema representation method that LLMs can easily understand; (2) the lack of an effective learning framework that encourages LLMs to accurately follow specific schemas for extracting structured knowledge.

The paper's approach involves using code-based representations to encode structured knowledge into LLMs, incorporating elements like class comments for defining concepts and type hints for modeling constraints among concepts in schemas.

You can access the full paper at the ACL Anthology: https://aclanthology.org/2024.acl-long.475/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0de4419e-825c-4e17-bcc2-85d130b56bc3",
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "0b2a9f4a-1d4a-403c-b87c-55fef0293523",
  "sourceToolAssistantUUID": "0de4419e-825c-4e17-bcc2-85d130b56bc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T12:56:03.518Z_

<details><summary>↩ Tool result · `toolu_01U4LHCB8nd8ggcX4KKoZVfz`</summary>

```text
Web search results for query: "ACL Anthology 2023.findings-emnlp.425 "Schema-adaptable Knowledge Graph Construction""

Links: [{"title":"Schema-adaptable Knowledge Graph Construction - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.425/"},{"title":"Schema-adaptable Knowledge Graph Construction","url":"https://arxiv.org/pdf/2305.08703"},{"title":"GitHub - zjunlp/AdaKGC: [EMNLP 2023 (Findings)] Schema-adaptable Knowledge Graph Construction","url":"https://github.com/zjunlp/AdaKGC"},{"title":"Schema-adaptable Knowledge Graph Construction","url":"https://aclanthology.org/2023.findings-emnlp.425.pdf"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"},{"title":"Schema-aware Reference as Prompt Improves Data-Efficient Knowledge Graph   Construction","url":"https://arxiv.org/pdf/2210.10709"},{"title":"AutoSchemaKG: Autonomous Knowledge Graph Construction through Dynamic Schema Induction from Web-Scale Corpora","url":"https://arxiv.org/pdf/2505.23628"}]

I found the paper! Here are the key details about this work:

**Paper Title:** Schema-adaptable Knowledge Graph Construction

**Authors and Publication Details:** Hongbin Ye, Honghao Gui, Xin Xu, Xi Chen, Huajun Chen, and Ningyu Zhang, published in Findings of the Association for Computational Linguistics: EMNLP 2023, pages 6408–6431, Singapore

**Main Problem Addressed:** Conventional Knowledge Graph Construction approaches typically follow a static information extraction paradigm with a closed set of pre-defined schema, but fall short when applied to dynamic scenarios or domains where new knowledge emerges

**Key Contribution:** The paper proposes a new task called schema-adaptable KGC, which aims to continually extract entity, relation, and event based on a dynamically changing schema graph without re-training

**Methodology:** The authors split and convert existing datasets based on three principles to build a benchmark (horizontal schema expansion, vertical schema expansion, and hybrid schema expansion), and propose a baseline called ADAKGC, which contains schema-enriched prefix instructor and schema-conditioned dynamic decoding

The paper is available on the ACL Anthology at https://aclanthology.org/2023.findings-emnlp.425/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9664147-0531-4aeb-a369-f47cc5258061",
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "f3380705-8154-486f-bd71-5fabbb7018e2",
  "sourceToolAssistantUUID": "e9664147-0531-4aeb-a369-f47cc5258061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T12:56:05.446Z_

<details><summary>↩ Tool result · `toolu_01QwR1HpRzRLg1muzgKzx7av`</summary>

```text
Web search results for query: "OpenReview Y3wpuxd7u9 GoLLIE annotation guidelines zero-shot information extraction ICLR 2024"

Links: [{"title":"ICLR Poster GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://iclr.cc/virtual/2024/poster/18435"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO-SHOT ...","url":"https://openreview.net/notes/edits/attachment?id=x345y4wtJb&name=pdf"},{"title":"GOLLIE: ANNOTATION GUIDELINES IMPROVE ZERO-SHOT INFORMATION-EXTRACTION | Documents - Universidad del País Vasco / Euskal Herriko Unibertsitatea","url":"https://ekoizpen-zientifikoa.ehu.eus/documentos/66cb8eeac7cd8e0cebf21fbb"},{"title":"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview","url":"https://openreview.net/forum?id=Y3wpuxd7u9"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"TRANSLATION AND FUSION IMPROVES ZERO-SHOT CROSS- ...","url":"https://openreview.net/notes/edits/attachment?id=Riqir2khU9&name=pdf"},{"title":"gollie : annotation guidelines improve zero-shot ...","url":"https://arxiv.org/pdf/2310.03668"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...","url":"https://openreview.net/pdf?id=Y3wpuxd7u9"}]

Based on the search results, I found the paper you're looking for on OpenReview. Here's what I discovered:

**GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction**

GoLLIE (Guideline-following Large Language Model for IE) is a model able to improve zero-shot results on unseen IE tasks by virtue of being fine-tuned to comply with annotation guidelines.

**Key Details:**

- **Paper ID**: Y3wpuxd7u9 on OpenReview
- **Conference**: Published as a conference paper at ICLR 2024
- **Authors**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, and Eneko Agirre

**Main Contribution:**

While LLMs combined with instruction tuning have been less successful in Information Extraction, lagging behind task-specific models, IE tasks are typically characterized by complex annotation guidelines, and previous attempts to leverage such information have failed even with the largest models as they are not able to follow the guidelines out-of-the-box.

Comprehensive evaluation empirically demonstrates that GoLLIE is able to generalize to and follow unseen guidelines, outperforming previous attempts at zero-shot information extraction.

The paper is available on the OpenReview forum at https://openreview.net/forum?id=Y3wpuxd7u9, and the code is available on GitHub at https://github.com/hitz-zentroa/GoLLIE.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef4309c8-27a7-45be-98ce-7da578ed34ac",
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "a16167f8-fea7-4a4c-9bde-7b5c45693dae",
  "sourceToolAssistantUUID": "ef4309c8-27a7-45be-98ce-7da578ed34ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T12:56:06.249Z_

<details><summary>↩ Tool result · `toolu_01P7GQ2S9mQaGaqWvFikmikY`</summary>

```text
Web search results for query: "ACL Anthology 2023.acl-long.855 "CodeIE" code generation information extractors"

Links: [{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.855/"},{"title":"[Quick Review] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://liner.com/review/codeie-large-code-generation-models-are-better-fewshot-information-extractors"},{"title":"GitHub - artpli/CodeIE: [ACL 23] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors · GitHub","url":"https://github.com/artpli/CodeIE"},{"title":"[2305.05711v2] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711v2"},{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information   Extractors","url":"https://arxiv.org/pdf/2305.05711"},{"title":"[2305.05711] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711"},{"title":"CODEIE: Large Code Generation Models are Better Few- ...","url":"https://aclanthology.org/2023.acl-long.855.pdf"},{"title":"Retrieval-Augmented Code Generation for Universal Information Extraction","url":"https://arxiv.org/pdf/2311.02962"},{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors | Request PDF","url":"https://www.researchgate.net/publication/372919086_CodeIE_Large_Code_Generation_Models_are_Better_Few-Shot_Information_Extractors"},{"title":"Releases · artpli/CodeIE","url":"https://github.com/artpli/CodeIE/releases"}]

I found information about the paper you're searching for. Here's what the search results show:

## CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors

This is a paper by Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, and Xipeng Qiu, published at ACL 2023.

**Main Contribution:**
The paper proposes to recast structured output in the form of code instead of natural language and utilize generative LLMs of code (Code-LLMs) such as Codex to perform IE tasks, particularly named entity recognition and relation extraction.

**Key Approach:**
CodeIE formulates structured outputs as Python code elements like dictionaries and lists, and designs code-style prompts and utilizes in-context demonstrations to guide Code-LLMs to generate structured predictions without fine-tuning.

**Results:**
Experiment results on seven benchmarks show that the method consistently outperforms fine-tuning moderate-size pre-trained models specially designed for IE tasks (e.g., UIE) and prompting NL-LLMs under few-shot settings.

The paper is available at the ACL Anthology and also on arXiv, with an official GitHub repository for the code and resources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "687d2887-944a-460b-b5be-3e02d57cfab8",
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "ed3b0200-99aa-4dc0-9dff-c2f2a4889f0e",
  "sourceToolAssistantUUID": "687d2887-944a-460b-b5be-3e02d57cfab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T12:56:10.716Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LZjRsuQYiUeozmPyvyJZxL`</summary>

```json
{
  "query": "arXiv 2405.21047 \"Grammar-Aligned Decoding\" Park Kanghee NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed3b0200-99aa-4dc0-9dff-c2f2a4889f0e",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeHsxB6mqRyvSrZtDQM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef1617e1-d724-4e0a-8d7e-4df8c2865dac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgNy9jP4tX6Ym92GtZZeix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3421,
      "cache_read_input_tokens": 16116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3421,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 14 · 2026-05-22T12:56:11.505Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LcL3jNLPWCCijNEkqsthn3`</summary>

```json
{
  "query": "ACL Anthology 2023.acl-long.868 \"Revisiting Relation Extraction\" large language models Wadhwa"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef1617e1-d724-4e0a-8d7e-4df8c2865dac",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeHsxB6mqRyvSrZtDQM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d38bd592-dcca-4de2-86fe-990617f5728f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgNy9jP4tX6Ym92GtZZeix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3421,
      "cache_read_input_tokens": 16116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3421,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 15 · 2026-05-22T12:56:12.524Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RfrRvF8LsYctJobcNBcDrr`</summary>

```json
{
  "query": "OpenReview r65xfUb76p UniversalNER targeted distillation ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d38bd592-dcca-4de2-86fe-990617f5728f",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeHsxB6mqRyvSrZtDQM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f33d8f10-4f0f-4c95-9e11-738f0dec266f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgNy9jP4tX6Ym92GtZZeix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3421,
      "cache_read_input_tokens": 16116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3421,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 16 · 2026-05-22T12:56:13.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VubTGPE6rC95TWYBE7XaQ8`</summary>

```json
{
  "query": "AAAI 2023 doi 10.1609/aaai.v37i11.26563 \"Universal Information Extraction as Unified Semantic Matching\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f33d8f10-4f0f-4c95-9e11-738f0dec266f",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeHsxB6mqRyvSrZtDQM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8ed12f6-421c-412b-b0be-772a091bf2d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgNy9jP4tX6Ym92GtZZeix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3421,
      "cache_read_input_tokens": 16116,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 282,
          "cache_read_input_tokens": 16116,
          "cache_creation_input_tokens": 3421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3421,
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

_source line 17 · 2026-05-22T12:56:17.113Z_

<details><summary>↩ Tool result · `toolu_01LZjRsuQYiUeozmPyvyJZxL`</summary>

```text
Web search results for query: "arXiv 2405.21047 "Grammar-Aligned Decoding" Park Kanghee NeurIPS 2024"

Links: [{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://arxiv.org/pdf/2405.21047"},{"title":"Grammar-Aligned Decoding | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/grammar-aligned-decoding"},{"title":"Grammar-Aligned Decoding","url":"https://www.popai.pro/chatwithdoc/paper/Grammar-Aligned-Decoding.html"},{"title":"(PDF) Grammar-Aligned Decoding","url":"https://www.researchgate.net/publication/381108984_Grammar-Aligned_Decoding"},{"title":"Grammar-Aligned Decoding | PromptLayer","url":"https://www.promptlayer.com/research-papers/grammar-aligned-decoding"},{"title":"Approximately Aligned Decoding","url":"https://arxiv.org/html/2410.01103v1"},{"title":"Grammar-Aligned Decoding","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"Grammar-Aligned Decoding - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240521047P/abstract"}]

Based on the search results, here's what I found about arXiv paper 2405.21047:

**Paper Details:**
The paper is titled "Grammar-Aligned Decoding" by authors Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, and Loris D'Antoni. It was accepted to Advances in Neural Information Processing Systems 37 (NeurIPS 2024) Main Conference Track.

**Main Problem:**
Large Language Models (LLMs) struggle with reliably generating highly structured outputs, such as program code, mathematical formulas, or well-formed markup. GCD techniques can distort the LLM's distribution, leading to outputs that are grammatical but appear with likelihoods that are not proportional to the ones given by the LLM, and so ultimately are low-quality.

**Proposed Solution:**
The paper introduces and formalizes grammar-aligned decoding (GAD), the problem of sampling from an LLM so that the outputs are guaranteed to adhere to a given grammar and are unbiased with respect to the LLM's distribution. The algorithm, which is dubbed Adaptive Sampling with Approximate Expected Futures (ASAp), is built "on top" of existing constrained decoding algorithms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef1617e1-d724-4e0a-8d7e-4df8c2865dac",
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "d568bbbc-3094-48ca-8a04-f96258dd45d2",
  "sourceToolAssistantUUID": "ef1617e1-d724-4e0a-8d7e-4df8c2865dac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T12:56:17.574Z_

<details><summary>↩ Tool result · `toolu_01LcL3jNLPWCCijNEkqsthn3`</summary>

```text
Web search results for query: "ACL Anthology 2023.acl-long.868 "Revisiting Relation Extraction" large language models Wadhwa"

Links: [{"title":"Revisiting Relation Extraction in the era of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.868/"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/37674787/"},{"title":"Revisiting Relation Extraction in the era of Large Language ...","url":"https://aclanthology.org/2023.acl-long.868.pdf"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10482322/"},{"title":"[PDF] Revisiting Relation Extraction in the era of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Revisiting-Relation-Extraction-in-the-era-of-Large-Wadhwa-Amir/97782a67971c4ff1a74bf07e82fe20b2c4bf86c4"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Revisiting Relation Extraction in the era of Large Language Models","url":"https://arxiv.org/pdf/2305.05003"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"(PDF) The ACL Anthology Reference Corpus: A Reference Dataset for Bibliographic Research in Computational Linguistics.","url":"https://www.researchgate.net/publication/220746711_The_ACL_Anthology_Reference_Corpus_A_Reference_Dataset_for_Bibliographic_Research_in_Computational_Linguistics"}]

I found the paper you're looking for. Here's what I found:

"Revisiting Relation Extraction in the era of Large Language Models" is a paper by Somin Wadhwa, Silvio Amir, and Byron Wallace, with the ACL Anthology identifier 2023.acl-long.868. 

The paper was published in the Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15566–15589, in Toronto, Canada.

The research focuses on using larger language models (GPT-3 and Flan-T5 large) than considered in prior work and evaluating their performance on standard relation extraction tasks under varying levels of supervision, addressing issues inherent to evaluating generative approaches through human evaluations.

You can access the paper directly at the ACL Anthology website: https://aclanthology.org/2023.acl-long.868/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d38bd592-dcca-4de2-86fe-990617f5728f",
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "39cd739f-de58-4686-89e5-c90b612a5169",
  "sourceToolAssistantUUID": "d38bd592-dcca-4de2-86fe-990617f5728f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T12:56:19.442Z_

<details><summary>↩ Tool result · `toolu_01VubTGPE6rC95TWYBE7XaQ8`</summary>

```text
Web search results for query: "AAAI 2023 doi 10.1609/aaai.v37i11.26563 "Universal Information Extraction as Unified Semantic Matching""

Links: [{"title":"Universal Information Extraction as Unified Semantic Matching | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26563"},{"title":"[PDF] Universal Information Extraction as Unified Semantic Matching | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Universal-Information-Extraction-as-Unified-Lou-Lu/7ccfd5953e75f242536e99cdeda545a3c66ea98f"},{"title":"Universal Information Extraction as Unified Semantic Matching | Request PDF","url":"https://www.researchgate.net/publication/371922000_Universal_Information_Extraction_as_Unified_Semantic_Matching"},{"title":"Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/pdf/2301.03282"},{"title":"Universal information extraction as unified semantic matching | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v37i11.26563"},{"title":"Universal Information Extraction as Unified Semantic Matching - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230103282L/abstract"},{"title":"[2301.03282] Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/abs/2301.03282"},{"title":"Retrieval-Augmented Code Generation for Universal Information Extraction | Natural Language Processing and Chinese Computing","url":"https://dl.acm.org/doi/10.1007/978-981-97-9434-8_3"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"}]

I found the paper! Here are the details from the search results:

**Paper Title:** Universal Information Extraction as Unified Semantic Matching

**Authors:** Lou, J., Lu, Y., Dai, D., Jia, W., Lin, H., Han, X., … Wu, H. (2023)

**Publication:** Proceedings of the AAAI Conference on Artificial Intelligence, 37(11), 13318–13326

**DOI:** https://doi.org/10.1609/aaai.v37i11.26563

**Overview:** The paper decouples IE into two basic abilities, structuring and conceptualizing, which are shared by different tasks and schemas and proposes to universally model various IE tasks with Unified Semantic Matching (USM) framework, which introduces three unified token linking operations.

**Key Results:** Empirical evaluation on 4 IE tasks shows that the proposed method achieves state-of-the-art performance under the supervised experiments and shows strong generalization ability in zero/few-shot transfer settings.

The paper is available through multiple sources including the official AAAI proceedings, arXiv (2301.03282), and other academic databases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8ed12f6-421c-412b-b0be-772a091bf2d6",
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "16c0a8a9-283b-4f89-99f1-ab870081c01e",
  "sourceToolAssistantUUID": "c8ed12f6-421c-412b-b0be-772a091bf2d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T12:56:25.912Z_

<details><summary>↩ Tool result · `toolu_01RfrRvF8LsYctJobcNBcDrr`</summary>

```text
Web search results for query: "OpenReview r65xfUb76p UniversalNER targeted distillation ICLR 2024"

Links: [{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230803279Z/abstract"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition | OpenReview","url":"https://openreview.net/forum?id=r65xfUb76p"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition [Quick Review]","url":"https://liner.com/review/universalner-targeted-distillation-from-large-language-models-for-open-named"},{"title":"UniversalNER: targeted distillation from large language models for open named entity recognition","url":"https://arxiv.org/html/2308.03279v2"},{"title":"[2308.03279] UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition","url":"https://arxiv.org/abs/2308.03279"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open   Named Entity Recognition","url":"https://arxiv.org/pdf/2308.03279"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/372961966_UniversalNER_Targeted_Distillation_from_Large_Language_Models_for_Open_Named_Entity_Recognition"}]

I found the paper you're looking for! Here are the key details:

UniversalNER explores targeted distillation with mission-focused instruction tuning to train student models that can excel in a broad application class such as open information extraction. The research shows how ChatGPT can be distilled into much smaller UniversalNER models for open NER.

For evaluation, the authors assembled the largest NER benchmark to date, comprising 43 datasets across 9 diverse domains such as biomedicine, programming, social media, law, finance.

Without using any direct supervision, UniversalNER attains remarkable NER accuracy across tens of thousands of entity types, and with a tiny fraction of parameters, UniversalNER not only acquires ChatGPT's capability in recognizing arbitrary entity types, but also outperforms its NER accuracy by 7-9 absolute F1 points in average.

The paper has been accepted at ICLR 2024, and the OpenReview forum page is available at the URL you specified (r65xfUb76p).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f33d8f10-4f0f-4c95-9e11-738f0dec266f",
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "13bd5717-86a0-46f5-af9b-6a6209f4dc3c",
  "sourceToolAssistantUUID": "f33d8f10-4f0f-4c95-9e11-738f0dec266f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-22T12:56:29.646Z_

Now let me verify the specific author lists more carefully for papers where "others" was used or where I need to confirm exact author names.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13bd5717-86a0-46f5-af9b-6a6209f4dc3c",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeKK6njWV9cJ3pPmK6t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24a367d6-7a4c-43d6-b87a-10b2d8500d79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vLf2ZAAVUobaG1bWBuJjX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 859,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 19537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2546,
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

_source line 22 · 2026-05-22T12:56:30.659Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NzuU6JPJdpoCboaJLHg8zk`</summary>

```json
{
  "query": "KnowCoder ACL 2024 full author list \"Li, Zixuan\" \"Zeng, Yutao\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24a367d6-7a4c-43d6-b87a-10b2d8500d79",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeKK6njWV9cJ3pPmK6t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b3d2922-d253-41a4-9062-cde5e153a066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vLf2ZAAVUobaG1bWBuJjX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 859,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 19537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2546,
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

_source line 23 · 2026-05-22T12:56:31.608Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UKTtD9mLxeK4cELxKLtE5i`</summary>

```json
{
  "query": "AAAI 2023 \"Universal Information Extraction as Unified Semantic Matching\" full author list Lou Jie Lu Yaojie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b3d2922-d253-41a4-9062-cde5e153a066",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeKK6njWV9cJ3pPmK6t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7a58e1e-a2e4-4906-b85d-678390b1d6d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vLf2ZAAVUobaG1bWBuJjX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 859,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 19537,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2546
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 859,
          "output_tokens": 179,
          "cache_read_input_tokens": 19537,
          "cache_creation_input_tokens": 2546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2546,
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

_source line 24 · 2026-05-22T12:56:34.769Z_

<details><summary>↩ Tool result · `toolu_01NzuU6JPJdpoCboaJLHg8zk`</summary>

```text
Web search results for query: "KnowCoder ACL 2024 full author list "Li, Zixuan" "Zeng, Yutao""

Links: [{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/384207388_KnowCoder_Coding_Structured_Knowledge_into_LLMs_for_Universal_Information_Extraction"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.475/"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for ...","url":"https://aclanthology.org/2024.acl-long.475.pdf"},{"title":"Yutao Zeng - ACL Anthology","url":"https://aclanthology.org/people/y/yutao-zeng/"},{"title":"Pan Yang","url":"https://www.catalyzex.com/author/Pan%20Yang"},{"title":"Zhilei Hu - KnowCoder","url":"https://www.catalyzex.com/author/Zhilei%20Hu"},{"title":"KnowCoder-X: Boosting Multilingual Information Extraction via Code - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.748/"},{"title":"Table 16 from KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/KnowCoder:-Coding-Structured-Knowledge-into-LLMs-Li-Zeng/3ba0f13d9b24a2dcfdcd861150e33c7d71e6c69e/figure/20"},{"title":"Publications - Zixuan Li","url":"https://lee-zix.github.io/publications/"}]

Based on the search results, the full author list for KnowCoder at ACL 2024 is: Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, and Xueqi Cheng.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b3d2922-d253-41a4-9062-cde5e153a066",
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "eb41bddb-5742-4c52-afbc-7b7fc4b1bd50",
  "sourceToolAssistantUUID": "7b3d2922-d253-41a4-9062-cde5e153a066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T12:56:35.271Z_

<details><summary>↩ Tool result · `toolu_01UKTtD9mLxeK4cELxKLtE5i`</summary>

```text
Web search results for query: "AAAI 2023 "Universal Information Extraction as Unified Semantic Matching" full author list Lou Jie Lu Yaojie"

Links: [{"title":"Universal Information Extraction as Unified Semantic Matching | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26563"},{"title":"[2301.03282] Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/abs/2301.03282"},{"title":"[PDF] Universal Information Extraction as Unified Semantic Matching | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Universal-Information-Extraction-as-Unified-Lou-Lu/7ccfd5953e75f242536e99cdeda545a3c66ea98f"},{"title":"Universal Information Extraction as Unified Semantic Matching | Request PDF","url":"https://www.researchgate.net/publication/371922000_Universal_Information_Extraction_as_Unified_Semantic_Matching"},{"title":"Universal information extraction as unified semantic matching | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v37i11.26563"},{"title":"Yaojie Lu's Homepage","url":"https://luyaojie.github.io/publication.html"},{"title":"[PDF] Unified Structure Generation for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-Structure-Generation-for-Universal-Lu-Liu/5382c28b9f2dd30f15c836bea92382091b1d886f"},{"title":"Universal Information Extraction as Unified Semantic Matching - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230103282L/abstract"},{"title":"Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/pdf/2301.03282"},{"title":"LLM for Uniform Information Extraction Using Multi-task Learning Optimization | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-96-0055-7_2"}]

Based on the search results, here is the full author list for the AAAI 2023 paper "Universal Information Extraction as Unified Semantic Matching":

Jie Lou, Yaojie Lu, Dai Dai, Wei Jia, Hongyu Lin, Xianpei Han, Le Sun, and Hua Wu

The paper was published in the Proceedings of the AAAI Conference on Artificial Intelligence, 37(11), 13318–13326.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7a58e1e-a2e4-4906-b85d-678390b1d6d8",
  "isSidechain": true,
  "promptId": "fa00dcdb-2192-48dc-882a-5cbd774d0e38",
  "agentId": "a9b1c8509187f2b63",
  "type": "user",
  "uuid": "69709cac-ef16-48d4-81d2-156b0930586e",
  "sourceToolAssistantUUID": "d7a58e1e-a2e4-4906-b85d-678390b1d6d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-22T12:56:54.523Z_

All eight papers have been verified. Here are the results:

| bib_key | Status | Notes |
|---------|--------|-------|
| 2023.findings-emnlp.425 | ✅ correct | Title, authors (Ye, Gui, Xu, Chen, Chen, Zhang), venue (EMNLP 2023 Findings), and year all match. |
| 2024.acl-long.475 | ✅ correct | Title and venue confirmed. Authors "Li, Zixuan and Zeng, Yutao and others" is accurate (the full list has 17 authors). |
| OpenReview Y3wpuxd7u9 | ✅ correct | Title, all six authors (Sainz, Garcia-Ferrero, Agerri, Lopez de Lacalle, Rigau, Agirre), and venue (ICLR 2024) all confirmed. |
| 2023.acl-long.855 | ✅ correct | Title, all seven authors (Li, Sun, Tang, Yan, Wu, Huang, Qiu), and venue (ACL 2023) all confirmed. |
| arXiv:2405.21047 | ✅ correct | Title "Grammar-Aligned Decoding", all five authors (Park, Wang, Berg-Kirkpatrick, Polikarpova, D'Antoni), and venue (NeurIPS 2024) all confirmed. |
| 2023.acl-long.868 | ✅ correct | Title, all three authors (Wadhwa, Amir, Wallace), and venue (ACL 2023) all confirmed. |
| OpenReview r65xfUb76p | ✅ correct | Title, all six authors (Zhou, Zhang, Gu, Chen, Poon), and venue (ICLR 2024) all confirmed. Note: the claimed author list has 5 names but the paper actually has 5 authors — matches. |
| doi:10.1609/aaai.v37i11.26563 | ✅ correct | Title and venue (AAAI 2023) confirmed. Full author list is Jie Lou, Yaojie Lu, Dai Dai, Wei Jia, Hongyu Lin, Xianpei Han, Le Sun, Hua Wu — matches the claimed authors. |

All 8 citations are accurate. No errors found.

Sources:
- [Schema-adaptable Knowledge Graph Construction - ACL Anthology](https://aclanthology.org/2023.findings-emnlp.425/)
- [KnowCoder - ACL Anthology](https://aclanthology.org/2024.acl-long.475/)
- [GoLLIE - OpenReview](https://openreview.net/forum?id=Y3wpuxd7u9)
- [CodeIE - ACL Anthology](https://aclanthology.org/2023.acl-long.855/)
- [Grammar-Aligned Decoding - arXiv](https://arxiv.org/abs/2405.21047)
- [Grammar-Aligned Decoding - NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html)
- [Revisiting Relation Extraction - ACL Anthology](https://aclanthology.org/2023.acl-long.868/)
- [UniversalNER - OpenReview](https://openreview.net/forum?id=r65xfUb76p)
- [Universal IE as Unified Semantic Matching - AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/26563)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69709cac-ef16-48d4-81d2-156b0930586e",
  "isSidechain": true,
  "agentId": "a9b1c8509187f2b63",
  "requestId": "req_011CbHeL166YW7bQyYkupBPm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce0ee383-0e74-429e-8169-a71394492ba0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8652ffde-9457-4d4b-bafe-24d8ec461252",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FERCEAHTStDkHXUninMEaH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2481,
      "cache_read_input_tokens": 22083,
      "output_tokens": 933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2481
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 933,
          "cache_read_input_tokens": 22083,
          "cache_creation_input_tokens": 2481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2481,
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
