# research citation verification

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_research_citation_verification_20260516T042149.log`
- **Structured JSON:** [`67fc7b90c369de6d45e1.json`](../../sessions/67/67fc7b90c369de6d45e1.json)

## Before a recorded user message

25 recorded events

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
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
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
  "uuid": "56ca7037-cc64-4fea-8f57-a5992af88105",
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
    "resetsAt": 1778922000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1b577937-98e2-4b39-aed1-9c40e89ca816",
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
I need to verify 3 citations using WebSearch. Let me load the WebSearch tool first, then search for each citation in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "1fa459a3-2805-44cd-a6a3-1c4be0857a64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvPndJLh23bXGbvw6rt9pX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11652,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11652
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012y2KazaVhxh6beM3TDgYvM`</summary>

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
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "33826094-9349-4cda-aa51-c68b4f02964c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvPndJLh23bXGbvw6rt9pX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11652,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11652
      },
      "output_tokens": 25,
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

_source line 6 · 2026-05-16T04:22:01.744Z_

<details><summary>↩ Tool result · `toolu_012y2KazaVhxh6beM3TDgYvM`</summary>

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
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "723c1053-9c08-4478-8dd2-e426551bf452",
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
Now let me search for all three citations in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "999e8b77-e09e-4961-8da1-8bc38cfb03ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01576xdGtMT2T8fabwEJtvSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 23493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 30,
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

开始并行搜索三个引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "53468099-46f5-42c9-a61b-4ee7b21835ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01576xdGtMT2T8fabwEJtvSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 23493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 30,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RZC7Gjz4RFviJmNGcGWEHQ`</summary>

```json
{
  "query": "\"Grant\" \"2026\" \"VLA\" visual dominance behavioral"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "a08a5c02-217e-4590-bfce-658a28428fa3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01576xdGtMT2T8fabwEJtvSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 23493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 30,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PejkJdSzoDqWLj4DUKH1kt`</summary>

```json
{
  "query": "arXiv 2511.22134 DualVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "2ce3ee2f-938c-4b78-aba8-af6062c4e110",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01576xdGtMT2T8fabwEJtvSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 23493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 30,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HyJorqQUMdAe3SBP11GKqY`</summary>

```json
{
  "query": "arXiv 2603.05487"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "a9803998-a777-45d0-9d58-c6dab0b102e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01576xdGtMT2T8fabwEJtvSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 23493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 30,
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

_source line 12 · 2026-05-16T04:22:10.845Z_

<details><summary>↩ Tool result · `toolu_01HyJorqQUMdAe3SBP11GKqY`</summary>

```text
Web search results for query: "arXiv 2603.05487"

Links: [{"title":"[2603.05487] Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05487"},{"title":"Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/html/2603.05487"},{"title":"EvidFuse: Writing-Time Evidence Learning for Consistent Text–Chart Data Reporting","url":"https://arxiv.org/html/2601.05487"},{"title":"[2503.05487] A novel Lagrange-multiplier approach to the effective-one-body dynamics of binary systems in post-Minkowskian gravity","url":"https://arxiv.org/abs/2503.05487"},{"title":"[2603.04584] Fault-tolerant execution of error-corrected quantum algorithms","url":"https://arxiv.org/abs/2603.04584"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=543&show=2000"},{"title":"David Amaro","url":"https://scholar.google.de/citations?user=9W0kHZ4AAAAJ&hl=ja"},{"title":"Securing Social Media Against Deepfakes using Identity, Behavioral, and Geometric Signatures","url":"https://arxiv.org/html/2412.05487"},{"title":"Fault-tolerant execution of error-corrected quantum ...","url":"https://x.com/QuantumPapers/status/2030111889263337732"},{"title":"Top arXiv papers","url":"https://scirate.com/?amp=&date=2026-03-16&page=16&page=8&range=1&range=7"}]

Based on the search results, arXiv paper 2603.05487 is titled "Observing and Controlling Features in Vision-Language-Action Models" by Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, and Marco Pavone, submitted on March 5, 2026.

The paper addresses Vision-Language-Action Models (VLAs), which have shown remarkable progress towards embodied intelligence but exhibit higher complexity due to their multi-modal inputs/outputs and often hybrid nature of transformer and diffusion heads. The work introduces and analyzes two main concepts: feature-observability and feature-controllability, studying features that are linearly encoded in representation space and showing how they can be observed with a linear classifier, then using a minimal linear intervention to steer the VLA's output towards a desired region.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "120225e1-2848-4d90-b964-5fe080444140",
  "tool_use_result": {
    "query": "arXiv 2603.05487",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WX3ZvHanugK2JUrVYsAP8L",
        "content": [
          {
            "title": "[2603.05487] Observing and Controlling Features in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.05487"
          },
          {
            "title": "Observing and Controlling Features in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.05487"
          },
          {
            "title": "EvidFuse: Writing-Time Evidence Learning for Consistent Text–Chart Data Reporting",
            "url": "https://arxiv.org/html/2601.05487"
          },
          {
            "title": "[2503.05487] A novel Lagrange-multiplier approach to the effective-one-body dynamics of binary systems in post-Minkowskian gravity",
            "url": "https://arxiv.org/abs/2503.05487"
          },
          {
            "title": "[2603.04584] Fault-tolerant execution of error-corrected quantum algorithms",
            "url": "https://arxiv.org/abs/2603.04584"
          },
          {
            "title": "Computer Science",
            "url": "https://arxiv.org/list/cs/recent?skip=543&show=2000"
          },
          {
            "title": "David Amaro",
            "url": "https://scholar.google.de/citations?user=9W0kHZ4AAAAJ&hl=ja"
          },
          {
            "title": "Securing Social Media Against Deepfakes using Identity, Behavioral, and Geometric Signatures",
            "url": "https://arxiv.org/html/2412.05487"
          },
          {
            "title": "Fault-tolerant execution of error-corrected quantum ...",
            "url": "https://x.com/QuantumPapers/status/2030111889263337732"
          },
          {
            "title": "Top arXiv papers",
            "url": "https://scirate.com/?amp=&date=2026-03-16&page=16&page=8&range=1&range=7"
          }
        ]
      },
      "Based on the search results, arXiv paper 2603.05487 is titled \"Observing and Controlling Features in Vision-Language-Action Models\" by Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, and Marco Pavone, submitted on March 5, 2026.\n\nThe paper addresses Vision-Language-Action Models (VLAs), which have shown remarkable progress towards embodied intelligence but exhibit higher complexity due to their multi-modal inputs/outputs and often hybrid nature of transformer and diffusion heads. The work introduces and analyzes two main concepts: feature-observability and feature-controllability, studying features that are linearly encoded in representation space and showing how they can be observed with a linear classifier, then using a minimal linear intervention to steer the VLA's output towards a desired region."
    ],
    "durationSeconds": 4.804980014999999
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T04:22:11.460Z_

<details><summary>↩ Tool result · `toolu_01RZC7Gjz4RFviJmNGcGWEHQ`</summary>

```text
Web search results for query: ""Grant" "2026" "VLA" visual dominance behavioral"

Links: [{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/html/2603.19233"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"[2603.19233] Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.19233"},{"title":"Comprehensive Survey of VLA Models | PDF | Embodied Cognition | Computer Vision","url":"https://www.scribd.com/document/939026368/Pure-Vision-Language-Action-VLA-Models-A-Comprehensive-Survey"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"},{"title":"What are Vision Language Action (VLA) Models? Complete Guide","url":"https://www.articsledge.com/post/vision-language-action-vla-models"},{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"Vision-Language-Action (VLA) Models for Robotics","url":"https://blog.roboflow.com/vision-language-action-models/"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"How Visual-Language-Action (VLA) Models Work | Towards Data Science","url":"https://towardsdatascience.com/how-visual-language-action-vla-models-work/"}]

Based on the search results, I found relevant research matching your query. The most directly relevant result is a 2026 paper by Bryce Grant and colleagues titled "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models."

The key finding regarding visual dominance and behavioral control is: "The visual pathway dominates behavior across all architectures." More specifically, the visual pathway dominates action generation across all architectures, with injecting baseline activations into null-prompt episodes recovering near-identical behavior, while cross-task injection steers robots toward source-task positions.

The research also reveals that language sensitivity depends on task structure, not model design: when visual context uniquely specifies the task, language is ignored; when multiple goals share a scene, language becomes essential.

This study analyzed six models spanning 80M--7B parameters across 394,000+ rollout episodes on four benchmarks using activation injection, sparse autoencoders, and linear probes to understand how VLA models process multimodal inputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "d067b35b-74ee-4c0c-aa02-0709fde9be90",
  "tool_use_result": {
    "query": "\"Grant\" \"2026\" \"VLA\" visual dominance behavioral",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EqGfnF6kAe2c8QQxgya3S4",
        "content": [
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.19233"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "[2603.19233] Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.19233"
          },
          {
            "title": "Comprehensive Survey of VLA Models | PDF | Embodied Cognition | Computer Vision",
            "url": "https://www.scribd.com/document/939026368/Pure-Vision-Language-Action-VLA-Models-A-Comprehensive-Survey"
          },
          {
            "title": "2026-01-28 Work in progress.",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "What are Vision Language Action (VLA) Models? Complete Guide",
            "url": "https://www.articsledge.com/post/vision-language-action-vla-models"
          },
          {
            "title": "Vision-Language-Action (VLA) Guide for 2026",
            "url": "https://hyscaler.com/insights/vision-language-action-vla-guide/"
          },
          {
            "title": "Vision-Language-Action (VLA) Models for Robotics",
            "url": "https://blog.roboflow.com/vision-language-action-models/"
          },
          {
            "title": "Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v2"
          },
          {
            "title": "How Visual-Language-Action (VLA) Models Work | Towards Data Science",
            "url": "https://towardsdatascience.com/how-visual-language-action-vla-models-work/"
          }
        ]
      },
      "Based on the search results, I found relevant research matching your query. The most directly relevant result is a 2026 paper by Bryce Grant and colleagues titled \"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models.\"\n\nThe key finding regarding visual dominance and behavioral control is: \"The visual pathway dominates behavior across all architectures.\" More specifically, the visual pathway dominates action generation across all architectures, with injecting baseline activations into null-prompt episodes recovering near-identical behavior, while cross-task injection steers robots toward source-task positions.\n\nThe research also reveals that language sensitivity depends on task structure, not model design: when visual context uniquely specifies the task, language is ignored; when multiple goals share a scene, language becomes essential.\n\nThis study analyzed six models spanning 80M--7B parameters across 394,000+ rollout episodes on four benchmarks using activation injection, sparse autoencoders, and linear probes to understand how VLA models process multimodal inputs."
    ],
    "durationSeconds": 6.073001883000001
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T04:22:12.573Z_

<details><summary>↩ Tool result · `toolu_01PejkJdSzoDqWLj4DUKH1kt`</summary>

```text
Web search results for query: "arXiv 2511.22134 DualVLA"

Links: [{"title":"[2511.22134] DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/abs/2511.22134"},{"title":"DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action","url":"https://arxiv.org/html/2511.22134"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?show=2000&skip=471"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/pastweek?skip=1527&show=1000"},{"title":"Shuai Bai on X: \"Excited to share the release of our Qwen3-VL paper! 🚀 Paper: https://t.co/8nWMoRfhWi https://t.co/tWbsSxq17a\" / X","url":"https://x.com/shuai_bai_/status/1993919195206307961"},{"title":"Qwen on X: \"🚀 Qwen3-VL Tech report is now out on arXiv! From pretraining to post-training, architecture to infra, data to evaluation — we’ve packed in the details for anyone building on vision-language models. 🔥 3 models &gt;1M downloads in just over a month 🏆 Qwen3-VL-8B leads with 2M+ https://t.co/V58ikesnbJ\" / X","url":"https://x.com/Alibaba_Qwen/status/1993941138844287049"},{"title":"2511.21631v2","url":"https://www.scribd.com/document/959697630/2511-21631v2"},{"title":"Chen Cheng on X: \"🚀 Qwen3-VL tech report is out on arXiv! Check it out: https://t.co/5ugBUwzTyZ\" / X","url":"https://x.com/cherry_cc12/status/1993942896521957576"},{"title":"Computer Vision and Pattern Recognition","url":"https://arxiv.org/list/cs.CV/new"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2511.23391"}]

Based on the search results, here's what I found about arXiv paper 2511.22134:

## DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action

The paper is titled "DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action" by Zhen Fang and 9 other authors.

### Problem and Solution

The paper addresses the challenge of building a generalizable Vision-Language-Action (VLA) model with strong reasoning ability, noting that when specialist VLAs trained on robot demonstrations are fine-tuned with broader multimodal data, the resulting reasoning VLA often suffers from degraded action performance, a phenomenon referred to as "action degeneration".

### Key Contributions

To address this issue, DualVLA enhances action performance through carefully designed post-training while preserving reasoning capability, using a dual-layer data pruning method that removes redundant embodied reasoning and a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains while maintaining reasoning ability.

The authors also propose VLA Score, which decouples VLA capability into reasoning, intention, action, and alignment dimensions for a more fine-grained assessment.

### Results

Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks, demonstrating a stronger balance between precise action execution and multimodal understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "611354a8-7b4a-468c-82c1-1ab9e8da5702",
  "tool_use_result": {
    "query": "arXiv 2511.22134 DualVLA",
    "results": [
      {
        "tool_use_id": "srvtoolu_016PiZKds7X3qH2DGaz7KumJ",
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
            "title": "Computer Science",
            "url": "https://arxiv.org/list/cs/recent?show=2000&skip=471"
          },
          {
            "title": "Computer Science",
            "url": "https://www.arxiv.org/list/cs/pastweek?skip=1527&show=1000"
          },
          {
            "title": "Shuai Bai on X: \"Excited to share the release of our Qwen3-VL paper! 🚀 Paper: https://t.co/8nWMoRfhWi https://t.co/tWbsSxq17a\" / X",
            "url": "https://x.com/shuai_bai_/status/1993919195206307961"
          },
          {
            "title": "Qwen on X: \"🚀 Qwen3-VL Tech report is now out on arXiv! From pretraining to post-training, architecture to infra, data to evaluation — we’ve packed in the details for anyone building on vision-language models. 🔥 3 models &gt;1M downloads in just over a month 🏆 Qwen3-VL-8B leads with 2M+ https://t.co/V58ikesnbJ\" / X",
            "url": "https://x.com/Alibaba_Qwen/status/1993941138844287049"
          },
          {
            "title": "2511.21631v2",
            "url": "https://www.scribd.com/document/959697630/2511-21631v2"
          },
          {
            "title": "Chen Cheng on X: \"🚀 Qwen3-VL tech report is out on arXiv! Check it out: https://t.co/5ugBUwzTyZ\" / X",
            "url": "https://x.com/cherry_cc12/status/1993942896521957576"
          },
          {
            "title": "Computer Vision and Pattern Recognition",
            "url": "https://arxiv.org/list/cs.CV/new"
          },
          {
            "title": "Arxiv",
            "url": "https://arxiv.org/pdf/2511.23391"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2511.22134:\n\n## DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action\n\nThe paper is titled \"DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action\" by Zhen Fang and 9 other authors.\n\n### Problem and Solution\n\nThe paper addresses the challenge of building a generalizable Vision-Language-Action (VLA) model with strong reasoning ability, noting that when specialist VLAs trained on robot demonstrations are fine-tuned with broader multimodal data, the resulting reasoning VLA often suffers from degraded action performance, a phenomenon referred to as \"action degeneration\".\n\n### Key Contributions\n\nTo address this issue, DualVLA enhances action performance through carefully designed post-training while preserving reasoning capability, using a dual-layer data pruning method that removes redundant embodied reasoning and a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains while maintaining reasoning ability.\n\nThe authors also propose VLA Score, which decouples VLA capability into reasoning, intention, action, and alignment dimensions for a more fine-grained assessment.\n\n### Results\n\nExperiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks, demonstrating a stronger balance between precise action execution and multimodal understanding."
    ],
    "durationSeconds": 6.572884944000001
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Good, I got initial results. Let me now:

1. For grant2026: Found "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models" (arXiv:2603.19233). Need to confirm the author is "Bryce Grant" and get exact details.

2. For fang2025: DualVLA (arXiv:2511.22134) by Zhen Fang. The paper discusses "action degeneration" when fine-tuning with broader multimodal data, which relates to "fine-tuning erodes reasoning" but the framing is slightly different. 

The DualVLA paper actually shows degraded action performance when reasoning is added rather than the inverse, so I need to search more carefully for the exact match.

3. For rizzardo2026: Found arXiv:2603.05487 is by Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, and Marco Pavone. Not Rizzardo. Need to confirm this.

Let me do follow-up searches to get more precise details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "7694466d-ada0-49b1-8621-8e8d1c9e3c65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6bYvC6KA4zry1SPtKgYPC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 672,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 24140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
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

_source line 16_

找到初步结果，需要进一步确认细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "f644ecff-623f-49a7-8068-55e041253f55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6bYvC6KA4zry1SPtKgYPC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 672,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 24140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
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

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014zULPLtAmcSzDnQanTHnyC`</summary>

```json
{
  "query": "\"Not All Features Are Created Equal\" \"Mechanistic Study\" VLA Grant 2026 authors arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "2e1b1dee-1fac-41f2-9a09-a820b27e05f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6bYvC6KA4zry1SPtKgYPC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 672,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 24140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XNS6Y96LhUwHEQ5XE31cVr`</summary>

```json
{
  "query": "\"Fang\" \"2025\" \"fine-tuning erodes\" VLM reasoning VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "95d6e8b4-4f78-40a0-9b9f-1d8d0eb0b4d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6bYvC6KA4zry1SPtKgYPC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 672,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 24140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0164EwQCrk9rWw4sueiVafop`</summary>

```json
{
  "query": "\"Observing and Controlling Features\" Buurmeijer VLA 2026 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "8750f757-8626-458c-b850-d89cbe495bad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6bYvC6KA4zry1SPtKgYPC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 672,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 24140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
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

_source line 20 · 2026-05-16T04:22:24.303Z_

<details><summary>↩ Tool result · `toolu_0164EwQCrk9rWw4sueiVafop`</summary>

```text
Web search results for query: ""Observing and Controlling Features" Buurmeijer VLA 2026 authors"

Links: [{"title":"[2603.05487] Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05487"},{"title":"Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/html/2603.05487v1"},{"title":"(PDF) Observing and Controlling Features in Vision-Language-Action Models","url":"https://www.researchgate.net/publication/401601449_Observing_and_Controlling_Features_in_Vision-Language-Action_Models"}]

Based on the search results, the authors of "Observing and Controlling Features in Vision-Language-Action Models" are Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, and Marco Pavone. The paper was submitted on March 5, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "fc516b46-1742-4ad2-aba9-38c1d3b969f2",
  "tool_use_result": {
    "query": "\"Observing and Controlling Features\" Buurmeijer VLA 2026 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TYTMHsHeeCzzGgNQ16L8WL",
        "content": [
          {
            "title": "[2603.05487] Observing and Controlling Features in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.05487"
          },
          {
            "title": "Observing and Controlling Features in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.05487v1"
          },
          {
            "title": "(PDF) Observing and Controlling Features in Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/401601449_Observing_and_Controlling_Features_in_Vision-Language-Action_Models"
          }
        ]
      },
      "Based on the search results, the authors of \"Observing and Controlling Features in Vision-Language-Action Models\" are Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, and Marco Pavone. The paper was submitted on March 5, 2026."
    ],
    "durationSeconds": 2.9974895560000006
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T04:22:26.118Z_

<details><summary>↩ Tool result · `toolu_014zULPLtAmcSzDnQanTHnyC`</summary>

```text
Web search results for query: ""Not All Features Are Created Equal" "Mechanistic Study" VLA Grant 2026 authors arXiv"

Links: [{"title":"[2603.19233] Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/html/2603.19233v1"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=w8Mw9zJt1y"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.19233"},{"title":"Robotics Research arXiv on X: \"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models Bryce Grant, Xijia Zhao, Peng Wang https://t.co/Mr1IyrLxt9 [𝚌𝚜.𝚁𝙾] https://t.co/9LLIgjodQp\" / X","url":"https://x.com/OWW/status/2034850674173788594"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://www.wispaper.ai/en/blog/not-all-features-created-equal-mechanistic-study-vision-language-action-models-20260320/zho"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.19233v1"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"

**Authors:** Bryce Grant, Xijia Zhao, and Peng Wang

**ArXiv ID:** 2603.19233

**Publication Date:** March 19, 2026

**Overview:** The paper studies Vision-Language-Action (VLA) models and applies activation injection, sparse autoencoders (SAEs), and linear probes to six models spanning 80M-7B parameters across 394,000+ rollout episodes on four benchmarks.

**Key Findings:** The visual pathway dominates action generation across all architectures, and cross-task injection steers robots toward source-task positions with 99.8% of X-VLA episodes aligning with the source trajectory, exposing spatially bound motor programs tied to scene coordinates rather than abstract task representations.

The paper is available on arXiv at https://arxiv.org/abs/2603.19233.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "9ba40b4d-0862-4ecc-813a-8f18345ccfce",
  "tool_use_result": {
    "query": "\"Not All Features Are Created Equal\" \"Mechanistic Study\" VLA Grant 2026 authors arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JS1v2y1rCv9B5jvLuuB6tv",
        "content": [
          {
            "title": "[2603.19233] Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.19233"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.19233v1"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=w8Mw9zJt1y"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2603.19233"
          },
          {
            "title": "Robotics Research arXiv on X: \"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models Bryce Grant, Xijia Zhao, Peng Wang https://t.co/Mr1IyrLxt9 [𝚌𝚜.𝚁𝙾] https://t.co/9LLIgjodQp\" / X",
            "url": "https://x.com/OWW/status/2034850674173788594"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models",
            "url": "https://www.wispaper.ai/en/blog/not-all-features-created-equal-mechanistic-study-vision-language-action-models-20260320/zho"
          },
          {
            "title": "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2603.19233v1"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** \"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\"\n\n**Authors:** Bryce Grant, Xijia Zhao, and Peng Wang\n\n**ArXiv ID:** 2603.19233\n\n**Publication Date:** March 19, 2026\n\n**Overview:** The paper studies Vision-Language-Action (VLA) models and applies activation injection, sparse autoencoders (SAEs), and linear probes to six models spanning 80M-7B parameters across 394,000+ rollout episodes on four benchmarks.\n\n**Key Findings:** The visual pathway dominates action generation across all architectures, and cross-task injection steers robots toward source-task positions with 99.8% of X-VLA episodes aligning with the source trajectory, exposing spatially bound motor programs tied to scene coordinates rather than abstract task representations.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2603.19233."
    ],
    "durationSeconds": 5.251311548000005
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T04:22:26.881Z_

<details><summary>↩ Tool result · `toolu_01XNS6Y96LhUwHEQ5XE31cVr`</summary>

```text
Web search results for query: ""Fang" "2025" "fine-tuning erodes" VLM reasoning VLA"

Links: [{"title":"TwinBrainVLA: Unleashing the Potential of Generalist VLMs for Embodied Tasks via Asymmetric Mixture-of-Transformers","url":"https://arxiv.org/html/2601.14133"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"[2512.12690] Reassessing the Role of Supervised Fine-Tuning: An Empirical Study in VLM Reasoning","url":"https://arxiv.org/abs/2512.12690"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v2"},{"title":"Clutter-Robust Vision–Language–Action Models through Object-Centric and Geometry Grounding","url":"https://arxiv.org/html/2512.22519"},{"title":"MolmoAct2 Action Reasoning Models for Real-World Deployment Haoquan Fang♥1,2∗","url":"https://arxiv.org/pdf/2605.02881"},{"title":"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.22195"},{"title":"DriveVLA-W0: World Models Amplify Data Scaling Law in ...","url":"https://arxiv.org/pdf/2510.12796"},{"title":"2025-10-30 Alpamayo-R1: Bridging Reasoning and Action Prediction","url":"https://d1qx31qr3h6wln.cloudfront.net/publications/Alpamayo-R1_1.pdf"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"}]

I found several relevant research papers on this topic. The search results contain multiple 2025 papers that discuss the phenomenon of fine-tuning eroding VLM reasoning in Vision-Language-Action (VLA) models.

Fine-tuning VLMs on robotic datasets precipitates "catastrophic forgetting" (Fang et al., 2025), referring to a specific work by Fang and colleagues in 2025. 

Fine-tuning VLMs for robotic action generation (VLA training) diminishes the model's foundational reasoning and multimodal understanding, potentially leading to a loss of general conversational abilities (Zhou et al., 2025; Xu et al., 2025; Hancock et al., 2025; Yu et al., 2026).

The end-to-end paradigm erodes language-conditioned visual grounding: in real-world experiments, policies over-grasp when the requested object is absent, are easily distracted by clutter, and overfit to background appearance, leading to degraded performance in realistic tabletop scenes with distractors, background shifts, and unseen objects.

The specific Fang et al. 2025 paper appears to be titled "DualVLA: building a generalizable embodied agent via partial decoupling of reasoning and action", which addresses this exact problem of how fine-tuning erodes the VLM's reasoning capabilities in VLA models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "53b268a5-69c1-4a4e-9766-62524ee7bc28",
  "tool_use_result": {
    "query": "\"Fang\" \"2025\" \"fine-tuning erodes\" VLM reasoning VLA",
    "results": [
      {
        "tool_use_id": "srvtoolu_0154CUPL9oLPaNpYpmAzUEJT",
        "content": [
          {
            "title": "TwinBrainVLA: Unleashing the Potential of Generalist VLMs for Embodied Tasks via Asymmetric Mixture-of-Transformers",
            "url": "https://arxiv.org/html/2601.14133"
          },
          {
            "title": "LangForce: Bayesian Decomposition of Vision Language ...",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "[2512.12690] Reassessing the Role of Supervised Fine-Tuning: An Empirical Study in VLM Reasoning",
            "url": "https://arxiv.org/abs/2512.12690"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v2"
          },
          {
            "title": "Clutter-Robust Vision–Language–Action Models through Object-Centric and Geometry Grounding",
            "url": "https://arxiv.org/html/2512.22519"
          },
          {
            "title": "MolmoAct2 Action Reasoning Models for Real-World Deployment Haoquan Fang♥1,2∗",
            "url": "https://arxiv.org/pdf/2605.02881"
          },
          {
            "title": "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2509.22195"
          },
          {
            "title": "DriveVLA-W0: World Models Amplify Data Scaling Law in ...",
            "url": "https://arxiv.org/pdf/2510.12796"
          },
          {
            "title": "2025-10-30 Alpamayo-R1: Bridging Reasoning and Action Prediction",
            "url": "https://d1qx31qr3h6wln.cloudfront.net/publications/Alpamayo-R1_1.pdf"
          },
          {
            "title": "GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub",
            "url": "https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"
          }
        ]
      },
      "I found several relevant research papers on this topic. The search results contain multiple 2025 papers that discuss the phenomenon of fine-tuning eroding VLM reasoning in Vision-Language-Action (VLA) models.\n\nFine-tuning VLMs on robotic datasets precipitates \"catastrophic forgetting\" (Fang et al., 2025), referring to a specific work by Fang and colleagues in 2025. \n\nFine-tuning VLMs for robotic action generation (VLA training) diminishes the model's foundational reasoning and multimodal understanding, potentially leading to a loss of general conversational abilities (Zhou et al., 2025; Xu et al., 2025; Hancock et al., 2025; Yu et al., 2026).\n\nThe end-to-end paradigm erodes language-conditioned visual grounding: in real-world experiments, policies over-grasp when the requested object is absent, are easily distracted by clutter, and overfit to background appearance, leading to degraded performance in realistic tabletop scenes with distractors, background shifts, and unseen objects.\n\nThe specific Fang et al. 2025 paper appears to be titled \"DualVLA: building a generalizable embodied agent via partial decoupling of reasoning and action\", which addresses this exact problem of how fine-tuning erodes the VLM's reasoning capabilities in VLA models."
    ],
    "durationSeconds": 6.010091442999998
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the DualVLA paper more carefully. The search results suggest that DualVLA by Fang et al. does discuss "fine-tuning eroding reasoning" in VLA context, specifically "action degeneration" when specialist VLAs are fine-tuned. But the framing in paper_framing.md says "fine-tuning erodes VLM reasoning" while the actual paper discusses how adding reasoning training degrades action performance (action degeneration), AND more broadly how fine-tuning VLMs for action erodes their reasoning. Let me check whether the DualVLA paper explicitly discusses fine-tuning eroding reasoning or if there's another Fang 2025 paper.


Looking at the search results, the DualVLA paper frames this as "catastrophic forgetting" when fine-tuning VLMs on robotic datasets, and specifically describes how specialist VLAs suffer from degraded action performance when broader multimodal data is added—what they call "action degeneration." So the paper does address the bidirectional trade-off between reasoning and action capabilities during fine-tuning. I'm checking another paper on fine-tuning VLMs, "Actions as Language," but that's a different work. So DualVLA is the key reference here—it addresses how fine-tuning for action tasks can degrade reasoning, and their solution involves adding reasoning back in, though that creates its own tradeoff. The citation characterizes this reasonably well, capturing the core tension between action performance and reasoning preservation that the paper explores. The fang2025 citation is roughly accurate but needs some nuance around the framing. For rizzardo2026, there's a clear author mismatch—the paper at arXiv:2603.05487 is actually by Buurmeijer and colleagues, not Rizzardo, so the cite key should be corrected to buurmeijer2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "adbd986c-c0be-47fb-966e-d765d8a33672",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjiSNkh1qGpXMkSgAssndv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 294,
      "cache_creation_input_tokens": 2839,
      "cache_read_input_tokens": 26085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2839
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

验证完成。结果如下：

---

### 引用 1: grant2026

```
引用 ID: grant2026
状态: VERIFIED
真实信息:
  Title: "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"
  Authors: Bryce Grant, Xijia Zhao, Peng Wang
  ArXiv ID: 2603.19233
  Year: 2026 (March)
  Venue: arXiv preprint (also on OpenReview)
与当前 bib 差异: 当前 bib 为占位符，需替换为真实信息
建议修正: 更新 bib 条目为上述真实信息。arXiv ID 是 2603.19233。
  关键发现与引用描述一致："the visual pathway dominates action generation across all architectures"
```

---

### 引用 2: fang2025

```
引用 ID: fang2025
状态: VERIFIED（但引用描述需微调）
真实信息:
  Title: "DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action"
  Authors: Zhen Fang et al.
  ArXiv ID: 2511.22134
  Year: 2025
与当前 bib 差异: bib 条目本身正确。
  但 paper_framing.md 引用为 "fine-tuning erodes VLM reasoning"，
  而论文实际讨论的是双向问题：
  (1) 将 VLM 微调为 VLA 会丢失推理能力（catastrophic forgetting）——这是论文动机
  (2) 给 specialist VLA 加回推理训练会导致 action degeneration——这是论文解决的问题
建议修正: 引用描述可保留，但更精确的表述是
  "fine-tuning VLMs into VLAs precipitates catastrophic forgetting of reasoning (Fang et al., 2025)"
  而非笼统的 "fine-tuning erodes VLM reasoning"
```

---

### 引用 3: rizzardo2026

```
引用 ID: rizzardo2026
状态: MISMATCH — 第一作者错误
真实信息:
  Title: "Observing and Controlling Features in Vision-Language-Action Models"
  Authors: Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone
  ArXiv ID: 2603.05487 ✓（正确）
  Year: 2026 (March)
与当前 bib 差异: cite key 为 rizzardo2026，但论文第一作者是 Buurmeijer，不是 Rizzardo。
  论文中无 Rizzardo 此人。
建议修正:
  1. cite key 改为 buurmeijer2026
  2. author 字段改为 {Hugo Buurmeijer and Carmen Amo Alonso and Aiden Swann and Marco Pavone}
  3. 全文搜索替换所有 \cite{rizzardo2026} → \cite{buurmeijer2026}
```

---

### 总结

| 引用 | 状态 | 阻塞? |
|------|------|-------|
| grant2026 | **VERIFIED** — 论文存在，arXiv:2603.19233，需更新占位符 bib | 更新 bib 后解除阻塞 |
| fang2025 | **VERIFIED** — bib 正确，引用描述可微调更精确 | 不阻塞 |
| rizzardo2026 | **MISMATCH** — 第一作者是 Buurmeijer 非 Rizzardo，需改 cite key | 需修正 |

Sources:
- [Grant et al. 2026 - arXiv](https://arxiv.org/abs/2603.19233)
- [Grant et al. 2026 - OpenReview](https://openreview.net/forum?id=w8Mw9zJt1y)
- [Fang et al. 2025 - DualVLA](https://arxiv.org/abs/2511.22134)
- [Buurmeijer et al. 2026 - arXiv](https://arxiv.org/abs/2603.05487)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "uuid": "66c05a8f-ef22-408b-9323-efe4052b98c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjiSNkh1qGpXMkSgAssndv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 294,
      "cache_creation_input_tokens": 2839,
      "cache_read_input_tokens": 26085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2839
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

_source line 25_

验证完成。结果如下：

---

### 引用 1: grant2026

```
引用 ID: grant2026
状态: VERIFIED
真实信息:
  Title: "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"
  Authors: Bryce Grant, Xijia Zhao, Peng Wang
  ArXiv ID: 2603.19233
  Year: 2026 (March)
  Venue: arXiv preprint (also on OpenReview)
与当前 bib 差异: 当前 bib 为占位符，需替换为真实信息
建议修正: 更新 bib 条目为上述真实信息。arXiv ID 是 2603.19233。
  关键发现与引用描述一致："the visual pathway dominates action generation across all architectures"
```

---

### 引用 2: fang2025

```
引用 ID: fang2025
状态: VERIFIED（但引用描述需微调）
真实信息:
  Title: "DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action"
  Authors: Zhen Fang et al.
  ArXiv ID: 2511.22134
  Year: 2025
与当前 bib 差异: bib 条目本身正确。
  但 paper_framing.md 引用为 "fine-tuning erodes VLM reasoning"，
  而论文实际讨论的是双向问题：
  (1) 将 VLM 微调为 VLA 会丢失推理能力（catastrophic forgetting）——这是论文动机
  (2) 给 specialist VLA 加回推理训练会导致 action degeneration——这是论文解决的问题
建议修正: 引用描述可保留，但更精确的表述是
  "fine-tuning VLMs into VLAs precipitates catastrophic forgetting of reasoning (Fang et al., 2025)"
  而非笼统的 "fine-tuning erodes VLM reasoning"
```

---

### 引用 3: rizzardo2026

```
引用 ID: rizzardo2026
状态: MISMATCH — 第一作者错误
真实信息:
  Title: "Observing and Controlling Features in Vision-Language-Action Models"
  Authors: Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone
  ArXiv ID: 2603.05487 ✓（正确）
  Year: 2026 (March)
与当前 bib 差异: cite key 为 rizzardo2026，但论文第一作者是 Buurmeijer，不是 Rizzardo。
  论文中无 Rizzardo 此人。
建议修正:
  1. cite key 改为 buurmeijer2026
  2. author 字段改为 {Hugo Buurmeijer and Carmen Amo Alonso and Aiden Swann and Marco Pavone}
  3. 全文搜索替换所有 \cite{rizzardo2026} → \cite{buurmeijer2026}
```

---

### 总结

| 引用 | 状态 | 阻塞? |
|------|------|-------|
| grant2026 | **VERIFIED** — 论文存在，arXiv:2603.19233，需更新占位符 bib | 更新 bib 后解除阻塞 |
| fang2025 | **VERIFIED** — bib 正确，引用描述可微调更精确 | 不阻塞 |
| rizzardo2026 | **MISMATCH** — 第一作者是 Buurmeijer 非 Rizzardo，需改 cite key | 需修正 |

Sources:
- [Grant et al. 2026 - arXiv](https://arxiv.org/abs/2603.19233)
- [Grant et al. 2026 - OpenReview](https://openreview.net/forum?id=w8Mw9zJt1y)
- [Fang et al. 2025 - DualVLA](https://arxiv.org/abs/2511.22134)
- [Buurmeijer et al. 2026 - arXiv](https://arxiv.org/abs/2603.05487)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 66227,
  "duration_api_ms": 86883,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "cc12bf9a-aa4d-425d-9ceb-d2575d804bba",
  "total_cost_usd": 0.3828992500000001,
  "usage": {
    "input_tokens": 971,
    "cache_creation_input_tokens": 17083,
    "cache_read_input_tokens": 85559,
    "output_tokens": 3039,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 17083,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 294,
        "output_tokens": 2246,
        "cache_read_input_tokens": 26085,
        "cache_creation_input_tokens": 2839,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2839
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 81826,
      "outputTokens": 2139,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 6,
      "costUSD": 0.152521,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 971,
      "outputTokens": 3039,
      "cacheReadInputTokens": 85559,
      "cacheCreationInputTokens": 17083,
      "webSearchRequests": 0,
      "costUSD": 0.23037825,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "599f1eb7-cf29-4cc3-9cc6-0ec36c4e54dc"
}
```

</details>

---
