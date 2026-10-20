# Research conversation: Search the web for "OneKE" paper from WWW 2025 (arXiv 2412.20005). I need: 1. The full title, authors, venue 2. What it 

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a1c2e06d61cd303be.jsonl`
- **Structured JSON:** [`3d815247ad9625c4d8d8.json`](../../sessions/3d/3d815247ad9625c4d8d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-10T19:16:59.686Z_

Search the web for "OneKE" paper from WWW 2025 (arXiv 2412.20005). I need:
1. The full title, authors, venue
2. What it does (schema-guided LLM agent for extraction)
3. How it relates to schema-guided extraction pipelines

Use WebSearch to find this paper and WebFetch to read its abstract/approach if possible. Report back concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "a1c2e06d61cd303be",
  "type": "user",
  "uuid": "a641b609-34fa-4728-aaa0-f9d7eb16d11b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:16:59.690Z_

```json
{
  "parentUuid": "a641b609-34fa-4728-aaa0-f9d7eb16d11b",
  "isSidechain": true,
  "agentId": "a1c2e06d61cd303be",
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
  "uuid": "dcecfde5-c95c-4368-9e93-5e66684b3003",
  "timestamp": "2026-05-10T19:16:59.690Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T19:17:02.157Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015ZYf9AtWTZwgAE9Gb1XBhL`</summary>

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
  "parentUuid": "dcecfde5-c95c-4368-9e93-5e66684b3003",
  "isSidechain": true,
  "agentId": "a1c2e06d61cd303be",
  "requestId": "req_011CauRdVvp7t4wApuqzNFav",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98b29f4b-b22a-4b0f-b122-a76a3fd3579a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUZtqSSmhxMdcwcChxXTKp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8873,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8873,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-10T19:17:02.161Z_

<details><summary>↩ Tool result · `toolu_015ZYf9AtWTZwgAE9Gb1XBhL`</summary>

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
  "parentUuid": "98b29f4b-b22a-4b0f-b122-a76a3fd3579a",
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "a1c2e06d61cd303be",
  "type": "user",
  "uuid": "af0d898a-0c43-4cc4-92ec-58ceda6cfb39",
  "sourceToolAssistantUUID": "98b29f4b-b22a-4b0f-b122-a76a3fd3579a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T19:17:05.078Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H6m25A83g4stqW4EpyUnom`</summary>

```json
{
  "query": "OneKE arXiv 2412.20005 WWW 2025 schema-guided knowledge extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af0d898a-0c43-4cc4-92ec-58ceda6cfb39",
  "isSidechain": true,
  "agentId": "a1c2e06d61cd303be",
  "requestId": "req_011CauRdh9FdiEZLqtTpBTee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94152ba7-9251-4cf9-831b-c4ded40e81d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiptfpwiAyCsmtdzFv4ttx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T19:17:06.657Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AVKErbh3XrbwnNDwrm93Bm`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.20005",
  "prompt": "Extract the full title, all authors, venue/conference, abstract, and key approach details of this paper. I need to understand what OneKE does, how it uses schema-guided LLM agents for extraction, and its relation to schema-guided extraction pipelines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94152ba7-9251-4cf9-831b-c4ded40e81d1",
  "isSidechain": true,
  "agentId": "a1c2e06d61cd303be",
  "requestId": "req_011CauRdh9FdiEZLqtTpBTee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a399eb53-13cd-4115-b98e-84cb7ac33e11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiptfpwiAyCsmtdzFv4ttx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8873,
      "output_tokens": 196,
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
          "output_tokens": 196,
          "cache_read_input_tokens": 8873,
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

_source line 7 · 2026-05-10T19:17:11.997Z_

<details><summary>↩ Tool result · `toolu_01AVKErbh3XrbwnNDwrm93Bm`</summary>

```text
# OneKE: Schema-Guided LLM Agent-based Knowledge Extraction

## Full Title
"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System"

## Authors
Yujie Luo, Xiangyuan Ru, Kangwei Liu, Lin Yuan, Mengshu Sun, Ningyu Zhang, Lei Liang, Zhiqiang Zhang, Jun Zhou, Lanning Wei, Da Zheng, Haofen Wang, and Huajun Chen

## Venue
WWW 2025 Demonstration

## Abstract Summary
The system extracts knowledge from web sources and PDF documents across multiple domains. It utilizes multiple specialized agents and a configuration knowledge base to handle various extraction scenarios while supporting schema-based approaches.

## Key Approach Details

**Architecture**: The system employs multiple agents with distinct roles, each handling specific aspects of the extraction pipeline. A configurable knowledge base enables schema management across different domains.

**Capabilities**:
- Extracts structured knowledge from diverse sources (web pages, PDF books)
- Supports multiple domains including science and news
- Enables error case debugging and correction through schema configuration

**Performance**: The authors demonstrate effectiveness through benchmark evaluations and case studies showing adaptability across multiple domains.

**Availability**: The code is open-sourced on GitHub (zjunlp/OneKE), and a demonstration video is available online.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a399eb53-13cd-4115-b98e-84cb7ac33e11",
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "a1c2e06d61cd303be",
  "type": "user",
  "uuid": "5e7769a0-aea6-4615-9a49-483281f58786",
  "sourceToolAssistantUUID": "a399eb53-13cd-4115-b98e-84cb7ac33e11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T19:17:13.695Z_

<details><summary>↩ Tool result · `toolu_01H6m25A83g4stqW4EpyUnom`</summary>

```text
Web search results for query: "OneKE arXiv 2412.20005 WWW 2025 schema-guided knowledge extraction"

Links: [{"title":"[2412.20005] OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://arxiv.org/abs/2412.20005"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://arxiv.org/pdf/2412.20005"},{"title":"Paper page - OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://huggingface.co/papers/2412.20005"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241220005L/abstract"},{"title":"GitHub - zjunlp/OneKE: [WWW 2025] A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System.","url":"https://github.com/zjunlp/oneke"},{"title":"dblp: OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System.","url":"https://dblp.org/rec/journals/corr/abs-2412-20005.html"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System | alphaXiv","url":"https://www.alphaxiv.org/abs/2412.20005"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://www.researchgate.net/publication/387539869_OneKE_A_Dockerized_Schema-Guided_LLM_Agent-based_Knowledge_Extraction_System"},{"title":"GitHub - OpenSPG/OneKE: OneKE is a knowledge extraction framework based on a large model, with preliminary generalized knowledge extraction capabilities in both Chinese and English and in multiple fields and tasks. · GitHub","url":"https://github.com/OpenSPG/OneKE"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"}]

I found detailed information about OneKE. Here are the key findings from the search results:

## OneKE Overview

OneKE is a dockerized schema-guided knowledge extraction system which can extract knowledge from the Web and raw PDF Books, and support various domains (science, news, etc.)

## System Architecture

OneKE is designed with multiple agents and a configure knowledge base, where different agents perform their respective roles enabling support for various extraction scenarios, and the configure knowledge base facilitates schema configuration, error case debugging and correction, further improving the performance.

More specifically, three agents are designed: Schema Agent for schema analysis with various data types, Extraction Agent for extracting knowledge with various LLMs, and Reflection Agent to debug and handle erroneous cases.

## Publication and Availability

The paper is published as part of the WWW Companion '25 (April 28-May 2, 2025) proceedings, and the code has been open-sourced at https://github.com/zjunlp/OneKE and a video demo is available at http://oneke.openkg.cn/demo.mp4.

## Performance and Applications

Empirical evaluations on benchmark datasets demonstrate OneKE's efficacy, while case studies further elucidate its adaptability to diverse tasks across multiple domains, highlighting its potential for broad applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94152ba7-9251-4cf9-831b-c4ded40e81d1",
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "a1c2e06d61cd303be",
  "type": "user",
  "uuid": "ec9651d8-5309-431a-9300-7bb02b78b996",
  "sourceToolAssistantUUID": "94152ba7-9251-4cf9-831b-c4ded40e81d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T19:17:17.921Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Bx7kGrYg9WMvUzDL9Ykijp`</summary>

```json
{
  "url": "https://github.com/zjunlp/OneKE",
  "prompt": "Extract details about the three agents (Schema Agent, Extraction Agent, Reflection Agent), how the schema-guided pipeline works, what extraction tasks it supports (NER, RE, EE, etc.), and how the system relates to schema-guided extraction paradigms."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec9651d8-5309-431a-9300-7bb02b78b996",
  "isSidechain": true,
  "agentId": "a1c2e06d61cd303be",
  "requestId": "req_011CauReXtAcyZucCZ9Ti6Xo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c0fa5df-f5c8-4ced-9e3f-345b1e7e313c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEiRG3kCAxSP3AZkn3L86j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 348,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 10761,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 348,
          "output_tokens": 136,
          "cache_read_input_tokens": 10761,
          "cache_creation_input_tokens": 1128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1128,
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

_source line 10 · 2026-05-10T19:17:25.570Z_

<details><summary>↩ Tool result · `toolu_01Bx7kGrYg9WMvUzDL9Ykijp`</summary>

```text
# OneKE: Schema-Guided Knowledge Extraction System

## The Three-Agent Architecture

OneKE employs a collaborative multi-agent framework for information extraction:

**Schema Agent**: Responsible for generating or retrieving output schemas. Options include using "the default JSON output format," applying "predefined output schema retrieved from the knowledge base," or performing "schema generation by inferring from the task description."

**Extraction Agent**: Performs the actual information retrieval. It either "directly extract[s] information from the given text based on the task description" or retrieves "similar good cases from the knowledge base to aid in the extraction."

**Reflection Agent**: Validates and refines results. The system can either "directly return the extraction results" or employ "the self-consistency approach, and if inconsistencies appear, reflect on the original answer by retrieving similar bad cases."

## Schema-Guided Pipeline

The framework operates through a structured workflow where schemas constrain what information gets extracted. Users define "entity types," "relation types," or complete subject-predicate-object specifications. The system then generates schemas matching these specifications and uses them to guide LLM-based extraction, ensuring outputs conform to predefined structures.

## Supported Extraction Tasks

OneKE handles five major task categories:

- **Named Entity Recognition (NER)**: Identifies and classifies "named entities such as names, locations, and organizations"
- **Relation Extraction (RE)**: Extracts "relationships between entities, typically returns results as entity-relation-entity triples"
- **Event Extraction (EE)**: Identifies "event type, event trigger words, and event arguments"
- **Triple Extraction**: Identifies "subject-predicate-object triples" for "knowledge graph construction"
- **Open Domain IE**: Handles user-defined extraction tasks like "web news extraction" and "book knowledge extraction"

The system represents this flexibility as "Base-Type Task[s]" allowing users to "provide an explicit Instruction that clearly defines your extraction task."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c0fa5df-f5c8-4ced-9e3f-345b1e7e313c",
  "isSidechain": true,
  "promptId": "68ffd92d-2815-470d-87ce-b7a6b5d68021",
  "agentId": "a1c2e06d61cd303be",
  "type": "user",
  "uuid": "b9e07a87-b572-49b8-9dce-046a541b3883",
  "sourceToolAssistantUUID": "4c0fa5df-f5c8-4ced-9e3f-345b1e7e313c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T19:17:41.151Z_

Here is a concise report on the OneKE paper:

---

## 1. Full Title, Authors, Venue

**Title:** "OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System"

**Authors:** Yujie Luo, Xiangyuan Ru, Kangwei Liu, Lin Yuan, Mengshu Sun, Ningyu Zhang, Lei Liang, Zhiqiang Zhang, Jun Zhou, Lanning Wei, Da Zheng, Haofen Wang, and Huajun Chen

**Venue:** WWW 2025 (The Web Conference 2025), Demonstration Track (WWW Companion '25, April 28 - May 2, 2025)

**arXiv:** 2412.20005

---

## 2. What It Does

OneKE is a dockerized, multi-agent system for knowledge extraction from web pages and PDF documents across diverse domains (science, news, etc.). It supports five core extraction tasks:

- **Named Entity Recognition (NER)**
- **Relation Extraction (RE)**
- **Event Extraction (EE)**
- **Triple Extraction** (for knowledge graph construction)
- **Open Domain IE** (user-defined tasks)

The system uses a three-agent architecture:

1. **Schema Agent** -- analyzes and generates output schemas (default JSON format, predefined schemas from a knowledge base, or inferred schemas from task descriptions).
2. **Extraction Agent** -- performs the actual extraction using LLMs, optionally retrieving similar successful cases from the knowledge base to improve results.
3. **Reflection Agent** -- validates outputs using self-consistency checks, and if inconsistencies appear, reflects on the answer by retrieving similar failure cases for debugging.

A configurable knowledge base underpins all three agents, storing schemas, good-case examples, and bad-case examples for iterative improvement.

---

## 3. Relation to Schema-Guided Extraction Pipelines

OneKE is a direct instantiation of the schema-guided extraction paradigm:

- **Schemas as first-class artifacts:** Users define entity types, relation types, or subject-predicate-object specifications. The Schema Agent translates these into structured output schemas that constrain what the LLM extracts and how it formats results.
- **Schema-driven prompting:** The Extraction Agent receives the schema as part of its context, ensuring outputs conform to predefined structures rather than producing free-form text.
- **Iterative schema refinement:** The Reflection Agent and knowledge base create a feedback loop -- when extraction fails or is inconsistent, error cases are stored and used to improve future schema-guided extractions.
- **Generalization via schema:** By decoupling the extraction logic (agents + LLMs) from the domain definition (schemas), OneKE generalizes across domains without retraining. New extraction tasks only require a new schema specification.

In essence, OneKE demonstrates that a schema-guided pipeline -- where structured schemas control what to extract, how to format it, and how to validate it -- can unify diverse IE tasks (NER, RE, EE, triples) under a single agent-based framework powered by LLMs.

---

Sources:
- [arXiv Paper](https://arxiv.org/abs/2412.20005)
- [GitHub Repository (zjunlp/OneKE)](https://github.com/zjunlp/OneKE)
- [HuggingFace Paper Page](https://huggingface.co/papers/2412.20005)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9e07a87-b572-49b8-9dce-046a541b3883",
  "isSidechain": true,
  "agentId": "a1c2e06d61cd303be",
  "requestId": "req_011CauRfQdP53uJ5QXArph7h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58805437-9367-4253-a149-0f604cc53bab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5af3fec1-3b85-4665-945a-6639209a9c66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQJKahapQNaYUvsrmuARcy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 938,
      "cache_read_input_tokens": 11889,
      "output_tokens": 816,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 938
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 816,
          "cache_read_input_tokens": 11889,
          "cache_creation_input_tokens": 938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 938,
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
