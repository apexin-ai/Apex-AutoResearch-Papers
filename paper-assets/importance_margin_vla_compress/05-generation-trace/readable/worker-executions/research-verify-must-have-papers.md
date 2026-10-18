# research verify must have papers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_research_verify_must_have_papers_20260519T013320.log`
- **Structured JSON:** [`925aeecad1922de8ecd9.json`](../../sessions/92/925aeecad1922de8ecd9.json)

## Before a recorded user message

56 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
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
  "uuid": "bfb5294c-f001-4fd6-b595-181d567c3a10",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779172200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d787157d-325d-4f45-be07-68396e6aa8cb",
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to verify 4 papers that a reviewer mentioned. I need to search for each one using WebSearch and WebFetch. Let me load those tools first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "30a9b228-361e-4066-b127-44c109a182df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BWgEbAwTXSzyVJUEGAeUq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12819,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12819
      },
      "output_tokens": 29,
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

我来逐一验证这 4 篇论文。先加载搜索工具，然后并行搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "397dcdab-d49f-4e34-b0a1-e3afb8f230dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BWgEbAwTXSzyVJUEGAeUq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12819,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12819
      },
      "output_tokens": 29,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01U6vzLawpj8FjqsnctHxGEE`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "cf560b97-d832-4c8c-8c1f-6d0a24e247fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BWgEbAwTXSzyVJUEGAeUq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12819,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12819
      },
      "output_tokens": 29,
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

_source line 7 · 2026-05-19T01:33:33.763Z_

<details><summary>↩ Tool result · `toolu_01U6vzLawpj8FjqsnctHxGEE`</summary>

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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "7e7770aa-ea1a-4c68-a0cd-198fa1aec17d",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for all 4 papers in parallel. I'll start with the arXiv ID searches for each.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "98238e2d-c15c-4844-9959-5d36f82ee342",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FmocYpgyL8e8NwgRn9wzq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 24660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1186
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

### Assistant

_source line 9_

并行搜索 4 篇论文的 arXiv ID。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "dfea8b06-a75d-4988-9b3f-7acdbf5d5200",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FmocYpgyL8e8NwgRn9wzq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 24660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1186
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PcEKAcfpyujpzhL6S5Vi6E`</summary>

```json
{
  "query": "arXiv 2511.18950 Compressor-VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "8897c881-8c2b-4a6b-af09-1dfe0dd4c7ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FmocYpgyL8e8NwgRn9wzq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 24660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1186
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JdZ4xktGgUrcKXWpgFhxi2`</summary>

```json
{
  "query": "arXiv 2509.05614 SpecPrune-VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "b423acba-a757-4473-8a27-8b35fc3d84a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FmocYpgyL8e8NwgRn9wzq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 24660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1186
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016FRgz7xBn74GwrowxgmtSM`</summary>

```json
{
  "query": "arXiv 2509.12594 LightVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "a6214855-e419-4b3f-9c6c-9c4d79f44a34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FmocYpgyL8e8NwgRn9wzq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 24660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1186
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HfGdm4aaBZfp3NnBsZycfM`</summary>

```json
{
  "query": "\"See What Matters\" VLA compression ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "86675875-4be6-41e9-b7f3-3e3c11203344",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FmocYpgyL8e8NwgRn9wzq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 24660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1186
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

_source line 14 · 2026-05-19T01:33:43.746Z_

<details><summary>↩ Tool result · `toolu_01PcEKAcfpyujpzhL6S5Vi6E`</summary>

```text
Web search results for query: "arXiv 2511.18950 Compressor-VLA"

Links: [{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950"},{"title":"RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.17639"}]

Based on the search results, here's what I found about arXiv paper 2511.18950:

## Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation

This paper was authored by Juntao Gao, Feiyang Ye, Jing Zhang, and Wenjing Qian from the Beijing University of Technology and LiAuto Inc.

**Overview:**
The paper addresses the challenge that Vision-Language-Action (VLA) models, while powerful for Embodied AI, suffer from significant computational overhead due to processing redundant visual tokens, which is a critical bottleneck for real-time robotic deployment.

**Proposed Solution:**
Compressor-VLA is a novel hybrid instruction-conditioned token compression framework consisting of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. This compression is dynamically modulated by the natural language instruction, allowing for the adaptive condensation of task-relevant visual information.

**Results:**
Experimentally, Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline. Real-robot deployments on a dual-arm robot platform validate the model's sim-to-real transferability and practical applicability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "14c9e553-b635-4d84-9c92-6b8eba6f2caf",
  "tool_use_result": {
    "query": "arXiv 2511.18950 Compressor-VLA",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VLjRAQjm6oNfA53nPpqZh4",
        "content": [
          {
            "title": "[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/abs/2511.18950"
          },
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2511.18950"
          },
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://chatpaper.com/paper/212383"
          },
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.18950"
          },
          {
            "title": "RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2506.17639"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2511.18950:\n\n## Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\n\nThis paper was authored by Juntao Gao, Feiyang Ye, Jing Zhang, and Wenjing Qian from the Beijing University of Technology and LiAuto Inc.\n\n**Overview:**\nThe paper addresses the challenge that Vision-Language-Action (VLA) models, while powerful for Embodied AI, suffer from significant computational overhead due to processing redundant visual tokens, which is a critical bottleneck for real-time robotic deployment.\n\n**Proposed Solution:**\nCompressor-VLA is a novel hybrid instruction-conditioned token compression framework consisting of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. This compression is dynamically modulated by the natural language instruction, allowing for the adaptive condensation of task-relevant visual information.\n\n**Results:**\nExperimentally, Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline. Real-robot deployments on a dual-arm robot platform validate the model's sim-to-real transferability and practical applicability."
    ],
    "durationSeconds": 5.534097803000001
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T01:33:44.392Z_

<details><summary>↩ Tool result · `toolu_01JdZ4xktGgUrcKXWpgFhxi2`</summary>

```text
Web search results for query: "arXiv 2509.05614 SpecPrune-VLA"

Links: [{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/abs/2509.05614"},{"title":"Specprune-vla Boosts Vision-Language-Action Models, Avoiding Over 20% Success Rate Drops With Smart Pruning","url":"https://quantumzeitgeist.com/faster-models-performance-specprune-vla-boosts-vision-language-action-avoiding-success/"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | Request PDF","url":"https://www.researchgate.net/publication/395354566_SpecPrune-VLA_Accelerating_Vision-Language-Action_Models_via_Action-Aware_Self-Speculative_Pruning"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"},{"title":"SPECPRUNE-VLA:","url":"https://openreview.net/pdf/f898de78034757b0bb38f30b7b6fd21bca97b4ad.pdf"}]

Based on the search results, here's information about arXiv paper 2509.05614 on SpecPrune-VLA:

## Overview

SpecPrune-VLA is a training-free, two-level pruning method with heuristic control designed to accelerate Vision-Language-Action (VLA) models.

## Problem Addressed

Existing acceleration methods focus on local information from the current action step and ignore the global context, leading to >20% success rate drop and limited speedup in some scenarios. The paper points out spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and proposes that token selection should combine local information with global context of the model.

## Key Components

The method has three main components:

1. Action-Level Static Pruning: leveraging global history and local attention to statically reduce visual tokens per action

2. Layer-Level Dynamic Pruning: pruning tokens adaptively per layer based on layer-wise importance

3. Lightweight Action-Aware Controller: classifying actions as coarse- or fine-grained by the speed of the end effector, with fine-grained actions being pruning-sensitive

## Results

SpecPrune-VLA achieves up to 1.57× speedup in the LIBERO simulation benchmark across different hardware configurations, and an average speedup of 1.70× in real-world robotic tasks, with negligible degradation in task success rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "4f1c1307-59da-44c9-b3f2-e58909cdcc86",
  "tool_use_result": {
    "query": "arXiv 2509.05614 SpecPrune-VLA",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X1ohuNo5gccYLo7PbNsPvL",
        "content": [
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware",
            "url": "https://arxiv.org/pdf/2509.05614"
          },
          {
            "title": "[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning",
            "url": "https://arxiv.org/abs/2509.05614"
          },
          {
            "title": "Specprune-vla Boosts Vision-Language-Action Models, Avoiding Over 20% Success Rate Drops With Smart Pruning",
            "url": "https://quantumzeitgeist.com/faster-models-performance-specprune-vla-boosts-vision-language-action-avoiding-success/"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning",
            "url": "https://arxiv.org/html/2509.05614v1"
          },
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | Request PDF",
            "url": "https://www.researchgate.net/publication/395354566_SpecPrune-VLA_Accelerating_Vision-Language-Action_Models_via_Action-Aware_Self-Speculative_Pruning"
          },
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview",
            "url": "https://openreview.net/forum?id=t85Ni0LwjC"
          },
          {
            "title": "SPECPRUNE-VLA:",
            "url": "https://openreview.net/pdf/f898de78034757b0bb38f30b7b6fd21bca97b4ad.pdf"
          }
        ]
      },
      "Based on the search results, here's information about arXiv paper 2509.05614 on SpecPrune-VLA:\n\n## Overview\n\nSpecPrune-VLA is a training-free, two-level pruning method with heuristic control designed to accelerate Vision-Language-Action (VLA) models.\n\n## Problem Addressed\n\nExisting acceleration methods focus on local information from the current action step and ignore the global context, leading to >20% success rate drop and limited speedup in some scenarios. The paper points out spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and proposes that token selection should combine local information with global context of the model.\n\n## Key Components\n\nThe method has three main components:\n\n1. Action-Level Static Pruning: leveraging global history and local attention to statically reduce visual tokens per action\n\n2. Layer-Level Dynamic Pruning: pruning tokens adaptively per layer based on layer-wise importance\n\n3. Lightweight Action-Aware Controller: classifying actions as coarse- or fine-grained by the speed of the end effector, with fine-grained actions being pruning-sensitive\n\n## Results\n\nSpecPrune-VLA achieves up to 1.57× speedup in the LIBERO simulation benchmark across different hardware configurations, and an average speedup of 1.70× in real-world robotic tasks, with negligible degradation in task success rate."
    ],
    "durationSeconds": 6.092074664
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T01:33:44.696Z_

<details><summary>↩ Tool result · `toolu_01HfGdm4aaBZfp3NnBsZycfM`</summary>

```text
Web search results for query: ""See What Matters" VLA compression ICML 2026"

Links: [{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/pdf/2510.08464"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models","url":"https://arxiv.org/pdf/2509.09090"}]

Based on the search results, I found research related to VLA (Vision-Language-Action) compression, but the specific paper titled "See What Matters" doesn't appear in these results. However, I did find several relevant papers on VLA compression presented at major conferences:

1. **Compressor-VLA** - A novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models.

2. **SQAP-VLA** - A framework for Vision-Language-Action models to address their substantial computational and memory demands through effective model compression strategies.

The search results include various VLA papers from 2025-2026, but don't specifically show "See What Matters" as a paper title. It's possible this paper may be:
- Known by a slightly different title
- Presented at ICML 2026 rather than ICLR
- Not yet widely indexed in the search results

Would you like me to search with different keywords or terms related to this paper?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "5a44c92d-ebf6-47ea-9b82-8940b899b4f3",
  "tool_use_result": {
    "query": "\"See What Matters\" VLA compression ICML 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N25aejwcExt52adLDHT3yr",
        "content": [
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2511.18950"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered",
            "url": "https://arxiv.org/pdf/2510.08464"
          },
          {
            "title": "ICLR 2026 Schedule",
            "url": "https://iclr.cc/virtual/2026/calendar"
          },
          {
            "title": "SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2509.09090"
          }
        ]
      },
      "Based on the search results, I found research related to VLA (Vision-Language-Action) compression, but the specific paper titled \"See What Matters\" doesn't appear in these results. However, I did find several relevant papers on VLA compression presented at major conferences:\n\n1. **Compressor-VLA** - A novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models.\n\n2. **SQAP-VLA** - A framework for Vision-Language-Action models to address their substantial computational and memory demands through effective model compression strategies.\n\nThe search results include various VLA papers from 2025-2026, but don't specifically show \"See What Matters\" as a paper title. It's possible this paper may be:\n- Known by a slightly different title\n- Presented at ICML 2026 rather than ICLR\n- Not yet widely indexed in the search results\n\nWould you like me to search with different keywords or terms related to this paper?"
    ],
    "durationSeconds": 5.638181293
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T01:33:45.481Z_

<details><summary>↩ Tool result · `toolu_016FRgz7xBn74GwrowxgmtSM`</summary>

```text
Web search results for query: "arXiv 2509.12594 LightVLA"

Links: [{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"}]

Based on the search results, here's what I found about arXiv paper 2509.12594 and LightVLA:

LightVLA is a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by the heavy attention-based computation over large sets of visual tokens.

LightVLA addresses this challenge through adaptive, performance-driven pruning of visual tokens by generating dynamic queries to evaluate visual token importance and adopting Gumbel softmax to enable differentiable token selection. Through fine-tuning, LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution, thereby improving efficiency and performance simultaneously.

Key features include:
- LightVLA requires no heuristic magic numbers and introduces no additional trainable parameters, making it compatible with modern inference frameworks.
- LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.9% improvement in task success rate.
- Experimental results demonstrate that LightVLA outperforms different VLA models and existing token pruning methods across diverse tasks on the LIBERO benchmark.

The paper was submitted on September 16, 2025, with a revision on September 21, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "6816a3eb-386e-4492-abe5-530068ae3ec1",
  "tool_use_result": {
    "query": "arXiv 2509.12594 LightVLA",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PFenkSJfNd4B8yDdSvhQKz",
        "content": [
          {
            "title": "[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/abs/2509.12594"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/pdf/2509.12594"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/html/2509.12594v1"
          },
          {
            "title": "GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)",
            "url": "https://github.com/LiAutoAD/LightVLA"
          },
          {
            "title": "Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium",
            "url": "https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2509.12594 and LightVLA:\n\nLightVLA is a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by the heavy attention-based computation over large sets of visual tokens.\n\nLightVLA addresses this challenge through adaptive, performance-driven pruning of visual tokens by generating dynamic queries to evaluate visual token importance and adopting Gumbel softmax to enable differentiable token selection. Through fine-tuning, LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution, thereby improving efficiency and performance simultaneously.\n\nKey features include:\n- LightVLA requires no heuristic magic numbers and introduces no additional trainable parameters, making it compatible with modern inference frameworks.\n- LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.9% improvement in task success rate.\n- Experimental results demonstrate that LightVLA outperforms different VLA models and existing token pruning methods across diverse tasks on the LIBERO benchmark.\n\nThe paper was submitted on September 16, 2025, with a revision on September 21, 2025."
    ],
    "durationSeconds": 6.651000516000002
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Good, I found 3 out of 4 papers. Let me now:
1. Fetch the arXiv pages for papers 1-3 to get more details
2. Do additional searches for paper 4 "See What Matters"

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "0e98d1ac-9cc2-41e9-a01d-59333d72eafb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ftp7Bi5KnNfAMKTnRGe6j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 533,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 25846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2546
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

_source line 19_

前 3 篇已找到，第 4 篇需要更多搜索。并行获取详情和扩展搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "c6c063fc-6855-4a54-8f98-731e853cf56e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ftp7Bi5KnNfAMKTnRGe6j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 533,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 25846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2546
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

_source line 20_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X5iTiUxjHQHK2kLaYxmdYc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.18950",
  "prompt": "Extract: full title, all authors, submission date, abstract. Is this about VLA token compression? What benchmark and success rate?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "73d4b5da-6a73-41fd-8c27-899a199850d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ftp7Bi5KnNfAMKTnRGe6j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 533,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 25846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2546
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

_source line 21_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TBHLSqbQjidCBsoMJSdpSc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.05614",
  "prompt": "Extract: full title, all authors, submission date, abstract. Is this about VLA token pruning? What benchmark, speedup, and success rate?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "b2fe103e-18b1-420c-abcb-4165d8fc9bd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ftp7Bi5KnNfAMKTnRGe6j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 533,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 25846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2546
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

_source line 22_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Pa3ucVNNJF7DNpoaatxsex`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.12594",
  "prompt": "Extract: full title, all authors, submission date, abstract. Is this LightVLA? What benchmark, FLOPs reduction, and success rate improvement?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "4b2f8eb5-25ac-4433-bbf8-d6cbc9230007",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ftp7Bi5KnNfAMKTnRGe6j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 533,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 25846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2546
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

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UyWssUMzEdcUb2gTrVRHab`</summary>

```json
{
  "query": "\"See What Matters\" vision language action grid compression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "b55e4d2b-677d-4c16-8162-766214d48157",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ftp7Bi5KnNfAMKTnRGe6j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 533,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 25846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2546
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

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rn6YSQgqvfjTjVGxFXPQHh`</summary>

```json
{
  "query": "\"See What Matters\" VLA token pruning robot manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "b5f0176a-b637-4e29-918b-1adf3f686e3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ftp7Bi5KnNfAMKTnRGe6j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 533,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 25846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2546
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

_source line 25 · 2026-05-19T01:33:55.513Z_

<details><summary>↩ Tool result · `toolu_01X5iTiUxjHQHK2kLaYxmdYc`</summary>

```text
# Paper Extraction

**Full Title:** "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation"

**Authors:** Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian

**Submission Date:** November 24, 2025

**Abstract:** The paper proposes a framework that addresses computational overhead in Vision-Language-Action models through instruction-conditioned token compression. It employs two modules—one distilling semantic task context and another preserving spatial details—to dynamically reduce visual information processing. The approach achieved "a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline."

**Is this about VLA token compression?** Yes, directly.

**Benchmark and Success Rate:** The work evaluated performance on LIBERO, though the abstract does not specify an exact success rate percentage—only describing it as "competitive" relative to the baseline model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "b0bd06b4-678e-47a1-9a9d-e4c563884282",
  "tool_use_result": {
    "bytes": 47906,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Extraction\n\n**Full Title:** \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\"\n\n**Authors:** Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian\n\n**Submission Date:** November 24, 2025\n\n**Abstract:** The paper proposes a framework that addresses computational overhead in Vision-Language-Action models through instruction-conditioned token compression. It employs two modules—one distilling semantic task context and another preserving spatial details—to dynamically reduce visual information processing. The approach achieved \"a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline.\"\n\n**Is this about VLA token compression?** Yes, directly.\n\n**Benchmark and Success Rate:** The work evaluated performance on LIBERO, though the abstract does not specify an exact success rate percentage—only describing it as \"competitive\" relative to the baseline model.",
    "durationMs": 4297,
    "url": "https://arxiv.org/abs/2511.18950"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T01:33:57.602Z_

<details><summary>↩ Tool result · `toolu_01TBHLSqbQjidCBsoMJSdpSc`</summary>

```text
# SpecPrune-VLA Research Paper Summary

**Full Title:** "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning"

**Authors:** Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, Guohao Dai

**Submission Date:** September 6, 2025 (revised February 9, 2026)

## Is This About VLA Token Pruning?
Yes. The paper directly addresses pruning Vision-Language-Action models by removing computationally unnecessary tokens while maintaining performance.

## Key Performance Metrics

**Benchmarks Tested:**
- LIBERO simulation environment
- Real-world robotic tasks

**Speedup Achieved:**
- Up to 1.57× faster inference in LIBERO simulation
- Up to 1.70× speedup on real-world tasks

**Success Rate Impact:**
The abstract states the method achieves results "with negligible success rate degradation," contrasting favorably with existing methods that cause ">20% success rate drop."

## Core Innovation
The approach combines spatial-temporal consistency observation with a two-level pruning strategy: action-level static pruning and layer-level dynamic pruning, guided by an action-aware controller that adjusts based on end-effector movement speed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "1594b30d-91f8-4e3e-a984-dd6f47a78ff3",
  "tool_use_result": {
    "bytes": 47468,
    "code": 200,
    "codeText": "OK",
    "result": "# SpecPrune-VLA Research Paper Summary\n\n**Full Title:** \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\"\n\n**Authors:** Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, Guohao Dai\n\n**Submission Date:** September 6, 2025 (revised February 9, 2026)\n\n## Is This About VLA Token Pruning?\nYes. The paper directly addresses pruning Vision-Language-Action models by removing computationally unnecessary tokens while maintaining performance.\n\n## Key Performance Metrics\n\n**Benchmarks Tested:**\n- LIBERO simulation environment\n- Real-world robotic tasks\n\n**Speedup Achieved:**\n- Up to 1.57× faster inference in LIBERO simulation\n- Up to 1.70× speedup on real-world tasks\n\n**Success Rate Impact:**\nThe abstract states the method achieves results \"with negligible success rate degradation,\" contrasting favorably with existing methods that cause \">20% success rate drop.\"\n\n## Core Innovation\nThe approach combines spatial-temporal consistency observation with a two-level pruning strategy: action-level static pruning and layer-level dynamic pruning, guided by an action-aware controller that adjusts based on end-effector movement speed.",
    "durationMs": 6038,
    "url": "https://arxiv.org/abs/2509.05614"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T01:33:58.228Z_

<details><summary>↩ Tool result · `toolu_01Pa3ucVNNJF7DNpoaatxsex`</summary>

```text
# Paper Summary

**Full Title:** "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning"

**Authors:** Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang

**Submission Date:** September 16, 2025 (v1); revised September 21, 2025 (v2)

**Is this LightVLA?** Yes, this paper presents LightVLA, a token pruning framework for vision-language-action models.

**Key Performance Metrics:**
- **Benchmark:** LIBERO benchmark
- **FLOPs Reduction:** 59.1%
- **Latency Reduction:** 38.2%
- **Success Rate Improvement:** 2.6%

**Abstract Summary:** The framework uses adaptive, performance-driven pruning of visual tokens through dynamic queries and Gumbel softmax for differentiable selection. "LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution" while maintaining compatibility with modern inference systems and introducing no additional trainable parameters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "4adb6a47-5b23-4e5f-a83e-d9ef5ebb5b7d",
  "tool_use_result": {
    "bytes": 50163,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Full Title:** \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning\"\n\n**Authors:** Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang\n\n**Submission Date:** September 16, 2025 (v1); revised September 21, 2025 (v2)\n\n**Is this LightVLA?** Yes, this paper presents LightVLA, a token pruning framework for vision-language-action models.\n\n**Key Performance Metrics:**\n- **Benchmark:** LIBERO benchmark\n- **FLOPs Reduction:** 59.1%\n- **Latency Reduction:** 38.2%\n- **Success Rate Improvement:** 2.6%\n\n**Abstract Summary:** The framework uses adaptive, performance-driven pruning of visual tokens through dynamic queries and Gumbel softmax for differentiable selection. \"LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution\" while maintaining compatibility with modern inference systems and introducing no additional trainable parameters.",
    "durationMs": 5740,
    "url": "https://arxiv.org/abs/2509.12594"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T01:34:00.032Z_

<details><summary>↩ Tool result · `toolu_01UyWssUMzEdcUb2gTrVRHab`</summary>

```text
Web search results for query: ""See What Matters" vision language action grid compression"

Links: [{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"The Compression Gap: Why Discrete Tokenization Limits Vision-Language-Action Model Scaling","url":"https://arxiv.org/pdf/2604.03191"},{"title":"Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2512.09927"},{"title":"DepthCache: Depth-Guided Training-Free Visual Token Merging for Vision-Language-Action Model Inference","url":"https://arxiv.org/pdf/2603.10469"},{"title":"RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.17639"}]

Based on the search results, I found several papers related to vision-language-action models and token compression, but the specific paper titled "See What Matters" doesn't appear in these results. However, the search returned several highly relevant papers on vision-language-action (VLA) model compression:

1. **Compressor-VLA** - A framework that addresses efficiency bottlenecks in Vision-Language-Action models through instruction-guided visual token compression, combining a Spatial Refinement Compressor for spatial detail and a Semantic Task Compressor for contextual summary.

2. **The Compression Gap** - An information-theoretic principle explaining that scaling behavior in visuomotor pipelines is governed by the location of the tightest information bottleneck.

3. **Token Expand-Merge (TEAM-VLA)** - A training-free token compression framework that accelerates VLA inference while preserving task performance, introducing a dynamic token expansion mechanism that identifies and samples additional informative tokens in the spatial vicinity of attention-highlighted regions.

4. **DepthCache** - A compression mechanism that uses depth maps from simulators or RGB-D sensors as a structural signal for spatially differentiated compression in robotic manipulation scenes.

If you're looking for a specific paper titled "See What Matters," you may want to try a more targeted search or provide additional details about the authors or publication venue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "b29fed39-75f6-4c4e-8a23-ba68bee27028",
  "tool_use_result": {
    "query": "\"See What Matters\" vision language action grid compression",
    "results": [
      {
        "tool_use_id": "srvtoolu_015xnKMNvLqUceKGvT8w8H5L",
        "content": [
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.18950v1"
          },
          {
            "title": "The Compression Gap: Why Discrete Tokenization Limits Vision-Language-Action Model Scaling",
            "url": "https://arxiv.org/pdf/2604.03191"
          },
          {
            "title": "Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2512.09927"
          },
          {
            "title": "DepthCache: Depth-Guided Training-Free Visual Token Merging for Vision-Language-Action Model Inference",
            "url": "https://arxiv.org/pdf/2603.10469"
          },
          {
            "title": "RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2506.17639"
          }
        ]
      },
      "Based on the search results, I found several papers related to vision-language-action models and token compression, but the specific paper titled \"See What Matters\" doesn't appear in these results. However, the search returned several highly relevant papers on vision-language-action (VLA) model compression:\n\n1. **Compressor-VLA** - A framework that addresses efficiency bottlenecks in Vision-Language-Action models through instruction-guided visual token compression, combining a Spatial Refinement Compressor for spatial detail and a Semantic Task Compressor for contextual summary.\n\n2. **The Compression Gap** - An information-theoretic principle explaining that scaling behavior in visuomotor pipelines is governed by the location of the tightest information bottleneck.\n\n3. **Token Expand-Merge (TEAM-VLA)** - A training-free token compression framework that accelerates VLA inference while preserving task performance, introducing a dynamic token expansion mechanism that identifies and samples additional informative tokens in the spatial vicinity of attention-highlighted regions.\n\n4. **DepthCache** - A compression mechanism that uses depth maps from simulators or RGB-D sensors as a structural signal for spatially differentiated compression in robotic manipulation scenes.\n\nIf you're looking for a specific paper titled \"See What Matters,\" you may want to try a more targeted search or provide additional details about the authors or publication venue."
    ],
    "durationSeconds": 7.016932319000003
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T01:34:01.892Z_

<details><summary>↩ Tool result · `toolu_01Rn6YSQgqvfjTjVGxFXPQHh`</summary>

```text
Web search results for query: ""See What Matters" VLA token pruning robot manipulation 2025 2026"

Links: [{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"},{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/pdf/2509.22093"},{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/pdf/2602.20566"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.22991"},{"title":"DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models","url":"https://arxiv.org/pdf/2601.16065"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"}]

I found relevant research on "See What Matters" and VLA token pruning for robot manipulation. Here are the key findings:

## See What Matters (GridS)

The research proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA by adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation. The work addresses a fundamental trade-off where aggressive compression using pruning discards critical geometric details like contact points, leading to severe performance degradation.

## VLA Token Pruning for Robot Manipulation

The search results show several recent approaches to token pruning for Vision-Language-Action (VLA) models:

1. **VLA-Pruner**: A plug-and-play VLA token pruning method that aligns with the dual-system nature of VLA models and exploits temporal continuity in robot manipulation, achieving up to 1.99× speedup with comparable manipulation quality.

2. **Action-aware Dynamic Pruning**: The importance of visual tokens in VLA models varies within different stages of robotic manipulation, motivating dynamic pruning methods that combine task instruction relevance with a gating rule based on end-effector motion.

3. **BFA++**: A hierarchical pruning strategy with two-level importance predictors that identify task-relevant regions within images and critical camera views, while preserving essential visual cues.

These papers were recently published (appearing in 2025-2026 conference venues) and represent the current state of research in efficient VLA inference for robotic manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "de4cf000-0989-43fc-94bf-32c2d0788137",
  "tool_use_result": {
    "query": "\"See What Matters\" VLA token pruning robot manipulation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PS6B3r3hm9jh5QsRbZyQiP",
        "content": [
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/pdf/2511.16449"
          },
          {
            "title": "Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation",
            "url": "https://arxiv.org/pdf/2509.22093"
          },
          {
            "title": "ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model",
            "url": "https://icml.cc/virtual/2026/poster/65010"
          },
          {
            "title": "BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model",
            "url": "https://arxiv.org/pdf/2602.20566"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.22991"
          },
          {
            "title": "DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models",
            "url": "https://arxiv.org/pdf/2601.16065"
          },
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2511.18950"
          }
        ]
      },
      "I found relevant research on \"See What Matters\" and VLA token pruning for robot manipulation. Here are the key findings:\n\n## See What Matters (GridS)\n\nThe research proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA by adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation. The work addresses a fundamental trade-off where aggressive compression using pruning discards critical geometric details like contact points, leading to severe performance degradation.\n\n## VLA Token Pruning for Robot Manipulation\n\nThe search results show several recent approaches to token pruning for Vision-Language-Action (VLA) models:\n\n1. **VLA-Pruner**: A plug-and-play VLA token pruning method that aligns with the dual-system nature of VLA models and exploits temporal continuity in robot manipulation, achieving up to 1.99× speedup with comparable manipulation quality.\n\n2. **Action-aware Dynamic Pruning**: The importance of visual tokens in VLA models varies within different stages of robotic manipulation, motivating dynamic pruning methods that combine task instruction relevance with a gating rule based on end-effector motion.\n\n3. **BFA++**: A hierarchical pruning strategy with two-level importance predictors that identify task-relevant regions within images and critical camera views, while preserving essential visual cues.\n\nThese papers were recently published (appearing in 2025-2026 conference venues) and represent the current state of research in efficient VLA inference for robotic manipulation."
    ],
    "durationSeconds": 8.498881066000001
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
I found the 4th paper too. Let me fetch the ICML poster page and try to find the arXiv version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "84521878-947c-4ea6-9c2e-2f063c78bd6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQuSy313PWmFxhxEtnNEoe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3457,
      "cache_read_input_tokens": 28392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3457
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

_source line 31_

第 4 篇也找到了，在 ICML 2026 poster 页面。获取详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "fea958f8-3254-4995-829f-05160051f057",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQuSy313PWmFxhxEtnNEoe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3457,
      "cache_read_input_tokens": 28392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3457
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

_source line 32_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Hmr7GhmbR6jLN2bJRBtGYA`</summary>

```json
{
  "url": "https://icml.cc/virtual/2026/poster/65010",
  "prompt": "Extract: full title, all authors, abstract, key method details. What is GridS? What benchmark and results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "424546f6-86d8-4a80-8bc7-c64604f66eeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQuSy313PWmFxhxEtnNEoe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3457,
      "cache_read_input_tokens": 28392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3457
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

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014upnMBFHb1fduJgfckiY4f`</summary>

```json
{
  "query": "\"See What Matters\" \"Differentiable Grid Sample Pruning\" VLA arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "14fb5d67-2964-4231-8dc5-f9e76194d17f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQuSy313PWmFxhxEtnNEoe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3457,
      "cache_read_input_tokens": 28392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3457
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

_source line 34_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0144oySvgVsoDtsbXekakD8i`</summary>

```json
{
  "url": "https://github.com/LiAutoAD/LightVLA",
  "prompt": "Confirm this is LightVLA, check if it mentions ICRA 2026, list authors or affiliations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "74384153-57ee-4b2b-8518-75cf3381b134",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQuSy313PWmFxhxEtnNEoe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3457,
      "cache_read_input_tokens": 28392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3457
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

_source line 35 · 2026-05-19T01:34:10.721Z_

<details><summary>↩ Tool result · `toolu_01Hmr7GhmbR6jLN2bJRBtGYA`</summary>

```text
# See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model

**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu

## Abstract
The paper addresses computational efficiency in Vision-Language-Action models for robotics. Traditional token pruning creates a problematic compromise: aggressive compression removes critical spatial details like contact points, degrading performance. The authors propose rethinking this as a continuous geometry-aware resampling challenge.

## GridS Overview
GridS (Differentiable Grid Sampler) is a "plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA." It operates by predicting minimal salient coordinates and extracting features through differentiable interpolation, enabling extreme compression while preserving spatial information critical for robotic tasks.

## Results & Benchmarks
- **Benchmark:** LIBERO benchmark and real robotic platform evaluation
- **Key Achievement:** "76% reduction in FLOPs with no degradation in the success rate"
- **Compression Rate:** Uses fewer than 10% of original visual tokens
- **Significance:** Researchers note this represents "the lowest feasible visual token count reported to date"

The method successfully breaks the traditional pruning trade-off by maintaining performance while dramatically reducing computational demands.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "ebf1908a-a3d0-49d7-bd89-5c906120eeb5",
  "tool_use_result": {
    "bytes": 87504,
    "code": 200,
    "codeText": "OK",
    "result": "# See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\n\n**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu\n\n## Abstract\nThe paper addresses computational efficiency in Vision-Language-Action models for robotics. Traditional token pruning creates a problematic compromise: aggressive compression removes critical spatial details like contact points, degrading performance. The authors propose rethinking this as a continuous geometry-aware resampling challenge.\n\n## GridS Overview\nGridS (Differentiable Grid Sampler) is a \"plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA.\" It operates by predicting minimal salient coordinates and extracting features through differentiable interpolation, enabling extreme compression while preserving spatial information critical for robotic tasks.\n\n## Results & Benchmarks\n- **Benchmark:** LIBERO benchmark and real robotic platform evaluation\n- **Key Achievement:** \"76% reduction in FLOPs with no degradation in the success rate\"\n- **Compression Rate:** Uses fewer than 10% of original visual tokens\n- **Significance:** Researchers note this represents \"the lowest feasible visual token count reported to date\"\n\nThe method successfully breaks the traditional pruning trade-off by maintaining performance while dramatically reducing computational demands.",
    "durationMs": 4238,
    "url": "https://icml.cc/virtual/2026/poster/65010"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T01:34:12.313Z_

<details><summary>↩ Tool result · `toolu_014upnMBFHb1fduJgfckiY4f`</summary>

```text
Web search results for query: ""See What Matters" "Differentiable Grid Sample Pruning" VLA arXiv"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"PDP: Parameter-free Differentiable Pruning is All You Need","url":"https://arxiv.org/pdf/2305.11203"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"}]

Based on the search results, I found the paper you're looking for:

"See What Matters" proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA. By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression.

The paper addresses a key challenge in Vision-Language-Action models: existing token pruning methods suffer from a trade-off where aggressive compression discards critical geometric details like contact points, leading to performance degradation and limiting compression rates.

The research appears to have been recently presented at ICML 2026, as indicated by the poster presentation link in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "4bc8b604-62bb-4207-ac05-9c3ca4d3d6ba",
  "tool_use_result": {
    "query": "\"See What Matters\" \"Differentiable Grid Sample Pruning\" VLA arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01792cF1EmCqKzmzkK76AxU2",
        "content": [
          {
            "title": "ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model",
            "url": "https://icml.cc/virtual/2026/poster/65010"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/pdf/2509.12594"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/html/2509.12594v1"
          },
          {
            "title": "[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/abs/2509.12594"
          },
          {
            "title": "PDP: Parameter-free Differentiable Pruning is All You Need",
            "url": "https://arxiv.org/pdf/2305.11203"
          },
          {
            "title": "Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2602.00780"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"See What Matters\" proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA. By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression.\n\nThe paper addresses a key challenge in Vision-Language-Action models: existing token pruning methods suffer from a trade-off where aggressive compression discards critical geometric details like contact points, leading to performance degradation and limiting compression rates.\n\nThe research appears to have been recently presented at ICML 2026, as indicated by the poster presentation link in the search results."
    ],
    "durationSeconds": 5.349254255
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T01:34:13.003Z_

<details><summary>↩ Tool result · `toolu_0144oySvgVsoDtsbXekakD8i`</summary>

```text
# LightVLA Verification

**Is this LightVLA?** Yes, confirmed.

**ICRA 2026 Mention?** Yes. The repository states: "LightVLA has been accepted by **ICRA 2026**! 🎉" (dated 2026-01-31).

**Authors/Affiliations:**
The paper credits include Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, and Xianpeng Lang. The repository is maintained under the LiAutoAD organization. No explicit institutional affiliations are listed on this GitHub page, though the project website and paper (arXiv 2509.12594) may contain additional details.

**Key focus:** This is a "differentiable token pruning framework designed for Vision-Language-Action (VLA) models" that achieves significant computational efficiency gains while improving task performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "4d3e0753-5add-4a6c-8f20-9d734bdda85a",
  "tool_use_result": {
    "bytes": 322564,
    "code": 200,
    "codeText": "OK",
    "result": "# LightVLA Verification\n\n**Is this LightVLA?** Yes, confirmed.\n\n**ICRA 2026 Mention?** Yes. The repository states: \"LightVLA has been accepted by **ICRA 2026**! 🎉\" (dated 2026-01-31).\n\n**Authors/Affiliations:**\nThe paper credits include Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, and Xianpeng Lang. The repository is maintained under the LiAutoAD organization. No explicit institutional affiliations are listed on this GitHub page, though the project website and paper (arXiv 2509.12594) may contain additional details.\n\n**Key focus:** This is a \"differentiable token pruning framework designed for Vision-Language-Action (VLA) models\" that achieves significant computational efficiency gains while improving task performance.",
    "durationMs": 4989,
    "url": "https://github.com/LiAutoAD/LightVLA"
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the arXiv ID of "See What Matters" paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "d56437bd-ee4f-4191-bacf-59fa264a89e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GF94nX4xz2MAoqLFURMCkC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1504,
      "cache_read_input_tokens": 31849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1504
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

_source line 39_

搜索第 4 篇的 arXiv ID。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "064c0839-96bc-485d-aba0-c6f92b08c0d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GF94nX4xz2MAoqLFURMCkC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1504,
      "cache_read_input_tokens": 31849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1504
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

_source line 40_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FQwyLiyzmKX2zinbqMua6w`</summary>

```json
{
  "query": "\"See What Matters\" Yixu Feng GridS VLA arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "2c3603ab-7c79-434b-869b-92c38afd5722",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GF94nX4xz2MAoqLFURMCkC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1504,
      "cache_read_input_tokens": 31849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1504
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

_source line 41_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fy9WyVNoEg25rWz3iY4RxQ`</summary>

```json
{
  "url": "https://openreview.net/forum?id=t85Ni0LwjC",
  "prompt": "What venue was SpecPrune-VLA submitted to? Was it accepted? What conference/workshop?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "e9ba95ea-2484-48d4-81ab-20475a71600b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GF94nX4xz2MAoqLFURMCkC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1504,
      "cache_read_input_tokens": 31849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1504
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

_source line 42 · 2026-05-19T01:34:23.263Z_

<details><summary>↩ Tool result · `toolu_01Fy9WyVNoEg25rWz3iY4RxQ`</summary>

```text
Based on the content provided, SpecPrune-VLA was submitted to **ICLR 2026 Conference**. 

However, the page does not indicate whether it was accepted. The submission shows a date of "16 Sept 2025 (modified: 11 Feb 2026)" and lists it as "Submitted to ICLR 2026," but there is no acceptance status mentioned on this OpenReview page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "5fc7b939-7363-4a55-9527-d09f17b25843",
  "tool_use_result": {
    "bytes": 71619,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the content provided, SpecPrune-VLA was submitted to **ICLR 2026 Conference**. \n\nHowever, the page does not indicate whether it was accepted. The submission shows a date of \"16 Sept 2025 (modified: 11 Feb 2026)\" and lists it as \"Submitted to ICLR 2026,\" but there is no acceptance status mentioned on this OpenReview page.",
    "durationMs": 2622,
    "url": "https://openreview.net/forum?id=t85Ni0LwjC"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-19T01:34:31.895Z_

<details><summary>↩ Tool result · `toolu_01FQwyLiyzmKX2zinbqMua6w`</summary>

```text
Web search results for query: ""See What Matters" Yixu Feng GridS VLA arXiv"

Links: [{"title":"3D printed cell culture grid holders for improved cellular specimen preparation in cryo-electron microscopy","url":"https://www.biorxiv.org/content/10.1101/2020.06.12.147678.full.pdf"},{"title":"GRIDSS: sensitive and specific genomic rearrangement detection using positional de Bruijn graph assembly","url":"https://www.biorxiv.org/content/10.1101/110387.full.pdf"},{"title":"[2503.07511] PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/abs/2503.07511"},{"title":"Lattice Radiation Therapy with Alternating Dosimetric Peaks and Valleys","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344368.full.pdf"},{"title":"Patch Based Grid Artifact Suppressing in Digital Mammography","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6109478/"},{"title":"On the Orientation of Entorhinal Grids","url":"https://www.biorxiv.org/content/10.1101/349373.full.pdf"},{"title":"GRIDSS2: comprehensive characterisation of somatic structural variation using single breakend variants and structural variant phasing","url":"https://www.biorxiv.org/content/10.1101/2020.07.09.196527.full.pdf"},{"title":"Robust variability of grid cell properties within individual grid modules enhances encoding of local space","url":"https://www.biorxiv.org/content/10.1101/2024.02.27.582373.full.pdf"}]

The search results don't contain information about the specific paper you're looking for titled "See What Matters" by Yixu Feng related to GridS and VLA on arXiv. The results returned are for unrelated topics like grid cells in neuroscience, genomic analysis tools, and medical imaging.

Let me try a more targeted search:

Links: [{"title":"3D printed cell culture grid holders for improved cellular specimen preparation in cryo-electron microscopy","url":"https://www.biorxiv.org/content/10.1101/2020.06.12.147678.full.pdf"},{"title":"Patch Based Grid Artifact Suppressing in Digital Mammography","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6109478/"},{"title":"[2503.07511] PointVLA: Injecting the 3D World into Vision-Language-Action Models","url":"https://arxiv.org/abs/2503.07511"},{"title":"Modeling the Effect of Environmental Geometries on Grid Cell Representations","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6339930/"},{"title":"GRIDSS: sensitive and specific genomic rearrangement detection using positional de Bruijn graph assembly","url":"https://www.biorxiv.org/content/10.1101/110387.full.pdf"},{"title":"[2604.09059] Learning Vision-Language-Action World Models for Autonomous Driving","url":"https://arxiv.org/abs/2604.09059"},{"title":"Lattice Radiation Therapy with Alternating Dosimetric Peaks and Valleys","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344368.full.pdf"},{"title":"A Plane-Dependent Model of 3D Grid Cells for Representing Both 2D and 3D Spaces Under Various Navigation Modes","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8493087/"}]

Unfortunately, the search results still don't contain the specific paper you're looking for. Let me try another search approach:

Links: [{"title":"[2509.23655] Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models","url":"https://arxiv.org/abs/2509.23655"},{"title":"[2412.14058] What Matters in Building Vision-Language-Action Models for Generalist Robots","url":"https://arxiv.org/abs/2412.14058"},{"title":"What matters in building vision–language–action models for generalist robots | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01168-7"},{"title":"Vision-Language-Action, explained with a minimum of math and jargon","url":"https://roboticsfyi.substack.com/p/vision-language-action-explained"},{"title":"Vision–Language–Action Models: What Actually Matters for Generalist Robots | by Amjad Y Majid | Medium","url":"https://medium.com/@amjad.y.majid/vision-language-action-models-what-actually-matters-for-generalist-robots-0e67388a060d"},{"title":"Vision-Language-Action Models: Types & VLA+","url":"https://www.turingpost.com/p/vlaplus"},{"title":"What are Vision Language Action (VLA) Models? Complete Guide","url":"https://www.articsledge.com/post/vision-language-action-vla-models"},{"title":"What matters in building vision–language–action models ...","url":"https://www.researchgate.net/publication/400683320_What_matters_in_building_vision-language-action_models_for_generalist_robots"},{"title":"Vision-Language-Action Models: How Foundation Models Are Transforming Autonomy - Digitaldividedata.com","url":"https://www.digitaldividedata.com/blog/vision-language-action-models-autonomy"},{"title":"Vision language Action (VLA) Models | by chidubem ndukwe | Mar, 2026 | Medium","url":"https://medium.com/@chidubemndukwe/vision-language-action-vla-models-91795fa227c6"}]

I haven't found the specific paper "See What Matters" by Yixu Feng with GridS and VLA on arXiv yet. Let me try one more search with a different approach:

Links: [{"title":"SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference","url":"https://arxiv.org/html/2502.18137v4"},{"title":"Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models","url":"https://www.researchgate.net/publication/398026272_Attention-Guided_Patch-Wise_Sparse_Adversarial_Attacks_on_Vision-Language-Action_Models"},{"title":"Determinantal point process attention over grid cell code supports out of distribution generalization","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11293867/"},{"title":"SpargeAttention2: Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning","url":"https://arxiv.org/pdf/2602.13515"},{"title":"Routing Absorption in Sparse Attention: Why Random Gates Are Hard to Beat","url":"https://arxiv.org/pdf/2603.02227"},{"title":"Sparse Attention","url":"https://www.aussieai.com/research/sparse-attention"},{"title":"Introduction to Native Sparse Attention | by Satish Kumar | Medium","url":"https://medium.com/@satish.salyal/introduction-to-native-sparse-attention-15e947380c2b"},{"title":"Attention neural networks with sparse attention mechanisms","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11238332"}]

I apologize, but I'm unable to locate the specific paper you're searching for titled "See What Matters" by Yixu Feng involving GridS and VLA on arXiv through my searches. The search results are returning related papers about Vision-Language-Action models, sparse attention mechanisms, and grid cells, but not the specific paper you mentioned.

It's possible that:
1. The paper title might be slightly different
2. The author name spelling might be different
3. It may be a very recent paper that hasn't been fully indexed yet
4. It could be on a preprint server other than arXiv

I'd recommend:
- Searching directly on arXiv.org using these keywords
- Checking the author's profile on arXiv if you have more details about them
- Trying alternative spellings or variations of the title
- Checking if there's a different preprint server where it might be hosted

Would you like to provide any additional information about the paper that might help me locate it?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "f28e08b5-2efc-49bc-8dfa-449e890a239b",
  "tool_use_result": {
    "query": "\"See What Matters\" Yixu Feng GridS VLA arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FMksFYcWr995NRSAcRQpXp",
        "content": [
          {
            "title": "3D printed cell culture grid holders for improved cellular specimen preparation in cryo-electron microscopy",
            "url": "https://www.biorxiv.org/content/10.1101/2020.06.12.147678.full.pdf"
          },
          {
            "title": "GRIDSS: sensitive and specific genomic rearrangement detection using positional de Bruijn graph assembly",
            "url": "https://www.biorxiv.org/content/10.1101/110387.full.pdf"
          },
          {
            "title": "[2503.07511] PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2503.07511"
          },
          {
            "title": "Lattice Radiation Therapy with Alternating Dosimetric Peaks and Valleys",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344368.full.pdf"
          },
          {
            "title": "Patch Based Grid Artifact Suppressing in Digital Mammography",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6109478/"
          },
          {
            "title": "On the Orientation of Entorhinal Grids",
            "url": "https://www.biorxiv.org/content/10.1101/349373.full.pdf"
          },
          {
            "title": "GRIDSS2: comprehensive characterisation of somatic structural variation using single breakend variants and structural variant phasing",
            "url": "https://www.biorxiv.org/content/10.1101/2020.07.09.196527.full.pdf"
          },
          {
            "title": "Robust variability of grid cell properties within individual grid modules enhances encoding of local space",
            "url": "https://www.biorxiv.org/content/10.1101/2024.02.27.582373.full.pdf"
          }
        ]
      },
      "The search results don't contain information about the specific paper you're looking for titled \"See What Matters\" by Yixu Feng related to GridS and VLA on arXiv. The results returned are for unrelated topics like grid cells in neuroscience, genomic analysis tools, and medical imaging.\n\nLet me try a more targeted search:",
      {
        "tool_use_id": "srvtoolu_01GKZJrxP8mwCXZxCiGsuK1x",
        "content": [
          {
            "title": "3D printed cell culture grid holders for improved cellular specimen preparation in cryo-electron microscopy",
            "url": "https://www.biorxiv.org/content/10.1101/2020.06.12.147678.full.pdf"
          },
          {
            "title": "Patch Based Grid Artifact Suppressing in Digital Mammography",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6109478/"
          },
          {
            "title": "[2503.07511] PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2503.07511"
          },
          {
            "title": "Modeling the Effect of Environmental Geometries on Grid Cell Representations",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6339930/"
          },
          {
            "title": "GRIDSS: sensitive and specific genomic rearrangement detection using positional de Bruijn graph assembly",
            "url": "https://www.biorxiv.org/content/10.1101/110387.full.pdf"
          },
          {
            "title": "[2604.09059] Learning Vision-Language-Action World Models for Autonomous Driving",
            "url": "https://arxiv.org/abs/2604.09059"
          },
          {
            "title": "Lattice Radiation Therapy with Alternating Dosimetric Peaks and Valleys",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344368.full.pdf"
          },
          {
            "title": "A Plane-Dependent Model of 3D Grid Cells for Representing Both 2D and 3D Spaces Under Various Navigation Modes",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8493087/"
          }
        ]
      },
      "Unfortunately, the search results still don't contain the specific paper you're looking for. Let me try another search approach:",
      {
        "tool_use_id": "srvtoolu_01C5uNKPWrsN7s8CXczNqaYg",
        "content": [
          {
            "title": "[2509.23655] Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models",
            "url": "https://arxiv.org/abs/2509.23655"
          },
          {
            "title": "[2412.14058] What Matters in Building Vision-Language-Action Models for Generalist Robots",
            "url": "https://arxiv.org/abs/2412.14058"
          },
          {
            "title": "What matters in building vision–language–action models for generalist robots | Nature Machine Intelligence",
            "url": "https://www.nature.com/articles/s42256-025-01168-7"
          },
          {
            "title": "Vision-Language-Action, explained with a minimum of math and jargon",
            "url": "https://roboticsfyi.substack.com/p/vision-language-action-explained"
          },
          {
            "title": "Vision–Language–Action Models: What Actually Matters for Generalist Robots | by Amjad Y Majid | Medium",
            "url": "https://medium.com/@amjad.y.majid/vision-language-action-models-what-actually-matters-for-generalist-robots-0e67388a060d"
          },
          {
            "title": "Vision-Language-Action Models: Types & VLA+",
            "url": "https://www.turingpost.com/p/vlaplus"
          },
          {
            "title": "What are Vision Language Action (VLA) Models? Complete Guide",
            "url": "https://www.articsledge.com/post/vision-language-action-vla-models"
          },
          {
            "title": "What matters in building vision–language–action models ...",
            "url": "https://www.researchgate.net/publication/400683320_What_matters_in_building_vision-language-action_models_for_generalist_robots"
          },
          {
            "title": "Vision-Language-Action Models: How Foundation Models Are Transforming Autonomy - Digitaldividedata.com",
            "url": "https://www.digitaldividedata.com/blog/vision-language-action-models-autonomy"
          },
          {
            "title": "Vision language Action (VLA) Models | by chidubem ndukwe | Mar, 2026 | Medium",
            "url": "https://medium.com/@chidubemndukwe/vision-language-action-vla-models-91795fa227c6"
          }
        ]
      },
      "I haven't found the specific paper \"See What Matters\" by Yixu Feng with GridS and VLA on arXiv yet. Let me try one more search with a different approach:",
      {
        "tool_use_id": "srvtoolu_01WakuNHTgxBo6pLgkZV9CPW",
        "content": [
          {
            "title": "SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference",
            "url": "https://arxiv.org/html/2502.18137v4"
          },
          {
            "title": "Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/398026272_Attention-Guided_Patch-Wise_Sparse_Adversarial_Attacks_on_Vision-Language-Action_Models"
          },
          {
            "title": "Determinantal point process attention over grid cell code supports out of distribution generalization",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11293867/"
          },
          {
            "title": "SpargeAttention2: Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning",
            "url": "https://arxiv.org/pdf/2602.13515"
          },
          {
            "title": "Routing Absorption in Sparse Attention: Why Random Gates Are Hard to Beat",
            "url": "https://arxiv.org/pdf/2603.02227"
          },
          {
            "title": "Sparse Attention",
            "url": "https://www.aussieai.com/research/sparse-attention"
          },
          {
            "title": "Introduction to Native Sparse Attention | by Satish Kumar | Medium",
            "url": "https://medium.com/@satish.salyal/introduction-to-native-sparse-attention-15e947380c2b"
          },
          {
            "title": "Attention neural networks with sparse attention mechanisms",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11238332"
          }
        ]
      },
      "I apologize, but I'm unable to locate the specific paper you're searching for titled \"See What Matters\" by Yixu Feng involving GridS and VLA on arXiv through my searches. The search results are returning related papers about Vision-Language-Action models, sparse attention mechanisms, and grid cells, but not the specific paper you mentioned.\n\nIt's possible that:\n1. The paper title might be slightly different\n2. The author name spelling might be different\n3. It may be a very recent paper that hasn't been fully indexed yet\n4. It could be on a preprint server other than arXiv\n\nI'd recommend:\n- Searching directly on arXiv.org using these keywords\n- Checking the author's profile on arXiv if you have more details about them\n- Trying alternative spellings or variations of the title\n- Checking if there's a different preprint server where it might be hosted\n\nWould you like to provide any additional information about the paper that might help me locate it?"
    ],
    "durationSeconds": 12.844685962000003
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the arXiv link for "See What Matters" paper. It seems to be at ICML 2026, but I couldn't find its arXiv link. Let me try one more search.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "eec13634-da7f-4d40-b090-115612b220d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tin9ewWTS1ry4hYi4dcw7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 129,
      "cache_creation_input_tokens": 2428,
      "cache_read_input_tokens": 33353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2428
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

_source line 45_

搜索第 4 篇的 arXiv 链接。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "91fdcb0d-c670-4979-9680-a4a58eb533bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tin9ewWTS1ry4hYi4dcw7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 129,
      "cache_creation_input_tokens": 2428,
      "cache_read_input_tokens": 33353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2428
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

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015rbmrwcGhhJUURpkcitGbm`</summary>

```json
{
  "query": "arxiv \"See What Matters\" \"Differentiable Grid Sample\" \"Vision-Language-Action\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "536201c4-3f50-4f88-a7f0-94091b275834",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tin9ewWTS1ry4hYi4dcw7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 129,
      "cache_creation_input_tokens": 2428,
      "cache_read_input_tokens": 33353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2428
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

_source line 47_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TXsnAHK1TrGPLMf7vX6Psp`</summary>

```json
{
  "query": "Yixu Feng Chang Xu VLA grid sample pruning arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "4627575c-10c9-47bd-8da2-6644c6c5b76b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tin9ewWTS1ry4hYi4dcw7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 129,
      "cache_creation_input_tokens": 2428,
      "cache_read_input_tokens": 33353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2428
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

_source line 48 · 2026-05-19T01:34:41.610Z_

<details><summary>↩ Tool result · `toolu_01TXsnAHK1TrGPLMf7vX6Psp`</summary>

```text
Web search results for query: "Yixu Feng Chang Xu VLA grid sample pruning arxiv 2025 2026"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/pdf/2510.08464"},{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/html/2509.22093v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/pdf/2509.05614"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.22991"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/pdf/2506.12723"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"}]

Based on the search results, I found a relevant paper that appears to match your query. The first result references a Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA. This appears to be from an ICML 2026 poster presentation titled "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model."

The search returned several related papers on VLA model pruning and acceleration from 2025-2026, but the specific paper you're asking about appears to be the ICML paper with the GridS method. The results indicate this was posted recently (about 2 weeks ago based on the metadata).

Would you like me to search for more specific information about this paper or the authors you mentioned?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "6fab6b45-acdf-4bb6-b2b9-2060047a3e6c",
  "tool_use_result": {
    "query": "Yixu Feng Chang Xu VLA grid sample pruning arxiv 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KSYTi9YzH388YNyzoVTCim",
        "content": [
          {
            "title": "ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model",
            "url": "https://icml.cc/virtual/2026/poster/65010"
          },
          {
            "title": "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered",
            "url": "https://arxiv.org/pdf/2510.08464"
          },
          {
            "title": "Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation",
            "url": "https://arxiv.org/html/2509.22093v1"
          },
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning",
            "url": "https://arxiv.org/pdf/2509.05614"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/pdf/2509.12594"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.22991"
          },
          {
            "title": "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration",
            "url": "https://arxiv.org/pdf/2506.12723"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/pdf/2511.16449"
          }
        ]
      },
      "Based on the search results, I found a relevant paper that appears to match your query. The first result references a Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA. This appears to be from an ICML 2026 poster presentation titled \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model.\"\n\nThe search returned several related papers on VLA model pruning and acceleration from 2025-2026, but the specific paper you're asking about appears to be the ICML paper with the GridS method. The results indicate this was posted recently (about 2 weeks ago based on the metadata).\n\nWould you like me to search for more specific information about this paper or the authors you mentioned?"
    ],
    "durationSeconds": 5.026062055000002
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T01:34:43.469Z_

<details><summary>↩ Tool result · `toolu_015rbmrwcGhhJUURpkcitGbm`</summary>

```text
Web search results for query: "arxiv "See What Matters" "Differentiable Grid Sample" "Vision-Language-Action""

Links: [{"title":"From Spatial to Actions: Grounding Vision-Language- Action Model in Spatial Foundation Priors","url":"https://arxiv.org/html/2510.17439v2"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/pdf/2505.04769"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.19233"},{"title":"[2412.14058] What Matters in Building Vision-Language-Action Models for Generalist Robots","url":"https://arxiv.org/abs/2412.14058"},{"title":"Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model","url":"https://arxiv.org/pdf/2510.27607"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.15618"},{"title":"DiffVLA: Vision-Language Guided Diffusion Planning for Autonomous Driving","url":"https://arxiv.org/html/2505.19381"},{"title":"GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics","url":"https://arxiv.org/pdf/2506.14009"}]

Based on the search results, I found several papers related to Vision-Language-Action (VLA) models, though the specific exact phrase match for "See What Matters" with "Differentiable Grid Sample" wasn't prominently featured in these particular results.

The closest match appears to be a paper that discloses key factors influencing VLA performance on robot manipulation and develops a new family of VLAs called RoboVLMs, which require very few manual designs and achieve state-of-the-art performance.

Other relevant papers in the search results include:

1. A study on Vision-Language-Action models that combine visual encoders, language backbones, and action decoders into end-to-end policies that generalize across objects and instructions

2. DeepVision-VLA, built on a Vision-Language Mixture-of-Transformers framework that enables shared attention between vision and VLA backbones, injecting multi-level visual features into deeper layers

3. GRaD-Nav++, a lightweight Vision-Language-Action framework trained via Differentiable Reinforcement Learning in a 3D Gaussian Splatting simulator

If you're looking for a specific paper with those exact phrases, you may want to try searching arXiv directly or providing additional context about the paper's topic or authors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "67b8a4ae-f4f5-49ef-94a1-1c0978f8391b",
  "tool_use_result": {
    "query": "arxiv \"See What Matters\" \"Differentiable Grid Sample\" \"Vision-Language-Action\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QKYb8X1DxPxGXgyWGn4J25",
        "content": [
          {
            "title": "From Spatial to Actions: Grounding Vision-Language- Action Model in Spatial Foundation Priors",
            "url": "https://arxiv.org/html/2510.17439v2"
          },
          {
            "title": "Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/pdf/2505.04769"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.19233"
          },
          {
            "title": "[2412.14058] What Matters in Building Vision-Language-Action Models for Generalist Robots",
            "url": "https://arxiv.org/abs/2412.14058"
          },
          {
            "title": "Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model",
            "url": "https://arxiv.org/pdf/2510.27607"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.15618"
          },
          {
            "title": "DiffVLA: Vision-Language Guided Diffusion Planning for Autonomous Driving",
            "url": "https://arxiv.org/html/2505.19381"
          },
          {
            "title": "GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics",
            "url": "https://arxiv.org/pdf/2506.14009"
          }
        ]
      },
      "Based on the search results, I found several papers related to Vision-Language-Action (VLA) models, though the specific exact phrase match for \"See What Matters\" with \"Differentiable Grid Sample\" wasn't prominently featured in these particular results.\n\nThe closest match appears to be a paper that discloses key factors influencing VLA performance on robot manipulation and develops a new family of VLAs called RoboVLMs, which require very few manual designs and achieve state-of-the-art performance.\n\nOther relevant papers in the search results include:\n\n1. A study on Vision-Language-Action models that combine visual encoders, language backbones, and action decoders into end-to-end policies that generalize across objects and instructions\n\n2. DeepVision-VLA, built on a Vision-Language Mixture-of-Transformers framework that enables shared attention between vision and VLA backbones, injecting multi-level visual features into deeper layers\n\n3. GRaD-Nav++, a lightweight Vision-Language-Action framework trained via Differentiable Reinforcement Learning in a 3D Gaussian Splatting simulator\n\nIf you're looking for a specific paper with those exact phrases, you may want to try searching arXiv directly or providing additional context about the paper's topic or authors."
    ],
    "durationSeconds": 7.245144373999996
  }
}
```

</details>

---

### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
The "See What Matters" paper seems to only appear on the ICML 2026 virtual site and doesn't seem to have a visible arXiv preprint. Let me try one more search to find if it has an arXiv ID.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "086aeb0c-d06d-4752-be29-ff08982e1c8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gsmrhgGEeHkE627fsBYsR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 657,
      "cache_creation_input_tokens": 1167,
      "cache_read_input_tokens": 35781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1167
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

_source line 51_

尝试通过 OpenReview 查找第 4 篇。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "4851743f-54f1-4a30-99ba-fc4aeb24ed4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gsmrhgGEeHkE627fsBYsR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 657,
      "cache_creation_input_tokens": 1167,
      "cache_read_input_tokens": 35781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1167
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

_source line 52_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012qZUojXLKr7rbxiKZnqkAe`</summary>

```json
{
  "query": "openreview \"See What Matters\" \"Grid Sample Pruning\" ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "02387cb1-276a-4a21-a288-45f3842181a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gsmrhgGEeHkE627fsBYsR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 657,
      "cache_creation_input_tokens": 1167,
      "cache_read_input_tokens": 35781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1167
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

_source line 53 · 2026-05-19T01:34:55.583Z_

<details><summary>↩ Tool result · `toolu_012qZUojXLKr7rbxiKZnqkAe`</summary>

```text
Web search results for query: "openreview "See What Matters" "Grid Sample Pruning" ICML 2026"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"OpenReviewer: A Specialized Large Language Model for Generating Critical   Scientific Paper Reviews","url":"https://arxiv.org/pdf/2412.11948"},{"title":"OpenReview Should be Protected and Leveraged as a Community Asset for Research in the Era of Large Language Models","url":"https://arxiv.org/pdf/2505.21537"},{"title":"GridPrune: From \"Where to Look\" to \"What to Select\" in Visual Token Pruning for MLLMs","url":"https://arxiv.org/pdf/2511.10081"},{"title":"Not All Data Matters: An End-to-End Adaptive Dataset Pruning Framework   for Enhancing Model Performance and Efficiency","url":"https://arxiv.org/pdf/2312.05599"},{"title":"Dataset Pruning: Reducing Training Data by Examining Generalization   Influence","url":"https://arxiv.org/pdf/2205.09329"}]

Based on the search results, I found a relevant paper at ICML 2026:

There is an ICML 2026 poster titled "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model" that addresses the fundamental trade-off in token pruning methods, where aggressive compression inevitably discards critical geometric details like contact points, leading to severe performance degradation.

The paper appears to be presented as a poster at ICML 2026 (available at https://icml.cc/virtual/2026/poster/65010). However, the search results do not contain the full paper details from OpenReview. If you're looking for more specific information about the paper (such as the authors, abstract, or a link to the OpenReview submission), you may want to visit the ICML 2026 website directly or search OpenReview.net for the paper title.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "b7f32dbf-2e7b-4040-928f-6f59e3c9979c",
  "tool_use_result": {
    "query": "openreview \"See What Matters\" \"Grid Sample Pruning\" ICML 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PuRXTBdwxtzSDcMfa3wofD",
        "content": [
          {
            "title": "ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model",
            "url": "https://icml.cc/virtual/2026/poster/65010"
          },
          {
            "title": "OpenReviewer: A Specialized Large Language Model for Generating Critical   Scientific Paper Reviews",
            "url": "https://arxiv.org/pdf/2412.11948"
          },
          {
            "title": "OpenReview Should be Protected and Leveraged as a Community Asset for Research in the Era of Large Language Models",
            "url": "https://arxiv.org/pdf/2505.21537"
          },
          {
            "title": "GridPrune: From \"Where to Look\" to \"What to Select\" in Visual Token Pruning for MLLMs",
            "url": "https://arxiv.org/pdf/2511.10081"
          },
          {
            "title": "Not All Data Matters: An End-to-End Adaptive Dataset Pruning Framework   for Enhancing Model Performance and Efficiency",
            "url": "https://arxiv.org/pdf/2312.05599"
          },
          {
            "title": "Dataset Pruning: Reducing Training Data by Examining Generalization   Influence",
            "url": "https://arxiv.org/pdf/2205.09329"
          }
        ]
      },
      "Based on the search results, I found a relevant paper at ICML 2026:\n\nThere is an ICML 2026 poster titled \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\" that addresses the fundamental trade-off in token pruning methods, where aggressive compression inevitably discards critical geometric details like contact points, leading to severe performance degradation.\n\nThe paper appears to be presented as a poster at ICML 2026 (available at https://icml.cc/virtual/2026/poster/65010). However, the search results do not contain the full paper details from OpenReview. If you're looking for more specific information about the paper (such as the authors, abstract, or a link to the OpenReview submission), you may want to visit the ICML 2026 website directly or search OpenReview.net for the paper title."
    ],
    "durationSeconds": 8.236971638999997
  }
}
```

</details>

---

### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
I have enough information now. Let me also check SpecPrune-VLA's venue status. It was submitted to ICLR 2026 on OpenReview. Let me compile the results.

Let me summarize what I found:

1. **Compressor-VLA (arXiv 2511.18950)** - ✅ Confirmed. arXiv Nov 24, 2025. Cross-attention style compression (STC + SRC). LIBERO benchmark, 59% FLOPs reduction. Reviewer said 97.1% SR - I don't have the exact SR from the abstract, it says "competitive". The reviewer's claim about cross-attention seems roughly accurate.


2. **SpecPrune-VLA (arXiv 2509.05614)** - ✅ Confirmed. arXiv Sep 6, 2025. Uses action-aware self-speculative pruning to achieve up to 1.57x speedup on LIBERO and 1.70x on real robot tasks. Submitted to ICLR 2026. The reviewer's characterization of the method is accurate.
3. **LightVLA (arXiv 2509.12594)** - ✅ Confirmed. arXiv Sep 16, 2025, accepted to ICRA 2026. Employs differentiable token pruning on LIBERO, reducing FLOPs by 59.1% while improving success rate by 2.6%.
4. **"See What Matters" (ICML 2026)** - ✅ Confirmed. ICML 2026 poster using a Differentiable Grid Sampler for grid-based VLA compression, achieving 76% FLOPs reduction with less than 10% visual tokens on LIBERO and real robot tasks. All four papers check out as legitimate publications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "79c4674e-8a23-4615-9502-9cf06f718548",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdBTx91k1XZU7Z9rf6Ts46",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 36948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1363
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

_source line 55_

全部 4 篇论文验证完毕。

---

## 论文 1: Compressor-VLA
- **状态**: ✅ 确认存在
- **arXiv ID**: [2511.18950](https://arxiv.org/abs/2511.18950)
- **真实标题**: Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation
- **作者**: Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian (北京工业大学 & LiAuto)
- **Venue/日期**: arXiv 2025-11-24 (无会议录用信息)
- **核心方法**: 提出 Semantic Task Compressor (STC) + Spatial Refinement Compressor (SRC) 双模块框架，由自然语言指令动态调制 visual token 压缩。在 LIBERO 上实现 59% FLOPs 削减、3x+ token 数量压缩，同时保持 competitive success rate。
- **与我们的关系**: 直接竞争 (instruction-guided VLA token compression on LIBERO)
- **Reviewer 描述准确性**: 部分准确。cross-attention 描述大致对应其 STC 模块机制，但 97.1% SR 在 abstract 中未明确提及（仅称 "competitive"），需查论文表格确认。

---

## 论文 2: SpecPrune-VLA
- **状态**: ✅ 确认存在
- **arXiv ID**: [2509.05614](https://arxiv.org/abs/2509.05614)
- **真实标题**: SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning
- **作者**: Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, Guohao Dai
- **Venue/日期**: arXiv 2025-09-06 (revised 2026-02-09)；submitted to ICLR 2026 ([OpenReview](https://openreview.net/forum?id=t85Ni0LwjC))，录用状态未确认
- **核心方法**: Training-free 两级剪枝：action-level static pruning (全局历史+局部 attention) + layer-level dynamic pruning (逐层重要性)。Lightweight action-aware controller 根据末端执行器速度区分粗/细粒度动作，细粒度动作降低剪枝力度。LIBERO 上 1.57x 加速，real robot 1.70x 加速，success rate 几乎无损。
- **与我们的关系**: 直接竞争 (action-aware VLA token pruning, LIBERO + real robot)
- **Reviewer 描述准确性**: 准确

---

## 论文 3: LightVLA
- **状态**: ✅ 确认存在
- **arXiv ID**: [2509.12594](https://arxiv.org/abs/2509.12594)
- **真实标题**: The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning
- **作者**: Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang (LiAuto)
- **Venue/日期**: arXiv 2025-09-16；**ICRA 2026 accepted**（[GitHub](https://github.com/LiAutoAD/LightVLA) 确认）
- **核心方法**: 可微分 token 剪枝框架，用动态 query 评估 visual token 重要性，Gumbel softmax 实现可微分 token 选择。无额外可训练参数，兼容现代推理框架。LIBERO 上 59.1% FLOPs 削减、38.2% latency 削减，success rate 提升 2.6%。
- **与我们的关系**: 直接竞争 (differentiable VLA token pruning on LIBERO)
- **Reviewer 描述准确性**: 准确（arXiv ID、ICRA 2026、differentiable pruning 均吻合）

---

## 论文 4: "See What Matters"
- **状态**: ✅ 确认存在
- **arXiv ID**: 未找到 arXiv 预印本（可能仅通过会议提交）
- **真实标题**: See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model
- **作者**: Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu
- **Venue/日期**: **[ICML 2026 poster](https://icml.cc/virtual/2026/poster/65010)**
- **核心方法**: 提出 Differentiable Grid Sampler (GridS)，一个即插即用模块，将 token pruning 重新定义为连续 geometry-aware resampling 问题。自适应预测少量关键坐标，通过可微分插值提取特征，仅使用 <10% 的原始 visual tokens 即可实现 76% FLOPs 削减且 success rate 无损。号称目前报告的最低可行 visual token 数量。
- **与我们的关系**: 直接竞争 (grid-based VLA token compression on LIBERO + real robot)
- **Reviewer 描述准确性**: 准确（ICML 2026、grid-based compression 均吻合）

---

## 总结

| 论文 | 存在性 | Reviewer 描述 | arXiv ID |
|------|--------|--------------|----------|
| Compressor-VLA | ✅ 真实 | 部分准确 (97.1% SR 待确认) | 2511.18950 ✅ |
| SpecPrune-VLA | ✅ 真实 | 准确 | 2509.05614 ✅ |
| LightVLA | ✅ 真实 | 准确 | 2509.12594 ✅ |
| See What Matters | ✅ 真实 | 准确 | 无 arXiv (ICML 2026 直接提交) |

**4 篇论文全部真实存在，reviewer 未出现幻觉。** 这 4 篇都是 VLA visual token compression/pruning 的直接竞争工作，均在 LIBERO 上评测。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "uuid": "0d6792c5-afc3-4f81-b0d3-b502a725d73e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdBTx91k1XZU7Z9rf6Ts46",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 36948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1363
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

_source line 56_

全部 4 篇论文验证完毕。

---

## 论文 1: Compressor-VLA
- **状态**: ✅ 确认存在
- **arXiv ID**: [2511.18950](https://arxiv.org/abs/2511.18950)
- **真实标题**: Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation
- **作者**: Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian (北京工业大学 & LiAuto)
- **Venue/日期**: arXiv 2025-11-24 (无会议录用信息)
- **核心方法**: 提出 Semantic Task Compressor (STC) + Spatial Refinement Compressor (SRC) 双模块框架，由自然语言指令动态调制 visual token 压缩。在 LIBERO 上实现 59% FLOPs 削减、3x+ token 数量压缩，同时保持 competitive success rate。
- **与我们的关系**: 直接竞争 (instruction-guided VLA token compression on LIBERO)
- **Reviewer 描述准确性**: 部分准确。cross-attention 描述大致对应其 STC 模块机制，但 97.1% SR 在 abstract 中未明确提及（仅称 "competitive"），需查论文表格确认。

---

## 论文 2: SpecPrune-VLA
- **状态**: ✅ 确认存在
- **arXiv ID**: [2509.05614](https://arxiv.org/abs/2509.05614)
- **真实标题**: SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning
- **作者**: Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, Guohao Dai
- **Venue/日期**: arXiv 2025-09-06 (revised 2026-02-09)；submitted to ICLR 2026 ([OpenReview](https://openreview.net/forum?id=t85Ni0LwjC))，录用状态未确认
- **核心方法**: Training-free 两级剪枝：action-level static pruning (全局历史+局部 attention) + layer-level dynamic pruning (逐层重要性)。Lightweight action-aware controller 根据末端执行器速度区分粗/细粒度动作，细粒度动作降低剪枝力度。LIBERO 上 1.57x 加速，real robot 1.70x 加速，success rate 几乎无损。
- **与我们的关系**: 直接竞争 (action-aware VLA token pruning, LIBERO + real robot)
- **Reviewer 描述准确性**: 准确

---

## 论文 3: LightVLA
- **状态**: ✅ 确认存在
- **arXiv ID**: [2509.12594](https://arxiv.org/abs/2509.12594)
- **真实标题**: The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning
- **作者**: Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang (LiAuto)
- **Venue/日期**: arXiv 2025-09-16；**ICRA 2026 accepted**（[GitHub](https://github.com/LiAutoAD/LightVLA) 确认）
- **核心方法**: 可微分 token 剪枝框架，用动态 query 评估 visual token 重要性，Gumbel softmax 实现可微分 token 选择。无额外可训练参数，兼容现代推理框架。LIBERO 上 59.1% FLOPs 削减、38.2% latency 削减，success rate 提升 2.6%。
- **与我们的关系**: 直接竞争 (differentiable VLA token pruning on LIBERO)
- **Reviewer 描述准确性**: 准确（arXiv ID、ICRA 2026、differentiable pruning 均吻合）

---

## 论文 4: "See What Matters"
- **状态**: ✅ 确认存在
- **arXiv ID**: 未找到 arXiv 预印本（可能仅通过会议提交）
- **真实标题**: See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model
- **作者**: Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu
- **Venue/日期**: **[ICML 2026 poster](https://icml.cc/virtual/2026/poster/65010)**
- **核心方法**: 提出 Differentiable Grid Sampler (GridS)，一个即插即用模块，将 token pruning 重新定义为连续 geometry-aware resampling 问题。自适应预测少量关键坐标，通过可微分插值提取特征，仅使用 <10% 的原始 visual tokens 即可实现 76% FLOPs 削减且 success rate 无损。号称目前报告的最低可行 visual token 数量。
- **与我们的关系**: 直接竞争 (grid-based VLA token compression on LIBERO + real robot)
- **Reviewer 描述准确性**: 准确（ICML 2026、grid-based compression 均吻合）

---

## 总结

| 论文 | 存在性 | Reviewer 描述 | arXiv ID |
|------|--------|--------------|----------|
| Compressor-VLA | ✅ 真实 | 部分准确 (97.1% SR 待确认) | 2511.18950 ✅ |
| SpecPrune-VLA | ✅ 真实 | 准确 | 2509.05614 ✅ |
| LightVLA | ✅ 真实 | 准确 | 2509.12594 ✅ |
| See What Matters | ✅ 真实 | 准确 | 无 arXiv (ICML 2026 直接提交) |

**4 篇论文全部真实存在，reviewer 未出现幻觉。** 这 4 篇都是 VLA visual token compression/pruning 的直接竞争工作，均在 LIBERO 上评测。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 131562,
  "duration_api_ms": 190147,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "345976c8-c1e5-4cd6-a8a0-3077adeacd55",
  "total_cost_usd": 0.7471675000000001,
  "usage": {
    "input_tokens": 1328,
    "cache_creation_input_tokens": 26470,
    "cache_read_input_tokens": 228670,
    "output_tokens": 4285,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26470,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2399,
        "cache_read_input_tokens": 36948,
        "cache_creation_input_tokens": 1363,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1363
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 183145,
      "outputTokens": 6097,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 14,
      "costUSD": 0.35363,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1328,
      "outputTokens": 4285,
      "cacheReadInputTokens": 228670,
      "cacheCreationInputTokens": 26470,
      "webSearchRequests": 0,
      "costUSD": 0.39353749999999993,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9ef4e946-0686-4bd5-914b-e25b86c07713"
}
```

</details>

---
