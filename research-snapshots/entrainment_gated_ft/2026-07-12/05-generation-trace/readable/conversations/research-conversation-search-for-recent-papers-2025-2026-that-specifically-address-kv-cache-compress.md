# Research conversation: Search for recent papers (2025-2026) that specifically address KV cache compression or sparse attention for agent/tool-c

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ad767beca5f4ce1e6.jsonl`
- **Structured JSON:** [`aebeb3cc26eb108fef71.json`](../../sessions/ae/aebeb3cc26eb108fef71.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-10T20:57:57.228Z_

Search for recent papers (2025-2026) that specifically address KV cache compression or sparse attention for agent/tool-calling workloads. I want to find work that the following proposal might have missed:

The proposal "SegAttn" claims to be the first method combining segment-role boundaries (system prompt, tool schemas, conversation history, tool outputs) with generation-phase-aware dynamic sparsity for attention-level compression.

Search queries to try:
1. "agent KV cache compression 2025 2026" 
2. "tool calling attention optimization LLM"
3. "segment aware KV cache eviction agent"
4. "role-based attention sparsity language model"
5. "structured context compression LLM serving"
6. "semantic segment KV cache management 2026"

For any relevant papers found, note title, venue, date, and how they relate to SegAttn's claims.

Use WebSearch for each query. Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "d69ff39d-0dc2-4795-9e5d-4ee1bf318d58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:57:57.230Z_

```json
{
  "parentUuid": "d69ff39d-0dc2-4795-9e5d-4ee1bf318d58",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
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
  "uuid": "e56bc1ab-e0c7-4c08-aae4-cd2a5aee7aef",
  "timestamp": "2026-05-10T20:57:57.230Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T20:58:00.616Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JRUH9LFAN3ugvCaFDxNqLd`</summary>

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
  "parentUuid": "e56bc1ab-e0c7-4c08-aae4-cd2a5aee7aef",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZL2YVjpEm8yzkWegPS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6571da4d-40b0-4ae8-b048-cc60dd436d40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kg4BoiE41hBaoK768Bm1Cp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 769
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 769,
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

_source line 4 · 2026-05-10T20:58:00.623Z_

<details><summary>↩ Tool result · `toolu_01JRUH9LFAN3ugvCaFDxNqLd`</summary>

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
  "parentUuid": "6571da4d-40b0-4ae8-b048-cc60dd436d40",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "d0e8dbc2-ca5d-409f-b943-be2ebe3c2ee9",
  "sourceToolAssistantUUID": "6571da4d-40b0-4ae8-b048-cc60dd436d40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-10T20:58:04.100Z_

Now let me run all six search queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0e8dbc2-ca5d-409f-b943-be2ebe3c2ee9",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZLH8LSFh2gxmwjWgex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7eac836f-31db-47fd-a4b6-93bf5fb0c752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138FjSPbmKUnH2cMUqcpi8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8992,
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

_source line 6 · 2026-05-10T20:58:04.102Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019U5wHZcAfQqWgfViSsMYje`</summary>

```json
{
  "query": "agent KV cache compression 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eac836f-31db-47fd-a4b6-93bf5fb0c752",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZLH8LSFh2gxmwjWgex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f432759-e570-4259-b481-33e1280f48de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138FjSPbmKUnH2cMUqcpi8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8992,
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

_source line 7 · 2026-05-10T20:58:04.574Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0125qUQsKi4N3a71FchxRH4n`</summary>

```json
{
  "query": "tool calling attention optimization LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f432759-e570-4259-b481-33e1280f48de",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZLH8LSFh2gxmwjWgex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bb497e0-3b70-4116-ac50-633cd0da5bed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138FjSPbmKUnH2cMUqcpi8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8992,
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

_source line 8 · 2026-05-10T20:58:05.044Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Kb1phqTLgdsjaBNqoDudm`</summary>

```json
{
  "query": "segment aware KV cache eviction agent 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bb497e0-3b70-4116-ac50-633cd0da5bed",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZLH8LSFh2gxmwjWgex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af01cce4-adcb-43ab-a9e6-0e460cfd5bc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138FjSPbmKUnH2cMUqcpi8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8992,
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

_source line 9 · 2026-05-10T20:58:05.574Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q9dpXfa1wNXtHXHRZTtr7z`</summary>

```json
{
  "query": "role-based attention sparsity language model 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af01cce4-adcb-43ab-a9e6-0e460cfd5bc6",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZLH8LSFh2gxmwjWgex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4155d0db-4736-4bbb-b3be-e6830ad95e64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138FjSPbmKUnH2cMUqcpi8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8992,
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

_source line 10 · 2026-05-10T20:58:05.579Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017bQezZyxH1yzoeZmCAR7Wv`</summary>

```json
{
  "query": "structured context compression LLM serving 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4155d0db-4736-4bbb-b3be-e6830ad95e64",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZLH8LSFh2gxmwjWgex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21dfe11e-ed35-444c-aeac-45fb232df267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138FjSPbmKUnH2cMUqcpi8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8992,
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

_source line 11 · 2026-05-10T20:58:05.804Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017dC6NBrkxAYUz15DpezJGB`</summary>

```json
{
  "query": "semantic segment KV cache management 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21dfe11e-ed35-444c-aeac-45fb232df267",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZLH8LSFh2gxmwjWgex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bffc530b-ec55-4f60-8e19-22b2f561a1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138FjSPbmKUnH2cMUqcpi8n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8992,
      "output_tokens": 299,
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
          "output_tokens": 299,
          "cache_read_input_tokens": 8992,
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

_source line 12 · 2026-05-10T20:58:12.223Z_

<details><summary>↩ Tool result · `toolu_01Q9dpXfa1wNXtHXHRZTtr7z`</summary>

```text
Web search results for query: "role-based attention sparsity language model 2025"

Links: [{"title":"Attention heads of large language models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11873009/"},{"title":"Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/pdf/2507.19595"},{"title":"Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://aclanthology.org/2025.acl-long.1126.pdf"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"[2507.19595] Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/abs/2507.19595"},{"title":"Optimizing Native Sparse Attention with Latent Attention and Local Global Alternating Strategies","url":"https://arxiv.org/html/2511.00819v1"},{"title":"Accelerating LLM Inference Using Sparsity Kira Selby, Varun Khare NimbleEdge","url":"https://www.nimbleedge.com/sparsity-white-paper.pdf"},{"title":"Gated Attention for Large Language Models: Non-linearity, ...","url":"https://openreview.net/pdf?id=1b7whO4SfY"},{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"},{"title":"Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1126/"}]

Based on the search results, here's what I found about role-based attention sparsity in language models in 2025:

## Key Research Areas

The 2025 research on attention sparsity in language models covers several important developments:

### Sparse Attention Mechanisms
Sparse attention techniques limit attention computation to selected subsets of tokens based on fixed patterns, block-wise routing, or clustering strategies, enhancing efficiency while preserving contextual coverage.

### Native Sparse Attention (NSA)
One prominent advancement is Native Sparse Attention, which represents a significant architectural innovation. This approach achieves substantial speedups through arithmetic intensity-balanced algorithm design with implementation optimizations for modern hardware, and enables end-to-end training, reducing pretraining computation without sacrificing model performance. Experiments show the model pretrained with NSA maintains or exceeds Full Attention models across general benchmarks, long-context tasks, and instruction-based reasoning, while achieving substantial speedups over Full Attention on 64k-length sequences.

### Efficient Attention Survey
As demands for million-token contexts and low inference cost increase, the quadratic time-space complexity of canonical self-attention constitutes the principal bottleneck inhibiting scalability, making the redesign of attention mechanisms a critical frontier for architectural innovation.

### Sparsity in Model Components
Recent research also examines how sparsity varies across different components. Query and key matrices exhibit high sparsifiability in early blocks with sharp decline thereafter, while output projection sparsifiability varies dynamically, peaking at 80-90% in mid-model layers.

The research indicates that 2025 has seen significant progress in making sparse attention mechanisms both more efficient and trainable, addressing a critical bottleneck in long-context language model inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4155d0db-4736-4bbb-b3be-e6830ad95e64",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "0cd2d4ef-0ecc-4214-8904-35ae46983884",
  "sourceToolAssistantUUID": "4155d0db-4736-4bbb-b3be-e6830ad95e64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T20:58:12.284Z_

<details><summary>↩ Tool result · `toolu_019Kb1phqTLgdsjaBNqoDudm`</summary>

```text
Web search results for query: "segment aware KV cache eviction agent 2025"

Links: [{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM- ...","url":"https://arxiv.org/pdf/2507.07400"},{"title":"SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size","url":"https://arxiv.org/html/2510.22556v1"},{"title":"KV Cache Strategies for LLM Efficiency","url":"https://www.emergentmind.com/topics/kv-cache-strategy"},{"title":"GitHub - antgroup/cakekv · GitHub","url":"https://github.com/antgroup/cakekv"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM- ...","url":"https://openreview.net/pdf?id=5Iw1nDtYmT"},{"title":"EpiCache: Episodic KV Cache Management for Long ...","url":"https://arxiv.org/pdf/2509.17396"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...","url":"https://arxiv.org/pdf/2407.11550"},{"title":"KV Cache Reuse in Transformers","url":"https://www.emergentmind.com/topics/kv-cache-reuse"},{"title":"MEPIC: Memory Efficient Position Independent Caching for LLM Serving","url":"https://arxiv.org/html/2512.16822v1"},{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"}]

Based on the search results, I found several relevant papers and frameworks related to segment-aware KV cache eviction for agents in 2025:

## Key Findings:

**KVFlow: Workflow-Aware KV Cache Management**

KVFlow is a workflow-aware KV cache management framework designed to address limitations of existing LLM serving systems in agentic workflows. The framework includes several important features:

- Since agents may share common prefix segments in a tree-structured cache layout, KVFlow assigns eviction priorities at the cache node level rather than at the agent level.
- KVFlow adopts a workflow-aware eviction strategy that prioritizes evicting KV caches belonging to agents with large steps-to-execution, and assigns eviction priorities at the cache node level to enable fine-grained and efficient management.

**SABlock: Semantic-Aware KV Cache Eviction**

SABlock is a semantic-aware KV cache eviction framework with adaptive block sizes that first performs semantic segmentation to ensure that compression respects natural boundaries, applies a segment-guided token scoring mechanism to propagate segment-level importance to individual tokens, and performs an adaptive block size search for each segment to balance semantic coherence and memory efficiency.

**Other Segment-Based Approaches**

MEPIC partitions each request into chunk segments (immutable, reusable content) and prompt segments (request-specific content).

These frameworks demonstrate the 2025 trend toward segment-aware approaches for KV cache eviction, particularly in agent-based systems and long-context scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af01cce4-adcb-43ab-a9e6-0e460cfd5bc6",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "fd50de53-401a-49b7-8952-2a35d7254c4f",
  "sourceToolAssistantUUID": "af01cce4-adcb-43ab-a9e6-0e460cfd5bc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T20:58:12.793Z_

<details><summary>↩ Tool result · `toolu_0125qUQsKi4N3a71FchxRH4n`</summary>

```text
Web search results for query: "tool calling attention optimization LLM 2025"

Links: [{"title":"LLM-Based Agents for Tool Learning: A Survey | Data Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41019-025-00296-9"},{"title":"Tool calling optimization: Efficient agent actions","url":"https://www.statsig.com/perspectives/tool-calling-optimization"},{"title":"A Joint Optimization Framework for Enhancing Efficiency of ...","url":"https://aclanthology.org/2025.findings-acl.1149.pdf"},{"title":"vLLM: An Efficient Inference Engine for Large Language Models by Woosuk Kwon","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-192.pdf"},{"title":"Adobe LLM Optimizer | AI Search & Generative SEO for Brand Visibility","url":"https://business.adobe.com/products/llm-optimizer.html"},{"title":"Mastering LLM Techniques: Inference Optimization | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/"},{"title":"LLM Optimizer Overview | Adobe LLM Optimizer","url":"https://experienceleague.adobe.com/en/docs/llm-optimizer/using/essentials/overview"},{"title":"Optimize your content with Adobe LLM Optimizer | valantic","url":"https://www.valantic.com/en/blog/adobe-llm-optimizer-geo/"},{"title":"Custom Optimization Tools for LLM: Best Practices and Comparison","url":"https://www.patronus.ai/llm-testing/custom-optimization-tools-for-llm"},{"title":"LLM Optimization: Techniques and Guide | Mirantis","url":"https://www.mirantis.com/blog/llm-optimization-techniques/"}]

I've successfully completed the web search for "tool calling attention optimization LLM 2025". Here are the key findings:

## Research on Tool Calling and LLM Optimization in 2025

The search results reveal several important developments in tool calling optimization for Large Language Models in 2025:

### Tool Calling Optimization Frameworks

Current guidance shows how to build reliable tool use, choose a scalable agent architecture, design intuitive tools, and monitor the whole thing. Tool documentation should read like contracts with a purpose line, crisp examples, and argument types that leave no room for guessing.

### Multi-Agent Approaches

The multi-agent framework has brought new possibilities and dimensions to tool learning by enabling the decomposition of complex tasks into specialized subtasks handled by dedicated agents. One approach proposes decomposing the general multi-agent framework into three distinct roles: a planner, a caller, and a summarizer, with each role instantiated by a single LLM agent.

### Attention Optimization Techniques

Optimizations to the attention mechanism, including multi-query attention (MQA) and grouped-query attention (GQA), reduce memory required by KV caches, and techniques like FlashAttention improve performance by minimizing memory movement costs. FlashAttention can deliver substantial speedups (often 2-4x for long sequences) without changing model outputs by optimizing memory access patterns.

### Tree Search-Based Planning

ToolChain* presents an efficient tree search-based planning algorithm tailored for LLM agents, integrating the A* search algorithm with a task-specific cost function, enabling the model to prune high-cost branches and identify the most cost-effective valid path as the solution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bb497e0-3b70-4116-ac50-633cd0da5bed",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "0111ae48-da65-46b3-8e58-ab69080a850f",
  "sourceToolAssistantUUID": "1bb497e0-3b70-4116-ac50-633cd0da5bed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T20:58:13.043Z_

<details><summary>↩ Tool result · `toolu_019U5wHZcAfQqWgfViSsMYje`</summary>

```text
Web search results for query: "agent KV cache compression 2025 2026"

Links: [{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Google’s TurboQuant Compression May Support Faster Inference, Same Accuracy on Less Capable Hardware - InfoQ","url":"https://www.infoq.com/news/2026/04/turboquant-compression-kv-cache/"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/html/2604.10235"},{"title":"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | OpenReview","url":"https://openreview.net/forum?id=JFygzwx8SJ"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"Google TurboQuant: The KV Cache Compression Math That Most Coverage Missed","url":"https://www.revolutioninai.com/2026/03/%20google-turboquant-kv-cache-compression-polarquant-qjl-explained-2026.html"},{"title":"Published as a conference paper at ICLR 2026 ADAPTIVE KV-CACHE COMPRESSION","url":"https://www.arxiv.org/pdf/2509.03136"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=20JDhbJqn3"}]

Based on the search results, here's what I found about agent KV cache compression in 2025-2026:

## Recent Developments in KV Cache Compression for Agents

**Key Compression Techniques (2026 Frontier)**

The 2026 research frontier is moving toward latent-space compaction (Attention Matching, 50× compaction) and reasoning-aware compression (TriAttention, 10.7× memory reduction on AIME25 at matched accuracy).

**TurboQuant - Google's Leading Method**

Google Research unveiled TurboQuant, a novel quantization algorithm that compresses large language models' Key-Value caches by up to 6x. With 3.5-bit compression, near-zero accuracy loss, and no retraining needed, it allows developers to run massive context windows on significantly more modest hardware than previously required.

**Architectural Approaches**

DeepSeek's MLA is the architectural endgame for KV efficiency in 2026. Multi-head Latent Attention compresses KV cache 7-14× by storing a low-rank projection instead of full keys and values.

**Agentic Coding-Specific Solutions**

CodeComp is a training-free KV cache compression framework for agentic code tasks that incorporates structural priors from static program analysis. CodeComp leverages the Code Property Graph (CPG) extracted by Joern to guide two complementary compression decisions: span-level structural protection, which preserves structurally critical tokens from eviction, and structure-aware budget allocation.

**Multi-Query Scenarios**

KVzip is a query-agnostic KV cache eviction method enabling effective reuse of compressed KV caches across diverse queries. KVzip reduces KV cache size by 3–4× and FlashAttention decoding latency by approximately 2×, with negligible performance loss in question-answering, retrieval, reasoning, and code comprehension tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f432759-e570-4259-b481-33e1280f48de",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "35b9bfee-b16d-4a66-aa43-e294d33b0bf0",
  "sourceToolAssistantUUID": "9f432759-e570-4259-b481-33e1280f48de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T20:58:14.283Z_

<details><summary>↩ Tool result · `toolu_017bQezZyxH1yzoeZmCAR7Wv`</summary>

```text
Web search results for query: "structured context compression LLM serving 2025 2026"

Links: [{"title":"2026-01-06 From Context to EDUs: Faithful and Structured Context Compression","url":"https://arxiv.org/pdf/2512.14244"},{"title":"Automatic Context Compression in LLM Agents: Why Agents Need to Forget — and How to Help Them Do It Well | by Plaban Nayak | The AI Forum | Mar, 2026 | Medium","url":"https://medium.com/the-ai-forum/automatic-context-compression-in-llm-agents-why-agents-need-to-forget-and-how-to-help-them-do-it-43bff14c341d"},{"title":"CCF: A Context Compression Framework for Efficient Long-Sequence Language Modeling","url":"https://arxiv.org/html/2509.09199v1"},{"title":"Compressing Code Context for LLM-based Issue Resolution","url":"https://arxiv.org/html/2603.28119"},{"title":"Prompt Compression for Large Language Models: A Survey","url":"https://aclanthology.org/2025.naacl-long.368.pdf"},{"title":"AI Agent Context Compression: Strategies for Long-Running Sessions | Zylos Research","url":"https://zylos.ai/research/2026-02-28-ai-agent-context-compression-strategies"},{"title":"ACON: OPTIMIZING CONTEXT COMPRESSION FOR ...","url":"https://openreview.net/pdf?id=7JbSwX6bNL"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"[2510.08907] Autoencoding-Free Context Compression for LLMs via Contextual Semantic Anchors","url":"https://arxiv.org/abs/2510.08907"},{"title":"Prompt Compression Techniques: Reducing Context Window Costs While Improving LLM Performance | by Kuldeep Paul | Medium","url":"https://medium.com/@kuldeep.paul08/prompt-compression-techniques-reducing-context-window-costs-while-improving-llm-performance-afec1e8f1003"}]

I found several relevant results on structured context compression for LLM serving in 2025-2026. Here's a summary of the key findings:

## Recent Research on Structured Context Compression

**EDU-Based Context Compression (January 2026)**
An EDU-based Context Compressor framework has emerged as a recent approach. This method preserves global structure while capturing fine-grained details and operates without latent representations, ensuring seamless unfaithful content mitigation.

**CCF Framework (September 2025)**
The CCF framework integrates segment-wise semantic aggregation with key-value memory encoding, forming compact representations that support accurate reconstruction and long-range understanding. It achieves competitive perplexity under high compression ratios and significantly improves throughput and memory efficiency, highlighting the potential of structured compression for scalable and effective long-context language modeling.

**Agent-Focused Compression Strategies (2025-2026)**
Recent approaches ask LLMs to produce structured JSON summaries with session_intent, progress_so_far, key_facts, artifacts_created, next_steps, and open_questions. In 2025–2026, the field has converged on anchored iterative summarization, failure-driven guideline optimization (ACON), and provider-native compaction APIs.

**ACON Framework (October 2025)**
ACON is validated on AppWorld, OfficeBench, and Multi-objective QA, showing that it reduces memory usage by 26-54% (peak tokens) while preserving task success with large LLMs.

**Industry Trends**
The industry is shifting from expanding context windows to smarter context management, with 2026 trends suggesting context window size is plateauing as focus shifts to inference-time scaling, hybrid compression+caching, and memory-augmented architectures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21dfe11e-ed35-444c-aeac-45fb232df267",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "ceb054c3-62be-4dc8-b051-6e4e7b653743",
  "sourceToolAssistantUUID": "21dfe11e-ed35-444c-aeac-45fb232df267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T20:58:14.797Z_

<details><summary>↩ Tool result · `toolu_017dC6NBrkxAYUz15DpezJGB`</summary>

```text
Web search results for query: "semantic segment KV cache management 2026"

Links: [{"title":"SentenceKV: Efficient LLM Inference via Sentence-Level Semantic KV Caching | OpenReview","url":"https://openreview.net/forum?id=HyPeYU9JR6"},{"title":"GraphRAG-RS 2026: KV Caching, Structural Extraction, GLiNER-Relex to improve speed | by Carlo C. | Feb, 2026 | Medium","url":"https://autognosi.medium.com/graphrag-rs-2026-kv-caching-structural-extraction-gliner-relex-to-improve-speed-d340c0e5d127"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"SentenceKV: Efficient LLM Inference via Sentence-Level Semantic KV Caching","url":"https://arxiv.org/html/2504.00970v1"},{"title":"EpiCache: Episodic KV Cache Management for Long ...","url":"https://arxiv.org/pdf/2509.17396"},{"title":"Efficient and Accurate KV-cache Management for Long-Sequence LLMs | OpenReview","url":"https://openreview.net/forum?id=LaqkFgHzYi"},{"title":"Semantic Caching for LLM Inference: GPTCache, Redis Vector Cache, and Prompt Cache Setup (2026) | Spheron Blog","url":"https://www.spheron.network/blog/semantic-cache-llm-inference-gpu-cloud/"},{"title":"Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing | OpenReview","url":"https://openreview.net/forum?id=kgzBkyqg6Z"},{"title":"SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging","url":"https://arxiv.org/html/2603.14303"},{"title":"SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/html/2602.22603v1"}]

Based on the search results, here's what I found about semantic segment KV cache management in 2026:

## Key Approaches and Methods

SentenceKV is a novel sentence-level semantic KV caching approach designed to enhance inference efficiency while preserving semantic coherence. It can match full KV cache performance in perplexity and task accuracy while using as little as 3% of the full cache capacity and reducing GPU memory usage by more than 30%.

SemantiCache is a novel three-stage, semantically hierarchical pipeline that begins with semantic chunking, where the original KV cache is segmented into semantically coherent chunks using natural language delimiters as boundaries.

Another approach integrates semantic token clustering with PagedAttention, a memory-efficient paging mechanism, by clustering semantically related tokens and organizing them into a hierarchical, dynamically updateable structure.

## Production Optimization Landscape

KV optimization is the single biggest cost lever in 2026 production inference, with five technique families doing the work: paged attention, prefix caching, attention-layer compression, and KV-cache quantization, which used together collapse long-context inference cost by 4-40×.

SideQuest is a novel framework that empowers Large Reasoning Models to actively manage their own context by leveraging the model's semantic understanding of the task state to perform self-referential KV cache eviction.

These semantic segment approaches address limitations of traditional token-level methods by preserving natural linguistic boundaries and semantic relationships during cache compression.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bffc530b-ec55-4f60-8e19-22b2f561a1fd",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "020df625-f74c-48a0-84ce-c627dafd5baa",
  "sourceToolAssistantUUID": "bffc530b-ec55-4f60-8e19-22b2f561a1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T20:58:17.805Z_

Let me run a few more targeted searches to find the most directly relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "020df625-f74c-48a0-84ce-c627dafd5baa",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZMKj8hd72obaRUqBHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f99415ba-2456-445b-b3f6-5c40f9074c47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hbd7132wAk1rduNtjNJiUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6058,
      "cache_read_input_tokens": 10384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6058,
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

_source line 19 · 2026-05-10T20:58:18.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0181DPF3rXT9m9DnP5EYBDTb`</summary>

```json
{
  "query": "CodeComp structural KV cache compression agentic coding 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f99415ba-2456-445b-b3f6-5c40f9074c47",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZMKj8hd72obaRUqBHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e7e306f-885d-4cfc-9c66-473c93507169",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hbd7132wAk1rduNtjNJiUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6058,
      "cache_read_input_tokens": 10384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6058,
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

_source line 20 · 2026-05-10T20:58:19.749Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014YHjXd7Kt8hXDah1WHgXpL`</summary>

```json
{
  "query": "SideQuest model-driven KV cache long-horizon agentic reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e7e306f-885d-4cfc-9c66-473c93507169",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZMKj8hd72obaRUqBHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7461684-91c4-4091-b6d3-5d3c97d30b07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hbd7132wAk1rduNtjNJiUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6058,
      "cache_read_input_tokens": 10384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6058,
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

_source line 21 · 2026-05-10T20:58:20.226Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UGeC4NdVhHJHtQu8FSA45X`</summary>

```json
{
  "query": "\"segment-level KV cache sharing\" agentic workflow prefix barrier 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7461684-91c4-4091-b6d3-5d3c97d30b07",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZMKj8hd72obaRUqBHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9769d175-fd38-4495-9b12-7d05f8391581",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hbd7132wAk1rduNtjNJiUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6058,
      "cache_read_input_tokens": 10384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6058,
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

_source line 22 · 2026-05-10T20:58:20.748Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WZnKNi4bZmKWPheNwhDMjW`</summary>

```json
{
  "query": "SABlock semantic-aware KV cache eviction adaptive block 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9769d175-fd38-4495-9b12-7d05f8391581",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZMKj8hd72obaRUqBHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f135f718-454e-49ca-bd0f-61eb46e3b687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hbd7132wAk1rduNtjNJiUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6058,
      "cache_read_input_tokens": 10384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6058,
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

_source line 23 · 2026-05-10T20:58:20.978Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RLRZ4K5frEqPvExDEkYffs`</summary>

```json
{
  "query": "KVFlow workflow-aware prefix caching LLM agent 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f135f718-454e-49ca-bd0f-61eb46e3b687",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZMKj8hd72obaRUqBHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d69ec86a-b919-43f3-b8ae-b2f6348fda36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hbd7132wAk1rduNtjNJiUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6058,
      "cache_read_input_tokens": 10384,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6058
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 291,
          "cache_read_input_tokens": 10384,
          "cache_creation_input_tokens": 6058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6058,
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

_source line 24 · 2026-05-10T20:58:26.029Z_

<details><summary>↩ Tool result · `toolu_014YHjXd7Kt8hXDah1WHgXpL`</summary>

```text
Web search results for query: "SideQuest model-driven KV cache long-horizon agentic reasoning 2026"

Links: [{"title":"SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/html/2602.22603v1"},{"title":"[2602.22603] SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/abs/2602.22603"},{"title":"Sanjay Kariyappa's research works | Georgia Institute of Technology and other places","url":"https://www.researchgate.net/scientific-contributions/Sanjay-Kariyappa-2145271758"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Don’t Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks","url":"https://arxiv.org/html/2601.06007v2"},{"title":"KV Cache in Local AI: Why Your Agentic Setup is 90% Slower Than It Should Be | ThinkSmart.Life Research","url":"https://thinksmart.life/research/posts/kv-cache-local-inference/"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"Optimizing Inference for Long Context and Large Batch Sizes with NVFP4 KV Cache | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/"}]

Based on the search results, here's what I found about SideQuest:

SideQuest is designed for agentic workloads that require multi-step reasoning to resolve complex user queries, typically employing the ReAct framework where the model interleaves reasoning traces with external actions to progressively gather information.

SideQuest is a novel approach that leverages the Large Reasoning Model itself to perform KV cache compression by reasoning about the usefulness of tokens in its context, framing KV cache compression as an auxiliary task executed in parallel to the main reasoning task.

Evaluations using a model trained with just 215 samples show that SideQuest reduces peak token usage by up to 65% on agentic tasks with minimal degradation in accuracy, outperforming heuristic-based KV cache compression techniques.

The paper addresses a key challenge in long-horizon agentic reasoning: long-running agentic tasks such as deep research require multi-hop reasoning over information distributed across multiple webpages and documents, and the LLM context is dominated by tokens from external retrieval, causing memory usage to grow rapidly and limiting decode performance.

The paper was published in February 2026 on arXiv by Sanjay Kariyappa and G. Edward Suh.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7461684-91c4-4091-b6d3-5d3c97d30b07",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "0022b03e-6e85-4fe3-b999-fb235a5c5f73",
  "sourceToolAssistantUUID": "f7461684-91c4-4091-b6d3-5d3c97d30b07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T20:58:26.352Z_

<details><summary>↩ Tool result · `toolu_0181DPF3rXT9m9DnP5EYBDTb`</summary>

```text
Web search results for query: "CodeComp structural KV cache compression agentic coding 2025 arxiv"

Links: [{"title":"[2604.10235] CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/abs/2604.10235"},{"title":"CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/html/2604.10235"},{"title":"KVCompose: Efficient Structured KV Cache Compression with Composite Tokens","url":"https://arxiv.org/pdf/2509.05165"},{"title":"Fast KV Compaction via Attention Matching","url":"https://arxiv.org/html/2602.16284"},{"title":"[2509.05165] KVCompose: Efficient Structured KV Cache Compression with Composite Tokens","url":"https://arxiv.org/abs/2509.05165"},{"title":"KVComp: A High-Performance, LLM-Aware, Lossy Compression Framework for KV Cache","url":"https://arxiv.org/html/2509.00579v1"},{"title":"A Systematic Exploration of KV Cache Compression ...","url":"https://arxiv.org/pdf/2503.11816"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning","url":"https://arxiv.org/html/2602.22603"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"}]

I found the research paper you're looking for! Here are the key findings:

## CodeComp: Structural KV Cache Compression for Agentic Coding

CodeComp is a training-free KV cache compression framework that incorporates static program analysis into LLM inference via Code Property Graph priors extracted by Joern.

### Key Problem It Addresses

Agentic code tasks such as fault localization and patch generation across entire codebases are among the most context-demanding applications of LLMs in software engineering. While LLMs have shown strong capabilities on these tasks, efficient deployment at repository scale is constrained by the Key-Value (KV) cache, which stores intermediate attention states to avoid redundant computation but grows linearly with context length and can consume up to 70% of total GPU memory during long-context inference.

### Core Innovation

The paper addresses the limitation that attention-only compression discards structurally critical tokens such as function calls, branch predicates, and return statements, while CodeComp uses CPG priors to explicitly preserve these tokens.

### Evaluation Results

The paper evaluates two 8B-scale code language models, Llama-3-8B-Instruct and Qwen3-8B, across five benchmarks spanning two task types: for bug localization using InfiniteBench-CodeDebug, DebugBench, and LongCodeQA, and for code generation using SWE-bench Lite and the LCA library-based code generation benchmark.

The paper is available on arXiv as paper 2604.10235 and was published approximately one month ago (as of your search date).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e7e306f-885d-4cfc-9c66-473c93507169",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "a1b7420b-0fef-489a-83b3-e729ab99b0e4",
  "sourceToolAssistantUUID": "8e7e306f-885d-4cfc-9c66-473c93507169",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T20:58:27.201Z_

<details><summary>↩ Tool result · `toolu_01UGeC4NdVhHJHtQu8FSA45X`</summary>

```text
Web search results for query: ""segment-level KV cache sharing" agentic workflow prefix barrier 2026"

Links: [{"title":"Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing | OpenReview","url":"https://openreview.net/forum?id=kgzBkyqg6Z"},{"title":"TOWARDS A COLLABORATIVE MEMORY FOR AGENTIC ...","url":"https://openreview.net/pdf/c8adae36c42059677552b1255da2411e2839f58a.pdf"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://arxiv.org/html/2507.07400v1"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM- ...","url":"https://arxiv.org/pdf/2507.07400"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows | OpenReview","url":"https://openreview.net/forum?id=5Iw1nDtYmT"},{"title":"PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving","url":"https://arxiv.org/html/2602.12029v1"},{"title":"Recursion-wise KV Caching for LLMs","url":"https://www.emergentmind.com/topics/recursion-wise-kv-caching"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Introducing NVIDIA BlueField-4-Powered CMX Context Memory Storage Platform for the Next Frontier of AI | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/introducing-nvidia-bluefield-4-powered-inference-context-memory-storage-platform-for-the-next-frontier-of-ai/"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"}]

Based on the search results, here's what I found about segment-level KV cache sharing in agentic workflows with prefix barriers:

## Key Research

A novel collaborative memory approach using Segment-Level KV Cache Sharing has been introduced that decomposes the cache unit into fine-grained semantic segments, enabling agents to dynamically reuse KV cache segments generated by any other agent at arbitrary positions, without relying on sequential prefix consistency.

## Problem This Solves

Prevailing KV cache reuse methods rely heavily on a rigid prefix matching mechanism, which mandates exact equivalence between the query request and the cached prefix. This inflexible matching scheme struggles to accommodate the highly heterogeneous instruction prompt template in multi-agent environments, thereby severely constraining the overall system throughput.

## Benefits

This approach not only significantly boosts the inference efficiency of LLMs in agentic workflows but also achieves genuine working memory sharing and collaboration. Extensive experimental results demonstrate that the proposed method markedly reduces redundant computation, increases system throughput, and even improves the performance of agentic workflow on benchmark tests through effective working memory sharing.

## Implementation

The implementation is built upon the vLLM framework and leverages the PageAttention mechanism.

This represents a significant advance in making multi-agent LLM systems more efficient by breaking the traditional "prefix barrier" that required exact sequential matching of cached content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9769d175-fd38-4495-9b12-7d05f8391581",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "9dd9f4d2-dbf8-43b7-89c8-26f7c5b3bef3",
  "sourceToolAssistantUUID": "9769d175-fd38-4495-9b12-7d05f8391581",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T20:58:28.629Z_

<details><summary>↩ Tool result · `toolu_01RLRZ4K5frEqPvExDEkYffs`</summary>

```text
Web search results for query: "KVFlow workflow-aware prefix caching LLM agent 2025"

Links: [{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://arxiv.org/html/2507.07400v1"},{"title":"[2507.07400] KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://arxiv.org/abs/2507.07400"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM- ...","url":"https://arxiv.org/pdf/2507.07400"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows | OpenReview","url":"https://openreview.net/forum?id=5Iw1nDtYmT"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250707400P/abstract"},{"title":"NeurIPS Poster KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://neurips.cc/virtual/2025/poster/119883"},{"title":"(PDF) KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://www.researchgate.net/publication/393586543_KVFlow_Efficient_Prefix_Caching_for_Accelerating_LLM-Based_Multi-Agent_Workflows"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/c8adae36c42059677552b1255da2411e2839f58a.pdf"},{"title":"KV-Cache Wins You Can See: From Prefix Caching in vLLM to Distributed Scheduling with llm-d | llm-d","url":"https://llm-d.ai/blog/kvcache-wins-you-can-see"},{"title":"Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/html/2603.04428v1"}]

Based on the search results, here's what I found about KVFlow:

## Overview

KVFlow is a workflow-aware KV cache management framework tailored for agentic workloads. Large language model (LLM) based agentic workflows have become a popular paradigm for coordinating multiple specialized agents to solve complex tasks.

## The Problem It Addresses

Current systems typically evict KV caches using a Least Recently Used (LRU) policy, which fails to anticipate future agent usage and often discards KV caches shortly before their reuse, leading to frequent cache misses and substantial recomputation or swapping overhead.

## Key Technical Approaches

KVFlow abstracts the agent execution schedule as an Agent Step Graph and assigns each agent a steps-to-execution value that estimates its temporal proximity to future activation. 

Additionally, KVFlow introduces a fully overlapped KV prefetching mechanism, which proactively loads required tensors from CPU to GPU in background threads for agents scheduled in the next step, thereby avoiding cache miss stalls during generation.

## Performance Results

Compared to SGLang with hierarchical radix cache, KVFlow achieves up to 1.83× speedup for single workflows with large prompts, and up to 2.19× speedup for scenarios with many concurrent workflows.

## Implementation

KVFlow is implemented based on SGLang v0.4.4, with SGLang's backend managing the prefix KV cache using a radix tree, extended to support workflow-aware eviction policy and fully overlapped KV prefetching.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d69ec86a-b919-43f3-b8ae-b2f6348fda36",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "be73e736-7b2f-471d-8186-f057f2f51a87",
  "sourceToolAssistantUUID": "d69ec86a-b919-43f3-b8ae-b2f6348fda36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T20:58:33.731Z_

<details><summary>↩ Tool result · `toolu_01WZnKNi4bZmKWPheNwhDMjW`</summary>

```text
Web search results for query: "SABlock semantic-aware KV cache eviction adaptive block 2025"

Links: [{"title":"[2510.22556] SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size","url":"https://arxiv.org/abs/2510.22556"},{"title":"SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size","url":"https://arxiv.org/html/2510.22556"},{"title":"Adaptive KV Aggregation in LLMs","url":"https://www.emergentmind.com/topics/adaptive-kv-aggregation"},{"title":"Hierarchical Adaptive Eviction for KV Cache Management in Multimodal Language Models","url":"https://arxiv.org/html/2602.02197v1"},{"title":"DynamicKV: Task-Aware Adaptive KV Cache Compression ...","url":"https://aclanthology.org/2025.findings-emnlp.426.pdf"},{"title":"GitHub - antgroup/cakekv · GitHub","url":"https://github.com/antgroup/cakekv"},{"title":"[2503.12491] CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences","url":"https://arxiv.org/abs/2503.12491"},{"title":"KV Cache Strategies for LLM Efficiency","url":"https://www.emergentmind.com/topics/kv-cache-strategy"},{"title":"Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics","url":"https://arxiv.org/html/2603.01426"},{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"}]

I found detailed search results for SABlock. Here's what I found:

## SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size

SABlock is a semantic-aware KV cache eviction framework with adaptive block sizes.

### Overview
The growing memory footprint of the Key-Value (KV) cache poses a severe scalability bottleneck for long-context Large Language Model (LLM) inference, and while KV cache eviction has emerged as an effective solution by discarding less critical tokens, existing token-, block-, and sentence-level compression methods struggle to balance semantic coherence and memory efficiency.

### How SABlock Works
SABlock first performs semantic segmentation to align compression boundaries with linguistic structures, then applies segment-guided token scoring to refine token importance estimation. Finally, for each segment, a budget-driven search strategy adaptively determines the optimal block size that preserves semantic integrity while improving compression efficiency under a given cache budget.

### Performance Results
With a 128K context length, SABlock reduces peak memory usage by 46.28% and achieves up to 9.5× speedup.

### Publication
The paper was submitted on October 26, 2025, with authors including Jinhan Chen and others. The arXiv identifier is 2510.22556.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f135f718-454e-49ca-bd0f-61eb46e3b687",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "f3ce70ee-801d-4a4a-a7c7-f1479725ba7a",
  "sourceToolAssistantUUID": "f135f718-454e-49ca-bd0f-61eb46e3b687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-10T20:58:37.756Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MqNrdgQaf4qoASHBKVdXRT`</summary>

```json
{
  "query": "\"Don't Break the Cache\" prompt caching long-horizon agentic 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3ce70ee-801d-4a4a-a7c7-f1479725ba7a",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZNibpxoSsgfvxejr5H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8f56810-a2a0-4c8b-b1a9-8128ae6a0467",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ump3sX5K3mowUvTyAMvd4J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1024,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 16442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3971,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-10T20:58:38.135Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019ayuWb2AJUUPsQqGbTHQmg`</summary>

```json
{
  "query": "ACON context compression agent memory management 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8f56810-a2a0-4c8b-b1a9-8128ae6a0467",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZNibpxoSsgfvxejr5H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a88fb25b-60fe-42ac-a942-f329449956ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ump3sX5K3mowUvTyAMvd4J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1024,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 16442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3971,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T20:58:38.753Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QmcNaqFuzSLpbY2AhA3Lq9`</summary>

```json
{
  "query": "CCF context compression framework segment semantic aggregation KV 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a88fb25b-60fe-42ac-a942-f329449956ee",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZNibpxoSsgfvxejr5H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "426638cd-010d-4f49-ba80-19e0a3d20ee3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ump3sX5K3mowUvTyAMvd4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1024,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 16442,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3971
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1024,
          "output_tokens": 163,
          "cache_read_input_tokens": 16442,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3971,
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

_source line 32 · 2026-05-10T20:58:45.492Z_

<details><summary>↩ Tool result · `toolu_01QmcNaqFuzSLpbY2AhA3Lq9`</summary>

```text
Web search results for query: "CCF context compression framework segment semantic aggregation KV 2025"

Links: [{"title":"CCF: A Context Compression Framework for Efficient Long-Sequence Language Modeling","url":"https://arxiv.org/html/2509.09199v1"},{"title":"[2509.09199] CCF: A Context Compression Framework for Efficient Long-Sequence Language Modeling","url":"https://arxiv.org/abs/2509.09199"},{"title":"CCF: A Context Compression Framework for Efficient Long-Sequence Language","url":"https://www.arxiv.org/pdf/2509.09199"},{"title":"Context Compression Framework Overview","url":"https://www.emergentmind.com/topics/context-compression-framework"},{"title":"(PDF) CCF: A Context Compression Framework for Efficient Long-Sequence Language Modeling","url":"https://www.researchgate.net/publication/395418146_CCF_A_Context_Compression_Framework_for_Efficient_Long-Sequence_Language_Modeling"},{"title":"[2502.00299] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://arxiv.org/abs/2502.00299"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=20JDhbJqn3"},{"title":"SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging","url":"https://arxiv.org/html/2603.14303"},{"title":"Efficient LLM inference via sentence-level semantic KV ...","url":"https://arxiv.org/pdf/2504.00970"},{"title":"NeurIPS Poster ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://neurips.cc/virtual/2025/poster/120181"}]

Based on the search results, I found detailed information about CCF (Context Compression Framework):

## CCF: Context Compression Framework

CCF is a Context Compression Framework designed to address the efficiency challenges of long-sequence language models. 

### Key Technical Approach

CCF integrates segment-wise semantic aggregation with key-value memory encoding, forming compact representations that support accurate reconstruction and long-range understanding. More specifically, tokens are processed by a lightweight encoder that aggregates local semantic representations through attention to produce a compact summary of each segment, and these condensed segment representations are then projected into a shared latent space and integrated into the language model's decoder as key-value caches.

### Performance and Efficiency

CCF significantly improves throughput and reduces KV cache size compared to the baseline, especially at longer context lengths. Empirical results on multiple long-context language modeling benchmarks demonstrate that CCF achieves competitive perplexity under high compression ratios, and significantly improves throughput and memory efficiency compared to existing approaches.

### Optimization Strategy

To further enhance scalability, CCF introduces a training-efficient optimization strategy that couples incremental segment decoding with sparse reservoir sampling, substantially reducing memory overhead without degrading performance.

The paper appears to be under review for AAAI 2026 and was initially released on arXiv in September 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "426638cd-010d-4f49-ba80-19e0a3d20ee3",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "4a3184a2-18df-49c5-b32d-b81b2b85650b",
  "sourceToolAssistantUUID": "426638cd-010d-4f49-ba80-19e0a3d20ee3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T20:58:45.783Z_

<details><summary>↩ Tool result · `toolu_019ayuWb2AJUUPsQqGbTHQmg`</summary>

```text
Web search results for query: "ACON context compression agent memory management 2025"

Links: [{"title":"[2510.00615] ACON: Optimizing Context Compression for Long-horizon LLM Agents","url":"https://arxiv.org/abs/2510.00615"},{"title":"Acon: Optimizing Context Compression for Long-horizon LLM Agents","url":"https://arxiv.org/html/2510.00615v1"},{"title":"AI Agent Context Compression: Strategies for Long-Running Sessions | Zylos Research","url":"https://zylos.ai/research/2026-02-28-ai-agent-context-compression-strategies"},{"title":"ACON: Optimizing Context Compression for Long-horizon LLM Agents | OpenReview","url":"https://openreview.net/forum?id=7JbSwX6bNL"},{"title":"ACON: OPTIMIZING CONTEXT COMPRESSION FOR LONG-HORIZON LLM AGENTS Minki Kang1∗","url":"https://arxiv.org/pdf/2510.00615"},{"title":"Paper page - ACON: Optimizing Context Compression for Long-horizon LLM Agents","url":"https://huggingface.co/papers/2510.00615"},{"title":"[2510.00615v1] ACON: Optimizing Context Compression for Long-horizon LLM Agents","url":"https://arxiv.org/abs/2510.00615v1"},{"title":"ACON: Optimizing Context Compression for Long-horizon LLM Agents - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251000615K/abstract"},{"title":"GitHub - TsinghuaC3I/Awesome-Memory-for-Agents: A Collection of Papers about Memory for Language Agents · GitHub","url":"https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents"},{"title":"ACON: OPTIMIZING CONTEXT COMPRESSION FOR ...","url":"https://openreview.net/pdf?id=7JbSwX6bNL"}]

## Search Results Summary

I found comprehensive information about ACON (Agent Context Optimization) and context compression for LLM agents. Here are the key findings:

### Overview of ACON

ACON is a unified framework that optimally compresses both environment observations and interaction histories into concise yet informative condensations. A central challenge for agentic tasks is the growing context length, as agents must accumulate long histories of actions and observations.

### How ACON Works

ACON leverages compression guideline optimization in natural language space: given paired trajectories where full context succeeds but compressed context fails, capable LLMs analyze the causes of failure, and the compression guideline is updated accordingly. ACON is gradient-free — no fine-tuning required, compatible with any API-accessible model.

### Performance Results

ACON reduces memory usage by 26-54% (peak tokens) while largely preserving task performance, preserves over 95% of accuracy when distilled into smaller compressors, and enhances smaller LMs as long-horizon agents with up to 46% performance improvement. The framework was validated on three multi-step agent benchmarks: AppWorld, OfficeBench, and Multi-objective QA, each requiring 15+ interaction steps.

### Distillation and Deployment

The optimized LLM compressor is distilled into smaller models to reduce the overhead of the additional module, making it cost-efficient for production deployment.

### Industry Context

In 2025–2026, the field has converged on a set of concrete compression techniques: anchored iterative summarization, failure-driven guideline optimization (ACON), and provider-native compaction APIs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a88fb25b-60fe-42ac-a942-f329449956ee",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "2eba30d6-8255-423f-a7de-271f6916744f",
  "sourceToolAssistantUUID": "a88fb25b-60fe-42ac-a942-f329449956ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T20:58:48.484Z_

<details><summary>↩ Tool result · `toolu_01MqNrdgQaf4qoASHBKVdXRT`</summary>

```text
Web search results for query: ""Don't Break the Cache" prompt caching long-horizon agentic 2026"

Links: [{"title":"Don’t Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks","url":"https://arxiv.org/html/2601.06007v2"},{"title":"[2601.06007] Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks","url":"https://arxiv.org/abs/2601.06007"},{"title":"Don’t Break the Cache: An Evaluation of Prompt Caching","url":"https://arxiv.org/pdf/2601.06007"},{"title":"Prompt Caching in LLMs! - by Avi Chawla","url":"https://blog.dailydoseofds.com/p/prompt-caching-in-llms"},{"title":"How We Cut LLM Costs by 59% With Prompt Caching — ProjectDiscovery Blog","url":"https://projectdiscovery.io/blog/how-we-cut-llm-cost-with-prompt-caching"},{"title":"Prompt caching - Claude API Docs","url":"https://platform.claude.com/docs/en/build-with-claude/prompt-caching"},{"title":"Prompt Caching","url":"https://www.aussieai.com/research/prompt-caching"},{"title":"Prompt Caching for AI Agents: How to Cut Cost and Latency Without Breaking Context | by Anna Jey | Apr, 2026 | Medium","url":"https://medium.com/@arvisionlab/prompt-caching-for-ai-agents-how-to-cut-cost-and-latency-without-breaking-context-245dc2502b4b"},{"title":"Prompt caching - OpenClaw","url":"https://docs.openclaw.ai/reference/prompt-caching"},{"title":"What Is Prompt Caching? LLM Speed & Cost Guide","url":"https://redis.io/blog/what-is-prompt-caching/"}]

Based on the search results, here's what I found about "Don't Break the Cache":

## Overview

"Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks" is the first comprehensive evaluation of prompt caching for long-horizon agentic tasks across three major LLM providers.

## Key Findings

The research demonstrates significant benefits from prompt caching:

- Prompt caching reduces API costs by 41 to 80% and improves TTFT (time to first token) by 13 to 31%.

## Methodology

The evaluation compares three caching strategies across three major LLM providers (OpenAI, Anthropic, and Google): full context caching, system prompt only caching, and caching that excludes dynamic tool results. The evaluation uses DeepResearch Bench, a multi-turn agentic benchmark where agents autonomously execute real-world web search tool calls to answer complex research questions.

## Critical Insight

Strategic cache boundary control, such as caching only system prompts while excluding dynamic tool results, provides more consistent benefits than naive full context caching, which can paradoxically increase latency.

The paper was published on January 31, 2026, and offers actionable guidance for deploying prompt caching in production agentic systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8f56810-a2a0-4c8b-b1a9-8128ae6a0467",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "974a7b2f-bf7f-4622-8667-509d88ea8b0f",
  "sourceToolAssistantUUID": "c8f56810-a2a0-4c8b-b1a9-8128ae6a0467",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-10T20:58:52.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Q57Y1jDgvXFs6ptZemLEz`</summary>

```json
{
  "query": "ChunkKV semantic-preserving KV cache compression chunk-level NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "974a7b2f-bf7f-4622-8667-509d88ea8b0f",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZPofCkQhNtapXitB3E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "549ba603-29b4-44bc-b349-27f3b0612da3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CxYvifUHgNP4t8bz9Pv91",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1785,
      "cache_creation_input_tokens": 2035,
      "cache_read_input_tokens": 20413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2035,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-10T20:58:52.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WwfyEsXeDo9sTt75LREKXc`</summary>

```json
{
  "query": "SemantiCache semantic chunking clustered merging KV cache 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "549ba603-29b4-44bc-b349-27f3b0612da3",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZPofCkQhNtapXitB3E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a104350-bdc9-4071-b5c7-a6366d65e4b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CxYvifUHgNP4t8bz9Pv91",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1785,
      "cache_creation_input_tokens": 2035,
      "cache_read_input_tokens": 20413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2035,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-10T20:58:53.170Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WsRUQCpzrG99YnPZXYYaGc`</summary>

```json
{
  "query": "generation phase aware dynamic sparsity attention LLM prefill decode 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a104350-bdc9-4071-b5c7-a6366d65e4b7",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZPofCkQhNtapXitB3E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1c56f44-3e1e-420f-a91c-cb4fc87cbe49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CxYvifUHgNP4t8bz9Pv91",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1785,
      "cache_creation_input_tokens": 2035,
      "cache_read_input_tokens": 20413,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2035
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1785,
          "output_tokens": 178,
          "cache_read_input_tokens": 20413,
          "cache_creation_input_tokens": 2035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2035,
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

_source line 38 · 2026-05-10T20:58:56.628Z_

<details><summary>↩ Tool result · `toolu_013Q57Y1jDgvXFs6ptZemLEz`</summary>

```text
Web search results for query: "ChunkKV semantic-preserving KV cache compression chunk-level NeurIPS 2025"

Links: [{"title":"ChunkKV: Semantic-Preserving KV Cache Compression ...","url":"https://neurips.cc/media/neurips-2025/Slides/120181.pdf"},{"title":"[2502.00299] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://arxiv.org/abs/2502.00299"},{"title":"NeurIPS Poster ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://neurips.cc/virtual/2025/poster/120181"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=20JDhbJqn3"},{"title":"ChunkKV: Semantic-Preserving KV Cache","url":"https://papers.neurips.cc/paper_files/paper/2025/file/2987f911151b39cd3a1761e212319e8e-Paper-Conference.pdf"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference - The Hong Kong University of Science and Technology","url":"https://researchportal.hkust.edu.hk/en/publications/chunkkv-semantic-preserving-kv-cache-compression-for-efficient-lo/"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://arxiv.org/html/2502.00299v5"},{"title":"Efficient LLMs at Scale: My NeurIPS Week in KV Caches, Spec Decoding, and FP4","url":"https://kaitchup.substack.com/p/efficient-llms-at-scale-my-neurips"},{"title":"[2502.00299v5] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://arxiv.org/abs/2502.00299v5"},{"title":"[PDF] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ef094815dc0118c8d1cc06d4bb3aa78bae0a3877"}]

I found comprehensive information about ChunkKV. Here's what the search reveals:

## Overview

ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference was presented at NeurIPS 2025.

## The Problem and Solution

Large Language Models (LLMs) require significant GPU memory when processing long texts, with the key value (KV) cache consuming up to 70% of total memory during inference. Although existing compression methods reduce memory by evaluating the importance of individual tokens, they overlook critical semantic relationships between tokens, resulting in fragmented context and degraded performance.

ChunkKV fundamentally reimagines KV cache compression by treating semantic chunks - rather than isolated tokens - as basic compression units. This approach preserves complete linguistic structures and contextual integrity, ensuring that essential meaning is retained even under aggressive compression.

## Key Technical Innovations

The approach includes a novel layer-wise index reuse technique that exploits the higher cross-layer similarity of preserved indices in ChunkKV, reducing computational overhead and improving throughput by 26.5%.

## Experimental Results

Comprehensive evaluations on challenging benchmarks: LongBench, Needle-In-A-HayStack, GSM8K, and JailbreakV demonstrate that ChunkKV outperforms state-of-the-art methods by up to 8.7% in precision while maintaining the same compression ratio.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "549ba603-29b4-44bc-b349-27f3b0612da3",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "f651750d-b903-4841-b439-9b18719d3e04",
  "sourceToolAssistantUUID": "549ba603-29b4-44bc-b349-27f3b0612da3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T20:58:58.853Z_

<details><summary>↩ Tool result · `toolu_01WwfyEsXeDo9sTt75LREKXc`</summary>

```text
Web search results for query: "SemantiCache semantic chunking clustered merging KV cache 2026"

Links: [{"title":"[2603.14303] SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging","url":"https://arxiv.org/abs/2603.14303"},{"title":"SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging","url":"https://arxiv.org/html/2603.14303"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=20JDhbJqn3"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://arxiv.org/html/2502.00299v5"},{"title":"[2502.00299] ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://arxiv.org/abs/2502.00299"},{"title":"ClusterKV: Manipulating LLM KV Cache in Semantic Space for Recallable Compression | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11132479/"},{"title":"Efficient LLM inference via sentence-level semantic KV ...","url":"https://arxiv.org/pdf/2504.00970"},{"title":"SentenceKV: Efficient LLM Inference via Sentence-Level Semantic KV CachingCode available at https://github.com/zzbright1998/SentenceKV","url":"https://arxiv.org/html/2504.00970"},{"title":"How to Build Semantic Chunking","url":"https://oneuptime.com/blog/post/2026-01-30-semantic-chunking/view"},{"title":"SentenceKV: Efficient LLM Inference via Sentence-Level Semantic KV Caching","url":"https://arxiv.org/html/2504.00970v1"}]

Based on the search results, I found information about SemantiCache and related semantic KV cache compression techniques:

## SemantiCache Overview

SemantiCache is a novel compression framework that preserves semantic integrity by aligning the compression process with the semantic hierarchical nature of language.

## How SemantiCache Works

The approach uses a three-stage pipeline:

1. **Semantic Chunking**: The cache is partitioned into semantically coherent chunks by delimiters, which are natural semantic boundaries.

2. **Clustering**: Within each chunk, a computationally efficient Greedy Seed-Based Clustering (GSC) algorithm groups tokens into semantic clusters.

3. **Clustered Merging**: These clusters are further merged into semantic cores, enhanced by a Proportional Attention mechanism that rebalances the reduced attention contributions of the merged tokens.

## Performance Results

SemantiCache accelerates the decoding stage of inference by up to 2.61 times and substantially reduces memory footprint, while maintaining performance comparable to the original model.

## Motivation

Existing KV cache compression methods generally operate on discrete tokens or non-semantic chunks. However, such approaches often lead to semantic fragmentation, where linguistically coherent units are disrupted, causing irreversible information loss and degradation in model performance.

The paper was published on arXiv on March 15, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a104350-bdc9-4071-b5c7-a6366d65e4b7",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "37cdc43b-f093-479c-8737-08025bb1ff39",
  "sourceToolAssistantUUID": "2a104350-bdc9-4071-b5c7-a6366d65e4b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T20:59:00.330Z_

<details><summary>↩ Tool result · `toolu_01WsRUQCpzrG99YnPZXYYaGc`</summary>

```text
Web search results for query: "generation phase aware dynamic sparsity attention LLM prefill decode 2025 2026"

Links: [{"title":"BLASST: DYNAMIC BLOCKED ATTENTION SPARSITY VIA SOFTMAX THRESHOLDING","url":"https://arxiv.org/pdf/2512.12087"},{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient ...","url":"https://aclanthology.org/2025.findings-acl.131.pdf"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"A Systematic Characterization of LLM Inference on GPUs","url":"https://www.arxiv.org/pdf/2512.01644"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=qBpYqQUFPx"},{"title":"FlashInfer: Efficient and Customizable Attention Engine for ...","url":"https://homes.cs.washington.edu/~arvind/papers/flashinfer.pdf"},{"title":"Accelerating Long Context Length LLM Inference","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/2025.acl-long.1568.pdf"},{"title":"MInference: Accelerating Pre-filling for Long-Context LLMs via Dynamic","url":"https://openreview.net/pdf/a4381abee166ed1f0b5031a25f70300889585579.pdf"},{"title":"DUETSERVE: HARMONIZING PREFILL AND DECODE FOR LLM SERVING","url":"https://arxiv.org/pdf/2511.04791"},{"title":"KASCADE: A PRACTICAL SPARSE ATTENTION METHOD FOR LONG-CONTEXT LLM INFERENCE","url":"https://arxiv.org/pdf/2512.16391"}]

Based on the web search results, I found several relevant papers and research on generation phase-aware dynamic sparsity attention for LLM prefill and decode from 2025-2026:

## Key Findings:

**Recent Methods (2025-2026):**

1. **BLASST**: A dynamic blocked attention sparsity method via softmax thresholding that prunes the attention matrix without pre-computation or proxy scores, applicable to both prefill and decode stages across all attention variants.

2. **RaaS (Reasoning-Aware Attention Sparsity)**: A method for efficient LLM reasoning that appears to be generation-phase aware.

3. **The Sparse Frontier**: A comprehensive benchmarking study of content-aware sparse attention methods that represent diverse strategies in terms of units, budget allocation, and KV cache management.

4. **Kascade**: A practical sparse attention method that leverages the fact that post-softmax attention is intrinsically sparse and that the identity of high-weight keys is stable across nearby layers, computing exact Top-k indices in anchor layers then reusing those indices.

## Key Phase-Specific Insights:

The inference process naturally decomposes into two distinct phases, with phase-aware parallelization strategies showing different bottlenecks.

BLASST achieves a 1.48× speedup for decode at 73.2% sparsity on modern GPUs, demonstrating practical efficiency gains.

These methods represent the current frontier in generation-phase aware dynamic sparsity for efficient LLM inference during both prefill and decode phases in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1c56f44-3e1e-420f-a91c-cb4fc87cbe49",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "9a759c24-77ef-4959-8c3d-e913c8b5604c",
  "sourceToolAssistantUUID": "a1c56f44-3e1e-420f-a91c-cb4fc87cbe49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-10T20:59:03.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EsAo3XJDx13imotxWso55M`</summary>

```json
{
  "query": "EpiCache episodic KV cache management long context conversation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a759c24-77ef-4959-8c3d-e913c8b5604c",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZQgKTcbozwcxZZsYcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27ca89b3-94ce-42e1-a840-adabd2ae08bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Puy4vmcwZxrCDytVxuXr8i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4795,
      "cache_read_input_tokens": 22448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4795,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-10T20:59:04.290Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014idwzYmqGAbZQVBU1h4a2b`</summary>

```json
{
  "query": "MInference dynamic sparse attention prefill long context 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27ca89b3-94ce-42e1-a840-adabd2ae08bf",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZQgKTcbozwcxZZsYcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e960b448-dbec-4960-b5b5-6083f0847232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Puy4vmcwZxrCDytVxuXr8i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4795,
      "cache_read_input_tokens": 22448,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4795
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 22448,
          "cache_creation_input_tokens": 4795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4795,
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

_source line 43 · 2026-05-10T20:59:10.473Z_

<details><summary>↩ Tool result · `toolu_01EsAo3XJDx13imotxWso55M`</summary>

```text
Web search results for query: "EpiCache episodic KV cache management long context conversation 2025"

Links: [{"title":"[2509.17396] EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://arxiv.org/abs/2509.17396"},{"title":"Paper page - EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://huggingface.co/papers/2509.17396"},{"title":"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/epicache"},{"title":"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://arxiv.org/html/2509.17396v1"},{"title":"EpiCache: Episodic KV Cache Management for Long ...","url":"https://arxiv.org/pdf/2509.17396"},{"title":"(PDF) EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://www.researchgate.net/publication/395724682_EpiCache_Episodic_KV_Cache_Management_for_Long_Conversational_Question_Answering"},{"title":"EpiCache: Episodic KV Cache for LongConvQA","url":"https://www.emergentmind.com/topics/epicache"},{"title":"GitHub - apple/ml-epicache","url":"https://github.com/apple/ml-epicache"},{"title":"EPICACHE: EPISODIC KV CACHE MANAGEMENT FOR ...","url":"https://openreview.net/pdf/49f7bca77eef6e14a14787a3c09771b58b20e6c7.pdf"},{"title":"[Literature Review] EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://www.themoonlight.io/en/review/epicache-episodic-kv-cache-management-for-long-conversational-question-answering"}]

Based on the search results, here's what I found about EpiCache:

## Overview

EpiCache is a training-free KV cache management framework for long conversational question answering (LongConvQA) under fixed memory budgets.

## Key Innovation

EpiCache bounds cache growth through block-wise prefill and preserves topic-relevant context via episodic KV compression, which clusters conversation history into coherent episodes and applies episode-specific KV cache eviction.

## Problem It Solves

Key-Value (KV) caching's memory grows linearly with dialogue length and quickly becomes the bottleneck in resource-constrained environments. Existing methods face two major limitations: (i) evicting the KV cache after full-context prefill causes unbounded peak memory, and (ii) query-dependent eviction narrows the cache to a single query, leading to failure cases in multi-turn conversations.

## Technical Approach

The framework includes an adaptive layer-wise budget allocation strategy that measures each layer's sensitivity to eviction and distributes the memory budget across layers accordingly.

## Performance Results

Across three LongConvQA benchmarks, EpiCache improves accuracy by up to 40%, maintains near-full KV accuracy under 4-6x compression, and reduces latency/memory by up to 2.4x/3.5x, enabling efficient multi-turn interaction under strict resource limits.

The paper was published in September 2025, with the code available on GitHub through Apple's ML-EpiCache repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27ca89b3-94ce-42e1-a840-adabd2ae08bf",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "206b7da1-74a6-4ea8-acd3-8e4f069df30c",
  "sourceToolAssistantUUID": "27ca89b3-94ce-42e1-a840-adabd2ae08bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T20:59:13.252Z_

<details><summary>↩ Tool result · `toolu_014idwzYmqGAbZQVBU1h4a2b`</summary>

```text
Web search results for query: "MInference dynamic sparse attention prefill long context 2025"

Links: [{"title":"MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention | OpenReview","url":"https://openreview.net/forum?id=fPBACAbqSN"},{"title":"[2407.02490] MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention","url":"https://arxiv.org/abs/2407.02490"},{"title":"GitHub - microsoft/MInference: [NeurIPS'24 Spotlight, ICLR'25, ICML'25] To speed up Long-context LLMs' inference, approximate and dynamic sparse calculate the attention, which reduces inference latency by up to 10x for pre-filling on an A100 while maintaining accuracy. · GitHub","url":"https://github.com/microsoft/MInference"},{"title":"Accelerating Pre-filling for Long-Context LLMs via Dynamic ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/5dfbe6f5671e82c76841ba687a8a9ecb-Paper-Conference.pdf"},{"title":"MMInference: Accelerating Pre-filling for Long-Context Visual Language Models via Modality-Aware Permutation Sparse Attention","url":"https://arxiv.org/html/2504.16083v1"},{"title":"ICML Poster MMInference: Accelerating Pre-filling for Long-Context Visual Language Models via Modality-Aware Permutation Sparse Attention","url":"https://icml.cc/virtual/2025/poster/44144"},{"title":"MInference: Accelerating Pre-filling for Long-Context LLMs via Dynamic","url":"https://openreview.net/pdf/a4381abee166ed1f0b5031a25f70300889585579.pdf"},{"title":"NeurIPS Poster MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention","url":"https://neurips.cc/virtual/2024/poster/94208"},{"title":"MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention","url":"https://arxiv.org/html/2407.02490v1"},{"title":"UniPrefill: Universal Long-Context Prefill Acceleration via Block-wise Dynamic Sparsification","url":"https://arxiv.org/html/2605.06221"}]

Based on my search results, here's what I found about MInference and dynamic sparse attention for long-context LLMs:

## MInference 1.0 Overview

MInference (Milliontokens Inference) is a sparse calculation method designed to accelerate pre-filling of long-sequence processing. Published in September 2024, it was a NeurIPS 2024 spotlight paper and has also been accepted at ICLR'25 and ICML'25.

## Key Technical Approach

The method identifies three unique patterns in long-context attention matrices—the A-shape, Vertical-Slash, and Block-Sparse—that can be leveraged for efficient sparse computation on GPUs. It determines the optimal pattern for each attention head offline and dynamically builds sparse indices based on the assigned pattern during inference.

With the pattern and sparse indices, efficient sparse attention calculations are performed via optimized GPU kernels to significantly reduce the latency in the pre-filling stage of long-context LLMs.

## Performance Results

MInference speeds up the pre-filling stage by up to 10× for 1M contexts with LLaMA-3-8B on a single A100, reducing latency from 30 minutes to 3 minutes per prompt, while maintaining or improving accuracy.

## Recent Extensions (2025)

Recent work has extended MInference concepts. MMInference, a dynamic sparse attention method that accelerates the prefilling stage for long-context multi-modal inputs, achieves speedups of over 8× on million-token-long inputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e960b448-dbec-4960-b5b5-6083f0847232",
  "isSidechain": true,
  "promptId": "9675c8d9-c066-4a51-852b-884e868d9748",
  "agentId": "ad767beca5f4ce1e6",
  "type": "user",
  "uuid": "fc474690-f805-4559-843a-e6f64b4064ae",
  "sourceToolAssistantUUID": "e960b448-dbec-4960-b5b5-6083f0847232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-10T21:00:16.593Z_

I now have comprehensive results. Here is my consolidated report:

---

## Literature Search Results: KV Cache Compression / Sparse Attention for Agent/Tool-Calling Workloads (2025-2026)

Below are the most relevant papers and systems that SegAttn's proposal should be aware of, organized by how directly they challenge or overlap with its claims.

---

### HIGHLY RELEVANT -- Directly overlapping with SegAttn's core claims

**1. "Towards a Collaborative Memory for Agentic Workflow: Breaking the Prefix Barrier with Segment-Level KV Cache Sharing"**
- Venue: OpenReview (under review, likely ICML or NeurIPS 2026)
- Date: 2026
- Relevance: **Directly uses segment-level KV cache decomposition for agentic workflows.** Decomposes cache into fine-grained semantic segments, enabling agents to reuse segments at arbitrary positions without prefix consistency. Implements on vLLM with PagedAttention. This is the closest prior work to SegAttn's segment-role boundary idea -- it segments by semantic role and enables cross-agent sharing.
- URL: https://openreview.net/forum?id=kgzBkyqg6Z

**2. CodeComp: Structural KV Cache Compression for Agentic Coding**
- Venue: arXiv 2604.10235 (April 2026)
- Relevance: **Training-free KV cache compression specifically for agentic coding workloads.** Uses structural priors (Code Property Graphs) to define segment boundaries and protect structurally critical tokens from eviction. Applies structure-aware budget allocation per segment. Directly addresses agent workloads with segment-aware compression, though its segments are code-structural rather than role-based.
- URL: https://arxiv.org/abs/2604.10235

**3. SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning**
- Venue: arXiv 2602.22603 (February 2026)
- Authors: Sanjay Kariyappa, G. Edward Suh
- Relevance: **The model itself performs KV cache compression as an auxiliary reasoning task during agentic workloads.** Reduces peak token usage by 65% on agentic tasks. Directly targets tool-calling/ReAct workflows. While not role-boundary-based, it is generation-phase-aware (compression happens dynamically during generation).
- URL: https://arxiv.org/abs/2602.22603

**4. SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size**
- Venue: arXiv 2510.22556 (October 2025)
- Relevance: **Performs semantic segmentation then segment-guided token scoring, with adaptive block sizes per segment.** Very close to SegAttn's segment-boundary-aware approach. Reduces peak memory by 46.28% and achieves up to 9.5x speedup at 128K context. The key difference is SABlock segments by linguistic structure, not by role (system/tool/user).
- URL: https://arxiv.org/abs/2510.22556

**5. KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows**
- Venue: NeurIPS 2025 (arXiv 2507.07400)
- Relevance: **Workflow-aware KV cache eviction for multi-agent systems.** Uses an "Agent Step Graph" abstraction to assign eviction priorities at the cache-node level based on agent execution schedules. Achieves up to 2.19x speedup. Directly targets agent workloads with structured, workflow-aware caching rather than LRU.
- URL: https://arxiv.org/abs/2507.07400

**6. EpiCache: Episodic KV Cache Management for Long Conversational QA**
- Venue: arXiv 2509.17396 (September 2025), Apple Research
- Relevance: **Clusters conversation history into coherent "episodes" and applies episode-specific KV cache eviction.** This is conceptually similar to SegAttn's conversation-history segmentation. Achieves near-full accuracy under 4-6x compression. Includes adaptive layer-wise budget allocation.
- URL: https://arxiv.org/abs/2509.17396

---

### MODERATELY RELEVANT -- Overlap with specific components

**7. SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging**
- Venue: arXiv 2603.14303 (March 2026)
- Relevance: Three-stage pipeline: semantic chunking by natural delimiters, clustering within chunks, then merging. Up to 2.61x decode speedup. Shares SegAttn's principle of aligning compression boundaries with semantic structure.
- URL: https://arxiv.org/abs/2603.14303

**8. ChunkKV: Semantic-Preserving KV Cache Compression**
- Venue: NeurIPS 2025
- Relevance: Treats semantic chunks as compression units rather than individual tokens. Outperforms token-level methods by 8.7% at same compression ratio. Relevant to SegAttn's chunk-level (segment-level) treatment of the cache.
- URL: https://arxiv.org/abs/2502.00299

**9. SentenceKV: Sentence-Level Semantic KV Caching**
- Venue: OpenReview (2025-2026)
- Relevance: Sentence-level semantic caching that matches full KV performance using only 3% of cache capacity. Demonstrates the power of semantic-unit-level cache management.
- URL: https://openreview.net/forum?id=HyPeYU9JR6

**10. CCF: A Context Compression Framework for Efficient Long-Sequence Language Modeling**
- Venue: arXiv 2509.09199 (September 2025, under review AAAI 2026)
- Relevance: Integrates **segment-wise semantic aggregation** with KV memory encoding. Projects condensed segment representations into KV caches. Directly demonstrates segment-level compression for KV caches.
- URL: https://arxiv.org/abs/2509.09199

**11. ACON: Optimizing Context Compression for Long-horizon LLM Agents**
- Venue: arXiv 2510.00615 (October 2025), OpenReview
- Relevance: Context compression framework specifically for long-horizon agents. Reduces peak tokens by 26-54%. Uses failure-driven guideline optimization. Operates at the prompt level rather than KV/attention level, but targets the same agent-workload memory problem.
- URL: https://arxiv.org/abs/2510.00615

**12. "Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks"**
- Venue: arXiv 2601.06007 (January 2026)
- Relevance: Evaluates prompt caching strategies for agents, finding that **caching only system prompts while excluding dynamic tool results** provides more consistent benefits. This cache-boundary insight aligns with SegAttn's role-boundary-aware approach.
- URL: https://arxiv.org/abs/2601.06007

---

### RELEVANT -- Phase-aware / dynamic sparsity (non-agent-specific)

**13. BLASST: Dynamic Blocked Attention Sparsity via Softmax Thresholding**
- Venue: arXiv 2512.12087 (December 2025)
- Relevance: Dynamic sparsity applicable to both prefill and decode phases without proxy scores. 1.48x decode speedup at 73.2% sparsity. Relevant to SegAttn's "generation-phase-aware dynamic sparsity" claim.
- URL: https://arxiv.org/pdf/2512.12087

**14. MInference 1.0: Accelerating Pre-filling via Dynamic Sparse Attention**
- Venue: NeurIPS 2024 Spotlight, extended to ICLR 2025, ICML 2025
- Relevance: Identifies per-head sparse patterns (A-shape, Vertical-Slash, Block-Sparse) and dynamically builds sparse indices during prefill. Up to 10x prefill speedup. Establishes that phase-specific sparse attention is practical at scale.
- URL: https://arxiv.org/abs/2407.02490

**15. Native Sparse Attention (NSA)**
- Venue: ACL 2025
- Relevance: Hardware-aligned, natively trainable sparse attention achieving substantial speedups on 64k sequences. Demonstrates end-to-end training with sparse attention.
- URL: https://aclanthology.org/2025.acl-long.1126/

---

### Assessment of SegAttn's Novelty Claims

Based on this search, SegAttn's claim of being "the first method combining segment-role boundaries with generation-phase-aware dynamic sparsity" faces several challenges:

1. **Segment-level KV cache for agents** is addressed by the "Collaborative Memory" paper (OpenReview 2026) which explicitly decomposes KV caches into semantic segments for agentic workflows.

2. **Structural/semantic segmentation for KV compression** is well-explored: SABlock, ChunkKV, SemantiCache, CCF, and SentenceKV all segment by semantic boundaries.

3. **Agent-workload-specific KV compression** is directly tackled by CodeComp (code agents), SideQuest (reasoning agents), KVFlow (multi-agent workflows), and EpiCache (conversational agents).

4. **Phase-aware dynamic sparsity** is explored by BLASST, MInference, and Kascade.

However, the specific combination of (a) role-based boundaries (system prompt / tool schemas / conversation history / tool outputs) with (b) per-phase dynamic sparsity at the attention level appears to still be a gap. No single paper found combines ALL of these elements simultaneously. The "Collaborative Memory" paper comes closest on the segmentation side, while SideQuest comes closest on the dynamic agent-aware compression side.

---

Sources:
- [Collaborative Memory: Segment-Level KV Cache Sharing](https://openreview.net/forum?id=kgzBkyqg6Z)
- [CodeComp: Structural KV Cache Compression for Agentic Coding](https://arxiv.org/abs/2604.10235)
- [SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning](https://arxiv.org/abs/2602.22603)
- [SABlock: Semantic-Aware KV Cache Eviction](https://arxiv.org/abs/2510.22556)
- [KVFlow: Workflow-Aware Prefix Caching for Multi-Agent](https://arxiv.org/abs/2507.07400)
- [EpiCache: Episodic KV Cache Management](https://arxiv.org/abs/2509.17396)
- [SemantiCache: Semantic Chunking and Clustered Merging](https://arxiv.org/abs/2603.14303)
- [ChunkKV: Semantic-Preserving KV Cache Compression (NeurIPS 2025)](https://arxiv.org/abs/2502.00299)
- [SentenceKV: Sentence-Level Semantic KV Caching](https://openreview.net/forum?id=HyPeYU9JR6)
- [CCF: Context Compression Framework](https://arxiv.org/abs/2509.09199)
- [ACON: Context Compression for Long-horizon Agents](https://arxiv.org/abs/2510.00615)
- [Don't Break the Cache: Prompt Caching for Agentic Tasks](https://arxiv.org/abs/2601.06007)
- [BLASST: Dynamic Blocked Attention Sparsity](https://arxiv.org/pdf/2512.12087)
- [MInference: Dynamic Sparse Attention](https://arxiv.org/abs/2407.02490)
- [Native Sparse Attention (ACL 2025)](https://aclanthology.org/2025.acl-long.1126/)
- [KV Cache Optimization 2026 Guide](https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc474690-f805-4559-843a-e6f64b4064ae",
  "isSidechain": true,
  "agentId": "ad767beca5f4ce1e6",
  "requestId": "req_011CauZRdaHoBc61qp2i6PBn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9cd9b8be-aea2-4b6a-9a3e-98f92b224199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d91b6641-7766-46ec-8211-66f280f961a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJ3DqRuXhj7AvJFGmZycUi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2061,
      "cache_read_input_tokens": 27243,
      "output_tokens": 3053,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2061
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3053,
          "cache_read_input_tokens": 27243,
          "cache_creation_input_tokens": 2061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2061,
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
