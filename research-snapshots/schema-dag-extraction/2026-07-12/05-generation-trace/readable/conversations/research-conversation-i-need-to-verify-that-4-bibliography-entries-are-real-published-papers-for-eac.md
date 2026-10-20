# Research conversation: I need to verify that 4 bibliography entries are real, published papers. For each, do a WebSearch and confirm the paper 

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a3424ecd3141166e3.jsonl`
- **Structured JSON:** [`7a9a060ea5455ff70c35.json`](../../sessions/7a/7a9a060ea5455ff70c35.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-16T17:03:54.114Z_

I need to verify that 4 bibliography entries are real, published papers. For each, do a WebSearch and confirm the paper exists with correct metadata.

1. **gliner2-2025**: "GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface" by Zaratiana et al., EMNLP 2025 System Demos. Search: "GLiNER2 Zaratiana 2025 multi-task"
2. **sclar-sensitivity-2024**: "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design" by Sclar et al., TACL 2024. Search: "Sclar sensitivity spurious features prompt design TACL 2024"
3. **json-schema-bench-2025**: "Generating Structured Outputs from Language Models: Benchmark and Studies" by Geng et al., 2025, arXiv:2501.10868. Search: "structured outputs language models benchmark 2501.10868"
4. **li2023evaluating**: "Evaluating ChatGPT's Information Extraction Capabilities" by Li et al., 2023, arXiv:2304.11633. Search: "evaluating ChatGPT information extraction Li 2304.11633"

For each, report: exists (yes/no), correct title, correct authors, correct venue/year, any corrections needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "247674ff-ea95-46d4-ba19-340e1c5404f3",
  "agentId": "a3424ecd3141166e3",
  "type": "user",
  "uuid": "fdaa408f-e77f-448c-90be-26009429bae1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T17:03:54.118Z_

```json
{
  "parentUuid": "fdaa408f-e77f-448c-90be-26009429bae1",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
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
      "WebSearch",
      "mcp__agent-ml-research__read_project_file"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__read_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "cf21eb21-f5dc-48fb-a35d-8da52fe5d3d8",
  "timestamp": "2026-05-16T17:03:54.118Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T17:03:57.078Z_



I'll search for all four papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf21eb21-f5dc-48fb-a35d-8da52fe5d3d8",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
  "requestId": "req_011Cb6cLLyeiGYBRqE8JGw86",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f11ed8b1-0cf1-4324-ae89-7ac3ffb7960e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L54pQnGLuYBPdLkMfAsfLG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6054,
      "cache_read_input_tokens": 7330,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6054
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 7330,
          "cache_creation_input_tokens": 6054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6054,
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

### Tool call

_source line 4 · 2026-05-16T17:03:57.084Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YPzjz1jSr31vvc3fLDUtkt`</summary>

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
  "parentUuid": "f11ed8b1-0cf1-4324-ae89-7ac3ffb7960e",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
  "requestId": "req_011Cb6cLLyeiGYBRqE8JGw86",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d729952f-b017-4de4-99d9-657b613bf2ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L54pQnGLuYBPdLkMfAsfLG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6054,
      "cache_read_input_tokens": 7330,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6054
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 7330,
          "cache_creation_input_tokens": 6054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6054,
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

_source line 5 · 2026-05-16T17:03:57.086Z_

<details><summary>↩ Tool result · `toolu_01YPzjz1jSr31vvc3fLDUtkt`</summary>

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
  "parentUuid": "d729952f-b017-4de4-99d9-657b613bf2ca",
  "isSidechain": true,
  "promptId": "247674ff-ea95-46d4-ba19-340e1c5404f3",
  "agentId": "a3424ecd3141166e3",
  "type": "user",
  "uuid": "8d8eb9dc-aa3e-49e9-a006-2051ae45f56f",
  "sourceToolAssistantUUID": "d729952f-b017-4de4-99d9-657b613bf2ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T17:04:00.360Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UjzoXV4KgADA9wSDtN9haC`</summary>

```json
{
  "query": "GLiNER2 Zaratiana 2025 multi-task information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d8eb9dc-aa3e-49e9-a006-2051ae45f56f",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
  "requestId": "req_011Cb6cLaV1UfmZYArmLWNTd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9d8c0df-c43c-48e9-ae24-9c8a5c53826b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WET2vuNzp2b2HqMVXdVuJR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 7 · 2026-05-16T17:04:00.364Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GZK83uz3sdsdPSp2ez2G4F`</summary>

```json
{
  "query": "Sclar sensitivity spurious features prompt design TACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9d8c0df-c43c-48e9-ae24-9c8a5c53826b",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
  "requestId": "req_011Cb6cLaV1UfmZYArmLWNTd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fc3c59d-bf91-4f2e-a8b9-339a04827408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WET2vuNzp2b2HqMVXdVuJR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 8 · 2026-05-16T17:04:00.843Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012YhY6MmtTAMAWWkfUUcdmr`</summary>

```json
{
  "query": "structured outputs language models benchmark 2501.10868"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fc3c59d-bf91-4f2e-a8b9-339a04827408",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
  "requestId": "req_011Cb6cLaV1UfmZYArmLWNTd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2aadb37-8e9a-4140-afbd-792a379d3c01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WET2vuNzp2b2HqMVXdVuJR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 9 · 2026-05-16T17:04:01.206Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ASywDqJFRykKGZddsJATj4`</summary>

```json
{
  "query": "evaluating ChatGPT information extraction Li 2304.11633"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2aadb37-8e9a-4140-afbd-792a379d3c01",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
  "requestId": "req_011Cb6cLaV1UfmZYArmLWNTd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5d0b038-0e52-4da4-9615-36146bca7eaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WET2vuNzp2b2HqMVXdVuJR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13384,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1451
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 13384,
          "cache_creation_input_tokens": 1451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1451,
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

_source line 10 · 2026-05-16T17:04:05.595Z_

<details><summary>↩ Tool result · `toolu_01ASywDqJFRykKGZddsJATj4`</summary>

```text
Web search results for query: "evaluating ChatGPT information extraction Li 2304.11633"

Links: [{"title":"[2304.11633] Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://arxiv.org/abs/2304.11633"},{"title":"GitHub - pkuserc/ChatGPT_for_IE: Evaluating ChatGPT’s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://github.com/pkuserc/ChatGPT_for_IE"},{"title":"[2304.11633v1] Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://arxiv.org/abs/2304.11633v1"},{"title":"dblp: Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness.","url":"https://dblp.org/rec/journals/corr/abs-2304-11633.html"},{"title":"[PDF] Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluating-ChatGPT's-Information-Extraction-An-of-Li-Fang/88abef771472c3aa46c53d5d626a0d0c3b66e8cd"},{"title":"[2304.11633] Evaluating ChatGPT’s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://ar5iv.labs.arxiv.org/html/2304.11633"},{"title":"(PDF) Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://www.researchgate.net/publication/370227431_Evaluating_ChatGPT's_Information_Extraction_Capabilities_An_Assessment_of_Performance_Explainability_Calibration_and_Faithfulness"},{"title":"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230411633L/abstract"},{"title":"ChatGPT Information Extraction Evaluation","url":"https://www.emergentmind.com/papers/2304.11633"},{"title":"[Paper Note] Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness, Bo Li+, arXiv'23 · Issue #534 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/534"}]

Based on the search results, I found the paper you're looking for. Here's an overview:

## Paper Overview

The paper focuses on assessing the overall ability of ChatGPT using 7 fine-grained information extraction (IE) tasks. It presents a systematic analysis by measuring ChatGPT's performance, explainability, calibration, and faithfulness, and resulting in 15 keys from either the ChatGPT or domain experts.

## Key Findings

**Performance:**
ChatGPT's performance in Standard-IE setting is poor, but it surprisingly exhibits excellent performance in the OpenIE setting, as evidenced by human evaluation.

**Explainability and Faithfulness:**
ChatGPT provides high-quality and trustworthy explanations for its decisions. ChatGPT demonstrates a high level of faithfulness to the original text in the majority of cases.

**Calibration:**
There is an issue of ChatGPT being overconfident in its predictions, which resulting in low calibration.

## Paper Details

The paper was authored by Bo Li, Gexiang Fang, Yang Yang, Quansen Wang, Wei Ye, Wen Zhao, and Shikun Zhang, and was submitted on April 23, 2023. The authors manually annotated and released test sets of 7 fine-grained IE tasks containing 14 datasets. The code and datasets are available on GitHub at https://github.com/pkuserc/ChatGPT_for_IE.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5d0b038-0e52-4da4-9615-36146bca7eaf",
  "isSidechain": true,
  "promptId": "247674ff-ea95-46d4-ba19-340e1c5404f3",
  "agentId": "a3424ecd3141166e3",
  "type": "user",
  "uuid": "813c4099-7d25-483f-a8b6-a7457ddc8c92",
  "sourceToolAssistantUUID": "d5d0b038-0e52-4da4-9615-36146bca7eaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T17:04:07.302Z_

<details><summary>↩ Tool result · `toolu_01UjzoXV4KgADA9wSDtN9haC`</summary>

```text
Web search results for query: "GLiNER2 Zaratiana 2025 multi-task information extraction"

Links: [{"title":"GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface","url":"https://arxiv.org/html/2507.18546v1"},{"title":"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-demos.10/"},{"title":"[2507.18546] GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface","url":"https://arxiv.org/abs/2507.18546"},{"title":"[PDF] GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GLiNER2:-An-Efficient-Multi-Task-Information-System-Zaratiana-Pasternak/73459ec452412f2653b341d55632190aeadc1e12"},{"title":"GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface [Quick Review]","url":"https://liner.com/review/gliner2-efficient-multitask-information-extraction-system-with-schemadriven-interface"},{"title":"Paper page - GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface","url":"https://huggingface.co/papers/2507.18546"},{"title":"GitHub - urchade/GLiNER: Generalist and Lightweight Model for Named Entity Recognition (Extract any entity types from texts) · GitHub","url":"https://github.com/urchade/GLiNER"},{"title":"GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250718546Z/abstract"},{"title":"fastino/gliner2-multi-v1 · Hugging Face","url":"https://huggingface.co/fastino/gliner2-multi-v1"},{"title":"GLiNER2: An Efficient Multi-Task Information Extraction System","url":"https://arxiv.org/pdf/2507.18546"}]

Based on the search results, here's information about GLiNER2:

## Overview

GLiNER2 is an efficient multi-task information extraction system developed by Urchade Zaratiana, Gil Pasternak, Oliver Boyd, George Hurn-Maloney, and Ash Lewis at Fastino AI.

## Key Features

GLiNER2 unifies entity recognition, text classification, and hierarchical extraction in a single CPU-efficient model, enabling multi-task extraction through declarative schemas while maintaining under 500M parameters for practical deployment.

The system maintains CPU efficiency while supporting entity recognition with natural language type descriptions and nested/overlapping spans, document-level classification with configurable single or multi-label outputs, and complex extraction schemas that capture hierarchical structures with parent-child relationships and repeated patterns.

## Technical Approach

GLiNER2 is built on a pretrained transformer encoder architecture and introduces multi-task composition through an intuitive schema-based interface. The library's Python API allows developers to define extraction schemas declaratively, compose multiple tasks in a single inference call, and deploy models with just a few lines of code.

## Performance

The system demonstrates competitive performance across extraction and classification tasks with substantial improvements in deployment accessibility compared to LLM-based alternatives.

## Availability

GLiNER2 is available through pip installation with pre-trained weights hosted on Hugging Face, and it is released under the Apache 2.0 license.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9d8c0df-c43c-48e9-ae24-9c8a5c53826b",
  "isSidechain": true,
  "promptId": "247674ff-ea95-46d4-ba19-340e1c5404f3",
  "agentId": "a3424ecd3141166e3",
  "type": "user",
  "uuid": "22a8fe8a-0259-404c-afd3-09fd84f8efdf",
  "sourceToolAssistantUUID": "e9d8c0df-c43c-48e9-ae24-9c8a5c53826b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T17:04:07.404Z_

<details><summary>↩ Tool result · `toolu_01GZK83uz3sdsdPSp2ez2G4F`</summary>

```text
Web search results for query: "Sclar sensitivity spurious features prompt design TACL 2024"

Links: [{"title":"[2310.11324] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/abs/2310.11324"},{"title":"Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/html/2310.11324v2"},{"title":"[PDF] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Language-Models'-Sensitivity-to-in-or:-Sclar-Choi/17a6116e5bbd8b87082cbb2e795885567300c483"},{"title":"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10520219-quantifying-language-models-sensitivity-spurious-features-prompt-design-how-learned-start-worrying-about-prompt-formatting"},{"title":"[2310.11324v2] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/abs/2310.11324v2"},{"title":"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://blog.athina.ai/quantifying-language-models-sensitivity-to-spurious-features-in-prompt-design-or-how-i-learned-to-start-worrying-about-prompt-formatting"},{"title":"How I learned to start worrying about prompt formatting","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6c0e99d736da621403018ca7b32b1a4d-Paper-Conference.pdf"},{"title":"dblp: Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting.","url":"https://dblp.org/rec/conf/iclr/Sclar0TS24.html"},{"title":"Efficient multi-prompt evaluation of LLMs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/28236482f64a72eec43706b6f3a6c511-Paper-Conference.pdf"},{"title":"Assessing and Understanding the Prompt Sensitivity of LLMs","url":"https://aclanthology.org/2024.findings-emnlp.108.pdf"}]

Based on the search results, I found information about the paper you're asking about. Here's what I found:

The paper is titled "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design" (subtitled "How I learned to start worrying about prompt formatting") by Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. However, I should note that according to the search results, this paper was published at ICLR 2024, not TACL 2024 as you mentioned.

**Key Findings:**

The researchers found that several widely used open-source LLMs are extremely sensitive to subtle changes in prompt formatting in few-shot settings, with performance differences of up to 76 accuracy points when evaluated using LLaMA-2-13B. Sensitivity remains even when increasing model size, the number of few-shot examples, or performing instruction tuning.

**Proposed Solution:**

The researchers proposed a tool called FormatSpread, which enables a systematic analysis of variances across a wide set of semantically equivalent prompt formats within a user-specified computational budget.

**Methodological Recommendations:**

The researchers suggest that work evaluating LLMs with prompting-based methods would benefit from reporting a range of performance across plausible prompt formats, instead of the currently-standard practice of reporting performance on a single format.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fc3c59d-bf91-4f2e-a8b9-339a04827408",
  "isSidechain": true,
  "promptId": "247674ff-ea95-46d4-ba19-340e1c5404f3",
  "agentId": "a3424ecd3141166e3",
  "type": "user",
  "uuid": "16cad91a-31b2-4ee8-991b-78cbfdde1162",
  "sourceToolAssistantUUID": "9fc3c59d-bf91-4f2e-a8b9-339a04827408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T17:04:07.494Z_

<details><summary>↩ Tool result · `toolu_012YhY6MmtTAMAWWkfUUcdmr`</summary>

```text
Web search results for query: "structured outputs language models benchmark 2501.10868"

Links: [{"title":"[2501.10868] JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/abs/2501.10868"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"(PDF) Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://www.researchgate.net/publication/388231978_Generating_Structured_Outputs_from_Language_Models_Benchmark_and_Studies"},{"title":"Paper page - Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://huggingface.co/papers/2501.10868"},{"title":"dblp: Generating Structured Outputs from Language Models: Benchmark and Studies.","url":"https://dblp.org/rec/journals/corr/abs-2501-10868.html"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/html/2501.10868"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2501.10868"},{"title":"StructEval: Benchmarking LLMs’ Capabilities to Generate Structural Outputs","url":"https://arxiv.org/html/2505.20139v1"},{"title":"The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models","url":"https://arxiv.org/html/2604.25359"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for LLMs | OpenReview","url":"https://openreview.net/forum?id=GDKYFegWD3"}]

I found information about arXiv paper 2501.10868. Here are the key details:

**Paper Title:** JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models

**Authors:** Saibo Geng, Hudson Cooper, Michał Moskal, Samuel Jenkins, Julian Berman, Nathan Ranchin, Robert West, Eric Horvitz, and Harsha Nori

**Main Topic:** Reliably generating structured outputs has become a critical capability for modern language model (LM) applications, and constrained decoding has emerged as the dominant technology across sectors for enforcing structured outputs during generation.

**Key Contribution:** The authors introduce JSONSchemaBench, a benchmark for constrained decoding comprising 10K real-world JSON schemas that encompass a wide range of constraints with varying complexity.

**Evaluation:** They evaluate six state-of-the-art constrained decoding frameworks, including Guidance, Outlines, Llamacpp, XGrammar, OpenAI, and Gemini. The evaluation framework assesses constrained decoding approaches across three critical dimensions: efficiency in generating constraint-compliant outputs, coverage of diverse constraint types, and quality of the generated outputs.

**Submission Date:** The paper was submitted on January 18, 2025


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2aadb37-8e9a-4140-afbd-792a379d3c01",
  "isSidechain": true,
  "promptId": "247674ff-ea95-46d4-ba19-340e1c5404f3",
  "agentId": "a3424ecd3141166e3",
  "type": "user",
  "uuid": "b5f3e05e-1d19-4a26-849e-084b4b41838f",
  "sourceToolAssistantUUID": "d2aadb37-8e9a-4140-afbd-792a379d3c01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-16T17:04:10.472Z_

Let me get more details on the GLiNER2 venue and the Sclar paper venue to confirm.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5f3e05e-1d19-4a26-849e-084b4b41838f",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
  "requestId": "req_011Cb6cMLKk1GDi4TUu9HdCd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12a9d3b4-124d-44f5-ac64-134b6339a398",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PV1x1Nf9Wi3frGv25AhPXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1153,
      "cache_creation_input_tokens": 3071,
      "cache_read_input_tokens": 14835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3071,
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

_source line 15 · 2026-05-16T17:04:10.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0187RSLk2NgfbkQJLZS9TEEp`</summary>

```json
{
  "query": "GLiNER2 EMNLP 2025 system demos ACL Anthology Zaratiana"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12a9d3b4-124d-44f5-ac64-134b6339a398",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
  "requestId": "req_011Cb6cMLKk1GDi4TUu9HdCd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "834e4e1e-d392-4334-ae92-9b412493a3eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PV1x1Nf9Wi3frGv25AhPXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1153,
      "cache_creation_input_tokens": 3071,
      "cache_read_input_tokens": 14835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3071,
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

_source line 16 · 2026-05-16T17:04:12.007Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DapvS8W2t9r59ZxtiQ8yDw`</summary>

```json
{
  "query": "Sclar \"quantifying language models sensitivity\" ICLR 2024 TACL venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "834e4e1e-d392-4334-ae92-9b412493a3eb",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
  "requestId": "req_011Cb6cMLKk1GDi4TUu9HdCd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66218193-f2ff-4a41-899f-64d75ca89e43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PV1x1Nf9Wi3frGv25AhPXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1153,
      "cache_creation_input_tokens": 3071,
      "cache_read_input_tokens": 14835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3071,
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

_source line 17 · 2026-05-16T17:04:12.339Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0124LCppwBs17M6FUVVgprFx`</summary>

```json
{
  "query": "JSONSchemaBench 2501.10868 Geng title change \"Generating Structured Outputs\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66218193-f2ff-4a41-899f-64d75ca89e43",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
  "requestId": "req_011Cb6cMLKk1GDi4TUu9HdCd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3fe2494-6c45-4081-a5ec-a35516be7391",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PV1x1Nf9Wi3frGv25AhPXj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1153,
      "cache_creation_input_tokens": 3071,
      "cache_read_input_tokens": 14835,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3071
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1153,
          "output_tokens": 216,
          "cache_read_input_tokens": 14835,
          "cache_creation_input_tokens": 3071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3071,
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

_source line 18 · 2026-05-16T17:04:16.166Z_

<details><summary>↩ Tool result · `toolu_0187RSLk2NgfbkQJLZS9TEEp`</summary>

```text
Web search results for query: "GLiNER2 EMNLP 2025 system demos ACL Anthology Zaratiana"

Links: [{"title":"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-demos.10/"},{"title":"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations - ACL Anthology","url":"https://aclanthology.org/volumes/2025.emnlp-demos/"},{"title":"GLiNER2: An Efficient Multi-Task Information Extraction ...","url":"https://aclanthology.org/2025.emnlp-demos.10.pdf"},{"title":"GitHub - fastino-ai/GLiNER2: Unified Schema-Based Information Extraction · GitHub","url":"https://github.com/fastino-ai/GLiNER2"},{"title":"EMNLP 2025 The 2025 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2025.emnlp-demos.0.pdf"},{"title":"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-demos.10@ACL"},{"title":"Accepted System Demonstrations Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/demo_papers/"},{"title":"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction","url":"https://www.researchgate.net/publication/397420183_GLiNER2_Schema-Driven_Multi-Task_Learning_for_Structured_Information_Extraction"},{"title":"Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/venues/emnlp/"},{"title":"[PDF] GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GLiNER2:-An-Efficient-Multi-Task-Information-System-Zaratiana-Pasternak/73459ec452412f2653b341d55632190aeadc1e12"}]

Based on the search results, I found detailed information about GLiNER2:

## GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction

The paper was authored by Urchade Zaratiana, Gil Pasternak, Oliver Boyd, George Hurn-Maloney, and Ash Lewis, and published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations, pages 130–140, in Suzhou, China.

GLiNER2 is a unified framework that enhances the original GLiNER architecture to support named entity recognition, text classification, and hierarchical structured data extraction within a single efficient model.

Built on a fine-tuned encoder architecture, GLiNER2 maintains CPU efficiency and compact size while introducing multi-task composition through an intuitive schema-based interface. The experiments demonstrate competitive performance across diverse IE tasks with substantial improvements in deployment accessibility compared to LLM-based alternatives.

The paper is available on the ACL Anthology at: https://aclanthology.org/2025.emnlp-demos.10/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "834e4e1e-d392-4334-ae92-9b412493a3eb",
  "isSidechain": true,
  "promptId": "247674ff-ea95-46d4-ba19-340e1c5404f3",
  "agentId": "a3424ecd3141166e3",
  "type": "user",
  "uuid": "7c30b436-6a3b-4c99-858b-8f4aea6251a6",
  "sourceToolAssistantUUID": "834e4e1e-d392-4334-ae92-9b412493a3eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T17:04:17.371Z_

<details><summary>↩ Tool result · `toolu_0124LCppwBs17M6FUVVgprFx`</summary>

```text
Web search results for query: "JSONSchemaBench 2501.10868 Geng title change "Generating Structured Outputs""

Links: [{"title":"[2501.10868] JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/abs/2501.10868"},{"title":"GitHub - guidance-ai/jsonschemabench · GitHub","url":"https://github.com/guidance-ai/jsonschemabench"},{"title":"epfl-dlab/JSONSchemaBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/epfl-dlab/JSONSchemaBench"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/html/2501.10868"},{"title":"GitHub - epfl-dlab/jsonschemabench","url":"https://github.com/epfl-dlab/jsonschemabench"},{"title":"[Literature Review] JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://www.themoonlight.io/en/review/jsonschemabench-a-rigorous-benchmark-of-structured-outputs-for-language-models"},{"title":"(PDF) Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://www.researchgate.net/publication/388231978_Generating_Structured_Outputs_from_Language_Models_Benchmark_and_Studies"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2501.10868"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250110868G/abstract"}]

Based on the search results, I found information about the JSONSchemaBench paper and the title change you're asking about.

The paper with arXiv ID 2501.10868 by Saibo Geng et al. has the title "Generating Structured Outputs from Language Models: Benchmark and Studies". However, the paper also appears as "JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models".

It appears the paper had different titles across versions. The paper was submitted on January 18, 2025 (v1) and last revised on February 27, 2025 (v3), so the title variation you're asking about likely reflects changes made during the revision process.

JSONSchemaBench is a benchmark for constrained decoding comprising 10K real-world JSON schemas, and the authors evaluated six state-of-the-art constrained decoding frameworks, including Guidance, Outlines, Llamacpp, XGrammar, OpenAI, and Gemini.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3fe2494-6c45-4081-a5ec-a35516be7391",
  "isSidechain": true,
  "promptId": "247674ff-ea95-46d4-ba19-340e1c5404f3",
  "agentId": "a3424ecd3141166e3",
  "type": "user",
  "uuid": "eec6a9c7-1e11-400c-b796-01618a14d319",
  "sourceToolAssistantUUID": "c3fe2494-6c45-4081-a5ec-a35516be7391",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T17:04:17.604Z_

<details><summary>↩ Tool result · `toolu_01DapvS8W2t9r59ZxtiQ8yDw`</summary>

```text
Web search results for query: "Sclar "quantifying language models sensitivity" ICLR 2024 TACL venue"

Links: [{"title":"ICLR Poster Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://iclr.cc/virtual/2024/poster/18650"},{"title":"[2310.11324] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/abs/2310.11324"},{"title":"dblp: Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting.","url":"https://dblp.org/rec/conf/iclr/Sclar0TS24.html"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6c0e99d736da621403018ca7b32b1a4d-Paper-Conference.pdf"},{"title":"[2310.11324v2] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/abs/2310.11324v2"},{"title":"State of What Art? A Call for Multi-Prompt LLM Evaluation | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00681/123885/State-of-What-Art-A-Call-for-Multi-Prompt-LLM"},{"title":"GitHub - SihengLi99/LLM-Honesty-Survey: [2025-TMLR] A Survey on the Honesty of Large Language Models · GitHub","url":"https://github.com/SihengLi99/LLM-Honesty-Survey"},{"title":"Published as a conference paper at ICLR 2024 CONFORMAL LANGUAGE MODELING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf"},{"title":"[PDF] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting ...","url":"https://www.semanticscholar.org/paper/Quantifying-Language-Models'-Sensitivity-to-in-or:-Sclar-Choi/17a6116e5bbd8b87082cbb2e795885567300c483"},{"title":"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting | OpenReview","url":"https://openreview.net/forum?id=RIu5lyNXjT"}]

Based on the search results, I found the paper you were asking about:

"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting" by Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr was published at ICLR 2024.

However, regarding the TACL venue mentioned in your query: The search results show that a related paper titled "State of What Art? A Call for Multi-Prompt LLM Evaluation" was published in Transactions of the Association for Computational Linguistics (TACL) in 2024, but this is a different paper. The Sclar et al. paper on quantifying language models' sensitivity was published specifically at ICLR 2024, not TACL.

The paper finds that several widely used open-source LLMs are extremely sensitive to subtle changes in prompt formatting in few-shot settings, with performance differences of up to 76 accuracy points when evaluated using LLaMA-2-13B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66218193-f2ff-4a41-899f-64d75ca89e43",
  "isSidechain": true,
  "promptId": "247674ff-ea95-46d4-ba19-340e1c5404f3",
  "agentId": "a3424ecd3141166e3",
  "type": "user",
  "uuid": "70713cc1-aa95-4c94-9013-0f2b6d4c49cb",
  "sourceToolAssistantUUID": "66218193-f2ff-4a41-899f-64d75ca89e43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T17:04:42.340Z_

Here are the verification results for all four entries:

---

### 1. gliner2-2025

**Exists:** Yes

**Bib title in question:** "GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface"

**Actual title(s):**
- arXiv version: "GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface"
- ACL Anthology (EMNLP proceedings): "GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction"

**Authors:** Urchade Zaratiana, Gil Pasternak, Oliver Boyd, George Hurn-Maloney, Ash Lewis -- correct (Zaratiana et al.)

**Venue:** EMNLP 2025 System Demonstrations -- **correct**

**Corrections needed:** The bib title is an abbreviated paraphrase. Use one of the two official titles. The ACL Anthology version ("GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction") is the canonical proceedings title.

---

### 2. sclar-sensitivity-2024

**Exists:** Yes

**Bib title in question:** "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design"

**Actual title:** "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting"

**Authors:** Melanie Sclar, Yejin Choi, Yulia Tsvetkov, Alane Suhr -- correct (Sclar et al.)

**Venue claimed:** TACL 2024 -- **INCORRECT**. The paper was published at **ICLR 2024** (confirmed by ICLR virtual site, OpenReview, dblp key `conf/iclr/Sclar0TS24`, and the PDF header "Published as a conference paper at ICLR 2024").

**Corrections needed:**
1. Venue must be changed from TACL 2024 to ICLR 2024.
2. Title is missing the subtitle ("or: How I learned to start worrying about prompt formatting"), though omitting a subtitle is a common and acceptable practice.

---

### 3. json-schema-bench-2025

**Exists:** Yes

**Bib title in question:** "Generating Structured Outputs from Language Models: Benchmark and Studies"

**Actual title:** The paper at arXiv:2501.10868 was originally titled "Generating Structured Outputs from Language Models: Benchmark and Studies" (v1) but was later revised to "JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models" (v3, Feb 2025).

**Authors:** Saibo Geng, Hudson Cooper, Michal Moskal, Samuel Jenkins, Julian Berman, Nathan Ranchin, Robert West, Eric Horvitz, Harsha Nori -- correct (Geng et al.)

**Venue:** arXiv preprint, 2025 -- correct as a preprint. The paper also appears on OpenReview, suggesting conference submission.

**Corrections needed:** The title matches v1 but is outdated. The current/canonical title is "JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models". Recommend updating the bib entry to use the latest title.

---

### 4. li2023evaluating

**Exists:** Yes

**Bib title in question:** "Evaluating ChatGPT's Information Extraction Capabilities"

**Actual title:** "Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness"

**Authors:** Bo Li, Gexiang Fang, Yang Yang, Quansen Wang, Wei Ye, Wen Zhao, Shikun Zhang -- correct (Li et al.)

**Venue:** arXiv:2304.11633, April 2023 -- **correct**

**Corrections needed:** The bib title is truncated. The full title includes the subtitle ": An Assessment of Performance, Explainability, Calibration, and Faithfulness". Recommend using the full title.

---

### Summary

| Entry | Exists | Title | Authors | Venue/Year | Action Required |
|-------|--------|-------|---------|------------|-----------------|
| gliner2-2025 | Yes | Paraphrased -- use official proceedings title | Correct | Correct (EMNLP 2025 Demos) | Fix title |
| sclar-sensitivity-2024 | Yes | Missing subtitle (minor) | Correct | **WRONG: ICLR 2024, not TACL 2024** | **Fix venue** |
| json-schema-bench-2025 | Yes | Outdated v1 title | Correct | Correct (arXiv 2025) | Update title to current revision |
| li2023evaluating | Yes | Truncated subtitle | Correct | Correct (arXiv 2023) | Optionally add full subtitle |

The only critical error is **sclar-sensitivity-2024**: the venue must be corrected from TACL to ICLR.

Sources:
- [GLiNER2 - ACL Anthology](https://aclanthology.org/2025.emnlp-demos.10/)
- [Sclar et al. - arXiv](https://arxiv.org/abs/2310.11324)
- [Sclar et al. - ICLR 2024 Poster](https://iclr.cc/virtual/2024/poster/18650)
- [Sclar et al. - dblp](https://dblp.org/rec/conf/iclr/Sclar0TS24.html)
- [JSONSchemaBench - arXiv](https://arxiv.org/abs/2501.10868)
- [Li et al. - arXiv](https://arxiv.org/abs/2304.11633)
- [Li et al. - Semantic Scholar](https://www.semanticscholar.org/paper/Evaluating-ChatGPT's-Information-Extraction-An-of-Li-Fang/88abef771472c3aa46c53d5d626a0d0c3b66e8cd)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70713cc1-aa95-4c94-9013-0f2b6d4c49cb",
  "isSidechain": true,
  "agentId": "a3424ecd3141166e3",
  "requestId": "req_011Cb6cN5FA6D13JcTYJpCUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82eb77b9-7948-4c66-9645-8e28a9df48e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b5e61f08-217d-41df-849c-35e6ac5c1049",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AazEbF922J7aDHmeGYAJM8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 799,
      "cache_creation_input_tokens": 3407,
      "cache_read_input_tokens": 17906,
      "output_tokens": 1532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3407
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 799,
          "output_tokens": 1532,
          "cache_read_input_tokens": 17906,
          "cache_creation_input_tokens": 3407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3407,
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
