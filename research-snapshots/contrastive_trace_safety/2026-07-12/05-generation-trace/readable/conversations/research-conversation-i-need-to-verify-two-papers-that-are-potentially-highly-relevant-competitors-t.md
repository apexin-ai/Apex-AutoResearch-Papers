# Research conversation: I need to verify two papers that are potentially highly relevant competitors to an idea about "using test assertions as 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5aa92c928bbf2f25.jsonl`
- **Structured JSON:** [`7ad0279120df49f9d8e5.json`](../../sessions/7a/7ad0279120df49f9d8e5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-12T00:02:10.628Z_

I need to verify two papers that are potentially highly relevant competitors to an idea about "using test assertions as structured behavioral specifications for code repair":

1. **SpecRover / AutoCodeRover-v2 (ICSE 2025, arXiv 2408.02232)** - Claimed to perform iterative specification inference to guide patching, extracting function summaries and "intended behavior" during context retrieval. Achieves 50%+ improvement over AutoCodeRover on full SWE-Bench at $0.65/issue.

2. **CodeSpecBench (arXiv 2604.12268, Apr 2026)** - A benchmark for executable behavioral specification generation. Claims even the best LLM (Claude-4.5-Sonnet) achieves only 20.2% pass rate on repository-level behavioral specification tasks.

For each paper:
- Use WebSearch to find the paper and verify it exists
- Try to read the abstract/key sections with WebFetch if possible
- Verify the specific claimed numbers
- Assess how directly relevant each is to "extracting structured behavioral specifications from test assertions for code repair"

Also search for:
- "test overfitting automated program repair LLM 2026" - to find the ICSE 2026 paper about undecidability of test overfitting in APR
- "CURE co-evolve coder tester reinforcement learning NeurIPS 2025" - to verify CURE exists

Report findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "4cabc0c2-f9da-4c27-95f9-9e75f0fdae84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:02:10.632Z_

```json
{
  "parentUuid": "4cabc0c2-f9da-4c27-95f9-9e75f0fdae84",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
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
  "uuid": "2412fdc8-55ac-4bcf-a253-83eb51c13d61",
  "timestamp": "2026-05-12T00:02:10.632Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:02:13.158Z_



I'll search for all four papers in parallel to verify their existence and claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2412fdc8-55ac-4bcf-a253-83eb51c13d61",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhBjjfsPSzdUiWWD4XU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01b26489-1fb5-44bc-adf1-e8c79c870d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtkJJEQDiS66gJ94HhFzYh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 885,
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

_source line 4 · 2026-05-12T00:02:13.269Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014V7zyz1HDEZdg6j3Ud7Mtn`</summary>

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
  "parentUuid": "01b26489-1fb5-44bc-adf1-e8c79c870d75",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhBjjfsPSzdUiWWD4XU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "688ba59c-bfa7-4d92-841b-9d93b7b99018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtkJJEQDiS66gJ94HhFzYh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 8223,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 885
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 885,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 885,
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

_source line 5 · 2026-05-12T00:02:13.272Z_

<details><summary>↩ Tool result · `toolu_014V7zyz1HDEZdg6j3Ud7Mtn`</summary>

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
  "parentUuid": "688ba59c-bfa7-4d92-841b-9d93b7b99018",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "af15c7f1-471f-4727-80d6-545b14effdc4",
  "sourceToolAssistantUUID": "688ba59c-bfa7-4d92-841b-9d93b7b99018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:02:16.009Z_



Now let me search for all four papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af15c7f1-471f-4727-80d6-545b14effdc4",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhBwEirdvEc6tvfCP9i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5b21ea7-102f-44cb-b8b0-1b58f0cfff67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012N6cX6nuoYcKyuKhFX9Yru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 7 · 2026-05-12T00:02:17.423Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SHZrBe4Yac8BTJuJ5gsz4H`</summary>

```json
{
  "query": "SpecRover AutoCodeRover-v2 ICSE 2025 arXiv 2408.02232 specification inference program repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5b21ea7-102f-44cb-b8b0-1b58f0cfff67",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhBwEirdvEc6tvfCP9i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6494937-c0a7-4060-88e0-1d01a433208a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012N6cX6nuoYcKyuKhFX9Yru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 8 · 2026-05-12T00:02:18.370Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016ib6sWQA4jnz4M1i9okJaj`</summary>

```json
{
  "query": "CodeSpecBench arXiv 2604.12268 executable behavioral specification generation benchmark LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6494937-c0a7-4060-88e0-1d01a433208a",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhBwEirdvEc6tvfCP9i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b28dca2-c3af-49dc-90e8-7317ccf22197",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012N6cX6nuoYcKyuKhFX9Yru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 9 · 2026-05-12T00:02:19.311Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015bzov86qkF4JeVW9C5ohoi`</summary>

```json
{
  "query": "test overfitting automated program repair LLM undecidability ICSE 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b28dca2-c3af-49dc-90e8-7317ccf22197",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhBwEirdvEc6tvfCP9i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1958a4b-7acc-4763-b9b9-94f68b7936fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012N6cX6nuoYcKyuKhFX9Yru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1906,
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

_source line 10 · 2026-05-12T00:02:19.884Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PazWBxehmXQxq2Qci1hrVH`</summary>

```json
{
  "query": "CURE co-evolve coder tester reinforcement learning NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1958a4b-7acc-4763-b9b9-94f68b7936fc",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhBwEirdvEc6tvfCP9i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52513717-4986-461d-b6be-67a25911d701",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012N6cX6nuoYcKyuKhFX9Yru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 9108,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1906
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 9108,
          "cache_creation_input_tokens": 1906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1906,
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

_source line 11 · 2026-05-12T00:02:22.868Z_

<details><summary>↩ Tool result · `toolu_01SHZrBe4Yac8BTJuJ5gsz4H`</summary>

```text
Web search results for query: "SpecRover AutoCodeRover-v2 ICSE 2025 arXiv 2408.02232 specification inference program repair"

Links: [{"title":"[2408.02232] SpecRover: Code Intent Extraction via LLMs","url":"https://arxiv.org/abs/2408.02232"},{"title":"SpecRover: Code Intent Extraction via LLMs *Joint first authors, ordered alphabetically.","url":"https://arxiv.org/html/arXiv:2408.02232"},{"title":"SpecRover: Code Intent Extraction via LLMs Haifeng Ruan* Yuntong Zhang*","url":"https://arxiv.org/pdf/2408.02232"},{"title":"GitHub - zanwenfu/auto-code-rover: A project structure aware autonomous software engineer aiming for autonomous program improvement. Resolved 37.3% tasks (pass@1) in SWE-bench lite and 51.6% tasks (pass@3) in SWE-bench verified with each task costs less than $0.7. · GitHub","url":"https://github.com/zanwenfu/auto-code-rover"},{"title":"publications | Yuntong Zhang","url":"https://yuntongzhang.github.io/publications/"},{"title":"SpecRover: Code Intent Extraction via LLMs (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/68/SpecRover-Code-Intent-Extraction-via-LLMs"},{"title":"Software Engineering Aug 2024","url":"https://www.arxiv.org/list/cs.SE/2024-08?skip=10&show=2000"},{"title":"[2404.05427] AutoCodeRover: Autonomous Program Improvement","url":"https://arxiv.org/abs/2404.05427"},{"title":"SpecRover: Code Intent Extraction via LLMs | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/specrover-code-intent-extraction-via-llms"},{"title":"(PDF) SpecRover: Code Intent Extraction via LLMs","url":"https://www.researchgate.net/publication/382885291_SpecRover_Code_Intent_Extraction_via_LLMs"}]

Based on the search results, I found comprehensive information about SpecRover:

## SpecRover: Code Intent Extraction via LLMs

SpecRover (AutoCodeRover-v2) is built on the open-source LLM agent AutoCodeRover. The paper "SpecRover: Code Intent Extraction via LLMs" by Haifeng Ruan and Yuntong Zhang is to appear in ICSE 2025 and is available on arXiv as 2408.02232.

### Key Contributions

Since program repair typically requires a specification of intended behavior, the work examines efficient and low-cost workflows for iterative specification inference within an LLM agent. The work looks into various sources of specifications such as function-level code summaries and testcases, apart from program structure.

### Approach

Given a GitHub issue to be resolved in a software project, the goal is to conduct iterative code search accompanied by specification inference—thereby inferring intent from both the project structure and behavior. The intent is examined by a reviewer agent with the goal of vetting the patches as well as providing a measure of confidence in the vetted patches.

### Performance Results

In an evaluation on the full SWE-Bench consisting of 2294 GitHub issues, it shows more than 50% improvement in efficacy over AutoCodeRover. The approach shows modest cost ($0.65 per issue) in resolving an average GitHub issue in SWE-Bench lite.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6494937-c0a7-4060-88e0-1d01a433208a",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "ca45d91f-9eb7-40c3-bfe5-0abb4cfbdf20",
  "sourceToolAssistantUUID": "d6494937-c0a7-4060-88e0-1d01a433208a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T00:02:25.290Z_

<details><summary>↩ Tool result · `toolu_016ib6sWQA4jnz4M1i9okJaj`</summary>

```text
Web search results for query: "CodeSpecBench arXiv 2604.12268 executable behavioral specification generation benchmark LLM"

Links: [{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"[2604.12268] CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/abs/2604.12268"},{"title":"Beyond Synthetic Benchmarks: Evaluating LLM Performance on Real-World Class-Level Code Generation","url":"https://arxiv.org/html/2510.26130v2"},{"title":"Paper page - QuantCode-Bench: A Benchmark for Evaluating the Ability of Large Language Models to Generate Executable Algorithmic Trading Strategies","url":"https://huggingface.co/papers/2604.15151"},{"title":"Evaluating LLM-Based 0-to-1 Software Generation in End-to-End CLI Tool Scenarios","url":"https://arxiv.org/html/2604.06742"},{"title":"[2410.21071] Automatic Generation of Benchmarks and Reliable LLM Judgment for Code Tasks","url":"https://arxiv.org/abs/2410.21071"},{"title":"HardSecBench: Benchmarking the Security Awareness of LLMs for Hardware Code Generation","url":"https://arxiv.org/html/2601.13864v1"},{"title":"ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research Code","url":"https://arxiv.org/html/2506.02314v1"},{"title":"[2510.26130] Beyond Synthetic Benchmarks: Evaluating LLM Performance on Real-World Class-Level Code Generation","url":"https://arxiv.org/abs/2510.26130"},{"title":"BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions","url":"https://arxiv.org/html/2406.15877v4"}]

Based on the search results, I found detailed information about CodeSpecBench:

## CodeSpecBench Overview

CodeSpecBench is a benchmark for executable behavioral specification generation under an execution-based evaluation protocol. The paper (arXiv:2604.12268) was submitted on April 14, 2026 by researchers from The Hong Kong Polytechnic University, University of Edinburgh, UCL, CUHK, SUTD, and HKUST.

## Key Features

Executable behavioral specifications, defined via preconditions and postconditions, provide a concrete means to assess whether LLMs understand intended program behavior. CodeSpecBench supports both function-level and repository-level tasks and encodes specifications as executable Python functions. Constructed from diverse real-world codebases, it enables a realistic assessment of both correctness (accepting valid behaviors) and completeness (rejecting invalid behaviors).

## Evaluation Results

Evaluating 15 state-of-the-art LLMs on CodeSpecBench, researchers observed a sharp performance degradation on repository-level tasks, where the best model attained only a 20.2% pass rate. Specification generation was found to be substantially more challenging than code generation, indicating that strong coding performance does not necessarily reflect deep understanding of intended program semantics.

The data and code are available at https://github.com/SparksofAGI/CodeSpecBench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b28dca2-c3af-49dc-90e8-7317ccf22197",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "0d1f89d0-b9fd-4b1c-a11c-286631eb4ff2",
  "sourceToolAssistantUUID": "8b28dca2-c3af-49dc-90e8-7317ccf22197",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:02:27.967Z_

<details><summary>↩ Tool result · `toolu_01PazWBxehmXQxq2Qci1hrVH`</summary>

```text
Web search results for query: "CURE co-evolve coder tester reinforcement learning NeurIPS 2025"

Links: [{"title":"GitHub - Gen-Verse/CURE: [NeurIPS 2025 Spotlight] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning · GitHub","url":"https://github.com/Gen-Verse/CURE"},{"title":"NeurIPS Poster CURE: Co-Evolving Coders and Unit Testers via Reinforcement Learning","url":"https://neurips.cc/virtual/2025/poster/115329"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=wPdBe9zxNr"},{"title":"[2506.03136] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/abs/2506.03136"},{"title":"CURE: Co-Evolving Coders and Unit Testers via Reinforcement Learning | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/wPdBe9zxNr@OpenReview"},{"title":"[2506.03136v1] Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/abs/2506.03136v1"},{"title":"CURE: Co-Evolving Coders and Unit Testers via Reinforcement Learning","url":"https://openreview.net/pdf/6be4b1f5dff8b39f2e222dc06ccafec29b4f4ec0.pdf"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning","url":"https://arxiv.org/html/2506.03136"},{"title":"GitHub - Gen-Verse/ReasonFlux: [NeurIPS 2025 Spotlight] LLM post-training suite — featuring ReasonFlux, ReasonFlux-PRM, and ReasonFlux-Coder.","url":"https://github.com/Gen-Verse/ReasonFlux"},{"title":"Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning |…","url":"https://www.opentrain.ai/papers/co-evolving-llm-coder-and-unit-tester-via-reinforcement-learning--arxiv-2506.03136/"}]

I found comprehensive information about CURE. Here's what the search revealed:

## CURE: Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning

CURE is a NeurIPS 2025 Spotlight paper on co-evolving LLM coder and unit tester via reinforcement learning.

### Core Framework

CURE is a novel reinforcement learning framework with a dedicated reward design that co-evolves coding and unit test generation capabilities based on their interaction outcomes—without any ground-truth code as supervision. This approach enables flexible and scalable training and allows the unit tester to learn directly from the coder's mistakes.

### Key Innovation

Unit test generation is highlighted as a key factor for enhancing coding ability, since accurate unit tests are essential for enabling self-checking and self-correction during inference. The unit tester requires no ground-truth code in the training data—it automatically learns from the coder's mistakes during the RL rollout process.

### Results and Models

Optimized models ReasonFlux-Coder-7B and ReasonFlux-Coder-14B outperform similarly sized Qwen Coders and DeepSeek Coders, and naturally fit into common test-time scaling and agentic coding pipelines. The models achieve a 6.2% improvement over the base model in test-time scaling—and a 25.1% improvement in agentic unit test generation.

### Code and Implementation

The code is available on GitHub, with the paper available on arXiv as arXiv:2506.03136.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52513717-4986-461d-b6be-67a25911d701",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "5ebc3d7c-fa74-4a97-90c3-b4871356ac76",
  "sourceToolAssistantUUID": "52513717-4986-461d-b6be-67a25911d701",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T00:02:28.270Z_

<details><summary>↩ Tool result · `toolu_015bzov86qkF4JeVW9C5ohoi`</summary>

```text
Web search results for query: "test overfitting automated program repair LLM undecidability ICSE 2026"

Links: [{"title":"The Undecidability of Overfitting in Automated Program Repair (ICSE 2026 - New Ideas and Emerging Results (NIER)) - ICSE 2026","url":"https://conf.researchr.org/details/icse-2026/icse-2026-nier/4/The-Undecidability-of-Overfitting-in-Automated-Program-Repair"},{"title":"Is the Cure Still Worse Than the Disease? Test Overfitting ...","url":"https://www.arxiv.org/pdf/2511.16858"},{"title":"Automated Repair of Programs from Large Language Models Zhiyu Fan","url":"https://abhikrc.com/pdf/ICSE23.pdf"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Evaluating the Generalizability of LLMs in Automated Program Repair","url":"https://arxiv.org/html/2503.09217"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Is the Cure Still Worse Than the Disease? Test Overfitting by LLMs in Automated Program Repair","url":"https://arxiv.org/html/2511.16858v1"},{"title":"2025 IEEE/ACM 47th International Conference on Software ...","url":"https://www.computer.org/csdl/proceedings/icse/2025/215aVCUIQmY"},{"title":"Calibration and Correctness of Language Models for Code Claudio Spiess∗","url":"https://www.software-lab.org/publications/icse2025_calibration.pdf"},{"title":"AwesomeLLM4APR/README.md at main · iSEngLab/AwesomeLLM4APR","url":"https://github.com/iSEngLab/AwesomeLLM4APR/blob/main/README.md"}]

Based on the search results, I found highly relevant information about your query. Here are the key findings:

## ICSE 2026 Paper on Undecidability and Overfitting

There is a paper at ICSE 2026 that presents the view that overfitting is not just a nuisance but a fundamental consequence of undecidability. Overfitting is one of the most persistent challenges in automated program repair (APR), typically attributed to weak or incomplete test suites. However, when full specifications are unavailable, test suites serve only as partial correctness oracles, and overfitting emerges as a structural outcome rather than an incidental defect.

## Recent Research on Test Overfitting with LLMs

Additionally, there is recent research examining test overfitting in LLM-based APR. Test overfitting occurs when code generated by APR passes white-box tests but fails black-box tests. Research confirms that LLMs can and do overfit on white-box tests. When improving code based on white-box tests, overfitting goes up for affected instances.

The research indicates that while APR with white-box tests improves performance on black-box tests on average, there is still test overfitting to beware of—the cure can still cause harm.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1958a4b-7acc-4763-b9b9-94f68b7936fc",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "0cbe260e-1667-4879-8efe-0882003bf252",
  "sourceToolAssistantUUID": "d1958a4b-7acc-4763-b9b9-94f68b7936fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-12T00:02:32.153Z_

All four papers found. Now let me fetch the actual paper pages to verify the specific claimed numbers and assess relevance more deeply.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cbe260e-1667-4879-8efe-0882003bf252",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhD38DJERsepMTYdWYD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4566f4bc-d4de-4dbf-a1a6-da8fc2faafcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9cWm7dwmEKCeGhMo2jYFP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1034,
      "cache_creation_input_tokens": 3035,
      "cache_read_input_tokens": 11014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3035,
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

_source line 16 · 2026-05-12T00:02:35.034Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MB5nzJkVRvLbFSqbQKAKNi`</summary>

```json
{
  "url": "https://arxiv.org/abs/2408.02232",
  "prompt": "Extract the full abstract. Identify: (1) the exact performance improvement claimed over AutoCodeRover, (2) the cost per issue, (3) whether it uses test assertions as behavioral specifications, (4) what \"specification inference\" means in this paper specifically, (5) the SWE-Bench results numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4566f4bc-d4de-4dbf-a1a6-da8fc2faafcc",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhD38DJERsepMTYdWYD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12bf89b1-29d5-4187-a6ff-3056f02bfc2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9cWm7dwmEKCeGhMo2jYFP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1034,
      "cache_creation_input_tokens": 3035,
      "cache_read_input_tokens": 11014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3035,
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

_source line 17 · 2026-05-12T00:02:37.961Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RtER4GzRC1XUGNV9fMnrzi`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.12268",
  "prompt": "Extract the full abstract. Identify: (1) the exact pass rate numbers for Claude-4.5-Sonnet and other models, (2) what \"executable behavioral specifications\" means in this paper (preconditions/postconditions?), (3) the difference between function-level and repository-level tasks, (4) how many models were evaluated, (5) what the benchmark consists of exactly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12bf89b1-29d5-4187-a6ff-3056f02bfc2b",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhD38DJERsepMTYdWYD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac4c7110-225a-40c9-9828-31d3d9d0fc18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9cWm7dwmEKCeGhMo2jYFP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1034,
      "cache_creation_input_tokens": 3035,
      "cache_read_input_tokens": 11014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3035,
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

_source line 18 · 2026-05-12T00:02:40.168Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016bgXYiNF8Hum3X6YVu2Bjo`</summary>

```json
{
  "url": "https://conf.researchr.org/details/icse-2026/icse-2026-nier/4/The-Undecidability-of-Overfitting-in-Automated-Program-Repair",
  "prompt": "Extract all details about this paper: title, authors, abstract, key claims about undecidability and test overfitting in automated program repair. What is the main thesis?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac4c7110-225a-40c9-9828-31d3d9d0fc18",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhD38DJERsepMTYdWYD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32bb1d19-6e64-4d1e-a0b6-269eaba465d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9cWm7dwmEKCeGhMo2jYFP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1034,
      "cache_creation_input_tokens": 3035,
      "cache_read_input_tokens": 11014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3035,
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

_source line 19 · 2026-05-12T00:02:41.885Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RXURTTt4PZ9R25LvKZwuZ5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.03136",
  "prompt": "Extract the full abstract. Identify: (1) what CURE stands for, (2) how the coder and tester co-evolve, (3) the exact performance numbers claimed, (4) whether it uses test assertions as specifications for code repair specifically, (5) the key innovation regarding unit test generation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32bb1d19-6e64-4d1e-a0b6-269eaba465d6",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhD38DJERsepMTYdWYD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02cb0d54-8594-432f-8be4-55413a8cd137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9cWm7dwmEKCeGhMo2jYFP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1034,
      "cache_creation_input_tokens": 3035,
      "cache_read_input_tokens": 11014,
      "output_tokens": 599,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3035
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1034,
          "output_tokens": 599,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3035,
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

_source line 20 · 2026-05-12T00:02:43.299Z_

<details><summary>↩ Tool result · `toolu_01MB5nzJkVRvLbFSqbQKAKNi`</summary>

```text
# SpecRover Paper Analysis

## Full Abstract
"Autonomous program improvement typically involves automatically producing bug fixes and feature additions. Such program improvement can be accomplished by a combination of large language model (LLM) and program analysis capabilities, in the form of an LLM agent. Since program repair or program improvement typically requires a specification of intended behavior - specification inference can be useful for producing high quality program patches. In this work, we examine efficient and low-cost workflows for iterative specification inference within an LLM agent. Given a GitHub issue to be resolved in a software project, our goal is to conduct iterative code search accompanied by specification inference - thereby inferring intent from both the project structure and behavior. The intent thus captured is examined by a reviewer agent with the goal of vetting the patches as well as providing a measure of confidence in the vetted patches. Our approach SpecRover (AutoCodeRover-v2) is built on the open-source LLM agent AutoCodeRover. In an evaluation on the full SWE-Bench consisting of 2294 GitHub issues, it shows more than 50% improvement in efficacy over AutoCodeRover. Compared to the open-source agents available, our work shows modest cost ($0.65 per issue) in resolving an average GitHub issue in SWE-Bench lite. The production of explanation by SpecRover allows for a better "signal" to be given to the developer, on when the suggested patches can be accepted with confidence. SpecRover also seeks to demonstrate the continued importance of specification inference in automated program repair, even as program repair technologies enter the LLM era."

## Key Findings

**(1) Performance Improvement:** "more than 50% improvement in efficacy over AutoCodeRover"

**(2) Cost Per Issue:** $0.65 per issue on SWE-Bench lite

**(3) Test Assertions:** Not mentioned in the abstract or webpage content provided.

**(4) Specification Inference Definition:** The paper describes it as inferring intent "from both the project structure and behavior" through iterative code search to identify intended behavior for generating high-quality patches.

**(5) SWE-Bench Results:** Evaluated on "full SWE-Bench consisting of 2294 GitHub issues" with >50% improvement; specific resolution numbers not provided in this content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12bf89b1-29d5-4187-a6ff-3056f02bfc2b",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "87354ecf-a969-4fc7-b305-724159d59af0",
  "sourceToolAssistantUUID": "12bf89b1-29d5-4187-a6ff-3056f02bfc2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T00:02:43.996Z_

<details><summary>↩ Tool result · `toolu_01RtER4GzRC1XUGNV9fMnrzi`</summary>

```text
# CodeSpecBench Paper Analysis

## Full Abstract
"Large language models (LLMs) can generate code from natural language, but the extent to which they capture intended program behavior remains unclear. Executable behavioral specifications, defined via preconditions and postconditions, provide a concrete means to assess such understanding. However, existing work on specification generation is constrained in evaluation methodology, task settings, and specification expressiveness. We introduce CodeSpecBench, a benchmark for executable behavioral specification generation under an execution-based evaluation protocol. CodeSpecBench supports both function-level and repository-level tasks and encodes specifications as executable Python functions. Constructed from diverse real-world codebases, it enables a realistic assessment of both correctness (accepting valid behaviors) and completeness (rejecting invalid behaviors). Evaluating 15 state-of-the-art LLMs on CodeSpecBench, we observe a sharp performance degradation on repository-level tasks, where the best model attains only a 20.2% pass rate."

## Key Findings

**(1) Pass Rate Numbers:** The abstract reports only that "the best model attains only a 20.2% pass rate" on repository-level tasks. No specific Claude-4.5-Sonnet results are provided in this webpage content.

**(2) Executable Behavioral Specifications:** These are "defined via preconditions and postconditions," encoded as executable Python functions to assess whether LLMs understand intended program behavior.

**(3) Task Level Differences:** Function-level tasks target individual functions, while repository-level tasks evaluate performance across entire codebases—showing substantially greater difficulty.

**(4) Models Evaluated:** "15 state-of-the-art LLMs" were assessed, though individual model names aren't listed in this excerpt.

**(5) Benchmark Composition:** CodeSpecBench consists of "diverse real-world codebases" with both correctness and completeness evaluation criteria, though specific dataset size isn't detailed here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac4c7110-225a-40c9-9828-31d3d9d0fc18",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "cbd659d6-9f09-499c-a05c-bbfc7208a47c",
  "sourceToolAssistantUUID": "ac4c7110-225a-40c9-9828-31d3d9d0fc18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T00:02:46.449Z_

<details><summary>↩ Tool result · `toolu_016bgXYiNF8Hum3X6YVu2Bjo`</summary>

```text
# Paper Details: "The Undecidability of Overfitting in Automated Program Repair"

**Author:** Omar I. Al-Bataineh (Gran Sasso Science Institute - GSSI)

**Track:** ICSE 2026 New Ideas and Emerging Results (NIER)

**Presentation:** Thursday, April 16, 2026, 16:00-16:15 (Brasilia time)

## Abstract

The paper challenges conventional thinking about overfitting in automated program repair. Rather than treating overfitting as a fixable problem, the authors argue it represents a fundamental, unavoidable consequence of incomplete specifications. 

## Main Thesis

When full program specifications remain unavailable, test suites function only as partial correctness oracles. This limitation makes overfitting "a structural outcome rather than an incidental defect." The authors contend that overfitting constitutes an "inherent boundary of the problem itself" rather than a solvable bug.

## Key Claims

1. **Undecidability Foundation:** Overfitting emerges from the theoretical undecidability problem when complete specifications are absent

2. **Reframed Perspective:** The problem should be understood as a fundamental limit rather than a technical shortcoming

3. **Research Direction:** Instead of eliminating overfitting, future work should focus on quantifying, explaining, and reasoning about it as unavoidable

This represents a paradigm shift—moving from "how do we fix overfitting?" to "how do we work within these fundamental constraints?"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32bb1d19-6e64-4d1e-a0b6-269eaba465d6",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "70a00c20-56f7-44c5-b70b-73f700f193b9",
  "sourceToolAssistantUUID": "32bb1d19-6e64-4d1e-a0b6-269eaba465d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T00:02:48.264Z_

<details><summary>↩ Tool result · `toolu_01RXURTTt4PZ9R25LvKZwuZ5`</summary>

```text
# Analysis of CURE Paper

## Full Abstract
"We propose CURE, a novel reinforcement learning framework with a dedicated reward design that co-evolves coding and unit test generation capabilities based on their interaction outcomes, without any ground-truth code as supervision. This approach enables flexible and scalable training and allows the unit tester to learn directly from the coder's mistakes. Our derived ReasonFlux-Coder-7B and 14B models improve code generation accuracy by 5.3% and Best-of-N accuracy by 9.0% after optimization on Qwen2.5-Instruct models, outperforming similarly sized Qwen-Coder, DeepSeek-Coder, and Seed-Coder. They naturally extend to downstream tasks such as test-time scaling and agentic coding-achieving a 8.1% improvement over the base model. For the long-CoT model, our ReasonFlux-Coder-4B consistently outperforms Qwen3-4B while achieving 64.8% inference efficiency in unit test generation. Notably, we also find that our model can serve as an effective reward model for reinforcement learning on base models."

## Key Findings

**(1) What CURE stands for:** The acronym meaning is not explicitly stated in the provided content.

**(2) Co-evolution mechanism:** The framework operates through "reinforcement learning with dedicated reward design" that evolves both components "based on their interaction outcomes" and crucially permits the tester to "learn directly from the coder's mistakes."

**(3) Performance claims:**
- 5.3% code generation accuracy improvement
- 9.0% Best-of-N accuracy gain
- 8.1% downstream task improvement
- 64.8% inference efficiency for unit test generation

**(4) Test assertions as repair specifications:** The document does not address whether assertions function as specifications for code repair.

**(5) Unit test generation innovation:** The framework enables test generation to occur "without any ground-truth code as supervision," representing a key departure from traditional supervised approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02cb0d54-8594-432f-8be4-55413a8cd137",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "866e2c4a-822c-41b6-b219-e15ef3c82bda",
  "sourceToolAssistantUUID": "02cb0d54-8594-432f-8be4-55413a8cd137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-12T00:02:52.191Z_

Good, I have strong results for all four. Let me now fetch the CodeSpecBench HTML page for more details on which model achieved the 20.2% pass rate, and also fetch the test overfitting arXiv paper for more specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "866e2c4a-822c-41b6-b219-e15ef3c82bda",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhEWdTnKbu3K5CuKWTi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4686623-f03b-473e-a3f2-066ea9b23f04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4W2oYDGp6euha8eQRTH7E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3601,
      "cache_read_input_tokens": 14049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3601,
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

_source line 25 · 2026-05-12T00:02:55.291Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KjZKTYjpKZRVcMoqVmxUta`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.12268v1",
  "prompt": "Find: (1) Which specific model achieved the 20.2% pass rate on repository-level tasks? Is it Claude-4.5-Sonnet or another model? (2) What are the function-level pass rates for the best models? (3) List all 15 models evaluated if possible. (4) How do they define \"correctness\" vs \"completeness\" in specification evaluation? (5) Any mention of using specifications for code repair or program repair?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4686623-f03b-473e-a3f2-066ea9b23f04",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhEWdTnKbu3K5CuKWTi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66d721f7-0ef0-4acc-8989-0b4c444794c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4W2oYDGp6euha8eQRTH7E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3601,
      "cache_read_input_tokens": 14049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3601,
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

_source line 26 · 2026-05-12T00:02:57.703Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019hng5VRef8Rdri86magEPc`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.16858v1",
  "prompt": "Extract the full abstract and key findings. What is this paper about exactly? Is it the ICSE 2026 paper on undecidability of test overfitting, or a different paper? What are its main claims about test overfitting in LLM-based automated program repair?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66d721f7-0ef0-4acc-8989-0b4c444794c1",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhEWdTnKbu3K5CuKWTi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "947985e6-7bbf-4a1c-9275-82edad7cb5cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4W2oYDGp6euha8eQRTH7E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3601,
      "cache_read_input_tokens": 14049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3601,
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

_source line 27 · 2026-05-12T00:03:00.653Z_

<details><summary>↩ Tool result · `toolu_01KjZKTYjpKZRVcMoqVmxUta`</summary>

```text
# CodeSpecBench Analysis

## (1) Model with 20.2% Pass Rate
**Claude-4.5-Sonnet** achieved the 20.2% pass rate on CodeSpecBench-Repo, making it the best-performing model for repository-level tasks.

## (2) Function-Level Pass Rates for Top Models
The strongest performers on CodeSpecBench-Func were:
- GPT-5-mini: 47.0%
- Gemini-2.5-Pro: 46.2%
- GPT-OSS-120B: 42.5%

## (3) All 15 Models Evaluated
The paper evaluated these models across both benchmarks:
- **Open-source**: Qwen3 variants (0.6B through 32B), QWQ-32B, GPT-OSS-20B, GPT-OSS-120B, DeepSeek-V3.2
- **Proprietary**: Gemini-2.5-Flash, Gemini-2.5-Pro, GPT-5-mini, GPT-5, Claude-4.5-Sonnet

## (4) Correctness vs. Completeness Definitions
- **Correctness**: "whether a generated specification admits behaviors consistent with intended behavior," evaluated by checking if specifications accept valid test cases
- **Completeness**: "whether a generated specification rejects behaviors inconsistent with intended behavior," assessed by confirming specifications reject invalid test cases

## (5) Specifications for Code Repair
The paper demonstrates that "generated specifications can improve code generation via re-ranking," showing practical utility beyond standalone evaluation, though direct program repair isn't discussed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66d721f7-0ef0-4acc-8989-0b4c444794c1",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "e84ce6be-bdaf-4ff8-a5e0-27425580b3b8",
  "sourceToolAssistantUUID": "66d721f7-0ef0-4acc-8989-0b4c444794c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-12T00:03:00.863Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GSkuGu2PF7ZRdKbfFM5jVd`</summary>

```json
{
  "url": "https://arxiv.org/html/arXiv:2408.02232",
  "prompt": "Find details about: (1) How does SpecRover extract specifications - does it use test assertions or test cases? (2) What does \"specification inference\" involve concretely - extracting from tests, from docstrings, from code? (3) What are the exact SWE-Bench numbers (resolved issues count)? (4) How does the reviewer agent work? (5) Any mention of preconditions, postconditions, or behavioral specifications?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e84ce6be-bdaf-4ff8-a5e0-27425580b3b8",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhEWdTnKbu3K5CuKWTi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d24427d-3977-489f-b2c6-37673b53281b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4W2oYDGp6euha8eQRTH7E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3601,
      "cache_read_input_tokens": 14049,
      "output_tokens": 539,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3601
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 539,
          "cache_read_input_tokens": 14049,
          "cache_creation_input_tokens": 3601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3601,
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

_source line 29 · 2026-05-12T00:03:03.884Z_

<details><summary>↩ Tool result · `toolu_019hng5VRef8Rdri86magEPc`</summary>

```text
# Paper Summary: Test Overfitting in LLM-Based Automated Program Repair

## Full Abstract

"Automated program repair (APR), which tries to automatically fix bugs in code, has long been an active research topic in the software engineering community. Thanks to SWE-bench, a recent benchmark for issue-driven repository-level APR, it is now also a hot research topic in the artificial intelligence (AI) community."

The authors investigate whether test overfitting—where repaired code passes visible tests but fails hidden ones—remains problematic in modern LLM-driven workflows.

## Paper Identity

This is **not** an ICSE 2026 paper on undecidability. Rather, it's a contemporary empirical study examining test overfitting phenomena in LLM-based program repair systems using repository-level benchmarks.

## Main Claims

1. **LLMs do overfit on white-box tests**: 21.8% of Claude-3.7-Sonnet patches and 33% of GPT-4o patches passed visible tests but failed hidden ones.

2. **Test-based refinement worsens overfitting**: When the system iteratively improved code patches using white-box tests, overfitting rates increased (from 21.8% to 25.5% for Claude models).

3. **The problem persists despite model advances**: Unlike earlier findings where "the cure was worse than the disease," modern APR shows mixed results—it generally helps, but test overfitting remains a significant concern warranting careful attention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "947985e6-7bbf-4a1c-9275-82edad7cb5cf",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "b32057f2-fbba-4dc3-b275-d21deb7391ff",
  "sourceToolAssistantUUID": "947985e6-7bbf-4a1c-9275-82edad7cb5cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T00:03:08.031Z_

<details><summary>↩ Tool result · `toolu_01GSkuGu2PF7ZRdKbfFM5jVd`</summary>

```text
# SpecRover: Specification Extraction and Patch Generation

## 1. Specification Extraction Method

SpecRover extracts specifications primarily **from program code and behavior**, not directly from test assertions. The paper states: "whenever a new code snippet is retrieved with an API and sent to the context retrieval agent, we explicitly prompt the agent to analyze the 'intended behavior' of this code snippet."

The system generates function summaries describing "how a function should behave to meet the requirements specified in the high-level problem description." These are natural language specifications derived from analyzing code context during repository exploration.

## 2. Concrete Specification Inference Process

Specification inference involves:

- **Function summaries**: Natural language descriptions of intended function behavior extracted during code context retrieval
- **Reproducer tests**: Automatically generated test cases that reproduce the reported issue
- **Reviewer feedback**: Meta-specifications reconciling patches, tests, and issue descriptions
- **Program structure analysis**: Using AutoCodeRover's structure-aware APIs to understand context

The approach does NOT rely on docstrings or formal preconditions/postconditions as primary sources.

## 3. SWE-Bench Resolution Numbers

- **Full SWE-Bench (2294 issues)**: 443 resolved (19.31%)
- **SWE-Bench Lite (300 issues)**: 93 resolved (31.00%)

This represents "more than 50% improvement" over AutoCodeRover's baseline performance.

## 4. Reviewer Agent Functionality

The reviewer agent operates in two steps:

1. **Execution testing**: Runs original and patched code against the reproducer test, collecting output and exit codes
2. **Decision making**: Analyzes execution information alongside the issue statement to determine patch/test correctness and provide explanations

Notably, it can approve patches while rejecting incorrect tests—addressing the problem that "reproducer tests can be incorrect due to the non-determinism of the LLM."

## 5. Behavioral Specifications

The paper does **not emphasize formal preconditions or postconditions**. Instead, it focuses on natural language specifications capturing intended behavior at function level to guide patch generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d24427d-3977-489f-b2c6-37673b53281b",
  "isSidechain": true,
  "promptId": "99388dc6-fd99-4881-8237-44fdbe0a4015",
  "agentId": "a5aa92c928bbf2f25",
  "type": "user",
  "uuid": "8ac9aedd-9e00-4be3-a751-3f16fdfe277d",
  "sourceToolAssistantUUID": "5d24427d-3977-489f-b2c6-37673b53281b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-12T00:04:08.681Z_

Excellent. I now have comprehensive data on all four papers. Here is the detailed report.

---

## Verification Report: Four Competitor Papers

### 1. SpecRover / AutoCodeRover-v2 (ICSE 2025, arXiv 2408.02232)

**Existence: CONFIRMED.** The paper is published at ICSE 2025 Research Track, available at [arXiv:2408.02232](https://arxiv.org/abs/2408.02232). Authors: Haifeng Ruan and Yuntong Zhang (joint first authors).

**Claimed numbers -- verified:**
- **">50% improvement over AutoCodeRover"** -- Confirmed. On full SWE-Bench (2294 issues), SpecRover resolved 443 issues (19.31%). On SWE-Bench Lite (300 issues), it resolved 93 (31.00%).
- **"$0.65 per issue"** -- Confirmed. This cost figure is for SWE-Bench Lite specifically.

**What "specification inference" actually means in this paper:** SpecRover does NOT extract formal behavioral specifications (preconditions/postconditions) from test assertions. Instead, it performs **natural language intent extraction**: whenever a new code snippet is retrieved, the agent is prompted to analyze the "intended behavior" of that snippet, producing function-level natural language summaries. It also generates "reproducer tests" (test cases that reproduce the reported issue) and uses a reviewer agent to vet patches against these tests. The specifications are informal, natural language descriptions of how functions should behave.

**Relevance to "extracting structured behavioral specifications from test assertions for code repair":** MODERATE. SpecRover demonstrates that specification inference improves APR quality, which validates the general thesis. However, its approach is fundamentally different -- it extracts informal natural language intent from code context and issue descriptions, not structured specifications from test assertions. It does not use preconditions/postconditions. The paper is a **conceptual predecessor** that motivates specification-guided repair but does not compete directly with a test-assertion-to-structured-specification approach.

---

### 2. CodeSpecBench (arXiv 2604.12268, April 2026)

**Existence: CONFIRMED.** Published April 14, 2026 on arXiv. Authors from Hong Kong PolyU, University of Edinburgh, UCL, CUHK, SUTD, and HKUST. Code available at [github.com/SparksofAGI/CodeSpecBench](https://github.com/SparksofAGI/CodeSpecBench).

**Claimed numbers -- verified:**
- **"Best LLM achieves only 20.2% pass rate on repository-level tasks"** -- Confirmed. The best model on CodeSpecBench-Repo is **Claude-4.5-Sonnet** at 20.2%.
- On function-level tasks (CodeSpecBench-Func), results are substantially higher: GPT-5-mini at 47.0%, Gemini-2.5-Pro at 46.2%.
- **15 models evaluated** -- Confirmed. Including open-source (Qwen3 variants, QWQ-32B, GPT-OSS-20B/120B, DeepSeek-V3.2) and proprietary (Gemini-2.5-Flash/Pro, GPT-5-mini, GPT-5, Claude-4.5-Sonnet).

**What "executable behavioral specifications" means:** Preconditions and postconditions encoded as **executable Python functions**. Evaluation uses two dimensions: correctness (does the specification accept valid behaviors?) and completeness (does it reject invalid behaviors?).

**Key finding:** "Specification generation is substantially more challenging than code generation" -- strong coding performance does not imply deep understanding of intended program semantics. The paper also demonstrates that generated specifications can improve code generation via re-ranking.

**Relevance to "extracting structured behavioral specifications from test assertions for code repair":** HIGH -- this is the most directly relevant competitor. CodeSpecBench defines exactly the kind of structured behavioral specifications (executable pre/postconditions) that an assertion-based approach would target. However, CodeSpecBench is a **benchmark**, not a repair system. It evaluates LLMs' ability to generate specifications, not to use them for repair. The 20.2% repo-level pass rate is powerful evidence that LLM-only specification generation is insufficient, which could actually **motivate** a test-assertion extraction approach as a complementary or superior alternative. The paper shows that generated specs can improve code generation via re-ranking, validating the downstream utility of specifications.

---

### 3. Test Overfitting / Undecidability in APR (ICSE 2026)

**Existence: CONFIRMED -- TWO separate papers found:**

**(a) "The Undecidability of Overfitting in Automated Program Repair"** -- ICSE 2026 NIER Track. Author: Omar I. Al-Bataineh (Gran Sasso Science Institute). Presented April 16, 2026. This is a **theoretical/position paper** arguing that test overfitting is a fundamental, unavoidable consequence of undecidability when complete specifications are unavailable. Test suites function only as partial correctness oracles, making overfitting "a structural outcome rather than an incidental defect." The paper advocates reframing overfitting as an inherent boundary rather than a solvable bug.

**(b) "Is the Cure Still Worse Than the Disease? Test Overfitting by LLMs in Automated Program Repair"** (arXiv 2511.16858) -- An empirical study finding that 21.8% of Claude-3.7-Sonnet patches and 33% of GPT-4o patches overfit on visible tests. Test-based refinement worsens overfitting rates (from 21.8% to 25.5% for Claude models).

**Relevance:** VERY HIGH for both. The undecidability paper (a) provides the theoretical foundation for why test-assertion-based specifications matter -- if tests alone are inherently insufficient as specifications, then extracting richer structured specifications from assertions could mitigate the fundamental limitation. The empirical paper (b) quantifies the overfitting problem, showing it is severe even with frontier LLMs. Both papers **strengthen the motivation** for a structured behavioral specification approach rather than competing with it.

---

### 4. CURE: Co-Evolving LLM Coder and Unit Tester (NeurIPS 2025)

**Existence: CONFIRMED.** NeurIPS 2025 **Spotlight** paper (arXiv 2506.03136). Available on [OpenReview](https://openreview.net/forum?id=wPdBe9zxNr) and [GitHub](https://github.com/Gen-Verse/CURE).

**Claimed numbers -- verified:**
- 5.3% code generation accuracy improvement
- 9.0% Best-of-N accuracy gain
- 8.1% improvement in downstream tasks (test-time scaling, agentic coding)
- Derived models: ReasonFlux-Coder-7B and 14B outperform similarly sized Qwen-Coder, DeepSeek-Coder, and Seed-Coder

**What CURE does:** It is a reinforcement learning framework where the coder and unit tester co-evolve. The unit tester learns from the coder's mistakes during RL rollouts, requiring no ground-truth code as supervision. The key insight is that better test generation enables better self-checking and self-correction during inference.

**Relevance to "extracting structured behavioral specifications from test assertions for code repair":** LOW-MODERATE. CURE focuses on **generating** better tests via RL co-evolution, not on extracting specifications from existing test assertions. It treats tests as pass/fail signals for RL reward, not as sources of structured behavioral specifications. The philosophical alignment is that tests and code benefit from mutual improvement, but the mechanism is completely different from specification extraction.

---

## Summary Assessment

| Paper | Verified? | Numbers Accurate? | Direct Relevance |
|---|---|---|---|
| SpecRover (ICSE 2025) | Yes | Yes, all claims confirmed | Moderate -- validates spec-guided repair but uses informal NL specs |
| CodeSpecBench (Apr 2026) | Yes | Yes, Claude-4.5-Sonnet at 20.2% confirmed | **High** -- defines the exact specification format; benchmark gap motivates your approach |
| Undecidability/Overfitting (ICSE 2026) | Yes | N/A (theoretical) | **Very High** -- provides theoretical justification for richer specifications |
| CURE (NeurIPS 2025 Spotlight) | Yes | Yes, all claims confirmed | Low-Moderate -- different mechanism (RL co-evolution vs. spec extraction) |

**Bottom line:** All four papers exist and their claimed numbers are accurate. The most relevant competitor is **CodeSpecBench**, but it is a benchmark, not a repair system -- and its finding that LLMs struggle with specification generation (20.2% repo-level) actually *supports* the case for extracting specifications from test assertions rather than generating them from scratch. **SpecRover** validates the concept of specification-guided repair but uses a different (informal) specification approach. The **undecidability paper** provides strong theoretical motivation. **CURE** is tangentially related at best.

Sources:
- [SpecRover arXiv page](https://arxiv.org/abs/2408.02232)
- [SpecRover ICSE 2025 listing](https://conf.researchr.org/details/icse-2025/icse-2025-research-track/68/SpecRover-Code-Intent-Extraction-via-LLMs)
- [CodeSpecBench arXiv page](https://arxiv.org/abs/2604.12268)
- [CodeSpecBench HTML](https://arxiv.org/html/2604.12268v1)
- [Undecidability of Overfitting ICSE 2026](https://conf.researchr.org/details/icse-2026/icse-2026-nier/4/The-Undecidability-of-Overfitting-in-Automated-Program-Repair)
- [Test Overfitting LLM APR arXiv](https://arxiv.org/html/2511.16858v1)
- [CURE arXiv page](https://arxiv.org/abs/2506.03136)
- [CURE NeurIPS 2025 poster](https://neurips.cc/virtual/2025/poster/115329)
- [CURE OpenReview](https://openreview.net/forum?id=wPdBe9zxNr)
- [CURE GitHub](https://github.com/Gen-Verse/CURE)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ac9aedd-9e00-4be3-a751-3f16fdfe277d",
  "isSidechain": true,
  "agentId": "a5aa92c928bbf2f25",
  "requestId": "req_011CawhFy5TZzUZ9LAkNrZS8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1c300f7-5016-48b0-95aa-826193709bf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f618e433-b20e-425e-ac02-458ec8b668db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HX4LfKpPwBwqgQ1haEjzKT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1833,
      "cache_read_input_tokens": 17650,
      "output_tokens": 2588,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2588,
          "cache_read_input_tokens": 17650,
          "cache_creation_input_tokens": 1833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1833,
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
