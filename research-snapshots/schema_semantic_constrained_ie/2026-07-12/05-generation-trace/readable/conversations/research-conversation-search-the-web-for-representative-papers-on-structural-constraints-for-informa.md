# Research conversation: Search the web for representative papers on structural constraints for Information Extraction (IE) with LLMs (2022-2026)

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a88824f793ba94b4e.jsonl`
- **Structured JSON:** [`b065dca712b4017160f8.json`](../../sessions/b0/b065dca712b4017160f8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-14T02:35:41.730Z_

Search the web for representative papers on structural constraints for Information Extraction (IE) with LLMs (2022-2026). I need 5-6 key papers covering:

1. **UIE** (Unified Structure Generation for Universal Information Extraction) - Lu et al.
2. **InstructUIE** - instruction-tuned universal IE
3. **GoLLIE** - Guideline-following Large Language Model for IE (likely ICLR 2024)
4. **CodeIE** - code generation approach for IE
5. **USM** or **UniRel** or other structured prediction + LLM approaches for IE
6. Any 2024-2025 work on making LLMs output structured IE results (NER, RE, EE)

For each paper, find:
- Full title
- Authors (first 2-3)
- Venue and year
- Core method in 1-2 sentences
- ArXiv ID if available

Report all findings in a structured format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "a09cca70-b496-4e9c-b294-4e6f734411bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T02:35:41.733Z_

```json
{
  "parentUuid": "a09cca70-b496-4e9c-b294-4e6f734411bc",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f0110781-7821-4146-8ed4-8320cde024aa",
  "timestamp": "2026-05-14T02:35:41.733Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T02:35:44.209Z_



I'll search for these papers using web search. Let me fetch the tool schema first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0110781-7821-4146-8ed4-8320cde024aa",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gWZKn3x1WFfHYgUCqz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a80f1bdd-0658-4a3a-8601-48a9edc738e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015goVkEa9ZeofVZzNSUbaYn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6045,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6045,
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

_source line 4 · 2026-05-14T02:35:44.517Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CNq4nnnDzcPKsstvhXJMot`</summary>

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
  "parentUuid": "a80f1bdd-0658-4a3a-8601-48a9edc738e8",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gWZKn3x1WFfHYgUCqz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc974b2b-a96b-4abe-84e5-3b9efb33692c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015goVkEa9ZeofVZzNSUbaYn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6045,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6045,
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

### Tool result

_source line 5 · 2026-05-14T02:35:44.519Z_

<details><summary>↩ Tool result · `toolu_01CNq4nnnDzcPKsstvhXJMot`</summary>

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
  "parentUuid": "fc974b2b-a96b-4abe-84e5-3b9efb33692c",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "c32a9392-982d-45bd-8da1-50d4f8679aa6",
  "sourceToolAssistantUUID": "fc974b2b-a96b-4abe-84e5-3b9efb33692c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T02:35:46.798Z_



Let me search for each paper systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c32a9392-982d-45bd-8da1-50d4f8679aa6",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gWmSnb5mSiJ354utiB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31ac6058-c6e2-4836-8fac-e3ceee4b9fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHh8XMdBxZmfipGHspvB3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 14297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1459,
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

_source line 7 · 2026-05-14T02:35:47.810Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M96c9sd78QrDV68b8GDmt1`</summary>

```json
{
  "query": "UIE Unified Structure Generation Universal Information Extraction Lu et al 2022 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31ac6058-c6e2-4836-8fac-e3ceee4b9fe3",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gWmSnb5mSiJ354utiB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "962f55f2-fc70-478c-94fc-1a314e3ab66d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHh8XMdBxZmfipGHspvB3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 14297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1459,
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

_source line 8 · 2026-05-14T02:35:48.753Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DuGYvY1nJCyHfivnHbSfub`</summary>

```json
{
  "query": "InstructUIE instruction-tuned universal information extraction paper arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "962f55f2-fc70-478c-94fc-1a314e3ab66d",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gWmSnb5mSiJ354utiB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a00f9b8a-dcc3-4353-b9cf-bd28c678478a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHh8XMdBxZmfipGHspvB3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 14297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1459,
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

_source line 9 · 2026-05-14T02:35:49.693Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E278SX2MepHK8VN13EWVLQ`</summary>

```json
{
  "query": "GoLLIE guideline-following large language model information extraction ICLR 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a00f9b8a-dcc3-4353-b9cf-bd28c678478a",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gWmSnb5mSiJ354utiB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b13d05e-3e62-4069-a85c-f658b7fc8195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHh8XMdBxZmfipGHspvB3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 14297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1459,
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

_source line 10 · 2026-05-14T02:35:49.909Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017viRiL79bKzT8MjPyv5vbm`</summary>

```json
{
  "query": "CodeIE code generation information extraction paper arxiv 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b13d05e-3e62-4069-a85c-f658b7fc8195",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gWmSnb5mSiJ354utiB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26a9dfea-c09f-4e36-90bd-af0fb9cf325c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHh8XMdBxZmfipGHspvB3c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 14297,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1459
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 234,
          "cache_read_input_tokens": 14297,
          "cache_creation_input_tokens": 1459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1459,
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

_source line 11 · 2026-05-14T02:35:53.756Z_

<details><summary>↩ Tool result · `toolu_01M96c9sd78QrDV68b8GDmt1`</summary>

```text
Web search results for query: "UIE Unified Structure Generation Universal Information Extraction Lu et al 2022 arxiv"

Links: [{"title":"[2203.12277] Unified Structure Generation for Universal Information Extraction","url":"https://arxiv.org/abs/2203.12277"},{"title":"Unified Structure Generation for Universal Information Extraction - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.395/"},{"title":"Unified Structure Generation for Universal Information Extraction | universal-ie.github.io","url":"https://universal-ie.github.io/"},{"title":"Paper page - Unified Structure Generation for Universal Information Extraction","url":"https://huggingface.co/papers/2203.12277"},{"title":"[2203.12277v1] Unified Structure Generation for Universal Information Extraction","url":"https://arxiv.org/abs/2203.12277v1"},{"title":"[2301.03282] Universal Information Extraction as Unified Semantic Matching","url":"https://ar5iv.labs.arxiv.org/html/2301.03282"},{"title":"[PDF] Unified Structure Generation for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-Structure-Generation-for-Universal-Lu-Liu/5eb9dad01d9b61947d7a9aae6dfff400d20555b9"},{"title":"Uniﬁed Structure Generation for Universal Information Extraction","url":"https://arxiv.org/pdf/2203.12277"},{"title":"(PDF) Unified Structure Generation for Universal Information Extraction","url":"https://www.researchgate.net/publication/359435785_Unified_Structure_Generation_for_Universal_Information_Extraction"},{"title":"Schema as Parameterized Tools for Universal Information Extraction","url":"https://arxiv.org/html/2506.01276"}]

I found the paper you're looking for! Here are the details:

**Paper:** Unified Structure Generation for Universal Information Extraction, by Yaojie Lu and 7 other authors

**ArXiv ID:** 2203.12277 (published March 23, 2022)

**Key Contribution:** UIE is a unified text-to-structure generation framework that can universally model different IE tasks, adaptively generate targeted structures, and collaboratively learn general IE abilities from different knowledge sources

**Technical Approach:** UIE uniformly encodes different extraction structures via a structured extraction language, adaptively generates target extractions via a schema-based prompt mechanism - structural schema instructor, and captures the common IE abilities via a large-scale pre-trained text-to-structure model

**Results:** UIE achieved state-of-the-art performance on 4 IE tasks, 13 datasets, and on all supervised, low-resource, and few-shot settings for a wide range of entity, relation, event and sentiment extraction tasks and their unification

The paper was published at the 60th Annual Meeting of the Association for Computational Linguistics (ACL 2022) in Dublin, Ireland.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "962f55f2-fc70-478c-94fc-1a314e3ab66d",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "e059c23b-c51e-4099-ab42-78c4ba033a05",
  "sourceToolAssistantUUID": "962f55f2-fc70-478c-94fc-1a314e3ab66d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T02:35:54.091Z_

<details><summary>↩ Tool result · `toolu_01DuGYvY1nJCyHfivnHbSfub`</summary>

```text
Web search results for query: "InstructUIE instruction-tuned universal information extraction paper arxiv"

Links: [{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085"},{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning · GitHub","url":"https://github.com/BeyonderXX/InstructUIE"},{"title":"(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations","url":"https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"},{"title":"InstructUIE: Multi-task Instruction Tuning for Uniﬁed Information Extraction","url":"https://arxiv.org/pdf/2304.08085"},{"title":"YAYI-UIE: A Chat-Enhanced Instruction Tuning Framework for Universal Information Extraction","url":"https://arxiv.org/html/2312.15548v2"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"},{"title":"[2304.08085v1] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085v1"},{"title":"MR-UIE: Multi-Perspective Reasoning with Reinforcement Learning for Universal Information Extraction","url":"https://arxiv.org/html/2509.09082"},{"title":"Paper page - InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://huggingface.co/papers/2304.08085"},{"title":"[PDF] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/bbb2fc6e95d24fb58ab6c25b216b14ac49a32fbe"}]

I found the paper you're looking for. Here are the key details about the InstructUIE paper:

## InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction

**ArXiv ID:** 2304.08085  
**Published:** April 17, 2023

### Overview
InstructUIE is a unified information extraction framework based on instruction tuning, which can uniformly model various information extraction tasks and capture the inter-task dependency.

### Key Contributions
The paper introduces IE INSTRUCTIONS, a benchmark of 32 diverse information extraction datasets in a unified text-to-text format with expert-written instructions.

### Motivation
Large language models have unlocked strong multi-task capabilities from reading instructive prompts. However, recent studies have shown that existing large models still have difficulty with information extraction tasks. For example, gpt-3.5-turbo achieved an F1 score of 18.22 on the Ontonotes dataset, which is significantly lower than the state-of-the-art performance.

### Implementation
The model is built based on the pretrained Flan T5 model, and fine-tuned on IE INSTRUCTIONS data.

You can access the full paper directly at: https://arxiv.org/abs/2304.08085


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a00f9b8a-dcc3-4353-b9cf-bd28c678478a",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "1b7a0f48-f24e-4515-b880-c84c9e906c7e",
  "sourceToolAssistantUUID": "a00f9b8a-dcc3-4353-b9cf-bd28c678478a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T02:35:56.034Z_

<details><summary>↩ Tool result · `toolu_01E278SX2MepHK8VN13EWVLQ`</summary>

```text
Web search results for query: "GoLLIE guideline-following large language model information extraction ICLR 2024 arxiv"

Links: [{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview","url":"https://openreview.net/forum?id=Y3wpuxd7u9"},{"title":"ICLR Poster GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://iclr.cc/virtual/2024/poster/18435"},{"title":"GoLLIE | Guideline following Large Language Model for Information Extraction","url":"https://hitz-zentroa.github.io/GoLLIE/"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"GitHub - azminewasi/Awesome-LLMs-ICLR-24: It is a comprehensive resource hub compiling all LLM papers accepted at the International Conference on Learning Representations (ICLR) in 2024. · GitHub","url":"https://github.com/azminewasi/Awesome-LLMs-ICLR-24"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/notes/edits/attachment?id=x345y4wtJb&name=pdf"}]

I found information about GoLLIE. Here are the search results:

## Overview

GoLLIE (Guideline-following Large Language Model for IE) is a model able to improve zero-shot results on unseen IE tasks by virtue of being fine-tuned to comply with annotation guidelines.

## Key Problem

Large Language Models (LLMs) combined with instruction tuning have made significant progress when generalizing to unseen tasks. However, they have been less successful in Information Extraction (IE), lagging behind task-specific models. Previous attempts to leverage such information have failed, even with the largest models, as they are not able to follow the guidelines out-of-the-box.

## Solution and Results

Comprehensive evaluation empirically demonstrates that GoLLIE is able to generalize to and follow unseen guidelines, outperforming previous attempts at zero-shot information extraction.

## Technical Approach

GoLLIE is based on Code-Llama. The approach adopts a Python code-based representation for both the input and output of the model. This approach not only offers a clear and human-readable structure but also addresses several challenges typically associated with natural language instructions. It enables the representation of any information extraction task under a unified format.

## Publication

GoLLIE: annotation guidelines improve zero-shot information-extraction was published in the Proceedings of the ICLR 2024. The paper is also available on arXiv (arxiv 2310.03668).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b13d05e-3e62-4069-a85c-f658b7fc8195",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "c0dd7e3c-a90a-4155-95d3-0eee271e37bc",
  "sourceToolAssistantUUID": "0b13d05e-3e62-4069-a85c-f658b7fc8195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T02:35:56.978Z_

<details><summary>↩ Tool result · `toolu_017viRiL79bKzT8MjPyv5vbm`</summary>

```text
Web search results for query: "CodeIE code generation information extraction paper arxiv 2023"

Links: [{"title":"[2305.05711] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711"},{"title":"[2305.05711v2] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711v2"},{"title":"[PDF] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeIE:-Large-Code-Generation-Models-are-Better-Li-Sun/a86dd6c62d3dc9c7989c98a3e4ace3fd8000e515"},{"title":"[2311.02962] Retrieval-Augmented Code Generation for Universal Information Extraction","url":"https://arxiv.org/abs/2311.02962"},{"title":"GitHub - artpli/CodeIE: [ACL 23] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors · GitHub","url":"https://github.com/artpli/CodeIE"},{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.855/"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=CodeIE:+Large+code+generation+models+are+better+few-shot+information+extractors&author=Peng+Li&author=Tianxiang+Sun&author=Qiong+Tang&author=Hang+Yan&author=Wu+Yuanbin&author=Xuanjing+Huang&author=Xipeng+Qiu&publication_year=2023&journal=Proceedings+of+the+61st+Annual+Meeting+of+the+Association+for+Computational+Linguistics&pages=15339-15353"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v1"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"},{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors | Request PDF","url":"https://www.researchgate.net/publication/372919086_CodeIE_Large_Code_Generation_Models_are_Better_Few-Shot_Information_Extractors"}]

I found the CodeIE paper for you. Here are the key details:

## CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors

**Publication Details:**
The paper was submitted on May 9, 2023 and authored by Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, and Xipeng Qiu. This is an ACL 2023 paper with arXiv identifier 2305.05711.

**Core Idea:**
The paper proposes to recast the structured output in the form of code instead of natural language and utilize generative LLMs of code (Code-LLMs) such as Codex to perform IE tasks, in particular, named entity recognition and relation extraction. Code-LLMs can be well-aligned with these IE tasks by designing code-style prompts and formulating these IE tasks as code generation tasks.

**Motivation:**
It is nontrivial to perform information extraction (IE) tasks with NL-LLMs since the output of the IE task is usually structured and therefore is hard to be converted into plain text.

**Results:**
Experiment results on seven benchmarks show that the method consistently outperforms fine-tuning moderate-size pre-trained models specially designed for IE tasks (e.g., UIE) and prompting NL-LLMs under few-shot settings.

You can access the paper at https://arxiv.org/abs/2305.05711, and the official code repository is available at https://github.com/artpli/CodeIE.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26a9dfea-c09f-4e36-90bd-af0fb9cf325c",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "42583f0e-3880-4b54-a4ae-a85c732de45e",
  "sourceToolAssistantUUID": "26a9dfea-c09f-4e36-90bd-af0fb9cf325c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-14T02:35:59.229Z_

Now let me search for the remaining papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42583f0e-3880-4b54-a4ae-a85c732de45e",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gXgWuSsGR8FApknNjB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8b79b41-b323-4c1e-9299-b7acf22def4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YtLUFmTmcWq7hhtGyhDyK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3957,
      "cache_read_input_tokens": 15756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3957,
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

_source line 16 · 2026-05-14T02:36:00.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sxg4kv49T2BALsMsQvzTP9`</summary>

```json
{
  "query": "USM Universal Semantic Matching information extraction structured prediction LLM arxiv 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8b79b41-b323-4c1e-9299-b7acf22def4f",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gXgWuSsGR8FApknNjB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba836ad2-4149-4aa4-b177-9479ecc94b82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YtLUFmTmcWq7hhtGyhDyK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3957,
      "cache_read_input_tokens": 15756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3957,
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

_source line 17 · 2026-05-14T02:36:01.214Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RAzqX1otc3eyG4PLeCcAMs`</summary>

```json
{
  "query": "structured information extraction LLM NER relation event 2024 2025 survey constrained decoding arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba836ad2-4149-4aa4-b177-9479ecc94b82",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gXgWuSsGR8FApknNjB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "445e2da6-fba0-43ed-8d4e-1cd673efc190",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YtLUFmTmcWq7hhtGyhDyK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3957,
      "cache_read_input_tokens": 15756,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 15756,
          "cache_creation_input_tokens": 3957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3957,
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

_source line 18 · 2026-05-14T02:36:06.329Z_

<details><summary>↩ Tool result · `toolu_01Sxg4kv49T2BALsMsQvzTP9`</summary>

```text
Web search results for query: "USM Universal Semantic Matching information extraction structured prediction LLM arxiv 2023"

Links: [{"title":"[2301.03282] Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/abs/2301.03282"},{"title":"Universal Information Extraction as Unified Semantic Matching | Request PDF","url":"https://www.researchgate.net/publication/371922000_Universal_Information_Extraction_as_Unified_Semantic_Matching"},{"title":"Universal Information Extraction as Unified Semantic Matching - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230103282L/abstract"},{"title":"[PDF] Unified Structure Generation for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-Structure-Generation-for-Universal-Lu-Liu/5382c28b9f2dd30f15c836bea92382091b1d886f"},{"title":"Universal information extraction as unified semantic matching | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v37i11.26563"},{"title":"XNLP: An Interactive Demonstration System for Universal Structured NLP","url":"https://arxiv.org/html/2308.01846"},{"title":"[2510.13515] UniME-V2: MLLM-as-a-Judge for Universal Multimodal Embedding Learning","url":"https://arxiv.org/abs/2510.13515"},{"title":"LLM for Uniform Information Extraction Using Multi-task Learning Optimization | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-96-0055-7_2"},{"title":"Universal Information Extraction as Unified Semantic Matching | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26563"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"}]

Based on the search results, here's information about USM (Unified Semantic Matching):

## Overview

USM proposes to universally model various IE tasks with the Unified Semantic Matching framework, which introduces three unified token linking operations to model the abilities of structuring and conceptualizing.

## Problem and Approach

Traditional methods require task-specific model design and rely heavily on expensive supervision, making them difficult to generalize to new schemas. The USM framework decouples IE into two basic abilities, structuring and conceptualizing, which are shared by different tasks and schemas.

## Key Capabilities

USM can jointly encode schema and input text, uniformly extract substructures in parallel, and controllably decode target structures on demand.

## Performance

Empirical evaluation on 4 IE tasks shows that the proposed method achieves state-of-the-art performance under the supervised experiments and shows strong generalization ability in zero/few-shot transfer settings.

## Publication Details

The paper was submitted to arXiv on January 9, 2023 (arxiv ID: 2301.03282) and was later presented at the AAAI 2023 conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba836ad2-4149-4aa4-b177-9479ecc94b82",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "b7b54aa1-7677-4150-9248-ac278c851b83",
  "sourceToolAssistantUUID": "ba836ad2-4149-4aa4-b177-9479ecc94b82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T02:36:07.886Z_

<details><summary>↩ Tool result · `toolu_01RAzqX1otc3eyG4PLeCcAMs`</summary>

```text
Web search results for query: "structured information extraction LLM NER relation event 2024 2025 survey constrained decoding arxiv"

Links: [{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"Information Extraction in Low-Resource Scenarios: Survey and Perspective","url":"https://arxiv.org/html/2202.08063v6"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Large language models for generative information extraction: a survey","url":"https://d-nb.info/1354655508/34"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"},{"title":"Published as a conference paper at ICLR 2024 LINEARITY OF RELATION DECODING IN","url":"https://arxiv.org/pdf/2308.09124"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"}]

I've found several highly relevant results for your search on structured information extraction with LLMs, NER, relation extraction, event extraction, constrained decoding, and related topics. Here are the key findings:

## Major Surveys and Resources

Recent surveys categorize methods for adapting LLMs to IE tasks including Data Augmentation, Prompt Design, Zero-shot Learning, Constrained Decoding Generation, Few-shot Learning, and Supervised Fine-tuning.

A major 2024 survey published in Frontiers of Computer Science covers Large language models for generative information extraction, available on arxiv.

A 2025 survey on generative information extraction appears in the proceedings of COLING.

## Key Technical Approaches

**Constrained Decoding:** Constrained decoding intervenes in the decoding process of LMs by masking out invalid tokens based on given constraints and prefix tokens, guiding the LM to sample only from valid tokens and ensuring output conforms to a predefined structure.

Recent benchmarks evaluate state-of-the-art constrained decoding frameworks including Guidance, Outlines, Llamacpp, XGrammar, OpenAI, and Gemini, providing insights into their capabilities and limitations on structured generation with real-world JSON schemas.

## IE Tasks Coverage

The surveys comprehensively cover Named Entity Recognition (NER), Relation Extraction (RE) and Event Extraction (EE) as major subtasks.

A GitHub repository (quqxui/Awesome-LLM4IE-Papers) maintains an updated collection of papers on LLM-based information extraction spanning 2023-2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "445e2da6-fba0-43ed-8d4e-1cd673efc190",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "b12ba857-8405-48c0-ac89-a752a3058fe6",
  "sourceToolAssistantUUID": "445e2da6-fba0-43ed-8d4e-1cd673efc190",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-14T02:36:11.371Z_

Let me search for more specific recent (2024-2025) papers on structured output for IE with LLMs, and get author details for the papers found so far.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b12ba857-8405-48c0-ac89-a752a3058fe6",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gYVA4ELimFL3KK35RN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b15f2734-5589-469b-b285-864e2face98c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018icSSLPWAovc6R1LZGtidd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 19713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 21 · 2026-05-14T02:36:12.474Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PBQcREFas1kYUm2Fb8qMSJ`</summary>

```json
{
  "query": "ADELIE aligning LLMs information extraction EMNLP 2024 arxiv schema-constrained"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b15f2734-5589-469b-b285-864e2face98c",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gYVA4ELimFL3KK35RN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2a89e4c-35c7-495b-ad56-f24002304227",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018icSSLPWAovc6R1LZGtidd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 19713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 22 · 2026-05-14T02:36:13.318Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XHbXxZQAon4iSCJK9jTsqa`</summary>

```json
{
  "query": "InstructUIE authors Xiao Wang first authors 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2a89e4c-35c7-495b-ad56-f24002304227",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gYVA4ELimFL3KK35RN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8003f9c7-0488-4ef0-9ea6-2a3e16386028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018icSSLPWAovc6R1LZGtidd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 19713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 23 · 2026-05-14T02:36:16.340Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FasGexkxT12LFWRiQcqecr`</summary>

```json
{
  "query": "GoLLIE authors Oscar Sainz Iker Garcia-Ferrero arxiv 2310.03668"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8003f9c7-0488-4ef0-9ea6-2a3e16386028",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gYVA4ELimFL3KK35RN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9dce0e98-b985-4197-9437-3487cf5ea9d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018icSSLPWAovc6R1LZGtidd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 19713,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2019
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 19713,
          "cache_creation_input_tokens": 2019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2019,
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

_source line 24 · 2026-05-14T02:36:17.830Z_

<details><summary>↩ Tool result · `toolu_01XHbXxZQAon4iSCJK9jTsqa`</summary>

```text
Web search results for query: "InstructUIE authors Xiao Wang first authors 2023"

Links: [{"title":"(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations","url":"https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"},{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085"},{"title":"[2304.08085v1] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085v1"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"},{"title":"[PDF] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/InstructUIE:-Multi-task-Instruction-Tuning-for-Wang-Zhou/bbb2fc6e95d24fb58ab6c25b216b14ac49a32fbe"},{"title":"Homepage of Xiao Wang","url":"https://wangxiaocs.github.io/"},{"title":"Publication — Wang Lab","url":"https://www.wangxiaolab.org/publications"},{"title":"Xiao Wang","url":"https://scholar.google.com/citations?user=AGS_dK8AAAAJ&hl=en"},{"title":"Xiao Wang | Nanjing University | 27 Publications | 104 Citations | Related Authors","url":"https://scispace.com/authors/xiao-wang-jkesd34ccw"},{"title":"Publications - Xiao Wang","url":"https://wangxiao1254.github.io/publications/"}]

Based on the search results, I found information about the InstructUIE paper from 2023 with Xiao Wang as the first author.

The InstructUIE paper was submitted on April 17, 2023, and the authors include Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, and Chunsai Du.

InstructUIE is a unified information extraction framework based on instruction tuning, which can uniformly model various information extraction tasks and capture the inter-task dependency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8003f9c7-0488-4ef0-9ea6-2a3e16386028",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "e48e003d-c67b-4b80-9e8a-1d8ed5139398",
  "sourceToolAssistantUUID": "8003f9c7-0488-4ef0-9ea6-2a3e16386028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T02:36:20.945Z_

<details><summary>↩ Tool result · `toolu_01FasGexkxT12LFWRiQcqecr`</summary>

```text
Web search results for query: "GoLLIE authors Oscar Sainz Iker Garcia-Ferrero arxiv 2310.03668"

Links: [{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"[PDF] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GoLLIE:-Annotation-Guidelines-improve-Zero-Shot-Sainz-Garc%C3%ADa-Ferrero/3f40edfcafc018b2cb54612a9aaa9d6b43a11a26"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v5"},{"title":"dblp: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction.","url":"https://dblp.org/rec/journals/corr/abs-2310-03668.html"},{"title":"dblp: Oscar Sainz","url":"https://dblp.org/pid/266/1113.html"},{"title":"dblp: Iker García-Ferrero","url":"https://dblp.org/pid/305/9880.html"},{"title":"gollie : annotation guidelines improve zero-shot ...","url":"https://arxiv.org/pdf/2310.03668"},{"title":"Iker García-Ferrero","url":"https://scholar.google.es/citations?user=yoOzj1MAAAAJ&hl=es"},{"title":"Oscar Sainz","url":"https://openreview.net/profile?id=~Oscar_Sainz1"},{"title":"Oscar Sainz","url":"https://www.catalyzex.com/author/Oscar%20Sainz"}]

Based on the search results, I found comprehensive information about the GoLLIE paper with arxiv ID 2310.03668:

## GoLLIE Paper Summary

The authors of this paper are Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, Germ­án Rigau, and Eneko Agirre.

GoLLIE (Guideline-following Large Language Model for IE) is a model able to improve zero-shot results on unseen IE tasks by virtue of being fine-tuned to comply with annotation guidelines.

The authors are affiliated with HiTZ Basque Center for Language Technology - Ixa NLP Group at the University of the Basque Country (UPV/EHU).

### Key Findings

Large Language Models (LLMs) combined with instruction tuning have made significant progress when generalizing to unseen tasks, but they have been less successful in Information Extraction (IE), lagging behind task-specific models. GoLLIE is able to generalize to and follow unseen guidelines, outperforming previous attempts at zero-shot information extraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dce0e98-b985-4197-9437-3487cf5ea9d1",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "06ef2ae2-4a0f-4812-aff0-d87d753a205b",
  "sourceToolAssistantUUID": "9dce0e98-b985-4197-9437-3487cf5ea9d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T02:36:21.449Z_

<details><summary>↩ Tool result · `toolu_01PBQcREFas1kYUm2Fb8qMSJ`</summary>

```text
Web search results for query: "ADELIE aligning LLMs information extraction EMNLP 2024 arxiv schema-constrained"

Links: [{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/html/2405.05008v1"},{"title":"[2405.05008] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/abs/2405.05008"},{"title":"GitHub - THU-KEG/ADELIE: [EMNLP2024] Aligning Large Language Models on Information Extraction · GitHub","url":"https://github.com/THU-KEG/ADELIE"},{"title":"Aligning Large Language Models on Information Extraction","url":"https://aclanthology.org/2024.emnlp-main.419.pdf"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/adelie-aligning-large-language-models-information-extraction"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.419/"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://openreview.net/pdf?id=hi5k4PDnX7"},{"title":"Main Conference - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_main_conference/"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/386188440_ADELIE_Aligning_Large_Language_Models_on_Information_Extraction"},{"title":"[Quick Review] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://liner.com/review/adelie-aligning-large-language-models-on-information-extraction"}]

I've found detailed information about ADELIE. Here's a comprehensive summary of the research:

## ADELIE: Aligning Large Language Models on Information Extraction

ADELIE (Aligning large language moDELs on Information Extraction) is an aligned LLM that effectively solves various IE tasks, including closed IE, open IE, and on-demand IE. The paper was accepted by the EMNLP 2024 main conference.

### Key Problem and Motivation

Large language models (LLMs) usually fall short on information extraction (IE) tasks and struggle to follow the complex instructions of IE tasks. This primarily arises from LLMs not being aligned with humans, as mainstream alignment datasets typically do not include IE data.

### Approach and Methods

The researchers first collect and construct a high-quality alignment corpus IEInstruct for IE. Then they train ADELIE_SFT using instruction tuning on IEInstruct. They further train ADELIE_SFT with direct preference optimization (DPO) objective, resulting in ADELIE_DPO.

### Results

Extensive experiments on various held-out IE datasets demonstrate that the models (ADELIE_SFT and ADELIE_DPO) achieve state-of-the-art (SoTA) performance among open-source models. The researchers further explore the general capabilities of ADELIE, and experimental results reveal that their general capabilities do not exhibit a noticeable decline.

### Availability

The researchers release three ADELIE models based on LLama-2 (7B), Llama-3.2 (3B) and Qwen2.5 (1.5B). The models are available in the HuggingFace Hub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2a89e4c-35c7-495b-ad56-f24002304227",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "63fc4367-89a7-4543-9216-efdd24a7f55f",
  "sourceToolAssistantUUID": "d2a89e4c-35c7-495b-ad56-f24002304227",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-14T02:36:24.235Z_

Now let me get the remaining author and venue details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63fc4367-89a7-4543-9216-efdd24a7f55f",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gZVE3yF1uRggB5KrQj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42343dff-803e-42a9-91d9-b29f53f594e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZoxUXVK3Dya1Ga8KEFwrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1539,
      "cache_creation_input_tokens": 1166,
      "cache_read_input_tokens": 21732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1166,
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

_source line 28 · 2026-05-14T02:36:25.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Shzc4GRfvwdkzNUASUehgv`</summary>

```json
{
  "query": "USM \"Universal Information Extraction as Unified Semantic Matching\" authors Lou Yaojie Lu AAAI 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42343dff-803e-42a9-91d9-b29f53f594e5",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gZVE3yF1uRggB5KrQj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76f407f3-1117-4a13-9841-e90a3ce82d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZoxUXVK3Dya1Ga8KEFwrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1539,
      "cache_creation_input_tokens": 1166,
      "cache_read_input_tokens": 21732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1166,
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

_source line 29 · 2026-05-14T02:36:26.530Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0114aTjpFVQodZ5SSzxU5kVc`</summary>

```json
{
  "query": "ADELIE authors Ning Hao Yixin Cao THU-KEG 2024 arxiv 2405.05008"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76f407f3-1117-4a13-9841-e90a3ce82d5f",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gZVE3yF1uRggB5KrQj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50f7cc05-b385-4e16-b3dc-70df870395d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZoxUXVK3Dya1Ga8KEFwrB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1539,
      "cache_creation_input_tokens": 1166,
      "cache_read_input_tokens": 21732,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1166
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1539,
          "output_tokens": 157,
          "cache_read_input_tokens": 21732,
          "cache_creation_input_tokens": 1166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1166,
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

_source line 30 · 2026-05-14T02:36:30.428Z_

<details><summary>↩ Tool result · `toolu_01Shzc4GRfvwdkzNUASUehgv`</summary>

```text
Web search results for query: "USM "Universal Information Extraction as Unified Semantic Matching" authors Lou Yaojie Lu AAAI 2023"

Links: [{"title":"Universal Information Extraction as Unified Semantic Matching | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26563"},{"title":"Universal Information Extraction as Unified Semantic Matching | Request PDF","url":"https://www.researchgate.net/publication/371922000_Universal_Information_Extraction_as_Unified_Semantic_Matching"},{"title":"[PDF] Universal Information Extraction as Unified Semantic Matching | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Universal-Information-Extraction-as-Unified-Lou-Lu/7ccfd5953e75f242536e99cdeda545a3c66ea98f"},{"title":"[2301.03282] Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/abs/2301.03282"},{"title":"Yaojie Lu's Homepage","url":"https://luyaojie.github.io/publication.html"},{"title":"Universal information extraction as unified semantic matching | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v37i11.26563"},{"title":"Universal Information Extraction as Unified Semantic Matching - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230103282L/abstract"},{"title":"[PDF] Unified Structure Generation for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-Structure-Generation-for-Universal-Lu-Liu/5382c28b9f2dd30f15c836bea92382091b1d886f"},{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://ar5iv.labs.arxiv.org/html/2304.08085"},{"title":"YAYI-UIE: A Chat-Enhanced Instruction Tuning Framework for Universal Information Extraction","url":"https://arxiv.org/html/2312.15548v2"}]

Based on the search results, I found detailed information about the paper "Universal Information Extraction as Unified Semantic Matching":

## Paper Information

**Title:** Universal Information Extraction as Unified Semantic Matching (USM)

**Authors:** Jie Lou, Yaojie Lu, Dai Dai, Wei Jia, Hongyu Lin, Xianpei Han, Le Sun, and Hua Wu

**Publication:** AAAI 2023

## Paper Overview

The paper proposes to universally model various IE (Information Extraction) tasks with the Unified Semantic Matching (USM) framework, which introduces three unified token linking operations to model the abilities of structuring and conceptualizing.

Empirical evaluation on 4 IE tasks shows that the proposed method achieves state-of-the-art performance under supervised experiments and shows strong generalization ability in zero/few-shot transfer settings.

**Official Sources:**
- AAAI Conference proceedings
- ArXiv preprint: 2301.03282 (submitted January 9, 2023)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76f407f3-1117-4a13-9841-e90a3ce82d5f",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "f86569cc-8c45-4c99-8e22-5b006977d4e9",
  "sourceToolAssistantUUID": "76f407f3-1117-4a13-9841-e90a3ce82d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T02:36:31.879Z_

<details><summary>↩ Tool result · `toolu_0114aTjpFVQodZ5SSzxU5kVc`</summary>

```text
Web search results for query: "ADELIE authors Ning Hao Yixin Cao THU-KEG 2024 arxiv 2405.05008"

Links: [{"title":"[2405.05008] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/abs/2405.05008"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/html/2405.05008"},{"title":"arXiv:2405.05008v2 [cs.CL] 24 Oct 2024","url":"https://arxiv.org/pdf/2405.05008"},{"title":"Publications - Xiaozhi Wang 王晓智","url":"https://bakser.github.io/publications/"},{"title":"Computer Science Mar 2024","url":"https://arxiv.org/list/cs/2024-03?skip=3960&show=2000"},{"title":"Computer Science May 2024","url":"https://arxiv.org/list/cs/2024-05?skip=8675&show=2000"},{"title":"Computer Vision and Pattern Recognition Aug 2024","url":"https://arxiv.org/list/cs.CV/2024-08?skip=225&show=2000"},{"title":"Haixin Wang - Google 学术搜索","url":"https://scholar.google.com/citations?user=RGZUJOkAAAAJ&hl=zh-CN"},{"title":"Computation and Language Apr 2026","url":"https://arxiv.org/list/cs.CL/current?skip=35&show=2000"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=1399&show=2000"}]

Based on the search results, I found information about the ADELIE paper (arxiv 2405.05008):

ADELIE (Aligning large language moDELs on Information Extraction) is an aligned LLM that effectively solves various IE tasks, including closed IE, open IE, and on-demand IE.

The paper was authored by Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, and Juanzi Li, and was published at EMNLP 2024.

The search results show that the authors are affiliated with THU-KEG (Tsinghua University Knowledge Engineering Group), which is evident from the author profiles found in the search results. However, I should note that while your query mentioned specific names like "Ning Hao" and "Yixin Cao," the search results for the actual ADELIE paper (2405.05008) show the primary authors listed above. Yixin Cao is mentioned as a co-author on other related work by these researchers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50f7cc05-b385-4e16-b3dc-70df870395d6",
  "isSidechain": true,
  "promptId": "73144d63-ba4e-4acf-8a9c-4cccb6d812d3",
  "agentId": "a88824f793ba94b4e",
  "type": "user",
  "uuid": "698b4a31-2ec0-4e22-b8a2-bfa058606825",
  "sourceToolAssistantUUID": "50f7cc05-b385-4e16-b3dc-70df870395d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-14T02:37:00.665Z_

Here are the findings for 6 representative papers on structural constraints for IE with LLMs (2022--2026):

---

**1. UIE -- Unified Structure Generation for Universal Information Extraction**
- **Authors:** Yaojie Lu, Qing Liu, Dai Dai, et al.
- **Venue:** ACL 2022
- **ArXiv:** 2203.12277
- **Method:** Defines a structured extraction language (SEL) to uniformly encode different IE output structures (entity, relation, event, sentiment). Uses a schema-based prompt mechanism (Structural Schema Instructor) with a large-scale pre-trained text-to-structure model to adaptively generate target structures. Achieves SOTA on 4 IE tasks across 13 datasets in supervised, low-resource, and few-shot settings.

---

**2. InstructUIE -- Multi-task Instruction Tuning for Unified Information Extraction**
- **Authors:** Xiao Wang, Weikang Zhou, Can Zu, et al.
- **Venue:** arXiv 2023 (2304.08085)
- **ArXiv:** 2304.08085
- **Method:** Builds IE INSTRUCTIONS, a benchmark of 32 diverse IE datasets in unified text-to-text format with expert-written instructions. Fine-tunes Flan-T5 on this benchmark, enabling a single model to handle NER, RE, EE, etc. via natural language instructions. Demonstrates that instruction-tuned smaller models can substantially outperform GPT-3.5 on IE tasks.

---

**3. GoLLIE -- Annotation Guidelines improve Zero-Shot Information-Extraction**
- **Authors:** Oscar Sainz, Iker Garcia-Ferrero, Rodrigo Agerri, et al.
- **Venue:** ICLR 2024
- **ArXiv:** 2310.03668
- **Method:** Fine-tunes Code-LLaMA to follow annotation guidelines expressed as Python class definitions (code-based schema representation). The model takes entity/relation/event type definitions as Python dataclasses and generates structured output as Python code. This code-based formulation enables strong zero-shot generalization to unseen IE schemas, outperforming previous zero-shot IE approaches.

---

**4. CodeIE -- Large Code Generation Models are Better Few-Shot Information Extractors**
- **Authors:** Peng Li, Tianxiang Sun, Qiong Tang, et al.
- **Venue:** ACL 2023
- **ArXiv:** 2305.05711
- **Method:** Recasts IE structured output as code rather than natural language and uses code-LLMs (e.g., Codex) with code-style prompts to perform NER and RE as code generation tasks. The code formulation naturally captures the structured nature of IE outputs. Consistently outperforms both fine-tuned IE-specific models (e.g., UIE) and NL-LLM prompting under few-shot settings.

---

**5. USM -- Universal Information Extraction as Unified Semantic Matching**
- **Authors:** Jie Lou, Yaojie Lu, Dai Dai, et al.
- **Venue:** AAAI 2023
- **ArXiv:** 2301.03282
- **Method:** Models IE as unified semantic matching via three token-linking operations that capture structuring (identifying spans/structures) and conceptualizing (mapping to schema types). Jointly encodes schema and input text, extracts substructures in parallel, and controllably decodes target structures on demand. Achieves SOTA on 4 IE tasks with strong zero/few-shot transfer ability.

---

**6. ADELIE -- Aligning Large Language Models on Information Extraction**
- **Authors:** Yunjia Qi, Hao Peng, Xiaozhi Wang, et al. (THU-KEG)
- **Venue:** EMNLP 2024
- **ArXiv:** 2405.05008
- **Method:** Constructs IEInstruct, a high-quality alignment corpus for IE, then trains LLMs with instruction tuning (SFT) followed by Direct Preference Optimization (DPO). Covers closed IE, open IE, and on-demand IE. ADELIE achieves SOTA among open-source models on diverse held-out IE benchmarks while preserving general LLM capabilities. Released in 1.5B/3B/7B sizes.

---

**Summary of the landscape:** These papers represent three main paradigms for structural constraints in LLM-based IE:
- **Text-to-structure generation** (UIE, InstructUIE): Define a linearized structure language and train seq2seq models to generate it.
- **Code-based schema representation** (GoLLIE, CodeIE): Leverage code LLMs and Python class/function definitions to naturally express IE schemas and structured outputs.
- **Semantic matching / alignment** (USM, ADELIE): Frame IE as matching or align LLMs specifically for IE through curated data and preference optimization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "698b4a31-2ec0-4e22-b8a2-bfa058606825",
  "isSidechain": true,
  "agentId": "a88824f793ba94b4e",
  "requestId": "req_011Cb1gaFnCmtQMnyHG7sQnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d375d27-5b52-465a-aadf-74cf39889ef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7c183f8e-6937-44d3-95b4-38b985cfc909",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqwYLcWbEJAtwmmYFPSyBr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3320,
      "cache_read_input_tokens": 22898,
      "output_tokens": 1191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3320
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1191,
          "cache_read_input_tokens": 22898,
          "cache_creation_input_tokens": 3320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3320,
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
