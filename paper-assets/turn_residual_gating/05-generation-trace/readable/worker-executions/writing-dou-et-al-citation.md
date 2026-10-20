# writing dou et al citation

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_writing_dou-et-al-citation_20260525T224600.log`
- **Structured JSON:** [`378e12645f7c7b59b29e.json`](../../sessions/37/378e12645f7c7b59b29e.json)

## Before a recorded user message

6 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
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
  "uuid": "7b2e8a49-1e5a-47cf-9c72-33c0667b655d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779782400,
    "rateLimitType": "seven_day",
    "utilization": 0.83,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "f1433765-13a0-46a6-adc7-295aa049e9a2",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777"
}
```

---

### Assistant

_source line 4_

I'll search for the paper information, find the bib file, and locate the discussion sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "49e1088f-f5a2-4ded-b89a-0a6c4d2c7228",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFV1iHLhiMJsJF76cejqpk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13537,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13537
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

<details open><summary>🔧 Tool call — Agent · `toolu_01GHXSdcVh8dbHCdXHG7tDBP`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find bib and discussion files",
  "prompt": "Find all .bib files and discussion.tex files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating. Search patterns: \"**/*.bib\" and \"**/discussion.tex\". Report all matching file paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "eae3bc0c-eb47-4581-b562-c59f59773bd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFV1iHLhiMJsJF76cejqpk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13537,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13537
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

### System

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a6f7d27fa6db0615d",
  "tool_use_id": "toolu_01GHXSdcVh8dbHCdXHG7tDBP",
  "description": "Find bib and discussion files",
  "task_type": "local_agent",
  "prompt": "Find all .bib files and discussion.tex files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating. Search patterns: \"**/*.bib\" and \"**/discussion.tex\". Report all matching file paths.",
  "uuid": "73c87f58-5bb4-4e2a-bbc2-12549f78bdfb",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777"
}
```

---

## Round 1

47 recorded events

### User

_source line 7 · 2026-05-25T22:46:15.735Z_

Find all .bib files and discussion.tex files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating. Search patterns: "**/*.bib" and "**/discussion.tex". Report all matching file paths.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GHXSdcVh8dbHCdXHG7tDBP",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "f9ad013f-4ad6-4aec-9cf4-a9ffd3d219f4"
}
```

</details>

---

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6f7d27fa6db0615d",
  "tool_use_id": "toolu_01GHXSdcVh8dbHCdXHG7tDBP",
  "description": "Finding **/*.bib",
  "usage": {
    "total_tokens": 15463,
    "tool_uses": 1,
    "duration_ms": 1693
  },
  "last_tool_name": "Glob",
  "uuid": "347668b9-a649-450c-8e4d-c6a9ebfa961b",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777"
}
```

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01SknxsxGypEKA8aZgEg89Fm`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GHXSdcVh8dbHCdXHG7tDBP",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "c2a3d456-dfa6-472e-89dd-ffbecf73188b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PsGxim15qX1sgVJzv5L5iY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15454,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15454,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 10 · 2026-05-25T22:46:17.470Z_

<details><summary>↩ Tool result · `toolu_01SknxsxGypEKA8aZgEg89Fm`</summary>

```text
artifacts/dream_reports/dream_20260519T135115/median/references.bib
artifacts/dream_reports/dream_20260519T145320/best/custom.bib
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GHXSdcVh8dbHCdXHG7tDBP",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "b2372717-3405-4fff-b0e1-d23f70fd65eb"
}
```

</details>

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6f7d27fa6db0615d",
  "tool_use_id": "toolu_01GHXSdcVh8dbHCdXHG7tDBP",
  "description": "Finding **/discussion.tex",
  "usage": {
    "total_tokens": 15466,
    "tool_uses": 2,
    "duration_ms": 1810
  },
  "last_tool_name": "Glob",
  "uuid": "b8806ea4-c96e-4f68-9ff6-f3f7c7351451",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01Uw6BK6nMnf1zTMKAtzXUNr`</summary>

```json
{
  "pattern": "**/discussion.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GHXSdcVh8dbHCdXHG7tDBP",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "d0562e5c-b900-45f0-a990-7367e8eb78ed",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PsGxim15qX1sgVJzv5L5iY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15454,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15454,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 13 · 2026-05-25T22:46:17.589Z_

<details><summary>↩ Tool result · `toolu_01Uw6BK6nMnf1zTMKAtzXUNr`</summary>

```text
paper/sections/discussion.tex
docs/paper/sections/discussion.tex
docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GHXSdcVh8dbHCdXHG7tDBP",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "be838dd5-9828-4f52-82e2-f7892e3f20bf"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a6f7d27fa6db0615d",
  "tool_use_id": "toolu_01GHXSdcVh8dbHCdXHG7tDBP",
  "status": "completed",
  "output_file": "",
  "summary": "Find bib and discussion files",
  "usage": {
    "total_tokens": 16645,
    "tool_uses": 2,
    "duration_ms": 5612
  },
  "uuid": "ff5a3e45-8353-402c-bc3d-4be9d2793f15",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777"
}
```

---

### Tool result

_source line 15 · 2026-05-25T22:46:21.349Z_

<details><summary>↩ Tool result · `toolu_01GHXSdcVh8dbHCdXHG7tDBP`</summary>

```text
Here are all the matching files found in the project:

**Bibliography files (.bib):**
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/references.bib
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/custom.bib
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib

**Discussion files (discussion.tex):**
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "168dc5db-2d9e-437c-83ca-ea01b90bc3b9",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find all .bib files and discussion.tex files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating. Search patterns: \"**/*.bib\" and \"**/discussion.tex\". Report all matching file paths.",
    "agentId": "a6f7d27fa6db0615d",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Here are all the matching files found in the project:\n\n**Bibliography files (.bib):**\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/references.bib\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/custom.bib\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib\n\n**Discussion files (discussion.tex):**\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/discussion.tex"
      }
    ],
    "totalDurationMs": 5614,
    "totalTokens": 16931,
    "totalToolUseCount": 2,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1174,
      "cache_read_input_tokens": 15454,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1174
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 296,
          "cache_read_input_tokens": 15454,
          "cache_creation_input_tokens": 1174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1174,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 2,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Do7pfyj8F1rpR4t3Yxhy6Y`</summary>

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
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "cf33e9dd-b800-4f71-8edb-f872e3f396ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwjV1ycW9KJ6FXgMou1ica",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 488,
      "cache_read_input_tokens": 25378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 488
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

_source line 17 · 2026-05-25T22:46:24.432Z_

<details><summary>↩ Tool result · `toolu_01Do7pfyj8F1rpR4t3Yxhy6Y`</summary>

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
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "f55ef0a5-0c27-483c-a25c-b6cd53b25ff3",
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

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the paper, read the bib file, and read both discussion.tex files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "c1b02328-4469-484a-a267-b652a1f37108",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATcJFHNuddnac7QTuVPUzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VFracwFUQXN7PTepCPEvo3`</summary>

```json
{
  "query": "Dou et al. 2024 \"Attention Forcing\" LLM autoregressive generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "a6bdf881-202f-470e-957a-26965d89cb61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATcJFHNuddnac7QTuVPUzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — Read · `toolu_016oDL94w8VpJkhKQV31mbkC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "7350ab4e-5076-4803-85a2-749f6c4e16fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATcJFHNuddnac7QTuVPUzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
      },
      "output_tokens": 21,
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

_source line 21 · 2026-05-25T22:46:30.293Z_

<details><summary>↩ Tool result · `toolu_016oDL94w8VpJkhKQV31mbkC`</summary>

```text
1	% ============================================================
2	% Multi-Turn Attention
3	% ============================================================
4	
5	@article{dongre2026attention,
6	  author  = {Dongre, Vardhan and Hsieh, Joseph and Lai, Viet Dac and Yoon, Seunghyun and Bui, Trung and Hakkani-T\"{u}r, Dilek},
7	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},
8	  journal = {arXiv preprint arXiv:2605.12922},
9	  year    = {2026},
10	  url     = {https://arxiv.org/abs/2605.12922}
11	}
12	
13	@article{hong2025rhea,
14	  author  = {Hong, Wanyang and Zhang, Zhaoning and Chen, Yi and Zhang, Libo and Liu, Baihui and Qiao, Linbo and Tian, Zhiliang and Li, Dongsheng},
15	  title   = {{Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs}},
16	  journal = {arXiv preprint arXiv:2512.06869},
17	  year    = {2025},
18	  url     = {https://arxiv.org/abs/2512.06869}
19	}
20	
21	@article{laban2025lost,
22	  author  = {Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},
23	  title   = {{LLMs Get Lost In Multi-Turn Conversation}},
24	  journal = {arXiv preprint arXiv:2505.06120},
25	  year    = {2025},
26	  url     = {https://arxiv.org/abs/2505.06120}
27	}
28	
29	@article{liu2026intent,
30	  author  = {Liu, Geng and Zhu, Fei and Feng, Rong and Ma, Changyi and Wang, Shiqi and Meng, Gaofeng},
31	  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},
32	  journal = {arXiv preprint arXiv:2602.07338},
33	  year    = {2026},
34	  url     = {https://arxiv.org/abs/2602.07338}
35	}
36	
37	@inproceedings{bai2024mtbench101,
38	  author    = {Bai, Ge and Liu, Jie and Bu, Xingyuan and He, Yancheng and Liu, Jiaheng and Zhou, Zhanhui and Lin, Zhuoran and Su, Wenbo and Ge, Tiezheng and Zheng, Bo and Ouyang, Wanli},
39	  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},
40	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
41	  year      = {2024},
42	  url       = {https://arxiv.org/abs/2402.14762}
43	}
44	
45	% ============================================================
46	% Residual Gating and Adaptive Depth
47	% ============================================================
48	
49	@inproceedings{fan2020layerdrop,
50	  author    = {Fan, Angela and Grave, Edouard and Joulin, Armand},
51	  title     = {{Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)}},
52	  booktitle = {International Conference on Learning Representations},
53	  year      = {2020},
54	  url       = {https://arxiv.org/abs/1909.11556}
55	}
56	
57	@inproceedings{raposo2024mixture,
58	  author    = {Raposo, David and Ritter, Sam and Richards, Blake and Lillicrap, Timothy and Humphreys, Peter Conway and Santoro, Adam},
59	  title     = {{Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models}},
60	  booktitle = {International Conference on Machine Learning},
61	  year      = {2024},
62	  url       = {https://arxiv.org/abs/2404.02258}
63	}
64	
65	@inproceedings{schuster2022calm,
66	  author    = {Schuster, Tal and Fisch, Adam and Gupta, Jai and Dehghani, Mostafa and Bahri, Dara and Tran, Vinh Q. and Tay, Yi and Metzler, Donald},
67	  title     = {{Confident Adaptive Language Modeling}},
68	  booktitle = {Advances in Neural Information Processing Systems},
69	  year      = {2022},
70	  url       = {https://arxiv.org/abs/2207.07061}
71	}
72	
73	@inproceedings{qiu2025gated,
74	  author    = {Qiu, Zihan and Wang, Zekun and Zheng, Bo and Huang, Zeyu and Wen, Kaiyue and Yang, Songlin and Men, Rui and Yu, Le and Huang, Fei and Huang, Suozhi and Liu, Dayiheng and Zhou, Jingren and Lin, Junyang},
75	  title     = {{Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free}},
76	  booktitle = {Advances in Neural Information Processing Systems},
77	  year      = {2025},
78	  url       = {https://arxiv.org/abs/2505.06708}
79	}
80	
81	@inproceedings{luo2025flexidepth,
82	  author    = {Luo, Xuan and Wang, Weizhi and Yan, Xifeng},
83	  title     = {{Adaptive Layer-skipping in Pre-trained LLMs}},
84	  booktitle = {Conference on Language Modeling},
85	  year      = {2025},
86	  url     = {https://arxiv.org/abs/2503.23798}
87	}
88	
89	% ============================================================
90	% Attention Manipulation
91	% ============================================================
92	
93	@inproceedings{xiao2024streaming,
94	  author    = {Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},
95	  title     = {{Efficient Streaming Language Models with Attention Sinks}},
96	  booktitle = {International Conference on Learning Representations},
97	  year      = {2024},
98	  url       = {https://arxiv.org/abs/2309.17453}
99	}
100	
101	@inproceedings{zhang2024tell,
102	  author    = {Zhang, Qingru and Singh, Chandan and Liu, Liyuan and Liu, Xiaodong and Yu, Bin and Gao, Jianfeng and Zhao, Tuo},
103	  title     = {{Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs}},
104	  booktitle = {International Conference on Learning Representations},
105	  year      = {2024},
106	  url       = {https://arxiv.org/abs/2311.02262}
107	}
108	
109	@inproceedings{hsieh2024found,
110	  author    = {Hsieh, Cheng-Yu and Chuang, Yung-Sung and Li, Chun-Liang and Wang, Zifeng and Le, Long and Kumar, Abhishek and Glass, James and Ratner, Alexander and Lee, Chen-Yu and Krishna, Ranjay and Pfister, Tomas},
111	  title     = {{Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization}},
112	  booktitle = {Findings of the Association for Computational Linguistics: ACL},
113	  year      = {2024},
114	  url       = {https://arxiv.org/abs/2406.16008}
115	}
116	
117	% ============================================================
118	% Exposure Bias
119	% ============================================================
120	
121	@inproceedings{bengio2015scheduled,
122	  author    = {Bengio, Samy and Vinyals, Oriol and Jaitly, Navdeep and Shazeer, Noam},
123	  title     = {{Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}},
124	  booktitle = {Advances in Neural Information Processing Systems},
125	  year      = {2015},
126	  url       = {https://arxiv.org/abs/1506.03099}
127	}
128	
129	@inproceedings{ranzato2016sequence,
130	  author    = {Ranzato, Marc'Aurelio and Chopra, Sumit and Auli, Michael and Zaremba, Wojciech},
131	  title     = {{Sequence Level Training with Recurrent Neural Networks}},
132	  booktitle = {International Conference on Learning Representations},
133	  year      = {2016},
134	  url       = {https://arxiv.org/abs/1511.06732}
135	}
136	
137	@inproceedings{lamb2016professor,
138	  author    = {Lamb, Alex and Goyal, Anirudh and Zhang, Ying and Zhang, Saizheng and Courville, Aaron and Bengio, Yoshua},
139	  title     = {{Professor Forcing: A New Algorithm for Training Recurrent Networks}},
140	  booktitle = {Advances in Neural Information Processing Systems},
141	  year      = {2016},
142	  url       = {https://arxiv.org/abs/1610.09038}
143	}
144	
145	@inproceedings{leblond2018searnn,
146	  author    = {Leblond, R\'{e}mi and Alayrac, Jean-Baptiste and Osokin, Anton and Lacoste-Julien, Simon},
147	  title     = {{SEARNN: Training RNNs with Global-Local Losses}},
148	  booktitle = {International Conference on Learning Representations},
149	  year      = {2018},
150	  url       = {https://arxiv.org/abs/1706.04499}
151	}
152	
153	@article{he2019exposure,
154	  author  = {He, Tianxing and Zhang, Jingzhao and Zhou, Zhiming and Glass, James},
155	  title   = {{Quantifying Exposure Bias for Neural Language Generation}},
156	  journal = {arXiv preprint arXiv:1905.10617},
157	  year    = {2019},
158	  url     = {https://arxiv.org/abs/1905.10617}
159	}
160	
161	@inproceedings{wiseman2016sequence,
162	  author    = {Wiseman, Sam and Rush, Alexander M.},
163	  title     = {{Sequence-to-Sequence Learning as Beam-Search Optimization}},
164	  booktitle = {Conference on Empirical Methods in Natural Language Processing},
165	  year      = {2016},
166	  url       = {https://arxiv.org/abs/1606.02960}
167	}
168	
169	@inproceedings{arora2022exposure,
170	  author    = {Arora, Kushal and El Asri, Layla and Bahuleyan, Hareesh and Cheung, Jackie Chi Kit},
171	  title     = {{Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation}},
172	  booktitle = {Findings of the Association for Computational Linguistics: ACL},
173	  year      = {2022},
174	  url       = {https://arxiv.org/abs/2204.01171}
175	}
176	
177	% ============================================================
178	% Instruction Stability
179	% ============================================================
180	
181	@inproceedings{li2024measuring,
182	  author    = {Li, Kenneth and Liu, Tianle and Bashkansky, Naomi and Bau, David and Vi\'{e}gas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin},
183	  title     = {{Measuring and Controlling Instruction (In)Stability in Language Model Dialogs}},
184	  booktitle = {Conference on Language Modeling},
185	  year      = {2024},
186	  url       = {https://arxiv.org/abs/2402.10962}
187	}
188	
189	% ============================================================
190	% Gradient Conflict / Multi-Task Learning
191	% ============================================================
192	
193	@inproceedings{yu2020pcgrad,
194	  author    = {Yu, Tianhe and Kumar, Saurabh and Gupta, Abhishek and Levine, Sergey and Hausman, Karol and Finn, Chelsea},
195	  title     = {{Gradient Surgery for Multi-Task Learning}},
196	  booktitle = {Advances in Neural Information Processing Systems},
197	  year      = {2020},
198	  url       = {https://arxiv.org/abs/2001.06782}
199	}
200	
201	@inproceedings{chen2018gradnorm,
202	  author    = {Chen, Zhao and Badrinarayanan, Vijay and Lee, Chen-Yu and Rabinovich, Andrew},
203	  title     = {{GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks}},
204	  booktitle = {International Conference on Machine Learning},
205	  year      = {2018},
206	  url       = {https://arxiv.org/abs/1711.02257}
207	}
208	
209	@inproceedings{liu2021cagrad,
210	  author    = {Liu, Bo and Liu, Xingchao and Jin, Xiaojie and Stone, Peter and Liu, Qiang},
211	  title     = {{Conflict-Averse Gradient Descent for Multi-task Learning}},
212	  booktitle = {Advances in Neural Information Processing Systems},
213	  year      = {2021},
214	  url       = {https://arxiv.org/abs/2110.14048}
215	}
216	
217	@inproceedings{navon2022nash,
218	  author    = {Navon, Aviv and Shamsian, Aviv and Achituve, Idan and Maron, Haggai and Kawaguchi, Kenji and Chechik, Gal and Fetaya, Ethan},
219	  title     = {{Multi-Task Learning as a Bargaining Game}},
220	  booktitle = {International Conference on Machine Learning},
221	  year      = {2022},
222	  url       = {https://arxiv.org/abs/2202.01017}
223	}
224	
225	% ============================================================
226	% Residual Scaling
227	% ============================================================
228	
229	@inproceedings{bachlechner2021rezero,
230	  author    = {Bachlechner, Thomas and Majumder, Bodhisattwa Prasad and Mao, Henry and Cottrell, Gary and McAuley, Julian},
231	  title     = {{ReZero is All You Need: Fast Convergence at Large Depth}},
232	  booktitle = {Uncertainty in Artificial Intelligence},
233	  year      = {2021},
234	  url       = {https://arxiv.org/abs/2003.04887}
235	}
236	
237	@article{grattafiori2024llama3,
238	  author  = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and others},
239	  title   = {{The Llama 3 Herd of Models}},
240	  journal = {arXiv preprint arXiv:2407.21783},
241	  year    = {2024},
242	  url     = {https://arxiv.org/abs/2407.21783}
243	}
244	
245	@inproceedings{gromov2024unreasonable,
246	  author    = {Gromov, Andrey and Tirumala, Kushal and Shapourian, Hassan and Glorioso, Paolo and Roberts, Daniel A.},
247	  title     = {{The Unreasonable Ineffectiveness of the Deeper Layers}},
248	  booktitle = {International Conference on Learning Representations},
249	  year      = {2025},
250	  url       = {https://arxiv.org/abs/2403.17887}
251	}
252	
253	% ============================================================
254	% Foundational Architecture
255	% ============================================================
256	
257	@inproceedings{vaswani2017attention,
258	  author    = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N. and Kaiser, {\L}ukasz and Polosukhin, Illia},
259	  title     = {{Attention Is All You Need}},
260	  booktitle = {Advances in Neural Information Processing Systems},
261	  year      = {2017},
262	  url       = {https://arxiv.org/abs/1706.03762}
263	}
264	
265	@inproceedings{he2016deep,
266	  author    = {He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian},
267	  title     = {{Deep Residual Learning for Image Recognition}},
268	  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition},
269	  year      = {2016},
270	  url       = {https://arxiv.org/abs/1512.03385}
271	}
272	
273	@inproceedings{srivastava2015highway,
274	  author    = {Srivastava, Rupesh Kumar and Greff, Klaus and Schmidhuber, J{\"u}rgen},
275	  title     = {{Highway Networks}},
276	  booktitle = {International Conference on Machine Learning Deep Learning Workshop},
277	  year      = {2015},
278	  url       = {https://arxiv.org/abs/1505.00387}
279	}
280	
281	% ============================================================
282	% Parameter-Efficient Fine-Tuning
283	% ============================================================
284	
285	@inproceedings{hu2022lora,
286	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
287	  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},
288	  booktitle = {International Conference on Learning Representations},
289	  year      = {2022},
290	  url       = {https://arxiv.org/abs/2106.09685}
291	}
292	
293	% ============================================================
294	% Multi-Turn Dialogue Systems
295	% ============================================================
296	
297	@inproceedings{zhang2020dialogpt,
298	  author    = {Zhang, Yizhe and Sun, Siqi and Galley, Michel and Chen, Yen-Chun and Brockett, Chris and Gao, Xiang and Gao, Jianfeng and Liu, Jingjing and Dolan, Bill},
299	  title     = {{DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation}},
300	  booktitle = {Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
301	  year      = {2020},
302	  url       = {https://arxiv.org/abs/1911.00536}
303	}
304	
305	@inproceedings{roller2021recipes,
306	  author    = {Roller, Stephen and Dinan, Emily and Goyal, Naman and Ju, Da and Williamson, Mary and Liu, Yinhan and Xu, Jing and Ott, Myle and Smith, Eric Michael and Boureau, Y-Lan and Weston, Jason},
307	  title     = {{Recipes for Building an Open-Domain Chatbot}},
308	  booktitle = {Conference of the European Chapter of the Association for Computational Linguistics},
309	  year      = {2021},
310	  url       = {https://arxiv.org/abs/2004.13637}
311	}
312	
313	@inproceedings{zheng2024judging,
314	  author    = {Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},
315	  title     = {{Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena}},
316	  booktitle = {Advances in Neural Information Processing Systems},
317	  year      = {2023},
318	  url       = {https://arxiv.org/abs/2306.05685}
319	}
320	
321	% ============================================================
322	% Attention Analysis
323	% ============================================================
324	
325	@inproceedings{clark2019what,
326	  author    = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},
327	  title     = {{What Does BERT Look At? An Analysis of BERT's Attention}},
328	  booktitle = {ACL Workshop on BlackboxNLP},
329	  year      = {2019},
330	  url       = {https://arxiv.org/abs/1906.04341}
331	}
332	
333	@inproceedings{voita2019analyzing,
334	  author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},
335	  title     = {{Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned}},
336	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
337	  year      = {2019},
338	  url       = {https://arxiv.org/abs/1905.09418}
339	}
340	
341	@inproceedings{kovaleva2019revealing,
342	  author    = {Kovaleva, Olga and Romanov, Alexey and Rogers, Anna and Rumshisky, Anna},
343	  title     = {{Revealing the Dark Secrets of BERT}},
344	  booktitle = {Conference on Empirical Methods in Natural Language Processing},
345	  year      = {2019},
346	  url       = {https://arxiv.org/abs/1908.08593}
347	}
348	
349	% ============================================================
350	% Long Context and Positional Bias
351	% ============================================================
352	
353	@article{liu2024lost,
354	  author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},
355	  title   = {{Lost in the Middle: How Language Models Use Long Contexts}},
356	  journal = {Transactions of the Association for Computational Linguistics},
357	  year    = {2024},
358	  url     = {https://arxiv.org/abs/2307.03172}
359	}
360	
361	% ============================================================
362	% Exposure Bias (additional)
363	% ============================================================
364	
365	@inproceedings{zhang2019bridging,
366	  author    = {Zhang, Wen and Feng, Yang and Meng, Fandong and You, Di and Liu, Qun},
367	  title     = {{Bridging the Gap between Training and Inference for Neural Machine Translation}},
368	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
369	  year      = {2019},
370	  url       = {https://arxiv.org/abs/1906.02448}
371	}
372	
373	% ============================================================
374	% Exposure Bias (transformer-era)
375	% ============================================================
376	
377	@inproceedings{mihaylova2019scheduled,
378	  author    = {Mihaylova, Tsvetomila and Martins, Andr\'{e} F. T.},
379	  title     = {{Scheduled Sampling for Transformers}},
380	  booktitle = {Annual Meeting of the Association for Computational Linguistics: Student Research Workshop},
381	  pages     = {351--356},
382	  year      = {2019},
383	  url       = {https://aclanthology.org/P19-2049/}
384	}
385	
386	% ============================================================
387	% Attention Forcing
388	% ============================================================
389	
390	@article{dou2019attention,
391	  author  = {Dou, Qingyun and Lu, Yiting and Efiong, Joshua and Gales, Mark J. F.},
392	  title   = {{Attention Forcing for Sequence-to-sequence Model Training}},
393	  journal = {arXiv preprint arXiv:1909.12289},
394	  year    = {2019},
395	  url     = {https://arxiv.org/abs/1909.12289}
396	}
397	
398	@article{dou2022parallel,
399	  author  = {Dou, Qingyun and Gales, Mark J. F.},
400	  title   = {{Parallel Attention Forcing for Machine Translation}},
401	  journal = {arXiv preprint arXiv:2211.03237},
402	  year    = {2022},
403	  url     = {https://arxiv.org/abs/2211.03237}
404	}
405	
406	% ============================================================
407	% Multi-Turn Dialogue (additional)
408	% ============================================================
409	
410	@inproceedings{li2016persona,
411	  author    = {Li, Jiwei and Galley, Michel and Brockett, Chris and Spithourakis, Georgios and Gao, Jianfeng and Dolan, Bill},
412	  title     = {{A Persona-Based Neural Conversation Model}},
413	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
414	  pages     = {994--1003},
415	  year      = {2016},
416	  url       = {https://aclanthology.org/P16-1094/}
417	}
418	
419	@inproceedings{xu2022goldfish,
420	  author    = {Xu, Jing and Szlam, Arthur and Weston, Jason},
421	  title     = {{Beyond Goldfish Memory: Long-Term Open-Domain Conversation}},
422	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
423	  pages     = {5180--5197},
424	  year      = {2022},
425	  url       = {https://aclanthology.org/2022.acl-long.356/}
426	}
427	
428	% ============================================================
429	% Attention Analysis (additional)
430	% ============================================================
431	
432	@inproceedings{vig2019multiscale,
433	  author    = {Vig, Jesse},
434	  title     = {{A Multiscale Visualization of Attention in the Transformer Model}},
435	  booktitle = {Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
436	  pages     = {37--42},
437	  year      = {2019},
438	  url       = {https://aclanthology.org/P19-3007/}
439	}
440	
441	@inproceedings{abnar2020quantifying,
442	  author    = {Abnar, Samira and Zuidema, Willem},
443	  title     = {{Quantifying Attention Flow in Transformers}},
444	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
445	  pages     = {4190--4197},
446	  year      = {2020},
447	  url       = {https://aclanthology.org/2020.acl-main.385/}
448	}
449	
450	@inproceedings{ethayarajh2019contextual,
451	  author    = {Ethayarajh, Kawin},
452	  title     = {{How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings}},
453	  booktitle = {Conference on Empirical Methods in Natural Language Processing},
454	  pages     = {55--65},
455	  year      = {2019},
456	  url       = {https://aclanthology.org/D19-1006/}
457	}
458	
459	@inproceedings{brunner2020identifiability,
460	  author    = {Brunner, Gino and Liu, Yang and Pascual, Damian and Richter, Oliver and Ciaramita, Massimiliano and Krause, Andreas},
461	  title     = {{On Identifiability in Transformers}},
462	  booktitle = {International Conference on Learning Representations},
463	  year      = {2020},
464	  url       = {https://arxiv.org/abs/1908.04211}
465	}
466	
467	% ============================================================
468	% Residual Theory and Depth (additional)
469	% ============================================================
470	
471	@inproceedings{veit2016residual,
472	  author    = {Veit, Andreas and Wilber, Michael and Belongie, Serge},
473	  title     = {{Residual Networks Behave Like Ensembles of Relatively Shallow Networks}},
474	  booktitle = {Advances in Neural Information Processing Systems},
475	  year      = {2016},
476	  url       = {https://arxiv.org/abs/1605.06431}
477	}
478	
479	@inproceedings{dong2021attention,
480	  author    = {Dong, Yihe and Cordonnier, Jean-Baptiste and Loukas, Andreas},
481	  title     = {{Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth}},
482	  booktitle = {International Conference on Machine Learning},
483	  pages     = {2793--2803},
484	  year      = {2021},
485	  url       = {https://arxiv.org/abs/2103.03404}
486	}
487	
488	@inproceedings{zhou2020drophead,
489	  author    = {Zhou, Wangchunshu and Ge, Tao and Wei, Furu and Zhou, Ming and Xu, Ke},
490	  title     = {{Scheduled DropHead: A Regularization Method for Transformer Models}},
491	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP},
492	  year      = {2020},
493	  url       = {https://arxiv.org/abs/2004.13342}
494	}
495	
496	% ============================================================
497	% Gating Mechanisms
498	% ============================================================
499	
500	@inproceedings{dauphin2017language,
501	  author    = {Dauphin, Yann N. and Fan, Angela and Auli, Michael and Grangier, David},
502	  title     = {{Language Modeling with Gated Convolutional Networks}},
503	  booktitle = {International Conference on Machine Learning},
504	  pages     = {933--941},
505	  year      = {2017},
506	  url       = {https://arxiv.org/abs/1612.08083}
507	}
508	
509	@article{shazeer2020glu,
510	  author  = {Shazeer, Noam},
511	  title   = {{GLU Variants Improve Transformer}},
512	  journal = {arXiv preprint arXiv:2002.05202},
513	  year    = {2020},
514	  url     = {https://arxiv.org/abs/2002.05202}
515	}
516	
517	% ============================================================
518	% Evaluation Benchmarks
519	% ============================================================
520	
521	@inproceedings{lin2022truthfulqa,
522	  author    = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},
523	  title     = {{TruthfulQA: Measuring How Models Mimic Human Falsehoods}},
524	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
525	  pages     = {3214--3252},
526	  year      = {2022},
527	  url       = {https://aclanthology.org/2022.acl-long.229/}
528	}
529	
530	@inproceedings{hendrycks2021measuring,
531	  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
532	  title     = {{Measuring Massive Multitask Language Understanding}},
533	  booktitle = {International Conference on Learning Representations},
534	  year      = {2021},
535	  url       = {https://arxiv.org/abs/2009.03300}
536	}
537	
538	% ============================================================
539	% Parameter-Efficient Fine-Tuning (additional)
540	% ============================================================
541	
542	@inproceedings{dettmers2023qlora,
543	  author    = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
544	  title     = {{QLoRA: Efficient Finetuning of Quantized LLMs}},
545	  booktitle = {Advances in Neural Information Processing Systems},
546	  year      = {2023},
547	  url       = {https://arxiv.org/abs/2305.14314}
548	}
549	
550	% ============================================================
551	% Dataset
552	% ============================================================
553	
554	@inproceedings{ding2023ultrachat,
555	  author    = {Ding, Ning and Chen, Yulin and Xu, Bokai and Qin, Yujia and Zheng, Zhi and Hu, Shengding and Liu, Zhiyuan and Sun, Maosong and Zhou, Bowen},
556	  title     = {{Enhancing Chat Language Models by Scaling High-quality Instructional Conversations}},
557	  booktitle = {Conference on Empirical Methods in Natural Language Processing},
558	  year      = {2023},
559	  url     = {https://arxiv.org/abs/2305.14233}
560	}
561	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "cd9896c6-fa14-430a-b241-151f952068a1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
      "content": "% ============================================================\n% Multi-Turn Attention\n% ============================================================\n\n@article{dongre2026attention,\n  author  = {Dongre, Vardhan and Hsieh, Joseph and Lai, Viet Dac and Yoon, Seunghyun and Bui, Trung and Hakkani-T\\\"{u}r, Dilek},\n  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},\n  journal = {arXiv preprint arXiv:2605.12922},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2605.12922}\n}\n\n@article{hong2025rhea,\n  author  = {Hong, Wanyang and Zhang, Zhaoning and Chen, Yi and Zhang, Libo and Liu, Baihui and Qiao, Linbo and Tian, Zhiliang and Li, Dongsheng},\n  title   = {{Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs}},\n  journal = {arXiv preprint arXiv:2512.06869},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2512.06869}\n}\n\n@article{laban2025lost,\n  author  = {Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},\n  title   = {{LLMs Get Lost In Multi-Turn Conversation}},\n  journal = {arXiv preprint arXiv:2505.06120},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2505.06120}\n}\n\n@article{liu2026intent,\n  author  = {Liu, Geng and Zhu, Fei and Feng, Rong and Ma, Changyi and Wang, Shiqi and Meng, Gaofeng},\n  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},\n  journal = {arXiv preprint arXiv:2602.07338},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2602.07338}\n}\n\n@inproceedings{bai2024mtbench101,\n  author    = {Bai, Ge and Liu, Jie and Bu, Xingyuan and He, Yancheng and Liu, Jiaheng and Zhou, Zhanhui and Lin, Zhuoran and Su, Wenbo and Ge, Tiezheng and Zheng, Bo and Ouyang, Wanli},\n  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.14762}\n}\n\n% ============================================================\n% Residual Gating and Adaptive Depth\n% ============================================================\n\n@inproceedings{fan2020layerdrop,\n  author    = {Fan, Angela and Grave, Edouard and Joulin, Armand},\n  title     = {{Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/1909.11556}\n}\n\n@inproceedings{raposo2024mixture,\n  author    = {Raposo, David and Ritter, Sam and Richards, Blake and Lillicrap, Timothy and Humphreys, Peter Conway and Santoro, Adam},\n  title     = {{Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.02258}\n}\n\n@inproceedings{schuster2022calm,\n  author    = {Schuster, Tal and Fisch, Adam and Gupta, Jai and Dehghani, Mostafa and Bahri, Dara and Tran, Vinh Q. and Tay, Yi and Metzler, Donald},\n  title     = {{Confident Adaptive Language Modeling}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2207.07061}\n}\n\n@inproceedings{qiu2025gated,\n  author    = {Qiu, Zihan and Wang, Zekun and Zheng, Bo and Huang, Zeyu and Wen, Kaiyue and Yang, Songlin and Men, Rui and Yu, Le and Huang, Fei and Huang, Suozhi and Liu, Dayiheng and Zhou, Jingren and Lin, Junyang},\n  title     = {{Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2505.06708}\n}\n\n@inproceedings{luo2025flexidepth,\n  author    = {Luo, Xuan and Wang, Weizhi and Yan, Xifeng},\n  title     = {{Adaptive Layer-skipping in Pre-trained LLMs}},\n  booktitle = {Conference on Language Modeling},\n  year      = {2025},\n  url     = {https://arxiv.org/abs/2503.23798}\n}\n\n% ============================================================\n% Attention Manipulation\n% ============================================================\n\n@inproceedings{xiao2024streaming,\n  author    = {Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  title     = {{Efficient Streaming Language Models with Attention Sinks}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2309.17453}\n}\n\n@inproceedings{zhang2024tell,\n  author    = {Zhang, Qingru and Singh, Chandan and Liu, Liyuan and Liu, Xiaodong and Yu, Bin and Gao, Jianfeng and Zhao, Tuo},\n  title     = {{Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.02262}\n}\n\n@inproceedings{hsieh2024found,\n  author    = {Hsieh, Cheng-Yu and Chuang, Yung-Sung and Li, Chun-Liang and Wang, Zifeng and Le, Long and Kumar, Abhishek and Glass, James and Ratner, Alexander and Lee, Chen-Yu and Krishna, Ranjay and Pfister, Tomas},\n  title     = {{Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization}},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2406.16008}\n}\n\n% ============================================================\n% Exposure Bias\n% ============================================================\n\n@inproceedings{bengio2015scheduled,\n  author    = {Bengio, Samy and Vinyals, Oriol and Jaitly, Navdeep and Shazeer, Noam},\n  title     = {{Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2015},\n  url       = {https://arxiv.org/abs/1506.03099}\n}\n\n@inproceedings{ranzato2016sequence,\n  author    = {Ranzato, Marc'Aurelio and Chopra, Sumit and Auli, Michael and Zaremba, Wojciech},\n  title     = {{Sequence Level Training with Recurrent Neural Networks}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1511.06732}\n}\n\n@inproceedings{lamb2016professor,\n  author    = {Lamb, Alex and Goyal, Anirudh and Zhang, Ying and Zhang, Saizheng and Courville, Aaron and Bengio, Yoshua},\n  title     = {{Professor Forcing: A New Algorithm for Training Recurrent Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1610.09038}\n}\n\n@inproceedings{leblond2018searnn,\n  author    = {Leblond, R\\'{e}mi and Alayrac, Jean-Baptiste and Osokin, Anton and Lacoste-Julien, Simon},\n  title     = {{SEARNN: Training RNNs with Global-Local Losses}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1706.04499}\n}\n\n@article{he2019exposure,\n  author  = {He, Tianxing and Zhang, Jingzhao and Zhou, Zhiming and Glass, James},\n  title   = {{Quantifying Exposure Bias for Neural Language Generation}},\n  journal = {arXiv preprint arXiv:1905.10617},\n  year    = {2019},\n  url     = {https://arxiv.org/abs/1905.10617}\n}\n\n@inproceedings{wiseman2016sequence,\n  author    = {Wiseman, Sam and Rush, Alexander M.},\n  title     = {{Sequence-to-Sequence Learning as Beam-Search Optimization}},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1606.02960}\n}\n\n@inproceedings{arora2022exposure,\n  author    = {Arora, Kushal and El Asri, Layla and Bahuleyan, Hareesh and Cheung, Jackie Chi Kit},\n  title     = {{Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation}},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2204.01171}\n}\n\n% ============================================================\n% Instruction Stability\n% ============================================================\n\n@inproceedings{li2024measuring,\n  author    = {Li, Kenneth and Liu, Tianle and Bashkansky, Naomi and Bau, David and Vi\\'{e}gas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin},\n  title     = {{Measuring and Controlling Instruction (In)Stability in Language Model Dialogs}},\n  booktitle = {Conference on Language Modeling},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.10962}\n}\n\n% ============================================================\n% Gradient Conflict / Multi-Task Learning\n% ============================================================\n\n@inproceedings{yu2020pcgrad,\n  author    = {Yu, Tianhe and Kumar, Saurabh and Gupta, Abhishek and Levine, Sergey and Hausman, Karol and Finn, Chelsea},\n  title     = {{Gradient Surgery for Multi-Task Learning}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/2001.06782}\n}\n\n@inproceedings{chen2018gradnorm,\n  author    = {Chen, Zhao and Badrinarayanan, Vijay and Lee, Chen-Yu and Rabinovich, Andrew},\n  title     = {{GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1711.02257}\n}\n\n@inproceedings{liu2021cagrad,\n  author    = {Liu, Bo and Liu, Xingchao and Jin, Xiaojie and Stone, Peter and Liu, Qiang},\n  title     = {{Conflict-Averse Gradient Descent for Multi-task Learning}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2110.14048}\n}\n\n@inproceedings{navon2022nash,\n  author    = {Navon, Aviv and Shamsian, Aviv and Achituve, Idan and Maron, Haggai and Kawaguchi, Kenji and Chechik, Gal and Fetaya, Ethan},\n  title     = {{Multi-Task Learning as a Bargaining Game}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2202.01017}\n}\n\n% ============================================================\n% Residual Scaling\n% ============================================================\n\n@inproceedings{bachlechner2021rezero,\n  author    = {Bachlechner, Thomas and Majumder, Bodhisattwa Prasad and Mao, Henry and Cottrell, Gary and McAuley, Julian},\n  title     = {{ReZero is All You Need: Fast Convergence at Large Depth}},\n  booktitle = {Uncertainty in Artificial Intelligence},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2003.04887}\n}\n\n@article{grattafiori2024llama3,\n  author  = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and others},\n  title   = {{The Llama 3 Herd of Models}},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2407.21783}\n}\n\n@inproceedings{gromov2024unreasonable,\n  author    = {Gromov, Andrey and Tirumala, Kushal and Shapourian, Hassan and Glorioso, Paolo and Roberts, Daniel A.},\n  title     = {{The Unreasonable Ineffectiveness of the Deeper Layers}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2403.17887}\n}\n\n% ============================================================\n% Foundational Architecture\n% ============================================================\n\n@inproceedings{vaswani2017attention,\n  author    = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N. and Kaiser, {\\L}ukasz and Polosukhin, Illia},\n  title     = {{Attention Is All You Need}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1706.03762}\n}\n\n@inproceedings{he2016deep,\n  author    = {He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian},\n  title     = {{Deep Residual Learning for Image Recognition}},\n  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1512.03385}\n}\n\n@inproceedings{srivastava2015highway,\n  author    = {Srivastava, Rupesh Kumar and Greff, Klaus and Schmidhuber, J{\\\"u}rgen},\n  title     = {{Highway Networks}},\n  booktitle = {International Conference on Machine Learning Deep Learning Workshop},\n  year      = {2015},\n  url       = {https://arxiv.org/abs/1505.00387}\n}\n\n% ============================================================\n% Parameter-Efficient Fine-Tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2106.09685}\n}\n\n% ============================================================\n% Multi-Turn Dialogue Systems\n% ============================================================\n\n@inproceedings{zhang2020dialogpt,\n  author    = {Zhang, Yizhe and Sun, Siqi and Galley, Michel and Chen, Yen-Chun and Brockett, Chris and Gao, Xiang and Gao, Jianfeng and Liu, Jingjing and Dolan, Bill},\n  title     = {{DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/1911.00536}\n}\n\n@inproceedings{roller2021recipes,\n  author    = {Roller, Stephen and Dinan, Emily and Goyal, Naman and Ju, Da and Williamson, Mary and Liu, Yinhan and Xu, Jing and Ott, Myle and Smith, Eric Michael and Boureau, Y-Lan and Weston, Jason},\n  title     = {{Recipes for Building an Open-Domain Chatbot}},\n  booktitle = {Conference of the European Chapter of the Association for Computational Linguistics},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2004.13637}\n}\n\n@inproceedings{zheng2024judging,\n  author    = {Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {{Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2306.05685}\n}\n\n% ============================================================\n% Attention Analysis\n% ============================================================\n\n@inproceedings{clark2019what,\n  author    = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},\n  title     = {{What Does BERT Look At? An Analysis of BERT's Attention}},\n  booktitle = {ACL Workshop on BlackboxNLP},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1906.04341}\n}\n\n@inproceedings{voita2019analyzing,\n  author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},\n  title     = {{Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1905.09418}\n}\n\n@inproceedings{kovaleva2019revealing,\n  author    = {Kovaleva, Olga and Romanov, Alexey and Rogers, Anna and Rumshisky, Anna},\n  title     = {{Revealing the Dark Secrets of BERT}},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1908.08593}\n}\n\n% ============================================================\n% Long Context and Positional Bias\n% ============================================================\n\n@article{liu2024lost,\n  author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n  title   = {{Lost in the Middle: How Language Models Use Long Contexts}},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2307.03172}\n}\n\n% ============================================================\n% Exposure Bias (additional)\n% ============================================================\n\n@inproceedings{zhang2019bridging,\n  author    = {Zhang, Wen and Feng, Yang and Meng, Fandong and You, Di and Liu, Qun},\n  title     = {{Bridging the Gap between Training and Inference for Neural Machine Translation}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1906.02448}\n}\n\n% ============================================================\n% Exposure Bias (transformer-era)\n% ============================================================\n\n@inproceedings{mihaylova2019scheduled,\n  author    = {Mihaylova, Tsvetomila and Martins, Andr\\'{e} F. T.},\n  title     = {{Scheduled Sampling for Transformers}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics: Student Research Workshop},\n  pages     = {351--356},\n  year      = {2019},\n  url       = {https://aclanthology.org/P19-2049/}\n}\n\n% ============================================================\n% Attention Forcing\n% ============================================================\n\n@article{dou2019attention,\n  author  = {Dou, Qingyun and Lu, Yiting and Efiong, Joshua and Gales, Mark J. F.},\n  title   = {{Attention Forcing for Sequence-to-sequence Model Training}},\n  journal = {arXiv preprint arXiv:1909.12289},\n  year    = {2019},\n  url     = {https://arxiv.org/abs/1909.12289}\n}\n\n@article{dou2022parallel,\n  author  = {Dou, Qingyun and Gales, Mark J. F.},\n  title   = {{Parallel Attention Forcing for Machine Translation}},\n  journal = {arXiv preprint arXiv:2211.03237},\n  year    = {2022},\n  url     = {https://arxiv.org/abs/2211.03237}\n}\n\n% ============================================================\n% Multi-Turn Dialogue (additional)\n% ============================================================\n\n@inproceedings{li2016persona,\n  author    = {Li, Jiwei and Galley, Michel and Brockett, Chris and Spithourakis, Georgios and Gao, Jianfeng and Dolan, Bill},\n  title     = {{A Persona-Based Neural Conversation Model}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  pages     = {994--1003},\n  year      = {2016},\n  url       = {https://aclanthology.org/P16-1094/}\n}\n\n@inproceedings{xu2022goldfish,\n  author    = {Xu, Jing and Szlam, Arthur and Weston, Jason},\n  title     = {{Beyond Goldfish Memory: Long-Term Open-Domain Conversation}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  pages     = {5180--5197},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.acl-long.356/}\n}\n\n% ============================================================\n% Attention Analysis (additional)\n% ============================================================\n\n@inproceedings{vig2019multiscale,\n  author    = {Vig, Jesse},\n  title     = {{A Multiscale Visualization of Attention in the Transformer Model}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  pages     = {37--42},\n  year      = {2019},\n  url       = {https://aclanthology.org/P19-3007/}\n}\n\n@inproceedings{abnar2020quantifying,\n  author    = {Abnar, Samira and Zuidema, Willem},\n  title     = {{Quantifying Attention Flow in Transformers}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  pages     = {4190--4197},\n  year      = {2020},\n  url       = {https://aclanthology.org/2020.acl-main.385/}\n}\n\n@inproceedings{ethayarajh2019contextual,\n  author    = {Ethayarajh, Kawin},\n  title     = {{How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings}},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  pages     = {55--65},\n  year      = {2019},\n  url       = {https://aclanthology.org/D19-1006/}\n}\n\n@inproceedings{brunner2020identifiability,\n  author    = {Brunner, Gino and Liu, Yang and Pascual, Damian and Richter, Oliver and Ciaramita, Massimiliano and Krause, Andreas},\n  title     = {{On Identifiability in Transformers}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/1908.04211}\n}\n\n% ============================================================\n% Residual Theory and Depth (additional)\n% ============================================================\n\n@inproceedings{veit2016residual,\n  author    = {Veit, Andreas and Wilber, Michael and Belongie, Serge},\n  title     = {{Residual Networks Behave Like Ensembles of Relatively Shallow Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1605.06431}\n}\n\n@inproceedings{dong2021attention,\n  author    = {Dong, Yihe and Cordonnier, Jean-Baptiste and Loukas, Andreas},\n  title     = {{Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth}},\n  booktitle = {International Conference on Machine Learning},\n  pages     = {2793--2803},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2103.03404}\n}\n\n@inproceedings{zhou2020drophead,\n  author    = {Zhou, Wangchunshu and Ge, Tao and Wei, Furu and Zhou, Ming and Xu, Ke},\n  title     = {{Scheduled DropHead: A Regularization Method for Transformer Models}},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/2004.13342}\n}\n\n% ============================================================\n% Gating Mechanisms\n% ============================================================\n\n@inproceedings{dauphin2017language,\n  author    = {Dauphin, Yann N. and Fan, Angela and Auli, Michael and Grangier, David},\n  title     = {{Language Modeling with Gated Convolutional Networks}},\n  booktitle = {International Conference on Machine Learning},\n  pages     = {933--941},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1612.08083}\n}\n\n@article{shazeer2020glu,\n  author  = {Shazeer, Noam},\n  title   = {{GLU Variants Improve Transformer}},\n  journal = {arXiv preprint arXiv:2002.05202},\n  year    = {2020},\n  url     = {https://arxiv.org/abs/2002.05202}\n}\n\n% ============================================================\n% Evaluation Benchmarks\n% ============================================================\n\n@inproceedings{lin2022truthfulqa,\n  author    = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  title     = {{TruthfulQA: Measuring How Models Mimic Human Falsehoods}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  pages     = {3214--3252},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.acl-long.229/}\n}\n\n@inproceedings{hendrycks2021measuring,\n  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},\n  title     = {{Measuring Massive Multitask Language Understanding}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2009.03300}\n}\n\n% ============================================================\n% Parameter-Efficient Fine-Tuning (additional)\n% ============================================================\n\n@inproceedings{dettmers2023qlora,\n  author    = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},\n  title     = {{QLoRA: Efficient Finetuning of Quantized LLMs}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2305.14314}\n}\n\n% ============================================================\n% Dataset\n% ============================================================\n\n@inproceedings{ding2023ultrachat,\n  author    = {Ding, Ning and Chen, Yulin and Xu, Bokai and Qin, Yujia and Zheng, Zhi and Hu, Shengding and Liu, Zhiyuan and Sun, Maosong and Zhou, Bowen},\n  title     = {{Enhancing Chat Language Models by Scaling High-quality Instructional Conversations}},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2023},\n  url     = {https://arxiv.org/abs/2305.14233}\n}\n",
      "numLines": 561,
      "startLine": 1,
      "totalLines": 561
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01Wv8MF5pnXGFWRzC5h66fN8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "c9ec3cd9-18d2-48d2-bb3a-e001a8b0ed97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATcJFHNuddnac7QTuVPUzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
      },
      "output_tokens": 21,
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

_source line 23 · 2026-05-25T22:46:30.476Z_

<details><summary>↩ Tool result · `toolu_01Wv8MF5pnXGFWRzC5h66fN8`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \citep{he2019exposure}; GAR optimizes a \emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\leq}$1.3$\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\,=\,0.743; Appendix~\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.
4	
5	\looseness=-1 Our diagnostic exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\S\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\times$ NTP dominance; \citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\,=\,0.200; Appendix~\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\beta$-steering is likewise a \emph{diagnostic}, distinct from inference-time remedies such as split-softmax \citep{li2024measuring} and Rhea \citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\beta$\,=\,5 the two converge (SS\,=\,0.717 vs.\ TG\,=\,0.727).
6	
7	\looseness=-1 Despite the weak GAR--compliance correlation ($r^2$\,=\,0.04), GAR retains independent diagnostic value: it directly quantifies how exposure bias reshapes attention allocation toward goal tokens, a mechanism invisible to surface-level compliance metrics. The downstream effect is category-dependent---content-constrained instructions benefit substantially (+23.8\,pp under $\beta$\,=\,3 steering) while format, count, and positional constraints show no change, suggesting that the attention shift GAR captures is necessary only for tasks requiring sustained reference to earlier context.
8	
9	\looseness=-1 We note that SS's benefit may partly reflect a curriculum learning effect---the linear schedule progressively increases difficulty by exposing more model-generated tokens---rather than a pure exposure bias correction. However, the core SS mechanism (substituting model generations for ground-truth prefixes) directly instantiates the definition of exposure bias mitigation, and the resulting gap compression is consistent across seeds and architectures.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "cc199336-da2c-4b28-a050-7df9beb254fc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \\citep{he2019exposure}; GAR optimizes a \\emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\\leq}$1.3$\\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\\,=\\,0.743; Appendix~\\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.\n\n\\looseness=-1 Our diagnostic exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\\S\\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\\times$ NTP dominance; \\citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\\,=\\,0.200; Appendix~\\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\\beta$-steering is likewise a \\emph{diagnostic}, distinct from inference-time remedies such as split-softmax \\citep{li2024measuring} and Rhea \\citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Despite the weak GAR--compliance correlation ($r^2$\\,=\\,0.04), GAR retains independent diagnostic value: it directly quantifies how exposure bias reshapes attention allocation toward goal tokens, a mechanism invisible to surface-level compliance metrics. The downstream effect is category-dependent---content-constrained instructions benefit substantially (+23.8\\,pp under $\\beta$\\,=\\,3 steering) while format, count, and positional constraints show no change, suggesting that the attention shift GAR captures is necessary only for tasks requiring sustained reference to earlier context.\n\n\\looseness=-1 We note that SS's benefit may partly reflect a curriculum learning effect---the linear schedule progressively increases difficulty by exposing more model-generated tokens---rather than a pure exposure bias correction. However, the core SS mechanism (substituting model generations for ground-truth prefixes) directly instantiates the definition of exposure bias mitigation, and the resulting gap compression is consistent across seeds and architectures.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01PLvNP1sXTrvGZXsCe5anmB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "27da41be-f836-4fba-866e-161337347f2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATcJFHNuddnac7QTuVPUzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 25866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
      },
      "output_tokens": 21,
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

_source line 25 · 2026-05-25T22:46:31.076Z_

<details><summary>↩ Tool result · `toolu_01PLvNP1sXTrvGZXsCe5anmB`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	The failure of ThreadGate traces to a fundamental incompatibility between teacher-forcing and auxiliary attention losses, not to the gating architecture itself. Under teacher-forcing, $\mathcal{L}_\text{GAR}$ optimizes attention patterns conditioned on ground-truth prefixes that never appear at inference time. The gate parameters, subject to NTP gradient pressure that grows from 7.5$\times$ to 14.7$\times$ the GAR gradient magnitude (\S\ref{subsec:gradient-conflict}), converge toward 1.0 and become passive. The resulting 2--7\% residual attenuation cannot compensate for the distributional mismatch between teacher-forced and autoregressive contexts, as the 30$\times$ GAR gap confirms (\S\ref{subsec:dist-shift}). Stronger gating (lower initial values, higher $\lambda_\text{GAR}$) would degrade NTP performance, while weaker gating is already ineffective. This dilemma is structural: any lightweight intervention trained jointly with NTP under teacher-forcing faces the same pressure toward passivity.
4	
5	Four directions follow from the experimental evidence. First, \textbf{inference-time attention intervention} sidesteps the training generalization problem entirely by rescaling or pruning attention heads at decoding time, operating on the actual autoregressive distribution rather than a teacher-forced proxy. Second, a \textbf{decoupled goal-processing pathway}, analogous to adapter modules but dedicated to goal tokens, could maintain goal information through a channel that NTP gradients do not dominate. Third, \textbf{GAR-aware decoding} would incorporate goal attention into the sampling or reranking stage rather than the training loss, avoiding exposure bias by construction. Fourth, \textbf{exposure bias mitigation for auxiliary losses} remains a viable direction: scheduled sampling \citep{bengio2015scheduled} or Professor Forcing \citep{lamb2016professor} applied specifically to $\mathcal{L}_\text{GAR}$ could reduce the distributional mismatch that destroys GAR transfer. Our v8 scheduled sampling experiment was invalidated by an implementation error; the approach itself warrants further study.
6	
7	Our findings converge with \citet{dongre2026attention} from an independent angle. Dongre et al.\ showed that goal information persists in the residual stream but attention fails to route it to the output. If one were to attempt goal re-injection (directly inserting goal embeddings into the residual stream at late turns), the injected signal would likely face the same distributional mismatch we document: patterns learned under teacher-forced prefixes may not transfer to autoregressive contexts. Should both independent intervention routes (attention gating and goal re-injection) prove insufficient, this would suggest that lightweight modifications to the forward pass face a fundamental obstacle under NTP training pressure.
8	
9	We scope our claims to lightweight residual gating combined with GAR auxiliary losses. More heavyweight interventions, such as full attention head retraining, separate goal encoders, or reinforcement learning from attention feedback, fall outside this investigation. The PCGrad diagnostic exclusion (\S\ref{subsec:pcgrad}) rules out gradient direction conflict but does not address magnitude imbalance \citep{chen2018gradnorm} or Nash equilibrium violations \citep{navon2022nash}, which remain untested. All experiments use a single model family (Qwen-2.5-7B-Instruct) on one dataset (UltraChat); the cross-model validation on Llama-3.1-8B-Instruct (\S\ref{sec:cross-model}) will determine whether these patterns generalize.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "bb7cfee0-d2c0-45db-a2c8-469d7bad4a7b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\nThe failure of ThreadGate traces to a fundamental incompatibility between teacher-forcing and auxiliary attention losses, not to the gating architecture itself. Under teacher-forcing, $\\mathcal{L}_\\text{GAR}$ optimizes attention patterns conditioned on ground-truth prefixes that never appear at inference time. The gate parameters, subject to NTP gradient pressure that grows from 7.5$\\times$ to 14.7$\\times$ the GAR gradient magnitude (\\S\\ref{subsec:gradient-conflict}), converge toward 1.0 and become passive. The resulting 2--7\\% residual attenuation cannot compensate for the distributional mismatch between teacher-forced and autoregressive contexts, as the 30$\\times$ GAR gap confirms (\\S\\ref{subsec:dist-shift}). Stronger gating (lower initial values, higher $\\lambda_\\text{GAR}$) would degrade NTP performance, while weaker gating is already ineffective. This dilemma is structural: any lightweight intervention trained jointly with NTP under teacher-forcing faces the same pressure toward passivity.\n\nFour directions follow from the experimental evidence. First, \\textbf{inference-time attention intervention} sidesteps the training generalization problem entirely by rescaling or pruning attention heads at decoding time, operating on the actual autoregressive distribution rather than a teacher-forced proxy. Second, a \\textbf{decoupled goal-processing pathway}, analogous to adapter modules but dedicated to goal tokens, could maintain goal information through a channel that NTP gradients do not dominate. Third, \\textbf{GAR-aware decoding} would incorporate goal attention into the sampling or reranking stage rather than the training loss, avoiding exposure bias by construction. Fourth, \\textbf{exposure bias mitigation for auxiliary losses} remains a viable direction: scheduled sampling \\citep{bengio2015scheduled} or Professor Forcing \\citep{lamb2016professor} applied specifically to $\\mathcal{L}_\\text{GAR}$ could reduce the distributional mismatch that destroys GAR transfer. Our v8 scheduled sampling experiment was invalidated by an implementation error; the approach itself warrants further study.\n\nOur findings converge with \\citet{dongre2026attention} from an independent angle. Dongre et al.\\ showed that goal information persists in the residual stream but attention fails to route it to the output. If one were to attempt goal re-injection (directly inserting goal embeddings into the residual stream at late turns), the injected signal would likely face the same distributional mismatch we document: patterns learned under teacher-forced prefixes may not transfer to autoregressive contexts. Should both independent intervention routes (attention gating and goal re-injection) prove insufficient, this would suggest that lightweight modifications to the forward pass face a fundamental obstacle under NTP training pressure.\n\nWe scope our claims to lightweight residual gating combined with GAR auxiliary losses. More heavyweight interventions, such as full attention head retraining, separate goal encoders, or reinforcement learning from attention feedback, fall outside this investigation. The PCGrad diagnostic exclusion (\\S\\ref{subsec:pcgrad}) rules out gradient direction conflict but does not address magnitude imbalance \\citep{chen2018gradnorm} or Nash equilibrium violations \\citep{navon2022nash}, which remain untested. All experiments use a single model family (Qwen-2.5-7B-Instruct) on one dataset (UltraChat); the cross-model validation on Llama-3.1-8B-Instruct (\\S\\ref{sec:cross-model}) will determine whether these patterns generalize.",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T22:46:40.293Z_

<details><summary>↩ Tool result · `toolu_01VFracwFUQXN7PTepCPEvo3`</summary>

```text
Web search results for query: "Dou et al. 2024 "Attention Forcing" LLM autoregressive generation"

Links: [{"title":"LLMs as High-Dimensional Nonlinear Autoregressive Models with Attention: Training, Alignment and Inference","url":"https://arxiv.org/pdf/2602.00426"},{"title":"Self-Selected Attention Span for Accelerating Large Language Model   Inference","url":"https://arxiv.org/pdf/2404.09336"},{"title":"Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression","url":"https://arxiv.org/pdf/2512.05081"},{"title":"Diffusion LLMs Can Do Faster-Than-AR Inference via Discrete Diffusion Forcing","url":"https://arxiv.org/html/2508.09192v1"},{"title":"[2406.07368] When Linear Attention Meets Autoregressive Decoding: Towards More Effective and Efficient Linearized Large Language Models","url":"https://arxiv.org/abs/2406.07368"},{"title":"GitHub - GATECH-EIC/Linearized-LLM: [ICML 2024] When Linear Attention Meets Autoregressive Decoding: Towards More Effective and Efficient Linearized Large Language Models","url":"https://github.com/GATECH-EIC/Linearized-LLM"},{"title":"Attention Illuminates LLM Reasoning: The Preplan-and-Anchor Rhythm Enables Fine-Grained Policy Optimization","url":"https://arxiv.org/pdf/2510.13554"},{"title":"Your LLM Knows the Future: Uncovering Its Multi-Token Prediction Potential","url":"https://arxiv.org/pdf/2507.11851"},{"title":"Continuous Autoregressive Language Models","url":"https://arxiv.org/html/2510.27688v1"}]

The search results don't appear to contain the specific paper by Dou et al. 2024 on "Attention Forcing" for LLM autoregressive generation. The results returned discuss related topics like linear attention, diffusion forcing, and speculative decoding, but not the specific paper you're looking for.

Let me try a more targeted search:

Links: [{"title":"Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/html/2507.19595v3"},{"title":"Attention Metrics Ecosystem 2024","url":"https://www.emarketer.com/content/attention-metrics-ecosystem-2024"},{"title":"We know what attention is!","url":"https://psycnet.apa.org/record/2024-38665-001"},{"title":"Attention (machine learning) - Wikipedia","url":"https://en.wikipedia.org/wiki/Attention_(machine_learning)"},{"title":"Common and distinct neural mechanisms of attention.","url":"https://psycnet.apa.org/record/2024-58715-001"},{"title":"Technology is the culprit for shortened attention spans – Massachusetts Daily Collegian","url":"https://dailycollegian.com/2024/02/technology-is-the-culprit-for-shortened-attention-spans/"},{"title":"ATTENTION 2024 - The ARF","url":"https://thearf.org/arf-events/attention-2024/"},{"title":"The End of Transformers? On Challenging Attention and the Rise of Sub-Quadratic Architectures","url":"https://arxiv.org/html/2510.05364v1"},{"title":"[2403.01643] Cost-Effective Attention Mechanisms for Low Resource Settings: Necessity & Sufficiency of Linear Transformations","url":"https://arxiv.org/abs/2403.01643"},{"title":"Attention Is All You Need Ashish Vaswani∗ Google Brain avaswani@google.com","url":"https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf"}]

The results still don't contain the specific paper by Dou et al. 2024 on "Attention Forcing." Let me try another search with different terms:

Links: [{"title":"Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales","url":"https://arxiv.org/pdf/2211.03237"},{"title":"[2211.03237] Parallel Attention Forcing for Machine Translation","url":"https://arxiv.org/abs/2211.03237"},{"title":"Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression","url":"https://arxiv.org/pdf/2512.05081"},{"title":"Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention","url":"https://arxiv.org/pdf/2602.04789"},{"title":"Attention Forcing for Sequence-to-sequence Model Training","url":"https://arxiv.org/pdf/1909.12289"}]

Based on my search results, I found papers by Qingyun Dou on "Attention Forcing," but they appear to be from earlier years (2019 and 2022) rather than 2024. The 2019 paper is titled "Attention Forcing for Sequence-to-sequence Model Training" and the 2022 paper is "Parallel Attention Forcing for Machine Translation."

According to Dou et al.'s work on attention forcing, auto-regressive sequence-to-sequence models with attention have achieved state-of-the-art performance in many tasks such as machine translation and speech synthesis. The standard approach, teacher forcing, guides a model with reference output history during training, but the problem is that the model is unlikely to recover from its mistakes during inference, where the reference output is replaced by generated output.

Attention forcing has been introduced to address the mismatch between training and inference, guiding the model with the generated back-history and reference attention.

If there is a 2024 paper by Dou et al. specifically on "Attention Forcing" for LLM autoregressive generation, it does not appear in the search results. You may want to check ArXiv directly or provide additional details about the paper's specific focus or venue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "92c1046c-647e-49b9-8868-f1e3c737a15c",
  "tool_use_result": {
    "query": "Dou et al. 2024 \"Attention Forcing\" LLM autoregressive generation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fd4aYpXGcKeMvun7VZL1aR",
        "content": [
          {
            "title": "LLMs as High-Dimensional Nonlinear Autoregressive Models with Attention: Training, Alignment and Inference",
            "url": "https://arxiv.org/pdf/2602.00426"
          },
          {
            "title": "Self-Selected Attention Span for Accelerating Large Language Model   Inference",
            "url": "https://arxiv.org/pdf/2404.09336"
          },
          {
            "title": "Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression",
            "url": "https://arxiv.org/pdf/2512.05081"
          },
          {
            "title": "Diffusion LLMs Can Do Faster-Than-AR Inference via Discrete Diffusion Forcing",
            "url": "https://arxiv.org/html/2508.09192v1"
          },
          {
            "title": "[2406.07368] When Linear Attention Meets Autoregressive Decoding: Towards More Effective and Efficient Linearized Large Language Models",
            "url": "https://arxiv.org/abs/2406.07368"
          },
          {
            "title": "GitHub - GATECH-EIC/Linearized-LLM: [ICML 2024] When Linear Attention Meets Autoregressive Decoding: Towards More Effective and Efficient Linearized Large Language Models",
            "url": "https://github.com/GATECH-EIC/Linearized-LLM"
          },
          {
            "title": "Attention Illuminates LLM Reasoning: The Preplan-and-Anchor Rhythm Enables Fine-Grained Policy Optimization",
            "url": "https://arxiv.org/pdf/2510.13554"
          },
          {
            "title": "Your LLM Knows the Future: Uncovering Its Multi-Token Prediction Potential",
            "url": "https://arxiv.org/pdf/2507.11851"
          },
          {
            "title": "Continuous Autoregressive Language Models",
            "url": "https://arxiv.org/html/2510.27688v1"
          }
        ]
      },
      "The search results don't appear to contain the specific paper by Dou et al. 2024 on \"Attention Forcing\" for LLM autoregressive generation. The results returned discuss related topics like linear attention, diffusion forcing, and speculative decoding, but not the specific paper you're looking for.\n\nLet me try a more targeted search:",
      {
        "tool_use_id": "srvtoolu_01Kccc91E7qHBqH4KP7PpaB5",
        "content": [
          {
            "title": "Efficient Attention Mechanisms for Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2507.19595v3"
          },
          {
            "title": "Attention Metrics Ecosystem 2024",
            "url": "https://www.emarketer.com/content/attention-metrics-ecosystem-2024"
          },
          {
            "title": "We know what attention is!",
            "url": "https://psycnet.apa.org/record/2024-38665-001"
          },
          {
            "title": "Attention (machine learning) - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Attention_(machine_learning)"
          },
          {
            "title": "Common and distinct neural mechanisms of attention.",
            "url": "https://psycnet.apa.org/record/2024-58715-001"
          },
          {
            "title": "Technology is the culprit for shortened attention spans – Massachusetts Daily Collegian",
            "url": "https://dailycollegian.com/2024/02/technology-is-the-culprit-for-shortened-attention-spans/"
          },
          {
            "title": "ATTENTION 2024 - The ARF",
            "url": "https://thearf.org/arf-events/attention-2024/"
          },
          {
            "title": "The End of Transformers? On Challenging Attention and the Rise of Sub-Quadratic Architectures",
            "url": "https://arxiv.org/html/2510.05364v1"
          },
          {
            "title": "[2403.01643] Cost-Effective Attention Mechanisms for Low Resource Settings: Necessity & Sufficiency of Linear Transformations",
            "url": "https://arxiv.org/abs/2403.01643"
          },
          {
            "title": "Attention Is All You Need Ashish Vaswani∗ Google Brain avaswani@google.com",
            "url": "https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf"
          }
        ]
      },
      "The results still don't contain the specific paper by Dou et al. 2024 on \"Attention Forcing.\" Let me try another search with different terms:",
      {
        "tool_use_id": "srvtoolu_01QKEib25tShbXRXkickh6bc",
        "content": [
          {
            "title": "Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales",
            "url": "https://arxiv.org/pdf/2211.03237"
          },
          {
            "title": "[2211.03237] Parallel Attention Forcing for Machine Translation",
            "url": "https://arxiv.org/abs/2211.03237"
          },
          {
            "title": "Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression",
            "url": "https://arxiv.org/pdf/2512.05081"
          },
          {
            "title": "Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention",
            "url": "https://arxiv.org/pdf/2602.04789"
          },
          {
            "title": "Attention Forcing for Sequence-to-sequence Model Training",
            "url": "https://arxiv.org/pdf/1909.12289"
          }
        ]
      },
      "Based on my search results, I found papers by Qingyun Dou on \"Attention Forcing,\" but they appear to be from earlier years (2019 and 2022) rather than 2024. The 2019 paper is titled \"Attention Forcing for Sequence-to-sequence Model Training\" and the 2022 paper is \"Parallel Attention Forcing for Machine Translation.\"\n\nAccording to Dou et al.'s work on attention forcing, auto-regressive sequence-to-sequence models with attention have achieved state-of-the-art performance in many tasks such as machine translation and speech synthesis. The standard approach, teacher forcing, guides a model with reference output history during training, but the problem is that the model is unlikely to recover from its mistakes during inference, where the reference output is replaced by generated output.\n\nAttention forcing has been introduced to address the mismatch between training and inference, guiding the model with the generated back-history and reference attention.\n\nIf there is a 2024 paper by Dou et al. specifically on \"Attention Forcing\" for LLM autoregressive generation, it does not appear in the search results. You may want to check ArXiv directly or provide additional details about the paper's specific focus or venue."
    ],
    "durationSeconds": 10.842643272000002
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze what I found:

1. **Paper search**: The web search found the 2019 paper "Attention Forcing for Sequence-to-sequence Model Training" by Dou et al. (arXiv:1909.12289) and the 2022 "Parallel Attention Forcing for Machine Translation" (arXiv:2211.03237). Both are already in the bib file. There doesn't seem to be a 2024 paper by Dou et al. on Attention Forcing.

Wait, the user is asking about "Dou et al. 2024". 

2. **Bib file**: Already has `dou2019attention` and `dou2022parallel` entries.

3. **Discussion files**: 
   - `paper/sections/discussion.tex` - shorter, more polished version
   - `docs/paper/discussion.tex` - longer version with more content

The task says to add Dou et al. 2024 citation, but I can't find a 2024 paper. Let me search more specifically to see if there's a newer version or a published venue version I'm missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "c17f8204-fdcc-49cb-80fe-d03742562670",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPxVHtMxzT7CDDpx5q8U5F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10955,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 26468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1875
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

_source line 28_

The bib file already has `dou2019attention` and `dou2022parallel`. Let me search more specifically for a 2024 version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "128ddfc0-3a20-4d71-99f6-09410dd271fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPxVHtMxzT7CDDpx5q8U5F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10955,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 26468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1875
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

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VqrEyn4D5MhEchDCRLPttV`</summary>

```json
{
  "query": "Dou Qingyun \"attention forcing\" 2024 published venue ICLR NeurIPS ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "30007e52-47af-4069-a75a-4cd924cd01a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPxVHtMxzT7CDDpx5q8U5F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10955,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 26468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1875
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

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_0147LLmUv8QMzxmrDCqCXHBD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "846597a0-669d-4d52-b470-b6fd87021fca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPxVHtMxzT7CDDpx5q8U5F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10955,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 26468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1875
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

_source line 31 · 2026-05-25T22:46:54.185Z_

<details><summary>↩ Tool result · `toolu_0147LLmUv8QMzxmrDCqCXHBD`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \citep{he2019exposure}; GAR optimizes a \emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\leq}$1.3$\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\,=\,0.743; Appendix~\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.
4	
5	\looseness=-1 Our diagnostic exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\S\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\times$ NTP dominance; \citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\,=\,0.200; Appendix~\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\beta$-steering is likewise a \emph{diagnostic}, distinct from inference-time remedies such as split-softmax \citep{li2024measuring} and Rhea \citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\beta$\,=\,5 the two converge (SS\,=\,0.717 vs.\ TG\,=\,0.727).
6	
7	\looseness=-1 Despite the weak GAR--compliance correlation ($r^2$\,=\,0.04), GAR retains independent diagnostic value: it directly quantifies how exposure bias reshapes attention allocation toward goal tokens, a mechanism invisible to surface-level compliance metrics. The downstream effect is category-dependent---content-constrained instructions benefit substantially (+23.8\,pp under $\beta$\,=\,3 steering) while format, count, and positional constraints show no change, suggesting that the attention shift GAR captures is necessary only for tasks requiring sustained reference to earlier context.
8	
9	\looseness=-1 We note that SS's benefit may partly reflect a curriculum learning effect---the linear schedule progressively increases difficulty by exposing more model-generated tokens---rather than a pure exposure bias correction. However, the core SS mechanism (substituting model generations for ground-truth prefixes) directly instantiates the definition of exposure bias mitigation, and the resulting gap compression is consistent across seeds and architectures.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "821ea737-0a1e-4b2f-8c19-72a19007e76e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \\citep{he2019exposure}; GAR optimizes a \\emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\\leq}$1.3$\\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\\,=\\,0.743; Appendix~\\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.\n\n\\looseness=-1 Our diagnostic exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\\S\\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\\times$ NTP dominance; \\citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\\,=\\,0.200; Appendix~\\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\\beta$-steering is likewise a \\emph{diagnostic}, distinct from inference-time remedies such as split-softmax \\citep{li2024measuring} and Rhea \\citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Despite the weak GAR--compliance correlation ($r^2$\\,=\\,0.04), GAR retains independent diagnostic value: it directly quantifies how exposure bias reshapes attention allocation toward goal tokens, a mechanism invisible to surface-level compliance metrics. The downstream effect is category-dependent---content-constrained instructions benefit substantially (+23.8\\,pp under $\\beta$\\,=\\,3 steering) while format, count, and positional constraints show no change, suggesting that the attention shift GAR captures is necessary only for tasks requiring sustained reference to earlier context.\n\n\\looseness=-1 We note that SS's benefit may partly reflect a curriculum learning effect---the linear schedule progressively increases difficulty by exposing more model-generated tokens---rather than a pure exposure bias correction. However, the core SS mechanism (substituting model generations for ground-truth prefixes) directly instantiates the definition of exposure bias mitigation, and the resulting gap compression is consistent across seeds and architectures.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T22:46:58.385Z_

<details><summary>↩ Tool result · `toolu_01VqrEyn4D5MhEchDCRLPttV`</summary>

```text
Web search results for query: "Dou Qingyun "attention forcing" 2024 published venue ICLR NeurIPS ACL"

Links: [{"title":"Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales","url":"https://arxiv.org/pdf/2211.03237"},{"title":"Qingyun DOU | University of Cambridge, Cambridge | Cam | Department of Engineering | Research profile","url":"https://www.researchgate.net/profile/Qingyun-Dou"},{"title":"Attention Forcing for Sequence-to-sequence Model Training | OpenReview","url":"https://openreview.net/forum?id=rJe5_CNtPB"},{"title":"Authors","url":"https://paper-republic.org/authors/"},{"title":"From Love to Marriage - WebNovel","url":"https://www.webnovel.com/ask/q335290321064983"},{"title":"Qingyun Wu","url":"https://twitter.com/qingyun_wu/status/1868004083862262236"},{"title":"GOSIM CHINA 2024-Qingyun Wu：AutoGen:Enabling Next ...","url":"https://www.youtube.com/watch?v=4xxp9h9CWvk"},{"title":"Regulating the solvation environment of hybrid electrolytes towards high-temperature zinc-ion storage","url":"https://www.oaepublish.com/articles/energymater.2024.183"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/"}]

Based on the search results, I found information about Dou Qingyun's work on "attention forcing." The work introduces attention forcing, which guides the model with generated output history and reference attention.

However, the search results show that the published attention forcing papers were from earlier years:
- A conference paper on "Attention Forcing for Speech Synthesis" from October 2020
- A preprint on "Attention Forcing for Machine Translation" from April 2021
- A paper on "Parallel Attention Forcing for Machine Translation"

The search results do not show a 2024 publication by Dou Qingyun on attention forcing at ICLR, NeurIPS, or ACL. The attention forcing work appears to have been published in earlier years (2019-2021), primarily in conference proceedings and as preprints. If there is a 2024 publication with this specific topic and author, it may not be prominently indexed in the search results, or it might be a very recent publication that hasn't been widely cataloged yet.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "7276994c-5856-4243-af55-2050c3c1ef88",
  "tool_use_result": {
    "query": "Dou Qingyun \"attention forcing\" 2024 published venue ICLR NeurIPS ACL",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X8ZCG2zrFt87KAphzZXwBz",
        "content": [
          {
            "title": "Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales",
            "url": "https://arxiv.org/pdf/2211.03237"
          },
          {
            "title": "Qingyun DOU | University of Cambridge, Cambridge | Cam | Department of Engineering | Research profile",
            "url": "https://www.researchgate.net/profile/Qingyun-Dou"
          },
          {
            "title": "Attention Forcing for Sequence-to-sequence Model Training | OpenReview",
            "url": "https://openreview.net/forum?id=rJe5_CNtPB"
          },
          {
            "title": "Authors",
            "url": "https://paper-republic.org/authors/"
          },
          {
            "title": "From Love to Marriage - WebNovel",
            "url": "https://www.webnovel.com/ask/q335290321064983"
          },
          {
            "title": "Qingyun Wu",
            "url": "https://twitter.com/qingyun_wu/status/1868004083862262236"
          },
          {
            "title": "GOSIM CHINA 2024-Qingyun Wu：AutoGen:Enabling Next ...",
            "url": "https://www.youtube.com/watch?v=4xxp9h9CWvk"
          },
          {
            "title": "Regulating the solvation environment of hybrid electrolytes towards high-temperature zinc-ion storage",
            "url": "https://www.oaepublish.com/articles/energymater.2024.183"
          },
          {
            "title": "Accepted Findings Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/find_papers/"
          },
          {
            "title": "Transactions on Machine Learning Research",
            "url": "https://jmlr.org/tmlr/papers/"
          }
        ]
      },
      "Based on the search results, I found information about Dou Qingyun's work on \"attention forcing.\" The work introduces attention forcing, which guides the model with generated output history and reference attention.\n\nHowever, the search results show that the published attention forcing papers were from earlier years:\n- A conference paper on \"Attention Forcing for Speech Synthesis\" from October 2020\n- A preprint on \"Attention Forcing for Machine Translation\" from April 2021\n- A paper on \"Parallel Attention Forcing for Machine Translation\"\n\nThe search results do not show a 2024 publication by Dou Qingyun on attention forcing at ICLR, NeurIPS, or ACL. The attention forcing work appears to have been published in earlier years (2019-2021), primarily in conference proceedings and as preprints. If there is a 2024 publication with this specific topic and author, it may not be prominently indexed in the search results, or it might be a very recent publication that hasn't been widely cataloged yet."
    ],
    "durationSeconds": 5.904741623000001
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Let me try one more search, this time looking for Dou's attention forcing work more specifically in the context of LLMs, or a 2024 version of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "d8fa9e42-ce3e-4c03-83bc-b4c385943e65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fd9gSUzdyBMcWKMME9G13F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 710,
      "cache_creation_input_tokens": 12337,
      "cache_read_input_tokens": 28343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12337
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SC3E4i9J3ur1gk4UjYWHdT`</summary>

```json
{
  "query": "arxiv \"attention forcing\" Dou Gales 2024 autoregressive training inference mismatch"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "66339c50-bf6d-4197-a227-4dc06df681dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fd9gSUzdyBMcWKMME9G13F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 710,
      "cache_creation_input_tokens": 12337,
      "cache_read_input_tokens": 28343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12337
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

_source line 35 · 2026-05-25T22:47:10.108Z_

<details><summary>↩ Tool result · `toolu_01SC3E4i9J3ur1gk4UjYWHdT`</summary>

```text
Web search results for query: "arxiv "attention forcing" Dou Gales 2024 autoregressive training inference mismatch"

Links: [{"title":"[2211.03237] Parallel Attention Forcing for Machine Translation","url":"https://arxiv.org/abs/2211.03237"},{"title":"Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales","url":"https://arxiv.org/pdf/2211.03237"},{"title":"Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation","url":"https://arxiv.org/html/2604.21221"},{"title":"End-to-End Training for Autoregressive Video Diffusion via Self-Resampling","url":"https://arxiv.org/html/2512.15702v1"},{"title":"Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion","url":"https://arxiv.org/html/2506.08009v1"},{"title":"Attention Forcing for Sequence-to-sequence Model Training","url":"https://arxiv.org/pdf/1909.12289"},{"title":"End-to-End Training for Autoregressive Video Diffusion via Self-Resampling","url":"https://arxiv.org/pdf/2512.15702"},{"title":"Rethinking Training Dynamics in Scale-wise Autoregressive Generation","url":"https://arxiv.org/pdf/2512.06421"}]

I found relevant results about attention forcing and the train-test mismatch in autoregressive models. The top result is directly about your query:

The paper "Parallel Attention Forcing for Machine Translation" is by Qingyun Dou and Mark Gales, published in November 2022 (arXiv:2211.03237).

**Key points from the paper:**

Attention-based autoregressive models have achieved state-of-the-art performance in various sequence-to-sequence tasks, but the standard training approach teacher forcing guides a model with the reference back-history. During inference, the generated back-history must be used, and this mismatch limits the evaluation performance.

Attention forcing has been introduced to address the mismatch, guiding the model with the generated back-history and reference attention. However, while successful in tasks with continuous outputs like TTS, attention forcing faces additional challenges in tasks with discrete outputs like NMT.

The paper introduces two extensions of attention forcing to tackle these challenges, with scheduled attention forcing automatically turning attention forcing on and off, which is essential for tasks with discrete outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "3c998af2-170a-48a3-8521-c3a143252bf9",
  "tool_use_result": {
    "query": "arxiv \"attention forcing\" Dou Gales 2024 autoregressive training inference mismatch",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RF8zCDDEf25m5hVCVbCVwB",
        "content": [
          {
            "title": "[2211.03237] Parallel Attention Forcing for Machine Translation",
            "url": "https://arxiv.org/abs/2211.03237"
          },
          {
            "title": "Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales",
            "url": "https://arxiv.org/pdf/2211.03237"
          },
          {
            "title": "Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation",
            "url": "https://arxiv.org/html/2604.21221"
          },
          {
            "title": "End-to-End Training for Autoregressive Video Diffusion via Self-Resampling",
            "url": "https://arxiv.org/html/2512.15702v1"
          },
          {
            "title": "Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion",
            "url": "https://arxiv.org/html/2506.08009v1"
          },
          {
            "title": "Attention Forcing for Sequence-to-sequence Model Training",
            "url": "https://arxiv.org/pdf/1909.12289"
          },
          {
            "title": "End-to-End Training for Autoregressive Video Diffusion via Self-Resampling",
            "url": "https://arxiv.org/pdf/2512.15702"
          },
          {
            "title": "Rethinking Training Dynamics in Scale-wise Autoregressive Generation",
            "url": "https://arxiv.org/pdf/2512.06421"
          }
        ]
      },
      "I found relevant results about attention forcing and the train-test mismatch in autoregressive models. The top result is directly about your query:\n\nThe paper \"Parallel Attention Forcing for Machine Translation\" is by Qingyun Dou and Mark Gales, published in November 2022 (arXiv:2211.03237).\n\n**Key points from the paper:**\n\nAttention-based autoregressive models have achieved state-of-the-art performance in various sequence-to-sequence tasks, but the standard training approach teacher forcing guides a model with the reference back-history. During inference, the generated back-history must be used, and this mismatch limits the evaluation performance.\n\nAttention forcing has been introduced to address the mismatch, guiding the model with the generated back-history and reference attention. However, while successful in tasks with continuous outputs like TTS, attention forcing faces additional challenges in tasks with discrete outputs like NMT.\n\nThe paper introduces two extensions of attention forcing to tackle these challenges, with scheduled attention forcing automatically turning attention forcing on and off, which is essential for tasks with discrete outputs."
    ],
    "durationSeconds": 6.940487881999994
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
There doesn't appear to be a 2024 paper by Dou et al. specifically. The attention forcing work by Dou has two papers:
1. Dou et al. 2019 - "Attention Forcing for Sequence-to-sequence Model Training" (arXiv:1909.12289)
2. Dou & Gales 2022 - "Parallel Attention Forcing for Machine Translation" (arXiv:2211.03237)

Both are already in the bib file.

Let me also check the OpenReview link to see if the 2019 paper was published at a conference.


The "2024" reference might actually be from a reviewer's comment rather than a real paper, so I should look at the review documents to understand what R6-SF4 was actually citing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "795aaeb0-3e45-4998-83d5-89cd16c9cb96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mu948VyWZjsDmMcfYMVRJP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1483,
      "cache_read_input_tokens": 40680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1483
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

_source line 37_

Let me check the review issues to understand what R6-SF4 actually requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "ffd34995-3188-423b-a5e9-99f35ab5b604",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mu948VyWZjsDmMcfYMVRJP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1483,
      "cache_read_input_tokens": 40680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1483
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

<details open><summary>🔧 Tool call — Read · `toolu_01AdUpmegHovbrrxaKrDUfbJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "2c443bde-dec4-4ae8-8843-8f2ccfe3b1b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mu948VyWZjsDmMcfYMVRJP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1483,
      "cache_read_input_tokens": 40680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1483
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

_source line 39 · 2026-05-25T22:47:22.436Z_

<details><summary>↩ Tool result · `toolu_01AdUpmegHovbrrxaKrDUfbJ`</summary>

```text
1	# Review Issues Tracker — turn_residual_gating
2	# Round 1 (2026-05-19, dream_20260519T145320)
3	# Round 2 (2026-05-22, fresh re-review of revised paper)
4	# Round 3 (2026-05-22, fresh re-review)
5	# Round 4 (2026-05-25, fresh re-review)
6	# Round 5 (2026-05-25, fresh re-review)
7	# Round 6 (2026-05-25, fresh re-review — current round)
8	# Cross-response phase completed: R1↔R2 convergence reached
9	
10	# ============================================================
11	# Issues from Round 1 — status updates through Round 6
12	# ============================================================
13	
14	- id: "R1-N1"
15	  summary: "所有引用渲染为 '?'——bibliography 编译失败"
16	  category: format
17	  severity: info
18	  status: resolved
19	  first_raised_round: 1
20	  last_seen_round: 1
21	  mentions:
22	    - round: 1
23	      reviewers: [1, 2]
24	      note: "Dream paper artifact。"
25	    - round: 2
26	      reviewers: []
27	      note: "视觉审查确认无 [?] 未解析引用。已修复。"
28	  action_items:
29	    - round: 1
30	      action: "Paper Agent 确保 bibtex 编译正确"
31	      assigned_to: paper_agent
32	      status: done
33	  resolution: "Round 2 视觉审查确认已修复。"
34	  resolution_round: 2
35	
36	- id: "R1-N2"
37	  summary: "单种子支撑结论——统计功效不足 + AR 评估 N=5 过小"
38	  category: experiment
39	  severity: warning
40	  status: in_progress
41	  first_raised_round: 1
42	  last_seen_round: 6
43	  mentions:
44	    - round: 1
45	      reviewers: [1, 2]
46	      note: "Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。"
47	    - round: 2
48	      reviewers: [1, 2]
49	      note: "ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。"
50	    - round: 3
51	      reviewers: [1, 2]
52	      note: "AR 评估仅 N=5，核心 claim 缺统计检验。"
53	    - round: 4
54	      reviewers: [1, 2]
55	      note: "两位 Reviewer 独立列为 Critical Must-Fix。"
56	    - round: 5
57	      reviewers: [1, 2]
58	      note: "Director 裁定降为 Should-Fix（效应量 8-17× 远超种子方差）。Phase 1A multi-seed 训练中。"
59	    - round: 6
60	      reviewers: [1, 2]
61	      note: "R6 未作为独立 Must-Fix 提出，但 R1-C3 指出 Llama 单种子问题。维持 Should-Fix。"
62	  action_items:
63	    - round: 1
64	      action: "plan_019: seed=123 extra training"
65	      assigned_to: agent
66	      status: done
67	    - round: 4
68	      action: "AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件"
69	      assigned_to: agent
70	      status: in_progress
71	    - round: 5
72	      action: "Phase 1A multi-seed 训练进行中（5 条件 × 3 seeds）"
73	      assigned_to: agent
74	      status: in_progress
75	
76	- id: "R1-N3"
77	  summary: "评估样本量过小"
78	  category: experiment
79	  severity: info
80	  status: resolved
81	  first_raised_round: 1
82	  last_seen_round: 1
83	  mentions:
84	    - round: 1
85	      reviewers: [1]
86	      note: "Cohen's d≈0.22 在 n=50 下 power 不足。"
87	  action_items: []
88	  resolution: "N=50 评估已在论文中体现。"
89	  resolution_round: 2
90	
91	- id: "R1-N4"
92	  summary: "损失函数超参数和 v1-v6 配置定义缺失"
93	  category: method
94	  severity: info
95	  status: resolved
96	  first_raised_round: 1
97	  last_seen_round: 1
98	  mentions:
99	    - round: 1
100	      reviewers: [1, 2]
101	      note: "v1-v7 配置仅报告 v7。"
102	  action_items: []
103	  resolution: "§3.3 + Appendix B Table 2 已提供完整信息。"
104	  resolution_round: 2
105	
106	- id: "R1-W1"
107	  summary: "Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）"
108	  category: experiment
109	  severity: warning
110	  status: in_progress
111	  first_raised_round: 1
112	  last_seen_round: 6
113	  mentions:
114	    - round: 1
115	      reviewers: [1, 2]
116	      note: "边际信息量不值 6h GPU。"
117	    - round: 2
118	      reviewers: [1, 2]
119	      note: "仍仅 3/5 条件，N=20，用 median。"
120	    - round: 3
121	      reviewers: [1, 2]
122	      note: "额外问题：mean/median 未双报。"
123	    - round: 4
124	      reviewers: [1, 2]
125	      note: "R1 列 Should-Fix。R2 建议标题改为 Cross-Model Replication。"
126	    - round: 5
127	      reviewers: [1, 2]
128	      note: "仅 3/5 条件削弱 cross-model generality。Phase 1B Llama PCGrad+UG 排队。"
129	    - round: 6
130	      reviewers: [1, 2]
131	      note: "R1-C3 指出 Llama 仅 3/5 条件、N=20、单种子、median 与 Qwen mean 不可比。R2 交叉同意。"
132	  action_items:
133	    - round: 2
134	      action: "补充 Llama PCGrad+UG 训练+评估"
135	      assigned_to: agent
136	      status: in_progress
137	    - round: 4
138	      action: "写作降级：§5.5 标题→Cross-Model Replication + mean/median 双报"
139	      assigned_to: paper_agent
140	      status: in_progress
141	
142	- id: "R1-W2"
143	  summary: "无 λ_GAR 敏感性消融"
144	  category: experiment
145	  severity: warning
146	  status: in_progress
147	  first_raised_round: 1
148	  last_seen_round: 6
149	  mentions:
150	    - round: 1
151	      reviewers: [1]
152	      note: "梯度冲突取决于 λ_GAR。"
153	    - round: 6
154	      reviewers: [1]
155	      note: "R1-C1 明确要求 λ_GAR rescaling 实验——NTP 幅值压倒 GAR 7.5-14.7×，未测试 rescaling 使排除链不完整。"
156	  action_items:
157	    - round: 1
158	      action: "plan_022: λ_GAR=10 敏感性测试"
159	      assigned_to: agent
160	      status: in_progress
161	    - round: 6
162	      action: "λ_GAR rescaling 实验：7B λ=10 + 1.5B λ∈{1,8,15}，测试 magnitude parity 下 TF-AR gap 变化"
163	      assigned_to: agent
164	      status: in_progress
165	
166	- id: "R1-W3"
167	  summary: "训练数据量混淆变量"
168	  category: experiment
169	  severity: info
170	  status: resolved
171	  first_raised_round: 1
172	  last_seen_round: 1
173	  mentions:
174	    - round: 1
175	      reviewers: [1]
176	      note: "1,000 convs 偏少。"
177	  action_items: []
178	  resolution: "训练数据量增加至 8K。"
179	  resolution_round: 2
180	
181	- id: "R1-W4"
182	  summary: "全文零 figure"
183	  category: format
184	  severity: info
185	  status: resolved
186	  first_raised_round: 1
187	  last_seen_round: 1
188	  mentions:
189	    - round: 1
190	      reviewers: [1, 2]
191	      note: "Dream paper artifact."
192	  action_items: []
193	  resolution: "Figure 1-6 + Table 1-2 已就位。"
194	  resolution_round: 2
195	
196	- id: "R1-W5"
197	  summary: "Scheduled sampling 统计支撑不足"
198	  category: experiment
199	  severity: critical
200	  status: in_progress
201	  first_raised_round: 1
202	  last_seen_round: 6
203	  mentions:
204	    - round: 1
205	      reviewers: [1, 2]
206	      note: "单 seed，单 ratio，PPL 未报告。"
207	    - round: 2
208	      reviewers: [1, 2]
209	      note: "PPL 已报告，但仍单 seed。"
210	    - round: 4
211	      reviewers: [1, 2]
212	      note: "SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。"
213	    - round: 5
214	      reviewers: [1, 2]
215	      note: "SS 贡献 ~8.5× 提升。ThreadGate 贡献边际。"
216	    - round: 6
217	      reviewers: [1, 2]
218	      note: "SS Llama 残留 2.9× gap 说明 exposure bias 可能非唯一因素。Abstract 'substantially' 模糊。"
219	  action_items:
220	    - round: 4
221	      action: "3 seeds (s42/s123/s456) + mean±std"
222	      assigned_to: agent
223	      status: in_progress
224	
225	- id: "R1-W6"
226	  summary: "Reverse turn conditioning 证据间接"
227	  category: experiment
228	  severity: info
229	  status: resolved
230	  first_raised_round: 1
231	  last_seen_round: 1
232	  mentions:
233	    - round: 1
234	      reviewers: [1]
235	      note: "差异可能是噪声。"
236	  resolution: "Wilcoxon p=3.73e-8, r=0.975。"
237	  resolution_round: 2
238	
239	# ============================================================
240	# Issues from Round 2 — status updates through Round 6
241	# ============================================================
242	
243	- id: "R2-N1"
244	  summary: "Novelty/causal 声称过高——contribution 措辞需调整"
245	  category: framing
246	  severity: critical
247	  status: in_progress
248	  first_raised_round: 1
249	  last_seen_round: 6
250	  mentions:
251	    - round: 1
252	      reviewers: [1, 2]
253	      note: "'first quantitative measurement' overclaim。"
254	    - round: 2
255	      reviewers: [1, 2]
256	      note: "'systematic causal diagnostic framework' 实际是消融。"
257	    - round: 4
258	      reviewers: [2]
259	      note: "'to our knowledge, the first' 仍被质疑。"
260	    - round: 5
261	      reviewers: [1, 2]
262	      note: "因果排除链不完整（KV cache drift + NTP magnitude imbalance 未排除）。强共识 Must-Fix。"
263	    - round: 6
264	      reviewers: [1, 2]
265	      note: "[复发 ×6 轮] 'causal exclusion' 措辞强共识必须修改。R1 从方法论（magnitude未排除），R2 从术语精确性（非interventionist causal inference）。建议→'diagnostic exclusion chain'/'systematic ablation-based exclusion'。"
266	  action_items:
267	    - round: 1
268	      action: "'first quantitative measurement' 降级"
269	      assigned_to: director
270	      status: done
271	    - round: 4
272	      action: "GAR 重新定位为 diagnostic probe"
273	      assigned_to: paper_agent
274	      status: in_progress
275	    - round: 5
276	      action: "Phase 2 switching 实验 + exposure bias 降级为 'a proximal cause'"
277	      assigned_to: agent
278	      status: in_progress
279	    - round: 6
280	      action: "[复发 ×6 轮] 全文 'causal exclusion'→'diagnostic exclusion chain' 术语替换已完成。等 λ_GAR + switching 实验结果后由 Paper Agent 重构排除链叙事。"
281	      assigned_to: paper_agent
282	      status: done
283	
284	- id: "R2-N2"
285	  summary: "标题过度声称"
286	  category: framing
287	  severity: warning
288	  status: in_progress
289	  first_raised_round: 1
290	  last_seen_round: 6
291	  mentions:
292	    - round: 1
293	      reviewers: [1, 2]
294	      note: "'Cannot Fix' → 'Fails to Fix'。"
295	    - round: 2
296	      reviewers: [1, 2]
297	      note: "'Lightweight Gating' 过宽。"
298	    - round: 5
299	      reviewers: [1, 2]
300	      note: "'Destroys' 与 r²=0.04 不匹配。需降调。"
301	    - round: 6
302	      reviewers: [1, 2]
303	      note: "维持 Should-Fix。标题需降调以匹配 evidence 强度。"
304	  action_items:
305	    - round: 5
306	      action: "标题 'Destroys' → 'Collapses'（描述 attention 行为而非下游灾难）"
307	      assigned_to: paper_agent
308	      status: in_progress
309	
310	- id: "R2-N3"
311	  summary: "Dongre et al. GAR 全称引用错误"
312	  category: format
313	  severity: critical
314	  status: in_progress
315	  first_raised_round: 1
316	  last_seen_round: 3
317	  mentions:
318	    - round: 1
319	      reviewers: [1, 2]
320	      note: "论文动机链依赖此引用。"
321	    - round: 3
322	      reviewers: [1, 2]
323	      note: "arXiv 原文验证确认。Critical Must-Fix。"
324	    - round: 6
325	      reviewers: []
326	      note: "本轮未提及。待确认修复状态。"
327	  action_items:
328	    - round: 3
329	      action: "全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'"
330	      assigned_to: agent
331	      status: in_progress
332	
333	- id: "R2-N4"
334	  summary: "Related Work 缺失 gradient conflict 文献 + PCGrad baseline"
335	  category: framing
336	  severity: info
337	  status: resolved
338	  first_raised_round: 1
339	  last_seen_round: 1
340	  mentions:
341	    - round: 1
342	      reviewers: [1, 2]
343	      note: "如果 PCGrad 能解决梯度竞争，论文核心结论悬空。"
344	  action_items: []
345	  resolution: "PCGrad 已纳入五路对比 + Related Work 已覆盖。"
346	  resolution_round: 2
347	
348	- id: "R2-C3"
349	  summary: "Exposure bias 归因——替代假说讨论不足"
350	  category: method
351	  severity: critical
352	  status: in_progress
353	  first_raised_round: 2
354	  last_seen_round: 6
355	  mentions:
356	    - round: 2
357	      reviewers: [1, 2]
358	      note: "β-steering 循环论证；KV cache 差异未排除。"
359	    - round: 3
360	      reviewers: [1, 2]
361	      note: "R1 列 Critical，R2 降 Should-Fix。"
362	    - round: 4
363	      reviewers: [1, 2]
364	      note: "PCGrad 失败可能反映投影副作用。"
365	    - round: 5
366	      reviewers: [1, 2]
367	      note: "[复发 ×4 轮] 强共识 Must-Fix。KV cache drift + Appendix L 非独立验证。"
368	    - round: 6
369	      reviewers: [1, 2]
370	      note: "[复发 ×5 轮] R1 交叉回应明确：λ_GAR rescaling 缺失使 exposure bias 归因无法与梯度幅值淹没假说区分。SS Llama 2.9× 残留进一步说明可能有其他因素。"
371	  action_items:
372	    - round: 2
373	      action: "'the proximal cause' → 'a proximal cause consistent with evidence'"
374	      assigned_to: paper_agent
375	      status: done
376	    - round: 4
377	      action: "§6 扩展 exposure bias 讨论"
378	      assigned_to: paper_agent
379	      status: done
380	    - round: 5
381	      action: "Phase 2 switching 实验区分 exposure bias vs KV cache drift"
382	      assigned_to: agent
383	      status: in_progress
384	    - round: 6
385	      action: "λ_GAR rescaling (7B λ=10 + 1.5B λ∈{1,8,15}) + TF→AR switching eval + Discussion 段落"
386	      assigned_to: agent
387	      status: in_progress
388	
389	- id: "R2-W3"
390	  summary: "GAR 单指标——instruction retention 不显著但占页过多"
391	  category: method
392	  severity: critical
393	  status: in_progress
394	  first_raised_round: 1
395	  last_seen_round: 6
396	  mentions:
397	    - round: 1
398	      reviewers: [1, 2]
399	      note: "r=0.82 sanity check 不足。"
400	    - round: 2
401	      reviewers: [1, 2]
402	      note: "McNemar p=0.077 不显著。"
403	    - round: 4
404	      reviewers: [1, 2]
405	      note: "r=0.200 的 95% CI ≈ [0.05, 0.35] 过宽。"
406	    - round: 5
407	      reviewers: [1, 2]
408	      note: "[复发 ×5 轮] 升级为 Must-Fix。r²=0.04 仅解释 4% 下游方差。"
409	    - round: 6
410	      reviewers: [1, 2]
411	      note: "[复发 ×6 轮] R2 补充：per-category 高度分化——仅 content constraints +23.8pp 显著，format/count/position 无变化。R1 交叉强烈同意。"
412	  action_items:
413	    - round: 4
414	      action: "重新定位 GAR 为 diagnostic probe"
415	      assigned_to: paper_agent
416	      status: in_progress
417	    - round: 5
418	      action: "标题 Destroys→Collapses + 叙事重构"
419	      assigned_to: paper_agent
420	      status: in_progress
421	    - round: 6
422	      action: "§6 新段落：GAR as diagnostic probe 独立价值论证 + proxy 局限讨论（r²=0.04 + per-category 分化）"
423	      assigned_to: paper_agent
424	      status: open
425	
426	- id: "R2-W5"
427	  summary: "liu2016attention 引用可能错配"
428	  category: format
429	  severity: warning
430	  status: in_progress
431	  first_raised_round: 1
432	  last_seen_round: 1
433	  mentions:
434	    - round: 1
435	      reviewers: [2]
436	      note: "语音识别 vs 注意力引导。"
437	  action_items:
438	    - round: 2
439	      action: "Paper Agent 确认引用准确性"
440	      assigned_to: paper_agent
441	      status: in_progress
442	
443	- id: "R2-W6"
444	  summary: "Bib 格式不一致"
445	  category: format
446	  severity: info
447	  status: in_progress
448	  first_raised_round: 1
449	  last_seen_round: 6
450	  mentions:
451	    - round: 5
452	      reviewers: [2]
453	      note: "Raposo et al. 缺 ICML 2024 venue；Gromov et al. 年份问题。"
454	    - round: 6
455	      reviewers: []
456	      note: "本轮未独立提出。"
457	  action_items:
458	    - round: 4
459	      action: "统一 bib 格式"
460	      assigned_to: paper_agent
461	      status: in_progress
462	
463	- id: "R1-MISC"
464	  summary: "无代码/数据发布"
465	  category: format
466	  severity: warning
467	  status: resolved
468	  first_raised_round: 1
469	  last_seen_round: 5
470	  mentions:
471	    - round: 5
472	      reviewers: [1, 2]
473	      note: "论文 p.1 Abstract 已有 anonymous.4open.science 链接。"
474	  action_items:
475	    - round: 2
476	      action: "投稿前准备匿名 GitHub repo"
477	      assigned_to: agent
478	      status: done
479	  resolution: "论文 p.1 已有匿名代码链接。"
480	  resolution_round: 5
481	
482	- id: "R2-W1-new"
483	  summary: "Table 1 AR 列需扩容"
484	  category: writing
485	  severity: warning
486	  status: in_progress
487	  first_raised_round: 2
488	  last_seen_round: 5
489	  mentions:
490	    - round: 5
491	      reviewers: [1]
492	      note: "与 R1-N2 联动，AR 列需 N≥50 + CI。"
493	    - round: 6
494	      reviewers: []
495	      note: "本轮未独立提出。"
496	  action_items:
497	    - round: 4
498	      action: "AR 列更新为 N≥50 数据 + CI + GAR-D + PPL"
499	      assigned_to: agent
500	      status: in_progress
501	
502	- id: "R2-W4-new"
503	  summary: "写作冗余——关键数字重复 8+ 次"
504	  category: writing
505	  severity: warning
506	  status: in_progress
507	  first_raised_round: 2
508	  last_seen_round: 6
509	  mentions:
510	    - round: 5
511	      reviewers: [2]
512	      note: "仍存在。"
513	    - round: 6
514	      reviewers: [1]
515	      note: "R1 交叉回应 rebut——认为核心 effect size 在 Abstract/Intro/Results 重复是正常科学写作。"
516	  action_items:
517	    - round: 5
518	      action: "Abstract/§4.2 保留完整数字，其余改用回指"
519	      assigned_to: paper_agent
520	      status: in_progress
521	
522	- id: "R2-W6-new"
523	  summary: "Contribution (1) 泛化声称"
524	  category: framing
525	  severity: warning
526	  status: in_progress
527	  first_raised_round: 2
528	  last_seen_round: 5
529	  mentions:
530	    - round: 5
531	      reviewers: [2]
532	      note: "'to our knowledge, the first' 仍被质疑。合并至 R2-N1 追踪。"
533	  action_items:
534	    - round: 4
535	      action: "删除泛化声称，合并至 R2-N1"
536	      assigned_to: paper_agent
537	      status: in_progress
538	
539	- id: "R2-W7-new"
540	  summary: "Li et al. split-softmax 缺实验对比"
541	  category: experiment
542	  severity: warning
543	  status: in_progress
544	  first_raised_round: 2
545	  last_seen_round: 5
546	  mentions:
547	    - round: 5
548	      reviewers: [1, 2]
549	      note: "Discussion 定性讨论即可，不做实验对比。"
550	  action_items:
551	    - round: 5
552	      action: "Discussion 中加强 split-softmax/Rhea 概念对比"
553	      assigned_to: paper_agent
554	      status: in_progress
555	
556	# ============================================================
557	# Supplementary items from Round 2
558	# ============================================================
559	
560	- id: "R2-SUPP-1"
561	  summary: "Figure/Table caption overclaim + 重复句"
562	  category: writing
563	  severity: warning
564	  status: in_progress
565	  first_raised_round: 2
566	  last_seen_round: 3
567	  mentions:
568	    - round: 6
569	      reviewers: []
570	      note: "本轮未独立提出。"
571	  action_items:
572	    - round: 3
573	      action: "修正 Fig 3b/Table 1/Fig 4 caption"
574	      assigned_to: paper_agent
575	      status: in_progress
576	
577	- id: "R2-SUPP-2"
578	  summary: "Multi-seed 完成后数字更新"
579	  category: writing
580	  severity: warning
581	  status: open
582	  first_raised_round: 2
583	  last_seen_round: 2
584	  mentions:
585	    - round: 6
586	      reviewers: []
587	      note: "仍待 multi-seed 实验完成。"
588	  action_items:
589	    - round: 2
590	      action: "Multi-seed 完成后统一更新"
591	      assigned_to: paper_agent
592	      status: open
593	
594	- id: "R2-SUPP-3"
595	  summary: "SS variance 风险应急计划"
596	  category: experiment
597	  severity: info
598	  status: open
599	  first_raised_round: 2
600	  last_seen_round: 5
601	  mentions:
602	    - round: 6
603	      reviewers: []
604	      note: "SS 统计支撑仍为核心问题。"
605	  action_items:
606	    - round: 2
607	      action: "SS multi-seed 结果出来后评估 variance"
608	      assigned_to: director
609	      status: open
610	
611	# ============================================================
612	# Issues from Round 3 — status updates through Round 6
613	# ============================================================
614	
615	- id: "R3-MF2"
616	  summary: "正文超过 EMNLP 8 页限制"
617	  category: format
618	  severity: critical
619	  status: resolved
620	  first_raised_round: 3
621	  last_seen_round: 4
622	  resolution: "Round 4 确认页数合规。"
623	  resolution_round: 4
624	
625	- id: "R3-SF4"
626	  summary: "PCGrad scope 过度概括"
627	  category: method
628	  severity: warning
629	  status: in_progress
630	  first_raised_round: 3
631	  last_seen_round: 6
632	  mentions:
633	    - round: 5
634	      reviewers: [1, 2]
635	      note: "NTP magnitude imbalance 7.5-14.7× 是 PCGrad 失败的替代解释。"
636	    - round: 6
637	      reviewers: [1, 2]
638	      note: "R1 交叉回应：即便改 'causal exclusion' 措辞，λ_GAR rescaling 缺失仍是实质问题。"
639	  action_items:
640	    - round: 3
641	      action: "'gradient conflict' → 'gradient direction conflict'"
642	      assigned_to: paper_agent
643	      status: in_progress
644	    - round: 5
645	      action: "补充 1 句：PCGrad 不处理 magnitude imbalance"
646	      assigned_to: paper_agent
647	      status: in_progress
648	
649	- id: "R3-SF6"
650	  summary: "缺少 Rhea (arXiv:2512.06869) 引用"
651	  category: framing
652	  severity: warning
653	  status: in_progress
654	  first_raised_round: 3
655	  last_seen_round: 5
656	  mentions:
657	    - round: 5
658	      reviewers: [2]
659	      note: "与 split-softmax 一并作为缺失对比方案。合并至 R2-W7-new。"
660	  action_items:
661	    - round: 5
662	      action: "Discussion 概念对比中一并覆盖 Rhea"
663	      assigned_to: paper_agent
664	      status: in_progress
665	
666	- id: "R3-MINOR-1"
667	  summary: "LoRA capacity saturation 未讨论"
668	  category: method
669	  severity: warning
670	  status: in_progress
671	  first_raised_round: 3
672	  last_seen_round: 6
673	  mentions:
674	    - round: 5
675	      reviewers: [1, 2]
676	      note: "R2 同意 R1 (Q4)。"
677	    - round: 6
678	      reviewers: [1, 2]
679	      note: "R2-W3 新增：LoRA 限制模型重组 attention patterns capacity，可能 confound capacity 排除步骤。R1 交叉同意。"
680	  action_items:
681	    - round: 5
682	      action: "§7 Limitations 加 1 句 acknowledge LoRA rank 16 可能影响 gate 效用上界"
683	      assigned_to: paper_agent
684	      status: done
685	    - round: 6
686	      action: "Limitations 扩展：LoRA-only 实验限制了 capacity 排除步骤的推断力度"
687	      assigned_to: paper_agent
688	      status: done
689	
690	- id: "R3-MINOR-2"
691	  summary: "GPU 型号名称准确性"
692	  category: format
693	  severity: info
694	  status: open
695	  first_raised_round: 3
696	  last_seen_round: 3
697	  action_items:
698	    - round: 3
699	      action: "确认准确性"
700	      assigned_to: agent
701	      status: open
702	
703	- id: "R3-NEW-1"
704	  summary: "UG 描述不清——未说明仍为可学习 MLP"
705	  category: method
706	  severity: info
707	  status: in_progress
708	  first_raised_round: 3
709	  last_seen_round: 3
710	  action_items:
711	    - round: 3
712	      action: "§4.1 或 §3 加一句说明"
713	      assigned_to: paper_agent
714	      status: in_progress
715	
716	- id: "R3-NEW-2"
717	  summary: "Contribution (4) 混淆开发迭代与系统消融"
718	  category: framing
719	  severity: info
720	  status: in_progress
721	  first_raised_round: 3
722	  last_seen_round: 3
723	  action_items:
724	    - round: 3
725	      action: "拆分为 loss design iterations + systematic conditions comparison"
726	      assigned_to: paper_agent
727	      status: in_progress
728	
729	# ============================================================
730	# Issues from Round 4 — status updates through Round 6
731	# ============================================================
732	
733	- id: "R4-N1"
734	  summary: "GAR 指标与下游任务性能之间缺乏因果验证"
735	  category: method
736	  severity: critical
737	  status: in_progress
738	  first_raised_round: 4
739	  last_seen_round: 6
740	  mentions:
741	    - round: 4
742	      reviewers: [1, 2]
743	      note: "r=0.200, r²=0.04。"
744	    - round: 5
745	      reviewers: [1, 2]
746	      note: "Director 裁定 Must-Fix。与 R2-W3 合并追踪。"
747	    - round: 6
748	      reviewers: [1, 2]
749	      note: "R2 补充 per-category 分化证据。R1 交叉强烈同意。维持 Must-Fix。"
750	  action_items:
751	    - round: 5
752	      action: "标题 Destroys→Collapses + GAR 叙事重构"
753	      assigned_to: paper_agent
754	      status: in_progress
755	    - round: 6
756	      action: "§6 GAR as diagnostic probe 独立价值论证 + per-category 分化讨论"
757	      assigned_to: paper_agent
758	      status: open
759	
760	- id: "R4-N2"
761	  summary: "SS+LoRA-only 消融缺失——ThreadGate 独立贡献不清"
762	  category: experiment
763	  severity: warning
764	  status: in_progress
765	  first_raised_round: 4
766	  last_seen_round: 5
767	  mentions:
768	    - round: 5
769	      reviewers: [1, 2]
770	      note: "关键缺失消融。"
771	  action_items:
772	    - round: 5
773	      action: "SS+LoRA-only 实验"
774	      assigned_to: agent
775	      status: in_progress
776	
777	- id: "R4-W1"
778	  summary: "GAR-D 全条件接近零——干预仅在 last token 成功"
779	  category: method
780	  severity: warning
781	  status: in_progress
782	  first_raised_round: 4
783	  last_seen_round: 5
784	  action_items:
785	    - round: 5
786	      action: "§3.1 补充 GAR-ours vs GAR-D 选择理由"
787	      assigned_to: paper_agent
788	      status: in_progress
789	
790	- id: "R4-W2"
791	  summary: "Table 1 四舍五入与正文数字精度不一致"
792	  category: writing
793	  severity: info
794	  status: open
795	  first_raised_round: 4
796	  last_seen_round: 4
797	  action_items:
798	    - round: 4
799	      action: "Table 1 增加一位小数"
800	      assigned_to: paper_agent
801	      status: open
802	
803	- id: "R4-W3"
804	  summary: "r_min 数值正文未报告"
805	  category: method
806	  severity: info
807	  status: open
808	  first_raised_round: 4
809	  last_seen_round: 4
810	  action_items:
811	    - round: 4
812	      action: "在 §3 或 Appendix A 中报告 r_min 数值"
813	      assigned_to: paper_agent
814	      status: open
815	
816	- id: "R4-MR1"
817	  summary: "缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用"
818	  category: framing
819	  severity: info
820	  status: in_progress
821	  first_raised_round: 4
822	  last_seen_round: 6
823	  mentions:
824	    - round: 6
825	      reviewers: [1, 2]
826	      note: "Missing References 中明确列出。"
827	  action_items:
828	    - round: 5
829	      action: "合并至 R2-W7-new Discussion 概念对比"
830	      assigned_to: paper_agent
831	      status: in_progress
832	
833	- id: "R4-W4"
834	  summary: "Appendix C instruction retention 多重比较未校正"
835	  category: experiment
836	  severity: warning
837	  status: in_progress
838	  first_raised_round: 4
839	  last_seen_round: 6
840	  mentions:
841	    - round: 5
842	      reviewers: [1, 2]
843	      note: "18-category McNemar's test 缺 FDR/Bonferroni 校正。"
844	    - round: 6
845	      reviewers: [1, 2]
846	      note: "m3 再次提出。per-category 分化进一步削弱未校正结果可信度。"
847	  action_items:
848	    - round: 4
849	      action: "Appendix C per-category 分析补充 Holm-Bonferroni 或 FDR 校正"
850	      assigned_to: agent
851	      status: in_progress
852	
853	# ============================================================
854	# Round 5 — status updates through Round 6
855	# ============================================================
856	
857	- id: "R5-SF1"
858	  summary: "β-steering 部分循环论证——GAR 恢复 vs 下游效果未解耦"
859	  category: method
860	  severity: warning
861	  status: in_progress
862	  first_raised_round: 2
863	  last_seen_round: 6
864	  mentions:
865	    - round: 2
866	      reviewers: [1, 2]
867	      note: "β-steering 循环论证首次提出。"
868	    - round: 5
869	      reviewers: [1, 2]
870	      note: "boost attention → attention metric recovers 是同义反复。"
871	    - round: 6
872	      reviewers: [1]
873	      note: "R1-S1 维持循环论证判断。"
874	  action_items:
875	    - round: 5
876	      action: "§5.4 拆为两段：GAR 恢复标注 'by construction' + 下游效果单独报告"
877	      assigned_to: paper_agent
878	      status: in_progress
879	
880	# ============================================================
881	# Round 6 新增
882	# ============================================================
883	
884	- id: "R6-SF1"
885	  summary: "单一数据集（仅 UltraChat）限制 generalizability claim"
886	  category: experiment
887	  severity: warning
888	  status: resolved
889	  first_raised_round: 6
890	  last_seen_round: 6
891	  mentions:
892	    - round: 6
893	      reviewers: [1, 2]
894	      note: "R2 列 Must-Fix，R1 rebut 降为 Should-Fix（诊断性论文单数据集可接受，UltraChat 18 种对话类型提供 domain diversity）。Director 裁定 Should-Fix——机制性发现依赖 training dynamics 而非数据，但 Limitations 需明确讨论。"
895	  action_items:
896	    - round: 6
897	      action: "Limitations 明确讨论单数据集对 generalizability 的限制 + future work 承诺跨数据集验证"
898	      assigned_to: paper_agent
899	      status: done
900	  resolution: "Limitations 已添加 cross-dataset validation discussion。Reviewer 确认。"
901	  resolution_round: 6
902	
903	- id: "R6-SF2"
904	  summary: "SS Llama 残留 2.9× gap——Abstract 'substantially' 措辞模糊"
905	  category: writing
906	  severity: warning
907	  status: open
908	  first_raised_round: 6
909	  last_seen_round: 6
910	  mentions:
911	    - round: 6
912	      reviewers: [1, 2]
913	      note: "强共识。Qwen 1.3× vs Llama 2.9× 差异显著。Abstract 应报告具体数字。可能暗示 Llama 上有 exposure bias 以外的因素。"
914	  action_items:
915	    - round: 6
916	      action: "Abstract 改为具体数字 + §6 讨论 Llama 残留 gap 根因"
917	      assigned_to: paper_agent
918	      status: open
919	
920	- id: "R6-SF3"
921	  summary: "仅 LoRA fine-tuning，未验证 full fine-tuning"
922	  category: experiment
923	  severity: warning
924	  status: resolved
925	  first_raised_round: 6
926	  last_seen_round: 6
927	  mentions:
928	    - round: 6
929	      reviewers: [1, 2]
930	      note: "R2 提出，R1 交叉同意。LoRA capacity 限制可能 confound capacity 排除步骤。合并至 R3-MINOR-1。"
931	  action_items:
932	    - round: 6
933	      action: "Limitations 讨论 LoRA-only 限制（合并至 R3-MINOR-1 执行）"
934	      assigned_to: paper_agent
935	      status: done
936	  resolution: "Limitations 已添加 LoRA-only + capacity confound 讨论。Reviewer 确认。"
937	  resolution_round: 6
938	
939	- id: "R6-SF4"
940	  summary: "Dou et al. attention forcing 区分讨论不够深入"
941	  category: framing
942	  severity: warning
943	  status: open
944	  first_raised_round: 6
945	  last_seen_round: 6
946	  mentions:
947	    - round: 6
948	      reviewers: [1, 2]
949	      note: "R2 提出 3 点缺失讨论（AR 退化、retrospective 解释、方法论互补），R1 交叉同意。"
950	    - round: 6
951	      reviewers: []
952	      note: "Reviewer 审查确认 Related Work 已有 3 点区分，但 3 个额外点（AR 退化/回溯解释/方法互补性）未见添加。优先级较低。"
953	  action_items:
954	    - round: 6
955	      action: "Related Work/Discussion 增加 2-3 句 Dou et al. deeper connection"
956	      assigned_to: paper_agent
957	      status: open
958	
959	- id: "R6-SF5"
960	  summary: "Loss formulation 搜索（v1-v9）的过拟合风险"
961	  category: experiment
962	  severity: warning
963	  status: resolved
964	  first_raised_round: 6
965	  last_seen_round: 6
966	  mentions:
967	    - round: 6
968	      reviewers: [1]
969	      note: "9 次迭代选 loss formulation 可能对 UltraChat 数据集过拟合。"
970	  action_items:
971	    - round: 6
972	      action: "Appendix B 加 1 段 loss search overfitting caveat + TF-AR gap 在所有 variants 中均出现的反驳"
973	      assigned_to: paper_agent
974	      status: done
975	  resolution: "Appendix 已添加 Overfitting caveat 段落，论证 TF-AR gap 跨 variants 一致性。Reviewer 确认。"
976	  resolution_round: 6
977	
978	- id: "R6-SF6"
979	  summary: "SS 替代解释（curriculum effect）未排除"
980	  category: method
981	  severity: warning
982	  status: open
983	  first_raised_round: 6
984	  last_seen_round: 6
985	  mentions:
986	    - round: 6
987	      reviewers: [1]
988	      note: "SS 改变训练动态不仅仅修复 exposure bias。"
989	  action_items:
990	    - round: 6
991	      action: "§6 Discussion 加 1 段 SS curriculum effect 替代机制讨论"
992	      assigned_to: paper_agent
993	      status: open
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "ef36e29b-e620-4907-8e79-a21d9450da20",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml",
      "content": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review)\n# Round 4 (2026-05-25, fresh re-review)\n# Round 5 (2026-05-25, fresh re-review)\n# Round 6 (2026-05-25, fresh re-review — current round)\n# Cross-response phase completed: R1↔R2 convergence reached\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 6\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足 + AR 评估 N=5 过小\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 评估仅 N=5，核心 claim 缺统计检验。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立列为 Critical Must-Fix。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Director 裁定降为 Should-Fix（效应量 8-17× 远超种子方差）。Phase 1A multi-seed 训练中。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R6 未作为独立 Must-Fix 提出，但 R1-C3 指出 Llama 单种子问题。维持 Should-Fix。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 4\n      action: \"AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件\"\n      assigned_to: agent\n      status: in_progress\n    - round: 5\n      action: \"Phase 1A multi-seed 训练进行中（5 条件 × 3 seeds）\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"额外问题：mean/median 未双报。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Should-Fix。R2 建议标题改为 Cross-Model Replication。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"仅 3/5 条件削弱 cross-model generality。Phase 1B Llama PCGrad+UG 排队。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1-C3 指出 Llama 仅 3/5 条件、N=20、单种子、median 与 Qwen mean 不可比。R2 交叉同意。\"\n  action_items:\n    - round: 2\n      action: \"补充 Llama PCGrad+UG 训练+评估\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"写作降级：§5.5 标题→Cross-Model Replication + mean/median 双报\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-C1 明确要求 λ_GAR rescaling 实验——NTP 幅值压倒 GAR 7.5-14.7×，未测试 rescaling 使排除链不完整。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"λ_GAR rescaling 实验：7B λ=10 + 1.5B λ∈{1,8,15}，测试 magnitude parity 下 TF-AR gap 变化\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n  action_items: []\n  resolution: \"Figure 1-6 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"SS AR GAR ≈ 0.401 vs TG AR GAR ≈ 0.047。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"SS 贡献 ~8.5× 提升。ThreadGate 贡献边际。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"SS Llama 残留 2.9× gap 说明 exposure bias 可能非唯一因素。Abstract 'substantially' 模糊。\"\n  action_items:\n    - round: 4\n      action: \"3 seeds (s42/s123/s456) + mean±std\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2 — status updates through Round 6\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——contribution 措辞需调整\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 4\n      reviewers: [2]\n      note: \"'to our knowledge, the first' 仍被质疑。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"因果排除链不完整（KV cache drift + NTP magnitude imbalance 未排除）。强共识 Must-Fix。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"[复发 ×6 轮] 'causal exclusion' 措辞强共识必须修改。R1 从方法论（magnitude未排除），R2 从术语精确性（非interventionist causal inference）。建议→'diagnostic exclusion chain'/'systematic ablation-based exclusion'。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 4\n      action: \"GAR 重新定位为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"Phase 2 switching 实验 + exposure bias 降级为 'a proximal cause'\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"[复发 ×6 轮] 全文 'causal exclusion'→'diagnostic exclusion chain' 术语替换已完成。等 λ_GAR + switching 实验结果后由 Paper Agent 重构排除链叙事。\"\n      assigned_to: paper_agent\n      status: done\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"'Destroys' 与 r²=0.04 不匹配。需降调。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"维持 Should-Fix。标题需降调以匹配 evidence 强度。\"\n  action_items:\n    - round: 5\n      action: \"标题 'Destroys' → 'Collapses'（描述 attention 行为而非下游灾难）\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"arXiv 原文验证确认。Critical Must-Fix。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未提及。待确认修复状态。\"\n  action_items:\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因——替代假说讨论不足\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 降 Should-Fix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"PCGrad 失败可能反映投影副作用。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[复发 ×4 轮] 强共识 Must-Fix。KV cache drift + Appendix L 非独立验证。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"[复发 ×5 轮] R1 交叉回应明确：λ_GAR rescaling 缺失使 exposure bias 归因无法与梯度幅值淹没假说区分。SS Llama 2.9× 残留进一步说明可能有其他因素。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"§6 扩展 exposure bias 讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 5\n      action: \"Phase 2 switching 实验区分 exposure bias vs KV cache drift\"\n      assigned_to: agent\n      status: in_progress\n    - round: 6\n      action: \"λ_GAR rescaling (7B λ=10 + 1.5B λ∈{1,8,15}) + TF→AR switching eval + Discussion 段落\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标——instruction retention 不显著但占页过多\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"McNemar p=0.077 不显著。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200 的 95% CI ≈ [0.05, 0.35] 过宽。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"[复发 ×5 轮] 升级为 Must-Fix。r²=0.04 仅解释 4% 下游方差。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"[复发 ×6 轮] R2 补充：per-category 高度分化——仅 content constraints +23.8pp 显著，format/count/position 无变化。R1 交叉强烈同意。\"\n  action_items:\n    - round: 4\n      action: \"重新定位 GAR 为 diagnostic probe\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"标题 Destroys→Collapses + 叙事重构\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"§6 新段落：GAR as diagnostic probe 独立价值论证 + proxy 局限讨论（r²=0.04 + per-category 分化）\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"Raposo et al. 缺 ICML 2024 venue；Gromov et al. 年份问题。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 4\n      action: \"统一 bib 格式\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"论文 p.1 Abstract 已有 anonymous.4open.science 链接。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: done\n  resolution: \"论文 p.1 已有匿名代码链接。\"\n  resolution_round: 5\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 AR 列需扩容\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1]\n      note: \"与 R1-N2 联动，AR 列需 N≥50 + CI。\"\n    - round: 6\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 4\n      action: \"AR 列更新为 N≥50 数据 + CI + GAR-D + PPL\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字重复 8+ 次\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"仍存在。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1 交叉回应 rebut——认为核心 effect size 在 Abstract/Intro/Results 重复是正常科学写作。\"\n  action_items:\n    - round: 5\n      action: \"Abstract/§4.2 保留完整数字，其余改用回指\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 泛化声称\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"'to our knowledge, the first' 仍被质疑。合并至 R2-N1 追踪。\"\n  action_items:\n    - round: 4\n      action: \"删除泛化声称，合并至 R2-N1\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. split-softmax 缺实验对比\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Discussion 定性讨论即可，不做实验对比。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 中加强 split-softmax/Rhea 概念对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure/Table caption overclaim + 重复句\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 6\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 3\n      action: \"修正 Fig 3b/Table 1/Fig 4 caption\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后数字更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 6\n      reviewers: []\n      note: \"仍待 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后统一更新\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 6\n      reviewers: []\n      note: \"SS 统计支撑仍为核心问题。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance\"\n      assigned_to: director\n      status: open\n\n# ============================================================\n# Issues from Round 3 — status updates through Round 6\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Round 4 确认页数合规。\"\n  resolution_round: 4\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad scope 过度概括\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"NTP magnitude imbalance 7.5-14.7× 是 PCGrad 失败的替代解释。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 交叉回应：即便改 'causal exclusion' 措辞，λ_GAR rescaling 缺失仍是实质问题。\"\n  action_items:\n    - round: 3\n      action: \"'gradient conflict' → 'gradient direction conflict'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"补充 1 句：PCGrad 不处理 magnitude imbalance\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869) 引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [2]\n      note: \"与 split-softmax 一并作为缺失对比方案。合并至 R2-W7-new。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 概念对比中一并覆盖 Rhea\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 未讨论\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2 同意 R1 (Q4)。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2-W3 新增：LoRA 限制模型重组 attention patterns capacity，可能 confound capacity 排除步骤。R1 交叉同意。\"\n  action_items:\n    - round: 5\n      action: \"§7 Limitations 加 1 句 acknowledge LoRA rank 16 可能影响 gate 效用上界\"\n      assigned_to: paper_agent\n      status: done\n    - round: 6\n      action: \"Limitations 扩展：LoRA-only 实验限制了 capacity 排除步骤的推断力度\"\n      assigned_to: paper_agent\n      status: done\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  action_items:\n    - round: 3\n      action: \"确认准确性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R3-NEW-1\"\n  summary: \"UG 描述不清——未说明仍为可学习 MLP\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  action_items:\n    - round: 3\n      action: \"§4.1 或 §3 加一句说明\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-NEW-2\"\n  summary: \"Contribution (4) 混淆开发迭代与系统消融\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  action_items:\n    - round: 3\n      action: \"拆分为 loss design iterations + systematic conditions comparison\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Issues from Round 4 — status updates through Round 6\n# ============================================================\n\n- id: \"R4-N1\"\n  summary: \"GAR 指标与下游任务性能之间缺乏因果验证\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"r=0.200, r²=0.04。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Director 裁定 Must-Fix。与 R2-W3 合并追踪。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 补充 per-category 分化证据。R1 交叉强烈同意。维持 Must-Fix。\"\n  action_items:\n    - round: 5\n      action: \"标题 Destroys→Collapses + GAR 叙事重构\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 6\n      action: \"§6 GAR as diagnostic probe 独立价值论证 + per-category 分化讨论\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-N2\"\n  summary: \"SS+LoRA-only 消融缺失——ThreadGate 独立贡献不清\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"关键缺失消融。\"\n  action_items:\n    - round: 5\n      action: \"SS+LoRA-only 实验\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R4-W1\"\n  summary: \"GAR-D 全条件接近零——干预仅在 last token 成功\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"§3.1 补充 GAR-ours vs GAR-D 选择理由\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-W2\"\n  summary: \"Table 1 四舍五入与正文数字精度不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  action_items:\n    - round: 4\n      action: \"Table 1 增加一位小数\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W3\"\n  summary: \"r_min 数值正文未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  action_items:\n    - round: 4\n      action: \"在 §3 或 Appendix A 中报告 r_min 数值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-MR1\"\n  summary: \"缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Missing References 中明确列出。\"\n  action_items:\n    - round: 5\n      action: \"合并至 R2-W7-new Discussion 概念对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R4-W4\"\n  summary: \"Appendix C instruction retention 多重比较未校正\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"18-category McNemar's test 缺 FDR/Bonferroni 校正。\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"m3 再次提出。per-category 分化进一步削弱未校正结果可信度。\"\n  action_items:\n    - round: 4\n      action: \"Appendix C per-category 分析补充 Holm-Bonferroni 或 FDR 校正\"\n      assigned_to: agent\n      status: in_progress\n\n# ============================================================\n# Round 5 — status updates through Round 6\n# ============================================================\n\n- id: \"R5-SF1\"\n  summary: \"β-steering 部分循环论证——GAR 恢复 vs 下游效果未解耦\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证首次提出。\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"boost attention → attention metric recovers 是同义反复。\"\n    - round: 6\n      reviewers: [1]\n      note: \"R1-S1 维持循环论证判断。\"\n  action_items:\n    - round: 5\n      action: \"§5.4 拆为两段：GAR 恢复标注 'by construction' + 下游效果单独报告\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# Round 6 新增\n# ============================================================\n\n- id: \"R6-SF1\"\n  summary: \"单一数据集（仅 UltraChat）限制 generalizability claim\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 列 Must-Fix，R1 rebut 降为 Should-Fix（诊断性论文单数据集可接受，UltraChat 18 种对话类型提供 domain diversity）。Director 裁定 Should-Fix——机制性发现依赖 training dynamics 而非数据，但 Limitations 需明确讨论。\"\n  action_items:\n    - round: 6\n      action: \"Limitations 明确讨论单数据集对 generalizability 的限制 + future work 承诺跨数据集验证\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Limitations 已添加 cross-dataset validation discussion。Reviewer 确认。\"\n  resolution_round: 6\n\n- id: \"R6-SF2\"\n  summary: \"SS Llama 残留 2.9× gap——Abstract 'substantially' 措辞模糊\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"强共识。Qwen 1.3× vs Llama 2.9× 差异显著。Abstract 应报告具体数字。可能暗示 Llama 上有 exposure bias 以外的因素。\"\n  action_items:\n    - round: 6\n      action: \"Abstract 改为具体数字 + §6 讨论 Llama 残留 gap 根因\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R6-SF3\"\n  summary: \"仅 LoRA fine-tuning，未验证 full fine-tuning\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 交叉同意。LoRA capacity 限制可能 confound capacity 排除步骤。合并至 R3-MINOR-1。\"\n  action_items:\n    - round: 6\n      action: \"Limitations 讨论 LoRA-only 限制（合并至 R3-MINOR-1 执行）\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Limitations 已添加 LoRA-only + capacity confound 讨论。Reviewer 确认。\"\n  resolution_round: 6\n\n- id: \"R6-SF4\"\n  summary: \"Dou et al. attention forcing 区分讨论不够深入\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 提出 3 点缺失讨论（AR 退化、retrospective 解释、方法论互补），R1 交叉同意。\"\n    - round: 6\n      reviewers: []\n      note: \"Reviewer 审查确认 Related Work 已有 3 点区分，但 3 个额外点（AR 退化/回溯解释/方法互补性）未见添加。优先级较低。\"\n  action_items:\n    - round: 6\n      action: \"Related Work/Discussion 增加 2-3 句 Dou et al. deeper connection\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R6-SF5\"\n  summary: \"Loss formulation 搜索（v1-v9）的过拟合风险\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"9 次迭代选 loss formulation 可能对 UltraChat 数据集过拟合。\"\n  action_items:\n    - round: 6\n      action: \"Appendix B 加 1 段 loss search overfitting caveat + TF-AR gap 在所有 variants 中均出现的反驳\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Appendix 已添加 Overfitting caveat 段落，论证 TF-AR gap 跨 variants 一致性。Reviewer 确认。\"\n  resolution_round: 6\n\n- id: \"R6-SF6\"\n  summary: \"SS 替代解释（curriculum effect）未排除\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"SS 改变训练动态不仅仅修复 exposure bias。\"\n  action_items:\n    - round: 6\n      action: \"§6 Discussion 加 1 段 SS curriculum effect 替代机制讨论\"\n      assigned_to: paper_agent\n      status: open",
      "numLines": 993,
      "startLine": 1,
      "totalLines": 993
    }
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the context. R6-SF4 refers to Dou et al.'s attention forcing work. They already have `dou2019attention` and `dou2022parallel` in the bib. The review issue is about deepening the discussion of Dou et al.'s attention forcing work in the Discussion section, not adding a new 2024 paper.

Let me also check if there is a 2024 version. But from the web search, there's no 2024 paper by Dou et al. on attention forcing. The existing papers are from 2019 and 2022.

The user's task says to search for "Dou et al. 

2024", but the actual papers are from 2019 and 2022. I should inform the user about this and proceed with the existing citations.

Now, looking at R6-SF4, the requirement is to strengthen the connection between Dou et al.'s work on attention mismatch during autoregressive generation and our exposure bias diagnosis. Their retrospective attention explanation aligns with our analysis of training-inference mismatch, and their intervention-based approach complements our diagnostic perspective. Let me check the existing discussion of Dou et al. in the paper to see where this deepening should occur.

I'm searching through the discussion and related work sections to find where Dou et al. is currently mentioned and how to integrate this connection more explicitly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "e66dd4be-b708-45ff-9951-66a86e78d594",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AKpQi8kzUXf7s6d3R7FGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13628,
      "cache_read_input_tokens": 42163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13628
      },
      "output_tokens": 10,
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

_source line 41_

Let me check where Dou et al. is currently cited in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "2c79640d-1d90-4d44-bebb-900f6f885d00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AKpQi8kzUXf7s6d3R7FGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13628,
      "cache_read_input_tokens": 42163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13628
      },
      "output_tokens": 10,
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

_source line 42_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ae375aPkau6tA52bthvkCg`</summary>

```json
{
  "pattern": "dou20",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "bccf7693-d792-4bb9-a519-d8909b4afeab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AKpQi8kzUXf7s6d3R7FGS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13628,
      "cache_read_input_tokens": 42163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13628
      },
      "output_tokens": 10,
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

_source line 43 · 2026-05-25T22:47:41.129Z_

<details><summary>↩ Tool result · `toolu_01Ae375aPkau6tA52bthvkCg`</summary>

```text
artifacts/dream_reports/dream_20260524T081135/best/paper.tex:78:[Omitted long matching line]
artifacts/dream_reports/dream_20260524T081135/best/paper.tex:421:[Omitted long matching line]
artifacts/dream_reports/dream_20260524T081135/best/paper.tex:460:\bibitem[Dou and Gales(2022)]{dou2022parallel}
artifacts/dream_reports/dream_20260524T081135/worst/paper.tex:84:[Omitted long matching line]
artifacts/dream_reports/dream_20260524T081135/worst/paper.tex:545:\bibitem[Dou and Gales(2022)]{dou2022parallel}
artifacts/dream_reports/dream_20260524T081135/median/paper.tex:60:[Omitted long matching line]
artifacts/dream_reports/dream_20260524T081135/median/paper.tex:421:\bibitem[Dou and Gales(2022)]{dou2022parallel}
paper/sections/related_work.tex:10:[Omitted long matching line]
docs/paper/sections/related_work.tex:10:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "d0625aa5-3167-4e9d-b76f-b5ea5cbd65b5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/dream_reports/dream_20260524T081135/best/paper.tex:78:[Omitted long matching line]\nartifacts/dream_reports/dream_20260524T081135/best/paper.tex:421:[Omitted long matching line]\nartifacts/dream_reports/dream_20260524T081135/best/paper.tex:460:\\bibitem[Dou and Gales(2022)]{dou2022parallel}\nartifacts/dream_reports/dream_20260524T081135/worst/paper.tex:84:[Omitted long matching line]\nartifacts/dream_reports/dream_20260524T081135/worst/paper.tex:545:\\bibitem[Dou and Gales(2022)]{dou2022parallel}\nartifacts/dream_reports/dream_20260524T081135/median/paper.tex:60:[Omitted long matching line]\nartifacts/dream_reports/dream_20260524T081135/median/paper.tex:421:\\bibitem[Dou and Gales(2022)]{dou2022parallel}\npaper/sections/related_work.tex:10:[Omitted long matching line]\ndocs/paper/sections/related_work.tex:10:[Omitted long matching line]",
    "numLines": 9
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_015AfwtJQHzrbZd7qrxKBNFP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "05cd7577-a6ea-4a79-8aa3-2d75873ec0cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Mv6EmDxvmUscexK54Dz5A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1087,
      "cache_read_input_tokens": 55791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1087
      },
      "output_tokens": 53,
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

_source line 45 · 2026-05-25T22:47:43.510Z_

<details><summary>↩ Tool result · `toolu_015AfwtJQHzrbZd7qrxKBNFP`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn dialogue and attention decay.}
4	Multi-turn coherence has been a persistent challenge from early dialogue systems \citep{li2016persona,roller2021recipes,zhang2020dialogpt} through modern long-context models \citep{xu2022goldfish}, with benchmarks such as MT-Bench \citep{zheng2024judging} and MT-Bench-101 \citep{bai2024mtbench101} continuing to expose quality gaps at later turns \citep{laban2025lost,liu2026intent}. Most relevant to our work, \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\% across 12 models while residual probes retain goal information (AUC\,=\,0.98). We observe a steeper 70.8\% decline on Qwen-2.5-7B. \citet{li2024measuring} independently quantified instruction instability and proposed split-softmax as an inference-time remedy. Our work differs in scope: we diagnose \emph{why} training-time attention optimization fails to transfer to inference, and provide the first training-time mitigation.
5	
6	\paragraph{Gating and attention manipulation.}
7	Residual gating spans highway networks \citep{srivastava2015highway}, ReZero \citep{bachlechner2021rezero}, layer pruning \citep{gromov2024unreasonable,fan2020layerdrop}, and adaptive depth \citep{schuster2022calm,raposo2024mixture}. Most relevant is Gated Attention \citep{qiu2025gated}: per-head sigmoid gates achieving MMLU \citep{hendrycks2021measuring} $+$2.03 at 15B scale; ThreadGate differs in conditioning on turn position. On the analysis side, head specialization \citep{clark2019what,voita2019analyzing,kovaleva2019revealing}, positional bias calibration \citep{liu2024lost,xiao2024streaming}, and attention steering (PASTA; \citealp{zhang2024tell}) address inference behavior; our $\beta$-steering serves a diagnostic role. PCGrad \citep{yu2020pcgrad} and CAGrad \citep{liu2021cagrad} treat gradient conflict as the root cause; we show direction conflict is a symptom, not the primary cause.
8	
9	\paragraph{Exposure bias in sequence models.}
10	Teacher forcing creates a distributional mismatch between training and inference \citep{wiseman2016sequence,arora2022exposure}. Scheduled sampling \citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \citep{ranzato2016sequence}, adversarial regularization \citep{lamb2016professor}, self-recovery analysis \citep{he2019exposure}, bridging strategies for neural machine translation (NMT; \citealp{zhang2019bridging}), and search-based training \citep{leblond2018searnn}. \citet{mihaylova2019scheduled} extended scheduled sampling to transformers for single-turn NMT. \citet{dou2019attention} proposed attention forcing (supervising cross-attention during NMT), and \citet{dou2022parallel} extended it with KL-divergence switching. Our work differs: (i)~time-scheduled sampling (linearly increasing $\rho$), not data-dependent; (ii)~self-attention in multi-turn dialogue, not cross-attention in NMT; (iii)~auxiliary attention objectives, not primary translation loss. No prior work examines exposure bias on \emph{auxiliary} attention objectives or provides multi-turn transformer mitigation; we fill both gaps.
11	
12	\begin{table*}[!t]
13	\centering
14	\small
15	\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\,=\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\leq$2\,pp spread); the 8--17$\times$ TF-AR gap persists across all configurations. $\bar{g}\!\pm\!\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
16	\label{tab:five-way}
17	\begin{tabular}{l ccc ccc cc c}
18	\toprule
19	& \multicolumn{3}{c}{\textbf{IID (TF)}} & \multicolumn{3}{c}{\textbf{Held-out (TF)}} & \multicolumn{2}{c}{\textbf{AR ($N$\,=\,50)}} & \\
20	\cmidrule(lr){2-4} \cmidrule(lr){5-7} \cmidrule(lr){8-9}
21	\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\% CI & $\bar{g}\!\pm\!\sigma_g$ \\
22	\midrule
23	\multicolumn{10}{l}{\emph{Baseline}} \\
24	Base              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\scriptsize[.014,\,.024]} & --- \\
25	\midrule
26	\multicolumn{10}{l}{\emph{Gated variants}} \\
27	ThreadGate        & 0.49 & \textbf{0.02} & 2.63 & 0.50 & \textbf{0.02} & 2.78 & \textbf{0.064} & {\scriptsize[.041,\,.091]} & .93\,{\scriptsize$\pm$\,.05} \\
28	\;+\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\scriptsize[.023,\,.038]} & --- \\
29	Uniform Gate      & 0.49 & 0.01 & 2.62 & \textbf{0.51} & 0.01 & 2.78 & 0.033 & {\scriptsize[.025,\,.043]} & .96\,{\scriptsize$\pm$\,.05} \\
30	\midrule
31	\multicolumn{10}{l}{\emph{Ungated}} \\
32	LoRA-only         & 0.49 & 0.01 & 2.63 & 0.50 & 0.01 & 2.78 & 0.037 & {\scriptsize[.027,\,.050]} & 1.00 \\
33	\bottomrule
34	\end{tabular}
35	\end{table*}
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "aa3eeb49-6e66-4173-b35b-8667a880da05",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Multi-turn dialogue and attention decay.}\nMulti-turn coherence has been a persistent challenge from early dialogue systems \\citep{li2016persona,roller2021recipes,zhang2020dialogpt} through modern long-context models \\citep{xu2022goldfish}, with benchmarks such as MT-Bench \\citep{zheng2024judging} and MT-Bench-101 \\citep{bai2024mtbench101} continuing to expose quality gaps at later turns \\citep{laban2025lost,liu2026intent}. Most relevant to our work, \\citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\\% across 12 models while residual probes retain goal information (AUC\\,=\\,0.98). We observe a steeper 70.8\\% decline on Qwen-2.5-7B. \\citet{li2024measuring} independently quantified instruction instability and proposed split-softmax as an inference-time remedy. Our work differs in scope: we diagnose \\emph{why} training-time attention optimization fails to transfer to inference, and provide the first training-time mitigation.\n\n\\paragraph{Gating and attention manipulation.}\nResidual gating spans highway networks \\citep{srivastava2015highway}, ReZero \\citep{bachlechner2021rezero}, layer pruning \\citep{gromov2024unreasonable,fan2020layerdrop}, and adaptive depth \\citep{schuster2022calm,raposo2024mixture}. Most relevant is Gated Attention \\citep{qiu2025gated}: per-head sigmoid gates achieving MMLU \\citep{hendrycks2021measuring} $+$2.03 at 15B scale; ThreadGate differs in conditioning on turn position. On the analysis side, head specialization \\citep{clark2019what,voita2019analyzing,kovaleva2019revealing}, positional bias calibration \\citep{liu2024lost,xiao2024streaming}, and attention steering (PASTA; \\citealp{zhang2024tell}) address inference behavior; our $\\beta$-steering serves a diagnostic role. PCGrad \\citep{yu2020pcgrad} and CAGrad \\citep{liu2021cagrad} treat gradient conflict as the root cause; we show direction conflict is a symptom, not the primary cause.\n\n\\paragraph{Exposure bias in sequence models.}\nTeacher forcing creates a distributional mismatch between training and inference \\citep{wiseman2016sequence,arora2022exposure}. Scheduled sampling \\citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \\citep{ranzato2016sequence}, adversarial regularization \\citep{lamb2016professor}, self-recovery analysis \\citep{he2019exposure}, bridging strategies for neural machine translation (NMT; \\citealp{zhang2019bridging}), and search-based training \\citep{leblond2018searnn}. \\citet{mihaylova2019scheduled} extended scheduled sampling to transformers for single-turn NMT. \\citet{dou2019attention} proposed attention forcing (supervising cross-attention during NMT), and \\citet{dou2022parallel} extended it with KL-divergence switching. Our work differs: (i)~time-scheduled sampling (linearly increasing $\\rho$), not data-dependent; (ii)~self-attention in multi-turn dialogue, not cross-attention in NMT; (iii)~auxiliary attention objectives, not primary translation loss. No prior work examines exposure bias on \\emph{auxiliary} attention objectives or provides multi-turn transformer mitigation; we fill both gaps.\n\n\\begin{table*}[!t]\n\\centering\n\\small\n\\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\\,=\\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\\leq$2\\,pp spread); the 8--17$\\times$ TF-AR gap persists across all configurations. $\\bar{g}\\!\\pm\\!\\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \\citep{dongre2026attention}.}\n\\label{tab:five-way}\n\\begin{tabular}{l ccc ccc cc c}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{IID (TF)}} & \\multicolumn{3}{c}{\\textbf{Held-out (TF)}} & \\multicolumn{2}{c}{\\textbf{AR ($N$\\,=\\,50)}} & \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7} \\cmidrule(lr){8-9}\n\\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\\% CI & $\\bar{g}\\!\\pm\\!\\sigma_g$ \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Baseline}} \\\\\nBase              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\\scriptsize[.014,\\,.024]} & --- \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Gated variants}} \\\\\nThreadGate        & 0.49 & \\textbf{0.02} & 2.63 & 0.50 & \\textbf{0.02} & 2.78 & \\textbf{0.064} & {\\scriptsize[.041,\\,.091]} & .93\\,{\\scriptsize$\\pm$\\,.05} \\\\\n\\;+\\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\\scriptsize[.023,\\,.038]} & --- \\\\\nUniform Gate      & 0.49 & 0.01 & 2.62 & \\textbf{0.51} & 0.01 & 2.78 & 0.033 & {\\scriptsize[.025,\\,.043]} & .96\\,{\\scriptsize$\\pm$\\,.05} \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Ungated}} \\\\\nLoRA-only         & 0.49 & 0.01 & 2.63 & 0.50 & 0.01 & 2.78 & 0.037 & {\\scriptsize[.027,\\,.050]} & 1.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 36,
      "startLine": 1,
      "totalLines": 36
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context. Let me summarize:

1. **No 2024 paper by Dou et al. exists.** The existing papers are from 2019 (arXiv:1909.12289) and 2022 (arXiv:2211.03237). Both are already in the bib file.

2. **R6-SF4 asks for deeper discussion of Dou et al.'s attention forcing** in the Discussion section, covering:
   - AR degradation: attention mismatch during autoregressive generation
   - Retrospective explanation: consistency with exposure bias diagnosis
   - Methodological complementarity: intervention vs diagnosis

3. The Related Work already mentions Dou et al. but only covers the methodological differences (cross-attention vs self-attention, NMT vs dialogue, etc.). The Discussion section needs to add the deeper connection requested.

For the edits, I should add 2-3 sentences to `paper/sections/discussion.tex` that connect Dou et al.'s attention forcing mechanism to our exposure bias findings. The best placement is after the first paragraph where we discuss GAR collapse and exposure bias, or near the end where we discuss inference-time remedies. This will show how their intervention approach complements our diagnostic perspective on the same underlying problem. TP self-recovery vs GAR failure, selectivity
- Para 2: Diagnostic exclusion, PCGrad, inference-time remedies (SS vs inference)
- Para 3: GAR independent diagnostic value, per-category effects
- Para 4: SS curriculum learning alternative explanation

The best place would be after paragraph 1 or within paragraph 2, where exposure bias and inference-time remedies are discussed. Or I could add a new short paragraph after paragraph 1.

Dou et al.'s attention forcing addresses the same core problem we're examining—attention patterns learned under teacher forcing fail to generalize to autoregressive generation due to training-inference mismatch. Their proposed solution intervenes at training time by supervising attention, whereas our work diagnoses why this degradation occurs and demonstrates that the failure persists even when mitigation strategies are applied. This methodological complementarity suggests the issue runs deeper than attention supervision alone can resolve.

For the longer discussion version, I'm looking at how to integrate this without disrupting the existing structure around fundamental incompatibilities and future directions. I've already reviewed both files, so let me verify they're identical before making changes. The user wants me to update both `paper/sections/discussion.tex` and `docs/paper/sections/discussion.tex` since they should contain the same content, plus I need to handle the longer version in `docs/paper/discussion.tex` separately.

Now I'm drafting the addition about attention forcing and teacher forcing to insert after the second paragraph, where the discussion of exposure bias and training-inference mismatch naturally fits. Our findings align with prior work on attention forcing in neural machine translation, where researchers observed that attention patterns degrade during autoregressive generation—a phenomenon that mirrors the exposure bias mechanism we identify in dialogue systems. While their approach intervenes directly on attention supervision to address the training-inference mismatch, our results suggest this mismatch runs deeper: even when attention objectives are jointly trained with the main task, the teacher-forcing gap persists, indicating that attention-level corrections alone cannot overcome the structural limitations of the training paradigm.

Now I'm deciding where to insert this connection in the discussion section. The first paragraph establishes the GAR collapse phenomenon, the second covers inference-time remedies and exposure bias, and I think placing this new text after the second paragraph flows naturally—it extends the exposure bias discussion before moving into the diagnostic value of our GAR analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "845eaaef-bf35-46b3-887f-d39bd99860ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8pbYnhpjvFEBd7kaWwbw8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 56878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
      },
      "output_tokens": 10,
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

_source line 47_

No 2024 paper by Dou et al. on attention forcing exists — the relevant papers are from 2019 and 2022, both already in the bib. The task is really about R6-SF4: deepening the discussion of Dou et al.'s attention forcing connection. I'll add the 2-3 sentences to both `paper/sections/discussion.tex` and `docs/paper/sections/discussion.tex`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "65513235-6f54-485f-b001-9435ae3b9c32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8pbYnhpjvFEBd7kaWwbw8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 56878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
      },
      "output_tokens": 10,
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

<details open><summary>🔧 Tool call — Edit · `toolu_01CiuTDiXW1wvVRpER6UdACs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex",
  "old_string": "At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Despite the weak GAR--compliance correlation",
  "new_string": "At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Our findings resonate with the attention forcing framework \\citep{dou2019attention,dou2022parallel}, which independently observed that attention patterns learned under teacher forcing degrade during autoregressive generation in NMT---a diagnosis consistent with the exposure bias mechanism we identify in multi-turn dialogue. Where attention forcing intervenes by supervising cross-attention to correct the training--inference mismatch, our work reveals that the mismatch persists even when auxiliary self-attention objectives are jointly optimized with NTP, suggesting that the teacher-forcing gap poses a structural obstacle beyond what single-task attention supervision addresses.\n\n\\looseness=-1 Despite the weak GAR--compliance correlation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "5fd926e0-cb7a-407b-8e11-9b942578ed57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8pbYnhpjvFEBd7kaWwbw8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 56878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
      },
      "output_tokens": 10,
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

_source line 49 · 2026-05-25T22:48:40.122Z_

<details><summary>↩ Tool result · `toolu_01CiuTDiXW1wvVRpER6UdACs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "d400cb48-d6da-45ec-aa17-e96fef5402a4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex",
    "oldString": "At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Despite the weak GAR--compliance correlation",
    "newString": "At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Our findings resonate with the attention forcing framework \\citep{dou2019attention,dou2022parallel}, which independently observed that attention patterns learned under teacher forcing degrade during autoregressive generation in NMT---a diagnosis consistent with the exposure bias mechanism we identify in multi-turn dialogue. Where attention forcing intervenes by supervising cross-attention to correct the training--inference mismatch, our work reveals that the mismatch persists even when auxiliary self-attention objectives are jointly optimized with NTP, suggesting that the teacher-forcing gap poses a structural obstacle beyond what single-task attention supervision addresses.\n\n\\looseness=-1 Despite the weak GAR--compliance correlation",
    "originalFile": "\\section{Discussion}\\label{sec:discussion}\n\n\\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \\citep{he2019exposure}; GAR optimizes a \\emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\\leq}$1.3$\\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\\,=\\,0.743; Appendix~\\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.\n\n\\looseness=-1 Our diagnostic exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\\S\\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\\times$ NTP dominance; \\citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\\,=\\,0.200; Appendix~\\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\\beta$-steering is likewise a \\emph{diagnostic}, distinct from inference-time remedies such as split-softmax \\citep{li2024measuring} and Rhea \\citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Despite the weak GAR--compliance correlation ($r^2$\\,=\\,0.04), GAR retains independent diagnostic value: it directly quantifies how exposure bias reshapes attention allocation toward goal tokens, a mechanism invisible to surface-level compliance metrics. The downstream effect is category-dependent---content-constrained instructions benefit substantially (+23.8\\,pp under $\\beta$\\,=\\,3 steering) while format, count, and positional constraints show no change, suggesting that the attention shift GAR captures is necessary only for tasks requiring sustained reference to earlier context.\n\n\\looseness=-1 We note that SS's benefit may partly reflect a curriculum learning effect---the linear schedule progressively increases difficulty by exposing more model-generated tokens---rather than a pure exposure bias correction. However, the core SS mechanism (substituting model generations for ground-truth prefixes) directly instantiates the definition of exposure bias mitigation, and the resulting gap compression is consistent across seeds and architectures.\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 6,
        "newStart": 4,
        "newLines": 8,
        "lines": [
          " ",
          " \\looseness=-1 Our diagnostic exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\\S\\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\\times$ NTP dominance; \\citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\\,=\\,0.200; Appendix~\\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\\beta$-steering is likewise a \\emph{diagnostic}, distinct from inference-time remedies such as split-softmax \\citep{li2024measuring} and Rhea \\citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).",
          " ",
          "+\\looseness=-1 Our findings resonate with the attention forcing framework \\citep{dou2019attention,dou2022parallel}, which independently observed that attention patterns learned under teacher forcing degrade during autoregressive generation in NMT---a diagnosis consistent with the exposure bias mechanism we identify in multi-turn dialogue. Where attention forcing intervenes by supervising cross-attention to correct the training--inference mismatch, our work reveals that the mismatch persists even when auxiliary self-attention objectives are jointly optimized with NTP, suggesting that the teacher-forcing gap poses a structural obstacle beyond what single-task attention supervision addresses.",
          "+",
          " \\looseness=-1 Despite the weak GAR--compliance correlation ($r^2$\\,=\\,0.04), GAR retains independent diagnostic value: it directly quantifies how exposure bias reshapes attention allocation toward goal tokens, a mechanism invisible to surface-level compliance metrics. The downstream effect is category-dependent---content-constrained instructions benefit substantially (+23.8\\,pp under $\\beta$\\,=\\,3 steering) while format, count, and positional constraints show no change, suggesting that the attention shift GAR captures is necessary only for tasks requiring sustained reference to earlier context.",
          " ",
          " \\looseness=-1 We note that SS's benefit may partly reflect a curriculum learning effect---the linear schedule progressively increases difficulty by exposing more model-generated tokens---rather than a pure exposure bias correction. However, the core SS mechanism (substituting model generations for ground-truth prefixes) directly instantiates the definition of exposure bias mitigation, and the resulting gap compression is consistent across seeds and architectures."
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

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_013KdSSniKqL72kfFWSa7LwB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex",
  "old_string": "At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Despite the weak GAR--compliance correlation",
  "new_string": "At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Our findings resonate with the attention forcing framework \\citep{dou2019attention,dou2022parallel}, which independently observed that attention patterns learned under teacher forcing degrade during autoregressive generation in NMT---a diagnosis consistent with the exposure bias mechanism we identify in multi-turn dialogue. Where attention forcing intervenes by supervising cross-attention to correct the training--inference mismatch, our work reveals that the mismatch persists even when auxiliary self-attention objectives are jointly optimized with NTP, suggesting that the teacher-forcing gap poses a structural obstacle beyond what single-task attention supervision addresses.\n\n\\looseness=-1 Despite the weak GAR--compliance correlation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "9c7d0f17-fe16-4f39-8acb-9d994e788888",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8pbYnhpjvFEBd7kaWwbw8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 56878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
      },
      "output_tokens": 10,
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

_source line 51 · 2026-05-25T22:48:42.664Z_

<details><summary>↩ Tool result · `toolu_013KdSSniKqL72kfFWSa7LwB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "de328e80-78f0-4f55-ba78-073b117d80fb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex",
    "oldString": "At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Despite the weak GAR--compliance correlation",
    "newString": "At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Our findings resonate with the attention forcing framework \\citep{dou2019attention,dou2022parallel}, which independently observed that attention patterns learned under teacher forcing degrade during autoregressive generation in NMT---a diagnosis consistent with the exposure bias mechanism we identify in multi-turn dialogue. Where attention forcing intervenes by supervising cross-attention to correct the training--inference mismatch, our work reveals that the mismatch persists even when auxiliary self-attention objectives are jointly optimized with NTP, suggesting that the teacher-forcing gap poses a structural obstacle beyond what single-task attention supervision addresses.\n\n\\looseness=-1 Despite the weak GAR--compliance correlation",
    "originalFile": "\\section{Discussion}\\label{sec:discussion}\n\n\\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \\citep{he2019exposure}; GAR optimizes a \\emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\\leq}$1.3$\\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\\,=\\,0.743; Appendix~\\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.\n\n\\looseness=-1 Our diagnostic exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\\S\\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\\times$ NTP dominance; \\citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\\,=\\,0.200; Appendix~\\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\\beta$-steering is likewise a \\emph{diagnostic}, distinct from inference-time remedies such as split-softmax \\citep{li2024measuring} and Rhea \\citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n\n\\looseness=-1 Despite the weak GAR--compliance correlation ($r^2$\\,=\\,0.04), GAR retains independent diagnostic value: it directly quantifies how exposure bias reshapes attention allocation toward goal tokens, a mechanism invisible to surface-level compliance metrics. The downstream effect is category-dependent---content-constrained instructions benefit substantially (+23.8\\,pp under $\\beta$\\,=\\,3 steering) while format, count, and positional constraints show no change, suggesting that the attention shift GAR captures is necessary only for tasks requiring sustained reference to earlier context.\n\n\\looseness=-1 We note that SS's benefit may partly reflect a curriculum learning effect---the linear schedule progressively increases difficulty by exposing more model-generated tokens---rather than a pure exposure bias correction. However, the core SS mechanism (substituting model generations for ground-truth prefixes) directly instantiates the definition of exposure bias mitigation, and the resulting gap compression is consistent across seeds and architectures.\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 6,
        "newStart": 4,
        "newLines": 8,
        "lines": [
          " ",
          " \\looseness=-1 Our diagnostic exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\\S\\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\\times$ NTP dominance; \\citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\\,=\\,0.200; Appendix~\\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\\beta$-steering is likewise a \\emph{diagnostic}, distinct from inference-time remedies such as split-softmax \\citep{li2024measuring} and Rhea \\citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).",
          " ",
          "+\\looseness=-1 Our findings resonate with the attention forcing framework \\citep{dou2019attention,dou2022parallel}, which independently observed that attention patterns learned under teacher forcing degrade during autoregressive generation in NMT---a diagnosis consistent with the exposure bias mechanism we identify in multi-turn dialogue. Where attention forcing intervenes by supervising cross-attention to correct the training--inference mismatch, our work reveals that the mismatch persists even when auxiliary self-attention objectives are jointly optimized with NTP, suggesting that the teacher-forcing gap poses a structural obstacle beyond what single-task attention supervision addresses.",
          "+",
          " \\looseness=-1 Despite the weak GAR--compliance correlation ($r^2$\\,=\\,0.04), GAR retains independent diagnostic value: it directly quantifies how exposure bias reshapes attention allocation toward goal tokens, a mechanism invisible to surface-level compliance metrics. The downstream effect is category-dependent---content-constrained instructions benefit substantially (+23.8\\,pp under $\\beta$\\,=\\,3 steering) while format, count, and positional constraints show no change, suggesting that the attention shift GAR captures is necessary only for tasks requiring sustained reference to earlier context.",
          " ",
          " \\looseness=-1 We note that SS's benefit may partly reflect a curriculum learning effect---the linear schedule progressively increases difficulty by exposing more model-generated tokens---rather than a pure exposure bias correction. However, the core SS mechanism (substituting model generations for ground-truth prefixes) directly instantiates the definition of exposure bias mitigation, and the resulting gap compression is consistent across seeds and architectures."
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

_source line 52_

完成。

**搜索结果**：不存在 "Dou et al. 2024" 的 attention forcing 论文。相关论文为 Dou et al. 2019（arXiv:1909.12289）和 Dou & Gales 2022（arXiv:2211.03237），两篇已在 bib 中。

**编辑内容**：在两份 `discussion.tex` 的第 2 段后新增 1 段（2 句），覆盖 R6-SF4 的 3 点要求：
1. **AR 退化**：Dou et al. 独立观察到 teacher forcing 下学到的 attention 在 AR 推理时退化
2. **回溯解释**：他们的诊断与我们的 exposure bias 发现一致
3. **方法论互补**：他们 intervene（监督 cross-attention），我们 diagnose（揭示 self-attention 辅助目标在 NTP 联合训练下仍无法迁移）——互补视角，共同指向 teacher-forcing gap 的结构性障碍

Sources:
- [Attention Forcing for Sequence-to-sequence Model Training](https://arxiv.org/abs/1909.12289)
- [Parallel Attention Forcing for Machine Translation](https://arxiv.org/abs/2211.03237)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "uuid": "4fa50119-2162-4eab-90f3-d2021a44f654",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JK1k9oZhgE33MmybU5sMcz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3008,
      "cache_read_input_tokens": 58823,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3008
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

_source line 53_

完成。

**搜索结果**：不存在 "Dou et al. 2024" 的 attention forcing 论文。相关论文为 Dou et al. 2019（arXiv:1909.12289）和 Dou & Gales 2022（arXiv:2211.03237），两篇已在 bib 中。

**编辑内容**：在两份 `discussion.tex` 的第 2 段后新增 1 段（2 句），覆盖 R6-SF4 的 3 点要求：
1. **AR 退化**：Dou et al. 独立观察到 teacher forcing 下学到的 attention 在 AR 推理时退化
2. **回溯解释**：他们的诊断与我们的 exposure bias 发现一致
3. **方法论互补**：他们 intervene（监督 cross-attention），我们 diagnose（揭示 self-attention 辅助目标在 NTP 联合训练下仍无法迁移）——互补视角，共同指向 teacher-forcing gap 的结构性障碍

Sources:
- [Attention Forcing for Sequence-to-sequence Model Training](https://arxiv.org/abs/1909.12289)
- [Parallel Attention Forcing for Machine Translation](https://arxiv.org/abs/2211.03237)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 165225,
  "duration_api_ms": 169386,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "a95abbf7-cbe6-4aed-8c87-f0d3f96b7777",
  "total_cost_usd": 0.8611833999999999,
  "usage": {
    "input_tokens": 11677,
    "cache_creation_input_tokens": 49990,
    "cache_read_input_tokens": 372231,
    "output_tokens": 5687,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 49990,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 373,
        "cache_read_input_tokens": 58823,
        "cache_creation_input_tokens": 3008,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3008
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 80245,
      "outputTokens": 1899,
      "cacheReadInputTokens": 15454,
      "cacheCreationInputTokens": 16628,
      "webSearchRequests": 5,
      "costUSD": 0.1620704,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11677,
      "outputTokens": 5687,
      "cacheReadInputTokens": 372231,
      "cacheCreationInputTokens": 49990,
      "webSearchRequests": 0,
      "costUSD": 0.699113,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "72799b9c-a79e-4b68-b4f9-04983a8231a9"
}
```

</details>

---
