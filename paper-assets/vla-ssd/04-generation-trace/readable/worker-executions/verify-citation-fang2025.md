# verify citation fang2025

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_verify_citation_fang2025_20260524T013504.log`
- **Structured JSON:** [`ac93bac4b42a28646284.json`](../../sessions/ac/ac93bac4b42a28646284.json)

## Before a recorded user message

38 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
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
    "Write"
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
  "uuid": "d67dafda-061d-4181-9a91-8877c4329103",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779593400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9742275f-fac2-491d-ab80-5a671a11d7f0",
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f"
}
```

---

### Assistant

_source line 4_

我来执行这个引用核实任务。先并行搜索 DualVLA 和 reasoning erosion 相关论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "93bf6ed6-a720-400e-99e9-7c30e8e81131",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUWkmdkfz1TEFV5vx34mJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11617,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11617
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FQH97YCAuUciMBLAxXTMru`</summary>

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
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "fab05a73-4a23-497f-a9fe-c40560e3f6fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUWkmdkfz1TEFV5vx34mJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11617,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11617
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

_source line 6 · 2026-05-24T01:35:23.636Z_

<details><summary>↩ Tool result · `toolu_01FQH97YCAuUciMBLAxXTMru`</summary>

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
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "23a5cbbb-104f-4721-974e-e5db8b83911e",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me run multiple searches in parallel to gather information about both papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "6e3b25b0-8f3b-4bdc-b467-608c9a257702",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No12wUTfZvc5YQeyCj4yQZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 23458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 642
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ud3dkzpemTtXCeSW2cEqfu`</summary>

```json
{
  "query": "DualVLA arXiv 2511.22134"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "4ebe2b09-bdb7-479b-9216-d799ec01ed6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No12wUTfZvc5YQeyCj4yQZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 23458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 642
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_018q6dJdVApr6dAUm4ajvoa9`</summary>

```json
{
  "query": "reasoning erosion VLA fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "5aa9de91-6883-4cbb-a228-f6d03e1bfb99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No12wUTfZvc5YQeyCj4yQZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 23458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 642
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F55bwYBcchbTN4GzMTvKin`</summary>

```json
{
  "query": "From Intention to Execution Probing Generalization Boundaries VLA Models Irving Fang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "331c1a42-24c6-42fd-8246-4d4542860868",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No12wUTfZvc5YQeyCj4yQZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 23458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 642
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_016MzAe5TMxTToujrFJicqVe`</summary>

```json
{
  "query": "arXiv 2506.09930"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "8f4479d8-ca30-4421-a480-c3f943e9b0fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No12wUTfZvc5YQeyCj4yQZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 23458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 642
      },
      "output_tokens": 22,
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

_source line 12 · 2026-05-24T01:35:32.481Z_

<details><summary>↩ Tool result · `toolu_016MzAe5TMxTToujrFJicqVe`</summary>

```text
Web search results for query: "arXiv 2506.09930"

Links: [{"title":"[2506.09930] From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.09930"},{"title":"Upregulation of ARHGAP9 is correlated with poor prognosis and immune infiltration in clear cell renal cell carcinoma","url":"https://www.medrxiv.org/content/10.1101/2023.08.31.23294890.full.pdf"},{"title":"Zero-shot ecological annotation of microbial genomes with myLLannotator accelerates scientific discovery","url":"https://www.biorxiv.org/content/10.64898/2026.01.18.700140.full.pdf"},{"title":"Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models","url":"https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"},{"title":"Uncertainty-aware genomic deep learning with knowledge distillation","url":"https://www.biorxiv.org/content/10.1101/2024.11.13.623485.full.pdf"},{"title":"Uncovering critical transitions and molecule mechanisms in disease progressions using Gaussian graphical optimal transport","url":"https://www.biorxiv.org/content/10.1101/2024.04.24.590914.full.pdf"}]

Based on the search results, arXiv paper 2506.09930 is titled "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models" and discusses how Vision-Language-Action (VLA) models can leverage the broad generalization capabilities of large Vision-Language Models (VLMs) to produce versatile, "generalist" robot policies.

The research introduces a unified probing suite of 50 simulation-based tasks across 10 subcategories spanning language instruction, vision, and objects to address gaps in current VLA evaluations. The paper was published on June 11, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "51b54294-fc5f-42d4-8cb5-67f47d83090b",
  "tool_use_result": {
    "query": "arXiv 2506.09930",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G2pYFQGdsY2NrVMksX1Mky",
        "content": [
          {
            "title": "[2506.09930] From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2506.09930"
          },
          {
            "title": "Upregulation of ARHGAP9 is correlated with poor prognosis and immune infiltration in clear cell renal cell carcinoma",
            "url": "https://www.medrxiv.org/content/10.1101/2023.08.31.23294890.full.pdf"
          },
          {
            "title": "Zero-shot ecological annotation of microbial genomes with myLLannotator accelerates scientific discovery",
            "url": "https://www.biorxiv.org/content/10.64898/2026.01.18.700140.full.pdf"
          },
          {
            "title": "Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models",
            "url": "https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"
          },
          {
            "title": "Uncertainty-aware genomic deep learning with knowledge distillation",
            "url": "https://www.biorxiv.org/content/10.1101/2024.11.13.623485.full.pdf"
          },
          {
            "title": "Uncovering critical transitions and molecule mechanisms in disease progressions using Gaussian graphical optimal transport",
            "url": "https://www.biorxiv.org/content/10.1101/2024.04.24.590914.full.pdf"
          }
        ]
      },
      "Based on the search results, arXiv paper 2506.09930 is titled \"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models\" and discusses how Vision-Language-Action (VLA) models can leverage the broad generalization capabilities of large Vision-Language Models (VLMs) to produce versatile, \"generalist\" robot policies.\n\nThe research introduces a unified probing suite of 50 simulation-based tasks across 10 subcategories spanning language instruction, vision, and objects to address gaps in current VLA evaluations. The paper was published on June 11, 2025."
    ],
    "durationSeconds": 4.482575836
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T01:35:33.653Z_

<details><summary>↩ Tool result · `toolu_018q6dJdVApr6dAUm4ajvoa9`</summary>

```text
Web search results for query: "reasoning erosion VLA fine-tuning"

Links: [{"title":"(PDF) ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy","url":"https://www.researchgate.net/publication/388884199_ConRFT_A_Reinforced_Fine-tuning_Method_for_VLA_Models_via_Consistency_Policy"},{"title":"DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/pdf/2511.22134"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models Angen Ye12∗","url":"https://arxiv.org/pdf/2510.01623"},{"title":"AutoDrive-R²: Incentivizing Reasoning and Self-Reflection Capacity for VLA","url":"https://arxiv.org/pdf/2509.01944"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"SFT or RL? An Early Investigation into Training R1-Like Reasoning Large   Vision-Language Models","url":"https://arxiv.org/pdf/2504.11468"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v2"},{"title":"Mitigating the Reasoning Tax in Vision-Language Fine-Tuning with Input-Adaptive Depth Aggregation","url":"https://arxiv.org/pdf/2603.26330"}]

Based on the search results, here's what I found about reasoning erosion in VLA fine-tuning:

## Reasoning Erosion in Vision-Language-Action Models

When reasoning capabilities are introduced to Vision-Language-Action models through fine-tuning, the resulting reasoning VLA exhibits degraded action performance compared to the specialist VLA before fine-tuning, a phenomenon defined as "action degeneration."

More broadly, supervised fine-tuning on visual instruction data, while improving perceptual capabilities, often weakens reasoning performance, particularly on mathematical, scientific, and complex visual inference tasks—a problem researchers call the "reasoning tax."

### Related Research Approaches

Several papers address this challenge:

1. **DualVLA**: Uses a dual-teacher strategy with an action teacher for fine-grained manipulation supervision and a reasoning teacher maintaining general reasoning capability, which improves action performance while preserving reasoning ability.

2. **IADA (Input-Adaptive Depth Aggregation)**: Reinterprets the reasoning tax as a problem of cross-depth representational access during fine-tuning.

3. **Training Paradigms**: Supervised fine-tuning can significantly undermine subsequent reinforcement learning by inducing "pseudo reasoning paths" imitated from expert models.

These findings highlight the tension between improving task-specific manipulation skills and maintaining broader reasoning capabilities in VLA models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "43256969-1cdf-40d7-bc21-5de66e26d9c7",
  "tool_use_result": {
    "query": "reasoning erosion VLA fine-tuning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LdEtmdEhxhmof4cwXTCYn8",
        "content": [
          {
            "title": "(PDF) ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy",
            "url": "https://www.researchgate.net/publication/388884199_ConRFT_A_Reinforced_Fine-tuning_Method_for_VLA_Models_via_Consistency_Policy"
          },
          {
            "title": "DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action",
            "url": "https://arxiv.org/pdf/2511.22134"
          },
          {
            "title": "VLA-R1: Enhancing Reasoning in Vision-Language-Action Models Angen Ye12∗",
            "url": "https://arxiv.org/pdf/2510.01623"
          },
          {
            "title": "AutoDrive-R²: Incentivizing Reasoning and Self-Reflection Capacity for VLA",
            "url": "https://arxiv.org/pdf/2509.01944"
          },
          {
            "title": "Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control",
            "url": "https://arxiv.org/html/2512.11921v1"
          },
          {
            "title": "SFT or RL? An Early Investigation into Training R1-Like Reasoning Large   Vision-Language Models",
            "url": "https://arxiv.org/pdf/2504.11468"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v2"
          },
          {
            "title": "Mitigating the Reasoning Tax in Vision-Language Fine-Tuning with Input-Adaptive Depth Aggregation",
            "url": "https://arxiv.org/pdf/2603.26330"
          }
        ]
      },
      "Based on the search results, here's what I found about reasoning erosion in VLA fine-tuning:\n\n## Reasoning Erosion in Vision-Language-Action Models\n\nWhen reasoning capabilities are introduced to Vision-Language-Action models through fine-tuning, the resulting reasoning VLA exhibits degraded action performance compared to the specialist VLA before fine-tuning, a phenomenon defined as \"action degeneration.\"\n\nMore broadly, supervised fine-tuning on visual instruction data, while improving perceptual capabilities, often weakens reasoning performance, particularly on mathematical, scientific, and complex visual inference tasks—a problem researchers call the \"reasoning tax.\"\n\n### Related Research Approaches\n\nSeveral papers address this challenge:\n\n1. **DualVLA**: Uses a dual-teacher strategy with an action teacher for fine-grained manipulation supervision and a reasoning teacher maintaining general reasoning capability, which improves action performance while preserving reasoning ability.\n\n2. **IADA (Input-Adaptive Depth Aggregation)**: Reinterprets the reasoning tax as a problem of cross-depth representational access during fine-tuning.\n\n3. **Training Paradigms**: Supervised fine-tuning can significantly undermine subsequent reinforcement learning by inducing \"pseudo reasoning paths\" imitated from expert models.\n\nThese findings highlight the tension between improving task-specific manipulation skills and maintaining broader reasoning capabilities in VLA models."
    ],
    "durationSeconds": 6.204016313
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T01:35:33.985Z_

<details><summary>↩ Tool result · `toolu_01Ud3dkzpemTtXCeSW2cEqfu`</summary>

```text
Web search results for query: "DualVLA arXiv 2511.22134"

Links: [{"title":"[2511.22134] DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/abs/2511.22134"},{"title":"DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/html/2511.22134"},{"title":"DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/pdf/2511.22134"},{"title":"A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM","url":"https://arxiv.org/pdf/2410.15549"},{"title":"DualCoT-VLA: Visual-Linguistic Chain of Thought via Parallel Reasoning for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.22280"}]

Based on the search results, here's information about DualVLA arXiv 2511.22134:

## Overview

DualVLA enhances action performance through carefully designed post-training while still preserving reasoning capability.

## The Problem It Addresses

A common strategy to build a generalizable Vision-Language-Action (VLA) model with strong reasoning ability is to first train a specialist VLA on robot demonstrations, then incorporate mixed annotated robot data together with multimodal data to restore broader reasoning capabilities. However, the resulting reasoning VLA often suffers from degraded action performance compared to the specialist model before fine-tuning, a phenomenon referred to as action degeneration.

## Key Technical Contributions

DualVLA introduces a dual-layer data pruning method that removes redundant embodied reasoning, preventing it from adversely influencing action learning. Additionally, it adopts a dual-teacher strategy: an action teacher offering fine-grained supervision for manipulation, and a reasoning teacher maintaining general reasoning capability.

## Results

DualVLA introduces VLA Score, which decouples VLA capabilities into reasoning, intention, action, and alignment for more fine-grained evaluation. Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks.

The paper was posted on arXiv on November 27, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "4351ce21-bdd8-4e37-a022-b903d64c54c3",
  "tool_use_result": {
    "query": "DualVLA arXiv 2511.22134",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GBPNL4crtPB2iuhZUoSpnv",
        "content": [
          {
            "title": "[2511.22134] DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action",
            "url": "https://arxiv.org/abs/2511.22134"
          },
          {
            "title": "DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action",
            "url": "https://arxiv.org/html/2511.22134"
          },
          {
            "title": "DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action",
            "url": "https://arxiv.org/pdf/2511.22134"
          },
          {
            "title": "A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM",
            "url": "https://arxiv.org/pdf/2410.15549"
          },
          {
            "title": "DualCoT-VLA: Visual-Linguistic Chain of Thought via Parallel Reasoning for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.22280"
          }
        ]
      },
      "Based on the search results, here's information about DualVLA arXiv 2511.22134:\n\n## Overview\n\nDualVLA enhances action performance through carefully designed post-training while still preserving reasoning capability.\n\n## The Problem It Addresses\n\nA common strategy to build a generalizable Vision-Language-Action (VLA) model with strong reasoning ability is to first train a specialist VLA on robot demonstrations, then incorporate mixed annotated robot data together with multimodal data to restore broader reasoning capabilities. However, the resulting reasoning VLA often suffers from degraded action performance compared to the specialist model before fine-tuning, a phenomenon referred to as action degeneration.\n\n## Key Technical Contributions\n\nDualVLA introduces a dual-layer data pruning method that removes redundant embodied reasoning, preventing it from adversely influencing action learning. Additionally, it adopts a dual-teacher strategy: an action teacher offering fine-grained supervision for manipulation, and a reasoning teacher maintaining general reasoning capability.\n\n## Results\n\nDualVLA introduces VLA Score, which decouples VLA capabilities into reasoning, intention, action, and alignment for more fine-grained evaluation. Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks.\n\nThe paper was posted on arXiv on November 27, 2025."
    ],
    "durationSeconds": 7.022613547000001
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-24T01:35:37.344Z_

<details><summary>↩ Tool result · `toolu_01F55bwYBcchbTN4GzMTvKin`</summary>

```text
Web search results for query: "From Intention to Execution Probing Generalization Boundaries VLA Models Irving Fang"

Links: [{"title":"[2506.09930] From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.09930"},{"title":"(PDF) From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://www.researchgate.net/publication/392597875_From_Intention_to_Execution_Probing_the_Generalization_Boundaries_of_Vision-Language-Action_Models"},{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://arxiv.org/html/2506.09930v1"},{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.09930"},{"title":"Paper page - From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.09930"},{"title":"Full benchmark results for the original Simpler tasks | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Full-benchmark-results-for-the-original-Simpler-tasks_tbl2_392597875"},{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.09930v1"},{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250609930F/abstract"},{"title":"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models","url":"https://ai4ce.github.io/INT-ACT/"}]

I found the paper for you! Here's information about this research:

"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models" is authored by Irving Fang, Juexiao Zhang, Shengbang Tong, and Chen Feng from New York University.

**Overview:**
The paper focuses on Vision-Language-Action (VLA) models and their promise to leverage the broad generalization capabilities of large Vision-Language Models (VLMs) to produce versatile, "generalist" robot policies.

**Key Problem:**
While VLA models show promise, current evaluations remain insufficient. Traditional imitation learning benchmarks lack language instructions, and emerging benchmarks often have limited evaluation tasks and don't investigate how much VLM pretraining truly contributes to robotic policy generalization.

**Main Contributions:**
The researchers introduce a unified probing suite of 50 simulation-based tasks across 10 subcategories spanning language instruction, vision, and objects.

**Key Findings:**
While VLM backbones endow VLAs with robust perceptual understanding and high level planning (good "intentions"), this does not reliably translate into precise motor execution—when faced with out-of-distribution observations, policies often exhibit coherent intentions but falter in action execution.

They released their task suite and evaluation code as a standardized benchmark for future VLAs to drive research on closing the perception-to-action gap.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "b326c5fd-d206-4e33-bc56-164f5a785f00",
  "tool_use_result": {
    "query": "From Intention to Execution Probing Generalization Boundaries VLA Models Irving Fang",
    "results": [
      {
        "tool_use_id": "srvtoolu_014HTkcxCGceEHHD2j44KXX3",
        "content": [
          {
            "title": "[2506.09930] From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2506.09930"
          },
          {
            "title": "(PDF) From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/392597875_From_Intention_to_Execution_Probing_the_Generalization_Boundaries_of_Vision-Language-Action_Models"
          },
          {
            "title": "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.09930v1"
          },
          {
            "title": "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2506.09930"
          },
          {
            "title": "Paper page - From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2506.09930"
          },
          {
            "title": "Full benchmark results for the original Simpler tasks | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Full-benchmark-results-for-the-original-Simpler-tasks_tbl2_392597875"
          },
          {
            "title": "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2506.09930v1"
          },
          {
            "title": "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250609930F/abstract"
          },
          {
            "title": "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models",
            "url": "https://ai4ce.github.io/INT-ACT/"
          }
        ]
      },
      "I found the paper for you! Here's information about this research:\n\n\"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models\" is authored by Irving Fang, Juexiao Zhang, Shengbang Tong, and Chen Feng from New York University.\n\n**Overview:**\nThe paper focuses on Vision-Language-Action (VLA) models and their promise to leverage the broad generalization capabilities of large Vision-Language Models (VLMs) to produce versatile, \"generalist\" robot policies.\n\n**Key Problem:**\nWhile VLA models show promise, current evaluations remain insufficient. Traditional imitation learning benchmarks lack language instructions, and emerging benchmarks often have limited evaluation tasks and don't investigate how much VLM pretraining truly contributes to robotic policy generalization.\n\n**Main Contributions:**\nThe researchers introduce a unified probing suite of 50 simulation-based tasks across 10 subcategories spanning language instruction, vision, and objects.\n\n**Key Findings:**\nWhile VLM backbones endow VLAs with robust perceptual understanding and high level planning (good \"intentions\"), this does not reliably translate into precise motor execution—when faced with out-of-distribution observations, policies often exhibit coherent intentions but falter in action execution.\n\nThey released their task suite and evaluation code as a standardized benchmark for future VLAs to drive research on closing the perception-to-action gap."
    ],
    "durationSeconds": 9.471026005000004
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have good information. Let me also check whether "From Intention to Execution" specifically discusses "reasoning erosion." The search results mention it focuses on the "intention-to-execution gap" — VLMs have good intentions/understanding but falter in action execution. This is related but not exactly "reasoning erosion" (which is about fine-tuning degrading reasoning capabilities).

Let me also check what DualVLA actually says about reasoning erosion. From the search results, DualVLA discusses "action degeneration" — the phenomenon where adding reasoning to a specialist VLA degrades action performance. This is actually the opposite direction: it's about action degradation when adding reasoning, not reasoning erosion from fine-tuning.


So DualVLA identifies action degeneration when reasoning is added to specialist models, but that's distinct from the broader issue of reasoning erosion where robot fine-tuning erodes the VLM's original reasoning abilities. Neither paper seems to directly address this latter phenomenon, though both touch on related performance trade-offs. I need to look at the actual related_work.tex file to see exactly how fang2025 is cited and what context surrounds it, then check whether "reasoning erosion" is terminology from that paper or something the user introduced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "4088c7c6-6f6d-49e0-b210-8bfb05a5aa28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KkcwNqFLJDcutu9PtCCVWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 567,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 24100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2526
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

_source line 17_

搜索结果已返回。让我看一下论文中的实际引用上下文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "a41f0959-fc8a-4d7e-b34f-e3988ee15f0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KkcwNqFLJDcutu9PtCCVWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 567,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 24100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2526
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

_source line 18_

<details open><summary>🔧 Tool call — Glob · `toolu_01HWcSfz1DdjsNUAWFKqPx6X`</summary>

```json
{
  "pattern": "**/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "9363b26e-38fc-4ca3-85d9-8569346da228",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KkcwNqFLJDcutu9PtCCVWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 567,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 24100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2526
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

_source line 19_

<details open><summary>🔧 Tool call — Glob · `toolu_01Neufi77NBhXbizDJhR65jx`</summary>

```json
{
  "pattern": "**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "2031770e-df84-49bd-9636-17fe95c29af2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KkcwNqFLJDcutu9PtCCVWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 567,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 24100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2526
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

_source line 20 · 2026-05-24T01:35:54.964Z_

<details><summary>↩ Tool result · `toolu_01HWcSfz1DdjsNUAWFKqPx6X`</summary>

```text
artifacts/_project/paper/related_work.tex
docs/paper-a-plus-backup/related_work.tex
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "6bed85e0-008d-49c9-bde8-4a26aaa33c2c",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/related_work.tex",
      "docs/paper-a-plus-backup/related_work.tex",
      "docs/paper/related_work.tex"
    ],
    "durationMs": 23,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T01:35:54.970Z_

<details><summary>↩ Tool result · `toolu_01Neufi77NBhXbizDJhR65jx`</summary>

```text
artifacts/_project/paper/references.bib
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "01164d08-599d-4a72-8d84-a7235cb96b89",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/references.bib",
      "docs/paper/references.bib"
    ],
    "durationMs": 21,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_016ytnGZTRw5Jr7pbVeRdZti`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "94fa94e0-bd76-4611-94a1-148744acc9c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017d3u4e3XXWaNQDkhWh2myo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1391,
      "cache_read_input_tokens": 26626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1391
      },
      "output_tokens": 35,
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

_source line 23 · 2026-05-24T01:35:58.338Z_

<details><summary>↩ Tool result · `toolu_016ytnGZTRw5Jr7pbVeRdZti`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce actions from visual and language input~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora,xiao2025ava}.
5	NLP instruction tuning is well-characterized behaviorally~\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.
6	Fine-tuning operates in a low intrinsic dimension~\cite{aghajanyan2021intrinsic} and can distort pretrained features~\cite{kumar2022finetuning}; existing analyses target single architectures and cannot separate training dynamics from backbone artifacts.
7	
8	\paragraph{Mechanistic and behavioral analysis.}
9	Mechanistic interpretability has revealed residual stream communication~\cite{elhage2021}, induction heads~\cite{olsson2022}, and task circuits~\cite{wang2023_ioi,conmy2023}; causal tracing localizes factual recall~\cite{meng2022_rome}; attention probing shows heads encode syntactic relations~\cite{clark2019} and most can be pruned~\cite{michel2019sixteen}.
10	In VLMs, recent work characterizes visual token redundancy~\cite{fan2026visual} and progressive visual-textual alignment~\cite{neo2025interpreting,long2026understanding}.
11	Behavioral evaluations of VLAs reveal visual dominance~\cite{grant2026,hou2026,fei2025}; mechanistic studies identify sparse semantic directions~\cite{haon2025}, interpretable features~\cite{swann2026,buurmeijer2026}, symbolic representations~\cite{lu2025,molinari2025}, and reasoning erosion~\cite{fang2025}.
12	All prior representational analyses target a single architecture; our $3 \times 4$ cross-architecture matrix tests whether mechanisms replicate across backbone families.
13	
14	\paragraph{Concurrent work.}
15	Three concurrent studies address complementary aspects of VLA understanding.
16	Fang et al.~\cite{fang2026when} construct a behavioral benchmark of counterfactual instruction failures on LIBERO and propose inference-time mitigation; their evaluation measures \emph{whether} the model follows the correct instruction, while our counterfactual perturbation measures \emph{how much} hidden-state geometry changes under instruction replacement (\S\ref{sec:cf_sensitivity}), providing a representational sensitivity metric rather than a behavioral success metric.
17	Our analysis thus provides the internal representational basis that may underlie the vision-override patterns they observe.
18	Buurmeijer et al.~\cite{buurmeijer2026} probe low-level motor features (position, gripper state) in OpenVLA via linear probes and explicitly identify abstract semantic features as future work; instruction-level routing is the focus of our analysis.
19	We additionally distinguish training-associated from inherited effects through trained/reference contrasts across three architectures, a decomposition absent from prior single-architecture studies.
20	
21	\paragraph{Probing and similarity methodology.}
22	RSA~\cite{kriegeskorte2008}, CKA~\cite{kornblith2019}, and linear probes~\cite{alain2017,belinkov2022} provide complementary geometric and functional evaluation.
23	We adopt RSA and MLP probes (CKA in appendix); the two metrics can diverge on the same data (Appendix~\ref{sec:cka_appendix}), and Cohen's $d$ vs.\ cosine distance are not comparable across trained/reference conditions (\S\ref{sec:cf_sensitivity}).
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "775a8aa2-04ba-48b7-9ded-74aec6f3eebd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce actions from visual and language input~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora,xiao2025ava}.\nNLP instruction tuning is well-characterized behaviorally~\\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; existing analyses target single architectures and cannot separate training dynamics from backbone artifacts.\n\n\\paragraph{Mechanistic and behavioral analysis.}\nMechanistic interpretability has revealed residual stream communication~\\cite{elhage2021}, induction heads~\\cite{olsson2022}, and task circuits~\\cite{wang2023_ioi,conmy2023}; causal tracing localizes factual recall~\\cite{meng2022_rome}; attention probing shows heads encode syntactic relations~\\cite{clark2019} and most can be pruned~\\cite{michel2019sixteen}.\nIn VLMs, recent work characterizes visual token redundancy~\\cite{fan2026visual} and progressive visual-textual alignment~\\cite{neo2025interpreting,long2026understanding}.\nBehavioral evaluations of VLAs reveal visual dominance~\\cite{grant2026,hou2026,fei2025}; mechanistic studies identify sparse semantic directions~\\cite{haon2025}, interpretable features~\\cite{swann2026,buurmeijer2026}, symbolic representations~\\cite{lu2025,molinari2025}, and reasoning erosion~\\cite{fang2025}.\nAll prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix tests whether mechanisms replicate across backbone families.\n\n\\paragraph{Concurrent work.}\nThree concurrent studies address complementary aspects of VLA understanding.\nFang et al.~\\cite{fang2026when} construct a behavioral benchmark of counterfactual instruction failures on LIBERO and propose inference-time mitigation; their evaluation measures \\emph{whether} the model follows the correct instruction, while our counterfactual perturbation measures \\emph{how much} hidden-state geometry changes under instruction replacement (\\S\\ref{sec:cf_sensitivity}), providing a representational sensitivity metric rather than a behavioral success metric.\nOur analysis thus provides the internal representational basis that may underlie the vision-override patterns they observe.\nBuurmeijer et al.~\\cite{buurmeijer2026} probe low-level motor features (position, gripper state) in OpenVLA via linear probes and explicitly identify abstract semantic features as future work; instruction-level routing is the focus of our analysis.\nWe additionally distinguish training-associated from inherited effects through trained/reference contrasts across three architectures, a decomposition absent from prior single-architecture studies.\n\n\\paragraph{Probing and similarity methodology.}\nRSA~\\cite{kriegeskorte2008}, CKA~\\cite{kornblith2019}, and linear probes~\\cite{alain2017,belinkov2022} provide complementary geometric and functional evaluation.\nWe adopt RSA and MLP probes (CKA in appendix); the two metrics can diverge on the same data (Appendix~\\ref{sec:cka_appendix}), and Cohen's $d$ vs.\\ cosine distance are not comparable across trained/reference conditions (\\S\\ref{sec:cf_sensitivity}).\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_01TqEr5yuMx2GSXoKXF215Lt`</summary>

```json
{
  "pattern": "fang2025",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "62dc7019-a93e-4d41-ab46-731fbb1110f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017d3u4e3XXWaNQDkhWh2myo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1391,
      "cache_read_input_tokens": 26626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1391
      },
      "output_tokens": 35,
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

_source line 25 · 2026-05-24T01:35:59.336Z_

<details><summary>↩ Tool result · `toolu_01TqEr5yuMx2GSXoKXF215Lt`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-8-\paragraph{Mechanistic and behavioral analysis.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-9-Mechanistic interpretability has revealed residual stream communication~\cite{elhage2021}, induction heads~\cite{olsson2022}, and task circuits~\cite{wang2023_ioi,conmy2023}; causal tracing localizes factual recall~\cite{meng2022_rome}; attention probing shows heads encode syntactic relations~\cite{clark2019} and most can be pruned~\cite{michel2019sixteen}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-10-In VLMs, recent work characterizes visual token redundancy~\cite{fan2026visual} and progressive visual-textual alignment~\cite{neo2025interpreting,long2026understanding}.
docs/paper/related_work.tex:11:Behavioral evaluations of VLAs reveal visual dominance~\cite{grant2026,hou2026,fei2025}; mechanistic studies identify sparse semantic directions~\cite{haon2025}, interpretable features~\cite{swann2026,buurmeijer2026}, symbolic representations~\cite{lu2025,molinari2025}, and reasoning erosion~\cite{fang2025}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-12-All prior representational analyses target a single architecture; our $3 \times 4$ cross-architecture matrix tests whether mechanisms replicate across backbone families.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-13-
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-14-\paragraph{Concurrent work.}
--
docs/paper/main.bbl-262-\newblock \emph{arXiv preprint arXiv:2509.24559}, 2025.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl-263-
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl-264-\bibitem[Fang et~al.(2025)Fang, Liu, Liu, Chen, Zeng, Huang, Chen, Chen, Zhang,
docs/paper/main.bbl:265:  and Zhao]{fang2025}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl-266-Z.~Fang, Z.~Liu, J.~Liu, H.~Chen, Y.~Zeng, S.~Huang, Z.~Chen, L.~Chen,
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl-267-  S.~Zhang, and F.~Zhao.
docs/paper/main.bbl-268-\newblock {DualVLA}: Building a generalizable embodied agent via partial
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib-313-
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib-314-% === VLA Fine-tuning and Reasoning ===
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib-315-
docs/paper/references.bib:316:@article{fang2025,
docs/paper/references.bib-317-  title     = {{DualVLA}: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action},
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib-318-  author    = {Fang, Zhen and Liu, Zhuoyang and Liu, Jiaming and Chen, Hao and Zeng, Yu and Huang, Shiting and Chen, Zehui and Chen, Lin and Zhang, Shanghang and Zhao, Feng},
docs/paper/references.bib-319-  journal   = {arXiv preprint arXiv:2511.22134},
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-31-\citation{haon2025}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-32-\citation{swann2026,buurmeijer2026}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-33-\citation{lu2025,molinari2025}
docs/paper/main.aux:34:\citation{fang2025}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-35-\citation{fang2026when}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-36-\citation{buurmeijer2026}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-37-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-149-\bibcite{buurmeijer2026}{{32}{2026}{{Buurmeijer et~al.}}{{Buurmeijer, Amo~Alonso, Swann, and Pavone}}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-150-\bibcite{lu2025}{{33}{2025}{{Lu et~al.}}{{Lu, Li, Shahani, Herbers, and Scheutz}}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-151-\bibcite{molinari2025}{{34}{2025}{{Molinari et~al.}}{{Molinari, Nevali, Navani, and Younis}}}
docs/paper/main.aux:152:\bibcite{fang2025}{{35}{2025}{{Fang et~al.}}{{Fang, Liu, Liu, Chen, Zeng, Huang, Chen, Chen, Zhang, and Zhao}}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-153-\bibcite{kriegeskorte2008}{{36}{2008}{{Kriegeskorte et~al.}}{{Kriegeskorte, Mur, and Bandettini}}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-154-\bibcite{kornblith2019}{{37}{2019}{{Kornblith et~al.}}{{Kornblith, Norouzi, Lee, and Hinton}}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-155-\bibcite{alain2017}{{38}{2017}{{Alain and Bengio}}{{}}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "d72b44f3-276e-422f-b7c5-6e791030bd0d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-8-\\paragraph{Mechanistic and behavioral analysis.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-9-Mechanistic interpretability has revealed residual stream communication~\\cite{elhage2021}, induction heads~\\cite{olsson2022}, and task circuits~\\cite{wang2023_ioi,conmy2023}; causal tracing localizes factual recall~\\cite{meng2022_rome}; attention probing shows heads encode syntactic relations~\\cite{clark2019} and most can be pruned~\\cite{michel2019sixteen}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-10-In VLMs, recent work characterizes visual token redundancy~\\cite{fan2026visual} and progressive visual-textual alignment~\\cite{neo2025interpreting,long2026understanding}.\ndocs/paper/related_work.tex:11:Behavioral evaluations of VLAs reveal visual dominance~\\cite{grant2026,hou2026,fei2025}; mechanistic studies identify sparse semantic directions~\\cite{haon2025}, interpretable features~\\cite{swann2026,buurmeijer2026}, symbolic representations~\\cite{lu2025,molinari2025}, and reasoning erosion~\\cite{fang2025}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-12-All prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix tests whether mechanisms replicate across backbone families.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-13-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-14-\\paragraph{Concurrent work.}\n--\ndocs/paper/main.bbl-262-\\newblock \\emph{arXiv preprint arXiv:2509.24559}, 2025.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl-263-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl-264-\\bibitem[Fang et~al.(2025)Fang, Liu, Liu, Chen, Zeng, Huang, Chen, Chen, Zhang,\ndocs/paper/main.bbl:265:  and Zhao]{fang2025}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl-266-Z.~Fang, Z.~Liu, J.~Liu, H.~Chen, Y.~Zeng, S.~Huang, Z.~Chen, L.~Chen,\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.bbl-267-  S.~Zhang, and F.~Zhao.\ndocs/paper/main.bbl-268-\\newblock {DualVLA}: Building a generalizable embodied agent via partial\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib-313-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib-314-% === VLA Fine-tuning and Reasoning ===\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib-315-\ndocs/paper/references.bib:316:@article{fang2025,\ndocs/paper/references.bib-317-  title     = {{DualVLA}: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action},\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib-318-  author    = {Fang, Zhen and Liu, Zhuoyang and Liu, Jiaming and Chen, Hao and Zeng, Yu and Huang, Shiting and Chen, Zehui and Chen, Lin and Zhang, Shanghang and Zhao, Feng},\ndocs/paper/references.bib-319-  journal   = {arXiv preprint arXiv:2511.22134},\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-31-\\citation{haon2025}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-32-\\citation{swann2026,buurmeijer2026}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-33-\\citation{lu2025,molinari2025}\ndocs/paper/main.aux:34:\\citation{fang2025}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-35-\\citation{fang2026when}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-36-\\citation{buurmeijer2026}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-37-[Omitted long context line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-149-\\bibcite{buurmeijer2026}{{32}{2026}{{Buurmeijer et~al.}}{{Buurmeijer, Amo~Alonso, Swann, and Pavone}}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-150-\\bibcite{lu2025}{{33}{2025}{{Lu et~al.}}{{Lu, Li, Shahani, Herbers, and Scheutz}}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-151-\\bibcite{molinari2025}{{34}{2025}{{Molinari et~al.}}{{Molinari, Nevali, Navani, and Younis}}}\ndocs/paper/main.aux:152:\\bibcite{fang2025}{{35}{2025}{{Fang et~al.}}{{Fang, Liu, Liu, Chen, Zeng, Huang, Chen, Chen, Zhang, and Zhao}}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-153-\\bibcite{kriegeskorte2008}{{36}{2008}{{Kriegeskorte et~al.}}{{Kriegeskorte, Mur, and Bandettini}}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-154-\\bibcite{kornblith2019}{{37}{2019}{{Kornblith et~al.}}{{Kornblith, Norouzi, Lee, and Hinton}}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.aux-155-\\bibcite{alain2017}{{38}{2017}{{Alain and Bengio}}{{}}}",
    "numLines": 39
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me also check if DualVLA specifically uses the term "reasoning erosion." From the search results, DualVLA discusses "action degeneration" (fine-tuning for reasoning degrades action performance), which is actually the opposite direction from "reasoning erosion" (fine-tuning for actions degrades reasoning).

Actually, wait. Let me re-read the DualVLA description more carefully:

"A common strategy to build a generalizable VLA model with strong reasoning ability is to first train a specialist VLA on robot demonstrations, then incorporate mixed annotated robot data together with multimodal data to restore broader reasoning capabilities. 

However, the resulting reasoning VLA often suffers from degraded action performance compared to the specialist model before fine-tuning, a phenomenon referred to as action degeneration."

So DualVLA is addressing a specific trade-off: when you enhance reasoning capabilities through fine-tuning, the model's action performance degrades. This is distinct from "reasoning erosion," which would describe the opposite problem—where training on robot data erodes the original reasoning abilities of the base VLM. DualVLA tackles this through its dual-teacher approach to preserve both capabilities simultaneously.

Looking at "From Intention to Execution" by Fang et al., they're identifying a different gap—the disconnect between what a VLM backbone understands perceptually and plans conceptually versus what the VLA can actually execute with precision. That's about the intention-to-execution gap, not reasoning erosion either.

So the related_work.tex citation of `fang2025` for "reasoning erosion" seems off. Let me reconsider what DualVLA actually means by its dual-teacher strategy—it's maintaining reasoning capability through one teacher while the other focuses on action performance. DualVLA does acknowledge reasoning erosion as a problem that occurs during VLA training, though it frames the main issue as action degeneration rather than studying reasoning erosion itself. The key question is whether acknowledging a phenomenon counts as a valid citation for it, especially since the paper doesn't use the term "reasoning erosion" explicitly and focuses its contribution elsewhere.

I'm also noticing there are actually two different Fang papers cited in the related work — one is DualVLA and another appears separately in the concurrent work section. Let me check what I've found about DualVLA's actual details to assess whether it's the right fit for this citation.

DualVLA does touch on reasoning erosion but frames it differently — the paper's main focus is "action degeneration" and proposes a dual-teacher approach to balance reasoning preservation with action performance. There's also "From Intention to Execution" which addresses a related but distinct problem about the gap between VLM understanding and VLA execution. Neither is a perfect match for the specific concept of reasoning erosion, though DualVLA comes closer since it at least acknowledges the phenomenon as motivation. DualVLA does acknowledge reasoning erosion as a problem in its motivation, so it's a reasonable citation even if it doesn't deeply explore the concept itself. I should present my findings clearly rather than continuing to search for a more comprehensive treatment of reasoning erosion specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "561129d5-d46e-40b5-a890-74690a9c45d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ey3gcNtCAahRcyNskR4NP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3469,
      "cache_read_input_tokens": 28017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3469
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

_source line 27_

让我再搜索一下 DualVLA 是否具体使用了 "reasoning erosion" 这个术语。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "ab42c787-0fad-4237-a3b1-061fb794193d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ey3gcNtCAahRcyNskR4NP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3469,
      "cache_read_input_tokens": 28017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3469
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Una2L4XSPYv2Fhwyd6Rtnd`</summary>

```json
{
  "query": "DualVLA \"reasoning erosion\" OR \"reasoning degradation\" VLA fine-tuning backbone"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "716a3cb0-5289-48fb-9924-1d6c81c98ece",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ey3gcNtCAahRcyNskR4NP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3469,
      "cache_read_input_tokens": 28017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3469
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

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01891oMamaHym7tbJ5iTW3Wi`</summary>

```json
{
  "query": "\"reasoning erosion\" VLA \"vision-language-action\" arXiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "6bc652a0-7be3-40ae-a3cd-e4059f359efd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ey3gcNtCAahRcyNskR4NP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3469,
      "cache_read_input_tokens": 28017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3469
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

_source line 30 · 2026-05-24T01:36:48.225Z_

<details><summary>↩ Tool result · `toolu_01891oMamaHym7tbJ5iTW3Wi`</summary>

```text
Web search results for query: ""reasoning erosion" VLA "vision-language-action" arXiv 2025 2026"

Links: [{"title":"Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving","url":"https://arxiv.org/pdf/2511.19912"},{"title":"VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning via Online Monte Carlo Tree Search","url":"https://arxiv.org/html/2509.22643v2"},{"title":"[2510.01623] VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.01623"},{"title":"[2509.22643] VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning via Online Monte Carlo Tree Search","url":"https://arxiv.org/abs/2509.22643"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01623v1"},{"title":"[2512.16760] Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future","url":"https://arxiv.org/abs/2512.16760"}]

Based on the search results, I found several relevant papers on Vision-Language-Action (VLA) models from arXiv in 2025 and 2026, though I note that your search query didn't directly return a paper with "reasoning erosion" in the title. Here are the key findings:

## Recent VLA Research (2025-2026):

1. **Reasoning-VLA**: A general and fast action-generation VLA framework for autonomous driving, published in late 2025.

2. **VLA-R1**: A reasoning-enhanced VLA that integrates Reinforcement Learning from Verifiable Rewards (RLVR) with Group Relative Policy Optimization (GRPO) to systematically optimize both reasoning and execution, published in October 2025.

3. **VLA-Reasoner**: A plug-in framework that effectively empowers off-the-shelf VLAs with the capability of foreseeing future states via test-time scaling, published in March 2026.

4. **Vision-Language-Action Models for Autonomous Driving Survey**: A comprehensive review tracing the evolution from early VA approaches to modern VLA frameworks, organizing existing methods into End-to-End VLA and Dual-System VLA paradigms, published in January 2026.

If you're looking for a specific paper on "reasoning erosion" in VLAs, it may not have appeared in these results. Would you like me to search with different terms or provide more details about any of these papers?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "e4abe00c-2776-4ed5-8b49-36977880f280",
  "tool_use_result": {
    "query": "\"reasoning erosion\" VLA \"vision-language-action\" arXiv 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013V7nxdizpbuUFfNV1CRo9m",
        "content": [
          {
            "title": "Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving",
            "url": "https://arxiv.org/pdf/2511.19912"
          },
          {
            "title": "VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning via Online Monte Carlo Tree Search",
            "url": "https://arxiv.org/html/2509.22643v2"
          },
          {
            "title": "[2510.01623] VLA-R1: Enhancing Reasoning in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.01623"
          },
          {
            "title": "[2509.22643] VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning via Online Monte Carlo Tree Search",
            "url": "https://arxiv.org/abs/2509.22643"
          },
          {
            "title": "VLA-R1: Enhancing Reasoning in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.01623v1"
          },
          {
            "title": "[2512.16760] Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future",
            "url": "https://arxiv.org/abs/2512.16760"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on Vision-Language-Action (VLA) models from arXiv in 2025 and 2026, though I note that your search query didn't directly return a paper with \"reasoning erosion\" in the title. Here are the key findings:\n\n## Recent VLA Research (2025-2026):\n\n1. **Reasoning-VLA**: A general and fast action-generation VLA framework for autonomous driving, published in late 2025.\n\n2. **VLA-R1**: A reasoning-enhanced VLA that integrates Reinforcement Learning from Verifiable Rewards (RLVR) with Group Relative Policy Optimization (GRPO) to systematically optimize both reasoning and execution, published in October 2025.\n\n3. **VLA-Reasoner**: A plug-in framework that effectively empowers off-the-shelf VLAs with the capability of foreseeing future states via test-time scaling, published in March 2026.\n\n4. **Vision-Language-Action Models for Autonomous Driving Survey**: A comprehensive review tracing the evolution from early VA approaches to modern VLA frameworks, organizing existing methods into End-to-End VLA and Dual-System VLA paradigms, published in January 2026.\n\nIf you're looking for a specific paper on \"reasoning erosion\" in VLAs, it may not have appeared in these results. Would you like me to search with different terms or provide more details about any of these papers?"
    ],
    "durationSeconds": 6.070598077000002
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T01:36:48.846Z_

<details><summary>↩ Tool result · `toolu_01Una2L4XSPYv2Fhwyd6Rtnd`</summary>

```text
Web search results for query: "DualVLA "reasoning erosion" OR "reasoning degradation" VLA fine-tuning backbone"

Links: [{"title":"DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/pdf/2511.22134"},{"title":"DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/html/2511.22134"},{"title":"[2511.22134] DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/abs/2511.22134"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge","url":"https://arxiv.org/html/2505.21906"},{"title":"Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge","url":"https://arxiv.org/html/2505.21906v1"},{"title":"Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation","url":"https://arxiv.org/pdf/2603.12717"}]

Based on the search results, I found relevant information about DualVLA and the concepts of reasoning degradation/erosion in VLA fine-tuning:

## DualVLA Overview

DualVLA addresses a common challenge in building generalizable Vision-Language-Action (VLA) models: when a specialist VLA trained on robot demonstrations is fine-tuned with mixed annotated-robot data to restore general reasoning, the resulting reasoning VLA exhibits degraded action performance compared to the specialist VLA before fine-tuning. This phenomenon is defined as action degeneration.

## Solution Approach

DualVLA improves action performance through carefully designed post-training while preserving the reasoning ability, using a dual-layer data pruning method to remove redundant embodied reasoning, and a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains and maintains reasoning ability.

## Related Phenomenon: Reasoning Erosion

The search results also reveal a broader concern in the field. Multi-modal understanding and robotic manipulation tasks often compete within the parameter space of dense VLA models, causing them to exhibit erosion of multi-modal comprehension capabilities. This highlights why careful architectural and training strategies like DualVLA's approach are important for maintaining both reasoning and action capabilities in VLA fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "82564952-ca43-4b68-b088-b35eae0cbb18",
  "tool_use_result": {
    "query": "DualVLA \"reasoning erosion\" OR \"reasoning degradation\" VLA fine-tuning backbone",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GWYcL91FwKoobfkJRu596Q",
        "content": [
          {
            "title": "DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action",
            "url": "https://arxiv.org/pdf/2511.22134"
          },
          {
            "title": "DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action",
            "url": "https://arxiv.org/html/2511.22134"
          },
          {
            "title": "[2511.22134] DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action",
            "url": "https://arxiv.org/abs/2511.22134"
          },
          {
            "title": "LangForce: Bayesian Decomposition of Vision Language ...",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge",
            "url": "https://arxiv.org/html/2505.21906"
          },
          {
            "title": "Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge",
            "url": "https://arxiv.org/html/2505.21906v1"
          },
          {
            "title": "Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2603.12717"
          }
        ]
      },
      "Based on the search results, I found relevant information about DualVLA and the concepts of reasoning degradation/erosion in VLA fine-tuning:\n\n## DualVLA Overview\n\nDualVLA addresses a common challenge in building generalizable Vision-Language-Action (VLA) models: when a specialist VLA trained on robot demonstrations is fine-tuned with mixed annotated-robot data to restore general reasoning, the resulting reasoning VLA exhibits degraded action performance compared to the specialist VLA before fine-tuning. This phenomenon is defined as action degeneration.\n\n## Solution Approach\n\nDualVLA improves action performance through carefully designed post-training while preserving the reasoning ability, using a dual-layer data pruning method to remove redundant embodied reasoning, and a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains and maintains reasoning ability.\n\n## Related Phenomenon: Reasoning Erosion\n\nThe search results also reveal a broader concern in the field. Multi-modal understanding and robotic manipulation tasks often compete within the parameter space of dense VLA models, causing them to exhibit erosion of multi-modal comprehension capabilities. This highlights why careful architectural and training strategies like DualVLA's approach are important for maintaining both reasoning and action capabilities in VLA fine-tuning."
    ],
    "durationSeconds": 6.939509105999997
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
The search results mention "erosion of multi-modal comprehension capabilities" — this appears in the context of DualVLA or related work. Let me check if this exact phrasing appears in DualVLA or another paper.

From the first search result: "Multi-modal understanding and robotic manipulation tasks often compete within the parameter space of dense VLA models, causing them to exhibit erosion of multi-modal comprehension capabilities."

This sounds like it could be from DualVLA or a related paper. The term used is "erosion of multi-modal comprehension capabilities" not "reasoning erosion" specifically.

Now let me compile my final analysis:


DualVLA (arXiv:2511.22134) does exist with Zhen Fang et al. as authors. The paper's main contribution focuses on "action degeneration" — where adding reasoning to a specialist VLA degrades action performance. While it acknowledges the erosion of multi-modal comprehension capabilities as background motivation and its dual-teacher approach preserves reasoning, the specific terminology "reasoning erosion" doesn't appear to be what DualVLA itself uses.

The "From Intention to Execution" paper (arXiv:2506.09930) by Irving Fang et al. from NYU addresses the intention-to-execution gap in VLAs, where VLM backbones produce good intentions but poor motor execution — not specifically about reasoning erosion.

So the current `fang2025` citation pointing to DualVLA is somewhat of a stretch. While DualVLA does discuss reasoning erosion as background context, its main contribution is solving action degeneration, which is a different problem. The Irving Fang paper seems like a better fit for the intention-to-execution gap concept, though it's also not specifically framed around reasoning erosion.

I should also check if there's a `fang2026when` entry in the bibliography since related_work.tex cites that as well, then I can provide a complete assessment of the citations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "c8981e5b-3ec5-4a69-88b9-aa6e3228d34c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017MoxDyPoAKZuxWkXdf1f5H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 2523,
      "cache_read_input_tokens": 31486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2523
      },
      "output_tokens": 11,
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

让我也看一下 `fang2026when` 条目，related_work.tex 也引用了它。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "289388ba-3147-441b-a866-3ff207178e25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017MoxDyPoAKZuxWkXdf1f5H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 2523,
      "cache_read_input_tokens": 31486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2523
      },
      "output_tokens": 11,
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

_source line 34_

<details open><summary>🔧 Tool call — Grep · `toolu_01GvPS5MaMcRwtcaCHYoykNU`</summary>

```json
{
  "pattern": "fang2026when",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "output_mode": "content",
  "-A": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "9c5491c8-38cb-4e2b-b6f1-40f08b130958",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017MoxDyPoAKZuxWkXdf1f5H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 2523,
      "cache_read_input_tokens": 31486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2523
      },
      "output_tokens": 11,
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

_source line 35 · 2026-05-24T01:37:09.358Z_

<details><summary>↩ Tool result · `toolu_01GvPS5MaMcRwtcaCHYoykNU`</summary>

```text
307:@article{fang2026when,
308-  title     = {When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in {VLAs}},
309-  author    = {Fang, Kaiyu and Li, Tao and Li, Zhenyu and Zhang, Hao and Guo, Yifeng and Zhang, Liangjun},
310-  journal   = {arXiv preprint arXiv:2602.17659},
311-  year      = {2026},
312-}
313-
314-% === VLA Fine-tuning and Reasoning ===
315-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "ccfbb392-71c0-4bf4-b579-da8420341ebe",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "307:@article{fang2026when,\n308-  title     = {When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in {VLAs}},\n309-  author    = {Fang, Kaiyu and Li, Tao and Li, Zhenyu and Zhang, Hao and Guo, Yifeng and Zhang, Liangjun},\n310-  journal   = {arXiv preprint arXiv:2602.17659},\n311-  year      = {2026},\n312-}\n313-\n314-% === VLA Fine-tuning and Reasoning ===\n315-",
    "numLines": 9
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Interesting. So `fang2026when` is a different paper by a different Fang (Kaiyu Fang), and `fang2025` is DualVLA by Zhen Fang. Neither is the Irving Fang paper from NYU.

Now let me give the final report. The key question is whether DualVLA is the right citation for "reasoning erosion." Based on my research:

1. DualVLA acknowledges reasoning erosion as a background problem (multi-modal comprehension erosion during VLA training) but its main contribution and named phenomenon is "action degeneration"


2. Irving Fang's "From Intention to Execution" addresses the intention-execution gap rather than reasoning erosion specifically
3. The citation works but isn't ideal—DualVLA mentions the concept but doesn't center on it, so if the paper wants to cite reasoning erosion as a primary focus, there might be stronger references available.

I should wrap up my analysis now and prepare the findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "893182ce-acf9-4e68-a118-ecc57c34bd58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xjWtQUmudcAHyZr8poRQN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 34009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1685
      },
      "output_tokens": 9,
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

_source line 37_

核实完成。汇报如下：

---

## DualVLA (arXiv:2511.22134)
- **存在**: 是
- **作者**: Zhen Fang, Zhuoyang Liu, Jiaming Liu, Hao Chen, Yu Zeng, Shiting Huang, Zehui Chen, Lin Chen, Shanghang Zhang, Feng Zhao
- **涉及 reasoning erosion**: 间接涉及。DualVLA 承认 VLA fine-tuning 会导致 "erosion of multi-modal comprehension capabilities"（作为背景动机），但论文的核心命名现象是 **"action degeneration"**（在 specialist VLA 上加推理数据后动作性能下降）。reasoning erosion 是它试图解决的前提问题之一，但不是论文的分析焦点。
- **实际内容**: 提出 dual-teacher 蒸馏策略 + 双层数据剪枝，在保持推理能力的同时提升动作性能。引入 VLA Score 评估指标。

## "From Intention to Execution" (arXiv:2506.09930)
- **存在**: 是
- **作者**: Irving Fang, Juexiao Zhang, Shengbang Tong, Chen Feng (NYU)
- **发表时间**: 2025 年 6 月
- **涉及 reasoning erosion**: 不直接涉及。论文研究的是 **intention-to-execution gap**（VLM backbone 赋予 VLA 良好的感知理解和高层规划，但无法可靠转化为精确动作执行）。
- **核心结论**: 引入 50 个仿真任务的 probing suite，发现 VLA 在 out-of-distribution 观测下表现出 "coherent intentions but falter in action execution"。

## 判断

- **fang2025 引用是否错误**: **有问题，但不算完全错误。** DualVLA 确实讨论了 reasoning erosion 作为背景动机（VLA training 侵蚀多模态理解能力），所以引用它来支撑 "reasoning erosion" 概念是可辩护的。但这不是 DualVLA 的核心贡献或分析焦点——读者去查阅 DualVLA 时，看到的主要是 "action degeneration" 而非 reasoning erosion 的系统性分析。
- **"From Intention to Execution" 不是正确替代**: 这篇论文关注 intention-execution gap，而非 reasoning erosion，且作者是 Irving Fang（NYU），与 DualVLA 的 Zhen Fang 是不同的人。
- **建议修正**:
  1. **如果保留 DualVLA 作为 `fang2025` 的引用**：将 related_work.tex 第 11 行的描述从 "reasoning erosion" 改为更贴合 DualVLA 实际贡献的表述，如 "multi-modal comprehension erosion and action degeneration"
  2. **如果坚持引用 "reasoning erosion" 作为独立概念**：需要找到一篇专门研究此现象的论文（搜索结果中未发现以 "reasoning erosion" 为核心术语的 VLA 论文，这个术语可能是你们论文自己提出的）。如果是你们自己的概念，应在行文中明确说明而非引用他人。
  3. **DualVLA 仍值得引用**：可以在讨论 VLA training trade-off（推理 vs 动作能力之间的冲突）时引用，但应匹配其实际贡献来描述。

Sources:
- [DualVLA (arXiv:2511.22134)](https://arxiv.org/abs/2511.22134)
- [From Intention to Execution (arXiv:2506.09930)](https://arxiv.org/abs/2506.09930)
- [DualVLA HTML](https://arxiv.org/html/2511.22134)
- [From Intention to Execution - Project Page](https://ai4ce.github.io/INT-ACT/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "uuid": "956ff720-648d-46d6-882a-bc4ed5ce4229",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xjWtQUmudcAHyZr8poRQN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 34009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1685
      },
      "output_tokens": 9,
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

_source line 38_

核实完成。汇报如下：

---

## DualVLA (arXiv:2511.22134)
- **存在**: 是
- **作者**: Zhen Fang, Zhuoyang Liu, Jiaming Liu, Hao Chen, Yu Zeng, Shiting Huang, Zehui Chen, Lin Chen, Shanghang Zhang, Feng Zhao
- **涉及 reasoning erosion**: 间接涉及。DualVLA 承认 VLA fine-tuning 会导致 "erosion of multi-modal comprehension capabilities"（作为背景动机），但论文的核心命名现象是 **"action degeneration"**（在 specialist VLA 上加推理数据后动作性能下降）。reasoning erosion 是它试图解决的前提问题之一，但不是论文的分析焦点。
- **实际内容**: 提出 dual-teacher 蒸馏策略 + 双层数据剪枝，在保持推理能力的同时提升动作性能。引入 VLA Score 评估指标。

## "From Intention to Execution" (arXiv:2506.09930)
- **存在**: 是
- **作者**: Irving Fang, Juexiao Zhang, Shengbang Tong, Chen Feng (NYU)
- **发表时间**: 2025 年 6 月
- **涉及 reasoning erosion**: 不直接涉及。论文研究的是 **intention-to-execution gap**（VLM backbone 赋予 VLA 良好的感知理解和高层规划，但无法可靠转化为精确动作执行）。
- **核心结论**: 引入 50 个仿真任务的 probing suite，发现 VLA 在 out-of-distribution 观测下表现出 "coherent intentions but falter in action execution"。

## 判断

- **fang2025 引用是否错误**: **有问题，但不算完全错误。** DualVLA 确实讨论了 reasoning erosion 作为背景动机（VLA training 侵蚀多模态理解能力），所以引用它来支撑 "reasoning erosion" 概念是可辩护的。但这不是 DualVLA 的核心贡献或分析焦点——读者去查阅 DualVLA 时，看到的主要是 "action degeneration" 而非 reasoning erosion 的系统性分析。
- **"From Intention to Execution" 不是正确替代**: 这篇论文关注 intention-execution gap，而非 reasoning erosion，且作者是 Irving Fang（NYU），与 DualVLA 的 Zhen Fang 是不同的人。
- **建议修正**:
  1. **如果保留 DualVLA 作为 `fang2025` 的引用**：将 related_work.tex 第 11 行的描述从 "reasoning erosion" 改为更贴合 DualVLA 实际贡献的表述，如 "multi-modal comprehension erosion and action degeneration"
  2. **如果坚持引用 "reasoning erosion" 作为独立概念**：需要找到一篇专门研究此现象的论文（搜索结果中未发现以 "reasoning erosion" 为核心术语的 VLA 论文，这个术语可能是你们论文自己提出的）。如果是你们自己的概念，应在行文中明确说明而非引用他人。
  3. **DualVLA 仍值得引用**：可以在讨论 VLA training trade-off（推理 vs 动作能力之间的冲突）时引用，但应匹配其实际贡献来描述。

Sources:
- [DualVLA (arXiv:2511.22134)](https://arxiv.org/abs/2511.22134)
- [From Intention to Execution (arXiv:2506.09930)](https://arxiv.org/abs/2506.09930)
- [DualVLA HTML](https://arxiv.org/html/2511.22134)
- [From Intention to Execution - Project Page](https://ai4ce.github.io/INT-ACT/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 147898,
  "duration_api_ms": 173148,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "e7a9d690-7984-496c-8e82-3674ceb7f37f",
  "total_cost_usd": 0.50917775,
  "usage": {
    "input_tokens": 1277,
    "cache_creation_input_tokens": 23853,
    "cache_read_input_tokens": 179537,
    "output_tokens": 5437,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 23853,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1504,
        "cache_read_input_tokens": 34009,
        "cache_creation_input_tokens": 1685,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1685
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 55658,
      "outputTokens": 2472,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 6,
      "costUSD": 0.12801800000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1277,
      "outputTokens": 5437,
      "cacheReadInputTokens": 179537,
      "cacheCreationInputTokens": 23853,
      "webSearchRequests": 0,
      "costUSD": 0.38115975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "65c7dac8-9a63-496b-8314-3fab7ead4b59"
}
```

</details>

---
