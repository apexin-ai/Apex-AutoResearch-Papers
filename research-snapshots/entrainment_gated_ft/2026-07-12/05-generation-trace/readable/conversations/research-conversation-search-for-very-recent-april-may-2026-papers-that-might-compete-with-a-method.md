# Research conversation: Search for very recent (April-May 2026) papers that might compete with a method called "TrajComp" that does trajectory-a

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aef8cf0a5e74b8ac5.jsonl`
- **Structured JSON:** [`325de7e15aaa67ed911c.json`](../../sessions/32/325de7e15aaa67ed911c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

57 recorded events

### User

_source line 1 · 2026-05-12T01:51:04.294Z_

Search for very recent (April-May 2026) papers that might compete with a method called "TrajComp" that does trajectory-aware joint quantization-eviction for agentic KV caches. I need to find papers the proposal might have missed.

Search these specific queries:
1. "KV cache compression multi-turn 2026" 
2. "KV cache reasoning long chain-of-thought compression May 2026"
3. "agentic LLM serving efficiency 2026"
4. "KV cache eviction quantization joint optimization 2026"
5. "speculative decoding KV cache agent 2026"

For each search, note any papers NOT in this list of already-cited works: ThinKV, HqeKV, ARKV, NGC, CapKV, LookaheadKV, TTKV, TRIM-KV, RateQuant, Transactional Attention, MixedDimKV, PBKV, KVFlow, EpiCache, SideQuest, CodeComp, CacheTTL, R-KV, PM-KVQ, TriAttention, KVTC, DMS, EVICPRESS, TurboQuant, ForesightKV, KVComm, Self-Indexing KVCache.

Use WebSearch. Report any genuinely new competitors that are missing from the proposal. Be concise.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "a8d5d3ae-ccc7-4434-9a8e-cecb9cf0def0",
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

_source line 2 · 2026-05-12T01:51:04.299Z_

```json
{
  "parentUuid": "a8d5d3ae-ccc7-4434-9a8e-cecb9cf0def0",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
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
  "uuid": "51f9645d-adfb-4d27-bba6-846f6cde6f12",
  "timestamp": "2026-05-12T01:51:04.299Z",
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

_source line 3 · 2026-05-12T01:51:09.143Z_



I'll search for recent papers across all five queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51f9645d-adfb-4d27-bba6-846f6cde6f12",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqVN679jXJA3JmpxT9A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0389a53-cf7c-42c5-9a66-efdcf7cefe84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AH82h4bzHd8vvtLpEsbVZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 880,
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

_source line 4 · 2026-05-12T01:51:09.222Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NT4NyZAqKvftvXZj75tDR5`</summary>

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
  "parentUuid": "a0389a53-cf7c-42c5-9a66-efdcf7cefe84",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqVN679jXJA3JmpxT9A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d07af6be-b83b-4d6e-bfc1-f57faef13e26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AH82h4bzHd8vvtLpEsbVZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 880,
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

### Tool result

_source line 5 · 2026-05-12T01:51:09.226Z_

<details><summary>↩ Tool result · `toolu_01NT4NyZAqKvftvXZj75tDR5`</summary>

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
  "parentUuid": "d07af6be-b83b-4d6e-bfc1-f57faef13e26",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "9272b095-bfd6-42fa-a1c9-99b4f14d7605",
  "sourceToolAssistantUUID": "d07af6be-b83b-4d6e-bfc1-f57faef13e26",
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

_source line 6 · 2026-05-12T01:51:13.662Z_



Now let me run all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9272b095-bfd6-42fa-a1c9-99b4f14d7605",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqVjBrxWDzyruyZwPTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "446baa03-b68a-4524-b325-8e288ebc2cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4PS3WFEFGitjgjufYkwNM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1407,
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

_source line 7 · 2026-05-12T01:51:14.093Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017o2fkdPdxjwug7QyL677mf`</summary>

```json
{
  "query": "KV cache compression multi-turn 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "446baa03-b68a-4524-b325-8e288ebc2cff",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqVjBrxWDzyruyZwPTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea3f0918-91cc-4a5a-a3ef-ff1c32f09cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4PS3WFEFGitjgjufYkwNM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1407,
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

_source line 8 · 2026-05-12T01:51:15.038Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016uR7fUZqyz3vdbG6PCAqQF`</summary>

```json
{
  "query": "KV cache reasoning long chain-of-thought compression May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea3f0918-91cc-4a5a-a3ef-ff1c32f09cfb",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqVjBrxWDzyruyZwPTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b2b7671-cc36-4f56-8ea7-4e66ac899b09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4PS3WFEFGitjgjufYkwNM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1407,
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

_source line 9 · 2026-05-12T01:51:15.507Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014GJRsyBM9r226Ux5Fbwmu1`</summary>

```json
{
  "query": "agentic LLM serving efficiency 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b2b7671-cc36-4f56-8ea7-4e66ac899b09",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqVjBrxWDzyruyZwPTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b0364d4-7d43-43cc-8393-d5238c6cae88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4PS3WFEFGitjgjufYkwNM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1407,
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

_source line 10 · 2026-05-12T01:51:15.973Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01776e55q1ma9neooSQsERbB`</summary>

```json
{
  "query": "KV cache eviction quantization joint optimization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b0364d4-7d43-43cc-8393-d5238c6cae88",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqVjBrxWDzyruyZwPTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a7416c0-9be5-42dd-a6b1-6573aa0fb63c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4PS3WFEFGitjgjufYkwNM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9103,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1407
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 258,
          "cache_read_input_tokens": 9103,
          "cache_creation_input_tokens": 1407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1407,
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

_source line 11 · 2026-05-12T01:51:15.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01USV9D9jSef1zp6RuDStwjj`</summary>

```json
{
  "query": "speculative decoding KV cache agent 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a7416c0-9be5-42dd-a6b1-6573aa0fb63c",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqVjBrxWDzyruyZwPTv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6208967e-a2da-43f2-bc5b-ae949f665bea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4PS3WFEFGitjgjufYkwNM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9103,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1407
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 258,
          "cache_read_input_tokens": 9103,
          "cache_creation_input_tokens": 1407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1407,
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

_source line 12 · 2026-05-12T01:51:22.387Z_

<details><summary>↩ Tool result · `toolu_014GJRsyBM9r226Ux5Fbwmu1`</summary>

```text
Web search results for query: "agentic LLM serving efficiency 2026"

Links: [{"title":"Agentix: An Efficient Serving Engine for LLM Agents as General Programs | USENIX","url":"https://www.usenix.org/conference/nsdi26/presentation/luo"},{"title":"GitHub - yxf203/Awesome-Efficient-Agents: Survey and paper list on efficiency-guided LLM agents (memory, tool learning, planning). · GitHub","url":"https://github.com/yxf203/Awesome-Efficient-Agents"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Agentic LLM Models & Frameworks 2026 | Adaline","url":"https://www.adaline.ai/blog/top-agentic-llm-models-frameworks-for-2026"},{"title":"Best Agentic AI Models January 2026: Top LLMs for Autonomous Agents & Tool Use | WhatLLM.org","url":"https://whatllm.org/blog/best-agentic-models-january-2026"},{"title":"The Best LLMs for Agentic Coding in 2026 (Real-World, Not Just Benchmarks) - DEV Community","url":"https://dev.to/danishashko/the-best-llms-for-agentic-coding-in-2026-real-world-not-just-benchmarks-96n"},{"title":"Top LLMs and AI Trends for 2026 | Clarifai Industry Guide","url":"https://www.clarifai.com/blog/llms-and-ai-trends"},{"title":"The Best Open-Source LLMs for Agentic Coding in 2026 | MindStudio","url":"https://www.mindstudio.ai/blog/best-open-source-llms-agentic-coding-2026"},{"title":"5 Key Trends Shaping Agentic Development in 2026 - The New Stack","url":"https://thenewstack.io/5-key-trends-shaping-agentic-development-in-2026/"},{"title":"7 Agentic AI Trends to Watch in 2026 - MachineLearningMastery.com","url":"https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/"}]

Based on the search results, here's what I found about agentic LLM serving efficiency in 2026:

## Key Developments in Agentic LLM Serving Efficiency

### Advanced Serving Systems

Large language model applications are evolving beyond simple chatbots into dynamic, general-purpose agentic programs. Agentix is an LLM serving system that treats programs as first-class citizens to minimize their end-to-end latencies. Existing LLM serving systems ignore dependencies between programs and calls, missing significant opportunities for optimization, with programs experiencing long cumulative wait times primarily due to head-of-line blocking.

### Cost-Performance Optimization

As organizations deploy agent fleets that make thousands of LLM calls daily, the economics of running agents at scale demand heterogeneous architectures: expensive frontier models for complex reasoning and orchestration, mid-tier models for standard tasks, and small language models for high-frequency execution.

The Plan-and-Execute pattern, where a capable model creates a strategy that cheaper models execute, can reduce costs by 90% compared to using frontier models for everything. Strategic caching of common agent responses, batching similar requests, and using structured outputs to reduce token consumption are becoming standard practices.

### Token Efficiency in Models

MiMo-V2.5-Pro reaches comparable capability to top proprietary models while using roughly 40–60% fewer tokens per trajectory, with this difference compounding quickly across long agentic runs.

### Production Scaling Challenges

While nearly two-thirds of organizations are experimenting with AI agents, fewer than one in four have successfully scaled them to production—2026's central business challenge.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b0364d4-7d43-43cc-8393-d5238c6cae88",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "8e0da566-b3c4-4fdb-9cef-6f47f99c7809",
  "sourceToolAssistantUUID": "6b0364d4-7d43-43cc-8393-d5238c6cae88",
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

_source line 13 · 2026-05-12T01:51:22.927Z_

<details><summary>↩ Tool result · `toolu_017o2fkdPdxjwug7QyL677mf`</summary>

```text
Web search results for query: "KV cache compression multi-turn 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING","url":"https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Google’s TurboQuant Compression May Support Faster Inference, Same Accuracy on Less Capable Hardware - InfoQ","url":"https://www.infoq.com/news/2026/04/turboquant-compression-kv-cache/"},{"title":"Compress the KV Cache with TurboQuant and Haystack | Haystack","url":"https://haystack.deepset.ai/tutorials/49_turboquant_quantization_with_huggingface"},{"title":"TurboQuant KV Cache Compression — Full HIP/ROCm Port (gfx1100) · ggml-org/llama.cpp · Discussion #21526","url":"https://github.com/ggml-org/llama.cpp/discussions/21526"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"Nvidia says it can shrink LLM memory 20x without changing model weights | VentureBeat","url":"https://venturebeat.com/orchestration/nvidia-shrinks-llm-memory-20x-without-changing-model-weights"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | OpenReview","url":"https://openreview.net/forum?id=JFygzwx8SJ"}]

I found comprehensive information about KV cache compression for multi-turn conversations in 2026. Here are the key findings:

## Recent Advances in KV Cache Compression (2026)

### Major Techniques

**TurboQuant (Google Research)**
TurboQuant is a KV cache compression algorithm from Google Research (ICLR 2026) that shrinks cache vectors to 3–4 bits per coordinate without any retraining. It compresses large language models' Key-Value caches by up to 6x, with 3.5-bit compression providing near-zero accuracy loss and requiring no retraining.

**KVTC (NVIDIA - KV Cache Transform Coding)**
KVTC applies ideas from media compression formats like JPEG to shrink the key-value cache behind multi-turn AI systems, lowering GPU memory demands and speeding up time-to-first-token by up to 8x.

**DeepSeek's Multi-head Latent Attention (MLA)**
DeepSeek's MLA compresses KV cache 7-14× by storing a low-rank projection instead of full keys and values.

### Multi-Turn Conversation Optimization

Standard cache-eviction methods such as H2O are not suitable for multi-turn conversations, as they permanently discard tokens that may be required in later turns. However, RocketKV-MT is a variant designed for multi-turn settings that retains all KV tokens in memory for future turns while constraining token selection in the current turn.

KVzip is a query-agnostic method that optimizes reusable compressed KV caches, enabling efficient inference across diverse future queries within a dialogue, and ShadowKV demonstrates "multi-turn capability" by sharing low-rank subspaces between a sequence and its continuation.

### Performance Impact

KVzip reduces KV cache size by 3-4× and FlashAttention decoding latency by approximately 2×, with negligible performance loss in question-answering, retrieval, reasoning, and code comprehension tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea3f0918-91cc-4a5a-a3ef-ff1c32f09cfb",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "45c53d18-c2e4-430e-9370-6252c02bc40a",
  "sourceToolAssistantUUID": "ea3f0918-91cc-4a5a-a3ef-ff1c32f09cfb",
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

_source line 14 · 2026-05-12T01:51:23.360Z_

<details><summary>↩ Tool result · `toolu_01776e55q1ma9neooSQsERbB`</summary>

```text
Web search results for query: "KV cache eviction quantization joint optimization 2026"

Links: [{"title":"HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=sLG2XsjSDe"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Towards 10 Million Context Length LLM Inference with KV ...","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/neurips-2024-kvquant.pdf"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/html/2604.25975"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"KV Cache Strategies for LLM Efficiency","url":"https://www.emergentmind.com/topics/kv-cache-strategy"},{"title":"Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression","url":"https://arxiv.org/html/2603.20616"},{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"}]

Based on the web search results, I found several recent 2026 research papers and articles on KV cache eviction and quantization joint optimization:

## Key Recent Work (2026)

HqeKV is a hybrid compression framework combining both quantization and eviction that offers finer-grained compression options, with an integrated optimizer automatically selecting the best compression action for each cached element, and a joint K–V importance metric for more accurate importance assessment. Extensive experiments show that HqeKV improves output quality from 40.53 to 49.98 under the same memory constraints, outperforming state-of-the-art alternatives.

## Current 2026 Research Frontiers

The 2026 research frontier is moving toward latent-space compaction (Attention Matching, 50× compaction) and reasoning-aware compression (TriAttention, 10.7× memory reduction on AIME25 at matched accuracy).

## Quantization vs. Other Approaches

In every setting tested, quantization outperforms rank reduction at matched storage, with INT4 achieving near-lossless compression (+0.23 PPL on Mistral 7B at 75% reduction), while rank-32 at identical storage loses 34.77 PPL.

## Hybrid Optimization Approaches

Combination methods integrate multiple optimization strategies including eviction, compression, and hybrid memory solutions, with some methods applying token selection algorithms alongside quantization to reduce cache size, while others combine compression with offloading to CPU or disk.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a7416c0-9be5-42dd-a6b1-6573aa0fb63c",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "1ea14665-e0fa-4598-9aa6-7109f26390a0",
  "sourceToolAssistantUUID": "9a7416c0-9be5-42dd-a6b1-6573aa0fb63c",
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

_source line 15 · 2026-05-12T01:51:23.624Z_

<details><summary>↩ Tool result · `toolu_016uR7fUZqyz3vdbG6PCAqQF`</summary>

```text
Web search results for query: "KV cache reasoning long chain-of-thought compression May 2026"

Links: [{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=M3CeHnZKNC"},{"title":"R-KV: Redundancy-aware KV Cache Compression for ...","url":"https://arxiv.org/pdf/2505.24133"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"TriAttention | Efficient KV Cache Compression for Long-Context Reasoning","url":"https://weianmao.github.io/tri-attention-project-page/"},{"title":"ICLR Oral ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://iclr.cc/virtual/2026/oral/10009981"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning | OpenReview","url":"https://openreview.net/forum?id=udgrpHqw4F"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | OpenReview","url":"https://openreview.net/forum?id=Vem6FQvRvq"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2503.24358"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/html/2604.04921"}]

Based on the search results, here are the key findings on KV cache compression for reasoning models with long chain-of-thought:

## Recent Methods and Approaches

Several cutting-edge approaches have emerged to address KV cache memory bottlenecks in reasoning models:

**ThinKV** - ThinKV is a thought-adaptive KV cache compression framework based on the observation that attention sparsity reveals distinct thought types with varying importance within the CoT, applying a hybrid quantization–eviction strategy that assigns token precision by thought importance and progressively evicts tokens from less critical thoughts as reasoning trajectories evolve. On diverse benchmarks, ThinKV achieves near-lossless accuracy with less than 5% of the original KV cache.

**R-KV** - R-KV is a redundancy-aware KV cache compression approach for reasoning models with three key components: an attention-based importance scoring mechanism, a dynamic redundancy scoring mechanism that identifies repetitive tokens, and a joint eviction mechanism that balances both redundancy and importance. Remarkably, R-KV achieves 105% accuracy of the full KV baseline with around 16% of the KV cache using DeepSeek-R1-Distill-Llama-8B on the AIME-24 dataset.

**TriAttention** - TriAttention leverages pre-RoPE trigonometric modeling to compress KV cache for long-context reasoning, preserving accuracy while improving throughput and memory efficiency.

**PM-KVQ** - PM-KVQ improves reasoning benchmark performance by up to 8% over SOTA baselines under the same memory budget and achieves 2.73–5.18× throughput over the original 16-bit LLMs.

## Core Challenge

The long-output context generation of large reasoning models enables extended chain of thought but also drives rapid growth of the key–value cache, quickly overwhelming GPU memory.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b2b7671-cc36-4f56-8ea7-4e66ac899b09",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "5e453816-1e04-4c44-9c09-ad2ee0341df2",
  "sourceToolAssistantUUID": "5b2b7671-cc36-4f56-8ea7-4e66ac899b09",
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

_source line 16 · 2026-05-12T01:51:26.115Z_

<details><summary>↩ Tool result · `toolu_01USV9D9jSef1zp6RuDStwjj`</summary>

```text
Web search results for query: "speculative decoding KV cache agent 2026"

Links: [{"title":"LLM Inference: Prefill, Decode, KV Cache & Cost Guide (2026) | Morph","url":"https://www.morphllm.com/llm-inference"},{"title":"QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache | OpenReview","url":"https://openreview.net/forum?id=7SHbJENgHX"},{"title":"Revolutionizing AI Efficiency: Breakthroughs in KV Cache Compression and Speculative Decoding from Late 2025 Research | by Harsh Prakash | Medium","url":"https://medium.com/@hs5492349/revolutionizing-ai-efficiency-breakthroughs-in-kv-cache-compression-and-speculative-decoding-from-094588b6833f"},{"title":"DeepSeek 4 Flash: Local LLM Inference on Metal | The Coders Blog | Home","url":"https://thecodersblog.com/deepseek-4-flash-local-inference-engine-2026/"},{"title":"QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache","url":"https://arxiv.org/html/2502.10424v1"},{"title":"[2512.11920] CXL-SpecKV: A Disaggregated FPGA Speculative KV-Cache for Datacenter LLM Serving","url":"https://arxiv.org/abs/2512.11920"},{"title":"llm-d 0.5: Sustaining Performance at Scale | llm-d","url":"https://llm-d.ai/blog/llm-d-v0.5-sustaining-performance-at-scale"},{"title":"Building the foundation for running extra-large language models","url":"https://blog.cloudflare.com/high-performance-llms/"},{"title":"Modular: The Five Eras of KVCache","url":"https://www.modular.com/blog/the-five-eras-of-kvcache"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"}]

Based on the search results, here's what I found about speculative decoding, KV cache, and agent-related developments in 2026:

## Speculative Decoding Overview

Speculative decoding uses a small draft model (1-7B parameters) to generate 3-12 candidate tokens per step, which the target model verifies in one parallel forward pass. A smaller LLM (the draft model) generates candidate tokens for the target model to choose from, and the target model then just has to select from a small pool of candidate tokens in a single forward pass, which is faster and less computationally expensive than using the larger target model to generate the tokens.

## KV Cache Challenges and Solutions

The key-value cache stores computed attention keys and values from all previous tokens so they are not recomputed at each decode step. Without it, generating token N would require reprocessing all N-1 previous tokens, making inference O(n²) per output token. The KV cache reduces this to O(n).

However, the Key-Value (KV) cache is the primary bottleneck in terms of both GPU memory and latency, as the full KV cache must be loaded for each decoding step.

## Recent 2026 Developments

Recent research has introduced innovations combining these techniques:

- QuantSpec is a novel self-speculative decoding framework where the draft model shares the architecture of the target model but employs a hierarchical 4-bit quantized KV cache and 4-bit quantized weights for acceleration.

- Two groundbreaking papers from December 2025 — "Trellis: Learning to Compress Key-Value Memory in Attention Models" and "Yggdrasil: Bridging Dynamic Speculation and Static Runtime for Latency-Optimal Tree-Based LLM Decoding" — offer elegant solutions, with Trellis introducing a learnable, bounded-memory alternative to traditional KV caches, while Yggdrasil optimizes speculative decoding for dramatic speedups.

## Agent-Specific Applications

In agentic use cases, speculative decoding really shines because of the volume of tool calls and structured outputs that models need to generate. A tool call is largely predictable — you know there will be a name, description, and it's wrapped in a JSON envelope.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6208967e-a2da-43f2-bc5b-ae949f665bea",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "570155a3-48e2-48f1-b84a-024ec5c00de8",
  "sourceToolAssistantUUID": "6208967e-a2da-43f2-bc5b-ae949f665bea",
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

_source line 17 · 2026-05-12T01:51:36.828Z_

Let me do a few more targeted searches to dig deeper into some of the new papers that surfaced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "570155a3-48e2-48f1-b84a-024ec5c00de8",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqWyCFs7smr5fcUzjvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7f48ddb-1e79-4e48-bbfc-442eec7b1c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFK32fJ2ZNxPWptBEnVHuU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5527,
      "cache_read_input_tokens": 10510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5527,
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

_source line 18 · 2026-05-12T01:51:42.836Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pg26ErwMNLGpVDp2eFg5WL`</summary>

```json
{
  "query": "Agentix LLM serving system NSDI 2026 KV cache"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7f48ddb-1e79-4e48-bbfc-442eec7b1c82",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqWyCFs7smr5fcUzjvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53451753-f826-4d27-9913-73be1225491c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFK32fJ2ZNxPWptBEnVHuU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5527,
      "cache_read_input_tokens": 10510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5527,
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

_source line 19 · 2026-05-12T01:51:42.857Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EcfG3imfwQW28bXuMycB31`</summary>

```json
{
  "query": "KVzip query-agnostic KV cache compression 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53451753-f826-4d27-9913-73be1225491c",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqWyCFs7smr5fcUzjvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38616dfe-a6c0-41c0-a2e9-6bff0b178e3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFK32fJ2ZNxPWptBEnVHuU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5527,
      "cache_read_input_tokens": 10510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5527,
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

_source line 20 · 2026-05-12T01:51:42.874Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019hzULCDkadMAwtsDnw3NYi`</summary>

```json
{
  "query": "\"Reformulating KV Cache Eviction\" arxiv 2605 long-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38616dfe-a6c0-41c0-a2e9-6bff0b178e3e",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqWyCFs7smr5fcUzjvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f475dbe7-a25f-410e-878b-c004546f9ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFK32fJ2ZNxPWptBEnVHuU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5527,
      "cache_read_input_tokens": 10510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5527,
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

_source line 21 · 2026-05-12T01:51:43.020Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EgboUy17rzGY5VvmuSPGuE`</summary>

```json
{
  "query": "\"Rethinking KV Cache Eviction\" information-theoretic 2604 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f475dbe7-a25f-410e-878b-c004546f9ea2",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqWyCFs7smr5fcUzjvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "222de419-5af9-4d34-a956-81a224c0227a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFK32fJ2ZNxPWptBEnVHuU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5527,
      "cache_read_input_tokens": 10510,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5527
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 10510,
          "cache_creation_input_tokens": 5527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5527,
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

_source line 22 · 2026-05-12T01:51:43.025Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011LSgGdjE27ASGzUrDaRvjg`</summary>

```json
{
  "query": "QuantSpec self-speculative decoding quantized KV cache 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "222de419-5af9-4d34-a956-81a224c0227a",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqWyCFs7smr5fcUzjvJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da766970-34d9-486a-8756-80f67c7fc110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFK32fJ2ZNxPWptBEnVHuU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5527,
      "cache_read_input_tokens": 10510,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5527
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 10510,
          "cache_creation_input_tokens": 5527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5527,
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

_source line 23 · 2026-05-12T01:51:47.793Z_

<details><summary>↩ Tool result · `toolu_01EcfG3imfwQW28bXuMycB31`</summary>

```text
Web search results for query: "KVzip query-agnostic KV cache compression 2026"

Links: [{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | OpenReview","url":"https://openreview.net/forum?id=JFygzwx8SJ"},{"title":"[2505.23416] KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction","url":"https://arxiv.org/abs/2505.23416"},{"title":"ICML KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction","url":"https://icml.cc/virtual/2025/51778"},{"title":"GitHub - snu-mllab/KVzip: [NeurIPS'25 Oral] Query-agnostic KV cache eviction: 3–4× reduction in memory and 2× decrease in latency (Qwen3/2.5, Gemma3, LLaMA3)","url":"https://github.com/snu-mllab/KVzip"},{"title":"Paper page - KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction","url":"https://huggingface.co/papers/2505.23416"},{"title":"NeurIPS Poster KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction","url":"https://neurips.cc/virtual/2025/poster/118741"},{"title":"KVzip+: Query-Agnostic Cache Compression for LLMs","url":"https://www.emergentmind.com/topics/kvzip-f20aca11-8dcb-448c-95e5-495a16d101d4"},{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | Request PDF","url":"https://www.researchgate.net/publication/392204044_KVzip_Query-Agnostic_KV_Cache_Compression_with_Context_Reconstruction"},{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction","url":"https://www.emergentmind.com/papers/2505.23416"},{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | alphaXiv","url":"https://www.alphaxiv.org/resources/2505.23416v1"}]

Based on the search results, here's information about KVzip:

## Overview

KVzip is a query-agnostic KV cache eviction method enabling effective reuse of compressed KV caches across diverse queries.

## How It Works

KVzip quantifies the importance of a KV pair using the underlying LLM to reconstruct original contexts from cached KV pairs, subsequently evicting pairs with lower importance.

## Performance Results

KVzip reduces KV cache size by 3-4× and FlashAttention decoding latency by approximately 2×, with negligible performance loss in question-answering, retrieval, reasoning, and code comprehension tasks. Evaluations include various models such as LLaMA3.1, Qwen2.5, and Gemma3, with context lengths reaching up to 170K tokens.

## Publication Status

KVzip was published on September 18, 2025, and accepted as an oral presentation at NeurIPS 2025. The paper is also available on arXiv with the identifier 2505.23416, and the code is publicly available on GitHub.

## Advantages

KVzip significantly outperforms existing query-aware KV eviction methods, which suffer from performance degradation even at a 90% cache budget ratio under multi-query scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38616dfe-a6c0-41c0-a2e9-6bff0b178e3e",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "acd0dd27-4d03-4aa1-85e3-2e6e20e5c5f3",
  "sourceToolAssistantUUID": "38616dfe-a6c0-41c0-a2e9-6bff0b178e3e",
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

_source line 24 · 2026-05-12T01:51:48.414Z_

<details><summary>↩ Tool result · `toolu_01Pg26ErwMNLGpVDp2eFg5WL`</summary>

```text
Web search results for query: "Agentix LLM serving system NSDI 2026 KV cache"

Links: [{"title":"Agentix: An Efficient Serving Engine for LLM Agents as General Programs | USENIX","url":"https://www.usenix.org/conference/nsdi26/presentation/luo"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"KV Cache Locality: The Hidden Variable in Your LLM Serving Cost | Ranvier","url":"https://ranvier.systems/2026/04/30/kv-cache-locality-the-hidden-variable-in-your-llm-serving-cost.html"},{"title":"CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving | USENIX","url":"https://www.usenix.org/conference/fast26/presentation/liu-yang"},{"title":"How to save GPU memory in LLM serving: Principles and operating conditions of KV cache offloading","url":"https://www.backend.ai/blog/2026-04-how-to-save-gpu-memory-in-llm-serving-kv-cache-offloading"},{"title":"Oneiros: KV Cache Optimization through Parameter Remapping for Multi-tenant LLM Serving | Proceedings of the 2025 ACM Symposium on Cloud Computing","url":"https://dl.acm.org/doi/10.1145/3772052.3772215"},{"title":"CacheTTL: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://arxiv.org/html/2511.02230v4"},{"title":"Modular: The Five Eras of KVCache","url":"https://www.modular.com/blog/the-five-eras-of-kvcache"},{"title":"Multi-tier dynamic storage of KV cache for LLM inference under resource-constrained conditions | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02200-4"},{"title":"CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/html/2604.25080v1"}]

Based on the search results, here's what I found:

Agentix is an LLM serving system that treats programs as first-class citizens to minimize their end-to-end latencies. Agentix intercepts LLM calls submitted by programs, enriching schedulers with program-level context.

The paper "Agentix: An Efficient Serving Engine for LLM Agents as General Programs" was presented at the 23rd USENIX Symposium on Networked Systems Design and Implementation (NSDI 26) in May 2026. The research was conducted by a team including Michael Luo, Xiaoxiang Shi, Colin Cai, and others from major institutions and Google Research.

While the search results confirm Agentix's presence at NSDI 2026, they don't provide detailed information about specific KV cache optimization techniques used by the system. However, the results do show that KV cache management is a central concern in modern LLM serving systems, and various optimization strategies like paged attention, prefix caching, and parameter compression are being employed across production inference stacks in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53451753-f826-4d27-9913-73be1225491c",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "6fd0efe1-2daf-48b7-b536-4f4e4e57558c",
  "sourceToolAssistantUUID": "53451753-f826-4d27-9913-73be1225491c",
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

_source line 25 · 2026-05-12T01:51:49.666Z_

<details><summary>↩ Tool result · `toolu_019hzULCDkadMAwtsDnw3NYi`</summary>

```text
Web search results for query: ""Reformulating KV Cache Eviction" arxiv 2605 long-context"

Links: [{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"[2605.07234] Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/abs/2605.07234"},{"title":"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction","url":"https://arxiv.org/html/2605.06676"},{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"},{"title":"[2605.04075] RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/abs/2605.04075"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/html/2603.10899v1"},{"title":"[2605.06676] LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction","url":"https://arxiv.org/abs/2605.06676"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"Learning What to Write: Write-Gated KV for Efficient Long-Context Inference","url":"https://arxiv.org/html/2512.17452v1"},{"title":"Stateful KV Cache Management for LLMs: Balancing Space, Time, Accuracy, and Positional Fidelity","url":"https://arxiv.org/html/2511.04686"}]

I found the paper you're looking for! Here are the key details:

## Paper Information

**Title:** Reformulating KV Cache Eviction Problem for Long-Context LLM Inference

**ArXiv ID:** 2605.07234

**Authors:** Tho Mai and 1 other author

**Published:** May 8, 2026

## Main Contribution

The paper reformulates KV Cache eviction from a conventional head-wise, weight-averaging approach into an output-aware, layer-wise matrix multiplication approximation problem.

## Key Method

The authors introduce LaProx, a novel eviction strategy that explicitly models the multiplicative interaction between attention maps and projected value states to accurately quantify token contributions while accounting for inter-head dependencies.

## Results

Experimental results across 19 datasets on long-context benchmarks LongBench and Needle-In-A-Haystack demonstrate that the approach maintains model performance with only 5% of the KV cache and consistently outperforms prior works, achieving up to 2× accuracy loss reduction under extreme compression scenarios compared to existing state-of-the-art baselines.

You can access the paper at: https://arxiv.org/html/2605.07234


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f475dbe7-a25f-410e-878b-c004546f9ea2",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "e2c59fcf-e416-40a2-a1ae-445ca241d075",
  "sourceToolAssistantUUID": "f475dbe7-a25f-410e-878b-c004546f9ea2",
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

_source line 26 · 2026-05-12T01:51:49.896Z_

<details><summary>↩ Tool result · `toolu_011LSgGdjE27ASGzUrDaRvjg`</summary>

```text
Web search results for query: "QuantSpec self-speculative decoding quantized KV cache 2026"

Links: [{"title":"QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache","url":"https://arxiv.org/html/2502.10424v1"},{"title":"QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache | OpenReview","url":"https://openreview.net/forum?id=7SHbJENgHX"},{"title":"[2502.10424] QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache","url":"https://arxiv.org/abs/2502.10424"},{"title":"QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/quantspec"},{"title":"Paper page - QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache","url":"https://huggingface.co/papers/2502.10424"},{"title":"[2502.10424v1] QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache","url":"https://arxiv.org/abs/2502.10424v1"},{"title":"QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/9485_QuantSpec_Self_Speculativ.pdf"},{"title":"ICML Poster QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache","url":"https://icml.cc/virtual/2025/poster/46326"},{"title":"Speculative Decoding Meets Quantization: Compatibility Evaluation and Hierarchical Framework Design","url":"https://arxiv.org/html/2505.22179v1"},{"title":"QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/quantspec-self-speculative-decoding-hierarchical-quantized-kv"}]

Based on the search results, here's what I found about QuantSpec:

## Overview

QuantSpec is a self-speculative decoding method that utilizes 4-bit weights and a 4-bit hierarchical KV cache to speed up long-context inference.

## Problem it Addresses

Large Language Models are increasingly being deployed on edge devices for long-context settings, with the Key-Value (KV) cache being the primary bottleneck in terms of both GPU memory and latency, as the full KV cache must be loaded for each decoding step.

## Key Technical Approach

QuantSpec is a novel self-speculative decoding framework where the draft model shares the architecture of the target model but employs a hierarchical 4-bit quantized KV cache and 4-bit quantized weights for acceleration.

The method introduces a novel hierarchical quantization technique that enables bit-sharing between the target and draft models' KV caches, eliminating the need for additional memory for the draft model.

## Performance Results

QuantSpec maintains high acceptance rates (>90%) and reliably provides consistent end-to-end speedups up to ~2.5×, outperforming other self-speculative decoding methods that use sparse KV cache for long-context LLM inference, and also reduces the memory requirements by ~1.3× compared to these alternatives.

## Publication

The paper was published on arXiv on February 5, 2025, and has been featured at ICML 2025, with recognition from Apple Machine Learning Research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da766970-34d9-486a-8756-80f67c7fc110",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "7c2e6b96-6e5d-47c6-a6fd-6cd278918502",
  "sourceToolAssistantUUID": "da766970-34d9-486a-8756-80f67c7fc110",
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

_source line 27 · 2026-05-12T01:51:50.556Z_

<details><summary>↩ Tool result · `toolu_01EgboUy17rzGY5VvmuSPGuE`</summary>

```text
Web search results for query: ""Rethinking KV Cache Eviction" information-theoretic 2604 arxiv"

Links: [{"title":"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/html/2604.25975"},{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"},{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"When Less Latent Leads to Better Relay: Information-Preserving Compression for Latent Multi-Agent LLM Collaboration","url":"https://arxiv.org/html/2604.13349"},{"title":"Judge Q: Trainable Queries for Optimized Information Retention in KV Cache Eviction","url":"https://arxiv.org/html/2509.10798"},{"title":"GitHub - Aitherium/aitherkvcache: Near-optimal KV cache quantization for LLM inference. Sub-byte compression (2-4 bit) within 2.7x of information-theoretic optimum. arXiv:2504.19874 · GitHub","url":"https://github.com/Aitherium/aitherkvcache"},{"title":"KV Cache Offloading for Context-Intensive Tasks","url":"https://arxiv.org/html/2604.08426"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference","url":"https://arxiv.org/html/2604.19769"},{"title":"Neural Garbage Collection: Learning to Forget while Learning to Reason","url":"https://arxiv.org/html/2604.18002"}]

I found the paper you're looking for! Here are the key details:

## "Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective"

**Paper Information:**
- **ArXiv ID:** 2604.25975
- **Authors:** Jiaming Yang, Chenwei Tang, Liangli Zhen, Jiancheng Lv
- **Date:** April 28, 2026

**Overview:**

The paper rethinks KV cache eviction from an information-theoretic view, framing the process as the preservation of effective information capacity under strict memory constraints.

**Key Contributions:**

1. **Theoretical Framework:** The work rethinks KV cache eviction through the lens of the Information Bottleneck principle. Under a linear–Gaussian surrogate of attention, they derive a closed-form mutual information objective that characterizes the effective information capacity of a retained KV cache subset.

2. **Unification of Existing Methods:** The formulation reveals that a wide range of existing eviction strategies can be interpreted as different approximations of the same capacity-maximization principle.

3. **New Method - CapKV:** They introduce CapKV, a capacity-aware eviction method that directly targets information preservation via a log-determinant approximation using statistical leverage scores. This approach replaces heuristic selection with a theoretically grounded mechanism that preserves the maximum predictive signal.

**Results:** Extensive experiments across multiple models and long-context benchmarks show that CapKV consistently outperforms prior methods, achieving a better trade-off between memory efficiency and generational fidelity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "222de419-5af9-4d34-a956-81a224c0227a",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "4af9cdb6-75dc-46c3-ab49-fd0d8eb234af",
  "sourceToolAssistantUUID": "222de419-5af9-4d34-a956-81a224c0227a",
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

_source line 28 · 2026-05-12T01:51:58.057Z_

Let me search for a few more papers that surfaced as potentially new.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4af9cdb6-75dc-46c3-ab49-fd0d8eb234af",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqYmhFrKDMScLBRPhPH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a915cdc6-69c9-43b8-aa8c-eba3fd816894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwXbb2vZDXBgXSMsEcL4BP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 16037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3986,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T01:51:59.066Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019LYF3ZgiWEiY73ECnYtTNg`</summary>

```json
{
  "query": "LKV end-to-end learning head-wise budgets KV cache eviction arxiv 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a915cdc6-69c9-43b8-aa8c-eba3fd816894",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqYmhFrKDMScLBRPhPH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb54aac6-6ca9-48dc-8131-9af570116fcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwXbb2vZDXBgXSMsEcL4BP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 16037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3986,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-12T01:51:59.954Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HjuwHTDWr3dN9wZNs4GnVP`</summary>

```json
{
  "query": "RetentiveKV state-space memory multimodal KV cache eviction 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb54aac6-6ca9-48dc-8131-9af570116fcc",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqYmhFrKDMScLBRPhPH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33c0b5d3-5ec9-4eae-bbfb-f5d3a6fb7b56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwXbb2vZDXBgXSMsEcL4BP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 16037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3986,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T01:52:00.906Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BTXjmBHDPjku47XjAXtDWb`</summary>

```json
{
  "query": "CacheFlow 3D-parallel KV cache restoration arxiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33c0b5d3-5ec9-4eae-bbfb-f5d3a6fb7b56",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqYmhFrKDMScLBRPhPH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e834444d-7e65-4d08-8e30-d3fc11321ea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwXbb2vZDXBgXSMsEcL4BP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 16037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3986,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-12T01:52:01.375Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019NTaYqDXpTAqLZtAzkELPE`</summary>

```json
{
  "query": "CacheSlide cross-position KV cache reuse FAST 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e834444d-7e65-4d08-8e30-d3fc11321ea9",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqYmhFrKDMScLBRPhPH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60000a0f-d92b-43b7-98f0-0c981acbfe9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwXbb2vZDXBgXSMsEcL4BP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 16037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3986,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-12T01:52:02.187Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01McPXz9rHFVR3n1qeayKVRR`</summary>

```json
{
  "query": "\"Which Heads Matter for Reasoning\" RL-guided KV cache compression 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60000a0f-d92b-43b7-98f0-0c981acbfe9f",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqYmhFrKDMScLBRPhPH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4906641e-e15a-4377-932a-449f7ad5b17e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwXbb2vZDXBgXSMsEcL4BP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 16037,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3986
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 950,
          "output_tokens": 301,
          "cache_read_input_tokens": 16037,
          "cache_creation_input_tokens": 3986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3986,
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

_source line 34 · 2026-05-12T01:52:05.579Z_

<details><summary>↩ Tool result · `toolu_019LYF3ZgiWEiY73ECnYtTNg`</summary>

```text
Web search results for query: "LKV end-to-end learning head-wise budgets KV cache eviction arxiv 2605"

Links: [{"title":"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction","url":"https://arxiv.org/html/2605.06676"},{"title":"[2605.06676] LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction","url":"https://arxiv.org/abs/2605.06676"},{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/new"},{"title":"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation","url":"https://arxiv.org/html/2509.09754v1"},{"title":"Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression","url":"https://arxiv.org/html/2603.20616"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://arxiv.org/html/2407.11550v5"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/html/2603.10899"},{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"},{"title":"[2605.07234] Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/abs/2605.07234"}]

I found the paper you're looking for! Here are the key details:

## LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction

**arXiv:** 2605.06676

**Main Contribution:**
LKV is the first framework to transform KV eviction into an end-to-end differentiable learning problem, eliminating the need for hand-crafted heuristics, minimum budgets, or forced recent windows.

**Overview:**
LKV formulates KV compression as an end-to-end differentiable optimization problem, integrating LKV-H to learn task-optimized global budgets, and LKV-T to derive intrinsic KV importance without materializing attention matrices.

**Key Results:**
- LKV achieves state-of-the-art performance on both LongBench and RULER benchmarks at high compression rates.
- The learned global budget contributes more to performance gains than the selection policy itself, demonstrating the importance of precise, head-level resource allocation.
- By maintaining a 15% budget, LKV reduces the actual storage cost at 200k length from 25.0 GB (Full) to 3.75 GB (Ours), achieving a 6.6× reduction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb54aac6-6ca9-48dc-8131-9af570116fcc",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "2b50f8c4-e70b-47fa-b23b-735f233d14e4",
  "sourceToolAssistantUUID": "bb54aac6-6ca9-48dc-8131-9af570116fcc",
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

_source line 35 · 2026-05-12T01:52:07.189Z_

<details><summary>↩ Tool result · `toolu_01HjuwHTDWr3dN9wZNs4GnVP`</summary>

```text
Web search results for query: "RetentiveKV state-space memory multimodal KV cache eviction 2605"

Links: [{"title":"[2605.04075] RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/abs/2605.04075"},{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"},{"title":"[2605.07234] Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/abs/2605.07234"},{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"KV Cache System — TensorRT LLM","url":"https://nvidia.github.io/TensorRT-LLM/latest/features/kvcache.html"},{"title":"MadaKV: Adaptive Modality-Perception KV Cache Eviction for Efficient Multimodal Long-Context Inference","url":"https://arxiv.org/html/2506.15724"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/html/2512.03324v1"},{"title":"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=nJgS06sX3O"},{"title":"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/html/2603.04428v1"},{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"}]

Based on the web search results, I found comprehensive information about RetentiveKV:

## RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction

RetentiveKV is an entropy-driven KV cache optimization method that reformulates KV eviction from "discrete context truncation" to "continuous memory evolution" based on State Space Models.

### Key Problems Addressed

Multimodal Large Language Models face severe challenges in computational efficiency and memory consumption due to the substantial expansion of the visual KV cache when processing long visual contexts. More specifically, RetentiveKV addresses issues where visual tokens display "deferred importance," initially exhibiting low salience but becoming pivotal during later decoding which can lead to premature eviction, and where discrete pruning disrupts the inherent spatial continuity of visual cues.

### How It Works

The method leverages information entropy to quantify the information potential of low-attention tokens and integrates tokens scheduled for eviction into a continuous state space through entropy-guided state transitions, enabling their dynamic reactivation when semantic relevance arises during subsequent decoding.

### Performance Results

Extensive experiments on multimodal benchmarks demonstrate that RetentiveKV achieves 5.0 times KV cache compression and 1.5 times decoding acceleration.

The paper (arXiv:2605.04075) was authored by SiHao Liu and colleagues and was submitted on April 14, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33c0b5d3-5ec9-4eae-bbfb-f5d3a6fb7b56",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "80127575-93e2-4f4e-ac77-b209b0b9ae92",
  "sourceToolAssistantUUID": "33c0b5d3-5ec9-4eae-bbfb-f5d3a6fb7b56",
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

_source line 36 · 2026-05-12T01:52:08.066Z_

<details><summary>↩ Tool result · `toolu_01BTXjmBHDPjku47XjAXtDWb`</summary>

```text
Web search results for query: "CacheFlow 3D-parallel KV cache restoration arxiv 2604"

Links: [{"title":"[2604.25080] CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/abs/2604.25080"},{"title":"CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/html/2604.25080"},{"title":"Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/pdf/2604.25080"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=332&show=1000"},{"title":"Predictive Multi-Tier Memory Management for KV Cache in Large-Scale GPU Inference","url":"https://arxiv.org/html/2604.26968"},{"title":"CacheFlow: Compressive Streaming Memory for Efficient Long-Form Video Understanding","url":"https://arxiv.org/html/2511.13644"},{"title":"CacheFlow: Compressive Streaming Memory for Efficient Long-Form Video","url":"https://arxiv.org/pdf/2511.13644"},{"title":"KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs","url":"https://arxiv.org/html/2604.13226"},{"title":"[2410.05004v1] Fast State Restoration in LLM Serving with HCache","url":"https://arxiv.org/abs/2410.05004v1"},{"title":"[2511.13644] CacheFlow: Compressive Streaming Memory for Efficient Long-Form Video Understanding","url":"https://arxiv.org/abs/2511.13644"}]

I found the paper you're looking for. Here's what I found about **CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration**:

## Overview

CacheFlow is a KV cache restoration framework that rethinks cache restoration as a multi-dimensional parallel execution problem. KV cache restoration has emerged as a dominant bottleneck in serving long-context LLM workloads, including multi-turn conversations, retrieval-augmented generation, and agentic pipelines.

## Key Innovation

CacheFlow introduces a unified 3D parallelism abstraction across tokens, layers, and GPUs, enabling fine-grained overlap of recomputation and I/O along the structural dependencies of transformer inference. The system introduces a unified execution model that orchestrates token-, layer-, and GPU-level parallelism via a novel batch-aware two-pointer scheduling strategy, enabling fine-grained overlap of recomputation and transfer.

## Performance

CacheFlow reduces Time-To-First-Token (TTFT) by 10%–62% over existing advances across diverse models, workloads, and hardware.

## Paper Details

The paper (arXiv:2604.25080) was authored by Sean Nian and 4 other authors, and it addresses the fundamental inefficiencies in existing KV cache restoration approaches by leveraging parallelism opportunities that prior work had overlooked.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e834444d-7e65-4d08-8e30-d3fc11321ea9",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "db1ba472-e836-4aae-bbab-b954aa528fbe",
  "sourceToolAssistantUUID": "e834444d-7e65-4d08-8e30-d3fc11321ea9",
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

_source line 37 · 2026-05-12T01:52:08.329Z_

<details><summary>↩ Tool result · `toolu_019NTaYqDXpTAqLZtAzkELPE`</summary>

```text
Web search results for query: "CacheSlide cross-position KV cache reuse FAST 2026"

Links: [{"title":"CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving | USENIX","url":"https://www.usenix.org/conference/fast26/presentation/liu-yang"},{"title":"CacheSlide: Unlocking Cross Position-Aware KV Cache ...","url":"https://www.usenix.org/system/files/fast26-liu-yang.pdf"},{"title":"Architecting for Reuse: A Deep Journey into the Heart of KV Caching","url":"https://blog.everpuredata.com/purely-technical/cut-llm-inference-costs-with-kv-caching/"},{"title":"Fused KV Caching","url":"https://www.aussieai.com/research/fused-kv-caching"},{"title":"Modular: The Five Eras of KVCache","url":"https://www.modular.com/blog/the-five-eras-of-kvcache"},{"title":"KV Cache Reuse Strategy: Efficient Inference","url":"https://www.emergentmind.com/topics/kv-cache-reuse-strategy"},{"title":"When KV Cache Reuse Fails in Multi-Agent Systems: Cross-Candidate Interaction is Crucial for LLM Judges","url":"https://arxiv.org/html/2601.08343"},{"title":"8 KV-Cache Systems You Can’t Afford to Miss in 2025 | by Kobe | Medium","url":"https://medium.com/@kobeeee/8-kv-cache-systems-you-cant-afford-to-miss-in-2025-9e5ce8c863ff"},{"title":"LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference","url":"https://arxiv.org/html/2510.09665v2"},{"title":"KV Cache Strategies for LLM Efficiency","url":"https://www.emergentmind.com/topics/kv-cache-strategy"}]

Based on the search results, here's information about CacheSlide:

## CacheSlide Overview

CacheSlide addresses the challenge that Large Language Models (LLMs) deployed in agent-based applications with complex prompt structures have inadequate support from existing KV cache reuse strategies—Position-Dependent Caching (PDC) and Position-Independent Caching (PIC)—which either impose strict positional constraints or introduce significant computational overhead.

## Key Innovation

CacheSlide identifies a distinct pattern in agent workflows termed Relative-Position-Dependent Caching (RPDC), where reusable segments maintain consistent relative ordering despite absolute position shifts.

## Technical Approach

CacheSlide is a novel KV cache management system that enhances positional-encoding similarity for fixed segments, computes attention for only a minimal subset of tokens, combines new and cached KVs using learned weights, and implements layer-wise and spill-aware KV-cache optimizations.

## Performance Results

Experimental evaluation across multiple LLMs and agent benchmarks demonstrates that CacheSlide significantly outperforms state-of-the-art baselines, achieving 3.11-4.3× reduction in latency and 3.5-5.8× improvement in throughput.

The paper was presented at the 24th USENIX Conference on File and Storage Technologies (FAST 26) in February 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60000a0f-d92b-43b7-98f0-0c981acbfe9f",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "f45d539a-237c-4b30-a578-26f2a357d9a9",
  "sourceToolAssistantUUID": "60000a0f-d92b-43b7-98f0-0c981acbfe9f",
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

_source line 38 · 2026-05-12T01:52:10.017Z_

<details><summary>↩ Tool result · `toolu_01McPXz9rHFVR3n1qeayKVRR`</summary>

```text
Web search results for query: ""Which Heads Matter for Reasoning" RL-guided KV cache compression 2026"

Links: [{"title":"[2510.08525] Which Heads Matter for Reasoning? RL-Guided KV Cache Compression","url":"https://arxiv.org/abs/2510.08525"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression","url":"https://arxiv.org/html/2510.08525v1"},{"title":"[PDF] Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Which-Heads-Matter-for-Reasoning-RL-Guided-KV-Cache-Du-Jiang/bb15d15655a41d12c714b3cd88c810ee5bb2886e"},{"title":"WHICH HEADS MATTER FOR REASONING? RL-GUIDED ...","url":"https://openreview.net/pdf?id=RvjpYNYpbU"},{"title":"Paper page - Which Heads Matter for Reasoning? RL-Guided KV Cache Compression","url":"https://huggingface.co/papers/2510.08525"},{"title":"Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning | OpenReview","url":"https://openreview.net/forum?id=FJFVmeXusW"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://zefan-cai.github.io/R-KV.page/"},{"title":"Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning","url":"https://arxiv.org/html/2410.19258"},{"title":"[2410.19258] Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning","url":"https://arxiv.org/abs/2410.19258"}]

I found comprehensive information about "Which Heads Matter for Reasoning? RL-Guided KV Cache Compression." Here's an overview:

## Overview

RLKV uses reinforcement learning as a probe to discover which heads contribute to reasoning quality by directly optimizing their cache usage against actual generation outcomes.

## The Problem

Reasoning large language models exhibit complex reasoning behaviors via extended chain-of-thought generation that are highly fragile to information loss during decoding, creating critical challenges for KV cache compression. Existing token-dropping methods directly disrupt reasoning chains by removing intermediate steps, while head-reallocation methods, designed for retrieval tasks, fail to preserve the heads essential for generative reasoning.

## The Solution

RLKV is a novel reasoning-critical head identification method which uses reinforcement learning to directly optimize the relationship between each head's cache usage and reasoning quality. The method allocates full KV cache to reasoning-critical heads while aggressively compressing others.

## Key Results

Experiments reveal that only a small fraction of attention heads is essential for reasoning, enabling the KV compression approach to outperform baseline methods while achieving 20-50% cache reduction with near lossless performance compared to uncompressed results. Additionally, the approach enables up to 1.21x speedup.

The paper was published at Latent & Implicit Thinking Workshop @ ICLR 2026 with authors from Westlake University, McGill University, Mila, Zhejiang University, and MBZUAI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4906641e-e15a-4377-932a-449f7ad5b17e",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "ccce1d53-0dc1-44d1-85e2-2dd948c2db4a",
  "sourceToolAssistantUUID": "4906641e-e15a-4377-932a-449f7ad5b17e",
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

_source line 39 · 2026-05-12T01:52:13.741Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011BFMP2S8KLMDwR2titqEDU`</summary>

```json
{
  "query": "\"Hold Onto That Thought\" KV cache compression reasoning openreview 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccce1d53-0dc1-44d1-85e2-2dd948c2db4a",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqaCsruQKwcu2pucmFW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9950e6ed-4e57-42ae-951c-ae167b3abf53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqmJVJtk8AqbWCVu8zGCyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5608,
      "cache_read_input_tokens": 20023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5608,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-12T01:52:14.657Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RXDkcKpxycNEeSwaKuz7JE`</summary>

```json
{
  "query": "\"Attention Matching\" KV cache compaction 50x 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9950e6ed-4e57-42ae-951c-ae167b3abf53",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqaCsruQKwcu2pucmFW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1ea034c-246e-4871-9460-064350c5942a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqmJVJtk8AqbWCVu8zGCyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5608,
      "cache_read_input_tokens": 20023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5608,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-12T01:52:15.601Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NDVVGtx2SstM5xbJaxkWtF`</summary>

```json
{
  "query": "\"RocketKV-MT\" multi-turn KV cache 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1ea034c-246e-4871-9460-064350c5942a",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqaCsruQKwcu2pucmFW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eef4ef62-bdc4-4945-a14e-c055cbc9ba57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqmJVJtk8AqbWCVu8zGCyo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5608,
      "cache_read_input_tokens": 20023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5608,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-12T01:52:15.836Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KBcLw2cLGL3Xadobfxzijf`</summary>

```json
{
  "query": "\"Quantization Dominates Rank Reduction\" KV cache compression arxiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eef4ef62-bdc4-4945-a14e-c055cbc9ba57",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqaCsruQKwcu2pucmFW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "935636a7-dfa8-49a5-bc2c-0d214f390bdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqmJVJtk8AqbWCVu8zGCyo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5608,
      "cache_read_input_tokens": 20023,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5608
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 20023,
          "cache_creation_input_tokens": 5608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5608,
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

_source line 43 · 2026-05-12T01:52:20.830Z_

<details><summary>↩ Tool result · `toolu_011BFMP2S8KLMDwR2titqEDU`</summary>

```text
Web search results for query: ""Hold Onto That Thought" KV cache compression reasoning openreview 2026"

Links: [{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning | OpenReview","url":"https://openreview.net/forum?id=udgrpHqw4F"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://openreview.net/pdf?id=OtZtLYAdQY"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"ASSESSING KV CACHE COMPRESSION ON REASONING","url":"https://openreview.net/pdf/44b8f67e54d6247cd9efe3b9c1c731ff3faf9513.pdf"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"NeurIPS Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://neurips.cc/virtual/2025/loc/san-diego/126664"},{"title":"[2512.12008] Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/abs/2512.12008"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | OpenReview","url":"https://openreview.net/forum?id=Vem6FQvRvq"},{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | OpenReview","url":"https://openreview.net/forum?id=JFygzwx8SJ"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=2jwAjomEDB"}]

I found the paper "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning" for you. Here's what the research covers:

## Overview

The work benchmarks the performance of several popular compression strategies on long-reasoning tasks. Large language models are often bottlenecked by memory constraints, as the KV cache, which is used to significantly speed up attention computations, grows linearly with context length.

## Key Focus

Several popular strategies are targeted towards the prefill phase of processing long prompt context, and their performance is rarely assessed on reasoning tasks requiring long decoding. In particular, short but complex prompts, such as those in benchmarks like GSM8K and MATH500, often benefit from multi-step reasoning and self-reflection, resulting in thinking sequences thousands of tokens long.

## Main Findings

The analysis reveals that classical attention-based "heavy-hitter" strategies, which evict tokens based on accumulated attention scores, significantly outperform other methods, even defeating full-cache reasoning occasionally. This includes H2O and a novel extension of SnapKV called SnapKV-Decoding.

The paper appears to be under review for ICLR 2026 and was also presented as a workshop paper at NeurIPS 2025 on Efficient Reasoning. The research evaluates multiple KV cache compression methods including H2O, StreamingLLM, KNorm, and others across various reasoning benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9950e6ed-4e57-42ae-951c-ae167b3abf53",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "2471a85c-0113-469b-be94-f594dd76a933",
  "sourceToolAssistantUUID": "9950e6ed-4e57-42ae-951c-ae167b3abf53",
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

_source line 44 · 2026-05-12T01:52:22.043Z_

<details><summary>↩ Tool result · `toolu_01NDVVGtx2SstM5xbJaxkWtF`</summary>

```text
Web search results for query: ""RocketKV-MT" multi-turn KV cache 2026"

Links: [{"title":"RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression","url":"https://arxiv.org/html/2502.14051v2"},{"title":"GitHub - NVlabs/RocketKV: [ICML 2025] RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression · GitHub","url":"https://github.com/NVlabs/RocketKV"},{"title":"RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=RyOpooIxDF"},{"title":"RocketKV: Accelerating Long-Context LLM Inference via ...","url":"https://arxiv.org/pdf/2502.14051"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"[2502.14051] RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression","url":"https://arxiv.org/abs/2502.14051"},{"title":"ICML Poster RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression","url":"https://icml.cc/virtual/2025/poster/45253"},{"title":"RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression - Paper Detail","url":"https://deeplearn.org/arxiv/629109/rocketkv:-accelerating-long-context-llm-inference-via-two-stage-kv-cache-compression"},{"title":"RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression","url":"https://proceedings.mlr.press/v267/behnam25a.html"},{"title":"RocketKV: Accelerating Long-Context LLM Inference via Two- ...","url":"https://www.arxiv.org/pdf/2502.14051v3"}]

Here are the search results for "RocketKV-MT" multi-turn KV cache:

## Overview

RocketKV-MT is a multi-turn variant of RocketKV that avoids permanently evicting any KV tokens during the first stage; instead, all KV tokens are retained in memory across turns, ensuring that no potentially useful context is lost.

## Design and Purpose

In a multi-turn conversation setting, KV tokens that were pruned in earlier turns may become essential for answering queries in later turns because KV token importance could vary significantly between different turns, and permanently removing these tokens could lead to a noticeable accuracy drop in subsequent turns.

The second stage still performs dynamic selection over the subset of KV tokens filtered by the first stage, similar to the original RocketKV. The model generates responses using a reduced KV token set for speed, while reserving the full KV history for future turns.

## Performance

RocketKV-MT is more suitable for multi-turn decoding and performs on par with oracle top-k attention. RocketKV-MT retains all KV tokens in memory for future turns while constraining token selection in the current turn.

The research was published as part of the ICML 2025 conference proceedings and is available on arXiv and GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eef4ef62-bdc4-4945-a14e-c055cbc9ba57",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "11ec6418-13d9-47c7-a83d-3ff90b280f0c",
  "sourceToolAssistantUUID": "eef4ef62-bdc4-4945-a14e-c055cbc9ba57",
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

_source line 45 · 2026-05-12T01:52:23.669Z_

<details><summary>↩ Tool result · `toolu_01KBcLw2cLGL3Xadobfxzijf`</summary>

```text
Web search results for query: ""Quantization Dominates Rank Reduction" KV cache compression arxiv 2604"

Links: [{"title":"[2604.11501] Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/abs/2604.11501"},{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"},{"title":"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/html/2605.02905"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit","url":"https://arxiv.org/html/2604.15356"},{"title":"KVLinC: KV Cache Quantization with Hadamard Rotation and Linear Correction","url":"https://arxiv.org/html/2510.05373v1"},{"title":"[2604.15356] Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit","url":"https://arxiv.org/abs/2604.15356"},{"title":"[2604.04722] Don't Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/abs/2604.04722"},{"title":"GPU-Accelerated INT8 Quantization for KV Cache Compression in Large Language Models","url":"https://arxiv.org/html/2601.04719v1"},{"title":"XQuant: Breaking the Memory Wall for LLM Inference with KV Cache Rematerialization","url":"https://arxiv.org/html/2508.10395v1"}]

I found the paper you're looking for! Here are the key findings:

## "Quantization Dominates Rank Reduction for KV-Cache Compression" (arXiv:2604.11501)

This paper compares two strategies for compressing the KV cache in transformer inference: rank reduction (discard dimensions) and quantization (keep all dimensions, reduce precision). At matched storage budgets across five models (124M–14B, MHA and GQA), quantization consistently outperforms rank reduction—by 4–364 PPL depending on model and compression level.

On LAMBADA, INT4 matches FP16 accuracy (+0.23 PPL on Mistral 7B, +0.58 on GPT-2) while rank-32 at identical storage collapses to 0.4%.

**Key Mechanistic Insight:**

The gap is traced to a structural asymmetry: under softmax attention routing, removing a dimension can flip which token is attended (a discrete failure), while quantization noise is bounded and typically preserves score ordering.

Under quantization, all directions are preserved. High-spice directions receive their own per-channel scale, keeping the quantized value within the correct region of the softmax decision boundary.

**Practical Result:**

Joint K+V INT4 quantization achieves 75% total KV reduction at only +0.18 PPL on Mistral 7B.

The paper was published about a month ago on arXiv and authored by Samuel Salfati and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "935636a7-dfa8-49a5-bc2c-0d214f390bdd",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "d9e4dcc8-e0fb-4635-a8a9-184b8d3942ee",
  "sourceToolAssistantUUID": "935636a7-dfa8-49a5-bc2c-0d214f390bdd",
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

_source line 46 · 2026-05-12T01:52:24.128Z_

<details><summary>↩ Tool result · `toolu_01RXDkcKpxycNEeSwaKuz7JE`</summary>

```text
Web search results for query: ""Attention Matching" KV cache compaction 50x 2026"

Links: [{"title":"[2602.16284] Fast KV Compaction via Attention Matching","url":"https://arxiv.org/abs/2602.16284"},{"title":"New KV cache compaction technique cuts LLM memory 50x without accuracy loss | VentureBeat","url":"https://venturebeat.com/orchestration/new-kv-cache-compaction-technique-cuts-llm-memory-50x-without-accuracy-loss"},{"title":"Startup News: Hidden Blueprint Revealed for Cutting LLM Memory Costs by 50x Without Compromising Accuracy in 2026","url":"https://blog.mean.ceo/startup-news-llm-memory-costs-cut-50x-accuracy-intact-2026/"},{"title":"Research: Implement \"Fast KV Compaction via Attention Matching\" for extreme VRAM savings · Issue #20037 · ggml-org/llama.cpp","url":"https://github.com/ggml-org/llama.cpp/issues/20037"},{"title":"[2602.16284v1] Fast KV Compaction via Attention Matching","url":"https://arxiv.org/abs/2602.16284v1"},{"title":"Fast KV Compaction via Attention Matching","url":"https://arxiv.org/pdf/2602.16284"},{"title":"Fast KV Compaction via Attention Matching | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/fast-kv-compaction-via-attention-matching"},{"title":"How MIT's Attention Matching Shrinks AI Memory By 50x Without Breaking Anything - Softtechhub","url":"https://softtechhub.us/2026/03/08/attention-matching/"},{"title":"Fast KV Compaction via Attention Matching","url":"https://www.catalyzex.com/paper/fast-kv-compaction-via-attention-matching"},{"title":"LLM Memory Usage Reduced by 50x","url":"https://businessanalytics.substack.com/p/llm-memory-usage-reduced-by-50x"}]

Based on the web search results, here's what I found about Attention Matching, KV cache compaction, and the 50x compression achievement in 2026:

## Overview

Attention Matching is an approach for fast context compaction in latent space that constructs compact keys and values to reproduce attention outputs and preserve attention mass at a per-KV-head level. The technique was published in February 18, 2026 in a paper titled "Fast KV Compaction via Attention Matching."

## Key Achievement

The technique manages to compact the context by up to 50x with very little loss in quality. Attention Matching can compact the model's KV cache by 50x without reducing the accuracy, while taking only seconds to process the documents.

## How It Works

Attention Matching bypasses the slow training process through clever mathematical tricks. The researchers realized that to perfectly mimic how an AI interacts with its memory, they need to preserve two mathematical properties when compressing the original key and value vectors into a smaller footprint: the "attention output," which is the actual information the AI extracts when it queries its memory.

## Advantages Over Previous Methods

Attention Matching achieves high-level compaction ratios and quality while being orders of magnitude faster than gradient-based optimization. This is a significant improvement over the previous state-of-the-art Cartridges method, which took several hours of heavy GPU computation to compress a single context.

## Practical Applications

In enterprise settings, KV cache bloat forces trade-offs like smaller batch sizes or offloading to slower storage, potentially slashing deployment costs by orders of magnitude as AI handles longer contexts without hardware upgrades.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1ea034c-246e-4871-9460-064350c5942a",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "98e43910-13dd-4da0-ae02-6f6e8e837107",
  "sourceToolAssistantUUID": "e1ea034c-246e-4871-9460-064350c5942a",
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

_source line 47 · 2026-05-12T01:52:27.039Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VmPYyULFvB4bN1PeUbChRn`</summary>

```json
{
  "query": "\"KV Packet\" recomputation-free context-independent KV cache arxiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98e43910-13dd-4da0-ae02-6f6e8e837107",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqbFFWdWEgg9uF1ZACR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14b9ac9c-99c9-4502-b466-33ad7642dedd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6bSb6eiEEKQuMeBv6Di3G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1786,
      "cache_creation_input_tokens": 2185,
      "cache_read_input_tokens": 25631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2185,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-12T01:52:27.991Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DsKMZeChzHoZg8W2YeHw62`</summary>

```json
{
  "query": "\"Agent Memory Below the Prompt\" persistent KV cache multi-agent edge 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14b9ac9c-99c9-4502-b466-33ad7642dedd",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqbFFWdWEgg9uF1ZACR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1918187d-e2ea-469e-90e2-2b91c00025b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6bSb6eiEEKQuMeBv6Di3G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1786,
      "cache_creation_input_tokens": 2185,
      "cache_read_input_tokens": 25631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2185,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-12T01:52:28.157Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KVb61SH9KEXRyEAg1utXim`</summary>

```json
{
  "query": "\"Sequential KV Cache Compression\" probabilistic language tries Shannon limit 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1918187d-e2ea-469e-90e2-2b91c00025b2",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqbFFWdWEgg9uF1ZACR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63578831-2193-4d79-a5ec-5122a344580f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6bSb6eiEEKQuMeBv6Di3G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1786,
      "cache_creation_input_tokens": 2185,
      "cache_read_input_tokens": 25631,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2185
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1786,
          "output_tokens": 177,
          "cache_read_input_tokens": 25631,
          "cache_creation_input_tokens": 2185,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2185,
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

_source line 50 · 2026-05-12T01:52:34.611Z_

<details><summary>↩ Tool result · `toolu_01VmPYyULFvB4bN1PeUbChRn`</summary>

```text
Web search results for query: ""KV Packet" recomputation-free context-independent KV cache arxiv 2604"

Links: [{"title":"[2604.13226] KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs","url":"https://arxiv.org/abs/2604.13226"},{"title":"KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs","url":"https://arxiv.org/html/2604.13226"},{"title":"Paper page - KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs","url":"https://huggingface.co/papers/2604.13226"},{"title":"[2604.08426] KV Cache Offloading for Context-Intensive Tasks","url":"https://arxiv.org/abs/2604.08426"},{"title":"FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference","url":"https://arxiv.org/html/2505.13109"},{"title":"[2604.25080] CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/abs/2604.25080"},{"title":"CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/html/2604.25080"},{"title":"[2603.20397] KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/abs/2603.20397"},{"title":"TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference","url":"https://arxiv.org/html/2604.19769"},{"title":"PackKV: Reducing KV Cache Memory Footprint through LLM-Aware Lossy Compression","url":"https://arxiv.org/html/2512.24449"}]

I found the paper you're looking for! Here's what I found:

## KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs

KV Packet is a recomputation-free cache reuse framework that treats cached documents as immutable "packets" wrapped in light-weight trainable soft-token adapters, which are trained via self-supervised distillation to bridge context discontinuities.

### Key Problem It Solves

Standard KV caches are context-dependent: reusing a cached document in a new context requires recomputing KV states to account for shifts in attention distribution. Existing solutions such as CacheBlend, EPIC, and SAM-KV mitigate this issue by selectively recomputing a subset of tokens; however, they still incur non-negligible computational overhead (FLOPs) and increased Time-to-First-Token (TTFT) latency.

### Results

Experiments on Llama-3.1 and Qwen2.5 demonstrate that the proposed KV Packet method achieves near-zero FLOPs and lower TTFT than recomputation-based baselines, while retaining F1 scores comparable to those of the full recomputation baseline.

The paper was published on arXiv as **2604.13226** and code is available at https://github.com/ChuangtaoChen-TUM/KVPacket.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14b9ac9c-99c9-4502-b466-33ad7642dedd",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "d0471c0d-30b2-4f1f-b360-fa5fe3436d1b",
  "sourceToolAssistantUUID": "14b9ac9c-99c9-4502-b466-33ad7642dedd",
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

_source line 51 · 2026-05-12T01:52:37.216Z_

<details><summary>↩ Tool result · `toolu_01KVb61SH9KEXRyEAg1utXim`</summary>

```text
Web search results for query: ""Sequential KV Cache Compression" probabilistic language tries Shannon limit 2604"

Links: [{"title":"[2604.15356] Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit","url":"https://arxiv.org/abs/2604.15356"},{"title":"Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit","url":"https://arxiv.org/html/2604.15356"},{"title":"Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2604.15356"},{"title":"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization | Request PDF","url":"https://www.researchgate.net/publication/397202512_KVQuant_Towards_10_Million_Context_Length_LLM_Inference_with_KV_Cache_Quantization"},{"title":"KV Cache Compression 900000x Beyond TurboQuant and Per-Vector Shannon Limit | Hacker News","url":"https://news.ycombinator.com/item?id=47843715"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"CacheGen: KV Cache Compression and Streaming for Fast Large","url":"https://cs.stanford.edu/~keithw/sigcomm2024/sigcomm24-final1571-acmpaginated.pdf"},{"title":"TurboQuant and the KV Cache Revolution: Toward Memory-Boundless LLM Inference","url":"https://medium.com/@comeback01/turboquant-and-the-kv-cache-revolution-toward-memory-boundless-llm-inference-906af7e69370"},{"title":"Compressing KV Cache for Long-Context LLM Inference with Inter-Layer Attention Similarity","url":"https://arxiv.org/html/2412.02252v2"},{"title":"Google TurboQuant: The KV Cache Compression Math That Most Coverage Missed","url":"https://www.revolutioninai.com/2026/03/%20google-turboquant-kv-cache-compression-polarquant-qjl-explained-2026.html"}]

I found the research paper you're looking for. Here are the key results from my search:

## Sequential KV Cache Compression via Probabilistic Language Tries

The paper introduces a two-layer architecture where the first layer, probabilistic prefix deduplication, identifies semantically equivalent shared prefixes across sessions using the trie metric d_T(s, s') = -log_2 P_M(s ^ s') from Probabilistic Language Tries (PLTs).

Recent work on KV cache quantization, culminating in TurboQuant, has approached the Shannon entropy limit for per-vector compression of transformer key-value caches. However, this limit applies to a strictly weaker problem than the one that actually matters: compressing the KV cache as a sequence.

The second layer, predictive delta coding, stores only the residual of each new KV vector from the model's own prediction of it, achieving a per-token entropy bound of H(KV_{i+1} | KV_{<=i}) <= H(token_{i+1} | token_{<=i}). At typical language model perplexity -- approximately 10-20 for fluent English text -- this bound is 3.3-4.3 bits on average per token position, compared to TurboQuant's 3 bits per vector component (with typical attention heads having 64-128 components).

The theoretical compression ratio over TurboQuant is approximately 914,000x at the Shannon limit. Even at 1000x above the entropy floor -- a deliberately pessimistic worst-case overhead, two orders of magnitude above the 2-5x typical of practical source coders -- the ratio remains approximately 914x over TurboQuant, with compression improving rather than degrading as context length grows.

The paper (arxiv 2604.15356) was published on April 10, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63578831-2193-4d79-a5ec-5122a344580f",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "0c14924b-a049-4869-a541-e359f4db80f3",
  "sourceToolAssistantUUID": "63578831-2193-4d79-a5ec-5122a344580f",
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

_source line 52 · 2026-05-12T01:52:40.314Z_

<details><summary>↩ Tool result · `toolu_01DsKMZeChzHoZg8W2YeHw62`</summary>

```text
Web search results for query: ""Agent Memory Below the Prompt" persistent KV cache multi-agent edge 2026"

Links: [{"title":"[2603.04428] Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/abs/2603.04428"},{"title":"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/html/2603.04428v1"},{"title":"GitHub - yshk-mxim/agent-memory: Persistent KV cache for multi-agent LLM systems on Apple Silicon · GitHub","url":"https://github.com/yshk-mxim/agent-memory"},{"title":"Persistent Q4 KV Cache for Multi-Agent LLM Inference on ...","url":"https://arxiv.org/pdf/2603.04428"},{"title":"GitHub - VoltAgent/awesome-ai-agent-papers: A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, and autonomous systems. · GitHub","url":"https://github.com/VoltAgent/awesome-ai-agent-papers"},{"title":"GitHub - rohitg00/agentmemory: #1 Persistent memory for AI coding agents based on real-world benchmarks · GitHub","url":"https://github.com/rohitg00/agentmemory"},{"title":"The KV Cache Wars? - by Ken Huang - Agentic AI - Substack","url":"https://kenhuangus.substack.com/p/the-kv-cache-wars"},{"title":"What is KV Cache? Efficient LLM Inference | Ultralytics","url":"https://www.ultralytics.com/glossary/kv-cache"},{"title":"Agents that remember: introducing Agent Memory","url":"https://blog.cloudflare.com/introducing-agent-memory/"},{"title":"Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management","url":"https://arxiv.org/html/2605.06472v1"}]

I found relevant research on your query. Here's what the search uncovered:

## "Agent Memory Below the Prompt" Research

The primary paper titled "Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices" was published by Yakov Pyotr Shkolnikov in February 2026 and addresses a memory management problem in multi-agent LLM systems on edge devices where device RAM is too small to hold every agent's KV cache simultaneously.

### Key Technical Findings

**Performance Improvements:**
Cache restoration reduces time-to-first-token by up to 136x across three architectures (Gemma: 22--136x at 4K--32K; DeepSeek: 11--76x at 4K--32K; Llama: 24--111x at 4K--16K).

**Memory Efficiency:**
Q4 quantization fits 4x more agent contexts into fixed device memory than FP16.

**System Architecture:**
The approach persists each agent's KV cache to disk in 4-bit quantized format and reloads it directly into the attention layer, eliminating redundant O(n) prefill computation via direct cache restoration.

### The Problem Solved

On Apple M4 Pro with 10.2 GB of cache budget, only 3 agents fit at 8K context in FP16, and a 10-agent workflow must constantly evict and reload caches. Without persistence, every eviction forces a full re-prefill through the model—15.7 seconds per agent at 4K context.

The agent-memory implementation persists KV caches to disk as Q4-quantized safetensors files, and when an agent returns with the same conversation prefix, the server reloads the cache and skips directly to decoding.

The project is open-source on GitHub (yshk-mxim/agent-memory) and provides an OpenAI-compatible API for multi-agent edge inference systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1918187d-e2ea-469e-90e2-2b91c00025b2",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "724aa68a-5c7e-43a6-883f-a13df1f3f0f8",
  "sourceToolAssistantUUID": "1918187d-e2ea-469e-90e2-2b91c00025b2",
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

_source line 53 · 2026-05-12T01:52:43.430Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012WsakuCkkJPsobyFD68gn9`</summary>

```json
{
  "query": "\"Efficient Serving Dynamic Agent Workflows\" prediction KV cache management arxiv 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "724aa68a-5c7e-43a6-883f-a13df1f3f0f8",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqcSSVRy66sS9Un69eh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "520da5ff-53b0-454f-8308-80d6e3e42ee8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUxaZPUEJuU5wMoLhGakXB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1139,
      "cache_creation_input_tokens": 3863,
      "cache_read_input_tokens": 27816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3863,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-12T01:52:44.083Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016pxZY42f5VpSEsW8C2LHex`</summary>

```json
{
  "query": "\"eOptShrinkQ\" near-lossless KV cache spectral denoising quantization 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "520da5ff-53b0-454f-8308-80d6e3e42ee8",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqcSSVRy66sS9Un69eh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34376bb6-73cb-495e-acad-24c18d30e3aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUxaZPUEJuU5wMoLhGakXB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1139,
      "cache_creation_input_tokens": 3863,
      "cache_read_input_tokens": 27816,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3863
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1139,
          "output_tokens": 131,
          "cache_read_input_tokens": 27816,
          "cache_creation_input_tokens": 3863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3863,
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

_source line 55 · 2026-05-12T01:52:51.213Z_

<details><summary>↩ Tool result · `toolu_012WsakuCkkJPsobyFD68gn9`</summary>

```text
Web search results for query: ""Efficient Serving Dynamic Agent Workflows" prediction KV cache management arxiv 2605"

Links: [{"title":"Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management","url":"https://arxiv.org/html/2605.06472v1"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://arxiv.org/html/2507.07400v1"},{"title":"CacheTTL: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV","url":"https://arxiv.org/pdf/2511.02230"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM- ...","url":"https://arxiv.org/pdf/2507.07400"},{"title":"CacheTTL: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://arxiv.org/html/2511.02230v4"},{"title":"Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://arxiv.org/html/2511.02230v3"},{"title":"SAGA: Workflow-Atomic Scheduling for AI Agent Inference on GPU Clusters","url":"https://arxiv.org/html/2605.00528"},{"title":"1 A Survey on Large Language Model Acceleration based on KV Cache Management","url":"https://arxiv.org/pdf/2412.19442"},{"title":"Predictive Multi-Tier Memory Management for KV Cache in Large-Scale GPU Inference","url":"https://arxiv.org/html/2604.26968"},{"title":"LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference","url":"https://arxiv.org/pdf/2510.09665"}]

I found the paper you're looking for! The paper "Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management" (arXiv:2605.06472v1) was published on May 7, 2026 by researchers from Wuhan University, Dameng Database, Shanghai Jiao Tong University, Macquarie University, and HKUST.

**Key Contributions:**

The paper addresses a challenge where LLM-based workflows compose specialized agents to execute complex tasks and share substantial context. Existing approaches either manage KV-Cache at agent level and fail to exploit reuse opportunities within workflows, or manage cache at the workflow level but assume static sequences of agents. However, practical workflows are typically dynamic, where the sequence of invoked agents and thus cache reuse opportunities depend on the context of each task.

**The PBKV System:**

The authors propose PBKV (Prediction-Based KV-Cache Management), which predicts the agent invocations in several future steps by fusing guidance from historical workflows and context of the target workflow. Based on the predictions, PBKV estimates the reuse potential of cache entries and keeps the high-potential entries in GPU memory.

**Performance and Design:**

PBKV is guided by two design principles: hierarchical eviction and conservative prefetching, which together identify cache with low reuse value for reclamation while preserving high-value cache. The system reduces average workflow latency by up to 1.39x.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "520da5ff-53b0-454f-8308-80d6e3e42ee8",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "2b0726bb-98f2-468f-b405-1bbf4e5e5ee7",
  "sourceToolAssistantUUID": "520da5ff-53b0-454f-8308-80d6e3e42ee8",
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

_source line 56 · 2026-05-12T01:52:52.664Z_

<details><summary>↩ Tool result · `toolu_016pxZY42f5VpSEsW8C2LHex`</summary>

```text
Web search results for query: ""eOptShrinkQ" near-lossless KV cache spectral denoising quantization 2605"

Links: [{"title":"[2605.02905] eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/abs/2605.02905"},{"title":"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/html/2605.02905"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"TurboQuant - Extreme KV Cache Quantization · ggml-org/llama.cpp · Discussion #20969","url":"https://github.com/ggml-org/llama.cpp/discussions/20969"},{"title":"[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/abs/2605.06675"},{"title":"HeadQ: Model-Visible Distortion and a Prototype KV Quantizer-Corrector Codec","url":"https://arxiv.org/html/2605.03562"},{"title":"KV Cache Is Eating Your VRAM. Here’s How Google Fixed It With TurboQuant. | Towards Data Science","url":"https://towardsdatascience.com/kv-cache-is-eating-your-vram-heres-how-google-fixed-it-with-turboquant/"},{"title":"TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate","url":"https://arxiv.org/html/2504.19874v1"},{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"},{"title":"Residual vector quantization for KV cache compression in large language model","url":"https://arxiv.org/html/2410.15704v1"}]

Based on the search results, I found detailed information about **eOptShrinkQ**:

## eOptShrinkQ: Near-Lossless KV Cache Compression

eOptShrinkQ is a method that shows the key-value (KV) cache in transformer attention heads admits a natural decomposition into a low-rank shared context component and a full-rank per-token residual, well described by the spiked random matrix model.

### Method Overview

The approach comprises a two-stage compression pipeline: optimal singular value shrinkage (eOptShrink) automatically extracts the shared structure, and the residual—which satisfies the thin shell property with delocalized coordinates—is quantized by TurboQuant, a recently proposed per-vector scalar quantizer with near-optimal distortion guarantees.

### Key Innovation

By restoring the isotropy that scalar quantization assumes, spectral denoising eliminates the need for both outlier handling and dedicated inner product bias correction, freeing those bits for improved reconstruction.

### Theoretical Guarantees

The theoretical grounding in random matrix theory provides three guarantees: automatic rank selection via the BBP phase transition, provably near-zero inner product bias on the residual, and coordinate delocalization ensuring near-optimal quantization distortion.

### Performance Results

Experimentally, on Llama-3.1-8B and Ministral-8B, eOptShrinkQ saves nearly one bit per entry over TurboQuant at equivalent quality; on LongBench (16 tasks), eOptShrinkQ at ~2.2 bits per entry outperforms TurboQuant at 3.0 bits; and in multi-needle retrieval, eOptShrinkQ at 2.2 bits closely matches or exceeds uncompressed FP16.

The paper was submitted on April 6, 2026 (arXiv:2605.02905).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34376bb6-73cb-495e-acad-24c18d30e3aa",
  "isSidechain": true,
  "promptId": "1f6d7e7c-a871-4d90-8e9e-ec90d172c63b",
  "agentId": "aef8cf0a5e74b8ac5",
  "type": "user",
  "uuid": "8a5008c9-5f55-44d5-9ba6-da96eec6b1a1",
  "sourceToolAssistantUUID": "34376bb6-73cb-495e-acad-24c18d30e3aa",
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

_source line 57 · 2026-05-12T01:53:45.402Z_

Here is my consolidated report of papers that appear to be genuinely new competitors NOT already in the cited-works list.

---

## New Competitor Papers Not in the Cited List

### Directly Competing (joint quantization-eviction or trajectory/reasoning-aware compression)

1. **LaProx** (arXiv:2605.07234, May 2026) -- "Reformulating KV Cache Eviction Problem for Long-Context LLM Inference." Reformulates eviction as output-aware, layer-wise matrix multiplication approximation. Maintains performance with only 5% of the KV cache. Directly competes on the eviction-policy front.

2. **RLKV** (arXiv:2510.08525, ICLR 2026 Workshop) -- "Which Heads Matter for Reasoning? RL-Guided KV Cache Compression." Uses reinforcement learning to identify reasoning-critical heads, allocating full cache to them while aggressively compressing others. 20-50% cache reduction with near-lossless reasoning. Competes on reasoning-aware compression.

3. **LKV** (arXiv:2605.06676, May 2026) -- "End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction." First fully differentiable KV eviction framework. Learns head-wise budgets end-to-end, achieving 6.6x reduction at 200k context. Competes on learned eviction policy.

4. **eOptShrinkQ** (arXiv:2605.02905, May 2026) -- "Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization." Decomposes KV cache into low-rank shared component + quantized residual using random matrix theory. Saves ~1 bit/entry over TurboQuant. Competes on the quantization side.

5. **Hold Onto That Thought** (arXiv:2512.12008, under review ICLR 2026) -- Benchmarks KV cache compression methods specifically on long-decoding reasoning tasks. Finds heavy-hitter eviction strategies can sometimes *beat* full cache on reasoning. Relevant as a benchmark/analysis paper for reasoning-aware compression claims.

6. **Quantization Dominates Rank Reduction** (arXiv:2604.11501, April 2026) -- Rigorous comparison showing quantization consistently beats low-rank methods at matched storage. Provides theoretical argument (softmax decision-boundary sensitivity). Relevant to any joint quantization-eviction design decisions.

### Agentic / Multi-Turn Specific

7. **Agentix** (NSDI 2026, May 2026) -- "An Efficient Serving Engine for LLM Agents as General Programs." Program-aware scheduling for agentic LLM serving. Not KV-compression per se, but directly addresses agentic serving efficiency and could subsume or complement TrajComp's scheduling.

8. **CacheSlide** (FAST 2026, February 2026) -- "Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving." Identifies Relative-Position-Dependent Caching (RPDC) pattern in agent workflows. 3-4x latency reduction, 4-6x throughput improvement. Directly targets agent-workflow KV reuse.

9. **Agent Memory Below the Prompt** (arXiv:2603.04428, February 2026) -- Persistent Q4 KV cache for multi-agent edge inference. 136x TTFT reduction via disk-persisted quantized caches. Competes on the multi-agent quantized cache management angle.

10. **RocketKV-MT** (ICML 2025, but relevant) -- Multi-turn variant of RocketKV that retains all tokens across turns while constraining per-turn selection. Directly relevant to multi-turn trajectory-aware eviction.

11. **Efficient Serving for Dynamic Agent Workflows** (arXiv:2605.06472, May 2026) -- Note: this paper *is* PBKV, which is already in your cited list. Confirmed not new.

### Advanced Compression Techniques

12. **Attention Matching** (arXiv:2602.16284, February 2026) -- "Fast KV Compaction via Attention Matching." Achieves 50x compaction by constructing compact KVs that reproduce attention outputs. Orders of magnitude faster than gradient-based methods. A very strong competitor for aggressive compression.

13. **Sequential KV Cache Compression via Probabilistic Language Tries** (arXiv:2604.15356, April 2026) -- Exploits sequential redundancy across KV vectors using predictive delta coding. Theoretically achieves ~914x compression beyond TurboQuant's per-vector limit. Radical new direction for quantization.

14. **KVzip** (arXiv:2505.23416, NeurIPS 2025 Oral) -- Query-agnostic eviction using context reconstruction. 3-4x cache reduction. Relevant for multi-turn/multi-query reuse scenarios. Older but high-impact and not in the cited list.

15. **RetentiveKV** (arXiv:2605.04075, May 2026) -- State-space memory for multimodal KV cache eviction. Uses information entropy to avoid premature eviction of visually important tokens. 5x compression. Niche (multimodal) but novel eviction mechanism.

16. **KV Packet** (arXiv:2604.13226, April 2026) -- Recomputation-free context-independent KV caching using trainable soft-token adapters. Eliminates recomputation overhead for cache reuse across different contexts.

17. **QuantSpec** (arXiv:2502.10424, ICML 2025) -- Self-speculative decoding with hierarchical 4-bit quantized KV cache. 2.5x speedup. Relevant if TrajComp interacts with speculative decoding.

18. **CacheFlow** (arXiv:2604.25080, April 2026) -- 3D-parallel KV cache restoration for serving. Reduces TTFT by 10-62%. Systems-level competitor for agentic multi-turn serving.

---

## Summary of Highest-Priority Gaps

The most dangerous omissions from TrajComp's related work are:

- **LKV** and **LaProx** (both May 2026): learned/principled eviction methods that directly compete on the eviction half of joint optimization.
- **eOptShrinkQ** and **Sequential KV Compression via PLTs** (April-May 2026): advanced quantization methods that outperform TurboQuant, competing on the quantization half.
- **CacheSlide** and **Agentix** (FAST/NSDI 2026): systems papers directly targeting agent-workflow KV cache management.
- **Attention Matching** (February 2026): 50x compaction is a fundamentally different and very aggressive compression approach.
- **RLKV** (ICLR 2026): RL-guided reasoning-aware head selection directly overlaps with trajectory-aware reasoning compression.

Sources:
- [LaProx - Reformulating KV Cache Eviction](https://arxiv.org/abs/2605.07234)
- [RLKV - Which Heads Matter for Reasoning](https://arxiv.org/abs/2510.08525)
- [LKV - End-to-End Learning of Head-wise Budgets](https://arxiv.org/abs/2605.06676)
- [eOptShrinkQ](https://arxiv.org/abs/2605.02905)
- [Hold Onto That Thought](https://arxiv.org/abs/2512.12008)
- [Quantization Dominates Rank Reduction](https://arxiv.org/abs/2604.11501)
- [Agentix - NSDI 2026](https://www.usenix.org/conference/nsdi26/presentation/luo)
- [CacheSlide - FAST 2026](https://www.usenix.org/conference/fast26/presentation/liu-yang)
- [Agent Memory Below the Prompt](https://arxiv.org/abs/2603.04428)
- [RocketKV-MT](https://arxiv.org/abs/2502.14051)
- [Attention Matching](https://arxiv.org/abs/2602.16284)
- [Sequential KV Cache Compression via PLTs](https://arxiv.org/abs/2604.15356)
- [KVzip](https://arxiv.org/abs/2505.23416)
- [RetentiveKV](https://arxiv.org/abs/2605.04075)
- [KV Packet](https://arxiv.org/abs/2604.13226)
- [QuantSpec](https://arxiv.org/abs/2502.10424)
- [CacheFlow](https://arxiv.org/abs/2604.25080)
- [Top 10 KV Cache Compression Techniques - MarkTechPost](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a5008c9-5f55-44d5-9ba6-da96eec6b1a1",
  "isSidechain": true,
  "agentId": "aef8cf0a5e74b8ac5",
  "requestId": "req_011CawqdMCzjL7SAbiuMZQpB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac805b11-3e7c-4360-94f4-f9ea9acbaee8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "947b4d90-011e-4fa3-b17f-236d81333ba3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HyyuMAUakNQVW24qhm3La",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3158,
      "cache_read_input_tokens": 31679,
      "output_tokens": 2273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3158
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2273,
          "cache_read_input_tokens": 31679,
          "cache_creation_input_tokens": 3158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3158,
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
