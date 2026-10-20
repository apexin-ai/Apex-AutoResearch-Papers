# Research conversation: I'm reviewing a research proposal about learned execution trace filtering for code repair. I need to verify two key comp

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6f43a06f31ed5e40.jsonl`
- **Structured JSON:** [`faf6c77623ad2b8b8578.json`](../../sessions/fa/faf6c77623ad2b8b8578.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-11T23:18:54.188Z_

I'm reviewing a research proposal about learned execution trace filtering for code repair. I need to verify two key competitor papers and check if the proposal's characterization is accurate:

1. **Squeez (arXiv 2604.04979)**: The proposal claims it "trains Qwen 3.5 2B with LoRA for task-conditioned line-level pruning of heterogeneous tool outputs (including stack traces and build logs), achieving 92% token removal with 0.86 recall across 27 tool families." Search for and verify this paper exists and these claims are accurate.

2. **SWE-Pruner (arXiv 2601.16746)**: The proposal claims it "trains a 0.6B CRF-based model on 61K synthetic data for task-aware code context pruning (23-54% token reduction on SWE-bench Verified while maintaining success rates)."

Search queries to use:
- arxiv 2604.04979 Squeez task-conditioned pruning
- arxiv 2601.16746 SWE-Pruner context pruning
- "Squeez" coding agent tool output pruning 2026
- "SWE-Pruner" self-adaptive context pruning
- site:arxiv.org 2604.04979
- site:arxiv.org 2601.16746

Also search for any OTHER learned compression/pruning methods for code that the proposal might be missing:
- learned context compression code LLM 2025 2026
- context pruning coding agent arxiv 2026
- execution trace compression code repair 2026

Report concisely: do these papers exist, are the claims accurate, and are there any other competitors the proposal is missing?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "c86f35ca-c9ed-4cc9-98b7-9d4b1d25d965",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:18:54.196Z_

```json
{
  "parentUuid": "c86f35ca-c9ed-4cc9-98b7-9d4b1d25d965",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
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
  "uuid": "e653a0b4-50d7-444c-997d-c5085d4de6aa",
  "timestamp": "2026-05-11T23:18:54.196Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:18:56.801Z_



I'll search for both papers and related work using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e653a0b4-50d7-444c-997d-c5085d4de6aa",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011CawdtLsBLVW3KtNWwQX2d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31c74e81-b48e-470b-a79b-cf60e23a4203",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1L3PK4ap1M37TcagkDZCz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 944,
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

_source line 4 · 2026-05-11T23:18:56.974Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EPz2Ag1D2xQjF9R1NiPzrP`</summary>

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
  "parentUuid": "31c74e81-b48e-470b-a79b-cf60e23a4203",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011CawdtLsBLVW3KtNWwQX2d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9a6e4bd-4012-484f-89e7-ac996b639457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1L3PK4ap1M37TcagkDZCz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 8223,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 944,
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

_source line 5 · 2026-05-11T23:18:56.977Z_

<details><summary>↩ Tool result · `toolu_01EPz2Ag1D2xQjF9R1NiPzrP`</summary>

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
  "parentUuid": "c9a6e4bd-4012-484f-89e7-ac996b639457",
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "23dcefeb-fe9f-4f29-bec6-c022d67b7a1d",
  "sourceToolAssistantUUID": "c9a6e4bd-4012-484f-89e7-ac996b639457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:19:05.624Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23dcefeb-fe9f-4f29-bec6-c022d67b7a1d",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011CawdtYsk1ZYSMbSapkx12",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df1bc36a-604b-418f-9e33-0128cc6c8426",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfSnCU1f2hrVXvch2s3Z8w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 7 · 2026-05-11T23:19:06.143Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UnyUjrJyAhnrsbavMQPzUF`</summary>

```json
{
  "query": "arxiv 2604.04979 Squeez task-conditioned pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df1bc36a-604b-418f-9e33-0128cc6c8426",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011CawdtYsk1ZYSMbSapkx12",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "804bdef8-05aa-4613-ba1a-998a96ed63dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfSnCU1f2hrVXvch2s3Z8w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9167,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1409
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 81,
          "cache_read_input_tokens": 9167,
          "cache_creation_input_tokens": 1409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1409,
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

_source line 8 · 2026-05-11T23:19:13.929Z_

<details><summary>↩ Tool result · `toolu_01UnyUjrJyAhnrsbavMQPzUF`</summary>

```text
Web search results for query: "arxiv 2604.04979 Squeez task-conditioned pruning"

Links: [{"title":"Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://arxiv.org/html/2604.04979"},{"title":"[2604.04979] Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://arxiv.org/abs/2604.04979"},{"title":"Paper page - Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://huggingface.co/papers/2604.04979"},{"title":"Frustratingly Easy Task-aware Pruning for Large Language Models","url":"https://arxiv.org/html/2510.22489v1"},{"title":"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://arxiv.org/html/2509.12464v1"},{"title":"Collaborative Multi-Mode Pruning for Vision-Language Models","url":"https://arxiv.org/html/2604.02956"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=767&show=2000"},{"title":"Layer Pruning with Consensus: A Triple-Win Solution","url":"https://arxiv.org/html/2411.14345v1"},{"title":"FastForward Pruning: Efficient LLM Pruning via Single-Step Reinforcement Learning","url":"https://arxiv.org/html/2511.18977"},{"title":"Task Specific Pruning with LLM-Sieve: How Many Parameters Does Your Task Really Need?","url":"https://arxiv.org/html/2505.18350v1"}]

Based on the search results, here's information about arxiv paper 2604.04979:

## Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents

The paper, authored by Ádám Kovács from KR Labs, focuses on task-conditioned tool-output pruning for coding agents that work over streams of file reads, grep hits, stack traces, build logs, API responses, and version-control history.

### Problem and Approach

Only a small fraction of tokens in tool observations is relevant to the next decision, yet agents often have to re-read the entire output. The paper studies task-conditioned tool-output pruning: given a focused query and one tool output, the goal is to return the smallest verbatim evidence block the agent should inspect next.

### Methodology and Results

The authors introduce a benchmark of 11,477 examples built from SWE-bench repository interactions and synthetic multi-ecosystem tool outputs with a manually curated 618-example test set, and fine-tune Qwen 3.5 2B with LoRA and compare it against larger zero-shot models and heuristic pruning baselines.

Their model reaches 0.86 recall and 0.80 F1 while removing 92% of input tokens, outperforming zero-shot Qwen 3.5 35B A3B by 11 recall points and all heuristic baselines by a wide margin.

### Availability

The model and evaluation code are available on GitHub, and the released model and dataset are available on Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "804bdef8-05aa-4613-ba1a-998a96ed63dd",
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "96ffee22-739f-4306-b4c5-2c515182f728",
  "sourceToolAssistantUUID": "804bdef8-05aa-4613-ba1a-998a96ed63dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-11T23:19:16.397Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XJbLUYMBqWmFzbaeXK9wYM`</summary>

```json
{
  "query": "arxiv 2601.16746 SWE-Pruner context pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96ffee22-739f-4306-b4c5-2c515182f728",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011CawduoCEqCPn3sqa7SVs2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e46f73e9-4144-47dd-9de5-ebebbaf3ea9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETGVZzMoBb8vQSLcuDtNhw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 10576,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 10576,
          "cache_creation_input_tokens": 910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 910,
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

_source line 10 · 2026-05-11T23:19:24.541Z_

<details><summary>↩ Tool result · `toolu_01XJbLUYMBqWmFzbaeXK9wYM`</summary>

```text
Web search results for query: "arxiv 2601.16746 SWE-Pruner context pruning"

Links: [{"title":"[2601.16746] SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/abs/2601.16746"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/html/2601.16746v1"},{"title":"GitHub - Ayanami1314/swe-pruner · GitHub","url":"https://github.com/Ayanami1314/swe-pruner"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"Paper page - SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://huggingface.co/papers/2601.16746"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.16746v1"},{"title":"ayanami-kitasan/code-pruner · Hugging Face","url":"https://huggingface.co/ayanami-kitasan/code-pruner"},{"title":"(PDF) SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.researchgate.net/publication/400071923_SWE-Pruner_Self-Adaptive_Context_Pruning_for_Coding_Agents"},{"title":"Software Engineering on X: \"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents Yuhang Wang, Yuling Shi, Mo Yang, Rongrui Zhang, Shilin He, Heng Lian, Yuting Chen, Siyu Ye, Kai Cai, Xiaodong Gu https://t.co/7gw9yLhyMf [𝚌𝚜.𝚂𝙴 𝚌𝚜.𝙲𝙻] https://t.co/kRlOYQc5jb\" / X","url":"https://x.com/ComputerPapers/status/2015694356875727079"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding ...","url":"https://liner.com/review/swepruner-selfadaptive-context-pruning-for-coding-agents"}]

Based on the search results, here's what I found about arXiv paper 2601.16746 - SWE-Pruner:

## Overview

SWE-Pruner is a self-adaptive context pruning framework tailored for coding agents. The paper was submitted on January 23, 2026 and last revised on February 4, 2026.

## Problem Statement

LLM agents have demonstrated remarkable capabilities in software development, but their performance is hampered by long interaction contexts, which incur high API costs and latency. While various context compression approaches such as LongLLMLingua have emerged to tackle this challenge, they typically rely on fixed metrics such as PPL, ignoring the task-specific nature of code understanding. As a result, they frequently disrupt syntactic and logical structure and fail to retain critical implementation details.

## Approach

Drawing inspiration from how human programmers "selectively skim" source code during development and debugging, SWE-Pruner performs task-aware adaptive pruning for long contexts. Given the current task, the agent formulates an explicit goal (e.g., "focus on error handling") as a hint to guide the pruning targets. A lightweight neural skimmer (0.6B parameters) is trained to dynamically select relevant lines from the surrounding context given the goal.

## Results

Evaluations across four benchmarks and multiple models validate SWE-Pruner's effectiveness in various scenarios, achieving 23-54% token reduction on agent tasks like SWE-Bench Verified while even improving success rates, and up to 14.84x compression on single-turn tasks like LongCodeQA with minimal performance impact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e46f73e9-4144-47dd-9de5-ebebbaf3ea9a",
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "40bf1b37-e43b-4929-962f-75812fd75976",
  "sourceToolAssistantUUID": "e46f73e9-4144-47dd-9de5-ebebbaf3ea9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-11T23:19:26.887Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013zPtLu2X3DJY7WvV5fYojm`</summary>

```json
{
  "query": "learned context compression code LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40bf1b37-e43b-4929-962f-75812fd75976",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011CawdvaZk2isM4awJTUme3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49d52c96-a5ea-4838-b793-8614326aefa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tuXAN3HxYcq72mLd9eVpK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 11486,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1138
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 11486,
          "cache_creation_input_tokens": 1138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1138,
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

_source line 12 · 2026-05-11T23:19:35.698Z_

<details><summary>↩ Tool result · `toolu_013zPtLu2X3DJY7WvV5fYojm`</summary>

```text
Web search results for query: "learned context compression code LLM 2025 2026"

Links: [{"title":"A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression","url":"https://arxiv.org/html/2604.19572v1"},{"title":"Compressing Code Context for LLM-based Issue Resolution","url":"https://arxiv.org/html/2603.28119"},{"title":"Compresr: LLM context compression for better accuracy | Y Combinator","url":"https://www.ycombinator.com/companies/compresr"},{"title":"Reimagining LLM Memory: Using Context as Training Data Unlocks Models That Learn at Test-Time | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/reimagining-llm-memory-using-context-as-training-data-unlocks-models-that-learn-at-test-time/"},{"title":"[2510.08907] Autoencoding-Free Context Compression for LLMs via Contextual Semantic Anchors","url":"https://arxiv.org/abs/2510.08907"},{"title":"[2603.28119] Compressing Code Context for LLM-based Issue Resolution","url":"https://arxiv.org/abs/2603.28119"},{"title":"LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models","url":"https://llmlingua.com/llmlingua.html"},{"title":"Pretraining Context Compressor for Large Language ...","url":"https://aclanthology.org/2025.acl-long.1394.pdf"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"ACON: Optimizing Context Compression for Long-horizon LLM Agents | OpenReview","url":"https://openreview.net/forum?id=7JbSwX6bNL"}]

Based on the search results, here's what I found about learned context compression for code LLMs in 2025-2026:

## Key Recent Developments

SWE-Pruner (Wang et al., 2026) is a representative learning-based approach with more adaptive pruning, but it requires additional fine-tuning and is largely tailored to SWE-style tasks.

SWEzze combines Oracle-guided Code Distillation (OCD), a context distillation algorithm that uses genetic search and delta debugging, with a lightweight model that learns to compress code context at inference time. Evaluated on SWE-bench Verified across three frontier LLMs, SWEzze maintains a stable compression rate of about 6 times across models, reduces the total token budget by 51.8%-71.3% relative to the uncompressed setting, and improves issue resolution rates by 5.0%-9.2%.

## Broader Context Compression Methods

TACO's learned compression rules consistently transfer well, demonstrating that it provides a general and scalable solution for terminal-agent context compression.

Semantic-Anchor Compression (SAC) shifts from autoencoding task based compression to an architecture equipped with compression capability, where anchor tokens from the original context are directly selected and contextual information is aggregated into their key-value representations.

The PCC Framework condenses long context into embedding-based memory slots for fast and accurate inference with a downstream LLM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49d52c96-a5ea-4838-b793-8614326aefa6",
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "30877aa7-b3ff-4346-adf9-e7244b6df259",
  "sourceToolAssistantUUID": "49d52c96-a5ea-4838-b793-8614326aefa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-11T23:19:40.750Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sfv82an7junyvU5DEsnCBr`</summary>

```json
{
  "query": "\"SWE-Pruner\" CRF model architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30877aa7-b3ff-4346-adf9-e7244b6df259",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011CawdwQFQcJ7GgyRhGSDs2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56419d37-f224-4761-8bde-106949ac3484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UbgeNzDCDtzzxhqBQA5ee",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 931,
      "cache_read_input_tokens": 12624,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 931
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 12624,
          "cache_creation_input_tokens": 931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 931,
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

_source line 14 · 2026-05-11T23:19:45.327Z_

<details><summary>↩ Tool result · `toolu_01Sfv82an7junyvU5DEsnCBr`</summary>

```text
Web search results for query: ""SWE-Pruner" CRF model architecture"

Links: [{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/html/2601.16746v1"},{"title":"(PDF) SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.researchgate.net/publication/400071923_SWE-Pruner_Self-Adaptive_Context_Pruning_for_Coding_Agents"},{"title":"GitHub - Ayanami1314/swe-pruner · GitHub","url":"https://github.com/Ayanami1314/swe-pruner"},{"title":"Paper page - SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://huggingface.co/papers/2601.16746"},{"title":"ayanami-kitasan/code-pruner · Hugging Face","url":"https://huggingface.co/ayanami-kitasan/code-pruner"},{"title":"SWE-Pruner Breaks the Context Wall: How to Slash AI Coding Agent Costs by 54% | Efficient Coder","url":"https://www.xugj520.cn/en/archives/swe-pruner-ai-coding-agent-cost-reduction.html"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.16746v1"},{"title":"[2601.16746] SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/abs/2601.16746"},{"title":"@YerbaPage on Hugging Face: \"🔥 SWE-Pruner can save up to 40% of your Claude Code cost without sacrificing…\"","url":"https://huggingface.co/posts/YerbaPage/493697712808947"}]

Based on the search results, here's information about the SWE-Pruner CRF model architecture:

## SWE-Pruner Model Architecture

The model consists of a lightweight reranker backbone with multi-layer feature fusion, followed by dual heads for pruning and reranking. The pruning head employs a CRF layer to model structured retention decisions, while the reranking head produces document-level relevance scores.

### CRF Implementation

The model uses line-level retention decisions via Conditional Random Fields (CRF), trained on synthetic data to make structured pruning decisions. The architecture is designed as a lightweight neural skimmer (0.6B parameters) that dynamically selects relevant code lines based on task-specific goals.

This CRF-based approach enables SWE-Pruner to preserve the syntactic and logical structure of code while performing adaptive context pruning for coding agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56419d37-f224-4761-8bde-106949ac3484",
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "ce5362e6-9190-44bb-9b98-462d0f739628",
  "sourceToolAssistantUUID": "56419d37-f224-4761-8bde-106949ac3484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-11T23:19:47.983Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017GjyR3WQW1kZLmTwQdnFMZ`</summary>

```json
{
  "query": "\"Squeez\" coding agent tool output pruning 27 tool families"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce5362e6-9190-44bb-9b98-462d0f739628",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011Cawdx7PgAgkycxU6M9hax",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8d80907-a158-4623-9971-c1032100e2ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyLbPPtxXmuPi843MNESjX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 13555,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 857
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 13555,
          "cache_creation_input_tokens": 857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 857,
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

_source line 16 · 2026-05-11T23:19:56.475Z_

<details><summary>↩ Tool result · `toolu_017GjyR3WQW1kZLmTwQdnFMZ`</summary>

```text
Web search results for query: ""Squeez" coding agent tool output pruning 27 tool families"

Links: [{"title":"Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://arxiv.org/html/2604.04979"},{"title":"Paper page - Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://huggingface.co/papers/2604.04979"},{"title":"[2604.04979] Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://arxiv.org/abs/2604.04979"},{"title":"GitHub - KRLabsOrg/squeez: Squeeze verbose LLM agent tool output down to only the relevant lines · GitHub","url":"https://github.com/KRLabsOrg/squeez"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/html/2601.16746"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"GitHub - Opencode-DCP/opencode-dynamic-context-pruning: Dynamic context pruning plugin for OpenCode - intelligently manages conversation context to optimize token usage · GitHub","url":"https://github.com/Opencode-DCP/opencode-dynamic-context-pruning"},{"title":"squeez - crates.io: Rust Package Registry","url":"https://crates.io/crates/squeez"},{"title":"Context Engineering: The Invisible Discipline Keeping AI Agents from Drowning in Their Own Memory | by Juan C Olamendy | Medium","url":"https://medium.com/@juanc.olamendy/context-engineering-the-invisible-discipline-keeping-ai-agents-from-drowning-in-their-own-memory-c0283ca6a954"},{"title":"GitHub - ai-boost/awesome-harness-engineering: Awesome list for AI agent harness engineering: tools, patterns, evals, memory, MCP, permissions, observability, and orchestration. · GitHub","url":"https://github.com/ai-boost/awesome-harness-engineering"}]

Based on the search results, I found comprehensive information about Squeez and its tool output pruning capabilities:

## Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents

Squeez is a task-conditioned tool-output pruner for coding agents, with a benchmark that pairs grounded span annotations over 27 tool types with real SWE-bench workflows and synthetic multi-ecosystem observations.

### Overview

Coding agents repeatedly consume long tool observations even though only a small fraction of each observation matters for the next step. Squeez studies task-conditioned tool-output pruning: given a focused query and one tool output, it returns the smallest verbatim evidence block the agent should inspect next.

### Dataset and Performance

The benchmark consists of 11,477 examples built from SWE-bench repository interactions and synthetic multi-ecosystem tool outputs, with a manually curated 618-example test set.

The researchers fine-tuned Qwen 3.5 2B with LoRA and compared it against larger zero-shot models and heuristic pruning baselines. The model reaches 0.86 recall and 0.80 F1 while removing 92% of input tokens, outperforming zero-shot Qwen 3.5 35B A3B by 11 recall points and all heuristic baselines by a wide margin.

### Tool Support

Squeez is trained on 27 types of tool output from real SWE-bench workflows and synthetic multi-ecosystem observations.

### Integration and Usage

The tool is exposed both as a CLI that can consume piped tool output and as a vLLM-served model, so existing coding agents can insert pruning before the next reasoning step without changing their core planning logic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8d80907-a158-4623-9971-c1032100e2ff",
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "4cfdfcf9-17b8-415d-a833-228c28a425b5",
  "sourceToolAssistantUUID": "b8d80907-a158-4623-9971-c1032100e2ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-11T23:19:59.317Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XyS6DX8rqX769sDsV6tYEm`</summary>

```json
{
  "query": "SWE-Pruner 61K synthetic training data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cfdfcf9-17b8-415d-a833-228c28a425b5",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011Cawdxw6L46fzYT3KDZBFd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c04df43-1780-44b7-9086-1f3d559e4af2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYLTqAjU2U32beoePonAyk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 14412,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1049
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 14412,
          "cache_creation_input_tokens": 1049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1049,
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

_source line 18 · 2026-05-11T23:20:06.249Z_

<details><summary>↩ Tool result · `toolu_01XyS6DX8rqX769sDsV6tYEm`</summary>

```text
Web search results for query: "SWE-Pruner 61K synthetic training data"

Links: [{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/html/2601.16746v1"},{"title":"GitHub - Ayanami1314/swe-pruner · GitHub","url":"https://github.com/Ayanami1314/swe-pruner"},{"title":"(PDF) SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.researchgate.net/publication/400071923_SWE-Pruner_Self-Adaptive_Context_Pruning_for_Coding_Agents"},{"title":"Paper page - SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://huggingface.co/papers/2601.16746"},{"title":"SWE-Pruner Breaks the Context Wall: How to Slash AI Coding Agent Costs by 54% | Efficient Coder","url":"https://www.xugj520.cn/en/archives/swe-pruner-ai-coding-agent-cost-reduction.html"},{"title":"[2601.16746] SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/abs/2601.16746"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.16746v1"},{"title":"Synthetic Repo-level Bug Dataset for Training Automated Program Repair Models | SWE-Synth","url":"https://swesynth.com/"},{"title":"@YerbaPage on Hugging Face: \"🔥 SWE-Pruner can save up to 40% of your Claude Code cost without sacrificing…\"","url":"https://huggingface.co/posts/YerbaPage/493697712808947"}]

Based on the search results, here's what I found about SWE-Pruner and its 61K synthetic training data:

## Overview

SWE-Pruner trains a lightweight 0.6B pruning model on 61K synthetic data, enabling adaptive selection conditioned on given goals. SWE-Pruner is a self-adaptive context pruning framework tailored for coding agents, drawing inspiration from how human programmers "selectively skim" source code during development and debugging.

## How the 61K Dataset Was Created

The synthetic training data was generated through a sophisticated process. Training data comes from high-quality GitHub repositories using a Teacher-Student Paradigm where a powerful 30B teacher model is used to synthesize task-oriented queries and generate line-level masks, covering 9 common agent tasks like Code Debugging, Feature Addition, and Refactoring.

## Purpose and Performance

By integrating as middleware within agentic workflows, SWE-Pruner reduces token usage by 23–38% on SWE-Bench and 29–54% on SWE-QA, achieving up to 14.84× compression on single-turn benchmarks.

## Availability

The 61k training dataset for Python was made available on Google Drive on March 8, 2026. The project has also been accepted to ACL 2026 Main Conference on April 6, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c04df43-1780-44b7-9086-1f3d559e4af2",
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "5cd7983e-44a1-4bc3-be5b-fb4edacef14f",
  "sourceToolAssistantUUID": "5c04df43-1780-44b7-9086-1f3d559e4af2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-11T23:20:08.994Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011dF9ni79arN4V865mZGHbs`</summary>

```json
{
  "query": "context pruning coding agent arxiv 2026 execution trace compression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cd7983e-44a1-4bc3-be5b-fb4edacef14f",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011CawdyetXuqfR6X3LbLGR4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d95b3aee-b0a8-4ae2-8dec-fdacba7f6009",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZXucZML7vsuxtnY8CDygL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 15461,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 965
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 15461,
          "cache_creation_input_tokens": 965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 965,
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

_source line 20 · 2026-05-11T23:20:17.885Z_

<details><summary>↩ Tool result · `toolu_011dF9ni79arN4V865mZGHbs`</summary>

```text
Web search results for query: "context pruning coding agent arxiv 2026 execution trace compression"

Links: [{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression","url":"https://arxiv.org/html/2604.19572v1"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/html/2601.16746"},{"title":"GitHub - VoltAgent/awesome-ai-agent-papers: A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, and autonomous systems. · GitHub","url":"https://github.com/VoltAgent/awesome-ai-agent-papers"},{"title":"PAACE: A Plan-Aware Automated Agent Context Engineering Framework","url":"https://arxiv.org/html/2512.16970"},{"title":"Acon: Optimizing Context Compression for Long-horizon LLM Agents","url":"https://arxiv.org/html/2510.00615v1"},{"title":"AI Agent Context Compression: Strategies for Long-Running Sessions | Zylos Research","url":"https://zylos.ai/research/2026-02-28-ai-agent-context-compression-strategies"},{"title":"ContextEvolve: Multi-Agent Context Compression for Systems Code Optimization","url":"https://www.arxiv.org/pdf/2602.02597"},{"title":"ContextEvolve: Multi-Agent Context Compression for Systems Code Optimization","url":"https://arxiv.org/html/2602.02597v1"},{"title":"SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios","url":"https://arxiv.org/html/2512.18470v5"}]

Based on the search results, here's what I found regarding context pruning, coding agents, and execution trace compression from recent 2026 arXiv papers:

## Key Research Papers

**SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents**

SWE-Pruner is a self-adaptive context pruning framework tailored for coding agents that draws inspiration from how human programmers "selectively skim" source code during development and debugging. The approach trains a lightweight 0.6B pruning model on 61K synthetic data, enabling adaptive selection conditioned on given goals, and operates at line-level granularity to preserve syntactic and structural integrity while achieving precise compression.

On SWE-Bench Verified, SWE-Pruner achieves substantial token reductions of 23–38% across models while maintaining nearly identical success rates, with interaction rounds decreasing by 18–26%.

**Related Context Compression Frameworks**

ContextEvolve is a multi-agent framework that compresses raw interaction logs into a refined optimization context, thereby enabling high search efficiency. PAACE is a framework for plan-aware context engineering, unifying context pruning, summarization, rewriting, compression, re-injection, and task refinement.

ACON (Agent Context Optimization) is a unified framework that optimally compresses both environment observations and interaction histories into concise yet informative condensations.

These papers represent a broader shift toward treating execution trace compression and context management as critical components for long-horizon coding agent performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d95b3aee-b0a8-4ae2-8dec-fdacba7f6009",
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "6c650e92-a20a-4ddc-8339-7d07cf4a2b11",
  "sourceToolAssistantUUID": "d95b3aee-b0a8-4ae2-8dec-fdacba7f6009",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-11T23:20:20.893Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UdgTEXCdykRsoAEpuiQrPf`</summary>

```json
{
  "query": "Compressing Code Context LLM Issue Resolution arxiv 2603.28119"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c650e92-a20a-4ddc-8339-7d07cf4a2b11",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011CawdzWcUo57Zj5hfEcY7G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a17a6714-9078-4030-9000-84605d68433f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7DJ2e2cUhrApipPSvLm7v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1026,
      "cache_read_input_tokens": 16426,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1026
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 16426,
          "cache_creation_input_tokens": 1026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1026,
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

_source line 22 · 2026-05-11T23:20:28.243Z_

<details><summary>↩ Tool result · `toolu_01UdgTEXCdykRsoAEpuiQrPf`</summary>

```text
Web search results for query: "Compressing Code Context LLM Issue Resolution arxiv 2603.28119"

Links: [{"title":"[2603.28119] Compressing Code Context for LLM-based Issue Resolution","url":"https://arxiv.org/abs/2603.28119"},{"title":"Compressing Code Context for LLM-based Issue Resolution","url":"https://arxiv.org/html/2603.28119"},{"title":"Compressing Code Context for LLM-based Issue Resolution Haoxiang Jia","url":"https://arxiv.org/pdf/2603.28119"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"CompLLM: Compression for Long Context Q&A","url":"https://arxiv.org/html/2509.19228v1"},{"title":"GitHub - liyucheng09/Selective_Context: Compress your input to ChatGPT or other LLMs, to let them process 2x more content and save 40% memory and GPU time. · GitHub","url":"https://github.com/liyucheng09/Selective_Context"},{"title":"LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression","url":"https://arxiv.org/html/2310.06839v2"},{"title":"In-context Autoencoder for Context Compression in a Large Language Model","url":"https://arxiv.org/html/2307.06945v3"},{"title":"Enhancing and Accelerating Large Language Models via Instruction-Aware Contextual Compression","url":"https://arxiv.org/html/2408.15491v1"},{"title":"Developing Adaptive Context Compression Techniques for Large Language Models (LLMs) in Long-Running Interactions","url":"https://arxiv.org/html/2603.29193"}]

Based on the web search results, here's what I found about the arXiv paper 2603.28119:

## Paper Summary

The paper is titled "Compressing Code Context for LLM-based Issue Resolution" by Haoxiang Jia, Earl T. Barr, and Sergey Mechtaev, and was submitted on March 30, 2026.

## Problem Statement

Large Language Models (LLMs) are now capable of resolving real-world GitHub issues. However, current approaches overapproximate the code context and suffer from two compounding problems: the prohibitive cost of processing massive inputs, and low effectiveness as noise floods the context window and distracts the model from the bug-fixing signal.

## Proposed Solution

The paper proposes a novel framework consisting of two components. They use distilled data to fine-tune SWEzze, a lightweight model that learns to compress code context at inference time, filtering noise and combating distraction while preserving fix ingredients.

## Results

Evaluated on SWE-bench Verified across three frontier LLMs, SWEzze maintains a stable compression rate of about 6 times across models, reduces the total token budget by 51.8%-71.3% relative to the uncompressed setting, improves issue resolution rates by 5.0%-9.2%, and delivers the best overall balance among effectiveness, compression ratio, and latency compared with state-of-the-art context compression baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a17a6714-9078-4030-9000-84605d68433f",
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "656addeb-7ad4-4422-b0df-3dd4d00472bc",
  "sourceToolAssistantUUID": "a17a6714-9078-4030-9000-84605d68433f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-11T23:20:30.815Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GH3bdN1hb4DmnNMkqxe4mz`</summary>

```json
{
  "query": "TACO terminal agent observational context compression arxiv 2604.19572"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "656addeb-7ad4-4422-b0df-3dd4d00472bc",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011Cawe1GyTxQG2F4Zixwp2E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed0514d3-a21f-4aab-964b-09d72ea5139c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N47Sc3jjU7optvoCottqsq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 925,
      "cache_read_input_tokens": 17452,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 925
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 17452,
          "cache_creation_input_tokens": 925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 925,
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

_source line 24 · 2026-05-11T23:20:37.997Z_

<details><summary>↩ Tool result · `toolu_01GH3bdN1hb4DmnNMkqxe4mz`</summary>

```text
Web search results for query: "TACO terminal agent observational context compression arxiv 2604.19572"

Links: [{"title":"[2604.19572] A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression","url":"https://arxiv.org/abs/2604.19572"},{"title":"A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression","url":"https://arxiv.org/html/2604.19572"},{"title":"Paper page - A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression","url":"https://huggingface.co/papers/2604.19572"},{"title":"[2509.19572] Analyzing α-divergence in Gaussian Rate-Distortion-Perception Theory","url":"https://arxiv.org/abs/2509.19572"},{"title":"[2604.26622] OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory","url":"https://arxiv.org/abs/2604.26622"},{"title":"Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents","url":"https://arxiv.org/html/2604.15877"},{"title":"Acon: Optimizing Context Compression for Long-horizon LLM Agents","url":"https://arxiv.org/html/2510.00615v1"},{"title":"Taco Cohen","url":"https://tacocohen.wordpress.com/"},{"title":"[2604.13725] On the Effectiveness of Context Compression for Repository-Level Tasks: An Empirical Investigation","url":"https://arxiv.org/abs/2604.13725"},{"title":"ACON: OPTIMIZING CONTEXT COMPRESSION FOR LONG-HORIZON LLM AGENTS Minki Kang1∗","url":"https://arxiv.org/pdf/2510.00615"}]

I found the paper you're looking for. Here are the key details about TACO:

## Overview

TACO is a plug-and-play, self-evolving Terminal Agent Compression framework that automatically discovers and refines compression rules from interaction trajectories for existing terminal agents.

## Problem Addressed

As terminal agents scale to long-horizon, multi-turn workflows, a key bottleneck is the accumulation of noisy terminal observations in the interaction history. Retaining raw observations preserves useful environment feedback, but also leads to context saturation and high token cost; conversely, naive compression may discard task-critical signals needed for subsequent actions.

## Key Features

TACO is a plug-and-play, training-free, self-evolving Terminal Agent Compression framework. It automatically discovers, refines, and reuses structured compression rules from interaction trajectories, enabling workflow-adaptive filtering of low-value terminal outputs while preserving task-relevant observations.

## Results

Experiments on TerminalBench and four additional terminal-related benchmarks show that TACO consistently improves task performance and token efficiency across agent scaffolds and backbone models. On TerminalBench, TACO yields 1%–4% accuracy gains across strong agentic models and improves accuracy by around 2%–3% under the same token budget.

The paper was published on April 21, 2026, and the code is publicly available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed0514d3-a21f-4aab-964b-09d72ea5139c",
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "51ebc624-8ef2-4f68-a438-4cbb77b737a3",
  "sourceToolAssistantUUID": "ed0514d3-a21f-4aab-964b-09d72ea5139c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-11T23:20:42.594Z_

Now let me also check for the effectiveness claims on the context compression for repo-level tasks paper, since it's specifically about empirical investigation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51ebc624-8ef2-4f68-a438-4cbb77b737a3",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011Cawe1zb1VHAniFFdVQjTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8eb59e19-4c75-471f-b8fa-3ceb35a229a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjzSazSA2ovzQps8FZua5X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 18377,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 877
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 18377,
          "cache_creation_input_tokens": 877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 877,
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

### Tool call

_source line 26 · 2026-05-11T23:20:42.619Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XkAxoQVjdnJFmXV9WAxVo4`</summary>

```json
{
  "query": "arxiv 2604.13725 context compression repository level tasks empirical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8eb59e19-4c75-471f-b8fa-3ceb35a229a6",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011Cawe1zb1VHAniFFdVQjTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86ec04ba-41ff-4604-87bb-c2376ff01d90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjzSazSA2ovzQps8FZua5X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 18377,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 877
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 18377,
          "cache_creation_input_tokens": 877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 877,
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

_source line 27 · 2026-05-11T23:20:48.768Z_

<details><summary>↩ Tool result · `toolu_01XkAxoQVjdnJFmXV9WAxVo4`</summary>

```text
Web search results for query: "arxiv 2604.13725 context compression repository level tasks empirical"

Links: [{"title":"[2604.13725] On the Effectiveness of Context Compression for Repository-Level Tasks: An Empirical Investigation","url":"https://arxiv.org/abs/2604.13725"},{"title":"On the Effectiveness of Context Compression for Repository-Level Tasks: An Empirical Investigation","url":"https://arxiv.org/html/2604.13725"},{"title":"From Context to EDUs: Faithful and Structured Context Compression via Elementary Discourse Unit Decomposition","url":"https://arxiv.org/html/2512.14244"},{"title":"CCF: A Context Compression Framework for Efficient Long-Sequence Language Modeling","url":"https://arxiv.org/html/2509.09199v1"},{"title":"A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression","url":"https://arxiv.org/html/2604.19572"},{"title":"Acon: Optimizing Context Compression for Long-horizon LLM Agents","url":"https://arxiv.org/html/2510.00615v2"},{"title":"Contextual Compression in Retrieval-Augmented Generation for Large Language Models: A Survey","url":"https://arxiv.org/html/2409.13385v1"},{"title":"Beyond Hard and Soft: Hybrid Context Compression for Balancing Local and Global Information Retention","url":"https://arxiv.org/html/2505.15774v1"},{"title":"Compressing Context to Enhance Inference Efficiency of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.391/"},{"title":"Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression","url":"https://arxiv.org/html/2505.19433v1"}]

I found information about the arXiv paper 2604.13725. Here are the key details:

**Paper Title:** On the Effectiveness of Context Compression for Repository-Level Tasks: An Empirical Investigation

**Main Focus:** The paper presents the first systematic empirical study of context compression for repository-level code intelligence, organizing eight methods into three paradigms: discrete token sequences, continuous latent vectors, and visual tokens.

**Problem Statement:** Repository-level code intelligence tasks require large language models (LLMs) to process long, multi-file contexts. Such inputs introduce three challenges: crucial context can be obscured by noise, truncated due to limited windows, and increased inference latency.

**Approach:** Context compression mitigates these risks by condensing inputs.

**Evaluation:** The methods are evaluated on code completion and generation, measuring performance and efficiency.

**Authors:** Jia Feng, Zhanyue Qin, Cuiyun Gao, Ruiqi Wang, Chaozheng Wang, Yingwei Ma, Xiaoyuan Xie

**Submission Date:** April 15, 2026


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86ec04ba-41ff-4604-87bb-c2376ff01d90",
  "isSidechain": true,
  "promptId": "f3fd6713-d6c3-46af-97a3-fe5e2012c44a",
  "agentId": "a6f43a06f31ed5e40",
  "type": "user",
  "uuid": "272ee607-2dab-4f4c-b05f-74cf6ed4a6a9",
  "sourceToolAssistantUUID": "86ec04ba-41ff-4604-87bb-c2376ff01d90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-11T23:21:21.352Z_

Here is my consolidated report on the two papers and the broader competitive landscape:

---

## 1. Squeez (arXiv 2604.04979) -- VERIFIED, claims are accurate

The paper exists and is titled "Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents" by Adam Kovacs from KR Labs. The proposal's characterization is **accurate on all points**:

- **Model**: Qwen 3.5 2B fine-tuned with LoRA -- confirmed
- **Task**: Task-conditioned line-level pruning of heterogeneous tool outputs (including stack traces and build logs) -- confirmed
- **Performance**: 0.86 recall, 92% token removal -- confirmed (paper also reports 0.80 F1)
- **27 tool families**: Confirmed -- the benchmark covers 27 tool types from real SWE-bench workflows and synthetic multi-ecosystem observations
- **Dataset**: 11,477 examples with a manually curated 618-example test set

No inaccuracies found in the proposal's characterization.

## 2. SWE-Pruner (arXiv 2601.16746) -- VERIFIED, claims are accurate

The paper exists and is titled "SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents." The proposal's characterization is **accurate on all points**:

- **0.6B CRF-based model**: Confirmed -- a lightweight 0.6B neural skimmer with a CRF layer for structured line-level retention decisions
- **61K synthetic data**: Confirmed -- generated via a Teacher-Student Paradigm using a 30B teacher model across 9 common agent tasks
- **23-54% token reduction on SWE-bench Verified while maintaining success rates**: Confirmed (specifically 23-38% on SWE-Bench, 29-54% on SWE-QA, and up to 14.84x on single-turn benchmarks like LongCodeQA)
- **Accepted to ACL 2026 Main Conference** (April 6, 2026)

One minor nuance: the proposal says "23-54% token reduction on SWE-bench Verified" but the paper actually reports 23-38% on SWE-Bench and 29-54% on SWE-QA -- so the 54% figure is from SWE-QA, not SWE-bench Verified. This is a slight conflation but not a material misrepresentation.

## 3. Potentially Missing Competitors

The proposal may be missing several relevant recent works:

1. **SWEzze** (arXiv 2603.28119, March 2026) -- "Compressing Code Context for LLM-based Issue Resolution." Uses Oracle-guided Code Distillation (OCD) with genetic search and delta debugging, plus a lightweight learned model for inference-time compression. Achieves ~6x compression, 51.8-71.3% token budget reduction, and *improves* issue resolution rates by 5.0-9.2% on SWE-bench Verified. This is a strong direct competitor.

2. **TACO** (arXiv 2604.19572, April 2026) -- "A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression." A training-free, plug-and-play framework that automatically discovers compression rules from interaction trajectories. Yields 1-4% accuracy gains on TerminalBench. Relevant if the proposal's scope includes terminal/execution output.

3. **ContextEvolve** (arXiv 2602.02597, February 2026) -- Multi-agent context compression for systems code optimization. Compresses raw interaction logs into refined optimization context.

4. **Empirical study** (arXiv 2604.13725, April 2026) -- "On the Effectiveness of Context Compression for Repository-Level Tasks" systematically compares 8 methods across 3 paradigms (discrete tokens, continuous latent vectors, visual tokens). Important for framing and baselines.

5. **ACON** (arXiv 2510.00615) -- A unified framework for optimally compressing both environment observations and interaction histories for long-horizon LLM agents.

Of these, **SWEzze is the most important omission** -- it's a directly competing learned compression method for code repair contexts with strong empirical results on SWE-bench Verified. The proposal should cite and differentiate against it.

Sources:
- [Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents](https://arxiv.org/abs/2604.04979)
- [Squeez HTML version](https://arxiv.org/html/2604.04979)
- [SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents](https://arxiv.org/abs/2601.16746)
- [SWE-Pruner HTML version](https://arxiv.org/html/2601.16746v1)
- [Compressing Code Context for LLM-based Issue Resolution (SWEzze)](https://arxiv.org/abs/2603.28119)
- [TACO: Self-Evolving Framework for Efficient Terminal Agents](https://arxiv.org/abs/2604.19572)
- [On the Effectiveness of Context Compression for Repository-Level Tasks](https://arxiv.org/abs/2604.13725)
- [ACON: Optimizing Context Compression for Long-horizon LLM Agents](https://arxiv.org/html/2510.00615v1)
- [Squeez on Hugging Face](https://huggingface.co/papers/2604.04979)
- [SWE-Pruner on Hugging Face](https://huggingface.co/papers/2601.16746)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "272ee607-2dab-4f4c-b05f-74cf6ed4a6a9",
  "isSidechain": true,
  "agentId": "a6f43a06f31ed5e40",
  "requestId": "req_011Cawe2nndLK5sdhGTp9iBF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "762572a3-350f-4201-8541-e8c9171da8f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bbf068bd-84bc-4d45-b959-d7d0ca192993",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TgqRkq8H2obQD9qZBRb5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 19254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 852,
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
