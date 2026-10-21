# research 1 3b model check

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_research_1_3b-model-check_20260518T072556.log`
- **Structured JSON:** [`0e518da7b8f7c9698be3.json`](../../sessions/0e/0e518da7b8f7c9698be3.json)

## Before a recorded user message

34 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
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
  "uuid": "5cf034ef-2234-43f7-8750-2d797408a4a0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/memory/"
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
    "resetsAt": 1779097200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "11537800-e370-46b9-abdb-5e3979fa88ad",
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f"
}
```

---

### Assistant

_source line 4_

I'll search for 1.3B models from Wang et al.'s hybrid linear attention work. Let me fetch the collection page and search in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "8ec3bcd0-650f-47a0-8136-ee97d000fc91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GgU9trgcYHNL8GH3juVV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12841,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12841
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LRcTj9NTidMeKPeS8rGWWk`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "13cc8dc1-a35b-40ba-8d0a-24c2dd274ecb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GgU9trgcYHNL8GH3juVV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12841,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12841
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-18T07:26:07.161Z_

<details><summary>↩ Tool result · `toolu_01LRcTj9NTidMeKPeS8rGWWk`</summary>

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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "efcf1356-4841-4736-ae84-16ea06921cd6",
  "tool_use_result": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
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
Now let me fetch the HuggingFace collection page and run searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "6ddca210-b943-4979-85d2-b1a40bb59127",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJrq6H8FaaaLB8VekJJg8V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 24682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1133
      },
      "output_tokens": 27,
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J9gwftt2JncE2XEk71q3ds`</summary>

```json
{
  "url": "https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e",
  "prompt": "List ALL models in this collection. For each model, extract: model name, size (340M, 1.3B, 7B etc), architecture type (GatedDeltaNet, HGRN2, RetNet, Transformer, etc), hybrid ratio, and any other details. I need a complete inventory of every model listed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "07c89929-5f12-42d4-8bec-210497c659ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJrq6H8FaaaLB8VekJJg8V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 24682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1133
      },
      "output_tokens": 27,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SAiXx7mAJyAdtBZSkzjYbX`</summary>

```json
{
  "query": "m-a-p 1.3B hybrid linear attention huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "23ed05b2-82e8-4ab7-9389-b5a89d1a2220",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJrq6H8FaaaLB8VekJJg8V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 24682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1133
      },
      "output_tokens": 27,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B4JFvmvbJBXZpgc8xn81aH`</summary>

```json
{
  "query": "Wang et al \"hybrid linear attention\" 1.3B model arXiv 2507.06457"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "36ec5f84-f2bb-493e-abc3-1ee44bcb4d78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJrq6H8FaaaLB8VekJJg8V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 24682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1133
      },
      "output_tokens": 27,
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

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M4hTAvpt6Ly1wWmCsaLHYn`</summary>

```json
{
  "query": "site:huggingface.co m-a-p 1.3B OR 1B linear attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "87a043a8-5854-49d1-924f-de460f022e36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJrq6H8FaaaLB8VekJJg8V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 24682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1133
      },
      "output_tokens": 27,
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

_source line 12 · 2026-05-18T07:26:19.047Z_

<details><summary>↩ Tool result · `toolu_01SAiXx7mAJyAdtBZSkzjYbX`</summary>

```text
Web search results for query: "m-a-p 1.3B hybrid linear attention huggingface"

Links: [{"title":"Hybrid Linear Attention Research - a m-a-p Collection","url":"https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research"},{"title":"Paper page - A Systematic Analysis of Hybrid Linear Attention","url":"https://huggingface.co/papers/2507.06457"},{"title":"m-a-p/1.3B-100B-DeltaNet-hybrid-6-1 · Hugging Face","url":"https://huggingface.co/m-a-p/1.3B-100B-DeltaNet-hybrid-6-1"},{"title":"m-a-p/transformer_340M_baseline · Hugging Face","url":"https://huggingface.co/m-a-p/transformer_340M_baseline"},{"title":"(PDF) A Systematic Analysis of Hybrid Linear Attention","url":"https://www.researchgate.net/publication/393538945_A_Systematic_Analysis_of_Hybrid_Linear_Attention"},{"title":"m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"},{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"m-a-p/340M-20B-DeltaNet-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-24-1"},{"title":"ByteDance conducted the Hybrid Linear Attention Research They systematically evaluated various linear attention models within hybrid architectures, revealing that superior standalone linear models do not necessarily lead to better performance in hybrid configurations.","url":"https://www.threads.com/@sung.kim.mw/post/DOJBMCIkVWH/bytedance-conducted-the-hybrid-linear-attention-researchthey-systematically-eval"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/html/2507.06457v1"}]

Based on the search results, here's what I found about the m-a-p 1.3B hybrid linear attention models on Hugging Face:

The m-a-p team trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios.

These models are part of a research project focused on systematically analyzing hybrid linear attention architectures. Transformers face quadratic complexity and memory issues with long sequences, which prompted the adoption of linear attention mechanisms using fixed-size hidden states. However, linear models often suffer from limited recall performance, leading to hybrid architectures that combine linear and full attention layers.

The researchers recommend architectures such as HGRN-2 or GatedDeltaNet with a linear-to-full ratio between 3:1 and 6:1 to achieve Transformer-level recall efficiently. Their benchmarking reveals that superior standalone linear models do not necessarily excel in hybrids.

The collection includes all 1.3B & 340M hybrid linear-attention experiments and is available on the Hugging Face Hub at the m-a-p collection page, along with a corresponding paper that provides detailed analysis of the different architectural variants and their performance characteristics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "346be440-3f31-4413-8075-20f965d61231",
  "tool_use_result": {
    "query": "m-a-p 1.3B hybrid linear attention huggingface",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LmMAXWNwZndQMPb3dAyWZE",
        "content": [
          {
            "title": "Hybrid Linear Attention Research - a m-a-p Collection",
            "url": "https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research"
          },
          {
            "title": "Paper page - A Systematic Analysis of Hybrid Linear Attention",
            "url": "https://huggingface.co/papers/2507.06457"
          },
          {
            "title": "m-a-p/1.3B-100B-DeltaNet-hybrid-6-1 · Hugging Face",
            "url": "https://huggingface.co/m-a-p/1.3B-100B-DeltaNet-hybrid-6-1"
          },
          {
            "title": "m-a-p/transformer_340M_baseline · Hugging Face",
            "url": "https://huggingface.co/m-a-p/transformer_340M_baseline"
          },
          {
            "title": "(PDF) A Systematic Analysis of Hybrid Linear Attention",
            "url": "https://www.researchgate.net/publication/393538945_A_Systematic_Analysis_of_Hybrid_Linear_Attention"
          },
          {
            "title": "m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 · Hugging Face",
            "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"
          },
          {
            "title": "[2507.06457] A Systematic Analysis of Hybrid Linear Attention",
            "url": "https://arxiv.org/abs/2507.06457"
          },
          {
            "title": "m-a-p/340M-20B-DeltaNet-hybrid-24-1 · Hugging Face",
            "url": "https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-24-1"
          },
          {
            "title": "ByteDance conducted the Hybrid Linear Attention Research They systematically evaluated various linear attention models within hybrid architectures, revealing that superior standalone linear models do not necessarily lead to better performance in hybrid configurations.",
            "url": "https://www.threads.com/@sung.kim.mw/post/DOJBMCIkVWH/bytedance-conducted-the-hybrid-linear-attention-researchthey-systematically-eval"
          },
          {
            "title": "A Systematic Analysis of Hybrid Linear Attention",
            "url": "https://arxiv.org/html/2507.06457v1"
          }
        ]
      },
      "Based on the search results, here's what I found about the m-a-p 1.3B hybrid linear attention models on Hugging Face:\n\nThe m-a-p team trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios.\n\nThese models are part of a research project focused on systematically analyzing hybrid linear attention architectures. Transformers face quadratic complexity and memory issues with long sequences, which prompted the adoption of linear attention mechanisms using fixed-size hidden states. However, linear models often suffer from limited recall performance, leading to hybrid architectures that combine linear and full attention layers.\n\nThe researchers recommend architectures such as HGRN-2 or GatedDeltaNet with a linear-to-full ratio between 3:1 and 6:1 to achieve Transformer-level recall efficiently. Their benchmarking reveals that superior standalone linear models do not necessarily excel in hybrids.\n\nThe collection includes all 1.3B & 340M hybrid linear-attention experiments and is available on the Hugging Face Hub at the m-a-p collection page, along with a corresponding paper that provides detailed analysis of the different architectural variants and their performance characteristics."
    ],
    "durationSeconds": 6.529573588999998
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T07:26:20.340Z_

<details><summary>↩ Tool result · `toolu_01M4hTAvpt6Ly1wWmCsaLHYn`</summary>

```text
Web search results for query: "site:huggingface.co m-a-p 1.3B OR 1B linear attention"

Links: [{"title":"Hybrid Linear Attention Research - a m-a-p Collection","url":"https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research"},{"title":"Paper page - A Systematic Analysis of Hybrid Linear Attention","url":"https://huggingface.co/papers/2507.06457"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=full+Linear+Attention"},{"title":"Paper page - Simple linear attention language models balance the recall-throughput tradeoff","url":"https://huggingface.co/papers/2402.18668"},{"title":"Paper page - Gated Linear Attention Transformers with Hardware-Efficient Training","url":"https://huggingface.co/papers/2312.06635"},{"title":"meta-llama/Llama-3.2-3B-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct"},{"title":"meta-llama/Llama-3.2-1B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.2-1B"},{"title":"meta-llama/Llama-3.2-3B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.2-3B"},{"title":"Wan2.1-T2V-1.3B-Q4_K_M.gguf · samuelchristlie/Wan2.1-T2V-1.3B-GGUF at 5a512b15fc35d1b67a074cfe55a591be9e9ef9b5","url":"https://huggingface.co/samuelchristlie/Wan2.1-T2V-1.3B-GGUF/blob/5a512b15fc35d1b67a074cfe55a591be9e9ef9b5/Wan2.1-T2V-1.3B-Q4_K_M.gguf"}]

Based on the search results, I found relevant information about m-a-p's 1.3B and linear attention research:

## Key Findings

The m-a-p organization maintains a collection featuring all 1.3B & 340M hybrid linear-attention experiments.

They trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios.

While linear models often suffer from limited recall performance, leading to hybrid architectures that combine linear and full attention layers, the choice of linear attention component has not been deeply explored.

The research highlights selective gating, hierarchical recurrence, and controlled forgetting as critical for effective hybrid models, and recommends architectures such as HGRN-2 or GatedDeltaNet with a linear-to-full ratio between 3:1 and 6:1 to achieve Transformer-level recall efficiently.

The collection and research is available at the Hugging Face model hub under the m-a-p organization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "71d25a8b-58d1-4562-a472-dabcf7c4d255",
  "tool_use_result": {
    "query": "site:huggingface.co m-a-p 1.3B OR 1B linear attention",
    "results": [
      {
        "tool_use_id": "srvtoolu_018foZ9YSW1UR2MfbWtJcd6Y",
        "content": [
          {
            "title": "Hybrid Linear Attention Research - a m-a-p Collection",
            "url": "https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research"
          },
          {
            "title": "Paper page - A Systematic Analysis of Hybrid Linear Attention",
            "url": "https://huggingface.co/papers/2507.06457"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=full+Linear+Attention"
          },
          {
            "title": "Paper page - Simple linear attention language models balance the recall-throughput tradeoff",
            "url": "https://huggingface.co/papers/2402.18668"
          },
          {
            "title": "Paper page - Gated Linear Attention Transformers with Hardware-Efficient Training",
            "url": "https://huggingface.co/papers/2312.06635"
          },
          {
            "title": "meta-llama/Llama-3.2-3B-Instruct · Hugging Face",
            "url": "https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct"
          },
          {
            "title": "meta-llama/Llama-3.2-1B · Hugging Face",
            "url": "https://huggingface.co/meta-llama/Llama-3.2-1B"
          },
          {
            "title": "meta-llama/Llama-3.2-3B · Hugging Face",
            "url": "https://huggingface.co/meta-llama/Llama-3.2-3B"
          },
          {
            "title": "Wan2.1-T2V-1.3B-Q4_K_M.gguf · samuelchristlie/Wan2.1-T2V-1.3B-GGUF at 5a512b15fc35d1b67a074cfe55a591be9e9ef9b5",
            "url": "https://huggingface.co/samuelchristlie/Wan2.1-T2V-1.3B-GGUF/blob/5a512b15fc35d1b67a074cfe55a591be9e9ef9b5/Wan2.1-T2V-1.3B-Q4_K_M.gguf"
          }
        ]
      },
      "Based on the search results, I found relevant information about m-a-p's 1.3B and linear attention research:\n\n## Key Findings\n\nThe m-a-p organization maintains a collection featuring all 1.3B & 340M hybrid linear-attention experiments.\n\nThey trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios.\n\nWhile linear models often suffer from limited recall performance, leading to hybrid architectures that combine linear and full attention layers, the choice of linear attention component has not been deeply explored.\n\nThe research highlights selective gating, hierarchical recurrence, and controlled forgetting as critical for effective hybrid models, and recommends architectures such as HGRN-2 or GatedDeltaNet with a linear-to-full ratio between 3:1 and 6:1 to achieve Transformer-level recall efficiently.\n\nThe collection and research is available at the Hugging Face model hub under the m-a-p organization."
    ],
    "durationSeconds": 6.572586757000001
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T07:26:22.370Z_

<details><summary>↩ Tool result · `toolu_01B4JFvmvbJBXZpgc8xn81aH`</summary>

```text
Web search results for query: "Wang et al "hybrid linear attention" 1.3B model arXiv 2507.06457"

Links: [{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/pdf/2507.06457"},{"title":"[2507.06457v1] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457v1"},{"title":"Paper page - A Systematic Analysis of Hybrid Linear Attention","url":"https://huggingface.co/papers/2507.06457"},{"title":"(PDF) A Systematic Analysis of Hybrid Linear Attention","url":"https://www.researchgate.net/publication/393538945_A_Systematic_Analysis_of_Hybrid_Linear_Attention"},{"title":"Hybrid Linear Attention Done Right: Efficient Distillation ...","url":"https://arxiv.org/pdf/2601.22156"},{"title":"A Systematic Analysis of Hybrid Linear Attention | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/systematic-analysis-hybrid-linear-attention"},{"title":"Alleviating Forgetfulness of Linear Attention by Hybrid Sparse Attention and Contextualized Learnable Token Eviction","url":"https://arxiv.org/html/2510.20787v2"},{"title":"(PDF) Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts","url":"https://www.researchgate.net/publication/400236907_Hybrid_Linear_Attention_Done_Right_Efficient_Distillation_and_Effective_Architectures_for_Extremely_Long_Contexts"},{"title":"Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts","url":"https://arxiv.org/html/2601.22156v1"}]

I found the paper! Here's what the search results show about the Wang et al. paper on hybrid linear attention:

## Paper Overview

"A Systematic Analysis of Hybrid Linear Attention" is by Dustin Wang and 10 other authors, published on arXiv as 2507.06457.

## Research Focus

The paper addresses how Transformers face quadratic complexity and memory issues with long sequences, and proposes using linear attention mechanisms with fixed-size hidden states. However, linear models often suffer from limited recall performance, leading to hybrid architectures that combine linear and full attention layers.

## Key Methodology

The researchers trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios.

## Main Findings

Benchmarking on standard language modeling and recall tasks reveals that superior standalone linear models do not necessarily excel in hybrids. Additionally, language modeling remains stable across linear-to-full attention ratios, while recall significantly improves with increased full attention layers, particularly below a 3:1 ratio.

## Recommendations

The authors recommend architectures such as HGRN-2 or GatedDeltaNet with a linear-to-full ratio between 3:1 and 6:1 to achieve Transformer-level recall efficiently.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "a6291c89-e497-4660-a1d2-af76327c44c7",
  "tool_use_result": {
    "query": "Wang et al \"hybrid linear attention\" 1.3B model arXiv 2507.06457",
    "results": [
      {
        "tool_use_id": "srvtoolu_018iBAfsVAyPmPGo7mFbo2xG",
        "content": [
          {
            "title": "[2507.06457] A Systematic Analysis of Hybrid Linear Attention",
            "url": "https://arxiv.org/abs/2507.06457"
          },
          {
            "title": "A Systematic Analysis of Hybrid Linear Attention",
            "url": "https://arxiv.org/pdf/2507.06457"
          },
          {
            "title": "[2507.06457v1] A Systematic Analysis of Hybrid Linear Attention",
            "url": "https://arxiv.org/abs/2507.06457v1"
          },
          {
            "title": "Paper page - A Systematic Analysis of Hybrid Linear Attention",
            "url": "https://huggingface.co/papers/2507.06457"
          },
          {
            "title": "(PDF) A Systematic Analysis of Hybrid Linear Attention",
            "url": "https://www.researchgate.net/publication/393538945_A_Systematic_Analysis_of_Hybrid_Linear_Attention"
          },
          {
            "title": "Hybrid Linear Attention Done Right: Efficient Distillation ...",
            "url": "https://arxiv.org/pdf/2601.22156"
          },
          {
            "title": "A Systematic Analysis of Hybrid Linear Attention | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/systematic-analysis-hybrid-linear-attention"
          },
          {
            "title": "Alleviating Forgetfulness of Linear Attention by Hybrid Sparse Attention and Contextualized Learnable Token Eviction",
            "url": "https://arxiv.org/html/2510.20787v2"
          },
          {
            "title": "(PDF) Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts",
            "url": "https://www.researchgate.net/publication/400236907_Hybrid_Linear_Attention_Done_Right_Efficient_Distillation_and_Effective_Architectures_for_Extremely_Long_Contexts"
          },
          {
            "title": "Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts",
            "url": "https://arxiv.org/html/2601.22156v1"
          }
        ]
      },
      "I found the paper! Here's what the search results show about the Wang et al. paper on hybrid linear attention:\n\n## Paper Overview\n\n\"A Systematic Analysis of Hybrid Linear Attention\" is by Dustin Wang and 10 other authors, published on arXiv as 2507.06457.\n\n## Research Focus\n\nThe paper addresses how Transformers face quadratic complexity and memory issues with long sequences, and proposes using linear attention mechanisms with fixed-size hidden states. However, linear models often suffer from limited recall performance, leading to hybrid architectures that combine linear and full attention layers.\n\n## Key Methodology\n\nThe researchers trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios.\n\n## Main Findings\n\nBenchmarking on standard language modeling and recall tasks reveals that superior standalone linear models do not necessarily excel in hybrids. Additionally, language modeling remains stable across linear-to-full attention ratios, while recall significantly improves with increased full attention layers, particularly below a 3:1 ratio.\n\n## Recommendations\n\nThe authors recommend architectures such as HGRN-2 or GatedDeltaNet with a linear-to-full ratio between 3:1 and 6:1 to achieve Transformer-level recall efficiently."
    ],
    "durationSeconds": 9.330200806
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T07:26:28.859Z_

<details><summary>↩ Tool result · `toolu_01J9gwftt2JncE2XEk71q3ds`</summary>

```text
# Hybrid Linear Attention Research - Complete Model Inventory

## Collection Overview
- **Total Models**: 58 models
- **Sizes**: 340M (0.3-0.4B) and 1.3B (1B)
- **Training Data**: 20B tokens (340M) and 100B tokens (1.3B)
- **Last Updated**: Sep 11, 2025

---

## 340M Models (20B Tokens)

| Model Name | Size | Architecture | Hybrid Ratio | Details |
|---|---|---|---|---|
| 340M-20B-GatedDeltaNet-hybrid-3-1 | 0.4B | GatedDeltaNet | 3:1 | Updated Mar 3, 2025 |
| 340M-20B-GatedDeltaNet-hybrid-6-1 | 0.4B | GatedDeltaNet | 6:1 | Updated Mar 3, 2025 |
| 340M-20B-GatedDeltaNet-hybrid-12-1 | 0.4B | GatedDeltaNet | 12:1 | Updated May 10, 2025 |
| 340M-20B-GatedDeltaNet-pure-baseline | 0.4B | GatedDeltaNet | Pure | Updated Jun 7, 2025 • **9 downloads** |
| 340M-20B-GatedDeltaNet-New-hybrid-24-1 | 0.4B | GatedDeltaNet | 24:1 | Updated Jun 10, 2025 |
| 340M-20B-GLA-hybrid-6-1 | 0.3B | GLA | 6:1 | Updated Mar 3, 2025 |
| 340M-20B-GLA-hybrid-3-1 | 0.3B | GLA | 3:1 | Updated Mar 3, 2025 |
| 340M-20B-GLA-hybrid-12-1 | 0.3B | GLA | 12:1 | Updated Mar 3, 2025 |
| 340M-20B-GLA-hybrid-24-1 | 0.3B | GLA | 24:1 | Updated Mar 3, 2025 • **7 downloads** |
| 340M-20B-GLA-pure-baseline | 0.3B | GLA | Pure | Updated May 10, 2025 |
| 340M-20B-HGRN2-pure-baseline | 0.3B | HGRN2 | Pure | Updated Mar 3, 2025 • **5 downloads** |
| 340M-20B-HGRN2-hybrid-6-1 | 0.3B | HGRN2 | 6:1 | Updated Mar 3, 2025 |
| 340M-20B-HGRN2-hybrid-3-1 | 0.3B | HGRN2 | 3:1 | Updated Mar 3, 2025 • **20 downloads** |
| 340M-20B-HGRN2-hybrid-12-1 | 0.3B | HGRN2 | 12:1 | Updated Mar 4, 2025 |
| 340M-20B-HGRN2-hybrid-24-1 | 0.3B | HGRN2 | 24:1 | Updated Mar 4, 2025 |
| 340M-20B-HGRN-hybrid-3-1 | 0.3B | HGRN | 3:1 | Updated Apr 20, 2025 |
| 340M-20B-HGRN-hybrid-6-1 | 0.3B | HGRN | 6:1 | Updated Apr 20, 2025 |
| 340M-20B-HGRN-hybrid-12-1 | 0.3B | HGRN | 12:1 | Updated Apr 20, 2025 |
| 340M-20B-HGRN-hybrid-24-1 | 0.3B | HGRN | 24:1 | Updated Apr 20, 2025 |
| 340M-20B-HGRN-pure-baseline | 0.3B | HGRN | Pure | Updated Apr 20, 2025 |
| 340M-20B-DeltaNet-hybrid-3-1 | 0.3B | DeltaNet | 3:1 | Updated Mar 4, 2025 • **8 downloads** |
| 340M-20B-DeltaNet-pure | 0.3B | DeltaNet | Pure | Updated Mar 4, 2025 • **38 downloads** |
| 340M-20B-DeltaNet-hybrid-6-1 | 0.3B | DeltaNet | 6:1 | Updated Mar 4, 2025 |
| 340M-20B-DeltaNet-hybrid-12-1 | 0.3B | DeltaNet | 12:1 | Updated Mar 4, 2025 |
| 340M-20B-DeltaNet-hybrid-24-1 | 0.3B | DeltaNet | 24:1 | Updated Mar 4, 2025 |
| 340M-20B-RetNet-hybrid-24-1 | 0.3B | RetNet | 24:1 | Updated Mar 4, 2025 |
| 340M-20B-RetNet-hybrid-12-1 | 0.3B | RetNet | 12:1 | Updated Mar 4, 2025 |
| 340M-20B-RetNet-hybrid-6-1 | 0.3B | RetNet | 6:1 | Updated Mar 4, 2025 |
| 340M-20B-RetNet-hybrid-3-1 | 0.3B | RetNet | 3:1 | Updated Mar 4, 2025 |
| 340M-20B-RetNet-pure | 0.3B | RetNet | Pure | Updated Mar 4, 2025 |
| transformer_340M_baseline | 0.3B | Transformer | Baseline | Updated Sep 11, 2025 • **8 downloads** |

---

## 1.3B Models (100B Tokens)

| Model Name | Size | Architecture | Hybrid Ratio | Details |
|---|---|---|---|---|
| 1.3B-100B-GatedDeltaNet-hybrid-3-1 | 1B | GatedDeltaNet | 3:1 | Updated Apr 20, 2025 • **14 downloads** |
| 1.3B-100B-GatedDeltaNet-hybrid-6-1 | 1B | GatedDeltaNet | 6:1 | Updated Apr 20, 2025 • **9 downloads** |
| 1.3B-100B-GatedDeltaNet-hybrid-12-1 | 1B | GatedDeltaNet | 12:1 | Updated Apr 20, 2025 |
| 1.3B-100B-GatedDeltaNet-hybrid-24-1 | 1B | GatedDeltaNet | 24:1 | Updated Apr 20, 2025 |
| 1.3B-100B-GatedDeltaNet-pure | 1B | GatedDeltaNet | Pure | Updated May 10, 2025 • **1.57k downloads** ⭐ |
| 1.3B-100B-GLA-hybrid-3-1 | 1B | GLA | 3:1 | Updated Apr 20, 2025 • **55 downloads** |
| 1.3B-100B-GLA-hybrid-6-1 | 1B | GLA | 6:1 | Updated Apr 20, 2025 |
| 1.3B-100B-GLA-hybrid-12-1 | 1B | GLA | 12:1 | Updated Apr 20, 2025 |
| 1.3B-100B-GLA-hybrid-24-1 | 1B | GLA | 24:1 | Updated Apr 20, 2025 |
| 1.3B-100B-GLA-pure | 1B | GLA | Pure | Updated Apr 20, 2025 • **557 downloads** ⭐ |
| 1.3B-100B-HGRN2-hybrid-3-1 | 1B | HGRN2 | 3:1 | Updated Apr 20, 2025 |
| 1.3B-100B-HGRN2-hybrid-6-1 | 1B | HGRN2 | 6:1 | Updated Apr 20, 2025 • **7 downloads** |
| 1.3B-100B-HGRN2-hybrid-12-1 | 1B | HGRN2 | 12:1 | Updated Apr 20, 2025 • **10 downloads** |
| 1.3B-100B-HGRN2-hybrid-24-1 | 1B | HGRN2 | 24:1 | Updated Apr 20, 2025 |
| 1.3B-100B-HGRN2-pure | 1B | HGRN2 | Pure | Updated May 10, 2025 |
| 1.3B-100B-HGRN-hybrid-3-1 | 1B | HGRN | 3:1 | Updated Apr 20, 2025 |
| 1.3B-100B-HGRN-hybrid-6-1 | 1B | HGRN | 6:1 | Updated Apr 20, 2025 |
| 1.3B-100B-HGRN-hybrid-12-1 | 1B | HGRN | 12:1 | Updated Apr 20, 2025 |
| 1.3B-100B-HGRN-hybrid-24-1 | 1B | HGRN | 24:1 | Updated Apr 20, 2025 • **25 downloads** |
| 1.3B-100B-HGRN-pure | 1B | HGRN | Pure | Updated Apr 20, 2025 • **5 downloads** |
| 1.3B-100B-DeltaNet-hybrid-3-1 | 1B | DeltaNet | 3:1 | Updated Jun 7, 2025 • **5 downloads** |
| 1.3B-100B-DeltaNet-hybrid-6-1 | 1B | DeltaNet | 6:1 | Updated Jun 7, 2025 |
| 1.3B-100B-DeltaNet-hybrid-12-1 | 1B | DeltaNet | 12:1 | Updated Jun 7, 2025 • **5 downloads** |
| 1.3B-100B-DeltaNet-hybrid-24-1 | 1B | DeltaNet | 24:1 | Updated Jun 7, 2025 • **6 downloads** |
| 1.3B-100B-DeltaNet-pure | 1B | DeltaNet | Pure | Updated Jun 7, 2025 • **516 downloads** ⭐ |
| 1.3B-100B-RetNet-hybrid-3-1 | 1B | RetNet | 3:1 | Updated Apr 20, 2025 • **16 downloads** |
| 1.3B-100B-RetNet-hybrid-6-1 | 1B | RetNet | 6:1 | Updated Apr 20, 2025 |
| 1.3B-100B-RetNet-hybrid-12-1 | 1B | RetNet | 12:1 | Updated Apr 20, 2025 |
| 1.3B-100B-RetNet-hybrid-24-1 | 1B | RetNet | 24:1 | Updated Apr 20, 2025 • **7 downloads** |
| 1.3B-100B-RetNet-pure | 1B | RetNet | Pure | Updated Apr 20, 2025 • **519 downloads** ⭐ |
| transformer_1.3B_baseline | 1B | Transformer | Baseline | Updated Sep 11, 2025 • **683 downloads** ⭐ |

---

## Key Insights

**Most Popular Models:**
- `transformer_1.3B_baseline` - 683 downloads
- `1.3B-100B-GatedDeltaNet-pure` - 1.57k downloads
- `1.3B-100B-GLA-pure` - 557 downloads
- `1.3B-100B-DeltaNet-pure` - 516 downloads

**Architecture Types:** GatedDeltaNet, GLA, HGRN2, HGRN, DeltaNet, RetNet, Transformer

**Hybrid Ratios:** 3:1, 6:1, 12:1, 24:1 (attention-to-linear layer ratios), plus "Pure" baselines
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "85c2e04a-21b7-4b91-b3cb-4b720e78bfb6",
  "tool_use_result": {
    "bytes": 314385,
    "code": 200,
    "codeText": "OK",
    "result": "# Hybrid Linear Attention Research - Complete Model Inventory\n\n## Collection Overview\n- **Total Models**: 58 models\n- **Sizes**: 340M (0.3-0.4B) and 1.3B (1B)\n- **Training Data**: 20B tokens (340M) and 100B tokens (1.3B)\n- **Last Updated**: Sep 11, 2025\n\n---\n\n## 340M Models (20B Tokens)\n\n| Model Name | Size | Architecture | Hybrid Ratio | Details |\n|---|---|---|---|---|\n| 340M-20B-GatedDeltaNet-hybrid-3-1 | 0.4B | GatedDeltaNet | 3:1 | Updated Mar 3, 2025 |\n| 340M-20B-GatedDeltaNet-hybrid-6-1 | 0.4B | GatedDeltaNet | 6:1 | Updated Mar 3, 2025 |\n| 340M-20B-GatedDeltaNet-hybrid-12-1 | 0.4B | GatedDeltaNet | 12:1 | Updated May 10, 2025 |\n| 340M-20B-GatedDeltaNet-pure-baseline | 0.4B | GatedDeltaNet | Pure | Updated Jun 7, 2025 • **9 downloads** |\n| 340M-20B-GatedDeltaNet-New-hybrid-24-1 | 0.4B | GatedDeltaNet | 24:1 | Updated Jun 10, 2025 |\n| 340M-20B-GLA-hybrid-6-1 | 0.3B | GLA | 6:1 | Updated Mar 3, 2025 |\n| 340M-20B-GLA-hybrid-3-1 | 0.3B | GLA | 3:1 | Updated Mar 3, 2025 |\n| 340M-20B-GLA-hybrid-12-1 | 0.3B | GLA | 12:1 | Updated Mar 3, 2025 |\n| 340M-20B-GLA-hybrid-24-1 | 0.3B | GLA | 24:1 | Updated Mar 3, 2025 • **7 downloads** |\n| 340M-20B-GLA-pure-baseline | 0.3B | GLA | Pure | Updated May 10, 2025 |\n| 340M-20B-HGRN2-pure-baseline | 0.3B | HGRN2 | Pure | Updated Mar 3, 2025 • **5 downloads** |\n| 340M-20B-HGRN2-hybrid-6-1 | 0.3B | HGRN2 | 6:1 | Updated Mar 3, 2025 |\n| 340M-20B-HGRN2-hybrid-3-1 | 0.3B | HGRN2 | 3:1 | Updated Mar 3, 2025 • **20 downloads** |\n| 340M-20B-HGRN2-hybrid-12-1 | 0.3B | HGRN2 | 12:1 | Updated Mar 4, 2025 |\n| 340M-20B-HGRN2-hybrid-24-1 | 0.3B | HGRN2 | 24:1 | Updated Mar 4, 2025 |\n| 340M-20B-HGRN-hybrid-3-1 | 0.3B | HGRN | 3:1 | Updated Apr 20, 2025 |\n| 340M-20B-HGRN-hybrid-6-1 | 0.3B | HGRN | 6:1 | Updated Apr 20, 2025 |\n| 340M-20B-HGRN-hybrid-12-1 | 0.3B | HGRN | 12:1 | Updated Apr 20, 2025 |\n| 340M-20B-HGRN-hybrid-24-1 | 0.3B | HGRN | 24:1 | Updated Apr 20, 2025 |\n| 340M-20B-HGRN-pure-baseline | 0.3B | HGRN | Pure | Updated Apr 20, 2025 |\n| 340M-20B-DeltaNet-hybrid-3-1 | 0.3B | DeltaNet | 3:1 | Updated Mar 4, 2025 • **8 downloads** |\n| 340M-20B-DeltaNet-pure | 0.3B | DeltaNet | Pure | Updated Mar 4, 2025 • **38 downloads** |\n| 340M-20B-DeltaNet-hybrid-6-1 | 0.3B | DeltaNet | 6:1 | Updated Mar 4, 2025 |\n| 340M-20B-DeltaNet-hybrid-12-1 | 0.3B | DeltaNet | 12:1 | Updated Mar 4, 2025 |\n| 340M-20B-DeltaNet-hybrid-24-1 | 0.3B | DeltaNet | 24:1 | Updated Mar 4, 2025 |\n| 340M-20B-RetNet-hybrid-24-1 | 0.3B | RetNet | 24:1 | Updated Mar 4, 2025 |\n| 340M-20B-RetNet-hybrid-12-1 | 0.3B | RetNet | 12:1 | Updated Mar 4, 2025 |\n| 340M-20B-RetNet-hybrid-6-1 | 0.3B | RetNet | 6:1 | Updated Mar 4, 2025 |\n| 340M-20B-RetNet-hybrid-3-1 | 0.3B | RetNet | 3:1 | Updated Mar 4, 2025 |\n| 340M-20B-RetNet-pure | 0.3B | RetNet | Pure | Updated Mar 4, 2025 |\n| transformer_340M_baseline | 0.3B | Transformer | Baseline | Updated Sep 11, 2025 • **8 downloads** |\n\n---\n\n## 1.3B Models (100B Tokens)\n\n| Model Name | Size | Architecture | Hybrid Ratio | Details |\n|---|---|---|---|---|\n| 1.3B-100B-GatedDeltaNet-hybrid-3-1 | 1B | GatedDeltaNet | 3:1 | Updated Apr 20, 2025 • **14 downloads** |\n| 1.3B-100B-GatedDeltaNet-hybrid-6-1 | 1B | GatedDeltaNet | 6:1 | Updated Apr 20, 2025 • **9 downloads** |\n| 1.3B-100B-GatedDeltaNet-hybrid-12-1 | 1B | GatedDeltaNet | 12:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-GatedDeltaNet-hybrid-24-1 | 1B | GatedDeltaNet | 24:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-GatedDeltaNet-pure | 1B | GatedDeltaNet | Pure | Updated May 10, 2025 • **1.57k downloads** ⭐ |\n| 1.3B-100B-GLA-hybrid-3-1 | 1B | GLA | 3:1 | Updated Apr 20, 2025 • **55 downloads** |\n| 1.3B-100B-GLA-hybrid-6-1 | 1B | GLA | 6:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-GLA-hybrid-12-1 | 1B | GLA | 12:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-GLA-hybrid-24-1 | 1B | GLA | 24:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-GLA-pure | 1B | GLA | Pure | Updated Apr 20, 2025 • **557 downloads** ⭐ |\n| 1.3B-100B-HGRN2-hybrid-3-1 | 1B | HGRN2 | 3:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-HGRN2-hybrid-6-1 | 1B | HGRN2 | 6:1 | Updated Apr 20, 2025 • **7 downloads** |\n| 1.3B-100B-HGRN2-hybrid-12-1 | 1B | HGRN2 | 12:1 | Updated Apr 20, 2025 • **10 downloads** |\n| 1.3B-100B-HGRN2-hybrid-24-1 | 1B | HGRN2 | 24:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-HGRN2-pure | 1B | HGRN2 | Pure | Updated May 10, 2025 |\n| 1.3B-100B-HGRN-hybrid-3-1 | 1B | HGRN | 3:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-HGRN-hybrid-6-1 | 1B | HGRN | 6:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-HGRN-hybrid-12-1 | 1B | HGRN | 12:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-HGRN-hybrid-24-1 | 1B | HGRN | 24:1 | Updated Apr 20, 2025 • **25 downloads** |\n| 1.3B-100B-HGRN-pure | 1B | HGRN | Pure | Updated Apr 20, 2025 • **5 downloads** |\n| 1.3B-100B-DeltaNet-hybrid-3-1 | 1B | DeltaNet | 3:1 | Updated Jun 7, 2025 • **5 downloads** |\n| 1.3B-100B-DeltaNet-hybrid-6-1 | 1B | DeltaNet | 6:1 | Updated Jun 7, 2025 |\n| 1.3B-100B-DeltaNet-hybrid-12-1 | 1B | DeltaNet | 12:1 | Updated Jun 7, 2025 • **5 downloads** |\n| 1.3B-100B-DeltaNet-hybrid-24-1 | 1B | DeltaNet | 24:1 | Updated Jun 7, 2025 • **6 downloads** |\n| 1.3B-100B-DeltaNet-pure | 1B | DeltaNet | Pure | Updated Jun 7, 2025 • **516 downloads** ⭐ |\n| 1.3B-100B-RetNet-hybrid-3-1 | 1B | RetNet | 3:1 | Updated Apr 20, 2025 • **16 downloads** |\n| 1.3B-100B-RetNet-hybrid-6-1 | 1B | RetNet | 6:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-RetNet-hybrid-12-1 | 1B | RetNet | 12:1 | Updated Apr 20, 2025 |\n| 1.3B-100B-RetNet-hybrid-24-1 | 1B | RetNet | 24:1 | Updated Apr 20, 2025 • **7 downloads** |\n| 1.3B-100B-RetNet-pure | 1B | RetNet | Pure | Updated Apr 20, 2025 • **519 downloads** ⭐ |\n| transformer_1.3B_baseline | 1B | Transformer | Baseline | Updated Sep 11, 2025 • **683 downloads** ⭐ |\n\n---\n\n## Key Insights\n\n**Most Popular Models:**\n- `transformer_1.3B_baseline` - 683 downloads\n- `1.3B-100B-GatedDeltaNet-pure` - 1.57k downloads\n- `1.3B-100B-GLA-pure` - 557 downloads\n- `1.3B-100B-DeltaNet-pure` - 516 downloads\n\n**Architecture Types:** GatedDeltaNet, GLA, HGRN2, HGRN, DeltaNet, RetNet, Transformer\n\n**Hybrid Ratios:** 3:1, 6:1, 12:1, 24:1 (attention-to-linear layer ratios), plus \"Pure\" baselines",
    "durationMs": 16713,
    "url": "https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e"
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Excellent! The collection has 1.3B models. Now let me get more details - I need to check a specific 1.3B model page for file sizes and architecture parameters, and also check the paper for ICL/function composition evaluation results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "56217773-7e52-486c-8900-96ef37d1aa22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShaDxEVCDJQsHYDe3gT3Es",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2669,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 25815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
      },
      "output_tokens": 28,
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

_source line 17_

1.3B 模型确认存在。让我获取具体模型的文件大小和架构参数，以及论文中关于 ICL 的评估结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "ef93d945-f73b-41a8-a5b0-680f00f62487",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShaDxEVCDJQsHYDe3gT3Es",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2669,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 25815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
      },
      "output_tokens": 28,
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

_source line 18_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Etfgzj6jo5L8xR4U3FSCxB`</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1",
  "prompt": "Extract: 1) All file sizes (especially safetensors files and total model size), 2) Model architecture parameters from config.json (hidden_size, num_layers, num_attention_heads, intermediate_size, vocab_size, etc.), 3) Any model card information about training data, architecture details, or usage instructions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "f8c6ff30-5b6c-4f17-b871-a99fa501decc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShaDxEVCDJQsHYDe3gT3Es",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2669,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 25815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
      },
      "output_tokens": 28,
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

_source line 19_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Sw5hTu2VDZ8t5U92KWCLxq`</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/transformer_1.3B_baseline",
  "prompt": "Extract: 1) All file sizes (especially safetensors files and total model size), 2) Model architecture parameters from config.json (hidden_size, num_layers, num_attention_heads, intermediate_size, vocab_size, etc.), 3) Any model card information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "0fec737b-ed43-4599-97fb-3de217781cfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShaDxEVCDJQsHYDe3gT3Es",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2669,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 25815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
      },
      "output_tokens": 28,
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

_source line 20_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FubKUr2uaNzSY411WEBVgG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.06457",
  "prompt": "Extract all information about: 1) In-context learning (ICL) evaluation or experiments, 2) Function composition tasks, 3) Recall tasks and results, 4) Model architecture details for 1.3B models (hidden_size, num_layers, etc.), 5) What benchmarks/tasks were used for evaluation, 6) Any findings about how model scale affects performance on recall or ICL tasks. List all evaluation tasks mentioned in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "d56c3f25-9db4-4760-8431-42a5eb9d29c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShaDxEVCDJQsHYDe3gT3Es",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2669,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 25815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
      },
      "output_tokens": 28,
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

_source line 21 · 2026-05-18T07:26:41.257Z_

<details><summary>↩ Tool result · `toolu_01Sw5hTu2VDZ8t5U92KWCLxq`</summary>

````text
# Model Information: m-a-p/transformer_1.3B_baseline

## File Sizes
- **Total Model Size:** 1B parameters
- **Format:** Safetensors
- **Tensor Type:** F32 (32-bit floating point)
- **Downloads (last month):** 683

*Note: Specific individual file sizes are not listed on the provided page content.*

## Model Architecture Parameters
The page content does not include access to the `config.json` file. To retrieve architecture parameters (hidden_size, num_layers, num_attention_heads, intermediate_size, vocab_size, etc.), you would need to:

1. Visit the model's "Files" section directly
2. Access the config.json file in the repository
3. Or use the Hugging Face API:

```python
from transformers import AutoConfig

config = AutoConfig.from_pretrained("m-a-p/transformer_1.3B_baseline")
print(config)
```

## Model Card Information
- **No model card available** - The page explicitly states "No model card"

## Additional Context
This model is part of the **"Hybrid Linear Attention Research"** collection (62 items, updated Sep 11, 2025), suggesting it's a research model exploring hybrid linear-attention mechanisms with 1.3B and 340M parameter variants.

To access complete architecture details, visit: https://huggingface.co/m-a-p/transformer_1.3B_baseline
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "aa313ec4-94e0-436e-a15e-f4107f73bfd9",
  "tool_use_result": {
    "bytes": 95304,
    "code": 200,
    "codeText": "OK",
    "result": "# Model Information: m-a-p/transformer_1.3B_baseline\n\n## File Sizes\n- **Total Model Size:** 1B parameters\n- **Format:** Safetensors\n- **Tensor Type:** F32 (32-bit floating point)\n- **Downloads (last month):** 683\n\n*Note: Specific individual file sizes are not listed on the provided page content.*\n\n## Model Architecture Parameters\nThe page content does not include access to the `config.json` file. To retrieve architecture parameters (hidden_size, num_layers, num_attention_heads, intermediate_size, vocab_size, etc.), you would need to:\n\n1. Visit the model's \"Files\" section directly\n2. Access the config.json file in the repository\n3. Or use the Hugging Face API:\n\n```python\nfrom transformers import AutoConfig\n\nconfig = AutoConfig.from_pretrained(\"m-a-p/transformer_1.3B_baseline\")\nprint(config)\n```\n\n## Model Card Information\n- **No model card available** - The page explicitly states \"No model card\"\n\n## Additional Context\nThis model is part of the **\"Hybrid Linear Attention Research\"** collection (62 items, updated Sep 11, 2025), suggesting it's a research model exploring hybrid linear-attention mechanisms with 1.3B and 340M parameter variants.\n\nTo access complete architecture details, visit: https://huggingface.co/m-a-p/transformer_1.3B_baseline",
    "durationMs": 3782,
    "url": "https://huggingface.co/m-a-p/transformer_1.3B_baseline"
  }
}
````

</details>

---

### Tool result

_source line 22 · 2026-05-18T07:26:43.873Z_

<details><summary>↩ Tool result · `toolu_01Etfgzj6jo5L8xR4U3FSCxB`</summary>

```text
# Model Information: m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1

Based on the web page content provided, here's what I can extract:

## File Sizes
- **Model size**: 1B params (1 billion parameters)
- **Tensor type**: F32 (32-bit floating point)
- **Format**: Safetensors
- **Downloads last month**: 14

## Model Architecture Parameters
Unfortunately, the webpage content does **not include** the detailed configuration from `config.json`. The following parameters are **not available** in the provided content:
- `hidden_size`
- `num_layers`
- `num_attention_heads`
- `intermediate_size`
- `vocab_size`
- Other architectural details

## Model Card Information
- **No model card available** - The page explicitly states "No model card"
- **Architecture type**: GatedDeltaNet (hybrid linear attention model)
- **Collection**: Part of "Hybrid Linear Attention Research" collection (62 items)
- **Organization**: Multimodal Art Projection (m-a-p)

## Limitations
To access the complete architectural parameters and training details, you would need to:
1. Visit the model's Files section to download and inspect `config.json`
2. Check the GitHub repository linked in the footer
3. Review the collection page for related documentation

The model appears to be a hybrid linear-attention architecture experiment, but comprehensive documentation is not publicly displayed on this landing page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "1ab63d95-ee96-4470-bf24-a2da98471aff",
  "tool_use_result": {
    "bytes": 95463,
    "code": 200,
    "codeText": "OK",
    "result": "# Model Information: m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1\n\nBased on the web page content provided, here's what I can extract:\n\n## File Sizes\n- **Model size**: 1B params (1 billion parameters)\n- **Tensor type**: F32 (32-bit floating point)\n- **Format**: Safetensors\n- **Downloads last month**: 14\n\n## Model Architecture Parameters\nUnfortunately, the webpage content does **not include** the detailed configuration from `config.json`. The following parameters are **not available** in the provided content:\n- `hidden_size`\n- `num_layers`\n- `num_attention_heads`\n- `intermediate_size`\n- `vocab_size`\n- Other architectural details\n\n## Model Card Information\n- **No model card available** - The page explicitly states \"No model card\"\n- **Architecture type**: GatedDeltaNet (hybrid linear attention model)\n- **Collection**: Part of \"Hybrid Linear Attention Research\" collection (62 items)\n- **Organization**: Multimodal Art Projection (m-a-p)\n\n## Limitations\nTo access the complete architectural parameters and training details, you would need to:\n1. Visit the model's Files section to download and inspect `config.json`\n2. Check the GitHub repository linked in the footer\n3. Review the collection page for related documentation\n\nThe model appears to be a hybrid linear-attention architecture experiment, but comprehensive documentation is not publicly displayed on this landing page.",
    "durationMs": 7348,
    "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T07:26:48.217Z_

<details><summary>↩ Tool result · `toolu_01FubKUr2uaNzSY411WEBVgG`</summary>

```text
# Analysis of arXiv:2507.06457 - Hybrid Linear Attention

Based on the provided webpage content, here's what can be extracted:

## 1) In-Context Learning (ICL) Evaluation
**Not mentioned** in the abstract or available content.

## 2) Function Composition Tasks
**Not mentioned** in the available excerpts.

## 3) Recall Tasks and Results
The paper includes recall task evaluation. Key finding: "recall significantly improves with increased full attention layers, particularly below a 3:1 ratio" between linear and full attention components. The study emphasizes that "Transformer-level recall" can be achieved efficiently with recommended architectures at specific ratios.

## 4) Model Architecture Details for 1.3B Models
Specific hidden sizes and layer counts are **not provided** in the abstract. Only that models were trained at "1.3B parameters (100B tokens)."

## 5) Benchmarks/Tasks Used
The abstract mentions: "standard language modeling and recall tasks"

## 6) Scale Effects on Performance
The paper trained 72 models across two scales (340M and 1.3B parameters) but detailed comparative findings on scale effects aren't explicit in the abstract provided.

## All Evaluation Tasks Listed
1. Language modeling
2. Recall tasks

**Note:** The full paper details are behind the PDF, so comprehensive architectural specifications and complete evaluation methodologies would require accessing the complete document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "e2e6a246-50e7-48c0-a479-6a839cad86e5",
  "tool_use_result": {
    "bytes": 47947,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv:2507.06457 - Hybrid Linear Attention\n\nBased on the provided webpage content, here's what can be extracted:\n\n## 1) In-Context Learning (ICL) Evaluation\n**Not mentioned** in the abstract or available content.\n\n## 2) Function Composition Tasks\n**Not mentioned** in the available excerpts.\n\n## 3) Recall Tasks and Results\nThe paper includes recall task evaluation. Key finding: \"recall significantly improves with increased full attention layers, particularly below a 3:1 ratio\" between linear and full attention components. The study emphasizes that \"Transformer-level recall\" can be achieved efficiently with recommended architectures at specific ratios.\n\n## 4) Model Architecture Details for 1.3B Models\nSpecific hidden sizes and layer counts are **not provided** in the abstract. Only that models were trained at \"1.3B parameters (100B tokens).\"\n\n## 5) Benchmarks/Tasks Used\nThe abstract mentions: \"standard language modeling and recall tasks\"\n\n## 6) Scale Effects on Performance\nThe paper trained 72 models across two scales (340M and 1.3B parameters) but detailed comparative findings on scale effects aren't explicit in the abstract provided.\n\n## All Evaluation Tasks Listed\n1. Language modeling\n2. Recall tasks\n\n**Note:** The full paper details are behind the PDF, so comprehensive architectural specifications and complete evaluation methodologies would require accessing the complete document.",
    "durationMs": 8118,
    "url": "https://arxiv.org/abs/2507.06457"
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Let me get more details from the paper itself - especially about evaluation tasks, and check config.json for a 1.3B model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "50bdec4e-46a0-4db3-9332-f547f6690b9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dy69RLeJwTxWyX1jeQUMWS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 29585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4460
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

让我获取论文全文中的评估细节和 1.3B 模型的 config.json。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "f9838b12-d0bc-4706-88d2-28bdf425a336",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dy69RLeJwTxWyX1jeQUMWS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 29585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4460
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

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xev3kCzA5sYJc2Hr7vHAd5`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.06457v1",
  "prompt": "Extract ALL evaluation tasks and benchmarks mentioned in this paper. Specifically look for: 1) Any mention of \"in-context learning\", \"ICL\", \"function composition\", \"compositional\", \"few-shot\" tasks. 2) The complete list of recall tasks used (e.g., MQAR, associative recall, etc.). 3) The complete list of language modeling benchmarks. 4) Model architecture details for both 340M and 1.3B (hidden_size, num_layers, num_heads, intermediate_size). 5) Any discussion about how model scale affects recall or ICL capabilities. 6) Table of results if available. Be thorough - scan the entire paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "079479fa-1bc2-43d3-939f-f05215a8ff27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dy69RLeJwTxWyX1jeQUMWS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 29585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4460
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

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Cyb5H1wz5wK2avqMaWoHAg`</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/raw/main/config.json",
  "prompt": "Extract the complete config.json content - all architecture parameters including hidden_size, num_hidden_layers, num_attention_heads, intermediate_size, vocab_size, max_position_embeddings, and any other parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "c358bdfe-18ae-4b71-92cd-9b82a0267677",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dy69RLeJwTxWyX1jeQUMWS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 29585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4460
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

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LXp7RFPGnfvynMs9H9GMeB`</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/tree/main",
  "prompt": "List ALL files in this model repository with their sizes. I need to know the total download size, especially the safetensors file sizes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "1e6890b9-602e-41cb-8bd7-0b1daad145a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dy69RLeJwTxWyX1jeQUMWS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 29585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4460
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

### Tool result

_source line 29 · 2026-05-18T07:26:59.753Z_

<details><summary>↩ Tool result · `toolu_01Xev3kCzA5sYJc2Hr7vHAd5`</summary>

```text
# Evaluation Tasks and Benchmarks from Paper

## Language Modeling Benchmarks (Complete List)
- ARC-Challenge (ARC-c)
- ARC-Easy (ARC-e)
- HellaSwag
- LAMBADA (LMB)
- OpenBookQA (OBQA)
- PIQA

## Recall/Long-Context Benchmarks
**RULER** suite with subtasks:
- Single-Key retrieval
- Multi-Key retrieval
- Multi-Query retrieval
- Multi-Value retrieval
- Single-Value
- Common Word Extraction (CWE)
- Frequent Word Extraction (FWE)
- Question Answering (QA)
- Variable Tokens (VT)

## In-Context Learning & Few-Shot Tasks
**Not mentioned.** The paper contains no discussion of "in-context learning," "ICL," "function composition," "compositional," or "few-shot" capabilities.

## Model Architecture Details

**340M models:**
- 20 billion tokens training
- Batch size: 50k tokens
- Specific hidden_size, num_layers, num_heads not provided in document

**1.3B models:**
- 100 billion tokens training
- Batch size: 1 million tokens
- Specific architecture parameters not provided in document

## Scale & Recall Discussion
The paper notes that "340M models show insignificant recall capability due to their relatively small parameter count," with recall only evaluated at 1.3B scale. However, no detailed analysis of how scale specifically affects recall or ICL performance appears in provided sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "8add37c3-707e-4a00-adbd-0d746b62727e",
  "tool_use_result": {
    "bytes": 546607,
    "code": 200,
    "codeText": "OK",
    "result": "# Evaluation Tasks and Benchmarks from Paper\n\n## Language Modeling Benchmarks (Complete List)\n- ARC-Challenge (ARC-c)\n- ARC-Easy (ARC-e)\n- HellaSwag\n- LAMBADA (LMB)\n- OpenBookQA (OBQA)\n- PIQA\n\n## Recall/Long-Context Benchmarks\n**RULER** suite with subtasks:\n- Single-Key retrieval\n- Multi-Key retrieval\n- Multi-Query retrieval\n- Multi-Value retrieval\n- Single-Value\n- Common Word Extraction (CWE)\n- Frequent Word Extraction (FWE)\n- Question Answering (QA)\n- Variable Tokens (VT)\n\n## In-Context Learning & Few-Shot Tasks\n**Not mentioned.** The paper contains no discussion of \"in-context learning,\" \"ICL,\" \"function composition,\" \"compositional,\" or \"few-shot\" capabilities.\n\n## Model Architecture Details\n\n**340M models:**\n- 20 billion tokens training\n- Batch size: 50k tokens\n- Specific hidden_size, num_layers, num_heads not provided in document\n\n**1.3B models:**\n- 100 billion tokens training\n- Batch size: 1 million tokens\n- Specific architecture parameters not provided in document\n\n## Scale & Recall Discussion\nThe paper notes that \"340M models show insignificant recall capability due to their relatively small parameter count,\" with recall only evaluated at 1.3B scale. However, no detailed analysis of how scale specifically affects recall or ICL performance appears in provided sections.",
    "durationMs": 5110,
    "url": "https://arxiv.org/html/2507.06457v1"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T07:27:00.946Z_

<details><summary>↩ Tool result · `toolu_01LXp7RFPGnfvynMs9H9GMeB`</summary>

```text
# Files in m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1 Repository

## All Files with Sizes

| File | Size |
|------|------|
| model-00001-of-00002.safetensors | 4.99 GB |
| model-00002-of-00002.safetensors | 606 MB |
| tokenizer.json | 3.51 MB |
| model.safetensors.index.json | 29.1 kB |
| config.json | 1.16 kB |
| .gitattributes | 1.52 kB |
| tokenizer_config.json | 1.03 kB |
| special_tokens_map.json | 414 Bytes |
| generation_config.json | 111 Bytes |

## Summary

**Total Safetensors Model Size:** **5.6 GB**
- Part 1: 4.99 GB
- Part 2: 606 MB

**Total Repository Size:** ~5.6 GB (the safetensors files comprise the vast majority; other config and tokenizer files are negligible)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "1dbe745d-5377-4d1e-ad11-e35a833a3e5a",
  "tool_use_result": {
    "bytes": 141584,
    "code": 200,
    "codeText": "OK",
    "result": "# Files in m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1 Repository\n\n## All Files with Sizes\n\n| File | Size |\n|------|------|\n| model-00001-of-00002.safetensors | 4.99 GB |\n| model-00002-of-00002.safetensors | 606 MB |\n| tokenizer.json | 3.51 MB |\n| model.safetensors.index.json | 29.1 kB |\n| config.json | 1.16 kB |\n| .gitattributes | 1.52 kB |\n| tokenizer_config.json | 1.03 kB |\n| special_tokens_map.json | 414 Bytes |\n| generation_config.json | 111 Bytes |\n\n## Summary\n\n**Total Safetensors Model Size:** **5.6 GB**\n- Part 1: 4.99 GB\n- Part 2: 606 MB\n\n**Total Repository Size:** ~5.6 GB (the safetensors files comprise the vast majority; other config and tokenizer files are negligible)",
    "durationMs": 3397,
    "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/tree/main"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T07:27:00.990Z_

<details><summary>↩ Tool result · `toolu_01Cyb5H1wz5wK2avqMaWoHAg`</summary>

````text
# GatedDeltaNet 1.3B Configuration

## Complete Model Architecture Parameters

```json
{
  "model_type": "gated_deltanet",
  "architectures": ["GatedDeltaNetForCausalLM"],
  
  "hidden_size": 2048,
  "num_hidden_layers": 24,
  "num_heads": 8,
  "head_dim": 256,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  
  "vocab_size": 32000,
  "max_position_embeddings": 2048,
  
  "bos_token_id": 1,
  "eos_token_id": 2,
  "tie_word_embeddings": false,
  
  "attention": {
    "attn_mode": "chunk",
    "layers": [2, 5, 8, 11, 14, 17, 20, 23],
    "num_heads": 16,
    "num_kv_heads": 8,
    "qkv_bias": false,
    "qk_activation": "silu",
    "qk_norm": "l2",
    "rope_theta": 10000.0,
    "window_size": null
  },
  
  "convolution": {
    "conv_size": 4,
    "use_short_conv": true
  },
  
  "gates": {
    "use_gate": true,
    "expand_k": 1,
    "expand_v": 1
  },
  
  "normalization": {
    "norm_eps": 1e-06,
    "norm_first": false,
    "use_output_norm": true,
    "qk_norm": "l2"
  },
  
  "optimization": {
    "fuse_cross_entropy": true,
    "fuse_norm": true,
    "fuse_swiglu": true,
    "use_cache": true,
    "use_beta": true
  },
  
  "initialization": {
    "initializer_range": 0.02
  },
  
  "torch_dtype": "float32",
  "transformers_version": "4.49.0"
}
```

## Key Architecture Features

- **Model Size**: 1.3B parameters
- **Context Length**: 2048 tokens
- **Vocabulary**: 32,000 tokens
- **Activation**: SwiGLU (fused)
- **Attention Pattern**: Sparse attention at layers [2, 5, 8, 11, 14, 17, 20, 23] with chunked mode
- **Position Encoding**: RoPE (θ=10000)
- **Normalization**: L2 norm on Q/K projections
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "7d7f9d5b-2d73-457c-8a0d-c75c89179bab",
  "tool_use_result": {
    "bytes": 1162,
    "code": 200,
    "codeText": "OK",
    "result": "# GatedDeltaNet 1.3B Configuration\n\n## Complete Model Architecture Parameters\n\n```json\n{\n  \"model_type\": \"gated_deltanet\",\n  \"architectures\": [\"GatedDeltaNetForCausalLM\"],\n  \n  \"hidden_size\": 2048,\n  \"num_hidden_layers\": 24,\n  \"num_heads\": 8,\n  \"head_dim\": 256,\n  \"hidden_act\": \"swish\",\n  \"hidden_ratio\": 4,\n  \n  \"vocab_size\": 32000,\n  \"max_position_embeddings\": 2048,\n  \n  \"bos_token_id\": 1,\n  \"eos_token_id\": 2,\n  \"tie_word_embeddings\": false,\n  \n  \"attention\": {\n    \"attn_mode\": \"chunk\",\n    \"layers\": [2, 5, 8, 11, 14, 17, 20, 23],\n    \"num_heads\": 16,\n    \"num_kv_heads\": 8,\n    \"qkv_bias\": false,\n    \"qk_activation\": \"silu\",\n    \"qk_norm\": \"l2\",\n    \"rope_theta\": 10000.0,\n    \"window_size\": null\n  },\n  \n  \"convolution\": {\n    \"conv_size\": 4,\n    \"use_short_conv\": true\n  },\n  \n  \"gates\": {\n    \"use_gate\": true,\n    \"expand_k\": 1,\n    \"expand_v\": 1\n  },\n  \n  \"normalization\": {\n    \"norm_eps\": 1e-06,\n    \"norm_first\": false,\n    \"use_output_norm\": true,\n    \"qk_norm\": \"l2\"\n  },\n  \n  \"optimization\": {\n    \"fuse_cross_entropy\": true,\n    \"fuse_norm\": true,\n    \"fuse_swiglu\": true,\n    \"use_cache\": true,\n    \"use_beta\": true\n  },\n  \n  \"initialization\": {\n    \"initializer_range\": 0.02\n  },\n  \n  \"torch_dtype\": \"float32\",\n  \"transformers_version\": \"4.49.0\"\n}\n```\n\n## Key Architecture Features\n\n- **Model Size**: 1.3B parameters\n- **Context Length**: 2048 tokens\n- **Vocabulary**: 32,000 tokens\n- **Activation**: SwiGLU (fused)\n- **Attention Pattern**: Sparse attention at layers [2, 5, 8, 11, 14, 17, 20, 23] with chunked mode\n- **Position Encoding**: RoPE (θ=10000)\n- **Normalization**: L2 norm on Q/K projections",
    "durationMs": 4426,
    "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/raw/main/config.json"
  }
}
````

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the results.

Key findings:
1. **1.3B models exist** - 31 models at 1.3B scale (6 architectures × 5 ratios + 1 transformer baseline)
2. **Architecture details**: hidden_size=2048, num_hidden_layers=24, num_heads=8, head_dim=256, vocab_size=32000, max_position_embeddings=2048


3. **Model specifications**: Each model is around 5.6 GB in F32 format, trained on 100B tokens across six different architectures—GatedDeltaNet, GLA, HGRN2, HGRN, DeltaNet, and RetNet—plus a standard Transformer baseline, with various mixing ratios (3:1, 6:1, 12:1, 24:1, and pure variants).
4. **Evaluation scope**: The paper focuses on language modeling benchmarks like ARC, HellaSwag, LAMBADA, OBQA, and PIQA, along with RULER recall tests, but doesn't include in-context learning or function composition evaluations.
5. **Key limitation**: The 340M models showed negligible recall performance due to their size, so recall was only properly evaluated at the 1.3B scale.

For my experiment, I need to figure out which models to actually download. I'm thinking I should focus on the same architectures I tested at 340M—GatedDeltaNet, HGRN2, and RetNet plus the Transformer baseline—across the different ratios. That's 16 models total at roughly 90 GB, though the F32 format is interesting since I might be able to work with a more efficient representation.

If I were to download all 31 models it would be around 174 GB. I'm also noting the attention layer pattern for the 3:1 hybrid—layers [2, 5, 8, 11, 14, 17, 20, 23] gives exactly 1/3 attention layers. One more thing to clarify: the paper includes HGRN alongside HGRN2, and GLA and DeltaNet are distinct from GatedDeltaNet, so there are actually 6 linear attention variants to consider.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "c66593fc-3632-422d-b88f-42bc0123447c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XA1o6AeTWAEkErtGHvTAbr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 315,
      "cache_creation_input_tokens": 1689,
      "cache_read_input_tokens": 34045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1689
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

_source line 33_

## 结论：1.3B 模型完整可用

### 完整 checkpoint 清单（31 个模型）

**6 种线性注意力架构 × 5 种配置 + 1 个 Transformer baseline：**

| 架构 | pure | 24:1 | 12:1 | 6:1 | 3:1 |
|------|------|------|------|-----|-----|
| GatedDeltaNet | ✅ (1.57k↓) | ✅ | ✅ | ✅ (9↓) | ✅ (14↓) |
| GLA | ✅ (557↓) | ✅ | ✅ | ✅ | ✅ (55↓) |
| HGRN2 | ✅ | ✅ | ✅ (10↓) | ✅ (7↓) | ✅ |
| HGRN | ✅ (5↓) | ✅ (25↓) | ✅ | ✅ | ✅ |
| DeltaNet | ✅ (516↓) | ✅ (6↓) | ✅ (5↓) | ✅ | ✅ (5↓) |
| RetNet | ✅ (519↓) | ✅ (7↓) | ✅ | ✅ | ✅ (16↓) |
| **Transformer** | **✅ baseline (683↓)** | | | | |

训练数据：100B tokens（340M 是 20B tokens）

### 架构参数（GatedDeltaNet 1.3B hybrid-3-1 为例）

| 参数 | 值 |
|------|-----|
| hidden_size | 2048 |
| num_hidden_layers | 24 |
| num_heads | 8 |
| head_dim | 256 |
| hidden_ratio | 4 (→ intermediate ≈ 8192) |
| vocab_size | 32000 |
| max_position_embeddings | 2048 |
| attention layers (3:1) | [2, 5, 8, 11, 14, 17, 20, 23] (8/24 layers) |
| torch_dtype | float32 |

### 磁盘与下载估算

- 单个模型：**~5.6 GB**（F32 safetensors，2 个分片：4.99 GB + 606 MB）
- 我们实验所需子集（GatedDeltaNet + HGRN2 + RetNet × 5 ratios + Transformer baseline = 16 个模型）：**~90 GB**
- 全部 31 个 1.3B 模型：**~174 GB**

### 论文中关于 ICL/function composition 的发现

**论文没有评估 ICL 或 function composition。** 评估任务为：

- **语言建模**：ARC-c, ARC-e, HellaSwag, LAMBADA, OBQA, PIQA
- **Recall**：RULER suite（Single/Multi-Key/Query/Value retrieval, CWE, FWE, QA, VT）

关键发现：**"340M models show insignificant recall capability due to their relatively small parameter count"**，recall 仅在 1.3B 上评估。这直接解释了我们 340M 模型在 function composition 上全部 random chance 的结果。

### 对我们实验的启示

1. **必须升级到 1.3B** — 340M 连 recall 能力都不足，function composition（更难的任务）自然无法完成
2. 论文推荐的最优配置是 **HGRN2 或 GatedDeltaNet，ratio 3:1 到 6:1**，这些应是我们重点关注的 variant
3. 1.3B 模型训练了 100B tokens（5× 于 340M 的 20B），能力差异不仅来自参数量，也来自训练数据量

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "uuid": "2351506f-1b14-4085-ad10-590224c0f105",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XA1o6AeTWAEkErtGHvTAbr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 315,
      "cache_creation_input_tokens": 1689,
      "cache_read_input_tokens": 34045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1689
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

_source line 34_

## 结论：1.3B 模型完整可用

### 完整 checkpoint 清单（31 个模型）

**6 种线性注意力架构 × 5 种配置 + 1 个 Transformer baseline：**

| 架构 | pure | 24:1 | 12:1 | 6:1 | 3:1 |
|------|------|------|------|-----|-----|
| GatedDeltaNet | ✅ (1.57k↓) | ✅ | ✅ | ✅ (9↓) | ✅ (14↓) |
| GLA | ✅ (557↓) | ✅ | ✅ | ✅ | ✅ (55↓) |
| HGRN2 | ✅ | ✅ | ✅ (10↓) | ✅ (7↓) | ✅ |
| HGRN | ✅ (5↓) | ✅ (25↓) | ✅ | ✅ | ✅ |
| DeltaNet | ✅ (516↓) | ✅ (6↓) | ✅ (5↓) | ✅ | ✅ (5↓) |
| RetNet | ✅ (519↓) | ✅ (7↓) | ✅ | ✅ | ✅ (16↓) |
| **Transformer** | **✅ baseline (683↓)** | | | | |

训练数据：100B tokens（340M 是 20B tokens）

### 架构参数（GatedDeltaNet 1.3B hybrid-3-1 为例）

| 参数 | 值 |
|------|-----|
| hidden_size | 2048 |
| num_hidden_layers | 24 |
| num_heads | 8 |
| head_dim | 256 |
| hidden_ratio | 4 (→ intermediate ≈ 8192) |
| vocab_size | 32000 |
| max_position_embeddings | 2048 |
| attention layers (3:1) | [2, 5, 8, 11, 14, 17, 20, 23] (8/24 layers) |
| torch_dtype | float32 |

### 磁盘与下载估算

- 单个模型：**~5.6 GB**（F32 safetensors，2 个分片：4.99 GB + 606 MB）
- 我们实验所需子集（GatedDeltaNet + HGRN2 + RetNet × 5 ratios + Transformer baseline = 16 个模型）：**~90 GB**
- 全部 31 个 1.3B 模型：**~174 GB**

### 论文中关于 ICL/function composition 的发现

**论文没有评估 ICL 或 function composition。** 评估任务为：

- **语言建模**：ARC-c, ARC-e, HellaSwag, LAMBADA, OBQA, PIQA
- **Recall**：RULER suite（Single/Multi-Key/Query/Value retrieval, CWE, FWE, QA, VT）

关键发现：**"340M models show insignificant recall capability due to their relatively small parameter count"**，recall 仅在 1.3B 上评估。这直接解释了我们 340M 模型在 function composition 上全部 random chance 的结果。

### 对我们实验的启示

1. **必须升级到 1.3B** — 340M 连 recall 能力都不足，function composition（更难的任务）自然无法完成
2. 论文推荐的最优配置是 **HGRN2 或 GatedDeltaNet，ratio 3:1 到 6:1**，这些应是我们重点关注的 variant
3. 1.3B 模型训练了 100B tokens（5× 于 340M 的 20B），能力差异不仅来自参数量，也来自训练数据量

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 89435,
  "duration_api_ms": 131922,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "a23b1a1e-d40e-4bbf-8b7c-435de195555f",
  "total_cost_usd": 0.48186825,
  "usage": {
    "input_tokens": 2991,
    "cache_creation_input_tokens": 23893,
    "cache_read_input_tokens": 125968,
    "output_tokens": 3461,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 23893,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 315,
        "output_tokens": 1803,
        "cache_read_input_tokens": 34045,
        "cache_creation_input_tokens": 1689,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1689
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 102858,
      "outputTokens": 7043,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 3,
      "costUSD": 0.168073,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 2991,
      "outputTokens": 3461,
      "cacheReadInputTokens": 125968,
      "cacheCreationInputTokens": 23893,
      "webSearchRequests": 0,
      "costUSD": 0.31379525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a478f570-e2b3-4a21-a9ab-0dc4ec43d876"
}
```

</details>

---
