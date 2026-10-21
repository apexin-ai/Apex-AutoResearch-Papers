# research competitive analysis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/workers/worker_research_competitive-analysis_20260515T014521.log`
- **Structured JSON:** [`0989cce848f03f372c4f.json`](../../sessions/09/0989cce848f03f372c4f.json)

## Before a recorded user message

60 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
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
  "uuid": "2ab27caf-968a-41ae-ba2c-0be645955ad2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778816400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "96498c67-3b2c-429a-b485-fb5335e19a3f",
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299"
}
```

---

### Assistant

_source line 4_

I'll start by searching for competitor papers and reading the current project files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "62878193-b531-4f6a-9ec0-e16732ef1b4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPVdUTiGLjR6tTahts7Wxd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11758,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11758
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0137CoHc62NWBbwr8XLPaCUq`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "834f60ac-e6b5-439e-80ac-e47544b7c8e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPVdUTiGLjR6tTahts7Wxd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11758,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11758
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

_source line 6 · 2026-05-15T01:45:30.581Z_

<details><summary>↩ Tool result · `toolu_0137CoHc62NWBbwr8XLPaCUq`</summary>

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
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "951a0500-cf79-46e8-b691-ff47fc8052ad",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
Now I'll launch the searches and file reads in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "d5b2006c-e74e-4a89-b62e-087db90ec1ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYCi8G7QjM5NidZxv2s1SZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1832
      },
      "output_tokens": 17,
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

Starting parallel searches and project file reads.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "0a3669b6-08fe-43ba-ba1f-1207df795f0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYCi8G7QjM5NidZxv2s1SZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1832
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_019G49gzaHcgcWf2jbAKJq4Q`</summary>

```json
{
  "query": "SC-VLA \"sample consensus\" VLA action selection robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "55840533-fee0-4688-8c42-40d93f138250",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYCi8G7QjM5NidZxv2s1SZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1832
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TqUzPUqt4ZFuJqoavZ7d7D`</summary>

```json
{
  "query": "VLA-Pilot robot action refinement 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "74390518-6093-4a0b-a05c-e340f9ee5742",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYCi8G7QjM5NidZxv2s1SZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1832
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T2ZoSdn5FqLxfzRqkpAwb1`</summary>

```json
{
  "query": "ACoT-VLA \"action chain of thought\" VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "59e92f2a-3c5b-4643-b10a-a2f67c36b5b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYCi8G7QjM5NidZxv2s1SZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1832
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_012CetgonX9xkFTrxUVQmyc2`</summary>

```json
{
  "query": "VLA action refinement correction flow matching robot manipulation 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "1f26be62-de86-474c-97a6-3b09771eeaa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYCi8G7QjM5NidZxv2s1SZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1832
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0168S8SXkHBBadhs2XpUHLYQ`</summary>

```json
{
  "query": "conformal prediction robotics action correction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "fd8fbc34-c37c-4175-a5f1-f3fc030ffbfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYCi8G7QjM5NidZxv2s1SZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1832
      },
      "output_tokens": 17,
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01T9vxY7buhyX29tAVWMrtit`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md",
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
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "a41dcc54-1b19-4b52-9dec-a1a91ca0311c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYCi8G7QjM5NidZxv2s1SZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1832
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LQY9m3wCKVMG3Xiyg1r8CK`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "166cecb9-9f1a-4fa2-9eca-22bb5b6a5a6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYCi8G7QjM5NidZxv2s1SZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1832,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1832
      },
      "output_tokens": 17,
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

_source line 16 · 2026-05-15T01:45:41.258Z_

<details><summary>↩ Tool result · `toolu_019G49gzaHcgcWf2jbAKJq4Q`</summary>

```text
Web search results for query: "SC-VLA "sample consensus" VLA action selection robot 2025 2026"

Links: [{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"What are Vision Language Action (VLA) Models? Complete Guide","url":"https://www.articsledge.com/post/vision-language-action-vla-models"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications","url":"https://vla-survey.github.io/"}]

I found search results related to VLA (Vision-Language-Action) models and robotics research for 2025-2026, but the results don't contain specific information about "SC-VLA" or "sample consensus" methods for VLA action selection. 

The search results do mention a relevant technique: a consensus-based approach using majority voting for pseudo-label construction in test-time reinforcement learning for VLAs, though this appears to underperform compared to other methods.

The broader context shows that by Q2 2025, three major robotics software companies had shipped VLA-based products to enterprise customers, and by Q1 2026, at least eleven commercial deployments are using VLA models as the primary policy backbone.

If you're looking for more specific information about SC-VLA or sample consensus methods for action selection in VLAs, it may be a very recent or specialized research area that isn't widely indexed yet, or the terminology might be slightly different than what's commonly used. Would you like me to search with different query terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "bc76ed68-ade1-4e77-b988-2badfcb094ea",
  "tool_use_result": {
    "query": "SC-VLA \"sample consensus\" VLA action selection robot 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S4q8T8z7GjLDtatPqj9E6o",
        "content": [
          {
            "title": "State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center",
            "url": "https://www.roboticscenter.ai/state-of-robotics-2026"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "What are Vision Language Action (VLA) Models? Complete Guide",
            "url": "https://www.articsledge.com/post/vision-language-action-vla-models"
          },
          {
            "title": "Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S1566253525011248"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2601.06748"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)",
            "url": "https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"
          },
          {
            "title": "Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications",
            "url": "https://vla-survey.github.io/"
          }
        ]
      },
      "I found search results related to VLA (Vision-Language-Action) models and robotics research for 2025-2026, but the results don't contain specific information about \"SC-VLA\" or \"sample consensus\" methods for VLA action selection. \n\nThe search results do mention a relevant technique: a consensus-based approach using majority voting for pseudo-label construction in test-time reinforcement learning for VLAs, though this appears to underperform compared to other methods.\n\nThe broader context shows that by Q2 2025, three major robotics software companies had shipped VLA-based products to enterprise customers, and by Q1 2026, at least eleven commercial deployments are using VLA models as the primary policy backbone.\n\nIf you're looking for more specific information about SC-VLA or sample consensus methods for action selection in VLAs, it may be a very recent or specialized research area that isn't widely indexed yet, or the terminology might be slightly different than what's commonly used. Would you like me to search with different query terms?"
    ],
    "durationSeconds": 5.044812333000002
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T01:45:42.914Z_

<details><summary>↩ Tool result · `toolu_01T2ZoSdn5FqLxfzRqkpAwb1`</summary>

```text
Web search results for query: "ACoT-VLA "action chain of thought" VLA 2025 2026"

Links: [{"title":"[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/abs/2601.11404"},{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/html/2601.11404v1"},{"title":"[2503.22020] CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://arxiv.org/abs/2503.22020"},{"title":"(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"},{"title":"CVPR Poster CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2025/poster/33233"},{"title":"ACoT-VLA/uv.lock at main · AgibotTech/ACoT-VLA","url":"https://github.com/AgibotTech/ACoT-VLA/blob/main/uv.lock"},{"title":"Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://huggingface.co/papers/2601.11404"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.11404"}]

Based on the search results, here's what I found about ACoT-VLA:

## Overview

Action Chain-of-Thought (ACoT) is a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy. ACoT-VLA is a novel architecture that materializes the ACoT paradigm through two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR).

## Architecture

The Explicit Action Reasoner proposes coarse reference trajectories as explicit action-level reasoning steps, while the Implicit Action Reasoner extracts latent action priors from internal representations of multimodal input, co-forming an ACoT that conditions the downstream action head to enable grounded policy learning.

## Key Innovation

By deliberating directly in the action space, ACoT-VLA provides more precise and grounded guidance for robotic policy learning than approaches relying on indirect linguistic or visual reasoning.

## Performance

The method achieves 98.5%, 84.1%, and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively. ACoT-VLA achieves state-of-the-art performance on multiple simulation benchmarks and exhibits superior robustness under distribution shifts.

## Publication Status

The paper is the official implementation presented at CVPR 2026. The repository serves as the official baseline implementation for the AgiBot World Challenge @ ICRA 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "e0789d32-890a-4d60-bab3-c0fb09ee081e",
  "tool_use_result": {
    "query": "ACoT-VLA \"action chain of thought\" VLA 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MQAWrMX88k3egr4dEva3NY",
        "content": [
          {
            "title": "[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2601.11404"
          },
          {
            "title": "GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub",
            "url": "https://github.com/AgibotTech/ACoT-VLA"
          },
          {
            "title": "[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"
          },
          {
            "title": "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2601.11404v1"
          },
          {
            "title": "[2503.22020] CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2503.22020"
          },
          {
            "title": "(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"
          },
          {
            "title": "CVPR Poster CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2025/poster/33233"
          },
          {
            "title": "ACoT-VLA/uv.lock at main · AgibotTech/ACoT-VLA",
            "url": "https://github.com/AgibotTech/ACoT-VLA/blob/main/uv.lock"
          },
          {
            "title": "Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2601.11404"
          },
          {
            "title": "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2601.11404"
          }
        ]
      },
      "Based on the search results, here's what I found about ACoT-VLA:\n\n## Overview\n\nAction Chain-of-Thought (ACoT) is a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy. ACoT-VLA is a novel architecture that materializes the ACoT paradigm through two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR).\n\n## Architecture\n\nThe Explicit Action Reasoner proposes coarse reference trajectories as explicit action-level reasoning steps, while the Implicit Action Reasoner extracts latent action priors from internal representations of multimodal input, co-forming an ACoT that conditions the downstream action head to enable grounded policy learning.\n\n## Key Innovation\n\nBy deliberating directly in the action space, ACoT-VLA provides more precise and grounded guidance for robotic policy learning than approaches relying on indirect linguistic or visual reasoning.\n\n## Performance\n\nThe method achieves 98.5%, 84.1%, and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively. ACoT-VLA achieves state-of-the-art performance on multiple simulation benchmarks and exhibits superior robustness under distribution shifts.\n\n## Publication Status\n\nThe paper is the official implementation presented at CVPR 2026. The repository serves as the official baseline implementation for the AgiBot World Challenge @ ICRA 2026."
    ],
    "durationSeconds": 5.212070744999999
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T01:45:43.511Z_

<details><summary>↩ Tool result · `toolu_01TqUzPUqt4ZFuJqoavZ7d7D`</summary>

```text
Web search results for query: "VLA-Pilot robot action refinement 2025 2026"

Links: [{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"What are Vision Language Action (VLA) Models? Complete Guide","url":"https://www.articsledge.com/post/vision-language-action-vla-models"},{"title":"Vision-Language-Action (VLA) Models for Robotics","url":"https://blog.roboflow.com/vision-language-action-models/"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"}]

Based on the web search results, here's what I found regarding VLA-Pilot robot action refinement in 2025-2026:

## Key Developments in VLA Action Refinement

Reinforcement learning feedback loops enable continuous improvement, as robots execute tasks and receive feedback about success or failure, reward signals, and corrections from human operators, driving ongoing policy refinement and allowing systems to adapt to new objects, environments, and task variations.

Upon encountering variations (e.g., a tilted bottle or slippery grip), systems like Helix perform micro-policy refinement in real time, adjusting control based on feedback. Advanced VLA models can even perform self-supervised learning, generating their own training signals by predicting action outcomes and learning from mismatches.

## Recent Innovations (2025-2026)

Recent improvements include CoT-VLA which introduces visual chain-of-thought reasoning by predicting intermediate visual goals before generating actions, and X-VLA which investigates scalable cross-embodiment learning through embodiment-specific soft prompts.

## Market Adoption and Performance

VLA adoption tripled in 2025–2026 and is now present in 40% of all new robot deployments. Quantized VLA models run at 10–25Hz on consumer-grade GPUs, making them viable for real-time manipulation.

These advancements show significant progress in making VLA systems more robust, adaptive, and deployable in real-world robotic applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "86f2ea70-85dc-4a06-97e2-903a1d2e73f4",
  "tool_use_result": {
    "query": "VLA-Pilot robot action refinement 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xp2ANFcfKqRwrmQqbMAbc9",
        "content": [
          {
            "title": "State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center",
            "url": "https://www.roboticscenter.ai/state-of-robotics-2026"
          },
          {
            "title": "Vision-Language-Action (VLA) Guide for 2026",
            "url": "https://hyscaler.com/insights/vision-language-action-vla-guide/"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v2"
          },
          {
            "title": "What are Vision Language Action (VLA) Models? Complete Guide",
            "url": "https://www.articsledge.com/post/vision-language-action-vla-models"
          },
          {
            "title": "Vision-Language-Action (VLA) Models for Robotics",
            "url": "https://blog.roboflow.com/vision-language-action-models/"
          },
          {
            "title": "Vision-Language-Action Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v1"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding VLA-Pilot robot action refinement in 2025-2026:\n\n## Key Developments in VLA Action Refinement\n\nReinforcement learning feedback loops enable continuous improvement, as robots execute tasks and receive feedback about success or failure, reward signals, and corrections from human operators, driving ongoing policy refinement and allowing systems to adapt to new objects, environments, and task variations.\n\nUpon encountering variations (e.g., a tilted bottle or slippery grip), systems like Helix perform micro-policy refinement in real time, adjusting control based on feedback. Advanced VLA models can even perform self-supervised learning, generating their own training signals by predicting action outcomes and learning from mismatches.\n\n## Recent Innovations (2025-2026)\n\nRecent improvements include CoT-VLA which introduces visual chain-of-thought reasoning by predicting intermediate visual goals before generating actions, and X-VLA which investigates scalable cross-embodiment learning through embodiment-specific soft prompts.\n\n## Market Adoption and Performance\n\nVLA adoption tripled in 2025–2026 and is now present in 40% of all new robot deployments. Quantized VLA models run at 10–25Hz on consumer-grade GPUs, making them viable for real-time manipulation.\n\nThese advancements show significant progress in making VLA systems more robust, adaptive, and deployable in real-world robotic applications."
    ],
    "durationSeconds": 6.804239075
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T01:45:46.644Z_

<details><summary>↩ Tool result · `toolu_012CetgonX9xkFTrxUVQmyc2`</summary>

```text
Web search results for query: "VLA action refinement correction flow matching robot manipulation 2025 2026 arXiv"

Links: [{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.14148v1"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://arxiv.org/html/2510.10274v1"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633"},{"title":"Universal Pose Pretraining for Generalizable Vision-Language-Action Policies","url":"https://arxiv.org/html/2602.19710v1"}]

The search results reveal several highly relevant papers on VLA (Vision-Language-Action) models with action refinement and flow matching for robot manipulation. Here are the key findings:

## Main Results:

1. **AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models** (November 2025)
   AsyncVLA breaks from vanilla SFM in VLA models by generating action tokens in a non-uniform time schedule with action context awareness, and introduces a confidence rater to extract confidence of initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution.

2. **Task Adaptation of Vision-Language-Action Model: 1st Place Solution for the 2025 BEHAVIOR Challenge** (December 2025)
   This work builds upon Pi0.5, a vision-language-action (VLA) model that uses flow matching to predict action sequences. It introduces System 2 stage tracking where the model predicts the current task stage with a voting mechanism to filter noisy predictions and maintain stable stage estimates, which is fused with task embeddings.

3. **Self-Correcting VLA: Online Action Refinement via Sparse World Imagination** (February 2026)
   This recent paper presents methods for online action refinement in VLA models using world imagination for robot manipulation tasks.

4. **Efficient VLA Architectures**
   Current VLA architectures typically employ a pre-trained LLM for high-level planning, which is then passed to a dedicated action expert module based on diffusion transformers, refining the plan and generating smooth, precise continuous actions through mechanisms such as flow matching.

These papers collectively address action refinement, correction mechanisms, and flow matching approaches in VLA models for robot manipulation during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "5a3d374a-2d6d-4536-8fbf-c44a528ca81e",
  "tool_use_result": {
    "query": "VLA action refinement correction flow matching robot manipulation 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VszGe18UdZR3zTg8tCbuYa",
        "content": [
          {
            "title": "Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/html/2512.06951v1"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/html/2508.13073v1"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v3"
          },
          {
            "title": "AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.14148v1"
          },
          {
            "title": "A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.24795v1"
          },
          {
            "title": "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2510.10274v1"
          },
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/html/2602.21633"
          },
          {
            "title": "Universal Pose Pretraining for Generalizable Vision-Language-Action Policies",
            "url": "https://arxiv.org/html/2602.19710v1"
          }
        ]
      },
      "The search results reveal several highly relevant papers on VLA (Vision-Language-Action) models with action refinement and flow matching for robot manipulation. Here are the key findings:\n\n## Main Results:\n\n1. **AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models** (November 2025)\n   AsyncVLA breaks from vanilla SFM in VLA models by generating action tokens in a non-uniform time schedule with action context awareness, and introduces a confidence rater to extract confidence of initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution.\n\n2. **Task Adaptation of Vision-Language-Action Model: 1st Place Solution for the 2025 BEHAVIOR Challenge** (December 2025)\n   This work builds upon Pi0.5, a vision-language-action (VLA) model that uses flow matching to predict action sequences. It introduces System 2 stage tracking where the model predicts the current task stage with a voting mechanism to filter noisy predictions and maintain stable stage estimates, which is fused with task embeddings.\n\n3. **Self-Correcting VLA: Online Action Refinement via Sparse World Imagination** (February 2026)\n   This recent paper presents methods for online action refinement in VLA models using world imagination for robot manipulation tasks.\n\n4. **Efficient VLA Architectures**\n   Current VLA architectures typically employ a pre-trained LLM for high-level planning, which is then passed to a dedicated action expert module based on diffusion transformers, refining the plan and generating smooth, precise continuous actions through mechanisms such as flow matching.\n\nThese papers collectively address action refinement, correction mechanisms, and flow matching approaches in VLA models for robot manipulation during 2025-2026."
    ],
    "durationSeconds": 8.014720629
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T01:45:47.824Z_

<details><summary>↩ Tool result · `toolu_0168S8SXkHBBadhs2XpUHLYQ`</summary>

```text
Web search results for query: "conformal prediction robotics action correction 2025 2026"

Links: [{"title":"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control","url":"https://arxiv.org/html/2603.10392v1"},{"title":"Learning Robot Safety from Sparse Human Feedback using Conformal Prediction","url":"https://arxiv.org/html/2501.04823"},{"title":"Formal Verification and Control With Conformal Prediction: Practical Safety Guarantees For Autonomous Systems | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/5488303/11274416/11274485.pdf"},{"title":"Conformal Prediction for Robotics | xLAB: Safe Autonomous Systems Lab","url":"https://xlab.upenn.edu/conformal-prediction-robotics/"},{"title":"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control","url":"https://jakeagonzales.github.io/crc-cbf-website/"},{"title":"Interaction-aware Conformal Prediction for Crowd Navigation","url":"https://arxiv.org/html/2502.06221"},{"title":"A Review of Theoretical Advances and Practical Applications of Conformal Prediction in China | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-15120-9_11"},{"title":"[2501.04823] Learning Robot Safety from Sparse Human Feedback using Conformal Prediction","url":"https://arxiv.org/abs/2501.04823"},{"title":"Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"},{"title":"End-to-End Conformal Prediction for Trajectory Optimization | OpenReview","url":"https://openreview.net/forum?id=ilcsm8B7Pe"}]

Based on the web search results, here's what I found about conformal prediction in robotics and action correction for 2025-2026:

## Recent Applications in Robotics

A novel probabilistic safe control framework combines control barrier functions (CBFs) with conformal risk control to provide formal safety guarantees while considering complex human behavior, using conformal risk control to quantify and control prediction errors in CBF safety values and establish formal guarantees on the probability of constraint satisfaction during interaction.

An algorithm dynamically adjusts the safety margins produced by conformal risk control based on the current interaction context, and experiments on human-robot navigation scenarios demonstrate that the approach significantly reduces collision rates and safety violations.

## Safety and Action Correction

From binary human feedback, conformal prediction is used to identify a region of states guaranteed to contain a user-specified fraction of future policy errors. One implementation involves modifying a model predictive control (MPC) policy to switch to a backup safety mode which steers to historical safe data when the MPC planned states are predicted to enter the unsafe region.

## Crowd Navigation and Interaction

Interaction-aware Conformal Prediction (ICP) alternates uncertainty-aware robot motion planning and decision-dependent human motion uncertainty quantification, composed of a trajectory predictor, a model predictive controller to plan robot motion with confidence intervals, a human simulator to collect calibration datasets, and a conformal prediction module to quantify trajectory prediction error.

## Recent Research Developments

Recent preprint work from 2026 includes "AdaptNC: Adaptive Nonconformity Scores for Uncertainty-Aware Autonomous Systems in Dynamic Environments," addressing the distribution shifts that arise in multi-agent settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "4be6f443-a686-4d75-b5d1-e55627b214c8",
  "tool_use_result": {
    "query": "conformal prediction robotics action correction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QNNfMnKPxqxkNfM3sHLipM",
        "content": [
          {
            "title": "Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control",
            "url": "https://arxiv.org/html/2603.10392v1"
          },
          {
            "title": "Learning Robot Safety from Sparse Human Feedback using Conformal Prediction",
            "url": "https://arxiv.org/html/2501.04823"
          },
          {
            "title": "Formal Verification and Control With Conformal Prediction: Practical Safety Guarantees For Autonomous Systems | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/iel8/5488303/11274416/11274485.pdf"
          },
          {
            "title": "Conformal Prediction for Robotics | xLAB: Safe Autonomous Systems Lab",
            "url": "https://xlab.upenn.edu/conformal-prediction-robotics/"
          },
          {
            "title": "Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control",
            "url": "https://jakeagonzales.github.io/crc-cbf-website/"
          },
          {
            "title": "Interaction-aware Conformal Prediction for Crowd Navigation",
            "url": "https://arxiv.org/html/2502.06221"
          },
          {
            "title": "A Review of Theoretical Advances and Practical Applications of Conformal Prediction in China | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-15120-9_11"
          },
          {
            "title": "[2501.04823] Learning Robot Safety from Sparse Human Feedback using Conformal Prediction",
            "url": "https://arxiv.org/abs/2501.04823"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"
          },
          {
            "title": "End-to-End Conformal Prediction for Trajectory Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=ilcsm8B7Pe"
          }
        ]
      },
      "Based on the web search results, here's what I found about conformal prediction in robotics and action correction for 2025-2026:\n\n## Recent Applications in Robotics\n\nA novel probabilistic safe control framework combines control barrier functions (CBFs) with conformal risk control to provide formal safety guarantees while considering complex human behavior, using conformal risk control to quantify and control prediction errors in CBF safety values and establish formal guarantees on the probability of constraint satisfaction during interaction.\n\nAn algorithm dynamically adjusts the safety margins produced by conformal risk control based on the current interaction context, and experiments on human-robot navigation scenarios demonstrate that the approach significantly reduces collision rates and safety violations.\n\n## Safety and Action Correction\n\nFrom binary human feedback, conformal prediction is used to identify a region of states guaranteed to contain a user-specified fraction of future policy errors. One implementation involves modifying a model predictive control (MPC) policy to switch to a backup safety mode which steers to historical safe data when the MPC planned states are predicted to enter the unsafe region.\n\n## Crowd Navigation and Interaction\n\nInteraction-aware Conformal Prediction (ICP) alternates uncertainty-aware robot motion planning and decision-dependent human motion uncertainty quantification, composed of a trajectory predictor, a model predictive controller to plan robot motion with confidence intervals, a human simulator to collect calibration datasets, and a conformal prediction module to quantify trajectory prediction error.\n\n## Recent Research Developments\n\nRecent preprint work from 2026 includes \"AdaptNC: Adaptive Nonconformity Scores for Uncertainty-Aware Autonomous Systems in Dynamic Environments,\" addressing the distribution shifts that arise in multi-agent settings."
    ],
    "durationSeconds": 8.257827894000002
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T01:45:47.844Z_

<details><summary>↩ Tool result · `toolu_01T9vxY7buhyX29tAVWMrtit`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021: 撤销 D011，重新瞄准 CoRL 2026\\n- ~~ICLR 2027~~ — 不再是首要目标\\n\\n## Core Insight\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\"which action dimensions are uncertain and how they co-vary\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\n\\n## Core Claims (3 条，均可证伪)\\n1. **Per-DOF conformal features enable dimension-selective correction**: CGS 提取的 40D 结构化 uncertainty 特征（per-DOF std + conformal radius + ellipsoid volume，action_dim=6, H_eff=5）比标量 uncertainty（ReconVLA 的 Euclidean distance）和无 uncertainty conditioning 的残差策略（A2C2 类）提供显著更好的 action correction。\\n   - 验证: MVP (✅ done) + A3 ablation (make-or-break) + A4 ablation + feature importance analysis\\n   - Kill criterion: A3 (CRM without conformal features) 与 full ACR-VLA 差距 <2% → claim 不成立\\n\\n2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。\\n   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static\\n   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI\\n\\n3. **ACR-VLA 与 training-time 方法正交互补**: 作为 inference-time 模块可叠加在 SRPO (82.1% LIBERO-Plus SOTA) 上进一步提升。\\n   - 验证: ACR-VLA + SRPO > SRPO alone\\n   - Kill criterion: stacking gain < 2% → claim 降级为\\\"complementary in principle\\\"\\n\\n## Story Spine\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\n- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作；SC-VLA 通过 sparse world imagination + residual RL 在线纠正，但需要任务级 RL 训练且无统计保证，纠正作用在全局 action vector 上无维度选择性；VLA-Pilot 用 MLLM 做开放世界 action scoring + evolutionary search，推理延迟 2.41s/step 且依赖启发式评分无 calibrated confidence。Training-time 方面，ACoT-VLA 通过 action chain-of-thought 达到 LIBERO-Plus 84.1% SOTA，但属于静态训练方法，部署后无法在线适应分布偏移。所有现有方法均未将 per-DOF conformal statistics 作为 learned correction 的输入特征。\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\"哪些维度不确定+跨维度协方差\\\"，使 CRM 能做维度选择性校正。\\n- **Headline result template**: \\\"On LIBERO-Plus, ACR-VLA improves base VLA success by X%, and when stacked on SRPO (82.1%), achieves Y% — demonstrating that inference-time conformal correction provides orthogonal value beyond training-time optimization.\\\"\\n\\n## Competitive Landscape\\n\\n### ReconVLA — 最直接竞品\\nPost-hoc conformal prediction on frozen VLA（理念最接近 ACR-VLA）。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\n\\n**关键差异**：(1) Scalar CQR aggregation 丢失维度信息，无法区分 \\\"哪个关节不确定\\\"；(2) Sample selection 而非 learned correction——当 K 个样本都不好时 selection 失效；(3) Static calibration set 不做在线适应，distribution shift 下 coverage 退化。ACR-VLA 在 UQ 粒度（40D vs scalar）、纠正策略（CRM synthesis vs selection）、在线适应（ACI+COC vs static）三个维度均更进一步。\\n\\n### SC-VLA — Inference-time RL refinement\\nSparse World Imagination (SPI) + Online Action Refinement (OAR)。在 VLA backbone 上附加辅助预测头预测任务进度和未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线调整动作。ManiSkill 平均 86%，+9% SR。\\n\\n**关键差异**：(1) 需要任务级 RL 训练（residual policy + auxiliary heads），非 plug-and-play；(2) 无统计保证和不确定性量化；(3) Residual 作用在整个 action vector 上，无维度选择性；(4) 未在 LIBERO-Plus 评估。ACR-VLA 的 SampleConsensus baseline 近似模拟此方法的 sample consensus 思路。\\n\\n### VLA-Pilot — MLLM-guided steering\\nMLLM verifier + evolutionary diffusion optimizer，三阶段 inference-time steering。利用 VLM 开放世界推理能力做 action scoring。OOD 场景成功率 0.50 vs baseline 0.12-0.19。\\n\\n**关键差异**：(1) 推理延迟 2.41s/step，不适合实时控制；(2) 依赖 MLLM 质量，scoring 为启发式方法无 calibrated confidence；(3) 无统计保证；(4) 未在 LIBERO 标准 benchmark 评估。优势在 zero-shot OOD 泛化（靠 MLLM 开放世界知识）。\\n\\n### ACoT-VLA — Training-time SOTA (CVPR 2026)\\nAction Chain-of-Thought：EAR (Explicit Action Reasoner) 生成粗粒度参考轨迹 + IAR (Implicit Action Reasoner) 提取 latent action priors，联合训练引导 action head。LIBERO 98.5%，LIBERO-Plus 84.1%（当前 SOTA 之一）。\\n\\n**关键差异**：(1) Training-time 方法，需在目标任务上训练 EAR+IAR；(2) 无不确定性量化，无法识别何时 \\\"不确定\\\"；(3) 静态模型，部署后不在线适应。**与 ACR-VLA 正交互补**——ACoT 增强 VLA 基础能力，ACR-VLA 在其之上提供 inference-time statistical safety net。\\n\\n### ACR-VLA 差异化定位\\n唯一将 multivariate conformal statistics（per-DOF intervals + ellipsoid volume + cross-DOF covariance structure）作为 learned correction module (CRM) 直接输入特征的方法。核心差异化组合：**Per-DOF statistical guarantees + Learned dimension-selective correction + Online coverage adaptation**——三者缺一不可，现有方法均未同时具备。\\n\\n## Anticipated Reviewer Concerns\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\n7. **[Dream 新增] \\\"Conformal\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\"conformal-feature-conditioned correction\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\n\\n## Framing 备选策略（基于 Dream median 观察）\\n如果 per-DOF 优势 < 5%：story 重心从 \\\"per-DOF > scalar\\\" 转向 \\\"structured uncertainty features enable principled correction\\\"（包含 per-DOF + ACI + COC 的完整框架优势）。Core Insight 和 Claim 1 措辞需相应调整。\\n\", \"total_chars\": 6063, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "a3adece1-fb9b-4069-aae2-4e9e4fe9e7f0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — acr-vla-conformal-refinement\\\\n\\\\n## Target Venue\\\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021: 撤销 D011，重新瞄准 CoRL 2026\\\\n- ~~ICLR 2027~~ — 不再是首要目标\\\\n\\\\n## Core Insight\\\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\\\\\"which action dimensions are uncertain and how they co-vary\\\\\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\\\n\\\\n## Core Claims (3 条，均可证伪)\\\\n1. **Per-DOF conformal features enable dimension-selective correction**: CGS 提取的 40D 结构化 uncertainty 特征（per-DOF std + conformal radius + ellipsoid volume，action_dim=6, H_eff=5）比标量 uncertainty（ReconVLA 的 Euclidean distance）和无 uncertainty conditioning 的残差策略（A2C2 类）提供显著更好的 action correction。\\\\n   - 验证: MVP (✅ done) + A3 ablation (make-or-break) + A4 ablation + feature importance analysis\\\\n   - Kill criterion: A3 (CRM without conformal features) 与 full ACR-VLA 差距 <2% → claim 不成立\\\\n\\\\n2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。\\\\n   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static\\\\n   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI\\\\n\\\\n3. **ACR-VLA 与 training-time 方法正交互补**: 作为 inference-time 模块可叠加在 SRPO (82.1% LIBERO-Plus SOTA) 上进一步提升。\\\\n   - 验证: ACR-VLA + SRPO > SRPO alone\\\\n   - Kill criterion: stacking gain < 2% → claim 降级为\\\\\\\"complementary in principle\\\\\\\"\\\\n\\\\n## Story Spine\\\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\\\n- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作；SC-VLA 通过 sparse world imagination + residual RL 在线纠正，但需要任务级 RL 训练且无统计保证，纠正作用在全局 action vector 上无维度选择性；VLA-Pilot 用 MLLM 做开放世界 action scoring + evolutionary search，推理延迟 2.41s/step 且依赖启发式评分无 calibrated confidence。Training-time 方面，ACoT-VLA 通过 action chain-of-thought 达到 LIBERO-Plus 84.1% SOTA，但属于静态训练方法，部署后无法在线适应分布偏移。所有现有方法均未将 per-DOF conformal statistics 作为 learned correction 的输入特征。\\\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\\\\\"哪些维度不确定+跨维度协方差\\\\\\\"，使 CRM 能做维度选择性校正。\\\\n- **Headline result template**: \\\\\\\"On LIBERO-Plus, ACR-VLA improves base VLA success by X%, and when stacked on SRPO (82.1%), achieves Y% — demonstrating that inference-time conformal correction provides orthogonal value beyond training-time optimization.\\\\\\\"\\\\n\\\\n## Competitive Landscape\\\\n\\\\n### ReconVLA — 最直接竞品\\\\nPost-hoc conformal prediction on frozen VLA（理念最接近 ACR-VLA）。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\\\n\\\\n**关键差异**：(1) Scalar CQR aggregation 丢失维度信息，无法区分 \\\\\\\"哪个关节不确定\\\\\\\"；(2) Sample selection 而非 learned correction——当 K 个样本都不好时 selection 失效；(3) Static calibration set 不做在线适应，distribution shift 下 coverage 退化。ACR-VLA 在 UQ 粒度（40D vs scalar）、纠正策略（CRM synthesis vs selection）、在线适应（ACI+COC vs static）三个维度均更进一步。\\\\n\\\\n### SC-VLA — Inference-time RL refinement\\\\nSparse World Imagination (SPI) + Online Action Refinement (OAR)。在 VLA backbone 上附加辅助预测头预测任务进度和未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线调整动作。ManiSkill 平均 86%，+9% SR。\\\\n\\\\n**关键差异**：(1) 需要任务级 RL 训练（residual policy + auxiliary heads），非 plug-and-play；(2) 无统计保证和不确定性量化；(3) Residual 作用在整个 action vector 上，无维度选择性；(4) 未在 LIBERO-Plus 评估。ACR-VLA 的 SampleConsensus baseline 近似模拟此方法的 sample consensus 思路。\\\\n\\\\n### VLA-Pilot — MLLM-guided steering\\\\nMLLM verifier + evolutionary diffusion optimizer，三阶段 inference-time steering。利用 VLM 开放世界推理能力做 action scoring。OOD 场景成功率 0.50 vs baseline 0.12-0.19。\\\\n\\\\n**关键差异**：(1) 推理延迟 2.41s/step，不适合实时控制；(2) 依赖 MLLM 质量，scoring 为启发式方法无 calibrated confidence；(3) 无统计保证；(4) 未在 LIBERO 标准 benchmark 评估。优势在 zero-shot OOD 泛化（靠 MLLM 开放世界知识）。\\\\n\\\\n### ACoT-VLA — Training-time SOTA (CVPR 2026)\\\\nAction Chain-of-Thought：EAR (Explicit Action Reasoner) 生成粗粒度参考轨迹 + IAR (Implicit Action Reasoner) 提取 latent action priors，联合训练引导 action head。LIBERO 98.5%，LIBERO-Plus 84.1%（当前 SOTA 之一）。\\\\n\\\\n**关键差异**：(1) Training-time 方法，需在目标任务上训练 EAR+IAR；(2) 无不确定性量化，无法识别何时 \\\\\\\"不确定\\\\\\\"；(3) 静态模型，部署后不在线适应。**与 ACR-VLA 正交互补**——ACoT 增强 VLA 基础能力，ACR-VLA 在其之上提供 inference-time statistical safety net。\\\\n\\\\n### ACR-VLA 差异化定位\\\\n唯一将 multivariate conformal statistics（per-DOF intervals + ellipsoid volume + cross-DOF covariance structure）作为 learned correction module (CRM) 直接输入特征的方法。核心差异化组合：**Per-DOF statistical guarantees + Learned dimension-selective correction + Online coverage adaptation**——三者缺一不可，现有方法均未同时具备。\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\\\n7. **[Dream 新增] \\\\\\\"Conformal\\\\\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\\\\\"conformal-feature-conditioned correction\\\\\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\\\n\\\\n## Framing 备选策略（基于 Dream median 观察）\\\\n如果 per-DOF 优势 < 5%：story 重心从 \\\\\\\"per-DOF > scalar\\\\\\\" 转向 \\\\\\\"structured uncertainty features enable principled correction\\\\\\\"（包含 per-DOF + ACI + COC 的完整框架优势）。Core Insight 和 Claim 1 措辞需相应调整。\\\\n\\\", \\\"total_chars\\\": 6063, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021: 撤销 D011，重新瞄准 CoRL 2026\\n- ~~ICLR 2027~~ — 不再是首要目标\\n\\n## Core Insight\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\"which action dimensions are uncertain and how they co-vary\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\n\\n## Core Claims (3 条，均可证伪)\\n1. **Per-DOF conformal features enable dimension-selective correction**: CGS 提取的 40D 结构化 uncertainty 特征（per-DOF std + conformal radius + ellipsoid volume，action_dim=6, H_eff=5）比标量 uncertainty（ReconVLA 的 Euclidean distance）和无 uncertainty conditioning 的残差策略（A2C2 类）提供显著更好的 action correction。\\n   - 验证: MVP (✅ done) + A3 ablation (make-or-break) + A4 ablation + feature importance analysis\\n   - Kill criterion: A3 (CRM without conformal features) 与 full ACR-VLA 差距 <2% → claim 不成立\\n\\n2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。\\n   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static\\n   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI\\n\\n3. **ACR-VLA 与 training-time 方法正交互补**: 作为 inference-time 模块可叠加在 SRPO (82.1% LIBERO-Plus SOTA) 上进一步提升。\\n   - 验证: ACR-VLA + SRPO > SRPO alone\\n   - Kill criterion: stacking gain < 2% → claim 降级为\\\"complementary in principle\\\"\\n\\n## Story Spine\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\n- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作；SC-VLA 通过 sparse world imagination + residual RL 在线纠正，但需要任务级 RL 训练且无统计保证，纠正作用在全局 action vector 上无维度选择性；VLA-Pilot 用 MLLM 做开放世界 action scoring + evolutionary search，推理延迟 2.41s/step 且依赖启发式评分无 calibrated confidence。Training-time 方面，ACoT-VLA 通过 action chain-of-thought 达到 LIBERO-Plus 84.1% SOTA，但属于静态训练方法，部署后无法在线适应分布偏移。所有现有方法均未将 per-DOF conformal statistics 作为 learned correction 的输入特征。\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\"哪些维度不确定+跨维度协方差\\\"，使 CRM 能做维度选择性校正。\\n- **Headline result template**: \\\"On LIBERO-Plus, ACR-VLA improves base VLA success by X%, and when stacked on SRPO (82.1%), achieves Y% — demonstrating that inference-time conformal correction provides orthogonal value beyond training-time optimization.\\\"\\n\\n## Competitive Landscape\\n\\n### ReconVLA — 最直接竞品\\nPost-hoc conformal prediction on frozen VLA（理念最接近 ACR-VLA）。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\n\\n**关键差异**：(1) Scalar CQR aggregation 丢失维度信息，无法区分 \\\"哪个关节不确定\\\"；(2) Sample selection 而非 learned correction——当 K 个样本都不好时 selection 失效；(3) Static calibration set 不做在线适应，distribution shift 下 coverage 退化。ACR-VLA 在 UQ 粒度（40D vs scalar）、纠正策略（CRM synthesis vs selection）、在线适应（ACI+COC vs static）三个维度均更进一步。\\n\\n### SC-VLA — Inference-time RL refinement\\nSparse World Imagination (SPI) + Online Action Refinement (OAR)。在 VLA backbone 上附加辅助预测头预测任务进度和未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线调整动作。ManiSkill 平均 86%，+9% SR。\\n\\n**关键差异**：(1) 需要任务级 RL 训练（residual policy + auxiliary heads），非 plug-and-play；(2) 无统计保证和不确定性量化；(3) Residual 作用在整个 action vector 上，无维度选择性；(4) 未在 LIBERO-Plus 评估。ACR-VLA 的 SampleConsensus baseline 近似模拟此方法的 sample consensus 思路。\\n\\n### VLA-Pilot — MLLM-guided steering\\nMLLM verifier + evolutionary diffusion optimizer，三阶段 inference-time steering。利用 VLM 开放世界推理能力做 action scoring。OOD 场景成功率 0.50 vs baseline 0.12-0.19。\\n\\n**关键差异**：(1) 推理延迟 2.41s/step，不适合实时控制；(2) 依赖 MLLM 质量，scoring 为启发式方法无 calibrated confidence；(3) 无统计保证；(4) 未在 LIBERO 标准 benchmark 评估。优势在 zero-shot OOD 泛化（靠 MLLM 开放世界知识）。\\n\\n### ACoT-VLA — Training-time SOTA (CVPR 2026)\\nAction Chain-of-Thought：EAR (Explicit Action Reasoner) 生成粗粒度参考轨迹 + IAR (Implicit Action Reasoner) 提取 latent action priors，联合训练引导 action head。LIBERO 98.5%，LIBERO-Plus 84.1%（当前 SOTA 之一）。\\n\\n**关键差异**：(1) Training-time 方法，需在目标任务上训练 EAR+IAR；(2) 无不确定性量化，无法识别何时 \\\"不确定\\\"；(3) 静态模型，部署后不在线适应。**与 ACR-VLA 正交互补**——ACoT 增强 VLA 基础能力，ACR-VLA 在其之上提供 inference-time statistical safety net。\\n\\n### ACR-VLA 差异化定位\\n唯一将 multivariate conformal statistics（per-DOF intervals + ellipsoid volume + cross-DOF covariance structure）作为 learned correction module (CRM) 直接输入特征的方法。核心差异化组合：**Per-DOF statistical guarantees + Learned dimension-selective correction + Online coverage adaptation**——三者缺一不可，现有方法均未同时具备。\\n\\n## Anticipated Reviewer Concerns\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\n7. **[Dream 新增] \\\"Conformal\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\"conformal-feature-conditioned correction\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\n\\n## Framing 备选策略（基于 Dream median 观察）\\n如果 per-DOF 优势 < 5%：story 重心从 \\\"per-DOF > scalar\\\" 转向 \\\"structured uncertainty features enable principled correction\\\"（包含 per-DOF + ACI + COC 的完整框架优势）。Core Insight 和 Claim 1 措辞需相应调整。\\n\", \"total_chars\": 6063, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T01:45:47.859Z_

<details><summary>↩ Tool result · `toolu_01LQY9m3wCKVMG3Xiyg1r8CK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2410.24164\\\"\\n    url: \\\"https://arxiv.org/abs/2410.24164\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"braun2025cgs\\\"\\n    title: \\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\"\\n    authors: \\\"Braun et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.20941\\\"\\n    url: \\\"https://arxiv.org/abs/2507.20941\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"brohan2023rt2\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv:2307.15818\\\"\\n    url: \\\"https://arxiv.org/abs/2307.15818\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chen2026reconvla\\\"\\n    title: \\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\"\\n    authors: \\\"Chen et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.16677\\\"\\n    url: \\\"https://arxiv.org/abs/2604.16677\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"digflow2025\\\"\\n    title: \\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.01715\\\"\\n    url: \\\"https://arxiv.org/abs/2512.01715\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"fei2025liberoplus\\\"\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.13626\\\"\\n    url: \\\"https://arxiv.org/abs/2510.13626\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"ghosh2024octo\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Ghosh et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2405.12213\\\"\\n    url: \\\"https://arxiv.org/abs/2405.12213\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gibbs2021aci\\\"\\n    title: \\\"Adaptive Conformal Inference Under Distribution Shift\\\"\\n    authors: \\\"Gibbs & Candès\\\"\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://arxiv.org/abs/2106.00170\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"gu2025safe\\\"\\n    title: \\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\"\\n    authors: \\\"Gu et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09937\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"kim2024openvla\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2406.09246\\\"\\n    url: \\\"https://arxiv.org/abs/2406.09246\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"ledoit2004well\\\"\\n    title: \\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\"\\n    authors: \\\"Ledoit & Wolf\\\"\\n    year: 2004\\n    venue: \\\"Journal of Multivariate Analysis, 88(2):365-411\\\"\\n    url: \\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lipman2023flow\\\"\\n    title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Lipman et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.02747\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2023libero\\\"\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2306.03310\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2026ttvla\\\"\\n    title: \\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.06748\\\"\\n    url: \\\"https://arxiv.org/abs/2601.06748\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"luan2026snapflow\\\"\\n    title: \\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\"\\n    authors: \\\"Luan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.05656\\\"\\n    url: \\\"https://arxiv.org/abs/2604.05656\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"robustvla2025\\\"\\n    title: \\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.01331\\\"\\n    url: \\\"https://arxiv.org/abs/2511.01331\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"romano2019cqr\\\"\\n    title: \\\"Conformalized Quantile Regression\\\"\\n    authors: \\\"Romano et al.\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1905.03222\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shafer2008tutorial\\\"\\n    title: \\\"A Tutorial on Conformal Prediction\\\"\\n    authors: \\\"Shafer & Vovk\\\"\\n    year: 2008\\n    venue: \\\"Journal of Machine Learning Research, 9:371-421\\\"\\n    url: \\\"https://jmlr.org/papers/v9/shafer08a.html\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shukor2025smolvla\\\"\\n    title: \\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\"\\n    authors: \\\"Shukor et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2506.01844\\\"\\n    url: \\\"https://arxiv.org/abs/2506.01844\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"srpo2025\\\"\\n    title: \\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.15605\\\"\\n    url: \\\"https://arxiv.org/abs/2511.15605\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"wang2025cploop\\\"\\n    title: \\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\"\\n    authors: \\\"Wang & Ning\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.16376\\\"\\n    url: \\\"https://arxiv.org/abs/2510.16376\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"xing2026diu\\\"\\n    title: \\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\"\\n    authors: \\\"Xing et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.00941\\\"\\n    url: \\\"https://arxiv.org/abs/2605.00941\\\"\\n    category: \\\"uq_flow_matching\\\"\\n    verified: true\\n    relevance: \\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"yuan2026ups\\\"\\n    title: \\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\"\\n    authors: \\\"Yuan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.22474\\\"\\n    url: \\\"https://arxiv.org/abs/2602.22474\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"zhao2024conformalized\\\"\\n    title: \\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\"\\n    authors: \\\"Zhao et al.\\\"\\n    year: 2024\\n    venue: \\\"RSS 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2406.07767\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"cosmos_policy_2026\\\"\\n    title: \\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.16163\\\"\\n    url: \\\"https://arxiv.org/abs/2601.16163\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"vla_gse_2026\\\"\\n    title: \\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.06175\\\"\\n    url: \\\"https://arxiv.org/abs/2605.06175\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lakshminarayanan2017ensembles\\\"\\n    title: \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\"\\n    authors: \\\"Lakshminarayanan et al.\\\"\\n    year: 2017\\n    venue: \\\"NeurIPS 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1612.01474\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gal2016dropout\\\"\\n    title: \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\"\\n    authors: \\\"Gal & Ghahramani\\\"\\n    year: 2016\\n    venue: \\\"ICML 2016\\\"\\n    url: \\\"https://arxiv.org/abs/1506.02142\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chi2023diffusion_policy\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: \\\"RSS 2023 / IJRR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2303.04137\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: false\\n    verification_note: \\\"Well-known paper, needs URL reachability confirmation\\\"\\n    relevance: \\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\"\\n    must_cite: true\\n\\n  # ===== New entries added 2026-05-14 =====\\n\\n  - bibtex_key: \\\"fan2025interpretable_mcp\\\"\\n    title: \\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\"\\n    authors: \\\"Fan & Sesia\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.15383\\\"\\n    url: \\\"https://arxiv.org/abs/2512.15383\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"klein2025otcp\\\"\\n    title: \\\"Multivariate Conformal Prediction using Optimal Transport\\\"\\n    authors: \\\"Klein, Bethune, Ndiaye & Cuturi\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2502.03609\\\"\\n    url: \\\"https://arxiv.org/abs/2502.03609\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"zollo2025vla_calibration\\\"\\n    title: \\\"Confidence Calibration in Vision-Language-Action Models\\\"\\n    authors: \\\"Zollo & Zemel\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17383\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17383\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\"\\n    must_cite: true\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"tang2026shifting_uncertainty\\\"\\n    title: \\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\"\\n    authors: \\\"Tang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2603.18342\\\"\\n    url: \\\"https://arxiv.org/abs/2603.18342\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lcp2025\\\"\\n    title: \\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.21955\\\"\\n    url: \\\"https://arxiv.org/abs/2509.21955\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"claps2025\\\"\\n    title: \\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.10294\\\"\\n    url: \\\"https://arxiv.org/abs/2512.10294\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lucca2024\\\"\\n    title: \\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\"\\n    authors: \\\"Marques et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2409.08249\\\"\\n    url: \\\"https://arxiv.org/abs/2409.08249\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"sc_vla_2026\\\"\\n    title: \\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.21633\\\"\\n    url: \\\"https://arxiv.org/abs/2602.21633\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"vla_pilot_2025\\\"\\n    title: \\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.14178\\\"\\n    url: \\\"https://arxiv.org/abs/2511.14178\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"acot_vla_2026\\\"\\n    title: \\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\"\\n    authors: \\\"AgibotTech\\\"\\n    year: 2026\\n    venue: \\\"CVPR 2026, arXiv:2601.11404\\\"\\n    url: \\\"https://arxiv.org/abs/2601.11404\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"gonzales2026crc_cbf\\\"\\n    title: \\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\"\\n    authors: \\\"Gonzales et al.\\\"\\n    year: 2026\\n    venue: \\\"IROS 2025, arXiv:2603.10392\\\"\\n    url: \\\"https://arxiv.org/abs/2603.10392\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"safediffcon2025\\\"\\n    title: \\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025, arXiv:2502.02205\\\"\\n    url: \\\"https://arxiv.org/abs/2502.02205\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"afil2026\\\"\\n    title: \\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.08434\\\"\\n    url: \\\"https://arxiv.org/abs/2605.08434\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"valle2025vla_uq_metrics\\\"\\n    title: \\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\"\\n    authors: \\\"Valle et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17049\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17049\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"diffusionvla2024\\\"\\n    title: \\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\"\\n    authors: \\\"Wen et al.\\\"\\n    year: 2024\\n    venue: \\\"ICML 2025, arXiv:2412.03293\\\"\\n    url: \\\"https://arxiv.org/abs/2412.03293\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\\n\\n  - bibtex_key: \\\"silver2018residual\\\"\\n    title: \\\"Residual Policy Learning\\\"\\n    authors: \\\"Silver et al.\\\"\\n    year: 2018\\n    venue: \\\"RSS 2018\\\"\\n    url: \\\"https://arxiv.org/abs/1812.06298\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\\\"\\n    must_cite: true\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"johannink2019residual\\\"\\n    title: \\\"Residual Reinforcement Learning for Robot Manipulator Control\\\"\\n    authors: \\\"Johannink et al.\\\"\\n    year: 2019\\n    venue: \\\"ICRA 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1812.03201\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"jiang2024transic\\\"\\n    title: \\\"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2405.10315\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"ankile2024resip\\\"\\n    title: \\\"ResiP: Residual Reinforcement Learning for Precise Assembly\\\"\\n    authors: \\\"Ankile et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL Workshop 2024\\\"\\n    url: \\\"\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: false\\n    verification_note: \\\"Workshop paper, no arXiv ID provided\\\"\\n    relevance: \\\"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"xiao2026pld\\\"\\n    title: \\\"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\\\"\\n    authors: \\\"Xiao et al.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2511.00091\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"pan2025drc\\\"\\n    title: \\\"DRC: Decaying Relative Correction for Policy Refinement\\\"\\n    authors: \\\"Pan et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2503.15368\\\"\\n    url: \\\"https://arxiv.org/abs/2503.15368\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"ma2026dawn\\\"\\n    title: \\\"DAWN: Value Learning in Residual Reinforcement Learning\\\"\\n    authors: \\\"Ma et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.10539\\\"\\n    url: \\\"https://arxiv.org/abs/2602.10539\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"vla_in_the_loop_2025\\\"\\n    title: \\\"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: false\\n    verification_note: \\\"No arXiv ID provided, needs verification\\\"\\n    relevance: \\\"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"zhou2025acp_cbf\\\"\\n    title: \\\"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\\\"\\n    authors: \\\"Zhou et al.\\\"\\n    year: 2025\\n    venue: \\\"ICRA 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.17678\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"method-component\\\"\\n\", \"total_chars\": 29225, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "e49be697-cfdc-4778-8891-e8a783c2ae48",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  - bibtex_key: \\\\\\\"a2c2_2025\\\\\\\"\\\\n    title: \\\\\\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\\\\\"\\\\n    authors: \\\\\\\"Sendai et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2509.23224\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.23224\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"angelopoulos2023gentle\\\\\\\"\\\\n    title: \\\\\\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\\\\\"\\\\n    authors: \\\\\\\"Angelopoulos & Bates\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Foundations and Trends in Machine Learning\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2107.07511\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"barber2023conformal\\\\\\\"\\\\n    title: \\\\\\\"Conformal Prediction Beyond Exchangeability\\\\\\\"\\\\n    authors: \\\\\\\"Barber et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Annals of Statistics, 51(2):816-845\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2202.13415\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"black2024pi0\\\\\\\"\\\\n    title: \\\\\\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\\\\\"\\\\n    authors: \\\\\\\"Black et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2410.24164\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.24164\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"braun2025cgs\\\\\\\"\\\\n    title: \\\\\\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\\\\\"\\\\n    authors: \\\\\\\"Braun et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.20941\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.20941\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"brohan2023rt2\\\\\\\"\\\\n    title: \\\\\\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Brohan et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv:2307.15818\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2307.15818\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"chen2026reconvla\\\\\\\"\\\\n    title: \\\\\\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Chen et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2604.16677\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.16677\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"digflow2025\\\\\\\"\\\\n    title: \\\\\\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.01715\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.01715\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"fei2025liberoplus\\\\\\\"\\\\n    title: \\\\\\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Fei et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2510.13626\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.13626\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"ghosh2024octo\\\\\\\"\\\\n    title: \\\\\\\"Octo: An Open-Source Generalist Robot Policy\\\\\\\"\\\\n    authors: \\\\\\\"Ghosh et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2405.12213\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2405.12213\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"gibbs2021aci\\\\\\\"\\\\n    title: \\\\\\\"Adaptive Conformal Inference Under Distribution Shift\\\\\\\"\\\\n    authors: \\\\\\\"Gibbs & Candès\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"NeurIPS 2021\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2106.00170\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"gu2025safe\\\\\\\"\\\\n    title: \\\\\\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Gu et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.09937\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"kim2024openvla\\\\\\\"\\\\n    title: \\\\\\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2406.09246\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.09246\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"ledoit2004well\\\\\\\"\\\\n    title: \\\\\\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\\\\\"\\\\n    authors: \\\\\\\"Ledoit & Wolf\\\\\\\"\\\\n    year: 2004\\\\n    venue: \\\\\\\"Journal of Multivariate Analysis, 88(2):365-411\\\\\\\"\\\\n    url: \\\\\\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"lipman2023flow\\\\\\\"\\\\n    title: \\\\\\\"Flow Matching for Generative Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Lipman et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"ICLR 2023\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2210.02747\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"liu2023libero\\\\\\\"\\\\n    title: \\\\\\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2306.03310\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"liu2026ttvla\\\\\\\"\\\\n    title: \\\\\\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2601.06748\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.06748\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"luan2026snapflow\\\\\\\"\\\\n    title: \\\\\\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\\\\\"\\\\n    authors: \\\\\\\"Luan et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2604.05656\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.05656\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"robustvla2025\\\\\\\"\\\\n    title: \\\\\\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.01331\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.01331\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"romano2019cqr\\\\\\\"\\\\n    title: \\\\\\\"Conformalized Quantile Regression\\\\\\\"\\\\n    authors: \\\\\\\"Romano et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"NeurIPS 2019\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1905.03222\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"shafer2008tutorial\\\\\\\"\\\\n    title: \\\\\\\"A Tutorial on Conformal Prediction\\\\\\\"\\\\n    authors: \\\\\\\"Shafer & Vovk\\\\\\\"\\\\n    year: 2008\\\\n    venue: \\\\\\\"Journal of Machine Learning Research, 9:371-421\\\\\\\"\\\\n    url: \\\\\\\"https://jmlr.org/papers/v9/shafer08a.html\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"shukor2025smolvla\\\\\\\"\\\\n    title: \\\\\\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\\\\\"\\\\n    authors: \\\\\\\"Shukor et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2506.01844\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.01844\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"srpo2025\\\\\\\"\\\\n    title: \\\\\\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Fei et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.15605\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.15605\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"wang2025cploop\\\\\\\"\\\\n    title: \\\\\\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Wang & Ning\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2510.16376\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.16376\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"xing2026diu\\\\\\\"\\\\n    title: \\\\\\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\\\\\"\\\\n    authors: \\\\\\\"Xing et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.00941\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.00941\\\\\\\"\\\\n    category: \\\\\\\"uq_flow_matching\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"yuan2026ups\\\\\\\"\\\\n    title: \\\\\\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\\\\\"\\\\n    authors: \\\\\\\"Yuan et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.22474\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.22474\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"zhao2024conformalized\\\\\\\"\\\\n    title: \\\\\\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\\\\\"\\\\n    authors: \\\\\\\"Zhao et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"RSS 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.07767\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"cosmos_policy_2026\\\\\\\"\\\\n    title: \\\\\\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2601.16163\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.16163\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_gse_2026\\\\\\\"\\\\n    title: \\\\\\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\\\\\"\\\\n    authors: \\\\\\\"Jiang et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.06175\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.06175\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"lakshminarayanan2017ensembles\\\\\\\"\\\\n    title: \\\\\\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\\\\\"\\\\n    authors: \\\\\\\"Lakshminarayanan et al.\\\\\\\"\\\\n    year: 2017\\\\n    venue: \\\\\\\"NeurIPS 2017\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1612.01474\\\\\\\"\\\\n    category: \\\\\\\"uq_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"gal2016dropout\\\\\\\"\\\\n    title: \\\\\\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\\\\\"\\\\n    authors: \\\\\\\"Gal & Ghahramani\\\\\\\"\\\\n    year: 2016\\\\n    venue: \\\\\\\"ICML 2016\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1506.02142\\\\\\\"\\\\n    category: \\\\\\\"uq_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"chi2023diffusion_policy\\\\\\\"\\\\n    title: \\\\\\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\\\\\"\\\\n    authors: \\\\\\\"Chi et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"RSS 2023 / IJRR 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2303.04137\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: false\\\\n    verification_note: \\\\\\\"Well-known paper, needs URL reachability confirmation\\\\\\\"\\\\n    relevance: \\\\\\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  # ===== New entries added 2026-05-14 =====\\\\n\\\\n  - bibtex_key: \\\\\\\"fan2025interpretable_mcp\\\\\\\"\\\\n    title: \\\\\\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\\\\\"\\\\n    authors: \\\\\\\"Fan & Sesia\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.15383\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.15383\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"klein2025otcp\\\\\\\"\\\\n    title: \\\\\\\"Multivariate Conformal Prediction using Optimal Transport\\\\\\\"\\\\n    authors: \\\\\\\"Klein, Bethune, Ndiaye & Cuturi\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2502.03609\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.03609\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"zollo2025vla_calibration\\\\\\\"\\\\n    title: \\\\\\\"Confidence Calibration in Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Zollo & Zemel\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.17383\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.17383\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"tang2026shifting_uncertainty\\\\\\\"\\\\n    title: \\\\\\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\\\\\"\\\\n    authors: \\\\\\\"Tang et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2603.18342\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.18342\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"lcp2025\\\\\\\"\\\\n    title: \\\\\\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2509.21955\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.21955\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"claps2025\\\\\\\"\\\\n    title: \\\\\\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.10294\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.10294\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"lucca2024\\\\\\\"\\\\n    title: \\\\\\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\\\\\"\\\\n    authors: \\\\\\\"Marques et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2409.08249\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2409.08249\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"sc_vla_2026\\\\\\\"\\\\n    title: \\\\\\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.21633\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.21633\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_pilot_2025\\\\\\\"\\\\n    title: \\\\\\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.14178\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.14178\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"acot_vla_2026\\\\\\\"\\\\n    title: \\\\\\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"AgibotTech\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"CVPR 2026, arXiv:2601.11404\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.11404\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"gonzales2026crc_cbf\\\\\\\"\\\\n    title: \\\\\\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\\\\\"\\\\n    authors: \\\\\\\"Gonzales et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"IROS 2025, arXiv:2603.10392\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.10392\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"safediffcon2025\\\\\\\"\\\\n    title: \\\\\\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICML 2025, arXiv:2502.02205\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.02205\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"afil2026\\\\\\\"\\\\n    title: \\\\\\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.08434\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.08434\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"valle2025vla_uq_metrics\\\\\\\"\\\\n    title: \\\\\\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\\\\\"\\\\n    authors: \\\\\\\"Valle et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.17049\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.17049\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"diffusionvla2024\\\\\\\"\\\\n    title: \\\\\\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Wen et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICML 2025, arXiv:2412.03293\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2412.03293\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\\\\n\\\\n  - bibtex_key: \\\\\\\"silver2018residual\\\\\\\"\\\\n    title: \\\\\\\"Residual Policy Learning\\\\\\\"\\\\n    authors: \\\\\\\"Silver et al.\\\\\\\"\\\\n    year: 2018\\\\n    venue: \\\\\\\"RSS 2018\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1812.06298\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"johannink2019residual\\\\\\\"\\\\n    title: \\\\\\\"Residual Reinforcement Learning for Robot Manipulator Control\\\\\\\"\\\\n    authors: \\\\\\\"Johannink et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"ICRA 2019\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1812.03201\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"jiang2024transic\\\\\\\"\\\\n    title: \\\\\\\"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\\\\\\\"\\\\n    authors: \\\\\\\"Jiang et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"CoRL 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2405.10315\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"direct-competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"ankile2024resip\\\\\\\"\\\\n    title: \\\\\\\"ResiP: Residual Reinforcement Learning for Precise Assembly\\\\\\\"\\\\n    authors: \\\\\\\"Ankile et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"CoRL Workshop 2024\\\\\\\"\\\\n    url: \\\\\\\"\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: false\\\\n    verification_note: \\\\\\\"Workshop paper, no arXiv ID provided\\\\\\\"\\\\n    relevance: \\\\\\\"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"xiao2026pld\\\\\\\"\\\\n    title: \\\\\\\"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Xiao et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.00091\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"direct-competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"pan2025drc\\\\\\\"\\\\n    title: \\\\\\\"DRC: Decaying Relative Correction for Policy Refinement\\\\\\\"\\\\n    authors: \\\\\\\"Pan et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2503.15368\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2503.15368\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"ma2026dawn\\\\\\\"\\\\n    title: \\\\\\\"DAWN: Value Learning in Residual Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Ma et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.10539\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.10539\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_in_the_loop_2025\\\\\\\"\\\\n    title: \\\\\\\"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2025\\\\\\\"\\\\n    url: \\\\\\\"\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: false\\\\n    verification_note: \\\\\\\"No arXiv ID provided, needs verification\\\\\\\"\\\\n    relevance: \\\\\\\"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"zhou2025acp_cbf\\\\\\\"\\\\n    title: \\\\\\\"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Zhou et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICRA 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2503.17678\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 29225, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2410.24164\\\"\\n    url: \\\"https://arxiv.org/abs/2410.24164\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"braun2025cgs\\\"\\n    title: \\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\"\\n    authors: \\\"Braun et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.20941\\\"\\n    url: \\\"https://arxiv.org/abs/2507.20941\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"brohan2023rt2\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv:2307.15818\\\"\\n    url: \\\"https://arxiv.org/abs/2307.15818\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chen2026reconvla\\\"\\n    title: \\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\"\\n    authors: \\\"Chen et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.16677\\\"\\n    url: \\\"https://arxiv.org/abs/2604.16677\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"digflow2025\\\"\\n    title: \\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.01715\\\"\\n    url: \\\"https://arxiv.org/abs/2512.01715\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"fei2025liberoplus\\\"\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.13626\\\"\\n    url: \\\"https://arxiv.org/abs/2510.13626\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"ghosh2024octo\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Ghosh et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2405.12213\\\"\\n    url: \\\"https://arxiv.org/abs/2405.12213\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gibbs2021aci\\\"\\n    title: \\\"Adaptive Conformal Inference Under Distribution Shift\\\"\\n    authors: \\\"Gibbs & Candès\\\"\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://arxiv.org/abs/2106.00170\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"gu2025safe\\\"\\n    title: \\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\"\\n    authors: \\\"Gu et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09937\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"kim2024openvla\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2406.09246\\\"\\n    url: \\\"https://arxiv.org/abs/2406.09246\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"ledoit2004well\\\"\\n    title: \\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\"\\n    authors: \\\"Ledoit & Wolf\\\"\\n    year: 2004\\n    venue: \\\"Journal of Multivariate Analysis, 88(2):365-411\\\"\\n    url: \\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lipman2023flow\\\"\\n    title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Lipman et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.02747\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2023libero\\\"\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2306.03310\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2026ttvla\\\"\\n    title: \\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.06748\\\"\\n    url: \\\"https://arxiv.org/abs/2601.06748\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"luan2026snapflow\\\"\\n    title: \\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\"\\n    authors: \\\"Luan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.05656\\\"\\n    url: \\\"https://arxiv.org/abs/2604.05656\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"robustvla2025\\\"\\n    title: \\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.01331\\\"\\n    url: \\\"https://arxiv.org/abs/2511.01331\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"romano2019cqr\\\"\\n    title: \\\"Conformalized Quantile Regression\\\"\\n    authors: \\\"Romano et al.\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1905.03222\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shafer2008tutorial\\\"\\n    title: \\\"A Tutorial on Conformal Prediction\\\"\\n    authors: \\\"Shafer & Vovk\\\"\\n    year: 2008\\n    venue: \\\"Journal of Machine Learning Research, 9:371-421\\\"\\n    url: \\\"https://jmlr.org/papers/v9/shafer08a.html\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shukor2025smolvla\\\"\\n    title: \\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\"\\n    authors: \\\"Shukor et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2506.01844\\\"\\n    url: \\\"https://arxiv.org/abs/2506.01844\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"srpo2025\\\"\\n    title: \\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.15605\\\"\\n    url: \\\"https://arxiv.org/abs/2511.15605\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"wang2025cploop\\\"\\n    title: \\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\"\\n    authors: \\\"Wang & Ning\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.16376\\\"\\n    url: \\\"https://arxiv.org/abs/2510.16376\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"xing2026diu\\\"\\n    title: \\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\"\\n    authors: \\\"Xing et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.00941\\\"\\n    url: \\\"https://arxiv.org/abs/2605.00941\\\"\\n    category: \\\"uq_flow_matching\\\"\\n    verified: true\\n    relevance: \\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"yuan2026ups\\\"\\n    title: \\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\"\\n    authors: \\\"Yuan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.22474\\\"\\n    url: \\\"https://arxiv.org/abs/2602.22474\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"zhao2024conformalized\\\"\\n    title: \\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\"\\n    authors: \\\"Zhao et al.\\\"\\n    year: 2024\\n    venue: \\\"RSS 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2406.07767\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"cosmos_policy_2026\\\"\\n    title: \\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.16163\\\"\\n    url: \\\"https://arxiv.org/abs/2601.16163\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"vla_gse_2026\\\"\\n    title: \\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.06175\\\"\\n    url: \\\"https://arxiv.org/abs/2605.06175\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lakshminarayanan2017ensembles\\\"\\n    title: \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\"\\n    authors: \\\"Lakshminarayanan et al.\\\"\\n    year: 2017\\n    venue: \\\"NeurIPS 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1612.01474\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gal2016dropout\\\"\\n    title: \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\"\\n    authors: \\\"Gal & Ghahramani\\\"\\n    year: 2016\\n    venue: \\\"ICML 2016\\\"\\n    url: \\\"https://arxiv.org/abs/1506.02142\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chi2023diffusion_policy\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: \\\"RSS 2023 / IJRR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2303.04137\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: false\\n    verification_note: \\\"Well-known paper, needs URL reachability confirmation\\\"\\n    relevance: \\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\"\\n    must_cite: true\\n\\n  # ===== New entries added 2026-05-14 =====\\n\\n  - bibtex_key: \\\"fan2025interpretable_mcp\\\"\\n    title: \\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\"\\n    authors: \\\"Fan & Sesia\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.15383\\\"\\n    url: \\\"https://arxiv.org/abs/2512.15383\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"klein2025otcp\\\"\\n    title: \\\"Multivariate Conformal Prediction using Optimal Transport\\\"\\n    authors: \\\"Klein, Bethune, Ndiaye & Cuturi\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2502.03609\\\"\\n    url: \\\"https://arxiv.org/abs/2502.03609\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"zollo2025vla_calibration\\\"\\n    title: \\\"Confidence Calibration in Vision-Language-Action Models\\\"\\n    authors: \\\"Zollo & Zemel\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17383\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17383\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\"\\n    must_cite: true\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"tang2026shifting_uncertainty\\\"\\n    title: \\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\"\\n    authors: \\\"Tang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2603.18342\\\"\\n    url: \\\"https://arxiv.org/abs/2603.18342\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lcp2025\\\"\\n    title: \\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.21955\\\"\\n    url: \\\"https://arxiv.org/abs/2509.21955\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"claps2025\\\"\\n    title: \\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.10294\\\"\\n    url: \\\"https://arxiv.org/abs/2512.10294\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lucca2024\\\"\\n    title: \\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\"\\n    authors: \\\"Marques et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2409.08249\\\"\\n    url: \\\"https://arxiv.org/abs/2409.08249\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"sc_vla_2026\\\"\\n    title: \\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.21633\\\"\\n    url: \\\"https://arxiv.org/abs/2602.21633\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"vla_pilot_2025\\\"\\n    title: \\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.14178\\\"\\n    url: \\\"https://arxiv.org/abs/2511.14178\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"acot_vla_2026\\\"\\n    title: \\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\"\\n    authors: \\\"AgibotTech\\\"\\n    year: 2026\\n    venue: \\\"CVPR 2026, arXiv:2601.11404\\\"\\n    url: \\\"https://arxiv.org/abs/2601.11404\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"gonzales2026crc_cbf\\\"\\n    title: \\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\"\\n    authors: \\\"Gonzales et al.\\\"\\n    year: 2026\\n    venue: \\\"IROS 2025, arXiv:2603.10392\\\"\\n    url: \\\"https://arxiv.org/abs/2603.10392\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"safediffcon2025\\\"\\n    title: \\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025, arXiv:2502.02205\\\"\\n    url: \\\"https://arxiv.org/abs/2502.02205\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"afil2026\\\"\\n    title: \\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.08434\\\"\\n    url: \\\"https://arxiv.org/abs/2605.08434\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"valle2025vla_uq_metrics\\\"\\n    title: \\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\"\\n    authors: \\\"Valle et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17049\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17049\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"diffusionvla2024\\\"\\n    title: \\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\"\\n    authors: \\\"Wen et al.\\\"\\n    year: 2024\\n    venue: \\\"ICML 2025, arXiv:2412.03293\\\"\\n    url: \\\"https://arxiv.org/abs/2412.03293\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\\n\\n  - bibtex_key: \\\"silver2018residual\\\"\\n    title: \\\"Residual Policy Learning\\\"\\n    authors: \\\"Silver et al.\\\"\\n    year: 2018\\n    venue: \\\"RSS 2018\\\"\\n    url: \\\"https://arxiv.org/abs/1812.06298\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\\\"\\n    must_cite: true\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"johannink2019residual\\\"\\n    title: \\\"Residual Reinforcement Learning for Robot Manipulator Control\\\"\\n    authors: \\\"Johannink et al.\\\"\\n    year: 2019\\n    venue: \\\"ICRA 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1812.03201\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"jiang2024transic\\\"\\n    title: \\\"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2405.10315\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"ankile2024resip\\\"\\n    title: \\\"ResiP: Residual Reinforcement Learning for Precise Assembly\\\"\\n    authors: \\\"Ankile et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL Workshop 2024\\\"\\n    url: \\\"\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: false\\n    verification_note: \\\"Workshop paper, no arXiv ID provided\\\"\\n    relevance: \\\"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"xiao2026pld\\\"\\n    title: \\\"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\\\"\\n    authors: \\\"Xiao et al.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2511.00091\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"pan2025drc\\\"\\n    title: \\\"DRC: Decaying Relative Correction for Policy Refinement\\\"\\n    authors: \\\"Pan et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2503.15368\\\"\\n    url: \\\"https://arxiv.org/abs/2503.15368\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"ma2026dawn\\\"\\n    title: \\\"DAWN: Value Learning in Residual Reinforcement Learning\\\"\\n    authors: \\\"Ma et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.10539\\\"\\n    url: \\\"https://arxiv.org/abs/2602.10539\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"vla_in_the_loop_2025\\\"\\n    title: \\\"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: false\\n    verification_note: \\\"No arXiv ID provided, needs verification\\\"\\n    relevance: \\\"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"zhou2025acp_cbf\\\"\\n    title: \\\"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\\\"\\n    authors: \\\"Zhou et al.\\\"\\n    year: 2025\\n    venue: \\\"ICRA 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.17678\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"method-component\\\"\\n\", \"total_chars\": 29225, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
Good, I have the search results and project files. Let me now do additional targeted searches to get more specific details on papers I found, and also search for a few more competitors.

Key findings so far:

1. **SC-VLA** - Found as "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination" (arXiv:2602.21633, Feb 2026). Already in literature_map.yaml.

2. **VLA-Pilot** - Found as "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion" (arXiv:2511.14178, 2025). Already in literature_map.yaml.
   
3. **ACoT-VLA** - CVPR 2026 paper with strong benchmarks (98.5% LIBERO, 84.1% LIBERO-Plus, 47.4% VLABench), already documented.

4. **AsyncVLA** - Asynchronous Flow Matching for VLA Models (arXiv:2511.14148, Nov 2025) is a new find I need to add to the literature map.

5. **Self-Correcting VLA** - arXiv:2602.21633 from February 2026, already catalogued.

Now I'm seeing several conformal prediction papers for robotics that are mostly already in the literature map. I should dig deeper into AsyncVLA's specific performance metrics and track down the LIBERO results for the Self-Correcting VLA paper to get a complete picture of how these methods compare.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "c33c86c7-bb80-4ae7-acd2-c188ef8188a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAysxKoiPiGVk54xZqMpys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19830,
      "cache_read_input_tokens": 25431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19830
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

Found initial results. Searching for more specific details on key competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "4c4b045d-f5ce-4917-b5f4-7780570e8fbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAysxKoiPiGVk54xZqMpys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19830,
      "cache_read_input_tokens": 25431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19830
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QvMgpdamCenT5Q5QZ3GC2B`</summary>

```json
{
  "query": "arxiv 2602.21633 \"Self-Correcting VLA\" LIBERO results success rate ManiSkill"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "1f2c80e9-b6a1-4f19-9b62-181081c1b7ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAysxKoiPiGVk54xZqMpys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19830,
      "cache_read_input_tokens": 25431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19830
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ck8pFNwXsAVQ5jE7EZMLB7`</summary>

```json
{
  "query": "arxiv 2511.14178 VLA-Pilot LIBERO success rate benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "cec7221c-9597-4b4d-aa37-8aed1e4de973",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAysxKoiPiGVk54xZqMpys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19830,
      "cache_read_input_tokens": 25431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19830
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TA9jmxmcw5A5hEVTaerfvb`</summary>

```json
{
  "query": "AsyncVLA arxiv 2511.14148 asynchronous flow matching VLA results benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "6c609eec-734f-4ffe-b8de-aef1d180fec2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAysxKoiPiGVk54xZqMpys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19830,
      "cache_read_input_tokens": 25431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19830
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_018UBe8Eo5o7iBHxf1yePssj`</summary>

```json
{
  "query": "\"ReconVLA\" conformal prediction VLA LIBERO results 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "7c713ee2-f07f-4c43-b3c4-7b12716c5b73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAysxKoiPiGVk54xZqMpys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19830,
      "cache_read_input_tokens": 25431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19830
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rd7kcdzq677S1TSn7joiGg`</summary>

```json
{
  "query": "VLA inference time action correction sampling consensus 2025 2026 LIBERO benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "26cf18c6-e8a9-4f4a-bdb2-722469f627ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAysxKoiPiGVk54xZqMpys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19830,
      "cache_read_input_tokens": 25431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19830
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

_source line 30 · 2026-05-15T01:46:09.158Z_

<details><summary>↩ Tool result · `toolu_01QvMgpdamCenT5Q5QZ3GC2B`</summary>

```text
Web search results for query: "arxiv 2602.21633 "Self-Correcting VLA" LIBERO results success rate ManiSkill"

Links: [{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/pdf/2602.21633"},{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"},{"title":"From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/html/2602.01811"},{"title":"[2602.01811] From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/abs/2602.01811"},{"title":"World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy","url":"https://arxiv.org/pdf/2602.06508"},{"title":"VQ-VLA: Improving Vision-Language-Action Models ...","url":"https://arxiv.org/pdf/2507.01016"},{"title":"Beyond the Majority: Long-tail Imitation Learning for Robotic Manipulation","url":"https://arxiv.org/html/2602.06512"}]

Based on the search results, I found information about the Self-Correcting VLA (SC-VLA) paper with arxiv ID 2602.21633:

## Paper Overview

Self-Correcting VLA: Online Action Refinement via Sparse World Imagination was authored by Chenyv Liu, Wentao Tan, Lei Zhu, Fengling Li, Jingjing Li, Guoli Yang, and Heng Tao Shen.

## Key Results

The paper demonstrates that SC-VLA achieves state-of-the-art performance on challenging robot manipulation tasks from simulation benchmarks and real-world settings, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.

## Methodology

The approach designs sparse world imagination by integrating auxiliary predictive heads to forecast current task progress and future trajectory trends, and introduces an online action refinement module to reshape progress-dependent dense rewards, adjusting trajectory orientation based on predicted sparse future states.

## Benchmarks

SC-VLA achieves superior performance on ManiSkill and real-world ARX5 benchmarks, surpassing baselines in both success rate and execution throughput.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "80a71e6c-78ff-4a49-a54c-db47fc00da9c",
  "tool_use_result": {
    "query": "arxiv 2602.21633 \"Self-Correcting VLA\" LIBERO results success rate ManiSkill",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QYCmTaVTh56qUq1tHsTTV9",
        "content": [
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/pdf/2602.21633"
          },
          {
            "title": "[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/abs/2602.21633"
          },
          {
            "title": "GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub",
            "url": "https://github.com/Kisaragi0/SC-VLA"
          },
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"
          },
          {
            "title": "From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models",
            "url": "https://arxiv.org/html/2602.01811"
          },
          {
            "title": "[2602.01811] From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models",
            "url": "https://arxiv.org/abs/2602.01811"
          },
          {
            "title": "World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy",
            "url": "https://arxiv.org/pdf/2602.06508"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models ...",
            "url": "https://arxiv.org/pdf/2507.01016"
          },
          {
            "title": "Beyond the Majority: Long-tail Imitation Learning for Robotic Manipulation",
            "url": "https://arxiv.org/html/2602.06512"
          }
        ]
      },
      "Based on the search results, I found information about the Self-Correcting VLA (SC-VLA) paper with arxiv ID 2602.21633:\n\n## Paper Overview\n\nSelf-Correcting VLA: Online Action Refinement via Sparse World Imagination was authored by Chenyv Liu, Wentao Tan, Lei Zhu, Fengling Li, Jingjing Li, Guoli Yang, and Heng Tao Shen.\n\n## Key Results\n\nThe paper demonstrates that SC-VLA achieves state-of-the-art performance on challenging robot manipulation tasks from simulation benchmarks and real-world settings, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.\n\n## Methodology\n\nThe approach designs sparse world imagination by integrating auxiliary predictive heads to forecast current task progress and future trajectory trends, and introduces an online action refinement module to reshape progress-dependent dense rewards, adjusting trajectory orientation based on predicted sparse future states.\n\n## Benchmarks\n\nSC-VLA achieves superior performance on ManiSkill and real-world ARX5 benchmarks, surpassing baselines in both success rate and execution throughput."
    ],
    "durationSeconds": 7.544976536000002
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T01:46:09.481Z_

<details><summary>↩ Tool result · `toolu_01Ck8pFNwXsAVQ5jE7EZMLB7`</summary>

```text
Web search results for query: "arxiv 2511.14178 VLA-Pilot LIBERO success rate benchmark results"

Links: [{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"[2511.14178] Towards Deploying VLA without Fine-Tuning","url":"https://arxiv.org/abs/2511.14178"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2511.11298v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"Interactive Post-Training for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=oXYZHg7HiZ"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"}]

Based on the search results, I found information about VLA-Pilot from arxiv paper 2511.14178. Here's what I found regarding the benchmark results:

## VLA-Pilot Overview

VLA-Pilot is a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection.

## LIBERO Benchmark Results

While the search results confirm that the paper evaluates VLA-Pilot on robotic manipulation tasks, the specific LIBERO success rate numbers are not detailed in the available excerpts. The paper evaluates VLA-Pilot on six real-world downstream manipulation tasks across two distinct robotic embodiments, encompassing both in-distribution and out-of-distribution scenarios, and experimental results demonstrate that VLA-Pilot substantially boosts the success rates of off-the-shelf pre-trained VLA policies, enabling robust zero-shot generalization to diverse tasks and embodiments.

To access the specific LIBERO success rate benchmark numbers, you would need to view the full paper at the arxiv link: https://arxiv.org/html/2511.14178 or https://arxiv.org/abs/2511.14178


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "1a7ea532-5d0f-4c8c-9920-318ec73c41c1",
  "tool_use_result": {
    "query": "arxiv 2511.14178 VLA-Pilot LIBERO success rate benchmark results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SCKDGatTrtRZ69DRMbHCjo",
        "content": [
          {
            "title": "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion",
            "url": "https://arxiv.org/html/2511.14178"
          },
          {
            "title": "[2511.14178] Towards Deploying VLA without Fine-Tuning",
            "url": "https://arxiv.org/abs/2511.14178"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.11298v1"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301v1"
          },
          {
            "title": "Interactive Post-Training for Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=oXYZHg7HiZ"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/abs/2603.28301"
          }
        ]
      },
      "Based on the search results, I found information about VLA-Pilot from arxiv paper 2511.14178. Here's what I found regarding the benchmark results:\n\n## VLA-Pilot Overview\n\nVLA-Pilot is a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection.\n\n## LIBERO Benchmark Results\n\nWhile the search results confirm that the paper evaluates VLA-Pilot on robotic manipulation tasks, the specific LIBERO success rate numbers are not detailed in the available excerpts. The paper evaluates VLA-Pilot on six real-world downstream manipulation tasks across two distinct robotic embodiments, encompassing both in-distribution and out-of-distribution scenarios, and experimental results demonstrate that VLA-Pilot substantially boosts the success rates of off-the-shelf pre-trained VLA policies, enabling robust zero-shot generalization to diverse tasks and embodiments.\n\nTo access the specific LIBERO success rate benchmark numbers, you would need to view the full paper at the arxiv link: https://arxiv.org/html/2511.14178 or https://arxiv.org/abs/2511.14178"
    ],
    "durationSeconds": 7.420162432999998
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T01:46:09.928Z_

<details><summary>↩ Tool result · `toolu_018UBe8Eo5o7iBHxf1yePssj`</summary>

```text
Web search results for query: ""ReconVLA" conformal prediction VLA LIBERO results 2026"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"Conformal Prediction Conference 2026","url":"https://copa-conference.com/"},{"title":"PI-VLA: Adaptive Symmetry-Aware Decision-Making for Long-Horizon Vision–Language–Action Manipulation","url":"https://www.mdpi.com/2073-8994/18/3/394"},{"title":"GitHub - InternRobotics/InstructVLA: [ICLR 2026] InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation · GitHub","url":"https://github.com/InternRobotics/InstructVLA"},{"title":"AAAI 2026 Results Announced: High Score of 88887 Achieved, 17.6% Acceptance Rate for 23,000 Submissions","url":"https://eu.36kr.com/en/p/3546803868545153"},{"title":"AAAI 2026 Accepted Papers: Outstanding Papers, Research Trends & Full Highlights","url":"https://www.bohrium.com/blog/research-notes/aaai-2026-accepted-papers-highlights/"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://vla-safe.github.io/"},{"title":"Conformal Prediction events","url":"https://alrw.net/events.html"}]

I found relevant information about ReconVLA and conformal prediction. Here's what the search results reveal:

## ReconVLA Overview

ReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals for vision-language-action (VLA) models. The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success.

## How ReconVLA Works

ReconVLA incorporates conformal quantile regression (CQR)-based uncertainty quantification into the VLA's action generation process and its state monitoring, allowing the robot to detect when it "doesn't know" or is likely to fail before a catastrophe occurs.

## LIBERO Benchmark Results

However, the search results don't provide specific LIBERO benchmark results for ReconVLA itself. Instead, I found that ReconVLA integrates a lightweight diffusion transformer that reconstructs latent "gaze regions" from noise, and on long-horizon manipulation tasks like block stacking, ReconVLA achieves up to 85% success rates, significantly outperforming OpenVLA and GraspVLA.

Additionally, ReconVLA received Outstanding Paper recognition at AAAI 2026, indicating its significance in the field.

If you need more specific LIBERO benchmark comparisons or detailed quantitative results, I can search for additional information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "57171b2c-9e5f-4064-8d36-ba355fbdd1bf",
  "tool_use_result": {
    "query": "\"ReconVLA\" conformal prediction VLA LIBERO results 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V7J3Y2dBG82NKiaQCxezHP",
        "content": [
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL"
          },
          {
            "title": "Conformal Prediction Conference 2026",
            "url": "https://copa-conference.com/"
          },
          {
            "title": "PI-VLA: Adaptive Symmetry-Aware Decision-Making for Long-Horizon Vision–Language–Action Manipulation",
            "url": "https://www.mdpi.com/2073-8994/18/3/394"
          },
          {
            "title": "GitHub - InternRobotics/InstructVLA: [ICLR 2026] InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation · GitHub",
            "url": "https://github.com/InternRobotics/InstructVLA"
          },
          {
            "title": "AAAI 2026 Results Announced: High Score of 88887 Achieved, 17.6% Acceptance Rate for 23,000 Submissions",
            "url": "https://eu.36kr.com/en/p/3546803868545153"
          },
          {
            "title": "AAAI 2026 Accepted Papers: Outstanding Papers, Research Trends & Full Highlights",
            "url": "https://www.bohrium.com/blog/research-notes/aaai-2026-accepted-papers-highlights/"
          },
          {
            "title": "SAFE: Multitask Failure Detection for Vision-Language-Action Models",
            "url": "https://vla-safe.github.io/"
          },
          {
            "title": "Conformal Prediction events",
            "url": "https://alrw.net/events.html"
          }
        ]
      },
      "I found relevant information about ReconVLA and conformal prediction. Here's what the search results reveal:\n\n## ReconVLA Overview\n\nReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals for vision-language-action (VLA) models. The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success.\n\n## How ReconVLA Works\n\nReconVLA incorporates conformal quantile regression (CQR)-based uncertainty quantification into the VLA's action generation process and its state monitoring, allowing the robot to detect when it \"doesn't know\" or is likely to fail before a catastrophe occurs.\n\n## LIBERO Benchmark Results\n\nHowever, the search results don't provide specific LIBERO benchmark results for ReconVLA itself. Instead, I found that ReconVLA integrates a lightweight diffusion transformer that reconstructs latent \"gaze regions\" from noise, and on long-horizon manipulation tasks like block stacking, ReconVLA achieves up to 85% success rates, significantly outperforming OpenVLA and GraspVLA.\n\nAdditionally, ReconVLA received Outstanding Paper recognition at AAAI 2026, indicating its significance in the field.\n\nIf you need more specific LIBERO benchmark comparisons or detailed quantitative results, I can search for additional information."
    ],
    "durationSeconds": 6.454092003999998
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T01:46:10.426Z_

<details><summary>↩ Tool result · `toolu_01TA9jmxmcw5A5hEVTaerfvb`</summary>

```text
Web search results for query: "AsyncVLA arxiv 2511.14148 asynchronous flow matching VLA results benchmark"

Links: [{"title":"[2511.14148] AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.14148"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.14148v1"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2511.14148v1"},{"title":"AsyncVLA: Asynchronous Flow Matching for VLA","url":"https://www.emergentmind.com/topics/asynchronous-flow-matching-vla-asyncvla"},{"title":"GitHub - YuhuaJiang2002/AsyncVLA: AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models · GitHub","url":"https://github.com/YuhuaJiang2002/AsyncVLA"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/397739249_AsyncVLA_Asynchronous_Flow_Matching_for_Vision-Language-Action_Models"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language...","url":"https://bytez.com/docs/arxiv/2511.14148/paper"},{"title":"AsyncVLA: An Asynchronous VLA for Fast and Robust Navigation on the Edge","url":"https://arxiv.org/html/2602.13476"},{"title":"[2602.13476] AsyncVLA: An Asynchronous VLA for Fast and Robust Navigation on the Edge","url":"https://arxiv.org/abs/2602.13476"},{"title":"(PDF) AsyncVLA: An Asynchronous VLA for Fast and Robust Navigation on the Edge","url":"https://www.researchgate.net/publication/400854776_AsyncVLA_An_Asynchronous_VLA_for_Fast_and_Robust_Navigation_on_the_Edge"}]

Based on the search results, here's information about AsyncVLA (arxiv 2511.14148):

## Overview

AsyncVLA is a novel framework that introduces temporal flexibility in asynchronous FM (AFM) and enables self-correction in action generation. It is a Vision-language-action (VLA) model designed for building generalist robots.

## Key Problem and Solution

Traditional VLA models that generate actions through flow matching typically rely on rigid and uniform time schedules (synchronous FM), and without action context awareness and asynchronous self-correction, they become unstable in long-horizon tasks where a single action error can cascade into failure. 

AsyncVLA breaks from vanilla synchronous flow matching in VLA models by generating action tokens in a non-uniform time schedule with action context awareness.

## Key Technical Features

The method introduces a confidence rater to extract confidence of the initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution. Additionally, a unified training procedure for SFM and AFM endows a single model with both modes, improving KV-cache utilization.

## Benchmark Results

Empirical results on LIBERO, Bridge-V2, and Fractal benchmarks highlight its superior performance and data efficiency compared to synchronous methods. When data is limited (10% of LIBERO-Spatial), AsyncVLA achieves a 45% lower training loss and 9.6 percentage point higher test-suite success after 200 epochs compared to SFM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "b2fec961-6849-49bc-84b9-acda096765ff",
  "tool_use_result": {
    "query": "AsyncVLA arxiv 2511.14148 asynchronous flow matching VLA results benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K98462xmWbY8yxQWVC9U9b",
        "content": [
          {
            "title": "[2511.14148] AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2511.14148"
          },
          {
            "title": "AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.14148v1"
          },
          {
            "title": "AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2511.14148v1"
          },
          {
            "title": "AsyncVLA: Asynchronous Flow Matching for VLA",
            "url": "https://www.emergentmind.com/topics/asynchronous-flow-matching-vla-asyncvla"
          },
          {
            "title": "GitHub - YuhuaJiang2002/AsyncVLA: AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models · GitHub",
            "url": "https://github.com/YuhuaJiang2002/AsyncVLA"
          },
          {
            "title": "AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/397739249_AsyncVLA_Asynchronous_Flow_Matching_for_Vision-Language-Action_Models"
          },
          {
            "title": "AsyncVLA: Asynchronous Flow Matching for Vision-Language...",
            "url": "https://bytez.com/docs/arxiv/2511.14148/paper"
          },
          {
            "title": "AsyncVLA: An Asynchronous VLA for Fast and Robust Navigation on the Edge",
            "url": "https://arxiv.org/html/2602.13476"
          },
          {
            "title": "[2602.13476] AsyncVLA: An Asynchronous VLA for Fast and Robust Navigation on the Edge",
            "url": "https://arxiv.org/abs/2602.13476"
          },
          {
            "title": "(PDF) AsyncVLA: An Asynchronous VLA for Fast and Robust Navigation on the Edge",
            "url": "https://www.researchgate.net/publication/400854776_AsyncVLA_An_Asynchronous_VLA_for_Fast_and_Robust_Navigation_on_the_Edge"
          }
        ]
      },
      "Based on the search results, here's information about AsyncVLA (arxiv 2511.14148):\n\n## Overview\n\nAsyncVLA is a novel framework that introduces temporal flexibility in asynchronous FM (AFM) and enables self-correction in action generation. It is a Vision-language-action (VLA) model designed for building generalist robots.\n\n## Key Problem and Solution\n\nTraditional VLA models that generate actions through flow matching typically rely on rigid and uniform time schedules (synchronous FM), and without action context awareness and asynchronous self-correction, they become unstable in long-horizon tasks where a single action error can cascade into failure. \n\nAsyncVLA breaks from vanilla synchronous flow matching in VLA models by generating action tokens in a non-uniform time schedule with action context awareness.\n\n## Key Technical Features\n\nThe method introduces a confidence rater to extract confidence of the initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution. Additionally, a unified training procedure for SFM and AFM endows a single model with both modes, improving KV-cache utilization.\n\n## Benchmark Results\n\nEmpirical results on LIBERO, Bridge-V2, and Fractal benchmarks highlight its superior performance and data efficiency compared to synchronous methods. When data is limited (10% of LIBERO-Spatial), AsyncVLA achieves a 45% lower training loss and 9.6 percentage point higher test-suite success after 200 epochs compared to SFM."
    ],
    "durationSeconds": 7.885792686999994
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T01:46:12.331Z_

<details><summary>↩ Tool result · `toolu_01Rd7kcdzq677S1TSn7joiGg`</summary>

```text
Web search results for query: "VLA inference time action correction sampling consensus 2025 2026 LIBERO benchmark"

Links: [{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748"},{"title":"PI-VLA: Adaptive Symmetry-Aware Decision-Making for Long-Horizon Vision–Language–Action Manipulation","url":"https://www.mdpi.com/2073-8994/18/3/394"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"},{"title":"Mixture of Horizons in Action Chunking","url":"https://timsty1.github.io/moh/"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.01166v2"},{"title":"[2512.02834] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://arxiv.org/abs/2512.02834"}]

I found relevant research results on this topic. Here's what the search reveals:

## Key Research on VLA Inference, Action Correction, and LIBERO Benchmark

The search results show several important recent developments (2025-2026) in Vision-Language-Action (VLA) models related to inference time, action correction, and the LIBERO benchmark:

### Action Correction and Inference Time

A method called A2C2 (Action Chunk Correction with Consensus) yields consistent success rate improvements across increasing delays and execution horizons (about 7% point improvement compared to RTC), and has minimal overhead compared to the inference of large VLA models. The approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC).

### Consensus-Based Sampling Approaches

A test-time reinforcement learning approach (TTRL) performs test-time adaptation by sampling multiple candidate outputs for each input and constructing a consensus pseudo-label via majority voting, though this consensus-based pseudo-label appears less effective for VLA tasks.

The Mixture of Horizons (MoH) approach enables dynamic inference that selects stable actions through cross-horizon consensus for higher efficiency and robustness.

### LIBERO Benchmark Performance

PI-VLA achieves state-of-the-art performance on the LIBERO benchmark with a 73.2% average success rate (with particularly strong gains on the Long-Horizon suite). Another method achieves near-saturated 99% success rates on the LIBERO benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "9639d217-435a-4b4a-8d25-d03323c449cb",
  "tool_use_result": {
    "query": "VLA inference time action correction sampling consensus 2025 2026 LIBERO benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_017an491JumC55Y3YrvQRznG",
        "content": [
          {
            "title": "Leave No Observation Behind: Real-time Correction for VLA Action Chunks",
            "url": "https://arxiv.org/html/2509.23224v1"
          },
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2601.06748"
          },
          {
            "title": "PI-VLA: Adaptive Symmetry-Aware Decision-Making for Long-Horizon Vision–Language–Action Manipulation",
            "url": "https://www.mdpi.com/2073-8994/18/3/394"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301v1"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"
          },
          {
            "title": "Mixture of Horizons in Action Chunking",
            "url": "https://timsty1.github.io/moh/"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data ...",
            "url": "https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"
          },
          {
            "title": "Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2602.01166v2"
          },
          {
            "title": "[2512.02834] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://arxiv.org/abs/2512.02834"
          }
        ]
      },
      "I found relevant research results on this topic. Here's what the search reveals:\n\n## Key Research on VLA Inference, Action Correction, and LIBERO Benchmark\n\nThe search results show several important recent developments (2025-2026) in Vision-Language-Action (VLA) models related to inference time, action correction, and the LIBERO benchmark:\n\n### Action Correction and Inference Time\n\nA method called A2C2 (Action Chunk Correction with Consensus) yields consistent success rate improvements across increasing delays and execution horizons (about 7% point improvement compared to RTC), and has minimal overhead compared to the inference of large VLA models. The approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC).\n\n### Consensus-Based Sampling Approaches\n\nA test-time reinforcement learning approach (TTRL) performs test-time adaptation by sampling multiple candidate outputs for each input and constructing a consensus pseudo-label via majority voting, though this consensus-based pseudo-label appears less effective for VLA tasks.\n\nThe Mixture of Horizons (MoH) approach enables dynamic inference that selects stable actions through cross-horizon consensus for higher efficiency and robustness.\n\n### LIBERO Benchmark Performance\n\nPI-VLA achieves state-of-the-art performance on the LIBERO benchmark with a 73.2% average success rate (with particularly strong gains on the Long-Horizon suite). Another method achieves near-saturated 99% success rates on the LIBERO benchmark."
    ],
    "durationSeconds": 7.854000177000001
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Let me search for a few more specific details I need:
1. ReconVLA's specific LIBERO numbers
2. SC-VLA's ManiSkill specific numbers
3. VLA-Pilot's specific OOD results
4. AsyncVLA's specific LIBERO numbers
5. Any other recent VLA correction papers I might have missed

Let me also check the ICLR 2026 VLA blog post for a landscape overview.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "708547dc-2171-4280-8e82-c5fe2493d896",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWC5GEZbQJo6iiLSVyJscy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5104,
      "cache_read_input_tokens": 45261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5104
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

_source line 36_

Let me get more specific quantitative results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "40869e69-ad96-4883-b4a4-7bcd7844d404",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWC5GEZbQJo6iiLSVyJscy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5104,
      "cache_read_input_tokens": 45261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5104
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

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HU39DRsHDoEVEhs6mUXqHc`</summary>

```json
{
  "query": "ReconVLA arxiv 2604.16677 LIBERO spatial goal object success rate table results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "92ff4a14-9155-4aaf-8d61-d8c6dd241f18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWC5GEZbQJo6iiLSVyJscy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5104,
      "cache_read_input_tokens": 45261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5104
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

_source line 38_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MSbTsPjUTTiYpwpTjBH4tr`</summary>

```json
{
  "query": "SC-VLA \"Self-Correcting VLA\" ManiSkill average success rate specific numbers table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "dffc2ff4-8d90-4cfa-bf60-679a2a0e74ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWC5GEZbQJo6iiLSVyJscy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5104,
      "cache_read_input_tokens": 45261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5104
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

_source line 39_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LCvbPbYCwhVxQYNoR1MDbb`</summary>

```json
{
  "query": "VLA-Pilot OOD success rate 0.50 real world results specific benchmark numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "7118558a-4fef-4255-a44d-ec6500c6b162",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWC5GEZbQJo6iiLSVyJscy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5104,
      "cache_read_input_tokens": 45261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5104
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TBXLVERFy1CUt2wzXv9oDz`</summary>

```json
{
  "query": "\"conformal prediction\" \"action correction\" \"per-DOF\" OR \"per-dimension\" OR \"dimension-wise\" robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "a8f679ef-3d0d-456d-9963-ef6d106308aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWC5GEZbQJo6iiLSVyJscy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5104,
      "cache_read_input_tokens": 45261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5104
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

_source line 41 · 2026-05-15T01:46:25.708Z_

<details><summary>↩ Tool result · `toolu_01MSbTsPjUTTiYpwpTjBH4tr`</summary>

```text
Web search results for query: "SC-VLA "Self-Correcting VLA" ManiSkill average success rate specific numbers table"

Links: [{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"},{"title":"RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.06710"},{"title":"A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation","url":"https://arxiv.org/html/2405.17418v2"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers","url":"https://xiaoxiao0406.github.io/vqvla.github.io/"},{"title":"FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.01642"},{"title":"From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/html/2602.01811"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"Jump-Start Reinforcement Learning with Vision-Language-Action Regularization","url":"https://arxiv.org/html/2604.13733"},{"title":"RLinf-VLA: A unified and efficient framework for VLA+RL training","url":"https://arxiv.org/html/2510.06710v1"}]

Based on my web search, I found information about SC-VLA (Self-Correcting VLA), though there appear to be multiple papers with similar names. Let me provide what I found:

## SC-VLA Research

SC-VLA achieves superior performance on ManiSkill and real-world ARX5 benchmarks, surpassing baselines in both success rate and execution throughput. More specifically, SC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.

However, my search did not return a specific detailed table with exact average success rate numbers for individual ManiSkill tasks. The GitHub repository and papers I found mention general performance improvements but don't provide the granular per-task breakdown table you're looking for.

To find the specific numbers table you're requesting, I'd recommend:
1. Checking the arXiv paper directly (arXiv:2602.21633 for the 2026 version mentioned in the search results)
2. Visiting the GitHub repository at https://github.com/Kisaragi0/SC-VLA, which may contain detailed results tables or supplementary materials
3. Looking for supplementary appendices in the full paper PDF

Would you like me to search for more specific information about particular ManiSkill tasks or a different aspect of SC-VLA's performance?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "37d55510-2b84-4010-8172-ff1e0556fb9a",
  "tool_use_result": {
    "query": "SC-VLA \"Self-Correcting VLA\" ManiSkill average success rate specific numbers table",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L9dgdHVinmYFXXBrfrDrdi",
        "content": [
          {
            "title": "GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub",
            "url": "https://github.com/Kisaragi0/SC-VLA"
          },
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"
          },
          {
            "title": "RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.06710"
          },
          {
            "title": "A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation",
            "url": "https://arxiv.org/html/2405.17418v2"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers",
            "url": "https://xiaoxiao0406.github.io/vqvla.github.io/"
          },
          {
            "title": "FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2510.01642"
          },
          {
            "title": "From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models",
            "url": "https://arxiv.org/html/2602.01811"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"
          },
          {
            "title": "Jump-Start Reinforcement Learning with Vision-Language-Action Regularization",
            "url": "https://arxiv.org/html/2604.13733"
          },
          {
            "title": "RLinf-VLA: A unified and efficient framework for VLA+RL training",
            "url": "https://arxiv.org/html/2510.06710v1"
          }
        ]
      },
      "Based on my web search, I found information about SC-VLA (Self-Correcting VLA), though there appear to be multiple papers with similar names. Let me provide what I found:\n\n## SC-VLA Research\n\nSC-VLA achieves superior performance on ManiSkill and real-world ARX5 benchmarks, surpassing baselines in both success rate and execution throughput. More specifically, SC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.\n\nHowever, my search did not return a specific detailed table with exact average success rate numbers for individual ManiSkill tasks. The GitHub repository and papers I found mention general performance improvements but don't provide the granular per-task breakdown table you're looking for.\n\nTo find the specific numbers table you're requesting, I'd recommend:\n1. Checking the arXiv paper directly (arXiv:2602.21633 for the 2026 version mentioned in the search results)\n2. Visiting the GitHub repository at https://github.com/Kisaragi0/SC-VLA, which may contain detailed results tables or supplementary materials\n3. Looking for supplementary appendices in the full paper PDF\n\nWould you like me to search for more specific information about particular ManiSkill tasks or a different aspect of SC-VLA's performance?"
    ],
    "durationSeconds": 5.970429652999999
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T01:46:28.100Z_

<details><summary>↩ Tool result · `toolu_01LCvbPbYCwhVxQYNoR1MDbb`</summary>

```text
Web search results for query: "VLA-Pilot OOD success rate 0.50 real world results specific benchmark numbers"

Links: [{"title":"Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2511.11298v1"},{"title":"Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification","url":"https://arxiv.org/html/2510.16281"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Point-VLA: Pixel-Level Visual Grounding for VLA","url":"https://www.emergentmind.com/topics/point-vla"},{"title":"Benchmarking Vision, Language, & Action Models in Procedurally Generated, Open Ended Action Environments","url":"https://www.manifoldrg.com/benchmarking-vision-language-action-models-in-procedurally-generated-open-ended-action-environments/"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"GitHub - NVlabs/vla0: VLA-0: Building State-of-the-Art VLAs with Zero Modification · GitHub","url":"https://github.com/NVlabs/vla0"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"}]

Based on the search results, I found relevant information about VLA model performance, though I didn't find specific results for a model explicitly named "VLA-Pilot" with a 0.50 OOD success rate. However, the search returned comprehensive benchmark data on Vision-Language-Action models and their out-of-distribution (OOD) performance metrics.

The search results reveal several key findings about VLA OOD performance:

**Key Real-World Results:**

ACT's success rates fall from 86% to only 36% under OOD settings on the Clean Dish task, and from 85% to 32% on Put into Pot, representing significant performance drops. OpenVLA's success on Clean Dish goes from 29% to 15%, approximately a 14% drop, and RDT-1B's Clean Dish goes from 27% to 14%.

**Broader Benchmark Insights:**

OpenVLA-OFT achieves SOTA results in LIBERO: 97.1% average success rate across 4 task suites, though this represents in-distribution performance. Reported SOTA figures (>95% success) reflect performance under clean, nearly identically distributed train/test splits, whereas systematic robustness analyses reveal significant brittleness and a tendency toward memorization.

The search results indicate that while some VLA models achieve high performance on standard benchmarks, their OOD generalization remains a significant challenge, with success rates often dropping 30-50% or more when exposed to spatial or instance variations.

If you're looking for specific "VLA-Pilot" results, you may want to provide additional context or check if the model might be published under a different name or in a more recent paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "2fed30f1-dbf6-4be8-ab74-8fe7d99fdf74",
  "tool_use_result": {
    "query": "VLA-Pilot OOD success rate 0.50 real world results specific benchmark numbers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W1mw7D2Tujz6Twdg2W8KJE",
        "content": [
          {
            "title": "Experiences from Benchmarking Vision–Language–Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.11298v1"
          },
          {
            "title": "Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification",
            "url": "https://arxiv.org/html/2510.16281"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "Point-VLA: Pixel-Level Visual Grounding for VLA",
            "url": "https://www.emergentmind.com/topics/point-vla"
          },
          {
            "title": "Benchmarking Vision, Language, & Action Models in Procedurally Generated, Open Ended Action Environments",
            "url": "https://www.manifoldrg.com/benchmarking-vision-language-action-models-in-procedurally-generated-open-ended-action-environments/"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data ...",
            "url": "https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"
          },
          {
            "title": "GitHub - NVlabs/vla0: VLA-0: Building State-of-the-Art VLAs with Zero Modification · GitHub",
            "url": "https://github.com/NVlabs/vla0"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression ...",
            "url": "https://openreview.net/pdf?id=SELYlDHZk2"
          }
        ]
      },
      "Based on the search results, I found relevant information about VLA model performance, though I didn't find specific results for a model explicitly named \"VLA-Pilot\" with a 0.50 OOD success rate. However, the search returned comprehensive benchmark data on Vision-Language-Action models and their out-of-distribution (OOD) performance metrics.\n\nThe search results reveal several key findings about VLA OOD performance:\n\n**Key Real-World Results:**\n\nACT's success rates fall from 86% to only 36% under OOD settings on the Clean Dish task, and from 85% to 32% on Put into Pot, representing significant performance drops. OpenVLA's success on Clean Dish goes from 29% to 15%, approximately a 14% drop, and RDT-1B's Clean Dish goes from 27% to 14%.\n\n**Broader Benchmark Insights:**\n\nOpenVLA-OFT achieves SOTA results in LIBERO: 97.1% average success rate across 4 task suites, though this represents in-distribution performance. Reported SOTA figures (>95% success) reflect performance under clean, nearly identically distributed train/test splits, whereas systematic robustness analyses reveal significant brittleness and a tendency toward memorization.\n\nThe search results indicate that while some VLA models achieve high performance on standard benchmarks, their OOD generalization remains a significant challenge, with success rates often dropping 30-50% or more when exposed to spatial or instance variations.\n\nIf you're looking for specific \"VLA-Pilot\" results, you may want to provide additional context or check if the model might be published under a different name or in a more recent paper."
    ],
    "durationSeconds": 7.427325512000003
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T01:46:31.335Z_

<details><summary>↩ Tool result · `toolu_01HU39DRsHDoEVEhs6mUXqHc`</summary>

```text
Web search results for query: "ReconVLA arxiv 2604.16677 LIBERO spatial goal object success rate table results"

Links: [{"title":"CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors","url":"https://arxiv.org/html/2604.21241"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models","url":"https://arxiv.org/html/2501.15830v2"},{"title":"InSpire: Vision-Language-Action Models with Intrinsic Spatial Reasoning","url":"https://arxiv.org/html/2505.13888v1"},{"title":"OmniVLA-RL: A Vision-Language-Action Model with Spatial Understanding and Online RL","url":"https://arxiv.org/html/2604.17706"},{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"[2604.21241] CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors","url":"https://arxiv.org/abs/2604.21241"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"}]

I found the ReconVLA paper (arxiv 2604.16677). However, the search results show this is a different paper about uncertainty-guided and failure-aware VLA models, not a reconstructive VLA model. Let me search more specifically for the table results you're looking for.

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"[PDF] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReconVLA:-Reconstructive-Vision-Language-Action-as-Song-Zhou/c87ea2afcd9212e5128e01daf17c733d285ac345"},{"title":"Mask World Model: Predicting What Matters for Robust Robot Policy Learning","url":"https://arxiv.org/html/2604.19683"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"}]

Based on my search, I've located the ReconVLA paper from arxiv 2604.16677 published on April 17, 2026. However, I should clarify that there are actually **two different papers titled "ReconVLA"**:

1. **arxiv 2604.16677** (the one you specified): An uncertainty-guided and failure-aware vision-language-action framework for robotic control

2. **arxiv 2508.10333**: A reconstructive vision-language-action model as an effective robot perceiver

The search results I retrieved show information about both papers, but the specific table results for the LIBERO spatial goal object success rates from arxiv 2604.16677 are not fully displayed in the search results. The HTML version of the paper appears to be available on arXiv, but the detailed numerical table results for "LIBERO-Spatial goal object success rate" are not included in the searchable content I retrieved.

To access the complete table results you're looking for, I recommend visiting the full paper directly at: **https://arxiv.org/html/2604.16677v1** where you should be able to view all the experimental results tables.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "d6db9eb2-08be-409b-bf97-60b292573c7c",
  "tool_use_result": {
    "query": "ReconVLA arxiv 2604.16677 LIBERO spatial goal object success rate table results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CU7Yt3mrSycrf7ky9Acoqy",
        "content": [
          {
            "title": "CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors",
            "url": "https://arxiv.org/html/2604.21241"
          },
          {
            "title": "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models",
            "url": "https://arxiv.org/html/2501.15830v2"
          },
          {
            "title": "InSpire: Vision-Language-Action Models with Intrinsic Spatial Reasoning",
            "url": "https://arxiv.org/html/2505.13888v1"
          },
          {
            "title": "OmniVLA-RL: A Vision-Language-Action Model with Spatial Understanding and Online RL",
            "url": "https://arxiv.org/html/2604.17706"
          },
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/html/2508.10333v1"
          },
          {
            "title": "[2604.21241] CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors",
            "url": "https://arxiv.org/abs/2604.21241"
          },
          {
            "title": "[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/abs/2508.10333"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          }
        ]
      },
      "I found the ReconVLA paper (arxiv 2604.16677). However, the search results show this is a different paper about uncertainty-guided and failure-aware VLA models, not a reconstructive VLA model. Let me search more specifically for the table results you're looking for.",
      {
        "tool_use_id": "srvtoolu_01QPRCsFJc3tmGNG8fDVjpej",
        "content": [
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/html/2508.10333v1"
          },
          {
            "title": "[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/abs/2508.10333"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "[PDF] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ReconVLA:-Reconstructive-Vision-Language-Action-as-Song-Zhou/c87ea2afcd9212e5128e01daf17c733d285ac345"
          },
          {
            "title": "Mask World Model: Predicting What Matters for Robust Robot Policy Learning",
            "url": "https://arxiv.org/html/2604.19683"
          },
          {
            "title": "LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium",
            "url": "https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"
          },
          {
            "title": "physical-intelligence/libero · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/physical-intelligence/libero"
          },
          {
            "title": "[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
            "url": "https://arxiv.org/abs/2306.03310"
          },
          {
            "title": "GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub",
            "url": "https://github.com/Lifelong-Robot-Learning/LIBERO"
          }
        ]
      },
      "Based on my search, I've located the ReconVLA paper from arxiv 2604.16677 published on April 17, 2026. However, I should clarify that there are actually **two different papers titled \"ReconVLA\"**:\n\n1. **arxiv 2604.16677** (the one you specified): An uncertainty-guided and failure-aware vision-language-action framework for robotic control\n\n2. **arxiv 2508.10333**: A reconstructive vision-language-action model as an effective robot perceiver\n\nThe search results I retrieved show information about both papers, but the specific table results for the LIBERO spatial goal object success rates from arxiv 2604.16677 are not fully displayed in the search results. The HTML version of the paper appears to be available on arXiv, but the detailed numerical table results for \"LIBERO-Spatial goal object success rate\" are not included in the searchable content I retrieved.\n\nTo access the complete table results you're looking for, I recommend visiting the full paper directly at: **https://arxiv.org/html/2604.16677v1** where you should be able to view all the experimental results tables."
    ],
    "durationSeconds": 12.094698403999995
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T01:46:35.165Z_

<details><summary>↩ Tool result · `toolu_01TBXLVERFy1CUt2wzXv9oDz`</summary>

```text
Web search results for query: ""conformal prediction" "action correction" "per-DOF" OR "per-dimension" OR "dimension-wise" robot 2025 2026"

Links: [{"title":"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception","url":"https://arxiv.org/html/2509.21955"},{"title":"[2509.21955] Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception","url":"https://arxiv.org/abs/2509.21955"},{"title":"Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024","url":"https://www.roboticsproceedings.org/rss20/p008.pdf"},{"title":"GitHub - valeman/awesome-conformal-prediction: A professionally curated list of awesome Conformal Prediction videos, tutorials, books, papers, PhD and MSc theses, articles and open-source libraries. · GitHub","url":"https://github.com/valeman/awesome-conformal-prediction"},{"title":"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control","url":"https://arxiv.org/html/2603.10392v1"},{"title":"Online Conformal Prediction: Enforcing monotonicity via Online Optimization","url":"https://arxiv.org/html/2605.12668"},{"title":"Probabilistic Object Detection with Conformal Prediction","url":"https://arxiv.org/html/2605.07549"},{"title":"Conformal Prediction for Robotics | xLAB: Safe Autonomous Systems Lab","url":"https://xlab.upenn.edu/conformal-prediction-robotics/"},{"title":"Automatica 183 (2026) 112616 Contents lists available at ScienceDirect","url":"https://xiangyin.sjtu.edu.cn/Paper/26AutoCP.pdf"},{"title":"Safe Planning in Dynamic Environments Using Conformal ...","url":"https://www.georgejpappas.org/wp-content/uploads/2023/08/Safe_Planning_in_Dynamic_Environments_Using_Conformal_Prediction.pdf"}]

I found several relevant research papers on conformal prediction applied to robotics. Here are the key findings from the search results:

## Recent Work on Conformal Prediction for Robot Control

Deep learning models in robotics often output point estimates with poorly calibrated confidences. Learnable Conformal Prediction (LCP) replaces fixed scores with a lightweight neural function that leverages geometric, semantic, and task-specific features to produce context-aware uncertainty sets.

### Per-Dimension Action Correction

The search results include work on dimension-wise uncertainty quantification in robot control:

One approach leverages conformal methods to quantify if the robot's learned controller can reliably lift a human's low-DoF input (joystick) to their desired high-DoF action (7 joint velocities). For any joystick input at the current state, the robot can assess its uncertainty in remapping that input.

### Related Techniques

Conformal prediction has recently attracted significant interest as a principled framework for uncertainty quantification, with properties that make it particularly appealing for robotics, where models must operate under distribution shift and safety requires formal reliability bounds on decision-making.

An algorithm that dynamically adjusts the safety margins produced by conformal risk control based on the current interaction context has been shown to significantly reduce collision rates and safety violations in human-robot navigation scenarios.

The search results show active research in applying conformal prediction to robot control problems, including per-dimension uncertainty quantification for action correction, though the specific combination of all your search terms appears to be a specialized research direction that may have limited coverage in publicly available sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "a9cb067d-20cd-4cfc-aa71-2022f1b077da",
  "tool_use_result": {
    "query": "\"conformal prediction\" \"action correction\" \"per-DOF\" OR \"per-dimension\" OR \"dimension-wise\" robot 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ss968PApihgrXQFL1353q4",
        "content": [
          {
            "title": "Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception",
            "url": "https://arxiv.org/html/2509.21955"
          },
          {
            "title": "[2509.21955] Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception",
            "url": "https://arxiv.org/abs/2509.21955"
          },
          {
            "title": "Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024",
            "url": "https://www.roboticsproceedings.org/rss20/p008.pdf"
          },
          {
            "title": "GitHub - valeman/awesome-conformal-prediction: A professionally curated list of awesome Conformal Prediction videos, tutorials, books, papers, PhD and MSc theses, articles and open-source libraries. · GitHub",
            "url": "https://github.com/valeman/awesome-conformal-prediction"
          },
          {
            "title": "Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control",
            "url": "https://arxiv.org/html/2603.10392v1"
          },
          {
            "title": "Online Conformal Prediction: Enforcing monotonicity via Online Optimization",
            "url": "https://arxiv.org/html/2605.12668"
          },
          {
            "title": "Probabilistic Object Detection with Conformal Prediction",
            "url": "https://arxiv.org/html/2605.07549"
          },
          {
            "title": "Conformal Prediction for Robotics | xLAB: Safe Autonomous Systems Lab",
            "url": "https://xlab.upenn.edu/conformal-prediction-robotics/"
          },
          {
            "title": "Automatica 183 (2026) 112616 Contents lists available at ScienceDirect",
            "url": "https://xiangyin.sjtu.edu.cn/Paper/26AutoCP.pdf"
          },
          {
            "title": "Safe Planning in Dynamic Environments Using Conformal ...",
            "url": "https://www.georgejpappas.org/wp-content/uploads/2023/08/Safe_Planning_in_Dynamic_Environments_Using_Conformal_Prediction.pdf"
          }
        ]
      },
      "I found several relevant research papers on conformal prediction applied to robotics. Here are the key findings from the search results:\n\n## Recent Work on Conformal Prediction for Robot Control\n\nDeep learning models in robotics often output point estimates with poorly calibrated confidences. Learnable Conformal Prediction (LCP) replaces fixed scores with a lightweight neural function that leverages geometric, semantic, and task-specific features to produce context-aware uncertainty sets.\n\n### Per-Dimension Action Correction\n\nThe search results include work on dimension-wise uncertainty quantification in robot control:\n\nOne approach leverages conformal methods to quantify if the robot's learned controller can reliably lift a human's low-DoF input (joystick) to their desired high-DoF action (7 joint velocities). For any joystick input at the current state, the robot can assess its uncertainty in remapping that input.\n\n### Related Techniques\n\nConformal prediction has recently attracted significant interest as a principled framework for uncertainty quantification, with properties that make it particularly appealing for robotics, where models must operate under distribution shift and safety requires formal reliability bounds on decision-making.\n\nAn algorithm that dynamically adjusts the safety margins produced by conformal risk control based on the current interaction context has been shown to significantly reduce collision rates and safety violations in human-robot navigation scenarios.\n\nThe search results show active research in applying conformal prediction to robot control problems, including per-dimension uncertainty quantification for action correction, though the specific combination of all your search terms appears to be a specialized research direction that may have limited coverage in publicly available sources."
    ],
    "durationSeconds": 13.521907191000006
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Now let me also look for specific numbers from the papers. Let me try to fetch the actual HTML content of a few key papers to get quantitative results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "936cd8c4-edea-465e-aa28-7bab77ba6190",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QaSG43swDfkULefVZ33NH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4696,
      "cache_read_input_tokens": 50365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4696
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

_source line 46_

Let me fetch the actual paper pages for quantitative results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "865345d0-8291-49b2-8656-76c85a660a21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QaSG43swDfkULefVZ33NH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4696,
      "cache_read_input_tokens": 50365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4696
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0147ZBF7ZdHUJRukTxbzScmS`</summary>

```json
{
  "query": "site:arxiv.org \"Self-Correcting VLA\" ManiSkill success rate 86% average per-task"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "709e5ea8-a0e6-4a3e-84f3-66a679bfd032",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QaSG43swDfkULefVZ33NH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4696,
      "cache_read_input_tokens": 50365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4696
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

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S4k7QmjFmuzerXCMSNatmn`</summary>

```json
{
  "query": "ACoT-VLA LIBERO-Plus 84.1 LIBERO 98.5 VLABench 47.4 detailed results breakdown"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "4412c756-c26b-4e01-8804-f86cb44c1980",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QaSG43swDfkULefVZ33NH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4696,
      "cache_read_input_tokens": 50365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4696
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

_source line 49_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hw2GCfssGkJuooGR3CMrVN`</summary>

```json
{
  "query": "AsyncVLA LIBERO-Spatial success rate specific numbers table 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "0f546ff7-3152-414b-88ca-ce1bbd66fffb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QaSG43swDfkULefVZ33NH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4696,
      "cache_read_input_tokens": 50365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4696
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

_source line 50 · 2026-05-15T01:46:45.348Z_

<details><summary>↩ Tool result · `toolu_0147ZBF7ZdHUJRukTxbzScmS`</summary>

```text
Web search results for query: "site:arxiv.org "Self-Correcting VLA" ManiSkill success rate 86% average per-task"

Links: [{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/html/2602.01811"},{"title":"RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.06710"},{"title":"RLinf-VLA: A unified and efficient framework for VLA+RL training","url":"https://arxiv.org/html/2510.06710v1"},{"title":"FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01642"},{"title":"A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation","url":"https://arxiv.org/html/2405.17418v2"},{"title":"[2602.01811] From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/abs/2602.01811"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers","url":"https://arxiv.org/html/2507.01016"},{"title":"Jump-Start Reinforcement Learning with Vision-Language-Action Regularization","url":"https://arxiv.org/html/2604.13733"}]

Based on the search results, I found relevant information about the Self-Correcting VLA paper. SC-VLA achieves state-of-the-art performance on challenging robot manipulation tasks, yielding 9% higher success rate than the best-performing baselines, and SC-VLA achieves superior performance on ManiSkill and real-world ARX5 benchmarks, surpassing baselines in both success rate and execution throughput.

The paper was published on arXiv (arxiv.org/html/2602.21633) in February 2026. However, the search results don't explicitly show the specific 86% average per-task success rate figure you mentioned. The results indicate strong performance improvements on ManiSkill tasks, but the exact numerical breakdown by task isn't fully visible in the search excerpts. You may find the detailed per-task success rates in Table 1 of the full paper, which is referenced in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "efaf0808-dacb-4362-b0a6-9ffdaf1c22e9",
  "tool_use_result": {
    "query": "site:arxiv.org \"Self-Correcting VLA\" ManiSkill success rate 86% average per-task",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QvNSnE8Po7NwayQTdEsRf3",
        "content": [
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/html/2602.21633"
          },
          {
            "title": "GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub",
            "url": "https://github.com/Kisaragi0/SC-VLA"
          },
          {
            "title": "From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models",
            "url": "https://arxiv.org/html/2602.01811"
          },
          {
            "title": "RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.06710"
          },
          {
            "title": "RLinf-VLA: A unified and efficient framework for VLA+RL training",
            "url": "https://arxiv.org/html/2510.06710v1"
          },
          {
            "title": "FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.01642"
          },
          {
            "title": "A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation",
            "url": "https://arxiv.org/html/2405.17418v2"
          },
          {
            "title": "[2602.01811] From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models",
            "url": "https://arxiv.org/abs/2602.01811"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers",
            "url": "https://arxiv.org/html/2507.01016"
          },
          {
            "title": "Jump-Start Reinforcement Learning with Vision-Language-Action Regularization",
            "url": "https://arxiv.org/html/2604.13733"
          }
        ]
      },
      "Based on the search results, I found relevant information about the Self-Correcting VLA paper. SC-VLA achieves state-of-the-art performance on challenging robot manipulation tasks, yielding 9% higher success rate than the best-performing baselines, and SC-VLA achieves superior performance on ManiSkill and real-world ARX5 benchmarks, surpassing baselines in both success rate and execution throughput.\n\nThe paper was published on arXiv (arxiv.org/html/2602.21633) in February 2026. However, the search results don't explicitly show the specific 86% average per-task success rate figure you mentioned. The results indicate strong performance improvements on ManiSkill tasks, but the exact numerical breakdown by task isn't fully visible in the search excerpts. You may find the detailed per-task success rates in Table 1 of the full paper, which is referenced in the search results."
    ],
    "durationSeconds": 4.8313817560000025
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T01:46:49.715Z_

<details><summary>↩ Tool result · `toolu_01Hw2GCfssGkJuooGR3CMrVN`</summary>

```text
Web search results for query: "AsyncVLA LIBERO-Spatial success rate specific numbers table 2025"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/9a959fdda3f49f4bf09cfe6e81b9ee1f82a16c5f.pdf"},{"title":"[Quick Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action\\n Models","url":"https://liner.com/review/liberoplus-indepth-robustness-analysis-visionlanguageaction-models"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"}]

I found some relevant information about AsyncVLA, LIBERO-Spatial, and success rate tables. Based on the search results, here's what I found:

The search results reference Table 3 containing task-wise LIBERO and LIBERO-PRO performance of three VLA models on the libero-spatial benchmark, which appears to be from the LIBERO-PRO paper (dated October 4, 2025).

However, the specific numerical data from that table isn't fully visible in the search results. The LIBERO-PRO evaluation suite introduces perturbations across four dimensions: objects, goals, spatial configurations, and task sets (shown in Tables 2, 3, 4, 5).

The search results indicate that all three models (OpenVLA, pi0, and pi0.5) achieve around 98% accuracy under the standard LIBERO, but perturbation experiments reveal significant robustness gaps, with models being highly sensitive to initial object position: for both OpenVLA and pi0, performance collapses once displacement exceeds 0.2 units, while pi0.5 sustains non-trivial accuracy up to 0.4 units before collapsing to zero.

To access the complete Table 3 with specific AsyncVLA LIBERO-Spatial success rate numbers, you would need to consult the original LIBERO-PRO paper directly at the sources I found, particularly the arxiv PDFs which should contain the full tables.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "6ffda67a-f851-496e-860e-7e9da46828d2",
  "tool_use_result": {
    "query": "AsyncVLA LIBERO-Spatial success rate specific numbers table 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Lxh7Td48pKZHkwngkoiRoe",
        "content": [
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019",
            "url": "https://openreview.net/pdf/9a959fdda3f49f4bf09cfe6e81b9ee1f82a16c5f.pdf"
          },
          {
            "title": "[Quick Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action\\n Models",
            "url": "https://liner.com/review/liberoplus-indepth-robustness-analysis-visionlanguageaction-models"
          },
          {
            "title": "LIBERO Tasks: Lifelong Robotic Learning",
            "url": "https://www.emergentmind.com/topics/libero-tasks"
          }
        ]
      },
      "I found some relevant information about AsyncVLA, LIBERO-Spatial, and success rate tables. Based on the search results, here's what I found:\n\nThe search results reference Table 3 containing task-wise LIBERO and LIBERO-PRO performance of three VLA models on the libero-spatial benchmark, which appears to be from the LIBERO-PRO paper (dated October 4, 2025).\n\nHowever, the specific numerical data from that table isn't fully visible in the search results. The LIBERO-PRO evaluation suite introduces perturbations across four dimensions: objects, goals, spatial configurations, and task sets (shown in Tables 2, 3, 4, 5).\n\nThe search results indicate that all three models (OpenVLA, pi0, and pi0.5) achieve around 98% accuracy under the standard LIBERO, but perturbation experiments reveal significant robustness gaps, with models being highly sensitive to initial object position: for both OpenVLA and pi0, performance collapses once displacement exceeds 0.2 units, while pi0.5 sustains non-trivial accuracy up to 0.4 units before collapsing to zero.\n\nTo access the complete Table 3 with specific AsyncVLA LIBERO-Spatial success rate numbers, you would need to consult the original LIBERO-PRO paper directly at the sources I found, particularly the arxiv PDFs which should contain the full tables."
    ],
    "durationSeconds": 6.599717563999992
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T01:46:53.807Z_

<details><summary>↩ Tool result · `toolu_01S4k7QmjFmuzerXCMSNatmn`</summary>

```text
Web search results for query: "ACoT-VLA LIBERO-Plus 84.1 LIBERO 98.5 VLABench 47.4 detailed results breakdown"

Links: [{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/html/2601.11404v1"},{"title":"Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://huggingface.co/papers/2601.11404"},{"title":"(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"},{"title":"[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2601.11404"},{"title":"Libero Checkpoint · Issue #3 · AgibotTech/ACoT-VLA","url":"https://github.com/AgibotTech/ACoT-VLA/issues/3"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - OpenMOSS/VLABench: Official repo of VLABench, a large scale benchmark designed for fairly evaluating VLA, Embodied Agent, and VLMs. · GitHub","url":"https://github.com/OpenMOSS/VLABench"},{"title":"VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics","url":"https://openreview.net/pdf/2bbc53ad5ee316c58cb3d6ad93efa6bea1088eec.pdf"}]

Based on the search results, I can provide you with detailed information about the ACoT-VLA results:

## Overall Performance Summary

ACoT-VLA achieves state-of-the-art performance on multiple benchmarks, with 98.5%, 84.1% and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively.

## Performance Breakdown by Benchmark

**LIBERO (98.5%):** ACoT-VLA achieves a 98.5% average success rate on LIBERO, surpassing the previous state-of-the-art by 1.6%, with particularly strong improvement in long-horizon tasks, indicating that direct action-space reasoning enhances robustness against error accumulation.

**LIBERO-Plus (84.1%):** Combining EAR and IAR modules achieves the highest success rate of 84.1%, demonstrating their complementary effects, where EAR provides explicit motion guidance, while IAR supplies dense representation-level priors. Additionally, ACoT-VLA substantially improves success rates under challenging perturbations such as camera-viewpoint shifts (+11.6%), robot initial-state perturbations (+16.3%), and sensor noise (+12.5%) compared to language-guided or vision-guided policies.

**VLABench (47.4%):** On the VLABench benchmark, ACoT-VLA achieves an average score of 47.4%, evaluated across multiple categories including Commonsense, Instruction, and Texture tasks.

## Key Technical Contributions

ACoT-VLA demonstrates significant improvements, particularly in the LIBERO-Long suite, by reducing ambiguity in mapping observations to actions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "5d1348bd-942b-4a48-be69-025e44d061dc",
  "tool_use_result": {
    "query": "ACoT-VLA LIBERO-Plus 84.1 LIBERO 98.5 VLABench 47.4 detailed results breakdown",
    "results": [
      {
        "tool_use_id": "srvtoolu_019cbDg1S6CLL7sVZ8RBsAgK",
        "content": [
          {
            "title": "GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub",
            "url": "https://github.com/AgibotTech/ACoT-VLA"
          },
          {
            "title": "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2601.11404v1"
          },
          {
            "title": "Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2601.11404"
          },
          {
            "title": "(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"
          },
          {
            "title": "[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"
          },
          {
            "title": "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | Takara TLDR",
            "url": "https://tldr.takara.ai/p/2601.11404"
          },
          {
            "title": "Libero Checkpoint · Issue #3 · AgibotTech/ACoT-VLA",
            "url": "https://github.com/AgibotTech/ACoT-VLA/issues/3"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "GitHub - OpenMOSS/VLABench: Official repo of VLABench, a large scale benchmark designed for fairly evaluating VLA, Embodied Agent, and VLMs. · GitHub",
            "url": "https://github.com/OpenMOSS/VLABench"
          },
          {
            "title": "VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics",
            "url": "https://openreview.net/pdf/2bbc53ad5ee316c58cb3d6ad93efa6bea1088eec.pdf"
          }
        ]
      },
      "Based on the search results, I can provide you with detailed information about the ACoT-VLA results:\n\n## Overall Performance Summary\n\nACoT-VLA achieves state-of-the-art performance on multiple benchmarks, with 98.5%, 84.1% and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively.\n\n## Performance Breakdown by Benchmark\n\n**LIBERO (98.5%):** ACoT-VLA achieves a 98.5% average success rate on LIBERO, surpassing the previous state-of-the-art by 1.6%, with particularly strong improvement in long-horizon tasks, indicating that direct action-space reasoning enhances robustness against error accumulation.\n\n**LIBERO-Plus (84.1%):** Combining EAR and IAR modules achieves the highest success rate of 84.1%, demonstrating their complementary effects, where EAR provides explicit motion guidance, while IAR supplies dense representation-level priors. Additionally, ACoT-VLA substantially improves success rates under challenging perturbations such as camera-viewpoint shifts (+11.6%), robot initial-state perturbations (+16.3%), and sensor noise (+12.5%) compared to language-guided or vision-guided policies.\n\n**VLABench (47.4%):** On the VLABench benchmark, ACoT-VLA achieves an average score of 47.4%, evaluated across multiple categories including Commonsense, Instruction, and Texture tasks.\n\n## Key Technical Contributions\n\nACoT-VLA demonstrates significant improvements, particularly in the LIBERO-Long suite, by reducing ambiguity in mapping observations to actions."
    ],
    "durationSeconds": 11.379825785000008
  }
}
```

</details>

---

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
I now have enough information to compile the competitive analysis report. Let me summarize what I know:

**ACoT-VLA** (CVPR 2026, arXiv:2601.11404):
- Method: Action Chain-of-Thought with EAR (Explicit Action Reasoner) + IAR (Implicit Action Reasoner)
- Results: LIBERO 98.5%, LIBERO-Plus 84.1%, VLABench 47.4%
- Training-time method, no online adaptation
- Already in literature_map.yaml and paper_framing.md


- **SC-VLA / Self-Correcting VLA** (arXiv:2602.21633, Feb 2026) uses Sparse World Imagination and online action refinement with residual RL to achieve ~86% on ManiSkill with 9% improvement over baselines and 14% gains on real-world tasks, though it lacks LIBERO benchmarks.
- **VLA-Pilot** (arXiv:2511.14178, Nov 2025) takes a different approach with an MLLM verifier and evolutionary diffusion optimizer for zero-shot deployment.
- **VLA-Pilot** shows strong out-of-distribution performance at 0.50 success rate compared to 0.12-0.19 baselines, though inference takes 2.41s per step and focuses mainly on real-world evaluation rather than standard LIBERO benchmarks.
- **ReconVLA** (arXiv:2604.16677, Apr 2026) combines CQR-based uncertainty estimation with diffusion-based latent gaze reconstruction and state anomaly detection, reaching 85% on long-horizon block stacking tasks and earning an AAAI 2026 Outstanding Paper award.
- **AsyncVLA** (arXiv:2511.14148, Nov 2025) is coming up next—let me see what approach it takes.

AsyncVLA uses asynchronous flow matching with a confidence rater to selectively refine action tokens, achieving 45% lower training loss and a 9.6 percentage point success improvement over standard flow matching on limited LIBERO-Spatial data, but it's not yet documented in the literature map.

**A2C2** applies an asynchronous action chunk correction head for about 7 percentage points of improvement over RTC, while **PLD** from ICLR 2026 uses residual reinforcement learning with scheduled magnitude bounds—both are already catalogued.

Now I'm identifying which papers still need to be added to the literature map: AsyncVLA is the main gap so far, and there's another paper starting to appear in the list.

Looking at what's missing from the documentation, AsyncVLA should be added to the literature map since it covers flow matching with self-correction through confidence rating, and while A2C2 is already in the literature map, it's not yet represented in the competitive landscape section of the paper framing document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "b533ad93-2129-478b-a601-958c45191670",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEoJVcZmHpzYWz1AfyLW4F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 914,
      "cache_creation_input_tokens": 2086,
      "cache_read_input_tokens": 55061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2086
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

_source line 54_

I have all the data I need. Now writing the competitive analysis report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "4bddaa59-1e24-45e9-bb62-88b2a05243dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEoJVcZmHpzYWz1AfyLW4F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 914,
      "cache_creation_input_tokens": 2086,
      "cache_read_input_tokens": 55061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2086
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

_source line 55_

<details open><summary>🔧 Tool call — Write · `toolu_01UcS597MQuKXQGVv3hUd2CX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/competitive_analysis_20260515.md",
  "content": "# Competitive Analysis (2026-05-15)\n\n## 竞品对比表\n\n| 方法 | 核心思路 | LIBERO / LIBERO-Plus 结果 | 与 ACR-VLA 关键差异 | 发表状态 |\n|------|---------|--------------------------|---------------------|---------|\n| **ACoT-VLA** | EAR (粗粒度参考轨迹) + IAR (latent action priors) 的 action chain-of-thought，联合训练引导 action head | LIBERO 98.5%, LIBERO-Plus **84.1%** (当前 SOTA), VLABench 47.4% | Training-time 方法，需在目标任务上训练 EAR+IAR；无 UQ，部署后不在线适应；与 ACR-VLA 正交互补 | **CVPR 2026** (arXiv:2601.11404) |\n| **ReconVLA** | CQR-based scalar uncertainty + SMD state anomaly detection + diffusion 重建 latent gaze regions；从 K 个 action samples 中选最佳 | 长程操作 (block stacking) 达 85%；标准 LIBERO/LIBERO-Plus 具体数值未公开 | Scalar CQR 丢失维度信息；sample selection（非 learned correction）——K 个样本都差时失效；static calibration 不做在线适应 | **AAAI 2026 Outstanding Paper** (arXiv:2604.16677) |\n| **SC-VLA** | Sparse World Imagination 预测任务进度 + 未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线纠正 | ManiSkill 平均 ~86% (+9% SR over baselines)，real-world +14%；**未在 LIBERO/LIBERO-Plus 评估** | 需任务级 RL 训练（非 plug-and-play）；无统计保证和 UQ；residual 作用在整个 action vector 无维度选择性 | arXiv:2602.21633 (Feb 2026) |\n| **VLA-Pilot** | MLLM verifier + evolutionary diffusion optimizer 的三阶段 inference-time steering，零样本 plug-and-play | OOD 场景 SR 0.50 vs baseline 0.12-0.19；**未在 LIBERO 标准 benchmark 评估** | 推理延迟 2.41s/step 不适合实时；MLLM scoring 为启发式无 calibrated confidence；无统计保证 | arXiv:2511.14178 (Nov 2025) |\n| **AsyncVLA** | 异步 flow matching + confidence rater 评估 action token 置信度，选择性 refine 低置信 token | 10% LIBERO-Spatial 数据下 +9.6pp vs SFM；full LIBERO 具体数值未在搜索中找到 | 改进 flow matching 推理过程本身（training-time 架构改动）；非 post-hoc correction；无 conformal guarantee | arXiv:2511.14148 (Nov 2025) |\n| **A2C2** | 轻量异步 action chunk correction head，利用最新观测修正已生成的 action chunk | ~+7pp vs RTC baseline；无需重训 base policy | Residual correction 无 UQ conditioning；无维度选择性；correction 基于观测差而非统计不确定性 | arXiv:2509.23224 (2025) |\n| **PLD** | Residual RL + scheduled magnitude bound ξ 在 VLA 上做 self-improving | LIBERO 上验证；ICLR 2026 | 需要 RL 训练；magnitude bound 为预设 schedule 而非 data-driven conformal bound | **ICLR 2026** (arXiv:2511.00091) |\n| **SRPO** | Self-referential RL post-training for VLA robustness | LIBERO-Plus **82.1%** | Training-time RL 方法；ACR-VLA 旨在 stacking 在其之上进一步提升 | arXiv:2511.15605 (2025) |\n\n## 我们的差异化优势（基于当前实验数据）\n\n### 当前实验数据摘要\n- Baseline (K=1): 30% on LIBERO-Spatial\n- VLA-mean (K=10 avg): 32%\n- Argmin-only selection: ~34%\n- **ACR-VLA per-DOF CRM** (K=10, max_norm=0.1): **52.5%** @ 4/10 tasks\n- **ACR-VLA obs_only CRM**: **63.3%** @ 3/10 tasks (early, may drop)\n- Object benchmark baseline: 13%\n\n### 差异化定位\n\n1. **唯一将 multivariate conformal statistics 作为 learned correction 输入的方法**。所有竞品要么不用 CP（SC-VLA, VLA-Pilot, ACoT-VLA, A2C2, PLD），要么只用 scalar CP（ReconVLA）。ACR-VLA 的 40D 结构化特征（per-DOF std + conformal radius + ellipsoid volume）是当前文献中粒度最细的 action-level UQ。\n\n2. **Learned dimension-selective correction vs. 全局修正/样本选择**。ReconVLA 做 sample selection（上界受限于最佳 sample 质量）；SC-VLA/A2C2/PLD 做全局 residual correction（无维度选择性）。ACR-VLA 的 CRM 可对高不确定 DOF 强纠正，低不确定 DOF 保持原样。\n\n3. **Online coverage adaptation (ACI+COC)**。ReconVLA 使用 static calibration set，分布偏移下 coverage 退化。ACR-VLA 通过 Chunk Overlap Consistency 提供自参考覆盖信号 + ACI 在线更新 threshold，无需外部监督。\n\n4. **与 training-time 方法正交互补**。ACoT-VLA (84.1%) 和 SRPO (82.1%) 是当前 LIBERO-Plus SOTA，但都是 training-time 方法。ACR-VLA 作为 inference-time 模块可叠加使用。\n\n### 当前结果的竞争力评估\n\nACR-VLA 的 52.5% (4/10 tasks) 在 LIBERO-Spatial 上显著优于自身 baseline (30%)，但与 ACoT-VLA 的 98.5% (full LIBERO) 或 SRPO 的 82.1% (LIBERO-Plus) 不直接可比——这些数值基于更强的 backbone (通常 7B+) 和 full benchmark evaluation。ACR-VLA 使用 SmolVLA (450M) 作为 backbone，重点是证明 **inference-time conformal correction 的增量价值**，而非绝对 SOTA。\n\n**关键叙事策略**: 强调 relative improvement (+22.5pp over baseline) 和 stacking potential（在强 backbone 上的叠加增益），而非绝对数值竞争。\n\n## paper_framing.md 建议更新\n\n### 需要增加的竞品引用\n\n1. **AsyncVLA** (arXiv:2511.14148) — 当前 `literature_map.yaml` 中缺失。AsyncVLA 在 flow matching 推理过程中引入 confidence rater 做选择性 token refinement，是与 ACR-VLA 最接近的 \"confidence-guided action refinement\" 思路，但在 training-time 层面实现（需修改 VLA 架构），且无 conformal guarantee。建议加入 competitive landscape 作为对比：ACR-VLA 是 post-hoc + conformal + per-DOF，AsyncVLA 是 built-in + heuristic confidence + per-token。\n\n2. **\"From Knowing to Doing Precisely\"** (arXiv:2602.01811) — self-correction + termination framework for VLA，可能相关但需进一步确认内容。\n\n### positioning 建议调整\n\n1. **paper_framing.md 中 SC-VLA 的描述已准确**，但建议补充其发表状态（目前仍为 arXiv preprint，无顶会录用信息），降低其作为竞品的威胁等级。\n\n2. **ACoT-VLA 的 LIBERO-Plus 84.1% 数据已确认**（CVPR 2026，代码开源），paper_framing.md 中的信息准确无需修改。\n\n3. **ReconVLA 已获 AAAI 2026 Outstanding Paper**，建议在 competitive landscape 中标注此荣誉，凸显我们与之的方法差异（scalar vs per-DOF, selection vs correction, static vs adaptive）的重要性——我们需要令人信服地展示 per-DOF conformal features 相比 scalar CQR 的增量价值。\n\n4. **Gap statement 建议微调**：当前 paper_framing.md 的 Gap 段已覆盖主要竞品，但 AsyncVLA 的 confidence-guided refinement 应作为新增 gap 描述的一部分：\"AsyncVLA 在 flow matching 内部引入 confidence rater 但需修改 VLA 架构且无 statistical guarantee\"。\n\n### 已收录且信息准确的竞品\n- ReconVLA ✓ (需补充 AAAI 2026 Outstanding Paper 信息)\n- SC-VLA ✓\n- VLA-Pilot ✓\n- ACoT-VLA ✓\n- A2C2 ✓\n- SRPO ✓\n- PLD ✓\n- SAFE ✓\n\n### literature_map.yaml 需新增\n- AsyncVLA (arXiv:2511.14148, category: inference_correction, relation: competitor)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "2d6d7659-1f89-4345-a33f-56c6bd751809",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEoJVcZmHpzYWz1AfyLW4F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 914,
      "cache_creation_input_tokens": 2086,
      "cache_read_input_tokens": 55061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2086
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

_source line 56 · 2026-05-15T01:48:23.860Z_

<details><summary>↩ Tool result · `toolu_01UcS597MQuKXQGVv3hUd2CX`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/competitive_analysis_20260515.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "8ec404b8-7e50-482f-b6ca-2cea08842fd8",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/competitive_analysis_20260515.md",
    "content": "# Competitive Analysis (2026-05-15)\n\n## 竞品对比表\n\n| 方法 | 核心思路 | LIBERO / LIBERO-Plus 结果 | 与 ACR-VLA 关键差异 | 发表状态 |\n|------|---------|--------------------------|---------------------|---------|\n| **ACoT-VLA** | EAR (粗粒度参考轨迹) + IAR (latent action priors) 的 action chain-of-thought，联合训练引导 action head | LIBERO 98.5%, LIBERO-Plus **84.1%** (当前 SOTA), VLABench 47.4% | Training-time 方法，需在目标任务上训练 EAR+IAR；无 UQ，部署后不在线适应；与 ACR-VLA 正交互补 | **CVPR 2026** (arXiv:2601.11404) |\n| **ReconVLA** | CQR-based scalar uncertainty + SMD state anomaly detection + diffusion 重建 latent gaze regions；从 K 个 action samples 中选最佳 | 长程操作 (block stacking) 达 85%；标准 LIBERO/LIBERO-Plus 具体数值未公开 | Scalar CQR 丢失维度信息；sample selection（非 learned correction）——K 个样本都差时失效；static calibration 不做在线适应 | **AAAI 2026 Outstanding Paper** (arXiv:2604.16677) |\n| **SC-VLA** | Sparse World Imagination 预测任务进度 + 未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线纠正 | ManiSkill 平均 ~86% (+9% SR over baselines)，real-world +14%；**未在 LIBERO/LIBERO-Plus 评估** | 需任务级 RL 训练（非 plug-and-play）；无统计保证和 UQ；residual 作用在整个 action vector 无维度选择性 | arXiv:2602.21633 (Feb 2026) |\n| **VLA-Pilot** | MLLM verifier + evolutionary diffusion optimizer 的三阶段 inference-time steering，零样本 plug-and-play | OOD 场景 SR 0.50 vs baseline 0.12-0.19；**未在 LIBERO 标准 benchmark 评估** | 推理延迟 2.41s/step 不适合实时；MLLM scoring 为启发式无 calibrated confidence；无统计保证 | arXiv:2511.14178 (Nov 2025) |\n| **AsyncVLA** | 异步 flow matching + confidence rater 评估 action token 置信度，选择性 refine 低置信 token | 10% LIBERO-Spatial 数据下 +9.6pp vs SFM；full LIBERO 具体数值未在搜索中找到 | 改进 flow matching 推理过程本身（training-time 架构改动）；非 post-hoc correction；无 conformal guarantee | arXiv:2511.14148 (Nov 2025) |\n| **A2C2** | 轻量异步 action chunk correction head，利用最新观测修正已生成的 action chunk | ~+7pp vs RTC baseline；无需重训 base policy | Residual correction 无 UQ conditioning；无维度选择性；correction 基于观测差而非统计不确定性 | arXiv:2509.23224 (2025) |\n| **PLD** | Residual RL + scheduled magnitude bound ξ 在 VLA 上做 self-improving | LIBERO 上验证；ICLR 2026 | 需要 RL 训练；magnitude bound 为预设 schedule 而非 data-driven conformal bound | **ICLR 2026** (arXiv:2511.00091) |\n| **SRPO** | Self-referential RL post-training for VLA robustness | LIBERO-Plus **82.1%** | Training-time RL 方法；ACR-VLA 旨在 stacking 在其之上进一步提升 | arXiv:2511.15605 (2025) |\n\n## 我们的差异化优势（基于当前实验数据）\n\n### 当前实验数据摘要\n- Baseline (K=1): 30% on LIBERO-Spatial\n- VLA-mean (K=10 avg): 32%\n- Argmin-only selection: ~34%\n- **ACR-VLA per-DOF CRM** (K=10, max_norm=0.1): **52.5%** @ 4/10 tasks\n- **ACR-VLA obs_only CRM**: **63.3%** @ 3/10 tasks (early, may drop)\n- Object benchmark baseline: 13%\n\n### 差异化定位\n\n1. **唯一将 multivariate conformal statistics 作为 learned correction 输入的方法**。所有竞品要么不用 CP（SC-VLA, VLA-Pilot, ACoT-VLA, A2C2, PLD），要么只用 scalar CP（ReconVLA）。ACR-VLA 的 40D 结构化特征（per-DOF std + conformal radius + ellipsoid volume）是当前文献中粒度最细的 action-level UQ。\n\n2. **Learned dimension-selective correction vs. 全局修正/样本选择**。ReconVLA 做 sample selection（上界受限于最佳 sample 质量）；SC-VLA/A2C2/PLD 做全局 residual correction（无维度选择性）。ACR-VLA 的 CRM 可对高不确定 DOF 强纠正，低不确定 DOF 保持原样。\n\n3. **Online coverage adaptation (ACI+COC)**。ReconVLA 使用 static calibration set，分布偏移下 coverage 退化。ACR-VLA 通过 Chunk Overlap Consistency 提供自参考覆盖信号 + ACI 在线更新 threshold，无需外部监督。\n\n4. **与 training-time 方法正交互补**。ACoT-VLA (84.1%) 和 SRPO (82.1%) 是当前 LIBERO-Plus SOTA，但都是 training-time 方法。ACR-VLA 作为 inference-time 模块可叠加使用。\n\n### 当前结果的竞争力评估\n\nACR-VLA 的 52.5% (4/10 tasks) 在 LIBERO-Spatial 上显著优于自身 baseline (30%)，但与 ACoT-VLA 的 98.5% (full LIBERO) 或 SRPO 的 82.1% (LIBERO-Plus) 不直接可比——这些数值基于更强的 backbone (通常 7B+) 和 full benchmark evaluation。ACR-VLA 使用 SmolVLA (450M) 作为 backbone，重点是证明 **inference-time conformal correction 的增量价值**，而非绝对 SOTA。\n\n**关键叙事策略**: 强调 relative improvement (+22.5pp over baseline) 和 stacking potential（在强 backbone 上的叠加增益），而非绝对数值竞争。\n\n## paper_framing.md 建议更新\n\n### 需要增加的竞品引用\n\n1. **AsyncVLA** (arXiv:2511.14148) — 当前 `literature_map.yaml` 中缺失。AsyncVLA 在 flow matching 推理过程中引入 confidence rater 做选择性 token refinement，是与 ACR-VLA 最接近的 \"confidence-guided action refinement\" 思路，但在 training-time 层面实现（需修改 VLA 架构），且无 conformal guarantee。建议加入 competitive landscape 作为对比：ACR-VLA 是 post-hoc + conformal + per-DOF，AsyncVLA 是 built-in + heuristic confidence + per-token。\n\n2. **\"From Knowing to Doing Precisely\"** (arXiv:2602.01811) — self-correction + termination framework for VLA，可能相关但需进一步确认内容。\n\n### positioning 建议调整\n\n1. **paper_framing.md 中 SC-VLA 的描述已准确**，但建议补充其发表状态（目前仍为 arXiv preprint，无顶会录用信息），降低其作为竞品的威胁等级。\n\n2. **ACoT-VLA 的 LIBERO-Plus 84.1% 数据已确认**（CVPR 2026，代码开源），paper_framing.md 中的信息准确无需修改。\n\n3. **ReconVLA 已获 AAAI 2026 Outstanding Paper**，建议在 competitive landscape 中标注此荣誉，凸显我们与之的方法差异（scalar vs per-DOF, selection vs correction, static vs adaptive）的重要性——我们需要令人信服地展示 per-DOF conformal features 相比 scalar CQR 的增量价值。\n\n4. **Gap statement 建议微调**：当前 paper_framing.md 的 Gap 段已覆盖主要竞品，但 AsyncVLA 的 confidence-guided refinement 应作为新增 gap 描述的一部分：\"AsyncVLA 在 flow matching 内部引入 confidence rater 但需修改 VLA 架构且无 statistical guarantee\"。\n\n### 已收录且信息准确的竞品\n- ReconVLA ✓ (需补充 AAAI 2026 Outstanding Paper 信息)\n- SC-VLA ✓\n- VLA-Pilot ✓\n- ACoT-VLA ✓\n- A2C2 ✓\n- SRPO ✓\n- PLD ✓\n- SAFE ✓\n\n### literature_map.yaml 需新增\n- AsyncVLA (arXiv:2511.14148, category: inference_correction, relation: competitor)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01R6Zi5BStLjN8skLUNhecT2`</summary>

```json
{
  "name": "competitive_analysis_20260515",
  "type": "report",
  "description": "竞品文献分析报告 (2026-05-15): 8篇竞品论文对比表、ACR-VLA差异化优势分析、paper_framing.md更新建议",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/competitive_analysis_20260515.md",
  "tags": [
    "competitive-analysis",
    "literature-review",
    "paper-framing",
    "CoRL-2026"
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
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "9b796e40-ac09-4f7b-93a0-a8510de7e685",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xx4SL9y287DqndoFQtTexe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4783,
      "cache_read_input_tokens": 57147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4783
      },
      "output_tokens": 78,
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

_source line 58 · 2026-05-15T01:48:29.572Z_

<details><summary>↩ Tool result · `toolu_01R6Zi5BStLjN8skLUNhecT2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_e74873\", \"name\": \"competitive_analysis_20260515\", \"type\": \"report\", \"description\": \"竞品文献分析报告 (2026-05-15): 8篇竞品论文对比表、ACR-VLA差异化优势分析、paper_framing.md更新建议\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/competitive_analysis_20260515.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T01:48:29.508400+00:00\", \"tags\": [\"competitive-analysis\", \"literature-review\", \"paper-framing\", \"CoRL-2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "88b939a0-4361-4ffb-ac0a-9e51f539e857",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_e74873\\\", \\\"name\\\": \\\"competitive_analysis_20260515\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"竞品文献分析报告 (2026-05-15): 8篇竞品论文对比表、ACR-VLA差异化优势分析、paper_framing.md更新建议\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/report/competitive_analysis_20260515.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T01:48:29.508400+00:00\\\", \\\"tags\\\": [\\\"competitive-analysis\\\", \\\"literature-review\\\", \\\"paper-framing\\\", \\\"CoRL-2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_e74873\", \"name\": \"competitive_analysis_20260515\", \"type\": \"report\", \"description\": \"竞品文献分析报告 (2026-05-15): 8篇竞品论文对比表、ACR-VLA差异化优势分析、paper_framing.md更新建议\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/competitive_analysis_20260515.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T01:48:29.508400+00:00\", \"tags\": [\"competitive-analysis\", \"literature-review\", \"paper-framing\", \"CoRL-2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

报告已生成并注册。核心发现：

**竞品覆盖**：8 篇竞品已分析（ACoT-VLA、ReconVLA、SC-VLA、VLA-Pilot、AsyncVLA、A2C2、PLD、SRPO）。paper_framing.md 和 literature_map.yaml 的覆盖率很好，主要缺失 **AsyncVLA** (arXiv:2511.14148)。

**关键数据点**：
- ACoT-VLA: LIBERO 98.5%, LIBERO-Plus 84.1% — CVPR 2026，confirmed SOTA
- ReconVLA: AAAI 2026 Outstanding Paper — 需在 paper_framing.md 中标注
- SC-VLA: ManiSkill +9% SR，但未在 LIBERO 评估
- 无竞品使用 per-DOF conformal statistics 作为 learned correction 输入

**建议行动**：
1. `literature_map.yaml` 新增 AsyncVLA 条目
2. paper_framing.md Gap 段补充 AsyncVLA 的 confidence-guided refinement 作为对比
3. ReconVLA 条目补充 AAAI 2026 Outstanding Paper 信息
4. 论文叙事策略：强调 relative improvement (+22.5pp) 和 stacking potential，而非与 7B+ backbone 方法做绝对数值竞争

Sources:
- [ACoT-VLA (CVPR 2026)](https://arxiv.org/abs/2601.11404)
- [SC-VLA](https://arxiv.org/abs/2602.21633)
- [VLA-Pilot](https://arxiv.org/abs/2511.14178)
- [AsyncVLA](https://arxiv.org/abs/2511.14148)
- [ReconVLA](https://arxiv.org/html/2604.16677v1)
- [A2C2](https://arxiv.org/abs/2509.23224)
- [PLD (ICLR 2026)](https://arxiv.org/abs/2511.00091)
- [SRPO](https://arxiv.org/abs/2511.15605)
- [Conformal Risk Control for HRI](https://arxiv.org/abs/2603.10392)
- [ICLR 2026 VLA landscape](https://mbreuss.github.io/blog_post_iclr_26_vla.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "uuid": "9fb59ea4-1b39-48b4-be14-82095ce54ac2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfzdudPDoewobZjwN25yr7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 61930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 609
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

_source line 60_

报告已生成并注册。核心发现：

**竞品覆盖**：8 篇竞品已分析（ACoT-VLA、ReconVLA、SC-VLA、VLA-Pilot、AsyncVLA、A2C2、PLD、SRPO）。paper_framing.md 和 literature_map.yaml 的覆盖率很好，主要缺失 **AsyncVLA** (arXiv:2511.14148)。

**关键数据点**：
- ACoT-VLA: LIBERO 98.5%, LIBERO-Plus 84.1% — CVPR 2026，confirmed SOTA
- ReconVLA: AAAI 2026 Outstanding Paper — 需在 paper_framing.md 中标注
- SC-VLA: ManiSkill +9% SR，但未在 LIBERO 评估
- 无竞品使用 per-DOF conformal statistics 作为 learned correction 输入

**建议行动**：
1. `literature_map.yaml` 新增 AsyncVLA 条目
2. paper_framing.md Gap 段补充 AsyncVLA 的 confidence-guided refinement 作为对比
3. ReconVLA 条目补充 AAAI 2026 Outstanding Paper 信息
4. 论文叙事策略：强调 relative improvement (+22.5pp) 和 stacking potential，而非与 7B+ backbone 方法做绝对数值竞争

Sources:
- [ACoT-VLA (CVPR 2026)](https://arxiv.org/abs/2601.11404)
- [SC-VLA](https://arxiv.org/abs/2602.21633)
- [VLA-Pilot](https://arxiv.org/abs/2511.14178)
- [AsyncVLA](https://arxiv.org/abs/2511.14148)
- [ReconVLA](https://arxiv.org/html/2604.16677v1)
- [A2C2](https://arxiv.org/abs/2509.23224)
- [PLD (ICLR 2026)](https://arxiv.org/abs/2511.00091)
- [SRPO](https://arxiv.org/abs/2511.15605)
- [Conformal Risk Control for HRI](https://arxiv.org/abs/2603.10392)
- [ICLR 2026 VLA landscape](https://mbreuss.github.io/blog_post_iclr_26_vla.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 197780,
  "duration_api_ms": 292429,
  "num_turns": 23,
  "stop_reason": "end_turn",
  "session_id": "12249461-90f8-4a62-abf2-d18d5a75d299",
  "total_cost_usd": 1.1992379999999998,
  "usage": {
    "input_tokens": 924,
    "cache_creation_input_tokens": 50698,
    "cache_read_input_tokens": 330635,
    "output_tokens": 6757,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 50698,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 662,
        "cache_read_input_tokens": 61930,
        "cache_creation_input_tokens": 609,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 609
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 324438,
      "outputTokens": 7815,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 18,
      "costUSD": 0.5435129999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 924,
      "outputTokens": 6757,
      "cacheReadInputTokens": 330635,
      "cacheCreationInputTokens": 50698,
      "webSearchRequests": 0,
      "costUSD": 0.655725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a506a593-1c04-4579-8a3e-417d219f6003"
}
```

</details>

---
