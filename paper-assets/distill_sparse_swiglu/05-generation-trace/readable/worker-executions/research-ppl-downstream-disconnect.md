# research ppl downstream disconnect

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_research_ppl-downstream-disconnect_20260516T015921.log`
- **Structured JSON:** [`d540579e249135442d09.json`](../../sessions/d5/d540579e249135442d09.json)

## Before a recorded user message

15 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
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
  "uuid": "5ae7e550-b6ce-491c-9633-793f708f49a7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/memory/"
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
    "resetsAt": 1778903400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "eeaf2e6a-9ded-43a9-a1de-f7dbab16523e",
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c"
}
```

---

### Assistant

_source line 4_

我来搜索关于 PPL-downstream disconnect 在 sparsity 场景下的相关文献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "3dca9784-3c51-42f4-96d8-ed51dcdc1d05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpXp9P3PwDv73F6S3g8RPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11520,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11520
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ph3EifeTxitRR6n4WNH2ET`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "ec975c04-fb76-402b-8205-6c67f68dde93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpXp9P3PwDv73F6S3g8RPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11520,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11520
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-16T01:59:35.970Z_

<details><summary>↩ Tool result · `toolu_01Ph3EifeTxitRR6n4WNH2ET`</summary>

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
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "477948ba-a4f3-4d2d-9626-89187da7a29c",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me search for relevant literature on the PPL-downstream disconnect phenomenon in sparsity/pruning contexts. I'll run multiple searches in parallel to cover different angles.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "7a7203ec-3852-48e8-89a5-7499b0ab46a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TK6uCSJXycYMJL21swCm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1512,
      "cache_read_input_tokens": 23361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1512
      },
      "output_tokens": 19,
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

_source line 8_

开始并行搜索多个关键词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "353ebf1c-a677-4ec3-9030-58b3db58c6fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TK6uCSJXycYMJL21swCm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1512,
      "cache_read_input_tokens": 23361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1512
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_013HLmgcb2vmKMuqmPErFTK9`</summary>

```json
{
  "query": "perplexity downstream accuracy gap LLM pruning sparsity misleading metric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "755f125e-5f38-48c7-b6db-455effb82407",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TK6uCSJXycYMJL21swCm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1512,
      "cache_read_input_tokens": 23361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1512
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_011wAkunxdb9tfH6UaXatMma`</summary>

```json
{
  "query": "LLM pruning downstream task degradation perplexity does not predict benchmark performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "06f5101f-7ad0-403e-acca-890cdf5e0d03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TK6uCSJXycYMJL21swCm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1512,
      "cache_read_input_tokens": 23361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1512
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SH6DhkFVUeW7sWG1igfJU7`</summary>

```json
{
  "query": "activation sparsity SwiGLU neuron pruning downstream evaluation catastrophic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "2f35f6f9-8f46-41d6-ace7-b0f23f138512",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TK6uCSJXycYMJL21swCm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1512,
      "cache_read_input_tokens": 23361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1512
      },
      "output_tokens": 19,
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0142KJpLQrQeqLrtYLAHthNg`</summary>

```json
{
  "query": "structured pruning LLM perplexity proxy metric limitation arXiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "8e6e2e3b-0f48-4561-9df9-df67f39ef883",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TK6uCSJXycYMJL21swCm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1512,
      "cache_read_input_tokens": 23361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1512
      },
      "output_tokens": 19,
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

_source line 13 · 2026-05-16T01:59:47.618Z_

<details><summary>↩ Tool result · `toolu_013HLmgcb2vmKMuqmPErFTK9`</summary>

```text
Web search results for query: "perplexity downstream accuracy gap LLM pruning sparsity misleading metric"

Links: [{"title":"UniPruning: Unifying Local Metric and Global Feedback for Scalable Sparse LLMs","url":"https://arxiv.org/html/2510.03291"},{"title":"Týr-the-Pruner: Unlocking Accurate 50% Structural Pruning ...","url":"https://arxiv.org/pdf/2503.09657"},{"title":"Perplexity for LLM Evaluation - Comet","url":"https://www.comet.com/site/blog/perplexity-for-llm-evaluation/"},{"title":"SoLA: Leveraging Soft Activation Sparsity and Low-Rank Decomposition for Large Language Model Compression","url":"https://arxiv.org/html/2604.03258"},{"title":"Towards Extreme Pruning of LLMs with Plug-and-Play Mixed Sparsity","url":"https://arxiv.org/html/2503.11164"},{"title":"Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models","url":"https://arxiv.org/html/2405.20541v1"},{"title":"PERPLEXITY-BASED PRUNING WITH SMALL ...","url":"https://openreview.net/pdf?id=wNseMYxwpq"},{"title":"Perplexity for LLM Evaluation - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/perplexity-for-llm-evaluation/"},{"title":"Efficient Post-Training Pruning of Large Language Models with Statistical Correction","url":"https://arxiv.org/html/2602.07375v1"},{"title":"FASP: Fast and Accurate Structured Pruning of Large Language Models","url":"https://arxiv.org/html/2501.09412"}]

Based on the search results, I found relevant research on the gap between perplexity and downstream accuracy metrics in LLM pruning and sparsity:

## Key Finding

Test set perplexity can be a misleading metric for evaluating the efficacy of data pruning techniques, as interventions that result in significantly higher test set perplexity can still achieve better performance on downstream tasks.

This insight comes from research titled "Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models," which specifically investigates the disconnect between upstream (perplexity) and downstream task performance metrics.

## Context on Perplexity's Limitations

More broadly, a model can achieve a low perplexity score by assigning high probabilities to common words, like articles and conjunctions, leading to a misleadingly low score, and overfit models can show low perplexity but lack true understanding. Additionally, research suggests that perplexity doesn't correlate well with an LLM's long-term understanding, likely because it fails to capture long-term dependencies.

## Implications for LLM Pruning Research

The research emphasizes that while previous works evaluate the resulting LLM's quality based on upstream metrics such as perplexity on the test split of the pretraining dataset, downstream evaluation benchmarks provide stronger, more rigorous conclusions about impact, as some techniques that significantly improve downstream performance have no, or even adverse, effects on upstream performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "9d6b730a-3435-4f8d-9982-4aaff1828b12",
  "tool_use_result": {
    "query": "perplexity downstream accuracy gap LLM pruning sparsity misleading metric",
    "results": [
      {
        "tool_use_id": "srvtoolu_0147BET1fwSH2SdNGqWTghYv",
        "content": [
          {
            "title": "UniPruning: Unifying Local Metric and Global Feedback for Scalable Sparse LLMs",
            "url": "https://arxiv.org/html/2510.03291"
          },
          {
            "title": "Týr-the-Pruner: Unlocking Accurate 50% Structural Pruning ...",
            "url": "https://arxiv.org/pdf/2503.09657"
          },
          {
            "title": "Perplexity for LLM Evaluation - Comet",
            "url": "https://www.comet.com/site/blog/perplexity-for-llm-evaluation/"
          },
          {
            "title": "SoLA: Leveraging Soft Activation Sparsity and Low-Rank Decomposition for Large Language Model Compression",
            "url": "https://arxiv.org/html/2604.03258"
          },
          {
            "title": "Towards Extreme Pruning of LLMs with Plug-and-Play Mixed Sparsity",
            "url": "https://arxiv.org/html/2503.11164"
          },
          {
            "title": "Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models",
            "url": "https://arxiv.org/html/2405.20541v1"
          },
          {
            "title": "PERPLEXITY-BASED PRUNING WITH SMALL ...",
            "url": "https://openreview.net/pdf?id=wNseMYxwpq"
          },
          {
            "title": "Perplexity for LLM Evaluation - GeeksforGeeks",
            "url": "https://www.geeksforgeeks.org/nlp/perplexity-for-llm-evaluation/"
          },
          {
            "title": "Efficient Post-Training Pruning of Large Language Models with Statistical Correction",
            "url": "https://arxiv.org/html/2602.07375v1"
          },
          {
            "title": "FASP: Fast and Accurate Structured Pruning of Large Language Models",
            "url": "https://arxiv.org/html/2501.09412"
          }
        ]
      },
      "Based on the search results, I found relevant research on the gap between perplexity and downstream accuracy metrics in LLM pruning and sparsity:\n\n## Key Finding\n\nTest set perplexity can be a misleading metric for evaluating the efficacy of data pruning techniques, as interventions that result in significantly higher test set perplexity can still achieve better performance on downstream tasks.\n\nThis insight comes from research titled \"Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models,\" which specifically investigates the disconnect between upstream (perplexity) and downstream task performance metrics.\n\n## Context on Perplexity's Limitations\n\nMore broadly, a model can achieve a low perplexity score by assigning high probabilities to common words, like articles and conjunctions, leading to a misleadingly low score, and overfit models can show low perplexity but lack true understanding. Additionally, research suggests that perplexity doesn't correlate well with an LLM's long-term understanding, likely because it fails to capture long-term dependencies.\n\n## Implications for LLM Pruning Research\n\nThe research emphasizes that while previous works evaluate the resulting LLM's quality based on upstream metrics such as perplexity on the test split of the pretraining dataset, downstream evaluation benchmarks provide stronger, more rigorous conclusions about impact, as some techniques that significantly improve downstream performance have no, or even adverse, effects on upstream performance."
    ],
    "durationSeconds": 6.731180055000001
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T01:59:48.435Z_

<details><summary>↩ Tool result · `toolu_011wAkunxdb9tfH6UaXatMma`</summary>

```text
Web search results for query: "LLM pruning downstream task degradation perplexity does not predict benchmark performance"

Links: [{"title":"Frustratingly Easy Task-aware Pruning for Large Language Models","url":"https://arxiv.org/html/2510.22489"},{"title":"When Less is More: Investigating Data Pruning for Pretraining LLMs at Scale","url":"https://openreview.net/pdf?id=XUIYn3jo5T"},{"title":"LLMs can Compress LLMs: Adaptive Pruning by Agents","url":"https://arxiv.org/html/2601.09694"},{"title":"Mitigating Forgetting in LLM Fine-Tuning via Low-Perplexity Token Learning","url":"https://arxiv.org/html/2501.14315v2"},{"title":"Is my model perplexed for the right reason? Contrasting LLMs’ Benchmark Behavior with Token-Level Perplexity","url":"https://arxiv.org/html/2603.29396v1"},{"title":"Týr-the-Pruner: Unlocking Accurate 50% Structural Pruning ...","url":"https://arxiv.org/pdf/2503.09657"},{"title":"DRPruning: Efficient Large Language Model Pruning through Distributionally Robust Optimization","url":"https://arxiv.org/html/2411.14055v1"},{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"},{"title":"Evaluating the Impact of Compression Techniques on Task-Specific Performance of Large Language Models","url":"https://arxiv.org/html/2409.11233"},{"title":"Multi-dimensional Safety Evaluation of LLM Compression","url":"https://aclanthology.org/2024.findings-emnlp.901.pdf"}]

I found several highly relevant research papers on this topic. Here are the key findings:

## Main Findings

Structured pruning methods experience near-total collapse in factual question-answering performance, with N:M sparsity patterns losing over 97% accuracy on knowledge-intensive tasks even at modest sparsity ratios (25-30%), despite negligible perplexity increases. This disconnect between perplexity and actual task performance underscores the inadequacy of current evaluation metrics and pruning strategies.

While SparseGPT and Wanda preserve perplexity even at 50% sparsity, they suffer significant degradation on downstream tasks, highlighting the inadequacy of perplexity as the sole evaluation metric.

## Why This Disconnect Occurs

Perplexity measures how confidently a model predicts the next token, but it does not fully capture the nuanced impacts of compression on task-specific outputs.

## Alternative Evaluation Approaches

Researchers have proposed alternatives to address this limitation. Jensen-Shannon (JS) Divergence has been introduced as a more comprehensive metric that captures nuanced changes in model behavior post-compression.

Additionally, at moderate sparsity levels such as 50% and 75%, task-aware pruning shows clear improvements on downstream tasks (including MMLU, MedQA, and ARC), while maintaining comparable perplexity on WikiText-2, indicating that the integration of task-specific information effectively enhances model capability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "75eb6ac4-c796-4b7f-9882-58ec689c9cab",
  "tool_use_result": {
    "query": "LLM pruning downstream task degradation perplexity does not predict benchmark performance",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VktmKAHmFjjectUktV92ok",
        "content": [
          {
            "title": "Frustratingly Easy Task-aware Pruning for Large Language Models",
            "url": "https://arxiv.org/html/2510.22489"
          },
          {
            "title": "When Less is More: Investigating Data Pruning for Pretraining LLMs at Scale",
            "url": "https://openreview.net/pdf?id=XUIYn3jo5T"
          },
          {
            "title": "LLMs can Compress LLMs: Adaptive Pruning by Agents",
            "url": "https://arxiv.org/html/2601.09694"
          },
          {
            "title": "Mitigating Forgetting in LLM Fine-Tuning via Low-Perplexity Token Learning",
            "url": "https://arxiv.org/html/2501.14315v2"
          },
          {
            "title": "Is my model perplexed for the right reason? Contrasting LLMs’ Benchmark Behavior with Token-Level Perplexity",
            "url": "https://arxiv.org/html/2603.29396v1"
          },
          {
            "title": "Týr-the-Pruner: Unlocking Accurate 50% Structural Pruning ...",
            "url": "https://arxiv.org/pdf/2503.09657"
          },
          {
            "title": "DRPruning: Efficient Large Language Model Pruning through Distributionally Robust Optimization",
            "url": "https://arxiv.org/html/2411.14055v1"
          },
          {
            "title": "Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling",
            "url": "https://arxiv.org/html/2604.25098"
          },
          {
            "title": "Evaluating the Impact of Compression Techniques on Task-Specific Performance of Large Language Models",
            "url": "https://arxiv.org/html/2409.11233"
          },
          {
            "title": "Multi-dimensional Safety Evaluation of LLM Compression",
            "url": "https://aclanthology.org/2024.findings-emnlp.901.pdf"
          }
        ]
      },
      "I found several highly relevant research papers on this topic. Here are the key findings:\n\n## Main Findings\n\nStructured pruning methods experience near-total collapse in factual question-answering performance, with N:M sparsity patterns losing over 97% accuracy on knowledge-intensive tasks even at modest sparsity ratios (25-30%), despite negligible perplexity increases. This disconnect between perplexity and actual task performance underscores the inadequacy of current evaluation metrics and pruning strategies.\n\nWhile SparseGPT and Wanda preserve perplexity even at 50% sparsity, they suffer significant degradation on downstream tasks, highlighting the inadequacy of perplexity as the sole evaluation metric.\n\n## Why This Disconnect Occurs\n\nPerplexity measures how confidently a model predicts the next token, but it does not fully capture the nuanced impacts of compression on task-specific outputs.\n\n## Alternative Evaluation Approaches\n\nResearchers have proposed alternatives to address this limitation. Jensen-Shannon (JS) Divergence has been introduced as a more comprehensive metric that captures nuanced changes in model behavior post-compression.\n\nAdditionally, at moderate sparsity levels such as 50% and 75%, task-aware pruning shows clear improvements on downstream tasks (including MMLU, MedQA, and ARC), while maintaining comparable perplexity on WikiText-2, indicating that the integration of task-specific information effectively enhances model capability."
    ],
    "durationSeconds": 7.058000543000002
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T01:59:49.813Z_

<details><summary>↩ Tool result · `toolu_01SH6DhkFVUeW7sWG1igfJU7`</summary>

```text
Web search results for query: "activation sparsity SwiGLU neuron pruning downstream evaluation catastrophic"

Links: [{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"},{"title":"Post-Training Statistical Calibration for Higher Activation Sparsity","url":"https://arxiv.org/html/2412.07174"},{"title":"SwiGLU Activation in Transformer Models","url":"https://www.emergentmind.com/topics/swiglu-activation"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://arxiv.org/pdf/2406.05955"},{"title":"training-free activation sparsity in large language models","url":"https://www.arxiv.org/pdf/2408.14690"},{"title":"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models","url":"https://arxiv.org/html/2512.12744"},{"title":"First Activations Matter: Training-Free Methods for Dynamic Activation in Large Language Models","url":"https://arxiv.org/html/2408.11393v1"},{"title":"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models","url":"https://arxiv.org/html/2604.27115"},{"title":"Activation Sparsity Opportunities for Compressing General Large Language Models","url":"https://arxiv.org/pdf/2412.12178"},{"title":"Efficient Activation Functions for Sparse LLMs","url":"https://www.emergentmind.com/topics/efficient-activation-functions-for-sparse-llms"}]

I found several relevant research papers on activation sparsity, SwiGLU, neuron pruning, and downstream evaluation. Here's what the search revealed:

## Key Research Findings:

**Activation Sparsity in SwiGLU Models:**

The CATS method enables training-free activation sparsity on SwiGLU-based LLMs by applying magnitude pruning on the output of Wgate, and achieves up to 50% sparsity in Wup and Wdown for Mistral and Llama-2-7B.

However, SwiGLU demonstrates negligible natural activation sparsity, creating new challenges for compression via activation sparsity. In contrast, ReLU-based and dReLU models allow substantially higher activation sparsity for a given accuracy budget than GELU, SiLU, or SwiGLU.

**Catastrophic Degradation:**

At higher sparsity ratios, standard models suffer catastrophic degradation, with this performance gap widening significantly. Aggressive pruning eliminates neurons that still contribute to the task, causing nonlinear degradation and reduced downstream performance.

**Downstream Evaluation:**

The research includes extensive downstream task evaluations. Full downstream task results are provided for evaluated models, with greedy sparsity configurations outperforming uniform configurations across the board.

**Robustness Solutions:**

Recent work like SPON (Spontaneous Neurons) addresses catastrophic degradation: SPON-integrated models consistently outperform standard baselines across all sparsity levels, with this performance gap widening significantly at higher sparsity ratios where standard models suffer catastrophic degradation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9118ce26-bee7-48a7-a485-ce6d383f8c1c",
  "uuid": "6c98df25-8cba-4d65-9507-0ff98fdfe8c7",
  "tool_use_result": {
    "query": "activation sparsity SwiGLU neuron pruning downstream evaluation catastrophic",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TYqgDAHwNhPw9vba33XEmm",
        "content": [
          {
            "title": "TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"
          },
          {
            "title": "Post-Training Statistical Calibration for Higher Activation Sparsity",
            "url": "https://arxiv.org/html/2412.07174"
          },
          {
            "title": "SwiGLU Activation in Transformer Models",
            "url": "https://www.emergentmind.com/topics/swiglu-activation"
          },
          {
            "title": "Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters",
            "url": "https://arxiv.org/pdf/2406.05955"
          },
          {
            "title": "training-free activation sparsity in large language models",
            "url": "https://www.arxiv.org/pdf/2408.14690"
          },
          {
            "title": "Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models",
            "url": "https://arxiv.org/html/2512.12744"
          },
          {
            "title": "First Activations Matter: Training-Free Methods for Dynamic Activation in Large Language Models",
            "url": "https://arxiv.org/html/2408.11393v1"
          },
          {
            "title": "Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models",
            "url": "https://arxiv.org/html/2604.27115"
          },
          {
            "title": "Activation Sparsity Opportunities for Compressing General Large Language Models",
            "url": "https://arxiv.org/pdf/2412.12178"
          },
          {
            "title": "Efficient Activation Functions for Sparse LLMs",
            "url": "https://www.emergentmind.com/topics/efficient-activation-functions-for-sparse-llms"
          }
        ]
      },
      "I found several relevant research papers on activation sparsity, SwiGLU, neuron pruning, and downstream evaluation. Here's what the search revealed:\n\n## Key Research Findings:\n\n**Activation Sparsity in SwiGLU Models:**\n\nThe CATS method enables training-free activation sparsity on SwiGLU-based LLMs by applying magnitude pruning on the output of Wgate, and achieves up to 50% sparsity in Wup and Wdown for Mistral and Llama-2-7B.\n\nHowever, SwiGLU demonstrates negligible natural activation sparsity, creating new challenges for compression via activation sparsity. In contrast, ReLU-based and dReLU models allow substantially higher activation sparsity for a given accuracy budget than GELU, SiLU, or SwiGLU.\n\n**Catastrophic Degradation:**\n\nAt higher sparsity ratios, standard models suffer catastrophic degradation, with this performance gap widening significantly. Aggressive pruning eliminates neurons that still contribute to the task, causing nonlinear degradation and reduced downstream performance.\n\n**Downstream Evaluation:**\n\nThe research includes extensive downstream task evaluations. Full downstream task results are provided for evaluated models, with greedy sparsity configurations outperforming uniform configurations across the board.\n\n**Robustness Solutions:**\n\nRecent work like SPON (Spontaneous Neurons) addresses catastrophic degradation: SPON-integrated models consistently outperform standard baselines across all sparsity levels, with this performance gap widening significantly at higher sparsity ratios where standard models suffer catastrophic degradation."
    ],
    "durationSeconds": 7.529897942
  }
}
```

</details>

---
