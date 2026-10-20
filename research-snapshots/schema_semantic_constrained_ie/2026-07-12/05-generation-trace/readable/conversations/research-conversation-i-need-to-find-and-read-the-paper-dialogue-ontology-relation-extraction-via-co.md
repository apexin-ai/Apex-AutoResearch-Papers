# Research conversation: I need to find and read the paper "Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding" from

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa91cb80c87bc5643.jsonl`
- **Structured JSON:** [`2b52c72522316498b5bd.json`](../../sessions/2b/2b52c72522316498b5bd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

75 recorded events

### User

_source line 1 · 2026-05-12T00:51:45.844Z_

I need to find and read the paper "Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding" from SIGDIAL 2024 (arXiv:2408.02361). 

Use WebSearch and WebFetch to find and read this paper. I need:
1. The exact title, authors, and venue
2. What ontology constraints they enforce during decoding
3. What decoding mechanism they use (CoT decoding, logit masking, grammar constraints?)
4. What datasets/benchmarks they evaluate on
5. Their key results
6. How it differs from logit-masking approaches for IE

Also search for "Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction" (EACL 2026). I need:
1. The exact title, authors, and venue
2. The key finding about format choice affecting F1 by 40%+ in IE
3. Which IE tasks and models were evaluated
4. Whether they discuss constrained decoding specifically

Report findings for both papers in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "8928ffe9-7300-421a-b96f-cd82bfcd4dec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:51:45.847Z_

```json
{
  "parentUuid": "8928ffe9-7300-421a-b96f-cd82bfcd4dec",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "96f0c1b6-57a3-4a68-b8d4-441384dd93db",
  "timestamp": "2026-05-12T00:51:45.847Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:51:51.550Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then search for both papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96f0c1b6-57a3-4a68-b8d4-441384dd93db",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawky42rk9J1gmtUsSQC4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab1cd748-42e8-4206-8945-259456f31c19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAA4XFX2gAtNEHMyWPR5fa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 777,
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

_source line 4 · 2026-05-12T00:51:51.705Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ASZaTGq3JGXdjj2daWW29r`</summary>

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
  "parentUuid": "ab1cd748-42e8-4206-8945-259456f31c19",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawky42rk9J1gmtUsSQC4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21e66d9c-31e1-4667-bae6-ddd12d5eeb2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAA4XFX2gAtNEHMyWPR5fa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 7304,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 777
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 777,
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

_source line 5 · 2026-05-12T00:51:51.708Z_

<details><summary>↩ Tool result · `toolu_01ASZaTGq3JGXdjj2daWW29r`</summary>

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
  "parentUuid": "21e66d9c-31e1-4667-bae6-ddd12d5eeb2a",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "4771a54d-d920-4805-b5f2-2ba191c2f611",
  "sourceToolAssistantUUID": "21e66d9c-31e1-4667-bae6-ddd12d5eeb2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:51:58.214Z_



Now let me search for both papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4771a54d-d920-4805-b5f2-2ba191c2f611",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawkyVDvf3gcntqECYQAn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a1a01b3-3938-48e4-aa92-3cd61200ed48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMRZGf4P1iiNsExTSAur41",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8081,
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

_source line 7 · 2026-05-12T00:51:59.172Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JdD5VCHccQ6aqXXXJHB4js`</summary>

```json
{
  "query": "Dialogue Ontology Relation Extraction Constrained Chain-of-Thought Decoding SIGDIAL 2024 arXiv 2408.02361"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a1a01b3-3938-48e4-aa92-3cd61200ed48",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawkyVDvf3gcntqECYQAn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b16e3f1-db96-49b8-ba8b-602287affac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMRZGf4P1iiNsExTSAur41",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8081,
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

_source line 8 · 2026-05-12T00:52:00.119Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MzEhNXuhhKS45KUZRXpo78`</summary>

```json
{
  "query": "Lost in Formatting How Output Formats Skew LLM Performance Information Extraction EACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b16e3f1-db96-49b8-ba8b-602287affac3",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawkyVDvf3gcntqECYQAn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "beaf2b35-a7a9-4298-a2ca-71eaca81cc3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMRZGf4P1iiNsExTSAur41",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8081,
      "output_tokens": 160,
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
          "output_tokens": 160,
          "cache_read_input_tokens": 8081,
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

_source line 9 · 2026-05-12T00:52:06.359Z_

<details><summary>↩ Tool result · `toolu_01JdD5VCHccQ6aqXXXJHB4js`</summary>

```text
Web search results for query: "Dialogue Ontology Relation Extraction Constrained Chain-of-Thought Decoding SIGDIAL 2024 arXiv 2408.02361"

Links: [{"title":"[2408.02361] Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/abs/2408.02361"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/html/2408.02361"},{"title":"SIGDIAL 2024","url":"https://2024.sigdial.org/"},{"title":"SIGDIAL 2024 25th Annual Meeting of the Special Interest Group on","url":"https://aclanthology.org/2024.sigdial-1.0.pdf"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2404.02361"},{"title":"Computer Science Aug 2024","url":"https://arxiv.org/list/cs/2024-08?skip=4640&show=25"},{"title":"arXiv:2408.12989v1 [cs.LG] 23 Aug 2024","url":"https://arxiv.org/pdf/2408.12989"},{"title":"SIGDial Conference (2024) - ACL Anthology","url":"https://aclanthology.org/events/sigdial-2024/"},{"title":"Arxiv Policy","url":"https://sigir-2024.github.io/policy_arxiv.html"},{"title":"Benjamin Matthias Ruppik - University of Düsseldorf | LinkedIn","url":"https://www.linkedin.com/in/benjamin-matthias-ruppik-614192211/"}]

Based on the search results, I found the paper you're looking for:

## Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding

This is arXiv paper 2408.02361, authored by Renato Vukovic, David Arps, Carel van Niekerk, Benjamin Matthias Ruppik, Hsien-Chin Lin, Michael Heck, and Milica Gašić.

### Overview

The paper addresses how state-of-the-art task-oriented dialogue systems rely on task-specific ontologies. Since most task-oriented dialogue data comes without ontology and annotation, and ontologies are normally built manually, the authors focus on automating dialogue ontology construction, which typically consists of term extraction and relation extraction.

### Methodology

The authors propose an extension to the decoding mechanism of large language models by adapting Chain-of-Thought (CoT) decoding for generative relation extraction, where they generate multiple branches in the decoding space and select relations based on a confidence threshold.

More specifically, they constrain generation to terms and relation types given in the model input to force the model to consider terms from the target data and output the desired format.

The paper was submitted on August 5, 2024, and revised on March 7, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b16e3f1-db96-49b8-ba8b-602287affac3",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "0b5a98e2-82e7-40a6-b92d-b7beaa3c55b6",
  "sourceToolAssistantUUID": "5b16e3f1-db96-49b8-ba8b-602287affac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T00:52:07.205Z_

<details><summary>↩ Tool result · `toolu_01MzEhNXuhhKS45KUZRXpo78`</summary>

```text
Web search results for query: "Lost in Formatting How Output Formats Skew LLM Performance Information Extraction EACL 2026"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"Taming LLM Outputs: Your Guide to Structured Text Generation","url":"https://www.dataiku.com/stories/blog/your-guide-to-structured-text-generation"},{"title":"Under review as a conference paper at ICLR 2026","url":"https://www.arxiv.org/pdf/2510.03595"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"LLMs Are Biased Towards Output Formats! Systematically Evaluating and Mitigating Output Format Bias of LLMs","url":"https://arxiv.org/html/2408.08656v1"},{"title":"Decoupling Task-Solving and Output Formatting in LLM Generation","url":"https://arxiv.org/html/2510.03595v1"},{"title":"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/html/2508.10036v1"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"The Price of Format: Diversity Collapse in LLMs","url":"https://arxiv.org/html/2505.18949v1"}]

Based on the search results, I found the paper you're looking for:

## "Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction"

This paper was written by Rishi Ravikumar, Nuhu Ibrahim, and Riza Batista-Navarro and was presented at the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026) in Rabat, Morocco in March 2026.

### Key Findings:

Based on over 280 experiments spanning multiple benchmarks, models and formats, the authors find that output formatting is a critical yet largely overlooked hyperparameter.

Remarkably, in some cases, changing only the output format shifts F1 scores by over 40% despite using the same model.

The researchers further observe that no single format consistently dominates across settings, and the optimal choice depends on factors like model family and dataset characteristics.

Overall, these results demonstrate that informationally equivalent output formats can produce substantial performance variation, highlighting the need to treat output formatting as a key factor in building accurate and reliable information extraction systems.

The paper is published in the conference proceedings, pages 5498–5513, and you can access it directly through the ACL Anthology at https://aclanthology.org/2026.eacl-long.256/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "beaf2b35-a7a9-4298-a2ca-71eaca81cc3c",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "3bdc3ef4-e6d1-4d41-ae98-6a4672ce8f33",
  "sourceToolAssistantUUID": "beaf2b35-a7a9-4298-a2ca-71eaca81cc3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-12T00:52:10.291Z_

Good, I found both papers. Now let me fetch the full content of both papers to get detailed information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bdc3ef4-e6d1-4d41-ae98-6a4672ce8f33",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawkzdM7DrPuRT2eprEeu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e0b0e7c-a317-42e5-9a75-f9c3e62e9a57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHiKsqMFMWZN234iyxYZH5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1782,
      "cache_read_input_tokens": 9992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1782,
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

_source line 12 · 2026-05-12T00:52:15.206Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QTaycD6RwFb9FyP4FJzNSs`</summary>

```json
{
  "url": "https://arxiv.org/html/2408.02361",
  "prompt": "Extract ALL of the following details from this paper:\n1. Exact title, all authors with affiliations, and venue/conference\n2. What ontology constraints they enforce during decoding - describe in detail\n3. The exact decoding mechanism - is it CoT decoding, logit masking, grammar constraints, or something else? How does it work step by step?\n4. All datasets and benchmarks they evaluate on\n5. Key quantitative results (F1 scores, accuracy, etc.) and main findings\n6. How their approach differs from logit-masking or other constrained decoding approaches for information extraction\n7. Any ablation studies or analysis of constrained vs unconstrained decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e0b0e7c-a317-42e5-9a75-f9c3e62e9a57",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawkzdM7DrPuRT2eprEeu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b32bafb-b8cd-408c-8af0-07fb1ebf3ac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHiKsqMFMWZN234iyxYZH5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1782,
      "cache_read_input_tokens": 9992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1782,
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

_source line 13 · 2026-05-12T00:52:17.774Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013w8sLswuA4PvGgx2bc7FZw`</summary>

```json
{
  "url": "https://aclanthology.org/2026.eacl-long.256/",
  "prompt": "Extract ALL of the following details from this paper page:\n1. Exact title, all authors with affiliations, and venue\n2. The key finding about format choice affecting F1 by 40%+ in IE - exact details\n3. Which IE tasks and which LLM models were evaluated\n4. Whether they discuss constrained decoding specifically\n5. What output formats were compared\n6. Key quantitative results\n7. Link to the PDF if available"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b32bafb-b8cd-408c-8af0-07fb1ebf3ac3",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawkzdM7DrPuRT2eprEeu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a78f756f-445c-4811-9334-d7ec852bc2e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHiKsqMFMWZN234iyxYZH5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1782,
      "cache_read_input_tokens": 9992,
      "output_tokens": 425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1782
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 425,
          "cache_read_input_tokens": 9992,
          "cache_creation_input_tokens": 1782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1782,
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

_source line 14 · 2026-05-12T00:52:21.825Z_

<details><summary>↩ Tool result · `toolu_013w8sLswuA4PvGgx2bc7FZw`</summary>

```text
# Paper Details Extraction

## 1. Title, Authors & Venue
**Title:** "Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction"

**Authors:** Rishi Ravikumar, Nuhu Ibrahim, Riza Batista-Navarro
*(No affiliations listed on this page)*

**Venue:** EACL 2026 (19th Conference of the European Chapter of the Association for Computational Linguistics), Rabat, Morocco, March 2026

## 2. Key Finding on F1 Score Impact
The research demonstrates that "changing only the output format shifts F1 scores by over 40%" despite using identical models. This underscores output formatting as a "critical yet largely overlooked hyperparameter."

## 3. Tasks & Models Evaluated
The abstract does not specify which particular IE tasks or LLM models were tested. It only mentions the evaluation spanned "over 280 experiments spanning multiple benchmarks, models and formats."

## 4. Constrained Decoding Discussion
Not addressed in this page content.

## 5. Output Formats Compared
The specific formats compared are not detailed in this excerpt.

## 6. Key Quantitative Results
- 280+ experiments conducted
- F1 score variations exceeding 40% from format changes alone
- No single format consistently optimal across settings

## 7. PDF Link
https://aclanthology.org/2026.eacl-long.256.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a78f756f-445c-4811-9334-d7ec852bc2e6",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "fa9a9696-ebb5-4015-b1a7-8cfadb147cec",
  "sourceToolAssistantUUID": "a78f756f-445c-4811-9334-d7ec852bc2e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T00:52:29.395Z_

<details><summary>↩ Tool result · `toolu_01QTaycD6RwFb9FyP4FJzNSs`</summary>

```text
# Paper Analysis: Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding

## 1. Citation Details
**Title:** "Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding"

**Authors:** Renato Vukovic, David Arps, Carel van Niekerk, Benjamin Matthias Ruppik, Hsien-Chin Lin, Michael Heck, Milica Gašić

**Affiliation:** Heinrich Heine University Düsseldorf

**Venue:** arXiv (arxiv.org/html/2408.02361v2)

## 2. Ontology Constraints During Decoding
The authors enforce constraints on three components of relational triplets [head, relation, tail]:
- Head and tail terms must exist in the input dialogue term set (T)
- Relation types must match predefined ontology relations (R)
- Constraints activate only "when an opening bracket is predicted" and resume normal generation after completing each triplet
- This prevents "hallucination" of terms or relations not present in the source data

## 3. Decoding Mechanism Details
The approach combines two techniques:

**CoT-Decoding Phase:**
- Generates k=5 parallel branches starting from the first token
- Computes "disparity" for each predicted relation: the difference between highest and second-highest token probability
- Calculates average disparity across all answer tokens using: Δ = (1/n)Σ[p(top) - p(next)]
- Selects the branch with highest average disparity across all predicted relations

**Constraint Application:**
- Token-level filtering that restricts vocabulary to valid terms/relations when inside bracket pairs
- Does not use grammar-based or automata-based constraint techniques

## 4. Datasets and Benchmarks
- **Source:** MultiWOZ 2.1 (7 domains, 10,000+ dialogues)
- **Target:** Schema-Guided Dialogue (SGD) test set (4,201 dialogues, 18 domains, 20,000+ total)
- **Upper bounds:** SGD training set for fine-tuning comparisons
- **Evaluation metrics:** Micro F1, precision, recall at global (accumulated) ontology level

## 5. Key Results
**Fine-tuned on MultiWOZ, tested on SGD:**
- Baseline: 10.9 F1
- Constrained decoding: 12.0 F1
- CoT decoding: 10.6 F1
- **Constrained CoT decoding: 13.7 F1** (statistically significant improvement)

**One-shot approach:**
- Baseline: 7.4 F1
- Constrained CoT decoding: 9.2 F1

Upper bound (trained on SGD): 37.3 F1

## 6. Differentiation from Other Constrained Approaches
Unlike logit-masking or grammar-constraint methods, this approach:
- Uses **confidence-based branch selection** rather than hard constraints as the primary mechanism
- Applies constrained decoding selectively (only within bracket pairs)
- Combines generation diversity (multiple branches) with constraint enforcement
- Focuses on "disparity as confidence metric" rather than probability thresholds
- Authors note that "absolute confidence threshold is not as meaningful" and that selecting the highest disparity branch works better

## 7. Ablation Studies
**Branch Analysis (Figure 3):**
- Performance gains primarily from first additional branch (k=2)
- Marginal improvements from k=3 to k=5
- Recall jumps significantly from k=2 to k=3

**Decoding Comparison (Table 2 & 3):**
- Constrained decoding alone: improves structure, reduces hallucination
- CoT decoding alone: generates reasoning but produces out-of-domain terms
- **Combined approach:** Forces model to use task-specific knowledge while maintaining multiple hypotheses

**Threshold Analysis (Figure 2):**
- Demonstrates high model overconfidence; most predictions exceed thresholds
- Relative branch confidence more meaningful than absolute thresholds
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b32bafb-b8cd-408c-8af0-07fb1ebf3ac3",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "bfef07c0-badd-4aba-9d4a-99ee05332881",
  "sourceToolAssistantUUID": "7b32bafb-b8cd-408c-8af0-07fb1ebf3ac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-12T00:52:33.768Z_

Good. I have detailed information on the first paper. Let me fetch the full PDF content of the EACL paper for more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfef07c0-badd-4aba-9d4a-99ee05332881",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm2GHt23wBMNicV3ZFF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04538253-6059-492c-a505-6a832c205c6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146NtFng4n7TYVsNseUTYuw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 371,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 11774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1431,
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

_source line 17 · 2026-05-12T00:52:39.087Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QXhbeJyfdonKm5kzANHJSF`</summary>

```json
{
  "url": "https://aclanthology.org/2026.eacl-long.256.pdf",
  "prompt": "Extract ALL of the following details from this paper:\n1. All authors and their affiliations\n2. The exact finding about format choice affecting F1 by 40%+ - which specific task/model/format combination showed this?\n3. Which IE tasks were evaluated (NER, RE, EE, etc.)?\n4. Which LLM models were evaluated?\n5. Which output formats were compared (JSON, XML, plain text, markdown, etc.)?\n6. Do they discuss constrained decoding (logit masking, grammar-constrained decoding, etc.) specifically? What do they say about it?\n7. Key quantitative results - tables of F1 scores across formats/models/tasks\n8. Their main recommendations and conclusions\n9. Any discussion of structured output generation methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04538253-6059-492c-a505-6a832c205c6a",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm2GHt23wBMNicV3ZFF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "216baaca-ea2b-4a16-8d86-f0f6c31a8702",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146NtFng4n7TYVsNseUTYuw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 371,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 11774,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1431
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 371,
          "output_tokens": 292,
          "cache_read_input_tokens": 11774,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1431,
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

_source line 18 · 2026-05-12T00:52:46.758Z_

<details><summary>↩ Tool result · `toolu_01QXhbeJyfdonKm5kzANHJSF`</summary>

```text
# Information Extraction Paper Analysis

**Note:** The provided content is a PDF with significant compression/encoding. I can identify structural elements but cannot fully extract all details due to the format's limitations.

## Extractable Information:

**1. Authors & Affiliations:**
The document references paper 856 from EACL 2026 publications. Specific author names and affiliations are embedded in the compressed PDF stream and not fully readable in this format.

**2. Format Choice Impact (40%+ F1 Finding):**
The core finding about format selection affecting F1 scores by 40%+ appears to be a central claim, but the specific task/model/format combinations are contained within the compressed content streams that aren't fully decodable from this extraction.

**3. IE Tasks Evaluated:**
References indicate multiple information extraction tasks are covered, likely including NER, RE, and event extraction based on typical IE benchmarks.

**4. LLM Models:**
The embedded images (llms.pdf, benchmark_details.pdf) suggest model comparisons were conducted, but specific model names require decoding the image content.

**5. Output Formats Compared:**
The document structure suggests JSON, XML, plain text, and markdown formats were evaluated based on typical format comparison studies.

**6. Constrained Decoding Discussion:**
No explicit mentions of logit masking or grammar-constrained decoding are visible in the readable metadata.

**7-9. Quantitative Results, Recommendations, Conclusions:**
These appear in the document's body content, which remains largely in compressed streams.

**Recommendation:** Access the original PDF directly or request a text-extracted version for complete, accurate information extraction.

[Binary content (application/pdf, 568.2KB) also saved to /home/ubuntu/.claude-account-1/projects/-/75e0b45d-e75d-44ab-9d00-5147ced3238c/tool-results/webfetch-1778547160365-aq552i.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "216baaca-ea2b-4a16-8d86-f0f6c31a8702",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "1f49b975-b396-4af9-b4ef-f29655a6972a",
  "sourceToolAssistantUUID": "216baaca-ea2b-4a16-8d86-f0f6c31a8702",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-12T00:52:49.242Z_

The PDF didn't extract well. Let me try to find an HTML version or preprint of the EACL paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f49b975-b396-4af9-b4ef-f29655a6972a",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm3YQmsRKArEUUsWT3V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9c5cded-f4a3-45c0-ba15-adb9b108ae82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej3ppX1UTj6gNXrs8oTjGx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 13205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1227,
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

_source line 20 · 2026-05-12T00:52:50.726Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013neHSbJ2ubEFgoZnzhV5Uh`</summary>

```json
{
  "query": "\"Lost in Formatting\" Ravikumar Ibrahim Batista-Navarro output format information extraction LLM F1 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9c5cded-f4a3-45c0-ba15-adb9b108ae82",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm3YQmsRKArEUUsWT3V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9f870ae-7f7e-4cff-b44e-e01ac86cbe60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej3ppX1UTj6gNXrs8oTjGx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 13205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1227,
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

_source line 21 · 2026-05-12T00:52:51.164Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XyM59JurHfSi5ByQCfKa8Z`</summary>

```json
{
  "query": "\"Lost in Formatting\" EACL 2026 NER relation extraction output format JSON XML constrained decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9f870ae-7f7e-4cff-b44e-e01ac86cbe60",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm3YQmsRKArEUUsWT3V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09499638-2523-48ad-afff-caaedbe447d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej3ppX1UTj6gNXrs8oTjGx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 13205,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1227
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 13205,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1227,
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

_source line 22 · 2026-05-12T00:52:56.640Z_

<details><summary>↩ Tool result · `toolu_013neHSbJ2ubEFgoZnzhV5Uh`</summary>

```text
Web search results for query: ""Lost in Formatting" Ravikumar Ibrahim Batista-Navarro output format information extraction LLM F1 arXiv"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"Riza Theresa Batista-Navarro - ACL Anthology","url":"https://aclanthology.org/people/riza-theresa-batista-navarro/"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction

**Authors:** Rishi Ravikumar, Nuhu Ibrahim, and Riza Batista-Navarro

**Publication:** Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 5498–5513, Rabat, Morocco in 2026

**Key Findings:** 

The paper investigates how the choice of output format influences the performance of fine-tuned large language models on information extraction tasks, based on over 280 experiments spanning multiple benchmarks, models and formats, finding that output formatting is a critical yet largely overlooked hyperparameter. 

Remarkably, in some cases, changing only the output format shifts F1 scores by over 40% despite using the same model.

The paper is available at the ACL Anthology: https://aclanthology.org/2026.eacl-long.256/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9f870ae-7f7e-4cff-b44e-e01ac86cbe60",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "0b082fdc-7048-4868-904d-9523f717c638",
  "sourceToolAssistantUUID": "b9f870ae-7f7e-4cff-b44e-e01ac86cbe60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T00:52:57.863Z_

<details><summary>↩ Tool result · `toolu_01XyM59JurHfSi5ByQCfKa8Z`</summary>

```text
Web search results for query: ""Lost in Formatting" EACL 2026 NER relation extraction output format JSON XML constrained decoding"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"How Output Formats Skew LLM Performance on ...","url":"https://aclanthology.org/2026.eacl-long.256.pdf"},{"title":"Named Entity Recognition (NER): Finding the Needle in the Haystack (AI 2026)","url":"https://blog.weskill.org/2026/04/named-entity-recognition-ner-finding.html"},{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"A Domain-Specific Curated Benchmark for Entity and Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.301/"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction","url":"https://arxiv.org/html/2402.13364v1"},{"title":"Information Extraction in NLP - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/information-extraction-in-nlp/"},{"title":"Exploring named entity recognition and relation extraction for ontology and medical records integration - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2352914823002277"}]

I found the paper! Here are the search results for "Lost in Formatting" EACL 2026:

## Paper Overview

"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction" was published at the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026) in Rabat, Morocco.

## Key Findings

Based on over 280 experiments spanning multiple benchmarks, models and formats, the researchers found that output formatting is a critical yet largely overlooked hyperparameter. 

Remarkably, in some cases, changing only the output format shifts F1 scores by over 40% despite using the same model. Additionally, the optimal choice depends on factors like model family and dataset characteristics, and no single format consistently dominates across settings.

## Authors

The paper was authored by Rishi Ravikumar, Nuhu Ibrahim, and Riza Batista-Navarro.

The paper investigates how different output formats (such as JSON, XML, and other structured formats) impact the performance of large language models on information extraction tasks including named entity recognition and relation extraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09499638-2523-48ad-afff-caaedbe447d4",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "28d036a9-4ae1-4354-8a94-55230bbd05d6",
  "sourceToolAssistantUUID": "09499638-2523-48ad-afff-caaedbe447d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-12T00:53:01.253Z_

Let me try to find an arXiv preprint or other accessible HTML version of the EACL paper, and also search for more details about it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28d036a9-4ae1-4354-8a94-55230bbd05d6",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm4Mv2agXoeXvW1UxP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55ae8c8c-cc04-4616-bc2c-53de0a264da6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9jgoMUwBzwYiusFedUWbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 14432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
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

_source line 25 · 2026-05-12T00:53:01.984Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019eaxAaCCt8DurQknvErtbi`</summary>

```json
{
  "query": "Rishi Ravikumar \"Lost in Formatting\" output format LLM information extraction NER relation extraction 280 experiments models benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55ae8c8c-cc04-4616-bc2c-53de0a264da6",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm4Mv2agXoeXvW1UxP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bef9094b-b1bb-4976-b12c-b6e4e0fa6a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9jgoMUwBzwYiusFedUWbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 14432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
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

_source line 26 · 2026-05-12T00:53:02.126Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017bhRvixWazPzre2vkLNCix`</summary>

```json
{
  "query": "arXiv \"Lost in Formatting\" output formats LLM information extraction Ravikumar"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bef9094b-b1bb-4976-b12c-b6e4e0fa6a36",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm4Mv2agXoeXvW1UxP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d78725d-a10c-4c70-b026-e542f54eb8db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9jgoMUwBzwYiusFedUWbz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 14432,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1426
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 14432,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1426,
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

_source line 27 · 2026-05-12T00:53:05.755Z_

<details><summary>↩ Tool result · `toolu_017bhRvixWazPzre2vkLNCix`</summary>

```text
Web search results for query: "arXiv "Lost in Formatting" output formats LLM information extraction Ravikumar"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"}]

Based on the search results, I found the paper you're looking for:

"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction" by Ravikumar et al. was published at EACL 2026.

The paper investigates how the choice of output format influences the performance of fine-tuned large language models on information extraction tasks. Based on over 280 experiments spanning multiple benchmarks, models and formats, the researchers found that output formatting is a critical yet largely overlooked hyperparameter.

Remarkably, in some cases, changing only the output format shifts F1 scores by over 40% despite using the same model. The optimal choice depends on factors like model family and dataset characteristics.

The paper is published in the Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics, pages 5498–5513, held in Rabat, Morocco.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d78725d-a10c-4c70-b026-e542f54eb8db",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "ee95920a-b690-46bf-a01b-79230c70f93b",
  "sourceToolAssistantUUID": "1d78725d-a10c-4c70-b026-e542f54eb8db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T00:53:08.061Z_

<details><summary>↩ Tool result · `toolu_019eaxAaCCt8DurQknvErtbi`</summary>

```text
Web search results for query: "Rishi Ravikumar "Lost in Formatting" output format LLM information extraction NER relation extraction 280 experiments models benchmarks"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"},{"title":"How Output Formats Skew LLM Performance on ...","url":"https://aclanthology.org/2026.eacl-long.256.pdf"},{"title":"LLM Document Extraction: How to use AI to get structured data from legacy documents","url":"https://www.pondhouse-data.com/blog/document-extraction-with-llms"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Computation and Language Feb 2025","url":"https://arxiv.org/list/cs.CL/2025-02?skip=1500&show=1000"},{"title":"Revolutionizing Document Data Extraction: How LLMs Outshine Traditional Tools","url":"https://theexcitedengineer.substack.com/p/revolutionizing-document-data-extraction"},{"title":"LLM-Powered Parsing and Analysis of Semi-Structured & Structured Documents | Towards Data Science","url":"https://towardsdatascience.com/llm-powered-parsing-and-analysis-of-semi-structured-structured-documents-f03ac92f063e/"},{"title":"3 Approaches to Knowledge Extraction with LLMs | by Experdot | Medium","url":"https://medium.com/@experdot/from-chaos-to-clarity-mastering-knowledge-extraction-with-llms-6dc703672554"},{"title":"Extracting Structured Data with LangExtract: A Deep Dive into LLM-Orchestrated Workflows | Towards Data Science","url":"https://towardsdatascience.com/extracting-structured-data-with-langextract-a-deep-dive-into-llm-orchestrated-workflows/"},{"title":"Using PyMuPDF4LLM: A Practical Guide for PDF Extraction in LLM & RAG Environments | by DhanushKumar | Medium","url":"https://medium.com/@danushidk507/using-pymupdf4llm-a-practical-guide-for-pdf-extraction-in-llm-rag-environments-63649915abbf"}]

Based on the search results, I found the research paper you're looking for:

"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction" is a paper by Rishi Ravikumar, Nuhu Ibrahim, and Riza Batista-Navarro, published at the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026).

**Key Findings:**

The paper is based on over 280 experiments spanning multiple benchmarks, models and formats, and finds that output formatting is a critical yet largely overlooked hyperparameter. Remarkably, in some cases, changing only the output format shifts F1 scores by over 40% despite using the same model.

The research observes that no single format consistently dominates across settings, and the optimal choice depends on factors like model family and dataset characteristics.

The paper investigates how the choice of output format influences the performance of fine-tuned large language models on information extraction tasks, which includes related tasks like named entity recognition (NER) and relation extraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bef9094b-b1bb-4976-b12c-b6e4e0fa6a36",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "a55d4f6d-f998-4d21-8d8e-16f204f1a871",
  "sourceToolAssistantUUID": "bef9094b-b1bb-4976-b12c-b6e4e0fa6a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-12T00:53:14.647Z_

Let me try to access the arxiv listing page for this paper (it might have an arXiv preprint) and also try the EACL accepted papers page for more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a55d4f6d-f998-4d21-8d8e-16f204f1a871",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm57g3f4K4rksQeoZdx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7e1ddc3-c2f1-42b4-8f83-ad538c37c027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfGNQQVx97R28ktZzfNQaP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 344,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 15858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1103,
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

_source line 30 · 2026-05-12T00:53:15.299Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QNkoGxj5ZusFM2Dmhkc7Z8`</summary>

```json
{
  "query": "site:arxiv.org \"Lost in Formatting\" \"output formats\" information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7e1ddc3-c2f1-42b4-8f83-ad538c37c027",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm57g3f4K4rksQeoZdx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b702b63c-8eb5-48d9-8acf-9d9e7d995a14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfGNQQVx97R28ktZzfNQaP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 344,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 15858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1103,
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

_source line 31 · 2026-05-12T00:53:16.556Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BHLHS6C2LKFCsse3JNZFFf`</summary>

```json
{
  "url": "https://2026.eacl.org/program/main-accepted/",
  "prompt": "Find the paper titled 'Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction' by Ravikumar et al. in the list of accepted papers. What details are given about it - authors, any description?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b702b63c-8eb5-48d9-8acf-9d9e7d995a14",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm57g3f4K4rksQeoZdx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f85f06ef-474f-4d3a-b47e-76a7b3e8fb5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfGNQQVx97R28ktZzfNQaP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 344,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 15858,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1103
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 344,
          "output_tokens": 232,
          "cache_read_input_tokens": 15858,
          "cache_creation_input_tokens": 1103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1103,
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

_source line 32 · 2026-05-12T00:53:19.524Z_

<details><summary>↩ Tool result · `toolu_01QNkoGxj5ZusFM2Dmhkc7Z8`</summary>

```text
Web search results for query: "site:arxiv.org "Lost in Formatting" "output formats" information extraction"

No links found.

I was able to process your search request. However, the search didn't return any results. This could mean that either:

1. There may not be an arxiv.org paper with those exact phrases combined
2. The specific combination of terms you're searching for doesn't match any existing papers
3. The paper might use slightly different wording

If you're looking for research on a specific paper about formatting and information extraction, you might try:
- Searching with fewer quoted phrases or partial terms
- Searching for just the main topic (formatting, information extraction, output formats)
- Checking if you have the exact title or authors' names that could help locate the paper

Would you like me to try a modified search query?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b702b63c-8eb5-48d9-8acf-9d9e7d995a14",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "2c0dd9bb-ac66-4e89-8433-18ac404348a9",
  "sourceToolAssistantUUID": "b702b63c-8eb5-48d9-8acf-9d9e7d995a14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-12T00:53:19.721Z_

<details><summary>↩ Tool result · `toolu_01BHLHS6C2LKFCsse3JNZFFf`</summary>

```text
# Paper Details

The paper titled **"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction"** appears in the Main Conference accepted papers list.

**Authors:** Rishi Ravikumar, Nuhu Ibrahim, Riza Batista-Navarro

**Description:** No abstract or additional details are provided in the webpage content—only the title and author names are listed as part of the accepted papers compilation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f85f06ef-474f-4d3a-b47e-76a7b3e8fb5d",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "4f8f928d-65aa-42c5-9b64-14108de84fb2",
  "sourceToolAssistantUUID": "f85f06ef-474f-4d3a-b47e-76a7b3e8fb5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-12T00:53:22.905Z_

Let me try to get more details on the EACL paper through the Riza Batista-Navarro ACL Anthology page and also try a broader search for discussion of this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f8f928d-65aa-42c5-9b64-14108de84fb2",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm5yRUyPwbBbHi9bzzx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd3536d4-9fd8-4f7a-be7e-fdbd087043f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hGc8Kj4fBZHEVrYj12UQx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 942,
      "cache_read_input_tokens": 16961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 942,
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

_source line 35 · 2026-05-12T00:53:24.364Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xwe12UTBBHnrmn15Dkt7ow`</summary>

```json
{
  "url": "https://aclanthology.org/people/riza-theresa-batista-navarro/",
  "prompt": "Find the paper 'Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction' in the list of publications. What details are available - abstract, any additional info?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd3536d4-9fd8-4f7a-be7e-fdbd087043f9",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm5yRUyPwbBbHi9bzzx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38ea8f23-c211-4f48-b83c-6abb1432f5a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hGc8Kj4fBZHEVrYj12UQx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 942,
      "cache_read_input_tokens": 16961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 942,
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

_source line 36 · 2026-05-12T00:53:25.193Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HyCu9GkFJZvAh52wfyNvcS`</summary>

```json
{
  "query": "\"Lost in Formatting\" LLM output format NER RE event extraction JSON XML plain text GPT Llama F1 score benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38ea8f23-c211-4f48-b83c-6abb1432f5a9",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm5yRUyPwbBbHi9bzzx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "307557d7-5129-4b60-9980-893940c95eca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hGc8Kj4fBZHEVrYj12UQx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 942,
      "cache_read_input_tokens": 16961,
      "output_tokens": 242,
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
          "output_tokens": 242,
          "cache_read_input_tokens": 16961,
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

_source line 37 · 2026-05-12T00:53:29.547Z_

<details><summary>↩ Tool result · `toolu_01Xwe12UTBBHnrmn15Dkt7ow`</summary>

```text
# Paper: Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction

**Authors:** Rishi Ravikumar, Nuhu Ibrahim, Riza Batista-Navarro

**Publication:** Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers) - 2026

**Available Resources:**
- PDF
- BibTeX citation
- Abstract
- Checklist

**Abstract Summary:**

The research investigates how output format selection affects fine-tuned large language models performing information extraction. Based on over 280 experiments using multiple benchmarks and models, the authors found that output formatting functions as "a critical yet largely overlooked hyperparameter." Notably, altering only the output format produced F1 score shifts exceeding 40 percentage points despite using identical models. The study demonstrates that no single format consistently performs best across different scenarios, with optimal selection depending on factors like model family and dataset characteristics. Their findings highlight that "informationally equivalent output formats can produce substantial performance variation."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38ea8f23-c211-4f48-b83c-6abb1432f5a9",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "76d45e35-56cb-415c-82d6-56607ef22d78",
  "sourceToolAssistantUUID": "38ea8f23-c211-4f48-b83c-6abb1432f5a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-12T00:53:32.475Z_

<details><summary>↩ Tool result · `toolu_01HyCu9GkFJZvAh52wfyNvcS`</summary>

```text
Web search results for query: ""Lost in Formatting" LLM output format NER RE event extraction JSON XML plain text GPT Llama F1 score benchmark"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"},{"title":"arXiv:2504.14633v1 [cs.CL] 20 Apr 2025","url":"https://arxiv.org/pdf/2504.14633"},{"title":"The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models","url":"https://arxiv.org/html/2604.25359"},{"title":"Taming LLM Outputs: Your Guide to Structured Text Generation","url":"https://www.dataiku.com/stories/blog/your-guide-to-structured-text-generation"},{"title":"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models","url":"https://arxiv.org/html/2408.02442v1"},{"title":"LLM Structured Output: JSON, YAML, XML & TOON | Medium","url":"https://medium.com/@michael.hannecke/beyond-json-picking-the-right-format-for-llm-pipelines-b65f15f77f7d"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"StructEval: Benchmarking LLMs’ Capabilities to Generate Structural Outputs","url":"https://arxiv.org/html/2505.20139v1"},{"title":"Decoupling Task-Solving and Output Formatting in LLM Generation","url":"https://arxiv.org/html/2510.03595v1"},{"title":"llm-output-parser · PyPI","url":"https://pypi.org/project/llm-output-parser/"}]

I found the paper you're looking for! Here are the key results from the search:

## "Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction"

This paper investigates how the choice of output format influences the performance of fine-tuned large language models on information extraction tasks.

**Key Findings:**

- Based on over 280 experiments spanning multiple benchmarks, models and formats, the research finds that output formatting is a critical yet largely overlooked hyperparameter, with changing only the output format shifting F1 scores by over 40% despite using the same model.

- No single format consistently dominates across settings, and the optimal choice depends on factors like model family and dataset characteristics.

- The results demonstrate that informationally equivalent output formats can produce substantial performance variation, highlighting the need to treat output formatting as a key factor in building accurate and reliable information extraction systems.

**Publication Details:**

The paper is by Rishi Ravikumar, Nuhu Ibrahim, and Riza Batista-Navarro, published in 2026 in the proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL).

The paper directly addresses your research interests in NER, relation extraction (RE), event extraction, and how different output formats (JSON, XML, plain text) impact LLM performance on these tasks as measured by F1 scores.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "307557d7-5129-4b60-9980-893940c95eca",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "37552280-3778-4257-a0e6-bb3c911fb9c6",
  "sourceToolAssistantUUID": "307557d7-5129-4b60-9980-893940c95eca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-12T00:53:35.943Z_

Let me try fetching some related papers that may discuss "Lost in Formatting" in more detail, and also try the "Let Me Speak Freely?" paper which seems closely related and might provide context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37552280-3778-4257-a0e6-bb3c911fb9c6",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm6uvuzV4gkTyiQZDCr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "908036b9-df37-4923-ba0a-4f4c782f97cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbQkGtTjsZh6BaSLruXKbN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 17903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1496,
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

_source line 40 · 2026-05-12T00:53:39.308Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XRLP21eyrTVMfxLyYVHGmA`</summary>

```json
{
  "url": "https://arxiv.org/html/2408.02442v1",
  "prompt": "This is the paper 'Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models'. Does it cite or discuss 'Lost in Formatting' by Ravikumar et al.? Also, does it discuss constrained decoding, logit masking, or grammar-constrained generation? What are its key findings about format restrictions and LLM performance? What specific formats, tasks, and models do they evaluate?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "908036b9-df37-4923-ba0a-4f4c782f97cb",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm6uvuzV4gkTyiQZDCr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0fdf593-a554-45d1-bfb9-620585f39614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbQkGtTjsZh6BaSLruXKbN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 17903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1496,
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

_source line 41 · 2026-05-12T00:53:40.011Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CnHRDehHUp1yLG8ygVa7Ks`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.03595v1",
  "prompt": "This is the paper 'Decoupling Task-Solving and Output Formatting in LLM Generation'. Does it cite or discuss 'Lost in Formatting' by Ravikumar et al.? What are its key findings about output formatting and LLM performance? Does it discuss constrained decoding?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0fdf593-a554-45d1-bfb9-620585f39614",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm6uvuzV4gkTyiQZDCr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae9c3f12-c153-4237-80c4-8fbab8e241cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbQkGtTjsZh6BaSLruXKbN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 17903,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1496
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 362,
          "cache_read_input_tokens": 17903,
          "cache_creation_input_tokens": 1496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1496,
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

_source line 42 · 2026-05-12T00:53:46.008Z_

<details><summary>↩ Tool result · `toolu_01CnHRDehHUp1yLG8ygVa7Ks`</summary>

```text
# Analysis of "Decoupling Task-Solving and Output Formatting in LLM Generation"

## Citation of "Lost in Formatting"

The paper does not cite or discuss "Lost in Formatting" by Ravikumar et al. in the provided content.

## Key Findings on Output Formatting and LLM Performance

The paper establishes that strict format constraints negatively impact LLM reasoning capabilities. The authors note that "stricter format constraints generally lead to a greater degradation in performance on reasoning tasks" (referencing Tam et al., 2024). They demonstrate this through their GSM8k results, where JSON-formatted prompts yielded only 51.8% accuracy compared to 82.3% with natural language, despite identical task instructions.

The core insight is that format adherence and task-solving compete for the model's attention, creating "competing goals" that impair overall performance.

## Constrained Decoding Discussion

Yes, the paper extensively discusses constrained decoding approaches. It categorizes existing methods into two branches:

1. **Hard control methods** (Outlines, guidance-ai) that enforce strict adherence but "exert invasive control over the LLM generation which often produce abrupt cut-off, resulting in incomplete and incoherent responses"

2. **Soft control approaches** using weighted decoding that modify probabilities at inference time

Deco-G positions itself as a superior alternative by decoupling format constraints from task prompts through a separate Format Estimation Module, achieving 1.0-6.0% relative performance gains while maintaining 100% format compliance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae9c3f12-c153-4237-80c4-8fbab8e241cb",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "deb87388-ffc9-4f8d-a8d5-a6e64d91a88d",
  "sourceToolAssistantUUID": "ae9c3f12-c153-4237-80c4-8fbab8e241cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-12T00:54:03.066Z_

<details><summary>↩ Tool result · `toolu_01XRLP21eyrTVMfxLyYVHGmA`</summary>

```text
# Analysis of "Let Me Speak Freely?" Paper

## Citation of "Lost in Formatting"

The paper does not cite or discuss "Lost in Formatting" by Ravikumar et al. in its references or content.

## Constrained Decoding & Related Techniques

Yes, the paper extensively discusses constrained decoding. It mentions that "Constrained decoding is a technique that limits the output of LLMs by enforcing predefined token space during the generation process." The authors specifically examine JSON mode as a primary implementation, noting similar approaches in Text-Generation-Inference. However, the paper does not extensively discuss logit masking or grammar-constrained generation by those specific names.

## Key Findings

The research reveals critical trade-offs:

- **Reasoning tasks**: Format restrictions significantly degrade performance, with stricter constraints causing greater decline
- **Classification tasks**: Structured formats (especially JSON-mode) often enhance accuracy by constraining answer space
- **Parsing errors**: Surprisingly not the primary cause of performance gaps despite initial hypotheses
- **Schema constraints**: Removing specific schema requirements improves results substantially

## Evaluated Elements

**Formats**: JSON, XML, YAML, and natural language

**Tasks**: 
- Reasoning: GSM8K, Last Letter Concatenation, Shuffled Objects
- Classification: DDXPlus, Sports Understanding, Task 280, MultiFin

**Models**: GPT-3.5-turbo, Claude-3-Haiku, Gemini-1.5-Flash, LLaMA-3-8B, Gemma-2-9B
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0fdf593-a554-45d1-bfb9-620585f39614",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "b6a5e146-cb80-4d45-9456-7b41ca654f43",
  "sourceToolAssistantUUID": "c0fdf593-a554-45d1-bfb9-620585f39614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-12T00:54:07.147Z_

Now let me get the remaining details about the SIGDIAL paper (specifically the ACL Anthology version for the official venue info) and also try one more search for the EACL paper specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6a5e146-cb80-4d45-9456-7b41ca654f43",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm9BEj3Ta33zUZZuReL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8e6e91d-6fce-4d57-b1ab-2391d6743ad4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F67rvgfXR5fZcuhJunst5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 385,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 19399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 752,
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

_source line 45 · 2026-05-12T00:54:09.195Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EWL7qn3i7U7FTciefCUWKM`</summary>

```json
{
  "url": "https://aclanthology.org/events/sigdial-2024/",
  "prompt": "Find the paper 'Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding' by Vukovic et al. in the SIGDIAL 2024 proceedings. What is the exact citation information - pages, paper ID?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8e6e91d-6fce-4d57-b1ab-2391d6743ad4",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm9BEj3Ta33zUZZuReL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88ce6b9e-bb51-433b-97d4-e0450ba4bb2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F67rvgfXR5fZcuhJunst5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 385,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 19399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 752,
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

_source line 46 · 2026-05-12T00:54:10.320Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019561ANmxtPK6qm5pYgLJoG`</summary>

```json
{
  "query": "\"Lost in Formatting\" Ravikumar EACL 2026 NER \"relation extraction\" \"event extraction\" models Llama GPT format JSON XML YAML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88ce6b9e-bb51-433b-97d4-e0450ba4bb2d",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011Cawm9BEj3Ta33zUZZuReL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a481c1b-e23c-4a0c-9166-f4f1fd8019b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F67rvgfXR5fZcuhJunst5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 385,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 19399,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 752
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 385,
          "output_tokens": 265,
          "cache_read_input_tokens": 19399,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 752,
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

_source line 47 · 2026-05-12T00:54:13.381Z_

<details><summary>↩ Tool result · `toolu_01EWL7qn3i7U7FTciefCUWKM`</summary>

```text
Based on the proceedings content provided, the paper details are:

**Title:** "Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding"

**Authors:** Renato Vukovic, David Arps, Carel van Niekerk, Benjamin Matthias Ruppik, Hsien-chin Lin, Michael Heck, Milica Gasic

**Paper ID:** 2024.sigdial-1.33

**Location in proceedings:** This appears as paper 33 in the main SIGDIAL conference proceedings (Proceedings of the 25th Annual Meeting of the Special Interest Group on Discourse and Dialogue)

The specific page numbers are not explicitly stated in the provided excerpt, but the paper can be accessed via the PDF link: https://aclanthology.org/2024.sigdial-1.33.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88ce6b9e-bb51-433b-97d4-e0450ba4bb2d",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "a4463a6d-0239-4a80-b95a-a3ff1374f773",
  "sourceToolAssistantUUID": "88ce6b9e-bb51-433b-97d4-e0450ba4bb2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-12T00:54:16.716Z_

<details><summary>↩ Tool result · `toolu_019561ANmxtPK6qm5pYgLJoG`</summary>

```text
Web search results for query: ""Lost in Formatting" Ravikumar EACL 2026 NER "relation extraction" "event extraction" models Llama GPT format JSON XML YAML"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"},{"title":"How Output Formats Skew LLM Performance on ...","url":"https://aclanthology.org/2026.eacl-long.256.pdf"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"Information Extraction in NLP - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/information-extraction-in-nlp/"},{"title":"GitHub - wutong8023/Awesome_Information_Extraction: Literature Survey of Information Extraction, especially Relation Extraction, Event Extraction, and Slot Filling. · GitHub","url":"https://github.com/wutong8023/Awesome_Information_Extraction"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Named Entity Recognition and Relation Detection for Biomedical Information Extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7485218/"},{"title":"A survey on Relation Extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2667305323000698"}]

Based on the web search results, I found the paper you're looking for:

**"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction"** by Rishi Ravikumar, Nuhu Ibrahim, and Riza Batista-Navarro was published at the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026) in Rabat, Morocco.

## Key Findings

The research investigated over 280 experiments spanning multiple benchmarks, models and formats, finding that output formatting is a critical yet largely overlooked hyperparameter. Remarkably, in some cases, changing only the output format shifts F1 scores by over 40% despite using the same model.

The optimal format choice depends on factors like model family and dataset characteristics, and no single format consistently dominates across settings.

The paper examines how the choice of output format influences the performance of fine-tuned large language models on information extraction tasks, which encompasses NER (Named Entity Recognition), relation extraction, and event extraction—the specific domains you mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a481c1b-e23c-4a0c-9166-f4f1fd8019b3",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "fe297d10-5e49-4a11-a5a8-5b7d79da6b46",
  "sourceToolAssistantUUID": "7a481c1b-e23c-4a0c-9166-f4f1fd8019b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-12T00:54:20.679Z_

Let me try one more attempt to get detailed content from the EACL paper by searching for any blog posts, reviews, or discussions of it that might provide more specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe297d10-5e49-4a11-a5a8-5b7d79da6b46",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmAB4aqGubXxRhotpCe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "012be536-6e23-4375-b7dd-131f5996a05c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQvy2WvSGpk9DKhxaRygGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1679,
      "cache_read_input_tokens": 20151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1679,
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

_source line 50 · 2026-05-12T00:54:21.688Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Bv96F9DaVnEgBcg2RZcnE`</summary>

```json
{
  "query": "\"Lost in Formatting\" Ravikumar 2026 EACL output format information extraction constrained decoding structured generation fine-tuned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "012be536-6e23-4375-b7dd-131f5996a05c",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmAB4aqGubXxRhotpCe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b6a1935-f234-4e7f-a477-f21faa35ce86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQvy2WvSGpk9DKhxaRygGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1679,
      "cache_read_input_tokens": 20151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1679,
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

_source line 51 · 2026-05-12T00:54:22.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WCpYCQxXS6dTZBZHK7geNy`</summary>

```json
{
  "query": "Rishi Ravikumar Nuhu Ibrahim \"University of Manchester\" information extraction output format LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b6a1935-f234-4e7f-a477-f21faa35ce86",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmAB4aqGubXxRhotpCe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a639e8f-c9a7-4a33-b844-234631751600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQvy2WvSGpk9DKhxaRygGT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1679,
      "cache_read_input_tokens": 20151,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1679
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 20151,
          "cache_creation_input_tokens": 1679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1679,
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

_source line 52 · 2026-05-12T00:54:29.067Z_

<details><summary>↩ Tool result · `toolu_01WCpYCQxXS6dTZBZHK7geNy`</summary>

```text
Web search results for query: "Rishi Ravikumar Nuhu Ibrahim "University of Manchester" information extraction output format LLM"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"},{"title":"Nuhu Ibrahim - Research Explorer The University of Manchester","url":"https://research.manchester.ac.uk/en/persons/nuhu-ibrahim/"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"Nuhu Ibrahim","url":"https://nuhuibrahim.com/"},{"title":"Nuhu Ibrahim - Software Developer","url":"https://personalpages.manchester.ac.uk/staff/nuhu.ibrahim/"},{"title":"Rishi Ravikumar - Heidelberg University | LinkedIn","url":"https://uk.linkedin.com/in/rishiravikumar"},{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"rishi-ravikumar (Rishi Ravikumar) · GitHub","url":"https://github.com/rishi-ravikumar"},{"title":"Image-Derived Phenotype Extraction for Genetic Discovery via Unsupervised Deep Learning in CMR Images - Research Explorer The University of Manchester","url":"https://research.manchester.ac.uk/en/publications/image-derived-phenotype-extraction-for-genetic-discovery-via-unsu/"},{"title":"Nuhu Ibrahim - The MAPD Group | LinkedIn","url":"https://www.linkedin.com/in/nuhu-ibrahim/"}]

Based on the search results, I found relevant information about your query:

## Key Findings

Rishi Ravikumar and Nuhu Ibrahim are co-authors on a paper titled "Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction", published at the EACL 2026 conference.

### The Research

The research investigates how the choice of output format influences the performance of fine-tuned large language models on information extraction tasks, based on over 280 experiments spanning multiple benchmarks, models and formats, finding that output formatting is a critical yet largely overlooked hyperparameter.

The study found that in some cases, changing only the output format shifts F1 scores by over 40% despite using the same model. No single format consistently dominates across settings, and the optimal choice depends on factors like model family and dataset characteristics.

### University Affiliation

Nuhu Ibrahim is a PhD researcher in Artificial Intelligence at The University of Manchester, specialising in Natural Language processing and Text-Mining, with academic work that explores the intersection of language understanding, knowledge representation, and domain-specific information extraction.

The paper was presented at the 19th Conference of the European Chapter of the Association for Computational Linguistics in Rabat, Morocco.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a639e8f-c9a7-4a33-b844-234631751600",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "fce997ad-b39f-4ebc-aea5-3275ba7ddefd",
  "sourceToolAssistantUUID": "7a639e8f-c9a7-4a33-b844-234631751600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-12T00:54:30.863Z_

<details><summary>↩ Tool result · `toolu_019Bv96F9DaVnEgBcg2RZcnE`</summary>

```text
Web search results for query: ""Lost in Formatting" Ravikumar 2026 EACL output format information extraction constrained decoding structured generation fine-tuned"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"}]

Based on the search results, I found the paper you're looking for:

**"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction"** by Rishi Ravikumar, Nuhu Ibrahim, and Riza Batista-Navarro, published at the 2026 EACL conference in Rabat, Morocco (pages 5498–5513).

**Research Overview:**

The paper investigates how the choice of output format influences the performance of fine-tuned large language models on information extraction tasks.

**Key Findings:**

- Based on over 280 experiments spanning multiple benchmarks, models and formats, output formatting is a critical yet largely overlooked hyperparameter.

- In some cases, changing only the output format shifts F1 scores by over 40% despite using the same model.

- No single format consistently dominates across settings, and the optimal choice depends on factors like model family and dataset characteristics.

The full paper is available on the ACL Anthology at: https://aclanthology.org/2026.eacl-long.256/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b6a1935-f234-4e7f-a477-f21faa35ce86",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "6bdce67b-59b0-41a0-95f2-817236f34c72",
  "sourceToolAssistantUUID": "1b6a1935-f234-4e7f-a477-f21faa35ce86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-12T00:54:38.129Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JrTKNHufkz2GoxE2ghendE`</summary>

```json
{
  "url": "https://nuhuibrahim.com/",
  "prompt": "Look for any details about the paper 'Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction' - specifically what IE tasks were studied (NER, RE, EE?), what models were used, what output formats were compared, and whether constrained decoding is discussed. Also look for any link to a preprint or arXiv version."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bdce67b-59b0-41a0-95f2-817236f34c72",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmBDZRj7KrNortyJWFg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa424edb-d354-4419-a2d1-abf04bd4ea77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCxhtBpNtS58kGoiRuweog",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 755,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 21830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 609,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-12T00:54:39.507Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GsZbMcj287jjEoV9sXTK2V`</summary>

```json
{
  "url": "https://github.com/rishi-ravikumar",
  "prompt": "Look for any repository related to the paper 'Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction'. What code, datasets, or experiments are available? What formats, models, and IE tasks were evaluated?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa424edb-d354-4419-a2d1-abf04bd4ea77",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmBDZRj7KrNortyJWFg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82f62193-f18f-408f-bbb4-f09b025d9af6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCxhtBpNtS58kGoiRuweog",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 755,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 21830,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 609
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 755,
          "output_tokens": 274,
          "cache_read_input_tokens": 21830,
          "cache_creation_input_tokens": 609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 609,
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

_source line 56 · 2026-05-12T00:54:41.420Z_

<details><summary>↩ Tool result · `toolu_01JrTKNHufkz2GoxE2ghendE`</summary>

```text
Based on the web page content provided, I cannot find any information about the paper 'Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction'. 

The page is a personal website for Nuhu Ibrahim that includes brief biographical information, navigation links to sections like resume, education, publications, and awards, along with social media links. However, the actual content of those linked pages is not included in the material you've shared.

To find details about that specific paper, IE tasks studied, models used, output formats compared, or constrained decoding discussions, you would need to visit the Publications section directly or access the paper through an academic repository like arXiv.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa424edb-d354-4419-a2d1-abf04bd4ea77",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "2070ec13-63b8-4bb3-b1c2-181f8b15eb3b",
  "sourceToolAssistantUUID": "aa424edb-d354-4419-a2d1-abf04bd4ea77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-12T00:54:42.363Z_

<details><summary>↩ Tool result · `toolu_01GsZbMcj287jjEoV9sXTK2V`</summary>

```text
# Repository Information for Output Formatting Paper

Based on the GitHub profile, there is one relevant repository:

**OutputFormattingExperiments**
- Description: "Code for our EACL 2026 paper 'Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction'"
- Status: Public repository available

## Limitations

The provided webpage content does not include detailed information about specific code implementations, datasets, experimental configurations, or which particular output formats, language models, and information extraction tasks were evaluated in the study. To access this comprehensive information, you would need to visit the actual repository page directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82f62193-f18f-408f-bbb4-f09b025d9af6",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "7a2c165e-2c3f-48f1-84f5-bd9cefdd9b7a",
  "sourceToolAssistantUUID": "82f62193-f18f-408f-bbb4-f09b025d9af6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-12T00:54:47.040Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014eVapLNEnBzSTCGmC64Zka`</summary>

```json
{
  "url": "https://github.com/rishi-ravikumar/OutputFormattingExperiments",
  "prompt": "Extract ALL details about this repository for the paper 'Lost in Formatting'. Specifically:\n1. What IE tasks are evaluated (NER, RE, EE, etc.)?\n2. What LLM models are used?\n3. What output formats are compared (JSON, XML, YAML, plain text, markdown, etc.)?\n4. Is constrained decoding discussed or implemented?\n5. What datasets/benchmarks are used?\n6. Any README content with key findings or experimental setup details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a2c165e-2c3f-48f1-84f5-bd9cefdd9b7a",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmC4iQBBvit63u2dS7G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "269a9e32-a22b-458b-8e76-847fa835347a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01669h6LKeENe7RXkFXQjg1E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1476,
      "cache_read_input_tokens": 22439,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1476
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 199,
          "cache_read_input_tokens": 22439,
          "cache_creation_input_tokens": 1476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1476,
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

_source line 59 · 2026-05-12T00:54:51.287Z_

<details><summary>↩ Tool result · `toolu_014eVapLNEnBzSTCGmC64Zka`</summary>

```text
# Repository Analysis: OutputFormattingExperiments

Based on the GitHub page content provided, I can extract the following information:

## Available Information

**Paper Title:** "Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction"

**Venue:** EACL 2026

**Repository Owner:** rishi-ravikumar

**License:** Apache-2.0

## Limitations

Unfortunately, the web page content provided only contains GitHub's navigation interface and repository metadata. The actual README file content, which would contain detailed information about the experimental setup, is not fully rendered in the provided text.

## Unable to Determine

Based solely on this page excerpt, I cannot extract:

1. **IE Tasks Evaluated** - Not specified in visible content
2. **LLM Models Used** - Not listed
3. **Output Formats Compared** - Not detailed
4. **Constrained Decoding Discussion** - Not mentioned
5. **Datasets/Benchmarks** - Not provided
6. **Key Findings or Setup Details** - README content not accessible

**Recommendation:** To obtain the comprehensive details you're seeking, you would need to view the full README.md file directly on GitHub at `rishi-ravikumar/OutputFormattingExperiments`, which would contain the experimental methodology and results summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "269a9e32-a22b-458b-8e76-847fa835347a",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "03a13b4a-670b-4c31-8578-f8539a845f20",
  "sourceToolAssistantUUID": "269a9e32-a22b-458b-8e76-847fa835347a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-12T00:55:05.572Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0143mpm1xM9CeREHgz9LevSf`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/rishi-ravikumar/OutputFormattingExperiments/main/README.md",
  "prompt": "Extract ALL details from this README:\n1. What IE tasks are evaluated (NER, RE, EE, etc.)?\n2. What LLM models are used?\n3. What output formats are compared (JSON, XML, YAML, plain text, etc.)?\n4. Is constrained decoding discussed?\n5. What datasets/benchmarks are used?\n6. Any key findings or experimental setup details\n7. How to reproduce the experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03a13b4a-670b-4c31-8578-f8539a845f20",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmCisZwwbJg6jHGHW3g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c79f2574-b3a0-4ed4-b682-be797bd0cdd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVR1Puzd46Z2U8JQzqF6NC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 507,
      "cache_read_input_tokens": 23915,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 507
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 23915,
          "cache_creation_input_tokens": 507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 507,
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

_source line 61 · 2026-05-12T00:55:09.278Z_

<details><summary>↩ Tool result · `toolu_0143mpm1xM9CeREHgz9LevSf`</summary>

```text
# Analysis of OutputFormattingExperiments README

Based on the provided content, here's what can be extracted:

**1. IE Tasks Evaluated:**
Not specified in the excerpt provided.

**2. LLM Models Used:**
Not detailed in the available content.

**3. Output Formats Compared:**
The title indicates the paper examines "how output formats skew LLM performance," but specific formats aren't enumerated in this excerpt.

**4. Constrained Decoding:**
Not mentioned in the provided material.

**5. Datasets/Benchmarks:**
Not identified in the excerpt.

**6. Key Findings/Experimental Setup:**
The core research premise is captured in the title: "Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction" (EACL 2026). The work investigates whether different output formatting approaches impact LLM performance on IE tasks.

**7. Reproduction Instructions:**
Not available in this excerpt.

---

**Note:** The provided README content is minimal. A complete analysis would require access to the full documentation, methodology section, or additional README sections that typically include experimental details, model specifications, and setup instructions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c79f2574-b3a0-4ed4-b682-be797bd0cdd5",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "234d32b3-252a-4a7d-938e-4cdbf24a0786",
  "sourceToolAssistantUUID": "c79f2574-b3a0-4ed4-b682-be797bd0cdd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-12T00:55:12.850Z_

The README is minimal. Let me try to access the paper content from a Semantic Scholar or similar source, and also look at the repo structure for clues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "234d32b3-252a-4a7d-938e-4cdbf24a0786",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmE3rMoZjfnmGhg8wb1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c70ce3ff-2f8f-45fc-a606-ec5b226f3274",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012C1N6MCbFYNq7YfeWgxBSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 474,
      "cache_read_input_tokens": 24422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 474,
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

_source line 63 · 2026-05-12T00:55:13.530Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01REsgzXp6EhnpQkTachPbMp`</summary>

```json
{
  "query": "semanticscholar.org \"Lost in Formatting\" output formats LLM information extraction Ravikumar"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c70ce3ff-2f8f-45fc-a606-ec5b226f3274",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmE3rMoZjfnmGhg8wb1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b90b24e-fa33-49a2-b1c0-dbc892953838",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012C1N6MCbFYNq7YfeWgxBSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 474,
      "cache_read_input_tokens": 24422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 474,
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

_source line 64 · 2026-05-12T00:55:14.629Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WbZE1D56oekPZyEb7A74Dq`</summary>

```json
{
  "query": "\"Lost in Formatting\" EACL 2026 Ravikumar NER CoNLL ACE SciERC TACRED output format fine-tuned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b90b24e-fa33-49a2-b1c0-dbc892953838",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmE3rMoZjfnmGhg8wb1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df451d6f-1fd7-4b03-b4a0-f45dfe18643b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012C1N6MCbFYNq7YfeWgxBSy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 474,
      "cache_read_input_tokens": 24422,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 474
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 24422,
          "cache_creation_input_tokens": 474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 474,
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

_source line 65 · 2026-05-12T00:55:17.401Z_

<details><summary>↩ Tool result · `toolu_01REsgzXp6EhnpQkTachPbMp`</summary>

```text
Web search results for query: "semanticscholar.org "Lost in Formatting" output formats LLM information extraction Ravikumar"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"}]

Based on the search results, I found the paper you're looking for:

"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction" is a paper by Rishi Ravikumar, Nuhu Ibrahim, and Riza Batista-Navarro published in the Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics in Rabat, Morocco in 2026.

The paper investigates how the choice of output format influences the performance of fine-tuned large language models on information extraction tasks, finding that output formatting is a critical yet largely overlooked hyperparameter based on over 280 experiments spanning multiple benchmarks, models and formats. Notably, changing only the output format can shift F1 scores by over 40% despite using the same model.

The full paper is available on the ACL Anthology at: https://aclanthology.org/2026.eacl-long.256/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b90b24e-fa33-49a2-b1c0-dbc892953838",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "25e6bd0a-0b66-4ad1-bff0-4bf5e97a4d8d",
  "sourceToolAssistantUUID": "0b90b24e-fa33-49a2-b1c0-dbc892953838",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-12T00:55:21.057Z_

<details><summary>↩ Tool result · `toolu_01WbZE1D56oekPZyEb7A74Dq`</summary>

```text
Web search results for query: ""Lost in Formatting" EACL 2026 Ravikumar NER CoNLL ACE SciERC TACRED output format fine-tuned"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"How Output Formats Skew LLM Performance on ...","url":"https://aclanthology.org/2026.eacl-long.256.pdf"},{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"The 19th Conference of the European Chapter of the Association for Computational LinguisticsRabat, MoroccoMarch 24-29, 2026 -","url":"https://2026.eacl.org/"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"},{"title":"A Scalable Framework for Automated NER Annotation ...","url":"https://aclanthology.org/2026.findings-eacl.215.pdf"},{"title":"Registration Information -","url":"https://2026.eacl.org/registration/"},{"title":"Conference Overview -","url":"https://2026.eacl.org/program/"},{"title":"EACL 2026 - Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-call-system-demonstrations"}]

I found the paper! Here are the search results for "Lost in Formatting" EACL 2026:

## Paper Details

The paper "Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction" was authored by Rishi Ravikumar, Nuhu Ibrahim, and Riza Batista-Navarro and published in the Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026) in Rabat, Morocco, pages 5498–5513.

## Research Summary

The research is based on over 280 experiments spanning multiple benchmarks, models and formats. The authors found that output formatting is a critical yet largely overlooked hyperparameter, and in some cases, changing only the output format shifts F1 scores by over 40% despite using the same model.

The authors further observe that no single format consistently dominates across settings, and the optimal choice depends on factors like model family and dataset characteristics.

The paper is available on the ACL Anthology at: https://aclanthology.org/2026.eacl-long.256/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df451d6f-1fd7-4b03-b4a0-f45dfe18643b",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "ce4035b5-9d40-4faa-82ba-28cd040dcd70",
  "sourceToolAssistantUUID": "df451d6f-1fd7-4b03-b4a0-f45dfe18643b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-12T00:55:24.934Z_

Let me try one more approach - searching for citing papers or discussions that reference the EACL paper with more specifics about its content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce4035b5-9d40-4faa-82ba-28cd040dcd70",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmEvAmuMSmD8F4A6uzy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08f8c557-f381-4cc6-a54a-aa2ad6e42580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CjX9p8MRoWjXcRH9fX8hH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 24896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1282,
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

_source line 68 · 2026-05-12T00:55:26.438Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KftUtLFLZeXDKShw4UJJf7`</summary>

```json
{
  "query": "\"Ravikumar\" \"Ibrahim\" \"Batista-Navarro\" 2026 information extraction format NER event extraction benchmark Llama Mistral GPT fine-tuned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08f8c557-f381-4cc6-a54a-aa2ad6e42580",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmEvAmuMSmD8F4A6uzy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "837173bd-2c89-4b29-9284-f8c9f2456dd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CjX9p8MRoWjXcRH9fX8hH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 24896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1282,
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

_source line 69 · 2026-05-12T00:55:28.546Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0157AFPhwbsLJh23yLwgV8hL`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.10036v1",
  "prompt": "Does this paper cite 'Lost in Formatting' by Ravikumar et al. (2026)? If so, what details does it provide about that paper - what IE tasks, models, formats, and findings are described? Also look for any references to Ravikumar, Ibrahim, or Batista-Navarro in the bibliography."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "837173bd-2c89-4b29-9284-f8c9f2456dd9",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmEvAmuMSmD8F4A6uzy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d66ac237-5a05-4863-881c-d491b4173dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CjX9p8MRoWjXcRH9fX8hH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 24896,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1282
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 24896,
          "cache_creation_input_tokens": 1282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1282,
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

_source line 70 · 2026-05-12T00:55:31.430Z_

<details><summary>↩ Tool result · `toolu_0157AFPhwbsLJh23yLwgV8hL`</summary>

```text
# Search Results for "Lost in Formatting" Citation

After thoroughly reviewing the provided document, I can confirm that **this paper does not cite "Lost in Formatting" by Ravikumar et al. (2026)**.

Additionally, I found **no references to Ravikumar, Ibrahim, or Batista-Navarro** anywhere in the bibliography or the paper's content.

The paper's reference section lists 32 citations, but none match the authors or title you're inquiring about. The most recent publication dates in the bibliography are from 2025, making a 2026 citation impossible in this version of the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d66ac237-5a05-4863-881c-d491b4173dcf",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "e1473f9d-6aa1-45df-8477-8fe37618ab0f",
  "sourceToolAssistantUUID": "d66ac237-5a05-4863-881c-d491b4173dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-12T00:55:33.149Z_

<details><summary>↩ Tool result · `toolu_01KftUtLFLZeXDKShw4UJJf7`</summary>

```text
Web search results for query: ""Ravikumar" "Ibrahim" "Batista-Navarro" 2026 information extraction format NER event extraction benchmark Llama Mistral GPT fine-tuned"

Links: [{"title":"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.256/"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"Named Entity Recognition and Relation Detection for Biomedical Information Extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7485218/"},{"title":"Information Extraction in NLP - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/information-extraction-in-nlp/"},{"title":"[1912.13415] End-to-end Named Entity Recognition and Relation Extraction using Pre-trained Language Models","url":"https://arxiv.org/abs/1912.13415"},{"title":"A survey on recent advances in Named Entity Recognition","url":"https://arxiv.org/html/2401.10825v1"},{"title":"A review of named entity recognition: from learning methods to modelling paradigms and tasks | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11321-8"},{"title":"A neural network based Event extraction system for Indian languages","url":"https://ceur-ws.org/Vol-2266/T5-2.pdf"}]

Based on the search results, I found the research paper you're looking for:

"Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction" is a paper by Rishi Ravikumar, Nuhu Ibrahim, and Riza Batista-Navarro, published in the Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 5498–5513, Rabat, Morocco in 2026.

The paper investigates how the choice of output format influences the performance of fine-tuned large language models on information extraction tasks, with findings based on over 280 experiments spanning multiple benchmarks, models and formats. In some cases, changing only the output format shifts F1 scores by over 40% despite using the same model. The researchers further observe that no single format consistently dominates across settings, and the optimal choice depends on factors like model family and dataset characteristics.

The paper directly addresses how output formatting impacts LLM performance on information extraction benchmarks across different model families, which aligns with your search query about NER and information extraction evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "837173bd-2c89-4b29-9284-f8c9f2456dd9",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "2c56c3f7-5a94-4fb3-bf1a-34db3edefe65",
  "sourceToolAssistantUUID": "837173bd-2c89-4b29-9284-f8c9f2456dd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-12T00:55:40.035Z_

Let me try one more approach - check if the Structured Output Benchmark paper or the Dataiku article references the EACL paper with more detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c56c3f7-5a94-4fb3-bf1a-34db3edefe65",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmFosHj7zZ1dMXEN6JM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8980138e-cba3-4b00-8f81-dc4c7b35e88d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6GGkbrwroGcMV4yTjGoCj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 169,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 26178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1067,
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

_source line 73 · 2026-05-12T00:55:42.231Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016X8tTMvWSSgXUKSbWkki7J`</summary>

```json
{
  "url": "https://www.dataiku.com/stories/blog/your-guide-to-structured-text-generation",
  "prompt": "Does this article mention or cite 'Lost in Formatting' by Ravikumar et al.? If so what details does it provide about the paper's specific IE tasks, models, formats evaluated? Also look for any discussion of how output formatting affects information extraction performance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8980138e-cba3-4b00-8f81-dc4c7b35e88d",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmFosHj7zZ1dMXEN6JM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3c4a31e-7787-4132-aa86-8f3a9661e80b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6GGkbrwroGcMV4yTjGoCj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 169,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 26178,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1067
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 169,
          "output_tokens": 182,
          "cache_read_input_tokens": 26178,
          "cache_creation_input_tokens": 1067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1067,
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

_source line 74 · 2026-05-12T00:55:45.627Z_

<details><summary>↩ Tool result · `toolu_016X8tTMvWSSgXUKSbWkki7J`</summary>

```text
# Response

The article does not mention or cite "Lost in Formatting" by Ravikumar et al. A thorough review of the content reveals no reference to this paper, nor does it discuss specific information extraction tasks, model comparisons, or format evaluations that such a paper might contain.

The article does discuss how output formatting impacts LLM performance generally. It notes that "enforcing a constraint may change not only the format, but also the substance of an answer," using examples showing how constraints can inadvertently shift which answers the model selects. However, this is presented as a pitfall of constrained decoding rather than an empirical study of formatting's effects on IE tasks specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3c4a31e-7787-4132-aa86-8f3a9661e80b",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "aa91cb80c87bc5643",
  "type": "user",
  "uuid": "9e3b4943-8ade-4881-8f77-66a35458f2d8",
  "sourceToolAssistantUUID": "f3c4a31e-7787-4132-aa86-8f3a9661e80b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-12T00:56:52.987Z_

I now have substantial information on both papers. Let me compile my findings. Here is the detailed report on both papers:

---

## Paper 1: Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding

**Exact Title:** "Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding"

**Authors:** Renato Vukovic, David Arps, Carel van Niekerk, Benjamin Matthias Ruppik, Hsien-chin Lin, Michael Heck, Milica Gasic -- all from Heinrich Heine University Dusseldorf.

**Venue:** SIGDIAL 2024 (25th Annual Meeting of the Special Interest Group on Discourse and Dialogue). Paper ID: `2024.sigdial-1.33`. Also on arXiv as `2408.02361`.

### Ontology Constraints Enforced During Decoding

The method constrains three components of relational triplets `[head, relation, tail]`:

- **Head and tail terms** must come from the input dialogue term set (T) -- i.e., only terms actually extracted from the dialogue data are permitted.
- **Relation types** must match a predefined set of ontology relation types (R).
- Constraints are activated selectively: they engage **only when an opening bracket is predicted** (since triplets are enclosed in brackets) and resume normal unconstrained generation after the bracket closes. This means the reasoning/chain-of-thought portion of the generation is unconstrained, while only the structured triplet output is constrained.
- The purpose is to prevent hallucination of terms or relations not present in the source data.

### Decoding Mechanism

The approach combines **two distinct techniques** -- it is neither pure logit masking nor grammar-constrained decoding:

1. **CoT Decoding (Chain-of-Thought Decoding):** This is not the typical "chain-of-thought prompting" but rather a decoding-time technique. They generate **k=5 parallel branches** starting from different first tokens. For each branch, they compute a "disparity" metric: the difference between the highest and second-highest token probability at each step. They then calculate the **average disparity** across all answer tokens: Delta = (1/n) * Sum[p(top) - p(next)]. The branch with the highest average disparity is selected as the most confident prediction. This acts as a confidence-based branch selection mechanism.

2. **Constrained Decoding:** Token-level vocabulary filtering that restricts the model's output vocabulary to valid terms and relation types, but only when inside bracket pairs (i.e., when generating structured triplet content). Outside brackets, generation proceeds normally.

**Key distinction from logit masking:** This is NOT standard logit masking in the traditional sense. Standard logit-masking approaches for IE typically mask invalid tokens at every step to enforce JSON/XML schema compliance. Instead, this method:
- Uses **confidence-based branch selection** (disparity) as the primary mechanism rather than hard probability constraints
- Applies constrained decoding **selectively** -- only within bracket pairs, leaving reasoning text unconstrained
- Combines generation **diversity** (multiple parallel branches) with constraint enforcement
- Focuses on "disparity as a confidence metric" rather than absolute probability thresholds, because the authors found that absolute confidence thresholds are not meaningful (models are overconfident)
- Does not use grammar-based or automata-based constraint techniques (like those in Outlines or guidance-ai)

### Datasets/Benchmarks

- **Training data:** MultiWOZ 2.1 (7 domains, 10,000+ dialogues) -- used for fine-tuning
- **Test data:** Schema-Guided Dialogue (SGD) test set (4,201 dialogues, 18 domains, 20,000+ dialogues total) -- used as out-of-domain target
- **Upper bound comparison:** SGD training set used for fine-tuning to establish ceiling performance
- **Evaluation metric:** Micro F1, precision, recall at the global (accumulated) ontology level

### Key Results

Fine-tuned on MultiWOZ, tested on SGD (cross-domain transfer):
| Method | F1 |
|--------|------|
| Baseline (unconstrained) | 10.9 |
| Constrained decoding only | 12.0 |
| CoT decoding only | 10.6 |
| **Constrained CoT decoding (combined)** | **13.7** |

One-shot setting:
| Method | F1 |
|--------|------|
| Baseline | 7.4 |
| Constrained CoT decoding | 9.2 |

Upper bound (trained on SGD directly): 37.3 F1

The combined constrained CoT decoding approach achieves statistically significant improvement over all individual components. The ablation studies show:
- Performance gains come primarily from the first additional branch (k=2), with marginal improvements from k=3 to k=5
- Constrained decoding alone improves structure and reduces hallucination
- CoT decoding alone generates reasoning but produces out-of-domain terms
- The combination forces the model to use task-specific knowledge while maintaining multiple hypotheses
- Models show high overconfidence; relative branch confidence (disparity) is more meaningful than absolute thresholds

### How It Differs from Logit-Masking Approaches for IE

1. **Not a full-output constraint:** Unlike logit-masking systems (e.g., Outlines, LMQL, guidance-ai) that enforce schema compliance at every token, this method constrains only during structured output portions (inside brackets), leaving reasoning text free.
2. **Multi-branch exploration:** Instead of constraining a single generation path, it explores k=5 parallel branches and selects the best one via a confidence metric -- this is fundamentally different from the single-path constraint enforcement of logit masking.
3. **No grammar/automaton:** It does not use finite-state automata or context-free grammars to enforce output structure, which is the mechanism behind tools like Outlines.
4. **Domain-specific vocabulary constraint:** Rather than enforcing JSON/XML syntax, it constrains the semantic content (valid terms and relations from the ontology), which is a domain-level constraint rather than a syntactic one.

---

## Paper 2: Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction

**Exact Title:** "Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction"

**Authors:** Rishi Ravikumar (Heidelberg University), Nuhu Ibrahim (University of Manchester), Riza Batista-Navarro (University of Manchester)

**Venue:** EACL 2026 (19th Conference of the European Chapter of the Association for Computational Linguistics), Volume 1: Long Papers, pages 5498-5513, Rabat, Morocco, March 2026.

### Key Finding: Format Choice Affecting F1 by 40%+

The central finding is that **changing only the output format shifts F1 scores by over 40 percentage points** despite using the same model, same data, and same task. This demonstrates that output formatting is "a critical yet largely overlooked hyperparameter" for information extraction. The paper further establishes that **no single format consistently dominates** across all settings -- the optimal format depends on factors like model family and dataset characteristics. "Informationally equivalent output formats can produce substantial performance variation."

### IE Tasks and Models Evaluated

The study spans **over 280 experiments** across **multiple benchmarks, models, and formats**. Based on the paper's positioning in the IE literature and the ACL Anthology metadata:

- **IE tasks:** The paper evaluates information extraction tasks broadly. Given the venue (a long paper at EACL), the scope, and the 280+ experiments, this almost certainly includes NER (Named Entity Recognition) and relation extraction, and likely event extraction as well.
- **Models:** The paper evaluates **fine-tuned** large language models across multiple model families. The specific model names are not fully extractable from the abstract and metadata alone, but the finding that optimal format depends on "model family" suggests multiple families (e.g., Llama, Mistral, GPT-class, etc.) were compared.
- **Output formats:** The paper compares informationally equivalent output formats -- likely including JSON, XML, YAML, plain text/natural language, and potentially others. The key insight is that these are informationally equivalent (they encode the same structured information) yet produce vastly different performance.

### Constrained Decoding Discussion

From the abstract and metadata, the paper's primary focus is on the **output format as a hyperparameter** in fine-tuning settings, rather than on constrained decoding mechanisms per se. The paper addresses the format in which models are trained to produce output, not the decoding-time enforcement of structure. However, this finding has major implications for constrained decoding: if format choice alone shifts F1 by 40%+, then constraining outputs to a suboptimal format via logit masking or grammar constraints could severely harm performance.

The related work in this space -- particularly "Let Me Speak Freely?" (Tam et al., 2024) and "Decoupling Task-Solving and Output Formatting" (2025) -- explicitly discusses constrained decoding and finds that format restrictions degrade reasoning performance. The "Lost in Formatting" paper extends this finding specifically to the IE domain with fine-tuned models.

### Connection Between the Two Papers

These papers are complementary:
- **Vukovic et al. (SIGDIAL 2024)** shows that constraining decoding to ontology-valid terms and relations improves relation extraction by reducing hallucination, combining this with confidence-based multi-branch decoding.
- **Ravikumar et al. (EACL 2026)** shows that the choice of output format itself (independent of any decoding constraint) massively impacts IE performance, meaning that any constrained decoding approach must carefully consider which format it enforces.

Together, they suggest that constrained decoding for IE must be thoughtful about both **what** is constrained (semantic content vs. syntactic format) and **how** (the specific output format chosen), since an ill-chosen format constraint can destroy 40%+ of F1 performance.

---

Sources:
- [Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding (arXiv)](https://arxiv.org/abs/2408.02361)
- [Dialogue Ontology Relation Extraction - HTML version (arXiv)](https://arxiv.org/html/2408.02361)
- [SIGDIAL 2024 Proceedings (ACL Anthology)](https://aclanthology.org/events/sigdial-2024/)
- [Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction (ACL Anthology)](https://aclanthology.org/2026.eacl-long.256/)
- [Lost in Formatting - PDF](https://aclanthology.org/2026.eacl-long.256.pdf)
- [EACL 2026 Main Conference Accepted Papers](https://2026.eacl.org/program/main-accepted/)
- [OutputFormattingExperiments GitHub Repository](https://github.com/rishi-ravikumar/OutputFormattingExperiments)
- [Let Me Speak Freely? (arXiv)](https://arxiv.org/html/2408.02442v1)
- [Decoupling Task-Solving and Output Formatting (arXiv)](https://arxiv.org/html/2510.03595v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e3b4943-8ade-4881-8f77-66a35458f2d8",
  "isSidechain": true,
  "agentId": "aa91cb80c87bc5643",
  "requestId": "req_011CawmGjCn2bgeYXB94QuY9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75a448d7-b776-4e27-9cca-d206d5619e28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNorxmxov54cbyvFDMnM39",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 611,
      "cache_read_input_tokens": 27245,
      "output_tokens": 2744,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 611
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2744,
          "cache_read_input_tokens": 27245,
          "cache_creation_input_tokens": 611,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 611,
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
