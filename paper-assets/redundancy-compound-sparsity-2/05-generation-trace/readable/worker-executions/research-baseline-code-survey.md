# research baseline code survey

**redundancy compound sparsity 2** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_research_baseline-code-survey_20260512T142059.log`
- **Structured JSON:** [`78857a90267ef706a4d3.json`](../../sessions/78/78857a90267ef706a4d3.json)

## Before a recorded user message

46 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "9d6ac6a3-3407-48a2-8f36-dd55cd0004bb",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-solver-verified-formalizer-rl/memory/"
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
    "resetsAt": 1778610000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "15d62333-c26d-45b0-af55-f7df0963ac76",
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to do a baseline code survey for their CARC (O(1) KV cache eviction) research project. Let me break this down:

1. Research kvpress framework (NVIDIA)
2. Research R-KV code
3. Create a competitor taxonomy table
4. Check installation feasibility

Let me start by loading the necessary tools and doing the research in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "492661cf-ebfe-4fff-9af3-6da5ee0f6c68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdYGEKKqNK5vHpUatJN8fo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11498,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11498
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

开始调研 baseline 代码和框架。先加载必要工具，然后并行搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "e00f3c1c-b4bc-4765-b6c7-5449c5d04f5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdYGEKKqNK5vHpUatJN8fo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11498,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11498
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Y2T16AjEKaMEjGfFEttkGh`</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "9fa95511-df9c-4e0c-b84e-ed85fe5aa3b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdYGEKKqNK5vHpUatJN8fo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11498,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11498
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-12T14:21:10.323Z_

<details><summary>↩ Tool result · `toolu_01Y2T16AjEKaMEjGfFEttkGh`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "32253e02-0de0-4107-a1b2-e909dc2c3762",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me start the research in parallel. I need to:
1. Read the existing literature_map.yaml
2. Search for kvpress
3. Search for R-KV
4. Search for other KV cache eviction baselines

Let me do all of these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "025733cc-9403-443f-9ed7-2623ce3b0ac1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014j1i5U4JLFsuBdx2BQoYDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2440,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2440
      },
      "output_tokens": 28,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 9_

并行启动调研：读取已有文献、搜索 kvpress 和 R-KV。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "ea239b29-d175-45f2-800e-89c25bad9f0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014j1i5U4JLFsuBdx2BQoYDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2440,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2440
      },
      "output_tokens": 28,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NQYoDXcfwV2ZHPEdddGGuc`</summary>

```json
{
  "project": "solver-verified-formalizer-rl",
  "file": "literature_map.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "33bcf506-d836-4159-b579-6f4d4b168992",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014j1i5U4JLFsuBdx2BQoYDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2440,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2440
      },
      "output_tokens": 28,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T14:21:15.988Z_

<details><summary>↩ Tool result · `toolu_01NQYoDXcfwV2ZHPEdddGGuc`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'solver-verified-formalizer-rl'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "b1100412-4377-4a19-9763-5a35ec641922",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No literature_map.yaml found for 'solver-verified-formalizer-rl'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'solver-verified-formalizer-rl'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HPu9gk3N9P5urLGTXML4fc`</summary>

```json
{
  "query": "kvpress NVIDIA KV cache compression PyPI GitHub 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "6778dd6f-bb34-4c2d-b768-c52800e7c930",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014j1i5U4JLFsuBdx2BQoYDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2440,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2440
      },
      "output_tokens": 28,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017Qbricv9JhrD67Uwft5YTx`</summary>

```json
{
  "query": "R-KV reasoning KV cache eviction GitHub code DeepSeek"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "1c966dbe-1218-4195-b08a-de05e27699c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014j1i5U4JLFsuBdx2BQoYDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2440,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2440
      },
      "output_tokens": 28,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VWivUMLWsFeHvotE646bjv`</summary>

```json
{
  "query": "SkipKV FASA KV cache eviction reasoning LLM GitHub 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "9953ed89-d464-4125-ac66-a380e8ca1f2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014j1i5U4JLFsuBdx2BQoYDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2440,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2440
      },
      "output_tokens": 28,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T14:21:25.254Z_

<details><summary>↩ Tool result · `toolu_017Qbricv9JhrD67Uwft5YTx`</summary>

```text
Web search results for query: "R-KV reasoning KV cache eviction GitHub code DeepSeek"

Links: [{"title":"[Feature Request] Per-phase KV cache quantization for reasoning models (DeepSeek-R1) · Issue #21679 · ggml-org/llama.cpp","url":"https://github.com/ggml-org/llama.cpp/issues/21679"},{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://zefan-cai.github.io/R-KV.page/"},{"title":"ktransformers/doc/en/deepseek-v2-injection.md at main · kvcache-ai/ktransformers","url":"https://github.com/kvcache-ai/ktransformers/blob/main/doc/en/deepseek-v2-injection.md"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"KV Cache Compression, But What Must We Give in Return ...","url":"https://aclanthology.org/2024.findings-emnlp.266.pdf"},{"title":"DeepSeek-V4: a million-token context that agents can actually use","url":"https://huggingface.co/blog/deepseekv4"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"DeepSeek V4 Compressed Attention: KV-Cache 2% Explained","url":"https://deepseek.ai/blog/deepseek-v4-compressed-attention"},{"title":"Hierarchical Adaptive Eviction for KV Cache Management in Multimodal Language Models","url":"https://arxiv.org/html/2602.02197v1"}]

Based on the search results, here's what I found about R-KV reasoning KV cache eviction:

## R-KV: Redundancy-aware KV Cache Compression

R-KV is a highly efficient decoding time KV Cache compression method to serve reasoning Models, with a release announced on May 29, 2025.

### Key Approach

R-KV consists of three key components: (1) an attention-based importance scoring mechanism that selects critical tokens for retention, (2) a dynamic redundancy scoring mechanism that identifies repetitive tokens through real-time analysis of key vectors, and (3) a joint eviction mechanism that balances both redundancy and importance to optimize cache efficiency.

### Performance Results

By selectively retaining only 10-34% of the original KV cache, R-KV achieves comparable performance parity with the uncompressed reasoning model, outperforming state-of-the-art compression baselines with only 60% of the performance. At 16 % (Llama-8B) or 33 % (Qwen-14B) cache, R-KV reaches 105 % of FullKV accuracy—evidence that trimming redundant tokens can improve reasoning quality.

### GitHub Repository

The R-KV code is available at the GitHub repository Zefan-Cai/R-KV, published as a NeurIPS 2025 paper on Redundancy-aware KV Cache Compression for Reasoning Models. The repository includes analysis_scripts/analysis.ipynb for visualization functions to illustrate the multi-step token eviction pattern.

### Memory Efficiency

R-KV allocates two fixed-size buffers—one for the retained KV cache and one for freshly generated tokens. Because these buffers stay the same size regardless of sequence length, memory usage remains constant, unlike FullKV, whose memory grows linearly with the sequence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "7765cd0d-920d-4bf9-98ce-3b39e420d56f",
  "tool_use_result": {
    "query": "R-KV reasoning KV cache eviction GitHub code DeepSeek",
    "results": [
      {
        "tool_use_id": "srvtoolu_0188YGgLh5d2g7YDHru9567Y",
        "content": [
          {
            "title": "[Feature Request] Per-phase KV cache quantization for reasoning models (DeepSeek-R1) · Issue #21679 · ggml-org/llama.cpp",
            "url": "https://github.com/ggml-org/llama.cpp/issues/21679"
          },
          {
            "title": "GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models",
            "url": "https://github.com/Zefan-Cai/R-KV"
          },
          {
            "title": "R-KV: Redundancy-aware KV Cache Compression for Reasoning Models",
            "url": "https://zefan-cai.github.io/R-KV.page/"
          },
          {
            "title": "ktransformers/doc/en/deepseek-v2-injection.md at main · kvcache-ai/ktransformers",
            "url": "https://github.com/kvcache-ai/ktransformers/blob/main/doc/en/deepseek-v2-injection.md"
          },
          {
            "title": "Expected Attention: KV Cache Compression by Estimating Attention",
            "url": "https://arxiv.org/pdf/2510.00636"
          },
          {
            "title": "KV Cache Compression, But What Must We Give in Return ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.266.pdf"
          },
          {
            "title": "DeepSeek-V4: a million-token context that agents can actually use",
            "url": "https://huggingface.co/blog/deepseekv4"
          },
          {
            "title": "R-KV: Redundancy-aware KV Cache Compression for Reasoning Models",
            "url": "https://arxiv.org/html/2505.24133"
          },
          {
            "title": "DeepSeek V4 Compressed Attention: KV-Cache 2% Explained",
            "url": "https://deepseek.ai/blog/deepseek-v4-compressed-attention"
          },
          {
            "title": "Hierarchical Adaptive Eviction for KV Cache Management in Multimodal Language Models",
            "url": "https://arxiv.org/html/2602.02197v1"
          }
        ]
      },
      "Based on the search results, here's what I found about R-KV reasoning KV cache eviction:\n\n## R-KV: Redundancy-aware KV Cache Compression\n\nR-KV is a highly efficient decoding time KV Cache compression method to serve reasoning Models, with a release announced on May 29, 2025.\n\n### Key Approach\n\nR-KV consists of three key components: (1) an attention-based importance scoring mechanism that selects critical tokens for retention, (2) a dynamic redundancy scoring mechanism that identifies repetitive tokens through real-time analysis of key vectors, and (3) a joint eviction mechanism that balances both redundancy and importance to optimize cache efficiency.\n\n### Performance Results\n\nBy selectively retaining only 10-34% of the original KV cache, R-KV achieves comparable performance parity with the uncompressed reasoning model, outperforming state-of-the-art compression baselines with only 60% of the performance. At 16 % (Llama-8B) or 33 % (Qwen-14B) cache, R-KV reaches 105 % of FullKV accuracy—evidence that trimming redundant tokens can improve reasoning quality.\n\n### GitHub Repository\n\nThe R-KV code is available at the GitHub repository Zefan-Cai/R-KV, published as a NeurIPS 2025 paper on Redundancy-aware KV Cache Compression for Reasoning Models. The repository includes analysis_scripts/analysis.ipynb for visualization functions to illustrate the multi-step token eviction pattern.\n\n### Memory Efficiency\n\nR-KV allocates two fixed-size buffers—one for the retained KV cache and one for freshly generated tokens. Because these buffers stay the same size regardless of sequence length, memory usage remains constant, unlike FullKV, whose memory grows linearly with the sequence."
    ],
    "durationSeconds": 8.515329801
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T14:21:25.474Z_

<details><summary>↩ Tool result · `toolu_01VWivUMLWsFeHvotE646bjv`</summary>

```text
Web search results for query: "SkipKV FASA KV cache eviction reasoning LLM GitHub 2025"

Links: [{"title":"GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub","url":"https://github.com/FFY0/AdaKV"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://janghyun1230.github.io/paper/fastkvzip26.pdf"},{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://www.arxiv.org/pdf/2601.17668"},{"title":"GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub","url":"https://github.com/FFY0/DefensiveKV"},{"title":"GitHub - antgroup/cakekv · GitHub","url":"https://github.com/antgroup/cakekv"},{"title":"GitHub - llm-d/llm-d-kv-cache: Distributed KV cache scheduling & offloading libraries · GitHub","url":"https://github.com/llm-d/llm-d-kv-cache"}]

Based on the search results, I found relevant information about KV cache eviction methods for LLMs, though the specific methods you mentioned (SkipKV and FASA) didn't appear prominently in these results. However, I can provide you with an overview of the KV cache eviction landscape in 2025:

## Recent KV Cache Eviction Methods (2025)

The search results show several recent approaches to KV cache eviction for efficient LLM inference:

**Methods Focused on Reasoning and Eviction:**
- SnapKV improved by introducing a pooling mechanism, while more recent work like CriticalKV employed the norm of projected value states to offer a more principled measure of importance
- CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences by Ziran Qin and colleagues was published at ICLR 2025
- R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration
- Fast KVzip achieves superior performance compared to decoding-scenario compression baselines and achieves near-lossless performance with a KV budget size of 4K

**Comprehensive Resources:**
The TreeAI-Lab/Awesome-KV-Cache-Management repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links.

If you're looking specifically for SkipKV or FASA implementations, I recommend checking the comprehensive GitHub repositories mentioned above, as they may contain links to those specific methods or papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "08b80ff9-b26b-457b-8ce7-86a20fd64d10",
  "tool_use_result": {
    "query": "SkipKV FASA KV cache eviction reasoning LLM GitHub 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VnrnmtN56TzZNDd2jxVbss",
        "content": [
          {
            "title": "GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub",
            "url": "https://github.com/FFY0/AdaKV"
          },
          {
            "title": "GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub",
            "url": "https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"
          },
          {
            "title": "Taming the Fragility of KV Cache Eviction in LLM Inference",
            "url": "https://arxiv.org/html/2510.13334v1"
          },
          {
            "title": "Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction",
            "url": "https://janghyun1230.github.io/paper/fastkvzip26.pdf"
          },
          {
            "title": "Reformulating KV Cache Eviction Problem for Long-Context LLM Inference",
            "url": "https://arxiv.org/html/2605.07234"
          },
          {
            "title": "GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).",
            "url": "https://github.com/October2001/Awesome-KV-Cache-Compression"
          },
          {
            "title": "Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction",
            "url": "https://www.arxiv.org/pdf/2601.17668"
          },
          {
            "title": "GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub",
            "url": "https://github.com/FFY0/DefensiveKV"
          },
          {
            "title": "GitHub - antgroup/cakekv · GitHub",
            "url": "https://github.com/antgroup/cakekv"
          },
          {
            "title": "GitHub - llm-d/llm-d-kv-cache: Distributed KV cache scheduling & offloading libraries · GitHub",
            "url": "https://github.com/llm-d/llm-d-kv-cache"
          }
        ]
      },
      "Based on the search results, I found relevant information about KV cache eviction methods for LLMs, though the specific methods you mentioned (SkipKV and FASA) didn't appear prominently in these results. However, I can provide you with an overview of the KV cache eviction landscape in 2025:\n\n## Recent KV Cache Eviction Methods (2025)\n\nThe search results show several recent approaches to KV cache eviction for efficient LLM inference:\n\n**Methods Focused on Reasoning and Eviction:**\n- SnapKV improved by introducing a pooling mechanism, while more recent work like CriticalKV employed the norm of projected value states to offer a more principled measure of importance\n- CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences by Ziran Qin and colleagues was published at ICLR 2025\n- R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration\n- Fast KVzip achieves superior performance compared to decoding-scenario compression baselines and achieves near-lossless performance with a KV budget size of 4K\n\n**Comprehensive Resources:**\nThe TreeAI-Lab/Awesome-KV-Cache-Management repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links.\n\nIf you're looking specifically for SkipKV or FASA implementations, I recommend checking the comprehensive GitHub repositories mentioned above, as they may contain links to those specific methods or papers."
    ],
    "durationSeconds": 7.930625835999999
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T14:21:25.749Z_

<details><summary>↩ Tool result · `toolu_01HPu9gk3N9P5urLGTXML4fc`</summary>

```text
Web search results for query: "kvpress NVIDIA KV cache compression PyPI GitHub 2025 2026"

Links: [{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"GitHub - lloydchang/NVIDIA-kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/lloydchang/NVIDIA-kvpress"},{"title":"Releases · NVIDIA/kvpress","url":"https://github.com/NVIDIA/kvpress/releases"},{"title":"GitHub - snu-mllab/KVzip: [NeurIPS'25 Oral] Query-agnostic KV cache eviction: 3–4× reduction in memory and 2× decrease in latency (Qwen3/2.5, Gemma3, LLaMA3)","url":"https://github.com/snu-mllab/KVzip"},{"title":"Request for Head-Specific KV Cache Compression Feature · Issue #7 · NVIDIA/kvpress","url":"https://github.com/NVIDIA/kvpress/issues/7"},{"title":"kvpress/kvpress/presses/composed_press.py at main · NVIDIA/kvpress","url":"https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/composed_press.py"},{"title":"GitHub - Janghyun1230/FastKVzip: Accurate and fast KV cache compression with a gating mechanism · GitHub","url":"https://github.com/Janghyun1230/FastKVzip"},{"title":"kvpress/kvpress/presses/expected_attention_press.py at main · NVIDIA/kvpress","url":"https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/expected_attention_press.py"},{"title":"kvpress/README.md at main · NVIDIA/kvpress","url":"https://github.com/NVIDIA/kvpress/blob/main/README.md"},{"title":"kvpress/kvpress/presses/tova_press.py at main · NVIDIA/kvpress","url":"https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/tova_press.py"}]

Based on the search results, I found comprehensive information about kvpress:

## Overview

kvpress implements multiple KV cache compression methods and benchmarks using 🤗 transformers, aiming to simplify the development of new methods for researchers and developers in this field.

## The Problem It Solves

Deploying long-context LLMs is costly due to the linear growth of the key-value (KV) cache in transformer models. For example, handling 1M tokens with Llama 3.1-70B in float16 requires up to 330GB of memory.

## Key Features

KVPress provides a set of "presses" that compress the KV cache during the prefilling-phase. Each press is associated with a compression_ratio attribute that measures the compression of the cache.

## Compression Methods

The project includes various compression approaches such as:
- ChunkPress: compress the KV cache on each sequence chunk separately.
- CriticalKVPress and CriticalAdaKVPress: refine the scores using the L1 norm of Wo @ values, coupled with a two-stage selection.
- DecodingPress wrapper supports decoding compression as a new experimental feature.

## Recent Updates (2025-2026)

In July 2025, NVIDIA KVpress added support for KVzip. Additionally, recent updates include Decoding Press Functionality for support of KV cache compression during the decoding phase, AIME25 & Math500 Benchmarks for new evaluation datasets for mathematical reasoning tasks, and post_init_from_model Hook for model-specific initialization support in BasePress.

The project is maintained on GitHub at NVIDIA/kvpress and provides both the implementation and evaluation tools for KV cache compression methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "9bbe7dc1-9096-4da8-8446-7ab66695031e",
  "tool_use_result": {
    "query": "kvpress NVIDIA KV cache compression PyPI GitHub 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018pKdpSFiz7ifQXEAggSpAD",
        "content": [
          {
            "title": "GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub",
            "url": "https://github.com/NVIDIA/kvpress"
          },
          {
            "title": "GitHub - lloydchang/NVIDIA-kvpress: LLM KV cache compression made easy · GitHub",
            "url": "https://github.com/lloydchang/NVIDIA-kvpress"
          },
          {
            "title": "Releases · NVIDIA/kvpress",
            "url": "https://github.com/NVIDIA/kvpress/releases"
          },
          {
            "title": "GitHub - snu-mllab/KVzip: [NeurIPS'25 Oral] Query-agnostic KV cache eviction: 3–4× reduction in memory and 2× decrease in latency (Qwen3/2.5, Gemma3, LLaMA3)",
            "url": "https://github.com/snu-mllab/KVzip"
          },
          {
            "title": "Request for Head-Specific KV Cache Compression Feature · Issue #7 · NVIDIA/kvpress",
            "url": "https://github.com/NVIDIA/kvpress/issues/7"
          },
          {
            "title": "kvpress/kvpress/presses/composed_press.py at main · NVIDIA/kvpress",
            "url": "https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/composed_press.py"
          },
          {
            "title": "GitHub - Janghyun1230/FastKVzip: Accurate and fast KV cache compression with a gating mechanism · GitHub",
            "url": "https://github.com/Janghyun1230/FastKVzip"
          },
          {
            "title": "kvpress/kvpress/presses/expected_attention_press.py at main · NVIDIA/kvpress",
            "url": "https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/expected_attention_press.py"
          },
          {
            "title": "kvpress/README.md at main · NVIDIA/kvpress",
            "url": "https://github.com/NVIDIA/kvpress/blob/main/README.md"
          },
          {
            "title": "kvpress/kvpress/presses/tova_press.py at main · NVIDIA/kvpress",
            "url": "https://github.com/NVIDIA/kvpress/blob/main/kvpress/presses/tova_press.py"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about kvpress:\n\n## Overview\n\nkvpress implements multiple KV cache compression methods and benchmarks using 🤗 transformers, aiming to simplify the development of new methods for researchers and developers in this field.\n\n## The Problem It Solves\n\nDeploying long-context LLMs is costly due to the linear growth of the key-value (KV) cache in transformer models. For example, handling 1M tokens with Llama 3.1-70B in float16 requires up to 330GB of memory.\n\n## Key Features\n\nKVPress provides a set of \"presses\" that compress the KV cache during the prefilling-phase. Each press is associated with a compression_ratio attribute that measures the compression of the cache.\n\n## Compression Methods\n\nThe project includes various compression approaches such as:\n- ChunkPress: compress the KV cache on each sequence chunk separately.\n- CriticalKVPress and CriticalAdaKVPress: refine the scores using the L1 norm of Wo @ values, coupled with a two-stage selection.\n- DecodingPress wrapper supports decoding compression as a new experimental feature.\n\n## Recent Updates (2025-2026)\n\nIn July 2025, NVIDIA KVpress added support for KVzip. Additionally, recent updates include Decoding Press Functionality for support of KV cache compression during the decoding phase, AIME25 & Math500 Benchmarks for new evaluation datasets for mathematical reasoning tasks, and post_init_from_model Hook for model-specific initialization support in BasePress.\n\nThe project is maintained on GitHub at NVIDIA/kvpress and provides both the implementation and evaluation tools for KV cache compression methods."
    ],
    "durationSeconds": 9.188395163999997
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Good, I have initial results. Let me now fetch more detailed information about kvpress (README, supported models) and R-KV (repo details). I also need to search specifically for SkipKV and FASA, and H2O.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "78ff5047-2bfb-4380-bae1-7a6738312410",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWcQWuUoYkqcBRirtGQxTh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 25779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1455
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 19_

找到了主要信息。现在深入获取 kvpress README、R-KV repo 详情，并补充搜索 SkipKV、FASA、H2O。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "060b42bd-2c8d-4ce4-8ad2-4d9901bd4bad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWcQWuUoYkqcBRirtGQxTh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 25779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1455
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YR74hHAzysv3CbXtkx7z24`</summary>

```json
{
  "url": "https://github.com/NVIDIA/kvpress/blob/main/README.md",
  "prompt": "Extract: 1) Full list of supported press/compression methods with their class names. 2) Supported model architectures (especially check for Qwen2). 3) Installation instructions. 4) API usage example. 5) Dependencies and Python/PyTorch version requirements. 6) Any benchmark results or evaluation methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "9df98259-5734-4d81-b4ca-6e92d4b2e819",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWcQWuUoYkqcBRirtGQxTh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 25779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1455
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GeAN3ZTcMUUakbR742MC43`</summary>

```json
{
  "url": "https://github.com/Zefan-Cai/R-KV",
  "prompt": "Extract: 1) Supported models (especially DeepSeek-R1-Distill-Qwen-14B or Qwen2 models). 2) Installation instructions and dependencies. 3) Key API/interface for running eviction. 4) Evaluation benchmarks and how to run them. 5) Complexity analysis (O(B²) pairwise scoring mentioned?). 6) Code structure overview."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "8f5760f5-22c3-4be2-bbe7-a290fa0311f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWcQWuUoYkqcBRirtGQxTh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 25779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1455
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N6dtQvyirCJSbp6WT3RZCY`</summary>

```json
{
  "query": "SkipKV \"KV cache\" reasoning model GitHub code 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "e12b08a6-3f51-48b1-b119-3ff3c742a0fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWcQWuUoYkqcBRirtGQxTh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 25779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1455
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G8ZNyNrtoyBEKgZBKE2Bjw`</summary>

```json
{
  "query": "FASA \"KV cache\" eviction reasoning LLM paper code GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "b1b9b41b-4ae9-4f7f-bbd5-cedfc6e27514",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWcQWuUoYkqcBRirtGQxTh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 25779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1455
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HAw75hsrfv795Y3PhZpVF8`</summary>

```json
{
  "query": "H2O \"Heavy Hitter Oracle\" KV cache eviction GitHub implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "9d6a7222-67a1-41f3-97ca-632346d560de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWcQWuUoYkqcBRirtGQxTh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 25779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1455
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-12T14:21:42.962Z_

<details><summary>↩ Tool result · `toolu_01N6dtQvyirCJSbp6WT3RZCY`</summary>

```text
Web search results for query: "SkipKV "KV cache" reasoning model GitHub code 2025"

Links: [{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"GitHub - MaxBelitsky/cache-steering: KV Cache Steering for Inducing Reasoning in Small Language Models · GitHub","url":"https://github.com/MaxBelitsky/cache-steering"},{"title":"Improving Model Representation and Reducing KV Cache via Skip Connections with First Value Heads","url":"https://arxiv.org/html/2510.16807"},{"title":"GitHub - FYYFU/HeadKV: [ICLR2025] Code and data for paper: Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning","url":"https://github.com/fyyfu/headkv"},{"title":"Beyond Speedup - Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/html/2601.20326"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/treeai-lab/awesome-kv-cache-management"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"kv-cache · GitHub Topics · GitHub","url":"https://github.com/topics/kv-cache"},{"title":"GitHub - jjiantong/Awesome-KV-Cache-Optimization: [ACL 2026] Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization · GitHub","url":"https://github.com/jjiantong/Awesome-KV-Cache-Optimization"},{"title":"Understanding and Coding the KV Cache in LLMs from Scratch","url":"https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms"}]

Based on the search results, I didn't find a specific project called "SkipKV" in the results. However, I found several related projects from 2025 involving KV cache optimization for reasoning models:

1. **SkipV1Former** - Available at https://github.com/Zhoutong-Wu/SkipV1Former. SkipV1Former mitigates information loss by explicitly routing the first layer's Value into every deeper layer, which allows the model to restore much of the information lost through copying and preserves more of the causal structure between samples and labels, enhancing the model's reasoning capabilities.

2. **R-KV** - An NeurIPS 2025 paper on Redundancy-aware KV Cache Compression for Reasoning Models. R-KV solves cache bloat in reasoning models by ranking tokens on-the-fly for both importance and non-redundancy, retaining only the informative, diverse ones.

3. **HeadKV** - An ICLR2025 paper presenting code and data for a Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning.

If you're looking specifically for "SkipKV," you might want to search with different terms or check if it's a recent project not yet widely indexed. The SkipV1Former project appears to be the closest match with "Skip" in the name and KV cache optimization focus.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "5c401c08-d579-4fb6-9b3e-9505851b8f26",
  "tool_use_result": {
    "query": "SkipKV \"KV cache\" reasoning model GitHub code 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XXjM1ShUyom2NrnPU8ua44",
        "content": [
          {
            "title": "GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models",
            "url": "https://github.com/Zefan-Cai/R-KV"
          },
          {
            "title": "GitHub - MaxBelitsky/cache-steering: KV Cache Steering for Inducing Reasoning in Small Language Models · GitHub",
            "url": "https://github.com/MaxBelitsky/cache-steering"
          },
          {
            "title": "Improving Model Representation and Reducing KV Cache via Skip Connections with First Value Heads",
            "url": "https://arxiv.org/html/2510.16807"
          },
          {
            "title": "GitHub - FYYFU/HeadKV: [ICLR2025] Code and data for paper: Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning",
            "url": "https://github.com/fyyfu/headkv"
          },
          {
            "title": "Beyond Speedup - Utilizing KV Cache for Sampling and Reasoning",
            "url": "https://arxiv.org/html/2601.20326"
          },
          {
            "title": "GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub",
            "url": "https://github.com/treeai-lab/awesome-kv-cache-management"
          },
          {
            "title": "GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).",
            "url": "https://github.com/October2001/Awesome-KV-Cache-Compression"
          },
          {
            "title": "kv-cache · GitHub Topics · GitHub",
            "url": "https://github.com/topics/kv-cache"
          },
          {
            "title": "GitHub - jjiantong/Awesome-KV-Cache-Optimization: [ACL 2026] Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization · GitHub",
            "url": "https://github.com/jjiantong/Awesome-KV-Cache-Optimization"
          },
          {
            "title": "Understanding and Coding the KV Cache in LLMs from Scratch",
            "url": "https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms"
          }
        ]
      },
      "Based on the search results, I didn't find a specific project called \"SkipKV\" in the results. However, I found several related projects from 2025 involving KV cache optimization for reasoning models:\n\n1. **SkipV1Former** - Available at https://github.com/Zhoutong-Wu/SkipV1Former. SkipV1Former mitigates information loss by explicitly routing the first layer's Value into every deeper layer, which allows the model to restore much of the information lost through copying and preserves more of the causal structure between samples and labels, enhancing the model's reasoning capabilities.\n\n2. **R-KV** - An NeurIPS 2025 paper on Redundancy-aware KV Cache Compression for Reasoning Models. R-KV solves cache bloat in reasoning models by ranking tokens on-the-fly for both importance and non-redundancy, retaining only the informative, diverse ones.\n\n3. **HeadKV** - An ICLR2025 paper presenting code and data for a Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning.\n\nIf you're looking specifically for \"SkipKV,\" you might want to search with different terms or check if it's a recent project not yet widely indexed. The SkipV1Former project appears to be the closest match with \"Skip\" in the name and KV cache optimization focus."
    ],
    "durationSeconds": 7.171647764000001
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T14:21:43.145Z_

<details><summary>↩ Tool result · `toolu_01GeAN3ZTcMUUakbR742MC43`</summary>

````text
# R-KV: KV Cache Compression Summary

## 1) Supported Models
The project explicitly benchmarks two DeepSeek-R1 variants:
- **DeepSeek-R1-Distill-Llama-8B**
- **DeepSeek-R1-Distill-Qwen-14B** (matching your Qwen interest)

The documentation notes it's designed as a "plug-and-play" wrapper for autoregressive LLMs generally, suggesting broader compatibility potential.

## 2) Installation & Dependencies
Basic setup requires:
```bash
pip install -r requirements.txt
pip install -e .  # Build the rkv package
```

For accelerated attention, Flash Attention is recommended for Hugging Face models. Evaluation separately requires building `evaluation/latex2sympy` dependencies.

## 3) Core API for Running Eviction
Primary command structure:
```bash
python3 ./run_math.py \
--dataset_path ./data/aime24.jsonl \
--model_path deepseek-ai/DeepSeek-R1-Distill-Llama-8B \
--method rkv \
--kv_budget 128
```

Key hyperparameters include buffer size (128), observation tokens (8), and importance/redundancy tradeoff (λ=0.1).

## 4) Evaluation Benchmarks
Two primary benchmarks tested:
- **MATH-500**: Average 2,979 tokens/solution
- **AIME 2024**: Average 15,536 tokens/solution

Run evaluations via: `bash examples/eval.sh`, with results saved to outputs directory.

## 5) Complexity Analysis
Documented operations include:
- "Importance scoring: **O(α × B_budget)**"
- "Redundancy scoring: **O(B_budget²)**"
- Attention scales with compressed cache size, creating favorable efficiency gains for longer sequences

## 6) Code Structure
Repository organized into framework-specific implementations:
- `/HuggingFace` - Main integration
- `/vLLM`, `/SGLang`, `/FlashInfer` - Alternative backends
- `/rkv` - Core compression logic
- `/evaluation` - Benchmark tools
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "2896dd56-ea1b-42a3-9c3d-c8a47a9c3264",
  "tool_use_result": {
    "bytes": 388864,
    "code": 200,
    "codeText": "OK",
    "result": "# R-KV: KV Cache Compression Summary\n\n## 1) Supported Models\nThe project explicitly benchmarks two DeepSeek-R1 variants:\n- **DeepSeek-R1-Distill-Llama-8B**\n- **DeepSeek-R1-Distill-Qwen-14B** (matching your Qwen interest)\n\nThe documentation notes it's designed as a \"plug-and-play\" wrapper for autoregressive LLMs generally, suggesting broader compatibility potential.\n\n## 2) Installation & Dependencies\nBasic setup requires:\n```bash\npip install -r requirements.txt\npip install -e .  # Build the rkv package\n```\n\nFor accelerated attention, Flash Attention is recommended for Hugging Face models. Evaluation separately requires building `evaluation/latex2sympy` dependencies.\n\n## 3) Core API for Running Eviction\nPrimary command structure:\n```bash\npython3 ./run_math.py \\\n--dataset_path ./data/aime24.jsonl \\\n--model_path deepseek-ai/DeepSeek-R1-Distill-Llama-8B \\\n--method rkv \\\n--kv_budget 128\n```\n\nKey hyperparameters include buffer size (128), observation tokens (8), and importance/redundancy tradeoff (λ=0.1).\n\n## 4) Evaluation Benchmarks\nTwo primary benchmarks tested:\n- **MATH-500**: Average 2,979 tokens/solution\n- **AIME 2024**: Average 15,536 tokens/solution\n\nRun evaluations via: `bash examples/eval.sh`, with results saved to outputs directory.\n\n## 5) Complexity Analysis\nDocumented operations include:\n- \"Importance scoring: **O(α × B_budget)**\"\n- \"Redundancy scoring: **O(B_budget²)**\"\n- Attention scales with compressed cache size, creating favorable efficiency gains for longer sequences\n\n## 6) Code Structure\nRepository organized into framework-specific implementations:\n- `/HuggingFace` - Main integration\n- `/vLLM`, `/SGLang`, `/FlashInfer` - Alternative backends\n- `/rkv` - Core compression logic\n- `/evaluation` - Benchmark tools",
    "durationMs": 7820,
    "url": "https://github.com/Zefan-Cai/R-KV"
  }
}
````

</details>

---

### Tool result

_source line 27 · 2026-05-12T14:21:44.167Z_

<details><summary>↩ Tool result · `toolu_01HAw75hsrfv795Y3PhZpVF8`</summary>

```text
Web search results for query: "H2O "Heavy Hitter Oracle" KV cache eviction GitHub implementation"

Links: [{"title":"[2306.14048] H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/abs/2306.14048"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://github.com/vllm-project/vllm/issues/3532"},{"title":"GitHub - lenscloth/KVCache: [NeurIPS'23] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models. · GitHub","url":"https://github.com/lenscloth/KVCache"},{"title":"Paper page - H_2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://huggingface.co/papers/2306.14048"},{"title":"H 2 O: heavy-hitter oracle for efficient generative inference ...","url":"https://dl.acm.org/doi/10.5555/3666122.3667628"},{"title":"GitHub - FMInference/H2O: [NeurIPS'23] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models.","url":"https://github.com/FMInference/H2O"},{"title":"Add support for H2O cache eviction with LLaMA by justincharney · Pull Request #35381 · huggingface/transformers","url":"https://github.com/huggingface/transformers/pull/35381"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/6ceefa7b15572587b78ecfcebb2827f8-Paper-Conference.pdf"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=RkRrPp7GKO"},{"title":"[PDF] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/H2O:-Heavy-Hitter-Oracle-for-Efficient-Generative-Zhang-Sheng/e586a4591ba0303b769f2c07cbddaf1899cb72e4"}]

Based on the search results, here's what I found about H2O "Heavy Hitter Oracle" KV cache eviction implementation:

## Overview

Heavy Hitter Oracle (H₂O) is a KV cache eviction policy that dynamically retains a balance of recent and H₂ tokens. The approach is based on the observation that a small portion of tokens contributes most of the value when computing attention scores, and these tokens are called Heavy Hitters (H₂).

## Key Technical Aspects

The KV cache eviction is formulated as a dynamic submodular problem with a theoretical guarantee for the novel eviction algorithm.

## GitHub Implementations

There are several GitHub repositories with H2O implementations:

1. **Official Implementation**: FMInference/H2O on GitHub contains the code for the NeurIPS'23 paper

2. **Alternative Implementation**: lenscloth/KVCache is another GitHub repository with the H2O implementation

3. **Hugging Face Integration**: H2O cache eviction strategy was implemented in Hugging Face transformers, which selectively retains a balance of KV pairs that are recent or contribute most to the cumulative attention scores while evicting less important ones to maintain a fixed cache size

## Performance Results

The H2O implementation with 20% heavy hitters improves the throughput over three leading inference systems (DeepSpeed Zero-Inference, Hugging Face Accelerate, and FlexGen) by up to 29×, 29×, and 3× on OPT-6.7B and OPT-30B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "a1b10ad3-8cd4-497c-9ed0-cfac413f9bcc",
  "tool_use_result": {
    "query": "H2O \"Heavy Hitter Oracle\" KV cache eviction GitHub implementation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PqnyRkoNhfJEf4RHoFprti",
        "content": [
          {
            "title": "[2306.14048] H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models",
            "url": "https://arxiv.org/abs/2306.14048"
          },
          {
            "title": "H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...",
            "url": "https://github.com/vllm-project/vllm/issues/3532"
          },
          {
            "title": "GitHub - lenscloth/KVCache: [NeurIPS'23] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models. · GitHub",
            "url": "https://github.com/lenscloth/KVCache"
          },
          {
            "title": "Paper page - H_2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models",
            "url": "https://huggingface.co/papers/2306.14048"
          },
          {
            "title": "H 2 O: heavy-hitter oracle for efficient generative inference ...",
            "url": "https://dl.acm.org/doi/10.5555/3666122.3667628"
          },
          {
            "title": "GitHub - FMInference/H2O: [NeurIPS'23] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models.",
            "url": "https://github.com/FMInference/H2O"
          },
          {
            "title": "Add support for H2O cache eviction with LLaMA by justincharney · Pull Request #35381 · huggingface/transformers",
            "url": "https://github.com/huggingface/transformers/pull/35381"
          },
          {
            "title": "H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/6ceefa7b15572587b78ecfcebb2827f8-Paper-Conference.pdf"
          },
          {
            "title": "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=RkRrPp7GKO"
          },
          {
            "title": "[PDF] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/H2O:-Heavy-Hitter-Oracle-for-Efficient-Generative-Zhang-Sheng/e586a4591ba0303b769f2c07cbddaf1899cb72e4"
          }
        ]
      },
      "Based on the search results, here's what I found about H2O \"Heavy Hitter Oracle\" KV cache eviction implementation:\n\n## Overview\n\nHeavy Hitter Oracle (H₂O) is a KV cache eviction policy that dynamically retains a balance of recent and H₂ tokens. The approach is based on the observation that a small portion of tokens contributes most of the value when computing attention scores, and these tokens are called Heavy Hitters (H₂).\n\n## Key Technical Aspects\n\nThe KV cache eviction is formulated as a dynamic submodular problem with a theoretical guarantee for the novel eviction algorithm.\n\n## GitHub Implementations\n\nThere are several GitHub repositories with H2O implementations:\n\n1. **Official Implementation**: FMInference/H2O on GitHub contains the code for the NeurIPS'23 paper\n\n2. **Alternative Implementation**: lenscloth/KVCache is another GitHub repository with the H2O implementation\n\n3. **Hugging Face Integration**: H2O cache eviction strategy was implemented in Hugging Face transformers, which selectively retains a balance of KV pairs that are recent or contribute most to the cumulative attention scores while evicting less important ones to maintain a fixed cache size\n\n## Performance Results\n\nThe H2O implementation with 20% heavy hitters improves the throughput over three leading inference systems (DeepSpeed Zero-Inference, Hugging Face Accelerate, and FlexGen) by up to 29×, 29×, and 3× on OPT-6.7B and OPT-30B."
    ],
    "durationSeconds": 7.443454984999996
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T14:21:45.506Z_

<details><summary>↩ Tool result · `toolu_01YR74hHAzysv3CbXtkx7z24`</summary>

````text
# KVPress Summary

## 1. Supported Compression Methods

KVPress includes 30+ compression methods (presses). Key examples include:

- **Scorer-based**: `RandomPress`, `KnormPress`, `SnapKVPress`, `ExpectedAttentionPress`, `StreamingLLMPress`, `TOVAPress`
- **Specialized**: `ThinKPress`, `SimLayerKVPress`, `DuoAttentionPress`, `FinchPress`, `KVzipPress`
- **Wrappers**: `AdaKVPress`, `ComposedPress`, `DecodingPress`, `PrefillDecodingPress`

Complete list available in the README under "Available presses."

## 2. Supported Model Architectures

The documentation explicitly states: "Some presses depend on the model architecture...We tested support for `LlamaForCausalLM`, `MistralForCausalLM`, `Phi3ForCausalLM`, `Qwen2ForCausalLM`, `Qwen3ForCausalLM`, and `Gemma3ForCausalLM`" with the note that many other models may work due to similar implementations.

**Qwen2 is confirmed as supported.**

## 3. Installation

Standard installation: `pip install kvpress`

Development setup requires `uv`:
```bash
git clone https://github.com/NVIDIA/kvpress.git
cd kvpress
uv sync --extra eval --extra flash-attn
```

## 4. API Usage Example

```python
from transformers import pipeline
from kvpress import ExpectedAttentionPress

pipe = pipeline("kv-press-text-generation", model="Qwen/Qwen3-8B")
press = ExpectedAttentionPress(compression_ratio=0.5)
answer = pipe(context, question=question, press=press)["answer"]
```

## 5. Dependencies & Version Requirements

No explicit Python or PyTorch version requirements are stated in this README. Optional dependencies include `optimum-quanto` for quantization and `flash-attention-2`.

## 6. Evaluation & Benchmarks

The README references "Hugging Face Leaderboard" for RULER dataset results (4k context length) but doesn't include actual benchmark numbers in this document. Users can access detailed evaluation via the project's CLI tools and dedicated notebooks like `speed_and_memory.ipynb`.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "95db123c-4019-481c-a33b-694946dfc3e2",
  "tool_use_result": {
    "bytes": 390304,
    "code": 200,
    "codeText": "OK",
    "result": "# KVPress Summary\n\n## 1. Supported Compression Methods\n\nKVPress includes 30+ compression methods (presses). Key examples include:\n\n- **Scorer-based**: `RandomPress`, `KnormPress`, `SnapKVPress`, `ExpectedAttentionPress`, `StreamingLLMPress`, `TOVAPress`\n- **Specialized**: `ThinKPress`, `SimLayerKVPress`, `DuoAttentionPress`, `FinchPress`, `KVzipPress`\n- **Wrappers**: `AdaKVPress`, `ComposedPress`, `DecodingPress`, `PrefillDecodingPress`\n\nComplete list available in the README under \"Available presses.\"\n\n## 2. Supported Model Architectures\n\nThe documentation explicitly states: \"Some presses depend on the model architecture...We tested support for `LlamaForCausalLM`, `MistralForCausalLM`, `Phi3ForCausalLM`, `Qwen2ForCausalLM`, `Qwen3ForCausalLM`, and `Gemma3ForCausalLM`\" with the note that many other models may work due to similar implementations.\n\n**Qwen2 is confirmed as supported.**\n\n## 3. Installation\n\nStandard installation: `pip install kvpress`\n\nDevelopment setup requires `uv`:\n```bash\ngit clone https://github.com/NVIDIA/kvpress.git\ncd kvpress\nuv sync --extra eval --extra flash-attn\n```\n\n## 4. API Usage Example\n\n```python\nfrom transformers import pipeline\nfrom kvpress import ExpectedAttentionPress\n\npipe = pipeline(\"kv-press-text-generation\", model=\"Qwen/Qwen3-8B\")\npress = ExpectedAttentionPress(compression_ratio=0.5)\nanswer = pipe(context, question=question, press=press)[\"answer\"]\n```\n\n## 5. Dependencies & Version Requirements\n\nNo explicit Python or PyTorch version requirements are stated in this README. Optional dependencies include `optimum-quanto` for quantization and `flash-attention-2`.\n\n## 6. Evaluation & Benchmarks\n\nThe README references \"Hugging Face Leaderboard\" for RULER dataset results (4k context length) but doesn't include actual benchmark numbers in this document. Users can access detailed evaluation via the project's CLI tools and dedicated notebooks like `speed_and_memory.ipynb`.",
    "durationMs": 13059,
    "url": "https://github.com/NVIDIA/kvpress/blob/main/README.md"
  }
}
````

</details>

---

### Tool result

_source line 29 · 2026-05-12T14:21:47.131Z_

<details><summary>↩ Tool result · `toolu_01G8ZNyNrtoyBEKgZBKE2Bjw`</summary>

```text
Web search results for query: "FASA "KV cache" eviction reasoning LLM paper code GitHub"

Links: [{"title":"GitHub - Zefan-Cai/Awesome-LLM-KV-Cache: Awesome-LLM-KV-Cache: A curated list of 📙Awesome LLM KV Cache Papers with Codes.","url":"https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache"},{"title":"GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub","url":"https://github.com/FFY0/AdaKV"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"},{"title":"GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub","url":"https://github.com/FFY0/DefensiveKV"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://janghyun1230.github.io/paper/fastkvzip26.pdf"},{"title":"[2605.07234] Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/abs/2605.07234"},{"title":"GitHub - Janghyun1230/FastKVzip: Accurate and fast KV cache compression with a gating mechanism · GitHub","url":"https://github.com/Janghyun1230/FastKVzip"},{"title":"NACL: A General and Effective KV Cache Eviction Framework for LLM at Inference Time - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.428/"},{"title":"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=nJgS06sX3O"}]

I didn't find a specific paper or project called "FASA" in these results. The search returned results for other prominent KV cache eviction methods and papers (like Ada-KV, DefensiveKV, LaProx, Fast KVzip, and NACL), but not specifically for "FASA."

Let me try a more targeted search for FASA:

Links: [{"title":"GitHub - MaxBelitsky/cache-steering: KV Cache Steering for Inducing Reasoning in Small Language Models · GitHub","url":"https://github.com/MaxBelitsky/cache-steering"},{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"GitHub - FYYFU/HeadKV: [ICLR2025] Code and data for paper: Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning","url":"https://github.com/fyyfu/headkv"},{"title":"GitHub - Zefan-Cai/KVCache-Factory: Unified KV Cache Compression Methods for Auto-Regressive Models · GitHub","url":"https://github.com/Zefan-Cai/KVCache-Factory"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://zefan-cai.github.io/R-KV.page/"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"},{"title":"FASA: FREQUENCY-AWARE SPARSE ATTENTION | OpenReview","url":"https://openreview.net/forum?id=FnSgecCEwg"},{"title":"The State of FP8 KV-Cache and Attention Quantization in vLLM | vLLM Blog","url":"https://vllm-project.github.io/2026/04/22/fp8-kvcache.html"},{"title":"GitHub - fsaporito/KVCache: C++ Implementation of a Key-Value cache · GitHub","url":"https://github.com/fsaporito/KVCache"},{"title":"GitHub - WeianMao/triattention: TriAttention — Efficient long reasoning with trigonometric KV cache compression. Enables OpenClaw local deployment on memory-constrained GPUs.","url":"https://github.com/WeianMao/triattention"}]

Perfect! I found FASA. Here are the search results:

## FASA - Frequency-Aware Sparse Attention

FASA is a novel framework that achieves query-aware token eviction by dynamically predicting token importance. 

FASA stems from a novel insight into RoPE: the discovery of functional sparsity at the frequency-chunk (FC) level, where a small, identifiable subset of "dominant" FCs consistently exhibits high contextual agreement with the full attention head.

### Key Features

FASA first identifies a critical set of tokens using dominant FCs, and then performs focused attention computation solely on this pruned subset.

### Performance

Across a spectrum of long-context tasks, from sequence modeling to complex CoT reasoning, FASA consistently outperforms all token-eviction baselines and achieves near-oracle accuracy, demonstrating remarkable robustness even under constraint budgets.

On LongBench-V1, FASA reaches nearly 100% of full-KV performance when only keeping 256 tokens, and achieves 2.56× speedup using just 18.9% of the cache on AIME24.

The paper for FASA was found on OpenReview, but I didn't locate a dedicated GitHub repository for the code in these search results. You may want to check the OpenReview page directly or search for the authors' affiliated institutions for code availability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "dd5b4458-ac5d-4585-adf1-cb1261d5c575",
  "tool_use_result": {
    "query": "FASA \"KV cache\" eviction reasoning LLM paper code GitHub",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BkHLJBd9XAzTxo1936CqPE",
        "content": [
          {
            "title": "GitHub - Zefan-Cai/Awesome-LLM-KV-Cache: Awesome-LLM-KV-Cache: A curated list of 📙Awesome LLM KV Cache Papers with Codes.",
            "url": "https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache"
          },
          {
            "title": "GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub",
            "url": "https://github.com/FFY0/AdaKV"
          },
          {
            "title": "GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub",
            "url": "https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"
          },
          {
            "title": "GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub",
            "url": "https://github.com/FFY0/DefensiveKV"
          },
          {
            "title": "Taming the Fragility of KV Cache Eviction in LLM Inference",
            "url": "https://arxiv.org/html/2510.13334v1"
          },
          {
            "title": "Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction",
            "url": "https://janghyun1230.github.io/paper/fastkvzip26.pdf"
          },
          {
            "title": "[2605.07234] Reformulating KV Cache Eviction Problem for Long-Context LLM Inference",
            "url": "https://arxiv.org/abs/2605.07234"
          },
          {
            "title": "GitHub - Janghyun1230/FastKVzip: Accurate and fast KV cache compression with a gating mechanism · GitHub",
            "url": "https://github.com/Janghyun1230/FastKVzip"
          },
          {
            "title": "NACL: A General and Effective KV Cache Eviction Framework for LLM at Inference Time - ACL Anthology",
            "url": "https://aclanthology.org/2024.acl-long.428/"
          },
          {
            "title": "DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview",
            "url": "https://openreview.net/forum?id=nJgS06sX3O"
          }
        ]
      },
      "I didn't find a specific paper or project called \"FASA\" in these results. The search returned results for other prominent KV cache eviction methods and papers (like Ada-KV, DefensiveKV, LaProx, Fast KVzip, and NACL), but not specifically for \"FASA.\"\n\nLet me try a more targeted search for FASA:",
      {
        "tool_use_id": "srvtoolu_014744xe3G3MJUUN21eL6n3g",
        "content": [
          {
            "title": "GitHub - MaxBelitsky/cache-steering: KV Cache Steering for Inducing Reasoning in Small Language Models · GitHub",
            "url": "https://github.com/MaxBelitsky/cache-steering"
          },
          {
            "title": "GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models",
            "url": "https://github.com/Zefan-Cai/R-KV"
          },
          {
            "title": "GitHub - FYYFU/HeadKV: [ICLR2025] Code and data for paper: Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning",
            "url": "https://github.com/fyyfu/headkv"
          },
          {
            "title": "GitHub - Zefan-Cai/KVCache-Factory: Unified KV Cache Compression Methods for Auto-Regressive Models · GitHub",
            "url": "https://github.com/Zefan-Cai/KVCache-Factory"
          },
          {
            "title": "R-KV: Redundancy-aware KV Cache Compression for Reasoning Models",
            "url": "https://zefan-cai.github.io/R-KV.page/"
          },
          {
            "title": "GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub",
            "url": "https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"
          },
          {
            "title": "FASA: FREQUENCY-AWARE SPARSE ATTENTION | OpenReview",
            "url": "https://openreview.net/forum?id=FnSgecCEwg"
          },
          {
            "title": "The State of FP8 KV-Cache and Attention Quantization in vLLM | vLLM Blog",
            "url": "https://vllm-project.github.io/2026/04/22/fp8-kvcache.html"
          },
          {
            "title": "GitHub - fsaporito/KVCache: C++ Implementation of a Key-Value cache · GitHub",
            "url": "https://github.com/fsaporito/KVCache"
          },
          {
            "title": "GitHub - WeianMao/triattention: TriAttention — Efficient long reasoning with trigonometric KV cache compression. Enables OpenClaw local deployment on memory-constrained GPUs.",
            "url": "https://github.com/WeianMao/triattention"
          }
        ]
      },
      "Perfect! I found FASA. Here are the search results:\n\n## FASA - Frequency-Aware Sparse Attention\n\nFASA is a novel framework that achieves query-aware token eviction by dynamically predicting token importance. \n\nFASA stems from a novel insight into RoPE: the discovery of functional sparsity at the frequency-chunk (FC) level, where a small, identifiable subset of \"dominant\" FCs consistently exhibits high contextual agreement with the full attention head.\n\n### Key Features\n\nFASA first identifies a critical set of tokens using dominant FCs, and then performs focused attention computation solely on this pruned subset.\n\n### Performance\n\nAcross a spectrum of long-context tasks, from sequence modeling to complex CoT reasoning, FASA consistently outperforms all token-eviction baselines and achieves near-oracle accuracy, demonstrating remarkable robustness even under constraint budgets.\n\nOn LongBench-V1, FASA reaches nearly 100% of full-KV performance when only keeping 256 tokens, and achieves 2.56× speedup using just 18.9% of the cache on AIME24.\n\nThe paper for FASA was found on OpenReview, but I didn't locate a dedicated GitHub repository for the code in these search results. You may want to check the OpenReview page directly or search for the authors' affiliated institutions for code availability."
    ],
    "durationSeconds": 10.678076680999999
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Good, I have comprehensive information now. Let me also search for a few more things:
1. FASA GitHub code specifically
2. SnapKV as another baseline
3. TOVA
4. StreamingLLM

Let me also check the Awesome-KV-Cache-Management list for a comprehensive view and get more details on FASA code availability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "12e167b6-7d03-4381-af01-84e3cb172f46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Vz5Z3PrWpHek4ev1q8JdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 6440,
      "cache_read_input_tokens": 27234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6440
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 31_

补充搜索 FASA 代码可用性和其他重要 baseline（SnapKV、TOVA、StreamingLLM）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "a480cdf3-4e89-452a-843f-d492931f126e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Vz5Z3PrWpHek4ev1q8JdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 6440,
      "cache_read_input_tokens": 27234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6440
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WX8LW7pP89jMSzUPriULiQ`</summary>

```json
{
  "query": "FASA frequency-aware sparse attention GitHub code release 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "4aac9d88-6583-45e1-990c-47974795b0cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Vz5Z3PrWpHek4ev1q8JdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 6440,
      "cache_read_input_tokens": 27234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6440
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GtCDKtSkv9J8wEpHRPL8Bo`</summary>

```json
{
  "query": "SnapKV KV cache compression GitHub observation window 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "e16fb258-dacc-4c03-abc0-ee926497cfd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Vz5Z3PrWpHek4ev1q8JdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 6440,
      "cache_read_input_tokens": 27234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6440
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H37xTHRwUCmJk7dybbPeNm`</summary>

```json
{
  "query": "TOVA \"Token Omission Via Attention\" KV cache GitHub 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "0193ef34-3680-41d1-8f71-3e60962f40b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Vz5Z3PrWpHek4ev1q8JdA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 6440,
      "cache_read_input_tokens": 27234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6440
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-12T14:21:59.809Z_

<details><summary>↩ Tool result · `toolu_01WX8LW7pP89jMSzUPriULiQ`</summary>

```text
Web search results for query: "FASA frequency-aware sparse attention GitHub code release 2025 2026"

Links: [{"title":"FASA: Frequency-Aware Sparse Attention","url":"https://arxiv.org/html/2602.03152v3"},{"title":"FASA: FREQUENCY-AWARE SPARSE ATTENTION | OpenReview","url":"https://openreview.net/forum?id=FnSgecCEwg"},{"title":"[2602.03152] FASA: Frequency-aware Sparse Attention","url":"https://arxiv.org/abs/2602.03152"},{"title":"GitHub - YannX1e/Sparse-Feature-Attention: Official implement of ICLR 2026 paper \"Scaling Attention via Feature Sparsity\". · GitHub","url":"https://github.com/YannX1e/Sparse-Feature-Attention"},{"title":"FASA: FREQUENCY-AWARE SPARSE ATTENTION","url":"https://cseweb.ucsd.edu/~jmcauley/reviews/iclr26b.pdf"},{"title":"FASA: FREQUENCY-AWARE SPARSE ATTENTION","url":"https://openreview.net/pdf/e516811d3a5d1c254a1bae73cc3d10457f24aa9c.pdf"},{"title":"Paper page - FASA: Frequency-aware Sparse Attention","url":"https://huggingface.co/papers/2602.03152"},{"title":"FASA: Frequency-aware Sparse Attention | alphaXiv","url":"https://www.alphaxiv.org/abs/2602.03152"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=FnSgecCEwg"},{"title":"GitHub - thu-ml/SpargeAttn: [ICML2025] SpargeAttention: A training-free sparse attention that accelerates any model inference. · GitHub","url":"https://github.com/thu-ml/SpargeAttn"}]

Based on the search results, here's what I found about FASA (Frequency-Aware Sparse Attention):

## Overview
FASA is a novel framework that achieves query-aware token eviction by dynamically predicting token importance. FASA stems from a novel insight into RoPE: the discovery of functional sparsity at the frequency-chunk (FC) level.

## GitHub Code Release
Code is available at https://github.com/AMAP-ML/FASA-ICLR2026.

## Key Innovation
A small, identifiable subset of "dominant" FCs consistently exhibits high contextual agreement with the full attention head. FASA first identifies a critical set of tokens using dominant FCs, and then performs focused attention computation solely on this pruned subset.

## Performance Results
On LongBench-V1, FASA reaches nearly 100% of full-KV performance when only keeping 256 tokens, and achieves 2.56× speedup using just 18.9% of the cache on AIME24.

## Publication Timeline
The research appears to have been submitted around February 2026 for ICLR 2026 (the International Conference on Learning Representations), with the paper available on arXiv as of February 28, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "eeaea192-53cc-46c0-9407-2dcd45e7d6cf",
  "tool_use_result": {
    "query": "FASA frequency-aware sparse attention GitHub code release 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014PtV2Tpk8wFs1DaekbF4ku",
        "content": [
          {
            "title": "FASA: Frequency-Aware Sparse Attention",
            "url": "https://arxiv.org/html/2602.03152v3"
          },
          {
            "title": "FASA: FREQUENCY-AWARE SPARSE ATTENTION | OpenReview",
            "url": "https://openreview.net/forum?id=FnSgecCEwg"
          },
          {
            "title": "[2602.03152] FASA: Frequency-aware Sparse Attention",
            "url": "https://arxiv.org/abs/2602.03152"
          },
          {
            "title": "GitHub - YannX1e/Sparse-Feature-Attention: Official implement of ICLR 2026 paper \"Scaling Attention via Feature Sparsity\". · GitHub",
            "url": "https://github.com/YannX1e/Sparse-Feature-Attention"
          },
          {
            "title": "FASA: FREQUENCY-AWARE SPARSE ATTENTION",
            "url": "https://cseweb.ucsd.edu/~jmcauley/reviews/iclr26b.pdf"
          },
          {
            "title": "FASA: FREQUENCY-AWARE SPARSE ATTENTION",
            "url": "https://openreview.net/pdf/e516811d3a5d1c254a1bae73cc3d10457f24aa9c.pdf"
          },
          {
            "title": "Paper page - FASA: Frequency-aware Sparse Attention",
            "url": "https://huggingface.co/papers/2602.03152"
          },
          {
            "title": "FASA: Frequency-aware Sparse Attention | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2602.03152"
          },
          {
            "title": "000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019",
            "url": "https://openreview.net/pdf?id=FnSgecCEwg"
          },
          {
            "title": "GitHub - thu-ml/SpargeAttn: [ICML2025] SpargeAttention: A training-free sparse attention that accelerates any model inference. · GitHub",
            "url": "https://github.com/thu-ml/SpargeAttn"
          }
        ]
      },
      "Based on the search results, here's what I found about FASA (Frequency-Aware Sparse Attention):\n\n## Overview\nFASA is a novel framework that achieves query-aware token eviction by dynamically predicting token importance. FASA stems from a novel insight into RoPE: the discovery of functional sparsity at the frequency-chunk (FC) level.\n\n## GitHub Code Release\nCode is available at https://github.com/AMAP-ML/FASA-ICLR2026.\n\n## Key Innovation\nA small, identifiable subset of \"dominant\" FCs consistently exhibits high contextual agreement with the full attention head. FASA first identifies a critical set of tokens using dominant FCs, and then performs focused attention computation solely on this pruned subset.\n\n## Performance Results\nOn LongBench-V1, FASA reaches nearly 100% of full-KV performance when only keeping 256 tokens, and achieves 2.56× speedup using just 18.9% of the cache on AIME24.\n\n## Publication Timeline\nThe research appears to have been submitted around February 2026 for ICLR 2026 (the International Conference on Learning Representations), with the paper available on arXiv as of February 28, 2026."
    ],
    "durationSeconds": 6.849724288000005
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-12T14:22:00.824Z_

<details><summary>↩ Tool result · `toolu_01GtCDKtSkv9J8wEpHRPL8Bo`</summary>

```text
Web search results for query: "SnapKV KV cache compression GitHub observation window 2024"

Links: [{"title":"SnapKV: LLM Knows What You Are Looking for before Generation Yuhong Li1∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/28ab418242603e0f7323e54185d19bde-Paper-Conference.pdf"},{"title":"Paper page - SnapKV: LLM Knows What You are Looking for Before Generation","url":"https://huggingface.co/papers/2404.14469"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation Yuhong Li1∗","url":"https://arxiv.org/pdf/2404.14469"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation | OpenReview","url":"https://openreview.net/forum?id=poE54GOq2l"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"SnapKV: Cache compression technique for faster LLM generation with less compute and memory | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/snapkv-cache-compression-technique-for-faster-llm-generation-with-less-compute-and-memory-516ac599c8ee"},{"title":"GitHub - Zefan-Cai/KVCache-Factory: Unified KV Cache Compression Methods for Auto-Regressive Models · GitHub","url":"https://github.com/Zefan-Cai/KVCache-Factory"},{"title":"SharedContextBench: Evaluating Long-Context Methods in KV Cache Reuse","url":"https://neurips2024-enlsp.github.io/papers/paper_93.pdf"},{"title":"SnapKV : LLM Knows What You are Looking for Before Generation","url":"https://arxiv.org/html/2404.14469v1"},{"title":"SnapKV | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738638"}]

Based on the search results, here's what I found about SnapKV, KV cache compression, and the observation window concept:

## SnapKV Overview

SnapKV reduces KV cache size and computational overhead in LLMs by compressing the cache based on observed attention patterns, improving decoding speed and memory efficiency without significant performance loss.

## The Observation Window

A key innovation in SnapKV is the observation window concept. Each attention head in the model consistently focuses on specific prompt attention features during generation, and this robust pattern can be obtained from an 'observation' window located at the end of the prompts.

The observation window is defined as the last segment of the prompt. The method uses this information to intelligently select which KV positions to keep in the compressed cache.

## Implementation Details

The prompt KV cache size can be configured (e.g., 1024 tokens), with a maximum pooling kernel size and observation window size that are hyperparameters that can be customized. One configuration uses max pooling with kernel size 7 and observation window size 32.

## Performance Results

SnapKV demonstrates potential to precisely manage small details on extremely long input contexts with a 380x compression ratio. SnapKV shows negligible performance drop compared with original implementations for 16 different datasets, even with prompt-KV with 1024 tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "8652d89a-5753-43dc-b639-d7c3059a4184",
  "tool_use_result": {
    "query": "SnapKV KV cache compression GitHub observation window 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XKJhsY3E97za8n6zUVNq3N",
        "content": [
          {
            "title": "SnapKV: LLM Knows What You Are Looking for before Generation Yuhong Li1∗",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/28ab418242603e0f7323e54185d19bde-Paper-Conference.pdf"
          },
          {
            "title": "Paper page - SnapKV: LLM Knows What You are Looking for Before Generation",
            "url": "https://huggingface.co/papers/2404.14469"
          },
          {
            "title": "SnapKV: LLM Knows What You are Looking for Before Generation Yuhong Li1∗",
            "url": "https://arxiv.org/pdf/2404.14469"
          },
          {
            "title": "SnapKV: LLM Knows What You are Looking for Before Generation | OpenReview",
            "url": "https://openreview.net/forum?id=poE54GOq2l"
          },
          {
            "title": "GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).",
            "url": "https://github.com/October2001/Awesome-KV-Cache-Compression"
          },
          {
            "title": "SnapKV: Cache compression technique for faster LLM generation with less compute and memory | by SACHIN KUMAR | Medium",
            "url": "https://medium.com/@techsachin/snapkv-cache-compression-technique-for-faster-llm-generation-with-less-compute-and-memory-516ac599c8ee"
          },
          {
            "title": "GitHub - Zefan-Cai/KVCache-Factory: Unified KV Cache Compression Methods for Auto-Regressive Models · GitHub",
            "url": "https://github.com/Zefan-Cai/KVCache-Factory"
          },
          {
            "title": "SharedContextBench: Evaluating Long-Context Methods in KV Cache Reuse",
            "url": "https://neurips2024-enlsp.github.io/papers/paper_93.pdf"
          },
          {
            "title": "SnapKV : LLM Knows What You are Looking for Before Generation",
            "url": "https://arxiv.org/html/2404.14469v1"
          },
          {
            "title": "SnapKV | Proceedings of the 38th International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3737916.3738638"
          }
        ]
      },
      "Based on the search results, here's what I found about SnapKV, KV cache compression, and the observation window concept:\n\n## SnapKV Overview\n\nSnapKV reduces KV cache size and computational overhead in LLMs by compressing the cache based on observed attention patterns, improving decoding speed and memory efficiency without significant performance loss.\n\n## The Observation Window\n\nA key innovation in SnapKV is the observation window concept. Each attention head in the model consistently focuses on specific prompt attention features during generation, and this robust pattern can be obtained from an 'observation' window located at the end of the prompts.\n\nThe observation window is defined as the last segment of the prompt. The method uses this information to intelligently select which KV positions to keep in the compressed cache.\n\n## Implementation Details\n\nThe prompt KV cache size can be configured (e.g., 1024 tokens), with a maximum pooling kernel size and observation window size that are hyperparameters that can be customized. One configuration uses max pooling with kernel size 7 and observation window size 32.\n\n## Performance Results\n\nSnapKV demonstrates potential to precisely manage small details on extremely long input contexts with a 380x compression ratio. SnapKV shows negligible performance drop compared with original implementations for 16 different datasets, even with prompt-KV with 1024 tokens."
    ],
    "durationSeconds": 7.330016732000003
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-12T14:22:00.968Z_

<details><summary>↩ Tool result · `toolu_01H37xTHRwUCmJk7dybbPeNm`</summary>

```text
Web search results for query: "TOVA "Token Omission Via Attention" KV cache GitHub 2024"

Links: [{"title":"GitHub - schwartz-lab-NLP/TOVA: Token Omission Via Attention · GitHub","url":"https://github.com/schwartz-lab-NLP/TOVA"},{"title":"CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based Token Eviction","url":"https://arxiv.org/html/2504.14051v6"},{"title":"How sparse attention is solving AI's memory bottleneck","url":"https://bdtechtalks.substack.com/p/how-sparse-attention-is-solving-ais"},{"title":"CAOTE: KV Caching through Attention Output Error based Token Eviction","url":"https://arxiv.org/html/2504.14051v1"},{"title":"CAOTE: KV Cache Eviction for LLMs via Attention Output Error-Based Token Selection","url":"https://arxiv.org/html/2504.14051v4"},{"title":"Learning What to Write: Write-Gated KV for Efficient Long-Context Inference","url":"https://arxiv.org/pdf/2512.17452"},{"title":"KVCompose: Efficient Structured KV Cache Compression with Composite Tokens","url":"https://arxiv.org/pdf/2509.05165"},{"title":"GitHub - Zefan-Cai/Awesome-LLM-KV-Cache: Awesome-LLM-KV-Cache: A curated list of 📙Awesome LLM KV Cache Papers with Codes.","url":"https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache"},{"title":"Keep the Cost Down: A Review on Methods to Optimize LLM’s KV Cache Consumption","url":"https://arxiv.org/html/2407.18003v4"},{"title":"CAOTE: KV Cache Eviction for LLMs via Attention Output Error-Based Token","url":"https://www.arxiv.org/pdf/2504.14051v4"}]

Based on the search results, here's what I found about TOVA (Token Omission Via Attention):

## Overview

Token Omission via Attention (TOVA) drops tokens based on attention values by looking at the current step and checking which tokens attention heads are focusing on.

## GitHub Repository

The official GitHub repository is located at https://github.com/schwartz-lab-NLP/TOVA, which provides implementation code and example usage for integrating TOVA with transformer models.

## Technical Details

TOVA proposes a simple greedy method to discard useless tokens. While keeping a fixed-length of KV-Cache, TOVA evicts at each decoding step the tokens with minimal attention weights layer-wise.

## Academic Context

TOVA is one of several token eviction methods (alongside H2O, SnapKV, and RoCO) that retain tokens with high attention scores in the KV cache with various algorithmic modifications. The paper "Transformers are Multi-State RNNs" by Oren et al., published in January 2024, introduced TOVA.

## Performance

TOVA has been evaluated against newer methods like CAOTE, with CAOTE-boosted approaches showing improvements over TOVA in some benchmarks, though TOVA still remains a competitive baseline for KV cache optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "f1d07b2c-322b-4446-a7dd-9a5ac2d7aa8c",
  "tool_use_result": {
    "query": "TOVA \"Token Omission Via Attention\" KV cache GitHub 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_017miVqYDRWqGay7qXbjX78j",
        "content": [
          {
            "title": "GitHub - schwartz-lab-NLP/TOVA: Token Omission Via Attention · GitHub",
            "url": "https://github.com/schwartz-lab-NLP/TOVA"
          },
          {
            "title": "CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based Token Eviction",
            "url": "https://arxiv.org/html/2504.14051v6"
          },
          {
            "title": "How sparse attention is solving AI's memory bottleneck",
            "url": "https://bdtechtalks.substack.com/p/how-sparse-attention-is-solving-ais"
          },
          {
            "title": "CAOTE: KV Caching through Attention Output Error based Token Eviction",
            "url": "https://arxiv.org/html/2504.14051v1"
          },
          {
            "title": "CAOTE: KV Cache Eviction for LLMs via Attention Output Error-Based Token Selection",
            "url": "https://arxiv.org/html/2504.14051v4"
          },
          {
            "title": "Learning What to Write: Write-Gated KV for Efficient Long-Context Inference",
            "url": "https://arxiv.org/pdf/2512.17452"
          },
          {
            "title": "KVCompose: Efficient Structured KV Cache Compression with Composite Tokens",
            "url": "https://arxiv.org/pdf/2509.05165"
          },
          {
            "title": "GitHub - Zefan-Cai/Awesome-LLM-KV-Cache: Awesome-LLM-KV-Cache: A curated list of 📙Awesome LLM KV Cache Papers with Codes.",
            "url": "https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache"
          },
          {
            "title": "Keep the Cost Down: A Review on Methods to Optimize LLM’s KV Cache Consumption",
            "url": "https://arxiv.org/html/2407.18003v4"
          },
          {
            "title": "CAOTE: KV Cache Eviction for LLMs via Attention Output Error-Based Token",
            "url": "https://www.arxiv.org/pdf/2504.14051v4"
          }
        ]
      },
      "Based on the search results, here's what I found about TOVA (Token Omission Via Attention):\n\n## Overview\n\nToken Omission via Attention (TOVA) drops tokens based on attention values by looking at the current step and checking which tokens attention heads are focusing on.\n\n## GitHub Repository\n\nThe official GitHub repository is located at https://github.com/schwartz-lab-NLP/TOVA, which provides implementation code and example usage for integrating TOVA with transformer models.\n\n## Technical Details\n\nTOVA proposes a simple greedy method to discard useless tokens. While keeping a fixed-length of KV-Cache, TOVA evicts at each decoding step the tokens with minimal attention weights layer-wise.\n\n## Academic Context\n\nTOVA is one of several token eviction methods (alongside H2O, SnapKV, and RoCO) that retain tokens with high attention scores in the KV cache with various algorithmic modifications. The paper \"Transformers are Multi-State RNNs\" by Oren et al., published in January 2024, introduced TOVA.\n\n## Performance\n\nTOVA has been evaluated against newer methods like CAOTE, with CAOTE-boosted approaches showing improvements over TOVA in some benchmarks, though TOVA still remains a competitive baseline for KV cache optimization."
    ],
    "durationSeconds": 7.235888747999997
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information. Let me also check for the FASA GitHub repo and StreamingLLM for completeness.

Let me compile all the information and create the survey document. Let me also check the kvpress PyPI page for specific version/dependency info.

Let me now write up the comprehensive survey document.

Here's what I have:

**kvpress (NVIDIA)**:
- GitHub: NVIDIA/kvpress
- PyPI: kvpress
- Supports: Qwen2ForCausalLM confirmed
- Presses: RandomPress, KnormPress, SnapKVPress, ExpectedAttentionPress, StreamingLLMPress, TOVAPress, ThinKPress, SimLayerKVPress, DuoAttentionPress, FinchPress, KVzipPress, AdaKVPress, ComposedPress, DecodingPress, PrefillDecodingPress, CriticalKVPress, C

Continuing with R-KV, which is a NeurIPS 2025 paper supporting DeepSeek-R1-Distill-Qwen-14B with importance and redundancy scoring complexities, installable via pip with requirements, and compatible with HuggingFace, vLLM, SGLang, and FlashInfer. Then there's H2O from FMInference, which I'm still gathering details on.

Looking at several other KV cache compression methods now: SnapKV from NeurIPS 2024 available in kvpress and KVCache-Factory, TOVA from the Schwartz lab with a kvpress implementation, FASA which uses frequency-aware sparse attention via RoPE frequency chunks and is coming to ICLR 2026, and StreamingLLM which has a kvpress version and an original MIT implementation. There are also other approaches like AdaKV that I'm noting down.

Now I'm cataloging more recent methods including DefensiveKV, CakeKV, HeadKV, KVzip which had an oral presentation at NeurIPS 2025, and FastKVzip. I'm starting to organize these by their computational complexity—methods like StreamingLLM that operate in O(1) per token using position-only signals with a sink and recent window approach, versus CARC which uses EMA centroid similarity, and then O(L) methods that scale with sequence length.

I need to reconsider the complexity analysis more carefully though. H2O actually requires O(B) per step to update cumulative attention scores across all cached tokens rather than true O(1), TOVA is O(B) looking at current attention weights, SnapKV does O(L) work during the prefill phase before settling into a static cache, and StreamingLLM maintains true O(1) with its fixed window. R-KV operates differently with pairwise redundancy scoring among retained tokens.

Now I'm categorizing these methods by their design philosophy—content-aware approaches like H2O, TOVA, SnapKV, R-KV, FASA, CARC, and KnormPress versus position-based methods like StreamingLLM, and noting that some blend both strategies. I'm also distinguishing which methods account for recurrence patterns in reasoning tasks: R-KV, FASA, and CARC are designed with this in mind, while the others aren't. Ready to start writing up the full document now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "58e76593-5614-451b-b3f2-d32389e4201b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsQmGUQKB31AKXjaDjhxwX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4020,
      "cache_read_input_tokens": 33674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4020
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 39_

信息收集完毕，现在整理产出文档。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "953b191a-ecc4-4b6a-ad0e-907a5adcd3b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsQmGUQKB31AKXjaDjhxwX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4020,
      "cache_read_input_tokens": 33674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4020
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Write · `toolu_01PAVimBo5c5uqXoap1TLYzb`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/baseline_code_survey.md",
  "content": "# Baseline Code Survey: KV Cache Eviction Methods\n\n> Date: 2026-05-12 | Project: CARC (O(1) KV Cache Eviction)\n\n---\n\n## 1. kvpress 框架调研\n\n### 概述\n- **PyPI**: `pip install kvpress`\n- **GitHub**: [NVIDIA/kvpress](https://github.com/NVIDIA/kvpress)\n- **定位**: 统一的 KV cache compression 框架，基于 HuggingFace transformers，NVIDIA 维护\n\n### Qwen2 兼容性\n**已确认支持。** README 明确列出测试过的架构：\n- `LlamaForCausalLM`, `MistralForCausalLM`, `Phi3ForCausalLM`\n- **`Qwen2ForCausalLM`**, `Qwen3ForCausalLM`, `Gemma3ForCausalLM`\n\nDeepSeek-R1-Distill-Qwen-14B 基于 Qwen2 架构，直接兼容。\n\n### 支持的 Press 清单（30+）\n\n| Press | 类型 | 说明 |\n|-------|------|------|\n| `ExpectedAttentionPress` | Scorer | 估计期望注意力分数 |\n| `SnapKVPress` | Scorer | 观察窗口 + 池化选 token |\n| `TOVAPress` | Scorer | 当前步注意力权重 evict |\n| `StreamingLLMPress` | Scorer | Sink + recent window |\n| `KnormPress` | Scorer | Key 向量范数 |\n| `RandomPress` | Scorer | 随机 eviction（baseline） |\n| `ThinKPress` | Scorer | 通道剪枝 |\n| `CriticalKVPress` | Scorer | L1(Wo @ V) 重要性 |\n| `CriticalAdaKVPress` | Scorer | Critical + 自适应 head 分配 |\n| `SimLayerKVPress` | Scorer | 层间相似性 |\n| `DuoAttentionPress` | Scorer | 双流注意力 |\n| `FinchPress` | Scorer | Finch 算法 |\n| `KVzipPress` | Scorer | KVzip 门控蒸馏 |\n| `AdaKVPress` | Wrapper | 自适应 per-head budget |\n| `ComposedPress` | Wrapper | 组合多个 press |\n| `DecodingPress` | Wrapper | 解码阶段压缩 |\n| `PrefillDecodingPress` | Wrapper | Prefill + Decoding 联合 |\n\n### API 用法\n\n```python\nfrom transformers import pipeline\nfrom kvpress import ExpectedAttentionPress\n\npipe = pipeline(\"kv-press-text-generation\", model=\"deepseek-ai/DeepSeek-R1-Distill-Qwen-14B\")\npress = ExpectedAttentionPress(compression_ratio=0.5)\nanswer = pipe(context, question=question, press=press)[\"answer\"]\n```\n\n### 安装与依赖\n```bash\npip install kvpress\n# 可选：flash-attn, optimum-quanto (量化)\n# 开发模式：\ngit clone https://github.com/NVIDIA/kvpress.git && cd kvpress\nuv sync --extra eval --extra flash-attn\n```\n- 无显式 Python/PyTorch 版本要求，依赖 transformers >= 4.x\n- Python 3.10 + PyTorch 2.x + CUDA 12.x 环境应无兼容性问题\n\n### 评估能力\n- 内置 RULER benchmark (4k context)\n- 支持 AIME25、Math500 数学推理 benchmark\n- HuggingFace Leaderboard 集成\n- `speed_and_memory.ipynb` 性能分析\n\n---\n\n## 2. R-KV 代码调研\n\n### 概述\n- **GitHub**: [Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV)\n- **论文**: NeurIPS 2025\n- **定位**: 面向推理模型的 KV cache 压缩，兼顾 importance 和 redundancy\n\n### DeepSeek-R1-Distill-Qwen-14B 支持\n**直接支持。** 官方 benchmark 显式包含：\n- DeepSeek-R1-Distill-Llama-8B\n- **DeepSeek-R1-Distill-Qwen-14B**\n\n### 核心机制\n1. **Importance scoring**: 注意力分数累积，O(α × B_budget)\n2. **Redundancy scoring**: Key 向量 pairwise 相似度，**O(B_budget²)**\n3. **Joint eviction**: λ 加权平衡 importance 和 redundancy\n\n### 关键超参数\n- `kv_budget`: 保留的 KV 对数（如 128）\n- `observation_tokens`: 观察窗口大小（如 8）\n- λ: importance/redundancy 权衡（默认 0.1）\n\n### 运行方式\n```bash\npython3 ./run_math.py \\\n  --dataset_path ./data/aime24.jsonl \\\n  --model_path deepseek-ai/DeepSeek-R1-Distill-Qwen-14B \\\n  --method rkv \\\n  --kv_budget 128\n```\n\n### 代码结构\n```\nR-KV/\n├── HuggingFace/     # 主要集成\n├── vLLM/            # vLLM 后端\n├── SGLang/          # SGLang 后端\n├── FlashInfer/      # FlashInfer 后端\n├── rkv/             # 核心压缩逻辑\n├── evaluation/      # benchmark 工具 (latex2sympy)\n└── examples/eval.sh # 评估脚本\n```\n\n### 安装\n```bash\npip install -r requirements.txt\npip install -e .\n# Flash Attention 推荐但非必需\n```\n\n### 评估 Benchmark\n- MATH-500（平均 2,979 tokens/solution）\n- AIME 2024（平均 15,536 tokens/solution）\n\n---\n\n## 3. 竞品清单（Signal Taxonomy）\n\n### 按计算复杂度分类\n\n| 方法 | 复杂度 (per step) | Content-Aware | Recurrence-Aware | 官方代码 | 论文 |\n|------|-------------------|---------------|-------------------|----------|------|\n| **StreamingLLM** | O(1) | ✗ (position only) | ✗ | [MIT-Han-Lab/streaming-llm](https://github.com/MIT-Han-Lab/streaming-llm) / kvpress 内置 | ICLR 2024 |\n| **CARC (ours)** | O(1) | ✓ (EMA centroid sim) | ✓ | — | — |\n| **TOVA** | O(B) | ✓ (attn weights) | ✗ | [schwartz-lab-NLP/TOVA](https://github.com/schwartz-lab-NLP/TOVA) / kvpress 内置 | 2024 |\n| **H2O** | O(B) | ✓ (cumul. attn) | ✗ | [FMInference/H2O](https://github.com/FMInference/H2O) / kvpress 内置 | NeurIPS 2023 |\n| **KnormPress** | O(B) | ✓ (key norm) | ✗ | kvpress 内置 | — |\n| **SnapKV** | O(L_obs) prefill-only | ✓ (obs. window attn) | ✗ | kvpress 内置 / [KVCache-Factory](https://github.com/Zefan-Cai/KVCache-Factory) | NeurIPS 2024 |\n| **AdaKV** | O(B) | ✓ (adaptive head budget) | ✗ | [FFY0/AdaKV](https://github.com/FFY0/AdaKV) / kvpress 内置 | NeurIPS 2025 |\n| **CakeKV** | O(B) | ✓ (layer-aware cascade) | ✗ | [antgroup/cakekv](https://github.com/antgroup/cakekv) | ICLR 2025 |\n| **HeadKV** | O(B) | ✓ (head-level) | Partial | [FYYFU/HeadKV](https://github.com/FYYFU/HeadKV) | ICLR 2025 |\n| **R-KV** | O(B²) | ✓ (pairwise key sim) | ✓ | [Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV) | NeurIPS 2025 |\n| **FASA** | O(L × k_FC) | ✓ (freq. chunk) | ✓ | [AMAP-ML/FASA-ICLR2026](https://github.com/AMAP-ML/FASA-ICLR2026) | ICLR 2026 |\n| **KVzip** | O(B) | ✓ (gated distill) | ✗ | [snu-mllab/KVzip](https://github.com/snu-mllab/KVzip) / kvpress 内置 | NeurIPS 2025 Oral |\n| **DefensiveKV** | O(B) | ✓ (defensive evict) | ✗ | [FFY0/DefensiveKV](https://github.com/FFY0/DefensiveKV) | ICLR 2026 |\n\n> **B** = budget size (retained tokens), **L** = sequence length, **L_obs** = observation window, **k_FC** = number of dominant frequency chunks (k_FC ≪ d)\n\n### CARC 的竞争优势定位\n\n| 维度 | StreamingLLM | H2O/TOVA | SnapKV | R-KV | FASA | **CARC** |\n|------|-------------|----------|--------|------|------|----------|\n| Per-token 复杂度 | O(1) | O(B) | O(L_obs) | O(B²) | O(L×k) | **O(1)** |\n| Content-aware | ✗ | ✓ | ✓ | ✓ | ✓ | **✓** |\n| Recurrence-aware | ✗ | ✗ | ✗ | ✓ | ✓ | **✓** |\n| 唯一的 O(1) + content-aware + recurrence-aware | — | — | — | — | — | **✓** |\n\n---\n\n## 4. 安装可行性（Python 3.10 + PyTorch 2.x + CUDA 12.x）\n\n### kvpress\n```bash\npip install kvpress\n# 预期无冲突。依赖 transformers, torch，均兼容目标环境。\n# 可选: pip install flash-attn --no-build-isolation (需 CUDA toolkit)\n```\n\n### R-KV\n```bash\ngit clone https://github.com/Zefan-Cai/R-KV.git\ncd R-KV\npip install -r requirements.txt\npip install -e .\n# 注意: evaluation/ 下有 latex2sympy 依赖需单独构建\n# Flash Attention 推荐: pip install flash-attn --no-build-isolation\n```\n\n### H2O（独立使用）\n```bash\ngit clone https://github.com/FMInference/H2O.git\n# 或直接用 kvpress 内置的 H2OPress（更推荐）\n```\n\n### 潜在冲突点\n1. **flash-attn** 编译需匹配 CUDA toolkit 版本，建议用 `pip install flash-attn --no-build-isolation`\n2. **R-KV 的 latex2sympy** 用于评估 MATH/AIME，非核心依赖\n3. **kvpress 与 R-KV 可共存**——kvpress 是 pip 包，R-KV 是独立 repo，依赖不冲突\n\n### 推荐安装顺序\n```bash\n# 1. 基础框架\npip install kvpress\n\n# 2. R-KV baseline\ngit clone https://github.com/Zefan-Cai/R-KV.git\ncd R-KV && pip install -r requirements.txt && pip install -e .\n\n# 3. 验证\npython -c \"from kvpress import ExpectedAttentionPress; print('kvpress OK')\"\npython -c \"import rkv; print('R-KV OK')\"\n```\n\n---\n\n## 5. 推荐 Baseline 选择\n\n### Primary Baselines（必须对比）\n1. **H2O** — 经典 attention-based eviction，NeurIPS 2023，通过 kvpress 直接可用\n2. **R-KV** — 唯一的 reasoning-aware baseline，NeurIPS 2025，直接支持 Qwen-14B\n\n### Secondary Baselines（增强论文说服力）\n3. **SnapKV** — Prefill-phase 压缩代表，NeurIPS 2024，kvpress 内置\n4. **StreamingLLM** — O(1) position-only baseline，凸显 CARC 的 content-aware 优势\n5. **FASA** — ICLR 2026 最新竞品，frequency-aware，reasoning-aware\n\n### 对比叙事\n- vs StreamingLLM: 同为 O(1)，但 CARC content-aware → 更好的压缩质量\n- vs H2O/TOVA: CARC O(1) vs O(B) → 更快，且 recurrence-aware\n- vs R-KV: CARC O(1) vs O(B²) → 显著更快，相当或更优的压缩质量\n- vs FASA: CARC O(1) vs O(L×k) → 更简单，无需频率分解\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "5405669d-eb81-4c1b-af8d-a87eb78554e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsQmGUQKB31AKXjaDjhxwX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4020,
      "cache_read_input_tokens": 33674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4020
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-12T14:23:30.708Z_

<details><summary>↩ Tool result · `toolu_01PAVimBo5c5uqXoap1TLYzb`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/baseline_code_survey.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "debe5f33-79cb-4a7a-bc3f-d40388826dae",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/baseline_code_survey.md",
    "content": "# Baseline Code Survey: KV Cache Eviction Methods\n\n> Date: 2026-05-12 | Project: CARC (O(1) KV Cache Eviction)\n\n---\n\n## 1. kvpress 框架调研\n\n### 概述\n- **PyPI**: `pip install kvpress`\n- **GitHub**: [NVIDIA/kvpress](https://github.com/NVIDIA/kvpress)\n- **定位**: 统一的 KV cache compression 框架，基于 HuggingFace transformers，NVIDIA 维护\n\n### Qwen2 兼容性\n**已确认支持。** README 明确列出测试过的架构：\n- `LlamaForCausalLM`, `MistralForCausalLM`, `Phi3ForCausalLM`\n- **`Qwen2ForCausalLM`**, `Qwen3ForCausalLM`, `Gemma3ForCausalLM`\n\nDeepSeek-R1-Distill-Qwen-14B 基于 Qwen2 架构，直接兼容。\n\n### 支持的 Press 清单（30+）\n\n| Press | 类型 | 说明 |\n|-------|------|------|\n| `ExpectedAttentionPress` | Scorer | 估计期望注意力分数 |\n| `SnapKVPress` | Scorer | 观察窗口 + 池化选 token |\n| `TOVAPress` | Scorer | 当前步注意力权重 evict |\n| `StreamingLLMPress` | Scorer | Sink + recent window |\n| `KnormPress` | Scorer | Key 向量范数 |\n| `RandomPress` | Scorer | 随机 eviction（baseline） |\n| `ThinKPress` | Scorer | 通道剪枝 |\n| `CriticalKVPress` | Scorer | L1(Wo @ V) 重要性 |\n| `CriticalAdaKVPress` | Scorer | Critical + 自适应 head 分配 |\n| `SimLayerKVPress` | Scorer | 层间相似性 |\n| `DuoAttentionPress` | Scorer | 双流注意力 |\n| `FinchPress` | Scorer | Finch 算法 |\n| `KVzipPress` | Scorer | KVzip 门控蒸馏 |\n| `AdaKVPress` | Wrapper | 自适应 per-head budget |\n| `ComposedPress` | Wrapper | 组合多个 press |\n| `DecodingPress` | Wrapper | 解码阶段压缩 |\n| `PrefillDecodingPress` | Wrapper | Prefill + Decoding 联合 |\n\n### API 用法\n\n```python\nfrom transformers import pipeline\nfrom kvpress import ExpectedAttentionPress\n\npipe = pipeline(\"kv-press-text-generation\", model=\"deepseek-ai/DeepSeek-R1-Distill-Qwen-14B\")\npress = ExpectedAttentionPress(compression_ratio=0.5)\nanswer = pipe(context, question=question, press=press)[\"answer\"]\n```\n\n### 安装与依赖\n```bash\npip install kvpress\n# 可选：flash-attn, optimum-quanto (量化)\n# 开发模式：\ngit clone https://github.com/NVIDIA/kvpress.git && cd kvpress\nuv sync --extra eval --extra flash-attn\n```\n- 无显式 Python/PyTorch 版本要求，依赖 transformers >= 4.x\n- Python 3.10 + PyTorch 2.x + CUDA 12.x 环境应无兼容性问题\n\n### 评估能力\n- 内置 RULER benchmark (4k context)\n- 支持 AIME25、Math500 数学推理 benchmark\n- HuggingFace Leaderboard 集成\n- `speed_and_memory.ipynb` 性能分析\n\n---\n\n## 2. R-KV 代码调研\n\n### 概述\n- **GitHub**: [Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV)\n- **论文**: NeurIPS 2025\n- **定位**: 面向推理模型的 KV cache 压缩，兼顾 importance 和 redundancy\n\n### DeepSeek-R1-Distill-Qwen-14B 支持\n**直接支持。** 官方 benchmark 显式包含：\n- DeepSeek-R1-Distill-Llama-8B\n- **DeepSeek-R1-Distill-Qwen-14B**\n\n### 核心机制\n1. **Importance scoring**: 注意力分数累积，O(α × B_budget)\n2. **Redundancy scoring**: Key 向量 pairwise 相似度，**O(B_budget²)**\n3. **Joint eviction**: λ 加权平衡 importance 和 redundancy\n\n### 关键超参数\n- `kv_budget`: 保留的 KV 对数（如 128）\n- `observation_tokens`: 观察窗口大小（如 8）\n- λ: importance/redundancy 权衡（默认 0.1）\n\n### 运行方式\n```bash\npython3 ./run_math.py \\\n  --dataset_path ./data/aime24.jsonl \\\n  --model_path deepseek-ai/DeepSeek-R1-Distill-Qwen-14B \\\n  --method rkv \\\n  --kv_budget 128\n```\n\n### 代码结构\n```\nR-KV/\n├── HuggingFace/     # 主要集成\n├── vLLM/            # vLLM 后端\n├── SGLang/          # SGLang 后端\n├── FlashInfer/      # FlashInfer 后端\n├── rkv/             # 核心压缩逻辑\n├── evaluation/      # benchmark 工具 (latex2sympy)\n└── examples/eval.sh # 评估脚本\n```\n\n### 安装\n```bash\npip install -r requirements.txt\npip install -e .\n# Flash Attention 推荐但非必需\n```\n\n### 评估 Benchmark\n- MATH-500（平均 2,979 tokens/solution）\n- AIME 2024（平均 15,536 tokens/solution）\n\n---\n\n## 3. 竞品清单（Signal Taxonomy）\n\n### 按计算复杂度分类\n\n| 方法 | 复杂度 (per step) | Content-Aware | Recurrence-Aware | 官方代码 | 论文 |\n|------|-------------------|---------------|-------------------|----------|------|\n| **StreamingLLM** | O(1) | ✗ (position only) | ✗ | [MIT-Han-Lab/streaming-llm](https://github.com/MIT-Han-Lab/streaming-llm) / kvpress 内置 | ICLR 2024 |\n| **CARC (ours)** | O(1) | ✓ (EMA centroid sim) | ✓ | — | — |\n| **TOVA** | O(B) | ✓ (attn weights) | ✗ | [schwartz-lab-NLP/TOVA](https://github.com/schwartz-lab-NLP/TOVA) / kvpress 内置 | 2024 |\n| **H2O** | O(B) | ✓ (cumul. attn) | ✗ | [FMInference/H2O](https://github.com/FMInference/H2O) / kvpress 内置 | NeurIPS 2023 |\n| **KnormPress** | O(B) | ✓ (key norm) | ✗ | kvpress 内置 | — |\n| **SnapKV** | O(L_obs) prefill-only | ✓ (obs. window attn) | ✗ | kvpress 内置 / [KVCache-Factory](https://github.com/Zefan-Cai/KVCache-Factory) | NeurIPS 2024 |\n| **AdaKV** | O(B) | ✓ (adaptive head budget) | ✗ | [FFY0/AdaKV](https://github.com/FFY0/AdaKV) / kvpress 内置 | NeurIPS 2025 |\n| **CakeKV** | O(B) | ✓ (layer-aware cascade) | ✗ | [antgroup/cakekv](https://github.com/antgroup/cakekv) | ICLR 2025 |\n| **HeadKV** | O(B) | ✓ (head-level) | Partial | [FYYFU/HeadKV](https://github.com/FYYFU/HeadKV) | ICLR 2025 |\n| **R-KV** | O(B²) | ✓ (pairwise key sim) | ✓ | [Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV) | NeurIPS 2025 |\n| **FASA** | O(L × k_FC) | ✓ (freq. chunk) | ✓ | [AMAP-ML/FASA-ICLR2026](https://github.com/AMAP-ML/FASA-ICLR2026) | ICLR 2026 |\n| **KVzip** | O(B) | ✓ (gated distill) | ✗ | [snu-mllab/KVzip](https://github.com/snu-mllab/KVzip) / kvpress 内置 | NeurIPS 2025 Oral |\n| **DefensiveKV** | O(B) | ✓ (defensive evict) | ✗ | [FFY0/DefensiveKV](https://github.com/FFY0/DefensiveKV) | ICLR 2026 |\n\n> **B** = budget size (retained tokens), **L** = sequence length, **L_obs** = observation window, **k_FC** = number of dominant frequency chunks (k_FC ≪ d)\n\n### CARC 的竞争优势定位\n\n| 维度 | StreamingLLM | H2O/TOVA | SnapKV | R-KV | FASA | **CARC** |\n|------|-------------|----------|--------|------|------|----------|\n| Per-token 复杂度 | O(1) | O(B) | O(L_obs) | O(B²) | O(L×k) | **O(1)** |\n| Content-aware | ✗ | ✓ | ✓ | ✓ | ✓ | **✓** |\n| Recurrence-aware | ✗ | ✗ | ✗ | ✓ | ✓ | **✓** |\n| 唯一的 O(1) + content-aware + recurrence-aware | — | — | — | — | — | **✓** |\n\n---\n\n## 4. 安装可行性（Python 3.10 + PyTorch 2.x + CUDA 12.x）\n\n### kvpress\n```bash\npip install kvpress\n# 预期无冲突。依赖 transformers, torch，均兼容目标环境。\n# 可选: pip install flash-attn --no-build-isolation (需 CUDA toolkit)\n```\n\n### R-KV\n```bash\ngit clone https://github.com/Zefan-Cai/R-KV.git\ncd R-KV\npip install -r requirements.txt\npip install -e .\n# 注意: evaluation/ 下有 latex2sympy 依赖需单独构建\n# Flash Attention 推荐: pip install flash-attn --no-build-isolation\n```\n\n### H2O（独立使用）\n```bash\ngit clone https://github.com/FMInference/H2O.git\n# 或直接用 kvpress 内置的 H2OPress（更推荐）\n```\n\n### 潜在冲突点\n1. **flash-attn** 编译需匹配 CUDA toolkit 版本，建议用 `pip install flash-attn --no-build-isolation`\n2. **R-KV 的 latex2sympy** 用于评估 MATH/AIME，非核心依赖\n3. **kvpress 与 R-KV 可共存**——kvpress 是 pip 包，R-KV 是独立 repo，依赖不冲突\n\n### 推荐安装顺序\n```bash\n# 1. 基础框架\npip install kvpress\n\n# 2. R-KV baseline\ngit clone https://github.com/Zefan-Cai/R-KV.git\ncd R-KV && pip install -r requirements.txt && pip install -e .\n\n# 3. 验证\npython -c \"from kvpress import ExpectedAttentionPress; print('kvpress OK')\"\npython -c \"import rkv; print('R-KV OK')\"\n```\n\n---\n\n## 5. 推荐 Baseline 选择\n\n### Primary Baselines（必须对比）\n1. **H2O** — 经典 attention-based eviction，NeurIPS 2023，通过 kvpress 直接可用\n2. **R-KV** — 唯一的 reasoning-aware baseline，NeurIPS 2025，直接支持 Qwen-14B\n\n### Secondary Baselines（增强论文说服力）\n3. **SnapKV** — Prefill-phase 压缩代表，NeurIPS 2024，kvpress 内置\n4. **StreamingLLM** — O(1) position-only baseline，凸显 CARC 的 content-aware 优势\n5. **FASA** — ICLR 2026 最新竞品，frequency-aware，reasoning-aware\n\n### 对比叙事\n- vs StreamingLLM: 同为 O(1)，但 CARC content-aware → 更好的压缩质量\n- vs H2O/TOVA: CARC O(1) vs O(B) → 更快，且 recurrence-aware\n- vs R-KV: CARC O(1) vs O(B²) → 显著更快，相当或更优的压缩质量\n- vs FASA: CARC O(1) vs O(L×k) → 更简单，无需频率分解\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 42_

注册 artifact。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "a33296ca-ab6c-4dbe-a8c0-6bd70595f432",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XtxYSWhFJUFZWjn8ULow7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5265,
      "cache_read_input_tokens": 37694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5265
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01AR71Dbb3EGTE9wkYkQZi9H`</summary>

```json
{
  "name": "baseline_code_survey",
  "type": "report",
  "description": "Baseline code survey for CARC project: kvpress framework analysis, R-KV code review, competitor taxonomy table (12 methods with complexity/signal classification), installation guide",
  "project": "solver-verified-formalizer-rl",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/baseline_code_survey.md",
  "tags": [
    "baseline",
    "kvpress",
    "R-KV",
    "H2O",
    "survey",
    "EMNLP2026"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "dab5bf09-7c5d-4612-89b9-afe65f442cc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XtxYSWhFJUFZWjn8ULow7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5265,
      "cache_read_input_tokens": 37694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5265
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-12T14:23:36.548Z_

<details><summary>↩ Tool result · `toolu_01AR71Dbb3EGTE9wkYkQZi9H`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_6c2367\", \"name\": \"baseline_code_survey\", \"type\": \"report\", \"description\": \"Baseline code survey for CARC project: kvpress framework analysis, R-KV code review, competitor taxonomy table (12 methods with complexity/signal classification), installation guide\", \"path\": \"projects/solver-verified-formalizer-rl/artifacts/_project/report/baseline_code_survey.md\", \"url\": null, \"project\": \"solver-verified-formalizer-rl\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T14:23:36.477484+00:00\", \"tags\": [\"baseline\", \"kvpress\", \"R-KV\", \"H2O\", \"survey\", \"EMNLP2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "d94a3657-6518-4daa-87e1-04042e716529",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260512_6c2367\\\", \\\"name\\\": \\\"baseline_code_survey\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Baseline code survey for CARC project: kvpress framework analysis, R-KV code review, competitor taxonomy table (12 methods with complexity/signal classification), installation guide\\\", \\\"path\\\": \\\"projects/solver-verified-formalizer-rl/artifacts/_project/report/baseline_code_survey.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"solver-verified-formalizer-rl\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-12T14:23:36.477484+00:00\\\", \\\"tags\\\": [\\\"baseline\\\", \\\"kvpress\\\", \\\"R-KV\\\", \\\"H2O\\\", \\\"survey\\\", \\\"EMNLP2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_6c2367\", \"name\": \"baseline_code_survey\", \"type\": \"report\", \"description\": \"Baseline code survey for CARC project: kvpress framework analysis, R-KV code review, competitor taxonomy table (12 methods with complexity/signal classification), installation guide\", \"path\": \"projects/solver-verified-formalizer-rl/artifacts/_project/report/baseline_code_survey.md\", \"url\": null, \"project\": \"solver-verified-formalizer-rl\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T14:23:36.477484+00:00\", \"tags\": [\"baseline\", \"kvpress\", \"R-KV\", \"H2O\", \"survey\", \"EMNLP2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 45_

调研完成。产出已写入 `artifacts/baseline_code_survey.md` 并注册。核心结论：

**kvpress**：确认支持 Qwen2ForCausalLM，`pip install kvpress` 即可获得 H2O、SnapKV、TOVA、StreamingLLM 等 30+ 种 press，API 简洁（pipeline 一行调用）。Python 3.10 + PyTorch 2.x + CUDA 12.x 无兼容性问题。

**R-KV**：[Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV)，NeurIPS 2025，显式支持 DeepSeek-R1-Distill-Qwen-14B。核心瓶颈是 redundancy scoring 的 **O(B²)** 复杂度——正好是 CARC 要替代的。支持 HuggingFace/vLLM/SGLang 多后端。

**推荐 baseline 选择**：
- **Primary**: H2O（kvpress 内置）+ R-KV（独立 repo）
- **Secondary**: StreamingLLM（凸显 content-aware 优势）、SnapKV、FASA（[ICLR 2026 最新竞品](https://github.com/AMAP-ML/FASA-ICLR2026)）

**CARC 唯一定位**：12 个竞品中唯一同时满足 O(1) + content-aware + recurrence-aware 的方法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "uuid": "6a5f94e8-50ed-43da-b0ce-52f3f08af6d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SXafwbyeDSVHcwq2rFHCA5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 42959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 585
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 46_

调研完成。产出已写入 `artifacts/baseline_code_survey.md` 并注册。核心结论：

**kvpress**：确认支持 Qwen2ForCausalLM，`pip install kvpress` 即可获得 H2O、SnapKV、TOVA、StreamingLLM 等 30+ 种 press，API 简洁（pipeline 一行调用）。Python 3.10 + PyTorch 2.x + CUDA 12.x 无兼容性问题。

**R-KV**：[Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV)，NeurIPS 2025，显式支持 DeepSeek-R1-Distill-Qwen-14B。核心瓶颈是 redundancy scoring 的 **O(B²)** 复杂度——正好是 CARC 要替代的。支持 HuggingFace/vLLM/SGLang 多后端。

**推荐 baseline 选择**：
- **Primary**: H2O（kvpress 内置）+ R-KV（独立 repo）
- **Secondary**: StreamingLLM（凸显 content-aware 优势）、SnapKV、FASA（[ICLR 2026 最新竞品](https://github.com/AMAP-ML/FASA-ICLR2026)）

**CARC 唯一定位**：12 个竞品中唯一同时满足 O(1) + content-aware + recurrence-aware 的方法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 161280,
  "duration_api_ms": 223207,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "b9dcae84-2952-42e4-abf2-4657902a740f",
  "total_cost_usd": 0.84487175,
  "usage": {
    "input_tokens": 3028,
    "cache_creation_input_tokens": 31703,
    "cache_read_input_tokens": 202520,
    "output_tokens": 7449,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31703,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 436,
        "cache_read_input_tokens": 42959,
        "cache_creation_input_tokens": 585,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 585
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 215418,
      "outputTokens": 5737,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 10,
      "costUSD": 0.34410300000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3028,
      "outputTokens": 7449,
      "cacheReadInputTokens": 202520,
      "cacheCreationInputTokens": 31703,
      "webSearchRequests": 0,
      "costUSD": 0.50076875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "31e77693-2e09-4155-ae2b-bfe3d6e95f5b"
}
```

</details>

---
