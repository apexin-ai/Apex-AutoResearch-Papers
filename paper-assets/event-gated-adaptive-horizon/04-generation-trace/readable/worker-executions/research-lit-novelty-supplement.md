# research lit novelty supplement

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_research_lit-novelty-supplement_20260514T144926.log`
- **Structured JSON:** [`1e9e8d29bccc790f21a3.json`](../../sessions/1e/1e9e8d29bccc790f21a3.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
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
  "uuid": "4cafe7c8-32bc-4379-a0df-5fd7356bf11d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1778778000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "11ebde85-44d7-4889-aa44-de5875eab08d",
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task into parts:

1. First, search for the 2 papers to verify their authenticity
2. Read the current literature_map.yaml
3. Search for the 4 new papers to confirm details
4. Update the literature_map.yaml

Let me start by doing the searches and reading the file in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "64c8d7a9-93dc-4e2c-a2e9-4e36517890ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPecZcKimydyuY9qPYhFCB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12145,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12145
      },
      "output_tokens": 24,
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

_source line 5_

先并行搜索论文和读取现有文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "9aee9e62-d121-4311-8c3d-e9423637f4f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPecZcKimydyuY9qPYhFCB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12145,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12145
      },
      "output_tokens": 24,
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XXoTGUEn7gVUskiYPRqf3R`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "17a7c14e-3cdd-40e6-85d0-35380ce6feef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPecZcKimydyuY9qPYhFCB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12145,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12145
      },
      "output_tokens": 24,
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

_source line 7 · 2026-05-14T14:49:41.385Z_

<details><summary>↩ Tool result · `toolu_01XXoTGUEn7gVUskiYPRqf3R`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "05356710-9586-4595-879b-b761c5094813",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the searches and read the file in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "27db2120-17ce-4b69-b598-cb53f278ffea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSA7cUFMr1FT9PejucCev3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
      },
      "output_tokens": 16,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LiTiuofFNbJybTKjZjmm7F`</summary>

```json
{
  "query": "HarmonyDream ICML 2024 world model observation reward prediction balance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "874b60f0-3ef0-4536-a30f-9ee4b3c86873",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSA7cUFMr1FT9PejucCev3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
      },
      "output_tokens": 16,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DqmC5LQHnKZNBqHg6EbWoT`</summary>

```json
{
  "query": "\"Mind the Model Not the Agent\" Qiao 2023 ECAI 2024 reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "cb2c4050-4397-47c7-9157-6d3f6ceecaa0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSA7cUFMr1FT9PejucCev3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
      },
      "output_tokens": 16,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QwGNJumdDJjVvCXCJk6ViG`</summary>

```json
{
  "query": "NE-Dreamer CoRL 2026 arXiv 2603.02765 next-embedding RSSM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "a263c639-d3ab-4d46-b237-b6ed835c2379",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSA7cUFMr1FT9PejucCev3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
      },
      "output_tokens": 16,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VsanR39tD1H7DMqNG1V1JY`</summary>

```json
{
  "query": "DyMoDreamer 2025 arXiv 2509.24804 dynamic modulation RSSM DreamerV3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "99687369-49a1-4278-8af8-eae50f603612",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSA7cUFMr1FT9PejucCev3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
      },
      "output_tokens": 16,
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NJwUiikVZJdkrJdo4eDvZ4`</summary>

```json
{
  "query": "VanTA semantic temporal abstraction ICLR 2025 VLM-guided"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "cd09ba50-0a7f-498a-a776-203f4b931b10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSA7cUFMr1FT9PejucCev3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
      },
      "output_tokens": 16,
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

_source line 14 · 2026-05-14T14:49:50.364Z_

<details><summary>↩ Tool result · `toolu_01LiTiuofFNbJybTKjZjmm7F`</summary>

```text
Web search results for query: "HarmonyDream ICML 2024 world model observation reward prediction balance"

Links: [{"title":"GitHub - thuml/HarmonyDream: Code release for \"HarmonyDream: Task Harmonization Inside World Models\" (ICML 2024), https://arxiv.org/abs/2310.00344 · GitHub","url":"https://github.com/thuml/harmonydream"},{"title":"ICML Poster HarmonyDream: Task Harmonization Inside World Models","url":"https://icml.cc/virtual/2024/poster/32730"},{"title":"HarmonyDream: Task Harmonization Inside World Models","url":"https://ise.thss.tsinghua.edu.cn/~mlong/doc/HarmonyDream-icml24.pdf"},{"title":"HarmonyDream: Task Harmonization Inside World Models","url":"https://icml.cc/media/icml-2024/Slides/32730.pdf"},{"title":"HarmonyDream: Task Harmonization Inside World Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/harmonydream-task-harmonization-inside-world-models"},{"title":"HarmonyDream: Task Harmonization Inside World Models","url":"https://arxiv.org/html/2310.00344"},{"title":"HarmonyDream: Task Harmonization Inside World Models | OpenReview","url":"https://openreview.net/forum?id=x0yIaw2fgk"},{"title":"Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models","url":"https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"},{"title":"[2310.00344] HarmonyDream: Task Harmonization Inside World Models","url":"https://arxiv.org/abs/2310.00344"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"}]

Based on the search results, here's what I found about HarmonyDream at ICML 2024:

## Overview

HarmonyDream: Task Harmonization Inside World Models was presented at ICML 2024. The paper proposes a new method called HarmonyDream that automatically adjusts the relative importance of observation modeling and reward modeling during the learning process.

## The Core Problem

Model-based reinforcement learning (MBRL) holds the promise of sample-efficient learning by utilizing a world model, which models how the environment works and typically encompasses components for two tasks: observation modeling and reward modeling. 

The key insight is that while prevalent approaches of explicit MBRL attempt to restore abundant details of the environment via observation models, it is difficult due to the environment's complexity and limited model capacity. On the other hand, reward models, while dominating implicit MBRL and adept at learning compact task-centric dynamics, are inadequate for sample-efficient learning without richer learning signals.

## The Solution

HarmonyDream is a simple yet effective approach which automatically adjusts loss coefficients to maintain task harmonization, specifically a dynamic equilibrium between the two tasks in world model learning.

## Key Advantages

The method takes high-dimensional observations as a whole and directly balances the two losses, and does not make assumptions on the distributions behind losses, which makes it possible to balance the KL loss.

## Results

Experiments show that the base MBRL method equipped with HarmonyDream gains 10%-69% absolute performance boosts on visual robotic tasks and sets a new state-of-the-art result on the Atari 100K benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "61ecb3f4-4ec3-421d-996e-28cb00ee2823",
  "tool_use_result": {
    "query": "HarmonyDream ICML 2024 world model observation reward prediction balance",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UXvBDrGvayJeC2MYfHTGfr",
        "content": [
          {
            "title": "GitHub - thuml/HarmonyDream: Code release for \"HarmonyDream: Task Harmonization Inside World Models\" (ICML 2024), https://arxiv.org/abs/2310.00344 · GitHub",
            "url": "https://github.com/thuml/harmonydream"
          },
          {
            "title": "ICML Poster HarmonyDream: Task Harmonization Inside World Models",
            "url": "https://icml.cc/virtual/2024/poster/32730"
          },
          {
            "title": "HarmonyDream: Task Harmonization Inside World Models",
            "url": "https://ise.thss.tsinghua.edu.cn/~mlong/doc/HarmonyDream-icml24.pdf"
          },
          {
            "title": "HarmonyDream: Task Harmonization Inside World Models",
            "url": "https://icml.cc/media/icml-2024/Slides/32730.pdf"
          },
          {
            "title": "HarmonyDream: Task Harmonization Inside World Models | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/harmonydream-task-harmonization-inside-world-models"
          },
          {
            "title": "HarmonyDream: Task Harmonization Inside World Models",
            "url": "https://arxiv.org/html/2310.00344"
          },
          {
            "title": "HarmonyDream: Task Harmonization Inside World Models | OpenReview",
            "url": "https://openreview.net/forum?id=x0yIaw2fgk"
          },
          {
            "title": "Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models",
            "url": "https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"
          },
          {
            "title": "[2310.00344] HarmonyDream: Task Harmonization Inside World Models",
            "url": "https://arxiv.org/abs/2310.00344"
          },
          {
            "title": "ICML 2024 Papers",
            "url": "https://icml.cc/virtual/2024/papers.html"
          }
        ]
      },
      "Based on the search results, here's what I found about HarmonyDream at ICML 2024:\n\n## Overview\n\nHarmonyDream: Task Harmonization Inside World Models was presented at ICML 2024. The paper proposes a new method called HarmonyDream that automatically adjusts the relative importance of observation modeling and reward modeling during the learning process.\n\n## The Core Problem\n\nModel-based reinforcement learning (MBRL) holds the promise of sample-efficient learning by utilizing a world model, which models how the environment works and typically encompasses components for two tasks: observation modeling and reward modeling. \n\nThe key insight is that while prevalent approaches of explicit MBRL attempt to restore abundant details of the environment via observation models, it is difficult due to the environment's complexity and limited model capacity. On the other hand, reward models, while dominating implicit MBRL and adept at learning compact task-centric dynamics, are inadequate for sample-efficient learning without richer learning signals.\n\n## The Solution\n\nHarmonyDream is a simple yet effective approach which automatically adjusts loss coefficients to maintain task harmonization, specifically a dynamic equilibrium between the two tasks in world model learning.\n\n## Key Advantages\n\nThe method takes high-dimensional observations as a whole and directly balances the two losses, and does not make assumptions on the distributions behind losses, which makes it possible to balance the KL loss.\n\n## Results\n\nExperiments show that the base MBRL method equipped with HarmonyDream gains 10%-69% absolute performance boosts on visual robotic tasks and sets a new state-of-the-art result on the Atari 100K benchmark."
    ],
    "durationSeconds": 5.163324148000002
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013YqQRwZhHTveJGgj6Urzqg`</summary>

```json
{
  "query": "Agarwal 2021 \"Deep RL at the Edge of the Statistical Precipice\" NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "e18e226c-b7d6-4f6b-a4b0-3a2472fd3962",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSA7cUFMr1FT9PejucCev3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
      },
      "output_tokens": 16,
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

_source line 16 · 2026-05-14T14:49:51.737Z_

<details><summary>↩ Tool result · `toolu_01DqmC5LQHnKZNBqHg6EbWoT`</summary>

```text
Web search results for query: ""Mind the Model Not the Agent" Qiao 2023 ECAI 2024 reinforcement learning"

Links: [{"title":"IOS Press Ebooks - Mind the Model, Not the Agent: The Primacy Bias in Model-Based RL","url":"https://ebooks.iospress.nl/DOI/10.3233/FAIA240694"},{"title":"About me - Jiafei Lyu’s Home Page","url":"https://dmksjfl.github.io/"},{"title":"Selective Learning for Sample-Efﬁcient Training in Multi-Agent Sparse Reward","url":"https://www.ijcai.org/proceedings/2024/0927.pdf"},{"title":"27th european conference on artificial intelligence","url":"https://www.ecai2024.eu/programme/tutorials/multi-objective-multi-agent-learning-evolutionary-and-reinforcement-learning-perspectives"},{"title":"Accepted Papers | 26th European Conference on Artificial Intelligence ECAI 2023","url":"https://ecai2023.eu/acceptedpapers"},{"title":"eXplainable AI for deep reinforcement learning. | Workshop @ AAAI2024 February, 27th 2024 Vancouver, Canada","url":"https://xai4drl.github.io/"},{"title":"Publications | Chenjia Bai","url":"http://baichenjia.cn/publication/"},{"title":"Xiaoteng Ma (马骁腾) - Homepage","url":"https://xtma.github.io/"},{"title":"Beyond Pipelines: A Survey of the Paradigm Shift toward Model-Native Agentic AI","url":"https://arxiv.org/html/2510.16720v1"},{"title":"Global Rewards in Multi-Agent Deep Reinforcement Learning ...","url":"https://proceedings.mlr.press/v242/hoppe24a/hoppe24a.pdf"}]

I found the paper! Here are the search results for "Mind the Model, Not the Agent: The Primacy Bias in Model-Based RL":

## Paper Details

The paper "Mind the Model, Not the Agent: The Primacy Bias in Model-based RL" was authored by Zhongjian Qiao, Jiafei Lyu, and Xiu Li, and was presented at the European Conference on Artificial Intelligence (ECAI) in 2024.

## Key Findings

The primacy bias in model-based reinforcement learning (MBRL) remained unexplored prior to this work. The researchers observed that resetting the agent's parameters harms its performance in the context of MBRL. 

The main contribution is that the primacy bias in MBRL is more closely related to the primacy bias of the world model instead of the primacy bias of the agent. Based on this finding, the authors propose world model resetting, a simple yet effective technique to alleviate the primacy bias in MBRL.

The paper is published by IOS Press and appears to have been published in October 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "69d4b06c-6b17-4b78-aa21-7d3ff3a43346",
  "tool_use_result": {
    "query": "\"Mind the Model Not the Agent\" Qiao 2023 ECAI 2024 reinforcement learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BSk8qLQirEEMErw38JRQxr",
        "content": [
          {
            "title": "IOS Press Ebooks - Mind the Model, Not the Agent: The Primacy Bias in Model-Based RL",
            "url": "https://ebooks.iospress.nl/DOI/10.3233/FAIA240694"
          },
          {
            "title": "About me - Jiafei Lyu’s Home Page",
            "url": "https://dmksjfl.github.io/"
          },
          {
            "title": "Selective Learning for Sample-Efﬁcient Training in Multi-Agent Sparse Reward",
            "url": "https://www.ijcai.org/proceedings/2024/0927.pdf"
          },
          {
            "title": "27th european conference on artificial intelligence",
            "url": "https://www.ecai2024.eu/programme/tutorials/multi-objective-multi-agent-learning-evolutionary-and-reinforcement-learning-perspectives"
          },
          {
            "title": "Accepted Papers | 26th European Conference on Artificial Intelligence ECAI 2023",
            "url": "https://ecai2023.eu/acceptedpapers"
          },
          {
            "title": "eXplainable AI for deep reinforcement learning. | Workshop @ AAAI2024 February, 27th 2024 Vancouver, Canada",
            "url": "https://xai4drl.github.io/"
          },
          {
            "title": "Publications | Chenjia Bai",
            "url": "http://baichenjia.cn/publication/"
          },
          {
            "title": "Xiaoteng Ma (马骁腾) - Homepage",
            "url": "https://xtma.github.io/"
          },
          {
            "title": "Beyond Pipelines: A Survey of the Paradigm Shift toward Model-Native Agentic AI",
            "url": "https://arxiv.org/html/2510.16720v1"
          },
          {
            "title": "Global Rewards in Multi-Agent Deep Reinforcement Learning ...",
            "url": "https://proceedings.mlr.press/v242/hoppe24a/hoppe24a.pdf"
          }
        ]
      },
      "I found the paper! Here are the search results for \"Mind the Model, Not the Agent: The Primacy Bias in Model-Based RL\":\n\n## Paper Details\n\nThe paper \"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\" was authored by Zhongjian Qiao, Jiafei Lyu, and Xiu Li, and was presented at the European Conference on Artificial Intelligence (ECAI) in 2024.\n\n## Key Findings\n\nThe primacy bias in model-based reinforcement learning (MBRL) remained unexplored prior to this work. The researchers observed that resetting the agent's parameters harms its performance in the context of MBRL. \n\nThe main contribution is that the primacy bias in MBRL is more closely related to the primacy bias of the world model instead of the primacy bias of the agent. Based on this finding, the authors propose world model resetting, a simple yet effective technique to alleviate the primacy bias in MBRL.\n\nThe paper is published by IOS Press and appears to have been published in October 2024."
    ],
    "durationSeconds": 5.5430824780000005
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XVgpsXqdM6JqSDCVbaFCqb`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "fde5aedc-63a9-49ea-ae5b-9f0f491942e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSA7cUFMr1FT9PejucCev3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 23592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1309
      },
      "output_tokens": 16,
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

_source line 18 · 2026-05-14T14:49:55.261Z_

<details><summary>↩ Tool result · `toolu_01QwGNJumdDJjVvCXCJk6ViG`</summary>

```text
Web search results for query: "NE-Dreamer CoRL 2026 arXiv 2603.02765 next-embedding RSSM"

Links: [{"title":"NE-Dreamer: Next Embedding Prediction Makes World Models Stronger","url":"https://corl-team.github.io/nedreamer/"},{"title":"[2603.02765] Next Embedding Prediction Makes World Models Stronger","url":"https://arxiv.org/abs/2603.02765"},{"title":"Next Embedding Prediction Makes World Models Stronger","url":"https://arxiv.org/html/2603.02765"},{"title":"GitHub - corl-team/nedreamer: Official implementation of the paper \"Next Embedding Prediction Makes World Models Stronger\" · GitHub","url":"https://github.com/corl-team/nedreamer"},{"title":"Paper page - Next Embedding Prediction Makes World Models Stronger","url":"https://huggingface.co/papers/2603.02765"},{"title":"NEXT EMBEDDING PREDICTION MAKES WORLD ...","url":"https://openreview.net/pdf/4e331ea63b3cecaf9da5b5312f8d8085c69ea946.pdf"},{"title":"Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction","url":"https://arxiv.org/html/2603.07083"},{"title":"TRANSDREAMER: REINFORCEMENT LEARNING WITH TRANSFORMER WORLD MODELS","url":"https://arxiv.org/pdf/2202.09481"},{"title":"Dreaming: Model-based Reinforcement Learning by Latent ...","url":"https://arxiv.org/pdf/2007.14535"},{"title":"DreamingV2: Reinforcement Learning with Discrete World ...","url":"https://arxiv.org/pdf/2203.00494"}]

I found comprehensive information about NE-Dreamer. Here's what the search results reveal:

## Overview

NE-Dreamer is a decoder-free MBRL agent that leverages a temporal transformer to predict next-step encoder embeddings from latent state sequences, directly optimizing temporal predictive alignment in representation space.

## Key Innovation

NE-Dreamer keeps Dreamer's RSSM dynamics and imagination-based actor–critic, but replaces same-step pixel reconstruction with next-embedding prediction using a causal temporal transformer, improving long-horizon performance under partial observability.

NE-Dreamer replaces pixel-level reconstruction with a simple yet powerful objective: at each timestep, a temporal transformer predicts the next encoder embedding in the sequence, and this prediction is aligned to the actual next-step embedding using a redundancy-reduction metric (specifically, Barlow Twins in our implementation).

## Benefits

This approach enables NE-Dreamer to learn coherent, predictive state representations without reconstruction losses or auxiliary supervision.

## Performance

On the DeepMind Control Suite, NE-Dreamer matches or exceeds the performance of DreamerV3 and leading decoder-free agents. On a challenging subset of DMLab tasks involving memory and spatial reasoning, NE-Dreamer achieves substantial gains.

## Paper Details

The paper was authored by George Bredis, Nikita Balagansky, Daniil Gavrilov, and Ruslan Rakhimov in 2026, with arXiv identifier 2603.02765.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "b3f6d304-0fff-4c47-a793-38748df6d1d1",
  "tool_use_result": {
    "query": "NE-Dreamer CoRL 2026 arXiv 2603.02765 next-embedding RSSM",
    "results": [
      {
        "tool_use_id": "srvtoolu_012o3BwRTr8eKBpabjLoi5dS",
        "content": [
          {
            "title": "NE-Dreamer: Next Embedding Prediction Makes World Models Stronger",
            "url": "https://corl-team.github.io/nedreamer/"
          },
          {
            "title": "[2603.02765] Next Embedding Prediction Makes World Models Stronger",
            "url": "https://arxiv.org/abs/2603.02765"
          },
          {
            "title": "Next Embedding Prediction Makes World Models Stronger",
            "url": "https://arxiv.org/html/2603.02765"
          },
          {
            "title": "GitHub - corl-team/nedreamer: Official implementation of the paper \"Next Embedding Prediction Makes World Models Stronger\" · GitHub",
            "url": "https://github.com/corl-team/nedreamer"
          },
          {
            "title": "Paper page - Next Embedding Prediction Makes World Models Stronger",
            "url": "https://huggingface.co/papers/2603.02765"
          },
          {
            "title": "NEXT EMBEDDING PREDICTION MAKES WORLD ...",
            "url": "https://openreview.net/pdf/4e331ea63b3cecaf9da5b5312f8d8085c69ea946.pdf"
          },
          {
            "title": "Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction",
            "url": "https://arxiv.org/html/2603.07083"
          },
          {
            "title": "TRANSDREAMER: REINFORCEMENT LEARNING WITH TRANSFORMER WORLD MODELS",
            "url": "https://arxiv.org/pdf/2202.09481"
          },
          {
            "title": "Dreaming: Model-based Reinforcement Learning by Latent ...",
            "url": "https://arxiv.org/pdf/2007.14535"
          },
          {
            "title": "DreamingV2: Reinforcement Learning with Discrete World ...",
            "url": "https://arxiv.org/pdf/2203.00494"
          }
        ]
      },
      "I found comprehensive information about NE-Dreamer. Here's what the search results reveal:\n\n## Overview\n\nNE-Dreamer is a decoder-free MBRL agent that leverages a temporal transformer to predict next-step encoder embeddings from latent state sequences, directly optimizing temporal predictive alignment in representation space.\n\n## Key Innovation\n\nNE-Dreamer keeps Dreamer's RSSM dynamics and imagination-based actor–critic, but replaces same-step pixel reconstruction with next-embedding prediction using a causal temporal transformer, improving long-horizon performance under partial observability.\n\nNE-Dreamer replaces pixel-level reconstruction with a simple yet powerful objective: at each timestep, a temporal transformer predicts the next encoder embedding in the sequence, and this prediction is aligned to the actual next-step embedding using a redundancy-reduction metric (specifically, Barlow Twins in our implementation).\n\n## Benefits\n\nThis approach enables NE-Dreamer to learn coherent, predictive state representations without reconstruction losses or auxiliary supervision.\n\n## Performance\n\nOn the DeepMind Control Suite, NE-Dreamer matches or exceeds the performance of DreamerV3 and leading decoder-free agents. On a challenging subset of DMLab tasks involving memory and spatial reasoning, NE-Dreamer achieves substantial gains.\n\n## Paper Details\n\nThe paper was authored by George Bredis, Nikita Balagansky, Daniil Gavrilov, and Ruslan Rakhimov in 2026, with arXiv identifier 2603.02765."
    ],
    "durationSeconds": 7.5893173769999995
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T14:49:57.024Z_

<details><summary>↩ Tool result · `toolu_013YqQRwZhHTveJGgj6Urzqg`</summary>

```text
Web search results for query: "Agarwal 2021 "Deep RL at the Edge of the Statistical Precipice" NeurIPS"

Links: [{"title":"GitHub - google-research/rliable: [NeurIPS'21 Outstanding Paper] Library for reliable evaluation on RL and ML benchmarks, even with only a handful of seeds. · GitHub","url":"https://github.com/google-research/rliable"},{"title":"Deep Reinforcement Learning at the Edge of the Statistical Precipice","url":"https://proceedings.neurips.cc/paper_files/paper/2021/file/f514cec81cb148559cf475e7426eed5e-Paper.pdf"},{"title":"[2108.13264] Deep Reinforcement Learning at the Edge of the Statistical Precipice","url":"https://arxiv.org/abs/2108.13264"},{"title":"Deep RL at the Edge of the Statistical Precipice","url":"https://agarwl.github.io/rliable/"},{"title":"Deep Reinforcement Learning at the Edge of the Statistical Precipice","url":"https://psc-g.github.io/posts/research/rl/precipice/"},{"title":"[PDF] Deep Reinforcement Learning at the Edge of the Statistical Precipice | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-Reinforcement-Learning-at-the-Edge-of-the-Agarwal-Schwarzer/558ca2e8c7eb56edd77a52b084e6cc24dffe5bcd"},{"title":"[Quick Review] Deep Reinforcement Learning at the Edge of the Statistical Precipice","url":"https://liner.com/review/deep-reinforcement-learning-at-the-edge-of-the-statistical-precipice"},{"title":"Deep Reinforcement Learning at the Edge of the Statistical Precipice | TransferLab — appliedAI Institute","url":"https://transferlab.ai/refs/agarwal_deep_2021/"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=R.+Agarwal%2C+M.+Schwarzer%2C+P.+Samuel+Castro%2C+A.+C.+Courville%2C+and+M.+G.+Bellemare.+2021.+Deep+reinforcement+learning+at+the+edge+of+the+statistical+precipice.+In+Proceedings+of+the+35th+International+Conference+on+Advances+in+Neural+Information+Processing+Systems+%28NeurIPS%2721%29%2C+M.+Ranzato%2C+A.+Beygelzimer%2C+K.+Nguyen%2C+P.+Liang%2C+J.+Vaughan%2C+and+Y.+Dauphin+%28Eds.%29.+Curran+Associates."},{"title":"Deep RL at the Edge of the Statistical Precipice (NeurIPS Best Paper) - YouTube","url":"https://www.youtube.com/watch?v=XSY9JwqD-bw"}]

I found the paper you're looking for! Here's what I found:

## "Deep Reinforcement Learning at the Edge of the Statistical Precipice"

This paper was authored by Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron C. Courville, and Marc Bellemare, and published in Advances in Neural Information Processing Systems in 2021. The work received an outstanding paper award at NeurIPS 2021.

### Main Contribution

The paper argues that most published results on deep RL benchmarks compare point estimates of aggregate performance such as mean and median scores across tasks, ignoring statistical uncertainty from finite training runs. The shift towards computationally-demanding benchmarks has led to evaluating only a small number of runs per task, exacerbating statistical uncertainty.

To address this, the authors advocate for reporting interval estimates of aggregate performance and propose performance profiles to account for variability in results, as well as present more robust and efficient aggregate metrics, such as interquartile mean scores.

### Practical Impact

The authors present a more rigorous evaluation methodology accompanied with an open-source library called rliable, to prevent unreliable results from stagnating the field.

The paper includes case studies on multiple RL benchmarks including Atari 100k, the Arcade Learning Environment (ALE), Procgen, and the DeepMind Control Suite.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "d9a5e211-c29d-4178-a327-bd939a874d85",
  "tool_use_result": {
    "query": "Agarwal 2021 \"Deep RL at the Edge of the Statistical Precipice\" NeurIPS",
    "results": [
      {
        "tool_use_id": "srvtoolu_01468gnL6gMeePstUX2iHcXc",
        "content": [
          {
            "title": "GitHub - google-research/rliable: [NeurIPS'21 Outstanding Paper] Library for reliable evaluation on RL and ML benchmarks, even with only a handful of seeds. · GitHub",
            "url": "https://github.com/google-research/rliable"
          },
          {
            "title": "Deep Reinforcement Learning at the Edge of the Statistical Precipice",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2021/file/f514cec81cb148559cf475e7426eed5e-Paper.pdf"
          },
          {
            "title": "[2108.13264] Deep Reinforcement Learning at the Edge of the Statistical Precipice",
            "url": "https://arxiv.org/abs/2108.13264"
          },
          {
            "title": "Deep RL at the Edge of the Statistical Precipice",
            "url": "https://agarwl.github.io/rliable/"
          },
          {
            "title": "Deep Reinforcement Learning at the Edge of the Statistical Precipice",
            "url": "https://psc-g.github.io/posts/research/rl/precipice/"
          },
          {
            "title": "[PDF] Deep Reinforcement Learning at the Edge of the Statistical Precipice | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Deep-Reinforcement-Learning-at-the-Edge-of-the-Agarwal-Schwarzer/558ca2e8c7eb56edd77a52b084e6cc24dffe5bcd"
          },
          {
            "title": "[Quick Review] Deep Reinforcement Learning at the Edge of the Statistical Precipice",
            "url": "https://liner.com/review/deep-reinforcement-learning-at-the-edge-of-the-statistical-precipice"
          },
          {
            "title": "Deep Reinforcement Learning at the Edge of the Statistical Precipice | TransferLab — appliedAI Institute",
            "url": "https://transferlab.ai/refs/agarwal_deep_2021/"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar?q=R.+Agarwal%2C+M.+Schwarzer%2C+P.+Samuel+Castro%2C+A.+C.+Courville%2C+and+M.+G.+Bellemare.+2021.+Deep+reinforcement+learning+at+the+edge+of+the+statistical+precipice.+In+Proceedings+of+the+35th+International+Conference+on+Advances+in+Neural+Information+Processing+Systems+%28NeurIPS%2721%29%2C+M.+Ranzato%2C+A.+Beygelzimer%2C+K.+Nguyen%2C+P.+Liang%2C+J.+Vaughan%2C+and+Y.+Dauphin+%28Eds.%29.+Curran+Associates."
          },
          {
            "title": "Deep RL at the Edge of the Statistical Precipice (NeurIPS Best Paper) - YouTube",
            "url": "https://www.youtube.com/watch?v=XSY9JwqD-bw"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\n## \"Deep Reinforcement Learning at the Edge of the Statistical Precipice\"\n\nThis paper was authored by Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron C. Courville, and Marc Bellemare, and published in Advances in Neural Information Processing Systems in 2021. The work received an outstanding paper award at NeurIPS 2021.\n\n### Main Contribution\n\nThe paper argues that most published results on deep RL benchmarks compare point estimates of aggregate performance such as mean and median scores across tasks, ignoring statistical uncertainty from finite training runs. The shift towards computationally-demanding benchmarks has led to evaluating only a small number of runs per task, exacerbating statistical uncertainty.\n\nTo address this, the authors advocate for reporting interval estimates of aggregate performance and propose performance profiles to account for variability in results, as well as present more robust and efficient aggregate metrics, such as interquartile mean scores.\n\n### Practical Impact\n\nThe authors present a more rigorous evaluation methodology accompanied with an open-source library called rliable, to prevent unreliable results from stagnating the field.\n\nThe paper includes case studies on multiple RL benchmarks including Atari 100k, the Arcade Learning Environment (ALE), Procgen, and the DeepMind Control Suite."
    ],
    "durationSeconds": 6.056546129000002
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T14:49:57.321Z_

<details><summary>↩ Tool result · `toolu_01NJwUiikVZJdkrJdo4eDvZ4`</summary>

```text
Web search results for query: "VanTA semantic temporal abstraction ICLR 2025 VLM-guided"

Links: [{"title":"SEMANTIC TEMPORAL ABSTRACTION VIA VISION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7c8c0db90a14c7a2db9475e52dc343a9-Paper-Conference.pdf"},{"title":"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=zY37C8d6bS"},{"title":"ICLR Poster Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning","url":"https://iclr.cc/virtual/2025/poster/27665"},{"title":"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/7c8c0db90a14c7a2db9475e52dc343a9-Abstract-Conference.html"},{"title":"Semantic Temporal Abstraction via Vision-Language ...","url":"https://iclr.cc/media/iclr-2025/Slides/27665_0737VV2.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf"},{"title":"dblp: Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning.","url":"https://dblp.dagstuhl.de/rec/conf/iclr/LiuL0JWZ025.html"},{"title":"Vision Language Models: A Survey of 26K Papers (CVPR, ICLR, NeurIPS 2023–2025)","url":"https://arxiv.org/pdf/2510.09586"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Towards Comprehensive Reasoning in Vision-Language Models | ICCV 2025","url":"https://wangywust.github.io/iccv-tutorial-reasoning-vlm/"}]

Based on the search results, I found information about VanTA from ICLR 2025:

## VanTA: Vision-Language Model Guided Temporal Abstraction

VanTA (Vision-language model guided Temporal Abstraction) facilitates the discovery of more interpretable and task-relevant temporal segmentations from offline data without the need for extensive manual intervention or heuristics.

### Overview

VanTA is a novel approach that leverages the prior knowledge of VLMs to decompose trajectories into reasonable subsequences. The method progressively guides the latent space after vector quantization to be more semantically meaningful through relabeling each skill.

### Key Contributions

Extracting temporally extended skills can significantly improve the efficiency of reinforcement learning by breaking down complex decision-making problems with sparse rewards into simpler subtasks and enabling more effective credit assignment. Existing abstraction methods either discover skills in an unsupervised manner, which often lacks semantic information and leads to erroneous or scattered skill extraction results, or require substantial human intervention.

### Performance

The effectiveness of the approach is validated through extensive experiments on diverse environments, including Franka Kitchen, Minigrid, and Crafter, with the method surpassing existing approaches in long-horizon offline reinforcement learning scenarios with both proprioceptive and visual observations.

The paper was authored by Tian-Shuo Liu, Xu-Hui Liu, Ruifeng Chen, Lixuan Jin, Pengyuan Wang, Zhilong Zhang, and Yang Yu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "6ee5eeab-1200-4c1e-80e6-8ab840e3eb36",
  "tool_use_result": {
    "query": "VanTA semantic temporal abstraction ICLR 2025 VLM-guided",
    "results": [
      {
        "tool_use_id": "srvtoolu_011CEVtg19Zxy938RUicFrXR",
        "content": [
          {
            "title": "SEMANTIC TEMPORAL ABSTRACTION VIA VISION",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/7c8c0db90a14c7a2db9475e52dc343a9-Paper-Conference.pdf"
          },
          {
            "title": "Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=zY37C8d6bS"
          },
          {
            "title": "ICLR Poster Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning",
            "url": "https://iclr.cc/virtual/2025/poster/27665"
          },
          {
            "title": "Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/7c8c0db90a14c7a2db9475e52dc343a9-Abstract-Conference.html"
          },
          {
            "title": "Semantic Temporal Abstraction via Vision-Language ...",
            "url": "https://iclr.cc/media/iclr-2025/Slides/27665_0737VV2.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf"
          },
          {
            "title": "dblp: Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning.",
            "url": "https://dblp.dagstuhl.de/rec/conf/iclr/LiuL0JWZ025.html"
          },
          {
            "title": "Vision Language Models: A Survey of 26K Papers (CVPR, ICLR, NeurIPS 2023–2025)",
            "url": "https://arxiv.org/pdf/2510.09586"
          },
          {
            "title": "ICLR 2025 Papers",
            "url": "https://iclr.cc/virtual/2025/papers.html"
          },
          {
            "title": "Towards Comprehensive Reasoning in Vision-Language Models | ICCV 2025",
            "url": "https://wangywust.github.io/iccv-tutorial-reasoning-vlm/"
          }
        ]
      },
      "Based on the search results, I found information about VanTA from ICLR 2025:\n\n## VanTA: Vision-Language Model Guided Temporal Abstraction\n\nVanTA (Vision-language model guided Temporal Abstraction) facilitates the discovery of more interpretable and task-relevant temporal segmentations from offline data without the need for extensive manual intervention or heuristics.\n\n### Overview\n\nVanTA is a novel approach that leverages the prior knowledge of VLMs to decompose trajectories into reasonable subsequences. The method progressively guides the latent space after vector quantization to be more semantically meaningful through relabeling each skill.\n\n### Key Contributions\n\nExtracting temporally extended skills can significantly improve the efficiency of reinforcement learning by breaking down complex decision-making problems with sparse rewards into simpler subtasks and enabling more effective credit assignment. Existing abstraction methods either discover skills in an unsupervised manner, which often lacks semantic information and leads to erroneous or scattered skill extraction results, or require substantial human intervention.\n\n### Performance\n\nThe effectiveness of the approach is validated through extensive experiments on diverse environments, including Franka Kitchen, Minigrid, and Crafter, with the method surpassing existing approaches in long-horizon offline reinforcement learning scenarios with both proprioceptive and visual observations.\n\nThe paper was authored by Tian-Shuo Liu, Xu-Hui Liu, Ruifeng Chen, Lixuan Jin, Pengyuan Wang, Zhilong Zhang, and Yang Yu."
    ],
    "durationSeconds": 7.774327108999998
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T14:49:59.387Z_

<details><summary>↩ Tool result · `toolu_01VsanR39tD1H7DMqNG1V1JY`</summary>

```text
Web search results for query: "DyMoDreamer 2025 arXiv 2509.24804 dynamic modulation RSSM DreamerV3"

Links: [{"title":"[2509.24804] DyMoDreamer: World Modeling with Dynamic Modulation","url":"https://arxiv.org/abs/2509.24804"},{"title":"DyMoDreamer: World Modeling with Dynamic Modulation","url":"https://arxiv.org/pdf/2509.24804"},{"title":"NeurIPS Poster DyMoDreamer: World Modeling with Dynamic Modulation","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/117925"},{"title":"DyMoDreamer: World Modeling with Dynamic Modulation | OpenReview","url":"https://openreview.net/forum?id=SYKwGnik3w"},{"title":"Intrinsic Mutual Information as a Modulator for Preference Optimization","url":"https://arxiv.org/html/2604.24804"},{"title":"[2503.18783] Frequency Dynamic Convolution for Dense Image Prediction","url":"https://arxiv.org/abs/2503.18783"},{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"Balanced Multimodal Learning: An Unidirectional Dynamic Interaction Perspective","url":"https://arxiv.org/html/2509.02281"},{"title":"Frequency-Dynamic Attention Modulation for Dense Prediction Linwei Chen1","url":"https://arxiv.org/pdf/2507.12006"},{"title":"[2509.23058] Risk Profiling and Modulation for LLMs","url":"https://arxiv.org/abs/2509.23058"}]

Based on the search results, here's information about DyMoDreamer:

## Overview

DyMoDreamer is a novel model-based reinforcement learning (MBRL) algorithm that incorporates a dynamic modulation mechanism to improve the extraction of dynamic features and enrich temporal information.

## Key Technical Features

DyMoDreamer employs differential observations derived from a novel inter-frame differencing mask, explicitly encoding object-level motion cues and temporal dynamics. Dynamic modulation is modeled as stochastic categorical distributions and integrated into a recurrent state-space model (RSSM), enhancing the model's focus on reward-relevant dynamics.

## Problem Addressed

Conventional world models process observations holistically, failing to decouple dynamic objects and temporal features from static backgrounds, which is computationally inefficient, especially for visual tasks where dynamic objects significantly influence rewards and decision-making performance.

## Empirical Results

DyMoDreamer sets a new state-of-the-art on the Atari 100k benchmark with a 156.6% mean human-normalized score, establishes a new record of 832 on the DeepMind Visual Control Suite, and gains a 9.5% performance improvement after 1M steps on the Crafter benchmark.

## Relationship to DreamerV3

The approach is mainly based on DreamerV3, introducing dynamic modulation into the RSSM world model architecture.

The paper was published on arXiv on September 29, 2025, and was presented as a poster at NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "1e1556cd-6acb-4718-9dd2-6369a21e581b",
  "tool_use_result": {
    "query": "DyMoDreamer 2025 arXiv 2509.24804 dynamic modulation RSSM DreamerV3",
    "results": [
      {
        "tool_use_id": "srvtoolu_013ehGED8nH7469XRKzraaon",
        "content": [
          {
            "title": "[2509.24804] DyMoDreamer: World Modeling with Dynamic Modulation",
            "url": "https://arxiv.org/abs/2509.24804"
          },
          {
            "title": "DyMoDreamer: World Modeling with Dynamic Modulation",
            "url": "https://arxiv.org/pdf/2509.24804"
          },
          {
            "title": "NeurIPS Poster DyMoDreamer: World Modeling with Dynamic Modulation",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/117925"
          },
          {
            "title": "DyMoDreamer: World Modeling with Dynamic Modulation | OpenReview",
            "url": "https://openreview.net/forum?id=SYKwGnik3w"
          },
          {
            "title": "Intrinsic Mutual Information as a Modulator for Preference Optimization",
            "url": "https://arxiv.org/html/2604.24804"
          },
          {
            "title": "[2503.18783] Frequency Dynamic Convolution for Dense Image Prediction",
            "url": "https://arxiv.org/abs/2503.18783"
          },
          {
            "title": "DreamerV3: Mastering Diverse Domains through World Models",
            "url": "https://vitalab.github.io/article/2023/01/19/DreamerV3.html"
          },
          {
            "title": "Balanced Multimodal Learning: An Unidirectional Dynamic Interaction Perspective",
            "url": "https://arxiv.org/html/2509.02281"
          },
          {
            "title": "Frequency-Dynamic Attention Modulation for Dense Prediction Linwei Chen1",
            "url": "https://arxiv.org/pdf/2507.12006"
          },
          {
            "title": "[2509.23058] Risk Profiling and Modulation for LLMs",
            "url": "https://arxiv.org/abs/2509.23058"
          }
        ]
      },
      "Based on the search results, here's information about DyMoDreamer:\n\n## Overview\n\nDyMoDreamer is a novel model-based reinforcement learning (MBRL) algorithm that incorporates a dynamic modulation mechanism to improve the extraction of dynamic features and enrich temporal information.\n\n## Key Technical Features\n\nDyMoDreamer employs differential observations derived from a novel inter-frame differencing mask, explicitly encoding object-level motion cues and temporal dynamics. Dynamic modulation is modeled as stochastic categorical distributions and integrated into a recurrent state-space model (RSSM), enhancing the model's focus on reward-relevant dynamics.\n\n## Problem Addressed\n\nConventional world models process observations holistically, failing to decouple dynamic objects and temporal features from static backgrounds, which is computationally inefficient, especially for visual tasks where dynamic objects significantly influence rewards and decision-making performance.\n\n## Empirical Results\n\nDyMoDreamer sets a new state-of-the-art on the Atari 100k benchmark with a 156.6% mean human-normalized score, establishes a new record of 832 on the DeepMind Visual Control Suite, and gains a 9.5% performance improvement after 1M steps on the Crafter benchmark.\n\n## Relationship to DreamerV3\n\nThe approach is mainly based on DreamerV3, introducing dynamic modulation into the RSSM world model architecture.\n\nThe paper was published on arXiv on September 29, 2025, and was presented as a poster at NeurIPS 2025."
    ],
    "durationSeconds": 10.779143757999998
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T14:49:59.407Z_

<details><summary>↩ Tool result · `toolu_01XVgpsXqdM6JqSDCVbaFCqb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\", \"content\": \"# Literature Map — event-gated-adaptive-horizon\\n# Last updated: 2026-05-14\\n# Total: 39 papers (5 existing + 34 new)\\n\\n# ============================================================\\n# EXISTING CITATIONS (already in paper.tex)\\n# ============================================================\\n\\n- paper_id: sutton1999options\\n  title: \\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\"\\n  authors: [Sutton R.S., Precup D., Singh S.]\\n  year: 1999\\n  venue: \\\"Artificial Intelligence 112(1-2):181-211\\\"\\n  category: background\\n  role: \\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2020dreamerv1\\n  title: \\\"Dream to Control: Learning Behaviors by Latent Imagination\\\"\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\n  year: 2020\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2023dreamerv3\\n  title: \\\"Mastering Diverse Domains through World Models\\\"\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\n  year: 2023\\n  venue: \\\"arXiv:2301.04104 (Nature 2025)\\\"\\n  category: background\\n  role: \\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\"\\n  relevance_score: 5\\n\\n- paper_id: sharma2017figar\\n  title: \\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\n  year: 2017\\n  venue: \\\"ICLR Workshop\\\"\\n  category: method-component\\n  role: \\\"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\\\"\\n  relevance_score: 4\\n\\n- paper_id: janner2019mbpo\\n  title: \\\"When to Trust Your Model: Model-Based Policy Optimization\\\"\\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\\n  year: 2019\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Multi-step prediction error compounding\\n# ============================================================\\n\\n- paper_id: ke2019learning\\n  title: \\\"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\\\"\\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\\n  year: 2019\\n  venue: ICLR\\n  category: background\\n  role: \\\"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\\\"\\n  relevance_score: 4\\n\\n- paper_id: asadi2019combating\\n  title: \\\"Combating the Compounding-Error Problem with a Multi-step Model\\\"\\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\\n  year: 2019\\n  venue: \\\"arXiv:1905.13320\\\"\\n  category: background\\n  role: \\\"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\\\"\\n  relevance_score: 4\\n\\n- paper_id: venkatraman2015improving\\n  title: \\\"Improving Multi-Step Prediction of Learned Time Series Models\\\"\\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\\n  year: 2015\\n  venue: AAAI\\n  category: background\\n  role: \\\"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\\\"\\n  relevance_score: 3\\n\\n- paper_id: lambert2022investigating\\n  title: \\\"Investigating Compounding Prediction Errors in Learned Dynamics Models\\\"\\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\\n  year: 2022\\n  venue: \\\"arXiv:2203.09637\\\"\\n  category: background\\n  role: \\\"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Model-predictive control with learned dynamics\\n# ============================================================\\n\\n- paper_id: chua2018pets\\n  title: \\\"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\\\"\\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\\\"\\n  relevance_score: 3\\n\\n- paper_id: nagabandi2018neural\\n  title: \\\"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\\\"\\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\\n  year: 2018\\n  venue: ICRA\\n  category: background\\n  role: \\\"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Value overestimation mitigation\\n# ============================================================\\n\\n- paper_id: thrun1993issues\\n  title: \\\"Issues in Using Function Approximation for Reinforcement Learning\\\"\\n  authors: [Thrun S., Schwartz A.]\\n  year: 1993\\n  venue: \\\"Connectionist Models Summer School\\\"\\n  category: background\\n  role: \\\"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\\\"\\n  relevance_score: 4\\n\\n- paper_id: vanhasselt2016double\\n  title: \\\"Deep Reinforcement Learning with Double Q-Learning\\\"\\n  authors: [van Hasselt H., Guez A., Silver D.]\\n  year: 2016\\n  venue: AAAI\\n  category: background\\n  role: \\\"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\\\"\\n  relevance_score: 4\\n\\n- paper_id: fujimoto2018td3\\n  title: \\\"Addressing Function Approximation Error in Actor-Critic Methods\\\"\\n  authors: [Fujimoto S., van Hoof H., Meger D.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\\\"\\n  relevance_score: 4\\n\\n- paper_id: haarnoja2018sac\\n  title: \\\"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\\\"\\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\\\"\\n  relevance_score: 3\\n\\n- paper_id: lee2021sunrise\\n  title: \\\"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\\\"\\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Delusional bias\\n# ============================================================\\n\\n- paper_id: lu2018nondelusional\\n  title: \\\"Non-delusional Q-learning and Value-Iteration\\\"\\n  authors: [Lu T., Schuurmans D., Boutilier C.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Hierarchical RL with learned models\\n# ============================================================\\n\\n- paper_id: hafner2022director\\n  title: \\\"Deep Hierarchical Planning from Pixels\\\"\\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\\n  year: 2022\\n  venue: NeurIPS\\n  category: direct-competitor\\n  role: \\\"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\\\"\\n  relevance_score: 4\\n\\n- paper_id: nachum2018hiro\\n  title: \\\"Data-Efficient Hierarchical Reinforcement Learning\\\"\\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Action repeat / frame skip\\n# ============================================================\\n\\n- paper_id: braylan2015frame\\n  title: \\\"Frame Skip Is a Powerful Parameter for Learning to Play Atari\\\"\\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\\n  year: 2015\\n  venue: \\\"AAAI Workshop on Learning for General Competency in Video Games\\\"\\n  category: background\\n  role: \\\"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\\\"\\n  relevance_score: 3\\n\\n- paper_id: lakshminarayanan2017dynamic\\n  title: \\\"Dynamic Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\\n  year: 2017\\n  venue: AAAI\\n  category: method-component\\n  role: \\\"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\\\"\\n  relevance_score: 4\\n\\n- paper_id: biedenkapp2021temporl\\n  title: \\\"TempoRL: Learning When to Act\\\"\\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: DreamerV2\\n# ============================================================\\n\\n- paper_id: hafner2021dreamerv2\\n  title: \\\"Mastering Atari with Discrete World Models\\\"\\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\\n  year: 2021\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Alternative world model architectures\\n# ============================================================\\n\\n- paper_id: micheli2023iris\\n  title: \\\"Transformers are Sample-Efficient World Models\\\"\\n  authors: [Micheli V., Alonso E., Fleuret F.]\\n  year: 2023\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\\\"\\n  relevance_score: 3\\n\\n- paper_id: robine2023twm\\n  title: \\\"Transformer-based World Models Are Happy With 100k Interactions\\\"\\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\\n  year: 2023\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\\\"\\n  relevance_score: 3\\n\\n- paper_id: chen2022transdreamer\\n  title: \\\"TransDreamer: Reinforcement Learning with Transformer World Models\\\"\\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\\n  year: 2022\\n  venue: \\\"arXiv:2202.09481\\\"\\n  category: direct-competitor\\n  role: \\\"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\\n# ============================================================\\n\\n- paper_id: gumbsch2024thick\\n  title: \\\"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\\\"\\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\\n  year: 2024\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\\\"\\n  relevance_score: 5\\n\\n- paper_id: mattes2024hieros\\n  title: \\\"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\\\"\\n  authors: [Mattes P., Schlosser R., Herbrich R.]\\n  year: 2024\\n  venue: ICML\\n  category: direct-competitor\\n  role: \\\"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Seed-dependent instability & value overestimation in MBRL\\n# ============================================================\\n\\n- paper_id: henderson2018deep\\n  title: \\\"Deep Reinforcement Learning that Matters\\\"\\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\\n  year: 2018\\n  venue: AAAI\\n  category: background\\n  role: \\\"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\\\"\\n  relevance_score: 4\\n\\n- paper_id: nikishin2022primacy\\n  title: \\\"The Primacy Bias in Deep Reinforcement Learning\\\"\\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\\n  year: 2022\\n  venue: ICML\\n  category: background\\n  role: \\\"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\\\"\\n  relevance_score: 4\\n\\n- paper_id: qiao2023mind\\n  title: \\\"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\\\"\\n  authors: [Qiao Z., Lyu J., Li X.]\\n  year: 2023\\n  venue: \\\"arXiv:2310.15017 (ECAI 2024)\\\"\\n  category: evaluation\\n  role: \\\"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\\\"\\n  relevance_score: 5\\n\\n- paper_id: hussing2024dissecting\\n  title: \\\"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\\\"\\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\\n  year: 2024\\n  venue: \\\"Reinforcement Learning Journal (RLC 2024)\\\"\\n  category: evaluation\\n  role: \\\"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\\\"\\n  relevance_score: 4\\n\\n- paper_id: barkley2024stealing\\n  title: \\\"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\\\"\\n  authors: [Barkley B., Fridovich-Keil D.]\\n  year: 2024\\n  venue: \\\"arXiv:2412.14312 (ICML 2025)\\\"\\n  category: evaluation\\n  role: \\\"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\\\"\\n  relevance_score: 3\\n\\n- paper_id: bjorck2022variance\\n  title: \\\"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\\\"\\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\\n  year: 2022\\n  venue: ICLR\\n  category: background\\n  role: \\\"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Reward prediction quality → MBRL performance\\n# ============================================================\\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\\n# (0.01 → 0.747), making performance seed-dependent. These papers\\n# establish that reward prediction quality is a known MBRL bottleneck.\\n\\n- paper_id: lee2024dreamsmooth\\n  title: \\\"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\\\"\\n  authors: [Lee V., Abbeel P., Lee Y.]\\n  year: 2024\\n  venue: ICLR\\n  category: background\\n  role: \\\"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\\\"\\n  relevance_score: 5\\n\\n- paper_id: ma2024harmonydream\\n  title: \\\"HarmonyDream: Task Harmonization Inside World Models\\\"\\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\\n  year: 2024\\n  venue: ICML\\n  category: background\\n  role: \\\"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\\\"\\n  relevance_score: 5\\n\\n- paper_id: lambert2020objective\\n  title: \\\"Objective Mismatch in Model-based Reinforcement Learning\\\"\\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\\n  year: 2020\\n  venue: \\\"L4DC (Proceedings of Machine Learning Research, vol. 120)\\\"\\n  category: background\\n  role: \\\"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: Auxiliary tasks & representation coupling in world models\\n# ============================================================\\n# Our finding: reward prediction quality is tightly coupled to temporal\\n# conditioning (dt_embedding). Removing the embedding degrades the\\n# reward head while dynamics remain intact — suggesting the reward head\\n# acts as more than a passive predictor; it conditions the shared\\n# representation. Literature gap: no prior work studies this coupling\\n# specifically in Dreamer-family world models.\\n\\n- paper_id: jaderberg2017unreal\\n  title: \\\"Reinforcement Learning with Unsupervised Auxiliary Tasks\\\"\\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\\n  year: 2017\\n  venue: ICLR\\n  category: background\\n  role: \\\"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\\\"\\n  relevance_score: 4\\n\\n- paper_id: lyle2021auxiliary\\n  title: \\\"On The Effect of Auxiliary Tasks on Representation Dynamics\\\"\\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\\n  year: 2021\\n  venue: AISTATS\\n  category: background\\n  role: \\\"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\\\"\\n  relevance_score: 4\\n\", \"total_chars\": 20790, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "f358cf81-1d15-4a06-8506-cd8289bb80fc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map — event-gated-adaptive-horizon\\\\n# Last updated: 2026-05-14\\\\n# Total: 39 papers (5 existing + 34 new)\\\\n\\\\n# ============================================================\\\\n# EXISTING CITATIONS (already in paper.tex)\\\\n# ============================================================\\\\n\\\\n- paper_id: sutton1999options\\\\n  title: \\\\\\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\\\\\"\\\\n  authors: [Sutton R.S., Precup D., Singh S.]\\\\n  year: 1999\\\\n  venue: \\\\\\\"Artificial Intelligence 112(1-2):181-211\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: hafner2020dreamerv1\\\\n  title: \\\\\\\"Dream to Control: Learning Behaviors by Latent Imagination\\\\\\\"\\\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\\\n  year: 2020\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: hafner2023dreamerv3\\\\n  title: \\\\\\\"Mastering Diverse Domains through World Models\\\\\\\"\\\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"arXiv:2301.04104 (Nature 2025)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: sharma2017figar\\\\n  title: \\\\\\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\\\n  year: 2017\\\\n  venue: \\\\\\\"ICLR Workshop\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: janner2019mbpo\\\\n  title: \\\\\\\"When to Trust Your Model: Model-Based Policy Optimization\\\\\\\"\\\\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\\\\n  year: 2019\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Multi-step prediction error compounding\\\\n# ============================================================\\\\n\\\\n- paper_id: ke2019learning\\\\n  title: \\\\\\\"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\\\\\\\"\\\\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\\\\n  year: 2019\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: asadi2019combating\\\\n  title: \\\\\\\"Combating the Compounding-Error Problem with a Multi-step Model\\\\\\\"\\\\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\\\\n  year: 2019\\\\n  venue: \\\\\\\"arXiv:1905.13320\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: venkatraman2015improving\\\\n  title: \\\\\\\"Improving Multi-Step Prediction of Learned Time Series Models\\\\\\\"\\\\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\\\\n  year: 2015\\\\n  venue: AAAI\\\\n  category: background\\\\n  role: \\\\\\\"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lambert2022investigating\\\\n  title: \\\\\\\"Investigating Compounding Prediction Errors in Learned Dynamics Models\\\\\\\"\\\\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"arXiv:2203.09637\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Model-predictive control with learned dynamics\\\\n# ============================================================\\\\n\\\\n- paper_id: chua2018pets\\\\n  title: \\\\\\\"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\\\\\\\"\\\\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: nagabandi2018neural\\\\n  title: \\\\\\\"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\\\\\\\"\\\\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\\\\n  year: 2018\\\\n  venue: ICRA\\\\n  category: background\\\\n  role: \\\\\\\"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Value overestimation mitigation\\\\n# ============================================================\\\\n\\\\n- paper_id: thrun1993issues\\\\n  title: \\\\\\\"Issues in Using Function Approximation for Reinforcement Learning\\\\\\\"\\\\n  authors: [Thrun S., Schwartz A.]\\\\n  year: 1993\\\\n  venue: \\\\\\\"Connectionist Models Summer School\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: vanhasselt2016double\\\\n  title: \\\\\\\"Deep Reinforcement Learning with Double Q-Learning\\\\\\\"\\\\n  authors: [van Hasselt H., Guez A., Silver D.]\\\\n  year: 2016\\\\n  venue: AAAI\\\\n  category: background\\\\n  role: \\\\\\\"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: fujimoto2018td3\\\\n  title: \\\\\\\"Addressing Function Approximation Error in Actor-Critic Methods\\\\\\\"\\\\n  authors: [Fujimoto S., van Hoof H., Meger D.]\\\\n  year: 2018\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: haarnoja2018sac\\\\n  title: \\\\\\\"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\\\\\\\"\\\\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\\\\n  year: 2018\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lee2021sunrise\\\\n  title: \\\\\\\"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\\\\n  year: 2021\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Delusional bias\\\\n# ============================================================\\\\n\\\\n- paper_id: lu2018nondelusional\\\\n  title: \\\\\\\"Non-delusional Q-learning and Value-Iteration\\\\\\\"\\\\n  authors: [Lu T., Schuurmans D., Boutilier C.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Hierarchical RL with learned models\\\\n# ============================================================\\\\n\\\\n- paper_id: hafner2022director\\\\n  title: \\\\\\\"Deep Hierarchical Planning from Pixels\\\\\\\"\\\\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\\\\n  year: 2022\\\\n  venue: NeurIPS\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: nachum2018hiro\\\\n  title: \\\\\\\"Data-Efficient Hierarchical Reinforcement Learning\\\\\\\"\\\\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Action repeat / frame skip\\\\n# ============================================================\\\\n\\\\n- paper_id: braylan2015frame\\\\n  title: \\\\\\\"Frame Skip Is a Powerful Parameter for Learning to Play Atari\\\\\\\"\\\\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\\\\n  year: 2015\\\\n  venue: \\\\\\\"AAAI Workshop on Learning for General Competency in Video Games\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lakshminarayanan2017dynamic\\\\n  title: \\\\\\\"Dynamic Action Repetition for Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\\\\n  year: 2017\\\\n  venue: AAAI\\\\n  category: method-component\\\\n  role: \\\\\\\"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: biedenkapp2021temporl\\\\n  title: \\\\\\\"TempoRL: Learning When to Act\\\\\\\"\\\\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\\\\n  year: 2021\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: DreamerV2\\\\n# ============================================================\\\\n\\\\n- paper_id: hafner2021dreamerv2\\\\n  title: \\\\\\\"Mastering Atari with Discrete World Models\\\\\\\"\\\\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\\\\n  year: 2021\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Alternative world model architectures\\\\n# ============================================================\\\\n\\\\n- paper_id: micheli2023iris\\\\n  title: \\\\\\\"Transformers are Sample-Efficient World Models\\\\\\\"\\\\n  authors: [Micheli V., Alonso E., Fleuret F.]\\\\n  year: 2023\\\\n  venue: ICLR\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: robine2023twm\\\\n  title: \\\\\\\"Transformer-based World Models Are Happy With 100k Interactions\\\\\\\"\\\\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\\\\n  year: 2023\\\\n  venue: ICLR\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: chen2022transdreamer\\\\n  title: \\\\\\\"TransDreamer: Reinforcement Learning with Transformer World Models\\\\\\\"\\\\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"arXiv:2202.09481\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\\\\n# ============================================================\\\\n\\\\n- paper_id: gumbsch2024thick\\\\n  title: \\\\\\\"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\\\\\\\"\\\\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\\\\n  year: 2024\\\\n  venue: ICLR\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: mattes2024hieros\\\\n  title: \\\\\\\"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\\\\\\\"\\\\n  authors: [Mattes P., Schlosser R., Herbrich R.]\\\\n  year: 2024\\\\n  venue: ICML\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Seed-dependent instability & value overestimation in MBRL\\\\n# ============================================================\\\\n\\\\n- paper_id: henderson2018deep\\\\n  title: \\\\\\\"Deep Reinforcement Learning that Matters\\\\\\\"\\\\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\\\\n  year: 2018\\\\n  venue: AAAI\\\\n  category: background\\\\n  role: \\\\\\\"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: nikishin2022primacy\\\\n  title: \\\\\\\"The Primacy Bias in Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\\\\n  year: 2022\\\\n  venue: ICML\\\\n  category: background\\\\n  role: \\\\\\\"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: qiao2023mind\\\\n  title: \\\\\\\"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\\\\\\\"\\\\n  authors: [Qiao Z., Lyu J., Li X.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"arXiv:2310.15017 (ECAI 2024)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: hussing2024dissecting\\\\n  title: \\\\\\\"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\\\\\\\"\\\\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"Reinforcement Learning Journal (RLC 2024)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: barkley2024stealing\\\\n  title: \\\\\\\"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\\\\\\\"\\\\n  authors: [Barkley B., Fridovich-Keil D.]\\\\n  year: 2024\\\\n  venue: \\\\\\\"arXiv:2412.14312 (ICML 2025)\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: bjorck2022variance\\\\n  title: \\\\\\\"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\\\\\\\"\\\\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\\\\n  year: 2022\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Reward prediction quality → MBRL performance\\\\n# ============================================================\\\\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\\\\n# (0.01 → 0.747), making performance seed-dependent. These papers\\\\n# establish that reward prediction quality is a known MBRL bottleneck.\\\\n\\\\n- paper_id: lee2024dreamsmooth\\\\n  title: \\\\\\\"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\\\\\\\"\\\\n  authors: [Lee V., Abbeel P., Lee Y.]\\\\n  year: 2024\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: ma2024harmonydream\\\\n  title: \\\\\\\"HarmonyDream: Task Harmonization Inside World Models\\\\\\\"\\\\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\\\\n  year: 2024\\\\n  venue: ICML\\\\n  category: background\\\\n  role: \\\\\\\"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: lambert2020objective\\\\n  title: \\\\\\\"Objective Mismatch in Model-based Reinforcement Learning\\\\\\\"\\\\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\\\\n  year: 2020\\\\n  venue: \\\\\\\"L4DC (Proceedings of Machine Learning Research, vol. 120)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: Auxiliary tasks & representation coupling in world models\\\\n# ============================================================\\\\n# Our finding: reward prediction quality is tightly coupled to temporal\\\\n# conditioning (dt_embedding). Removing the embedding degrades the\\\\n# reward head while dynamics remain intact — suggesting the reward head\\\\n# acts as more than a passive predictor; it conditions the shared\\\\n# representation. Literature gap: no prior work studies this coupling\\\\n# specifically in Dreamer-family world models.\\\\n\\\\n- paper_id: jaderberg2017unreal\\\\n  title: \\\\\\\"Reinforcement Learning with Unsupervised Auxiliary Tasks\\\\\\\"\\\\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\\\\n  year: 2017\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: lyle2021auxiliary\\\\n  title: \\\\\\\"On The Effect of Auxiliary Tasks on Representation Dynamics\\\\\\\"\\\\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\\\\n  year: 2021\\\\n  venue: AISTATS\\\\n  category: background\\\\n  role: \\\\\\\"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\", \\\"total_chars\\\": 20790, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\", \"content\": \"# Literature Map — event-gated-adaptive-horizon\\n# Last updated: 2026-05-14\\n# Total: 39 papers (5 existing + 34 new)\\n\\n# ============================================================\\n# EXISTING CITATIONS (already in paper.tex)\\n# ============================================================\\n\\n- paper_id: sutton1999options\\n  title: \\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\"\\n  authors: [Sutton R.S., Precup D., Singh S.]\\n  year: 1999\\n  venue: \\\"Artificial Intelligence 112(1-2):181-211\\\"\\n  category: background\\n  role: \\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2020dreamerv1\\n  title: \\\"Dream to Control: Learning Behaviors by Latent Imagination\\\"\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\n  year: 2020\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2023dreamerv3\\n  title: \\\"Mastering Diverse Domains through World Models\\\"\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\n  year: 2023\\n  venue: \\\"arXiv:2301.04104 (Nature 2025)\\\"\\n  category: background\\n  role: \\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\"\\n  relevance_score: 5\\n\\n- paper_id: sharma2017figar\\n  title: \\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\n  year: 2017\\n  venue: \\\"ICLR Workshop\\\"\\n  category: method-component\\n  role: \\\"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\\\"\\n  relevance_score: 4\\n\\n- paper_id: janner2019mbpo\\n  title: \\\"When to Trust Your Model: Model-Based Policy Optimization\\\"\\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\\n  year: 2019\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Multi-step prediction error compounding\\n# ============================================================\\n\\n- paper_id: ke2019learning\\n  title: \\\"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\\\"\\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\\n  year: 2019\\n  venue: ICLR\\n  category: background\\n  role: \\\"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\\\"\\n  relevance_score: 4\\n\\n- paper_id: asadi2019combating\\n  title: \\\"Combating the Compounding-Error Problem with a Multi-step Model\\\"\\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\\n  year: 2019\\n  venue: \\\"arXiv:1905.13320\\\"\\n  category: background\\n  role: \\\"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\\\"\\n  relevance_score: 4\\n\\n- paper_id: venkatraman2015improving\\n  title: \\\"Improving Multi-Step Prediction of Learned Time Series Models\\\"\\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\\n  year: 2015\\n  venue: AAAI\\n  category: background\\n  role: \\\"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\\\"\\n  relevance_score: 3\\n\\n- paper_id: lambert2022investigating\\n  title: \\\"Investigating Compounding Prediction Errors in Learned Dynamics Models\\\"\\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\\n  year: 2022\\n  venue: \\\"arXiv:2203.09637\\\"\\n  category: background\\n  role: \\\"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Model-predictive control with learned dynamics\\n# ============================================================\\n\\n- paper_id: chua2018pets\\n  title: \\\"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\\\"\\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\\\"\\n  relevance_score: 3\\n\\n- paper_id: nagabandi2018neural\\n  title: \\\"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\\\"\\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\\n  year: 2018\\n  venue: ICRA\\n  category: background\\n  role: \\\"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Value overestimation mitigation\\n# ============================================================\\n\\n- paper_id: thrun1993issues\\n  title: \\\"Issues in Using Function Approximation for Reinforcement Learning\\\"\\n  authors: [Thrun S., Schwartz A.]\\n  year: 1993\\n  venue: \\\"Connectionist Models Summer School\\\"\\n  category: background\\n  role: \\\"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\\\"\\n  relevance_score: 4\\n\\n- paper_id: vanhasselt2016double\\n  title: \\\"Deep Reinforcement Learning with Double Q-Learning\\\"\\n  authors: [van Hasselt H., Guez A., Silver D.]\\n  year: 2016\\n  venue: AAAI\\n  category: background\\n  role: \\\"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\\\"\\n  relevance_score: 4\\n\\n- paper_id: fujimoto2018td3\\n  title: \\\"Addressing Function Approximation Error in Actor-Critic Methods\\\"\\n  authors: [Fujimoto S., van Hoof H., Meger D.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\\\"\\n  relevance_score: 4\\n\\n- paper_id: haarnoja2018sac\\n  title: \\\"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\\\"\\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\\\"\\n  relevance_score: 3\\n\\n- paper_id: lee2021sunrise\\n  title: \\\"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\\\"\\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Delusional bias\\n# ============================================================\\n\\n- paper_id: lu2018nondelusional\\n  title: \\\"Non-delusional Q-learning and Value-Iteration\\\"\\n  authors: [Lu T., Schuurmans D., Boutilier C.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Hierarchical RL with learned models\\n# ============================================================\\n\\n- paper_id: hafner2022director\\n  title: \\\"Deep Hierarchical Planning from Pixels\\\"\\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\\n  year: 2022\\n  venue: NeurIPS\\n  category: direct-competitor\\n  role: \\\"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\\\"\\n  relevance_score: 4\\n\\n- paper_id: nachum2018hiro\\n  title: \\\"Data-Efficient Hierarchical Reinforcement Learning\\\"\\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Action repeat / frame skip\\n# ============================================================\\n\\n- paper_id: braylan2015frame\\n  title: \\\"Frame Skip Is a Powerful Parameter for Learning to Play Atari\\\"\\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\\n  year: 2015\\n  venue: \\\"AAAI Workshop on Learning for General Competency in Video Games\\\"\\n  category: background\\n  role: \\\"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\\\"\\n  relevance_score: 3\\n\\n- paper_id: lakshminarayanan2017dynamic\\n  title: \\\"Dynamic Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\\n  year: 2017\\n  venue: AAAI\\n  category: method-component\\n  role: \\\"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\\\"\\n  relevance_score: 4\\n\\n- paper_id: biedenkapp2021temporl\\n  title: \\\"TempoRL: Learning When to Act\\\"\\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: DreamerV2\\n# ============================================================\\n\\n- paper_id: hafner2021dreamerv2\\n  title: \\\"Mastering Atari with Discrete World Models\\\"\\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\\n  year: 2021\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Alternative world model architectures\\n# ============================================================\\n\\n- paper_id: micheli2023iris\\n  title: \\\"Transformers are Sample-Efficient World Models\\\"\\n  authors: [Micheli V., Alonso E., Fleuret F.]\\n  year: 2023\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\\\"\\n  relevance_score: 3\\n\\n- paper_id: robine2023twm\\n  title: \\\"Transformer-based World Models Are Happy With 100k Interactions\\\"\\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\\n  year: 2023\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\\\"\\n  relevance_score: 3\\n\\n- paper_id: chen2022transdreamer\\n  title: \\\"TransDreamer: Reinforcement Learning with Transformer World Models\\\"\\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\\n  year: 2022\\n  venue: \\\"arXiv:2202.09481\\\"\\n  category: direct-competitor\\n  role: \\\"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\\n# ============================================================\\n\\n- paper_id: gumbsch2024thick\\n  title: \\\"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\\\"\\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\\n  year: 2024\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\\\"\\n  relevance_score: 5\\n\\n- paper_id: mattes2024hieros\\n  title: \\\"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\\\"\\n  authors: [Mattes P., Schlosser R., Herbrich R.]\\n  year: 2024\\n  venue: ICML\\n  category: direct-competitor\\n  role: \\\"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Seed-dependent instability & value overestimation in MBRL\\n# ============================================================\\n\\n- paper_id: henderson2018deep\\n  title: \\\"Deep Reinforcement Learning that Matters\\\"\\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\\n  year: 2018\\n  venue: AAAI\\n  category: background\\n  role: \\\"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\\\"\\n  relevance_score: 4\\n\\n- paper_id: nikishin2022primacy\\n  title: \\\"The Primacy Bias in Deep Reinforcement Learning\\\"\\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\\n  year: 2022\\n  venue: ICML\\n  category: background\\n  role: \\\"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\\\"\\n  relevance_score: 4\\n\\n- paper_id: qiao2023mind\\n  title: \\\"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\\\"\\n  authors: [Qiao Z., Lyu J., Li X.]\\n  year: 2023\\n  venue: \\\"arXiv:2310.15017 (ECAI 2024)\\\"\\n  category: evaluation\\n  role: \\\"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\\\"\\n  relevance_score: 5\\n\\n- paper_id: hussing2024dissecting\\n  title: \\\"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\\\"\\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\\n  year: 2024\\n  venue: \\\"Reinforcement Learning Journal (RLC 2024)\\\"\\n  category: evaluation\\n  role: \\\"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\\\"\\n  relevance_score: 4\\n\\n- paper_id: barkley2024stealing\\n  title: \\\"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\\\"\\n  authors: [Barkley B., Fridovich-Keil D.]\\n  year: 2024\\n  venue: \\\"arXiv:2412.14312 (ICML 2025)\\\"\\n  category: evaluation\\n  role: \\\"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\\\"\\n  relevance_score: 3\\n\\n- paper_id: bjorck2022variance\\n  title: \\\"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\\\"\\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\\n  year: 2022\\n  venue: ICLR\\n  category: background\\n  role: \\\"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Reward prediction quality → MBRL performance\\n# ============================================================\\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\\n# (0.01 → 0.747), making performance seed-dependent. These papers\\n# establish that reward prediction quality is a known MBRL bottleneck.\\n\\n- paper_id: lee2024dreamsmooth\\n  title: \\\"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\\\"\\n  authors: [Lee V., Abbeel P., Lee Y.]\\n  year: 2024\\n  venue: ICLR\\n  category: background\\n  role: \\\"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\\\"\\n  relevance_score: 5\\n\\n- paper_id: ma2024harmonydream\\n  title: \\\"HarmonyDream: Task Harmonization Inside World Models\\\"\\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\\n  year: 2024\\n  venue: ICML\\n  category: background\\n  role: \\\"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\\\"\\n  relevance_score: 5\\n\\n- paper_id: lambert2020objective\\n  title: \\\"Objective Mismatch in Model-based Reinforcement Learning\\\"\\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\\n  year: 2020\\n  venue: \\\"L4DC (Proceedings of Machine Learning Research, vol. 120)\\\"\\n  category: background\\n  role: \\\"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: Auxiliary tasks & representation coupling in world models\\n# ============================================================\\n# Our finding: reward prediction quality is tightly coupled to temporal\\n# conditioning (dt_embedding). Removing the embedding degrades the\\n# reward head while dynamics remain intact — suggesting the reward head\\n# acts as more than a passive predictor; it conditions the shared\\n# representation. Literature gap: no prior work studies this coupling\\n# specifically in Dreamer-family world models.\\n\\n- paper_id: jaderberg2017unreal\\n  title: \\\"Reinforcement Learning with Unsupervised Auxiliary Tasks\\\"\\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\\n  year: 2017\\n  venue: ICLR\\n  category: background\\n  role: \\\"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\\\"\\n  relevance_score: 4\\n\\n- paper_id: lyle2021auxiliary\\n  title: \\\"On The Effect of Auxiliary Tasks on Representation Dynamics\\\"\\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\\n  year: 2021\\n  venue: AISTATS\\n  category: background\\n  role: \\\"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\\\"\\n  relevance_score: 4\\n\", \"total_chars\": 20790, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me summarize the verification results:

**HarmonyDream** (already in literature_map.yaml as `ma2024harmonydream`):
- Confirmed: ICML 2024
- Title: "HarmonyDream: Task Harmonization Inside World Models"
- Authors from search: The GitHub and ICML pages confirm it. The authors listed in the yaml are: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]
- From the search, the paper is from Tsinghua University (thuml). 

The search confirms it's at ICML 2024, and while the yaml lists "Ma H." as the first author, the search results trace back to Mingsheng Long's group at Tsinghua, which aligns with the author list. Status: **VERIFIED - correct**

**"Mind the Model, Not the Agent"** (already in literature_map.yaml as `qiao2023mind`):
- From search: "

Mind the Model, Not the Agent: The Primacy Bias in Model-Based RL" by Zhongjian Qiao, Jiafei Lyu, and Xiu Li
- The yaml authors match, and the venue checks out as ECAI 2024 published in October 2024. Status: **VERIFIED - correct**

Now I'm looking at the new papers to add. Starting with NE-Dreamer: "Next Embedding Prediction Makes World Models Stronger" by George Bredis, Nikita Balagansky, Daniil Gavrilov, and Ruslan Rakhimov on arXiv 2603.02765.

For the venue, I found an OpenReview page and the project is hosted at corl-team.github.io/nedreamer/, which suggests CoRL 2026 as the user indicated, and the March 2026 arXiv date aligns with that timeline.

For DyMoDreamer: "World Modeling with Dynamic Modulation" on arXiv 2509.24804 is confirmed, and it was presented as a poster at NeurIPS 2025.

For VanTA: The full title is "Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning" at ICLR 2025, with authors Tian-Shuo Liu, Xu-Hui Liu, Ruifeng Chen, Lixuan Jin, Pengyuan Wang, Zhilong Zhang, and Yang Yu.

Now I need to find the complete author list for the Agarwal et al. 2021 paper on deep reinforcement learning at the statistical precipice.

Updating the YAML file with the four new papers while keeping the existing entries for ma2024harmonydream and qiao2023mind intact. I should also verify that DyMoDreamer is specifically NeurIPS 2025 and track down the venue and authors for NE-Dreamer.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "4d564c74-6920-464d-8589-bd2fd585d702",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1YAdxQ7WL2aAMvzVZ6aPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12673,
      "cache_read_input_tokens": 24901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12673
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

_source line 24_

搜索结果已返回。需要补充确认 DyMoDreamer 的作者信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "053cfc4e-a2e5-4c35-9e09-fdf98047147e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1YAdxQ7WL2aAMvzVZ6aPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12673,
      "cache_read_input_tokens": 24901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12673
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DWEBkC2JiuoY4DSmR1ZiVY`</summary>

```json
{
  "query": "DyMoDreamer arXiv 2509.24804 authors world modeling dynamic modulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "b743fec0-6f0b-40d6-802b-ca02ea7e0f39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1YAdxQ7WL2aAMvzVZ6aPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12673,
      "cache_read_input_tokens": 24901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12673
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LBWmrnQJnXG6KQdunxDdCb`</summary>

```json
{
  "query": "NE-Dreamer \"Next Embedding Prediction\" CoRL 2026 venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "2c6edf8a-6336-4998-8a44-c986c742a05e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1YAdxQ7WL2aAMvzVZ6aPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12673,
      "cache_read_input_tokens": 24901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12673
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

_source line 27 · 2026-05-14T14:50:38.495Z_

<details><summary>↩ Tool result · `toolu_01DWEBkC2JiuoY4DSmR1ZiVY`</summary>

```text
Web search results for query: "DyMoDreamer arXiv 2509.24804 authors world modeling dynamic modulation"

Links: [{"title":"[2509.24804] DyMoDreamer: World Modeling with Dynamic Modulation","url":"https://arxiv.org/abs/2509.24804"},{"title":"DyMoDreamer: World Modeling with Dynamic Modulation","url":"https://arxiv.org/pdf/2509.24804"},{"title":"DyMoDreamer: World Modeling with Dynamic Modulation | OpenReview","url":"https://openreview.net/forum?id=SYKwGnik3w"},{"title":"NeurIPS Poster DyMoDreamer: World Modeling with Dynamic Modulation","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/117925"},{"title":"MoWM: Mixture-of-World-Models for Embodied Planning via Latent-to-Pixel Feature Modulation","url":"https://arxiv.org/html/2509.21797"},{"title":"[2509.18428] Latent Action Pretraining Through World Modeling","url":"https://arxiv.org/abs/2509.18428"},{"title":"3D and 4D World Modeling: A Survey","url":"https://arxiv.org/html/2509.07996v2"},{"title":"DyMoDreamer: World Modeling with Dynamic Modulation","url":"https://neurips.cc/media/neurips-2025/Slides/117925.pdf"},{"title":"Latent Action Pretraining Through World Modeling","url":"https://arxiv.org/html/2509.18428v1"},{"title":"Diffusion World Model","url":"https://arxiv.org/html/2402.03570v1"}]

Based on the search results, here's the information about DyMoDreamer (arXiv 2509.24804):

## Paper Details

The authors of DyMoDreamer are: Boxuan Zhang, Runqing Wang, Wei Xiao, Weipu Zhang, Jian Sun, Gao Huang, Jie Chen, and Gang Wang.

## Overview

DyMoDreamer is a novel model-based reinforcement learning (MBRL) algorithm that incorporates a dynamic modulation mechanism. It employs differential observations derived from a novel inter-frame differencing mask, explicitly encoding object-level motion cues and temporal dynamics. Dynamic modulation is modeled as stochastic categorical distributions and integrated into a recurrent state-space model (RSSM), enhancing the model's focus on reward-relevant dynamics.

## Key Results

DyMoDreamer sets a new state-of-the-art on the Atari 100k benchmark with a 156.6% mean human-normalized score, establishes a new record of 832 on the DeepMind Visual Control Suite, and gains a 9.5% performance improvement after 1M steps on the Crafter benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "afe880f6-5242-4c3d-9612-9713b512886f",
  "tool_use_result": {
    "query": "DyMoDreamer arXiv 2509.24804 authors world modeling dynamic modulation",
    "results": [
      {
        "tool_use_id": "srvtoolu_015KXvw5NpPGVn84YiraZa2E",
        "content": [
          {
            "title": "[2509.24804] DyMoDreamer: World Modeling with Dynamic Modulation",
            "url": "https://arxiv.org/abs/2509.24804"
          },
          {
            "title": "DyMoDreamer: World Modeling with Dynamic Modulation",
            "url": "https://arxiv.org/pdf/2509.24804"
          },
          {
            "title": "DyMoDreamer: World Modeling with Dynamic Modulation | OpenReview",
            "url": "https://openreview.net/forum?id=SYKwGnik3w"
          },
          {
            "title": "NeurIPS Poster DyMoDreamer: World Modeling with Dynamic Modulation",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/117925"
          },
          {
            "title": "MoWM: Mixture-of-World-Models for Embodied Planning via Latent-to-Pixel Feature Modulation",
            "url": "https://arxiv.org/html/2509.21797"
          },
          {
            "title": "[2509.18428] Latent Action Pretraining Through World Modeling",
            "url": "https://arxiv.org/abs/2509.18428"
          },
          {
            "title": "3D and 4D World Modeling: A Survey",
            "url": "https://arxiv.org/html/2509.07996v2"
          },
          {
            "title": "DyMoDreamer: World Modeling with Dynamic Modulation",
            "url": "https://neurips.cc/media/neurips-2025/Slides/117925.pdf"
          },
          {
            "title": "Latent Action Pretraining Through World Modeling",
            "url": "https://arxiv.org/html/2509.18428v1"
          },
          {
            "title": "Diffusion World Model",
            "url": "https://arxiv.org/html/2402.03570v1"
          }
        ]
      },
      "Based on the search results, here's the information about DyMoDreamer (arXiv 2509.24804):\n\n## Paper Details\n\nThe authors of DyMoDreamer are: Boxuan Zhang, Runqing Wang, Wei Xiao, Weipu Zhang, Jian Sun, Gao Huang, Jie Chen, and Gang Wang.\n\n## Overview\n\nDyMoDreamer is a novel model-based reinforcement learning (MBRL) algorithm that incorporates a dynamic modulation mechanism. It employs differential observations derived from a novel inter-frame differencing mask, explicitly encoding object-level motion cues and temporal dynamics. Dynamic modulation is modeled as stochastic categorical distributions and integrated into a recurrent state-space model (RSSM), enhancing the model's focus on reward-relevant dynamics.\n\n## Key Results\n\nDyMoDreamer sets a new state-of-the-art on the Atari 100k benchmark with a 156.6% mean human-normalized score, establishes a new record of 832 on the DeepMind Visual Control Suite, and gains a 9.5% performance improvement after 1M steps on the Crafter benchmark."
    ],
    "durationSeconds": 6.506654664999995
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T14:50:41.576Z_

<details><summary>↩ Tool result · `toolu_01LBWmrnQJnXG6KQdunxDdCb`</summary>

```text
Web search results for query: "NE-Dreamer "Next Embedding Prediction" CoRL 2026 venue conference"

Links: [{"title":"NE-Dreamer: Next Embedding Prediction Makes World Models Stronger","url":"https://corl-team.github.io/nedreamer/"},{"title":"GitHub - corl-team/nedreamer: Official implementation of the paper \"Next Embedding Prediction Makes World Models Stronger\" · GitHub","url":"https://github.com/corl-team/nedreamer"},{"title":"[2603.02765] Next Embedding Prediction Makes World Models Stronger","url":"https://arxiv.org/abs/2603.02765"},{"title":"Next Embedding Prediction Makes World Models Stronger","url":"https://arxiv.org/html/2603.02765v1"},{"title":"Paper page - Next Embedding Prediction Makes World Models Stronger","url":"https://huggingface.co/papers/2603.02765"},{"title":"(PDF) Next Embedding Prediction Makes World Models Stronger","url":"https://www.researchgate.net/publication/401523861_Next_Embedding_Prediction_Makes_World_Models_Stronger"},{"title":"Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction","url":"https://arxiv.org/html/2603.07083"},{"title":"Next-Embedding Prediction Makes Strong Vision Learners","url":"https://arxiv.org/html/2512.16922v2"},{"title":"Next Embedding Prediction Makes World Models Stronger (Mar 2026) - YouTube","url":"https://www.youtube.com/watch?v=Y32GGvchNng"},{"title":"Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models","url":"https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"}]

Based on the search results, I found information about NE-Dreamer and "Next Embedding Prediction," but I did not find specific information about a CoRL 2026 venue or conference venue in the results. Let me search more specifically for this connection.

Links: [{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"2025 Conference on Robot Learning - CoRL","url":"https://www.corl.org/home"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz","url":"https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"},{"title":"Home | Corlas 2026","url":"https://www.corlas2026.org/"},{"title":"CoRL 2026 — Conference on Robot Learning - Passion PA","url":"https://passionpa.com/event/corl-2026"},{"title":"CoRL 2026 - CoRL History","url":"https://www.corl.org/about-corl/corl-history"}]

## Search Results Summary

Based on my web search, here's what I found:

### NE-Dreamer: Next Embedding Prediction

NE-Dreamer is a decoder-free MBRL agent that leverages a temporal transformer to predict next-step encoder embeddings from latent state sequences, directly optimizing temporal predictive alignment in representation space. On the DeepMind Control Suite, NE-Dreamer matches or exceeds DreamerV3 and leading decoder-free agents, and on a challenging subset of DMLab tasks involving memory and spatial reasoning, NE-Dreamer achieves substantial gains.

The paper was authored by George Bredis, Nikita Balagansky, Daniil Gavrilov, and Ruslan Rakhimov in 2026.

### CoRL 2026 Conference Venue

CoRL 2026 will be held in Austin, Texas, US. More specifically, CoRL 2026 will be held at the JW Marriott Austin in Austin, TX (November 9–12, 2026), with a workshop day on November 9 and the main conference on November 10–12.

The NE-Dreamer paper was posted to arXiv on March 3, 2026, which predates the CoRL 2026 conference scheduled for November 2026. The search results do not indicate whether NE-Dreamer was specifically accepted to or presented at CoRL 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "5c7086df-880c-4223-ba2c-5c2173487071",
  "tool_use_result": {
    "query": "NE-Dreamer \"Next Embedding Prediction\" CoRL 2026 venue conference",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YVMCx39WqkkHJUtzDpPHYC",
        "content": [
          {
            "title": "NE-Dreamer: Next Embedding Prediction Makes World Models Stronger",
            "url": "https://corl-team.github.io/nedreamer/"
          },
          {
            "title": "GitHub - corl-team/nedreamer: Official implementation of the paper \"Next Embedding Prediction Makes World Models Stronger\" · GitHub",
            "url": "https://github.com/corl-team/nedreamer"
          },
          {
            "title": "[2603.02765] Next Embedding Prediction Makes World Models Stronger",
            "url": "https://arxiv.org/abs/2603.02765"
          },
          {
            "title": "Next Embedding Prediction Makes World Models Stronger",
            "url": "https://arxiv.org/html/2603.02765v1"
          },
          {
            "title": "Paper page - Next Embedding Prediction Makes World Models Stronger",
            "url": "https://huggingface.co/papers/2603.02765"
          },
          {
            "title": "(PDF) Next Embedding Prediction Makes World Models Stronger",
            "url": "https://www.researchgate.net/publication/401523861_Next_Embedding_Prediction_Makes_World_Models_Stronger"
          },
          {
            "title": "Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction",
            "url": "https://arxiv.org/html/2603.07083"
          },
          {
            "title": "Next-Embedding Prediction Makes Strong Vision Learners",
            "url": "https://arxiv.org/html/2512.16922v2"
          },
          {
            "title": "Next Embedding Prediction Makes World Models Stronger (Mar 2026) - YouTube",
            "url": "https://www.youtube.com/watch?v=Y32GGvchNng"
          },
          {
            "title": "Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models",
            "url": "https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"
          }
        ]
      },
      "Based on the search results, I found information about NE-Dreamer and \"Next Embedding Prediction,\" but I did not find specific information about a CoRL 2026 venue or conference venue in the results. Let me search more specifically for this connection.",
      {
        "tool_use_id": "srvtoolu_01Q8tcZpc4QUd5ThAHr7oGGZ",
        "content": [
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "2025 Conference on Robot Learning - CoRL",
            "url": "https://www.corl.org/home"
          },
          {
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz",
            "url": "https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"
          },
          {
            "title": "Home | Corlas 2026",
            "url": "https://www.corlas2026.org/"
          },
          {
            "title": "CoRL 2026 — Conference on Robot Learning - Passion PA",
            "url": "https://passionpa.com/event/corl-2026"
          },
          {
            "title": "CoRL 2026 - CoRL History",
            "url": "https://www.corl.org/about-corl/corl-history"
          }
        ]
      },
      "## Search Results Summary\n\nBased on my web search, here's what I found:\n\n### NE-Dreamer: Next Embedding Prediction\n\nNE-Dreamer is a decoder-free MBRL agent that leverages a temporal transformer to predict next-step encoder embeddings from latent state sequences, directly optimizing temporal predictive alignment in representation space. On the DeepMind Control Suite, NE-Dreamer matches or exceeds DreamerV3 and leading decoder-free agents, and on a challenging subset of DMLab tasks involving memory and spatial reasoning, NE-Dreamer achieves substantial gains.\n\nThe paper was authored by George Bredis, Nikita Balagansky, Daniil Gavrilov, and Ruslan Rakhimov in 2026.\n\n### CoRL 2026 Conference Venue\n\nCoRL 2026 will be held in Austin, Texas, US. More specifically, CoRL 2026 will be held at the JW Marriott Austin in Austin, TX (November 9–12, 2026), with a workshop day on November 9 and the main conference on November 10–12.\n\nThe NE-Dreamer paper was posted to arXiv on March 3, 2026, which predates the CoRL 2026 conference scheduled for November 2026. The search results do not indicate whether NE-Dreamer was specifically accepted to or presented at CoRL 2026."
    ],
    "durationSeconds": 9.384219324999998
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me summarize:

**Verification Results:**

1. **HarmonyDream** - VERIFIED CORRECT
   - Already in yaml as `ma2024harmonydream`
   - Title: "HarmonyDream: Task Harmonization Inside World Models"
   - Authors: Ma H. et al. (from Tsinghua/thuml)
   - Venue: ICML 2024 ✓
   - arXiv: 2310.00344

2. **"Mind the Model, Not the Agent"** - VERIFIED CORRECT
   - Already in yaml as `qiao2023mind`
   - Title: "Mind the Model, Not the Agent: The Primacy Bias in Model-based RL"
   - Authors: Qiao Z., Lyu J., Li X. ✓
   - Venue: ECAI 2024 ✓

I've also identified a new paper to add: NE-Dreamer from March 2026 about next embedding prediction strengthening world models, authored by Bredis G. and Bala.

For the second entry, I'm noting that while the GitHub organization suggests a CoRL connection, the paper is currently just an arXiv preprint since CoRL 2026 hasn't occurred yet. I should list it as arXiv:2603.02765 without confirming a venue.

There's also DyMoDreamer from NeurIPS 2025 on dynamic modulation in world modeling, with authors Zhang B., Wang R., Xiao W., Zhang W., Sun J., and Huang.

Then VanTA at ICLR 2025, which uses vision-language model guidance for semantic temporal abstraction in reinforcement learning. And finally, the Agarwal et al. paper from NeurIPS 2021 that won an Outstanding Paper Award, examining deep RL at the statistical precipice.

Now I need to update the YAML file with these four entries. The user mentioned save_project_file, but that's restricted to specific files, so I'll use the Write tool directly instead. The current count is 39 papers, so adding these four brings it to 43. I should also verify the venue information—DyMoDreamer is confirmed as NeurIPS 2025, but NE-Dreamer listed as CoRL 2026 is problematic since that conference hasn't occurred yet. The arXiv date is March 2026, so I'll note it accordingly rather than assume a future venue confirmation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "64f391f8-aef1-4779-9027-982b5a1c047a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ViDeB4szDC2qnBdAo5qUT8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3511,
      "cache_read_input_tokens": 37574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3511
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

_source line 30_

所有搜索完成。现在更新 `literature_map.yaml`。

验证结果：
- **HarmonyDream**: 已在 yaml 中，信息正确（Ma et al., ICML 2024）
- **Qiao et al.**: 已在 yaml 中，信息正确（ECAI 2024）
- **NE-Dreamer**: 确认 arXiv:2603.02765，CoRL 2026 尚未举办（2026年11月），标为 arXiv preprint
- **DyMoDreamer**: 确认 arXiv:2509.24804，实际是 **NeurIPS 2025**（非仅 2025）
- **VanTA**: 确认 ICLR 2025
- **Agarwal et al.**: 确认 NeurIPS 2021 Outstanding Paper Award

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "948b488d-574a-4138-9915-2d354dfdd133",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ViDeB4szDC2qnBdAo5qUT8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3511,
      "cache_read_input_tokens": 37574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3511
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01Su16YJAd4dKaTXVMDopj3m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "8c7ee4d9-b033-4f9d-abfe-11aa80039eaa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ViDeB4szDC2qnBdAo5qUT8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3511,
      "cache_read_input_tokens": 37574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3511
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

_source line 32 · 2026-05-14T14:51:22.920Z_

<details><summary>↩ Tool result · `toolu_01Su16YJAd4dKaTXVMDopj3m`</summary>

```text
1	# Literature Map — event-gated-adaptive-horizon
2	# Last updated: 2026-05-14
3	# Total: 39 papers (5 existing + 34 new)
4	
5	# ============================================================
6	# EXISTING CITATIONS (already in paper.tex)
7	# ============================================================
8	
9	- paper_id: sutton1999options
10	  title: "Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning"
11	  authors: [Sutton R.S., Precup D., Singh S.]
12	  year: 1999
13	  venue: "Artificial Intelligence 112(1-2):181-211"
14	  category: background
15	  role: "Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL"
16	  relevance_score: 5
17	
18	- paper_id: hafner2020dreamerv1
19	  title: "Dream to Control: Learning Behaviors by Latent Imagination"
20	  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]
21	  year: 2020
22	  venue: ICLR
23	  category: background
24	  role: "DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm"
25	  relevance_score: 5
26	
27	- paper_id: hafner2023dreamerv3
28	  title: "Mastering Diverse Domains through World Models"
29	  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]
30	  year: 2023
31	  venue: "arXiv:2301.04104 (Nature 2025)"
32	  category: background
33	  role: "DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here"
34	  relevance_score: 5
35	
36	- paper_id: sharma2017figar
37	  title: "Fine Grained Action Repetition for Deep Reinforcement Learning"
38	  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]
39	  year: 2017
40	  venue: "ICLR Workshop"
41	  category: method-component
42	  role: "FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL"
43	  relevance_score: 4
44	
45	- paper_id: janner2019mbpo
46	  title: "When to Trust Your Model: Model-Based Policy Optimization"
47	  authors: [Janner M., Fu J., Zhang M., Levine S.]
48	  year: 2019
49	  venue: NeurIPS
50	  category: background
51	  role: "MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding"
52	  relevance_score: 5
53	
54	# ============================================================
55	# NEW: Multi-step prediction error compounding
56	# ============================================================
57	
58	- paper_id: ke2019learning
59	  title: "Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future"
60	  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]
61	  year: 2019
62	  venue: ICLR
63	  category: background
64	  role: "Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1"
65	  relevance_score: 4
66	
67	- paper_id: asadi2019combating
68	  title: "Combating the Compounding-Error Problem with a Multi-step Model"
69	  authors: [Asadi K., Misra D., Kim S., Littman M.L.]
70	  year: 2019
71	  venue: "arXiv:1905.13320"
72	  category: background
73	  role: "Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error"
74	  relevance_score: 4
75	
76	- paper_id: venkatraman2015improving
77	  title: "Improving Multi-Step Prediction of Learned Time Series Models"
78	  authors: [Venkatraman A., Hebert M., Bagnell J.A.]
79	  year: 2015
80	  venue: AAAI
81	  category: background
82	  role: "Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error"
83	  relevance_score: 3
84	
85	- paper_id: lambert2022investigating
86	  title: "Investigating Compounding Prediction Errors in Learned Dynamics Models"
87	  authors: [Lambert N., Pister K.S.J., Calandra R.]
88	  year: 2022
89	  venue: "arXiv:2203.09637"
90	  category: background
91	  role: "Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead"
92	  relevance_score: 3
93	
94	# ============================================================
95	# NEW: Model-predictive control with learned dynamics
96	# ============================================================
97	
98	- paper_id: chua2018pets
99	  title: "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models"
100	  authors: [Chua K., Calandra R., McAllister R., Levine S.]
101	  year: 2018
102	  venue: NeurIPS
103	  category: background
104	  role: "PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach"
105	  relevance_score: 3
106	
107	- paper_id: nagabandi2018neural
108	  title: "Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning"
109	  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]
110	  year: 2018
111	  venue: ICRA
112	  category: background
113	  role: "Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures"
114	  relevance_score: 3
115	
116	# ============================================================
117	# NEW: Value overestimation mitigation
118	# ============================================================
119	
120	- paper_id: thrun1993issues
121	  title: "Issues in Using Function Approximation for Reinforcement Learning"
122	  authors: [Thrun S., Schwartz A.]
123	  year: 1993
124	  venue: "Connectionist Models Summer School"
125	  category: background
126	  role: "First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning"
127	  relevance_score: 4
128	
129	- paper_id: vanhasselt2016double
130	  title: "Deep Reinforcement Learning with Double Q-Learning"
131	  authors: [van Hasselt H., Guez A., Silver D.]
132	  year: 2016
133	  venue: AAAI
134	  category: background
135	  role: "Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL"
136	  relevance_score: 4
137	
138	- paper_id: fujimoto2018td3
139	  title: "Addressing Function Approximation Error in Actor-Critic Methods"
140	  authors: [Fujimoto S., van Hoof H., Meger D.]
141	  year: 2018
142	  venue: ICML
143	  category: method-component
144	  role: "TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify"
145	  relevance_score: 4
146	
147	- paper_id: haarnoja2018sac
148	  title: "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor"
149	  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]
150	  year: 2018
151	  venue: ICML
152	  category: method-component
153	  role: "SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values"
154	  relevance_score: 3
155	
156	- paper_id: lee2021sunrise
157	  title: "SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning"
158	  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]
159	  year: 2021
160	  venue: ICML
161	  category: method-component
162	  role: "Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism"
163	  relevance_score: 3
164	
165	# ============================================================
166	# NEW: Delusional bias
167	# ============================================================
168	
169	- paper_id: lu2018nondelusional
170	  title: "Non-delusional Q-learning and Value-Iteration"
171	  authors: [Lu T., Schuurmans D., Boutilier C.]
172	  year: 2018
173	  venue: NeurIPS
174	  category: background
175	  role: "Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision"
176	  relevance_score: 5
177	
178	# ============================================================
179	# NEW: Hierarchical RL with learned models
180	# ============================================================
181	
182	- paper_id: hafner2022director
183	  title: "Deep Hierarchical Planning from Pixels"
184	  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]
185	  year: 2022
186	  venue: NeurIPS
187	  category: direct-competitor
188	  role: "Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt"
189	  relevance_score: 4
190	
191	- paper_id: nachum2018hiro
192	  title: "Data-Efficient Hierarchical Reinforcement Learning"
193	  authors: [Nachum O., Gu S., Lee H., Levine S.]
194	  year: 2018
195	  venue: NeurIPS
196	  category: background
197	  role: "HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed"
198	  relevance_score: 3
199	
200	# ============================================================
201	# NEW: Action repeat / frame skip
202	# ============================================================
203	
204	- paper_id: braylan2015frame
205	  title: "Frame Skip Is a Powerful Parameter for Learning to Play Atari"
206	  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]
207	  year: 2015
208	  venue: "AAAI Workshop on Learning for General Competency in Video Games"
209	  category: background
210	  role: "Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice"
211	  relevance_score: 3
212	
213	- paper_id: lakshminarayanan2017dynamic
214	  title: "Dynamic Action Repetition for Deep Reinforcement Learning"
215	  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]
216	  year: 2017
217	  venue: AAAI
218	  category: method-component
219	  role: "Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach"
220	  relevance_score: 4
221	
222	- paper_id: biedenkapp2021temporl
223	  title: "TempoRL: Learning When to Act"
224	  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]
225	  year: 2021
226	  venue: ICML
227	  category: method-component
228	  role: "Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify"
229	  relevance_score: 4
230	
231	# ============================================================
232	# NEW: DreamerV2
233	# ============================================================
234	
235	- paper_id: hafner2021dreamerv2
236	  title: "Mastering Atari with Discrete World Models"
237	  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]
238	  year: 2021
239	  venue: ICLR
240	  category: background
241	  role: "DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system"
242	  relevance_score: 5
243	
244	# ============================================================
245	# NEW: Alternative world model architectures
246	# ============================================================
247	
248	- paper_id: micheli2023iris
249	  title: "Transformers are Sample-Efficient World Models"
250	  authors: [Micheli V., Alonso E., Fleuret F.]
251	  year: 2023
252	  venue: ICLR
253	  category: direct-competitor
254	  role: "IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction"
255	  relevance_score: 3
256	
257	- paper_id: robine2023twm
258	  title: "Transformer-based World Models Are Happy With 100k Interactions"
259	  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]
260	  year: 2023
261	  venue: ICLR
262	  category: direct-competitor
263	  role: "TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap"
264	  relevance_score: 3
265	
266	- paper_id: chen2022transdreamer
267	  title: "TransDreamer: Reinforcement Learning with Transformer World Models"
268	  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]
269	  year: 2022
270	  venue: "arXiv:2202.09481"
271	  category: direct-competitor
272	  role: "Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures"
273	  relevance_score: 3
274	
275	# ============================================================
276	# NEW: 2024-2026 concurrent work on temporal abstraction in world models
277	# ============================================================
278	
279	- paper_id: gumbsch2024thick
280	  title: "Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics"
281	  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]
282	  year: 2024
283	  venue: ICLR
284	  category: direct-competitor
285	  role: "THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination"
286	  relevance_score: 5
287	
288	- paper_id: mattes2024hieros
289	  title: "Hieros: Hierarchical Imagination on Structured State Space Sequence World Models"
290	  authors: [Mattes P., Schlosser R., Herbrich R.]
291	  year: 2024
292	  venue: ICML
293	  category: direct-competitor
294	  role: "Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify"
295	  relevance_score: 5
296	
297	# ============================================================
298	# NEW: Seed-dependent instability & value overestimation in MBRL
299	# ============================================================
300	
301	- paper_id: henderson2018deep
302	  title: "Deep Reinforcement Learning that Matters"
303	  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]
304	  year: 2018
305	  venue: AAAI
306	  category: background
307	  role: "Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config"
308	  relevance_score: 4
309	
310	- paper_id: nikishin2022primacy
311	  title: "The Primacy Bias in Deep Reinforcement Learning"
312	  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]
313	  year: 2022
314	  venue: ICML
315	  category: background
316	  role: "Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent"
317	  relevance_score: 4
318	
319	- paper_id: qiao2023mind
320	  title: "Mind the Model, Not the Agent: The Primacy Bias in Model-based RL"
321	  authors: [Qiao Z., Lyu J., Li X.]
322	  year: 2023
323	  venue: "arXiv:2310.15017 (ECAI 2024)"
324	  category: evaluation
325	  role: "Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't"
326	  relevance_score: 5
327	
328	- paper_id: hussing2024dissecting
329	  title: "Dissecting Deep RL with High Update Ratios: Combatting Value Divergence"
330	  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]
331	  year: 2024
332	  venue: "Reinforcement Learning Journal (RLC 2024)"
333	  category: evaluation
334	  role: "Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization"
335	  relevance_score: 4
336	
337	- paper_id: barkley2024stealing
338	  title: "Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning"
339	  authors: [Barkley B., Fridovich-Keil D.]
340	  year: 2024
341	  venue: "arXiv:2412.14312 (ICML 2025)"
342	  category: evaluation
343	  role: "Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix"
344	  relevance_score: 3
345	
346	- paper_id: bjorck2022variance
347	  title: "Is High Variance Unavoidable in RL? A Case Study in Continuous Control"
348	  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]
349	  year: 2022
350	  venue: ICLR
351	  category: background
352	  role: "Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability"
353	  relevance_score: 3
354	
355	# ============================================================
356	# NEW: Reward prediction quality → MBRL performance
357	# ============================================================
358	# Our key finding: removing dt_embedding causes reward_MAE to spike 75x
359	# (0.01 → 0.747), making performance seed-dependent. These papers
360	# establish that reward prediction quality is a known MBRL bottleneck.
361	
362	- paper_id: lee2024dreamsmooth
363	  title: "DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing"
364	  authors: [Lee V., Abbeel P., Lee Y.]
365	  year: 2024
366	  venue: ICLR
367	  category: background
368	  role: "Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x"
369	  relevance_score: 5
370	
371	- paper_id: ma2024harmonydream
372	  title: "HarmonyDream: Task Harmonization Inside World Models"
373	  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]
374	  year: 2024
375	  venue: ICML
376	  category: background
377	  role: "Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion"
378	  relevance_score: 5
379	
380	- paper_id: lambert2020objective
381	  title: "Objective Mismatch in Model-based Reinforcement Learning"
382	  authors: [Lambert N., Amos B., Yadan O., Calandra R.]
383	  year: 2020
384	  venue: "L4DC (Proceedings of Machine Learning Research, vol. 120)"
385	  category: background
386	  role: "Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch"
387	  relevance_score: 4
388	
389	# ============================================================
390	# NEW: Auxiliary tasks & representation coupling in world models
391	# ============================================================
392	# Our finding: reward prediction quality is tightly coupled to temporal
393	# conditioning (dt_embedding). Removing the embedding degrades the
394	# reward head while dynamics remain intact — suggesting the reward head
395	# acts as more than a passive predictor; it conditions the shared
396	# representation. Literature gap: no prior work studies this coupling
397	# specifically in Dreamer-family world models.
398	
399	- paper_id: jaderberg2017unreal
400	  title: "Reinforcement Learning with Unsupervised Auxiliary Tasks"
401	  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]
402	  year: 2017
403	  venue: ICLR
404	  category: background
405	  role: "UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction"
406	  relevance_score: 4
407	
408	- paper_id: lyle2021auxiliary
409	  title: "On The Effect of Auxiliary Tasks on Representation Dynamics"
410	  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]
411	  year: 2021
412	  venue: AISTATS
413	  category: background
414	  role: "Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space"
415	  relevance_score: 4
416	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "4fed5df0-e631-4622-b59f-acb7410e5dec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
      "content": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 39 papers (5 existing + 34 new)\n\n# ============================================================\n# EXISTING CITATIONS (already in paper.tex)\n# ============================================================\n\n- paper_id: sutton1999options\n  title: \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\"\n  authors: [Sutton R.S., Precup D., Singh S.]\n  year: 1999\n  venue: \"Artificial Intelligence 112(1-2):181-211\"\n  category: background\n  role: \"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\"\n  relevance_score: 5\n\n- paper_id: hafner2020dreamerv1\n  title: \"Dream to Control: Learning Behaviors by Latent Imagination\"\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\n  year: 2020\n  venue: ICLR\n  category: background\n  role: \"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\"\n  relevance_score: 5\n\n- paper_id: hafner2023dreamerv3\n  title: \"Mastering Diverse Domains through World Models\"\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\n  year: 2023\n  venue: \"arXiv:2301.04104 (Nature 2025)\"\n  category: background\n  role: \"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\"\n  relevance_score: 5\n\n- paper_id: sharma2017figar\n  title: \"Fine Grained Action Repetition for Deep Reinforcement Learning\"\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\n  year: 2017\n  venue: \"ICLR Workshop\"\n  category: method-component\n  role: \"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\"\n  relevance_score: 4\n\n- paper_id: janner2019mbpo\n  title: \"When to Trust Your Model: Model-Based Policy Optimization\"\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\n  year: 2019\n  venue: NeurIPS\n  category: background\n  role: \"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Multi-step prediction error compounding\n# ============================================================\n\n- paper_id: ke2019learning\n  title: \"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\"\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\n  year: 2019\n  venue: ICLR\n  category: background\n  role: \"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\"\n  relevance_score: 4\n\n- paper_id: asadi2019combating\n  title: \"Combating the Compounding-Error Problem with a Multi-step Model\"\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\n  year: 2019\n  venue: \"arXiv:1905.13320\"\n  category: background\n  role: \"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\"\n  relevance_score: 4\n\n- paper_id: venkatraman2015improving\n  title: \"Improving Multi-Step Prediction of Learned Time Series Models\"\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\n  year: 2015\n  venue: AAAI\n  category: background\n  role: \"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\"\n  relevance_score: 3\n\n- paper_id: lambert2022investigating\n  title: \"Investigating Compounding Prediction Errors in Learned Dynamics Models\"\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\n  year: 2022\n  venue: \"arXiv:2203.09637\"\n  category: background\n  role: \"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Model-predictive control with learned dynamics\n# ============================================================\n\n- paper_id: chua2018pets\n  title: \"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\"\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\"\n  relevance_score: 3\n\n- paper_id: nagabandi2018neural\n  title: \"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\"\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\n  year: 2018\n  venue: ICRA\n  category: background\n  role: \"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Value overestimation mitigation\n# ============================================================\n\n- paper_id: thrun1993issues\n  title: \"Issues in Using Function Approximation for Reinforcement Learning\"\n  authors: [Thrun S., Schwartz A.]\n  year: 1993\n  venue: \"Connectionist Models Summer School\"\n  category: background\n  role: \"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\"\n  relevance_score: 4\n\n- paper_id: vanhasselt2016double\n  title: \"Deep Reinforcement Learning with Double Q-Learning\"\n  authors: [van Hasselt H., Guez A., Silver D.]\n  year: 2016\n  venue: AAAI\n  category: background\n  role: \"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\"\n  relevance_score: 4\n\n- paper_id: fujimoto2018td3\n  title: \"Addressing Function Approximation Error in Actor-Critic Methods\"\n  authors: [Fujimoto S., van Hoof H., Meger D.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\"\n  relevance_score: 4\n\n- paper_id: haarnoja2018sac\n  title: \"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\"\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\"\n  relevance_score: 3\n\n- paper_id: lee2021sunrise\n  title: \"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\"\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Delusional bias\n# ============================================================\n\n- paper_id: lu2018nondelusional\n  title: \"Non-delusional Q-learning and Value-Iteration\"\n  authors: [Lu T., Schuurmans D., Boutilier C.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Hierarchical RL with learned models\n# ============================================================\n\n- paper_id: hafner2022director\n  title: \"Deep Hierarchical Planning from Pixels\"\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\n  year: 2022\n  venue: NeurIPS\n  category: direct-competitor\n  role: \"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\"\n  relevance_score: 4\n\n- paper_id: nachum2018hiro\n  title: \"Data-Efficient Hierarchical Reinforcement Learning\"\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Action repeat / frame skip\n# ============================================================\n\n- paper_id: braylan2015frame\n  title: \"Frame Skip Is a Powerful Parameter for Learning to Play Atari\"\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\n  year: 2015\n  venue: \"AAAI Workshop on Learning for General Competency in Video Games\"\n  category: background\n  role: \"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\"\n  relevance_score: 3\n\n- paper_id: lakshminarayanan2017dynamic\n  title: \"Dynamic Action Repetition for Deep Reinforcement Learning\"\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\n  year: 2017\n  venue: AAAI\n  category: method-component\n  role: \"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\"\n  relevance_score: 4\n\n- paper_id: biedenkapp2021temporl\n  title: \"TempoRL: Learning When to Act\"\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV2\n# ============================================================\n\n- paper_id: hafner2021dreamerv2\n  title: \"Mastering Atari with Discrete World Models\"\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\n  year: 2021\n  venue: ICLR\n  category: background\n  role: \"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Alternative world model architectures\n# ============================================================\n\n- paper_id: micheli2023iris\n  title: \"Transformers are Sample-Efficient World Models\"\n  authors: [Micheli V., Alonso E., Fleuret F.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\"\n  relevance_score: 3\n\n- paper_id: robine2023twm\n  title: \"Transformer-based World Models Are Happy With 100k Interactions\"\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\"\n  relevance_score: 3\n\n- paper_id: chen2022transdreamer\n  title: \"TransDreamer: Reinforcement Learning with Transformer World Models\"\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\n  year: 2022\n  venue: \"arXiv:2202.09481\"\n  category: direct-competitor\n  role: \"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\n# ============================================================\n\n- paper_id: gumbsch2024thick\n  title: \"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\"\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\n  year: 2024\n  venue: ICLR\n  category: direct-competitor\n  role: \"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\"\n  relevance_score: 5\n\n- paper_id: mattes2024hieros\n  title: \"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\"\n  authors: [Mattes P., Schlosser R., Herbrich R.]\n  year: 2024\n  venue: ICML\n  category: direct-competitor\n  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Seed-dependent instability & value overestimation in MBRL\n# ============================================================\n\n- paper_id: henderson2018deep\n  title: \"Deep Reinforcement Learning that Matters\"\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\n  year: 2018\n  venue: AAAI\n  category: background\n  role: \"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\"\n  relevance_score: 4\n\n- paper_id: nikishin2022primacy\n  title: \"The Primacy Bias in Deep Reinforcement Learning\"\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\n  year: 2022\n  venue: ICML\n  category: background\n  role: \"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\"\n  relevance_score: 4\n\n- paper_id: qiao2023mind\n  title: \"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\"\n  authors: [Qiao Z., Lyu J., Li X.]\n  year: 2023\n  venue: \"arXiv:2310.15017 (ECAI 2024)\"\n  category: evaluation\n  role: \"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\"\n  relevance_score: 5\n\n- paper_id: hussing2024dissecting\n  title: \"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\"\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\n  year: 2024\n  venue: \"Reinforcement Learning Journal (RLC 2024)\"\n  category: evaluation\n  role: \"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\"\n  relevance_score: 4\n\n- paper_id: barkley2024stealing\n  title: \"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\"\n  authors: [Barkley B., Fridovich-Keil D.]\n  year: 2024\n  venue: \"arXiv:2412.14312 (ICML 2025)\"\n  category: evaluation\n  role: \"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\"\n  relevance_score: 3\n\n- paper_id: bjorck2022variance\n  title: \"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\"\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\n  year: 2022\n  venue: ICLR\n  category: background\n  role: \"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Reward prediction quality → MBRL performance\n# ============================================================\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\n# (0.01 → 0.747), making performance seed-dependent. These papers\n# establish that reward prediction quality is a known MBRL bottleneck.\n\n- paper_id: lee2024dreamsmooth\n  title: \"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\"\n  authors: [Lee V., Abbeel P., Lee Y.]\n  year: 2024\n  venue: ICLR\n  category: background\n  role: \"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\"\n  relevance_score: 5\n\n- paper_id: ma2024harmonydream\n  title: \"HarmonyDream: Task Harmonization Inside World Models\"\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\n  year: 2024\n  venue: ICML\n  category: background\n  role: \"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\"\n  relevance_score: 5\n\n- paper_id: lambert2020objective\n  title: \"Objective Mismatch in Model-based Reinforcement Learning\"\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\n  year: 2020\n  venue: \"L4DC (Proceedings of Machine Learning Research, vol. 120)\"\n  category: background\n  role: \"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: Auxiliary tasks & representation coupling in world models\n# ============================================================\n# Our finding: reward prediction quality is tightly coupled to temporal\n# conditioning (dt_embedding). Removing the embedding degrades the\n# reward head while dynamics remain intact — suggesting the reward head\n# acts as more than a passive predictor; it conditions the shared\n# representation. Literature gap: no prior work studies this coupling\n# specifically in Dreamer-family world models.\n\n- paper_id: jaderberg2017unreal\n  title: \"Reinforcement Learning with Unsupervised Auxiliary Tasks\"\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\n  year: 2017\n  venue: ICLR\n  category: background\n  role: \"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\"\n  relevance_score: 4\n\n- paper_id: lyle2021auxiliary\n  title: \"On The Effect of Auxiliary Tasks on Representation Dynamics\"\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\n  year: 2021\n  venue: AISTATS\n  category: background\n  role: \"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\"\n  relevance_score: 4\n",
      "numLines": 416,
      "startLine": 1,
      "totalLines": 416
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01TwsZj1nD4utgzoZsLrw1LG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
  "old_string": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 39 papers (5 existing + 34 new)",
  "new_string": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 43 papers (5 existing + 38 new)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "6f7c4672-1aa1-4125-adc5-0c2e9507c8aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GUEDgfrypmhWAi3yfkbLsu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8149,
      "cache_read_input_tokens": 41085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8149
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

_source line 34 · 2026-05-14T14:51:29.338Z_

<details><summary>↩ Tool result · `toolu_01TwsZj1nD4utgzoZsLrw1LG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "cb19a893-795e-4fcd-bc25-efed40677cca",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
    "oldString": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 39 papers (5 existing + 34 new)",
    "newString": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 43 papers (5 existing + 38 new)",
    "originalFile": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 39 papers (5 existing + 34 new)\n\n# ============================================================\n# EXISTING CITATIONS (already in paper.tex)\n# ============================================================\n\n- paper_id: sutton1999options\n  title: \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\"\n  authors: [Sutton R.S., Precup D., Singh S.]\n  year: 1999\n  venue: \"Artificial Intelligence 112(1-2):181-211\"\n  category: background\n  role: \"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\"\n  relevance_score: 5\n\n- paper_id: hafner2020dreamerv1\n  title: \"Dream to Control: Learning Behaviors by Latent Imagination\"\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\n  year: 2020\n  venue: ICLR\n  category: background\n  role: \"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\"\n  relevance_score: 5\n\n- paper_id: hafner2023dreamerv3\n  title: \"Mastering Diverse Domains through World Models\"\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\n  year: 2023\n  venue: \"arXiv:2301.04104 (Nature 2025)\"\n  category: background\n  role: \"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\"\n  relevance_score: 5\n\n- paper_id: sharma2017figar\n  title: \"Fine Grained Action Repetition for Deep Reinforcement Learning\"\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\n  year: 2017\n  venue: \"ICLR Workshop\"\n  category: method-component\n  role: \"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\"\n  relevance_score: 4\n\n- paper_id: janner2019mbpo\n  title: \"When to Trust Your Model: Model-Based Policy Optimization\"\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\n  year: 2019\n  venue: NeurIPS\n  category: background\n  role: \"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Multi-step prediction error compounding\n# ============================================================\n\n- paper_id: ke2019learning\n  title: \"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\"\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\n  year: 2019\n  venue: ICLR\n  category: background\n  role: \"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\"\n  relevance_score: 4\n\n- paper_id: asadi2019combating\n  title: \"Combating the Compounding-Error Problem with a Multi-step Model\"\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\n  year: 2019\n  venue: \"arXiv:1905.13320\"\n  category: background\n  role: \"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\"\n  relevance_score: 4\n\n- paper_id: venkatraman2015improving\n  title: \"Improving Multi-Step Prediction of Learned Time Series Models\"\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\n  year: 2015\n  venue: AAAI\n  category: background\n  role: \"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\"\n  relevance_score: 3\n\n- paper_id: lambert2022investigating\n  title: \"Investigating Compounding Prediction Errors in Learned Dynamics Models\"\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\n  year: 2022\n  venue: \"arXiv:2203.09637\"\n  category: background\n  role: \"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Model-predictive control with learned dynamics\n# ============================================================\n\n- paper_id: chua2018pets\n  title: \"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\"\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\"\n  relevance_score: 3\n\n- paper_id: nagabandi2018neural\n  title: \"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\"\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\n  year: 2018\n  venue: ICRA\n  category: background\n  role: \"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Value overestimation mitigation\n# ============================================================\n\n- paper_id: thrun1993issues\n  title: \"Issues in Using Function Approximation for Reinforcement Learning\"\n  authors: [Thrun S., Schwartz A.]\n  year: 1993\n  venue: \"Connectionist Models Summer School\"\n  category: background\n  role: \"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\"\n  relevance_score: 4\n\n- paper_id: vanhasselt2016double\n  title: \"Deep Reinforcement Learning with Double Q-Learning\"\n  authors: [van Hasselt H., Guez A., Silver D.]\n  year: 2016\n  venue: AAAI\n  category: background\n  role: \"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\"\n  relevance_score: 4\n\n- paper_id: fujimoto2018td3\n  title: \"Addressing Function Approximation Error in Actor-Critic Methods\"\n  authors: [Fujimoto S., van Hoof H., Meger D.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\"\n  relevance_score: 4\n\n- paper_id: haarnoja2018sac\n  title: \"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\"\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\"\n  relevance_score: 3\n\n- paper_id: lee2021sunrise\n  title: \"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\"\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Delusional bias\n# ============================================================\n\n- paper_id: lu2018nondelusional\n  title: \"Non-delusional Q-learning and Value-Iteration\"\n  authors: [Lu T., Schuurmans D., Boutilier C.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Hierarchical RL with learned models\n# ============================================================\n\n- paper_id: hafner2022director\n  title: \"Deep Hierarchical Planning from Pixels\"\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\n  year: 2022\n  venue: NeurIPS\n  category: direct-competitor\n  role: \"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\"\n  relevance_score: 4\n\n- paper_id: nachum2018hiro\n  title: \"Data-Efficient Hierarchical Reinforcement Learning\"\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Action repeat / frame skip\n# ============================================================\n\n- paper_id: braylan2015frame\n  title: \"Frame Skip Is a Powerful Parameter for Learning to Play Atari\"\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\n  year: 2015\n  venue: \"AAAI Workshop on Learning for General Competency in Video Games\"\n  category: background\n  role: \"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\"\n  relevance_score: 3\n\n- paper_id: lakshminarayanan2017dynamic\n  title: \"Dynamic Action Repetition for Deep Reinforcement Learning\"\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\n  year: 2017\n  venue: AAAI\n  category: method-component\n  role: \"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\"\n  relevance_score: 4\n\n- paper_id: biedenkapp2021temporl\n  title: \"TempoRL: Learning When to Act\"\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV2\n# ============================================================\n\n- paper_id: hafner2021dreamerv2\n  title: \"Mastering Atari with Discrete World Models\"\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\n  year: 2021\n  venue: ICLR\n  category: background\n  role: \"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Alternative world model architectures\n# ============================================================\n\n- paper_id: micheli2023iris\n  title: \"Transformers are Sample-Efficient World Models\"\n  authors: [Micheli V., Alonso E., Fleuret F.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\"\n  relevance_score: 3\n\n- paper_id: robine2023twm\n  title: \"Transformer-based World Models Are Happy With 100k Interactions\"\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\"\n  relevance_score: 3\n\n- paper_id: chen2022transdreamer\n  title: \"TransDreamer: Reinforcement Learning with Transformer World Models\"\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\n  year: 2022\n  venue: \"arXiv:2202.09481\"\n  category: direct-competitor\n  role: \"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\n# ============================================================\n\n- paper_id: gumbsch2024thick\n  title: \"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\"\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\n  year: 2024\n  venue: ICLR\n  category: direct-competitor\n  role: \"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\"\n  relevance_score: 5\n\n- paper_id: mattes2024hieros\n  title: \"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\"\n  authors: [Mattes P., Schlosser R., Herbrich R.]\n  year: 2024\n  venue: ICML\n  category: direct-competitor\n  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Seed-dependent instability & value overestimation in MBRL\n# ============================================================\n\n- paper_id: henderson2018deep\n  title: \"Deep Reinforcement Learning that Matters\"\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\n  year: 2018\n  venue: AAAI\n  category: background\n  role: \"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\"\n  relevance_score: 4\n\n- paper_id: nikishin2022primacy\n  title: \"The Primacy Bias in Deep Reinforcement Learning\"\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\n  year: 2022\n  venue: ICML\n  category: background\n  role: \"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\"\n  relevance_score: 4\n\n- paper_id: qiao2023mind\n  title: \"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\"\n  authors: [Qiao Z., Lyu J., Li X.]\n  year: 2023\n  venue: \"arXiv:2310.15017 (ECAI 2024)\"\n  category: evaluation\n  role: \"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\"\n  relevance_score: 5\n\n- paper_id: hussing2024dissecting\n  title: \"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\"\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\n  year: 2024\n  venue: \"Reinforcement Learning Journal (RLC 2024)\"\n  category: evaluation\n  role: \"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\"\n  relevance_score: 4\n\n- paper_id: barkley2024stealing\n  title: \"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\"\n  authors: [Barkley B., Fridovich-Keil D.]\n  year: 2024\n  venue: \"arXiv:2412.14312 (ICML 2025)\"\n  category: evaluation\n  role: \"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\"\n  relevance_score: 3\n\n- paper_id: bjorck2022variance\n  title: \"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\"\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\n  year: 2022\n  venue: ICLR\n  category: background\n  role: \"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Reward prediction quality → MBRL performance\n# ============================================================\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\n# (0.01 → 0.747), making performance seed-dependent. These papers\n# establish that reward prediction quality is a known MBRL bottleneck.\n\n- paper_id: lee2024dreamsmooth\n  title: \"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\"\n  authors: [Lee V., Abbeel P., Lee Y.]\n  year: 2024\n  venue: ICLR\n  category: background\n  role: \"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\"\n  relevance_score: 5\n\n- paper_id: ma2024harmonydream\n  title: \"HarmonyDream: Task Harmonization Inside World Models\"\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\n  year: 2024\n  venue: ICML\n  category: background\n  role: \"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\"\n  relevance_score: 5\n\n- paper_id: lambert2020objective\n  title: \"Objective Mismatch in Model-based Reinforcement Learning\"\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\n  year: 2020\n  venue: \"L4DC (Proceedings of Machine Learning Research, vol. 120)\"\n  category: background\n  role: \"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: Auxiliary tasks & representation coupling in world models\n# ============================================================\n# Our finding: reward prediction quality is tightly coupled to temporal\n# conditioning (dt_embedding). Removing the embedding degrades the\n# reward head while dynamics remain intact — suggesting the reward head\n# acts as more than a passive predictor; it conditions the shared\n# representation. Literature gap: no prior work studies this coupling\n# specifically in Dreamer-family world models.\n\n- paper_id: jaderberg2017unreal\n  title: \"Reinforcement Learning with Unsupervised Auxiliary Tasks\"\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\n  year: 2017\n  venue: ICLR\n  category: background\n  role: \"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\"\n  relevance_score: 4\n\n- paper_id: lyle2021auxiliary\n  title: \"On The Effect of Auxiliary Tasks on Representation Dynamics\"\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\n  year: 2021\n  venue: AISTATS\n  category: background\n  role: \"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\"\n  relevance_score: 4\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " # Literature Map — event-gated-adaptive-horizon",
          " # Last updated: 2026-05-14",
          "-# Total: 39 papers (5 existing + 34 new)",
          "+# Total: 43 papers (5 existing + 38 new)",
          " ",
          " # ============================================================",
          " # EXISTING CITATIONS (already in paper.tex)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_01SM3GccqD5GYceX3oDpBEhK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
  "old_string": "- paper_id: lyle2021auxiliary\n  title: \"On The Effect of Auxiliary Tasks on Representation Dynamics\"\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\n  year: 2021\n  venue: AISTATS\n  category: background\n  role: \"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\"\n  relevance_score: 4",
  "new_string": "- paper_id: lyle2021auxiliary\n  title: \"On The Effect of Auxiliary Tasks on Representation Dynamics\"\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\n  year: 2021\n  venue: AISTATS\n  category: background\n  role: \"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV3 architecture improvements (2025-2026)\n# ============================================================\n\n- paper_id: bredis2026nedreamer\n  title: \"Next Embedding Prediction Makes World Models Stronger\"\n  authors: [Bredis G., Balagansky N., Gavrilov D., Rakhimov R.]\n  year: 2026\n  venue: \"arXiv:2603.02765\"\n  category: direct-competitor\n  role: \"NE-Dreamer — decoder-free MBRL replacing pixel reconstruction with next-embedding prediction via temporal transformer + Barlow Twins; improves RSSM prediction quality on DMC and DMLab but does not address temporal abstraction or delusional critic — orthogonal to our dt-embedding diagnosis\"\n  relevance_score: 3\n\n- paper_id: zhang2025dymodreamer\n  title: \"DyMoDreamer: World Modeling with Dynamic Modulation\"\n  authors: [Zhang B., Wang R., Xiao W., Zhang W., Sun J., Huang G., Chen J., Wang G.]\n  year: 2025\n  venue: NeurIPS\n  category: direct-competitor\n  role: \"Modulates RSSM via inter-frame differencing mask and stochastic categorical dynamic modulation; SOTA on Atari 100k (156.6% HNS) and DMC (832) — improves dynamics extraction but does not address variable-rate imagination or dt_embedding-induced value overestimation\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Temporal abstraction methods\n# ============================================================\n\n- paper_id: liu2025vanta\n  title: \"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning\"\n  authors: [Liu T.-S., Liu X.-H., Chen R., Jin L., Wang P., Zhang Z., Yu Y.]\n  year: 2025\n  venue: ICLR\n  category: method-component\n  role: \"VanTA — VLM-guided trajectory decomposition into semantically meaningful skills via vector quantization + relabeling; operates at high-level skill abstraction (Franka Kitchen, Crafter) — contrasts with our low-level dt-based temporal abstraction within world-model imagination steps\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Evaluation methodology\n# ============================================================\n\n- paper_id: agarwal2021precipice\n  title: \"Deep Reinforcement Learning at the Edge of the Statistical Precipice\"\n  authors: [Agarwal R., Schwarzer M., Castro P.S., Courville A.C., Bellemare M.]\n  year: 2021\n  venue: NeurIPS\n  category: evaluation\n  role: \"Proposes rliable — interval estimates, performance profiles, IQM for robust multi-seed RL evaluation (NeurIPS Outstanding Paper); our multi-seed experiment design follows this methodology to ensure statistical validity of collapse detection across seeds\"\n  relevance_score: 4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "a5879420-6861-4467-b9ad-233ac473bc18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6J9PGMTjsPYSmC2BUtnfn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 49234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
      },
      "output_tokens": 72,
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

_source line 36 · 2026-05-14T14:51:54.550Z_

<details><summary>↩ Tool result · `toolu_01SM3GccqD5GYceX3oDpBEhK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "e172044b-3f52-44e1-a7b2-e5a2b9ed7982",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
    "oldString": "- paper_id: lyle2021auxiliary\n  title: \"On The Effect of Auxiliary Tasks on Representation Dynamics\"\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\n  year: 2021\n  venue: AISTATS\n  category: background\n  role: \"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\"\n  relevance_score: 4",
    "newString": "- paper_id: lyle2021auxiliary\n  title: \"On The Effect of Auxiliary Tasks on Representation Dynamics\"\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\n  year: 2021\n  venue: AISTATS\n  category: background\n  role: \"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV3 architecture improvements (2025-2026)\n# ============================================================\n\n- paper_id: bredis2026nedreamer\n  title: \"Next Embedding Prediction Makes World Models Stronger\"\n  authors: [Bredis G., Balagansky N., Gavrilov D., Rakhimov R.]\n  year: 2026\n  venue: \"arXiv:2603.02765\"\n  category: direct-competitor\n  role: \"NE-Dreamer — decoder-free MBRL replacing pixel reconstruction with next-embedding prediction via temporal transformer + Barlow Twins; improves RSSM prediction quality on DMC and DMLab but does not address temporal abstraction or delusional critic — orthogonal to our dt-embedding diagnosis\"\n  relevance_score: 3\n\n- paper_id: zhang2025dymodreamer\n  title: \"DyMoDreamer: World Modeling with Dynamic Modulation\"\n  authors: [Zhang B., Wang R., Xiao W., Zhang W., Sun J., Huang G., Chen J., Wang G.]\n  year: 2025\n  venue: NeurIPS\n  category: direct-competitor\n  role: \"Modulates RSSM via inter-frame differencing mask and stochastic categorical dynamic modulation; SOTA on Atari 100k (156.6% HNS) and DMC (832) — improves dynamics extraction but does not address variable-rate imagination or dt_embedding-induced value overestimation\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Temporal abstraction methods\n# ============================================================\n\n- paper_id: liu2025vanta\n  title: \"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning\"\n  authors: [Liu T.-S., Liu X.-H., Chen R., Jin L., Wang P., Zhang Z., Yu Y.]\n  year: 2025\n  venue: ICLR\n  category: method-component\n  role: \"VanTA — VLM-guided trajectory decomposition into semantically meaningful skills via vector quantization + relabeling; operates at high-level skill abstraction (Franka Kitchen, Crafter) — contrasts with our low-level dt-based temporal abstraction within world-model imagination steps\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Evaluation methodology\n# ============================================================\n\n- paper_id: agarwal2021precipice\n  title: \"Deep Reinforcement Learning at the Edge of the Statistical Precipice\"\n  authors: [Agarwal R., Schwarzer M., Castro P.S., Courville A.C., Bellemare M.]\n  year: 2021\n  venue: NeurIPS\n  category: evaluation\n  role: \"Proposes rliable — interval estimates, performance profiles, IQM for robust multi-seed RL evaluation (NeurIPS Outstanding Paper); our multi-seed experiment design follows this methodology to ensure statistical validity of collapse detection across seeds\"\n  relevance_score: 4",
    "originalFile": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 43 papers (5 existing + 38 new)\n\n# ============================================================\n# EXISTING CITATIONS (already in paper.tex)\n# ============================================================\n\n- paper_id: sutton1999options\n  title: \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\"\n  authors: [Sutton R.S., Precup D., Singh S.]\n  year: 1999\n  venue: \"Artificial Intelligence 112(1-2):181-211\"\n  category: background\n  role: \"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\"\n  relevance_score: 5\n\n- paper_id: hafner2020dreamerv1\n  title: \"Dream to Control: Learning Behaviors by Latent Imagination\"\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\n  year: 2020\n  venue: ICLR\n  category: background\n  role: \"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\"\n  relevance_score: 5\n\n- paper_id: hafner2023dreamerv3\n  title: \"Mastering Diverse Domains through World Models\"\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\n  year: 2023\n  venue: \"arXiv:2301.04104 (Nature 2025)\"\n  category: background\n  role: \"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\"\n  relevance_score: 5\n\n- paper_id: sharma2017figar\n  title: \"Fine Grained Action Repetition for Deep Reinforcement Learning\"\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\n  year: 2017\n  venue: \"ICLR Workshop\"\n  category: method-component\n  role: \"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\"\n  relevance_score: 4\n\n- paper_id: janner2019mbpo\n  title: \"When to Trust Your Model: Model-Based Policy Optimization\"\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\n  year: 2019\n  venue: NeurIPS\n  category: background\n  role: \"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Multi-step prediction error compounding\n# ============================================================\n\n- paper_id: ke2019learning\n  title: \"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\"\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\n  year: 2019\n  venue: ICLR\n  category: background\n  role: \"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\"\n  relevance_score: 4\n\n- paper_id: asadi2019combating\n  title: \"Combating the Compounding-Error Problem with a Multi-step Model\"\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\n  year: 2019\n  venue: \"arXiv:1905.13320\"\n  category: background\n  role: \"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\"\n  relevance_score: 4\n\n- paper_id: venkatraman2015improving\n  title: \"Improving Multi-Step Prediction of Learned Time Series Models\"\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\n  year: 2015\n  venue: AAAI\n  category: background\n  role: \"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\"\n  relevance_score: 3\n\n- paper_id: lambert2022investigating\n  title: \"Investigating Compounding Prediction Errors in Learned Dynamics Models\"\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\n  year: 2022\n  venue: \"arXiv:2203.09637\"\n  category: background\n  role: \"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Model-predictive control with learned dynamics\n# ============================================================\n\n- paper_id: chua2018pets\n  title: \"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\"\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\"\n  relevance_score: 3\n\n- paper_id: nagabandi2018neural\n  title: \"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\"\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\n  year: 2018\n  venue: ICRA\n  category: background\n  role: \"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Value overestimation mitigation\n# ============================================================\n\n- paper_id: thrun1993issues\n  title: \"Issues in Using Function Approximation for Reinforcement Learning\"\n  authors: [Thrun S., Schwartz A.]\n  year: 1993\n  venue: \"Connectionist Models Summer School\"\n  category: background\n  role: \"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\"\n  relevance_score: 4\n\n- paper_id: vanhasselt2016double\n  title: \"Deep Reinforcement Learning with Double Q-Learning\"\n  authors: [van Hasselt H., Guez A., Silver D.]\n  year: 2016\n  venue: AAAI\n  category: background\n  role: \"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\"\n  relevance_score: 4\n\n- paper_id: fujimoto2018td3\n  title: \"Addressing Function Approximation Error in Actor-Critic Methods\"\n  authors: [Fujimoto S., van Hoof H., Meger D.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\"\n  relevance_score: 4\n\n- paper_id: haarnoja2018sac\n  title: \"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\"\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\"\n  relevance_score: 3\n\n- paper_id: lee2021sunrise\n  title: \"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\"\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Delusional bias\n# ============================================================\n\n- paper_id: lu2018nondelusional\n  title: \"Non-delusional Q-learning and Value-Iteration\"\n  authors: [Lu T., Schuurmans D., Boutilier C.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Hierarchical RL with learned models\n# ============================================================\n\n- paper_id: hafner2022director\n  title: \"Deep Hierarchical Planning from Pixels\"\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\n  year: 2022\n  venue: NeurIPS\n  category: direct-competitor\n  role: \"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\"\n  relevance_score: 4\n\n- paper_id: nachum2018hiro\n  title: \"Data-Efficient Hierarchical Reinforcement Learning\"\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Action repeat / frame skip\n# ============================================================\n\n- paper_id: braylan2015frame\n  title: \"Frame Skip Is a Powerful Parameter for Learning to Play Atari\"\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\n  year: 2015\n  venue: \"AAAI Workshop on Learning for General Competency in Video Games\"\n  category: background\n  role: \"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\"\n  relevance_score: 3\n\n- paper_id: lakshminarayanan2017dynamic\n  title: \"Dynamic Action Repetition for Deep Reinforcement Learning\"\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\n  year: 2017\n  venue: AAAI\n  category: method-component\n  role: \"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\"\n  relevance_score: 4\n\n- paper_id: biedenkapp2021temporl\n  title: \"TempoRL: Learning When to Act\"\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV2\n# ============================================================\n\n- paper_id: hafner2021dreamerv2\n  title: \"Mastering Atari with Discrete World Models\"\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\n  year: 2021\n  venue: ICLR\n  category: background\n  role: \"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Alternative world model architectures\n# ============================================================\n\n- paper_id: micheli2023iris\n  title: \"Transformers are Sample-Efficient World Models\"\n  authors: [Micheli V., Alonso E., Fleuret F.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\"\n  relevance_score: 3\n\n- paper_id: robine2023twm\n  title: \"Transformer-based World Models Are Happy With 100k Interactions\"\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\"\n  relevance_score: 3\n\n- paper_id: chen2022transdreamer\n  title: \"TransDreamer: Reinforcement Learning with Transformer World Models\"\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\n  year: 2022\n  venue: \"arXiv:2202.09481\"\n  category: direct-competitor\n  role: \"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\n# ============================================================\n\n- paper_id: gumbsch2024thick\n  title: \"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\"\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\n  year: 2024\n  venue: ICLR\n  category: direct-competitor\n  role: \"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\"\n  relevance_score: 5\n\n- paper_id: mattes2024hieros\n  title: \"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\"\n  authors: [Mattes P., Schlosser R., Herbrich R.]\n  year: 2024\n  venue: ICML\n  category: direct-competitor\n  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Seed-dependent instability & value overestimation in MBRL\n# ============================================================\n\n- paper_id: henderson2018deep\n  title: \"Deep Reinforcement Learning that Matters\"\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\n  year: 2018\n  venue: AAAI\n  category: background\n  role: \"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\"\n  relevance_score: 4\n\n- paper_id: nikishin2022primacy\n  title: \"The Primacy Bias in Deep Reinforcement Learning\"\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\n  year: 2022\n  venue: ICML\n  category: background\n  role: \"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\"\n  relevance_score: 4\n\n- paper_id: qiao2023mind\n  title: \"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\"\n  authors: [Qiao Z., Lyu J., Li X.]\n  year: 2023\n  venue: \"arXiv:2310.15017 (ECAI 2024)\"\n  category: evaluation\n  role: \"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\"\n  relevance_score: 5\n\n- paper_id: hussing2024dissecting\n  title: \"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\"\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\n  year: 2024\n  venue: \"Reinforcement Learning Journal (RLC 2024)\"\n  category: evaluation\n  role: \"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\"\n  relevance_score: 4\n\n- paper_id: barkley2024stealing\n  title: \"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\"\n  authors: [Barkley B., Fridovich-Keil D.]\n  year: 2024\n  venue: \"arXiv:2412.14312 (ICML 2025)\"\n  category: evaluation\n  role: \"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\"\n  relevance_score: 3\n\n- paper_id: bjorck2022variance\n  title: \"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\"\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\n  year: 2022\n  venue: ICLR\n  category: background\n  role: \"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Reward prediction quality → MBRL performance\n# ============================================================\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\n# (0.01 → 0.747), making performance seed-dependent. These papers\n# establish that reward prediction quality is a known MBRL bottleneck.\n\n- paper_id: lee2024dreamsmooth\n  title: \"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\"\n  authors: [Lee V., Abbeel P., Lee Y.]\n  year: 2024\n  venue: ICLR\n  category: background\n  role: \"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\"\n  relevance_score: 5\n\n- paper_id: ma2024harmonydream\n  title: \"HarmonyDream: Task Harmonization Inside World Models\"\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\n  year: 2024\n  venue: ICML\n  category: background\n  role: \"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\"\n  relevance_score: 5\n\n- paper_id: lambert2020objective\n  title: \"Objective Mismatch in Model-based Reinforcement Learning\"\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\n  year: 2020\n  venue: \"L4DC (Proceedings of Machine Learning Research, vol. 120)\"\n  category: background\n  role: \"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: Auxiliary tasks & representation coupling in world models\n# ============================================================\n# Our finding: reward prediction quality is tightly coupled to temporal\n# conditioning (dt_embedding). Removing the embedding degrades the\n# reward head while dynamics remain intact — suggesting the reward head\n# acts as more than a passive predictor; it conditions the shared\n# representation. Literature gap: no prior work studies this coupling\n# specifically in Dreamer-family world models.\n\n- paper_id: jaderberg2017unreal\n  title: \"Reinforcement Learning with Unsupervised Auxiliary Tasks\"\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\n  year: 2017\n  venue: ICLR\n  category: background\n  role: \"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\"\n  relevance_score: 4\n\n- paper_id: lyle2021auxiliary\n  title: \"On The Effect of Auxiliary Tasks on Representation Dynamics\"\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\n  year: 2021\n  venue: AISTATS\n  category: background\n  role: \"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\"\n  relevance_score: 4\n",
    "structuredPatch": [
      {
        "oldStart": 413,
        "oldLines": 3,
        "newStart": 413,
        "newLines": 51,
        "lines": [
          "   category: background",
          "   role: \"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\"",
          "   relevance_score: 4",
          "+",
          "+# ============================================================",
          "+# NEW: DreamerV3 architecture improvements (2025-2026)",
          "+# ============================================================",
          "+",
          "+- paper_id: bredis2026nedreamer",
          "+  title: \"Next Embedding Prediction Makes World Models Stronger\"",
          "+  authors: [Bredis G., Balagansky N., Gavrilov D., Rakhimov R.]",
          "+  year: 2026",
          "+  venue: \"arXiv:2603.02765\"",
          "+  category: direct-competitor",
          "+  role: \"NE-Dreamer — decoder-free MBRL replacing pixel reconstruction with next-embedding prediction via temporal transformer + Barlow Twins; improves RSSM prediction quality on DMC and DMLab but does not address temporal abstraction or delusional critic — orthogonal to our dt-embedding diagnosis\"",
          "+  relevance_score: 3",
          "+",
          "+- paper_id: zhang2025dymodreamer",
          "+  title: \"DyMoDreamer: World Modeling with Dynamic Modulation\"",
          "+  authors: [Zhang B., Wang R., Xiao W., Zhang W., Sun J., Huang G., Chen J., Wang G.]",
          "+  year: 2025",
          "+  venue: NeurIPS",
          "+  category: direct-competitor",
          "+  role: \"Modulates RSSM via inter-frame differencing mask and stochastic categorical dynamic modulation; SOTA on Atari 100k (156.6% HNS) and DMC (832) — improves dynamics extraction but does not address variable-rate imagination or dt_embedding-induced value overestimation\"",
          "+  relevance_score: 3",
          "+",
          "+# ============================================================",
          "+# NEW: Temporal abstraction methods",
          "+# ============================================================",
          "+",
          "+- paper_id: liu2025vanta",
          "+  title: \"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning\"",
          "+  authors: [Liu T.-S., Liu X.-H., Chen R., Jin L., Wang P., Zhang Z., Yu Y.]",
          "+  year: 2025",
          "+  venue: ICLR",
          "+  category: method-component",
          "+  role: \"VanTA — VLM-guided trajectory decomposition into semantically meaningful skills via vector quantization + relabeling; operates at high-level skill abstraction (Franka Kitchen, Crafter) — contrasts with our low-level dt-based temporal abstraction within world-model imagination steps\"",
          "+  relevance_score: 3",
          "+",
          "+# ============================================================",
          "+# NEW: Evaluation methodology",
          "+# ============================================================",
          "+",
          "+- paper_id: agarwal2021precipice",
          "+  title: \"Deep Reinforcement Learning at the Edge of the Statistical Precipice\"",
          "+  authors: [Agarwal R., Schwarzer M., Castro P.S., Courville A.C., Bellemare M.]",
          "+  year: 2021",
          "+  venue: NeurIPS",
          "+  category: evaluation",
          "+  role: \"Proposes rliable — interval estimates, performance profiles, IQM for robust multi-seed RL evaluation (NeurIPS Outstanding Paper); our multi-seed experiment design follows this methodology to ensure statistical validity of collapse detection across seeds\"",
          "+  relevance_score: 4"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 37_

完成。汇总如下：

## Part 1：真实性验证

| 论文 | 结果 | 备注 |
|------|------|------|
| **HarmonyDream** (Ma et al., ICML 2024) | **真实，信息正确** | arXiv:2310.00344，Tsinghua thuml 组，yaml 中已有条目无需修改 |
| **"Mind the Model, Not the Agent"** (Qiao et al., ECAI 2024) | **真实，信息正确** | arXiv:2310.15017，IOS Press 出版，yaml 中已有条目无需修改 |

## Part 2：4 篇新文献已添加

| 论文 | 验证状态 | category / role | 与我们工作的 differentiation |
|------|----------|----------------|--------------------------|
| **NE-Dreamer** (Bredis et al., arXiv:2603.02765) | 真实。CoRL 2026 尚未举行（11月），标为 arXiv preprint | direct-competitor | 改进 RSSM 预测质量（next-embedding 替代 pixel reconstruction），但不涉及 temporal abstraction 或 dt_embedding 问题——与我们正交 |
| **DyMoDreamer** (Zhang et al., arXiv:2509.24804) | 真实。实际 venue 是 **NeurIPS 2025**（非仅 2025） | direct-competitor | 动态调制 RSSM 提升 dynamics 特征提取，Atari 100k SOTA，但不涉及 variable-rate imagination 或 value overestimation 诊断 |
| **VanTA** (Liu et al., ICLR 2025) | 真实 | method-component | High-level VLM-guided skill abstraction（Franka Kitchen/Crafter），与我们 low-level dt-based imagination abstraction 层级不同 |
| **Agarwal et al. 2021** (NeurIPS 2021) | 真实，Outstanding Paper Award | evaluation | rliable 评估方法论（IQM、performance profiles），我们的 multi-seed 实验设计遵循此标准 |

## Part 3

HarmonyDream 和 Qiao et al. 信息均已确认正确，无需修正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "uuid": "b7f32cf2-558b-464d-a73f-913d76aaa886",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fvpw6nykihS5XMdTZfHTjJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 49513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1216
      },
      "output_tokens": 1,
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

完成。汇总如下：

## Part 1：真实性验证

| 论文 | 结果 | 备注 |
|------|------|------|
| **HarmonyDream** (Ma et al., ICML 2024) | **真实，信息正确** | arXiv:2310.00344，Tsinghua thuml 组，yaml 中已有条目无需修改 |
| **"Mind the Model, Not the Agent"** (Qiao et al., ECAI 2024) | **真实，信息正确** | arXiv:2310.15017，IOS Press 出版，yaml 中已有条目无需修改 |

## Part 2：4 篇新文献已添加

| 论文 | 验证状态 | category / role | 与我们工作的 differentiation |
|------|----------|----------------|--------------------------|
| **NE-Dreamer** (Bredis et al., arXiv:2603.02765) | 真实。CoRL 2026 尚未举行（11月），标为 arXiv preprint | direct-competitor | 改进 RSSM 预测质量（next-embedding 替代 pixel reconstruction），但不涉及 temporal abstraction 或 dt_embedding 问题——与我们正交 |
| **DyMoDreamer** (Zhang et al., arXiv:2509.24804) | 真实。实际 venue 是 **NeurIPS 2025**（非仅 2025） | direct-competitor | 动态调制 RSSM 提升 dynamics 特征提取，Atari 100k SOTA，但不涉及 variable-rate imagination 或 value overestimation 诊断 |
| **VanTA** (Liu et al., ICLR 2025) | 真实 | method-component | High-level VLM-guided skill abstraction（Franka Kitchen/Crafter），与我们 low-level dt-based imagination abstraction 层级不同 |
| **Agarwal et al. 2021** (NeurIPS 2021) | 真实，Outstanding Paper Award | evaluation | rliable 评估方法论（IQM、performance profiles），我们的 multi-seed 实验设计遵循此标准 |

## Part 3

HarmonyDream 和 Qiao et al. 信息均已确认正确，无需修正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 155317,
  "duration_api_ms": 198336,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "f1af66ba-540f-4b09-bbc0-9152d0442e08",
  "total_cost_usd": 0.7464355,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 39282,
    "cache_read_input_tokens": 237346,
    "output_tokens": 5445,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 39282,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 636,
        "cache_read_input_tokens": 49513,
        "cache_creation_input_tokens": 1216,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1216
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 136385,
      "outputTokens": 3937,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 9,
      "costUSD": 0.24607,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 5445,
      "cacheReadInputTokens": 237346,
      "cacheCreationInputTokens": 39282,
      "webSearchRequests": 0,
      "costUSD": 0.5003655,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3b56d799-5397-417a-9955-b45d090883a1"
}
```

</details>

---
