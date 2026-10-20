# research recency control literature

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_research_recency_control_literature_20260516T231504.log`
- **Structured JSON:** [`3f20d0e514c499ca4bc3.json`](../../sessions/3f/3f20d0e514c499ca4bc3.json)

## Before a recorded user message

26 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "7a44d4e5-0ea0-4077-84cd-970606f8bb16",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778988000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7b3c1f35-71f8-452a-b82e-cebd80c42afb",
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to do a literature survey on recency-based eviction as a control condition in KV cache compression research. Let me search for relevant papers using WebFetch and WebSearch tools.

Let me first load the WebSearch tool schema.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "8ddeaf6a-f123-43d4-a987-78063a83cdad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dYsjETQvQbCbncdWy8BKH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12528,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12528
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ks3uXkiJ3vJGBHcHxSJSvv`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "37aa6f0b-c510-4e0e-aaaa-b6fc4ea79207",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dYsjETQvQbCbncdWy8BKH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12528,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12528
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T23:15:17.831Z_

<details><summary>↩ Tool result · `toolu_01Ks3uXkiJ3vJGBHcHxSJSvv`</summary>

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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "f5be251c-7d58-400c-87d0-e84d1f8050c8",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for relevant papers on recency-based eviction as a control condition in KV cache compression research. I'll run multiple searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "01605ec8-8c4e-4a48-9bb0-36875e7af29f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsdkuRiXRi9cwvNyHUzsLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 24369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 672
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MvN4LJzEQ6nWVP2kdGhFgy`</summary>

```json
{
  "query": "\"recency eviction\" OR \"FIFO eviction\" OR \"oldest-first eviction\" KV cache LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "ea84fa8b-193b-46cc-aa30-f67ebc38c90e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsdkuRiXRi9cwvNyHUzsLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 24369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 672
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WzNzT1uGa7KiQ9YBtPctBQ`</summary>

```json
{
  "query": "\"position-based eviction\" OR \"scoring-independent\" KV cache baseline control experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "86980119-057f-45b8-8c78-7cf3e77ea0c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsdkuRiXRi9cwvNyHUzsLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 24369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 672
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013PZVJHLatreNGavW6PVoBG`</summary>

```json
{
  "query": "attention-score-based vs position-based eviction KV cache reasoning comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "2e6096a9-47fa-4e9f-817e-10281cbbe2b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsdkuRiXRi9cwvNyHUzsLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 24369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 672
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T23:15:28.816Z_

<details><summary>↩ Tool result · `toolu_01WzNzT1uGa7KiQ9YBtPctBQ`</summary>

```text
Web search results for query: ""position-based eviction" OR "scoring-independent" KV cache baseline control experiment"

Links: [{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"[2603.10899] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203"},{"title":"Published as preprint paper G-KV: DECODING-TIME KV CACHE EVICTION WITH","url":"https://arxiv.org/pdf/2512.00504"},{"title":"[2510.13334] Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/abs/2510.13334"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"Paper page - LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://huggingface.co/papers/2603.10899"},{"title":"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/html/2604.25975v1"},{"title":"[2504.15364] KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/abs/2504.15364"}]

Based on the search results, I found relevant information about KV cache eviction methods. Here's what I discovered:

## Position-Based and Scoring-Independent Approaches

The search results discuss various KV cache eviction strategies, though I didn't find a paper specifically titled with both "position-based eviction" and "scoring-independent" together. However, I found related work:

One study identifies three KV cache patterns in reasoning models, including "Position-dependent" patterns, which relates to position-based considerations in KV cache management.

Regarding scoring-independent approaches, KeyDiff is a training-free KV cache eviction method based solely on key similarity that notably does not rely on attention scores, making it a notable scoring-independent baseline.

## Alternative Baseline Control Methods

The search results show several baseline approaches used in control experiments:

1. **Position-aware methods**: H2O dynamically retains a balance of recent tokens and important tokens, with selection driven by cumulative attention scores.

2. **No-correction baselines**: Some studies evaluate a no-correction baseline to demonstrate the effectiveness of proposed improvements.

3. **Scoring-aggregation frameworks**: Recent methods employ a scoring-aggregation framework to evict unimportant cache entries, based on the stability assumption that a fixed subset of entries remains consistently important during generation.

If you're looking for a specific paper on position-based eviction or scoring-independent methods, you might want to search with more specific author names or publication venues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "1f769f45-26f1-4b4e-86e2-6923d7a45dc7",
  "tool_use_result": {
    "query": "\"position-based eviction\" OR \"scoring-independent\" KV cache baseline control experiment",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JnywFGqHtPUkqGefVVi8Yb",
        "content": [
          {
            "title": "Taming the Fragility of KV Cache Eviction in LLM Inference",
            "url": "https://arxiv.org/html/2510.13334v1"
          },
          {
            "title": "[2603.10899] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation",
            "url": "https://arxiv.org/abs/2603.10899"
          },
          {
            "title": "ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution",
            "url": "https://arxiv.org/html/2602.03203"
          },
          {
            "title": "Published as preprint paper G-KV: DECODING-TIME KV CACHE EVICTION WITH",
            "url": "https://arxiv.org/pdf/2512.00504"
          },
          {
            "title": "[2510.13334] Taming the Fragility of KV Cache Eviction in LLM Inference",
            "url": "https://arxiv.org/abs/2510.13334"
          },
          {
            "title": "Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost",
            "url": "https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"
          },
          {
            "title": "Reformulating KV Cache Eviction Problem for Long-Context LLM Inference",
            "url": "https://arxiv.org/html/2605.07234"
          },
          {
            "title": "Paper page - LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation",
            "url": "https://huggingface.co/papers/2603.10899"
          },
          {
            "title": "Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective",
            "url": "https://arxiv.org/html/2604.25975v1"
          },
          {
            "title": "[2504.15364] KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments",
            "url": "https://arxiv.org/abs/2504.15364"
          }
        ]
      },
      "Based on the search results, I found relevant information about KV cache eviction methods. Here's what I discovered:\n\n## Position-Based and Scoring-Independent Approaches\n\nThe search results discuss various KV cache eviction strategies, though I didn't find a paper specifically titled with both \"position-based eviction\" and \"scoring-independent\" together. However, I found related work:\n\nOne study identifies three KV cache patterns in reasoning models, including \"Position-dependent\" patterns, which relates to position-based considerations in KV cache management.\n\nRegarding scoring-independent approaches, KeyDiff is a training-free KV cache eviction method based solely on key similarity that notably does not rely on attention scores, making it a notable scoring-independent baseline.\n\n## Alternative Baseline Control Methods\n\nThe search results show several baseline approaches used in control experiments:\n\n1. **Position-aware methods**: H2O dynamically retains a balance of recent tokens and important tokens, with selection driven by cumulative attention scores.\n\n2. **No-correction baselines**: Some studies evaluate a no-correction baseline to demonstrate the effectiveness of proposed improvements.\n\n3. **Scoring-aggregation frameworks**: Recent methods employ a scoring-aggregation framework to evict unimportant cache entries, based on the stability assumption that a fixed subset of entries remains consistently important during generation.\n\nIf you're looking for a specific paper on position-based eviction or scoring-independent methods, you might want to search with more specific author names or publication venues."
    ],
    "durationSeconds": 6.221903254999997
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T23:15:31.647Z_

<details><summary>↩ Tool result · `toolu_013PZVJHLatreNGavW6PVoBG`</summary>

```text
Web search results for query: "attention-score-based vs position-based eviction KV cache reasoning comparison"

Links: [{"title":"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning","url":"https://arxiv.org/html/2506.15969"},{"title":"LazyEviction: Lagged KV Eviction with Attention Pattern Observation for","url":"https://www.arxiv.org/pdf/2506.15969v3"},{"title":"Decoding-Time KV Cache Eviction with Global Attention","url":"https://arxiv.org/pdf/2512.00504"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203v1"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based","url":"https://arxiv.org/pdf/2504.14051"},{"title":"hashevict:apre-attention kv cache eviction strategy using locality- ...","url":"https://www.researchgate.net/publication/387349709_HashEvict_A_Pre-Attention_KV_Cache_Eviction_Strategy_using_Locality-Sensitive_Hashing/fulltext/676a25b7e74ca64e1f26c82c/HashEvict-A-Pre-Attention-KV-Cache-Eviction-Strategy-using-Locality-Sensitive-Hashing.pdf"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"hashevict:apre-attention kv cache eviction strategy using ...","url":"https://arxiv.org/pdf/2412.16187"},{"title":"KV Cache Eviction in Transformer LLMs","url":"https://www.emergentmind.com/topics/kv-cache-eviction"}]

Based on the search results, here's a comprehensive comparison of attention-score-based vs position-based eviction strategies for KV cache in reasoning tasks:

## Attention-Score-Based Eviction

Attention-based methods include current attention-based eviction which executes stepwise evictions using immediate attention scores, and cumulative attention-based eviction which integrates historical attention for eviction decisions.

For reasoning models, attention-based eviction methods such as H2O and SnapKV-D perform exceptionally well across a variety of reasoning tasks and even sometimes surpass full-cache performance. For reasoning models, accumulated attention scores are a high-quality token importance metric, therefore, lead with heavy-hitter methods for compression.

However, attention-based methods have limitations: Purely attention-score based eviction suffers from monotonic position bias, resulting in systematic retention of early (prefix) tokens even when their contextual utility wanes.

## Position-Based Approaches

Many popular eviction strategies, such as StreamingLLM, KNorm, and PyramidKV are based on empirical observations as opposed to attention-tracking.

## Key Challenge: Token Importance Recurrence

A large proportion of tokens regain high attention after multiple decoding steps, which is failed to capture by existing works and may lead to unpredictable eviction on such periodically critical tokens. The recurring tokens often contain information vital for later reasoning stages, and premature eviction of recurring tokens leads to catastrophic performance degradation.

## Emerging Solutions

LazyEviction performs lagged KV evictions based on the observation window to detect latent recurring tokens and prevent prematurely discarding them. This addresses the limitations of both pure attention-score and position-based approaches by observing attention patterns over time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "641f3ead-2188-46bd-9ea5-1ddad6ba1018",
  "tool_use_result": {
    "query": "attention-score-based vs position-based eviction KV cache reasoning comparison",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AdWGuMZGDX8cr4rCUpkqTc",
        "content": [
          {
            "title": "LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning",
            "url": "https://arxiv.org/html/2506.15969"
          },
          {
            "title": "LazyEviction: Lagged KV Eviction with Attention Pattern Observation for",
            "url": "https://www.arxiv.org/pdf/2506.15969v3"
          },
          {
            "title": "Decoding-Time KV Cache Eviction with Global Attention",
            "url": "https://arxiv.org/pdf/2512.00504"
          },
          {
            "title": "ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution",
            "url": "https://arxiv.org/html/2602.03203v1"
          },
          {
            "title": "Expected Attention: KV Cache Compression by Estimating Attention",
            "url": "https://arxiv.org/pdf/2510.00636"
          },
          {
            "title": "CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based",
            "url": "https://arxiv.org/pdf/2504.14051"
          },
          {
            "title": "hashevict:apre-attention kv cache eviction strategy using locality- ...",
            "url": "https://www.researchgate.net/publication/387349709_HashEvict_A_Pre-Attention_KV_Cache_Eviction_Strategy_using_Locality-Sensitive_Hashing/fulltext/676a25b7e74ca64e1f26c82c/HashEvict-A-Pre-Attention-KV-Cache-Eviction-Strategy-using-Locality-Sensitive-Hashing.pdf"
          },
          {
            "title": "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning",
            "url": "https://arxiv.org/html/2512.12008v1"
          },
          {
            "title": "hashevict:apre-attention kv cache eviction strategy using ...",
            "url": "https://arxiv.org/pdf/2412.16187"
          },
          {
            "title": "KV Cache Eviction in Transformer LLMs",
            "url": "https://www.emergentmind.com/topics/kv-cache-eviction"
          }
        ]
      },
      "Based on the search results, here's a comprehensive comparison of attention-score-based vs position-based eviction strategies for KV cache in reasoning tasks:\n\n## Attention-Score-Based Eviction\n\nAttention-based methods include current attention-based eviction which executes stepwise evictions using immediate attention scores, and cumulative attention-based eviction which integrates historical attention for eviction decisions.\n\nFor reasoning models, attention-based eviction methods such as H2O and SnapKV-D perform exceptionally well across a variety of reasoning tasks and even sometimes surpass full-cache performance. For reasoning models, accumulated attention scores are a high-quality token importance metric, therefore, lead with heavy-hitter methods for compression.\n\nHowever, attention-based methods have limitations: Purely attention-score based eviction suffers from monotonic position bias, resulting in systematic retention of early (prefix) tokens even when their contextual utility wanes.\n\n## Position-Based Approaches\n\nMany popular eviction strategies, such as StreamingLLM, KNorm, and PyramidKV are based on empirical observations as opposed to attention-tracking.\n\n## Key Challenge: Token Importance Recurrence\n\nA large proportion of tokens regain high attention after multiple decoding steps, which is failed to capture by existing works and may lead to unpredictable eviction on such periodically critical tokens. The recurring tokens often contain information vital for later reasoning stages, and premature eviction of recurring tokens leads to catastrophic performance degradation.\n\n## Emerging Solutions\n\nLazyEviction performs lagged KV evictions based on the observation window to detect latent recurring tokens and prevent prematurely discarding them. This addresses the limitations of both pure attention-score and position-based approaches by observing attention patterns over time."
    ],
    "durationSeconds": 8.822833414
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T23:15:33.312Z_

<details><summary>↩ Tool result · `toolu_01MvN4LJzEQ6nWVP2kdGhFgy`</summary>

```text
Web search results for query: ""recency eviction" OR "FIFO eviction" OR "oldest-first eviction" KV cache LLM"

Links: [{"title":"7 Cache Eviction Strategies. Caching is a technique to make… | by Premchandu | Medium","url":"https://medium.com/@premchandu.in/7-cache-eviction-strategies-you-should-know-0bc4f08fd414"},{"title":"Cache Eviction Policies | System Design - GeeksforGeeks","url":"https://www.geeksforgeeks.org/system-design/cache-eviction-policies-system-design/"},{"title":"7 Cache Eviction Strategies You Should Know","url":"https://blog.algomaster.io/p/7-cache-eviction-strategies"},{"title":"Cache Eviction Policies | System Design - DEV Community","url":"https://dev.to/zeeshanali0704/cache-eviction-policies-system-design-1igm"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"KV Cache Eviction Policies for Long-Running LLM Sessions | by Zaina Haider | Jan, 2026 | GoPenAI","url":"https://blog.gopenai.com/kv-cache-eviction-policies-for-long-running-llm-sessions-fe7c828dfc26?gi=ad700e6e9431"},{"title":"What Is Cache Eviction? Strategies & How It Works","url":"https://www.ioriver.io/terms/cache-eviction-policy"},{"title":"LFU vs. LRU: How to choose the right cache eviction policy | Redis","url":"https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/"},{"title":"Cache Eviction Policies. Cache eviction policies determine which… | by Kandaanusha | Medium","url":"https://medium.com/@kandaanusha/cache-eviction-policies-70b9f3cfd90b"},{"title":"Cache Replacement Policies Explained for System Performance | Aerospike","url":"https://aerospike.com/blog/cache-replacement-policies/"}]

Based on the web search results, here's information about recency, FIFO, and oldest-first eviction policies in the context of KV cache for LLMs:

## General Cache Eviction Concepts

FIFO (First-In-First-Out) is a cache eviction policy that removes the oldest item from the cache when it becomes full, where the item that has been present in the cache for the longest time is the first to be evicted when the cache reaches its capacity.

When the cache is full, the item at the front of the queue (the oldest item) is evicted to make space for the new item, where the oldest item, which has been in the cache the longest, is removed to make room for the new item.

FIFO is straightforward and requires minimal logic with low overhead, as there's no need to track additional metadata like access frequency or recency.

## KV Cache Eviction in LLMs

In the context of LLM inference specifically, KV cache eviction is crucial for efficient long-sequence inference in LLMs, with early methods like StreamingLLM retaining only recent cache entries, often losing valuable information.

FIFO assumes recency equals importance, which is often false. More recent LLM-specific approaches have moved beyond simple recency or FIFO-based strategies. Subsequent methods like H2O and Scissorhands introduced importance-based eviction, assuming that a small set of entries remains consistently important.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "47fbde4d-daf1-4eb8-9edd-ee16ce361b0d",
  "tool_use_result": {
    "query": "\"recency eviction\" OR \"FIFO eviction\" OR \"oldest-first eviction\" KV cache LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Qav64AGYjiL6r34f1vhduw",
        "content": [
          {
            "title": "7 Cache Eviction Strategies. Caching is a technique to make… | by Premchandu | Medium",
            "url": "https://medium.com/@premchandu.in/7-cache-eviction-strategies-you-should-know-0bc4f08fd414"
          },
          {
            "title": "Cache Eviction Policies | System Design - GeeksforGeeks",
            "url": "https://www.geeksforgeeks.org/system-design/cache-eviction-policies-system-design/"
          },
          {
            "title": "7 Cache Eviction Strategies You Should Know",
            "url": "https://blog.algomaster.io/p/7-cache-eviction-strategies"
          },
          {
            "title": "Cache Eviction Policies | System Design - DEV Community",
            "url": "https://dev.to/zeeshanali0704/cache-eviction-policies-system-design-1igm"
          },
          {
            "title": "Taming the Fragility of KV Cache Eviction in LLM Inference",
            "url": "https://arxiv.org/html/2510.13334v1"
          },
          {
            "title": "KV Cache Eviction Policies for Long-Running LLM Sessions | by Zaina Haider | Jan, 2026 | GoPenAI",
            "url": "https://blog.gopenai.com/kv-cache-eviction-policies-for-long-running-llm-sessions-fe7c828dfc26?gi=ad700e6e9431"
          },
          {
            "title": "What Is Cache Eviction? Strategies & How It Works",
            "url": "https://www.ioriver.io/terms/cache-eviction-policy"
          },
          {
            "title": "LFU vs. LRU: How to choose the right cache eviction policy | Redis",
            "url": "https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/"
          },
          {
            "title": "Cache Eviction Policies. Cache eviction policies determine which… | by Kandaanusha | Medium",
            "url": "https://medium.com/@kandaanusha/cache-eviction-policies-70b9f3cfd90b"
          },
          {
            "title": "Cache Replacement Policies Explained for System Performance | Aerospike",
            "url": "https://aerospike.com/blog/cache-replacement-policies/"
          }
        ]
      },
      "Based on the web search results, here's information about recency, FIFO, and oldest-first eviction policies in the context of KV cache for LLMs:\n\n## General Cache Eviction Concepts\n\nFIFO (First-In-First-Out) is a cache eviction policy that removes the oldest item from the cache when it becomes full, where the item that has been present in the cache for the longest time is the first to be evicted when the cache reaches its capacity.\n\nWhen the cache is full, the item at the front of the queue (the oldest item) is evicted to make space for the new item, where the oldest item, which has been in the cache the longest, is removed to make room for the new item.\n\nFIFO is straightforward and requires minimal logic with low overhead, as there's no need to track additional metadata like access frequency or recency.\n\n## KV Cache Eviction in LLMs\n\nIn the context of LLM inference specifically, KV cache eviction is crucial for efficient long-sequence inference in LLMs, with early methods like StreamingLLM retaining only recent cache entries, often losing valuable information.\n\nFIFO assumes recency equals importance, which is often false. More recent LLM-specific approaches have moved beyond simple recency or FIFO-based strategies. Subsequent methods like H2O and Scissorhands introduced importance-based eviction, assuming that a small set of entries remains consistently important."
    ],
    "durationSeconds": 11.054199320999999
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AMKQ8tCW38Ewx7Hquw4nV7`</summary>

```json
{
  "query": "StreamingLLM \"attention sink\" \"recent tokens\" window eviction baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "ece6ff59-8eaa-4d50-b85e-d673457294ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sp6JV5xa1q3PE5FotqrhG2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1916,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 25041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1176
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BUcUMMS33qcAs9yRoighEw`</summary>

```json
{
  "query": "\"Hold Onto That Thought\" KV cache compression reasoning tasks eviction comparison 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "c4237cd0-a4ba-4d1f-8d09-1935ce83f8cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sp6JV5xa1q3PE5FotqrhG2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1916,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 25041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1176
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016qMDYQL6GcSYoiHoA9mwAi`</summary>

```json
{
  "query": "H2O heavy hitter oracle \"local\" OR \"window\" OR \"recent\" eviction baseline comparison arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "3972703a-c557-410b-8f06-8de34f1ff1ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sp6JV5xa1q3PE5FotqrhG2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1916,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 25041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1176
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T23:15:43.712Z_

<details><summary>↩ Tool result · `toolu_01AMKQ8tCW38Ewx7Hquw4nV7`</summary>

```text
Web search results for query: "StreamingLLM "attention sink" "recent tokens" window eviction baseline"

Links: [{"title":"GitHub - mit-han-lab/streaming-llm: [ICLR 2024] Efficient Streaming Language Models with Attention Sinks · GitHub","url":"https://github.com/mit-han-lab/streaming-llm"},{"title":"[2309.17453] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453"},{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://hanlab.mit.edu/projects/streamingllm"},{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/html/2309.17453v3"},{"title":"Efficient Streaming Language Models with Attention Sinks | OpenReview","url":"https://openreview.net/forum?id=NG7sS51zVF"},{"title":"Why Streaming LLMs Need Attention Sinks | Adam's Blog","url":"https://www.adambutterworth.com/posts/attention-sinks"},{"title":"Attention Sinks: Enabling Infinite-Length LLM Generation with StreamingLLM - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/attention-sinks-streamingllm-infinite-generation"},{"title":"How Attention Sinks Keep Language Models Stable","url":"https://hanlab.mit.edu/blog/streamingllm"},{"title":"StreamingLLM: Efficient Streaming for LLMs","url":"https://www.emergentmind.com/topics/streamingllm"},{"title":"Efficient Deployment Algorithms for Large Language Models by Guangxuan Xiao","url":"https://dspace.mit.edu/bitstream/handle/1721.1/156332/xiao-xgx-sm-eecs-2024-thesis.pdf"}]

Here's what I found about StreamingLLM, attention sinks, recent tokens, and window eviction baselines:

## Key Concepts

The attention sink phenomenon occurs when keeping the KV (Key-Value) of initial tokens recovers the performance of window attention, and emerges because initial tokens receive strong attention scores as a "sink" even if they are not semantically important.

## The Window Eviction Problem

Window attention collapses once the sequence length exceeds the cache size, particularly when the KV of the first token is evicted. Window attention fails when the input length exceeds the cache size, especially as initial tokens are evicted.

## StreamingLLM Solution

StreamingLLM retains only the most recent tokens and attention sinks, discarding middle tokens. Instead of discarding the first few tokens like any others, the approach permanently preserves their Key and Value states while maintaining a sliding window for everything else.

## Baseline Comparisons

StreamingLLM benchmarks against established baselines such as dense attention, window attention, and the sliding window approach with re-computation. In streaming settings, StreamingLLM outperforms the sliding window recomputation baseline by up to 22.2x speedup.

StreamingLLM enables Llama-2, MPT, Falcon, and Pythia to perform stable and efficient language modeling with up to 4 million tokens and more.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "aad7baf8-039f-4da2-a99a-67f085aaa423",
  "tool_use_result": {
    "query": "StreamingLLM \"attention sink\" \"recent tokens\" window eviction baseline",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QRqSuaAVmjdoqhHm6YB2pp",
        "content": [
          {
            "title": "GitHub - mit-han-lab/streaming-llm: [ICLR 2024] Efficient Streaming Language Models with Attention Sinks · GitHub",
            "url": "https://github.com/mit-han-lab/streaming-llm"
          },
          {
            "title": "[2309.17453] Efficient Streaming Language Models with Attention Sinks",
            "url": "https://arxiv.org/abs/2309.17453"
          },
          {
            "title": "Efficient Streaming Language Models with Attention Sinks",
            "url": "https://hanlab.mit.edu/projects/streamingllm"
          },
          {
            "title": "Efficient Streaming Language Models with Attention Sinks",
            "url": "https://arxiv.org/html/2309.17453v3"
          },
          {
            "title": "Efficient Streaming Language Models with Attention Sinks | OpenReview",
            "url": "https://openreview.net/forum?id=NG7sS51zVF"
          },
          {
            "title": "Why Streaming LLMs Need Attention Sinks | Adam's Blog",
            "url": "https://www.adambutterworth.com/posts/attention-sinks"
          },
          {
            "title": "Attention Sinks: Enabling Infinite-Length LLM Generation with StreamingLLM - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/attention-sinks-streamingllm-infinite-generation"
          },
          {
            "title": "How Attention Sinks Keep Language Models Stable",
            "url": "https://hanlab.mit.edu/blog/streamingllm"
          },
          {
            "title": "StreamingLLM: Efficient Streaming for LLMs",
            "url": "https://www.emergentmind.com/topics/streamingllm"
          },
          {
            "title": "Efficient Deployment Algorithms for Large Language Models by Guangxuan Xiao",
            "url": "https://dspace.mit.edu/bitstream/handle/1721.1/156332/xiao-xgx-sm-eecs-2024-thesis.pdf"
          }
        ]
      },
      "Here's what I found about StreamingLLM, attention sinks, recent tokens, and window eviction baselines:\n\n## Key Concepts\n\nThe attention sink phenomenon occurs when keeping the KV (Key-Value) of initial tokens recovers the performance of window attention, and emerges because initial tokens receive strong attention scores as a \"sink\" even if they are not semantically important.\n\n## The Window Eviction Problem\n\nWindow attention collapses once the sequence length exceeds the cache size, particularly when the KV of the first token is evicted. Window attention fails when the input length exceeds the cache size, especially as initial tokens are evicted.\n\n## StreamingLLM Solution\n\nStreamingLLM retains only the most recent tokens and attention sinks, discarding middle tokens. Instead of discarding the first few tokens like any others, the approach permanently preserves their Key and Value states while maintaining a sliding window for everything else.\n\n## Baseline Comparisons\n\nStreamingLLM benchmarks against established baselines such as dense attention, window attention, and the sliding window approach with re-computation. In streaming settings, StreamingLLM outperforms the sliding window recomputation baseline by up to 22.2x speedup.\n\nStreamingLLM enables Llama-2, MPT, Falcon, and Pythia to perform stable and efficient language modeling with up to 4 million tokens and more."
    ],
    "durationSeconds": 6.715320758999998
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T23:15:46.501Z_

<details><summary>↩ Tool result · `toolu_01BUcUMMS33qcAs9yRoighEw`</summary>

```text
Web search results for query: ""Hold Onto That Thought" KV cache compression reasoning tasks eviction comparison 2024"

Links: [{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"[2512.12008] Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/abs/2512.12008"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://openreview.net/pdf?id=OtZtLYAdQY"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning | OpenReview","url":"https://openreview.net/forum?id=udgrpHqw4F"},{"title":"NeurIPS Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://neurips.cc/virtual/2025/loc/san-diego/126664"},{"title":"Paper page - Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://huggingface.co/papers/2601.17668"},{"title":"R-KV: Redundancy-aware KV Cache Compression for ...","url":"https://arxiv.org/pdf/2505.24133"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression Adrian Ła´ncucki†","url":"https://openreview.net/pdf?id=8ZiElzQxf1"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203v1"}]

I found research on "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning". Here are the key findings:

## Overview

This paper addresses how Large Language Models (LLMs) are bottlenecked by memory constraints, as the KV cache grows linearly with context length. A suite of compression algorithms has been introduced to alleviate cache growth by evicting unimportant tokens.

## Key Focus

The paper focuses on reasoning tasks requiring long decoding, addressing that several popular strategies are targeted towards the prefill phase (processing long prompt context), and that short but complex prompts in benchmarks like GSM8K and MATH500 often benefit from multi-step reasoning and self-reflection, resulting in thinking sequences thousands of tokens long.

## Compression Strategies Evaluated

The comprehensive evaluation includes major KV cache compression strategies: StreamingLLM, H2O, a decoding-enabled SnapKV, R-KV, and KNorm, across a suite of eight benchmarks spanning mathematical, logical, and commonsense reasoning.

## Main Findings

Classical attention-based "heavy-hitter" strategies, which evict tokens based on accumulated attention scores, significantly outperform other methods, even defeating full-cache reasoning occasionally. This includes H2O and a novel simple extension of SnapKV (prompt-only compression method) to a decoding-enabled variant, SnapKV-Decoding.

H2O and the decoding-enabled variant of SnapKV are dominant strategies for reasoning models, indicating the utility of heavy-hitter tracking for reasoning traces.

## Important Tradeoff

Eviction strategies at low budgets can produce longer reasoning traces, revealing a tradeoff between cache size and inference costs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "6453918a-78a3-4f68-837d-f4c80cfcae9d",
  "tool_use_result": {
    "query": "\"Hold Onto That Thought\" KV cache compression reasoning tasks eviction comparison 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L7LXjuzvdDqGctCQp9frmd",
        "content": [
          {
            "title": "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning",
            "url": "https://arxiv.org/html/2512.12008v1"
          },
          {
            "title": "[2512.12008] Hold Onto That Thought: Assessing KV Cache Compression On Reasoning",
            "url": "https://arxiv.org/abs/2512.12008"
          },
          {
            "title": "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning",
            "url": "https://openreview.net/pdf?id=OtZtLYAdQY"
          },
          {
            "title": "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=udgrpHqw4F"
          },
          {
            "title": "NeurIPS Hold Onto That Thought: Assessing KV Cache Compression On Reasoning",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/126664"
          },
          {
            "title": "Paper page - Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction",
            "url": "https://huggingface.co/papers/2601.17668"
          },
          {
            "title": "R-KV: Redundancy-aware KV Cache Compression for ...",
            "url": "https://arxiv.org/pdf/2505.24133"
          },
          {
            "title": "ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models",
            "url": "https://arxiv.org/html/2510.01290v1"
          },
          {
            "title": "Inference-Time Hyper-Scaling with KV Cache Compression Adrian Ła´ncucki†",
            "url": "https://openreview.net/pdf?id=8ZiElzQxf1"
          },
          {
            "title": "ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution",
            "url": "https://arxiv.org/html/2602.03203v1"
          }
        ]
      },
      "I found research on \"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning\". Here are the key findings:\n\n## Overview\n\nThis paper addresses how Large Language Models (LLMs) are bottlenecked by memory constraints, as the KV cache grows linearly with context length. A suite of compression algorithms has been introduced to alleviate cache growth by evicting unimportant tokens.\n\n## Key Focus\n\nThe paper focuses on reasoning tasks requiring long decoding, addressing that several popular strategies are targeted towards the prefill phase (processing long prompt context), and that short but complex prompts in benchmarks like GSM8K and MATH500 often benefit from multi-step reasoning and self-reflection, resulting in thinking sequences thousands of tokens long.\n\n## Compression Strategies Evaluated\n\nThe comprehensive evaluation includes major KV cache compression strategies: StreamingLLM, H2O, a decoding-enabled SnapKV, R-KV, and KNorm, across a suite of eight benchmarks spanning mathematical, logical, and commonsense reasoning.\n\n## Main Findings\n\nClassical attention-based \"heavy-hitter\" strategies, which evict tokens based on accumulated attention scores, significantly outperform other methods, even defeating full-cache reasoning occasionally. This includes H2O and a novel simple extension of SnapKV (prompt-only compression method) to a decoding-enabled variant, SnapKV-Decoding.\n\nH2O and the decoding-enabled variant of SnapKV are dominant strategies for reasoning models, indicating the utility of heavy-hitter tracking for reasoning traces.\n\n## Important Tradeoff\n\nEviction strategies at low budgets can produce longer reasoning traces, revealing a tradeoff between cache size and inference costs."
    ],
    "durationSeconds": 8.399837787999997
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T23:15:52.509Z_

<details><summary>↩ Tool result · `toolu_016qMDYQL6GcSYoiHoA9mwAi`</summary>

```text
Web search results for query: "H2O heavy hitter oracle "local" OR "window" OR "recent" eviction baseline comparison arxiv"

Links: [{"title":"[2306.14048] H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/abs/2306.14048"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/6ceefa7b15572587b78ecfcebb2827f8-Paper-Conference.pdf"},{"title":"\"H\"₂⁢\"O\": Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/html/2306.14048v3"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language","url":"https://openreview.net/pdf?id=ctPizehA9D"},{"title":"H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/371871295_H_2O_Heavy-Hitter_Oracle_for_Efficient_Generative_Inference_of_Large_Language_Models"},{"title":"Paper page - H_2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://huggingface.co/papers/2306.14048"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...","url":"https://arxiv.org/pdf/2407.11550"},{"title":"hashevict:apre-attention kv cache eviction strategy using ...","url":"https://arxiv.org/pdf/2412.16187"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=RkRrPp7GKO"},{"title":"KV CACHE OPTIMIZATION STRATEGIES FOR SCALABLE AND EFFICIENT LLM INFERENCE","url":"https://arxiv.org/pdf/2603.20397"}]

Based on the search results, I found the H₂O (Heavy-Hitter Oracle) paper and relevant information about the baseline comparisons you're asking about.

## Key Findings:

H₂O is a KV cache eviction policy that dynamically retains a balance of recent and H₂ tokens, and the paper specifically evaluates different eviction strategies.

### Local vs. Heavy Hitter vs. Window Comparisons:

The researchers compared the performance of three KV cache eviction policies: only the KV embeddings of H₂, only the ones of local tokens, and H₂O that keeps both. Only retaining the embeddings of H₂ or local tokens resulted in performance degradation from 2.85% to 22.75%.

Incorporating both components, H₂O successfully retained the baseline performance with full embeddings. The model with only H₂ showed consistent improvement against the one with only local tokens, indicating H₂ might contribute more to maintaining performance.

### Baseline Comparisons:

H₂O implementation with 20% heavy hitters improved the throughput over three leading inference systems DeepSpeed Zero-Inference, Hugging Face Accelerate, and FlexGen by up to 29×, 29×, and 3× on OPT-6.7B and OPT-30B.

The arxiv paper ID is **2306.14048**, and you can find the full details at https://arxiv.org/abs/2306.14048.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "0bd1757f-32e0-4242-9aa5-72519deef625",
  "tool_use_result": {
    "query": "H2O heavy hitter oracle \"local\" OR \"window\" OR \"recent\" eviction baseline comparison arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PkGzLt2GiGVoJPQPzjem3A",
        "content": [
          {
            "title": "[2306.14048] H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models",
            "url": "https://arxiv.org/abs/2306.14048"
          },
          {
            "title": "H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/6ceefa7b15572587b78ecfcebb2827f8-Paper-Conference.pdf"
          },
          {
            "title": "\"H\"₂⁢\"O\": Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models",
            "url": "https://arxiv.org/html/2306.14048v3"
          },
          {
            "title": "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language",
            "url": "https://openreview.net/pdf?id=ctPizehA9D"
          },
          {
            "title": "H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/371871295_H_2O_Heavy-Hitter_Oracle_for_Efficient_Generative_Inference_of_Large_Language_Models"
          },
          {
            "title": "Paper page - H_2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models",
            "url": "https://huggingface.co/papers/2306.14048"
          },
          {
            "title": "Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...",
            "url": "https://arxiv.org/pdf/2407.11550"
          },
          {
            "title": "hashevict:apre-attention kv cache eviction strategy using ...",
            "url": "https://arxiv.org/pdf/2412.16187"
          },
          {
            "title": "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=RkRrPp7GKO"
          },
          {
            "title": "KV CACHE OPTIMIZATION STRATEGIES FOR SCALABLE AND EFFICIENT LLM INFERENCE",
            "url": "https://arxiv.org/pdf/2603.20397"
          }
        ]
      },
      "Based on the search results, I found the H₂O (Heavy-Hitter Oracle) paper and relevant information about the baseline comparisons you're asking about.\n\n## Key Findings:\n\nH₂O is a KV cache eviction policy that dynamically retains a balance of recent and H₂ tokens, and the paper specifically evaluates different eviction strategies.\n\n### Local vs. Heavy Hitter vs. Window Comparisons:\n\nThe researchers compared the performance of three KV cache eviction policies: only the KV embeddings of H₂, only the ones of local tokens, and H₂O that keeps both. Only retaining the embeddings of H₂ or local tokens resulted in performance degradation from 2.85% to 22.75%.\n\nIncorporating both components, H₂O successfully retained the baseline performance with full embeddings. The model with only H₂ showed consistent improvement against the one with only local tokens, indicating H₂ might contribute more to maintaining performance.\n\n### Baseline Comparisons:\n\nH₂O implementation with 20% heavy hitters improved the throughput over three leading inference systems DeepSpeed Zero-Inference, Hugging Face Accelerate, and FlexGen by up to 29×, 29×, and 3× on OPT-6.7B and OPT-30B.\n\nThe arxiv paper ID is **2306.14048**, and you can find the full details at https://arxiv.org/abs/2306.14048."
    ],
    "durationSeconds": 13.720669720999998
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014cYdTKKtHFFigYt6yUF5g5`</summary>

```json
{
  "query": "Scissorhands KV cache \"window attention\" OR \"local tokens\" baseline eviction arxiv 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "926b6f76-16e1-44d0-aaa7-62c2badaea7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdXnwKQM7dnQSrd64ucerJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4834,
      "cache_read_input_tokens": 26217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4834
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YDJUGmXNMaDNxQz54os9vM`</summary>

```json
{
  "query": "\"Taming the Fragility\" KV cache eviction 2024 arxiv recency local policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "f3469180-7f53-4fd4-9150-aef54f5a7975",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdXnwKQM7dnQSrd64ucerJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4834,
      "cache_read_input_tokens": 26217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4834
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T23:16:04.320Z_

<details><summary>↩ Tool result · `toolu_014cYdTKKtHFFigYt6yUF5g5`</summary>

```text
Web search results for query: "Scissorhands KV cache "window attention" OR "local tokens" baseline eviction arxiv 2023"

Links: [{"title":"[2305.17118] Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time","url":"https://arxiv.org/abs/2305.17118"},{"title":"hashevict:apre-attention kv cache eviction strategy using ...","url":"https://arxiv.org/pdf/2412.16187"},{"title":"HashEvict: A Pre-Attention KV Cache Eviction Strategy using Locality-Sensitive Hashing","url":"https://arxiv.org/html/2412.16187v3"},{"title":"Judge Q: Trainable Queries for Optimized Information Retention in KV Cache Eviction","url":"https://arxiv.org/html/2509.10798v2"},{"title":"NaCl: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://arxiv.org/html/2408.03675"},{"title":"2d management of kv- cache in llm inference via layer-wise ...","url":"https://arxiv.org/pdf/2404.04793"},{"title":"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time | OpenReview","url":"https://openreview.net/forum?id=JZfg6wGi6g"},{"title":"(PDF) HashEvict: A Pre-Attention KV Cache Eviction ...","url":"https://www.arxiv.org/pdf/2412.16187v1"},{"title":"SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget","url":"https://arxiv.org/html/2404.04793v1"},{"title":"In-context KV-Cache Eviction for LLMs via Attention-Gate","url":"https://arxiv.org/html/2410.12876v1"}]

Based on the search results, I found relevant information about Scissorhands and KV cache eviction:

Scissorhands is a system that maintains the memory usage of the KV cache at a fixed budget without finetuning the model. The method is inspired by the hypothesis of "persistence of importance": only pivotal tokens, which had a substantial influence at one step, will significantly influence future generations.

Scissorhands sequentially predicted the potentially pivotal tokens with the attention score above average within a history window. Scissorhands reduces the inference memory usage of the KV cache by up to 5X without compromising model quality.

Regarding comparisons with baseline methods, the search results show that Scissorhands is compared against other eviction strategies. FastGen proposed an algorithm to choose the best eviction strategy from 1) Locality strategy (like Sliding Window), 2) Special Tokens strategy (like StreamingLLM), 3) Local and Frequency strategy (like Scissorhands, H2O) and so on for each attention head during the inference.

The arxiv paper 2305.17118 was submitted on May 26, 2023, with a revision on August 28, 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "066d07a3-03e9-46e3-89be-4f243f08583b",
  "tool_use_result": {
    "query": "Scissorhands KV cache \"window attention\" OR \"local tokens\" baseline eviction arxiv 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UzSvvGiF4cgT1JhYqLVMi8",
        "content": [
          {
            "title": "[2305.17118] Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time",
            "url": "https://arxiv.org/abs/2305.17118"
          },
          {
            "title": "hashevict:apre-attention kv cache eviction strategy using ...",
            "url": "https://arxiv.org/pdf/2412.16187"
          },
          {
            "title": "HashEvict: A Pre-Attention KV Cache Eviction Strategy using Locality-Sensitive Hashing",
            "url": "https://arxiv.org/html/2412.16187v3"
          },
          {
            "title": "Judge Q: Trainable Queries for Optimized Information Retention in KV Cache Eviction",
            "url": "https://arxiv.org/html/2509.10798v2"
          },
          {
            "title": "NaCl: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time",
            "url": "https://arxiv.org/html/2408.03675"
          },
          {
            "title": "2d management of kv- cache in llm inference via layer-wise ...",
            "url": "https://arxiv.org/pdf/2404.04793"
          },
          {
            "title": "Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time | OpenReview",
            "url": "https://openreview.net/forum?id=JZfg6wGi6g"
          },
          {
            "title": "(PDF) HashEvict: A Pre-Attention KV Cache Eviction ...",
            "url": "https://www.arxiv.org/pdf/2412.16187v1"
          },
          {
            "title": "SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget",
            "url": "https://arxiv.org/html/2404.04793v1"
          },
          {
            "title": "In-context KV-Cache Eviction for LLMs via Attention-Gate",
            "url": "https://arxiv.org/html/2410.12876v1"
          }
        ]
      },
      "Based on the search results, I found relevant information about Scissorhands and KV cache eviction:\n\nScissorhands is a system that maintains the memory usage of the KV cache at a fixed budget without finetuning the model. The method is inspired by the hypothesis of \"persistence of importance\": only pivotal tokens, which had a substantial influence at one step, will significantly influence future generations.\n\nScissorhands sequentially predicted the potentially pivotal tokens with the attention score above average within a history window. Scissorhands reduces the inference memory usage of the KV cache by up to 5X without compromising model quality.\n\nRegarding comparisons with baseline methods, the search results show that Scissorhands is compared against other eviction strategies. FastGen proposed an algorithm to choose the best eviction strategy from 1) Locality strategy (like Sliding Window), 2) Special Tokens strategy (like StreamingLLM), 3) Local and Frequency strategy (like Scissorhands, H2O) and so on for each attention head during the inference.\n\nThe arxiv paper 2305.17118 was submitted on May 26, 2023, with a revision on August 28, 2023."
    ],
    "durationSeconds": 6.400349770000001
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T23:16:05.449Z_

<details><summary>↩ Tool result · `toolu_01YDJUGmXNMaDNxQz54os9vM`</summary>

```text
Web search results for query: ""Taming the Fragility" KV cache eviction 2024 arxiv recency local policy"

Links: [{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"[2510.13334] Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/abs/2510.13334"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://www.aimodels.fyi/papers/arxiv/taming-fragility-kv-cache-eviction-llm-inference"},{"title":"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=nJgS06sX3O"},{"title":"GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub","url":"https://github.com/FFY0/DefensiveKV"},{"title":"DEFENSIVEKV: TAMING THE FRAGILITY OF KV CACHE ...","url":"https://openreview.net/pdf?id=nJgS06sX3O"},{"title":"TAMING THE FRAGILITY OF KV CACHE EVICTION","url":"https://openreview.net/pdf/2d8c7805c4fcdb477dd04f7b60dd05bd9551c246.pdf"},{"title":"(PDF) Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://www.researchgate.net/publication/396517805_Taming_the_Fragility_of_KV_Cache_Eviction_in_LLM_Inference"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...","url":"https://arxiv.org/pdf/2407.11550"},{"title":"FFY0 (Yuan Feng) · GitHub","url":"https://github.com/FFY0"}]

I found the paper you're looking for. Here are the key findings:

## "Taming the Fragility of KV Cache Eviction in LLM Inference"

KV cache eviction is crucial for efficient long-sequence inference in LLMs. Early methods like StreamingLLM retained only recent cache entries, while subsequent H2O and Scissorhands introduced importance-based eviction, assuming "cache importance stability"—that a small set of entries remains consistently important.

### The Core Problem

The underlying assumption is inherently fragile, making mean aggregation highly vulnerable in extreme cases. The paper reveals the fragility of this assumption, showing prevalent mean aggregation's vulnerability.

### Proposed Solution

The authors propose a defensive aggregation strategy: a two-step, linear-time approach that controls worst-case risk, thereby defending against extreme cases with negligible computational overhead. They introduce two novel cache eviction methods: DefensiveKV and Layer-DefensiveKV, with DefensiveKV directly integrating defensive aggregation into the traditional cache eviction workflow by replacing conventional mean aggregation.

### Results

Across seven task domains (18 datasets), their methods reduce generation quality loss by 2.3x and 4.3x respectively, versus the strongest baseline under a 20% cache size.

**Paper Details:** arXiv:2510.13334 (October 2025), accepted to ICLR 2026. Code is available at GitHub: FFY0/DefensiveKV.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "d72e1af8-2e53-4baf-97e2-b91bab835141",
  "tool_use_result": {
    "query": "\"Taming the Fragility\" KV cache eviction 2024 arxiv recency local policy",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H35xwVyFkdHzXctf7N3oV7",
        "content": [
          {
            "title": "Taming the Fragility of KV Cache Eviction in LLM Inference",
            "url": "https://arxiv.org/html/2510.13334v1"
          },
          {
            "title": "[2510.13334] Taming the Fragility of KV Cache Eviction in LLM Inference",
            "url": "https://arxiv.org/abs/2510.13334"
          },
          {
            "title": "Taming the Fragility of KV Cache Eviction in LLM Inference",
            "url": "https://www.aimodels.fyi/papers/arxiv/taming-fragility-kv-cache-eviction-llm-inference"
          },
          {
            "title": "DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview",
            "url": "https://openreview.net/forum?id=nJgS06sX3O"
          },
          {
            "title": "GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub",
            "url": "https://github.com/FFY0/DefensiveKV"
          },
          {
            "title": "DEFENSIVEKV: TAMING THE FRAGILITY OF KV CACHE ...",
            "url": "https://openreview.net/pdf?id=nJgS06sX3O"
          },
          {
            "title": "TAMING THE FRAGILITY OF KV CACHE EVICTION",
            "url": "https://openreview.net/pdf/2d8c7805c4fcdb477dd04f7b60dd05bd9551c246.pdf"
          },
          {
            "title": "(PDF) Taming the Fragility of KV Cache Eviction in LLM Inference",
            "url": "https://www.researchgate.net/publication/396517805_Taming_the_Fragility_of_KV_Cache_Eviction_in_LLM_Inference"
          },
          {
            "title": "Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...",
            "url": "https://arxiv.org/pdf/2407.11550"
          },
          {
            "title": "FFY0 (Yuan Feng) · GitHub",
            "url": "https://github.com/FFY0"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key findings:\n\n## \"Taming the Fragility of KV Cache Eviction in LLM Inference\"\n\nKV cache eviction is crucial for efficient long-sequence inference in LLMs. Early methods like StreamingLLM retained only recent cache entries, while subsequent H2O and Scissorhands introduced importance-based eviction, assuming \"cache importance stability\"—that a small set of entries remains consistently important.\n\n### The Core Problem\n\nThe underlying assumption is inherently fragile, making mean aggregation highly vulnerable in extreme cases. The paper reveals the fragility of this assumption, showing prevalent mean aggregation's vulnerability.\n\n### Proposed Solution\n\nThe authors propose a defensive aggregation strategy: a two-step, linear-time approach that controls worst-case risk, thereby defending against extreme cases with negligible computational overhead. They introduce two novel cache eviction methods: DefensiveKV and Layer-DefensiveKV, with DefensiveKV directly integrating defensive aggregation into the traditional cache eviction workflow by replacing conventional mean aggregation.\n\n### Results\n\nAcross seven task domains (18 datasets), their methods reduce generation quality loss by 2.3x and 4.3x respectively, versus the strongest baseline under a 20% cache size.\n\n**Paper Details:** arXiv:2510.13334 (October 2025), accepted to ICLR 2026. Code is available at GitHub: FFY0/DefensiveKV."
    ],
    "durationSeconds": 7.143195334999997
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to compile a comprehensive report. Let me summarize the findings:

1. **Recency/position-based eviction as a control condition**: No paper found that explicitly uses recency/position-based eviction as a "control condition" in the experimental design sense (i.e., to rule out confounds). Instead, papers like H2O, Scissorhands, and StreamingLLM use "local tokens" (recent window) as one of their baselines to compare against their attention-score-based methods. But these are performance baselines, not methodological controls designed to isolate scoring-dependency effects.


2. **Known properties of FIFO/oldest-first eviction**: Several papers demonstrate the limitations of pure recency-based approaches. StreamingLLM shows that keeping only recent tokens fails when initial "attention sink" tokens get evicted, so they preserve both sink tokens and the recent window. H2O compares local-only against heavy-hitter-only strategies and finds that recency alone underperforms, indicating it's insufficient on its own. DefensiveKV identifies fragility in this approach.

3. **Attention-score-based vs position-based differences on reasoning**: Recent work directly compares these strategies on reasoning benchmarks, with heavy-hitter methods significantly outperforming position-based approaches. Papers like "Hold Onto That Thought" and ForesightKV specifically address reasoning models, while LazyEviction examines attention patterns for this task. Notably, I haven't found any paper that uses pure recency-based eviction as a baseline control to isolate whether the scoring method itself or phase-dependent effects are driving the performance differences.

This suggests our approach of using recency eviction as a scoring-independent control—to show that phase gradient effects are specifically tied to attention-based scoring rather than eviction in general—appears to be methodologically novel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "456ea978-d082-40f0-a20f-4ba81aa43bd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6yPXwEgvLvKmx63Vmza8Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 31051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1918
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 25_

## 文献调研结果

### Q1: Recency/position-based eviction 作为 control condition 的先例

**无直接先例。** 现有文献中，recency/window eviction 均作为 **performance baseline**（比较方法优劣），而非作为 **methodological control**（排除 scoring mechanism 作为 confound）。

具体角色：
- **H2O** (NeurIPS 2023, 2306.14048): 比较 "local only" vs "H2 only" vs "H2O"，但目的是展示两种 signal 的互补性，不是排除 scoring circularity
- **StreamingLLM** (ICLR 2024, 2309.17453): sink + recent window 作为其方法本身，不作为 control
- **Scissorhands** (2305.17118): 使用 sliding window 作为 baseline 之一

### Q2: FIFO/recency eviction 的已知性质

| 论文 | 关键发现 |
|------|---------|
| StreamingLLM | 纯 window attention 丢失 attention sink 后 perplexity 崩塌 |
| H2O | local-only 比 H2-only 表现更差（2.85%–22.75% 性能退化），说明 recency ≠ importance |
| Hold Onto That Thought (NeurIPS 2025, 2512.12008) | 在 reasoning task 上，heavy-hitter 方法显著优于 StreamingLLM 的 recency 策略 |
| DefensiveKV (ICLR 2026, 2510.13334) | 将 StreamingLLM 归类为 "early method that loses valuable information" |

### Q3: Attention-based vs Position-based 在 reasoning task 上的行为差异

- **"Hold Onto That Thought"** 是最直接的比较：在 GSM8K/MATH500 等 reasoning benchmark 上，H2O/SnapKV-D（attention-based）显著优于 StreamingLLM（position-based），甚至偶尔超越 full-cache
- **ForesightKV** (2602.03203): 针对 reasoning model，学习 long-term contribution，隐含说明 position 信号不足
- **LazyEviction** (2506.15969): 发现 recurring tokens（间歇性重要）被 position-based 方法错误驱逐，导致 reasoning 性能崩塌

### 判断

**我们的 recency control 用法是方法论创新。** 现有文献将 recency eviction 视为一种（次优的）方法或 baseline，但无人将其作为 scoring-independent control 来检验 "观察到的 phase gradient 是否源于 attention scoring mechanism 本身"。

**论文中可以这样 claim：**
> While prior work (H2O, StreamingLLM) has established that recency-based eviction underperforms attention-based methods, we repurpose it as a scoring-independent control to isolate whether observed phase-dependent behavior arises from the eviction mechanism itself or specifically from attention-score-based token selection.

可引用 H2O 和 "Hold Onto That Thought" 作为 recency eviction 性质的支撑文献，同时指出我们的 control design 用法是新的。

Sources:
- [H2O: Heavy-Hitter Oracle (NeurIPS 2023)](https://arxiv.org/abs/2306.14048)
- [StreamingLLM (ICLR 2024)](https://arxiv.org/abs/2309.17453)
- [Hold Onto That Thought (NeurIPS 2025)](https://arxiv.org/abs/2512.12008)
- [DefensiveKV (ICLR 2026)](https://arxiv.org/abs/2510.13334)
- [Scissorhands](https://arxiv.org/abs/2305.17118)
- [ForesightKV](https://arxiv.org/html/2602.03203v1)
- [LazyEviction](https://arxiv.org/html/2506.15969)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "uuid": "a507bd5a-2786-47f0-a25d-3628a6a5dd33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6yPXwEgvLvKmx63Vmza8Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 31051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1918
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 26_

## 文献调研结果

### Q1: Recency/position-based eviction 作为 control condition 的先例

**无直接先例。** 现有文献中，recency/window eviction 均作为 **performance baseline**（比较方法优劣），而非作为 **methodological control**（排除 scoring mechanism 作为 confound）。

具体角色：
- **H2O** (NeurIPS 2023, 2306.14048): 比较 "local only" vs "H2 only" vs "H2O"，但目的是展示两种 signal 的互补性，不是排除 scoring circularity
- **StreamingLLM** (ICLR 2024, 2309.17453): sink + recent window 作为其方法本身，不作为 control
- **Scissorhands** (2305.17118): 使用 sliding window 作为 baseline 之一

### Q2: FIFO/recency eviction 的已知性质

| 论文 | 关键发现 |
|------|---------|
| StreamingLLM | 纯 window attention 丢失 attention sink 后 perplexity 崩塌 |
| H2O | local-only 比 H2-only 表现更差（2.85%–22.75% 性能退化），说明 recency ≠ importance |
| Hold Onto That Thought (NeurIPS 2025, 2512.12008) | 在 reasoning task 上，heavy-hitter 方法显著优于 StreamingLLM 的 recency 策略 |
| DefensiveKV (ICLR 2026, 2510.13334) | 将 StreamingLLM 归类为 "early method that loses valuable information" |

### Q3: Attention-based vs Position-based 在 reasoning task 上的行为差异

- **"Hold Onto That Thought"** 是最直接的比较：在 GSM8K/MATH500 等 reasoning benchmark 上，H2O/SnapKV-D（attention-based）显著优于 StreamingLLM（position-based），甚至偶尔超越 full-cache
- **ForesightKV** (2602.03203): 针对 reasoning model，学习 long-term contribution，隐含说明 position 信号不足
- **LazyEviction** (2506.15969): 发现 recurring tokens（间歇性重要）被 position-based 方法错误驱逐，导致 reasoning 性能崩塌

### 判断

**我们的 recency control 用法是方法论创新。** 现有文献将 recency eviction 视为一种（次优的）方法或 baseline，但无人将其作为 scoring-independent control 来检验 "观察到的 phase gradient 是否源于 attention scoring mechanism 本身"。

**论文中可以这样 claim：**
> While prior work (H2O, StreamingLLM) has established that recency-based eviction underperforms attention-based methods, we repurpose it as a scoring-independent control to isolate whether observed phase-dependent behavior arises from the eviction mechanism itself or specifically from attention-score-based token selection.

可引用 H2O 和 "Hold Onto That Thought" 作为 recency eviction 性质的支撑文献，同时指出我们的 control design 用法是新的。

Sources:
- [H2O: Heavy-Hitter Oracle (NeurIPS 2023)](https://arxiv.org/abs/2306.14048)
- [StreamingLLM (ICLR 2024)](https://arxiv.org/abs/2309.17453)
- [Hold Onto That Thought (NeurIPS 2025)](https://arxiv.org/abs/2512.12008)
- [DefensiveKV (ICLR 2026)](https://arxiv.org/abs/2510.13334)
- [Scissorhands](https://arxiv.org/abs/2305.17118)
- [ForesightKV](https://arxiv.org/html/2602.03203v1)
- [LazyEviction](https://arxiv.org/html/2506.15969)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 91700,
  "duration_api_ms": 129891,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "0648f41f-953e-4ed1-97e9-1aad11f2fab2",
  "total_cost_usd": 0.5199475,
  "usage": {
    "input_tokens": 1924,
    "cache_creation_input_tokens": 21128,
    "cache_read_input_tokens": 118519,
    "output_tokens": 2407,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21128,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1718,
        "cache_read_input_tokens": 31051,
        "cache_creation_input_tokens": 1918,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1918
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 158908,
      "outputTokens": 3987,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 8,
      "costUSD": 0.258843,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1924,
      "outputTokens": 2407,
      "cacheReadInputTokens": 118519,
      "cacheCreationInputTokens": 21128,
      "webSearchRequests": 0,
      "costUSD": 0.26110449999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5806cee1-d8a2-43cf-8e68-669ae46f7e3e"
}
```

</details>

---
