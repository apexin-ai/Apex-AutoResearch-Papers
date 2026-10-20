# Research conversation: Search the web to verify: 1. "On-Policy Context Distillation" (arXiv:2602.12275, Feb 2026) - Does this paper exist? What

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ab46ba9bdcb28f83d.jsonl`
- **Structured JSON:** [`a43a1cbe6b4079e67e00.json`](../../sessions/a4/a43a1cbe6b4079e67e00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-10T17:49:03.832Z_

Search the web to verify:

1. "On-Policy Context Distillation" (arXiv:2602.12275, Feb 2026) - Does this paper exist? What does it actually propose?

2. "Qwen3.6-27B" - Is this an actual model? Search for Qwen3 model family, Qwen3.6, or Qwen 3.6 27B. Check if this is a real released model or if the generator might have hallucinated this model name. The actual Qwen models might be Qwen2.5-Coder or Qwen3 (released in 2025).

3. "InlineCoder" (arXiv:2601.00376, Jan 2026) - Does this paper exist?

Use WebSearch to verify these.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "ab46ba9bdcb28f83d",
  "type": "user",
  "uuid": "4cc6717a-84af-4595-85ef-d7a9d31c5e6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T17:49:03.835Z_

```json
{
  "parentUuid": "4cc6717a-84af-4595-85ef-d7a9d31c5e6a",
  "isSidechain": true,
  "agentId": "ab46ba9bdcb28f83d",
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
  "uuid": "0c77b3bf-b690-4389-bcaf-34fcff61d1c6",
  "timestamp": "2026-05-10T17:49:03.835Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T17:49:07.220Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01G6x1gTKerMJpUktBNHnwcx`</summary>

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
  "parentUuid": "0c77b3bf-b690-4389-bcaf-34fcff61d1c6",
  "isSidechain": true,
  "agentId": "ab46ba9bdcb28f83d",
  "requestId": "req_011CauJvbP9BwZg6KK4bZDtC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a6b9338-6eaa-411a-9e66-636ac5fbf973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6ace8jpqQZQbwecdveT8j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 731
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 731,
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

_source line 4 · 2026-05-10T17:49:07.223Z_

<details><summary>↩ Tool result · `toolu_01G6x1gTKerMJpUktBNHnwcx`</summary>

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
  "parentUuid": "0a6b9338-6eaa-411a-9e66-636ac5fbf973",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "ab46ba9bdcb28f83d",
  "type": "user",
  "uuid": "d1761f57-5d49-4b47-b3df-aa9f807ad364",
  "sourceToolAssistantUUID": "0a6b9338-6eaa-411a-9e66-636ac5fbf973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T17:49:10.635Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012SG2DToB1oAa13dyhUVW81`</summary>

```json
{
  "query": "arXiv 2602.12275 \"On-Policy Context Distillation\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1761f57-5d49-4b47-b3df-aa9f807ad364",
  "isSidechain": true,
  "agentId": "ab46ba9bdcb28f83d",
  "requestId": "req_011CauJvr9PoY7Jfb9VNk3Mt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b88d868-b08c-42ba-a538-da9b4020f6de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xqJ9N2dtcxbM1R6fmMVgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T17:49:10.850Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LphNUueKvoT8e7FAtpoB55`</summary>

```json
{
  "query": "Qwen3.6-27B model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b88d868-b08c-42ba-a538-da9b4020f6de",
  "isSidechain": true,
  "agentId": "ab46ba9bdcb28f83d",
  "requestId": "req_011CauJvr9PoY7Jfb9VNk3Mt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "307e8986-44db-4d24-bed8-8c7cad0133fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xqJ9N2dtcxbM1R6fmMVgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T17:49:11.136Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UXQnatjR2puQVitZZhWGLG`</summary>

```json
{
  "query": "arXiv 2601.00376 \"InlineCoder\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "307e8986-44db-4d24-bed8-8c7cad0133fe",
  "isSidechain": true,
  "agentId": "ab46ba9bdcb28f83d",
  "requestId": "req_011CauJvr9PoY7Jfb9VNk3Mt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d297699-a426-4b7f-9415-c7e8ae02c0bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xqJ9N2dtcxbM1R6fmMVgA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8954,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 175,
          "cache_read_input_tokens": 8954,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 8 · 2026-05-10T17:49:17.160Z_

<details><summary>↩ Tool result · `toolu_012SG2DToB1oAa13dyhUVW81`</summary>

```text
Web search results for query: "arXiv 2602.12275 "On-Policy Context Distillation" 2026"

Links: [{"title":"[2602.12275] On-Policy Context Distillation for Language Models","url":"https://arxiv.org/abs/2602.12275"},{"title":"On-Policy Context Distillation for Language Models","url":"https://arxiv.org/html/2602.12275.pdf"},{"title":"On-Policy Context Distillation for Language Models Tianzhu Ye∗ Li Dong∗ Xun Wu","url":"https://arxiv.org/pdf/2602.12275"},{"title":"Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe","url":"https://arxiv.org/html/2604.13016v1"},{"title":"On-Policy Context Distillation for Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.12275"},{"title":"Rethinking On-Policy Distillation of Large Language Models","url":"https://arxiv.org/pdf/2604.13016"},{"title":"Understanding Self-Distillation and Privileged Information Distillation","url":"https://emilianopp.github.io/Privileged-Information-Distillation-and-Self-Distillation/"},{"title":"On-Policy Distillation 三大流派：一个方法解决两道难题","url":"https://qingkeai.online/archives/On-Policy%20Distillation"},{"title":"On-Policy Self-Distillation for Reasoning Compression","url":"https://arxiv.org/html/2603.05433v3"},{"title":"Continual Policy Distillation from Distributed Reinforcement Learning Teachers","url":"https://arxiv.org/html/2601.22475v1"}]

I found the paper arXiv 2602.12275. Here's what I found:

## On-Policy Context Distillation for Language Models

The paper was submitted on February 12, 2026, with a revised version on March 23, 2026, authored by Tianzhu Ye, Li Dong, Xun Wu, Shaohan Huang, and Furu Wei from Microsoft Research.

**Overview:**
The paper proposes On-Policy Context Distillation (OPCD), a framework that bridges on-policy distillation with context distillation by training a student model on its own generated trajectories while minimizing reverse Kullback-Leibler divergence against a context-conditioned teacher.

**Key Applications:**
The framework demonstrates effectiveness on two important applications: experiential knowledge distillation, where models extract and consolidate transferable knowledge from their historical solution traces, and system prompt distillation, where models internalize beneficial behaviors encoded in optimized prompts.

**Results:**
Across mathematical reasoning, text-based games, and domain-specific tasks, OPCD consistently outperforms baseline methods, achieving higher task accuracy while better preserving out-of-distribution capabilities. OPCD also enables effective cross-size distillation, where smaller student models can internalize experiential knowledge from larger teachers.

The paper addresses limitations of existing off-policy context distillation methods by using an on-policy approach that avoids exposure bias and the hallucination issues associated with forward KL divergence minimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b88d868-b08c-42ba-a538-da9b4020f6de",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "ab46ba9bdcb28f83d",
  "type": "user",
  "uuid": "e0ce403d-d794-499c-b2d1-c194bfc4a5b8",
  "sourceToolAssistantUUID": "6b88d868-b08c-42ba-a538-da9b4020f6de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T17:49:17.381Z_

<details><summary>↩ Tool result · `toolu_01UXQnatjR2puQVitZZhWGLG`</summary>

```text
Web search results for query: "arXiv 2601.00376 "InlineCoder" 2026"

Links: [{"title":"[2601.00376] In Line with Context: Repository-Level Code Generation via Context Inlining","url":"https://arxiv.org/abs/2601.00376"},{"title":"In Line with Context: Repository-Level Code Generation via Context Inlining","url":"https://arxiv.org/pdf/2601.00376"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1499&show=2000"},{"title":"Computer Science Jan 2026","url":"https://arxiv.org/list/cs/2026-01?skip=11000"},{"title":"arXiv:2601.19217v1 [cs.SE] 27 Jan 2026 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16","url":"https://arxiv.org/pdf/2601.19217"},{"title":"[2601.07372] Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models","url":"https://arxiv.org/abs/2601.07372"},{"title":"[2601.13531] ICASSP 2026 URGENT Speech Enhancement Challenge","url":"https://arxiv.org/abs/2601.13531"},{"title":"Computation and Language Mar 2026","url":"https://arxiv.org/list/cs.CL/current?skip=135&show=250"},{"title":"[2601.08624] Rare Near-Opposition Alignment of 3I/ATLAS on 22 January, 2026","url":"https://arxiv.org/abs/2601.08624"},{"title":"The ICASSP 2026 HumDial Challenge: Benchmarking Human-like Spoken Dialogue Systems in the LLM Era","url":"https://arxiv.org/html/2601.05564"}]

Based on the search results, I found information about arXiv paper 2601.00376 titled "InlineCoder":

## Paper Summary

InlineCoder is a novel framework for repository-level code generation. Unlike function-level code generation, it requires the model to understand the entire repository, reasoning over complex dependencies across functions, classes, and modules.

## How InlineCoder Works

InlineCoder enhances the understanding of repository context by inlining the unfinished function into its call graph, thereby reframing the challenging repository understanding as an easier function-level coding task.

The framework operates through a three-stage process:

1. InlineCoder first generates a draft completion, termed an anchor, which approximates downstream dependencies and enables perplexity-based confidence estimation

2. This anchor drives a bidirectional inlining process: (i) Upstream Inlining, which embeds the anchor into its callers to capture diverse usage scenarios; and (ii) Downstream Retrieval, which integrates the anchor's callees into the prompt to provide precise dependency context

## Authors and Submission

The paper was submitted on January 1, 2026 by authors including Chao Hu, Wenhao Zeng, Yuling Shi, Beijun Shen, and Xiaodong Gu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d297699-a426-4b7f-9415-c7e8ae02c0bb",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "ab46ba9bdcb28f83d",
  "type": "user",
  "uuid": "b56a8a58-52a6-4833-93f7-72acd6569187",
  "sourceToolAssistantUUID": "3d297699-a426-4b7f-9415-c7e8ae02c0bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T17:49:17.985Z_

<details><summary>↩ Tool result · `toolu_01LphNUueKvoT8e7FAtpoB55`</summary>

```text
Web search results for query: "Qwen3.6-27B model 2026"

Links: [{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model","url":"https://qwen.ai/blog?id=qwen3.6-27b"},{"title":"Qwen3.6 27B - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/qwen/qwen3.6-27b"},{"title":"Qwen3.6-27B: 27B Model Beats 397B on Coding (2026)","url":"https://www.buildfastwithai.com/blogs/qwen3-6-27b-review-2026"},{"title":"Qwen3.6 - How to Run Locally | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3.6"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"qwen3.6:27b","url":"https://ollama.com/library/qwen3.6:27b"},{"title":"qwen/qwen3.6-27b • LM Studio","url":"https://lmstudio.ai/models/qwen/qwen3.6-27b"},{"title":"Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model","url":"https://simonwillison.net/2026/Apr/22/qwen36-27b/"},{"title":"Qwen/Qwen3.6-27B | vLLM Recipes","url":"https://recipes.vllm.ai/Qwen/Qwen3.6-27B"}]

Based on the search results, here's what I found about the Qwen3.6-27B model:

## Overview

Qwen3.6 27B is a dense 27-billion-parameter language model from the Qwen Team at Alibaba, released in April 2026. It's Alibaba's first dense open-weight model in the Qwen3.6 family, built for agentic coding, repository-level reasoning, and frontend development workflows.

## Key Features

It features hybrid multimodal capabilities — accepting text, image, and video inputs — and is designed for agentic coding and reasoning tasks, with particular strength in repository-level code comprehension, front-end development workflows, and multi-step problem solving.

The model supports a context length of 262,144 tokens natively and is extensible up to 1,010,000 tokens.

It includes a built-in thinking mode for extended reasoning and preserves thinking context across conversation history.

## Performance & Architecture

Qwen3.6-27B is fully dense: all 27 billion parameters are active on every inference pass. This distinguishes it from most large open-source models that use Mixture-of-Experts (MoE) architectures.

On SWE-bench Verified, it achieves 77.2%, putting it within 3.7 points of Claude Opus 4.6 (80.8%).

## Availability & Licensing

It was released on April 22, 2026 on Hugging Face and ModelScope under the Apache 2.0 license.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "307e8986-44db-4d24-bed8-8c7cad0133fe",
  "isSidechain": true,
  "promptId": "47039f3f-f390-4407-8ec8-a6a53a32cf73",
  "agentId": "ab46ba9bdcb28f83d",
  "type": "user",
  "uuid": "9676327e-878f-4b40-b6b6-7ecf9c9eda59",
  "sourceToolAssistantUUID": "307e8986-44db-4d24-bed8-8c7cad0133fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T17:49:35.985Z_

Here are the verification results for all three items:

---

## 1. "On-Policy Context Distillation" (arXiv:2602.12275, Feb 2026)

**Verdict: REAL -- This paper exists.**

The paper is titled "On-Policy Context Distillation for Language Models," submitted February 12, 2026 (revised March 23, 2026). It is authored by Tianzhu Ye, Li Dong, Xun Wu, Shaohan Huang, and Furu Wei from Microsoft Research.

**What it proposes:** The paper introduces On-Policy Context Distillation (OPCD), a framework that trains a student model on its own generated trajectories while minimizing reverse KL divergence against a context-conditioned teacher. It addresses two applications:
- **Experiential knowledge distillation** -- extracting transferable knowledge from a model's historical solution traces
- **System prompt distillation** -- internalizing behaviors encoded in optimized prompts

The approach outperforms baselines on mathematical reasoning, text-based games, and domain-specific tasks, while better preserving out-of-distribution capabilities. It also enables cross-size distillation (smaller students learning from larger teachers).

---

## 2. "Qwen3.6-27B"

**Verdict: REAL -- This is an actual released model.**

Qwen3.6-27B is a dense 27-billion-parameter language model released by the Qwen Team at Alibaba on April 22, 2026, under the Apache 2.0 license. It is available on Hugging Face, Ollama, LM Studio, and other platforms.

Key facts:
- It is a **dense** model (all 27B parameters active on every pass, not MoE)
- Supports 262K tokens natively (extensible to ~1M)
- Achieves 77.2% on SWE-bench Verified
- Focused on agentic coding, repository-level reasoning, and frontend development
- Has a built-in thinking mode for extended reasoning

So if someone suggested this model might be hallucinated based on knowledge of only Qwen2.5 or Qwen3 (released in 2025), it turns out Qwen3.6 is a newer release from April 2026.

---

## 3. "InlineCoder" (arXiv:2601.00376, Jan 2026)

**Verdict: REAL -- This paper exists.**

The full title is "In Line with Context: Repository-Level Code Generation via Context Inlining," submitted January 1, 2026. Authors include Chao Hu, Wenhao Zeng, Yuling Shi, Beijun Shen, and Xiaodong Gu.

**What it proposes:** InlineCoder is a framework for repository-level code generation that works by "inlining" an unfinished function into its call graph, converting the hard problem of repository-level understanding into an easier function-level coding task. It uses a three-stage process:
1. Generates a draft completion ("anchor") to approximate downstream dependencies
2. Performs **Upstream Inlining** -- embedding the anchor into its callers to capture usage scenarios
3. Performs **Downstream Retrieval** -- integrating the anchor's callees into the prompt for dependency context

---

**Summary:** All three items are verified as real and accurately described.

Sources:
- [On-Policy Context Distillation for Language Models (arXiv:2602.12275)](https://arxiv.org/abs/2602.12275)
- [On-Policy Context Distillation - alphaXiv](https://www.alphaxiv.org/overview/2602.12275)
- [Qwen3.6-27B on Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B)
- [Qwen3.6-27B Blog Post](https://qwen.ai/blog?id=qwen3.6-27b)
- [Qwen3.6-27B on OpenRouter](https://openrouter.ai/qwen/qwen3.6-27b)
- [Simon Willison's coverage of Qwen3.6-27B](https://simonwillison.net/2026/Apr/22/qwen36-27b/)
- [Qwen3.6-27B on Ollama](https://ollama.com/library/qwen3.6:27b)
- [InlineCoder (arXiv:2601.00376)](https://arxiv.org/abs/2601.00376)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9676327e-878f-4b40-b6b6-7ecf9c9eda59",
  "isSidechain": true,
  "agentId": "ab46ba9bdcb28f83d",
  "requestId": "req_011CauJwdwCyQyq5qurbHCPE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e223314-8477-4320-8a2d-9a7a92a3633a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "89242a75-96eb-4c62-bd61-c8808bbe5e16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vu1A5A6kmasXmGBc3fNuTL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 838,
      "cache_creation_input_tokens": 1949,
      "cache_read_input_tokens": 10346,
      "output_tokens": 1100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1949
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 838,
          "output_tokens": 1100,
          "cache_read_input_tokens": 10346,
          "cache_creation_input_tokens": 1949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1949,
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
