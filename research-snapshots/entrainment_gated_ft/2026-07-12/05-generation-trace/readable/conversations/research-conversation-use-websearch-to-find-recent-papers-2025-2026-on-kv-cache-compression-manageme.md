# Research conversation: Use WebSearch to find recent papers (2025-2026) on KV cache compression/management specifically for agentic LLM workload

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa9988d91ce776806.jsonl`
- **Structured JSON:** [`c6c2cd5c08fa3ed66343.json`](../../sessions/c6/c6c2cd5c08fa3ed66343.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-11T23:36:21.317Z_

Use WebSearch to find recent papers (2025-2026) on KV cache compression/management specifically for agentic LLM workloads. Search for:
1. "agentic KV cache" compression 2026
2. "multi-step" "KV cache" agent compression 2026
3. "trajectory" KV cache compression agent LLM 2026
4. "SideQuest" KV cache agentic reasoning 2026
5. "CodeComp" KV cache agentic coding 2026
6. "PBKV" prediction-based KV cache agent 2026
7. "KVFlow" KV cache agent workflow 2026

For each paper found, note the title, date, venue, and key contribution. I need to know if there are competitors the proposal might be missing, especially any that do JOINT quantization-eviction for agentic workloads. Report everything you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "c15fab2f-e2f8-4d21-a2b8-2b1c712432ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-11T23:36:23.062Z_

I'll search for recent papers on KV cache compression/management for agentic LLM workloads. Let me run these searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c15fab2f-e2f8-4d21-a2b8-2b1c712432ad",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfDXkfWFpFdvwVmQZr8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "92e43370-9b56-443c-9586-05ca9b6cc24d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014vAriHegVuukqTzqFr33Pr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-11T23:36:23.065Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XJGCJHLMsiQF8kRkfWUj6h`</summary>

```json
{
  "query": "agentic KV cache compression 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92e43370-9b56-443c-9586-05ca9b6cc24d",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfDXkfWFpFdvwVmQZr8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b34a9d32-f1f4-45c7-b2ee-e915a117dd25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014vAriHegVuukqTzqFr33Pr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T23:36:23.266Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LD5xNt8psXip9webmWACPj`</summary>

```json
{
  "query": "multi-step KV cache agent compression 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b34a9d32-f1f4-45c7-b2ee-e915a117dd25",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfDXkfWFpFdvwVmQZr8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b9bca4c-06f3-4292-a5b8-094b08b6d627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014vAriHegVuukqTzqFr33Pr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-11T23:36:23.494Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G2LqMc47QUbcXLoSJSrwGK`</summary>

```json
{
  "query": "trajectory KV cache compression agent LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b9bca4c-06f3-4292-a5b8-094b08b6d627",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfDXkfWFpFdvwVmQZr8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "48d00e83-ba7d-4bac-b482-3d97fc780e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014vAriHegVuukqTzqFr33Pr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-11T23:36:23.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CSfDDZEJ8am9RHorSg3s16`</summary>

```json
{
  "query": "SideQuest KV cache agentic reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48d00e83-ba7d-4bac-b482-3d97fc780e41",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfDXkfWFpFdvwVmQZr8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f09628c0-26ec-4b36-83e5-f68de68bf3c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014vAriHegVuukqTzqFr33Pr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-11T23:36:23.714Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HnywvaaniUJu1LFY46s9oY`</summary>

```json
{
  "query": "CodeComp KV cache agentic coding 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f09628c0-26ec-4b36-83e5-f68de68bf3c5",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfDXkfWFpFdvwVmQZr8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0400622e-a5cd-47cd-9452-16343c56dce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014vAriHegVuukqTzqFr33Pr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-11T23:36:23.908Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01324bHoaWokBqt8LpEm7aeu`</summary>

```json
{
  "query": "PBKV prediction-based KV cache agent 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0400622e-a5cd-47cd-9452-16343c56dce2",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfDXkfWFpFdvwVmQZr8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ea8b6ecc-7e94-4f86-9910-76b83ba65264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014vAriHegVuukqTzqFr33Pr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 16153,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 639
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 373,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 639,
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

_source line 9 · 2026-05-11T23:36:23.970Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sdzvb9aaUu8g9NSYQm3Q9S`</summary>

```json
{
  "query": "KVFlow KV cache agent workflow 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea8b6ecc-7e94-4f86-9910-76b83ba65264",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfDXkfWFpFdvwVmQZr8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fd50543f-89d3-479e-a8cb-c844b18d9f6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014vAriHegVuukqTzqFr33Pr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 16153,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 639
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 373,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 639,
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

_source line 10 · 2026-05-11T23:36:31.676Z_

<details><summary>↩ Tool result · `toolu_01324bHoaWokBqt8LpEm7aeu`</summary>

```text
Web search results for query: "PBKV prediction-based KV cache agent 2026"

Links: [{"title":"Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management","url":"https://arxiv.org/html/2605.06472v1"},{"title":"PaFu-KV: Past & Future-Informed Cache Policy","url":"https://www.emergentmind.com/topics/past-and-future-informed-kv-cache-policy-pafu-kv"},{"title":"Predictive Multi-Tier Memory Management for KV Cache in Large-Scale GPU Inference","url":"https://arxiv.org/html/2604.26968"},{"title":"KV Cache: The Secret to Cheaper and Faster AI Inference – Frank's World of Data Science & AI","url":"https://www.franksworld.com/2026/05/09/kv-cache-the-secret-to-cheaper-and-faster-ai-inference/"},{"title":"Nvidia and its partners' KV Cache extenders","url":"https://www.blocksandfiles.com/ai-ml/2026/03/30/nvidia-and-its-partners-kv-cache-extenders/5209284"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/html/2603.10899"},{"title":"Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING","url":"https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"What is KV Cache? Efficient LLM Inference | Ultralytics","url":"https://www.ultralytics.com/glossary/kv-cache"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"}]

Based on the search results, I found relevant information about PBKV:

PBKV is a system dubbed Prediction-Based KV-Cache Management designed for efficient LLM serving. 

LLM-based workflows compose specialized agents to execute complex tasks, and these agents usually share substantial context, allowing KV-Cache reuse to save computation. Existing approaches either manage KV-Cache at agent level and fail to exploit the reuse opportunities within workflows, or manage cache at the workflow level but assume that each workflow calls a static sequence of agents. However, practical workflows are typically dynamic, where the sequence of invoked agents and thus induced cache reuse opportunities depend on the context of each task.

For each workflow, PBKV predicts the agent invocations in several future steps by fusing the guidance from historical workflows and context of the target workflow. Based on the predictions, PBKV estimates the reuse potential of cache entries and keeps the high-potential entries in GPU memory.

PBKV is guided by two design principles, i.e., hierarchical eviction and conservative prefetching, that together identify cache with low reuse value for reclamation while preserving high-value cache.

PBKV reduces the average workflow latency by up to 1.39x on realistic dynamic workflows according to the research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea8b6ecc-7e94-4f86-9910-76b83ba65264",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "436607c0-5e6c-4a4b-b24b-1e22cdbce826",
  "sourceToolAssistantUUID": "ea8b6ecc-7e94-4f86-9910-76b83ba65264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-11T23:36:31.699Z_

<details><summary>↩ Tool result · `toolu_01Sdzvb9aaUu8g9NSYQm3Q9S`</summary>

```text
Web search results for query: "KVFlow KV cache agent workflow 2026"

Links: [{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM- ...","url":"https://arxiv.org/pdf/2507.07400"},{"title":"Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management","url":"https://arxiv.org/html/2605.06472v1"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM- ...","url":"https://openreview.net/pdf?id=5Iw1nDtYmT"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://arxiv.org/html/2507.07400"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows | OpenReview","url":"https://openreview.net/forum?id=5Iw1nDtYmT"},{"title":"[2507.07400] KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://arxiv.org/abs/2507.07400"},{"title":"Paper published at the Lifelong Agent Workshop @ ICLR 2026","url":"https://openreview.net/pdf/5c6ed290be90eea7b75202124c5bffecac714a4c.pdf"},{"title":"CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/html/2604.25080"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250707400P/abstract"},{"title":"Persistent Q4 KV Cache for Multi-Agent LLM Inference on ...","url":"https://arxiv.org/pdf/2603.04428"}]

Based on the search results, here's what I found about KVFlow and KV cache management in agent workflows:

## KVFlow: Efficient Prefix Caching for Agent Workflows

KVFlow is a workflow-aware KV cache management framework tailored for agentic workloads that abstracts the agent execution schedule as an Agent Step Graph and assigns each agent a steps-to-execution value that estimates its temporal proximity to future activation.

### Key Problem It Addresses

Current systems typically evict KV caches using a Least Recently Used (LRU) policy, which fails to anticipate future agent usage and often discards KV caches shortly before their reuse, leading to frequent cache misses and substantial recomputation or swapping overhead.

### Core Features

KVFlow addresses this through two main mechanisms:

1. **Workflow-Aware Eviction Strategy**: KVFlow adopts a workflow-aware eviction strategy that prioritizes evicting KV caches belonging to agents with large steps-to-execution, and assigns eviction priorities at the cache node level to enable fine-grained and efficient management.

2. **KV Prefetching**: KVFlow introduces a fully overlapped KV prefetching mechanism that proactively loads required KV tensors from CPU to GPU ahead of time, effectively eliminating prefix cache misses without stalling generation.

### Performance

Compared to SGLang with hierarchical radix cache, KVFlow achieves up to 1.83× speedup for single workflows with large prompts, and up to 2.19× speedup for scenarios with many concurrent workflows.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd50543f-89d3-479e-a8cb-c844b18d9f6d",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "9c2c5e73-70f2-49a8-8f01-2b75bf2f157d",
  "sourceToolAssistantUUID": "fd50543f-89d3-479e-a8cb-c844b18d9f6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:36:31.825Z_

<details><summary>↩ Tool result · `toolu_01HnywvaaniUJu1LFY46s9oY`</summary>

```text
Web search results for query: "CodeComp KV cache agentic coding 2026"

Links: [{"title":"CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/html/2604.10235"},{"title":"[2604.10235] CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/abs/2604.10235"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"KV Cache in Local AI: Why Your Agentic Setup is 90% Slower Than It Should Be | ThinkSmart.Life Research","url":"https://thinksmart.life/research/posts/kv-cache-local-inference/"},{"title":"Prompt Caching and Context Optimization in Coding Agents","url":"https://susheemk.substack.com/p/prompt-caching-and-context-optimization"},{"title":"The KV Cache Wars? - by Ken Huang - Agentic AI - Substack","url":"https://kenhuangus.substack.com/p/the-kv-cache-wars"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"A Coding Implementation on kvcached for Elastic KV Cache Memory, Bursty LLM Serving, and Multi-Model GPU Sharing - MarkTechPost","url":"https://www.marktechpost.com/2026/04/25/a-coding-implementation-on-kvcached-for-elastic-kv-cache-memory-bursty-llm-serving-and-multi-model-gpu-sharing/"},{"title":"SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/html/2602.22603v1"},{"title":"The Best Open-Source LLMs for Agentic Coding in 2026 | MindStudio","url":"https://www.mindstudio.ai/blog/best-open-source-llms-agentic-coding-2026"}]

Based on the search results, here's information about CodeComp and related KV cache technologies for agentic coding in 2026:

## CodeComp: Structural KV Cache Compression

CodeComp is a training-free KV cache compression framework for agentic code tasks that incorporates structural priors from static program analysis. 

CodeComp leverages the Code Property Graph (CPG) extracted by Joern to guide two complementary compression decisions: span-level structural protection, which preserves structurally critical tokens from eviction, and structure-aware budget allocation, which distributes the compression budget according to each chunk's structural importance.

### Key Problem It Solves

Existing KV cache compression methods exhibit a structural blind spot when applied to code: attention-based importance estimation fails to capture program-semantic relationships, leading to systematic mis-pruning of structurally critical tokens such as callsites, branches, and assignments.

### Performance and Integration

CodeComp is implemented on SGLang and integrates seamlessly into large-scale agentic code workflows without modifying the underlying model. Across bug localization and code generation benchmarks, CodeComp consistently outperforms attention-only compression baselines under equal memory budgets, recovering the majority of full-context accuracy under aggressive KV cache compression, while matching the patch generation quality of uncompressed full-context inference.

### Context and Motivation

Agentic code tasks such as fault localization and patch generation require processing long codebases under tight memory constraints, where the Key-Value (KV) cache becomes the primary inference bottleneck.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0400622e-a5cd-47cd-9452-16343c56dce2",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "b44b54c0-5e6b-4b3c-ac08-c7b8948bd768",
  "sourceToolAssistantUUID": "0400622e-a5cd-47cd-9452-16343c56dce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-11T23:36:32.222Z_

<details><summary>↩ Tool result · `toolu_01CSfDDZEJ8am9RHorSg3s16`</summary>

```text
Web search results for query: "SideQuest KV cache agentic reasoning 2026"

Links: [{"title":"SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/html/2602.22603v1"},{"title":"[2602.22603] SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/abs/2602.22603"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"Sanjay Kariyappa's research works | Georgia Institute of Technology and other places","url":"https://www.researchgate.net/scientific-contributions/Sanjay-Kariyappa-2145271758"},{"title":"Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management","url":"https://arxiv.org/html/2605.06472v1"},{"title":"KV Cache in Local AI: Why Your Agentic Setup is 90% Slower Than It Should Be | ThinkSmart.Life Research","url":"https://thinksmart.life/research/posts/kv-cache-local-inference/"},{"title":"CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/html/2604.10235v1"},{"title":"The KV Cache Wars? - by Ken Huang - Agentic AI - Substack","url":"https://kenhuangus.substack.com/p/the-kv-cache-wars"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Nvidia and its partners' KV Cache extenders","url":"https://www.blocksandfiles.com/ai-ml/2026/03/30/nvidia-and-its-partners-kv-cache-extenders/5209284"}]

Based on the search results, here's what I found about SideQuest, KV cache management, and agentic reasoning in 2026:

## SideQuest Overview

SideQuest is designed for agentic workloads that require multi-step reasoning to resolve complex user queries. It leverages the Large Reasoning Model (LRM) itself to perform KV cache compression by reasoning about the usefulness of tokens in its context.

## The Problem SideQuest Solves

Long-running agentic tasks, such as deep research, require multi-hop reasoning over information distributed across multiple webpages and documents. In such tasks, the LLM context is dominated by tokens from external retrieval, causing memory usage to grow rapidly and limiting decode performance. 

While several KV cache compression techniques exist for long-context inputs, existing heuristics fail to support multi-step reasoning models effectively.

## How SideQuest Works

SideQuest equips the model with a mechanism to selectively clear segments of its own KV cache, effectively allowing the model to perform its own memory garbage collection. To ensure that the overhead of this self-management does not interfere with the primary task, KV cache compression is framed as an auxiliary task executed in parallel to the main reasoning process. This architecture prevents the management tokens from polluting the model's primary attention window while maintaining a lean, high-fidelity KV cache.

## Performance Results

Evaluations, using a model trained with just 215 samples, show that SideQuest reduces peak token usage by up to 65% on agentic tasks with minimal degradation in accuracy, outperforming heuristic-based KV cache compression techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f09628c0-26ec-4b36-83e5-f68de68bf3c5",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "bcdf1593-059c-4128-9697-09f89c2291ec",
  "sourceToolAssistantUUID": "f09628c0-26ec-4b36-83e5-f68de68bf3c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T23:36:32.995Z_

<details><summary>↩ Tool result · `toolu_01XJGCJHLMsiQF8kRkfWUj6h`</summary>

```text
Web search results for query: "agentic KV cache compression 2026"

Links: [{"title":"[2604.10235] CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/abs/2604.10235"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/html/2604.10235"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"Researchers from MIT, NVIDIA, and Zhejiang University Propose TriAttention: A KV Cache Compression Method That Matches Full Attention at 2.5× Higher Throughput - MarkTechPost","url":"https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/"},{"title":"The KV Cache Wars? - by Ken Huang - Agentic AI - Substack","url":"https://kenhuangus.substack.com/p/the-kv-cache-wars"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Google’s TurboQuant Compression May Support Faster Inference, Same Accuracy on Less Capable Hardware - InfoQ","url":"https://www.infoq.com/news/2026/04/turboquant-compression-kv-cache/"},{"title":"Google's new TurboQuant algorithm speeds up AI memory 8x, cutting costs by 50% or more | VentureBeat","url":"https://venturebeat.com/infrastructure/googles-new-turboquant-algorithm-speeds-up-ai-memory-8x-cutting-costs-by-50"},{"title":"New KV cache compaction technique cuts LLM memory 50x without accuracy loss | VentureBeat","url":"https://venturebeat.com/orchestration/new-kv-cache-compaction-technique-cuts-llm-memory-50x-without-accuracy-loss"}]

Based on the search results, here's what's happening with agentic KV cache compression in 2026:

## Key Methods and Techniques

The approaches to KV cache optimization fall into three broad families: reducing what gets stored through eviction and sparse attention, compressing what gets stored through quantization and dimensionality reduction, and rethinking where context lives through hierarchical memory and hardware innovation.

## Notable 2026 Advances

**CodeComp for Coding**: CodeComp is a training-free KV cache compression framework that incorporates static program analysis into LLM inference via Code Property Graph priors extracted by Joern. Agentic code tasks such as fault localization and patch generation require processing long codebases under tight memory constraints, where the Key-Value (KV) cache becomes the primary inference bottleneck.

**TurboQuant**: TurboQuant, introduced in 2026, is a training-free method that reduces KV memory usage by up to 6x while maintaining low-latency inference on the H100 GPU. On standard benchmarks like LongBench and Needle in a Haystack, a 3.5-bit TurboQuant implementation matched the performance of full 16-bit precision across Gemma and Mistral models.

**Attention Matching**: A technique called Attention Matching manages to compact the context by up to 50x with very little loss in quality.

**TriAttention**: The 2026 research frontier is moving toward latent-space compaction (Attention Matching, 50× compaction) and reasoning-aware compression (TriAttention, 10.7× memory reduction on AIME25 at matched accuracy).

## Industry Impact

Google is providing the essential "plumbing" for the burgeoning "Agentic AI" era: the need for massive, efficient, and searchable vectorized memory that can finally run on the hardware users already own.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b34a9d32-f1f4-45c7-b2ee-e915a117dd25",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "5eff4a0a-d936-4f54-ab34-c328ab7ddcea",
  "sourceToolAssistantUUID": "b34a9d32-f1f4-45c7-b2ee-e915a117dd25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T23:36:33.770Z_

<details><summary>↩ Tool result · `toolu_01LD5xNt8psXip9webmWACPj`</summary>

```text
Web search results for query: "multi-step KV cache agent compression 2026"

Links: [{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Google’s TurboQuant Compression May Support Faster Inference, Same Accuracy on Less Capable Hardware - InfoQ","url":"https://www.infoq.com/news/2026/04/turboquant-compression-kv-cache/"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"Compress the KV Cache with TurboQuant and Haystack | Haystack","url":"https://haystack.deepset.ai/tutorials/49_turboquant_quantization_with_huggingface"},{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | OpenReview","url":"https://openreview.net/forum?id=JFygzwx8SJ"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"Researchers from MIT, NVIDIA, and Zhejiang University Propose TriAttention: A KV Cache Compression Method That Matches Full Attention at 2.5× Higher Throughput - MarkTechPost","url":"https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/"},{"title":"New KV cache compaction technique cuts LLM memory 50x without accuracy loss | VentureBeat","url":"https://venturebeat.com/orchestration/new-kv-cache-compaction-technique-cuts-llm-memory-50x-without-accuracy-loss"},{"title":"Published as a conference paper at ICLR 2026 ADAPTIVE KV-CACHE COMPRESSION","url":"https://www.arxiv.org/pdf/2509.03136"}]

Based on the search results, here's what I found about multi-step KV cache agent compression in 2026:

## Recent Advances in KV Cache Compression for Agents (2026)

### Key Methods for Agent Workloads

The 2026 research frontier is moving toward latent-space compaction (Attention Matching, 50× compaction) and reasoning-aware compression (TriAttention, 10.7× memory reduction on AIME25 at matched accuracy).

For agent-specific use cases, prefix caching gives 85-95% cost savings on cache hits — on agent loops, multi-tenant SaaS, repo Q&A, and long-doc workflows, hit-rates of 60-85% are achievable, dropping per-call cost by 5-12×.

### Multi-Step Compression Approaches

TurboQuant uses a two-step approach: First, data vectors are rotated (randomized Hadamard transform) which spreads out the values and removes outlier-heavy coordinate distribution, and second, the Quantized Johnson-Lindenstrauss (QJL) transform is applied to remove bias created by the first step.

### Performance on Agentic Workloads

As of 2026, the most recent methodologies leverage specialized tools such as TurboQuant, VQKV, and Quant VideoGen (QVG), which are designed to compress KV caches while maintaining fidelity in long-horizon agentic workloads, and this article tests the impact of KV cache quantization on long-horizon agentic coding workloads.

LongFlow, a 2026 method, addresses compression errors by using an importance estimation metric derived from intermediate attention results, minimizing the impact of compression on critical tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b9bca4c-06f3-4292-a5b8-094b08b6d627",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "898c9184-52ca-436a-b6ed-f9e816b3ed01",
  "sourceToolAssistantUUID": "0b9bca4c-06f3-4292-a5b8-094b08b6d627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T23:36:34.942Z_

<details><summary>↩ Tool result · `toolu_01G2LqMc47QUbcXLoSJSrwGK`</summary>

```text
Web search results for query: "trajectory KV cache compression agent LLM 2026"

Links: [{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Reducing Cost of LLM Agents with Trajectory Reduction","url":"https://arxiv.org/pdf/2509.23586"},{"title":"TurboQuant: Google’s 6x KV Cache Compression for LLMs | byteiota","url":"https://byteiota.com/turboquant-googles-6x-kv-cache-compression-for-llms/"},{"title":"TurboQuant KV Cache Compression: What Changes for LLM Inference","url":"https://www.kriraai.com/blog/turboquant-kv-cache-compression-changes-llm-inference"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"KV Cache Transform Coding for Compact Storage in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=aNVKROYpLB"},{"title":"Google TurboQuant: 2026 LLM Compression Guide | Articles","url":"https://o-mega.ai/articles/google-turboquant-the-2026-llm-compression-guide"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"},{"title":"Implementing Google’s TurboQuant: KV Cache Compression and LLM Evaluation with W&B | by Dave Davies | Online Inference | Mar, 2026 | Medium","url":"https://medium.com/online-inference/implementing-googles-turboquant-kv-cache-compression-and-llm-evaluation-with-w-b-1403d460846b"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"}]

Based on the search results, I found relevant information about trajectory reduction in LLM agents and KV cache compression techniques in 2026:

## Trajectory Reduction for LLM Agents

The root cause of efficiency issues in LLM agents lies in the ever-growing trajectory, where tool calls and their results are kept until the agent completes the entire task, so if the LLM opens a large file or runs a command that generates verbose output, the computational cost of these tokens snowballs in each subsequent step.

A notable research contribution is a paper titled "Reducing Cost of LLM Agents with Trajectory Reduction" published in July 2026, which appears to address the cost challenges of agent systems through trajectory management.

## KV Cache Compression in 2026

The field has seen significant advancement in KV cache compression techniques:

**TurboQuant**: TurboQuant is a training-free, data-oblivious vector quantization algorithm that compresses the KV cache of large language models to 3 bits per value, achieving a 6x reduction in KV cache memory and up to 8x speedup on NVIDIA H100 GPUs for attention computation, all without measurable accuracy degradation. The algorithm was announced in March 2026 and presented at ICLR on April 23-25.

**Other Methods**: The 2026 research frontier is moving toward latent-space compaction (Attention Matching, 50× compaction) and reasoning-aware compression (TriAttention, 10.7× memory reduction on AIME25 at matched accuracy).

**KVTC Transform Coding**: KVTC achieves up to 20x compression while maintaining reasoning and long-context accuracy, and 40x or higher for specific use cases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48d00e83-ba7d-4bac-b482-3d97fc780e41",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "af580250-3388-4b42-8b15-a7eb58783a83",
  "sourceToolAssistantUUID": "48d00e83-ba7d-4bac-b482-3d97fc780e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-11T23:36:37.217Z_

Excellent results! Let me search for a few more specific papers that might have been mentioned and look for any joint quantization-eviction approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af580250-3388-4b42-8b15-a7eb58783a83",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfEYT7oau2stPZCqfCe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "82aa9ade-302e-48bb-b79b-f920724226da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2KFUK1Z3sav8CBCVDW7eK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3874,
      "cache_creation_input_tokens": 4620,
      "cache_read_input_tokens": 16792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4620,
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

_source line 18 · 2026-05-11T23:36:37.437Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ETCfffAk7SCjbWqMqb4CvK`</summary>

```json
{
  "query": "joint quantization eviction KV cache agent 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82aa9ade-302e-48bb-b79b-f920724226da",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfEYT7oau2stPZCqfCe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0e9d3613-3236-438e-aaa5-0dff3e30493d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2KFUK1Z3sav8CBCVDW7eK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3874,
      "cache_creation_input_tokens": 4620,
      "cache_read_input_tokens": 16792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4620,
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

_source line 19 · 2026-05-11T23:36:37.648Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RyXShR9VFim4mgJ8HBnifs`</summary>

```json
{
  "query": "LongFlow KV cache compression 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e9d3613-3236-438e-aaa5-0dff3e30493d",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfEYT7oau2stPZCqfCe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9fc7edae-6544-4d5c-85e3-8617f78ad4da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2KFUK1Z3sav8CBCVDW7eK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3874,
      "cache_creation_input_tokens": 4620,
      "cache_read_input_tokens": 16792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4620,
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

_source line 20 · 2026-05-11T23:36:37.886Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BsWFJGBcRpr4JiHpF7MypK`</summary>

```json
{
  "query": "TriAttention KV cache compression reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fc7edae-6544-4d5c-85e3-8617f78ad4da",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfEYT7oau2stPZCqfCe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ec0b47b-7ac8-4f8c-b8a1-f2ca7c90b0cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2KFUK1Z3sav8CBCVDW7eK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3874,
      "cache_creation_input_tokens": 4620,
      "cache_read_input_tokens": 16792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4620,
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

_source line 21 · 2026-05-11T23:36:38.206Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0168Y382bz7ZYxkUexGSsnqK`</summary>

```json
{
  "query": "Attention Matching KV cache 50x compaction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ec0b47b-7ac8-4f8c-b8a1-f2ca7c90b0cc",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfEYT7oau2stPZCqfCe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c9c8e60c-f604-4504-93b0-0dfa7607b412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2KFUK1Z3sav8CBCVDW7eK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3874,
      "cache_creation_input_tokens": 4620,
      "cache_read_input_tokens": 16792,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4620
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3874,
          "output_tokens": 233,
          "cache_read_input_tokens": 16792,
          "cache_creation_input_tokens": 4620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4620,
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

_source line 22 · 2026-05-11T23:36:45.415Z_

<details><summary>↩ Tool result · `toolu_01RyXShR9VFim4mgJ8HBnifs`</summary>

```text
Web search results for query: "LongFlow KV cache compression 2026"

Links: [{"title":"[2603.11504] LongFlow: Efficient KV Cache Compression for Reasoning M","url":"https://arxiv.org/abs/2603.11504"},{"title":"LongFlow: Efficient KV Cache Compression for Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=rz6WybXjgk"},{"title":"LongFlow: Efficient KV Cache Compression for Reasoning Models","url":"https://arxiv.org/pdf/2603.11504"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"EFFICIENT KV CACHE COMPRESSION - LONGFLOW","url":"https://openreview.net/pdf?id=rz6WybXjgk"},{"title":"Paper page - TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://huggingface.co/papers/2604.04921"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"GitHub - dongwonjo/FastKV: [ACL Findings 2026] Official Implementation of \"FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration\" · GitHub","url":"https://github.com/dongwonjo/FastKV"}]

Based on the search results, here's what I found about LongFlow KV cache compression:

## Overview

LongFlow is a KV cache compression method with an efficient importance estimation metric derived from an intermediate result of attention computation using only the current query.

## Performance

LongFlow achieves up to an 11.8 times throughput improvement with 80% KV cache compression with minimal impact on model accuracy.

## Key Features

The design introduces negligible computational overhead and requires no auxiliary storage, with a custom kernel that fuses FlashAttention, importance estimation, and token eviction into a single optimized operator to improve system-level efficiency.

## Target Use Case

LongFlow is designed for recent reasoning models such as OpenAI-o1 and DeepSeek-R1, which have shown strong performance on complex tasks including mathematical reasoning and code generation, but produce substantially longer output sequences, requiring large KV caches that result in high memory consumption and severe bandwidth pressure during attention computation.

## Research Details

The paper was submitted on March 12, 2026. The research was conducted by Yi Su and five other authors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fc7edae-6544-4d5c-85e3-8617f78ad4da",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "d6cba084-f77e-4c86-bc27-bea3c3a74a5b",
  "sourceToolAssistantUUID": "9fc7edae-6544-4d5c-85e3-8617f78ad4da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-11T23:36:45.910Z_

<details><summary>↩ Tool result · `toolu_01ETCfffAk7SCjbWqMqb4CvK`</summary>

```text
Web search results for query: "joint quantization eviction KV cache agent 2026"

Links: [{"title":"HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=sLG2XsjSDe"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/pdf/2512.14946"},{"title":"Towards 10 Million Context Length LLM Inference with KV ...","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/neurips-2024-kvquant.pdf"},{"title":"[2603.04428] Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/abs/2603.04428"},{"title":"[2512.14946] EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/abs/2512.14946"},{"title":"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/html/2603.04428v1"},{"title":"Mixed-Dimension Budget Allocation for Efficient KV Cache ...","url":"https://arxiv.org/pdf/2603.20616"},{"title":"GitHub - Aitherium/aitherkvcache: Near-optimal KV cache quantization for LLM inference. Sub-byte compression (2-4 bit) within 2.7x of information-theoretic optimum. arXiv:2504.19874 · GitHub","url":"https://github.com/Aitherium/aitherkvcache"},{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"}]

Based on the search results, here's what I found regarding joint quantization and eviction for KV cache in 2026:

## Key Research Papers and Approaches

HqeKV is a hybrid compression framework built on both quantization and eviction, offering finer-grained compression options that adapt smoothly to the varying importance of cached KV pairs. It includes a joint K–V importance metric to provide more accurate importance assessment results. HqeKV improves output quality from 40.53 to 49.98 under the same memory constraints, outperforming state-of-the-art alternatives.

Another significant system is EVICPRESS: EVICPRESS is a KV-cache management system that applies lossy compression and adaptive eviction to KV cache across multiple storage tiers. It jointly optimizes the eviction and compression decisions across all KV caches to minimize average generation latency without hurting quality.

## Agent-Specific Approaches

For multi-agent systems, one approach addresses this by persisting each agent's KV cache to disk in 4-bit quantized format and reloading it directly into the attention layer, eliminating redundant O(n) prefill computation via direct cache restoration.

## 2026 Research Trends

The 2026 research frontier is moving toward latent-space compaction (Attention Matching, 50× compaction) and reasoning-aware compression (TriAttention, 10.7× memory reduction on AIME25 at matched accuracy).

These developments represent significant advances in making LLM inference more efficient by intelligently managing KV cache memory through combined quantization and eviction strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e9d3613-3236-438e-aaa5-0dff3e30493d",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "c0b32a41-3a70-4de3-ac19-ee009cb21d5c",
  "sourceToolAssistantUUID": "0e9d3613-3236-438e-aaa5-0dff3e30493d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-11T23:36:46.323Z_

<details><summary>↩ Tool result · `toolu_0168Y382bz7ZYxkUexGSsnqK`</summary>

```text
Web search results for query: "Attention Matching KV cache 50x compaction 2026"

Links: [{"title":"New KV cache compaction technique cuts LLM memory 50x without accuracy loss | VentureBeat","url":"https://venturebeat.com/orchestration/new-kv-cache-compaction-technique-cuts-llm-memory-50x-without-accuracy-loss"},{"title":"[2602.16284] Fast KV Compaction via Attention Matching","url":"https://arxiv.org/abs/2602.16284"},{"title":"Startup News: Hidden Blueprint Revealed for Cutting LLM Memory Costs by 50x Without Compromising Accuracy in 2026","url":"https://blog.mean.ceo/startup-news-llm-memory-costs-cut-50x-accuracy-intact-2026/"},{"title":"Research: Implement \"Fast KV Compaction via Attention Matching\" for extreme VRAM savings · Issue #20037 · ggml-org/llama.cpp","url":"https://github.com/ggml-org/llama.cpp/issues/20037"},{"title":"[2602.16284v1] Fast KV Compaction via Attention Matching","url":"https://arxiv.org/abs/2602.16284v1"},{"title":"Fast KV Compaction via Attention Matching","url":"https://arxiv.org/pdf/2602.16284"},{"title":"LLM Memory Usage Reduced by 50x","url":"https://businessanalytics.substack.com/p/llm-memory-usage-reduced-by-50x"},{"title":"Fast KV Compaction via Attention Matching","url":"https://www.emergentmind.com/papers/2602.16284"},{"title":"Fast KV Compaction via Attention Matching","url":"https://www.catalyzex.com/paper/fast-kv-compaction-via-attention-matching"},{"title":"Fast KV Compaction via Attention Matching | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/fast-kv-compaction-via-attention-matching"}]

Based on the web search results, here's what I found about Attention Matching KV cache 50x compaction:

## Overview

A new technique developed by researchers at MIT called Attention Matching manages to compact the context by up to 50x with very little loss in quality. This approach for fast context compaction in latent space constructs compact keys and values to reproduce attention outputs and preserve attention mass at a per-KV-head level.

## Key Advantages

The key finding was the ability of Attention Matching to compact the model's KV cache by 50x without reducing the accuracy, while taking only seconds to process the documents. Attention Matching achieves high-level compaction ratios and quality while being orders of magnitude faster than gradient-based optimization.

## How It Works

Attention Matching compresses the KV cache by preserving two core properties: the attention output (extracted info) and attention mass (token weights), using fast algebraic approximations instead of slow neural retraining.

## Real-World Applications

The technique compresses the key-value cache in large language models by up to 50x in seconds, preserving full accuracy on long-context tasks like analyzing 8,000-word documents or 60,000-token medical records. The AM pipeline can be stacked over summarization, achieving compound compaction rates exceeding 200× with only marginal further loss.

The research was published on February 18, 2026, and represents a significant advancement in making long-context LLM inference more efficient and practical for real-world deployment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9c8e60c-f604-4504-93b0-0dfa7607b412",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "359291c2-975b-4d61-8542-321d32e2622c",
  "sourceToolAssistantUUID": "c9c8e60c-f604-4504-93b0-0dfa7607b412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-11T23:36:48.037Z_

<details><summary>↩ Tool result · `toolu_01BsWFJGBcRpr4JiHpF7MypK`</summary>

```text
Web search results for query: "TriAttention KV cache compression reasoning 2026"

Links: [{"title":"🔥 Introducing TriAttention: A New KV Cache Compression Technique | by Mayur Jain | MLWorks | Apr, 2026 | Medium","url":"https://medium.com/mlworks/introducing-triattention-a-new-kv-cache-compression-technique-60d1215f5af2"},{"title":"Paper page - TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://huggingface.co/papers/2604.04921"},{"title":"GitHub - WeianMao/triattention: TriAttention — Efficient long reasoning with trigonometric KV cache compression. Enables OpenClaw local deployment on memory-constrained GPUs.","url":"https://github.com/WeianMao/triattention"},{"title":"[2604.04921] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921"},{"title":"Researchers from MIT, NVIDIA, and Zhejiang University Propose TriAttention: A KV Cache Compression Method That Matches Full Attention at 2.5× Higher Throughput - MarkTechPost","url":"https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/"},{"title":"[2604.04921v1] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921v1"},{"title":"TriAttention | Efficient KV Cache Compression for Long-Context Reasoning","url":"https://weianmao.github.io/tri-attention-project-page/"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/html/2604.04921v1"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://papers.fzhiy.net/papers/2604-04921.html"},{"title":"TriAttention KV Cache Compression: How to Stop Long AI Chats from Slowing Down and Speed Up Long-Context Reasoning","url":"https://www.intelligentliving.co/triattention-kv-cache-compression/"}]

Based on the search results, here's what I found about TriAttention KV cache compression for reasoning:

## Overview

TriAttention addresses KV cache memory bottlenecks in LLMs by leveraging Q/K vector concentration in pre-RoPE space to improve key importance estimation and enable efficient long-context generation.

## The Problem

Extended reasoning in large language models (LLMs) creates severe KV cache memory bottlenecks. Long-chain reasoning is one of the most compute-intensive tasks in modern LLMs. When a model like DeepSeek-R1 or Qwen3 works through a complex math problem, it can generate tens of thousands of tokens. Every one of those tokens must be stored in the KV cache — a memory structure that holds the Key and Value vectors the model needs to attend back to during generation, and for many deployment scenarios, this growth eventually exhausts GPU memory entirely.

## How It Works

TriAttention observes that Q and K vectors are highly concentrated around fixed non-zero centers and remain stable across positions -- Q/K concentration. This concentration causes queries to preferentially attend to keys at specific distances (e.g., nearest keys), with the centers determining which distances are preferred via a trigonometric series. Via the trigonometric series, the distance preference characterized by these centers is used to score keys according to their positions, and Q/K norms are leveraged as an additional signal for importance estimation.

## Performance Results

On AIME25 with 32K-token generation, TriAttention matches Full Attention reasoning accuracy while achieving 2.5x higher throughput or 10.7x KV memory reduction, whereas leading baselines achieve only about half the accuracy at the same efficiency. On throughput, TriAttention achieves 1,405 tokens per second on MATH 500 against Full Attention's 223 tokens per second, a 6.3× speedup.

## Practical Impact

TriAttention enables OpenClaw deployment on a single consumer GPU, where long context would otherwise cause out-of-memory with Full Attention.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ec0b47b-7ac8-4f8c-b8a1-f2ca7c90b0cc",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "c5bbad9f-4e6e-4063-93d5-c8f984d386c5",
  "sourceToolAssistantUUID": "1ec0b47b-7ac8-4f8c-b8a1-f2ca7c90b0cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-11T23:36:50.085Z_

Perfect! Now let me search for a few more papers to ensure comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5bbad9f-4e6e-4063-93d5-c8f984d386c5",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfFW3n54QrqEPYAWQPM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aaa8c9f2-a35f-4f97-8aa3-3fd9bd91aa03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fg3qcA2yMZdmB4LT74aNLz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 918,
      "cache_creation_input_tokens": 7261,
      "cache_read_input_tokens": 21412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7261,
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

_source line 27 · 2026-05-11T23:36:50.218Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KwNTd1p1dbafnNkwtCHqPq`</summary>

```json
{
  "query": "HqeKV hybrid quantization eviction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaa8c9f2-a35f-4f97-8aa3-3fd9bd91aa03",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfFW3n54QrqEPYAWQPM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a449eeb1-980e-4a28-adb5-6f7ff38c5acd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fg3qcA2yMZdmB4LT74aNLz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 918,
      "cache_creation_input_tokens": 7261,
      "cache_read_input_tokens": 21412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7261,
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

_source line 28 · 2026-05-11T23:36:50.622Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015EpshGLSUqgwGahCL47xhi`</summary>

```json
{
  "query": "EVICPRESS joint compression eviction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a449eeb1-980e-4a28-adb5-6f7ff38c5acd",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfFW3n54QrqEPYAWQPM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3002d0df-a78c-4403-9623-d5e9b686ab7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fg3qcA2yMZdmB4LT74aNLz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 918,
      "cache_creation_input_tokens": 7261,
      "cache_read_input_tokens": 21412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7261,
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

_source line 29 · 2026-05-11T23:36:50.712Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MZGV7Hj2Yb4aVrdFZPmwYx`</summary>

```json
{
  "query": "KVzip query-agnostic compression 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3002d0df-a78c-4403-9623-d5e9b686ab7e",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfFW3n54QrqEPYAWQPM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "45aa292d-fb46-4450-81f6-49cc879c23d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fg3qcA2yMZdmB4LT74aNLz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 918,
      "cache_creation_input_tokens": 7261,
      "cache_read_input_tokens": 21412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7261,
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

_source line 30 · 2026-05-11T23:36:56.390Z_

<details><summary>↩ Tool result · `toolu_01MZGV7Hj2Yb4aVrdFZPmwYx`</summary>

```text
Web search results for query: "KVzip query-agnostic compression 2026"

Links: [{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | OpenReview","url":"https://openreview.net/forum?id=JFygzwx8SJ"},{"title":"[2505.23416] KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction","url":"https://arxiv.org/abs/2505.23416"},{"title":"GitHub - snu-mllab/KVzip: [NeurIPS'25 Oral] Query-agnostic KV cache eviction: 3–4× reduction in memory and 2× decrease in latency (Qwen3/2.5, Gemma3, LLaMA3)","url":"https://github.com/snu-mllab/KVzip"},{"title":"ICML KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction","url":"https://icml.cc/virtual/2025/51778"},{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | Request PDF","url":"https://www.researchgate.net/publication/392204044_KVzip_Query-Agnostic_KV_Cache_Compression_with_Context_Reconstruction"},{"title":"KVzip+: Query-Agnostic Cache Compression for LLMs","url":"https://www.emergentmind.com/topics/kvzip-f20aca11-8dcb-448c-95e5-495a16d101d4"},{"title":"Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://www.arxiv.org/pdf/2601.17668"},{"title":"NeurIPS Poster KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction","url":"https://neurips.cc/virtual/2025/poster/118741"},{"title":"Paper page - KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction","url":"https://huggingface.co/papers/2505.23416"},{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | alphaXiv","url":"https://www.alphaxiv.org/resources/2505.23416v1"}]

Based on the search results, here's what I found about KVzip query-agnostic compression:

## Overview

KVzip is a query-agnostic KV cache eviction method enabling effective reuse of compressed KV caches across diverse queries. KVzip quantifies the importance of a KV pair using the underlying LLM to reconstruct original contexts from cached KV pairs, subsequently evicting pairs with lower importance.

## Performance Results

KVzip reduces KV cache size by 3-4× and FlashAttention decoding latency by approximately 2×, with negligible performance loss in question-answering, retrieval, reasoning, and code comprehension tasks. Evaluations include various models such as LLaMA3.1, Qwen2.5, and Gemma3, with context lengths reaching up to 170K tokens.

## Recent Developments in 2026

In January 2026, Fast KVzip was released, which eliminates compression overhead and enhances both prefill and decoding efficiency. Additionally, KVzip+ is a query-agnostic key-value cache compression method that leverages information-theoretic context reconstruction and reduces the cache size by up to 4× with less than 1% accuracy loss on benchmarks like SQuAD and GSM8K.

## NeurIPS Recognition

KVzip was accepted at NeurIPS 2025 as an Oral Presentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45aa292d-fb46-4450-81f6-49cc879c23d2",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "b14f137d-57a1-4fa0-b4d0-77ceddc328ca",
  "sourceToolAssistantUUID": "45aa292d-fb46-4450-81f6-49cc879c23d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-11T23:36:57.619Z_

<details><summary>↩ Tool result · `toolu_01KwNTd1p1dbafnNkwtCHqPq`</summary>

```text
Web search results for query: "HqeKV hybrid quantization eviction 2026"

Links: [{"title":"HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=sLG2XsjSDe"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"GitHub - AmesianX/TurboQuant: TurboQuant KV Cache Compression for llama.cpp — 5.2x memory reduction with near-lossless quality | Implementation of Google DeepMind's TurboQuant (ICLR 2026)","url":"https://github.com/AmesianX/TurboQuant"},{"title":"© 2025 Akshat Sharma - IDEALS - University of Illinois","url":"https://www.ideals.illinois.edu/items/136217/bitstreams/445287/data.pdf"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"1 A Survey on Large Language Model Acceleration based on KV Cache Management","url":"https://arxiv.org/pdf/2412.19442"},{"title":"A Survey on Large Language Model Acceleration based on KV Cache Management","url":"https://arxiv.org/html/2412.19442v3"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization | Request PDF","url":"https://www.researchgate.net/publication/397202512_KVQuant_Towards_10_Million_Context_Length_LLM_Inference_with_KV_Cache_Quantization"}]

Based on the search results, here's what I found about HqeKV:

HqeKV is a hybrid compression framework built on both quantization and eviction, offering finer-grained compression options that adapt smoothly to the varying importance of cached KV pairs.

**Key Features:**

An integrated optimizer automatically selects the best compression action for each cached element, maximizing quality while insulating end-users from tedious low-level tuning details.

HqeKV designs a joint K–V importance metric to provide more accurate importance assessment results so that the optimizer can make smarter decisions.

HqeKV supports flexible conversion policies across multiple quantization precision levels, to further reduce quality degradation.

**Performance:**

Extensive experiments show that HqeKV improves output quality from 40.53 to 49.98 under the same memory constraints, outperforming state-of-the-art alternatives.

Code is available at https://github.com/skywclouds/HqeKV.

The research addresses a key challenge in long-context LLM inference: while caching intermediate key-value (KV) pairs eliminates redundancy, it introduces severe memory overhead, particularly in long-context settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a449eeb1-980e-4a28-adb5-6f7ff38c5acd",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "6f6d83c6-0036-4b84-9b90-e134960948c6",
  "sourceToolAssistantUUID": "a449eeb1-980e-4a28-adb5-6f7ff38c5acd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-11T23:37:00.138Z_

<details><summary>↩ Tool result · `toolu_015EpshGLSUqgwGahCL47xhi`</summary>

```text
Web search results for query: "EVICPRESS joint compression eviction 2026"

Links: [{"title":"[2512.14946] EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/abs/2512.14946"},{"title":"EvicPress: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/html/2512.14946"},{"title":"(PDF) EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://www.researchgate.net/publication/398806282_EVICPRESS_Joint_KV-Cache_Compression_and_Eviction_for_Efficient_LLM_Serving"},{"title":"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/evicpress-joint-kv-cache-compression-and-eviction-for-efficient-llm-serving/"},{"title":"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2512.14946"},{"title":"EVICPRESS jointly optimizes offloading and compression, achieving much... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/EVICPRESS-jointly-optimizes-offloading-and-compression-achieving-much-better-trade-off_fig1_398806282"},{"title":"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving – Own Your AI","url":"https://ownyourai.com/evicpress-joint-kv-cache-compression-and-eviction-for-efficient-llm-serving/"},{"title":"Efficient Memory Management for Large Language Model Serving with PagedAttention | Request PDF","url":"https://www.researchgate.net/publication/374920067_Efficient_Memory_Management_for_Large_Language_Model_Serving_with_PagedAttention"},{"title":"Joint KV-Cache Compression and Eviction for Efficient LLM ...","url":"https://www.semanticscholar.org/paper/EVICPRESS:-Joint-KV-Cache-Compression-and-Eviction-Feng-Liu/9bbaf2992fecb53cbe8ce289b6a4c081417d20dd"},{"title":"Tenant advocates hope for eviction moratorium during ICE surge | MPR News","url":"https://www.mprnews.org/story/2026/01/23/tenant-advocates-hope-for-eviction-moratorium-during-ice-surge"}]

Based on the search results, here's what I found about EVICPRESS:

EVICPRESS is a KV-cache management system that applies lossy compression and adaptive eviction to KV cache across multiple storage tiers. It jointly optimizes the eviction and compression decisions across all KV caches to minimize average generation latency without hurting quality.

**Key Features:**

EVICPRESS's profiling module periodically updates the utility function scores on all possible eviction-compression configurations for all contexts and places KV caches using a fast heuristic to rearrange KV caches on all storage tiers, with the goal of maximizing the utility function scores on each storage tier.

**Performance Results:**

EVICPRESS achieves up to 2.19x faster time-to-first-token (TTFT) at equivalent generation quality. Compared to the baselines that evict KV cache or compress KV cache, EVICPRESS achieves higher KV-cache hit rates on fast devices, i.e., lower delay, while preserving high generation quality by applying conservative compression to contexts that are sensitive to compression errors.

The research was published in December 2025 and represents advances in efficient Large Language Model (LLM) inference by managing the growing demands on GPU memory through intelligent cache management strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3002d0df-a78c-4403-9623-d5e9b686ab7e",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "bca6e0f0-3185-423e-aea3-8fc2f5d2859e",
  "sourceToolAssistantUUID": "3002d0df-a78c-4403-9623-d5e9b686ab7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-11T23:37:02.006Z_

Excellent! Let me do a couple more targeted searches to ensure I've captured all the major recent papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bca6e0f0-3185-423e-aea3-8fc2f5d2859e",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfGPkYSvx9WckpPY2ML",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1420af18-9dcd-49b4-bf23-e416adb9bda6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XX2CfNx8RQWuW2WMNurQYU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 955,
      "cache_creation_input_tokens": 3071,
      "cache_read_input_tokens": 28673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3071,
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

_source line 34 · 2026-05-11T23:37:02.250Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H28BY3rSaTw9N2CS6nxUEz`</summary>

```json
{
  "query": "LookaheadKV predictive eviction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1420af18-9dcd-49b4-bf23-e416adb9bda6",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfGPkYSvx9WckpPY2ML",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2a549e51-ede0-40a7-8402-5c188d149183",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XX2CfNx8RQWuW2WMNurQYU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 955,
      "cache_creation_input_tokens": 3071,
      "cache_read_input_tokens": 28673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3071,
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

_source line 35 · 2026-05-11T23:37:02.514Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ETgX1i9BWy7xSc4KWrRwBG`</summary>

```json
{
  "query": "KVTC transform coding 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a549e51-ede0-40a7-8402-5c188d149183",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfGPkYSvx9WckpPY2ML",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "79e594e1-fef1-43df-934b-82b6f33a7cef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XX2CfNx8RQWuW2WMNurQYU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 955,
      "cache_creation_input_tokens": 3071,
      "cache_read_input_tokens": 28673,
      "output_tokens": 131,
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
          "input_tokens": 955,
          "output_tokens": 131,
          "cache_read_input_tokens": 28673,
          "cache_creation_input_tokens": 3071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3071,
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

_source line 36 · 2026-05-11T23:37:08.900Z_

<details><summary>↩ Tool result · `toolu_01ETgX1i9BWy7xSc4KWrRwBG`</summary>

```text
Web search results for query: "KVTC transform coding 2026"

Links: [{"title":"NVIDIA Researchers Introduce KVTC Transform Coding Pipeline to Compress Key-Value Caches by 20x for Efficient LLM Serving - MarkTechPost","url":"https://www.marktechpost.com/2026/02/10/nvidia-researchers-introduce-kvtc-transform-coding-pipeline-to-compress-key-value-caches-by-20x-for-efficient-llm-serving/"},{"title":"KV Cache Transform Coding for Compact Storage in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=aNVKROYpLB"},{"title":"[2511.01815] KV Cache Transform Coding for Compact Storage in LLM Inference","url":"https://arxiv.org/abs/2511.01815"},{"title":"Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING","url":"https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"},{"title":"Nvidia says it can shrink LLM memory 20x without changing model weights | VentureBeat","url":"https://venturebeat.com/orchestration/nvidia-shrinks-llm-memory-20x-without-changing-model-weights"},{"title":"GitHub - OnlyTerp/kvtc: First open-source KVTC implementation (NVIDIA, ICLR 2026) -- 8-32x KV cache compression via PCA + adaptive quantization + entropy coding · GitHub","url":"https://github.com/OnlyTerp/kvtc"},{"title":"NVIDIA'S KVTC brings 20x memory savings to open source LLM infrastructure | Open Source For You - technology - Read this story on Magzter.com","url":"https://www.magzter.com/stories/technology/Open-Source-For-You/NVIDIAS-KVTC-BRINGS-20X-MEMORY-SAVINGS-TO-OPEN-SOURCE-LLM-INFRASTRUCTURE"},{"title":"KV Cache Transform Coding Reduces LLM Memory Usage by 20x | Satyendra Pasalapudi☁ posted on the topic | LinkedIn","url":"https://www.linkedin.com/posts/satyendra_nvidia-brings-20x-memory-savings-to-open-activity-7442883927398334465-1PK-"},{"title":"Nvidia Brings 20x Memory Savings To Open Source LLM Infrastructure - Open Source For You","url":"https://www.opensourceforu.com/2026/03/nvidia-brings-20x-memory-savings-to-open-source-llm-infrastructure/"},{"title":"ICLR Poster KV Cache Transform Coding for Compact Storage in LLM Inference","url":"https://iclr.cc/virtual/2026/poster/10008708"}]

Based on the search results, here's what KVTC transform coding is:

## Overview

NVIDIA researchers have introduced KVTC (KV Cache Transform Coding), a lightweight transform coder that compresses KV caches for compact on-GPU and off-GPU storage.

## Technical Approach

The method utilizes a pipeline inspired by classical media compression, combining PCA-based feature decorrelation, adaptive quantization via dynamic programming, and lossless entropy coding (DEFLATE).

## Performance

It achieves up to 20x compression while maintaining reasoning and long-context accuracy. For specific use cases, it can reach 40x or higher.

## Key Features

To maintain model performance, KVTC avoids compressing the 4 oldest 'attention sink' tokens and a 'sliding window' of the 128 most recent tokens.

The system is 'tuning-free,' requiring only a brief initial calibration (under 10 minutes for a 12B model) that leaves model parameters unchanged and adds minimal storage overhead—only 2.4% for a 70B model.

## Publication

The paper was published as a conference paper at ICLR 2026 by researchers from NVIDIA and the University of Warsaw.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79e594e1-fef1-43df-934b-82b6f33a7cef",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "3a7c634a-76dd-4d5d-bfff-552b31b23a22",
  "sourceToolAssistantUUID": "79e594e1-fef1-43df-934b-82b6f33a7cef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-11T23:37:10.106Z_

<details><summary>↩ Tool result · `toolu_01H28BY3rSaTw9N2CS6nxUEz`</summary>

```text
Web search results for query: "LookaheadKV predictive eviction 2026"

Links: [{"title":"[2603.10899] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899"},{"title":"GitHub - SamsungLabs/LookaheadKV: [ICLR 2026] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation · GitHub","url":"https://github.com/SamsungLabs/LookaheadKV"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/html/2603.10899v1"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by ...","url":"https://arxiv.org/pdf/2603.10899"},{"title":"[2603.10899v1] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899v1"},{"title":"ICLR Poster LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://iclr.cc/virtual/2026/poster/10009483"},{"title":"Paper page - LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://huggingface.co/papers/2603.10899"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation | OpenReview","url":"https://openreview.net/forum?id=RVLMGPXt2i"},{"title":"[Blog] LookaheadKV: Fast and Accurate KV Cache Eviction ...","url":"https://research.samsung.com/blog/LookaheadKV-Fast-and-Accurate-KV-Cache-Eviction-by-Glimpsing-into-the-Future-without-Generation"},{"title":"LOOKAHEADKV: FAST AND ACCURATE KV CACHE EVICTION ...","url":"https://openreview.net/pdf/c50329bc498e901e0546f2761d86a8d7dcdacf67.pdf"}]

Based on the search results, here's information about LookaheadKV and predictive eviction:

## Overview

LookaheadKV is a novel method to perform efficient KV cache eviction by predicting the attention pattern of the model's future response with parameter-efficient modules—lookahead tokens and lookahead LoRA.

## The Problem

Transformer-based large language models (LLMs) rely on key-value (KV) caching to avoid redundant computation during autoregressive inference. While this mechanism greatly improves efficiency, the cache size grows linearly with the input sequence length, quickly becoming a bottleneck for long-context tasks.

## How LookaheadKV Works

LookaheadKV is a lightweight eviction framework that leverages the strength of surrogate future response without requiring explicit draft generation. Rather than using computationally expensive draft generation like other approaches, LookaheadKV directly predicts future attention patterns to accurately estimate token importance.

The method uses two key components:
- Learnable lookahead tokens combined with specialized LoRA modules—allowing the model to "glimpse" into future attention distributions with minimal computational cost.

## Performance Results

The method reduces the eviction cost by up to 14.5x, leading to significantly faster time-to-first-token. Additionally, LookaheadKV shows a performance drop less than 0.7% with 1K cache budget (~81% compression).

The work was accepted at ICLR 2026 and is available on GitHub from Samsung Labs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a549e51-ede0-40a7-8402-5c188d149183",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "5e4bd3b5-4459-45e5-b1d1-345cf0e8c47d",
  "sourceToolAssistantUUID": "2a549e51-ede0-40a7-8402-5c188d149183",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-11T23:37:16.187Z_

Perfect! Let me do one final search to check for any other agent-specific or multi-agent systems I might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e4bd3b5-4459-45e5-b1d1-345cf0e8c47d",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfHKz6nfxomirLPbgRv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "49cafac5-9721-4ab6-bb11-ed692f4f8310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015icQCCAEZcyFuZhnMr4FTG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1059,
      "cache_creation_input_tokens": 2120,
      "cache_read_input_tokens": 31744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2120,
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

_source line 39 · 2026-05-11T23:37:16.530Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A25NyFrndoHPPchZPamxNs`</summary>

```json
{
  "query": "\"agentic workload\" KV cache 2026 compression management"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49cafac5-9721-4ab6-bb11-ed692f4f8310",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfHKz6nfxomirLPbgRv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d0358789-3a15-48e1-9fba-982f07703495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015icQCCAEZcyFuZhnMr4FTG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1059,
      "cache_creation_input_tokens": 2120,
      "cache_read_input_tokens": 31744,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2120
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1059,
          "output_tokens": 94,
          "cache_read_input_tokens": 31744,
          "cache_creation_input_tokens": 2120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2120,
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

_source line 40 · 2026-05-11T23:37:25.669Z_

<details><summary>↩ Tool result · `toolu_01A25NyFrndoHPPchZPamxNs`</summary>

```text
Web search results for query: ""agentic workload" KV cache 2026 compression management"

Links: [{"title":"SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/html/2602.22603"},{"title":"[2604.10235] CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/abs/2604.10235"},{"title":"CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/html/2604.10235"},{"title":"[2602.22603] SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/abs/2602.22603"},{"title":"LMCACHE: AN EFFICIENT KV CACHE LAYER FOR ENTERPRISE-SCALE LLM INFERENCE","url":"https://lmcache.ai/tech_report.pdf"},{"title":"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/html/2603.04428v1"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"CacheTTL: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV","url":"https://arxiv.org/pdf/2511.02230"},{"title":"KV Cache Optimization (KVO) - Agentic Design | Agentic Design Patterns","url":"https://agentic-design.ai/patterns/context-management/kv-cache-optimization"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"}]

Based on the search results, here's what recent research shows about agentic workload KV cache compression and management in 2026:

## Key Approaches

Agentic workloads involve a context that evolves over time as the model performs multiple rounds of tool-calling and internal reflection. This creates unique challenges for KV cache management.

### Model-Driven Management

SideQuest is a novel approach that shifts KV cache management from a fixed heuristic to an intelligent, model-driven process. SideQuest reduces peak token usage by up to 65% on agentic tasks with minimal degradation in accuracy, outperforming heuristic-based KV cache compression techniques.

### Structure-Aware Compression

For agentic code tasks such as fault localization and patch generation that require processing long codebases under tight memory constraints, CodeComp is a training-free KV cache compression framework that incorporates static program analysis into LLM inference via Code Property Graph priors.

### Quantization Methods

TurboQuant, introduced in 2026, is a training-free method that reduces KV memory usage by up to 6x while maintaining low-latency inference on the H100 GPU. VQKV, a training-free vector quantization method, achieves over 80% compression with minimal performance degradation by mapping high-dimensional cache vectors to a compact codebook.

### Edge Device Solutions

Agent-memory persists each agent's KV cache to disk in 4-bit quantized format and reloads it directly into the attention layer, eliminating redundant prefill computation via direct cache restoration.

### Enterprise-Scale Management

LMCache exposes APIs that allow developers and operators to locate, move, pin, and compress KV cache, allowing higher-level applications such as query schedulers to make better decisions like KV cache-aware query routing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0358789-3a15-48e1-9fba-982f07703495",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aa9988d91ce776806",
  "type": "user",
  "uuid": "9c96e86e-b0a2-49d7-99fd-1fcc16a802e8",
  "sourceToolAssistantUUID": "d0358789-3a15-48e1-9fba-982f07703495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-11T23:37:58.136Z_

Excellent! Now I have comprehensive coverage. Let me compile my final report with all the papers found.

## Comprehensive Report: KV Cache Compression/Management for Agentic LLM Workloads (2025-2026)

Based on my search, I've identified **16 major papers and approaches** for KV cache compression and management, with special attention to agentic workloads. Here's the complete landscape:

### **PAPERS SPECIFICALLY FOR AGENTIC WORKLOADS**

1. **SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning**
   - **Date:** February 2026 (arXiv:2602.22603)
   - **Key Contribution:** Self-managed KV cache compression via the LRM itself. Allows models to selectively clear cache segments while performing parallel memory management as an auxiliary task. Reduces peak token usage by 65% on agentic tasks with minimal accuracy degradation.
   - **Approach:** Reasoning-based compression (model-driven garbage collection)

2. **CodeComp: Structural KV Cache Compression for Agentic Coding**
   - **Date:** April 2026 (arXiv:2604.10235)
   - **Key Contribution:** Training-free compression using Code Property Graph (CPG) priors from Joern. Addresses structural blind spot in attention-based methods by preserving semantically important tokens (callsites, branches, assignments). Implemented on SGLang.
   - **Approach:** Structure-aware eviction + budget allocation

3. **KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows**
   - **Date:** July 2025 (arXiv:2507.07400) - Published at Lifelong Agent Workshop @ ICLR 2026
   - **Key Contribution:** Workflow-aware KV cache management using Agent Step Graph abstraction. Assigns steps-to-execution values and implements workflow-aware eviction + KV prefetching. Achieves 1.83× speedup for single workflows, 2.19× for multi-workflow scenarios.
   - **Approach:** Workflow-aware eviction + predictive prefetching

4. **Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management** (PBKV)
   - **Date:** June 2026 (arXiv:2605.06472)
   - **Key Contribution:** Prediction-based KV-cache management for dynamic workflows. Predicts future agent invocations using historical workflows + context fusion. Hierarchical eviction + conservative prefetching. Reduces workflow latency by 1.39×.
   - **Approach:** Predictive workflow scheduling with hierarchical cache management

5. **Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices**
   - **Date:** March 2026 (arXiv:2603.04428)
   - **Key Contribution:** Persists each agent's KV cache to disk in 4-bit quantized format. Direct cache restoration eliminates redundant prefill computation. Enables multi-agent systems on edge devices.
   - **Approach:** Quantization + persistent storage for multi-agent systems

6. **CacheTTL: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV**
   - **Date:** November 2025 (arXiv:2511.02230)
   - **Key Contribution:** KV cache scheduling optimized for multi-turn agent interactions with intelligent TTL management.
   - **Approach:** Cache lifetime management for agent conversations

---

### **GENERAL-PURPOSE PAPERS (APPLICABLE TO AGENTIC WORKLOADS)**

7. **EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving**
   - **Date:** December 2025 (arXiv:2512.14946)
   - **Key Contribution:** **JOINT quantization-eviction approach** across multiple storage tiers. Adaptive compression policies based on compression sensitivity. Achieves 2.19× faster TTFT while preserving quality.
   - **Approach:** Joint optimization of lossy compression + adaptive eviction (THIS IS A DIRECT COMPETITOR FOR COMBINED QUANTIZATION-EVICTION)
   - **Affiliation:** Microsoft Research

8. **HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference**
   - **Date:** 2026 (OpenReview: sLG2XsjSDe)
   - **Key Contribution:** **HYBRID quantization-eviction framework** with joint K-V importance metric. Fine-grained compression options adapting to KV pair importance. Improves output quality from 40.53 to 49.98 under same memory constraints.
   - **Approach:** Joint hybrid compression-eviction with importance metrics (ANOTHER JOINT APPROACH)
   - **Code:** Available at https://github.com/skywclouds/HqeKV

9. **LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation**
   - **Date:** March 2026 (arXiv:2603.10899, ICLR 2026 Poster)
   - **Key Contribution:** Predictive eviction using lookahead tokens + LoRA modules. Predicts future attention patterns without draft generation. Reduces eviction cost by 14.5×, <0.7% perf drop at 81% compression.
   - **Approach:** Predictive token importance estimation
   - **Affiliation:** Samsung Labs

10. **Fast KV Compaction via Attention Matching**
    - **Date:** February 2026 (arXiv:2602.16284, MIT)
    - **Key Contribution:** Latent-space compaction achieving 50× memory reduction with minimal accuracy loss. Preserves attention output and attention mass. Compresses in seconds using fast algebraic approximations.
    - **Approach:** Attention-preserving compaction in latent space

11. **TriAttention: Efficient Long Reasoning with Trigonometric KV Compression**
    - **Date:** April 2026 (arXiv:2604.04921, MIT/NVIDIA/Zhejiang University)
    - **Key Contribution:** Reasoning-aware compression leveraging Q/K vector concentration in pre-RoPE space. On AIME25: 10.7× memory reduction at matched accuracy, 2.5× throughput improvement. 6.3× speedup on MATH 500.
    - **Approach:** Trigonometric importance scoring + position-based attention patterns
    - **Venue:** ICLR 2026

12. **LongFlow: Efficient KV Cache Compression for Reasoning Models**
    - **Date:** March 2026 (arXiv:2603.11504, OpenReview)
    - **Key Contribution:** Importance estimation derived from intermediate attention results for reasoning models (o1, DeepSeek-R1). 11.8× throughput improvement with 80% compression. Custom fused kernel.
    - **Approach:** Intermediate attention-based importance with hardware optimization

13. **KV Cache Transform Coding (KVTC) for Compact Storage in LLM Inference**
    - **Date:** February 2026 (arXiv:2511.01815, ICLR 2026 conference paper, NVIDIA)
    - **Key Contribution:** Transform coder pipeline: PCA decorrelation + adaptive quantization + entropy coding. Achieves 20× compression (up to 40×+ for specific cases). Tuning-free with <10 min calibration.
    - **Approach:** Classical media compression techniques applied to KV
    - **Code:** https://github.com/OnlyTerp/kvtc

14. **KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction**
    - **Date:** 2025/2026 (arXiv:2505.23416, NeurIPS 2025 Oral, ICML 2025)
    - **Key Contribution:** Query-agnostic eviction using context reconstruction to estimate token importance. 3-4× memory reduction, ~2× latency decrease. Works across diverse queries with reusable compressed caches.
    - **Approach:** Context reconstruction for importance estimation
    - **Code:** https://github.com/snu-mllab/KVzip

15. **TurboQuant: Training-free KV Cache Quantization**
    - **Date:** March 2026 (Google, ICLR 2026)
    - **Key Contribution:** Data-oblivious vector quantization to 3 bits per value. 6× memory reduction, up to 8× speedup on H100. Randomized Hadamard transform + QJL transform. No accuracy degradation on LongBench/NIAH.
    - **Approach:** Quantization-only (no joint eviction)

16. **Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution**
    - **Date:** October 2025 (arXiv:2510.00636)
    - **Key Contribution:** Predicts future attention distributions to estimate token importance for compression.
    - **Approach:** Future query prediction for importance estimation

---

### **KEY FINDINGS - CRITICAL GAPS & COMPETITORS**

**JOINT QUANTIZATION-EVICTION APPROACHES (Direct Competitors):**
- **EVICPRESS** (Microsoft Research, Dec 2025) - THE most mature joint approach, jointly optimizes compression + eviction across storage tiers
- **HqeKV** (2026) - Hybrid quantization-eviction with joint importance metrics

These two are the primary competitors specifically doing **joint optimization** of quantization and eviction decisions. Both claim superior quality-compression tradeoffs compared to single-method approaches.

**AGENTIC-SPECIFIC APPROACHES:**
1. **SideQuest** - Model-driven (reasoning-based) garbage collection
2. **CodeComp** - Structure-aware for code understanding tasks
3. **KVFlow** - Workflow-aware eviction + prefetching
4. **PBKV** - Dynamic workflow prediction
5. **CacheTTL** - Agent conversation scheduling

**REASONING-AWARE APPROACHES (High relevance for agentic workloads):**
- **TriAttention** - Position-based importance via Q/K concentration (AIME25 reasoning benchmark)
- **LongFlow** - Designed for o1/R1-style reasoning models

**PREDICTIVE/LOOKAHEAD APPROACHES:**
- **LookaheadKV** - Predicts future attention without draft generation
- **PBKV** - Predicts future agent invocations
- **Expected Attention** - Estimates from future query distributions

**WHAT'S NOT BEING JOINTLY OPTIMIZED (Gaps):**
- Most papers focus on either quantization OR eviction, not both
- EVICPRESS and HqeKV are exceptions, but neither is optimized specifically for agentic multi-step reasoning workloads
- No papers appear to jointly optimize quantization+eviction specifically for dynamic agent workflows (SideQuest does model-driven eviction but not quantization; CodeComp does eviction but not quantization)
- Limited work on combining predictive scheduling (like PBKV) with quantization strategies

**AGENTIC-SPECIFIC GAPS:**
- Most agentic papers (SideQuest, CodeComp, KVFlow) focus on eviction OR compression, not joint approaches
- PBKV + quantization combination unexplored
- No papers combining reasoning-aware compression (TriAttention) with agent workflow prediction

---

### **SOURCES**

- [SideQuest: Model-Driven KV Cache Management](https://arxiv.org/abs/2602.22603)
- [CodeComp: Structural KV Cache Compression for Agentic Coding](https://arxiv.org/abs/2604.10235)
- [KVFlow: Efficient Prefix Caching for Multi-Agent Workflows](https://arxiv.org/abs/2507.07400)
- [Efficient Serving for Dynamic Agent Workflows (PBKV)](https://arxiv.org/html/2605.06472v1)
- [Agent Memory Below the Prompt](https://arxiv.org/abs/2603.04428)
- [CacheTTL: Multi-Turn Agent Scheduling](https://arxiv.org/pdf/2511.02230)
- [EVICPRESS: Joint KV-Cache Compression and Eviction](https://arxiv.org/abs/2512.14946)
- [HqeKV: Hybrid Quantization and Eviction](https://openreview.net/forum?id=sLG2XsjSDe)
- [LookaheadKV: Predictive Eviction](https://arxiv.org/abs/2603.10899)
- [Fast KV Compaction via Attention Matching](https://arxiv.org/abs/2602.16284)
- [TriAttention: Efficient Long Reasoning](https://arxiv.org/abs/2604.04921)
- [LongFlow: Compression for Reasoning Models](https://arxiv.org/abs/2603.11504)
- [KV Cache Transform Coding (KVTC)](https://arxiv.org/abs/2511.01815)
- [KVzip: Query-Agnostic Compression](https://arxiv.org/abs/2505.23416)
- [Expected Attention: Future Query-based Compression](https://arxiv.org/html/2510.00636v1)
- [MarkTechPost: Top 10 KV Cache Compression Techniques](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)
- [Is KV Cache Quantization Sabotaging Your Context](https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/)
- [The KV Cache Wars Substack](https://kenhuangus.substack.com/p/the-kv-cache-wars)
- [Agentic Design KV Cache Optimization](https://agentic-design.ai/patterns/context-management/kv-cache-optimization)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c96e86e-b0a2-49d7-99fd-1fcc16a802e8",
  "isSidechain": true,
  "agentId": "aa9988d91ce776806",
  "requestId": "req_011CawfJGwKiVE4Qfm9XVzzH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b930549f-61d8-433a-9618-7c2040ec1f72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PhzPcpJD6UT32X35tympmR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2117,
      "cache_read_input_tokens": 33864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2117,
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
