# Research conversation: I need to verify a critical competing paper that was found during my review and check its relevance to a proposal about 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ada046e084cc3fb73.jsonl`
- **Structured JSON:** [`4cfe3e4471e24c4705d0.json`](../../sessions/4c/4cfe3e4471e24c4705d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-10T18:31:50.580Z_

I need to verify a critical competing paper that was found during my review and check its relevance to a proposal about "head-selective decomposed importance scoring for self-speculative decoding."

1. **LycheeDecode (Feb 2026, ICLR 2026, arXiv:2602.04541)**: "Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding"
   - Search for this paper and read its abstract via WebFetch
   - Does it classify heads into types (retrieval vs sparse)?
   - Does it apply different attention strategies per head type?
   - How close is this to "head-selective decomposed importance scoring"?

2. **Also search for**: "Decoupling Positional and Symbolic Attention Behavior in Transformers" (Urrutia et al., Oct 2025, arXiv:2511.11579)
   - Does this paper prove positional and content attention are mutually exclusive?
   - How close is this to the structural/content decomposition in the proposal?

3. **Search for any very recent (March-May 2026) papers on**:
   - "head-selective speculative decoding 2026"
   - "attention decomposition efficient inference 2026"
   - "per-head scoring self-speculation"

Use WebFetch to read abstracts of the most relevant papers. Report exactly what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "17a9e730-e871-437c-8db5-6ad0212ec45e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:31:50.583Z_

```json
{
  "parentUuid": "17a9e730-e871-437c-8db5-6ad0212ec45e",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
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
  "uuid": "b17362b4-6595-4741-96db-deedc0e83f08",
  "timestamp": "2026-05-10T18:31:50.583Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:31:52.989Z_



I'll start by loading the WebFetch and WebSearch tool schemas, then search for all the papers mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b17362b4-6595-4741-96db-deedc0e83f08",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNBoLVjbwxfFBbXQ8f5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69e3d3d6-fc7e-47cb-a595-6a8e21dfbf70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BUcSJDWjPjfYFdAUyaZEv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 873,
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

_source line 4 · 2026-05-10T18:31:53.347Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EX2XqsR9fZ11LKXTQMTnFV`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69e3d3d6-fc7e-47cb-a595-6a8e21dfbf70",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNBoLVjbwxfFBbXQ8f5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd42aea2-32fe-429f-a989-3dd6b703d46c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BUcSJDWjPjfYFdAUyaZEv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 8223,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 873,
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

_source line 5 · 2026-05-10T18:31:53.350Z_

<details><summary>↩ Tool result · `toolu_01EX2XqsR9fZ11LKXTQMTnFV`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "bd42aea2-32fe-429f-a989-3dd6b703d46c",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "bf208165-129e-4024-824c-aecdd6a52906",
  "sourceToolAssistantUUID": "bd42aea2-32fe-429f-a989-3dd6b703d46c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:31:55.699Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf208165-129e-4024-824c-aecdd6a52906",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNC1NYRWxL8dZMyBi71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d29b48e4-6d32-4ce2-b497-cba520773f85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gd2ABGbnyca42929ShMBD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 7 · 2026-05-10T18:31:58.064Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AEQFWLrKkQ1xuX8HTT2GK7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.04541",
  "prompt": "Extract the full title, authors, abstract, and any key details about the paper. Does it classify attention heads into types (e.g., retrieval vs sparse)? Does it apply different attention strategies per head type? What is the core methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d29b48e4-6d32-4ce2-b497-cba520773f85",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNC1NYRWxL8dZMyBi71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c99f01d-c79b-4785-b4b9-4742bc0b8495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gd2ABGbnyca42929ShMBD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 8 · 2026-05-10T18:31:59.949Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V95DLW7N7LRvDwvHKzfPAp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.11579",
  "prompt": "Extract the full title, authors, abstract, and key findings. Does this paper prove that positional and content attention are mutually exclusive? Does it decompose attention into structural/positional vs content components? What is the core methodology and conclusion?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c99f01d-c79b-4785-b4b9-4742bc0b8495",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNC1NYRWxL8dZMyBi71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e83c9d1-0e58-44e4-a503-3c5284afbaee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gd2ABGbnyca42929ShMBD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 9 · 2026-05-10T18:32:00.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TB19ALxXkfNNTQ1bsyZiC1`</summary>

```json
{
  "query": "head-selective speculative decoding 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e83c9d1-0e58-44e4-a503-3c5284afbaee",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNC1NYRWxL8dZMyBi71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d7a4bb7-e59c-4381-981b-1345e532b738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gd2ABGbnyca42929ShMBD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 10 · 2026-05-10T18:32:00.884Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XjAz6sWQJsdGMiVmzh9ajt`</summary>

```json
{
  "query": "attention decomposition efficient inference 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d7a4bb7-e59c-4381-981b-1345e532b738",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNC1NYRWxL8dZMyBi71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68e8d44e-2e1c-49fc-b4aa-1e3ddd82f16a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gd2ABGbnyca42929ShMBD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 11 · 2026-05-10T18:32:01.375Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VMvxBakzUCvvFgPvGNtAp7`</summary>

```json
{
  "query": "per-head scoring self-speculation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68e8d44e-2e1c-49fc-b4aa-1e3ddd82f16a",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNC1NYRWxL8dZMyBi71",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "638664fe-1eb4-4e81-bb3e-b4f56e768e8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gd2ABGbnyca42929ShMBD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9096,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 390,
          "cache_read_input_tokens": 9096,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
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

_source line 12 · 2026-05-10T18:32:04.601Z_

<details><summary>↩ Tool result · `toolu_01AEQFWLrKkQ1xuX8HTT2GK7`</summary>

```text
# LycheeDecode Paper Summary

**Full Title:** LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding

**Authors:** Gang Lin, Dongfang Li, Zhuoen Chen, Yukun Shi, Xuhui Chen, Baotian Hu, Min Zhang

**Submission:** February 4, 2026 (ICLR 2026)

## Key Details

**Yes, the paper classifies attention heads into types.** The approach partitions heads into two categories: "a small subset of retrieval heads that dynamically identify crucial tokens and a majority of sparse heads that reuse them for efficient computation."

**Differentiated Strategies:** Different attention mechanisms are applied per head type—retrieval heads perform dynamic token selection while sparse heads leverage those selections for computational efficiency.

**Core Methodology:**

The method centers on a "fine-grained hybrid-head attention mechanism that employs a hardware-efficient top-k selection strategy." The innovation uses a HardKuma-based mechanism to manage this head partitioning, addressing limitations of previous approaches that use coarse-grained sharing across all layers.

**Performance Results:**

Testing on models like Llama3 and Qwen3 across benchmarks (LongBench, RULER, AIME24, OlympiadBench) demonstrates "generative quality comparable to, and at times surpassing even the full-attention baseline" while achieving up to 2.7x speedup at 128K context length.

**Primary Problem Solved:** The expanding key-value cache during long-context decoding, which creates memory and latency bottlenecks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c99f01d-c79b-4785-b4b9-4742bc0b8495",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "14a0f417-87d6-4830-92ec-ba54d5115d17",
  "sourceToolAssistantUUID": "3c99f01d-c79b-4785-b4b9-4742bc0b8495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T18:32:05.049Z_

<details><summary>↩ Tool result · `toolu_01V95DLW7N7LRvDwvHKzfPAp`</summary>

```text
# Paper Analysis: Decoupling Positional and Symbolic Attention Behavior in Transformers

## Full Title
"Decoupling Positional and Symbolic Attention Behavior in Transformers"

## Authors
Felipe Urrutia, Jorge Salas, Alexander Kozachinskiy, Cristian Buc Calderon, Hector Pasten, Cristobal Rojas

## Abstract Summary
The paper investigates how Transformer models encode positional versus semantic information separately. It focuses on Rotary Positional Encodings (RoPE), proposing that large frequencies encode position while small frequencies encode meaning. The researchers develop theoretical definitions and metrics to measure when attention heads behave positionally versus symbolically.

## Core Methodology
1. **Theoretical Framework**: Provide formal definitions distinguishing positional from symbolic head behavior
2. **Proof of Mutual Exclusivity**: Demonstrate these represent "two mutually exclusive behaviors"
3. **Quantitative Metrics**: Create measurement tools to assess behavior types
4. **Empirical Validation**: Analyze LLMs using RoPE to verify theoretical predictions
5. **Causal Testing**: Design canonical tasks (purely positional or symbolic) and manipulate frequency access to demonstrate causal relationships

## Key Findings
- Strong correspondence exists between attention head behavior and frequency utilization patterns
- Model performance directly correlates with heads accessing appropriate frequencies for their task type
- Controlling frequency access causally influences model performance on targeted tasks

## Mutual Exclusivity Question
Yes, the paper explicitly proves positional and symbolic behaviors are mutually exclusive categories, establishing this as a fundamental theoretical principle of their framework.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e83c9d1-0e58-44e4-a503-3c5284afbaee",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "b1b12b9e-fd1e-41e9-a262-e501dd980da8",
  "sourceToolAssistantUUID": "5e83c9d1-0e58-44e4-a503-3c5284afbaee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:32:06.935Z_

<details><summary>↩ Tool result · `toolu_01VMvxBakzUCvvFgPvGNtAp7`</summary>

```text
Web search results for query: "per-head scoring self-speculation 2026"

Links: [{"title":"Fantasy baseball: 2026 Head-to-head points mock draft - ESPN","url":"https://www.espn.com/fantasy/baseball/story/_/id/47887958/fantasy-baseball-head-head-points-mock-draft-mlb-2026"},{"title":"Predictions Scorecard, 2026 January 01 – Rodney Brooks","url":"https://rodneybrooks.com/predictions-scorecard-2026-january-01/"},{"title":"2026 Fantasy Baseball Mock Draft: Head-to-Head (H2H) points is a small format where it pays to think big","url":"https://www.cbssports.com/fantasy/baseball/news/2026-fantasy-baseball-mock-draft-head-to-head-h2h-points/"},{"title":"2026 Fantasy Baseball Mock Draft: Head-to-Head (H2H) points league contextualizes spring risers and fallers","url":"https://www.cbssports.com/fantasy/baseball/news/2026-fantasy-baseball-mock-draft-head-to-head/"},{"title":"2026 Season-Long Fantasy Hockey Projections - 5V5 Hockey","url":"https://5v5hockey.com/season-long/fantasy-hockey-projections/"},{"title":"Updated Fantasy Baseball Draft Rankings: H2H Points (2026)","url":"https://www.rotoballer.com/updated-fantasy-baseball-draft-rankings-h2h-points-2026/1833627"},{"title":"Speculation: - Official 2025-2026 Post Season Thread | HFBoards - NHL Message Board and Forum for National Hockey League","url":"https://forums.hfboards.com/threads/official-2025-2026-post-season-thread.3029530/"},{"title":"Fantasy baseball: The final mock draft before the 2026 season - ESPN","url":"https://www.espn.com/fantasy/baseball/story/_/id/48221499/fantasy-baseball-espn-final-head-head-points-mock-draft-mlb-2026"},{"title":"PBR | PBR enhances scoring system for 2026 season, marking riders and bulls in tenth-point increments","url":"https://www.pbr.com/news/2025/11/pbr-enhances-scoring-system-for-2026-season-marking-riders-and-bulls-in-tenth-point-increments/"},{"title":"What is your preliminary top 10 for the 2026 season? - Bijan, Puka and JSN look like favorites - Fantasy Index","url":"https://fantasyindex.com/2026/02/12/ask-the-experts/what-is-your-preliminary-top-10-for-the-2026-season"}]

Based on the search results, I found information related to your query about "per-head scoring" in 2026, though the results primarily focus on fantasy sports scoring systems rather than a specific "self-speculation" metric. Here's what I found:

The search results contain extensive information about **head-to-head (H2H) points scoring formats** for fantasy baseball in 2026:

In fantasy baseball head-to-head points leagues, hitters score one point for every base reached via hits (total bases), as well as each walk, run, RBI and stolen base, and lose one point when they strike out. Saves are worth five points each for relievers, while pitchers lose two points per run allowed, one point per baserunner (hit or walk) and two points for a loss.

However, I did not find specific results about a metric called "per-head scoring self-speculation" in 2026. The search results mostly cover fantasy sports draft information and strategies for the 2026 season.

If you're looking for information about a different meaning of this term (such as a technical computing term, AI/machine learning concept, or something else), could you provide more context? That would help me conduct a more targeted search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "638664fe-1eb4-4e81-bb3e-b4f56e768e8f",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "9495210d-ed72-4f22-bae1-442a81190a1c",
  "sourceToolAssistantUUID": "638664fe-1eb4-4e81-bb3e-b4f56e768e8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T18:32:06.990Z_

<details><summary>↩ Tool result · `toolu_01TB19ALxXkfNNTQ1bsyZiC1`</summary>

```text
Web search results for query: "head-selective speculative decoding 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf?id=aL1Wnml9Ef"},{"title":"Speculative Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=aL1Wnml9Ef"},{"title":"Speculative Decoding and Beyond: A Survey of Speculative Decoding Techniques","url":"https://blog.codingconfessions.com/p/a-selective-survey-of-speculative-decoding"},{"title":"[2603.03251] Speculative Speculative Decoding","url":"https://arxiv.org/abs/2603.03251"},{"title":"Efficient LLM System with Speculative Decoding | EECS at UC Berkeley","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-224.html"},{"title":"SPECULATIVE SPECULATIVE DECODING","url":"https://openreview.net/pdf/20f1f3685b9fff60c510b3f327fbbde9d5584379.pdf"},{"title":"Speculative Speculative Decoding","url":"https://arxiv.org/html/2603.03251"},{"title":"MIRROR SPECULATIVE DECODING: BREAKING THE SERIAL BARRIER IN LLM INFERENCE","url":"https://arxiv.org/pdf/2510.13161"},{"title":"Performance improvements with speculative decoding in vLLM for gpt-oss | Red Hat Developer","url":"https://developers.redhat.com/articles/2026/04/16/performance-improvements-speculative-decoding-vllm-gpt-oss"},{"title":"A Hitchhiker’s Guide to Speculative Decoding – PyTorch","url":"https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/"}]

Based on the search results, I found relevant information about speculative decoding research in 2026. However, I didn't find specific results specifically about "head-selective speculative decoding." Let me share what I found about recent speculative decoding developments:

## Speculative Speculative Decoding (SSD)

Speculative speculative decoding (SSD) is a technique that paralelizes speculation and verification operations, where while a verification is ongoing, the draft model predicts likely verification outcomes and prepares speculations pre-emptively for them. If the actual verification outcome is in the predicted set, a speculation can be returned immediately, eliminating drafting overhead entirely.

The resulting algorithm is called Saguaro, an optimized SSD algorithm that is on average 30% faster than optimized speculative decoding baselines and up to 5x faster than autoregressive decoding with open source inference engines.

## Related Techniques

The search results also reference Medusa, an architecture where multiple prediction heads are attached to the last hidden layer of the base LLM, where the head at the ith position predicts the next ith token, and each head produces multiple predictions from which the top-k are selected, resulting in a tree of possible continuations.

The specific term "head-selective speculative decoding" doesn't appear in these results. If you're looking for more specific information about head-selective approaches or other related techniques from 2026, I'd recommend checking the full papers on arXiv or OpenReview directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d7a4bb7-e59c-4381-981b-1345e532b738",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "17c8d8ac-5eb2-4bfe-9faf-66c5926f42af",
  "sourceToolAssistantUUID": "8d7a4bb7-e59c-4381-981b-1345e532b738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:32:09.472Z_

<details><summary>↩ Tool result · `toolu_01XjAz6sWQJsdGMiVmzh9ajt`</summary>

```text
Web search results for query: "attention decomposition efficient inference 2026"

Links: [{"title":"Optimizing Attention for Efficient LLM Inference: A Review | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/abstract/document/11027973/"},{"title":"[2603.23914v1] Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding","url":"https://arxiv.org/abs/2603.23914v1"},{"title":"Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/html/2507.19595v3"},{"title":"Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding","url":"https://arxiv.org/html/2603.23914v1"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"[2507.19595] Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/abs/2507.19595"},{"title":"LREA: Low-Rank Efficient Attention on Modeling Long-Term User Behaviors for CTR Prediction","url":"https://arxiv.org/html/2503.02542"},{"title":"Transformer Inference Optimization Techniques: Enhancing Efficiency in Large Language Models · Technical news about AI, coding and all","url":"https://dasroot.net/posts/2026/03/transformer-inference-optimization-techniques/"},{"title":"1 A Survey on Efficient Inference for Large Language Models","url":"https://arxiv.org/pdf/2404.14294"},{"title":"GitHub - dongwonjo/Token-Sparse-Attention: [ICML 2026] Official Implementation of \"Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection\" · GitHub","url":"https://github.com/dongwonjo/Token-Sparse-Attention"}]

Based on the search results, here's an overview of recent developments in attention decomposition and efficient inference for 2026:

## Key Research Areas

**Low-Rank Decomposition Approaches**

Optimization strategies for attention mechanisms include sparse attention, low-rank decomposition, quantization techniques, block-based parallel computation, and memory management. AttentionPack introduces a multi-head compression technique leveraging singular value decomposition to reduce the size of stored key and value vectors, and an attention-aware partial decompression technique minimizing latency overhead. This approach can reduce the key-value cache size by up to 8 times and improve batch inference throughput by up to 50%.

**Efficient Attention Mechanisms**

Linear attention methods achieve linear complexity through kernel approximations, recurrent formulations, or fast-weight dynamics. Sparse attention techniques limit attention computation to selected subsets of tokens based on fixed patterns, block-wise routing, or clustering strategies.

Token Sparse Attention is a lightweight token-level sparsification mechanism for efficient long-context inference, achieving up to 3.23× attention speedup at 128K context with less than 1% accuracy degradation.

**Comparative Compression Strategies**

Token eviction is training-free and hardware-compatible but discards tokens permanently. Quantization reduces memory without removing tokens—KIVI achieves 2.6× combined peak memory reduction at 2-bit precision; TurboQuant achieves 6× memory reduction at 3-bit precision. Low-rank methods target hidden dimension redundancy and remain underexplored relative to token eviction.

These advances represent a shift toward more efficient inference architectures for large language models in production environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68e8d44e-2e1c-49fc-b4aa-1e3ddd82f16a",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "c6c155d9-6fc9-42f8-9d70-7f07151dcbbe",
  "sourceToolAssistantUUID": "68e8d44e-2e1c-49fc-b4aa-1e3ddd82f16a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T18:32:14.583Z_

Good, I have the two main papers. Now let me fetch more details on the most relevant recent papers from the search results and do a few more targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6c155d9-6fc9-42f8-9d70-7f07151dcbbe",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNDC7ETUs5wE86aZvR7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6af113d0-4a55-47cb-bba7-dec27ceea146",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Abu5YSd8vSjpQ9r4AQ1sR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 999,
      "cache_creation_input_tokens": 3067,
      "cache_read_input_tokens": 11009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3067,
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

_source line 18 · 2026-05-10T18:32:16.478Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E1iB8d5gDfo8qaWLeof4tJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.03251",
  "prompt": "Extract the full title, authors, abstract. Does this paper involve per-head analysis, head-selective mechanisms, or attention decomposition for speculative decoding? What is the core idea?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6af113d0-4a55-47cb-bba7-dec27ceea146",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNDC7ETUs5wE86aZvR7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19ebb314-6803-4819-9ab6-77c74a8c2faf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Abu5YSd8vSjpQ9r4AQ1sR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 999,
      "cache_creation_input_tokens": 3067,
      "cache_read_input_tokens": 11009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3067,
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

_source line 19 · 2026-05-10T18:32:17.891Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DecqVoDj6qPbcYK9AwJi2A`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.23914v1",
  "prompt": "Extract the full title, authors, abstract. Does this paper involve per-head scoring, head-selective mechanisms, attention decomposition, or importance scoring for efficient inference? What is the core methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19ebb314-6803-4819-9ab6-77c74a8c2faf",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNDC7ETUs5wE86aZvR7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a91e4f7f-a4c7-41dd-8832-5d29c1f70ccd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Abu5YSd8vSjpQ9r4AQ1sR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 999,
      "cache_creation_input_tokens": 3067,
      "cache_read_input_tokens": 11009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3067,
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

_source line 20 · 2026-05-10T18:32:18.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017dRadioBbvi4W7AnqHWSyW`</summary>

```json
{
  "query": "\"self-speculative decoding\" head importance scoring attention 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a91e4f7f-a4c7-41dd-8832-5d29c1f70ccd",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNDC7ETUs5wE86aZvR7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46810652-3840-4d33-95ae-9518a863277b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Abu5YSd8vSjpQ9r4AQ1sR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 999,
      "cache_creation_input_tokens": 3067,
      "cache_read_input_tokens": 11009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3067,
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

_source line 21 · 2026-05-10T18:32:19.108Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018cVmXAcqauxMawbgNmxzdW`</summary>

```json
{
  "query": "LycheeDecode hybrid head sparse decoding retrieval heads speculative"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46810652-3840-4d33-95ae-9518a863277b",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNDC7ETUs5wE86aZvR7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04bae735-ff5b-4989-9b95-79191f9fdd78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Abu5YSd8vSjpQ9r4AQ1sR2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 999,
      "cache_creation_input_tokens": 3067,
      "cache_read_input_tokens": 11009,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3067
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 999,
          "output_tokens": 360,
          "cache_read_input_tokens": 11009,
          "cache_creation_input_tokens": 3067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3067,
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

_source line 22 · 2026-05-10T18:32:21.138Z_

<details><summary>↩ Tool result · `toolu_01E1iB8d5gDfo8qaWLeof4tJ`</summary>

```text
# Paper Summary

**Full Title:** Speculative Speculative Decoding

**Authors:** Tanishq Kumar, Tri Dao, Avner May

**Abstract:** The paper addresses autoregressive decoding bottlenecks by introducing speculative speculative decoding (SSD). Rather than sequential speculation-then-verification, it "parallelize[s] these operations" by having the draft model "predict[] likely verification outcomes and prepare[] speculations pre-emptively." Their implementation (Saguaro) achieves 30% faster performance than speculative decoding baselines.

---

## Attention/Head Analysis?

**No.** This paper does not involve per-head analysis, head-selective mechanisms, or attention decomposition. It focuses on algorithmic acceleration through concurrent prediction and verification rather than analyzing internal model structures.

## Core Idea

The fundamental contribution is eliminating sequential dependency in speculative decoding. While verification occurs, the draft model speculatively predicts multiple possible verification outcomes in advance. When actual verification results match the predicted set, a token can be returned immediately without additional drafting, thus reducing latency overhead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19ebb314-6803-4819-9ab6-77c74a8c2faf",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "7cb51c2d-8e12-4971-91b3-5efa3838d9b1",
  "sourceToolAssistantUUID": "19ebb314-6803-4819-9ab6-77c74a8c2faf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T18:32:23.786Z_

<details><summary>↩ Tool result · `toolu_01DecqVoDj6qPbcYK9AwJi2A`</summary>

```text
# Paper Analysis: AttentionPack

## Full Title
"Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding"

## Authors
Fatih Ilhan, Gaowen Liu, Ramana Rao Kompella, Selim Furkan Tekin, Tiansheng Huang, Zachary Yahn, Yichang Xu, Ling Liu

## Abstract
The paper addresses memory overhead during decoding in large VLMs by introducing "an adaptive and attention-aware optimization framework." It focuses on handling lengthy sequences of visual and text tokens, particularly in multi-image or video contexts.

## Methodology & Key Techniques

**Yes**, this paper incorporates attention-based scoring mechanisms:

1. **Multi-head Attention Compaction**: The framework "introduces a multi-head attention compaction method for economically storing key and value matrices by exploiting the implicit low-rank structure." This represents per-head optimization targeting the KV cache.

2. **Token-Specific Attention-Aware Decompression**: Implements "a token-specific attention-aware decompression mechanism to reduce latency overhead," indicating selective token processing based on attention patterns.

**Core Results**: Achieves up to 8x memory efficiency improvements while maintaining model output quality, enabling larger batch sizes and longer context support.

The methodology centers on intelligent compression and selective decompression of attention components rather than wholesale pruning, making it an attention-decomposition approach for efficient inference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a91e4f7f-a4c7-41dd-8832-5d29c1f70ccd",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "743d0354-97a7-4a2a-8772-df5cdf6fa682",
  "sourceToolAssistantUUID": "a91e4f7f-a4c7-41dd-8832-5d29c1f70ccd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T18:32:26.315Z_

<details><summary>↩ Tool result · `toolu_018cVmXAcqauxMawbgNmxzdW`</summary>

```text
Web search results for query: "LycheeDecode hybrid head sparse decoding retrieval heads speculative"

Links: [{"title":"Lychee LycheeDecode: Accelerating Long-Context LLM Inference via","url":"https://www.arxiv.org/pdf/2602.04541"},{"title":"LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding","url":"https://arxiv.org/html/2602.04541"},{"title":"[2602.04541] LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding","url":"https://arxiv.org/abs/2602.04541"},{"title":"LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding | OpenReview","url":"https://openreview.net/forum?id=YWCHLdNGVU"},{"title":"LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding","url":"https://lg9077.github.io/lycheedecode/"},{"title":"LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding | Request PDF","url":"https://www.researchgate.net/publication/400460197_LycheeDecode_Accelerating_Long-Context_LLM_Inference_via_Hybrid-Head_Sparse_Decoding"},{"title":"Baotian Hu","url":"https://www.catalyzex.com/author/Baotian%20Hu"},{"title":"Accelerate Speculative Decoding with Sparse Computation in Verification","url":"https://arxiv.org/html/2512.21911"},{"title":"H2EAL: Hybrid-Bonding Architecture with Hybrid Sparse Attention for Efficient Long-Context LLM Inference","url":"https://arxiv.org/html/2508.16653"},{"title":"HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness","url":"https://arxiv.org/html/2603.17573"}]

Based on the search results, here's what I found about LycheeDecode and its hybrid-head sparse decoding approach:

## Overview

LycheeDecode is an efficient decoding method centered on a fine-grained hybrid-head attention mechanism that employs a hardware-efficient top-k selection strategy.

## Architecture

The HardKuma-based mechanism partitions attention heads into a small subset of retrieval heads that dynamically identify crucial tokens and a majority of sparse heads that reuse them for efficient computation. More specifically:

- **Retrieval Heads**: These are responsible for performing full attention computation over the entire context to accurately identify the most important tokens.

- **Sparse Heads**: These perform a more efficient computation, calculating attention only on the sparse subset of tokens provided by the preceding layer.

## Key Innovation

LycheeDecode introduces the Hard Kumaraswamy distribution to address the discrete optimization problem in end-to-end head type identification, reducing the train-inference gap and improving model robustness and performance.

## Performance

LycheeDecode achieves up to 2.7x speedup on 128k context with Hybrid-Head Sparse Decoding. Through extensive experiments on leading models like Llama3 and Qwen3 across diverse benchmarks for long-context understanding and complex reasoning, LycheeDecode demonstrates generative quality comparable to, and at times surpassing even the full-attention baseline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04bae735-ff5b-4989-9b95-79191f9fdd78",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "5807adf8-7413-4f2f-8499-dac5c4fce3a4",
  "sourceToolAssistantUUID": "04bae735-ff5b-4989-9b95-79191f9fdd78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T18:32:30.648Z_

<details><summary>↩ Tool result · `toolu_017dRadioBbvi4W7AnqHWSyW`</summary>

```text
Web search results for query: ""self-speculative decoding" head importance scoring attention 2026"

Links: [{"title":"Speculative Decoding: Types and Optimizations","url":"https://www.aussieai.com/research/speculative-decoding"},{"title":"Self Speculative Decoding for Diffusion Large Language Model | OpenReview","url":"https://openreview.net/forum?id=rKJ7A30lQQ"},{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641"},{"title":"Speculative Decoding and Beyond: An In-Depth Survey of Techniques","url":"https://arxiv.org/html/2502.19732v4"},{"title":"Speculative Verification: Exploiting Information Gain to Refine Speculative Decoding","url":"https://arxiv.org/html/2509.24328v1"},{"title":"Q K V softmax αij Attention Mechanisms in Neural Networks","url":"https://arxiv.org/pdf/2601.03329"},{"title":"Cross-Attention Speculative Decoding Wei Zhong wei.zhong@lge.com","url":"https://www.arxiv.org/pdf/2505.24544"},{"title":"(PDF) SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://www.researchgate.net/publication/400603323_SpecAttn_Co-Designing_Sparse_Attention_with_Self-Speculative_Decoding"},{"title":"Cross-Attention Speculative Decoding","url":"https://arxiv.org/html/2505.24544v3"},{"title":"Kangaroo: Lossless Self-Speculative Decoding for Accelerating LLMs via Double Early Exiting | OpenReview","url":"https://openreview.net/forum?id=lT3oc04mDp"}]

Based on the search results, I found several relevant papers and resources about self-speculative decoding and attention mechanisms from 2025-2026:

## Self-Speculative Decoding Overview

Self-speculative decoding is the idea that the smaller draft model, instead of being a separately trained model from the larger verifier model, could simply be a cut-down version of the bigger model. Self-speculative decoding is based on early-exited versions of the larger model, used as the smaller draft model. Then the larger model simply computes the remaining layers that haven't yet been executed, but it does so in parallel.

## Recent Research (2025-2026)

Several recent papers address self-speculative decoding with attention mechanisms:

1. **SpecAttn**: SpecAttn is a novel training-free approach that seamlessly integrates with existing speculative decoding techniques to enable efficient sparse attention in pre-trained transformers. The key insight is to exploit the attention weights already computed by the draft model during speculative decoding to identify important tokens for the target model, eliminating redundant computation while maintaining output quality.

2. **Head Importance and Attention Analysis**: Attention heads across layers serve different roles that vary with context. Some compute attention scores globally over many tokens, while others focus locally on a subset. However, mapping attention heads between the draft and target models does not provide useful signals for speculation accuracy – even heads that strongly correlate with those in the target model show no noticeable differences in attention patterns between accepted and rejected tokens.

3. **Self-Speculative Decoding Variants**: Kangaroo proposes a novel self-speculative decoding framework with double early exiting strategy, which leverages the shallow sub-network and the LM Head of the well-trained target LLM to construct a self-drafting model. The self-verification stage only requires computing the remaining layers over the early-exited hidden states in parallel. To bridge the representation gap between the sub-network and the full model, a lightweight and efficient adapter module is trained on top of the sub-network.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46810652-3840-4d33-95ae-9518a863277b",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "1174bc11-96d4-45f3-9fa6-5ef44e600247",
  "sourceToolAssistantUUID": "46810652-3840-4d33-95ae-9518a863277b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T18:32:36.383Z_

Excellent. Let me now fetch the SpecAttn paper and do one more targeted search for very recent work combining head-level analysis with self-speculative decoding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1174bc11-96d4-45f3-9fa6-5ef44e600247",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNEkgq42x8oRFCA9hMx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d78bb5a-a68c-43ba-a4df-40dae9a65a27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzKczq7EWXzStwymiEiMGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 913,
      "cache_creation_input_tokens": 3077,
      "cache_read_input_tokens": 14076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3077,
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

_source line 27 · 2026-05-10T18:32:36.862Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NvGc9YHF4ModjvGY9fQTg7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.27641",
  "prompt": "Extract the full title, authors, abstract. Does this paper decompose attention heads by importance or type? Does it use per-head scoring? How does it relate to self-speculative decoding? What is the core methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d78bb5a-a68c-43ba-a4df-40dae9a65a27",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNEkgq42x8oRFCA9hMx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47fb8fbc-c00d-4cd0-bee2-b1c5b4971ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzKczq7EWXzStwymiEiMGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 913,
      "cache_creation_input_tokens": 3077,
      "cache_read_input_tokens": 14076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3077,
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

_source line 28 · 2026-05-10T18:32:36.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014DiSFDPYLJBRwwpbuEHh8J`</summary>

```json
{
  "query": "SpecAttn sparse attention self-speculative decoding head classification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47fb8fbc-c00d-4cd0-bee2-b1c5b4971ff4",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNEkgq42x8oRFCA9hMx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fbc8712-7cc9-43c1-907b-df066ceb5e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzKczq7EWXzStwymiEiMGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 913,
      "cache_creation_input_tokens": 3077,
      "cache_read_input_tokens": 14076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3077,
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

_source line 29 · 2026-05-10T18:32:37.503Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N942z4kbv4kToWipMtEQVM`</summary>

```json
{
  "query": "\"head importance\" \"layer skipping\" self-speculative decoding attention decomposition arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fbc8712-7cc9-43c1-907b-df066ceb5e7f",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNEkgq42x8oRFCA9hMx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af274ba3-9b88-4ddb-af0e-34ceea3dc60d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzKczq7EWXzStwymiEiMGr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 913,
      "cache_creation_input_tokens": 3077,
      "cache_read_input_tokens": 14076,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3077
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 913,
          "output_tokens": 277,
          "cache_read_input_tokens": 14076,
          "cache_creation_input_tokens": 3077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3077,
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

_source line 30 · 2026-05-10T18:32:42.231Z_

<details><summary>↩ Tool result · `toolu_01NvGc9YHF4ModjvGY9fQTg7`</summary>

```text
# SpecAttn: Speculating Sparse Attention - Analysis

## Full Metadata
**Title:** SpecAttn: Speculating Sparse Attention

**Author:** Harsh Shah

**Abstract:** The paper addresses computational bottlenecks in LLM inference by introducing a training-free approach integrating with speculative decoding. It achieves "over 75% reduction in key-value cache accesses with a mere 15.29% increase in perplexity on the PG-19 dataset."

## Key Findings

**Attention Head Decomposition:** The paper does not decompose attention heads by importance or type, nor does it employ per-head scoring mechanisms.

**Core Methodology:** SpecAttn uses three techniques:
1. KL divergence-based layer alignment between draft and target models
2. GPU-optimized sorting-free algorithm for top-p token selection from draft attention patterns
3. Dynamic key-value cache pruning guided by attention predictions

**Relationship to Self-Speculative Decoding:** SpecAttn directly enhances speculative decoding by "leveraging the computational work already performed in standard speculative decoding pipelines" rather than operating independently. It exploits draft model attention weights to identify important tokens for the target model, enabling sparse attention without redundant computation.

**Central Innovation:** The key insight is reusing attention computations already performed during speculative decoding to guide token selection, creating an efficient integrated approach rather than a standalone sparse attention method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47fb8fbc-c00d-4cd0-bee2-b1c5b4971ff4",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "e048ab3b-9455-47c0-a9ea-ec470872d4a4",
  "sourceToolAssistantUUID": "47fb8fbc-c00d-4cd0-bee2-b1c5b4971ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T18:32:44.393Z_

<details><summary>↩ Tool result · `toolu_014DiSFDPYLJBRwwpbuEHh8J`</summary>

```text
Web search results for query: "SpecAttn sparse attention self-speculative decoding head classification 2025 2026"

Links: [{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641v1"},{"title":"[2602.07223] SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://arxiv.org/abs/2602.07223"},{"title":"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://arxiv.org/html/2602.07223"},{"title":"[2510.27641] SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/abs/2510.27641"},{"title":"SPAttention: Sparse Attention Methods","url":"https://www.emergentmind.com/topics/spattention-methods"},{"title":"SPAttention: Structured Sparse Attention","url":"https://www.emergentmind.com/topics/spattention"},{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"},{"title":"Accelerating Large-Scale Reasoning Model Inference with ...","url":"https://arxiv.org/pdf/2512.01278"},{"title":"(PDF) SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://www.researchgate.net/publication/400603323_SpecAttn_Co-Designing_Sparse_Attention_with_Self-Speculative_Decoding"},{"title":"SpecAttn: Speculating Sparse Attention Harsh Shah Machine Learning Department","url":"https://openreview.net/pdf?id=5HgJc8B3j5"}]

I found relevant results about SpecAttn. Here's what the search reveals:

## SpecAttn Overview

There are actually two notable papers with the SpecAttn name from 2025-2026:

### 1. SpecAttn: Speculating Sparse Attention (October 2025)

SpecAttn is a novel training-free approach that seamlessly integrates with existing speculative decoding techniques to enable efficient sparse attention in pre-trained transformers. SpecAttn achieves over 75% reduction in key-value cache accesses with a mere 15.29% increase in perplexity on the PG-19 dataset, significantly outperforming existing sparse attention methods.

### 2. SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding (February 2026)

SpecAttn is a self-speculative decoding method with verification-guided sparse attention. SpecAttn identifies critical KV entries as a byproduct of verification and only loads these entries when drafting subsequent tokens. SpecAttn achieves 2.81× higher throughput over vanilla auto-regressive decoding and 1.29× improvement over state-of-the-art sparsity-based self-speculative decoding methods.

## Key Features

SpecAttn is a training-free framework that fuses speculative decoding with dynamic sparse attention to reduce KV cache usage, mapping layers using KL divergence similarity and employing a sorting-free top-p token selection mechanism.

Regarding head classification specifically, the result is averaged across all query heads.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fbc8712-7cc9-43c1-907b-df066ceb5e7f",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "fc958451-3792-47fb-9d3a-66481744c312",
  "sourceToolAssistantUUID": "2fbc8712-7cc9-43c1-907b-df066ceb5e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T18:32:46.356Z_

<details><summary>↩ Tool result · `toolu_01N942z4kbv4kToWipMtEQVM`</summary>

```text
Web search results for query: ""head importance" "layer skipping" self-speculative decoding attention decomposition arxiv 2026"

Links: [{"title":"Component-Aware Self-Speculative Decoding in Hybrid Language Models","url":"https://arxiv.org/html/2605.01106"},{"title":"ConfLayers: Adaptive Confidence-based Layer Skipping for Self-Speculative Decoding","url":"https://arxiv.org/html/2604.14612"},{"title":"CLaSp: In-Context Layer Skip for Self-Speculative Decoding","url":"https://arxiv.org/html/2505.24196v1"},{"title":"LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding","url":"https://arxiv.org/pdf/2404.16710"},{"title":"Paper page - LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding","url":"https://huggingface.co/papers/2404.16710"},{"title":"[2404.16710] LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding","url":"https://arxiv.org/abs/2404.16710"},{"title":"SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration | OpenReview","url":"https://openreview.net/forum?id=EKJhH5D5wA"},{"title":"Energy-Efficient Wireless LLM Inference via Uncertainty and Importance-Aware Speculative Decoding","url":"https://arxiv.org/html/2508.12590"},{"title":"LayerSkip: faster LLM Inference with Early Exit and Self-speculative decoding | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/layerskip-faster-llm-inference-with-early-exit-and-self-speculative-decoding-3110cb93c94e"},{"title":"DEL: Context-Aware Dynamic Exit Layer for Efficient Self- ...","url":"https://arxiv.org/pdf/2504.05598"}]

I found several relevant research papers on arXiv from 2025-2026 addressing layer skipping, self-speculative decoding, and related topics. Here are the key papers:

## Recent Papers (2025-2026):

1. **Component-Aware Self-Speculative Decoding in Hybrid Language Models** (arXiv 2605.01106, May 2026)
   This introduces component-aware self-speculative decoding, the first method to exploit the internal architectural heterogeneity of hybrid language models, isolating the SSM/linear-attention subgraph as a zero-cost internal draft. The paper shows a perfect inverse relationship: the more a model relies on its attention pathway, the less viable component-aware self-speculation becomes.

2. **ConfLayers: Adaptive Confidence-based Layer Skipping for Self-Speculative Decoding** (arXiv 2604.14612, April 2026)
   ConfLayers is a confidence-based method for constructing draft models in self-speculative decoding that adaptively skips layers based on intermediate confidence scores, eliminating the need for training a policy while preserving strong speed–quality trade-offs.

3. **CLaSp: In-Context Layer Skip for Self-Speculative Decoding** (arXiv 2505.24196, May 2025)
   CLaSp is an in-context layer-skipping strategy for self-speculative decoding that does not require additional drafting modules or extra training, instead employing a plug-and-play mechanism by skipping intermediate layers of the verify model to construct a compressed draft model.

## Earlier Foundational Work:

4. **LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding** (arXiv 2404.16710, 2024)
   LayerSkip presents an end-to-end solution to speed-up inference of large language models, applying layer dropout during training with low dropout rates for earlier layers and higher dropout rates for later layers.

These papers collectively explore how layer importance, attention mechanisms, and architectural components can be leveraged to create more efficient draft models for speculative decoding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af274ba3-9b88-4ddb-af0e-34ceea3dc60d",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "3cff7f08-9538-4434-a80c-dd4d450bed9e",
  "sourceToolAssistantUUID": "af274ba3-9b88-4ddb-af0e-34ceea3dc60d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-10T18:32:50.863Z_

This is very promising. Let me fetch the two most critical recent papers -- the "Component-Aware Self-Speculative Decoding" (May 2026) and the "SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding" (Feb 2026), as well as the ConfLayers paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cff7f08-9538-4434-a80c-dd4d450bed9e",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNFupnKeAQozPDX6L2F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ef1d834-ba8c-4dc6-90d0-c9e6b9d5b738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015K52JDFWfnLF6RsfiXdgmE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3485,
      "cache_read_input_tokens": 17153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3485,
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

_source line 34 · 2026-05-10T18:32:53.296Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018aS2fM7hEWgtCqnymKdFYh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.01106",
  "prompt": "Extract the full title, authors, abstract. Does this paper perform per-head or per-component importance scoring? Does it classify attention heads or decompose attention? How does it relate to head-selective importance scoring for self-speculative decoding? What is the core methodology and key finding?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ef1d834-ba8c-4dc6-90d0-c9e6b9d5b738",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNFupnKeAQozPDX6L2F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a644c961-7e97-47bb-8ee2-15fe5be32905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015K52JDFWfnLF6RsfiXdgmE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3485,
      "cache_read_input_tokens": 17153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3485,
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

_source line 35 · 2026-05-10T18:32:54.852Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NbFfiLMkrEoNqqvd14VKPK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.07223",
  "prompt": "Extract the full title, authors, abstract. Does this paper involve per-head scoring, head classification, or attention decomposition? How does it relate to self-speculative decoding with head-level analysis? What is the core methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a644c961-7e97-47bb-8ee2-15fe5be32905",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNFupnKeAQozPDX6L2F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbfa3712-ecaa-42d1-91e0-baacb9b73687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015K52JDFWfnLF6RsfiXdgmE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3485,
      "cache_read_input_tokens": 17153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3485,
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

_source line 36 · 2026-05-10T18:32:55.461Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XMy9Hrk9QHkKCvvb2R8YN7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.14612",
  "prompt": "Extract the full title, authors, abstract. Does this paper involve per-head importance scoring, head-selective mechanisms, or attention decomposition? How does it relate to self-speculative decoding? What is the core methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbfa3712-ecaa-42d1-91e0-baacb9b73687",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNFupnKeAQozPDX6L2F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3f2194b-9031-4c02-b3d4-56eeafc1d923",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015K52JDFWfnLF6RsfiXdgmE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3485,
      "cache_read_input_tokens": 17153,
      "output_tokens": 447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3485
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 447,
          "cache_read_input_tokens": 17153,
          "cache_creation_input_tokens": 3485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3485,
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

_source line 37 · 2026-05-10T18:32:59.317Z_

<details><summary>↩ Tool result · `toolu_018aS2fM7hEWgtCqnymKdFYh`</summary>

```text
# Paper Analysis

**Full Title:** Component-Aware Self-Speculative Decoding in Hybrid Language Models

**Authors:** Hector Borobia, Elies Seguí-Mas, Guillermina Tormo-Carbó

## Abstract Summary
The paper addresses speculative decoding acceleration by introducing a method that exploits internal architectural differences in hybrid language models. Rather than relying on external drafting models, the approach treats SSM/linear-attention subgraphs as internal drafters, eliminating computational overhead.

## Key Methodology Questions

**Per-Head or Per-Component Scoring:** This paper does NOT perform per-head importance scoring. Instead, it operates at the component level—examining entire SSM and attention modules rather than individual attention heads.

**Attention Head Classification:** The paper does not classify or decompose individual attention heads. It treats architectural components (Mamba-2, linear-attention, or standard attention layers) as unified units.

**Relation to Head-Selective Importance Scoring:** This work represents a different approach entirely. Rather than scoring head importance within attention mechanisms, it leverages the compositional structure of hybrid architectures themselves.

## Core Finding
The architectural composition pattern—specifically whether components are arranged in parallel or sequential configurations—fundamentally determines speculative decoding viability. Parallel hybrids (like Falcon-H1) achieve substantially higher acceptance rates (α = 0.68) compared to sequential designs (α = 0.038), an "18x gap attributable to how each architecture integrates its components."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a644c961-7e97-47bb-8ee2-15fe5be32905",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "ed097457-5e21-453a-bc00-e2ca01e10f00",
  "sourceToolAssistantUUID": "a644c961-7e97-47bb-8ee2-15fe5be32905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T18:32:59.998Z_

<details><summary>↩ Tool result · `toolu_01NbFfiLMkrEoNqqvd14VKPK`</summary>

```text
# Paper Summary: SpecAttn

**Full Title:** "SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding"

**Authors:** Yikang Yue, Yuqi Xue, Jian Huang

**Abstract:**
The paper addresses memory bottlenecks in long-context LLM inference by proposing SpecAttn, which combines sparse attention with self-speculative decoding. The method "identifies critical KV entries as a byproduct of verification" and selectively loads these entries during drafting. This approach achieves 2.81× throughput improvement over standard decoding and 1.29× over existing sparsity-based methods.

---

## Analysis

**Per-Head Scoring/Head Classification:** The provided content does not mention per-head attention analysis, head-level classification, or attention decomposition mechanisms. The paper focuses on KV cache entry selection rather than attention head-level operations.

**Relation to Head-Level Self-Speculative Decoding:** No explicit connection to head-level analysis is evident from this abstract. The methodology operates at the KV entry level across the full attention computation.

**Core Methodology:**
The approach uses verification-guided sparse attention, where:
- Critical KV entries are identified during the verification phase
- Only these selected entries are loaded when drafting subsequent tokens
- This reduces KV selection overhead while improving draft token acceptance rates

The innovation lies in treating KV criticality computation during verification as input for subsequent drafting stages, rather than relying on standalone KV selection algorithms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbfa3712-ecaa-42d1-91e0-baacb9b73687",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "d0ec216a-ecf7-49b7-a3b7-63bff87a0565",
  "sourceToolAssistantUUID": "bbfa3712-ecaa-42d1-91e0-baacb9b73687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T18:33:00.132Z_

<details><summary>↩ Tool result · `toolu_01XMy9Hrk9QHkKCvvb2R8YN7`</summary>

```text
# Paper Analysis: ConfLayers

## Full Title
"ConfLayers: Adaptive Confidence-based Layer Skipping for Self-Speculative Decoding"

## Authors
- Walaa Amer
- Uday das
- Fadi Kurdahi

## Abstract
The paper proposes a method that "iteratively computes confidence scores for all layers, selects layers to skip based on an adaptive threshold" to accelerate LLM inference. The approach achieves "up to 1.4x speedup over vanilla LLM generation" while maintaining output quality.

## Attention/Head Mechanisms
**No.** This paper does not involve per-head importance scoring, head-selective mechanisms, or attention decomposition. It operates at the layer level, not the attention head level.

## Relation to Self-Speculative Decoding
ConfLayers is directly positioned within self-speculative decoding. The method forms a draft model by skipping intermediate layers, which is then used in the speculative decoding pipeline where "approximate decoding using a compact version of the model" is combined with "selective re-evaluation by the full target model."

## Core Methodology
The approach uses a dynamic, iterative selection process:
1. Compute confidence scores across all layers
2. Apply an adaptive threshold to identify skippable layers
3. Evaluate the resulting subnetwork's performance
4. Iterate until convergence or maximum iterations

This avoids the computational overhead of learning explicit layer-skipping policies while maintaining adaptivity across different tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3f2194b-9031-4c02-b3d4-56eeafc1d923",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "0e947b56-0db4-4fd2-978f-65b05d651843",
  "sourceToolAssistantUUID": "c3f2194b-9031-4c02-b3d4-56eeafc1d923",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-10T18:33:03.557Z_

Now let me do one final round of searches to check if there is anything that directly combines head-level decomposition with self-speculative decoding, and also search for "decomposed importance scoring."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e947b56-0db4-4fd2-978f-65b05d651843",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNGvguHKLRd7dnLGeH4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b11be12-0cc1-45a2-85d0-e066fadd038e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9HSdL8qgNG5BPUNrsGdh2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 20638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1564,
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

_source line 41 · 2026-05-10T18:33:04.513Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PWLZcwEtvVFViwp8G3cLpf`</summary>

```json
{
  "query": "\"decomposed importance\" OR \"head-selective\" attention scoring speculative decoding arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b11be12-0cc1-45a2-85d0-e066fadd038e",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNGvguHKLRd7dnLGeH4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8ee7bdf-ba98-476f-b870-6d399add245d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9HSdL8qgNG5BPUNrsGdh2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 20638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1564,
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

_source line 42 · 2026-05-10T18:33:05.103Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JgUTDANrW4SNEMhLaHZP4x`</summary>

```json
{
  "query": "retrieval heads attention head type classification importance self-speculative decoding layer pruning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8ee7bdf-ba98-476f-b870-6d399add245d",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNGvguHKLRd7dnLGeH4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52ca29b7-3b60-4970-803a-c8a628012e04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9HSdL8qgNG5BPUNrsGdh2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 20638,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1564
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 20638,
          "cache_creation_input_tokens": 1564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1564,
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

_source line 43 · 2026-05-10T18:33:12.371Z_

<details><summary>↩ Tool result · `toolu_01JgUTDANrW4SNEMhLaHZP4x`</summary>

```text
Web search results for query: "retrieval heads attention head type classification importance self-speculative decoding layer pruning 2026"

Links: [{"title":"[1905.09418] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://arxiv.org/abs/1905.09418"},{"title":"The Story of Heads","url":"https://lena-voita.github.io/posts/acl19_heads.html"},{"title":"[PDF] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Analyzing-Multi-Head-Self-Attention:-Specialized-Do-Voita-Talbot/07a64686ce8e43ac475a8d820a8a9f1d87989583"},{"title":"Why multi-head self attention works: math, intuitions and 10+1 hidden insights | AI Summer","url":"https://theaisummer.com/self-attention/"},{"title":"Published as a conference paper at ICLR 2025 RETRIEVAL HEAD MECHANISTICALLY","url":"https://openreview.net/pdf?id=EytBpUGB1Z"},{"title":"GitHub - lena-voita/the-story-of-heads: This is a repository with the code for the ACL 2019 paper \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\" and the ACL 2021 paper \"Analyzing Source and Target Contributions to NMT Predictions\". · GitHub","url":"https://github.com/lena-voita/the-story-of-heads"},{"title":"Are Sixteen Heads Really Better than One? Paul Michel","url":"http://papers.neurips.cc/paper/9551-are-sixteen-heads-really-better-than-one.pdf"},{"title":"Towards Lossless Head Pruning through Automatic Peer ...","url":"https://www.ijcai.org/proceedings/2023/0568.pdf"},{"title":"PICKING THE UNDERUSED HEADS:","url":"https://arxiv.org/pdf/2312.09541"},{"title":"Pruning Attention Heads with Almost-sure Sparsity Targets | OpenReview","url":"https://openreview.net/forum?id=yhvtZdqBNm&noteId=mNFIXNMqUf"}]

Based on the search results, I found relevant information about attention heads, their classification, importance, and pruning. Here are the key findings:

## Attention Head Types and Classification

Research has identified three types of important heads by examining attention matrices: positional heads that attend mostly to neighbors, syntactic heads that point to tokens with specific syntactic relations, and heads that point to rare words in sentences.

## Retrieval Heads

A particularly relevant finding from recent research (2025) concerns retrieval heads: Retrieval heads are specialized attention heads responsible for redirecting relevant information from the input to the output. The retrieval score for a head is defined as the frequency of copy-paste behavior during tasks that require retrieving raw information from the input.

## Head Importance and Pruning

The most important and confident heads play consistent and often linguistically-interpretable roles. Research shows that the model prefers to prune encoder self-attention heads first, while decoder-encoder attention heads appear to be the most important for both datasets.

When it comes to pruning impact, masking out the top-K retrieval heads by highest retrieval scores severely impacts performance, whereas pruning random heads has far less effect, with pruning more than 50 retrieval heads—approximately 5% of all attention heads—resulting in performance dropping below 50%.

## Layer-wise Distribution

Self-attention heads are retained more readily in lower layers while decoder-encoder attention heads are retained in higher layers, suggesting that lower layers are mostly responsible for language modeling while higher layers are mostly responsible for conditioning on the source.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52ca29b7-3b60-4970-803a-c8a628012e04",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "99490e69-375f-4bff-a40a-7f1a8a725b5b",
  "sourceToolAssistantUUID": "52ca29b7-3b60-4970-803a-c8a628012e04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T18:33:12.493Z_

<details><summary>↩ Tool result · `toolu_01PWLZcwEtvVFViwp8G3cLpf`</summary>

```text
Web search results for query: ""decomposed importance" OR "head-selective" attention scoring speculative decoding arxiv 2026"

Links: [{"title":"Component-Aware Self-Speculative Decoding in Hybrid Language Models","url":"https://arxiv.org/html/2605.01106"},{"title":"[2510.21518] Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/abs/2510.21518"},{"title":"SinkRouter: Sink-Aware Routing for Efficient Long-Context Decoding in Large Language and Multimodal Models","url":"https://arxiv.org/html/2604.16883"},{"title":"SpecAttn: Speculating Sparse Attention","url":"https://arxiv.org/html/2510.27641"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/html/2510.21518"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"Speculative Speculative Decoding","url":"https://arxiv.org/html/2603.03251v2"},{"title":"Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance","url":"https://arxiv.org/html/2602.05774v1"},{"title":"Q K V softmax αij Attention Mechanisms in Neural Networks","url":"https://arxiv.org/pdf/2601.03329"},{"title":"Cross-Attention Speculative Decoding Wei Zhong wei.zhong@lge.com","url":"https://www.arxiv.org/pdf/2505.24544"}]

Based on the web search results, I found several relevant papers related to speculative decoding and attention mechanisms from 2026 arxiv submissions, though not all specifically mention both "decomposed importance" and "head-selective" attention scoring together.

Here are the most relevant findings:

## Head-Selective and Attention-Based Approaches

SinkRouter is a plug-and-play, training-free decoding framework that uses sink-aware signals to selectively bypass weakly contributing attention heads, operating at the head level to reduce unnecessary KV-cache loading while preserving retained context.

SpecAttn is a training-free approach that integrates with speculative decoding techniques by exploiting attention weights already computed by the draft model to score and select the most informative tokens at each generation step.

## Attention Head Analysis and Decomposition

Recent work on head specialization uses a sparse, interpretable decomposition approach where Simultaneous Orthogonal Matching Pursuit (SOMP) over the model's unembedding space identifies directions aligned with semantically meaningful attributes to recover sets of specialized heads.

## Hybrid Architecture Speculative Decoding

Component-Aware Self-Speculative Decoding addresses the limitation that existing self-speculative methods assume homogeneous layer stacks, which breaks down in hybrid architectures where layers contain fundamentally different computational components, with hybrid language models combining softmax attention with alternative sequence-processing mechanisms.

These papers represent recent advances in using attention head properties and component decomposition for efficient speculative decoding in 2026 arxiv research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8ee7bdf-ba98-476f-b870-6d399add245d",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "12bde961-50e2-42fa-9347-27e9027b03ae",
  "sourceToolAssistantUUID": "e8ee7bdf-ba98-476f-b870-6d399add245d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-10T18:33:17.176Z_

Let me fetch one more highly relevant paper -- SinkRouter, which appears to do per-head bypassing for decoding efficiency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12bde961-50e2-42fa-9347-27e9027b03ae",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNHqe5Ay6ZfdBLTC5gs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "458863c2-a61c-4ede-ad61-5f4f9fb5e958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjwcKwJ1Xe3e7vFvhDqcit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 22202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1105,
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

_source line 46 · 2026-05-10T18:33:20.063Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CjQyrgiRRQG7U8QV8ptN1d`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.16883",
  "prompt": "Extract the full title, authors, abstract. Does this paper classify heads by type or importance? Does it selectively bypass attention heads during decoding? How does it score head importance? What is the core methodology and how close is it to \"head-selective decomposed importance scoring\"?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "458863c2-a61c-4ede-ad61-5f4f9fb5e958",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNHqe5Ay6ZfdBLTC5gs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3336873-0708-4d12-88d5-58cec38fd7e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjwcKwJ1Xe3e7vFvhDqcit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 22202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1105,
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

_source line 47 · 2026-05-10T18:33:21.048Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Nu6v6SiUjTKpJv4EXBqGr9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.01278",
  "prompt": "Extract the full title, authors, abstract. Does this paper involve sparse attention combined with self-speculative decoding? Does it use head-level or layer-level analysis? What is the core methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3336873-0708-4d12-88d5-58cec38fd7e9",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNHqe5Ay6ZfdBLTC5gs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4933c691-ef58-42f1-8c75-665ef32602a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjwcKwJ1Xe3e7vFvhDqcit",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1000,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 22202,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1105
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1000,
          "output_tokens": 275,
          "cache_read_input_tokens": 22202,
          "cache_creation_input_tokens": 1105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1105,
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

_source line 48 · 2026-05-10T18:33:25.324Z_

<details><summary>↩ Tool result · `toolu_01CjQyrgiRRQG7U8QV8ptN1d`</summary>

```text
# SinkRouter Paper Analysis

**Full Title:** "SinkRouter: Sink-Aware Routing for Efficient Long-Context Decoding in Large Language and Multimodal Models"

**Authors:** Junnan Liu, Xinyan Liu, Peifeng Gao, Zhaobo Qi, Beichen Zhang, Weigang Zhang, Antoni Bert Chen

**Abstract:** The paper addresses memory efficiency in long-context LLM/LMM decoding by proposing a training-free framework that detects attention sink signals and skips computations producing near-zero outputs, achieving 2.03x speedup with 512K context across multiple benchmarks.

---

## Head Classification & Methodology

**Head Classification by Type/Importance:** The paper does NOT appear to classify heads by type or importance in the traditional sense.

**Selective Head Bypassing:** The document does NOT indicate that the method selectively bypasses attention heads during decoding.

**Head Importance Scoring:** No head importance scoring mechanism is described in the provided content.

**Core Methodology:** SinkRouter operates at a different architectural level—it focuses on the "attention sink phenomenon" as a "stable, reachable, and error-controllable fixed point constructed during training." Rather than scoring individual heads, it uses "sink signal detection" to skip computations across the attention mechanism.

**Proximity to Head-Selective Decomposed Importance Scoring:** This approach is **fundamentally different**. It doesn't decompose or score head importance; instead, it targets the broader attention sink phenomenon through mechanism-level optimization via custom Triton kernels with block-level branching and Split-K parallelism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3336873-0708-4d12-88d5-58cec38fd7e9",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "a544794c-1a4a-4808-bee5-8aab8bd4588c",
  "sourceToolAssistantUUID": "e3336873-0708-4d12-88d5-58cec38fd7e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-10T18:33:27.318Z_

<details><summary>↩ Tool result · `toolu_01Nu6v6SiUjTKpJv4EXBqGr9`</summary>

```text
# Paper Analysis

**Full Title:** "Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding"

**Authors:** Yilong Zhao, Jiaming Tang, Kan Zhu, Zihao Ye, Chi-Chih Chang, Chaofan Lin, Jongseok Park, Guangxuan Xiao, Mohamed S. Abdelfattah, Mingyu Gao, Baris Kasikci, Song Han, Ion Stoica

**Abstract Summary:** The paper addresses memory bandwidth bottlenecks in reasoning models by introducing SparseSpec, which combines sparse attention mechanisms with speculative decoding. The framework uses the same model for both drafting and verification, featuring a novel sparse attention mechanism called PillarAttn that "accurately selects critical tokens via elegantly reusing information from the verification stage." The system includes three optimizations: unified scheduling, delayed verification for overlap, and dynamic KV-Cache management, achieving up to 2.13x throughput speedup.

---

## Key Questions Answered

**Does it combine sparse attention with self-speculative decoding?** Yes, this is the core contribution of SparseSpec.

**Head-level or layer-level analysis?** The provided content does not specify the granularity of attention optimization (head vs. layer level).

**Core methodology:** Implements speculative decoding using the same model in both roles, with PillarAttn as a sparse attention draft model that intelligently reuses information from the verification phase, coupled with system-level optimizations for efficient batching and memory management.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4933c691-ef58-42f1-8c75-665ef32602a2",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "ada046e084cc3fb73",
  "type": "user",
  "uuid": "c82d0619-eae3-40bc-bfd8-d75f487b5c54",
  "sourceToolAssistantUUID": "4933c691-ef58-42f1-8c75-665ef32602a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-10T18:34:23.446Z_

I now have comprehensive findings. Here is the full report.

---

## Report: Competing Paper Verification for "Head-Selective Decomposed Importance Scoring for Self-Speculative Decoding"

---

### 1. LycheeDecode (Feb 2026, ICLR 2026, arXiv:2602.04541)

**Title:** "LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding"
**Authors:** Gang Lin, Dongfang Li, Zhuoen Chen, Yukun Shi, Xuhui Chen, Baotian Hu, Min Zhang

**Confirmed findings:**

- **Does it classify heads into types?** Yes. LycheeDecode partitions attention heads into two categories: (1) a small subset of **retrieval heads** that dynamically identify crucial tokens via full attention, and (2) a majority of **sparse heads** that reuse those token selections for efficient computation.
- **Does it apply different attention strategies per head type?** Yes. Retrieval heads perform full attention computation over the entire context. Sparse heads compute attention only on the sparse token subset identified by retrieval heads.
- **Core mechanism:** Uses a **Hard Kumaraswamy (HardKuma) distribution** to solve the discrete optimization problem of head type assignment in an end-to-end differentiable way. This is a learned partitioning, not a heuristic.
- **Performance:** Up to 2.7x speedup at 128K context on Llama3 and Qwen3, with quality comparable to or surpassing full attention.

**How close to "head-selective decomposed importance scoring"?** This is the **closest competing work** found. LycheeDecode performs head-type classification (retrieval vs. sparse) and applies differentiated computation per head type. However, it differs from a "decomposed importance scoring" proposal in several important ways:
  - LycheeDecode's classification is binary (retrieval vs. sparse), not a continuous decomposition of importance.
  - It does not decompose attention into structural/content components -- it classifies heads by their empirical sparsity behavior.
  - It targets **long-context KV cache efficiency**, not self-speculative decoding. There is no draft/verify pipeline.
  - It does not perform per-head importance scoring in the sense of ranking heads for layer skipping or self-speculation.

**Verdict:** Highly relevant as prior art for head-type classification, but addresses a different problem (long-context sparse decoding, not self-speculative decoding). A proposal on head-selective decomposed importance scoring for self-speculative decoding would need to clearly differentiate from LycheeDecode's binary head classification approach.

---

### 2. Urrutia et al. (Oct 2025, arXiv:2511.11579)

**Title:** "Decoupling Positional and Symbolic Attention Behavior in Transformers"
**Authors:** Felipe Urrutia, Jorge Salas, Alexander Kozachinskiy, Cristian Buc Calderon, Hector Pasten, Cristobal Rojas

**Confirmed findings:**

- **Does it prove positional and content attention are mutually exclusive?** Yes, explicitly. The paper provides formal definitions distinguishing positional from symbolic (content-based) head behavior and proves these are **"two mutually exclusive behaviors."**
- **Methodology:** Focuses on RoPE-based models. Demonstrates that large RoPE frequencies encode position while small frequencies encode meaning. Develops quantitative metrics to measure when heads behave positionally vs. symbolically. Causal experiments show that controlling frequency access causally influences model performance on targeted tasks.
- **Key finding:** Strong correspondence between head behavior type and frequency utilization patterns.

**How close to structural/content decomposition?** This paper provides **strong theoretical grounding** for a structural/content decomposition. It proves the dichotomy exists and is measurable. However:
  - It is a **theoretical/analytical** paper, not an inference optimization paper.
  - It does not propose any efficient inference method, scoring system, or speculative decoding technique.
  - It provides the theoretical justification that could motivate a decomposed importance scoring approach, but does not itself build one.

**Verdict:** Strong supporting evidence for the theoretical basis of decomposing attention into structural vs. content components. A proposal could cite this as foundational justification for why such decomposition is principled.

---

### 3. Broader Search: Recent Papers (March-May 2026)

#### 3a. SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding (Feb 2026, arXiv:2602.07223)
**Authors:** Yikang Yue, Yuqi Xue, Jian Huang

- Combines sparse attention with **self-speculative decoding** (same model for draft and verify).
- Identifies critical KV entries as a byproduct of the verification phase, then loads only those entries during drafting.
- Achieves 2.81x throughput over vanilla autoregressive decoding.
- **Does NOT operate at the head level.** Works at the KV entry level across all heads.
- **No head classification or decomposed scoring.**

**Relevance:** Directly relevant as a competing approach to efficient self-speculative decoding with sparse attention, but operates at a different granularity (KV entries, not heads).

#### 3b. Component-Aware Self-Speculative Decoding in Hybrid Language Models (May 2026, arXiv:2605.01106)

- Exploits architectural heterogeneity in **hybrid models** (e.g., Mamba + attention) to use SSM/linear-attention subgraphs as zero-cost internal drafters.
- Operates at the **component level** (entire attention vs. SSM modules), NOT at the individual head level.
- Key finding: parallel hybrid architectures achieve 18x higher acceptance rates than sequential ones.
- **No per-head importance scoring or attention decomposition.**

**Relevance:** Related concept of exploiting internal model structure for self-speculation, but fundamentally different scope (architectural components, not attention heads).

#### 3c. ConfLayers: Adaptive Confidence-based Layer Skipping (April 2026, arXiv:2604.14612)

- Adaptively skips layers based on confidence scores for self-speculative decoding.
- Achieves up to 1.4x speedup.
- **Operates at the layer level, not the head level.** No head-selective mechanisms.

#### 3d. SparseSpec: Accelerating Large-Scale Reasoning Model Inference (Dec 2025, arXiv:2512.01278)

- Combines sparse attention (PillarAttn) with self-speculative decoding for reasoning models.
- Reuses information from the verification stage to guide sparse attention during drafting.
- Achieves up to 2.13x throughput speedup.
- Does not specify head-level vs. layer-level granularity in the abstract.

#### 3e. SinkRouter (April 2026, arXiv:2604.16883)

- Training-free framework that detects attention sink signals and skips computations producing near-zero outputs.
- Does NOT classify heads or score head importance. Operates on the attention sink phenomenon at the mechanism level.
- Not related to speculative decoding.

---

### Summary of Key Findings

**No paper was found that directly proposes "head-selective decomposed importance scoring for self-speculative decoding."** The conceptual space is currently occupied by related but distinct approaches:

| Paper | Head-Level? | Decomposition? | Self-Spec Decoding? | Closest Overlap |
|-------|-------------|----------------|---------------------|-----------------|
| LycheeDecode | Yes (binary classification) | No (behavioral, not structural/content) | No | Head-type classification for sparse decoding |
| Urrutia et al. | Yes (theoretical) | Yes (positional vs. symbolic) | No | Theoretical basis for decomposition |
| SpecAttn (Feb 2026) | No (KV-entry level) | No | Yes | Self-spec + sparse attention |
| Component-Aware SSD | No (component level) | No | Yes | Internal structure for self-spec |
| ConfLayers | No (layer level) | No | Yes | Layer scoring for self-spec |
| SparseSpec | Unclear | No | Yes | Sparse attention + self-spec |

**The gap:** No existing work combines (1) per-head importance scoring with (2) a decomposed (structural/content) scoring framework with (3) self-speculative decoding. The proposal would sit at the intersection of LycheeDecode's head-type awareness, Urrutia et al.'s structural/content decomposition theory, and SpecAttn/SparseSpec's self-speculative decoding pipelines. This appears to be a genuinely novel combination as of May 2026.

**Key risks:** LycheeDecode is the strongest competing reference and must be carefully differentiated. Its binary head classification using HardKuma is conceptually adjacent to head-selective scoring, even though the downstream application (long-context sparse decoding vs. self-speculative decoding) differs significantly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c82d0619-eae3-40bc-bfd8-d75f487b5c54",
  "isSidechain": true,
  "agentId": "ada046e084cc3fb73",
  "requestId": "req_011CauNJvw6QWJUBjfQ4V5Z2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d76b96d5-15bf-4cee-bb83-ee6fe6f7d5e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCdZKc5jPGFH1ZeR2M8keQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2065,
      "cache_read_input_tokens": 23307,
      "output_tokens": 2178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2065
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2178,
          "cache_read_input_tokens": 23307,
          "cache_creation_input_tokens": 2065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2065,
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
