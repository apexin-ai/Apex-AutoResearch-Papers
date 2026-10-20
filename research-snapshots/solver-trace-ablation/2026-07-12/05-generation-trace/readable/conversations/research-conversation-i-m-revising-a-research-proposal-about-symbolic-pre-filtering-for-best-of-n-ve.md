# Research conversation: I'm revising a research proposal about symbolic pre-filtering for best-of-N verification in mathematical reasoning. A re

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a40596f27d93c653d.jsonl`
- **Structured JSON:** [`6f261243ddf845af28f6.json`](../../sessions/6f/6f261243ddf845af28f6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

68 recorded events

### User

_source line 1 · 2026-05-10T18:09:31.551Z_

I'm revising a research proposal about symbolic pre-filtering for best-of-N verification in mathematical reasoning. A reviewer pointed out I'm missing T3RL (arXiv 2603.02203, March 2026), which compiles reasoning traces into executable Python code for verification.

Please do the following:
1. Use WebSearch to find T3RL (arXiv 2603.02203) and any related work on code-execution-based verification for test-time scaling
2. Use WebFetch to read the T3RL paper abstract and method section from its arXiv page
3. Search for "code execution verification best-of-N mathematical reasoning 2025 2026" to find other related works
4. Search for "PAL program-aided language models" and "ToRA tool-integrated reasoning" to understand the foundational code-execution works

For each paper found, report:
- Title, venue, date
- Core method (2-3 sentences)
- How it relates to using symbolic/code verification in best-of-N selection
- Key results (accuracy numbers on MATH/AIME if available)

Be thorough - I need to understand the full landscape of code-execution-based verification approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "28e1beae-b867-4194-83c8-e23dd6dbb473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:09:31.554Z_

```json
{
  "parentUuid": "28e1beae-b867-4194-83c8-e23dd6dbb473",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
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
  "uuid": "ec423fac-efa4-4d1e-a765-9e8891a3d50e",
  "timestamp": "2026-05-10T18:09:31.554Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:09:34.549Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then conduct the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec423fac-efa4-4d1e-a765-9e8891a3d50e",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLV6QQPHYdjXhUQGLDF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8762da8-a26e-4528-aa07-6f07dec2516e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jkJWRbUNHbeFxWgJuK2LC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9041,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9041,
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

_source line 4 · 2026-05-10T18:09:34.860Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DQWfL3WrAVDDHkN2AHU18y`</summary>

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
  "parentUuid": "f8762da8-a26e-4528-aa07-6f07dec2516e",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLV6QQPHYdjXhUQGLDF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6613ddc2-bacd-4741-ab0e-b33d114317ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jkJWRbUNHbeFxWgJuK2LC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9041,
      "cache_read_input_tokens": 0,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9041
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9041,
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

_source line 5 · 2026-05-10T18:09:34.868Z_

<details><summary>↩ Tool result · `toolu_01DQWfL3WrAVDDHkN2AHU18y`</summary>

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
  "parentUuid": "6613ddc2-bacd-4741-ab0e-b33d114317ba",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "676d10ee-36d7-4c10-96a3-2185e5018906",
  "sourceToolAssistantUUID": "6613ddc2-bacd-4741-ab0e-b33d114317ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:09:39.324Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "676d10ee-36d7-4c10-96a3-2185e5018906",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLVM3iJuuEu7G6hj5dU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa2d3bca-013b-41fa-92d9-e6d5c2a7c904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QKAqjfEuRrHHw8415YcZb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 7 · 2026-05-10T18:09:40.318Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HHvYeTHJXkcaoZLpigyW8E`</summary>

```json
{
  "query": "T3RL arXiv 2603.02203 code execution verification reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa2d3bca-013b-41fa-92d9-e6d5c2a7c904",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLVM3iJuuEu7G6hj5dU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e47b48fa-ff1c-4e96-8c69-c1a1e1c243db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QKAqjfEuRrHHw8415YcZb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 8 · 2026-05-10T18:09:41.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RBmeuYNdk229S5eHUiikh4`</summary>

```json
{
  "query": "code execution verification best-of-N mathematical reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e47b48fa-ff1c-4e96-8c69-c1a1e1c243db",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLVM3iJuuEu7G6hj5dU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8423a1c4-7039-4ca6-925a-e477295171b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QKAqjfEuRrHHw8415YcZb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 9 · 2026-05-10T18:09:41.700Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017GVhTif6T7TwKta1guo9cC`</summary>

```json
{
  "query": "PAL program-aided language models verification mathematical reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8423a1c4-7039-4ca6-925a-e477295171b5",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLVM3iJuuEu7G6hj5dU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a32851a-459a-45f9-bc6f-94d82783047f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QKAqjfEuRrHHw8415YcZb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 10 · 2026-05-10T18:09:42.156Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0181YSgmVijLZHFKxxNmoJ7K`</summary>

```json
{
  "query": "ToRA tool-integrated reasoning mathematical problem solving"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a32851a-459a-45f9-bc6f-94d82783047f",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLVM3iJuuEu7G6hj5dU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a2219cf-6b20-4d7c-8286-341d6d88220f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QKAqjfEuRrHHw8415YcZb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9041,
      "output_tokens": 218,
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
          "output_tokens": 218,
          "cache_read_input_tokens": 9041,
          "cache_creation_input_tokens": 1912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1912,
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

_source line 11 · 2026-05-10T18:09:48.593Z_

<details><summary>↩ Tool result · `toolu_0181YSgmVijLZHFKxxNmoJ7K`</summary>

```text
Web search results for query: "ToRA tool-integrated reasoning mathematical problem solving"

Links: [{"title":"ToRA: Tool-Integrated Reasoning Agents","url":"https://microsoft.github.io/ToRA/"},{"title":"[2309.17452] ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving","url":"https://arxiv.org/abs/2309.17452"},{"title":"GitHub - microsoft/ToRA: ToRA is a series of Tool-integrated Reasoning LLM Agents designed to solve challenging mathematical reasoning problems by interacting with tools [ICLR'24]. · GitHub","url":"https://github.com/microsoft/ToRA"},{"title":"ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving | OpenReview","url":"https://openreview.net/forum?id=Ep0TtjVoap"},{"title":"\\logo ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving","url":"https://arxiv.org/html/2309.17452v4"},{"title":"[2309.17452v1] ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving","url":"https://arxiv.org/abs/2309.17452v1"},{"title":"ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230917452G/abstract"},{"title":"[2309.17452v4] ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving","url":"http://arxiv.org/abs/2309.17452v4"},{"title":"[2309.17452v2] ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving","url":"https://arxiv.org/abs/2309.17452v2"},{"title":"ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving | by Rama Jha | Medium","url":"https://ramajha.medium.com/tora-a-tool-integrated-reasoning-agent-for-mathematical-problem-solving-5736cdc71b44"}]

Based on the search results, here's comprehensive information about ToRA:

## Overview

ToRA is a series of Tool-integrated Reasoning Agents designed to solve challenging mathematical reasoning problems by interacting with tools, e.g., computation libraries and symbolic solvers.

## Core Approach

ToRA adopts a tool-integrated reasoning format that interweaves natural language reasoning with program-based tool use. This format effectively combines the advantages of semantic analysis, planning, and abstract reasoning in language reasoning with the precise calculation, symbolic operation, and efficient algorithm execution of tool use, thereby effectively addressing the challenges of complex mathematical reasoning tasks.

## Training Methodology

To train ToRA, researchers curate interactive tool-use trajectories on mathematical datasets, apply imitation learning on the annotations, and propose output space shaping to further refine models' reasoning behavior.

## Performance

ToRA models significantly outperform open-source models on 10 mathematical reasoning datasets across all scales with 13%-19% absolute improvements on average. Notable achievements include:

- ToRA-7B reaches 44.6% on the competition-level dataset MATH, surpassing the best open-source model WizardMath-70B by 22% absolute.
- ToRA-Code-34B is also the first open-source model that achieves an accuracy exceeding 50% on MATH, which significantly outperforms GPT-4's CoT result, and is competitive with GPT-4 solving problems with programs.

## Advantages

ToRA achieves fast zero-shot inference, averaging 1.02 tool interaction rounds per problem, maintaining high efficiency with one round of interaction for most problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a2219cf-6b20-4d7c-8286-341d6d88220f",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "b52a8d88-8966-429d-9c10-a48052a0649f",
  "sourceToolAssistantUUID": "3a2219cf-6b20-4d7c-8286-341d6d88220f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:09:48.636Z_

<details><summary>↩ Tool result · `toolu_01RBmeuYNdk229S5eHUiikh4`</summary>

```text
Web search results for query: "code execution verification best-of-N mathematical reasoning 2025 2026"

Links: [{"title":"5 Best AI Reasoning Models of 2026: Ranked!","url":"https://www.labellerr.com/blog/compare-reasoning-models/"},{"title":"Code2Math: Can Your Code Agent Effectively Evolve Math Problems Through","url":"https://arxiv.org/pdf/2603.03202"},{"title":"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/pdf/2511.18760"},{"title":"Position: Formal Mathematical Reasoning—A New Frontier in AI | OpenReview","url":"https://openreview.net/forum?id=HuvAM5x2xG"},{"title":"Top 10 Open-source Reasoning Models in 2026","url":"https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026"},{"title":"MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning | OpenReview","url":"https://openreview.net/forum?id=z8TW0ttBPp"},{"title":"A Survey on Code-Enhanced Reasoning and ...","url":"https://aclanthology.org/2025.emnlp-main.130.pdf"},{"title":"Ultimate Guide - The Best LLMs for Reasoning Tasks in 2026","url":"https://www.siliconflow.com/articles/en/best-LLMs-for-reasoning-tasks"},{"title":"A Survey on LLM Symbolic Reasoning","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/295282/preprint_pdf/17368bd9e5235ed8466977226241d74d.pdf"},{"title":"Olympiad-level formal mathematical reasoning with reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09833-y"}]

I found several relevant results for your search on code execution verification, best-of-N approaches, and mathematical reasoning in 2025-2026. Here are the key findings:

## Mathematical Reasoning Models (2025-2026)

Leading AI models for reasoning include OpenAI o3, Gemini 2.5, Claude 3.7 Sonnet, Grok 3, DeepSeek‑R1, and AM‑Thinking‑v1. OpenAI's O3 uses external tools like web search, file analysis, and Python code execution.

## Code-Enhanced Reasoning

GPT-4 Code Interpreter has demonstrated remarkable proficiency in solving challenging math problems, primarily attributed to its ability to seamlessly reason with natural language, generate code, execute code, and continue reasoning based on the execution output.

Performance comparisons of code-aided reasoning methods exist across benchmarks including GSM8K, SVAMP, and MATH.

## Verification and Symbolic Execution

There is a shift from merely plausible reasoning traces to verifiable pipelines, where symbolic execution ensures correctness and consistency. HybridProver combines whole-proof synthesis and tactic-based generation through proof sketch refinement, achieving state-of-the-art theorem proving in Isabelle/HOL.

## Test-Time Methods

AlphaProof uses test-time RL, a method of generating and learning from millions of related problem variants at inference time to enable deep, problem-specific adaptation.

The search results show significant progress in combining code execution with mathematical reasoning and verification approaches in 2025-2026, though specific literature on "best-of-N" methods appears limited in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8423a1c4-7039-4ca6-925a-e477295171b5",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "5436c62a-4994-4d26-af98-4b173791d909",
  "sourceToolAssistantUUID": "8423a1c4-7039-4ca6-925a-e477295171b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T18:09:50.253Z_

<details><summary>↩ Tool result · `toolu_017GVhTif6T7TwKta1guo9cC`</summary>

```text
Web search results for query: "PAL program-aided language models verification mathematical reasoning"

Links: [{"title":"[2211.10435] PAL: Program-aided Language Models","url":"https://arxiv.org/abs/2211.10435"},{"title":"PAL: Program-aided Language Models","url":"https://arxiv.org/pdf/2211.10435"},{"title":"PAL: Program-aided Language Models","url":"https://reasonwithpal.com/"},{"title":"PAL: program-aided language models","url":"https://dl.acm.org/doi/10.5555/3618408.3618843"},{"title":"GitHub - reasoning-machines/pal: PaL: Program-Aided Language Models (ICML 2023) · GitHub","url":"https://github.com/reasoning-machines/pal"},{"title":"Program-Aided Language Models (PAL)","url":"https://www.emergentmind.com/topics/program-aided-language-models-pal"},{"title":"[2211.10435] PAL: Program-aided Language Models","url":"https://ar5iv.labs.arxiv.org/html/2211.10435"},{"title":"PAL (Program-Aided Language Models) | Prompt Engineering Guide&lt;!-- -->","url":"https://www.promptingguide.ai/techniques/pal"},{"title":"(PDF) PAL: Program-aided Language Models","url":"https://www.researchgate.net/publication/365614638_PAL_Program-aided_Language_Models"},{"title":"PAL: Program-aided Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10479607-pal-program-aided-language-models"}]

## Search Results for PAL: Program-Aided Language Models

Here's a comprehensive overview of what I found about PAL and its approach to mathematical reasoning verification:

### What is PAL?

PAL (Program-Aided Language models) is a new method that uses the LLM to read natural language problems and generate programs as the intermediate reasoning steps, but offloads the solution step to a programmatic runtime such as a Python interpreter.

### The Core Problem It Solves

While LLMs seem to be adept at step-by-step decomposition, LLMs often make logical and arithmetic mistakes in the solution part, even when the problem is decomposed correctly. PAL addresses this by having the LLM focus on problem decomposition while delegating actual computation to a symbolic executor.

### How PAL Works

The canonical steps are: the LLM is presented with few-shot exemplars demonstrating code with comments elucidating logic; given a new query, the LLM emits a program whose structure mirrors the exemplars; and the synthesized program is executed in a standard interpreter (e.g., Python) and the output is taken as the answer.

### Performance on Mathematical Reasoning

PAL using CODEX achieves state-of-the-art few-shot accuracy on GSM8K, surpassing PaLM-540B which uses chain-of-thought by absolute 15% top-1. On GSM8K (grade-school math), PAL with Codex achieves 72.0% top-1 accuracy, and on GSM-Hard, PAL remains robust (61.2%) where CoT degrades severely.

### Broader Applicability

PAL has been demonstrated across 12 reasoning tasks from BIG-Bench Hard and other benchmarks, including mathematical reasoning, symbolic reasoning, and algorithmic problems, and generating code using an LLM and reasoning using a Python interpreter leads to more accurate results than much larger models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a32851a-459a-45f9-bc6f-94d82783047f",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "8044d966-5d48-4b91-9b97-c172aaa80124",
  "sourceToolAssistantUUID": "8a32851a-459a-45f9-bc6f-94d82783047f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:09:52.811Z_

<details><summary>↩ Tool result · `toolu_01HHvYeTHJXkcaoZLpigyW8E`</summary>

```text
Web search results for query: "T3RL arXiv 2603.02203 code execution verification reasoning"

Links: [{"title":"[2603.02203] Tool Verification for Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2603.02203"},{"title":"Tool Verification for Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2603.02203"},{"title":"Paper page - Tool Verification for Test-Time Reinforcement Learning","url":"https://huggingface.co/papers/2603.02203"},{"title":"Code2Math: Can Your Code Agent Effectively Evolve Math Problems Through Exploration?","url":"https://arxiv.org/html/2603.03202"},{"title":"Agentic Code Reasoning","url":"https://arxiv.org/html/2603.01896v1"},{"title":"[2603.01896v2] Agentic Code Reasoning","url":"https://arxiv.org/abs/2603.01896v2"},{"title":"ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning","url":"https://arxiv.org/html/2603.11226"},{"title":"[2603.11226] ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning","url":"https://arxiv.org/abs/2603.11226"},{"title":"[2603.02961] Delegation and Verification Under AI","url":"https://arxiv.org/abs/2603.02961"},{"title":"[2603.01896] Agentic Code Reasoning","url":"https://arxiv.org/abs/2603.01896"}]

I found the paper you're searching for! Here's what the research is about:

**T³RL (Tool-Verification for Test-Time Reinforcement Learning)**

T³RL introduces test-time tool verification into reward estimation, where a verifier uses an external tool as evidence (e.g., from code execution) to upweight verified rollouts in a verification-aware voting, producing more reliable pseudo-labels for training.

**The Problem It Addresses:**

Test-time reinforcement learning has emerged as a paradigm for self-evolving large reasoning models, but a spurious yet high-frequency unverified consensus can become a biased and reinforced reward signal, leading to incorrect mode collapse.

**How It Works:**

An LLM verifier parses each sampled rollout to examine the returned execution result, and the verifier compiles the rollout's claimed computations into lightweight Python and queries a code interpreter to obtain executable evidence.

**Key Results:**

Across various math difficulties (MATH-500, AMC, and AIME 2024) and diverse backbone types, T³RL significantly improves over TTRL, with larger gains on harder problems.

The paper was published on arXiv on March 2, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e47b48fa-ff1c-4e96-8c69-c1a1e1c243db",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "6d32ad73-8c21-4700-acab-5b4f8ec18756",
  "sourceToolAssistantUUID": "e47b48fa-ff1c-4e96-8c69-c1a1e1c243db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T18:09:56.061Z_

Good, I have initial results. Now let me fetch the T3RL paper details and search for more related works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d32ad73-8c21-4700-acab-5b4f8ec18756",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLWfJMCVvH2heYKv445",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca6e4239-ae0a-4af3-b2a0-4df8426e991b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dg4JmNsxDk84bY5uAXiNK8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2717,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 966,
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

_source line 16 · 2026-05-10T18:09:58.953Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VewTkmvTJi95ZF7SMnYGMV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.02203",
  "prompt": "Extract the full title, all authors, the complete abstract, and the method section or introduction describing the core approach of T3RL. Include any specific accuracy numbers reported on MATH-500, AMC, AIME benchmarks. Also extract any discussion of best-of-N, majority voting, or verification-aware voting."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca6e4239-ae0a-4af3-b2a0-4df8426e991b",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLWfJMCVvH2heYKv445",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34a8dd57-f16c-41f2-95f9-439213dcb230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dg4JmNsxDk84bY5uAXiNK8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2717,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 966,
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

_source line 17 · 2026-05-10T18:09:59.899Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DZ9utBMRiQLVJuqTqAw5kK`</summary>

```json
{
  "query": "HERMES verifiable mathematical reasoning code execution verification arXiv 2511.18760"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34a8dd57-f16c-41f2-95f9-439213dcb230",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLWfJMCVvH2heYKv445",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b7d01c6-e933-4e3b-8043-1d17b60e7778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dg4JmNsxDk84bY5uAXiNK8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2717,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 966,
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

_source line 18 · 2026-05-10T18:10:00.878Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DdnezM58BCQ1TqghmtzNxY`</summary>

```json
{
  "query": "MathCoder code integration LLM mathematical reasoning verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b7d01c6-e933-4e3b-8043-1d17b60e7778",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLWfJMCVvH2heYKv445",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99557448-2098-4fc1-ab6f-43b603fad262",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dg4JmNsxDk84bY5uAXiNK8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2717,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 10953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 966,
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

_source line 19 · 2026-05-10T18:10:01.343Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PYYzgqmoAd77ADK4HEWGcZ`</summary>

```json
{
  "query": "test-time compute scaling verification mathematical reasoning best-of-N 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99557448-2098-4fc1-ab6f-43b603fad262",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLWfJMCVvH2heYKv445",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6045c8a5-ab55-43ba-909d-e06db8cbf744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dg4JmNsxDk84bY5uAXiNK8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2717,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 10953,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 966
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2717,
          "output_tokens": 325,
          "cache_read_input_tokens": 10953,
          "cache_creation_input_tokens": 966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 966,
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

_source line 20 · 2026-05-10T18:10:04.954Z_

<details><summary>↩ Tool result · `toolu_01VewTkmvTJi95ZF7SMnYGMV`</summary>

```text
# T³RL: Tool Verification for Test-Time Reinforcement Learning

## Full Title
"Tool Verification for Test-Time Reinforcement Learning"

## Authors
Ruotong Liao, Nikolai Röhrich, Xiaohan Wang, Yuhui Zhang, Yasaman Samadzadeh, Volker Tresp, Serena Yeung-Levy

## Abstract
The paper addresses a critical failure mode in test-time reinforcement learning where "spurious yet high-frequency unverified consensus can become a biased" signal. T³RL introduces external tool verification into reward estimation, using a verifier to "upweight verified rollouts in a verification-aware voting" mechanism. The approach produces more dependable pseudo-labels across mathematical problem sets including MATH-500, AMC, and AIME 2024, with "larger gains on harder problems."

## Core Approach
The method implements "verified online data synthesis" by incorporating test-time tool verification. Rather than relying on simple majority voting consensus, the system uses external tools (such as code execution) as evidence to validate rollouts. This verification-aware approach distinguishes correct solutions from spurious high-frequency incorrect ones, creating a more stable self-evolution mechanism for reasoning models.

## Specific Performance Numbers
The document abstract references improvements "across various math difficulties (MATH-500, AMC, and AIME 2024)" but does not provide exact numerical accuracy improvements in the accessible content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34a8dd57-f16c-41f2-95f9-439213dcb230",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "e550d835-1fbc-41d6-ab36-f7bb1437df7a",
  "sourceToolAssistantUUID": "34a8dd57-f16c-41f2-95f9-439213dcb230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T18:10:06.276Z_

<details><summary>↩ Tool result · `toolu_01DdnezM58BCQ1TqghmtzNxY`</summary>

```text
Web search results for query: "MathCoder code integration LLM mathematical reasoning verification"

Links: [{"title":"GitHub - mathllm/MathCoder: [MathCoder, MathCoder-VL] Family of LLMs/LMMs for mathematical reasoning. · GitHub","url":"https://github.com/mathllm/MathCoder"},{"title":"[2310.03731] MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning","url":"https://arxiv.org/abs/2310.03731"},{"title":"[2310.03731] MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning","url":"https://ar5iv.labs.arxiv.org/html/2310.03731"},{"title":"Paper page - MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning","url":"https://huggingface.co/papers/2310.03731"},{"title":"[PDF] MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MathCoder:-Seamless-Code-Integration-in-LLMs-for-Wang-Ren/cddb552f6c3464a54a02b0b64b2d1af56c086606"},{"title":"MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning | OpenReview","url":"https://openreview.net/forum?id=z8TW0ttBPp"},{"title":"MATHCODER: SEAMLESS CODE INTEGRATION IN LLMS ...","url":"https://openreview.net/pdf?id=z8TW0ttBPp"},{"title":"Papers Explained Review 12: LLMs for Maths | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-review-12-llms-for-maths-1597e3c7251c"},{"title":"MathLLMs/MathCoder-L-7B · Hugging Face","url":"https://huggingface.co/MathLLMs/MathCoder-L-7B"},{"title":"MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning - CityUHK Scholars","url":"https://scholars.cityu.edu.hk/en/publications/mathcoder(556df54e-c210-4e0c-91ce-db2e0e78ea99).html"}]

Based on the search results, here's what I found about MathCoder:

## Overview

MathCoder is titled "Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning", and it is a family of LLMs/LMMs for mathematical reasoning.

## Key Approach

The method fine-tunes open-source language models, enabling them to use code for modeling and deriving math equations and, consequently, enhancing their mathematical reasoning abilities. The approach is inspired by the GPT-4 Code Interpreter's ability to seamlessly reason with natural language, generate code, execute code, and continue reasoning based on the execution output.

## Dataset and Training

MathCoder proposes generating novel and high-quality datasets with math problems and their code-based solutions, referred to as MathCodeInstruct, where each solution interleaves natural language, code, and execution results. The first step involves collecting GPT-4 Code Interpreter-style solutions for the GSM8K and MATH training sets, which consist of grade school math word problems and challenging competition mathematics problems, respectively.

## Results

The MathCoder model not only surpasses ChatGPT-3.5 and PaLM-2 on GSM8K and MATH but also outperforms GPT-4 on the competition-level MATH dataset. The project has released MathCoder-VL to bridge vision and code for enhanced multimodal mathematical reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99557448-2098-4fc1-ab6f-43b603fad262",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "b804d9ba-dd4e-4cc7-9251-7da0cf8017ae",
  "sourceToolAssistantUUID": "99557448-2098-4fc1-ab6f-43b603fad262",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T18:10:06.325Z_

<details><summary>↩ Tool result · `toolu_01DZ9utBMRiQLVJuqTqAw5kK`</summary>

```text
Web search results for query: "HERMES verifiable mathematical reasoning code execution verification arXiv 2511.18760"

Links: [{"title":"[2511.18760] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/abs/2511.18760"},{"title":"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/pdf/2511.18760"},{"title":"[2511.18760v1] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/abs/2511.18760v1"},{"title":"(PDF) HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://www.researchgate.net/publication/397933683_HERMES_Towards_Efficient_and_Verifiable_Mathematical_Reasoning_in_LLMs"},{"title":"Hermes: Verified Math Reasoning for LLMs - YouTube","url":"https://www.youtube.com/watch?v=LHbloXgSd-c"},{"title":"[2511.22570v1] DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning","url":"https://arxiv.org/abs/2511.22570v1"},{"title":"[2511.22570] DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning","url":"https://arxiv.org/abs/2511.22570"},{"title":"Self-Verifiable Mathematical Reasoning","url":"https://www.emergentmind.com/topics/self-verifiable-mathematical-reasoning"},{"title":"Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning","url":"https://arxiv.org/html/2502.13820v3"},{"title":"SymCode: A Neurosymbolic Approach to Mathematical Reasoning via","url":"https://arxiv.org/pdf/2510.25975"}]

Based on the search results, here's what I found about HERMES (arXiv 2511.18760):

## Overview

HERMES is the first tool-assisted agent that explicitly interleaves informal reasoning with formally verified proof steps in Lean.

## Problem Statement

Informal mathematics has been central to modern LLM reasoning, offering flexibility and enabling efficient construction of arguments. However, purely informal reasoning is prone to logical gaps and subtle errors that are difficult to detect and correct. In contrast, formal theorem proving provides rigorous, verifiable mathematical reasoning, where each inference step is checked by a trusted compiler in systems such as Lean, but lacks the exploratory freedom of informal problem solving.

## Key Features

The framework performs intermediate formal checking to prevent reasoning drift and employs a memory module that maintains proof continuity across long, multi-step reasoning chains.

## Authors and Details

The paper was submitted on November 24, 2025, with authors including Azim Ospanov, Zijin Feng, Jiacheng Sun, Haoli Bai, Xin Shen, and Farzan Farnia. The paper addresses the fundamental mismatch between informal and formal mathematical reasoning in LLMs by combining the exploratory strengths of informal reasoning with the rigor of formal verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b7d01c6-e933-4e3b-8043-1d17b60e7778",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "9695a271-8540-403c-b4db-6e855cd428e6",
  "sourceToolAssistantUUID": "2b7d01c6-e933-4e3b-8043-1d17b60e7778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T18:10:16.984Z_

<details><summary>↩ Tool result · `toolu_01PYYzgqmoAd77ADK4HEWGcZ`</summary>

```text
Web search results for query: "test-time compute scaling verification mathematical reasoning best-of-N 2025"

Links: [{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models","url":"https://testtimescaling.github.io/"},{"title":"ICLR 2025 Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning Oral","url":"https://iclr.cc/virtual/2025/oral/31924"},{"title":"Track: Oral Session 1A","url":"https://iclr.cc/virtual/2025/session/31935"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/html/2512.02008v1"},{"title":"Tutorial: Test-Time Scaling for Mathematical Reasoning Sean Welleck","url":"https://wellecks.com/data/welleck2025scifm_tutorial.pdf"},{"title":"Scaling Test-time Compute for LLM Agents","url":"https://arxiv.org/html/2506.12928v1"},{"title":"inference scaling laws: an empirical analysis of compute- ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf"},{"title":"Revisiting the Test-Time Scaling of o1-like Models","url":"https://aclanthology.org/2025.acl-long.232.pdf"}]

Based on the search results, here's what I found about test-time compute scaling, verification, mathematical reasoning, and best-of-N approaches in 2025:

## Key Findings on Test-Time Compute Scaling for Mathematical Reasoning

### Compute-Optimal Scaling Strategy
A compute-optimal strategy can improve the efficiency of test-time compute scaling for math reasoning problems by more than 4x compared to a best-of-N baseline. The primary mechanisms for scaling test-time computation include searching against dense, process-based verifier reward models (PRMs) and updating the model's distribution over a response adaptively, given the prompt at test time.

### Verification Mechanisms
Verification plays an important role in test-time scaling and can be adapted to directly select the output sample among various ones, guide the stimulation process and determine when to stop, serve as the criteria in the search process, and determine what sample to aggregate and how to aggregate them.

### Best-of-N and Alternative Strategies
No single test-time scaling strategy is optimal and optimality depends on compute budget. The optimal TTS strategy by compute budget varies: shortest for low compute, beam search for medium, and majority voting for high.

### Broader Test-Time Scaling Research
Test-time scaling (TTS) has emerged as a prominent research focus, and recent studies demonstrate that TTS can elicit the problem-solving capabilities of large language models in specialized reasoning tasks such as mathematics and coding, as well as in general tasks.

The research indicates that adaptive, compute-optimal strategies significantly outperform simple best-of-N approaches for mathematical reasoning tasks in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6045c8a5-ab55-43ba-909d-e06db8cbf744",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "74db4ad8-c5e4-4892-8abd-d053217bc25e",
  "sourceToolAssistantUUID": "6045c8a5-ab55-43ba-909d-e06db8cbf744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T18:10:19.389Z_

Let me now fetch more details and search for additional related works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74db4ad8-c5e4-4892-8abd-d053217bc25e",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLYSgskyE6fndjaCL29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "270760bc-2dd6-4d2f-87d5-eeee46e87fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdeJgb9aoYwgDK8mDUVTRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 11919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6123,
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

_source line 25 · 2026-05-10T18:10:21.564Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GHc43khBEm8h87iqTobxqk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.18760",
  "prompt": "Extract the full title, authors, abstract, core method, and any accuracy results on MATH, GSM8K, or other benchmarks. How does HERMES relate to code execution for verification?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "270760bc-2dd6-4d2f-87d5-eeee46e87fe3",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLYSgskyE6fndjaCL29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be5b669a-489e-4ada-a67f-839942251798",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdeJgb9aoYwgDK8mDUVTRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 11919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6123,
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

_source line 26 · 2026-05-10T18:10:22.440Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017iUKjWUSTYH8rsXqetQyDk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2310.03731",
  "prompt": "Extract the full title, authors, venue, abstract, core method, and key accuracy results on MATH and GSM8K benchmarks for MathCoder."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be5b669a-489e-4ada-a67f-839942251798",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLYSgskyE6fndjaCL29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ee39fa1-56ed-41c6-8122-4a7d82b7317a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdeJgb9aoYwgDK8mDUVTRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 11919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6123,
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

_source line 27 · 2026-05-10T18:10:23.626Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018tDcUvVHdSxxQAsZVa3qb3`</summary>

```json
{
  "query": "ExecVerify white-box RL verifiable stepwise rewards code execution reasoning arXiv 2603.11226"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ee39fa1-56ed-41c6-8122-4a7d82b7317a",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLYSgskyE6fndjaCL29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6aae008e-c11b-49e4-a15e-438fbf4e095a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdeJgb9aoYwgDK8mDUVTRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 11919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6123,
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

_source line 28 · 2026-05-10T18:10:24.322Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HuHvanLAru5DqbEHqJygw7`</summary>

```json
{
  "query": "DeepSeekMath-V2 self-verifiable mathematical reasoning code verification arXiv 2511.22570"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aae008e-c11b-49e4-a15e-438fbf4e095a",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLYSgskyE6fndjaCL29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffd22f6e-229e-4c2c-b18d-0091b08664f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdeJgb9aoYwgDK8mDUVTRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 11919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6123,
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

_source line 29 · 2026-05-10T18:10:25.291Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TvbR3PQDRHNo73izfqY8Sw`</summary>

```json
{
  "query": "SymCode neurosymbolic mathematical reasoning code verification arXiv 2510.25975"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffd22f6e-229e-4c2c-b18d-0091b08664f5",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLYSgskyE6fndjaCL29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cdfe317-c1db-4e74-9d8a-4da8097bce89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdeJgb9aoYwgDK8mDUVTRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 11919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6123,
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

_source line 30 · 2026-05-10T18:10:25.780Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0152my3kLwJ2FsPo4TYXwgKQ`</summary>

```json
{
  "query": "TTRL test-time reinforcement learning mathematical reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cdfe317-c1db-4e74-9d8a-4da8097bce89",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLYSgskyE6fndjaCL29",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15d91fed-656e-43aa-a5e2-2c93f019956e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdeJgb9aoYwgDK8mDUVTRx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 11919,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6123
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 463,
          "cache_read_input_tokens": 11919,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6123,
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

_source line 31 · 2026-05-10T18:10:26.924Z_

<details><summary>↩ Tool result · `toolu_01GHc43khBEm8h87iqTobxqk`</summary>

```text
# HERMES: Paper Analysis

## Full Title
"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs"

## Authors
Azim Ospanov, Zijin Feng, Jiacheng Sun, Haoli Bai, Xin Shen, Farzan Farnia

## Abstract Summary
The paper addresses a fundamental tension in LLM reasoning: informal mathematics enables flexible problem-solving but risks logical errors, while formal theorem proving guarantees correctness but limits exploratory freedom. The researchers present a framework that "explicitly interleaves informal reasoning with formally verified proof steps in Lean."

## Core Method
HERMES operates by:
- Performing "intermediate formal checking to prevent reasoning drift"
- Maintaining a "memory module that sustains proof continuity across long, multi-step reasoning chains"
- Combining exploration and verification in one workflow

## Benchmark Results
The abstract reports results on four mathematical reasoning benchmarks. Most notably, on AIME'25, HERMES achieves "up to a 67% accuracy improvement while using 80% fewer total inference FLOPs" compared to reward-based approaches.

**Note:** The provided content does not mention results for MATH or GSM8K specifically.

## Code Verification Relationship
HERMES uses **Lean** as its verification system—a formal proof assistant with a "trusted compiler." Rather than executing code, it verifies mathematical proofs through formal proof checking, ensuring each inference step is logically sound.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be5b669a-489e-4ada-a67f-839942251798",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "a9cd92e9-2193-4039-9e5a-7a5ddb267ca3",
  "sourceToolAssistantUUID": "be5b669a-489e-4ada-a67f-839942251798",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T18:10:27.435Z_

<details><summary>↩ Tool result · `toolu_017iUKjWUSTYH8rsXqetQyDk`</summary>

```text
# MathCoder Research Summary

**Full Title:** "MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning"

**Authors:** Ke Wang, Houxing Ren, Aojun Zhou, Zimu Lu, Sichun Luo, Weikang Shi, Renrui Zhang, Linqi Song, Mingjie Zhan, Hongsheng Li

**Venue:** arXiv:2310.03731 (Computer Science > Computation and Language), submitted October 5, 2023

**Abstract:** The researchers present a method for fine-tuning open-source language models to leverage code for mathematical reasoning. They introduce MathCodeInstruct, a dataset containing "math problems and their code-based solutions" where solutions blend natural language, code, and execution output. The resulting MathCoder models demonstrate enhanced mathematical problem-solving capabilities.

**Core Method:** Fine-tuning open-source LLMs using supervised training with a custom dataset that interleaves natural language explanations, executable code, and code execution results to develop code-based mathematical reasoning.

**Key Accuracy Results:**
- **MATH dataset:** 45.2%
- **GSM8K dataset:** 83.9%

The models reportedly surpass ChatGPT-3.5, PaLM-2, and outperform GPT-4 on the competition-level MATH benchmark among open-source alternatives.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ee39fa1-56ed-41c6-8122-4a7d82b7317a",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "859f6d5a-c5ba-49ae-82e6-90287856c8b1",
  "sourceToolAssistantUUID": "9ee39fa1-56ed-41c6-8122-4a7d82b7317a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T18:10:30.325Z_

<details><summary>↩ Tool result · `toolu_018tDcUvVHdSxxQAsZVa3qb3`</summary>

```text
Web search results for query: "ExecVerify white-box RL verifiable stepwise rewards code execution reasoning arXiv 2603.11226"

Links: [{"title":"[2603.11226] ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning","url":"https://arxiv.org/abs/2603.11226"},{"title":"ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning","url":"https://arxiv.org/html/2603.11226"},{"title":"ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code","url":"https://arxiv.org/pdf/2603.11226"},{"title":"(PDF) ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning","url":"https://www.researchgate.net/publication/401909194_ExecVerify_White-Box_RL_with_Verifiable_Stepwise_Rewards_for_Code_Execution_Reasoning"},{"title":"ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning | OpenReview","url":"https://openreview.net/forum?id=DDZw4Y5gHY"},{"title":"Paper page - Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning","url":"https://huggingface.co/papers/2603.15611"},{"title":"GitHub - tlx000000001/ExecVerify · GitHub","url":"https://github.com/tlx000000001/ExecVerify"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=code+execution+reasoning"},{"title":"He Ye's research works | Carnegie Mellon University and other places","url":"https://www.researchgate.net/scientific-contributions/He-Ye-2284079487"},{"title":"GitHub - benjaminzwhite/reasoning-models: Experiments with reasoning models, training techniques, papers · GitHub","url":"https://github.com/benjaminzwhite/reasoning-models"}]

I found the research paper for you. Here's what ExecVerify is about:

ExecVerify is a paper addressing code LLMs' struggles with code execution reasoning, especially in smaller models. 

**Core Contribution:**
ExecVerify incorporates verifiable white-box rewards derived from execution traces, including next-statement prediction and variable value/type prediction.

**Methodology:**
The approach involves three main components:
1. Building a dataset with multiple difficulty levels via constraint-based program synthesis
2. Applying reinforcement learning (RL) to reward correct answers about both intermediate execution steps and final outputs, aligning the training objective with semantic correctness at each execution step
3. Adopting a two-stage training pipeline that first enhances execution reasoning and then transfers to code generation

**Results:**
A 7B model trained with ExecVerify achieves performance comparable to 32B models on code reasoning benchmarks and improves pass@1 by up to 5.9% on code generation tasks over strong post-training baselines.

The paper (arXiv:2603.11226) was published on March 11, 2026, by researchers from Zhejiang University and University College London.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6aae008e-c11b-49e4-a15e-438fbf4e095a",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "3d091819-3062-42d4-8070-64f325035f3d",
  "sourceToolAssistantUUID": "6aae008e-c11b-49e4-a15e-438fbf4e095a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T18:10:33.882Z_

<details><summary>↩ Tool result · `toolu_01HuHvanLAru5DqbEHqJygw7`</summary>

```text
Web search results for query: "DeepSeekMath-V2 self-verifiable mathematical reasoning code verification arXiv 2511.22570"

Links: [{"title":"[2511.22570] DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning","url":"https://arxiv.org/abs/2511.22570"},{"title":"DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning","url":"https://arxiv.org/html/2511.22570v1"},{"title":"Paper page - DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning","url":"https://huggingface.co/papers/2511.22570"},{"title":"DeepSeekMath-V2: Self-Verifiable Math Reasoning","url":"https://www.emergentmind.com/papers/2511.22570"},{"title":"[2511.22570v1] DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning","url":"https://arxiv.org/abs/2511.22570v1"},{"title":"Zhihong Shao 邵智宏 - Zhihong Shao 邵智宏","url":"https://zhihongshao.github.io/"},{"title":"deepseek-ai/DeepSeek-Math-V2 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Math-V2"},{"title":"DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning","url":"https://www.researchgate.net/publication/398135500_DeepSeekMath-V2_Towards_Self-Verifiable_Mathematical_Reasoning"},{"title":"DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning | by Tahir | Nov, 2025 | Medium","url":"https://medium.com/@tahirbalarabe2/deepseekmath-v2-towards-self-verifiable-mathematical-reasoning-cecdb03cea13"},{"title":"2025 Major Release: How Does DeepSeekMath-V2 Achieve Self-Verifying Mathematical Reasoning? Complete Technical Analysis - DEV Community","url":"https://dev.to/czmilo/2025-major-release-how-does-deepseekmath-v2-achieve-self-verifying-mathematical-reasoning-3pje"}]

I found comprehensive information about the DeepSeekMath-V2 paper (arXiv 2511.22570). Here's a summary of the key findings:

## Overview

DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning is a recent paper that addresses fundamental limitations in how LLMs are trained for mathematical reasoning.

## Key Innovation

The paper's core contribution is a shift in training methodology. Correct answers don't guarantee correct reasoning, and many mathematical tasks like theorem proving require rigorous step-by-step derivation rather than numerical answers, making final answer rewards inapplicable.

## Technical Approach

The researchers investigate how to train an accurate and faithful LLM-based verifier for theorem proving, then train a proof generator using the verifier as the reward model, and incentivize the generator to identify and resolve as many issues as possible in their own proofs before finalizing them.

A sophisticated innovation is the meta-verifier: A meta-verifier is trained to evaluate not only proofs but also the verifier's analyses; incorporating this second-order feedback in the training loop reduces hallucinated errors and aligns verification outputs with expert mathematical judgment, producing consistent verification outcomes with a substantial increase in analysis quality (from 0.85 to 0.96 on held-out data).

## Performance Results

DeepSeekMath-V2 demonstrates strong theorem-proving capabilities, achieving gold-level scores on IMO 2025 and CMO 2024 and a near-perfect 118/120 on Putnam 2024 with scaled test-time compute.

The paper was submitted to arXiv on November 27, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffd22f6e-229e-4c2c-b18d-0091b08664f5",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "67916ec3-c812-4fbc-b68d-80d824ecc30c",
  "sourceToolAssistantUUID": "ffd22f6e-229e-4c2c-b18d-0091b08664f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T18:10:34.312Z_

<details><summary>↩ Tool result · `toolu_01TvbR3PQDRHNo73izfqY8Sw`</summary>

```text
Web search results for query: "SymCode neurosymbolic mathematical reasoning code verification arXiv 2510.25975"

Links: [{"title":"[2510.25975] SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation","url":"https://arxiv.org/abs/2510.25975"},{"title":"SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation","url":"https://arxiv.org/html/2510.25975v1"},{"title":"SymCode: A Neurosymbolic Approach to Mathematical Reasoning via","url":"https://arxiv.org/pdf/2510.25975"},{"title":"A Neurosymbolic Approach to Mathematical Reasoning via ...","url":"https://aclanthology.org/2026.findings-eacl.76.pdf"},{"title":"Neuro-Symbolic Data Generation for Math Reasoning","url":"https://arxiv.org/html/2412.04857v1"},{"title":"NeuroSymbolic LLM for Mathematical Reasoning and Software Engineering","url":"https://www.ijcai.org/proceedings/2024/0961.pdf"},{"title":"Neuro-Symbolic Data Generation for Math Reasoning Zenan Li1∗ Zhi Zhou1∗","url":"https://openreview.net/pdf?id=CIcMZGLyZW"},{"title":"A Path Less Traveled: Reimagining Software Engineering Automation via a Neurosymbolic Paradigm","url":"https://arxiv.org/html/2505.02275v1"},{"title":"Neuro-Symbolic Data Generation for Math Reasoning","url":"https://www.arxiv.org/pdf/2412.04857"},{"title":"Neuro-Symbolic Verifier","url":"https://www.emergentmind.com/topics/neuro-symbolic-verifier"}]

Based on the search results, I found comprehensive information about SymCode from arXiv paper 2510.25975. Here's what the paper is about:

## Overview

SymCode is a neurosymbolic framework that reframes mathematical problem-solving as a task of verifiable code generation using the SymPy library.

## Problem it Addresses

Large Language Models (LLMs) often struggle with complex mathematical reasoning, where prose-based generation leads to unverified and arithmetically unsound solutions. Current prompting strategies like Chain of Thought still operate within this unreliable medium, lacking a mechanism for deterministic verification.

## How SymCode Works

Instead of prompting an LLM to describe its reasoning in prose, SymCode instructs it to construct a verifiable, executable Python script where the code serves as the reasoning trace. A natural language problem is translated into Python code by the LLM, executed, and iteratively refined through error feedback until successful execution or a retry limit is reached.

Framing mathematical reasoning as code generation enables applying an iterative self-debugging mechanism where LLM uses deterministic interpreter feedback to correct its own errors, a robust verification process not available to prose-based reasoners.

## Key Features

SymCode is a training-free method focused on verifiable SymPy code generation with a self-debugging loop.

## Results

SymCode improves accuracy by up to 13.6 percentage points (and up to 16.8 with SymCode+) over traditional prompting baselines, with the performance gap increasing as problem difficulty rises. The evaluation was conducted on MATH-500, OlympiadBench, and AIME datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cdfe317-c1db-4e74-9d8a-4da8097bce89",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "7ded508b-3cb7-4651-92c3-a252609cf363",
  "sourceToolAssistantUUID": "4cdfe317-c1db-4e74-9d8a-4da8097bce89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T18:10:36.170Z_

<details><summary>↩ Tool result · `toolu_0152my3kLwJ2FsPo4TYXwgKQ`</summary>

```text
Web search results for query: "TTRL test-time reinforcement learning mathematical reasoning 2025 2026"

Links: [{"title":"arXiv:2504.16084v3 [cs.CL] 30 Jun 2025 TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2504.16084"},{"title":"TTRL: Test-Time Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=VuVhgEiu20"},{"title":"[2504.16084] TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2504.16084"},{"title":"TTRL: Test-Time Reinforcement Learning | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/ttrl-test-time-reinforcement-learning-d78a74e78a28"},{"title":"GitHub - PRIME-RL/TTRL: [NeurIPS 2025] TTRL: Test-Time Reinforcement Learning · GitHub","url":"https://github.com/prime-rl/ttrl"},{"title":"Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning","url":"https://arxiv.org/html/2604.21327"},{"title":"arXiv:2504.16084v1 [cs.CL] 22 Apr 2025 TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2504.16084v1"},{"title":"[2604.21327] Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning","url":"https://arxiv.org/abs/2604.21327"},{"title":"Olympiad-level formal mathematical reasoning with reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09833-y"},{"title":"Amplification Effects in Test-Time Reinforcement Learning","url":"https://www.merl.com/publications/docs/TR2026-020.pdf"}]

Based on the web search results, here's what I found about TTRL (Test-Time Reinforcement Learning) for mathematical reasoning:

## Overview

TTRL is a novel method for training LLMs using RL on unlabeled data. The method investigates Reinforcement Learning on data without explicit labels for reasoning tasks in Large Language Models, with the core challenge being reward estimation during inference while not having access to ground-truth information.

## How It Works

Common practices in Test-Time Scaling (TTS), such as majority voting, yield surprisingly effective rewards suitable for driving RL training. TTRL uses majority voting among multiple model predictions to create pseudo-labels, which then serve as reward signals for reinforcement learning during test time.

## Performance Results

TTRL boosts the pass@1 performance of Qwen-2.5-Math-7B by approximately 211% on the AIME 2024 with only unlabeled test data. Although TTRL is only supervised by the Maj@N metric, it has demonstrated performance to consistently surpass the upper limit of the initial model, and approach the performance of models trained directly on test data with ground-truth labels.

## Publication Status

The paper was published at NeurIPS 2025, with the preprint available on arXiv dated April 22, 2025.

## Recent Extensions

Research building on TTRL has continued into 2026, with work extending this paradigm by various researchers, addressing challenges like spurious signal amplification in mathematical reasoning applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15d91fed-656e-43aa-a5e2-2c93f019956e",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "5b79a646-d17b-4aef-8a51-647c3678c5e2",
  "sourceToolAssistantUUID": "15d91fed-656e-43aa-a5e2-2c93f019956e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-10T18:10:39.993Z_

Excellent. Let me fetch additional details and search for a few more important related works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b79a646-d17b-4aef-8a51-647c3678c5e2",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLZrhXyDUmYCXidiSmZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f590595b-41a5-4244-b04e-632d5f20df19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2UstjwBPDYVK8cfXcXULb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4845,
      "cache_read_input_tokens": 18042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4845,
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

_source line 38 · 2026-05-10T18:10:44.793Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q3pMboasUk4J4Tx8Lp6gbu`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.25975",
  "prompt": "Extract the full title, authors, venue, abstract, and key accuracy numbers on MATH-500, AIME, and OlympiadBench benchmarks. How does SymCode relate to best-of-N selection or verification?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f590595b-41a5-4244-b04e-632d5f20df19",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLZrhXyDUmYCXidiSmZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7cca2b4-4d3a-46cf-8abc-da0fbc3929fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2UstjwBPDYVK8cfXcXULb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4845,
      "cache_read_input_tokens": 18042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4845,
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

_source line 39 · 2026-05-10T18:10:44.994Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014bvQKXhyBpVfjqc7BMkmfb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.11226",
  "prompt": "Extract the full title, authors, abstract, core method, and key results. How does ExecVerify relate to code execution-based verification for mathematical reasoning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7cca2b4-4d3a-46cf-8abc-da0fbc3929fb",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLZrhXyDUmYCXidiSmZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0155646-7c96-4c88-adbb-55da89a1d5f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2UstjwBPDYVK8cfXcXULb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4845,
      "cache_read_input_tokens": 18042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4845,
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

_source line 40 · 2026-05-10T18:10:45.035Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mm6jCo7sJPq7o1GTeQYXoJ`</summary>

```json
{
  "query": "process reward model verification best-of-N math reasoning ORM PRM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0155646-7c96-4c88-adbb-55da89a1d5f0",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLZrhXyDUmYCXidiSmZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e82f06c2-e858-46dc-9cc6-bb0fe0608ced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2UstjwBPDYVK8cfXcXULb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4845,
      "cache_read_input_tokens": 18042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4845,
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

_source line 41 · 2026-05-10T18:10:45.075Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P8sGSpPjihfmSHkPYR2aw5`</summary>

```json
{
  "query": "code-based verification reward model mathematical reasoning scaling inference compute 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e82f06c2-e858-46dc-9cc6-bb0fe0608ced",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLZrhXyDUmYCXidiSmZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6fb951c-33ba-4fa4-b8ed-d3bca2416f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2UstjwBPDYVK8cfXcXULb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4845,
      "cache_read_input_tokens": 18042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4845,
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

_source line 42 · 2026-05-10T18:10:49.945Z_

<details><summary>↩ Tool result · `toolu_01Q3pMboasUk4J4Tx8Lp6gbu`</summary>

```text
# SymCode: Research Summary

**Full Title:** "SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation"

**Authors:** Sina Bagheri Nezhad, Yao Li, Ameeta Agrawal

**Venue:** EACL 2026 Findings

## Abstract

The paper addresses LLM limitations in mathematical reasoning by introducing a framework that "reframes mathematical problem-solving as a task of verifiable code generation using the SymPy library."

## Key Accuracy Numbers

The provided webpage content mentions only **MATH-500 and OlympiadBench benchmarks**, reporting "significant accuracy improvements of up to 13.6 percentage points over baselines." Specific scores and AIME results are not detailed in this page excerpt.

## SymCode's Relation to Verification

The webpage does not explicitly discuss connections to best-of-N selection. However, it emphasizes that SymCode "shifts model failures from opaque logical fallacies towards transparent, programmatic errors" through deterministic symbolic verification via SymPy, representing "a key step towards more accurate and trustworthy AI in formal domains."

The full paper PDF would contain detailed benchmark comparisons and methodology discussion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7cca2b4-4d3a-46cf-8abc-da0fbc3929fb",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "e5dbb2ad-ec80-4da2-a50f-a58922230d9c",
  "sourceToolAssistantUUID": "f7cca2b4-4d3a-46cf-8abc-da0fbc3929fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T18:10:54.207Z_

<details><summary>↩ Tool result · `toolu_01P8sGSpPjihfmSHkPYR2aw5`</summary>

```text
Web search results for query: "code-based verification reward model mathematical reasoning scaling inference compute 2025 2026"

Links: [{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Shrinking the Generation-Verification Gap with Weak Verifiers","url":"https://scalingintelligence.stanford.edu/pubs/weaver.pdf"},{"title":"Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=A6Y7AqlzLW"},{"title":"From Mathematical Reasoning to Code: Generalization of Process Reward Models in Test-Time Scaling | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40289"},{"title":"Reward Models and Learning Strategies","url":"https://aclanthology.org/2025.findings-emnlp.970.pdf"},{"title":"Published as a conference paper at ICLR 2025 INFERENCE SCALING LAWS:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf"},{"title":"SCALING AUTOMATED PROCESS VERIFIERS FOR LLM ...","url":"https://openreview.net/pdf?id=A6Y7AqlzLW"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"Incentivizing LLMs to Self-Verify Their Answers Fuxiang Zhang1,2 Jiacheng Xu1,2","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_Verify.pdf"},{"title":"Rethinking Reward Models for Multi-Domain Test-Time Scaling | OpenReview","url":"https://openreview.net/forum?id=NFJK96X82a"}]

I've completed a web search for your query about code-based verification reward models, mathematical reasoning, and scaling inference compute in 2025-2026. Here's a summary of the relevant findings:

## Key Research Areas

**Process Reward Models (PRMs) and Verification**

Recent work includes "From Mathematical Reasoning to Code: Generalization of Process Reward Models in Test-Time Scaling" and "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning" (2025). A paper on "From Mathematical Reasoning to Code: Generalization of Process Reward Models in Test-Time Scaling" was published in the AAAI-26 proceedings (2026).

**Verification Scaling and Test-Time Compute**

Verifiers score responses, and when combined with repeated sampling of multiple candidate responses, a perfect verifier can select correct responses, significantly enhancing model capability on tasks such as math, code, and reasoning. However, a generation-verification gap emerges when perfect verifiers are unavailable, where models can generate correct responses but fail to identify them—this gap is prevalent across mathematics, coding, scientific reasoning, and instruction-following.

**Inference Scaling Laws**

Performance scales with increased inference compute across various model sizes, with increasing compute budgets leading to higher accuracy until saturation; as compute budget increases, smaller models initially perform better than larger ones, but once smaller model accuracy saturates, larger models show favorable performance.

**Multi-Domain Reward Models**

A unified evaluation of reward model variants across 14 diverse domains found that discriminative outcome reward models (dORM) perform on par with discriminative process reward models (dPRM), generative ORMs (gORM) are the most robust, and gPRM is not competitive.

The search results show active research into scaling verification approaches for both mathematical reasoning and code across 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6fb951c-33ba-4fa4-b8ed-d3bca2416f17",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "3b198cd4-50a1-41dc-b17b-4629ceb53ddf",
  "sourceToolAssistantUUID": "c6fb951c-33ba-4fa4-b8ed-d3bca2416f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T18:10:55.026Z_

<details><summary>↩ Tool result · `toolu_014bvQKXhyBpVfjqc7BMkmfb`</summary>

```text
# ExecVerify: Paper Summary

**Full Title:**
ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning

**Authors:**
Lingxiao Tang, He Ye, Zhaoyang Chu, Muyang Ye, Zhongxin Liu, Xiaoxue Ren, Lingfeng Bao

**Abstract:**
The research addresses limitations in code LLMs' execution reasoning capabilities. Rather than relying solely on teacher-generated explanations, the work introduces "white-box rewards derived from execution traces, including next-statement prediction and variable value/type prediction."

**Core Method:**
The approach employs three key components: (1) constructing difficulty-stratified datasets via constraint-based program synthesis, (2) applying reinforcement learning to optimize intermediate execution steps and final outputs for semantic correctness, and (3) implementing a two-stage training pipeline that first enhances execution reasoning before transferring to code generation.

**Key Results:**
A 7-billion-parameter model trained with this method demonstrates performance matching much larger 32B models on code reasoning benchmarks, achieving up to 5.9% improvement in pass@1 metrics on code generation tasks compared to baseline post-training approaches.

**Relation to Mathematical Reasoning:**
The paper focuses specifically on code execution verification rather than mathematical reasoning. While both domains involve step-by-step correctness verification, ExecVerify targets program semantics and computational traces rather than mathematical proof chains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0155646-7c96-4c88-adbb-55da89a1d5f0",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "676b7c57-eb91-41c2-8d2c-fb99fc8fe13e",
  "sourceToolAssistantUUID": "b0155646-7c96-4c88-adbb-55da89a1d5f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T18:10:55.863Z_

<details><summary>↩ Tool result · `toolu_01Mm6jCo7sJPq7o1GTeQYXoJ`</summary>

```text
Web search results for query: "process reward model verification best-of-N math reasoning ORM PRM 2024 2025"

Links: [{"title":"[2501.07301] The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"https://arxiv.org/abs/2501.07301"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://aclanthology.org/2025.emnlp-main.679.pdf"},{"title":"Paper page - The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"https://huggingface.co/papers/2501.07301"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"Let’s Verify Step by Step, ORM vs PRM | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/lets-verify-step-by-step-orm-vs-prm-613ecffb59ab"},{"title":"2024-10-11 Rewarding Progress: Scaling Automated Process","url":"https://arxiv.org/pdf/2410.08146"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Qwen/Qwen2.5-Math-PRM-72B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"}]

Based on the web search results, I found several recent papers and resources about Process Reward Models (PRMs), verification, and best-of-N selection in mathematical reasoning from 2024-2025:

## Key Findings:

### Major Recent Works

Process Reward Models (PRMs) emerge as a promising approach for process supervision in mathematical reasoning of Large Language Models (LLMs), which aim to identify and mitigate intermediate errors in the reasoning processes.

**"The Lessons of Developing Process Reward Models in Mathematical Reasoning"** (January 2025): This research demonstrates that commonly used Monte Carlo (MC) estimation-based data synthesis for PRMs typically yields inferior performance and generalization compared to LLM-as-a-judge and human annotation methods, as MC estimation relies on completion models to evaluate current-step correctness, leading to inaccurate step verification. The work identifies potential biases in conventional Best-of-N (BoN) evaluation strategies for PRMs: unreliable policy models generate responses with correct answers but flawed processes, leading to a misalignment between the evaluation criteria of BoN and the PRM objectives of process verification, and the tolerance of PRMs of such responses leads to inflated BoN scores.

**ThinkPRM - "Process Reward Models That Think"** (October 2025): ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs, capitalizing on the inherent reasoning abilities of long CoT models, and outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks.

**R-PRM - "Reasoning-Driven Process Reward Modeling"** (March 2025): When used to guide policy model reasoning via Best-of-N and Guided Search strategies, this approach improves accuracy by average margins of 8.6 and 8.4 points over the Pass@1 baseline across six challenging math datasets.

### ORM vs PRM

An outcome reward model (ORM) is a trained verifier that assigns a numerical score after the last step of the trace, and a process reward model (PRM) is a trained verifier that scores each step of the trace individually.

### Practical Implementation

Qwen2.5-Math released both Outcome Reward Model (ORM) and Process Reward Model (PRM) variants, with trained PRMs exhibiting both impressive performance in Best-of-N (BoN) evaluation and stronger error identification performance in ProcessBench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e82f06c2-e858-46dc-9cc6-bb0fe0608ced",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "705aa69a-03ce-4b28-a35c-2d378ef20671",
  "sourceToolAssistantUUID": "e82f06c2-e858-46dc-9cc6-bb0fe0608ced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-10T18:10:59.493Z_

Let me now search for a few more highly relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "705aa69a-03ce-4b28-a35c-2d378ef20671",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLbJtAKoRUdCoUADS4R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "357d9bc6-beae-4ea5-a2c3-48900b6f9887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6Q5n4qL7mLapvnwEpP4wi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 2105,
      "cache_read_input_tokens": 22887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2105,
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

_source line 47 · 2026-05-10T18:11:00.387Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MyLrUNaZQ5AH9GYDjFXWDg`</summary>

```json
{
  "query": "Agentic Code Reasoning arXiv 2603.01896 mathematical verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "357d9bc6-beae-4ea5-a2c3-48900b6f9887",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLbJtAKoRUdCoUADS4R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb650d40-3eb1-4fe0-b5d6-457478876243",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6Q5n4qL7mLapvnwEpP4wi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 2105,
      "cache_read_input_tokens": 22887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2105,
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

_source line 48 · 2026-05-10T18:11:01.329Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XRnEmhzmyZmAuHD9j5dikj`</summary>

```json
{
  "query": "\"scaling LLM test-time compute\" Snell best-of-N verifier ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb650d40-3eb1-4fe0-b5d6-457478876243",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLbJtAKoRUdCoUADS4R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfa64daa-1c76-45aa-bb08-7425bef2ecc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6Q5n4qL7mLapvnwEpP4wi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 2105,
      "cache_read_input_tokens": 22887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2105,
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

_source line 49 · 2026-05-10T18:11:01.701Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011SuXN3H98qWA8eDz3aTXDo`</summary>

```json
{
  "query": "GenPRM generative process reward model test-time scaling code verification 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfa64daa-1c76-45aa-bb08-7425bef2ecc5",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLbJtAKoRUdCoUADS4R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1e5c39b-19f2-4898-8134-cd3964a16d17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6Q5n4qL7mLapvnwEpP4wi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 2105,
      "cache_read_input_tokens": 22887,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2105
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1044,
          "output_tokens": 195,
          "cache_read_input_tokens": 22887,
          "cache_creation_input_tokens": 2105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2105,
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

_source line 50 · 2026-05-10T18:11:06.232Z_

<details><summary>↩ Tool result · `toolu_01MyLrUNaZQ5AH9GYDjFXWDg`</summary>

```text
Web search results for query: "Agentic Code Reasoning arXiv 2603.01896 mathematical verification"

Links: [{"title":"[2603.01896] Agentic Code Reasoning","url":"https://arxiv.org/abs/2603.01896"},{"title":"Agentic Code Reasoning","url":"https://arxiv.org/html/2603.01896"},{"title":"Agentic Code Reasoning Shubham Ugare, Satish Chandra Meta, USA","url":"https://arxiv.org/pdf/2603.01896"},{"title":"[2603.01896v2] Agentic Code Reasoning","url":"https://arxiv.org/abs/2603.01896v2"},{"title":"Agentic Code Reasoning","url":"https://www.emergentmind.com/papers/2603.01896"},{"title":"Agentic Code Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260301896U/abstract"},{"title":"Paper page - Agentic Code Reasoning","url":"https://huggingface.co/papers/2603.01896"},{"title":"Agentic Code Reasoning","url":"https://www.researchgate.net/publication/401494216_Agentic_Code_Reasoning"},{"title":"Agentic Code Reasoning | Scilit","url":"https://www.scilit.com/publications/e596d05bf8683fa7df50946e1a7f7041"},{"title":"Agentic Code Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.01896"}]

Based on the search results, here's information about the arXiv paper 2603.01896 on "Agentic Code Reasoning":

## Overview

The paper was submitted on March 2, 2026, with a revised version on March 4, 2026, authored by Shubham Ugare and Satish Chandra from Meta.

## Main Contribution

The paper introduces semi-formal reasoning: a structured prompting methodology that requires agents to construct explicit premises, trace execution paths, and derive formal conclusions. Unlike unstructured chain-of-thought, semi-formal reasoning acts as a certificate: the agent cannot skip cases or make unsupported claims.

## Evaluation and Results

The paper evaluates across three tasks (patch equivalence verification, fault localization, and code question answering) and shows that semi-formal reasoning consistently improves accuracy on all of them. 

More specifically:
- For patch equivalence, accuracy improves from 78% to 88% on curated examples and reaches 93% on real-world agent-generated patches
- For code question answering on RubberDuckBench, semi-formal reasoning achieves 87% accuracy, a 9 percentage point gain over standard agentic reasoning
- For fault localization on Defects4J, semi-formal reasoning improves Top-5 accuracy by 5 percentage points over standard reasoning

## Practical Applications

These results demonstrate that structured agentic reasoning enables meaningful semantic code analysis without execution, opening practical applications in RL training pipelines, code review, and static program analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb650d40-3eb1-4fe0-b5d6-457478876243",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "47c5689c-f36c-4380-bad7-b42d20092112",
  "sourceToolAssistantUUID": "cb650d40-3eb1-4fe0-b5d6-457478876243",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-10T18:11:08.557Z_

<details><summary>↩ Tool result · `toolu_011SuXN3H98qWA8eDz3aTXDo`</summary>

```text
Web search results for query: "GenPRM generative process reward model test-time scaling code verification 2025"

Links: [{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward ...","url":"https://arxiv.org/pdf/2504.00891"},{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"},{"title":"Paper page - GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://huggingface.co/papers/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://ryanliu112.github.io/GenPRM/"},{"title":"[PDF] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GenPRM:-Scaling-Test-Time-Compute-of-Process-Reward-Zhao-Liu/bd94932b7604933a11d1538b0de6f9543089711f"},{"title":"Breaking the LLM Bottleneck: GenPRM’s approach to Scale test-time compute via generative reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Arxiv - DeepPaper","url":"https://arxiv.deeppaper.ai/papers/2504.00891v2?locale=en"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Request PDF","url":"https://www.researchgate.net/publication/390404512_GenPRM_Scaling_Test-Time_Compute_of_Process_Reward_Models_via_Generative_Reasoning"}]

Based on the search results, here's what I found about GenPRM:

## Overview

GenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step.

## Key Features

Current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. GenPRM addresses these issues through several innovations:

- **Generative Approach**: GenPRM redefines process supervision as a generative task rather than a discriminative scoring task by integrating Chain-of-Thought (CoT) reasoning and code verification processes before providing final judgment.

- **Training Methodology**: To obtain high-quality process supervision labels and rationale data, the researchers propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification.

## Performance and Test-Time Scaling

Through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement.

## Release and Availability

GenPRM was accepted by AAAI 2026. Models (GenPRM-1.5B & GenPRM-7B) and training data were released on HuggingFace. The full data synthesis code became available on April 24, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1e5c39b-19f2-4898-8134-cd3964a16d17",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "f3ce1341-17e2-4f3d-9549-0ef8e45d2def",
  "sourceToolAssistantUUID": "d1e5c39b-19f2-4898-8134-cd3964a16d17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-10T18:11:09.460Z_

<details><summary>↩ Tool result · `toolu_01XRnEmhzmyZmAuHD9j5dikj`</summary>

```text
Web search results for query: ""scaling LLM test-time compute" Snell best-of-N verifier ICLR 2025"

Links: [{"title":"[2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314"},{"title":"SCALING LLM TEST-TIME COMPUTE OPTIMALLY CAN ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"Track: Oral Session 1A","url":"https://iclr.cc/virtual/2025/session/31935"},{"title":"ICLR 2025 Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning Oral","url":"https://iclr.cc/virtual/2025/oral/31924"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"},{"title":"ICLR Poster Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning","url":"https://iclr.cc/virtual/2025/poster/31024"},{"title":"Published as a conference paper at ICLR 2025 INFERENCE SCALING LAWS:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/scaling-llm-test-time-compute-optimally-can-be-more-effective-than-scaling-model-parameters-19a0c9fb7c44"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More ...","url":"https://faculty.cc.gatech.edu/~zk15/teaching/AY2025_cs7643_spring/assets/L25_Charlie_Snell_Scaling_TestTime_Compute.pdf"}]

I found detailed information about the paper you're searching for. Here are the results:

## Overview

The paper "Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Parameters for Reasoning" by Charlie Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar was published as a conference paper at ICLR 2025.

## Main Research Question and Approach

The paper investigates how much an LLM can improve its performance on a challenging prompt if allowed to use a fixed but non-trivial amount of inference-time compute. Answering this question has implications on both performance and the future of LLM pretraining, including how to tradeoff inference-time and pre-training compute.

## Key Methods and Findings

The work analyzes two primary mechanisms to scale test-time computation: (1) searching against dense, process-based verifier reward models (PRMs); and (2) updating the model's distribution over a response adaptively.

Comparing different search methods, at low generation budgets, beam search performs best, but as the budget increases further, improvements diminish, falling below the best-of-N baseline.

The paper introduces the notion of "compute-optimal" scaling of test-time computation, which prescribes an adaptive, prompt-dependent strategy to improve performance under a given test-time compute budget. By applying such a compute-optimal scaling strategy, they improve the efficiency of test-time compute scaling by a factor of 2–4×.

When comparing benefits obtained from additional test-time compute against benefits from additional pre-training compute in a FLOPs-matched setting, they show that using test-time computation with simple methods like revisions and search can scale well on certain types of prompts, providing gains over spending those FLOPs in pretraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfa64daa-1c76-45aa-bb08-7425bef2ecc5",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "683ce701-d0f1-45d8-9920-23194e201c87",
  "sourceToolAssistantUUID": "bfa64daa-1c76-45aa-bb08-7425bef2ecc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-10T18:11:12.674Z_

Let me fetch one more crucial paper and do a final search for any works I might be missing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "683ce701-d0f1-45d8-9920-23194e201c87",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLcK4bv49vtB8J93SS7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ef4fa28-38a5-4ef0-854e-830a8ce83085",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5FxMxSAUuqYqgferJC74U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1107,
      "cache_creation_input_tokens": 3150,
      "cache_read_input_tokens": 24992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3150,
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

_source line 54 · 2026-05-10T18:11:15.132Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KGMFtQJZBWKPrbGp4U6QAf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.00891",
  "prompt": "Extract the full title, authors, abstract, core method details about code verification in the process reward model, and key accuracy numbers. How does GenPRM use code execution for verification in best-of-N selection?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ef4fa28-38a5-4ef0-854e-830a8ce83085",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLcK4bv49vtB8J93SS7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd702d72-63de-4b1f-bd58-edc3a80290aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5FxMxSAUuqYqgferJC74U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1107,
      "cache_creation_input_tokens": 3150,
      "cache_read_input_tokens": 24992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3150,
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

_source line 55 · 2026-05-10T18:11:16.100Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018daYHsPaM3AcGwfum5RMf7`</summary>

```json
{
  "query": "\"Scoring Verifiers\" synthetic verification code reasoning best-of-N arXiv 2502.13820"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd702d72-63de-4b1f-bd58-edc3a80290aa",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLcK4bv49vtB8J93SS7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86a3212b-2ac0-4d79-91af-5a52d70eb1c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5FxMxSAUuqYqgferJC74U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1107,
      "cache_creation_input_tokens": 3150,
      "cache_read_input_tokens": 24992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3150,
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

_source line 56 · 2026-05-10T18:11:16.745Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qbz3fqp1pHidoGEcRp5bVY`</summary>

```json
{
  "query": "Skywork-o1 open series best-of-N process reward verification math reasoning 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86a3212b-2ac0-4d79-91af-5a52d70eb1c7",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLcK4bv49vtB8J93SS7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b46d5aba-1069-4aa4-816a-3690bc3e311c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5FxMxSAUuqYqgferJC74U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1107,
      "cache_creation_input_tokens": 3150,
      "cache_read_input_tokens": 24992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3150,
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

_source line 57 · 2026-05-10T18:11:21.249Z_

<details><summary>↩ Tool result · `toolu_01KGMFtQJZBWKPrbGp4U6QAf`</summary>

```text
# GenPRM: Process Reward Models via Generative Reasoning

## Title
"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning"

## Authors
Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, and Bowen Zhou

## Abstract Summary
The paper introduces a generative process reward model that performs explicit reasoning with code verification before judging each step. The approach incorporates Relative Progress Estimation (RPE) and a rationale synthesis framework with code verification to generate high-quality training labels. Results demonstrate significant improvements using only 23K training examples from the MATH dataset.

## Core Method: Code Verification Integration
The model executes "explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment" for each reasoning step. This generative approach leverages LLM capabilities beyond scalar predictions, incorporating verification mechanisms into the process supervision framework.

## Key Performance Metrics
- A 1.5B parameter GenPRM outperforms GPT-4o on ProcessBench
- A 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench
- Trained on only 23K examples from MATH dataset

## Best-of-N Selection Mechanism
The provided content does not explicitly describe how GenPRM applies code verification specifically for best-of-N selection. The abstract notes strong abilities "to serve as a critic model for policy model refinement" but doesn't detail the selection strategy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd702d72-63de-4b1f-bd58-edc3a80290aa",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "9770a75c-4b6a-46d6-9088-61450364c004",
  "sourceToolAssistantUUID": "dd702d72-63de-4b1f-bd58-edc3a80290aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T18:11:24.363Z_

<details><summary>↩ Tool result · `toolu_01Qbz3fqp1pHidoGEcRp5bVY`</summary>

```text
Web search results for query: "Skywork-o1 open series best-of-N process reward verification math reasoning 2024"

Links: [{"title":"Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B · Hugging Face","url":"https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B"},{"title":"Skywork O1 Open PRM Qwen 2.5 7B · Models · Dataloop","url":"https://dataloop.ai/library/model/skywork_skywork-o1-open-prm-qwen-25-7b/"},{"title":"Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B · Hugging Face","url":"https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B"},{"title":"Skywork/Skywork-o1-Open-Llama-3.1-8B · Hugging Face","url":"https://huggingface.co/Skywork/Skywork-o1-Open-Llama-3.1-8B"},{"title":"Skywork-o1-Open-PRM-Qwen-2.5-1.5B","url":"https://www.promptlayer.com/models/skywork-o1-open-prm-qwen-25-15b"},{"title":"Skywork-o1-Open-PRM-Qwen-2.5-7B","url":"https://www.promptlayer.com/models/skywork-o1-open-prm-qwen-25-7b"},{"title":"Kunlun Tech \"Tiangong Large Model 4.0\" o1 version (Skywork o1) officially starts inviting testing.","url":"https://news.futunn.com/en/post/50484756/kunlun-tech-tiangong-large-model-4-0-o1-version-skywork"},{"title":"Skywork O1 Open PRM Qwen 2.5 1.5B · Models · Dataloop","url":"https://dataloop.ai/library/model/skywork_skywork-o1-open-prm-qwen-25-15b/"},{"title":"The Lessons of Developing Process Reward Models in ...","url":"https://arxiv.org/pdf/2501.07301"},{"title":"GitHub - SkyworkAI/Skywork-OR1: Unleashing the Power of Reinforcement Learning for Math and Code Reasoners · GitHub","url":"https://github.com/SkyworkAI/Skywork-OR1"}]

Based on the search results, here's what I found about Skywork-o1 Open Series, Best-of-N process reward verification, and math reasoning in 2024:

## Skywork-o1 Open Series Overview

The Skywork o1 Open model series was developed by the Skywork team at Kunlun Inc. and introduces a series of models that incorporate o1-like slow thinking and reasoning capabilities. The series includes three models: Skywork o1 Open-Llama-3.1-8B, Skywork o1 Open-PRM-Qwen-2.5-1.5B, and Skywork o1 Open-PRM-Qwen-2.5-7B.

## Best-of-N Process with Reward Models

Best-of-N@64 ranks 64 answers based on output values provided by the Reward Model (RM). For ORM, only the reward from the final step is used, while for PRM, the average reward across all steps is used for weighting.

## Process Reward Model (PRM) for Math Reasoning

The Skywork o1 Open-PRM-Qwen-2.5-1.5B model is designed to enhance reasoning capability through incremental process rewards, ideal for complex problem solving at a smaller scale. The models were evaluated on datasets including GSM8K, MATH, GaoKao, CN-Middle School 24, OlympiadBench, AMC-23, and AIME-24, with the latter three being competition-level datasets.

## Performance Results

In evaluations, Skywork O1 Open PRM Qwen 2.5 7B has shown remarkable performance, outperforming other models in mathematical evaluations and code-related tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b46d5aba-1069-4aa4-816a-3690bc3e311c",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "cf05e3e3-5e92-4c58-8e3e-350e42162442",
  "sourceToolAssistantUUID": "b46d5aba-1069-4aa4-816a-3690bc3e311c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-10T18:11:24.648Z_

<details><summary>↩ Tool result · `toolu_018daYHsPaM3AcGwfum5RMf7`</summary>

```text
Web search results for query: ""Scoring Verifiers" synthetic verification code reasoning best-of-N arXiv 2502.13820"

Links: [{"title":"[2502.13820] Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning","url":"https://arxiv.org/abs/2502.13820"},{"title":"[2502.13820v3] Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning","url":"https://arxiv.org/abs/2502.13820v3"},{"title":"Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning","url":"https://arxiv.org/html/2502.13820v2"},{"title":"Scoring Verifiers: Evaluating Synthetic Verification in Code and Reasoning","url":"https://www.arxiv.org/pdf/2502.13820v1"},{"title":"Scoring Verifiers: Evaluating Synthetic Verification in Code and Reasoning","url":"https://arxiv.org/html/2502.13820v1"},{"title":"Paper page - Scoring Verifiers: Evaluating Synthetic Verification in Code and Reasoning","url":"https://huggingface.co/papers/2502.13820"},{"title":"Computer Science Feb 2025","url":"https://www.arxiv.org/list/cs/2025-02?skip=6975&show=50"},{"title":"Software Engineering Feb 2025","url":"https://www.arxiv.org/list/cs.SE/2025-02?skip=325&show=250"},{"title":"Evaluating Synthetic Verification for Code and Reasoning","url":"https://arxiv.org/pdf/2502.13820"},{"title":"Software Engineering Feb 2025","url":"https://arxiv.org/list/cs.SE/2025-02?skip=325&show=2000"}]

I found the paper you're looking for! Here's what I found about arXiv 2502.13820:

## Overview

The paper is titled "Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning" by Aleksander Ficek, Somshubra Majumdar, Vahid Noroozi, and Boris Ginsburg.

## Main Contribution

Synthetic verification techniques such as generating test cases and reward modelling are common ways to enhance the coding capabilities of large language models (LLM) beyond predefined tests. Additionally, code verification has recently found great success as a critical component in improving reasoning capability of LLMs via reinforcement learning.

The paper proposes an approach which can transform existing coding benchmarks into scoring and ranking datasets to evaluate the effectiveness of synthetic verifiers, and also proposes multiple metrics to measure different aspects of the synthetic verifiers with the proposed benchmarks.

## Key Results

The authors release four new benchmarks (HE-R, HE-R+, MBPP-R, and MBPP-R+), and analyzed synthetic verification methods with standard, reasoning-based, and reward-based LLMs. Their results show that recent reasoning models significantly improve test case generation and that scaling test cases enhances verification accuracy.

The paper was accepted to COLM 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86a3212b-2ac0-4d79-91af-5a52d70eb1c7",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "ff8339f4-4ef4-4b32-b15b-05e1c3ebe505",
  "sourceToolAssistantUUID": "86a3212b-2ac0-4d79-91af-5a52d70eb1c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-10T18:11:29.221Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JGHGwgHk16QnGAvjXiM97B`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.13820",
  "prompt": "Extract the full title, authors, abstract, and key findings about how synthetic verification (test case generation, code execution) can be used for verifying reasoning and selecting among candidate solutions. Include any best-of-N or ranking results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff8339f4-4ef4-4b32-b15b-05e1c3ebe505",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLdRzLxAxQ1SYnNKVdF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6227f18-14b8-46e8-8723-0560c06f9ded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012F8qx7yq7traSkCzaCXjYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1138,
      "cache_creation_input_tokens": 2575,
      "cache_read_input_tokens": 28142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2575,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-10T18:11:30.196Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VwhTdNYsj8YkRBnk9udZGb`</summary>

```json
{
  "query": "verification code execution reward model mathematical reasoning \"best of N\" selection reranking 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6227f18-14b8-46e8-8723-0560c06f9ded",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLdRzLxAxQ1SYnNKVdF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abb9754a-57b3-4958-8e3a-f7b16cfd33ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012F8qx7yq7traSkCzaCXjYc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1138,
      "cache_creation_input_tokens": 2575,
      "cache_read_input_tokens": 28142,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2575
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1138,
          "output_tokens": 185,
          "cache_read_input_tokens": 28142,
          "cache_creation_input_tokens": 2575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2575,
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

_source line 62 · 2026-05-10T18:11:33.303Z_

<details><summary>↩ Tool result · `toolu_01JGHGwgHk16QnGAvjXiM97B`</summary>

```text
# Paper Summary: Scoring Verifiers

**Full Title:** Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning

**Authors:** Aleksander Ficek, Somshubra Majumdar, Vahid Noroozi, Boris Ginsburg

## Abstract

The researchers address how "synthetic verification techniques such as generating test cases and reward modelling" enhance LLM coding abilities beyond predefined tests. They propose transforming existing benchmarks into scoring and ranking datasets and introduce four new benchmarks (HE-R, HE-R+, MBPP-R, MBPP-R+) to evaluate synthetic verifiers across standard, reasoning-based, and reward-based LLMs.

## Key Findings

1. **Reasoning Impact:** The study demonstrates that reasoning-enhanced approaches substantially improve test case generation quality

2. **Scaling Benefits:** Increasing the quantity of generated test cases directly correlates with improved verification accuracy

3. **Verification Application:** Code verification serves as an important component for strengthening LLM reasoning capabilities through reinforcement learning approaches

The work effectively bridges code verification and reasoning enhancement, showing that synthetic verification methods can rank candidate solutions effectively when properly scaled and reasoning-informed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6227f18-14b8-46e8-8723-0560c06f9ded",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "844a6de5-a558-4fb9-b5ad-8dcc1eec1fe5",
  "sourceToolAssistantUUID": "f6227f18-14b8-46e8-8723-0560c06f9ded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-10T18:11:40.122Z_

<details><summary>↩ Tool result · `toolu_01VwhTdNYsj8YkRBnk9udZGb`</summary>

```text
Web search results for query: "verification code execution reward model mathematical reasoning "best of N" selection reranking 2025 2026"

Links: [{"title":"Scaling Automated Process Verifiers for LLM Reasoning","url":"https://arxiv.org/pdf/2410.08146"},{"title":"Execution Feedback-enhanced Process Reward Model for ...","url":"https://aclanthology.org/2025.findings-acl.428.pdf"},{"title":"Better Process Supervision with Bi-directional Rewarding ...","url":"https://aclanthology.org/2025.findings-acl.747.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=A6Y7AqlzLW"},{"title":"CS 224R - Final Report Beyond Strict Verification:","url":"https://cs224r.stanford.edu/projects/pdfs/CS224R_FinalReport__2_.pdf"},{"title":"Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=A6Y7AqlzLW"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://arxiv.org/pdf/2502.18581"},{"title":"Dynamic Scaling of Unit Tests for Code Reward Modeling","url":"https://aclanthology.org/2025.acl-long.343.pdf"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Published as a conference paper at ICLR 2025 LEARNING HOW HARD TO THINK:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf"}]

I've performed the web search for your query. The results show significant recent developments in this area from 2025. Here are the key findings:

## Execution Feedback-Enhanced Process Reward Models

CodePRM is an execution feedback-enhanced process reward model published at ACL 2025. It collects data labeled with average pass rates via tree search to train an execution feedback-enhanced PRM, and integrates CODEPRM into a Generate-Verify-Refine (GVR) pipeline, where it verifies and refines thought steps.

## Process Reward Models for Mathematical Reasoning

Process reward models (PRMs) provide feedback at each step of a multi-step reasoning trace, improving credit assignment over outcome reward models (ORMs) that only provide feedback at the final step.

## Automated Process Supervision

Recent work has advanced automation in this field. CodePRM employs automated tree search and execution feedback to derive step-level supervision for code reasoning, achieving fully automatic label generation without human involvement. OmegaPRM uses a divide-and-conquer style Monte Carlo Tree Search (MCTS) algorithm to efficiently identify the first error in a reasoning chain.

## Best-of-N Selection and Reranking

Reward models are used as rerankers within a beam search procedure where process rewards assign a score to every new state and only the states corresponding to the top-B values are retained in the beam for the next step. Scaling LLM test-time compute optimally can be more effective than scaling model parameters, and best-of-k reranking with a reward model is used in settings like Math, Code and Chat, where k equals the compute budget.

These developments represent significant advances in making reasoning more verifiable and scalable through automated execution feedback and intelligent selection strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abb9754a-57b3-4958-8e3a-f7b16cfd33ed",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "88133c45-1886-45e1-9792-2afc219fec0e",
  "sourceToolAssistantUUID": "abb9754a-57b3-4958-8e3a-f7b16cfd33ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-10T18:11:42.197Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DJUJ2BYr2KFbbvthm4VvUr`</summary>

```json
{
  "query": "CodePRM execution feedback process reward model mathematical reasoning ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88133c45-1886-45e1-9792-2afc219fec0e",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLea9G15d49cofqtC2i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6405fa96-4289-4ab8-9000-8b58c3e0d1e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NH5oLZokokJDKxHS1svmbt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2549,
      "cache_read_input_tokens": 30717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2549,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-10T18:11:42.427Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019h2N1d1jT37ZRoYhfLWhTm`</summary>

```json
{
  "query": "\"dynamic scaling unit tests\" code reward modeling mathematical reasoning ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6405fa96-4289-4ab8-9000-8b58c3e0d1e4",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLea9G15d49cofqtC2i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44cb3ded-6d1b-403e-9cf7-e778448cd996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NH5oLZokokJDKxHS1svmbt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2549,
      "cache_read_input_tokens": 30717,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2549
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 30717,
          "cache_creation_input_tokens": 2549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2549,
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

_source line 66 · 2026-05-10T18:11:48.668Z_

<details><summary>↩ Tool result · `toolu_01DJUJ2BYr2KFbbvthm4VvUr`</summary>

```text
Web search results for query: "CodePRM execution feedback process reward model mathematical reasoning ACL 2025"

Links: [{"title":"CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.428/"},{"title":"Execution Feedback-enhanced Process Reward Model for ...","url":"https://aclanthology.org/2025.findings-acl.428.pdf"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment","url":"https://arxiv.org/html/2510.18471v1"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/html/2601.22249v1"},{"title":"The Lessons of Developing Process Reward Models in Mathematical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.547/"},{"title":"ICML Poster Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation","url":"https://icml.cc/virtual/2025/poster/44014"},{"title":"GitHub - codefuse-ai/Awesome-Code-LLM: [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. · GitHub","url":"https://github.com/codefuse-ai/Awesome-Code-LLM"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"}]

Based on the search results, here's what I found about CodePRM:

## CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation

CodePRM is a paper published in the Findings of the Association for Computational Linguistics: ACL 2025, addressing code generation as a critical reasoning task for large language models.

### Core Problem and Approach

While the thought process in code generation lacks effective process supervision, making it hard to optimize the thoughts, Process Reward Models (PRMs) have been widely established in mathematical reasoning, but building a code PRM is still not trivial due to the gap between thoughts to code.

### Methodology

The researchers first collect a large dataset of thought traces, where each thought step is labeled with their derived code pass rates, accompanied by the corresponding code snippets and execution feedback. During training, they train a PRM to take both the reasoning process and code execution feedback as input to score individual thought steps, enabling it to leverage code execution results to distinguish between high-quality and low-quality thought steps.

### Inference Pipeline

To use the PRM during inference, they develop a Generate-Verify-Refine (GVR) pipeline where the CodePRM serves as a process verifier to dynamically identify and correct errors in the thought process during code search.

### Results

Experimental results demonstrate that CodePRM with the inference algorithm outperforms strong baselines, significantly enhancing code generation performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6405fa96-4289-4ab8-9000-8b58c3e0d1e4",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "f21a716d-1111-436c-b8c9-ab732ad0143c",
  "sourceToolAssistantUUID": "6405fa96-4289-4ab8-9000-8b58c3e0d1e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-10T18:11:49.800Z_

<details><summary>↩ Tool result · `toolu_019h2N1d1jT37ZRoYhfLWhTm`</summary>

```text
Web search results for query: ""dynamic scaling unit tests" code reward modeling mathematical reasoning ACL 2025"

Links: [{"title":"Dynamic Scaling of Unit Tests for Code Reward Modeling - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.343/"},{"title":"GitHub - RUCKBReasoning/CodeRM: Official code implementation for the ACL 2025 paper: 'Dynamic Scaling of Unit Tests for Code Reward Modeling'","url":"https://github.com/RUCKBReasoning/CodeRM"},{"title":"Dynamic Scaling of Unit Tests for Code Reward Modeling","url":"https://aclanthology.org/2025.acl-long.343.pdf"},{"title":"[2501.01054] Dynamic Scaling of Unit Tests for Code Reward Modeling","url":"https://arxiv.org/abs/2501.01054"},{"title":"(PDF) Dynamic Scaling of Unit Tests for Code Reward Modeling","url":"https://www.researchgate.net/publication/387671082_Dynamic_Scaling_of_Unit_Tests_for_Code_Reward_Modeling"},{"title":"Dynamic Scaling of Unit Tests for Code Reward Modeling","url":"https://arxiv.org/pdf/2501.01054"},{"title":"Track: Oral Session 1A","url":"https://iclr.cc/virtual/2025/session/31935"},{"title":"Paper page - Dynamic Scaling of Unit Tests for Code Reward Modeling","url":"https://huggingface.co/papers/2501.01054"},{"title":"A Survey of Mathematical Reasoning in the Era ...","url":"https://aclanthology.org/2025.findings-acl.614.pdf"},{"title":"Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.699/"}]

I found relevant information about the paper "Dynamic Scaling of Unit Tests for Code Reward Modeling" from ACL 2025. Here's what the search results show:

## Overview

The paper "Dynamic Scaling of Unit Tests for Code Reward Modeling" addresses how current large language models (LLMs) often struggle to produce accurate responses on the first attempt for complex reasoning tasks like code generation.

## Key Problem and Approach

Prior research tackles this challenge by generating multiple candidate solutions and validating them with LLM-generated unit tests. However, these unit tests are not reliable, thereby diminishing the quality of reward signals.

## Main Findings

The research reveals a positive correlation between the number of unit tests and reward signal quality, with greater benefits observed in more challenging problems.

## Proposed Solution

The authors train a lightweight yet effective unit test generator named CodeRM-8B and employ dynamic scaling over problems of different difficulties to facilitate efficient and high-quality unit test scaling.

## Results

Experimental results show that their approach significantly improves performance across various models on three benchmarks (e.g., with gains of 18.43% for Llama3-8B and 3.42% for GPT-4o-mini on HumanEval Plus).

The paper was authored by Zeyao Ma, Xiaokang Zhang, Jing Zhang, Jifan Yu, Sijia Luo, and Jie Tang, and appears in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 6917–6935, Vienna, Austria.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44cb3ded-6d1b-403e-9cf7-e778448cd996",
  "isSidechain": true,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "agentId": "a40596f27d93c653d",
  "type": "user",
  "uuid": "249bfb91-014f-4804-b9e4-f65989202fb9",
  "sourceToolAssistantUUID": "44cb3ded-6d1b-403e-9cf7-e778448cd996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-10T18:13:50.138Z_

Now I have comprehensive information. Let me compile the full landscape analysis.

---

Here is the full landscape of code-execution-based verification approaches relevant to your research proposal on symbolic pre-filtering for best-of-N verification in mathematical reasoning.

---

## 1. CORE PAPER: T3RL (Tool Verification for Test-Time Reinforcement Learning)

- **Title:** Tool Verification for Test-Time Reinforcement Learning
- **Authors:** Ruotong Liao, Nikolai Rohrich, Xiaohan Wang, Yuhui Zhang, Yasaman Samadzadeh, Volker Tresp, Serena Yeung-Levy
- **Date/Venue:** arXiv:2603.02203, March 2, 2026
- **Core method:** T3RL addresses a critical failure mode in TTRL (test-time reinforcement learning) where spurious high-frequency consensus among sampled rollouts creates biased reward signals leading to incorrect mode collapse. The system compiles each rollout's claimed computations into lightweight Python code, queries a code interpreter to obtain executable evidence, and then an LLM verifier uses the execution result to upweight verified rollouts in a "verification-aware voting" scheme. This produces more reliable pseudo-labels for self-training.
- **Relation to best-of-N:** Directly replaces naive majority voting in best-of-N with verification-aware weighted voting. The code execution acts as a symbolic pre-filter that distinguishes genuinely correct solutions from plausible-looking but wrong ones that happen to be frequent.
- **Key results:** Improvements over TTRL across MATH-500, AMC, and AIME 2024, with larger gains on harder problems (exact numbers not in abstract).

**Sources:**
- [T3RL on arXiv](https://arxiv.org/abs/2603.02203)
- [T3RL on HuggingFace Papers](https://huggingface.co/papers/2603.02203)

---

## 2. FOUNDATIONAL WORKS: Code-Execution for Reasoning

### PAL: Program-Aided Language Models
- **Title:** PAL: Program-aided Language Models
- **Authors:** Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan, Graham Neubig
- **Date/Venue:** arXiv:2211.10435, ICML 2023
- **Core method:** Instead of having the LLM solve math problems end-to-end in natural language, PAL has the LLM decompose the problem into a Python program and delegates actual computation to a Python interpreter. The LLM focuses on semantic understanding and program structure; the interpreter provides guaranteed-correct arithmetic.
- **Relation to best-of-N:** PAL establishes the foundational insight that code execution provides a deterministic verification channel. In a best-of-N setting, solutions that produce executable code with correct outputs can be trivially verified, while prose-only reasoning cannot.
- **Key results:** 72.0% on GSM8K (top-1, surpassing PaLM-540B CoT by 15% absolute), 61.2% on GSM-Hard. Demonstrated across 12 BIG-Bench Hard tasks.

**Source:** [PAL on arXiv](https://arxiv.org/abs/2211.10435)

### ToRA: Tool-Integrated Reasoning Agent
- **Title:** ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving
- **Authors:** Zhibin Gou, Zhihong Shao, Yeyun Gong, et al. (Microsoft Research)
- **Date/Venue:** arXiv:2309.17452, ICLR 2024
- **Core method:** ToRA interleaves natural language reasoning with programmatic tool use (computation libraries, symbolic solvers) in a unified format. Models are trained via imitation learning on interactive tool-use trajectories, followed by output space shaping to refine reasoning behavior. The method achieves fast inference averaging only 1.02 tool interaction rounds per problem.
- **Relation to best-of-N:** ToRA's interleaved format means each candidate solution contains executable code segments whose outputs can be checked, providing a natural verification signal for selection among candidates.
- **Key results:** ToRA-7B reaches 44.6% on MATH (surpassing WizardMath-70B by 22% absolute). ToRA-Code-34B exceeds 50% on MATH, competitive with GPT-4. 13-19% absolute improvements over open-source baselines across 10 math datasets.

**Source:** [ToRA on arXiv](https://arxiv.org/abs/2309.17452)

### MathCoder: Seamless Code Integration in LLMs
- **Title:** MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning
- **Authors:** Ke Wang, Houxing Ren, Aojun Zhou, Zimu Lu, et al.
- **Date/Venue:** arXiv:2310.03731, October 2023
- **Core method:** Fine-tunes open-source LLMs on MathCodeInstruct, a dataset where each solution interleaves natural language, executable code, and code execution results. Inspired by GPT-4 Code Interpreter's seamless reasoning-code-execution loop.
- **Relation to best-of-N:** Each generated solution contains embedded code that can be re-executed for verification. The interleaved format creates a trace where computational claims are checkable.
- **Key results:** 45.2% on MATH, 83.9% on GSM8K. Surpasses ChatGPT-3.5 and PaLM-2; competitive with GPT-4 on MATH.

**Source:** [MathCoder on arXiv](https://arxiv.org/abs/2310.03731)

---

## 3. CODE-EXECUTION-BASED VERIFICATION SYSTEMS

### SymCode: Neurosymbolic Verifiable Code Generation
- **Title:** SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation
- **Authors:** Sina Bagheri Nezhad, Yao Li, Ameeta Agrawal
- **Date/Venue:** arXiv:2510.25975, EACL 2026 Findings
- **Core method:** Reframes mathematical problem-solving as verifiable SymPy code generation. The LLM translates a natural language problem into an executable Python/SymPy script, which is then iteratively refined through a self-debugging loop using deterministic interpreter feedback. Training-free -- works purely through structured prompting.
- **Relation to best-of-N:** Highly relevant. SymCode shifts model failures from opaque logical fallacies to transparent, programmatic errors. In a best-of-N setting, candidates that execute successfully and produce consistent symbolic outputs can be verified deterministically. The self-debugging loop is itself a form of iterative verification.
- **Key results:** Up to 13.6 percentage points improvement (16.8 with SymCode+) over CoT baselines on MATH-500, OlympiadBench, and AIME, with gains increasing on harder problems.

**Source:** [SymCode on arXiv](https://arxiv.org/abs/2510.25975)

### HERMES: Efficient and Verifiable Mathematical Reasoning
- **Title:** HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs
- **Authors:** Azim Ospanov, Zijin Feng, Jiacheng Sun, Haoli Bai, Xin Shen, Farzan Farnia
- **Date/Venue:** arXiv:2511.18760, November 2025
- **Core method:** The first tool-assisted agent that explicitly interleaves informal reasoning with formally verified proof steps in Lean. Uses intermediate formal checking to prevent reasoning drift and employs a memory module for proof continuity across long multi-step chains. Combines exploratory informal reasoning with the rigor of formal theorem-proving verification.
- **Relation to best-of-N:** Uses formal verification (Lean compiler) rather than code execution, but addresses the same core problem: verifying correctness of candidate solutions. HERMES shows that symbolic verification can dramatically reduce the number of candidates needed by filtering out incorrect reasoning early.
- **Key results:** Up to 67% accuracy improvement on AIME'25 while using 80% fewer total inference FLOPs compared to reward-based approaches.

**Source:** [HERMES on arXiv](https://arxiv.org/abs/2511.18760)

### DeepSeekMath-V2: Self-Verifiable Mathematical Reasoning
- **Title:** DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning
- **Authors:** Zhihong Shao et al. (DeepSeek)
- **Date/Venue:** arXiv:2511.22570, November 2025
- **Core method:** Trains an LLM-based verifier for theorem proving, then trains a generator using the verifier as a reward model. Critically introduces a meta-verifier that evaluates the verifier's own analyses, reducing hallucinated errors. The generator is incentivized to self-identify and resolve issues in its proofs before finalizing them.
- **Relation to best-of-N:** The self-verification paradigm means each candidate can be scored by the model's own verification module. The meta-verifier addresses the key failure mode in verification-guided best-of-N: the verifier itself being unreliable. Analysis quality improves from 0.85 to 0.96 with the meta-verifier.
- **Key results:** Gold-level on IMO 2025 and CMO 2024; 118/120 on Putnam 2024 with scaled test-time compute.

**Source:** [DeepSeekMath-V2 on arXiv](https://arxiv.org/abs/2511.22570)

---

## 4. PROCESS REWARD MODELS WITH CODE VERIFICATION

### GenPRM: Generative PRM with Code Verification
- **Title:** GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning
- **Authors:** Jian Zhao, Runze Liu, Kaiyan Zhang, et al.
- **Date/Venue:** arXiv:2504.00891, AAAI 2026
- **Core method:** Redefines process supervision as a generative task. GenPRM performs explicit Chain-of-Thought reasoning with code verification before judging each reasoning step. Uses Relative Progress Estimation (RPE) and a rationale synthesis framework incorporating code verification for training data. Trained on only 23K examples from MATH.
- **Relation to best-of-N:** Directly applicable as a verifier for best-of-N selection. The code verification component provides a deterministic signal within the generative PRM framework. GenPRM can rank candidates by verified step-level correctness.
- **Key results:** 1.5B GenPRM outperforms GPT-4o on ProcessBench; 7B GenPRM surpasses Qwen2.5-Math-PRM-72B (a 10x larger discriminative PRM).

**Source:** [GenPRM on arXiv](https://arxiv.org/abs/2504.00891)

### CodePRM: Execution Feedback-Enhanced Process Reward Model
- **Title:** CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation
- **Authors:** (ACL 2025 Findings)
- **Date/Venue:** ACL 2025 Findings
- **Core method:** Collects thought traces where each step is labeled with derived code pass rates from execution feedback. Trains a PRM that takes both the reasoning process and code execution feedback as input to score individual thought steps. Deployed in a Generate-Verify-Refine (GVR) pipeline.
- **Relation to best-of-N:** The GVR pipeline is essentially a refined best-of-N: generate candidates, verify each step using code execution feedback, and refine failing candidates. Code execution provides the ground-truth signal for step-level scoring.
- **Key results:** Outperforms strong baselines on code generation benchmarks.

**Source:** [CodePRM at ACL Anthology](https://aclanthology.org/2025.findings-acl.428/)

### CodeRM: Dynamic Scaling of Unit Tests for Reward Modeling
- **Title:** Dynamic Scaling of Unit Tests for Code Reward Modeling
- **Authors:** Zeyao Ma, Xiaokang Zhang, Jing Zhang, Jifan Yu, Sijia Luo, Jie Tang
- **Date/Venue:** ACL 2025 (Long Papers)
- **Core method:** Reveals a positive correlation between the number of unit tests and reward signal quality. Trains CodeRM-8B, a lightweight unit test generator, and employs dynamic scaling -- generating more unit tests for harder problems -- to improve verification quality.
- **Relation to best-of-N:** Directly addresses the quality of reward signals used in best-of-N selection via code execution. Shows that scaling the number of verification tests per candidate improves selection accuracy, especially for harder problems.
- **Key results:** 18.43% improvement for Llama3-8B and 3.42% for GPT-4o-mini on HumanEval Plus.

**Source:** [CodeRM on arXiv](https://arxiv.org/abs/2501.01054)

---

## 5. TEST-TIME SCALING AND VERIFICATION CONTEXT

### TTRL: Test-Time Reinforcement Learning (baseline for T3RL)
- **Title:** TTRL: Test-Time Reinforcement Learning
- **Authors:** (PRIME-RL team)
- **Date/Venue:** arXiv:2504.16084, NeurIPS 2025
- **Core method:** Uses majority voting among multiple sampled predictions to create pseudo-labels on unlabeled test data, then uses these as reward signals for RL training at test time. The key insight is that majority voting provides surprisingly effective rewards without ground-truth labels.
- **Relation to best-of-N:** TTRL is the direct predecessor to T3RL. It demonstrates that majority voting (a form of best-of-N) can drive self-improvement, but is vulnerable to "spurious signal amplification" where frequent-but-wrong answers dominate. T3RL fixes this with code-execution verification.
- **Key results:** Boosts Qwen-2.5-Math-7B pass@1 by ~211% on AIME 2024 with only unlabeled test data.

**Source:** [TTRL on arXiv](https://arxiv.org/abs/2504.16084)

### Snell et al.: Scaling LLM Test-Time Compute
- **Title:** Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Model Parameters
- **Authors:** Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar
- **Date/Venue:** arXiv:2408.03314, ICLR 2025 (Oral)
- **Core method:** Analyzes two mechanisms for scaling test-time compute: (1) searching against process-based verifier reward models (PRMs) and (2) adaptively updating the model's response distribution. Introduces compute-optimal strategies that adaptively allocate test-time compute per prompt.
- **Relation to best-of-N:** Establishes the theoretical framework for best-of-N with verification. Shows compute-optimal strategies improve efficiency 2-4x over naive best-of-N. The quality of the verifier is the key bottleneck -- directly motivating symbolic/code-based verification as a stronger signal.
- **Key results:** Compute-optimal test-time scaling can match the performance of a 14x larger model on certain prompts.

**Source:** [Snell et al. on arXiv](https://arxiv.org/abs/2408.03314)

### Scoring Verifiers: Evaluating Synthetic Verification
- **Title:** Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning
- **Authors:** Aleksander Ficek, Somshubra Majumdar, Vahid Noroozi, Boris Ginsburg
- **Date/Venue:** arXiv:2502.13820, COLM 2025
- **Core method:** Proposes benchmarks and metrics to evaluate synthetic verifiers (test case generators, reward models) for code and reasoning tasks. Releases HE-R, HE-R+, MBPP-R, MBPP-R+ benchmarks for scoring and ranking candidate solutions.
- **Relation to best-of-N:** Directly evaluates the ranking quality of different verification methods for selecting among candidates. Shows that reasoning-enhanced models substantially improve test case generation quality, and scaling the number of test cases improves verification accuracy.
- **Key results:** Reasoning models significantly improve synthetic verification quality; more test cases yield better ranking accuracy.

**Source:** [Scoring Verifiers on arXiv](https://arxiv.org/abs/2502.13820)

---

## 6. ADDITIONAL RELATED WORK

### ExecVerify: White-Box RL with Verifiable Stepwise Rewards
- **Title:** ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning
- **Authors:** Lingxiao Tang, He Ye, et al. (Zhejiang University, UCL)
- **Date/Venue:** arXiv:2603.11226, March 2026
- **Core method:** Derives verifiable white-box rewards from execution traces (next-statement prediction, variable value/type prediction). Uses a two-stage training pipeline: first enhances execution reasoning, then transfers to code generation. Note: this paper focuses on code execution reasoning rather than mathematical reasoning specifically.
- **Relation to best-of-N:** Demonstrates that execution traces can provide reliable step-level verification signals, which could be applied to verify mathematical reasoning steps that are expressed as code.
- **Key results:** 7B model matches 32B models on code reasoning benchmarks; up to 5.9% pass@1 improvement on code generation.

**Source:** [ExecVerify on arXiv](https://arxiv.org/abs/2603.11226)

### Agentic Code Reasoning
- **Title:** Agentic Code Reasoning
- **Authors:** Shubham Ugare, Satish Chandra (Meta)
- **Date/Venue:** arXiv:2603.01896, March 2026
- **Core method:** Introduces "semi-formal reasoning" -- structured prompting that requires agents to construct explicit premises, trace execution paths, and derive formal conclusions. Acts as a certificate that prevents the agent from skipping cases or making unsupported claims.
- **Relation to best-of-N:** Demonstrates that structured code reasoning without execution can still serve as verification. The semi-formal certificates provide verifiable traces that could be used to filter/rank candidates in a best-of-N setting.
- **Key results:** Accuracy improves from 78% to 88% on patch equivalence verification; 87% on RubberDuckBench (9 point gain).

**Source:** [Agentic Code Reasoning on arXiv](https://arxiv.org/abs/2603.01896)

---

## SYNTHESIS: The Landscape

The field can be organized along two axes:

**Axis 1 -- What is verified:**
- Final answer only (majority voting, ORM)
- Step-level process (PRM, GenPRM, CodePRM)
- Full symbolic trace (PAL, SymCode, HERMES, T3RL)

**Axis 2 -- How verification is performed:**
- Neural/learned verifiers (PRM, ORM, ThinkPRM)
- Code execution against test cases (PAL, ToRA, MathCoder, CodeRM)
- Formal proof checking (HERMES via Lean, DeepSeekMath-V2)
- Hybrid: neural + code execution (T3RL, GenPRM, CodePRM)

T3RL sits at the intersection of step-level verification and hybrid neural+code execution, making it directly relevant to your symbolic pre-filtering proposal. The key gap it fills is using code execution not just for generating answers (as in PAL/ToRA) but specifically for filtering/reweighting candidates in the best-of-N selection process during test-time self-improvement.

The most important papers for your related work section are likely: T3RL, TTRL (as baseline), GenPRM (code-verified PRM), SymCode (neurosymbolic verification), HERMES (formal verification for efficiency), Snell et al. (compute-optimal best-of-N framework), and the foundational PAL/ToRA works.

Sources:
- [T3RL - arXiv:2603.02203](https://arxiv.org/abs/2603.02203)
- [TTRL - arXiv:2504.16084](https://arxiv.org/abs/2504.16084)
- [PAL - arXiv:2211.10435](https://arxiv.org/abs/2211.10435)
- [ToRA - arXiv:2309.17452](https://arxiv.org/abs/2309.17452)
- [MathCoder - arXiv:2310.03731](https://arxiv.org/abs/2310.03731)
- [SymCode - arXiv:2510.25975](https://arxiv.org/abs/2510.25975)
- [HERMES - arXiv:2511.18760](https://arxiv.org/abs/2511.18760)
- [DeepSeekMath-V2 - arXiv:2511.22570](https://arxiv.org/abs/2511.22570)
- [GenPRM - arXiv:2504.00891](https://arxiv.org/abs/2504.00891)
- [CodePRM - ACL 2025 Findings](https://aclanthology.org/2025.findings-acl.428/)
- [CodeRM - arXiv:2501.01054](https://arxiv.org/abs/2501.01054)
- [Snell et al. - arXiv:2408.03314](https://arxiv.org/abs/2408.03314)
- [Scoring Verifiers - arXiv:2502.13820](https://arxiv.org/abs/2502.13820)
- [ExecVerify - arXiv:2603.11226](https://arxiv.org/abs/2603.11226)
- [Agentic Code Reasoning - arXiv:2603.01896](https://arxiv.org/abs/2603.01896)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "249bfb91-014f-4804-b9e4-f65989202fb9",
  "isSidechain": true,
  "agentId": "a40596f27d93c653d",
  "requestId": "req_011CauLfHVBDQd1smxSHKgXG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40c05100-31cd-4e04-805d-3e56864973ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135qNzfz8MwLqwctDMi1DTT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1836,
      "cache_read_input_tokens": 33266,
      "output_tokens": 5495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1836
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5495,
          "cache_read_input_tokens": 33266,
          "cache_creation_input_tokens": 1836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1836,
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
