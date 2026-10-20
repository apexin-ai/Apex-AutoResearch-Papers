# Research conversation: You are helping me verify claims about three specific papers for an ML research review. Please verify each one: **Paper 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ad02a57428dc7bf78.jsonl`
- **Structured JSON:** [`75628d18261fba290e36.json`](../../sessions/75/75628d18261fba290e36.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-11T23:35:49.327Z_

You are helping me verify claims about three specific papers for an ML research review. Please verify each one:

**Paper 1: Squeez (arXiv 2604.04979, Apr 2026)**
Claims: Trains Qwen 3.5 2B with LoRA for task-conditioned line-level pruning of heterogeneous tool outputs (including stack traces and build logs), achieving 92% token removal with 0.86 recall across 27 tool families.

**Paper 2: SWEzze (arXiv 2603.28119, Mar 2026)**  
Claims: Trains Qwen3-Reranker-0.6B via Oracle-guided Code Distillation for static code context compression (6x compression, 5-9% resolution improvement).

**Paper 3: SWE-Pruner (arXiv 2601.16746, Jan 2026)**
Claims: Trains a 0.6B CRF-based model on 61K synthetic data for task-aware code context pruning (23-38% token reduction on SWE-bench, 29-54% on SWE-QA).

For each paper:
- Use WebSearch to find the paper (try both the arxiv ID directly and keyword searches)
- Use WebFetch to read the abstract and key results if possible
- Verify whether the claimed results (compression ratios, model sizes, training methods) are accurate
- Check if there are any results or findings the proposal omits that would be relevant

Report findings for all three papers in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "bdd117c7-c6bd-47b7-a840-6ea2c1d057b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:35:49.330Z_

```json
{
  "parentUuid": "bdd117c7-c6bd-47b7-a840-6ea2c1d057b1",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
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
  "uuid": "7216acbb-916e-4151-8491-5b1355c606aa",
  "timestamp": "2026-05-11T23:35:49.330Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:35:51.703Z_



I'll systematically verify each paper. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7216acbb-916e-4151-8491-5b1355c606aa",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfBAxTzPpDZLrwxV6AR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ff2804c-9914-4b6d-b84c-e9d31d1b21c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118pCDUPNy25nQA2fPHNcj5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 903,
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

_source line 4 · 2026-05-11T23:35:52.248Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017VqHBsmoPKxSxJfTkKkGL7`</summary>

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
  "parentUuid": "4ff2804c-9914-4b6d-b84c-e9d31d1b21c2",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfBAxTzPpDZLrwxV6AR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "496bb623-aea9-4bbf-b204-17a71548c15c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118pCDUPNy25nQA2fPHNcj5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 8223,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 903
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 903,
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

_source line 5 · 2026-05-11T23:35:52.251Z_

<details><summary>↩ Tool result · `toolu_017VqHBsmoPKxSxJfTkKkGL7`</summary>

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
  "parentUuid": "496bb623-aea9-4bbf-b204-17a71548c15c",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "84ea6c1f-e769-4f72-8c8a-7c2ce600920f",
  "sourceToolAssistantUUID": "496bb623-aea9-4bbf-b204-17a71548c15c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:35:55.317Z_



Now let me search for all three papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84ea6c1f-e769-4f72-8c8a-7c2ce600920f",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfBPgw61Fp3vVsWs8fi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "035480cd-a106-4292-bd22-44e88685988c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9fk7BodpJekwccmj29siU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9126,
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

_source line 7 · 2026-05-11T23:35:55.745Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WiGwLgxpRpBt4nqZgaPyBE`</summary>

```json
{
  "query": "arXiv 2604.04979 Squeez tool output pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "035480cd-a106-4292-bd22-44e88685988c",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfBPgw61Fp3vVsWs8fi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d088800f-f945-402f-9d40-002d02432279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9fk7BodpJekwccmj29siU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9126,
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

_source line 8 · 2026-05-11T23:35:56.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vb3BUr41AUD21FVVLCa7yj`</summary>

```json
{
  "query": "arXiv 2603.28119 SWEzze code context compression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d088800f-f945-402f-9d40-002d02432279",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfBPgw61Fp3vVsWs8fi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "649298f8-22b6-4f1f-82d4-de0af21860ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9fk7BodpJekwccmj29siU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9126,
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

_source line 9 · 2026-05-11T23:35:56.537Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WT4GXZUipnGugeRHpXyB6i`</summary>

```json
{
  "query": "arXiv 2601.16746 SWE-Pruner code context pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "649298f8-22b6-4f1f-82d4-de0af21860ae",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfBPgw61Fp3vVsWs8fi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9f46ecc-c4c4-44a1-bb16-0aeea5b4a90d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9fk7BodpJekwccmj29siU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9126,
      "output_tokens": 188,
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
          "output_tokens": 188,
          "cache_read_input_tokens": 9126,
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

_source line 10 · 2026-05-11T23:36:03.152Z_

<details><summary>↩ Tool result · `toolu_01WT4GXZUipnGugeRHpXyB6i`</summary>

```text
Web search results for query: "arXiv 2601.16746 SWE-Pruner code context pruning"

Links: [{"title":"[2601.16746] SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/abs/2601.16746"},{"title":"GitHub - Ayanami1314/swe-pruner · GitHub","url":"https://github.com/Ayanami1314/swe-pruner"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/html/2601.16746v1"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"Paper page - SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://huggingface.co/papers/2601.16746"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.16746v1"},{"title":"(PDF) SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.researchgate.net/publication/400071923_SWE-Pruner_Self-Adaptive_Context_Pruning_for_Coding_Agents"},{"title":"ayanami-kitasan/code-pruner · Hugging Face","url":"https://huggingface.co/ayanami-kitasan/code-pruner"},{"title":"Software Engineering on X: \"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents Yuhang Wang, Yuling Shi, Mo Yang, Rongrui Zhang, Shilin He, Heng Lian, Yuting Chen, Siyu Ye, Kai Cai, Xiaodong Gu https://t.co/7gw9yLhyMf [𝚌𝚜.𝚂𝙴 𝚌𝚜.𝙲𝙻] https://t.co/kRlOYQc5jb\" / X","url":"https://x.com/ComputerPapers/status/2015694356875727079"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding ...","url":"https://liner.com/review/swepruner-selfadaptive-context-pruning-for-coding-agents"}]

I found comprehensive information about arXiv 2601.16746 and SWE-Pruner. Here's a summary of the paper:

## Overview

SWE-Pruner is a self-adaptive context pruning framework tailored for coding agents that performs task-aware adaptive pruning for long contexts, drawing inspiration from how human programmers "selectively skim" source code during development and debugging.

## Problem

LLM agents have demonstrated remarkable capabilities in software development, but their performance is hampered by long interaction contexts, which incur high API costs and latency. While various context compression approaches such as LongLLMLingua have emerged to tackle this challenge, they typically rely on fixed metrics such as PPL, ignoring the task-specific nature of code understanding, and frequently disrupt syntactic and logical structure and fail to retain critical implementation details.

## Solution

Given the current task, the agent formulates an explicit goal (e.g., "focus on error handling") as a hint to guide the pruning targets. A lightweight neural skimmer (0.6B parameters) is trained to dynamically select relevant lines from the surrounding context given the goal.

## Results

Evaluations across four benchmarks and multiple models validate SWE-Pruner's effectiveness in various scenarios, achieving 23-54% token reduction on agent tasks like SWE-Bench Verified while even improving success rates, and up to 14.84x compression on single-turn tasks like LongCodeQA with minimal performance impact.

The paper was submitted on January 23, 2026, with a revised version on February 4, 2026. The code and model are available on GitHub and Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9f46ecc-c4c4-44a1-bb16-0aeea5b4a90d",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "2c73ec75-e4f7-454e-88a0-fb27b3e10acc",
  "sourceToolAssistantUUID": "f9f46ecc-c4c4-44a1-bb16-0aeea5b4a90d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-11T23:36:03.783Z_

<details><summary>↩ Tool result · `toolu_01WiGwLgxpRpBt4nqZgaPyBE`</summary>

```text
Web search results for query: "arXiv 2604.04979 Squeez tool output pruning"

Links: [{"title":"Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://arxiv.org/html/2604.04979"},{"title":"[2604.04979] Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://arxiv.org/abs/2604.04979"},{"title":"Paper page - Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://huggingface.co/papers/2604.04979"},{"title":"GitHub - KRLabsOrg/squeez: Squeeze verbose LLM agent tool output down to only the relevant lines · GitHub","url":"https://github.com/KRLabsOrg/squeez"},{"title":"Edge AI: Evaluation of Model Compression Techniques for Convolutional Neural Networks","url":"https://arxiv.org/html/2409.02134v1"},{"title":"Focus Session: Hardware and Software Techniques for Accelerating Multimodal Foundation Models","url":"https://arxiv.org/html/2604.21952"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"BVRA/legacy_seresnext101_32x4d.in1k_ft_df20_384 · Hugging Face","url":"https://huggingface.co/BVRA/legacy_seresnext101_32x4d.in1k_ft_df20_384"},{"title":"SVD-PRUNE: TRAINING-FREE TOKEN PRUNING FOR EFFICIENT VISION-LANGUAGE MODELS","url":"https://arxiv.org/html/2604.11530"},{"title":"[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/abs/2604.25098"}]

Based on the search results, I found detailed information about arXiv 2604.04979:

## Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents

This paper by Ádám Kovács from KR Labs introduces Squeez, a system designed to help coding agents work more efficiently by pruning tool output.

### Problem and Approach

Coding agents must process streams of tool observations (file reads, grep hits, stack traces, build logs, API responses, etc.) where only a small fraction of tokens is relevant to the next decision, making pruning a central efficiency problem for agent systems. The paper studies task-conditioned tool-output pruning: given a focused query and one tool output, return the smallest verbatim evidence block the agent should inspect next.

### Dataset and Methods

The researchers introduced a benchmark of 11,477 examples built from SWE-bench repository interactions and synthetic multi-ecosystem tool outputs, with a manually curated 618-example test set, and fine-tuned Qwen 3.5 2B with LoRA.

### Results

The model reaches 0.86 recall and 0.80 F1 while removing 92% of input tokens, outperforming zero-shot Qwen 3.5 35B A3B by 11 recall points and all heuristic baselines by a wide margin.

### Implementation

Squeez extracts only the relevant lines from raw tool observations (pytest, grep, git log, kubectl, build logs, etc.), removing 92% of tokens while retaining 0.86 recall, and works as a CLI pipe, Python library, or vLLM server.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d088800f-f945-402f-9d40-002d02432279",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "4ed5f332-a935-49f4-ac9b-d1316b332e88",
  "sourceToolAssistantUUID": "d088800f-f945-402f-9d40-002d02432279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:36:03.954Z_

<details><summary>↩ Tool result · `toolu_01Vb3BUr41AUD21FVVLCa7yj`</summary>

```text
Web search results for query: "arXiv 2603.28119 SWEzze code context compression"

Links: [{"title":"[2603.28119] Compressing Code Context for LLM-based Issue Resolution","url":"https://arxiv.org/abs/2603.28119"},{"title":"Compressing Code Context for LLM-based Issue Resolution","url":"https://arxiv.org/html/2603.28119"},{"title":"Compressing Code Context for LLM-based Issue Resolution Haoxiang Jia","url":"https://arxiv.org/pdf/2603.28119"},{"title":"PoC: Performance-oriented Context Compression for Large Language Models via Performance Prediction","url":"https://arxiv.org/html/2603.19733"},{"title":"[2603.25926] Density-aware Soft Context Compression with Semi-Dynamic Compression Ratio","url":"https://arxiv.org/abs/2603.25926"},{"title":"Density-aware Soft Context Compression with Semi-Dynamic Compression Ratio","url":"https://arxiv.org/html/2603.25926"},{"title":"Context Adaptive Extended Chain Coding for Semantic Map Compression","url":"https://arxiv.org/html/2603.03073"},{"title":"[2603.19733] PoC: Performance-oriented Context Compression for Large Language Models via Performance Prediction","url":"https://arxiv.org/abs/2603.19733"},{"title":"Distilling Conversations: Abstract Compression of Conversational Audio Context for LLM-based ASR","url":"https://arxiv.org/html/2603.26246"},{"title":"Developing Adaptive Context Compression Techniques for Large Language Models (LLMs) in Long-Running Interactions","url":"https://arxiv.org/html/2603.29193"}]

Based on the search results, here's information about arXiv paper 2603.28119:

## Paper Overview

The paper is titled "Compressing Code Context for LLM-based Issue Resolution" and was published on March 30, 2026.

## The Problem

Current approaches overapproximate the code context and suffer from two compounding problems: the prohibitive cost of processing massive inputs, and low effectiveness as noise floods the context window and distracts the model from the bug-fixing signal.

## The Solution

The paper proposes a two-component framework:

1. **Oracle-guided Code Distillation (OCD)**: A context distillation algorithm that combines genetic search and delta debugging to systematically reduce code contexts to their minimal sufficient subsequence - retaining only the ingredients required for a successful fix.

2. **SWEzze**: A lightweight model that learns to compress code context at inference time, filtering noise and comb[ining] the distilled training data. SWEzze compresses prompts by pruning their code segments to an issue's fix ingredients, the minimal set of semantic dependencies needed to resolve that issue.

## Results

Evaluated on SWE-bench Verified across three frontier LLMs, SWEzze maintains a stable compression rate of about 6 times across models, reduces the total token budget by 51.8%-71.3% relative to the uncompressed setting, improves issue resolution rates by 5.0%-9.2%, and delivers the best overall balance among effectiveness, compression ratio, and latency compared with state-of-the-art context compression baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "649298f8-22b6-4f1f-82d4-de0af21860ae",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "a6e6554f-acd4-415d-88a8-974fafbcf09b",
  "sourceToolAssistantUUID": "649298f8-22b6-4f1f-82d4-de0af21860ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-11T23:36:06.757Z_

Good, I found all three papers. Now let me fetch the actual arxiv pages for detailed verification of the specific claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6e6554f-acd4-415d-88a8-974fafbcf09b",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfCFVqhp9WKPVvgKBtV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "878f83b2-3601-41d9-ae23-203cb3229a07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmRcGXgZdmkUMrqGg6eBTq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1092,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 11038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1992,
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

_source line 14 · 2026-05-11T23:36:09.287Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FaT14ocLqRokwM5A4EhXZN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.04979",
  "prompt": "Extract the full abstract, list of authors, model details (what base model was fine-tuned, training method like LoRA), dataset size, number of tool families, key metrics (recall, F1, token removal percentage), and any other important results. Also note what the paper says about the types of tool outputs it handles."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "878f83b2-3601-41d9-ae23-203cb3229a07",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfCFVqhp9WKPVvgKBtV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ecc2b1d-dd2a-44c1-9553-5d0480702388",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmRcGXgZdmkUMrqGg6eBTq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1092,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 11038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1992,
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

_source line 15 · 2026-05-11T23:36:12.620Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EsUqRow7wzv6XHvybVDYSx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.28119",
  "prompt": "Extract the full abstract, list of authors, model details (what base model was used, model size like 0.6B), training method (Oracle-guided Code Distillation), compression ratio, resolution improvement percentages, token budget reduction, and all key metrics. Note whether the paper mentions the name \"SWEzze\" and whether it uses Qwen3-Reranker-0.6B specifically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ecc2b1d-dd2a-44c1-9553-5d0480702388",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfCFVqhp9WKPVvgKBtV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06e2b4f7-bd2d-4fe0-93a1-1e7542b09de7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmRcGXgZdmkUMrqGg6eBTq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1092,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 11038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1992,
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

_source line 16 · 2026-05-11T23:36:13.798Z_

<details><summary>↩ Tool result · `toolu_01FaT14ocLqRokwM5A4EhXZN`</summary>

```text
# Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents

## Abstract
The research addresses how coding agents consume lengthy tool observations when only small portions matter for subsequent steps. The authors develop a technique to identify and return minimal verbatim evidence blocks from tool outputs based on focused queries.

## Authors
Ádám Kovács

## Model Details
- **Base Model:** Qwen 3.5 2B
- **Training Method:** Fine-tuned with LoRA (Low-Rank Adaptation)
- **Comparison Models:** Zero-shot Qwen 3.5 35B A3B and heuristic baselines

## Dataset Information
- **Total Examples:** 11,477 instances
- **Test Set:** 618 manually curated examples
- **Source:** SWE-bench repository interactions with synthetic multi-ecosystem tool outputs

## Key Metrics
- **Recall:** 0.86
- **F1 Score:** 0.80
- **Token Removal:** 92% of input tokens eliminated
- **Performance Gain:** 11 recall points above zero-shot Qwen 3.5 35B A3B

## Tool Output Coverage
The paper references "synthetic multi-ecosystem tool outputs," indicating the approach handles diverse tool families across different programming environments, though specific tool categories aren't detailed in this abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ecc2b1d-dd2a-44c1-9553-5d0480702388",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "70295de1-6e28-4caa-9105-0ef7bac6d018",
  "sourceToolAssistantUUID": "9ecc2b1d-dd2a-44c1-9553-5d0480702388",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-11T23:36:14.590Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018cmmYoUgtan663QyQ9NTYj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.16746",
  "prompt": "Extract the full abstract, list of authors, model details (model size 0.6B, architecture like CRF), training data size (61K synthetic), training method, key metrics for SWE-bench token reduction (23-38%), SWE-QA metrics (29-54%), and all other benchmarks mentioned. Note whether the paper describes the model as CRF-based."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70295de1-6e28-4caa-9105-0ef7bac6d018",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfCFVqhp9WKPVvgKBtV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16ba0e47-2296-4c21-b471-1e4cf0a6af21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmRcGXgZdmkUMrqGg6eBTq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1092,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 11038,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1992
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1092,
          "output_tokens": 479,
          "cache_read_input_tokens": 11038,
          "cache_creation_input_tokens": 1992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1992,
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

_source line 18 · 2026-05-11T23:36:17.834Z_

<details><summary>↩ Tool result · `toolu_01EsUqRow7wzv6XHvybVDYSx`</summary>

```text
# Paper Analysis: Compressing Code Context for LLM-based Issue Resolution

## Full Abstract
"Large Language Models (LLMs) are now capable of resolving real-world GitHub issues. However, current approaches overapproximate the code context and suffer from two compounding problems: the prohibitive cost of processing massive inputs, and low effectiveness as noise floods the context window and distracts the model from the bug-fixing signal."

The authors propose combining genetic search with delta debugging to reduce code contexts while preserving essential repair components.

## Authors
- Haoxiang Jia
- Earl T. Barr
- Sergey Mechtaev

## Model & Training Details

**Model Name:** SWEzze (confirmed mentioned in abstract)

**Training Method:** Oracle-guided Code Distillation (OCD) - "a context distillation algorithm that combines genetic search and delta debugging"

**Base Model Specifics:** The document does not specify the base model architecture or mention "Qwen3-Reranker-0.6B"

## Key Performance Metrics
- **Compression Ratio:** ~6x across models
- **Token Budget Reduction:** 51.8%-71.3%
- **Resolution Rate Improvement:** 5.0%-9.2%
- **Evaluation Dataset:** SWE-bench Verified
- **Models Tested:** Three frontier LLMs (specific names not detailed in provided content)

## Notable Omission
The paper abstract does not specify model size parameters or particular base model identifiers like "0.6B."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06e2b4f7-bd2d-4fe0-93a1-1e7542b09de7",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "99a4f3a6-446b-4e9e-83e8-eb4f9e9b096d",
  "sourceToolAssistantUUID": "06e2b4f7-bd2d-4fe0-93a1-1e7542b09de7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-11T23:36:19.682Z_

<details><summary>↩ Tool result · `toolu_018cmmYoUgtan663QyQ9NTYj`</summary>

```text
# SWE-Pruner Paper Summary

## Abstract
The paper addresses context length challenges in LLM coding agents by proposing a task-aware pruning framework. It introduces a lightweight neural skimmer that dynamically selects relevant code lines based on explicit task goals, achieving significant token reduction while maintaining or improving performance across multiple benchmarks.

## Authors
Yuhang Wang, Yuling Shi, Mo Yang, Rongrui Zhang, Shilin He, Heng Lian, Yuting Chen, Siyu Ye, Kai Cai, and Xiaodong Gu

## Model Details
- **Size:** 0.6B parameters
- **Architecture:** Not explicitly identified as CRF-based in the provided content
- The paper describes it as a "lightweight neural skimmer"

## Training Data
No specific training data size (e.g., "61K synthetic") is mentioned in the provided excerpt.

## Training Method
Not detailed in the provided content.

## Key Metrics
- **SWE-Bench Verified:** "23-54% token reduction on agent tasks" with success rate improvements
- **LongCodeQA:** "up to 14.84x compression on single-turn tasks with minimal performance impact"

## Additional Benchmarks
The abstract mentions evaluations "across four benchmarks and multiple models," but specific names beyond SWE-Bench Verified and LongCodeQA are not detailed in the provided content.

## Note
The CRF architecture designation and additional benchmark details are not present in the supplied webpage excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16ba0e47-2296-4c21-b471-1e4cf0a6af21",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "8b4b2ff1-cf44-4cae-903c-c2cf5b59c823",
  "sourceToolAssistantUUID": "16ba0e47-2296-4c21-b471-1e4cf0a6af21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-11T23:36:22.506Z_

I need more details on all three papers. Let me fetch the full HTML versions for deeper information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b4b2ff1-cf44-4cae-903c-c2cf5b59c823",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfDQjVfLNxD9A6M3dft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de465633-5340-4f12-bec1-d373225a3450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2PRynvCidVEToFLKC1jFp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 13030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2664,
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

_source line 21 · 2026-05-11T23:36:24.860Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011Ax618jbqAfpyhQVfAnEEB`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.04979",
  "prompt": "I need to verify specific claims. Please extract: 1) The exact number of tool families mentioned (is it 27?), 2) The exact recall number and token removal percentage, 3) Whether the paper uses LoRA specifically, 4) Whether Qwen 3.5 2B is the base model, 5) The types of tool outputs handled (stack traces, build logs, etc.), 6) Any additional results or findings not captured in the abstract, 7) Dataset construction details, 8) Any limitations or important caveats mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de465633-5340-4f12-bec1-d373225a3450",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfDQjVfLNxD9A6M3dft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a1b58fb-6d4d-4320-a4e8-0e126ec60ef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2PRynvCidVEToFLKC1jFp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 13030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2664,
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

_source line 22 · 2026-05-11T23:36:28.246Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NFch7PPDb71w4Zq6xuDBTW`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.28119",
  "prompt": "I need to verify specific claims. Please extract: 1) The exact base model used for SWEzze (is it Qwen3-Reranker-0.6B?), 2) The model size (0.6B?), 3) The exact compression ratio (6x?), 4) The exact resolution improvement percentages (5-9%?), 5) Details about Oracle-guided Code Distillation training method, 6) What SWEzze stands for if mentioned, 7) Any additional results about token savings, cost reduction, latency, 8) Important limitations or caveats, 9) What specific LLMs were tested."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a1b58fb-6d4d-4320-a4e8-0e126ec60ef8",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfDQjVfLNxD9A6M3dft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dce8cae9-6074-46c1-a51c-f961c46102f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2PRynvCidVEToFLKC1jFp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 13030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2664,
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

_source line 23 · 2026-05-11T23:36:30.796Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y3Ck8eywj4kaR54oNLNYfK`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.16746v1",
  "prompt": "I need to verify specific claims. Please extract: 1) Whether the model architecture uses CRF (Conditional Random Field), 2) The exact training data size (is it 61K synthetic?), 3) The exact token reduction on SWE-bench (is it 23-38%?), 4) The exact results on SWE-QA (is it 29-54%?), 5) All four benchmarks mentioned and their results, 6) How the synthetic training data was generated, 7) The model architecture details beyond just 0.6B, 8) Any limitations or important caveats, 9) Whether it improves or maintains success rates after pruning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dce8cae9-6074-46c1-a51c-f961c46102f0",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfDQjVfLNxD9A6M3dft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c61c500f-81f3-4756-9304-9b188d0f2789",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2PRynvCidVEToFLKC1jFp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 13030,
      "output_tokens": 658,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2664
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 658,
          "cache_read_input_tokens": 13030,
          "cache_creation_input_tokens": 2664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2664,
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

_source line 24 · 2026-05-11T23:36:31.433Z_

<details><summary>↩ Tool result · `toolu_011Ax618jbqAfpyhQVfAnEEB`</summary>

```text
# Squeez Paper Claims Verification

**1) Tool families count:** Yes, exactly 27 tool types. The paper states: "covering 27 tool types; Table 2 lists the tool-family counts."

**2) Recall and token removal:** The model achieves 0.86 recall while removing 92% of input tokens, as confirmed in both abstract and results table.

**3) LoRA usage:** Confirmed. The paper explicitly uses "Qwen 3.5 2B fine-tuned with LoRA" and specifies training parameters including "LoRA adapter."

**4) Base model:** Yes, Qwen 3.5 2B is the foundation. The authors justify this choice: "A 2B backbone is therefore a better fit for this use case than a much larger decoder."

**5) Tool output types:** The paper confirms handling "file reads, grep hits, stack traces, build logs, API responses, and version-control history."

**6) Additional findings:**
- Outperforms unfine-tuned 2B base by 33 recall points
- Returns empty output correctly 80% of the time on negative examples (vs. 7% for Qwen 35B)
- Achieves 0.80 F1 score with 0.80 precision

**7) Dataset construction:** Used two-stage teacher-labeling with GPT-OSS-120B; 11,477 total examples split as 10,508 training, 240 development, 618 test; manually curated test set excluded 15.2% of candidates as duplicates or flawed.

**8) Key limitations acknowledged:** Evaluation measures single observations rather than full agent trajectories; usefulness approximated via span overlap; some tool families remain noisier (grep, lint_output).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a1b58fb-6d4d-4320-a4e8-0e126ec60ef8",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "5d2421ed-ffff-448a-b52d-5c29348d05c7",
  "sourceToolAssistantUUID": "9a1b58fb-6d4d-4320-a4e8-0e126ec60ef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-11T23:36:35.047Z_

<details><summary>↩ Tool result · `toolu_01NFch7PPDb71w4Zq6xuDBTW`</summary>

```text
# SWEzze: Key Technical Claims Verification

## 1. Base Model
**Exact base model:** "Qwen3-Reranker-0.6B" with "parameter-efficient LoRA adaptation"

## 2. Model Size
**Confirmed:** 0.6B parameters (lightweight cross-encoder)

## 3. Compression Ratio
**Exact claim:** "maintains a stable compression rate of about 6×" across models
- DeepSeek-V3.2: 6.03×
- Qwen3-Coder-Next: 5.95×
- GPT-5.2: 6.55×

## 4. Resolution Improvement
**Exact percentages vs. no compression:**
- "improves issue resolution rates by 5.0%–9.2%"
- Specific gains: 9.2% (DeepSeek), 5.0% (Qwen3), 8.6% (GPT-5.2)

## 5. OCD Training Method
Two-phase approach: (1) Genetic Algorithm discovers patch-enabling configurations, (2) Hierarchical Delta Debugging minimizes them to achieve 1-minimality—ensuring "every retained element is individually necessary"

## 6. SWEzze Meaning
The paper does not explicitly define what "SWEzze" stands for; it's presented as the model's name without backronym explanation.

## 7. Additional Results
**Token savings:** "reduces the total token budget by 51.8%–71.3% relative to the uncompressed setting"
**Latency:** 6.1 seconds average (4.0× faster than LongCodeZip's 24.4 seconds)

## 8. Important Limitations
- Requires ground-truth patches and test coverage during OCD (unavailable at inference)
- Minimality defined relative to specific LLM and generation parameters
- Manual analysis: 17 of 30 failures due to "disrupted syntactic structure"

## 9. LLMs Tested
- GPT-5.2
- DeepSeek-V3.2
- Qwen3-Coder-Next
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dce8cae9-6074-46c1-a51c-f961c46102f0",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "4beadd5f-d9e5-4c3a-a4b4-d42dc53a3fa1",
  "sourceToolAssistantUUID": "dce8cae9-6074-46c1-a51c-f961c46102f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T23:36:40.714Z_

<details><summary>↩ Tool result · `toolu_01Y3Ck8eywj4kaR54oNLNYfK`</summary>

```text
# SWE-Pruner: Verification of Key Claims

## 1) CRF Architecture
**Confirmed.** The model uses a "CRF-based pruning head" employing "Conditional Random Field negative log likelihood (CRF-NLL)" to model "transition probabilities between retain/prune states."

## 2) Training Data Size
**Confirmed as 61K synthetic.** The system generated 200,000 initial samples, then applied "rigorous quality control mechanism using Qwen3-Next-80B-A3B-Thinking as an LLM-as-a-Judge filter," yielding "61,184 training samples with verified line-level annotations."

## 3) SWE-Bench Token Reduction
**Confirmed as 23-38%.** Results show "23.1% reduction" for Claude Sonnet 4.5 and "38.3% reduction" for GLM 4.6 on SWE-Bench Verified, with "18.2% reduction" and "25.7% reduction" in interaction rounds respectively.

## 4) SWE-QA Results
**Confirmed as 29-54%.** Token reductions range from "8.9%" to "54.4%" across three repositories (Streamlink, Reflex, Conan) and two models.

## 5) Four Benchmarks and Results
The evaluation covers:
- **Long Code Completion**: up to 10.92x compression under 8x constraint
- **Long Code QA**: up to 14.84x compression under 8x constraint  
- **SWE-Bench Verified**: 23-38% token reduction
- **SWE-QA**: 29-54% token reduction across repositories

## 6) Synthetic Data Generation
Data came from GitHub repositories using "Qwen3-Coder-30B-A3B-Instruct as the teacher LLM to generate task-oriented queries and corresponding line-level retention masks" based on "a taxonomy of nine distinct agentic tasks" (Code Debugging, Feature Addition, Code Refactoring, etc.).

## 7) Model Architecture Details
Beyond 0.6B parameters, the system includes: "multi-layer feature fusion" extracting "hidden states from three intermediate layers (layers 7, 14, and 28)," processed through "self-attention block followed by multi-head attention layer (8 heads, hidden size 256)" with a CRF layer and separate reranking head.

## 8) Limitations
The paper acknowledges: focus on Python repositories (though "does not rely on Python-specific features"), potential data leakage mitigated by using "recently collected repositories from SWE-QA that postdate our training data," and "marginal latency overhead that could be further optimized."

## 9) Success Rate Impact
**Maintains/slightly improves success rates.** SWE-Bench shows "less than 1% degradation" (70.6% vs 70.2% for Claude). On SWE-QA, results are "minimal impact on task performance" with some models showing improvements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c61c500f-81f3-4756-9304-9b188d0f2789",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "7b8527b1-5cc0-4832-bd00-431eae3f2ac4",
  "sourceToolAssistantUUID": "c61c500f-81f3-4756-9304-9b188d0f2789",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-11T23:36:44.109Z_

Excellent. I now have comprehensive data on all three papers. Let me also do a quick search to see if there's anything important I might have missed about these papers' relationships or any retractions/corrections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b8527b1-5cc0-4832-bd00-431eae3f2ac4",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfExeezAuXMkByyktMq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86a3bfdf-45ae-4767-b155-d1de2ff4438e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011svxgYHeU9s3PfWE6GcJpG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2382,
      "cache_read_input_tokens": 15694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2382,
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

_source line 28 · 2026-05-11T23:36:44.389Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013tX4fEt9YPTFXQZnngjyre`</summary>

```json
{
  "query": "Squeez SWEzze SWE-Pruner coding agent context compression comparison 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86a3bfdf-45ae-4767-b155-d1de2ff4438e",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfExeezAuXMkByyktMq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "880d0760-d3d5-4578-b819-51445572eaa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011svxgYHeU9s3PfWE6GcJpG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2382,
      "cache_read_input_tokens": 15694,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2382
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 15694,
          "cache_creation_input_tokens": 2382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2382,
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

_source line 29 · 2026-05-11T23:36:52.922Z_

<details><summary>↩ Tool result · `toolu_013tX4fEt9YPTFXQZnngjyre`</summary>

```text
Web search results for query: "Squeez SWEzze SWE-Pruner coding agent context compression comparison 2026"

Links: [{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"[2601.16746] SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/abs/2601.16746"},{"title":"Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://arxiv.org/html/2604.04979"},{"title":"GitHub - KRLabsOrg/squeez: Squeeze verbose LLM agent tool output down to only the relevant lines · GitHub","url":"https://github.com/KRLabsOrg/squeez"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/html/2601.16746v1"},{"title":"GitHub - Ayanami1314/swe-pruner · GitHub","url":"https://github.com/Ayanami1314/swe-pruner"},{"title":"Paper page - SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://huggingface.co/papers/2601.16746"},{"title":"A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression","url":"https://arxiv.org/html/2604.19572v1"},{"title":"Compressing Code Context for LLM-based Issue Resolution","url":"https://arxiv.org/html/2603.28119"},{"title":"GitHub - VoltAgent/awesome-ai-agent-papers: A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, and autonomous systems. · GitHub","url":"https://github.com/VoltAgent/awesome-ai-agent-papers"}]

Based on the search results, here's what I found about these coding agent context compression approaches from 2026:

## Key Systems

**SWE-Pruner:** A self-adaptive pruning framework tailored for coding agents that trains a lightweight 0.6B pruning model on 61K synthetic data, enabling adaptive selection conditioned on given goals. It achieves 23-54% token reduction on agent tasks like SWE-Bench Verified and up to 14.84× compression on single-turn tasks like LongCodeQA with minimal performance impact.

**Squeez:** A task-conditioned tool-output pruner for coding agents, with a benchmark pairing grounded span annotations over 27 tool types with real SWE-bench workflows and synthetic multi-ecosystem observations. Squeez-2B (2B params) outperforms the 18x larger Qwen 3.5 35B model by 11 recall points at the same compression level.

**SWEzze:** Designed to be model- and harness-agnostic, ensuring compatibility with any downstream repair workflow, and integrates into Agentless, a pipeline combining fault localization and context construction. When using contexts from LongCodeZip and SWE-Pruner, the model produces patches that do not resolve the issue, while SWEzze produces effective patches.

## Key Differences

The main distinction is that SWE-Pruner targets coding agents more directly by pruning repository code context, while Squeez focuses on reducing verbose tool output from tool observations. Meanwhile, SWEzze specializes in context compression for issue resolution tasks specifically.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "880d0760-d3d5-4578-b819-51445572eaa0",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "ad02a57428dc7bf78",
  "type": "user",
  "uuid": "d10af7c7-c044-42ee-8418-fb46c1ca499f",
  "sourceToolAssistantUUID": "880d0760-d3d5-4578-b819-51445572eaa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-11T23:37:33.003Z_

Now I have all the information needed for a thorough verification. Here is my detailed report.

---

## Paper 1: Squeez (arXiv 2604.04979, Apr 2026)

**Claimed:** Trains Qwen 3.5 2B with LoRA for task-conditioned line-level pruning of heterogeneous tool outputs (including stack traces and build logs), achieving 92% token removal with 0.86 recall across 27 tool families.

**Verification: ACCURATE -- all specific claims confirmed.**

- **Base model and training method:** Confirmed. The paper explicitly uses Qwen 3.5 2B fine-tuned with LoRA adapters.
- **Task scope:** Confirmed. The paper handles heterogeneous tool outputs including "file reads, grep hits, stack traces, build logs, API responses, and version-control history."
- **92% token removal:** Confirmed.
- **0.86 recall:** Confirmed. Also achieves 0.80 F1 and 0.80 precision.
- **27 tool families:** Confirmed. The paper states "covering 27 tool types; Table 2 lists the tool-family counts."

**Omissions from the review's description that may be relevant:**
1. The paper also reports that it **outperforms the unfine-tuned 2B base by 33 recall points** (not just 11 points over the 35B model).
2. A notable finding: Squeez correctly returns **empty output on 80% of negative examples** (where nothing is relevant), vs. only 7% for the zero-shot Qwen 35B. This is important for real-world use where not every tool output contains relevant information.
3. The dataset is relatively small (11,477 examples total, 618 manually curated test examples), labeled via a two-stage teacher-labeling process using GPT-OSS-120B.
4. **Key limitation acknowledged by the paper:** Evaluation measures single observations rather than full agent trajectories. Some tool families (grep, lint_output) remain noisier than others.
5. The description says "line-level pruning" -- the paper actually describes returning "the smallest verbatim evidence block," which operates at line granularity but returns contiguous spans.

---

## Paper 2: SWEzze (arXiv 2603.28119, Mar 2026)

**Claimed:** Trains Qwen3-Reranker-0.6B via Oracle-guided Code Distillation for static code context compression (6x compression, 5-9% resolution improvement).

**Verification: ACCURATE -- all specific claims confirmed.**

- **Base model:** Confirmed. The paper explicitly uses **Qwen3-Reranker-0.6B** with parameter-efficient LoRA adaptation.
- **Oracle-guided Code Distillation (OCD):** Confirmed. This is a two-phase approach: (1) Genetic Algorithm discovers patch-enabling configurations, then (2) Hierarchical Delta Debugging minimizes them to 1-minimality.
- **6x compression:** Confirmed. Stable across models: DeepSeek-V3.2 (6.03x), Qwen3-Coder-Next (5.95x), GPT-5.2 (6.55x).
- **5-9% resolution improvement:** Confirmed. Specifically: 9.2% (DeepSeek-V3.2), 5.0% (Qwen3-Coder-Next), 8.6% (GPT-5.2).

**Omissions from the review's description that may be relevant:**
1. **Total token budget reduction is 51.8%-71.3%** relative to uncompressed settings -- this is a separate and important metric beyond the 6x code compression ratio.
2. **Latency:** SWEzze averages 6.1 seconds, which is 4x faster than LongCodeZip (24.4 seconds).
3. The paper was evaluated on **SWE-bench Verified** specifically, across three frontier LLMs (GPT-5.2, DeepSeek-V3.2, Qwen3-Coder-Next).
4. **Key limitation:** OCD requires ground-truth patches and test coverage during training data generation (unavailable at inference). The minimality definition is relative to a specific LLM and its generation parameters.
5. **Failure mode analysis:** 17 of 30 analyzed failures were due to "disrupted syntactic structure" -- suggesting the compression can break code structure.
6. The description calls it "static code context compression" -- this is fair but undersells its sophistication. SWEzze compresses prompts by pruning code segments to an issue's "fix ingredients," the minimal set of semantic dependencies needed to resolve an issue.

---

## Paper 3: SWE-Pruner (arXiv 2601.16746, Jan 2026)

**Claimed:** Trains a 0.6B CRF-based model on 61K synthetic data for task-aware code context pruning (23-38% token reduction on SWE-bench, 29-54% on SWE-QA).

**Verification: MOSTLY ACCURATE -- core claims confirmed, but the SWE-bench range is slightly understated.**

- **0.6B model:** Confirmed.
- **CRF-based architecture:** Confirmed. Uses a "CRF-based pruning head" with "Conditional Random Field negative log likelihood (CRF-NLL)" to model transition probabilities between retain/prune states.
- **61K synthetic data:** Confirmed. Started from 200K samples, filtered down to 61,184 training samples using Qwen3-Next-80B-A3B-Thinking as an LLM-as-a-Judge filter.
- **23-38% token reduction on SWE-bench:** Confirmed. 23.1% for Claude Sonnet 4.5, 38.3% for GLM 4.6.
- **29-54% on SWE-QA:** Partially confirmed but the range is wider than stated. The paper reports token reductions ranging from 8.9% to 54.4% across three repositories (Streamlink, Reflex, Conan) and two models. The low end (8.9%) is below the claimed 29%.

**Omissions from the review's description that may be relevant:**
1. **The paper evaluates on four benchmarks, not two:** Long Code Completion (up to 10.92x compression), Long Code QA (up to 14.84x compression), SWE-Bench Verified, and SWE-QA. The single-turn task results (14.84x compression on LongCodeQA) are impressive and omitted.
2. **Architecture is more sophisticated than "CRF-based"** -- it uses multi-layer feature fusion extracting hidden states from three intermediate layers (7, 14, 28), processed through self-attention and multi-head attention (8 heads, hidden size 256), plus a separate reranking head.
3. **Success rate impact:** Less than 1% degradation on SWE-Bench (70.6% vs 70.2% for Claude), meaning pruning barely hurts task performance.
4. **Training data generation:** Uses Qwen3-Coder-30B-A3B-Instruct as the teacher LLM to generate task-oriented queries and line-level retention masks across a taxonomy of nine distinct agentic tasks.
5. **Limitation:** Currently focused on Python repositories only, though the approach does not rely on Python-specific features.
6. **The SWE-QA range "29-54%" appears cherry-picked** -- the full range across all repository/model combinations is actually 8.9%-54.4%.

---

## Summary of Accuracy

| Paper | Claims Accurate? | Key Discrepancy |
|-------|-----------------|-----------------|
| Squeez | Yes, fully accurate | None -- all numbers and methods verified |
| SWEzze | Yes, fully accurate | None -- base model, compression ratio, improvement range all confirmed |
| SWE-Pruner | Mostly accurate | SWE-QA range of "29-54%" omits the lower end (8.9% for some repo/model combos); also omits strong single-turn compression results |

The most important omission across all three reviews is the **scope distinction**: Squeez handles tool output (runtime observations), SWEzze handles static code context for issue resolution, and SWE-Pruner handles code context for agent tasks more broadly. These are complementary rather than competing approaches, which the SWEzze paper itself highlights -- it notes that contexts from SWE-Pruner failed to produce effective patches for its task, while SWEzze succeeded.

Sources:
- [Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents (abs)](https://arxiv.org/abs/2604.04979)
- [Squeez (HTML)](https://arxiv.org/html/2604.04979)
- [Compressing Code Context for LLM-based Issue Resolution (abs)](https://arxiv.org/abs/2603.28119)
- [SWEzze (HTML)](https://arxiv.org/html/2603.28119)
- [SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents (abs)](https://arxiv.org/abs/2601.16746)
- [SWE-Pruner (HTML)](https://arxiv.org/html/2601.16746v1)
- [Squeez GitHub](https://github.com/KRLabsOrg/squeez)
- [SWE-Pruner GitHub](https://github.com/Ayanami1314/swe-pruner)
- [SWE-Pruner on HuggingFace](https://huggingface.co/papers/2601.16746)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d10af7c7-c044-42ee-8418-fb46c1ca499f",
  "isSidechain": true,
  "agentId": "ad02a57428dc7bf78",
  "requestId": "req_011CawfFsMwPYoJRapsYUS5y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6f2ea84-e8e0-41ae-b547-876d75dea0ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URT8Kd5Bm2rX6gbqAUvajN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1018,
      "cache_read_input_tokens": 18076,
      "output_tokens": 2366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1018
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2366,
          "cache_read_input_tokens": 18076,
          "cache_creation_input_tokens": 1018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1018,
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
