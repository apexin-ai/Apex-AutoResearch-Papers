# Research conversation: Search the web to verify whether these papers exist and what they actually claim. For each paper, search for it and repo

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-acae1ebdea03f6d39.jsonl`
- **Structured JSON:** [`10f894cd7bce630616de.json`](../../sessions/10/10f894cd7bce630616de.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-10T17:48:58.900Z_

Search the web to verify whether these papers exist and what they actually claim. For each paper, search for it and report: (1) does it exist, (2) what does it actually claim (briefly), (3) any discrepancies with the descriptions below.

Papers to verify:
1. "Self-Execution Simulation Improves Coding Models" (arXiv:2604.03253, Apr 2026) - claimed to show LLMs can simulate execution traces with ~80% accuracy
2. "CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models" (arXiv:2602.17684) - claimed +11.72 points on Qwen3-8B
3. "Scalable Supervising Software Agents with Patch Reasoner" (arXiv:2510.22775) - claimed 72.2% on SWE-bench Verified, 50x faster
4. "S*: Test Time Scaling for Code Generation" (arXiv:2502.14382) - claimed to show imperfect verifiers enable effective test-time scaling
5. "DryRUN" (arXiv:2604.21598) - claimed to demonstrate prompt-based execution simulation for self-correction
6. "Scaling Test-Time Compute for Agentic Coding" (arXiv:2604.16529) - claimed Claude Opus 4.5 improves from 70.9% to 77.6% on SWE-bench Verified
7. "FunPRM: Function-as-Step Process Reward Model" (arXiv:2601.22249)

Use WebSearch for each. Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bca633b7-27f5-483b-9192-8c0cf0607331",
  "agentId": "acae1ebdea03f6d39",
  "type": "user",
  "uuid": "f86b3c40-1512-4e58-a6df-0a0765ad2794",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T17:48:58.904Z_

```json
{
  "parentUuid": "f86b3c40-1512-4e58-a6df-0a0765ad2794",
  "isSidechain": true,
  "agentId": "acae1ebdea03f6d39",
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
  "uuid": "53b5a2f2-bd68-4f52-8353-7c9598ebd376",
  "timestamp": "2026-05-10T17:48:58.904Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T17:49:02.117Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MwonNQaHd6ihzrXxc3gtLs`</summary>

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
  "parentUuid": "53b5a2f2-bd68-4f52-8353-7c9598ebd376",
  "isSidechain": true,
  "agentId": "acae1ebdea03f6d39",
  "requestId": "req_011CauJvEL7Xa2b7NEiNZFq3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcf7dbe6-9707-4da1-8c12-99cdd1cbcdea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tEY8zZTeV6awmp8fUB1Ni",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9162,
      "cache_read_input_tokens": 0,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9162
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9162,
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

_source line 4 · 2026-05-10T17:49:02.122Z_

<details><summary>↩ Tool result · `toolu_01MwonNQaHd6ihzrXxc3gtLs`</summary>

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
  "parentUuid": "bcf7dbe6-9707-4da1-8c12-99cdd1cbcdea",
  "isSidechain": true,
  "promptId": "bca633b7-27f5-483b-9192-8c0cf0607331",
  "agentId": "acae1ebdea03f6d39",
  "type": "user",
  "uuid": "650d4f18-a146-4344-8726-c9e047f99750",
  "sourceToolAssistantUUID": "bcf7dbe6-9707-4da1-8c12-99cdd1cbcdea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-10T17:49:05.473Z_

I'll search for each paper to verify its existence and claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "650d4f18-a146-4344-8726-c9e047f99750",
  "isSidechain": true,
  "agentId": "acae1ebdea03f6d39",
  "requestId": "req_011CauJvUQCXSrBLg2D5JbzB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffc77e76-105c-43a0-98f5-cdd7d7b09497",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKXv6WWnUccKcyMYcyqcHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 6 · 2026-05-10T17:49:06.113Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A4kPqrHZeLj47AJfYXew5Y`</summary>

```json
{
  "query": "arXiv 2604.03253 \"Self-Execution Simulation Improves Coding Models\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffc77e76-105c-43a0-98f5-cdd7d7b09497",
  "isSidechain": true,
  "agentId": "acae1ebdea03f6d39",
  "requestId": "req_011CauJvUQCXSrBLg2D5JbzB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "812387c8-8568-4133-936e-5488e63e1879",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKXv6WWnUccKcyMYcyqcHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 7 · 2026-05-10T17:49:06.426Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E9aLM8vawLyp5tdmKxJc1S`</summary>

```json
{
  "query": "arXiv 2602.17684 \"CodeScaler\" execution-free reward models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "812387c8-8568-4133-936e-5488e63e1879",
  "isSidechain": true,
  "agentId": "acae1ebdea03f6d39",
  "requestId": "req_011CauJvUQCXSrBLg2D5JbzB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f6bddc1-96b1-484f-aba3-6e56bbf9f52a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKXv6WWnUccKcyMYcyqcHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 8 · 2026-05-10T17:49:06.888Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012YCZmEcQzshSD4BDSWB4Sn`</summary>

```json
{
  "query": "arXiv 2510.22775 \"Scalable Supervising Software Agents with Patch Reasoner\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f6bddc1-96b1-484f-aba3-6e56bbf9f52a",
  "isSidechain": true,
  "agentId": "acae1ebdea03f6d39",
  "requestId": "req_011CauJvUQCXSrBLg2D5JbzB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8b3bfb1-5682-4231-ba95-cf3c71321d26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKXv6WWnUccKcyMYcyqcHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 9 · 2026-05-10T17:49:07.250Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L2RsbrsngEqX8kJTQn7kUz`</summary>

```json
{
  "query": "arXiv 2502.14382 \"S*: Test Time Scaling for Code Generation\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8b3bfb1-5682-4231-ba95-cf3c71321d26",
  "isSidechain": true,
  "agentId": "acae1ebdea03f6d39",
  "requestId": "req_011CauJvUQCXSrBLg2D5JbzB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ac921f6-658a-4f06-b903-0bba1919f806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKXv6WWnUccKcyMYcyqcHL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9162,
      "output_tokens": 260,
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
          "output_tokens": 260,
          "cache_read_input_tokens": 9162,
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

_source line 10 · 2026-05-10T17:49:11.670Z_

<details><summary>↩ Tool result · `toolu_01A4kPqrHZeLj47AJfYXew5Y`</summary>

```text
Web search results for query: "arXiv 2604.03253 "Self-Execution Simulation Improves Coding Models""

Links: [{"title":"[2604.03253] Self-Execution Simulation Improves Coding Models","url":"https://arxiv.org/abs/2604.03253"},{"title":"Self-Execution Simulation Improves Coding Models","url":"https://arxiv.org/html/2604.03253"},{"title":"Paper page - Self-Execution Simulation Improves Coding Models","url":"https://huggingface.co/papers/2604.03253"},{"title":"SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution","url":"https://arxiv.org/html/2604.19825"},{"title":"Code Simulation as a Proxy for High-order Tasks in Large Language Models","url":"https://arxiv.org/html/2502.03568v1"},{"title":"The Self-Execution Benchmark: Measuring LLMs’ Attempts to Overcome Their Lack of Self-Execution","url":"https://arxiv.org/html/2508.12277v1"},{"title":"Code Simulation Challenges for Large Language Models","url":"https://arxiv.org/html/2401.09074v4"},{"title":"Embarrassingly Simple Self-Distillation Improves Code Generation","url":"https://arxiv.org/html/2604.01193v1"},{"title":"A Self-Improving Coding Agent","url":"https://arxiv.org/html/2504.15228v2"},{"title":"[2604.01193] Embarrassingly Simple Self-Distillation Improves Code Generation","url":"https://arxiv.org/abs/2604.01193"}]

Based on the search results, I found the paper arXiv 2604.03253 "Self-Execution Simulation Improves Coding Models."

The work demonstrates that Code LLMs can be trained to simulate program execution in a step-by-step manner and that this capability can be leveraged to improve competitive programming performance.

The approach combines supervised fine-tuning on natural language execution traces, textual explanations grounded in true execution, with reinforcement learning using verifiable rewards. The authors introduce two complementary objectives: output prediction given code and inputs, and solving competitive programming tasks with either ground-truth or self-predicted execution feedback.

These objectives enable models to perform self-verification over multiple candidate solutions, and iterative self-fixing by simulating test execution.

The paper was submitted on March 11, 2026 and authored by Gallil Maimon, Ori Yoran, Felix Kreuk, Michael Hassid, Gal Cohen, Pierre Chambon, and Yossi Adi.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "812387c8-8568-4133-936e-5488e63e1879",
  "isSidechain": true,
  "promptId": "bca633b7-27f5-483b-9192-8c0cf0607331",
  "agentId": "acae1ebdea03f6d39",
  "type": "user",
  "uuid": "02726ecd-4931-4650-85ee-d11eedea9b0c",
  "sourceToolAssistantUUID": "812387c8-8568-4133-936e-5488e63e1879",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T17:49:13.808Z_

<details><summary>↩ Tool result · `toolu_01E9aLM8vawLyp5tdmKxJc1S`</summary>

```text
Web search results for query: "arXiv 2602.17684 "CodeScaler" execution-free reward models"

Links: [{"title":"[2602.17684] CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models","url":"https://arxiv.org/abs/2602.17684"},{"title":"CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models","url":"https://arxiv.org/html/2602.17684"},{"title":"CodeScaler: Scaling Code LLM Training and Test-Time ...","url":"https://arxiv.org/pdf/2602.17684"},{"title":"GitHub - LARK-AI-Lab/CodeScaler: The official repo for \"CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models\" · GitHub","url":"https://github.com/LARK-AI-Lab/CodeScaler"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/recent?skip=651&show=50"},{"title":"Reward Models Enable Scalable Code Verification by Trading Accuracy for Throughput","url":"https://arxiv.org/html/2506.10056v1"},{"title":"Lookahead Sample Reward Guidance for Test-Time Scaling of Diffusion Models","url":"https://arxiv.org/html/2602.03211"},{"title":"Mitigating Reward Hacking via Information-Theoretic Reward Modeling","url":"https://arxiv.org/html/2402.09345v3"},{"title":"GitHub - iszhanjiawei/flow_matching_arxiv_daily · GitHub","url":"https://github.com/iszhanjiawei/flow_matching_arxiv_daily"},{"title":"Dynamic Scaling of Unit Tests for Code Reward Modeling","url":"https://arxiv.org/pdf/2501.01054"}]

Based on the search results, here's what I found about arXiv paper 2602.17684:

## CodeScaler: Execution-Free Reward Models

CodeScaler is an execution-free reward model designed to scale both reinforcement learning training and test-time inference for code generation. The paper was submitted on February 4, 2026, by authors including Xiao Zhu and 7 others.

### Motivation

Reinforcement Learning from Verifiable Rewards (RLVR) has driven recent progress in code large language models by leveraging execution-based feedback from unit tests, but its scalability is fundamentally constrained by the availability and reliability of high-quality test cases.

### Key Features

CodeScaler is trained on carefully curated preference data derived from verified code problems and incorporates syntax-aware code extraction and validity-preserving reward shaping to ensure stable and robust optimization.

### Performance Results

Across five coding benchmarks, CodeScaler improves Qwen3-8B-Base by an average of +11.72 points, outperforming binary execution-based RL by +1.82 points, and enables scalable reinforcement learning on synthetic datasets without any test cases. At inference time, CodeScaler serves as an effective test-time scaling method, achieving performance comparable to unit test approaches while providing a 10-fold reduction in latency.

An official GitHub repository with code, datasets, and models has been released: https://github.com/LARK-AI-Lab/CodeScaler


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f6bddc1-96b1-484f-aba3-6e56bbf9f52a",
  "isSidechain": true,
  "promptId": "bca633b7-27f5-483b-9192-8c0cf0607331",
  "agentId": "acae1ebdea03f6d39",
  "type": "user",
  "uuid": "8180694d-9aff-49cd-aca3-f16176834415",
  "sourceToolAssistantUUID": "8f6bddc1-96b1-484f-aba3-6e56bbf9f52a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T17:49:14.239Z_

<details><summary>↩ Tool result · `toolu_01L2RsbrsngEqX8kJTQn7kUz`</summary>

```text
Web search results for query: "arXiv 2502.14382 "S*: Test Time Scaling for Code Generation""

Links: [{"title":"[2502.14382] S*: Test Time Scaling for Code Generation","url":"https://arxiv.org/abs/2502.14382"},{"title":"[2502.14382v1] S*: Test Time Scaling for Code Generation","url":"https://arxiv.org/abs/2502.14382v1"},{"title":"dblp: S*: Test Time Scaling for Code Generation.","url":"https://dblp.org/rec/journals/corr/abs-2502-14382.html"},{"title":"(PDF) S*: Test Time Scaling for Code Generation","url":"https://www.researchgate.net/publication/389176524_S_Test_Time_Scaling_for_Code_Generation"},{"title":"S*: Test-Time Scaling for Code Generation","url":"https://novasky-ai.github.io/posts/S*/"},{"title":"𝑆^∗: Test Time Scaling for Code Generation","url":"https://arxiv.org/html/2502.14382v1"},{"title":"Paper page - S*: Test Time Scaling for Code Generation","url":"https://huggingface.co/papers/2502.14382"},{"title":"S∗: Test Time Scaling for Code Generation","url":"https://aclanthology.org/2025.findings-emnlp.865.pdf"},{"title":"s1: Simple test-time scaling","url":"https://arxiv.org/html/2501.19393v1"},{"title":"\\name: Scaling LLMs with Reasoning Data and Test-Time Compute for Accurate RTL Code Generation","url":"https://arxiv.org/html/2506.05566v1"}]

I found the paper! Here are the key details about arXiv 2502.14382:

**Title:** S*: Test Time Scaling for Code Generation

**Authors:** Dacheng Li, Shiyi Cao, Chengkun Cao, Xiuyu Li, Shangyin Tan, Kurt Keutzer, Jiarong Xing, Joseph E. Gonzalez, Ion Stoica

**Submission Date:** February 20, 2025

**Overview:** Increasing test-time compute for LLMs shows promise across domains but remains underexplored in code generation, despite extensive study in math. The paper proposes S*, the first hybrid test-time scaling framework that substantially improves the coverage and selection accuracy of generated code. S* extends the existing parallel scaling paradigm with sequential scaling to push performance boundaries.

**Key Innovation:** It further leverages a novel selection mechanism that adaptively generates distinguishing inputs for pairwise comparison, combined with execution-grounded information to robustly identify correct solutions.

**Notable Results:** S* consistently improves performance across model families and sizes, enabling a 3B model to outperform GPT-4o-mini; S* enables non-reasoning models to surpass reasoning models - GPT-4o-mini with S* outperforms o1-preview by 3.7% on LiveCodeBench.

The paper is available on arXiv at https://arxiv.org/abs/2502.14382.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ac921f6-658a-4f06-b903-0bba1919f806",
  "isSidechain": true,
  "promptId": "bca633b7-27f5-483b-9192-8c0cf0607331",
  "agentId": "acae1ebdea03f6d39",
  "type": "user",
  "uuid": "d8b47462-aef5-4936-8e39-d5d3c9181b2c",
  "sourceToolAssistantUUID": "1ac921f6-658a-4f06-b903-0bba1919f806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T17:49:15.470Z_

<details><summary>↩ Tool result · `toolu_012YCZmEcQzshSD4BDSWB4Sn`</summary>

```text
Web search results for query: "arXiv 2510.22775 "Scalable Supervising Software Agents with Patch Reasoner""

Links: [{"title":"[2510.22775] Scalable Supervising Software Agents with Patch Reasoner","url":"https://arxiv.org/abs/2510.22775"},{"title":"Scalable Supervising Software Agents with Patch Reasoner","url":"https://arxiv.org/html/2510.22775"},{"title":"Preprint SCALABLE SUPERVISING SOFTWARE AGENTS WITH PATCH REASONER","url":"https://arxiv.org/pdf/2510.22775"},{"title":"SCALABLE SUPERVISING SOFTWARE AGENTS WITH ...","url":"https://openreview.net/pdf/559f04da6800e2dec4bdac71d08cb1ce0d9a16af.pdf"},{"title":"SCALABLE SUPERVISING SOFTWARE AGENTS WITH PATCH ...","url":"https://openreview.net/pdf/0668db7cc85c9762d53806cf4aabc486f72ce722.pdf"},{"title":"Toward Training Superintelligent Software Agents through Self-Play SWE-RL","url":"https://arxiv.org/pdf/2512.18552"},{"title":"Towards a Science of Scaling Agent Systems (Google ...","url":"https://www.facebook.com/groups/DeepNetGroup/posts/2681070338952498/"},{"title":"GitHub - kyegomez/awesome-multi-agent-papers: A compilation of the best multi-agent papers · GitHub","url":"https://github.com/kyegomez/awesome-multi-agent-papers"},{"title":"Toward Training Superintelligent Software Agents through ...","url":"https://www.facebook.com/groups/DeepNetGroup/posts/2686724418387090/"},{"title":"Reason-Plan-ReAct: A Reasoner-Planner Supervising a ReAct Executor for Complex Enterprise Tasks","url":"https://arxiv.org/html/2512.03560v1"}]

Based on the search results, I found detailed information about arXiv paper 2510.22775:

## Overview

The paper proposes R4P, a patch verifier model to provide scalable rewards for training and testing SWE agents via reasoning.

## Key Problem

While large language model agents have advanced software engineering tasks, the unscalable nature of existing test-based supervision limits the potential improvement of data scaling because building and running test sandbox is rather heavy and fragile, and data with high-coverage tests is naturally rare and threatened by test hacking via edge cases.

## Core Approach

The paper considers that patch verification is fundamentally a reasoning task, mirroring how human repository maintainers review patches without writing and running new reproduction tests. R4P uses a group-wise objective for RL training, enabling it to verify multiple patches against each other's modification and gain a dense reward for stable training.

## Results and Performance

R4P achieves 72.2% Acc. for verifying patches from SWE-bench-verified, surpassing OpenAI o3. The Pass@1 resolution rate on SWE-bench-verified reaches 26.2%, outperforming Lingma Agent, and can be further improved to 32.8% with R4P for patch selection. R4P verifies each patch within a second on average, 50x faster than the minute-level time cost of testing.

## Authors

The paper was submitted on October 26, 2025, with authors Junjielong Xu, Boyin Tan, Xiaoyuan Liu, Chao Peng, Pengfei Gao, and Pinjia He.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8b3bfb1-5682-4231-ba95-cf3c71321d26",
  "isSidechain": true,
  "promptId": "bca633b7-27f5-483b-9192-8c0cf0607331",
  "agentId": "acae1ebdea03f6d39",
  "type": "user",
  "uuid": "c38ec3a7-cd84-46e4-8eab-00e4e2caedde",
  "sourceToolAssistantUUID": "d8b3bfb1-5682-4231-ba95-cf3c71321d26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-10T17:49:19.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FAqi6rQjbrDnxvBumW6Lsy`</summary>

```json
{
  "query": "arXiv 2604.21598 \"DryRUN\" execution simulation self-correction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c38ec3a7-cd84-46e4-8eab-00e4e2caedde",
  "isSidechain": true,
  "agentId": "acae1ebdea03f6d39",
  "requestId": "req_011CauJwTB4EnLaXgGHX8iRH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efa0bd22-b50e-4e29-ab94-b2502e9f4774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mZo24ZqfaK9xpHeymF4Tc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 821,
      "cache_creation_input_tokens": 2739,
      "cache_read_input_tokens": 10554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2739,
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

_source line 15 · 2026-05-10T17:49:20.116Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WFJBd6foMRPZJYU6NELqsZ`</summary>

```json
{
  "query": "arXiv 2604.16529 \"Scaling Test-Time Compute for Agentic Coding\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efa0bd22-b50e-4e29-ab94-b2502e9f4774",
  "isSidechain": true,
  "agentId": "acae1ebdea03f6d39",
  "requestId": "req_011CauJwTB4EnLaXgGHX8iRH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be76ec3d-17b2-4185-9f70-0eadff38846e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mZo24ZqfaK9xpHeymF4Tc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 821,
      "cache_creation_input_tokens": 2739,
      "cache_read_input_tokens": 10554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2739,
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

_source line 16 · 2026-05-10T17:49:20.802Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T7252ar5MVGaTPbWQVhBQa`</summary>

```json
{
  "query": "arXiv 2601.22249 \"FunPRM\" function process reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be76ec3d-17b2-4185-9f70-0eadff38846e",
  "isSidechain": true,
  "agentId": "acae1ebdea03f6d39",
  "requestId": "req_011CauJwTB4EnLaXgGHX8iRH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bfb0e72-8ee1-485c-9af7-e1bdd2713256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mZo24ZqfaK9xpHeymF4Tc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 821,
      "cache_creation_input_tokens": 2739,
      "cache_read_input_tokens": 10554,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2739
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 821,
          "output_tokens": 186,
          "cache_read_input_tokens": 10554,
          "cache_creation_input_tokens": 2739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2739,
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

_source line 17 · 2026-05-10T17:49:26.666Z_

<details><summary>↩ Tool result · `toolu_01FAqi6rQjbrDnxvBumW6Lsy`</summary>

```text
Web search results for query: "arXiv 2604.21598 "DryRUN" execution simulation self-correction"

Links: [{"title":"You Don’t Need Public Tests to Generate Correct Code","url":"https://arxiv.org/html/2604.21598"},{"title":"[2604.21598] You Don't Need Public Tests to Generate Correct Code","url":"https://arxiv.org/abs/2604.21598"},{"title":"Self-Execution Simulation Improves Coding Models","url":"https://arxiv.org/html/2604.03253"},{"title":"[2604.19825] SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution","url":"https://arxiv.org/abs/2604.19825"},{"title":"[2603.21598] Systematic construction of digital autonomous quantum error correction for state preparation and error suppression via conditional Gaussian operations","url":"https://arxiv.org/abs/2603.21598"},{"title":"SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution","url":"https://arxiv.org/html/2604.19825"},{"title":"Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction","url":"https://arxiv.org/html/2510.14319v1"},{"title":"[2604.03253] Self-Execution Simulation Improves Coding Models","url":"https://arxiv.org/abs/2604.03253"},{"title":"Systematic construction of digital autonomous quantum error correction for state preparation and error suppression via conditional Gaussian operations","url":"https://arxiv.org/html/2603.21598"},{"title":"[2604.28181] Synthetic Computers at Scale for Long-Horizon Productivity Simulation","url":"https://arxiv.org/abs/2604.28181"}]

Based on the search results, I found the paper you're looking for:

## arXiv 2604.21598: "You Don't Need Public Tests to Generate Correct Code"

DryRUN is a framework that removes the necessity for ground-truth data by enabling the LLM to iteratively plan, synthesize its own test inputs, and run simulated executions, thereby mitigating algorithmic overconfidence.

**Key aspects of DryRUN:**

- **Problem addressed**: Existing simulation-guided methods rely heavily on human-authored public test cases, and hand-crafting exhaustive input-output pairs creates a significant, labor-intensive bottleneck.

- **Core capability**: Large language models possess the capability to autonomously construct valid inputs and simulate execution flows for self-correction.

- **Operating principle**: DryRUN operates under strictly zero-example constraints and shifts the burden of verification entirely inward, utilizing the LLM's ability to plan, autonomously synthesize inputs and simulate mental traces, eliminating the need for external oracles.

- **Performance**: Assessments using the LiveCodeBench v6 dataset (post-March 2025) reveal that DryRUN achieves comparable performance to CodeSIM, a state-of-the-art, test-dependent baseline, entirely without public tests or external execution signals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efa0bd22-b50e-4e29-ab94-b2502e9f4774",
  "isSidechain": true,
  "promptId": "bca633b7-27f5-483b-9192-8c0cf0607331",
  "agentId": "acae1ebdea03f6d39",
  "type": "user",
  "uuid": "0dff9c06-af55-4182-8182-c90965f09aee",
  "sourceToolAssistantUUID": "efa0bd22-b50e-4e29-ab94-b2502e9f4774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T17:49:28.653Z_

<details><summary>↩ Tool result · `toolu_01T7252ar5MVGaTPbWQVhBQa`</summary>

```text
Web search results for query: "arXiv 2601.22249 "FunPRM" function process reward model"

Links: [{"title":"[2601.22249] FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/abs/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://arxiv.org/html/2601.22249"},{"title":"FunPRM: Function-as-Step Process Reward Model with Meta Reward","url":"https://www.arxiv.org/pdf/2601.22249"},{"title":"(PDF) FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation","url":"https://www.researchgate.net/publication/400340056_FunPRM_Function-as-Step_Process_Reward_Model_with_Meta_Reward_Correction_for_Code_Generation"},{"title":"PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization","url":"https://arxiv.org/html/2601.07182"},{"title":"PROMISE: Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations","url":"https://arxiv.org/html/2601.04674"},{"title":"[2601.12748] Towards Robust Process Reward Modeling via Noise-aware Learning","url":"https://arxiv.org/abs/2601.12748"},{"title":"Towards Robust Process Reward Modeling via Noise-aware Learning","url":"https://arxiv.org/html/2601.12748"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=process+reward"},{"title":"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents","url":"https://arxiv.org/html/2601.12294"}]

Based on the search results, I found the paper arXiv 2601.22249 on FunPRM. Here's what it contains:

## Paper Summary

FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation is a research paper submitted on January 29, 2026, by authors Ruiyi Zhang, Peijia Qin, Qi Cao, Eric Xue, and Pengtao Xie.

## Problem and Solution

Code generation is a core application of large language models (LLMs), yet LLMs still frequently fail on complex programming tasks. While test-time scaling approaches such as Process Reward Model (PRM)-based Best-of-N selection offer promise, existing PRMs remain ineffective for code generation due to the lack of meaningful step decomposition in code and the noise of Monte Carlo-estimated partial-solution correctness scores.

## Key Approach

FunPRM prompts LLMs to encourage modular code generation organized into functions, with functions treated as PRM reasoning steps. Furthermore, FunPRM introduces a novel meta-learning-based reward correction mechanism that leverages clean final-solution rewards obtained via a unit-test-based evaluation system to purify noisy partial-solution rewards.

## Results

Experiments on LiveCodeBench and BigCodeBench demonstrate that FunPRM consistently outperforms existing test-time scaling methods across five base LLMs, notably achieving state-of-the-art performance on LiveCodeBench when combined with O4-mini. Furthermore, FunPRM produces code that is more readable and reusable for developers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bfb0e72-8ee1-485c-9af7-e1bdd2713256",
  "isSidechain": true,
  "promptId": "bca633b7-27f5-483b-9192-8c0cf0607331",
  "agentId": "acae1ebdea03f6d39",
  "type": "user",
  "uuid": "3899fd06-8927-4c52-9bab-1612e1b7b6e9",
  "sourceToolAssistantUUID": "3bfb0e72-8ee1-485c-9af7-e1bdd2713256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T17:49:29.410Z_

<details><summary>↩ Tool result · `toolu_01WFJBd6foMRPZJYU6NELqsZ`</summary>

```text
Web search results for query: "arXiv 2604.16529 "Scaling Test-Time Compute for Agentic Coding""

Links: [{"title":"[2604.16529] Scaling Test-Time Compute for Agentic Coding","url":"https://arxiv.org/abs/2604.16529"},{"title":"[Paper Note] Scaling Test-Time Compute for Agentic Coding, Joongwon Kim+, arXiv'26, 2026.04 · Issue #5307 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/5307"},{"title":"Scaling Test-Time Compute for Agentic Coding","url":"https://www.emergentmind.com/papers/2604.16529"},{"title":"Paper page - Scaling Test-Time Compute for Agentic Coding","url":"https://huggingface.co/papers/2604.16529"},{"title":"Scaling Test-Time Compute for Agentic Coding - ArXivIQ","url":"https://arxiviq.substack.com/p/scaling-test-time-compute-for-agentic"},{"title":"Implementation of recent meta ai paper - projects - PyTorch Forums","url":"https://discuss.pytorch.org/t/implementation-of-recent-meta-ai-paper/224893"},{"title":"Software Engineering","url":"https://arxiv.org/list/cs.SE/pastweek?skip=64&show=50"},{"title":"Scaling Test-Time Compute for Agentic Coding Kim et al. ...","url":"https://www.facebook.com/ceobillionairetv/posts/scaling-test-time-compute-for-agentic-codingkim-et-al-httpsarxivorgabs260416529a/26668407972789426/"},{"title":"Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations","url":"https://arxiv.org/html/2604.21018"},{"title":"[2602.12276] Agentic Test-Time Scaling for WebAgents","url":"https://arxiv.org/abs/2602.12276"}]

I found the paper! Here's a summary of arXiv 2604.16529 "Scaling Test-Time Compute for Agentic Coding":

## Overview

The paper proposes a test-time scaling framework for agentic coding based on compact representations of rollout trajectories.

## Problem Statement

Test-time scaling has become a powerful way to improve large language models, but existing methods are best suited to short, bounded outputs that can be directly compared, ranked or refined. Long-horizon coding agents violate this premise: each attempt produces an extended trajectory of actions, observations, errors, and partial progress taken by the agent.

## Proposed Solution

The framework converts each rollout into a structured summary that preserves its salient hypotheses, progress, and failure modes while discarding low-signal trace details. This representation enables two complementary forms of inference-time scaling.

The two approaches are:
- Recursive Tournament Voting (RTV), which recursively narrows a population of rollout summaries through small-group comparisons
- Parallel-Distill-Refine (PDR) adapted to the agentic setting by conditioning new rollouts on summaries distilled from prior attempts

## Results

The method consistently improves the performance of frontier coding agents across SWE-Bench Verified and Terminal-Bench v2.0. For example, by using the method Claude-4.5-Opus improves from 70.9% to 77.6% on SWE-Bench Verified (mini-SWE-agent) and 46.9% to 59.1% on Terminal-Bench v2.0 (Terminus 1).

The researchers from Meta and their academic collaborators introduced this framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be76ec3d-17b2-4185-9f70-0eadff38846e",
  "isSidechain": true,
  "promptId": "bca633b7-27f5-483b-9192-8c0cf0607331",
  "agentId": "acae1ebdea03f6d39",
  "type": "user",
  "uuid": "0e65b9e4-0820-472d-a9a0-b1352e149e56",
  "sourceToolAssistantUUID": "be76ec3d-17b2-4185-9f70-0eadff38846e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T17:50:06.647Z_

Here are my findings for each paper:

---

## Paper 1: "Self-Execution Simulation Improves Coding Models" (arXiv:2604.03253)

**Exists:** Yes

**Actual claims:** The paper demonstrates that Code LLMs can be trained to simulate program execution step-by-step, and this can improve competitive programming performance. It combines supervised fine-tuning on natural language execution traces with reinforcement learning using verifiable rewards. Models can then perform self-verification and iterative self-fixing by simulating test execution.

**Discrepancies:** The claimed "~80% accuracy" for simulating execution traces was not specifically confirmed in the search results. The paper's focus is broader -- it's about training models to simulate execution and using that for self-verification/self-fixing in competitive programming, rather than simply measuring simulation accuracy. The "~80%" figure may be an oversimplification or fabrication of a specific result.

---

## Paper 2: "CodeScaler" (arXiv:2602.17684)

**Exists:** Yes

**Actual claims:** CodeScaler improves Qwen3-8B-Base by an average of +11.72 points across five coding benchmarks, outperforming binary execution-based RL by +1.82 points. It also provides 10x reduction in inference latency compared to unit test approaches.

**Discrepancies:** The claim of "+11.72 points on Qwen3-8B" is **confirmed and accurate**. Note: the improvement is on Qwen3-8B-**Base**, and it's an average across five benchmarks. No significant discrepancy.

---

## Paper 3: "Scalable Supervising Software Agents with Patch Reasoner" (arXiv:2510.22775)

**Exists:** Yes

**Actual claims:** R4P achieves 72.2% accuracy for **verifying patches** from SWE-bench Verified (not resolving issues). Pass@1 resolution rate reaches 26.2% (up to 32.8% with R4P for patch selection). R4P verifies each patch within a second on average, 50x faster than testing.

**Discrepancies:** The "72.2% on SWE-bench Verified" claim is **misleading as described**. The 72.2% is the patch **verification accuracy** (i.e., correctly identifying whether a patch is correct), NOT a resolution/solve rate on SWE-bench Verified. The actual resolution rate is 26.2-32.8%. The "50x faster" claim is accurate but refers to verification speed vs. running tests. The original description makes it sound like 72.2% is a solve rate, which it is not.

---

## Paper 4: "S*: Test Time Scaling for Code Generation" (arXiv:2502.14382)

**Exists:** Yes

**Actual claims:** S* is a hybrid test-time scaling framework combining parallel and sequential scaling. It uses a novel selection mechanism that generates distinguishing inputs for pairwise comparison. A 3B model can outperform GPT-4o-mini; GPT-4o-mini with S* outperforms o1-preview by 3.7% on LiveCodeBench.

**Discrepancies:** The claimed description that S* shows "imperfect verifiers enable effective test-time scaling" is a **reasonable but incomplete summary**. The paper is more specifically about a hybrid framework that generates distinguishing test inputs for selection, not just about imperfect verifiers in general. The paper's novelty is in the selection mechanism using execution-grounded information, not merely observing that imperfect verifiers work.

---

## Paper 5: "DryRUN" (arXiv:2604.21598)

**Exists:** Yes, but the actual title is **"You Don't Need Public Tests to Generate Correct Code"** (DryRUN is the method name)

**Actual claims:** DryRUN enables LLMs to iteratively plan, synthesize their own test inputs, and run simulated executions for self-correction -- all without any public test cases. It achieves comparable performance to test-dependent baselines on LiveCodeBench v6.

**Discrepancies:** The description of "prompt-based execution simulation for self-correction" is **broadly accurate**. The key nuance is that DryRUN specifically operates under zero-example constraints (no public tests at all) and the LLM autonomously constructs inputs and simulates execution. The framing is correct.

---

## Paper 6: "Scaling Test-Time Compute for Agentic Coding" (arXiv:2604.16529)

**Exists:** Yes

**Actual claims:** The paper proposes converting long rollout trajectories into structured summaries, then using Recursive Tournament Voting (RTV) and Parallel-Distill-Refine (PDR) for test-time scaling. Claude-4.5-Opus improves from 70.9% to 77.6% on SWE-Bench Verified.

**Discrepancies:** The claim says "Claude Opus 4.5" which matches the paper's reported result. The improvement from 70.9% to 77.6% is **confirmed accurate**. However, note this is specifically with the "mini-SWE-agent" setup. The paper is from Meta and collaborators, not from Anthropic. No major discrepancy.

---

## Paper 7: "FunPRM: Function-as-Step Process Reward Model" (arXiv:2601.22249)

**Exists:** Yes

**Full title:** "FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation"

**Actual claims:** FunPRM treats functions as PRM reasoning steps (prompting LLMs to generate modular code organized into functions). It introduces a meta-learning-based reward correction mechanism. It consistently outperforms existing test-time scaling methods across five base LLMs on LiveCodeBench and BigCodeBench, achieving state-of-the-art when combined with O4-mini.

**Discrepancies:** The description provided was just the paper name with no specific claims to verify. The paper exists and is legitimate.

---

## Summary

| Paper | Exists? | Claims Accurate? |
|-------|---------|-----------------|
| 1. Self-Execution Simulation | Yes | "~80% accuracy" not confirmed; may be embellished |
| 2. CodeScaler | Yes | +11.72 on Qwen3-8B confirmed |
| 3. Patch Reasoner | Yes | **72.2% is verification accuracy, NOT solve rate** -- misleading |
| 4. S* | Yes | Broadly accurate but oversimplified |
| 5. DryRUN | Yes | Accurate (title is actually "You Don't Need Public Tests") |
| 6. Scaling Test-Time Compute | Yes | 70.9% to 77.6% confirmed |
| 7. FunPRM | Yes | Exists, no specific claims to dispute |

The most significant discrepancy is Paper 3, where 72.2% is presented as if it were a SWE-bench solve rate when it is actually a patch verification accuracy score (the actual solve rate is 26-33%).

Sources:
- [Self-Execution Simulation Improves Coding Models](https://arxiv.org/abs/2604.03253)
- [CodeScaler](https://arxiv.org/abs/2602.17684)
- [Scalable Supervising Software Agents with Patch Reasoner](https://arxiv.org/abs/2510.22775)
- [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)
- [You Don't Need Public Tests to Generate Correct Code (DryRUN)](https://arxiv.org/abs/2604.21598)
- [Scaling Test-Time Compute for Agentic Coding](https://arxiv.org/abs/2604.16529)
- [FunPRM](https://arxiv.org/abs/2601.22249)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e65b9e4-0820-472d-a9a0-b1352e149e56",
  "isSidechain": true,
  "agentId": "acae1ebdea03f6d39",
  "requestId": "req_011CauJxUnKXEoSq1CFrY6Sv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c6be92a-0189-46aa-a1c8-7ab1362c9621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8f33ca80-8bf9-4950-8364-3c9f92158895",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gz2F7UuJ8d2J4hZMHfGJr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 903,
      "cache_creation_input_tokens": 2784,
      "cache_read_input_tokens": 13293,
      "output_tokens": 1914,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 903,
          "output_tokens": 1914,
          "cache_read_input_tokens": 13293,
          "cache_creation_input_tokens": 2784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2784,
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
