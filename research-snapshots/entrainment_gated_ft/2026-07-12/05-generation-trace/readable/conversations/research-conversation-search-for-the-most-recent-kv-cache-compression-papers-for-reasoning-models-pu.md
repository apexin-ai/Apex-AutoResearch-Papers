# Research conversation: Search for the most recent KV cache compression papers for reasoning models (published or posted April-May 2026) that I 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a0d64cbc73c0919e7.jsonl`
- **Structured JSON:** [`8828ec820d61889cf2b7.json`](../../sessions/88/8828ec820d61889cf2b7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

60 recorded events

### User

_source line 1 · 2026-05-09T18:56:51.099Z_

Search for the most recent KV cache compression papers for reasoning models (published or posted April-May 2026) that I might have missed. I'm working on a paper called RIC (Retrospective Importance Cascade) that does one-shot training-free compression at the &lt;/think> boundary of reasoning models like DeepSeek-R1.

Search queries to run:
1. "KV cache compression reasoning models 2026" on arxiv
2. "thinking phase KV cache boundary trigger 2026"
3. "KV cache eviction reasoning LLM AIME 2026"

For each paper found, note: title, arxiv ID, date, method summary, whether it's training-free, whether it's boundary-triggered, compression rate, and benchmark results. Flag any that are directly competitive with a one-shot boundary-triggered training-free method.

Also check if there are any papers addressing pre-RoPE KV scoring or conclusion-token query proxies specifically.

Return a concise list of new relevant papers from April-May 2026 that should be cited or addressed in related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "56fa3df8-f3df-4bd4-8116-5ec882593585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-09T18:56:51.101Z_

```json
{
  "parentUuid": "56fa3df8-f3df-4bd4-8116-5ec882593585",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
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
  "uuid": "bdbd439d-b61b-4ba1-ba34-3fe4c4f1c643",
  "timestamp": "2026-05-09T18:56:51.101Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-09T18:56:52.752Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01U35tRJJa9KBBCFfhWAXUmR`</summary>

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
  "parentUuid": "bdbd439d-b61b-4ba1-ba34-3fe4c4f1c643",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWHVcEK9xJpnS8cWhUC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dddf57f-6c3c-4e8d-a972-eec288f5adf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WxFnrH61SpJAfEBhqRRQ5L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 8088,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 794
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8088,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 794,
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

_source line 4 · 2026-05-09T18:56:52.758Z_

<details><summary>↩ Tool result · `toolu_01U35tRJJa9KBBCFfhWAXUmR`</summary>

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
  "parentUuid": "8dddf57f-6c3c-4e8d-a972-eec288f5adf4",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "48dd3b5a-e081-42fa-b5a8-2a445349986c",
  "sourceToolAssistantUUID": "8dddf57f-6c3c-4e8d-a972-eec288f5adf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-09T18:56:56.079Z_

I'll run all three searches in parallel to cover the full landscape efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48dd3b5a-e081-42fa-b5a8-2a445349986c",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWHcuXNxxFtkMQdBpNs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63d01dd1-23d1-4c06-980f-2353c0618da4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019wbUqB1PB17s3jwoT9LQhM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 6 · 2026-05-09T18:56:57.304Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WvegEjPj9QKHxmD6vAsTgJ`</summary>

```json
{
  "query": "KV cache compression reasoning models 2026 arxiv",
  "allowed_domains": [
    "arxiv.org",
    "ar5iv.org",
    "huggingface.co",
    "semanticscholar.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63d01dd1-23d1-4c06-980f-2353c0618da4",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWHcuXNxxFtkMQdBpNs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d9019d6-6b6c-4098-bc22-2222130d71bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019wbUqB1PB17s3jwoT9LQhM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 7 · 2026-05-09T18:56:58.506Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qfvsc9okWyMJaKcWkFxXDN`</summary>

```json
{
  "query": "thinking phase KV cache boundary trigger 2026 arxiv reasoning LLM",
  "allowed_domains": [
    "arxiv.org",
    "ar5iv.org",
    "huggingface.co",
    "semanticscholar.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d9019d6-6b6c-4098-bc22-2222130d71bc",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWHcuXNxxFtkMQdBpNs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a50bfd3-8009-4938-b34e-22fee407ae84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019wbUqB1PB17s3jwoT9LQhM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 8 · 2026-05-09T18:56:59.174Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R1BTG1heRypJyZ1JzXovuc`</summary>

```json
{
  "query": "KV cache eviction reasoning LLM AIME 2026 arxiv DeepSeek",
  "allowed_domains": [
    "arxiv.org",
    "ar5iv.org",
    "huggingface.co",
    "semanticscholar.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a50bfd3-8009-4938-b34e-22fee407ae84",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWHcuXNxxFtkMQdBpNs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34d6ec87-e5c7-4366-ba5a-759fa0fd6170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019wbUqB1PB17s3jwoT9LQhM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8882,
      "output_tokens": 327,
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
          "output_tokens": 327,
          "cache_read_input_tokens": 8882,
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

_source line 9 · 2026-05-09T18:57:05.259Z_

<details><summary>↩ Tool result · `toolu_01WvegEjPj9QKHxmD6vAsTgJ`</summary>

```text
Web search results for query: "KV cache compression reasoning models 2026 arxiv"

Links: [{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"[2505.24133] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/abs/2505.24133"},{"title":"LongFlow: Efficient KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2603.11504"},{"title":"[2604.04921v1] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921v1"},{"title":"[2603.11504] LongFlow: Efficient KV Cache Compression for Reasoning M","url":"https://arxiv.org/abs/2603.11504"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"1 A Survey on Large Language Model Acceleration based on KV Cache Management","url":"https://arxiv.org/pdf/2412.19442"},{"title":"[2604.17935v1] How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers","url":"https://arxiv.org/abs/2604.17935v1"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"[2604.15356] Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit","url":"https://arxiv.org/abs/2604.15356"}]

I found several recent papers on arXiv about KV cache compression for reasoning models from 2026. Here are the key findings:

## Recent Papers on KV Cache Compression for Reasoning Models (2026)

**1. R-KV: Redundancy-aware KV Cache Compression**

R-KV proposes a novel method specifically targeting redundant tokens in reasoning models. The method preserves nearly 100% of the full KV cache performance using only 10% of the KV cache. The approach consists of three key components: (1) an attention-based importance scoring mechanism that selects critical tokens for retention, (2) a dynamic redundancy scoring mechanism that identifies repetitive tokens through real-time analysis of key vectors, and (3) a joint eviction mechanism that balances both redundancy and importance to optimize cache efficiency.

**2. LongFlow: Efficient KV Cache Compression**

LongFlow is a KV cache compression method with an efficient importance estimation metric derived from an intermediate result of attention computation using only the current query, introducing negligible computational overhead and requiring no auxiliary storage. Experiments show that LongFlow achieves up to an 11.8 times throughput improvement with 80% KV cache compression with minimal impact on model accuracy.

**3. TriAttention: Trigonometric KV Compression**

Extended reasoning in large language models creates severe KV cache memory bottlenecks. TriAttention observes that Q and K vectors are highly concentrated around fixed non-zero centers and remain stable across positions in the pre-RoPE space.

**4. Sequential KV Cache Compression via Probabilistic Language Tries**

This approach introduces sequential KV compression, a two-layer architecture that exploits language structure through probabilistic prefix deduplication and predictive delta coding, storing only the residual of each new KV vector from the model's own prediction of it.

These papers represent the cutting edge of research on making reasoning model inference more efficient through intelligent KV cache management.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d9019d6-6b6c-4098-bc22-2222130d71bc",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "1911ba7d-dfe9-4a59-8d79-d2fcfbbe6c21",
  "sourceToolAssistantUUID": "9d9019d6-6b6c-4098-bc22-2222130d71bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-09T18:57:06.931Z_

<details><summary>↩ Tool result · `toolu_01R1BTG1heRypJyZ1JzXovuc`</summary>

```text
Web search results for query: "KV cache eviction reasoning LLM AIME 2026 arxiv DeepSeek"

Links: [{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203v1"},{"title":"[2504.15364] KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/abs/2504.15364"},{"title":"Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://www.arxiv.org/pdf/2601.17668"},{"title":"R-KV: Redundancy-aware KV Cache Compression for ...","url":"https://arxiv.org/pdf/2505.24133"},{"title":"CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/html/2604.25080"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"Hierarchical Adaptive Eviction for KV Cache Management in Multimodal Language Models","url":"https://arxiv.org/html/2602.02197v1"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning","url":"https://arxiv.org/html/2506.15969v1"}]

Based on the search results, here are the key findings on KV cache eviction for reasoning models on AIME tasks:

## Recent Research Papers

ForesightKV designs a Golden Eviction algorithm that identifies optimal eviction KV pairs using future attention scores, with these traces distilled via supervised training with a Pairwise Ranking Loss. The method was evaluated on AIME2024 and AIME2025 benchmarks and consistently outperforms prior methods under only half the cache budget.

KeyDiff demonstrates near baseline performance for Deepseek-R1-Distill-Llama-8B on the Math500 reasoning benchmark and decreases end-to-end inference latency by up to 30% compared to other token-eviction methods.

R-KV achieves 105% accuracy of the full KV baseline with around 16% of the KV cache using DeepSeek-R1-Distill-Llama-8B on the AIME-24 dataset.

LazyEviction can maintain comparable performance while reducing 50% KV budget on mathematics reasoning datasets, surpassing SOTA KV cache compression methods.

## Key Technical Approaches

Fast KVzip integrates a lightweight gating mechanism into the Transformer's forward pass that allows the model to directly assess the importance of KV pairs during both prefill and decoding stages with negligible memory and computational overhead.

R-KV uses a joint eviction mechanism that balances both redundancy and importance to optimize cache efficiency.

These papers from early 2026 demonstrate significant progress in making KV cache eviction effective for reasoning-intensive tasks like AIME problem solving.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34d6ec87-e5c7-4366-ba5a-759fa0fd6170",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "8dd36de0-f608-4f7b-8cd2-b5c9d17fb27a",
  "sourceToolAssistantUUID": "34d6ec87-e5c7-4366-ba5a-759fa0fd6170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-09T18:57:07.982Z_

<details><summary>↩ Tool result · `toolu_01Qfvsc9okWyMJaKcWkFxXDN`</summary>

```text
Web search results for query: "thinking phase KV cache boundary trigger 2026 arxiv reasoning LLM"

Links: [{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle","url":"https://arxiv.org/html/2601.16986v1"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"[2603.13289] RelayCaching: Accelerating LLM Collaboration via Decoding KV Cache Reuse","url":"https://arxiv.org/abs/2603.13289"},{"title":"[2601.20326] Beyond Speedup -- Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/abs/2601.20326"},{"title":"A Survey on Large Language Model Acceleration based on KV Cache Management","url":"https://arxiv.org/html/2412.19442v3"},{"title":"CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/html/2604.25080"},{"title":"Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning","url":"https://arxiv.org/html/2505.16950"},{"title":"Challenges and Research Directions for Large Language ...","url":"https://arxiv.org/pdf/2601.05047"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://arxiv.org/html/2511.06029"}]

Based on the web search results, I found several relevant arxiv papers from 2026 and late 2025 related to KV cache management in reasoning LLMs:

## Key Findings:

**Crystal-KV (January 2026)**: Crystal-KV is an efficient CoT KV-cache management framework built on an answer-first principle that prioritizes think-KV essential to the final answer, redefining KV management for reasoning-oriented LLMs during long think stage.

**Bottlenecked Transformers (March 2026)**: This work addresses reasoning ability that scales with inference-time compute through "thinking" chains of thought, proposing memory consolidation via KV cache rewrites as analogous to performing in-place rewrites of new KV segments, with theoretical justification for why this is beneficial for improved reasoning. The Cache Processor is invoked each time a newline token is generated (marking the end of a reasoning step).

**Lethe (November 2025)**: This approach uses dynamic thresholds to evict tokens below the threshold while preserving recent and boundary tokens, allowing gradual forgetting of stale context while preserving salient history.

**General Context**: Specialized reasoning models such as DeepSeek-R1 and the Llama-Nemotron series output excessively long reasoning traces which outnumber the length of the prompt itself by hundreds to thousands of tokens.

These papers collectively address the challenge of managing KV cache boundaries and transitions between thinking and answer phases in reasoning LLMs, with multiple approaches exploring different boundary-trigger mechanisms for cache management.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a50bfd3-8009-4938-b34e-22fee407ae84",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "db66fea1-d4c0-4e61-94ec-d9dbd4fd855c",
  "sourceToolAssistantUUID": "4a50bfd3-8009-4938-b34e-22fee407ae84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-09T18:57:10.759Z_

Good initial sweep. Now I'll fetch the abstract details for the most relevant papers to get precise dates, compression rates, and benchmark numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db66fea1-d4c0-4e61-94ec-d9dbd4fd855c",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWJjo3U2xBd78KiJLAF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5bc55aa-93bb-4809-bd86-7ecc135edd76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VQbxdqSSSZYspWqZxKJUme",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 2132,
      "cache_read_input_tokens": 10274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2132,
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

_source line 13 · 2026-05-09T18:57:11.732Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YLnKEJ7h2HMVFCF5ev2BxD`</summary>

```json
{
  "query": "arxiv 2505.24133 R-KV Redundancy-aware KV Cache Compression Reasoning Models abstract method",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5bc55aa-93bb-4809-bd86-7ecc135edd76",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWJjo3U2xBd78KiJLAF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29a47332-884b-4aeb-ab15-d218fd6def82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VQbxdqSSSZYspWqZxKJUme",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 2132,
      "cache_read_input_tokens": 10274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2132,
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

_source line 14 · 2026-05-09T18:57:12.910Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QDj5UAUgPNG3dwmpyagPtv`</summary>

```json
{
  "query": "arxiv 2604.04921 TriAttention Trigonometric KV Compression pre-RoPE reasoning abstract",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29a47332-884b-4aeb-ab15-d218fd6def82",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWJjo3U2xBd78KiJLAF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f1a8533-b9fb-4243-8388-e5a93c23c03f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VQbxdqSSSZYspWqZxKJUme",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 2132,
      "cache_read_input_tokens": 10274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2132,
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

_source line 15 · 2026-05-09T18:57:14.210Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QgMBWr8pQ6pGZ7bcyy95ZE`</summary>

```json
{
  "query": "arxiv 2604.17935 \"How Much Cache Does Reasoning Need\" Depth-Cache Tradeoffs KV-Compressed abstract results",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f1a8533-b9fb-4243-8388-e5a93c23c03f",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWJjo3U2xBd78KiJLAF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14f70623-3701-4b37-9f28-580f6992c7e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VQbxdqSSSZYspWqZxKJUme",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 902,
      "cache_creation_input_tokens": 2132,
      "cache_read_input_tokens": 10274,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2132
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 902,
          "output_tokens": 309,
          "cache_read_input_tokens": 10274,
          "cache_creation_input_tokens": 2132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2132,
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

_source line 16 · 2026-05-09T18:57:17.922Z_

<details><summary>↩ Tool result · `toolu_01YLnKEJ7h2HMVFCF5ev2BxD`</summary>

```text
Web search results for query: "arxiv 2505.24133 R-KV Redundancy-aware KV Cache Compression Reasoning Models abstract method"

Links: [{"title":"[2505.24133] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/abs/2505.24133"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"R-KV: Redundancy-aware KV Cache Compression for ...","url":"https://arxiv.org/pdf/2505.24133"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration","url":"https://arxiv.org/html/2505.24133v1"},{"title":"Redundancy-aware KV Cache Compression for Training- ...","url":"https://www.arxiv.org/pdf/2505.24133v2"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"CSKV: Training-Efficient Channel Shrinking for KV Cache in Long-Context Scenarios","url":"https://arxiv.org/html/2409.10593"},{"title":"Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning","url":"https://arxiv.org/html/2503.04973v1"},{"title":"ReCalKV: Low-Rank KV Cache Compression via Head Reordering and Offline Calibration","url":"https://arxiv.org/html/2505.24357v1"},{"title":"[2603.20397] KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/abs/2603.20397"}]

I found the arXiv paper 2505.24133. Here's information about the R-KV paper:

## Paper Details

R-KV: Redundancy-aware KV Cache Compression for Reasoning Models

## Abstract

Reasoning models have demonstrated impressive performance in self-reflection and chain-of-thought reasoning. However, they often produce excessively long outputs, leading to prohibitively large key-value (KV) caches during inference. While chain-of-thought inference significantly improves performance on complex reasoning tasks, it can also lead to reasoning failures when deployed with existing KV cache compression approaches.

## Method

The paper proposes Redundancy-aware KV Cache Compression for Reasoning models (R-KV), a novel method specifically targeting redundant tokens in reasoning models. The approach consists of three key components: (1) an attention-based importance scoring mechanism that selects critical tokens for retention, (2) a dynamic redundancy scoring mechanism (which evaluates the similarity of key vectors), and (3) a joint selection strategy that optimizes cache efficiency.

## Results

The method preserves nearly 100% of the full KV cache performance using only 10% of the KV cache, substantially outperforming existing KV cache baselines, which reach only 60% of the performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29a47332-884b-4aeb-ab15-d218fd6def82",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "2c16fb84-6f35-4209-a14c-35e28e541c29",
  "sourceToolAssistantUUID": "29a47332-884b-4aeb-ab15-d218fd6def82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-09T18:57:20.081Z_

<details><summary>↩ Tool result · `toolu_01QDj5UAUgPNG3dwmpyagPtv`</summary>

```text
Web search results for query: "arxiv 2604.04921 TriAttention Trigonometric KV Compression pre-RoPE reasoning abstract"

Links: [{"title":"[2604.04921] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921"},{"title":"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/html/2604.04921v1"},{"title":"[2604.04921v1] TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://arxiv.org/abs/2604.04921v1"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2604.04921"},{"title":"SAW-INT4: System-AWare 4-Bit KV-Cache Quantization for Real-World LLM Serving","url":"https://arxiv.org/html/2604.19157"},{"title":"[2604.15356] Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit","url":"https://arxiv.org/abs/2604.15356"},{"title":"CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/html/2604.10235"},{"title":"[2604.10235] CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/abs/2604.10235"},{"title":"Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit","url":"https://arxiv.org/html/2604.15356"},{"title":"Residual-Mass Accounting for Partial-KV Decoding","url":"https://arxiv.org/html/2604.05438"}]

Based on the search results, here is the abstract for arxiv paper 2604.04921 on TriAttention:

## TriAttention: Efficient Long Reasoning with Trigonometric KV Compression

**Abstract:**

Extended reasoning in large language models (LLMs) creates severe KV cache memory bottlenecks. Leading KV cache compression methods estimate KV importance using attention scores from recent post-RoPE queries. However, queries rotate with position during RoPE, making representative queries very few, leading to poor top-key selection and unstable reasoning. 

To avoid this issue, the authors turn to the pre-RoPE space, where they observe that Q and K vectors are highly concentrated around fixed non-zero centers and remain stable across positions -- Q/K concentration. This concentration causes queries to preferentially attend to keys at specific distances (e.g., nearest keys), with the centers determining which distances are preferred via a trigonometric series.

Based on this, they propose TriAttention to estimate key importance by leveraging these centers. On AIME25 with 32K-token generation, TriAttention matches Full Attention reasoning accuracy while achieving 2.5x higher throughput or 10.7x KV memory reduction, whereas leading baselines achieve only about half the accuracy at the same efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f1a8533-b9fb-4243-8388-e5a93c23c03f",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "dc213fe4-2927-40e9-8cde-1966fa508b1f",
  "sourceToolAssistantUUID": "8f1a8533-b9fb-4243-8388-e5a93c23c03f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-09T18:57:20.958Z_

<details><summary>↩ Tool result · `toolu_01QgMBWr8pQ6pGZ7bcyy95ZE`</summary>

```text
Web search results for query: "arxiv 2604.17935 "How Much Cache Does Reasoning Need" Depth-Cache Tradeoffs KV-Compressed abstract results"

Links: [{"title":"How Much Cache Does Reasoning Need? Depth–Cache Tradeoffs in KV-Compressed Transformers","url":"https://arxiv.org/html/2604.17935v1"},{"title":"[2604.17935v1] How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers","url":"https://arxiv.org/abs/2604.17935v1"},{"title":"[2602.19137] Derivation Depth as an Information Metric: Axioms, Coding Theorems, and Storage--Computation Tradeoffs","url":"https://arxiv.org/abs/2602.19137"},{"title":"[2604.24647] DepthKV: Layer-Dependent KV Cache Pruning for Long-Context LLM Inference","url":"https://arxiv.org/abs/2604.24647"},{"title":"Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning","url":"https://arxiv.org/html/2503.04973v1"},{"title":"MiniCache: KV Cache Compression in Depth Dimension for Large Language Models","url":"https://arxiv.org/html/2405.14366v2"},{"title":"Universal Transformers Need Memory: Depth-State Trade-offs in Adaptive Recursive Reasoning","url":"https://arxiv.org/html/2604.21999"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"Depth-Width Tradeoffs in Algorithmic Reasoning of Graph Tasks with Transformers","url":"https://arxiv.org/pdf/2503.01805"},{"title":"[2604.21999] Universal Transformers Need Memory: Depth-State Trade-offs in Adaptive Recursive Reasoning","url":"https://arxiv.org/abs/2604.21999"}]

Based on the search results, here's what I found about arxiv 2604.17935:

## Paper Overview

"How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers" addresses the key-value (KV) cache as the dominant memory bottleneck during Transformer inference, exploring how aggressively it can be compressed before multi-step reasoning degrades.

## Methodology

The study examines this through k-hop pointer chasing on n tokens under a shared KV cache of size s, attention dimension m, H heads, p-bit precision, and a locality-respecting cache controller (satisfied by all standard KV-compression methods).

## Main Results

The paper provides three results, with the first being a product depth lower bound (conjectured), where they conjecture that any such Transformer requires depth L = Ω(⌈k/s⌉ · ⌈log₂ n/(Hmp)⌉).

Unconditionally, they prove a matching upper bound L = O(min(k, ⌈k/s⌉ log s) · log n/(mp)) via windowed pointer doubling, and a max-bound L = Ω(max(⌈k/s⌉, log n/(Hmp))).

The paper was submitted on April 20, 2026, by author Xiao Wang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14f70623-3701-4b37-9f28-580f6992c7e4",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "b82b02a6-b6a2-402e-8f29-aa244d6a750f",
  "sourceToolAssistantUUID": "14f70623-3701-4b37-9f28-580f6992c7e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-09T18:57:24.197Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UjaTxkn6ZaGu1FGszCATAS`</summary>

```json
{
  "query": "arxiv 2505 \"Bottlenecked Transformers\" KV cache consolidation reasoning periodic newline token",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b82b02a6-b6a2-402e-8f29-aa244d6a750f",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWKhGWnPA78RRKZQNko",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8615394a-97a1-46f7-93ca-330ded2b1cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017X2YzSDaijUEY9XwrNsrdB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3725,
      "cache_read_input_tokens": 12406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3725,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-09T18:57:25.383Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013enXYRwtZjAoE8soJ3Ws7L`</summary>

```json
{
  "query": "arxiv ForesightKV 2602.03203 golden eviction reasoning AIME training-free method",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8615394a-97a1-46f7-93ca-330ded2b1cfe",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWKhGWnPA78RRKZQNko",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8aa7d872-0715-404c-8f61-8729fe7cfe0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017X2YzSDaijUEY9XwrNsrdB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3725,
      "cache_read_input_tokens": 12406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3725,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-09T18:57:26.405Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011j2FuvisUDMbvYsYs5Ft2C`</summary>

```json
{
  "query": "arxiv Crystal-KV 2601.16986 answer-first KV cache think boundary training-free reasoning",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8aa7d872-0715-404c-8f61-8729fe7cfe0e",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWKhGWnPA78RRKZQNko",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "486025a0-be22-4b1e-915a-2b00c83ea88f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017X2YzSDaijUEY9XwrNsrdB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3725,
      "cache_read_input_tokens": 12406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3725,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-09T18:57:31.669Z_

<details><summary>↩ Tool result · `toolu_013enXYRwtZjAoE8soJ3Ws7L`</summary>

```text
Web search results for query: "arxiv ForesightKV 2602.03203 golden eviction reasoning AIME training-free method"

Links: [{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203"},{"title":"[2602.03203] ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/abs/2602.03203"},{"title":"Learning to Evict from Key-Value Cache","url":"https://arxiv.org/html/2602.10238v1"},{"title":"[2602.10238] Learning to Evict from Key-Value Cache","url":"https://arxiv.org/abs/2602.10238"},{"title":"NEAT: Neuron-Based Early Exit for Large Reasoning Models","url":"https://arxiv.org/html/2602.02010v1"},{"title":"On the Efficacy of Eviction Policy for Key-Value Constrained Generative Language Model Inference","url":"https://arxiv.org/html/2402.06262v2"},{"title":"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning","url":"https://arxiv.org/html/2506.15969"},{"title":"Dynamic Early Exit in Reasoning Models","url":"https://arxiv.org/html/2504.15895v1"},{"title":"[2504.15895] Dynamic Early Exit in Reasoning Models","url":"https://arxiv.org/abs/2504.15895"},{"title":"[2602.02828] A Single Revision Step Improves Token-Efficient LLM Reasoning","url":"https://www.arxiv.org/abs/2602.02828"}]

Based on the search results, here's what I found about ForesightKV (arXiv 2602.03203):

## ForesightKV Overview

ForesightKV is a method that learns to predict the long-term contribution of each KV pair and adaptively evicts less important ones during generation.

## Key Components

**Golden Eviction Algorithm:**
The method introduces the Golden Eviction algorithm to construct supervision labels by partitioning the attention matrix into fixed-length blocks and using the maximum block scores of future steps as future scores, discarding pairs with the lowest future scores to minimize eviction impact.

**Training Approach:**
ForesightKV employs a two-stage training paradigm: supervised learning with constructed future importance labels, followed by reinforcement learning to refine eviction policies. The method formulates cache eviction as a Markov Decision Process and applies the GRPO algorithm to mitigate significant language modeling loss increase on low-entropy tokens.

## Performance on AIME

Experiments on AIME2024 and AIME2025 benchmarks of three reasoning models demonstrate that ForesightKV consistently outperforms prior methods under only half the cache budget.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8aa7d872-0715-404c-8f61-8729fe7cfe0e",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "4f3e50ca-7436-4a5f-aa49-b91f25b21d38",
  "sourceToolAssistantUUID": "8aa7d872-0715-404c-8f61-8729fe7cfe0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-09T18:57:32.766Z_

<details><summary>↩ Tool result · `toolu_01UjaTxkn6ZaGu1FGszCATAS`</summary>

```text
Web search results for query: "arxiv 2505 "Bottlenecked Transformers" KV cache consolidation reasoning periodic newline token"

Links: [{"title":"Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning","url":"https://arxiv.org/html/2505.16950"},{"title":"[2505.16950] Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning","url":"https://arxiv.org/abs/2505.16950"},{"title":"Bottlenecked Transformers: Periodic KV Cache Abstraction for Generalised Reasoning","url":"https://arxiv.org/html/2505.16950v2"},{"title":"[2604.17935v1] How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers","url":"https://arxiv.org/abs/2604.17935v1"},{"title":"How Much Cache Does Reasoning Need? Depth–Cache Tradeoffs in KV-Compressed Transformers","url":"https://arxiv.org/html/2604.17935v1"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"Time and Memory Trade-off of KV-Cache Compression in Tensor Transformer Decoding","url":"https://arxiv.org/html/2503.11108"},{"title":"EFFICIENTLY SCALING TRANSFORMER INFERENCE","url":"https://arxiv.org/pdf/2211.05102"},{"title":"Limits of KV Cache Compression for Tensor Attention based Autoregressive Transformers","url":"https://arxiv.org/html/2503.11108v1"},{"title":"Periodic KV Cache Consolidation for Generalised Reasoning","url":"https://arxiv.org/pdf/2505.16950"}]

I found the paper you're looking for! Here's what I found:

## Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning

The Bottlenecked Transformer augments a backbone LLM with a Cache Processor, an auxiliary Transformer that performs periodic, non-causal, in-place KV rewrites at newline-delimited reasoning step boundaries.

### Key Approach

The work provides a theoretical justification as to why memory (re)consolidation via KV cache rewrites is beneficial for improved reasoning through the lens of Information Bottleneck (IB) theory, which posits that model generalisation emerges from an optimal balance between input information compression and retention of predictive information in latent representations.

### Architecture Details

The Processor consolidates recently written KV entries and reconsolidates a small, top-k attention-selected set of prior entries.

### Performance

The model sees consistent performance gains over vanilla Transformers and pause-token augmented baselines, with gains of up to +6.6pp for selected tasks/backbone.

The paper (arxiv 2505.16950) was authored by Adnan Oomerjee and colleagues and received its most recent update on March 25, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8615394a-97a1-46f7-93ca-330ded2b1cfe",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "5172a193-bddb-46af-a81e-92b5ef71d5e9",
  "sourceToolAssistantUUID": "8615394a-97a1-46f7-93ca-330ded2b1cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-09T18:57:32.984Z_

<details><summary>↩ Tool result · `toolu_011j2FuvisUDMbvYsYs5Ft2C`</summary>

```text
Web search results for query: "arxiv Crystal-KV 2601.16986 answer-first KV cache think boundary training-free reasoning"

Links: [{"title":"[2601.16986] Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle","url":"https://arxiv.org/abs/2601.16986"},{"title":"Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle","url":"https://arxiv.org/html/2601.16986"},{"title":"KVzap: Fast, Adaptive, and Faithful KV Cache Pruning","url":"https://arxiv.org/html/2601.07891"},{"title":"[2601.13631] ContiguousKV: Accelerating LLM Prefill with Granularity-Aligned KV Cache Management","url":"https://arxiv.org/abs/2601.13631"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"[2603.20397] KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/abs/2603.20397"},{"title":"GPU-Accelerated INT8 Quantization for KV Cache Compression in Large Language Models","url":"https://arxiv.org/html/2601.04719v1"},{"title":"Past- and Future-Informed KV Cache Policy with Salience Estimation in Autoregressive Video Diffusion","url":"https://arxiv.org/html/2601.21896"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"TableCache: Primary Foreign Key Guided KV Cache Precomputation for Low Latency Text-to-SQL","url":"https://arxiv.org/html/2601.08743v1"}]

Based on the search results, here's what I found:

Crystal-KV is an efficient KV cache management framework tailored for CoT (Chain-of-Thought) reasoning. The key insight is the answer-first principle.

Chain-of-Thought reasoning in large language models significantly improves accuracy on complex tasks, yet incurs excessive memory overhead due to the long think-stage sequences stored in the Key-Value cache. Unlike traditional generation tasks where all tokens are uniformly important, CoT emphasizes the final answer, rendering conventional KV compression strategies ineffective.

The approach distinguishes between SlipKV, which mainly maintains reasoning flow but may occasionally introduce misleading context, and CrystalKV, which truly contributes to answer correctness. It precisely identifies when a SlipKV entry's utility expires and evicts it. The framework also introduces an adaptive cache budget allocation algorithm that estimates the importance of each layer/head and adjusts the KV cache budget during inference based on the dynamic proportion of CrystalKV.

Results show that Crystal-KV achieves state-of-the-art KV cache compression, significantly improves throughput, and enables faster response time, while maintaining or even improving answer accuracy for CoT reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "486025a0-be22-4b1e-915a-2b00c83ea88f",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "24c06c9f-1ff5-4f23-bdcd-0c3ed3414744",
  "sourceToolAssistantUUID": "486025a0-be22-4b1e-915a-2b00c83ea88f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-09T18:57:35.987Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017FEKgANwEpWry6Sz7a8DaH`</summary>

```json
{
  "query": "arxiv 2602.03203 ForesightKV date submitted February 2026 training required",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24c06c9f-1ff5-4f23-bdcd-0c3ed3414744",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWLahQVCLN1dJYKX1Mp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "314ca2df-6d9b-4593-b5c7-d2c72bae7906",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NjgrWpJbpnwQjPiJQj6pqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2770,
      "cache_read_input_tokens": 16131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2770,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-09T18:57:36.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0144wx1NPLn6z9nsy71rNGGE`</summary>

```json
{
  "query": "arxiv \"think token\" OR \"end of thinking\" OR \"&lt;/think>\" KV cache compression one-shot boundary 2025 2026",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "314ca2df-6d9b-4593-b5c7-d2c72bae7906",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWLahQVCLN1dJYKX1Mp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c669be9-6893-41e3-b8bd-6c9984c65156",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NjgrWpJbpnwQjPiJQj6pqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2770,
      "cache_read_input_tokens": 16131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2770,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-09T18:57:37.867Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L4o4w662XnKG71mtJQvXWj`</summary>

```json
{
  "query": "arxiv pre-RoPE KV scoring query proxy conclusion token importance estimation reasoning 2026",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c669be9-6893-41e3-b8bd-6c9984c65156",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWLahQVCLN1dJYKX1Mp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c0b6366-0f29-46dc-bc93-1f56c8f553b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NjgrWpJbpnwQjPiJQj6pqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2770,
      "cache_read_input_tokens": 16131,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2770
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 264,
          "cache_read_input_tokens": 16131,
          "cache_creation_input_tokens": 2770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2770,
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

_source line 28 · 2026-05-09T18:57:40.745Z_

<details><summary>↩ Tool result · `toolu_017FEKgANwEpWry6Sz7a8DaH`</summary>

```text
Web search results for query: "arxiv 2602.03203 ForesightKV date submitted February 2026 training required"

Links: [{"title":"[2602.03203] ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/abs/2602.03203"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203"},{"title":"[2603.03203] No Memorization, No Detection: Output Distribution-Based Contamination Detection in Small Language Models","url":"https://arxiv.org/abs/2603.03203"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1499&show=2000"},{"title":"Convex optimization for non-equilibrium steady states on a hybrid quantum processor","url":"https://arxiv.org/html/2204.03203"},{"title":"[2602.12322v1] ForeAct: Steering Your VLA with Efficient Visual Foresight Planning","url":"https://arxiv.org/abs/2602.12322v1"},{"title":"[2503.03203] Efficient Parallel Execution of Blockchain Transactions Leveraging Conflict Specifications","url":"https://arxiv.org/abs/2503.03203"},{"title":"[2605.03203] A Partition-Based Generating Function for Row-Convex Polyominoes","url":"https://arxiv.org/abs/2605.03203"},{"title":"[2601.03203] Counterfactual Fairness with Graph Uncertainty","url":"https://arxiv.org/abs/2601.03203"},{"title":"[2204.03203] Convex Optimization for Nonequilibrium Steady States on a Hybrid Quantum Processor","url":"https://arxiv.org/abs/2204.03203"}]

Based on the search results, here's the information about arxiv paper 2602.03203:

**Paper:** ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution

**Date Submitted:** Submitted on Tuesday, February 3, 2026

**Training Required:** Yes. ForesightKV is a training-based KV cache eviction framework that learns to predict which KV pairs to evict during long-text generations. More specifically, the framework employs a two-stage training paradigm: supervised learning with constructed future importance labels, followed by reinforcement learning to optimize the scoring models' long-term prediction capacities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "314ca2df-6d9b-4593-b5c7-d2c72bae7906",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "544f0773-9791-4589-ae8d-1e6244559fd4",
  "sourceToolAssistantUUID": "314ca2df-6d9b-4593-b5c7-d2c72bae7906",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-09T18:57:46.120Z_

<details><summary>↩ Tool result · `toolu_01L4o4w662XnKG71mtJQvXWj`</summary>

```text
Web search results for query: "arxiv pre-RoPE KV scoring query proxy conclusion token importance estimation reasoning 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.03152"},{"title":"[2602.08329] Near-Oracle KV Selection via Pre-hoc Sparsity for Long-Context Inference","url":"https://arxiv.org/abs/2602.08329"},{"title":"Near-Oracle KV Selection via Pre-hoc Sparsity for Long-Context Inference","url":"https://arxiv.org/html/2602.08329"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning","url":"https://arxiv.org/html/2506.15969v1"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by ...","url":"https://arxiv.org/pdf/2603.10899"},{"title":"[2601.14279] On the Limits of Learned Importance Scoring for KV Cache Compression","url":"https://arxiv.org/abs/2601.14279"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"HashEvict: A Pre-Attention KV Cache Eviction Strategy using Locality-Sensitive Hashing","url":"https://arxiv.org/html/2412.16187v3"}]

I found several relevant arxiv papers related to your search query. Here are the key findings:

## Pre-hoc Sparsity and KV Selection

Pre-hoc Sparsity (PrHS) selects KV entries before attention scoring and provides explicit accuracy control. This approach addresses a critical problem: existing sparse methods generally rely on posterior heuristics conditioned on observed attention or proxy scores, which introduces posterior bias that tends to distort true token importance and miss salient tokens, thereby impairing long-range reasoning.

## Token Importance Estimation Approaches

Several recent papers explore different methods for estimating token importance:

1. **Query-Proxy Methods**: Learnable special tokens can serve as implicit future response for importance estimation, leveraging draft-based methods without their computational overhead.

2. **Attention-based Estimation**: SnapKV estimates token importance based on accumulated attention scores within an observation window during prefilling.

3. **RoPE and Pre-attention Processing**: A recent finding uncovered functional sparsity at feed-forward level (FC) induced by RoPE.

## Reasoning Task Performance

FASA surpasses standard baselines and also R-KV, a highly specialized method for chain-of-thought compression, achieving 86.4% accuracy on a scant 10% context budget. Additionally, token importance recurrence is observed in reasoning tasks, where specific tokens exhibit recurrent attention patterns representing foundational formulations or intermediate conclusions crucial for maintaining knowledge continuity in multi-step reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c0b6366-0f29-46dc-bc93-1f56c8f553b1",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "cefa4c7c-dde7-4033-9acb-87b7649c79b4",
  "sourceToolAssistantUUID": "6c0b6366-0f29-46dc-bc93-1f56c8f553b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-09T18:57:47.056Z_

<details><summary>↩ Tool result · `toolu_0144wx1NPLn6z9nsy71rNGGE`</summary>

```text
Web search results for query: "arxiv "think token" OR "end of thinking" OR "&lt;/think>" KV cache compression one-shot boundary 2025 2026"

Links: [{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"THINKV: THOUGHT-ADAPTIVE KV CACHE COM- PRESSION FOR EFFICIENT REASONING MODELS","url":"https://arxiv.org/pdf/2510.01290v1"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"[2510.01290v1] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290v1"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"A Systematic Exploration of KV Cache Compression ...","url":"https://arxiv.org/pdf/2503.11816"},{"title":"[2512.12008] Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/abs/2512.12008"},{"title":"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/html/2605.02905"}]

I've performed the web search for your query. Here are the relevant results from arXiv papers on KV cache compression in the context of reasoning models with thinking tokens:

## Key Papers Found:

**1. ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (October 2025)**

ThinKV is a thought-adaptive KV cache compression framework based on the observation that attention sparsity reveals distinct thought types with varying importance within the chain of thought. It applies a hybrid quantization–eviction strategy, assigning token precision by thought importance and progressively evicting tokens from less critical thoughts as reasoning trajectories evolve. ThinKV achieves near-lossless accuracy with less than 5% of the original KV cache, while improving performance with up to 5.8x higher inference throughput over state-of-the-art baselines.

**2. Utilizing KV Cache for Sampling and Reasoning (January 2026)**

This paper discusses "two-step switch" methods that can append &lt;/think> to terminate reasoning early or inject &lt;think> to engage slow thinking mid-generation. The approach shows that pooled KV-cache features can drive both one-shot (classification-style) and in-generation (generative-style) switching through simple control tokens.

**3. Hold Onto That Thought: Assessing KV Cache Compression On Reasoning (December 2025)**

This work benchmarks the performance of several popular compression strategies on long-reasoning tasks, discovering that H2O and a decoding-enabled variant of SnapKV are dominant strategies for reasoning models, indicating the utility of heavy-hitter tracking for reasoning traces.

**4. Additional KV Cache Quantization Work (April 2026)**

Adaptive KV-cache quantization assigns bit-width proportional to token importance, inspired by Huffman coding's principle of variable-length allocation, minimizing expected memory and latency without sacrificing competitive accuracy.

The search results indicate active research in 2025-2026 on compressing KV caches for reasoning models that generate extended thinking traces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c669be9-6893-41e3-b8bd-6c9984c65156",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "56e64104-edce-4928-afea-bbc3d9c6cd74",
  "sourceToolAssistantUUID": "0c669be9-6893-41e3-b8bd-6c9984c65156",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-09T18:57:49.773Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ACwqRiqBvnYyr8kPbU9fAN`</summary>

```json
{
  "query": "arxiv 2602.08329 \"Near-Oracle KV Selection\" pre-hoc sparsity reasoning training-free abstract results",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56e64104-edce-4928-afea-bbc3d9c6cd74",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWMcrAf9Zr6dbX2SUe6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec5d4cbb-a09f-47c4-bf84-4044dae0ace6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KZEt8uWERskLzoDRwWCSbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 840,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 18901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 32 · 2026-05-09T18:57:50.541Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0114QbzWqfJrjMF2zHJGcSny`</summary>

```json
{
  "query": "arxiv LookaheadKV 2603.10899 query proxy future KV eviction reasoning training-free",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec5d4cbb-a09f-47c4-bf84-4044dae0ace6",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWMcrAf9Zr6dbX2SUe6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4087090b-57e2-4ef7-956c-77099b2be935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KZEt8uWERskLzoDRwWCSbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 840,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 18901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 33 · 2026-05-09T18:57:51.973Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R5XLFBXxy2qPB572JeLQnK`</summary>

```json
{
  "query": "arxiv 2504 2505 KV cache \"one-shot\" OR \"single-pass\" compression training-free reasoning DeepSeek-R1 thinking boundary 2026",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4087090b-57e2-4ef7-956c-77099b2be935",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWMcrAf9Zr6dbX2SUe6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39775fd1-34bf-4707-9eb8-63688de65b58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KZEt8uWERskLzoDRwWCSbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 840,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 18901,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 840,
          "output_tokens": 289,
          "cache_read_input_tokens": 18901,
          "cache_creation_input_tokens": 1956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1956,
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

_source line 34 · 2026-05-09T18:57:57.748Z_

<details><summary>↩ Tool result · `toolu_0114QbzWqfJrjMF2zHJGcSny`</summary>

```text
Web search results for query: "arxiv LookaheadKV 2603.10899 query proxy future KV eviction reasoning training-free"

Links: [{"title":"[2603.10899] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899"},{"title":"[2603.10899v1] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899v1"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/html/2603.10899"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by ...","url":"https://arxiv.org/pdf/2603.10899"},{"title":"Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query","url":"https://arxiv.org/html/2505.20334"},{"title":"[2505.20334] Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query","url":"https://arxiv.org/abs/2505.20334"},{"title":"Randomization Boosts KV Caching, Learning Balances Query Load: A Joint Perspective","url":"https://arxiv.org/html/2601.18999"},{"title":"Where Matters More Than What: Decoding-aligned KV Cache Compression via Position-aware Pseudo Queries","url":"https://arxiv.org/html/2603.11564"},{"title":"KV CACHE OPTIMIZATION STRATEGIES FOR SCALABLE AND EFFICIENT LLM INFERENCE","url":"https://arxiv.org/pdf/2603.20397"},{"title":"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs","url":"https://arxiv.org/html/2603.08727"}]

Based on the search results, I found detailed information about the LookaheadKV paper (arXiv:2603.10899). Here's what it covers:

## LookaheadKV Overview

LookaheadKV is a paper submitted on March 11, 2026 by authors including Jinwoo Ahn, Ingyu Seong, Akhil Kedia, and others from Samsung Research.

## The Problem It Addresses

Transformer-based large language models rely on key-value (KV) caching to avoid redundant computation during autoregressive inference, but the cache size grows linearly with input sequence length, becoming a bottleneck for long-context tasks.

## Key Innovation

LookaheadKV proposes a lightweight eviction framework that leverages surrogate future response without requiring explicit draft generation, augmenting transformer layers with parameter-efficient modules trained to predict true importance scores with high accuracy.

The method uses trainable soft lookahead tokens whose queries in each attention head are used to estimate the attention pattern of the true model response.

## Training-Free Aspect

During training, lookahead tokens and lookahead LoRA are trained to predict ground-truth importance scores obtained with pre-generated model response via a KL divergence loss.

## Performance Results

The method outperforms recent competitive baselines in various long-context understanding tasks and reduces eviction cost by up to 14.5x, leading to significantly faster time-to-first-token.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4087090b-57e2-4ef7-956c-77099b2be935",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "be06151e-b6fa-463f-b5f9-3f9728fa7814",
  "sourceToolAssistantUUID": "4087090b-57e2-4ef7-956c-77099b2be935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-09T18:57:58.229Z_

<details><summary>↩ Tool result · `toolu_01ACwqRiqBvnYyr8kPbU9fAN`</summary>

```text
Web search results for query: "arxiv 2602.08329 "Near-Oracle KV Selection" pre-hoc sparsity reasoning training-free abstract results"

Links: [{"title":"[2602.08329] Near-Oracle KV Selection via Pre-hoc Sparsity for Long-Context Inference","url":"https://arxiv.org/abs/2602.08329"},{"title":"Near-Oracle KV Selection via Pre-hoc Sparsity for Long-Context Inference","url":"https://arxiv.org/html/2602.08329"},{"title":"FASA: Frequency-Aware Sparse Attention","url":"https://arxiv.org/html/2602.03152"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.03560"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://arxiv.org/html/2508.15212v1"},{"title":"DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity","url":"https://arxiv.org/html/2602.08005"},{"title":"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding","url":"https://arxiv.org/html/2602.07223"},{"title":"[2602.03560] HySparse: A Hybrid Sparse Attention Architecture with Oracle Token Selection and KV Cache Sharing","url":"https://arxiv.org/abs/2602.03560"},{"title":"CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based Token Eviction","url":"https://arxiv.org/html/2504.14051"},{"title":"HillInfer: Efficient Long-Context LLM Inference on the Edge with Hierarchical KV Eviction using SmartSSD","url":"https://arxiv.org/html/2602.18750"}]

Based on the search results, I found comprehensive information about arxiv 2602.08329. Here's what the paper is about:

## Near-Oracle KV Selection via Pre-hoc Sparsity for Long-Context Inference

A core bottleneck in large language model (LLM) inference is the cost of attending over the ever-growing key-value (KV) cache. Although near-oracle top-k KV selection can preserve the quality of dense attention while sharply reducing computation and bandwidth, existing sparse methods generally rely on posterior heuristics, i.e., selectors conditioned on observed attention or proxy scores.

### The Problem with Posterior Approaches

Such conditioning introduces posterior bias: it tends to distort true token importance and miss salient tokens, thereby impairing long-range reasoning.

### The Proposed Solution: Pre-hoc Sparsity (PrHS)

To tackle this problem, the authors propose Pre-hoc Sparsity (PrHS), which selects KV entries before attention scoring and provides explicit accuracy control. Through a marginal-to-mutual-information analysis, they derive an upper bound on the mutual-information loss that depends only on the dropped mass.

### Key Techniques

Within PrHS, three orthogonal pre-hoc selectors are instantiated along the axes of time, depth, and layer.

### Experimental Results

Across GSM8K and CoQA, PrHS reduces retrieval overhead by over 90%, achieving 3x higher retrieval sparsity than HShare at matched or better accuracy. It incurs under 1% average degradation on LongBench, lowers attention FLOPs by about 15% versus prior sparse baselines, and yields a 9.9x speedup in attention-operator latency and 2.8x higher throughput on NVIDIA A100-80GB GPUs than the dense baseline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec5d4cbb-a09f-47c4-bf84-4044dae0ace6",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "222587f8-be19-475f-94ca-a6c2dd3f974b",
  "sourceToolAssistantUUID": "ec5d4cbb-a09f-47c4-bf84-4044dae0ace6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-09T18:58:00.607Z_

<details><summary>↩ Tool result · `toolu_01R5XLFBXxy2qPB572JeLQnK`</summary>

```text
Web search results for query: "arxiv 2504 2505 KV cache "one-shot" OR "single-pass" compression training-free reasoning DeepSeek-R1 thinking boundary 2026"

Links: [{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding","url":"https://arxiv.org/html/2505.22618v1"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via","url":"https://arxiv.org/pdf/2501.12948"},{"title":"[2501.12948] DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2501.12948"},{"title":"Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning","url":"https://arxiv.org/html/2503.04973v1"},{"title":"Can LLMs Maintain Fundamental Abilities under KV Cache Compression?","url":"https://arxiv.org/html/2502.01941v2"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://arxiv.org/html/2506.05345v1"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"KVzap: Fast, Adaptive, and Faithful KV Cache Pruning","url":"https://arxiv.org/html/2601.07891"}]

The search returned several highly relevant papers on KV cache compression and reasoning models. Here are the key findings:

## Papers Found

**1. Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution**
This paper introduces Expected Attention, a training-free compression method that estimates KV pairs importance by predicting how future queries will attend to them, leveraging distributional properties of LLM activations to compute expected attention scores in closed form. For prefilling (one-shot compression before generation), it tests on Llama3.1-8B, Qwen3-8B, and Gemma3-12B, while for decoding, it analyzes reasoning models including Qwen-15B-R1 and Qwen-7B-R1.

**2. Utilizing KV Cache for Sampling and Reasoning**
This paper deploys strategies on DeepSeek-R1-14B and Qwen3-8B, with a design that directly reuses the KV cache available during decoding, introduces negligible VRAM or FLOPs overhead, and functions as a modular component.

**3. Can LLMs Maintain Fundamental Abilities under KV Cache Compression?**
The paper notes that reasoning LLMs demonstrate enhanced robustness to KV cache compression, and multi-step reasoning LLMs are more robust to KV cache compression.

**4. Inference-Time Hyper-Scaling with KV Cache Compression**
This paper addresses scaling inference-time compute in models such as OpenAI's o1 or DeepSeek's R1, which trade increased inference time and memory for higher reasoning accuracy.

**5. KVzap: Fast, Adaptive, and Faithful KV Cache Pruning**
KVzap is a fast, input-adaptive approximation that works in both prefilling and decoding, achieving 4× KV cache compression with negligible accuracy loss.

These papers represent recent work (April-June 2025) addressing training-free and efficient KV cache compression for reasoning models like DeepSeek-R1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39775fd1-34bf-4707-9eb8-63688de65b58",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "fd5c381c-4873-4003-8693-8c18b5bc7fa6",
  "sourceToolAssistantUUID": "39775fd1-34bf-4707-9eb8-63688de65b58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-09T18:58:04.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CXDghKDSbgSpEMnHRdDV5F`</summary>

```json
{
  "query": "arxiv 2505.20334 \"Lookahead Q-Cache\" pseudo query KV eviction training-free reasoning abstract",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd5c381c-4873-4003-8693-8c18b5bc7fa6",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWNcmj82RPryZBAhxrf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e2898e4-2796-4b0b-8115-d41ac2bf141e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G5fgakqGVCNF3aPCCp7xsX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3992,
      "cache_read_input_tokens": 20857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3992,
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

_source line 38 · 2026-05-09T18:58:05.088Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019jQWsKT3y7dWLYVgoLnmus`</summary>

```json
{
  "query": "arxiv 2603.11564 \"Position-aware Pseudo Queries\" decoding-aligned KV cache compression reasoning",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e2898e4-2796-4b0b-8115-d41ac2bf141e",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWNcmj82RPryZBAhxrf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8c4b64a-5a29-4610-b07b-2e4e7ca4e36e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G5fgakqGVCNF3aPCCp7xsX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3992,
      "cache_read_input_tokens": 20857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3992,
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

_source line 39 · 2026-05-09T18:58:05.772Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LbUh95dMWvfaCcW4qcgohw`</summary>

```json
{
  "query": "arxiv 2504.15364 KeyDiff key similarity KV cache eviction training-free reasoning April 2025",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8c4b64a-5a29-4610-b07b-2e4e7ca4e36e",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWNcmj82RPryZBAhxrf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0855173-2438-4423-a7e2-88bb9abcbf86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G5fgakqGVCNF3aPCCp7xsX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3992,
      "cache_read_input_tokens": 20857,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3992
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 274,
          "cache_read_input_tokens": 20857,
          "cache_creation_input_tokens": 3992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3992,
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

_source line 40 · 2026-05-09T18:58:10.502Z_

<details><summary>↩ Tool result · `toolu_01CXDghKDSbgSpEMnHRdDV5F`</summary>

```text
Web search results for query: "arxiv 2505.20334 "Lookahead Q-Cache" pseudo query KV eviction training-free reasoning abstract"

Links: [{"title":"Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query","url":"https://arxiv.org/pdf/2505.20334"},{"title":"[2505.20334] Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query","url":"https://arxiv.org/abs/2505.20334"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/html/2603.10899v1"},{"title":"Judge Q: Trainable Queries for Optimized Information Retention in KV Cache Eviction","url":"https://arxiv.org/html/2509.10798"},{"title":"[2603.10899v1] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899v1"},{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=1550&show=250"},{"title":"[2603.10899] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/html/2604.25975"}]

I found the paper you're looking for. Here's information about arxiv paper 2505.20334:

**Title:** Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query

**Abstract:**

Large language models (LLMs) rely on key-value cache (KV cache) to accelerate decoding by reducing redundant computations. However, the KV cache memory usage grows substantially with longer text sequences, posing challenges for efficient deployment.

Existing KV cache eviction methods prune tokens using prefilling-stage attention scores, causing inconsistency with actual inference queries, especially under tight memory budgets. The paper proposes Lookahead Q-Cache (LAQ), a novel eviction framework that generates low-cost pseudo lookahead queries to better approximate the true decoding-stage queries.

By using these lookahead queries as the observation window for importance estimation, LAQ achieves more consistent and accurate KV cache eviction aligned with real inference scenarios.

The paper addresses the key problem of inconsistency between KV cache compression strategies (which use prefilling-stage information) and actual inference requirements (which occur during decoding), proposing pseudo queries as a training-free solution to improve cache eviction accuracy under memory constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e2898e4-2796-4b0b-8115-d41ac2bf141e",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "7fbc72bd-0fdb-4593-8d27-5269158cd414",
  "sourceToolAssistantUUID": "0e2898e4-2796-4b0b-8115-d41ac2bf141e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-09T18:58:10.521Z_

<details><summary>↩ Tool result · `toolu_019jQWsKT3y7dWLYVgoLnmus`</summary>

```text
Web search results for query: "arxiv 2603.11564 "Position-aware Pseudo Queries" decoding-aligned KV cache compression reasoning"

Links: [{"title":"[2603.11564] Where Matters More Than What: Decoding-aligned KV Cache Compression via Position-aware Pseudo Queries","url":"https://arxiv.org/abs/2603.11564"},{"title":"Where Matters More Than What: Decoding-aligned KV Cache Compression via Position-aware Pseudo Queries","url":"https://arxiv.org/html/2603.11564"},{"title":"Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query","url":"https://arxiv.org/html/2505.20334"},{"title":"A2ATS: Retrieval-Based KV Cache Reduction via Windowed Rotary Position Embedding and Query-Aware Vector Quantization","url":"https://arxiv.org/html/2502.12665"},{"title":"Compactor: Calibrated Query-Agnostic KV Cache Compression with Approximate Leverage Scores","url":"https://arxiv.org/html/2507.08143v1"},{"title":"One Size Does Not Fit All: Token-Wise Adaptive Compression for KV Cache","url":"https://arxiv.org/html/2603.04411"},{"title":"SQuat: Subspace-orthogonal KV Cache Quantization","url":"https://arxiv.org/html/2503.24358v2"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"}]

Based on the search results, I found the arxiv paper you're looking for. Here's what the research is about:

The paper addresses KV cache compression for LLM inference. Existing methods rely on input-side attention patterns during the prefill stage but fail to preserve critical tokens for future generation since these assessments aren't derived from the decoding process.

The key insight is that an effective observation window should mirror decoding-stage queries to reflect which tokens the generation process will attend to. However, since ground-truth decoding queries aren't available during inference, the authors find that positional information plays a more critical role than semantic content when constructing pseudo queries to approximate them.

The paper is titled **"Where Matters More Than What: Decoding-aligned KV Cache Compression via Position-aware Pseudo Queries"** and was submitted to arxiv on March 12, 2026. The authors are from Soochow University in China.

The DapQ (decoding-aligned KV cache compression via position-aware pseudo queries) method represents a novel approach to the KV cache compression problem by prioritizing positional information in pseudo query construction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8c4b64a-5a29-4610-b07b-2e4e7ca4e36e",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "1f646b35-00ba-410a-b952-72f534188d5b",
  "sourceToolAssistantUUID": "c8c4b64a-5a29-4610-b07b-2e4e7ca4e36e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-09T18:58:13.544Z_

<details><summary>↩ Tool result · `toolu_01LbUh95dMWvfaCcW4qcgohw`</summary>

```text
Web search results for query: "arxiv 2504.15364 KeyDiff key similarity KV cache eviction training-free reasoning April 2025"

Links: [{"title":"[2504.15364] KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/abs/2504.15364"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/html/2504.15364v1"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"EpiCache: Episodic KV Cache Management for Long ...","url":"https://arxiv.org/pdf/2509.17396"},{"title":"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://arxiv.org/html/2509.17396v1"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference","url":"https://arxiv.org/html/2509.04377v1"},{"title":"Learning to Evict from Key-Value Cache","url":"https://arxiv.org/html/2602.10238"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/html/2603.10899"},{"title":"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/html/2604.25975"}]

Based on the search results, here's information about arxiv paper 2504.15364:

## KeyDiff: Key Similarity-Based KV Cache Eviction

KeyDiff is a training-free KV cache eviction method based solely on key similarity. The method is motivated by the observation that geometrically distinctive keys during LLM inference tend to have high attention scores.

### Key Features

Unlike other KV cache eviction methods, KeyDiff can process arbitrarily long prompts within strict resource constraints and efficiently generate responses. Notably KeyDiff does not rely on attention scores, allowing the use of optimized attention mechanisms like FlashAttention.

### How It Works

KeyDiff evicts keys from the cache with the highest cosine similarity to a cache representative called an anchor. The method provides a theoretical basis by relating key diversity with attention scores, implying KeyDiff can efficiently identify the most important tokens to retain.

### Performance

Under a strict memory allowance of 8K cache budget (approximately 23% KV cache reduction), the method demonstrates a performance gap of less than 0.04% from the non-evicting baseline on LongBench for Llama 3.1-8B and Llama 3.2-3B. The method shows near baseline performance for Deepseek-R1-Distill-Llama-8B on the Math500 reasoning benchmark and decreases end-to-end inference latency by up to 30% compared to other token-eviction methods.

The paper was submitted in April 2025 and is authored by Junyoung Park and collaborators.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0855173-2438-4423-a7e2-88bb9abcbf86",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "ff03d217-9339-4d9d-b304-2be80ebbe366",
  "sourceToolAssistantUUID": "d0855173-2438-4423-a7e2-88bb9abcbf86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-09T18:58:17.046Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J9vjapwQS6WABbFryCXahg`</summary>

```json
{
  "query": "arxiv 2505 2504 \"think\" OR \"reasoning\" KV cache \"evict\" OR \"prune\" \"end of\" training-free one-shot DeepSeek AIME 2026 April May",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff03d217-9339-4d9d-b304-2be80ebbe366",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWPa81bmsFVXoyUGke6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f64921f-6114-46ec-8f32-0506ebb5aa62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015TBLmTGpydPFg2x35zDott",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2797,
      "cache_read_input_tokens": 24849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2797,
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

_source line 44 · 2026-05-09T18:58:18.098Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015eiZy7iigHMVLxeQ6SVpMv`</summary>

```json
{
  "query": "arxiv ReCalKV 2505.24357 low-rank KV compression head reordering offline reasoning abstract",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f64921f-6114-46ec-8f32-0506ebb5aa62",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWPa81bmsFVXoyUGke6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b7fc775-853d-4b8e-871e-7482407db1e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015TBLmTGpydPFg2x35zDott",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2797,
      "cache_read_input_tokens": 24849,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2797
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 24849,
          "cache_creation_input_tokens": 2797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2797,
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

_source line 45 · 2026-05-09T18:58:24.431Z_

<details><summary>↩ Tool result · `toolu_015eiZy7iigHMVLxeQ6SVpMv`</summary>

```text
Web search results for query: "arxiv ReCalKV 2505.24357 low-rank KV compression head reordering offline reasoning abstract"

Links: [{"title":"[2505.24357] ReCalKV: Low-Rank KV Cache Compression via Head Reordering and Offline Calibration","url":"https://arxiv.org/abs/2505.24357"},{"title":"ReCalKV: Low-Rank KV Cache Compression via Head Reordering and Offline Calibration","url":"https://arxiv.org/html/2505.24357"},{"title":"Joint Encoding of KV-Cache Blocks for Scalable LLM Serving","url":"https://arxiv.org/html/2601.03067"},{"title":"XQuant: Breaking the Memory Wall for LLM Inference with KV Cache Rematerialization","url":"https://arxiv.org/html/2508.10395v1"},{"title":"OjaKV: Context-Aware Online Low-Rank KV Cache Compression with Oja’s Rule","url":"https://arxiv.org/html/2509.21623v1"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"XQuant: Breaking the Memory Wall for LLM Inference with ...","url":"https://arxiv.org/pdf/2508.10395"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=22925&show=2000"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration","url":"https://arxiv.org/html/2505.24133v1"},{"title":"One Size Does Not Fit All: Token-Wise Adaptive Compression for KV Cache","url":"https://arxiv.org/html/2603.04411"}]

Based on the search results, I found detailed information about the ReCalKV paper (arxiv 2505.24357). Here's the abstract and key details:

## ReCalKV: Low-Rank KV Cache Compression via Head Reordering and Offline Calibration

**Abstract:**

Large language models (LLMs) have demonstrated remarkable performance, but their long-context reasoning remains constrained by the excessive memory required for the Key-Value (KV) cache. This makes KV cache compression a critical step toward efficient long-context inference. Recent methods have explored low-rank techniques to reduce the hidden size of the KV cache. However, they neglect the distinct roles and varying importance of Keys and Values, leading to significant performance drops under high compression.

**Main Contributions:**

ReCalKV is a post-training low-rank KV cache compression approach with tailored strategies for Keys and Values. For Keys, it proposes Head-wise Similarity aware Reordering (HSR), which clusters structurally similar heads into groups, enabling more accurate low-rank approximation via grouped SVD. For Values, it introduces Offline Value Calibration (OVC) to refine Value projection matrices using calibration data to ensure accurate contextual representation.

**Results:**

Extensive experiments show that ReCalKV consistently outperforms existing low-rank compression methods, achieving high compression ratios with minimal performance loss. For example, on the LLaMA-2-7B model evaluated on six zero-shot QA datasets, ReCalKV achieves an average accuracy of 63.64% under a 50% KV cache compression ratio, compared to 64.99% for the full-precision model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b7fc775-853d-4b8e-871e-7482407db1e3",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "8189b5ea-c4f0-4975-8a65-ee5c4c30c8a4",
  "sourceToolAssistantUUID": "0b7fc775-853d-4b8e-871e-7482407db1e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-09T18:58:24.697Z_

<details><summary>↩ Tool result · `toolu_01J9vjapwQS6WABbFryCXahg`</summary>

```text
Web search results for query: "arxiv 2505 2504 "think" OR "reasoning" KV cache "evict" OR "prune" "end of" training-free one-shot DeepSeek AIME 2026 April May"

Links: [{"title":"R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration","url":"https://arxiv.org/html/2505.24133v1"},{"title":"R-KV: Redundancy-aware KV Cache Compression for ...","url":"https://arxiv.org/pdf/2505.24133"},{"title":"Towards Threshold-Free KV Cache Pruning","url":"https://arxiv.org/html/2502.16886"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203v1"},{"title":"Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning","url":"https://arxiv.org/html/2505.16950"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://arxiv.org/html/2511.06029"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference","url":"https://arxiv.org/html/2505.13109v4"},{"title":"CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based","url":"https://arxiv.org/pdf/2504.14051"}]

Based on the search results, I found a highly relevant paper that matches several key terms from your query:

## R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models

R-KV proposes redundancy-aware KV cache compression for reasoning models, with three key components: an attention-based importance scoring mechanism, a dynamic redundancy scoring mechanism that identifies repetitive tokens through real-time analysis of key vectors, and a joint eviction mechanism that balances both redundancy and importance.

By selectively retaining only 10-34% of the original KV cache, R-KV achieves comparable performance with the uncompressed reasoning model, outperforming state-of-the-art compression baselines. Remarkably, R-KV achieves 105% accuracy of the full KV baseline with around 16% of the KV cache using DeepSeek-R1-Distill-Llama-8B on the AIME-24 dataset.

This paper is from May 2025 (arxiv 2505.24133), and directly addresses KV cache eviction/pruning for reasoning models with training-free methods, specifically tested on DeepSeek models and AIME benchmarks.

I also found several other related papers on KV cache compression and pruning from the same timeframe:
- ReFreeKV is a threshold-free KV cache pruning method that ranks tokens by position and evicts the least significant tokens based on attention matrix norm values
- Lethe is evaluated on reasoning-oriented models from the DeepSeek-R1-Distill family
- ThinKV references R-KV as a recent work on redundancy-aware KV cache compression for training-free reasoning models (arxiv 2505.24133)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f64921f-6114-46ec-8f32-0506ebb5aa62",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "0e478fb3-8fa6-49f0-ad2f-1a311f4fecbd",
  "sourceToolAssistantUUID": "6f64921f-6114-46ec-8f32-0506ebb5aa62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-09T18:58:29.129Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RStySBiknXBPE6rJLmytqB`</summary>

```json
{
  "query": "arxiv 2505 2504 KV cache compression \"think\" token boundary triggered reasoning DeepSeek-R1 training-free April May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e478fb3-8fa6-49f0-ad2f-1a311f4fecbd",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWQPogC27RJYqNFmMoi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67f138d9-9942-40f3-863e-cd97ac37ff97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BmZtyNZWW8o2kSwbe9uNaY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 903,
      "cache_creation_input_tokens": 1260,
      "cache_read_input_tokens": 27646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1260,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-09T18:58:30.342Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ENWzus3TdCNsF5QhWWHzGj`</summary>

```json
{
  "query": "arxiv \"conclusion token\" OR \"answer token\" query proxy KV importance scoring reasoning model 2025 2026",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67f138d9-9942-40f3-863e-cd97ac37ff97",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWQPogC27RJYqNFmMoi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d2be16c-887f-42ae-9052-f3ec8094d9c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BmZtyNZWW8o2kSwbe9uNaY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 903,
      "cache_creation_input_tokens": 1260,
      "cache_read_input_tokens": 27646,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1260
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 903,
          "output_tokens": 170,
          "cache_read_input_tokens": 27646,
          "cache_creation_input_tokens": 1260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1260,
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

_source line 49 · 2026-05-09T18:58:35.729Z_

<details><summary>↩ Tool result · `toolu_01RStySBiknXBPE6rJLmytqB`</summary>

```text
Web search results for query: "arxiv 2505 2504 KV cache compression "think" token boundary triggered reasoning DeepSeek-R1 training-free April May 2026"

Links: [{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"[2510.01290v1] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290v1"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://arxiv.org/html/2506.05345v1"},{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"THINKV: THOUGHT-ADAPTIVE KV CACHE COM- PRESSION FOR EFFICIENT REASONING MODELS","url":"https://arxiv.org/pdf/2510.01290v1"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290"},{"title":"KVReviver: Reversible KV Cache Compression with Sketch-Based Token Reconstruction","url":"https://arxiv.org/html/2512.17917"}]

Based on my search results, I found several relevant papers on KV cache compression for reasoning models. Here are the key findings:

## Key Papers Found

**ThinKV** (arXiv 2510.01290) proposes a thought-adaptive KV cache compression framework based on the observation that attention sparsity reveals distinct thought types with varying importance within the chain-of-thought (CoT).

Recent research evaluates KV cache compression on reasoning models including Qwen-7B-R1 and Qwen-15B-R1, analyzing models that generate extensive intermediate reasoning tokens and therefore large KV caches.

R-KV is a training-free and model-agnostic method for KV cache compression that can be used in the rollout process in reinforcement learning and LLM serving.

Expected Attention is a training-free algorithm for KV cache compression.

Recent evaluations test DeepSeek-R1-Distill-Qwen-7B/14B and DeepSeek-R1-Distill-Llama-8B reasoning models for KV cache compression.

The papers I found discuss various training-free KV cache compression methods applied to reasoning models like DeepSeek-R1 variants, though the specific combination of all elements in your query (boundary-triggered reasoning with explicit "think" token detection) may require examining the full paper PDFs for implementation details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67f138d9-9942-40f3-863e-cd97ac37ff97",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "2d87d535-b88a-4341-9216-1c8eca84ff7b",
  "sourceToolAssistantUUID": "67f138d9-9942-40f3-863e-cd97ac37ff97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-09T18:58:38.812Z_

<details><summary>↩ Tool result · `toolu_01ENWzus3TdCNsF5QhWWHzGj`</summary>

```text
Web search results for query: "arxiv "conclusion token" OR "answer token" query proxy KV importance scoring reasoning model 2025 2026"

Links: [{"title":"CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based Token Eviction","url":"https://arxiv.org/html/2504.14051"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/html/2512.03324v2"},{"title":"CAOTE: KV Caching through Attention Output Error based Token Eviction","url":"https://arxiv.org/html/2504.14051v1"},{"title":"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning","url":"https://arxiv.org/html/2506.15969v1"},{"title":"arXiv:2412.16187v3 [cs.LG] 4 Jun 2025","url":"https://arxiv.org/pdf/2412.16187"},{"title":"CAOTE: KV Cache Eviction for LLMs via Attention Output Error-Based Token Selection","url":"https://arxiv.org/html/2504.14051v4"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.03152"},{"title":"State over Tokens: Characterizing the Role of Reasoning Tokens Mosh Levy","url":"https://arxiv.org/pdf/2512.12777"},{"title":"Attention Score is not All You Need for Token Importance Indicator in KV Cache Reduction: Value Also Matters","url":"https://arxiv.org/html/2406.12335v2"}]

I've found several relevant papers from arXiv in 2025-2026 related to your search query about KV cache optimization, token importance scoring, and reasoning models. Here's a summary of the key results:

## Key Papers Found:

1. **CAOTE: KV Cache Selection via Attention Output Error** (April-August 2025)
   Token eviction typically uses attention scores as proxy metrics for token importance, but CAOTE proposes an eviction criterion based on the contribution of cached tokens to attention outputs, integrating attention scores and value vectors.

2. **Utilizing KV Cache for Sampling and Reasoning** (January 2026)
   This work investigates whether the KV cache alone suffices to support reasoning subtasks, showing that pooled KV-cache features can drive switching through simple control tokens, without storing hidden states or altering model architecture.

3. **Cache What Lasts: Token Retention for Memory-Bounded KV Cache** (March 2026)
   Each gate predicts a scalar retention score that decays over time, reflecting the long-term utility of the token for a specific layer and head, with low-scoring tokens evicted when memory budget is exceeded.

4. **LazyEviction: Lagged KV Eviction for Efficient Long Reasoning** (June 2025)
   This observes Token Importance Recurrence in reasoning tasks where tokens exhibit recurrent attention patterns, and proposes a framework that enables prediction of future token importance to prevent premature eviction.

5. **HASHEVICT: Non-Attentive KV Cache Compression** (2025)
   HASHEVICT determines token eviction pre-attention via locality-sensitive hashing, evicting past tokens whose key embeddings are highly cosine dissimilar to the current query token embedding.

These papers collectively address KV cache optimization for long-context reasoning in LLMs using various token importance scoring strategies beyond simple attention-based metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d2be16c-887f-42ae-9052-f3ec8094d9c4",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "0dcccd4c-faee-45e8-980f-3039fc3b8ff2",
  "sourceToolAssistantUUID": "4d2be16c-887f-42ae-9052-f3ec8094d9c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-09T18:58:46.865Z_

I now have sufficient data to compile a comprehensive, well-structured report. Let me do one final targeted sweep for anything specifically about the `&lt;/think>` boundary trigger and any April-May 2026 papers I may have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dcccd4c-faee-45e8-980f-3039fc3b8ff2",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWRSA5zb3X3rdBcxcEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5edaed8b-5f8b-4560-a84b-ec6a20ab7797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SrMYADVhH8i9EsGZr4QYFT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 28906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2869,
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

_source line 52 · 2026-05-09T18:58:48.640Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R17cAzaG5WVaMUKG3pgyuo`</summary>

```json
{
  "query": "arxiv April May 2026 KV cache reasoning model compression \"2504\" OR \"2505\" training-free eviction AIME math500",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5edaed8b-5f8b-4560-a84b-ec6a20ab7797",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWRSA5zb3X3rdBcxcEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f844c202-2ae7-46ec-a05b-96a6435f0665",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SrMYADVhH8i9EsGZr4QYFT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 28906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2869,
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

_source line 53 · 2026-05-09T18:58:49.559Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DYYMyAHKuienPwDF1GXD83`</summary>

```json
{
  "query": "arxiv 2504 2505 \"think phase\" OR \"thinking phase\" OR \"chain-of-thought\" KV cache compression boundary one-shot 2026",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f844c202-2ae7-46ec-a05b-96a6435f0665",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWRSA5zb3X3rdBcxcEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3c86dc9-26de-49ee-865a-9a45db279ab4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SrMYADVhH8i9EsGZr4QYFT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 28906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2869,
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

_source line 54 · 2026-05-09T18:58:57.081Z_

<details><summary>↩ Tool result · `toolu_01DYYMyAHKuienPwDF1GXD83`</summary>

```text
Web search results for query: "arxiv 2504 2505 "think phase" OR "thinking phase" OR "chain-of-thought" KV cache compression boundary one-shot 2026"

Links: [{"title":"Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning","url":"https://arxiv.org/html/2505.16950"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"[2505.24133] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/abs/2505.24133"},{"title":"R-KV: Redundancy-aware KV Cache Compression for ...","url":"https://arxiv.org/pdf/2505.24133"},{"title":"[2512.12008] Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/abs/2512.12008"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"[2510.01290v1] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290v1"}]

Based on the search results, I found several relevant arxiv papers from 2024-2026 that address KV cache compression for reasoning models with chain-of-thought. Here are the key papers:

## Papers from 2505 (May 2025) and related:

1. **ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models** (arXiv:2510.01290)
   - Addresses KV cache growth during extended chain of thought generation through a thought-adaptive compression framework based on attention sparsity that reveals distinct thought types with varying importance, applying a hybrid quantization-eviction strategy.

2. **R-KV: Redundancy-aware KV Cache Compression for Reasoning Models** (arXiv:2505.24133)
   - Targets reasoning models' long outputs and KV cache growth by proposing a redundancy-aware compression method specifically addressing reasoning failures when using existing KV cache compression approaches.
   - Preserves nearly 100% of full KV cache performance using only 10% of the KV cache, and achieves 105% of full KV cache performance with 16% of the KV cache.

3. **Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning** (arXiv:2505.16950)
   - Discusses transformer LLMs with reasoning abilities that scale with inference-time compute through token-space "thinking" chains of thought, exploring auxiliary latent-space computation including memory compression.

4. **Hold Onto That Thought: Assessing KV Cache Compression On Reasoning** (arXiv:2512.12008)
   - Examines KV cache compression strategies and their impact on reasoning model performance.

5. **Utilizing KV Cache for Sampling and Reasoning** (arXiv:2601.20326)
   - Introduces KV Cache Steering, a one-shot intervention that adds layer-wise steering vectors to the key and value tensors after prefill, reliably inducing longer and more structured reasoning.

These papers collectively address the challenge of managing KV cache growth during extended chain-of-thought reasoning in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3c86dc9-26de-49ee-865a-9a45db279ab4",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "f10e33a7-30b9-4cc6-985f-cbf1a1a74880",
  "sourceToolAssistantUUID": "f3c86dc9-26de-49ee-865a-9a45db279ab4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-09T18:58:57.705Z_

<details><summary>↩ Tool result · `toolu_01R17cAzaG5WVaMUKG3pgyuo`</summary>

```text
Web search results for query: "arxiv April May 2026 KV cache reasoning model compression "2504" OR "2505" training-free eviction AIME math500"

Links: [{"title":"R-KV: Redundancy-aware KV Cache Compression for ...","url":"https://arxiv.org/pdf/2505.24133"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration","url":"https://arxiv.org/html/2505.24133v1"},{"title":"Redundancy-aware KV Cache Compression for Training- ...","url":"https://www.arxiv.org/pdf/2505.24133v2"},{"title":"Reasoning Path Compression: Compressing","url":"https://arxiv.org/pdf/2505.13866"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://arxiv.org/html/2506.05345v1"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"G-KV: Decoding-Time KV Cache Eviction with Global Attention","url":"https://arxiv.org/html/2512.00504"},{"title":"CodeComp: Structural KV Cache Compression for Agentic Coding","url":"https://arxiv.org/html/2604.10235"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203v1"}]

Based on my search results, I found several highly relevant papers from April-May 2026 (arXiv IDs 2504-2505) on KV cache compression for reasoning models with training-free eviction methods, evaluated on AIME and MATH-500 benchmarks:

## Key Findings:

### R-KV: Redundancy-aware KV Cache Compression (arXiv:2505.24133)

R-KV proposes a redundancy-aware KV cache compression for reasoning models consisting of three key components: (1) an attention-based importance scoring mechanism that selects critical tokens for retention, (2) a dynamic redundancy scoring mechanism that identifies repetitive tokens through real-time analysis of key vectors, and (3) a joint eviction mechanism that balances both redundancy and importance to optimize cache efficiency.

**Performance Results:**
- By selectively retaining only 10-34% of the original KV cache, R-KV achieves comparable performance parity with the uncompressed reasoning model, outperforming state-of-the-art compression baselines with only 60% of the performance.
- R-KV even achieves 105% accuracy of the full KV baseline with around 16% of the KV cache using DeepSeek-R1-Distill-Llama-8B on the AIME-24 dataset.
- For R1-Qwen-14B, R-KV achieves lossless compression with 54% KV cache budget on the MATH-500 dataset and with 25% KV cache budget on the AIME-2024 dataset.

### Reasoning Path Compression (arXiv:2505.13866)

Reasoning Path Compression (RPC) for compressing KV cache of reasoning LLMs observes that reasoning paths often contain redundant segments and inherent semantic sparsity, leveraging this characteristic by periodically compressing the KV cache and employs an importance scoring mechanism based on a selector window composed of recent queries, and as RPC does not require any additional training or model modifications, it can be applied to a broad range of reasoning models.

These papers represent significant advances in training-free KV cache compression specifically optimized for reasoning models on mathematical benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f844c202-2ae7-46ec-a05b-96a6435f0665",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "524f43da-b622-4ee9-98d5-af252f37a606",
  "sourceToolAssistantUUID": "f844c202-2ae7-46ec-a05b-96a6435f0665",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-09T18:59:01.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RhPtZmJfPyak1af6z2EQKH`</summary>

```json
{
  "query": "arxiv 2505.13866 \"Reasoning Path Compression\" RPC KV cache periodic training-free AIME abstract",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "524f43da-b622-4ee9-98d5-af252f37a606",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWSpvLNc7C4YrBmVq9h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c10c644-d0cf-421d-9179-d5c595942dc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0111AqbWPiLnGfdJYdpif356",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1033,
      "cache_creation_input_tokens": 1261,
      "cache_read_input_tokens": 31775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1261,
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

_source line 57 · 2026-05-09T18:59:02.587Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011qj3TY2LtnRXEof624rDvg`</summary>

```json
{
  "query": "arxiv 2604.25975 \"Rethinking KV Cache Eviction\" unified information-theoretic reasoning results",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c10c644-d0cf-421d-9179-d5c595942dc4",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWSpvLNc7C4YrBmVq9h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c534bd9d-448c-4af5-81fa-340a7e6a56e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0111AqbWPiLnGfdJYdpif356",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1033,
      "cache_creation_input_tokens": 1261,
      "cache_read_input_tokens": 31775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1261,
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

### Tool result

_source line 58 · 2026-05-09T18:59:08.805Z_

<details><summary>↩ Tool result · `toolu_01RhPtZmJfPyak1af6z2EQKH`</summary>

```text
Web search results for query: "arxiv 2505.13866 "Reasoning Path Compression" RPC KV cache periodic training-free AIME abstract"

Links: [{"title":"[2505.13866] Reasoning Path Compression: Compressing Generation Trajectories for Efficient LLM Reasoning","url":"https://arxiv.org/abs/2505.13866"},{"title":"Reasoning Path Compression: Compressing","url":"https://arxiv.org/pdf/2505.13866"},{"title":"Reasoning Path Compression: Compressing Generation Trajectories for Efficient LLM Reasoning","url":"https://arxiv.org/html/2505.13866v2"},{"title":"arXiv:2505.13866v1 [cs.CL] 20 May 2025","url":"https://arxiv.org/pdf/2505.13866v1"},{"title":"A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings","url":"https://arxiv.org/html/2505.24550"},{"title":"[2505.24550] A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings","url":"https://arxiv.org/abs/2505.24550"},{"title":"When Do Hallucinations Arise? A Graph Perspective on the Evolution of Path Reuse and Path Compression","url":"https://arxiv.org/html/2604.03557v1"},{"title":"[2505.16552v1] Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains","url":"https://arxiv.org/abs/2505.16552v1"},{"title":"SCOPE: Compress Mathematical Reasoning Steps for Efficient Automated Process Annotation","url":"https://arxiv.org/html/2505.14419"},{"title":"DeepCompress: A Dual Reward Strategy for Dynamically Exploring and Compressing Reasoning Chains","url":"https://arxiv.org/html/2510.27419"}]

I found the paper! Here's the information about arxiv 2505.13866:

## Paper Summary

**Title:** Reasoning Path Compression: Compressing Generation Trajectories for Efficient LLM Reasoning - Recent reasoning-focused language models achieve high accuracy by generating lengthy intermediate reasoning paths before producing final answers. While this approach is effective in solving problems that require logical thinking, long reasoning paths significantly increase memory usage and reduce throughput of token generation, limiting the practical deployment of such models. The paper proposes Reasoning Path Compression (RPC), a training-free method that accelerates inference by leveraging the semantic sparsity of reasoning paths.

**Key Method Details:**

RPC periodically compresses the KV cache by retaining cache entries that receive high importance score, which are computed using a selector window composed of recently generated queries.

**Results:**

Experiments show that RPC improves generation throughput of QwQ-32B by up to 1.60× compared to the inference with full KV cache, with an accuracy drop of 1.2% on the AIME 2024 benchmark.

**Authors:** Jiwon Song, Dongwon Jo, Yulhwa Kim, and Jae-Joon Kim (from Seoul National University and Sungkyunkwan University)

The paper was submitted on May 20, 2025, with the latest version (v2) dated October 24, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c10c644-d0cf-421d-9179-d5c595942dc4",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "b8627ef7-acbc-4d90-b92d-fdfae97f91bf",
  "sourceToolAssistantUUID": "4c10c644-d0cf-421d-9179-d5c595942dc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-09T18:59:09.471Z_

<details><summary>↩ Tool result · `toolu_011qj3TY2LtnRXEof624rDvg`</summary>

```text
Web search results for query: "arxiv 2604.25975 "Rethinking KV Cache Eviction" unified information-theoretic reasoning results"

Links: [{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"},{"title":"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/html/2604.25975"},{"title":"[2605.04075] RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/abs/2605.04075"},{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"},{"title":"TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference","url":"https://arxiv.org/html/2604.19769"},{"title":"CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences","url":"https://arxiv.org/html/2503.12491v2"},{"title":"IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs","url":"https://arxiv.org/html/2604.10539"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"MPCache: MPC-Friendly KV Cache Eviction For Efficient Private LLM Inference","url":"https://arxiv.org/html/2501.06807"},{"title":"Learning to Evict from Key-Value Cache","url":"https://arxiv.org/html/2602.10238v1"}]

I found the paper you're looking for! Here's what the search revealed about arxiv 2604.25975:

## Paper Overview

The paper is titled "Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective" by authors Jiaming Yang, Chenwei Tang, Liangli Zhen, and Jiancheng Lv, submitted on April 28, 2026.

## Key Contributions

The work addresses how existing eviction policies predominantly rely on empirical heuristics lacking rigorous theoretical foundation, and rethinks KV cache eviction through the lens of the Information Bottleneck principle.

Under a linear-Gaussian surrogate of attention, the authors derive a closed-form mutual information objective that characterizes the effective information capacity of a retained KV cache subset.

The formulation reveals that a wide range of existing eviction strategies can be interpreted as different approximations of the same capacity-maximization principle.

## Proposed Method (CapKV)

The authors introduce CapKV, a capacity-aware eviction method that directly targets information preservation via a log-determinant approximation using statistical leverage scores, replacing heuristic selection with a theoretically grounded mechanism that preserves the maximum predictive signal.

Extensive experiments across multiple models and long-context benchmarks show that CapKV consistently outperforms prior methods, achieving a better trade-off between memory efficiency and generational fidelity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c534bd9d-448c-4af5-81fa-340a7e6a56e8",
  "isSidechain": true,
  "promptId": "df458d81-282b-4e80-9794-9720edf3d7b4",
  "agentId": "a0d64cbc73c0919e7",
  "type": "user",
  "uuid": "f8760768-6eab-4307-935e-333e30258870",
  "sourceToolAssistantUUID": "c534bd9d-448c-4af5-81fa-340a7e6a56e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-09T19:00:38.981Z_

I now have a comprehensive picture. Here is the full structured report:

---

## New Relevant Papers: KV Cache Compression for Reasoning Models (April–May 2026)

Papers are organized by relevance to RIC. Dates use the arXiv ID prefix as the primary dating signal (25XX = 2025, 26XX = 2026).

---

### TIER 1 — Directly Competitive / Must Address in Related Work

---

**1. R-KV: Redundancy-aware KV Cache Compression for Reasoning Models**
- **arXiv:** 2505.24133 (May 2025, v2 posted later)
- **Training-free:** Yes
- **Boundary-triggered:** No — continuous/online eviction during decoding
- **Method:** Three-component joint eviction: (a) attention-based importance scoring, (b) dynamic redundancy scoring via key-vector cosine similarity to detect repeated tokens, (c) joint eviction balancing both scores.
- **Compression rate:** 10–34% KV retention; lossless at 25% budget on AIME-2024
- **Benchmarks:** AIME-24 (105% of full-KV accuracy at 16% cache with DeepSeek-R1-Distill-Llama-8B); MATH-500 (lossless at 54% for R1-Qwen-14B)
- **FLAG — HIGH COMPETITION:** Training-free, reasoning-specific, tested on the same models and benchmarks as RIC. The key differentiator for RIC is that R-KV is continuous/streaming (no boundary event) whereas RIC does a single one-shot compression at the `&lt;/think>` token. Also R-KV does not exploit the structural transition from "think" phase to "answer" phase. Must be cited and directly compared.

---

**2. Reasoning Path Compression (RPC)**
- **arXiv:** 2505.13866 (May 20, 2025)
- **Training-free:** Yes
- **Boundary-triggered:** No — periodic compression at fixed intervals during generation
- **Method:** Periodically compresses KV cache using a sliding "selector window" of recent queries to score importance; retains high-scoring entries. Exploits semantic sparsity of reasoning paths.
- **Compression rate / throughput:** 1.60× throughput improvement on QwQ-32B
- **Benchmarks:** AIME 2024 (1.2% accuracy drop at 1.60× speedup)
- **FLAG — MODERATE COMPETITION:** Training-free, reasoning-specific, periodic triggers. RIC's `&lt;/think>`-boundary trigger is architecturally cleaner and one-shot rather than periodic. RIC should cite this and contrast the one-shot vs. periodic approaches and that RIC's trigger is semantically motivated (phase transition), not interval-based.

---

**3. TriAttention: Efficient Long Reasoning with Trigonometric KV Compression**
- **arXiv:** 2604.04921 (April 4, 2026)
- **Training-free:** Yes (no fine-tuning; uses intrinsic Q/K structure)
- **Boundary-triggered:** No — layer-wise continuous compression
- **Method:** Observes that Q and K vectors cluster around fixed non-zero centers in **pre-RoPE space** and remain stable across positions. Uses these centers (via a trigonometric series decomposition) to estimate key importance without per-query attention computation, avoiding the positional rotation instability of post-RoPE query proxies.
- **Compression rate:** 10.7× KV memory reduction; 2.5× throughput
- **Benchmarks:** AIME 2025 with 32K-token generation — matches Full Attention accuracy; baselines achieve only ~50% accuracy at same efficiency
- **FLAG — HIGH RELEVANCE FOR PRE-ROPE SCORING ANGLE:** This is the most important paper for RIC's pre-RoPE KV scoring design. TriAttention provides strong evidence and theoretical grounding that pre-RoPE space is the right place to score KV importance for reasoning models. If RIC uses pre-RoPE representations for importance scoring, TriAttention should be cited as motivation and distinguished from (TriAttention is continuous; RIC is one-shot at boundary). If RIC uses post-RoPE scoring, TriAttention's argument is a potential critique to address.

---

**4. Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning**
- **arXiv:** 2505.16950 (May 2025, updated March 25, 2026)
- **Training-free:** No — requires training an auxiliary Cache Processor (a separate Transformer)
- **Boundary-triggered:** Yes — triggered at **newline tokens** (end of each reasoning step)
- **Method:** Augments LLM with an auxiliary Transformer ("Cache Processor") that performs non-causal, in-place KV rewrites at newline-delimited step boundaries. Consolidates recent KV entries and reconsolidates a top-k attention-selected set of prior entries. Justified via Information Bottleneck theory.
- **Compression rate:** Not specified numerically; gains up to +6.6pp on selected tasks
- **Benchmarks:** General reasoning gains vs. vanilla Transformer and pause-token baselines
- **FLAG — NOTABLE DISTINCTION:** Boundary-triggered like RIC, but requires training an auxiliary model and triggers on every newline (sub-step), not at the single `&lt;/think>` boundary. RIC's advantage: zero training cost, single trigger at the semantically meaningful phase-transition token. Must cite; key contrast is training-free one-shot vs. trained periodic.

---

**5. Lookahead Q-Cache (LAQ)**
- **arXiv:** 2505.20334 (May 2025)
- **Training-free:** Yes (pseudo-query generation is training-free)
- **Boundary-triggered:** No — operates during prefill stage
- **Method:** Generates low-cost pseudo lookahead queries to approximate decoding-stage queries; uses these for more consistent KV importance estimation during prefill, addressing the mismatch between prefill-stage scores and actual generation queries.
- **Compression rate / results:** Improved accuracy vs. standard prefill-scored eviction under tight memory budgets
- **FLAG — RELEVANT FOR CONCLUSION-TOKEN QUERY PROXY:** This paper directly addresses the same problem RIC's conclusion-token query proxy targets — that prefill-stage queries don't represent what decoding will attend to. LAQ uses synthetic pseudo-queries; if RIC uses the `&lt;/think>` token's query vector as a proxy for the answer-phase queries, this paper is the closest methodological precedent. Cite and distinguish: LAQ generates artificial queries; RIC uses a real model-generated query at the semantically natural transition point.

---

### TIER 2 — Related Work / Background / Cite Without Detailed Comparison

---

**6. ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution**
- **arXiv:** 2602.03203 (February 3, 2026)
- **Training-free:** No — requires two-stage training (supervised + RL/GRPO)
- **Boundary-triggered:** No — continuous online eviction
- **Method:** Distills future attention scores into a learned eviction policy using a "Golden Eviction" algorithm; trains with Pairwise Ranking Loss + GRPO.
- **Benchmarks:** AIME 2024 and AIME 2025 — outperforms prior methods at 50% cache budget
- **Note:** Strong trained baseline on same benchmarks. RIC's advantage is training-free.

---

**7. Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle**
- **arXiv:** 2601.16986 (January 2026)
- **Training-free:** Partially (inference-time adaptive budget; may use calibration)
- **Boundary-triggered:** Partially — distinguishes "think-KV" from answer-KV, prioritizing tokens essential to the final answer
- **Method:** Separates SlipKV (reasoning flow tokens) from CrystalKV (answer-critical tokens); evicts SlipKV when utility expires. Adaptive per-layer/head budget allocation based on dynamic importance proportion.
- **Note:** Conceptually close to RIC's insight that think-phase KV can be selectively discarded at the answer boundary. Differentiator: Crystal-KV is an online streaming method; RIC is a single one-shot compression event.

---

**8. Where Matters More Than What: Decoding-aligned KV Cache Compression via Position-aware Pseudo Queries (DapQ)**
- **arXiv:** 2603.11564 (March 12, 2026)
- **Training-free:** Yes
- **Boundary-triggered:** No
- **Method:** Finds that positional information is more important than semantic content when constructing pseudo queries to approximate decoding-stage queries. Constructs position-aware pseudo queries during prefill for better KV selection.
- **Note:** Relevant to the "conclusion-token query proxy" question — confirms positional alignment matters more than semantic content in query proxies. If RIC's proxy is the `&lt;/think>` query, its position at the boundary may be as important as its semantics.

---

**9. Near-Oracle KV Selection via Pre-hoc Sparsity (PrHS)**
- **arXiv:** 2602.08329 (February 2026)
- **Training-free:** Yes
- **Boundary-triggered:** No
- **Method:** Selects KV entries before attention scoring using mutual-information analysis to avoid posterior bias; derives upper bound on MI loss from dropped mass. Three orthogonal selectors along time, depth, and layer axes.
- **Benchmarks:** GSM8K, CoQA, LongBench; 9.9× speedup in attention latency
- **Note:** Provides theoretical backing for avoiding posterior/attention-score-based importance estimates — relevant if RIC motivates pre-RoPE or query-proxy scoring as a way to escape posterior bias.

---

**10. How Much Cache Does Reasoning Need? Depth–Cache Tradeoffs in KV-Compressed Transformers**
- **arXiv:** 2604.17935 (April 20, 2026)
- **Training-free:** N/A — theoretical
- **Boundary-triggered:** N/A
- **Method:** Proves depth lower/upper bounds for multi-hop pointer chasing under a compressed KV cache. Shows that L = O(⌈k/s⌉ log s · log n/mp) depth suffices, with matching lower bound conjectured.
- **Note:** Theoretical grounding for the claim that reasoning models need more cache than retrieval-only tasks. Useful background citation for motivating why naive compression fails on AIME-class tasks.

---

**11. LookaheadKV: Glimpsing into the Future without Generation**
- **arXiv:** 2603.10899 (March 11, 2026)
- **Training-free:** No — requires training lookahead tokens and LoRA modules
- **Boundary-triggered:** No
- **Method:** Trainable soft lookahead tokens predict true importance scores via KL divergence loss; reduces eviction cost by up to 14.5× and improves TTFT.
- **Note:** Trained counterpart to LAQ and RIC's proxy idea. Confirms the general approach of using future-query proxies is fruitful.

---

**12. KeyDiff: Key Similarity-Based KV Cache Eviction**
- **arXiv:** 2504.15364 (April 2025)
- **Training-free:** Yes
- **Boundary-triggered:** No
- **Method:** Evicts keys with highest cosine similarity to an anchor (cache representative); motivated by geometric distinctiveness correlating with attention importance. Compatible with FlashAttention (no attention scores needed).
- **Benchmarks:** Near-baseline on Math500 and LongBench at 23% KV reduction; 30% latency reduction
- **Note:** Pre-attention scoring using key geometry rather than attention — relevant background for pre-RoPE scoring discussion.

---

### SPECIFIC ANSWERS TO YOUR QUESTIONS

**Pre-RoPE KV scoring:** TriAttention (2604.04921) is the primary paper directly addressing this. It proves Q/K concentration is stable in pre-RoPE space and uses this as the theoretical basis for a compression method that works on reasoning tasks. KeyDiff (2504.15364) also avoids attention scores by using key-space geometry. PrHS (2602.08329) argues for pre-hoc (pre-attention) selection to avoid posterior bias. These three form a coherent related-work cluster for RIC's pre-RoPE scoring.

**Conclusion-token query proxies:** Lookahead Q-Cache (2505.20334) and DapQ (2603.11564) are the closest precedents. LAQ generates artificial pseudo-queries to proxy decoding-stage attention; DapQ finds positional alignment is more important than semantic content in such proxies. Neither uses an actual model-generated token at a semantic boundary (the `&lt;/think>` token) as the proxy — RIC's approach is meaningfully distinct. The "Utilizing KV Cache for Sampling and Reasoning" paper (2601.20326) is also adjacent, using pooled KV features for one-shot control token switching.

**No paper found doing one-shot, training-free, `&lt;/think>`-boundary-triggered compression.** The boundary-triggered approaches (Bottlenecked Transformers) require training; the training-free approaches (R-KV, RPC, Crystal-KV) are either continuous or periodic but not single-event at the phase-transition boundary. RIC occupies a distinct position in this design space.

---

### SUMMARY TABLE

| Paper | arXiv ID | Date | Training-free | Boundary-triggered | Direct Competitor |
|---|---|---|---|---|---|
| R-KV | 2505.24133 | May 2025 | Yes | No | HIGH |
| TriAttention | 2604.04921 | Apr 2026 | Yes | No | HIGH (pre-RoPE) |
| RPC | 2505.13866 | May 2025 | Yes | No (periodic) | MODERATE |
| Bottlenecked Transformers | 2505.16950 | May 2025 | No | Yes (newline) | MODERATE |
| Lookahead Q-Cache | 2505.20334 | May 2025 | Yes | No | NOTABLE (proxy) |
| ForesightKV | 2602.03203 | Feb 2026 | No | No | LOW |
| Crystal-KV | 2601.16986 | Jan 2026 | Partial | Partial | LOW-MODERATE |
| DapQ | 2603.11564 | Mar 2026 | Yes | No | NOTABLE (proxy) |
| PrHS | 2602.08329 | Feb 2026 | Yes | No | LOW (theory) |
| Depth-Cache Tradeoffs | 2604.17935 | Apr 2026 | N/A | N/A | BACKGROUND |
| LookaheadKV | 2603.10899 | Mar 2026 | No | No | LOW |
| KeyDiff | 2504.15364 | Apr 2025 | Yes | No | LOW |
| ReCalKV | 2505.24357 | May 2025 | No (calibration) | No | LOW |

Sources:
- [R-KV: Redundancy-aware KV Cache Compression for Reasoning Models](https://arxiv.org/abs/2505.24133)
- [TriAttention: Efficient Long Reasoning with Trigonometric KV Compression](https://arxiv.org/abs/2604.04921v1)
- [Reasoning Path Compression](https://arxiv.org/abs/2505.13866)
- [Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning](https://arxiv.org/abs/2505.16950)
- [Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query](https://arxiv.org/abs/2505.20334)
- [ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution](https://arxiv.org/abs/2602.03203)
- [Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle](https://arxiv.org/abs/2601.16986)
- [Where Matters More Than What: Decoding-aligned KV Cache Compression via Position-aware Pseudo Queries](https://arxiv.org/abs/2603.11564)
- [Near-Oracle KV Selection via Pre-hoc Sparsity for Long-Context Inference](https://arxiv.org/abs/2602.08329)
- [How Much Cache Does Reasoning Need? Depth-Cache Tradeoffs in KV-Compressed Transformers](https://arxiv.org/abs/2604.17935v1)
- [LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation](https://arxiv.org/abs/2603.10899)
- [KeyDiff: Key Similarity-Based KV Cache Eviction](https://arxiv.org/abs/2504.15364)
- [ReCalKV: Low-Rank KV Cache Compression via Head Reordering and Offline Calibration](https://arxiv.org/abs/2505.24357)
- [Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective](https://arxiv.org/abs/2604.25975)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8760768-6eab-4307-935e-333e30258870",
  "isSidechain": true,
  "agentId": "a0d64cbc73c0919e7",
  "requestId": "req_011CasWThEG2bKcHVQouzFqe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82743097-ac3a-472b-94be-f54c5112110e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a245f53e-dd72-43de-9359-1089831cfdcf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TAhRVPJz6BCb3zRpidm7tA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2938,
      "cache_read_input_tokens": 33036,
      "output_tokens": 4328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2938
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4328,
          "cache_read_input_tokens": 33036,
          "cache_creation_input_tokens": 2938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2938,
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
