# Research conversation: Search the web to verify these two papers exist and check their details: 1. "Neural Garbage Collection" (NGC) - arXiv:26

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a1def3fd557e01d90.jsonl`
- **Structured JSON:** [`52edb314ac1dde1930c3.json`](../../sessions/52/52edb314ac1dde1930c3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-12T01:43:21.832Z_

Search the web to verify these two papers exist and check their details:

1. "Neural Garbage Collection" (NGC) - arXiv:2604.18002, April 2026 - claims to learn trajectory-aware KV eviction via RL within single-model reasoning chains. Check: does it exist? What exactly does it do? Is it eviction-only? Does it require RL training?

2. "CapKV" - arXiv:2604.25975 - claims to use Information Bottleneck principle for KV cache eviction with capacity-aware scoring. Check: does it exist? What exactly does it do?

3. Also search for any NEW KV cache compression papers from April-May 2026 that might be competitors to a "trajectory-aware joint quantization-eviction for agentic KV caches" method. Search: "KV cache compression agentic 2026", "KV cache agent workflow compression 2026", "trajectory KV cache 2026"

Use WebSearch for searches and WebFetch to read key paper abstracts. Report exact findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "79f26ec2-924c-4e56-baf9-f6e0c1807591",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T01:43:21.837Z_

```json
{
  "parentUuid": "79f26ec2-924c-4e56-baf9-f6e0c1807591",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
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
  "uuid": "3c3f770b-5134-4c3d-b0ba-dab2ffc2472b",
  "timestamp": "2026-05-12T01:43:21.837Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T01:43:24.884Z_



I'll start by loading the WebSearch and WebFetch tools, then conduct the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c3f770b-5134-4c3d-b0ba-dab2ffc2472b",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpuGkw3sihaQSCzrLu2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8018b1d8-5d9b-4e60-80ed-a1386d10a61f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZLDECySNdSQxtvRTK9TTg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 797,
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

_source line 4 · 2026-05-12T01:43:25.057Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YbXmdRW8jHUQxYes1F6Ptg`</summary>

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
  "parentUuid": "8018b1d8-5d9b-4e60-80ed-a1386d10a61f",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpuGkw3sihaQSCzrLu2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06528803-7026-4703-8b8e-e5935e7337f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZLDECySNdSQxtvRTK9TTg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 8223,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 797
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 797,
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

_source line 5 · 2026-05-12T01:43:25.062Z_

<details><summary>↩ Tool result · `toolu_01YbXmdRW8jHUQxYes1F6Ptg`</summary>

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
  "parentUuid": "06528803-7026-4703-8b8e-e5935e7337f0",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "e4631721-f40e-46d0-a61e-e07f4f455066",
  "sourceToolAssistantUUID": "06528803-7026-4703-8b8e-e5935e7337f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T01:43:27.679Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4631721-f40e-46d0-a61e-e07f4f455066",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpuWwiF9Ci7AafbaCjc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b2fe603-33a1-464c-824a-243b23fdae0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sTfxnzoPfR1XWM4G2qXNX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 7 · 2026-05-12T01:43:28.225Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F4SWko6JtMqbqjXc6GCjJB`</summary>

```json
{
  "query": "arXiv 2604.18002 Neural Garbage Collection KV cache"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b2fe603-33a1-464c-824a-243b23fdae0e",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpuWwiF9Ci7AafbaCjc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28ccd022-7905-497a-8d84-851794d90d82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sTfxnzoPfR1XWM4G2qXNX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 8 · 2026-05-12T01:43:29.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TbDESxwBaRRRbnwdeSeRBm`</summary>

```json
{
  "query": "arXiv 2604.25975 CapKV information bottleneck KV cache"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28ccd022-7905-497a-8d84-851794d90d82",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpuWwiF9Ci7AafbaCjc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1506c44b-f753-4982-ab4c-863648fe781d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sTfxnzoPfR1XWM4G2qXNX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 9 · 2026-05-12T01:43:29.634Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HSM6XEjxWB9pUjLfn5g2Vc`</summary>

```json
{
  "query": "KV cache compression agentic 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1506c44b-f753-4982-ab4c-863648fe781d",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpuWwiF9Ci7AafbaCjc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84c6b76e-319f-45a6-aa8e-028b11fedd06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sTfxnzoPfR1XWM4G2qXNX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 10 · 2026-05-12T01:43:30.106Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0188LtsTDbqP7iGrizFDZ5N4`</summary>

```json
{
  "query": "KV cache agent workflow compression 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84c6b76e-319f-45a6-aa8e-028b11fedd06",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpuWwiF9Ci7AafbaCjc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3efbed0a-0ebc-40d7-9332-917c35de7716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sTfxnzoPfR1XWM4G2qXNX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 11 · 2026-05-12T01:43:30.508Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JjuvQ2va2fqJ2jeKk5fmgE`</summary>

```json
{
  "query": "trajectory KV cache 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3efbed0a-0ebc-40d7-9332-917c35de7716",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpuWwiF9Ci7AafbaCjc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "283f1f4b-008c-49c2-a5a5-eb0e5a41899f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sTfxnzoPfR1XWM4G2qXNX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9020,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 263,
          "cache_read_input_tokens": 9020,
          "cache_creation_input_tokens": 1909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1909,
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

_source line 12 · 2026-05-12T01:43:36.373Z_

<details><summary>↩ Tool result · `toolu_01TbDESxwBaRRRbnwdeSeRBm`</summary>

```text
Web search results for query: "arXiv 2604.25975 CapKV information bottleneck KV cache"

Links: [{"title":"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/html/2604.25975"},{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"},{"title":"[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/abs/2605.06675"},{"title":"KV Cache Offloading for Context-Intensive Tasks","url":"https://arxiv.org/html/2604.08426"},{"title":"Stochastic KV Routing: Enabling Adaptive Depth-Wise Cache Sharing","url":"https://arxiv.org/html/2604.22782"},{"title":"DepthKV: Layer-Dependent KV Cache Pruning for Long-Context LLM Inference","url":"https://arxiv.org/html/2604.24647"},{"title":"TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference","url":"https://arxiv.org/html/2604.19769"},{"title":"Predictive Multi-Tier Memory Management for KV Cache in Large-Scale GPU Inference","url":"https://arxiv.org/html/2604.26968"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/html/2604.10235"}]

Based on the search results, I found the paper you're looking for. Here's an overview of arXiv:2604.25975:

## Title and Authors
"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective" by Jiaming Yang, Chenwei Tang, Liangli Zhen, and Jiancheng Lv (posted April 28, 2026)

## Main Problem
Key-value (KV) caching is essential for large language model inference, yet its memory overhead poses a critical bottleneck for long-context generation.

## Key Contributions
The paper addresses KV cache eviction through information theory. The work rethinks KV cache eviction through the lens of the Information Bottleneck principle. Under a linear-Gaussian surrogate of attention, the authors derive a closed-form mutual information objective that characterizes the effective information capacity of a retained KV cache subset.

## CapKV Method
The authors introduce CapKV, a capacity-aware eviction method that directly targets information preservation via a log-determinant approximation using statistical leverage scores. This approach replaces heuristic selection with a theoretically grounded mechanism that preserves the maximum predictive signal.

## Results
Extensive experiments across multiple models and long-context benchmarks show that CapKV consistently outperforms prior methods, achieving a better trade-off between memory efficiency and generational fidelity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1506c44b-f753-4982-ab4c-863648fe781d",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "a582c7dc-0a6c-4a55-9bd1-5e4c30a1b1a0",
  "sourceToolAssistantUUID": "1506c44b-f753-4982-ab4c-863648fe781d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T01:43:38.166Z_

<details><summary>↩ Tool result · `toolu_01JjuvQ2va2fqJ2jeKk5fmgE`</summary>

```text
Web search results for query: "trajectory KV cache 2026"

Links: [{"title":"TurboQuant KV Cache Compression: What Changes for LLM Inference","url":"https://www.kriraai.com/blog/turboquant-kv-cache-compression-changes-llm-inference"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"TurboQuant: Google’s 6x KV Cache Compression for LLMs | byteiota","url":"https://byteiota.com/turboquant-googles-6x-kv-cache-compression-for-llms/"},{"title":"Nvidia and its partners' KV Cache extenders","url":"https://www.blocksandfiles.com/ai-ml/2026/03/30/nvidia-and-its-partners-kv-cache-extenders/5209284"},{"title":"Modular: The Five Eras of KVCache","url":"https://www.modular.com/blog/the-five-eras-of-kvcache"},{"title":"KV Cache, Made Visible: Qwen3-0.6B on Apple Silicon | Rick Lamers' blog","url":"https://ricklamers.io/posts/kvcache-exploration/"},{"title":"Google TurboQuant: Technical Analysis of 6x KV Cache Compression | Tech Bytes","url":"https://techbytes.app/posts/google-turboquant-llm-memory-compression-breakthrough/"},{"title":"Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING","url":"https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"},{"title":"What is KV Cache? Efficient LLM Inference | Ultralytics","url":"https://www.ultralytics.com/glossary/kv-cache"},{"title":"TurboQuant - Extreme KV Cache Quantization · ggml-org/llama.cpp · Discussion #20969","url":"https://github.com/ggml-org/llama.cpp/discussions/20969"}]

Based on the search results, here's what I found about trajectory KV cache in 2026:

## Key Developments

2026 marks a significant shift in AI development toward "same performance, less resources," with infrastructure costs rising despite GPU prices dropping, making inference optimization a competitive necessity.

### TurboQuant - Google's Major Innovation

On March 25, 2026, Google Research published TurboQuant, which prompted significant market reactions including Cloudflare CEO Matthew Prince calling it Google's DeepSeek moment. TurboQuant compresses the KV cache of large language models to 3 bits per value, achieving a 6x reduction in KV cache memory and up to 8x speedup on NVIDIA H100 GPUs without measurable accuracy degradation.

### Context Length Trajectory

Context windows have expanded from 128k tokens in 2024 to 5M+ tokens in 2026, with the KV cache growing to consume more memory than model weights themselves.

### Production Timeline

The realistic production-ready window for major inference frameworks to integrate TurboQuant is Q3 to Q4 2026, with Google's Q2 2026 official code release expected.

### Infrastructure Response

Announced at CES 2026, ICMSP (Inference Context Memory Storage Platform) extended GPU KV cache into NVMe-based storage with a 4-tier hierarchy.

The trajectory shows a clear evolution from scaling models at any cost to optimizing inference efficiency, with KV cache compression becoming central to deployment economics in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "283f1f4b-008c-49c2-a5a5-eb0e5a41899f",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "be17742a-8155-4c7f-b988-bb011ff4335a",
  "sourceToolAssistantUUID": "283f1f4b-008c-49c2-a5a5-eb0e5a41899f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T01:43:38.494Z_

<details><summary>↩ Tool result · `toolu_01HSM6XEjxWB9pUjLfn5g2Vc`</summary>

```text
Web search results for query: "KV cache compression agentic 2026"

Links: [{"title":"[2604.10235] CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/abs/2604.10235"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/html/2604.10235"},{"title":"Google’s TurboQuant Compression May Support Faster Inference, Same Accuracy on Less Capable Hardware - InfoQ","url":"https://www.infoq.com/news/2026/04/turboquant-compression-kv-cache/"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"TurboQuant KV Cache Compression: What Changes for LLM Inference","url":"https://www.kriraai.com/blog/turboquant-kv-cache-compression-changes-llm-inference"},{"title":"Researchers from MIT, NVIDIA, and Zhejiang University Propose TriAttention: A KV Cache Compression Method That Matches Full Attention at 2.5× Higher Throughput - MarkTechPost","url":"https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/"},{"title":"Google's new TurboQuant algorithm speeds up AI memory 8x, cutting costs by 50% or more | VentureBeat","url":"https://venturebeat.com/infrastructure/googles-new-turboquant-algorithm-speeds-up-ai-memory-8x-cutting-costs-by-50"},{"title":"The KV Cache Wars? - by Ken Huang - Agentic AI - Substack","url":"https://kenhuangus.substack.com/p/the-kv-cache-wars"}]

Based on the search results, here's what I found about KV cache compression and agentic AI in 2026:

## Key Developments in 2026

**CodeComp - Structural KV Cache Compression for Agentic Coding**

CodeComp is a training-free KV cache compression framework that incorporates static program analysis into LLM inference via Code Property Graph priors extracted by Joern. CodeComp consistently outperforms attention-only compression baselines under equal memory budgets, recovering the majority of full-context accuracy under aggressive KV cache compression, while integrating seamlessly into SGLang-based agentic coding pipelines without model modification.

**TurboQuant - Google's Quantization Breakthrough**

Google Research unveiled TurboQuant, a novel quantization algorithm that compresses large language models' Key-Value caches by up to 6x, with 3.5-bit compression, near-zero accuracy loss, and no retraining needed. In testing across open-source models like Llama-3.1-8B and Mistral-7B, TurboQuant achieved perfect recall scores, mirroring the performance of uncompressed models while reducing the KV cache memory footprint by a factor of at least 6x.

**TriAttention - Reasoning-Aware Compression**

The 2026 research frontier is moving toward latent-space compaction (Attention Matching, 50× compaction) and reasoning-aware compression (TriAttention, 10.7× memory reduction on AIME25 at matched accuracy).

## Broader Context

By releasing these methodologies under an open research framework, Google is providing the essential "plumbing" for the burgeoning "Agentic AI" era: the need for massive, efficient, and searchable vectorized memory that can finally run on the hardware users already own.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84c6b76e-319f-45a6-aa8e-028b11fedd06",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "140d41d2-1c9d-4c6e-bf31-ec6d5c1cbacd",
  "sourceToolAssistantUUID": "84c6b76e-319f-45a6-aa8e-028b11fedd06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T01:43:40.612Z_

<details><summary>↩ Tool result · `toolu_0188LtsTDbqP7iGrizFDZ5N4`</summary>

```text
Web search results for query: "KV cache agent workflow compression 2026"

Links: [{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"Google’s TurboQuant Compression May Support Faster Inference, Same Accuracy on Less Capable Hardware - InfoQ","url":"https://www.infoq.com/news/2026/04/turboquant-compression-kv-cache/"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"🔥 Introducing TriAttention: A New KV Cache Compression Technique | by Mayur Jain | MLWorks | Apr, 2026 | Medium","url":"https://medium.com/mlworks/introducing-triattention-a-new-kv-cache-compression-technique-60d1215f5af2"},{"title":"What Is Google TurboQuant? The KV Cache Compression That Crashed Memory Chip Stocks | MindStudio","url":"https://www.mindstudio.ai/blog/what-is-google-turboquant-kv-cache-compression"},{"title":"Compress the KV Cache with TurboQuant and Haystack | Haystack","url":"https://haystack.deepset.ai/tutorials/49_turboquant_quantization_with_huggingface"},{"title":"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/html/2603.04428v1"},{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | OpenReview","url":"https://openreview.net/forum?id=JFygzwx8SJ"},{"title":"New KV cache compaction technique cuts LLM memory 50x without accuracy loss | VentureBeat","url":"https://venturebeat.com/orchestration/new-kv-cache-compaction-technique-cuts-llm-memory-50x-without-accuracy-loss"}]

Based on the search results, here's what's current in KV cache compression and agent workflows in 2026:

## Key Compression Techniques

Google's TurboQuant, accepted at ICLR 2026, represents a major advancement. TurboQuant is a KV cache quantization algorithm that compresses cache storage from 16 bits to 3 bits with minimal accuracy loss, achieving 8x faster inference and 6x memory reduction on H100 GPUs. It works in two stages: PolarQuant applies random orthogonal rotation to cache vectors, then QJL (Quantized Johnson-Lindenstrauss) adds a single extra bit per vector to correct residual errors in attention score computation.

## Agent Workflow Optimization

On agent loops, multi-tenant SaaS, repo Q&A, and long-doc workflows, hit-rates of 60-85% are achievable with prefix caching, dropping per-call cost by 5-12×. DeepSeek's Multi-head Latent Attention (MLA) compresses KV cache 7-14× by storing a low-rank projection instead of full keys and values, while competing models are still on GQA at 4-8× compression.

## Advanced Methods for Long-Horizon Tasks

As of 2026, the most recent methodologies leverage specialized tools such as TurboQuant, VQKV, and Quant VideoGen (QVG), which are designed to compress KV caches while maintaining fidelity in long-horizon agentic workloads. The 2026 research frontier is moving toward latent-space compaction (Attention Matching, 50× compaction) and reasoning-aware compression (TriAttention, 10.7× memory reduction on AIME25 at matched accuracy).

Workflows involving long documents, multi-step reasoning chains, or high-volume batch processing benefit directly from these efficiency gains, making document-heavy workflows and agents that reason across large context windows more cost-effective.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3efbed0a-0ebc-40d7-9332-917c35de7716",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "66f68ef1-c4c9-407b-941b-70f57f496493",
  "sourceToolAssistantUUID": "3efbed0a-0ebc-40d7-9332-917c35de7716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T01:43:40.930Z_

<details><summary>↩ Tool result · `toolu_01F4SWko6JtMqbqjXc6GCjJB`</summary>

```text
Web search results for query: "arXiv 2604.18002 Neural Garbage Collection KV cache"

Links: [{"title":"[2604.18002] Neural Garbage Collection: Learning to Forget while Learning to Reason","url":"https://arxiv.org/abs/2604.18002"},{"title":"Neural Garbage Collection: Learning to Forget while Learning to Reason","url":"https://arxiv.org/pdf/2604.18002"},{"title":"Neural Garbage Collection: Efficient LM Memory Management","url":"https://www.emergentmind.com/papers/2604.18002"},{"title":"Neural Garbage Collection: Learning to Forget while Learning to Reason | alphaXiv","url":"https://www.alphaxiv.org/abs/2604.18002"},{"title":"[Paper Note] Neural Garbage Collection: Learning to Forget while Learning to Reason, Michael Y. Li+, arXiv'26, 2026.04 · Issue #5306 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/5306"},{"title":"Neural Garbage Collection: Learning to Forget while Learning to Reason","url":"https://www.researchgate.net/publication/404022150_Neural_Garbage_Collection_Learning_to_Forget_while_Learning_to_Reason"},{"title":"Neural Garbage Collection: Learning to Forget while Learning to Reason","url":"https://www.wispaper.ai/en/blog/neural-garbage-collection-learning-to-forget-while-learning-to-reason-20260421/eng"},{"title":"Machine Learning (ML) Papers on X: \"Neural Garbage Collection: Learning to Forget while Learning to Reason Michael Y. Li, Jubayer Ibn Hamid, Emily B. Fox, Noah D. Goodman https://t.co/xrsV9oGiY2 [𝚌𝚜.𝙻𝙶] https://t.co/I3uaAY2kUS\" / X","url":"https://x.com/Memoirs/status/2046686365379702932"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"DumpKV: Learning based lifetime aware garbage collection for key value separation in LSM-tree","url":"https://arxiv.org/html/2406.01250v1"}]

Based on the search results, here's what I found about arXiv paper 2604.18002:

## Neural Garbage Collection: Learning to Forget while Learning to Reason

Neural Garbage Collection (NGC) is a framework in which a language model learns to forget while learning to reason, trained end-to-end from outcome-based task reward alone.

### The Problem
Chain-of-thought reasoning has driven striking advances in language model capability, yet every reasoning step grows the KV cache, creating a bottleneck to scaling this paradigm further.

### How NGC Works
As the model reasons, it periodically pauses, decides which KV cache entries to evict, and continues to reason conditioned on the remaining cache. More specifically, the model uses its internal attention mechanism to score all current KV blocks, samples a subset of blocks to keep and permanently deletes the rest, and then continues reasoning conditioned only on the remaining "pruned" cache.

### Key Technical Approach
By treating tokens in a chain-of-thought and cache-eviction decisions as discrete actions sampled from the language model, reinforcement learning is used to jointly optimize how the model reasons and how it manages cache.

### Results
NGC achieves 2-5x compression in peak KV cache size while maintaining high accuracy on reasoning tasks like Countdown and math competitions (AMC/AIME).

### Authors
The paper was submitted on April 20, 2026, with authors Michael Y. Li, Jubayer Ibn Hamid, Emily B. Fox, and Noah D. Goodman.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28ccd022-7905-497a-8d84-851794d90d82",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "ad18f558-171f-49c8-94a1-414b3dd41ecb",
  "sourceToolAssistantUUID": "28ccd022-7905-497a-8d84-851794d90d82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-12T01:43:44.111Z_

Good, I found both papers. Let me now fetch the actual arXiv abstracts for precise details, plus look at some of the interesting competitor papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad18f558-171f-49c8-94a1-414b3dd41ecb",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpvgvmEL7WU7ea6QddE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e697cc9-e0f9-43b2-82a6-27311f3a7ab2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017S5FWWeXiYkD9pVYB9efon",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4147,
      "cache_creation_input_tokens": 1264,
      "cache_read_input_tokens": 10929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1264,
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

_source line 18 · 2026-05-12T01:43:46.565Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JGyJQXGz4jSXiPrH1s4ZYJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.18002",
  "prompt": "Extract the full abstract, authors, submission date, and exact title. What exactly does the method do? Is it eviction-only or does it also do quantization? Does it require RL training? What tasks/benchmarks is it evaluated on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e697cc9-e0f9-43b2-82a6-27311f3a7ab2",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpvgvmEL7WU7ea6QddE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c43b93f-2122-433c-bd7d-022f47363ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017S5FWWeXiYkD9pVYB9efon",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4147,
      "cache_creation_input_tokens": 1264,
      "cache_read_input_tokens": 10929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1264,
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

_source line 19 · 2026-05-12T01:43:48.391Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014RWoy48bBCZdofTgccNeyz`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.25975",
  "prompt": "Extract the full abstract, authors, submission date, and exact title. What exactly does the method do? Does it use the Information Bottleneck principle? What is CapKV specifically? Is it eviction-only or does it do quantization too?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c43b93f-2122-433c-bd7d-022f47363ca1",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpvgvmEL7WU7ea6QddE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2122ff6-de95-4df0-93d9-abeac9ab2be2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017S5FWWeXiYkD9pVYB9efon",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4147,
      "cache_creation_input_tokens": 1264,
      "cache_read_input_tokens": 10929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1264,
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

_source line 20 · 2026-05-12T01:43:49.917Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017D4N9Jx6VCpVo5GYPqKmEm`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.10235",
  "prompt": "Extract the full abstract, authors, submission date, and exact title. What is CodeComp? Does it deal with agentic workflows? Is it eviction, quantization, or both? What is the key novelty?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2122ff6-de95-4df0-93d9-abeac9ab2be2",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpvgvmEL7WU7ea6QddE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2d8a074-c713-4b9a-8355-7fabe3dd274d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017S5FWWeXiYkD9pVYB9efon",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4147,
      "cache_creation_input_tokens": 1264,
      "cache_read_input_tokens": 10929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1264,
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

_source line 21 · 2026-05-12T01:43:50.293Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EFpFZycToQT69KUAiTMtXZ`</summary>

```json
{
  "query": "KV cache quantization eviction joint 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2d8a074-c713-4b9a-8355-7fabe3dd274d",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpvgvmEL7WU7ea6QddE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27acd40c-6e30-4839-855d-d759022b28b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017S5FWWeXiYkD9pVYB9efon",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4147,
      "cache_creation_input_tokens": 1264,
      "cache_read_input_tokens": 10929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1264,
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

_source line 22 · 2026-05-12T01:43:50.694Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V6rhCGgGaq5ASw7x16E1bu`</summary>

```json
{
  "query": "arXiv 2605.06675 RateQuant mixed-precision KV cache quantization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27acd40c-6e30-4839-855d-d759022b28b2",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpvgvmEL7WU7ea6QddE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0baac205-8dcc-4c0e-af0f-73eb9c38738a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017S5FWWeXiYkD9pVYB9efon",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4147,
      "cache_creation_input_tokens": 1264,
      "cache_read_input_tokens": 10929,
      "output_tokens": 503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1264
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4147,
          "output_tokens": 503,
          "cache_read_input_tokens": 10929,
          "cache_creation_input_tokens": 1264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1264,
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

_source line 23 · 2026-05-12T01:43:54.075Z_

<details><summary>↩ Tool result · `toolu_014RWoy48bBCZdofTgccNeyz`</summary>

```text
# Paper Summary: KV Cache Eviction via Information-Theoretic Objective

## Full Abstract
"Key-value (KV) caching is essential for large language model inference, yet its memory overhead poses a critical bottleneck for long-context generation. Existing eviction policies predominantly rely on empirical heuristics, lacking a rigorous theoretical foundation. This work rethinks KV cache eviction through the lens of the Information Bottleneck principle. Under a linear-Gaussian surrogate of attention, we derive a closed-form mutual information objective that characterizes the effective information capacity of a retained KV cache subset. This formulation reveals that a wide range of existing eviction strategies can be interpreted as different approximations of the same capacity-maximization principle. Guided by this insight, we introduce CapKV, a capacity-aware eviction method that directly targets information preservation via a log-determinant approximation using statistical leverage scores. This approach replaces heuristic selection with a theoretically grounded mechanism that preserves the maximum predictive signal. Extensive experiments across multiple models and long-context benchmarks show that CapKV consistently outperforms prior methods, achieving a better trade-off between memory efficiency and generational fidelity."

## Key Details

**Authors:** Jiaming Yang, Chenwei Tang, Liangli Zhen, Jiancheng Lv

**Submission Date:** 28 April 2026

**Exact Title:** "Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective"

## Method Overview

Yes, the work explicitly uses the Information Bottleneck principle. **CapKV** is specifically an eviction-only method that uses statistical leverage scores and log-determinant approximations to identify which cache entries to remove. It addresses memory constraints through selective deletion rather than quantization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2122ff6-de95-4df0-93d9-abeac9ab2be2",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "ee971a51-6b98-4efe-a4be-7fb68b4a8f91",
  "sourceToolAssistantUUID": "a2122ff6-de95-4df0-93d9-abeac9ab2be2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T01:43:55.403Z_

<details><summary>↩ Tool result · `toolu_01JGyJQXGz4jSXiPrH1s4ZYJ`</summary>

```text
# Neural Garbage Collection: Paper Summary

**Title:** "Neural Garbage Collection: Learning to Forget while Learning to Reason"

**Authors:** Michael Y. Li, Jubayer Ibn Hamid, Emily B. Fox, Noah D. Goodman

**Submission Date:** April 20, 2026

**Full Abstract:**
"Chain-of-thought reasoning has driven striking advances in language model capability, yet every reasoning step grows the KV cache, creating a bottleneck to scaling this paradigm further. Current approaches manage these constraints on the model's behalf using hand-designed criteria. A more scalable approach would let end-to-end learning subsume this design choice entirely, following a broader pattern in deep learning. After all, if a model can learn to reason, why can't it learn to forget? We introduce Neural Garbage Collection (NGC), in which a language model learns to forget while learning to reason, trained end-to-end from outcome-based task reward alone. As the model reasons, it periodically pauses, decides which KV cache entries to evict, and continues to reason conditioned on the remaining cache. By treating tokens in a chain-of-thought and cache-eviction decisions as discrete actions sampled from the language model, we can use reinforcement learning to jointly optimize how the model reasons and how it manages its own memory: what the model evicts shapes what it remembers, what it remembers shapes its reasoning, and the correctness of that reasoning determines its reward. Crucially, the model learns this behavior entirely from a single learning signal - the outcome-based task reward - without supervised fine-tuning or proxy objectives. On Countdown, AMC, and AIME tasks, NGC maintains strong accuracy relative to the full-cache upper bound at 2-3x peak KV cache size compression and substantially outperforms eviction baselines. Our results are a first step towards a broader vision where end-to-end optimization drives both capability and efficiency in language models."

---

## Key Details

**Method Type:** Eviction-only (not quantization). The approach focuses on deciding which KV cache entries to remove.

**Training Approach:** Yes, it requires RL training. The model uses reinforcement learning to jointly optimize reasoning and memory management based on outcome-based task rewards.

**Benchmarks:** Countdown, AMC, and AIME tasks

**Performance:** Achieves 2-3x peak KV cache compression while maintaining strong accuracy compared to full-cache baselines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c43b93f-2122-433c-bd7d-022f47363ca1",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "cf69ed40-0d26-4a86-8b98-6b0166dafa36",
  "sourceToolAssistantUUID": "0c43b93f-2122-433c-bd7d-022f47363ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-12T01:43:56.496Z_

<details><summary>↩ Tool result · `toolu_017D4N9Jx6VCpVo5GYPqKmEm`</summary>

```text
# CodeComp: Structural KV Cache Compression for Agentic Coding

## Full Abstract
"Agentic code tasks such as fault localization and patch generation require processing long codebases under tight memory constraints, where the Key-Value (KV) cache becomes the primary inference bottleneck. Existing compression methods rely exclusively on attention signals to estimate token importance, systematically discarding structurally critical tokens such as call sites, branch conditions, and assignments that are essential for code understanding. We present CodeComp, a training-free KV cache compression framework that incorporates static program analysis into LLM inference via Code Property Graph priors extracted by Joern. Across bug localization and code generation benchmarks, CodeComp consistently outperforms attention-only compression baselines under equal memory budgets, recovering the majority of full-context accuracy under aggressive KV cache compression, while matching the patch generation quality of uncompressed full-context inference and integrating seamlessly into SGLang-based agentic coding pipelines without model modification."

## Authors
Qiujiang Chen, Jing Xiong, Chenyang Zhao, Sidi Yang, Ngai Wong

## Submission Date
April 11, 2026

## Exact Title
"CodeComp: Structural KV Cache Compression for Agentic Coding"

## Analysis

**What is CodeComp?**
A training-free framework that reduces memory demands during language model inference by identifying and preserving structurally important code tokens.

**Agentic Workflows?**
Yes—it explicitly integrates with "SGLang-based agentic coding pipelines" for tasks like debugging and patch generation.

**Compression Type?**
Eviction (token selection). It strategically discards less important tokens rather than reducing precision through quantization.

**Key Novelty?**
Unlike prior methods relying solely on attention patterns, CodeComp incorporates static program analysis via Code Property Graphs to recognize code-specific structural elements—function calls, conditionals, variable assignments—as essential preservation targets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2d8a074-c713-4b9a-8355-7fabe3dd274d",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "af8a1cc5-ede4-420b-86d9-f5812caf4a7d",
  "sourceToolAssistantUUID": "d2d8a074-c713-4b9a-8355-7fabe3dd274d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T01:43:58.821Z_

<details><summary>↩ Tool result · `toolu_01EFpFZycToQT69KUAiTMtXZ`</summary>

```text
Web search results for query: "KV cache quantization eviction joint 2026 arXiv"

Links: [{"title":"HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=sLG2XsjSDe"},{"title":"randomization boosts kv caching, learning balances query ...","url":"https://arxiv.org/pdf/2601.18999"},{"title":"Mixed-Dimension Budget Allocation for Efficient KV Cache ...","url":"https://arxiv.org/pdf/2603.20616"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences","url":"https://arxiv.org/html/2503.12491v2"},{"title":"VQKV: High-Fidelity and High-Ratio Cache Compression via Vector-Quantization","url":"https://arxiv.org/html/2603.16435"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"EvicPress: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/html/2512.14946"},{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"}]

Based on the search results, I found several highly relevant papers on KV cache quantization and eviction from 2026 and recent arXiv submissions:

## Key Papers Found:

**1. HqeKV: Hybrid Quantization and Eviction for KV Cache**
HqeKV is a hybrid compression framework built on both quantization and eviction, offering finer-grained compression options that adapt smoothly to the varying importance of cached KV pairs. The framework includes a joint K–V importance metric to provide more accurate importance assessment results so that the optimizer can make smarter decisions. Extensive experiments show that HqeKV improves output quality from 40.53 to 49.98 under the same memory constraints, outperforming state-of-the-art alternatives.

**2. EvicPress: Joint KV-Cache Compression and Eviction**
EvicPress is a KV-cache management system that applies lossy compression and adaptive eviction to KV cache across multiple storage tiers, considering the effect of compression and eviction of the KV cache on the average generation quality and delay across all contexts as a whole. Evaluation on 12 datasets and 5 models demonstrates that EvicPress achieves up to 2.19 × faster time-to-first-token (TTFT) at equivalent generation quality.

**3. VQKV: Vector Quantization for KV Cache Compression**
VQKV is a training-free KV cache compression framework that leverages vector quantization to jointly capture correlations within cache vectors, achieving high compression ratios while preserving fidelity by replacing continuous representations with compact discrete codes.

**4. CAKE: Cascading and Adaptive KV Cache Eviction**
When combining KIVI-INT4 with CAKE, the combined approach maintains strong performance at aggressive compression ratios, showing the effectiveness of integrating eviction and quantization strategies.

These papers represent the current state-of-the-art in jointly optimizing KV cache quantization and eviction strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27acd40c-6e30-4839-855d-d759022b28b2",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "9d7bcf9f-6e09-418d-9690-8411d5f3cb09",
  "sourceToolAssistantUUID": "27acd40c-6e30-4839-855d-d759022b28b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T01:43:59.083Z_

<details><summary>↩ Tool result · `toolu_01V6rhCGgGaq5ASw7x16E1bu`</summary>

```text
Web search results for query: "arXiv 2605.06675 RateQuant mixed-precision KV cache quantization"

Links: [{"title":"[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/abs/2605.06675"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/new"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.18643"},{"title":"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning","url":"https://arxiv.org/html/2512.19206v1"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | OpenReview","url":"https://openreview.net/forum?id=Vem6FQvRvq"},{"title":"[2605.02262v1] WindowQuant: Mixed-Precision KV Cache Quantization based on Window-Level Similarity for VLMs Inference Optimization","url":"https://arxiv.org/abs/2605.02262v1"},{"title":"for Keys, Less for Values: Adaptive KV Cache Quantization","url":"https://arxiv.org/html/2502.15075"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/new"},{"title":"[2605.02262] WindowQuant: Mixed-Precision KV Cache Quantization based on Window-Level Similarity for VLMs Inference Optimization","url":"https://arxiv.org/abs/2605.02262"}]

I found the paper for you! Here are the key details about arXiv 2605.06675:

**Title:** RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory

**Authors:** Fei Zuo, Zikang Zhou, Hao Cong, Xiaoyan Xi, Ho Fai Leung

**Submission Date:** 22 Apr 2026

**Core Problem:** Large language models cache all previously computed key-value (KV) pairs during generation, and this KV cache grows linearly with sequence length, making it a primary memory bottleneck for serving. While quantizing the KV cache to fewer bits reduces this cost, current quantizers assign the same bit-width to every attention head, ignoring the large variation in head importance.

**Key Innovation:** Each quantizer follows a different distortion curve, and the decay rate beta varies from 3.6 to 5.3 across quantizer designs. Applying one quantizer's distortion model to another inverts the allocation order and makes performance worse than uniform quantization. The paper calls this failure mode distortion model mismatch and proposes RateQuant to resolve it.

**Solution:** RateQuant fits a per-quantizer distortion model from a small calibration set, then solves the resulting bit-allocation problem in closed form via reverse waterfilling from rate-distortion theory.

**Results:** On Qwen3-8B at 2.5 average bits, calibrated RateQuant reduces KIVI's perplexity from 49.3 to 14.9 (70% reduction) and improves QuaRot by 6.6 PPL. The entire calibration takes 1.6 s on a single GPU and adds zero overhead at inference time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0baac205-8dcc-4c0e-af0f-73eb9c38738a",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "5b7fe537-bea3-4e30-aaa4-2b0ed3dedda2",
  "sourceToolAssistantUUID": "0baac205-8dcc-4c0e-af0f-73eb9c38738a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-12T01:44:02.471Z_

Let me fetch a few more potentially relevant competitor papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b7fe537-bea3-4e30-aaa4-2b0ed3dedda2",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011Cawpx1ymNumvCJNvd9ama",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "650c717d-1f92-48fa-bc4c-9a467c649c4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMByb7jZDW1rMAGEvhHPQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8126,
      "cache_read_input_tokens": 12193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8126,
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

_source line 29 · 2026-05-12T01:44:04.972Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YC14ZmsSevFQqd7quVhDd8`</summary>

```json
{
  "url": "https://openreview.net/forum?id=sLG2XsjSDe",
  "prompt": "Extract the title, authors, abstract, and venue of HqeKV. What does it do? Does it jointly do quantization and eviction? Is it trajectory-aware or agentic? When was it published?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "650c717d-1f92-48fa-bc4c-9a467c649c4e",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011Cawpx1ymNumvCJNvd9ama",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "543c6c7b-4950-44c5-8bb0-dee93667b473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMByb7jZDW1rMAGEvhHPQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8126,
      "cache_read_input_tokens": 12193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8126,
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

_source line 30 · 2026-05-12T01:44:05.754Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KEhvNPYYtr4wqAYXRZXBai`</summary>

```json
{
  "query": "\"KV cache\" \"multi-turn\" OR \"multi-step\" OR \"agentic\" compression eviction quantization 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "543c6c7b-4950-44c5-8bb0-dee93667b473",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011Cawpx1ymNumvCJNvd9ama",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09c21ba5-7c99-4579-ae17-3f2841e516db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMByb7jZDW1rMAGEvhHPQu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8126,
      "cache_read_input_tokens": 12193,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 12193,
          "cache_creation_input_tokens": 8126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8126,
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

_source line 31 · 2026-05-12T01:44:08.832Z_

<details><summary>↩ Tool result · `toolu_01YC14ZmsSevFQqd7quVhDd8`</summary>

```text
# HqeKV Paper Summary

**Title:** "HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference"

**Authors:** Not listed in the provided content

**Venue:** ACL ARR 2026 January

**Publication Date:** January 5, 2026 (modified March 20, 2026)

## What It Does

HqeKV addresses memory overhead from key-value (KV) cache during long-context language model inference. The framework combines compression techniques to reduce cache size while preserving output quality.

## Hybrid Approach

Yes, it performs both operations jointly. The system employs "both quantization and eviction" simultaneously, where an integrated optimizer selects appropriate compression actions for each cached element. Rather than applying uniform compression, it adapts compression strategies based on individual KV pair importance.

## Key Features

- Uses a "joint K–V importance metric" for improved importance assessment
- Supports "flexible conversion policies across multiple quantization precision levels"
- Achieves improved quality metrics (40.53 to 49.98) within memory constraints

## Trajectory-Aware or Agentic?

The provided content contains no information suggesting the method is trajectory-aware or agentic in nature.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "543c6c7b-4950-44c5-8bb0-dee93667b473",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "bd313f0b-4580-4a0f-b38c-9e4b207b9cee",
  "sourceToolAssistantUUID": "543c6c7b-4950-44c5-8bb0-dee93667b473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T01:44:15.230Z_

<details><summary>↩ Tool result · `toolu_01KEhvNPYYtr4wqAYXRZXBai`</summary>

```text
Web search results for query: ""KV cache" "multi-turn" OR "multi-step" OR "agentic" compression eviction quantization 2026 arXiv"

Links: [{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/html/2604.10235"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"},{"title":"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs","url":"https://arxiv.org/html/2603.08727"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"VQKV: High-Fidelity and High-Ratio Cache Compression via Vector-Quantization","url":"https://arxiv.org/html/2603.16435"},{"title":"CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences","url":"https://arxiv.org/html/2503.12491v2"},{"title":"HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=sLG2XsjSDe"}]

I found several highly relevant 2026 arXiv papers and research on KV cache optimization. Here are the key findings:

## Recent 2026 Research on KV Cache Compression

### Major Papers and Approaches

Recent strategies for KV cache optimization are categorized into five major directions: cache eviction, compression and reconstruction, hybrid memory solutions, novel attention mechanisms, and combined approaches.

### Agentic Coding Applications

CodeComp is a training-free KV cache compression framework for agentic code tasks that incorporates structural priors from static program analysis, leveraging the Code Property Graph to guide compression decisions including span-level structural protection and structure-aware budget allocation.

The emergence of deep-research agents and agentic-AI systems, in which LLMs autonomously plan, retrieve, and act across extended workflows, has significantly increased demand for large context windows, with benchmarks like AGENTIF showing that agentic scenarios often involve instructions with thousands of words and complex tool specifications.

### Quantization Advances

TurboQuant is Google Research's latest contribution accepted at ICLR 2026, addressing a weakness in prior quantization methods where MSE-optimal scalar quantizers introduce systematic bias in inner product estimation through a two-stage pipeline where the first stage (PolarQuant) applies random orthogonal rotation to each key and value vector before quantization.

Quantization consistently outperforms rank reduction at matched storage budgets across five models, with quantization outperforming rank reduction in every setting tested.

### Hybrid Approaches

HqeKV is a hybrid compression framework built on both quantization and eviction, offering finer-grained compression options that adapt smoothly to the varying importance of cached KV pairs, with an integrated optimizer automatically selecting the best compression action for each cached element.

When combining eviction and quantization strategies, even at a very aggressive 6.25% compression ratio, the combined approach maintains strong performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09c21ba5-7c99-4579-ae17-3f2841e516db",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "b7747ec1-305f-4e9f-904e-e9fb9db02e37",
  "sourceToolAssistantUUID": "09c21ba5-7c99-4579-ae17-3f2841e516db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-12T01:44:22.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vv3kASN9YW83t6ewg3Mbnc`</summary>

```json
{
  "query": "arXiv 2603.04428 \"Agent Memory Below the Prompt\" KV cache multi-agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7747ec1-305f-4e9f-904e-e9fb9db02e37",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpyD3JXCzqFywPz4x75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55ec7096-c1b7-4287-bf18-b9af01b6aa42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ruv5UQpboSKjxTsjte5ZaL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 20319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1612,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-12T01:44:22.701Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JN21cRH2qfGXA1nhB4CcNx`</summary>

```json
{
  "query": "\"KV cache\" \"reinforcement learning\" OR \"RL\" eviction quantization 2026 arXiv reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55ec7096-c1b7-4287-bf18-b9af01b6aa42",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011CawpyD3JXCzqFywPz4x75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b135db29-1cc3-443b-af6d-4748d84f28a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ruv5UQpboSKjxTsjte5ZaL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 20319,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1612
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 20319,
          "cache_creation_input_tokens": 1612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1612,
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

_source line 35 · 2026-05-12T01:44:30.024Z_

<details><summary>↩ Tool result · `toolu_01Vv3kASN9YW83t6ewg3Mbnc`</summary>

```text
Web search results for query: "arXiv 2603.04428 "Agent Memory Below the Prompt" KV cache multi-agent"

Links: [{"title":"[2603.04428] Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/abs/2603.04428"},{"title":"Agent Memory Below the Prompt:","url":"https://arxiv.org/pdf/2603.04428"},{"title":"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/html/2603.04428"},{"title":"GitHub - yshk-mxim/agent-memory: Persistent KV cache for multi-agent LLM systems on Apple Silicon · GitHub","url":"https://github.com/yshk-mxim/agent-memory"},{"title":"Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing | OpenReview","url":"https://openreview.net/forum?id=kgzBkyqg6Z"},{"title":"KVCache-Centric Memory for LLM Agents | OpenReview","url":"https://openreview.net/forum?id=YolJOZOGhI"},{"title":"Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead","url":"https://arxiv.org/html/2603.10062v1"},{"title":"KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning","url":"https://arxiv.org/html/2602.23592v2"},{"title":"Make Your LVLM KV Cache More Lightweight","url":"https://arxiv.org/html/2605.00789"},{"title":"Prompt Leakage via KV-Cache Sharing in Multi-Tenant ...","url":"https://www.ndss-symposium.org/wp-content/uploads/2025-1772-paper.pdf"}]

I found the paper you searched for! Here's what I found:

arXiv 2603.04428 is titled "Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices" by Yakov Pyotr Shkolnikov.

**Key Problem:** Multi-agent LLM systems on edge devices face a memory management problem where device RAM is too small to hold every agent's KV cache simultaneously. On Apple M4 Pro with 10.2 GB of cache budget, only 3 agents fit at 8K context in FP16, and a 10-agent workflow must constantly evict and reload caches.

**The Solution:** The paper addresses this by persisting each agent's KV cache to disk in 4-bit quantized format and reloading it directly into the attention layer, eliminating redundant O(n) prefill computation via direct cache restoration.

**Performance Results:** Cache restoration reduces time-to-first-token by up to 136x across three architectures (Gemma: 22–136x at 4K–32K; DeepSeek: 11–76x at 4K–32K; Llama: 24–111x at 4K–16K; 3–10x at 1K). Q4 quantization fits 4x more agent contexts into fixed device memory than FP16.

The paper was submitted on February 17, 2026, and is open-source on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55ec7096-c1b7-4287-bf18-b9af01b6aa42",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "3f6bcf59-e42a-400a-b48c-29cd1bcbfa8e",
  "sourceToolAssistantUUID": "55ec7096-c1b7-4287-bf18-b9af01b6aa42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-12T01:44:38.308Z_

<details><summary>↩ Tool result · `toolu_01JN21cRH2qfGXA1nhB4CcNx`</summary>

```text
Web search results for query: ""KV cache" "reinforcement learning" OR "RL" eviction quantization 2026 arXiv reasoning"

Links: [{"title":"Learning to Evict from Key-Value Cache","url":"https://arxiv.org/html/2602.10238v1"},{"title":"[2602.10238] Learning to Evict from Key-Value Cache","url":"https://arxiv.org/abs/2602.10238"},{"title":"G-KV: Decoding-Time KV Cache Eviction with Global Attention","url":"https://arxiv.org/html/2512.00504"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203v1"},{"title":"randomization boosts kv caching, learning balances query ...","url":"https://arxiv.org/pdf/2601.18999"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"[2602.03203] ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/abs/2602.03203"},{"title":"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs","url":"https://arxiv.org/html/2603.08727"}]

Based on the search results, I found several recent 2026 arXiv papers combining KV cache management with reinforcement learning and reasoning models:

## Key Recent Papers (2026)

**1. Learning to Evict from Key-Value Cache (arXiv 2602.10238)**
This paper reframes KV cache eviction as a reinforcement learning problem and introduces KV Policy (KVP), a framework of lightweight per-head RL agents trained on pre-computed generation traces using only key and value vectors. While prior work has addressed KV cache constraints through heuristics, memory hierarchies, or compression, this approach introduces an RL framework that casts eviction as a ranking problem.

**2. ForesightKV: Optimizing KV Cache Eviction for Reasoning Models (arXiv 2602.03203)**
ForesightKV is a training-based KV cache eviction framework that learns to predict which KV pairs to evict during long-text generations, with a Golden Eviction algorithm that identifies optimal eviction KV pairs at each step using future attention scores. The framework formulates cache eviction as a Markov Decision Process and applies the GRPO algorithm, with experiments on AIME2024 and AIME2025 benchmarks showing it consistently outperforms prior methods under only half the cache budget while benefiting synergistically from both supervised and reinforcement learning approaches.

**3. G-KV: Decoding-Time KV Cache Eviction with Global Attention (arXiv 2512.00504)**
This work implements a reinforcement learning framework specifically tailored for KV cache compression, which eliminates the discrepancy between the training policy and the inference policy.

**4. ARKV: Adaptive and Resource-Efficient KV Cache Management (arXiv 2603.08727)**
ARKV proposes a lightweight framework that dynamically assigns cache precision to tokens at runtime, where tokens are ranked via an efficient heavy-hitter score and assigned to one of three states—Original, Quantization, or Eviction—under a strict memory budget.

These papers represent the current frontier of combining RL and quantization techniques for optimizing KV cache management in reasoning models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b135db29-1cc3-443b-af6d-4748d84f28a9",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "a1def3fd557e01d90",
  "type": "user",
  "uuid": "66b573c6-f245-49ff-8994-33df7ca59624",
  "sourceToolAssistantUUID": "b135db29-1cc3-443b-af6d-4748d84f28a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-12T01:45:20.440Z_

Now I have comprehensive findings. Here is my report:

---

## Paper 1: Neural Garbage Collection (NGC) -- arXiv:2604.18002

**Status: CONFIRMED EXISTS.**

- **Exact title:** "Neural Garbage Collection: Learning to Forget while Learning to Reason"
- **Authors:** Michael Y. Li, Jubayer Ibn Hamid, Emily B. Fox, Noah D. Goodman
- **Date:** April 20, 2026
- **What it does:** The model periodically pauses during chain-of-thought reasoning, scores all KV cache blocks via its internal attention mechanism, samples a subset to keep, and permanently deletes the rest. It then continues reasoning on the pruned cache.
- **Eviction-only?** YES -- purely eviction, no quantization component.
- **Requires RL training?** YES -- it uses reinforcement learning end-to-end. Both reasoning tokens and cache-eviction decisions are treated as discrete actions sampled from the LM, optimized jointly from outcome-based task reward alone. No supervised fine-tuning or proxy objectives.
- **Benchmarks:** Countdown, AMC, AIME tasks.
- **Compression:** 2-3x peak KV cache size compression (the abstract says 2-3x; some summaries say 2-5x).
- **Scope:** Single-model reasoning chains only. Not multi-turn or agentic workflows.

## Paper 2: CapKV -- arXiv:2604.25975

**Status: CONFIRMED EXISTS.**

- **Exact title:** "Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective"
- **Authors:** Jiaming Yang, Chenwei Tang, Liangli Zhen, Jiancheng Lv
- **Date:** April 28, 2026
- **What it does:** Derives a closed-form mutual information objective from the Information Bottleneck principle under a linear-Gaussian surrogate of attention. Shows that many existing eviction heuristics are approximations of the same capacity-maximization principle. Introduces CapKV, which uses statistical leverage scores and a log-determinant approximation to select which KV entries to retain.
- **Eviction-only?** YES -- purely eviction-based, no quantization.
- **Training-free?** YES -- no RL or fine-tuning needed; it's a scoring method applied at inference time.
- **Scope:** General long-context benchmarks, not specifically agentic or trajectory-aware.

## Competitor Landscape: April-May 2026 KV Cache Compression Papers

Here are the most relevant recent papers, particularly those that might compete with a "trajectory-aware joint quantization-eviction for agentic KV caches" method:

### Joint Quantization + Eviction (most directly competitive):

1. **HqeKV** (OpenReview, ACL ARR Jan 2026) -- "Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference." Jointly applies quantization and eviction with a joint K-V importance metric and flexible multi-precision conversion policies. NOT trajectory-aware or agentic.

2. **ARKV** (arXiv:2603.08727, March 2026) -- "Adaptive and Resource-Efficient KV Cache Management." Dynamically ranks tokens and assigns them to three states: Original, Quantization, or Eviction, under a strict memory budget. Closest to joint quant-eviction under budget constraints. NOT agentic.

3. **EvicPress** (arXiv:2512.14946) -- "Joint KV-Cache Compression and Eviction for Efficient LLM Serving." Multi-tier storage with lossy compression + adaptive eviction. System-level, not trajectory-aware.

### Agentic-specific:

4. **CodeComp** (arXiv:2604.10235, April 11, 2026) -- "Structural KV Cache Compression for Agentic Coding." Training-free, uses Code Property Graphs for structure-aware eviction in agentic coding pipelines. Eviction-only, code-domain-specific, not joint quant-eviction.

5. **Agent Memory Below the Prompt** (arXiv:2603.04428, Feb 2026) -- Persistent Q4 KV cache for multi-agent LLM inference on edge. Quantizes and persists caches to disk for agent switching. Multi-agent but focused on cache persistence/reload, not compression during inference.

### RL-based eviction (related to NGC):

6. **ForesightKV** (arXiv:2602.03203, Feb 2026) -- Learns to predict which KV pairs to evict for reasoning models using a Markov Decision Process + GRPO. Evaluated on AIME benchmarks. Eviction-only, not joint with quantization.

7. **KV Policy (KVP)** (arXiv:2602.10238, Feb 2026) -- "Learning to Evict from Key-Value Cache." Per-head RL agents for eviction. Eviction-only.

### Quantization-only:

8. **RateQuant** (arXiv:2605.06675, April 2026) -- Mixed-precision KV cache quantization via rate-distortion theory. Per-head optimal bit allocation. Quantization-only, no eviction.

9. **TurboQuant** (Google, ICLR 2026) -- 3-bit KV cache quantization with 6x compression. Quantization-only.

### Key Gap Identified:

**No paper found from April-May 2026 combines ALL of:** (a) trajectory-awareness across multi-step/agentic workflows, (b) joint quantization + eviction, and (c) agentic KV cache management. The closest are HqeKV/ARKV for joint quant-eviction (but not agentic/trajectory-aware) and CodeComp for agentic compression (but eviction-only, code-specific). NGC uses RL for trajectory-aware eviction but is eviction-only within single reasoning chains, not agentic workflows.

Sources:
- [NGC - arXiv:2604.18002](https://arxiv.org/abs/2604.18002)
- [CapKV - arXiv:2604.25975](https://arxiv.org/abs/2604.25975)
- [CodeComp - arXiv:2604.10235](https://arxiv.org/abs/2604.10235)
- [HqeKV - OpenReview](https://openreview.net/forum?id=sLG2XsjSDe)
- [ARKV - arXiv:2603.08727](https://arxiv.org/html/2603.08727)
- [EvicPress - arXiv:2512.14946](https://arxiv.org/html/2512.14946)
- [ForesightKV - arXiv:2602.03203](https://arxiv.org/abs/2602.03203)
- [KV Policy - arXiv:2602.10238](https://arxiv.org/abs/2602.10238)
- [RateQuant - arXiv:2605.06675](https://arxiv.org/abs/2605.06675)
- [Agent Memory Below the Prompt - arXiv:2603.04428](https://arxiv.org/abs/2603.04428)
- [MarkTechPost Top 10 KV Cache Techniques](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66b573c6-f245-49ff-8994-33df7ca59624",
  "isSidechain": true,
  "agentId": "a1def3fd557e01d90",
  "requestId": "req_011Cawpzuh5WjSsiQWNxdGLT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c536123-f783-44c2-a834-2f83d0671e69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6rt3pimzDcFu62YkVPTQc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2115,
      "cache_read_input_tokens": 21931,
      "output_tokens": 1871,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1871,
          "cache_read_input_tokens": 21931,
          "cache_creation_input_tokens": 2115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2115,
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
