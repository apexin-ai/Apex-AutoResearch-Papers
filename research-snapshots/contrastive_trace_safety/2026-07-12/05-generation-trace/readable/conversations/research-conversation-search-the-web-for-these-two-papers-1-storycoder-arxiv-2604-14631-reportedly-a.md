# Research conversation: Search the web for these two papers: 1. StoryCoder (arXiv:2604.14631) — reportedly a training-free structured intermedia

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8782099bb64677a1.jsonl`
- **Structured JSON:** [`b5ebb0d583657695dd17.json`](../../sessions/b5/b5ebb0d583657695dd17.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-12T01:59:20.914Z_

Search the web for these two papers:

1. StoryCoder (arXiv:2604.14631) — reportedly a training-free structured intermediate reasoning method for code
2. SSDE (arXiv:2605.02455) — "LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering"

For each, verify:
- Does the paper exist?
- What is the core method?
- When published?
- What benchmarks/results?

Search queries:
- "arXiv 2604.14631 StoryCoder"
- "arXiv 2605.02455 SSDE structured spec-driven engineering"
- "StoryCoder code generation 2026"

Use WebSearch. Report findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a8782099bb64677a1",
  "type": "user",
  "uuid": "8acdbf23-bb7f-4b68-9a52-48c299d947a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T01:59:20.919Z_

```json
{
  "parentUuid": "8acdbf23-bb7f-4b68-9a52-48c299d947a8",
  "isSidechain": true,
  "agentId": "a8782099bb64677a1",
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
  "uuid": "1af36dab-0bef-4f5b-85a3-209377d2a4d6",
  "timestamp": "2026-05-12T01:59:20.919Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T01:59:26.961Z_



I'll search for both papers using WebSearch. Let me first load the tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1af36dab-0bef-4f5b-85a3-209377d2a4d6",
  "isSidechain": true,
  "agentId": "a8782099bb64677a1",
  "requestId": "req_011Cawr7yDyCnUHsN9uEzDCC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c72c723-02bd-41df-8111-ae860cf02b38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZYEgzyLZBeLfMKh1gvqUT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 716,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T01:59:27.200Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01P5ox2WFgbLsweBqntrc9UH`</summary>

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
  "parentUuid": "5c72c723-02bd-41df-8111-ae860cf02b38",
  "isSidechain": true,
  "agentId": "a8782099bb64677a1",
  "requestId": "req_011Cawr7yDyCnUHsN9uEzDCC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e3f8388-a600-4bdd-bb98-0e60983c6f28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZYEgzyLZBeLfMKh1gvqUT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 8223,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 716,
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

_source line 5 · 2026-05-12T01:59:27.203Z_

<details><summary>↩ Tool result · `toolu_01P5ox2WFgbLsweBqntrc9UH`</summary>

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
  "parentUuid": "9e3f8388-a600-4bdd-bb98-0e60983c6f28",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a8782099bb64677a1",
  "type": "user",
  "uuid": "cf2ecc81-ca3d-4126-a652-bb005b4cd63f",
  "sourceToolAssistantUUID": "9e3f8388-a600-4bdd-bb98-0e60983c6f28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T01:59:37.192Z_



Now let me run all three search queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf2ecc81-ca3d-4126-a652-bb005b4cd63f",
  "isSidechain": true,
  "agentId": "a8782099bb64677a1",
  "requestId": "req_011Cawr8SKdf45ME3beGfMKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "870f0c82-b605-4f96-8130-a7e38e0bce1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Zg7TY9YizeYgCNMSoKH5S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1908,
      "cache_read_input_tokens": 8939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1908,
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

_source line 7 · 2026-05-12T01:59:37.680Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011MXWafTnmWPcZjESwqo6oz`</summary>

```json
{
  "query": "arXiv 2604.14631 StoryCoder"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "870f0c82-b605-4f96-8130-a7e38e0bce1f",
  "isSidechain": true,
  "agentId": "a8782099bb64677a1",
  "requestId": "req_011Cawr8SKdf45ME3beGfMKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03a5868c-469d-46de-8f7a-8dddddcb97a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Zg7TY9YizeYgCNMSoKH5S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1908,
      "cache_read_input_tokens": 8939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1908,
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

_source line 8 · 2026-05-12T01:59:38.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UqqW6Cp7PNUxdUqW46poqQ`</summary>

```json
{
  "query": "arXiv 2605.02455 SSDE structured spec-driven engineering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03a5868c-469d-46de-8f7a-8dddddcb97a4",
  "isSidechain": true,
  "agentId": "a8782099bb64677a1",
  "requestId": "req_011Cawr8SKdf45ME3beGfMKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d98f46e8-3e33-411c-a12a-f7d58029cadf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Zg7TY9YizeYgCNMSoKH5S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1908,
      "cache_read_input_tokens": 8939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1908,
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

_source line 9 · 2026-05-12T01:59:39.024Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WcNzfsKCESCEwz8P3TrHNG`</summary>

```json
{
  "query": "StoryCoder code generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d98f46e8-3e33-411c-a12a-f7d58029cadf",
  "isSidechain": true,
  "agentId": "a8782099bb64677a1",
  "requestId": "req_011Cawr8SKdf45ME3beGfMKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01c865b6-ba72-4153-bdbd-a1e4c69d5eb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Zg7TY9YizeYgCNMSoKH5S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1908,
      "cache_read_input_tokens": 8939,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1908
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 8939,
          "cache_creation_input_tokens": 1908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1908,
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

_source line 10 · 2026-05-12T01:59:42.443Z_

<details><summary>↩ Tool result · `toolu_011MXWafTnmWPcZjESwqo6oz`</summary>

```text
Web search results for query: "arXiv 2604.14631 StoryCoder"

Links: [{"title":"[2604.14631] StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation","url":"https://arxiv.org/abs/2604.14631"},{"title":"StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation","url":"https://arxiv.org/html/2604.14631"},{"title":"(PDF) StoryCoder: Teaching Computational Thinking Concepts Through Storytelling in a Voice-Guided App for Children","url":"https://www.researchgate.net/publication/351418072_StoryCoder_Teaching_Computational_Thinking_Concepts_Through_Storytelling_in_a_Voice-Guided_App_for_Children"},{"title":"storycoder (Joseph Margolis) · GitHub","url":"https://github.com/storycoder"},{"title":"MindScratch: A Visual Programming Support Tool for Classroom Learning Based on Multimodal Generative AI","url":"https://arxiv.org/html/2412.09001v1"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1393&show=1000"},{"title":"Explainability for Embedding AI: Aspirations and Actuality","url":"https://arxiv.org/html/2504.14631"},{"title":"arXiv:2505.14631v2 [cs.CL] 21 May 2025 Think Only When You Need","url":"https://arxiv.org/pdf/2505.14631"},{"title":"[1602.06566] Interactive Storytelling over Document Collections","url":"https://arxiv.org/abs/1602.06566"},{"title":"[2511.14631] Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities","url":"https://arxiv.org/abs/2511.14631"}]

Based on the search results, here's what I found about arXiv paper 2604.14631 on StoryCoder:

StoryCoder is a narrative reformulation framework that transforms code generation questions into coherent natural language narratives, providing richer contextual structure than simple rephrasings.

Each narrative consists of three components: a task overview, constraints, and example test cases, guided by the selected algorithm and genre. The design is based on findings from cognitive science that humans comprehend and reason more effectively when organizing fragmented conditions into coherent mental models using analogical structures.

**Results:**
Experiments across 11 models on HumanEval, LiveCodeBench, and CodeForces demonstrate consistent improvements, with an average gain of 18.7% in zero-shot pass@10.

You can access the full paper at: https://arxiv.org/abs/2604.14631


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03a5868c-469d-46de-8f7a-8dddddcb97a4",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a8782099bb64677a1",
  "type": "user",
  "uuid": "8b1a8eb5-1cee-4873-9a5f-60db48f457b3",
  "sourceToolAssistantUUID": "03a5868c-469d-46de-8f7a-8dddddcb97a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T01:59:44.892Z_

<details><summary>↩ Tool result · `toolu_01WcNzfsKCESCEwz8P3TrHNG`</summary>

```text
Web search results for query: "StoryCoder code generation 2026"

Links: [{"title":"[2604.14631] StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation","url":"https://arxiv.org/abs/2604.14631"},{"title":"StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation","url":"https://arxiv.org/html/2604.14631"},{"title":"StoryCode | Facebook","url":"https://www.facebook.com/storycodeorg/"},{"title":"StoryCode.org | LinkedIn","url":"https://www.linkedin.com/company/storycode.org"},{"title":"GitHub - roseTech/storycoder.dev: What is StoryCoder.dev? StoryCoder.dev is an open source project to which anyone can contribute. The project consists of writing stories of all genres (comedy, action, detective, love stories, drama, fairy tales, fiction, historical, etc.). Somewhere in the story there is a code to solve which can be solved in all programming languages you know!","url":"https://github.com/roseTech/storycoder.dev"},{"title":"storycoder (Joseph Margolis) · GitHub","url":"https://github.com/storycoder"},{"title":"Storycode - Crunchbase Company Profile & Funding","url":"https://www.crunchbase.com/organization/storycode"},{"title":"Coding Stories","url":"https://codingstories.io/"},{"title":"StoryCoder","url":"https://hci.stanford.edu/research/storycoder/"},{"title":"Best AI Coding Tools 2026: 7 Tested [Ranked] - Tech Insider","url":"https://tech-insider.org/ai-coding-tools-2026-transforming-software-development/"}]

Based on the search results, I found relevant information about StoryCoder related to code generation in 2026:

StoryCoder is a narrative reformulation framework that transforms code generation questions into coherent natural language narratives, providing richer contextual structure than simple rephrasings. Each narrative consists of three components: a task overview, constraints, and example test cases, guided by the selected algorithm and genre.

Experiments across 11 models on HumanEval, LiveCodeBench, and CodeForces demonstrate consistent improvements, with an average gain of 18.7% in zero-shot pass@10. Narrative reformulation guides models toward correct algorithmic strategies, reduces implementation errors, and induces a more modular code structure.

The research was submitted on April 16, 2026, making it a recent contribution to the field of LLM-based code generation. The framework appears to address a key challenge in code generation by improving how problems are represented to language models through more coherent narrative structures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01c865b6-ba72-4153-bdbd-a1e4c69d5eb9",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a8782099bb64677a1",
  "type": "user",
  "uuid": "d7da261f-80f3-4bd5-877e-acd0852b5134",
  "sourceToolAssistantUUID": "01c865b6-ba72-4153-bdbd-a1e4c69d5eb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T01:59:45.306Z_

<details><summary>↩ Tool result · `toolu_01UqqW6Cp7PNUxdUqW46poqQ`</summary>

```text
Web search results for query: "arXiv 2605.02455 SSDE structured spec-driven engineering"

Links: [{"title":"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/html/2605.02455"},{"title":"[2605.02455] LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/abs/2605.02455"},{"title":"[2605.02455v1] LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/abs/2605.02455v1"},{"title":"Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants","url":"https://arxiv.org/html/2602.00180v1"},{"title":"[2602.00180] Spec-Driven Development:From Code to Contract in the Age of AI Coding Assistants","url":"https://arxiv.org/abs/2602.00180"},{"title":"[2605.05024] Hypergraph Generation via Structured Stochastic Diffusion","url":"https://arxiv.org/abs/2605.05024"},{"title":"[2605.07475] Broken-symmetry shape discrimination on a driven Duffing ring","url":"https://arxiv.org/abs/2605.07475"},{"title":"[2602.00180v1] Spec-Driven Development:From Code to Contract in the Age of AI Coding Assistants","url":"https://arxiv.org/abs/2602.00180v1"},{"title":"Towards Specification-Driven LLM-Based Generation of Embedded Automotive Software","url":"https://arxiv.org/html/2411.13269v1"},{"title":"Paper page - Spec-Driven Development:From Code to Contract in the Age of AI Coding Assistants","url":"https://huggingface.co/papers/2602.00180"}]

Based on the search results, here's what I found about arXiv paper 2605.02455:

## Paper Overview

The paper is titled "LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering" by Shuzhao Feng, Boqi Chen, Brett H Meyer, and Gunter Mussbacher, submitted on May 4, 2026.

## Key Concept

The paper proposes structured spec-driven engineering (SSDE), a paradigm that leverages structured artifacts to guide LLM generation. Current workflows relying only on natural language prompts suffer from inherent ambiguity and a lack of verifiability.

## Problem and Solution

While state-of-the-art LLMs excel in code generation at the function level, the output quality significantly declines when scaling to repository-level systems. The authors argue that structured specifications as LLM inputs make high-quality, repository-level code generation a tangible goal, while at the same time offering superior verifiability.

## Methodology

The researchers investigated the feasibility of this vision through a pilot study generating Model-View-Controller (MVC) business logic for three software systems using five LLMs. In the study, they generated MVC systems following the SSDE workflow using Gherkin specifications and domain models as inputs.

## Findings

The study shows that, with SSDE, high-quality automated repository generation is a tangible goal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d98f46e8-3e33-411c-a12a-f7d58029cadf",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a8782099bb64677a1",
  "type": "user",
  "uuid": "3d02d543-5c49-49c6-8469-5f2ba7a3ada1",
  "sourceToolAssistantUUID": "d98f46e8-3e33-411c-a12a-f7d58029cadf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-12T01:59:54.064Z_

Now let me fetch the actual arXiv abstract pages for both papers to get more precise details (authors, exact dates, specific benchmark numbers).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d02d543-5c49-49c6-8469-5f2ba7a3ada1",
  "isSidechain": true,
  "agentId": "a8782099bb64677a1",
  "requestId": "req_011Cawr9mULmVZ6htSnydr8q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e7693b9-bda0-4b19-b7ee-0d0d85e36e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015AUzQa7sGHczQzNQ21MB6J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 1756,
      "cache_read_input_tokens": 10847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1756,
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

_source line 14 · 2026-05-12T01:59:55.720Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016QXJ1k7h2BvPZT3pDRNci6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.14631",
  "prompt": "Extract: full title, all authors, submission date, abstract, and any benchmark results or key numbers mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e7693b9-bda0-4b19-b7ee-0d0d85e36e41",
  "isSidechain": true,
  "agentId": "a8782099bb64677a1",
  "requestId": "req_011Cawr9mULmVZ6htSnydr8q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9551ce48-dded-46a5-9f93-afe9a50208e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015AUzQa7sGHczQzNQ21MB6J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 1756,
      "cache_read_input_tokens": 10847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1756,
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

_source line 15 · 2026-05-12T01:59:56.099Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G5tj9rkC54GgT66gxM55kf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.02455",
  "prompt": "Extract: full title, all authors, submission date, abstract, and any benchmark results or key numbers mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9551ce48-dded-46a5-9f93-afe9a50208e6",
  "isSidechain": true,
  "agentId": "a8782099bb64677a1",
  "requestId": "req_011Cawr9mULmVZ6htSnydr8q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a2ed546-dc06-424a-ada7-e47f779f127d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015AUzQa7sGHczQzNQ21MB6J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 1756,
      "cache_read_input_tokens": 10847,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1756
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 701,
          "output_tokens": 219,
          "cache_read_input_tokens": 10847,
          "cache_creation_input_tokens": 1756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1756,
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

_source line 16 · 2026-05-12T01:59:59.832Z_

<details><summary>↩ Tool result · `toolu_016QXJ1k7h2BvPZT3pDRNci6`</summary>

```text
# StoryCoder Paper Summary

**Full Title:**
StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation

**Authors:**
- Geonhui Jang
- Dongyoon Han
- YoungJoon Yoo

**Submission Date:**
April 16, 2026

**Abstract:**
The researchers introduce a framework that converts code generation problems into coherent natural language narratives containing three elements: task overview, constraints, and example test cases. This approach aims to help language models reason more effectively about programming tasks.

**Key Benchmark Results:**
- Tested across 11 models on HumanEval, LiveCodeBench, and CodeForces
- "average gain of 18.7% in zero-shot pass@10"
- The method demonstrated consistent improvements across different model scales and architectures
- Analysis showed that narrative reformulation "guides models toward correct algorithmic strategies, reduces implementation errors, and induces a more modular code structure"

**Publication:**
ACL 2026 Main Conference (21 pages, 12 figures)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9551ce48-dded-46a5-9f93-afe9a50208e6",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a8782099bb64677a1",
  "type": "user",
  "uuid": "5a81a30b-f448-4401-ab51-af71b6d84389",
  "sourceToolAssistantUUID": "9551ce48-dded-46a5-9f93-afe9a50208e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T02:00:00.679Z_

<details><summary>↩ Tool result · `toolu_01G5tj9rkC54GgT66gxM55kf`</summary>

```text
# Paper Summary

**Full Title:** LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering

**Authors:** Shuzhao Feng, Boqi Chen, Brett H Meyer, Gunter Mussbacher

**Submission Date:** May 4, 2026

**Abstract:**
The paper proposes structured spec-driven engineering (SSDE), a paradigm addressing limitations in LLM code generation at scale. The authors note that while "Large Language Models (LLMs) excel in code generation at the function level," output quality deteriorates for repository-level systems. They argue that structured specifications improve generation quality and verifiability compared to natural language prompts alone. The research includes a pilot study generating Model-View-Controller business logic across three software systems using five LLMs.

**Key Numbers/Benchmarks:**
- Study scope: Three software systems
- LLMs evaluated: Five different models
- Accepted to: 34th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (FSE Companion '26)

**Note:** The paper presents research findings rather than specific quantitative benchmark results in the abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a2ed546-dc06-424a-ada7-e47f779f127d",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a8782099bb64677a1",
  "type": "user",
  "uuid": "9d0da955-0add-4f6d-ac51-62fd4be454ab",
  "sourceToolAssistantUUID": "4a2ed546-dc06-424a-ada7-e47f779f127d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-12T02:00:19.909Z_

Here are the findings for both papers.

---

## Paper 1: StoryCoder (arXiv:2604.14631)

**Exists:** Yes, confirmed on arXiv.

**Full title:** "StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation"

**Authors:** Geonhui Jang, Dongyoon Han, YoungJoon Yoo

**Published:** April 16, 2026 (accepted to ACL 2026 Main Conference; 21 pages, 12 figures)

**Core method:** StoryCoder is a training-free framework that reformulates code generation problems into coherent natural language narratives. Each narrative has three components: (1) a task overview, (2) constraints, and (3) example test cases, guided by a selected algorithm and genre. The design draws on cognitive science findings that humans reason more effectively when organizing fragmented conditions into coherent mental models via analogical structures. Notably, it requires no model fine-tuning -- it operates purely at the prompt/input level.

**Benchmarks and results:**
- Evaluated across **11 models** on **HumanEval**, **LiveCodeBench**, and **CodeForces**
- Achieved an **average gain of 18.7% in zero-shot pass@10**
- Consistent improvements across different model scales and architectures
- Analysis showed narrative reformulation guides models toward correct algorithmic strategies, reduces implementation errors, and induces more modular code structure

---

## Paper 2: SSDE (arXiv:2605.02455)

**Exists:** Yes, confirmed on arXiv.

**Full title:** "LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering"

**Authors:** Shuzhao Feng, Boqi Chen, Brett H Meyer, Gunter Mussbacher

**Published:** May 4, 2026 (accepted to the 34th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering -- FSE Companion '26)

**Core method:** SSDE (Structured Spec-Driven Engineering) is a paradigm that uses structured artifacts (specifically Gherkin specifications and domain models) as inputs to guide LLM code generation at the repository level. The key insight is that natural language prompts alone are inherently ambiguous and lack verifiability, whereas structured specifications provide both higher quality generation and superior verifiability. The approach targets Model-View-Controller (MVC) business logic generation.

**Benchmarks and results:**
- Pilot study generating MVC business logic for **3 software systems** using **5 LLMs**
- The study is more qualitative/feasibility-oriented than benchmark-driven
- Demonstrates that high-quality automated repository-level generation is a "tangible goal" with SSDE
- No specific quantitative benchmark numbers (e.g., pass@k) are reported in the abstract; the contribution is more about establishing the SSDE paradigm and demonstrating its feasibility

---

## Summary comparison

| Aspect | StoryCoder | SSDE |
|---|---|---|
| Scope | Function-level code generation | Repository-level code generation |
| Approach | Narrative reformulation of prompts (training-free) | Structured specifications (Gherkin + domain models) |
| Venue | ACL 2026 | FSE Companion '26 |
| Quantitative results | 18.7% avg. gain on pass@10 across 11 models | Feasibility study across 3 systems, 5 LLMs |
| Key novelty | Cognitive-science-inspired narrative structure | Spec-driven engineering for repo-level generation |

Both papers are real, published in 2026, and address structured intermediate representations for LLM code generation -- but at very different scales (function-level vs. repository-level).

Sources:
- [StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation](https://arxiv.org/abs/2604.14631)
- [StoryCoder (HTML version)](https://arxiv.org/html/2604.14631)
- [LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering](https://arxiv.org/abs/2605.02455)
- [SSDE (HTML version)](https://arxiv.org/html/2605.02455)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d0da955-0add-4f6d-ac51-62fd4be454ab",
  "isSidechain": true,
  "agentId": "a8782099bb64677a1",
  "requestId": "req_011CawrAuAEGzLoxuf1tUb8J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da77c680-97ad-4d8c-b69f-db9769709593",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018M9y8ikGGdZdWysgD3Dimf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1483,
      "cache_read_input_tokens": 12603,
      "output_tokens": 1024,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1483
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1024,
          "cache_read_input_tokens": 12603,
          "cache_creation_input_tokens": 1483,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1483,
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
